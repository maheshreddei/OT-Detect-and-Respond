# Telemetry Strategy

Three ranked views of OT telemetry sit in `01-telemetry/`. They are not redundant and they
are not versions of each other — they answer three different questions that get asked by
three different people. This document explains when to reach for which, and what to do
when they conflict.

## The three views

### 1. Telemetry hierarchy (`TEL-01..14`) — ranked by hunt value

*Asked by: the detection engineer / threat hunter.* "If I could have one more data source,
which would find the most?"

Ranked on hunt value against collection effort. The top of this list is where detection
capability actually comes from:

| Rank | Source | Effort | Hunt value |
|------|--------|--------|------------|
| 1 | Network metadata (Zeek/sensor) | Medium | Very high |
| 2 | Windows Security + Sysmon on HMI/EWS/historian | Medium | Very high |
| 3 | Firewall / boundary logs | Low | High |
| 4 | Remote-access and VPN authentication | Low | High |
| 7 | Controller checksums and mode state | Medium | Very high |

Note that **rank 7 carries a "very high" hunt value** — controller checksum and mode state
is described as the highest-fidelity signal in OT. It ranks 7th rather than 1st because
fidelity is not the same as reach: it is a narrow, precise signal, where network metadata
is a broad one. Both belong near the top of a mature program.

### 2. Collection plan (`CP-01..14`) — ranked by deployment priority

*Asked by: the engineer building the pipeline.* "What do I deploy first, and how do I
actually get the data?"

Priority 1 is four things: IDMZ firewall both directions, jump host / remote-access broker,
EWS Windows Security + Sysmon, and a passive network sensor. Together those cover the
boundary, the human path in, the place adversaries operate, and the protocol layer no host
can report on. Each row carries its collection mechanism (syslog, WEF/agent, SPAN/TAP,
poll-and-forward, DB export) because "collect the historian" and "collect the firewall" are
completely different engineering jobs.

### 3. Minimum viable telemetry (`MVT-1..7`) — ranked by budget sequence

*Asked by: the customer or the CFO.* "We have nothing and limited money. Where do we
start?"

Seven steps, each **independently useful** — that property is the point. This is not a
phased project that only pays off at the end; step 1 alone (boundary firewall allow+deny
into the SIEM) delivers real detection value before step 2 is funded. That makes it a
credible proposal rather than a wish list.

## Where the views disagree — and why that matters

The most important disagreement in the whole repository:

> **Network monitoring is the #1 hunt-value source (TEL-01) and a priority-1 collection
> item (CP-04), but it is Tier 3 for onboarding (LS-18).**

Nothing is wrong. Hunt value says *build this*; onboarding tier says *it will take the
longest*, because SPAN/TAP design, sensor placement per Purdue zone, and DPI tuning are a
project with capex, not a syslog destination change.

Holding both facts at once is what separates a realistic program plan from a wish list. The
practical consequence is the sequencing in `MVT`: get the cheap boundary and identity
telemetry flowing (steps 1–3) *while* the sensor architecture is being designed and
procured (step 4), then expand sensors per Level 2 area (step 6) once the pattern is
proven. You are never idle waiting on the expensive thing, and you are never pretending the
expensive thing is optional.

## What this buys you — measured

From `05-crosswalk/coverage-rollup.csv`, the sources that unlock the most detection:

| Log source | Onboarding tier | Use cases unlocked | Distinct ATT&CK techniques |
|------------|-----------------|--------------------|----------------------------|
| Network Traffic (SPAN/TAP/IDS) | Tier 3 | 11 | 10 |
| PLC (via passive monitoring) | Tier 2 | 6 | 6 |
| Firewall (OT) | Tier 1 | 4 | 4 |
| Control Server / SCADA | Tier 1 | 3 | 2 |

And the headline sequencing fact: **11 of 28 use cases are reachable with Tier 1 telemetry
alone.** That is the number to put in front of a customer who wants to know what the first
phase actually delivers — roughly 40% of the detection catalog from the cheap, fast
sources, before any sensor is racked.

## Using this with a customer

- Lead with **MVT** — it is the only view that survives a budget conversation.
- Justify with **TEL** — it explains *why* the sequence is what it is.
- Deliver with **CP** and the `LS` onboarding tiers — they are what the engineers work
  from.
- Prove value with **coverage-rollup** — it converts "we onboarded the firewall" into "we
  unlocked four use cases across four ATT&CK techniques."

That last translation is the one most programs cannot make, and it is the reason the
crosswalk exists.
