# Control Systems and Protocols

## System responsibilities

| System | Main purpose | Typical assets | Cyber significance |
|---|---|---|---|
| DCS | Continuous process control | Controllers, I/O, HMI, EWS, servers | Plant-wide control and operator visibility |
| PLC | Discrete/package control | PLC, remote I/O, drives, package HMI | Local autonomous control and sequences |
| SIS/ESD | Independent risk reduction | Safety logic solver, safety I/O/EWS | High-consequence trip/bypass/configuration |
| F&G | Detect fire/toxic/flammable gas | Detectors, controller, annunciation | Life safety and emergency response |
| SCADA | Remote supervision | Master, RTU, telemetry, comms | Tank farm, pipeline, utilities, remote sites |
| Historian | Time-series record | Collectors, database, interfaces | Investigation and IT/OT conduit |
| APC/optimizer | Improve process performance | Application servers/models | Can influence DCS targets |
| Machinery control | Protect/control turbines/compressors | Dedicated PLC/controllers | Availability and equipment protection |
| Electrical/PMS | Power monitoring/control | Relays, gateways, HMI | Plant-wide common dependency |
| Gateway | Protocol/data translation | Serial/Ethernet/OPC gateway | Trust boundary and visibility limitation |

SIS is independent by design intent; DCS alarms/interlocks do not automatically equal a Safety Instrumented Function.

## Architecture components

Field transmitter → marshalling/remote I/O → controller → control network → HMI/EWS/server. Redundant controllers, networks, power and servers can exist, but redundancy behavior must be learned per vendor.

An HMI displays/commands; a controller executes logic; an engineering workstation changes configuration; a historian records; a gateway translates; an OPC server exposes data; a domain controller authenticates; Nozomi observes copied network traffic.

## Protocol map

| Area | Likely protocols | Learn to recognize |
|---|---|---|
| Instruments | 4–20 mA/HART, FF H1, PROFIBUS PA | Device identity, status, configuration |
| Remote I/O/drives | PROFIBUS DP, PROFINET, EtherNet/IP/CIP | Cyclic I/O, acyclic engineering |
| Serial packages | Modbus RTU, vendor serial | Unit ID, function code, read/write |
| Ethernet packages | Modbus TCP, EtherNet/IP, PROFINET | Client/server roles and writes |
| Siemens controllers | S7comm/S7comm-plus, PROFINET | Engineering/download/mode behavior |
| Integration | OPC DA, OPC UA | Client/server, methods, certificates |
| Historian/Windows | TCP/IP, DNS, Kerberos, LDAP, SMB, RPC, RDP | Identity, file/admin dependencies |
| Infrastructure | SNMP, Syslog, SSH, HTTPS, NTP/PTP | Management and time |
| Electrical | IEC 61850 MMS/GOOSE/SV, Modbus | Protection/control and time sensitivity |
| Remote SCADA | IEC 60870-5-104, DNP3 | Telecontrol, commands and events |
| IIoT | MQTT, AMQP, HTTPS/REST | Broker/topic/API trust |
| Safety networks | PROFIsafe, CIP Safety or vendor-specific | Safety overlays and independence |

## Protocol learning requirements

For each protocol be able to state:

- Physical/transport layer and common port only when verified.
- Master/client and slave/server roles.
- Read versus write/control operations.
- Engineering/configuration capability.
- Authentication/encryption availability and actual use.
- Broadcast/multicast behavior.
- Normal source-destination pairs and frequency.
- What Nozomi can decode.
- Safe collection method.
- Security control at the conduit.

Do not memorize only TCP/UDP ports. In OT, the function code or industrial operation can matter more than the port.

## High-value examples

- Modbus: distinguish read functions from coil/register writes and diagnostics.
- OPC: identify new clients, unexpected browse/read/write, insecure legacy DCOM dependencies and UA certificate/trust issues.
- S7/engineering traffic: recognize downloads, online changes, start/stop and new engineering sources.
- EtherNet/IP/CIP: distinguish I/O from explicit messaging and programming.
- PROFINET: understand discovery/configuration and real-time traffic.
- IEC 61850: understand MMS client/server versus fast multicast GOOSE and why ordinary routing assumptions may fail.
- NTP/PTP: time change can corrupt sequence-of-events investigation.

## Gateways

A gateway can normalize, aggregate or convert protocols, but can hide the original device identity/function from monitoring. Document both sides, translation mapping, management interface, credentials, firmware, logging and failure behavior. Protocol translation is not automatically segmentation or security enforcement.

## Lab-safe learning

Use vendor simulators, isolated virtual PLCs, sample PCAPs and Wireshark. Never connect a learning laptop or protocol tool to a production control network. Practice identifying flows and writing hypotheses before generating any traffic.
