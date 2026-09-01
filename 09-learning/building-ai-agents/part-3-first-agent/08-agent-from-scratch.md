# Chapter 08 — An Agent From Scratch

> Part III · Your first agent. The single most clarifying thing you can do is build a working agent with **no framework** — just the model API, a couple of tools, and the loop. After this chapter, every framework will look like sugar over what you now understand.

## 8.1 What we're building

A minimal ReAct agent that can answer questions using two tools — a calculator and a mock web search — running the full **think → act → observe** loop until it produces an answer. It's ~60 lines and contains every concept from Part I–II.

## 8.2 The pieces

1. **Tools** — plain Python functions plus their schemas.
2. **The model call** — send messages + tool schemas, get back either a tool call or an answer.
3. **The loop** — execute tool calls, feed results back, repeat, with a step limit.

## 8.3 Defining tools

```python
def calculator(expression: str) -> str:
    """Evaluate a math expression, e.g. '3 * (4 + 5)'."""
    import ast, operator as op
    # safe eval omitted for brevity; use a real safe evaluator in production
    return str(eval(expression, {"__builtins__": {}}))

def web_search(query: str) -> str:
    """Return search results for a query (mocked here)."""
    return f"Top result for '{query}': ..."

TOOLS = {"calculator": calculator, "web_search": web_search}

TOOL_SCHEMAS = [
    {"name": "calculator", "description": "Evaluate a math expression.",
     "input_schema": {"type": "object",
        "properties": {"expression": {"type": "string"}}, "required": ["expression"]}},
    {"name": "web_search", "description": "Search the web for current info.",
     "input_schema": {"type": "object",
        "properties": {"query": {"type": "string"}}, "required": ["query"]}},
]
```

## 8.4 The loop

```python
def run_agent(user_goal: str, max_steps: int = 10) -> str:
    messages = [{"role": "user", "content": user_goal}]
    system = ("You are a helpful agent. Use tools when needed. "
              "When you have the answer, reply directly without calling a tool.")

    for step in range(max_steps):
        response = model.generate(system=system, messages=messages, tools=TOOL_SCHEMAS)

        if not response.tool_calls:            # model produced a final answer
            return response.text

        messages.append({"role": "assistant", "content": response.raw})
        for call in response.tool_calls:       # execute each requested tool
            fn = TOOLS[call.name]
            try:
                result = fn(**call.args)
            except Exception as e:
                result = f"ERROR: {e}"         # errors are observations, not crashes
            messages.append({"role": "tool", "tool_call_id": call.id, "content": str(result)})

    return "Stopped: reached the step limit without finishing."
```

That's a complete agent. Note every Part I–II concept in it: the **loop**, **tools as actions**, the **context** (`messages`) growing each turn, the **stopping conditions** (final answer or `max_steps`), and **errors returned as observations** so the model can recover.

## 8.5 Tracing what happens

For the goal *"What is 15% of 2,400, and is it more than the population of Vatican City?"* the loop might run:

```
  step 1: model → calculator(expression="0.15 * 2400")  → 360
  step 2: model → web_search(query="population of Vatican City") → "~800"
  step 3: model → (no tool) → "15% of 2,400 is 360, which is less than ~800."
```

Three model calls, two tool executions, one answer. You can *see* the reasoning by logging each step — which is exactly the observability you'll formalize in Chapter 14.

## 8.6 Hardening the from-scratch agent

The skeleton above is the happy path. Production needs:

- **A safe tool executor** (never raw `eval`; validate arguments against the schema).
- **A budget** (max tokens/dollars, not just steps).
- **Loop/no-progress detection** (bail if the same tool+args repeats).
- **Structured logging** of every step for debugging.
- **A final-answer guard** (if it hits the step limit, summarize progress rather than returning nothing).

The full runnable version with these is in [`../code/minimal_agent.py`](../code/minimal_agent.py).

## 8.7 Why build this before using a framework

Frameworks (Chapter 09) implement this loop with persistence, streaming, branching, and integrations. But when a framework agent misbehaves — loops, picks the wrong tool, blows its budget — you debug it by understanding *this* loop. Teams that skip the from-scratch step tend to treat frameworks as magic and get stuck when the magic breaks. Build it once by hand; then use the framework knowing what it does.

## Chapter summary
- A complete agent is ~60 lines: **tools + schemas, a model call, and a loop** that executes tool calls and feeds results back.
- The loop embodies every core concept: **context growth, tools as actions, stopping conditions, errors-as-observations.**
- **Harden** it with a safe executor, budgets, loop detection, logging, and a final-answer guard.
- Build from scratch first so you can **debug frameworks** later.

## Cross-references
- Chapter 03 (the loop) is what this implements; Chapter 09 shows the framework equivalents; Chapter 14 adds tracing.
- Code: [`../code/minimal_agent.py`](../code/minimal_agent.py).
