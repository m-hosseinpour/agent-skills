# Reviewer Brief

Use this when delegating a read-only review to another agent.

Include only what the reviewer needs:

- **Goal:** what changed and why.
- **Requirements:** the acceptance criteria or agreed behavior.
- **Scope:** base/head revisions or exact files, and any important neighboring contract.
- **Constraints:** compatibility or project rules relevant to the change.
- **Expected result:** actionable findings, what could not be verified, and a merge/readiness assessment.

Ask the reviewer not to modify the checkout. They should inspect the relevant diff and surrounding code, and report evidence for each finding. Do not require a fixed status vocabulary or a report file for a small review; use a file when the report is long or needs to be handed off.

```text
Goal: [what changed and why]
Requirements: [plan, issue, or concise behavior]
Scope: [base..head or paths]
Constraints: [relevant compatibility/project rules]
Return: actionable findings with evidence, unverified scope, and readiness
Read-only: inspect only; do not change the checkout
```
