# IT / DMZ to OT Cross-Zone - Sigma Use Case Library

Cross-zone detections mapped to the Purdue model - lateral movement, pivoting and unauthorized flows across the IT/OT boundary.

**27 Sigma rules** - each as an individual file under [`rules/`](rules/). Original authored deliverable preserved at [`source/IT_DMZ_OT_CrossZone_Sigma_Use_Case_Library.docx`](source/IT_DMZ_OT_CrossZone_Sigma_Use_Case_Library.docx).

> Field names follow Zeek ICSNPP parser output and Nozomi Guardian/Vantage export conventions (`proto`, `function_code`, `src_ip`, `node_id`, `type_id`, ...). Map them to your SIEM's parsed field names, and replace placeholder subnets/allow-lists, before enabling in production.

## Rule index

| # | Title | Zone Boundary | ATT&CK | Level |
|---|---|---|---|---|
| 1 | Direct IT-to-OT-DMZ Connection Bypassing Jump Host | IT (L4/L5) → OT DMZ (L3.5) | attack.ics.t0886, attack.t1021 | HIGH |
| 2 | Unauthorized Lateral-Movement Protocol Entering OT DMZ | IT (L4/L5) → OT DMZ (L3.5) | attack.ics.t0866, attack.t1021.002, attack.t1021.006 | HIGH |
| 3 | OT DMZ Historian Replication Direction Anomaly | IT (L4/L5) → OT DMZ (L3.5) | attack.ics.t0886, attack.ics.t0840 | HIGH |
| 4 | AV/Patch Management Push to DMZ Outside Maintenance Window or Scope | IT (L4/L5) → OT DMZ (L3.5) | attack.t1072, attack.ics.t0843 | MEDIUM |
| 5 | OT DMZ Asset External DNS or NTP Resolution Attempt | IT (L4/L5) → OT DMZ (L3.5) | attack.t1071.004, attack.t1568 | MEDIUM |
| 6 | Web or Email Content Landing on OT DMZ Jump Host | IT (L4/L5) → OT DMZ (L3.5) | attack.t1566, attack.ics.t0817 | CRITICAL |
| 7 | Jump Host Issuing OT Control Protocol Traffic Directly | OT DMZ (L3.5) → Site Operations (L3) | attack.ics.t0867, attack.ics.t0855 | CRITICAL |
| 8 | Remote Access Session into L3 Without Approved Change Window | OT DMZ (L3.5) → Site Operations (L3) | attack.t1133, attack.ics.t0859 | MEDIUM |
| 9 | Shared or Service Account Used From Unusual DMZ Source | OT DMZ (L3.5) → Site Operations (L3) | attack.t1078, attack.ics.t0859 | HIGH |
| 10 | File Transfer From DMZ to L3 With Executable or Engineering Project Extension | OT DMZ (L3.5) → Site Operations (L3) | attack.ics.t0843, attack.t1105 | HIGH |
| 11 | Vendor Remote Access Session Duration or Scope Anomaly | OT DMZ (L3.5) → Site Operations (L3) | attack.t1133, attack.ics.t0883 | MEDIUM |
| 12 | Unscheduled HMI Project or Configuration Deployment | Site Operations (L3) → Supervisory (L2 — HMI/SCADA) | attack.ics.t0831, attack.ics.t0843 | MEDIUM |
| 13 | New or Modified Scheduled Task on HMI or SCADA Server | Site Operations (L3) → Supervisory (L2 — HMI/SCADA) | attack.t1053.005, attack.ics.t0839 | HIGH |
| 14 | Engineering Software Launched by Non-Engineering Account | Site Operations (L3) → Supervisory (L2 — HMI/SCADA) | attack.ics.t0858, attack.t1078 | HIGH |
| 15 | Abnormal Authentication Pattern on SCADA or HMI Server | Site Operations (L3) → Supervisory (L2 — HMI/SCADA) | attack.t1110, attack.ics.t0859 | MEDIUM |
| 16 | Unexpected Outbound Connection from L2 HMI Toward DMZ or IT | Site Operations (L3) → Supervisory (L2 — HMI/SCADA) | attack.ics.t0886, attack.t1041 | HIGH |
| 17 | Control Command From HMI Outside Documented HMI-to-PLC Pairing | Supervisory (L2) → Control (L1 — PLC/RTU) | attack.ics.t0855, attack.ics.t0867 | HIGH |
| 18 | PLC Logic or Firmware Upload From Non-Engineering Host | Supervisory (L2) → Control (L1 — PLC/RTU) | attack.ics.t0843, attack.ics.t0857 | CRITICAL |
| 19 | Engineering Protocol Session Opened by HMI Account | Supervisory (L2) → Control (L1 — PLC/RTU) | attack.ics.t0867, attack.ics.t0858 | HIGH |
| 20 | Safety Instrumented System Point Forced or Overridden | Control (L1) → Field Devices (L0) | attack.ics.t0837, attack.ics.t0800 | CRITICAL |
| 21 | Setpoint Change Exceeding Safe Delta Threshold | Control (L1) → Field Devices (L0) | attack.ics.t0836, attack.ics.t0855 | HIGH |
| 22 | Redundant Sensor Correlation Divergence | Control (L1) → Field Devices (L0) | attack.ics.t0856, attack.ics.t0804 | MEDIUM |
| 23 | First-Time Asset Communication Across a Zone Boundary | Cross-Cutting (All Zone Boundaries) | attack.ics.t0883, attack.ics.t0846 | MEDIUM |
| 24 | Zone Enforcement Firewall Rule Hit-Count Anomaly | Cross-Cutting (All Zone Boundaries) | attack.ics.t0886 | MEDIUM |
| 25 | Removable Media Event on DMZ or L3 Asset | Cross-Cutting (All Zone Boundaries) | attack.ics.t0847, attack.t1091 | HIGH |
| 26 | East-West Traffic Between L1 Controllers Across Process Cells | Cross-Cutting (All Zone Boundaries) | attack.ics.t0867, attack.ics.t0883 | HIGH |
| 27 | NTP or Time Desynchronization Anomaly Across IT-OT Path | Cross-Cutting (All Zone Boundaries) | attack.ics.t0851, attack.ics.t0804 | LOW |

