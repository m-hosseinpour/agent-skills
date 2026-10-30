# Plan Document Reviewer Prompt Template

Use this template when dispatching a plan document reviewer subagent.

**Purpose:** Verify the plan is complete, internally consistent, and ready for implementation. If the project has a spec, check the plan against it too.

**Dispatch after:** The complete plan is written.

```
You are a plan document reviewer. Verify this plan is complete and ready for implementation.

**Plan to review:** [PLAN_FILE_PATH]
**Spec for reference:** [SPEC_FILE_PATH] (include this line only when a spec exists; delete it otherwise)

## What to Check

| Category | What to Look For |
|----------|------------------|
| Completeness | TODOs, placeholders, incomplete tasks, missing interfaces |
| Spec Alignment (only when a spec exists) | Plan covers spec requirements, no major scope creep |
| Task Decomposition | Tasks have clear boundaries, interfaces are pinned |
| Implementable | Could a subagent with only its task brief build this without getting stuck? |
| Code Leakage | Does any fenced block contain implementation rather than a contract? |

## Code Leakage — check this explicitly

The plan is intent, not code. Flag any fenced block that could be copy-pasted and
run: a function body, a test body, an import list, anything with a loop, a `return`,
an `assert`, or longer than about five lines. A legitimate block is a signature, a
field list, a table of columns, or a one-line statement of behavior. Leaked code
means the work gets written twice, once here and once by the implementer.

Note: a plan may legitimately contain verified external facts — real API response
shapes, exact endpoint payloads. Those are captured evidence, not implementation.

## Calibration

**Only flag issues that would cause real problems during implementation.**
An implementer building the wrong thing or getting stuck is an issue.
Minor wording, stylistic preferences, and "nice to have" suggestions are not.

Approve unless there are serious gaps — missing requirements, contradictory
interfaces, placeholder content, or tasks so vague they can't be acted on.

## Output Format

## Plan Review

**Status:** Approved | Issues Found

**Issues (if any):**
- [Task X]: [specific issue] - [why it matters for implementation]

**Recommendations (advisory, do not block approval):**
- [suggestions for improvement]
```

**Reviewer returns:** Status, Issues (if any), Recommendations
