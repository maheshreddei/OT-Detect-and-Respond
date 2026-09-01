# Chapter 02 — ICS Components: Field Devices, PLC, RTU

> Part I · Foundations. To defend a plant you must first understand the machinery of control — how a physical process is measured, decided upon, and acted on. This chapter builds that picture from the ground up, then shows, for each component, how it betrays an attacker.

## 2.1 The universal control loop

Every industrial process, from a brewery to a power grid, is a variation on one loop:

```
        ┌───────────────────────────────────────────┐
        │                                           ▼
   [ PROCESS ] ──▶ [ SENSOR ] ──▶ [ CONTROLLER ] ──▶ [ ACTUATOR ] ──┐
        ▲            measures        decides          moves         │
        └──────────────────────── the physical world ───────────────┘
```

1. A **sensor** measures a physical quantity (temperature, pressure, flow, level, position, speed).
2. A **controller** compares that measurement to a desired value (a **setpoint**) and computes an action.
3. An **actuator** carries out the action (opens a valve, speeds a motor, closes a breaker).
4. The **process** responds, the sensor measures again, and the loop repeats — continuously, deterministically, forever.

This is a **closed feedback loop**. The most common control algorithm is **PID** (Proportional-Integral-Derivative), which smoothly drives the measured value toward the setpoint without overshooting. You do not need to implement PID, but you must understand its implication: the controller is *always* acting to hold the process at its setpoint. If an attacker changes the setpoint, the controller will faithfully and automatically drive the real process to the new, possibly dangerous, value — using entirely legitimate control action. That is what makes setpoint manipulation so dangerous and so hard to see.

## 2.2 Field devices: sensors, actuators, and signals

**Level 0** of the plant — the physical edge — is made of field devices.

- **Sensors / transmitters** convert a physical quantity into an electrical signal. A transmitter is a sensor packaged with electronics that outputs a standard signal.
- **Actuators / final elements** convert a signal back into physical action: control valves, motor drives (VFDs), solenoids, breakers, pumps.

Signals come in a few standard forms you should recognize:

| Signal | Type | Typical use |
|--------|------|-------------|
| 4–20 mA | Analog current | The workhorse of process instrumentation; robust over distance |
| 0–10 V | Analog voltage | Shorter-range analog I/O |
| Digital / discrete | On/off | Limit switches, relays, run/stop |
| HART | Digital over 4–20 mA | Smart instruments carrying diagnostics on the analog wire |
| Fieldbus (PROFIBUS, Foundation Fieldbus) | Digital bus | Multi-drop instrument networks |

A subtle but important detail: **4–20 mA never goes to zero in normal operation** (the "live zero" starts at 4 mA), so a reading of 0 mA means a broken wire, not a low value. This is an early example of *fail-detectable* design — the same philosophy that underlies de-energize-to-trip safety systems in Chapter 04.

**Security note on Level 0:** field devices are Purdue Level 0 and are **never targeted for direct log collection**. There are far too many of them, they produce no useful logs, and their state is already visible indirectly through the controller and the historian. Attempting to instrument them adds cost for no detection value. You watch Level 0 *through* Level 1.

## 2.3 The PLC in depth

The **Programmable Logic Controller (PLC)** is the heart of discrete and hybrid control. It is a ruggedized industrial computer that runs a control program in a tight, repeating cycle.

### The scan cycle
A PLC executes a **scan cycle**, typically in single-digit milliseconds:

```
   ┌──▶ 1. Read all inputs  (copy physical input states into memory)
   │    2. Solve the logic  (execute the control program once, top to bottom)
   │    3. Write all outputs (copy computed output states to the physical outputs)
   └──── 4. Housekeeping/comms  (diagnostics, network) ──┘  then repeat
```

Because inputs are sampled and outputs are written once per scan, the PLC's behavior is deterministic and predictable — the foundation of reliable control.

### Programming languages
PLCs are programmed in the languages defined by **IEC 61131-3**:

- **Ladder Logic (LD)** — looks like relay wiring diagrams; the most common, readable by electricians.
- **Function Block Diagram (FBD)** — blocks wired together; good for process/analog logic.
- **Structured Text (ST)** — Pascal-like text; for complex algorithms.
- **Instruction List (IL)** and **Sequential Function Chart (SFC)** round out the set.

An engineer writes this logic in a vendor tool on an **engineering workstation (EWS)** and **downloads** it to the PLC.

