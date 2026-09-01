# Test Cases

Worked TDA test cases in [`examples/`](examples/) and the machine-readable backlog in [`test-case-catalog.csv`](test-case-catalog.csv).

Each test case follows [`../templates/test-case-template.md`](../templates/test-case-template.md):
scope → simulation → expected detection → validation criteria → result → remediation.

| ID | Scenario | Layer | Detection | ATT&CK |
|----|----------|-------|-----------|--------|
| TDA-IT-001 | Brute-force success after failures | IT | IAM-03 | T1110 |
| TDA-IT-002 | Encoded PowerShell | IT | EDR-01 | T1059.001 |
| TDA-IT-003 | DNS tunnelling | IT | OUT-01 | T1071.004 |
| TDA-OT-001 | Unauthorized Modbus write | OT | MOD-01 | T0836 |
| TDA-OT-002 | PLC program download (S7) | OT | S7-02 | T0843 |
| TDA-OT-003 | SIS key-switch to PROGRAM | OT | SIS-B4 | T0858 |

Build your own from the template; add each to the catalog CSV as a backlog item.
