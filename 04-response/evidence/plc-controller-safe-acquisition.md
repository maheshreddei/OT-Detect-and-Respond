# Evidence: PLC / Controller (Safe Acquisition)

The highest-risk, highest-value host-side evidence. Proving whether a controller's **logic, configuration, or firmware** was modified is the Stuxnet/TRITON question. But the controller may be actively running the process, and the wrong action here can trip the plant or destroy volatile state.

> **Golden rule: read-only, engineer-led, operations-authorized, capture-or-lose. Never download, write, or reset.** Every action in this guide is performed or directly supervised by the controls engineer with operations' authorization. The SOC advises; it does not operate controllers.

## Prove it passively first
Before touching the controller, try to prove the change from evidence you already have:
- **Network capture** of a program download/upload (Zeek `s7comm.log` download function, Nozomi program-transfer alert, pcap of the transfer) proves a change *happened*, when, and from where — with **zero controller risk**. See [`network-and-ot-protocols.md`](network-and-ot-protocols.md).
- **EWS artifacts** (engineering-tool logs, project-file modification) show the change was *prepared*. See [`windows-ews-hmi-historian-host.md`](windows-ews-hmi-historian-host.md).
If these establish the change, you may not need to touch the controller at all — and you've preserved its running state.

## Compare-to-golden-baseline (the core method)
The definitive proof of logic modification is a **read-only upload of the running program compared against the golden baseline** captured in the Prepare phase.
1. Engineer performs a **read-only/upload** of the current controller program using the vendor engineering tool.
2. **Offline compare** (the tool's compare function) against the known-good baseline project.
3. Any difference in logic, blocks, tags, or config is the proof — export the compare report, hash it.
> This is why the Prepare phase matters: **without a golden baseline you cannot prove a change**, only describe the current state. Baseline every critical controller in advance.

## Other controller evidence (read-only)
| Evidence | How | Proves |
|----------|-----|--------|
| Diagnostic buffer / controller event log | Engineering-tool read | Mode changes (RUN↔STOP↔PROGRAM), download events, faults, timestamps |
| Firmware version | Read; compare to inventory/baseline | Firmware replaced or downgraded |
| Key-switch / mode position | Read / SER record | Whether protection was in PROGRAM/REMOTE when the change occurred |
| Force tables / forced I/O | Engineering-tool read | Overridden I/O masking real conditions |
| Online vs offline logic diff | Tool compare | Running logic differs from the last saved project |

## Volatile controller state — capture-or-lose
Live logic in controller memory, force tables, and the diagnostic buffer are volatile — a power cycle or reset destroys them. This creates tension with the "don't touch it" rule, resolved by:
- Capturing this state **read-only** while the controller runs, engineer-led, **before** any containment that might reset it.
- If containment requires a reset/shutdown, **capture first** (read-only upload + diagnostic buffer export), then let operations execute the controlled action.

## Hard don'ts
- ✗ Do **not** download/write logic to "fix" or "clean" the controller during investigation.
- ✗ Do **not** power-cycle or reset to "clear" it — you destroy evidence and may trip the process.
- ✗ Do **not** change the key-switch or mode.
- ✗ Do **not** connect an untrusted laptop to the controller — use a clean, dedicated engineering machine.

## SIS controllers — extra caution
For safety controllers, add the plant **safety authority** to every decision and treat the SIS as sacrosanct. Capture SIS logic/config read-only, compare to baseline, and pull SIS diagnostic/event logs and safety-PV/trip records — but take **no action** that could affect a safety function. Any SIS involvement is minimum SEV-1.

## What controller evidence proves
- **Unauthorized logic/config/firmware modification** (compare-to-baseline) — or clears the controller of it.
- **When and how** the change was applied (diagnostic buffer + network transfer).
- Whether **protection was bypassed** (key-switch/mode, forces).
Pair with network evidence (the transfer) and host/identity evidence (the operator) for a complete chain.
