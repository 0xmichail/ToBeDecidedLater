"""Generate and verify detached integrity metadata for scenario packages."""

from __future__ import annotations

import argparse
import hashlib
import json
from enum import StrEnum
from pathlib import Path
from typing import Literal

from pydantic import Field, model_validator

from tbdl.io import load_scenario
from tbdl.models import (
    RiskScenario,
    SemanticVersion,
    Sha256,
    SourceSnapshot,
    StrictModel,
)


MANIFEST_NAME = "artifact-manifest.json"
MANIFEST_CHECKSUM_NAME = "artifact-manifest.sha256"
RELEASE_MANIFEST_PATH = Path("integrity/release-manifest.json")
RELEASE_CHECKSUM_PATH = Path("integrity/release-manifest.sha256")


class ArtifactRole(StrEnum):
    CANONICAL_SCENARIO = "canonical_scenario"
    HUMAN_REVIEW_VIEW = "human_review_view"
    JSON_SCHEMA = "json_schema"
    SOURCE_SNAPSHOT = "source_snapshot"
    PACKAGE_MANIFEST = "package_manifest"
    MANIFEST_CHECKSUM = "manifest_checksum"
    PROJECT_FILE = "project_file"


class ArtifactDigest(StrictModel):
    path: str = Field(min_length=1)
    role: ArtifactRole
    media_type: str = Field(min_length=3)
    bytes: int = Field(gt=0)
    sha256: Sha256


class ArtifactManifest(StrictModel):
    schema_version: SemanticVersion = "0.1.0"
    package_id: str = Field(min_length=3)
    package_version: SemanticVersion
    package_status: str = Field(min_length=3)
    generated_at: str = Field(min_length=10)
    generator: str = Field(min_length=2)
    generator_version: SemanticVersion
    hash_algorithm: Literal["sha256"] = "sha256"
    artifacts: list[ArtifactDigest] = Field(min_length=1)
    source_snapshots: list[SourceSnapshot] = Field(min_length=1)
    signature_status: Literal["unsigned"] = "unsigned"
    verification_note: str = Field(min_length=20)

    @model_validator(mode="after")
    def artifact_paths_are_unique(self) -> ArtifactManifest:
        paths = [item.path for item in self.artifacts]
        if len(paths) != len(set(paths)):
            raise ValueError("Manifest artifact paths must be unique")
        return self


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _artifact(
    path: Path,
    role: ArtifactRole,
    media_type: str,
    *,
    display_path: str | None = None,
) -> ArtifactDigest:
    return ArtifactDigest(
        path=display_path or path.name,
        role=role,
        media_type=media_type,
        bytes=path.stat().st_size,
        sha256=sha256_file(path),
    )


def build_manifest(package_dir: Path, scenario: RiskScenario) -> ArtifactManifest:
    return ArtifactManifest(
        package_id=scenario.scenario_id,
        package_version=scenario.version,
        package_status=scenario.status.value,
        generated_at=scenario.provenance.generated_at.isoformat(),
        generator=scenario.provenance.generator,
        generator_version=scenario.provenance.generator_version,
        artifacts=[
            _artifact(
                package_dir / "scenario.yaml",
                ArtifactRole.CANONICAL_SCENARIO,
                "application/yaml",
            ),
            _artifact(
                package_dir / "scenario.md",
                ArtifactRole.HUMAN_REVIEW_VIEW,
                "text/markdown",
            ),
        ],
        source_snapshots=scenario.provenance.source_snapshots,
        verification_note=(
            "SHA-256 detects byte-level changes. Authenticity requires a trusted "
            "manifest checksum or a future digital signature."
        ),
    )


