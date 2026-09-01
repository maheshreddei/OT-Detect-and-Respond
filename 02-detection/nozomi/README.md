# Nozomi Assertion Queries

N2QL queries that turn the [detection catalog](../../source-libraries/protocol-ndr-catalog.csv) into **Nozomi Guardian/CMC assertions** — so the detections in this repo run natively in a Nozomi deployment, not just in a SIEM.

Built in the style of Nozomi's *20 Queries* white paper, and mapped back to the protocol pages and detection IDs.

## Files
- [`assertion-queries.md`](assertion-queries.md) — the queries, grouped (Access · Segmentation · Protocol Write/Command · Baseline · Reporting/IR), each with its N2QL, the assertion trigger, and the detection IDs it maps to.
- [`n2ql-reference.md`](n2ql-reference.md) — N2QL syntax/idioms distilled from the white paper, so the queries are maintainable.
- [`queries-catalog.csv`](queries-catalog.csv) — machine-readable index (id, category, protocol, detection, maps_to, execute_on, severity, assert condition).

## The idea
The protocol guide's core model is *reads are recon, writes are impact, and the protocol enforces no authorization.* These queries encode that missing authorization: each returns rows **only for the disallowed case** (a write from a non-master, a control protocol crossing a zone, remote access into OT), so the assertion rule is simply **"non-empty ⇒ alert."**

## Deploy order
1. Run **Q-BASE-01** to confirm the exact **protocol tokens** in your environment.
2. Run **Q-BASE-02** per protocol to confirm the **function/service code numbers** to assert on.
3. Fill in the `<PLACEHOLDERS>` (zones, master/EWS IPs, subnets).
4. Stand up the **Protocol Write/Command** assertions first (highest value), then Segmentation and Access.
5. Keep the Baseline/Reporting queries as scheduled hunts, not assertions.

## Caveats
- Protocol tokens and function-code numbers are environment/version dependent — Modbus is fully worked; the others give the pattern plus a native-signature fallback, to be finalized with `Q-BASE-02`.
- Encrypted protocols (OPC UA SignAndEncrypt, MQTT over TLS) hide payload from DPI — those queries catch the *connection*; pair with server/broker logs for payload-level detection (see [`docs/protocol-ndr-log-sources.md`](../../docs/protocol-ndr-log-sources.md)).
- Validate every query with **Run** before saving it as an assertion.
