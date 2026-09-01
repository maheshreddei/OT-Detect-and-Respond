# Chapter 22 — Hunting on SIEM / XDR: Sentinel, Splunk, Elastic

> Part IV. This chapter is about hunting at scale on the platforms where your OT telemetry lands. The method is one thing; the query language is a dialect. Learn the method once and translate.

## 22.1 One method, many dialects

The same OT hunt — say, "a Modbus write to a critical controller from a source that isn't its master" — expresses differently on each platform:

- **KQL** on Microsoft Sentinel and Defender for IoT/XDR.
- **SPL** (and data models) on Splunk Enterprise Security.
- **ES|QL / EQL / Lucene** on Elastic.

The hypothesis, the data source, and the logic are identical; only the syntax changes. Anchor on the hunt (Chapter 16) and the data model, and the language becomes the easy part. A practitioner who understands the pattern can move between platforms in days.

## 22.2 Normalize with a data model

Fast, portable hunts depend on **normalized data**. Each platform has a schema:

- **Splunk CIM** (Common Information Model).
- **Sentinel ASIM** (Advanced Security Information Model).
- **Elastic ECS** (Elastic Common Schema).

Map your OT logs — Zeek/ICSNPP, firewall, host, historian — onto the relevant fields (source, destination, action, user, protocol) so a hunt references `src`/`dst`/`action` rather than raw, source-specific field names. Normalization is what lets one Sigma rule (Chapter 20) compile cleanly to all three backends and what makes cross-source correlation (network + host + identity) possible.

## 22.3 Defender for IoT and the Microsoft stack

Microsoft's **Defender for IoT** brings OT asset discovery and network detection into the Microsoft ecosystem, surfacing OT alerts and device context alongside endpoint (Defender for Endpoint) and identity (Entra) signals. Its value in hunting is **correlation across the seam**: an OT alert becomes far stronger when joined to the identity that logged into the jump host and the endpoint behavior on the EWS. If you run the Microsoft stack, this cross-domain correlation is the reason to integrate OT telemetry into it rather than siloing it.

## 22.4 Build a hunting practice, not one-off queries

Ad-hoc queries don't compound; a practice does:

- **Save hunts** as scheduled analytics/searches so they run continuously.
- **Track results** over time — a hunt that fires is a candidate detection; a hunt that never fires may indicate a data gap.
- **Promote** the good hunts to detections (Chapter 20) and retire the noisy ones.
- **Version** hunt logic alongside detections.

This turns hunting from an artisanal activity into a repeatable capability with measurable output (coverage, MTTD) — the same discipline the delivery playbook's KPIs and Threat Detection Assurance measure.

## 22.5 Worked hunt (platform-neutral logic)

Hypothesis: *an unauthorized host is writing to a critical PLC.*
1. Source: Zeek `modbus.log` (or NDR), normalized.
2. Filter to **write function codes** (5/6/15/16) targeting the critical-PLC asset group.
3. Exclude the **known master(s)** for that PLC (the command allow-list).
4. Anything remaining is a candidate — enrich with the identity/jump-host session active at that time and a historian check (did the process move?).
5. Confirmed pattern → promote to a scheduled detection with an MTTD target.

Expressed in KQL, SPL, or ES|QL the steps are the same; only the syntax differs.

## Chapter summary
- One hunting **method**, three **dialects** (KQL / SPL / ES|QL) — anchor on hypothesis and data model, not syntax.
- **Normalize** OT logs to CIM / ASIM / ECS so hunts are fast, portable, and correlatable.
- **Defender for IoT** adds OT context to the Microsoft stack; its power is cross-seam correlation.
- Build a **practice**: save, track, promote, retire, and version hunts — measurable output, not one-offs.

## Cross-references
- Chapter 09 (the telemetry hunted here), Chapter 16 (methodology), Chapter 20 (Sigma compiles to these), Chapter 21 (host/network sources).
- Companion: detection repos ship SPL + KQL; `threat-detection-assurance` measures MTTD on-platform.
