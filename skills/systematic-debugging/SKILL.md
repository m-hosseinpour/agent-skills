---
name: systematic-debugging
description: Use when a bug, test failure, build error, performance problem, or unexpected result needs investigation before proposing a fix.
---

# Systematic Debugging

Find the cause before changing code. A fix should explain the evidence, not merely make one symptom disappear.

## Investigate

1. **Observe and reproduce.** Read the complete error or wrong output. Record the exact steps, inputs, environment, and expected versus actual result. If it is intermittent, gather more examples instead of claiming a reproduction.
2. **Trace the failing path.** Check recent changes and follow the relevant data or control flow from the observed failure toward its source. In multi-component systems, inspect the values at the boundaries to learn which component first diverges.
3. **Compare with a working case.** Find a similar successful path and identify the differences in inputs, state, configuration, dependencies, or timing.
4. **State one hypothesis.** Explain which evidence supports it. Test the smallest useful change or probe, changing one variable at a time.
5. **Fix the root cause and verify.** Preserve a reproducible failure before editing. Prefer the project's existing test setup; if none exists, record exact manual steps or use a small disposable check instead of scaffolding a framework unasked. After the fix, repeat the reproduction and run relevant checks. State what was and was not verified.

If the hypothesis is wrong, return to the evidence and form another one; do not stack guesses. If several well-supported fixes fail or each exposes a new coupling, pause and reconsider the design with the user before another attempt.

## When the Failure Is in an Output

When a system produces incorrect decisions or reports without throwing an error, inspect the recorded inputs and outputs first. Compare like cases, identify the rule or branch associated with the failure, change one rule at a time, and measure the same outcome again. A metric that does not improve is evidence to investigate the implementation; by itself it is not a reason to delete the concept.

## Useful Supporting Techniques

These files are optional deeper techniques in this skill's directory:

- `root-cause-tracing.md` — trace a defect back through a deep call chain.
- `defense-in-depth.md` — add layered checks after identifying the source.
- `condition-based-waiting.md` — replace timing guesses with condition-based waits.
