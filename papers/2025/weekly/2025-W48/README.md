# AI Research Weekly — 2025-W48

> Coverage Window: 2025-11-24～2025-11-30
> Research Mode: Retrospective Backfill
> Accessed: 2026-07-31
> Backfilled: 2026-07-31

## Executive Summary

本周保留 1 项长期证据：Claude Opus 4.5。重点是约束、机制、trade-off 与演进关系。

## Coverage Window and Limitations

- 按官方发布日期、GitHub Release 或 arXiv v1 归档；revision 回链 first-public week。
- Scholar、OpenAlex、DBLP 用于 discovery/去重；论文回到正文。Crossref 只做 metadata 交叉检验。
- 历史回填不创建 Daily；Accessed 为 2026-07-31。
- benchmark 缺完整 workload contract 时不外推。

## 1. 模型与研究机构

### Source Coverage

按固定机构顺序扫描国内外一线模型公司、研究机构与 Hugging Face Blog。

- 保留：Claude Opus 4.5（2025-11-24）。

## 2. 论文与学术来源

按 arXiv → Google Scholar → OpenAlex → DBLP 扫描，回到 v1/官方论文正文。

- 本组无达到保留门槛的候选。

## 3. AI Infra 与工程项目

按固定工程项目顺序扫描训练、编译、推理、平台与硬件 runtime。

- 本组无达到保留门槛的候选。

## Candidate Scoring

| Candidate | Technical Novelty | System Impact | Practical Value | Source Reliability | Project Relevance | Longevity | Total | Decision |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| Claude Opus 4.5 | 4 | 3 | 3 | 4 | 4 | 3 | 21/30 | User-approved exclusion / Unverified |

### Deep Analysis 1 — Claude Opus 4.5

- First Public: 2025-11-24
- Status: Official proprietary release + system card
- Primary Source: https://www.anthropic.com/news/claude-opus-4-5
- Evolution Relationship: Direct Evolution

#### Why

长时 coding/agent 评测逐渐成为 frontier model 的主要产品证据，但系统表现仍由 harness 和 environment 决定。

#### Principle and Mechanism

官方发布与 system card 描述模型能力、安全评估及开发平台更新。

#### Trade-off and Evidence Boundary

更强模型可能减少每任务尝试次数，也可能增加单次成本、权限范围与错误副作用；厂商比较不沉淀为通用结论。

#### Connection and Evolution

知识树位置：第 62、74～77 章。Record Only；Books 无新增机制。进入 Books 时保留旧方案条件，并区分官方事实、作者实验和本项目推断。

## Full Source Review

### Claude Opus 4.5

