# 04 — Response

Safety-first response content: playbooks, SOPs, evidence-handling guides, and templates.

| Path | Contents |
|------|----------|
| `playbooks/` | 9 playbooks + template + index |
| `sop/` | Universal and OT investigation SOPs, first-30-minutes triage |
| `evidence/` | Evidence source matrix and 6 per-domain acquisition guides |
| `templates/` | Chain of custody, evidence collection log, incident report |

## Playbook structure

Every playbook carries: **Trigger · Severity guide · Safety check · Investigate (passive) ·
Decide · Respond (only with sign-off) · Close**. `tools/validate.py` fails the build if any
section is missing.

Two sections deserve emphasis:

**Severity guide** — the default severity plus *concrete, checkable* escalation criteria.
Not "if it looks suspicious" but "if the connecting host is not the asset's normal
engineering workstation".

**Safety check** — the gate asked *before* investigation begins: is there a legitimate
operational explanation that was not logged? It exists because **most hits on most OT
playbooks are legitimate work with missing paperwork**, and because an analyst who skips it
is one step from a disruptive response to a non-event. In `PLAYBOOK-OT-05` the question
inverts — there it asks whether the safety function is currently able to do its job.

## The playbooks

| ID | Title | Default severity |
|----|-------|------------------|
| OT-01 | Engineering software activity outside change window | Medium |
| OT-02 | Unauthorized setpoint or parameter change | Medium |
| OT-03 | Unauthorized PLC / controller logic change | High |
| OT-04 | Malware or ransomware on an OT host | High |
| OT-05 | Safety instrumented system manipulation | **Critical** |
| OT-06 | Suspicious remote access into OT | High |
| OT-07 | Unauthorized control command on an OT protocol | High |
| OT-08 | New or rogue asset in an OT zone | Medium |
| OT-09 | Process data anomaly (historian-detected) | Medium |

Investigate steps are **read-only in every playbook**. Anything that writes, resets, or
disconnects belongs in Respond, behind sign-off.
