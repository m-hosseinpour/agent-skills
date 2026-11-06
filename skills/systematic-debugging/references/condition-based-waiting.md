# Condition-Based Waiting

Use when a flaky test or async flow guesses at completion with `sleep` or `setTimeout`. Wait for evidence of the intended operation, not elapsed time or unrelated state. First confirm the race; changing a delay does not fix missing events, stale state, deadlocks, or a failed producer.

## Choose the Right Completion Signal

1. Prefer the project's existing retrying assertion, awaited operation, or event/subscription API. Register a listener **before** triggering work so a fast event is not missed; release listeners on success, timeout, and cancellation.
2. Define the exact condition and operation identity. Two old `TOOL_RESULT` events do not prove two new calls finished. Match current request/call IDs, distinct results, or a baseline captured before triggering work. A count offset works only for an append-only history that is neither reset nor truncated; use correlation IDs otherwise.
3. Keep assertions about returned data and errors. A completion marker alone may not prove the behavior under test.
4. Bound the wait using the operation's requirement and observed environment. Choose polling frequency based on getter cost and responsiveness, not a universal 10 ms rule. On timeout, surface the missing condition and relevant sanitized state; do not suppress the producer's failure or blindly raise the budget.

## A Scoped Polling Example

[condition-based-waiting-example.ts](../scripts/condition-based-waiting-example.ts) provides a dependency-free, **synchronous-probe** polling helper. Use it only when no suitable project waiter exists. The getter returns `undefined` until ready; other values, including `0`, `false`, and `null`, are valid results. Unexpected getter errors reject immediately instead of escaping a later timer callback.

The following assumes an existing API where events have documented `callId` and `type` fields. Adapt to the real contract; it is not a schema to impose on a project:

```typescript
import { waitFor } from '/path/to/systematic-debugging/scripts/condition-based-waiting-example.ts';

// Capture these IDs before triggering work. Budgets come from the test setup.
const expectedCallIds = new Set(['current-call-1', 'current-call-2']);
const results = await waitFor(() => {
  const current = getEvents().filter(
    event => event.type === 'TOOL_RESULT' && expectedCallIds.has(event.callId)
  );
  const completed = new Set(current.map(event => event.callId));
  return completed.size === expectedCallIds.size ? current : undefined;
}, 'results for both current calls', { timeoutMs, intervalMs });

// Assert expected content/status and any duplicate-delivery policy separately.
```

This polling helper is not an async I/O deadline or cancellation framework. A slow synchronous probe can block beyond its budget, and a synchronous state read can miss transient events. For async getters or transient events, use an existing bounded async/event mechanism and propagate operation failures. Check its timeout, cancellation, and cleanup behavior rather than assuming `Promise.race` cancels the loser. Polling must observe, not retry a side effect.

## When Time Is the Behavior Under Test

For debounce, throttling, expiry, or periodic ticks, elapsed time is part of the contract. Prefer the project's controlled clock/fake timers, advance the relevant interval, and flush pending async work as the framework requires. Ensure any waiter uses compatible timers/clocks so it cannot hang while fake time is paused. With real timers, first establish the triggering state, then verify the documented timing with appropriate tolerances; observing a sleep finish does not prove two ticks happened.

## Verify the Replacement

- Old/unrelated events and duplicate results for one ID must not satisfy a multi-operation condition.
- A partially completed operation remains pending; the full current operation resolves with the correct values.
- Missing completion fails within a stated budget; a producer/probe failure remains visible.
- No listener or repeating timer remains after settlement where the chosen API allocates one.
- Revisit the original failing workload and relevant CI/concurrency conditions. Report observations; a few passes do not prove all races eliminated.
