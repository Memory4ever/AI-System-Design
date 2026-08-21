# AI Research Weekly — 2025-W11

> Coverage Window: 2025-03-10～2025-03-16
> Research Mode: Retrospective Backfill
> Audit Status: Candidate Evidence Gate Reopened — Full Discovery Replay In Progress
> Historical Books Gate: Closed — Weekly evidence only
> Accessed: 2026-07-31
> Backfilled: 2026-07-31
> Re-audited: 2026-08-20

## Executive Summary

旧版周报只保留 Gemma 3，不能证明 3 月 10～16 日 fixed-source、academic cross-index 与 engineering release
已重放。本轮首先恢复 OpenAI Responses API / Agents SDK（2025-03-11）这一独立 platform event，并开始
Hugging Face/arXiv discovery replay。Gemma 3 与 OpenAI Source Review 可作为已验证 seed，但在全部候选完成
归周、评分与 Full/low-score disposition前，W11 Candidate Evidence Gate保持 Open，Historical Books Gate关闭。

## Coverage Window and Limitations

- 使用官方发布日期、GitHub Release 时间或 arXiv v1 时间；不使用搜索收录日和后续修订日替代 first-public date。
- Google Scholar、OpenAlex、DBLP 用于 discovery、去重和引用链检查；论文机制回到 arXiv / 作者正文。
- Crossref 仅用于 Weekly metadata 交叉检验，不作为机制证据。
- 本周为历史回填，不补造 Daily；访问日期统一为 2026-07-31。
- 厂商 benchmark 和论文实验只代表其披露条件，缺少完整 workload contract 时不做跨系统性能结论。

## 1. 模型与研究机构

### Source Coverage

按固定机构顺序扫描 OpenAI、Anthropic、Apple、Google、Meta、Microsoft、NVIDIA、xAI、Amazon、Cohere、Ai2、Mistral、Qwen、DeepSeek、Kimi、Zhipu、MiniMax、Seed、ERNIE、Hunyuan、Huawei Noah、InternLM、StepFun、MiMo、InclusionAI 与 Hugging Face Blog。

- 保留：Gemma 3（2025-03-12）。
- 保留：OpenAI Responses API / Agents SDK / built-in tools（2025-03-11，public interface/platform event）。

## 2. 论文与学术来源

按 arXiv → Google Scholar → OpenAlex → DBLP 发现与去重，回到论文 v1 正文核验；Crossref 只做 metadata 交叉检查。

- Discovery replay 进行中：3 月 10 feed 已恢复 Unified Reward Model、Sketch-of-Thought、Forgetting
  Transformer、R1-Searcher、SafeArena、Learning from Failures、Linear-MoE、SAGE、LONGCODEU 等 identity；
  需要按 arXiv v1 日期回拨/留存后才能评分。

## 3. AI Infra 与工程项目

按固定工程顺序扫描 PyTorch、JAX、CUDA、Triton、vLLM、SGLang、NVIDIA Dynamo、TensorRT-LLM、Ray、KServe、Kubeflow、Kubernetes、Transformers、Accelerate、DeepSpeed、Megatron-LM、Unsloth、MLX、llama.cpp、ONNX Runtime 与 OpenXLA。

- 本组无达到保留门槛的候选。

## Candidate Scoring

| Candidate | Technical Novelty | System Impact | Practical Value | Source Reliability | Project Relevance | Longevity | Total | Decision |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| Gemma 3 | 4 | 3 | 3 | 4 | 4 | 3 | 21/30 | Worth Watching；版本事实留 Weekly |
| OpenAI Responses API / Agents SDK launch | 3 | 5 | 5 | 5 | 5 | 3 | 26/30 | Books Pending — Refine Agent Platform interface contract |

### Deep Analysis 1 — Gemma 3

- First Public: 2025-03-12
- Status: Official open-model release
- Primary Source: https://blog.google/technology/developers/gemma-3/
- Evolution Relationship: Layering / Dependency

#### Why

