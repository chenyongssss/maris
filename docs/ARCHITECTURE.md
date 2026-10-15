# MARIS design notes

## Product thesis

Agents remove production bottlenecks; humans then need to allocate attention to high-impact decisions rather than reading all generated output. MARIS separates evidence-grounded criticality from personalized comprehension demand.

## Core decisions

1. **Inspect allowed artifacts.** Identify completed task, diff/proof/report, tests and unknowns.
2. **Build consequence graph.** Connect the changes to behavior, assumptions, invariants and downstream decisions.
3. **Prioritize criticality.** Correctness, security, physical/math validity, irreversible impact and missing evidence; never downgraded by familiarity.
4. **Optionally consult approved profile.** Learning/familiar signals and explanation preferences with sources and human confirmation.
5. **Allocate attention.** Select 0–3 issue cards, preserve visibility of additional serious risks, let user choose Explain / Verify / Challenge.
6. **Optional in-session Flow.** When activated by the user, introduce a short checkpoint only at meaningful decision boundaries; no passive external-agent monitoring.
7. **Never claim verified results that were not actually checked.** Source labels OBSERVED / REPORTED / INFERRED / UNKNOWN.

## Why a Skill + helper?

`SKILL.md` defines agent behavior and can be installed across clients. Python stdlib `profile.py` provides a deterministic, local history-selection and profile-lifecycle primitive. Inference over selected history is performed by the host agent only after user consent; a Skill alone cannot read a user's online account history or guarantee host-data privacy.

## Design tradeoff

MARIS does not attempt mathematically calibrated probabilities, automatic long-term mastery tracking, real-time hooks or autonomous agent orchestration in the first public package. These require independent user studies, reliable ground truth and host-specific integrations. The current package intentionally exposes the review/evidence/approval stages so users can check them.
