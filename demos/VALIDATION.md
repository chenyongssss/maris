# Local verification snapshot — 2026-10-15

Command executed from the repository root:

```bash
python -m unittest discover -s tests -v
python demos/run.py --verify
python demos/02-research/evidence/poisson_checker.py
python demos/03-decision/evidence/score_options.py --scenario all
```

Validation scope:

- **Package + profile helper + demo integrity:** 19 unit tests passed in the creation environment. This tests static package structure, consent-helper behavior, local mathematics and scenario scoring; it **does not** test a real Agent Skills host or whether generated advice improves human decisions.
- **Coding:** verified selected source-excerpt anchors against pinned public GitHub commits 42ab1cb and 40b487; checker confirms presence of the stored `30_days` and later expiry logic in local reference excerpts. It **does not** run full RevAgent at those commits.
- **Research:** exact rational counterexample executed: four sensor values equal, \(u_1-u_0=-1/16\) at \((1/2,1/4)\), and both satisfy the same Poisson source by analytic differentiation.
- **Decision:** tested weight normalization, evidence-ID references and ranking sensitivity. No FMU, CAD, EDA toolchain, legal review or market trial performed. Option ratings are illustrative, not evidence.

Consult `EVALUATION.md` for a *real* model/user benchmarking protocol. Never use the three curated baseline/model-style reference briefs as proof of superior model performance.
