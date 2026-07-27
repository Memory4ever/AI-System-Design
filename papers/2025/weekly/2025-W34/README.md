# AI Research Weekly — 2025-W34

> Coverage Window: 2025-08-18～2025-08-24
> Research Mode: Retrospective Backfill
> Accessed: 2026-07-31
> Backfilled: 2026-07-31

## Executive Summary

本周保留 1 项长期证据：DeepSeek-V3.1。重点是约束、机制、trade-off 与演进，不是发布热度。

## Coverage Window and Limitations

- 按官方发布日期、GitHub Release 或 arXiv v1 归档；后续修订回链首次公开周。
- Scholar、OpenAlex、DBLP 负责 discovery/去重；论文事实回到正文。Crossref 仅交叉检验 metadata。
- 历史回填不创建 Daily；Accessed 统一为 2026-07-31。
- 作者/厂商 benchmark 缺少完整 workload contract 时不外推。

## 1. 模型与研究机构

### Source Coverage

按固定机构顺序扫描国内外模型公司、研究机构与 Hugging Face Blog。

- 保留：DeepSeek-V3.1（2025-08-21）。

## 2. 论文与学术来源

按 arXiv → Google Scholar → OpenAlex → DBLP 扫描，回到 v1 正文核验。

- 本组无达到保留门槛的候选。

## 3. AI Infra 与工程项目

按 PyTorch → JAX → CUDA → Triton → vLLM → SGLang → Dynamo → TensorRT-LLM → Ray → KServe → Kubeflow → Kubernetes → Hugging Face → DeepSpeed → Megatron-LM → llama.cpp → ONNX Runtime → OpenXLA 扫描。

- 本组无达到保留门槛的候选。

## Candidate Scoring

| Candidate | Technical Novelty | System Impact | Practical Value | Source Reliability | Project Relevance | Longevity | Total | Decision |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| DeepSeek-V3.1 | 4 | 4 | 4 | 4 | 5 | 4 | 25/30 | Must Read；作为 hybrid reasoning 工程 contract，而非 benchmark 更新 |

### Deep Analysis 1 — DeepSeek-V3.1

- First Public: 2025-08-21
- Status: Official API/model update; open weights
- Primary Source: https://api-docs.deepseek.com/updates
- Evolution Relationship: Direct Evolution

#### Why

同一权重支持 thinking/non-thinking 与 agent tool use，可减少模型 fleet，却要求 runtime 正确处理 reasoning state 和 tool protocol。

#### Principle and Mechanism

官方 changelog 确认 hybrid reasoning 与 agent capability 更新；缺少独立完整技术报告时不推断训练细节。

#### Trade-off and Evidence Boundary

统一 endpoint 简化部署，也增加模式选择、parser compatibility、reasoning_content 生命周期和版本漂移。

#### Connection and Evolution

知识树位置：第 20、29、45、46、52、74 章。Must Read；作为 hybrid reasoning 工程 contract，而非 benchmark 更新。若进入 Books，将保留旧方案仍成立的条件，并区分官方事实、作者实验和跨来源推断。

## Full Source Review

### DeepSeek-V3.1

