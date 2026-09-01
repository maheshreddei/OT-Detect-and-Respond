# PLAYBOOK-OT-07 — Unauthorized control command on an OT protocol

**Trigger.** A protocol-level detection fires on a control or disruptive command: a Modbus
write from a non-authorized master, a DNP3 cold/warm restart or disable-unsolicited, an
IEC-104 control ASDU from an unexpected source, an S7 STOP, or a CIP service that changes
controller state.

Catalog references: `OTD-0003` (Modbus unauthorized write), `OTD-0004` (Modbus FC08
restart), `OTD-0005` (S7comm STOP CPU), `OTD-0007` (DNP3 restart), `OTD-0008` (DNP3 block
reporting), `OTD-0009` (IEC-104 unauthorized control), plus the `ot-ics-soc` Sigma library
and the protocol NDR families.

**Severity guide.** **High** by default. Escalate to **Critical** if the command targets a
safety controller (→ `PLAYBOOK-OT-05`), if it is a restart/stop affecting a live process,
or if multiple controllers received commands in a short window. Reduce to **Medium** only
where the source is a known master whose allowlist entry is simply missing — a
configuration gap, not an intrusion.

**Safety check.** **Did the process move?** Before attributing intent, establish whether the
commanded change actually took effect and whether the process is inside its safe envelope
now. Then check whether commissioning, loop checks, or a vendor factory-acceptance activity
is running — loop checks legitimately write to coils and registers all day. Call the
control room. A restart command during a scheduled device swap is routine; the same command
at 02:00 on a running unit is not.

## Investigate (passive) — every step here is read-only

1. Identify the exact command: protocol, function code, target address/point, and value
   written.
2. Identify the source host and compare against the authorized master / EWS allowlist for
   that zone. Determine whether the source is even supposed to speak this protocol.
3. Confirm on the wire whether the controller accepted the command (response code) or
   rejected it — an exception response tells a different story than an acknowledgement.
4. Pull historian trends for the affected point across the command window to establish
   physical effect.
5. Check for a pattern: enumeration or scanning preceding the write, repeated attempts, or
   commands to several controllers.
6. Correlate with identity and remote-access telemetry to attribute the source host to a
   human session.

**Decide.** Three branches:

- **Confirmed legitimate control action** (known master, missing allowlist entry, active
  loop check) → close as false positive and route the allowlist gap to the detection owner
  for tuning. Record the source so the baseline improves.
- **Unclear** → contact the shift engineer and the loop owner; **do not block the source
  host on ambiguity** — it may be a production master.
- **Unauthorised or unexplained** → escalate to incident response; if a logic download
  rather than a runtime write, move to `PLAYBOOK-OT-03`.

**Respond (only with sign-off).** Blocking a source host or filtering a protocol at the
firewall requires operations approval — if the source turns out to be a production master,
blocking it causes the outage the detection was meant to prevent. Never issue a
counter-command to "undo" a write; reverting process state is operations' action under
their procedure.

**Close.** Record the command, the source, whether it was accepted, and the measured
process effect. Where the finding was an allowlist gap, feed the corrected baseline back
into the detection content and note it as a tuning change with a version bump.
