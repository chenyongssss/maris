# Coding task — real RevAgent revision-history implementation

A software agent has implemented revision-history import, redaction, approval, full-text search, export and deletion in **RevAgent**. Review historical commit `42ab1cb4488051a6c4066b3053deea548d47be27` for decisions that the maintainer MUST understand or verify before declaring the privacy lifecycle complete.

**Evidence:** `evidence/retention-before.py.txt`, `evidence/provenance.json`; compare against the actual follow-up fix `40b48733b1d8e9b0641dbb750c488b1f77bae2f1` for ground truth. Evidence snapshots quote real source excerpts; check source links if uncertain. Do not infer that this problem still exists in current HEAD.

**Goal for MARIS:** surface 30-day expiration semantics first, then assess consent/redaction gates and residual privacy risks. Do not invent a security breach. Distinguish `OBSERVED` (historical code), `INFERRED` (possible consequence) and `UNKNOWN` (external retention mechanisms, operational deployment). Never run history imports or read private histories.

**Suggested agent invocation:** `Use the maris Skill to review demos/01-coding/task.md and attached evidence, first with profile off. Output MARIS Brief with max three decisions and cite line anchors.`
