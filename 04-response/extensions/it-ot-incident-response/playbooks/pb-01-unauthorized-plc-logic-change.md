# PB-01 — Unauthorized PLC / Controller Logic Change

**Minimum severity: SEV-1** (controller logic modification is an auto-escalator). ATT&CK ICS: T0843 (Program Download), T0889 (Modify Program), T0839 (Module Firmware).

## Indicators
Nozomi/Dragos program-transfer alert; S7comm download / logic-transfer on the wire; EWS engineering-tool activity out of change window; operators report unexpected process behaviour; controller mode change to PROGRAM.

## Immediate triage
- Raise SEV-1, notify operations, controls engineering, and safety authority.
- Confirm whether the process is behaving normally *now*; if not, operations leads process-safety response in parallel.
- Begin non-disruptive preservation (below) immediately — **do not touch the controller yet.**

## Evidence to collect — and what it proves
1. **Network transfer (prove it happened, passively — do first).** pcap + Zeek `s7comm.log`/Nozomi alert → proves a download/upload occurred, when, from which source. → [network guide](../evidence/network-and-ot-protocols.md) (matrix §F).
2. **EWS artifacts (prove it was prepared).** Engineering-tool logs, project-file modification time & hash, logon events → proves who ran the tool and modified the project. → [windows guide](../evidence/windows-ews-hmi-historian-host.md).
3. **Controller compare (prove the logic differs) — read-only, engineer-led.** Upload running logic, offline-compare to golden baseline; export diagnostic buffer (mode changes, download events), firmware version, key-switch position. → [controller guide](../evidence/plc-controller-safe-acquisition.md) (matrix §F).
4. **Process impact (prove the effect).** Historian trends + alarm journal for the window → proves whether the change altered the process. → [historian guide](../evidence/historian-and-process.md) (matrix §G).
5. **Identity (prove attribution).** Remote-access + AD logs → proves which account/session. → [identity guide](../evidence/identity-and-remote-access.md).

## Analysis
Build the chain: identity/session → EWS logon & project change → network transfer → controller compare mismatch → process deviation. Each link artifact-backed. Determine if the modification is active and whether other controllers were touched.

## Containment (OT-safe — operations-authorized)
- IT-side: disable the implicated account, cut the remote-access path, isolate the EWS (with operations sign-off).
- Controller: **capture read-only first**, then operations + engineering decide whether to restore golden-baseline logic or move the loop to a safe state. A controlled shutdown is operations' call if the modified logic poses process risk.

## Eradication & recovery
Restore verified golden-baseline logic (engineer-led) after confirming compromise; rebuild the EWS from known-good; reset involved credentials; close the entry vector. Validate via historian that the process is back within its safe envelope before recovery sign-off.

## Proof-artifact checklist
- [ ] Network capture of the transfer (hashed)
- [ ] Controller logic compare report vs golden baseline (hashed)
- [ ] Diagnostic buffer export (mode/download events)
- [ ] EWS project file (hashed) + engineering-tool log + logon events
- [ ] Historian trend + alarm journal for the window
- [ ] Identity/session timeline
- [ ] Chain-of-custody complete for all of the above
