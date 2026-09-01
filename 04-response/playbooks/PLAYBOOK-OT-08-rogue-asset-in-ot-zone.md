# PLAYBOOK-OT-08 — New or rogue asset in an OT zone

**Trigger.** A detection fires because a node appeared in a monitored OT zone that is not in
the learned inventory, a first-time communication crossed a zone boundary, a new MAC
appeared on a switch port, or an unexpected wireless client associated.

Catalog references: `OTD-0014` (new/unauthorized node on OT segment), `OTD-0002`
(internet-accessible ICS device), `OTD-0026` (unauthorized wireless/cellular modem),
`SIS-A4` (new asset on the safety network), `SIGMA:it-dmz-ot-crosszone/23` (first-time
cross-zone communication).

**Severity guide.** **Medium** by default. Escalate to **High** if the node appeared in a
Level 1/2 process zone, if it speaks a control protocol, or if it has any path to or from
public address space. Escalate to **Critical** if the node appeared inside the SIS zone —
hand off to `PLAYBOOK-OT-05`.

**Safety check.** Is a device replacement, commissioning activity, contractor visit, or
temporary test set in progress? New assets appear in OT for entirely routine reasons — a
swapped-out transmitter, a vendor laptop on a loop check, a spare PLC on the bench. Check
the shift log, the work-order system, and the asset-change record before treating this as
rogue. Call the control room and ask plainly whether anyone plugged something in.

## Investigate (passive) — every step here is read-only

1. Characterise the node: IP, MAC, OUI/vendor, open ports, protocols spoken, and the
   Purdue level of the zone it appeared in.
2. Determine where it is physically: switch, port, VLAN — and whether the port was
   previously in use.
3. Establish who it talks to and what it does: passive listening only, or active
   enumeration and control traffic?
4. Check whether it has any external path — public IP, cellular modem, wireless
   association, or a route out through the DMZ.
5. Compare against the asset inventory and any pending change or procurement record.
6. If it speaks a control protocol, check whether any controller responded to it.

**Decide.** Three branches:

- **Confirmed authorised device** (replacement, contractor tool, commissioning) → close as
  false positive and route the inventory gap to the asset owner so the baseline is updated.
- **Unclear** → contact the area engineer and request a physical check; **do not disable the
  switch port on ambiguity** — the node may be a live replacement carrying the process.
- **Unauthorised or unexplained** → escalate. If the node has an external path or is
  performing enumeration, treat as an active intrusion, not an inventory problem.

**Respond (only with sign-off).** Port shutdown, MAC filtering, and quarantine VLAN
assignment all require operations approval, because an incorrectly identified node may be
performing a live process function. Physical removal is an operations action following a
physical verification — the SOC does not unplug things.

**Close.** Record the node's full characterisation, its authorisation outcome, and the
physical verification result. Update the asset inventory and the NDR learned baseline
either way — an authorised device that was never inventoried is a governance finding worth
recording.
