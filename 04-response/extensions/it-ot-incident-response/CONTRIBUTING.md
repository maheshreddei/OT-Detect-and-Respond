# Contributing

This is a template IR framework. Adapt it to your site; keep these conventions.

## Rules
- **Never commit real incident data, evidence, or site specifics** — the `.gitignore` blocks common evidence formats, but check every commit. Filled templates go in an access-controlled evidence store, not git.
- Keep the doctrine intact: safety first, passive before active, operations in the loop. New playbooks must respect the authority-to-act matrix.
- Every playbook maps response steps to **evidence that proves the assertion**, referencing the evidence guides and matrix.
- Map scenarios to MITRE ATT&CK for ICS.

## Adding a playbook
Copy an existing `playbooks/pb-*.md` and keep the shape: indicators → severity → triage → evidence (with what it proves) → analysis → OT-safe containment → eradication/recovery → proof-artifact checklist.

## Adding an evidence source
Add it to `evidence/evidence-source-matrix.md` (assertion → location → collection → proves → volatility) and, if it's a new domain, a guide under `evidence/`.
