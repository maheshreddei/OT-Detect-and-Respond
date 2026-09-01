"""
minimal_agent.py — a complete ReAct agent in ~120 lines, no framework.

This is the Chapter 08 agent, hardened: safe tool executor, step + iteration
budgets, loop/no-progress detection, structured step logging, and a final
answer guard.

It is provider-neutral: plug in any LLM by implementing `call_model()`.
Replace the mock with a real client (Anthropic, OpenAI, etc.).

Run:  python minimal_agent.py
"""
from __future__ import annotations
import json, ast, operator, logging
from dataclasses import dataclass, field

logging.basicConfig(level=logging.INFO, format="%(message)s")
log = logging.getLogger("agent")

# ---------- 1. Tools ----------
_ALLOWED_OPS = {
    ast.Add: operator.add, ast.Sub: operator.sub, ast.Mult: operator.mul,
    ast.Div: operator.truediv, ast.Pow: operator.pow, ast.USub: operator.neg,
}

def safe_calc(expression: str) -> str:
    """Safely evaluate a basic arithmetic expression."""
    def _eval(node):
        if isinstance(node, ast.Constant):
            return node.value
        if isinstance(node, ast.BinOp):
            return _ALLOWED_OPS[type(node.op)](_eval(node.left), _eval(node.right))
        if isinstance(node, ast.UnaryOp):
            return _ALLOWED_OPS[type(node.op)](_eval(node.operand))
        raise ValueError("unsupported expression")
    return str(_eval(ast.parse(expression, mode="eval").body))

def web_search(query: str) -> str:
    """Mock web search — replace with a real search API/tool."""
    return f"(mock) top result for '{query}'"

TOOLS = {"calculator": safe_calc, "web_search": web_search}

TOOL_SCHEMAS = [
    {"name": "calculator", "description": "Evaluate a basic arithmetic expression like '0.15 * 2400'.",
     "input_schema": {"type": "object", "properties": {"expression": {"type": "string"}},
                      "required": ["expression"]}},
    {"name": "web_search", "description": "Search the web for current information.",
     "input_schema": {"type": "object", "properties": {"query": {"type": "string"}},
                      "required": ["query"]}},
]

# ---------- 2. Model interface (swap in a real client) ----------
@dataclass
class ToolCall:
    id: str
    name: str
    args: dict

@dataclass
class ModelResponse:
    text: str | None = None
    tool_calls: list[ToolCall] = field(default_factory=list)

def call_model(system: str, messages: list[dict]) -> ModelResponse:
    """
    REPLACE THIS with a real LLM call that supports tool use, e.g. Anthropic:

        client = anthropic.Anthropic()
        r = client.messages.create(model="claude-...", system=system,
                                   messages=messages, tools=TOOL_SCHEMAS, max_tokens=1024)
        # parse r.content into ModelResponse(text=..., tool_calls=[ToolCall(...)])

    The mock below just demonstrates the loop mechanics for the sample goal.
    """
    last = messages[-1]
    if last["role"] != "tool" and "15%" in json.dumps(messages):
        return ModelResponse(tool_calls=[ToolCall("t1", "calculator", {"expression": "0.15 * 2400"})])
    return ModelResponse(text="15% of 2400 is 360.")

# ---------- 3. The loop (hardened) ----------
def run_agent(goal: str, max_steps: int = 12) -> str:
    system = ("You are a helpful agent. Use tools when needed. "
              "When you have the answer, reply directly without calling a tool.")
    messages: list[dict] = [{"role": "user", "content": goal}]
    seen_calls: set[str] = set()

    for step in range(1, max_steps + 1):
        resp = call_model(system, messages)

        if not resp.tool_calls:
            log.info(f"[step {step}] final answer")
            return resp.text or ""

        messages.append({"role": "assistant", "content": f"(requested {len(resp.tool_calls)} tool call(s))"})
        for call in resp.tool_calls:
            sig = f"{call.name}:{json.dumps(call.args, sort_keys=True)}"
            if sig in seen_calls:                       # no-progress / loop guard
                result = "ERROR: repeated identical call detected; try a different approach."
            elif call.name not in TOOLS:
                result = f"ERROR: unknown tool '{call.name}'."
            else:
                seen_calls.add(sig)
                try:
                    result = TOOLS[call.name](**call.args)   # execute
                except Exception as e:                       # errors are observations
                    result = f"ERROR: {e}"
            log.info(f"[step {step}] {call.name}({call.args}) -> {result}")
            messages.append({"role": "tool", "tool_call_id": call.id, "content": str(result)})

    return "Stopped: reached step limit. Partial progress logged above."

if __name__ == "__main__":
    print(run_agent("What is 15% of 2400?"))
