# Threat Detection Assurance (TDA)

**A repeatable process to measure and verify that detection rules and use cases actually work** — validating the log feeds, the detection logic, the coverage, the false-positive rate, and the real Mean Time to Detect (MTTD). With worked test-case examples for both IT and OT/ICS.

![Focus](https://img.shields.io/badge/focus-detection%20validation%20%2F%20purple%20team-brightgreen)
![Framework](https://img.shields.io/badge/mapped-MITRE%20ATT%26CK-red)
![Scope](https://img.shields.io/badge/scope-IT%20%2B%20OT%2FICS-blue)
![License](https://img.shields.io/badge/license-MIT-green)

---

## Why TDA

A detection rule that has never been tested is a hypothesis, not a control. TDA turns "we have a rule for that" into "we proved it fires, with the right data, fast enough, without drowning us in false positives." It answers the question every SOC should be able to answer for every use case: **would we actually catch this?**

## The five goals

| Goal | What it verifies |
|------|------------------|
| **Log validation** | The necessary log sources feed properly into the SIEM/NDR — the data the rule needs is actually there |
| **Logic testing** | The detection rule correctly triggers during a simulated attack |
| **Blind-spot discovery** | Missing coverage or absent data streams are found and recorded |
| **False-positive reduction** | Thresholds are tuned so normal behavior doesn't alert |
| **Speed tracking** | The real-life **MTTD** is measured, not assumed |

## The process (four steps + close the loop)

```
  SCOPE ──▶ SIMULATE ──▶ VALIDATE ──▶ REMEDIATE ──▶ RETEST ──▶ REPORT
  choose    emulate the   did the      fix the root    prove    score &
  scenarios threat vector expected     cause of any    the fix   trend
  & use      (manual /    alert reach  failed          works
  cases      automated)   the SOC?     detection
```

1. **Scope definition** — choose the threat scenarios and use cases to test.
2. **Attack simulation** — emulate the threat vector (manual or automated).
3. **Alert validation** — verify the SOC receives the expected alert (right rule, right fields, right speed).
4. **Remediation & retesting** — fix the root cause of any failed detection, then test again.

Full method: [`docs/02-methodology.md`](docs/02-methodology.md).

## What's in this repo

```
threat-detection-assurance/
├── docs/
│   ├── 01-what-is-tda.md          ← definition, goals, where TDA fits
│   ├── 02-methodology.md          ← the goals + steps as a repeatable method, roles, cadence, pass/fail
│   ├── 03-attack-simulation.md    ← how to simulate safely (Atomic Red Team, Caldera, manual, OT)
│   ├── 04-metrics-and-reporting.md← MTTD, coverage, detection-health scorecard, reporting
│   └── 05-tda-in-ot.md            ← OT/ICS-specific: passive, safety-first validation
├── test-cases/
│   ├── examples/                  ← six worked test cases (IT + OT)
│   └── test-case-catalog.csv      ← machine-readable test backlog
└── templates/
    ├── test-case-template.md      ← the standard TDA test-case format
    ├── tda-report-template.md     ← per-cycle report
    └── remediation-tracker.md     ← failed-detection remediation log
```

## Worked examples
Six concrete test cases in [`test-cases/examples/`](test-cases/examples/), each: scenario → simulation → expected detection → validation criteria → result → remediation.

| ID | Scenario | Layer | Detection tested |
|----|----------|-------|------------------|
| [TDA-IT-001](test-cases/examples/TDA-IT-001-brute-force-success.md) | Brute-force success after failures | IT / identity | IAM-03 |
| [TDA-IT-002](test-cases/examples/TDA-IT-002-encoded-powershell.md) | Encoded PowerShell execution | IT / endpoint | EDR-01 |
| [TDA-IT-003](test-cases/examples/TDA-IT-003-dns-tunnelling.md) | DNS tunnelling | IT / egress | OUT-01 |
| [TDA-OT-001](test-cases/examples/TDA-OT-001-modbus-unauthorized-write.md) | Unauthorized Modbus write | OT / protocol | MOD-01 |
| [TDA-OT-002](test-cases/examples/TDA-OT-002-plc-program-download.md) | PLC program download | OT / engineering | S7-02 |
| [TDA-OT-003](test-cases/examples/TDA-OT-003-sis-keyswitch.md) | SIS key-switch to PROGRAM | OT / safety | SIS-B4 |

## How TDA fits the wider portfolio
TDA is the **assurance loop** around every detection library: it validates the `perimeter-to-endpoint`, `ot-protocol-defense`, `ot-historian-detection`, and `sis-safety-detection` rules, and it's the "validate" step of the detection lifecycle in the delivery playbook. Run it in the `ot-security-lab` so OT tests never touch production.

## Author
Prepared for detection engineering & SOC assurance — MSS Cyber Defense.

## License
MIT — see [`LICENSE`](LICENSE).

> TDA that involves attack simulation runs in a lab or under strict authorization. OT simulations never run against a live process — see [`docs/05-tda-in-ot.md`](docs/05-tda-in-ot.md).
