# Defense-in-Depth Safeguards

Use after tracing invalid input or a dangerous side effect to its source. Fix the source, then add safeguards only at boundaries that protect distinct invariants or independently reachable operations. Several useful checks can coexist; duplicating one check at every internal call is not the goal.

## Choose Checks by Responsibility

| Location | Distinct purpose | When justified |
| --- | --- | --- |
| External input boundary | Reject malformed or untrusted values before side effects | Runtime input is not already validated; types alone are insufficient |
| Domain operation | Enforce a business invariant, such as ownership or allowed state transition | Validly shaped input can still violate the operation's rules |
| Dangerous filesystem/process operation | Constrain the target or operation | Another entry path can invoke it, or a mistake risks valuable state |
| Diagnostics | Explain a failure with limited, sanitized context | Existing signals cannot distinguish the plausible causes |

Diagnostics observe; they do not prevent a bug. A test-only guard is not a production security boundary. Before adding a check, name what it catches that an existing check cannot. Share validation when genuinely reused; do not add speculative wrappers or require a fixed number of layers.

## Example: An Empty Working Directory

If a fixture is read before initialization, correct that lifecycle error. At a real input or process-launch boundary, reject empty or whitespace-only paths instead of silently substituting the working directory. Preserve valid path semantics: some operations require an existing directory, others intentionally create one. Prechecking existence or writability does not guarantee the later filesystem operation will succeed; handle its actual error using project conventions.

If tests must stay inside an approved workspace, compare **path components**, not string prefixes: `/tmp/work-other` is not inside `/tmp/work`. For existing directories in Node, the following is an illustrative check, not a portable security sandbox:

```typescript
import { realpathSync } from 'node:fs';
import { isAbsolute, relative, sep } from 'node:path';

function requireWithinRoot(root: string, directory: string): string {
  if (!root.trim() || !directory.trim()) {
    throw new Error('Explicit root and directory are required');
  }
  const canonicalRoot = realpathSync(root);
  const target = realpathSync(directory);
  const offset = relative(canonicalRoot, target);
  if (offset === '..' || offset.startsWith(`..${sep}`) || isAbsolute(offset)) {
    throw new Error('Directory is outside the approved root');
  }
  return target;
}
```

This allows the root itself; require a nonempty `offset` if only descendants are permitted. Canonicalization catches existing symlink escapes, but requires existing paths and does not prevent another actor changing the filesystem between check and use. For a new target, validate the existing parent and creation semantics; for adversarial paths or concurrent mutation, use the platform's appropriate isolation/handle-based protections. Use a task-specific approved root, not “anything under the system temp directory.”

## Verify the Safeguards

- Repeat the original failure after the source correction.
- Exercise invalid input before mutation and a valid neighboring case.
- If an independent caller can reach a guarded operation, exercise that path too.
- For containment, check the allowed root policy, a valid child, a sibling sharing the root's text prefix, traversal outside the root, and applicable symlink escapes.
- Confirm failures are visible and useful, without leaking sensitive context.

Report which conditions were checked and remaining limitations. Neither layered checks nor a passing suite proves a bug impossible.
