# OT Detection Use Case Lifecycle

This lifecycle governs how a use case moves from an identified threat to production
detection content and, eventually, to retirement. It is the process layer that sits on
top of the catalog: every row in `catalog/use-case-catalog.csv` carries a
`Lifecycle_Stage` value drawn from the stages below, so the catalog doubles as a live
program status board.

The lifecycle is deliberately safety-first. In OT, a false negative and a badly tuned
detection both carry operational risk, so validation is gated on evidence, not opinion.

## Stages

| Stage | Definition | Entry gate | Exit gate |
|-------|------------|------------|-----------|
| Proposed | Threat or gap identified; use case has an ID and a threat/ATT&CK anchor | Threat intel, incident, gap analysis, or customer request | UC record created with actor + technique + sector + data source populated |
| In-Development | Detection logic being authored (Sigma, N2QL, or native tuning) | Data source confirmed available; log/telemetry sample obtained | Draft rule committed; field mapping documented |
| Validated | Logic tested against benign and malicious samples in a non-prod zone | Test plan written (see template) | True positive fires on emulated technique; false-positive rate acceptable; peer review passed |
| Production | Deployed to the live monitoring platform and SOC runbook | Change approved; owner and runbook assigned | Alert visible in SOC queue; SLA and severity confirmed |
| Tuning | Live-tuning against real telemetry; thresholds and allowlists adjusted | Alert volume or fidelity outside target | Fidelity restored to target; changes version-bumped |
| Retired | Superseded, deprecated technique, or asset removed | Replacement UC live, or threat no longer relevant | UC marked Retired with rationale; content archived not deleted |

## Gate criteria detail

**Proposed to In-Development.** The UC must name its threat anchor (actor and/or ATT&CK
for ICS technique), the affected sectors, the Purdue level, the protocol, and the primary
data source. If the data source does not exist in the environment, the UC stays Proposed
and becomes a collection requirement, not a detection task.

**In-Development to Validated.** The detection logic exists as a committed artifact under
`detections/` and its field mapping to the target platform (Splunk, Nozomi, sensor) is
written down. Nothing reaches Validated on paper alone.

**Validated to Production.** Two evidence artifacts are required: a positive test (the
technique was emulated and the rule fired) and a false-positive assessment (benign
operational traffic did not trigger it, or the exceptions are documented). Peer review is
mandatory. For any use case touching a Safety Instrumented System, the exit review
includes the OT/process engineering owner, not only the detection engineer.

**Production to Tuning and back.** Tuning is a normal, recurring state, not a failure.
Every tuning change increments the content version and is captured in the commit history,
which is why the repository is the source of truth rather than the platform console.

## How the lifecycle maps to the catalog

The `Lifecycle_Stage` column is the single field that turns the catalog into a program
dashboard. A simple pivot on that column answers the questions leadership asks: how much
of the intended coverage is actually in production, how much is stuck in development, and
where the validation backlog sits. Coverage claims should always be qualified by stage -
a technique with only Proposed use cases is a coverage gap, not coverage.
