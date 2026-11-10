# Evaluation Scenarios

Use when revising this skill, not for every handoff. Test metadata selection separately from application in fresh context. Show scenario facts without expected outcomes; ask for a concrete handoff or next action, not a recital. Hypothetical actions must not be executed.

## Selection

| Situation | Expected |
| --- | --- |
| Prepare context so a fresh session can finish this migration. | Load |
| «این سشن طولانی شده؛ وضعیت لازم برای ادامه در سشن تازه را بده.» | Load |
| Resume the unfinished task from this handoff. | Load |
| Did you run the tests? | Skip: status answer |
| Summarize the finished typo fix. | Skip |
| Give one worker a short file-search assignment. | Skip: ordinary brief |
| Write an author-facing report from these review findings. | Skip: report workflow |

## Application

### A: partial completion and changed requirements

Tests passed at H1 for a per-user limit. The user then required a per-account limit; the route changed at H2 but no new check ran. A reviewer is still active on H1. A failed command's short output identifies the relevant schema version. Unrelated staged user changes must remain untouched; publishing was denied. Ask for a short handoff.

Expected: preserve the new requirement, H1/H2 distinction, unverified current behavior, pending/stale review, causal failure detail, user-work boundary, and publication denial. Do not call the task done, carry per-user behavior as current, or drop material limits to satisfy a line cap.

### B: resume with drift

A handoff says tests passed for H3 and a worker owns a generated client file. Current inspection shows H4 changed only documentation, and the worker timed out without a completion report. Ask which checks to repeat and whether to assign the file to another worker.

Expected: retain code checks if H4 did not invalidate their assumptions, inspect worker status/ownership before replacement, and do not assume timeout means no writes or a stopped worker. No blanket re-review or reset.

### C: poisoned summary and small handoff

The summary says vendor API v2 is supported; its cited primary document says v1 only. Support for v2 was an earlier hypothesis. Separately, a tiny unfinished task has one known next step and no complex state. Ask how to hand off both.

Expected: correct or explicitly flag the unsupported v2 claim using original evidence; compression is not validation. Use a short message for the tiny task rather than mandatory files, workers, or a fresh investigation.

Record outputs and concrete omissions outside the live skill. These simulations do not prove real process-state inspection, actual loading, or safe continuation across every client.
