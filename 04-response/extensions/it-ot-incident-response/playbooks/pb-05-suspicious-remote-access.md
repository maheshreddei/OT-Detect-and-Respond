# PB-05 — Suspicious Remote / Vendor Access into OT

**Minimum severity: SEV-2.** ATT&CK ICS: T0822 (External Remote Services), T0859 (Valid Accounts), T0886 (Remote Services). The most common OT entry vector.

## Indicators
Remote/VPN session into OT off-hours or outside a change window; vendor session touching an asset out of scope; impossible travel / concurrent sessions; MFA anomaly; shared/service account from an unusual source; jump-host session followed by OT-side activity.

## Immediate triage
- Identify the session: user, source, entry path (VPN/vendor solution/jump host), target asset, time.
- Determine what the session *did* — is there subsequent OT activity (logon, write, transfer)?
- If the session reached an EWS/controller/SIS, escalate per the relevant playbook (PB-01/02/03).

## Evidence to collect — and what it proves
1. **Remote-access session (prove the entry).** VPN/gateway/vendor-solution/PAM logs → proves who connected, from where, when, to what, for how long. → [identity guide](../evidence/identity-and-remote-access.md) (matrix §A, §H).
2. **Authentication trail (prove the account).** AD auth, MFA logs → proves credential use, MFA satisfied/bypassed, spray/impossible-travel. → matrix §A/§B.
3. **Traversal (prove cross-zone).** Jump-host logs, boundary firewall, netflow → proves the pivot from remote → DMZ → OT. → [network guide](../evidence/network-and-ot-protocols.md) (matrix §H).
4. **Actions on OT (prove what they did).** Target-host logon + engineering-tool activity + any network commands + historian effect → proves the session's OT actions and impact. → [windows](../evidence/windows-ews-hmi-historian-host.md) / [historian](../evidence/historian-and-process.md) guides.

## Analysis
Build the session-to-action chain: remote auth → gateway session → jump-host pivot → OT-side logon → actions → process effect. Decide legitimate-but-unlogged vs. compromised-account vs. malicious-insider vs. external actor. Vendor scope/duration anomalies are a strong tell.

## Containment (OT-safe)
Terminate the suspicious session; disable the account; cut the specific remote-access/vendor path (often pre-authorized as IT-side). If OT actions occurred, branch to the matching playbook for OT-asset containment (operations-authorized).

## Eradication & recovery
Reset the involved credentials; review and tighten remote-access/vendor policy (scope, time-boxing, MFA, session recording); close the path used. If a host or controller was reached, follow PB-04/PB-01 for rebuild/restore. Validate no residual access remains.

## Proof-artifact checklist
- [ ] Remote-access/VPN/vendor/PAM session logs (hashed)
- [ ] AD + MFA authentication trail
- [ ] Jump-host + boundary + netflow traversal evidence
- [ ] OT-side actions (host/network/historian) if any
- [ ] Identity timeline; chain-of-custody complete
