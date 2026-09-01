# Asset Discovery and Inventory Governance

## Objective

Create a defensible OT asset inventory from passive Guardian visibility, approved enrichment and—only when authorized—Discovery or Smart Polling. The outcome is an owned, reconciled, confidence-scored inventory, not merely a dashboard count.

## Discovery sources

| Source | Strength | Limitation/risk |
|---|---|---|
| Guardian passive DPI | Continuous protocol-aware visibility | Misses silent/unmonitored assets |
| Asset Intelligence | Product/profile enrichment | License/product/cloud availability varies |
| Smart Polling | Firmware, patch and detailed attributes | Direct contact, credentials, firewall and MOC |
| Discovery | Finds additional devices | Active traffic needs risk approval |
| Arc | Host/local observations | Supported platforms only |
| Engineering inventory/CMDB | Ownership and intended state | Can be stale |
| Network data | Switch port, ARP, DHCP, DNS | Limited process/product context |
| Manual/import | Curated authoritative fields | Human error/conflict risk |

Preserve the source, granularity and confidence Nozomi associates with important asset attributes.

## Passive-first implementation

1. Approve capture points and validate feeds.
2. Observe at least one representative process cycle.
3. Verify both directions, VLAN tags, capture origin and protocol parsing.
4. Define site, zone and naming rules.
5. identify duplicates, reused IPs, NAT and multi-homed equipment.
6. Reconcile with engineering inventory.
7. Classify gaps.
8. Add active methods only for defined fields and approved targets.

## Enterprise asset model

Use a stable ID independent of IP address. Store: enterprise/CMDB ID; Nozomi ID and capture origin; hostname, IP, MAC, VLAN, switch/port and location; vendor/product/model/serial/firmware/components; Purdue level and IEC 62443 zone; system/process and owners; safety/business criticality; function; protocols/services and approved peers; vulnerabilities/controls; source/confidence; first/last seen; lifecycle state.

IP-only identity fails with DHCP, reused ranges, NAT and hardware replacement. Decide whether VLAN/site/capture provenance is required before scale deployment.

## Duplicate workflow

- Same device on multiple feeds: one enterprise asset with several observation paths.
- Same IP at different sites/VLANs: separate identities.
- Redundant controllers: do not merge because product/process match.
- Replacement reusing IP: retire predecessor and link successor.
- NAT/proxy: preserve logical node and underlying asset.
- Ambiguous match: owner review; no automatic merge.

Require evidence from MAC, serial, product identity, switch location, capture provenance and time overlap. Keep merge/split audit and rollback.

## Smart Polling and active Discovery gate

Smart Polling directly contacts assets using protocol-specific strategies. “Non-invasive” does not mean “no operational risk.”

Before use require:

- Asset-owner and vendor approval for exact device/firmware.
- Defined targets; exclude fragile/legacy/SIS assets unless explicitly approved.
- Maintenance window, schedule/rate, stop criteria and rollback.
- Least-privilege vaulted credentials.
- Source sensor and firewall flow.
- Lab/pilot result and process baseline.

Roll out progressively: one noncritical device, a small homogeneous group, then one zone. Review device CPU/logs/alarms, collected-field accuracy, merge effects and retries before expansion.

## Reconciliation workflow

~~~text
Nozomi observations
 -> normalize identity/provenance
 -> compare with engineering inventory
 -> matched | Nozomi-only | CMDB-only | ambiguous
 -> owner-approved disposition
 -> update source of truth and detections
~~~

Dispositions:

- Authorized/matched: refresh confidence and validation date.
- New authorized: create enterprise record and link change ticket.
- Unauthorized/unknown: investigate; do not automatically block.
- CMDB-only: check power, silent state, traffic path, serial/non-IP nature and visibility.
- Field conflict: apply field-level source authority and owner review.
- Retired but active: investigate incomplete decommissioning.
- Wrong zone: validate topology/NAT before escalating.

## New-asset triage

1. Confirm capture origin and identity.
2. Determine first seen, switch port, VLAN and peers.
3. Review protocols, external connections and vulnerabilities.
4. Correlate change/procurement/owner records.
5. Establish process criticality and impact.
6. Resolve physical/virtual/NAT/duplicate status.
7. Assign authorized, unauthorized or unknown.
8. Coordinate physical verification.
9. Update inventory and detection.
10. Record the control failure or blind spot.

## Coverage measures

Report by critical conduit, communicating critical assets, zone/owner completeness, vendor/model confidence, verified firmware, passive versus enriched source, unknown-asset age, duplicate backlog, last-seen freshness, protocol/direction coverage and capture uptime. Never claim “100% coverage” from a node count.

## Lifecycle

Commission with approved baseline; link modifications to MOC; mark temporary vendor behavior with expiry; retire only after traffic, credentials and network rules are removed; alert if a retired identity reappears. Review critical assets quarterly and all assets according to policy.

## Acceptance criteria

- Critical assets have owner, process, zone, criticality and stable ID.
- Reused IP spaces are separated.
- Silent/non-Ethernet and capture blind spots are documented.
- Active discovery has approval and test evidence.
- Reconciliation produces owned dispositions and SLAs.
- Important fields retain source/confidence.
