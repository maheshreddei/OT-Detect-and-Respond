#!/usr/bin/env python3
"""
validate.py - structural and referential integrity across the whole program.

Run before every commit. Exit 0 = clean, 1 = issues.

Usage:  python3 tools/validate.py
"""
import csv
import glob
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
errors, warnings = [], []


def read(p):
    full = os.path.join(ROOT, p)
    if not os.path.exists(full):
        errors.append(f"missing required file: {p}")
        return []
    with open(full, newline="", encoding="utf-8-sig") as fh:
        return list(csv.DictReader(fh))


def ids(v):
    return [x.strip() for x in (v or "").split(";") if x.strip()]


def check(cond, msg):
    if not cond:
        errors.append(msg)


print("== CSV structure ==")
for path in sorted(glob.glob(os.path.join(ROOT, "**", "*.csv"), recursive=True)):
    rel = os.path.relpath(path, ROOT)
    with open(path, newline="", encoding="utf-8-sig") as fh:
        rows = list(csv.reader(fh))
    widths = {len(r) for r in rows if r}
    if len(widths) != 1:
        errors.append(f"{rel}: inconsistent column count {sorted(widths)}")
    print(f"  {rel}: {len(rows)-1} rows{'' if len(widths)==1 else '  <-- INCONSISTENT'}")

tel = read("01-telemetry/telemetry-hierarchy.csv")
cp = read("01-telemetry/collection-plan.csv")
mvt = read("01-telemetry/minimum-viable-telemetry.csv")
ls = read("01-telemetry/log-source-inventory.csv")
parser = read("01-telemetry/parser-mapping.csv")
cat = read("02-detection/catalog/master-detection-catalog.csv")
qidx = read("02-detection/catalog/query-index.csv")
merge = read("02-detection/catalog/merge-log.csv")
pbi = read("04-response/playbooks/playbook-index.csv")
xw = read("05-crosswalk/master-crosswalk.csv")

TEL = {r["TEL_ID"] for r in tel}
CP = {r["CP_ID"] for r in cp}
LS = {r["Source_ID"] for r in ls}
OTD = {r["OTD_ID"] for r in cat}

print(f"\n== ID universes ==\n  TEL={len(TEL)} CP={len(CP)} MVT={len(mvt)} LS={len(LS)} OTD={len(OTD)} playbooks={len(pbi)}")

print("\n== Referential integrity ==")
for r in tel:
    for l in ids(r["Maps_To_LS"]):
        check(l in LS, f"{r['TEL_ID']} -> unknown log source {l}")
for r in cp:
    for l in ids(r["Maps_To_LS"]):
        check(l in LS, f"{r['CP_ID']} -> unknown log source {l}")
    for t in ids(r["Maps_To_TEL"]):
        check(t in TEL, f"{r['CP_ID']} -> unknown telemetry {t}")
for r in mvt:
    for c in ids(r["Maps_To_CP"]):
        check(c in CP, f"{r['MVT_ID']} -> unknown CP {c}")
    for l in ids(r["Maps_To_LS"]):
        check(l in LS, f"{r['MVT_ID']} -> unknown log source {l}")
for r in xw:
    check(r["OTD_ID"] in OTD, f"crosswalk -> unknown detection {r['OTD_ID']}")
    for l in ids(r["LS_IDs"]):
        check(l in LS, f"{r['OTD_ID']} -> unknown log source {l}")
check({r["Source_ID"] for r in parser} == LS, "parser-mapping does not cover exactly the LS universe")

# unique IDs
check(len(OTD) == len(cat), "duplicate OTD_ID in master catalog")
legacy = [r["Legacy_ID"] for r in cat]
check(len(legacy) == len(set(legacy)), "duplicate Legacy_ID in master catalog")

print(f"  checked {len(tel)+len(cp)+len(mvt)+len(xw)} cross-layer references")

print("\n== Detection artifacts ==")
missing_art = 0
for r in cat:
    a = r["Artifact_Path"]
    if a and not os.path.exists(os.path.join(ROOT, a)):
        errors.append(f"{r['OTD_ID']}: artifact path does not exist -> {a}")
        missing_art += 1
print(f"  artifact paths checked, {missing_art} broken")

# every catalogued detection must have both queries
qmap = {r["OTD_ID"]: r for r in qidx}
noq = [o for o in OTD if o not in qmap]
check(not noq, f"{len(noq)} detections have no query index entry")
missing_q = 0
for r in qidx:
    for f in ("Sentinel_KQL_Path", "Splunk_SPL_Path"):
        if r[f] and not os.path.exists(os.path.join(ROOT, r[f])):
            errors.append(f"{r['OTD_ID']}: missing query file {r[f]}")
            missing_q += 1
