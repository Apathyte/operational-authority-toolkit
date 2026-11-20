# Contested decision policies -> negative acceptance specifications

Treat different procedures or stakeholder accounts as **distinct labelled candidate policies**, not a single reconciled rule. Only an external authorised decision can select a policy. Example (fictional): `P-A` requires an independent sign-off *before inspection*; `P-B` requires a 6-item independent sign-off *after inspection but before downstream work*. Neither is approved merely because a skill can test it.

## Candidate policy contract

For each candidate: `policy_id`, `version`, `claims/sources`, `object_transition`, `trigger`, `authorised_role`, `actor_separation`, `required_evidence/check_count`, `guard`, `expiry/shift_change`, `active_hold_behaviour`, `correction/override_authority`, `approved_status`, `decision_owner`. Include an explicit `not a PLC/safety permissive` boundary when software approval may appear to authorise machine operation.

## Generate negative cases (only the relevant ones)

- wrong role and self-approval: rejected without mutating decision state;
- incomplete/missing/NOK required checks: rejected, reason recorded;
- repeat submission, replay and stale approvals: idempotent/rejected with audit;
- ongoing quality/safety/maintenance hold: workflow cannot claim release;
- missing network or clock quality: queue/pending/reconcile rather than fabricate success;
- unauthorised override, retroactive correction or deleted evidence: rejected/escalated;
- transition before predecessor/guard: rejected; record who resolves exception.

For each test: `preconditions`, `action`, `expected_state`, `expected_audit`, `rejected_reason`, `recovery`, `authority_proof`, `execution_status`. A test passing in an offline reference model does **not** establish target product behaviour. If the host has no execution tool, write `NOT EXECUTED`, show input/expected output and refrain from saying PASS.

**Safety:** These are application-level workflow policies and simulated tests only. Never convert a digital sign-off into hardware interlock bypass, write-back, automatic restart, or live OT control. Actual safety/QA permission needs separately authorised experts and evidence.
