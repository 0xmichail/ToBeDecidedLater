"""Render the first approved scenario into reviewable Markdown."""

from __future__ import annotations

from pathlib import Path

from tbdl.io import load_scenario, render_scenario_markdown


DEFAULT_INPUT = Path("scenarios/approved/RS-IAM-001/scenario.yaml")
DEFAULT_OUTPUT = Path("scenarios/approved/RS-IAM-001/scenario.md")


def render_file(source: Path = DEFAULT_INPUT, output: Path = DEFAULT_OUTPUT) -> Path:
    scenario = load_scenario(source)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(
        render_scenario_markdown(scenario), encoding="utf-8", newline="\n"
    )
    return output


if __name__ == "__main__":
    rendered = render_file()
    print(rendered)
