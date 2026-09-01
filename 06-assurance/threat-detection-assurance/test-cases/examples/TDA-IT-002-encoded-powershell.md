# TDA-IT-002 — Encoded PowerShell execution

| Field | Value |
|-------|-------|
| Use case | Obfuscated / encoded PowerShell |
| Detection tested | EDR-01 |
| ATT&CK | T1059.001 Command & Scripting: PowerShell |
| TDA goals | Log validation · Logic · Speed |
| Layer / severity | IT / endpoint · High |
| Environment | Lab / authorized |

## Objective
Prove that encoded/obfuscated PowerShell execution is detected with the command line captured, within MTTD.

## Preconditions (log validation)
- **4104** script-block and **4688**/Sysmon 1 (with command line) — or MDE `DeviceProcessEvents` — feeding the SIEM.
- EDR-01 rule deployed.

## Attack simulation
Instrumented lab host. Record start time.
```
# Benign encoded command (writes a marker, no harm) - lab only
powershell.exe -NoProfile -EncodedCommand \
  VwByAGkAdABlAC0ASABvAHMAdAAgACcAVABEAEEAIAB0AGUAcwB0ACcA
# (decodes to: Write-Host 'TDA test')
```
Atomic Red Team alternative: **T1059.001** atomics (encoded command / download cradle variants). Capture execution timestamp.

## Expected detection
EDR-01 matches `-enc`/`-EncodedCommand`/`FromBase64String`/`IEX`/hidden-window patterns. Expected fields: **host, user, parent process, full command line**.

## Validation criteria
- [ ] Data present — process-creation event with **command line** captured (this is the #1 silent gap).
- [ ] Rule fired — EDR-01 alert on the encoded execution.
- [ ] Fidelity — full decoded/encoded command line present.
- [ ] Speed — MTTD ≤ target.
- [ ] FP — legitimate admin/automation encoded use is allow-listed.

## Result (fill in)
State: ☐ Pass ☐ Partial ☐ Fail-no-rule ☐ Fail-no-data · MTTD: ____ · Evidence: · Notes:

## Remediation (if failed)
- No command line → enable 4688 command-line auditing / script-block logging / deploy Sysmon.
- Rule miss → widen the encoded-pattern set; check case sensitivity.
- Noisy → allow-list known automation; then retest.
