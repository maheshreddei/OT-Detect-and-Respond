# Chapter 20 — Detection Engineering: Sigma, YARA, KQL

> Part IV. Detection engineering is where a hunt or an indicator becomes a durable, validated, versioned rule. This is how OT defense compounds over time instead of depending on one hunter's memory.

## 20.1 The discipline

A detection is a hypothesis about malicious activity, expressed as a rule, that fires on data. Detection *engineering* treats rules like software: **written, reviewed, version-controlled, tested, deployed, measured, and retired.** An unmanaged pile of rules decays; an engineered detection estate improves.

## 20.2 Rule formats — the right tool for the data

| Format | Runs on | Use for |
|--------|---------|---------|
| **Sigma** | Vendor-neutral → compiles to SIEM backends | Log-based detections as the source of truth |
| **KQL / SPL / ES\|QL** | Sentinel / Splunk / Elastic | SIEM-native queries and hunts |
| **Suricata / Snort** | Network sensor | Signature detection on the wire (Chapter 21) |
| **Zeek scripts** | Zeek | Behavioral network logic |
| **YARA** | Files / memory | Malware artifacts (DFIR, Chapter 26) |

**Sigma** is the keystone: write a detection once in Sigma, keep it under version control as the authoritative artifact, and compile it to whatever SIEM backends you run (Splunk, Sentinel, Elastic). This avoids maintaining the same logic three times and makes the estate portable.

## 20.3 Signature vs baseline detections

Two complementary styles:

- **Signature / rule** — matches a known-bad pattern (a specific function code from a non-master, a program-transfer, an IOC). Precise, low false-positive, fast — but blind to novel activity.
- **Baseline / deviation** — flags a statistical or allow-list deviation (a new conversation, a value outside its baseline, a rate anomaly). Catches the unknown — but needs a clean baseline and tuning.

OT leans on **both**: signatures for the well-defined protocol writes and known malware behaviors, baselines for the "something new in a stable environment" detections that OT's determinism makes powerful.

## 20.4 The detection lifecycle

```
  Hypothesis ─▶ Draft rule ─▶ Tune ─▶ Validate ─▶ Promote (shadow→active) ─▶ Maintain/Retire
   (from hunt/    (Sigma)    (thresholds/  (simulate the    (watch FPs)        (re-test on
    IOA/intel)               allow-lists)   technique)                          change; retire stale)
```

The step teams skip is **validate** — proving the rule actually fires on the technique it targets, with the right fields, within an acceptable time, and without flooding on normal activity. A rule that has never been tested is a hypothesis, not a control. (This is exactly the Threat Detection Assurance discipline: log validation, logic testing, blind-spot discovery, false-positive reduction, and MTTD.)

## 20.5 Good-rule practices

- **Map every rule to ATT&CK** (ICS or Enterprise) and record its data source and severity.
- **Name the data dependency** — a rule is only real if its log source is feeding.
- **Tune with the allow-lists** — exclude known-good (service accounts, backup windows, vuln scanners) rather than loosening the core logic.
- **Pair OT writes with a historian check** — so an alert distinguishes a probe from an actual process change.
- **Version and review** — treat rule changes like code changes.

## Chapter summary
- Detection engineering treats rules like **software**: written, reviewed, versioned, tested, measured, retired.
- **Sigma** is the vendor-neutral source of truth; compile to SIEM backends; use YARA for files/memory, Suricata/Snort/Zeek for network.
- Use **signature and baseline** styles together; OT's stability makes baseline detections powerful.
- Run the **lifecycle** and never skip **validation** — an untested rule is a hypothesis.
- Map to ATT&CK, name the data dependency, tune with allow-lists, and pair writes with a historian check.

## Cross-references
- Chapter 16 (hunts feed rules), Chapter 17 (process-indicator rules), Chapters 21–22 (network/SIEM), Chapter 19 (the logs rules run on).
- Companion: `ot-detection-engineering` (87 Sigma rules), `threat-detection-assurance` (validation).
