# Auditable ROM estimation and lifecycle economics

The estimator is a **conditional planning instrument**, not a calculator that turns a few nouns into engineering days. Never produce industry rates or benchmarks from this file. Effort must come from supplied benchmarks, measured historical data approved for reuse, or explicitly stated synthetic planning assumptions.

## Stage 0 — unit of estimation

Work breakdown by separately deliverable and owned work package (WP). At minimum distinguish product configuration, custom workflow, machine connectivity/semantics, enterprise integration, verification/validation, deployment/training, and support. Each WP carries:

`id`, `quantity`, `unit`, `source`, `complexity driver`, `interfaces`, `depends_on`, `owner`, `estimate_status`, `low`, `high`, `basis`, `exclusions`, `unblock_test`, `reestimate_trigger`.

States:
- `BLOCKED`: critical quantity/meaning/access/authority unknown, no defensible numerical basis. Provide effort drivers and a discovery experiment, **not zero**.
- `CONDITIONAL`: bounded known/assumed units, named dependencies, auditable range; attach sensitivity.
- `READY_FOR_REVIEW`: enough observed/authorised inputs and discipline estimates for human technical/commercial review. Still **not contracted**.

Blocking one WP **must not** force all other independent WPs into `BLOCKED`. Represent dependency graph explicitly. If package B relies on blocked A to function, B is `CONDITIONAL_PENDING_A` or blocked, not silently unaffected; a manual substitute may decouple it if credible.

## Stage 1 — bottom-up ranges

For each bounded WP, calculate from explicit components: `quantity × low effort per unit + fixed low` to `quantity × high effort per unit + fixed high`, with unit assumptions recorded. Example *synthetic arithmetic only*: 3 screens × (2–3 days) + 1 exception flow × (4–6 days) = **10–15 engineering-days**; no claim that these productivity rates are real. Record whether specification, review, test and rework are included. Never layer arbitrary percentage contingency on top of correlated high-case ranges without disclosing overlap.

- Sum only the WPs actually estimated. Label total `ESTIMATED-SCOPE ONLY`; list excluded/unestimated WPs alongside it.
- Third-party costs cannot be silently treated as SI engineering effort. Licences, cloud, hardware, travel, integration partners and 24/7 services are separate unknown/known lines.
- A range is conditional on both the workload and the *contractual ownership*. `No risk-eating`: unowned interfaces are not assumed to be delivered at the SI's cost.

## Stage 2 — sensitivity and correlated risk

Describe dominant drivers, what would change the bound, and common-cause correlations (e.g., bad machine identity affects tagging, event mapping, test and support). A scenario view (`BASE`, `HARDER`, `SCOPE-REDUCED`) is often more honest than pretending independent probabilities can be multiplied. Do not present confidence percentages without empirical calibration. If essential validity fails, withdraw the numeric scope rather than adding an arbitrary buffer.

## Stage 3 — first factory and rollout

Separate `first_site = reference build + site-specific adapter + commissioning + enablement`; `subsequent_site = template validation + site adaptation + requalification + training + deployment`. **Do not multiply full first-site engineering by the number of sites by default.** Equally, do not assume subsequent sites are cheap clones without inspecting variation.

Classify candidate sites:
- `T0` same workflow, validated interfaces, similar master data (parameterise).
- `T1` same workflow, different machine adapter or ERP mapping (local engineering).
- `T2` process/authority divergence requiring design/revalidation (not a simple rollout).

No per-site numeric estimate without a documented site mix and real or explicitly declared planning basis. Commercial scenarios should include what percentage of sites can reuse the template **only if backed by a survey or clearly labelled hypothetical scenario**, not a fact.

## Stage 4 — TCO / lifecycle

Use a horizon explicitly requested or declared (e.g., hypothetical three years), and show assumptions:

`TCO = initial product/licence + first build + integration + rollout + annual subscriptions/hosting + support + upgrades/revalidation + site operating effort + change requests + exit/migration (if material)`.

Identify costs not priced; an incomplete TCO is a **coverage map**, not a numeric total. The status of first-site ROM and whole-estate TCO can differ. Distinguish pilot success from scalable operating model. Show ownership of second-year maintenance and escalating support expectations.

## Decision rule for commercially viable MVP

A narrow MVP must provide an observable benefit, bounded acceptance, and explicit non-MVP obligations. The next increment is a fresh decision gate. Do not suggest commercial approval, rates, margin, or guaranteed benefits from synthetic quantities.
