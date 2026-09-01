#!/usr/bin/env python3
"""
build_catalog.py - merge every source library into one master detection catalog.

Assigns a unified OTD-#### ID to each distinct detection while preserving the
originating library and legacy ID, so nothing loses provenance. Known duplicates
across libraries are merged explicitly via MERGE_MAP (below) rather than guessed,
because a silent merge of two subtly different detections is worse than two rows.

Inputs   : source-libraries/*.csv (normalized exports), 02-detection/sigma/**/*.yml
Outputs  : 02-detection/catalog/master-detection-catalog.csv
           02-detection/catalog/merge-log.csv

Usage:  python3 tools/build_catalog.py
"""
import csv
import glob
import os
import re

import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ---------------------------------------------------------------------------
# Explicit merge map: legacy IDs that describe the SAME detection.
# Curated by hand - each group was compared on logic, not just title.
# The first entry in each tuple is the canonical/primary source.
# ---------------------------------------------------------------------------
MERGE_MAP = [
    # Modbus unauthorized write: use case + sigma rule + protocol catalog row
    ("OT-UC-0003", ["SIGMA:ot-ics-soc/01", "MOD-01"],
     "Same detection: Modbus write FC 5/6/15/16 from a source outside the authorized "
     "master allowlist. UC carries threat/sector context, Sigma carries portable logic, "
     "protocol catalog carries the NDR pattern."),
    # Modbus diagnostic restart
    ("OT-UC-0004", ["SIGMA:ot-ics-soc/02", "MOD-03"],
     "Same detection: Modbus FC08 diagnostic sub-function restart / force listen-only."),
    # DNP3 restart
    ("OT-UC-0007", ["SIGMA:ot-ics-soc/05", "DNP3-02"],
     "Same detection: DNP3 function code 13/14 cold or warm restart to an outstation."),
    # DNP3 disable unsolicited
    ("OT-UC-0008", ["SIGMA:ot-ics-soc/06", "DNP3-03"],
     "Same detection: DNP3 function 21 disabling unsolicited responses (blind the master)."),
    # S7comm stop CPU
    ("OT-UC-0005", ["SIGMA:ot-ics-soc/09", "S7-02"],
     "Same detection: S7comm PLC STOP / run-state change issued to a controller."),
    # IEC-104 unauthorized control
    ("OT-UC-0009", ["SIGMA:ot-ics-soc/13", "IEC104-02"],
     "Same detection: IEC 60870-5-104 control-direction ASDU from a non-authorized source."),
    # Network scan of OT
    ("OT-UC-0013", ["SCAN-01", "SCN-01"],
     "Same detection concept at two vantage points: horizontal scan across OT hosts. "
     "Perimeter library scores it on IT flow data, protocol library on OT NDR."),
    # SIS program mode / safety manipulation
    ("OT-UC-0017", ["SIS-B1", "SIGMA:it-dmz-ot-crosszone/20"],
     "Same detection: safety controller placed in PROGRAM mode or an SIS point forced/"
     "overridden. SIS library carries the functional-safety framing."),
    # Rogue EWS to controller
    ("OT-UC-0015", ["SIGMA:it-dmz-ot-crosszone/18", "SIGMA:it-dmz-ot-crosszone/07"],
     "Related detections merged: engineering/control protocol traffic to a controller "
     "from a host that is not an approved engineering workstation."),
    # New node in OT
    ("OT-UC-0014", ["SIGMA:it-dmz-ot-crosszone/23", "SIS-A4"],
     "Same detection at different scopes: first-time asset communication across a zone "
     "boundary / new node appearing in a monitored zone."),
]

LIBRARY_META = {
    "use-case":      ("OT Threat Content", "Threat-informed use case catalog"),
    "ot-ics-soc":    ("Sigma: OT/ICS SOC", "Protocol-level Sigma rules"),
    "it-dmz-ot-crosszone": ("Sigma: IT/DMZ/OT Cross-Zone", "Purdue zone-crossing Sigma rules"),
    "threat-actor":  ("Sigma: Threat Actor", "Actor-derived Sigma rules"),
    "advisory":      ("Sigma: CTI Advisory", "Advisory-derived Sigma rules (ME/GCC focus)"),
    "core-protocol": ("Sigma: Core Protocol", "Core protocol Sigma rules"),
    "protocol-ndr":  ("OT Protocol Defense (NDR)", "Protocol attack-surface detections"),
    "perimeter":     ("Perimeter-to-Endpoint", "IT-side perimeter, identity, endpoint"),
    "sis":           ("SIS Safety Detection", "Functional-safety detections"),
    "historian":     ("OT Historian Detection", "Process-data behavioural detections"),
}


def slug(text, maxlen=60):
    s = re.sub(r"[^a-z0-9]+", "-", (text or "").lower()).strip("-")
    return s[:maxlen].strip("-")


