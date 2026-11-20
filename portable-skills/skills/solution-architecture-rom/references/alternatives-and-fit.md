# Capability-led option analysis: challenge the requested platform

## Separate demand, symptom and mechanism

Customer statement → affected operational decision → evidence of current failure → measurable target → required capability → intervention candidates.

Example (fictional): "We need an MES to improve OEE" → operator cannot distinguish planned cleaning from fault stops → inconsistent time semantics and reasons → trustworthy loss reasons and defined response ownership → event semantics and exception capture → options include no-new-platform taxonomy+work instructions, standard OEE/configuration, or broader execution platform. This is *not* a conclusion that an MES is inappropriate; it is a hypothesis to test.

## Three options minimum when genuinely viable

- **A: Minimum change / no new platform.** Procedure/role/master-data correction, existing system configuration, manual controlled workflow. Assess failure, scalability and support limits honestly.
- **B: Reuse or integrate incumbents.** Existing ERP/MES/SCADA/historian workflows plus governed interface, without duplicating execution authority.
- **C: New composable or platform capability.** Product configuration, orchestration/UNS and/or specialised module. If options converge after evidence, document why rather than inventing alternatives.

### Decision matrix

For each capability/option, record `source_claim_ids`, `demonstrated|documented|vendor-asserted|proposed|unknown`, functional fit, exception coverage, authority model, data readiness, lifecycle implications, organisational change, proof required and strongest objection. **No weighted scoring until decision makers agree weights**, and never treat a weighted score as a substitute for a mandatory safety/compliance/authority gate.

Use `FIT` only for a capability actually evidenced within the requested boundary; `CONDITIONAL` when a known precondition applies; `GAP` when contrary evidence exists; `UNKNOWN` when unverified. A capability being sold/licensed does not make it integrated, commissioned or accepted.

## Reject attractive answers when

- The requested vendor product solves a different problem from the one demonstrated.
- The data master is inadequate; software optimisation would amplify bad order/recipe/changeover data.
- Local ownership of the exception is unresolved; software would make a disputed decision faster, not better.
- Standard product fit is overstated; planned custom extensions defeat the economics of the selected product.
- A low-code alternative is compared with MES on screen count alone rather than operational traceability, governance and lifecycle.

## Value hypothesis / counter-hypothesis

For each option state:

1. Mechanism: how does behaviour change, and whose decision becomes better?
2. Value: what outcome improves and how will it be measured?
3. Dependency: master data, process acceptance, semantics, people, licences, support.
4. Negative: under what evidence would this option become worse than doing nothing?
5. Reversal: can it be trialled and undone without breaking live operations?

Identify not only expected benefits but **adoption burden** and ability/willingness of operations to change. A credible architecture that nobody uses is not value.
