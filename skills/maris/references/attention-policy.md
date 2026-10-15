# MARIS attention policy

## Two axes that must not be conflated

**Objective criticality (independent of the user):** safety or security impact, mathematical/correctness risk, irreversible change, downstream blast radius, whether an invariant or assumption changes, available verification evidence.

**Personalized understanding demand:** a user-confirmed learning goal, unknown concept needed for an upcoming decision, gaps in prior understanding, requested explanation depth, repeated explicit requests for detail. When no validated profile exists, treat knowledge as unknown; do not invent one.

Decision selection order:
1. Preserve all urgent objective risks even if the user's profile says `familiar`.
2. Among the remaining consequential changes, prefer those the user must understand for the *next* choice.
3. Within equal-priority changes, explain unfamiliar/learning topics more deeply and familiar topics more briefly.
4. Cap the **initial** list at 3. Invite full audit if material risks remain.

**Never:** use profile to suppress a major risk; grade a person's ability from topic frequency; use social or intimate chats for work review; diagnose traits; assign a 95% confidence without calibration; cite a file you did not read.

## Examples

- PDE: change from Euler to SSP-RK3, revised CFL number and boundary flux. A PDE expert sees stability and conservation evidence first, not an introductory PDE lesson. A beginner gets the exact same critical checks plus a short explanation.
- Backend: auth middleware refactor. A user who knows HTTP but is learning authorization sees threat model and permission checks before a routine logging change.
- Research: AI fills a theorem proof. Identify assumptions and gaps before writing a motivational explanation; distinguish a demonstrable counterexample from a missing proof step.

## Evidence labels

- `OBSERVED`: inspected actual code, derivation, record. Observing a log does not mean independently executing the test.
- `REPORTED`: another agent/user claims "tests passed", no rerun evidence.
- `INFERRED`: plausible downstream concern, reason given, remains unconfirmed.
- `UNKNOWN`: no basis to assess; recommend smallest feasible check.
