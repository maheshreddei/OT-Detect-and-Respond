# 00 — Where to Start an OT SOC

The most common mistake is starting with a tool purchase. You start with **visibility and governance**, not a SIEM licence. Here's the honest starting point and a phased path.

## First principle: you can't defend what you can't see, and you can't act without ownership
Two things gate everything else: an **asset inventory + network visibility** (so you know what's there and what's talking), and **defined ownership + sponsorship** (so someone can act on what you find). If either is missing, fix it before buying tools.

## OT SOC maturity model

| Level | State | Hallmarks |
|-------|-------|-----------|
| 0 — Blind | No OT visibility | IT SOC only; OT is a black box |
| 1 — Visible | Passive network + asset inventory | Nozomi/Dragos/Claroty deployed; you can *see* OT |
| 2 — Monitored | Logs to SIEM, boundary + remote-access detection | IT↔OT crossing and remote-access abuse detections live |
| 3 — Detecting | Protocol, physics & safety detection engineering | Sigma/historian/SIS detections; tuned; IR playbooks |
| 4 — Optimized | Threat hunting, metrics, continuous improvement | Hypotheses, purple team, KPI-driven, safety monitoring |

Most programs are trying to move from 0/1 to 2/3. Know your current level before scoping.

## Phased roadmap (Crawl → Walk → Run)

### Crawl (visibility & quick wins) — weeks 0–8
- Build/validate the **asset inventory** and **passive network visibility** (NDR).
- Onboard the **Tier-1 log sources** — firewall (OT), jump host, VPN, control server, workstations, switch (see `ot-monitoring-deployment`).
- Ship the two highest-value detection families first: **IT→OT zone crossing** and **remote-access abuse** — the two most common real compromise paths.
- Establish who gets paged and how.

### Walk (detection & response) — weeks 8–20
- Integrate to the **SIEM**; onboard Tier-2 (PLC via passive, historian, HMI, safety controller).
- Stand up **detection engineering**: protocol (`ot-protocol-defense`), physics (`ot-historian-detection`), Sigma libraries (`ot-detection-engineering`).
- Wire **IR playbooks & investigation SOPs** (`it-ot-incident-response`).
- Define SOC processes: triage, escalation, OT-safe containment, shift model.

### Run (optimize & assure) — ongoing
- Add **safety monitoring** (`sis-safety-detection`) and **IT-side perimeter detections** (`perimeter-to-endpoint-detections`).
- Onboard Tier-3 (network SPAN/TAP DPI, DCS, PAC, RTU).
- **Threat hunting**, detection lifecycle, KPIs/SLAs, periodic purple-team and re-baselining.

## First 90 days (concrete)
1. **Weeks 1–2:** sponsorship confirmed, scope agreed, pre-deployment documents requested (`ot-monitoring-deployment`).
2. **Weeks 3–6:** passive NDR deployed, asset inventory built, Tier-1 logs onboarding.
3. **Weeks 7–10:** first detections live (zone-crossing, remote access), triage process running.
4. **Weeks 11–13:** SIEM correlation, first IR playbook tabletop, initial KPI baseline.

## Build vs. buy vs. co-managed (MSS)
- **Build (internal SOC):** max control, needs scarce OT-capable analysts and 24/7 staffing.
- **Buy (full MSS):** fast, provider owns detection/run; ensure OT-specific capability, not repurposed IT SOC.
- **Co-managed (most common):** asset owner keeps operations/engineering context and OT-safe response authority; provider brings detection engineering, tooling, and 24/7 monitoring. Best fit for most plants.

## What "started" looks like
You've started an OT SOC when: you can see every asset and its comms, Tier-1 logs reach a SIEM, at least the zone-crossing and remote-access detections fire, and there's a named owner who can act — with operations in the loop. Everything after that is depth.
