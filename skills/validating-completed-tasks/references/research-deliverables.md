# Validating Research Deliverables

Open for a completed investigation, security assessment, experiment report, or other non-code output.
Load `research-with-evidence` for claim validation: it owns source selection/fitness, provenance,
counterevidence, quantitative reasoning, and coverage reporting. This reference adds acceptance of the
delivered task, not a second research method or a generic audit of its whole subject.

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

Apply the research owner's source-fitness and evidence checks to the report's claims, keeping inherent
design risks, deployment misconfiguration, and demonstrated exploits distinct. Reconcile the target
revision, upstream version, build patches, image, and effective config before using local runtime
observations: an old image or wrong branch cannot refute a claim about another deployment. Missing
attached logs mean execution is unverified unless stronger evidence establishes otherwise, not “never
ran.” Ask for pivotal evidence or reproduce safely. Reuse the research owner's claim/evidence record.

Check requested questions and exclusions explicitly. A task asking for current security risks and
exploits but no replacement architecture is not fulfilled by a migration plan or product comparison.
Necessary context or a focused remedy isn't automatically scope creep; establish the mismatch.
Do not expand to retired/excluded components merely because they appear in the repository.

## Experiments and Security PoCs

When executable evidence is required, use [acceptance verification](acceptance-verification.md) for
layers and environments; the main skill links it directly as well. Add the experiment's required output
and actual execution to the research owner's evidence record, including relevant target/configuration
and whether a real boundary, model/mock, or source trace was used.

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

Pass the claim/coverage record and the two conclusions to the main skill's reporting stage, using the
owner method appropriate to pure research versus mixed work. Don't prescribe a replacement architecture
in a task that excludes it. A polished rewrite of the colleague's report is not a substitute for validation,
and validation does not authorize editing their original deliverable.
