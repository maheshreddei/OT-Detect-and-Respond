# Threat Detection Engineering and Tuning

## Objective

Translate process risk into observable behavior, prove required telemetry, validate safely, integrate with SOC operations and continuously measure efficacy. Exact alert names and licensed features vary by N2OS release; design around behaviors and outcomes.

## Lifecycle

~~~text
threat/process risk
 -> hypothesis
 -> telemetry/coverage check
 -> logic/configuration
 -> safe validation
 -> SOC/OT workflow
 -> governed tuning
 -> metrics and revalidation
~~~

A use case is not ready until the sensor sees the required direction, protocol and asset context.

## Use-case specification

Every use case records: stable ID/title; risk and process consequence; assets/zones; observable hypothesis; required capture point/protocol/functions/external logs; release-specific Nozomi configuration/query; severity; safe validation; analyst triage; authorized response; exceptions; metrics; technical/process owner and review date.

## Priority families

**Identity/topology:** new node/link; wrong zone; retired asset returns; new conduit; time/network infrastructure change.

**Industrial operations:** logic/program upload/download; firmware or run/stop/reset/mode change; force/write/setpoint command; engineering protocol from unauthorized source; SIS interaction outside expected peer/window.

**Remote/admin:** new vendor source; RDP/SSH/SMB/WinRM; access outside window; one-to-many administration; jump-host bypass.

**Threat/network:** scanning, enumeration, failed-connection bursts, malformed operations, new internet/DNS destination, beaconing, abnormal transfer, IOC/signature/reputation match, weak authentication exposure.

**Reliability:** asset/link disappearance, abnormal process communication, storm, redundant-path failure, zero capture, stale collector and integration failure.

## Severity model

Combine vendor severity with process/safety criticality, confidence/corroboration, command capability, conduit crossed, maintenance approval, exposure, scope and compensating controls.

- P1: credible unauthorized control/safety action or active compromise.
- P2: suspicious engineering/admin behavior on critical assets.
- P3: policy deviation, new asset/link or vulnerable exposure.
- P4: information/baseline/monitoring-health event.

Tailor to incident policy.

## Baseline

Observe steady state, startup/shutdown, batch or recipe change, failover, patching, vendor maintenance, backups and engineering work. Record modes not observed and missing feeds. Do not suppress rare high-consequence activity merely because it occurred during learning.

## Safe validation

Preferred order: confirmed historical event; lab/digital twin; supported isolated PCAP replay; approved benign administrative test; tabletop. Never manipulate a PLC/SIS/process simply to trigger an alert.

Validate end to end:

~~~text
behavior -> Guardian -> CMC/Vantage -> SIEM -> case -> analyst -> OT owner
~~~

Check timestamps, asset/site, severity, parser fields, escalation and closure evidence.

## Tuning governance

Tune by scope, context, approved schedule, threshold, time-limited exception, routing or redesign. Avoid global suppression.

Each entry includes sample events, disposition, root cause, affected scope, exact change, missed-detection risk, owner approval, before/after evidence, rollback, expiry and review date. A benign positive can be a correct detection of approved but risky behavior.

## Operating rhythm

**Daily:** critical alert delivery, process-aware triage, change correlation and escalation.

**Weekly:** noisy/missed/stale detections, new assets/protocols, packet/parser health, new hypotheses and expired exceptions.

**Monthly:** threat-family/conduit coverage, dispositions, detection latency, blind spots, content impact and undetected priority risks.

**Quarterly:** safe retest/tabletop, threat-model alignment, RBAC/config review and process-owner signoff.

## Metrics

- Critical use cases with validated telemetry.
- Critical conduits with bidirectional visibility.
- Detection-to-triage and triage-to-owner time.
- Validation pass rate and disposition completeness.
- False/benign-positive rates per use case.
- Expired exceptions and aged unknown cases.
- Monitoring/integration uptime.
- Missed detections from incidents.
- Coverage gaps closed.

Do not optimize only for fewer alerts.

## Release/content changes

Review release notes; back up; test on non-production/low-risk ring; record parser/alert/classification changes; monitor load/event rate; revalidate priority use cases and integrations; roll out with stop criteria and support/rollback plan.

## Acceptance criteria

- Priority risks have testable observable hypotheses.
- Capture/parser coverage is proven.
- Severity includes process consequences.
- Tests are safe and owner-approved.
- Exceptions are scoped and expire.
- End-to-end routing is demonstrated.
- Metrics expose efficacy and blind spots.
