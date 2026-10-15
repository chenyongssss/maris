#!/usr/bin/env python3
"""Reproducible MARIS demo runner (standard library only).

'--mode' prints CURATED REFERENCE outputs from real/verified evidence; it does
NOT invoke an LLM, Agent Skills host, or a user's private chat/profile.
'--verify' executes the local exact-math/scoring/integrity checks only.
"""
import argparse
import importlib.util
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
CASES = {'coding': '01-coding', 'research': '02-research', 'decision': '03-decision'}
MODES = {'baseline': 'baseline.md', 'cold': 'cold-start.md', 'personalized': 'personalized.md'}

def load_py(filepath):
    spec = importlib.util.spec_from_file_location(filepath.stem, filepath)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod

def verify_coding() -> str:
    root = HERE / CASES['coding'] / 'evidence'
    source1 = (root/'retention-before.py.txt').read_text(encoding='utf-8')
    source2 = (root/'retention-after.py.txt').read_text(encoding='utf-8')
    prov = json.loads((root/'provenance.json').read_text(encoding='utf-8'))
    assert 'RETENTION_RULES = {"30_days"' in source1
    assert '"retention_rule": retention_rule' in source1
    assert 'record.get("consent") == "approved"' in source1
    assert 'timedelta' not in source1
    assert '"retention_rule") != "30_days"' in source2
    assert 'enforce_history_retention(base)' in source2
    assert 'expired' in source2
    assert prov['before_commit'].startswith('42ab1cb') and prov['after_commit'].startswith('40b487')
    return 'PASS: pinned source-excerpt static integrity (NOT full runtime validation)'

def verify_research() -> str:
    checker = load_py(HERE/CASES['research']/'evidence'/'poisson_checker.py')
    result = checker.run()
    assert result['status'] == 'PASS'
    assert result['off_sensor_point']['u1_minus_u0'] == '-1/16'
    assert result['boundary_point']['u1_minus_u0'] == '1/4'
    return 'PASS: exact rational Poisson equation and counterexample'

def verify_decision() -> str:
    root = HERE/CASES['decision']/'evidence'
    m = load_py(root/'score_options.py')
    results = {name:m.score(name) for name in ('neutral','pde','eda')}
    assert results['pde']['ranking'][0]['option']=='fmi'
    assert results['eda']['ranking'][0]['option']=='eda'
    led=json.loads((root/'source-ledger.json').read_text(encoding='utf-8'))
    ids={x['id'] for x in led['facts']}
    assert len(ids)==len(led['facts']) and len(ids)>=8
    assert all(x['url'].startswith('https://') for x in led['facts'])
    option_data=json.loads((root/'option-scores.json').read_text(encoding='utf-8'))
    assert all(set(o['evidence']).issubset(ids) for o in option_data['options'])
    return 'PASS: transparent heuristic scores and source ledger (NOT empirical feasibility)'

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--case',choices=sorted(CASES),default='coding')
    p.add_argument('--mode',choices=sorted(MODES),default='cold')
    p.add_argument('--verify',action='store_true',help='Run local verifiers for all 3 cases')
    args=p.parse_args()
    if args.verify:
        for label,func in [('coding',verify_coding),('research',verify_research),('decision',verify_decision)]:
            print(f'{label:>9}: {func()}')
        print('VERIFIED: 3 local case checkers passed. No external agent/model/host evaluation was performed.')
        return
    filepath=HERE/CASES[args.case]/MODES[args.mode]
    print(f'=== MARIS {args.case.upper()} | {args.mode.upper()} | CURATED REFERENCE, NOT MODEL OUTPUT ===\n')
    print(filepath.read_text(encoding='utf-8'))

if __name__=='__main__': main()
