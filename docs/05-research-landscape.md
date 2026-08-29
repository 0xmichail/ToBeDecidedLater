# Research Landscape

## Status

These notes capture the research direction discussed during project inception. They are not a formal literature review and should be re-verified before publication or citation.

## Main Finding

The proposed idea is not composed of entirely novel individual building blocks. Several adjacent efforts already exist:

- OSCAL representation of security/control frameworks and assessment artefacts;
- FedRAMP automation based on OSCAL;
- European adoption/exploration of OSCAL, including German BSI work;
- community work representing European regulation in OSCAL;
- MITRE ATT&CK mappings to security control frameworks;
- MITRE Attack Flow for machine-readable attack sequences;
- D3FEND for defensive knowledge;
- financial-sector threat-informed mappings through MITRE CTID / CRI;
- academic work connecting attack graphs/threat intelligence with OSCAL.

The potential differentiation is therefore the **risk-assessment methodology, contextual risk abstraction, executable reasoning, and end-to-end traceability**, not the existence of any single source, mapping, or standard.

## Research Hypothesis

The research hypothesis is that a machine-assisted, threat-informed cyber risk assessment methodology and executable reasoning engine can reduce analyst variance and improve consistency, reproducibility, traceability, and explainability without removing necessary human judgment.

The intended reasoning chain is:

```text
System context
     |
     v
MITRE threat relevance
     |
     v
Attack behaviour / Attack Flow
     |
     v
Contextual risk scenario
     |
     v
Inherent risk reasoning
     |
     v
Defensive requirement
     |
     v
Independent controls + evidence expectations
     |
     v
Assessment / findings
     |
     v
Residual risk / treatment
```

Regulatory requirements constrain and extend the chain where applicable. OSCAL is used downstream for machine-readable interoperability and representation.

The important research layers are:

> **technical adversary behaviour -> contextual cyber risk scenario -> explicit risk reasoning -> evidence-supported residual risk**

These should be treated as the core methodology and engineering hypotheses.

## What Must Be Demonstrated

The project should not claim methodological superiority based on architecture alone. The hypothesis should eventually be tested using synthetic or otherwise permitted assessment cases.

Candidate evaluation dimensions include:

- inter-reviewer consistency for comparable system contexts;
- deterministic reproducibility of machine-executable decisions;
- relevant versus incorrectly activated risk scenarios;
- reviewer rejection, override, and correction rates;
- duplicate scenario generation;
- completeness of threat-to-scenario-to-control-to-evidence traceability;
- consistency of inherent and residual risk reasoning;
- time and effort compared with a predominantly manual assessment process.

No current performance claim is implied by listing these measures.

## Prior Art / Adjacent Areas to Track

### NIST OSCAL

Track:

- OSCAL Catalog;
- Profile;
- Control Mapping;
- Component Definition;
- SSP;
- Assessment Plan;
- Assessment Results;
- POA&M;
- extension mechanisms;
- OSCAL tooling and validation.

### FedRAMP

Important as a mature example of machine-readable security-assessment automation and validation using OSCAL artefacts.

### German BSI

Important evidence that OSCAL is moving beyond a US-federal-only use case and is relevant to European security-assurance ecosystems.

### MITRE ATT&CK

Authoritative public threat-behaviour knowledge. Use structured ATT&CK datasets rather than scraping human-facing pages.

### MITRE Attack Flow

Important because the project should not recreate an attack-sequencing language. Attack Flow can be an upstream representation of adversary sequences, while this project focuses on converting those sequences into risk abstractions.

### MITRE D3FEND

Candidate source for defensive techniques/countermeasure knowledge. It should inform defensive requirements but should not automatically generate authoritative project controls.

### MITRE CTID / Cyber Risk Institute

Important prior art because threat-informed mappings for the financial sector already exist. The project should not position itself merely as another ATT&CK-to-controls mapping exercise.

### Regulatory OSCAL Projects

Track community work representing DORA, EU AI Act and other regulation through OSCAL. Regulatory conversion alone should not be presented as the project's primary novelty.

### Academic Research

Track work around:

- attack graph-based risk assessment with OSCAL;
- threat-intelligence knowledge graphs;
- automated generation of OSCAL SSP/assessment results;
- compliance-as-code;
- evidence interoperability;
- analyst variance and inter-rater reliability in cyber risk assessment;
- explainable and reproducible risk-scoring methodologies.

## Proposed Differentiation

1. Threat-informed but explicitly **risk-oriented** abstraction.
2. Explicit, machine-executable methodology rules where defensible.
3. Human-certified scenario and judgment gates where automation is not defensible.
4. Independent controls rather than copied proprietary catalogs.
5. Regulatory requirements as first-class structured constraints and traceability objects.
6. OSCAL-native downstream interoperability.
7. Evidence and treatment traceability.
8. Versioned source provenance.
9. Separation of deterministic logic, AI assistance and human accountability.
10. Empirical evaluation of consistency and reviewer variance rather than assuming methodology quality.

## Questions Still Open

- What formal risk-scenario grammar should be adopted?
- Which assessment decisions can be made deterministic without creating false precision?
- How should inherent risk be calibrated and validated?
- How much of scenario relevance can be deterministic?
- Should consequence taxonomies use CIA only or richer operational/customer/regulatory dimensions?
- How should control effectiveness influence residual risk without hiding professional judgment inside arbitrary formulas?
- What is the right relationship between Attack Flow and scenario families?
- What is the best initial public control source/reference set?
- How should regulatory requirement normalization be governed?
- What experimental design can measure analyst variance and methodology consistency credibly?
- At what point does a graph database provide enough value to justify operational complexity?
- Which contribution should eventually be proposed back to OSCAL/MITRE communities?
