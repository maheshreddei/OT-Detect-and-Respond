# Detections

Detection artifacts referenced by the catalog. Each file carries a `uc_id` and a
`nozomi_type_id` so it is self-describing.

## `sigma/`

Portable Sigma rules for OT protocol and network use cases. These are treated as the
**source format** for anything portable and are compiled to the SIEM backend (Splunk SPL)
downstream with a pySigma pipeline. Notes:

- Rules assume a **Zeek OT logsource** using ICSNPP-style parser fields
  (`modbus`, `dnp3`, `s7comm`, `iec104`, `conn`). If your telemetry comes from Nozomi
  syslog or a different parser, remap the `logsource` and field names accordingly.
- Every rule that relies on an allowlist (authorized master / EWS / control center /
  OT CIDR) has that list inlined with placeholder addresses and a comment. Baseline these
  before enabling - the allowlist is where the false-positive risk lives.
- Custom keys (`uc_id`, `nozomi_type_id`, `sectors`, `threat_actors`) are appended below
  the standard Sigma body. They are ignored by Sigma tooling and carried for catalog join.

Current rules: unauthorized Modbus write, Modbus FC08 restart, S7comm STOP CPU, DNP3
restart, IEC-104 unauthorized control, OT subnet scan.

## `nozomi-n2ql/`

Nozomi N2QL queries and Assertion logic for use cases that lean on Nozomi-native
detection. These run on the sensor / Vantage rather than the SIEM. Validate field names
against your Guardian version's data model before deploying (see
`../docs/nozomi-alert-taxonomy.md`).

Current queries: new node in critical zone, internet-exposed device, malware-over-SMB
surfacing.

## Adding a detection

1. Author the logic; set `uc_id` to the catalog UC ID.
2. Confirm the `nozomi_type_id` matches `../catalog/nozomi-alert-mapping.csv`.
3. Validate with `../lifecycle/validation-test-plan-template.md` before moving the
   catalog `Lifecycle_Stage` beyond In-Development.
