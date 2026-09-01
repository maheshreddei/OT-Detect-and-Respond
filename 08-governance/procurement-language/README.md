# ICS/OT Cyber Security Procurement Language

**A browsable, GitHub-native rendering of the DHS/ICS-CERT _Cyber Security Procurement Language for Control Systems_ (September 2009) — 47 control requirements you can drop into RFPs and contracts, mapped to modern standards.**

![Source](https://img.shields.io/badge/source-DHS%20%2F%20ICS--CERT%202009-blue)
![Controls](https://img.shields.io/badge/controls-47%20across%2012%20categories-brightgreen)
![Use](https://img.shields.io/badge/use-RFP%20%2F%20contract%20requirements-orange)
![Mapped](https://img.shields.io/badge/mapped-NIST%20800--82r3%20%7C%20IEC%2062443%20%7C%20CSF%202.0-lightgrey)
![License](https://img.shields.io/badge/license-US%20Gov%20public%20domain-green)

---

## What this document is about

Securing a control system doesn't start at deployment — it starts at **procurement**. Most ICS/OT security debt is bought, not built: it arrives baked into products and integration contracts that never specified security in the first place. This document exists to fix that at the source. It gives asset owners **ready-to-use contractual language** — the actual "the Vendor shall…" clauses — to put security requirements into RFPs, bids, and contracts when buying or integrating SCADA, DCS, PCS, and other control systems.

It was produced by the U.S. Department of Homeland Security Control Systems Security Program (with Idaho National Laboratory, NY State CISO, and the SANS Institute), drawing on a workgroup of 242 public- and private-sector organizations. It is a foundational reference in OT security procurement and remains a practical clause library today.

A framing idea runs through it: for control systems the classic security priorities **invert**. The document is explicit that the order is **Availability → Integrity → Confidentiality** — a SCADA operator needs the system available and the readings trustworthy far more than they need secrecy, because most process data is only valid for the instant it's produced. Full framing in [`docs/00-about.md`](docs/00-about.md).

## What it covers

**12 control categories, 47 individual controls**, each written as an 8-part template so a requirement is not just a "shall" statement but a testable, maintainable obligation. See the full index below and the per-category files in [`catalog/`](catalog/).

| # | Category | Controls | What it addresses |
|---|----------|----------|-------------------|
| 2 | [System Hardening](catalog/02-system-hardening.md) | 6 | Removing unnecessary services, host IDS, FS/OS permissions, hardware config, heartbeat signals, patching |
| 3 | [Perimeter Protection](catalog/03-perimeter-protection.md) | 3 | Firewalls, network IDS, canaries |
| 4 | [Account Management](catalog/04-account-management.md) | 7 | Default/guest accounts, session mgmt, passwords/auth, auditing, RBAC, SSO, separation |
| 5 | [Coding Practices](catalog/05-coding-practices.md) | 1 | Secure coding requirements for delivered software |
| 6 | [Flaw Remediation](catalog/06-flaw-remediation.md) | 2 | Vendor vulnerability notification & problem reporting |
| 7 | [Malware Detection & Protection](catalog/07-malware-detection-and-protection.md) | 1 | Anti-malware controls suited to control systems |
| 8 | [Host Name Resolution](catalog/08-host-name-resolution.md) | 1 | Network addressing & name-resolution security |
| 9 | [End Devices](catalog/09-end-devices.md) | 4 | IEDs, RTUs, PLCs, sensors/actuators/meters |
| 10 | [Remote Access](catalog/10-remote-access.md) | 6 | Dial-up & dedicated modems, TCP/IP, web interfaces, VPNs, serial comms |
| 11 | [Physical Security](catalog/11-physical-security.md) | 4 | Physical access to cyber components, perimeter, manual override, intraperimeter comms |
| 12 | [Network Partitioning](catalog/12-network-partitioning.md) | 2 | Network devices, network architecture/segmentation |
| 13 | [Wireless Technologies](catalog/13-wireless-technologies.md) | 10 | Bluetooth, Wi-Fi, ZigBee, WirelessHART, RFID, mobile radio, mesh, cellular, WiMAX, microwave/satellite |

A machine-readable list of every control is in [`catalog/requirements-index.csv`](catalog/requirements-index.csv) — use it to build an RFP checklist or a compliance matrix.

## The 8-part topical template

Every control is structured identically, which is what makes it usable as a requirements library rather than just advice:

| Part | Purpose |
|------|---------|
| **Basis** | Why the control matters — the risk it addresses |
| **Language Guidance** | Context and how to tailor the requirement |
| **Procurement Language** | The actual clause to put in the RFP/contract |
| **FAT Measures** | How to verify it at Factory Acceptance Test |
| **SAT Measures** | How to verify it at Site Acceptance Test |
| **Maintenance Guidance** | Keeping the control effective over the system life |
| **References** | Supporting standards/sources |
| **Dependencies** | Other controls this one relies on |

Details in [`docs/topical-template.md`](docs/topical-template.md).

## How to use it today

1. **Build an RFP security section.** Pull the *Procurement Language* from the relevant controls into your tender; tailor per *Language Guidance*.
2. **Define acceptance criteria.** Use the *FAT/SAT Measures* as the verification tests your contract requires the vendor to pass.
3. **Create a requirements matrix.** Start from [`catalog/requirements-index.csv`](catalog/requirements-index.csv); track each control's inclusion, vendor response, and test result.
4. **Map to your framework.** Use [`docs/standards-mapping.md`](docs/standards-mapping.md) to align each category to NIST SP 800-82 Rev 3, IEC 62443, and NIST CSF 2.0 so procurement traces to your control catalog.

## Historical note

This is the September 2009 edition. It predates much of the modern OT-security standards landscape, and a few technology specifics (wireless protocols especially) have aged — but the **procurement discipline and the clause structure remain directly useful**. Treat it as a foundational clause library and pair it with current standards: **IEC 62443-4-1/-4-2** (secure product development and component requirements), **NIST SP 800-82 Rev 3**, and current CISA/INL procurement guidance. [`docs/standards-mapping.md`](docs/standards-mapping.md) bridges the two.

## Repository structure

```
ics-procurement-language/
├── README.md
├── docs/
│   ├── 00-about.md            ← what it is, origin, security-objectives framing
│   ├── topical-template.md    ← the 8-part control template explained
│   └── standards-mapping.md   ← categories → NIST 800-82r3 / IEC 62443 / CSF 2.0
├── catalog/
│   ├── 02-system-hardening.md … 13-wireless-technologies.md   ← the 47 controls
│   └── requirements-index.csv ← machine-readable control list
└── source/
    └── Cyber_Security_Procurement_Language_for_Control_Systems_Sept2009.pdf
```

## License & attribution

The source document is a work of the U.S. Federal Government (DHS/ICS-CERT) and is in the **public domain**. This repository reproduces and reformats it for accessibility; the markdown rendering and the standards-mapping analysis are provided under MIT. See [`LICENSE`](LICENSE).

> Rendered from the OCR text layer of the source PDF. For any contractual use, verify wording against the authoritative [`source/`](source/) PDF.
