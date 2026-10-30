# Review Patterns

Language-specific traps, test-quality criteria, and the deeper security pass. Load this when the
diff touches Python, TypeScript/JavaScript, authentication, or the test suite.
Language traps adapted from wshobson/agents `code-review-excellence` (MIT, Seth Hobson).

## Python traps

```python
# Mutable default argument — shared across every call
def add_item(item, items=[]):        # bug
def add_item(item, items=None):      # fix
    if items is None:
        items = []

# Bare except swallows everything, including KeyboardInterrupt
try: ...
except: pass
except ValueError as e: logger.error(e); raise   # fix

# Mutable class attribute — shared across instances
class User:
    permissions = []                 # bug
    def __init__(self): self.permissions = []
```

## TypeScript / JavaScript traps

```typescript
// `any` defeats the type system at the boundary
function processData(data: any) { return data.value; }
interface DataPayload { value: string }                 // fix

// Await without checking the response — a 500 reads as success
async function fetchUser(id: string) { return (await fetch(`/api/users/${id}`)).json(); }
if (!response.ok) throw new Error(`HTTP ${response.status}`);   // fix

// Mutating props — the parent never learns
function UserProfile({ user }: Props) { user.lastViewed = new Date(); }
function UserProfile({ user, onView }: Props) { useEffect(() => onView(user.id), [user.id, onView]); }
```

## Test quality

```typescript
// ❌ asserts internal state — breaks on every refactor
expect(component.state.counter).toBe(1);
// ✅ asserts what a user observes
expect(screen.getByText('Count: 1')).toBeInTheDocument();
```

Ask: do the tests describe behavior or internals, do they cover the unhappy path, are they
independent and order-free, and would they fail if the change were wrong?

## Security pass

Run this when the diff touches auth, input handling, storage, or public endpoints.

- **Auth**: authentication required where needed; authorization checked *before* every action, not after; JWT signature and expiry validated; keys and secrets loaded from config, never literals.
- **Input**: all user input validated server-side; uploads restricted by size and type; SQL parameterized, never interpolated; output escaped for the target context (XSS).
- **Data**: passwords hashed with bcrypt/argon2; sensitive data encrypted at rest; HTTPS enforced; PII handled per regulation.
- **Common holes**: no `eval` or dynamic execution; no hardcoded secrets; CSRF protection on state-changing operations; rate limiting on public endpoints.
