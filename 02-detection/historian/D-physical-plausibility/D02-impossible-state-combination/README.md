# D02 — Impossible State Combination

## Problem
Individual tags can each look plausible while their *combination* is physically impossible — and physics doesn't lie. A pump reporting OFF while its downstream flow transmitter reads healthy flow; a valve reporting CLOSED while differential pressure builds across it; a heater OFF while temperature climbs. An impossible pair means at least one value is wrong — a spoofed reading, a manipulated I/O image, or a serious instrument fault. Because it cross-checks *independent* tags against a physical law, it's hard for an attacker to satisfy without manipulating every tag in the relationship consistently.

## Detection concept
A small rules table encodes known impossible combinations as `(condition_A AND condition_B)` that must never be simultaneously true. The detection aligns the participating tags to a common time bin and fires when a forbidden combination holds. Each rule is a physical invariant of the plant, authored with the process engineer.

Example rule (shipped): **pump `P101` RUN=0 (off) AND downstream flow `FT201` > 5 m³/h** ⇒ impossible.

## Data required
- The participating discrete/status and analog tags per [`docs/historian-data-model.md`](../../../../docs/historian-data-model.md)
- A site-specific rules table of impossible pairs (illustrated inline in the query; externalize to a `state_rules.csv` lookup as the rule count grows)

## Logic
- Splunk: [`splunk.spl`](splunk.spl)
- Sentinel: [`sentinel.kql`](sentinel.kql)

## Tuning
- **Author rules with the process engineer.** Each rule is a claimed physical impossibility; a wrong claim is a guaranteed false positive. Start with a handful of high-confidence invariants.
- **Allow transition windows.** A pump just commanded off may show residual flow for seconds. Add a short dwell so momentary, physically-real transients don't fire.
- **Bin alignment matters** — compare the two tags within the same small time bin so you're not pairing stale samples.
- Externalize rules to a lookup once you have more than a few; keep each rule versioned and attributed.

## Response
1. Identify which tag in the pair is the liar: corroborate each against an independent source (E01) or a redundant sensor (E02).
2. A spoofed status/analog value is an integrity incident (manipulate I/O image); a genuine instrument fault is a maintenance ticket — but treat as incident until integrity is confirmed.
3. Correlate with NDR for I/O-image or reporting manipulation on the affected controller.

## MITRE ATT&CK for ICS
- **T0835** — Manipulate I/O Image
- **T0831** — Manipulation of Control

## Validation
See [`validation.md`](validation.md).
