#!/usr/bin/env python3
"""
generate_queries.py - compile every catalogued detection to Sentinel KQL and Splunk SPL.

Sigma is the authoritative source format where a rule exists; the catalog row is the
fallback for detections that are currently specification-only. Both paths emit a query
per target so the whole catalog is deployable, and every generated file carries a header
naming its OTD ID, source artifact, and the field mapping applied.

Field mapping is the part that actually matters. OT telemetry does not land in a single
schema, so this compiles against a declared table/index per data-source class rather than
pretending one mapping fits all. Placeholders in ANGLE BRACKETS are deliberate: they are
the environment-specific values (zone CIDRs, authorized masters, tag prefixes) that must
be baselined locally. A query with placeholders left in will run but will not be correct.

Outputs : 02-detection/queries/sentinel/<OTD_ID>__<slug>.kql
          02-detection/queries/splunk/<OTD_ID>__<slug>.spl
          02-detection/catalog/query-index.csv

Usage:  python3 tools/generate_queries.py
"""
import csv
import os
import re

import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ---------------------------------------------------------------------------
# Data-source class -> (Sentinel table, Splunk index/sourcetype, key time field)
# ---------------------------------------------------------------------------
SOURCE_MAP = {
    "ics-network":  ("OTNetwork_CL",      "index=ot_network",        "TimeGenerated"),
    "modbus":       ("OTNetwork_CL",      "index=ot_network sourcetype=zeek:modbus",  "TimeGenerated"),
    "dnp3":         ("OTNetwork_CL",      "index=ot_network sourcetype=zeek:dnp3",    "TimeGenerated"),
    "s7comm":       ("OTNetwork_CL",      "index=ot_network sourcetype=zeek:s7comm",  "TimeGenerated"),
    "iec104":       ("OTNetwork_CL",      "index=ot_network sourcetype=zeek:iec104",  "TimeGenerated"),
    "opcua":        ("OTNetwork_CL",      "index=ot_network sourcetype=zeek:opcua",   "TimeGenerated"),
    "enip":         ("OTNetwork_CL",      "index=ot_network sourcetype=zeek:enip",    "TimeGenerated"),
    "conn":         ("OTNetwork_CL",      "index=ot_network sourcetype=zeek:conn",    "TimeGenerated"),
    "nozomi":       ("OTNozomi_CL",       "index=ot_nozomi sourcetype=nozomi:alert",  "TimeGenerated"),
    "historian":    ("OTHistorian_CL",    "index=ot_historian",      "TimeGenerated"),
    "windows":      ("SecurityEvent",     "index=wineventlog",       "TimeGenerated"),
    "sysmon":       ("Event",             "index=wineventlog sourcetype=XmlWinEventLog:Sysmon", "TimeGenerated"),
    "firewall":     ("CommonSecurityLog", "index=firewall",          "TimeGenerated"),
    "identity":     ("SigninLogs",        "index=wineventlog sourcetype=WinEventLog:Security", "TimeGenerated"),
    "flow":         ("CommonSecurityLog", "index=netflow",           "TimeGenerated"),
    "dns":          ("DnsEvents",         "index=dns",               "TimeGenerated"),
    "edr":          ("DeviceEvents",      "index=edr",               "TimeGenerated"),
    "default":      ("OTNetwork_CL",      "index=ot_network",        "TimeGenerated"),
}

