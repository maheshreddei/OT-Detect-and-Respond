# DNP3

## Snapshot
| Property | Value |
|----------|-------|
| Port/transport | TCP/20000 (also serial) |
| Purdue | L2 (SCADA master ↔ outstation); power/water |
| Auth | Base none; **DNP3-SA** (Secure Authentication) optional, often unused |
| Telemetry | Zeek `dnp3.log`, NDR, pcap |

## What it is
A SCADA protocol common in North American electric and water utilities, between a master and outstations (RTUs/IEDs). It has a richer object model than Modbus (points grouped by Group/Variation) and supports **unsolicited responses** (outstations reporting events without polling).

## What it really means for a defender
DNP3's control model is **select-before-operate**: to actuate a point the master issues Select then Operate (or Direct Operate) carrying a **CROB** (Control Relay Output Block) for binary outputs or an analog output block for setpoints. So the impact events are specific and detectable — Operate/Direct-Operate function codes to output points. As with IEC-104, these should come only from the sanctioned master. Two extra watch-items: **unsolicited-response anomalies** (a spoofed outstation feeding false telemetry) and **restart** functions (disruption). Where DNP3-SA is deployed, authentication failures are themselves a signal.

## Attacker actions (recon → impact)
- **Discover:** connect on TCP/20000; read (FC 1) to enumerate points; read outstation attributes.
- **Read (recon):** poll classes/points to map the process.
- **Command (impact):** Select (FC 3) + Operate (FC 4), or Direct Operate (FC 5), with a CROB (Group 12) or analog output (Group 41) — actuate a relay or write a setpoint.
- **Disrupt:** cold/warm restart (FC 13/14); spoof unsolicited responses (FC 130) to falsify the master's view.

## Detections you can build
| Detection | Signal / logic | Log source | ATT&CK ICS |
|-----------|----------------|------------|------------|
| Operate from non-master | FC 4/5 (operate/direct-operate) from outside master baseline | `dnp3.log` | T0855 Unauthorized Command Message, T0831 |
| CROB / analog-output write | Operate carrying Group 12 (CROB) or Group 41 (AO) | `dnp3.log` | T0836 Modify Parameter |
| Cold/warm restart | FC 13/14 to an outstation | `dnp3.log` | T0814 Denial of Service |
| Unsolicited-response anomaly | Unexpected FC 130 / spoofed outstation source | `dnp3.log` | T0856 Spoof Reporting Message |
| DNP3-SA auth failure | Secure-Auth challenge failures (where deployed) | `dnp3.log`/device | T0859 |
| New DNP3 client | First-time source speaking DNP3 | NDR + baseline | T0855 |
| Cross-zone DNP3 | TCP/20000 outside SCADA zone | firewall/NDR | T0885 |

## Log sources & telemetry
Zeek `dnp3.log` exposes function code, object group/variation, and IIN (Internal Indications) flags. NDRs carry DNP3 control policies. pcap decodes the CROB/AO value; historian confirms the actuated point moved.

## Functions/services to watch
**Read (recon):** FC 1 (read). **Command (impact):** FC 3 (select), 4 (operate), 5 (direct operate) — with Group 12 Var 1 (CROB) / Group 41 (analog output). **Disrupt:** FC 13 (cold restart), 14 (warm restart). **Reporting:** FC 130 (unsolicited response) — watch for spoofing. Watch IIN flags for device-need-time/restart indicators.

## ATT&CK mapping
T0855 Unauthorized Command Message · T0831 Manipulation of Control · T0836 Modify Parameter · T0856 Spoof Reporting Message · T0814 Denial of Service · T0885 Commonly Used Port.
