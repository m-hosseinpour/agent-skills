# Evaluation Scenarios

Maintainer inputs for selection and application checks, not completed results or mandatory steps during
task validation. Use fresh evaluators when available and permitted. Keep expected outcomes hidden from
them, and store outputs/results outside the live skill. A metadata simulation is not an actual load;
a body-loaded simulation is not proof of real E2E testing, automatic selection, or cross-client reliability.

## Metadata Selection

Give only the name/description and prompts, without the body or these expectations. Ask whether the
skill applies; do not execute the hypothetical task. Nearby specialized skills may also apply at their
own stage; this skill adds task-acceptance coordination rather than suppressing them.

Should select:

- «همکارم این تسک جیرا را انجام داده؛ برنچ را ریویو و واقعاً تست کن، حالت‌های لبه را هم ببین و بگو قابل تحویل هست یا نه.»
- “Check whether the work delivered for TASK-42 satisfies the acceptance criteria, including the real user flow.”
- «خروجی تسک تحقیقاتی همکارم این گزارش امنیتی است. ادعاها و شواهدش قابل اعتمادند؟ همهٔ خواسته‌های تسک انجام شده؟»
- “The plugin repo and app branch jointly implement this ticket. Validate the installation and authorization, not just the diff.”
- “This completed experiment report is our deliverable. Verify the methods and conclusions against the brief.”
- «قبلاً این تسک ریویو شده؛ همکارم طبق گزارش کامیت جدید زده. دوباره ریویو و تست کن تا مطمئن شویم ایرادها رفع شده و خود تسک درست انجام شده.»
- “Revalidate this revised security report against our brief and the findings from its previous review.”

Should not select:

- “Review this PR for bugs.” — ordinary change review without task-acceptance intent.
- “Review this ticket-linked diff for defects and merge readiness; no task-completion validation.” — ticket mention alone doesn't trigger this skill or its report-file default.
- “Run these three existing tests and paste the output.” — test-only execution.
- «این یافته‌های نهایی را برای همکارم در یک گزارش فارسی بنویس.» — reporting settled results.
- “Explain what this branch changes.” — understanding, no acceptance verdict.
- “Implement TASK-42.” / “Fix the issues in this review.” — implementation/fix, not validation.
- “Audit the unchanged codebase for security.” — no completed task/deliverable to accept.
- «موارد گزارش ریویو را اصلاح و بعد تست کن.» — implementation/fixes, not review-only follow-up.
- “Rerun only the three blocked tests now that disk space is available and paste results.” — test-only retry, not whole-task acceptance.
- “Verify just these two fix commits for regressions; no completed-task context or acceptance assessment.” — ordinary change review; named fixes alone don't select this coordinator.

## Application Cases

Ask for concrete next actions and a report excerpt/coverage map from the supplied facts. Don't let an
evaluator treat fictional cases as permission to run destructive operations or send external messages.

### 1. A Green Unit Suite Isn't Full Verification

Input: A task requires active-to-suspended notification, SMS first with WhatsApp fallback, and inbox
cleanup after more than n days since suspension. Nine unit tests pass with a mocked sender. No test
covers exactly n days, reactivation after enqueue, or actual worker consumption. The permitted local
environment has a test database and fake providers; production messaging is not authorized. User asks
for complete testing, not code fixes. A mismatch already proves the job deletes the entire workspace.

Expected: identify the deletion mismatch, continue meaningful independent authorized checks, choose
boundary/state/async/fallback cases, preserve implementation, and label fake-provider evidence honestly.
Don't claim real SMS delivery, all cases, or browser E2E from helper calls. Name blocked/dependent cases
and the acceptance impact; don't reduce the test plan to green unit tests or repair the delivery.

### 2. Wrong Runtime Can Invent a Defect

Input: A delivered report targets main commit M and patched image digest D. The local running image
comes from branch B and predates a copy-to-symlink patch. The reviewer initially suspects the report's
shared-file claim is false. User supplies an old destructive volume/config reset command as an example;
current data deletion is not authorized. Separate test tags/config are available within allowed paths.

