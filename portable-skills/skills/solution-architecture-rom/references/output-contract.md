# Solution architecture & ROM output contract v0.1

Minimum sections:

- `case_id`, upstream `source_claim_ids`, `target_capability`, `alternatives` with trade-offs
- `mvp` with outcome, boundaries, acceptance evidence and exclusions
- `fit_gap` with statuses and source claims
- `ownership` with each contract boundary and unresolved owner
- `estimate_status`: `ROM BLOCKED` or `CONDITIONAL ROM`
- `estimate_basis`, `workstreams`, `external_dependencies`, `risks`, `decision_gates`
- `commercial_status`: `NON-BINDING / NOT FOR CONTRACTING`

If numeric ranges exist, each line needs unit (engineering days), bounded activity, low/high, basis, and conditions. Totals must sum exact component lows/highs, and must exclude any dependency labelled separately unestimated. Estimates must never imply approved prices or acceptance.
