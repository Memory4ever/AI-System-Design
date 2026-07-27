# AI Research Weekly — 2025-W39

> Coverage Window: 2025-09-22～2025-09-28
> Research Mode: Retrospective Backfill
> Accessed: 2026-07-31
> Backfilled: 2026-07-31

## Executive Summary

本周保留 1 项长期证据：DeepSeek-V3.1-Terminus。重点是约束、机制、trade-off 与演进，不是发布热度。

## Coverage Window and Limitations

- 按官方发布日期、GitHub Release 或 arXiv v1 归档；后续修订回链首次公开周。
- Scholar、OpenAlex、DBLP 负责 discovery/去重；论文事实回到正文。Crossref 仅交叉检验 metadata。
- 历史回填不创建 Daily；Accessed 统一为 2026-07-31。
- 作者/厂商 benchmark 缺少完整 workload contract 时不外推。

## 1. 模型与研究机构

### Source Coverage

按固定机构顺序扫描国内外模型公司、研究机构与 Hugging Face Blog。

- 保留：DeepSeek-V3.1-Terminus（2025-09-22）。

## 2. 论文与学术来源

按 arXiv → Google Scholar → OpenAlex → DBLP 扫描，回到 v1 正文核验。

- 本组无达到保留门槛的候选。

## 3. AI Infra 与工程项目

按 PyTorch → JAX → CUDA → Triton → vLLM → SGLang → Dynamo → TensorRT-LLM → Ray → KServe → Kubeflow → Kubernetes → Hugging Face → DeepSpeed → Megatron-LM → llama.cpp → ONNX Runtime → OpenXLA 扫描。

- 本组无达到保留门槛的候选。

## Candidate Scoring

| Candidate | Technical Novelty | System Impact | Practical Value | Source Reliability | Project Relevance | Longevity | Total | Decision |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| DeepSeek-V3.1-Terminus | 4 | 3 | 3 | 3 | 3 | 3 | 19/30 | Record Only |

### Deep Analysis 1 — DeepSeek-V3.1-Terminus

- First Public: 2025-09-22
- Status: Official corrective model update
- Primary Source: https://api-docs.deepseek.com/updates
- Evolution Relationship: Direct Evolution

#### Why

模型版本修正语言一致性和 agent 行为，显示 model lifecycle 需要可追踪 regression。

#### Principle and Mechanism

官方 changelog 只证明修复范围，不提供新机制。

#### Trade-off and Evidence Boundary

silent alias upgrade 会改变线上行为与评测基线；但本事件未达到 Books 机制门槛。

#### Connection and Evolution

知识树位置：第 55、62、69 章。Record Only。若进入 Books，将保留旧方案仍成立的条件，并区分官方事实、作者实验和跨来源推断。

## Full Source Review

### DeepSeek-V3.1-Terminus

