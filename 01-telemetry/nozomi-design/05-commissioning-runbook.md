# Commissioning, Validation and Operational Handover

## 1. Pre-commissioning gate

Verify approved HLD/LLD, BOM, licenses, support entitlement, backups, change/MOC, safety permit, rack/power/cooling, cable plan, IP/firewall approvals, PKI/NTP/DNS, named administrators, integration owners, rollback plan and maintenance window.

## 2. Layered validation

### Physical and platform

- Correct model/serial/asset tag and supported software version.
- Redundant power/UPS status and environmental health.
- Management and monitoring cables match as-built map.
- Expected link speed/duplex; no new errors, flaps or optical alarms.
- CPU, RAM, disk and interface health within approved baseline.

### Management plane

- Admin access works only from allowed jump hosts.
- Denied source cannot access the UI/API.
- RBAC roles enforce least privilege; audit logs record logon/configuration.
- NTP is synchronized and timestamps match SIEM.
- Certificates validate and expiry monitoring exists.
- Guardian-to-CMC/Vantage/collector health is good.
- Backup/export and restore procedure is demonstrated.

### Packet visibility

For each capture point, prove:

1. Packets increment on the intended monitoring interface.
2. Expected source/destination pairs appear.
3. Both directions are present.
4. VLAN tags/site origin are correct.
5. Industrial protocols and functions are decoded as expected.
6. Expected critical assets are discovered.
7. A known safe test conversation is visible.
8. Peak Mbps/PPS stays within designed capacity.
9. Switch, TAP and broker show no unexplained drops.
10. Duplicate-flow rate is understood.

A zero-traffic feed during a quiet process period is not automatically a failure; correlate with production schedule. Conversely, link-up alone is not success.

### Detection and integrations

- Generate an approved benign test condition or vendor test event—never unsafe process manipulation.
- Confirm event in Guardian, CMC/Vantage, SIEM and ticketing.
- Validate severity, timestamp, source site, asset identity, rule name and case routing.
- Confirm SOC escalation and OT-owner acknowledgment.
- Test sensor/collector loss alert and restoration notification.

## 3. Coverage reconciliation

Compare Nozomi inventory with the engineering asset list. Classify each gap:

- Device silent or powered off.
- Traffic never crosses monitored point.
- Serial/proprietary/non-Ethernet segment.
- Encrypted or unsupported protocol.
- Reused IP/overlapping site identity.
- SPAN/TAP direction/tagging/filter problem.
- Capacity loss or capture outage.
- Incorrect zone/site mapping.
- Asset inventory error.

Do not claim “100% coverage” from a node count. Report coverage by critical conduit, asset class, protocol, direction and operational scenario.

## 4. Performance baseline

Capture at least normal load, startup/shutdown if safe, batch transition, maintenance/vendor-access period and redundancy failover if approved. Record average/95th/peak Mbps and PPS, packet drops, CPU/RAM/disk, node/license utilization, event rate, storage growth and Remote Collector WAN usage.

## 5. Operational SOP

Daily:

- Sensor/collector/CMC health, stale state and input-rate anomalies.
- Critical alerts and failed integrations.
- Time synchronization and storage warnings.

Weekly:

- Capture-point trends, packet drops, unexpected zero traffic.
- New assets, new protocols, unmanaged devices and high-risk changes.
- Tuning effectiveness and aged cases.

Monthly/quarterly:

- Coverage versus network changes.
- Account/RBAC and certificate review.
- Capacity/license/retention forecast.
- Backup/restore evidence and software/content lifecycle.
- SPAN/broker configuration drift and TAP/cable inspection.
- Use-case coverage against threat model and incident lessons.

## 6. RACI

| Activity | OT asset owner | Network | OT security/Nozomi | SOC | Vendor |
|---|---|---|---|---|---|
| Approve monitoring scope | A | C | R | C | C |
| Configure SPAN/TAP/broker | C | R/A | C | I | C |
| Configure Guardian/CMC | C | C | R/A | C | C |
| Alert triage | C | I | R | R/A | C |
| Process-impact decision | R/A | C | C | C | I |
| Platform upgrade | C | C | R/A | I | C |
| Incident containment | A | R | R | C | C |

R = Responsible, A = Accountable, C = Consulted, I = Informed. Tailor locally.

## 7. Acceptance record

For each requirement capture ID, test method, expected result, actual result, evidence link, tester, date, status, defect, owner and retest. Open defects must have risk acceptance or remediation date; “visible in dashboard” is insufficient evidence.

## 8. Handover package

As-built HLD/LLD, asset/BOM, rack and cable maps, IP/firewall matrix, SPAN/TAP/broker configs, account/RBAC matrix, certificates/expiry owners, backup/recovery, health thresholds, SIEM mappings, use-case owners, tuning register, capacity baseline, acceptance evidence, support/escalation matrix, known limitations and next coverage improvements.
