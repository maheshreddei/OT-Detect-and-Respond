# Common Data Model

Every detection in this repo assumes this schema. Standardize your ingestion to it (or edit the field names in each query to match yours). Consistency here is what makes the detections portable across sites and across Splunk/Sentinel.

## Historian value events

One event per tag value (on-change or interpolated sample).

| Concept | Splunk field | Sentinel column | Example | Notes |
|---------|--------------|-----------------|---------|-------|
| Timestamp | `_time` | `TimeGenerated` | 2026-01-14T08:22:03Z | Source timestamp, not ingest time |
| Tag name | `tag` | `TagName_s` | `PLANT1.U200.FT201.PV` | Fully-qualified point name |
| Value | `value` | `Value_d` | `42.7` | Numeric |
| Quality | `quality` | `Quality_s` | `Good` | `Good` / `Bad` / `Uncertain` |
| Source | `source` | `Source_s` | `hmi_historian` | Provenance — key for E01 |
| Mode / state | `mode` | `Mode_s` | `run` | Segmentation key (may be derived) |
| Engineering unit | `unit` | `Unit_s` | `m3/h` | Optional |
| Asset / unit | `asset` | `Asset_s` | `U200` | Optional, for grouping |

**`source` values used in this repo**
- `hmi_historian` — value as it arrived through the normal control→HMI→historian path
- `direct_opcua` — independent direct read from the controller/OPC server (for E01 divergence)
- `plc_direct` — direct PLC tap, if available

### Splunk
- **Index:** `ot_historian`
- **Sourcetype:** `historian:snapshot`
- Recommended: define a **data model / CIM-style acceleration** over `ot_historian` so `| tstats` works for high-volume tags.

### Sentinel
- **Custom table:** `OTHistorian_CL`
- Ingest via Data Collector API / AMA custom log. Keep the `_s` / `_d` suffixes the DCR assigns, or map them in a parser function `OTHistorian` and query that.

## Baseline lookup / watchlist

Per-tag, per-mode baseline. Seeded per [`baseline-methodology.md`](baseline-methodology.md).

- **Splunk:** lookup `ot_baseline.csv` — see [`../lookups/ot_baseline.csv`](../02-detection/historian/ot_baseline.csv)
- **Sentinel:** watchlist `OTBaseline`, key alias `TagName`

| Column | Meaning |
|--------|---------|
| `tag` / `TagName` | Fully-qualified point name |
| `mode` | Operating mode this row applies to |
| `mean`, `std` | Mean and standard deviation (clean window, Good quality) |
| `p01`, `p50`, `p99` | Percentile band |
| `ll`, `hl` | Engineering low/high limits (authoritative when present) |
| `max_slew_per_min` | Max plausible absolute rate of change |
| `min_variance` | Variance floor (replay/freeze detection) |
| `max_stall_sec` | Max legitimate constant-hold duration |

## Safety trip limits lookup / watchlist

Trip and pre-alarm limits for safety-related tags (G-family).

- **Splunk:** lookup `sif_trip_limits.csv` — see [`../lookups/sif_trip_limits.csv`](../02-detection/historian/sif_trip_limits.csv)
- **Sentinel:** watchlist `SIFTripLimits`, key alias `TagName`

| Column | Meaning |
|--------|---------|
| `tag` / `TagName` | Safety-related PV point name |
| `sif_id` | Safety Instrumented Function identifier |
| `trip_direction` | `high` or `low` — direction the trip fires |
| `trip_value` | The SIF trip setpoint |
| `prealarm_value` | Pre-alarm threshold |
| `safe_margin` | Engineering margin that defines "approaching" |
| `unit` | Engineering unit |

## Field lookups referenced by queries

- Splunk detections use `| lookup ot_baseline.csv tag mode OUTPUT ...` and `| lookup sif_trip_limits.csv tag OUTPUT ...`.
- Sentinel detections use `_GetWatchlist("OTBaseline")` / `_GetWatchlist("SIFTripLimits")` joined on `TagName`.

## A note on timestamps

Historians backfill and interpolate. Two rules keep the math honest:
1. Detections that compare values across sources (E01) or over time (C01, A03, G01) **bin by time** (`bin`/`summarize ... by bin()`) so samples align, and require the compared samples to fall in the same bin.
2. Always filter `quality == "Good"` before statistics unless the detection is specifically *about* quality (C03).
