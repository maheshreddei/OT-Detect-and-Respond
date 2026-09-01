# 04 — Metrics & Reporting

TDA only earns its keep if it produces measurable, trendable output. These are the metrics and the report.

## Core metrics
| Metric | Definition | Target (set yours) |
|--------|------------|--------------------|
| **MTTD** | alert time − simulated-action time, per test | ≤ target per severity (e.g. critical ≤ 5 min) |
| **Detection pass rate** | tests passed ÷ tests run | trend up; e.g. > 90% for priority use cases |
| **Coverage** | use cases validated ÷ total use cases | trend up |
| **ATT&CK coverage tested** | techniques with a passing test ÷ techniques claimed | trend up |
| **Blind spots** | techniques with no data *and* no rule | trend down |
| **False-positive rate** | FP ÷ total alerts for the rule | < threshold per severity |
| **Validation currency** | % priority detections tested within cadence window | ~100% |

## Detection-health scorecard (per use case)
| Use case | Detection | ATT&CK | Data? | Fired? | MTTD | FP rate | State | Owner |
|----------|-----------|--------|:-----:|:------:|:----:|:-------:|-------|-------|
| ... | MOD-01 | T0836 | ✓ | ✓ | 40s | low | Pass | |

## Coverage visualization
Export tested techniques to a **MITRE ATT&CK Navigator** layer, colored by state (green pass / yellow partial / red fail / grey untested). This is the single most effective way to show leadership where the detection gaps are — for both ATT&CK Enterprise (IT) and ATT&CK for ICS (OT).

## The TDA report (per cycle)
Use [`../templates/tda-report-template.md`](../templates/tda-report-template.md):
1. **Scope** — use cases/techniques tested this cycle.
2. **Results** — the scorecard (pass/partial/fail, MTTD, FP).
3. **Blind spots** — newly discovered gaps → detection backlog.
4. **Remediation** — failed detections, root cause, fix, retest status.
5. **Trends** — pass-rate, MTTD, coverage over time.
6. **Recommendations** — what to build/tune next.

## Trending
Keep results over time so you can show the detection estate **improving**: pass-rate up, MTTD down, blind spots closing, coverage expanding. This is what turns TDA from an audit into a program, and ties directly into the SOC KPIs (FP rate, MTTD, coverage) in the delivery playbook.
