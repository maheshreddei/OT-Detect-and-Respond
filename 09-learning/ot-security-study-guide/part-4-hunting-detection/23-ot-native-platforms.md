# Chapter 23 — OT-Native Platforms: Nozomi and Claroty

> Part IV. Purpose-built OT monitoring platforms give you the asset inventory, protocol parsing, and baselining that a generic SIEM lacks. This chapter is about hunting *inside* them and integrating them with the rest of your stack.

## 23.1 What OT-native platforms add

Products like **Nozomi Networks**, **Claroty**, and **Dragos** are passive OT network monitoring platforms. Out of the box they provide:

- **Passive asset inventory** — devices, roles, firmware, vulnerabilities, discovered from traffic without scanning.
- **Protocol-aware parsing and baselining** — they learn normal conversations and command patterns for industrial protocols.
- **Prebuilt OT alerts** — unauthorized write, new asset, protocol anomaly, known-threat signatures.
- **Network visualization** — the Purdue/communication map drawn from real traffic.

They are, in effect, a productized version of the Zeek+ICSNPP+baseline pipeline (Chapters 08–09, 19), with an OT-tuned analytics and asset layer on top.

## 23.2 Hunting inside the platform

The platform is a rich hunting surface, not just an alert generator:

- **Asset review** — reconcile the discovered inventory against the CMDB; a device the platform sees but you don't know is a finding.
- **Link/conversation review** — confirm that controller-directed conversations come only from sanctioned masters/EWS; investigate any new link.
- **Variable/tag review** — for critical controllers, review which writable variables are being touched and by whom; an unexpected writer to a critical variable is high-signal.
- **Alert triage by asset criticality** — work the platform's alerts consequence-first, not chronologically.
- **Baseline review** — inspect what the platform *learned* as normal; a baseline that absorbed malicious activity during learning is a subtle trap to check.

## 23.3 Query languages and custom logic

Beyond built-in alerts, these platforms expose query/assertion languages (for example, Nozomi's **N2QL**) that let you build custom checks — "assert that no source outside this set ever issues a write function code to this zone," or "list all new nodes in the safety zone in the last 24 hours." Custom assertions are how you encode *your* environment's command allow-list into the platform, turning generic capability into site-specific detection.

## 23.4 Integrate, don't silo

The most common mistake is treating the OT platform as a separate console the SOC rarely opens. Instead:

- **Forward its alerts and underlying detail to the SIEM** (Chapter 22) so OT correlates with identity, endpoint, and IT events on one pane.
- **Use it as the sensor and asset brain**, and hunt across it from the SIEM.
- **Feed its asset inventory** into your CMDB and your allow-lists.

Extend one pane of glass rather than running two; the OT platform's job is best visibility and asset context, the SIEM's job is correlation and response.

## Chapter summary
- OT-native platforms (Nozomi/Claroty/Dragos) provide **passive inventory, protocol baselining, prebuilt alerts, and network maps** — a productized Zeek+baseline pipeline with an OT asset/analytics layer.
- Hunt inside them via **asset, link, variable, alert, and baseline review.**
- Use their **query/assertion languages** (e.g. N2QL) to encode your command allow-list as custom detection.
- **Integrate to the SIEM** — use the platform as sensor/asset brain, correlate and respond centrally.

## Cross-references
- Chapters 08–09 and 19 (the underlying pipeline they productize); Chapter 22 (SIEM correlation).
- Companion: `ot-protocol-defense/nozomi-queries` (N2QL assertion library).
