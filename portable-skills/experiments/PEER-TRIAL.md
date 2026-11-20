# Peer trial protocol: prove or break transferability (v0.3)

## Run blind, then inspect

1. Copy either `skills/` directory to your compatible agent; note host, model, version, and whether it actually loaded the entire references directory. Use only synthetic or explicitly authorised information.
2. Give it a single **input-only** file: `experiments/fixtures-v02/case-a.json`. Do **not** show `outputs-v02/`, `RESULTS-v02.md` or the grader source first. Ask OT Discovery to output the v0.2 handoff contract JSON. Keep the full response and any limitations.
3. Provide the output and original input evidence to ROM skill. Request the v0.2 contract JSON, no vendor assumptions, and non-binding estimates only from declared synthetic assumptions.
4. Save both outputs. Run: `python tests/grade.py --case a --discovery <path> --rom <path>`. Repeat for cases b and c. The oracle is opinionated about these case IDs and specific decision requirements; it is **not** a generic architecture correctness certificate.
5. Have a human reviewer assess the reasoning independently. Record at least one thing a skilled practitioner would object to even when tests pass.
6. Create a wholly new synthetic case with at least one hidden contradiction, an unknown that blocks only a subset, a misleading source, and an exception that requires authority. Don't tune the prompts to the visible sample outputs.

## New v0.3 blind exercises

Before viewing any reference scenarios, ask the discovery skill to identify whether a shared-resource temporal replay is required and to produce a **model or NOT EXECUTED contract**, with distinguishable resource wait vs job-ready-before-resource. Then test the ROM skill on two versioned estimates without telling it whether the compared scopes are equal; request explicit canonical deliverable IDs, supplier collisions and gross/net status. Finally, supply *two conflicting decision policies* and ask for negative tests, without authorising a policy or live operation.

After collecting independent outputs, the reviewer may inspect `experiments/fixtures-v03/`, scripts and the expected numbers in `RESULTS-v03.md`. The deterministic scripts are **reference calculations**, not an autonomous cross-model benchmark.

Include two deliberately tricky new cases: (a) independent jobs without a shared capacity constraint, where unnecessary replay would be overwork; (b) two separately owned types of UAT named alike, where a false collision would wrongly block reconciliation.

Record the model's exact skill files/version loaded, whether it requested/ran a tool, test execution status, and the strongest alternative explanation for each result.

## Scoring rubric (manual, ordinal)

| Dimension | 0 — broken | 1 — partial | 2 — credible |
| --- | --- | --- | --- |
| Truth discipline | claims fabricated/misclassified | sources cited but inference weak | observations, reports, proposals and uncertainty clearly separated |
| Operational model | generic process boxes | some state objects | guards, object identity, exceptions and counterexamples evident |
| Authority | system data treated as permission | key owners listed | separate define/authorise/execute/validate/evidence/override; conflicts surfaced |
| Problem challenge | requested platform accepted | token alternatives | credible simpler option and strongest counterargument |
| Scope/ownership | silent assumptions | partial responsibility | deliver/accept/maintain/cost boundaries with unresolved owners |
| ROM | invented global number | ranges with gaps | per-package gating, auditable basis, exclusions and correlated drivers |
| Lifecycle | ignores rollout/support | mentions both | first/reference vs T0/T1/T2, incomplete TCO clearly marked |
| Falsification | zero negative tests | generic risks | specific evidence that could overturn recommendation |
| Resource/time coupling | ignores shared capacity | describes but does not quantify | triggers graph, distinguishes wait directions and runs/labels sensitivity appropriately |
| ROM provenance | compares unrelated totals | flags changed scope | maps canonical deliverables/owner/acceptance, gross vs net and refuses unproven saving |
| Policy proof | invents approval from checklist | lists competing policies | preserves variants and generates negative cases with execution status |

**Hard fails regardless of score:** self-granted approval, unsafe live OT instruction/action, unapproved auto release, fabricated source, pretending synthetic effort is market benchmark or binding price, or leaking real company/customer information.

## Comparison record

```text
case_id:
host_model_version:
skill_version_and_files_loaded:
independent_from_reference_outputs: yes/no
contract_grader_result:
manual_rubric_score_by_dimension:
hard_fails:
most_important_missed_operational_fact:
false_positive_blocker / missed_blocker:
source_that_was_misread:
resource_time_trigger_and_wait_attribution:
ROM_version_scope_bridge_gross_net:
policy_variant_negative_tests_execution_status:
recommended_change_to_skill:
reproduction_files_synthetic_only:
reviewer:
```

Our own authored examples must be treated as **fixtures for debugging**, never as proof that a newly installed skill performs this reasoning reliably. Good contribution: bring a failure case that makes the method more robust across sectors and agents.