# Sigma field name -> (Sentinel column, Splunk field)
FIELD_MAP = {
    "src_ip":        ("SourceIP", "src_ip"),
    "dst_ip":        ("DestinationIP", "dest_ip"),
    "id.orig_h":     ("SourceIP", "src_ip"),
    "id.resp_h":     ("DestinationIP", "dest_ip"),
    "id.resp_p":     ("DestinationPort", "dest_port"),
    "src_port":      ("SourcePort", "src_port"),
    "dst_port":      ("DestinationPort", "dest_port"),
    "function_code": ("FunctionCode", "function_code"),
    "func":          ("FunctionCode", "func"),
    "fc":            ("FunctionCode", "fc"),
    "sub_function":  ("SubFunction", "sub_function"),
    "type_id":       ("TypeId", "type_id"),
    "proto":         ("Protocol", "proto"),
    "protocol":      ("Protocol", "protocol"),
    "rosctr":        ("Rosctr", "rosctr"),
    "function":      ("FunctionName", "function"),
    "asdu_address":  ("AsduAddress", "asdu_address"),
    "ioa":           ("IOA", "ioa"),
    "user":          ("AccountName", "user"),
    "Image":         ("NewProcessName", "Image"),
    "CommandLine":   ("CommandLine", "CommandLine"),
    "EventID":       ("EventID", "EventCode"),
    "ComputerName":  ("Computer", "host"),
    "quantity":      ("Quantity", "quantity"),
    "address":       ("Address", "address"),
}


def slug(text, maxlen=60):
    s = re.sub(r"[^a-z0-9]+", "-", (text or "").lower()).strip("-")
    return s[:maxlen].strip("-")


def pick_source(data_source, protocol, library):
    """Choose a source-map key from whatever context the detection carries."""
    blob = f"{data_source} {protocol} {library}".lower()
    for key in ("modbus", "dnp3", "s7comm", "iec104", "opcua", "enip", "historian",
                "nozomi", "sysmon", "firewall", "dns", "edr"):
        if key in blob:
            return key
    if "ics-network" in blob or "zeek" in blob:
        return "ics-network"
    if "windows" in blob or "winevent" in blob:
        return "windows"
    if "ident" in blob or "auth" in blob or "vpn" in blob:
        return "identity"
    if "flow" in blob or "netflow" in blob:
        return "flow"
    if "endpoint" in blob or "edr" in blob:
        return "edr"
    if library == "perimeter":
        return "firewall"
    return "default"


def map_field(name, target):
    base = name.split("|")[0]
    mapped = FIELD_MAP.get(base)
    if mapped:
        return mapped[0] if target == "kql" else mapped[1]
    return base


def render_value(v):
    if isinstance(v, bool):
        return "true" if v else "false"
    if isinstance(v, (int, float)):
        return str(v)
    return f'"{v}"'


def build_conditions(selection, target):
    """Turn one Sigma selection block into a list of condition strings."""
    conds = []
    if not isinstance(selection, dict):
        return conds
    for key, val in selection.items():
        field = map_field(key, target)
        mods = key.split("|")[1:] if "|" in key else []
        values = val if isinstance(val, list) else [val]

        if "cidr" in mods:
            for v in values:
                if target == "kql":
                    conds.append(f'ipv4_is_in_range({field}, "{v}")')
                else:
                    conds.append(f'{field}="{v}"')
            continue
        if "contains" in mods:
            parts = []
            for v in values:
                parts.append(f'{field} contains "{v}"' if target == "kql"
                             else f'{field}="*{v}*"')
            conds.append("(" + (" or " if target == "kql" else " OR ").join(parts) + ")")
            continue
        if "startswith" in mods:
            parts = [f'{field} startswith "{v}"' if target == "kql" else f'{field}="{v}*"'
                     for v in values]
            conds.append("(" + (" or " if target == "kql" else " OR ").join(parts) + ")")
            continue

        if len(values) == 1:
            v = values[0]
            conds.append(f"{field} == {render_value(v)}" if target == "kql"
                         else f"{field}={render_value(v)}")
        else:
            if target == "kql":
                vals = ", ".join(render_value(v) for v in values)
                conds.append(f"{field} in ({vals})")
            else:
                vals = " OR ".join(f"{field}={render_value(v)}" for v in values)
                conds.append(f"({vals})")
    return conds


