# Review Checklist

35 things to verify, each with the reason it exists. Adapted from the PR Review Canvas
(MIT, Alexandre Iglesias / Projekta2 — https://github.com/projekta2/pr-review-canvas).

Work through every category the diff could touch. Drop an item only when it cannot apply to this change,
never because the diff is long or the item feels unlikely.

IDs follow the source checklist, so gaps mark items dropped as redundant or hosted-PR-only.
`c5`, `a10` and `s5` are additions from the `thermos` review rubric (cursor/plugins, MIT).

## Context & Purpose

- **c1** Commits and the branch name say what changed and why — a reader a year from now needs intent without the tracker, and git blame matters most once context is gone.
- **c3** The diff does one thing: unrelated changes are visible and called out — scope creep hides the change that needed the attention.
- **c5** Deliberate breakage is stated and bounded — a removed feature, flag, or safeguard says what stops working and for whom; unannounced removal is indistinguishable from a bug.

## Architecture & Design

- **a1** Fits the existing architecture, or justifies the deviation, and introduces no new pattern where an existing one already solves it — silent drift creates five ways to do one thing.
- **a2** Responsibilities sit in the right layer — business logic in a UI component resists testing and reuse.
- **a4** Coupling between unrelated modules is minimized — tight coupling turns a five-minute fix into a four-file change.
- **a5** Abstraction level matches the problem — over-engineering a one-off costs as much as under-engineering reuse.
- **a7** Consistent with similar solved problems elsewhere — search for the existing one before accepting a second way to do it.
- **a8** New dependencies carry a justified trade-off — bundle size, maintenance, and license are real costs.
- **a10** Gated behaviour stays gated — a feature behind a flag or an internal-only check does not leak onto a path open to everyone, including error and fallback paths.

## Code Quality

- **q1** Naming, function size, magic values, duplication, control flow, and comments are visible while reading, so mention them in passing rather than hunting them: names should say the domain concept, one function one job, no raw literals, no avoidable duplication, flat control flow, comments that say why.
- **q2** No dead code, commented-out blocks, or debug statements — version control already remembers deletions.
- **q4** Error handling explicit, not swallowed, and not reported as success — an empty catch that still answers `ok` is a bug report waiting to happen.
- **q10** Edge cases visibly handled — the happy path gets demoed, the edge cases get paged.
- **q11** No reliance on implicit, fragile behavior — undocumented ordering or defaults are landmines for upgraders.

## Testing

- **t1** New behavior has a test when the project's existing test setup can cover it; do not require new tests or scaffolding a framework against project norms.
- **t2** Tests verify behavior, not implementation details — internals break on every refactor.
- **t3** At least one test covers the unhappy path — the golden path rarely causes incidents.
- **t4** Tests deterministic, no flaky timing or randomness.
- **t5** Bug fixes include a regression test when the project's test setup supports it; otherwise verify with a recorded reproduction and relevant available checks.

## Performance & Security

- **p1** No N+1 queries or loops over large collections — invisible with test data, catastrophic at scale.
- **p2** User input validated before touching anything sensitive — frontend validation is not a security boundary.
- **p3** Secrets not hardcoded or logged — once a secret hits version control, rotation is the only fix.
- **p4** New endpoints respect existing authorization rules — bypassing a permission check is privilege escalation.
- **p5** No new attack surface without a clear mitigation — file uploads and raw SQL are common entry points.
- **p6** Memory and resource usage bounded — unbounded caches work in dev and fall over in production.
- **p7** Third-party data treated as untrusted — "it's a partner API" is not "safe to trust".

## Documentation

- **d1** Public functions and endpoints documented where intent is not obvious.
- **d2** README or API docs updated if usage changed — stale docs actively mislead.
- **d3** Breaking changes called out explicitly — nobody reads every line of every diff.
- **d4** Config and environment variable changes documented — an undocumented required env var is a guaranteed support ticket.

## Standards Compliance

- **s1** Follows the team's style guide and ADRs — a settled decision should not be re-litigated per change.
- **s2** Test/build evidence is current for the reviewed tree — run the checks yourself when reported results are absent, stale, contradicted, or the tree changed; otherwise state what was reported and what you did not rerun.
- **s4** Accessibility basics respected for user-facing changes — labels, contrast, keyboard navigation decide who it works for.
- **s5** Local run and build still work — a renamed env var, a moved secret, a remapped port, or a new required setup step breaks every developer, and is not an implementation detail.
