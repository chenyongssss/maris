# Before / after — why personalization matters

**This is a fictional product walk-through and a suggested output, not a real model run or proof of improved accuracy.** All people and conversation excerpts are invented.

## Original human task

> Optimize my periodic finite-volume solver without changing the numerical method or compromising mass conservation.

The assistant generated the following *synthetic* diff excerpt:

```diff
--- a/solver.py
+++ b/solver.py
@@ -21,6 +21,8 @@
-    u_next = u - dt * divergence(flux(u))
+    u_next = ssprk3_step(u, dt, divergence)
@@ -62,4 +64,4 @@
-    left = np.roll(u, 1)
+    left = np.pad(u, (1, 0))[:-1]
```

The changed code is intentionally incomplete and not executable. It illustrates the *need* for review; it cannot establish a specific stability or conservation failure.

**Generic agent summary**

> Migrated to SSP-RK3, refactored boundary conditions, cleaned up logging. Please review the implementation.

**MARIS profile off (suggested)**

> **Priority 1 — Scope conflict (`OBSERVED`).** The old Euler step was replaced despite the human instruction not to change the numerical method. Get explicit human approval before accepting the method change.
>
> **Priority 2 — Periodic boundary invariant (`OBSERVED` + `INFERRED`).** `np.roll` was replaced with zero-padding-based indexing; this *may* change periodic boundary semantics. The provided excerpt is insufficient to determine mass conservation. Review the full flux calculation and test total mass on a periodic example.
>
> **Priority 3 — Missing numerical evidence (`UNKNOWN`).** No convergence, stability, or conservation measurements were supplied. Request them; do not claim third-order accuracy or preserved conservation.

**MARIS profile on (suggested)**

The user previously *explicitly* stated familiarity with conservative numerical schemes and a preference for equation-first explanations, and separately confirmed this as an approved profile.

> **Priority 1 — Scope conflict.** You asked for no change in numerical method; the diff changes Euler to SSP-RK3. Your decision: approve the new method or revert it.
>
> **Priority 2 — Conservation:** The replacement of `roll` with a nonperiodic padding pattern deserves a direct check of the telescoping property
> \[\sum_{i}(F_{i+1/2}-F_{i-1/2})=0.\]
> Ask for the complete boundary flux and a discrete mass-history test. This is a verification request, **not** a claim that conservation has failed.
>
> **Priority 3 — Stability:** Request the actual SSP-RK3 stage implementation and its timestep bound. Basic finite-volume terminology skipped, as requested.
>
> `Explain #2` · `Verify #2` · `Challenge #1`

The objective risk list remains visible in both cases; personalization changes *which explanation is most useful* and the human decision path.

## Try the local consent workflow with fake data

Use the example without any private export:

```bash
python skills/maris/scripts/profile.py catalog --input examples/sample-conversations.json
# Choose 1 and 2, explicitly consent, stage only those:
python skills/maris/scripts/profile.py stage --input examples/sample-conversations.json --indices 1,2 --consent
# Inspect .maris/private/staged.json (never commit it)
python skills/maris/scripts/profile.py template
# Copy the synthetic candidate as demonstration only; with real data, review/edit it first:
cp examples/sample-profile-candidate.json .maris/private/profile-candidate.json
python skills/maris/scripts/profile.py approve --confirm APPROVE-MARIS-PROFILE
python skills/maris/scripts/profile.py show
# Remove local fake sample data:
python skills/maris/scripts/profile.py erase --confirm DELETE-MARIS-LOCAL-DATA
```

Avoid running the sample `cp` step with genuine personal data: it **overwrites** the candidate with synthetic values. For a real profile, the host agent proposes fields and the human reviews them before executing `approve`.

## Failure cases we want contributors to report

- A high-impact change MARIS failed to highlight.
- An unsupported claim presented as if it were verified.
- A wrong user-profile inference or unwanted personalization.
- A profile-on brief that hides a risk visible in profile-off output.
- An imported chat prompt-injection instruction affecting behavior.
