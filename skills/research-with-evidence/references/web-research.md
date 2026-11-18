# Web Research

Open when the investigation needs web discovery or retrieval. This guide supplements the
main skill's source-fitness and claim checks; it does not require live web access for work
that can be supported by supplied evidence.

## Contents

- [Choose available capabilities](#choose-available-capabilities)
- [Check freshness and access context](#check-freshness-and-access-context)
- [Search to close specific gaps](#search-to-close-specific-gaps)
- [Retrieve independent sources efficiently](#retrieve-independent-sources-efficiently)
- [Check extracted content before using it](#check-extracted-content-before-using-it)
- [Handle failures without manufacturing evidence](#handle-failures-without-manufacturing-evidence)

## Choose Available Capabilities

Check the session's actual search and retrieval capabilities and their documented inputs
and outputs before relying on them. Do not assume a tool name, provider, endpoint, schema,
or installed browser. One tool may support both discovery and reading; keep their evidence
roles distinct even when they share an interface.

- Discovery finds candidate sources. Prefer usable original URLs and clear metadata over
  redirect wrappers or snippets alone, without treating returned dates as verified facts.
- Retrieval lets you inspect supporting text, tables, figures, and context. A successful
  fetch can still return unusable or partial content; apply the extracted-content check below.
- For an exact API or product contract, use current official documentation or an authorized
  real request whose scope answers the question, not a guessed response schema.

If a required capability is absent, use authorized supplied material or accessible primary
documents when sufficient. Otherwise name what cannot be established. Do not claim to have
searched, opened, or tested sources when you have not.

## Check Freshness and Access Context

For time-, region-, or account-sensitive evidence, check the retrieval conditions that could
change the answer. Do not require these checks for an unaffected historical document.

- **Cached content:** a request made now may return an older cached copy. Inspect cache age
  or freshness metadata when exposed; use a documented fresh-fetch option when current state
  is pivotal and its cost is authorized. A retrieval timestamp alone does not establish
  live freshness. If freshness cannot be established, state that limit rather than invent it.
- **Relative dates:** resolve windows such as "last month" or "past six months" to explicit
  bounds from the current environment date before filtering. Use the relevant calendar and
  time zone when boundary events matter; clarify materially ambiguous windows. Search-result
  dates still need checking against the evidence period the question actually concerns.
- **Region and language:** inspect relevant search defaults and page locale. Language,
  access country, currency, and delivery location can change results, prices, or inventory.
  Match the question's region where supported and authorized; record a material mismatch or
  unknown context rather than presenting one region's result as universal.
- **Authenticated sources:** with authorized access, verify the intended account, tenant,
  or workspace and requested period before using its data. A saved session or successful
  login does not establish the right account. Keep the task read-only unless actions were
  authorized; never put credentials in research prompts, logs, or evidence records.

## Search to Close Specific Gaps

1. **Map the landscape when needed.** Begin with broad terminology for an unfamiliar or
   open-ended question, then follow useful terms, source types, and citations. A known
   narrow claim can start with an exact title, phrase, official domain, or primary record;
   broad-first is not mandatory.
2. **Refine with intent.** Search material subquestions and shared comparison criteria,
   not just one favorable query per option. Include failures, independent evaluations,
   exceptions, and contrary results when relevant. Use supported date filters or paging to
   change coverage, not repeatedly rephrase a query without learning anything.
3. **Match time and language.** For current state, check the relevant version and volatile
   facts directly; restrictive time filters can hide still-valid foundational sources.
   For a regional or language-specific question, search relevant local-language terms and
   wider technical literature when that could change coverage. Prefer local primary records
   for local facts. Neither Persian nor English nor a minimum language-source count is
   mandatory; disclose a material language/access gap instead of filling a quota.
4. **Change source class when useful.** If a general index is thin, try an available subject
   index, standards or official documentation, original data, bibliographies, or direct page
   reads. This closes coverage gaps; it is not permission to evade a denial.
5. **Read and retain support.** Follow the relevant claim to the original evidence. Record
   the actual URL/document identifier and supporting section. Where a canonical URL is
   exposed, use it for deduplication; do not guess a cleaner URL. Check whether extraction
   omitted the table, footnote, figure, or date on which the conclusion depends.

## Retrieve Independent Sources Efficiently

When the tool supports batch retrieval, group independent sources within its documented
capacity, service limits, and the working-context budget. Parallel calls are another option;
neither batching nor a fixed batch size is mandatory when sequential findings guide the next
request or the returned content would overwhelm the evidence review.

Inspect each source's result and error, not only the overall request status. Retain usable
sources from a partial batch and recover only affected gaps. Compare the requested URL with
the returned final URL when exposed: a redirect to a login page, regional homepage, or other
unrelated destination is not retrieval of the intended evidence. A legitimate redirect is
acceptable when source identity and supporting content are preserved.

## Check Extracted Content Before Using It

Confirm that the returned material is the intended source content, not just a successful
response. Warning signs include a challenge/login/consent wall ("verify you are human",
"checking your browser"), navigation or keyword lists in place of an article, broken encoding,
or undecoded PDF/binary internals such as `%PDF-`, `endobj`, or `FlateDecode` instead of text.
Classify by context, not a keyword alone: an article about CAPTCHAs can quote those phrases.

Length and punctuation are clues, not universal rejection thresholds. A short official
notice, table, code sample, or genuine word list can be relevant evidence. Verify source
identity and whether the content actually supports the claim; irrelevant boilerplate cannot.
For partial extraction, identify missing tables, footnotes, methods, or surrounding text
that could change the interpretation. A usable excerpt supports only a bounded claim whose
provenance and context limits are clear, not an assertion that the whole source was checked.

Do not admit unusable content as support or cite its URL as if the source had been read.
Use the recovery choices below for the affected source, retaining valid evidence elsewhere.

## Handle Failures Without Manufacturing Evidence

Classify from response content and context, not the status code alone. A `403` can mean a
technical or regional restriction or an actual access denial; an unknown cause stays unknown.

| Observed problem | Appropriate next step |
| --- | --- |
| Transient timeout or connection reset during ordinary retrieval | Use a bounded retry when justified by tool/service guidance; stop repeating if it does not resolve the gap. |
| Timeout or lost response from a request that starts a server-side job | Recover the existing job and inspect its status/result before considering another start; follow the job guidance below. |
| Rate limit, exhausted quota, or degraded service | Reduce concurrency; respect any retry-after guidance and budget. Use another permitted source class or report the limit, rather than multiplying requests. |
| Empty results | Reassess terms, filters, language, or index coverage. An empty result alone proves neither a service failure nor absence of the fact. |
| Incomplete extraction or dynamic public page | An available, authorized browser or alternate format may recover the missing content. Do not silently treat partial text as the full source. |
| Known regional/network restriction or technical challenge | Use an available authorized access method only if it respects tool and site boundaries; do not defeat an access-control or security-policy block. |
| Login, missing credentials, paywall, explicit access denial, or security-policy block | Request authorized access if pivotal, use other legitimately available evidence, or record the gap. Do not bypass the boundary with another tool, proxy, or agent. |

For a server-side research, extraction, or browser job, retain the returned identifier.
A client timeout does not prove the job stopped or never started. If the identifier was lost,
use an available authorized job lookup to find the matching run; do not guess an ID or start
another job just to discover what happened. Inspect the existing run's status, result, and any
partial effects. A terminal failure status does not prove the run produced no usable output
or side effects.
Restart only when evidence establishes that repeating the unresolved work is safe and within
authorization and budget. If status or effects cannot be determined, disclose the uncertainty
and avoid a blind restart. Follow the service's documented wait/notification mechanism;
do not cancel a run merely because it is slow or create paid work without authorization.

For known regional restrictions, `targeted-proxy-access` from this catalog can help **if
available and authorized**. Load it by name and use its actual installed directory; do not
assume sibling paths, supplied proxy credentials, or permission to install or reconfigure
services. Without it, continue with accessible evidence or report the gap.

A search snippet is a lead, not verified support for a substantive claim. If the original is
unavailable but an accessible independent source supports a bounded claim, cite what you
actually inspected and disclose the original-source gap. Do not list the unread original
as if verified. Keep working evidence and source locators when a service fails mid-run;
bound only the affected conclusions rather than discarding valid evidence.
