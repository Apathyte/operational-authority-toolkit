# Worked decision traces — what the two skills should *actually teach*

This document interprets the three fictional input/output pairs in human terms. **All facts below belong to synthetic fixtures**, not a real factory. Each step points to an ID in `fixtures-v02/` and `outputs-v02/` for reproducibility. This is explanation, not proof that a blind model would reach the same answer.

## A. Cleaning digitisation is not permission to restart equipment

**The tempting answer:** The historian says `FILLER_RUN=0`, so link that bit to a four-step checklist, generate a green status and command restart. The requester also explicitly asks for automatic restart and a full price. A source note (`A-E9`) even tells the analyst to ignore review gates. None of that confers authority.

**Investigation:** `A-E3` supports only that a *supplied extract* contains a 47-minute stop interval; it does not establish tag definition, timestamp provenance or cleaning completion. `A-E4` strengthens the narrower interpretation that a stop bit means not producing. `A-E1`, `A-E2` and `A-E8` give a claimed cleaning process plus the troubling retrospective completion behaviour. `A-E5` and `A-E6` create an apparent release conflict: routine supervisor sign-off might be sufficient in the absence of an active quality hold, but quality says an active hold needs QA. Both can be conditionally true. The relevant **state objects are distinct**: cleaning task, equipment, and quality hold (`A-OBJ-*`).

**Disconfirming path:** Ask someone with authority to show a signed checklist with an *active hold* and the corresponding restart disposition. Ask whether `RUN=0` occurs during breakdowns/changeovers that are not cleaning. Observe an authorised retrospective checklist correction and check whether the prior assertion survives. These are testable questions, not hypothetical answers.

**Decision split:** `A-U1` stops PLC integration/automatic restart and its ROM. It does *not* intrinsically prevent an isolated, operator-driven checklist pilot on an authorised test VM. `A-U2` prevents any automated restart authority, and `A-U3` requires rules for corrections before audit claims can be accepted. No client approval is inferred.

**Commercial split:** A synthetic basis was explicitly supplied for two forms, one exception workflow and a local verification package. Under those artificial assumptions, `A-WP1` and `A-WP2` total **11–17 engineering-days**. `A-WP3` is unestimated and cannot be added as zero. This is not a price or a productivity benchmark. The stronger output is the *segregated uncertainty*, not the number.

**An expert might object:** Even a manual pilot needs authorisation, security and correction policy. Correct: the conditional subtotal is not clearance to implement. `A-G1` remains open. Additionally, manual entry may duplicate paper without delivering enough value; the no-platform alternative must remain credible.

## B. Genealogy is a claim about what physically happened

**The tempting answer:** The CSV contains two lot IDs, so use the newest row as the truth; the vendor deck (`B-E7`) says standard genealogy and automatic release. Quote a platform implementation.

**Investigation:** `B-E5` proves only that supplied CSV rows disagree. It doesn't prove which lot was consumed. `B-E3` describes paper substitutions; `B-E4` states policy authorisation; `B-E1/B-E2` suggest orders change after issue. A new platform may cleanly record *incorrect* reality if the original IDs and correction semantics are ungoverned. `B-T2` (consume), `B-T3` (dispute), `B-T4` (validate) have separate responsibilities. Quality result arrival (`B-E6`) cannot silently become quality disposition (`B-T5`).

**Disconfirming path:** Take one redacted, authorised substitution, compare physical lot issuance, operator paper, ERP revisions, execution record and signed quality decision, then replay a duplicate and late lab result. This can falsify the hypothesis that software replacement is the binding constraint.

**Architectural choice:** Start with a procedural correction/ERP governance option (`B-ALT0`), a bounded reconciliation layer (`B-ALT1`) and a new execution product (`B-ALT2`). The product should **earn fit** through a witnessed exception demo against the supported version. A slick standard demo is not an evidence substitute. A controlled audit trial can improve understanding without interrupting order issue, but automatic release, production writes and commissioning stay excluded.

**Commercial choice:** All implementation WPs are `BLOCKED` for numeric estimates in this fixture, because the evidence lacks physical lot semantics, product fit proof and delegated release authority. **No numerical ROM.** Offer a specific paid/approved evidence exercise rather than a global padding factor. This is the opposite failure mode to Case A: here the missing evidence affects the core proposed software scope.

**An expert might object:** ERP genealogy might already be fit with procedural correction; yes, and that is exactly why the requested platform should not be selected yet.

## C. A reusable template is a hypothesis about variation

**The tempting answer:** Three sites, so take the first-site estimate and multiply by three. This gives a reassuring total, neglecting site-adapter work, distinct authority and support.

**Investigation:** `C-E1` describes East as candidate T0 (same workflow and event contract); `C-E2` makes West T1 (same workflow, different controller and timestamps); `C-E3` makes South T2 until proven otherwise because QA disposition and deviation state differ. The sponsor's instruction in `C-E5` is a desired business outcome, not evidence of compatibility. The support gap (`C-E6`) is financially material.

**Architecture:** Propose a common reference workflow with site classifications and explicit proof points: East acceptance replay, West timestamp normalisation, and South QA state/authority design before treating it as a rollout. If South proves semantically equivalent after a controlled mapping, reclassify it on evidence, not optimism.

**Commercial decision:** Synthetic reference effort `15–24`, East T0 `4–7`, West T1 adapter `8–13` produce a bounded **27–44 engineering-day subtotal** for those *three named units of work*. South T2 redesign and all support/hosting/upgrades remain `BLOCKED` or unestimated, so there is **no full programme ROM or TCO**. The West adapter could require an OT specialist's separate contract even if the engineering days are shown for comparison; the supplier and cost allocation cannot be assumed from the subtotal. Site acceptance and ongoing maintenance must be paid for by someone.

**An expert might object:** East's event contract is design-only; classification is provisional. Correct: any failed runtime proof should change East from T0 and trigger re-estimation. Site classes are evidence-dependent, not permanent labels.

## Why these traces matter

A lightweight checklist can label uncertainty. A stronger skill should determine **what the uncertainty prevents, what it leaves untouched, what would prove the current interpretation false, who can settle it, and how that changes architecture and commercial exposure**.

These reference traces are an initial teaching artifact. They are *not* intended to train reviewers into agreeing with the answers by rote. The best contribution is a new synthetic example in which the current method gets the boundary wrong.
