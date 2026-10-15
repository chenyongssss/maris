# Auditable mathematical evidence — Poisson with finite interior sensors

Take Ω=(0,1)^2, and let `a(s)=s(1-s)`.

\[
 u_0(x,y)=30a(x)a(y),\qquad f(x,y)=60[a(x)+a(y)].
\]

Direct differentiation gives \(-\Delta u_0=f\). Suppose only four interior pointwise observations are given, at \((x,y)\in\{0.3,0.7\}^2\), inside the observation subdomain \((1/8,7/8)^2\). Complete boundary data are **not** prescribed.

Define

\[
 h(x,y)=(x-\tfrac12)^2-(y-\tfrac12)^2,
 \quad \Delta h=2-2=0,
 \quad u_1=u_0+h.
\]

At all four sensors \(h=0\), so both states generate identical sensor measurements; and \(-\Delta u_1=f\) holds everywhere. But at \((1/2,1/4)\), \(h=-1/16\), so \(u_1\ne u_0\). At the boundary point \((0,1/2)\), \(h=1/4\), so the complete boundary traces differ.

**Conclusion:** exact finite point observations + this PDE + unknown boundary trace do not uniquely specify the full state. No fabricated PINN outputs, numerical convergence or model performance is implied. Execute `python demos/02-research/evidence/poisson_checker.py` for exact arithmetic assertions.

**What this does NOT show:** Nonuniqueness when an exact solution is known on a genuine open subdomain. The difference of two solutions with the same source is harmonic; if it vanishes on an open subset of a connected domain, analyticity/unique continuation forces it to vanish throughout. Practical noisy, finitely sampled data create a distinct inverse problem with stability and regularization questions.

**General argument:** Given \(N\) finitely many measurement points, the real harmonic polynomials of degree ≤\(N\) have dimension \(2N+1\), e.g., \(1,\Re z^k,\Im z^k\) for \(k=1,\dots,N\). The map taking values at the \(N\) sensors has a nontrivial kernel, producing a nonzero harmonic perturbation with zero sensor values. This is a linear-algebra proof for arbitrary finite sensor locations, provided no other constraints exclude the perturbation.
