# OT Detection Engineering

**A portfolio of production-oriented detection content for ICS/OT environments** — Sigma protocol/threat libraries and a process-historian baseline-and-deviation library, mapped end-to-end to MITRE ATT&CK for ICS.

![Sigma rules](https://img.shields.io/badge/sigma%20rules-87-blue)
![Historian detections](https://img.shields.io/badge/historian%20detections-6%20built%20%2F%2032%20cataloged-blue)
![Platforms](https://img.shields.io/badge/platforms-Splunk%20%7C%20Sentinel%20%7C%20Zeek%2FICSNPP%20%7C%20Nozomi-orange)
![Framework](https://img.shields.io/badge/mapped-MITRE%20ATT%26CK%20for%20ICS-red)
![Standards](https://img.shields.io/badge/aligned-NIST%20800--82r3%20%7C%20IEC%2062443-lightgrey)
![License](https://img.shields.io/badge/license-MIT-green)

---

## What's here

Two complementary detection layers. The Sigma libraries watch the **network and host** — what commands and sessions crossed the wire. The historian library watches the **physics** — whether those commands drove the process outside its safe, normal envelope. Together they cover both halves of an OT attack.

```
ot-detection-engineering/
├── sigma-libraries/              ← 87 Sigma rules across 4 libraries
│   ├── ot-ics-soc/               ← 20 · protocol-level (Modbus/DNP3/OPC UA/S7comm/IEC104)
│   ├── it-dmz-ot-crosszone/      ← 27 · IT/DMZ→OT cross-zone (Purdue-mapped)
│   ├── threat-actor/             ← 20 · Sandworm, APT34, CHERNOVITE, XENOTIME/TRITON
│   └── shieldworkz-advisory/     ← 20 · Middle East OT threat-intel-derived
├── ot-historian-detection/       ← baseline & deviation on process historians
│   └── detections/               ← 6 built (A01,B01,C01,D02,E01,G01) / 32 cataloged
├── docs/
│   └── mitre-ics-data-sources.md ← telemetry → ATT&CK-ICS data source mapping
├── CONTRIBUTING.md
└── LICENSE
```

## The two layers

### Sigma libraries — network & host detection
Four libraries, **87 rules**, each rule an individual validated `.yml` with an ATT&CK-ICS tag, false-positive guidance, and a severity level. Authored against Zeek ICSNPP / Nozomi Guardian field names. Human-readable indexes render on GitHub; the original authored Word deliverables are preserved under each library's `source/`. See [`sigma-libraries/`](sigma-libraries/).

### Historian library — process & physics detection
Baseline-and-deviation detections on the process historian — the only telemetry that reveals whether a legitimate-looking command actually *harmed the process*. Six built detections (each with Splunk SPL, Sentinel KQL, YAML, and validation cases) including the two that most differentiate a senior portfolio: **E01 historian-vs-live-PLC divergence** (Stuxnet-class) and **G01 SIF trip-point approach** (TRITON-class). See [`ot-historian-detection/`](ot-historian-detection/).

## How they fit together

| Attack | Network/host layer (Sigma) | Physics layer (historian) |
|---|---|---|
| Unauthorized setpoint change | `ot-ics-soc` — Modbus/OPC UA write from unauthorized source | `B01` — setpoint outside approved range |
| Safety-system targeting (TRITON) | `threat-actor` — XENOTIME/TRITON TTPs | `G01` — SIF trip-point approach |
| View manipulation / replay (Stuxnet) | `ot-ics-soc` — protocol anomalies | `E01`/`C01` — divergence & frozen-value |
| Cross-zone pivot to OT | `it-dmz-ot-crosszone` — boundary-crossing flows | `D02` — impossible state combination |

A correlation that fires on *both* layers — a Sigma protocol alert **and** a historian deviation on the same asset — is a high-confidence, low-false-positive incident. That fusion is the point of keeping both in one repo.

## Data sources

Every detection here is only as good as the telemetry beneath it. [`docs/mitre-ics-data-sources.md`](docs/mitre-ics-data-sources.md) maps the MITRE ATT&CK for ICS data sources to the concrete OT SOC telemetry that feeds them (Zeek ICSNPP, Nozomi DPI, historian, EWS EDR, boundary netflow) and shows which library consumes each — including the two OT-native sources most SOCs leave on the floor: **Data historian** and **Alarm history**.

## Quick start

1. Pick a layer. For Sigma: map ICSNPP/Nozomi fields to your SIEM and replace placeholder allow-lists. For historian: stand up the data model and baselines per that folder's docs.
2. Deploy a handful of rules/detections into scheduled searches or analytics rules.
3. Validate before promoting — the historian detections ship explicit validation cases; the Sigma rules carry false-positive guidance.
4. Correlate across layers for the high-confidence wins.

## Standards alignment

Detections map to **MITRE ATT&CK for ICS** throughout, and align to **NIST SP 800-82 Rev 3** and **IEC 62443** zone/conduit and monitoring guidance. The historian library additionally structures delivery around **NIST CSF 2.0** (Identify/Detect/Respond, plus Govern) with a RACI and KPI cadence for managed-service use.

## Author

Mahesh Reddy — OT/ICS Security · GICSP, SANS ICS410, Nozomi Certified

## License & handling

MIT — see [`LICENSE`](LICENSE).

> **Before making this repository public:** the Sigma libraries and historian lookups use illustrative tag names, subnets, and trip limits, but review every file for anything that could resemble a real client's asset inventory, addressing, or threat intel. Keep the repo **private** until that review is done. All detection logic is read-only; nothing here writes to a control system.
