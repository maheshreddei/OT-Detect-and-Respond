# Use Case Testing & Validation Guide

How a detection moves from written to trusted. This is the methodology behind the
five-stage gate in the briefing, with the specific test method for each class of detection
in the library.

The governing principle: **a detection is not validated until it has fired on something
real and stayed quiet on something benign.** Everything below is in service of those two
pieces of evidence.

---

## Stage 1 — Data availability check

Before writing or completing any logic, prove the telemetry exists.

| Check | How | Pass condition |
|-------|-----|----------------|
| Source is collecting | Query the index/table for the last 24h | Non-zero events, no gaps > expected interval |
| Fields extract | Sample 20 events, inspect the fields the rule needs | Every referenced field resolves, no nulls where values are expected |
| Timestamps correct | Compare event time to wall clock and check timezone | No skew; ordering is sane |
| Volume is sane | Compare against the estimate in `parser-mapping.csv` | Within tolerance; a 10x surprise means a parsing or filtering problem |

**If the data is not there, stop.** The detection becomes a collection requirement in
`01-telemetry/`, not a detection task. This single discipline is what prevents a library of
rules that silently cover nothing.

---

## Stage 2 — Positive test (does it fire?)

Emulate the technique and confirm the rule fires. **Never against live process equipment.**
Choose the method by detection class:

### Protocol detections (Modbus, DNP3, IEC-104, S7comm, ENIP, OPC UA)

**Preferred: PCAP replay.** Deterministic, repeatable, and safe — no equipment touched.

```bash
# Replay a crafted or captured PCAP onto the monitored segment / sensor interface
tcpreplay -i eth1 --pps=100 modbus-unauthorized-write.pcap
```

Build the PCAP either by capturing a legitimate operation on a bench and rewriting the
source address, or by generating the traffic with a protocol client.

**Alternative: bench generation** against an isolated PLC or a simulator:

| Protocol | Tool | Note |
|----------|------|------|
| Modbus | `pymodbus` client, `mbtget`, ICS simulators | Write FCs 5/6/15/16 from an unlisted source IP |
| DNP3 | `opendnp3`, `dnp3-simulator` | Function 13/14 restart, function 21 disable-unsolicited |
| IEC-104 | `lib60870` sample clients | C_SC/C_DC ASDU from a non-authorised host |
| S7comm | `snap7` | Run/stop and download operations against a bench S7 |
| EtherNet/IP | `pycomm3`, `cpppo` | CIP services against a bench Logix |
| OPC UA | `opcua-client`, `python-opcua` | Anonymous session, SecurityMode=None |

Use a **spare or decommissioned controller on a bench**, never a spare that is a hot standby.

### Windows, identity, and endpoint detections

Atomic Red Team is the fastest route for the IT-side rules (log clearing, remote tooling,
lateral movement, credential patterns):

```powershell
Invoke-AtomicTest T1070.001 -TestNumbers 1    # e.g. event log clearing
```

For OT-specific host behaviour (engineering tool launch outside a change window), simply run
the engineering software on a lab EWS outside the window and confirm the rule fires.

### Historian and process-data detections

**Synthetic tag injection.** Write a controlled series into a test historian instance or a
copy of the tag namespace:

- *Envelope breach*: inject values outside the P1–P99 band for longer than the dwell.
- *Frozen value / replay*: repeat an identical value past the staleness threshold.
- *Divergence*: inject a historian value that disagrees with the controller value.
- *Impossible state*: set a combination the physics forbids (valve closed + flow rising).

### SIS and safety detections

**These are validated on a bench or simulator only — never on an in-service safety system.**
Coordinate with functional safety. Where a bench SIS is unavailable, validate by PCAP replay
of captured boundary traffic and treat the detection as partially validated, recorded as
such.

### Recording the result

| Field | Value |
|-------|-------|
| Technique emulated | T0855 |
| Method | PCAP replay / bench client / Atomic |
| Source → destination | |
| Rule fired? | Yes / No |
| Time to alert | |
| Evidence | Alert ID, screenshot, log excerpt path |

**If it did not fire, the detection returns to development.** No promotion on intent.

---

## Stage 3 — Negative test (does it stay quiet?)

This is the stage that determines whether the detection survives contact with production,
and in OT it is *more* work than the positive test — because most OT alerts are legitimate
activity.

