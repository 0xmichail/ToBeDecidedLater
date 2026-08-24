# Technical Environment

## Initial Goal

The first proof of concept should be intentionally small and should not require paid infrastructure or a complex platform stack.

## Recommended Local Environment

For Windows development:

```text
Windows 11
   |
   +-- WSL2
        +-- Ubuntu
             |
             +-- Git
             +-- Python 3.11+
             +-- uv
             +-- Docker
             +-- VS Code
```

## Recommended Tools

- Visual Studio Code
- WSL2 + Ubuntu
- Git
- GitHub
- Python 3.11+
- `uv` for Python dependency/environment management
- Docker Desktop with WSL2 backend

Suggested VS Code extensions:

- WSL
- Python
- Pylance
- Docker
- YAML
- GitHub Pull Requests

## Initial Python Stack

Candidate libraries:

| Library | Purpose |
| --- | --- |
| `mitreattack-python` | ATT&CK processing |
| `stix2` | STIX objects |
| `taxii2-client` | TAXII access |
| `pydantic` | canonical project models |
| `PyYAML` | YAML methodology files |
| `jsonschema` | schema validation |
| `httpx` | external API clients |
| `rdflib` | D3FEND RDF/JSON-LD work |
| `typer` | command-line interface |
| `rich` | readable CLI output/review UX |
| `pytest` | tests |

Exact dependencies must be validated before implementation.

## What Not to Add Initially

Do not introduce the following until a real requirement exists:

- Kubernetes;
- cloud deployment;
- Redis;
- Elasticsearch;
- Neo4j;
- large web framework;
- complex event bus;
- multiple databases.

Start with files + Git + schemas.

## Proposed Repository Structure

```text
ToBeDecidedLater/
|
├── README.md
├── pyproject.toml
├── docs/
├── schemas/
│   └── risk-scenario.schema.json
|
├── sources/
│   ├── mitre-attack/
│   ├── mitre-d3fend/
│   └── attack-flow/
|
├── scenarios/
│   ├── candidates/
│   ├── approved/
│   └── rejected/
|
├── controls/
│   ├── candidates/
│   └── approved/
|
├── regulations/
│   ├── dora/
│   ├── nis2/
│   └── adae/
|
├── oscal/
│   ├── catalogs/
│   ├── profiles/
│   └── mappings/
|
├── src/
│   ├── ingest/
│   ├── scenario/
│   ├── review/
│   └── oscal/
|
└── tests/
```

Directories should be created only as implementation begins; this is the target structure, not a requirement to create empty folders immediately.

## Source API / Data Cost Assumption

The initial design assumes use of public/open data interfaces for MITRE ATT&CK, Attack Flow, D3FEND and OSCAL tooling, with local snapshots to avoid runtime reliance on external services.

Commercial LLM APIs are optional and should not be required for the deterministic core.

## Source Snapshot Model

```text
External source
     |
     v
risk-engine sync
     |
     v
versioned raw snapshot
     |
     v
normalize
     |
     v
validate
     |
     v
local knowledge objects
```

## Candidate CLI

```text
risk-engine sync attack
risk-engine sync d3fend
risk-engine techniques
risk-engine scenario generate <technique-or-family>
risk-engine scenario review
risk-engine control map <scenario>
risk-engine oscal compile <scenario>
risk-engine oscal validate <scenario>
```

Names are placeholders.

## First Vertical Slice

The first implementation should prove only this:

```text
ATT&CK sync
    |
    v
T1078 / selected techniques
    |
    v
candidate scenario YAML
    |
    v
human approval
    |
    v
approved scenario YAML
    |
    v
small dummy/independent control set
    |
    v
OSCAL Profile
    |
    v
OSCAL validation
```

No UI, regulation ingestion or large control library is required to prove the architecture.
