from pathlib import Path

from tbdl.io import load_scenario, render_scenario_markdown


SCENARIO_DIR = Path("scenarios/approved/RS-IAM-001")


def test_rendered_markdown_matches_committed_review_view() -> None:
    scenario = load_scenario(SCENARIO_DIR / "scenario.yaml")
    rendered = render_scenario_markdown(scenario)

    assert rendered == (SCENARIO_DIR / "scenario.md").read_text(encoding="utf-8")
    assert "T1078 — Valid Accounts" in rendered
    assert "T1110 — Brute Force" in rendered
    assert "**Platforms:** `Containers`, `ESXi`, `IaaS`" in rendered
    assert "Upstream platforms: `Containers`, `ESXi`, `IaaS`" in rendered
    assert "Upstream tactics: `Stealth`, `Persistence`" in rendered
    assert "T1078.001 — Default Accounts" in rendered
    assert "T1110.004 — Credential Stuffing" in rendered
    assert "**Scenario tactics:** `Stealth`, `Persistence`" in rendered
    assert "## CIA impact weighting" in rendered
    assert "**Confidentiality: 3/3**" in rendered
    assert "**Integrity: 3/3**" in rendered
    assert "**Availability: 2/3**" in rendered
    assert "**Total: 8/9**" in rendered
    assert "**Dominant dimension(s):** Confidentiality, Integrity" in rendered
    assert "## Integrity metadata" in rendered
    assert "`artifact-manifest.json`" in rendered
    assert "`integrity/release-manifest.json`" in rendered
    assert "Signature status: `unsigned`" in rendered
    assert "- Status: `approved`" in rendered
    assert "- Review: `approved`" in rendered
    assert "- Reviewer: Project owner" in rendered
    assert "- Decision date: `2026-08-19`" in rendered
    assert "candidate only" not in rendered
