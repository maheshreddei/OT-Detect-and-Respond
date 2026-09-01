# About This Document

## Origin
*Cyber Security Procurement Language for Control Systems* was produced by the U.S. Department of Homeland Security Control Systems Security Program, in partnership with Idaho National Laboratory, the Chief Information Security Officer of New York State, and the SANS Institute. The effort began in March 2006 and drew on a workgroup of **242 public- and private-sector organizations** — asset owners, operators, regulators — plus 20+ vendors. This repository renders the **September 2009** edition.

## Purpose
The premise is simple and still under-applied: **security in control systems is most cheaply and effectively established at the point of purchase.** Once a SCADA/DCS/PCS product or integration contract is signed without security requirements, the owner inherits whatever the vendor shipped — and retrofitting security into a running, safety-critical process is far harder and riskier than specifying it up front.

The document supplies **common, reusable procurement language** so that federal, state, local, and private asset owners can:
- put concrete security requirements into RFPs, bids, and contracts,
- hold vendors and integrators to a testable standard (via Factory and Site Acceptance Tests), and
- arrive at a shared owner/vendor understanding of "secure enough" for control systems.

## Audience
Asset owners and operators writing procurements; integrators responding to them; and the security engineers who translate risk into contract requirements. It is a **procurement and contracting** tool, not an operational runbook.

## The security-objectives framing (why control systems are different)
The document opens by grounding everything in security objectives — and makes the point that for control systems these are prioritized **differently from enterprise IT**:

- **Availability — highest priority.** Control systems operate in near-real-time on physical processes and life-safety systems; loss of availability can have immediate physical consequences. A denial-of-service condition that would be an inconvenience in IT can be a safety event in OT.
- **Integrity — second.** Operators act on the readings and status the system reports; if that data can't be trusted, correct action is impossible. Because legacy control systems rarely implemented role-based access control, the document deliberately folds **authentication, authorization, and access control under Integrity**.
- **Confidentiality — lowest, usually.** Most control-system data is state-based and valid only for an instant (a setpoint is superseded within seconds), unlike an IT secret such as a credit-card number that stays sensitive for years. Confidentiality still matters for selected uses (e.g. market-facing data, where non-repudiation is also relevant), but it is not the driver.

This inversion — **Availability → Integrity → Confidentiality** — is the lens for reading every control that follows, and it remains one of the clearest one-paragraph explanations of why OT security is its own discipline.

## How the content is organized
The body is a catalog of control categories; each category contains individual controls; each control is written to a fixed **8-part topical template** (Basis, Language Guidance, Procurement Language, FAT Measures, SAT Measures, Maintenance Guidance, References, Dependencies). That structure is what turns guidance into contractable, verifiable requirements — see [`topical-template.md`](topical-template.md).

## Status and modern context
As a 2009 document it predates most current OT-security standards, and some technology specifics have dated. Its **procurement discipline, clause structure, and FAT/SAT verification model remain directly useful.** Pair it with IEC 62443-4-1/-4-2, NIST SP 800-82 Rev 3, and current CISA/INL procurement guidance — bridged in [`standards-mapping.md`](standards-mapping.md).
