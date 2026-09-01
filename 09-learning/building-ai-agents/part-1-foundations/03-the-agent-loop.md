# Chapter 03 — The Agent Loop

> Part I · Foundations. The loop is the beating heart of every agent. This chapter covers the canonical loop and the three patterns that shape how the model reasons within it.

## 3.1 The canonical loop

At its simplest, every agent runs this cycle:

```
  while not done and steps < max_steps:
      decision = model(context)          # think + decide
      if decision.is_final_answer:
          done = True
          return decision.answer
      else:
          result = execute(decision.tool, decision.args)   # act
          context.append(decision, result)                  # observe
```

Three things happen each turn — **think, act, observe** — and the context grows with each cycle so the model always sees the full history of what it has tried and learned. The loop ends when the model produces a final answer or a guardrail (step limit, budget, error) stops it.

## 3.2 Pattern 1 — ReAct (Reason + Act)

**ReAct** is the foundational and most common agent pattern. The model **interleaves reasoning and acting**: before each action it produces a short "thought" explaining its plan, then the action, then observes the result, then reasons again. The transcript looks like:

```
  Thought: I need the user's account balance, which requires their account ID.
  Action: lookup_account(email="user@example.com")
  Observation: {"account_id": "A-123", "balance": 4200}
  Thought: I have the balance. I can answer now.
  Answer: Your balance is $4,200.
```

ReAct works because the explicit reasoning step improves the model's decisions and makes the agent's behavior **inspectable** — you can read exactly why it did what it did. Most agents you build are ReAct agents, whether or not the framework names it.

## 3.3 Pattern 2 — Plan-and-Execute

For complex, multi-step tasks, having the model decide every micro-step reactively can wander. **Plan-and-execute** splits the work:

1. A **planning** step: the model produces an explicit, ordered plan of subtasks up front.
2. An **execution** phase: the agent works through the plan, using the loop for each subtask.
3. Optional **re-planning**: if reality diverges from the plan, the model revises it.

Advantages: better handling of long tasks, fewer wasted steps, and a plan you can inspect or approve before execution. Trade-off: a rigid plan can be wrong; good implementations allow re-planning when observations contradict the plan.

## 3.4 Pattern 3 — Reflection (self-critique)

**Reflection** adds a step where the model **critiques its own output** and tries again. After producing a result, a reflection prompt asks "is this correct/complete? what's wrong? how would you improve it?" and the agent revises. Variants (sometimes called Reflexion) feed the critique back into another attempt. Reflection markedly improves quality on tasks with a checkable notion of "good" (code that must run, answers that must satisfy constraints) at the cost of extra model calls. It pairs naturally with the **evaluator-optimizer** workflow (Chapter 10).

## 3.5 Choosing and combining patterns

These patterns are not exclusive — real agents combine them:

- Use **ReAct** as the default for tool-using agents.
- Add **planning** when tasks are long or benefit from an up-front, inspectable plan.
- Add **reflection** when quality matters and correctness is checkable.

Start with plain ReAct. Add planning or reflection only when you observe the specific failure they fix (wandering → planning; low-quality output → reflection). Complexity you don't need is complexity that will bite you in production.

## 3.6 Stopping conditions — the unglamorous essential

A loop needs to end. Robust agents enforce several stopping conditions:

- **Task complete** — the model signals a final answer.
- **Step/iteration limit** — a hard cap (e.g. 15 steps) to prevent runaway loops.
- **Budget limit** — a maximum token/dollar/time spend.
- **No-progress detection** — the same action repeated, or repeated errors.
- **Human handoff** — escalate to a person when stuck or when an action needs approval.

Skipping stopping conditions is the most common way a demo agent becomes a runaway bill. Build them in from the first version.

## Chapter summary
- Every agent runs a **think → act → observe** loop, growing its context each turn, ending on completion or a guardrail.
- **ReAct** (interleaved reasoning and acting) is the default, inspectable pattern.
- **Plan-and-execute** helps long tasks (with re-planning); **reflection** improves quality on checkable tasks.
- **Combine patterns** as needed, starting simple; add complexity only to fix an observed failure.
- Always enforce **stopping conditions** (completion, step/budget limits, no-progress, human handoff).

## Cross-references
- Chapter 08 implements a ReAct loop from scratch; Chapter 10 covers workflow patterns and evaluator-optimizer.
- Chapter 15 (guardrails) hardens the stopping conditions.
