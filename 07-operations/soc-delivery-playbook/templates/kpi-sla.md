# MSS KPIs & SLAs (Template)

## Service levels (agree per engagement)
| SLA | Definition | Example target |
|-----|------------|----------------|
| Monitoring coverage | Hours of active monitoring | 24x7 (or 8x5) |
| Alert triage time | Alert raised → triaged | Critical < 15 min; High < 1 h |
| Incident response time | Confirmed incident → response initiated | Critical < 30 min |
| Escalation | Time to escalate per severity | Per runbook |
| Reporting cadence | Operational + executive reports | Weekly ops / monthly exec |

## KPIs (track & report)
| KPI | Definition | Target |
|-----|------------|--------|
| False-positive rate | FP ÷ total alerts (per detection & portfolio) | < 15% per detection; < 5% portfolio |
| MTTD | Deviation onset → alert | < 5 min (near-real-time detections) |
| MTTT | Alert → triage complete | < 30 min |
| MTTR | Incident → resolved | Per severity |
| Detection coverage | Deployed ÷ prioritized use cases | Trend up |
| ATT&CK-ICS coverage | Techniques covered | Trend up |
| Baseline freshness | % tags/pairs baselined within cadence | > 95% |
| Validation currency | % prod detections validated in last quarter | 100% |
| Threat-hunt cadence | Hunts per period; findings actioned | Per plan |

## Reporting
- **Operational (weekly):** alert/incident summary, FP tuning, new/retired detections, coverage changes.
- **Executive (monthly/quarterly):** risk posture, KPI trends, notable incidents, coverage & maturity progression, recommendations.

Ties to the detection lifecycle (RACI, cadence) in the detection libraries.
