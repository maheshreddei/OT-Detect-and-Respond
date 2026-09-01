# OT SIEM Log Source Prioritization & Onboarding Guide

*A practical reference for sequencing log source onboarding by feasibility, noise, and security value.*

## How to read this

Each OT data source is rated on four practical axes: how **easy** the logs are to collect, how **noisy** the source typically is once collecting, how many **instances** of that source type usually exist in a given network, and its overall **security importance**. The onboarding **tier** translates those four axes into the order a Cyber Defense / MSS team should realistically bring sources into the SIEM — rather than trying to ingest everything on day one.

## Onboarding tiers

### Tier 1 — Onboard first
**Control Server / SCADA Server · Firewall (OT) · Jump Host · VPN Server · Switch · Engineering/Operator Workstations**

These combine easy or medium collection effort with critical importance. They form the backbone of both **IT-to-OT crossing** detections and **remote-access abuse** detections — the two most common real-world OT compromise paths.

### Tier 2 — Onboard next
**PLC · Safety Controller · Data Gateway · Data Historian · HMI · IED · Router**

High or critical importance, but either harder to instrument directly (PLC, Safety Controller) or lower urgency/volume (Historian, Router). **Safety Controllers deserve special handling: rare events here should always page out**, regardless of collection difficulty.

### Tier 3 — Fill coverage gaps
**Application Server · DCS Controller · PAC · RTU · Network Traffic (SPAN/TAP/IDS)**

Network Traffic monitoring is listed here not because it's low-value — it's arguably the single most important source for protocol-level Sigma detections (Modbus, DNP3, OPC UA, S7comm, IEC 104) — but because it demands the most engineering effort (SPAN/TAP architecture, DPI tuning) before it produces usable signal.

### Tier 4 — Do not collect directly
**Field I/O**

Sensors/actuators should never be targeted for direct log collection. Their state is already represented indirectly through PLC/RTU telemetry and historian data — attempting native collection here adds cost for near-zero marginal detection value.

## Reference table

| Source | Short description | Log ease | Noise | Count | Importance | Tier / notes |
|--------|-------------------|----------|-------|-------|------------|--------------|
| **Control Server / SCADA Server** | Central server communicating with PLCs/RTUs and HMIs | Easy | Medium | Few | **Critical** | **Tier 1** — best single vantage point for commands reaching the process |
| **Firewall (OT)** | Segments zones, controls IT/DMZ/OT traffic | Easy | Medium | Few | **Critical** | **Tier 1** — cheapest high-value source; confirms Purdue zone-crossing |
| **Jump Host** | Secure access point into OT (RDP/SSH) | Easy | Medium | Few | **Critical** | **Tier 1** — every legit remote session should pass here; alert on anything that doesn't |
| **VPN Server** | Remote connectivity into OT / between sites | Easy | Low | Very Few | **Critical** | **Tier 1** — pairs with jump host for full remote-access chain |
| **Switch** | Connects devices, defines OT segments | Medium | Low | Many | **Critical** | **Tier 1** — port security, MAC changes, VLAN hopping; filter to security events |
| **Workstations (Eng/Operator)** | Config, programming, diagnostics | Medium | High | Moderate | **Critical** | **Tier 1** — easy to collect; tune aggressively, usually the noisiest critical source |
| **PLC** | Core automation controllers executing logic | Hard | Low | Many | **Critical** | **Tier 2** — high value, limited native logging; often needs passive monitoring (Nozomi/SPAN) |
| **Safety Controller** | Safety-critical logic with redundancy | Hard | Low | Few | **Critical** | **Tier 2** — low volume; any event is a priority-1 investigation |
| **Data Gateway** | Protocol translation / aggregation between zones | Medium | Medium | Few | **High** | **Tier 2** — chokepoint for cross-protocol detections (e.g. Modbus↔OPC UA abuse) |
| **Data Historian** | Stores process data, events, alarms | Easy | Low | Few | **High** | **Tier 2** — easy win; also baselines process behavior, not just security |
| **HMI** | Operator monitoring/control interface | Easy | Medium | Moderate | **High** | **Tier 2** — unauthorized setpoint changes, login anomalies, off-window engineering mode |
| **IED** | Protection/control devices (power sector) | Easy | Low | Many | **High** | **Tier 2** — IEC 61850 GOOSE/MMS if available; else substation gateway logs |
| **Router** | Routes traffic between OT segments | Medium | Low | Moderate | **High** | **Tier 2** — complements firewall for east-west between cells/zones |
| **Application Server** | Hosts ICS apps (analytics, alarms, reporting) | Medium | Medium | Few | **Medium** | **Tier 3** — standard Windows/Linux pipeline (Sysmon/auditd) |
| **DCS Controller** | Manages continuous processes | Hard | Low | Many | **High** | **Tier 3** — vendor logging limited; prioritize network-based detection |
| **PAC** | Advanced programmable controller | Hard | Low | Moderate | **Critical** | **Tier 3** — same constraints as PLC; passive monitoring is the practical path |
| **RTU** | Aggregates field data, forwards to SCADA | Hard | Low | Moderate | **High** | **Tier 3** — distributed, often serial; polling-based DNP3/104 monitoring |
| **Network Traffic (SPAN/TAP/IDS)** | Passive OT protocol monitoring | Medium | Nightmare | Very Few | **High** | **Tier 3** — highest effort but fills every gap above (PLC/PAC/RTU/DCS); needs DPI + Sigma tuning |
| **Field I/O** | Sensors and actuators (raw I/O) | Nightmare | Low | Very Many | **Low** | **Tier 4** — do not collect directly; covered via PLC/RTU + historian |

## Onboarding principle
Sequence by **value-per-effort**: Tier 1 gives the highest detection value for the least engineering (IT-to-OT crossing + remote-access abuse — the two most common compromise paths). Network traffic (Tier 3) is the most valuable single source for protocol detections but the most engineering-heavy, so it comes once the quick wins are in and the SPAN/TAP architecture is ready. Never chase Field I/O directly.
