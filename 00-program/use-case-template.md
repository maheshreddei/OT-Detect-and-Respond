# Use Case Template

Copy this file to author a new use case. When complete, add a corresponding row to
`catalog/use-case-catalog.csv` and the relevant pivot CSVs. Keep the prose here; keep the
structured fields in the CSVs so they stay queryable.

---

## Identity

- **UC ID:** OT-UC-00NN
- **Title:**
- **Category:** (Access / Control / Recon / Denial / Evasion / Malware / C2 / Exfil / Safety)
- **Author:**
- **Version:** 1.0
- **Lifecycle stage:** Proposed

## Threat anchor (hybrid spine)

- **ATT&CK for ICS tactic:**
- **ATT&CK for ICS technique:** T0NNN - <name>
- **Threat actors / groups:** (Dragos or named group; link to `threat-actor-coverage.csv`)
- **Campaign / precedent:** (real incident or toolkit that motivates this UC, if any)

## Environment scope

- **Sectors:** (link to `sector-applicability.csv`)
- **Purdue level:**
- **Protocol(s):**
- **Affected asset types:** (PLC / RTU / HMI / historian / EWS / SIS / gateway)

## Detection

- **Primary data source:**
- **Detection type:** Sigma / N2QL / Native / Hybrid
- **Detection reference:** (path under `detections/`)
- **Nozomi Type ID / mechanism:** (link to `nozomi-alert-mapping.csv`)
- **Native vs Assertion:** (does Guardian raise this out of the box, or is a custom
  Assertion / N2QL required?)

## Logic summary

Describe, in plain language, what condition raises the alert and why it is high-signal in
OT. State the baseline assumption explicitly (e.g. "authorized master list", "learned
node inventory") because that assumption is where the false-positive risk lives.

## Expected fidelity and severity

- **Severity:**
- **Expected fidelity:** High / Medium / Low
- **Known benign causes:** (maintenance, commissioning, backup control center, scanners)

## Response pointer

- **SOC runbook reference:**
- **OT-specific caution:** (what an IT-trained analyst might get wrong here - e.g. do not
  isolate a controller mid-process; safety and availability rank above containment)

## Validation

- **Test plan:** (link to a filled copy of `validation-test-plan-template.md`)
- **Validation status:**
