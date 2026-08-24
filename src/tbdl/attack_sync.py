"""Create a compact, hash-linked snapshot from an official ATT&CK STIX bundle."""

from __future__ import annotations

import argparse
import hashlib
import json
from datetime import date
from pathlib import Path
from typing import Any
from urllib.request import Request, urlopen


SOURCE_TEMPLATE = (
    "https://raw.githubusercontent.com/mitre-attack/attack-stix-data/"
    "v{version}/enterprise-attack/enterprise-attack-{version}.json"
)


def _external_id(item: dict[str, Any]) -> str | None:
    for reference in item.get("external_references", []):
        if reference.get("source_name") == "mitre-attack":
            return reference.get("external_id")
    return None


def _source_url(item: dict[str, Any]) -> str | None:
    for reference in item.get("external_references", []):
        if reference.get("source_name") == "mitre-attack":
            return reference.get("url")
    return None


def _display_tactic(phase_name: str) -> str:
    return phase_name.replace("-", " ").title()


def build_compact_snapshot(
    raw_bundle: bytes,
    *,
    version: str,
    technique_ids: list[str],
    retrieved_on: date,
    source_url: str,
) -> dict[str, Any]:
    bundle = json.loads(raw_bundle)
    patterns = [
        item
        for item in bundle.get("objects", [])
        if item.get("type") == "attack-pattern"
        and not item.get("revoked", False)
        and not item.get("x_mitre_deprecated", False)
    ]
    by_external_id = {
        external_id: item
        for item in patterns
        if (external_id := _external_id(item)) is not None
    }

    techniques: list[dict[str, Any]] = []
    for technique_id in technique_ids:
        if technique_id not in by_external_id:
            raise ValueError(f"Technique {technique_id} not found in ATT&CK {version}")
        item = by_external_id[technique_id]
        subtechniques = [
            child
            for external_id, child in by_external_id.items()
            if external_id.startswith(f"{technique_id}.")
            and child.get("x_mitre_is_subtechnique", False)
        ]
        subtechniques.sort(key=lambda child: _external_id(child) or "")

        techniques.append(
            {
                "external_id": technique_id,
                "name": item["name"],
                "stix_id": item["id"],
                "modified": item["modified"],
                "object_version": item.get("x_mitre_version"),
                "source_url": _source_url(item),
                "platforms": item.get("x_mitre_platforms", []),
                "tactics": [
                    _display_tactic(phase["phase_name"])
                    for phase in item.get("kill_chain_phases", [])
                    if phase.get("kill_chain_name") == "mitre-attack"
                ],
                "subtechniques": [
                    {
                        "external_id": _external_id(child),
                        "name": child["name"],
                        "stix_id": child["id"],
                        "modified": child["modified"],
                        "source_url": _source_url(child),
                    }
                    for child in subtechniques
                ],
            }
        )

    return {
        "schema_version": "0.1.0",
        "source": {
            "name": "MITRE ATT&CK Enterprise STIX 2.1",
            "version": version,
            "source_url": source_url,
            "retrieved_on": retrieved_on.isoformat(),
            "bundle_sha256": hashlib.sha256(raw_bundle).hexdigest(),
            "bundle_bytes": len(raw_bundle),
        },
        "techniques": techniques,
    }


def sync(version: str, technique_ids: list[str], output: Path) -> Path:
    source_url = SOURCE_TEMPLATE.format(version=version)
    request = Request(source_url, headers={"User-Agent": "ToBeDecidedLater/0.1"})
    with urlopen(request, timeout=120) as response:
        raw_bundle = response.read()
    snapshot = build_compact_snapshot(
        raw_bundle,
        version=version,
        technique_ids=technique_ids,
        retrieved_on=date.today(),
        source_url=source_url,
    )
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(
        json.dumps(snapshot, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    return output


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--version", required=True)
    parser.add_argument("--technique", action="append", required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    print(sync(args.version, args.technique, args.output))


if __name__ == "__main__":
    main()
