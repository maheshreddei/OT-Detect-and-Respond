# Chapter 19 — Zeek for ICS

> Part IV. Zeek turns raw industrial traffic into structured, huntable logs at scale — the workhorse that makes an OT network *queryable*. Where Wireshark is the microscope, Zeek is the always-on observatory.

## 19.1 What Zeek does

Zeek watches a network feed (from a TAP/SPAN) and, instead of storing packets, emits **structured logs** describing what happened: connections, protocol transactions, files, and more. Its `conn.log` records every conversation; protocol-specific logs record the semantics. This is the format your SIEM rules and Sigma detections run against — Zeek is the bridge from packets to detection.

## 19.2 ICSNPP — the industrial parsers

Base Zeek understands IT protocols; **ICSNPP (ICS Network Protocol Parsers)** extends it to industrial ones, producing per-protocol logs with function-level detail:

| Protocol | Zeek/ICSNPP log | Key fields |
|----------|-----------------|-----------|
| Modbus | `modbus.log` | function code, unit id, address, quantity |
| DNP3 | `dnp3.log` | function code, object/variation, IIN |
| S7comm | `s7comm.log` | rosctr, function, subfunction |
| EtherNet/IP + CIP | `enip.log`, `cip.log` | service, class, instance, tag |
| IEC 60870-5-104 | `iec104.log` | ASDU type, COT, IOA |
| BACnet | `bacnet.log` | service, object, property |
| OPC UA | `opcua*.log` | service, node id, security mode |
| IEC 61850 MMS | `mms.log` | service, domain, item |

These fields are exactly what you write detections against — "Modbus write function code from a source not in the master allow-list" is a query over `modbus.log`.

## 19.3 conn.log — the foundation

Even before deep protocol parsing, `conn.log` is invaluable. It yields the **conversation allow-list** and catches new pairs, scanning (one source to many destinations), and beaconing (regular intervals) — behavioral detections that need no DPI. In OT's stable environment, a *new* conversation in `conn.log` is high-signal on its own.

## 19.4 Deployment

- Zeek runs on the **passive capture** (Chapter 08), on the segments whose traffic you need to see.
- Forward Zeek logs to the **SIEM** (Chapter 22) for correlation, retention, and detection at scale.
- **Verify parser coverage:** confirm ICSNPP actually parses *your* protocols and versions. If a protocol you care about isn't producing a log, that's a **blind spot** to close before writing detections for it — the classic "we have a Modbus rule but Modbus isn't being parsed" failure that Threat Detection Assurance is designed to catch.

## 19.5 From Zeek to detection

The pipeline is: **TAP → Zeek+ICSNPP → structured logs → SIEM → Sigma/SPL/KQL detection.** Chapter 20 writes the rules; Chapter 22 runs them on the platform. Zeek's job is to make the traffic queryable and consistent so those rules are simple and reliable. If Zeek sees it and parses it, you can detect on it; if it doesn't, no rule downstream can help.

## Chapter summary
- Zeek converts traffic into **structured, queryable logs** — the always-on complement to Wireshark.
- **ICSNPP** adds industrial protocol parsers with function-level fields — the substrate for OT detections.
- **conn.log** alone catches new conversations, scanning, and beaconing (no DPI needed).
- Deploy on the passive capture, forward to the SIEM, and **verify parser coverage** (unparsed protocol = blind spot).
- Zeek makes the traffic detectable; the rules live downstream.

## Cross-references
- Chapter 08 (capture) feeds Zeek; Chapter 06 (protocols) explains the fields; Chapters 20/22 build and run the rules.
- Companion: `ot-protocol-defense` (per-protocol log fields), TDA (verify the parsing/feed).
