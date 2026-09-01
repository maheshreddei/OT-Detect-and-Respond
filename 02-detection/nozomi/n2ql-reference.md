# N2QL Reference (for these assertions)

A short reference for the Nozomi Network Query Language (N2QL) idioms used in [`assertion-queries.md`](assertion-queries.md), distilled from Nozomi's *20 Queries* white paper and the Nozomi Academy query material. Enough to read, modify, and maintain every query here.

## Data sources (start of a query)
| Source | Holds | Used for |
|--------|-------|----------|
| `links` | node-to-node communication links (protocol, bytes, TCP stats, function codes) | most protocol/traffic detections |
| `sessions` | live/active sessions | active-flow checks (e.g. ICMP tunnelling) |
| `alerts` | Guardian alerts (type_id, MITRE, src/dst, time) | native-signature and reporting queries |
| `nodes` | discovered nodes (ip, label, zone, level, first/last activity) | asset/appliance context, new-node |
| `assets` | assets (may map to multiple nodes) | multihomed, asset inventory |
| `node_cves` | per-node vulnerabilities | vuln queries (out of scope here) |
| `appliances` | Nozomi sensors themselves | licensing/health |

## Core pipes
```
| where <condition>              filter rows
| select a b c->alias            keep/rename fields (-> renames)
| group_by <field> [sum <f>]     aggregate (count is implicit)
| sort <field> desc|asc          order
| head [N]                       top N
| join nodes to ip               enrich 'to' side with node data -> joined_node_to_ip.*
| join nodes from ip             enrich 'from' side -> joined_node_from_ip.*
| join nodes ip ip               join assets/nodes on ip
| expand <field>                 explode a list field into rows (e.g. function_codes)
| coalesce(a,b)->alias           first non-null
| concat(a,"-",b)->alias         string join
| split(ip,.,N)->part            split by delimiter, take index N
| uniq                           dedupe
| pie / column / column_colored_by_label / history count / bucket   visualizations
```

## Condition operators
```
==  !=  >  >=  <            comparisons (numbers, tokens)
include?  "text"           substring / membership match (zones, labels, type_id)
exclude?  "text"           negated membership
is_public / is_to_public / is_broadcast     boolean node/link flags
is_empty(<field>)          emptiness test
size(<field>)              collection size (e.g. size(nodes) > 1)
days_ago(<time>)  seconds_ago(<time>)        relative time
ipv4(ip)                   ipv4 predicate/extractor
dist(a,b)                  numeric distance (used for Purdue level gap)
```

## Field idioms seen in the wild
- Sub-fields with dots: `transferred.bytes`, `tcp_connection_attempts.total`, `tcp_handshaked_connections.total`.
- Function codes: `expand function_codes | where expanded_function_codes.name == <N>` — **the key idiom for protocol write/command detection**. `<N>` is the protocol's function/service code.
- Zones/levels via join: `joined_node_to_ip.zone->to_zone`, `joined_node_to_ip.level->dst_level`.
- Alert fields: `type_id`, `mitre_attack_tactics`, `mitre_attack_techniques`, `ip_src`, `ip_dst`, `created_time`.
- Node fields: `first_activity_time`, `last_activity_time`, `label`, `zone`, `level`, `is_public`.

## Two things to confirm in *your* environment before deploying
1. **Protocol tokens.** The literal used in `where protocol == <token>` (e.g. `modbus`, `s7`, `dnp3`, `iec104`, `cip`, `bacnet`, `opcua`, `mqtt`, `vnc`, `rdp`, `ftp`, `http`, `icmp`) depends on how Nozomi labels the protocol in your deployment. **Run `Q-BASE-01` (most-used protocols) first** to see the exact tokens present, then substitute.
2. **Function/service code numbers.** `expanded_function_codes.name == N` uses the protocol's numeric code. Modbus is well-defined (see below); for S7/DNP3/IEC-104/CIP/BACnet, confirm the codes Nozomi exposes via `Q-BASE-02` (is-this-function-used) before asserting on them.

## Modbus function codes (the worked example)
| Code | Meaning | Class |
|------|---------|-------|
| 1,2,3,4 | read coils / discrete inputs / holding / input registers | read (recon) |
| 5 | write single coil | **write** |
| 6 | write single register | **write** |
| 15 (0x0F) | write multiple coils | **write** |
| 16 (0x10) | write multiple registers | **write** |
| 8 | diagnostics (sub-functions) | disrupt |
| 43 (0x2B) | read device identification | recon |

## Placeholders used in the queries
Replace before deploying:
`<OT_ZONE>` `<IT_ZONE>` `<ENG_ZONE>` (your Guardian zone names) · `<MODBUS_MASTER_IP>` / `<MASTER_IP>` (authorized master/EWS) · `<MGMT_SUBNET>` (management network) · `<BROKER_IP>` (MQTT broker) · time windows in epoch-ms where shown.

## Where queries run
Per the white paper: most run on **Guardian** or **CMC**; a few (licensing) are **CMC-only**; some alert queries also work in **Vantage**. Each query below notes its target.
