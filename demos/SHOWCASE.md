# Three-demo launch storyboard — truthful, reproducible, and short

This is a presentation script / screen-recording outline. **Do not fabricate a live MARIS host run.** Before a public claim of actual Agent performance, follow `EVALUATION.md`, record the command, host/model/time and preserve the unedited logs.

## 01 — CODING / Understand (50–70 seconds)

**Hook:** “The feature stores ‘delete after 30 days.’ But does it actually delete?”

1. Show real GitHub commit `42ab1cb`: source snippet persists `retention_rule`, indexing tests consent and preview hashes; point out absent time-expiry predicate *in this historical version*.
2. Show follow-up commit `40b487`: `_expire_history_records()`, search-time expiry, regression test.
3. Run `python demos/run.py --case coding --mode personalized`. Explain that this displays an **expert-authored reference**, not an LLM benchmark; show profile fixture marked fictional.
4. User decision: demand an expiry-boundary test before treating the user promise as implemented.

**One-line outcome:** Understanding means identifying what the implementation promised but did not yet enforce, not merely describing changed files.

## 02 — RESEARCH / Verify (50–70 seconds)

**Hook:** “A PDE residual plus four observations. Is the solution uniquely determined?”

1. Show `task.md` and the overly broad candidate claim. State known source / unknown full boundary values.
2. Show \(h(x,y)=(x-\tfrac12)^2-(y-\tfrac12)^2\) and four sensor locations.
3. Execute `python demos/02-research/evidence/poisson_checker.py`. It prints exact `PASS`, zero differences at four sensors and nonzero difference `-1/16` away from sensors.
4. Show MARIS PDE-persona reference: focus immediately on mismatch between exact open-set unique continuation and a finite sampling map; don't explain what Poisson means to a PDE expert.
5. User decision: qualify the theorem claim and specify actual observation/stability assumptions.

**One-line outcome:** An AI-generated mathematical argument can sound convincing; a reproducible counterexample exposes the missing hypothesis.

## 03 — DECISION / Decide (50–70 seconds)

**Hook:** “Should our first open-source engineering tool target simulation, CAD, or EDA?”

1. Show source ledger (Modelica FMI, OpenModelica/OMSimulator, FreeCAD/OCCT, OpenROAD); these are *documented tool capabilities*, not empirical winning scores.
2. Execute `python demos/03-decision/evidence/score_options.py --scenario all`. Show that scores are explicitly hypothetical judgments and the recommendation flips for a different team/customer profile.
3. Show `checkpoint.md` with a human choice. Remind the viewer no proprietary-source reverse engineering or full product replacement is being claimed.
4. User decision: choose target buyer, define one tiny open-standard pilot and the acceptance metrics before committing resources.

**One-line outcome:** The best recommendation depends on user goals; MARIS is designed to surface the decision and uncertainty, not autonomously make the commitment.

---

## Public release checklist

- All source claims have links and pinned commit identifiers wherever possible.
- Research script executed with reproducible exact output, not screenshots of non-existent model runs.
- Decision scores prominently labeled hypothetical; provenance comes from public documentation as of 2026-10-15.
- No real personal conversation/profile, unpublished manuscript or proprietary engineering material appears in the demos.
- Differently worded `baseline.md` comparisons are not described as *observed* model differences.
- Record a true host session before claiming speedups, comprehension gains, autonomous checkpoints or actual model superiority.

## Chinese short hooks for social posting

1. **代码改完了，但用户承诺真的实现了吗？** 通过 RevAgent 真实历史提交，看 AI 审查如何锁定最需要人的一项决策。
2. **四个观测点加 PDE 残差，就能唯一恢复全场吗？** 用一个可运行的 Poisson 反例检验 AI 推理。
3. **Simulink / CAD / EDA，开源替代该先做哪条路？** 同样的技术资料，在不同团队目标下给出不同推荐；关键是人决定什么。

*MARIS: Less output. More understanding. Better decisions.*
