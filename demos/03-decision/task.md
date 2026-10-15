# Decision task — publicly releasable engineering-software interoperability wedge

A hypothetical small research-software founding team wants to announce a credible **open-source engineering software prototype** within eight weeks. They are evaluating three public-ecosystem paths related to gaps around Simulink, CAD/CAE and EDA:

A. FMI/SSP-based dynamic-system model interoperability (OpenModelica/OMSimulator/Xcos),
B. STEP CAD geometry validation/round-trip tooling (FreeCAD/OCCT),
C. Open-source digital ASIC design-flow auditing (Yosys/OpenROAD/KLayout).

**User goal:** decide which *narrow, demonstrable, independently testable* open-source project to prototype first; NOT claim replacement of entire proprietary systems. Use only public, license-permitted input artifacts. Do not assume proprietary format access or legal reverse-engineering permissions.

**Evidence:** `evidence/source-ledger.json` contains dated official/maintainer documentation links; `evidence/option-scores.json` contains *illustrative assumptions*, not measured performance. Their separation is essential.

**MARIS checkpoint:** before recommending a final path, ask whether the first target user is dynamic-systems modeling, mechanical CAD, or digital ASIC engineering, and whether the team has corresponding engineering/domain capability. If no answer, give only a provisional ranking and an experiment plan. Explicitly identify unknowns.
