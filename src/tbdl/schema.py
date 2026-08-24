"""Generate JSON Schema from the canonical Pydantic model."""

from __future__ import annotations

import json
from pathlib import Path

from tbdl.manifest import ArtifactManifest
from tbdl.models import RiskScenario


DEFAULT_OUTPUT = Path("schemas/risk-scenario.schema.json")
DEFAULT_MANIFEST_OUTPUT = Path("schemas/artifact-manifest.schema.json")


def generate_schema(output: Path = DEFAULT_OUTPUT) -> Path:
    schema = RiskScenario.model_json_schema(mode="validation")
    schema["$id"] = "urn:tbdl:schema:risk-scenario:0.1.0"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(schema, indent=2) + "\n", encoding="utf-8")
    return output


def generate_manifest_schema(output: Path = DEFAULT_MANIFEST_OUTPUT) -> Path:
    schema = ArtifactManifest.model_json_schema(mode="validation")
    schema["$id"] = "urn:tbdl:schema:artifact-manifest:0.1.0"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(schema, indent=2) + "\n", encoding="utf-8")
    return output


if __name__ == "__main__":
    print(generate_schema())
    print(generate_manifest_schema())
