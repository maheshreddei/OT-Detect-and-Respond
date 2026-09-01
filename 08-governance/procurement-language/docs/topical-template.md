# The 8-Part Topical Template

Every control in this document is written to the same eight-part structure. This is the feature that makes the document a *requirements library* rather than a set of recommendations: each control is testable, maintainable, and traceable to a rationale.

| # | Part | Answers | Used by |
|---|------|---------|---------|
| 1 | **Basis** | *Why* does this control matter? What risk does it address? | Justifying the requirement to stakeholders |
| 2 | **Language Guidance** | *How* should the requirement be understood and tailored? Context, caveats, options. | The engineer tailoring the clause to the system |
| 3 | **Procurement Language** | The *actual contract text* — "the Vendor shall…" | Drops straight into the RFP/contract |
| 4 | **FAT Measures** | How is compliance verified at **Factory Acceptance Test**, before delivery? | Acceptance criteria at the vendor site |
| 5 | **SAT Measures** | How is compliance verified at **Site Acceptance Test**, after installation? | Acceptance criteria on site |
| 6 | **Maintenance Guidance** | How is the control kept effective over the system's 15–30 year life? | Sustaining the requirement post-deployment |
| 7 | **References** | Supporting standards and sources. | Traceability |
| 8 | **Dependencies** | Which other controls this one relies on. | Sequencing and completeness |

## How to use the template in practice

- **Writing an RFP:** lift **part 3 (Procurement Language)** into the tender, adjusted per **part 2 (Language Guidance)**. Attach **parts 4–5 (FAT/SAT Measures)** as the acceptance criteria the vendor must satisfy.
- **Evaluating bids:** score vendor responses against the Procurement Language and require evidence they can meet the FAT/SAT Measures.
- **Managing the contract:** carry **part 6 (Maintenance Guidance)** into the O&M agreement so the control doesn't decay after go-live.
- **Ensuring completeness:** follow **part 8 (Dependencies)** so you don't specify a control while omitting one it needs.

## Why FAT/SAT matters in OT procurement
Factory and Site Acceptance Tests are the natural, low-risk gates to *verify security before a system controls a live process*. Specifying security tests as part of FAT/SAT means vulnerabilities are found on a test bench and at commissioning — not discovered in production where scanning or remediation could disrupt operations. The template's explicit FAT/SAT parts turn each security requirement into something you can actually accept or reject the delivery on.
