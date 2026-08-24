from datetime import date
from pathlib import Path

import pytest
from pydantic import ValidationError

from tbdl.io import load_scenario


SCENARIO = Path("scenarios/approved/RS-IAM-001/scenario.yaml")


def test_approved_scenario_loads_and_retains_source_provenance() -> None:
    scenario = load_scenario(SCENARIO)

    assert scenario.scenario_id == "RS-IAM-001"
    assert scenario.version == "1.0.0"
    assert scenario.status.value == "approved"
    assert [ref.external_id for ref in scenario.attack_behaviour.techniques] == [
        "T1078",
        "T1110",
    ]
    expected_platforms = [
        "Containers",
        "ESXi",
        "IaaS",
        "Identity Provider",
        "Linux",
        "Network Devices",
        "Office Suite",
        "SaaS",
        "Windows",
        "macOS",
    ]
    assert [platform.value for platform in scenario.target.platforms] == expected_platforms
    expected_upstream_platforms = [
        "Containers",
        "ESXi",
        "IaaS",
        "Identity Provider",
        "Linux",
        "macOS",
        "Network Devices",
        "Office Suite",
        "SaaS",
        "Windows",
    ]
    assert all(
        [platform.value for platform in ref.upstream_platforms]
        == expected_upstream_platforms
        for ref in scenario.attack_behaviour.techniques
    )
    assert scenario.attack_behaviour.techniques[0].upstream_tactics == [
        "Stealth",
        "Persistence",
        "Privilege Escalation",
        "Initial Access",
    ]
    assert [
        item.external_id
        for item in scenario.attack_behaviour.techniques[0].upstream_subtechniques
    ] == ["T1078.001", "T1078.002", "T1078.003", "T1078.004"]
    assert scenario.attack_behaviour.techniques[1].upstream_tactics == [
        "Credential Access"
    ]
    assert scenario.cia_impact.total_weight == 8
    assert scenario.cia_impact.dominant_dimensions == [
        "Confidentiality",
        "Integrity",
    ]
    assert scenario.provenance.source_snapshots[0].version == "19.1"
    assert scenario.provenance.source_snapshots[0].sha256 == (
        "bdf1ce86a4e604214c5076d37ae4dcb322678afc528df8492e6fdc1b554f5da3"
    )
    assert scenario.attack_behaviour.techniques[0].stix_id == (
        "attack-pattern--b17a1a56-e99c-403c-8948-561df0cffe81"
    )
    assert scenario.review.status.value == "approved"
    assert scenario.review.reviewer == "Project owner"
    assert scenario.review.decision_date == date(2026, 8, 19)


def test_approved_scenario_requires_stable_id_version_and_review() -> None:
    payload = load_scenario(SCENARIO).model_dump(mode="json")
    payload["review"] = {
        "status": "pending",
        "reviewer": None,
        "decision_date": None,
        "rationale": None,
    }

    with pytest.raises(ValidationError, match="approved review decision"):
        load_from_payload(payload)

    payload = load_scenario(SCENARIO).model_dump(mode="json")
    payload["scenario_id"] = "RS-CANDIDATE-0001"

    with pytest.raises(ValidationError, match="stable non-candidate ID"):
        load_from_payload(payload)

    payload = load_scenario(SCENARIO).model_dump(mode="json")
    payload["version"] = "0.1.0"

    with pytest.raises(ValidationError, match="1.0.0 or later"):
        load_from_payload(payload)


def test_completed_review_requires_audit_fields() -> None:
    payload = load_scenario(SCENARIO).model_dump(mode="json")
    payload["review"] = {
        "status": "rejected",
        "reviewer": "Michalis",
        "decision_date": date(2026, 8, 19).isoformat(),
        "rationale": None,
    }

    with pytest.raises(ValidationError, match="requires reviewer"):
        load_from_payload(payload)


def test_duplicate_technique_references_are_rejected() -> None:
    payload = load_scenario(SCENARIO).model_dump(mode="json")
    payload["attack_behaviour"]["techniques"].append(
        payload["attack_behaviour"]["techniques"][0]
    )

    with pytest.raises(ValidationError, match="must be unique"):
        load_from_payload(payload)


def test_platforms_use_unique_canonical_attack_values() -> None:
    payload = load_scenario(SCENARIO).model_dump(mode="json")
    payload["target"]["platforms"].append("macOS")

    with pytest.raises(ValidationError, match="Target platforms must be unique"):
        load_from_payload(payload)

    payload = load_scenario(SCENARIO).model_dump(mode="json")
    payload["target"]["platforms"][-1] = "macO"

    with pytest.raises(ValidationError, match="Input should be"):
        load_from_payload(payload)


def test_subtechniques_must_be_unique_and_belong_to_the_parent() -> None:
    payload = load_scenario(SCENARIO).model_dump(mode="json")
    payload["attack_behaviour"]["techniques"][0]["upstream_subtechniques"].append(
        payload["attack_behaviour"]["techniques"][0]["upstream_subtechniques"][0]
    )

    with pytest.raises(ValidationError, match="sub-techniques must be unique"):
        load_from_payload(payload)

    payload = load_scenario(SCENARIO).model_dump(mode="json")
    payload["attack_behaviour"]["techniques"][0]["upstream_subtechniques"][0] = {
        "external_id": "T1110.001",
        "name": "Password Guessing",
        "source_url": "https://attack.mitre.org/techniques/T1110/001/",
    }

    with pytest.raises(ValidationError, match="belong to their parent"):
        load_from_payload(payload)


def test_cia_weights_are_limited_to_zero_through_three() -> None:
    payload = load_scenario(SCENARIO).model_dump(mode="json")
    payload["cia_impact"]["availability"]["weight"] = 4

    with pytest.raises(ValidationError, match="less than or equal to 3"):
        load_from_payload(payload)


def test_approved_scenario_requires_non_zero_cia_profile() -> None:
    payload = load_scenario(SCENARIO).model_dump(mode="json")
    for dimension in ("confidentiality", "integrity", "availability"):
        payload["cia_impact"][dimension]["weight"] = 0

    with pytest.raises(ValidationError, match="non-zero CIA impact profile"):
        load_from_payload(payload)


def load_from_payload(payload: dict):
    from tbdl.models import RiskScenario

    return RiskScenario.model_validate(payload)
