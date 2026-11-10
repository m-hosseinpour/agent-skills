---
name: writing-implementation-plans
description: Use when asked to write, review, or update an implementation plan; when substantial cross-component changes, migrations, or high-risk work need coordinated steps and checks; or when preparing multi-session or cross-owner implementation work or resuming from a potentially stale implementation plan. Not for routine local edits without a plan request, executing a current settled plan, design-only exploration, or non-implementation handoffs.
---

# Writing Implementation Plans

A useful plan lets an implementer start the right work, in the right order, without guessing consequential decisions. It connects the agreed outcome to bounded tasks, dependencies, and observable checks. Detail should prevent a costly mistake or lost context, not prescribe every coding move.

This skill is self-contained and focuses on writing, reviewing, and maintaining plans, not managing the entire implementation. Loading it does not authorize implementation, delegation, publishing, or destructive actions.

## Choose the Smallest Useful Artifact

- **No new plan:** a routine, local change with obvious steps, or execution of an existing plan that still matches the project and requirements. Do not plan merely because several files or steps are involved.
- **Short checklist:** a small explicit planning request or a clear single-session task that needs a little sequencing. Chat may be sufficient.
- **Durable plan:** work with meaningful cross-component dependencies, staged migration or rollout, costly failure, or context that must survive a session or ownership change. A short but risky change can qualify; size alone is not the test.

Reuse an existing plan and follow the project's document conventions. Save long-lived plans where future implementers can find them; if the location or a new document convention is unsettled and matters, ask rather than inventing a directory or filename convention. A template is not a requirement to create a file.

Keep the agreed approach in the plan unless a separate design/spec is already maintained or has a distinct audience or purpose. Do not create a spec merely because a plan exists. For a separate design record, read [references/spec-template.md](references/spec-template.md); link to its authoritative decisions rather than duplicating them.

## Ground the Plan Before Writing Tasks

1. **Establish the goal and authority.** Read the request, acceptance criteria, prior decisions, existing plan/spec, and relevant project instructions. Distinguish user decisions, verified facts, proposals, and assumptions. A planning-only request stops at the plan.
2. **Check the current project.** Inspect the affected code, documents, interfaces, and existing verification practice. Record exact known paths and the relevant starting revision or state for a handoff; label proposed new files as proposed. Do not invent paths, commands, API shapes, or a test framework.
3. **Resolve decision-changing gaps.** Investigate relevant dependencies, failure behavior, compatibility, security/privacy, persisted data, and operational constraints. Get external API facts from authoritative docs or an authorized focused probe. Ask about material user choices before scheduling dependent implementation; `structured-reasoning`, if available, can help resolve design choices but is not a prerequisite.
4. **Bound remaining uncertainty.** State low-risk assumptions and their consequences. If a technical fact cannot yet be verified, add a bounded investigation task with a question, evidence required, and the work it blocks. Do not call the dependent work ready or disguise an unsettled design as an implementation task.

Use existing evidence when it still describes the current state; do not repeat investigation just to fill a template. A bug whose cause is unknown needs diagnosis before a fix plan, not a guessed solution.

## Build Tasks Around Outcomes and Dependencies

Map affected areas, shared files/resources, and producer/consumer contracts before splitting work. Group tightly coupled edits; sequence tasks that need another task's output. Mark tasks parallelizable only when their inputs are settled and their writable resources do not conflict. Planning independent units does not require delegating them.

The plan should capture:

- **Outcome and boundaries:** goal, non-goals, observable acceptance criteria, and the chosen approach or link to it.
- **Current context and constraints:** relevant sources, verified contracts, compatibility limits, bounded assumptions, and unresolved blockers.
- **Tasks:** for each coherent unit, a stable ID, outcome, affected paths/responsibilities, dependencies or required inputs, meaningful actions, and verification with an expected result. Include an owner only when ownership matters or is already agreed; do not invent workers.
- **Integration:** which task or milestone checks the combined behavior and shared interfaces. Trace each acceptance criterion to a task or final check so local completion cannot hide a missing end-to-end outcome.
- **Risk-dependent safeguards:** where relevant, data preservation, old/new version coexistence, rollout order, rollback or recovery limits, and actions needing explicit authorization. Preserve a performance or behavior baseline before removing the way to measure it.

A task should be finishable and checkable as a coherent unit, not necessarily independently runnable. Avoid a task per file, arbitrary minute estimates, full implementation bodies, and commands for every edit. A contract, example input/output, pseudocode sketch, or exact verification command is useful when it removes a consequential ambiguity; syntax or block length alone does not make it excessive.

For a starting layout, read [references/plan-template.md](references/plan-template.md) when drafting a durable plan or task handoff. Omit irrelevant sections; the contents above matter more than the headings.

## Make Verification and Review Useful

- Specify behavior and expected results, not just “run tests” or “works.” Cover relevant failure paths and integration seams using the project's existing practices. If there is no framework, use an appropriate manual flow or focused check; introducing a framework is a separate choice.
- Record known baseline failures and unavailable checks honestly. A planned command is not a result, and missing evidence is not proof of a defect. If a gap affects readiness, name what must resolve it before dependent work starts or completion is claimed.
- Self-review requirement coverage, dependency order, contract consistency, feasible checks, unnecessary scope, and unresolved decisions. If the plan introduces a consequential choice, get the user's decision; merely recording an approved approach does not need another approval round.
- For a large or high-stakes plan that warrants an independent review, use one read-only reviewer **only when delegation is available and allowed**. Read [references/plan-document-reviewer-prompt.md](references/plan-document-reviewer-prompt.md) at that point. If a reviewer is unavailable or prohibited, do the self-review and report that limit. Reviewer readiness is not user authorization.

## Handoff, Resume, and Change

Leave one current plan, linked decisions, and the next authorized action. For multi-session work, use one progress record, optionally the plan itself: pending, blocked, in progress, or completed **with evidence**. Include outstanding blockers and the next task; avoid competing ledgers. If delegation is chosen and allowed, `dispatching-parallel-agents`, if available, covers safe ownership and dispatch, not the plan template.

On resumption, compare the plan and recorded progress with current requirements, code state, and relevant checks before treating old items as current. Do not rewrite an unchanged, settled plan or redo still-valid work merely to restart.

When a requirement, decision, path, or interface changes:

1. Identify affected pending, active, **and completed** work, including integration checks and documentation.
2. Update the authoritative decision and affected plan items. Notify active implementers before they continue dependent work; revise pending briefs and reopen completed work when needed.
3. Reverify the behavior affected by the change. Prior checks remain evidence only for artifacts and assumptions they still cover.
4. Correct stale live references without erasing useful historical context; label retained old decisions or results as superseded snapshots, not current instructions.

## Evaluating This Skill

When revising discovery or planning guidance, use [references/evaluation-scenarios.md](references/evaluation-scenarios.md) for optional metadata-selection and plan-quality cases. These are maintainer inputs, not a ritual during ordinary planning. Installer discovery does not prove automatic loading, and a decision simulation does not prove implementation success.
