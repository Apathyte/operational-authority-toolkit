#!/usr/bin/env python3
"""Offline app-policy negative tests. Not a safety controller or equipment permission."""
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[1]

def approve(f,policy_id,*,role,actor,requestor,completed_checks,active_hold=False,already_approved=False):
    p=next(x for x in f['policies'] if x['id']==policy_id)
    if role!=f['approved_role']: return 'REJECT_WRONG_ROLE'
    if actor==requestor: return 'REJECT_SELF_APPROVAL'
    if active_hold:return 'REJECT_ACTIVE_HOLD'
    if already_approved:return 'REJECT_DUPLICATE'
    if len(completed_checks)!=p['required_checks'] or not all(completed_checks):return 'REJECT_CHECKS'
    return 'APP_POLICY_ALLOW_PENDING_EXTERNAL_APPROVAL'

def load(path=None):
    p=Path(path) if path else ROOT/'experiments/fixtures-v03/policies.json'
    f=json.loads(p.read_text(encoding='utf-8'))
    if not f.get('synthetic'):raise ValueError('synthetic fixtures only')
    return f
