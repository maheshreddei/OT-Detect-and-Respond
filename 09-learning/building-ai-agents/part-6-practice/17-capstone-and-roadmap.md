# Chapter 17 — Capstone & Roadmap

> Part VI · Practice. This closing chapter ties the guide together with an end-to-end build you can actually do, the patterns and anti-patterns to remember, and a learning roadmap for going further.

## 17.1 Capstone: a support agent, end to end

Build a **customer-support agent** that demonstrates every part of the guide. It's ambitious enough to be real, small enough to finish.

**The task.** Answer customer questions about orders and policies, and (with approval) issue refunds.

**Design it through the guide's lenses:**

1. **Is an agent the right shape? (Ch 01)** — Yes: the steps depend on the question (look up an order, search policy, maybe refund). A fixed workflow can't cover the variety. But keep it a *single* agent (Ch 11) — one coherent job.
2. **Anatomy (Ch 02) & loop (Ch 03)** — A ReAct agent: think → act → observe, with step and budget limits.
3. **Model layer (Ch 04)** — A capable model with tool use; a crisp system prompt defining role, tool policy, and the stopping condition; route trivial formatting to a cheaper model if needed.
4. **Tools (Ch 05)** — `get_order_status` (read), `search_docs` (read/RAG), `issue_refund` (write). Focused, well-described, constrained inputs, clean errors.
5. **Memory (Ch 06)** — Working context for the conversation; optionally remember the customer's preferences across sessions.
6. **RAG (Ch 07)** — `search_docs` retrieves policy chunks; the agent answers grounded, with citations, and says "I don't know" when retrieval is empty.
7. **Build it (Ch 08)** — Start from the from-scratch loop to understand it; then move to a framework (Ch 09) for persistence, streaming, and tracing.
8. **Patterns (Ch 10)** — Not needed as a full workflow here, but the refund flow uses **human-in-the-loop** approval.
9. **Evaluation (Ch 13)** — An eval set: order lookups, policy questions (grounded?), refund requests (does it seek approval?), edge cases (unknown order), and safety cases (prompt injection in a document).
10. **Observability (Ch 14)** — Trace every run; promote failures into the eval set.
11. **Guardrails (Ch 15)** — Treat retrieved docs as untrusted (injection defense); **require human approval for `issue_refund`**; cap the refund amount; step/budget limits.
12. **Deployment (Ch 16)** — Async serving with streaming, durable state, model routing, prompt caching, the pre-launch checklist, and iteration in production.

Ship it behind the checklist, start with refunds requiring approval, and loosen only as evaluation earns trust. This one project exercises the entire guide.

## 17.2 Patterns to remember

- **Simplest thing that works** — prompt < workflow < agent; add autonomy only when needed.
- **The loop is everything** — master think→act→observe; everything else refines it.
- **Tools are prompts** — description quality drives tool-use quality.
- **Curate the context** — the window is a budget, not a bucket.
- **Ground with retrieval** — cite sources; say "I don't know."
- **Start with one agent** — add agents only for nameable role separation.
- **Evaluate before shipping** — an un-evaluated agent is a hypothesis.
- **Trace everything** — you can't fix what you can't see.
- **Guardrail the actions** — human approval for high-stakes; least privilege; sandbox code.
- **Iterate in production** — trace → eval → fix → ship.

## 17.3 Anti-patterns to avoid

- **Reaching for an agent when a workflow would do** — the most common and expensive mistake.
- **Going multi-agent to seem advanced** — it multiplies a weak foundation's problems.
- **No evaluation** — shipping on vibes; can't tell better from worse.
- **No observability** — debugging blind.
- **No guardrails on write actions** — one bad step from an incident.
- **Overstuffed context** — pay more, work worse (context rot).
- **Too many tools** — dilutes tool selection accuracy.
- **Skipping the from-scratch loop** — treating frameworks as magic and getting stuck when they break.
- **Chasing framework hype** — porting on trends instead of fit.

## 17.4 A learning roadmap

**Now (you've built one agent):**
- Do the capstone end to end; instrument and evaluate it.
- Learn one framework deeply (LangGraph or a vendor SDK) rather than sampling many.

**Next (depth):**
- **RAG quality** — chunking, hybrid search, re-ranking, evaluation of retrieval.
- **Evaluation** — LLM-as-judge design, trajectory eval, building datasets from production.
- **MCP** — build and consume MCP servers; make your tools reusable.
- **Cost/performance** — model routing, caching, latency profiling from traces.

**Later (frontier):**
- **Multi-agent** orchestration where genuinely warranted; **A2A** for cross-boundary systems.
- **Advanced memory** — episodic/procedural memory, long-horizon agents.
- **Safety** — prompt-injection defense, sandboxing, autonomy governance for consequential agents.

**Habits that compound:**
- Keep a **traced, evaluated** project you iterate on.
- Read the primary sources (framework docs, model-provider agent guides) since the field moves monthly.
- When something breaks, **debug at the loop level** — the fundamentals in this guide don't change even as tools do.

## 17.5 The closing idea

Agents look magical, but they're an engineering discipline: **a model in a loop with tools, memory, and guardrails, measured and iterated.** The teams that ship reliable agents aren't the ones with the fanciest architecture — they're the ones who kept it as simple as the problem allowed, evaluated relentlessly, traced everything, and guarded the actions. Build the loop, measure it, constrain it, improve it. That's the whole craft.

## Chapter summary
- The **capstone support agent** exercises every chapter: single ReAct agent, three tools (two read, one gated write), RAG with citations, eval set, tracing, human-approved refunds, production checklist.
- Remember the **patterns** (simplest-thing-that-works, the loop, tools-as-prompts, curate context, ground, one-agent-first, evaluate, trace, guardrail, iterate).
- Avoid the **anti-patterns** (agent-when-workflow, needless multi-agent, no eval/observability/guardrails, overstuffed context, too many tools, skipping from-scratch, hype-chasing).
- Follow the **roadmap** (deepen one framework, then RAG/eval/MCP/cost, then multi-agent/A2A/safety) with **traced, evaluated** practice.

## Cross-references
- Every chapter — this is the synthesis. Start the capstone with Chapter 08 and instrument it with Chapters 13–16.
