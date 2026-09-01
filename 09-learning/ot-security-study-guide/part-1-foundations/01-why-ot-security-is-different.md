# Chapter 01 — Why OT Security Is Different

> Part I · Foundations. This chapter establishes the mental model that every later chapter depends on. If you come from IT security, the single most valuable thing you can do is *un-learn* a few reflexes before you touch a plant.

## 1.1 The one table that changes everything

In enterprise IT the guiding priority is **CIA — Confidentiality, Integrity, Availability**, usually in that order. Protecting data is the mission. In operational technology the order inverts and a new priority moves to the very top:

| Rank | IT priority | OT priority |
|------|-------------|-------------|
| 1 | Confidentiality | **Safety** (of people and environment) |
| 2 | Integrity | **Availability** (the process keeps running) |
| 3 | Availability | **Integrity** (of the process and its data) |
| 4 | — | Confidentiality |

Safety is not even on the classic IT list, yet in OT it outranks everything. The reason is simple and non-negotiable: a control system moves physical things — valves, motors, turbines, breakers, robotic arms, boilers. If security action stops a process at the wrong moment, or a safety function is defeated, people can be hurt and the environment can be harmed. No amount of data protection justifies a safety event.

This inversion is not a slogan; it changes concrete decisions. In IT, "when in doubt, isolate the host" is sound. In OT, isolating a live controller can trip a process or blind an operator at exactly the wrong moment. In IT, a vulnerability scan is routine hygiene. In OT, an aggressive scan can knock a fragile legacy device offline. The same action that is *responsible* in IT can be *dangerous* in OT.

## 1.2 What "consequence" really means

The word that separates OT risk from IT risk is **consequence**. An IT breach is measured in records exposed, downtime, and remediation cost. An OT incident is measured in:

- **Human harm** — injury or loss of life from a runaway process or a defeated safety system.
- **Environmental harm** — a release, spill, or emission.
- **Physical destruction** — equipment damaged beyond repair (a centrifuge, a turbine, a transformer).
- **Production loss** — a stopped process that can cost enormous sums per hour and take days to safely restart.
- **Cascading effects** — loss of a utility (power, water, gas) that affects a whole region.

Because the worst outcomes are physical and sometimes irreversible, OT risk is **consequence-driven**, not likelihood-driven and not data-driven. A vulnerability with a modest CVSS score on a device that can open a breaker outranks a "critical" CVE on a device that can only affect a report. You will see this principle return again and again: **prioritize by what the compromise can do to the physical process.**

## 1.3 Ten structural differences you must internalize

OT environments differ from IT in ways that are structural — baked into how plants are designed and operated. Each one has a direct security consequence.

**1. Determinism.** Control loops execute on fixed, predictable cycle times (often milliseconds). The system is engineered so that the same inputs produce the same outputs at the same time. Anything that introduces unexpected latency or load — including a well-meaning security tool — can disrupt control. *Consequence:* prefer passive tools; never assume "a quick scan won't hurt."

**2. Long asset lifetimes.** IT refreshes hardware every 3–5 years; OT assets run for 15–30 years. A plant commissioned in 2005 may still run the controllers, operating systems, and protocols of its era. *Consequence:* you will defend systems that cannot be upgraded and were never designed with security in mind.

**3. Patching is rare and hard.** Patching a controller usually requires a plant outage, vendor validation, and a management-of-change process. Outages are scheduled months in advance and cost money. *Consequence:* vulnerabilities persist by design; you compensate with segmentation and detection, not patching.

**4. Insecure-by-design protocols.** Most industrial protocols (Modbus, DNP3, S7comm, EtherNet/IP, IEC-104) have **no authentication, no authorization, and no encryption**. They were built for isolated, trusted networks where the network *was* the security boundary. *Consequence:* any host that can reach a device can command it; your detection layer supplies the authorization the protocol never had.

**5. Vendor and integrator access.** Plants depend on OEM vendors and system integrators who need remote or on-site access to maintain equipment. This access is frequently broad, standing, and under-monitored. *Consequence:* remote access and the supply chain are among the most common real intrusion paths.

**6. Few endpoint agents.** You cannot install an EDR agent on a PLC, an RTU, or most HMIs. Endpoint visibility exists only on Windows engineering and operator stations. *Consequence:* the network and the historian carry most of your visibility; plan for the agent gap.

**7. Physical consequence.** Already covered, but it bears repeating as a structural fact: the output of an OT system is physical motion and energy, not data. *Consequence:* safety-first, always.

**8. Change is rare and documented.** A well-run plant changes slowly and records every change through management of change (MOC). New assets, new logic, and new communication paths are events, not background noise. *Consequence:* this is a gift to defenders — deviations from a documented, stable baseline are unusually high-signal.

