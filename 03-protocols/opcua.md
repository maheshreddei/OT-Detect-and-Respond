# OPC UA

## Snapshot
| Property | Value |
|----------|-------|
| Port/transport | TCP/4840 (opc.tcp); also HTTPS |
| Purdue | L2–L3 (gateways, historians, MES, modern PLCs) |
| Auth | **Supports** anonymous/user/cert + None/Sign/SignAndEncrypt — but often misconfigured to None/anonymous |
| Telemetry | ICSNPP `opcua*.log`, server audit logs, NDR, pcap |

## What it is
The modern, platform-neutral industrial protocol — a structured **address space** of nodes (variables, objects, methods) that clients browse, read, write, subscribe to, and call. Unlike the legacy protocols, OPC UA *has* real security (authentication, signing, encryption). The risk is that it's frequently **turned off**.

## What it really means for a defender
OPC UA can be secure — so the defender's job is largely **detecting insecurity and misuse**: sessions established **anonymously** or with **security mode None**, when policy requires certificates and encryption. Beyond that it follows the model: **Browse is reconnaissance** (walking the address space to map the process) and **Write / CallMethod are impact** (changing a command node's value, invoking a method). The range's "write ShockPLC command nodes" is a Write service to a specific NodeId. Watch for anonymous/None sessions, browse sweeps from unexpected clients, and writes/method-calls to control nodes.

## Attacker actions (recon → impact)
- **Discover:** GetEndpoints (enumerate security policies/endpoints); connect, ideally anonymously / mode None.
- **Recon:** Browse the address space; Read node attributes — full process map.
- **Write (impact):** Write to a command/control node value ("ShockPLC").
- **Method (impact):** CallMethod to invoke a control method.
- **Subscribe:** create subscriptions/monitored items to watch values (recon/exfil).

## Detections you can build
| Detection | Signal / logic | Log source | ATT&CK ICS |
|-----------|----------------|------------|------------|
| Anonymous / None session | ActivateSession with anonymous token or securityMode None (vs policy) | `opcua.log`, server audit | T0859 Valid Accounts, T0822 |
| Write to command node | Write service to a control NodeId from unexpected client | `opcua.log` | T0836 Modify Parameter, T0831 |
| CallMethod to control method | Call service invoking a control method | `opcua.log` | T0831 Manipulation of Control |
| Browse sweep (recon) | Broad Browse/Read across the address space from new client | `opcua.log` | T0846 Remote System Discovery |
| Endpoint enumeration | GetEndpoints from unexpected source | `opcua.log` | T0846 |
| Cert/session anomaly | New/unknown client cert; session churn | server audit | T0859 |
| New OPC UA client | First-time source→server session | NDR + baseline | T0822 |

## Log sources & telemetry
ICSNPP OPC UA binary parser (`opcua*.log`) exposes service type, node ids, and security mode/policy — the fields for anonymous-session and write-node detections. **OPC UA server audit logs** are authoritative for session/auth events — enable and collect them. SignAndEncrypt sessions blind network DPI to payload, so lean on server audit logs there.

## Functions/services to watch
GetEndpoints (recon), CreateSession/ActivateSession (auth token + security mode — watch **anonymous/None**), Browse/Read (recon), **Write** (impact), **CallMethod** (impact), CreateSubscription/CreateMonitoredItems (watch). Baseline client certs and endpoints.

## ATT&CK mapping
T0859 Valid Accounts · T0822 External Remote Services · T0836 Modify Parameter · T0831 Manipulation of Control · T0846 Remote System Discovery.
