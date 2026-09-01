# E01 — Historian vs Live PLC Value Divergence ⭐

## Problem
This is the **"Stuxnet detection."** A sophisticated attacker manipulates the process but feeds the operator's view a fabricated, normal-looking value — a man-in-the-middle on the reporting path, or a compromised HMI/historian collector. Every value-based detection that trusts the historian path is blind to this, because the historian *shows normal*.

The only way to catch it is to compare the value that arrived through the normal control→HMI→historian path against an **independent second reading of the same tag**, taken from a different point on the path — a direct OPC UA read from the controller, a separate protocol tap, or a redundant collector. If the two disagree beyond sensor tolerance, one of them is being lied to.

## Detection concept
The same physical tag is collected from two sources:
- `hmi_historian` — the value as the operator sees it
- `direct_opcua` — an independent direct read from the controller/OPC server

Align both to a common time bin, compare them, and alert when they diverge by more than sensor tolerance (expressed in both absolute %, and in σ of the tag's own noise so tolerance scales with the tag). Require the divergence to persist across ≥2 consecutive bins so a one-off timing skew between collectors doesn't fire.

This is a **manipulation-of-view** detection (ATT&CK T0832) and the strongest single differentiator in the library — almost no OT SOC builds it, because it requires deliberately provisioning a second, independent collection path. That provisioning is the point: it removes the historian's single point of trust.

## Data required
- The same tags collected from **two independent sources** (`source` field = `hmi_historian` and `direct_opcua`) per [`../../../docs/data-model.md`](../../../docs/data-model.md)
- Baseline lookup `ot_baseline.csv` for the tag's `std` (used to scale tolerance)

> **Deployment prerequisite.** The second source must be **genuinely independent** — a different physical/logical path to the value. A second collector reading the *same* OPC tag from the *same* compromised server gives no assurance. Read direct from the controller where possible, or from a network tap the attacker doesn't control.

## Logic
- Splunk: [`splunk.spl`](splunk.spl)
- Sentinel: [`sentinel.kql`](sentinel.kql)

## Tuning
- **Bin width:** default 10s. Must be wide enough to absorb normal collection-timing skew between the two sources, narrow enough to catch a real divergence quickly. Set from the slower collector's update rate.
- **Tolerance:** default `sigma_diff > 3` OR `pct_diff > 2%`. The σ term auto-scales to each tag's noise; the % term is a floor for very-low-noise tags. Tighten for stable tags, loosen for noisy ones.
- **Persistence:** require ≥2 consecutive divergent bins. Transient one-bin divergence is almost always collection skew.
- **Quality gate:** only compare bins where *both* sources are Good quality. A Bad-quality direct read is a sensor/collector problem, not a spoof.

## Response
This is a **high-severity, low-false-positive** detection — divergence between two independent readings of the same physical value has few benign explanations. Treat a persistent, corroborated hit as a probable integrity compromise.
1. **Do not trust the HMI/historian value.** Assume the operator view may be fabricated.
2. **Do not act on the control system** from the compromised view.
3. Determine which source is anomalous: pull a third reading if available (redundant sensor E02, direct PLC tap).
4. Correlate with NDR: is there rogue-master / MITM activity (Nozomi) on the reporting path? Unexpected sessions to the OPC server or historian collector?
5. Escalate immediately per IR runbook — this is a candidate manipulation-of-view / spoofed-reporting incident. Consider it safety-relevant until proven otherwise.

## MITRE ATT&CK for ICS
- **T0832** — Manipulation of View
- **T0856** — Spoof Reporting Message

## Validation
See [`validation.md`](validation.md).
