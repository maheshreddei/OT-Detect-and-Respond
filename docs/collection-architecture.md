# Collection Architecture

How each source class actually reaches the SIEM. Three collection patterns cover the whole
inventory; the pattern, not the device, determines the onboarding work.

## Pattern A — Host agent (Windows/Linux)

Applies to: Control/SCADA server, jump host, engineering/operator workstations, HMI,
application server, historian (agent mode).

A Splunk Universal Forwarder (or equivalent) on the host ships Windows Event Log / Sysmon
or Linux auditd/syslog. This is the Easy-to-Medium path. The work is inputs configuration
and, for high-noise hosts (workstations), aggressive filtering at the forwarder so you ship
security-relevant events rather than everything. CIM-normalize to Authentication and
Endpoint.

## Pattern B — Syslog (network and appliance)

Applies to: firewall, VPN, switch, router, data gateway, IED (where supported).

The device streams syslog to a collection tier (syslog-ng / Splunk HEC / heavy forwarder)
and a vendor TA parses it. This is the cheapest high-value path (firewall especially).
Filter switches/routers to security events only to keep volume manageable. CIM-normalize to
Network Traffic and Change.

## Pattern C — Passive network monitoring (the OT proxy)

Applies to: PLC, PAC, DCS, RTU, safety controller, and Network Traffic itself — every source
where native logging is Hard or absent.

A passive sensor (Nozomi Guardian, optionally Zeek with ICSNPP OT parsers) on a SPAN/TAP
observes OT protocol traffic and emits alerts via syslog/CEF to the SIEM. This is how you
"collect" a controller that cannot log about itself: you monitor what it says on the wire.
Two things make this pattern high-leverage:

- **It covers a fleet, not a device.** One sensor gives visibility into many controllers,
  which is the only realistic answer to Many/Very-Few instance counts on Hard sources.
- **It carries ATT&CK for ICS natively.** Nozomi alerts include the MITRE ATT&CK for ICS
  technique/tactic fields, so the resulting SIEM events are pre-mapped for detection
  correlation and coverage tracking.

The cost is engineering effort: SPAN/TAP design, sensor placement per Purdue zone, and DPI
tuning. That effort is why the Network Traffic source sits in Tier 3 even though it feeds
the most detections.

## Pattern mapping summary

| Pattern | Sources | Transport | Typical parser | Effort |
|---------|---------|-----------|----------------|--------|
| A Host agent | LS-01, LS-03, LS-08, LS-10, LS-11, LS-14 | Forwarder TCP | UF + OS/Sysmon TA | Low-Med |
| B Syslog | LS-02, LS-04, LS-05, LS-09, LS-12, LS-13 | UDP/TCP 514 | Vendor TA | Low |
| C Passive | LS-06, LS-07, LS-15, LS-16, LS-17, LS-18 | Syslog/CEF from sensor | Nozomi / Zeek ICSNPP | High |
| None | LS-19 | — | — | N/A |

## Where this hands off

Once a source is collecting and CIM-normalized, it becomes a `Primary_Data_Source` value in
the OT Threat Content Repository catalog. The `catalog/detection-linkage.csv` file in this
repo names, per source, which use cases it enables — so onboarding a source is not "done"
until at least one detection consuming it is live. That is the loop: collection here,
detection there, tracked in both.
