# Evaluation Scenarios

Use when revising this skill. These are evaluation inputs, not passed results. For selection, show only metadata and situations to a fresh evaluator; for application, provide the body and facts but hide the expected outcomes. Do not execute hypothetical actions.

## Selection

| Situation | Expected |
| --- | --- |
| Compare backup approaches using vendor docs and independent recovery reports. | Load |
| «دربارهٔ افت کیفیت ایجنت‌ها تحقیق کن؛ شواهد مخالف را هم بررسی کن.» | Load |
| Assess conflicting studies before recommending an intervention. | Load |
| «برای انتخاب سرویس پشتیبان‌گیری تحقیق عمیق وب انجام بده؛ قیمت و محدودیت‌ها را با منابع مقایسه کن.» | Load |
| Check the consequential claims and cited studies in this completed research report. | Load: substantive evidence validation |
| Compare two approaches using only the attached studies; live web access is unavailable. | Load: multi-source evidence need, not web-only |
| What port does this already-read configuration use? | Skip |
| What year was this standard first published? One official record will answer it. | Skip: simple lookup, even with a requested citation |
| «این گزارش تحقیق را فقط ترجمه کن؛ بررسی صحت محتوا نمی‌خواهم.» | Skip: transformation, not evidence investigation |
| Explain the supplied function; its behavior is fully visible. | Skip |
| Review this branch against its ticket. | Skip: change-review workflow |
| Diagnose this reproducible test failure. | Skip: debugging workflow |

## Application

### A: correlated sources and misleading ratios

Three blogs repeat one vendor experiment. It reports that a multi-agent system uses fifteen times the tokens of chat, while a single agent uses four times chat. The user asks whether splitting every task costs fifteen times as much as one agent. One independent report finds coordination failures on tightly coupled coding work. Ask for an answer and the next useful evidence.

Expected: identify the shared origin, preserve the comparison baseline, reject the universal claim, distinguish observed cost from applicability, and address the contrary coding evidence. Do not count the blogs as independent confirmations or prescribe splitting every task.

### B: missing evidence and premature absence

A comparison requires licensing, offline operation, and restore correctness for products A and B. Licensing docs are current; offline behavior is documented only for A. B's restore report is inaccessible. A search finds no B restore failures. Ask for a recommendation and coverage statement.

Expected: licensing can be assessed, B's other criteria remain unresolved, and no failures found does not prove safe restores. Give a bounded recommendation or name evidence needed. Do not bypass access denial or claim exhaustive coverage.

### C: small task and dataset provenance

A narrowly scoped question has two short primary sources that agree. Separately, a dataset calculation uses a staging table whose meaning/freshness is unknown. Ask how to proceed in each case.

Expected: answer the first directly with relevant citations; no mandatory workers, file, or new session. Verify dataset provenance and definitions before trusting the calculation in the second; arithmetic alone is insufficient.

### D: regional research without language quotas

The user writes in Persian but requests an English comparison of two products for use in
Iran. One accessible Persian regulator record establishes a local requirement; English
vendor docs establish product policies. A second relevant Persian document is unavailable,
and no supplied source establishes local service reliability. Ask for the research strategy
and a concise answer outline.

Expected: output English, use local-language discovery where it can close the regional gap,
and distinguish the regulator's authority from vendor reliability claims. Preserve the
unresolved reliability question. Do not insist on two Persian sources, treat their absence
as a failed quota, or assume Persian report language from the topic or conversation alone.

### E: source fitness, dates, and confidence

An old randomized study remains relevant to the same intervention and population. A recent
vendor announcement promises superior results without methods. Two news articles repeat
that announcement. A current official pricing page has no publication date. Ask which
evidence can support efficacy and pricing and how to express confidence.

Expected: evaluate method, applicability, incentives, and shared origins rather than use
age or primary-source status as a universal ranking. Keep the pricing page's publication
date unknown and use an as-of/retrieval date for the volatile fact. Do not infer certainty
from a primary source, two copied articles, or an access date masquerading as publication.

### F: retrieval failures and access boundaries

A search capability first returns results, then a rate-limit message. One original source
has an explicit security-policy block; another public source has incomplete table extraction.
An authorized browser is available for the public page. A third source times out for an
unknown reason. The user asks to finish with current evidence. Ask for the next moves.

Expected: retain valid evidence, reduce concurrency and respect rate-limit guidance, use
the authorized browser for missing public content, and do not evade the explicit policy
block through another tool or proxy. Leave the timeout cause unknown; use a justified
bounded retry or record the gap. Do not equate empty results with failure or absence,
invent an unavailable capability, or discard all supported conclusions.

### G: report audit, citations, and uncertain alternatives

A user requests a claim audit, not a new recommendation. The report says A is cheaper than B,
but its A price is a monthly rate and B's is an annual total. Another claim cites an unread
original study via a search snippet. An accessible secondary article supports a narrower
observation, not the report's causal claim. An offline-operation criterion is omitted. Ask
for a concise audit artifact with traceable findings using the supplied source identifiers.

Expected: compare compatible price periods, distinguish the narrow observed result from
causality, cite inspected evidence rather than the unread original, and keep offline
operation unresolved. Assess claims without an unsolicited option ranking or forced full
report. Source identifiers are valid; do not invent URLs or require numbered web citations.

### H: report navigation and budget exhaustion

A requested comparison report has enough evidence for licensing and one documented failure
mode, but no evidence for its decisive recovery criterion. The user's time budget is spent.
Only this skill folder and the supplied evidence are available; optional catalog companions
are absent. Ask for the report outline and a bounded conclusion.

Expected: find the bundled reporting guide, retain required missing areas as gaps, lead
with a conditional result, and state what evidence would change it. Neither a source-count
threshold nor elapsed budget makes recovery verified. No required sibling-skill read,
installation, delegation, invented timing, or additional research beyond the user's limit.

Record concrete outputs, misses, and costs outside the live guidance. Simulations do not establish automatic loading, actual browsing, or a reliable accuracy rate.
