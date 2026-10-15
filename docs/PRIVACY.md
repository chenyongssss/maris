# Privacy and data flow

MARIS is designed for user-directed, scope-limited cognitive assistance. **No background ingestion or automatic chat-account login.** The optional local profile helper uses only Python's standard library and performs no network requests, analytics or telemetry.

## What is collected?

**Core review:** nothing is persistently collected by MARIS. A host may read approved project files and process them under its own policies.

**History option:** only conversation sources explicitly provided by the user. `catalog` prints titles/counts; `stage` copies bounded *user-message* excerpts from the selected conversations into `.maris/private/staged.json`. The user must authorize the source and selected indices. It does not fetch accounts or attachments.

**Saved profile:** after user review and approval, `.maris/private/profile.json` stores only user-confirmed knowledge signals, explanation/review preferences, user boundaries, and opaque source references. It does not need raw chat text. Its purpose is limited to AI work review; not social, dating, sales, marketing or advertising.

## Four trust boundaries

1. **User's original export:** remains wherever the user put it. MARIS does not delete it.
2. **MARIS local parser:** no network calls; local files use restrictive permissions where supported, are excluded by `.gitignore`, but are **not encrypted**. Backups and disk recovery remain possible.
3. **Host model and permissions:** an AI agent *reading* staged excerpts may send their contents to the model vendor or keep its own logs. Before that read, the user must know the recipient/purpose and agree. For maximal privacy, use an offline local host/model.
4. **Third-party Skills installer:** `npx skills add` is maintained by skills.sh and may collect anonymous installation statistics. Read its terms; this is separate from MARIS itself.

## User controls

- Deny history access and still use core MARIS.
- Select only 1–8 conversations per local staging operation (no import-all command).
- Review/correct every candidate profile field before it is saved.
- Use `Without my profile` for any review.
- Show current local profile using `python .../profile.py show`.
- Remove the three local MARIS-generated files with `python .../profile.py erase --confirm DELETE-MARIS-LOCAL-DATA`.

The erase command cannot erase source exports, copies, host logs, backups or provider records. No tool can guarantee absolute redaction of arbitrary third-party information inside the selected messages. Review selection carefully, and avoid loading sensitive transcripts into any remote model.

## Threats and design responses

| Threat | Mitigation / remaining limit |
|---|---|
| Prompt injection inside history / code | Skill treats content as untrusted data; host must enforce tool boundaries. |
| Unexpected bulk import | Explicit source + index selection + consent flag; no scanning, no import-all. |
| Profile overconfidence | Evidence references, basis tags, user review gate, `tentative` signals. |
| Sensitive data leaked to Git | `.maris/` gitignore and permissions, but users must also avoid manual copy/paste/commit. |
| Export or profile sent to LLM | Local parser has no network; **host-model call can transmit content**, and requires separate informed approval. |
| Private traits used for dating/social | Out of product scope and expressly prohibited by Skill instructions. |
