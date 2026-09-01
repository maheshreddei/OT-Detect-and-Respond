# Contributing

This repo holds two kinds of detection content, each with its own conventions:

## Sigma libraries (`sigma-libraries/`)
- One rule per `.yml` under `<library>/rules/`.
- Keep `status: experimental` until validated; promote to `test`/`stable` after review.
- Use ICSNPP/Nozomi field names; keep placeholder allow-lists commented inline.
- Add the rule to the library's `README.md` index and tag it with ATT&CK for ICS.

## Historian detections (`ot-historian-detection/`)
- Follow that folder's own `CONTRIBUTING.md` and `templates/detection-template/`.
- Baseline segmented by mode; queries filter Good quality; ship a `validation.md`.

## Both
- Detections are **read-only**. Nothing writes to a control system.
- Scrub site-specific tags, subnets, and customer identifiers before committing.
- Map new detections to telemetry in `docs/mitre-ics-data-sources.md`.