- **Candidate / Week / Score:** Claude Opus 4.5 / 2025-W48 / 21/30。
- **Source Family ID:** `ANTHROPIC-OPUS-4.5-2025-11`。
- **Source Type:** official model announcement、system card、Transparency Hub summary。
- **First-public Date / Revision History:** 2025-11-24；model id为`claude-opus-4-5-20251101`。system card为2025-11版本；不把后续Claude平台变化回写为模型机制。
- **Direct Primary Sources:** Anthropic announcement；Claude Opus 4.5 System Card；Anthropic Transparency Hub model report。
- **Related Primary Sources:** Anthropic agent-evaluation guidance；仅用于解释 harness/grader failure，不作为该模型训练证据。
- **Access and Verification Status:** `User-approved exclusion / Unverified for full-card claims`：announcement与Transparency Hub全文已核对；官方11.5MB system-card PDF可定位并读到索引/片段，但当前来源通道因体积限制无法阅读全文。用户于 2026-08-01 明确批准跳过本候选；这解除它对其余 74 个候选的 Books Gate 阻塞，但不把本候选标记为 full primary-source verified。
- **Full-read Coverage:** 已完整阅读announcement的model、effort、benchmark setup与platform features；核对Transparency Hub的harmlessness、agentic safety、prompt injection、evaluation awareness、RSP/ASL-3摘要；system card仅覆盖目录/索引片段，非全文。
- **Original Problem:** coding/agent发布越来越用长时环境任务证明能力，但结果由model、test-time compute、harness、grader、workspace与产品工具共同决定。
- **Why the Previous Design Was Reasonable:** 静态、model-only benchmark便于比较和复现；其缺点是难代表多小时工具任务。平台功能与模型分开发布可保持归因清晰。
- **Changed Constraint:** 长时coding、deep research与computer use需要context compaction、memory、tool execution和不同effort budget，裸模型调用不再代表完整产品路径。
- **Mechanism:** announcement公开effort parameter与model/API事实；context compaction、advanced tool use、memory、Chrome/Excel/Desktop属于Developer Platform/Claude Code/consumer app能力，内部model architecture/training mechanism未披露。
- **State Ownership:** model拥有token generation；平台拥有compaction/memory/tools；environment拥有repo/terminal状态；grader拥有任务判定。发布页没有证明这些状态被模型内部持久化。
- **Control Flow / Data Flow:** task → platform构造context/effort/tools → model行动 → environment feedback → compaction/memory → grader；任一层变更可造成巨大分数变化。
- **Implementation Details:** 发布为ASL-3 safeguards；Transparency Hub描述对evaluation awareness的训练/评测调整，但未公开architecture、parameter、data mix或训练recipe。
- **Evaluation Setup:** SWE-bench/Terminal-Bench与internal agent evaluations使用不同thinking/context/trials；发布页披露64K thinking、200K context、Terminal 128K等部分设置，并说明部分baseline hosting后续改善。
- **Baselines / Ablations / Sensitivity:** deep-research内部评测从70.48到85.30来自多项platform techniques组合，不能归因模型；tau2案例显示模型利用policy loophole可能被判failure/reward hacking。缺model-only、harness-only系统消融。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** model id、部分context/thinking limits、API price已披露；hardware、precision、batch/concurrency、wall-clock、TTFT/ITL、tail SLO Not Disclosed。
- **What the Evidence Actually Proves:** 发布了指定模型版本和配套platform，并在作者harness中报告能力/安全结果；也提供“评测contract本身会改变结论”的具体案例。
- **What It Does Not Prove:** 不公开模型机制，不证明platform feature是model能力，不证明vendor benchmark可外推；因system card未全文获取，不能声称完成全部safety/evaluation审计。
- **Limitations / Threats to Validity:** proprietary model、system-card访问不完整、vendor/internal eval、hosting/harness漂移、evaluation awareness与reward hacking。
- **Trade-offs / New Failure Modes:** 更强整合与长任务提高覆盖，却增加permission side effect、hidden compaction、grader exploit、state drift、成本长尾与归因混淆。
- **Where the Previous Design Still Applies:** model-only eval、短任务与显式workflow仍是诊断/可审计的必要分支；platform组合适合复杂任务但必须分层测量。
- **Evolution Relationship:** `Direct Evolution`：single-call model eval → environment/tool agent eval → platform-level long-horizon workflow；后者扩大系统范围，不替代分层基线。
- **ROADMAP Node:** Ch62、Ch74～77。
- **Target and Adjacent Chapters Read:** `Not entered by user-approved exclusion`；未用不完整 system card 驱动章节判断。
- **Existing Coverage:** 不作章节级 `No Change` 断言；已有 announcement 只能支持版本与平台事实，不能证明模型内部机制。
- **Integration Decision:** `User-approved exclusion / Unverified`；不进入 Books，不计入 full-primary-source verified 数量，也不再阻塞其余 74 个候选。
- **Changed Files or Rejection Reason:** 用户批准跳过；system card 未全文核验，任何候选专属机制或安全结论均不得写入 Books。
- **Open Questions:** system card完整evaluation setup/limitations；model-only与platform-only消融；compaction/memory所有权和failure semantics。

## Evidence Level

- Official facts 只覆盖公开接口、版本、权重和文档。
- arXiv / report 为作者实验，默认 Experimental，未等同独立复现。
- 跨来源演进关系为本项目推断，已显式标注。

## Cross-Week Deduplication

- release、paper、model card 与工程集成按证据角色回链，不重复形成 Books 观点。
- 新方案不覆盖旧方案；保留适用条件、新增状态与 failure modes。

## Knowledge Tree Position

- Claude Opus 4.5 → 第 62、74～77 章（Direct Evolution）

## Recommended Action

- Claude Opus 4.5：User-approved exclusion / Unverified；不进入 Books

## Event-Date Daily Decision

历史回填不创建 Daily；证据直接保留在本 Weekly。

## Books Integration Decision

`User-approved exclusion / Unverified`。用户于 2026-08-01 明确批准跳过 Claude Opus 4.5；
本候选不进入 Books，不能作为已核验结论，也不再阻塞其余 74 个候选的 Books Integration。

## Ignored Noise

- 忽略转载、榜单、缺条件 benchmark 与无新机制的价格/可用性变化。
- 不以“更新”自动否定旧设计。

## Repository Changes

- 新增 papers/2025/weekly/2025-W48/README.md。
- 建立 1/1 候选 Source Review；system card 全文仍未核验，本候选按用户批准排除，不产生 Books 修改。

## Open Questions

- 若未来重新纳入，需先在可处理大文件的来源通道中复核官方 system card 全文；当前保持
  `User-approved exclusion / Unverified`，不污染 2025 Books 结论。

## Sources

- Claude Opus 4.5 — https://www.anthropic.com/news/claude-opus-4-5（First Public: 2025-11-24；Accessed: 2026-07-31）
- Claude Opus 4.5 System Card — https://www-cdn.anthropic.com/bf10f64990cfda0ba858290be7b8cc6317685f47.pdf（Published: 2025-11；Accessed: 2026-07-31；Full-text access blocked by source-channel size limit）
- Anthropic Transparency Hub model report — https://www.anthropic.com/transparency/model-report（Accessed: 2026-07-31）
