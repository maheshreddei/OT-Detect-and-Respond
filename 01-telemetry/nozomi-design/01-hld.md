# Nozomi High-Level Design (HLD)

## 1. Objective

Provide passive, resilient visibility of OT assets, industrial protocols, abnormal behavior and security events without placing Nozomi inline with control traffic. The design supports local operations, enterprise SOC monitoring, incident investigation and auditable telemetry assurance.

## 2. Scope and assumptions

The reference estate contains an enterprise/SOC zone, an industrial DMZ (IDMZ), Level 3 site operations, Level 2 supervisory control, Level 1 controllers and Level 0 process devices. Adapt zone names to the approved IEC 62443 zone-and-conduit model and site network drawings.

Nozomi does not replace firewalls, endpoint protection, backups, safety systems or process-engineering controls. Passive discovery sees only traffic presented to the sensor. Silent, serial, air-gapped, powered-off, locally switched or unmirrored devices can remain invisible.

## 3. Logical architecture

~~~text
Enterprise SOC / SIEM / Ticketing / Identity / NTP / DNS
                         |
                  [CMC or Vantage]
                         |
                 Enterprise/OT DMZ
                    management FW
                         |
            Dedicated OT security-management network
               |                 |                 |
         [Guardian A]      [Guardian B]      [Guardian site N]
          mgmt | mon        mgmt | mon
               |                 |
       TAP / Packet Broker / SPAN destinations
               |
     L3 site core -- L2 cell/area -- L1 controller networks
                              |
                    [Remote Collector]
                     remote small segment
~~~

Monitoring traffic flows one way from TAP/SPAN/broker toward monitoring ports. Management traffic is explicitly allowed through firewalls from approved administration and integration systems. A monitoring interface must never bridge, route, or transmit into the production control network.

## 4. Monitoring-point strategy

Select points from traffic objectives:

| Priority | Monitoring point | Visibility gained | Main limitation |
|---|---|---|---|
| P1 | IDMZ/Level 3 firewall inside and outside | IT/OT ingress, remote access, north-south sessions | Does not show local cell traffic |
| P1 | Level 3 distribution/core trunks | Site-wide server, historian, engineering and inter-zone traffic | Oversubscription/duplicate packets |
| P1 | Level 2 to Level 1 cell/area boundary | HMI/SCADA-to-PLC commands and controller communications | One feed required per isolated cell path |
| P2 | Safety/security zone boundary | Access to SIS and other critical conduits | Safety approval and strict passive design |
| P2 | Vendor remote-access conduit | Jump host and third-party sessions | Encrypted payload may limit content inspection |
| P2 | Wireless/IIoT gateway uplink | Wireless/IoT assets and gateway communications | Local radio traffic may not traverse uplink |
| P3 | Redundant control-network paths | Failover and east-west visibility | Both paths may create duplicates |
| P3 | Remote substations/skids | Distributed assets via Remote Collector | WAN bandwidth and collector capacity |

Choose the fewest points that answer: who talks to whom, which protocol/function is used, whether commands cross a zone, and whether both redundant paths are visible.

## 5. Component placement

- **Guardian:** one per major site or visibility domain when traffic can be locally aggregated within supported throughput. Place its management interface on an OT security-management VLAN, not directly on the enterprise user LAN.
- **CMC:** central management zone accessible to the SOC and permitted to communicate with downstream Guardians. Design HA and DR according to the licensed product/version.
- **Remote Collector:** small or bandwidth-constrained locations. It captures and securely forwards to assigned Guardian(s); confirm WAN bandwidth, latency, TLS/certificate lifecycle and outage behavior.
- **Packet broker:** aggregate, filter, replicate, timestamp, deduplicate or load-balance capture traffic when many links exceed practical direct monitoring-port count.
- **TAP:** preferred on critical links where deterministic, full-duplex capture and independence from switch CPU/configuration are important.
- **SPAN/RSPAN/ERSPAN:** acceptable where load, platform behavior and failure modes are understood and tested.

## 6. Availability and failure domains

A Nozomi sensor failure must not interrupt control traffic because monitoring is out of band. Dual power, redundant management switching, monitored UPS, spare optics/cables and configuration backups reduce monitoring outage. Do not combine two redundant production paths into a single failure-prone aggregation point without documenting the risk.

Define monitoring availability targets separately from process availability. Alert when packet input becomes zero unexpectedly, interfaces flap, sensors become stale, resources exceed thresholds, clock drift occurs, or CMC synchronization fails.

## 7. Security architecture

- Dedicated management VLAN/VRF with deny-by-default ACLs.
- Admin access through approved jump hosts; MFA/SSO/RBAC where supported.
- Named accounts; no shared daily-use administrator credentials.
- TLS certificates from approved PKI; planned rotation for Guardian/CMC/collector relationships.
- NTP from trusted OT sources; consistent time zone and UTC-normalized logs.
- DNS only if required; static addressing and documented routes.
- Egress allowlisting for licensing, updates, support or Vantage, as applicable.
- Syslog/API integration to SIEM over authenticated/encrypted channels where supported.
- Backups, configuration exports and recovery tests protected as sensitive OT information.
- No internet browsing or general user workload from sensor systems.

## 8. Sizing inputs and decision gates

Record for normal and peak periods: Mbps, packets/second, average packet size, VLAN count, unique MAC/IP nodes, protocols, concurrent sessions, broadcast/multicast rate and projected growth. Add remote-capture bandwidth and duplicate-feed overhead. Compare measured values with the exact Guardian/collector technical specification and license.

The final BOM is not approved until Nozomi or an authorized partner validates sizing. Link speed is not sensor throughput: a 10-Gb link may carry 100 Mb/s, while many small packets can create high processing load.

## 9. Integrations

| Integration | Direction | Purpose | Design requirement |
|---|---|---|---|
| CMC/Vantage | Guardian outbound/bidirectional per product | Centralized management and analytics | Explicit firewall matrix and certificates |
| SIEM | Nozomi to SIEM | Alerts, audit and asset events | Parsing, field mapping, rate limit and health alert |
| SOAR/ticketing | API/event flow | Case creation and enrichment | Human approval for OT containment |
| AD/LDAP/SAML | Management plane | Authentication/RBAC | Break-glass local account |
| NTP/DNS/SMTP | Management plane | Time, naming, notification | OT-approved infrastructure |
| CMDB/vulnerability workflow | API/export | Asset ownership and remediation | Source-of-truth and conflict rules |

## 10. Outcomes and acceptance criteria

- Critical conduits have documented packet visibility in both expected directions.
- Known assets, VLANs and industrial protocols appear with correct zone/site context.
- Management access is restricted and audited.
- Packet loss, oversubscription and duplicate-capture risks are measured.
- Alerts reach the SIEM/ticketing workflow with correct timestamps and severity.
- Monitoring outages generate operational alarms.
- Baseline learning and tuning are approved by operations; false-positive handling has owners and SLAs.
- As-built diagrams, port maps, configuration evidence, rollback records and support handover are complete.
