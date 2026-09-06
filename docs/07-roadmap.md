# Research roadmap

Status: proposed experiments and future directions, not delivery commitments.

## Current baseline

The repository contains one project-approved experimental scenario, a scenario schema, a compact ATT&CK snapshot, integrity tooling, and early code and tests. The existing CIA scoring has [documented limitations](validation-status.md). A complete assessment workflow and demonstrated practical benefit remain to be established.

## Next milestone: a small, reviewable assessment example

Proposed scope:

- one synthetic system with explicit service, asset, account, and data context;
- two or three scenarios with applicability rationale;
- five to ten independently authored controls with mapping rationale and evidence expectations;
- proposed impact criteria with evidence requirements and explicit handling of unknown information;
- cases on both sides of rating boundaries, including an insufficient-evidence case;
- a reproducible human-readable output and a small OSCAL Catalog/Profile experiment.

The numbers bound the experiment; they are not coverage or quality targets. No new scoring scale or thresholds are approved by this roadmap. Attack Flow or D3FEND integration should be added only if needed to test the selected cases.

## Success criteria

- A reviewer can trace each applicability, impact, and control-mapping judgment to its criteria, evidence, assumptions, and source versions.
- Boundary cases make the distinction between adjacent impact categories explicit; missing evidence is not treated as low impact.
- A second practitioner can attempt the example without oral guidance. Record disagreements and revisions rather than assuming reviewer agreement.
- Compare the approach with a simple manual assessment of the same cases using review time, omissions, and clarity of decisions. Record the evaluation procedure and limitations; do not claim improvement unless supported by the results.
- Generated artifacts are structurally valid and reproducible. Passing these checks demonstrates the technical path, not methodological correctness.

## Expansion gate

Review the example and its evaluation before expanding the library or regulatory scope. If it does not show useful, explainable results, revise the method or reduce scope. Revised approved scenarios require new versions and review decisions.

## Future directions

Subject to evidence from the first milestone:

- broader ATT&CK ingestion and semantic change analysis;
- Attack Flow and D3FEND adapters;
- additional scenario families and control mappings;
- one bounded regulatory slice, with source-level traceability and human review;
- assessment evidence, findings, treatment, and later residual-risk experiments;
- additional OSCAL models, integrations, or UI where a demonstrated use case warrants them.

DORA, NIS2, and Greek ADAE sources remain candidate research directions. Their mention does not imply implemented regulatory coverage or compliance assurance. Delivery dates will be reconsidered after measuring implementation and review effort on the first milestone.
