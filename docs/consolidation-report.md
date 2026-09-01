# Consolidation Report

What was merged, what was kept separate, and the reasoning for each decision. This document
exists so the consolidation is auditable — a reader should be able to trace any detection in
the master catalog back to the repository it came from.

## Source repositories

Ten archives were supplied. Four were exact or near-exact duplicates:

| Archive | Disposition |
|---------|-------------|
| `ot-detection-engineering-main` | **Primary.** 148 files: 87 Sigma rules across 4 libraries + 6 historian detections with hand-authored KQL/SPL |
| `ot-detection-engineering-main__1_` | **Dropped** — byte-identical to the above (verified by recursive diff) |
| `ot-siem-log-source-onboarding-main` | **Primary** for log-source content |
| `ot-siem-log-source-onboarding` | **Dropped** — identical except for CRLF vs LF line endings |
| `ot-protocol-defense_NDR-main` | **Primary** — superset: adds `nozomi-queries/` (N2QL reference, assertion queries, query catalog) |
| `ot-protocol-defense-main` | **Dropped** — proper subset of the NDR version |
| `ot-threat-content-repo-main` | Merged — 28 use cases, 6 Sigma, 3 N2QL, lifecycle framework |
| `it-ot-incident-response-main` | Merged — 5 playbooks, 3 SOPs, 6 evidence guides, 3 templates |
| `sis-safety-detection-main` | Merged — 33 SIS detections, functional-safety primer |
| `perimeter-to-endpoint-detections-main` | Merged — 62 IT-side detections |

Verification method: recursive `diff -rq` and per-tree MD5 aggregate. Nothing was dropped on
filename similarity alone.

## Detection-level merges

The four catalogs used four different ID schemes (`OT-UC-####`, `SCAN-`/`MOD-`/`DNP3-`…,
`NET-`/`IAM-`/`EDR-`…, `SIS-A1`…) and overlapped in places. Every detection received a
unified `OTD-####` ID while **retaining its original ID in the `Legacy_ID` column**, so
provenance is never lost.

19 detections were merged into 10 canonical entries. Each merge was decided by comparing
detection *logic*, not titles — a silent merge of two subtly different detections is worse
than two rows. The full list is in `02-detection/catalog/merge-log.csv`. Examples:

| Canonical | Absorbed | Why |
|-----------|----------|-----|
| `OT-UC-0003` | `SIGMA:ot-ics-soc/01`, `MOD-01` | Same detection — Modbus write FC 5/6/15/16 from outside the authorized master allowlist. The use case carries threat/sector context, the Sigma carries portable logic, the protocol catalog carries the NDR pattern. Merging keeps all three facets on one row. |
| `OT-UC-0007` | `SIGMA:ot-ics-soc/05`, `DNP3-02` | Same detection — DNP3 FC 13/14 cold/warm restart to an outstation. |
| `OT-UC-0017` | `SIS-B1`, `SIGMA:it-dmz-ot-crosszone/20` | Same detection — safety controller in PROGRAM mode / SIS point forced. The SIS library contributes the functional-safety framing. |
| `OT-UC-0013` | `SCAN-01`, `SCN-01` | Same concept observed at two vantage points: the perimeter library scores it on IT flow data, the protocol library on OT NDR. |

**Enrichment on merge.** When a use case absorbed a Sigma rule, the canonical row inherits
the Sigma file as its executable artifact — the use case supplies threat context, the Sigma
supplies the logic. This is why `OTD-0003` compiles to real KQL/SPL rather than a scaffold.

## What was deliberately NOT merged

Similar-sounding detections were kept separate where their **logic or vantage point
differs**:

- **Perimeter vs OT versions of the same technique.** `NET-`/`SCN-` detections operate on IT
  flow and firewall data; their OT counterparts operate on protocol-aware NDR. Same
  adversary behaviour, different telemetry, different tuning, different false positives.
- **Protocol-specific variants.** Modbus, DNP3, IEC-104, and S7 restart commands are
  separate detections, not one "controller restart" entry. The function codes, the
  telemetry, and the response differ per protocol.
- **SIS versions of general detections.** A new asset in a process zone and a new asset in
  the SIS zone are different severities with different playbooks. Merging them would lose
  the safety escalation.

## Structural consolidation

| Source structure | Destination | Note |
|------------------|-------------|------|
| 4 Sigma libraries + our 6 core rules | `02-detection/sigma/{advisory,it-dmz-ot-crosszone,ot-ics-soc,threat-actor,core-protocol}/` | 93 rules, library folders preserved |
| Historian folder-per-detection | `02-detection/historian/` | Structure kept intact — it is the best pattern in the whole portfolio (`detection.yml` + `sentinel.kql` + `splunk.spl` + `validation.md`) |
| 3 catalog CSVs | `source-libraries/` | Preserved verbatim for provenance; the master catalog is derived from them |
| Protocol references (13 + README) | `03-protocols/` | From the NDR superset |
| IR playbooks, SOPs, evidence, templates | `04-response/` | Playbooks rewritten to the standard template (below) |
| Nozomi N2QL + assertion queries | `02-detection/nozomi/` | Merged from two sources |

## Playbook standardisation

The five original IR playbooks were strong on evidence handling but **lacked two sections**
the standard template requires: a **Severity guide** (default severity plus concrete
escalation criteria) and a **Safety check** (the "is this legitimate work?" gate asked
*before* investigation).

All playbooks were rewritten to the full template and four new ones added to cover
detection families that had none — unauthorized control command, rogue asset, process-data
anomaly, and engineering software outside change window. Result: 9 playbooks, all carrying
Trigger, Severity guide, Safety check, Investigate (passive), Decide, Respond (with
sign-off), and Close. `tools/validate.py` fails the build if any section is missing.

Playbooks route to detections two ways: **explicit** `OTD` references in the playbook text
(18 detections), and **family routing** by keyword against title, category, logic, and
protocol (175 more). A playbook covers a class of alert, so family routing is the normal
case. 193 of 257 detections (75%) route to a playbook; the remainder are mostly IT-side
perimeter detections whose response is standard IT procedure.

## What is intentionally still separate

Not everything belongs in one repository. These remain standalone because they serve
different readers and formats:

- The long-form OT/ICS handbook (educational, chapter-structured)
- The IT→OT intrusion simulation toolkit (executable Python)
- The MSS capability proposal and leadership deck (commercial artifact)

Consolidation improves a portfolio when it removes redundancy and reveals relationships. It
damages one when it merges things whose only commonality is subject matter.
