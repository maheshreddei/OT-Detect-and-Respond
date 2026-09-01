# PLAYBOOK-OT-02 — Unauthorized setpoint or parameter change

**Trigger.** A detection fires because a setpoint, alarm limit, or tuning parameter changed
outside an approved change window, exceeded a safe delta threshold, or was written by an
account or host outside the approved operator set.

Catalog references: `OTD-0016` (alarm suppression / alarm-config change),
`SIGMA:it-dmz-ot-crosszone/21` (setpoint change exceeding safe delta),
`HIST-B01` (setpoint outside range), `SIS-E*` (bypass/override family).

**Severity guide.** Medium by default. Escalate to **High** if the parameter governs a
protective function (alarm limit, interlock threshold, trip point), if the change was made
from a host that is not a sanctioned HMI/EWS, or if multiple setpoints changed in a short
window. Escalate to **Critical** if the affected parameter belongs to a safety
instrumented function — hand off to `PLAYBOOK-OT-05`.

**Safety check.** Is the plant in startup, shutdown, grade change, or a commissioning
phase? Operating-point changes are routine and expected during these, and a legitimate
post-MOC operating change will look identical to an attack on the wire. Check the shift log
and the MOC (Management of Change) record, and call the control room before treating this
as malicious. Ask explicitly: *is the process behaving normally right now?*

## Investigate (passive) — every step here is read-only

1. Identify the exact tag/parameter, its previous value, its new value, and the magnitude
   of the delta against its documented safe range.
2. Pull the SCADA/HMI application audit trail for operator identity and the workstation
   used; compare against the approved operator list for that area.
3. Pull historian trends for the affected loop across the change — did the process value
   actually move, and did it stay inside the safe envelope?
4. Pull the alarm journal for the same window: were alarms raised, acknowledged, or
   suppressed around the change?
5. Check network telemetry for the write itself (protocol, function code, source host) to
   confirm the audit trail and the wire agree. A mismatch between them is itself a finding.

**Decide.** Three branches:

- **Confirmed legitimate operational change** → close as false positive; if there is no MOC
  record, route the process gap to the change-management owner.
- **Unclear** → contact the shift engineer and the loop owner directly; **do not proceed
  until you have a human answer.** Do not revert a setpoint on your own judgement.
- **Unauthorised or unexplained** → escalate to incident response; if the change reached a
  controller via a logic download rather than a normal write, move to `PLAYBOOK-OT-03`.

**Respond (only with sign-off).** Reverting a setpoint is a **process action, not a
security action** — it is operations' decision and operations' hand on the keyboard.
Account disablement and session termination require the asset owner's approval, since the
account may belong to an operator actively running the unit.

**Close.** Record the tag, the before/after values, the identity chain, and the decision.
Where the audit trail and network telemetry disagreed, raise that as a logging-integrity
finding regardless of the outcome.
