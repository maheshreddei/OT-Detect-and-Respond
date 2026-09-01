# Chapter 01 — What an AI Agent Is

> Part I · Foundations. Before you build one, get crisp on what an agent actually is, how it differs from a chatbot or a script, and — most importantly — when you should and shouldn't use one.

## 1.1 A definition you can build from

An **AI agent** is a system where a language model (LLM) **decides its own actions in a loop** to accomplish a goal. Given an objective and a set of **tools** (things it can do — call an API, run code, search a database), the model repeatedly:

1. **Reasons** about what to do next,
2. **Acts** by choosing a tool and its inputs,
3. **Observes** the result of that action,
4. **Repeats** until the goal is met or it decides to stop.

The defining property is **autonomy over control flow**: the LLM, not your code, decides what happens next. That single shift — handing the "what to do next" decision to the model — is what makes something an agent.

## 1.2 The spectrum: from prompt to agent

It helps to see agents as one end of a spectrum of LLM applications:

| Type | Who controls the flow | Example |
|------|----------------------|---------|
| **Single prompt** | You (one call) | "Summarize this text" |
| **Chain / workflow** | You (fixed sequence) | Extract → classify → format, in a hard-coded order |
| **Router** | You (LLM picks one branch) | The model chooses which of N predefined paths to run |
| **Agent** | **The model (dynamic loop)** | The model decides which tools to call, in what order, how many times |

The crucial line is between **workflows** (you define the steps; the LLM fills them in) and **agents** (the LLM defines the steps at runtime). Both are legitimate and useful. Agents are more flexible but less predictable, more expensive, and harder to test — so the choice between them is a real engineering decision, not a default.

## 1.3 Agent vs chatbot

A chatbot responds to messages. An agent **acts on the world**. A chatbot can tell you what the weather API would say; an agent calls the weather API, reads the result, and may then book you an indoor venue because it rained. The differences that matter:

- A chatbot's output is **text**; an agent's output includes **actions** (tool calls) with real effects.
- A chatbot does one turn; an agent runs **many internal steps** before it responds.
- A chatbot is stateless-ish; an agent usually needs **memory** to track progress across steps.

## 1.4 When to use an agent (and when not to)

This is the most important judgment in the whole field, and the industry consensus is clear: **use the simplest thing that works.** Reach for an agent only when the task genuinely needs dynamic decision-making.

**Good fits for an agent:**
- The steps **can't be known in advance** — they depend on what earlier steps discover (research a topic, debug an error, triage a ticket).
- The task needs **many tools used in a data-dependent order**.
- The **path branches** widely and enumerating branches by hand is impractical.

**Bad fits — use a workflow or a single call instead:**
- The steps are **fixed and known** (extract → validate → store). A hard-coded chain is cheaper, faster, and more reliable.
- **Latency or cost is tight** — every agent step is another model call.
- **Predictability/auditability is paramount** — an agent's dynamic path is harder to certify.

A useful rule of thumb: *start with a workflow; upgrade to an agent only when a fixed sequence provably can't handle the variety of the task.* Many "agent" projects are workflows that would be simpler, cheaper, and more reliable if built as workflows.

## 1.5 What can go wrong (so you design for it)

Agents fail in characteristic ways you should anticipate from day one:

- **Looping** — the agent repeats actions without progress (needs step limits and loop detection).
- **Hallucinated actions** — calling a tool with invented arguments (needs strict schemas and validation).
- **Cost/latency blowups** — a task that should take 3 steps takes 30 (needs budgets and observability).
- **Unsafe actions** — an agent with real permissions doing something destructive (needs guardrails and human-in-the-loop).

Every later chapter is, in part, an answer to one of these failure modes. Good agent engineering is mostly about **constraining** a powerful, unpredictable loop.

## Chapter summary
- An agent is an **LLM that decides its own actions in a loop** to reach a goal — its defining trait is **autonomy over control flow.**
- Agents sit at one end of a spectrum: prompt → chain → router → **agent**; the key line is **workflow (you define steps) vs agent (the model defines steps).**
- Use an agent only when steps **can't be known in advance**; otherwise a workflow is cheaper, faster, and more reliable.
- Design from the start for the failure modes: **looping, hallucinated actions, cost blowups, unsafe actions.**

## Cross-references
- Chapter 02 (anatomy) and Chapter 03 (the loop) formalize how an agent works.
- Chapter 10 (patterns) covers the workflow patterns to prefer when a full agent is overkill.