开放模型必须在能力、context、multimodality 与可部署硬件预算之间形成可用组合。

#### Principle and Mechanism

官方材料披露模型族、context 和部署目标，但主要 benchmark 来自厂商。

#### Trade-off and Evidence Boundary

模型族提供部署选择，不代表较小模型在真实 workload 中自动获得更优 cost-quality；需要引擎、量化和 SLO 条件。

#### Connection and Evolution

知识树位置：第 21、22、45、46 章。Worth Watching；版本事实留 Weekly。后续若进入 Books，必须保留旧方案仍成立的条件，并把作者实验、官方版本事实和本项目推断分开。

## Full Source Review

### Gemma 3

- **Candidate / Week / Score:** Gemma 3 / 2025-W11 / 21/30。
- **Source Family ID:** `google-gemma3-2025`。
- **Source Type:** 官方发布、technical report、model card。
- **First-public Date / Revision History:** 模型发布于 2025-03-12；technical report arXiv v1 于 2025-03-25 公开，当前 arXiv 仅 v1。两者属于同一 source family，但不能用 3 月 25 日论文发布日期替换 3 月 12 日 release event。
- **Direct Primary Sources:** Google Developers 发布；《Gemma 3 Technical Report》arXiv v1 / 官方 PDF；Google model card。
- **Related Primary Sources:** Gemma 2 technical report、SigLIP 论文仅用于确认演进依赖，不替代本条证据。
- **Access and Verification Status:** Verified；已读取报告正文 25 页、模型卡和发布材料。
- **Full-read Coverage:** metadata、architecture、pre/post-training、long-context、multimodal、distillation、quantization、evaluation、ablation、safety 与 appendix 已覆盖。
- **Original Problem:** 开放权重模型要同时覆盖从单设备到多加速器的部署预算、长上下文和视觉输入；全局 attention 与 KV Cache 会使序列长度直接压缩可服务并发。
- **Why the Previous Design Was Reasonable:** 全局 attention 为任意 token pair 提供最直接的信息路径；dense decoder 和统一 attention pattern 简化训练、kernel 与质量验证。在上下文较短、显存足够时，该方案仍是较低复杂度的基线。
- **Changed Constraint:** 128K context、视觉 token 与消费级/单卡部署目标同时出现后，不能只扩大窗口而忽略 KV 容量、attention pair compute 与量化后的质量保持。
- **Mechanism:** 4B/12B/27B 使用 5 个 local-attention layer 加 1 个 global-attention layer 的周期；local window 为 1024，global/local RoPE base 分别为 1M/10K。视觉侧使用冻结的 400M SigLIP encoder，将 896×896 图像压到 256 个 visual tokens；模型还使用 knowledge distillation 与后训练蒸馏。QAT 约 5,000 steps，以 per-channel/per-block INT4 weights 配合 FP8 execution path。
- **State Ownership:** decoder layer 拥有 local/global attention state；视觉 encoder 产生固定视觉 embeddings；deployment runtime 仍拥有 KV allocation、quantized weight layout 与 batch/SLO。报告没有把这些 runtime state 交给单一通用实现。
- **Control Flow / Data Flow:** image → SigLIP → average pooling / 256 visual tokens → decoder；text/visual tokens → 5 local + 1 global attention 周期 → logits。长上下文减少 global layers 并未消除 local KV、global pair compute 或 serving capacity pressure。
- **Implementation Details:** 1B/4B/12B/27B 的训练 token 分别约 2T/4T/12T/14T；较大模型使用 frozen vision encoder。训练使用 JAX、Pathways/GSPMD、ZeRO-3；报告披露 1B TPUv5e-512、4B TPUv5e-2048、12B TPUv4-6144、27B TPUv5p-6144。
- **Evaluation Setup:** 报告覆盖通用、代码、数学、多语言、多模态、long-context 与安全评测；RULER 同时报告不同 context lengths，量化表给出 32K context 下的 memory estimates。厂商模型比较和 contamination 风险按作者披露处理。
- **Baselines / Ablations / Sensitivity:** 与 Gemma 2 和同规模模型比较；报告包含 local/global attention 配比、QK normalization、蒸馏、post-training 与 quantization 分析。RULER 结果在 128K 相对 32K 下降，说明“窗口可接受”不等于“远距离信息利用稳定”。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 训练硬件如上；context 为 1B 32K、其余最高 128K；量化为 INT4 weight / FP8 path。在线 batch、concurrency、TTFT、TPOT 与 production SLO 未披露，因此不能从模型卡推出 serving 性能。
- **What the Evidence Actually Proves:** 在作者训练与评测条件下，local/global attention、视觉压缩、蒸馏与量化可以组合成不同尺寸的 multimodal open models；报告给出了机制与受限评测证据。
- **What It Does Not Prove:** 不证明 128K 中任意任务都可可靠利用，不证明单卡声明在所有 engine、batch 和输出长度下满足 SLO，也不证明 INT4 对任意下游任务无质量损失。
- **Limitations / Threats to Validity:** 厂商自评、benchmark contamination、未披露 production workload；视觉 encoder 冻结限制端到端适应；long-context retrieval 与复杂多证据推理不是同一能力。
- **Trade-offs / New Failure Modes:** local attention 降低 global compute/KV pressure，却可能削弱跨窗口组合；视觉 token 增加 sequence/KV；蒸馏继承 teacher bias；量化引入 kernel/精度兼容；更长窗口压缩并发并放大 tail latency。
- **Where the Previous Design Still Applies:** 短上下文、需要每层全局交互、部署环境不受 KV 容量约束，或目标 runtime 尚未稳定支持 mixed local/global attention 时，全局 attention / 较短窗口仍合理。
- **Evolution Relationship:** `Direct Evolution`（Gemma 2 → Gemma 3 的 attention/context/multimodal 设计）；与第 22 章属于 `Layering / Dependency`，不是用新模型否定全局 attention。
- **ROADMAP Node:** 主 owner 第 22 章；第 21、24、45、46 章为边界或 handoff。
- **Target and Adjacent Chapters Read:** 已读第 21 章 MoE、第 22 章 Long Context、第 23 章数据；同时核对第 45、46 章职责边界。
- **Existing Coverage:** 第 22 章已经明确最大长度、有效利用、attention compute、KV capacity 与 SLO 必须分开，并已有 local/sparse attention 演进框架；本材料主要提供一个版本化实例，没有改变核心结论。
- **Integration Decision:** `No Change — Already Covered`；Ch21/22 已区分 MoE cost、窗口长度、effective utilization 与 KV/SLO。
- **Changed Files or Rejection Reason:** 不改 Books；只提供 bounded model case。
- **Open Questions:** 5:1 local/global ratio 在真实多证据 workload 的 accuracy/TTFT/KV trade-off；不同 engine 对 mixed attention 与 INT4/FP8 的支持；128K 下并发和 P99。

