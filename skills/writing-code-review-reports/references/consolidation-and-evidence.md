# Consolidation and Evidence

Open when merging reviewer outputs or handling duplicates, conflicting claims, code-state drift,
or difficult verification provenance. Reporting organizes available evidence; it does not authorize
reopening code review, rerunning tests, or fixing findings.

## 1. Establish what each source covers

For each report, identify the reviewed revision/local scope, baseline, covered paths, requirements,
findings with their evidenced relationship to the change/requirements, and checks with their results. Preserve whether the reviewer executed a check or relied on
another source. Report timestamps may help establish order but do not identify a code state.

Determine the report's intended target from the request and supplied inputs. Do not assume the latest
timestamp refers to the current checkout. When the target or an essential revision is unknown, ask
or mark that gap instead of building a current verdict from mixed snapshots.

For complicated inputs, a small working table can help; it is not a mandatory report section:

| Claim | Source/revision | Evidence | State at target | Next needed input |
| --- | --- | --- | --- | --- |
| Guard missing | A, H1 | `src/api.ts:20`, traced path | Historical; target unknown | Target revision and guard evidence |
| Guard fixed | B, H2 | Fix claimed; test command absent | Reportedly resolved at H2, not confirmed current | Revision-bound fix/check result |

Read supplied reports and linked supporting results to resolve factual transcription gaps. If determining
actual current behavior needs new code inspection or execution, identify that as follow-up review work,
not a check silently performed under report-writing scope.

## 2. Deduplicate without erasing distinctions

Group reports of the same underlying failure at the same relevant code state. Keep distinct callers,
conditions, affected versions, and verification evidence within the grouped finding. Similar titles are
not proof of a common cause; one location can contain different defects.

Do not count repeated log entries as several defects. Do not merge one historical finding and one
new failure into an apparently continuous current issue without evidence. Preserve a reported
resolution as such; omit resolved historical findings from the active list only when target-specific
supplied evidence supports resolution, retaining a short history note when useful or requested.

## 3. Reconcile conflicts explicitly

- **Different revisions:** both accounts may be correct for their versions. Label each and obtain target-specific evidence; neither is automatically current.
- **Same revision, contradictory claims:** keep the conflict visible with both sources and identify what resolves it. Do not pick the more senior reviewer or newest wording as proof.
- **Different criteria:** per-user enforcement does not prove a per-account requirement. Preserve the agreed criterion; if supplied evidence genuinely proves a mismatch, report it. Otherwise mark the coverage dispute/unverified evidence, not a new defect discovered during writing.
- **Different severity rubrics:** map only defined equivalent meanings. Preserve undefined labels with their gap; do not choose the highest severity merely to be safe. A confirmed required gap or hard constraint violation must be reconciled with the main skill's Blocking rule for a composed handoff, not quietly regraded.
- **Reported fixes:** a bare “fixed” or “tests pass” does not establish resolution at the intended target. Trust clear, relevant, revision-bound supplied evidence without demanding an independent rerun merely for ceremony.

Do not fabricate a remedy to make a finding look complete. Preserve a supplied action and acceptable
alternatives; otherwise say the correction plan is missing and request it. A material unresolved
question remains visible even when not listed among confirmed findings.

## 4. Preserve portable verification evidence

Keep code state, command/scenario, observed result, relevant environment, source, and necessary
conditions. A concise source trace is not an execution result; reading a test does not mean it passed.
A build may establish compilation without proving authorization or runtime behavior. A review's
successful focused check supports only the relevant behavior, not automatically the whole change.

Distinguish known baseline failures from introduced regressions only when supplied baseline evidence
establishes that difference. Do not erase an already-red suite or call its failures newly introduced.
If checks apply to an older state, qualify which evidence remains relevant and what is stale. Report
known revision drift without assuming all old results are useless or that all still apply.

Apply the main skill's scope filter when composing the consolidated handoff: important unrelated
pre-existing issues belong only in their separate optional section; unrelated minor issues are omitted.
Baseline evidence must establish the pre-existing failure, not merely that its file or lines are unchanged.
Do not filter out an agreed requirement gap or new impact from the change. If sources disagree about
this relationship, retain the material uncertainty and name the missing evidence rather than guessing.

Portability and privacy are not reasons to delete the proof:

- Convert a known project-root prefix to a repository-relative path. If unknown, retain a clearly marked `[PROJECT_ROOT]` placeholder and name the unresolved mapping.
- Redact tokens, secrets, personal records, and unnecessary private environment identifiers in snippets, commands, and logs. Keep surrounding syntax and a clear placeholder; state that it was redacted rather than claiming a literal reproduction command.
- Keep a material timestamp or environment fact when it establishes freshness, order, or reproducibility. Omit incidental session narrative.
- Use exact supplied lines/symbols or pinned links; if a location is missing, mark it missing. Do not invent a new line number by assuming the current checkout matches the report.

## 5. Produce an evidence-bounded verdict

The main skill owns severity and readiness. A confirmed current in-scope Blocking issue means Not ready,
even if another path is unverified. With no confirmed blocker but material conflicting/unavailable
evidence, use Cannot determine and name the required input. Historical defects do not become
current blockers just because their resolution is uncertain. Important unrelated pre-existing issues
may warrant separate urgent follow-up, but alone do not make this task Not ready or Cannot determine.

State the scope and target the verdict concerns; preserve material exclusions. Faithful translations
retain the source verdict, attributed to the source, with any necessary caveat separate. Do not
turn a report into independent merge approval or a publication action.