## Files

- `01_direct-it-to-ot-dmz-connection-bypassing-jump-host.yml` - Direct IT-to-OT-DMZ Connection Bypassing Jump Host
- `02_unauthorized-lateral-movement-protocol-entering-ot-dmz.yml` - Unauthorized Lateral-Movement Protocol Entering OT DMZ
- `03_ot-dmz-historian-replication-direction-anomaly.yml` - OT DMZ Historian Replication Direction Anomaly
- `04_av-patch-management-push-to-dmz-outside-maintenance-window-o.yml` - AV/Patch Management Push to DMZ Outside Maintenance Window or Scope
- `05_ot-dmz-asset-external-dns-or-ntp-resolution-attempt.yml` - OT DMZ Asset External DNS or NTP Resolution Attempt
- `06_web-or-email-content-landing-on-ot-dmz-jump-host.yml` - Web or Email Content Landing on OT DMZ Jump Host
- `07_jump-host-issuing-ot-control-protocol-traffic-directly.yml` - Jump Host Issuing OT Control Protocol Traffic Directly
- `08_remote-access-session-into-l3-without-approved-change-window.yml` - Remote Access Session into L3 Without Approved Change Window
- `09_shared-or-service-account-used-from-unusual-dmz-source.yml` - Shared or Service Account Used From Unusual DMZ Source
- `10_file-transfer-from-dmz-to-l3-with-executable-or-engineering.yml` - File Transfer From DMZ to L3 With Executable or Engineering Project Extension
- `11_vendor-remote-access-session-duration-or-scope-anomaly.yml` - Vendor Remote Access Session Duration or Scope Anomaly
- `12_unscheduled-hmi-project-or-configuration-deployment.yml` - Unscheduled HMI Project or Configuration Deployment
- `13_new-or-modified-scheduled-task-on-hmi-or-scada-server.yml` - New or Modified Scheduled Task on HMI or SCADA Server
- `14_engineering-software-launched-by-non-engineering-account.yml` - Engineering Software Launched by Non-Engineering Account
- `15_abnormal-authentication-pattern-on-scada-or-hmi-server.yml` - Abnormal Authentication Pattern on SCADA or HMI Server
- `16_unexpected-outbound-connection-from-l2-hmi-toward-dmz-or-it.yml` - Unexpected Outbound Connection from L2 HMI Toward DMZ or IT
- `17_control-command-from-hmi-outside-documented-hmi-to-plc-pairi.yml` - Control Command From HMI Outside Documented HMI-to-PLC Pairing
- `18_plc-logic-or-firmware-upload-from-non-engineering-host.yml` - PLC Logic or Firmware Upload From Non-Engineering Host
- `19_engineering-protocol-session-opened-by-hmi-account.yml` - Engineering Protocol Session Opened by HMI Account
- `20_safety-instrumented-system-point-forced-or-overridden.yml` - Safety Instrumented System Point Forced or Overridden
- `21_setpoint-change-exceeding-safe-delta-threshold.yml` - Setpoint Change Exceeding Safe Delta Threshold
- `22_redundant-sensor-correlation-divergence.yml` - Redundant Sensor Correlation Divergence
- `23_first-time-asset-communication-across-a-zone-boundary.yml` - First-Time Asset Communication Across a Zone Boundary
- `24_zone-enforcement-firewall-rule-hit-count-anomaly.yml` - Zone Enforcement Firewall Rule Hit-Count Anomaly
- `25_removable-media-event-on-dmz-or-l3-asset.yml` - Removable Media Event on DMZ or L3 Asset
- `26_east-west-traffic-between-l1-controllers-across-process-cell.yml` - East-West Traffic Between L1 Controllers Across Process Cells
- `27_ntp-or-time-desynchronization-anomaly-across-it-ot-path.yml` - NTP or Time Desynchronization Anomaly Across IT-OT Path