### OpenAI Responses API / Agents SDK Launch

- **Candidate / Week / Score:** OpenAI Responses API / built-in tools / Agents SDK launch / 2025-W11 / 26/30；Source Family `openai-responses-agents-platform-2025`，official announcement + public API/SDK interface event。
- **Event / sources / coverage:** first public 2025-03-11；已读 https://openai.com/index/new-tools-for-building-agents/ 的 Responses item/stream contract、web/file/computer tools、Agents SDK handoff/guardrail/tracing、Assistants migration boundary及examples。Current docs/code只能作later revision，不倒灌成launch behavior。
- **Problem / previous design / changed constraint:** Chat Completions适合单次生成，Assistants与custom orchestration分别持有 thread/tool/workflow state；多工具、多模型turn与production debugging使“prompt+function call”不足。新接口将model/tool outputs组织为items/stream events，SDK显式暴露 agent、handoff、guardrail与trace，但应用仍拥有业务authorization、durable state与side-effect commit。
- **State / flow / implementation:** application input→Responses model/tool items→built-in或function tool→subsequent model turn→final output；Agents SDK Runner协调 agent/handoff，guardrail在input/output边界检查，trace记录execution。announcement只证明public interface，不披露hosted scheduler、tool sandbox、retry/idempotency或internal model机制。
- **Evaluation contract / evidence boundary:** vendor列出的SimpleQA、OSWorld、WebArena/WebVoyager及customer cases绑定preview model/tool/harness；没有统一hardware、concurrency、TTFT/TPOT或SLO，不能写成通用agent可靠性/性能结论。接口可用不等于tool result正确、权限安全或workflow durable。
- **Trade-offs / failure modes / coexistence:**统一primitive减少client glue，却增加vendor-hosted state、tool billing、data residency、event schema/migration与partial-failure语义；无需built-in tools时 Chat Completions仍是合理简单分支。Assistants当时尚未正式deprecated，不能用later sunset覆盖launch事实。
- **Evolution / owner / disposition:** `Direct Evolution`（Chat Completions/Assistants/Swarm→Responses+Agents SDK public platform contract）；owner `AGENT-PLATFORM`（Ch84，legacy Ch80），handoff `AGENT-TOOL-CALLING`、`AGENT-WORKFLOW`、`PLATFORM-TRACE`；目标/相邻章节已由既有全书审计覆盖。`Books Pending — Refine Existing Argument Candidate`，W11 Gate前不改Books。Open questions：item identity、durable resume、exactly-once side effects、trace redaction与provider portability。

