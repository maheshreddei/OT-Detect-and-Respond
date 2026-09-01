#!/usr/bin/env python3
"""
build_crosswalk.py - derive the cross-layer relationship files.

Generated, never hand-edited. Joins the five ID namespaces so the program can be
queried in either direction: from a threat down to the SPAN port, or from a budget
line up to the techniques it buys.

Chain: MVT -> CP -> TEL -> LS -> OTD (detection) -> ATT&CK / playbook

Usage:  python3 tools/build_crosswalk.py
"""
import csv
import os
import re
import glob
from collections import defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def read(path):
    full = os.path.join(ROOT, path)
    if not os.path.exists(full):
        return []
    with open(full, newline="", encoding="utf-8-sig") as fh:
        return list(csv.DictReader(fh))


def ids(v):
    return [x.strip() for x in (v or "").split(";") if x.strip()]


def write(path, header, rows):
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(header)
        w.writerows(rows)
    print(f"  wrote {path} ({len(rows)} rows)")


# Map a detection's data-source text to log source IDs
LS_HINTS = {
    "LS-02": ["firewall", "boundary", "perimeter", "flow", "netflow"],
    "LS-03": ["jump", "rdp", "ssh", "broker"],
    "LS-04": ["vpn", "remote access"],
    "LS-05": ["switch", "mac", "vlan", "wireless"],
    "LS-06": ["plc", "modbus", "s7", "controller"],
    "LS-07": ["sis", "safety", "tristation"],
    "LS-08": ["ews", "workstation", "sysmon", "windows", "endpoint", "edr", "engineering"],
    "LS-10": ["historian", "process data", "tag"],
    "LS-11": ["hmi", "scada", "operator"],
    "LS-12": ["ied", "61850", "goose"],
    "LS-14": ["identity", "auth", "account", "kerberos", "domain", "application"],
    "LS-17": ["rtu", "dnp3", "104"],
    "LS-18": ["ndr", "network", "zeek", "nozomi", "span", "tap", "conn", "ics-network",
              "opcua", "enip", "cip", "mqtt", "bacnet", "vnc", "ftp", "http"],
}


def infer_ls(row):
    blob = f"{row['Data_Source']} {row['Protocol']} {row['Category']} {row['Library']}".lower()
    hits = [ls for ls, kws in LS_HINTS.items() if any(k in blob for k in kws)]
    return sorted(set(hits)) or ["LS-18"]


