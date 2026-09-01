# PLAYBOOK-OT-01 — Engineering software activity outside change window

**Trigger.** A KQL, SPL, or Sigma detection fires because TIA Portal, Studio 5000, Control
Expert, RSLogix, or a similar engineering tool ran on an EWS or connected to a controller
outside the site's approved change window.

Catalog references: `OTD-0015` (rogue engineering workstation to PLC),
`SIGMA:it-dmz-ot-crosszone/14` (engineering software launched by non-engineering account),
`SIGMA:ot-ics-soc/04` (write outside approved change window).

**Severity guide.** Medium by default. Escalate to **High** if the connecting host is not
the asset's normal engineering workstation, or if the activity targets a safety controller.
Escalate to **Critical** if a logic download or online edit actually reached an SIS asset —
that is `PLAYBOOK-OT-05` territory, not this one.

**Safety check.** Is a maintenance window, commissioning activity, or emergency repair in
progress that was not logged in the change-management system? Check the shift log and call
the control room before assuming malicious intent — **most hits on this playbook are
legitimate work with missing paperwork.** Confirm before proceeding.

## Investigate (passive) — every step here is read-only

1. Pull the EWS's process list around the event time (Sysmon Event ID 1 / EDR timeline).
2. Identify the logged-on user and compare against the asset's approved engineer list.
3. Check network telemetry for what the EWS talked to: which controller IP, which protocol
   function code (upload vs download vs online-monitor), and for how long.
4. Pull the controller's own audit trail if the platform supports it (S7 diagnostic buffer,
   Logix controller log — see `04-response/evidence/plc-controller-safe-acquisition.md`).
5. Check whether this EWS shows indicators from prior hunts: unusual parent process,
   unsigned add-in, outbound connection to a non-plant destination.

**Decide.** Three branches:

- **Confirmed legitimate work, missing paperwork** → close as false positive, remind the
  team to log changes, route the process gap to the change-management owner. No further
  action.
- **Unclear** → contact the asset owner and the shift engineer directly; **do not proceed
  until you have a human answer.**
- **Unauthorised or unexplained** → escalate to `PLAYBOOK-OT-03` if a download or online
  edit actually reached a controller; escalate to incident response
  (`04-response/sop/ot-investigation-sop.md`) if the EWS itself shows compromise indicators.

**Respond (only with sign-off).** Engineering-station network isolation, forced logoff, or
credential reset — all require the asset owner's approval, because the EWS may be
mid-session with a controller and an abrupt disconnect can leave the controller in an
undefined online-edit state.

**Close.** Record the finding, the evidence reviewed, and the decision in the hunt log. If
it was legitimate work, note the process gap and route it to the change-management owner.
