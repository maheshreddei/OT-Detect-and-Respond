# Architecture — The Relational Model

This repository is one system, not a folder of documents. Every layer is joined to the
next by a stable ID, and the joins are **generated and validated**, never hand-maintained.
That is the whole design: you can start at a threat and walk down to the SPAN port, or
start at a budget line and walk up to the techniques it buys you.

## The chain

```
   THREAT                                                        BUDGET
      |                                                             |
      v                                                             v
  +--------+     +--------+     +--------+     +--------+     +---------+
  |   UC   |<----|   LS   |<----|  TEL   |<----|   CP   |<----|   MVT   |
  +--------+     +--------+     +--------+     +--------+     +---------+
  use case      log source     telemetry      collection    minimum viable
  (detection)   (onboarding)   (hunt value)   (deployment)  (budget order)
      |              |
      v              v
   ATT&CK        parser /
   for ICS       CIM mapping
   + Nozomi
   type_id
```

Read **right to left** and it answers "I have limited budget — what do I get?"
Read **left to right** and it answers "I need to detect this — what must I collect?"

## The five ID namespaces

| Prefix | Layer | Count | Question it answers | File |
|--------|-------|-------|---------------------|------|
| `OT-UC-####` | Detection | 28 | What are we trying to catch? | `02-detection/catalog/use-case-catalog.csv` |
| `LS-##` | Log source | 19 | What can we realistically onboard, in what order? | `01-telemetry/log-source-inventory.csv` |
| `TEL-##` | Telemetry | 14 | What is worth the most for hunting? | `01-telemetry/telemetry-hierarchy.csv` |
| `CP-##` | Collection plan | 14 | What do we deploy, and how? | `01-telemetry/collection-plan.csv` |
| `MVT-#` | Minimum viable | 7 | If we start from nothing, what order? | `01-telemetry/minimum-viable-telemetry.csv` |

## Why three telemetry views, not one

`TEL`, `CP`, and `LS` describe the same equipment through three different lenses, and they
deliberately disagree. That disagreement is the useful part:

- **TEL ranks by hunt value.** Network metadata is rank 1 because it sees what agents
  cannot.
- **CP ranks by deployment priority.** The IDMZ firewall is priority 1 because it is the
  best log per unit of effort.
- **LS ranks by onboarding tier.** Network traffic drops to Tier 3 because SPAN/TAP
  architecture and DPI tuning are a project, not a config change.

Network monitoring is simultaneously **the highest-value source and one of the last to
arrive**. Any single view hides that. Holding all three is what lets you tell a customer
"this is the most valuable thing you can build, and it is also the thing that will take
longest — here is what to do in the meantime." `MVT` is the answer to that "meantime".

## Generated joins

`05-crosswalk/` is **build output**. Do not edit it by hand.

| File | Derived from | What it shows |
|------|--------------|---------------|
| `telemetry-to-logsource.csv` | TEL + CP + MVT + LS | Each telemetry source resolved to onboardable log sources, with tier and pattern |
| `master-crosswalk.csv` | UC + linkage + TEL + LS | Every use case with its full chain: technique, actor, Nozomi type, sources, tiers |
| `coverage-rollup.csv` | LS + linkage + UC | What each log source unlocks — use case count and distinct ATT&CK techniques |

Regenerate with `python3 tools/build_crosswalk.py`, verify with `python3 tools/validate.py`.

## What validation enforces

`tools/validate.py` is the guarantee that the model holds. It checks:

1. **CSV structure** — consistent column counts across every file.
2. **Referential integrity** — every `TEL -> LS`, `CP -> TEL/LS`, `MVT -> CP/LS`, and
   `LS -> UC` reference resolves to a real ID.
3. **Parser coverage** — `parser-mapping.csv` covers exactly the LS universe, no
   duplicates, no gaps.
4. **Orphans** — log sources feeding no use case, and use cases with no collectable
   source. The second is the serious one: *a detection with no data source is a plan, not
   a detection.*
5. **Sigma linkage** — every rule parses, carries required fields, and its `uc_id`
   resolves to a catalog entry.

The build currently reports exactly one orphan warning — `LS-19` (Field I/O) feeds no use
case. That is correct and intentional: Field I/O is Tier 4, never collected, represented
indirectly through PLC/RTU and historian. An expected orphan documented as expected is
different from an unnoticed gap.

## Adding content

1. New use case: author from `00-program/use-case-template.md`, add the row to
   `use-case-catalog.csv`, update the pivots, and **map it to at least one `LS`** in
   `05-crosswalk/detection-to-logsource.csv` — otherwise validation flags it as
   uncollectable.
2. New log source: add to `log-source-inventory.csv` and `parser-mapping.csv` (both, or
   validation fails), tier it using `docs/log-source-methodology.md`, then link it.
3. Rebuild and validate. Both must pass before commit.
