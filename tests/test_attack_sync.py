import json
from datetime import date, datetime
from pathlib import Path

from tbdl.attack_sync import build_compact_snapshot
from tbdl.io import load_scenario
from tbdl.manifest import sha256_file


def test_compact_snapshot_preserves_hash_and_attack_metadata() -> None:
    bundle = {
        "type": "bundle",
        "objects": [
            {
                "type": "attack-pattern",
                "id": "attack-pattern--parent",
                "name": "Example Technique",
                "modified": "2026-01-01T00:00:00.000Z",
                "x_mitre_version": "1.0",
                "x_mitre_platforms": ["Windows"],
                "kill_chain_phases": [
                    {"kill_chain_name": "mitre-attack", "phase_name": "initial-access"}
                ],
                "external_references": [
                    {
                        "source_name": "mitre-attack",
                        "external_id": "T1000",
                        "url": "https://attack.mitre.org/techniques/T1000/",
                    }
                ],
            },
            {
                "type": "attack-pattern",
                "id": "attack-pattern--child",
                "name": "Example Sub-technique",
                "modified": "2026-01-01T00:00:00.000Z",
                "x_mitre_is_subtechnique": True,
                "external_references": [
                    {
                        "source_name": "mitre-attack",
                        "external_id": "T1000.001",
                        "url": "https://attack.mitre.org/techniques/T1000/001/",
                    }
                ],
            },
        ],
    }
    raw = json.dumps(bundle).encode()
    snapshot = build_compact_snapshot(
        raw,
        version="test",
        technique_ids=["T1000"],
        retrieved_on=date(2026, 8, 19),
        source_url="https://example.test/bundle.json",
    )

    assert snapshot["source"]["bundle_bytes"] == len(raw)
    assert len(snapshot["source"]["bundle_sha256"]) == 64
    assert snapshot["techniques"][0]["tactics"] == ["Initial Access"]
    assert snapshot["techniques"][0]["subtechniques"][0]["external_id"] == "T1000.001"


def test_approved_scenario_metadata_matches_the_pinned_compact_snapshot() -> None:
    snapshot = json.loads(
        Path(
            "data/source-snapshots/mitre-attack/enterprise/19.1/T1078-T1110.json"
        ).read_text(encoding="utf-8")
    )
    scenario = load_scenario(
        Path("scenarios/approved/RS-IAM-001/scenario.yaml")
    )

    source = scenario.provenance.source_snapshots[0]
    assert source.version == snapshot["source"]["version"]
    assert source.sha256 == snapshot["source"]["bundle_sha256"]
    assert source.bundle_bytes == snapshot["source"]["bundle_bytes"]
    assert source.local_reference is not None
    assert source.local_reference_sha256 == sha256_file(Path(source.local_reference))

    snapshot_techniques = {
        item["external_id"]: item for item in snapshot["techniques"]
    }
    for reference in scenario.attack_behaviour.techniques:
        upstream = snapshot_techniques[reference.external_id]
        assert reference.name == upstream["name"]
        assert reference.stix_id == upstream["stix_id"]
        assert reference.upstream_modified_at == datetime.fromisoformat(
            upstream["modified"].replace("Z", "+00:00")
        )
        assert [item.value for item in reference.upstream_platforms] == upstream[
            "platforms"
        ]
        assert reference.upstream_tactics == upstream["tactics"]
        assert [item.external_id for item in reference.upstream_subtechniques] == [
            item["external_id"] for item in upstream["subtechniques"]
        ]
