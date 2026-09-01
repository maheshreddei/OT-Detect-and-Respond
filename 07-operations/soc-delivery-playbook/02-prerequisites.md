# 02 — Prerequisites

What must be in place before an OT SOC deployment succeeds. Missing prerequisites are the top reason deployments produce noise instead of detections — or stall.

## Organizational
- **Executive sponsorship** — a named owner with budget and authority (CISO + plant/operations leadership jointly).
- **Stakeholder alignment** — IT security, OT/engineering, operations, and **plant safety** all bought in. OT SOC is a joint discipline; without engineering and operations, you can't safely act on detections.
- **Defined ownership** — who owns OT security operations, and who has **authority to act** on OT assets (see the IR RACI — operations decides for the process).

## Governance
- **Scope defined** — sites, zones, asset classes, and what's in/out.
- **Policy & RACI** — roles, escalation, and the authority-to-act matrix agreed before go-live.
- **Safety doctrine accepted** — monitoring is **passive / read-only**; nothing touches the process without operations sign-off; MOC applies to any change.

## Technical
- **Network readiness** — segmentation defined (Purdue/zones), and **SPAN/TAP or mirror capability** for passive monitoring. If the network is flat, plan segmentation as part of the program.
- **Asset inventory baseline** — even a rough one; the SOC will refine it, but you need a starting picture.
- **The pre-deployment document package** — architecture, Purdue diagram, communication matrix, firewall rules, P&ID, PLC I/O, historian tags, risk assessment (see `ot-monitoring-deployment/pre-deployment`). Missing docs become early deployment tasks.
- **SIEM / monitoring platform** decision (Nozomi/Dragos/Claroty for NDR; Sentinel/Splunk for SIEM) or agreement to select one during design.

## People & skills
- **OT-capable analysts** — IT SOC skills alone aren't enough; OT context (protocols, Purdue, safety) is required. Co-managed MSS is the common way to bridge this gap.
- **Engineering partnership** — named controls/operations engineers who join investigations and authorize OT-side actions.

## Prerequisite checklist
- [ ] Executive sponsor + budget confirmed
- [ ] IT / OT / operations / safety stakeholders aligned
- [ ] Scope (sites/zones/assets) agreed, in/out documented
- [ ] Authority-to-act / RACI agreed; safety veto acknowledged
- [ ] Passive-only monitoring doctrine accepted; MOC process available
- [ ] Network segmentation & SPAN/TAP capability assessed
- [ ] Asset inventory baseline available (or discovery scoped)
- [ ] Pre-deployment document package requested (`ot-monitoring-deployment`)
- [ ] NDR + SIEM platform selected or selection scoped
- [ ] OT-capable analyst coverage (internal or MSS) in place
- [ ] Engineering points-of-contact named for investigations

## Readiness gate
Proceed to delivery when sponsorship, scope, safety doctrine, and network/asset readiness are confirmed and the priority documents are at least partially in hand. Gaps are acceptable **if** each has an owner and a plan — often the first delivery phase produces the missing artifacts.
