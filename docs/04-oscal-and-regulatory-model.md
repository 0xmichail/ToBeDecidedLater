# OSCAL and Regulatory Model

## Role of OSCAL

OSCAL should be treated as the project's machine-readable interoperability layer, not as the project's risk methodology.

The project risk methodology should remain independent and compile approved information into OSCAL artefacts.

## Proposed Mapping

| Project Concept | OSCAL Model / Treatment |
| --- | --- |
| Independent control library | Catalog |
| Scenario-specific applicable controls | Profile |
| Framework/regulation relationships | Control Mapping |
| Shared platform/control implementation | Component Definition |
| Assessed system implementation | SSP |
| Assessment scope/methods | Assessment Plan |
| Evidence/observations/findings/risks | Assessment Results |
| Treatment/remediation | POA&M |
| Project-native risk scenario | External canonical object + OSCAL props/links/references |

## Regulations as Structured Requirements

Regulatory requirements should not be mixed directly into the control library.

Create separate catalogs/knowledge sets for regulatory obligations, for example:

```text
regulations/
├── dora/
├── nis2/
└── adae/
```

Each normalized regulatory requirement should have a stable project identifier and authoritative provenance.

Example conceptual object:

```yaml
id: REG-DORA-EXAMPLE-001
authority: European Union
instrument: DORA
article: "..."
paragraph: "..."
source_uri: "..."
effective_date: "..."
applicability:
  - financial_entity
obligation_type: ict_risk_management
normalized_requirement: "..."
review_status: candidate
```

## Regulation Is Not a Control

Avoid simplistic equivalence such as:

```text
DORA Article X = CTRL-001
```

Preferred relationship:

```text
Regulatory Requirement
        |
        v
Required Security Outcome
        |
        v
One or more Controls
```

Mappings may represent partial, intersecting, subset/superset or equivalent relationships where semantically justified.

## Control as a Junction Point

```text
MITRE ATT&CK
      |
      v
Risk Scenario
      |
      v
Control Objective
      |
      v
Project Control
   /     |      \
 DORA   NIS2   ADAE
```

This allows two-way queries:

- Why is this control needed?
- Which threats/scenarios does it address?
- Which regulations reference the outcome?
- Which controls support a regulatory requirement?
- Which evidence is available for those controls?
- Which gaps remain?

## Regulatory Ingestion Strategy

### DORA / NIS2

Prefer authoritative legal sources and stable identifiers where available. Preserve article/paragraph provenance and effective/version information.

### ADAE

Expect more curated/document-based ingestion and human verification where machine-readable authoritative sources are limited.

### Human Validation

Regulatory requirement extraction and mapping must be human-reviewed before becoming authoritative project content.

AI may propose normalized wording or mappings, but the original legal text/source must remain accessible and the normalized requirement must never replace the authoritative legal source.

## OSCAL Extensions

Project-specific metadata may be represented through namespaced OSCAL properties and links where appropriate, for example:

- risk scenario ID;
- ATT&CK technique ID;
- scenario family;
- project methodology version;
- regulatory source identifiers;
- human-review metadata.

The project should avoid modifying OSCAL schemas when ordinary extension mechanisms are sufficient.

## Example End State

For a real system:

```text
Baseline Control Profile
        +
Activated Scenario Profiles
        +
Applicable Regulatory Profiles
        +
System-specific conditions
        |
        v
Resolved System OSCAL Profile
        |
        v
Assessment Plan
        |
        v
Assessment Results
        |
        v
Residual Risk / POA&M
```
