# Evidence Source Matrix

**The core reference: for each thing you need to prove, where the artifact lives, how to collect it safely, and what it establishes.**

Investigation is hypothesis-driven — you collect evidence to prove or disprove a specific assertion. This matrix is organized by *investigative assertion* so you start from the question, not the tool. Cross-references point to the domain guide with the detailed collection steps.

Legend for **Volatility/OT**: 🟢 safe & non-disruptive · 🟡 low risk, coordinate · 🔴 process risk, engineer + operations authorization required.

---

## A. "An unauthorized login / session occurred"

| Evidence | Location | Collection | Proves | Vol/OT |
|----------|----------|-----------|--------|--------|
| Windows logon events 4624/4625/4634/4647 | `%SystemRoot%\System32\winevt\Logs\Security.evtx` on EWS/HMI/historian | `wevtutil epl Security out.evtx` or EDR export | Interactive/network/RDP logon, success/failure, account, source host | 🟢 |
| Logon type & source IP (in 4624) | Same event, LogonType + IpAddress fields | SIEM query | *How* they logged in (2=console,3=network,10=RDP) and from where | 🟢 |
| AD authentication (Kerberos 4768/4769/4771, NTLM 4776) | Domain Controller Security log | DC log / SIEM | Domain auth, ticket requests, spray/brute patterns | 🟢 |
| VPN / remote-access session | Gateway/VPN concentrator logs | Gateway log export | Remote entry, session start/end, source, user | 🟢 |
| RDP artifacts (bitmap cache, 1149) | `%LocalAppData%\...\Cache\`, TerminalServices logs | Host acquisition | Which RDP sessions ran, partial screen recovery | 🟡 |

## B. "An account was created / privileged / abused"

| Evidence | Location | Collection | Proves | Vol/OT |
|----------|----------|-----------|--------|--------|
| Account creation 4720 / group add 4728/4732/4756 | Security.evtx / DC | SIEM | New account, privilege escalation via group | 🟢 |
| Special privileges assigned 4672 | Security.evtx | SIEM | Admin-equivalent logon | 🟢 |
| Service account used from unusual host | Auth logs + asset context | SIEM correlation | Service/shared account misuse | 🟢 |

## C. "Code / a program executed on a host"

| Evidence | Location | Collection | Proves | Vol/OT |
|----------|----------|-----------|--------|--------|
| Process creation 4688 (+ cmdline) / Sysmon 1 | Security.evtx / Sysmon | SIEM / export | What ran, parent process, command line, hashes | 🟢 |
| PowerShell script block 4104 / 4103 | `Microsoft-Windows-PowerShell/Operational` | SIEM / export | Actual script content executed | 🟢 |
| Prefetch | `%SystemRoot%\Prefetch\*.pf` | Host acquisition (copy) | Program executed + first/last run times + run count | 🟡 |
| Amcache / Shimcache | `Amcache.hve`, SYSTEM hive | Registry acquisition | Execution/presence of binaries, even if deleted | 🟡 |
| Running process / live connections | Live memory / EDR | EDR telemetry; live capture only if host tolerates | Currently-executing malware, C2 | 🟡 |

## D. "A file was created / modified / exfiltrated"

| Evidence | Location | Collection | Proves | Vol/OT |
|----------|----------|-----------|--------|--------|
| $MFT / $LogFile / $UsnJrnl | NTFS volume | Forensic image / triage collector | File creation/rename/delete timeline | 🟡 |
| File create/modify Sysmon 11/2 | Sysmon | SIEM | Specific file written, timestomping | 🟢 |
| Data-transfer flow | Zeek `conn.log`, firewall, pcap | Network capture | Volume/destination of exfil, staging | 🟢 |
| Engineering project file change | See project paths in [windows guide](windows-ews-hmi-historian-host.md) | File hash + timestamp | Control-logic project opened/modified | 🟡 |

## E. "An unauthorized OT protocol command was issued" ★

| Evidence | Location | Collection | Proves | Vol/OT |
|----------|----------|-----------|--------|--------|
| Nozomi/Dragos protocol alert | NDR console / SIEM feed | Export alert + linked session | Write/operate/stop command, source, target, time | 🟢 |
| Zeek ICSNPP protocol log | `modbus.log`, `dnp3.log`, `s7comm.log`, etc. | Log export | Function code, register/point, direction | 🟢 |
| **Full packet capture** | Tap/SPAN on the segment | pcap (hash immediately) | The command *verbatim* — ground truth | 🟢 |
| Boundary firewall log | IT/OT firewall | Log export | The connection that carried it crossed a zone | 🟢 |

## F. "Controller logic / firmware was changed" ★★

| Evidence | Location | Collection | Proves | Vol/OT |
|----------|----------|-----------|--------|--------|
| Program-transfer on the wire | pcap / Zeek `s7comm.log` (download), Nozomi alert | Network capture | A download/upload happened, when, from where — **prove this first, passively** | 🟢 |
| Running-logic vs golden baseline | Controller, via engineering tool | **Read-only upload**, engineer-led, offline compare | The logic actually differs from known-good | 🔴 |
| Controller diagnostic buffer / event log | Controller | Engineering-tool read | Mode changes (RUN/STOP/PROGRAM), download events, faults | 🟡 |
| Firmware version | Controller / asset inventory delta | Read; compare to baseline | Firmware replaced/downgraded | 🟡 |
| Key-switch position record | Controller / SER | Read | Whether protection was in PROGRAM when change occurred | 🟡 |

## G. "The process was physically manipulated" ★★

| Evidence | Location | Collection | Proves | Vol/OT |
|----------|----------|-----------|--------|--------|
| Historian value trend | Historian (PI/Proficy/Canary) | Export CSV + hash | PV excursion, setpoint jump, rate anomaly — the physical effect | 🟢 |
| Setpoint-change record | Historian SP tags / DCS audit | Export | SP written outside approved range/window (Oldsmar-class) | 🟢 |
| Alarm & event journal | Historian/DCS alarm subsystem | Export | Alarm suppression, shelving, trip-point approach | 🟢 |
| Independent value vs HMI-path value | Second historian source / direct read | Compare | View spoofing (Stuxnet-class) — HMI showed normal, reality didn't | 🟢 |
| Batch/sequence record | Batch historian | Export | Step-order or timing manipulation | 🟢 |

## H. "They moved from IT into OT"

| Evidence | Location | Collection | Proves | Vol/OT |
|----------|----------|-----------|--------|--------|
| Boundary firewall allow/deny | IT/OT firewall | Log export | The specific cross-zone connection | 🟢 |
| Jump-host session logs | Jump/bastion host | Log + host acquisition | The pivot through the DMZ | 🟡 |
| Netflow across the boundary | Flow collector | Export | Flow shape/volume of the traversal | 🟢 |
| Matching auth on both sides | IT + OT auth logs | SIEM correlation | Same identity used across the boundary | 🟢 |

## I. "Persistence / they're still here"

| Evidence | Location | Collection | Proves | Vol/OT |
|----------|----------|-----------|--------|--------|
| Run keys / services 7045 | Registry Run keys, System log | Registry + SIEM | Autostart persistence, malicious service install | 🟡 |
| Scheduled tasks 4698 | `%SystemRoot%\System32\Tasks\`, Security log | File copy + SIEM | Scheduled persistence | 🟡 |
| Live C2 connections | EDR / netflow / pcap | Telemetry | Active adversary channel | 🟢 |
| Anomalous new asset on OT net | Nozomi asset inventory delta | Export | Rogue device/foothold | 🟢 |

---

## Using this matrix
1. From your investigative question (Universal SOP Step 2), find the matching section (A–I).
2. Collect the 🟢 sources first — they're safe and often decaying.
3. For 🔴/🟡 OT sources, route through the authority-to-act matrix ([`docs/02-roles-and-raci.md`](../../docs/02-roles-and-raci.md)) — engineer-led, operations-authorized.
4. Hash and custody-log every artifact ([`docs/04-evidence-handling-chain-of-custody.md`](../../docs/04-evidence-handling-chain-of-custody.md)).
5. The strongest proof **corroborates across sections** — e.g. E (command on wire) + F (logic differs) + G (process deviated) is an irrefutable chain.
