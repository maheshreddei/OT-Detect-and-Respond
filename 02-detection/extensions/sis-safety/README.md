# SIS / Safety System Detection

**Detection engineering for Safety Instrumented Systems — monitoring the BPCS↔SIS boundary, engineering and program integrity, the safety-function chain, sensor voting, and bypass management.** Grounded in IEC 61511 functional-safety principles; mapped to MITRE ATT&CK for ICS.

![Detections](https://img.shields.io/badge/detections-32-blue)
![Class](https://img.shields.io/badge/threat-TRITON%2FTRISIS%20class-red)
![Standard](https://img.shields.io/badge/grounded-IEC%2061511%20%7C%20IEC%2061508-lightgrey)
![Telemetry](https://img.shields.io/badge/telemetry-NDR%20%7C%20SIS%20logs%20%7C%20historian-orange)
![Principle](https://img.shields.io/badge/doctrine-passive%20%C2%B7%20read--only%20%C2%B7%20safety--first-green)
![License](https://img.shields.io/badge/license-MIT-green)

---

## The principle every detection defends

A Safety Instrumented System is an **independent protection layer**. Under IEC 61511 (ISA 84) it must stay effective *when the control system fails or is wrong* — so it is kept separate from the Basic Process Control System (BPCS = DCS/SCADA). Three properties follow, and each one is a thing you can monitor:

1. **Independence — read up, don't write down.** The SIS publishes status to the DCS/historian; the DCS must **not** be able to write the SIS's logic, trip points, or outputs. A control-to-safety write is a boundary violation. → *category A*
2. **Integrity of the safety function.** The SIF chain is sensor → logic solver → final element, executing certified logic against trip limits derived from the hazard analysis. Changing that logic, its limits, or its mode (key-switch → PROGRAM) is the TRITON attack. → *categories B, C*
3. **Fail-safe by design.** De-energize-to-trip, voting (1oo2/2oo3), and self-diagnostics mean the system fails toward safe. Bypasses, forces, voting degradation, and diagnostic faults erode that — and must be visible. → *categories D, E, F*

TRITON/TRISIS reached a Triconex SIS through the **engineering workstation**, not a DCS write. So the detections here watch the safety network, the SIS engineering path, and the safety-function state — the three places a safety-targeting attack shows up.

## Detection categories

| Cat | Name | Safety principle it defends | File |
|-----|------|------------------------------|------|
| A | BPCS↔SIS boundary integrity | independence (no control→safety writes) | [`detections/A-bpcs-sis-boundary.md`](detections/A-bpcs-sis-boundary.md) |
| B | SIS engineering & program integrity | logic/mode integrity (TRITON class) | [`detections/B-sis-engineering-program.md`](detections/B-sis-engineering-program.md) |
| C | Safety function state & trip | correct trip on deviation; no suppression | [`detections/C-safety-function-trip.md`](detections/C-safety-function-trip.md) |
| D | Sensor & voting integrity | valid inputs; voting & independence | [`detections/D-sensor-voting-integrity.md`](detections/D-sensor-voting-integrity.md) |
| E | Bypass / override / inhibit | protection not silently disabled | [`detections/E-bypass-override.md`](detections/E-bypass-override.md) |
| F | Availability & diagnostics | fail-safe & SIS health visible | [`detections/F-availability-diagnostics.md`](detections/F-availability-diagnostics.md) |

## Grounding & telemetry
- [`docs/functional-safety-primer.md`](docs/functional-safety-primer.md) — the *why*: IEC 61511 independence, the SIF chain, trip logic, de-energize-to-trip, voting, and the shared-sensor common-cause rule. Read this first if the safety concepts are new.
- [`docs/data-sources.md`](docs/data-sources.md) — where SIS telemetry comes from (NDR on the safety network, SIS diagnostic/event logs, historian safety tags, the SIS engineering-station host, DCS alarm journal).
- [`docs/monitoring-architecture.md`](docs/monitoring-architecture.md) — **how to monitor an SIS without touching it**: passive, read-only, sensor placement, and the hard don'ts.

## Doctrine (non-negotiable)
> Monitoring an SIS must never affect its safety function. Everything here is **passive and read-only** — no active scanning of safety controllers, no queries that write, no probes. Instrument the network passively and consume logs/historian; the SIS keeps doing its job untouched. When in doubt, collect less.

## What each detection looks like
Each category file has a **detection table** (id, detection, logic, data source, ATT&CK, severity) plus **worked queries** for the flagship detections — in the source that fits (Nozomi N2QL for the safety network, Splunk SPL / Sentinel KQL for historian/host/alarm). Full list in [`catalog/detection-catalog.csv`](catalog/detection-catalog.csv).

## Relationship to the other libraries
This is the **highest-consequence** slice of OT detection. It complements the OT protocol and historian libraries: the protocol layer sees traffic to the SIS, the historian layer sees the physics (trip-point approach), and this layer adds the SIS-specific engineering, voting, and bypass detections. Any SIS detection here is minimum **SEV-1** and engages the plant safety authority.

## Author
Mahesh Reddy — OT/ICS Security · GICSP, SANS ICS410, Nozomi Certified

## License
MIT — see [`LICENSE`](LICENSE).

> SIS vendors differ (Triconex/TriStation, HIMA, Siemens S7 F-Series, Rockwell GuardLogix/CIP Safety). Protocol tokens, ports, event names, and tag conventions are vendor/site-specific — confirm against your environment. All content is detection-only and read-only by design.
