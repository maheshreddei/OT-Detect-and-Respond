# OT Investigation SOP

The OT-specific procedure, invoked from the [Universal SOP](universal-investigation-sop.md) whenever OT assets are in scope. Organized around six OT investigation domains, each mapped to MITRE ATT&CK for ICS and to the evidence guides.

**Every action in this SOP that touches Purdue Level 2 or below is engineer-led and operations-authorized. The SOC investigates and recommends; operations decides for the process.**

## Domain 1 — Network & protocol activity
*What crossed the wire.* Detect and prove unauthorized OT protocol actions (writes, program transfers, session establishment, recon).
- Evidence: Nozomi/Dragos alerts & asset-change log, Zeek ICSNPP logs, **full pcap** from tap/SPAN, boundary firewall logs.
- Proves: exact protocol commands (Modbus write, S7 STOP, DNP3 operate), source/destination, session timing.
- Method: **passive** — pull from taps and sensors; no active scanning of OT.
- Guide: [`../evidence/network-and-ot-protocols.md`](../evidence/network-and-ot-protocols.md). ATT&CK: T0855, T0836, T0846, T0867.

## Domain 2 — Engineering workstation & HMI hosts
*Who operated the tools.* The EWS is the crown jewel — it can program controllers. Prove logon, tool execution, project changes, and lateral movement.
- Evidence: Windows security/Sysmon/PowerShell logs, prefetch, registry, scheduled tasks, engineering-software (TIA/Studio 5000/PCS7) project files & logs, USB/RDP artifacts.
- Proves: who logged in, what engineering software ran, whether a project was opened/modified/downloaded.
- Method: EDR telemetry first; disk/memory acquisition only if the host tolerates it, engineer-coordinated.
- Guide: [`../evidence/windows-ews-hmi-historian-host.md`](../evidence/windows-ews-hmi-historian-host.md). ATT&CK: T0843, T0867, T0873.

## Domain 3 — Controller / PLC integrity
*Was the logic changed.* The Stuxnet/TRITON question. Prove whether running controller logic, config, or firmware was modified.
- Evidence: read-only **logic upload compared to golden baseline**, controller diagnostic buffer/event log, firmware version, online/offline compare in the engineering tool.
- Proves: unauthorized logic/config/firmware modification (or clears the controller).
- Method: **read-only, engineer-led, capture-or-lose.** Never download/write. Prefer proving the change from the *network capture* of the transfer if one exists (Domain 1) before touching the controller.
- Guide: [`../evidence/plc-controller-safe-acquisition.md`](../evidence/plc-controller-safe-acquisition.md). ATT&CK: T0843, T0839, T0857, T0889.

## Domain 4 — Process & historian (physics)
*What happened to the process.* The decisive OT evidence — the physical record no attacker view-spoof survives if you have an independent source.
- Evidence: historian value trends, **alarm & event journal**, setpoint-change records, batch/sequence logs.
- Proves: setpoint manipulation, PV excursion, trip-point approach, alarm suppression, and the **real physical impact** of the incident.
- Method: **safe, non-disruptive, do early.** Export and hash.
- Guide: [`../evidence/historian-and-process.md`](../evidence/historian-and-process.md). ATT&CK: T0831, T0836, T0880, T0856.

## Domain 5 — Identity, remote access & vendor paths
*How they got in and moved.* Remote access and vendor connections are the most common OT entry vectors.
- Evidence: AD security logs, VPN/remote-access gateway logs, jump-host logs, MFA/PAM logs, vendor-access records.
- Proves: initial access, account misuse, cross-zone traversal, session hijack.
- Guide: [`../evidence/identity-and-remote-access.md`](../evidence/identity-and-remote-access.md). ATT&CK: T0822, T0859, T0886.

## Domain 6 — Safety instrumented system (SIS)
*The highest-consequence domain.* Any SIS involvement is minimum SEV-1 and engages plant safety authority.
- Evidence: SIS engineering-tool logs, SIS controller diagnostic/event logs, safety-PV historian trends and trip records, key-switch position records (RUN/PROGRAM), SIS logic compare to baseline.
- Proves: attempts to modify, bypass, or approach/defeat safety functions.
- Method: **extreme caution, safety-authority-led.** Treat the SIS as sacrosanct; capture without any action that could affect its function.
- ATT&CK: T0880, T0837, T0858.

## Cross-domain synthesis
The strongest OT findings corroborate across domains: a Domain 5 remote session → Domain 2 EWS logon → Domain 1 program-transfer on the wire → Domain 3 logic-compare mismatch → Domain 4 process deviation. That chain, each link artifact-backed, is an irrefutable narrative. Build it in the timeline (Universal SOP Step 5).
