# A — BPCS↔SIS Boundary Integrity

**Principle defended: independence.** The SIS publishes status up to the BPCS but the BPCS must not write the SIS's logic, trip points, or outputs (functional-safety primer §1). Every detection here catches a violation of the read-up / no-safety-writes rule. Any hit is minimum SEV-1.

## Detections

| ID | Detection | Logic | Data source | ATT&CK | Severity |
|----|-----------|-------|-------------|--------|----------|
| SIS-A1 | Control-to-safety write/command | A BPCS-zone source issues a write/command (function code) to an SIS asset | NDR (safety net) | T0855 / T0836 | critical |
| SIS-A2 | New comms path into the SIS zone | A source↔SIS link (any protocol) not in the sanctioned baseline | NDR + baseline | T0855 | high |
| SIS-A3 | Reversed data direction at the boundary | Traffic the SIS should only *publish* is instead being *written into* it | interface gateway / NDR | T0855 | high |
| SIS-A4 | New / unauthorized asset on the safety network | A node appears in the SIS zone | NDR asset inventory | T0846 | high |
| SIS-A5 | SIS traffic bypassing the sanctioned gateway | Cross-boundary SIS traffic not traversing the approved conduit | NDR / firewall | T0855 | high |

## Worked queries

### SIS-A1 — Control-to-safety write (the "can the DCS write the safety PLC?" detection)
Nozomi N2QL — control-zone source issuing function codes into the SIS zone:
```
links | where protocol == modbus OR protocol == s7 OR protocol == cip OR protocol == tristation
| expand function_codes
| join nodes to ip | join nodes from ip
| select from to joined_node_from_ip.zone->from_zone joined_node_to_ip.zone->to_zone
  expanded_function_codes.name->fc protocol last_activity_time
| where to_zone include? "<SIS_ZONE>"
| where from_zone include? "<BPCS_ZONE>"
| sort last_activity_time desc
```
**Assert:** non-empty ⇒ **critical**. The answer to "can a DCS/SCADA write directly to a Safety PLC" is *no* — so any such write is a boundary violation by definition. Constrain to write function codes once confirmed (see the OT protocol library for per-protocol write codes).

### SIS-A4 — New asset on the safety network
Nozomi N2QL:
```
nodes | where zone include? "<SIS_ZONE>" | where seconds_ago(first_activity_time) < 86400
| select ip label type first_activity_time | sort first_activity_time desc
```
**Assert:** non-empty ⇒ alert. The safety network's asset set is small and static; anything new is suspect.

### SIS-A2 — New comms path into the SIS zone
Nozomi N2QL (against a saved allow-list of approved SIS links):
```
links | join nodes to ip | join nodes from ip
| select from to joined_node_from_ip.zone->from_zone joined_node_to_ip.zone->to_zone protocol last_activity_time
| where to_zone include? "<SIS_ZONE>"
| sort last_activity_time desc
```
**Assert:** alert on any pair not in the approved SIS-communications baseline (only the sanctioned gateway/EWS should appear).

## Notes
- The only legitimate BPCS→SIS interactions are non-safety, access-controlled requests (e.g. a reset) the SIS logic chooses to honor — everything else into the SIS zone is a finding.
- Pair SIS-A1 with the historian to confirm whether the write changed a safety value (category C).
