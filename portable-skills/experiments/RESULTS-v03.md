# v0.3 evidence log — method upgrades and known limits

**Status:** Experimental. v0.2's three authored cases and its structural oracle remain in `fixtures-v02`, `outputs-v02`, `RESULTS-v02.md`. v0.1 remains in `v01-baseline/`. No independent blind model trials or real-plant acceptance claim is made.

## Why v0.3 exists

A private historical replay comparing skill-constrained and broader analysis revealed: (1) the v0.2 skill knew to mention shared crews and time but did not **trigger deterministic coupling analysis**, (2) ROM revisions could be naively compared across changed scope/supplier owners, (3) policy alternatives needed executable negative tests, and (4) product demos needed stronger proof-state distinctions. These are generalised without publishing the private historical case, data or derived timeline.

## Public independently fictional v0.3 examples

| Fixture | Trigger and check | Reference conclusion | Caveat |
| --- | --- | --- | --- |
| `temporal.json` | One mobile QA sampler across **three** fictional packaging cells | baseline 09:52; second cell +10 min readiness -> 10:02 and 10 resource-wait minutes; last-cell service norm +8 -> 10:00 | Exactly specified, simulated clocks, not measured performance |
| `lineage.json` | Two revisions with changed scope and two suppliers claiming APP-UAT | gross R1 21–33 and R2 27–44; R2 vendor/integrator UAT collision; `NET UNRESOLVED`, `NOT COMPARABLE` | Synthetic engineering-day arithmetic; no price or vendor quote |
| `policies.json` | Two competing offline app approval points and 6 required checks in one variant | wrong role, self-sign, missing/NOK checks, active hold and duplicates rejected by deterministic reference model | No safety or quality-release authority granted |

## Checks executed

`python tests/validate.py`: validates quoted YAML frontmatter and links, existing three v0.2 cases with negative mutations, synthetic-source hygiene, and v0.3 deterministic resource, estimate lineage, policy and leak guards. Standalone scripts under `tests/` are stdlib only and never connect to a system.

**What this proves:** the *specific authored fixture expectations* and deterministic arithmetic are reproducible and select documented failure modes are rejected. It does **not** prove a fresh agent uses these instructions faithfully, product feature fit, real world timing, safe operation, implementation rates or transferability to colleagues. A simple validator can be overfitted to known fixtures.

## Evidence still required before promotion

- Independent runs on >=2 agent/host combinations using **inputs only** and without showing expected outputs, tests or this report.
- At least one new colleague-created fictional fixture; one case where time modelling should **not** trigger; one case with false apparent overlap, where same word `UAT` represents different acceptance obligations.
- Human review: does uncertainty propagate selectively; does the assistant distinguish event time from arrival and release; does it refuse net savings without a delivered-work reconciliation?
- Record all failures and update the skill methods by cause, not test-ID wording.

**Repository distribution:** public CC0 package is synthetic. Private historical analysis is deliberately not committed, copied or quoted here.
