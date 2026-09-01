# Chapter 08 — Passive Visibility: TAP, SPAN and Sensor Placement

> Part II. Visibility is the foundation of everything else — you cannot hunt or detect what you cannot see. This chapter is the engineering of *seeing* an OT network without ever risking the process.

## 8.1 Passive by default, always

The governing rule from Chapter 01 becomes concrete here: **capture passively.** You observe copies of traffic; you never inject, scan, or sit inline in a way that could disrupt control. Active queries of Level 0–2 devices happen only inside a **written test window with engineer supervision and a clear reason** — never as a first move, never as background hygiene. A passive sensor cannot, by construction, disrupt the process, which is why it is the default OT visibility tool.

## 8.2 TAP vs SPAN

There are two ways to get a copy of traffic to a sensor:

| | Network TAP | SPAN / mirror port |
|---|-------------|--------------------|
| What it is | A hardware device inserted on a link that copies traffic to a monitor port | A switch feature that mirrors selected ports/VLANs to a monitor port |
| Fidelity | Lossless, sees everything including errors | Can drop packets under load; oversubscription possible |
| Impact | Passive, no switch load; must break the link to install (planned window) | No cabling change, but consumes switch CPU/backplane |
| Best for | Critical links where completeness matters | Broad, cheap coverage where occasional loss is acceptable |

Prefer **TAPs on critical links** (the boundary, key control segments) and use **SPAN for breadth**. Whichever you use, remember a mirror only shows the traffic on the ports/VLANs it's configured for — a sensor sees exactly what you feed it and nothing else.

## 8.3 Placement follows Purdue

Sensor placement is a direct application of Chapter 05:

- **The IT/OT boundary (Level 3.5)** — the first and cheapest sensor; catches the pivot and boundary crossings (north–south).
- **Control segments (Level 1–2)** — see the protocol writes, program downloads, and east–west lateral movement that never leave the OT network.
- **A dedicated Layer-2 tap on the station/process bus** — mandatory for **GOOSE and Sampled Values**, which do not route and are invisible to any sensor north of the boundary.
- **Per-area sensors** — in large plants, one sensor per Level-2 area/cell so intra-area traffic is seen.

A useful staging: boundary first (fast value), then critical control segments, then fill in areas and L2 buses.

## 8.4 Capture engineering

Getting a clean, complete capture is real engineering:

- **Size for peak.** Provision the sensor NIC and storage for peak traffic, not average, or you'll silently drop packets under load.
- **Accurate timestamps.** Detections and MTTD depend on time; keep the sensor clock disciplined (NTP/PTP) and consistent with the SIEM.
- **Aggregation.** TAP aggregators or packet brokers combine multiple links into one sensor feed; watch for oversubscription.
- **Verify the feed is alive.** A dead tap or a reconfigured SPAN is a **silent blind spot** — the worst kind, because everything looks fine while you see nothing. Make "is the sensor still receiving expected traffic?" an explicit, monitored check (this is log-validation, Chapter/Companion TDA).

## 8.5 Baselining — the payoff of visibility

Passive capture over **30–90 days** yields the allow-lists that power most OT detection and hunting:

- **Asset allow-list** — IP, MAC, vendor, model, zone, role (from passive discovery + the CMDB).
- **Conversation allow-list** — src, dst, port, protocol, expected rate (from Zeek conn.log).
- **Command allow-list** — which sources may issue which function codes to which targets (from protocol logs confirmed with engineering).
- **Software / account allow-lists** — from host telemetry (Chapter 09).

These baselines are what make "something new" meaningful in OT. Because the environment is small and stable (Chapter 01), a clean baseline turns most hunts into "show me what's not on the list."

## Chapter summary
- Capture **passively**; active work on control devices needs a written window and supervision.
- **TAPs** are lossless (use on critical links); **SPAN** is cheap and broad (watch for drops).
- Place sensors by Purdue: boundary first, then control segments, with a **dedicated L2 tap for GOOSE/SV**.
- Engineer the capture: size for peak, accurate time, and **continuously verify the feed** (a dead tap is a silent blind spot).
- 30–90 days of passive capture builds the **asset/conversation/command allow-lists** that power detection and hunting.

## Cross-references
- Chapter 05 (Purdue) locates the taps; Chapter 09 covers what else to collect; Chapter 19 (Zeek) processes the capture.
- Companion: `sis-safety-detection/docs/monitoring-architecture.md`, and TDA log-validation (verify the feed).
