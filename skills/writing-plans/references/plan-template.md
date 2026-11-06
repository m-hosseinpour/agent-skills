# Adaptable Implementation Plan

Read when a durable plan or task handoff needs a starting layout. Keep only sections that serve the work; a small request may need just a few checklist items in chat. Follow project conventions instead of introducing a new document structure by default.

The main `SKILL.md` owns the planning rules. This template supplies an output shape, not additional gates. Replace placeholders with checked facts or explicitly bounded uncertainty; do not present an unfinished template as a ready plan.

```markdown
# [Change] — Implementation Plan

## Outcome and scope
- Goal:
- Non-goals:
- Acceptance criteria: [stable labels for observable outcomes]

## Starting context and approach
- Relevant request/design record and project instructions:
- Starting revision/state and affected areas:
- Chosen approach and important trade-offs: [or link to the authoritative design]
- Verified interfaces and compatibility constraints: [source when needed]
- Assumptions and blockers: [consequence, resolver, dependent work]

## Tasks

### T1 — [Coherent outcome]
- Result: [what becomes true; acceptance criteria covered]
- Scope: [known paths and responsibilities; label proposed new files]
- Depends on: [task IDs, decisions, or required evidence; none if independent]
- Actions: [meaningful implementation steps, not a full code recipe]
- Verify: [existing check or manual flow, expected result, relevant failure case]

### T2 — [Next coherent outcome]
...

## Integration and completion
- Combined behavior and interface checks:
- Acceptance criteria coverage: [criterion -> task/check]
- Known verification gaps and how they will be resolved:

## Rollout or recovery [only when relevant]
- Compatibility, data preservation, rollout order:
- Rollback/recovery limits and required authorization:

## Handoff or progress [only for ongoing work]
- Task status and evidence for completed work:
- Outstanding decisions/blockers:
- Next authorized action:
```

## Example Task: Clear Without Writing the Implementation

The paths and contract below are illustrative, not facts about the current project. Assume inspection has confirmed them and the user has agreed to the new contract:

> **T2 — Move the checkout consumer to the agreed money contract**
>
> - Result: the checkout shows the correct amount and currency for accepted responses.
> - Scope: `src/checkout/summary.ts` and the existing checkout checks; no producer changes.
> - Depends on: T1's verified `{amountMinor: integer, currency: string}` response and the agreed minor-unit conversion policy.
> - Actions: replace the old `total` consumption and route formatting through the existing money formatter.
> - Verify: the existing checkout flow with `{amountMinor: 1234, currency: "USD"}` displays `$12.34`; exercise the existing error path for unavailable totals; the integration check confirms the producer and consumer agree.

This pins the consequential input, behavior, and dependency. It leaves routine coding choices to the implementer. If the conversion policy or error behavior were unsettled, T2 would be blocked on that decision rather than guessing it.
