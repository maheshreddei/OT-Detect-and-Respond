# Nozomi Investigation and Threat-Hunting Playbooks

## Principles

Safety and process stability come first. Nozomi observations are evidence, not automatic proof. Preserve timestamps, capture origin, query/filter and exports. Correlate with process state and MOC. Never block, scan, reboot, isolate or modify a control asset without authorized operations approval.

## Case record

Record case/alert ID; first/last seen; Guardian/site/interface/capture point; source/destination assets, zones, protocol and function; criticality/owner/process state; severity/confidence; maintenance correlation; timeline and external evidence; hypotheses and competing explanations; scope/impact; decisions/approvers/actions; hashes and evidence location; recovery and lessons.

## Core workflow

### Validate

1. Confirm sensor/feed health.
2. Read the exact alert observable.
3. Validate asset identity and reused-IP/duplicate risk.
4. Verify time and capture origin.
5. Determine recurrence and current activity.
6. Correlate approved change/maintenance.

### Contextualize

Identify process, Purdue/IEC 62443 zone and owner. Review normal peers/protocols, industrial operation/direction/frequency and baseline. Pivot through assets, sessions, links, alerts, vulnerabilities, network view and Time Machine where applicable. Correlate firewall, VPN, jump host, EDR, Windows, identity, historian and switch evidence.

### Scope

Find earliest activity, persistence, all targets, other sources with the behavior, other sites/IOCs, new links, conduit crossings, safety/redundant-system involvement and blind spots.

### Decide/respond

Classify as malicious, unauthorized, approved benign, unapproved benign, false positive, insufficient evidence or monitoring defect. Present process consequences and options to the authorized OT decision-maker. Preserve evidence before changes.

### Close

Document root cause, impact, recovery, tuning/detection change, inventory correction, capture improvement and owners/dates.

## Playbook A — New/unauthorized asset

Validate capture origin, MAC/IP/VLAN, first seen and duplicate/NAT possibility. Pivot to switch port, peers, protocols, DNS/DHCP, external links, profile and change records. Determine installer, function and conduit access. Physically verify with operations; do not disconnect when impact is unknown. Hunt for same OUI, hostname, first-seen window and behavior across sites.

## Playbook B — PLC/SIS logic or mode change

Validate exact protocol operation, engineering source, controller target, direction and repeats. Check work order, control-room log, vendor session, redundancy and process state. Correlate VPN/jump-host/account, EDR process, project/file version and controller audit. Scope other controllers and earlier discovery. Immediately escalate unauthorized critical/safety action; operations owns containment. Hunt for programming operations outside windows and mode changes followed by loss.

## Playbook C — Remote/vendor access

Validate VPN identity, account, MFA, ticket/window and approved targets. Trace VPN to jump host to target; inspect RDP/SSH/SMB/engineering traffic, file movement, fan-out and internet access. Hunt outside schedule, shared accounts, direct Level 3-to-Level 1 access and new sources. End sessions or revoke credentials only after authorized process review.

## Playbook D — Scanning/lateral movement

Distinguish authorized vulnerability/engineering discovery from hostile scanning. Analyze target/port count, timing, failures followed by success and later admin/control sessions. Scope zone boundaries and credentials. Hunt fan-out deviations, SMB/RDP/SSH after enumeration and repeated low-and-slow patterns.

## Playbook E — IOC or command-and-control

Validate indicator, confidence, age, source/destination and enforcement status. An IP reputation hit alone is not compromise. Pivot through DNS, TLS metadata if visible, periodicity, bytes, peer assets, file transfer, EDR and firewall/proxy. Hunt related indicators, identical beacon intervals and new external destinations. OT incident command selects safe boundary blocks/isolation/rotation.

## Playbook F — Asset/communication loss

Validate sensor/capture health before declaring process outage. Inspect interface counters, SPAN, TAP/broker, switch, redundancy, process alarms and maintenance. Classify monitoring, network or asset failure, planned shutdown or identity change. Hunt common switch/feed/power dependencies.

## Hypothesis-led hunting

1. State testable hypothesis and consequence.
2. Define time, sites, zones, assets and protocols.
3. Prove telemetry health for that period.
4. Describe normal behavior and exceptions.
5. Preserve broad query/filter and results.
6. Reduce by criticality, novelty, direction, function and frequency.
7. Build timeline and peer group.
8. Correlate external evidence.
9. Assign disposition/confidence.
10. Convert findings to detection, coverage or inventory improvement.

## Repeatable hunts

| Hunt | Logic | False-positive check |
|---|---|---|
| New engineering source | First-seen source uses engineering protocol | Approved workstation/MOC |
| Unauthorized write | Control/write from non-approved source | Automation/maintenance |
| Conduit bypass | Direct session omits jump/proxy | Approved failover route |
| Rare admin service | SMB/RDP/SSH/WinRM new to zone | Patch/backup/vendor |
| Internet from OT | New external destination | Licensing/NTP/update |
| Beaconing | Regular low-volume persistence | Legitimate heartbeat |
| Fan-out | Unusual targets/ports | Approved discovery |
| Retired asset returns | Activity after retirement | Reused identity |
| Firmware outlier | Same model, different firmware | Staged upgrade/profile error |
| Blind spot | Expected control conversation absent | Idle process/asymmetry |

Use product-supported filters/queries for the installed release; do not invent syntax.

## Evidence handling

Record timezone/clock offset, product version, query and capture limits. Hash PCAP/exports when required. Store in an access-controlled case repository. Distinguish Nozomi metadata, selected traces and external full packet capture. State packet-loss and retention limitations and follow chain-of-custody policy.

## Metrics

Measure detection-to-triage/owner time, cases with process context, dispositions, hunts producing improvements, evidence lost to retention/coverage, repeated uncorrected causes, monitoring-defect closure time and playbook exercises.

## Interview summary

“I validate telemetry before assuming compromise. I establish identity, capture origin, time, zone and process consequence; pivot through assets, sessions, functions and timeline; correlate change, VPN, endpoint and firewall evidence; scope the behavior across sites; and give operations safe response options. Closure produces a better detection, inventory record, monitoring point or procedure.”
