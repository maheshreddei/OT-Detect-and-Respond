# Chapter 04 — The Model Layer

> Part II · Building blocks. The model is the agent's brain. This chapter is about choosing one, prompting it to behave like an agent, and getting reliable structured output out of it.

## 4.1 Choosing a model

Agent quality depends heavily on the model's **reasoning**, **instruction-following**, and **tool-use reliability**. When choosing:

- **Tool-use reliability** matters most for agents — does the model emit well-formed tool calls and pick the right tool? A model that reasons beautifully but calls tools sloppily makes a bad agent.
- **Context window** — agents accumulate long histories; a larger window means fewer truncation headaches (but costs more).
- **Latency and cost** — every step is a call; a cheaper/faster model per step compounds across a long loop.
- **Structured output support** — native JSON/schema modes make extraction reliable.

A common and effective pattern is **model routing** (Chapter 16): use a strong model for the hard reasoning/planning steps and a cheaper, faster model for routine steps (formatting, simple extraction). Don't pay flagship prices for trivial turns.

## 4.2 The agent system prompt

The system prompt is where you define the agent's **role, goals, constraints, and tool-use policy**. A good agent system prompt covers:

- **Role & objective** — what the agent is and what "done" looks like.
- **How to use tools** — when to call them, and to prefer tools over guessing.
- **Constraints** — what it must not do; when to ask a human; safety limits.
- **Output format** — how to present the final answer.
- **Reasoning guidance** — e.g. "think step by step before acting" (encourages ReAct behavior).

Keep it explicit. Agents fail more often from vague instructions than from weak models. State the stopping condition ("when you have the answer, respond directly instead of calling more tools") — a surprising amount of looping comes from omitting it.

## 4.3 Structured output

Agents constantly need the model to return **structured data** — a tool call's arguments, an extracted record, a routing decision. Three approaches, most to least reliable:

1. **Native tool/function calling** — the model returns arguments that conform to a JSON schema you provide. This is the backbone of agents (Chapter 05) and the most reliable path.
2. **Native structured-output / JSON mode** — ask for output matching a schema; the API enforces valid JSON.
3. **Prompt-and-parse** — ask for JSON in the prompt and parse it. The fallback; always validate and handle parse failures.

Prefer schema-enforced approaches. A validation layer (e.g. a Pydantic model) that rejects malformed output and asks the model to retry turns flaky parsing into reliable extraction.

## 4.4 Prompting patterns that make agents work

- **Be explicit about tools.** Tell the model which tools exist and when to use each; don't assume it will infer usage.
- **Encourage reasoning.** "Think before you act" improves tool selection (the ReAct effect).
- **Give examples** of good tool use for tricky tasks (few-shot).
- **Constrain the output** so the loop can parse it deterministically.
- **Handle the "I don't know / I need a human" path** explicitly, so the agent escalates rather than hallucinating.

## 4.5 A minimal model call with tools (illustrative)

The shape of an agentic model call — provider-neutral pseudocode:

```python
response = model.generate(
    system="You are a support agent. Use tools to look things up; "
           "when you have the answer, respond directly.",
    messages=history,                 # the running transcript
    tools=[lookup_account, issue_refund],   # tool schemas (Chapter 05)
)

if response.tool_calls:
    # the model chose to act -> execute (Chapter 08)
    ...
else:
    # the model produced a final answer
    return response.text
```

Every framework wraps this; understanding the raw shape is what lets you debug when the wrapper misbehaves.

## Chapter summary
- Choose a model for **tool-use reliability**, context size, latency/cost, and structured-output support; **route** hard vs easy steps to different models.
- The **system prompt** defines role, tool-use policy, constraints, output format, and the **stopping condition** — vague prompts cause most failures.
- Get structure via **native tool calling** or **JSON/schema mode**; validate and retry on malformed output.
- Prompt explicitly about tools, encourage reasoning, and give the agent an **escalation path.**

## Cross-references
- Chapter 05 (tools) builds on native function calling; Chapter 16 (deployment) covers model routing and caching.
