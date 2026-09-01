# MITRE ATT&CK for ICS — Data Sources for OT Detection

A practical mapping between the data sources referenced by MITRE ATT&CK for ICS and the concrete telemetry an OT SOC actually collects — and which library in this repo consumes each one. Use it to answer the two questions every detection program eventually faces: *what do we need to collect to detect this?* and *what does our current collection let us detect?*

## Framework note (accuracy)

In MITRE ATT&CK, a data source represents a subject of information a sensor or log can provide, and each one carries **data components** that pin down the specific property relevant to a technique. <cite index="4-1">Data sources also include data components, which identify specific properties or values relevant to detecting a given technique or sub-technique.</cite>

One current caveat worth stating up front: <cite index="4-1">data sources were deprecated in the ATT&CK v18 release in October 2025</cite>, and MITRE is steering detection toward **Detection Strategies and Analytics** instead. <cite index="4-1">The data sources page remains available for reference, but no new data sources are being added to the framework.</cite> That doesn't retire the concept for engineering purposes — you still have to know which telemetry feeds a detection — it reframes it. The Sigma rules and historian analytics in this repo *are* the analytics that realize that telemetry, so this mapping is written to bridge cleanly into the newer analytic-centric model.

The libraries here were authored against the ICS-classic data source names (Network protocol analysis, Data historian, Alarm history, and so on); the table below carries both those names and the modern data-component equivalents so the repo reads correctly against either version of the framework.

## OT-relevant data sources → telemetry → repo coverage

| ATT&CK for ICS data source | Modern data component (post-v14) | Concrete OT SOC telemetry | Consumed by |
|---|---|---|---|
| Network protocol analysis / Packet capture | Network Traffic Content (DS0029) | Zeek + ICSNPP dissectors; Nozomi Guardian DPI; Claroty/Dragos deep-packet inspection | `ot-ics-soc`, `it-dmz-ot-crosszone`, `threat-actor`, `shieldworkz-advisory` |
| Netflow / Enclave netflow | Network Traffic Flow (DS0029) | Firewall/router flow records at the IT↔OT boundary; span/tap flow | `it-dmz-ot-crosszone` |
| Network device logs | Network Connection Creation (DS0029) | OT firewall, L2/L3 switch, remote-access gateway logs | `it-dmz-ot-crosszone` |
| Data historian | Process History/Live Data — Operational Databases (DS0040) | PI / Proficy / Canary / Ignition historian values; PI Web API / OPC UA feed | `ot-historian-detection` |
| Alarm history / Alarm thresholds | Process/Event Alarm — Operational Databases (DS0040) | Historian alarm subsystem; DCS/SCADA alarm & event journal; SER/SOE | `ot-historian-detection` (G-family) |
| Controller parameters | Device Configuration/Parameters — Asset (DS0039) | Setpoint/parameter values via OPC UA node reads and historian SP tags; EWS project config | `ot-historian-detection` (B-setpoint), `ot-ics-soc` |
| Controller program | Application Binary / program transfer — Asset (DS0039) | S7comm block up/download and DNP3/IEC program transfers on the wire; EWS engineering-action logs | `ot-ics-soc` (S7comm), `threat-actor` |
| Asset management | Asset Inventory — Asset (DS0039) | Nozomi/Claroty passive asset inventory; CMDB; DHCP/ARP baselines | `it-dmz-ot-crosszone` (new/rogue asset) |
| Application logs | Application Log Content (DS0015) | HMI/SCADA application logs; engineering-software logs; OPC UA server logs | `threat-actor`, `shieldworkz-advisory` |
| Authentication logs | Logon Session Creation/Metadata (DS0028); User Account Authentication (DS0002) | Windows security logs on EWS/HMI/historian hosts; AD auth; OPC UA session establishment | `ot-ics-soc` (OPC UA anon auth), `it-dmz-ot-crosszone` |
| File monitoring | File Access/Modification/Creation (DS0022) | File-integrity monitoring on EWS/historian; project-file change tracking | `threat-actor` |
| Process monitoring / command-line | Process Creation, Command Execution (DS0009/DS0017) | EDR on Level 2–3 Windows assets (EWS, HMI, historian host) | `threat-actor`, `shieldworkz-advisory` |
| Windows Registry | Windows Registry Key Modification (DS0024) | EDR / Sysmon on OT Windows endpoints | `threat-actor` |
| Sequential event recorder | Process/Event Alarm (DS0040) | SER/SOE streams in power & utility environments | *(planned)* |

## The two OT-native data sources most SOCs miss

Almost every OT SOC ingests **Network protocol analysis** (via Nozomi or Zeek) because it's the obvious network-visibility play. Two ICS-native data sources are routinely left on the floor, and they're precisely the ones that see manipulation the network layer can't:

- **Data historian** → *Process History/Live Data* under Operational Databases (DS0040). This is the physics layer. It's the sole telemetry that reveals whether a legitimate-looking command drove the process outside its safe envelope — the entire premise of the `ot-historian-detection` library.
- **Alarm history / thresholds** → *Process/Event Alarm* (DS0040). Alarm suppression, shelving, and trip-point approach live here. Attacks that target the Safety Instrumented System (TRITON-class) surface as alarm and trip-margin behaviour before they surface anywhere else.

Wiring these two into the SIEM alongside protocol analysis is the difference between detecting *that a write happened* and detecting *that the process was harmed*.

## Collection priority for a new deployment

1. **Network protocol analysis** (Nozomi/Zeek ICSNPP) — broadest technique coverage per unit of effort; feeds three of the four Sigma libraries.
2. **Netflow + network device logs** at the IT↔OT boundary — enables the cross-zone library and boundary-crossing detections.
3. **Data historian + alarm history** — unlocks the physics and safety layers (the historian library) that nothing else can see.
4. **Authentication + application logs** from Level 2–3 Windows assets — attributes activity to accounts and stations.
5. **Endpoint (EDR/Sysmon)** on EWS/HMI/historian hosts — threat-actor host-side TTPs.

## References

- MITRE ATT&CK for ICS — https://attack.mitre.org/matrices/ics/
- ATT&CK Data Sources (reference, deprecated v18) — https://attack.mitre.org/datasources/
- ATT&CK Data Components — https://attack.mitre.org/datacomponents/

> Mappings above are engineering guidance, not an official MITRE work product. Data-component names track ATT&CK's evolving schema; confirm against your deployed ATT&CK version.
