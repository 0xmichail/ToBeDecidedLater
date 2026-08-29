# Project Vision

## Problem Statement

Cyber risk and compliance work is still frequently managed as documents: spreadsheets, questionnaires, PDFs, screenshots, manual mappings and periodic evidence collection. This creates duplicated work, weak traceability, inconsistent control selection, difficult versioning and limited automation.

A second problem is methodological variance: two analysts can evaluate similar systems differently because assumptions, threat relevance, scoring logic, control expectations, and professional judgments are often only partially explicit.

The project explores a different model:

> **Threat-informed, evidence-based, regulatory-aware cyber risk assessment supported by structured data, explicit methodology rules, deterministic code, and human review.**

The research question is whether the repeatable parts of cyber risk assessment can be made more consistent, reproducible, traceable, and explainable without removing the human judgment required for contextual risk decisions.

## Proposed Value Chain

```text
Authoritative threat knowledge
        |
        v
System / service context
        |
        v
Contextual risk scenarios
        |
        v
Inherent risk reasoning
        |
        v
Defensive outcomes / controls
        |
        v
Assessment + evidence
        |
        v
Findings + residual risk
        |
        v
Treatment / acceptance
```

Regulatory requirements and OSCAL representations are attached to this chain where they add traceability or interoperability; they do not define the underlying risk methodology.

## Core Building Blocks

### Threat Knowledge

Use MITRE ATT&CK as authoritative structured adversary-behaviour knowledge and Attack Flow to represent sequences of ATT&CK behaviours where appropriate.

### Risk Scenario Compiler

Create a project-specific abstraction layer that transforms technical threat behaviour plus system context into human-readable and machine-readable cyber risk scenarios.

### Executable Methodology Logic

Represent repeatable methodology decisions as explicit rules and structured objects where this can be done safely and transparently.

Deterministic code may calculate, validate, route, compare, and enforce consistency. It must not disguise subjective judgment as objective computation.

### Human Certification

Generated scenarios are candidates only. A human reviewer must approve, modify or reject each scenario before it becomes part of the authoritative methodology library.

Human judgment also remains required for contextual applicability, materiality, residual risk, treatment, acceptance, and methodology changes that cannot be reduced to defensible deterministic rules.

### Defensive Knowledge

Use MITRE D3FEND and other public defensive sources as inputs for candidate defensive outcomes. These do not automatically become project controls.

### Independent Control Library

Create an original control library with stable IDs, objectives, control statements, evidence expectations and mappings to risk scenarios and external requirements.

### Regulatory Knowledge

Represent regulatory obligations such as DORA, NIS2 and ADAE requirements as structured, versioned requirements with authoritative source provenance.

Regulatory requirements may constrain or extend the assessment, but they are not substitutes for risk reasoning.

### OSCAL

Use OSCAL primarily as the interoperability/data representation layer for control catalogs, profiles, mappings, implementation/assessment artefacts and POA&M/remediation data.

## Design Principle

OSCAL is not the project's risk methodology.

The project should maintain its own canonical domain model for concepts OSCAL does not natively model well, especially system context, risk-scenario generation, scenario relevance, risk-routing logic, and human review decisions. OSCAL is a downstream representation and interoperability standard.

The project is also not intended to create another general-purpose cybersecurity framework. Existing public standards and knowledge bases are inputs to a project-native risk assessment methodology.

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

## Evaluation Direction

The methodology should eventually be evaluated on evidence rather than positioning claims. Relevant measures include:

- consistency between reviewers assessing comparable contexts;
- reproducibility of deterministic outputs;
- scenario relevance and incorrect scenario activation;
- reviewer override and correction rates;
- completeness of source-to-decision traceability;
- consistency of control and residual-risk reasoning;
- assessment effort compared with a predominantly manual approach.

These measures are research and calibration targets, not current claims of validated performance.

## Long-Term Vision

A user should eventually be able to describe/profile a system and obtain an explainable chain:

```text
Why is this risk scenario relevant?
    -> system context + ATT&CK/Attack Flow + explicit methodology logic

Why is this risk level proposed?
    -> contextual inputs + approved risk reasoning rules + recorded judgments

Why is this control required?
    -> risk scenario + defensive requirement

Why does regulation matter?
    -> mapped regulatory requirement

What proves the control works?
    -> evidence / observation

What remains?
    -> finding / residual risk / treatment
```

Every material conclusion should be traceable to structured inputs, explicit rules, source provenance, and recorded human judgments.
