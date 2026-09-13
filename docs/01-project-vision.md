# Project Vision

Status: exploratory research direction.

Approval terminology and current scoring limitations are defined in [Validation status](validation-status.md). Approval is internal to the project and does not constitute independent validation or certification.

## Research Problem

Cyber risk and compliance work is often represented across spreadsheets, questionnaires, documents, screenshots, manual mappings, and periodic evidence collection. This project is exploring whether some parts of that reasoning can be made more explicit, traceable, reproducible, and easier to review through structured data and code.

The working research idea is:

> **Explore threat-informed, evidence-aware cyber risk assessment using machine-readable structures while keeping judgment and approval human-owned.**

This is a hypothesis to investigate, not a claim that a complete methodology or product has been established.

## Research Questions

The project currently asks questions such as:

- Can system context and threat knowledge be combined into reusable but context-sensitive risk scenarios?
- Can the reasoning behind scenario applicability be made explicit enough for another reviewer to challenge or reproduce it?
- Can control rationale and evidence expectations be represented separately from control implementation and effectiveness?
- Can source provenance and versioning reduce ambiguity when external knowledge changes?
- Can OSCAL add useful interoperability without forcing the project domain model into concepts it does not naturally represent?
- Does the additional structure improve assessment quality or review efficiency enough to justify its maintenance cost?

A negative or mixed answer to any of these questions is a valid research outcome.

## Conceptual Value Chain Under Investigation

```text
Authoritative threat knowledge
        |
        v
System / service context
        |
        v
Candidate risk scenarios
        |
        v
Human review and applicability reasoning
        |
        v
Defensive outcomes / controls
        |
        v
Evidence expectations / observations
        |
        v
Findings / treatment

Possible downstream branches:
- regulatory traceability
- OSCAL interoperability
- residual-risk reasoning
```

This flow is conceptual. The public repository does not currently implement the complete chain.

## Current Building Blocks

### Threat Knowledge

MITRE ATT&CK is used as a versioned source of structured adversary-behaviour knowledge in the current prototype. Attack Flow is being considered where sequencing would add useful context.

### Risk Scenario Representation

The current code and schema provide a project-specific structured representation for risk scenarios and one experimental published example.

A generalized scenario-generation engine from arbitrary system context has not yet been demonstrated.

### Human Review and Project Approval

Generated or authored scenarios are candidates until reviewed. Project-owner approval means approval for inclusion in the experimental project library; it is not independent validation, certification, or organizational risk acceptance.

### Defensive Knowledge

MITRE D3FEND and other public defensive sources may be used as inputs when exploring defensive outcomes. They are not treated as a control library or as evidence of control effectiveness.

### Project Controls

The research direction includes independently authored control objects with stable identifiers, objectives, evidence expectations, and explicit scenario mappings. This work should be treated separately from claims about implementation effectiveness or residual-risk reduction.

### Regulatory Knowledge

DORA, NIS2, ADAE requirements, and other authoritative sources may be explored as structured, versioned obligations. Mapping a project object to a requirement would not by itself establish compliance.

### OSCAL

OSCAL is being explored primarily as a downstream interoperability and representation layer. It is not the project's risk methodology and is not evidence that a risk judgment is correct.

## Human/AI Boundary

AI may assist with:

- drafting and revising scenario wording;
- comparing structured objects;
- identifying candidate duplicates or inconsistencies;
- generating challenge questions;
- assisting with coding and tests;
- exploring regulatory normalization approaches;
- generating human-readable material from reviewed structured data.

AI must not autonomously:

- approve a risk scenario;
- determine final applicability;
- approve a control-to-risk relationship;
- approve a regulatory mapping;
- make final residual-risk decisions;
- close findings;
- accept risk on behalf of any person or organization.

## Possible Longer-Term Direction

One question worth testing is whether a user could eventually describe a system and obtain an explainable chain such as:

```text
Why might this risk scenario be relevant?
    -> system context + threat knowledge + explicit assumptions

Why might this control be relevant?
    -> risk scenario + defensive rationale

What evidence is expected?
    -> control objective + assessment criteria

What was actually observed?
    -> evidence / observation

What remains unresolved?
    -> finding / treatment / uncertainty
```

This is not a committed target state. The project may narrow to only those parts that prove useful, or may remain a small research prototype if the broader chain does not provide enough value.
