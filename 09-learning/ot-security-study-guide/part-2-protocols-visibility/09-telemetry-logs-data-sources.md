# Chapter 09 — Telemetry, Logs and Data Sources

> Part II. This chapter inventories the telemetry that makes OT hunting and detection possible, and — just as importantly — the order in which to collect it, because you can never onboard everything at once.

## 9.1 The primary OT data sources

| Source | What it gives you | Priority |
|--------|-------------------|----------|
| **Passive network monitoring** (Zeek+ICSNPP / OT-NDR) | Protocol-level actions: reads, writes, program transfers, new conversations | Primary |
| **IT/OT firewall logs** (allow + deny) | Boundary crossings; the cheapest high-value source | Primary |
| **Remote-access authentication** (VPN, jump host) | Who reached OT and when — attribution | Primary |
| **Windows Security + Sysmon** on EWS/HMI/historian | The engineering/host path: process, logon, network, registry | Primary |
| **Historian** (curated tags) | The physical record: setpoints, trips, bypasses, critical values | High |
| **Controller baseline/mode job** | Running-logic checksum and mode, correlated to MOC | High |
| **Switch/router, NetFlow** | Presence, flow shape, breadth where DPI doesn't reach | Supporting |

## 9.2 The allow-lists telemetry builds

The reason to collect this telemetry is to build and maintain the five allow-lists that turn OT's stability into detection power:

- **Asset** — every device: IP, MAC, vendor, model, zone, role.
- **Conversation** — every legitimate src↔dst↔port↔protocol pair and its expected rate.
- **Command** — which source may issue which function code to which target (the highest-value list — it encodes the authorization the protocols lack).
- **Software** — executables and publishers per host role (from Sysmon Event 1 over ~90 days).
- **Account** — which accounts may log on to which hosts, and when (from Windows 4624 plus HR/vendor contracts).

Hunting and detection then reduce, again and again, to "**show me what deviates from the list.**"

## 9.3 The historian as security telemetry

The historian deserves special emphasis because it is unique to OT and uniquely powerful. Curate (don't dump) the tags that carry safety and process meaning:

- Critical **process values** and their **setpoints** (for trip-approach and setpoint-change detection).
- **Trip points** and **trip/demand events** (for safety monitoring).
- **Bypass / inhibit / MOS** status (for protection-defeat detection).
- **Voting / channel-health** and **mode/key-switch** states.

These feed the **process-indicator** detections of Chapter 17 — the ones an attacker cannot avoid touching and cannot easily fake.

## 9.4 Onboarding order: value per effort

You cannot ingest everything on day one, so sequence by **value per unit of effort** (this is the tiered onboarding model):

1. **Boundary firewall + remote-access auth + EWS/HMI host logs** — easy to collect, catch the two most common attack paths (IT→OT pivot and remote-access abuse).
2. **One passive sensor (Zeek) at the boundary** — unlocks protocol visibility.
3. **Controller baseline/mode job** and **curated historian tags** — the OT-specific, high-value additions.
4. **Per-area sensors** and deeper protocol coverage — as the program matures.
5. **Never Field I/O directly** — it's covered via the controller and historian.

## 9.5 A minimal-but-complete stack

If you can only stand up a handful of things, these seven cover most real OT attacks:

1. Firewall logs (allow + deny) at the IT/OT boundary → SIEM.
2. Remote-access authentication logs.
3. Windows Security + Sysmon on every EWS and HMI.
4. One passive sensor with Zeek at the boundary.
5. A controller checksum/mode baseline job with MOC correlation.
6. A sensor per Level-2 area (as you scale).
7. Curated historian tags into the SIEM.

## Chapter summary
- Primary OT telemetry: **passive network, boundary firewall, remote-access auth, EWS/HMI host logs, curated historian, controller baseline** — with NetFlow/switch as support.
- Telemetry exists to build five **allow-lists** (asset, conversation, command, software, account); detection is deviation from them.
- The **historian's safety/process tags** enable the process-indicator detections unique to OT.
- Onboard by **value per effort** (boundary + host + one sensor first); never collect Field I/O directly.
- A seven-source minimal stack covers most real attacks.

## Cross-references
- Chapter 08 (capture) and Chapter 17 (process indicators) sit on either side of this chapter.
- Chapter 22 (SIEM/XDR) is where this telemetry is hunted.
- Companion: `ot-monitoring-deployment/log-onboarding`, `perimeter-to-endpoint-detections/docs/data-sources.md`.
