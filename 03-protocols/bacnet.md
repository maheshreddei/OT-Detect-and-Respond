# BACnet/IP

## Snapshot
| Property | Value |
|----------|-------|
| Port/transport | UDP/47808 (0xBAC0) |
| Purdue | L2 building automation (BAS/BMS — HVAC, lighting, access) |
| Auth | **None** in classic BACnet (BACnet/SC adds security; new, limited adoption) |
| Telemetry | Zeek `bacnet.log`, NDR, pcap |

## What it is
The dominant building-automation protocol — HVAC, lighting, energy, and sometimes physical-access systems. Devices expose **objects** (Analog/Binary Input/Output/Value, etc.), each with **properties** (notably `present-value`). Discovery is via **Who-Is / I-Am** broadcasts.

## What it really means for a defender
BACnet is unauthenticated UDP, so the model holds: **Who-Is sweeps are recon** (and cheap — one broadcast enumerates every device), **ReadProperty is deeper recon**, and **WriteProperty to a command object's present-value is impact** (override a damper, setpoint, fan, or door). Two BACnet-specific disruption services deserve their own alerts: **DeviceCommunicationControl** (can silence a device's comms — a clean DoS) and **ReinitializeDevice** (reboot/reset). Building systems are often flatter and less monitored than process OT, and increasingly bridge to it (shared networks, shared power/cooling for control rooms) — so BACnet abuse is both a direct safety/comfort issue and a pivot.

## Attacker actions (recon → impact)
- **Discover:** Who-Is broadcast → I-Am responses enumerate every device and instance.
- **Recon:** ReadProperty / ReadPropertyMultiple to enumerate objects and values.
- **Write (impact):** WriteProperty / WritePropertyMultiple to a command object's present-value ("ShockPLC" equivalent) — override HVAC/lighting/access.
- **Disrupt:** DeviceCommunicationControl (stop a device communicating); ReinitializeDevice (reboot).

## Detections you can build
| Detection | Signal / logic | Log source | ATT&CK ICS |
|-----------|----------------|------------|------------|
| WriteProperty to command object | WriteProperty(Multiple) to AO/BO/AV/BV present-value from unexpected source | `bacnet.log` | T0836 Modify Parameter, T0831 |
| Who-Is sweep (recon) | Broad/repeated Who-Is from one source | `bacnet.log` | T0846 Remote System Discovery |
| ReadProperty enumeration | Bulk ReadPropertyMultiple across objects from new client | `bacnet.log` | T0846, T0888 |
| DeviceCommunicationControl | Any DeviceCommunicationControl service | `bacnet.log` | T0814 Denial of Service |
| ReinitializeDevice | Any ReinitializeDevice service | `bacnet.log` | T0816 Device Restart/Shutdown |
| New BACnet writer | First-time source issuing WriteProperty | NDR + baseline | T0836 |

## Log sources & telemetry
Zeek `bacnet.log` exposes the service, object type/instance, and property — the fields for read-vs-write and target-object detections. NDRs carry BACnet policies. pcap confirms the written value; where BAS bridges to process OT, watch that boundary specifically.

## Functions/services to watch
**Discovery:** Who-Is / I-Am. **Recon:** ReadProperty, ReadPropertyMultiple. **Impact:** WriteProperty, WritePropertyMultiple (to AO/BO/AV/BV `present-value`). **Disrupt:** DeviceCommunicationControl, ReinitializeDevice. Baseline which controllers legitimately write.

## ATT&CK mapping
T0836 Modify Parameter · T0831 Manipulation of Control · T0846 Remote System Discovery · T0888 Remote System Information Discovery · T0814 Denial of Service · T0816 Device Restart/Shutdown.
