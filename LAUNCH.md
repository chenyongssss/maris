# MARIS — public launch kit

## GitHub repository title

**MARIS — Your AI moves fast. Understand what matters.**

Repository description (under 160 characters):

> Memory-aware human oversight for AI agents. Know what to understand, verify and decide—with optional consent-based cognitive profiles.

Suggested topics: `agent-skills`, `ai-agents`, `human-in-the-loop`, `cognitive-assistance`, `code-review`, `research`, `privacy-first`, `claude-code`, `codex`

## Short English launch post

**AI agents are getting faster than we can understand their output.**

I’m open-sourcing **MARIS — Memory-Aware Review & Insight Skill**.

It helps you identify the handful of decisions that actually deserve human attention, links every important claim to available evidence, and explains the hard parts at *your* level. With your explicit consent, MARIS can use selected past conversations to propose a user-reviewable cognitive profile that personalizes the review.

Not another AI agent. A human-understanding layer for the agents you already use.

- In-session checkpoints or post-task review
- Evidence vs. inference, clearly separated
- Optional local cognitive profile; no silent history access
- Cross-host Agent Skills packaging, with documented limitations

Source and install: [replace with live GitHub link].

**What part of your agent's output do you usually struggle to trust or understand?**

## 中文首发文案

**AI 生成得越来越快，但我们真的理解自己交给 AI 完成的工作了吗？**

今天公开一个新的开源项目：**MARIS — Memory-Aware Review & Insight Skill**。

它不试图再造一个 Agent，而是补上 Agent 与人之间缺失的一层：

- 从大量 AI 产出中识别真正值得理解、检查与决定的关键内容；
- 证据、风险推断、未验证结论严格区分；
- 在当前 Agent 工作过程中按需提供低打扰的关键决策 Checkpoint；
- 经用户明确授权后，选取部分历史对话生成**可审阅、可纠正、可删除**的认知画像，让解释和审查更加个性化。

默认不读取历史、不后台监控、不收集遥测。

我们想做的不是让 AI 解释得更多，而是让人用更少的注意力掌握更重要的决策。

**先公开，边试用边验证。欢迎提交真实但脱敏的案例。**

GitHub：[公开后填入链接]

## Publishing checklist (do not skip)

1. Confirm MARIS naming and licenses in your target jurisdiction. Search GitHub for closely related names; trademark/domain clearance is a separate step.
2. Confirm there is **no user transcript, API key, account secret, private export, `.maris/` staging file or proprietary content** in the Git staging area.
3. From the repository root, run `python -m unittest discover -s tests -v` and inspect `skills/maris/SKILL.md` metadata and all READMEs.
4. Perform at least one real host installation/invocation test and document exact host version and what was observed. Until then, disclose that compatibility is expected from the standard, not experimentally verified.
5. Create the public GitHub repository. Keep the project name `maris`, not `maris-v0.1`, `maris-alpha` etc.
6. Repository owner has been set to `chenyongssss` in the README install command. Verify the public URL resolves before sharing the install command. Replace any launch-post link placeholders.
7. Add repository topics, enable Issues, and consider private vulnerability reporting; publish to skills.sh with the real install link.
8. Publish one 20-second evidence-backed synthetic demo plus one real, consented, sanitized task once tested. Never imply synthetic output is a measured benchmark.
9. Invite feedback about a missed important decision and whether cognitive personalization improved usefulness. Do not request raw private transcripts in GitHub issues.

## GitHub CLI example (requires existing GitHub login)

```bash
git init
git add .
git diff --cached --check
# Review files before publishing:
git diff --cached --stat
git commit -m "Introduce MARIS: personalized human oversight for AI agents"
gh repo create maris --public --source=. --remote=origin --push
```

Publishing is a user-controlled irreversible action: inspect everything, especially staged files and credentials, before proceeding. No GitHub repository has been published by this package's authoring process.
