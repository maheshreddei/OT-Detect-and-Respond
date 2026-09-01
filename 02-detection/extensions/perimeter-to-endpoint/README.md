# Perimeter-to-Endpoint Detections

**Detection engineering across the external-facing kill chain — from the internet edge, through identity and the network interior, to the endpoint.** SIEM-ready logic (Splunk SPL + Microsoft Sentinel KQL), mapped to MITRE ATT&CK.

![Detections](https://img.shields.io/badge/detections-40%2B-blue)
![Platforms](https://img.shields.io/badge/platforms-Splunk%20%7C%20Microsoft%20Sentinel-orange)
![Framework](https://img.shields.io/badge/mapped-MITRE%20ATT%26CK-red)
![Scope](https://img.shields.io/badge/scope-perimeter%20%E2%86%92%20identity%20%E2%86%92%20endpoint-lightgrey)
![License](https://img.shields.io/badge/license-MIT-green)

---

## The model: follow the attacker inward

An external compromise moves through predictable stages. This library is organized along that path, so coverage maps to the way an intrusion actually unfolds — and so a single incident lights up multiple layers you can correlate.

```
  INTERNET EDGE          IDENTITY              ENDPOINT              INTERIOR              EGRESS
  ─────────────          ────────              ────────              ────────              ──────
  scanning, DoS,     →   failed auth,      →   process, cred     →   east-west         →   DNS anomalies,
  webapp attacks,        spray, success        access, persist,      lateral movement,     C2 beaconing,
  prohibited traffic     after failure,        defense evasion       internal scanning     exfil, outliers
                         priv change
        │                     │                     │                     │                    │
    01 network           02 identity           03 endpoint           04 east-west         05 outliers
    06 scanning                                                                            07 prohibited
```

Each layer is a folder of detections; the numbering follows the flow, not priority.

## Detection categories

| # | Category | Covers | File |
|---|----------|--------|------|
| 01 | Network — perimeter, baseline & DoS/DDoS | volumetric baselines, SYN/UDP floods, connection-rate spikes, amplification | [`detections/01-network-perimeter-dos.md`](detections/01-network-perimeter-dos.md) |
| 02 | Identity & account | failed auth, password spray, brute-force **success after failures**, privilege/permission change, impossible travel | [`detections/02-identity-account.md`](detections/02-identity-account.md) |
| 03 | Endpoint — Windows & EDR | suspicious process/LOLBins, credential access, persistence, defense evasion, EDR correlation | [`detections/03-endpoint-windows-edr.md`](detections/03-endpoint-windows-edr.md) |
| 04 | East-west / lateral movement | internal scanning, SMB/WMI/RDP lateral, new internal peer deviations, admin-share abuse | [`detections/04-east-west-lateral.md`](detections/04-east-west-lateral.md) |
| 05 | Network traffic outliers | DNS tunnelling/DGA/NXDOMAIN, beaconing, connection & byte-count outliers, rare destinations | [`detections/05-traffic-outliers-dns.md`](detections/05-traffic-outliers-dns.md) |
| 06 | Outbound scanning & web-app attacks | internal→external scanning, web brute force, injection/enumeration patterns | [`detections/06-scanning-webapp.md`](detections/06-scanning-webapp.md) |
| 07 | Prohibited network traffic | threat-intel IOC hits, Tor/P2P/mining, geo-prohibited, unauthorized cleartext/cloud | [`detections/07-prohibited-traffic.md`](detections/07-prohibited-traffic.md) |

## What each detection looks like

Every category file has a **detection table** (id, detection, logic, data source, ATT&CK, severity) covering the category comprehensively, plus **worked queries** (Splunk SPL + Sentinel KQL) for the flagship detections. The full list is in [`catalog/detection-catalog.csv`](catalog/detection-catalog.csv) as an implementation backlog.

## Two detection styles, used deliberately

- **Signature / rule** — a known-bad pattern (encoded PowerShell, IOC hit, prohibited protocol). Fast, precise, low-FP; blind to novel activity.
- **Baseline / deviation** — statistical or peer-relative anomaly (traffic volume outlier, new east-west peer, beaconing regularity). Catches the unknown; needs a clean baseline and tuning.

The perimeter and prohibited-traffic layers lean signature; the network-outlier and east-west layers lean baseline. [`docs/baseline-methodology.md`](docs/baseline-methodology.md) covers how to build the baselines the deviation detections depend on.

## Data sources

Every detection names the telemetry it needs. The master mapping — Splunk CIM data models / sourcetypes and Sentinel tables (SigninLogs, SecurityEvent, Device* from MDE, CommonSecurityLog, DnsEvents, W3CIISLog, threat-intel) — is in [`docs/data-sources.md`](docs/data-sources.md). Cross-check it to find telemetry gaps before deploying.

## How to use

1. Confirm the data sources you have ([`docs/data-sources.md`](docs/data-sources.md)); gaps become a telemetry backlog.
2. Deploy signature detections first (fast wins), then stand up baselines for the deviation detections.
3. Tune thresholds to your environment — every threshold here is a starting point.
4. Correlate across layers: a webapp attack (06) → a new account (02) → suspicious process on that host (03) → beaconing egress (05) is one incident, not four alerts.

## Relationship to OT
This is the **IT/enterprise** side. In an IT/OT architecture it defends the path attackers take *before* they reach the OT boundary — pair it with the OT-specific protocol and historian detection libraries for defence in depth across the whole environment.

## Author
Mahesh Reddy — Security & OT/ICS Detection Engineering

## License
MIT — see [`LICENSE`](LICENSE).

> Queries assume common data models (Splunk CIM; Sentinel/MDE schema). Field names, table names, and thresholds must be adapted to your environment. All content is detection-only.
