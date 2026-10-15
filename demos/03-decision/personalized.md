# MARIS reference brief — profile ON (hypothetical persona, illustrative)

**Profile:** fictional `profile-pde-example.json`, **not derived from an actual user's history**. Eight-week timeline, strong numerical analysis, limited scope.

**Provisional recommendation:** **FMI/SSP-based model interoperability and reproducibility checker**, NOT a Simulink clone or a general .slx converter. Under the explicit 1–5 assumption matrix, the PDE-focused scenario scores FMI 4.3 and CAD/EDA 2.7 (`evidence/score_options.py`, `evidence/option-scores.json`). These are *decision-tool scores*, not measurements.

**Why this user should care:** They already know numerical ODE/PDE verification, so explain the important distinction between *model interchange* and *semantic/simulation equivalence*. FMI documents exchange interfaces, but does not by itself prove that two solvers produce matching trajectories. The user should inspect solver settings, event handling and reference trajectories rather than spend time learning what a block diagram is.

**One-week falsifiable pilot:** Use publicly licensed dynamical systems with known reference trajectories, export or obtain compatible FMUs, validate FMI metadata with OMSimulator, run two toolchain configurations, compare trajectories under declared tolerances and document unsupported blocks/events. **Not performed in this demo.**

**What could flip the decision?** An EDA-focused team and committed digital-ASIC user changes the explicit ranking: the alternative fictional EDA scenario scores OpenROAD 4.3 vs FMI 2.55 (run `--scenario eda`). The public technical facts remain unchanged; the **authorized objective** changes.

**MARIS checkpoint before a real resource decision:** Is the first distribution target control/simulation researchers, CAD engineers or chip designers? Do we have a representative legally shareable model and somebody able to evaluate acceptance? If not, treat FMI as a reversible hypothesis only.
