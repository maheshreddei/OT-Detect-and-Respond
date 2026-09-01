# 02 — Discovery Framework

Before proposing, map the gap between what your MSS can do today and what an OT service requires — across four lenses. Don't start with tools; start with an honest current-state. Score each lens using [`../templates/capability-assessment.md`](../templates/capability-assessment.md).

## Lens 1 — Internal capability (what you already have)
Inventory the reusable foundation before assessing gaps:
- **Platform:** existing SIEM (Sentinel/Splunk), SOAR, ticketing, case management, threat intel — most is reusable for OT.
- **Operations:** shift model, escalation, on-call, reporting cadence, MDR runbooks.
- **Existing OT-relevant visibility:** are you already ingesting IT/OT boundary firewalls, jump hosts, VPN, AD? You likely have more OT-adjacent coverage than you think.
- **Delivery muscle:** onboarding process, multi-tenancy, client reporting.

Output: a list of what transfers as-is, what needs OT extension, and what's missing.

## Lens 2 — Skills (the people gap)
OT SOC needs skills an IT SOC lacks: OT protocols (Modbus/DNP3/S7/OPC UA/IEC-104), the Purdue model, ICS threat landscape, safety-system awareness, and the **doctrine** differences (safety-first, passive-before-active, operations-in-the-loop). Map current team skills against these; for each gap decide **train / hire / partner** (detail in `04`).

Output: skills matrix with gaps and a sourcing decision per gap.

## Lens 3 — Tooling (the platform gap)
The defining technical/commercial decision: which **OT NDR** you standardize on (Nozomi / Dragos / Claroty). Assess on protocol coverage, detection depth, **multi-tenancy for MSS**, SIEM/SOAR integration, licensing model, and **partner/MSSP program** (tiering, enablement, margins). Then define how it feeds your existing SIEM so you extend one platform rather than run two. (Detail in `03`.)

Output: platform shortlist + integration approach + partnership path.

## Lens 4 — Service / commercial (the offering gap)
Unlike an internal build, an MSS capability must be a **productized, repeatable, priceable service**. Define: service tiers, delivery model (co-managed), SLAs, pricing model, and the target market/sectors. (Detail in `03`, `06`.)

Output: a one-page service concept and target-market definition.

## Running the discovery
1. Score the four lenses (capability-assessment template) → current-state maturity.
2. Define the **target state** (the service you want to offer) → `03`.
3. **Gap = target − current**, per lens → feeds the implementation plan (`05`).
4. Validate demand: talk to 2–3 sales leads / existing clients with OT exposure to confirm the market signal before you build.

## Current-state → target-state summary (fill in)
| Lens | Current state | Target state | Gap | Close by (train/hire/partner/build/buy) |
|------|---------------|--------------|-----|------------------------------------------|
| Capability | | | | |
| Skills | | | | |
| Tooling | | | | |
| Service/commercial | | | | |
