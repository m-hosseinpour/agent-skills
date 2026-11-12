# Follow-up Validation After Review

Open when a completed task has a prior review and the user asks to validate a revised delivery or
confirm fixes and task acceptance. This is an entry path into the main workflow, not a second review,
test-design, or reporting method. Use the stage owners named in `SKILL.md` throughout.

## Recover the Relevant Prior State

Start with the supplied prior report, its reviewed revisions/local scope, requirement coverage, findings,
and check results. Recover decisions and pivotal evidence from linked sessions or artifacts only where
the report does not establish them. Use `session-handoff` if actually resuming from a supplied handoff
or preparing continuation; don't load it merely because a previous review exists.

Establish the current target for each repository/component or research document, including vendored
copies, images, and configuration when relevant. A report date, branch name, or “nine new commits” does
not establish the comparison. Use the review owner's scope guidance to resolve it. If history was
rebased or prior local content is unavailable, identify the missing comparison/evidence; don't assume
the previous head is an ancestor or fabricate the old snapshot.

Reconcile the original task with approved subsequent decisions **before** grading fixes. The prior
report is evidence, not a new acceptance contract. Distinguish:

- A confirmed correction to implementation.
- An approved scope change that makes an old requirement inapplicable.
- An explicitly accepted risk/deviation that remains present.
- An author's unsupported “everything else is fine” or claimed approval.
- A prior criticism refuted by current reliable evidence.

An author's statement is not approval by itself; a decision explicitly adopted by the user counts.
Ask only when the unresolved distinction changes acceptance. Don't reopen settled decisions without
new evidence, silently broaden a risk acceptance beyond its stated scope, or label a superseded
requirement as a fixed bug.

## Use Two Connected Scopes

1. **Revision scope:** all changes from the last reviewed delivery to the current target, including fixes,
   refactors, tests, docs, configuration, and other additions—not only the lines named in old findings.
   Pass this scope to `reviewing-code-changes` (or the research owner for revised claims/content).
2. **Acceptance scope:** the current task as a whole under its approved requirements. Update the existing
   coverage map using still-valid prior evidence plus new evidence, including previously blocked or
   untested material paths. A clean fix diff alone does not establish task acceptance.

Neither scope requires rereviewing every unchanged file or rerunning every old check. Inspect the
changed behavior and affected unchanged contracts; broaden only where the change, new decision,
unreliable prior coverage, or evidence gap justifies it. A fix in one repository can invalidate tests of
an unchanged consumer or vendored copy in another. Conversely, preserve unaffected evidence when its
scope, provenance, and assumptions remain adequate.

If the user asks only to verify named fixes, respect that narrower scope and label the conclusion as
fix verification, not whole-task approval. Without completed-task context, use ordinary fix/change
review; clarify scope only if acceptance is genuinely ambiguous, not when the user already excluded it.
A request only to run listed tests or format settled findings
belongs to that operation, not this acceptance workflow. “Fix the report's issues” is implementation
work; an ambiguous “do the items in this report” requires distinguishing tests from code changes before
acting. Prior review instructions don't authorize fixes, setup, deployment, or destructive resets today.

## Account for Every Prior Finding

Keep a compact disposition list in the shared evidence/coverage record. Reuse existing identifiers or
short titles and original evidence locators; associate each with the current requirement, fix/change,
current evidence, and acceptance effect. Dispositions are **finding lifecycle**, not a new severity or
requirement-status rubric:

| Disposition | Required distinction |
| --- | --- |
| Resolved | Target-specific evidence shows the underlying failure is corrected on its material affected paths; label source/supplied/executed evidence accurately. A commit message or changed line alone is not closure. |
| Still open / Partially resolved | State the remaining trigger/path, not a copy of the old wording as if nothing changed. |
| Superseded by decision | Cite the approved scope change and which old requirement no longer applies; not an implementation fix. |
| Accepted deviation/risk | State the behavior still present and exact approval/limits; don't infer it from silence or classify it as fixed. |
| Prior finding refuted | Identify the evidence correcting the earlier criticism; don't pretend the product was fixed when the report was wrong. |
| Unverified at target | Current evidence cannot establish persistence or closure; name what resolves it. A historical blocker is not automatically a confirmed current blocker. |

Include confirmed extras and material coverage gaps from earlier rounds as well as bugs. Don't lose an
open item because its file was untouched or the author didn't mention it. New symptoms from a partial
fix may share the old cause; use the review owner's validation/grouping rules instead of multiplying
findings. For research, apply dispositions to claims, methods, and required experiment/evidence gaps,
preserving the distinction between reviewer verification and the colleague's required deliverable.

## Select Retests by What Could Have Changed

For implementation checks, use the code-review owner's `references/test-design.md` and the local
acceptance-verification guide. For research claims/experiments, use `research-with-evidence` plus local
acceptance-verification/completeness guidance; don't require a code-only method. For each material
correction or decision, identify:

- The old failure/reproduction and whether its expected result still applies.
- The current shipped entry point and meaningful adjacent/alternate path the fix might miss or break.
- Prior evidence that remains valid versus evidence invalidated by code, build, config, or scope changes.
- Necessary previously untested/blocked acceptance cases and what now permits them.

Reproduce the corrected behavior at the level needed for the claim, not just the helper changed by the
fix. For example, a correct status API response after a manual refresh does not prove the final streamed
message and notification were correct before that refresh. Observe the user's original trigger, relevant
rendered outcome/side effects, and important continuation transitions. Judge tests by their assertions:
a budget-exhausted message alone cannot show that a rejecting verifier ever executed. If a model can
manufacture the requested “always failing” result, that is a flawed test premise, not necessarily a
product defect; use an independently controlled verifier appropriate to the agreed experiment.

Don't invalidate all prior evidence because time passed or a new round started. Don't reuse old green
results for materially changed paths. If a disk, network/access, credential, or resource blocker is
resolved, repeat affected failed/blocked checks without automatically restarting the entire campaign.
Distinguish setup failure from product failure. Check current project procedures and effective artifacts
before execution; remembered build/reset steps aren't current authorization or proof of runtime state.

## Close the Round Using the Existing Owners

Apply the main skill's risk-based independent-validation policy to unresolved or newly decisive claims;
the number of previous rounds doesn't itself require another reviewer. If continuing the same coherent
review, send only open findings and direct effects to the existing reviewer when appropriate. An earlier
independent approval covers its actual code/evidence state, not later changes.

Hand the applicable delivery owner the current target, acceptance map, disposition list, new/open
findings, executed versus retained results, and material limits. For code/mixed reports, the code-report
owner's consolidation guide handles historical/current claims and report structure. Pure research uses
the research owner's delivery plus local trust/completeness and handoff safety guidance, not code-only
consolidation. Don't copy the old report and merely replace its verdict.
Keep a concise closure summary distinct from active findings. Do not present superseded/refuted items
as product fixes or imply all paths ran because prior checks are being relied on.

Respect the user's report path/update request and existing conventions. Otherwise save a non-colliding
follow-up report, preserving the previous report as historical evidence; don't overwrite or rewrite old
rounds unasked. The report must assess the current acceptance scope, not just “all old items closed.”
If manual testing supplies a new failure after the report, reopen the affected finding, checks, and
acceptance conclusion and update the current report within authorization. Diagnosis or fixes remain
separate work with their own methods and permissions.
