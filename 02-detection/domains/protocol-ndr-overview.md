# Detection Catalog

Every detection idea from the protocol pages, consolidated into one machine-readable list: [`source-libraries/protocol-ndr-catalog.csv`](../../source-libraries/protocol-ndr-catalog.csv).

Columns: `id, protocol, detection, pattern, logic, log_source, attack_ics, severity`.

- **pattern** is one of the five reusable patterns from [`docs/protocol-attack-surface-model.md`](../../docs/protocol-attack-surface-model.md): `unauthorized-client`, `recon`, `write-command`, `disruptive-function`, `baseline-deviation`.
- **log_source** names the feed the detection needs — cross-check against [`docs/protocol-ndr-log-sources.md`](../../docs/protocol-ndr-log-sources.md) to find telemetry gaps.
- **severity** is a starting point; tune to your asset criticality (a write to a safety point outranks the same write elsewhere).

## Using the catalog
1. Filter to the protocols present in your environment.
2. Sort by `severity` and start with the `write-command` and `disruptive-function` rows — highest value, closest to true-positive.
3. Confirm you have each `log_source`; where you don't, that's a telemetry backlog item.
4. Implement in your NDR (many ship as built-in policies) or as SPL/KQL against Zeek/ICSNPP fields.
5. Pair every `write-command`/`disruptive-function` detection with a historian impact check.

The five patterns mean these are largely the same detections re-instantiated per protocol — build the pattern once, apply the protocol-specific fields from each page.
