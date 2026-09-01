# Changelog

All notable changes to this detection library are documented here.
Format follows Keep a Changelog; versioning is semantic.

## [0.1.0] - 2026-01-14
### Added
- Repository scaffold: README, catalog (32 use cases), docs, template, sample lookups.
- Architecture, baseline-methodology, data-model, and detection-lifecycle documentation.
- Six built detections: A01, B01, C01, D02, E01, G01 — each with SPL, KQL, YAML, and validation.
- Common data model for Splunk and Microsoft Sentinel.
- MITRE ATT&CK for ICS mapping across built detections.

### Notes
- All logic is read-only against historian data.
- Trip limits and baselines in `lookups/` are illustrative and must be replaced with site MOC-approved values.
