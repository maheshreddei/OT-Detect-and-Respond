# PLAYBOOK-OT-03 — Unauthorized PLC / controller logic change

**Trigger.** A detection fires on a program download, online edit, or firmware change
reaching a controller: NDR program-transfer alert, S7comm/CIP logic transfer on the wire,
controller mode change to PROGRAM, or a configuration drift check against the golden
baseline.

Catalog references: `OTD-0006` (S7comm program download), `OTD-0027` (PLC operating mode
change), `OTD-0028` (unsigned/downgrade firmware),
`SIGMA:it-dmz-ot-crosszone/18` (logic/firmware upload from non-engineering host),
`SIGMA:advisory/12` (PLC configuration drift from verified offline backup).

ATT&CK for ICS: T0843 Program Download, T0889 Modify Program, T0839 Module Firmware.

**Severity guide.** **High minimum — controller logic modification is an auto-escalator.**
Escalate to **Critical** (SEV-1) if the target is a safety controller, if the process is
currently behaving abnormally, if more than one controller was touched, or if the source
host is not an approved engineering workstation. This playbook does not have a "Low" branch.

**Safety check.** **Ask first: is the process behaving normally right now?** If it is not,
operations leads a process-safety response in parallel and security follows their lead —
the investigation does not gate the safety response. Then check whether a commissioning,
maintenance, or emergency-repair activity is in progress that was not logged. A legitimate
engineer mid-download and an attacker mid-download look the same on the wire; the shift log
and a phone call to the control room distinguish them faster than any query.

**Do not touch the controller yet.** Begin non-disruptive preservation immediately.

## Investigate (passive) — every step here is read-only

1. **Prove it happened.** PCAP + Zeek `s7comm.log` / `cip.log` or the NDR program-transfer
   alert — establishes that a download occurred, when, and from which source.
2. **Prove it was prepared.** EWS engineering-tool logs, project-file modification time and
   hash, logon events — establishes who ran the tool and modified the project.
3. **Prove the logic differs — read-only, engineer-led.** Upload the running logic and
   offline-compare against the golden baseline. Export the diagnostic buffer (mode changes,
   download events), firmware version, and key-switch position.
4. **Prove the effect.** Historian trends and the alarm journal across the window —
   establishes whether the change altered the process.
5. **Prove attribution.** Remote-access and directory logs — establishes which account and
   session.

Build the chain: identity/session → EWS logon and project change → network transfer →
controller compare mismatch → process deviation. Each link artifact-backed. Determine
whether the modification is still active and whether other controllers were touched.

**Decide.** Three branches:

- **Confirmed legitimate engineering work** → close as false positive; route the missing
  MOC record to the change-management owner. Still record the logic hash for the baseline.
- **Unclear** → contact the asset owner, controls engineering, and the shift engineer;
  **do not proceed until you have a human answer.**
- **Unauthorised or unexplained** → declare an incident. Notify operations, controls
  engineering, and the safety authority.

**Respond (only with sign-off).** IT-side actions — disable the implicated account, cut the
remote-access path, isolate the EWS — require operations sign-off. Controller-side:
**capture read-only first**, then operations and engineering decide whether to restore
golden-baseline logic or move the loop to a safe state. A controlled shutdown is
operations' call, not the SOC's.

**Close.** Record the full evidence chain with hashes and chain-of-custody. Restore verified
golden-baseline logic (engineer-led) only after compromise is confirmed and captured;
rebuild the EWS from known-good; reset involved credentials; close the entry vector.
Validate via historian that the process is inside its safe envelope before recovery
sign-off.
