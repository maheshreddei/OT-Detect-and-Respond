# Nozomi Assertion Queries

N2QL queries that operationalize the [detection catalog](../../source-libraries/protocol-ndr-catalog.csv) inside Nozomi Guardian/CMC. Each is written in the style of Nozomi's *20 Queries* white paper and is designed to be saved as an **assertion** so it raises an alert when the condition is met.

Read [`n2ql-reference.md`](n2ql-reference.md) first, and **replace the `<PLACEHOLDERS>`** with your zone names, master/EWS IPs, and subnets before deploying.

---

## Turning a query into an assertion

Nozomi assertions let a saved query act as a custom detection. Workflow in Guardian:

1. Open **Queries**, paste the query, and **Run** it to confirm it returns what you expect against live data.
2. **Save** the query (give it the ID/name below).
3. Create an **assertion** from it: set the trigger condition (for almost every query here that's **"result is non-empty" / count ≥ 1** — the query is written so that *any* row is a finding), assign a **severity**, and set the evaluation cadence.
4. The assertion then raises a Nozomi alert when it matches, so it flows into your normal alert pipeline (and onward to the SIEM).

Design principle carried over from the protocol guide: **the query encodes the authorization the protocol lacks.** It returns rows only for the disallowed case (write from a non-master, control protocol crossing a zone, remote access into OT), so "non-empty ⇒ alert" is correct by construction. Baseline/reporting queries at the end are *not* assertions — they're for hunting and review.

Severity guidance follows the catalog: writes/commands and disruptive functions → high/critical; recon and cross-zone → medium/high.

---

## 1. Recon & access assertions

### Q-ACC-01 — Remote access (VNC/RDP) into an OT zone
Maps: `VNC-01`, `VNC-04`. Execute on: Guardian/CMC. Severity: high.
```
links | where protocol == vnc OR protocol == rdp
| join nodes to ip | join nodes from ip
| select coalesce(joined_node_from_ip.label,from)->src coalesce(joined_node_to_ip.label,to)->dst
  joined_node_from_ip.zone->from_zone joined_node_to_ip.zone->to_zone protocol last_activity_time
| where to_zone include? "<OT_ZONE>"
| sort last_activity_time desc
```
**Assert:** non-empty ⇒ alert. Any interactive remote-desktop session terminating in an OT zone.

### Q-ACC-02 — FTP into an OT zone (firmware/logic channel)
Maps: `FTP-01`, `FTP-03`. Execute on: Guardian/CMC. Severity: high.
```
links | where protocol == ftp
| join nodes to ip | select from to joined_node_to_ip.label->dst joined_node_to_ip.zone->to_zone last_activity_time
| where to_zone include? "<OT_ZONE>"
| sort last_activity_time desc
```
**Assert:** non-empty ⇒ alert. FTP to a control device is a firmware/project-file path.

### Q-ACC-03 — HTTP(S) to an OT device from outside management
Maps: `HTTP-03`. Execute on: Guardian/CMC. Severity: medium.
```
links | where protocol == http OR protocol == https
| join nodes to ip | select from to joined_node_to_ip.label->dst joined_node_to_ip.zone->to_zone last_activity_time
| where to_zone include? "<OT_ZONE>"
| where from exclude? "<MGMT_SUBNET>"
| sort last_activity_time desc
```
**Assert:** non-empty ⇒ alert. Web-UI access to OT gear from an unexpected source (brute-force/enumeration precursor).

### Q-ACC-04 — Egress from OT to the public internet
Maps: internet-egress (attack-surface model). Execute on: Guardian/CMC. Severity: high.
```
links | join nodes to ip | where joined_node_to_ip.is_public
| join nodes from ip
| select joined_node_from_ip.zone->from_zone from to joined_node_to_ip.label->dst protocol
  tcp_connection_attempts.total last_activity_time
| where from_zone include? "<OT_ZONE>"
| sort last_activity_time desc
```
**Assert:** non-empty ⇒ alert. OT assets should not originate traffic to public IPs.

### Q-ACC-05 — Possible ICMP tunnelling
Maps: `SCAN`/covert-channel (protocol guide, Nozomi Q16). Execute on: Guardian/CMC. Severity: medium.
```
sessions | where protocol == icmp | where status == ACTIVE
| where transferred.bytes > 1000 | where seconds_ago(last_activity_time) < 10
```
**Assert:** non-empty ⇒ alert. Sustained, high-byte ICMP is anomalous in OT and a classic covert channel.

### Q-ACC-06 — Horizontal scan (one source, many peers)
Maps: `SCAN-01`, `SCAN-03`. Execute on: Guardian/CMC. Severity: medium.
```
links | select from to | group_by from | sort count desc | head 25 | column from count
```
**Assert:** alert when any `from` `count` exceeds your fan-out threshold (e.g. > 50 peers). Tune per environment; a scanner talks to far more peers than a normal asset.

### Q-ACC-07 — Blocked/failed TCP handshakes (scan / firewall probing)
Maps: `SCAN-03`, firewall (Nozomi Q14). Execute on: Guardian/CMC. Severity: medium.
```
links | expand transport_protocols
| where tcp_connection_attempts.total >= 1 | where tcp_handshaked_connections.total == 0
| select from to transport_protocol protocol last_activity_time
| sort last_activity_time desc
```
**Assert:** alert on spike / count over threshold. Many half-open attempts from one source = scanning or blocked probing.

---

## 2. Segmentation & cross-zone assertions

### Q-SEG-01 — Traffic crossing more than one Purdue level
Maps: cross-zone pivot (attack-surface model). Execute on: Guardian/CMC. Severity: high.
```
links | where from_zone != $to_zone | where to != 0.0.0.0
| where to exclude? "224.0.0" | where to exclude? "255.255.255.255"
| join nodes from ip | join nodes to ip
| select from to protocol joined_node_from_ip.level->src_level joined_node_to_ip.level->dst_level from_zone to_zone
| select from to protocol dst_level src_level dist(dst_level,src_level) from_zone to_zone
| where dst_level_src_level_dist > 1
| sort dst_level_src_level_dist desc
```
**Assert:** non-empty ⇒ alert (after baselining known-good links). Traffic skipping Purdue levels is a segmentation break / pivot. (Requires Purdue levels assigned to assets.)

### Q-SEG-02 — Control protocol originating from the IT zone
Maps: cross-zone control (`MOD-05`, `S7`, `104`, `DNP3`, `ENIP`). Execute on: Guardian/CMC. Severity: high.
```
links | where protocol == modbus OR protocol == s7 OR protocol == dnp3 OR protocol == iec104 OR protocol == cip
| join nodes from ip
| select from to protocol joined_node_from_ip.zone->from_zone last_activity_time
| where from_zone include? "<IT_ZONE>"
| sort last_activity_time desc
```
**Assert:** non-empty ⇒ alert. Control protocols should never source from IT. (Confirm protocol tokens with `Q-BASE-01`.)

### Q-SEG-03 — New link between two specific zones
Maps: new-pair baseline deviation. Execute on: Guardian/CMC. Severity: medium.
```
links | join nodes to ip | join nodes from ip
| select joined_node_from_ip.zone->from_zone joined_node_to_ip.zone->to_zone from to protocol
  tcp_connection_attempts.total tcp_handshaked_connections.total last_activity_time
| sort last_activity_time desc
| where from_zone include? "<IT_ZONE>" | where to_zone include? "<OT_ZONE>"
```
**Assert:** non-empty ⇒ alert (or assert-on-change against a saved baseline of allowed IT↔OT links).

---

## 3. Protocol write / command assertions (core)

> These are the highest-value assertions — a control write/command from a non-authorized source. The Modbus set is fully worked (function codes are well defined). For the others, confirm the exact function/service codes with `Q-BASE-02` first, then fill them into the same pattern; a protocol-presence + native-alert fallback is given for each.

### Q-WR-MOD-01 — Modbus write from a non-master source
Maps: `MOD-01`, `MOD-02`. Execute on: Guardian/CMC. Severity: high (critical if to a safety asset).
```
links | where protocol == modbus | expand function_codes
| where expanded_function_codes.name == 5 OR expanded_function_codes.name == 6
     OR expanded_function_codes.name == 15 OR expanded_function_codes.name == 16
| join nodes from ip
| select from to joined_node_from_ip.zone->from_zone expanded_function_codes.name->fc last_activity_time
| where from exclude? "<MODBUS_MASTER_IP>"
| sort last_activity_time desc
```
**Assert:** non-empty ⇒ alert. Write function codes (5/6/15/16) from anything other than the authorized master.

### Q-WR-MOD-02 — Modbus diagnostic / disruptive function (FC 8)
Maps: `MOD-04`. Execute on: Guardian/CMC. Severity: high.
```
links | where protocol == modbus | expand function_codes
| where expanded_function_codes.name == 8
| select from to expanded_function_codes.name->fc last_activity_time | sort last_activity_time desc
```
**Assert:** non-empty ⇒ alert. FC 8 sub-functions can restart comms / force listen-only.

### Q-WR-MOD-03 — Modbus device-ID reconnaissance (FC 43)
Maps: `MOD-03`. Execute on: Guardian/CMC. Severity: medium.
```
links | where protocol == modbus | expand function_codes
| where expanded_function_codes.name == 43
| select from to last_activity_time | sort last_activity_time desc
```
**Assert:** non-empty ⇒ alert. Device-identification reads from an unexpected source are fingerprinting.

### Q-WR-S7-01 — S7comm program-transfer / stop (native signature)
Maps: `S7-01`, `S7-02`. Execute on: Guardian/CMC. Severity: critical.
```
alerts | where type_id include? "PROGRAM" OR type_id include? "PLC"
| select type_id ip_src ip_dst created_time | sort created_time desc
```
Plus, once the S7 control function codes are confirmed in your environment:
```
links | where protocol == s7 | expand function_codes
| select from to expanded_function_codes.name->s7_function last_activity_time
| where from exclude? "<ENG_ZONE>"
| sort last_activity_time desc
```
**Assert:** non-empty ⇒ alert. CPU STOP / program download is the crown-jewel Siemens event. (Guardian ships native program-transfer signatures — the first query rides those; the second catches S7 functions from non-engineering sources.)

### Q-WR-DNP3-01 — DNP3 operate from a non-master
Maps: `DNP3-01`, `DNP3-02`. Execute on: Guardian/CMC. Severity: critical.
```
links | where protocol == dnp3 | expand function_codes
| where expanded_function_codes.name == 3 OR expanded_function_codes.name == 4 OR expanded_function_codes.name == 5
| join nodes from ip
| select from to joined_node_from_ip.zone->from_zone expanded_function_codes.name->fc last_activity_time
| where from exclude? "<MASTER_IP>"
| sort last_activity_time desc
```
**Assert:** non-empty ⇒ alert. Select/Operate/Direct-Operate (FC 3/4/5) from anything but the master. *Confirm FC numbers via `Q-BASE-02`.*

### Q-WR-104-01 — IEC-104 command ASDU from a non-master
Maps: `104-01`, `104-02`. Execute on: Guardian/CMC. Severity: critical.
```
links | where protocol == iec104 | expand function_codes
| join nodes from ip
| select from to joined_node_from_ip.zone->from_zone expanded_function_codes.name->asdu last_activity_time
| where from exclude? "<MASTER_IP>"
| sort last_activity_time desc
```
**Assert:** alert when `asdu` is a command type (C_SC 45 / C_DC 46 / C_RC 47 / C_SE 48–50) from a non-master — add `| where expanded_function_codes.name == 45 OR ... == 46 ...` once ASDU-type exposure is confirmed. Operating a breaker/setpoint from the wrong source.

### Q-WR-ENIP-01 — EtherNet/IP CIP write from a non-controller
Maps: `ENIP-01`, `ENIP-04`. Execute on: Guardian/CMC. Severity: high.
```
links | where protocol == cip OR protocol == ethernetip | expand function_codes
| join nodes from ip
| select from to joined_node_from_ip.zone->from_zone expanded_function_codes.name->cip_service last_activity_time
| where from exclude? "<MASTER_IP>"
| sort last_activity_time desc
```
**Assert:** alert when `cip_service` is a Set_Attribute / tag-write service from a non-controller. Constrain to the write service codes once confirmed.

### Q-WR-BAC-01 — BACnet WriteProperty from an unexpected source
Maps: `BAC-01`, `BAC-03`. Execute on: Guardian/CMC. Severity: high.
```
links | where protocol == bacnet | expand function_codes
| join nodes from ip
| select from to joined_node_from_ip.zone->from_zone expanded_function_codes.name->bacnet_service last_activity_time
| sort last_activity_time desc
```
**Assert:** alert when `bacnet_service` is WriteProperty/WritePropertyMultiple (or DeviceCommunicationControl / ReinitializeDevice for the disruptive variants) from a non-controller.

### Q-WR-OPCUA-01 — OPC UA activity into an OT zone
Maps: `OPC-02`, `OPC-04`. Execute on: Guardian/CMC. Severity: medium (high if writes decode).
```
links | where protocol == opcua
| join nodes to ip | join nodes from ip
| select from to joined_node_from_ip.zone->from_zone joined_node_to_ip.zone->to_zone last_activity_time
| where to_zone include? "<OT_ZONE>" | where from exclude? "<MASTER_IP>"
| sort last_activity_time desc
```
**Assert:** non-empty ⇒ alert. Note: SignAndEncrypt OPC UA hides service detail from DPI — pair with OPC UA **server audit logs** (see log-sources) for Write/anonymous-session detection.

### Q-WR-MQTT-01 — MQTT client into the broker from an unexpected source
Maps: `MQTT-01`, `MQTT-03`. Execute on: Guardian/CMC. Severity: high.
```
links | where protocol == mqtt
| join nodes to ip | select from to joined_node_to_ip.label->broker last_activity_time
| where to include? "<BROKER_IP>" | where from exclude? "<MASTER_IP>"
| sort last_activity_time desc
```
**Assert:** non-empty ⇒ alert. Network view can't see the topic (esp. over TLS) — pair with **broker logs** to catch publish-to-command-topic; this catches the unexpected client reaching the broker.

---

## 4. Baseline & hygiene (run first / periodically — not assertions)

### Q-BASE-01 — Most-used protocols (confirm your protocol tokens)
Execute on: Guardian/CMC.
```
links | group_by protocol sum transferred.bytes | sort sum desc
| select protocol sum->transferred_bytes | head 15 | column protocol transferred_bytes
```
Run this **before deploying section 3** — it shows the exact protocol tokens Nozomi uses in your environment.

### Q-BASE-02 — Is this protocol/function in use? (confirm function codes)
Execute on: Guardian/CMC.
```
links | where protocol == modbus | expand function_codes
| select from to expanded_function_codes.name->fc last_activity_time transferred.bytes
| sort last_activity_time desc
```
Swap `modbus` for any protocol to enumerate which function/service codes actually appear — use this to fill the `== N` values in the write assertions.

### Q-BASE-03 — New nodes in the last 7 days
Maps: `new-asset`. Execute on: Guardian/CMC.
```
nodes | where seconds_ago(first_activity_time) < 604800
| select ip label type zone first_activity_time | sort first_activity_time desc
```
**Optional assert:** alert when a new node appears **in an OT zone** (`| where zone include? "<OT_ZONE>"`).

### Q-BASE-04 — Multihomed assets (bridging risk)
Maps: `multihomed`. Execute on: Guardian/CMC.
```
assets | where size(nodes) > 1 | join nodes ip ip
| select name nodes joined_node_ip_ip.created_at
| sort joined_node_ip_ip_created_at asc | uniq
```
A device on two networks can bridge zones — review changes over time; assert-on-change.

### Q-BASE-05 — Assets per subnet (inventory hygiene)
Execute on: Guardian/CMC.
```
nodes | where is_public != true | where is_broadcast != true | where ipv4(ip) != ""
| select ip id split(ip,.,0)->o1 split(ip,.,1)->o2 split(ip,.,2)->o3
| select concat(o1,".",o2,".",o3,".0/24")->subnet | group_by subnet | sort count desc
```

---

## 5. Reporting & IR support (not assertions)

### Q-RPT-01 — Top 10 alerts (regular reporting)
Execute on: Guardian/CMC/Vantage.
```
alerts | group_by type_id | sort count desc | head | pie type_id count
```

### Q-RPT-02 — Greatest MITRE ATT&CK exposure
Maps: ATT&CK coverage. Execute on: Guardian/CMC.
```
alerts | where is_empty(mitre_attack_tactics) == false
| group_by concat(mitre_attack_tactics,"-",mitre_attack_techniques)->tech
| sort tech asc | column_colored_by_label tech count
```

### Q-RPT-03 — Alerts within a time window (threat hunt / IR)
Execute on: Guardian/CMC/Vantage. Set the epoch-ms window.
```
alerts | select type_id->alert_type id->alert_id created_time->time ip_src->source ip_dst->destination
| sort created_time
| where created_time >= <START_EPOCH_MS> | where created_time <= <END_EPOCH_MS>
```

### Q-RPT-04 — Native unauthorized-write / anomaly signatures
Execute on: Guardian/CMC. Complements section 3 by riding Guardian's built-in signatures.
```
alerts | where type_id include? "PROGRAM" OR type_id include? "ANOMAL" OR type_id include? "PACKET-RULE"
| select type_id ip_src ip_dst created_time | sort created_time desc
```

---

## Coverage summary

| Protocol / area | Assertion queries | Confidence |
|-----------------|-------------------|-----------|
| Modbus | Q-WR-MOD-01/02/03 | high (function codes defined) |
| S7comm | Q-WR-S7-01 (+native) | high via native signature |
| DNP3 | Q-WR-DNP3-01 | pattern set; confirm FCs |
| IEC-104 | Q-WR-104-01 | pattern set; confirm ASDU types |
| EtherNet/IP | Q-WR-ENIP-01 | pattern set; confirm services |
| BACnet | Q-WR-BAC-01 | pattern set; confirm services |
| OPC UA | Q-WR-OPCUA-01 | network + note on server logs |
| MQTT | Q-WR-MQTT-01 | network + note on broker logs |
| Access (VNC/RDP/FTP/HTTP) | Q-ACC-01..03 | high |
| Segmentation | Q-SEG-01..03 | high |
| Recon/scan | Q-ACC-05/06/07 | high |

Machine-readable list of all queries: [`queries-catalog.csv`](queries-catalog.csv).
