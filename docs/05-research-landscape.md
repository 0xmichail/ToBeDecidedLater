# Research landscape and open questions

## Status

These are initial research questions, not a completed literature review. Novelty, comparative advantage, and practical benefit have not been established. The references below identify primary project resources to investigate; they do not substantiate a claim that this project fills a previously unaddressed gap.

## Initial research hypothesis

The project explores whether a traceable transition from technical adversary behaviour and system context to risk scenarios, control rationale, and evidence expectations can improve assessment consistency or reduce review effort.

This is a hypothesis to evaluate through the [small assessment milestone](07-roadmap.md). Connecting existing standards alone is not evidence of a novel contribution.

## Primary resources and investigation questions

| Resource | Question to investigate |
| --- | --- |
| [MITRE ATT&CK](https://attack.mitre.org/) and [structured source data](https://github.com/mitre-attack/attack-stix-data) | Which source relationships support a contextual scenario, and which judgments require additional evidence? |
| [Attack Flow](https://github.com/center-for-threat-informed-defense/attack-flow) | When does explicit attack sequencing improve the selected scenarios? |
| [D3FEND](https://d3fend.mitre.org/) | How can defensive knowledge inform reviewable control objectives and evidence expectations? |
| [NIST OSCAL](https://pages.nist.gov/OSCAL/) | Which models and extensions can represent the selected outputs without defining the project's risk methodology? |

## Prior-art review still required

Investigate existing threat-to-control mappings, regulatory representations, threat-intelligence and attack-graph research, and assessment/evidence automation. Record specific publications or implementations, dates or versions, supported capabilities, and limitations before making comparative claims.

In particular, assess whether existing approaches already provide the proposed risk abstraction and what, if anything, the project adds. No claim of superiority over existing tools or frameworks is made here.

## Evaluation questions

- Can different reviewers explain and reproduce applicability and impact judgments using the same criteria?
- Does context materially change scenario selection and control rationale?
- Are evidence expectations useful to a practitioner?
- Does the workflow improve on a simple manual baseline, and at what review cost?
- Which artifacts could another practitioner reuse independently?

Human review, provenance, structured data, and integrity checks are design choices. Their presence alone does not demonstrate methodological validity or community value. See [Validation status](validation-status.md).
