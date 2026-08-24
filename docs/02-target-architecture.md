# Target Architecture

## High-Level Architecture

```text
┌───────────────────────────────────────────┐
│          AUTHORITATIVE SOURCES            │
│                                           │
│ MITRE ATT&CK   Attack Flow   D3FEND      │
│ DORA          NIS2          ADAE         │
└────────────────────┬──────────────────────┘
                     │
                     v
┌───────────────────────────────────────────┐
│          VERSIONED KNOWLEDGE STORE        │
│                                           │
│ Threat techniques                         │
│ Attack flows                              │
│ Defensive techniques                      │
│ Regulatory requirements                   │
│ Provenance / source versions              │
└────────────────────┬──────────────────────┘
                     │
                     v
┌───────────────────────────────────────────┐
│          RISK SCENARIO COMPILER           │
│                                           │
│ System context                            │
│ Exposure                                  │
│ Asset/service type                        │
│ Data                                      │
│ Criticality                               │
│ Threat relevance                          │
│ Attack behaviour                          │
│ Consequence abstraction                   │
└────────────────────┬──────────────────────┘
                     │
                     v
              Candidate Scenario
                     │
                     v
               HUMAN GATE #1
           approve / modify / reject
                     │
                     v
              Approved Scenario
                     │
          ┌──────────┼───────────┐
          v          v           v
       D3FEND     Controls   Regulations
          │          │           │
          └──────────┼───────────┘
                     v
               HUMAN GATE #2
          approve control mappings
                     │
                     v
┌───────────────────────────────────────────┐
│              OSCAL COMPILER               │
│                                           │
│ Catalog                                   │
│ Profile                                   │
│ Control Mapping                           │
│ Component Definition / SSP later          │
│ Assessment Plan / Results later           │
│ POA&M later                               │
└────────────────────┬──────────────────────┘
                     │
                     v
               OSCAL Validation
                     │
                     v
             Published Methodology
```

## Architectural Separation

### Domain Layer

Project-native concepts:

- RiskScenario
- SystemProfile
- ThreatContext
- ScenarioApplicability
- ControlObjective
- Control
- RegulatoryRequirement
- MappingDecision
- ReviewDecision

This layer remains independent of OSCAL.

### Integration Layer

Adapters for:

- MITRE ATT&CK STIX/TAXII;
- Attack Flow;
- D3FEND API/ontology;
- EUR-Lex/ELI and other regulatory sources;
- OSCAL models and validators.

### OSCAL Layer

Compiled artefacts generated from approved project objects.

## Source Synchronization Principle

Runtime assessment must not depend directly on the availability of external APIs.

Preferred pattern:

```text
Authoritative source
      |
      v
controlled sync
      |
      v
versioned local snapshot
      |
      v
normalization / validation
      |
      v
project knowledge store
```

This supports reproducibility, deterministic assessment and provenance.

### ATT&CK Change Detection and Integration Loop

The synchronization boundary also acts as an early-warning mechanism for
upstream ATT&CK changes. It checks the official collection index/release tags
weekly when automation is available, on demand during research, and before each
scenario approval or project release.

The comparison is semantic, not merely a file-hash comparison. It tracks STIX
IDs and external IDs across versions and evaluates changes to:

- techniques and sub-techniques;
- `modified`, `revoked`, and `x_mitre_deprecated` state;
- platforms and kill-chain phases/tactics;
- parent/sub-technique and other STIX relationships;
- campaigns, groups, software, procedure examples, and Attack Flow evidence.

A source change enters the project through one of three paths:

1. record-only, when no project-relevant semantics changed;
2. `review_required`, when an existing scenario dependency changed;
3. a new candidate, when the delta suggests a genuinely new attack vector or
   a novel combination of known techniques.

The project maintains an impact index from ATT&CK/STIX object IDs to scenario
IDs so each delta report can identify affected methodology artifacts. Approved
objects are never overwritten. Accepted changes produce new project versions
with new manifests, hashes, and review decisions.

## Initial Storage Strategy

Do not introduce a complex database prematurely.

Initial source of truth:

- YAML for project-authored methodology objects;
- JSON for source snapshots and OSCAL outputs;
- Markdown for human-readable rendering;
- Git for review/history/versioning.

A graph or relational database can be introduced after the relationships and query patterns are stable.

## Security-by-Design Principles

- no secrets in repository;
- pin and record source versions;
- validate all imported structured data;
- schema-validate project domain objects;
- treat external content as untrusted input;
- retain source hashes where useful;
- immutable approved versions;
- explicit human approval gates;
- no silent updates of approved scenarios after an upstream framework change;
- deterministic OSCAL compilation from approved data;
- tests for mappings and serialization.
