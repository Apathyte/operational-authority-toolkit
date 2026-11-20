#!/usr/bin/env python3
"""v0.2 portable package acceptance. Runs fully offline with Python stdlib."""
import copy,json,re,unittest
from pathlib import Path
from grade import check,ROOT,load
class SkillsV02(unittest.TestCase):
 def files(self,case):
  return ROOT/'experiments/outputs-v02'/f'case-{case}.discovery.json',ROOT/'experiments/outputs-v02'/f'case-{case}.rom.json'
 def test_entrypoints_and_linked_refs(self):
  for name in ('ot-discovery','solution-architecture-rom'):
   f=ROOT/'skills'/name/'SKILL.md';t=f.read_text(encoding='utf-8')
   self.assertTrue(t.startswith('---\n'));self.assertIn(f'name: {name}',t);self.assertIn('version: "0.2.0"',t)
   self.assertIn('license: CC0-1.0',t);self.assertLess(len(t.splitlines()),500)
   # Description is a JSON double-quoted string, valid as a YAML scalar.
   # This protects against the easily missed unquoted ': ' YAML mapping error.
   frontmatter=t.split('---',2)[1].strip()
   desc=next((line[len('description: '):] for line in frontmatter.splitlines() if line.startswith('description: ')),None)
   self.assertIsNotNone(desc)
   self.assertTrue(desc.startswith('"') and desc.endswith('"'),f'{name}: quote the description scalar')
   self.assertIsInstance(json.loads(desc),str)
   # When PyYAML is available, verify parsing using a real YAML loader.
   try: import yaml
   except ImportError: pass
   else:
    parsed=yaml.safe_load(frontmatter)
    self.assertEqual(parsed['name'],name)
    self.assertEqual(parsed['metadata']['version'],'0.2.0')
   for href in re.findall(r'\]\((references/[^)]+)\)',t):self.assertTrue((f.parent/href).is_file(),href)
 def test_worked_cases(self):
  for case in 'abc':
   d,r=self.files(case)
   self.assertEqual(check(case,d,r),[],f'{case}: {check(case,d,r)}')
 def test_mutations_rejected(self):
  # Mutations operate in-memory then use the same checked oracle via temporary JSON files.
  from tempfile import TemporaryDirectory
  for case in 'abc':
   dpath,rpath=self.files(case);d=load(dpath);r=load(rpath)
   with TemporaryDirectory() as temp:
    def run(bad_d,bad_r):
     dp=Path(temp)/'d.json';rp=Path(temp)/'r.json';dp.write_text(json.dumps(bad_d));rp.write_text(json.dumps(bad_r))
     return check(case,dp,rp)
    m=copy.deepcopy(d);m['claims'][0]['source_ids']=['INVENTED-EVIDENCE'];self.assertTrue(run(m,r),'invented evidence accepted')
    m=copy.deepcopy(r);m['approval']='APPROVED';self.assertTrue(run(d,m),'self approval accepted')
    m=copy.deepcopy(r);b=next(p for p in m['work_packages'] if p['estimate_status']=='BLOCKED');b['low_days']=0;self.assertTrue(run(d,m),'fake zero estimate accepted')
  da,ra=self.files('a');d=load(da);r=load(ra)
  with TemporaryDirectory() as temp:
   d['unknowns'][0]['does_not_block']=[]
   (Path(temp)/'d.json').write_text(json.dumps(d));(Path(temp)/'r.json').write_text(json.dumps(r))
   self.assertTrue(check('a',Path(temp)/'d.json',Path(temp)/'r.json'),'overblocking accepted')
  dc,rc=self.files('c');d=load(dc);r=load(rc)
  with TemporaryDirectory() as temp:
   r['rollout']['site_classes'][2]['class']='T0'
   (Path(temp)/'d.json').write_text(json.dumps(d));(Path(temp)/'r.json').write_text(json.dumps(r))
   self.assertTrue(check('c',Path(temp)/'d.json',Path(temp)/'r.json'),'copy paste site accepted')
 def test_public_safety_surface(self):
  alltext='\n'.join(p.read_text().lower() for p in ROOT.rglob('*') if p.is_file() and p.suffix in ('.md','.json'))
  for forbidden in ('password =', 'api_key =', 'secret_token =', 'real customer transcript'):
   self.assertNotIn(forbidden,alltext)
  for case in 'abc':self.assertTrue(load(ROOT/'experiments/fixtures-v02'/f'case-{case}.json')['synthetic'])
if __name__=='__main__':unittest.main(verbosity=2)
