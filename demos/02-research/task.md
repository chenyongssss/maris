# Research task — check a Poisson reconstruction claim

A research-writing agent proposes the statement:

> "Because the PDE source is known and noisy interior observations are combined with a Poisson residual, the reconstructed full-domain state is uniquely determined, even though complete boundary data are not supplied."

Review the mathematical validity of this statement under **finite sensor observations**. Work only with the independent manufactured test in `evidence/argument.md`, not any confidential manuscript. If useful, run `evidence/poisson_checker.py`, which uses exact rational arithmetic.

Required distinctions:
1. Exact equality of solutions on an **open subdomain** versus equality at **finitely many sample points**.
2. Uniqueness versus conditional stability versus the trained network's approximation error.
3. Known source term and unknown boundary trace; if full boundary data are added, reconsider the conclusion.

Return a MARIS Brief with source-anchored findings, an explicit correction to the statement and a small validation plan. Never claim this counterexample disproves unique continuation under its actual hypotheses.
