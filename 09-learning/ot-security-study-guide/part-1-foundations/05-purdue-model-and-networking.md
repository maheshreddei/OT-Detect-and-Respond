# Chapter 05 — The Purdue Model and OT Networking

> Part I · Foundations. The Purdue model is the map every OT defender works from. It tells you where assets live, what should talk to what, where to place your eyes, and how to reason about an intrusion's movement. Master this chapter and much of the rest of the guide becomes "apply the map."

## 5.1 The Purdue Enterprise Reference Architecture

The **Purdue model** organizes a plant into hierarchical **levels**, from the physical process at the bottom to enterprise IT at the top. Its power is that it maps the *logical* trust hierarchy of a plant onto a structure you can segment and monitor.

```
  Level 5  ── Enterprise network (corporate IT, internet-facing)
  Level 4  ── Business logistics (ERP, email, corporate services)
 ─────────────  IT / OT DMZ (Level 3.5)  ─── the boundary ───────────
  Level 3  ── Site operations (historian, MES, domain, patch, jump host)
  Level 2  ── Supervisory control (HMI, SCADA master, EWS)
  Level 1  ── Basic control (PLC, RTU, PAC) and Safety (SIS)
  Level 0  ── The physical process (sensors, actuators)
```

- **Level 0 — Process.** The physical edge: sensors and actuators. Watched *through* Level 1, never instrumented directly.
- **Level 1 — Basic control.** Controllers (PLC/RTU/PAC) and, importantly, the **safety system (SIS)**, which is logically separate even though it lives at this level.
- **Level 2 — Supervisory.** HMIs, SCADA masters, engineering workstations — where humans supervise and program.
- **Level 3 — Site operations.** Plant-wide IT-like services that still belong to OT: historian, MES, OT domain controllers, patch/AV servers, the jump host.
- **Level 3.5 — the DMZ.** The demilitarized zone between OT and IT. **This is the boundary you defend hardest** — every legitimate IT↔OT exchange should pass through controlled brokers here (a jump host, a data diode, a replicated historian), and nothing should cross it directly.
- **Levels 4/5 — Enterprise.** Corporate IT and the internet. Not OT, but the origin of most intrusions that eventually reach OT.

## 5.2 Zones and conduits (IEC 62443)

Purdue gives you levels; **IEC 62443** gives you the security construct layered on top: **zones and conduits.**

- A **zone** is a grouping of assets that share the same security requirements and trust level (e.g. "the polymer unit control zone," "the DMZ").
- A **conduit** is a controlled communication path *between* zones (e.g. the specific, firewalled link that carries historian data from the control zone to the DMZ).

The discipline is: put like-trust assets in a zone, define exactly which conduits may cross zone boundaries and what they may carry, and enforce and monitor those conduits. Because the protocols themselves provide no security (Chapter 06), **segmentation via zones and conduits is the compensating control that does the heavy lifting** — and the conduits are precisely where you place detection.

## 5.3 The two high-signal rules the map gives you

The Purdue/zone map immediately yields two of the highest-value detections in all of OT, because they describe things that should *never* happen in a correctly segmented plant:

1. **A control protocol crossing a zone boundary the wrong way.** Modbus, S7, DNP3, or IEC-104 originating from IT and reaching a controller means the IT/OT boundary has been breached or misconfigured. Control protocols should be intra-zone.
2. **An IT/access protocol reaching a control asset.** VNC, RDP, FTP, or HTTP from an unexpected source straight to a PLC or EWS is the classic pivot — an attacker using IT tools to reach OT.

Both are "abnormal by architecture" — you don't need a signature of malice, just knowledge of where the boundaries are. This is why the map is a prerequisite for detection.

## 5.4 North–south vs east–west

Two directions of traffic, two kinds of risk:

- **North–south** traffic crosses levels/zones — IT to OT, DMZ to control. This is where boundary crossings and the initial pivot show up. Watch the DMZ and inter-level conduits.
- **East–west** traffic moves laterally *within* a level — controller to controller, cell to cell, HMI to PLC. This is where an attacker who is already inside spreads. East–west is the classic OT blind spot; a new east–west conversation between assets that never talked before is high-signal.

A complete monitoring design sees both: boundary/conduit taps for north–south, and control-segment taps for east–west.

## 5.5 Where to place your eyes

Sensor placement follows directly from the map (Chapter 08 covers the engineering; here is the logic):

- **The IT/OT boundary (Level 3.5)** is the cheapest, highest-value vantage point — it catches the pivot and boundary crossings, and it's usually the easiest place to tap.
- **Control-segment taps (Level 1–2)** see intra-OT and east–west traffic — the protocol writes, program downloads, and lateral movement.
- **A dedicated Layer-2 tap** is required for **GOOSE and Sampled Values (IEC 61850)** and other L2 protocols, because they do **not** cross routers — a sensor north of the boundary is blind to them. If you protect a substation, you must tap the station bus itself.

A useful heuristic for prioritization: **consequence rises as you go down the levels.** A detection at Level 1 (a controller write) is closer to the physical process — and thus higher consequence — than one at Level 3.

## 5.6 OT networking realities

A few networking facts shape everything:

- **Flat networks are common.** Many real plants have little internal segmentation — one big control VLAN. Where the network is flat, *segmentation itself becomes part of the security program*, and until it exists, monitoring is your primary control.
- **Legacy and fragile.** Switches, media converters, and serial-to-Ethernet gateways abound. Devices can be sensitive to scanning and unusual traffic — reinforcing passive-first.
- **Serial and radio persist.** Especially for RTUs at remote sites; monitoring there is polling- or gateway-based, not sensor-per-site.
- **Deterministic timing.** Some control networks (PROFINET IRT, EtherCAT) have hard real-time requirements; never insert anything inline.

## 5.7 The map as a hunting tool

Finally, the Purdue/zone map is not just an architecture diagram — it is an active hunting tool. Overlay your **asset inventory** on it (which asset is in which zone) and your **conversation baseline** (which zones legitimately talk). Then hunting becomes concrete questions: *Is anything talking across a conduit that shouldn't? Is any asset in the wrong zone? Did a new north–south or east–west path appear?* The map turns "look for bad things" into "look for traffic that violates the architecture" — which is far more tractable.

## Chapter summary

- The **Purdue model** organizes the plant into levels 0–5 with a **DMZ at 3.5**; **IEC 62443 zones and conduits** add the security construct on top.
- Segmentation is the compensating control for insecure protocols; **conduits are where you detect.**
- Two architecture-level detections: **control protocols crossing a boundary** and **IT/access protocols reaching control assets.**
- Watch both **north–south** (pivot/boundary) and **east–west** (lateral); the boundary is the cheapest high-value tap, control segments catch the process-level actions, and **L2 protocols need a local tap.**
- Consequence rises toward Level 0; the map is an active hunting tool when overlaid with asset and conversation baselines.

## Cross-references
- Chapter 08 (passive visibility) engineers the taps this chapter locates.
- Chapter 06 (protocols) explains *what* crosses the conduits.
- Chapter 27 (hardening/62443) formalizes zones, conduits, and security levels.
- Companion repositories: `ot-monitoring-deployment` (Purdue-aligned onboarding), `ot-protocol-defense` (zone-crossing detections).