def read_csv(path):
    full = os.path.join(ROOT, path)
    if not os.path.exists(full):
        return []
    with open(full, newline="", encoding="utf-8-sig") as fh:
        return list(csv.DictReader(fh))


def collect():
    """Gather every detection from every library into a normalized list."""
    items = []

    # --- 1. Threat-informed use cases (the spine) ---
    for r in read_csv("02-detection/catalog/use-case-catalog.csv"):
        items.append({
            "legacy_id": r["UC_ID"], "library": "use-case",
            "title": r["Title"], "category": r["Category"],
            "attack": r["ATTACK_Technique_ID"], "actors": r["Threat_Actors"],
            "sectors": r["Sectors"], "protocol": r["Protocol"],
            "data_source": r["Primary_Data_Source"], "nozomi": r["Nozomi_Type_ID"],
            "severity": r["Severity"], "stage": r["Lifecycle_Stage"],
            "purdue": r["Purdue_Level"], "logic": "", "artifact": r["Detection_Ref"],
        })

    # --- 2. Sigma rules across all libraries ---
    for path in sorted(glob.glob(os.path.join(ROOT, "02-detection/sigma/*/*.yml"))):
        lib = os.path.basename(os.path.dirname(path))
        fname = os.path.basename(path)
        num = re.match(r"(\d+)_", fname)
        legacy = f"SIGMA:{lib}/{num.group(1)}" if num else f"SIGMA:{lib}/{fname[:-4]}"
        try:
            with open(path, encoding="utf-8") as fh:
                doc = yaml.safe_load(fh) or {}
        except Exception:
            continue
        tags = doc.get("tags") or []
        attack = ";".join(sorted({
            t.split(".")[-1].upper() for t in tags
            if re.search(r"t0\d{3}", str(t), re.I)
        }))
        ls = doc.get("logsource") or {}
        items.append({
            "legacy_id": legacy, "library": lib,
            "title": doc.get("title", fname), "category": "Sigma",
            "attack": attack, "actors": ";".join(doc.get("threat_actors", []) or []),
            "sectors": ";".join(doc.get("sectors", []) or []), "protocol": ls.get("product", ""),
            "data_source": f"{ls.get('category','')}/{ls.get('product','')}".strip("/"),
            "nozomi": doc.get("nozomi_type_id", ""), "severity": doc.get("level", "medium"),
            "stage": doc.get("status", "experimental"), "purdue": "",
            "logic": (doc.get("description") or "").strip().replace("\n", " ")[:300],
            "artifact": os.path.relpath(path, ROOT),
        })

    # --- 3. Protocol NDR catalog ---
    for r in read_csv("source-libraries/protocol-ndr-catalog.csv"):
        items.append({
            "legacy_id": r["id"], "library": "protocol-ndr",
            "title": r["detection"], "category": r["protocol"],
            "attack": r.get("attack_ics", ""), "actors": "", "sectors": "",
            "protocol": r["protocol"], "data_source": r.get("log_source", ""),
            "nozomi": "", "severity": r.get("severity", "medium"),
            "stage": "Validated", "purdue": "",
            "logic": r.get("logic", ""), "artifact": "",
        })

    # --- 4. Perimeter-to-endpoint catalog ---
    for r in read_csv("source-libraries/perimeter-catalog.csv"):
        items.append({
            "legacy_id": r["id"], "library": "perimeter",
            "title": r["detection"], "category": r["category"],
            "attack": r.get("attack", ""), "actors": "", "sectors": "",
            "protocol": "", "data_source": r.get("data_source", ""),
            "nozomi": "", "severity": r.get("severity", "medium"),
            "stage": "Validated", "purdue": "L3.5/IT",
            "logic": r.get("style", ""), "artifact": "",
        })

    # --- 5. SIS safety catalog ---
    for r in read_csv("source-libraries/sis-catalog.csv"):
        items.append({
            "legacy_id": r["id"], "library": "sis",
            "title": r["detection"], "category": r["category"],
            "attack": r.get("attack_ics", ""), "actors": "", "sectors": "",
            "protocol": "", "data_source": r.get("data_source", ""),
            "nozomi": "", "severity": r.get("severity", "high"),
            "stage": "Validated", "purdue": "L1-SIS",
            "logic": r.get("safety_principle", ""), "artifact": "",
        })

    # --- 6. Historian detections (folder-per-detection) ---
    for path in sorted(glob.glob(os.path.join(ROOT, "02-detection/historian/*/*/detection.yml"))):
        with open(path, encoding="utf-8") as fh:
            doc = yaml.safe_load(fh) or {}
        d = os.path.dirname(path)
        items.append({
            "legacy_id": f"HIST-{doc.get('id','?')}", "library": "historian",
            "title": doc.get("title", ""), "category": doc.get("family", ""),
            "attack": ";".join(str(a).split()[0] for a in (doc.get("attack_ics") or [])),
            "actors": "", "sectors": "", "protocol": "",
            "data_source": "historian", "nozomi": "",
            "severity": doc.get("level", "medium"), "stage": doc.get("status", ""),
            "purdue": "L3", "logic": (doc.get("description") or "").replace("\n", " ").strip()[:300],
            "artifact": os.path.relpath(d, ROOT),
        })

    return items


