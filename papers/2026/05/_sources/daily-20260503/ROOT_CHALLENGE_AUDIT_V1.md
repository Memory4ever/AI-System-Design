# 2026-05-03 Root Challenge Repair

本文件记录 root fresh-context title audit 触发的 author-side exact-v1 修订。它不是独立 reviewer 的最终 Semantic Audit，不能关闭 Coverage、Evidence 或 Books Gate。

## Challenge Scope

- 挑战对象：14 个原 pre-denominator closure。
- 全部使用官方 `https://arxiv.org/html/<id>v1` exact-v1 正文，核验 method、evaluation、limitations/counterevidence 与 artifact boundary。
- 审计问题：是否改变长期 security sensor、agent identity、RAG evidence、workflow artifact、evaluation、compute allocation 或 data lifecycle contract，而不只是“与 AI 相关”。

## Reconciled Decisions

### Reopened into Candidate Denominator

| arXiv v1 | Source Family | Owner | Books Decision |
| --- | --- | --- | --- |
| 2605.01186 | SF-ATTACK-AGENT-TERMINAL-FINGERPRINT | PLATFORM-SECURITY | No Change — Existing Coverage |
| 2605.01247 | SF-BROWSING-AGENT-BEHAVIORAL-FINGERPRINT | PLATFORM-SECURITY | No Change — Existing Coverage |
| 2605.01284 | SF-PIXEL-LEVEL-RAG-EVIDENCE-CHAIN | AGENT-RAG | Integrate |
| 2605.01293 | SF-LOGIC-GROUNDED-SKILL-INDUCTION | AGENT-WORKFLOW | No Change — Existing Coverage |
| 2605.01471 | SF-AUTONOMOUS-TEST-REPAIR-VALIDATION-BOUNDARY | PLATFORM-EVALUATION-SYSTEM | Integrate |
| 2605.01560 | SF-NOTEBOOK-REPRODUCIBILITY-STATE-GATE | AGENT-WORKFLOW | Integrate |
| 2605.01566 | SF-MULTIAGENT-PARETO-COMPUTE-ALLOCATION | AGENT-MULTI-AGENT | Integrate |
| 2605.01660 | SF-AGENT-GENERATED-VERIFIED-COMPILER | PLATFORM-EVALUATION-SYSTEM | Integrate |

### Retained as Pre-denominator Closure

- `2605.01208`：GUI-specific SFT/GuAE post-training branch；未形成训练外 verifier/action-commit contract。
- `2605.01346`：GUV hidden-connectivity 的 competing-hypothesis selective predictor；未证明跨 workload calibration/release ownership。
- `2605.01415`：decision-energy/sovereignty 概念框架；尚无 executable enforcement、绕过与 availability evidence。
- `2605.01489`：frontier-science automated data construction 与 8B model；未建立跨领域 data lineage/gate。
- `2605.01502`：seismic segmentation 的 inter-layer-MI proxy；不是 calibrated epistemic probability 或平台 commit sensor。
- `2605.08138`：synthetic-data toolkit/product integration；没有新的 dataset identity、lineage、contamination 或 rollback invariant。

逐项完整 closure 与重开条件已写回 `screening-ledger-v2.1.json/tsv`。

## Result

- Registered/screened：274/274。
- Candidate Denominator：28 → 36。
- Pre-denominator closure：246 → 238。
- exact-v1 author review：36/36。
- Books Decision：22 Integrate、13 No Change、1 Structural Candidate。
- blocked=0；ordinary pending=0。
- Gate：Coverage/Evidence/Books 仍 Open，等待真正独立的 full-population Semantic Audit、root 串行 Books writeback 与 post-write audit。
