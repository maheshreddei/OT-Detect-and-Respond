# Shieldworkz Advisory (Middle East OT TI) - Sigma Use Case Library

Detections derived from Middle East OT threat-intelligence advisories, tuned for regional targeting patterns.

**20 Sigma rules** - each as an individual file under [`02-detection/sigma/advisory`](.). Original authored deliverable preserved at `Shieldworkz_Advisory_Sigma_Use_Case_Library.docx` (original authored deliverable, retained in the source repository; not migrated into this program repo).

> Field names follow Zeek ICSNPP parser output and Nozomi Guardian/Vantage export conventions (`proto`, `function_code`, `src_ip`, `node_id`, `type_id`, ...). Map them to your SIEM's parsed field names, and replace placeholder subnets/allow-lists, before enabling in production.

## Rule index

| # | Title | Source / Actor | ATT&CK | Level |
|---|---|---|---|---|
| 1 | Unitronics Vision PLC Default Port Access (BAUXITE Pattern) | BAUXITE / CyberAv3ngers (IRGC-affiliated) | attack.ics.t0810, attack.ics.t0806 | CRITICAL |
| 2 | HMI Display Screen Defacement or Unauthorized Image/Text Overwrite | BAUXITE / CyberAv3ngers (IRGC-affiliated) | attack.ics.t0831, attack.ics.t0829 | CRITICAL |
| 3 | Post-Unitronics-Compromise Lateral Movement via SMB/RDP From PLC Network Segment | BAUXITE / CyberAv3ngers (IRGC-affiliated) | attack.t1021.001, attack.t1021.002, attack.ics.t0867 | HIGH |
| 4 | Remote Management Tool Installation on OT-Adjacent Host (MuddyWater Pattern) | MuddyWater (Static Kitten / MERCURY) | attack.t1219, attack.ics.t0883 | HIGH |
| 5 | Bulk Exfiltration of OT Documentation and Network Diagrams (Moses Staff Pattern) | Moses Staff / Abraham's Ax | attack.t1560, attack.t1567, attack.ics.t0811 | HIGH |
| 6 | Ransomware Precursor — Lateral Movement Targeting Historian or SCADA Hostnames | RansomHub and OT-Capable Affiliates | attack.t1135, attack.t1018, attack.ics.t0888 | HIGH |
| 7 | Mass File Transfer Appliance Exploitation Preceding OT Document Theft (Cl0p Pattern) | Cl0p and Industrial Data Extortion Groups | attack.t1190, attack.t1505.003 | CRITICAL |
| 8 | Sensor Gateway Mass Filesystem Wipe or RS485/MBus Disruption (Fuxnet Pattern) | Blackjack (Fuxnet) — included for cross-theatre capability awareness | attack.ics.t0826, attack.t1561.002 | CRITICAL |
| 9 | Coordinated Multi-Site SCADA Command Triggering Mass Manual-Fallback (Predatory Sparrow-Class Pattern) | Predatory Sparrow-class capability (calibration reference) | attack.ics.t0855, attack.ics.t0826 | CRITICAL |
| 10 | Password Spray Against Cloud Identity Tenant Serving OT-Adjacent Accounts | APT33 / Elfin (Refined Kitten) | attack.t1110.003, attack.t1078.004 | HIGH |
| 11 | Security Event Log Cleared on OT Network System | Generalized (anti-forensic indicator across multiple actors) | attack.t1070.001, attack.ics.t0851 | CRITICAL |
| 12 | PLC Configuration Drift From Verified Offline Backup | Generalized (integrity-verification hunt, not actor-specific) | attack.ics.t0873, attack.ics.t0839 | CRITICAL |
| 13 | Historian Query Pattern Anomaly From IT-Network Host | Generalized (reconnaissance hunt, not actor-specific) | attack.ics.t0801, attack.ics.t0811 | MEDIUM |
| 14 | Engineering Workstation Outbound Connection to Infrastructure Outside Approved List | Generalized (EWS compromise hunt, not actor-specific) | attack.t1071, attack.ics.t0883 | HIGH |
| 15 | Vendor VPN Authentication Outside Approved Window or Geography | Generalized (vendor access hunt, not actor-specific) | attack.t1078.002, attack.ics.t0883 | MEDIUM |
| 16 | Dormant Vendor Account First-Use After Extended Inactivity | Generalized (credential hygiene gap, not actor-specific) | attack.t1078, attack.ics.t0859 | HIGH |
| 17 | Unauthenticated Modbus/DNP3 Traffic Through Legacy Serial-to-Ethernet Gateway | Generalized (legacy gateway exposure, not actor-specific) | attack.ics.t0846, attack.ics.t0855 | HIGH |
| 18 | Unauthorized Association to Industrial Wireless Network (WirelessHART/ISA100/OT Wi-Fi) | Generalized (wireless exposure, not actor-specific) | attack.ics.t0822, attack.ics.t0846 | HIGH |
| 19 | OT Cloud Agent Unexpected Outbound Data Pathway | Generalized (OT cloud/IIoT governance gap, not actor-specific) | attack.t1071.001, attack.ics.t0846 | MEDIUM |
| 20 | Spearphishing Lure Execution by OT Engineering Personnel | Multiple (APT33, APT34, Moses Staff) | attack.t1566.001, attack.t1204.002 | CRITICAL |

