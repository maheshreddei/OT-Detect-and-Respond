# VNC (Remote Framebuffer / RFB)

## Snapshot
| Property | Value |
|----------|-------|
| Port/transport | TCP/5900+ (5900+display) |
| Purdue | L2–L3 (EWS/HMI); vendor access |
| Auth | Often weak (short VNC password) or none; frequently unencrypted |
| Telemetry | Zeek `conn.log`, host logs (VNC server), NDR, firewall |

## What it is
VNC/RFB gives graphical remote-desktop access to a host's screen, keyboard, and mouse. In OT it's a common way to reach an **engineering workstation or HMI** — for vendor support or operator convenience — which makes it a direct path to hands-on-keyboard control.

## What it really means for a defender
A VNC session to an EWS/HMI is **interactive control of an engineering host** — from there an attacker uses the *legitimate* engineering software to program controllers, so subsequent malicious actions can look like normal engineering. VNC deployments in OT are notoriously weak: short passwords, no MFA, cleartext, exposed to too-broad a network. A VNC connection to a control host from an unexpected source is one of the highest-value pivots to catch — and once inside, detection shifts to the *host* (what the interactive session did).

## Attacker actions (recon → impact)
- **Discover:** find open 5900+ services (see scanning page).
- **Access:** connect, authenticate (weak/blank VNC password) or exploit an unauthenticated server.
- **Impact:** drive the desktop — launch engineering software, open/modify/download PLC projects, change HMI config. The protocol just carries screen+input; the damage happens in the apps.

## Detections you can build
| Detection | Signal / logic | Log source | ATT&CK ICS |
|-----------|----------------|------------|------------|
| VNC to a control host | Session to an EWS/HMI/PLC from any source | `conn.log`/NDR + asset context | T0822 External Remote Services |
| VNC from unexpected source | New/first-time source→EWS VNC pair, or off-hours | NDR + baseline | T0822, T0859 |
| VNC auth activity | Repeated RFB auth attempts / failures | VNC server log, `conn.log` | T1110* |
| Post-session engineering activity | After a VNC session: engineering-tool launch, project change, program download on that host | host Sysmon/EDR + S7/ENIP network | T0843 Program Download |
| Cross-zone VNC | VNC crossing an IT→OT boundary | firewall | T0822 |

## Log sources & telemetry
Network: Zeek `conn.log` / NDR identify the session, source, duration, and target asset. **Host is where the impact is** — Windows logon (type 10/RemoteInteractive), Sysmon process/creation, and engineering-tool logs on the EWS reveal what the session did. Correlate the two.

## Functions/services to watch
RFB handshake and authentication; session establishment to control-host assets; the *host-side* activity that follows (this is the real detection surface once access succeeds).

## ATT&CK mapping
T0822 External Remote Services · T0859 Valid Accounts · T0843 Program Download / T0873 Project File Infection (post-access) · T0831 Manipulation of Control.
