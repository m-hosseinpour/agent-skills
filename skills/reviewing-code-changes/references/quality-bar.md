# The Quality Bar

The structural pass: correctness asks "does it work?", this asks "is the codebase better for it?".

Use it during the shape assessment, before the detail pass. A structural finding may change which
details deserve attention. Severity follows `SKILL.md`: explain concrete risk or cost, not just the signal.

## The question that comes first

**Is there a reframing that deletes branches, helpers or layers — instead of rearranging them?**

A refactor that moves complexity around has not reduced it. The strongest finding available to a
reviewer is the one that makes a whole concept disappear: a special case absorbed into the default
flow, two modes collapsed into one, a flag that turns out to be a state which should not exist.

Stop at "this could be cleaner" and you have written a nit. Say instead: *this works, but there is a
simpler shape — here it is.* Only claim that when you can sketch the simpler shape. Otherwise you are
asking the author to do your thinking.

## Signals to investigate

| Signal | Why it matters |
|---|---|
| A file crosses 1,000 lines in this diff | A prompt to inspect navigation and mixed responsibilities, not proof of a defect |
| A special case bolted onto an unrelated flow | The next special case goes in the same place; the flow becomes unreadable one exception at a time |
| A thin wrapper that only forwards | Every reader pays the indirection; nobody is repaid |
| Feature logic in a shared path | The shared path now knows about one caller, and every other caller inherits the branch |
| A bespoke helper where a canonical one exists | Two implementations of one rule drift; the second one is the bug you find in six months |
| New `any`, a cast, or an optional that hides the contract | The type stopped saying what is true; the invariant moves into someone's memory |
| Independent work serialized for no reason | Slower, and more states to reason about than the problem has |
| Related updates that can leave state half-applied | The failure window is invisible until it is a support ticket |

## The 1,000-line heuristic

A heuristic, not a merge threshold. When a diff pushes a file past 1,000 lines, inspect whether
responsibilities are tangled and a split would improve navigation. A clearly organized file whose
split would be artificial is not a finding merely because of its line count.

When decomposition addresses a concrete maintenance problem, describe that problem and the proposed
responsibility boundary. Scale its severity by impact, not by line count alone.

## Remedies, in order of preference

1. **Delete a concept.** If two branches exist because one state was never modeled, model it and the
   branches go away.
2. **Move the boundary.** Put the feature behind the abstraction that owns it, so the shared path
   stops knowing about it.
3. **Reuse the canonical helper.** Search before accepting a second implementation.
4. **Extract a pure function** where logic is tangled with I/O.
5. **Split the file** by responsibility.
6. **Rename** — only when nothing above applies.

Do not suggest 6 when 1 is available.

## Report priority

1. Structural regression (the change made the codebase harder to reason about)
2. A missed simplification that would delete real complexity
3. Branching growth in an existing flow
4. Boundary, abstraction, or type-contract damage
5. File size and decomposition
6. Legibility

Prefer four high-conviction findings over twenty cosmetic ones. If a structural finding exists, the
cosmetic ones are not worth the reader's attention in the same document.

## Readiness and severity

Correct behavior does not rule out meaningful maintenance risks. Investigate:

- a structural regression, or incidental complexity preserved where a path to delete it was visible
- a file pushed past 1,000 lines
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

Direct, not rude. Do not soften a structural problem into a suggestion, and do not inflate a
suggestion into a blocker. Two sentences: what is wrong, and which shape you want instead.

---

Distilled from `thermo-nuclear-code-quality-review` in [cursor/plugins](https://github.com/cursor/plugins)
(MIT, © 2026 Cursor).
