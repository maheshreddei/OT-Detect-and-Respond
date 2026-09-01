# Evidence: Windows Hosts (EWS / HMI / Historian)

The Windows assets in OT — engineering workstations, HMIs, historian servers, jump hosts — hold the richest host-side evidence. The **engineering workstation (EWS) is the crown jewel**: it runs the software that can program controllers, so proving what happened on it often proves the whole incident.

> **OT caution:** many of these hosts are fragile, legacy, or actively driving a process. Prefer **EDR/agent telemetry** and **targeted triage collection** over full disk/memory imaging on a live HMI. Coordinate any acquisition with operations. Never run untested tools against a host mid-process without sign-off.

## Windows Event Logs — the backbone

Location: `%SystemRoot%\System32\winevt\Logs\*.evtx`
Collect: `wevtutil epl <Channel> <out>.evtx`, EDR export, or a triage collector (KAPE-style). Hash on collection.

| What you're proving | Event IDs | Channel |
|---------------------|-----------|---------|
| Logon success/failure/logoff | 4624 / 4625 / 4634 / 4647 | Security |
| Logon type & source IP | 4624 (LogonType, IpAddress) | Security |
| Special/admin privileges | 4672 | Security |
| Account created / enabled | 4720 / 4722 | Security |
| Added to privileged group | 4728 / 4732 / 4756 | Security |
| Process creation (+ cmdline*) | 4688 | Security |
| Service installed | 7045 | System |
| Scheduled task created | 4698 | Security |
| Log cleared (anti-forensics) | 1102 | Security |
| RDP session reconnect | 1149 | TerminalServices-RemoteConnectionManager |
| PowerShell script block | 4104 / 4103 | PowerShell/Operational |
| WMI activity | 5857-5861 | WMI-Activity/Operational |

\*Command-line logging (4688) and PowerShell script-block logging must be enabled beforehand — a Prepare-phase item. If absent, note the gap.

## Sysmon (if deployed)
`Microsoft-Windows-Sysmon/Operational`. High-value components: process creation (1) with hashes, network connection (3), image load (7), file create (11), registry (12/13), WMI (19-21). Sysmon is the single best host telemetry to have pre-deployed on OT Windows assets.

## Execution artifacts (prove a program ran, even if deleted)
| Artifact | Location | Proves |
|----------|----------|--------|
| Prefetch | `%SystemRoot%\Prefetch\*.pf` | Executed program, first/last run, run count |
| Amcache | `%SystemRoot%\AppCompat\Programs\Amcache.hve` | Presence/execution + SHA1 of binaries |
| Shimcache | `SYSTEM` hive → AppCompatCache | Executables present/run |
| UserAssist | `NTUSER.DAT` | GUI programs a user launched |
| BAM/DAM | `SYSTEM` hive | Background/foreground app execution with timestamps |
| SRUM | `%SystemRoot%\System32\sru\SRUDB.dat` | Per-app network/resource use over time |

## Registry hives
Collect: `SYSTEM`, `SOFTWARE`, `SECURITY`, `SAM` (`%SystemRoot%\System32\config\`), and per-user `NTUSER.DAT`, `UsrClass.dat`.
| Prove | Key |
|-------|-----|
| Autostart persistence | `...\CurrentVersion\Run` / `RunOnce` (SOFTWARE + NTUSER) |
| Services | `SYSTEM\CurrentControlSet\Services` |
| USB device history | `SYSTEM\...\USBSTOR`, `SOFTWARE\...\Windows Portable Devices` |
| RDP destinations | `NTUSER\...\Terminal Server Client\Servers` |
| Network profiles | `SOFTWARE\...\NetworkList\Profiles` |

## Filesystem timeline
- `$MFT`, `$LogFile`, `$UsnJrnl:$J` from the NTFS volume → file create/rename/delete timeline (detects timestomping via $STANDARD_INFO vs $FILE_NAME).
- Collect via triage tool or forensic image. Build a super-timeline (plaso/log2timeline) correlating all host artifacts.

## Engineering & HMI software artifacts (OT-specific, high value)
Prove that control-engineering software ran and whether a project was opened/modified/downloaded:

| Vendor / tool | Project & log locations (typical) | Proves |
|---------------|-----------------------------------|--------|
| Siemens TIA Portal / STEP 7 | `.ap##`/`.s7p` project dirs; TIA logs under user profile | Project opened/edited; download prepared |
| Rockwell Studio 5000 / RSLogix | `.ACD`/`.RSS` project files; FactoryTalk Diagnostics logs | Logic project changes; who/when |
| Siemens PCS7 / WinCC | Project dirs; WinCC audit logs (if licensed) | HMI/DCS config & operator actions |
| Schneider EcoStruxure / Unity | `.STU`/`.XEF` projects | Controller project changes |
| Emerson DeltaV / AVEVA / Wonderware | DeltaV audit trail; historian host logs | Config changes, operator actions |

Collect the project file (hash it), its last-modified time, and any application/audit log the tool keeps. Compare project timestamps against logon and network-transfer timelines.

## USB & removable media
USBSTOR registry + `setupapi.dev.log` (`%SystemRoot%\inf\`) → device first-connect times, serials. A common OT air-gap-crossing vector; prove whether removable media was introduced around the incident window.

## Memory (if the host tolerates it)
Live RAM capture (WinPMEM/DumpIt/Magnet) yields running processes, injected code, network state, and credentials. **On OT: only with sign-off, and never on a fragile HMI mid-process.** Prefer EDR memory telemetry. If captured, hash immediately and analyze the copy (Volatility).

## Minimum triage collection (fast, low-risk)
If you can only grab a little before the host must keep running: **Security.evtx + Sysmon + PowerShell logs + Prefetch + Amcache/Shimcache + relevant registry hives + $MFT**. A triage collector bundles these in minutes without a full image.
