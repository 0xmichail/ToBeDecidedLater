"""Canonical project-native RiskScenario model.

OSCAL is deliberately not used as the domain model. Approved project objects can
be compiled into OSCAL artefacts in a later integration layer.
"""

from __future__ import annotations

from datetime import date, datetime
from enum import StrEnum
from typing import Annotated, Literal

from pydantic import (
    AnyUrl,
    BaseModel,
    ConfigDict,
    Field,
    StringConstraints,
    field_validator,
    model_validator,
)

SemanticVersion = Annotated[
    str,
    StringConstraints(pattern=r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)$"),
]
ScenarioIdentifier = Annotated[
    str,
    StringConstraints(pattern=r"^RS-(?:CANDIDATE-\d{4}|[A-Z][A-Z0-9]*-\d{3})$"),
]
MitreTechniqueIdentifier = Annotated[
    str,
    StringConstraints(pattern=r"^T\d{4}(?:\.\d{3})?$"),
]
MitreSubTechniqueIdentifier = Annotated[
    str,
    StringConstraints(pattern=r"^T\d{4}\.\d{3}$"),
]
Sha256 = Annotated[str, StringConstraints(pattern=r"^[a-f0-9]{64}$")]
Slug = Annotated[str, StringConstraints(pattern=r"^[a-z][a-z0-9]*(?:_[a-z0-9]+)*$")]
CiaWeight = Annotated[int, Field(ge=0, le=3)]


class StrictModel(BaseModel):
    """Shared settings for deterministic, closed project objects."""

    model_config = ConfigDict(extra="forbid", frozen=True, str_strip_whitespace=True)


class ScenarioStatus(StrEnum):
    CANDIDATE = "candidate"
    IN_REVIEW = "in_review"
    APPROVED = "approved"
    REJECTED = "rejected"
    RETIRED = "retired"
    REVIEW_REQUIRED = "review_required"


class ReviewStatus(StrEnum):
    PENDING = "pending"
    APPROVED = "approved"
    CHANGES_REQUESTED = "changes_requested"
    REJECTED = "rejected"


class ActorType(StrEnum):
    EXTERNAL = "external"
    INTERNAL = "internal"
    THIRD_PARTY = "third_party"
    UNKNOWN = "unknown"


class MitreDomain(StrEnum):
    ENTERPRISE = "enterprise"
    ICS = "ics"
    MOBILE = "mobile"


class AttackPlatform(StrEnum):
    """Normalized Enterprise ATT&CK platform vocabulary used for asset matching."""

    CONTAINERS = "Containers"
    ESXI = "ESXi"
    IAAS = "IaaS"
    IDENTITY_PROVIDER = "Identity Provider"
    LINUX = "Linux"
    NETWORK_DEVICES = "Network Devices"
    OFFICE_SUITE = "Office Suite"
    SAAS = "SaaS"
    WINDOWS = "Windows"
    MACOS = "macOS"


class ThreatContext(StrictModel):
    actor_types: list[ActorType] = Field(min_length=1)
    intent_context: list[str] = Field(min_length=1)
    capability_context: str | None = None


class TargetContext(StrictModel):
    asset_types: list[Slug] = Field(min_length=1)
    service_types: list[Slug] = Field(default_factory=list)
    platforms: list[AttackPlatform] = Field(min_length=1)
    technology_context: list[str] = Field(min_length=1)

    @field_validator("platforms")
    @classmethod
    def platforms_are_unique(
        cls, platforms: list[AttackPlatform]
    ) -> list[AttackPlatform]:
        if len(platforms) != len(set(platforms)):
            raise ValueError("Target platforms must be unique")
        return platforms


class MitreSubTechniqueReference(StrictModel):
    external_id: MitreSubTechniqueIdentifier
    name: str = Field(min_length=2)
    source_url: AnyUrl
    stix_id: str | None = None
    upstream_modified_at: datetime | None = None


class MitreTechniqueReference(StrictModel):
    framework: Literal["MITRE ATT&CK"] = "MITRE ATT&CK"
    domain: MitreDomain
    external_id: MitreTechniqueIdentifier
    name: str = Field(min_length=2)
    source_version: str = Field(min_length=1)
    source_url: AnyUrl
    upstream_platforms: list[AttackPlatform] = Field(min_length=1)
    upstream_tactics: list[str] = Field(min_length=1)
    upstream_subtechniques: list[MitreSubTechniqueReference] = Field(
        default_factory=list
    )
    stix_id: str | None = None
    upstream_modified_at: datetime | None = None

    @field_validator("upstream_platforms")
    @classmethod
    def upstream_platforms_are_unique(
        cls, platforms: list[AttackPlatform]
    ) -> list[AttackPlatform]:
        if len(platforms) != len(set(platforms)):
            raise ValueError("Upstream ATT&CK platforms must be unique")
        return platforms

    @model_validator(mode="after")
    def upstream_relationships_are_consistent(self) -> MitreTechniqueReference:
        if len(self.upstream_tactics) != len(set(self.upstream_tactics)):
            raise ValueError("Upstream ATT&CK tactics must be unique")

        subtechnique_ids = [item.external_id for item in self.upstream_subtechniques]
        if len(subtechnique_ids) != len(set(subtechnique_ids)):
            raise ValueError("Upstream ATT&CK sub-techniques must be unique")

        if self.upstream_subtechniques:
            if "." in self.external_id:
                raise ValueError("A sub-technique cannot contain child sub-techniques")
            expected_prefix = f"{self.external_id}."
            if any(not item.startswith(expected_prefix) for item in subtechnique_ids):
                raise ValueError(
                    "Upstream sub-techniques must belong to their parent technique"
                )
        return self


