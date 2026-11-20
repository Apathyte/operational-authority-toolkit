#!/usr/bin/env python3
"""Pure deterministic scheduling arithmetic for synthetic finite-resource fixtures.
No OT or customer access; not a solver for general shift scheduling.
"""
from __future__ import annotations
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[1]

def replay(fixture,scenario):
    ready_delta=scenario.get('ready_delta',{})
    duration_delta=scenario.get('duration_delta',{})
    prior_finish=0
    result=[]
    for item in fixture['sequence']:
        arrival=prior_finish+item['travel_from_previous'] if result else item['travel_from_previous']
        ready=item['ready']+ready_delta.get(item['id'],0)
        start=max(arrival,ready)
        finish=start+item['duration']+duration_delta.get(item['id'],0)
        result.append({'id':item['id'],'arrival':arrival,'ready':ready,'start':start,'finish':finish,
                       'resource_wait':max(0,ready-arrival),'job_ready_before_resource':max(0,arrival-ready)})
        prior_finish=finish
    return {'scenario':scenario['id'],'finish':prior_finish,'resource_wait':sum(x['resource_wait'] for x in result),
            'job_ready_before_resource':sum(x['job_ready_before_resource'] for x in result),'jobs':result,
            'execution_status':'EXECUTED','domain':'SYNTHETIC OFFLINE'}

def run(path=None):
    path=Path(path) if path else ROOT/'experiments/fixtures-v03/temporal.json'
    fixture=json.loads(path.read_text(encoding='utf8'))
    if not fixture.get('synthetic'): raise ValueError('Only synthetic fixtures permitted')
    return {x['id']:replay(fixture,x) for x in fixture['scenarios']}

if __name__=='__main__': print(json.dumps(run(),indent=2))
