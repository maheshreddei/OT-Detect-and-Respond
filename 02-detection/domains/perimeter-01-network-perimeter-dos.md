# 01 — Network: Perimeter, Baseline & DoS/DDoS

The internet edge. These detect volumetric abuse (DoS/DDoS), baseline traffic deviations, and perimeter policy anomalies. Most run on firewall + flow telemetry, so they scale across breadth without full packet logs.

## Detections

| ID | Detection | Logic | Data source | ATT&CK | Severity |
|----|-----------|-------|-------------|--------|----------|
| NET-01 | Ingress/egress volume baseline deviation | Per-interface/service byte or connection rate exceeds baseline (p95/mean+Nσ) for the time-of-day | firewall/flow | T1498 | medium |
| NET-02 | SYN flood | High rate of SYN with low completed-handshake ratio to a dest | firewall/flow (TCP state) | T1498.001 | high |
| NET-03 | UDP / amplification flood | Spike of UDP to/from amplification ports (53,123,1900,11211) or large-response ratio | flow | T1498.002 | high |
| NET-04 | Connection-rate spike to a service | Connections/sec to one dest:port far above baseline | firewall/flow | T1498 | high |
| NET-05 | Source fan-in (DDoS) | Unusually many distinct source IPs → one destination in a short window | firewall/flow | T1498 | high |
| NET-06 | ICMP flood | ICMP packet/byte rate spike to/from a host | flow | T1498 | medium |
| NET-07 | Perimeter deny surge | Firewall drop/deny count spikes vs baseline (probing or misconfig) | firewall | T1595 | medium |
| NET-08 | Resource-exhaustion on public service | Application-layer request rate to a public app far above baseline | WAF/LB/app | T1499 | high |

## Worked queries

### NET-01 — Egress volume baseline deviation

**Sentinel (KQL)** — time-series anomaly on egress bytes per source:
```kql
let lookback = 14d;
let step = 1h;
CommonSecurityLog
| where TimeGenerated > ago(lookback)
| where DeviceAction in ("allow","allowed") and Direction == "Outbound"
| make-series TotalBytes = sum(SentBytes) default=0 on TimeGenerated step step by SourceIP
| extend (anomalies, score, baseline) = series_decompose_anomalies(TotalBytes, 2.5, -1, "linefit")
| mv-expand TimeGenerated to typeof(datetime), TotalBytes to typeof(long),
            anomalies to typeof(int), score to typeof(double), baseline to typeof(long)
| where anomalies == 1 and TotalBytes > baseline
| project TimeGenerated, SourceIP, TotalBytes, baseline, score
| sort by score desc
```

**Splunk (SPL)** — compare live volume to a stored per-hour baseline lookup:
```spl
index=firewall action=allowed direction=outbound earliest=-1h
| stats sum(bytes_out) as bytes_out by src_ip
| eval hour=strftime(now(),"%H")
| lookup egress_baseline.csv src_ip hour OUTPUT p95_bytes stdev_bytes avg_bytes
| where bytes_out > p95_bytes AND bytes_out > (avg_bytes + 3*stdev_bytes)
| eval deviation_x=round(bytes_out/avg_bytes,1)
| table _time src_ip bytes_out avg_bytes p95_bytes deviation_x
| sort - deviation_x
```

### NET-05 — Source fan-in (volumetric DDoS)

**Splunk (SPL)**:
```spl
index=firewall earliest=-5m
| stats dc(src_ip) as unique_sources sum(bytes) as total_bytes count as conns by dest_ip dest_port
| where unique_sources > 500 AND conns > 10000
| sort - unique_sources
```

**Sentinel (KQL)**:
```kql
CommonSecurityLog
| where TimeGenerated > ago(5m)
| summarize UniqueSources = dcount(SourceIP), Conns = count(), Bytes = sum(SentBytes)
    by DestinationIP, DestinationPort
| where UniqueSources > 500 and Conns > 10000
| sort by UniqueSources desc
```

## Tuning
- Whitelist CDNs, backup/replication windows, and known bulk-transfer hosts before enabling NET-01.
- DoS thresholds (500 sources, 10k conns) are placeholders — set from your link capacity and NET-01 baseline.
- Pair NET with upstream provider/scrubbing telemetry where you have it; the SIEM view is corroboration, not the primary mitigation.
