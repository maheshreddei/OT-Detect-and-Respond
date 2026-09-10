# IEC 62443-3-3 FR, SR and RE Implementation Framework

This folder provides a complete identifier-level implementation register for IEC 62443-3-3:2013, including the 2014 corrigendum affecting SR 3.4.

## Coverage check

| Type | Count |
|---|---:|
| Foundational Requirements | 7 |
| Base System Requirements | 51 |
| Requirement Enhancements | 49 |
| Total SR/RE rows | 100 |

The register uses original, concise implementation summaries. It does not reproduce the licensed normative requirement language, rationale, supplemental guidance or full Annex B. Obtain the official standard for a formal assessment.

[Open the requirements register](requirements-register.csv)

## Seven Foundational Requirements

| FR | Code | Practical objective | Petrochemical example |
|---|---|---|---|
| FR 1 | IAC | Identify and authenticate users, devices and processes | Named DCS/EWS accounts, MFA for vendor access, device certificates |
| FR 2 | UC | Authorize and audit permitted actions | Operator/engineer roles, controlled overrides, session and audit policy |
| FR 3 | SI | Preserve system and communication integrity | Signed updates, validation, malware controls, safe failure behavior |
| FR 4 | DC | Protect sensitive information | Credentials, configurations, recipes and remote sessions |
| FR 5 | RDF | Restrict communications through zones and conduits | DCS/SIS separation, IDMZ, deny-by-default firewall rules |
| FR 6 | TRE | Detect, record and respond to security events | Nozomi, SIEM, accessible logs and OT incident workflow |
| FR 7 | RA | Maintain essential availability and recovery | Backup/restore, UPS, DoS resistance, capacity and inventory |

## How the hierarchy works

- **FR** states the broad security outcome.
- **SR** states a system-level capability within an FR.
- **RE** strengthens a parent SR for higher adversary capability.
- **SL-T** is the target security level selected from risk assessment for a zone or conduit.
- **SL-C** is the capability a system can provide.
- **SL-A** is the level achieved in the implemented environment.

Treat the security level as a seven-element vector, one value per FR, rather than automatically giving an entire plant one uniform number.

## Register fields

- `Minimum_SL_C`: first capability level at which the row appears in the Annex B mapping.
- `Implementation_Summary`: non-normative paraphrase for design workshops.
- `Petrochemical_Evidence_Examples`: starting evidence examples, not proof by themselves.
- `Assessment_Status`: use Not assessed, Meets, Partially meets, Does not meet or Not applicable with approved rationale.
- `Gap`: precise missing capability or evidence.
- `Compensating_Countermeasure`: documented alternative where the direct requirement cannot be implemented.
- `Owner`, `Evidence_Link`, `Review_Date`: accountability and traceability.

## Assessment workflow

1. Define the System under Consideration.
2. Identify assets, process consequences, safety dependencies and operating modes.
3. Define zones and conduits.
4. Perform IEC 62443-3-2 risk assessment and assign an SL-T vector to each zone/conduit.
5. Filter the register to rows whose minimum SL-C is at or below the relevant SL-T.
6. Evaluate architecture, configuration, procedures and test evidence.
7. Record gaps and compensating countermeasures.
8. Validate that a compensating measure delivers equivalent risk reduction without harming safety or availability.
9. Derive SL-A only from verified implementation—not plans or product claims.
10. Approve residual risk, remediation and periodic reassessment.

## Petrochemical design cautions

- Do not force enterprise authentication into fragile PLC/SIS components if it can impair safe operation; use engineered compensating controls.
- Do not assume a certified component makes a zone compliant.
- Do not equate a firewall rule with a complete conduit.
- Do not use Nozomi presence as proof that every FR is satisfied.
- Do not select SL-T from preference. Base it on zone/conduit risk.
- Coordinate cybersecurity changes through process safety and MOC.
- Apply the IEC 62443-3-3 corrigendum: SR 3.4 base begins at SL 2 in the corrected mapping.

## Validation sources

- [IEC official preview and scope](https://webstore.iec.ch/en/iec_catalog/product/preview/?id=L3B1Yi9wZGYvcHJldmlldy9pbmZvX2llYzYyNDQzLTMtM3tlZDEuMH1iLnBkZg%3D%3D)
- [IEC 62443 overview](https://syc-se.iec.ch/deliveries/cybersecurity-guidelines/security-standards-and-best-practices/iec-62443/)
- [IEC corrigendum](https://webstore.iec.ch/en/publication/7032)
- [ISA standards series](https://www.isa.org/standards-and-publications/isa-standards/isa-iec-62443-series-of-standards)

IEC 62443-3-3 has a stability date, edition and licensing status controlled by IEC. Confirm the applicable edition, national adoption, contract and certification scheme before formal use.