def sigma_to_queries(doc, otd, artifact):
    """Compile a Sigma rule to (kql, spl). Returns None if unparseable."""
    det = doc.get("detection")
    if not isinstance(det, dict):
        return None
    ls = doc.get("logsource") or {}
    src_key = pick_source(f"{ls.get('category','')} {ls.get('service','')}",
                          ls.get("product", ""), "")
    table, index, _ = SOURCE_MAP.get(src_key, SOURCE_MAP["default"])

    sel_blocks, filt_blocks = {}, {}
    for name, block in det.items():
        if name in ("condition", "timeframe"):
            continue
        low = name.lower()
        if low.startswith(("filter", "authorized", "allow", "exclu")):
            filt_blocks[name] = block
        else:
            sel_blocks[name] = block

    def compose(target):
        joiner_and = " and " if target == "kql" else " "
        sel_parts, filt_parts = [], []
        for block in sel_blocks.values():
            c = build_conditions(block, target)
            if c:
                sel_parts.append("(" + joiner_and.join(c) + ")")
        for block in filt_blocks.values():
            c = build_conditions(block, target)
            if c:
                filt_parts.append("(" + joiner_and.join(c) + ")")
        return sel_parts, filt_parts

    # ---- KQL ----
    sel, filt = compose("kql")
    kql = [f"// {otd} - {doc.get('title','')}",
           f"// Source: {artifact}",
           f"// ATT&CK for ICS: {', '.join(str(t) for t in (doc.get('tags') or []) if 't0' in str(t).lower()) or 'n/a'}",
           f"// Severity: {doc.get('level','medium')}",
           "// PLACEHOLDERS in <angle brackets> must be baselined before use.",
           "//",
           table]
    if sel:
        kql.append("| where " + " and ".join(sel))
    for f in filt:
        kql.append(f"| where not ({f})")
    tf = det.get("timeframe")
    if tf:
        kql.append(f"| summarize Count = count(), FirstSeen = min(TimeGenerated), "
                   f"LastSeen = max(TimeGenerated) by SourceIP, DestinationIP "
                   f"// original Sigma timeframe: {tf}")
    kql.append("| project TimeGenerated, SourceIP, DestinationIP, Protocol, "
               "FunctionCode, AccountName, Computer")
    kql.append("| order by TimeGenerated desc")

    # ---- SPL ----
    sel, filt = compose("spl")
    spl = [f"``` {otd} - {doc.get('title','')} ```",
           f"``` Source: {artifact} ```",
           f"``` Severity: {doc.get('level','medium')} ```",
           "``` PLACEHOLDERS in <angle brackets> must be baselined before use. ```",
           index]
    if sel:
        spl.append("  " + " ".join(sel))
    for f in filt:
        spl.append(f"  NOT {f}")
    spl.append("| table _time src_ip dest_ip protocol function_code user host")
    spl.append("| sort - _time")

    return "\n".join(kql) + "\n", "\n".join(spl) + "\n"


def catalog_to_queries(row):
    """Build a scaffold query for a detection that has no Sigma artifact yet."""
    otd, title = row["OTD_ID"], row["Title"]
    src_key = pick_source(row["Data_Source"], row["Protocol"], row["Library"])
    table, index, _ = SOURCE_MAP.get(src_key, SOURCE_MAP["default"])
    logic = row["Logic_Summary"] or row["Category"]
    attack = row["ATTACK_Technique_IDs"] or "n/a"

    kql = f"""// {otd} - {title}
// Library: {row['Library_Name']}  |  Legacy ID: {row['Legacy_ID']}
// ATT&CK for ICS: {attack}  |  Severity: {row['Severity']}
// Detection logic: {logic}
//
// STATUS: SCAFFOLD. This detection is catalogued as a specification; the logic below
// expresses the intent against the mapped table but MUST be completed and validated
// against real telemetry before deployment. Placeholders in <angle brackets> are
// environment-specific.
//
{table}
| where TimeGenerated > ago(24h)
// TODO: express the detection condition -- {logic}
| where isnotempty(SourceIP)
| summarize Count = count(), FirstSeen = min(TimeGenerated), LastSeen = max(TimeGenerated)
    by SourceIP, DestinationIP
| where Count > <THRESHOLD>
| order by Count desc
"""

    spl = f"""``` {otd} - {title} ```
``` Library: {row['Library_Name']}  |  Legacy ID: {row['Legacy_ID']} ```
``` ATT&CK for ICS: {attack}  |  Severity: {row['Severity']} ```
``` Detection logic: {logic} ```
``` STATUS: SCAFFOLD - complete and validate before deployment. ```
{index} earliest=-24h
``` TODO: express the detection condition -- {logic} ```
| stats count AS event_count, min(_time) AS first_seen, max(_time) AS last_seen
    BY src_ip dest_ip
| where event_count > <THRESHOLD>
| convert ctime(first_seen) ctime(last_seen)
| sort - event_count
"""
    return kql, spl


