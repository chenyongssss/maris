"""Check local demonstration integrity; no AI performance claims."""
from pathlib import Path
import json
import subprocess
import sys
import unittest

ROOT=Path(__file__).resolve().parents[1]
DEMOS=ROOT/'demos'

class DemoTests(unittest.TestCase):
    def run_script(self,*args):
        p=subprocess.run([sys.executable,*map(str,args)],capture_output=True,text=True,timeout=15)
        self.assertEqual(p.returncode,0,msg=p.stdout+'\n'+p.stderr)
        return p.stdout

    def test_all_three_verifiers(self):
        result=self.run_script(DEMOS/'run.py','--verify')
        self.assertIn('3 local case checkers passed',result)
        self.assertIn('exact rational Poisson',result)

    def test_exact_poisson_rational_counterexample(self):
        result=json.loads(self.run_script(DEMOS/'02-research'/'evidence'/'poisson_checker.py'))
        self.assertEqual(result['status'],'PASS')
        self.assertEqual(result['off_sensor_point']['u1_minus_u0'],'-1/16')
        self.assertTrue(all(x['u0']==x['u1'] for x in result['sensors']))

    def test_decision_profile_sensitivity(self):
        result=json.loads(self.run_script(DEMOS/'03-decision'/'evidence'/'score_options.py','--scenario','all'))
        self.assertEqual(result['pde']['ranking'][0]['option'],'fmi')
        self.assertEqual(result['eda']['ranking'][0]['option'],'eda')
        self.assertEqual(result['neutral']['ranking'][0]['option'],'fmi')

    def test_demos_have_three_mode_references(self):
        for case in ('01-coding','02-research','03-decision'):
            for f in ('README.md','task.md','baseline.md','cold-start.md','personalized.md'):
                with self.subTest(case=case,file=f):
                    self.assertTrue((DEMOS/case/f).is_file())

    def test_public_demo_profiles_are_fixtures(self):
        paths=list(DEMOS.glob('*/profile*.json'))
        self.assertGreaterEqual(len(paths),4)
        for p in paths:
            data=json.loads(p.read_text(encoding='utf-8'))
            self.assertIs(data.get('fixture'),True)
            self.assertIs(data.get('actual_user_history_used'),False)

    def test_reference_output_is_disclosed_as_curated(self):
        output=self.run_script(DEMOS/'run.py','--case','coding','--mode','personalized')
        self.assertIn('CURATED REFERENCE, NOT MODEL OUTPUT',output)
        self.assertIn('hypothetical',output.lower())

    def test_readmes_link_all_demos(self):
        en=(ROOT/'README.md').read_text(encoding='utf-8')
        zh=(ROOT/'README.zh-CN.md').read_text(encoding='utf-8')
        for case in ('01-coding','02-research','03-decision'):
            self.assertIn(f'demos/{case}/README.md',en)
            self.assertIn(f'demos/{case}/README.md',zh)

if __name__=='__main__': unittest.main()
