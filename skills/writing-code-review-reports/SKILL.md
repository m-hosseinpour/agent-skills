---
name: writing-code-review-reports
description: Use when existing code-review findings need to be written, edited, translated, or consolidated into a handoff report for the author or another reader. Not for inspecting a diff, discovering defects, or performing a new review.
---

# Writing Code Review Reports

Turn existing review results into a report the reader can understand and act on without access to the reviewer's session. Write in the reader's language; translate headings, labels, and status names too. For Persian reports, use the Persian labels and template below; for other languages, translate them consistently into the reader's language. Preserve code identifiers, paths, and log text unchanged.

## Boundary and Inputs

Use this skill for the reporting stage, after findings and review evidence exist, including a report requested at the end of a review. A request to inspect a diff or judge a change belongs to `reviewing-code-changes`; a walkthrough explaining how a change works belongs to `understanding-a-merge-request`.

Collect the reviewed change and scope, findings with locations and impact, verification results and limits, and any stated requirements with their coverage and confirmed extras. If material information is missing, ask for it or mark the gap. Do not invent findings, imply a broader review, or turn report preparation into a new code review. This skill works from supplied results without requiring another skill to be installed.

## Structure

1. **Subject:** one line describing the reviewed change.
2. **Verdict:** ready, not ready, or cannot determine, with the main reason.
3. **Scope:** what the review covers and any important limits.
4. **Requirements** (only when stated requirements exist): use the coverage statuses below, including ambiguity, unavailable evidence, and respected or violated scope constraints. Include evidence and verification limits. Record confirmed extras separately with their severity in a subsection under Findings. Missing, partial, violated, and extra behavior also appears as findings.
5. **Findings:** most serious first. Put confirmed behavior beyond the agreed scope in a separate **Out of scope** subsection within Findings. For each finding, include:
   - **Problem:** what is wrong and where (file/line).
   - **Why it matters:** the concrete failure or cost.
   - **Action:** what change would address it.
6. **Confirmed:** important behavior or contract checked and found sound.

Use two severity levels for ordinary findings in a handoff report:

- **Blocking:** correctness, security, data-loss, or contract issue that must be resolved before merge. Confirmed missing, incorrect, partial, or unreachable required behavior is Blocking.
- **Important:** material issue worth fixing; if left, state why and any acceptable alternative supported by the review.

Do not transfer internal nits or optional suggestions into the handoff report, except confirmed extras: always retain those and label low-risk ones **Nit — scope mismatch** rather than inflating them to Important. Extras are behavior introduced beyond the agreed scope, not necessary supporting work or pre-existing behavior. Their severity follows concrete risk or cost; violating a hard acceptance constraint is Blocking. Recommend removal, separation, or explicit scope approval.

Keep each finding's concrete failure or cost and proposed action. Do not turn personal preference, uncertainty, or a pre-existing issue into a defect introduced by the change. Avoid local-only evidence, process narrative, dates, and claims the reader cannot check. Distinguish inspected code from executed checks, and checks the reviewer ran from results supplied by someone else. Preserve verification limits rather than implying an unrun check passed.

## Requirement Coverage and Verdict

Use these statuses for stated requirements. In a Persian report, use the Persian names shown here:

| English status | Persian label | Meaning |
| --- | --- | --- |
| Met | محقق‌شده | Reachable behavior matches the criterion and its stated edge cases |
| Partial | ناقص | Implemented but incorrect or incomplete; state the specific gap |
| Missing | تحقق‌نیافته | No implementation or no reachable path to it |
| Ambiguous | مبهم | More than one plausible reading; retain the unresolved question |
| Unverified | راستی‌آزمایی‌نشده | Required implementation, configuration, or runtime evidence is unavailable |
| Violated | نقض‌شده | A stated non-goal or scope constraint is implemented |
| Respected | رعایت‌شده | A stated non-goal or scope constraint stays out |

For explicit non-goals or scope constraints, use **Respected** or **Violated**, not Met or Missing. Present coverage in one table, with evidence and limits, rather than scattered findings. Do not invent requirement rows for unrequested behavior; report confirmed extras as findings under **Out of scope**, with their evidence and severity.

State readiness only for the reviewed scope and available evidence. Material unresolved requirements or missing evidence prevent an unqualified Ready verdict, but are not themselves confirmed defects. If the supplied review does not support a verdict, say readiness cannot be determined and identify what is missing. An empty findings list is not proof that the change is ready.

## Template

Omit the Requirements section when the change had no stated requirements. If confirmed extras still
exist, report them under the Out of scope subsection within Findings; omit that subsection when there are none. In Confirmed, include only supported checks; say none were
supplied when that is the limit rather than filling the section with inferred successes.

```markdown
# [موضوع کوتاه: چه تغییری بازبینی شد]

**حکم:** [آماده / آماده نیست / قابل‌تعیین نیست] — [یک یا دو جمله دربارهٔ دلیل اصلی و هر ابهام مهمِ حل‌نشده]

**دامنه:** [این بازبینی چه چیزی را پوشش می‌دهد؛ محدودیت‌ها یا موارد مهمِ بررسی‌نشده]

## الزامات

| الزام یا محدودیت دامنه | وضعیت | شواهد و محدودیت‌ها |
| --- | --- | --- |
| [معیار در یک سطر] | محقق‌شده / ناقص / تحقق‌نیافته / مبهم / راستی‌آزمایی‌نشده / نقض‌شده / رعایت‌شده | [مسیر:خط، گزاره/نتیجه یا شواهد در دسترس‌نبود؛ بررسی ایستا را از اجرای واقعی جدا کنید] |

## یافته‌ها

### [مانع ادغام / مهم] — [عنوان کوتاه]

- **مشکل:** [ایراد و محل آن، همراه با فایل و خط]
- **چرا مهم است:** [پیامد یا هزینهٔ مشخص]
- **اقدام:** [تغییری که مشکل را برطرف می‌کند]

### موارد خارج از دامنه

#### [مانع ادغام / مهم / کم‌اهمیت — خارج از دامنه] — [عنوان کوتاه]

- **مشکل:** [رفتار اضافه و محل آن، همراه با فایل و خط]
- **چرا مهم است:** [ریسک یا هزینهٔ مشخص، یا توضیح اینکه مورد کم‌اهمیت است]
- **اقدام:** [حذف، جداسازی از این تغییر، یا تأیید صریح دامنه]

## موارد تأییدشده

- [رفتار یا قراردادی مهم که بررسی و درستی آن تأیید شده است]
```

For Persian findings, translate severity labels as **مانع ادغام** (Blocking) and **مهم** (Important). Translate **Nit** or **Minor** as **کم‌اهمیت**; label a low-risk scope extra **کم‌اهمیت — خارج از دامنه**. Do not use English severity names in the Persian report.
