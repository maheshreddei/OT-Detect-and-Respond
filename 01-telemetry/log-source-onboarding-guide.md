# OT SIEM Log Source Prioritization & Onboarding Guide

*A practical reference for sequencing log source onboarding by feasibility, noise, and security value.*

## How to read this

Each OT data source is rated on four practical axes: how easy the logs are to collect
(**Log Ease**), how noisy the source typically is once collecting (**Noise**), how many
instances of that source type usually exist in a given network (**Source Count**), and its
overall **Importance**. The onboarding tier translates those four axes into the order in
which a Cyber Defense / MSS team should realistically bring sources into the SIEM, rather
than trying to ingest everything on day one.

The machine-readable version of the table below lives in `log-source-inventory.csv`;
collection/parser detail is in `parser-mapping.csv`; and the outcome mapping from each
source to detection, validation evidence, and response playbooks is in
`detection-response-linkage.csv`.

## Collection boundary

“OT telemetry” means telemetry needed to defend the OT mission, not only packets captured
inside Levels 0–2. Keep IT-side data when it establishes the route into OT (identity, VPN,
jump host, IDMZ firewall), describes activity on an OT-serving host, or helps confirm
operational impact. Do not duplicate unrelated enterprise telemetry in the OT pipeline.

Every source must have a named detection use, a validation role, an owner, and a response
playbook. If it has none, do not onboard it merely because it is available.

## Onboarding tiers

### Tier 1 — Onboard first

Control Server/SCADA Server, Firewall (OT), Jump Host, VPN Server, Switch,
Engineering/Operator Workstations, OT Identity/Directory.

These combine easy or medium collection effort with critical importance. They form the
backbone of both IT-to-OT crossing detections and remote-access abuse detections — the two
most common real-world OT compromise paths.

### Tier 2 — Onboard next

PLC, Safety Controller, Data Gateway, Data Historian, HMI, IED, Router,
Backup/Recovery Platform.

High or critical importance, but either harder to instrument directly (PLC, Safety
Controller) or lower urgency/volume (Historian, Router). Safety Controllers deserve special
handling: rare events here should always page out regardless of collection difficulty.

### Tier 3 — Fill coverage gaps

Application Server, DCS Controller, PAC, RTU, and expansion of Network Traffic
(SPAN/TAP/IDS) beyond the initial boundary pilot.

Network Traffic monitoring is phased. One boundary sensor is an early minimum-viable
control because it exposes IT/OT crossings and remote-access paths. Extending sensors to
every cell/area is Tier 3 because SPAN/TAP architecture, asset context, protocol parsing,
and tuning require more engineering. This distinction removes the apparent conflict
between collection priority and rollout effort.

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
| OT Identity / Directory | Directory and identity services used by OT users, systems, and remote access | Easy | Medium | Very Few | **Critical** | Tier 1 — scope to OT identities and dependencies; detect account, privilege, policy, and authentication abuse. |
| Backup / Recovery Platform | Backups for OT hosts, applications, and controller projects | Easy | Low | Very Few | **High** | Tier 2 — detect tampering and preserve evidence that a safe recovery point actually exists. |
| Field I/O | Sensors and actuators providing raw input/output | Nightmare | Low | Very Many | **Low** | Tier 4 — do not attempt direct log collection; covered indirectly via PLC/RTU and process historian data. |

---

*OT/ICS detection engineering — original content authored by Mahesh Reddy.*
