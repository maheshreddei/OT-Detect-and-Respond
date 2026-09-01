# How to Use This Guide

Turning these pages into deployed detections.

## The workflow
1. **Baseline first.** For each OT protocol in your environment, record the legitimate client↔server pairs (which engineering stations, HMIs, SCADA masters speak it to which devices) and the normal function/service set and polling cadence. Most detections here fire on deviations from that baseline, so the baseline is the prerequisite.
2. **Pick the reusable patterns.** Almost every detection is one of five patterns (unauthorized client, recon, write/command, disruptive function, baseline deviation). Start with **write/command** detections — they're the highest severity and closest to true-positive by construction.
3. **Confirm the log source.** Each detection names its feed. Cross-check against [`log-sources.md`](log-sources.md); if you lack the feed, that's a telemetry gap to close before the detection is real.
4. **Implement in your SIEM/NDR.** Where you run Nozomi/Dragos/Claroty, many of these ship as built-in policies — enable and tune them. Where you run Zeek+ICSNPP into Splunk/Sentinel, the per-protocol log fields tell you what to write SPL/KQL against. (Field names follow ICSNPP/Nozomi conventions — map to your parsed fields.)
5. **Pair writes with impact.** Route every write/command detection to also pull the historian trend/alarm journal for the target, so triage separates a probe from a real process change.
6. **Correlate across layers.** A protocol write (network) + an unexpected source host (identity/host) + a historian deviation (physics) on the same asset is a high-confidence incident. That fusion is the goal.

## Severity guidance
| Pattern | Typical severity |
|---------|------------------|
| Write/command to a control/command point from a non-engineering source | High / Critical |
| Disruptive function (STOP, program download, force) | Critical |
| Cross-zone control protocol (e.g. Modbus from IT) | High |
| Recon / enumeration from an unexpected source | Medium |
| New asset speaking a control protocol | Medium / High |
| IT/access protocol (VNC/FTP/HTTP) reaching a control asset | High |

## What to build first (highest value)
1. **Unauthorized-source write** on your most-used control protocol (Modbus/S7/ENIP/IEC-104/DNP3 — whichever dominates your site).
2. **Disruptive-function** detection (S7 STOP / program download; DNP3 operate; IEC-104 command ASDU).
3. **Cross-zone control traffic** via firewall logs.
4. **New OT asset** via NDR inventory delta.
5. **VNC/FTP to an EWS/PLC** via host + network.

These five cover the bulk of real OT protocol attacks with modest effort.
