# Baseline Methodology (for the deviation detections)

Signature detections need no baseline; the deviation detections in categories 01, 04, and 05 do. A weak baseline turns them into noise. This is how to build them.

## What "normal" means per detection type
| Detection type | Baseline unit | Deviation signal |
|----------------|---------------|------------------|
| Volumetric (traffic/DoS) | per-service or per-interface byte/packet/connection rate over time-of-day | rate exceeds mean + Nσ, or historical max |
| East-west peer | per-host set of peers it normally talks to | a **new** peer / new port not seen in the learning window |
| Beaconing | per src→dst connection timing | low jitter / high regularity of intervals |
| DNS volume | per-host query rate, per-domain query count | outlier query volume, high NXDOMAIN ratio, rare domain |
| Auth | per-account normal source/geo/time | new geo, impossible travel, off-hours |

## Building a baseline
1. **Pick a clean learning window.** 2–4 weeks of representative activity with no known incident. Longer for weekly/seasonal patterns.
2. **Segment by the right key.** Time-of-day and day-of-week matter for volume; per-host for peer/DNS baselines; per-account for auth. A single global baseline over-generalizes.
3. **Compute robust stats.** Prefer median/percentiles (p95/p99) over mean±σ for skewed network data; keep per-key historical max.
4. **Store it.** Splunk: a summary index or lookup refreshed on a schedule; Sentinel: a scheduled summarization to a custom table or `_CL`, or inline `series_decompose_anomalies()` / built-in UEBA.
5. **Re-baseline on a cadence.** Networks drift (new apps, cloud migration). Recompute monthly, and after any known environment change.

## Splunk patterns
- Historical baseline via summary + `stats`: compute `avg`, `stdev`, `p95` per key in a lookup; compare live with `| eval is_outlier=if(value > p95_baseline, 1, 0)`.
- Built-in anomaly: `| anomalydetection`, or ML Toolkit for richer models.
- New-peer detection: keep a lookup of known `src→dst` (or `src→dst_port`) pairs; alert on pairs not present.

## Sentinel patterns
- `series_decompose_anomalies()` over `make-series` for time-series volume outliers.
- `materialize()` + a summarized baseline table joined to live data for new-peer / rare-value detection.
- Native **UEBA** and built-in anomaly analytics for identity/east-west where available.

## Managing false positives
- **Require persistence** where possible (an outlier that lasts N intervals, not one sample).
- **Whitelist known-benign** (backup windows, vuln scanners, patch servers, monitoring hosts) — these dominate volume/scan FPs.
- **Tier by asset value** — the same deviation on a domain controller or a crown-jewel host outranks a workstation.
- **Feed confirmed benigns back** into the baseline/whitelist rather than just closing the alert.
