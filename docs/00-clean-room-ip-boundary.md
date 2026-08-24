# Clean-Room and IP Boundary

## Purpose

This project must be developed as a genuinely independent framework using public/open sources, independently authored methodology, independently authored control language, and newly created code/data structures.

The goal is not to reproduce, extract, port, rename, or commercialize an employer-specific cyber risk assessment methodology or tool.

## Prohibited Source Material

The project must not copy or use as implementation source material:

- employer-specific control libraries;
- employer-specific questionnaires;
- internal assessment workbooks or macros;
- internal risk registries;
- internal service trackers;
- internal architecture or workflows;
- proprietary control mappings;
- internal findings, assessment results, examples, evidence, or datasets;
- internal wording or documentation;
- internal source code;
- confidential or non-public business logic.

## Permitted Foundation

The project may rely on:

- general professional knowledge and skills;
- independently developed methodology concepts;
- public laws and regulatory texts;
- MITRE ATT&CK;
- MITRE Attack Flow;
- MITRE D3FEND;
- NIST OSCAL;
- NIST publications and public frameworks;
- other public/open standards and properly licensed sources;
- synthetic examples created specifically for this project.

## Independent Creation Requirements

1. All project documentation is written from a blank page.
2. Every authoritative external dependency should have provenance.
3. Major methodology decisions should be recorded in `decision-log.md`.
4. Controls must be independently authored, even where public frameworks inform the objective or rationale.
5. Scoring thresholds and routing logic must be independently justified and calibrated.
6. Synthetic data must be used for demonstrations and tests.
7. Employer-specific names, identifiers, control codes, artifacts and terminology should not appear in public project content.

## Provenance Principle

Every important machine-readable object should eventually carry enough provenance to establish:

- source framework or regulation;
- source identifier;
- source version/date;
- retrieval date;
- transformation method;
- reviewer/approval state;
- project version that generated it.

## Legal Review

Before any commercialization or public release that could raise employment/IP concerns, the project owner should obtain independent legal advice covering employment terms, confidentiality, intellectual property assignment, outside-business restrictions and trade-secret obligations.

This file is a project governance boundary, not legal advice.
