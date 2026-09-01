# SPAN, TAP and Change-Control Implementation

## 1. Is a change request required?

**Normally yes.** A production change/MOC is required when configuring a switch mirror, changing a firewall, installing a TAP, moving cables, adding optics, changing a hypervisor virtual switch, mounting/powering an appliance, or enabling new routed communication. Passive monitoring does not mean the installation activity is risk-free.

A documentation-only update or work in an isolated lab may follow a lower change class, but the asset owner and local policy decide. Emergency change is not justified merely because visibility is missing.

## 2. Selection decision

| Factor | Local SPAN | RSPAN/ERSPAN | Passive TAP | Packet broker |
|---|---|---|---|---|
| Cost/lead time | Low | Low-medium | Medium | High |
| Switch dependency | Yes | Yes plus network path | No for capture copy | Broker dependency |
| Loss under congestion | Possible | Possible | Lowest when correctly sized | Depends on broker/output |
| Full duplex visibility | Aggregated | Aggregated/encapsulated | Separate A/B outputs commonly | Can aggregate |
| Timestamp/evidence quality | Platform-dependent | Platform/path-dependent | Stronger foundation | Strong if supported |
| Remote transport | No | Yes | Needs transport/broker | Yes |
| Filtering/deduplication | Limited | Limited | None | Strong |
| Production cabling impact | None | None | Yes, planned outage/risk | Usually at aggregation layer |

Use TAP/broker for critical or high-rate links, loss-sensitive investigations, and redundant architectures. Use SPAN when expected aggregate traffic is comfortably below destination capacity and the switch's mirroring behavior is validated.

## 3. Monitoring-point engineering

For every candidate link calculate:

- Sum of mirrored ingress and egress peak traffic.
- Packets per second and burst behavior, not only average Mbps.
- Destination-port speed and sensor capacity.
- Whether broadcast/multicast appears on multiple sources.
- Whether VLAN tags, errors, pause frames or physical-layer faults are preserved.
- Whether hardware/software SPAN resources are already used.
- Effect of switch reboot, stack failover, supervisor switchover and topology changes.
- Duplicate traffic created by monitoring both trunk and access links.
- Visibility during active/standby failover.

Target utilization needs platform-specific engineering margin. If aggregate source bursts can exceed the SPAN destination, redesign rather than assuming the switch will queue every copied packet.

## 4. Generic local SPAN pattern

Vendor syntax differs. The approved network engineer must translate this intent:

~~~text
monitor-session <ID>
  source interface <uplink-A> both
  source interface <uplink-B> both        # only if duplication/capacity assessed
  or source vlan <approved-vlan-list>
  destination interface <dedicated-port>
  preserve vlan tags: <validated setting>
  truncate: disabled unless explicitly required
~~~

Rules:

- Destination port is dedicated to monitoring; never connect a user/production endpoint.
- Do not configure the Guardian management IP on this link.
- Mirror both directions unless the use case intentionally needs one.
- Prefer trunk/choke-point sources over dozens of access ports.
- Exclude irrelevant backup/video traffic only through an approved, evidenced filter.
- Validate whether the platform permits a destination port in a VLAN or to transmit.
- Record any platform limits on sessions, sources and destination ports.
- Test that the session survives the intended switch/stack failover.

## 5. RSPAN/ERSPAN considerations

RSPAN consumes a dedicated transport VLAN across the path and can expose mirrored traffic beyond its original zone. ERSPAN encapsulates packets over IP and adds MTU, routing, bandwidth, latency and security considerations. Treat either as a production data flow requiring architecture and firewall review.

Check encapsulation compatibility with the receiving appliance or packet broker, VLAN/MTU behavior, packet ordering, fragmentation, QoS, route symmetry and encryption requirements. Do not route unencrypted mirrored OT payload across untrusted networks.

## 6. TAP implementation

- Match media, speed, optics, bypass behavior and link-loss characteristics.
- Determine copper versus fiber TAP and whether regeneration/aggregation is needed.
- For full-duplex breakout, connect both monitor outputs or aggregate through a broker.
- Confirm optical power budget and polarity for fiber.
- Install during an approved outage unless the architecture provides a tested hitless method.
- Label network A/B and monitor A/B; never reverse production and monitor ports.
- Verify the TAP cannot inject traffic from the monitor port.
- Test link negotiation, redundancy and process health after insertion.
- Retain before/after optical levels, interface counters and packet evidence.

## 7. Packet-broker policy

Document every input and output mapping, filters, replication, aggregation, deduplication, slicing, tunnel termination and timestamp function. Avoid over-filtering industrial protocols. Monitor broker output drops and license limits. Keep an export of the approved policy and apply RBAC/MFA to broker administration.

## 8. Change record template

**Purpose:** Enable passive Nozomi visibility for capture point MP-___.

**Assets affected:** switches, firewalls, links, controllers indirectly dependent on link, Guardian/broker, rack/power.

**Risk:** switch CPU/resource impact; oversubscribed mirror; cabling error; link interruption; loss of redundancy; unintended VLAN exposure; duplicate traffic; missing direction/tags.

**Prechecks:**

- Latest backups and exact device identifiers confirmed.
- Process owner and control-room approval obtained.
- Existing SPAN resources and port utilization checked.
- Destination cable traced and disconnected from production addressing.
- Out-of-band access and rollback engineer available.
- Safety/operations hold points agreed.
- Baseline interface errors, CPU, redundancy and process status recorded.

**Implementation:**

1. Confirm change window and communications.
2. Validate sensor management health.
3. Patch dedicated destination to the correct monitoring port.
4. Apply peer-reviewed mirror/TAP/broker configuration.
5. Check network/device/process health.
6. Validate packets, directions, VLANs and expected protocols in Nozomi.
7. Observe counters and drops through representative load.
8. Save configuration and evidence.

**Rollback triggers:** process alarm, link flap, error increase, CPU/resource threshold breach, STP/redundancy change, packet storm, unexpected forwarding, or failed acceptance.

**Rollback:** remove/disable mirror session; restore previous configuration; remove TAP only under safe approved procedure; restore cabling; verify process/network health; notify stakeholders.

## 9. Evidence to attach

Approved config diff, peer review, topology, port/cable IDs, pre/post counters, process-owner confirmation, Nozomi packet/asset screenshots, packet-rate/throughput sample, loss test, SIEM test event, rollback result if invoked and updated as-built drawing.
