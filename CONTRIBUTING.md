# Contributing

## Adding a detection

1. Author from `00-program/use-case-template.md`.
2. If it has portable logic, write a Sigma rule under `02-detection/sigma/<library>/`.
3. Add it to the appropriate source catalog, or the use-case catalog if threat-informed.
4. Run the build chain — **never hand-write files in `02-detection/queries/` or
   `05-crosswalk/`**, they are generated:

```bash
python3 tools/build_catalog.py
python3 tools/generate_queries.py
python3 tools/build_crosswalk.py
python3 tools/validate.py
```

5. Validate against real telemetry using `00-program/validation-test-plan-template.md`
   before moving its status past In-Development.

## Merging duplicates

If a new detection duplicates an existing one, add the pair to `MERGE_MAP` in
`tools/build_catalog.py` **with a written rationale** — the rationale is emitted to
`merge-log.csv` and is the audit trail. Compare logic, not titles. Two detections that share
a name but differ in vantage point (IT flow vs OT NDR) or protocol are **not** duplicates.

## Adding a playbook

Copy `04-response/playbooks/PLAYBOOK-TEMPLATE.md`. All sections are mandatory and the
validator enforces them: Trigger, Severity guide, Safety check, Investigate (passive),
Decide, Respond (only with sign-off), Close.

Two rules: **Investigate steps must be read-only** — anything that writes, resets, or
disconnects belongs in Respond behind sign-off. And the **Safety check must be specific** to
this alert class, not a restatement of the standing doctrine.

## Before you commit

`python3 tools/validate.py` must exit 0. CI runs the full chain and fails if the generated
layer is stale.
