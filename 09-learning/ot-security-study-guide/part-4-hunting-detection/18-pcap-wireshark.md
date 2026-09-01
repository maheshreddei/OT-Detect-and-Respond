# Chapter 18 — PCAP Analysis with Wireshark

> Part IV. Wireshark is how you read industrial traffic packet by packet — the microscope you reach for to confirm and detail an anomaly that a log or alert first surfaced.

## 18.1 What Wireshark is for

Wireshark answers one question extremely well: **"exactly what happened in this conversation?"** It is not a monitoring platform — it doesn't scale to continuous, network-wide detection (that's Zeek, Chapter 19). It is the deep-dive tool: given a suspicious conversation, Wireshark shows you the precise operations, values, and timing, frame by frame.

## 18.2 Dissectors and filters

Wireshark's **dissectors** decode industrial protocols into human-readable fields — Modbus, DNP3, S7comm, EtherNet/IP/CIP, IEC-104, BACnet, and more. The skill is **display filters** that separate reads from writes:

- Filter by protocol: `modbus`, `dnp3`, `s7comm`, `cip`, `iec60870_5_104`, `bacnet`.
- Filter to write/command operations (the impact): e.g. Modbus function codes 5/6/15/16, DNP3 operate, S7 program transfer, IEC-104 command ASDUs.
- Filter by endpoint: `ip.addr == <controller>` to scope to one device.
- Combine: a write function code, to a critical controller, from a non-master source.

You don't memorize every filter; you learn the pattern — *protocol + write-operation + endpoints* — and look up the exact field names per protocol.

## 18.3 An investigation workflow

1. **Scope** — filter to the conversation of interest (the two endpoints, the protocol).
2. **Establish normal** — what does this pair usually do? Reads at a steady rate? A known function set?
3. **Isolate the anomaly** — find the exchange that doesn't fit (an unexpected write, a program transfer, a new function code, a malformed/replayed frame).
4. **Extract the specifics** — the exact register/value written, the CIP service, the ASDU type and IOA, the block being downloaded.
5. **Corroborate** — line it up with the historian (did the process move?) and identity logs (who was on the source host?).

## 18.4 Safety and hygiene

- **Work from a copy.** Analyze captured PCAP offline; never generate traffic onto the OT segment while investigating (no active Wireshark features against live control).
- **Hash on collection** for chain of custody — OT incidents can become safety/regulatory investigations.
- **Capture at the right point** — from the TAP/SPAN that sees the relevant segment (Chapter 08); you can only analyze what was captured.

## 18.5 The handoff to scale

When a Wireshark deep-dive reveals a pattern worth watching continuously, hand it to **Zeek** (Chapter 19) to detect at scale, and to **detection engineering** (Chapter 20) to make it a durable rule. Wireshark finds and details; Zeek and the SIEM watch always.

## Chapter summary
- Wireshark answers **"exactly what happened in this conversation?"** — the deep-dive microscope, not a monitoring platform.
- Master the filter pattern: **protocol + write/command operation + endpoints.**
- Workflow: scope → establish normal → isolate anomaly → extract specifics → corroborate with historian/identity.
- **Work from hashed copies, offline**; capture from the right tap.
- Hand durable patterns to Zeek and detection engineering.

## Cross-references
- Chapter 06 (protocol structure) tells you what the fields mean; Chapter 19 (Zeek) scales it; Chapter 26 (forensics) uses PCAP as evidence.
