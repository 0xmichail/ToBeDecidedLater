# Technical Environment

## Current Goal

Keep the research prototype intentionally small, reproducible, and inexpensive to work on. The current implementation does not require cloud infrastructure, containers, a database, or paid services.

## Primary Local Environment

The project is currently developed primarily on native Windows using PowerShell and Python.

Current baseline:

```text
Windows
   |
   +-- PowerShell
   +-- Git
   +-- Python 3.13
   +-- project-local .venv
   +-- editable install from pyproject.toml
```

The repository should not require WSL, Docker, or a separate orchestration layer for the present prototype.

## Useful Tools

Typical development tools may include:

- Visual Studio Code or another editor;
- Git and GitHub;
- Python 3.13 for the current primary development environment;
- a repository-local virtual environment;
- `pytest` for tests.

WSL2, `uv`, Docker, or other tooling may be useful in some environments, but they are optional and should be introduced only when they solve a demonstrated requirement.

## Current Python Stack

The implemented project dependencies are defined by `pyproject.toml` and should be treated as the source of truth.

The current prototype is intentionally narrow. Additional libraries such as STIX/TAXII clients, OSCAL tooling, RDF libraries, richer CLI frameworks, or HTTP clients may be evaluated later if an experiment requires them.

A candidate dependency is not a current capability simply because it appears in a design note.

## What Not to Add Without a Demonstrated Need

Avoid introducing infrastructure only because it may be useful in a future architecture:

- Kubernetes;
- cloud deployment;
- Redis;
- Elasticsearch;
- Neo4j;
- a large web framework;
- a complex event bus;
- multiple databases;
- mandatory containers.

Start with files, Git, schemas, tests, and explicit transformations.

## Repository Structure

The actual repository tree is the source of truth for what exists today.

Possible future areas may include controls, regulatory representations, OSCAL outputs, additional source snapshots, or assessment artifacts, but empty directories should not be created merely to make the repository resemble a target architecture.

## External Source Model

The current approach favors versioned local snapshots and recorded provenance where external public data is used.

Conceptually:

```text
External authoritative source
     |
     v
controlled retrieval
     |
     v
versioned local snapshot
     |
     v
validation / normalization
     |
     v
project objects
```

The present public repository demonstrates only a limited ATT&CK snapshot workflow. Equivalent pipelines for D3FEND, Attack Flow, regulation sources, or OSCAL are future research possibilities rather than current capabilities.

## Optional AI Use

Commercial or hosted LLM APIs are not required for the deterministic project core.

AI may be used as a development and research assistant, but the public artifacts should remain understandable, reviewable, and testable without requiring an AI service to approve or interpret them.

## Candidate CLI Direction

Commands discussed in design notes, such as scenario generation, control mapping, or OSCAL compilation, should be treated as placeholders until they are actually implemented and tested.

Implemented command behavior should be documented from the code and tests, not inferred from a future command list.

## Near-Term Engineering Principle

The next useful engineering step should prove a small research question end to end rather than expand the technology stack.

For example:

```text
versioned threat input
    |
    v
structured scenario object
    |
    v
human review context
    |
    v
explicit control/evidence reasoning
    |
    v
reproducible validation
```

OSCAL export, broader regulatory ingestion, UI work, and larger knowledge stores should remain optional until smaller experiments demonstrate that they add value.
