# MQTT

## Snapshot
| Property | Value |
|----------|-------|
| Port/transport | TCP/1883 (8883 TLS) |
| Purdue | L2–L3, IIoT/edge, DMZ; broker-centric |
| Auth | Optional user/pass; frequently anonymous; TLS often off |
| Telemetry | Zeek `mqtt.log`, broker logs, NDR, pcap |

## What it is
A lightweight publish/subscribe messaging protocol common in IIoT and modern edge/telemetry architectures. Clients publish to and subscribe from **topics** on a central **broker**; there's no direct device-to-device link — everything flows through the broker.

## What it really means for a defender
MQTT's risk is the broker and its **topic access control** — which is frequently absent. If the broker allows anonymous connect and doesn't enforce topic ACLs, **any client can subscribe to everything (mass recon via wildcard) and publish to command topics (impact).** The range's "publish to command topic" is exactly this: a PUBLISH to a topic the PLC/edge gateway acts on. Two signals dominate: **wildcard subscribes** (`#` / `+`) that vacuum up the whole process telemetry, and **publishes to control/command topics from unexpected clients**. The broker is your best sensor — its logs see every connect, subscribe, and publish.

## Attacker actions (recon → impact)
- **Discover:** connect (often anonymously); subscribe to `#` to enumerate every topic and its data — the entire process in one move.
- **Read (recon):** watch telemetry topics.
- **Publish (impact):** PUBLISH to a command/control topic that the consuming device acts on ("ShockPLC"); tamper with **retained** messages so the malicious value persists for new subscribers.
- **Disrupt:** publish malformed/oversized payloads; connect-flood the broker.

## Detections you can build
| Detection | Signal / logic | Log source | ATT&CK ICS |
|-----------|----------------|------------|------------|
| Publish to command topic | PUBLISH to a control/command topic from a non-authorized client id | `mqtt.log`, broker log | T0855 Unauthorized Command Message, T0831 |
| Wildcard subscribe (mass recon) | SUBSCRIBE with `#` or high-level `+` | `mqtt.log`, broker log | T0846 Remote System Discovery |
| Anonymous / new client connect | CONNECT with no auth or a new client id | broker log | T0822 External Remote Services |
| Retained-message tampering | Retained flag set on a command-topic publish | `mqtt.log` | T0856 Spoof Reporting Message |
| Auth failure spike | Repeated CONNECT auth failures | broker log | T0859 |
| Cross-zone MQTT | 1883 crossing IT→OT/DMZ boundary unexpectedly | firewall/NDR | T0885 |

## Log sources & telemetry
The **broker's own logs** are the richest source (connects, client ids, subscribe/publish per topic, auth results) — get them into the SIEM. Zeek `mqtt.log` gives connect/publish/subscribe and topic on the wire. NDR flags new clients and topic anomalies. Note: TLS (8883) blinds network DPI — rely on broker logs there.

## Functions/services to watch
CONNECT (auth, client id, anonymous), SUBSCRIBE (topic filters — `#`/`+` wildcards), PUBLISH (topic, retained flag, QoS), to/for **command/control topics** specifically. Baseline the legitimate client-id ↔ topic map.

## ATT&CK mapping
T0855 Unauthorized Command Message · T0831 Manipulation of Control · T0846 Remote System Discovery · T0856 Spoof Reporting Message · T0822 External Remote Services.
