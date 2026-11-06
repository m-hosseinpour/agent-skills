# The Quality Bar

The structural pass asks whether a change adds avoidable complexity or damages a useful boundary.

Open when responsibilities, abstractions, dependencies, or complexity change. A structural finding
may redirect detail inspection, but must not outrank security, correctness, or data loss merely because
it is structural. Severity and reporting order follow `SKILL.md`: concrete impact, not the signal.

## The question that comes first

**Is there a reframing that deletes branches, helpers or layers — instead of rearranging them?**

A refactor can move complexity for a legitimate ownership, testing, or compatibility boundary without
reducing branch count. When simplification is relevant, look for a special case absorbed into the default
flow, duplicated rules unified, or an unnecessary state eliminated. Preserve real constraints; do not
assume modes or flags are interchangeable because a smaller design would be convenient.

Stop at "this could be cleaner" and you have written a nit. Say instead: *this works, but there is a
simpler shape — here it is.* Only claim that when you can sketch the simpler shape. Otherwise you are
asking the author to do your thinking.

## Signals to investigate

| Signal | Why it matters |
|---|---|
| A growing file mixes unrelated responsibilities | Navigation and change ownership may be getting harder; size alone is not proof |
| A special case bolted onto an unrelated flow | The next special case goes in the same place; the flow becomes unreadable one exception at a time |
| A thin wrapper that only forwards | Check whether indirection earns a boundary for injection, compatibility, lifecycle, or policy; forwarding alone does not make it useless |
| Feature logic in a shared path | The shared path now knows about one caller, and every other caller inherits the branch |
| A bespoke helper where a canonical one exists | Two implementations of one rule drift; the second one is the bug you find in six months |
| New `any`, a cast, or an optional that hides the contract | The type stopped saying what is true; the invariant moves into someone's memory |
| Independent work serialized for no reason | Can increase latency; first check ordering, rate limits, resource budgets, and failure semantics before recommending concurrency |
| Related updates that can leave state half-applied | The failure window is invisible until it is a support ticket |

## File growth without arbitrary cutoffs

Inspect whether responsibilities are tangled and a split would improve navigation or ownership.
A clearly organized file whose split would be artificial is not a finding merely because it is long.
Do not impose a line-count threshold that the project has not agreed to.

When decomposition addresses a concrete maintenance problem, describe that problem and the proposed
responsibility boundary. Scale its severity by impact, not by line count alone.

## Choose a remedy that preserves the contract

These are options, not a mandatory redesign ladder. Choose the smallest viable change that addresses
the evidenced cost under the existing architecture, compatibility, and deployment constraints.

1. **Delete a concept** when it is demonstrably unnecessary, not when it encodes a real constraint.
2. **Move the boundary.** Put the feature behind the abstraction that owns it, so the shared path
   stops knowing about it.
3. **Reuse the canonical helper.** Search before accepting a second implementation.
4. **Extract a pure function** where logic is tangled with I/O.
5. **Split the file** by responsibility.
6. **Rename** when ambiguous terminology is the actual problem.

Do not demand an architectural rewrite to fix a local naming problem, or rename around an actual
boundary defect. Sketch an alternative and its trade-offs; a hypothetical cleaner design is not proof.

## Prioritizing structural findings

Within findings of comparable impact, these can help choose what earns attention. The final report
still orders all findings by severity and concrete impact; a tenant leak precedes an unnecessary wrapper.

1. Structural regression (the change made the codebase harder to reason about)
2. A missed simplification that would delete real complexity
3. Branching growth in an existing flow
4. Boundary, abstraction, or type-contract damage
5. File size and decomposition
6. Legibility

Prefer evidenced material findings over a cosmetic inventory; there is no quota. Keep optional polish
separate. Preserve required scope-mismatch findings from `requirements.md`, including low-risk extras.

## Readiness and severity

Correct behavior does not rule out meaningful maintenance risks. Investigate:

- a structural regression, or an avoidable complication introduced by this change
- file growth that mixes responsibilities or obscures ownership
- ad-hoc branching that tangles an existing flow
- feature-specific checks scattered through shared code
- an unnecessary wrapper, cast, or optional that makes the design more indirect
- a duplicate of an existing helper, or logic in the wrong layer

These are signals, not automatic blockers. Explain the concrete failure or maintenance cost and a
viable remedy; use Blocking only when the issue must be resolved before merge, Important for material
cost, and Suggestion for an optional improvement with concrete value. A merely conceivable simpler
design is not a defect. The absence of structural findings does not establish readiness: include
requirements, correctness, security, and verification evidence from the rest of the review.

## Tone

Direct, not rude. Do not soften a confirmed material problem into a suggestion, and do not inflate
an optional simplification into a blocker. Explain the problem, concrete cost, and viable remedy;
use enough detail for the reader to check the claim, not a fixed sentence count.

---

Distilled from `thermo-nuclear-code-quality-review` in [cursor/plugins](https://github.com/cursor/plugins)
(MIT, © 2026 Cursor).