print(f"  query files checked ({len(qidx)} indexed), {missing_q} missing")

print("\n== Sigma rules ==")
try:
    import yaml
    bad = 0
    sigma_files = sorted(glob.glob(os.path.join(ROOT, "02-detection/sigma/*/*.yml")))
    for path in sigma_files:
        rel = os.path.relpath(path, ROOT)
        with open(path, encoding="utf-8") as fh:
            try:
                doc = yaml.safe_load(fh)
            except Exception as e:
                errors.append(f"{rel}: YAML parse error {e}")
                bad += 1
                continue
        for field in ("title", "id", "logsource", "detection"):
            if field not in (doc or {}):
                errors.append(f"{rel}: missing required Sigma field '{field}'")
                bad += 1
    print(f"  {len(sigma_files)} Sigma rules parsed, {bad} issue(s)")
except ImportError:
    warnings.append("PyYAML not installed - Sigma rules not validated")

print("\n== Playbooks ==")
for path in sorted(glob.glob(os.path.join(ROOT, "04-response/playbooks/PLAYBOOK-OT-*.md"))):
    rel = os.path.relpath(path, ROOT)
    txt = open(path, encoding="utf-8").read()
    for section in ("**Trigger.**", "**Severity guide.**", "**Safety check.**",
                    "**Decide.**", "**Respond", "**Close.**"):
        if section not in txt:
            errors.append(f"{rel}: missing required section {section}")
    if "Investigate (passive)" not in txt:
        errors.append(f"{rel}: missing 'Investigate (passive)' section")
print(f"  {len(pbi)} playbooks checked for required sections")

print("\n== Documentation links ==")
# Catch the failure mode where a doc is referenced but was never migrated. A README that
# points at a file which does not exist is a silent defect - it reads as complete.
md_files = sorted(glob.glob(os.path.join(ROOT, "**", "*.md"), recursive=True))
link_re = re.compile(r"\[[^\]]*\]\(([^)#][^)]*)\)")
backtick_re = re.compile(r"`((?:docs|tools|0\d-[a-z]+|source-libraries)/[A-Za-z0-9_\-./]+\.(?:md|csv|py|yml))`")
checked = broken = 0
for path in md_files:
    rel = os.path.relpath(path, ROOT)
    base = os.path.dirname(path)
    txt = open(path, encoding="utf-8").read()
    # Code samples can contain expressions such as c["check"](out), which are not
    # Markdown links. Exclude fenced code before applying the intentionally small
    # link parser.
    link_text = re.sub(r"```.*?```", "", txt, flags=re.DOTALL)
    targets = set()
    for m in link_re.finditer(link_text):
        t = m.group(1).strip()
        if t.startswith(("http://", "https://", "mailto:")):
            continue
        targets.add((t, base))
    # Backtick-quoted repo paths are references too, resolved from the repo root
    for m in backtick_re.finditer(link_text):
        target = m.group(1)
        # Extension guides retain their original relative docs/tools references.
        # Prefer the document-relative target when it exists; otherwise preserve
        # the original root-relative validation behavior.
        origin = base if os.path.exists(os.path.normpath(os.path.join(base, target))) else ROOT
        targets.add((target, origin))
    for t, origin in targets:
        checked += 1
        if not os.path.exists(os.path.normpath(os.path.join(origin, t))):
            errors.append(f"{rel}: references missing file -> {t}")
            broken += 1
print(f"  {checked} internal references checked across {len(md_files)} docs, {broken} broken")

print("\n== Coverage warnings ==")
nopb = sum(1 for r in xw if not r["Playbook_IDs"])
if nopb:
    warnings.append(f"{nopb} of {len(xw)} detections have no linked playbook")
scaffold = sum(1 for r in qidx if r["Query_Origin"] == "scaffold")
if scaffold:
    warnings.append(f"{scaffold} queries are SCAFFOLD (spec-only, need completion before deployment)")
print(f"  {len(warnings)} warning(s)")

print("\n" + "=" * 64)
if warnings:
    print(f"WARNINGS ({len(warnings)}):")
    for w in warnings:
        print(f"  ! {w}")
if errors:
    print(f"\nERRORS ({len(errors)}):")
    for e in errors[:40]:
        print(f"  X {e}")
    if len(errors) > 40:
        print(f"  ... and {len(errors)-40} more")
    print("\nVALIDATION FAILED")
    sys.exit(1)
print("\nVALIDATION PASSED")
sys.exit(0)
