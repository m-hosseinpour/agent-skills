# Evaluation Scenarios

Use when revising this skill, not during normal planning. These are reusable inputs and expected behaviors, not completed test results. Evaluate discovery separately from the quality of the resulting plan.

## Discovery: Show Only Name and Description

Give a fresh evaluator the candidate name and description and the situations below, without the expected decisions or body. Ask for LOAD or SKIP and a brief reason; do not execute the hypothetical work. Compare current and candidate metadata in separate fresh evaluations when practical, reporting missed cases and false positives.

| ID | Situation | Expected |
| --- | --- | --- |
| D1 | The user asks for a short implementation plan for a clear, local change; no code yet. | LOAD; explicit request, small artifact |
| D2 | Backend and frontend must move to a new response contract, with staged compatibility checks. | LOAD |
| D3 | A three-line migration drops persisted data; execution order and recovery limits matter. | LOAD; risk, not line count |
| D4 | Implementation work spans several sessions and will be handed to another owner. | LOAD |
| D5 | Resume an implementation plan written last month; requirements and some completed code have changed. | LOAD; check and update stale guidance |
| D6 | Review an existing implementation plan against supplied acceptance criteria. | LOAD |
| D7 | Correct a typo and apply a known formatter in two files; no plan requested. | SKIP |
| D8 | Execute the next task of a current, verified, approved plan; no new planning choice. | SKIP; existing plan is sufficient |
| D9 | Discuss possible product directions without choosing implementation or requesting a plan. | SKIP; design exploration |
| D10 | Explain what an existing plan says, without judging or changing it. | SKIP; explanation only |
| D11 | Apply one obvious rename across five files with no behavior or contract change; no plan requested. | SKIP; file count alone |
| D12 | The user asks to update a plan after an agreed API contract changes. | LOAD |
| D13 | Hand off a multi-session literature-summary report to another researcher; no implementation work or plan requested. | SKIP; a handoff alone is not implementation planning |
| D14 | Turn existing code-review findings into an author-facing handoff report; no plan request. | SKIP; reporting, not implementation planning |

The explicit D1 request overrides the routine-work exclusion. D8 does not prohibit loading when execution reveals that a plan is stale. Metadata decisions are evidence about selection, not a guaranteed loading rate across harnesses or models.

## Application: Supply the Full Skill and Needed Context

Ask a fresh evaluator to produce the next action and an appropriately sized plan or revision. Hide the expected behavior until scoring. Supply realistic project excerpts or allow scoped read-only inspection; no real implementation, database writes, or workers in these simulations. Score useful outputs, not repetition of the skill's wording.

### B1 — Small Explicit Request, Settled Decisions

The user requests a plan only for a label rename in one known component. The new label, path, and existing visual check are supplied. There is no document convention, and chat is sufficient.

**Expected:** a short checklist with the change and expected visual result. No interview, separate spec, durable-plan directory, implementation, delegation, or new framework.

### B2 — Coupled Contract Change Under Deadline Pressure

The user wants a plan for changing an API response from `{total:number}` to `{amountMinor:integer,currency:string}` and updating checkout. Inspection confirms producer/consumer paths and an existing money formatter and checkout check. The minor-unit policy is agreed; older clients remain supported during rollout. “Split every file into a parallel task; we need this fast.”

**Expected:** coherent tasks with settled inputs, producer/consumer sequencing or compatible staging, relevant shared ownership, old/new compatibility, exact known paths, observable money-format expectations, and a combined contract check. No invented files or a worker per file. Keep implementation bodies out while retaining useful contract evidence or check commands.

### B3 — Unverified API and No Test Framework

A third-party integration needs a durable handoff plan. Local configuration identifies the integration location, but the API shape and failure behavior are unavailable from permitted inputs. The project has manual checks and no test framework. The user says, “Just assume a conventional JSON response and give me a ready-to-code plan.”

**Expected:** do not invent the schema, endpoint, paths, or test command. Include a bounded documentation/probe investigation with required evidence and blocked consumers; state the readiness limit and authorization for any live probe. Plan existing manual or focused verification with expected behavior once the contract is known. Do not scaffold tests or require another skill to proceed.

### B4 — Stale Plan and Completed Work

A saved plan shows the API task complete with checks for `{total:number}`. The consumer is active, docs pending. Requirements now specify `{amountMinor:integer,currency:string}`. Current code excerpts and old check evidence are supplied; the new contract is agreed.

**Expected:** compare current state, reopen affected producer work, update the active consumer scope and pending docs, correct contract and acceptance references, and require new combined verification. Preserve unaffected completed work and distinguish old evidence from verification of the new contract. One current progress record, not a full rewrite or a second ledger.

### B5 — Risky Small Migration

A three-line migration drops an old column containing persisted records. Existing readers still use it; backup/recovery capability has not been established, and the request is for a plan only.

**Expected:** treat risk as sufficient for planning; identify data/reader dependencies, preservation and recovery questions, compatibility/rollout order, verification, and destructive authorization boundaries. Do not call the drop ready while those prerequisites remain unresolved; do not execute it or pretend rollback restores erased data.

### B6 — Review Without Arbitrary Code or Approval Gates

A plan includes an eight-line verified response example, a one-line existing verification command, and a small pseudocode sketch that clarifies behavior. It links to an approved design instead of copying it. One dependent task is explicitly blocked on an investigation. Subagents are prohibited.

**Expected:** self-review with stated limits; do not dispatch or require a fresh user approval of settled choices. Judge blocks by purpose, not line count or executability. Distinguish legitimate investigation from ready dependent implementation; assess requirement coverage and expected checks rather than rejecting useful examples.

## Reference Navigation

A representative reader should be able to find:

- The adaptable plan/task output shape from **Build Tasks Around Outcomes and Dependencies**.
- The separate design record only when **Choose the Smallest Useful Artifact** establishes a distinct need.
- The read-only reviewer prompt at the independent-review decision in **Make Verification and Review Useful**.
- These maintainer cases from **Evaluating This Skill**, not as ordinary planning steps.

Check relative links and installer discovery mechanically. For simulations, record the tested revision, inputs, outputs, and skipped checks separately from live guidance. A read-through is not a behavior test; a plan simulation does not demonstrate real rollout, recovery, code correctness, or automatic loading in a running harness.
