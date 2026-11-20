# Portable Industrial Skills — v0.2 experimental

**We give away the reasoning method, not merely the paperwork.** Two open, vendor-neutral Agent Skills for evidence-led operational discovery and industrial software/automation solution qualification. Public-domain dedication: [CC0-1.0](LICENSE.md). No corporate endorsement, no proprietary customer material, no real factory data, no vendor guarantees.

This repository folder is the **public experimental branch** of a wider skill idea. The package is portable at the `SKILL.md` format level; model results are **not automatically interchangeable** across hosts. Two independently installable skill folders deliberately carry their own reference documents.

## What changed from v0.1

| Dimension | v0.1 | v0.2 |
| --- | --- | --- |
| Discovery | list facts/unknowns | source reliability, counter-hypotheses, object lifecycle, guarded transitions, failure/retry paths, six-verbs authority, interface semantics and falsification |
| ROM | options and broad estimate status | no-build comparison, ability to challenge platform premise, site/partner responsibility graph, scope-specific readiness, detailed synthetic units, first vs nth site economics, incomplete TCO |
| Unknowns | could block whole ROM | **selectively block affected decisions**, preserve independently testable/manual work |
| Evaluations | two small illustrative examples, structural checks | three larger synthetic scenarios, richer model-authored outputs, case-specific offline oracle and negative mutations |
| Confidence | no independent runs | still **no independent model runs or field validation**; candid peer protocol provided |

## Install

Copy **either entire skill folder** into the directory supported by your assistant:

- `skills/ot-discovery/` — source, authority, state/exception and semantics investigation.
- `skills/solution-architecture-rom/` — outcome-led alternatives, selective ROM, responsibility and rollout/TCO.

Many Agent Skills-compatible environments look for a `SKILL.md` and lazily load `references/`. Common directories include `.agents/skills/`, `.github/skills/`, `.claude/skills/`; exact compatibility and discovery rules depend on the host. **No runtime, API key, plugin or access to our GitHub account is necessary.** The skills do not depend on each other, though passing stable discovery claim IDs into ROM enables evidence tracing.

## Use it — independent workflow

Give the first skill *your own authorised notes* or a fictional scenario. Ask:

> Use the OT Discovery skill. Reconstruct the operational objects and transitions, identify where evidence or authority conflicts, propose tests that could falsify your conclusions and state exactly which downstream decisions remain blocked versus unaffected. Do not design or estimate yet.

Give the resulting evidence-led report to the second:

> Use Solution Architecture & ROM. Challenge the requested product, compare the simplest credible alternatives, define a minimum coherent pilot with negative acceptance tests, allocate owners and uncertainty per work package, and estimate only work packages with an explicit legitimate basis. Show what remains outside every subtotal and distinguish first site from future rollout.

For an independent benchmark, use a fresh model run with the `experiments/fixtures-v02/` inputs and **do not show** it `outputs-v02/` or the case-specific grader first.

## Real methodology, not templates alone

The investigation distinguishes `cleaning complete`, `equipment stopped`, `quality authorised` and `safe/allowed to restart`. Those can be separate objects and transitions with distinct authorities. It distinguishes a reliable interface from one with **correct meaning**. The ROM process separates product, machine connectivity, integration, workflow, deployment, validation and managed service; an unknown interface can block *that* work package without necessarily blocking a manual trial. First-site reference build economics differ from parameterised site reuse, adapter work and genuine process redesign.

Read each skill's `SKILL.md` then its linked reference playbooks to inspect the actual reasoning procedures. The reference documents provide investigation questions, falsification methods, state/authority modelling, decision matrices, estimation formulae, ownership semantics and adversarial reviews.

## Reproducible offline checks

Python 3.9+ standard library only, no network, no model calls:

```bash
python tests/validate.py
python tests/grade.py --case a --discovery experiments/outputs-v02/case-a.discovery.json --rom experiments/outputs-v02/case-a.rom.json
```

The tests check contract traceability, state/authority references, source IDs, conditional-vs-blocked estimates, subtotal coverage, exceptions and scenario-specific failures, plus deliberate mutation/rejection. **They do not measure independent agent competence, hallucination rate, solution quality in a real plant or ROI.** `experiments/RESULTS-v02.md` and `experiments/PEER-TRIAL.md` spell out the evidence gap and how to close it.

## How to improve it responsibly

Open an issue or PR with a *synthetic or permitted* counterexample showing where an agent got a claim, ownership or architectural decision wrong. Provide the input, expected invariant, observed bad output, and a minimal reproduction that does **not** include confidential material. Challenge not just the phrasing but the reasoning. Do not upload identifiable interviews, proprietary estimates, production addresses, controller credentials, internal system diagrams or customer-specific procedures. Real industrial deployments require local technical, cyber/safety, operational, quality and commercial approval.

The v0.1 baseline is retained in `experiments/v01-baseline/` for honest comparison, not as the current reference output contract. Names are provisional and versions are experimental; adoption is not certification.

## Licence

Original skill contents, synthetic fixtures and test scripts in this package are dedicated under [CC0-1.0](LICENSE.md). Third-party standards or proprietary implementations are not reproduced. No warranties, no safety certification and no automatic authorisation to connect to operational systems or commit a company financially.
