# Project Vision

## Problem Statement

Cyber risk and compliance work is still frequently managed as documents: spreadsheets, questionnaires, PDFs, screenshots, manual mappings and periodic evidence collection. This creates duplicated work, weak traceability, inconsistent control selection, difficult versioning and limited automation.

The project explores a different model:

> **Threat-informed, evidence-based, regulatory-aware cyber risk assessment represented through open machine-readable standards.**

## Proposed Value Chain

```text
Authoritative threat knowledge
        |
        v
Contextual risk scenarios
        |
        v
Risk reasoning
        |
        v
Defensive outcomes / controls
        |
        v
Regulatory traceability
        |
        v
OSCAL representation
        |
        v
Assessment + evidence
        |
        v
Findings + residual risk + treatment
```

## Core Building Blocks

### Threat Knowledge

Use MITRE ATT&CK as authoritative structured adversary-behaviour knowledge and Attack Flow to represent sequences of ATT&CK behaviours where appropriate.

### Risk Scenario Compiler

Create a project-specific abstraction layer that transforms technical threat behaviour plus system context into human-readable and machine-readable cyber risk scenarios.

### Human Certification

Generated scenarios are candidates only. A human reviewer must approve, modify or reject each scenario before it becomes part of the authoritative methodology library.

### Defensive Knowledge

Use MITRE D3FEND and other public defensive sources as inputs for candidate defensive outcomes. These do not automatically become project controls.

### Independent Control Library

Create an original control library with stable IDs, objectives, control statements, evidence expectations and mappings to risk scenarios and external requirements.

### Regulatory Knowledge

Represent regulatory obligations such as DORA, NIS2 and ADAE requirements as structured, versioned requirements with authoritative source provenance.

### OSCAL

Use OSCAL primarily as the interoperability/data representation layer for control catalogs, profiles, mappings, implementation/assessment artefacts and POA&M/remediation data.

## Design Principle

OSCAL is not the project's risk methodology.

The project should maintain its own canonical domain model for concepts OSCAL does not natively model well, especially risk-scenario generation and risk-routing logic. OSCAL is a downstream representation and interoperability standard.

## Human/AI Boundary

AI may:

- draft scenario wording;
- consolidate related techniques;
- explain relationships;
- identify candidate duplicates;
- generate challenge questions;
- assist with regulatory normalization;
- generate human-readable documentation from approved structured data.

AI must not autonomously:

- approve a risk scenario;
- determine final applicability;
- approve a control-to-risk relationship;
- approve a regulatory mapping;
- make final residual-risk decisions;
- close findings or accept risk.

## Long-Term Vision

A user should eventually be able to describe/profile a system and obtain an explainable chain:

```text
Why is this risk scenario relevant?
    -> system context + ATT&CK/Attack Flow

Why is this control required?
    -> risk scenario + defensive requirement

Why does regulation matter?
    -> mapped regulatory requirement

What proves the control works?
    -> evidence / observation

What remains?
    -> finding / residual risk / treatment
```

Every conclusion should be traceable to structured evidence and approved methodology objects.
