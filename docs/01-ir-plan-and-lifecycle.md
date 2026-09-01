# IR Plan & OT-Adapted Lifecycle

The overarching incident response plan for IT and OT/ICS security events. Built on the NIST SP 800-61 lifecycle, adapted with the OT-specific constraints from NIST SP 800-82 Rev 3 and IEC 62443.

## Why OT IR is different

In enterprise IT, the default response to a compromised host is *isolate and image*. In OT, that host may be an HMI operating a live process, a historian feeding safety dashboards, or an engineering workstation whose disconnection blinds operators. The consequences of a response action can exceed the consequences of the incident itself. Three constraints reshape the whole lifecycle:

- **Availability and safety dominate.** The classic CIA triad inverts: for OT, the priority order is **Safety → Availability → Integrity → Confidentiality**. A detection that's 100% confident does not justify a containment action that trips the process.
- **You often cannot take the standard forensic action.** You may not be able to power down a controller, pull a live HMI, or run intrusive tooling on a fragile legacy host. Evidence strategy must lead with what's *safe* to collect.
- **Response is a joint discipline.** Cyber responders do not act alone on OT assets. Control-systems engineers and operations own the process and hold veto authority over any action affecting it.

## The lifecycle (six phases)

```
  ┌───────────┐   ┌───────────┐   ┌──────────────┐   ┌─────────────┐   ┌──────────┐   ┌──────────────┐
  │ 1 Prepare │──▶│ 2 Detect  │──▶│ 3 Analyze &  │──▶│ 4 Contain   │──▶│ 5 Eradi- │──▶│ 6 Recover &  │
  │           │   │ & Report  │   │   Triage     │   │  (OT-safe)  │   │  cate    │   │  Post-Incid. │
  └───────────┘   └───────────┘   └──────────────┘   └─────────────┘   └──────────┘   └──────────────┘
        ▲                                                                                      │
        └──────────────────────────── lessons learned feed back ───────────────────────────────┘

  Running through every phase: SAFETY FIRST · PASSIVE BEFORE ACTIVE · OPERATIONS IN THE LOOP · PRESERVE EVIDENCE
```

### Phase 1 — Prepare
Done before any incident. Establish and maintain:
- **Asset inventory** with Purdue level, criticality, safety relevance, owner, and normal communication baselines. You cannot investigate what you haven't inventoried.
- **Golden baselines**: reference controller logic/config, firmware versions, historian baselines, approved network flows. Half of OT forensics is *compare-to-known-good* — see [`../evidence/plc-controller-safe-acquisition.md`](../04-response/evidence/plc-controller-safe-acquisition.md).
- **Logging & telemetry** wired to the SIEM per the data-source mapping — network (Nozomi/Zeek), historian, endpoint (EDR on Windows OT hosts), identity, boundary firewall. Confirm retention meets your longest plausible dwell time.
- **Pre-authorized response actions** agreed with operations: what may be done unilaterally (e.g. block an IT-side IP) vs. what requires an engineer/operations sign-off (anything touching L0–L2).
- **Contacts & escalation tree**, out-of-band comms, and a jump-kit (write-blockers, tested collection USBs, a clean forensic laptop that has *never* touched OT, capture tooling).

### Phase 2 — Detect & Report
An event arrives from a SIEM correlation, a Nozomi/Dragos alert, a historian deviation, an operator observation ("the readings look wrong"), or an external notification (ISAC, vendor, regulator). **Operator reports are first-class signals in OT** — a human noticing implausible process behaviour has caught attacks that evaded network monitoring. Log the report, timestamp it, open the incident record, and move to triage. See [`../sop/triage-first-30-minutes.md`](../04-response/sop/triage-first-30-minutes.md).

### Phase 3 — Analyze & Triage
Establish four things fast: **scope** (which assets/zones), **consequence** (safety/production impact, actual and potential), **confidence** (real vs false positive), and **volatility** (what evidence is decaying now). Assign severity per [`03-severity-classification.md`](03-severity-classification.md). Begin **evidence preservation in parallel** — the historian and network captures are safe to pull immediately and are decaying, so start them before deep analysis. Build the initial timeline. This is where [`../evidence/evidence-source-matrix.md`](../04-response/evidence/evidence-source-matrix.md) drives the work.

### Phase 4 — Contain (OT-safe)
Containment is where OT diverges hardest from IT. Options, in ascending order of process risk:
- **IT-side / boundary containment** (usually pre-authorized): block an external IP, disable a compromised IT account, isolate an infected IT host, tighten a firewall rule at the IT/OT boundary. Preferred first move — stops the bleed without touching the process.
- **Segmentation** at the conduit: cut a specific cross-zone flow or vendor-access path while leaving the process running.
- **OT-asset containment** (requires operations sign-off): isolating an HMI/EWS, moving a loop to manual/local control, or in the extreme a controlled process shutdown. A **controlled shutdown by operations is a valid, sometimes correct, containment** — but it is a plant decision, not a SOC decision.
- **What NOT to do reflexively**: yank a controller's network cable, power-cycle a PLC, or push a config to "clean" it. Each can trip the process or destroy volatile evidence. Capture first (safely), then act.
Record who authorized each action and the operational rationale.

### Phase 5 — Eradicate
Remove the adversary's foothold: rebuild compromised Windows OT hosts from known-good images, reset credentials (coordinated to avoid lockout of running systems), restore controller logic/config from verified golden baselines after confirming the running logic is compromised, patch or compensate the entry vector. **Verify eradication against evidence** — don't declare clean because an alert stopped; confirm the specific artifacts you found are gone.

### Phase 6 — Recover & Post-Incident
Return to normal operations under heightened monitoring; validate process integrity with operations before declaring recovery (the historian confirms the process is back within its safe envelope). Then: finalize the case file with all custody-logged artifacts (see [`../templates/incident-report.md`](../04-response/templates/incident-report.md)), complete regulatory reporting per [`05-communications-and-regulatory.md`](05-communications-and-regulatory.md), and run a blameless lessons-learned that feeds detections, baselines, and this plan.

## Decision rule when cyber and safety conflict

> If a proposed cyber response action could increase risk to people, environment, or safe process operation, **it does not proceed on cyber authority alone.** It is escalated to the incident commander and the operations/plant-safety authority, who decide jointly. Safety has the final veto. This rule is absolute and overrides urgency.

## Related
- Roles and who-decides-what: [`02-roles-and-raci.md`](02-roles-and-raci.md)
- Severity: [`03-severity-classification.md`](03-severity-classification.md)
- The step-by-step procedure: [`../sop/universal-investigation-sop.md`](../04-response/sop/universal-investigation-sop.md)
