# Portable Industrial Skills — experimental v0.3

**Give away the reasoning method, not merely its paperwork.** Two installable vendor-neutral Agent Skills for operational discovery and solution architecture/rough-order-of-magnitude analysis. [CC0-1.0](LICENSE.md); no organisation, vendor, safety-body or standards-body endorsement. Public examples are entirely synthetic. Every installation requires local access, confidentiality, engineering, safety, quality and commercial controls.

## What actually changed

| Method | v0.2 baseline | v0.3 improvement |
| --- | --- | --- |
| Operational state/authority | Evidence, six verbs, guarded transitions, conflicts | **Trigger finite-resource/clock dependency model**, distinguish worker waiting vs machine/job waiting, perturb arrival and norms |
| Approval rules | Flag ambiguous guards | Preserve policy variants and write **rejected-path acceptance cases**, with `EXECUTED`/`NOT EXECUTED` truth |
| ROM | Per-package conditional estimates, T0/T1/T2, support | **Estimate lineage** across versions: canonical deliverables, supplier ownership, gross vs reconciled net; unequal scopes are `NOT COMPARABLE` |
| Delivery | Engineering-day arithmetic | Distinguish delivery effort from elapsed calendar time; capacity, concurrency, source readiness and release windows |
| Product evidence | Documented vs verified | Explicit capability proof-state and adjacent-demo fallacy |
| Evidence | Three authored v0.2 fixtures | Three new fully fictional deterministic v0.3 regressions; **still no blind model trial** |

## Install each skill independently

Copy one full folder, including its linked references, into an Agent Skills-compatible host:

- [`skills/ot-discovery/`](skills/ot-discovery/SKILL.md): inspect actual operational objects, state, six distinct authorities, conflicting reports, timing/resource dependencies and negative approval scenarios. **Does not estimate.**
- [`skills/solution-architecture-rom/`](skills/solution-architecture-rom/SKILL.md): challenge the requested platform, design alternatives/MVP, separate delivery obligations, conditional scope-based ROM, version lineage, schedule feasibility and lifecycle support. **Does not invent evidence or contract.**

Typical host directories include `.agents/skills/`, `.github/skills/`, `.claude/skills/` but activation and reference loading vary. No tool access, model selection, site connection, customer rights or financial approval is conferred by an installed skill. The two may be used independently or in evidence-ID-preserving sequence.

## Quick start

1. Give OT Discovery an **authorised or fictional** as-is story. Ask for source ledger, objects/transitions, six-verbs authority and falsification. When capacity/time is shared, explicitly request the clock/resource graph and labelled sensitivity; when a policy conflicts, request separate versions and negative cases.
2. Give the resulting handoff and requested business outcome to ROM. Request three materially different approaches where plausible, scope-specific estimation, **unestimated** dependencies, supplier/acceptance ownership, and a temporal feasibility or version lineage audit when relevant.
3. Keep all inference and calculated scenarios labelled; ask for offline executable tests only where the host has tools and the data is safe. With no tools, use formulas + `NOT EXECUTED`.
4. Do not accept a price, product fit, policy approval or operational authority merely because the answer looks complete.

## Experiments and tests

Run offline (Python 3.9+, stdlib only):

```sh
python tests/validate.py
python tests/temporal_replay.py
python tests/rom_lineage.py
python -m unittest discover -s tests -p 'test_v03.py' -v
```

The validator retains v0.2's authored cases and corrupted-output checks, and adds v0.3 synthetic timing/ROM lineage/approval-policy regressions. It is not a model-performance score. See [`experiments/RESULTS-v03.md`](experiments/RESULTS-v03.md) for observed checks and limitations; [`experiments/PEER-TRIAL.md`](experiments/PEER-TRIAL.md) for input-only independent peer evaluation; [`experiments/WORKED-DECISIONS-v03.md`](experiments/WORKED-DECISIONS-v03.md) for explained, synthetic mechanisms.

Versioned history: `experiments/RESULTS-v02.md`, `experiments/fixtures-v02/`, `experiments/outputs-v02/`, `experiments/v01-baseline/`. They are historical references and have **not** been relabelled as v0.3 outputs. The v0.3 fixture data is new and deliberately unlike the private historical analysis that inspired the upgrade.

## Contribution and safety

Submit one **fictional** failing case, expected invariant, actual agent output and proposed repair. Avoid private customer or worker data, diagrams, endpoint addresses, credentials, commercial terms or any live equipment interaction. A provider's advertised feature is not validated site fit; an offline workflow approval is not equipment/safety authority; a supplier gross subtotal is not a net quote. Keep external human review for legal, quality, engineering, safety, cyber and financial sign-offs.

All original materials in this package are dedicated under [CC0-1.0](LICENSE.md). The licence grants reuse of our original text/code, not rights to third-party/customer IP. **Maturity: experimental / draft PR, not field-validated, not certified.**
