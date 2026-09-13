# Design Decisions

Approval terminology and current scoring limitations are defined in [Validation status](validation-status.md). Approval is internal to the project and does not constitute independent validation or certification.

Status: Draft / research working positions

This document records early design decisions and hypotheses for the project. Its purpose is to make assumptions, trade-offs, and boundaries visible while the research direction is being tested.

These decisions are not product commitments and do not assume that the project must evolve into a complete framework, methodology, or commercial tool. They may be revised, narrowed, or abandoned when later work provides better evidence.

## DD-001 — Keep `ToBeDecidedLater` as a working codename

The repository keeps the name `ToBeDecidedLater` as a deliberate working codename.

The project currently has a defined research question but no predetermined endpoint. The name reflects that exploratory status rather than a promise that a final product or framework name will eventually replace it.

**Trade-off:**

- A descriptive repository name could make the topic immediately clearer.
- The current name preserves a personal, exploratory tone and leaves room for the research direction itself to change.

**Current position:** keep the name while making the research scope and current limitations explicit in the README.

## DD-002 — Explore OSCAL as an interoperability layer, not as the risk methodology

OSCAL is being explored because it provides structured, machine-readable models for catalogs, profiles, mappings, assessment artifacts, and remediation-related outputs.

The project does not assume that cyber-risk reasoning should be forced into OSCAL or that using OSCAL validates the reasoning.

**Trade-off:**

- OSCAL may improve structured exchange, traceability, and interoperability.
- Adopting it too early or too rigidly may add complexity before the project has stable domain semantics.

**Current position:** test OSCAL downstream where it adds demonstrable value. Do not make it a prerequisite for the core research model.

## DD-003 — Treat MITRE ATT&CK and Attack Flow as threat-behaviour inputs, not risk scenarios

MITRE ATT&CK and Attack Flow describe adversary behaviour and attack sequences. They can inform risk-scenario reasoning, but they are not themselves business or operational risk scenarios.

A contextual risk scenario requires additional information such as scope, exposed assets or services, preconditions, consequences, assumptions, and uncertainty.

**Trade-off:**

- Starting from ATT&CK can strengthen threat traceability.
- Treating ATT&CK techniques as ready-made risk scenarios would create shallow or potentially misleading outputs.

**Current position:** use ATT&CK and, where useful, Attack Flow as research inputs. Their practical value in a repeatable assessment workflow still needs to be tested.

## DD-004 — Treat MITRE D3FEND as defensive knowledge, not a control library or effectiveness model

MITRE D3FEND may help explore relationships between adversary behaviour and defensive techniques.

The project should not treat D3FEND as a complete control framework, regulatory control set, assessment checklist, or evidence that a particular control is effective.

**Trade-off:**

- D3FEND may improve defensive reasoning and terminology.
- Translating defensive knowledge into assessable project controls requires additional, independently authored semantics and human review.

**Current position:** use D3FEND, if useful, as an input to research. Keep control definition, implementation evidence, effectiveness, and residual-risk reasoning separate.

## DD-005 — Keep human judgment in the approval path

The project may use deterministic rules, structured data, and AI-assisted development, but risk judgments and methodology decisions remain human-owned.

AI can help draft, compare, structure, challenge, and test ideas. It is not an authority or approval mechanism.

**Trade-off:**

- Automation may reduce repetitive work and make reasoning more consistent.
- Automated outputs can create false confidence when context, uncertainty, or missing evidence is hidden.

**Current position:** AI assists; human reviewers decide. Project approval remains distinct from independent validation, organizational approval, or risk acceptance.

## DD-006 — Prefer private-to-public release for working material

Development and research can happen privately first, with public releases containing only deliberately selected, reviewed, and cleaned artifacts.

This helps separate raw experimentation from material intended to represent the project publicly and reduces the chance of publishing sensitive, employer-specific, misleading, or immature content.

**Trade-off:**

- Fully public development can improve transparency.
- Private-first research gives stronger control over confidentiality, provenance, and wording before publication.

**Current position:** publish curated artifacts, not raw working material by default.

## DD-007 — Use a mixed-license model

The repository uses Apache License 2.0 for code, scripts, schemas, validation logic, and machine-readable artifacts.

Documentation, diagrams, methodology/research notes, explanatory text, and other narrative material use Creative Commons Attribution 4.0 International unless otherwise stated.

**Trade-off:**

- A single license would be simpler.
- Different content types have different reuse patterns, so a mixed model gives clearer expectations.

**Current position:** keep the mixed-license model and make license scope explicit in the README and notices.

## DD-008 — Treat negative findings as useful research results

The project should not expand merely to preserve an initial vision.

If experiments show that a proposed abstraction adds overhead without improving traceability, reviewability, consistency, or usefulness, narrowing or abandoning that abstraction is an acceptable outcome.

**Trade-off:**

- A fixed roadmap can make progress appear more predictable.
- An open research process is more likely to expose assumptions that do not survive practical testing.

**Current position:** evidence from small experiments should determine whether the scope expands, changes, or contracts.

## Review Notes

Revisit these working positions when there is new evidence, for example:

- additional synthetic scenarios assessed under explicit criteria;
- independent or second-practitioner review attempts;
- control and evidence experiments;
- OSCAL transformation examples;
- comparisons with a simpler manual baseline;
- public material intended for external reuse.

Revisions should record why a decision changed rather than presenting the latest position as if it had always been settled.
