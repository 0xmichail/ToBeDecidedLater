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

The potential differentiation is therefore the **end-to-end composition and risk abstraction layer**, not the existence of any single source or standard.

## Research Hypothesis

The opportunity appears to be a framework that performs:

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
Risk reasoning
     |
     v
Defensive requirement
     |
     v
Independent controls
     |
     v
Regulatory mappings
     |
     v
OSCAL representation
     |
     v
Evidence / findings / treatment
```

The important middle layer is:

> **technical adversary behaviour -> contextual cyber risk scenario**

This should be treated as the core research/engineering hypothesis.

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
- evidence interoperability.

## Proposed Differentiation

1. Threat-informed but explicitly **risk-oriented** abstraction.
2. Human-certified scenario methodology.
3. Independent controls rather than copied proprietary catalogs.
4. Regulatory requirements as first-class structured objects.
5. OSCAL-native interoperability.
6. Evidence and treatment traceability.
7. Versioned source provenance.
8. Separation of deterministic logic, AI assistance and human accountability.

## Questions Still Open

- What formal risk-scenario grammar should be adopted?
- How much of scenario relevance can be deterministic?
- Should consequence taxonomies use CIA only or richer operational/customer/regulatory dimensions?
- What is the right relationship between Attack Flow and scenario families?
- What is the best initial public control source/reference set?
- How should regulatory requirement normalization be governed?
- At what point does a graph database provide enough value to justify operational complexity?
- Which contribution should eventually be proposed back to OSCAL/MITRE communities?
