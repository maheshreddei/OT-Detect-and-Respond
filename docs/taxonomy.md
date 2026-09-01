# Cross-Reference Taxonomy

The catalog is organized on a **hybrid spine**: threat-informed and ATT&CK-for-ICS-mapped
at the same time, with sector and Nozomi alert as two further axes. This document defines
each axis and how they resolve against one another.

## Axis 1 - Threat (who)

Use cases are anchored to real adversaries so the library is threat-informed rather than
generic. Actors follow Dragos activity-group naming where possible, with common aliases in
`threat-actor-coverage.csv`. Anchoring to an actor answers "why do we detect this" and lets
you prioritize by the threat landscape of a given customer or sector.

Actors currently referenced: ELECTRUM, KAMACITE, CHERNOVITE, XENOTIME, BAUXITE, VOLTZITE,
GRAPHITE, DragonFly.

## Axis 2 - ATT&CK for ICS (what technique)

Every use case maps to exactly one primary ATT&CK for ICS technique (`T0NNN`) under its
tactic. This is the interoperability layer: it is how coverage is measured, how gaps are
communicated, and how this library aligns to any other ATT&CK-mapped tooling. Coverage
against the ICS matrix is tracked in `attack-ics-coverage.csv`, qualified by lifecycle
stage - a technique covered only by Proposed use cases is a gap, not coverage.

## Axis 3 - Sector (where)

Detection value is sector-dependent. IEC 61850 GOOSE matters in an electric substation and
nowhere else; SIS key-switch monitoring matters in oil & gas and chemical. The
`sector-applicability.csv` matrix marks each UC against Electric, Oil & Gas,
Water/Wastewater, Manufacturing, Chemical, Building Automation, and Transportation, so a
per-customer content set is a filter, not a rewrite.

## Axis 4 - Nozomi alert (how it surfaces)

Each UC is mapped to the Nozomi detection mechanism and Type ID that would raise it
(`nozomi-alert-mapping.csv`), and whether Guardian raises it natively or needs a custom
Assertion / N2QL. See `nozomi-alert-taxonomy.md` for the Type ID convention.

## How the axes resolve together

The axes are not independent - the useful intelligence is in their intersection. A worked
example, OT-UC-0009:

- **Threat:** ELECTRUM (Industroyer / Industroyer2 abused exactly this command class)
- **ATT&CK:** T0855 Unauthorized Command Message (Impair Process Control)
- **Sector:** Electric (and Transportation signalling)
- **Nozomi:** PROT:IEC104-ILLEGAL, protocol validation, native + tuning Assertion
- **Detection:** `detections/sigma/iec104-unauthorized-control.yml`

Read across the row and you have the whole story: a named adversary, the technique they
use, the sectors where it applies, how your sensor surfaces it, and the portable rule that
detects it. That is the point of the hybrid spine - any single axis is a weak organizing
principle on its own, but the intersection is what a lead-level program is actually
managing.

## A useful property: Nozomi already speaks ATT&CK for ICS

Nozomi alerts natively carry MITRE ATT&CK for ICS technique and tactic fields (for
example, a malware alert emits the technique in the CEF/syslog record). That means Axis 2
and Axis 4 are not just conceptually linked - the technique mapping can be lifted straight
off the alert at ingestion time and used to auto-populate coverage. Where the
`ATTACK_ICS_Native` column in the Nozomi mapping reads Yes, the SIEM can derive the ATT&CK
tag from the alert itself rather than from a static lookup.
