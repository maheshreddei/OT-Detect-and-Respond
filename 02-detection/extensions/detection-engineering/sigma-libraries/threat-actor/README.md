# OT Threat-Actor - Sigma Use Case Library

Threat-actor-aligned detections covering Sandworm, APT34, CHERNOVITE/PIPEDREAM and XENOTIME/TRITON TTPs.

**20 Sigma rules** - each as an individual file under [`rules/`](rules/). Original authored deliverable preserved at [`source/OT_Threat_Actor_Sigma_Use_Case_Library.docx`](source/OT_Threat_Actor_Sigma_Use_Case_Library.docx).

> Field names follow Zeek ICSNPP parser output and Nozomi Guardian/Vantage export conventions (`proto`, `function_code`, `src_ip`, `node_id`, `type_id`, ...). Map them to your SIEM's parsed field names, and replace placeholder subnets/allow-lists, before enabling in production.

## Rule index

| # | Title | Threat Actor | ATT&CK | Level |
|---|---|---|---|---|
| 1 | IEC 104 Mass Coordinated Breaker-Open Command Burst | Sandworm / APT44 (Electrum) | attack.ics.t0855, attack.ics.t0831, attack.ics.t0879 | CRITICAL |
| 2 | Modbus Holding Register Manipulation at Abnormal Cadence | Sandworm / APT44 (assessed) | attack.ics.t0855, attack.ics.t0836 | HIGH |
| 3 | Mass Disk-Wiping Utility Execution Across Multiple Hosts | Sandworm / APT44 | attack.t1490, attack.t1561, attack.ics.t0826 | CRITICAL |
| 4 | IEC 61850 GOOSE Unauthorized Publisher or Spoofed Message | Sandworm / APT44 (Electrum) | attack.ics.t0855, attack.ics.t0856 | CRITICAL |
| 5 | Mass Lateral Deployment Tooling Preceding Suspected Wiper Activity | Sandworm / APT44 | attack.t1570, attack.t1047, attack.ics.t0867 | HIGH |
| 6 | DNS Tunneling Beacon From OT DMZ or Engineering Host | APT34 / OilRig (Helix Kitten) | attack.t1071.004, attack.t1568 | HIGH |
| 7 | Web Shell Activity on Internet-Facing OT-Adjacent Server | APT34 / OilRig (Crambus) | attack.t1505.003, attack.t1190 | CRITICAL |
| 8 | Credential Harvesting Tool Execution on Engineering or SCADA Host | APT34 / OilRig | attack.t1003.001, attack.t1003.002, attack.ics.t0859 | CRITICAL |
| 9 | Low-and-Slow HTTPS Beaconing Indicative of OilRig-Class Backdoor C2 | APT34 / OilRig | attack.t1071.001, attack.t1102 | MEDIUM |
| 10 | Shamoon-Style MBR Wiper Execution | APT33 / Elfin (Refined Kitten) | attack.t1561.002, attack.t1529, attack.ics.t0826 | CRITICAL |
| 11 | Password Spray Against OT Remote Access Portal | APT33 / Elfin | attack.t1110.003, attack.t1133 | HIGH |
| 12 | Mass Malware Spreader Tool Execution Across Multiple Hosts | APT33 / Elfin | attack.t1570, attack.t1021.002 | CRITICAL |
| 13 | OPC UA Server Enumeration Followed by Node Value Tampering | CHERNOVITE (PIPEDREAM / INCONTROLLER) | attack.ics.t0846, attack.ics.t0856 | HIGH |
| 14 | CODESYS Protocol Command to Schneider Controller From Non-Engineering Host | CHERNOVITE (PIPEDREAM / INCONTROLLER) | attack.ics.t0859, attack.ics.t0843, attack.ics.t0814 | CRITICAL |
| 15 | OMRON FINS/HTTP Backdoor Command Execution | CHERNOVITE (PIPEDREAM / INCONTROLLER) | attack.ics.t0859, attack.ics.t0883 | HIGH |
| 16 | ASRock RGB Driver Exploitation Attempt (CVE-2020-15368) | CHERNOVITE (PIPEDREAM / INCONTROLLER) | attack.t1068, attack.t1562.001 | CRITICAL |
| 17 | Triconex Safety Controller Engineering Session From Unauthorized Host | XENOTIME (TRITON / TRISIS) | attack.ics.t0859, attack.ics.t0800, attack.ics.t0837 | CRITICAL |
| 18 | Safety Controller Key-Switch or Mode Change Outside Proof-Test Window | XENOTIME (TRITON / TRISIS) | attack.ics.t0858, attack.ics.t0800 | CRITICAL |
| 19 | Engineering Workstation Reflective/Memory-Only Process Injection | Generalized (Stuxnet-class TTP) | attack.t1055, attack.ics.t0851 | HIGH |
| 20 | Mass File Encryption or Rename Activity on OT Historian or Engineering Host | Generalized (Ransomware precursor to OT shutdown) | attack.t1486, attack.ics.t0826 | CRITICAL |

