# Universal Security Event Investigation SOP

The master procedure for investigating a security event across IT and OT. Branch into the [OT Investigation SOP](ot-investigation-sop.md) whenever OT assets are in scope. Every step is written to produce **defensible, custody-logged evidence** tied to a specific investigative assertion.

**Governing doctrine:** safety first · passive before active · operations in the loop · preserve before you analyze.

---

## Step 0 — Receive & record (0–5 min)
- Open the incident record. Capture: source of report, time (with timezone), reporting system/person, initial indicators, affected asset(s) if known.
- Assign a provisional severity ([`docs/03-severity-classification.md`](../../docs/03-severity-classification.md)). If any OT escalator applies (SIS, controller logic, loss of view/control, sub-L2 activity), raise immediately and notify operations.
- Note the current time on the SIEM and on any suspect system to establish clock offsets for the timeline.

## Step 1 — Triage & validate (5–30 min)
Goal: real or false positive? Scope? Consequence? Volatility?
- Reproduce the triggering signal in the SIEM; pull the raw event(s) behind the alert.
- Identify the asset(s): Purdue level, criticality, safety relevance, owner. Pull from asset inventory.
- Assess **actual and potential** consequence with operations if OT is involved.
- Decide: close as FP (document why), or confirm as incident and proceed.
- **Start evidence preservation in parallel now** — the non-disruptive, decaying sources (network capture, historian export, volatile host telemetry via EDR) should begin collecting while you continue analysis. See [`triage-first-30-minutes.md`](triage-first-30-minutes.md).

## Step 2 — Frame the investigative questions
Before collecting, write down **what you need to prove.** Investigation is hypothesis-driven; evidence collection serves specific assertions. Typical questions:
- *Did an unauthorized action occur?* (login, write, program change, config change)
- *Who/what performed it?* (account, host, source IP, session)
- *When, and in what sequence?* (timeline)
- *What was the impact?* (process deviation, data access, lateral movement)
- *How did they get in, and are they still here?* (entry vector, persistence, active access)

For each question, [`../evidence/evidence-source-matrix.md`](../evidence/evidence-source-matrix.md) tells you which artifact proves it and where it lives.

## Step 3 — Preserve volatile evidence (order of volatility)
Following [`docs/04-evidence-handling-chain-of-custody.md`](../../docs/04-evidence-handling-chain-of-custody.md), and never overriding safety:
1. Network state & capture (taps/SPAN, device session/ARP tables) — safe, do first.
2. Historian & alarm export for the affected process/time window — safe, decisive, do early.
3. Volatile host state (memory, connections, processes) — via EDR where possible; live capture only if the host tolerates it.
4. Controller volatile state — **only** engineer-led, read-only, if in scope (see OT SOP).
Hash and custody-log every artifact at collection.

## Step 4 — Collect durable evidence
- Windows OT/IT hosts: event logs, Sysmon, PowerShell logs, prefetch, registry, scheduled tasks, $MFT/USN, engineering-software project files & logs. See [`../evidence/windows-ews-hmi-historian-host.md`](../evidence/windows-ews-hmi-historian-host.md).
- Network: pcap, Zeek logs, Nozomi/Dragos alerts & asset changes, firewall & VPN logs. See [`../evidence/network-and-ot-protocols.md`](../evidence/network-and-ot-protocols.md).
- Identity: AD security logs, authentication logs, remote-access/PAM logs. See [`../evidence/identity-and-remote-access.md`](../evidence/identity-and-remote-access.md).
- Process: historian trends, alarm/event journal, setpoint-change records. See [`../evidence/historian-and-process.md`](../evidence/historian-and-process.md).

## Step 5 — Build the timeline
Normalize all timestamps to a single reference timezone (record offsets). Merge events from every source into one master timeline. The timeline is the backbone of the case — it turns scattered artifacts into a narrative of *who did what, when, and with what effect*. Correlate across layers: a network-layer action (Nozomi write) plus a host-layer action (EWS login) plus a physics-layer effect (historian deviation) on the same asset in the same window is a proven, corroborated event.

## Step 6 — Analyze & attribute
- Determine the entry vector, the actions taken, the accounts/hosts involved, persistence mechanisms, and whether access is still active.
- Map observed behaviour to **MITRE ATT&CK for ICS / Enterprise** techniques — it structures the analysis and reveals gaps ("if they did T-X, they likely also did T-Y; did we check?").
- Distinguish **confirmed** (artifact-backed) from **assessed** (inferred). The report separates these clearly.

## Step 7 — Recommend containment
Produce containment options ranked by process risk ([`docs/01-ir-plan-and-lifecycle.md`](../../docs/01-ir-plan-and-lifecycle.md), Phase 4). Recommend; let the authority-to-act matrix decide. Record decisions and rationale.

## Step 8 — Support eradication & recovery
Verify eradication against the specific artifacts found. Validate recovery with operations — confirm via historian that the process is back inside its safe envelope before sign-off.

## Step 9 — Document & close
Compile the case file using [`04-response/templates/incident-report.md`](../templates/incident-report.md): executive summary, timeline, evidence register (with hashes & custody), root cause, impact, actions taken, ATT&CK mapping, and recommendations. Confirm regulatory reporting is handled. Feed findings into detections, baselines, and this SOP.

---

## Quality bar for the final report
- Every factual assertion cites a **collected, hashed, custody-logged artifact**.
- Confirmed vs assessed are labelled.
- The timeline is complete and timezone-normalized.
- No investigative action taken on OT without recorded operations authorization.
- Detections/baselines updated so the same event is caught faster next time.