def generate_manifest(package_dir: Path) -> tuple[Path, Path]:
    scenario = load_scenario(package_dir / "scenario.yaml")
    manifest = build_manifest(package_dir, scenario)
    manifest_path = package_dir / MANIFEST_NAME
    manifest_path.write_text(
        json.dumps(manifest.model_dump(mode="json"), indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    checksum_path = package_dir / MANIFEST_CHECKSUM_NAME
    checksum_path.write_text(
        f"{sha256_file(manifest_path)}  {MANIFEST_NAME}\n",
        encoding="ascii",
        newline="\n",
    )
    return manifest_path, checksum_path


def verify_manifest(package_dir: Path) -> list[str]:
    return _verify_manifest_at(
        base_dir=package_dir,
        manifest_path=package_dir / MANIFEST_NAME,
        checksum_path=package_dir / MANIFEST_CHECKSUM_NAME,
    )


def _verify_manifest_at(
    *, base_dir: Path, manifest_path: Path, checksum_path: Path
) -> list[str]:
    errors: list[str] = []
    manifest = ArtifactManifest.model_validate_json(
        manifest_path.read_text(encoding="utf-8")
    )

    expected_manifest_hash = checksum_path.read_text(encoding="ascii").split()[0]
    actual_manifest_hash = sha256_file(manifest_path)
    if actual_manifest_hash != expected_manifest_hash:
        errors.append("Manifest checksum mismatch")

    for artifact in manifest.artifacts:
        artifact_path = base_dir / artifact.path
        if not artifact_path.is_file():
            errors.append(f"Missing artifact: {artifact.path}")
            continue
        if artifact_path.stat().st_size != artifact.bytes:
            errors.append(f"Artifact size mismatch: {artifact.path}")
        if sha256_file(artifact_path) != artifact.sha256:
            errors.append(f"Artifact SHA-256 mismatch: {artifact.path}")
    return errors


def build_release_manifest(repository_root: Path) -> ArtifactManifest:
    scenario_dir = repository_root / "scenarios/approved/RS-IAM-001"
    scenario = load_scenario(scenario_dir / "scenario.yaml")
    excluded_parts = {
        ".git",
        ".venv",
        ".pytest_cache",
        ".pytest-tmp",
        "__pycache__",
    }
    excluded_paths = {
        RELEASE_MANIFEST_PATH.as_posix(),
        RELEASE_CHECKSUM_PATH.as_posix(),
        "AGENTS.md",
    }

    def classify(relative_path: str) -> tuple[ArtifactRole, str]:
        if relative_path.endswith(".schema.json"):
            return ArtifactRole.JSON_SCHEMA, "application/schema+json"
        if relative_path.startswith("data/source-snapshots/"):
            return ArtifactRole.SOURCE_SNAPSHOT, "application/json"
        if relative_path.endswith("/scenario.yaml"):
            return ArtifactRole.CANONICAL_SCENARIO, "application/yaml"
        if relative_path.endswith("/scenario.md"):
            return ArtifactRole.HUMAN_REVIEW_VIEW, "text/markdown"
        if relative_path.endswith("/artifact-manifest.json"):
            return ArtifactRole.PACKAGE_MANIFEST, "application/json"
        if relative_path.endswith("/artifact-manifest.sha256"):
            return ArtifactRole.MANIFEST_CHECKSUM, "text/plain"

        media_types = {
            ".json": "application/json",
            ".md": "text/markdown",
            ".py": "text/x-python",
            ".toml": "application/toml",
            ".yaml": "application/yaml",
            ".yml": "application/yaml",
        }
        return (
            ArtifactRole.PROJECT_FILE,
            media_types.get(Path(relative_path).suffix, "application/octet-stream"),
        )

    artifact_specs: list[tuple[str, ArtifactRole, str]] = []
    for artifact_path in sorted(repository_root.rglob("*")):
        if not artifact_path.is_file():
            continue
        relative_path = artifact_path.relative_to(repository_root).as_posix()
        if relative_path in excluded_paths:
            continue
        if relative_path.startswith("sources/") or relative_path.endswith(".pyc"):
            continue
        if any(part in excluded_parts or part.endswith(".egg-info") for part in artifact_path.parts):
            continue
        role, media_type = classify(relative_path)
        artifact_specs.append((relative_path, role, media_type))
    return ArtifactManifest(
        package_id="TBDL-RISK-LIBRARY",
        package_version="0.1.0",
        package_status=scenario.status.value,
        generated_at=scenario.provenance.generated_at.isoformat(),
        generator="release_manifest",
        generator_version="0.1.0",
        artifacts=[
            _artifact(
                repository_root / relative_path,
                role,
                media_type,
                display_path=relative_path,
            )
            for relative_path, role, media_type in artifact_specs
        ],
        source_snapshots=scenario.provenance.source_snapshots,
        verification_note=(
            "SHA-256 detects byte-level changes across distributable repository "
            "artifacts. Authenticity requires a trusted checksum or signature."
        ),
    )


def generate_release_manifest(repository_root: Path = Path(".")) -> tuple[Path, Path]:
    manifest = build_release_manifest(repository_root)
    manifest_path = repository_root / RELEASE_MANIFEST_PATH
    checksum_path = repository_root / RELEASE_CHECKSUM_PATH
    manifest_path.parent.mkdir(parents=True, exist_ok=True)
    manifest_path.write_text(
        json.dumps(manifest.model_dump(mode="json"), indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    checksum_path.write_text(
        f"{sha256_file(manifest_path)}  {manifest_path.name}\n",
        encoding="ascii",
        newline="\n",
    )
    return manifest_path, checksum_path


def verify_release_manifest(repository_root: Path = Path(".")) -> list[str]:
    return _verify_manifest_at(
        base_dir=repository_root,
        manifest_path=repository_root / RELEASE_MANIFEST_PATH,
        checksum_path=repository_root / RELEASE_CHECKSUM_PATH,
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "action", choices=("generate", "verify", "generate-release", "verify-release")
    )
    parser.add_argument("path", type=Path)
    args = parser.parse_args()

    if args.action == "generate":
        for path in generate_manifest(args.path):
            print(path)
        return

    if args.action == "generate-release":
        for path in generate_release_manifest(args.path):
            print(path)
        return

    if args.action == "verify-release":
        errors = verify_release_manifest(args.path)
        if errors:
            raise SystemExit("\n".join(errors))
        print(f"Release integrity verified: {args.path}")
        return

    errors = verify_manifest(args.path)
    if errors:
        raise SystemExit("\n".join(errors))
    print(f"Integrity verified: {args.path}")


if __name__ == "__main__":
    main()
