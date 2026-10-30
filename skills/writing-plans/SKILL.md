---
name: writing-plans
description: Use when a large or high-risk change, or work spanning multiple components, sessions, or delegated units, needs a durable implementation plan before coding.
---

# Writing Plans

A plan records decisions an implementer should not have to guess: the goal, scope, interfaces, files, and how to tell the work is done. It is useful for large, multi-session, high-risk, or delegated work. A clear task that one agent can finish in one session may need only a short checklist or no plan.

This skill is self-contained. It does not require a separate design or execution skill.

## Choose the Right Artifact

- Use a short checklist for a small, clear task with a few steps.
- Use a plan when work spans components, sessions, or independent delegated units, or when losing a decision would be costly.
- Add a separate design/spec document only when another person will implement or maintain the work, the decisions need a durable record, or the project already uses design documents. Otherwise put the agreed design in the plan. The optional template `references/spec-template.md` explains what its sections capture; omit sections that do not apply.

Do not create both a spec and a plan that repeat the same detail. A spec records why and what; a plan records how the work is divided and verified. If the project has no convention for specs, ask once whether the user wants one. The compact template in `references/spec-template.md` is optional and can be included in or linked from the plan.

## Plan Contents

Before writing tasks, map the affected areas and identify shared files and interfaces. Group work that touches the same files or depends on unsettled decisions. Split only where tasks can be completed and checked independently.

Include:

- **Goal and non-goals:** what changes and what is explicitly out of scope.
- **Approach:** the chosen design and important trade-offs; note unresolved decisions that need the user's input.
- **Files and responsibilities:** exact known paths and why they change.
- **Interfaces:** names and shapes of data or calls that cross task boundaries.
- **Behavior to verify:** the meaningful outcomes and relevant edge cases, using the project's testing practice.
- **Acceptance criteria:** observable conditions that show the whole change works.
- **Constraints:** verified external API facts, compatibility needs, or project rules that affect implementation.

Do not write the implementation into the plan. Code bodies and command-by-command recipes usually belong to the implementer. Be specific where a guess would alter behavior; leave routine implementation choices to the person doing the work.

## Execution

The plan does not determine who implements the work. The coordinator may implement directly, delegate independent units, or combine both approaches according to task size, risk, context, and the user's preference. Do not create a subagent per task by default.

- Give each delegate only the goal, scope, constraints, settled interfaces, and expected result it needs. See `dispatching-parallel-agents` when sending two or more agents to work concurrently.
- Use one progress record only when work is long enough that progress could be lost; the plan itself may be that record.
- If a decision or interface changes, update the affected plan items and any not-yet-started briefs before continuing.
- Review the integrated result at meaningful boundaries. Small edits do not need per-task review.
- Verify the combined work with checks relevant to the changes and the project's norms. Preserve a baseline before a change removes the path needed to measure it.
- Do not push, merge, or delete branches without the user's instruction. Preserve uncommitted work.

## Plan Review

Review your plan for missing requirements, unclear interfaces, unnecessary tasks, and acceptance criteria that cannot be checked. Ask the user to review it when it will guide delegated or multi-session work, or when an incorrect assumption would be expensive. Do not require a separate approval round for a short checklist or a plan that merely records an already-approved design without adding decisions.

When a large or high-stakes plan would benefit from a fresh reader, dispatch one read-only reviewer using `plan-document-reviewer-prompt.md`. Point its spec field at the separate design record when one exists; when none exists, omit that field and tell the reviewer to use the plan's design section. Skip this for short checklists or when the user does not want an extra review round.

## When the Plan Changes

Keep the plan and any active briefs consistent. Update only the affected items; do not preserve obsolete choices as current instructions. Search documents for paths, names, values, and requirements that changed, and correct references that would mislead the next reader.
