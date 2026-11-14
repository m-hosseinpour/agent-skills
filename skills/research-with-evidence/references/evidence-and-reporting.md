# Evidence Records and Research Reports

Open when evidence volume, reuse, or a requested report calls for a structured record or
output. This is an adaptable format, not a requirement for files, numbered citations,
recommendations, or a fixed set of report sections. Follow the main skill's evidence checks.

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
and the connection from evidence to conclusions. Distinguish verified source statements
from derived or unverified ones; a source being primary, or two sources agreeing, does not
make a result certain. Preserve ranges and disagreement rather than substituting an
unjustified midpoint. State what was inspected versus merely discovered, and do not imply
whole-report validation if the check was sampled.
