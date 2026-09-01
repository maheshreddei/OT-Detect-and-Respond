# OT SCADA Server Detection (S-01)

Detection content for a **Control / SCADA Server** (asset S-01) in an OT/ICS
environment. A SCADA server is a Windows-class supervisory host, so coverage is
IT-style **host telemetry** (Enterprise ATT&CK precursors) **plus** correlation of
**controller telemetry against operator intent** (ATT&CK for ICS) — the half that
protocol-only detection libraries never touch.

Rules ship as [Sigma](https://github.com/SigmaHQ/sigma) with **compiled Microsoft
Sentinel (KQL)** and **Splunk (SPL)** queries, and the correlation use cases include
**Nozomi Networks N2QL** for the controller stream.

## Layout
```
.
├── host/
│   ├── sigma/                     # 9 rule files (10 docs) - Enterprise ATT&CK, host-side
│   └── compiled/
│       ├── s01_host_sentinel.kql  # all host rules, Sentinel
│       └── s01_host_splunk.spl    # all host rules, Splunk
├── correlation/                   # controller telemetry x host intent (ATT&CK for ICS)
│   ├── UC-S01-001_operator_intent.md             # T0855
│   ├── UC-S01-002_program_download_provenance.md # T0843
│   └── UC-S01-003_change_operating_mode.md       # T0858
└── coverage/
    └── S-01_row.md                # matrix row: 0/0 -> 14 techniques / 12 detections
```

## Coverage
| | |
|---|---|
| **Techniques** | 14 (11 Enterprise, 3 ICS) |
| **Detections** | 12 (9 host Sigma + 3 correlation) |

**Enterprise:** T1021.001, T1136.001, T1098, T1543.003, T1053.005, T1059.001,
T1003.001, T1574, T1091, T1562.001, T1071
**ICS:** T0855, T0843, T0858 (enrichment references T0831)

## Data sources
Windows Security (logon, account, service/task, audit, PnP), Sysmon (1/3/7/10/11)
or MDE `Device*` equivalents, the SCADA operator-action / tag-write audit log, and the
Nozomi controller command/write stream (SIGN:/PROTOCOL:/VI: assertions).

## Deploy
1. Replace placeholders: S-01 IP/hostname, jump-host list, OT egress allowlist,
   SCADA/HMI runtime image names, sanctioned EWS list, change-window calendar.
2. Onboard the two correlation streams — SCADA operator-action log and the Nozomi
   controller stream — or the correlation use cases run host-only / degraded.
3. Confirm Nozomi `type_id` values against your N2OS version and enabled protocol packs
   (the N2QL uses representative SIGN: identifiers, not guaranteed literals).
4. Validate Sigma offline before deploy, e.g. `otdt validate host/sigma/`.

## Design notes
- Sigma cannot cleanly express the **absence** match at the core of UC-S01-001 (a command
  with *no* matching operator action); that logic lives in the platform-native KQL/SPL.
- `DeviceImageLoadEvents` signature columns vary by tenant; the unsigned-DLL rule falls
  back to the Sysmon EventID 7 path (`Signed` / `SignatureStatus`) where they are absent.
- Response posture is safety-first: alerts notify the control room / process engineer;
  containment on the OT path requires process-engineer authorization, never auto-block.

## License
MIT — see [LICENSE](LICENSE). All detection content here is original; no third-party
attribution applies to this repository.
