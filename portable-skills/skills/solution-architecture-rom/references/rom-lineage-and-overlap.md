# ROM revision lineage — compare obligations, not headline day totals

A ROM is a versioned **scope-and-ownership hypothesis**. When comparing two estimate versions or multiple suppliers, do not infer improvement or confidence from numerically narrower ranges alone.

## Canonical deliverable ledger

For every line record `estimate_version`, `as_of_date`, `wp_id`, `canonical_deliverable_id`, `acceptance_id`, `deliverable_description`, `site_count`, `quantity_and_unit`, `supplier`, `delivery_owner`, `test_owner`, `acceptor`, `operating_owner`, `support_owner`, `status` (included/conditional/excluded/optional/unestimated), `assumptions`, `dependencies`, `low/high engineering days`, `external_costs`, `change_reason`. Use an explicit mapping table when names differ between supplier spreadsheets. A matching title is **not** proof that two lines represent identical work; matching quantities, acceptance and contract boundary matter.

## Comparability audit (must precede delta calculation)

1. **Identify scopes:** first pilot vs whole factory; first site vs rollout; product vs integrator vs external OEM; fixed vs optional items; support, licenses, hosting, hardware and lifecycle.
2. **Normalise deliverables:** map line IDs to a canonical deliverable and acceptance result. Check whether UAT is a vendor test, SI product UAT, integrated acceptance or operator acceptance — these are not inherently duplicates.
3. **Classify revision differences:** `SAME-BOUNDARY-REESTIMATE`, `SCOPE-ADDED`, `SCOPE-REMOVED`, `OWNER-TRANSFER`, `ASSUMPTION-CHANGED`, `METHOD-CHANGED`, `UNRESOLVED`.
4. **Detect overlaps:** if two suppliers claim the same canonical acceptance/deliverable, identify the exact task/portion and contractual owner. A collision is a **review flag**, not proof of 100% duplicated effort. Preserve the supplier gross subtotal.
5. **Report four states separately:** `GROSS ESTIMATED-SCOPE` (sum of all included estimated supplier lines, with overlaps flagged); `DUPLICATION IDENTIFIED` (matched tasks with signed scope boundaries); `NET RECONCILED` (only if duplicate portions quantified against a consistent scenario and accepted ownership); `NET UNRESOLVED` (otherwise). **Do not subtract the low of one range from the high of another as a fake saving.**
6. **Quantify deltas only on equivalent scope **with an explicit signed/recorded equivalence basis:**** if both versions cover the same canonical deliverables, acceptance and delivery boundary, compare corresponding lower/upper assumptions. Otherwise show a scope bridge and `NOT COMPARABLE` overall.

## Practical source/line comparison record

| Field | Version A | Version B | Result |
| --- | --- | --- | --- |
| Boundary | single work cell | first factory | NOT COMPARABLE |
| Product UAT | integrator | integrator + vendor UAT | COLLISION TO INVESTIGATE |
| Controller mapping | excluded | supplier-dependent | ADDED/UNESTIMATED |
| Warranty/support | excluded | still excluded | unchanged open lifecycle |

## Synthetic example (not a customer rate)

A v1 estimate contains `APP-WORKFLOW`, `APP-UAT`, `SOURCE-ADAPTER`. A v2 includes those plus a vendor's `APP-UAT` and `EVENT-CONTRACT`. If v2 gross is **27–44 synthetic engineering days** and the vendor's APP-UAT overlaps an integrator APP-UAT, the **net is unknown** until the test/acceptance portions are reconciled. Neither v2−v1 nor subtracting the entire vendor UAT is a defensible change claim. The actual gross example is in `experiments/fixtures-v03/lineage.json` (synthetic only).

## Acceptance and authority

A verified line reconciliation requires provenance to both source versions, who approved delivery boundaries, estimates restated per surviving task, and a distinct human commercial review. `NET RECONCILED` still does not imply price approval. If changed scope cannot be traced, retain previous baseline as historical and require fresh scoping; never silently overwrite it.
