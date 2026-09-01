# Log Sources & Telemetry

You cannot detect what you cannot see. This is the master guide to *what telemetry sees which protocol*, so every detection in the per-protocol pages has a feed behind it. The short version: **network monitoring is primary for OT protocols; host logs cover the IT/access protocols; the historian confirms physical impact.**

## The telemetry stack, by priority

### 1. OT network monitoring (Zeek + ICSNPP, Nozomi, Dragos, Claroty) — primary
Passive, non-disruptive deep-packet inspection is the backbone of OT protocol detection. It parses control protocols into structured fields you can alert on.

- **Zeek with ICSNPP** (ICS Network Protocol Parsers) gives per-protocol logs with function-level detail. The parsers relevant here:

  | Protocol | Zeek/ICSNPP log | Key fields |
  |----------|-----------------|-----------|
  | Modbus | `modbus.log` (+ ICSNPP detail) | func, unit_id, address, quantity |
  | S7comm | `s7comm.log` | rosctr, function, subfunction |
  | DNP3 | `dnp3.log` | func code, object/variation, IIN |
  | IEC 60870-5-104 | `iec104.log` (ICSNPP) | ASDU type, COT, IOA |
  | EtherNet/IP + CIP | `enip.log`, `cip.log` | CIP service, class, instance, tag |
  | OPC UA | `opcua*.log` (ICSNPP-opcua-binary) | service, node id, security mode |
  | BACnet | `bacnet.log` | service, object type, instance, property |
  | IEC 61850 MMS | `mms.log` / ICSNPP-61850 | MMS service, domain, item |
  | DNS/HTTP/FTP/SSL | `dns/http/ftp/ssl.log` | standard Zeek fields |

- **Nozomi Guardian / Dragos / Claroty** produce the same visibility as vendor products, plus **asset inventory, baselines, and prebuilt OT alerts** (unauthorized write, new asset, protocol anomaly). Forward their alerts *and* the underlying session detail to the SIEM.

- **Sensor placement is everything.** A sensor sees only the traffic on the segments it taps. Tap the control segments (SPAN/tap at the L2/L3 switches and at zone conduits). Note that **Layer-2 protocols (IEC 61850 GOOSE/SV, PROFINET DCP)** are only visible to a sensor on that physical LAN segment — a north-of-boundary tap won't see them.

### 2. Full packet capture (pcap) — ground truth
Tap/SPAN capture on the relevant segment. Where an alert says "a write occurred," the pcap shows *which register to what value*. Expensive to keep at volume; capture continuously on critical segments if you can, or trigger-capture on NDR alerts. Hash on collection.

### 3. Boundary & flow telemetry
- **IT/OT firewall logs** — the single best source for *cross-zone* protocol attempts (Modbus from IT, IEC-104 from outside SCADA). Allow and deny both matter.
- **NetFlow/IPFIX** — flow shape and volume; catches scanning, new pairs, and beaconing even without DPI.
- **Switch/router** — ARP/MAC tables (device presence), port-security events.

### 4. Host & application logs — primary for IT/access protocols
For HTTP, VNC, FTP, RDP, SSH — the endpoints hold the record:
- **Windows Security/Sysmon** on EWS/HMI/historian hosts — logons (4624/4625), process creation (4688/Sysmon 1), network connections (Sysmon 3), service installs (7045). See the IT/OT IR evidence guide for detail.
- **Application logs** — OpenPLC/web-UI access & auth logs, FTP server logs, VNC server logs.
- **Auth/identity** — AD, VPN/remote-access gateway, MFA/PAM for the sessions that carried the access.

### 5. Endpoint on control devices — limited
PLCs/IEDs rarely produce useful logs, but where available: controller **diagnostic buffers / event logs** record mode changes (RUN/STOP/PROGRAM) and download events — pull these read-only during investigation (not usually streamed).

### 6. Historian — impact confirmation
Not a protocol source, but decisive: when a write/command detection fires, the **historian trend + alarm journal** proves whether the process actually moved. Pair every write/command detection with a historian check to separate a probe from an impact.

## Mapping to MITRE ATT&CK for ICS data sources
This telemetry realizes the ICS data sources the techniques expect:
- **Network protocol analysis / Packet capture** → Zeek/ICSNPP, Nozomi, pcap (the bulk of OT protocol detection).
- **Application Log** → web-UI/FTP/VNC/engineering-tool logs.
- **Operational Databases (Process History/Live Data, Process/Event Alarm)** → historian, for impact.
- **Authentication logs / Logon Session** → identity for the access protocols.
- **Asset Inventory** → NDR inventory, for new-asset detections.

## Minimum viable telemetry for this guide's detections
If you can only stand up a few things, in order:
1. **Zeek+ICSNPP (or an NDR) on the control segments** — unlocks almost every OT-protocol detection here.
2. **IT/OT firewall logs to the SIEM** — cross-zone attempts, cheap and high-signal.
3. **Windows host logs (EDR/Sysmon) on EWS/HMI** — the IT/access protocols and hands-on-keyboard.
4. **Historian feed** — impact confirmation.
5. **NetFlow** — breadth where DPI doesn't reach.

Everything in [`../detections/detection-catalog.csv`](../detections/detection-catalog.csv) names the log source it needs; cross-check against what you have to find your gaps.
