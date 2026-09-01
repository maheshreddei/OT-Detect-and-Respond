# Document Request Checklist / Tracker

A template to run the pre-deployment document request when engaging a plant. Copy per engagement; fill the status columns.

Status key: `Requested` · `Received` · `Partial` · `Stale` (exists but outdated) · `Missing` (to be produced during deployment).

## Priority set (request first)
| # | Document | Owner (plant) | Status | Version / date | Notes / gaps |
|---|----------|---------------|--------|----------------|--------------|
| 1 | High-Level Design (HLD) | | | | |
| 2 | Low-Level Design (LLD) | | | | |
| 3 | Network Architecture Diagram | | | | |
| 4 | Purdue / Zone & Conduit Diagram | | | | |
| 5 | Asset Inventory | | | | |
| 6 | Communication Matrix | | | | |
| 7 | Firewall Rule Matrix | | | | |
| 8 | P&ID | | | | |
| 9 | PLC I/O List | | | | |
| 10 | Historian Tag List | | | | |
| 11 | Risk Assessment | | | | |
| 12 | Incident Response Procedures | | | | |

## Full package (complete coverage)
| Document | Owner (plant) | Status | Version / date | Notes / gaps |
|----------|---------------|--------|----------------|--------------|
| Data Flow Diagram | | | | |
| Cause & Effect Matrix | | | | |
| Log Source Matrix | | | | |

## Engagement notes
- **Handling:** these documents are sensitive (they map the plant's attack surface). Store with access control; follow the customer's data-handling and NDA terms.
- **Gaps → deployment scope:** every `Missing`/`Stale` item becomes a deployment task (e.g. passive asset discovery to build the inventory, traffic baselining to build the communication matrix).
- **Sign-off:** confirm with plant engineering/operations before any action that touches the process; monitoring setup stays passive/read-only.

## Readiness gate
Proceed to sensor placement and onboarding when the **priority set** is at least `Received`/`Partial` and any `Missing` items have an owner and a plan. Then sequence log sources per [`../log-onboarding/onboarding-guide.md`](../log-onboarding/onboarding-guide.md).