Replay or observe each benign scenario and record whether the rule fires:

| Benign scenario | Why it matters |
|-----------------|----------------|
| Normal steady-state operation | The baseline. Any firing here is disqualifying. |
| Scheduled maintenance window | Engineering tools, downloads, and writes are expected |
| Commissioning / loop checks | Loop checks write to coils and registers all day |
| Startup / shutdown / grade change | Produces legitimate out-of-envelope process values |
| Backup or secondary master | A second control centre looks like an unauthorised source |
| Sanctioned vulnerability scanner | Looks exactly like reconnaissance |
| Vendor remote support session | Off-hours access with no local paperwork |
| Device replacement | New MAC/IP appears in a monitored zone |

Every benign trigger must resolve to one of:

1. **An allowlist entry** — added to the rule's inline baseline (authorised masters, EWS
   list, scanner IPs).
2. **A tuning change** — threshold, dwell, or time-window adjustment, version-bumped.
3. **A documented accepted false positive** — with the reason and the expected rate.

An unexplained benign trigger **blocks promotion**. Target a benign corpus of at least two
weeks covering one full maintenance cycle where the process allows.

---

## Stage 4 — Peer and safety review

| Reviewer | Confirms |
|----------|----------|
| Detection engineer (peer) | Logic is sound, fields map correctly, no silent inversion of filter conditions |
| OT/process engineer | **Mandatory for anything touching an SIS or a controller.** Operational plausibility and the impact of the documented response |
| SOC lead | Severity, SLA, runbook linkage, and alert-volume acceptability |

**Detection engineering does not self-certify operational impact.** For safety-relevant
content the process engineering owner signs the review, and that signature is a promotion
gate, not a formality.

Reviewers should specifically check the **filter-negation direction** — a selection block
mistakenly treated as a filter inverts the detection and produces a rule that fires on
everything *except* the attack. It is the most damaging and least visible defect in
converted content.

---

## Stage 5 — Promote and monitor

- Runbook / playbook linked (`04-response/playbooks/`)
- Severity and escalation criteria set
- Source-health alerting in place — **if the feed stops, someone is told**. A silent
  detection and a silent data source look identical from the console.
- Status moved to Production in the catalog and committed

**Tuning is a normal recurring state, not a failure.** Every tuning change is a commit with
a version bump, which is why the content lives in git rather than only in the platform.

---

## Continuous validation

A detection that fired last quarter is not proven to fire today — schemas drift, parsers
change, sensors get moved.

- **Quarterly re-test** of the top detections by severity, using the same PCAPs and
  synthetic data. Keep the test corpus in version control alongside the rules.
- **Re-baseline after MOC.** A legitimate operating-point change makes envelope and
  threshold detections wrong until re-based. Treat MOC notification as a detection-maintenance
  trigger.
- **Coverage review** each quarter against `05-crosswalk/attack-coverage.csv` — which
  techniques gained detections, which remain uncovered, and which are covered only by
  scaffolds.

---

## Prioritising the scaffold backlog

161 detections are specification-only. Do not work them in ID order. Prioritise by:

1. **Technique coverage gain** — a scaffold covering an otherwise-uncovered ATT&CK technique
   is worth more than the fifth detection for a well-covered one.
2. **Tier 1 reachability** — detections needing only telemetry already collected can be
   validated immediately, with no procurement dependency.
3. **Severity** — Critical and High first, with all SIS-related content near the top.
4. **Test repeatability** — protocol detections validate fastest because PCAP replay makes
   the test deterministic and reusable.

Applying these filters, roughly the top 40 scaffolds close most of the coverage gap. That is
the proposed first tranche.

---

## Minimum viable test environment

To run the above, the requirements are modest:

- A **bench PLC or simulator** (one Siemens S7 or Allen-Bradley unit, plus open-source
  simulators for the rest)
- A **traffic replay host** with `tcpreplay` and an interface into the monitored segment or
  directly to a sensor
- A **lab Windows host** representing an EWS, with the same agent configuration as
  production
- A **non-production SIEM index or workspace** so test data never pollutes production
  baselines
- A **PCAP library** — captured or crafted, version-controlled with the rules

None of this requires production access, and none of it needs to touch live process
equipment.
