# Initial Roadmap

## Guiding Principle

Prove the architecture with the smallest end-to-end vertical slice before expanding the regulatory corpus, control library or UI.

## Phase 0 - Governance and Clean Room

**Goal:** establish project boundaries and traceability.

Deliverables:

- clean-room/IP boundary;
- project vision;
- decision log;
- public-source provenance rules;
- new project naming later.

Indicative effort: **~1 week full-time equivalent**.

## Phase 1 - Canonical Domain Model

**Goal:** define project-native objects before coding external integrations.

Deliverables:

- `RiskScenario` model;
- review status/version model;
- provenance model;
- system-context/profiling minimum model;
- JSON Schema / Pydantic representation.

Indicative effort: **1-2 weeks**.

## Phase 2 - ATT&CK Ingestion

Deliverables:

- versioned ATT&CK source sync;
- STIX normalization;
- local query interface;
- provenance/version recording;
- basic CLI.

Indicative effort: **1-2 weeks**.

## Phase 3 - Attack Flow and D3FEND Integration

Deliverables:

- Attack Flow parser/integration;
- selected corpus test cases;
- D3FEND sync/query adapter;
- relationships retained as candidate knowledge.

Indicative effort: **1-2 weeks**.

## Phase 4 - Risk Scenario Compiler v0.1

Deliverables:

- technique/family clustering;
- context-aware candidate generation;
- candidate YAML;
- human-readable Markdown rendering;
- approve/modify/reject workflow;
- immutable approved versions;
- upstream-change review trigger.

Indicative effort: **3-4 weeks**.

## Phase 5 - Independent Control Library Seed

Goal is not completeness. Build enough original controls to prove scenario-to-control relationships.

Initial target: approximately **50-80 independently authored controls** across a small set of domains.

Deliverables:

- control/objective schema;
- evidence expectation fields;
- scenario relationships;
- D3FEND/public-source provenance;
- second human approval gate.

Indicative effort: **3-5 weeks**.

## Phase 6 - OSCAL PoC

Deliverables:

- control library -> OSCAL Catalog;
- approved scenario controls -> OSCAL Profile;
- project metadata using OSCAL extension mechanisms;
- schema validation;
- deterministic compiler tests.

Indicative effort: **2-3 weeks**.

## Phase 7 - DORA Regulatory Slice

Start with a bounded subset rather than the entire regulatory corpus.

Deliverables:

- regulatory requirement schema;
- authoritative source provenance;
- normalized requirements;
- human review workflow;
- selected control mappings;
- OSCAL representation/mapping.

Indicative effort: **2-3 weeks for a first useful slice**.

## Phase 8 - NIS2 and ADAE

Extend the same model after DORA proves stable.

Indicative effort:

- NIS2: **2-3 weeks initial slice**;
- ADAE: **2-3 weeks initial slice**, likely with more manual curation.

## Phase 9 - Assessment and Evidence Prototype

Deliverables:

- system profile;
- scenario activation;
- resolved OSCAL Profile;
- assessment scope;
- evidence/observation model;
- finding and residual-risk prototype;
- treatment / POA&M experiment.

Indicative effort: **3-4 weeks**.

## Phase 10 - Calibration and Synthetic Cases

Deliverables:

- 10-20 synthetic assessment cases;
- false-positive/false-negative analysis for scenario relevance;
- scenario duplication analysis;
- control-mapping review;
- regulatory mapping review;
- versioned methodology calibration notes.

Indicative effort: **3-4 weeks**.

## Overall Indicative Timeline

Assuming focused full-time-equivalent effort and some parallelization:

- **Architecture PoC:** ~6-8 weeks
- **Useful MVP:** ~3-4 months
- **Serious public beta:** ~6 months
- **Community/research-quality framework:** ~9-12 months

As a side project at roughly 10-15 hours/week, a realistic MVP horizon is closer to **6-9 months**.

These are planning estimates, not delivery commitments. They should be recalibrated after the first vertical slice.

## Initial Definition of Done

The architecture is proven when one synthetic system/context can execute the following chain:

```text
MITRE source data
      -> candidate scenario
      -> human-approved scenario
      -> approved controls
      -> OSCAL Catalog/Profile
      -> valid OSCAL artifact
```

Only after this works should scope expand materially.