def main():
    cat_path = os.path.join(ROOT, "02-detection/catalog/master-detection-catalog.csv")
    with open(cat_path, newline="", encoding="utf-8") as fh:
        rows = list(csv.DictReader(fh))

    kql_dir = os.path.join(ROOT, "02-detection/queries/sentinel")
    spl_dir = os.path.join(ROOT, "02-detection/queries/splunk")
    os.makedirs(kql_dir, exist_ok=True)
    os.makedirs(spl_dir, exist_ok=True)

    index_rows = []
    compiled = scaffold = existing = 0

    for r in rows:
        otd, name = r["OTD_ID"], f"{r['OTD_ID']}__{r['Slug'] or slug(r['Title'])}"
        artifact = r["Artifact_Path"]
        kql = spl = None
        origin = "scaffold"

        # Historian detections already ship hand-written KQL/SPL - reference, don't overwrite
        if r["Library"] == "historian" and artifact:
            k = os.path.join(ROOT, artifact, "sentinel.kql")
            s = os.path.join(ROOT, artifact, "splunk.spl")
            if os.path.exists(k) and os.path.exists(s):
                index_rows.append([otd, r["Title"], r["Library_Name"], "authored",
                                   os.path.relpath(k, ROOT), os.path.relpath(s, ROOT)])
                existing += 1
                continue

        if artifact.endswith(".yml") and os.path.exists(os.path.join(ROOT, artifact)):
            try:
                with open(os.path.join(ROOT, artifact), encoding="utf-8") as fh:
                    doc = yaml.safe_load(fh) or {}
                out = sigma_to_queries(doc, otd, artifact)
                if out:
                    kql, spl = out
                    origin = "compiled-from-sigma"
                    compiled += 1
            except Exception:
                kql = None

        if kql is None:
            kql, spl = catalog_to_queries(r)
            scaffold += 1

        kp = os.path.join(kql_dir, f"{name}.kql")
        sp = os.path.join(spl_dir, f"{name}.spl")
        with open(kp, "w", encoding="utf-8") as fh:
            fh.write(kql)
        with open(sp, "w", encoding="utf-8") as fh:
            fh.write(spl)
        index_rows.append([otd, r["Title"], r["Library_Name"], origin,
                           os.path.relpath(kp, ROOT), os.path.relpath(sp, ROOT)])

    idx = os.path.join(ROOT, "02-detection/catalog/query-index.csv")
    with open(idx, "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["OTD_ID", "Title", "Library_Name", "Query_Origin",
                    "Sentinel_KQL_Path", "Splunk_SPL_Path"])
        w.writerows(index_rows)

    print(f"  compiled from Sigma : {compiled}")
    print(f"  scaffolded from spec: {scaffold}")
    print(f"  already authored    : {existing}")
    print(f"  total indexed       : {len(index_rows)}")
    print(f"\n  wrote query-index.csv")


if __name__ == "__main__":
    main()
