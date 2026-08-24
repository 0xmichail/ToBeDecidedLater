import json
from pathlib import Path

from tbdl.manifest import ArtifactManifest
from tbdl.models import RiskScenario


def test_generated_schema_matches_committed_schema() -> None:
    committed = json.loads(
        Path("schemas/risk-scenario.schema.json").read_text(encoding="utf-8")
    )
    generated = RiskScenario.model_json_schema(mode="validation")
    generated["$id"] = "urn:tbdl:schema:risk-scenario:0.1.0"

    assert committed == generated
    assert committed["additionalProperties"] is False


def test_generated_manifest_schema_matches_committed_schema() -> None:
    committed = json.loads(
        Path("schemas/artifact-manifest.schema.json").read_text(encoding="utf-8")
    )
    generated = ArtifactManifest.model_json_schema(mode="validation")
    generated["$id"] = "urn:tbdl:schema:artifact-manifest:0.1.0"

    assert committed == generated
    assert committed["additionalProperties"] is False
