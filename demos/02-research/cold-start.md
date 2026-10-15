# MARIS reference brief — profile OFF (expected mathematically grounded checks)

**Work:** review a Poisson state reconstruction uniqueness claim. **Evidence:** independent manufactured mathematical example and executable rational checks; not a PINN training result.

1. **Finite observation points do not imply unique full-state reconstruction.** `[VERIFIED MATHEMATICALLY]` The states `u0=30x(1−x)y(1−y)` and `u1=u0+(x−1/2)^2−(y−1/2)^2` share the same source `f=60[x(1−x)+y(1−y)]` and identical values at all four specified sensors. They differ elsewhere by `−1/16` at `(1/2,1/4)` (`evidence/argument.md`; `evidence/poisson_checker.py`). **Action:** narrow the uniqueness statement to its actual observation and regularity assumptions.
2. **Do not confuse unique continuation with discrete identification.** `[MATHEMATICAL DISTINCTION]` Exact equality on an open subset forces a harmonic difference to vanish globally in a connected domain, but four (or finitely many) measurements do not. **Action:** state the measurement model and conditional stability assumptions explicitly.
3. **Boundary information changes the answer.** `[VERIFIED MATHEMATICALLY]` The two constructed solutions have different boundary values, so complete prescribed Dirichlet data would exclude this alternative. **Action:** inventory all imposed BC/IC constraints and separate formal PDE uniqueness from algorithmic recovery.

**Suggested replacement:** "We consider PDE-constrained state reconstruction from partial finite observations without a fully prescribed boundary trace. Identifiability and reconstruction stability depend on the observation model, admissible solution class and additional regularization; a continuous unique-continuation result alone does not establish uniqueness or robustness for finitely sampled noisy data."

**Next:** `Explain #2` · `Verify #1` · `Challenge #3`.
