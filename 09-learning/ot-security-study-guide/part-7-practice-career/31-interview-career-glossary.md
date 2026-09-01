# Chapter 31 — Interview Questions, Career and Glossary

> Part VII. This closing chapter helps you convert the knowledge in this guide into a role, and gives you the vocabulary to speak the field fluently.

## 31.1 Interview themes (understand, don't memorize)

OT security interviews probe understanding, not recall. Be ready to reason through:

- **OT vs IT priorities** — the safety/availability inversion and why it changes security decisions (Chapter 01).
- **The Purdue model** — the levels, the DMZ, and why boundary crossing is a top detection (Chapter 05).
- **"How would you detect X?"** — an unauthorized write, a program download, a setpoint change, an SIS manipulation — reason from telemetry (network/host/historian) to a detection (Chapters 17, 20).
- **Safety-first IR** — operations decides, safety vetoes, containment is constrained (Chapter 25).
- **Passive-before-active** — why you don't scan control devices, and what you do instead (Chapters 08, 16).
- **Consequence-based risk** — prioritizing by physical impact, not CVSS (Chapters 01, 13).

Answer with the *reasoning*, and where you can, with a concrete example from your lab or portfolio — demonstrated capability beats recited definitions.

## 31.2 Common mistakes to avoid

Interviewers (and plants) watch for the tells of someone who treats OT like IT:

- Proposing to **active-scan** or patch-on-a-schedule control devices.
- Wanting to **isolate/power off** a controller as a first containment move.
- **Over-committing on containment** you don't control (ignoring operations' authority).
- Relying on **atomic IOCs** instead of behavioral and process indicators.
- Forgetting **safety** — treating an SIS event as just another alert.

Avoiding these signals maturity more than any certification.

## 31.3 Certifications that map to this guide

- **GICSP** (GIAC Global Industrial Cyber Security Professional) — broad OT security.
- **SANS ICS410** (ICS/SCADA security essentials) and **ICS515** (ICS active defense and incident response / threat hunting).
- **IEC 62443** credentials — for the standards/architecture side.
- **Vendor certifications** — Nozomi, Dragos, Claroty for platform skills.
- Foundational IT security certs remain valuable, since Stage-1 of OT attacks is IT.

Certifications open doors; a portfolio of real detection and hunting work walks you through them.

## 31.4 Career arc

A common and effective path: **IT SOC analyst → OT SOC analyst → OT detection engineer / threat hunter → OT security lead / architect.** At each step, build visible evidence of capability — detection libraries, hunting playbooks, a home lab, write-ups. The field is small and rewards demonstrated, hands-on skill; a public body of work (like the companion repositories this guide references) is often what distinguishes candidates.

## 31.5 Glossary

Keep this living list fluent — using the vocabulary correctly signals credibility:

- **BPCS** — Basic Process Control System (the DCS/PLC layer).
- **DCS** — Distributed Control System (single-site continuous control).
- **EWS** — Engineering Workstation (programs controllers; crown-jewel host).
- **HMI** — Human-Machine Interface (operator screens).
- **ICS** — Industrial Control System (umbrella term).
- **IED** — Intelligent Electronic Device (protection/control, power sector).
- **IOA / IOC** — Indicator of Attack (behavior) / Compromise (atomic artifact).
- **LOPA** — Layers of Protection Analysis (risk method crediting independent layers).
- **MES** — Manufacturing Execution System (Level 3 production management).
- **MOC** — Management of Change (authorized, recorded change process).
- **PFD** — Probability of Failure on Demand (SIF failure measure).
- **PLC / PAC / RTU** — controllers (logic / advanced / remote-telemetry).
- **Purdue model** — the level hierarchy (0–5 + DMZ) of a plant.
- **SCADA** — Supervisory Control and Data Acquisition (distributed supervision).
- **SIF / SIS** — Safety Instrumented Function / System.
- **SIL** — Safety Integrity Level (1–4).
- **Zone / conduit** — IEC 62443 segmentation constructs.

## Chapter summary
- Interviews probe **understanding** — OT vs IT, Purdue, "how would you detect X," safety-first IR, passive-first, consequence-based risk — answered with reasoning and lab/portfolio examples.
- Avoid the **IT-thinking tells** (active-scanning, power-off containment, ignoring operations' authority, atomic-IOC reliance, forgetting safety).
- Map your growth to **GICSP, SANS ICS410/515, IEC 62443, vendor certs**, backed by a **portfolio.**
- Career arc: IT SOC → OT analyst → detection engineer/hunter → lead/architect; **demonstrated capability wins.**
- Keep the **glossary** fluent.

## Cross-references
- This chapter synthesizes the whole guide; Chapters 29–30 build the portfolio and lab that back your answers.