def main():
    tel = read("01-telemetry/telemetry-hierarchy.csv")
    cp = read("01-telemetry/collection-plan.csv")
    mvt = read("01-telemetry/minimum-viable-telemetry.csv")
    ls = read("01-telemetry/log-source-inventory.csv")
    cat = read("02-detection/catalog/master-detection-catalog.csv")
    pbi = read("04-response/playbooks/playbook-index.csv")

    ls_by_id = {r["Source_ID"]: r for r in ls}

    # ---- 1. telemetry-to-logsource ----
    cp_by_tel = defaultdict(list)
    for r in cp:
        for t in ids(r["Maps_To_TEL"]):
            cp_by_tel[t].append(r["CP_ID"])
    mvt_by_ls = defaultdict(list)
    for r in mvt:
        for l in ids(r["Maps_To_LS"]):
            mvt_by_ls[l].append(r["MVT_ID"])

    rows = []
    for r in sorted(tel, key=lambda x: int(x["Rank"])):
        for lsid in ids(r["Maps_To_LS"]):
            s = ls_by_id.get(lsid, {})
            rows.append([r["TEL_ID"], r["Rank"], r["Source"], r["Hunt_Value"], r["Effort"],
                         lsid, s.get("Source", "UNKNOWN"), s.get("Onboarding_Tier", ""),
                         ";".join(cp_by_tel.get(r["TEL_ID"], [])),
                         ";".join(sorted(set(mvt_by_ls.get(lsid, [])))),
                         r["Collection_Pattern"]])
    write("05-crosswalk/telemetry-to-logsource.csv",
          ["TEL_ID", "Hunt_Rank", "Telemetry_Source", "Hunt_Value", "Effort", "LS_ID",
           "Log_Source", "Onboarding_Tier", "CP_IDs", "MVT_IDs", "Collection_Pattern"], rows)

    # ---- 2. detection-to-logsource ----
    det_ls = {}
    rows = []
    for r in cat:
        lsids = infer_ls(r)
        det_ls[r["OTD_ID"]] = lsids
        tiers = sorted({ls_by_id[l]["Onboarding_Tier"] for l in lsids if l in ls_by_id})
        rows.append([r["OTD_ID"], r["Title"], r["Library_Name"], ";".join(lsids),
                     ";".join(ls_by_id[l]["Source"] for l in lsids if l in ls_by_id),
                     ";".join(tiers), "Yes" if tiers and tiers[0] == "Tier 1" else "No"])
    write("05-crosswalk/detection-to-logsource.csv",
          ["OTD_ID", "Title", "Library_Name", "LS_IDs", "Log_Sources",
           "Onboarding_Tiers", "Reachable_At_Tier1"], rows)

    # ---- 3. detection-to-playbook ----
    # Two routing mechanisms: an explicit OTD reference inside the playbook text (strong),
    # and family routing by keyword (default). A playbook covers a CLASS of alert, so a
    # detection without an explicit mention still routes to the right procedure.
    FAMILY_ROUTES = [
        ("PLAYBOOK-OT-05", ["sis", "safety", "sif", "trip", "bypass", "voting", "tristation",
                            "interlock"]),
        ("PLAYBOOK-OT-03", ["program download", "logic", "firmware", "online edit",
                            "mode change", "operating mode", "project"]),
        ("PLAYBOOK-OT-01", ["engineering software", "engineering tool", "engineering workstation",
                            "change window", "tia", "studio 5000", "rslogix"]),
        ("PLAYBOOK-OT-02", ["setpoint", "parameter", "alarm", "tuning", "envelope", "limit"]),
        ("PLAYBOOK-OT-09", ["historian", "process data", "frozen", "replay", "divergence",
                            "sensor", "tag", "plausibility", "stale"]),
        ("PLAYBOOK-OT-06", ["remote access", "vpn", "jump host", "rdp", "vendor", "dormant",
                            "authentication", "logon", "credential", "account", "identity",
                            "brute", "password spray", "kerberos"]),
        ("PLAYBOOK-OT-04", ["malware", "ransomware", "yara", "virus", "trojan", "payload",
                            "phish", "removable media", "usb", "log cleared", "backup"]),
        ("PLAYBOOK-OT-08", ["new node", "new asset", "rogue", "new link", "first-time",
                            "unauthorized asset", "wireless", "rogue ap", "inventory",
                            "exposed", "internet accessible", "new client"]),
        ("PLAYBOOK-OT-07", ["write", "command", "function code", "restart", "stop",
                            "unsolicited", "control", "coil", "register", "asdu", "operate",
                            "modbus", "dnp3", "s7", "iec", "cip", "opc", "bacnet", "mqtt"]),
    ]

    pb_explicit = defaultdict(list)
    for r in pbi:
        for o in ids(r["Linked_OTD_IDs"]):
            pb_explicit[o].append(r["Playbook_ID"])

    def route(row):
        explicit = pb_explicit.get(row["OTD_ID"], [])
        blob = f"{row['Title']} {row['Category']} {row['Logic_Summary']} {row['Protocol']}".lower()
        family = [pb for pb, kws in FAMILY_ROUTES if any(k in blob for k in kws)]
        # Keep the highest-priority family route (list is ordered by escalation precedence)
        return explicit, family[:1]

    pb_by_otd = {}
    rows = []
    for r in cat:
        explicit, family = route(r)
        all_pb = sorted(set(explicit + family))
        pb_by_otd[r["OTD_ID"]] = all_pb
        rows.append([r["OTD_ID"], r["Title"], r["Severity"], ";".join(all_pb),
                     "explicit" if explicit else ("family" if family else "none"),
                     "Yes" if all_pb else "No"])
    write("05-crosswalk/detection-to-playbook.csv",
          ["OTD_ID", "Title", "Severity", "Playbook_IDs", "Routing", "Has_Playbook"], rows)

    # ---- 4. master-crosswalk: the full chain per detection ----
    qidx = {r["OTD_ID"]: r for r in read("02-detection/catalog/query-index.csv")}
    rows = []
    for r in cat:
        q = qidx.get(r["OTD_ID"], {})
        lsids = det_ls[r["OTD_ID"]]
        tiers = sorted({ls_by_id[l]["Onboarding_Tier"] for l in lsids if l in ls_by_id})
        rows.append([
            r["OTD_ID"], r["Title"], r["Library_Name"], r["Legacy_ID"],
            r["ATTACK_Technique_IDs"], r["Threat_Actors"], r["Sectors"],
            r["Purdue_Level"], r["Protocol"], r["Nozomi_Type_ID"], r["Severity"],
            ";".join(lsids), ";".join(tiers),
            ";".join(pb_by_otd.get(r["OTD_ID"], [])),
            q.get("Query_Origin", ""), q.get("Sentinel_KQL_Path", ""),
            q.get("Splunk_SPL_Path", ""), r["Artifact_Path"],
        ])
    write("05-crosswalk/master-crosswalk.csv",
          ["OTD_ID", "Title", "Library_Name", "Legacy_ID", "ATTACK_Technique_IDs",
           "Threat_Actors", "Sectors", "Purdue_Level", "Protocol", "Nozomi_Type_ID",
           "Severity", "LS_IDs", "Onboarding_Tiers", "Playbook_IDs", "Query_Origin",
           "Sentinel_KQL", "Splunk_SPL", "Sigma_Artifact"], rows)

    # ---- 5. coverage-rollup: what each log source unlocks ----
    det_by_ls = defaultdict(list)
    for otd, lsids in det_ls.items():
        for l in lsids:
            det_by_ls[l].append(otd)
    tech_by_otd = {r["OTD_ID"]: ids(r["ATTACK_Technique_IDs"].replace(",", ";")) for r in cat}
    rows = []
    for r in sorted(ls, key=lambda x: x["Source_ID"]):
        lsid = r["Source_ID"]
        dets = sorted(det_by_ls.get(lsid, []))
        techs = sorted({t for d in dets for t in tech_by_otd.get(d, []) if t.upper().startswith("T0")})
        rows.append([lsid, r["Source"], r["Onboarding_Tier"], r["Importance"],
                     r["Log_Ease"], len(dets), len(techs), ";".join(techs[:25])])
    write("05-crosswalk/coverage-rollup.csv",
          ["LS_ID", "Log_Source", "Onboarding_Tier", "Importance", "Log_Ease",
           "Detection_Count", "Technique_Count", "ATTACK_Technique_IDs"], rows)

    # ---- 6. ATT&CK coverage across the whole program ----
    tech_counts = defaultdict(list)
    for r in cat:
        for t in ids(r["ATTACK_Technique_IDs"].replace(",", ";")):
            t = t.strip().upper()
            m = re.search(r"T0\d{3}", t)
            if m:
                tech_counts[m.group(0)].append(r["OTD_ID"])
    rows = [[t, len(v), ";".join(sorted(v)[:20])] for t, v in sorted(tech_counts.items())]
    write("05-crosswalk/attack-coverage.csv",
          ["ATTACK_Technique_ID", "Detection_Count", "OTD_IDs"], rows)

    print("\nCrosswalk build complete.")


if __name__ == "__main__":
    main()