## Files

- `01_unitronics-vision-plc-default-port-access-bauxite-pattern.yml` - Unitronics Vision PLC Default Port Access (BAUXITE Pattern)
- `02_hmi-display-screen-defacement-or-unauthorized-image-text-ove.yml` - HMI Display Screen Defacement or Unauthorized Image/Text Overwrite
- `03_post-unitronics-compromise-lateral-movement-via-smb-rdp-from.yml` - Post-Unitronics-Compromise Lateral Movement via SMB/RDP From PLC Network Segment
- `04_remote-management-tool-installation-on-ot-adjacent-host-mudd.yml` - Remote Management Tool Installation on OT-Adjacent Host (MuddyWater Pattern)
- `05_bulk-exfiltration-of-ot-documentation-and-network-diagrams-m.yml` - Bulk Exfiltration of OT Documentation and Network Diagrams (Moses Staff Pattern)
- `06_ransomware-precursor-lateral-movement-targeting-historian-or.yml` - Ransomware Precursor — Lateral Movement Targeting Historian or SCADA Hostnames
- `07_mass-file-transfer-appliance-exploitation-preceding-ot-docum.yml` - Mass File Transfer Appliance Exploitation Preceding OT Document Theft (Cl0p Pattern)
- `08_sensor-gateway-mass-filesystem-wipe-or-rs485-mbus-disruption.yml` - Sensor Gateway Mass Filesystem Wipe or RS485/MBus Disruption (Fuxnet Pattern)
- `09_coordinated-multi-site-scada-command-triggering-mass-manual.yml` - Coordinated Multi-Site SCADA Command Triggering Mass Manual-Fallback (Predatory Sparrow-Class Pattern)
- `10_password-spray-against-cloud-identity-tenant-serving-ot-adja.yml` - Password Spray Against Cloud Identity Tenant Serving OT-Adjacent Accounts
- `11_security-event-log-cleared-on-ot-network-system.yml` - Security Event Log Cleared on OT Network System
- `12_plc-configuration-drift-from-verified-offline-backup.yml` - PLC Configuration Drift From Verified Offline Backup
- `13_historian-query-pattern-anomaly-from-it-network-host.yml` - Historian Query Pattern Anomaly From IT-Network Host
- `14_engineering-workstation-outbound-connection-to-infrastructur.yml` - Engineering Workstation Outbound Connection to Infrastructure Outside Approved List
- `15_vendor-vpn-authentication-outside-approved-window-or-geograp.yml` - Vendor VPN Authentication Outside Approved Window or Geography
- `16_dormant-vendor-account-first-use-after-extended-inactivity.yml` - Dormant Vendor Account First-Use After Extended Inactivity
- `17_unauthenticated-modbus-dnp3-traffic-through-legacy-serial-to.yml` - Unauthenticated Modbus/DNP3 Traffic Through Legacy Serial-to-Ethernet Gateway
- `18_unauthorized-association-to-industrial-wireless-network-wire.yml` - Unauthorized Association to Industrial Wireless Network (WirelessHART/ISA100/OT Wi-Fi)
- `19_ot-cloud-agent-unexpected-outbound-data-pathway.yml` - OT Cloud Agent Unexpected Outbound Data Pathway
- `20_spearphishing-lure-execution-by-ot-engineering-personnel.yml` - Spearphishing Lure Execution by OT Engineering Personnel

