# OT SOC Delivery Playbook

**How to plan, justify, propose, build, and run an OT/ICS Security Operations Centre — end to end, the way it's done in real projects.** This is the program layer that ties together the technical detection & response libraries into a deliverable service.

![Scope](https://img.shields.io/badge/scope-strategy%20%E2%86%92%20proposal%20%E2%86%92%20delivery%20%E2%86%92%20run-blue)
![For](https://img.shields.io/badge/for-OT%20security%20leads%20%7C%20architects%20%7C%20MSS-brightgreen)
![Aligned](https://img.shields.io/badge/aligned-IEC%2062443%20%7C%20NIST%20800--82r3%20%7C%20NIST%20CSF%202.0-lightgrey)
![License](https://img.shields.io/badge/license-MIT-green)

---

## What this is

Every other library in this portfolio answers *"how do I detect/respond to X?"* This one answers the questions that come **before and around** the technical work:

- **Where do I even start** with an OT SOC? → [`00-where-to-start.md`](00-where-to-start.md)
- **How do I justify it** to a board / build the business case? → [`01-business-case.md`](01-business-case.md)
- **What must be in place first** (prerequisites)? → [`02-prerequisites.md`](02-prerequisites.md)
- **What do we actually do in the project**, phase by phase? → [`03-delivery-lifecycle.md`](03-delivery-lifecycle.md)
- **How do I create a proposal**, and price it? → [`04-proposal-guide.md`](04-proposal-guide.md)
- **What goes in the proposal**? → [`05-proposal-template.md`](05-proposal-template.md)
- **How does all the content fit together**? → [`06-portfolio-map.md`](06-portfolio-map.md)

Plus reusable [`templates/`](templates/): discovery questionnaire, program RACI, and MSS KPI/SLA.

## The delivery lifecycle at a glance

```
  STRATEGY            PROPOSAL           DELIVERY (Assess→Design→Deploy→Detect→Respond)        RUN
  ────────            ────────           ────────────────────────────────────────────         ───
  business case   →   scope, price,  →   discover · design · deploy sensors/SIEM ·        →   MSS operations,
  prerequisites,      proposal,          onboard logs · engineer detections ·                 KPIs/SLAs,
  where to start      win themes         wire IR playbooks · validate                          hunt, improve
       │                  │                              │                                        │
   00, 01, 02          04, 05        ────────────  03  ────────────                          03, templates
```

## The portfolio, mapped to the lifecycle

The technical libraries aren't standalone — each is a **deliverable in a specific phase** of an OT SOC project. That relationship is the point of this repo:

| Phase | What you do | Companion library |
|-------|-------------|-------------------|
| **Assess** | Gather docs, discover assets, assess risk | `ot-monitoring-deployment` (pre-deployment package), `ics-procurement-language` (requirements) |
| **Design** | Architecture, HLD/LLD, log-source plan, use-case catalog | `ot-monitoring-deployment` (log onboarding) |
| **Deploy** | Passive sensors, SIEM integration, onboard logs by tier | `ot-monitoring-deployment` |
| **Detect** | Engineer & tune detections across protocol, physics, safety, IT | `ot-protocol-defense` (+ Nozomi queries), `ot-historian-detection`, `ot-detection-engineering` (87 Sigma rules), `sis-safety-detection`, `perimeter-to-endpoint-detections` |
| **Respond** | IR plan, investigation SOPs, evidence, playbooks | `it-ot-incident-response` |
| **Run / Improve** | MSS operations, detection lifecycle, KPIs, hunting | detection-lifecycle docs across the above; templates here |

Full mapping with buyer/user per artifact: [`06-portfolio-map.md`](06-portfolio-map.md).

## How to use this repo

- **Selling / justifying a program** → start at `01-business-case.md`, then `04`/`05` for the proposal.
- **Asked to "review a plant and propose OT monitoring"** → `02-prerequisites.md` + `ot-monitoring-deployment` to scope, then `04`/`05`.
- **Running the delivery** → `03-delivery-lifecycle.md` is the master method; pull the companion library for each phase.
- **Standing up an internal SOC (not MSS)** → the same lifecycle applies; skip the commercial sections of `04`/`05`.

## Assumptions
Written primarily for an **MSS / consulting delivery** context (a provider deploying and running OT monitoring for an asset owner), but the strategy, prerequisites, and lifecycle apply equally to an **internal** build — the proposal/commercial sections are simply internal business-case/roadmap artifacts in that case.

## Author
Prepared for OT/ICS security program delivery — MSS Cyber Defense.

## License
MIT — see [`LICENSE`](LICENSE).

> A methodology, not a substitute for engineering and operations judgement. Every action affecting a live process requires plant sign-off; monitoring stays passive/read-only.
