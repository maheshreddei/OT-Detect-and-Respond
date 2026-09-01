# Chapter 06 — Industrial Protocols in Depth

> Part II · Protocols, Visibility & Telemetry. Protocols are where an attacker's intent becomes an action on the wire, and where your detections live. This chapter gives you a working model for *any* OT protocol, then the specifics of the major ones.

## 6.1 The unifying model

Learn one idea and every protocol becomes readable:

> Most OT protocols have **no authentication, no authorization, and no encryption.** A reachable client can therefore **read** (reconnaissance) or **write/command** (impact) at will. There is no "unauthorized" flag on the wire — an attacker's write looks identical to an engineer's. **Your detection layer is the authorization the protocol never had.**

So for each protocol, answer three questions and you can defend it:
1. **Who legitimately speaks it to whom?** (the command allow-list — source, destination, direction)
2. **Which operations are reads (recon) and which are writes/commands (impact)?** (the function codes/services)
3. **Where does it sit in Purdue, and should it ever cross a zone boundary?**

The severity model falls straight out: a **write/command from a source not on the allow-list**, especially crossing a boundary or outside hours, is close to a true positive by construction.

## 6.2 The major protocols

### Modbus (TCP/502)
The simplest and most widespread. A master reads/writes numbered items (coils, registers) on a slave by **function code**. The read/write split is explicit in the code:
- **Reads (recon):** FC1 read coils, FC2 read discrete inputs, FC3 read holding registers, FC4 read input registers.
- **Writes (impact):** FC5 write single coil, FC6 write single register, FC15 write multiple coils, FC16 write multiple registers.
- **Recon/disrupt:** FC43/0x2B read device identification, FC8 diagnostics (sub-functions can restart comms / force listen-only).
No authentication whatsoever. Detection centers on write FCs from non-masters and diagnostic abuse.

### DNP3 (TCP/20000)
Utility SCADA (electric/water), master↔outstation, richer object model (Group/Variation). Control uses **select-before-operate**: Select (FC3) then Operate (FC4), or Direct Operate (FC5), carrying a **CROB** (Control Relay Output Block, Group 12) for binary outputs or an analog output block (Group 41) for setpoints. Watch operate function codes from non-masters, cold/warm restart (FC13/14), and spoofed **unsolicited responses** (FC130) that falsify the master's view. DNP3-SA (Secure Authentication) exists but is often unused.

### S7comm (TCP/102)
Siemens proprietary, used by STEP7/TIA Portal. Carries the crown-jewel operations: **PLC STOP/START**, and **program upload/download** (block transfer). Reading the SZL/system status is fingerprinting. A program download or STOP from anything but the sanctioned EWS is the Stuxnet-class event. S7comm-Plus adds integrity/anti-replay on newer CPUs (still researched).

### EtherNet/IP + CIP (TCP/44818, UDP/2222)
Rockwell and many vendors. Carries **CIP** (Common Industrial Protocol) — an object model of classes/instances/attributes; Rockwell exposes **symbolic tags**. Reads are Get_Attribute; **writes are Set_Attribute / tag writes** (impact). Discovery via **ListIdentity** (UDP/44818, often broadcast) enumerates every device loudly. `forward_open` establishes connected sessions. Watch tag/attribute writes from non-controllers and ListIdentity sweeps.

### IEC 60870-5-104 (TCP/2404)
Electric-power telecontrol (control center ↔ substation). Data is **ASDUs** addressed to **IOAs**, with a **Cause of Transmission (COT)**. **Monitor** ASDUs report; **command** ASDUs operate: C_SC (45, single command), C_DC (46, double), C_RC (47, regulating step), C_SE (48–50, setpoint). Interrogation (C_IC, 100) dumps the point list. A command ASDU from a non-master can open a breaker — top severity.

### IEC 61850 (MMS over TCP/102; GOOSE and SV on Layer 2)
Substation automation. Three sub-protocols: **MMS** (client/server, read/write named variables, control operations), **GOOSE** (fast L2 multicast event/trip messaging between IEDs), **Sampled Values** (streamed measurements). GOOSE is unauthenticated L2 multicast that IEDs *trust* — a spoofed GOOSE with a higher **stNum** can force or block a trip, and it is only visible on the physical LAN. Watch MMS control writes and GOOSE stNum/sqNum anomalies (requires an L2 tap).

### OPC UA (TCP/4840)
The modern, secure-capable protocol — a structured **address space** of nodes browsed/read/written/subscribed. Unlike the legacy protocols, it *supports* authentication, signing, and encryption. The risk is **misconfiguration**: anonymous sessions or SecurityMode None. **Browse** is recon; **Write / CallMethod** are impact. Watch anonymous/None sessions and writes to control nodes.

### BACnet/IP (UDP/47808)
Building automation (HVAC, lighting, sometimes access control). Objects (AI/AO/BI/BO/AV/BV) with properties (notably present-value). **Who-Is** broadcast enumerates devices; **ReadProperty** is recon; **WriteProperty** to a command object is impact; **DeviceCommunicationControl** and **ReinitializeDevice** are disruptive. Increasingly bridges to process OT.

### PROFINET and MQTT (brief)
- **PROFINET** — Siemens/others real-time Ethernet; DCP for discovery; hard real-time variants must never be touched inline.
- **MQTT (TCP/1883)** — IIoT publish/subscribe via a broker; risk is the broker's topic access control — wildcard subscribes (mass recon) and publishes to command topics (impact).

## 6.3 A defender's protocol cheat-pattern

For any protocol you meet, fill this in from its spec and confirm against your environment:

| Question | How to answer |
|----------|---------------|
| Port/transport | Protocol reference |
| Purdue placement | Where its speakers live |
| Read operations (recon) | The get/read/monitor codes |
| Write/command operations (impact) | The set/write/operate codes |
| Disruptive operations | Stop/restart/reinit/diagnostics |
| Legitimate speakers | Your command allow-list |
| Should it cross a boundary? | Almost always no for control protocols |

## 6.4 Confirm before you detect

Two things vary by vendor and deployment and must be confirmed with your own traffic before writing detections: the **protocol token** your tooling uses (how it labels the protocol) and the **exact function/service code numbers** present. Run a protocol inventory (Chapter 19) first, then instantiate the detection patterns with real values.

## Chapter summary
- One model fits all: **no auth; reads = recon, writes = impact; detection is the missing authorization.**
- Learn each protocol's **read vs write operations**, legitimate speakers, and Purdue placement.
- Modbus (function codes), DNP3 (select-before-operate/CROB), S7comm (program/STOP), ENIP/CIP (tag writes/ListIdentity), IEC-104 (command ASDUs), IEC 61850 (MMS + L2 GOOSE/SV), OPC UA (misconfig/anonymous), BACnet (WriteProperty) — with the specific codes that constitute impact.
- Confirm protocol tokens and codes against your own environment before deploying rules.

## Cross-references
- Chapter 19 (Zeek/ICSNPP) parses these into huntable logs; Chapter 20 turns the write operations into detections.
- Companion repository: `ot-protocol-defense` (13-protocol defender guide, 54 detections, Nozomi queries).
