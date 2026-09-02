# 01 — Telemetry & Collection

What should be collected, in what order, and which detection and response outcome it
supports. Nothing in `02-detection/` works without a source here, and an alert is not
operationally useful unless it can be investigated and routed to `04-response/`.

## Scope: OT-centred, not OT-network-only

This telemetry set is for defending an OT environment, but collection should not stop at
the OT network boundary. It deliberately covers four evidence planes:

1. **Access and boundary** — VPN, identity, jump hosts, IDMZ firewalls and remote-access
   brokers show how a person or system reached OT.
2. **OT hosts and applications** — EWS, HMI, SCADA, historian and application logs show
   user, process and configuration activity that passive packet inspection cannot.
3. **OT network and controllers** — passive network metadata/DPI, controller diagnostics,
   mode and checksum state show commands and changes on assets that often cannot run an
   agent.
4. **Process and physical context** — historian values, alarms, safety events, badge and
   removable-media records help distinguish cyber activity from authorized operations and
   confirm process impact.

Enterprise-wide IT telemetry is out of scope unless it explains an access path into OT,
activity on an OT-serving system, or likely impact to operations. Collecting every IT log
would add cost without improving this OT detection mission.

| File | IDs | Ranked by |
|------|-----|-----------|
| `telemetry-hierarchy.csv` | `TEL-01..15` | **Hunt value** vs effort |
| `collection-plan.csv` | `CP-01..14` | **Deployment priority**, with collection mechanism |
| `minimum-viable-telemetry.csv` | `MVT-1..7` | **Budget sequence** — each step independently useful |
| `log-source-inventory.csv` | `LS-01..21` | **Onboarding tier**, from four-axis scoring |
| `parser-mapping.csv` | `LS-##` | Transport, parser, sourcetype, key fields, CIM |
| `onboarding-tiers.csv` | — | Tier rollup with rationale |
| `detection-response-linkage.csv` | `DR-01..09` | Telemetry -> detection -> validation -> safe response playbook |
| [`nozomi-design/`](nozomi-design/) | — | Nozomi HLD, LLD, SPAN/TAP, interfaces, commissioning and interview guide |

## Three views, deliberately

They rank the same equipment differently and that disagreement is information. The clearest
case: **network monitoring is the #1 hunt-value source (`TEL-01`) and starts with one
priority-1 boundary pilot (`CP-04`)**, while full cell/area coverage remains a later
engineering phase. `MVT` defines useful increments rather than waiting for complete OT
visibility. The outcome mapping in `detection-response-linkage.csv` shows why each source
is collected and prevents collection from becoming an end in itself. See
`../docs/telemetry-strategy.md`.
