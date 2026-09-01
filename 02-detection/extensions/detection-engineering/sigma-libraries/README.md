# Sigma Use Case Libraries

Four OT/ICS Sigma detection libraries — **87 rules total**. Each rule is an individual `.yml` under its library's `rules/` folder; the authored Word deliverable is preserved under `source/`.

| Library | Rules | Focus |
|---------|-------|-------|
| [`ot-ics-soc`](ot-ics-soc/) | 20 | Protocol-level: Modbus, DNP3, OPC UA, S7comm, IEC 60870-5-104 |
| [`it-dmz-ot-crosszone`](it-dmz-ot-crosszone/) | 27 | IT/DMZ→OT cross-zone, mapped to the Purdue model |
| [`threat-actor`](threat-actor/) | 20 | Sandworm, APT34, CHERNOVITE/PIPEDREAM, XENOTIME/TRITON |
| [`advisory`](advisory/) | 20 | Middle East OT threat-intelligence-derived |

## Deployment notes (all libraries)

- Field names follow **Zeek ICSNPP** parser output and **Nozomi Guardian/Vantage** export conventions (`proto`, `function_code`, `src_ip`, `node_id`, `type_id`, …). Map to your SIEM's parsed field names first.
- Every rule carries **placeholder subnets/allow-lists** commented inline — replace with your asset inventory before enabling.
- Rules are `status: experimental`. Validate in a non-production pipeline before promotion.
- Telemetry each library needs is mapped in [`../docs/mitre-ics-data-sources.md`](../docs/mitre-ics-data-sources.md).
