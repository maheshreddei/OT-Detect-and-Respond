# Triage — First 30 Minutes

A quick-reference card for the analyst who just caught the alert. Goal: decide real-vs-false, scope, consequence, and start preserving decaying evidence — without taking any process-affecting action.

## Do immediately
- [ ] Open the incident record; timestamp everything (with timezone).
- [ ] Record the source: alert/correlation, Nozomi/Dragos, historian deviation, operator report, external notice.
- [ ] Pull the raw event(s) behind the trigger in the SIEM.
- [ ] Identify affected asset(s): **Purdue level, criticality, safety relevance, owner** (from inventory).
- [ ] Note SIEM clock vs. suspect-system clock (offset for timeline).

## Ask the OT escalator questions
If **any** is yes → raise to SEV-1/2 and notify operations now:
- [ ] Is a **safety system (SIS)** or safety-related tag involved?
- [ ] Any sign of **controller logic/firmware modification**?
- [ ] Have operators reported **loss of view or loss of control** / implausible readings?
- [ ] Is activity confirmed **at/below Purdue Level 2** with control-affecting capability?
- [ ] Confirmed **IT→OT cross-zone** movement?

## Start non-disruptive preservation (in parallel — these are decaying)
- [ ] Begin/confirm **network capture** on relevant segment (tap/SPAN) and snapshot device session/ARP tables.
- [ ] Export **historian** values + **alarm/event journal** for the affected process and time window.
- [ ] Capture **volatile host telemetry** via EDR (processes, connections, logged-on users) — do **not** live-poke a fragile HMI mid-process.
- [ ] Confirm **retention** on SIEM/historian/firewall covers the incident window; flag Legal for hold if it's close to rolling off.

## Do NOT (without operations authorization)
- ✗ Isolate/disconnect an HMI, EWS, or historian.
- ✗ Power-cycle, reboot, or "clean" a controller.
- ✗ Move a loop to manual or push any config to an OT asset.
- ✗ Run intrusive scans/tools against L0-L2.

## Decide
- [ ] **False positive** → document the reasoning, close, consider tuning.
- [ ] **Incident** → assign severity, notify per escalation tree, open full investigation ([`universal-investigation-sop.md`](universal-investigation-sop.md)).

> When unsure whether an action is safe on OT: **stop and ask operations.** A 5-minute pause to confirm beats an unplanned trip.
