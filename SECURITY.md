# Security and trust

## Scope

This repository distributes documents and templates. It does not contain or require executable application code, package managers, runtime dependencies, credentials, network services, or installation scripts.

The published artefacts are:

- PDF for print and workshop use;
- DOCX for editing the full pack;
- XLSX for working directly in the authority matrix;
- ZIP containing the distributed toolkit files.

## Safe use

Before using editable files in a controlled, validated, regulated, or production environment:

1. Obtain the artefact from this repository or an explicitly pinned commit.
2. Verify its SHA-256 hash against `SHA256SUMS.txt` when provenance matters.
3. Review the document contents and adapt them to your own engineering, safety, quality, legal, cybersecurity, validation, and change-control requirements.
4. Do not treat this toolkit as an approval, certification, standard, risk assessment, or authority to make an operational change.

## Artifact integrity

The public download links in `README.md` are pinned to immutable commit `b277752fe39713c05b1ff0cb9a70e34424883488`.

`SHA256SUMS.txt` records the SHA-256 digest of each distributed artefact. A mismatch means the file should not be assumed to be the published artefact.

## What to report

Please report anything that could undermine trust in the repository or distributed files, including:

- an unexpected executable, macro, embedded payload, or external dependency;
- a published artefact whose hash does not match the recorded digest;
- a suspicious link or redirect;
- accidental disclosure of confidential, personal, customer, or company-specific information;
- content that materially misrepresents the toolkit's scope or safety boundaries.

For public, non-sensitive problems, open a GitHub issue. For genuinely sensitive security reports, use GitHub's private vulnerability reporting feature if it is enabled for this repository rather than posting exploit details publicly.

## Supported versions

The pinned artefacts linked from the README are the current published distribution until a newer version is explicitly published and documented.

## Security claims

No claim is made that these templates make a system secure, safe, compliant, validated, or correct. Their purpose is narrower: to help make operational meaning, authority, evidence, and exceptions explicit enough to examine and govern.
