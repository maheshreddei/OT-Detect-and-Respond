# PB-02 — Unauthorized Setpoint Change

**Minimum severity: SEV-2** (SEV-1 if a safety-related setpoint). ATT&CK ICS: T0836 (Modify Parameter), T0831 (Manipulation of Control). The Oldsmar class.

## Indicators
Historian/SIEM setpoint-out-of-range alert; SP written outside approved band or maintenance window; operators notice a dosing/temperature/pressure target moved.

## Immediate triage
- Raise severity; if the loop is safety-related, SEV-1 and engage safety authority.
- Confirm current process state with operations; if the SP is driving the process toward a hazard, operations acts on process safety immediately.

## Evidence to collect — and what it proves
1. **Setpoint-change record (prove the write).** Historian SP tag trend + DCS/SCADA audit trail → proves the SP value, time, and (if audited) user/source. → [historian guide](../evidence/historian-and-process.md) (matrix §G).
2. **Command on the wire (prove how).** pcap / Zeek / Nozomi write alert to the SP register → proves the protocol write and its source. → [network guide](../evidence/network-and-ot-protocols.md) (matrix §E).
3. **Process effect (prove impact).** PV trend + alarm journal → proves how the process responded and whether alarms were suppressed. → matrix §G.
4. **Origin host & identity (prove who).** HMI/EWS logon + remote-access logs → attributes the write. → [windows](../evidence/windows-ews-hmi-historian-host.md) / [identity](../evidence/identity-and-remote-access.md) guides.

## Analysis
Determine whether the change was a legitimate (unlogged) operator action, an insider, or an external actor — the identity + host + network chain distinguishes them. Check whether the SP band itself was altered (an attacker widening limits first is a stronger signal).

## Containment (OT-safe — operations-authorized)
Operations restores the correct setpoint (not the SOC). IT-side: disable the implicated account/session, cut the path. If attribution points to a compromised HMI/EWS, isolate it with operations sign-off.

## Eradication & recovery
Close the access vector; reset credentials; if a host was compromised, rebuild it. Confirm via historian the process is stable within its safe envelope. Consider adding/enabling write-auditing on the control system if it wasn't present (a Prepare gap).

## Proof-artifact checklist
- [ ] Historian SP trend + change record (hashed)
- [ ] Network capture of the write (hashed)
- [ ] PV trend + alarm journal
- [ ] Origin host logon + identity/session timeline
- [ ] Chain-of-custody complete
