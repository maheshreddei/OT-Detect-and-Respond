# Architecture

This repository is a detection-content-as-code store for an OT SOC. It is built on one
idea: **the catalog is the source of truth, and everything else hangs off a use case ID.**

## Layers

```
                 +---------------------------------------------+
                 |          catalog/ (the spine)               |
                 |  use-case-catalog.csv  <-- master record    |
                 |     |        |        |         |           |
                 |  ATT&CK   threat    sector    Nozomi         |
                 |  coverage  actor    applic.   alert map      |
                 +----|--------|--------|---------|-------------+
                      |        |        |         |
        +-------------+        |        |         +--------------+
        |                      |        |                        |
   +----v-----+          +-----v----+   |                  +-----v------+
   | detections/|        | lifecycle/|  |                  |   docs/    |
   |  sigma/    |        | stages,   |  |                  | taxonomy,  |
   |  nozomi-   |        | RACI,     |  |                  | nozomi     |
   |  n2ql/     |        | templates |  |                  | taxonomy   |
   +------------+        +-----------+  |                  +------------+
                                        |
                              sector applicability
```

## The spine: `catalog/use-case-catalog.csv`

Every use case is one row with a stable `UC_ID` (OT-UC-00NN). That ID is the join key.
The row carries all four cross-reference dimensions inline so the master file answers most
questions on its own:

- **Threat** - `Threat_Actors` (Dragos / named groups)
- **ATT&CK for ICS** - `ATTACK_Tactic`, `ATTACK_Technique_ID`, `ATTACK_Technique`
- **Sector** - `Sectors`
- **Nozomi** - `Nozomi_Type_ID`

The pivot CSVs (`attack-ics-coverage.csv`, `threat-actor-coverage.csv`,
`sector-applicability.csv`, `nozomi-alert-mapping.csv`) are denormalized views of the same
truth, precomputed so you can hand a stakeholder the view they care about without a
database. When you add a UC, update the master row first, then the pivots.

## Detection artifacts

`detections/sigma/` holds portable Sigma rules; `detections/nozomi-n2ql/` holds Nozomi
N2QL queries and Assertion logic. Each artifact carries its own `uc_id` and
`nozomi_type_id` so a rule file is self-describing even when read in isolation. Sigma is
treated as the source format for anything portable and compiled to the SIEM backend
(Splunk SPL) downstream; Nozomi content lives in N2QL because it runs on the sensor.

## Why content-as-code, not console-only

Detection content that lives only in a platform console cannot be versioned, peer
reviewed, diffed, or moved between customer tenants. Keeping it here means: tuning changes
are commits, coverage is a query over the catalog, and the same content library seeds a
new MSS engagement on day one. The console is a deployment target, not the record.

## Adding content

1. Author from `lifecycle/use-case-template.md`.
2. Add the master row to `catalog/use-case-catalog.csv`, then the pivots.
3. Commit the detection artifact under `detections/` with `uc_id` set.
4. Fill `lifecycle/validation-test-plan-template.md`; move the stage forward only on
   evidence.
