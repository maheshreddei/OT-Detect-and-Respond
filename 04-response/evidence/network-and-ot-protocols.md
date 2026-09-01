# Evidence: Network & OT Protocols

Network evidence is the OT investigator's best friend: it is **passive, non-disruptive, and often ground truth.** A packet capture of a Modbus write or an S7 program download is the command itself — not an inference about it. Lead with network evidence before touching any host or controller.

## Primary sources

### OT network monitoring (Nozomi / Dragos / Claroty)
- **Alerts**: the correlated detection (unauthorized write, program transfer, new asset, protocol anomaly). Export the alert *and* the underlying session/flow it references.
- **Asset inventory & deltas**: a new/changed asset around the incident window proves a rogue device or foothold. Export the inventory snapshot and change log.
- **Protocol/session records**: source/dest, protocol, function, timing.
- Collect: export from the NDR console or its SIEM feed; note sensor placement (which segment it sees).

### Zeek logs (with ICSNPP OT parsers)
Location: Zeek log directory (`conn.log`, `dns.log`, `ssl.log`, `weird.log`, and ICSNPP `modbus.log`, `dnp3.log`, `s7comm.log`, `enip.log`, `bacnet.log`, `iec104.log`, `opcua*.log`).
| Prove | Log & fields |
|-------|--------------|
| A connection existed | `conn.log` — src/dst, ports, duration, bytes, state |
| A Modbus write/read | `modbus.log` — function code, unit id, address |
| An S7 program download | `s7comm.log` — rosctr/function, job type |
| A DNP3 operate | `dnp3.log` — function code, object/CROB |
| Protocol violations | `weird.log` — malformed/anomalous traffic |

### Full packet capture (pcap) — the ground truth
- Source: SPAN/mirror port or **network tap** on the relevant segment. Taps are preferred (fail-safe, no switch load).
- Collect: `tcpdump -i <iface> -w capture-$(date +%s).pcap` (or the tap appliance's capture). **Hash the pcap immediately** when the capture stops.
- Proves: the exact bytes — the verbatim command, the payload, the handshake. Where an NDR alert says "a write occurred," the pcap shows *which register to what value*.
- Analyze on a copy with Wireshark (ICS dissectors) / tshark / Zeek offline.

### Boundary & infrastructure logs
| Source | Proves | Collect |
|--------|--------|---------|
| IT/OT firewall (allow/deny) | The specific cross-zone connection; blocked attempts | Firewall log export / SIEM |
| NetFlow / IPFIX | Flow shape & volume (exfil, scanning, traversal) | Flow collector export |
| Switch/router | MAC/ARP tables (device presence), port security events | Device CLI capture (snapshot state early) |
| Remote-access gateway / VPN | Remote session establishment (see identity guide) | Gateway logs |
| DNS | C2/beaconing, DGA, external resolution from OT | DNS server / Zeek `dns.log` |

## Volatile network state — snapshot early
ARP tables, MAC address tables, active session/connection tables, and routing state on switches/firewalls are volatile. Snapshot them (read-only CLI capture) early in the investigation — they place a device on the network at a moment in time and disappear on reboot or timeout.

## Collection discipline
- **Passive only** on OT — never active-scan a production OT segment during IR; you risk disrupting fragile devices.
- Record **sensor/tap placement** so you know what each capture could and couldn't see (a tap north of the boundary won't see intra-zone L2 traffic).
- Preserve the original capture; analyze copies. Hash on collection; note capture start/stop and interface.
- Correlate every network artifact into the master timeline with normalized timestamps (network device clocks drift too).

## What network evidence proves best
- The **exact OT command** issued (with pcap) — writes, operates, stops, program transfers.
- **Cross-zone traversal** (boundary firewall + netflow).
- **Rogue assets** (NDR inventory delta, ARP/MAC).
- **C2 / exfil** (conn/dns logs, netflow).
It is weakest at attribution to a *person* — pair it with host/identity evidence to tie a command to an account and operator.
