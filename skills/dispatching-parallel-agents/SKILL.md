---
name: dispatching-parallel-agents
description: Use when planning to dispatch two or more subagents concurrently, including when work boundaries or dependencies still need to be assessed.
---

# Dispatching Parallel Agents

Use this skill when you plan to have two or more subagents work at the same time. The work can be related; it must be independently executable without waiting for another unit or writing to the same uncoordinated files or state.

Do not use parallel dispatch just because a task has several steps. If one step needs another's result, sequence them. If units share files or unresolved interfaces, keep them together or settle ownership and the interface before dispatch.

## Decide What Can Run Together

1. List the work units, files they may change, and outputs they need from one another.
2. Group together any units that share files, mutable state, or an undecided interface. If one unit consumes another's output, sequence them instead.
3. Dispatch only groups that can make progress concurrently. Related work is fine when its boundaries are clear.

Examples:

- Two independent bugs in different subsystems can be investigated at the same time.
- UI and API work can proceed together if the interface and file ownership are already agreed.
- A schema change and code that depends on the new schema should be sequenced unless the contract is fixed first and file ownership is separate.

## Give Each Agent a Usable Brief

For each subagent, state:

- **Goal:** the result or question to resolve.
- **Scope:** relevant files, paths, or subsystem; say what it should not change when that boundary matters.
- **Context:** requirements, known facts, and settled interfaces it needs; do not make it infer critical decisions from an unrelated long conversation.
- **Result:** what to return, such as a short summary, evidence, findings, or changed files.

Make the brief self-contained enough for the task, but do not copy irrelevant history. Invite the agent to ask or stop if a missing decision could change the result.

For a small task, a concise report in the reply is enough. Ask for a report file when the result is long, needs durable evidence, or several outputs must be tracked. A named status list or progress ledger is useful for long or multi-stage work; do not create one for a short dispatch.

## Dispatch and Integrate

Send independent briefs in the same dispatch round so the agents can work concurrently. Keep dependent work for a later round after its input is settled.

When results return:

1. Read the summary and inspect the changes or evidence that affect your decision.
2. Check for overlapping edits, inconsistent assumptions, and interface mismatches.
3. Resolve conflicts before combining the work.
4. Run the checks relevant to the combined changes. Run the full suite when project practice or the scope warrants it, not automatically for every delegation.

If a requirement or shared interface changes, update only the briefs for work not yet completed before dispatching those agents.
