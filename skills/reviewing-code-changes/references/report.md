# Code Review Report

Use this format when handing a review to the change's author or another reader. Write in the reader's language; preserve code identifiers, paths, and log text unchanged.

## Structure

1. **Subject:** one line describing the reviewed change.
2. **Verdict:** ready/not ready, with the main reason.
3. **Scope:** what the review covers and any important limits.
4. **Requirements** (only when stated requirements exist): use the coverage statuses in `requirements.md`, including ambiguity, unavailable evidence, and respected or violated scope constraints. Include evidence and verification limits. List confirmed extras separately with their severity. Missing, partial, violated, and extra behavior also appears as findings.
5. **Findings:** most serious first. For each, include:
   - **Problem:** what is wrong and where (file/line).
   - **Why it matters:** the concrete failure or cost.
   - **Action:** what change would address it.
6. **Confirmed:** important behavior or contract checked and found sound.

Use two severity levels for ordinary findings in a handoff report:

- **Blocking** (internal blocking/serious): must be fixed before merge.
- **Important** (internal important/moderate): worth fixing; if left, state why.

Do not transfer internal nits or optional suggestions into the handoff report, except confirmed extras: always retain those and label low-risk ones **Nit — scope mismatch** rather than inflating them to Important. Every finding should be easy to locate, understand, and act on without access to the reviewer's session. Avoid local-only evidence, process narrative, dates, and claims the reader cannot check.

Omit the Requirements section when the change had no stated requirements.

```markdown
# [Short subject: what change was reviewed]

**Verdict:** [Ready / Not ready] — [one or two sentences stating the main reason]

**Scope:** [what this review covers; mention important exclusions or limits]

## Requirements

| Requirement or scope constraint | Status | Evidence and limits |
| --- | --- | --- |
| [one-line criterion] | Met / Partial / Missing / Ambiguous / Unverified / Violated / Respected | [file:line, assertion/result, or unavailable evidence; distinguish inspected from executed] |

**Extras:** [confirmed behavior beyond the agreed scope, evidence and severity; or none found within the reviewed scope]

## Findings

### [Blocking / Important / Nit — scope mismatch] — [short title]

- **Problem:** [what is wrong, with file and line]
- **Why it matters:** [concrete failure or cost]
- **Action:** [what change would address it]

## Confirmed

- [Important behavior or contract checked and found sound]
```
