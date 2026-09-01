# C01 — Frozen Value / Replay

## Problem
A live analog sensor is never perfectly still — real process signals always carry noise. A value that goes **perfectly flat** is therefore suspicious in two ways: it can be a **stuck/failed sensor** (a reliability issue the SOC should surface), or it can be a **replayed/held value** — an attacker feeding the historian a constant or recorded signal to mask a manipulation underneath (the reporting half of a Stuxnet-style deception).

This detection is the cheap, high-yield companion to E01: E01 needs a second source, C01 needs only the one you already have.

## Detection concept
Two complementary signatures against the same tag:
1. **Frozen value** — the value holds *exactly* constant for longer than the tag's `max_stall_sec` (the longest it legitimately holds still, from the clean window). Discrete/status tags legitimately hold for a long time; analog PVs should not.
2. **Variance collapse** — over a rolling window, the signal's variance drops below `min_variance` (the tag's normal noise floor). This catches a "held" value that has tiny synthetic jitter added to dodge an exact-match freeze test.

Either signature fires. Variance collapse is the harder-to-evade of the two.

## Data required
- Historian value events (`tag`, `value`, `quality`) per [`docs/historian-data-model.md`](../../../../docs/historian-data-model.md)
- Baseline lookup for `max_stall_sec` and `min_variance`

## Logic
- Splunk: [`splunk.spl`](splunk.spl) (frozen-value primary + variance-collapse companion)
- Sentinel: [`sentinel.kql`](sentinel.kql)

## Tuning
- **`max_stall_sec`** must be per-tag. A tank level in a slow process legitimately holds far longer than a flow. Discrete status tags should either be excluded or given a very large `max_stall_sec`.
- **`min_variance`** is the noise floor from the clean window's 1st-percentile rolling variance. Set the rolling window wide enough to contain real noise, narrow enough to react.
- Exclude tags that are *supposed* to be constant (manual constants, disabled loops).
- A frozen value coinciding with normal-looking downstream behaviour is more suspicious than one during a known idle period — correlate with `mode`.

## Response
1. First determine **sensor fault vs replay.** A stuck transmitter is a maintenance ticket; a replayed value is an incident.
2. Corroborate with an independent reading (E01) — does the direct read agree the value is truly flat, or is only the historian path flat?
3. Check whether the frozen value is masking movement in coupled tags (D03) or an approach to a limit (G01) underneath.
4. If replay is suspected, escalate as spoofed-reporting / manipulation-of-view.

## MITRE ATT&CK for ICS
- **T0856** — Spoof Reporting Message
- **T0815** — Denial of View

## Validation
See [`validation.md`](validation.md).
