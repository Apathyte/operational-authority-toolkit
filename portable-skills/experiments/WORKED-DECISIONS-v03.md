# What v0.3 adds — entirely fictional worked mechanisms

**Not a model benchmark.** Three independent synthetic fixtures exercise the new method. They are not derived from, or disguised versions of, any real customer.

## 1. Three packing cells, one mobile QA sampler

A fictional QA sampler serves three cells in a fixed order. The baseline illustrative sampling finishes at 09:52. If Cell B is ready 10 minutes late, the sampler waits 10 minutes; Cell C is already ready when the sampler arrives 11 minutes after Cell C's ready time, and the final finish shifts to 10:02. Those are **different metrics**. If instead the third sample takes eight minutes longer, finish is 10:00. The clock is arbitrary and is not a measured line KPI. `tests/temporal_replay.py` is the deterministic reference.

## 2. Two ROM revisions are not a success story by subtraction

The second fictional scope adds an event contract and a second supplier's UAT line. Gross combined engineering days are **27–44** compared with an earlier **21–33**, but a `APP-UAT` acceptance collision exists and the scope changed. Net supplier effort and numeric improvement are unresolved. The example deliberately avoids a claims-based savings calculation. `tests/rom_lineage.py` computes the gross and flags duplicated acceptance labels for human reconciliation; it does not calculate net.

## 3. Two competing approval points

One candidate application policy requires role separation before an inspection; a second requires six complete checks after inspection. Neither is approved. Wrong-role, self-sign, missing/NOK checks, active hold and duplicate attempts must fail in the offline reference. Test outcomes do not grant an app any physical machine release or safety authority. `tests/policy_variants.py` contains the deterministic negative tests.

## The v0.3 principle

Trigger deeper modelling **only when the causal structure demands it**: shared capacity/time, repeated supplier lines, or disputed decision policy. If the host lacks tools, return equations and `NOT EXECUTED`; never assert tests were executed. Maintain exact provenance and do not overwrite earlier versions to make estimates appear consistent.
