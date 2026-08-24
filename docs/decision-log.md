# Decision Log

This log records major project architecture, methodology, licensing, release-boundary, and implementation decisions.

Decisions may be revised, but changes should be explicit and versioned. The purpose of this file is to make reasoning, assumptions, trade-offs, and review triggers visible over time.

## How to use this log

Add or update an entry when a decision:

- changes the project direction;
- accepts an important trade-off;
- defines scope or out-of-scope boundaries;
- selects a standard, framework, model, technology, or license;
- affects public release readiness;
- affects clean-room / IP boundaries;
- affects security, privacy, evidence, or assurance logic.

Keep entries short enough to be readable, but specific enough that a future reader can understand why the decision was made.

## Status values

- `Proposed` — under discussion, not yet accepted.
- `Accepted` — current project position.
- `Accepted as design direction` — accepted as the current direction, but still expected to evolve.
- `Superseded` — replaced by a later decision.
- `Rejected` — considered but not adopted.
- `Deprecated` — previously used, but should no longer guide new work.

## Decisions

## D-001 - Independent clean-room project

**Status:** Accepted

The project will be developed independently from any employer-specific methodology, control library, questionnaire, tooling, dataset or wording.

Rationale: reduce IP/confidentiality risk and create a genuinely independent research/product foundation.

## D-002 - Threat-informed scenario foundation

**Status:** Accepted as design direction

MITRE ATT&CK will be used as a principal structured source of adversary behaviour. ATT&CK techniques are inputs to risk scenarios, not risk scenarios themselves.

## D-003 - Do not build a new attack-sequencing standard

**Status:** Accepted as design direction

Use MITRE Attack Flow where attack sequencing is needed instead of inventing a proprietary attack-flow language.

## D-004 - Human-certified methodology

**Status:** Accepted

Machine-generated scenarios and mappings are candidates only. Human approval is required before a scenario or scenario-to-control mapping becomes authoritative.

## D-005 - AI is assistive, not accountable

**Status:** Accepted

AI may draft, consolidate, explain and challenge. It may not approve scenarios, control mappings, regulatory mappings, residual risk or risk acceptance.

## D-006 - Project-native canonical RiskScenario model

**Status:** Accepted

The project will define its own canonical risk-scenario object rather than force risk scenarios into an OSCAL model that was not designed specifically for them.

## D-007 - OSCAL as interoperability layer

**Status:** Accepted

OSCAL is used downstream for control catalogs, profiles, mappings and later assessment/remediation artefacts. OSCAL does not replace project risk methodology.

## D-008 - Independent control library

**Status:** Accepted

A new control library will be independently authored using public defensive/security knowledge as source material. Proprietary/employer-specific control statements will not be reused.

## D-009 - Regulations are first-class requirement objects

**Status:** Accepted

DORA, NIS2, ADAE and later regulatory sources will be represented separately from project controls. Regulation-to-control mapping will be explicit and reviewable; regulatory text will not be treated as identical to a control statement.

## D-010 - Start file-based and version-controlled

**Status:** Accepted

Initial source of truth will use YAML/JSON/Markdown + Git. A graph database or relational store will be introduced only when query/scale needs are demonstrated.

## D-011 - Use local source snapshots

**Status:** Accepted

External authoritative data sources are synchronized into versioned local snapshots. Runtime methodology execution should not depend on external API availability.

## D-012 - First implementation is a vertical slice

**Status:** Accepted

The first PoC will prove:

ATT&CK -> candidate scenario -> human approval -> approved controls -> OSCAL Profile -> validation.

UI, large-scale regulation ingestion and large control catalogs are deferred.

## D-013 - Detect and integrate ATT&CK changes through a controlled delta workflow

**Status:** Accepted

The project will monitor the official MITRE `attack-stix-data` STIX 2.1 releases without allowing upstream changes to rewrite project methodology silently.

Change detection will run:

- weekly when automation is available;
- on demand during active research;
- mandatorily before approving a scenario or publishing a project release.

Each check compares the latest official versioned bundle with the most recent locally pinned snapshot. The full upstream bundle SHA-256 and a compact local snapshot are retained; an older snapshot is never overwritten.

The delta classifier must distinguish:

| Upstream event | Project response |
|---|---|
| New technique or sub-technique | Create a new scenario-research candidate; never auto-approve it. |
| Modified technique metadata, platforms, tactics, relationships, or procedure evidence | Identify every dependent scenario and mark it `review_required` when the change may affect meaning or applicability. |
| Revoked or deprecated object | Preserve historical references, flag dependent scenarios, and require an explicit replace/retain/retire decision. |
| New relationship, campaign, group, software, or Attack Flow evidence using known techniques | Evaluate whether it creates a novel attack path or scenario combination; create a candidate if it does. |
| Non-semantic source change | Record the sync and hashes without forcing methodology changes. |

