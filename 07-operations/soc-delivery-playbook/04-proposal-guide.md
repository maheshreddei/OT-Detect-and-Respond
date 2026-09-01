# 04 — How to Create a Proposal

Turning an opportunity into a proposal that wins and is deliverable. The proposal is where discovery, scope, method, and commercials come together — get scoping right and the rest follows.

## Step 1 — Qualify & discover (before you write anything)
Understand the buyer's real driver (safety? compliance deadline? insurer? post-incident?), their maturity level (00 model), and their constraints. Use the discovery questionnaire (`templates/discovery-questionnaire.md`). Key things to establish:
- **Why now** — the trigger; it shapes the win theme.
- **Scope reality** — number of sites, zones, approximate asset counts, network segmentation state, existing tooling.
- **Maturity** — are they at Level 0 (blind) or Level 2 (need detection depth)?
- **Delivery model** — internal build, full MSS, or co-managed.
- **Prerequisites** — what documents/readiness exist (`02-prerequisites.md`).

## Step 2 — Scope
Scope is the single biggest driver of price and risk. Define:
- **Sites & zones** in scope (and explicitly out).
- **Sensor count** — driven by network architecture (segments/spans to cover), not asset count alone.
- **Log sources** — which tiers (`ot-monitoring-deployment`).
- **Use-case coverage** — how many/which detection families (protocol, physics, safety, IT).
- **MSS scope** — monitoring hours (8x5 vs 24x7), response scope, reporting cadence.
- **Assumptions & dependencies** — customer-provided docs, network readiness, change windows, engineering availability.

## Step 3 — Estimate effort
- **Deploy** scales with sensor count and site count (travel, change windows).
- **Detect** scales with use-case count and tuning depth — this is where your prebuilt libraries cut effort dramatically (reuse vs. build-from-scratch).
- **Run** is recurring — sized by monitoring hours, alert volume, and detection-lifecycle cadence.

## Step 4 — Choose a pricing model
| Model | Fits | Notes |
|-------|------|-------|
| **Fixed-price project + recurring MSS** | Most engagements | Project (assess→deploy→detect→respond) as fixed price; run as monthly/annual MSS. Clean for the buyer. |
| **Per-sensor / per-site** | Multi-site, standardized | Predictable unit economics; good for scaling. |
| **Per-asset / per-monitored-node** | Some MSS models | Aligns to environment size; watch definition of "asset." |
| **T&M / capped** | Ambiguous scope, discovery-heavy | Use for assessment phase, then fixed-price the rest. |

Common structure: **fixed-price for Assess+Design+Deploy+Detect+Respond**, then **recurring MSS** for Run.

## Step 5 — Win themes / differentiation
Lead with what makes the delivery lower-risk and faster:
- **Prebuilt, ATT&CK-mapped detection libraries** (protocol, historian/physics, Sigma, safety, IT) → faster time-to-value, deeper coverage than a from-scratch build.
- **Safety-aware, passive-only methodology** → operations trust you won't disrupt the process.
- **Physics-layer detection** (historian baseline/deviation) → catches manipulation the network layer misses; few competitors offer it.
- **Safety-system monitoring** (SIS) → the TRITON-class coverage most SOCs lack.
- **End-to-end** — assessment through 24/7 run, with IR playbooks and evidence-grade investigation.

## Step 6 — Review for deliverability
Before submitting: is the scope actually deliverable with the priced effort? Are prerequisites and assumptions explicit (so scope creep is controlled)? Is the safety/passive doctrine stated? Is there a clear time-to-first-value?

## Common pitfalls
- **Under-scoping the network/SPAN work** (Tier-3 network traffic is the highest engineering effort — price it honestly).
- **Over-promising day-one coverage** — stage it (Crawl→Walk→Run); commit to early quick wins, not everything at once.
- **Ignoring prerequisites** — missing docs/segmentation blow timelines; make them assumptions/dependencies.
- **Treating OT like IT** — repurposed IT SOC content erodes credibility with engineers.
