# Baseline Methodology

The single biggest determinant of whether historian detection is useful or noise. Read this before deploying anything.

## The central problem: OT process data is non-stationary

A control variable does not have *one* normal range. A reactor temperature has a completely different normal during **startup**, **steady-state production**, **grade change**, and **shutdown**. A tank level's normal depends on the **batch phase**. Load-following assets vary by **time of day**.

A single global `mean ± 3σ` baseline computed across all of that will:
- set bands so wide they never fire (misses the attack), **or**
- fire constantly on legitimate mode changes (analyst tunes it off).

**Baselines must be segmented.** This is the whole game.

## Segmentation dimensions

Key each baseline by the dimensions that actually change "normal" for a tag:

| Dimension | Source | Applies to |
|-----------|--------|------------|
| **Operating mode / state** | An explicit state/mode tag, or a derived regime | Almost everything — the primary key |
| **Batch phase / step** | Batch execution tags (S88) | Batch and hybrid processes |
| **Time-of-day / shift** | Calendar | Load-following (utilities, HVAC, water demand) |
| **Product grade / recipe** | Recipe ID tag | Multi-product lines |

In the repo's data model, the segmentation key is the `mode` field (Splunk) / `Mode_s` column (Sentinel). The baseline lookup is keyed on `(tag, mode)`. If a site has no mode tag, derive one (see "Inferring mode" below) rather than falling back to a global baseline.

## Seeding a baseline from a clean window

1. **Select a validated clean window.** Choose a period of known-good operation — no incidents, no unusual maintenance, representative of each operating mode. Confirm with the process/ops team, not just by looking at the data. Two to four weeks covering all modes is a reasonable starting point; longer for seasonal assets.
2. **Filter to Good quality.** Drop Bad/Uncertain samples before computing statistics so sensor faults don't poison the baseline.
3. **Split by segmentation key.** Group samples by `(tag, mode)`.
4. **Compute robust statistics per group:**
   - `mean`, `std`
   - percentiles `p01`, `p50`, `p99` (percentile bands are more robust to skew than mean±σ for asymmetric process variables)
   - engineering limits `ll`/`hl` where the instrument/process defines hard limits (prefer these over statistical bands when available)
   - `max_slew_per_min` — the 99th-percentile absolute rate of change (for A03)
   - `min_variance` — the 1st-percentile rolling variance (for A04 / C01 variance collapse)
   - `max_stall_sec` — the 99th-percentile duration the value legitimately holds constant (for C01 frozen detection)
5. **Sanity-check with the process engineer.** A baseline that disagrees with the operator's intuition about a loop is a finding in itself.
6. **Publish** to `lookups/ot_baseline.csv` (Splunk) or the `OTBaseline` watchlist (Sentinel).

## Prefer engineering limits over statistical bands where they exist

Statistics describe what the process *did*; engineering limits describe what it *should* do. For any tag with instrument range, alarm limits, or design limits, use those as the authoritative band and use statistics only to tighten within them. The detections `coalesce(ll, p01)` / `coalesce(hl, p99)` for exactly this reason — hard limits win when present.

## Re-baselining cadence

Process "normal" drifts legitimately (catalyst aging, seasonal feedstock, equipment wear). A stale baseline slowly becomes noise.

| Trigger | Action |
|---------|--------|
| **Scheduled** | Recompute quarterly (or per production campaign) against a fresh validated clean window. |
| **Post-MOC** | Any Management-of-Change that alters a loop's normal (new setpoint policy, retune, equipment swap) triggers a targeted re-baseline of the affected tags. |
| **Post-incident** | After a confirmed incident, exclude the incident window and re-seed. |
| **Drift alarm (A05)** | If the operating-band-drift detector fires legitimately, that's the signal to re-baseline that tag. |

Re-baselining is a controlled change: version the lookup, record who approved it, and keep the prior version for rollback. This hooks into the KPI cadence in [`detection-lifecycle.md`](detection-lifecycle.md).

## Inferring mode where no state tag exists

If the process has no clean mode/state tag:
- **Threshold on a driver tag** — e.g. main feed flow > X ⇒ "running", else "idle". Simple and usually sufficient.
- **Cluster steady-state regimes** — offline k-means / change-point detection on a handful of driver tags to label regimes, then encode the labels as a derived mode. Do this in the historian analytics or an offline job; publish the resulting label as a synthetic mode tag.

Do the clustering **offline during baselining**, not live in the SIEM.

## Managing false positives

- **Require persistence.** A single out-of-band sample is usually noise or a transient. Every statistical detection here supports an *N-consecutive-samples* / *T-seconds* dwell before alerting. Tune this per tag class.
- **Suppress during known transitions.** Mode changes, startups, and MOC windows are expected excursions. Gate detections with the mode key and a maintenance-window calendar.
- **Tier by consequence, not just by statistics.** A 3σ excursion on a safety-related tag (G-family) outranks a 5σ excursion on a non-critical trend. Severity should weight the tag's process criticality.
- **Feed FP outcomes back into the baseline.** A confirmed-benign excursion that recurs is a baseline gap — fix the baseline, don't just close the alert.

## Statistical method selection

| Tag behaviour | Recommended baseline method |
|---------------|-----------------------------|
| Symmetric, stable analog | `mean ± Nσ` |
| Skewed / bounded analog | Percentile band `p01–p99` |
| Hard-limited by instrument/process | Engineering `ll`/`hl` |
| Rate-limited actuator | `max_slew_per_min` on the derivative |
| Should-be-noisy sensor | `min_variance` floor (detects replay/freeze) |
| Discrete / stateful | State-transition model (F-family), not statistics |
| Coupled pair | Baseline the **correlation/ratio**, not each tag alone (D03/D04) |

The right method is a property of the tag, not a global setting. The baseline lookup carries all of these columns so a single detection can pick the appropriate one per tag.
