# Chapter 24 — Hunting Playbooks Library

> Part IV. Playbooks turn a skilled hunter's judgment into a repeatable team capability. This chapter defines the playbook format and a starter library of the recurring OT hunts.

## 24.1 Why playbooks

A hunt run once by an expert helps once. The same hunt written as a **playbook** — a repeatable, safety-checked procedure any analyst can follow identically — helps every time, produces consistent MTTD, and can be measured and improved. Playbooks are the bridge between the methodology (Chapter 16) and day-to-day operations.

## 24.2 The playbook format

Every playbook should contain:

- **Trigger** — what starts it (an alert, a schedule, an intel report, a situational change).
- **Hypothesis** — the specific thing you're testing for.
- **Required data** — the exact sources needed (and the check that they're feeding).
- **Steps** — the ordered, **safe (read-only)** queries/actions, with platform-neutral logic.
- **Decision criteria** — what distinguishes benign from suspicious from confirmed.
- **Escalation / response** — who to involve and the next step if confirmed (linking to the IR playbooks, Chapter 25).

Every step must be read-only or lab-validated — **nothing in a hunting playbook touches the live process.**

## 24.3 A starter library

The recurring OT hunts worth having as playbooks:

1. **Unauthorized write/command** — write function code to a critical controller from a source off the command allow-list.
2. **New asset on the OT network** — a device not in the asset allow-list appears in a control/safety zone.
3. **Remote access into OT** — a new or off-hours remote session reaching the OT network; correlate jump-host/VPN auth with subsequent OT actions.
4. **Program download / mode change** — a controller program transfer or key-switch/mode change, especially outside a change window.
5. **Setpoint anomaly** — a setpoint written outside the approved range, outside hours, or by an unexpected source (historian).
6. **Beaconing / DNS egress from OT** — a control-zone host making regular outbound connections or unusual DNS — possible C2.
7. **Internet-exposed OT discovery** — enumerate OT assets reachable from outside their zone or the internet.
8. **Baseline drift review** — periodic review of new conversations/assets against the allow-lists.

Each maps to an ATT&CK technique and, once mature, graduates into an automated detection (Chapter 20) — at which point the playbook may retire or become the triage procedure for that detection's alerts.

## 24.4 Feeding the loop

Playbooks are living artifacts: each run refines the steps, surfaces data gaps, and may spawn a new detection. Version them alongside detections, review them on the same cadence, and retire those whose detection is now fully automated. This keeps the library sharp and prevents it from becoming stale documentation.

## Chapter summary
- Playbooks turn expert hunts into a **repeatable, measurable team capability** with consistent MTTD.
- Format: **trigger · hypothesis · required data · safe steps · decision criteria · escalation** — every step read-only.
- Keep a **starter library** (unauthorized write, new asset, remote access, program download/mode change, setpoint anomaly, beaconing, internet exposure, baseline drift).
- Playbooks are living — refine each run, promote mature ones to detections, retire the automated.

## Cross-references
- Chapter 16 (methodology), Chapter 20 (playbooks → detections), Chapter 25 (IR playbooks).
- Companion: `it-ot-incident-response` (response playbooks and SOPs).
