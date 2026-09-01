# 05 — Proposal Template (What to Include)

A reusable structure for an OT SOC / OT monitoring proposal. Fill per opportunity; not every section applies to every deal, but this is the full set.

## 1. Executive summary
The buyer's driver, what you propose, the outcome, and the headline commercial — in half a page a sponsor can read.

## 2. Understanding of requirements
Demonstrate you understand *their* environment and driver (safety / compliance / post-incident / insurer). Restate their goals and constraints — this is where you win trust.

## 3. Scope
- **In scope:** sites, zones, sensor coverage, log-source tiers, use-case families, MSS hours & response.
- **Out of scope:** explicitly (prevents scope creep).
- **Assumptions & dependencies:** customer-provided documents (the pre-deployment package), network readiness/segmentation, change windows, engineering availability, platform licences.

## 4. Proposed solution & architecture
- High-level architecture (HLD summary): NDR sensor placement, SIEM integration, data flows, respecting Purdue zones and passive/read-only collection.
- Platform approach (Nozomi/Dragos/Claroty + Sentinel/Splunk) — anchored or agnostic.

## 5. Methodology / approach
The delivery lifecycle (`03-delivery-lifecycle.md`): Assess → Design → Deploy → Detect → Respond → Run. Emphasize **safety-first, passive-only, operations-in-the-loop**, and staged time-to-value (Crawl→Walk→Run).

## 6. Detection coverage / use cases
The differentiator. Summarize the detection families you'll deploy and their ATT&CK-for-ICS mapping:
- IT↔OT boundary & remote-access abuse
- OT protocol write/command detection (Modbus, S7, DNP3, IEC-104, OPC UA, ENIP, BACnet, IEC 61850)
- Process/physics baseline & deviation (historian)
- Safety-system (SIS) monitoring
- IT perimeter-to-endpoint detections
Reference the prebuilt libraries as evidence of depth and speed.

## 7. Deliverables
List concrete artifacts per phase (assessment report, HLD/LLD, log-source matrix, detection rules + validation, ATT&CK coverage map, IR plan + playbooks, RACI, KPI/SLA framework, runbooks, reporting).

## 8. Project plan & timeline
Phased plan with milestones and time-to-first-value. Show early quick wins (zone-crossing, remote access) landing before full detection engineering completes.

## 9. Team & roles
Named roles (OT security lead, architect, detection engineer, deployment engineer, SOC/MSS analysts) and the customer roles required (sponsor, engineering PoCs, operations, safety). Include the authority-to-act model.

## 10. Service levels & KPIs (for MSS)
Monitoring hours, alert triage SLA, incident response SLA, reporting cadence, and KPIs (FP rate, MTTD, MTTT, coverage, baseline freshness). See `templates/kpi-sla.md`.

## 11. Commercials
Pricing model (`04-proposal-guide.md`): one-time project + recurring MSS, per-sensor/site, or T&M-capped for assessment. Break out capex vs opex. Show phased funding option (fund Crawl first).

## 12. Why us / differentiators
Prebuilt ATT&CK-mapped libraries · physics-layer & safety-system detection · safety-aware passive methodology · end-to-end assess-to-run · OT-specific (not repurposed IT).

## 13. Appendices
Sample deliverables (a redacted detection catalog, a sample IR playbook, a sample KPI report), reference architecture, standards alignment (IEC 62443, NIST 800-82r3, NIST CSF 2.0), and the assumptions/document-request list.

---

### Quick checklist
Exec summary · Requirements understanding · Scope (in/out/assumptions) · Architecture · Methodology · Use-case coverage · Deliverables · Timeline · Team · SLAs/KPIs · Commercials · Differentiators · Appendices.
