# Requirement Conformance

Use this pass when the change has a ticket, issue, spec, or acceptance criteria. It systematically checks both directions: is every stated requirement implemented, and does the change introduce behavior beyond the agreed scope? Continue the general review as well.

When only a vague description exists, state the assumptions you reviewed against instead of inventing acceptance criteria, and say so in the report.

## 1. Build the requirement list

Read the requirement text and approved clarifications before the diff, so the code does not frame what you look for. Keep their source identifiable; the author's implementation summary cannot silently expand the agreed scope. Turn the requirements into separate, checkable statements:

- One line per behavior, not per ticket bullet — a bullet often holds several criteria.
- Include stated edge cases, error behavior, limits, permissions, and compatibility requirements.
- Record explicit non-goals and "out of scope" notes, when present, as scope constraints. Extras can exist even without an explicit non-goal.
- Mark contradictions and genuine ambiguities instead of resolving them yourself. If two readings both satisfy the text, that is a question for the author, not a guess.

## 2. Find evidence for each

A requirement is met only when the shipped path reaches behavior matching the criterion. Inspect the resulting implementation and relevant unchanged code, not just added lines: a requirement may already be satisfied in the base. Evidence can be a traced code path, a test's actual assertions, or a migration, config, or doc when the requirement concerns those. Distinguish static inspection from executed checks; do not imply a test ran merely because you read it.

Commit messages, branch names, and test titles are claims, not evidence. Record the evidence location (file:line) as you go; the report needs it.

## 3. Classify

| Status | Meaning |
| --- | --- |
| Met | Reachable, observable, and matches the requirement including its stated edge cases |
| Partial | Implementation exists but does not fully match the criterion: incorrect behavior, coverage on only some paths, or a missing edge case, limit, or stated variant; state exactly what fails |
| Missing | No implementation, or code exists with no reachable path to it |
| Ambiguous | Implementation plausible, requirement reads two ways; ask instead of grading |
| Unverified | Required code, configuration, or runtime evidence is unavailable; state the gap rather than calling it missing or met |

A non-goal is not graded like a requirement: mark it **Violated** when the diff implements it and **Respected** when it stays out. Never fail a change for leaving a non-goal alone.

## 4. Look for extras

List behavior in the diff that no requirement traces to, then separate it from work the change genuinely needs:

- **Supporting work** — refactoring, tests, migrations, docs, or dependencies reasonably needed to deliver and verify the requirement safely under existing project contracts. Explain the connection; a file type alone does not justify unrelated work. Not an extra.
- **Extra** — a new endpoint, flag, option, config key, permission, user-facing text, or validation beyond the ask; behavior of touched code changed beyond the ticket; an unrelated fix or feature carried along.

Compare with the base so unchanged behavior is not mislabeled as an extra introduced by this diff. Approved scope changes are requirements, not extras; an author's claim of approval is not a substitute for the agreement. If scope is genuinely unclear, ask and report the uncertainty rather than declaring a confirmed extra.

Always report confirmed extras. For each, explain the scope mismatch and concrete risk or cost; recommend removal, separation into another change, or explicit scope approval. An explicit non-goal is strong evidence of a mismatch, but severity still depends on the risk and whether it is a hard acceptance constraint.

Also check the inverse: a requirement that changed an existing behavior, where the old behavior still runs beside the new one.

## 5. Severity

- Confirmed missing, incorrect, partial, or unreachable required behavior: **Blocking** — the change does not meet its agreed contract.
- Extra functionality: severity follows concrete risk, not mere presence. **Blocking** for a hard acceptance-constraint violation or risk that must be resolved before merge, such as an authorization bypass, data-loss risk, or incompatible contract change; **Important** for material maintenance cost or unintended behavior; **Nit** for a low-risk scope mismatch with no material impact. Merely touching persisted data or adding an endpoint is not automatically Blocking. Always include the extra in the report, even at Nit severity.
- Ambiguous or unverified is not a severity. State the unresolved question or missing evidence and its effect on readiness; do not claim conformance while material criteria remain unresolved.

## Return coverage evidence

Return every criterion and scope constraint with its status, evidence location, and any gap or unresolved question. List extras separately with their evidence and severity; do not invent requirements for behavior nobody requested. Write a normal finding for every Partial, Missing, Violated, and confirmed extra: location, scope mismatch or concrete failure/cost, and the change that would address it. The handoff format belongs to `writing-code-review-reports`; the conformance pass must supply the evidence it needs, including low-risk extras.

## Traps

- Grading a requirement met because a test with a matching name exists — read what the test asserts.
- Turning implementation details into requirements: the ticket says what the product must do, not which function to add.
- Reporting necessary refactoring as scope creep, or an unrequested feature as "part of the change".
- Skipping the pass because the diff is small; small diffs are where a missing requirement hides.
- Treating the author's summary as the requirement. Use the agreed source and approved clarifications; note discrepancies rather than silently adopting the summary or ignoring an approved scope change.
