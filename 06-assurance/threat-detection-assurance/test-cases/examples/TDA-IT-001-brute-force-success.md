# TDA-IT-001 — Brute-force success after failures

| Field | Value |
|-------|-------|
| Use case | Credential brute force resulting in success |
| Detection tested | IAM-03 (also IAM-01/02) |
| ATT&CK | T1110 Brute Force · T1078 Valid Accounts |
| TDA goals | Log validation · Logic · Speed |
| Layer / severity | IT / identity · High |
| Environment | Lab / authorized |

## Objective
Prove that a burst of failed logons followed by a success for the same account/source raises the expected alert, with the right entities, within the MTTD target.

## Preconditions (log validation)
- Windows Security events **4625/4624** (or Entra `SigninLogs` + `AADNonInteractiveUserSignInLogs`) feeding the SIEM.
- IAM-03 rule deployed and enabled.

## Attack simulation
Lab host / test account. Record the exact start time.
```
# Simulate N failed logons then a success (lab test account)
for i in $(seq 1 12); do
  # authenticate with a wrong password (tooling of choice, e.g. crackmapexec/smb, or RDP)
  echo "$(date -u +%FT%TZ) attempt $i (fail)"
done
# then one correct authentication
echo "$(date -u +%FT%TZ) success"
```
Atomic Red Team alternative: relevant **T1110** atomics against a lab target. Capture the timestamp of the successful logon (this anchors MTTD).

## Expected detection
IAM-03 logic: ≥ N failures then a success for the same user+source within the window → one alert. Expected alert fields: **user, source IP, failure count, first/last failure, success time**.

## Validation criteria
- [ ] Data present — 4625 and 4624 (or Signin logs) arrived for the test account.
- [ ] Rule fired — exactly one IAM-03 alert for the correct user+source.
- [ ] Fidelity — alert carries user, source, failure count, success time.
- [ ] Speed — MTTD ≤ target (e.g. High ≤ 30 min).
- [ ] FP — normal lockout/typo activity does not trigger it.

## Result (fill in)
State: ☐ Pass ☐ Partial ☐ Fail-no-rule ☐ Fail-no-data · MTTD: ____ · Evidence: (alert link/screenshot) · Notes:

## Remediation (if failed)
- No data → onboard/repair 4625/4624 or non-interactive Signin logs.
- Rule didn't fire → check window/threshold and the failure→success join.
- Too slow → check ingestion latency / rule schedule.
- Too noisy → exclude known service-account failure patterns; then retest.
