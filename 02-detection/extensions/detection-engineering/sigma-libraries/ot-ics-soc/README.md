# OT/ICS SOC Protocol - Sigma Use Case Library

Protocol-level detections for Modbus, DNP3, OPC UA, S7comm and IEC 60870-5-104, authored against Zeek ICSNPP /  Guardian export fields.

**20 Sigma rules** - each as an individual file under [`rules/`](rules/). Original authored deliverable preserved at [`source/OT_ICS_SOC_Sigma_Use_Case_Library.docx`](source/OT_ICS_SOC_Sigma_Use_Case_Library.docx).

> Field names follow Zeek ICSNPP parser output and  Guardian/Vantage export conventions (`proto`, `function_code`, `src_ip`, `node_id`, `type_id`, ...). Map them to your SIEM's parsed field names, and replace placeholder subnets/allow-lists, before enabling in production.

## Rule index

| # | Title | Protocol | ATT&CK ICS | Level |
|---|---|---|---|---|
| 1 | Modbus Write Operation from Unauthorized Source | modbus | attack.ics.t0855, attack.ics.t0836 | HIGH |
| 2 | Modbus Diagnostic Restart Communications Function Code | modbus | attack.ics.t0816, attack.ics.t0814 | HIGH |
| 3 | Modbus Exception Response Flood (Possible Scanning or Fuzzing) | modbus | attack.ics.t0846, attack.ics.t0888 | MEDIUM |
| 4 | Modbus Write to Coil/Register Outside Approved Change Window | modbus | attack.ics.t0855, attack.ics.t0831 | MEDIUM |
| 5 | DNP3 Cold or Warm Restart Command Issued | dnp3 | attack.ics.t0816, attack.ics.t0814 | CRITICAL |
| 6 | DNP3 Disable Unsolicited Responses Command | dnp3 | attack.ics.t0804, attack.ics.t0814 | HIGH |
| 7 | DNP3 Direct Operate Without Preceding Select (Bypass of Select-Before-Operate) | dnp3 | attack.ics.t0855, attack.ics.t0858 | HIGH |
| 8 | DNP3 CROB Control Command Outside Maintenance Window | dnp3 | attack.ics.t0855 | MEDIUM |
| 9 | OPC UA Session Established with Anonymous Authentication | opcua | attack.ics.t0859, attack.ics.t0883 | HIGH |
| 10 | OPC UA Untrusted or Self-Signed Certificate Accepted | opcua | attack.ics.t0859, attack.ics.t0822 | HIGH |
| 11 | OPC UA Write Request to Critical Node from Unauthorized Client | opcua | attack.ics.t0855, attack.ics.t0836 | HIGH |
| 12 | OPC UA Address Space Browse Flood (Reconnaissance) | opcua | attack.ics.t0846, attack.ics.t0888 | MEDIUM |
| 13 | S7comm PLC STOP Command Issued | s7comm | attack.ics.t0816, attack.ics.t0858 | CRITICAL |
| 14 | S7comm Program Block Download/Upload Outside Change Window | s7comm | attack.ics.t0843, attack.ics.t0871 | HIGH |
| 15 | S7comm System Status List (SZL) Enumeration | s7comm | attack.ics.t0888, attack.ics.t0846 | MEDIUM |
| 16 | IEC 60870-5-104 General Interrogation from Unauthorized Master | iec104 | attack.ics.t0846, attack.ics.t0888 | HIGH |
| 17 | IEC 60870-5-104 Single or Double Command Outside Maintenance Window | iec104 | attack.ics.t0855 | MEDIUM |
| 18 | IEC 60870-5-104 Clock Synchronization Command Anomaly | iec104 | attack.ics.t0804, attack.ics.t0851 | LOW |
| 19 | Engineering Workstation Communicating with Multiple PLCs Across Zones | generic | attack.ics.t0867, attack.ics.t0843 | HIGH |
| 20 | New or Unauthorized Asset Communicating on OT Engineering Protocol Port | generic | attack.ics.t0883, attack.ics.t0846 | MEDIUM |

## Files

- `01_modbus-write-operation-from-unauthorized-source.yml` - Modbus Write Operation from Unauthorized Source
- `02_modbus-diagnostic-restart-communications-function-code.yml` - Modbus Diagnostic Restart Communications Function Code
- `03_modbus-exception-response-flood-possible-scanning-or-fuzzing.yml` - Modbus Exception Response Flood (Possible Scanning or Fuzzing)
- `04_modbus-write-to-coil-register-outside-approved-change-window.yml` - Modbus Write to Coil/Register Outside Approved Change Window
- `05_dnp3-cold-or-warm-restart-command-issued.yml` - DNP3 Cold or Warm Restart Command Issued
- `06_dnp3-disable-unsolicited-responses-command.yml` - DNP3 Disable Unsolicited Responses Command
- `07_dnp3-direct-operate-without-preceding-select-bypass-of-selec.yml` - DNP3 Direct Operate Without Preceding Select (Bypass of Select-Before-Operate)
- `08_dnp3-crob-control-command-outside-maintenance-window.yml` - DNP3 CROB Control Command Outside Maintenance Window
- `09_opc-ua-session-established-with-anonymous-authentication.yml` - OPC UA Session Established with Anonymous Authentication
- `10_opc-ua-untrusted-or-self-signed-certificate-accepted.yml` - OPC UA Untrusted or Self-Signed Certificate Accepted
- `11_opc-ua-write-request-to-critical-node-from-unauthorized-clie.yml` - OPC UA Write Request to Critical Node from Unauthorized Client
- `12_opc-ua-address-space-browse-flood-reconnaissance.yml` - OPC UA Address Space Browse Flood (Reconnaissance)
- `13_s7comm-plc-stop-command-issued.yml` - S7comm PLC STOP Command Issued
- `14_s7comm-program-block-download-upload-outside-change-window.yml` - S7comm Program Block Download/Upload Outside Change Window
- `15_s7comm-system-status-list-szl-enumeration.yml` - S7comm System Status List (SZL) Enumeration
- `16_iec-60870-5-104-general-interrogation-from-unauthorized-mast.yml` - IEC 60870-5-104 General Interrogation from Unauthorized Master
- `17_iec-60870-5-104-single-or-double-command-outside-maintenance.yml` - IEC 60870-5-104 Single or Double Command Outside Maintenance Window
- `18_iec-60870-5-104-clock-synchronization-command-anomaly.yml` - IEC 60870-5-104 Clock Synchronization Command Anomaly
- `19_engineering-workstation-communicating-with-multiple-plcs-acr.yml` - Engineering Workstation Communicating with Multiple PLCs Across Zones
- `20_new-or-unauthorized-asset-communicating-on-ot-engineering-pr.yml` - New or Unauthorized Asset Communicating on OT Engineering Protocol Port

