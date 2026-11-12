# Acceptance Verification

Open when planning task tests, choosing real versus simulated flows, or reconciling code with its
runtime environment. For implementation checks, first use `reviewing-code-changes` and its
`references/test-design.md` for independent expectations, discriminating assertions, real boundaries,
and execution safety. This guide adds task-acceptance coverage; it does not duplicate that method or
authorize setup, writes, paid calls, deletion, or deployment.

## Build a Small Coverage Map

For each material requirement, identify its public entry point, independently derived expected outcome,
important variants/failures, useful test layer, and required resources. Record what ran, what supplied
evidence suffices, and what remains blocked. Reuse the task's requirement map rather than maintaining
two inconsistent lists. Several criteria can share one scenario.

Do not wait until after a green unit suite to discover that the task required UI, asynchronous jobs,
provider fallback, or an earlier acceptance experiment. Before execution, identify the real critical path
and permissions/resources that might block it. Explain material gaps early, without a fixed questionnaire.

Choose tests that could expose a realistic mistake:

| Affected behavior | Useful checks, when relevant |
| --- | --- |
| Input or time threshold | Valid/invalid/empty input; below, exactly at, and above the specified boundary; units, timezone, and cutoff semantics from the requirement |
| State transition | Intended transition, unrelated edit, repeated transition, reactivation, and state change between selection and execution |
| Authorization/isolation | Allowed and denied caller; two identities/tenants/sessions; denied operation has no protected side effect; alternate route cannot bypass the gate |
| Async job/event | Real trigger, enqueue/serialization, worker consumption, persisted effect; retry/duplicate/order behavior where meaningful |
| Provider fallback | First provider succeeds; fails/throws/times out; fallback succeeds/fails; correct recipient/content and no duplicate side effect |
| Installation/build | Fresh intended installation, upgrade/restart when required, effective ownership/config, offline startup if required; artifact actually includes/loads changed code |
| Long-running loop | Success stop, budget exhaustion, rejection/refusal, empty response, pause/resume, restart/compaction, competing loop, and isolation where affected |
| Data cleanup | Intended object and associated data only, unaffected data retained, safe cutoff/input, late reactivation, batch boundary, and partial failure |

These are prompts, not a mandatory Cartesian product. Select based on changed behavior and agreed
risks. For example, a cleanup job using “more than n days since suspension” needs evidence at the exact
cutoff and after an unrelated edit; testing only a very old suspended row cannot distinguish `updated_at`
from suspension time. A callback test that merely checks a sender was called cannot prove its fallback.

## Match Evidence to the Layer

- **Source trace:** demonstrates reachable logic or a violated static contract. Doesn't prove deployment,
  real permissions, timing, provider response, or actual LLM behavior.
- **Unit test:** isolates a rule; inspect assertions, not only test names or mock calls.
- **Integration test:** exercises a real seam such as database, serialization/worker, or service transport.
  Name replacements: a synthetic MCP server tests transport/shape, not the actual Trino/OpenMetadata
  service's contract, authorization, data, or deployment.
- **End-to-end:** uses the task's shipped entry point through the relevant real components to its observable
  outcome. Name the entry point and mocked boundaries. A real CLI test is not browser E2E; a browser
  trigger with a fake message provider is not proof of real SMS delivery.

If an LLM or external provider is part of acceptance, distinguish deterministic test doubles from real
execution and control the relevant budget/model/settings. One observed success does not prove universal
predictability. Don't launch costly calls or send real messages without authorization; a missing credential
or budget leaves a named verification gap rather than permission to infer the result.

## Establish the Environment Before Trusting It

Check only facts that could change conclusions: relevant commit/local changes, Dockerfile/build inputs
and patches, image ID/digest, effective command/import location, mounts, config/feature flags, database
schema, and running frontend/worker. Tags, file presence in the checkout, and a successful build alone
do not show which code a service actually executes.

Prefer a separate image tag, isolated compose project, fresh authorized test volumes/config, and a test
database when stale state could distort a result. First inspect compose/config: new project names do not
isolate explicit container names, external volumes, fixed ports, absolute bind mounts, credentials, or
shared providers. A copied `.env` may still point at production.

Do not copy a destructive reset sequence from an earlier session or README into today's environment.
Identify ownership, scope, and authorization first. Never delete current user volumes/config/dev records
just to obtain a clean build. If safe isolation is unavailable, ask about the exact setup operation or
report the limit. No-cache rebuilding, pulling images, migrations, and service restarts are not mandatory
rituals; use them when required, authorized, and result-changing.

## Preserve Results and Close Coverage

Use the owner skill's evidence record rather than a second logging/reporting scheme. Attach the
acceptance-case/layer coverage and mocked/replaced boundaries to those results. For code/mixed reports,
`writing-code-review-reports` handles evidence portability, redaction, provenance, and baseline issues;
for pure research, use the research owner and the main skill's research-handoff safety guidance.

Before delivery, list each material case/layer as executed, covered by trustworthy supplied evidence,
not applicable, blocked, or skipped with reason. Do not mark a layer executed because a test source exists.
A requested full test pass isn't silently reduced to smoke tests because the verdict is already negative;
continue independent safe checks, but skip paths whose broken prerequisite makes them uninformative.

Temporary logs that disappeared are no longer independently inspectable evidence; retain the observed
historical result with that qualification and rerun only if acceptance needs it and execution is authorized.
