---
name: solution-architecture-rom
description: Turn an evidence-led industrial discovery record into bounded software/automation options, fit-gap, integration ownership, phased MVP and conditional rough-order-of-magnitude effort. Use for early solution design and commercial qualification, never to invent as-is facts or issue a fixed-price offer.
license: CC0-1.0
metadata:
  version: "0.1.0"
  maturity: "experimental"
---

# Solution Architecture & ROM

## Purpose and boundary

Translate **supplied discovery evidence** into explicit design choices, obligations, delivery phases and a decision-ready, non-binding ROM when possible. Do not silently fill discovery gaps. The goal is to make risk ownership visible, not to absorb it in a price. This is not purchasing authority, project approval, safety design, detailed system design or contractual commitment.

## Inputs

Ask for the discovery artifact with its source/claim IDs, target outcomes, constraints, existing standards, proposed ownership model, candidate scope and any independently provided cost/effort assumptions. When unavailable, do a **conditional options and effort-driver analysis** without numeric effort. No direct access to enterprise data or production systems is presumed.

## Workflow

1. Confirm what is `FACT`, `INFERENCE`, `ASSUMPTION`, `UNKNOWN`, and what decisions are authorised. Preserve upstream IDs exactly.
2. Separate the desired **capability** from a named product; describe at least two viable patterns when the evidence supports a meaningful choice, including a minimal/no-new-platform alternative where relevant.
3. Define first-use scope: actors, trigger, system boundary, happy path, exception path, acceptance evidence, and explicit exclusions. Distinguish **product/configuration**, **integration**, **deployment**, **training** and **support**.
4. Build a dependency/ownership table: system of record, signal semantics, data access, event transport, interfaces, application workflow, verification, operational support. Mark missing owner or contract as `UNASSIGNED`, not assumed provider responsibility.
5. Create a fit-gap table by requirement, source claim, option, status (`FIT`, `GAP`, `CONDITIONAL`, `UNKNOWN`) and resolution authority. Do not invent vendor functionality.
6. Select an **estimate readiness gate**. Use `ROM BLOCKED` if critical quantity/complexity or boundary inputs are absent. Otherwise present **conditional engineering-day ranges**, broken down by workstream, with explicit assumptions, uncertainty and separate third-party effort. Never infer a binding price from these ranges, and never claim precision unsupported by evidence.
7. State first paid/approved discovery activities and Go/NoGo questions. Recommend decisions but do not declare them approved.
8. Audit that every design-driving assertion points to a source claim or is explicitly a proposal. `UNKNOWN` evidence cannot turn into a delivery commitment.

## Deliverable contract

Use [ROM output contract](references/output-contract.md) and [estimate rules](references/estimating-and-boundaries.md). Provide alternatives, proposed MVP, fit-gap, ownership, estimate readiness, quantified effort *only when credible*, risks, exclusions and decision gates. Include a one-line `NON-BINDING / NOT FOR CONTRACTING` disclaimer on any numeric ROM.

## Edge cases

- If the discovery record is missing, create a **discovery request**, not imaginary findings.
- If site/PLC mapping is unknown, segregate connectivity as a partner workstream with its own estimate gate.
- If client asks for a fixed price prematurely, explain what must be verified and offer a paid discovery stage.
- If safety or regulated processes are involved, route for competent domain review and separate validation obligations.
- A deliberately narrow MVP is not permission to bury the full-scope TCO or lifetime support obligations.

Use the smallest useful deliverable, but never make commercial uncertainty disappear through brevity.
