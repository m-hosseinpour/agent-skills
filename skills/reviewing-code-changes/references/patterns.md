# Review Patterns

Open for affected dependencies/imports and locked APIs, Python/JS/TS code, external-data boundaries, test/gate diffs, authentication/authorization and audit logs, storage, public endpoints, recurring/resumable work, or asynchronous, transactional, cached, and resource-owning changes. These are traps to investigate, not automatic findings. Establish the actual contract, reachable path, and impact before reporting.
Language traps adapted from wshobson/agents `code-review-excellence` (MIT, Seth Hobson).

## Contents

- [Dependencies and external APIs: plausible is not installed](#dependencies-and-external-apis-plausible-is-not-installed)
- [Python: accidental shared state and swallowed failures](#python-accidental-shared-state-and-swallowed-failures)
- [TypeScript / JavaScript: static types are not runtime validation](#typescript--javascript-static-types-are-not-runtime-validation)
- [Test quality: would a realistic mistake fail?](#test-quality-would-a-realistic-mistake-fail)
- [Security: follow the trust boundary](#security-follow-the-trust-boundary)
- [Recurring and resumable work](#recurring-and-resumable-work)
- [Lifetime, concurrency, and partial failure](#lifetime-concurrency-and-partial-failure)

## Dependencies and external APIs: plausible is not installed

For new or changed imports, library calls, or service integrations, verify the package/path and API against the project's installed or locked version and authoritative documentation. The latest release's API is not proof that the deployed version supports it. Check that the reachable implementation uses the dependency and follows the project's existing conventions; do not add speculative adapters or flag an intentional local module solely because it is absent from a package manifest. For dependency upgrades or lockfile changes, inspect release notes or migration guides for breaking behavior and default changes across the actual version range, check transitive lockfile diffs and affected consumers, and verify with relevant tests; a clean installation or semantic version bump alone does not establish compatibility.

These boundary, failure, and lifetime checks apply to generated code as well as human code. Line count, the absence of a literal `finally`, or compiling successfully is not a safety test: establish ownership, existing safeguards, and a reachable failure before reporting a defect. Avoid duplicate full audits just because code was AI-written.

## Python: accidental shared state and swallowed failures

- A mutable default such as `def add_item(item, items=[])` shares state across calls. When calls should be independent, use `None` and allocate inside the function. Verify intended ownership rather than treating an intentional shared cache as the same defect.
- A mutable class attribute such as `permissions = []` is shared across instances. Allocate per instance if permissions are instance-owned; check the actual mutation paths.
- Bare `except` catches interruptions as well as ordinary failures. Broad catches that swallow exceptions or return success can conceal an incomplete operation. Catch expected failures at the right boundary and propagate or report them according to the contract; blindly logging and re-raising at every layer duplicates logs rather than fixing recovery.
- Check context-manager/finally ownership for files, transactions, and other resources. Cancellation or exceptions can bypass success-only release logic.

## TypeScript / JavaScript: static types are not runtime validation

An interface, a type annotation, or `as Payload` does not validate JSON at runtime. Treat external
data as unknown and parse it against the real documented contract, using an existing project validator
when available. `any` or a cast is a signal to inspect the boundary, not proof of a defect if validation
already happened on a reachable preceding path.

For example, when the contract requires a finite integer limit from 1 through 100:

```typescript
interface ImportPayload { limit: number }

function parseImportPayload(value: unknown): ImportPayload {
  if (typeof value !== "object" || value === null) {
    throw new Error("Invalid import payload");
  }
  const limit = (value as Record<string, unknown>).limit;
  if (typeof limit !== "number" || !Number.isInteger(limit) || limit < 1 || limit > 100) {
    throw new Error("Invalid import limit");
  }
  return { limit };
}

async function fetchImport(url: string): Promise<ImportPayload> {
  const response = await fetch(url);
  if (!response.ok) throw new Error(`HTTP ${response.status}`);
  const raw: unknown = await response.json();
  return parseImportPayload(raw);
}
```

Here `Number.isInteger` also rejects non-finite numbers. The bounds belong to this example's contract,
not every API. Adapt failure handling to the project: network, non-success status, malformed JSON,
and invalid payloads must not silently become success. A plain numeric interface is not a remedy.

Other affected paths:

- Unawaited promises, incomplete `Promise.all` failure handling, or missing cancellation can leave background work running after the caller fails. Check ownership and observable consequences.
- Render-time mutation of props or external state can make UI behavior depend on repeated rendering. Use the established event/effect flow only when it matches the intended trigger; moving a mutation to an effect is not automatically correct and may still duplicate it.
- Duplicating derivable state (from props/inputs, store, URL, or query cache) into local mutable state and synchronizing it through watchers or effects can leave stale data on updates or resets; distinguish an intentional editable draft from state meant to stay derived.
- An unchecked `fetch` status may interpret a parseable error body as success; inspect the surrounding response handling before reporting it.

## Test quality: would a realistic mistake fail?

Read assertions, fixtures, and mocks, not just test names. A passing test may mock away the very
authorization, transaction, parser, or network boundary the change needs to exercise.

- Derive expected outcomes from requirements and contracts, independently of the implementation. Confirm that a plausible wrong behavior would fail an assertion. Watch for circular tests that copy the implementation's formula or assert only what a mock was configured to return instead of verifying the post-condition and absence of forbidden side effects.
- Inspect diffs to existing tests, test configs, and lint/type/CI rules for weakened assertions (such as replacing an exact expected value with a truthiness or status-only check), deleted or newly skipped tests, lowered coverage/check thresholds, or suppressions (`@ts-ignore`, `eslint-disable`, `# noqa`) that turn checks green by hiding a failure.
- Prefer observable results at the appropriate boundary: returned values, persisted state, emitted events, or UI behavior. Testing a genuine low-level contract is legitimate; incidental private state or source-text matching usually is not.
- Cover relevant failure and boundary cases, including no forbidden side effects after rejection. Use existing project norms; lack of a framework calls for a recorded focused check, not compulsory scaffolding.
- Check order independence, deterministic timing, and whether mocks/fixtures hide integration mistakes. Distinguish reading a test from executing it; when designing or running a verification check, open [test design](test-design.md).

## Security: follow the trust boundary

Open this pass when auth, input, storage, uploads, or public endpoints change. Apply controls to the
actual threat model and existing contracts, not as universal requirements for every endpoint.

- **Identity and access:** distinguish authentication from authorization; verify tenant/object ownership and allowed operation before sensitive reads or side effects, including fallback/background paths. Validate token signature, issuer/audience, and expiry when the system uses tokens.
- **Input and output:** validate untrusted data server-side at its real boundary, including partner API data, and guard against mass-assignment or internal-field exposure when binding or serializing storage models directly. Parameterize SQL; constrain uploads and file paths; escape output for the target context. A cast, frontend check, or authenticated caller does not establish data safety.
- **Sensitive data:** follow password-storage and encryption requirements, avoid secrets, PII, or internal stack traces in logs and client-facing error bodies, and inspect transport/config changes. Do not quote a discovered secret into the report; identify its location and required containment/rotation. For sensitive-action audit logs, verify that denied, failed, or rolled-back attempts still leave a durable record rather than writing only on the success path or inside a rolled-back transaction.
- **Conditional protections:** assess CSRF for cookie-authenticated state changes, rate/size limits for abuse-prone public paths, and injection/sandbox risks for dynamic execution. Do not demand CSRF where its threat does not apply, or call a controlled execution facility a defect solely because it executes code.

## Recurring and resumable work

Use for scheduled cleanup, expiry, sweeps, or batches that can run again. Review selection, effects,
completion, and the next run together, not just whether one invocation performs the requested action.

- **What changes eligibility?** Trace the actual predicate, timestamps/cursor, and affected records before and after success. Recheck even an unchanged selector when the action changes scope: deleting a parent's children may no longer remove the parent from the selected set, unlike deleting the parent itself. Do not assume child writes update parent timestamps; inspect callbacks and other selection paths.
- **What should later runs do?** Distinguish completing one work item from continuous enforcement or reconciliation. Completion may remove eligibility through deletion, a predicate, a cursor, or a completion marker; a new terminal status is not universally required. Intentional repeated selection can be correct, including periodic sync and cleanup of newly added children. Establish the contract and plausible work/retention bounds rather than treating repetition alone as a defect.
- **Is repetition harmless in practice?** Idempotency (repeating an effect does not change the result) does not establish convergence (finished work stops accumulating in the selected set). Trace later runs for retained backlog, repeated queries/logs/queue entries, misleading completion reporting, and effects on data created afterward. Report a reachable failure or concrete operational cost, supported by workload or contract evidence, not merely “the selector does not converge.” Missing intent is a question, not proof that future cleanup is forbidden.
- **When is the work actually complete?** Enqueueing or dispatching is not completion of asynchronous effects. If a marker excludes a record from future selection, trace partial enqueue, worker failure/retry exhaustion, and interruption before all effects finish. Verify a durable recovery owner: pending work with retries/reconciliation can justify exclusion from the original sweep; a success marker that strands unfinished effects cannot. A state meaning “dispatched” need not wait for execution, but must not falsely report completion or lose recovery. Check affected consumers and gates if states change.

For focused verification, follow [test design](test-design.md): compare later-run selection and effects,
and exercise a relevant asynchronous failure when completion depends on downstream workers.

## Lifetime, concurrency, and partial failure

Use when changes own resources, start asynchronous work, retry operations, or update related state.

- Who owns each connection, file, timer, listener, task, or subscription, and who releases it on success, failure, and cancellation? Conversely, are heavyweight shared clients or connection pools reused rather than recreated per request or loop iteration?
- Can concurrent requests, retries, duplicates, or reordered events violate a limit, apply an operation twice, or overwrite request/user state stored on a shared singleton, service instance, or module field? Look for a concrete race, shared mutable state, missing idempotency, or incorrect ordering; do not infer one just from asynchronous syntax.
- For stateful UI or client flows (including live search or filter inputs that trigger requests), what happens on rapid input, when the active target, item, user, or route changes, a component unmounts or a dialog dismisses, or overlapping operations settle out of order? Verify rate control or cancellation where needed and check that stale completions or retries cannot overwrite a newer owner's state, lose in-progress edits, or leave visible state inconsistent with persisted state.
- Can a multi-step write leave partial state, or does a database transaction/lock stay open across external HTTP/RPC calls, queues, or slow I/O (holding locks/connections and leaving external side effects committed if the transaction rolls back)? Inspect transaction boundaries, compensation, and recovery; check authorization before any side effect.
- When a change introduces an early return, clamp, `null`/empty fallback, or new thrown error, do all unchanged callers and downstream consumers handle that result shape safely?
- Are timeouts, work queues, caches, and retry budgets bounded for plausible loads? When data is cached, check how writes invalidate or refresh it, whether transient failures get cached, and whether cache keys include the full scope (such as tenant, user, or parameters). Use current cardinality/contract evidence for performance claims rather than invented thresholds.
- Does deployment/activation make the path reachable, and can mixed versions safely read/write the changed format? Missing rollout evidence is a limit; a demonstrated incompatible consumer is a finding.
