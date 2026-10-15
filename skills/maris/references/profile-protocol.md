# MARIS consent-based cognitive profile protocol

## What this is (and is not)

The profile is a **user-reviewed aid to selective explanation and human oversight**. It is not a personality profile, psychometric score, surveillance database, cross-app tracker, or general account memory. Store only what changes how MARIS should review work.

## Permission sequence

1. **Source:** user points to selected export/text, not "all your chats". Never scan folders, browser sessions, chats or app connectors by default.
2. **Scope:** name the exact history source and which conversation indices/topics will be read. `catalog` requires source access permission and reveals titles/counts only. `stage` requires explicit selected indices.
3. **Processing disclosure:** tell the user that the local parser does not upload data, but the configured LLM may process explicitly selected excerpts if they are provided to the agent. Obtain user agreement before letting the host read staged text.
4. **Purpose:** work-specific selective explanation and review only. No dating, friend matching, marketing or sale of information. Do not process sensitive categories or third-party secrets.
5. **Control:** show candidate fields with evidence references; allow user to remove/edit. No background learning and no saving without a separate explicit confirmation.
6. **Reuse:** profile reuse is opt-in for this workspace and work-review purpose; each review must disclose `Profile: on` and support `without profile`.
7. **Revocation:** remove local staged/candidate/profile files on request; do not imply provider copies or source exports are deleted.

## Supported local sources

- ChatGPT exported `conversations.json` and a ChatGPT export ZIP **if present and authorized**. `catalog` lists conversation titles and counts. The importer stages only selected user messages, never attachments or assistant messages. Excerpts are bounded and do not imply full comprehension of a discussion.
- Curated Markdown / `.txt` transcripts that a user explicitly supplies. No undocumented access to online histories or internal model memory.
- Manually supplied work interests and explanation preferences without any history import.

## Local commands (from workspace root)

```bash
python path/to/skills/maris/scripts/profile.py catalog --input /path/to/conversations.json
python path/to/skills/maris/scripts/profile.py stage --input /path/to/conversations.json --indices 2,5 --consent
python path/to/skills/maris/scripts/profile.py template
# Review and edit .maris/private/profile-candidate.json, then explicitly approve:
python path/to/skills/maris/scripts/profile.py approve --confirm APPROVE-MARIS-PROFILE
python path/to/skills/maris/scripts/profile.py show
python path/to/skills/maris/scripts/profile.py erase --confirm DELETE-MARIS-LOCAL-DATA
```

The helper is Python standard library only, network-free and workspace-local. It does not produce a profile autonomously; a host AI can draft one *only after consent* and a human confirms it. `.maris/` is gitignored; private storage is not encrypted. The host may have its own logs and data-processing policies. If supported, run with a local model and offline host for stricter privacy.

## Candidate JSON schema

```json
{
  "schema_version": 1,
  "purpose": "personalized-ai-work-review",
  "knowledge_signals": [
    {"topic": "PDE discretization", "signal": "familiar", "basis": "self-reported", "evidence_ref": "source12:3"},
    {"topic": "cloud deployment", "signal": "learning", "basis": "tentative", "evidence_ref": "source13:2"}
  ],
  "explanation_preferences": [{"preference": "mathematical, concise", "evidence_ref": "source12:1"}],
  "review_preferences": [{"preference": "prioritize unverified assumptions", "evidence_ref": "source12:4"}],
  "user_boundaries": ["do not use data for social matching"],
  "source_refs": ["source12", "source13"]
}
```

The source IDs above are placeholders, not real data. `signal` is one of `familiar`, `learning`, `unsure`. `basis` is `self-reported`, `demonstrated`, or `tentative`. A saved profile is **user confirmed**, not necessarily externally verified mastery. When a topic is inferred from conversation frequency alone, keep it `tentative` and do not mark it familiar until user confirmation.

Avoid sensitive personal attributes, demographic guesses, financial accounts, locations, private relationship details, credentials, chat text, phone numbers and emails. Avoid saving excerpts: retain only minimal topic/preferences and opaque source references. Never quote or reproduce unrelated personal chats in a public review report.
