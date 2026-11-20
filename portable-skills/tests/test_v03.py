"""v0.3 methodology-specific regression checks; authored fixtures, not blind AI eval."""
import json,re,sys,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
from temporal_replay import run as temporal
from rom_lineage import run as lineage, audit
from policy_variants import load as policy_load, approve

class V03Tests(unittest.TestCase):
 def test_metadata_and_reference_integrity(self):
  for name in ('ot-discovery','solution-architecture-rom'):
   path=ROOT/'skills'/name/'SKILL.md';doc=path.read_text(encoding='utf-8')
   self.assertTrue(doc.startswith('---\n'))
   front=doc.split('---',2)[1]
   self.assertIn('version: "0.3.0"',front)
   desc=next(x.split('description: ',1)[1] for x in front.splitlines() if x.startswith('description: '))
   self.assertTrue(desc.startswith('"') and desc.endswith('"'))
   self.assertIsInstance(json.loads(desc),str)
   for href in re.findall(r'\]\((references/[^)]+)\)',doc):self.assertTrue((path.parent/href).is_file(),href)
   self.assertLess(len(doc.splitlines()),500)
  try:import yaml
  except ImportError:pass
  else:
   for name in ('ot-discovery','solution-architecture-rom'):
    raw=(ROOT/'skills'/name/'SKILL.md').read_text(encoding='utf8')
    self.assertEqual(yaml.safe_load(raw.split('---',2)[1])['metadata']['version'],'0.3.0')
 def test_resource_clock_sensitivities(self):
  r=temporal()
  self.assertEqual({k:v['finish'] for k,v in r.items()},{'BASE':52,'B-LATE':62,'C-NORM':60})
  self.assertEqual(r['B-LATE']['resource_wait'],10)
  self.assertEqual(r['B-LATE']['jobs'][2]['job_ready_before_resource'],11)
  self.assertEqual(r['BASE']['jobs'][2]['job_ready_before_resource'],1)
  self.assertEqual(r['C-NORM']['jobs'][2]['finish'],60)
  self.assertTrue(all(x['execution_status']=='EXECUTED' for x in r.values()))
  self.assertNotEqual(r['B-LATE']['resource_wait'],r['B-LATE']['job_ready_before_resource'])
 def test_rom_gross_net_comparability(self):
  r=lineage();a,b=r['revisions']
  self.assertEqual((a['gross_low'],a['gross_high']),(21,33))
  self.assertEqual((b['gross_low'],b['gross_high']),(27,44))
  self.assertEqual(b['supplier_collisions'],[{'canonical':'APP-UAT','acceptance':'AC-APP-UAT'}])
  self.assertEqual(r['comparison'],'NOT COMPARABLE')
  self.assertIsNone(r['net_change_days'])
  self.assertEqual(b['net_status'],'NET UNRESOLVED')
 def test_same_title_different_acceptance_is_not_proven_overlap(self):
  f=json.loads((ROOT/'experiments/fixtures-v03/lineage.json').read_text())
  f['revisions'][1]['items'][3]['acceptance']='AC-VENDOR-CONFORMANCE'
  audited=audit(f)
  self.assertEqual(audited['revisions'][1]['supplier_collisions'],[])
  self.assertEqual(audited['comparison'],'NOT COMPARABLE')  # scope still expanded
  self.assertIsNone(audited['net_change_days'])
 def test_comparable_revision_needs_explicit_scope_and_owner_evidence(self):
  f=json.loads((ROOT/'experiments/fixtures-v03/lineage.json').read_text())
  # Matching work-package names are insufficient without an external equivalence record.
  f['revisions'][1]['items']=json.loads(json.dumps(f['revisions'][0]['items']))
  f['revisions'][1]['boundary']=f['revisions'][0]['boundary']
  f['revisions'][1]['items'][0]['high']+=2
  self.assertEqual(audit(f)['comparison'],'NOT COMPARABLE')
  f['equivalence_record']='SYNTHETIC-EXTERNAL-EQUIVALENCE-01'
  comparison=audit(f)
  self.assertEqual(comparison['comparison'],'COMPARABLE FOR HUMAN REVIEW')
  self.assertEqual(comparison['net_change_days'],[0,2])
  f['revisions'][1]['items'][1]['supplier']='Other supplier'
  self.assertEqual(audit(f)['comparison'],'NOT COMPARABLE')
 def test_rom_lineage_fails_invalid_or_conflated_scope(self):
  f=json.loads((ROOT/'experiments/fixtures-v03/lineage.json').read_text())
  f['revisions'][1]['items'][1]['low']=-1
  with self.assertRaises(ValueError):audit(f)
  f['revisions'][1]['items'][1]['low']=5
  f['revisions'][1]['items'][3]['canonical']='APP-WORKFLOW';f['revisions'][1]['items'][3]['acceptance']='AC-WORKFLOW'
  a=audit(f)
  self.assertEqual(a['comparison'],'NOT COMPARABLE')
  self.assertIsNone(a['net_change_days'])
 def test_policy_variants_negative_cases(self):
  f=policy_load();normal={'role':'qa-reviewer','actor':'reviewer-B','requestor':'worker-A'}
  self.assertEqual(approve(f,'P-A',completed_checks=[],**normal),'APP_POLICY_ALLOW_PENDING_EXTERNAL_APPROVAL')
  self.assertEqual(approve(f,'P-B',completed_checks=[True]*6,**normal),'APP_POLICY_ALLOW_PENDING_EXTERNAL_APPROVAL')
  self.assertEqual(approve(f,'P-B',completed_checks=[True]*5,**normal),'REJECT_CHECKS')
  self.assertEqual(approve(f,'P-B',completed_checks=[True]*5+[False],**normal),'REJECT_CHECKS')
  self.assertEqual(approve(f,'P-B',completed_checks=[True]*6,active_hold=True,**normal),'REJECT_ACTIVE_HOLD')
  self.assertEqual(approve(f,'P-B',completed_checks=[True]*6,already_approved=True,**normal),'REJECT_DUPLICATE')
  self.assertEqual(approve(f,'P-B',completed_checks=[True]*6,role='operator',actor='reviewer-B',requestor='worker-A'),'REJECT_WRONG_ROLE')
  self.assertEqual(approve(f,'P-B',completed_checks=[True]*6,role='qa-reviewer',actor='worker-A',requestor='worker-A'),'REJECT_SELF_APPROVAL')
 def test_no_private_case_in_public_v03(self):
  newpaths=[*ROOT.glob('experiments/fixtures-v03/*'),*ROOT.glob('skills/*/references/*')]
  for p in newpaths:
   if p.is_file():
    text=p.read_text(encoding='utf8').lower()
    for marker in ('real customer transcript','private customer quote','confidential internal rom','actual plc address','secret access token'):
     self.assertNotIn(marker,text,p.name)

if __name__=='__main__':unittest.main(verbosity=2)
