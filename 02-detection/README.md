# 02 — Detection Content

257 canonical detections consolidated from ten source libraries, each with a unified
`OTD-####` ID, its original `Legacy_ID`, a Sentinel query, and a Splunk query.

## Layout

| Path | Contents |
|------|----------|
| `catalog/master-detection-catalog.csv` | **The spine** — 257 detections, all metadata |
| `catalog/merge-log.csv` | 19 merges with rationale, for audit |
| `catalog/query-index.csv` | Per-detection query paths and provenance |
| `catalog/*.csv` (attack/actor/sector/nozomi) | Threat-content pivot views |
| `sigma/` | 93 Sigma rules in 5 library folders |
| `queries/sentinel/` | 257 KQL queries |
| `queries/splunk/` | 257 SPL queries |
| `historian/` | 6 detections, folder-per-detection with hand-authored KQL/SPL |
| `nozomi/` | N2QL queries, assertion queries, N2QL reference |
| `domains/` | Narrative detection docs (SIS families, perimeter families, protocol NDR) |

## Reading a catalog row

`OTD-0003` carries every axis at once: title, source library, legacy ID, the IDs it absorbed
on merge, ATT&CK for ICS technique, threat actors, sectors, Purdue level, protocol, data
source, Nozomi `type_id`, severity, status, and the path to its Sigma artifact.

## Sigma libraries

| Library | Rules | Focus |
|---------|------:|-------|
| `it-dmz-ot-crosszone/` | 27 | Purdue zone crossing, IT→OT paths |
| `advisory/` | 20 | CTI advisory-derived (ME/GCC focus) |
| `ot-ics-soc/` | 20 | Protocol-level OT SOC rules |
| `threat-actor/` | 20 | Actor-derived rules |
| `core-protocol/` | 6 | Core protocol rules |

## Queries

See `../docs/query-generation.md`. In short: 90 compiled from Sigma, 6 hand-authored, 161
scaffolds that are **specifications, not deployable detections**. Placeholders in
`<angle brackets>` must be baselined before use.
