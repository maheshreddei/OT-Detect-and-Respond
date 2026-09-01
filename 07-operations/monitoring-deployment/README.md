# OT Monitoring Deployment Readiness

**Everything you need to stand up OT monitoring (Nozomi, Microsoft Sentinel, or any OT SIEM/NDR) safely and effectively — the documents to gather *before* deployment, and the order to onboard log sources *after*.**

![Scope](https://img.shields.io/badge/scope-pre--deploy%20docs%20%2B%20log%20onboarding-blue)
![For](https://img.shields.io/badge/for-OT%20security%20architects%20%7C%20MSS%20SOC-brightgreen)
![Aligned](https://img.shields.io/badge/aligned-Purdue%20%7C%20IEC%2062443-lightgrey)
![License](https://img.shields.io/badge/license-MIT-green)

---

## The deployment-readiness lifecycle

Deploying OT monitoring is not "install the sensor." In an OT/ICS plant the wrong move can disrupt a live process, and a sensor with no context produces noise, not detections. The path is:

```
  1. GATHER CONTEXT            2. DESIGN                3. ONBOARD SOURCES          4. DETECT
  ────────────────            ─────────                ──────────────────          ──────
  request & review the    →   HLD/LLD, sensor      →   bring log sources in    →   build detections
  pre-deployment docs         placement, safe          by tier (feasibility,       on the onboarded
  (architecture, assets,      collection design        noise, value)               telemetry
  comms, P&ID, risk)
        │                          │                        │                         │
   pre-deployment/           pre-deployment/          log-onboarding/            (other detection
   document-package          priority-request-list    onboarding-guide            libraries)
```

This repo covers stages 1 and 3 — the two most commonly skipped, and the two that most determine whether the deployment is safe and the detections are any good.

## What's here

```
ot-monitoring-deployment/
├── pre-deployment/                     ← what to gather BEFORE you deploy
│   ├── document-package.md             ← the full document package + who uses each (RACI)
│   ├── priority-request-list.md        ← the docs to request FIRST + what each tells you
│   └── document-request-checklist.md   ← a tracker to run the document request
└── log-onboarding/                     ← what to turn on AFTER, and in what order
    ├── onboarding-guide.md             ← tiered log-source prioritization (the reference)
    └── log-source-matrix.csv           ← machine-readable source matrix
```

## Part 1 — Pre-deployment document package
Before deploying Nozomi/Sentinel/any OT monitoring, an architect gathers the technical, operational, and security context needed to place sensors safely and build effective detections. [`pre-deployment/document-package.md`](pre-deployment/document-package.md) lists the full package (with who — Security / SOC / Engineers — relies on each and *why it matters for monitoring*), and [`pre-deployment/priority-request-list.md`](pre-deployment/priority-request-list.md) gives the request-first order with what each document tells you. Run the request with [`pre-deployment/document-request-checklist.md`](pre-deployment/document-request-checklist.md).

## Part 2 — Log source onboarding
Once you're deploying, you can't ingest everything on day one. [`log-onboarding/onboarding-guide.md`](log-onboarding/onboarding-guide.md) sequences OT log sources into four tiers by **collection ease, noise, source count, and security value**, so a Cyber Defense / MSS team onboards in the order that yields the most detection value per unit of effort. The same data is in [`log-onboarding/log-source-matrix.csv`](log-onboarding/log-source-matrix.csv) for tooling.

## How the two halves connect
The pre-deployment documents *are* the inputs to onboarding and detection:

| Pre-deployment document | Feeds |
|-------------------------|-------|
| Network Architecture / Purdue diagram | sensor & SPAN/TAP placement; Tier-1 firewall/switch onboarding; zone-crossing detections |
| Asset Inventory | scoping sensors/licenses; new-asset detections; which Tier-2/3 controllers exist |
| Communication Matrix | the "allowed pair" baseline for protocol detections; firewall-rule validation |
| Historian Tag List | process/physics (baseline & deviation) detections |
| Risk Assessment / Cause & Effect | detection priority; safety-critical (SIS) handling |
| HLD / LLD | the deployment build itself |

## Who this is for
OT security architects and OT SOC / MSS engineers scoping or running a monitoring deployment — the checklist you'd use when asked to *"review this plant before we deploy."*

## Author
Prepared for OT/ICS detection engineering — MSS Cyber Defense.

## License
MIT — see [`LICENSE`](LICENSE).

> Adapt document names, tiers, and thresholds to your site and toolset. Nothing here should be actioned against a live process without engineering and operations sign-off.
