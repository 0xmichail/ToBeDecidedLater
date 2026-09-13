# Risk Scenario Compiler — Research Design

Status: exploratory design. The public repository contains structured scenario models and one experimental scenario, but it does not currently implement a generalized scenario-generation engine.

Approval terminology and current scoring limitations are defined in [Validation status](validation-status.md). Approval is internal to the project and does not constitute independent validation or certification.

## Research Objective

Investigate whether structured threat knowledge plus explicit system context can support the creation of candidate cyber risk scenarios that are easier to review, challenge, version, and reproduce.

The term **compiler** is used here as a design metaphor for a deterministic transformation pipeline. It should not be read as a claim that a complete compiler currently exists.

Any generated output would remain a candidate for human review. The project does not treat generation as certification, validation, or risk approval.

## Conceptual Workflow

```text
MITRE ATT&CK / optional Attack Flow
        |
        v
Candidate threat behaviour
        |
        + system context
        + exposure
        + target type
        + data / criticality
        + explicit assumptions
        |
        v
Scenario reasoning / transformation
        |
        v
Candidate structured scenario
        |
        v
Human review
  approve / modify / reject
        |
        v
Project-approved experimental scenario
        |
        v
Possible later research:
controls / evidence / OSCAL representation
```

Only parts of this chain are implemented in the current public prototype.

## Why an Abstraction Layer May Be Useful

MITRE ATT&CK techniques describe adversary behaviours. They are not, by themselves, business or operational risk scenarios.

A useful risk scenario usually needs additional context about the target, relevant preconditions, exposure, consequences, uncertainty, and the scope of the assessment.

The research hypothesis is that multiple ATT&CK behaviours may sometimes be combined into a more meaningful scenario abstraction. For example:

```text
Brute Force
    +
Valid Accounts
        |
        v
Possible credential-compromise scenario family
```

Whether such grouping is useful, repeatable, and sufficiently context-sensitive still needs to be tested.

## Canonical Scenario Representation

The executable schema in [`../schemas/risk-scenario.schema.json`](../schemas/risk-scenario.schema.json) and the corresponding source model are the canonical description of the currently implemented scenario structure.

The published example is available at:

- [`../scenarios/approved/RS-IAM-001/scenario.yaml`](../scenarios/approved/RS-IAM-001/scenario.yaml)
- [`../scenarios/approved/RS-IAM-001/scenario.md`](../scenarios/approved/RS-IAM-001/scenario.md)

This document intentionally does not duplicate a simplified YAML structure, because illustrative examples can drift from the executable schema and create ambiguity about what the prototype actually supports.

## Human Review

A reviewer may need to assess, among other things:

- whether the scenario has meaningful cyber-risk semantics;
- whether the threat-source relationship is reasonable;
- whether the target and assessment scope are clear;
- whether preconditions and exposure assumptions are defensible;
- whether consequences are overstated or under-specified;
- what information is missing or uncertain;
- whether apparently similar scenarios should remain separate or be combined.

Project approval means only that the object has been accepted into the experimental project library under the recorded review context.

Upstream source changes should not silently rewrite an approved historical scenario. A later process may instead flag dependencies for review and produce a new project version when necessary.

## Defensive-Knowledge Research

After a scenario is reviewed, D3FEND or other public sources may be explored as inputs for candidate defensive outcomes.

Such relationships do not establish that a specific project control is appropriate, implemented, effective, or sufficient.

A possible future reasoning chain is:

```text
Reviewed Scenario
      |
Relevant adversary behaviour
      |
      v
Candidate defensive knowledge
      |
      v
Project control objective
      |
      v
Project control
      |
      v
Human-reviewed mapping
```

## OSCAL Research

A scenario remains a project-native object because OSCAL does not provide a standalone project-specific risk-scenario model.

A future experiment may represent reviewed controls or mappings in OSCAL where the semantics align. Structural OSCAL validity would demonstrate format conformance only; it would not establish that the underlying scenario, mapping, or risk judgment is methodologically valid.

## Candidate Scenario Areas for Future Exploration

Possible areas include:

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

These are research candidates only. They are not an approved taxonomy, complete risk library, or commitment to implement each area.
