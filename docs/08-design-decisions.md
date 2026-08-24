# Design Decisions

Status: Draft

This document records early design decisions for the project. The goal is to make assumptions, trade-offs, and boundaries visible while the framework is still being shaped.

These decisions are not final product commitments. They are working positions that may change as the project becomes more concrete.

## DD-001 — Keep `ToBeDecidedLater` as a working codename

The repository keeps the name `ToBeDecidedLater` as a deliberate working codename.

This is not meant to signal that the project has no direction. The project problem is specific: exploring an open, threat-informed cyber assurance framework. The name simply leaves room for the final product or framework name to emerge later.

**Trade-off:**

- A descriptive name such as `open-cyber-assurance` would be clearer and more brandable.
- The current name keeps a human, exploratory tone and signals that this is still a research and engineering workspace.

**Current position:** keep the name for now, but make the project intent clear in the README.

## DD-002 — Use OSCAL as an interoperability layer, not as the whole methodology

OSCAL is being explored because it provides structured, machine-readable models for catalogs, profiles, mappings, assessment artifacts, and POA&M-style outputs.

The project does not assume that all cyber risk reasoning should be forced into OSCAL.

**Trade-off:**

- Using OSCAL may improve traceability, exchange, and auditability.
- Using OSCAL too early or too rigidly may make the framework harder to reason about while the methodology is still evolving.

**Current position:** use OSCAL as a downstream representation and interoperability layer where it adds structure, not as the starting point for all reasoning.

## DD-003 — Treat MITRE ATT&CK and Attack Flow as threat-behaviour inputs, not risk scenarios

MITRE ATT&CK and Attack Flow describe adversary behaviour and attack sequences. They are valuable inputs, but they are not the same thing as business or operational risk scenarios.

A risk scenario needs additional context, such as exposed assets, service criticality, data sensitivity, preconditions, consequences, defensive expectations, evidence, and human review.

**Trade-off:**

- Starting from ATT&CK improves threat relevance.
- Treating ATT&CK techniques as ready-made risk scenarios would create shallow or misleading outputs.

**Current position:** ATT&CK and Attack Flow feed the scenario-generation process; they do not replace risk scenario design.

## DD-004 — Use MITRE D3FEND as defensive knowledge, not as a complete control library

MITRE D3FEND can help connect adversary behaviour to defensive techniques and outcomes.

The project should not treat D3FEND as a full control framework, regulatory control set, or assessment checklist.

**Trade-off:**

- D3FEND can improve the defensive reasoning behind candidate controls.
- A usable assurance framework still needs independently authored control objectives, evidence expectations, and assessment logic.

**Current position:** D3FEND is an input for defensive reasoning, not the authoritative project control library.

## DD-005 — Keep human certification in the approval path

The project may use rules, structured data, and AI-assisted drafting, but scenario approval and methodology decisions remain human-owned.

AI can help draft, compare, structure, and test ideas. It should not be treated as an authority or approval mechanism.

**Trade-off:**

- Automation can reduce repetitive work and improve consistency.
- Fully automated risk or assurance outputs can create false confidence if they are not reviewed in context.

**Current position:** AI assists; human reviewers certify.

## DD-006 — Prefer private-to-public release for sensitive development work

Development can happen privately first, with public releases containing only reviewed, cleaned, and approved artifacts.

This supports clean-room discipline and reduces the chance of publishing unfinished, misleading, employer-specific, or sensitive material.

**Trade-off:**

- Public development improves transparency.
- Private-first development gives more control over quality, wording, and release boundaries.

**Current position:** publish cleaned public artifacts, not raw working material by default.

## DD-007 — Use a mixed-license model

The repository uses Apache License 2.0 for code, scripts, schemas, validation logic, and machine-readable artifacts.

Documentation, diagrams, methodology notes, research notes, explanatory text, and narrative framework content use Creative Commons Attribution 4.0 International.

**Trade-off:**

- A single license would be simpler.
- Different content types have different reuse patterns, so a mixed model gives clearer expectations.

**Current position:** keep the mixed-license model and make license scope explicit in the README.

## Review notes

These decisions should be revisited when the project introduces:

- a first complete scenario schema;
- a larger synthetic scenario set;
- OSCAL transformation examples;
- control objective examples;
- evidence expectation examples;
- public documentation intended for external reuse.
