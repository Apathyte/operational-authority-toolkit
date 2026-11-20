# Solution Architecture & ROM deliverable contract v0.2

Readable Markdown first; JSON optional. Preserve all source/claim IDs from discovery (never rename). Minimum fields:

```json
{
  "case_id":"SYN-001",
  "objective":"outcome and decision, not product label",
  "upstream_claim_ids":["C1"],
  "capabilities":[{"id":"CAP-1","acceptance_metric":"...","evidence":"C1"}],
  "alternatives":[{"id":"A0","pattern":"no-new-platform","benefit":"...","limitation":"...","proof_status":"PROPOSED","counterargument":"..."}],
  "mvp":{"actors":[],"transitions":[],"exceptions":[],"acceptance_tests":[],"excluded":[],"deferred":[]},
  "fit_gap":[{"capability_id":"CAP-1","option_id":"A0","status":"UNKNOWN","evidence_claim_ids":["C1"],"test":"..."}],
  "work_packages":[{"id":"WP-1","boundary":"...","owner":"UNASSIGNED","acceptor":"UNASSIGNED","estimate_status":"BLOCKED","unblock_test":"..."}],
  "dependency_graph":[{"from":"WP-1","to":"WP-2","kind":"required-for-runtime"}],
  "numeric_estimated_scope_only":null,
  "rollout":{"first_site":"UNESTIMATED","site_classes":[],"next_site":"UNESTIMATED"},
  "lifecycle":{"hosting":"UNESTIMATED","support":"UNESTIMATED","upgrade":"UNESTIMATED"},
  "risks_and_counterevidence":[],
  "decision_gates":[{"id":"G1","status":"OPEN","owner":"UNASSIGNED","evidence_to_unblock":"..."}],
  "approval":"NOT GRANTED",
  "commercial_status":"NON-BINDING / NOT FOR CONTRACTING"
}
```

Numeric WP entries, when included, must carry `quantity`, `unit`, `basis_source_or_declared_hypothesis`, `low_days`, `high_days`, `condition`, `scope`, `owner`, `reestimate_trigger`; aggregate only the estimated WPs and assert total = sum. A `BLOCKED` WP cannot contribute numerical `0` to the total. Include an explicit `excluded/unestimated/third-party` coverage view adjacent to any subtotal. Do not confuse proposal with signed owner acceptance.

## Decision memo headings

1. Problem and measurable target (counter-hypothesis)
2. Verified vs provisional evidence and blocked semantics
3. A/B/C alternatives with feasibility tests and change/adoption cost
4. Minimum coherent first-use outcome and negative acceptance tests
5. Responsibility and integration graph
6. Fit/gap by capability and *proof status*
7. Per-WP estimate readiness and estimated-scope-only conditional ranges
8. Full-scope rollout/lifecycle coverage (or why unestimated)
9. Strongest objection, gating evidence and named decision roles

A colleague should be able to take only this memo, challenge the assumptions and decide what evidence to commission next. It must not depend on knowing who originally prompted the agent.
