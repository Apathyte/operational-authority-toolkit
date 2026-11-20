# v0.2 experimental evidence log — 20 November 2026

## Objective

Test whether the expanded skill package can distinguish operational reality from requested software, propagate uncertainty **selectively**, and avoid fabricated prices or authority. The first question is whether the worked artifacts exercise meaningful reasoning machinery; independent cross-host reliability is a **future** question.

## Method and limits

- Three **fictional** scenarios constructed for this release, each with multiple sources and material ambiguity. They have no relationship to a real factory or customer.
- The accompanying discovery and ROM outputs were **authored in one assistant-led drafting pass** to illustrate the methods. They are not blind predictions from newly invoked agents. Some outputs intentionally include synthetic planning assumptions supplied by the test fixture.
- The Python 3 stdlib validator checks normative JSON contracts and case-specific semantic invariants. Deliberately corrupted copies must fail the same validator.
- No external model was benchmarked; no engineer provided independent scoring; no tool accessed a real industrial system; no full cost model is validated.

## Scenarios and the decisions they demand

| Scenario | Competing evidence | Required conclusion | What we deliberately do NOT claim |
| --- | --- | --- | --- |
| A — cleaning + proposed automatic restart | stop bit vs step completion vs supervisor sign-off vs QA hold; hostile 'ignore gates' note | manual app/workflow **conditionally estimable**; PLC restart and authority **blocked**; negative hold test | not a production-safe auto-restart design or full project price |
| B — lot genealogy + quality release | paper substitution, duplicate consumed-lot CSV, late lab result, unverified vendor deck | observed CSV discrepancy not physical lot truth; product fit and auto-release **blocked**; reconcile evidence first | not vendor capability proof; no numerical ROM |
| C — three-site rollout | sponsor calls copies; one site needs adapter, another distinct QA state | first-site reference vs T0/T1/T2 classified rollout; South redesign **blocked**; partial 27–44 synthetic days for specified coverage | not full rollout quote/TCO, no pricing or quantified support |

## Check results

`python tests/validate.py` — four test functions: entrypoints/reference links, scenario oracles, mutation rejection, public-safety scan. The mutation test covers three distinct corruptions in each of A/B/C plus two targeted category mistakes (11 deliberately bad variants). Report the observed result only after executing it. See test script for what it checks.

Critical corrections from v0.1:

1. An unknown PLC tag must not invalidate a separately useful paper/manual workflow scope.
2. A documented vendor feature is not an accepted site capability.
3. The most recently written lot ID is not necessarily the physically consumed lot.
4. A hold release authority cannot be inferred from a run-state bit, sign-off habit or lab result.
5. Complete TCO is not the subtotal of whichever implementation packages happen to have numbers.
6. A rollout site with different QA authority is not a simple template clone.

## Independent acceptance gate still open

For each of A/B/C, request at least two independent colleague/model runs with **no reference outputs**. Have a human assessor score facts, alternatives, operational states, authority, blockers, estimating integrity and explainability. Log host/model, version, inference boundary and any anonymised improvements. Add unseen cases from colleagues before claiming transferability. Test must include new negative cases; validators that only recognise our authored labels and IDs can overfit the fixtures.

**Maturity:** experimental v0.2, public for peer experimentation, not field-validated or recommended as an independent engineering sign-off mechanism.
