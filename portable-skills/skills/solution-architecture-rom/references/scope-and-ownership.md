# Scope, first-use slice and responsibility graph

## Minimum coherent first-use slice (not minimum screen count)

Describe `actor → trigger → desired state transition → verification → exception → audit → acceptance`. Define boundary by one unit, process path, object population, shift or site. The slice must be meaningful to operations while not claiming deferred dependencies have disappeared.

Example fictional cleaning slice:

- **Within:** plan one machine cleaning, assign five steps, record actual starts/finishes, flag late/overrun, require supervisor confirmation, demonstrate missed/duplicate acknowledgement handling.
- **Out:** automatic machine stop/start, production ERP rescheduling, full maintenance system sync, cross-site deployment, 24/7 support.
- **Indispensable:** accepted meaning of 'complete', operator identity, timestamps, exception owner, right to confirm and audit retention.
- **Acceptance:** demonstrate normal flow, late start, incomplete step, duplicate event and refused unauthorised release; show before/after in audit.

Avoid a narrow MVP that depends silently on the very integration it excluded. If the manual pathway is independently usable, define it separately; if not, classify the package as blocked.

## Responsibility is multidimensional

For each deliverable/integration boundary capture `delivery_owner`, `semantic_owner`, `access_owner`, `verifier`, `acceptance_authority`, `operational_owner`, `support_owner`, `cost_owner`, `status`, `contract/evidence`. They need not be the same. Use `UNASSIGNED` instead of auto-assigning to vendor, SI or customer.

| Boundary | Essential work | Typical questions |
| --- | --- | --- |
| Product | licence, setup, standard configuration, upgrades | what is OOTB vs custom; who owns licence change? |
| Machine | PLC access, equipment identity, tag mapping, timestamps | who is competent/authorised to inspect? |
| Integration | transport, schemas, identity mapping, retry/reconciliation | who signs event meaning and change control? |
| Workflow | screens, tasks, rights, exceptions and audit | who approves state transitions? |
| Enterprise | ERP, LIMS, CMMS, roster, identity | is deferral feasible for MVP? |
| Deployment | environments, backup, release, acceptance, training | who operates at go-live? |
| Service | monitoring, restoration, patching, 24/7, SLAs | what is explicitly excluded vs purchased? |

## Fit/gap decisions and change control

`FIT` requires credible proof under site conditions; `CONDITIONAL` requires owner and evidence; `GAP` requires a mitigation or explicit out-of-scope; `UNKNOWN` requires a targeted experiment. Differentiate native product configuration from extension/custom code, a special integration, and operational change. Classify variation by parameterisation / site adapter / product extension / new design. Do not market every variation as a 'template'.

For every scope line document a scenario, observed/proposed source, acceptance evidence, and decision owner. For each exclusion record whether it is (1) truly unnecessary, (2) deferred future work, (3) third-party work, or (4) a mandatory external dependency. These are economically different.

## Handoff to commerce

- Proposal state is `UNAPPROVED` unless external signed authority exists.
- ROM, fixed quote, license order, release, and support agreement are independent approvals.
- Identify discovery deliverables with fixed *question/evidence* scope rather than pretending full implementation certainty.
- Define change triggers: undocumented machine types, site-specific process differences, source-data quality, interfaces, regulatory review, security, support level.