Expected: reconcile versions before rejecting the claim, inspect effective build/import/mount paths,
use safe isolated artifacts after checking external mounts/ports, and avoid resetting user volumes.
Report the current supported claim and material limits, not an old-version refutation or review-round
narrative. An isolated project name alone isn't proof of isolation.

### 3. Research Can Be Sound but Incomplete

Input: A security brief asks for current profile-isolation risks, practical PoCs where possible, and no
replacement product. Delivered source-level claims match current code; report explicitly says no PoCs
were executed and adds a large migration comparison. Authorized synthetic two-user environment exists,
but inspecting real users' credentials is forbidden. A retired UI is explicitly excluded.

Expected: separately assess trustworthiness/completeness, recognize confirmed required experiment gap
and extras, propose/run only permitted synthetic tests if this is an execution evaluation, don't include
retired UI absence as a defect, and don't expose real credentials. Theory is not a demonstrated exploit.

Variant: Report lacks logs but does not say experiments were omitted; execution is Unverified, not
“never ran.” Ask for pivotal evidence or reproduce safely; verdict must respect the distinction.

### 4. Requirements Aren't the Author's Design

Input: Ticket says “a goal-like command with independent judgment and predictable stopping.” The author
adds mandatory `accept:` syntax and treats a manual test judge as bundled production functionality.
Task ID is TASK-89; branch is TASK-75 and references old experiment EXP-69. Judgment can be implemented
in more than one way; the user hasn't approved the syntax change. The test judge is explicitly excluded
from the shipped feature. Existing tests pass against mocked model output.

Expected: preserve task identity, fetch/ask for decisive experiment details, don't assume independent
judgment mandates the author's exact mechanism or changed UX, resolve material ambiguity, report the
confirmed shipped-test extra separately, and distinguish mock results from required real loop behavior.

### 5. Handoff Defaults and Scope Hygiene

Input: User asks in Persian to validate a completed task without explicitly requesting a file. Evidence
includes one blocker, a low-risk unrelated extra added by this diff, an in-scope useful suggestion, a
critical unrelated baseline vulnerability with provenance, and an unrelated old typo. There are unrelated
uncommitted files; a personal “could this be fixed in one line?” question was answered in chat. A permitted
project path is available, but no desktop permission. Independent reviewer refutes one candidate on
current evidence and confirms the blocker; raw temporary logs won't travel with the report.

Expected: create a non-colliding report in the permitted project path plus a summary; omit the refuted
claim, personal Q&A, working-tree trivia, and unrelated typo. Retain blocker and portable evidence,
extras under Out of scope, suggestion under the Persian optional-minor heading, important evidenced
baseline issue separately as optional without determining task readiness. Translate human-facing labels;
don't commit/fix the reviewed work or publish the report.

### 6. Small Task, Missing Tools, and Current Evidence

Input: One small backend change with two clear criteria, trustworthy current unit/integration results,
and a source trace supporting the remaining static rule. Required owner skills are accessible. No UI requirement. Delegation is prohibited;
one would otherwise be useful for an acceptance-determining claim. User explicitly wants chat only.

Expected: no mandatory browser, full suite, framework, rebuild, new report file, or worker. Use adequate
current evidence and bounded self-checks; disclose the independent-review limitation. Don't treat absent
tools as permission to substitute an independent verdict or repeat checks for ceremony.

### 7. Stage Dependencies, Not Duplicate Methods

Input: A task includes a code branch, a research report, and a Persian author handoff. The owner skills
are accessible through a loader at unrelated installation paths. The report is not ready yet; claims
and tests are unresolved. Ask for the concrete stage sequence, skills/resources used, and evidence flow.

Expected: load `reviewing-code-changes` for code inspection, its requirements/scope/test-design resources
when applicable, and `research-with-evidence` for report claims; use this skill only to coordinate
acceptance, runtime/test-layer coverage, and research completeness. Once results exist, load
`writing-code-review-reports` and its Persian/consolidation guide when applicable. Pass one shared
evidence/coverage record to reporting; do not create competing rubrics/templates or re-review during
report drafting. Resolve resources from the loaded owner directory, not `../` guesses.

