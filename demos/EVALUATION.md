# Fair evaluation protocol — from evidence-backed examples to actual efficacy data

**At present these three demos are not three measured MARIS LLM runs.** They are: (1) a verifiable historical code-review target using real public commits, (2) an exact mathematical audit with a real local proof/check, and (3) a public-document desk-research decision scenario with explicit simulated team preferences and transparent scores. Each demo includes curated **reference outcomes** (`cold-start.md`, `personalized.md`) and an illustrative **baseline** (`baseline.md`), all explicitly marked as hand-authored. Do not advertise them as benchmark wins or independent performance tests.

## Two ways to demonstrate

### A. Fast offline evidence playback (available now)

```bash
python demos/run.py --verify
python demos/run.py --case coding --mode personalized
python demos/run.py --case research --mode personalized
python demos/run.py --case decision --mode personalized
```

This checks/can replay objective evidence and reference briefs without API keys, history access or agent execution. The runner *does not* call an LLM or evaluate real MARIS output.

### B. Real Agent Skills run (requires a supported host)

1. Install `skills/maris/` in a compatible host (or use the host's skill discovery). Record host, model version, time, config, tool permissions and seed if available.
2. For each case, open the pinned `task.md` and **all its evidence**, including links to complete original sources when available. Keep source access, base model, compute/time limits and tools identical across conditions. If the model lacks internet access, give each arm the same local snapshot plus stated limitations.
3. Run the following arms in fresh sessions, randomizing order:
   - **Baseline:** no Skill. Prompt: “Review this work and identify up to three things I need to understand, verify or decide. Cite evidence and mark uncertainty.” (Not a deliberately weak baseline.)
   - **MARIS cold:** the same evidence and model with the Skill active, with profile explicitly disabled.
   - **MARIS personalized:** identical evidence/model/Skill and one *user-approved, task-relevant* profile. Demo profiles are **fictional fixtures** and may be used only for a simulated-persona experiment.
   - **Profile-only ablation (strongly recommended):** no Skill, but the same profile supplied to the base model. This isolates the Skill's incremental value from merely furnishing extra context.
4. Save raw model outputs and tool logs under a separate consented, sanitized evaluation record with exact run date; **do not include private chat history** in public artifacts.
5. Blindly score each arm against the same, predefined ground-truth anchors. Evaluators should not know which arm they are rating.

## Ground truth and failure criteria

| Case | Required anchor | False claim to penalize |
|---|---|---|
| Coding | Historical `30_days` retention value without expiry in commit 42ab1cb; follow-up 40b487 adds expiry; do not misstate current HEAD | “A user data breach occurred” / “current RevAgent is broken” / claiming tests run when not |
| Research | Two analytic Poisson solutions coincide at four points, with same source; finite samples ≠ exact open-set observations | “Unique continuation is false” or “a PINN training benchmark was executed” |
| Decision | Tool features trace to official sources; preferences and numeric scores are *assumptions*; requires a real user checkpoint | “FMI beats all options experimentally” / “reverse engineering is automatically legal” / making binding resource choice |

Also score: source-anchor validity; high-impact issue recall; false alarms; criticality not hidden by claimed expertise; completeness of assumptions; user-actionable next steps; profile privacy compliance; review time; user decision accuracy and comprehension questions where real human subjects exist.

**Interpretation:** With only three chosen examples, avoid statistical assertions. Plan a larger prospectively collected set with negative/neutral cases, multiple users, professional labels and interval estimates before publishing improvement claims. Never report an unrun test as passed.
