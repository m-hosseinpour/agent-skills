# Root Cause Tracing

Use when the observed failure is far from the source of an invalid value or state, or when an unwanted artifact appears during tests. Trace to the first point that violates the intended contract, not automatically the deepest or oldest caller.

## Trace the Value or State

1. Locate the operation producing the symptom. What value, state, and context did it actually receive?
2. Follow its callers or producers backward. At each step, record where the value originated, how it changed, and what the receiving contract expects.
3. Compare a working path under like conditions. Stop at the first demonstrated divergence: an invalid producer, a broken transformation, missing initialization, or a mismatch between legitimate caller and callee expectations.
4. Confirm with a small probe or reproduction. Fix the violated contract; add a separate boundary safeguard only when it has an independent purpose. See [defense-in-depth](defense-in-depth.md).

Illustrative trace:

```text
unwanted repository in source directory
  ← process launcher receives empty working directory
  ← workspace creation forwards an uninitialized path
  ← test reads its fixture before the setup hook runs
```

Verify how the actual launcher handles an empty directory; do not assume all APIs resolve it identically. If premature fixture access is demonstrated, initialize/use the fixture at the right lifecycle point. Rejecting an invalid path at the filesystem boundary may also be warranted, but does not replace that correction.

## Instrument Only the Missing Link

- Use the project's visible diagnostic channel. Verify the logger is captured before falling back to stderr; do not mandate one logging API for every test runner.
- Include only distinguishing context: correlation ID, state transition, sanitized input shape, relevant path, or caller. Avoid dumping environment variables, credentials, or whole customer payloads.
- A synchronous stack trace helps with callers, but may not show an earlier async producer or another process. Follow job/event IDs across those boundaries.
- Preserve useful surrounding output and the original command's status. Filtering a log is a reading aid, not evidence that the test command succeeded.
- Keep probes bounded and safe. Remove temporary instrumentation you added before delivery unless retaining it is justified; do not delete user artifacts or test data as incidental cleanup.

If the trail ends, name the missing evidence and the next discriminating probe. Do not invent an upstream cause. A local guard can be a disclosed mitigation, not proof of root cause.

## Test Pollution and Order Dependence

First reproduce the original order, concurrency, fixture lifecycle, and process reuse. If A leaves state that B consumes, B may create the artifact without being the initiating cause. Compare isolated A, isolated B, A→B, and B→A when those runs are safe and informative. To minimize a longer sequence, preserve ordering and necessary predecessor state.

[find-polluter.sh](../scripts/find-polluter.sh) is an optional **sequential file scan**, not bisection or an isolated clean-room test. Use it only when the unwanted path starts absent in an approved disposable workspace and separate runner invocations can reveal the symptom. It does not delete artifacts or reset other state between runs. A hit identifies the invocation after which the path appeared, not necessarily the root cause; process-local or concurrency failures may not reproduce at all.

Run from the project workspace, using the helper's installed path and a verified command that runs **one file**. The paths below are illustrative placeholders, not literal installation locations:

```bash
bash /path/to/systematic-debugging/scripts/find-polluter.sh \
  'unexpected.db' 'tests/**/test_*.py' -- uv run pytest '{}'

# With no {} argument, the file is appended. Use npm's argument separator.
bash /path/to/systematic-debugging/scripts/find-polluter.sh \
  'unexpected-cache' 'src/**/*.test.ts' -- npm test --
```

The helper requires Bash 4+, preserves runner output/status, and stops on pollution or runner failure. The glob uses Bash pathname rules (`**` enabled, hidden entries excluded). Filenames with spaces are preserved; `{}` must be a standalone argument. It does not infer the runner from manifests. Exit **0** means all selected invocations succeeded without the target path; **1** means the path appeared; **2** means invalid setup or inconclusive execution. None of these proves absence of other pollution or success in the original shared-process suite. If a selected test fails before any artifact appears, investigate that failure rather than silently continuing.

Selection rejects symlinked test files (even internal ones) and parent directories that physically resolve outside the workspace. Internal directory links are allowed only if their physical target stays inside. This prevents accidental out-of-workspace selection, not side effects from the runner or adversarial filesystem changes; use proper isolation when those are a risk.

If the path already exists, preserve it. Use a fresh approved workspace or ask before removing it; do not delete a project's `.git` directory to make a scan possible.
