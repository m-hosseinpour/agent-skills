# Designing Verification that Can Catch a Mistake

Open when designing a focused reproduction/test or judging whether existing tests cover a changed behavior (for weakened assertions, circular mocks, or lint/type suppressions in test and config diffs, also see [test quality in patterns.md](patterns.md#test-quality-would-a-realistic-mistake-fail)). This expands verification within a review; it does not authorize fixes, a new framework, or writing outside approved paths.

## Choose the Behavior Before the Test

Derive expected results from the requirement, external contract, or independent working example before reading the implementation's output. Identify the shipped entry point and the relevant observable result: response, denied side effect, saved state, event, or user interaction. A helper's low-level contract can deserve its own test, but cannot by itself prove the feature reaches that helper.

Choose only cases that can change the assessment: the intended flow, a plausible failure, and an important boundary where applicable. For authorization, include the forbidden operation and absence of its side effects; for retry/concurrency changes, include the relevant duplicate/order behavior. Do not create a Cartesian product of imaginary inputs or require every category for a tiny change.

## Make the Check Discriminating

- Ask which realistic implementation mistake the check should catch and which assertion would fail. A matching test title or a mock being called is not enough.
- Keep the boundary under investigation real. Mock unrelated services when useful, but do not mock away the authorization, transaction, parser, or integration seam being assessed.
- For a demonstrated bug, show the check catches the original failure when safe, then repeat on the correction. For an existing test, inspect its assertions; an authorized isolated mutation experiment can resolve uncertainty, but is not mandatory and must not overwrite user work.
- Control relevant timing, fixtures, test order, and data ownership. A single isolated pass does not reproduce a shared-process pollution or intermittent failure. For stateful or asynchronous UI/client changes, control completion order (or target switch, dismissal, or unmount during an in-flight operation) and assert both visible and persisted state so stale completions or lost edits fail the check.
- For recurring/resumable work, run the shipped entry point again with the first run's persisted effects retained and relevant clock/queue progress controlled. Check both eligibility and observable work: a second-run no-op can still rescan or enqueue the same finished records. Expect exclusion of completed work or the contract's intentional reprocessing, not universally an empty result. Include newly eligible data when it distinguishes the intended behavior.
- When downstream workers finish the operation, enqueue counts alone do not prove completion. Exercise a relevant partial-dispatch or worker-failure path and verify unfinished work remains recoverable after the next sweep/retry/reconciliation; distinguish a pending/dispatched marker from an actual success marker. Keep this boundary real rather than mocking every worker as successful.

For example, an account limit test needs two users in the same account: a per-user implementation can pass every single-user case. Establish the expected account-wide result independently, and exercise the actual entry point. One targeted case can expose more than many happy-path assertions.

## Bound Writes and Execution

Follow the project's existing test approach. Without a framework, use exact manual steps or an authorized disposable check rather than scaffolding one. Before trusting an executed check, confirm it runs against the reviewed code state: check that unstaged working-tree edits do not alter a staged-only or commit-range review, and that compiled artifacts, containers, workers, or running servers have built and loaded the reviewed revision rather than stale code. Inspect scripts before running them; tests may change databases, generated files, caches, services, or external accounts even when the source checkout is read-only.

A review-and-test request may authorize verification artifacts in an isolated scratch area or explicitly approved test paths, not production fixes. Preserve the reviewed version and distinguish added verification code from the implementation under review. Get additional approval for unapproved dependencies, shared-state setup, destructive operations, or uploads. A scratch checkout does not isolate its database or credentials. Leave test data/artifacts according to user and project rules; do not assume teardown is authorized.

If writes are unavailable or denied, use existing checks or a source trace and state the verification limit. Do not bypass permissions via shell, another tool, or a worker.

## Report Evidence, Not Confidence Alone

Record the behavior tested, exact command or steps, outcome, relevant environment and code state, and paths/artifacts created. Distinguish proposed checks, inspected tests, and executed results. Trust adequate current evidence rather than rerunning it for ceremony. Separate independently established baseline failures from regressions, and revisit only evidence invalidated by later changes.
