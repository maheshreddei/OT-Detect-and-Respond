# 05 — Crosswalk (Generated)

**Do not edit these files by hand.** They are build output from `tools/build_crosswalk.py`,
derived from `01-telemetry/`, `02-detection/`, and `04-response/`. Hand-editing creates the
exact drift this layer prevents.

| File | Shows |
|------|-------|
| `master-crosswalk.csv` | Every detection's full chain: technique → actor → protocol → Nozomi → log sources → tiers → playbook → both queries |
| `detection-to-logsource.csv` | Which log sources each detection needs, and whether it is reachable at Tier 1 |
| `detection-to-playbook.csv` | Playbook routing, with `Routing` showing explicit vs family |
| `telemetry-to-logsource.csv` | TEL → LS resolution with tier, CP, MVT, collection pattern |
| `coverage-rollup.csv` | What each log source unlocks — detections and distinct techniques |
| `attack-coverage.csv` | ATT&CK for ICS technique → detections (49 techniques) |

## What it tells you

- **Network Traffic (LS-18, Tier 3)** unlocks 138 detections across 37 techniques — the
  highest-leverage source and the slowest to deploy.
- **Firewall (LS-02, Tier 1)** unlocks 77 detections — the best value per unit of effort.
- **119 of 257 detections** are reachable with Tier 1 telemetry alone.
- **193 of 257** route to a response playbook.

## Rebuild

```bash
python3 tools/build_catalog.py && python3 tools/generate_queries.py && \
python3 tools/build_crosswalk.py && python3 tools/validate.py
```
