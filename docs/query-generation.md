# Query Generation

Every detection in the master catalog has a Sentinel KQL query and a Splunk SPL query.
This document explains how they are produced, what the provenance labels mean, and what
must be changed before deployment.

## Provenance — three classes, tracked per detection

`02-detection/catalog/query-index.csv` records `Query_Origin` for all 257 detections:

| Origin | Count | Meaning |
|--------|------:|---------|
| `compiled-from-sigma` | 90 | Real compilation from the Sigma rule's `detection` block |
| `authored` | 6 | Hand-written by the author (historian family); referenced, never overwritten |
| `scaffold` | 161 | The detection is a **specification**; the query carries intent but is not complete |

**The distinction is the point.** A scaffold presented as a production query is how a
detection program acquires silent false negatives — the query runs, returns nothing, and
everyone assumes coverage. Every scaffold file states its status in its header, and
`tools/validate.py` reports the scaffold count as a standing warning so it cannot be
forgotten.

## What the compiler actually does

`tools/generate_queries.py` is a real multi-target compiler, not a template filler. From a
Sigma `detection` block it handles:

- **Selection vs filter blocks** — any block named `filter*`, `authorized*`, `allow*`, or
  `exclu*` is treated as a negation and emitted as `| where not (...)` in KQL and `NOT (...)`
  in SPL. Getting this backwards inverts the detection, so it is explicit rather than
  positional.
- **List membership** — `field: [a, b, c]` becomes `field in ("a","b","c")` in KQL and an
  `OR` group in SPL.
- **Sigma modifiers** — `|contains`, `|startswith`, and `|cidr` each map to the correct
  target syntax (`contains`, `startswith`, `ipv4_is_in_range` in KQL; wildcard forms in SPL).
- **Field mapping** — Zeek/ICSNPP and Sigma field names are translated through `FIELD_MAP`
  to each target's schema (`id.orig_h` → `SourceIP` / `src_ip`, `function_code` →
  `FunctionCode` / `function_code`, and so on).
- **Source mapping** — the rule's logsource selects a table (Sentinel) and index/sourcetype
  (Splunk) from `SOURCE_MAP`, so Modbus traffic and Windows events do not compile to the
  same place.
- **Timeframe** — Sigma aggregation windows are emitted as a `summarize` with the original
  timeframe preserved in a comment, since threshold semantics differ per platform and should
  be reviewed rather than silently translated.

## What you must change before deployment

**1. Schema mapping.** `SOURCE_MAP` and `FIELD_MAP` in `tools/generate_queries.py` declare
the target schema. They are written for a plausible OT deployment (custom `OTNetwork_CL`,
`OTHistorian_CL`, `OTNozomi_CL` tables in Sentinel; `index=ot_network` with Zeek sourcetypes
in Splunk). Point them at your real tables and regenerate — do not hand-edit 514 query files.

**2. Placeholders.** Queries contain `<ANGLE BRACKET>` placeholders and inline allowlists
with example addresses (`10.20.30.11`, `10.20.0.0/16`). These are the environment-specific
values — authorized masters, engineering workstations, zone CIDRs, tag prefixes, thresholds.
**A query that still contains placeholders will execute but will not be correct.** Baseline
them first; that baselining is the real onboarding work.

**3. Scaffold completion.** The 161 scaffolds each carry the detection's intent in a `TODO`
comment. Completing one means expressing that intent against your actual schema and
validating it with `00-program/validation-test-plan-template.md`.

## Regenerating

```bash
python3 tools/build_catalog.py      # rebuild the master catalog first
python3 tools/generate_queries.py   # then regenerate all queries
python3 tools/build_crosswalk.py    # then the crosswalk that indexes them
python3 tools/validate.py           # verify
```

Queries are build output. Edit the Sigma rule or the field mappings, not the generated file
— anything hand-edited in `02-detection/queries/` is overwritten on the next build. The one
exception is the historian family, whose hand-authored queries live beside their
`detection.yml` and are referenced rather than regenerated.
