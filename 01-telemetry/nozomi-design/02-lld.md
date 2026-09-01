# Nozomi Low-Level Design (LLD)

## 1. Required site survey inputs

Do not configure from assumptions. Collect:

- Current logical/physical diagrams, VLAN database, IP plan and IEC 62443 zones/conduits.
- Switch/firewall models, software versions, stacking/VSS/MLAG topology, interface names and utilization.
- Redundancy protocols and all active/standby data paths.
- Critical assets, owners, safety classification and maintenance windows.
- Seven-day minimum traffic statistics; preferably representative production cycles.
- Rack units, dual power, UPS circuits, grounding, temperature, optics and patch-panel details.
- Existing management VRF/VLAN, routing, firewall, proxy, NTP, DNS, PKI and identity services.
- Nozomi appliance/VM model, N2OS version, license, node/throughput limits and retention target.

## 2. Addressing worksheet

| Item | Example only | Final value/owner |
|---|---|---|
| Guardian hostname | SITE01-GDN01 | TBD |
| Management IP/prefix | 10.250.10.21/24 | Network |
| Default gateway | 10.250.10.1 | Network |
| Management VLAN/VRF | VLAN 2510 / OT-SEC-MGMT | Network |
| DNS | Approved OT DNS | Infrastructure |
| NTP | Redundant OT NTP | Infrastructure |
| CMC FQDN/IP | CMC service address | Security |
| SIEM destination | TLS/syslog/API endpoint | SOC |
| Admin jump hosts | Allowlisted CIDRs | IAM/OT |
| Monitoring interfaces | mon1...monN, no IP | OT security |
| Capture source IDs | MP-S01-001... | OT security |

Examples are not deployable values.

## 3. Interface mapping

Maintain an as-built row for every cable or vNIC:

| Sensor | Nozomi role | Physical/vNIC | Connected device/port | Capture source | Speed/duplex | VLAN tags | Expected Mbps/PPS | Owner |
|---|---|---|---|---|---|---|---|---|
| SITE01-GDN01 | Management | Vendor-labelled MGMT | OTSW-M01 Gi1/0/10 | n/a | Auto/1G | Access 2510 | <20 Mbps | Network |
| SITE01-GDN01 | Monitoring 1 | Vendor-labelled MON1 | Broker OUT-01 | MP-S01-001 | 1G | Tagged copies | 250/45k | SOC |
| SITE01-GDN01 | Monitoring 2 | Vendor-labelled MON2 | SW-L2-A Gi1/0/48 SPAN dst | MP-S01-002 | 1G | Platform-dependent | 80/12k | Controls |

Photograph and label both ends. Never infer port function solely from connector position; use the appliance quick-start/hardware guide for the purchased model.

## 4. Management-plane configuration

1. Connect only the vendor-designated management interface.
2. Configure static IP, prefix, gateway and hostname from the approved IP plan.
3. Configure trusted NTP, timezone and DNS if required.
4. Replace bootstrap/default credentials immediately; create named RBAC accounts.
5. Install trusted HTTPS and inter-component certificates.
6. Configure identity integration and a tested, vaulted break-glass account.
7. Apply the supported internal firewall/management protections and upstream ACLs.
8. Allow only documented flows to CMC/Vantage, SIEM, SMTP, NTP, DNS, PKI, backup and support/update destinations.
9. Enable health, audit and configuration-change logging.
10. Back up/export the approved baseline configuration.

Do not place a default gateway or normal services on monitoring ports.

## 5. Physical Guardian implementation

- Verify rack airflow, environmental ratings, grounding and power feeds.
- Connect redundant power supplies to separate approved circuits when the selected appliance supports them.
- Match copper/fiber/SFP/SFP+ media to the exact specification.
- Use management port only for routed administration.
- Connect TAP/SPAN/broker outputs to designated monitoring ports.
- Install expansion NICs only when supported for the appliance and approved by the BOM.
- Disable or administratively secure unused management-capable services; label unused capture ports.
- Record serial number, asset tag, rack position, warranty/support and software version.

## 6. Virtual Guardian implementation

- Use the vendor-supported hypervisor and virtual hardware specification.
- Separate management port group from monitoring port groups.
- Configure promiscuous/forged-transmit/MAC-change policies exactly as required by the hypervisor design; avoid granting broader permissions than needed.
- Deliver physical traffic to the hypervisor through a dedicated capture NIC/uplink or supported virtual switching design.
- Ensure the monitoring vNIC receives all mirrored frames and VLAN tags without routing.
- Reserve CPU/RAM/storage as required; avoid uncontrolled overcommit and snapshots as a backup strategy.
- Add monitoring vNICs while powered off when required by current Nozomi guidance; verify automatic recognition after boot.
- Prevent vMotion/host migration to a host without identical capture connectivity unless the design explicitly supports it.

## 7. Firewall matrix template

| Source | Destination | Service | Direction | Purpose | Evidence |
|---|---|---|---|---|---|
| Admin jump subnet | Guardian/CMC mgmt IP | HTTPS/approved admin service | Inbound | Administration | Rule ID |
| Guardian | CMC/Vantage | Product-required ports | As documented | Sync/management | Vendor matrix |
| Remote Collector | Guardian | Product-required TLS/control | As documented | Forward capture | Certificate test |
| Guardian/CMC | NTP/DNS/PKI | Approved services | Outbound | Infrastructure | Query/test |
| Guardian/CMC | SIEM/ticketing | TLS syslog/API | Outbound | Events/cases | Test event |

Resolve exact ports from the release-specific Nozomi documentation. Never copy an unverified internet port list into production.

## 8. Capture normalization

For each feed specify: source switch/TAP, source interfaces or VLANs, RX/TX/both, encapsulation, VLAN-tag behavior, packet-broker filters, timestamps, expected utilization and duplicate domain. Where the same conversation appears on multiple feeds, decide whether duplication is acceptable, filtered by the broker, or separated by sensor/site context.

Use BPF filtering only after evidence shows capacity or scope requires it. A filter can silently erase investigative evidence; document expression, owner, justification, test PCAP and expiry/review date.

## 9. Data model and zones

Map discovered nodes to site, Purdue level, IEC 62443 zone, asset owner, process criticality and safety relevance. Decide before go-live whether VLAN or remote-capture provenance is required to disambiguate reused IP addresses. Node-identity behavior should be chosen during clean deployment because later changes can create inconsistent identities.

## 10. Baseline and tuning

- Observe at least one representative process cycle and planned maintenance cycle.
- Suppress only understood, documented benign behavior.
- Preserve high-consequence alerts even when rare.
- Assign rule owner, rationale, scope, expiry and rollback to every tuning change.
- Compare Nozomi inventory with engineering inventory/CMDB; investigate gaps.
- Establish normal engineering-workstation, remote-access, firmware, logic-download and controller-mode-change behavior.
- Review rule/content updates under change control.

## 11. Capacity thresholds

Define site-specific warning and critical thresholds for packet drops, capture utilization, CPU, RAM, disk, sensor health, stale collector state, sync backlog, event queue, storage retention and license/node utilization. Thresholds must align with the selected product/version; do not treat a generic percentage as vendor warranty.

## 12. As-built deliverables

Approved HLD/LLD, BOM, rack elevation, cable schedule, IP plan, firewall matrix, SPAN/TAP configurations, packet-broker policy, screenshots/config exports, capacity baseline, acceptance results, risk register, rollback record, SOPs, support contacts and training evidence.
