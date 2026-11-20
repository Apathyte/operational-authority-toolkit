# Field investigation playbook — discover the lived process

This is a **question library and observation method**, not permission to enter a plant, probe a controller or record workers.

## Three passes

**Pass A — declared intention:** ask operations, quality, planning, maintenance, IT/OT what ought to happen; capture SOP revisions, role definitions and system diagrams, including provenance. Ask what outcome justifies spending money.

**Pass B — actual work:** follow a single unit of work from incoming order through release/stock, or one cleaning/changeover activity. Ask an operator to narrate the last interruption. Record who actually makes decisions, what is copied to paper/Excel, where people know more than systems, and which screen is ignored. Never call a workaround a defect before understanding its purpose.

**Pass C — divergence:** compare day/night shift, planned/unplanned work, clean/dirty data, normal/exception, and new/experienced operators. Ask one *what would prove our interpretation wrong?* question per high-impact claim.

## Core prompts by role

| Role | Ask | Look for |
| --- | --- | --- |
| Operator | Show last late-start, correction and shift handover. Which system do you not believe? | workarounds and local authority |
| Supervisor | When do you allow restart or override? What if everyone is absent? | delegated authority and escalation |
| Quality | What is the exact evidence for hold, disposition and release? | decision versus status |
| Planner | What changes after order release, and who is informed? | timing / plan-vs-execution split |
| Maintenance | What constitutes fit to return, and who owns that statement? | machine status vs work order close |
| Automation engineer | What can be safely observed? Source time, quality bits, semantic map, ownership? | connectivity feasibility without intrusive action |
| IT/security | Accounts, zones, egress, change control, logging, retention, recovery? | authorised access and support |

## Evidence request order

Start with non-invasive approved artifacts: process documents, role matrix, sample redacted transaction, interface contract, time-stamped event sample, standard runbook, change records. Progress to authorised observation and test environments if necessary. Never infer permission to browse live networks or write PLCs from the user's wish to get the answer.

## Falsifiable tests

- **Contradictory release:** a checklist is complete while quality hold remains active: what may the system display and command?
- **Late arrival:** two events arrive out of order: what state wins, who reconciles and what audit persists?
- **Manual correction:** wrong lot posted then fixed: what object and evidence change, and by whose authority?
- **Site variation:** identical equipment labels but different control semantics: what portion of a template is still reusable?

## Time and capacity interrogation

When people or equipment are shared across orders or units, shadow the complete handoff: exact job-ready time, resource arrival, travel, actual start, required checks, finish, released-for-next-step and missed-notification behavior. Ask what happens to the **next two jobs**, not only the delayed one. Obtain comparable timestamps with permission; distinguish expected norms from witnessed durations. Follow [temporal/resource analysis](temporal-and-resource-model.md) before suggesting capacity improvements.

## Output question discipline

Prefer a compact set of high-impact unanswered questions ordered by `consequence × reversibility × decision urgency` (qualitative, not invented numerical score). Each asks for a **specific evidence-producing action**, not a generic workshop. Example: “Provide the approved quality-release decision record and a redacted event trail demonstrating that hold cannot be cleared by the PLC idle bit.”
