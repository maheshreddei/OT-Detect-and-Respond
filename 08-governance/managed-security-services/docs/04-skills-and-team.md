# 04 — Skills & Team

The people gap is usually the real constraint. Plan it as train + hire + partner — rarely just one.

## Skills required (map current team against these)
- **OT protocols & fundamentals** — Modbus, DNP3, S7, OPC UA, IEC-104/61850; Purdue model; IEC 62443.
- **OT threat landscape** — ICS threat actors, MITRE ATT&CK for ICS, ICS malware (TRITON, INDUSTROYER, PIPEDREAM).
- **OT detection engineering** — protocol, historian/physics, safety-system detection; Sigma; NDR query languages (e.g. N2QL).
- **OT-safe IR & forensics** — passive acquisition, evidence handling, operations-in-the-loop response.
- **Platform** — the chosen NDR (Nozomi/Dragos/Claroty), SIEM/SOAR integration.
- **Doctrine** — safety-first, passive-before-active — as much mindset as skill.

Use [`../templates/skills-matrix.md`](../templates/skills-matrix.md) to score each person.

## Train / hire / partner (decide per gap)
- **Train** your existing nucleus — analysts with network/DFIR/threat-hunting strengths adapt well. Certs: **GICSP, SANS ICS410 / ICS515 (ICS threat hunting & IR)**, vendor academies (Nozomi/Dragos/Claroty). Build a structured ramp, not ad-hoc.
- **Hire** one or two experienced OT people to **anchor** the team and lead detection engineering / architecture — credibility with clients and a mentor for the nucleus.
- **Partner** where you're thin — SIs for on-site deployment, contractors for surge, vendor PS for complex builds — while you build internal depth.

## Target roles (scale with the service)
| Role | Focus |
|------|-------|
| **OT Security Lead / Architect** | Owns capability, architecture, client engagements, standards |
| **OT Detection Engineer** | Builds & tunes detections (protocol/physics/safety) |
| **OT SOC Analysts (L1–L3)** | Monitoring, triage, investigation (OT-capable) |
| **Deployment Engineer** | Sensor install, SIEM integration |
| **(Shared) SOAR / platform, pre-sales, delivery mgmt** | Reuse from existing MSS |

Start lean: an anchor lead + a trained nucleus + shared MSS functions can run a pilot and Essential tier; scale analysts as clients onboard.

## Culture / doctrine
Bake in from day one: **safety outranks everything; monitoring is passive/read-only; operations decides for the process.** This is what separates a credible OT SOC from an IT SOC pointed at OT — and what earns trust with plant engineers.
