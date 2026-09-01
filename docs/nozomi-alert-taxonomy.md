# Nozomi Alert Taxonomy (for this repository)

This document explains how the `Nozomi_Type_ID` column and `nozomi-alert-mapping.csv` are
structured, and how to keep them accurate against your own Guardian deployment.

## The Type ID is the integration key

In the Nozomi data model, each alert type has a **strict identifier - the Type ID** - and
Nozomi's own guidance is that this field, not a friendly name and not a regex over the
message text, is what you key integrations and SIEM parsing on. The Type ID is exposed as
`type_id` in the API and appears in the syslog/CEF record. Example CEF fragment from a
malware alert:

```
CEF:0|Nozomi Networks|N2OS|...|SIGN:MALWARE-DETECTED|Malware detected|9| ...
    flexString1=T0843 flexString1Label=mitre_attack_techniques ...
```

Note two things in that one record: the Type ID (`SIGN:MALWARE-DETECTED`) and the native
ATT&CK for ICS technique (`T0843`). Both are usable directly in your SIEM.

## Type ID prefix convention

Type IDs are namespaced by a prefix that indicates the detection family. The prefixes used
in this repository:

| Prefix | Family | Detection basis |
|--------|--------|-----------------|
| `SIGN:` | Threat intelligence / signatures | Yara rules, packet rules, STIX/IOC reputation |
| `NET:` | Network behaviour | Learned baseline, scans, new node/link, bandwidth |
| `PROT:` | Protocol validation | Malformed packets, illegal/high-risk protocol functions |
| `VI:` | Node / inventory / variable | Asset visibility, exposure, variable changes |

Representative Type IDs referenced by the catalog include `SIGN:MALWARE-DETECTED`,
`SIGN:PACKET-RULE`, `SIGN:MALICIOUS-IP`, `NET:NEW-NODE`, `NET:NEW-LINK`,
`NET:TCP-SYN-SCAN`, `PROT:MODBUS-ILLEGAL`, `PROT:DNP3-ILLEGAL`, `PROT:IEC104-ILLEGAL`,
`PROT:S7-ILLEGAL`, and `VI:NEW-NODE`.

## Native vs Assertion

The `Native_or_Assertion` column records whether Guardian raises an alert out of the box or
whether a custom **Assertion / N2QL** is required to express the specific condition:

- **Native** - Guardian generates the alert from its built-in analysis (e.g. a new node, a
  malformed packet, a Yara match). You consume it; you may still tune it.
- **Assertion** - the specific condition (e.g. "Modbus FC08 sub-function 04 from a
  non-authorized master") is narrower than a built-in type and is expressed as a
  user-defined Assertion, often surfacing under a protocol or custom Type ID.
- **Native+Assertion** - Guardian raises a broad native alert and you add an Assertion to
  sharpen fidelity or add zone/source context.

## Keeping this accurate against your deployment

Exact Type ID strings and the set of available types **vary by N2OS version**. Treat the
Type IDs here as a working reference, and reconcile them against the authoritative list in
your Guardian version's **Alerts and Incidents - Reference Guide** (Nozomi technical docs).
Before relying on a Type ID in production parsing:

1. Trigger or locate a real instance of the alert.
2. Read the `type_id` from the syslog/CEF export or the API.
3. Confirm it matches the catalog; update the CSV if your version differs.

Because the Type ID is the integration key, a mismatch here silently breaks SIEM
correlation - which is exactly why it is worth verifying per environment rather than
trusting any static list, including this one.
