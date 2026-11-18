# Evidence Records and Research Reports

Open when evidence volume, reuse, a requested report, or entity collection calls for a
structured record or output. This is an adaptable format, not a requirement for files,
numbered citations, recommendations, or a fixed set of report sections. Follow the main
skill's evidence checks.

## Contents

- [A compact working record](#a-compact-working-record)
- [Collect structured entity records](#collect-structured-entity-records)
- [Select working passages](#select-working-passages)
- [Choose the output size](#choose-the-output-size)
- [Adaptable report skeleton](#adaptable-report-skeleton)
- [Citation and final consistency check](#citation-and-final-consistency-check)

## A Compact Working Record

Use a single record or index when helpful. One row per consequential claim can be enough:

| Question / claim | Evidence and locator | Applicability | Assessment / gap |
| --- | --- | --- | --- |
| What is asserted or compared? | Source ID + supporting passage, table/page/section, or observed result | Date/version, population, method, units and baseline as relevant | Supported, derived, disputed, unresolved, sampled, or inaccessible; what remains to check |

Keep source details behind each ID: title, author/publisher when known, actual URL or document
identifier, publication/update date when available, and relevant version or evidence period.
For changing web facts, retain retrieval/as-of dates separately. Mark missing metadata as
unknown; do not invent it. Trace common origins so copied reports are not counted as
independent evidence.

For calculations or observations, retain inputs, definitions, filters, comparison conditions,
method or command, relevant environment/version, and actual result. A file path or dataset
name alone does not establish provenance. Use portable locators or attach authorized evidence
for the intended reader; do not publish private files, credentials, or machine-specific paths.

When sources conflict, keep both claims with their locators and conditions in this same
record. Note whether the disagreement is explained by scope/method, remains unresolved,
or changes the conclusion. A separate contradiction ledger is unnecessary unless volume
makes one useful. Summaries must preserve qualifications and pointers to original detail.

## Collect Structured Entity Records

For requests such as "find 30 companies meeting these conditions," decide what qualifies as
an entry, which fields answer the request, and how to identify the same entity before bulk
extraction. Initial discovery may refine the schema, but it must not silently relax the
user's conditions to fill rows. A short list needs only lightweight checks, not a new
dataset service, file, or formal schema.

- **Qualification:** translate hard constraints into evidence checks, including relevant
  dates, regions, units, and thresholds. Finding a candidate does not establish eligibility.
  Distinguish verified matches from candidates with unresolved decisive criteria. If ranking
  is requested, make its criteria explicit and keep unknown values from scoring as successes.
- **Identity and deduplication:** choose a key that fits the entity, such as an official
  identifier or a verified name/domain combination. Different URLs can describe one entity;
  one domain can contain several entities. Do not collapse namesakes, subsidiaries, or
  branches without checking what the requested unit represents.
- **Field evidence and merges:** retain source locators and applicable dates for important
  fields. Merge only after establishing identity and compatible meanings. A newer or fuller
  record is not automatically a better source; preserve conflicting values and conditions
  instead of silently overwriting them or constructing an unsupported composite record.
- **Missing-value meaning:** distinguish unknown, not checked, confirmed absent, and not
  applicable, using a status or note when needed. A missing key or `null` alone proves neither
  that a field was checked nor that the fact is absent. Preserve zero, false, and unlimited
  values according to their documented meaning rather than treating them all as missing.
- **Final validation:** check returned entries against qualification and identity rules,
  required fields, and field evidence. Count unique qualified entities separately from raw
  candidates and source URLs. Report a target shortfall and the affected coverage or budget
  limit; do not pad the list or claim the web contains no further matches without adequate
  evidence. A structured result or completed dataset is not itself factual verification.

## Select Working Passages

For long sources or a large corpus, keep a compact evidence set per material subquestion
rather than carrying whole pages or cutting off their tails. Select passages that answer,
challenge, or qualify the claim; a topically similar passage need not support it. Retain
headings, source IDs and section/page locators, and enough neighboring text to preserve
definitions, table units, footnotes, methods, and exceptions. Keep the original retrievable.

Choose passage boundaries by meaning and source structure. A full section or document may
be necessary when the argument depends on its structure. If retrieval/ranking tools are
available, inspect what their selection omitted before relying on it for a decisive claim;
do not adopt fixed chunk lengths or relevance cutoffs without task-specific evidence.
Compression is a context/cost choice, not verification or proof of corpus-wide coverage.

## Choose the Output Size

- **Short answer:** result, relevant citations, and material caveats. A source list is useful
  if inline links do not carry enough context; no full report ceremony.
- **Substantial report:** a scoped synthesis organized by material questions or shared
  comparison criteria. Use the skeleton below, retaining only sections that help the reader.
- **Claim audit:** an assessment of the supplied report, disputed/unsupported claims with
  report locators and source evidence, and verification/coverage limits. Do not replace it
  with an unsolicited product recommendation. If full task acceptance is requested,
  `validating-completed-tasks` can coordinate completeness when available; this skill owns
  the research claims, not whether every non-research deliverable was completed.

Required areas with missing evidence stay visible as gaps, even if a template's empty
optional section is omitted. The output can stay in chat unless the user requests an artifact
or durability warrants one within authorized paths. Use the requested language, normally
the conversation's language when unspecified; keep source titles and product/version names
recognizable. Local-language research requirements come from the question, not report language.

## Adaptable Report Skeleton

```markdown
# <Specific title>

As of: <relevant date/version, if time-sensitive>

## Answer or assessment
Lead with the result. Put decisive conditions and limitations here, not only at the end.

## Scope and approach
Question/decision, shared comparison criteria or material subquestions, relevant
population/region/versions, and deliberate exclusions. Summarize methods and access
limits to the detail needed to assess the result; include effort metrics only if useful
or requested and actually measured.

## Findings
Organize by question or comparable criterion. Put a supporting citation near each
consequential factual claim. Label calculations, interpretations, and assumptions.
An unknown cell in a comparison stays unknown rather than implying the option passed.

## Evidence or comparison table (when useful)
| Criterion / claim | Finding and conditions | Evidence | Uncertainty |
| --- | --- | --- | --- |
| ... | ... | [1], document/page, or observation ID | ... |

## Disagreements and gaps
Show materially different results and whether scope/method explains them. Name unresolved
questions, sampled areas, inaccessible evidence, and their effects on the answer.

## Recommendation (only when requested or useful to the decision)
Connect the choice to the user's criteria and evidence. Address a credible alternative
and relevant costs/risks. State what evidence or conditions would change the choice;
use a conditional recommendation when a decisive premise is unresolved.

## Sources / evidence
1. <Original title> — <publisher/author if known> — <date/version if known> — <actual URL or document ID>
```

## Citation and Final Consistency Check

Choose one readable citation convention. Inline links and document/page locators are valid;
with numbered `[n]` markers, make every marker resolve to its matching source. Do not cite a
page merely because its title sounds supportive, or attach one citation to a paragraph of
claims it does not support. A source list is not a substitute for traceable claims.

Verify the support for consequential claims and numbers, their relevant conditions and dates,
and the connection from evidence to conclusions. For a substantial report or claim audit:

1. **Identify checkable claims.** Split mixed assertions when one citation supports only
   part of a sentence. Start with decisive premises, recommendations' factual foundations,
   quantitative comparisons, disputed claims, and support weakened by extraction/compression.
2. **Inspect the cited support.** Match each checked claim to the actual passage, table,
   or observation and its conditions—not the title or a resolving link. Reuse adequate
   inspected evidence; reopen the source when detail is missing or the claim has changed.
   Record supported, partially supported, contradicted, unsupported, or unverifiable, with
   a locator and reason. Missing access is unverifiable, not proof of falsity; a successfully
   opened but unrelated passage is not supporting evidence. A prior check with no available
   outcome or supporting evidence remains unverified; recover that record or check it again.
3. **Bound sampling honestly.** Check every decisive premise. For a large supplied report
   or an additional spot-check, sample remaining claims across sections, source types, and
   claim types, not only easy citations. State the selection and omissions; sampling does
   not replace support for consequential claims in your own answer. A failed check warrants
   inspecting directly related claims or shared sources, not declaring the rest verified.
4. **Correct and report.** Correct, narrow, or remove unsupported assertions in your own
   draft; when auditing someone else's report, report the finding without rewriting it
   unasked. If verification counts help or are requested, give the number supported out of
   claims checked, with partial, contradicted, unsupported, and unverifiable outcomes distinct. State
   whether counts describe the original audit or a corrected draft. Citation totals or a
   sampled support fraction are not whole-report accuracy, completeness, or confidence.

Distinguish verified source statements from derived or unverified ones; a source being
primary, or two sources agreeing, does not make a result certain. Preserve ranges and
disagreement rather than substituting an unjustified midpoint. State what was inspected
versus merely discovered, and do not imply whole-report validation if the check was sampled.
