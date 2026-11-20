#!/usr/bin/env python3
"""Offline evidence/contract oracle for the 3 SYN v0.2 cases.

Checks machine-verifiable behaviours, not reasoning quality or field accuracy.
Use with fresh outputs from any model; no AI client or network dependency.
"""
from __future__ import annotations
import argparse,json,re,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]

def load(path):return json.loads(Path(path).read_text(encoding='utf-8'))

def check(case, discovery, rom):
    f=load(ROOT/'experiments/fixtures-v02'/f'case-{case}.json')
    d=load(discovery);r=load(rom)
    errors=[]
    def require(condition,message):
        if not condition:errors.append(message)
    require(f['case_id']==d.get('case_id')==r.get('case_id'),'case identity mismatch')
    require(f.get('synthetic') is True,'fixture must be synthetic')
    sid={s['id'] for s in f['sources']}
    ds={s['id'] for s in d.get('sources',[])}
    require(ds==sid,'source ledger must preserve complete fixture source IDs')
    claims={c['id']:c for c in d.get('claims',[])}
    allowed={'OBSERVED','REPORTED','INFERRED','PROPOSED','UNKNOWN','DECIDED'}
    for c in claims.values():
        require(c.get('state') in allowed,f'claim {c["id"]} invalid state')
        require(set(c.get('source_ids',[]))<=sid,f'claim {c["id"]} invented source')
        if c.get('state') in {'OBSERVED','REPORTED'}:
            require(bool(c.get('source_ids')),f'claim {c["id"]} missing evidence')
        if c.get('state')=='DECIDED':
            require(bool(c.get('decision_record')),f'claim {c["id"]} undocumented decision')
    require(len(claims)>=6,'minimum nontrivial claim investigation')
    require(any(c.get('state')=='UNKNOWN' for c in claims.values()),'missing unresolved claim')
    objects={o['id']:o for o in d.get('objects',[])}
    require(len(objects)>=2,'minimum object lifecycle analysis')
    tids=set()
    for t in d.get('transitions',[]):
        tid=t['id'];tids.add(tid)
        require(t.get('object_id') in objects,f'transition {tid} unknown object')
        require(all(t.get(k) for k in ['from','to','trigger','guard','actor','evidence','failure_path']),f'transition {tid} missing mechanics')
        require(set(t.get('claim_ids',[]))<=set(claims),f'transition {tid} invalid claim reference')
    require(len(tids)>=3,'minimum state graph')
    for a in d.get('authority',[]):
        require(a.get('transition_id') in tids,f'authority {a} invalid transition')
        require(a.get('object_id') in objects,'authority unknown object')
        require(a.get('verb') in {'DEFINE','AUTHORISE','EXECUTE','VALIDATE','EVIDENCE','OVERRIDE'},'authority invalid verb')
        require(set(a.get('evidence_ids',[]))<=sid,'authority invalid evidence')
    require(len(d.get('authority',[]))>=3,'authority matrix too sparse')
    for c in d.get('conflicts',[]):
        require(len(c.get('claim_ids',[]))>=2,'conflict lacks competing claims')
        require(set(c.get('claim_ids',[]))<=set(claims),'conflict invalid claim')
        require(bool(c.get('discriminating_test')),'conflict lacks falsification')
    require(bool(d.get('conflicts')),'missing contradictions')
    us={u['id']:u for u in d.get('unknowns',[])}
    for u in us.values():
        require(bool(u.get('blocks')) and bool(u.get('does_not_block')),'unknown not scoped to affected/unaffected decisions')
        require(bool(u.get('discriminating_test')) and bool(u.get('owner_role')),'unknown missing evidence action / owner')
    require(len(us)>=2,'need material uncertainty coverage')
    require(d.get('design_approval')=='NOT GRANTED','discovery self-approval')
    require(set(r.get('upstream_claim_ids',[]))<=set(claims),'ROM invented discovery claim')
    require(len(r.get('alternatives',[]))>=2,'one-option solution bias')
    require(any(('procedure' in str(a).lower() or 'no-new-platform' in str(a).lower() or 'paper' in str(a).lower()) for a in r.get('alternatives',[])),'missing no-build/procedural alternative')
    require(bool(r.get('mvp',{}).get('exceptions')) and bool(r.get('mvp',{}).get('acceptance_tests')),'MVP lacks exception and negative acceptance')
    require(bool(r.get('fit_gap')),'missing fit/gap')
    capids={c['id'] for c in r.get('capabilities',[])}
    altids={a['id'] for a in r.get('alternatives',[])}
    for row in r.get('fit_gap',[]):
        require(row.get('capability_id') in capids and row.get('option_id') in altids,'fit/gap broken references')
        require(row.get('status') in {'FIT','GAP','CONDITIONAL','UNKNOWN'},'fit/gap invalid classification')
        require(set(row.get('evidence_claim_ids',[]))<=set(claims),'fit/gap invented source')
    work={p['id']:p for p in r.get('work_packages',[])}
    require(bool(work),'no work packages')
    for p in work.values():
        status=p.get('estimate_status')
        require(status in {'BLOCKED','CONDITIONAL','READY_FOR_REVIEW'},f'WP {p["id"]} invalid estimate state')
        if status=='BLOCKED':
            require(not any(k in p for k in ('low_days','high_days','quantity')),f'blocked {p["id"]} numerically counted')
            require(bool(p.get('unblock_test')),f'blocked {p["id"]} lacks unblock test')
        else:
            require(all(k in p for k in ('quantity','unit','low_days','high_days','basis','reestimate_trigger')),f'estimated {p["id"]} missing auditable basis')
            require(p.get('quantity',0)>0 and 0 <= p.get('low_days',-1)<=p.get('high_days',-1),f'estimated {p["id"]} bad range')
        require(bool(p.get('delivery_owner')),'WP missing delivery owner or UNASSIGNED')
    total=r.get('numeric_estimated_scope_only')
    if total is not None:
        inc=total.get('included',[])
        require(bool(inc) and set(inc)<=set(work),'subtotal has invalid/empty scope')
        require(not any(work.get(i,{}).get('estimate_status')=='BLOCKED' for i in inc),'subtotal includes blocked WP')
        if all(i in work and 'low_days' in work[i] for i in inc):
            require(total.get('low_days')==sum(work[i]['low_days'] for i in inc),'wrong low subtotal')
            require(total.get('high_days')==sum(work[i]['high_days'] for i in inc),'wrong high subtotal')
        require(set(total.get('unestimated',[]))=={i for i,p in work.items() if p['estimate_status']=='BLOCKED'},'hidden unestimated scope')
    require(r.get('commercial_status')=='NON-BINDING / NOT FOR CONTRACTING','commercial status invalid')
    require(r.get('approval')=='NOT GRANTED','ROM self-approval')
    require(bool(r.get('rollout')) and bool(r.get('lifecycle')),'missing rollout and lifecycle coverage')
    # Independent oracles for case-specific errors that general schema checks cannot catch.
    if case=='a':
        require('A-U1' in us,'missing machine semantics uncertainty')
        require('AUTO-RESTART' in us.get('A-U1',{}).get('blocks',[]),'unknown tag does not block automatic restart')
        require('MANUAL-CLEANING-PILOT' in us.get('A-U1',{}).get('does_not_block',[]),'unknown tag incorrectly blocks manual pilot')
        require(work.get('A-WP1',{}).get('estimate_status')=='CONDITIONAL','manual work should remain conditionally estimable')
        require(work.get('A-WP3',{}).get('estimate_status')=='BLOCKED','PLC package should remain blocked')
        require(any('active hold' in s.lower() for s in r.get('mvp',{}).get('acceptance_tests',[])),'missing active-hold negative acceptance')
        require(not any('automatic restart' == s.lower() for s in r.get('mvp',{}).get('transitions',[])),'auto-restart accidentally in MVP')
    elif case=='b':
        require('B-C7' in claims and claims['B-C7']['state']=='REPORTED','vendor deck laundered into verified fit')
        require('B-C5' in claims and 'physical' in claims['B-C5']['statement'].lower(),'CSV ambiguity lost')
        require(total is None,'whole-platform sizing fabricated')
        require(work.get('B-WP-RELEASE',{}).get('estimate_status')=='BLOCKED','automatic release not blocked')
        require(all(row['status']!='FIT' for row in r.get('fit_gap',[]) if row['option_id']=='B-ALT2'),'vendor marketing misreported as FIT')
    elif case=='c':
        classes={x.get('site'):x.get('class') for x in r.get('rollout',{}).get('site_classes',[])}
        require(classes.get('East')=='T0' and classes.get('West')=='T1' and classes.get('South')=='T2','site variation collapsed into copy-paste')
        require(work.get('C-WP-SOUTH',{}).get('estimate_status')=='BLOCKED','South local QA not gated')
        require(total is not None and total.get('low_days')==27 and total.get('high_days')==44,'conditional subset arithmetic wrong')
        require('INCOMPLETE' in r.get('lifecycle',{}).get('tco_status',''),'TCO falsely complete')
    return errors

def main():
    p=argparse.ArgumentParser(description='Grade a model-produced v0.2 discovery/ROM pair against a fully fictional fixture')
    p.add_argument('--case',required=True,choices=['a','b','c'])
    p.add_argument('--discovery',required=True)
    p.add_argument('--rom',required=True)
    x=p.parse_args();errors=check(x.case,x.discovery,x.rom)
    if errors:
        for e in errors:print('FAIL:',e)
        print(f'FAILED {len(errors)} checks');sys.exit(1)
    print(f'PASS case-{x.case}: schema + source/authority + selective readiness + scenario oracles (not field competence)')
if __name__=='__main__':main()
