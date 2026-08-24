"""Load, validate, serialize, and render canonical scenario objects."""

from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml

from tbdl.models import RiskScenario


def load_scenario(path: Path) -> RiskScenario:
    payload: Any = yaml.safe_load(path.read_text(encoding="utf-8"))
    return RiskScenario.model_validate(payload)


def render_scenario_markdown(scenario: RiskScenario) -> str:
    lines = [
        f"# {scenario.scenario_id} — {scenario.title}",
        "",
        f"- Status: `{scenario.status.value}`",
        f"- Version: `{scenario.version}`",
        f"- Family: `{scenario.family}`",
        f"- Review: `{scenario.review.status.value}`",
        "",
        "## MITRE basis",
        "",
    ]

    for technique in scenario.attack_behaviour.techniques:
        lines.append(
            f"- [{technique.external_id} — {technique.name}]({technique.source_url}) "
            f"({technique.domain.value}, ATT&CK {technique.source_version})"
        )
        lines.append(
            "  - Upstream platforms: "
            + ", ".join(f"`{platform.value}`" for platform in technique.upstream_platforms)
        )
        lines.append(
            "  - Upstream tactics: "
            + ", ".join(f"`{tactic}`" for tactic in technique.upstream_tactics)
        )
        if technique.upstream_subtechniques:
            lines.append(
                "  - Sub-techniques: "
                + ", ".join(
                    f"[{item.external_id} — {item.name}]({item.source_url})"
                    for item in technique.upstream_subtechniques
                )
            )

    if scenario.attack_behaviour.tactics:
        lines.extend(["", "**Scenario tactics:** " + ", ".join(
            f"`{tactic}`" for tactic in scenario.attack_behaviour.tactics
        )])

    lines.extend(["", "## Target", ""])
    lines.append("**Asset types:** " + ", ".join(f"`{x}`" for x in scenario.target.asset_types))
    if scenario.target.service_types:
        lines.append(
            "**Service types:** "
            + ", ".join(f"`{x}`" for x in scenario.target.service_types)
        )
    lines.append(
        "**Platforms:** "
        + ", ".join(f"`{platform.value}`" for platform in scenario.target.platforms)
    )
    lines.append("**Technology context:** " + "; ".join(scenario.target.technology_context))

    lines.extend(["", "## Preconditions", ""])
    lines.extend(f"- {item}" for item in scenario.preconditions)
    lines.extend(["", "## Exposure conditions", ""])
    lines.extend(f"- {item}" for item in scenario.exposure_conditions)

    lines.extend(
        [
            "",
            "## Attack behaviour",
            "",
            scenario.attack_behaviour.narrative,
            "",
            "## Adverse event",
            "",
            scenario.adverse_event,
            "",
            "## CIA impact weighting",
            "",
            f"- Calibration: `{scenario.cia_impact.calibration}` "
            "(`0` none, `1` low, `2` moderate, `3` high)",
            f"- **Confidentiality: {scenario.cia_impact.confidentiality.weight}/3** — "
            f"{scenario.cia_impact.confidentiality.rationale}",
            f"- **Integrity: {scenario.cia_impact.integrity.weight}/3** — "
            f"{scenario.cia_impact.integrity.rationale}",
            f"- **Availability: {scenario.cia_impact.availability.weight}/3** — "
            f"{scenario.cia_impact.availability.rationale}",
            f"- **Total: {scenario.cia_impact.total_weight}/9**",
            "- **Dominant dimension(s):** "
            + (", ".join(scenario.cia_impact.dominant_dimensions) or "None"),
            f"- Context: {scenario.cia_impact.contextual_note}",
            "",
            "## Potential consequences",
            "",
        ]
    )
    for dimension, narrative in scenario.consequences.model_dump().items():
        if narrative:
            lines.append(f"- **{dimension.replace('_', ' ').title()}:** {narrative}")

    lines.extend(["", "## Candidate scenario statement", ""])
    lines.extend(f"> {line}" if line else ">" for line in scenario.scenario_statement.splitlines())

    lines.extend(
        [
            "",
            "## Provenance",
            "",
            f"- Generator: `{scenario.provenance.generator}` "
            f"`{scenario.provenance.generator_version}`",
            f"- Generated at: `{scenario.provenance.generated_at.isoformat()}`",
        ]
    )
    for source in scenario.provenance.source_snapshots:
        digest = f", SHA-256 `{source.sha256}`" if source.sha256 else ", hash pending sync"
        size = f", {source.bundle_bytes} bytes" if source.bundle_bytes else ""
        lines.append(
            f"- Source snapshot: {source.source} {source.version}, "
            f"retrieved `{source.retrieved_on.isoformat()}`{digest}{size}"
        )
        if source.local_reference:
            lines.append(
                f"  - Local compact snapshot: `{source.local_reference}`, "
                f"SHA-256 `{source.local_reference_sha256}`"
            )
    lines.append(f"- Transformation: {scenario.provenance.transformation_summary}")

    lines.extend(
        [
            "",
            "## Integrity metadata",
            "",
            "- Artifact hashes: `artifact-manifest.json`",
            "- Manifest checksum: `artifact-manifest.sha256`",
            "- Repository release manifest: `integrity/release-manifest.json`",
            "- Hash algorithm: `SHA-256`",
            "- Signature status: `unsigned`",
        ]
    )

    lines.extend(["", "## Human review gate", ""])
    if scenario.review.status.value == "pending":
        lines.extend(
            [
                "This is a candidate only. It is not part of the authoritative methodology library.",
                "",
                "Required decision: **approve, modify, reject, or challenge**.",
            ]
        )
    else:
        lines.extend(
            [
                f"- Reviewer: {scenario.review.reviewer}",
                f"- Decision date: `{scenario.review.decision_date}`",
                f"- Rationale: {scenario.review.rationale}",
            ]
        )

    return "\n".join(lines) + "\n"
