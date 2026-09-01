# PLAYBOOK-OT-06 — Suspicious remote access into OT

**Trigger.** A detection fires on the remote-access path: VPN or jump-host authentication
outside an approved window, a vendor account used from an unexpected geography, a dormant
account's first use after long inactivity, a session bypassing the jump host, or a session
whose duration or scope is anomalous.

Catalog references: `OTD-0001` (external remote services abuse), `SIGMA:advisory/15`
(vendor VPN outside approved window/geography), `SIGMA:advisory/16` (dormant vendor account
first use), `SIGMA:it-dmz-ot-crosszone/01` (direct IT→OT bypassing jump host),
`SIGMA:it-dmz-ot-crosszone/11` (vendor session duration/scope anomaly).

**Severity guide.** **High** by default — remote access is the most common initial-access
path into OT. Escalate to **Critical** if the session bypassed the jump host entirely, if
it reached Level 2 or below, if it used a shared/service account, or if control-protocol
traffic followed the session. Reduce to **Medium** only after confirming the vendor and the
work order — never before.

**Safety check.** Is a vendor support call, emergency repair, or scheduled remote
maintenance in progress? Vendor remote access is normal and often urgent — a plant with a
tripped unit may have a vendor connected at 03:00 with entirely legitimate cause and no
paperwork. Check the shift log, the work-order system, and call the control room. Ask
whether anyone is currently expecting a vendor on the system, and whether cutting the
session would interrupt an active repair.

## Investigate (passive) — every step here is read-only

1. Establish the full session chain: source IP and geography → VPN authentication → jump
   host logon → onward connections into OT. A gap in that chain (e.g. OT access with no
   corresponding jump-host session) is itself the finding.
2. Identify the account: is it a named individual, a shared account, or a vendor account?
   Check last-use history and whether the account should still be active.
3. Compare session time against the approved maintenance window and the account's normal
   pattern.
4. Determine what the session reached: which hosts, which zones, which Purdue level, and
   whether any OT control protocol was used.
5. Pull session recording if the access broker provides it.
6. Check for follow-on activity: engineering tool launch, file transfer, credential use on
   other hosts.

**Decide.** Three branches:

- **Confirmed authorised support work** → close as false positive; route missing work-order
  or window records to the access-management owner.
- **Unclear** → contact the asset owner and the vendor's site sponsor directly; **do not
  terminate an active session on ambiguity** — it may be mid-repair.
- **Unauthorised or unexplained** → escalate to incident response. If control-protocol
  traffic or engineering activity followed the session, move to `PLAYBOOK-OT-01` or
  `PLAYBOOK-OT-03` as appropriate.

**Respond (only with sign-off).** Session termination and account disablement require asset
owner approval, because the session may be an active repair on a running unit and an abrupt
cut can leave an engineering operation half-complete. Prefer to *observe and contain the
blast radius* over immediate disconnection while the operational picture is being
established. Revoking vendor access is an access-management action with contractual
implications — route it, do not do it unilaterally.

**Close.** Record the session chain, the account, what was reached, and the authorisation
outcome. Where access bypassed the jump host, raise that as an architecture finding
separate from the incident outcome — the control gap persists regardless of whether this
session was malicious.
