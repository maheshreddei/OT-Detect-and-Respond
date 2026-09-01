# IT/OT Incident Response & Investigation

**A field-ready incident response plan, investigation SOPs, scenario playbooks, and — the centerpiece — an evidence-source layer that maps what you need to prove to exactly where the artifact lives and how to collect it safely in an OT environment.**

![Scope](https://img.shields.io/badge/scope-IT%20%2B%20OT%2FICS-blue)
![Aligned](https://img.shields.io/badge/aligned-NIST%20800--61%20%7C%20800--82r3%20%7C%20IEC%2062443-lightgrey)
![Framework](https://img.shields.io/badge/mapped-MITRE%20ATT%26CK%20for%20ICS-red)
![Principle](https://img.shields.io/badge/doctrine-safety--first%20%C2%B7%20passive--before--active-green)
![License](https://img.shields.io/badge/license-MIT-green)

---

## What this is

Most IR documentation tells you *what phase you're in*. This one is built to answer the two questions that actually matter during an OT investigation:

1. **What am I trying to prove?** (an unauthorized logic change happened; a setpoint was manipulated; a remote session was hijacked)
2. **Where is the evidence that proves it, and how do I collect it without disrupting a live physical process?**

The OT twist runs through everything here: in IT you can isolate and image a host; in OT the host might be an HMI driving a running reactor. So the doctrine is **safety first, passive before active, operations in the loop** — collect the non-disruptive evidence (network, historian, logs) before anyone touches a controller.

## Repository map

```
it-ot-incident-response/
├── docs/                                  ← the plan
│   ├── 01-ir-plan-and-lifecycle.md        ← OT-adapted NIST 800-61 lifecycle + safety doctrine
│   ├── 02-roles-and-raci.md               ← who does what, authority to act
│   ├── 03-severity-classification.md      ← consequence-driven severity (IT vs OT)
│   ├── 04-evidence-handling-chain-of-custody.md
│   └── 05-communications-and-regulatory.md
├── sop/                                   ← how to investigate, step by step
│   ├── triage-first-30-minutes.md         ← the triage card
│   ├── universal-investigation-sop.md     ← master investigation procedure
│   └── ot-investigation-sop.md            ← OT-specific procedure (6 domains)
├── evidence/                              ← ★ where the proof lives
│   ├── evidence-source-matrix.md          ← assertion → evidence → location → what it proves
│   ├── windows-ews-hmi-historian-host.md
│   ├── network-and-ot-protocols.md
│   ├── historian-and-process.md
│   ├── plc-controller-safe-acquisition.md
│   └── identity-and-remote-access.md
├── playbooks/                             ← per-scenario response + evidence steps
│   ├── pb-01-unauthorized-plc-logic-change.md
│   ├── pb-02-unauthorized-setpoint-change.md
│   ├── pb-03-safety-system-manipulation.md
│   ├── pb-04-malware-ransomware-on-ot-host.md
│   └── pb-05-suspicious-remote-access.md
└── templates/                             ← fill-in forms
    ├── incident-report.md
    ├── chain-of-custody-form.md
    └── evidence-collection-log.md
```

## How to use it

- **A pager just got an alert** → [`sop/triage-first-30-minutes.md`](sop/triage-first-30-minutes.md).
- **Confirmed incident, need the procedure** → [`sop/universal-investigation-sop.md`](sop/universal-investigation-sop.md), branch into [`sop/ot-investigation-sop.md`](sop/ot-investigation-sop.md) if OT is in scope.
- **Known scenario** → pick the matching [`playbooks/`](playbooks/) file.
- **"Where do I find proof of X?"** → [`evidence/evidence-source-matrix.md`](evidence/evidence-source-matrix.md), then the domain guide it points to.
- **Building the case file** → [`templates/`](templates/).

## Core doctrine (read first)

1. **Human safety outranks everything.** No investigative action may increase risk to people or the process. When cyber response and plant safety conflict, safety wins and the plant/process engineer has the call.
2. **Passive before active.** Exhaust non-disruptive evidence (network capture, historian, logs, EDR) before any active acquisition that touches a live controller.
3. **Operations in the loop.** Every OT containment or acquisition decision is a joint cyber + controls-engineering decision, recorded.
4. **Preserve, then analyze.** Capture volatile evidence in order of volatility *before* remediation destroys it — but never at the cost of rule 1.
5. **Prove with artifacts, not inference.** Every assertion in the final report is backed by a collected, hashed, custody-logged artifact.

## Alignment

Structured on **NIST SP 800-61** (IR lifecycle) and **NIST SP 800-82 Rev 3** (OT security), with containment and zoning per **IEC 62443**, adversary technique mapping via **MITRE ATT&CK for ICS**, and evidence handling per **RFC 3227** order-of-volatility (OT-adapted). Regulatory reporting guidance in [`docs/05-communications-and-regulatory.md`](docs/05-communications-and-regulatory.md) — verify current thresholds with your legal team and regulator.

## Author

Mahesh Reddy — OT/ICS Security · GICSP, SANS ICS410, Nozomi Certified

## License

MIT — see [`LICENSE`](LICENSE).

> These are template procedures. Adapt tag names, zone architecture, tool names, contacts, and regulatory obligations to your site before use. All acquisition guidance is written to be read-only and non-disruptive, but **you** are responsible for validating any action against your plant's safety case before executing it.
