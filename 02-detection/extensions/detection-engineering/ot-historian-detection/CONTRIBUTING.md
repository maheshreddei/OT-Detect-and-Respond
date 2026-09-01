# Contributing

## Adding a new detection

1. Copy `templates/detection-template/` to `detections/<FAMILY>/<ID>-<slug>/`.
2. Fill in all five files. A detection is not "done" without a passing `validation.md`.
3. Use the common data model (`docs/data-model.md`) field names. Don't invent new field names unless the detection needs a source your data model lacks — if so, extend the data model doc too.
4. Map to MITRE ATT&CK for ICS in `detection.yml` and add the row to `catalog.md` and the README catalog table.
5. Keep everything **read-only**. No detection may write to a control system, ever.

## Detection quality bar

- Baseline is **segmented by mode** (or documents why not).
- Query filters `quality == "Good"` unless the detection is about quality itself.
- Persistence / dwell logic present to control false positives.
- `validation.md` has at least one positive, one negative, and one edge case.
- `level` in the YAML reflects **process consequence**, not just statistical rarity.

## Style

- Detection IDs: `<FamilyLetter><NN>` (e.g. `A03`, `G02`).
- Folder slug: kebab-case, short.
- SPL and KQL are commented; a reviewer should understand the logic without running it.
- Thresholds live in lookups/watchlists, not hardcoded in queries, wherever practical.

## Review

Every detection change re-opens validation and requires OT Security Lead sign-off before production (see `docs/detection-lifecycle.md`).
