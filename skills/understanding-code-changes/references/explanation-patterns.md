# Choosing an Explanation for a Change

Use this guide when the change's difficulty is clearer than the best way to explain it. Pick the smallest representation that answers the reader's real question. Combine views only when they explain different things; a map, pseudocode, and trace that repeat the same story are noise.

## Match the view to the question

| Reader's question | Useful view | What to make explicit |
| --- | --- | --- |
| Where does this fit, and how is it reached? | Before/after flow or call map | Entry, changed edge, unchanged dependency, effect, process boundary |
| Why does this input now behave differently? | Side-by-side trace or input/output table | Same initial conditions, first divergence, resulting behavior |
| What happens over time or under failure? | State/transition table or sequence | Guards, side effects, ownership, retry/terminal state |
| What must callers or stored data now obey? | Contract delta table | Old/new contract, affected producer and consumer, compatibility |
| If behavior is unchanged, what moved? | Responsibility/dependency map | Old/new owner, public boundary, dependency direction, evidence limits |
| When does the shipped code actually take effect? | Activation/rollout table | Default, prerequisite, enabled path, mixed-version constraints |
| How do several MRs build on each other? | Dependency chain and layer table | Baseline per layer, supplied prerequisite, cumulative effect |

## Flow maps: show relationships, not a directory tree

Keep only the actors and edges needed to explain the change. Name which edges are new, removed, or unchanged. An unchanged caller can be the most important node. Separate a function call from a queue handoff or database write; these have different timing and failure behavior.

Prefer a short text flow when it is enough:

```text
Before: receiver → transaction [record event → call mail provider] → 202
After, flag on: receiver → transaction [record event + enqueue mail] → 202
               separate worker → pending outbox row → mail provider → mark sent
Unchanged: 202 means accepted, not delivered; flag off keeps the old path.
```

Use Mermaid for branching or multiple actors only if the reader can render it. Explain the key relationship in prose too. Solid-looking diagrams must not conceal unknown edges: mark an uninspected queue consumer or unavailable external contract as unknown.

## Traces: expose the divergence

1. Choose a small input and initial state tied to the changed branch, not an arbitrary happy path.
2. Hold input and relevant conditions constant between before and after. Include the flag/default if it selects the path.
3. Walk to the first different decision or effect, then stop at the observable result.
4. State whether this is a source-based hand trace or an executed scenario. For a hand trace, expose assumptions about omitted code or runtime behavior.

For the flow above, a provider failure is more informative than a successful send:

| Moment | Before | After, queue flag on |
| --- | --- | --- |
| Receiver's transaction | Calls the provider before completion | Stores the event and mail request together |
| Provider unavailable | Send failure propagates through the receiver path | Provider is not called by the receiver |
| Observable result | Normal `202` return is not reached; exact HTTP error depends on surrounding handling | After a successful commit, the receiver returns `202` |
| Later delivery | No separate worker in this path | Worker attempts sending; a failed row remains pending if that is what the inspected storage/dispatcher implement |

This explains decoupling without claiming guaranteed delivery. A second short boundary example may be worth adding: process termination after sending but before marking the row can allow another attempt. Whether that causes duplicate delivery also depends on the provider's contract. Do not infer exactly-once delivery from a unique row key.

For a new feature with no predecessor, use “previously unavailable” and show its new path; do not invent an old implementation to fill the table.

## Dense logic: keep the meaning in the simplification

Pseudocode can remove syntax, not the conditions that determine behavior. Retain a failed-send branch when explaining retries, transaction boundaries when explaining atomicity, and ordering when explaining races. Anchor it to the actual source.

For a state table, separate the logical state inferred from fields from any explicitly modeled state:

| Current state | Event/guard | Effect | Next state |
| --- | --- | --- | --- |
| Pending | Provider call succeeds and success record is stored | Send, then record success | Sent |
| Pending | Provider call fails | Record failure if implemented | Pending |
| Pending | Process stops between send and success record | External send may already have happened | Still pending in storage |

Include only transitions the implementation supports. A dead-letter state, retry limit, or locking guarantee that would be useful is not necessarily present.

## Refactors: explain ownership and preserved contracts

Start with the responsibility that changed hands, not a made-up input/output delta:

| Responsibility | Before owner | After owner | Caller-visible contract |
| --- | --- | --- | --- |
| Decide whether an event is eligible | Request handler | Domain policy called by handler | Same decision rules in inspected paths |
| Translate policy result into HTTP response | Request handler | Request handler | Same status/body mapping in inspected paths |

Add a dependency arrow when its direction matters, and point to the unchanged caller. Explain how the project's existing layering or convention relates to the move, based on actual neighboring code.

“The author calls this a refactor,” “these inspected branches preserve behavior,” and “equivalence was established by these checks” are different claims. Look for changed defaults, exception handling, evaluation order, lifecycle, exports, and initialization when they could invalidate the structural-only explanation. A focused test is evidence for its exercised paths, not universal equivalence.

## Contracts and activation: explain the conditions around the code

For schema/API/configuration changes, show the contract delta and who depends on it. Include an unchanged consumer that matters; do not limit the table to edited files.

| Contract | Before → after | Producer/consumer | Evidence or unresolved edge |
| --- | --- | --- | --- |
| Response meaning | Accepted → still accepted | Receiver / external caller | Project docs and response path |
| Storage | No outbox → tenant-scoped pending mail records | Receiver / dispatcher | Migration plus storage calls; implementation availability matters |
| Activation | Direct send → queued path only with flag enabled | Receiver / scheduled worker | Default and registration; deployed flag values may be unknown |

For rollout, record the **documented or code-required** order separately from the deployed state. For example, inserting into a new table requires the schema to exist; that does not prove the migration has run in production. If rollback/draining behavior is not documented, mark it unknown rather than designing a rollout on the author's behalf.

## Stacks and mixed changes: give each layer a job

For a stack such as `target → schema MR → producer MR → consumer MR`, explain what each layer adds and what cannot work without its parent. Record each diff's actual parent/baseline; comparing every branch directly to the target can count inherited changes repeatedly.

Use commit chronology only when it reveals a migration sequence or an evidenced design evolution. Commit order alone does not reveal why the author changed their mind. For unrelated changes in one MR, use separate behavioral units and shared orientation once; do not force one causal story.

## Keep the explanation navigable

- Lead with the central insight, then connect it to code anchors: `path` + symbol and revision, with line ranges when known.
- Place a consequential callout at the divergence or boundary it explains, rather than gathering all insight into a detached risk list.
- Pair a concise main narrative with a coverage appendix when the file inventory is large.
- Remove a view if it adds no information beyond the surrounding prose. A short bug fix may need only one anchored before/after example; a cross-process feature may need a map plus one failure trace.
