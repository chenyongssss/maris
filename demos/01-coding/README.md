# Demo 01 — Coding: A declared privacy promise that was not yet enforced

**Use case:** real, public, historical RevAgent commits; no fabricated code defect.  
**MARIS axis:** Understand + Verify.  
**Source:** [before (Sep 3, 2026)](https://github.com/chenyongssss/revagent/commit/42ab1cb4488051a6c4066b3053deea548d47be27) → [later fix (Sep 3, 2026)](https://github.com/chenyongssss/revagent/commit/40b48733b1d8e9b0641dbb750c488b1f77bae2f1).

## Why this is interesting

The first commit added consent-gated local history with regex redaction, approval, SQLite FTS indexing and deletion. It accepted `30_days` as a retention-rule value, but the historical module had no corresponding time-expiration check. A later commit added automatic retention enforcement before search/rebuild/export, with a backdated-timestamp test. This is a genuine **intended contract vs implemented behavior** gap; it is **not** evidence of an actual privacy incident or of a current bug.

## Inspect and reproduce

1. Read `task.md` and `evidence/provenance.json`; use the pinned GitHub commits to inspect complete modules.
2. Run `python demos/run.py --case coding --mode baseline|cold|personalized` from the repository root for **curated reference views**. This command is a playback fixture, not an AI run.
3. Run `python demos/run.py --verify` to check local evidence snapshots.
4. For a *real agent test*, follow `demos/EVALUATION.md`, using the same agent, artifact and tool permissions in all conditions.

**Expected critical item:** time-bound deletion must be enforced rather than just serialized. **Expected user-specific difference:** an experienced Python researcher gets temporal-invariant reasoning instead of an introductory Python explanation.

## Publication boundary

The public commit links and small excerpts are shareable subject to the repository license. Profiles here are hypothetical demonstration fixtures; no private conversation transcripts, unpublished manuscripts or personal histories were imported.
