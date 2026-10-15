# MARIS reference brief — profile ON (illustrative PDE-expert profile)

**Profile:** hypothetical PDE researcher from `profile-example.json` (NOT extracted from actual conversations). **Evidence:** exact rational verification of the independent Poisson fixture.

**Focus 1: Quantifier mismatch in the identifiability claim.** Do not spend space defining \(\Delta\) or Poisson. Instead identify the precise step: **unique continuation on a nonempty open observation set is not an injectivity theorem for the finite sampling operator** \(S_N:u\mapsto(u(x_i))_{i=1}^N\) on an unrestricted harmonic perturbation space. `evidence/argument.md` provides a nonzero element of \(\ker S_N\). This is a structural, not a numerical-optimization, objection.

**Focus 2: The correct stability question.** Even when an idealized continuum observation condition guarantees uniqueness, a noisy/discrete reconstruction needs a quantified conditional stability estimate (under explicit solution class and observation topology) or a regularization/finite-dimensional restriction. `[UNKNOWN]` No such estimate has been supplied for this particular trained PINN. Do not state one unconditionally.

**Focus 3: Keep the experimental claim separate.** A PINN attaining small residual loss and a low validation error in a manufactured test demonstrates that experimental setup's behavior; it does not certify inverse-problem uniqueness. A useful follow-up is to vary sensor density, location, noise level and regularization, and test error outside the sensor region.

**Checkpoint for author:** Is the intended theorem about exact continuum observations, or a finite noisy data-learning problem? Preserve the former statement under its hypotheses; qualify the latter. **No risk is hidden because the user knows PDEs.**
