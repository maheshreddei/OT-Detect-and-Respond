# TDA-OT-003 — SIS key-switch to PROGRAM

| Field | Value |
|-------|-------|
| Use case | Safety controller mode change enabling logic edits |
| Detection tested | SIS-B4 (sis-safety-detection) |
| ATT&CK for ICS | T0858 Change Operating Mode |
| TDA goals | Log validation · Logic · Escalation-path |
| Layer / severity | OT / safety · Critical (SEV-1) |
| Environment | **Event injection only — never live against an SIS** |

## Objective
Prove that a safety-controller key-switch/mode change to PROGRAM raises a SEV-1 alert **and routes to the safety authority** — validated without ever touching a live SIS.

## Preconditions (log validation)
- Historised key-switch / mode tag (or SIS diagnostic event) feeding the SIEM.
- SIS-B4 rule enabled; SEV-1 escalation path defined.

## Attack simulation (safe — injection only)
Do **not** change a real safety controller's mode. Inject a representative event into the SIEM/historian test index:
```
# Inject a key-switch RUN -> PROGRAM transition into the test index
# (example: HTTP/HEC event, or write to a historian test tag)
{ "tag": "SIS.CTRL01.KEYSWITCH", "prev": "RUN", "value": "PROGRAM",
  "time": "<UTC now>", "source": "TDA-OT-003" }
```
Record the injection timestamp.

## Expected detection
SIS-B4 fires on RUN→PROGRAM/REMOTE. Fields: **controller/tag, previous mode, new mode, time**. Alert severity = **SEV-1**, routed to the safety authority path.

## Validation criteria
- [ ] Data present — the key-switch tag/event is ingested (log validation).
- [ ] Rule fired — SIS-B4 alert on the transition.
- [ ] Severity — raised as **SEV-1**.
- [ ] **Escalation** — routed to the safety authority (validate the path; tabletop if needed).
- [ ] No live SIS was touched (by construction).

## Result (fill in)
State: ☐ Pass ☐ Partial ☐ Fail-no-rule ☐ Fail-no-data · MTTD: ____ · Evidence: · Notes:

## Remediation (if failed)
- No data → historise the key-switch DI / collect SIS diagnostic events (**blind spot** if unmonitored).
- Rule miss → confirm SIS-B4 mode values and tag pattern.
- Wrong routing → fix SEV-1 escalation to the safety authority; retest via tabletop.
