#!/usr/bin/env python3
"""Transparent scenario sensitivity for the MARIS decision demo.

The inputs are illustrative judgments; rankings are conditional, not empirical.
No installed engineering simulators are invoked, and no external API is called.
"""
from pathlib import Path
import argparse
import json

HERE = Path(__file__).resolve().parent

def score(scenario: str) -> dict:
    data = json.loads((HERE / 'option-scores.json').read_text(encoding='utf-8'))
    s = next((x for x in data['scenarios'] if x['id'] == scenario), None)
    if s is None:
        raise ValueError('unknown scenario: ' + scenario)
    weights = s['weights']
    assert abs(sum(weights.values())-1) < 1e-10, 'weights must sum to one'
    options = []
    for o in data['options']:
        assert all(1 <= o[k] <= 5 for k in data['features'])
        assert all(k in data['features'] for k in weights)
        options.append({'option':o['id'], 'title':o['name'], 'score':round(sum(o[k]*v for k,v in weights.items()),3), 'source_ids':o['evidence']})
    ranked = sorted(options, key=lambda x:(-x['score'],x['option']))
    return {'scenario':scenario, 'status':'PASS', 'weights':weights, 'ranking':ranked, 'warning':data['notice']}

if __name__ == '__main__':
    ap=argparse.ArgumentParser()
    ap.add_argument('--scenario',choices=['neutral','pde','eda','all'],default='all')
    args=ap.parse_args()
    out={x:score(x) for x in ('neutral','pde','eda')} if args.scenario == 'all' else score(args.scenario)
    print(json.dumps(out,ensure_ascii=False,indent=2))
