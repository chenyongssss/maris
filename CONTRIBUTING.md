# Contributing to MARIS

Thanks for helping make human-AI collaboration more understandable and safer.

Best contributions are **reproducible**: an anonymized task, generated artifact/diff, expected attention-worthy decision(s), MARIS's actual output, and why the result mattered. Do not attach private exports or customer data.

Priority areas:

- Profile-on versus profile-off comparisons where prioritization differs appropriately.
- Missed invariant, assumption, security or scientific-validity changes.
- Evidence-label and citation correctness.
- Export parser support with real *synthetic* fixtures and strict consent boundaries.
- Host-specific invocation/installation tests (provide exact versions and outputs).

Run tests before opening PR:

```bash
python -m unittest discover -s tests -v
```

Do not modify consent or privacy rules to improve engagement metrics. No telemetry collection without a separate public proposal and explicit opt-in.
