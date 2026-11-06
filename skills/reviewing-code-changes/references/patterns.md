# Review Patterns

Open for affected Python/JS/TS code, external-data boundaries, tests, authentication, storage,
public endpoints, or asynchronous/resource-owning changes. These are traps to investigate, not
automatic findings. Establish the actual contract, reachable path, and impact before reporting.
Language traps adapted from wshobson/agents `code-review-excellence` (MIT, Seth Hobson).

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
- An unchecked `fetch` status may interpret a parseable error body as success; inspect the surrounding response handling before reporting it.

## Test quality: would a realistic mistake fail?

Read assertions, fixtures, and mocks, not just test names. A passing test may mock away the very
authorization, transaction, parser, or network boundary the change needs to exercise.

- Derive expected outcomes from requirements and contracts, independently of the implementation. Confirm that a plausible wrong behavior would fail an assertion.
- Prefer observable results at the appropriate boundary: returned values, persisted state, emitted events, or UI behavior. Testing a genuine low-level contract is legitimate; incidental private state or source-text matching usually is not.
- Cover relevant failure and boundary cases, including no forbidden side effects after rejection. Use existing project norms; lack of a framework calls for a recorded focused check, not compulsory scaffolding.
- Check order independence, deterministic timing, and whether mocks/fixtures hide integration mistakes. Distinguish reading a test from executing it.

## Security: follow the trust boundary

Open this pass when auth, input, storage, uploads, or public endpoints change. Apply controls to the
actual threat model and existing contracts, not as universal requirements for every endpoint.

- **Identity and access:** distinguish authentication from authorization; verify tenant/object ownership and allowed operation before sensitive reads or side effects, including fallback/background paths. Validate token signature, issuer/audience, and expiry when the system uses tokens.
- **Input and output:** validate untrusted data server-side at its real boundary, including partner API data. Parameterize SQL; constrain uploads and file paths; escape output for the target context. A cast, frontend check, or authenticated caller does not establish data safety.
- **Sensitive data:** follow password-storage and encryption requirements, avoid secrets/PII in logs and error bodies, and inspect transport/config changes. Do not quote a discovered secret into the report; identify its location and required containment/rotation.
- **Conditional protections:** assess CSRF for cookie-authenticated state changes, rate/size limits for abuse-prone public paths, and injection/sandbox risks for dynamic execution. Do not demand CSRF where its threat does not apply, or call a controlled execution facility a defect solely because it executes code.

## Lifetime, concurrency, and partial failure

Use when changes own resources, start asynchronous work, retry operations, or update related state.

- Who owns each connection, file, timer, listener, task, or subscription, and who releases it on success, failure, and cancellation?
- Can concurrent requests, retries, duplicates, or reordered events violate a limit or apply an operation twice? Look for a concrete race, missing idempotency, or incorrect ordering; do not infer one just from asynchronous syntax.
- Can a multi-step write leave partial state? Inspect transaction boundaries, compensation, and recovery; check authorization before any side effect.
- Are timeouts, work queues, caches, and retry budgets bounded for plausible loads? Use current cardinality/contract evidence for performance claims rather than invented thresholds.
- Does deployment/activation make the path reachable, and can mixed versions safely read/write the changed format? Missing rollout evidence is a limit; a demonstrated incompatible consumer is a finding.
