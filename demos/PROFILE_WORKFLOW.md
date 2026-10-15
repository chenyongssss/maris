# Optional: demonstration of consent-gated cognitive profiles

The three case profiles are **fictional fixture personas**, not user data or evidence that MARIS automatically mined real chat histories. The existing `profile.py` supports an *explicit*, user-initiated, local workflow.

## Safe synthetic workflow (no real personal history)

1. Use only `examples/sample-conversations.json`, a synthetic chat export containing an intentionally **excluded** conversation.
2. To avoid touching your real workspace, enter an empty temporary directory. Point `PY` and `SAMPLE` to absolute paths in the MARIS repo.
3. Inspect titles only; then select exactly indices `1,2` and explicitly authorize local staging.

```bash
# From inside a disposable temporary directory:
python "$PY" catalog --input "$SAMPLE"
python "$PY" stage --input "$SAMPLE" --indices 1,2 --consent
python "$PY" template
```

4. The created `.maris/private/staged.json` has selected user messages (not assistant replies) and may be sent to a model **if you authorize that separate processing step**. For a public trial, do not send it anywhere; manually fill `.maris/private/profile-candidate.json` from the two selected synthetic conversations and review every entry. The candidate remains inactive.
5. A real person should explicitly approve their finalized candidate. For the **synthetic-only** tutorial, you may test the command:

```bash
python "$PY" approve --confirm APPROVE-MARIS-PROFILE
python "$PY" show
python "$PY" erase --confirm DELETE-MARIS-LOCAL-DATA
```

**Caution:** `approve` means *you* have reviewed and chosen to save this local file. Do not run it for actual users without their review/consent; do not auto-approve candidate profiles as part of an agent background job. The selected data may reach your Agent model provider when read by the host, even though the local Python helper does not transmit it. Local files are unencrypted; the erase command does not erase source exports or remote provider logs.

## Live MARIS profiling evaluation

For real participants: get source-specific and purpose-specific consent; allow users to refuse with no-profile mode, review/rectify estimated competencies, and withdraw. Hold their approved profile fixed across tasks, and also compare a **generic base model given the same approved profile** to isolate what the Skill contributes. See `EVALUATION.md`.
