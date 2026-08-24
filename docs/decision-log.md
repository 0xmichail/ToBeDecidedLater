# Decision Log

This log records major project architecture and methodology decisions. Decisions may be revised, but changes should be explicit and versioned.

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

The project will monitor the official MITRE `attack-stix-data` STIX 2.1 releases
without allowing upstream changes to rewrite project methodology silently.

Change detection will run:

- weekly when automation is available;
- on demand during active research;
- mandatorily before approving a scenario or publishing a project release.

Each check compares the latest official versioned bundle with the most recent
locally pinned snapshot. The full upstream bundle SHA-256 and a compact local
snapshot are retained; an older snapshot is never overwritten.

The delta classifier must distinguish:

| Upstream event | Project response |
|---|---|
| New technique or sub-technique | Create a new scenario-research candidate; never auto-approve it. |
| Modified technique metadata, platforms, tactics, relationships, or procedure evidence | Identify every dependent scenario and mark it `review_required` when the change may affect meaning or applicability. |
| Revoked or deprecated object | Preserve historical references, flag dependent scenarios, and require an explicit replace/retain/retire decision. |
| New relationship, campaign, group, software, or Attack Flow evidence using known techniques | Evaluate whether it creates a novel attack path or scenario combination; create a candidate if it does. |
| Non-semantic source change | Record the sync and hashes without forcing methodology changes. |

Every sync produces a machine-readable delta plus a human-readable change
report. The report includes added, modified, revoked, and deprecated objects;
affected scenario IDs; changed fields; old/new source versions and hashes; and
the recommended review action.

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

Approved scenarios are immutable historical versions. An accepted upstream
change produces a new scenario version rather than modifying the previously
approved artifact in place. Candidate generation may be automated; approval,
replacement, retirement, and risk-methodology interpretation remain human
decisions.

Initial notification output is a local Markdown/JSON report. A later GitHub
Actions monitor may open or update a single tracking issue when a new ATT&CK
release is detected, but it must not commit generated methodology changes or
merge anything automatically.

## D-014 - Approve the first authoritative risk scenario

**Status:** Accepted

On 2026-08-19, the project owner explicitly approved candidate
`RS-CANDIDATE-0001` after review of its ATT&CK 19.1 provenance, platform, tactic
and sub-technique mappings, CIA impact weighting, and package and repository
integrity controls.

The approved artifact is promoted as `RS-IAM-001` version `1.0.0` under
`scenarios/approved/RS-IAM-001/`. Its embedded review decision records the
human reviewer role, decision date, and rationale. The previously committed
candidate remains recoverable through Git history; the approved package is the
authoritative methodology version from this decision onward.

## Open Decisions

- project name;
- license/publication strategy;
- final risk-scenario grammar;
- initial system/context profiling schema;
- initial scenario-family taxonomy;
- initial public control-reference sources;
- exact OSCAL tooling choice;
- first DORA regulatory slice;
- eventual database/knowledge-graph architecture;
- contribution strategy toward OSCAL/MITRE communities.
