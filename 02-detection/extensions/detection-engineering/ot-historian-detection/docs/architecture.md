# Reference Architecture

How historian process data reaches detection logic, and where the statistics should run.

## The core pattern: historian does the math, SIEM does the correlation

Computing raw σ-bands, slew rates, and mass balances on full-resolution streams for thousands of tags **inside the SIEM** gets expensive fast and duplicates capability the historian already has. The scalable pattern splits the work:

```
   Level 0-1              Level 2                 Level 3 / DMZ            Level 3.5 / IT SOC
 ┌───────────┐        ┌────────────┐          ┌──────────────┐         ┌──────────────────┐
 │ Sensors / │  I/O   │ PLC / DCS  │  OPC/hist │  Process     │ exception│  SIEM            │
 │ actuators ├───────▶│ controllers├──────────▶│  Historian   ├─────────▶│  (Splunk ES /    │
 │           │        │            │           │  + native    │  events  │   Sentinel)      │
 └───────────┘        └────────────┘           │  analytics   │         │                  │
                                               │ (PI AF / GE) │         │  correlation +   │
                                               └──────┬───────┘         │  enrichment + IR │
                                                      │ raw values      └────────┬─────────┘
                                                      │ (optional, downsampled)  │
                                                      └──────────────────────────┘
                                                                                 │
   Network sensors (Nozomi / Claroty / Dragos) ─────── protocol anomalies ───────┘
```

**Baseline + deviation math runs in the historian's native analytics** (PI AF Analyses, GE Proficy calc engine, Canary Axiom, Ignition expressions). Only **exception events** — "tag X breached its P99 envelope for its current mode" — are forwarded to the SIEM. The SIEM's job is the thing only it can do: **cross-domain correlation** (historian deviation + Nozomi protocol write + Level-3 auth event = an incident, not three unrelated alerts).

Every `splunk.spl` and `sentinel.kql` in this repo is written to work **either way**:
- **SIEM-native** — historian raw/downsampled values are indexed and the SPL/KQL computes the deviation directly (simpler to stand up, heavier to run).
- **Exception-forwarded** — the historian emits exception events and the SPL/KQL correlates and enriches them (lighter, preferred at scale).

## Two go-to-market deployment models

### Model 1 — Nozomi-anchored (network + process fusion)
Nozomi Guardian is already deployed for network visibility. Historian exception events are forwarded into the same SIEM and **correlated with Guardian alerts**. This is the strongest analytic position: a setpoint change seen on the wire (Guardian) *and* an out-of-envelope PV (historian) is a high-confidence, low-FP incident. Best fit where an NDR is already in place.

### Model 2 — SIEM-agnostic (historian-only)
No assumption of an NDR. Historian data is the sole source; detections stand alone. Faster to deploy, portable across Splunk and Sentinel, and a strong differentiator for sites that have a historian but no OT network monitoring yet — which is most of them.

Both models use identical detection logic; only the correlation layer differs.

## Getting historian data into the SIEM

| Historian | Splunk method | Sentinel method |
|-----------|---------------|-----------------|
| OSIsoft / AVEVA PI | PI Web API (REST) via a modular input; or PI Integrator → DB Connect | PI Web API → Logic App / Function → Data Collector API (or AMA custom log) |
| GE Proficy | OPC UA / OPC HDA bridge → HEC | OPC UA → edge collector → AMA |
| Canary / Ignition | REST / MQTT Sparkplug → HEC | MQTT → Event Hub → Sentinel |
| Generic SQL historian | DB Connect (scheduled) | Function App polling → Data Collector |

**Collection guidance**
- Prefer **exception/on-change** collection over fixed-interval polling — it matches how historians store data and cuts volume dramatically.
- For detections that need continuous math (slew rate, variance), pull **downsampled** interpolated values (e.g. 1/sec or 1/5-sec), not every raw sample.
- Preserve the **quality** attribute (Good/Bad/Uncertain) end to end — several detections key off it.
- Keep collection **read-only**. Use a dedicated read account with least privilege. Nothing in this pipeline writes to the control system.

## Data flow direction and zone rules

Collection must respect the Purdue model and IEC 62443 zone/conduit rules:
- The historian typically lives at **Level 3** (site operations) or is mirrored to a **Level 3.5 DMZ** replica.
- **Pull from the DMZ replica** where one exists — never reach an analyst tool directly into Level 2.
- The conduit from historian/DMZ to the IT SOC is **outbound, unidirectional-preferred** (data diode or tightly-filtered firewall rule). No inbound path from the SIEM to OT.

## Where each repo artifact runs

| Artifact | Runs in |
|----------|---------|
| `lookups/*.csv` | SIEM (Splunk lookup / Sentinel watchlist) — the baseline reference |
| `splunk.spl` / `sentinel.kql` | SIEM scheduled search / analytics rule |
| Baseline computation (seeding + re-baseline) | Historian native analytics, or an offline job that regenerates the lookups |
| Exception generation (at scale) | Historian native analytics |

See [`data-model.md`](data-model.md) for the exact schema the queries expect.
