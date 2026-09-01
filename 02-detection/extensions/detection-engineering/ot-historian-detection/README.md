# OT Historian Detection Library

**Baseline-and-deviation threat detection for ICS/OT process historians**

![Status](https://img.shields.io/badge/status-active-brightgreen)
![Detections](https://img.shields.io/badge/detections-6%20built%20%2F%2032%20cataloged-blue)
![Platforms](https://img.shields.io/badge/platforms-Splunk%20%7C%20Microsoft%20Sentinel%20%7C%20PI%20AF-orange)
![Framework](https://img.shields.io/badge/mapped-MITRE%20ATT%26CK%20for%20ICS-red)
![Standards](https://img.shields.io/badge/aligned-NIST%20800--82r3%20%7C%20IEC%2062443-lightgrey)
![License](https://img.shields.io/badge/license-MIT-green)

---

## Why historian-based detection

The process historian (OSIsoft/AVEVA PI, GE Proficy, Wonderware, Canary, Ignition) is the **only telemetry source in an OT environment that sees the physics**. Network-layer monitoring (Nozomi, Claroty, Dragos) tells you *a Modbus write occurred*; the historian tells you *whether that write drove the process outside its safe, normal, physically-plausible envelope*.

Every landmark ICS attack surfaces in historian data even when the network layer looks legitimate:

| Incident | Process-value signature | Detection family here |
|---|---|---|
| Stuxnet (2010) | Recorded sensor values replayed to the HMI while centrifuges over-sped | `C` Replay / `E` Divergence |
| Ukraine grid (2015/16) | Breaker state transitions in the wrong sequence | `F` State-transition |
| TRITON / TRISIS (2017) | PV trending toward SIS trip while control appeared normal | `G` SIF trip-point approach |
| Oldsmar water (2021) | NaOH setpoint written 100 → 11,100 ppm | `B` Setpoint outside range |

This library packages that detection layer as a versioned, testable, SIEM-portable rule set.

## What's in the box

- **32 cataloged use cases** across 7 detection families — see [`catalog.md`](catalog.md)
- **6 fully built detections** — each with a use-case brief, Sigma-style YAML metadata, **Splunk SPL** + **Microsoft Sentinel KQL** logic, and validation test cases
- **Reference architecture** for the historian → exception-bus → SIEM pipeline — see [`docs/architecture.md`](docs/architecture.md)
- **Baseline methodology** — segmentation, clean-window seeding, re-baselining cadence — see [`docs/baseline-methodology.md`](docs/baseline-methodology.md)
- **A common data model** for Splunk and Sentinel — see [`docs/data-model.md`](docs/data-model.md)
- **Detection lifecycle** with RACI and KPI cadence for MSS delivery — see [`docs/detection-lifecycle.md`](docs/detection-lifecycle.md)
- **A detection template** so new use cases stay consistent — see [`templates/detection-template/`](templates/detection-template/)

## Repository structure

```
ot-historian-detection/
├── README.md                     ← you are here
├── catalog.md                    ← all 32 use cases + status
├── docs/
│   ├── architecture.md           ← pipeline & deployment patterns
│   ├── baseline-methodology.md   ← the statistical core
│   ├── data-model.md             ← Splunk + Sentinel schema
│   └── detection-lifecycle.md    ← RACI + KPI (MSS delivery)
├── templates/
│   └── detection-template/       ← skeleton for new detections
├── lookups/
│   ├── ot_baseline.csv           ← per-tag/per-mode baseline
│   └── sif_trip_limits.csv       ← safety trip limits
└── detections/
    ├── A-statistical-envelope/
    ├── B-setpoint-control/
    ├── C-replay-stale/
    ├── D-physical-plausibility/
    ├── E-data-integrity/
    └── G-safety-alarm/
```

## Anatomy of a detection

Every built detection ships as a self-contained folder:

```
E01-historian-plc-divergence/
├── README.md         ← problem, logic, tuning, response, references
├── detection.yml     ← Sigma-style metadata (id, ATT&CK, baseline spec, level)
├── splunk.spl        ← production SPL
├── sentinel.kql      ← production KQL
└── validation.md     ← positive / negative / edge test cases
```

## Catalog at a glance

Legend: ✅ built · 🚧 planned

| ID | Detection | Family | ATT&CK ICS | Status |
|----|-----------|--------|------------|--------|
| A01 | Tag out of operating envelope | Statistical | T0836, T0831 | ✅ |
| A02 | Z-score / σ-band breach | Statistical | T0836, T0856 | 🚧 |
| A03 | Rate-of-change anomaly | Statistical | T0831, T0806 | 🚧 |
| A04 | Variance collapse ("too stable") | Statistical | T0856 | 🚧 |
| B01 | Setpoint outside approved range | Setpoint | T0836 | ✅ |
| B02 | Setpoint change off-window | Setpoint | T0836, T0855 | 🚧 |
| B03 | PV–CV loop mismatch | Setpoint | T0832, T0856 | 🚧 |
| C01 | Frozen value / replay | Replay/Stale | T0856, T0815 | ✅ |
| C02 | Cyclic replay signature | Replay/Stale | T0856, T0832 | 🚧 |
| D02 | Impossible state combination | Physical | T0831, T0835 | ✅ |
| D01 | Mass/energy balance violation | Physical | T0831, T0806 | 🚧 |
| D03 | Cross-tag correlation break | Physical | T0856, T0832 | 🚧 |
| E01 | Historian vs live PLC divergence | Integrity | T0832, T0856 | ✅ ⭐ |
| E02 | Redundant sensor disagreement | Integrity | T0856 | 🚧 |
| G01 | SIF trip-point approach | Safety | T0880, T0837 | ✅ ⭐ |
| G03 | Alarm suppression / shelving | Safety | T0878, T0815 | 🚧 |

Full 32-item catalog: [`catalog.md`](catalog.md).

## Quick start

1. Land historian data in your SIEM per [`docs/data-model.md`](docs/data-model.md) (PI Web API / OPC UA / DB Connect for Splunk; Data Collector / AMA for Sentinel).
2. Seed baselines from a validated clean window and load [`lookups/ot_baseline.csv`](lookups/ot_baseline.csv) — method in [`docs/baseline-methodology.md`](docs/baseline-methodology.md).
3. Deploy a detection: copy the `splunk.spl` or `sentinel.kql` into a scheduled correlation search / analytics rule.
4. Run the cases in each detection's `validation.md` before promoting to production.
5. Track FP rate and MTTD against the KPI cadence in [`docs/detection-lifecycle.md`](docs/detection-lifecycle.md).

## Design principles

- **Physics over signatures.** Detect what the process *did*, not just what a packet *said*.
- **Baseline by operating mode.** OT data is non-stationary; a global mean±σ drowns you in false positives. Baselines are keyed by mode/state.
- **Historian does the math, SIEM does the correlation.** Heavy per-tag statistics belong in the historian's native analytics engine; forward *exception events* to the SIEM for cross-domain correlation and IR.
- **Safety-first, passive-before-active.** Detections are read-only. Nothing here writes to a control system.
- **Testable.** No detection is "done" without positive, negative, and edge validation cases.

## Author

Mahesh Reddy — OT/ICS Security · GICSP, SANS ICS410, Nozomi Certified

## License

MIT — see [`LICENSE`](LICENSE).

> **Disclaimer.** Detection content is provided for defensive use. All logic is read-only against historian data. Validate every rule in a non-production environment before deployment. Trip limits, tag names, and thresholds in this repo are illustrative and **must** be replaced with site-specific, MOC-approved values.
