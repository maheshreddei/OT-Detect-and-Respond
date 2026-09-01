# Chapter 30 — Hands-On Labs and Purple Team

> Part VII. Knowledge becomes skill through repetition, and detections become trustworthy through testing. This chapter turns the home lab into a training ground and introduces purple-teaming as the safe way to prove OT detections work.

## 30.1 A progression of guided exercises

Build skill in order, each exercise on the isolated lab of Chapter 29:

1. **Capture and read traffic** — tap the lab network, open the capture in Wireshark, identify the protocols and the read/write operations (Chapters 06, 18).
2. **Build the allow-lists** — from Zeek logs, derive the conversation and command allow-lists for the lab (Chapters 08–09, 19).
3. **Detect an unauthorized write** — issue a Modbus write from a non-master and confirm your detection fires (Chapters 20, 22).
4. **Catch a program download / mode change** — perform an S7 transfer or key-switch change and validate the detection (Chapters 02, 12).
5. **Spot a setpoint anomaly** — drive a historian value/setpoint outside range and catch it with a process-indicator detection (Chapter 17).
6. **Run an end-to-end hunt** — start from a hypothesis, work the data, reach a conclusion, and produce a detection (Chapter 16).

Each exercise reinforces a chapter and leaves behind a working, tested detection.

## 30.2 Purple team in OT

**Purple teaming** is red (attack) and blue (defense) working together to test and improve detection. In OT it has a strict form: you test detections against **real techniques** but **never against a real process.**

The method:
- **Run the technique in the lab**, or **replay a crafted PCAP** of the technique to the sensor, or **inject a representative event** into the SIEM.
- **Validate** that the detection fires, with the right fidelity, within an acceptable MTTD.
- **Measure** the result — pass/fail, MTTD, and a remediation for anything that missed.

This is exactly the Threat Detection Assurance discipline: log validation, logic testing, blind-spot discovery, false-positive reduction, and speed — done as a collaborative exercise.

## 30.3 Never live

The cardinal rule: **purple-teaming a production plant does not mean attacking it.** For production OT you use only the safe methods — lab replication, PCAP replay to the sensor, event injection, and tabletop for destructive or safety-relevant scenarios. A live attack simulation against a running process or a safety system is never acceptable. The lab exists precisely so you can run real techniques safely.

## 30.4 Measure and improve

Every exercise and purple-team run produces measurable output: which detections passed, which missed, the MTTD achieved, and a remediation backlog for the gaps. Track these over time and you convert practice into a trend — coverage rising, MTTD falling, blind spots closing. That measurement loop is what makes the difference between "we think we'd catch it" and "we proved we catch it."

## Chapter summary
- Build skill through a **progression of lab exercises**, each reinforcing a chapter and leaving a tested detection.
- **Purple team** = testing detections against real techniques collaboratively — the practical form of Threat Detection Assurance.
- In OT, **never live**: use lab replication, PCAP replay, event injection, and tabletop for production.
- **Measure** every run (pass/fail, MTTD, remediation) to turn practice into a coverage trend.

## Cross-references
- Chapter 29 (the lab), Chapter 16 (hunting), Chapter 20 (detections under test), Chapter 03/05 of the TDA companion.
- Companion: `threat-detection-assurance` (the validation framework), the open-source OT lab.
