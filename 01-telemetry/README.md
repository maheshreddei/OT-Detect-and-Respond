# 01 — Telemetry & Collection

What can be collected, in what order, and why. Nothing in `02-detection/` works without a
source here.

| File | IDs | Ranked by |
|------|-----|-----------|
| `telemetry-hierarchy.csv` | `TEL-01..14` | **Hunt value** vs effort |
| `collection-plan.csv` | `CP-01..14` | **Deployment priority**, with collection mechanism |
| `minimum-viable-telemetry.csv` | `MVT-1..7` | **Budget sequence** — each step independently useful |
| `log-source-inventory.csv` | `LS-01..19` | **Onboarding tier**, from four-axis scoring |
| `parser-mapping.csv` | `LS-##` | Transport, parser, sourcetype, key fields, CIM |
| `onboarding-tiers.csv` | — | Tier rollup with rationale |

## Three views, deliberately

They rank the same equipment differently and that disagreement is information. The clearest
case: **network monitoring is the #1 hunt-value source (`TEL-01`), a priority-1 collection
item (`CP-04`), and Tier 3 for onboarding (`LS-18`)** — highest value, slowest to arrive.
`MVT` is the answer to what you do meanwhile. See `../docs/telemetry-strategy.md`.
