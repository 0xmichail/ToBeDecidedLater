# Exploratory Target Architecture

Status: proposed research architecture, not a description of a fully implemented system.

This document records a possible architecture for testing the project ideas. Components marked as future or proposed should not be read as currently available capabilities.

## Conceptual Architecture

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
│       VERSIONED KNOWLEDGE SNAPSHOTS       │
│                                           │
│ Threat techniques                         │
│ Defensive knowledge                       │
│ Regulatory sources                        │
│ Provenance / source versions              │
└────────────────────┬──────────────────────┘
                     │
                     v
┌───────────────────────────────────────────┐
│      SCENARIO REASONING / COMPILATION     │
│                                           │
│ System context                            │
│ Exposure                                  │
│ Asset/service type                        │
│ Data / criticality                        │
│ Threat relevance                          │
│ Attack behaviour                          │
│ Consequence reasoning                     │
└────────────────────┬──────────────────────┘
                     │
                     v
              Candidate Scenario
                     │
                     v
               HUMAN REVIEW
           approve / modify / reject
                     │
                     v
      Project-approved experimental object
                     │
          ┌──────────┼───────────┐
          v          v           v
     Defensive    Controls   Regulations
      knowledge   research    research
          │          │           │
          └──────────┼───────────┘
                     v
          Further human review
                     │
                     v
        Optional OSCAL representation
                     │
                     v
        Structural validation / export
```

The current public implementation covers only a subset of this flow.

## Architectural Separation

### Domain Layer

Possible project-native concepts include:

- RiskScenario
- SystemProfile
- ThreatContext
- ScenarioApplicability
- ControlObjective
- Control
- RegulatoryRequirement
- MappingDecision
- ReviewDecision
- EvidenceExpectation
- AssessmentObservation

Not all of these concepts are implemented today. They represent the domain vocabulary being explored.

### Integration Layer

Potential adapters may include:

- MITRE ATT&CK STIX/TAXII;
- Attack Flow;
- D3FEND data/ontology;
- EUR-Lex/ELI and other regulatory sources;
- OSCAL models and validators.

Only implemented integrations should be described elsewhere as current capabilities.

### OSCAL Layer

OSCAL is being considered as a downstream representation/interoperability layer for approved project objects where the semantics align.

Generating structurally valid OSCAL would demonstrate representation compatibility, not methodological validity or regulatory compliance.

## Source Synchronization Principle

A useful design goal is that assessment logic should not depend directly on the live availability of an external source.

Preferred pattern:

```text
Authoritative source
      |
      v
controlled retrieval
      |
      v
versioned local snapshot
      |
      v
normalization / validation
      |
      v
project objects
```

This can support reproducibility and provenance. The current prototype already demonstrates a limited versioned ATT&CK snapshot; broader synchronization remains future work.

## Proposed ATT&CK Change-Review Loop

A richer change-detection mechanism is a possible future experiment, not an implemented current capability.

Potential questions include whether the project should compare ATT&CK versions semantically rather than only by file hash, and whether it can identify when an upstream change may affect an existing scenario.

Possible change dimensions include:

- techniques and sub-techniques;
- `modified`, `revoked`, and `x_mitre_deprecated` state;
- platforms and tactics;
- parent/sub-technique relationships;
- relevant procedure examples or other referenced objects.

A future implementation might classify a source change as:

1. informational only;
2. review required for an existing project object;
3. a prompt for a new research candidate.

A project-wide semantic impact index, automated schedule, and approval-triggered change workflow do **not** currently exist in the public prototype.

## Initial Storage Strategy

Avoid introducing a complex database until there is evidence that the relationships and query patterns require one.

The current research favors simple artifacts first:

- YAML for project-authored structured objects;
- JSON for source snapshots and possible interoperability outputs;
- Markdown for human-readable rendering;
- Git for version history and review context.

A graph or relational database should be considered only if later experiments justify it.

## Security and Integrity Principles

Current or intended principles include:

- no secrets in the repository;
- record source versions and provenance;
- validate imported structured data;
- schema-validate project domain objects;
- treat external content as untrusted input;
- retain source hashes where useful;
- preserve approved historical artifacts rather than silently rewriting them;
- keep human approval explicit;
- distinguish structural validation from methodological validation;
- add deterministic transformation and mapping tests when those transformations exist.

These are engineering constraints and research safeguards, not claims of production-grade security assurance.