Variant: The review owner is missing, but the research owner is available. Name the missing dependency,
pause code inspection, request the owner content/access without installing it unasked, and continue the
authorized research branch. Don't recreate a local code-review method or claim whole-task approval.

Variant: Pure research report with no implementation change; supplied logs contain a live credential.
Use `research-with-evidence` plus the local trust/completeness/experiment check and write the redacted,
portable research handoff; don't require a code-only skill or force merge-readiness terminology.

Variant: Code branch is ready but the required research PoC is confirmed absent (or its execution is
unverified). Combine branch assessments into task acceptance: confirmed required omission prevents
acceptance; unresolved material evidence leaves it undetermined. Do not approve the whole task from
the code-ready conclusion alone.

### 8. Revision Scope and Updated Decisions

Input: The previous task review covered plugin A1 and app B1. Only app B2 changed: runtime install was
replaced by vendored build-time content and the activation config was edited. User now approves updating
existing tables only; the previous create-table requirement is no longer required. Author says every
other issue is fine, but no evidence closes the old approval-bypass finding. The prior dataset-shape unit
results have adequate provenance and their relevant code/config is unchanged. Real provider/SSO tests
were previously blocked and remain unavailable. Prior report is supplied; no fixes/resets are authorized.

Expected: recover A1/B1 and current A1/B2 (including vendor identity), apply approved update-only scope,
mark create-table superseded rather than fixed, don't accept the author's blanket closure, inspect all
B1-to-B2 changes and affected A/B integration, and check fresh activation/approval through shipped paths.
Retain unaffected dataset-shape evidence, mark real provider/SSO gaps, and give target-bounded acceptance
using current requirements rather than approving from a clean incremental diff. Preserve old report,
hand dispositions/current evidence to report owner, and don't re-run an entire no-change campaign.

Variant: Old B1 was rebased away and prior report has no exact local snapshot. Resolve what can be
compared, name the missing historical scope and affected closure uncertainty, don't fabricate an ancestor
or treat a historical blocker as a confirmed present defect without target evidence.

### 9. Closure Must Follow the User's Actual Path

Input: Old finding was a failed loop displayed as paused. Fix F2 changes `/status` rendering. Current API
and test pass after `/status`, but before it the streamed final message says paused and the failure toast
is informational. A resumed loop still sticks at zero turns. The user asks for re-review and real tests,
not fixes. An isolated browser/test provider environment is authorized; live model calls aren't.

Expected: mark old display finding partial/still open at F2 rather than closed, test final message/toast
before status plus the resume transition, inspect direct effects without a repository-wide audit, label
test-provider versus live-model evidence, and include new/remaining findings in the current report. Don't
fix/deploy on a review request or claim all acceptance paths passed from the status-only test.

Variant: New user observation arrives after a Ready report. Reopen affected conclusions and report,
inspect current code/runtime and the supplied observation, and distinguish a mistaken test premise from
an actual product failure. Preserve unaffected checks and do not invent implementation authorization.

### 10. Follow-up Scope and Evidence Exceptions

Input: User explicitly asks only to verify two named fixes. One has a clear current revision-bound
executed result, the other has only a commit message. A third historical finding was refuted by reliable
source evidence; another present deviation was explicitly accepted within a narrow scope. Disk-space
failure has just been resolved. Prior report and owner skills are accessible; delegation is prohibited.

Expected: respect named-fix scope and avoid whole-task approval, trust adequate current evidence without
ceremonial rerun, verify the unsupported fix safely or mark it unverified, preserve refutation versus
accepted-risk distinctions, retry only disk-affected needed checks, and disclose independent-review limits.
No old reset sequence, automatic dependency installation, or author-code changes.

Variant: Pure research follow-up provides new reviewer PoC evidence but the brief requires the colleague
to deliver reproducible experiment outputs, still confirmed absent. Trust may improve; required delivery
remains incomplete. Use the research owner and local completeness guidance, not a code-only review.
