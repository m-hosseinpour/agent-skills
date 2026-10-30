# Code Review Report

Use this format when handing a review to the change's author or another reader. Write in the reader's language; preserve code identifiers, paths, and log text unchanged.

## Structure

1. **Subject:** one line describing the reviewed change.
2. **Verdict:** ready/not ready, with the main reason.
3. **Scope:** what the review covers and any important limits.
4. **Findings:** most serious first. For each, include:
   - **Problem:** what is wrong and where (file/line).
   - **Why it matters:** the concrete failure or cost.
   - **Action:** what change would address it.
5. **Confirmed:** important behavior or contract checked and found sound.

Use two severity levels in a handoff report:

- **Blocking** (internal blocking/serious): must be fixed before merge.
- **Important** (internal important/moderate): worth fixing; if left, state why.

Do not transfer internal nits or optional suggestions into the handoff report. Drop them unless they reveal a concrete issue that deserves one of these levels. Every finding should be easy to locate, understand, and act on without access to the reviewer's session. Avoid local-only evidence, process narrative, dates, and claims the reader cannot check.

```markdown
# [Short subject: what change was reviewed]

**Verdict:** [Ready / Not ready] — [one or two sentences stating the main reason]

**Scope:** [what this review covers; mention important exclusions or limits]

## Findings

### [Blocking / Important] — [short title]

- **Problem:** [what is wrong, with file and line]
- **Why it matters:** [concrete failure or cost]
- **Action:** [what change would address it]

## Confirmed

- [Important behavior or contract checked and found sound]
```