Every sync produces a machine-readable delta plus a human-readable change report. The report includes added, modified, revoked, and deprecated objects; affected scenario IDs; changed fields; old/new source versions and hashes; and the recommended review action.

Integration follows this gate:

```text
official MITRE release/tag
        |
        v
version + hash comparison
        |
        v
immutable local snapshot
        |
        v
semantic STIX delta
        |
        +---- no relevant change ----> record only
        |
        +---- affected scenario -----> review_required
        |
        +---- novel attack vector ----> new candidate
                                      |
                                      v
                                human decision
```

Approved scenarios are immutable historical versions. An accepted upstream change produces a new scenario version rather than modifying the previously approved artifact in place. Candidate generation may be automated; approval, replacement, retirement, and risk-methodology interpretation remain human decisions.

Initial notification output is a local Markdown/JSON report. A later GitHub Actions monitor may open or update a single tracking issue when a new ATT&CK release is detected, but it must not commit generated methodology changes or merge anything automatically.

## D-014 - Approve the first authoritative risk scenario

**Status:** Accepted

On 2026-08-19, the project owner explicitly approved candidate `RS-CANDIDATE-0001` after review of its ATT&CK 19.1 provenance, platform, tactic and sub-technique mappings, CIA impact weighting, and package and repository integrity controls.

The approved artifact is promoted as `RS-IAM-001` version `1.0.0` under `scenarios/approved/RS-IAM-001/`. Its embedded review decision records the human reviewer role, decision date, and rationale. The previously committed candidate remains recoverable through Git history; the approved package is the authoritative methodology version from this decision onward.

## D-015 - Use structured decision-log entries going forward

**Status:** Accepted

Future material decisions should use the structured entry format in this file when the decision affects methodology, architecture, licensing, public release boundaries, clean-room discipline, security posture, or project scope.

Rationale: this project is intended to be auditable as a research and engineering workspace. Decisions should show not only what was selected, but why it was selected, what alternatives were considered, what trade-offs were accepted, and when the decision should be revisited.

Existing decisions remain valid and do not need to be rewritten immediately. They may be expanded into the structured format when they are revisited.

## Open Decisions

- project name;
- final risk-scenario grammar;
- initial system/context profiling schema;
- initial scenario-family taxonomy;
- initial public control-reference sources;
- exact OSCAL tooling choice;
- first DORA regulatory slice;
- eventual database/knowledge-graph architecture;
- contribution strategy toward OSCAL/MITRE communities.

## Structured entry template

Use this format for decisions that materially affect project scope, architecture, methodology, licensing, public release boundaries, data handling, or security posture.

### D-XXXX - Decision title

**Date:** YYYY-MM-DD  
**Status:** Proposed / Accepted / Accepted as design direction / Superseded / Rejected / Deprecated  
**Owner:** Name or role  
**Related files:** `README.md`, `docs/example.md`, `schemas/example.schema.json`

#### Context

What problem, uncertainty, constraint, or opportunity led to this decision?

Include only relevant background. Avoid private, employer-specific, customer-specific, or confidential details.

#### Decision

What was decided?

State the decision directly and clearly.

#### Rationale

Why was this option selected?

Explain the reasoning, assumptions, and intended benefits.

#### Alternatives considered

- **Option A:** Brief description and why it was not selected.
- **Option B:** Brief description and why it was not selected.
- **Option C:** Brief description and why it was not selected.

#### Trade-offs

What are the accepted costs, limitations, or risks?

Examples:

- simpler now, but less flexible later;
- more structured, but higher initial documentation burden;
- more open, but requires stronger clean-room discipline;
- more automation, but requires human validation.

#### Impact

What changes because of this decision?

Consider:

- documentation;
- code;
- schemas;
- examples;
- tests;
- licensing;
- release model;
- future work.

#### Review trigger

When should this decision be revisited?

Examples:

- when the project becomes public;
- when the first schema is stable;
- when real users or reviewers appear;
- when a better standard or model is selected;
- before production use;
- before external publication.

## Lightweight entry template

Use this shorter format for smaller decisions that do not need a full explanation.

### D-XXXX - Decision title

**Date:** YYYY-MM-DD  
**Status:** Accepted  
**Decision:** Short statement of what was decided.  
**Reason:** Short reason.  
**Review trigger:** When to revisit.
