# Source repositories

This page records what each original repository contributes to the consolidated program. The
exact file-level decisions are available in `consolidation-manifest.csv`.

| Source repository | Consolidated location | Contribution |
|---|---|---|
| `OT-detection-program` | Repository core | Canonical lifecycle, telemetry model, 257-detection catalog, KQL/SPL, protocols, response and generated crosswalks |
| `ot-detection-engineering` | `02-detection/extensions/detection-engineering/` | Detection engineering guidance, Sigma libraries and historian analytics |
| `ot-protocol-defense` | `03-protocols/extensions/protocol-defense/` | Protocol attack-surface and log-source guidance |
| `ot-protocol-defense_NDR` | `02-detection/extensions/protocol-ndr/` | NDR-focused material and Nozomi query guidance |
| `perimeter-to-endpoint-detections` | `02-detection/extensions/perimeter-to-endpoint/` | Perimeter, identity, endpoint and cross-zone analytics |
| `sis-safety-detection` | `02-detection/extensions/sis-safety/` | Safety-instrumented-system detection context |
| `ot-threat-content-repo` | `02-detection/extensions/threat-content/` | Threat-informed content lifecycle and coverage context |
| `ot-scada-server-detection` | `02-detection/extensions/scada-server/` | Host and correlation analytics for SCADA servers |
| `it-ot-incident-response` | `04-response/extensions/it-ot-incident-response/` | IT/OT incident coordination, SOPs, evidence and templates |
| `threat-detection-assurance--TDA` | `06-assurance/threat-detection-assurance/` | Detection validation methodology, test cases and reporting templates |
| `ot-monitoring-deployment` | `07-operations/monitoring-deployment/` | Pre-deployment and log-onboarding activities |
| `ot-siem-log-source-onboarding` | `07-operations/siem-log-source-onboarding/` | SIEM onboarding workflow and linkage catalog |
| `ot-soc-delivery-playbook` | `07-operations/soc-delivery-playbook/` | Business case, prerequisites, lifecycle and proposal guidance |
| `ot-soc-journey-map` | `07-operations/soc-journey-map/` | Stakeholder-oriented service journey material |
| `ics-procurement-language` | `08-governance/procurement-language/` | Contractable control clauses, FAT/SAT measures and standards mapping |
| `ot-mss-capability` | `08-governance/managed-security-services/` | Managed OT security capability model, service definitions and templates |
| `ot-security-study-guide_New` | `09-learning/ot-security-study-guide/` | OT foundations, protocols, adversaries, hunting, response and career practice |
| `building-ai-agents` | `09-learning/building-ai-agents/` | Applied agent design, tool use, safety, evaluation and production practices |

`My-rep` contained no files and therefore contributes no content. The empty target repository
was used as the clean destination.

## Relationship between the source domains

The repositories are not treated as independent books. They form one operating chain:

1. Program governance and procurement define requirements and ownership.
2. Deployment and log onboarding make the required evidence available.
3. Protocol and threat knowledge drive detection hypotheses.
4. Detection engineering turns hypotheses into governed analytics.
5. Assurance proves whether those analytics work.
6. Monitoring, hunting and investigation establish what happened.
7. Response playbooks guide safe, coordinated action.
8. Metrics, learning and service-delivery material sustain improvement.
