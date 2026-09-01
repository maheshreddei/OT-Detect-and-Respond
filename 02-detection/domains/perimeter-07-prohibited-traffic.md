# 07 — Prohibited Network Traffic

Policy-based detections: traffic that shouldn't exist regardless of anomaly — threat-intel IOC hits, banned services (Tor/P2P/mining), geo-prohibited destinations, and unauthorized cleartext or cloud egress. These are signature/allow-list detections: precise and low-FP once policy is defined.

## Detections

| ID | Detection | Logic | Data source | ATT&CK | Severity |
|----|-----------|-------|-------------|--------|----------|
| PRB-01 | Threat-intel IOC hit | Connection/DNS to a known-bad IP/domain/hash from TI feed | flow/DNS + TI | T1071 | high |
| PRB-02 | Tor usage | Traffic to Tor entry nodes / known Tor ports/fingerprints | flow / proxy | T1090.003 | high |
| PRB-03 | Crypto-mining | Connections to mining pools / Stratum; mining domains | flow / DNS / proxy | T1496 | high |
| PRB-04 | P2P / torrent | BitTorrent/P2P protocol or tracker traffic | flow / IDS | T1048 | medium |
| PRB-05 | Geo-prohibited destination | Traffic to/from embargoed or policy-forbidden countries | flow + geoIP | T1071 | medium |
| PRB-06 | Unauthorized cloud storage | Egress to non-sanctioned file-sharing/cloud (exfil risk) | proxy / DNS | T1567.002 | medium |
| PRB-07 | Prohibited cleartext protocol | Telnet/FTP/HTTP where policy forbids, esp. to sensitive zones | flow | T1071 | medium |
| PRB-08 | Unauthorized remote-access tool | TeamViewer/AnyDesk/ngrok/RMM not sanctioned | proxy / DNS / flow | T1219 | high |
| PRB-09 | Traffic to newly-registered domain | DNS to domains registered very recently | DNS + enrichment | T1071 | medium |

## Worked queries

### PRB-01 — Threat-intel IOC hit

**Sentinel (KQL)** — native TI table join:
```kql
let iocs = ThreatIntelligenceIndicator
    | where ExpirationDateTime > now() and Active == true and isnotempty(NetworkIP)
    | project NetworkIP, ThreatType, Description;
CommonSecurityLog
| where TimeGenerated > ago(1h)
| join kind=inner iocs on $left.DestinationIP == $right.NetworkIP
| project TimeGenerated, SourceIP, DestinationIP, DestinationPort, ThreatType, Description
| sort by TimeGenerated desc
```

**Splunk (SPL)** — TI lookup:
```spl
index=firewall OR index=proxy earliest=-1h
| lookup threat_intel_ip.csv ip as dest_ip OUTPUT threat_type ioc_source
| where isnotnull(threat_type)
| table _time src_ip dest_ip dest_port threat_type ioc_source
| sort - _time
```

### PRB-05 — Geo-prohibited destination

**Splunk (SPL)**:
```spl
index=firewall action=allowed direction=outbound earliest=-1h
| iplocation dest_ip
| search Country IN ("<PROHIBITED_COUNTRY_1>","<PROHIBITED_COUNTRY_2>")
| stats count sum(bytes_out) as bytes_out values(dest_ip) as dests by src_ip Country
| sort - bytes_out
```

**Sentinel (KQL)**:
```kql
CommonSecurityLog
| where TimeGenerated > ago(1h) and DeviceAction in ("allow","allowed")
| extend geo = geo_info_from_ip_address(DestinationIP)
| extend Country = tostring(geo.country)
| where Country in ("<PROHIBITED_COUNTRY_1>","<PROHIBITED_COUNTRY_2>")
| summarize Conns = count(), Bytes = sum(SentBytes) by SourceIP, Country
| sort by Bytes desc
```

### PRB-08 — Unauthorized remote-access tooling (DNS)

**Splunk (SPL)**:
```spl
index=dns
| eval domain=lower(query)
| search domain IN ("*.teamviewer.com","*.anydesk.com","*.ngrok.io","*.ngrok-free.app","*.logmein.com","*.screenconnect.com")
| stats count values(query) as domains by src_ip
| sort - count
```

## Tuning
- These are policy detections — define the allow-list/policy first, then any hit is by definition prohibited (low FP, high confidence).
- Keep TI feeds fresh and scoped (age-out stale IOCs) to avoid PRB-01 noise; prefer high-confidence indicators.
- PRB-06/PRB-08 need a sanctioned-services list — maintain it; the detection is the inverse of that list.
- Geo and NRD (PRB-05/09) require enrichment (geoIP, domain-age) wired into the pipeline.