**9. Small, knowable populations.** An OT network has a bounded, enumerable set of devices and conversations that rarely changes. IT networks are large and chaotic; OT networks are small and stable. *Consequence:* baselining works far better in OT than in IT, and "something new" is genuinely suspicious.

**10. The people are different.** OT is owned by process and control engineers whose job is to keep the plant running safely. They hold authority over the process and can stop your activity at any time. *Consequence:* security acts *with* operations, never around them. You are a guest on the plant floor.

## 1.4 The air-gap myth

For years OT was assumed to be safe because it was "air-gapped" — physically disconnected from IT and the internet. That assumption is now false in almost every plant. Business demands (remote monitoring, cloud analytics, predictive maintenance, IIoT), operational convenience (remote vendor support, engineers working from home), and simple network drift have created dozens of intended and unintended paths between IT and OT. Even genuinely isolated plants are bridged by removable media and by laptops that move between networks.

The practical takeaway is not "restore the air gap" — that ship has sailed — but "**assume connectivity exists, find every path, and monitor it.**" The IT/OT boundary is the single most important place to watch, precisely because the myth of its impermeability persists.

## 1.5 The mindset shift, stated as rules

Everything above condenses into a small set of operating rules that govern every technique in this guide:

- **Safety first.** No security action is worth a safety event. When a choice risks the process, choose the option that doesn't.
- **Passive before active.** Default to passive capture, log collection, and configuration review. Active queries or scans of control devices require a written window, engineer supervision, and a clear reason — never as a first move.
- **Operations in the loop.** Investigations and especially containment happen *with* the control engineers who own the process and understand the consequences. Operations holds stop authority at all times.
- **Consequence-based prioritization.** Rank everything — vulnerabilities, alerts, hunts — by what it could do to the physical process, not by CVSS or by volume.
- **Baseline is king.** Because OT is stable and knowable, a clean baseline of assets, conversations, and commands is your most powerful tool.

## 1.6 Two lenses: the engineer and the hunter

This guide is written from two perspectives that you should learn to hold at once:

- **The OT engineer** keeps the plant running safely. They know the process, the normal, the consequences, and the constraints. Their instinct is *protect the process*.
- **The OT threat hunter** keeps the plant safe from adversaries. They know the attacker, the telemetry, and the detections. Their instinct is *find the intrusion*.

The best OT defenders think like both. Every hunting or security action must pass the engineer's test — *does this risk the process?* — and every engineering decision benefits from the hunter's question — *how would I see this being abused?* When the two lenses agree, you have a safe and effective control. When they conflict, safety wins.

## 1.7 A concrete picture

Imagine a simple dosing process at a water treatment plant. A **sensor** measures chlorine concentration. A **PLC** compares it to a setpoint and drives a **dosing pump** to hold the concentration in a safe band. An **HMI** shows the operator the current value and lets them adjust the setpoint. A **historian** records every value over time. A **safety system**, independent of the PLC, will shut the process down if concentration ever approaches a dangerous level.

Now consider the attacker's opportunities and the defender's answers:

- An attacker who reaches the HMI or PLC could raise the chlorine setpoint to a harmful level. *The defender watches for setpoint writes outside the approved range, from unexpected sources, or outside operating hours (a process indicator).*
- They might spoof the sensor value the operator sees so the manipulation looks normal. *The defender compares the historian's recorded values against the live process and looks for a divergence between commanded and actual (the command-versus-feedback check).*
- They might try to defeat the independent safety system so it won't trip. *The defender treats any activity touching the safety system as a top-severity event.*

This tiny example already contains the whole discipline: physical consequence, insecure protocols, the value of the historian, the primacy of safety, and the power of knowing what "normal" looks like. Every later chapter deepens one part of this picture.

## Chapter summary

- OT inverts IT's priorities: **safety → availability → integrity → confidentiality**.
- OT risk is **consequence-driven** — measured in physical, safety, and environmental terms.
- Ten structural differences (determinism, long lifetimes, rare patching, insecure protocols, vendor access, few agents, physical consequence, slow documented change, small knowable populations, different people) shape every decision.
- The air gap is a myth; assume connectivity and monitor the IT/OT boundary.
- The operating rules are **safety-first, passive-before-active, operations-in-the-loop, consequence-based, baseline-driven.**
- Hold two lenses at once — the engineer who protects the process and the hunter who finds the adversary.

## Cross-references
- Chapter 05 (Purdue model) formalizes "where to watch."
- Chapter 16 (hunting methodology) turns the rules into a repeatable practice.
- Chapter 25 (incident response) is where safety-first and authority-to-act become procedure.
- Companion repository: `sis-safety-detection` shows the safety-first doctrine as working detections.
