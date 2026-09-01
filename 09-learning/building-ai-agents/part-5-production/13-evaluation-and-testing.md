# Chapter 13 — Evaluation & Testing

> Part V · Production. The line between a demo and a product is evaluation. Agents are non-deterministic and act in the world, so you cannot ship them on vibes — you need a systematic way to measure whether they work and to catch regressions. This is the most-skipped and most-important production discipline.

## 13.1 Why agent eval is hard (and essential)

Agents are **non-deterministic** (the same input can yield different paths), **multi-step** (many places to go wrong), and **open-ended** (often no single correct answer). Traditional unit tests don't fit. Yet without evaluation you can't answer the questions that matter: *Is the new prompt better or worse? Did that change break anything? Is it good enough to ship?* Evaluation is what turns agent development from trial-and-error into engineering.

## 13.2 What to evaluate

Evaluate at three levels:

- **Final output quality** — is the answer correct, complete, well-formed, safe? (outcome)
- **Trajectory** — did the agent take a sensible path: right tools, right order, no wasted or wrong steps? (process)
- **Operational** — cost, latency, and step count per task. (efficiency)

A good agent is right, *and* gets there efficiently, *and* stays within budget. Measure all three.

## 13.3 Building an eval set

Start with a **dataset of representative tasks** with known-good expectations:

- Collect real or realistic inputs (bias toward the hard and the common).
- For each, define **success criteria** — an exact answer, a rubric, required tool calls, or constraints to satisfy.
- Include **edge cases and failure cases** (ambiguous inputs, missing data, adversarial prompts).
- Grow the set from **production failures** — every real miss becomes a permanent test.

Even 20–50 well-chosen cases beat none; you can expand over time.

## 13.4 Scoring methods

- **Exact / programmatic** — for checkable outputs (the number, the JSON shape, the required tool was called). Cheap and reliable; use wherever possible.
- **LLM-as-judge** — a model scores the output against a rubric ("is this answer correct and grounded? 1–5"). Scales to open-ended tasks; validate the judge against human labels and keep rubrics specific.
- **Human review** — the gold standard for nuanced quality; expensive, so reserve for calibration and high-stakes cases.
- **Trajectory checks** — assert on the *path*: did it call `search_docs` before answering a policy question? did it avoid the destructive tool without approval?

Combine: programmatic where you can, LLM-as-judge for quality, human for calibration.

## 13.5 The eval loop

Wire evaluation into development like a test suite:

```
  change (prompt/tool/model) → run eval set → compare scores to baseline
        → better? keep. worse/regression? revert or fix. → repeat
```

Run evals **before shipping any change** and on a schedule against production samples. This is exactly the assurance mindset — a rule/agent that hasn't been evaluated is a hypothesis, not a product. Track scores over time so you can *see* quality moving.

## 13.6 A minimal eval harness (illustrative)

```python
cases = [
    {"input": "What is 15% of 2400?", "check": lambda out: "360" in out},
    {"input": "Refund policy?", "check": lambda out: "30 days" in out.lower()},
]

def evaluate(agent):
    passed = 0
    for c in cases:
        out = agent(c["input"])
        ok = c["check"](out)
        passed += ok
        print(f"{'PASS' if ok else 'FAIL'}: {c['input']}")
    print(f"score: {passed}/{len(cases)}")
```

Start this simple; add LLM-as-judge scoring and trajectory assertions as the agent grows.

## Chapter summary
- Agents are non-deterministic, multi-step, and open-ended — you **cannot ship on vibes**; evaluation makes it engineering.
- Evaluate **output quality, trajectory (the path), and operational cost/latency.**
- Build an **eval set** of representative + edge + past-failure cases with explicit success criteria.
- Score with **programmatic checks (preferred), LLM-as-judge (scaled), human review (calibration), and trajectory checks.**
- Run evals **on every change and on production samples**; track scores over time.

## Cross-references
- Chapter 14 (observability) supplies the production traces you evaluate; Chapter 03 (stopping/quality) and Chapter 10 (evaluator-optimizer) relate.
