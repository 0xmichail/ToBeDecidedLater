import json
import shutil
from pathlib import Path

from tbdl.manifest import (
    generate_manifest,
    verify_manifest,
    verify_release_manifest,
)


SOURCE_PACKAGE = Path("scenarios/approved/RS-IAM-001")


def _copy_package(tmp_path: Path) -> Path:
    package = tmp_path / "scenario-package"
    package.mkdir()
    shutil.copy2(SOURCE_PACKAGE / "scenario.yaml", package / "scenario.yaml")
    shutil.copy2(SOURCE_PACKAGE / "scenario.md", package / "scenario.md")
    return package


def test_manifest_verifies_an_unchanged_package(tmp_path: Path) -> None:
    package = _copy_package(tmp_path)
    manifest_path, checksum_path = generate_manifest(package)

    assert manifest_path.is_file()
    assert checksum_path.is_file()
    assert verify_manifest(package) == []


def test_manifest_detects_artifact_tampering(tmp_path: Path) -> None:
    package = _copy_package(tmp_path)
    generate_manifest(package)
    with (package / "scenario.md").open("a", encoding="utf-8") as handle:
        handle.write("\nunauthorized change\n")

    errors = verify_manifest(package)

    assert "Artifact size mismatch: scenario.md" in errors
    assert "Artifact SHA-256 mismatch: scenario.md" in errors


def test_committed_release_manifest_verifies_all_distributable_artifacts() -> None:
    assert verify_release_manifest(Path(".")) == []
    manifest = json.loads(
        Path("integrity/release-manifest.json").read_text(encoding="utf-8")
    )
    paths = {artifact["path"] for artifact in manifest["artifacts"]}
    assert {
        "docs/decision-log.md",
        "scenarios/approved/RS-IAM-001/scenario.yaml",
        "src/tbdl/models.py",
        "tests/test_manifest.py",
    } <= paths
