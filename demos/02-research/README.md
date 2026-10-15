# Demo 02 — Research: A convincing uniqueness claim meets an exact counterexample

**Use case:** a genuine mathematical auditing task motivated by PDE-constrained partial-observation reconstruction. **MARIS axis:** Verify. **Evidence:** a fully public, self-contained manufactured Poisson example and executed exact-rational checks.

The candidate claim incorrectly promotes "PDE residual + a few interior observations" into unconditional full-domain uniqueness without specifying boundary data, solution space or observation model. The rigorous counterexample \(u_1=u_0+(x-\tfrac12)^2-(y-\tfrac12)^2\) agrees on four sensor points, but not across the domain. It does **not** contradict continuous unique continuation on an open observation subset, and it does **not** criticize any private manuscript or indicate a real PINN run was performed.

## Reproduce

```bash
python demos/02-research/evidence/poisson_checker.py
python demos/run.py --case research --mode cold
python demos/run.py --case research --mode personalized
```

Read `task.md`, `evidence/argument.md` and the raw test output. The mathematical proof is the ground truth; model-produced summaries are not a substitute for it. The personalized fixture is fictional and does not use the researcher's private historical conversations.

**Takeaway:** scientific-argument review requires exact assumptions, an applicable theorem and an actual evidence chain. Personalization should prioritize the quantifier/identifiability issue rather than recite elementary PDE facts.
