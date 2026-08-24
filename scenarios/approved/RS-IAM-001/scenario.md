# RS-IAM-001 — Compromise of privileged credentials

- Status: `approved`
- Version: `1.0.0`
- Family: `credential_compromise`
- Review: `approved`

## MITRE basis

- [T1078 — Valid Accounts](https://attack.mitre.org/techniques/T1078/) (enterprise, ATT&CK 19.1)
  - Upstream platforms: `Containers`, `ESXi`, `IaaS`, `Identity Provider`, `Linux`, `macOS`, `Network Devices`, `Office Suite`, `SaaS`, `Windows`
  - Upstream tactics: `Stealth`, `Persistence`, `Privilege Escalation`, `Initial Access`
  - Sub-techniques: [T1078.001 — Default Accounts](https://attack.mitre.org/techniques/T1078/001/), [T1078.002 — Domain Accounts](https://attack.mitre.org/techniques/T1078/002/), [T1078.003 — Local Accounts](https://attack.mitre.org/techniques/T1078/003/), [T1078.004 — Cloud Accounts](https://attack.mitre.org/techniques/T1078/004/)
- [T1110 — Brute Force](https://attack.mitre.org/techniques/T1110/) (enterprise, ATT&CK 19.1)
  - Upstream platforms: `Containers`, `ESXi`, `IaaS`, `Identity Provider`, `Linux`, `macOS`, `Network Devices`, `Office Suite`, `SaaS`, `Windows`
  - Upstream tactics: `Credential Access`
  - Sub-techniques: [T1110.001 — Password Guessing](https://attack.mitre.org/techniques/T1110/001/), [T1110.002 — Password Cracking](https://attack.mitre.org/techniques/T1110/002/), [T1110.003 — Password Spraying](https://attack.mitre.org/techniques/T1110/003/), [T1110.004 — Credential Stuffing](https://attack.mitre.org/techniques/T1110/004/)

**Scenario tactics:** `Stealth`, `Persistence`, `Privilege Escalation`, `Initial Access`, `Credential Access`

## Target

**Asset types:** `application`, `identity_service`
**Service types:** `business_service`, `shared_service`
**Platforms:** `Containers`, `ESXi`, `IaaS`, `Identity Provider`, `Linux`, `Network Devices`, `Office Suite`, `SaaS`, `Windows`, `macOS`
**Technology context:** Identity and access management; Remote and privileged administration

## Preconditions

- Privileged or otherwise security-significant accounts exist for the assessed service.
- Legitimate credentials provide access to functions or data that could materially affect the assessed service.

## Exposure conditions

- Authentication interfaces are reachable by users, administrators, services, or external integrations.
- Credential strength, protection, monitoring, or lifecycle controls may be insufficient for the assessed context.

## Attack behaviour

A threat actor obtains or guesses legitimate credentials and uses the resulting valid account access to reach security-significant functions of the assessed service.

## Adverse event

Unauthorized privileged access is obtained and used to perform actions against the assessed service under the identity of a legitimate account.

## CIA impact weighting

- Calibration: `cia-0-3-v0.1` (`0` none, `1` low, `2` moderate, `3` high)
- **Confidentiality: 3/3** — Privileged account access can directly expose sensitive information across the services and resources available to the compromised identity.
- **Integrity: 3/3** — Privileged account access can directly enable unauthorized changes to data, configuration, permissions, and security-relevant transactions.
- **Availability: 2/3** — Privileged actions can materially disrupt services or administrative access, although disruption is not required for this scenario to succeed.
- **Total: 8/9**
- **Dominant dimension(s):** Confidentiality, Integrity
- Context: These are inherent scenario-level weights. An assessment must recalibrate them using the affected asset, information, business service, and operating context.

## Potential consequences

- **Confidentiality:** Sensitive information may be accessed or disclosed without authorization.
- **Integrity:** Data, configuration, access rights, or transactions may be modified without authorization.
- **Availability:** Privileged actions may disrupt the service or prevent legitimate administrative access.
- **Operational:** Investigation, containment, credential recovery, and service restoration may interrupt operations.
- **Customer:** Customer accounts, data, transactions, or service availability may be affected depending on scope.
- **Regulatory:** Reporting or other legal obligations may arise depending on the affected data, service, and jurisdiction.

## Candidate scenario statement

> A threat actor compromises or guesses legitimate privileged credentials and uses the resulting valid account access to perform unauthorized actions against the assessed service, potentially causing unauthorized disclosure, modification, or disruption of information and services.

## Provenance

- Generator: `scenario_compiler` `0.1.0`
- Generated at: `2026-08-19T00:00:00+00:00`
- Source snapshot: MITRE ATT&CK Enterprise STIX 2.1 19.1, retrieved `2026-08-19`, SHA-256 `bdf1ce86a4e604214c5076d37ae4dcb322678afc528df8492e6fdc1b554f5da3`, 53277393 bytes
  - Local compact snapshot: `data/source-snapshots/mitre-attack/enterprise/19.1/T1078-T1110.json`, SHA-256 `7ce3e038b061ca61f991c8ed3cb88e34f585750e8b03b4ef1fca7988e799630b`
- Transformation: Independently authored clean-room synthesis of two ATT&CK behaviours into a contextual scenario, verified against the official ATT&CK 19.1 STIX snapshot; no employer-specific methodology, control library, questionnaire, dataset, mapping, findings, evidence, wording, or confidential/internal content was used.

## Integrity metadata

- Artifact hashes: `artifact-manifest.json`
- Manifest checksum: `artifact-manifest.sha256`
- Repository release manifest: `integrity/release-manifest.json`
- Hash algorithm: `SHA-256`
- Signature status: `unsigned`

## Human review gate

- Reviewer: Project owner
- Decision date: `2026-08-19`
- Rationale: Approved for the authoritative methodology library after review of the ATT&CK 19.1 provenance, platform, tactic and sub-technique mappings, CIA impact weighting, and package and repository integrity controls.
