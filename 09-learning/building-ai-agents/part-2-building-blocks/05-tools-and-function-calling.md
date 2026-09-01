# Chapter 05 — Tools & Function Calling

> Part II · Building blocks. Tools are how an agent does anything beyond talk. This chapter covers how to define them, how the model calls them, how to execute them safely, and the emerging standard (MCP) for sharing them.

## 5.1 What a tool is

A tool is three things bundled together:
1. **A function** — the actual code that does something (query a DB, call an API, run a calculation).
2. **A schema** — a machine-readable description of its inputs (names, types, which are required).
3. **A description** — natural language telling the model *what the tool does and when to use it.*

The model never runs your code; it **requests** a call by emitting the tool's name and arguments, and *your* runtime executes it. The description is the model's only guide to using the tool well — write it like documentation for a smart colleague.

## 5.2 Defining a tool

A typical tool definition (the schema the model sees):

```json
{
  "name": "get_weather",
  "description": "Get the current weather for a city. Use when the user asks about weather or when weather affects a recommendation.",
  "input_schema": {
    "type": "object",
    "properties": {
      "city": {"type": "string", "description": "City name, e.g. 'Dubai'"},
      "units": {"type": "string", "enum": ["c", "f"], "default": "c"}
    },
    "required": ["city"]
  }
}
```

And the function behind it:

```python
def get_weather(city: str, units: str = "c") -> dict:
    data = weather_api.fetch(city)
    return {"city": city, "temp": data.temp_c if units == "c" else data.temp_f, "units": units}
```

Most frameworks generate the schema for you from a typed Python function and its docstring — but this is what's underneath.

## 5.3 The function-calling loop

Function calling is a request/response dance between your runtime and the model:

1. You send the model the messages **plus the tool schemas**.
2. The model responds with a **tool call**: `get_weather(city="Dubai")`.
3. Your runtime **executes** the function and gets a result.
4. You send the result **back to the model** as a tool result.
5. The model uses it to continue — another tool call, or a final answer.

This is exactly the agent loop (Chapter 03) with tools as the actions. Chapter 08 implements it end to end.

## 5.4 Writing good tools

Tool quality determines agent quality. Practical rules:

- **Descriptions are prompts.** Say what the tool does *and when to use it*; ambiguity causes wrong tool selection.
- **Keep tools focused.** One clear job each; a mega-tool with a dozen modes confuses the model.
- **Constrain inputs** with enums, types, and required fields — the schema is a guardrail.
- **Return clean, structured results** the model can reason over; include useful errors ("no account found for that email") rather than raising raw exceptions.
- **Make tools idempotent or safe to retry** where possible; agents will re-call on error.
- **Right-size the toolset.** Too many tools dilutes selection accuracy; give the agent only what the task needs.

## 5.5 Executing tools safely

Tools are where an agent touches real systems, so they're where the danger is:

- **Validate arguments** before executing (never trust model-generated inputs blindly).
- **Least privilege** — a tool should be able to do only its job; scope credentials tightly.
- **Separate read from write.** Read tools are low-risk; write/destructive tools deserve confirmation or human approval (Chapter 15).
- **Sandbox code execution** — if the agent runs code, run it in an isolated, resource-limited environment.
- **Handle failure** — return errors as results the model can react to, and cap retries.

## 5.6 MCP — a standard for tools

The **Model Context Protocol (MCP)** is an open standard that lets agents connect to tools and data sources through a uniform interface, so a tool ("MCP server") built once works with any MCP-compatible agent. <cite index="6-1">The MCP 2026-07-28 spec reached release-candidate status</cite>, and major frameworks (the Claude Agent SDK, Microsoft Agent Framework, and others) support it natively. The value: instead of re-writing a Slack/GitHub/database tool for every framework, you use or publish an MCP server once and any MCP-aware agent can use it. As you scale, prefer standard MCP tools over bespoke integrations where they exist.

## Chapter summary
- A tool = **function + input schema + description**; the model **requests** calls, your runtime **executes** them.
- The **function-calling loop** (send schemas → model calls tool → execute → return result → continue) is the agent loop with tools as actions.
- Write **focused tools with prompt-quality descriptions, constrained inputs, and clean results**; right-size the toolset.
- Execute tools **safely**: validate inputs, least privilege, gate writes, sandbox code, handle errors.
- **MCP** standardizes tools so they're reusable across agents/frameworks.

## Cross-references
- Chapter 08 (from-scratch agent) executes tools in a loop; Chapter 12 (protocols) goes deeper on MCP; Chapter 15 (guardrails) gates dangerous tools.
- Code: [`../code/tools_example.py`](../code/tools_example.py).