- **Candidate / Week / Score:** DeepSeek-V3.1-Terminus / 2025-W39 / 19/30。
- **Source Family ID:** `DEEPSEEK-V3.1-2025-08`。
- **Source Type:** official corrective release、API changelog、open-weight artifact。
- **First-public Date / Revision History:** Terminus 2025-09-22；是W34 V3.1的corrective revision，不是新architecture family。
- **Direct Primary Sources:** official Terminus announcement；DeepSeek API changelog；official model repository/checkpoint。
- **Related Primary Sources:** W34 DeepSeek-V3.1、W40 V3.2-Exp。
- **Access and Verification Status:** Verified for stated corrections and availability；root cause、training data/algorithm、regression set与internal architecture delta Not Disclosed。
- **Full-read Coverage:** 已读announcement、changelog、stated language/coding/search-agent fixes与deployment availability；无technical report可供mechanism全文阅读。
- **Original Problem:** V3.1线上/开放checkpoint出现中英混杂、异常字符及Code/Search Agent体验问题，需要可定位的corrective version。
- **Why the Previous Design Was Reasonable:** alias直接跟随最新checkpoint降低用户迁移成本；同family小修避免重新发布完整技术报告。
- **Changed Constraint:** agent workflow和多语言输出使小行为regression也会传播到parser、tool query与评测baseline。
- **Mechanism:** 官方仅声明保持原能力并修正语言一致性/异常字符、优化Code Agent与Search Agent；具体data、loss、decoding或parser change Not Disclosed。
- **State Ownership:** provider拥有API alias与checkpoint rollout；self-host operator拥有artifact pinning；workflow owner拥有parser/regression tests。
- **Control Flow / Data Flow:** corrective checkpoint → API alias/artifact发布 → downstream eval/tool workflow；没有公开内部训练控制流。
- **Implementation Details:** Version Fact；Mechanism Not Disclosed。
- **Evaluation Setup:** 官方未公开本次修正的完整benchmark、sample size、hardware或regression thresholds。
- **Baselines / Ablations / Sensitivity:** Not Disclosed。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** Not Disclosed；不能从产品可用性反推。
- **What the Evidence Actually Proves:** 证明model version需要被纳入workflow identity和regression governance，即使architecture未变。
- **What It Does Not Prove:** 不证明新机制、不证明所有语言/agent问题消失，也不证明优于V3.1或其他模型。
- **Limitations / Threats to Validity:** 厂商定性声明、无方法/样本/误差、alias可能silent upgrade。
- **Trade-offs / New Failure Modes:** 快速修正降低已知regression，却使实验可复现性、cache compatibility、baseline lineage与rollback更复杂。
- **Where the Previous Design Still Applies:** 需要reproducibility或validated baseline时应固定旧checkpoint，而不是自动追随alias；V3.1机制结论仍由W34 source承担。
- **Evolution Relationship:** `Layering / Dependency`：base release → corrective checkpoint → later experimental architecture；不是技术替代节点。
- **ROADMAP Node:** Ch55、Ch62、Ch69。
- **Target and Adjacent Chapters Read:** 已阅读 Ch54～56与Ch61～69；现有章节已有version pinning、evaluation identity与rollback原则。
- **Existing Coverage:** Ch55/62/69已覆盖version/trace/regression；本事件只增加一个厂商案例，没有新机制。
- **Integration Decision:** `Weekly Only — Version/Product Fact`（低分来源与拒绝理由已核验）。
- **Changed Files or Rejection Reason:** 不改 Books；Ch55/62/69 已覆盖 version pinning、regression 与 rollback。
- **Open Questions:** 修正集、root cause、alias rollout/rollback、tool-parser compatibility与independent regression未披露。

## Evidence Level

- Official facts 只覆盖公开接口、版本、权重和文档。
- arXiv / technical report 为作者实验，默认 Experimental，未等同独立复现。
- 跨来源演进关系是本项目推断，已显式标注。

## Cross-Week Deduplication

- release、paper v1 与后续集成若日期不同，分别记录证据角色，但只建立一个 Books source packet。
- 新方案不静默覆盖旧方案；记录新增状态、成本和 failure modes。

## Knowledge Tree Position

- DeepSeek-V3.1-Terminus → 第 55、62、69 章（Direct Evolution）

## Recommended Action

- DeepSeek-V3.1-Terminus：Record Only

## Event-Date Daily Decision

历史回填不创建 Daily；证据保留在本 Weekly。

## Books Integration Decision

Books Gate 已完成。该周候选的最终 disposition 已写入各自 Full Source Review；没有评分候选的周保持 No Material Update，不为制造 diff 修改 Books。


## Ignored Noise

- 忽略转载、旧内容重发、无 primary evidence 的榜单与缺条件 benchmark。
- API alias/价格变化若不形成机制，只作为版本治理信号。

## Repository Changes

- 新增 papers/2025/weekly/2025-W39/README.md。
- 新增 DeepSeek-V3.1-Terminus 候选级 Full Source Review；本阶段未修改 Books。

## Open Questions

- 该版本的机制、regression set与rollout边界未披露，因此只保留为version-governance evidence。

## Sources

- DeepSeek-V3.1-Terminus — https://api-docs.deepseek.com/news/news250922/（First Public: 2025-09-22；Accessed: 2026-07-31）
- DeepSeek API changelog — https://api-docs.deepseek.com/updates（Accessed: 2026-07-31）
