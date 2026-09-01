# EtherNet/IP + CIP

## Snapshot
| Property | Value |
|----------|-------|
| Port/transport | TCP/44818 (explicit), UDP/2222 (implicit I/O), UDP/44818 (ListIdentity) |
| Purdue | L1–L2 (Rockwell/Allen-Bradley ControlLogix/CompactLogix, many vendors) |
| Auth | **None** in base CIP (CIP Security optional, rarely deployed) |
| Telemetry | ICSNPP `enip.log`/`cip.log`, NDR, pcap |

## What it is
EtherNet/IP carries the **Common Industrial Protocol (CIP)** — an object-oriented model of classes, instances, and attributes. Rockwell PLCs expose **symbolic tags**; clients read/write tags and CIP attributes over explicit messaging, with a `forward_open` establishing connected sessions for I/O.

## What it really means for a defender
CIP splits into **Get** (read attributes/tags — recon) and **Set / tag-write** (impact). The range's "write ShockPLC command tags" is a CIP tag write to a Rockwell controller. Device discovery is trivially loud — **ListIdentity** (UDP/44818, often broadcast) enumerates every EtherNet/IP device and its identity, a strong recon signal. Defensive priorities: ListIdentity sweeps, `forward_open` and tag writes from non-controller sources, and Set_Attribute to config classes. As with the others: baseline the legitimate controllers/EWS and alert on writes from anyone else.

## Attacker actions (recon → impact)
- **Discover:** ListIdentity / ListServices (UDP/44818) to enumerate devices; read Identity object (vendor/product/rev).
- **Recon:** Get_Attribute_Single/All; enumerate the tag/symbol list.
- **Session:** forward_open to establish connected messaging.
- **Write (impact):** CIP tag write / Set_Attribute to change a tag or configuration value ("ShockPLC").
- **Disrupt:** writes to config classes; assembly-object manipulation.

## Detections you can build
| Detection | Signal / logic | Log source | ATT&CK ICS |
|-----------|----------------|------------|------------|
| Tag / Set_Attribute write from non-controller | CIP write service from a host outside the controller/EWS baseline | `cip.log` | T0836 Modify Parameter, T0831 |
| ListIdentity sweep | UDP/44818 ListIdentity to many hosts / from unexpected source | `enip.log` | T0846 Remote System Discovery |
| Tag enumeration | Bulk symbol/tag list reads from new client | `cip.log` | T0846, T0888 |
| forward_open from unexpected source | Connection establishment from non-controller | `enip.log` | T0855 Unauthorized Command Message |
| Write to config class | Set_Attribute to identity/config/assembly classes | `cip.log` | T0836 |
| New EtherNet/IP client | First-time source speaking CIP to a PLC | NDR + baseline | T0836 |
| Cross-zone ENIP | 44818/2222 crossing IT→OT boundary | firewall/NDR | T0885 |

## Log sources & telemetry
ICSNPP `enip.log` / `cip.log` expose CIP service, class, instance, attribute, and (for Rockwell) tag names — the fields for read-vs-write and target-object detections. NDRs carry EtherNet/IP policies. pcap decodes the written tag/value; historian confirms impact.

## Functions/services to watch
**Discovery:** ListIdentity, ListServices (UDP/44818). **Recon:** Get_Attribute_Single/All, Get_Attributes; symbol/tag enumeration. **Session:** ForwardOpen/ForwardClose. **Impact:** Set_Attribute_Single/All, CIP tag **write** services. Watch the CIP class/service pairs against a baseline of normal controller traffic.

## ATT&CK mapping
T0836 Modify Parameter · T0831 Manipulation of Control · T0846 Remote System Discovery · T0888 Remote System Information Discovery · T0855 Unauthorized Command Message · T0885 Commonly Used Port.
