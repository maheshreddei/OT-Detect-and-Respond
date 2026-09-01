# Chapter 02 — The Anatomy of an Agent

> Part I · Foundations. Every agent, no matter the framework, is assembled from the same handful of parts. Learn the parts and you can read, build, or debug any agent.

## 2.1 The five components

```
                 ┌──────────────────────────────────────┐
   goal ───────▶ │   ORCHESTRATION  (the loop)          │
                 │   ┌──────────┐   decides next action  │
                 │   │  MODEL   │◀──────────┐            │
                 │   │ (the     │           │            │
                 │   │  brain)  │──▶ action │            │
                 │   └──────────┘           │            │
                 │        ▲                 ▼            │
                 │     ┌──────┐         ┌───────┐        │
                 │     │MEMORY│         │ TOOLS │        │
                 │     └──────┘         └───────┘        │
                 └──────────────────────────────────────┘
                            observation ◀── result
```

1. **Model (the brain).** The LLM that reasons and decides. It doesn't *do* anything itself — it emits text and tool-call requests.
2. **Tools (the hands).** Functions the agent can invoke to affect or observe the world: APIs, database queries, code execution, web search, other agents.
3. **Memory.** What the agent knows and remembers — the immediate context, the running scratchpad of this task, and any long-term store across sessions.
4. **Orchestration (the loop).** The code that runs the cycle: send context to the model, get its decision, execute tools, feed results back, repeat, and decide when to stop.
5. **The goal / instructions.** The system prompt and task that define what the agent is for, how it should behave, and what "done" means.

That's it. Frameworks differ in ergonomics, but every one of them is these five parts.

## 2.2 The model: the decision-maker

The model is prompted with the goal, the available tools, and the history so far, and it returns either a **final answer** or a **tool call** (a structured request to run a specific tool with specific arguments). Modern models are **trained for tool use** — they emit tool calls in a structured format the runtime can parse and execute. The model's quality (reasoning, instruction-following, tool-use reliability) is the single biggest determinant of agent quality.

## 2.3 Tools: how the agent acts

A tool is a function plus a **description the model can understand**: a name, a natural-language description of what it does and when to use it, and a schema for its inputs. The model reads these descriptions to decide which tool to call. Tools are how an agent transcends "just talking" — they connect the reasoning loop to real systems. Chapter 05 covers them in depth.

## 2.4 Memory: three horizons

Agents need memory at three horizons:

- **Context (working memory)** — everything currently in the model's context window: the system prompt, the task, and the running transcript of thoughts, actions, and observations. This is the agent's short-term memory and it's finite.
- **Task/session memory** — the scratchpad for the current task, sometimes summarized or externalized when the transcript grows too large for the context window.
- **Long-term memory** — knowledge that persists across sessions (user preferences, past interactions, learned facts), usually stored externally (e.g. a vector database) and retrieved when relevant.

Managing memory — especially keeping the context window relevant and within limits — is one of the central engineering challenges of agents (Chapter 06).

## 2.5 Orchestration: the loop that ties it together

The orchestration layer is the actual program. Its job:

1. Assemble the context (instructions + tools + history).
2. Call the model.
3. If the model returned a tool call: **execute the tool**, capture the result, append it to the history, and go to step 1.
4. If the model returned a final answer: **stop** and return it.
5. Enforce the guardrails: step limits, budgets, error handling, and stopping conditions.

This loop is so central that Chapter 03 is devoted to it, and Chapter 08 builds it from scratch. Frameworks (Chapter 09) implement this loop for you with extra features (state persistence, streaming, branching), but it's the same loop underneath.

## 2.6 Putting it together conceptually

A one-paragraph mental model: *You give the **model** a **goal** and a description of its **tools**. The **orchestration loop** shows the model the goal and everything that's happened so far (its **memory/context**), asks it what to do next, executes whatever tool it chooses, feeds the result back, and repeats — until the model says it's done, or a guardrail stops it.* Hold this picture and every agent framework becomes легible.

## Chapter summary
- Every agent = **model + tools + memory + orchestration loop + goal/instructions.**
- The **model decides** (emits answers or tool calls) but doesn't act; **tools** are how it acts.
- Memory spans three horizons: **context (working), task/session, and long-term.**
- The **orchestration loop** assembles context → calls the model → executes tools → repeats → stops on completion or a guardrail.

## Cross-references
- Chapter 03 (the loop), Chapter 05 (tools), Chapter 06 (memory) go deep on each part.
- Chapter 08 builds all five components from scratch in Python.
