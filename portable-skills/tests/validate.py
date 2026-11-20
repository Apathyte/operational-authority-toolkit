#!/usr/bin/env python3
"""Portable, stdlib-only structural/contract checks. Not a model reliability test."""
from pathlib import Path
import json,re,unittest
ROOT=Path(__file__).resolve().parents[1]
class ContractTests(unittest.TestCase):
    def load(self, name):return json.loads((ROOT/'experiments'/name).read_text())
    def test_agent_skills_metadata(self):
        for skill in ('ot-discovery','solution-architecture-rom'):
            doc=(ROOT/'skills'/skill/'SKILL.md').read_text()
            self.assertTrue(doc.startswith('---\n'))
            fm=doc.split('---',2)[1]
            match=re.search(r'(?m)^name: ([a-z0-9-]+)$',fm)
            self.assertIsNotNone(match)
            self.assertEqual(match.group(1),skill)
            self.assertFalse('--' in skill or len(skill)>64)
            desc=re.search(r'(?m)^description: (.+)$',fm)
            self.assertTrue(desc and 1<=len(desc.group(1))<=1024)
            self.assertIn('license: CC0-1.0',fm)
            self.assertLess(len(doc.splitlines()),500)
    def test_outputs_trace_sources_and_preserve_unknowns(self):
        for c in 'ab':
            f=self.load(f'fixtures/case-{c}.json')
            d=self.load(f'outputs/case-{c}.discovery.json')
            r=self.load(f'outputs/case-{c}.rom.json')
            self.assertEqual(f['case_id'],d['case_id'])
            self.assertEqual(f['case_id'],r['case_id'])
            ev={e['id'] for e in f['evidence']}
            self.assertEqual(set(d['evidence_ids']),ev)
            claim={x['id']:x for x in d['claims']}
            self.assertTrue(any(x['status']=='UNKNOWN' for x in d['claims']))
            for x in d['claims']:
                self.assertIn(x['status'],{'FACT','INFERENCE','ASSUMPTION','UNKNOWN'})
                self.assertTrue(set(x['evidence_ids'])<=ev)
                if x['status']=='FACT':self.assertGreater(len(x['evidence_ids']),0)
            self.assertTrue(set(r['source_claim_ids'])<=set(claim))
            for x in r['fit_gap']:self.assertIn(x['source_claim_id'],claim)
            uids={u['id'] for u in d['unknowns']}
            self.assertTrue(set(r['external_dependencies'])<=uids)
            self.assertNotEqual(d['design_gate'],'APPROVED')
            self.assertEqual(r['commercial_status'],'NON-BINDING / NOT FOR CONTRACTING')
            self.assertTrue(r['alternatives'] and r['decision_gates'] and r['mvp']['exclusions'])
    def test_rom_readiness_and_arithmetic(self):
        a=self.load('outputs/case-a.rom.json');b=self.load('outputs/case-b.rom.json')
        self.assertEqual(a['estimate_status'],'ROM BLOCKED')
        self.assertNotIn('rom_total',a)
        self.assertEqual(b['estimate_status'],'CONDITIONAL ROM')
        self.assertEqual(sum(x['low_days'] for x in b['workstreams']),b['rom_total']['low_days'])
        self.assertEqual(sum(x['high_days'] for x in b['workstreams']),b['rom_total']['high_days'])
        self.assertTrue(all(x['low_days']<=x['high_days'] for x in b['workstreams']))
        self.assertIn('Fictional',b['estimate_basis'])
    def test_synthetic_and_no_case_bleed(self):
        a=''.join((ROOT/'experiments'/'outputs'/p).read_text() for p in ['case-a.discovery.json','case-a.rom.json'])
        b=''.join((ROOT/'experiments'/'outputs'/p).read_text() for p in ['case-b.discovery.json','case-b.rom.json'])
        self.assertNotIn('B-E1',a);self.assertNotIn('A-E1',b)
        for p in (ROOT/'skills').rglob('*'):
            if p.is_file():
                v=p.read_text().lower()
                for forbidden in ('avebe','excluton','fujifilm','winclove','ats global'):
                    self.assertNotIn(forbidden,v)
    def test_no_auto_execution_claims(self):
        discovery=(ROOT/'skills/ot-discovery/SKILL.md').read_text().lower()
        rom=(ROOT/'skills/solution-architecture-rom/SKILL.md').read_text().lower()
        self.assertIn('do not',discovery)
        self.assertIn('rom blocked',rom)
        self.assertIn('non-binding',rom)
if __name__=='__main__':unittest.main(verbosity=2)
