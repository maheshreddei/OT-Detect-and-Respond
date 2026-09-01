# Chapter 03 — HMI, SCADA, DCS, Historian, EWS and MES

> Part I · Foundations. Above the controllers sits the supervisory and information layer — the systems humans use to watch and command the process, and the systems that store its history. These are mostly Windows/Linux computers, which makes them both more familiar to an IT defender and the place where hands-on-keyboard OT attacks land.

## 3.1 HMI — the operator's window and hands

The **Human-Machine Interface (HMI)** is the screen an operator uses to monitor and control the process. It renders the plant as graphical mimics — tanks, pipes, pumps, live values — and lets the operator issue commands: start a pump, change a setpoint, acknowledge an alarm.

Two security truths about HMIs:

1. **A compromised HMI can issue legitimate commands.** Because the HMI is *supposed* to command the process, an attacker who controls it (via the host, via remote access, or via stolen credentials) can manipulate the process using entirely normal-looking actions. There is no malformed packet to catch — just a valid command from a valid source.
2. **A compromised HMI can lie to the operator.** By altering what the HMI displays, an attacker can hide the manipulation — showing normal values while the real process drifts. This is **Manipulation of View**, and it is exactly what made Stuxnet and the Ukraine grid attacks so effective: the operators could not see what was happening.

HMIs are frequently weakly secured — shared operator accounts, no lockout, default credentials, engineering-mode access left available, and old Windows underneath. Watch for **unauthorized setpoint changes, logins outside normal patterns, and engineering-mode access outside change windows.**

## 3.2 SCADA vs DCS — two shapes of supervision

**SCADA (Supervisory Control and Data Acquisition)** and **DCS (Distributed Control System)** both supervise the process, but they suit different plant shapes:

| | SCADA | DCS |
|---|-------|-----|
| Geography | **Distributed / wide-area** (pipelines, grids, water networks) | **Single site** (refinery, chemical plant, power station) |
| Model | A central master **polls** remote RTUs/PLCs | Tightly integrated controllers and I/O on a plant network |
| Latency tolerance | Higher (remote links) | Low (continuous, fast control) |
| Typical protocols | DNP3, IEC-104, Modbus | Vendor DCS protocols, OPC, Foundation Fieldbus |
| Examples | Water utility SCADA, gas pipeline | Emerson DeltaV, Honeywell Experion, Yokogawa Centum, ABB 800xA |

The distinction matters for defense mainly because it tells you *where the data and commands flow* and *what protocols to expect*. A SCADA master is a crown-jewel host — it can command many field sites. A DCS controller network is dense and continuous, so passive monitoring must be sized for volume.

## 3.3 The Historian — the memory of the plant

The **process historian** is a time-series database that records process values, events, and alarms — often millions of tags sampled over years. Its primary job is operational (trending, reporting, optimization), but for a defender it is one of the most valuable data sources in the entire plant, because it is the **physical record**.

With historian data you can ask questions no network log can answer:

- Is a value being driven toward a dangerous limit while the operator view looks normal?
- Was a setpoint written outside its approved range, or outside operating hours?
- Did a commanded action actually happen (command versus feedback)?
- Has a sensor value frozen (a sign of a replay or spoof)?

Common historians include **OSIsoft PI (now AVEVA PI)**, **Wonderware/AVEUA Historian**, and vendor-embedded historians. You do not collect *every* tag for security — you curate the tags that carry safety and process meaning (setpoints, trip points, critical measurements, bypass and mode states) and feed those to your SIEM. Chapter 17 develops the process-indicator detections this enables.

## 3.4 EWS — the crown-jewel host

The **Engineering Workstation (EWS)** is the computer engineers use to program controllers and configure the system. It holds the vendor engineering software (TIA Portal, Studio 5000, EcoStruxure, the SIS engineering tool) and the project files — the logic of the plant.

The EWS is the **single most important host to protect**, because it is the legitimate path to change controller logic. Reaching the EWS and using its own software is how the most consequential OT attacks work — **TRITON reached a safety controller through the engineering workstation.** Once an attacker is on the EWS, their actions look like engineering, so detection shifts from "what" to "who, when, and from where."

Guard the EWS like a domain controller: strict access control, MFA, application allow-listing, full endpoint logging (Windows Security + Sysmon), and tight monitoring of any remote session into it. Its project files should be backed up and integrity-checked so you can compare running logic against a known-good baseline (Chapter 26).

## 3.5 MES and the Level 3 information layer

The **Manufacturing Execution System (MES)** sits at Purdue Level 3, between the control systems below and the business systems (ERP) above. It manages production — recipes, batches, scheduling, quality, and production reporting — and therefore bridges OT and IT. MES and other Level 3 servers (application servers, reporting, alarm management) run on standard Windows/Linux and are onboarded with standard host telemetry (Sysmon/auditd), but their **position at the IT/OT seam** makes them a natural pivot point worth watching.

## 3.6 Putting the layer together

A mental map of who talks to whom:

```
  ENTERPRISE (L4/5) ── ERP, business IT
        │
  ── IT/OT DMZ (L3.5) ── the boundary you watch hardest
        │
  SITE OPS (L3) ── MES, historian, app servers, domain services
        │
  SUPERVISORY (L2) ── HMI, SCADA master, EWS
        │
  CONTROL (L1) ── PLC, RTU, PAC, safety controller
        │
  FIELD (L0) ── sensors, actuators
```

For defense, the priority targets in this chapter are clear: the **EWS and HMI** (where hands-on-keyboard OT attacks land) and the **historian** (where you prove physical impact). Instrument all three, and understand the SCADA/DCS shape so your monitoring matches how the plant actually communicates.

## Chapter summary

- The **HMI** both commands the process and shows it to the operator, so it can be used to manipulate control *and* hide it (Manipulation of View).
- **SCADA** is distributed/polled; **DCS** is single-site/integrated — this shapes protocols, data flow, and monitoring.
- The **historian** is the plant's physical memory and one of the best security data sources — curate its safety/process tags into the SIEM.
- The **EWS** is the crown-jewel host and the classic path to logic-level attacks; protect and monitor it like a domain controller.
- **MES/Level 3** bridges OT and IT and is a natural pivot to watch.

## Cross-references
- Chapter 05 places each component in the Purdue model.
- Chapter 09 treats the historian as a data source in detail.
- Chapter 26 (forensics) uses EWS artifacts and the logic baseline.
- Companion repositories: `ot-historian-detection`, `perimeter-to-endpoint-detections` (EWS/HMI host detections).
