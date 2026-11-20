# OT discovery output contract v0.1

Minimum report content:

- `case_id`, `objective`, `boundary`, `evidence` (`id`, `origin`, `statement`, `limitation`)
- `claims` (`id`, `status: FACT|INFERENCE|ASSUMPTION|UNKNOWN`, `statement`, `evidence_ids`)
- `as_is_flow` (observable steps and exception path; cite any source-dependent statement)
- `authority_gaps` (`object`, `question`, `evidence_ids`)
- `unknowns` (`id`, `question`, `impact`, `owner_or_role`, `gate`)
- `design_gate`: `OPEN` until key uncertainties are resolved. Discovery must not issue a commercial Go/NoGo.

For each FACT claim, the evidence list must reference actual source IDs. For UNKNOWN claims, do not fabricate supporting evidence; point to the relevant gap if available. Evidence can report a source's statement without proving its operational truth. Preserve original source IDs across stages.

Recommended standalone tables: Source/Evidence, Object/Authority Verbs, Claim/Status, Unknown/Gate.
