# MARIS reference brief — profile OFF (expert-authored expected findings)

**Goal:** verify an historical RevAgent memory-feature commit (`42ab1cb`). **Profile:** off. **Evidence:** source excerpts plus follow-up patch, not full runtime execution.

## Focus first

1. **Critical decision — enforce stated retention period.** `[OBSERVED]` The code accepts `30_days` and writes it to `retention_rule`, but the pre-fix `rebuild_history_index()` predicate checks approval, preview and deletion status, not elapsed time (`evidence/retention-before.py.txt`, lines 5–14). `[OBSERVED]` a later fix adds `_expire_history_records()` and invokes expiry before rebuild, search and export (`evidence/retention-after.py.txt`, lines 5–21). `[INFERRED]` Without an independent expiry mechanism, an approved item could remain searchable after the selected period. **Action:** verify behavior at 29, 30 and 31 days with a clock-controlled test; do not claim a breach.
2. **Consent boundary — approve is a separate gate.** `[OBSERVED]` the original lifecycle used `consent == approved` and preview-hash matching before index insertion. **Action:** negative-test unapproved and tampered previews; inspect actual complete module/tests before accepting.
3. **Redaction scope — a regex match is not full deidentification.** `[OBSERVED]` the source documents pattern-based redaction. `[UNKNOWN]` whether personal data outside the patterns exist in representative histories. **Action:** add adversarial redaction examples and manual preview approval.

**Can skim:** simple documentation text explaining CLI command names (not a guarantee of correctness).

**Next:** `Explain #1` · `Verify #1` · `Challenge #1`. **Do not assert that MARIS found this during the historical development**: these are curated expected observations.
