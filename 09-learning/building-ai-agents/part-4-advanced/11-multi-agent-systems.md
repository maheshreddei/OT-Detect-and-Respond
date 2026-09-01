# Chapter 11 — Multi-Agent Systems

> Part IV · Advanced. Sometimes one agent isn't the right shape and you want several specialized agents collaborating. This chapter covers how multi-agent systems work, the orchestration styles, and — critically — when multiple agents help and when they just add cost and chaos.

## 11.1 What a multi-agent system is

A **multi-agent system** is several agents, each with its own instructions, tools, and often its own model, working together on a task. Each agent typically has a **specialized role** (researcher, writer, critic; or triage, billing, technical). They coordinate by passing work and results between them.

The appeal: **separation of concerns** (each agent is simpler and focused), **specialization** (different tools/prompts/models per role), and **parallelism** (agents work concurrently). The cost: **coordination overhead**, more failure modes, higher token spend, and harder debugging.

## 11.2 Orchestration styles

Different frameworks coordinate agents differently (Chapter 09):

- **Handoffs (OpenAI Agents SDK).** An agent explicitly **transfers control** to another, passing context. Good for routing/triage: a front-line agent hands off to a specialist.
- **Graph (LangGraph).** Agents are **nodes** in a directed graph; edges (some conditional) control flow and shared state. Best for complex, stateful control with branching and error handling.
- **Crews / roles (CrewAI).** A **team of role-playing agents** with tasks; work passes sequentially or hierarchically. Fastest to a working multi-agent prototype.
- **Conversation (AutoGen-style).** Agents **converse** in a group chat until the task is done. Natural for open-ended collaboration/research.
- **Hierarchical / supervisor.** A **supervisor** agent delegates to and coordinates subordinate agents (an orchestrator-workers pattern with full agents as workers).

## 11.3 Common topologies

- **Supervisor-workers** — one coordinator delegates to specialists and synthesizes. The most common and controllable topology.
- **Pipeline** — agents in sequence, each transforming the work (research → draft → edit).
- **Peer collaboration** — agents converse as equals toward a shared goal.
- **Router → specialists** — a triage agent hands off to the right specialist.

## 11.4 When multi-agent helps

Multiple agents earn their complexity when:
- The task has **genuinely distinct sub-roles** that benefit from different tools/prompts/models.
- **Parallelism** across independent subtasks meaningfully speeds things up.
- A single agent's **context would be overloaded** doing everything, and splitting keeps each context focused.
- You want an **independent critic/evaluator** separate from the generator (evaluator-optimizer with real separation).

## 11.5 When it hurts (start with one)

Multi-agent is frequently **over-used**. Prefer a single agent when:
- The task is really one coherent job — splitting it adds coordination cost for no benefit.
- **Latency/cost** matters — every agent adds calls and tokens.
- **Reliability** matters — more agents means more places to fail and harder debugging; errors compound across handoffs.
- You haven't yet made a **single** agent work well — multi-agent won't fix a weak single-agent foundation; it multiplies its problems.

The mature default: **start with one well-designed agent.** Add agents only when you can name the specific role separation or parallelism that a second agent provides. "Multi-agent" is not a maturity level to aspire to; it's a tool for specific shapes of problem.

## 11.6 Making multi-agent reliable

If you do go multi-agent:
- **Give each agent a crisp, narrow role** and only the tools it needs.
- **Define the coordination explicitly** (who hands off to whom, on what condition, with what context).
- **Manage shared context** — decide what each agent sees; don't blindly pass everything (cost + confusion).
- **Bound the interaction** — cap total steps/turns across the system, not just per agent, to prevent runaway back-and-forth.
- **Trace across agents** (Chapter 14) — you need to see the whole multi-agent trajectory to debug it.

## Chapter summary
- A **multi-agent system** = specialized agents (role, tools, model) collaborating; benefits are separation, specialization, parallelism; costs are coordination, failure modes, spend, debuggability.
- Orchestration styles: **handoffs, graphs, crews, conversation, hierarchical/supervisor**; common topology is **supervisor-workers.**
- Use multiple agents for **distinct roles, parallelism, context-overload relief, or an independent critic.**
- **Start with one agent**; add more only for a nameable role separation — multi-agent multiplies a weak foundation's problems.
- Reliability needs **narrow roles, explicit coordination, managed shared context, system-wide bounds, and cross-agent tracing.**

## Cross-references
- Chapter 10 (orchestrator-workers, evaluator-optimizer), Chapter 09 (framework orchestration), Chapter 12 (A2A for agent interop), Chapter 14 (tracing).
