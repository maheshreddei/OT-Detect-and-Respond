# Functional Safety Primer

The safety concepts every detection in this repo is built on. If you know IEC 61511 cold, skim to the "detection hooks" at the end of each section.

## 1. The SIS is an independent protection layer

Under IEC 61511 (ISA 84), a Safety Instrumented System exists to take the process to a **safe state** when the Basic Process Control System (BPCS = DCS/SCADA) cannot be relied on. For that to mean anything, the SIS must remain effective *when the BPCS fails or is wrong* — so it is kept **independent** of the BPCS.

Communication across the boundary is deliberately asymmetric:
- **SIS → BPCS: read-mostly.** The SIS publishes status, trip states, alarms, and diagnostics up to the DCS/SCADA/historian so operators can see it. Normal and expected.
- **BPCS → SIS: tightly restricted.** At most, non-safety-critical, access-controlled actions (an operator reset or a bypass *request* the SIS logic may choose to honor). **The BPCS must not be able to write the SIS's logic, trip points, or outputs.** If it could, a faulty or compromised DCS would defeat the safety layer — destroying the independence the risk assessment (LOPA) credited.

IEC 61511 allows **separated**, **interfaced**, and **integrated** architectures; independence is easiest to prove in separated/interfaced designs and must be explicitly demonstrated in integrated ones. Either way, the read-up/no-safety-writes rule holds.

> **Detection hook (A):** any write/command from a BPCS-zone source to an SIS asset, any new comms path into the SIS zone not via the sanctioned gateway, and any reversal of the expected read-only direction.

## 2. The safety function chain: sensor → logic solver → final element

A Safety Instrumented Function (SIF) is a straight chain:
1. **Dedicated safety-rated sensors** wire process values directly into the **logic solver** (Triconex, HIMA, Siemens S7 F-Series, Rockwell GuardLogix…).
2. The certified safety application continuously compares those inputs to **trip limits** derived from the process hazard analysis and SIL determination — *not* from the DCS.
3. On a deviation past a trip point, the logic drives the **final elements** (shutdown/safety valves, breakers) to the safe state — **autonomously**, without waiting on the DCS.

> **Detection hook (B, C):** changes to the safety logic, its trip limits, or its operating mode (key-switch → PROGRAM); a safety PV trending toward its trip while the BPCS view looks normal; a commanded safe-state action the final element doesn't follow.

## 3. Fail-safe by design: de-energize-to-trip

Most SIS final-element circuits are **de-energize-to-trip**: outputs are energized in normal operation and *de-energize* to reach the safe position on a trip. This makes failures fail safe — loss of power, a broken wire, or a dead output module all drop to the safe state, and line monitoring detects open circuits. Combined with continuous self-diagnostics (on a detected dangerous fault, the solver trips to safe), this is what lets the SIS carry a low PFDavg and hold its target SIL.

> **Detection hook (F):** loss of line monitoring, unexpected energize where de-energize is expected, diagnostic faults, and SIS restarts — anything eroding the fail-safe property.

## 4. Voting: balancing spurious trips against dangerous failure

Safety inputs and logic use **voting** — 1oo1, 1oo2, 2oo2, 2oo3 — to trade off nuisance trips vs. dangerous (missed) trips. A **2oo3** transmitter set tolerates one failed/deviating transmitter without a false trip while still protecting if two agree. Degradation (a channel dropped, a transmitter deviating) reduces the effective SIL even if the process still runs.

> **Detection hook (D):** voting degradation, redundant safety-sensor disagreement beyond tolerance, and frozen/replayed safety inputs.

## 5. The shared-sensor rule (independence at the sensor)

Best practice is **dedicated safety sensors**, separate from the BPCS. Sharing a sensor between control and safety is heavily constrained by IEC 61511-1 (clause 11.2): a device may **not** be shared such that its failure *both* causes the demand on the SIF *and* disables the SIF's response. That single-point common-cause is exactly what independence exists to prevent. If a device is shared, it becomes part of the SIS (managed to SIL), and the common-cause failure must be accounted for in the PFDavg — which is why most designs simply use separate transmitters with voting.

> **Detection hook (D):** a safety PV that appears to be sourced from (or agrees suspiciously with) a BPCS path — a sign of lost independence — and shared-tag anomalies.

## 6. Bypasses, overrides, and forces

Legitimate maintenance uses **bypasses / overrides / MOS (maintenance override switches)** and **forces** to take a SIF or channel out of service temporarily — under strict procedure (authorization, time limit, compensating measures). Each active bypass is a hole in the protection; an unauthorized, overdue, or clustered set of bypasses is both a safety and a security problem.

> **Detection hook (E):** bypass/inhibit/force activation, long-duration/overdue bypasses, bypasses from unexpected sources or outside maintenance windows, and multiple simultaneous bypasses.

## Why this maps so cleanly to security
Independence, integrity, and fail-safe are **safety** properties — and each is also a **security** control. A safety-targeting attack (TRITON class) works by defeating one of them: reaching the engineering path to change logic (integrity), or manipulating inputs/bypasses so the SIF won't act when needed (fail-safe/voting). Monitoring these properties is therefore both safety assurance and attack detection.
