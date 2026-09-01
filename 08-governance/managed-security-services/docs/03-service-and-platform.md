# 03 — Service Definition & Platform

Define *what you're selling* before *how you'll build it*.

## Service tiers (adapt)
| Tier | Scope | Buyer |
|------|-------|-------|
| **Essential** | Asset visibility + IT/OT boundary & remote-access detection + IR readiness | Early-maturity clients; regulatory starter |
| **Advanced** | + full protocol detection, Sigma content, historian/physics detection, 24/7 monitoring | Clients wanting real detection depth |
| **Safety-critical** | + SIS/safety-system monitoring + IT perimeter + threat hunting | High-consequence sites (O&G, power) |

Map each tier to concrete detection content and deliverables (reuse prebuilt libraries to accelerate).

## Delivery model — co-managed (recommended)
The asset owner keeps operations/engineering context and **authority to act on OT assets** (safety-first); the provider brings detection engineering, tooling, and 24/7 monitoring. Cleanest fit for OT because response must stay with those who own the process. Define the split explicitly (who triages, who contains, who decides).

## SLAs (define per tier)
Monitoring hours (8x5 / 24x7), alert triage time by severity, incident response time, escalation, reporting cadence. Keep OT-realistic (response involves operations; don't over-commit on containment you don't control).

## Platform / NDR selection
Decision criteria for Nozomi / Dragos / Claroty (score each):
- **Protocol & detection coverage** for your target sectors.
- **Multi-tenancy / MSSP fit** — central management across clients (e.g. CMC/Vantage-style), tenant isolation.
- **Integration** with your existing SIEM/SOAR (native connectors, data model, alert forwarding).
- **Licensing model** — per-sensor/per-site/per-asset; how it maps to your pricing.
- **Partner program** — MSSP/MDR tier, enablement, deal registration, margins, support.
- **Deployment footprint** — passive sensors, sizing, remote management.

Output: a scored shortlist and a recommended primary platform (+ possibly a second for coverage).

## SIEM integration
Forward NDR alerts + underlying detail into your existing SIEM for correlation, enrichment, cross-client analytics, and unified reporting — so OT extends your single pane, not a parallel stack. Reuse your SOAR for OT playbooks (with OT-safe guardrails).

## Partnerships
- **NDR vendor** — MSSP partnership, enablement, joint go-to-market.
- **System integrators / OT engineering firms** — for on-site deployment where you lack local hands.
- **Training providers** (SANS/GIAC, vendor academies) — for the skills ramp.
