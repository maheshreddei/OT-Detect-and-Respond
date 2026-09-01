# Chapter 16 — Threat-Hunting Methodology for OT

> Part IV · Hunting & Detection. This is the craft: structured, repeatable, safety-checked ways to look for what your alerts never told you. The methodology is what separates hunting from random log-grepping.

## 16.1 What hunting is (and isn't)

Threat hunting is the **proactive, hypothesis-driven** search for adversary activity that automated detections missed. It is not alert triage (reactive), not a vulnerability scan, and not ad-hoc grepping. A hunt starts from a question, uses data to answer it, and — critically — **ends by hardening detection**: every hunt should leave behind a new or improved rule, or a documented "nothing here, and here's how I'd know next time."

## 16.2 The six hunt types

Different triggers call for different hunts:

1. **Intelligence-driven** — start from a report/group: "adversary X uses techniques A, B, C; do I have coverage and evidence?"
2. **Hypothesis / analytics-driven** — start from a testable idea: "if an attacker did Y, I'd expect Z in the data."
3. **Baseline-deviation** — start from "what's new/abnormal versus the allow-lists?" (OT's strongest, thanks to stability).
4. **Crown-jewel / consequence-driven** — start from the highest-consequence assets and work outward.
5. **Situational / architecture-triggered** — start from a change (new remote access, a new vendor link, a merger).
6. **Incident-driven / retrospective** — re-hunt historic data with new knowledge after an incident or disclosure.

## 16.3 The hypothesis loop

The core mechanic of any hunt:

```
  Hypothesis ─▶ Data ─▶ Analyze ─▶ Confirm/Deny ─▶ Output (detection or documented negative)
       ▲                                                   │
       └───────────────── refine and repeat ───────────────┘
```

- **Hypothesis:** specific and testable ("an unauthorized host is writing to a controller"), not vague ("find bad things").
- **Data:** identify the exact source (Zeek modbus.log, historian setpoints, jump-host auth) and confirm it exists before hunting — a hunt without data is a coverage gap to log, not a hunt to run.
- **Analyze:** compare against the baseline/allow-list; group by asset criticality, not by time.
- **Confirm/deny:** reach a conclusion.
- **Output:** a durable detection if the pattern is worth watching, or a documented negative that records how you'd detect it next time.

## 16.4 Safety rules for hunting (non-negotiable)

Hunting in OT operates under the Chapter 01 doctrine, made concrete:

1. **Read-only by default.** Passive capture, log collection, and configuration review only — unless a specific active step is explicitly authorized.
2. **No active scanning of Level 0–2 devices** without a written test window and engineer supervision.
3. **Change-window discipline.** Any sensor install, SPAN change, or agent deployment follows management of change.
4. **A named escalation engineer** who can authoritatively answer "is this change/observation expected?"
5. **Stop authority.** Operations can halt your activity at any moment, no justification required.

A hunt that violates these is not a hunt — it's an incident waiting to happen.

## 16.5 Prioritize by consequence

Because you can't hunt everything, hunt the **crown jewels and safety-relevant assets first**, and triage findings by **asset criticality** rather than chronologically. A minor anomaly on a safety-related controller outranks a louder one on a reporting server. The consequence lens (Chapter 01) governs hunt prioritization just as it governs vulnerability triage.

## 16.6 The allow-lists are your hunting ground

Most OT hunts reduce to "**show me what's not on the list**": a source not on the asset allow-list, a conversation not on the conversation allow-list, a write not on the command allow-list, a binary not on the software allow-list, a logon not on the account allow-list. This is why the baselining of Chapters 08–09 is the prerequisite for effective hunting: the allow-lists convert OT's stability into a detection surface.

## Chapter summary
- Hunting is **proactive and hypothesis-driven**, and it always **ends by hardening detection**.
- Six hunt types (intelligence, hypothesis, baseline-deviation, crown-jewel, situational, retrospective) for different triggers.
- Run the **hypothesis loop**: specific hypothesis → confirmed data → baseline comparison → conclusion → durable output.
- Obey the **safety rules** (read-only default, no unsupervised active scanning, change discipline, named engineer, operations' stop authority).
- Prioritize by **consequence**; hunt against the **allow-lists** ("show me what's not on the list").

## Cross-references
- Chapters 08–09 (baselining) enable this; Chapter 17 (indicators) supplies hunt targets; Chapter 20 (detection engineering) receives the outputs; Chapter 24 (playbooks) makes recurring hunts repeatable.
- Companion: `threat-detection-assurance` validates the detections hunts produce.
