# HTTP

## Snapshot
| Property | Value |
|----------|-------|
| Port/transport | TCP/80, 443 (and device-specific, e.g. OpenPLC on 8080) |
| Purdue | L2–L3, DMZ; embedded web UIs down to L1 |
| Auth | Application-dependent; frequently weak/default on OT web UIs |
| Telemetry | Zeek `http.log`/`ssl.log`, web-app logs, WAF, NDR |

## What it is
HTTP(S) fronts the web management UIs of OT gear and software — PLC web servers (e.g. OpenPLC), HMIs, historians, gateways, network devices. It's often the softest way into a device because the web layer bolts weak auth onto a control asset.

## What it really means for a defender
OT web UIs are frequently shipped with **default credentials, no lockout, and no MFA**, and they expose control functions (start/stop, config, logic upload) behind a login. So the web layer is where **credential brute force and directory enumeration** pay off — and a successful login can equal process control. Treat any OT device web UI as a high-value target and watch its access logs like you'd watch a DC.

## Attacker actions (recon → impact)
- **Fingerprint:** identify the device/app and version from headers, titles, favicons, default pages.
- **Enumerate:** directory/endpoint brute force to find admin panels, APIs, config pages.
- **Brute force:** password-guess the login (e.g. OpenPLC admin).
- **Impact:** authenticated abuse of control functions (upload logic, change config, start/stop).

## Detections you can build
| Detection | Signal / logic | Log source | ATT&CK ICS |
|-----------|----------------|------------|------------|
| Web login brute force | Many auth failures then a success from one source to an OT UI | web-app log, `http.log` | T0859 Valid Accounts, T1110* |
| Directory/endpoint enumeration | Burst of 404s / many distinct paths from one source | `http.log`, WAF | T0846 |
| Default-page / fingerprint access | Requests to known device default/admin paths from unexpected source | `http.log` | T0846 |
| New client to device web UI | First-time source→OT-web-UI pair | NDR + baseline | T0822 External Remote Services |
| Post-login control action | Config/upload/start-stop endpoints hit after login | web-app log | T0831 Manipulation of Control |

## Log sources & telemetry
The **web application's own access/auth logs** are richest (status codes, paths, usernames). Zeek `http.log` gives host/URI/status/user-agent across the wire; `ssl.log` for TLS metadata when encrypted. NDR flags new client↔UI pairs.

## Functions/services to watch
Auth endpoints (login/session), admin/config/upload paths, API endpoints that change device state; 401/403/404 patterns; user-agent anomalies (scripts vs browsers).

## ATT&CK mapping
T0822 External Remote Services · T0859 Valid Accounts · T0846 Remote System Discovery · T0831 Manipulation of Control (post-auth).