def main():
    items = collect()

    # Build merge lookup: legacy_id -> canonical legacy_id
    merged_into, merge_reason = {}, {}
    for primary, dupes, reason in MERGE_MAP:
        for d in dupes:
            merged_into[d] = primary
            merge_reason[d] = reason

    by_legacy = {i["legacy_id"]: i for i in items}
    merge_rows = []

    # Assign OTD IDs to canonical detections only
    canonical, absorbed = [], {}
    for it in items:
        target = merged_into.get(it["legacy_id"])
        if target and target in by_legacy:
            absorbed.setdefault(target, []).append(it)
            merge_rows.append([it["legacy_id"], it["library"], it["title"],
                               target, merge_reason[it["legacy_id"]]])
        else:
            canonical.append(it)

    # Sort: use cases first (they carry the threat context), then by library, then legacy id
    order = {"use-case": 0, "sis": 1, "ot-ics-soc": 2, "core-protocol": 3,
             "it-dmz-ot-crosszone": 4, "threat-actor": 5, "advisory": 6,
             "protocol-ndr": 7, "historian": 8, "perimeter": 9}
    canonical.sort(key=lambda x: (order.get(x["library"], 99), x["legacy_id"]))

    rows = []
    for n, it in enumerate(canonical, start=1):
        otd = f"OTD-{n:04d}"
        merged = absorbed.get(it["legacy_id"], [])
        # enrich from absorbed duplicates where the canonical is missing a field
        for m in merged:
            for f in ("attack", "actors", "sectors", "nozomi", "protocol", "logic"):
                if not it.get(f) and m.get(f):
                    it[f] = m[f]
        # A use case that absorbed a Sigma rule inherits that rule as its executable
        # artifact - the UC carries the threat context, the Sigma carries the logic.
        if not str(it.get("artifact", "")).endswith(".yml"):
            for m in merged:
                if str(m.get("artifact", "")).endswith(".yml"):
                    it["artifact"] = m["artifact"]
                    break
        # Repoint surviving use-case artifact refs at their migrated location
        art = str(it.get("artifact", ""))
        if art.startswith("sigma/"):
            cand = os.path.join("02-detection/sigma/core-protocol", os.path.basename(art))
            it["artifact"] = cand if os.path.exists(os.path.join(ROOT, cand)) else ""
        elif art.startswith("n2ql/"):
            cand = os.path.join("02-detection/nozomi", os.path.basename(art))
            it["artifact"] = cand if os.path.exists(os.path.join(ROOT, cand)) else ""
        lib_name = LIBRARY_META.get(it["library"], (it["library"], ""))[0]
        rows.append([
            otd, it["title"], it["library"], lib_name, it["legacy_id"],
            ";".join(m["legacy_id"] for m in merged), len(merged),
            it["category"], it["attack"], it["actors"], it["sectors"],
            it["purdue"], it["protocol"], it["data_source"], it["nozomi"],
            it["severity"], it["stage"], it["artifact"],
            slug(it["title"]), it["logic"],
        ])

    header = ["OTD_ID", "Title", "Library", "Library_Name", "Legacy_ID", "Merged_Legacy_IDs",
              "Merge_Count", "Category", "ATTACK_Technique_IDs", "Threat_Actors", "Sectors",
              "Purdue_Level", "Protocol", "Data_Source", "Nozomi_Type_ID", "Severity",
              "Status", "Artifact_Path", "Slug", "Logic_Summary"]

    out = os.path.join(ROOT, "02-detection/catalog/master-detection-catalog.csv")
    with open(out, "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(header)
        w.writerows(rows)
    print(f"  wrote master-detection-catalog.csv ({len(rows)} detections)")

    out2 = os.path.join(ROOT, "02-detection/catalog/merge-log.csv")
    with open(out2, "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["Absorbed_Legacy_ID", "Absorbed_Library", "Absorbed_Title",
                    "Merged_Into_Legacy_ID", "Rationale"])
        w.writerows(merge_rows)
    print(f"  wrote merge-log.csv ({len(merge_rows)} merges)")

    # Library summary
    print("\n  Detections by library:")
    counts = {}
    for r in rows:
        counts[r[3]] = counts.get(r[3], 0) + 1
    for k in sorted(counts, key=lambda x: -counts[x]):
        print(f"    {k:<38} {counts[k]:>4}")
    print(f"    {'TOTAL':<38} {len(rows):>4}")


if __name__ == "__main__":
    main()
