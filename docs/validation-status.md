# Validation status and scoring limitation

Notice date: 2026-09-06

## Affected example

This notice applies to [RS-IAM-001 version 1.0.0](../scenarios/approved/RS-IAM-001/scenario.md), including its YAML representation and outputs that reproduce its CIA ratings.

The example records confidentiality 3/3, integrity 3/3, availability 2/3, and a total of 8/9. These values do not yet have a documented, validated calibration basis. The label `cia-0-3-v0.1` identifies the existing scale; it is not evidence of validation. Neither the individual ratings nor their sum should be used to score or compare systems or to support operational risk decisions. The scenario's contextual recalibration note does not resolve this limitation.

## Meaning of approval

`approved` means the project owner approved inclusion in the experimental project library. It does not mean independent methodological validation, external certification, or demonstrated suitability for an operational assessment. Historical references to "human-certified" or "authoritative methodology" describe internal project approval only.

The approval recorded on 2026-08-19 remains part of the project history. This notice qualifies present use of that example without rewriting the historical decision or the approved package.

## Preservation and future review

The scenario YAML, Markdown, version, status, and package integrity files remain unchanged. Readers accessing those historical files directly should consult this notice. The repository release manifest is updated for the documentation changes; the scenario package manifest is preserved.

A replacement scoring approach requires explicit criteria, contextual evidence, documented uncertainty, boundary cases, and review before adoption. Any revision of the approved scenario must receive a new version and a recorded review decision. No replacement scale, thresholds, likelihood model, or residual-risk calculation is adopted by this notice.

## What existing checks establish

Schema validation checks structural constraints. Integrity checks detect byte-level changes against recorded digests. Source provenance records the basis of referenced material. These checks do not demonstrate that impact judgments are correct or that the methodology improves assessment outcomes.

See [D-016](decision-log.md#d-016---clarify-public-validation-and-approval-status) and the [next validation milestone](07-roadmap.md).
