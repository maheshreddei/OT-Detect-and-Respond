# 05 — Network Traffic Outliers (DNS & Volume)

The egress/C2 layer. These catch command-and-control and exfiltration through statistical outliers: DNS abuse (tunnelling, DGA), beaconing regularity, and connection/byte-count anomalies.

## Detections

| ID | Detection | Logic | Data source | ATT&CK | Severity |
|----|-----------|-------|-------------|--------|----------|
| OUT-01 | DNS tunnelling | High query volume to one domain, long/high-entropy labels, TXT/NULL abuse | DNS logs | T1071.004 / T1048 | high |
| OUT-02 | DGA activity | High NXDOMAIN ratio + high-entropy domains from one host | DNS logs | T1568.002 | high |
| OUT-03 | Rare / new external domain | Domain seen by very few hosts / first-seen, low popularity | DNS logs / proxy | T1071 | medium |
| OUT-04 | Beaconing (regular C2) | Low jitter / high regularity of connection intervals src→dst | flow / proxy | T1071 / T1573 | high |
| OUT-05 | Connection-count outlier | Host's outbound connection count far exceeds its baseline | flow | T1071 | medium |
| OUT-06 | Data-volume outlier (exfil) | Outbound bytes to one dst far exceed baseline / upload>>download | flow / proxy | T1041 / T1048 | high |
| OUT-07 | Long-lived / high-byte session | Single session with abnormal duration+bytes to external | flow | T1071 | medium |
| OUT-08 | DNS over HTTPS/rare resolver | DNS to non-approved resolver / DoH endpoints | flow / proxy | T1071.004 | medium |

## Worked queries

### OUT-01 — DNS tunnelling

**Sentinel (KQL)**:
```kql
let window = 1h;
DnsEvents
| where TimeGenerated > ago(window) and QueryType in ("TXT","NULL","CNAME","A","AAAA")
| extend Domain = strcat_array(array_slice(split(Name,"."), -2, -1), ".")
| extend SubLen = strlen(Name) - strlen(Domain)
| summarize Queries = count(), AvgSubLen = avg(SubLen), DistinctSub = dcount(Name), TxtRatio = countif(QueryType=="TXT")*1.0/count()
    by ClientIP, Domain
| where Queries > 500 and (AvgSubLen > 30 or DistinctSub > 200 or TxtRatio > 0.5)
| sort by Queries desc
```

**Splunk (SPL)** — CIM Network_Resolution:
```spl
index=dns
| eval domain=mvindex(split(query,"."),-2)+"."+mvindex(split(query,"."),-1)
| eval sublen=len(query)-len(domain)
| stats count as queries avg(sublen) as avg_sublen dc(query) as distinct_sub by src_ip domain
| where queries > 500 AND (avg_sublen > 30 OR distinct_sub > 200)
| sort - queries
```

### OUT-02 — DGA (high NXDOMAIN + entropy)

**Splunk (SPL)**:
```spl
index=dns
| stats count as total count(eval(reply_code=="NXDOMAIN")) as nxdomain dc(query) as distinct_q by src_ip
| eval nx_ratio=round(nxdomain/total,2)
| where total > 100 AND nx_ratio > 0.4 AND distinct_q > 50
| sort - nx_ratio
```

**Sentinel (KQL)**:
```kql
DnsEvents
| where TimeGenerated > ago(1h)
| summarize Total = count(), Nx = countif(ResponseCode == 3), Distinct = dcount(Name) by ClientIP
| extend NxRatio = round(Nx * 1.0 / Total, 2)
| where Total > 100 and NxRatio > 0.4 and Distinct > 50
| sort by NxRatio desc
```

### OUT-04 — Beaconing (interval regularity)

**Sentinel (KQL)** — low coefficient-of-variation of inter-connection gaps:
```kql
let window = 24h;
DeviceNetworkEvents
| where TimeGenerated > ago(window) and RemoteIPType == "Public"
| order by DeviceName, RemoteIP, TimeGenerated asc
| serialize
| extend gap = datetime_diff('second', TimeGenerated, prev(TimeGenerated))
| where isnotnull(gap) and prev(RemoteIP) == RemoteIP and prev(DeviceName) == DeviceName
| summarize Conns = count(), AvgGap = avg(gap), StdevGap = stdev(gap) by DeviceName, RemoteIP
| extend CoV = StdevGap / AvgGap
| where Conns >= 20 and CoV < 0.1 and AvgGap > 30
| sort by CoV asc
```

### OUT-06 — Data-volume exfil outlier

**Splunk (SPL)**:
```spl
index=flow direction=outbound earliest=-1h
| stats sum(bytes_out) as bytes_out sum(bytes_in) as bytes_in by src_ip dest_ip
| eval upload_ratio=round(bytes_out/(bytes_in+1),1)
| lookup egress_dst_baseline.csv src_ip OUTPUT p95_bytes
| where bytes_out > 100000000 OR (bytes_out > p95_bytes AND upload_ratio > 10)
| sort - bytes_out
```

## Tuning
- Whitelist CDNs, telemetry/analytics domains, software-update and cloud-backup destinations — they dominate beaconing/volume FPs.
- OUT-04 beaconing legitimately matches many SaaS heartbeats; combine low-CoV with rare/new destination (OUT-03) to sharpen.
- Entropy/length thresholds (30, 0.4 NX ratio) are starting points; validate against your DNS baseline.
