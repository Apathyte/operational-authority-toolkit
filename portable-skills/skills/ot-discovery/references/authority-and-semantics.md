# Operational authority and interface meaning

## Six verbs, six different powers

For each consequential object/transition, fill:

| Verb | Investigation prompt | Example distinction |
| --- | --- | --- |
| DEFINE | Who sets the meaning and valid range? | production state code definitions vs UI labels |
| AUTHORISE | Who permits the action/transition? | quality permits release; operator may request it |
| EXECUTE | Who performs it? | PLC actuates, human cleans, service sends message |
| VALIDATE | Who determines the result met requirements? | checker confirms cleaning; quality verifies exception |
| EVIDENCE | Which record proves action/state with lineage? | historian event, signed check, audit trail |
| OVERRIDE | Who can bypass, rescind, correct with traceability? | controlled override vs silent data edit |

For each assign `actor`, `system`, `authority_source`, `evidence`, `status: CONFIRMED|REPORTED|PROPOSED|UNRESOLVED`, `limitations`. A single role may hold multiple verbs, but **do not collapse them automatically**. Especially distinguish writing a database value from having authority over its meaning.

## System-of-record is not a universal answer

A field's authoritative source varies by question: ERP may own planned order; MES execution status; PLC observed equipment signals; LIMS quality result; human quality authority release. Some facts have no single source until an operational rule is established. Distinguish:

- definition / desired target
- command / permission
- observation / execution result
- validation / acceptance
- durable evidence / replay
- override / correction

Ask what happens when representations disagree. Do not decide by latest timestamp, system hierarchy or vendor branding alone.

## Interface semantic contract (minimum for each consequential signal)

`producer`, `consumer`, `business_object_id`, `machine_identity`, `meaning`, `event_or_state`, `unit`, `source_timestamp`, `ingest_timestamp`, `time_quality`, `source_version`, `sequence_or_idempotency`, `quality_flag`, `authority`, `failure_behaviour`, `replay_policy`, `acceptance_test`, `owner`.

**Example:** `machine_stopped=true` may be a momentary sensor observation. It does not mean `maintenance complete`, `safe to service` or `operator authorised restart`. A broker transferring a signal reliably does not prove the semantic contract is correct. A normalised pub/sub interface needs one named party accountable for tag mapping/meaning and another for downstream workflow; do not quietly assign both to the integrator.

## Three-way ownership separation

1. **Machine domain:** safe access, controller ownership, tags, timestamp origin, units, quality, equipment identity.
2. **Integration domain:** transport, retry, event schema, mapping contract, security and observability.
3. **Workflow domain:** business state, task assignment, exception, approvals, reconciliation and audit.

These boundaries may be combined by agreement but must not be assumed. Whenever site support or upgrades can change meaning, capture lifecycle ownership as a fourth question.

## Disputed decision-point policy

Different accounts of where approval belongs are **versioned policy variants**, not a clerical difference to smooth over. Specify separate guard and rejection tests for each policy; withhold selection until the responsible human signs off. See [policy variants and negative tests](policy-variants-and-negative-tests.md). An app approval controls the app's state only; operational/safety release and PLC permissives are separate domains.

## Authority conflict record

Record at minimum: `object`, `decision`, `claiming_parties`, `candidate_sources`, `current_rule`, `approved_rule_or_UNRESOLVED`, `consequence`, `evidence_to_resolve`, `owner`. A proposed rule cannot authorise itself by appearing in a diagram.
