# B01 — Setpoint Outside Approved Range

## Problem
The **Oldsmar detection.** An attacker (or an errant insider) writes a setpoint far outside the Management-of-Change-approved operating range — the 2021 Oldsmar water attack drove sodium hydroxide dosing from 100 ppm toward 11,100 ppm. Unlike a PV excursion, a setpoint jump is a direct human/attacker *intent* signal: setpoints don't drift, they're written.

## Detection concept
For each setpoint (`*.SP`) tag, the baseline carries the MOC-approved `sp_min`/`sp_max` (engineering limits, not statistics). Alert when a written SP falls outside that band. Because setpoints change infrequently and deliberately, this detection tolerates a very tight band and needs little persistence logic — a single out-of-range write is the event.

A companion signal (see B02) is *when* the change happened; an in-range change at 03:00 off-shift is its own weaker signal.

## Data required
- Setpoint tags (`*.SP`) per [`docs/historian-data-model.md`](../../../../docs/historian-data-model.md)
- Approved SP band. In the sample lookup this is carried as `ll`/`hl` on the SP rows of `ot_baseline.csv`; in production, source these from the MOC register / SP limit register, not from observed data.

## Logic
- Splunk: [`splunk.spl`](splunk.spl)
- Sentinel: [`sentinel.kql`](sentinel.kql)

## Tuning
- SP limits are **authoritative engineering values**. Keep them in a change-controlled register; a widened SP limit should itself be an MOC.
- Detect on the *change*, not on every sample, to avoid re-alerting on a value that sits out-of-range: alert when a new SP value differs from the prior and is out of band.
- Correlate with an NDR write to the same controller for high-confidence attribution.

## Response
1. Identify the write source: which HMI/engineering station/account issued the SP change? Correlate with NDR and Level-3 auth logs.
2. **Do not revert from a possibly-compromised console.** Route corrective action through verified operations.
3. If unattributable to a legitimate operator action, escalate as parameter modification — potentially safety-relevant depending on the loop.

## MITRE ATT&CK for ICS
- **T0836** — Modify Parameter

## Validation
See [`validation.md`](validation.md).
