# Validating Research Deliverables

Open for a completed investigation, security assessment, experiment report, or other non-code output.
Validate the deliverable against the task, not a generic audit of everything related to its subject.

## Two Independent Questions

1. **Trustworthiness:** Are consequential claims and conclusions supported, accurate, and applicable to
   the intended version/environment? Are methods, sources, measurements, and qualifications sound?
2. **Completeness:** Did the colleague cover the requested questions and perform/deliver the required
   investigation, experiments, evidence, and exclusions?

A report can have correct source-level claims but omit a required executable experiment. Conversely,
many experiments don't rescue a wrong conclusion or work on the wrong deployment. If the reviewer
supplies new evidence, distinguish what the original delivery established from what is now verified;
don't misrepresent new reviewer work as work the colleague already delivered.

## Inspect Claims and Coverage

Read the supplied report, task, and material referenced evidence. Use an identifiable section/table/claim
locator; don't require source-code line numbers for a document finding. Build a compact claim/coverage
map for acceptance-critical claims and requested areas. Account for the whole deliverable; spend depth
on consequential claims and disclose any sampling rather than pretending every sentence was verified.

For each consequential claim check:

- Its exact proposition and conditions. Separate inherent design risks, deployment-specific
  misconfiguration, reachable vulnerabilities, and hypothetical attacks.
- Provenance: primary docs/source, version-pinned code/config, measured data, request/response,
  experiment output, or unsupported assertion. Follow the supporting section, not just the URL/title.
- Applicability: repository revision, upstream version, applied patches, image/build inputs, effective
  runtime config, dataset/population, relevant date and assumptions. An old local image or wrong branch
  cannot refute a report about a different deployment; resolve the mismatch before grading the claim.
- Reasoning: does the evidence establish the asserted mechanism and impact? Could an existing
  safeguard, another environment, correlated source, or narrower result explain the observation?
- Evidence availability: missing attached logs means execution is unverified unless stronger evidence
  establishes otherwise. Ask for pivotal missing evidence or reproduce safely; don't claim “never ran”
  merely because a document has no screenshot.

AI-generated reports, shared model chats, OCR, and repeated summaries are leads, not independent
confirmation. Verify version-specific public API/CVE/security claims with primary sources when material.
Quantitative scores need a defined rubric, data, denominator, units, and relevant comparison; do not add
confidence percentages or severity from rhetoric. Evaluate research design against its question, not
an unrelated ideal methodology.

Check requested questions and exclusions explicitly. A task asking for current security risks and
exploits but no replacement architecture is not fulfilled by a migration plan or product comparison.
Necessary context or a focused remedy isn't automatically scope creep; establish the mismatch.
Do not expand to retired/excluded components merely because they appear in the repository.

## Experiments and Security PoCs

When executable evidence is required, use [acceptance verification](acceptance-verification.md) for
layers and environments; the main skill links it directly as well. Establish:

- The tested proposition, relevant artifact/configuration, expected result, and meaningful counter-case.
- Actual steps/input, observed output or side effect, and repeatability conditions.
- Whether the real boundary under investigation ran, or a model/mock/source trace substituted for it.
- The authorized target, accounts/data ownership, write limits, costs, and evidence redaction.

For security tests, prefer two synthetic identities and synthetic secrets/canary data in an authorized
isolated environment. Verify both permitted and forbidden operations and their side effects. A theoretical
chain isn't an observed exploit, but it can be a supported risk if clearly labeled. Demonstrate only as
far as necessary for the claim; don't extract real credentials or access another user's private data.
“Read-only” does not automatically make secret access, cross-account requests, or remote scans authorized.
If the task requests PoCs but targets or permissions are unavailable, identify that verification gap and
its completeness impact; do not bypass it or launch a broad security campaign.

Distinguish a delivered method/experiment that demonstrably violates the agreed requirement from
unavailable evidence about an otherwise plausible experiment. The former can make the task Not ready;
the latter may require Cannot determine until evidence resolves it. A confirmed omission of a required
experiment/evidence deliverable is a conformance gap, even if source inspection supports the risk.

## Report the Current Assessment

For each material issue give the document locator, problem, concrete effect on trust/coverage, evidence
and limits, and a supported action: correct the claim, qualify the mechanism, supply missing evidence,
rerun on the intended artifact, or remove/separate confirmed extras. Don't prescribe a replacement
architecture in a task that explicitly excludes it.

Use the main skill's report spine with document locators and separate trust/completeness conclusions
where useful. Keep current supported findings and qualifications; remove superseded criticisms without
laundering unresolved uncertainty. Internal iteration history and side questions aren't author-facing
findings. A polished rewrite of the colleague's report is not a substitute for the requested validation,
and validation does not authorize editing their original deliverable.
