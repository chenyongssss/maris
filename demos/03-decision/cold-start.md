# MARIS reference brief — profile OFF (curated evidence-first assessment)

**Goal:** select a narrowly scoped 8-week engineering-software open-source demo. **Profile:** off. **Evidence:** current public vendor/project documentation only; local toolchain and market validation NOT run.

1. **Decision gate: which engineer/user will adopt the first version?** `[UNKNOWN]` No buyer/community segment has been specified. `[OBSERVED]` Public tooling already exists in three different problem classes (FMI/SSP, STEP CAD, RTL-to-GDS). **Action:** confirm dynamic-systems, mechanical geometry, or chip-design target before ranking strategic fit.
2. **Distinguish interop from full product replacement.** `[OBSERVED]` FMI is a public model-exchange/co-simulation standard; FreeCAD/OCCT offer STEP exchange; OpenROAD provides an open digital flow (IDs `FMI-01`/`CAD-01`/`EDA-01` in `evidence/source-ledger.json`). `[UNKNOWN]` Proprietary model import fidelity, end-user demand, commercial license compatibility and equivalence with closed engineering tools. **Action:** prototype against a public, legally shareable benchmark.
3. **Use a reversible selection criterion.** `[ASSUMPTION]` Heuristic scorecard in `evidence/option-scores.json`, not product performance data. A neutral weighting provisionally ranks FMI > EDA > CAD, but must not be treated as a fact about market attractiveness. **Action:** run a one-week feasibility spike per credible finalist and seek three target-user interviews.

**Can skim:** broad feature inventories and marketing slogans; only keep features linked to the pilot acceptance criteria.

**Next:** `Explain trade-off` · `Verify evidence` · `Choose first customer`; do NOT automatically commit budget or perform actions.
