# Designing Verification that Can Catch a Mistake

Open when designing a focused reproduction/test or judging whether existing tests cover a changed behavior. This expands verification within a review; it does not authorize fixes, a new framework, or writing outside approved paths.

## Choose the Behavior Before the Test

Derive expected results from the requirement, external contract, or independent working example before reading the implementation's output. Identify the shipped entry point and the relevant observable result: response, denied side effect, saved state, event, or user interaction. A helper's low-level contract can deserve its own test, but cannot by itself prove the feature reaches that helper.

Choose only cases that can change the assessment: the intended flow, a plausible failure, and an important boundary where applicable. For authorization, include the forbidden operation and absence of its side effects; for retry/concurrency changes, include the relevant duplicate/order behavior. Do not create a Cartesian product of imaginary inputs or require every category for a tiny change.

## Make the Check Discriminating

- Ask which realistic implementation mistake the check should catch and which assertion would fail. A matching test title or a mock being called is not enough.
- Keep the boundary under investigation real. Mock unrelated services when useful, but do not mock away the authorization, transaction, parser, or integration seam being assessed.
- For a demonstrated bug, show the check catches the original failure when safe, then repeat on the correction. For an existing test, inspect its assertions; an authorized isolated mutation experiment can resolve uncertainty, but is not mandatory and must not overwrite user work.
- Control relevant timing, fixtures, test order, and data ownership. A single isolated pass does not reproduce a shared-process pollution or intermittent failure.

For example, an account limit test needs two users in the same account: a per-user implementation can pass every single-user case. Establish the expected account-wide result independently, and exercise the actual entry point. One targeted case can expose more than many happy-path assertions.

## Bound Writes and Execution

Follow the project's existing test approach. Without a framework, use exact manual steps or an authorized disposable check rather than scaffolding one. Inspect scripts before running them; tests may change databases, generated files, caches, services, or external accounts even when the source checkout is read-only.

A review-and-test request may authorize verification artifacts in an isolated scratch area or explicitly approved test paths, not production fixes. Preserve the reviewed version and distinguish added verification code from the implementation under review. Get additional approval for unapproved dependencies, shared-state setup, destructive operations, or uploads. A scratch checkout does not isolate its database or credentials. Leave test data/artifacts according to user and project rules; do not assume teardown is authorized.

If writes are unavailable or denied, use existing checks or a source trace and state the verification limit. Do not bypass permissions via shell, another tool, or a worker.

## Report Evidence, Not Confidence Alone

Record the behavior tested, exact command or steps, outcome, relevant environment and code state, and paths/artifacts created. Distinguish proposed checks, inspected tests, and executed results. Trust adequate current evidence rather than rerunning it for ceremony. Separate independently established baseline failures from regressions, and revisit only evidence invalidated by later changes.
