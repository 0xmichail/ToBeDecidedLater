# Risk Scenario Compiler

## Objective

Build a semi-automated engine that turns structured MITRE threat knowledge plus system context into candidate cyber risk scenarios.

The engine does **not** certify methodology. It proposes structured candidates for human review.

## Core Workflow

```text
MITRE ATT&CK / Attack Flow
        |
        v
Candidate threat behaviour
        |
        + system context
        + exposure
        + target type
        + data / criticality
        |
        v
Scenario Compiler
        |
        v
Candidate Scenario YAML
        |
        v
Human Review
  approve / modify / reject
        |
        v
Approved Scenario v1.0
        |
        v
D3FEND + Control Mapping
        |
        v
Second Human Approval
        |
        v
OSCAL compilation
```

## Why an Abstraction Layer is Needed

MITRE ATT&CK techniques are adversary behaviours, not business-oriented risk scenarios.

The project should not create one scenario per ATT&CK technique. Multiple techniques may contribute to one meaningful risk scenario.

Example abstraction:

```text
Brute Force
    +
Valid Accounts
    +
Account Manipulation
        |
        v
Credential / Account Compromise scenario family
```

## Proposed Scenario Model

```text
RiskScenario
├── id
├── version
├── title
├── status
├── family
│
├── threat
│   ├── actor_type
│   └── intent / capability context
│
├── target
│   ├── asset_types
│   ├── service_types
│   └── technology context
│
├── preconditions
├── exposure_conditions
│
├── attack_behaviour
│   ├── ATT&CK techniques
│   ├── tactics
│   └── optional Attack Flow reference
│
├── adverse_event
├── consequences
│   ├── confidentiality
│   ├── integrity
│   ├── availability
│   ├── operational
│   ├── customer
│   └── regulatory
│
├── defensive_requirements
├── control_references
├── regulatory_references
│
├── provenance
│   ├── ATT&CK version
│   ├── source object IDs
│   ├── source hashes / retrieval date
│   └── generator version
│
└── review
    ├── status
    ├── reviewer
    ├── decision_date
    └── rationale
```

## Candidate Scenario Example

```yaml
scenario_id: RS-IAM-001
version: 0.1
status: candidate
family: credential_compromise

title: Compromise of privileged credentials

target:
  asset_types:
    - application
    - identity_service

preconditions:
  - privileged_accounts_exist
  - administrative_access_is_available

attack_behaviour:
  mitre_attack:
    - id: T1078
      name: Valid Accounts
    - id: T1110
      name: Brute Force

adverse_event: >
  A threat actor obtains or abuses legitimate credentials to gain
  unauthorized access to the assessed service.

potential_consequences:
  confidentiality: true
  integrity: true
  availability: true

scenario_statement: >
  A threat actor compromises legitimate credentials and uses them to
  obtain unauthorized access to the assessed service, potentially
  enabling unauthorized disclosure, modification or disruption of
  information and services.

provenance:
  generator: scenario-compiler
  generator_version: 0.1

review:
  status: pending
  reviewer: null
  decision_date: null
  rationale: null
```

## Human Approval Gate #1

The reviewer certifies whether:

- the scenario has meaningful cyber-risk semantics;
- the ATT&CK relationship is reasonable;
- the target/scope is correct;
- preconditions are defensible;
- consequences are not overstated;
- duplicate scenarios should be merged;
- the scenario should enter the authoritative library.

Approved scenarios receive a stable ID and version.

Upstream ATT&CK changes must never silently rewrite an approved scenario. They should instead set a `review_required` state.

## D3FEND Enrichment

After scenario approval, D3FEND may be queried to identify candidate defensive techniques associated with the relevant ATT&CK behaviour.

D3FEND relationships are inputs, not automatic controls.

Flow:

```text
Approved Scenario
      |
ATT&CK Techniques
      |
      v
D3FEND candidate defensive techniques
      |
      v
Project Control Objectives
      |
      v
Project Controls
```

## Human Approval Gate #2

Control mappings require a second explicit review:

> Do these controls materially address this approved risk scenario?

Only approved relationships should be used to generate an authoritative OSCAL Profile.

## OSCAL Output Per Scenario

A scenario remains a project-native object because OSCAL does not define a standalone Risk Scenario model.

Suggested package:

```text
scenarios/RS-IAM-001/
├── scenario.yaml
├── scenario.md
├── provenance.json
├── attack-flow.json        # optional
└── oscal/
    ├── profile.json
    └── mapping.json
```

The OSCAL Profile represents the approved control set relevant to assessment of the scenario.

## Initial Scenario Families to Explore

- credential compromise;
- privileged account compromise;
- external application exploitation;
- API abuse;
- malware / ransomware;
- data exfiltration;
- data manipulation;
- service disruption / DDoS;
- lateral movement;
- security-control impairment;
- logging/detection evasion;
- supply-chain compromise;
- cloud-account compromise;
- administrative-interface compromise;
- recovery inhibition.

These are research candidates, not yet approved methodology families.