- **Candidate / Week / Score:** DeepSeek-V3.1 / 2025-W34 / 25/30。
- **Source Family ID:** `DEEPSEEK-V3.1-2025`（W39 Terminus为corrective revision）。
- **Source Type:** official release/API changelog、open weights/model card/tokenizer/chat template；无独立technical report。
- **First-public Date / Revision History:** 2025-08-21；2025-09-22由V3.1-Terminus纠正，不能把corrective版本倒写为初始release事实。
- **Direct Primary Sources:** DeepSeek-V3.1 release/changelog；V3.1 Base/Instruct weights、model card、tokenizer config与API thinking/tool documentation。
- **Related Primary Sources:** DeepSeek-V3/V3.1 lineage；W39 Terminus、W40 V3.2-Exp与W49 V3.2。
- **Access and Verification Status:** Verified for artifact/API contract；hybrid training、post-training objective、hardware与效率测量机制 Not Disclosed。
- **Full-read Coverage:** 已阅读release/API/model card/tokenizer/template、mode mapping、128K/tool interface、840B continued-pretraining disclosure与benchmark说明；因无report，不能满足论文式method/ablation覆盖。
- **Original Problem:** separate chat/reasoning checkpoints使model fleet、tool parser和version governance分裂，而agent workload希望在reasoning中调用工具。
- **Why the Previous Design Was Reasonable:** 专用R1 reasoning与V3 chat各自行为清晰、部署与评测可单独回滚；non-thinking请求无需承担reasoning tokens。
- **Changed Constraint:** 同一128K endpoint需要按请求提供think/non-think并复用agent/tool ecosystem，且基础模型还需通过continued pretraining扩展context/data distribution。
- **Mechanism:** 可核实的是`deepseek-chat`→non-thinking、`deepseek-reasoner`→thinking、同一V3.1 family、128K、strict function calling beta与V3 base之上840B tokens continued pretraining；“hybrid reasoning architecture”的内部训练/路由机制未公开。
- **State Ownership:** API alias/router拥有mode mapping；artifact/tokenizer/template拥有serialization contract；serving runtime拥有reasoning/tool parser；workflow拥有tool authority。
- **Control Flow / Data Flow:** request+endpoint/mode → V3.1 artifact/template → thinking或direct generation → tool proposal/parser → external workflow；内部router与training data flow Not Disclosed。
- **Implementation Details:** tokenizer/chat template发生版本变化；weights公开。release未给optimizer、parallelism、quantization或tool parser reference implementation的完整contract。
- **Evaluation Setup:** SWE-bench/Multilingual/Terminal-bench及reasoning efficiency为官方结果；hardware、sampling、scaffold、token budget、concurrency和latency percentile不完整。
- **Baselines / Ablations / Sensitivity:** 仅与R1-0528/前代产品比较；无hybrid-vs-separate、840B continued training、mode contamination或tool-use post-training消融。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 128K与840B continued tokens披露；parameter变化、hardware、precision、batch/concurrency、TTFT/TPOT/SLO Not Disclosed。
- **What the Evidence Actually Proves:** 证明hybrid mode已成为公开API/artifact contract，并要求endpoint、tokenizer、template与tool parser共同版本化。
- **What It Does Not Prove:** 不证明单一hybrid checkpoint总优于双fleet，不证明“更快thinking”的通用latency，也不公开内部mode control。
- **Limitations / Threats to Validity:** mechanism disclosure不足；作者benchmark条件缺失；strict function calling仍beta；一个月后出现language/abnormal-character corrective release。
- **Trade-offs / New Failure Modes:** 减少fleet分裂，却新增mode alias漂移、reasoning-state/parser compatibility、template migration与难以归因的回归。
- **Where the Previous Design Still Applies:** 强SLO隔离、需复现/回滚或runtime不支持reasoning/tool channels时，独立chat/reasoning models仍合理。
- **Evolution Relationship:** `Direct Evolution`：V3 chat + R1 reasoning分支 → V3.1公开hybrid contract → Terminus纠错 → V3.2将thinking tool-use与sparse attention继续整合。
- **ROADMAP Node:** Ch20、Ch31、Ch38、Ch46、Ch52、Ch62、Ch74。
- **Target and Adjacent Chapters Read:** 已阅读 Ch19～21、Ch30～32、Ch37～39、Ch45～47、Ch51～53、Ch61～63、Ch73～75。
- **Existing Coverage:** Ch46/52已有artifact、parser与routing contract，Ch62要求记录实际model/version。V3.1主要是Version Fact；是否refine需与GPT-5/GLM hybrid路线合并后判断。
- **Integration Decision:** `Weekly Only — Version/Product Fact / Mechanism Not Disclosed`。
- **Changed Files or Rejection Reason:** 不改 Books；parser、routing 与 artifact identity 已由 Ch46/52/62 覆盖。
- **Open Questions:** hybrid训练/route实现、mode contamination、exact benchmark harness、Terminus修正范围与independent serving evidence。

## Evidence Level

- Official facts 只覆盖公开接口、版本、权重和文档。
- arXiv / technical report 为作者实验，默认 Experimental，未等同独立复现。
- 跨来源演进关系是本项目推断，已显式标注。

## Cross-Week Deduplication

- release、paper v1 与后续集成若日期不同，分别记录证据角色，但只建立一个 Books source packet。
- 新方案不静默覆盖旧方案；记录新增状态、成本和 failure modes。

## Knowledge Tree Position

- DeepSeek-V3.1 → 第 20、29、45、46、52、74 章（Direct Evolution）

## Recommended Action

- DeepSeek-V3.1：Must Read；作为 hybrid reasoning 工程 contract，而非 benchmark 更新

## Event-Date Daily Decision

历史回填不创建 Daily；证据保留在本 Weekly。

## Books Integration Decision

Books Gate 已完成。该周候选的最终 disposition 已写入各自 Full Source Review；没有评分候选的周保持 No Material Update，不为制造 diff 修改 Books。


## Ignored Noise

- 忽略转载、旧内容重发、无 primary evidence 的榜单与缺条件 benchmark。
- API alias/价格变化若不形成机制，只作为版本治理信号。

## Repository Changes

- 新增 papers/2025/weekly/2025-W34/README.md。
- 本周候选已完成 Source Review；Books Integration 仍受年度 Evidence Gate 约束。

## Open Questions

- 已完成 DeepSeek-V3.1 的 Books disposition；未来只在出现新机制、纠错证据或新的演进关系时重新开启审计。

## Sources

- DeepSeek-V3.1 — https://api-docs.deepseek.com/updates（First Public: 2025-08-21；Accessed: 2026-07-31）
