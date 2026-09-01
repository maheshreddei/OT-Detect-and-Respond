# Nmap / Scanning & Reconnaissance

## Snapshot
| Property | Value |
|----------|-------|
| Nature | Active host/port/service discovery (not a protocol) |
| Where seen | Any segment an attacker can reach; especially early in an intrusion |
| Telemetry | NetFlow, NDR/Zeek `conn.log`, firewall logs |

## What it is
Scanning is how an attacker (or a careless tool) maps the network: which hosts are alive, which ports are open, which services and versions respond. In the range it's the discovery step that precedes any protocol-specific action.

## What it really means for a defender
In IT, scanning is background noise. **In a steady-state OT network it is not** — the set of talkers and flows is small and stable, engineering tools poll *known* devices in *known* patterns, and legacy control devices can be **knocked over by aggressive scans** (fragile TCP stacks, tight resource limits). So scanning in OT is both a strong intrusion signal *and* a safety concern. Active scanning of OT segments should essentially never come from an unexpected source — which makes it one of the highest-signal, lowest-false-positive things you can watch for.

## Attacker actions (recon → impact)
- **Discover:** host sweep (ARP/ICMP/TCP), port scan, service/version detection, OS fingerprint.
- **Enumerate:** targeted probes of discovered services (feeds every protocol page that follows).
- Scanning itself doesn't change the process, but it *precedes* the writes that do — catching it buys the most response time.

## Detections you can build
| Detection | Signal / logic | Log source | ATT&CK ICS |
|-----------|----------------|------------|------------|
| Horizontal scan | One source → many destinations on the same port in a short window | NetFlow, `conn.log` | T0846 Remote System Discovery |
| Vertical scan | One source → many ports on one host | NetFlow, `conn.log` | T0840 Network Connection Enumeration |
| Connection-attempt spike | Surge in SYN/failed connections from one source | firewall, `conn.log` (state) | T0846 |
| Scan from unexpected source | Any scan pattern from a host not on the engineering/management baseline | NDR + baseline | T0846 |
| OT-service probing | Probes to control ports (502/102/2404/20000/44818/47808) from a non-master | NDR/Zeek | T0846, T0842 |

## Log sources & telemetry
Primary: NetFlow/IPFIX and Zeek `conn.log` (fan-out patterns), firewall logs (deny spikes). NDRs flag scanning natively. Because scanning is flow-shaped, you can catch it without DPI — good coverage even on segments you only see via flow.

## Functions/services to watch
Fan-out (one→many hosts) and fan-in-of-ports (one host→many ports); connection failure ratios; probes specifically to OT control ports.

## ATT&CK mapping
T0846 Remote System Discovery · T0840 Network Connection Enumeration · T0842 Network Sniffing (passive recon).
