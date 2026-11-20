# Operational state and exception reconstruction

## Model the object, not merely the process boxes

Start with one transaction and list objects with a stable ID, creation event, lifecycle, linkage and granularity. Typical objects: demand/order, recipe/version, batch, lot, machine, check, deviation, quality hold, person/role, work instruction, event. Decide whether a state belongs to a **physical asset**, **material**, **order**, **work instruction**, or **authorised decision**. Cross-object equality is not automatic.

Represent each consequential transition as:

`object / from → to / trigger / actor / required guard / evidence / timestamp owner / duplicate-or-retry behaviour / exception-or-compensation / source IDs`.

An example (entirely fictional):

| Object | From → to | Trigger | Guard | Evidence | Failure |
| --- | --- | --- | --- | --- | --- |
| Cleaning task | ASSIGNED → EXECUTING | operator starts | assignment valid | operator/start timestamp | late start escalation |
| Cleaning task | EXECUTING → COMPLETED | all steps marked | steps verified? **UNKNOWN** | checklist entries | interrupted step resumes or invalidates? |
| Equipment | STOPPED → AVAILABLE | production release | quality/ops approval **UNKNOWN** | release record | remain stopped pending decision |

`Cleaning task COMPLETED` and `Equipment AVAILABLE` are **not the same state**. `Run=0` does not establish cleaning was performed.

## Minimum questions per object

- Who creates the ID and where is identity reconciled across systems?
- Which events are commands, acknowledgments, observations, calculated states or decisions?
- What guards an irreversible transition? Who authorises the guard?
- What is the allowed state graph? Are there illegal transitions and why?
- Where is time recorded: source, gateway, broker, business application, manual entry? Is order authoritative?
- How do manual correction, rescind, override, partial completion, restart, retry and replay behave?
- How are competing representations reconciled and conflicts surfaced?

## Model at least three exception paths when relevant

1. **Operational deviation:** material shortage/substitution, incomplete cleaning, quality hold, changeover overrun.
2. **Information deviation:** missed event, duplicate, delayed timestamp, wrong unit, mismatched lot or machine ID.
3. **Human-authority deviation:** operator workaround, supervisor override, missing quality release, change of shift.

Not all scenarios apply. Do not invent failure pathways as observed facts; list them as `TEST SCENARIO` with the required authority/evidence. Where safety or regulated control is implicated, do not specify bypass or unsafe operation. Document and defer to a competent specialist.

## Invariants: assertions the model must preserve

Examples that MUST be verified/approved for the actual process before adopting:
- `Task completed` cannot be equated to `equipment authorised to start`.
- A quality hold cannot be released solely on an unchecked external event.
- A changed lot identity cannot silently inherit a different lot's evidence.
- Replayed events cannot multiply physical production or approvals.
- An operator correction must retain who changed what, when and under which authority.

Write these as explicit **proposed invariants**, not as claims that the site already enforces them. Each needs an owner, authoritative proof and failure test.

## Stop when evidence is insufficient

When a transition has unknown guards, describe it as unresolved. Do not fabricate a complete state machine for a messy plant; present a minimal, bounded graph, its holes and the next discriminating observations. This is often more useful than a polished digital-twin diagram.
