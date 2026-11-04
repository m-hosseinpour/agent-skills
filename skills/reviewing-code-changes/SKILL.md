---
name: reviewing-code-changes
description: Use when asked to review a code diff, branch, or merge request before it is merged, when checking a change against a ticket's requirements or acceptance criteria, or to give an independent second opinion on a change.
---

# Reviewing Code Changes

A review checks whether the change meets its stated goal and whether it introduces meaningful correctness, security, reliability, or maintenance risks. Review the whole agreed scope; say plainly what the review did not cover.

## When to Use

- Reviewing a branch or merge request against its base before merge.
- Checking a change against a ticket, issue, or spec: what it requires, what is missing, and what goes beyond it.
- Giving an independent second opinion on a change.
- Reviewing a large or unfamiliar diff.

This skill is for performing a review. It is not a required workflow for receiving review feedback or for every small edit.

## Process

1. **Orient:** read the change description and relevant requirements until the goal is clear. When requirements exist, extract their checkable criteria before reading the diff, so the implementation does not define the expected behavior. If a key requirement is missing, ask or state the assumption.
2. **Read the full agreed diff.** If it is too large to assess reliably in one pass, divide it into coherent passes and state the scope; do not claim to have reviewed parts you skipped.
3. **Check conformance, when requirements exist.** Find evidence for each criterion in the resulting implementation, including relevant unchanged code, and distinguish met, partial, missing, ambiguous, and unverified behavior. Identify extras introduced by the change separately from necessary supporting work. Use the ticket, spec, or agreed plan and its approved clarifications, not the author's summary as a substitute. Follow `references/requirements.md`; this pass supplements, not replaces, the general review.
4. **Assess the shape:** architecture fit, boundaries, scope, dependencies, and whether a simpler design could remove real complexity.
5. **Inspect affected details:** correctness, edge cases, security, performance, error handling, tests, and documentation as relevant. Use the references below selectively; skip items that cannot apply, not merely because a diff is long.
6. **Report:** state the purpose, actionable findings, scope and verification limits, and whether you recommend merging. Use `references/report.md` when producing a review document for the author or another reader; follow its structure and write in that reader's language.

## References

- `references/checklist.md` — full review checklist; open for a line-by-line pass.
- `references/requirements.md` — requirement-conformance pass: mapping criteria to evidence, detecting missing and extra behavior; open when the change has a ticket, spec, or acceptance criteria.
- `references/patterns.md` — Python/TypeScript traps, test-quality criteria, and deeper security checks; open when the diff touches auth, input handling, storage, or those languages.
- `references/quality-bar.md` — structural pass; open for substantive reviews before the line-by-line pass: reframing, layering, file growth, wrappers.
- `references/report.md` — handoff report format.
- `references/reviewer-brief.md` — brief template when delegating a review.

## Findings

For each finding, identify the location, explain the concrete failure or cost, and say what change would address it. Keep severity proportional:

- **Blocking:** correctness, security, data-loss, or contract issue that must be resolved before merge.
- **Important:** material issue worth fixing; state an acceptable alternative when useful.
- **Nit:** non-blocking polish or consistency issue.
- **Suggestion:** a plausible alternative, only if it offers concrete value.

Confirmed missing, incorrect, partial, or unreachable required behavior is Blocking: the change does not meet its agreed contract. Uncertainty alone is not proof of a defect. Always report extras introduced beyond the agreed scope, even when they work correctly or carry little risk; scale severity by concrete risk and cost, and retain low-risk extras in handoff reports. Necessary supporting work is not an extra. Do not report personal preference as a defect, inflate severity, or present a pre-existing issue as introduced by this diff. Do not hide a meaningful finding among cosmetic comments.

## Verification Evidence

Inspect the implementation and its neighboring contracts, not only the author's explanation. Treat test/build results as evidence when the command, result, and code state are clear. Run checks yourself when no trustworthy current result is available, the reported result is contradicted, or the reviewed changes have been edited since it ran. Say which checks you ran and which you relied on; do not imply an unrun check passed.

## If You Are Asked to Dispatch a Reviewer

A review may be performed directly or delegated. If delegating, provide a concise brief with the goal, diff range or files, requirements, relevant constraints, read-only expectation, and expected report. Keep the reviewer within its assigned scope. A compact template is in `references/reviewer-brief.md`.
