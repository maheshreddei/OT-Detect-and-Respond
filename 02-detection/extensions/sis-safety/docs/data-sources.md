# Data Sources (SIS Telemetry)

SIS telemetry is scarcer than IT or even general OT — safety controllers are locked down and quiet. This maps each detection category to the sources that actually see it. The rule throughout: **passive and read-only** (see [`monitoring-architecture.md`](monitoring-architecture.md)).

## Sources

| Source | What it sees | Feeds categories |
|--------|--------------|------------------|
| **OT network monitoring (Nozomi/Dragos/Claroty) on the safety network** | Engineering sessions, program up/download, SIS protocol traffic, reads/writes, new assets | A, B (primary) |
| **SIS controller diagnostic / event log** | Mode/key-switch changes, downloads, faults, forces, restarts | B, C, F |
| **Process historian (safety tags)** | Safety PV trends, trip records, bypass/inhibit status tags, SOE/SER, voting/channel status | C, D, E, F |
| **DCS/SCADA alarm & event journal** | Trips, bypass annunciation, SIS status, suppression | C, E, F |
| **SIS engineering-station host (EDR / Windows / Sysmon)** | TriStation/SafetyManager/TIA-Safety execution, project file changes, logons | B (host side) |
| **SIS↔BPCS interface gateway logs** | Cross-boundary data exchange, direction, volume | A |
| **Key-switch position (hardwired DI, historized)** | RUN / PROGRAM / REMOTE state | B, C |
| **Final-element & line-monitoring status** | De-energize-to-trip circuit health, output state vs command | C, F |

## Vendor / protocol notes (confirm per site)
- **Triconex** — engineering via **TriStation** (the protocol TRITON abused; TCP-based, ~port 1502/UDP 1500). Key-switch: RUN / PROGRAM / STOP / REMOTE. NDRs parse TriStation and flag program download.
- **HIMA** — HIMax/HIMatrix over safe­ethernet; SILworX engineering tool.
- **Siemens S7 F-Series** — S7 (TCP/102) carrying F-programs; TIA Portal Safety.
- **Rockwell GuardLogix** — CIP Safety over EtherNet/IP (TCP/44818, UDP/2222); Studio 5000 with Safety task.
- Protocol tokens, ports, and event IDs are **vendor/version specific** — confirm with an inventory query before asserting on them.

## Historian tag conventions (adapt to your tag naming)
The historian is the workhorse for C/D/E/F. Typical safety tags to collect:
- Safety PVs and their **trip setpoints** (for trip-approach and setpoint-change detection).
- **Bypass / inhibit / MOS** status tags per SIF (for category E).
- **Voting / channel-health** tags (e.g. 2oo3 status) and redundant transmitter values (for category D).
- **Trip / demand** event tags and SOE/SER records (for category C/F).
- **Key-switch position** tag (for B/C).

## ATT&CK for ICS data-source alignment
Network protocol analysis (safety network) · Operational Databases (Process History/Live Data, Process/Event Alarm — the historian) · Application Log (SIS engineering-station, DCS journal) · Asset (device config/parameters, firmware — SIS logic/firmware). These are the components the SIS techniques (T0880/T0837/T0843/T0858…) are detected from.

## Minimum viable telemetry
1. **NDR/passive tap on the safety network** — unlocks A and B (the TRITON-class engineering/program detections).
2. **Historian safety tags** (PV, trip setpoints, bypass, voting, trips) — unlocks C, D, E, F.
3. **SIS engineering-station EDR** — the host side of B.
4. **DCS alarm journal + SIS diagnostic events** — corroboration and F.