class AttackBehaviour(StrictModel):
    techniques: list[MitreTechniqueReference] = Field(min_length=1)
    tactics: list[str] = Field(default_factory=list)
    attack_flow_reference: AnyUrl | None = None
    narrative: str = Field(min_length=20)

    @model_validator(mode="after")
    def technique_ids_are_unique(self) -> AttackBehaviour:
        technique_ids = [item.external_id for item in self.techniques]
        if len(technique_ids) != len(set(technique_ids)):
            raise ValueError("ATT&CK technique references must be unique")
        if len(self.tactics) != len(set(self.tactics)):
            raise ValueError("Scenario ATT&CK tactics must be unique")
        return self


class Consequences(StrictModel):
    confidentiality: str | None = None
    integrity: str | None = None
    availability: str | None = None
    operational: str | None = None
    customer: str | None = None
    regulatory: str | None = None

    @model_validator(mode="after")
    def at_least_one_consequence_is_present(self) -> Consequences:
        if not any(value for value in self.model_dump().values()):
            raise ValueError("At least one consequence narrative is required")
        return self


class CiaDimensionWeight(StrictModel):
    weight: CiaWeight
    rationale: str = Field(min_length=20)


class CiaImpactProfile(StrictModel):
    """Scenario-level inherent CIA weighting; asset assessments may override it."""

    calibration: Literal["cia-0-3-v0.1"] = "cia-0-3-v0.1"
    confidentiality: CiaDimensionWeight
    integrity: CiaDimensionWeight
    availability: CiaDimensionWeight
    contextual_note: str = Field(min_length=20)

    @property
    def total_weight(self) -> int:
        return sum(
            dimension.weight
            for dimension in (
                self.confidentiality,
                self.integrity,
                self.availability,
            )
        )

    @property
    def dominant_dimensions(self) -> list[str]:
        dimensions = {
            "Confidentiality": self.confidentiality.weight,
            "Integrity": self.integrity.weight,
            "Availability": self.availability.weight,
        }
        highest = max(dimensions.values())
        if highest == 0:
            return []
        return [name for name, weight in dimensions.items() if weight == highest]

    @model_validator(mode="after")
    def total_is_within_calibration(self) -> CiaImpactProfile:
        if not 0 <= self.total_weight <= 9:
            raise ValueError("CIA total weight must be between 0 and 9")
        return self


class SourceSnapshot(StrictModel):
    source: str = Field(min_length=2)
    version: str = Field(min_length=1)
    source_uri: AnyUrl
    retrieved_on: date
    sha256: Sha256 | None = None
    bundle_bytes: int | None = Field(default=None, gt=0)
    local_reference: str | None = None
    local_reference_sha256: Sha256 | None = None

    @model_validator(mode="after")
    def local_reference_has_digest(self) -> SourceSnapshot:
        if bool(self.local_reference) != bool(self.local_reference_sha256):
            raise ValueError(
                "Local source snapshot reference and SHA-256 must be provided together"
            )
        return self


class Provenance(StrictModel):
    generator: Slug
    generator_version: SemanticVersion
    generated_at: datetime
    source_snapshots: list[SourceSnapshot] = Field(min_length=1)
    transformation_summary: str = Field(min_length=20)


class ReviewDecision(StrictModel):
    status: ReviewStatus = ReviewStatus.PENDING
    reviewer: str | None = None
    decision_date: date | None = None
    rationale: str | None = None

    @model_validator(mode="after")
    def completed_decision_has_audit_fields(self) -> ReviewDecision:
        if self.status is ReviewStatus.PENDING:
            if any((self.reviewer, self.decision_date, self.rationale)):
                raise ValueError("Pending review cannot carry decision audit fields")
            return self

        if not self.reviewer or not self.decision_date or not self.rationale:
            raise ValueError(
                "A completed review requires reviewer, decision_date, and rationale"
            )
        return self


class RiskScenario(StrictModel):
    schema_version: SemanticVersion = "0.1.0"
    scenario_id: ScenarioIdentifier
    version: SemanticVersion
    status: ScenarioStatus
    family: Slug
    title: str = Field(min_length=5)
    threat: ThreatContext
    target: TargetContext
    preconditions: list[str] = Field(min_length=1)
    exposure_conditions: list[str] = Field(min_length=1)
    attack_behaviour: AttackBehaviour
    adverse_event: str = Field(min_length=20)
    consequences: Consequences
    cia_impact: CiaImpactProfile
    scenario_statement: str = Field(min_length=40)
    defensive_requirements: list[str] = Field(default_factory=list)
    control_references: list[str] = Field(default_factory=list)
    regulatory_references: list[str] = Field(default_factory=list)
    provenance: Provenance
    review: ReviewDecision

    @model_validator(mode="after")
    def lifecycle_is_consistent(self) -> RiskScenario:
        if self.status is ScenarioStatus.APPROVED:
            if self.review.status is not ReviewStatus.APPROVED:
                raise ValueError("Approved scenario requires an approved review decision")
            if self.scenario_id.startswith("RS-CANDIDATE-"):
                raise ValueError("Approved scenario requires a stable non-candidate ID")
            if self.version.startswith("0."):
                raise ValueError("Approved scenario version must be 1.0.0 or later")
            if self.cia_impact.total_weight == 0:
                raise ValueError("Approved scenario requires a non-zero CIA impact profile")

        if self.status is ScenarioStatus.REJECTED:
            if self.review.status is not ReviewStatus.REJECTED:
                raise ValueError("Rejected scenario requires a rejected review decision")

        if self.status in {ScenarioStatus.CANDIDATE, ScenarioStatus.IN_REVIEW}:
            if self.review.status is ReviewStatus.APPROVED:
                raise ValueError("Candidate or in-review scenario cannot carry approval")

        return self
