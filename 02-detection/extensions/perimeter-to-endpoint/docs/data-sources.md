# Data Sources

Every detection is only as good as its telemetry. This maps each category to the log sources it needs, in both Splunk (CIM data models / sourcetypes) and Microsoft Sentinel (tables).

## Master mapping

| Category | Telemetry needed | Splunk (CIM / sourcetype) | Sentinel table |
|----------|------------------|---------------------------|----------------|
| 01 Network / DoS | firewall, flow/NetFlow, load-balancer, IDS | `Network_Traffic`, `Intrusion_Detection`; `pan:traffic`, netflow | `CommonSecurityLog`, `AzureDiagnostics` (NSG/FW), `AzureNetworkAnalytics_CL` |
| 02 Identity | AD/Windows auth, Entra ID sign-ins, VPN, MFA | `Authentication`; `WinEventLog:Security` (4624/4625/4740…) | `SecurityEvent`, `SigninLogs`, `AADNonInteractiveUserSignInLogs`, `AuditLogs` |
| 03 Endpoint | Windows Security/Sysmon, EDR (MDE/CrowdStrike) | `Endpoint` (Processes/Registry/Services); `WinEventLog`, `Sysmon` | `DeviceProcessEvents`, `DeviceNetworkEvents`, `DeviceRegistryEvents`, `SecurityEvent` |
| 04 East-west | internal flow, AD auth, SMB/RDP/WMI logs | `Network_Traffic`, `Authentication`; Sysmon 3 | `DeviceNetworkEvents`, `SecurityEvent`, `CommonSecurityLog` |
| 05 Outliers / DNS | DNS query logs, flow, proxy | `Network_Resolution` (DNS); `Web`, netflow | `DnsEvents`, `DeviceNetworkEvents`, `CommonSecurityLog` |
| 06 Scanning / webapp | firewall/flow, WAF, IIS/web server, proxy | `Network_Traffic`, `Web`; `iis`, `apache` | `CommonSecurityLog` (WAF), `W3CIISLog`, `AzureDiagnostics` (AppGW) |
| 07 Prohibited | firewall, proxy, DNS, threat intel | `Network_Traffic`, `Web`, `Network_Resolution` + threat-intel lookup | `CommonSecurityLog`, `DnsEvents`, `ThreatIntelligenceIndicator` |

## Enabling notes (common gaps)
- **Process command line** (Windows 4688) and **PowerShell script-block** (4104) logging must be explicitly enabled — many endpoint detections are blind without them. Sysmon dramatically improves 03/04 coverage.
- **DNS query logging** is often not collected; without it, 05's tunnelling/DGA detections can't run. MDE `DeviceNetworkEvents` or dedicated DNS logs both work.
- **Non-interactive sign-ins** (`AADNonInteractiveUserSignInLogs`) carry most spray/token activity — collect them, not just interactive `SigninLogs`.
- **Flow vs full logs.** Volumetric/DoS and outlier detections run on flow/NetFlow (cheap, broad); signature detections need fuller logs.
- **Threat-intel feed** must be wired into a lookup (Splunk) or `ThreatIntelligenceIndicator` (Sentinel) for category 07 IOC matching.

## ATT&CK data-source alignment
Network Traffic (flow/content/connection), Logon Session, User Account, Command, Process, Application Log, DNS — the standard enterprise ATT&CK data components. This library assumes a normalized pipeline into one SIEM; where you have an EDR, prefer its telemetry for 03/04 over raw Windows logs.
