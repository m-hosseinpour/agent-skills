# Evaluation Scenarios

Use these when revising the skill, not during normal dispatch. They separate discovery (will an agent load it?) from application (does it make useful coordination decisions?). They are reusable inputs, not a record of completed tests.

## Discovery: Show Only Name and Description

Give a fresh evaluator only the candidate name and description, plus the cases below. Ask for LOAD or SKIP with a short reason. Do not show the body or expected decisions; do not let the evaluator execute the hypothetical task.

| ID | Situation | Expected decision |
| --- | --- | --- |
| D1 | Checkout latency needs substantial backend-query, browser-rendering, and third-party-call investigations. Delegation is allowed, but no split has been chosen. | LOAD: assess plausible independent workstreams before choosing workers |
| D2 | The user explicitly requests parallel investigation of two independent bugs, with delegation allowed. | LOAD |
| D3 | One subagent will investigate logs while the coordinator independently inspects code; both are substantial tasks. | LOAD: coordinator plus one worker is parallel work |
| D4 | Fix a typo, rename a variable, and adjust a comment in one small function. | SKIP: multiple tiny steps do not warrant this workflow |
| D5 | Choose one schema contract, then update its sole consumer; no separate investigation or concurrent work is contemplated. | SKIP: one dependent workstream |
| D6 | Request one read-only reviewer and wait for its report without doing other work. | SKIP: sequential delegation |
| D7 | Two agents will implement UI and API concurrently against a settled contract and separate ownership. | LOAD |
| D8 | Read two short files with independent tool calls; no agents or substantial workstreams. | SKIP: tool concurrency alone |
| D9 | Investigate five test failures whose relationship is unknown; assessing possible work boundaries is the next decision and delegation is allowed. | LOAD: assess boundaries, not automatically one worker per failure |
| D10 | Three substantial research areas look independent, but the environment prohibits subagent use. | SKIP: delegation is not available and allowed |

Compare the current and revised descriptions with the same cases in separate fresh sessions when practical. Report false positives as well as missed opportunities. A single evaluator's choices are evidence, not a guaranteed loading rate across harnesses or models.

## Application: Provide the Full Skill

Ask a fresh evaluator to choose concrete next actions, ownership, and verification for the following cases. Hide the expected behavior until scoring. Do not launch real workers or mutate a real database for these simulations.

### B1: Tiny Tasks Under Mild Delegation Pressure

Twelve two-line edits affect one 60-line config module. The user says, “Use agents if that really saves time.” Delegation is allowed.

**Expected:** keep the coherent batch inline; avoid agent-per-edit and mandatory plan/report files; inspect the diff and use the relevant existing check.

### B2: Shared Reading, Not Shared Writing

Two substantial auth investigations ask separate questions: token expiry and retry behavior. Both need the same stable checkout; neither changes files or state.

**Expected:** allow concurrent read-only investigation of the same files; assign question ownership, stable input context, and evidence requirements. Do not serialize solely because paths overlap.

### B3: Hidden Mutable Resources

Three implementation workers have non-overlapping source files in a shared checkout, but their normal commands may all rewrite `api/generated.ts`, `package-lock.json`, and the same development database. The tool provides no automatic isolation and the deadline is close.

**Expected:** name owners for indirect writes and shared state. Launch only work that can respect those boundaries; reserve cross-cutting changes for an integration owner or sequence dependent work. Separate worktrees alone would not isolate the database. Respect project rules for retained test data.

### B4: A Contract Changes After Partial Completion

The API worker has completed and checked `{total:number}`. The UI worker is active; the documentation worker is pending. The user changes the agreed response to `{amountMinor:number,currency:string}`.

**Expected:** reassess completed API output and reopen or assign follow-up; notify the active UI worker and establish the revised contract; update the pending documentation brief. Reverify affected producer/consumer behavior and live documentation; do not treat old checks as evidence for the new contract.

### B5: Timeout Is Not Proof of Quiescence

A worker times out after partial shared-checkout edits; whether it stopped is unknown. Another reports “done, tests pass” without commands or results. The coordinator has unrelated useful work available.

**Expected:** establish that the timed-out writer has stopped before handing its resources to a replacement; inspect partial changes and preserve user work; resume only remaining scope. Obtain evidence for the other worker's completion claim and verify relevant integration. Continue unrelated work outside reserved resources rather than duplicating workers or polling contrary to runtime rules.

## What These Checks Do Not Prove

Decision simulations do not demonstrate real parallel execution, tool isolation, recovery, or reliable loading in every agent. If a change makes claims about a particular runtime, verify those with that runtime's actual tools and a safely scoped task. Keep evaluation outputs separate from the live skill; record the tested revision and skipped checks when reporting results.
