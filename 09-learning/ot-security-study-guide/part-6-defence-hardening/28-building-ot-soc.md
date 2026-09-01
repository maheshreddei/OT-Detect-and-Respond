# Chapter 28 — Building and Running an OT SOC

> Part VI. Everything in this guide comes together in an operating capability: a Security Operations Center that can actually monitor, hunt, and respond in OT. This chapter is how you stand one up and run it.

## 28.1 Start with visibility and ownership, not tools

The most common failure is buying a platform before establishing two prerequisites: **visibility** (an asset inventory and passive network monitoring — you cannot defend what you cannot see) and **ownership** (a named owner who can act, with operations in the loop). Fix those first; the tooling is the easy part once you know what you have and who decides.

## 28.2 The maturity path (Crawl → Walk → Run)

An OT SOC is built in stages, sequenced by value per effort:

- **Crawl — visibility and quick wins.** Asset inventory, passive monitoring at the IT/OT boundary, Tier-1 log sources, and the two highest-value detections: **IT→OT boundary crossing** and **remote-access abuse** (the two most common real attack paths).
- **Walk — detection and response.** SIEM integration, detection engineering across protocol/physics/host, IR playbooks and investigation SOPs, defined triage and escalation.
- **Run — optimize and assure.** Safety-system monitoring, threat hunting, purple team / detection assurance, KPIs, and continuous improvement.

Trying to do everything at once fails; staging delivers value early and de-risks the rest.

## 28.3 The co-managed model

Few asset owners can staff a 24/7 OT SOC with scarce OT-skilled analysts, so the common and effective model is **co-managed**: the asset owner keeps **operations context and authority to act on OT assets** (safety-first), while a provider brings **detection engineering, tooling, and 24/7 monitoring**. Define the split explicitly — who triages, who contains, who decides — so the response authority (Chapter 25) is unambiguous.

## 28.4 People

OT SOC needs skills an IT SOC lacks: OT protocols, the Purdue model, safety awareness, and the safety-first doctrine. Build the team through **train (upskill IT-SOC analysts with adjacent strengths) + hire (an experienced OT anchor) + partner (integrators/vendors for gaps)**. Just as important as skills is **culture**: bake in safety-first, passive-before-active, and operations-in-the-loop from day one — this is what earns the trust of plant engineers and separates a credible OT SOC from an IT SOC pointed at OT.

## 28.5 Run discipline

Operating well is a discipline, not a state:

- **Triage and OT-safe containment** per playbooks, with the authority matrix.
- **Detection lifecycle** — validate (TDA), tune false positives, re-baseline, add and retire detections.
- **KPIs/SLAs** — false-positive rate, MTTD, coverage, and the assurance metrics — tracked and trended.
- **Threat hunting** and periodic **purple team** to find what the automation misses and prove it's fixed.
- **Reporting** to stakeholders that shows the posture improving over time.

## 28.6 The mindset, one more time

An OT SOC is an IT SOC with **different physics, different authority, and passive-first doctrine**. Reuse the platform and the operational muscle of an IT SOC where you can, but change the mindset, the response model, and the detection content to fit a world where the assets are physical, safety is paramount, and operations owns the process.

## Chapter summary
- Start with **visibility and ownership**, not tools.
- Build in stages (**Crawl → Walk → Run**), value-per-effort, quick wins first.
- **Co-managed** is the common model — asset owner keeps operations/authority, provider brings detection/tooling/24-7; define the split.
- Build the team via **train/hire/partner** and bake in **safety-first culture.**
- Run with discipline — triage, detection lifecycle, KPIs, hunting/purple team, reporting.
- An OT SOC = an IT SOC with **different physics, authority, and passive-first doctrine.**

## Cross-references
- Chapters 08–09 (visibility), 16 (hunting), 20 (detection engineering), 25 (IR), 27 (hardening).
- Companion: `ot-soc-delivery-playbook` (strategy → proposal → delivery → run), `ot-monitoring-deployment`, `threat-detection-assurance`.
