# Reviewer Brief

Use this when delegating a read-only review to another agent.

Include only what the reviewer needs:

- **Goal:** what changed and why.
- **Requirements** (when available): the source text or checkable criteria, approved clarifications, explicit non-goals, and anything deliberately out of scope. Do not substitute the author's implementation summary for the agreed requirements.
- **Scope:** base/head revisions or exact files, and any important neighboring contract.
- **Constraints:** compatibility or project rules relevant to the change.
- **Expected result:** actionable findings, requirement coverage when requirements exist, all confirmed extras with risk-based severity (including low-risk ones), what could not be verified, and a merge/readiness assessment.

Ask the reviewer not to modify the checkout. They should inspect the relevant diff and surrounding code, and report evidence for each finding. Do not require a fixed status vocabulary or a report file for a small review; use a file when the report is long or needs to be handed off.

```text
Goal: [what changed and why]
Requirements, if available: [source/criteria, approved clarifications, non-goals, and out-of-scope notes]
Scope: [base..head or paths]
Constraints: [relevant compatibility/project rules]
Return: actionable findings with evidence, coverage when requirements exist, all confirmed extras with risk-based severity, unverified scope, and readiness
Read-only: inspect only; do not change the checkout
```
