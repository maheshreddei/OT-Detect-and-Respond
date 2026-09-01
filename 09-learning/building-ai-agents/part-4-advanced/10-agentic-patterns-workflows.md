# Chapter 10 — Agentic Patterns & Workflows

> Part IV · Advanced. Before you reach for a full autonomous agent, know the **workflow patterns** — structured ways to combine LLM calls that are more reliable and cheaper than a free-running loop. The best systems mix workflows and agents deliberately.

## 10.1 Workflows vs agents, revisited

Recall Chapter 01: a **workflow** has steps *you* define; an **agent** decides steps at runtime. Workflows are more predictable, testable, and cheaper; agents are more flexible. The five patterns below are the workflow building blocks. Master them and you'll often find a workflow solves the problem an "agent" was overkill for — and when you do need an agent, these patterns become its internal structure.

## 10.2 Pattern 1 — Prompt chaining

Break a task into a **fixed sequence** of LLM calls, each building on the last: extract → transform → format; or draft → critique → revise. Use when the task decomposes cleanly into ordered steps. It trades a little latency for a lot of reliability, because each step is simple and checkable. Add a **gate** between steps (a programmatic check) to catch failures early.

```
  input → [LLM: extract] → [check] → [LLM: summarize] → [LLM: format] → output
```

## 10.3 Pattern 2 — Routing

Classify the input, then send it to a **specialized** handler. A router LLM (or classifier) picks one of N paths; each path is optimized for its case. Use when inputs fall into distinct categories that benefit from different handling (billing vs technical vs sales support). Routing keeps each handler simple and lets you use cheaper models for easy categories.

```
  input → [router] → billing_handler | tech_handler | sales_handler → output
```

## 10.4 Pattern 3 — Parallelization

Run multiple LLM calls **at once** and aggregate. Two flavors:
- **Sectioning** — split a task into independent subtasks run in parallel (analyze ten documents simultaneously).
- **Voting** — run the same task multiple times and take a consensus/best (improves reliability on hard judgments).

Use when subtasks are independent (speed) or when multiple attempts improve confidence (quality). Aggregation logic (merge, vote, pick-best) is yours to define.

## 10.5 Pattern 4 — Orchestrator-workers

An **orchestrator** LLM dynamically breaks a task into subtasks, delegates each to a **worker** LLM, and synthesizes the results. Unlike fixed parallelization, the orchestrator decides the subtasks *at runtime* based on the input. Use for complex tasks whose decomposition can't be known in advance (research across many sources, multi-file code changes). This is the boundary where workflows start becoming agentic — the orchestrator has autonomy over decomposition.

```
  input → [orchestrator: plan subtasks] → [worker]…[worker] → [orchestrator: synthesize] → output
```

## 10.6 Pattern 5 — Evaluator-optimizer

One LLM **generates**, another **evaluates** and gives feedback, and the loop repeats until the evaluator is satisfied. Use when you have a clear quality bar and iterative refinement helps (writing that must meet criteria, code that must pass checks, translation that must preserve nuance). This is the **reflection** pattern (Chapter 03) formalized into two roles, and it can lift quality substantially when "good" is checkable.

```
  input → [generator] → [evaluator] → good? ── no ──▶ (feedback) ──┐
                                        │ yes                      │
                                        ▼                          │
                                      output    ◀──── generator ◀──┘
```

## 10.7 Choosing a pattern

- Fixed, ordered steps → **prompt chaining.**
- Distinct input categories → **routing.**
- Independent subtasks or need for consensus → **parallelization.**
- Unknown decomposition → **orchestrator-workers.**
- Iterative quality improvement → **evaluator-optimizer.**
- Genuinely open-ended, tool-driven, unpredictable path → a **full agent** (Chapter 03).

The guiding principle from the field: **find the simplest pattern that solves your problem, and only add autonomy/complexity when simpler patterns provably fall short.** Complexity is a cost you pay in latency, dollars, and debuggability.

## Chapter summary
- **Workflows** (you define steps) are more reliable/cheaper than **agents** (model defines steps); prefer them when they suffice.
- Five patterns: **prompt chaining** (fixed sequence), **routing** (classify→specialize), **parallelization** (sectioning/voting), **orchestrator-workers** (runtime decomposition), **evaluator-optimizer** (generate→critique→revise).
- Match the pattern to the task shape; escalate to a full agent only when open-ended and tool-driven.
- **Simplest thing that works** — add autonomy only when simpler patterns fail.

## Cross-references
- Chapter 01 (workflow vs agent), Chapter 03 (reflection = evaluator-optimizer), Chapter 11 (multi-agent orchestration).
