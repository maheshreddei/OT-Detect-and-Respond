# G01 — SIF Trip-Point Approach ⭐

## Problem
This is the **TRITON/TRISIS precursor detection.** In a safety-targeting attack, the adversary manipulates the process toward a hazardous condition while keeping the basic process control system (BPCS) view looking routine — the goal is to approach or defeat the Safety Instrumented System (SIS) without tripping the operator's suspicion. By the time the safety instrumented function (SIF) trips, you're already at the hazard boundary; by the time it's *defeated*, there's no trip at all.

The detection opportunity is the **approach**: a safety-related PV trending steadily toward its SIF trip setpoint, especially when the BPCS control layer looks normal (no process alarm, controller not obviously fighting). Catching the drift toward the trip point buys response time *before* the safety system is tested.

## Detection concept
For each safety-related PV, the `sif_trip_limits` lookup provides the trip setpoint, direction (high/low), a pre-alarm value, and an engineering `safe_margin`. The detection:
1. Computes the **margin** between the current value and the trip point (respecting trip direction).
2. Fires when the value is **inside the safe margin** (approaching the trip) —
3. **and** the margin is **shrinking** (a sustained approach, not a stable offset) —
4. optionally weighted higher when the BPCS control layer appears normal (the deceptive-approach signature).

Margin shrinking over a rolling window separates a genuine approach from a tag that simply operates close to its trip. Reaching the pre-alarm level escalates severity.

## Data required
- Safety-related historian PVs (`tag`, `value`, `quality`) per [`docs/historian-data-model.md`](../../../../docs/historian-data-model.md)
- Safety trip lookup `sif_trip_limits.csv` (`trip_direction`, `trip_value`, `prealarm_value`, `safe_margin`)
- Optional: companion BPCS alarm-state / controller-output tags for the "control looks normal" enrichment

> **This detection does not replace the SIS.** The SIS is an independent protection layer and must remain so. G01 is a *monitoring* control that provides early warning and forensic signal — it never interacts with the safety system.

## Logic
- Splunk: [`splunk.spl`](splunk.spl)
- Sentinel: [`sentinel.kql`](sentinel.kql)

## Tuning
- **`safe_margin`** is an engineering value from the process safety team / LOPA study, **not** a statistical one. It defines "close enough to the trip to care." Get it from the SIS documentation, don't invent it.
- **Approach window:** default 10 samples for the margin-rate calculation. Widen for slow processes (level, temperature), narrow for fast ones (pressure).
- **Rate threshold:** fire only when `margin_rate < 0` (closing). Add a small deadband so noise around a stable offset doesn't read as an approach.
- **Control-normal weighting:** if companion alarm/CV tags are available, raise severity when the PV approaches the trip *without* a corresponding BPCS alarm — that's the deceptive signature. If they're not available, the PV-only version still works.
- **Never suppress this one heavily.** Safety-adjacent detections favour sensitivity over a clean queue.

## Response
Treat any confirmed approach as **safety-relevant and time-critical.**
1. **Do not act on the control or safety system** from a potentially compromised view.
2. Notify the control room / shift supervisor immediately — a human at the console is the fastest independent check.
3. Corroborate the PV with an independent reading (ties directly to E01) — is the approach real, or is the safety PV itself being spoofed?
4. Check for BPCS-layer manipulation feeding the approach (setpoint change B01, spoofed feedback B03) and for any engineering/rogue-master activity against the SIS controller on the NDR.
5. Escalate on the safety IR path, not just the cyber path. A potential loss-of-safety event is a plant-safety incident.

## MITRE ATT&CK for ICS
- **T0880** — Loss of Safety
- **T0837** — Loss of Protection

## Validation
See [`validation.md`](validation.md).
