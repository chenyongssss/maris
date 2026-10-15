# MARIS reference brief — profile ON (illustrative profile fixture)

**Profile:** `profile-example.json` — hypothetical, supplied for the demo. No person's historical chat was read, no real profile approval is claimed.

**Focus 1 — The 30-day promise was *stored*, not *enforced*.** `[OBSERVED]` `retention_rule='30_days'` is persisted in the original module, but the original search/index eligibility predicate does not read its age. A follow-up commit implements expiry checks (`evidence/retention-before.py.txt:5–14`; `retention-after.py.txt:5–21`). Since this profile already knows Python and Git, skip function basics: think of retention as a **temporal invariant**, analogous to checking a PDE invariant after each numerical time step. Here the invariant is `now >= approved_at + 30 days ⇒ preview absent and no indexed content`. The historical implementation enforced an approval-state invariant, not a time invariant.

**Focus 2 — Separate consent and deidentification evidence.** Hash matching protects against post-preview tampering but does not prove regex redaction removed all sensitive information. This user is learning data-governance semantics; distinguish **consent to index** from **privacy of indexed text**. Ask for redaction-negative tests and review the allowed purpose.

**Focus 3 — Verify follow-up behavior.** The follow-up code invokes expiration before search/rebuild/export, and adds a backdated timestamp test. `[UNKNOWN]` Full suite result and deployed retention practice; no run is claimed here.

**Decision gate:** Do we require strict 30-day erasure from previews and search indexes for release, or only documented manual deletion? If strict, test expiry before accepting. **No expertise signal suppresses this gate.**
