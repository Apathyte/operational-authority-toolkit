# Temporal and resource coupling — investigate consequences, not just durations

## Trigger (required when present)

If **any** resource is shared among otherwise separate activities — a technician, crew, machine, crane, test bench, warehouse slot, material, changeover window, scarce lab capacity — or if completion, escalation or release depends on elapsed time, analyse time and resource coupling. Do not claim a schedule without adequate evidence. Purely independent activities without timing consequences can state `NOT TRIGGERED` and why.

## Graph and timestamp provenance

Build separate nodes for each object's **ready-to-process event**, resource **arrival/availability**, **start**, **finish**, handover and **permission to proceed**. Edges include precedence, common-resource serialisation, travel/setup, and conditional release or hold. Label every node/edge with source claim or a `HYPOTHETICAL` assumption. Distinguish source event time, transport/ingest time, manually entered time, approval time and scheduling plan. Note timezone, units, clock uncertainty, source freshness and what happens with duplicate, late or missing events.

For one non-preemptive resource in an agreed sequence, a minimal model is:

```
arrival_i = previous_finish + changeover_or_travel_i
start_i = max(arrival_i, job_ready_i, other_authorised_guards_i)
finish_i = start_i + service_duration_i
resource_waiting_for_job_i = max(0, job_ready_i - arrival_i)
job_ready_before_resource_i = max(0, arrival_i - job_ready_i)
```

*Only use the numerical `max` formula for guards expressed as valid times.* A quality hold, permit, safety stop or absence of authorised release is a discrete gate, not a lateness offset. Mark work `BLOCKED` rather than assigning a fake timestamp. `resource_waiting_for_job` is not the same as `job_ready_before_resource`. `start - job_ready` is not necessarily worker waiting, especially when there are prerequisite tasks or other guards.

## Minimum perturbations

When evidence supports the parameters, compute baseline plus: (1) a delayed-ready/missed trigger or absent resource, and (2) a disputed service norm or duration. Trace downstream finish, slack, waiting attribution, deadline breaches and who receives escalations. If there is no reliable basis, produce **symbolic sensitivities** (`+Δ on upstream A may propagate through B`) and a reproducible `NOT EXECUTED` test plan; never claim measured shift performance.

When tools are available, prefer tiny deterministic calculations with declared fixture inputs and at least one negative assertion (e.g. a second resource cannot be double-booked; a hold prevents start). State script/version, input hash if applicable, execution status and what the test does **not** prove. An LLM mental calculation alone is a hypothesis until verified.

## Investigation questions

- Does the schedule use physical readiness, notification time, task acknowledgement or actual arrival?
- Are durations inclusive of setup, cleanup, inspection, restart and travel, or counted separately?
- Does a resource work one job at a time? Are overtime, shift change and parallel work allowed?
- Which milestone is an operational observation, which is planning intent, which is a human decision?
- Which clock determines an SLA breach; what happens when the event is late or corrected?
- Does a variance affect just the first job, or propagate into downstream work and other objects?

## Output card

`trigger`, `source_claim_ids`, `jobs_and_resource_ids`, `precedence_edges`, `clock_semantics`, `baseline_inputs`, `scenario_delta`, `resource_wait`, `job_ready_before_resource`, `finish`, `impacted_operational_decisions`, `invariants`, `execution_status=EXECUTED|NOT EXECUTED`, `limitations`, `evidence_to_validate`. When reporting an illustrative clock, mark **synthetic scenario** explicitly. Do not put private customer timelines in a public regression fixture.
