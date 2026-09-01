# Evidence: Identity & Remote Access

Remote access and vendor connections are the **most common OT entry vectors**, and identity evidence is what ties an action to a *who*. Network evidence proves a command was sent; identity evidence proves which account and session sent it. Most of it is safe to collect.

## Active Directory & authentication
| Evidence | Location | Proves |
|----------|----------|--------|
| Kerberos TGT/TGS 4768/4769/4771 | Domain Controller Security log | Domain auth, ticket requests, Kerberoasting/spray patterns |
| NTLM auth 4776 | DC Security log | NTLM logons, relay/spray indicators |
| Logon/logoff 4624/4634 (+ type, source IP) | Host + DC | Where/how each session authenticated |
| Account/group changes 4720/4728/4732/4756 | DC | Account creation, privilege escalation |
| Credential-dumping precursors (4672, LSASS access via Sysmon 10) | Host | Admin logon, credential theft attempts |

## Remote access & vendor paths (top OT entry vector)
| Source | Proves | Collect |
|--------|--------|---------|
| VPN / remote-access gateway | Remote session: user, source IP, start/end, duration | Gateway log export |
| Jump / bastion host | The pivot into the DMZ/OT: who connected onward, when | Host logs + acquisition |
| Vendor-access solution (e.g. dedicated OT remote access) | Third-party session: which vendor, which asset, what scope | Solution audit log |
| MFA provider | Whether MFA was satisfied or bypassed; impossible-travel | MFA/IdP logs |
| PAM / privileged session manager | Recorded privileged sessions, sometimes full session video | PAM audit + recordings |

## Session-hijack & anomaly indicators
- **Impossible travel / concurrent sessions** — same account, two geographies/hosts at once.
- **Off-hours / off-window access** to OT — correlate with maintenance calendar.
- **Service or shared account from an unusual source** — service accounts should have predictable source hosts.
- **Vendor session outside its approved scope or duration** — vendor connected to an asset it has no business touching.

## Collection & correlation
1. Export gateway/VPN/jump-host/PAM logs for the incident window.
2. Pull AD auth from the DC(s) for the involved accounts.
3. Build the **identity timeline**: initial auth → remote session → jump-host pivot → OT-side logon → action. Each hop is an artifact.
4. Correlate identity with network (the traversal) and host (the actions performed) — this is what turns "an action occurred" into "*this account*, via *this session*, performed *this action*."

## What identity evidence proves
- **Initial access** and its vector (which remote path, which credential).
- **Attribution** — the account/session behind an action.
- **Cross-zone traversal** by identity (same principal on both sides of the boundary).
- **Account/privilege abuse** and creation of footholds.
Its limit: an account is not a person. Where it matters (insider, HR, legal), corroborate the account with badge/physical-access records, endpoint session, and interviews via the appropriate authority.
