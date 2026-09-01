# <ID> — <Title>

## Problem
What an attacker/fault does, and why the historian sees it.

## Detection concept
Baseline established, deviation condition, persistence requirement.

## Data required
Tags, sources, lookups (per [`../../docs/data-model.md`](../../docs/data-model.md)).

## Logic
- Splunk: [`splunk.spl`](splunk.spl)
- Sentinel: [`sentinel.kql`](sentinel.kql)

## Tuning
Thresholds, dwell, mode gating, known benign excursions.

## Response
SOC runbook steps. Read-only; corroborate before escalation.

## MITRE ATT&CK for ICS
- TXXXX — Technique name

## Validation
See [`validation.md`](validation.md).
