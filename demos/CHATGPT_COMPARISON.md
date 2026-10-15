# ChatGPT + MARIS: three workflow comparisons

**Same tasks. Two substantive review presentations. No claimed benchmark win.**

Prepared in the current ChatGPT conversation on 2026-10-15, after the user chose ChatGPT instead of Codex. Session model label: **GPT-6 Astra Pro**; no API response was obtained to pin a backend model snapshot. There were **zero separate Codex or API model calls**. This is not offline local inference.

> **Non-blind, in-session demonstration—not an independent A/B benchmark.** This conversation already contained the tasks, answers and MARIS instructions. The standard-review presentation is **not an unexposed control**. The responses below are authored demonstrations, not transcripts from six independent sessions. Do not infer an accuracy, speed, learning or causal benefit from this page.

Both presentations receive the same task-scoped synthetic context. No private history, stored cognitive profile or third-party personal data was used. `Profile: OFF` does not mean ignoring explicitly supplied task context. MARIS is applied as instructions in this conversation; native Skill installation/discovery and interactive host behavior are **not tested**.

| Case | Standard review and MARIS share | MARIS presentation emphasizes |
|---|---|---|
| [Coding](#coding) | Missing elapsed-time expiry in the supplied historical module | Acceptance gate, temporal semantics and authorization for verification |
| [Research](#research) | The same explicit harmonic counterexample | Which manuscript sentence cannot be accepted and which assumption must change |
| [Decision](#decision) | Only a conditional, reversible FMI experiment | Reported capabilities vs. judgment assumptions vs. human approval |

The ordinary reviews are not intentionally reduced to shallow summaries. These examples show **organization and decision support**, not proof that MARIS found something an ordinary model could not.

## Authoring and evidence rules

The common specification is a strong concise review: identify substantive issues, exact supporting locations, implications for the supplied user context, unresolved assumptions, and a minimum next check. Do not merely summarize. Do not execute the supplied program/tests, approve spending, browse the task-source sites or access private history. The MARIS presentation additionally follows the supplied Skill's attention and response contract, with `GATE / FOCUS / CONTEXT`, claim-level evidence states and explicit execution status.

All six responses were authored within this single ongoing conversation; these specifications are **not separate invocation logs**. Task files and the Skill were inspected before composition. `NOT_RUN` means no task-specific executable check was run to produce that response. Subsequent package checks validate files and helper behavior, not model performance.

### Shared inputs

**Coding:** audit only [the full pinned historical module](https://github.com/chenyongssss/revagent/blob/42ab1cb4488051a6c4066b3053deea548d47be27/src/revagent/history.py) against a requirement for approved redacted history with a user-selected 30-day retention policy. Commit: `42ab1cb4488051a6c4066b3053deea548d47be27`; blob: `692eb28a39e3c7a9878c1860d08db3d4aa69215f`. Dependencies and application scheduling are not supplied. Shared synthetic context: comfortable reading Python, interested in retention-state semantics rather than basic syntax. No claim about a current vulnerability or actual data leak.

**Research:** review the claim that a twice continuously differentiable state is uniquely determined by the following manufactured data. Shared synthetic context: familiar with PDEs and numerical analysis. This is not a confidential manuscript.

```text
1  # Supplied mathematical data
2
3  Domain: (0,1)^2. Equation: -Delta u = 60[x(1-x) + y(1-y)].
4  Observations: u = 135/128 at (1/4,1/4), (1/4,3/4), (3/4,1/4), (3/4,3/4).
5  No complete boundary trace. Exact point observations, not an open subdomain.
```

**Decision:** review FMI/SSP interoperability, STEP geometry exchange and an open digital-ASIC workflow using the [dated source ledger](03-decision/evidence/source-ledger.json) and the `notice`, `features` and `options` portions of [the illustrative option table](03-decision/evidence/option-scores.json). The table's `scenarios` section was **excluded** from the supplied task packet; neither presentation receives an agreed weighting vector. Shared synthetic context: a small numerical-simulation team, no confirmed budget, customer or EDA integration experience; prefer reversible experiments. Linked technical product pages were **not freshly revalidated in this review**. An original ledger date is not evidence of a fresh check by this session.

---

## Coding

### A · Standard-review presentation

**Do not accept this module as implementing the 30-day retention requirement.** It implements parts of a consent-controlled storage lifecycle, but storing a duration is not enforcing it.

In [history.py.txt](https://github.com/chenyongssss/revagent/blob/42ab1cb4488051a6c4066b3053deea548d47be27/src/revagent/history.py), `RETENTION_RULES` admits `30_days` (line 7), and `redact_history` saves the selected rule and `redacted_at` (29–42). Approval records `approved_at` (44–48). However, index eligibility checks consent, deidentification, deletion state and hash—not elapsed time (50–60). Search reads the existing index without an age check (62–70), and export applies the same non-temporal eligibility pattern (78–86). Thus an otherwise eligible old record is not excluded by these functions merely for being old. The full application is not supplied, so this is not a claim that no external scheduler exists or that current users suffered a leak.

Before accepting the feature, define what starts the 30-day clock, how equality at the cutoff is handled, and whether the promise means exclusion on next access or physical removal even while the application is idle. Those are different acceptance conditions.

The minimal regression plan should freeze the clock, create an approved record, build its index, and exercise search, rebuild and export immediately before, exactly at and after the cutoff. Inspect both preview storage and index contents. Include a previously built stale index, `until_deleted`, malformed timestamps and the chosen handling of pending records. A background-deletion promise also needs evidence of its scheduler.

Manual deletion is present (72–76), but requiring a user action does not establish automatic retention. Dependencies and application scheduling remain unreviewed. **No tests were executed; these are proposed checks, not passing results.**

### B · MARIS-guided presentation

**MARIS BRIEF · Historical retention review**  
`Profile: OFF` · `Checks: NOT_RUN` · Scope: supplied module only; shared synthetic task context.

#### 01 · GATE · Can “30 days” be accepted as implemented?

**OBSERVED:** [history.py.txt](https://github.com/chenyongssss/revagent/blob/42ab1cb4488051a6c4066b3053deea548d47be27/src/revagent/history.py):7,29–48 stores the rule and timestamps. Indexing (50–60), search (62–70) and export (78–86) do not compare record age against a deadline.

**INFERRED:** An otherwise eligible old record is not rejected by those functions solely for its age. **UNKNOWN:** whether unsupplied application code schedules deletion; no current-release leak is established.

**FOR YOU:** Treat this as a missing state transition—`approved → expired`—not a missing settings field. Python syntax is not the part you need explained.

**NEXT:** Hold acceptance of the retention claim. Inspect all lifecycle entry points and specify where expiry becomes enforceable.

#### 02 · GATE · What exactly must happen at the deadline?

**UNKNOWN:** clock origin, cutoff equality, invalid-timestamp behavior, and whether idle-time deletion is promised. Manual deletion exists (72–76); it is a different mechanism.

**FOR YOU:** “Unavailable on next access” and “deleted at the deadline even if idle” require different implementations. A read-time guard alone cannot establish the latter.

**NEXT:** The product owner selects the policy; then freeze the clock and test just before/at/after the cutoff across search, rebuild and export, including stale indexes and preview files. Include pending and non-expiring records in the test plan. Do not run it without authorization.

**Acceptance:** blocked for the claimed behavior on the supplied evidence, not a rejection of every part of the module. Routine syntax can wait; scheduler behavior and dependencies remain outside this review.

`Explain #1` / `Verify #2` / `Challenge #1`

## Research

### A · Standard-review presentation

**The stated global uniqueness claim is false.** The [supplied data](#shared-inputs):3–5 contain four exact point observations and no complete boundary trace. They do not exclude nonzero harmonic perturbations.

Set
\[
u_0(x,y)=30x(1-x)y(1-y),\qquad h(x,y)=(x-\tfrac12)^2-(y-\tfrac12)^2.
\]
Then
\[
-\Delta u_0=60[x(1-x)+y(1-y)],\qquad \Delta h=2-2=0.
\]
At each of the four observation points, both squared terms in \(h\) equal \(1/16\), so \(h=0\), and \(u_0=30(3/16)^2=135/128\). Therefore every \(u_\alpha=u_0+\alpha h\), \(\alpha\in\mathbb R\), is a smooth state satisfying the same equation and samples. Yet
\[
u_\alpha(\tfrac12,\tfrac14)-u_0(\tfrac12,\tfrac14)=-\alpha/16.
\]
This is constructive nonuniqueness, not merely a missing proof.

Unique continuation from exact observations on an open set is a different premise: the observation set here has four points, not an open interior. Nor does an optimizer selecting one reconstruction establish that the observations identify that state.

To retain a uniqueness statement, explicitly change and justify the setting—for example, add complete compatible Dirichlet data, or restrict the admissible class and prove injectivity there. A regularized estimator can have a selected or unique minimizer without making the unrestricted inverse problem identifiable.

For the manuscript as currently posed, replace the uniqueness claim with a description of reconstruction under stated priors, and separate empirical reconstruction quality from identifiability. Check the displayed derivatives and samples before use. **This response supplies algebraic reasoning; no numerical solver or verification script was executed.**

### B · MARIS-guided presentation

**MARIS BRIEF · Poisson identifiability**  
`Profile: OFF` · `Checks: NOT_RUN (no script)` · Scope: supplied equation and exact samples.

#### 01 · GATE · Can the manuscript claim a unique full state?

**OBSERVED:** [problem.md](#shared-inputs):3–5 specifies four points and omits full boundary data.

**INFERRED — established by the following explicit algebraic argument:** define
\[
u_0=30x(1-x)y(1-y),\quad h=(x-\tfrac12)^2-(y-\tfrac12)^2,\quad u_\alpha=u_0+\alpha h.
\]
Here \(-\Delta u_0=f\), \(\Delta h=0\), and at the samples \(h=0\) and \(u_0=135/128\). At \((1/2,1/4)\), however, \(u_\alpha-u_0=-\alpha/16\). These are distinct admissible smooth states.

**FOR YOU:** The deciding issue is the nullspace left by the observations, not the accuracy of the training residual. The uniqueness claim is refuted for the supplied class.

**NEXT:** Do not approve that sentence. Check the algebra; revise the claim or explicitly supply assumptions excluding the perturbation.

#### 02 · FOCUS · Which claim can the evidence support instead?

**OBSERVED:** no open-subdomain observations or restricted trial class are included in the task.

**FOR YOU:** Open-set unique continuation, finite-sample identifiability and uniqueness of a regularized minimizer are distinct statements. Numerical convergence to one answer does not make them interchangeable.

**NEXT:** Choose between describing a prior-dependent reconstruction and proving injectivity under added conditions. Complete compatible Dirichlet data would change the problem; do not silently add them to the original experiment.

**Suggested wording:** “We reconstruct a state from finite interior observations under the stated model and regularization; these observations alone do not establish uniqueness in the unrestricted smooth class.”

No confidential manuscript was reviewed. `NOT_RUN` refers to executable checks, not an absence of the displayed proof argument.

`Explain #1` / `Verify #1` / `Challenge #2`

## Decision

### A · Standard-review presentation

**Choose a reversible FMI/SSP feasibility experiment provisionally, not a commercial replacement program.** That is a judgment based on the supplied numerical-simulation team context; it is not a finding of market demand.

The [source ledger](03-decision/evidence/source-ledger.json), entries `FMI-01`–`FMI-03`, reports model exchange/co-simulation interfaces and supporting tools. `CAD-01`–`CAD-02` concerns geometry exchange, while `EDA-01`–`EDA-03` concerns an open digital-ASIC flow and distinguishes it from PCB tooling. These are different workflows, not interchangeable substitutes for one product. The linked pages and software installations have not been independently rechecked for this review.

The [option table](03-decision/evidence/option-scores.json), `notice` and `options`, explicitly labels the numbers as illustrative judgments. It supplies no agreed weighting vector in the assigned task packet, so there is no unique weighted ranking to report. Team-fit assumptions may favor FMI, but neither scores nor tool availability prove customer value, integration effort or distribution suitability.

Before choosing a product, identify the intended user and workflow, the representative models or files, success tolerances, operating constraints and who approves effort. Do not invent a budget or timeline.

For a minimal FMI experiment, select a public dynamic model with an analytic or independently converged reference; pin the FMI version and supported execution mode; export/import across two compatible tools; compare behavior under step refinement and pre-agreed error tolerances. Include event behavior when relevant. Record failures and manual integration steps. This tests interoperability only, not proprietary `.slx` compatibility or a full Simulink replacement.

If the real pain instead concerns STEP round trips or an identified digital-ASIC workflow, reassess the route rather than defend a weighted score. **No tools, market tests or benchmarks were run, and no resource commitment is authorized.**

### B · MARIS-guided presentation

**MARIS BRIEF · Engineering-software pilot**  
`Profile: OFF` · `Checks: NOT_RUN` · Scope: dated ledger, hypothetical scores, shared synthetic team context.

#### 01 · GATE · Are we selecting an experiment or committing to a product?

**OBSERVED:** [option-scores.json](03-decision/evidence/option-scores.json), `notice`, calls all scores illustrative; no agreed weights are supplied in the assigned packet. **REPORTED:** [source-ledger.json](03-decision/evidence/source-ledger.json), `FMI-01`–`EDA-03`, describes tools and standards. Those pages were not revalidated here.

**UNKNOWN:** customer workflow, effort ceiling, required compatibility and acceptance criteria.

**FOR YOU:** Technical availability is not evidence that someone needs the resulting product. Do not turn this table into an approved roadmap.

**NEXT:** Keep any product or spending commitment pending human approval.

#### 02 · FOCUS · Which reversible experiment best fits the supplied context?

**INFERRED:** FMI/SSP interoperability is a reasonable provisional starting point for the stated numerical-simulation team. This is conditional judgment, not an objective winner.

**FOR YOU:** FMU interoperability is not proprietary `.slx` conversion; STEP shape exchange is not complete design-history reconstruction; an open ASIC flow is not PCB design. These boundaries follow the *supplied scope descriptions*, not newly executed compatibility tests.

**NEXT:** Pin a model and compatible tool versions; agree on a reference and tolerances; compare exchange/co-simulation behavior with step refinement. Log failures and integration effort. Do not execute before scope is approved.

#### 03 · GATE · Human checkpoint

“Do we authorize only the bounded FMI interoperability experiment, with a named owner and agreed acceptance criteria, while deferring any replacement-product or commercial claim?”

No answer is inferred from silence. Reopen the route choice if a real STEP or digital-ASIC use case becomes the primary requirement. Weighted scores may support sensitivity analysis later; they are not independent evidence.

`Explain #2` / `Verify #2` / `Challenge #1`

## What this does not establish

The two presentations reach the same substantive conclusions in these three examples. The visible difference is how the findings are organized for the user's next action. No scoring, elapsed-time comparison, user-learning result or independent judgment is reported. These examples do not replace a real first-run host test, a consent-flow test or an evaluation of persistent profiles.

For stronger evidence, use fresh conversations with identical model settings, task packets, tool permissions and output budgets; keep project history and answer keys out, disable unrelated personalization, save the first answers including failures, counterbalance order across repetitions, and obtain independent blinded judging. Model settings that the UI does not expose remain uncontrolled. Assess whether people choose the right acceptance action—not merely whether tags appear.

## 中文说明

这里已经改用当前 ChatGPT（会话模型标识 GPT-6 Astra Pro），不依赖 Codex 登录。Coding、Research、Decision 各有普通审查与 MARIS 工作流两份全文。**当前会话已看过答案，普通审查不是独立基线**，因此只展示工作流组织方式，不宣传胜率或性能提升。两边保留同样的核心发现：到期实现缺口、调和扰动反例、仅有条件成立的探索建议。

两边仅使用相同的虚构任务背景，没有读取真实聊天历史或生成用户画像。MARIS 的展示重点是把分析变成可追踪的证据、用户需要理解的决策和最小验收步骤。严格实测需要另开独立会话；不能将当前页面改名为“六次独立模型测试”。

[Back to README](../README.md) · [原始三个案例](README.zh-CN.md)
