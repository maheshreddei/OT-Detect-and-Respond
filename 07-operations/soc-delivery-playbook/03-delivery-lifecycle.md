# 03 — Delivery Lifecycle

The end-to-end method for delivering an OT SOC — what actually happens in a real project, phase by phase, with deliverables, who does what, and which companion library you pull in. Six phases: **Assess → Design → Deploy → Detect → Respond → Run.**

```
  ASSESS ──▶ DESIGN ──▶ DEPLOY ──▶ DETECT ──▶ RESPOND ──▶ RUN
  discover   architect   sensors    engineer   playbooks   operate,
  & scope    & plan      & logs     detections & readiness  improve
     └──────────────── passive · safety-first · operations in the loop ────────────────┘
```

---

## Phase 1 — Assess & Discover
**Goal:** understand the environment, risk, and gaps well enough to design safely.

Activities:
- Kickoff, scope confirmation, stakeholder map, safety doctrine agreed.
- **Request & review the pre-deployment document package** (architecture, Purdue, comms matrix, firewall, P&ID, PLC I/O, historian tags, risk assessment) — `ot-monitoring-deployment/pre-deployment`.
- **Passive asset discovery** and network baselining (where an inventory is missing).
- **Risk assessment / gap analysis** against IEC 62443 / NIST 800-82; identify crown jewels, safety-critical systems, and the IT/OT boundary reality.

Deliverables: Current-state assessment · Asset inventory (baseline) · Risk & gap report · Prioritized use-case candidate list.
RACI: **R** consultant/architect · **A** OT security lead · **C** plant engineering, operations · **I** sponsor.
Companion: `ot-monitoring-deployment`, `ics-procurement-language` (requirements language).

## Phase 2 — Design
**Goal:** the blueprint for a safe, effective deployment.

Activities:
- **HLD** (architecture, sensor/collector placement, data flows, integrations) and **LLD** (IPs, ports, SPAN sessions, sensor specs, rulesets).
- **Log-source onboarding plan** by tier (`ot-monitoring-deployment/log-onboarding`).
- **Use-case / detection catalog** selection — map risks to detections across protocol, physics, safety, and IT layers.
- Sensor placement validated against the network architecture; **passive-only** confirmed.

Deliverables: HLD · LLD · Log-source matrix (site-specific) · Use-case catalog · Deployment plan.
RACI: **R** architect · **A** OT security lead · **C** engineering, network team · **I** sponsor, operations.
Companion: `ot-monitoring-deployment`.

## Phase 3 — Deploy
**Goal:** telemetry flowing, safely, without touching the process.

Activities:
- Install **passive NDR** sensors (SPAN/TAP) — no inline, no active scanning.
- **SIEM integration**; onboard log sources **by tier** (Tier-1 first: firewall, jump host, VPN, control server, workstations, switch).
- Validate data quality, timestamps, parsing; confirm no operational impact with operations.

Deliverables: Deployed sensors · SIEM integration · Onboarded sources (tiered) · Validation report.
RACI: **R** deployment engineer · **A** OT security lead · **C** operations (change windows), network · **I** sponsor.
Companion: `ot-monitoring-deployment`.

## Phase 4 — Detect (Detection Engineering)
**Goal:** turn telemetry into tuned, validated detections mapped to ATT&CK for ICS.

Activities:
- Stand up detections in priority order:
  - **Boundary & remote-access** first (zone crossing, VNC/RDP/FTP into OT) — `ot-protocol-defense`, `perimeter-to-endpoint-detections`.
  - **Protocol write/command** detections — `ot-protocol-defense` (+ Nozomi assertion queries).
  - **Physics / process** baseline & deviation — `ot-historian-detection`.
  - **Sigma libraries** (protocol, cross-zone, threat-actor) — `ot-detection-engineering` (87 rules).
  - **Safety monitoring** — `sis-safety-detection` (any SIS event = SEV-1).
- **Baseline** the deviation detections; **tune** for false positives; **validate** each with test cases before promotion (shadow → active).

Deliverables: Deployed detection rules · Baselines · Tuning & validation records · ATT&CK coverage map.
RACI: **R** detection engineer · **A** OT security lead · **C** process engineering (baselines) · **I** SOC.
Companion: `ot-protocol-defense`, `ot-historian-detection`, `ot-detection-engineering`, `sis-safety-detection`, `perimeter-to-endpoint-detections`.

## Phase 5 — Respond (Readiness)
**Goal:** every detection has a safe, actionable response.

Activities:
- Deploy the **IR plan, investigation SOPs, evidence guides, and per-scenario playbooks** — `it-ot-incident-response`.
- Agree the **authority-to-act matrix** (operations decides for the process; safety veto).
- **Tabletop** the top scenarios (unauthorized logic change, setpoint change, SIS manipulation, ransomware, remote access).
- Define triage, escalation, and OT-safe containment; wire alerts to the right paths (SIS → safety authority).

Deliverables: IR plan · Investigation SOPs · Playbooks · RACI · Tabletop results.
RACI: **R** IR lead · **A** OT security lead · **C** operations, safety, IT sec · **I** sponsor.
Companion: `it-ot-incident-response`.

## Phase 6 — Run & Improve (MSS Operations)
**Goal:** sustained, measurable operations that get better over time.

Activities:
- 24/7 (or agreed) **monitoring & triage**; incident handling per playbooks.
- **Detection lifecycle**: FP/MTTD review, re-baselining, new use cases, retire stale ones.
- **Threat hunting** (hypothesis-driven), periodic **purple team**, and **reporting** to stakeholders.
- **KPIs / SLAs** tracked (see `templates/kpi-sla.md`).

Deliverables: Monitoring & incident reports · KPI/SLA dashboards · Detection lifecycle records · Hunt findings · Continuous-improvement backlog.
RACI: **R** SOC/MSS · **A** OT security lead · **C** engineering, operations · **I** sponsor.
Companion: detection-lifecycle docs across the detection libraries; `templates/`.

---

## Typical timeline (co-managed, single site)
| Phase | Indicative duration |
|-------|---------------------|
| Assess & Discover | 2–4 weeks |
| Design | 2–4 weeks |
| Deploy | 3–6 weeks (change-window dependent) |
| Detect | 4–8 weeks (overlaps Deploy) |
| Respond readiness | 2–3 weeks (overlaps Detect) |
| Run | ongoing |

Time-to-first-value is short: zone-crossing and remote-access detections can be live within the Deploy phase, well before full detection engineering completes. Multi-site programs repeat Assess→Deploy per site with a shared Design and Run.

## Deliverable checklist (whole program)
Assessment report · Asset inventory · Risk & gap analysis · HLD · LLD · Log-source matrix · Use-case catalog · Deployed sensors & SIEM integration · Detection rules + baselines + validation · ATT&CK coverage map · IR plan + SOPs + playbooks · RACI · KPI/SLA framework · Runbooks · Reporting cadence.
