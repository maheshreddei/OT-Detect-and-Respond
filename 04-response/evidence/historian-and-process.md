# Evidence: Historian & Process (Physics)

This is the decisive OT evidence layer and the one most investigations underuse. The historian is the **physical record of what actually happened to the process.** Network evidence proves a command was sent; the historian proves what that command *did* — and no view-spoofing survives an independent process record. It is also **safe, non-disruptive, and durable**, so collect it early.

## Sources

### Historian value trends (PI, Proficy, Canary, Ignition, AVEVA)
- Export the relevant tags for a window generously bracketing the incident (before, during, after).
- Collect: PI Web API / DataLink export, Proficy export, DB query, or the historian's native export — to CSV or native format. **Hash the export and record the exact query (tags + time range)** so the extraction is reproducible.
- Proves: PV excursions, setpoint jumps, rate-of-change anomalies, frozen/replayed values, variance collapse — the physical signature of manipulation or upset.

### Setpoint-change records
- Historian SP tags, or the DCS/SCADA audit trail if it records writes with user/source.
- Proves: a setpoint written outside its approved range or window (Oldsmar-class), ideally with *who/when/from where* if the control system audits writes.

### Alarm & event journal
- Historian alarm subsystem or DCS/SCADA alarm & event journal; SER/SOE in power/utility.
- Proves: **alarm suppression or shelving** (attacker hiding the effect), **trip-point approach** (TRITON precursor), alarm floods (masking), and the operator-facing timeline of the event.

### Independent value comparison (view-spoof proof)
- Compare the HMI-path historian value against an independent reading (a second historian source, a direct controller read, or a network-captured value).
- Proves **manipulation of view (Stuxnet-class)**: the operator was shown normal while reality diverged. This is often the *only* way to prove a sophisticated spoof.

### Batch / sequence records
- Batch historian / sequence-of-events.
- Proves: step-order or timing manipulation, phase deviations from the golden batch.

## Why the historian is decisive
- **It survives host and view compromise.** An attacker can spoof an HMI in real time, but an independent historical record (or a second source) contradicts the spoof after the fact.
- **It proves impact, not just action.** Regulators, insurers, and safety reviews care about physical consequence — the historian quantifies it.
- **It's safe to collect.** Read-only export, no process risk — so there's no reason not to pull it immediately.

## Collection steps
1. Identify the affected asset(s), their tags (PV, SP, CV, mode, alarm), and safety-related tags.
2. Choose a window that brackets the incident with margin (baseline before + full event + recovery after).
3. Export values + alarm/event journal for those tags/window; hash the export; record the query.
4. If a spoof is suspected, obtain a second independent source for the key tags and compare.
5. Correlate the process timeline with network (command issued) and host (who issued it) evidence — the three together prove *who did what and what it did to the plant*.

## What "good" looks like
A historian export showing a setpoint stepping from 100 to an out-of-range value at time T, an alarm-journal entry showing the corresponding high alarm suppressed at T-minus-seconds, and a PV trend showing the process responding — cross-referenced to a network capture of the write and an EWS logon — is a complete, artifact-backed proof of a manipulated-process incident.
