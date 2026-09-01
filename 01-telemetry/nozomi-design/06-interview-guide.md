# Nozomi Architecture and Operations Interview Guide

Use this to explain work you genuinely understand. Do not claim a deployment, outage, metric or product feature you did not perform or verify.

## 1. Strong architecture answer

“I start with the process and zone/conduit model, not the appliance. I identify critical communications and choke points—IDMZ, Level 3 core, Level 2/1 cell boundaries, safety and vendor-access conduits. I measure peak Mbps and packets per second, include redundant paths and growth, then decide between TAP, packet broker, local SPAN or a Remote Collector. Guardian monitoring ports receive passive copies with no production addressing; the management port sits on a restricted OT security-management network. Multiple Guardians roll up to CMC or the approved central service. I validate both directions, VLAN context, protocols, critical assets, packet loss and end-to-end alert delivery.”

## 2. SPAN versus TAP answer

“SPAN is fast and cost-effective, but it depends on switch resources and can drop copied packets under congestion. It may alter VLAN/error visibility depending on platform. A passive TAP gives a more deterministic copy and is preferred for critical or evidentiary links, but insertion affects production cabling and needs an outage/change plan. A packet broker helps aggregate, filter, replicate and deduplicate many feeds. I select based on criticality, traffic profile, redundancy, packet fidelity and operational risk.”

## 3. Change-request answer

“Yes, in production I normally raise an MOC/change even though Nozomi monitoring is passive. The risk is in changing switch configuration, inserting a TAP, moving cables, adding firewall flows, hypervisor settings, rack power and rollback—not in Nozomi transmitting control commands. The change includes prechecks, peer-reviewed intent, process-owner approval, monitoring window, rollback triggers, exact rollback and before/after evidence.”

## 4. Port explanation

“The management port is an IP-addressed control plane for UI, API, NTP, identity, updates, integrations and central synchronization. Monitoring ports ingest mirrored or TAP traffic and should not be routable production endpoints. Expansion slots add supported NIC capacity on particular models, but they do not automatically increase licensed throughput or act as HA/inline ports. I verify exact labels and capabilities against the purchased model and release.”

## 5. Investigation workflow

1. Establish alert time, site, asset, zone, process state and safety impact.
2. Review alert logic, confidence, risk and asset criticality.
3. Pivot through source/destination nodes, sessions, protocol functions and timeline.
4. Compare behavior with baseline, maintenance window and approved engineering activity.
5. Check adjacent telemetry: firewall, VPN, jump host, Windows, historian, switch and identity logs.
6. Determine first-seen, last-seen, scope, affected peers and whether behavior crossed a conduit.
7. Preserve evidence/export and document timestamps and capture origin.
8. Engage the control-system owner before containment; prioritize safe process operation.
9. Hunt for the same indicators/behavior across sites and historical data.
10. Close with root cause, detection improvement, coverage gap and lessons learned.

## 6. Hunting examples

- New engineering workstation or unauthorized laptop in a control zone.
- First-seen controller, HMI, PLC firmware or vendor.
- New protocol or administrative protocol crossing an IEC 62443 conduit.
- PLC programming, logic download/upload, mode change, stop/start or firmware activity outside a window.
- Write commands where only reads are expected.
- New remote-access source, unusual session duration or access outside schedule.
- Level 3 host communicating directly with Level 1, bypassing expected jump/proxy path.
- Scanning/enumeration, failed connections or one-to-many connection fan-out.
- SMB/RDP/SSH/PowerShell/Windows administrative behavior entering OT.
- New external DNS/internet destination from an OT asset.
- Beacon-like periodic connections, unusual bytes/packets ratio or data exfiltration pattern.
- Asset disappearance, zero capture rate or loss of a redundant path.

For each hunt define hypothesis, scope, time range, required telemetry, expected normal behavior, query/filter, findings, false-positive checks and disposition.

## 7. Troubleshooting scenarios

**Assets missing:** verify the device is active; trace its traffic path; check SPAN sources/directions, VLAN tags, TAP A/B links, broker filters, interface counters, BPF filters and sensor capacity.

**Only one traffic direction:** inspect source direction keywords, asymmetric routing, redundant paths, TAP breakout cabling and broker aggregation.

**Duplicate assets/sessions:** determine whether the same packets arrive from multiple points or whether overlapping IP spaces require VLAN/site/capture provenance.

**Sensor shows high load:** correlate PPS, small packets, duplicates, noisy broadcast/multicast, Remote Collector inputs, event burst, retention and resource metrics; redesign aggregation before blindly filtering.

**Collector stale:** verify management/WAN reachability, time, certificates, assigned Guardian, bandwidth, version compatibility and last payload timestamp.

**SIEM lacks alerts:** test Nozomi generation, export configuration, firewall/TLS, parser, queue/rate limiting, timestamp and field mapping.

## 8. Experience signals interviewers value

- You distinguish network availability from monitoring availability.
- You talk about PPS, bursts and duplicates—not only Mbps.
- You know passive monitoring still needs MOC.
- You can explain missing visibility and false confidence.
- You separate management and capture planes.
- You involve process/safety owners before response actions.
- You validate end-to-end outcomes and keep as-built evidence.
- You state model/version dependencies instead of inventing port numbers.
- You connect alerts to asset criticality and process consequence.
- You turn incident findings into new monitoring points, rules and procedures.

## 9. Questions to ask the interviewer

- How many sites, nodes, protocols and reused address spaces exist?
- Is central management CMC, Vantage, or a hybrid model?
- Which links use TAPs, brokers, SPAN, RSPAN or ERSPAN?
- How is packet loss measured and who owns capture health?
- How are Nozomi assets reconciled with engineering inventory?
- What is the process for tuning, MOC and rule/content upgrades?
- How does the SOC engage control-room and safety personnel?
- Which investigation exports and retention periods are available?
- What are the current blind spots and highest-consequence conduits?
- What evidence defines successful monitoring coverage?

## 10. Honest wording

Prefer: “I designed,” “I configured,” “I validated,” “I supported,” or “I understand the procedure,” matching your real role. A credible experienced practitioner explains assumptions, risk, verification and lessons—not just product screens.
