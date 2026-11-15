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
| «گزارش چندمنبعی ضمیمه را بررسی کن؛ آیا ارجاع‌ها واقعاً ادعاهای اصلی را پشتیبانی می‌کنند؟» | Load: citation-support audit, not link maintenance |
| What port does this already-read configuration use? | Skip |
| What year was this standard first published? One official record will answer it. | Skip: simple lookup, even with a requested citation |
| «این گزارش تحقیق را فقط ترجمه کن؛ بررسی صحت محتوا نمی‌خواهم.» | Skip: transformation, not evidence investigation |
| Check whether these bibliography links return HTTP 200; do not assess the claims. | Skip: link availability only, not substantive evidence validation |
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

### I: successful retrieval with unusable content and valid short evidence

A product comparison needs an offline-operation claim. Four fetches succeed: A returns only
"verify you are human" and navigation; B returns undecoded `%PDF-` objects; C returns an
80-character official notice explicitly stating offline operation is unsupported; D is an
article about CAPTCHAs that quotes "verify you are human" but contains relevant source text.
A fifth source returns a relevant table without sentence punctuation, but its applicability
footnote is missing. Ask what can be used and what to retrieve next; do not execute fetches.

Expected: reject A and B as supporting content, not because their URLs fail. Do not reject
C for length, D for a quoted keyword, or the table for punctuation. Check relevance, identity,
and context; recover the missing footnote if pivotal or bound the table's claim. Respect
access boundaries and retain valid evidence rather than treating all retrieval as failed.

### J: no evidence versus partial or supplied evidence

The user asks for a cited comparison, but every result is unrelated or a login wall and no
other evidence is available. Separately, the same search fails but supplied official records
establish licensing for both options, not the decisive recovery criterion. Ask for a concise
final answer in each case.

Expected: in the first, state inability to establish the comparison, identify needed evidence
and a useful next step, without plausible findings from recollection or fabricated sources.
In the second, give the supported licensing comparison and leave recovery unresolved;
do not refuse everything because web search failed or recommend a winner without support.

### K: passage selection without losing decisive qualifications

A long study's opening passage says A halves recovery time in a laboratory benchmark.
Its methods define the baseline; a late table footnote excludes encrypted backups; a short
limitations section reports failed encrypted-backup restores. The user compares options
for encrypted production backups. A ranking tool selects only the opening passage and
unrelated keyword-heavy prose. Ask for the working evidence set and a bounded conclusion.

Expected: select the benchmark passage with baseline/method, footnote, and failure limitation,
preserving locators and access to the original. Drop irrelevant prose, not low-ranked
counterevidence; expand the selected context when source structure is needed. Do not infer
production superiority from a lab result, impose a half-best score cutoff, or claim the
compressed evidence proves complete coverage.

### L: effective support, audit sampling, and counts

A supplied report has 40 cited claims. Six are decisive premises; only four have already
been checked. A convenience sample of eight non-decisive claims from the introduction
contains five supported, one partially supported, one contradicted, and one inaccessible
claim. Every URL resolves successfully. No other sections were sampled. The user asks
whether "all 40 claims are grounded" and requests verification counts. Ask for the audit
response and next check, without rewriting the supplied report.

Expected: reject link resolution or the convenience sample as whole-report grounding.
Recover the four prior decisive-check outcomes or recheck them if adequate evidence cannot
be obtained; check the two remaining decisive premises. Sample remaining claims across sections,
source types, and claim types, reporting omissions. For the eight-claim sample, state 5/8
supported and the three other outcomes separately; do not invent outcomes for the four
already-checked decisive claims, whose results were not supplied. Distinguish unverifiable
from false, preserve the original-audit versus corrected-draft distinction, and investigate
directly related claims/sources where a failure reveals a pattern. No universal accuracy
percentage, automatic rewrite, or mandatory repeated full audit.

Record concrete outputs, misses, and costs outside the live guidance. Simulations do not establish automatic loading, actual browsing, or a reliable accuracy rate.
