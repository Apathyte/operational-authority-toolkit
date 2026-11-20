#!/usr/bin/env python3
"""Synthetic ROM version and supplier collision audit; gross is not reconciled net."""
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[1]

def audit(f):
    if not f.get('synthetic'):raise ValueError('Only synthetic fixtures permitted')
    revisions=[]
    for r in f['revisions']:
        items=r['items']
        if not all(0<=i['low']<=i['high'] for i in items):raise ValueError('invalid estimate range')
        collisions={}
        for i in items: collisions.setdefault((i['canonical'],i['acceptance']),set()).add(i['supplier'])
        duplicates=[{'canonical':k[0],'acceptance':k[1]} for k,v in collisions.items() if len(v)>1]
        revisions.append({'id':r['id'],'boundary':r['boundary'],
                          'gross_low':sum(i['low'] for i in items),'gross_high':sum(i['high'] for i in items),
                          'deliverables':sorted({(i['canonical'],i['acceptance']) for i in items}),
                          'supplier_boundaries':sorted({(i['canonical'],i['acceptance'],i['supplier']) for i in items}),
                          'supplier_collisions':duplicates,
                          'net_status':'NET UNRESOLVED' if duplicates else 'GROSS ONLY / NOT CONTRACTED'})
    a,b=revisions
    same_scope=(a['boundary']==b['boundary'] and a['deliverables']==b['deliverables']
                and a['supplier_boundaries']==b['supplier_boundaries']
                and not a['supplier_collisions'] and not b['supplier_collisions']
                and bool(f.get('equivalence_record')))
    return {'revisions':revisions,'comparison':'COMPARABLE FOR HUMAN REVIEW' if same_scope else 'NOT COMPARABLE',
            'net_change_days':None if not same_scope else [b['gross_low']-a['gross_low'],b['gross_high']-a['gross_high']],
            'approval':'NOT GRANTED','execution_status':'EXECUTED / SYNTHETIC'}

def run(path=None):
    p=Path(path) if path else ROOT/'experiments/fixtures-v03/lineage.json'
    return audit(json.loads(p.read_text(encoding='utf8')))
if __name__=='__main__':print(json.dumps(run(),indent=2))
