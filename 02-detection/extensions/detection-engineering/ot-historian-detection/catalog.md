# Detection Catalog

Complete catalog of historian baseline-and-deviation use cases. Legend: ✅ built · 🚧 planned.

Every use case follows the same shape: **establish a baseline of "normal" from a validated clean window, then alert on statistically or physically significant deviation.** Baselines are segmented by operating mode — see [`docs/baseline-methodology.md`](docs/baseline-methodology.md).

---

## A. Statistical / operating-envelope deviation

| ID | Detection | Concept | Key tags | ATT&CK ICS | Status |
|----|-----------|---------|----------|------------|--------|
| A01 | Tag out of operating envelope | Value breaches historical min/max or P1–P99 band for its mode | Any analog PV | T0836, T0831 | ✅ |
| A02 | Z-score / σ-band breach | Value exceeds rolling mean ± Nσ | Continuous analog PV | T0836, T0856 | 🚧 |
| A03 | Rate-of-change anomaly | Derivative exceeds physically plausible slew rate | PV + timestamp | T0831, T0806 | 🚧 |
| A04 | Variance collapse | Live noise drops below baseline variance (a real sensor is never perfectly flat) | Analog PV | T0856 | 🚧 |
| A05 | Operating-band drift | Steady-state mean slowly departs baseline centroid | Steady-state PV | T0831 | 🚧 |

## B. Setpoint & control-loop integrity

| ID | Detection | Concept | Key tags | ATT&CK ICS | Status |
|----|-----------|---------|----------|------------|--------|
| B01 | Setpoint outside approved range | SP written beyond MOC-approved limits (Oldsmar) | SP tags | T0836 | ✅ |
| B02 | Setpoint change off-window | SP altered outside maintenance/MOC window or off-shift | SP + timestamp | T0836, T0855 | 🚧 |
| B03 | PV–CV loop mismatch | Output moves but PV doesn't track (spoofed feedback) | PV + CV pair | T0832, T0856 | 🚧 |
| B04 | Controller output saturation | CV pinned 0%/100% persistently | CV / MV tags | T0831 | 🚧 |
| B05 | Loop mode-flip anomaly | AUTO→MANUAL or cascade broken outside normal ops | Loop mode tags | T0831, T0855 | 🚧 |

## C. Frozen / stale / replay

| ID | Detection | Concept | Key tags | ATT&CK ICS | Status |
|----|-----------|---------|----------|------------|--------|
| C01 | Frozen value / replay | PV stuck at identical value beyond max stall (stuck sensor or Stuxnet-style replay) | Any PV | T0856, T0815 | ✅ |
| C02 | Cyclic replay signature | Value pattern repeats a prior recorded window | High-res PV | T0856, T0832 | 🚧 |
| C03 | Timestamp / quality anomaly | Bad/Uncertain OPC quality flags or backfill gaps spike | Tag quality attribute | T0815, T0829 | 🚧 |

## D. Physical plausibility / process model

| ID | Detection | Concept | Key tags | ATT&CK ICS | Status |
|----|-----------|---------|----------|------------|--------|
| D01 | Mass/energy balance violation | Σ(in) − Σ(out) exceeds tolerance beyond storage change | Flow + level tags | T0831, T0806 | 🚧 |
| D02 | Impossible state combination | e.g. pump OFF but downstream flow present | Discrete state + analog PV | T0831, T0835 | ✅ |
| D03 | Cross-tag correlation break | Coupled variables (temp↔pressure) diverge from baseline correlation | Correlated PV pairs | T0856, T0832 | 🚧 |
| D04 | Energy/production ratio anomaly | kWh-per-unit departs baseline (covert manipulation) | Utility + throughput | T0831 | 🚧 |

## E. Data-integrity / value divergence

| ID | Detection | Concept | Key tags | ATT&CK ICS | Status |
|----|-----------|---------|----------|------------|--------|
| E01 | Historian vs live PLC divergence | Independent direct read disagrees with HMI-path historian value (spoofed view) | Same tag, two sources | T0832, T0856 | ✅ ⭐ |
| E02 | Redundant sensor disagreement | 2oo3 / redundant transmitters diverge beyond tolerance | Redundant PV set | T0856 | 🚧 |
| E03 | Analog vs discrete disagreement | Analog PV contradicts its own limit-switch status | Analog + discrete pair | T0835 | 🚧 |

## F. Temporal / operational context

| ID | Detection | Concept | Key tags | ATT&CK ICS | Status |
|----|-----------|---------|----------|------------|--------|
| F01 | Off-hours process activity | PVs/SPs changing while unit should be idle/unmanned | PV/SP + shift calendar | T0831, T0836 | 🚧 |
| F02 | Batch/sequence timing anomaly | Phase duration or step order deviates from golden batch | Batch phase + step | T0831 | 🚧 |
| F03 | State-transition anomaly | Equipment starts in wrong sequence (Ukraine breaker ops) | Discrete state machine | T0855, T0831 | 🚧 |
| F04 | Startup/shutdown profile deviation | Ramp curve departs baseline trajectory | PV during transient | T0831 | 🚧 |

## G. Safety & alarm

| ID | Detection | Concept | Key tags | ATT&CK ICS | Status |
|----|-----------|---------|----------|------------|--------|
| G01 | SIF trip-point approach | PV trending toward safety trip while control appears normal (TRITON precursor) | Safety-related PV | T0880, T0837 | ✅ ⭐ |
| G02 | Safety limit trending | Sustained drift toward alarm/interlock threshold | PV + alarm limits | T0880 | 🚧 |
| G03 | Alarm suppression / shelving | Expected alarms absent, or mass shelving | Alarm state tags | T0878, T0815 | 🚧 |
| G04 | Alarm flood correlation | Alarm-rate spike correlated with PV deviations (masking) | Alarm event stream | T0878 | 🚧 |

---

## ATT&CK for ICS coverage (built detections)

| Technique | ID | Covered by |
|-----------|----|-----------|
| Modify Parameter | T0836 | A01, B01 |
| Manipulate I/O Image | T0835 | D02 |
| Spoof Reporting Message | T0856 | C01, E01 |
| Rogue Master | T0848 | (planned) |
| Loss of Safety | T0880 | G01 |
| Denial of Control | T0813 | (planned) |
| Manipulation of View | T0832 | E01 |
| Detect Operating Mode / Point&Tag ID | T0868/T0861 | (planned) |

## Contribution order (suggested build sequence)

1. **A02, A03** — extend the statistical family (highest reuse, seed baseline once).
2. **E02** — redundant sensor disagreement (reuses E01 pattern).
3. **G02, G03** — complete the safety family.
4. **F01, F03** — temporal context, needs shift/calendar and state-machine data.
5. **D01, D03** — process-model detections (require engineering tolerances).