### The security-relevant states and operations
For a defender, a handful of PLC facts matter enormously:

- **Operating mode / key-switch.** PLCs have a mode: **RUN** (executing logic normally), **PROGRAM/REMOTE** (accepting logic changes), and often **STOP**. Changing out of RUN is what enables online logic modification. A key-switch physically enforces this on many controllers. *A mode change to PROGRAM is a top-signal event.*
- **Program download / upload.** Downloading replaces the running logic; uploading reads it out. An unexpected **program download** is the archetypal high-consequence attack (this is what Stuxnet did). An **upload** may be reconnaissance or logic theft.
- **Forcing.** Engineers can "force" an input or output to a fixed value for testing, overriding the real signal. A **force left in place** (or set maliciously) disconnects the logic from reality — a favored, quiet manipulation.
- **Online edits.** Some platforms allow changing logic while running. The **online-edit history** is a forensic goldmine.
- **Firmware.** Replacing firmware can implant persistent, stealthy capability below the logic layer.

Vendors and families you will meet: **Siemens SIMATIC S7 (S7-300/400/1200/1500)**, **Rockwell/Allen-Bradley ControlLogix/CompactLogix (GuardLogix for safety)**, **Schneider Modicon**, **Mitsubishi**, **Omron**, **Beckhoff**. Each has its own engineering tool (TIA Portal, Studio 5000, EcoStruxure) and, often, its own protocol dialect.

## 2.4 The RTU

The **Remote Terminal Unit (RTU)** is a close cousin of the PLC, optimized for **remote, distributed sites** and **telemetry**. Where a PLC sits in a factory cell, an RTU sits at a pipeline valve station, a remote substation, or a distant pump house — often communicating back to a central SCADA master over long distances, frequently over **serial links or cellular/radio**, using protocols built for telemetry (**DNP3**, **IEC 60870-5-101/104**).

RTUs share the PLC's security-relevant traits (modes, configuration, remote writes) but add two wrinkles: they are **geographically dispersed** (physical access is a real risk at unmanned sites) and often **bandwidth-constrained and serial**, which shapes how you monitor them (polling-based monitoring, boundary/gateway logging rather than a sensor at every remote site).

The line between PLC, RTU, and **PAC** (Programmable Automation Controller — a higher-capability controller blending PLC and PC features) is blurry and vendor-marketing-driven. For defense, treat them the same: **controllers that execute logic and accept remote commands, with limited native logging, best watched passively over the network.**

## 2.5 How each component betrays an attacker

The reason to learn this machinery is that each component leaves evidence when abused. Summarized:

| Component | Malicious action | What the defender observes |
|-----------|------------------|----------------------------|
| Sensor/transmitter | Spoofed/frozen value | Historian value frozen or diverging from reality; command-vs-feedback mismatch |
| PLC | Program download | Program-transfer on the wire; running logic differs from baseline |
| PLC | Mode change | Key-switch / operating-mode change to PROGRAM/REMOTE |
| PLC | Force / online edit | Force table populated; online-edit history entries |
| PLC/RTU | Unauthorized write | Write function code from a source not on the command allow-list |
| Controller | Firmware change | Firmware version delta; firmware-update mode entered |

Notice the recurring theme: you rarely see a "hacker signature." You see a **legitimate operation performed by the wrong source, at the wrong time, or with the wrong value.** Learning the machinery is how you tell the difference.

## Chapter summary

- Every process is a feedback loop: sensor → controller → actuator → process → sensor. The controller always drives toward the setpoint, which is why setpoint manipulation is so dangerous.
- Field devices (Level 0) are watched *through* the controller, never instrumented directly.
- The PLC runs a deterministic scan cycle; its security-relevant surface is **mode/key-switch, program up/download, forcing, online edits, and firmware.**
- The RTU is a PLC for remote/telemetry sites, adding physical-access and serial-monitoring considerations.
- Abuse shows up as **legitimate operations from the wrong source, time, or value** — which is why knowing "normal" is everything.

## Cross-references
- Chapter 06 (protocols) shows *how* these operations travel on the wire.
- Chapter 17 (process indicators) develops the sensor-spoofing and command-vs-feedback detections.
- Chapter 20 (detection engineering) turns "unauthorized write / program download / mode change" into rules.
- Companion repositories: `ot-protocol-defense`, `ot-historian-detection`.
