# FTP

## Snapshot
| Property | Value |
|----------|-------|
| Port/transport | TCP/21 (control), 20/passive (data) |
| Purdue | L2–L3; embedded FTP on devices down to L1 |
| Auth | Cleartext; anonymous access common; no encryption |
| Telemetry | Zeek `ftp.log`, FTP server logs, NDR, firewall |

## What it is
FTP moves files to and from hosts and devices. In OT it shows up on PLCs, RTUs, gateways, and historians — used for **firmware, configuration, project files, and logic** transfer. Credentials and data are cleartext, and anonymous access is frequently left enabled.

## What it really means for a defender
FTP to a control device is a **firmware/logic delivery channel**. An attacker who can write files via FTP may be able to stage or replace firmware, configuration, or logic — a direct route to persistence or process manipulation — and reads can exfiltrate project files that reveal the whole control design. Because it's cleartext, credentials are also harvestable by anyone on-path. Anonymous-writable FTP on an OT device is close to a standing backdoor.

## Attacker actions (recon → impact)
- **Banner grab:** identify the FTP server/device from the greeting.
- **Anonymous check:** test `anonymous` login for read/write.
- **Brute force:** guess credentials (cleartext, usually no lockout).
- **Impact:** download project/config files (recon/exfil); upload firmware/logic/config (staging, persistence, manipulation).

## Detections you can build
| Detection | Signal / logic | Log source | ATT&CK ICS |
|-----------|----------------|------------|------------|
| Anonymous FTP login to OT device | `USER anonymous` accepted on an OT asset | `ftp.log`, server log | T0822 External Remote Services |
| FTP brute force | Many failed logins then success from one source | `ftp.log`, server log | T1110*, T0859 |
| Upload to a control device | `STOR`/`PUT` to a PLC/RTU/gateway | `ftp.log` | T0839 Module Firmware, T0843 Program Download |
| Firmware/project file transfer | Transfer of firmware/project extensions to/from OT | `ftp.log` + filename | T0839, T0873 Project File Infection |
| New FTP client to OT asset | First-time source→OT FTP pair | NDR + baseline | T0822 |
| Cross-zone FTP | FTP crossing IT→OT boundary | firewall | T0822 |

## Log sources & telemetry
Zeek `ftp.log` captures commands (USER/PASS/STOR/RETR), args (filenames), and reply codes — enough to see anonymous logins, brute force, and uploads. The **device/server FTP log** adds detail. NDR flags new pairs and cross-zone transfers; firewall logs catch boundary crossings.

## Functions/services to watch
`USER`/`PASS` (auth, anonymous), `STOR`/`STOU`/`APPE` (writes = staging), `RETR` (reads = exfil), filenames with firmware/project/config extensions; reply-code patterns (530 failures → 230 success = brute force).

## ATT&CK mapping
T0822 External Remote Services · T0859 Valid Accounts · T0839 Module Firmware · T0843 Program Download · T0873 Project File Infection.

> *T1110 is ATT&CK Enterprise (Brute Force); shown where the technique originates on IT-side services.*