## Files

- `01_iec-104-mass-coordinated-breaker-open-command-burst.yml` - IEC 104 Mass Coordinated Breaker-Open Command Burst
- `02_modbus-holding-register-manipulation-at-abnormal-cadence.yml` - Modbus Holding Register Manipulation at Abnormal Cadence
- `03_mass-disk-wiping-utility-execution-across-multiple-hosts.yml` - Mass Disk-Wiping Utility Execution Across Multiple Hosts
- `04_iec-61850-goose-unauthorized-publisher-or-spoofed-message.yml` - IEC 61850 GOOSE Unauthorized Publisher or Spoofed Message
- `05_mass-lateral-deployment-tooling-preceding-suspected-wiper-ac.yml` - Mass Lateral Deployment Tooling Preceding Suspected Wiper Activity
- `06_dns-tunneling-beacon-from-ot-dmz-or-engineering-host.yml` - DNS Tunneling Beacon From OT DMZ or Engineering Host
- `07_web-shell-activity-on-internet-facing-ot-adjacent-server.yml` - Web Shell Activity on Internet-Facing OT-Adjacent Server
- `08_credential-harvesting-tool-execution-on-engineering-or-scada.yml` - Credential Harvesting Tool Execution on Engineering or SCADA Host
- `09_low-and-slow-https-beaconing-indicative-of-oilrig-class-back.yml` - Low-and-Slow HTTPS Beaconing Indicative of OilRig-Class Backdoor C2
- `10_shamoon-style-mbr-wiper-execution.yml` - Shamoon-Style MBR Wiper Execution
- `11_password-spray-against-ot-remote-access-portal.yml` - Password Spray Against OT Remote Access Portal
- `12_mass-malware-spreader-tool-execution-across-multiple-hosts.yml` - Mass Malware Spreader Tool Execution Across Multiple Hosts
- `13_opc-ua-server-enumeration-followed-by-node-value-tampering.yml` - OPC UA Server Enumeration Followed by Node Value Tampering
- `14_codesys-protocol-command-to-schneider-controller-from-non-en.yml` - CODESYS Protocol Command to Schneider Controller From Non-Engineering Host
- `15_omron-fins-http-backdoor-command-execution.yml` - OMRON FINS/HTTP Backdoor Command Execution
- `16_asrock-rgb-driver-exploitation-attempt-cve-2020-15368.yml` - ASRock RGB Driver Exploitation Attempt (CVE-2020-15368)
- `17_triconex-safety-controller-engineering-session-from-unauthor.yml` - Triconex Safety Controller Engineering Session From Unauthorized Host
- `18_safety-controller-key-switch-or-mode-change-outside-proof-te.yml` - Safety Controller Key-Switch or Mode Change Outside Proof-Test Window
- `19_engineering-workstation-reflective-memory-only-process-injec.yml` - Engineering Workstation Reflective/Memory-Only Process Injection
- `20_mass-file-encryption-or-rename-activity-on-ot-historian-or-e.yml` - Mass File Encryption or Rename Activity on OT Historian or Engineering Host

