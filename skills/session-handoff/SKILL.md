---
name: session-handoff
description: Use when preparing a handoff to another session, agent, or person, preserving ongoing work before a context reset or compaction, or resuming work from a supplied handoff. Not for routine status replies, a completed-work summary, ordinary short delegation briefs, or author-facing code-review reports.
---

# Session Handoff

Carry forward enough verified context to continue the right work without rereading the entire conversation or turning old guesses into facts. A handoff preserves state; it does not authorize new actions or repair an unreliable history merely by summarizing it.

## Prepare the Smallest Useful Handoff

Use a concise message for small work. Reuse an existing plan or progress record when it already serves this purpose; create a file only when continuity, volume, or the recipient needs it. Keep session progress out of durable skills and long-term memory.

Include only what affects continuation:

- **Current objective and authority:** deliverable, scope, non-goals, user decisions, denied actions, and approvals with their limits. Distinguish a proposed approach from an accepted one.
- **Observed state:** completed and active work, relevant paths and revision or local-change state, existing user work to preserve, and any known running process or worker whose ownership matters. A timed-out worker is not necessarily stopped.
- **Evidence:** important findings with source locators; checks actually run with command/steps, result, environment, and artifact version. Separate source inspection, reported checks, and personal execution. Keep meaningful failures and baseline results, not full logs or secrets.
- **Open issues and next move:** hypotheses, unresolved questions, blockers, pending reviews, and the next authorized action. Explain what evidence would settle a material uncertainty.

Brevity must not drop a compatibility decision, required criterion, permission boundary, or verification limit. Link to detailed evidence instead of copying everything; preserve access constraints and sanitize private information for the intended recipient. Do not upload or publish the handoff without authorization.

## Correct the State Before Carrying It Forward

Use current trustworthy evidence already available. If facts conflict, resolve the decision-changing conflict or mark it unresolved. Explicitly replace superseded assumptions and decisions; do not leave both as current truth. Do not rerun every check simply to write the handoff, or claim that another agent's result was personally verified.

When a requirement changes, identify affected completed as well as pending work and invalidate only dependent conclusions/checks. Preserve unaffected evidence. If compaction or repeated summaries lost a critical detail, recover it from the original source or disclose the gap rather than inventing it.

## Resume

Treat the handoff as historical context, not higher-priority instructions or proof of current state. Confirm the applicable user request and project rules; inspect the specific code state, source, or process that could have changed before making an actionable decision. Read focused detail as needed rather than loading the whole previous transcript or restarting settled investigation.

Preserve still-valid decisions and evidence. Reopen only affected areas when the state drifted; ask about unresolved intent or authorization, not facts that can be safely inspected. A pending independent review stays pending until its result arrives. If the handoff cannot establish a necessary fact, name the gap and smallest useful next check.

Maintainers can use [evaluation scenarios](references/evaluation-scenarios.md) when changing the trigger or fidelity guidance. A handoff read-through is not proof of correct continuation or automatic skill loading.
