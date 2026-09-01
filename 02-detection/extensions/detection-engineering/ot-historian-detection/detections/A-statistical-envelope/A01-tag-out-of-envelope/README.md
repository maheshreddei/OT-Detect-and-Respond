# A01 — Tag Out of Operating Envelope

## Problem
A manipulated setpoint, a spoofed actuator command, or a genuine process upset drives a measured value outside the range it occupies during normal operation *for its current mode*. This is the foundational process-deviation detection — most other statistical detections are refinements of it.

## Detection concept
For each analog PV, the baseline defines a normal band per operating mode: engineering limits (`ll`/`hl`) where they exist, otherwise the `p01`–`p99` percentile band from the clean window. Alert when the value falls outside that band **and stays out for N consecutive samples** (dwell), so a single noisy sample doesn't fire.

Percentile bands are preferred over `mean ± 3σ` here because process variables are frequently skewed and bounded; hard engineering limits win over both when present (`coalesce(ll, p01)`).

## Data required
- Historian value events (`tag`, `value`, `quality`, `mode`) per [`../../../docs/data-model.md`](../../../docs/data-model.md)
- Baseline lookup `ot_baseline.csv` keyed on `(tag, mode)`

## Logic
- Splunk: [`splunk.spl`](splunk.spl)
- Sentinel: [`sentinel.kql`](sentinel.kql)

## Tuning
- **Dwell (`minRun`):** default 3 consecutive out-of-band samples. Raise for noisy tags, lower for safety-adjacent tags where speed matters.
- **Mode gating:** the baseline is keyed by `mode`; a value that's out-of-band for `run` may be perfectly normal for `startup`. Ensure the mode tag is accurate, or the detection inherits its errors.
- **Band source:** prefer engineering limits. If a tag has only statistical bands and fires often on legitimate excursions, that's a baseline gap — re-seed, don't just widen.
- Suppress during MOC / maintenance windows.

## Response
1. **Do not touch the control system.** This is a detection, not a control action.
2. Check whether the excursion is explained by a legitimate mode change the `mode` tag missed.
3. Corroborate: is there a matching Nozomi/Claroty write to this tag's controller? An operator action? A second sensor?
4. If uncorroborated and the tag is process- or safety-critical, escalate per runbook.

## MITRE ATT&CK for ICS
- **T0836** — Modify Parameter
- **T0831** — Manipulation of Control

## Validation
See [`validation.md`](validation.md).
