# OT SIEM Log Source Onboarding

A prioritization and onboarding reference for bringing OT/ICS log sources into a SIEM in the
right order — sequenced by feasibility, noise, and security value rather than ingesting
everything on day one. It is the **collection** half of an OT detection program; the
**detection** half lives in the OT Threat Content Repository, and the two are wired together
by `catalog/detection-linkage.csv`.

## The idea

Every OT data source is scored on four axes — **Log Ease, Noise, Source Count, Importance**
— and those axes derive an **onboarding tier**. Tier governs onboarding *order*, never
response *priority* (safety-critical events always page out regardless of tier). The scoring
model is written down in `docs/methodology.md` so it can be applied to new sources
consistently.

## What's here

| Path | Contents |
|------|----------|
| `guide/log-source-onboarding-guide.md` | The narrative guide: how to read the axes, the four tiers, and the full reference table. |
| `catalog/log-source-inventory.csv` | The reference table as data — 19 sources, four axes, tier, collection method. The spine. |
| `catalog/onboarding-tiers.csv` | Tier rollup with source lists and rationale. |
| `catalog/parser-mapping.csv` | Per-source collection method, transport, parser, sourcetype, key fields, CIM normalization. |
| `catalog/detection-linkage.csv` | Per-source mapping to the use cases it enables (join to the Threat Content Repository). |
| `docs/methodology.md` | The four-axis scoring model and how tier is derived, with worked examples. |
| `docs/collection-architecture.md` | The three collection patterns (host agent / syslog / passive) that cover the whole inventory. |
| `onboarding/` | Per-source runbook template, go-live checklist, and validation template. |

## The tiers at a glance

- **Tier 1 — Onboard first:** Control/SCADA server, OT firewall, jump host, VPN, switch,
  engineering/operator workstations. The backbone of IT-to-OT crossing and remote-access
  detection.
- **Tier 2 — Onboard next:** PLC, safety controller, data gateway, historian, HMI, IED,
  router. High value but harder to instrument or lower urgency.
- **Tier 3 — Fill gaps:** application server, DCS, PAC, RTU, network traffic (SPAN/TAP/IDS).
  High effort; network traffic feeds the most detections but is gated on SPAN/TAP and DPI
  work.
- **Tier 4 — Do not collect:** field I/O, represented indirectly via PLC/RTU and historian.

## How it connects to detection

Onboarding a source is not complete when events arrive — it is complete when a detection
consuming it is live. `catalog/detection-linkage.csv` names, per source, which use cases it
enables (e.g. the OT firewall feeds the zone-crossing and remote-access use cases; network
traffic feeds the protocol-level Sigma detections). Those `UC_ID` values correspond to the
OT Threat Content Repository, so a source's `Primary_Data_Source` there and its linkage here
are two ends of the same wire.

## Collection patterns

Three patterns cover everything (detail in `docs/collection-architecture.md`):

- **A — Host agent:** Windows Event Log / Sysmon / auditd via forwarder (SCADA server, jump
  host, workstations, HMI, app server, historian).
- **B — Syslog:** appliance streams to a collection tier with a vendor parser (firewall,
  VPN, switch, router, gateway, IED).
- **C — Passive:** a SPAN/TAP sensor (Nozomi Guardian, optionally Zeek + ICSNPP) observes OT
  protocols for sources that cannot log about themselves (PLC, PAC, DCS, RTU, safety
  controller). Nozomi alerts carry ATT&CK for ICS natively, so these feeds arrive
  pre-mapped for correlation.

## License

MIT — see `LICENSE`.

## Push to your remote

```bash
git init
git add .
git commit -m "Initial commit: OT SIEM log source onboarding"
git branch -M main
git remote add origin git@github.com:<your-username>/ot-siem-log-source-onboarding.git
git push -u origin main
```

*Prepared for OT/ICS detection engineering — Help AG MSS Cyber Defense.*