## Evidence Level

- 官方 Blog / Release 只证明公开的产品、版本与项目事实；未公开实现标记为未知。
- arXiv v1 属于作者实验结论，默认 Status: Experimental，不等于独立复现或通用生产结论。
- 本周没有使用社区观点支撑机制结论；跨来源连接属于本项目推断，已通过 Evolution Relationship 标记。

## Cross-Week Deduplication

- 事件按 first-public date 归属本周；后续 revision、模型卡补充和工程集成回链本周，不重复创建新事件。
- 与前后周出现的同一技术只在年度索引建立演进关系，不把新版本写成对旧方案的静默替代。

## Knowledge Tree Position

- Gemma 3 → 第 21、22、45、46 章（Layering / Dependency）

## Recommended Action

- Gemma 3：Worth Watching；版本事实留 Weekly

## Event-Date Daily Decision

历史回填不创建 Daily。事件日期与 evidence boundary 直接保留在本 Weekly。

## Books Integration Decision

Historical Books Gate关闭。Gemma 3与OpenAI platform event仅作为已验证seed；W11 discovery/evidence Gate闭合前
不确认任何Books Integration，本轮不修改Books。


## Ignored Noise

- 未保留旧内容重发、缺少 primary source 的转述、未绑定 workload contract 的 benchmark 宣传和纯产品可用性更新。
- discovery 数据库的相关性排序与引用量不作为 Technical Novelty 或 Source Reliability 的替代指标。

## Repository Changes

- 重开 `papers/2025/weekly/2025-W11/README.md` 的Candidate Evidence Gate，保留Gemma 3并补入OpenAI platform event Full Source Review。
- 开始3月10～14 academic replay；尚未完成的identity不提前评分或写入Books。

## Open Questions

- 继续闭合3月10～14 feed的v1归周、3月11页面429 gap、3月13/14候选与engineering releases；ordinary pending仍非零。

## Sources

- Gemma 3 — https://blog.google/technology/developers/gemma-3/（First Public: 2025-03-12；Accessed: 2026-07-31）
- Gemma 3 Technical Report — https://arxiv.org/abs/2503.19786（v1: 2025-03-25；Accessed: 2026-07-31）
- Gemma 3 Technical Report PDF — https://storage.googleapis.com/deepmind-media/gemma/Gemma3Report.pdf（Accessed: 2026-07-31）
- OpenAI agent tools launch — https://openai.com/index/new-tools-for-building-agents/（First Public: 2025-03-11；Accessed: 2026-08-20）
