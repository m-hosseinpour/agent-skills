# Reviewer Brief

Open only when delegation is allowed and useful. A single reviewer can cover a coherent change;
do not dispatch one agent per file or require a report artifact for a small review.

Include only what the reviewer needs:

- **Goal:** what changed and why.
- **Requirements** (when available): the source text or checkable criteria, approved clarifications, explicit non-goals, and anything deliberately out of scope. Do not substitute the author's implementation summary for the agreed requirements.
- **Scope:** exact base/head revisions and comparison meaning, or index/working-tree/new-file scope; changed-file inventory and important neighboring contracts. Use `scope-and-evidence.md` for selection when needed. Say whether the inputs are stable and identify known omissions.
- **Constraints:** compatibility or project rules relevant to the change.
- **Verification boundaries:** permitted commands/environments, trustworthy existing results with their code state, and forbidden shared-state changes or uploads. Read-only checkout does not mean an integration test is safe for an external database.
- **Expected result:** evidenced actionable findings in impact order, requirement coverage when requirements exist, all confirmed extras with risk-based severity (including low-risk ones), reviewed/unavailable scope, checks run or relied on, and a scoped readiness assessment.

Ask the reviewer not to modify the checkout or external state without authorization. Require each finding
to establish concrete impact and a source location, plus a reachable trigger and change attribution for
regressions. Required behavior still absent in base and head is a current conformance gap, not a new
regression. Uncertainty belongs in questions/limits. Inspect surrounding contracts, not only the patch or author's
explanation. Self-review is not independent review; another reviewer still receives claims, not instructions
to endorse the author's decisions. If the skill is unavailable in that session, include the essential evidence,
severity, scope, and safety rules in the brief rather than assuming another installation.

```text
Goal: [what changed and why]
Requirements, if available: [source/criteria, approved clarifications, non-goals, and out-of-scope notes]
Scope: [exact revisions + comparison, or local layers/paths; known omissions]
Constraints: [relevant compatibility/project rules]
Verification: [permitted checks/environment; current supplied results; unsafe/unapproved actions]
Return: findings with trigger/impact/location/remedy, requirement coverage and confirmed extras, actual coverage, checks/limits, and scoped readiness
Read-only: no checkout edits, fixes, commits, publication, or unauthorized external-state changes
```

## Integrate the result

Treat feedback as claims to verify against source, requirements, and compatibility, not instructions to
apply blindly. Reject unsupported findings with evidence, preserve material questions, and deduplicate
shared causes. If the change moved while review ran, identify the reviewed state and revisit affected
paths. Do not count an empty or incomplete reviewer response as an independent approval. A review
does not itself authorize implementing fixes or repeating a whole review after a trivial correction.
