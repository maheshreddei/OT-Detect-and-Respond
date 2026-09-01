# 06 — Portfolio Map (How the Content Fits Together)

The relationship between everything in this portfolio. Each library is a **deliverable in a phase** of an OT SOC program — this is the map from content to real delivery.

## Content → lifecycle phase → buyer

| Library | Phase | Primary user | What it delivers |
|---------|-------|--------------|------------------|
| `ot-monitoring-deployment` | Assess, Design, Deploy | Architect, SOC | Pre-deployment document package + tiered log-source onboarding |
| `ics-procurement-language` | Assess (requirements) | Architect, procurement | Contract/RFP security requirements for OT systems |
| `ot-protocol-defense` (+ Nozomi queries) | Detect | Detection engineer, SOC | 13-protocol defender guide, 54 detections, N2QL assertions |
| `ot-historian-detection` | Detect | Detection engineer | Physics-layer baseline & deviation detection |
| `ot-detection-engineering` (87 Sigma) | Detect | Detection engineer, SOC | Protocol / cross-zone / threat-actor Sigma libraries |
| `sis-safety-detection` | Detect (safety) | Detection engineer, safety | SIS/safety-system monitoring (TRITON-class) |
| `perimeter-to-endpoint-detections` | Detect (IT side) | SOC | Enterprise perimeter→endpoint detections (the pre-OT path) |
| `it-ot-incident-response` | Respond | IR lead, SOC | IR plan, investigation SOPs, evidence, playbooks |
| `ot-soc-delivery-playbook` (this) | All / program | OT security lead | Strategy, business case, proposal, delivery method |

## The picture

```
                         ┌──────────────────────────────────────────────┐
                         │        ot-soc-delivery-playbook (this)        │
                         │   strategy · business case · proposal · method │
                         └───────────────┬──────────────────────────────┘
                                         │ orchestrates
   ASSESS/DESIGN/DEPLOY        DETECT                         RESPOND
   ┌───────────────────┐   ┌──────────────────────────────┐  ┌────────────────────┐
   │ ot-monitoring-    │   │ ot-protocol-defense          │  │ it-ot-incident-    │
   │ deployment        │   │ ot-historian-detection       │  │ response           │
   │ ics-procurement-  │   │ ot-detection-engineering     │  │                    │
   │ language          │   │ sis-safety-detection         │  │                    │
   │                   │   │ perimeter-to-endpoint-det.    │  │                    │
   └───────────────────┘   └──────────────────────────────┘  └────────────────────┘
```

## How they compose into a service offering (tiered MSS)

| Tier | Includes | Content |
|------|----------|---------|
| **Essential** | Visibility + boundary/remote-access detection + IR readiness | `ot-monitoring-deployment`, subset of `ot-protocol-defense`, `it-ot-incident-response` |
| **Advanced** | + full protocol & Sigma detection + physics layer | + `ot-detection-engineering`, `ot-historian-detection`, full `ot-protocol-defense` |
| **Safety-critical** | + SIS monitoring + IT perimeter + hunting | + `sis-safety-detection`, `perimeter-to-endpoint-detections` |

## Why the relationship matters
Each library is reusable IP that **cuts delivery effort and deepens coverage** in its phase — the reason a proposal can promise faster time-to-value and greater depth than a from-scratch build. The playbook (this repo) is what turns that IP into a repeatable, priceable, deliverable program.
