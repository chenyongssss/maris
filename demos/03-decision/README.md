# Demo 03 — Decision: Which engineering-software open-source pilot should we build?

**Use case:** a real and time-sensitive engineering-software ecosystem decision, grounded in independently checkable official documents. Constraints and weights are explicitly hypothetical; this is **not** a verified company purchase decision.  
**MARIS axis:** Decide + In-session Checkpoint.

## What makes it credible

The technology alternatives exist today: Modelica Association FMI standard, OpenModelica/OMSimulator, Scilab Xcos, FreeCAD/Open CASCADE STEP exchange and OpenROAD RTL-to-GDS infrastructure. Documentation sources, date and limitations are listed in `evidence/source-ledger.json`.

However, the presence of these tools **does not** establish which commercial/engineering problem is worth solving. That requires user type, licensed test materials, team expertise, empirical feasibility tests and buyer interviews.

## Reproduce preference sensitivity

```bash
python demos/03-decision/evidence/score_options.py --scenario all
python demos/run.py --case decision --mode cold
python demos/run.py --case decision --mode personalized
```

Heuristic weights and scores are transparent and modifiable in `evidence/option-scores.json`. If the hypothetical persona prioritizes a PDE-based quick prototype, FMI leads; if the persona is an experienced EDA team with a chip-design customer, OpenROAD leads. This is demonstration of **decision dependence on user objectives**, not quantified MARIS model quality.

## A genuine checkpoint

See `checkpoint.md`: the agent must not make a binding commitment while the target customer and actual resources are unknown. It should offer a reversible first experiment and let the user choose.

**What was NOT performed:** licensing review, proprietary format decoding, real FMU exchange/STEP round-trip/OpenROAD layout run, performance benchmark, investor/market interviews, and validation of the illustrative scoring scale.
