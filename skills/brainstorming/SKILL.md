---
name: brainstorming
description: Use when starting nontrivial implementation — features, behavior changes, refactors, integrations, or multi-component work — even with clear requirements, or when asked to brainstorm or explore a design. Not for mechanical edits or explanation-only requests; diagnose bugs first.
---

# Brainstorming

Make sure nontrivial work solves the right problem before building it. Ground the design in evidence, resolve important choices with the user, and leave a clear way to tell whether it works. This skill is self-contained.

**Loading is a design checkpoint, not an automatic interview or approval gate.** If the request or an approved design already settles the important decisions, inspect the current context, summarize briefly, and proceed within the user's authorization.

## When to Use

Use before nontrivial implementation even if the request sounds precise. Work is nontrivial when it requires reasoning about behavior, interacting parts, interfaces, data, compatibility, or a meaningful design trade-off rather than directly applying a local, obvious edit. Typical cases include a new workflow, changes across modules, a refactor that shifts responsibilities, or an external integration.

Also use when the user asks to explore ideas, requirements, or a design, even before implementation is requested. Exploration authorizes discussion and investigation, not automatically building the result.

- Skip mechanical edits such as a typo, a static-label rename, or formatting, and explanation-only requests.
- For an existing bug or performance problem, establish the cause first; `systematic-debugging`, if available, owns that investigation. Use brainstorming when the fix needs nontrivial design or investigation reveals a redesign choice, not instead of finding the cause.
- An already-approved design still gets a brief check against current code and constraints, not another approval round.

## Investigate Before Proposing

1. **Establish the problem.** Identify the desired outcome, who it serves, scope, constraints, and observable success. Read the relevant code, documents, and existing behavior before asking about facts they can answer. Keep user decisions, verified facts, proposals, and assumptions distinct.
2. **Close gaps that could change the approach.** Check affected interfaces, dependencies, and relevant failure paths. Verify uncertain technical facts with authoritative documentation or a focused probe; do not ask the user to guess an API's behavior or invent a contract.
3. **Find the decisions that remain.** Consider relevant alternatives, edge cases, compatibility, security/privacy, persisted data, and downstream effects. Scale depth to the work: investigate what could change scope, approach, correctness, or verification, not every imaginable concern.

If evidence is unavailable, name the uncertainty and its consequence. Resolve a material gap before relying on it; a low-risk, reversible assumption can be stated without blocking the work. If no material decisions remain, take the fast path to handoff.

## Conversation

1. **Ask the next decision-changing question.** Start with the most important unresolved goal or constraint. Ask one focused question at a time; batch only genuinely independent questions. Explain why the answer matters when that is not obvious. Do not repeat answered questions or run a fixed questionnaire.
2. **Make choices easy to compare.** Prefer the environment's question tool with selectable options when available; otherwise give concise choices in chat. Explain each option's benefit and cost, mark a recommendation when justified, and leave room for an alternative answer. Use an open question when meaningful choices cannot yet be offered.
3. **Compare real approaches once the goal is understood.** For important alternatives with meaningful trade-offs, present the viable options, usually two or three, and recommend one using the user's goals and the evidence. Include the smallest useful solution or retaining the current approach when viable. Do not invent alternatives to meet a quota.
4. **Resolve consequential choices before implementing them.** Ask when comparable alternatives change scope, architecture, user experience, privacy, data, compatibility, or operational cost. A recommendation does not settle a real trade-off for the user. If one approach is clearly better under the agreed constraints, explain why and proceed; routine code-level choices do not need permission.

Stop asking when the outcome, scope, approach, important constraints, and verification are clear enough that remaining unknowns cannot reasonably change them. Briefly summarize what is agreed and any bounded assumptions. For a small design, a few sentences in chat are enough.

For a feasibility-only question, answer from sufficient existing evidence or run the smallest useful disposable probe within the request's scope. Report findings and limitations, not a production implementation or a new test framework. Keeping a prototype is a separate decision.

## Approval and Handoff

For unresolved consequential choices, get the user's decision before implementation. The user's stated requirements and prior approvals already count as decisions; do not require a separate “approve the design” turn that adds nothing. Approval of a design does not authorize implementation when the user requested discussion only.

The handoff should make clear:

- What will change, what will not, and why the approach fits.
- Important behavior, interfaces, constraints, and relevant failure cases.
- Observable acceptance criteria and how to verify them using the project's existing practices.
- Any unresolved limitation, bounded assumption, and the authorized next step.

Use only the detail the work needs. A written design is optional: use one when decisions need a durable record, another person needs a handoff, or the project already keeps design docs. Follow project conventions and ask before introducing a new document convention. A durable implementation plan, using `writing-plans` if available, is useful for large, risky, multi-session, or delegated work; neither a plan nor a separate spec is mandatory after every discussion. Do not duplicate an agreed design across artifacts.

## Visual Decisions

When seeing a choice would genuinely help, offer the simplest useful mockup or diagram. Use ordinary text or an inline diagram when sufficient; a visual preview is optional, not a prerequisite for UI or architecture discussion.

Read `references/visual-decisions.md` when preparing mockups or comparing visual alternatives; it covers representation, preview, feedback, and privacy. Use an existing preview tool or a static artifact rather than adding a custom server. Get the user's decision in the conversation, not through assumed browser click capture. If previewing is unavailable, offer a simpler representation. No companion scripts or service are required.

## Scope and Simplicity

- Start with the smallest useful outcome; exclude features that do not serve the stated goal.
- If the request contains independent projects, name them and agree which to tackle first.
- If new information changes an approved design, explain the change and get approval for the changed decision, not for unchanged details again.
- If investigation contradicts the proposed approach, reassess before building; do not patch around an invalid assumption.
- Do not turn a settled request into an interview, a document, or a plan merely because this skill was loaded.
