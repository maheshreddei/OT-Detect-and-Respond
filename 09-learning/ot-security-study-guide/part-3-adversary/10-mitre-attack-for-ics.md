# Chapter 10 — MITRE ATT&CK for ICS

> Part III · The Adversary. ATT&CK for ICS is the shared language for describing what industrial adversaries do. This chapter teaches you to use it as a coverage map and a hunting index, not just a poster.

## 10.1 Why a separate matrix

MITRE maintains ATT&CK for **Enterprise** (IT) and a distinct matrix for **ICS**. They are complementary: a real OT intrusion crosses both. The IT stages (phishing, credential theft, lateral movement to the OT boundary) live in Enterprise ATT&CK; the plant-floor actions (manipulating a controller, defeating a safety function, causing a physical effect) live in ATT&CK for ICS. A complete picture maps an intrusion across the two matrices.

## 10.2 The ICS tactics

Tactics are the adversary's *goals* — the "why" of a step. ATT&CK for ICS tactics include, roughly in campaign order:

- **Initial Access** — getting into the OT/control network (often via the IT pivot, remote services, or removable media).
- **Execution** — running code or commands on ICS assets.
- **Persistence** — staying (e.g. modifying a program or firmware).
- **Privilege Escalation / Evasion** — gaining rights and avoiding detection.
- **Discovery** — enumerating assets, roles, and the control logic.
- **Lateral Movement** — moving between OT systems.
- **Collection** — gathering process data and understanding the process.
- **Command and Control** — maintaining a channel.
- **Inhibit Response Function** — defeating protective/safety functions (this is where TRITON lives).
- **Impair Process Control** — manipulating the process (parameter changes, unauthorized commands).
- **Impact** — the physical consequence (loss/manipulation of control, view, safety, availability).

The three tactics that make ICS distinct — **Inhibit Response Function, Impair Process Control, Impact** — are the ones with no IT equivalent, because they describe effects on the physical world.

## 10.3 Techniques worth memorizing

A working defender should know these ICS technique IDs on sight, because they map directly to detections:

| Technique | ID | Why it matters |
|-----------|----|----------------|
| Modify Parameter | T0836 | Setpoint/parameter change — the quiet manipulation |
| Unauthorized Command Message | T0855 | A command from a source that shouldn't send it |
| Program Download | T0843 | Replacing controller logic (Stuxnet-class) |
| Change Operating Mode | T0858 | Key-switch/mode to PROGRAM (enables logic change) |
| Manipulation of Control | T0831 | Driving the process to an attacker's ends |
| Manipulation of View | T0832 | Falsifying what the operator sees |
| Loss of Safety | T0880 | Defeating the safety function |
| Loss/Denial of Protection | T0837 | Removing a protective function |
| Denial of Control / View | T0813/T0815 | Blinding or disabling operators |

## 10.4 ATT&CK as a coverage map

The most valuable use of ATT&CK is **measuring coverage**. For each technique you claim to defend, ask: do I have the **data** to see it, and a **detection** that fires on it? Export the answers as an **ATT&CK Navigator layer**, colored by state (covered / partial / gap). This single artifact turns "we watch for bad things" into a defensible, gap-driven program — and it's exactly what Threat Detection Assurance (companion) validates.

## 10.5 ATT&CK as a hunting index

ATT&CK is also a hunt backlog. Intelligence-driven hunts (Chapter 16) start from "a group we care about uses techniques X, Y, Z — do we have coverage, and can I find evidence?" Anchoring every hunt and every detection to a technique ID gives you a common vocabulary across intel, hunting, detection, and reporting.

## Chapter summary
- ATT&CK for ICS is a **separate, complementary matrix**; real intrusions span it and Enterprise ATT&CK.
- The ICS-unique tactics are **Inhibit Response Function, Impair Process Control, and Impact** — physical-world effects.
- Memorize the high-value techniques (T0836/T0855/T0843/T0858/T0831/T0832/T0880/T0837).
- Use ATT&CK as a **coverage map** (Navigator layer) and a **hunting index**; anchor every hunt and detection to a technique ID.

## Cross-references
- Chapter 11 (TTPs/kill chain) and Chapter 16 (methodology) build on this vocabulary.
- Companion: every detection repo is ATT&CK-mapped; `threat-detection-assurance` measures the coverage.
