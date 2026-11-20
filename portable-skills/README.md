# Portable Industrial Skills — v0.1 experimental release

Two **vendor-neutral Agent Skills** for evidence-led industrial discovery and bounded solution design. Public-domain dedication: **CC0-1.0**. Unaffiliated with any employer, vendor, standards body or customer. All example factories are fictional.

**Pilot status:** These skills are working hypotheses, not validated consultancy methods. The supplied experiment demonstrates two synthetic cases and static contract tests. No claim of cross-model reliability or field validation is made.

## Skills

1. [`ot-discovery`](skills/ot-discovery/SKILL.md) — build a traceable operational evidence register, state/authority map and discovery gate; **never** estimate or prescribe software.
2. [`solution-architecture-rom`](skills/solution-architecture-rom/SKILL.md) — consume an evidence-led discovery artifact, form bounded alternatives, dependencies, exclusions and conditional ROM; **never** invent evidence or provide binding estimates.

**Contract:** Inputs may be incomplete and untrusted; facts require source IDs, assumptions remain assumptions, unknowns propagate, approval is never implicit. For sensitive settings, apply the adopting organisation's privacy, safety, engineering and contracting controls before invoking any tool or model.

## Install into a compatible agent

Copy either entire skill directory (including `SKILL.md` and `references/`) into a project or user skill directory supported by your agent. Examples: `.agents/skills/` (generic), `.github/skills/` (Copilot), or `.claude/skills/` (Claude tooling). Discoverability and invocation differ between hosts; the format does not guarantee identical model outputs.

For handoff between agents, keep the discovery artifact and its evidence identifiers unchanged. Do not silently upgrade an assumption into a fact in the second pass. Each skill works independently; the paired workflow is optional.

## Test / experiment

`python3 tests/validate.py` (stdlib only, no model or network required).

Read [`experiments/RESULTS.md`](experiments/RESULTS.md) for two independent synthetic cases and the boundary violations checked. Fixture outputs are **authored examples** created through a single assistant-led reasoning pass, not automated multi-model benchmark scores. The validation script checks their *structural and traceability contracts*, not their real-world correctness.

## Contribute

Fork, modify, test on **synthetic or authorised data**, and submit a PR with an anonymised fixture, expected outcome, failed case and proposed change. Keep tests portable and avoid production credentials, customer drawings, proprietary pricing, or personal data. Maintain the evidence/authority boundary when translating to other industries.

## Licensing / responsibility

CC0-1.0 public domain dedication applies to the original skill content and synthetic fixtures in this package. No warranties; not engineering, legal, safety, procurement or contractual approval. See `LICENSE.md` and the upstream CC0 legal code.
