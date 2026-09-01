# OT SIEM Log Source Prioritization & Onboarding Guide

*A practical reference for sequencing log source onboarding by feasibility, noise, and security value.*

## How to read this

Each OT data source is rated on four practical axes: how easy the logs are to collect
(**Log Ease**), how noisy the source typically is once collecting (**Noise**), how many
instances of that source type usually exist in a given network (**Source Count**), and its
overall **Importance**. The onboarding tier translates those four axes into the order in
which a Cyber Defense / MSS team should realistically bring sources into the SIEM, rather
than trying to ingest everything on day one.

The machine-readable version of the table below lives in
`catalog/log-source-inventory.csv`; collection/parser detail is in
`catalog/parser-mapping.csv`; and the mapping from each source to the detection use cases
it enables is in `catalog/detection-linkage.csv`.

## Onboarding tiers

### Tier 1 — Onboard first

Control Server/SCADA Server, Firewall (OT), Jump Host, VPN Server, Switch,
Engineering/Operator Workstations.

These combine easy or medium collection effort with critical importance. They form the
backbone of both IT-to-OT crossing detections and remote-access abuse detections — the two
most common real-world OT compromise paths.

### Tier 2 — Onboard next

PLC, Safety Controller, Data Gateway, Data Historian, HMI, IED, Router.

High or critical importance, but either harder to instrument directly (PLC, Safety
Controller) or lower urgency/volume (Historian, Router). Safety Controllers deserve special
handling: rare events here should always page out regardless of collection difficulty.

### Tier 3 — Fill coverage gaps

Application Server, DCS Controller, PAC, RTU, Network Traffic (SPAN/TAP/IDS).

Network Traffic monitoring is listed here not because it's low-value — it's arguably the
single most important source for protocol-level Sigma detections (Modbus, DNP3, OPC UA,
S7comm, IEC 104) — but because it demands the most engineering effort (SPAN/TAP
architecture, DPI tuning) before it produces usable signal.

### Tier 4 — Do not collect directly

Field I/O.

Sensors/actuators should never be targeted for direct log collection. Their state is
already represented indirectly through PLC/RTU telemetry and historian data — attempting
native collection here adds cost for near-zero marginal detection value.

## Reference table

| Source | Description | Log Ease | Noise | Source Count | Importance | Onboarding Priority / Notes |
|--------|-------------|----------|-------|--------------|------------|-----------------------------|
| Control Server / SCADA Server | Central server communicating with PLCs/RTUs and HMIs | Easy | Medium | Few | **Critical** | Tier 1 — onboard first. Best single vantage point for commands reaching the process. |
| Firewall (OT) | Segments zones, controls traffic between IT/DMZ/OT | Easy | Medium | Few | **Critical** | Tier 1 — cheapest high-value source. Confirms Purdue zone-crossing detections. |
| Jump Host | Secure access point into OT network (RDP/SSH) | Easy | Medium | Few | **Critical** | Tier 1 — every legitimate remote-access session should pass through here. Alert on anything that doesn't. |
| VPN Server | Secure remote connectivity into OT or between sites | Easy | Low | Very Few | **Critical** | Tier 1 — pairs with jump host logs for full remote-access chain visibility. |
| Switch | Connects devices, defines OT network segments | Medium | Low | Many | **Critical** | Tier 1 — port security, MAC changes, VLAN hopping detection; volume manageable if filtered to security events only. |
| PLC | Core automation controllers executing logic | Hard | Low | Many | **Critical** | Tier 2 — high value but limited native logging; often requires passive network monitoring (Nozomi/SPAN) as a proxy. |
| Safety Controller | Executes safety-critical logic with redundancy | Hard | Low | Few | **Critical** | Tier 2 — low volume but any event here is a priority-1 investigation regardless of source difficulty. |
| Workstations (Engineering/Operator) | Used for configuration, programming, diagnostics | Medium | High | Moderate | **Critical** | Tier 1 — Windows event logs are easy to collect; tune aggressively, this is usually the noisiest critical source. |
| Data Gateway | Protocol translation, aggregation, mirroring between zones | Medium | Medium | Few | **High** | Tier 2 — good chokepoint for cross-protocol detections (e.g. Modbus-to-OPC UA translation abuse). |
| Data Historian | Stores process data, events, alarms for analysis and business use | Easy | Low | Few | **High** | Tier 2 — easy win; also valuable for baselining process behavior, not just security events. |
| HMI | Operator interface for monitoring and control | Easy | Medium | Moderate | **High** | Tier 2 — watch for unauthorized setpoint changes, login anomalies, engineering-mode access outside change windows. |
| IED | Protection and control devices (mostly power sector) | Easy | Low | Many | **High** | Tier 2 — IEC 61850 GOOSE/MMS visibility if available; otherwise rely on substation gateway logs. |
| Router | Routes traffic between OT network segments | Medium | Low | Moderate | **High** | Tier 2 — complements firewall logs for east-west traffic between cells/zones. |
| Application Server | Hosts ICS applications (analytics, alarms, reporting) on Windows/Linux | Medium | Medium | Few | **Medium** | Tier 3 — standard Windows/Linux telemetry pipeline (Sysmon/auditd) applies directly. |
| DCS Controller | Manages continuous processes in distributed control systems | Hard | Low | Many | **High** | Tier 3 — vendor-specific logging is limited; prioritize network-based detection here. |
| PAC | Advanced programmable controller with extended capabilities | Hard | Low | Moderate | **Critical** | Tier 3 — same constraints as PLC; passive monitoring is the practical path. |
| RTU | Aggregates field data and forwards to SCADA | Hard | Low | Moderate | **High** | Tier 3 — geographically distributed, often serial-based; polling-based DNP3/104 monitoring recommended. |
| Network Traffic (SPAN/TAP/IDS) | Passive monitoring of OT protocols | Medium | Nightmare | Very Few | **High** | Tier 3 — highest engineering effort but fills every visibility gap above (PLC, PAC, RTU, DCS). Needs dedicated tuning and a Sigma/DPI ruleset. |
| Field I/O | Sensors and actuators providing raw input/output | Nightmare | Low | Very Many | **Low** | Tier 4 — do not attempt direct log collection; covered indirectly via PLC/RTU and process historian data. |

---

*Prepared for OT/ICS detection engineering — Help AG MSS Cyber Defense.*
