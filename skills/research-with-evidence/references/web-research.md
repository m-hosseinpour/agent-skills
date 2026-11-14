# Web Research

Open when the investigation needs web discovery or retrieval. This guide supplements the
main skill's source-fitness and claim checks; it does not require live web access for work
that can be supported by supplied evidence.

## Choose Available Capabilities

Check the session's actual search and retrieval capabilities and their documented inputs
and outputs before relying on them. Do not assume a tool name, provider, endpoint, schema,
or installed browser. One tool may support both discovery and reading; keep their evidence
roles distinct even when they share an interface.

- Discovery finds candidate sources. Prefer usable original URLs and clear metadata over
  redirect wrappers or snippets alone, without treating returned dates as verified facts.
- Retrieval lets you inspect supporting text, tables, figures, and context. A successful
  fetch can still be a login wall, truncated extraction, or an empty page; inspect the content.
- For an exact API or product contract, use current official documentation or an authorized
  real request whose scope answers the question, not a guessed response schema.

If a required capability is absent, use authorized supplied material or accessible primary
documents when sufficient. Otherwise name what cannot be established. Do not claim to have
searched, opened, or tested sources when you have not.

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

## Handle Failures Without Manufacturing Evidence

Classify from response content and context, not the status code alone. A `403` can mean a
technical or regional restriction or an actual access denial; an unknown cause stays unknown.

| Observed problem | Appropriate next step |
| --- | --- |
| Transient timeout or connection reset | Use a bounded retry when justified by tool/service guidance; stop repeating if it does not resolve the gap. |
| Rate limit, exhausted quota, or degraded service | Reduce concurrency; respect any retry-after guidance and budget. Use another permitted source class or report the limit, rather than multiplying requests. |
| Empty results | Reassess terms, filters, language, or index coverage. An empty result alone proves neither a service failure nor absence of the fact. |
| Incomplete extraction or dynamic public page | An available, authorized browser or alternate format may recover the missing content. Do not silently treat partial text as the full source. |
| Known regional/network restriction or technical challenge | Use an available authorized access method only if it respects tool and site boundaries; do not defeat an access-control or security-policy block. |
| Login, missing credentials, paywall, explicit access denial, or security-policy block | Request authorized access if pivotal, use other legitimately available evidence, or record the gap. Do not bypass the boundary with another tool, proxy, or agent. |

For known regional restrictions, `targeted-proxy-access` from this catalog can help **if
available and authorized**. Load it by name and use its actual installed directory; do not
assume sibling paths, supplied proxy credentials, or permission to install or reconfigure
services. Without it, continue with accessible evidence or report the gap.

A search snippet is a lead, not verified support for a substantive claim. If the original is
unavailable but an accessible independent source supports a bounded claim, cite what you
actually inspected and disclose the original-source gap. Do not list the unread original
as if verified. Keep working evidence and source locators when a service fails mid-run;
bound only the affected conclusions rather than discarding valid evidence.
