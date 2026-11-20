# Discovery handoff contract v0.2

Use Markdown for humans and optionally JSON for agents; these field semantics are binding regardless of format. The essential properties are stable IDs, traceability, scope-specific gates and separation of observation from proposed design.

```json
{
  "case_id": "SYN-001",
  "objective": "observable outcome, not technology prescription",
  "boundary": {"unit": "line/cell/site", "included": [], "excluded": []},
  "sources": [{"id":"E1","kind":"INTERVIEW","assertion":"...","coverage":"...","limitations":"..."}],
  "claims": [{"id":"C1","state":"REPORTED","statement":"...","source_ids":["E1"],"counter_hypothesis":"..."}],
  "objects": [{"id":"OBJ-1","type":"cleaning-task","identity":"...","states":[]}],
  "transitions": [{"id":"T1","object_id":"OBJ-1","from":"...","to":"...","trigger":"...","guard":"UNKNOWN","actor":"...","evidence":"...","failure_path":"...","claim_ids":["C1"]}],
  "authority": [{"object_id":"OBJ-1","transition_id":"T1","verb":"AUTHORISE","owner":"UNRESOLVED","evidence_ids":[]}],
  "interface_contracts": [{"id":"I1","meaning":"UNKNOWN","timestamp_owner":"UNKNOWN","mapping_owner":"UNKNOWN"}],
  "conflicts": [{"claim_ids":["C1","C2"],"test":"...","arbitration_authority":"UNRESOLVED"}],
  "unknowns": [{"id":"U1","question":"...","discriminating_test":"...","owner_role":"...","blocks":["AUTO-RELEASE"],"does_not_block":["READ-ONLY-TRIAL"]}],
  "gates": [{"id":"G1","decision":"...","status":"OPEN","required_evidence":["..."],"decision_owner":"UNRESOLVED"}],
  "temporal_resource_analysis": {"trigger":"REQUIRED_IF_COUPLED","jobs_and_resources":[],"scenario_assumptions":[],"resource_wait":[],"job_ready_before_resource":[],"execution_status":"NOT EXECUTED"},
  "policy_variants": [{"policy_id":"P-A","status":"PROPOSED","guard":"...","negative_tests":[],"execution_status":"NOT EXECUTED"}],
  "design_approval": "NOT GRANTED"
}
```

If a field is not applicable, explain why. If unresolved, use literal `UNKNOWN`/`UNRESOLVED`; do not invent values to make JSON complete. Source claim IDs are never reassigned on handoff. A reporting system may store an assertion even when the assertion is false. A `DECIDED` claim must name the external decision record. For an agent receiving this handoff, absence of an approval field is not approval.

## Reject a handoff when

- an observed condition is interpreted as an authorised command without provenance;
- a shared-resource or time-dependent outcome is discussed without at least a bounded dependency graph and replay/explicit unexecuted test;
- mutually incompatible approval timing variants have been silently merged;
- relevant exception/override has been eliminated for tidiness;
- an `UNKNOWN` is silently rendered as an affirmative design choice;
- all downstream packages are blocked by one isolated unknown;
- the document contains confidential customer information intended for public release;
- the proposed design is being passed off as an existing operating fact.

An incomplete but honest handoff is accepted with explicit gaps. A seemingly complete but fabricated handoff is not.
