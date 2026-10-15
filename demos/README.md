# MARIS: three evidence-backed demos — Understand · Verify · Decide

**Your AI moves fast. Stay in control.** These are three real *tasks*, not three alleged benchmark wins. They exercise different cognitive interventions with user goals, observations, missing evidence and a human decision gate.

| | Demo | Evidence class | Exact takeaway |
|---|---|---|---|
| **01 · Understand** | [Coding: RevAgent privacy retention](01-coding/README.md) | Real, pinned [history commit](https://github.com/chenyongssss/revagent/commit/42ab1cb4488051a6c4066b3053deea548d47be27) and [later fix](https://github.com/chenyongssss/revagent/commit/40b48733b1d8e9b0641dbb750c488b1f77bae2f1) | Storing `30_days` is not enforcing expiry |
| **02 · Verify** | [Research: Poisson reconstruction](02-research/README.md) | Exact manufactured counterexample; independent [rational-arithmetic checker](02-research/evidence/poisson_checker.py) | Finite sensors do not establish the same uniqueness theorem as exact open-set observations |
| **03 · Decide** | [Decision: open engineering software](03-decision/README.md) | Official [FMI/STEP/EDA documentation ledger](03-decision/evidence/source-ledger.json) and a transparent [what-if scorecard](03-decision/evidence/option-scores.json) | Recommendation may change with the user's authorized project objectives; decisions require a checkpoint |

## Execute all local checks

```bash
python demos/run.py --verify
```

## Inspect all three MARIS reference views

```bash
python demos/run.py --case coding   --mode personalized
python demos/run.py --case research --mode personalized
python demos/run.py --case decision --mode personalized
```

`baseline`, `cold`, and `personalized` reference views exist for every case:

```bash
python demos/run.py --case research --mode baseline
python demos/run.py --case research --mode cold
python demos/run.py --case research --mode personalized
```

**Essential honesty:** This command is an **offline curated-reference player**, not a MARIS/Claude/Codex model execution. These texts are author-prepared expected findings with evidence links, **not** actual LLM answers or measured comparisons. The verification command checks source-excerpt integrity, executes the exact Poisson arithmetic, and checks the decision matrix/ledger; it cannot certify the full upstream code or any agent effectiveness.

## Run MARIS for real

Use the [common evaluation protocol](EVALUATION.md) to run the same underlying host/model/task in baseline, MARIS cold-start, MARIS with approved profile, and optionally baseline+same profile conditions. Capture provenance and output; compare blind with a predeclared rubric. For public demonstration, the included profile fixtures are *invented, non-identifying personas*, not scraped or inferred from real users' histories.

## What these demos deliberately do not contain

No imported personal chat history, unpublished research manuscript, proprietary engineering models, hidden background interception, simulated success metrics or unlicensed binary reverse engineering. Historical RevAgent commit behavior must not be misrepresented as current code behavior. See [MARIS privacy policy](../docs/PRIVACY.md).
