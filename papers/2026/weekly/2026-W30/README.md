# AI Research Weekly — 2026-W30

> Coverage Window: 2026-07-20～2026-07-26
> Research Mode: Retrospective Backfill
> Accessed: 2026-07-31
> Backfilled: 2026-07-31
> Discovery Review Reopened: 2026-08-09
> Re-audit Status: 25/25 source families have final Books dispositions; 17 Refine, 3 No Change, 3 Weekly Only, 1 Emerging, 1 Disputed; 25/25 Full Source Reviews complete; W30 Source-Family Books Gate passed; broader Archive/Discovery Gate remains Open

## Executive Summary

本周最值得沉淀的系统信号来自 NVIDIA Dynamo v1.3。它把 request selection、KV index、
topology-aware routing、SLA planning 与 GPU memory service 放在同一个 disaggregated
serving control plane 中，说明大规模推理的主要矛盾已不只是单 worker kernel 效率，而是：

```text
请求应该去哪里
→ 哪些状态已经存在
→ 状态事件如何传播
→ 资源如何按 SLO 重配置
```

SGLang v0.5.16、HiKV 与 Hugging Face Nunchaku Lite 分别提供了 hybrid state、KV 访问和
量化 kernel 的补充证据，但这些内容已经在现有 7 月 27 日 Daily 中深入记录。本周只校准
首次发布日期并建立前向引用，不再复制同一分析。

模型机构侧的 Gemini 3.5 Flash Cyber 展示了小模型通过多轮 agent invocation 执行
cybersecurity workflow 的产品方向，但它仍是 limited-access preview，效果主要来自厂商
评测，尚不足以形成通用的 agent 架构结论。

重新播放 7 月 20～26 日学术发现源后，本周从 3 篇论文恢复到 20 篇。新增候选覆盖
harness-native RL、异步 RL staleness、agent self-state security、可执行文档/项目构建评测、
retrieval set selection、activation explanation verification、training/runtime co-design 与 Agent
experience distillation。OpenForgeRL 已完成全文核验；2026-08-13 exact arXiv HTML recovery 又恢复其余
16 项，逐篇完成 method、state/control flow、evaluation/ablation、limitations/appendix 与相邻章节审计。
当前 25/25 候选均有非模板化 Full Source Review；broader discovery cross-index 尚未闭合，因此不把
forward checkpoint 误写成全历史 Evidence Gate。

## Coverage Window and Limitations

- 本周按 primary source 的 `published_at`、Blog 日期或 arXiv v1 提交时间归档；不使用
  搜索索引日期代替首次公开日期。
- vLLM v0.26.0 的 GitHub 页面与 API 日期跨越 7 月 25～27 日，归现有 7 月 27 日 Daily，
  本周不抢先改写发布日期。
- Dynamo 与 SGLang 的性能数字均为作者/项目方报告。未同时披露模型、硬件、输入输出长度、
  并发、精度/量化与 SLO 的数字不写成跨系统结论。
- Google Scholar、OpenAlex、DBLP 用于发现与去重；论文事实回到 arXiv 正文。Crossref
  用于 Weekly metadata 交叉检查，不作为机制证据。
- RESOURCE2SKILL、Xiaomi-Robotics-1、On-Policy Delta Distillation、Recursive Harness
  Self-Improvement、Muon Agentic RL、DSWorld、cost-aware security evaluation、ReflectWorld-MM、
  SeerGuard、environment-free API data、Distilled RL、JoyNexus、DataFlow-Harness 与 ReOPD 在
  7 月 20～24 日榜单再次出现，但 arXiv v1 早于 7 月 20 日，分别回归 W27～W29。

## Discovery Recall Ledger

| Ledger Item | Current Count | Review Result |
| --- | ---: | --- |
| Score rows / candidate families | 25 / 25 | 25 Full Source Reviews complete；0 blocked；0 ordinary pending |
| Fixed source coverage | Passed | official/model and infra rows retained；Dynamo/SGLang/Nunchaku source packets reviewed；pre-window attribution corrected |
| Academic discovery window | Expanded | daily discovery feeds + arXiv v1 metadata replayed；cross-index closure pending |
| W30 Evidence Gate | Forward checkpoint passed | all scored candidates reviewed；broader discovery/Historical Evidence Gate remains Open |

## 1. 模型与研究机构

### Source Coverage

按固定顺序扫描：

| Order | Sources | Result |
| --- | --- | --- |
| 1–5 | OpenAI；Anthropic；Apple ML Research；Google DeepMind；Google Research | DeepMind Gemini 3.5 Flash Cyber（7 月 21 日）保留；Google Research SymptomAI（7 月 22 日）仅作 evaluation signal |
| 6–14 | Meta AI / FAIR；Microsoft Research；NVIDIA Research；xAI；Amazon Science；Cohere Labs；Ai2；Mistral AI；Alibaba Qwen | 未发现需升级为 Must Read 的模型研究发布 |
| 15–25 | DeepSeek；Moonshot / Kimi；Zhipu；MiniMax；ByteDance Seed；Baidu ERNIE；Tencent Hunyuan；Huawei Noah；Shanghai AI Lab / InternLM；StepFun；Xiaomi MiMo | 未发现窗口内有完整 primary evidence、且改变本书长期结论的发布 |
| 26–27 | InclusionAI / Ant Group；Hugging Face Blog | Nunchaku Lite 属于 inference engineering，归第 3 节 |
| Weekly | LG AI Research；Sakana AI；01.AI；Baichuan；ModelBest；BAAI；Salesforce；IBM；Databricks / Mosaic | 无高门槛更新 |

### Candidate Scoring

| Candidate | Technical Novelty | System Impact | Practical Value | Source Reliability | Project Relevance | Longevity | Total | Decision |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| Gemini 3.5 Flash Cyber | 3 | 4 | 4 | 4 | 4 | 3 | 22/30 | Worth Watching；Weekly only |
| SymptomAI | 3 | 3 | 3 | 4 | 2 | 3 | 18/30 | Record Only |

### Gemini 3.5 Flash Cyber — Product and Evaluation Signal

- Published: 2026-07-21
- Status: Limited-access preview；官方 benchmark
- Primary Source: https://deepmind.google/blog/introducing-gemini-3-5-flash-cyber/

Google DeepMind 将其描述为面向 defensive cybersecurity workflow 的小型 agentic model，
通过多次 model invocation、tool use 与 iterative refinement 完成任务。它支持一个值得
继续观察的方向：在可验证、工具密集、边界明确的任务中，系统能力可能来自较小模型与
runtime loop 的组合，而不是只依赖单次大模型推理。

目前无法把官方 cyber benchmark 外推到一般 agent workload，也无法从产品页分离 model、
harness、tool environment 和 evaluator 的贡献。因此本周不把它写入 Books。

### SymptomAI — Domain Evaluation Signal

Google Research 报告了一项包含 13,917 名参与者的 conversational symptom assessment
研究。它说明高风险领域的 agent 评测需要同时检查多轮交互、分诊安全、用户理解与不同
人群表现，但医学系统并非本书当前主线，且研究结果不能外推到通用 agent correctness。

## 2. 论文与学术来源

### Candidate Scoring

| Candidate | Technical Novelty | System Impact | Practical Value | Source Reliability | Project Relevance | Longevity | Total | Decision |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| HiKV | 5 | 4 | 2 | 4 | 5 | 4 | 24/30 | Must Read；已由 7 月 27 日 Daily 深入分析 |
| Ground Truth First | 4 | 4 | 3 | 3 | 4 | 4 | 22/30 | Worth Watching；已由 7 月 27 日 Daily 深入分析 |
| Scaling Native Multimodal Pre-Training From Scratch | 4 | 4 | 3 | 3 | 4 | 4 | 22/30 | Worth Watching；已由 7 月 27 日 Daily 记录 |
| SWE-Pruner Pro | 5 | 4 | 5 | 3 | 5 | 3 | 25/30 | Full Source Review complete；Refine `AGENT-CONTEXT` |
| LLM-as-a-Coach | 4 | 3 | 4 | 4 | 4 | 4 | 23/30 | Full Source Review complete；Refine `TRAIN-GRPO` |
| FlashRT | 4 | 4 | 5 | 3 | 5 | 3 | 24/30 | Full Source Review complete；Refine `AGENT-WORKFLOW` |
| Self-State Attacks on Self-Hosted AI Agents | 5 | 5 | 4 | 4 | 5 | 2 | 25/30 | Full Source Review complete；Refine `PLATFORM-SECURITY` |
| Stale but Stable | 5 | 5 | 4 | 4 | 5 | 3 | 26/30 | Full Source Review complete；Refine `TRAIN-GRPO` |
| AgentDebugX | 4 | 4 | 5 | 3 | 5 | 3 | 24/30 | Full Source Review complete；Refine `PLATFORM-TRACE` |
| AutoIndex | 4 | 4 | 4 | 3 | 5 | 4 | 24/30 | Full Source Review complete；Refine `AGENT-RAG` |
| Tiered Optimizer State for MoE | 4 | 4 | 4 | 2 | 5 | 5 | 24/30 | Full Source Review complete；Emerging / Disputed；Weekly only |
| SLAI T-Rex | 5 | 5 | 5 | 4 | 5 | 3 | 27/30 | Full Source Review complete；Refine `TRAIN-DISTRIBUTED-TRAINING` |
| Rubric-Oriented Document Set Selection | 5 | 4 | 4 | 4 | 5 | 3 | 25/30 | Full Source Review complete；Refine `AGENT-RAG` |
| DocOps | 4 | 3 | 5 | 4 | 4 | 3 | 23/30 | Full Source Review complete；No Change — Ch62 already covers artifact verification |
| Decodability Supervision / RECAP | 5 | 4 | 4 | 3 | 5 | 5 | 26/30 | Full Source Review complete；Refine `WORLDVIEW-WHAT-NEURAL-NETWORKS-LEARN` |
| ICAE-Bench | 4 | 4 | 5 | 3 | 5 | 3 | 24/30 | Full Source Review complete；Refine `PLATFORM-EVALUATION-SYSTEM` |
| AREX | 5 | 5 | 5 | 4 | 5 | 4 | 28/30 | Full Source Review complete；Refine `AGENT-WORKFLOW` |
| LLMs Get Lost in Evolving User Intent | 4 | 4 | 4 | 4 | 5 | 3 | 24/30 | Full Source Review complete；Refine `PLATFORM-EVALUATION-SYSTEM` |
| Sample-Efficient Learning from Agent Experience | 5 | 4 | 4 | 3 | 5 | 4 | 25/30 | Full Source Review complete；Refine `AGENT-MEMORY` |
| OpenForgeRL | 5 | 5 | 5 | 4 | 5 | 4 | 28/30 | Full Source Review complete；No Change |

### Deep Analysis 1 — HiKV：从 KV 容量问题走向访问选择问题

- Submitted / First Public Version: 2026-07-24
- Status: Experimental
- Primary Source: https://arxiv.org/abs/2607.22389
- Detailed Record: `papers/2026/07/27/README.md`

#### Why

Decode 的长期瓶颈不仅是 KV 是否装得下，还包括每步必须搬运多少历史状态。

#### Principle

若重要性估计与选择开销低于被避免的数据搬运，就可以用受控的信息损失换取 memory
traffic；但收益必须连同 quality budget 和硬件 dataflow 一起核算。

#### Mechanism

论文以 recent/important banks 与 element-level selection 组合压缩 KV 访问，并提出专用
sorter。具体结构和作者实验边界已在 7 月 27 日 Daily 展开。

#### Trade-off

选择器自身占用算力、面积与控制复杂度；topic shift、irregular access 和 GPU kernel
overhead 都可能侵蚀论文中的专用硬件收益。

#### Connection

第 41 章 KV lifecycle → 第 50 章 memory budget → Part V hardware-aware scheduling。

#### Evolution

只有公开实现和 commodity GPU 上的端到端、等质量复现出现后，才能判断 importance-aware
KV 是否会从研究机制演化为通用 runtime primitive。

### Ground Truth First — Agent Memory Evaluation Signal

- Submitted / First Public Version: 2026-07-24
- Status: Experimental
- Primary Source: https://arxiv.org/abs/2607.21962
- Detailed Record: `papers/2026/07/27/README.md`

该论文把 `valid interval + provenance + supersession + write result` 纳入长期 memory
ground truth。方法论与第 73 章相关，但它仍是单篇、single-author、synthetic benchmark；
本周不重复展开，也不依据架构排名改写 Books。

## 3. AI Infra 与工程项目

### Source Coverage

按 PyTorch → JAX → CUDA → Triton → vLLM → SGLang → NVIDIA Dynamo → TensorRT-LLM
→ Ray → KServe → Kubeflow → Kubernetes → Transformers → Accelerate → DeepSpeed
→ Megatron-LM → Unsloth → MLX → llama.cpp → ONNX Runtime → OpenXLA 的顺序扫描。

### Candidate Scoring

| Candidate | Technical Novelty | System Impact | Practical Value | Source Reliability | Project Relevance | Longevity | Total | Decision |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| NVIDIA Dynamo v1.3 | 4 | 5 | 5 | 5 | 5 | 4 | 28/30 | Must Read；已归并 Weekly；Books 已评估 |
| SGLang v0.5.16 | 4 | 5 | 5 | 5 | 5 | 3 | 27/30 | Must Read；由 7 月 27 日 Daily 深入分析 |
| Nunchaku Lite in Diffusers | 4 | 4 | 4 | 4 | 4 | 3 | 23/30 | Worth Watching；由 7 月 27 日 Daily 记录 |

### Deep Analysis 2 — Dynamo v1.3：把 Selection 从 Router 中独立出来

- Released: 2026-07-22
- Status: Official stable release
- Primary Source: https://github.com/ai-dynamo/dynamo/releases/tag/v1.3.0

#### Why

在 disaggregated serving 中，router 若同时维护前缀状态、worker load、topology、media
identity 和 failure recovery，会逐渐成为共享状态与事件处理瓶颈。

#### Principle

请求入口、placement policy 与状态索引是不同变化速率、不同一致性要求的职责。将
selection service 独立后，可以分别扩展 frontend 和 global scheduling state：

```text
frontend request path
→ selection query
→ KV / media / load / topology state
→ worker assignment
```

#### Mechanism

官方 release 引入 standalone selection service、branch-sharded KV indexer、compressed
radix tree 与 topology-aware routing；同时加入 media-aware KV routing、面向 RL rollout
的 TITO、SLA Planner、workload replay Mocker 和 GPU Memory Service。

#### Trade-off

独立 selection service 降低 frontend 状态负担，却新增网络 hop、索引一致性、分片热点、
故障域和 stale decision 风险。branch sharding 改善吞吐不等于改善 tail latency；状态事件
的处理速度也不等同于端到端 token throughput。

官方给出的约 `28×` store/remove event processing 与 `13.7%` multi-frontend throughput
提升只属于项目方测试。release summary 未完整披露模型、硬件、输入输出长度、精度/量化、
并发与 SLO，不能据此做通用性能承诺。

#### Connection

知识树位置：第 47 章 disaggregated inference → 第 48 章 Dynamo → 第 49～52 章
scheduling、memory hierarchy、communication 与 performance model。

#### Evolution

从每个 router 持有局部 prefix map，到共享 selection service 与分片状态索引，下一阶段
会更像分布式 control plane：需要明确 freshness、ownership、backpressure、failure
recovery 与 decision trace。

### Deep Analysis 3 — SGLang v0.5.16：统一接口不等于统一状态

- Released: 2026-07-25
- Status: Official stable release
- Primary Source: https://github.com/sgl-project/sglang/releases/tag/v0.5.16
- Detailed Record: `papers/2026/07/27/README.md`

#### Why

SWA、Mamba、DSA 与 full attention 的 state shape、lifecycle 和 reuse 条件不同，单一
KV-tree 假设不能稳定覆盖 hybrid model。

#### Principle

runtime 可以统一 ownership、lookup 与 eviction 接口，但必须保留不同 state type 的
layout、更新语义与 verification snapshot。

#### Mechanism

本版本默认启用 UnifiedRadixTree，拆分 DSA cache，并降低 ReplaySSM 的 scratch memory；
同时包含 DSpark 与 KDA 相关实现。具体机制和边界已在 7 月 27 日 Daily 记录。

#### Trade-off

抽象统一减少上层分支，却可能隐藏 state-specific cost；若 scheduler 只看“cache hit”，
就会错误比较不同 state 的重算、搬运和一致性成本。

#### Connection

第 41～45 章 cache/speculative decoding → 第 47～52 章 distributed runtime。

#### Evolution

Serving 的共享抽象会从 `KV block` 演化为 typed model state。兼容性、ownership 与
cost model 比“统一类名”更重要。

## Evidence Level

| Claim | Evidence | Boundary |
| --- | --- | --- |
| Gemini Flash Cyber 的产品形态 | Google DeepMind 官方 Blog | limited access；厂商评测，不外推 |
| HiKV / Ground Truth First | arXiv v1 正文 | `Status: Experimental`；尚无独立复现 |
| OpenForgeRL mechanism / experiments | arXiv v1 full text | 作者实现；特定 harness、models、tasks 与 cloud contract |
| 16 个 recovered expanded candidates | arXiv HTML full text / revision history | Full Source Review complete；作者实验与 prototype claims 保持 bounded |
| Dynamo v1.3 / SGLang v0.5.16 功能 | 官方 GitHub Release | 版本事实；性能数字受未披露条件限制 |
| Nunchaku Lite 集成 | Hugging Face 官方 Blog / Diffusers PR | 工程案例，不代表所有量化模型 |

## Cross-Week Deduplication

- AgentCompass v3 于 7 月 20 日更新，但 first public version 是 7 月 15 日，归 W29。
- HiKV、Ground Truth First、SGLang v0.5.16 与 Nunchaku Lite 已在
  `papers/2026/07/27/README.md` 深入记录；本周只恢复事件时间线。
- Kimi K3 technical report 与 vLLM v0.26.0 的正式公开时间落在 7 月 27 日之后，不纳入
  本批次的 7 月 1～26 日新增内容。
- 14 项在本周 Daily Papers feed 出现、但 v1 早于 7 月 20 日，不在 W30 重复评分。RESOURCE2SKILL
  已凭稳定 primary ID / v1 date 回写 W27；其余 13 项随后也已完成 owner-week identity/date attribution。
  ReOPD 与 ReflectWorld-MM 已在 W28，OPD²、Recursive Harness Self-Improvement、Muon Agentic RL、
  Xiaomi-Robotics-1、DSWorld、Cost-Aware Security Agents、SeerGuard 与 Environment-free API data 已在 W29
  完成 Full Source Review；Distilled RL、JoyNexus、DataFlow-Harness 与 Data-Centric Parallel 也已在
  2026-08-13 exact HTML recovery 后于 owner week 完成全文、评分与章节审计。归周关系与全文证据现已分开记账。

## Knowledge Tree Position

| Candidate | ROADMAP Node | Role |
| --- | --- | --- |
| Gemini 3.5 Flash Cyber | 第 72、76、78 章 Agent / Tool / Evaluation | 产品与评测信号 |
| HiKV | 第 41、50、52 章 KV / Memory / Performance | 研究候选 |
| Ground Truth First | 第 62、73 章 Evaluation / Memory | 方法论候选 |
| Dynamo v1.3 | 第 47～52 章 Distributed Inference | 稳定工程机制 |
| SGLang v0.5.16 | 第 41～45、47～52 章 | hybrid state 实现证据 |
| OpenForgeRL | 第 29、62、77、80 章 | harness-native rollout / train–deploy identity |
| Expanded training / RAG / evaluation / agent set | Stable owners 见 final ledger | 16 项已完成全文审计与最终 disposition |

## Recommended Action

- 7 月 22 日 Dynamo 事件的机制、事实边界与 Books 决策已完整归并 W30；第 48 章已补入
  selection service、状态索引分片和 failure-domain 讨论，独立历史 Daily 已清理。
- SGLang v0.5.16 的 typed-state 机制已 refine Ch47；HiKV、Ground Truth First 与 Nunchaku
  保留现有 7 月 27 日 Daily 作为深入记录，不创建重复的 7 月 23～25 日 Daily。
- Gemini Flash Cyber 与 SymptomAI 保留 Weekly；在出现独立复现或可分离 model/harness/
  environment 的证据前不进入 Books。
- OpenForgeRL 已完成全文审计并判定 `No Change — Already Covered`：Ch29/62/77/80 已有
  rollout identity、environment/version contract、durable execution、trajectory evaluation 与
  governed rollout；论文提供新的实现案例，但未改变章节结论。
- 16 个 expanded candidates 均完成 Full Source Review 与最终 disposition；不存在 blocked/pending。
- Books 只新增 self-state protection/recovery 与 set-level evidence utility；其他 Refine 项由当前 J-space、KV、
  RL staleness、trace repair、world model、workflow 与 distributed-serving 主线具体覆盖，经复核保留。

## Event-Date Daily Decision

| Date | Decision | Reason |
| --- | --- | --- |
| 2026-07-21 | 不创建 | Gemini Flash Cyber 为 limited-access product signal，尚未改变通用框架 |
| 2026-07-22 | 归并后清理 | Dynamo v1.3 的 stable facts、机制与 Books 决策已完整进入 W30 |
| 2026-07-23 | 不创建 | Nunchaku Lite 已由 7 月 27 日 Daily 覆盖 |
| 2026-07-24 | 不创建 | 三篇论文已由 7 月 27 日 Daily 覆盖，避免重复 |
| 2026-07-25 | 不创建 | SGLang v0.5.16 已由 7 月 27 日 Daily 覆盖 |

## Books Integration Decision

`Source-Family Books Gate Passed — Archive Completion Gate Open`。Dynamo v1.3 验证并保留 distributed selection
control-plane 推导：
frontend/selection 独立扩展，index 是观测副本而非 KV authority，sharding 不自动解决
consistency、reservation、failover 与 recovery。SGLang v0.5.16 refine Ch47：统一 radix
identity 不等于统一 physical state，hybrid/recurrent state 必须显式定义 restore、generation、
reset 与 rollback。HiKV 因 custom-accelerator、batch-1 与质量/端到端边界保持
`Emerging / Experimental`，没有写成 commodity GPU 的通用结论。新增的 self-state 与 setwise retrieval
机制分别进入 `PLATFORM-SECURITY` 与 `AGENT-RAG`；其余 16 项由现有具体论点吸收或保留边界。

## Ignored Noise

- 只重复 benchmark 排名、没有 workload contract 的发布摘要；
- 将 GitHub commit、pre-release 或 search snippet 误记为 stable release；
- 用聚合榜单日期覆盖 arXiv v1 日期；
- 把 cybersecurity 或 medical domain 的单项产品结果外推为通用 agent 能力；
- 与 7 月 27～31 日现有 Daily 重复的版本功能列表。

## 2026-07-31 Full Re-Audit Addendum

- Dynamo v1.3 release/code 重审确认 standalone selection、branch-sharded index、topology 与
  trajectory routing 应作为 Ch48 的 versioned control-plane case。
- SGLang v0.5.16 release/code 重审后，将 KV/recurrent/KDA state 共用 cache identity 时的
  reset、rollback、generation 与 retraction contract 写入 Ch47。
- HiKV、Nunchaku 与 Native Multimodal 保留 Daily/Weekly；Ground Truth First 的稳定原则
  已由 Ch62/77 覆盖；Gemini Flash Cyber 为版本化模型状态。

## Full Source Review

### Gemini 3.5 Flash Cyber — 22/30

- **Source Family / Date / Coverage**：`GEMINI-35-FLASH-CYBER`；Google DeepMind 2026-07-21 official
  announcement、evaluation/safety/access material；公开产品能力、harness 和 governance 已核对，训练/
  runtime mechanism `Not Disclosed`。
- **Evidence / Decision**：厂商 cyber benchmarks/cases 不能分离 model、harness、tool/environment 或推导
  unrestricted deployment risk。Ch62/68/74 已读；`Weekly Only — Version/Product Fact`。

### SymptomAI — 18/30

- **Source / Verification**：Google Research 2026-07-22 official report、study/evaluation/limitations 已核对；
  属 everyday symptom-assessment domain Agent，非 clinical diagnosis evidence。
- **Score / Decision**：18/30 维持；`Weekly Only — Version/Product Fact`。

### HiKV — 24/30

- **Source Family ID / Type / Date**：`HIKV-HIERARCHICAL-CACHE`；arXiv:2607.22389v1，
  first-public 2026-07-24。
- **Full-read Coverage**：已覆盖 token/element importance、dual-bank/frozen scores、chunk selection、
  hierarchical decode integration、reconfigurable sorter/Verilog architecture、algorithm/hardware/system
  evaluation、baselines 与 complete setup；论文无独立 limitations 章节，assumptions 单列。
- **Problem / Previous Design / Changed Constraint**：完整 KV 保留准确且 PagedAttention 易管理；长 context
  和大 batch 下 decode memory traffic 主导。token eviction 已减少行数，但 retained token 的 full K/V
  vector 仍带 element redundancy。
- **Mechanism / Ownership / Flow**：Stage I 以 recent/important dual bank、局部 attention accumulation 和
  min-heap 选 token；Stage II 用 Q magnitude 选 K dimensions、对 P 分 chunk 选 V rows；reconfigurable
  importance sorter支持两种数据路。cache manager 拥有 selection metadata，accelerator 拥有 layout/
  datapath，model quality gate 决定允许压缩。
- **Evaluation Contract**：Mistral-7B、Llama3-8B、LongChat-7B-32k、Qwen2.5-0.5B，LongBench 10 tasks，
  prompt 4096、batch1、FP16 baseline，rI/rII 1–4x；硬件为 TSMC16nm/300MHz/0.8V synthesis。headline
  7.95x/90% 是 attention/custom-accelerator result，不是 commodity GPU end-to-end serving SLO。
- **Trade-offs / Evolution**：hierarchical selection 降 memory traffic，增加 approximate error、importance
  drift、multi-turn recompute、non-contiguous layout、custom hardware area 和 fallback；full KV/单粒度方案在
  quality-critical、短 context、commodity runtime 中仍成立。关系为 `Direct Evolution`。
- **ROADMAP / Decision**：Ch50 主 owner，已读 Ch43～45、Ch47～52；现有 capacity→access selection 原则
  已覆盖。`Emerging / Experimental`，不写 Books。

### Ground Truth First — 22/30

- **Source Family / Full-read Coverage**：`GROUND-TRUTH-FIRST-MEMORY-EVAL`；arXiv:2607.21962v1，
  first-public 2026-07-24；已读 longitudinal instrument、tenure crossover、memory architectures、
  baselines/metrics、sensitivity、limitations 和 appendix。
- **Evidence / Decision**：论文支持 memory ranking 可随 tenure/accumulated state 反转，说明短 horizon
  benchmark 可能误选架构；不证明某 memory architecture 普遍最优。Ch62/73/77 已读；现有 longitudinal/
  validity contract 已覆盖，`No Change — Already Covered`。

### Scaling Native Multimodal Pre-Training From Scratch — 22/30

- **Source Family / Full-read Coverage**：`NATIVE-MULTIMODAL-PRETRAINING`；arXiv:2607.22043v1，
  first-public 2026-07-24；已读 native multimodal objective/data mix、scaling/model architecture、training、
  evaluation/ablation/limitations。
- **Evidence / Decision**：作者 experiments 说明特定 data/compute recipe 从 scratch 的 scaling behavior；
  不证明优于所有 adapter/staged training、数据质量/版权已解决或 production serving cost。Ch5/23～25/
  32～37 已读；`Emerging / Experimental`。

### NVIDIA Dynamo v1.3 — 28/30

- **Source Family ID / Type / Date**：`DYNAMO-1.3-SELECTION`；GitHub v1.3.0 release
  2026-07-22，联读 docs、standalone selection/indexer design、PRs/tests/code paths。
- **Full-read Coverage**：已核对 branch-sharded KV index、runtime-free selection/reservation/scoring、
  overlap freshness/decay、topology/taints、retry/backpressure、recovery/replica sync、lower-tier weights、
  session/trajectory affinity、stable worker ID、metrics/logging 和 failure fixes。
- **Problem / Previous Design / Changed Constraint**：router 内嵌 selection 对单进程低延迟合理；多 runtime、
  多 cache tier、PD/topology 和 worker churn 使 index/selection 生命周期需要独立扩展与恢复。
- **Mechanism / Ownership / Flow**：KV events进入 branch-sharded index；selection service reconcile worker
  catalog，按 overlap/load/topology/SLA/affinity评分并 reservation；router执行 dispatch；recovery 以 bounded
  event buffer、best-effort replica sync 和 cancellation/ghost-booking防护恢复。index 是观测副本，不是 KV
  data authority；worker/engine 才拥有实际 cache state。
- **Evidence Boundary**：release/code/PR/tests 证明 v1.3 behavior；13.7% 等 micro/AgentX数字只属对应 bs64
  c384 path，不是通用吞吐。best-effort sync 表明 selection metadata 可暂时 stale，不能宣传强一致性。
- **Trade-offs / Evolution**：独立服务提高复用/可扩展性和 runtime neutrality，新增 reconciliation、stale
  scores、reservation leak、failover/backpressure、identity/security 与 decision trace。in-process selector 在
  小规模/单 runtime 仍更简单。关系为 `Direct Evolution`。
- **ROADMAP / Decision**：Ch48 主 owner，已读 Ch47～52、Ch59、Ch63、Ch77；现有 versioned control-plane
  case 已覆盖。`No Change — Already Covered`，保留 Ch48 provisional 内容。

### SGLang v0.5.16 — 27/30

- **Source Family ID / Type / Date**：`SGLANG-0.5.16-TYPED-STATE`；GitHub v0.5.16 release
  2026-07-25，联读 UnifiedRadixTree、SWA/Mamba/DSA replay/reset、HiCache/FlexKV、scheduler/kernel PRs、
  tests/code paths。
- **Full-read Coverage**：已核对 cache identity/lifecycle、recurrent state replay、used-state reset、tiered
  storage、scheduler barrier/logprob/memory fixes、compatibility和回归测试；release 功能表不直接写 Books。
- **Problem / Mechanism**：Radix/KV cache 对 standard attention prefix合理；SWA、Mamba、DSA/KDA 等模型
  同时含 window、recurrent 或其他 typed state。统一 tree 只能统一索引/lifecycle，cache hit 必须按 model-
  state type replay，rollback/retraction/reset 只触及本次实际使用的 state，并维护 generation/version。
- **Evidence Boundary / Trade-offs**：release/PR 证明该版本 implementation；不证明所有 hybrid model state
  已统一、跨 backend 完全等价或 tiered cache 无一致性问题。统一接口减少重复 infra，增加 typed validity、
  reset/rollback bugs、backend capability checks 和 recovery testing。
- **ROADMAP / Decision**：Ch47 主 owner，已读 Ch43～52；`Refine — Existing Argument` 已写入 typed
  cache identity 与 rollback contract；保留 provisional 内容。

### Nunchaku Lite in Diffusers — 23/30

- **Source Family / Coverage**：`NUNCHAKU-DIFFUSERS`；Hugging Face 2026-07-23 official engineering blog、
  package/model artifact、kernel/support matrix 与 benchmarks 已核对。
- **Evidence / Decision**：4-bit diffusion integration 证明特定 models/hardware/pipelines 可执行，数字绑定
  GPU、resolution、steps、precision 和 implementation；不证明 generic quantization speedup。Ch45/50 已读；
  `Weekly Only — Version/Product Fact`。

### OpenForgeRL — 28/30

- **Source Family ID / Type / History**：`OPENFORGE-RL`；arXiv:2607.21557v1，first-public
  2026-07-23，v2 仅在 7 月 24 日修正论文 header；本轮以 v1 HTML 为事件窗口证据。
- **Full-read Coverage**：已读 metadata、Introduction/Related Work、MDP/harness abstraction、proxy 与
  trajectory reconstruction、Kubernetes rollout orchestration、timeout/error handling、task/environment
  synthesis、Claw/GUI training contract、六个 benchmark、cross-harness analysis、behavior analysis、
  conclusion、training/data/evaluation appendices。论文没有独立 `Limitations` 章节，未披露或未评测项
  单列为 evidence boundary。
- **Original Problem / Why Previous Design Was Reasonable**：把 rollout loop 直接写进 trainer 对简单
  single-turn、轻量 tool sandbox 合理：trainer 拥有 prompt、generation、reward 与 batch barrier。但真实
  harness 自己管理多轮 Context、subagent、skills 和工具，环境还需要独立 CPU/memory/container；为训练
  重写简化 harness 会造成 train–deploy mismatch，把环境与 trainer 共置又无法安全扩展。
- **Changed Constraint / Mechanism**：OpenForgeRL 用 inference proxy 截获任意 harness 发往 policy server
  的每次 prompt/response，并在 rollout 结束后把 terminal reward 与这些 pairs 重建为标准 RL trajectory；
  Kubernetes orchestrator 为每次 rollout 创建 task-specific remote pod，使 harness/environment 生命周期与
  GPU trainer 解耦。新 harness 或 environment 的适配主要进入 sandbox image，而不是修改 RL algorithm。
- **State Ownership / Control and Data Flow**：harness 拥有运行时 Context 与 control flow；sandbox pod
  拥有 environment state；proxy 拥有请求 interception、trajectory records 与 terminal reward join；
  orchestrator 拥有 pod resource/lifecycle；veRL/policy server 拥有 optimization 与 weights。数据流是
  `trainer weights → inference server → proxy → harness in remote pod → environment → terminal reward →
  trajectory reconstruction → GRPO update`。这是一种 adapter boundary，不代表 arbitrary harness semantics
  已被形式化。
- **Timeout / Error / Credit Contract**：作者使用 wall-clock timeout，而不是不一致的“turn”上限；超时
  rollout 被终止并返回 error。network、harness crash 或 timeout 导致的部分 trajectory 整体丢弃，以避免
  正确 prefix 被错误 terminal reward 污染。这让 batch 继续推进，却损失有效 partial experience，并把
  failure attribution、retry、idempotency 与 partial credit 留作未解决问题。
- **Data and Evaluation Contract**：task synthesis 经 propose→prune→build executable environment/verifier→
  open-model test→refine；RL task 保留完整 test/refine，SFT task 为节省成本跳过并用 GPT-5.4 judge 过滤。
  Claw 用 Qwen3-30B-A3B-Thinking、892 SFT trajectories、343 RL tasks、GRPO batch/group 8/8、
  8×B200；GUI 用 Qwen3-VL-8B-Thinking、795/1,496 SFT trajectories、252/900 RL tasks，computer
  batch/group 8/8，browser 12/5。rollout pod 为 Azure D-series nodes 上 2–4 CPU、2–6 GiB，训练 32–48h。
- **What Evidence Proves**：在作者固定的 synthetic tasks、harness modifications、cloud sandbox、reward/
  judge 与 benchmark protocol 中，proxy + remote orchestration 能向标准 RL backend 提供可训练 trajectories；
  SFT+RL 对相同 backbone/SFT baseline 的多项 outcome 有提升。cross-harness table 说明 harness choice 本身
  显著改变结果，100-trajectory analysis 观察到 tool mix、自验证和 error recovery 变化。
- **What It Does Not Prove / Threats**：结果不能分离 task synthesis、teacher distillation、harness、RL 和
  evaluator 的全部因果贡献；MCPAtlas 使用 89-task credential-free subset 与 LLM judge，browser benchmarks
  又使用 o4-mini/GPT-4o scorer。论文未展示 fleet-scale failure rate、proxy backpressure、weight-version
  skew、duplicate/lost trajectory、pod isolation/security、external website drift、cost/SLO 或 crash recovery。
  “any harness/environment”是接口目标，不是对所有动态 control flow 的完备证明。
- **Trade-offs / New Failure Modes**：复用真实 harness 降低 train–deploy semantic drift，却引入 proxy
  interception correctness、request/response correlation、terminal-reward join、remote latency、straggler、
  pod/image provenance、credential/secret isolation、partial-rollout discard bias 与 harness version churn。
  每 trajectory 一个容器提高隔离性，也增加 control-plane 和 environment startup 成本。
- **Where Previous Design Still Applies / Evolution**：简单 ReAct、单工具或 verifier 便宜的任务继续适合
  trainer-owned rollout；离线 SFT/DPO 在 environment interaction 昂贵或不可逆时仍合理。演进关系是
  `Layering / Dependency`：trainer-local rollout → proxy-adapted real harness → isolated remote environment；
  下一阶段压力是 exactly-once trajectory identity、policy/harness/environment version binding、partial credit、
  recovery、multi-tenant security 与端到端 cost control。
- **ROADMAP / Adjacent Chapters / Decision**：Ch29 为训练机制 owner，Ch80 为平台 owner，已读 Ch28～30、
  Ch62、Ch77、Ch78 与 Ch80。现有章节已覆盖 on-policy rollout/version、environment/reward identity、
  durable timeout/recovery、agent run/evaluation planes 和 governed rollout。论文强化实现可行性但不新增长期
  设计结论，最终 disposition 为 `No Change — Already Covered`；现有 Workflow/Training contract 经复核保留。

### SWE-Pruner Pro — 25/30

- **Coverage / Mechanism**：`SWE-PRUNER-PRO`；arXiv:2607.18213v1，2026-07-20；已读 frozen-backbone
  hidden-state probe、length-aware pruning head、balanced focal loss、in-server KV/prefill integration、four benchmarks、
  ablations、latency 与 appendices。tool response 的 last-layer state 经小 head 产生 line-level keep/prune；当前 turn 仍看完整
  response，压缩版本在下一 turn 替换历史，避免额外 scoring model。
- **Evidence / Evolution / Decision**：两种 open-weight backbone 与四项任务支持 hidden state 含 relevance signal；不证明 closed
  models、其他语言或 safety-critical recall。external compressor → agent-conditioned scorer → reuse internal relevance state，代价是
  per-backbone retraining、false-prune 与 cache re-forward。`Refine — Existing Argument / Experimental`，Ch71 owner，Ch72 handoff。

### LLM-as-a-Coach — 23/30

- **Coverage / Mechanism**：`LLM-AS-COACH`；arXiv:2607.18110v1，2026-07-20；已读 rubric RL baseline、coach
  feedback extraction、on-policy context distillation、held-out/OOD experiments、reward-hacking analysis 与 appendix。它把 judge 的
  scalar score 改为可迁移 textual experience，再由 context-conditioned teacher 提供 token-level distillation signal。
- **Boundary / Decision**：两类 policy 与开放任务实验支持 high-bandwidth feedback，但 coach correctness、verbosity、self-coaching
  bias 和反馈 provenance 未被普遍解决。scalar reward → textual diagnosis → distilled policy；`Refine — Existing Argument /
  Experimental`，Ch29 owner，Ch76 handoff。

### FlashRT — 24/30

- **Coverage / Mechanism**：`FLASHRT-HARNESS`；arXiv:2607.18171v1，2026-07-20，v2 2026-08-10 仅作 revision
  verification；已读 chain-of-program、IR/data dependency/persistent state scope、sequential interpreter、static analyses、agent passes、
  multimodal pipelines、hardware placement/streaming evaluation、ablations 与 appendices。reference code 先被提升为可验证 IR，再搜索
  placement、streaming 与 component-specific parallelism，逐步执行 correctness checks。
- **Boundary / Decision**：作者 applications/hardware 证明 guided synthesis 可行，不证明任意 pipeline、kernel 或 SLO；agent code、IR
  semantics、interpreter equivalence 与 benchmark overfitting 是新风险。manual deployment → rule compiler → verified agent-guided
  transformation；`Refine — Existing Argument / Experimental`，Ch77 owner，Ch45/52 handoff。

### Self-State Attacks on Self-Hosted AI Agents — 25/30

- **Coverage / Mechanism**：`SELF-STATE-ATTACKS`；arXiv:2607.17986v1，2026-07-20；已读 four-axis threat model、
  23-cell/43-operation matrix、live workload traces、prevention/detection/recovery stack、residual indistinguishability 与 ethics appendix。
  合法 syscall 可破坏 instruction/config/memory；静态 access control 保护较稳定层，workload-conditioned detection 监视 memory，backup
  提供恢复，但 4/23 cells 在 OS 层与合法行为不可区分。
- **Evolution / Decision**：file permission → telemetry anomaly → semantic authorization + recoverable state；OS 不能单独判断 agent
  intent。`Refine — Existing Argument / Experimental`，Ch68 owner，Ch63/73/80 handoff。

### Stale but Stable — 26/30

- **Coverage / Mechanism**：`STALENESS-ADAPTIVE-TR`；arXiv:2607.18722v1 first-public 2026-07-21，v3 2026-07-24；
  已读 finite-horizon bound、policy/engine/MoE lag decomposition、SAT sampled log-ratio proxy、tail quantile kernel、sign-selected PPO
  endpoint contraction、reasoning experiments、ablations 与 open questions。
- **Evidence / Decision**：SAT 只收缩当前 batch 高 mismatch tail 的 outward update；作者明确它约束 sampled surrogate，不约束整个
  realized policy，`|log r|` 也不是 TV distance 或 version age。同步 rollout → fixed clipping async RL → staleness-adaptive trust
  region；新增 relative-quantile drift 与 unobserved-action risk。`Refine — Existing Argument / Experimental`，Ch29 owner，Ch34 handoff。

### AgentDebugX — 24/30

- **Coverage / Mechanism**：`AGENTDEBUGX`；arXiv:2607.18754v1，2026-07-21；已读 unified trace schema、Detect→Attribute→
  Recover→Rerun loop、DeepDebug global/structure/cross-examination、Who&When/GAIA evaluation、Error Hub、redaction、human gate 与 limits。
  append-only trace 被诊断为 agent+step root-cause candidate，再生成修复并在审批后重跑。
- **Boundary / Decision**：exact attribution 仍低且额外 calls 非总有收益；GAIA complete recipes 未隔离 attribution 因果，Error Hub 尚未
  评估。trace replay → causal hypothesis → gated repair/rerun；`Refine — Existing Argument / Experimental`，Ch65 owner，Ch76 handoff。

### AutoIndex — 24/30

- **Coverage / Mechanism**：`AUTOINDEX`；arXiv:2607.18603v1，2026-07-21；已读 representation-program DSL、validation-
  guided diagnose/synthesize/select loop、CRUMB 8 tasks、fixed BM25 controls、ablations、program cases、history 与 limitations。它不调
  retriever，而搜索 slice/enrich/normalize/reweight/reorganize document 的 executable preprocessing program。
- **Boundary / Decision**：结果主要优化 Recall@100、seed/iteration 少且 per-corpus；不能证明 transfer 到 dense/hybrid/reranker，亦未
  完整计入 index/latency cost。fixed chunking → tuned hyperparameters → executable representation program；`Refine — Existing
  Argument / Experimental`，Ch72 owner，Ch62/77 handoff。

### Tiered Optimizer State for MoE / SkewAdam — 24/30

- **Coverage / Mechanism**：`SKEWADAM-TIERED-STATE`；arXiv:2607.19058v1，2026-07-21；已读 backbone/expert/router
  state allocation、memory accounting、82M-token experiment、tier/optimizer ablations、routing stability、downstream sanity check 与 limits。
  dense backbone 保存 momentum+factored second moment，experts 只保留 factored second moment，router 保留 exact second moment。
- **Boundary / Decision**：2-layer 6.78B MoE、128 context、多数单 run，downstream near chance；论文自己说明 allocation 不是
  perplexity gain 的唯一原因。uniform optimizer state → parameter-role-specific state tiering；工程机制有价值但证据不足，`Emerging /
  Disputed — Weekly Only`，Ch31 provisional owner。

### SLAI T-Rex — 27/30

- **Coverage / Mechanism**：`SLAI-TREX`；arXiv:2607.20145v1，2026-07-22，v2 2026-07-30；已读 Ascend SuperPOD
  hierarchy、parallel/communication/kernel optimization、monitoring、solver-grounded CPT/SFT data engine、training stability、matched
  ablations、scale-up 与 appendices。system owner 从 model parallel plan 向 collective/kernel hot spots 逐层下钻；data side 以 solver
  验证 synthetic OR artifacts。
- **Boundary / Decision**：34.22% MFU / 2.93× 绑定 DeepSeek-V4-Pro、Ascend stack 和 open-source baseline recipe；不能外推
  non-GPU 普遍优势或 CPT 因果到所有领域。generic distributed recipe → hardware-aware stack → verifier-grounded specialization；
  `Refine — Existing Argument / Experimental`，Ch32 owner，Ch23/45 handoff。

### Rubric-Oriented Document Set Selection — 25/30

- **Coverage / Mechanism**：`RUBRIC-DOCSET-RETRIEVAL`；arXiv:2607.19747v1，2026-07-22；已读 three-level/nine-
  dimension rubric、28K rubrics、12 rerankers、setwise selection、short/long generation experiments、annotation/appendix。candidate set
  不再是独立 relevance 分数之和，而显式检查 coverage、redundancy、conflict 与 complementarity，再选择较小 evidence set。
- **Boundary / Decision**：rubric/judge、generator 和 curated domains 限制结论；conflict detection 并非所有场景瓶颈。pointwise
  relevance → listwise rank → set-level evidence utility；`Refine — Existing Argument / Experimental`，Ch72 owner，Ch62 handoff。

### DocOps — 23/30

- **Coverage / Mechanism**：`DOCOPS`；arXiv:2607.19865v1，2026-07-22；已读 hierarchical task taxonomy、210 native-format
  tasks、deterministic structural/content verifiers、model×harness evaluation、failure taxonomy 与 limitations。它把“生成回答”改成
  可打开、结构保持、内容正确的 artifact，并检测 long-term state、semantic verification 与 metadata destruction。
- **Boundary / Decision**：offline deterministic tasks 不覆盖 live service、collaboration、clarification；token accounting 跨 harness
  不同。Ch62 已有 executable artifact + preservation-aware verifier，故 `No Change — Already Covered / Experimental Case`。

### Decodability Supervision / RECAP — 26/30

- **Coverage / Mechanism**：`RECAP-DECODABILITY`；arXiv:2607.20379v1，2026-07-22；已读 reconstruction audit、grounded-vs-
  true cross、evaluator swap、private-code sandbox、co-trained auxiliary predictors、scale audit、reader drift、ablations 与 limits。标准
  reconstruction 可只捕捉 gist 或形成 verbalizer/reconstructor private code；RECAP 在 target model 训练时加 linear heads 保持指定
  content decodable，再由 fresh reader 验证。
- **Boundary / Decision**：synthetic sandbox、one NLA、Pythia-160M mostly single seed；decodable 不等于 verbalizable，更不等于模型
  使用该信息。post-hoc readable explanation → claim audit → training-time decodability contract；`Refine — Existing Argument /
  Experimental`，Ch5 owner，Ch62 handoff。

### ICAE-Bench — 24/30

- **Coverage / Mechanism**：`ICAE-BENCH`；arXiv:2607.21217v1，2026-07-23；已读 repository-grounded ambiguity、User Agent
  interaction、requirement reveal/revision、project construction、black-box artifact tests、models/harnesses、analysis 与 appendix。任务从
  precise repository behavior 反向生成 fuzzy intent，由 user simulator 逐步澄清，最终以 executable behavior 评分。
- **Boundary / Decision**：simulated users/curated repos 不能代表真实 product negotiation，interactive gains 混合 clarification 与 coding
  ability。static issue → evolving requirement → executable project artifact；`Refine — Existing Argument / Experimental`，Ch62 owner，
  Ch75/77 handoff。

### AREX — 28/30

- **Coverage / Mechanism**：`AREX-DEEP-RESEARCH`；arXiv:2607.21461v1 first-public 2026-07-23，v2 2026-07-24；已读 inner
  research / outer constraint audit、context-update tool、verified synthetic tasks、agentic mid-training、long-horizon RL、step-aware reward、
  benchmarks、ablation 与 appendices。verified evidence 与 unresolved constraints 被压缩为 improvement state，驱动 targeted follow-up。
- **Boundary / Decision**：作者 tasks/verifiers 支持 discovery-verification asymmetry，不证明 open-web truth、context compression 无损或
  recursive loop 不会固化错误。search longer → verify final → constraint-wise recursive repair；`Refine — Existing Argument /
  Experimental`，Ch77 owner，Ch71/72/76 handoff。

### LLMs Get Lost in Evolving User Intent — 24/30

- **Coverage / Mechanism**：`EVOLVING-USER-INTENT`；arXiv:2607.20734v1，2026-07-22；已读 backward synthesis from final
  intent、argument reveal/revision/function switch、preserved verifier、multi-domain evaluation、RL experiment、capacity/turn/length analyses
  与 limitations。static benchmark 被转成 controlled conversation，同时最终 task verifier 不变。
- **Boundary / Decision**：每 turn 单一 transition、style/persona 简化且不含多意图；下降不能直接等同真实用户失败率。single-turn final
  intent → multi-turn reveal → revision/switch-aware state tracking；`Refine — Existing Argument / Experimental`，Ch62 owner，Ch71/75 handoff。

### Sample-Efficient Learning from Agent Experience — 25/30

- **Coverage / Mechanism**：`EXPERIENCE-DISTILLATION`；arXiv:2607.21051v1，2026-07-23；已读 ICL experience collection、teacher
  target selection、context distillation without new environment calls、749 SWE tasks/six games、SFT/PPO controls、cross-case appendix 与
  limitations。先用 trial history 提升 in-context policy，再把 experience-conditioned behavior 蒸馏进 weights，部署时移除 history。
- **Boundary / Decision**：保留的是特定 cases 的部分 gains；teacher selection、rejected hypotheses、weight interference 和未来
  environment drift 未解决。transient context learning → experience curation → weight consolidation；`Refine — Existing Argument /
  Experimental`，Ch73 owner，Ch25/29 handoff。

## Expanded Candidate Review Queue

2026-08-13 exact-source recovery 已使本队列 16/16 完成全文与章节审计。保留此标题作为 discovery
closure checkpoint，不再保留伪 blocked 表；所有 disposition 见上方 Full Source Review。

### Date-corrected spillbacks

- RESOURCE2SKILL (`2606.29538`) v1 2026-06-30，已回写 W27 并完成全文、评分与 disposition。
- ReflectWorld-MM (`2607.09759`) 与 ReOPD (`2607.04763`) v1 均为 2026-07-06，已回写 W28。
- Xiaomi-Robotics-1、On-Policy Delta Distillation、Recursive Harness Self-Improvement、Muon Agentic
  RL、DSWorld、cost-aware security evaluation、SeerGuard、environment-free API data、Distilled RL、
  JoyNexus 与 DataFlow-Harness 的 primary ID 与 2026-07-16～19 v1 date 已核验并回写 W29。
- 上述 14 项完成归周后，ReOPD 与 ReflectWorld-MM 已在 W28，OPD²、Recursive Harness Self-Improvement、
  Muon Agentic RL、Xiaomi-Robotics-1、DSWorld、Cost-Aware Security Agents、SeerGuard 与 Environment-free
  API data、Distilled RL、JoyNexus 与 DataFlow-Harness 已在 W29 完成 Full Source Review 与评分；
  identity attribution 本身不等于全文、评分或 Books-ready。
- 2026-08-12 对 W29 剩余三项 attribution 的访问曾失败；2026-08-13 exact HTML recovery 已在 owner week
  完成全文与评分，RESOURCE2SKILL 也已在 W27 闭合。过程失败记录不再作为当前 blocker。
- DeepSearch-World (`2607.07820`) v1 为 2026-07-08，回归 W28；Daily Papers 的 7 月 21 日条目不是
  first-public date。

## Final Books Integration Ledger

| # | Candidate / Source Family | Final disposition | Stable owner / evidence |
| ---: | --- | --- | --- |
| 1 | Gemini 3.5 Flash Cyber | Weekly Only — Product Preview | model/harness/environment contribution 不可分离 |
| 2 | SymptomAI | Weekly Only — Domain Study | 不改变通用系统 contract |
| 3 | HiKV | Refine — Existing Argument | INFER-KV-CACHE；importance-aware access/quality budget 已覆盖 |
| 4 | Ground Truth First | No Change — Already Covered | AGENT-MEMORY；valid-time/provenance/supersession 已覆盖 |
| 5 | Native Multimodal Pre-training | Emerging / Experimental | MULTIMODAL-REPRESENTATION；既有受限分支 |
| 6 | SWE-Pruner Pro | Refine — Existing Argument | AGENT-CONTEXT；next-turn agent-conditioned pruning |
| 7 | LLM-as-a-Coach | Refine — Existing Argument | TRAIN-GRPO；textual feedback provenance/outcome Gate |
| 8 | FlashRT | Refine — Existing Argument | AGENT-WORKFLOW；IR-verified deployment synthesis |
| 9 | Self-State Attacks | Refine — New Mechanism | PLATFORM-SECURITY；self-state protect/detect/recover |
| 10 | Stale but Stable | Refine — Existing Argument | TRAIN-GRPO；staleness-adaptive sampled trust region |
| 11 | AgentDebugX | Refine — Existing Argument | PLATFORM-TRACE；gated diagnosis/recovery/rerun |
| 12 | AutoIndex | Refine — Existing Argument | AGENT-RAG；executable representation program |
| 13 | Tiered Optimizer State for MoE | Disputed / Emerging | TRAIN-OPTIMIZER；证据不足，不进长期结论 |
| 14 | SLAI T-Rex | Refine — Existing Argument | TRAIN-DISTRIBUTED-TRAINING；hardware-aware stack + verifier data |
| 15 | Rubric-Oriented Document Set Selection | Refine — New Mechanism | AGENT-RAG；set-level evidence utility |
| 16 | DocOps | No Change — Already Covered | PLATFORM-EVALUATION-SYSTEM；artifact preservation verifier 已覆盖 |
| 17 | RECAP | Refine — Existing Argument | WORLDVIEW-WHAT-NEURAL-NETWORKS-LEARN；decodability 证据边界 |
| 18 | ICAE-Bench | Refine — Existing Argument | PLATFORM-EVALUATION-SYSTEM；evolving requirement + artifact verifier |
| 19 | AREX | Refine — Existing Argument | AGENT-WORKFLOW；constraint-wise recursive repair |
| 20 | Evolving User Intent | Refine — Existing Argument | PLATFORM-EVALUATION-SYSTEM；reveal/revision/switch state |
| 21 | Agent Experience Distillation | Refine — Existing Argument | AGENT-MEMORY；context experience→weight consolidation boundary |
| 22 | OpenForgeRL | No Change — Already Covered | AGENT-WORKFLOW；rollout identity/governance 已覆盖 |
| 23 | NVIDIA Dynamo v1.3 | Refine — Existing Argument | INFER-DYNAMO；selection/index/control-plane ownership 已复核 |
| 24 | SGLang v0.5.16 | Refine — Existing Argument | INFER-SGLANG；heterogeneous state restore/rollback 已复核 |
| 25 | Nunchaku Lite | Weekly Only — Version/Engineering Fact | INFER-EXECUTION；无完整 workload contract |

计数：`Refine 17 / No Change 3 / Weekly Only 3 / Emerging 1 / Disputed 1`。25 项均已全文审计，
不存在 blocked 或普通 pending。

## Repository Changes

- 新增本 Weekly；
- 删除已被 W30 完整吸收的 `papers/2026/07/22/README.md`；
- refine `books/part-05-inference-system/51-sglang.md` 与
  `books/part-05-inference-system/52-dynamo.md`；
- HiKV、Nunchaku、Ground Truth First 与 Native Multimodal 均保留明确 disposition，
  未为产生 diff 强行写入；
- 未修改 ROADMAP 或新增章节。
- 2026-08-09 discovery replay 将 W30 从 8 个恢复为 25 个 scored source families；新增
  OpenForgeRL 全文 Source Review，并记录榜单 revision spillbacks。
- 2026-08-11 disposition review 将 16 项未读候选逐项转入 `Unverified / Blocked Backlog`；
  current-review pending 清零，forward cursor 推进 W31；未修改 Books。
- 2026-08-12 fixed-source review 确认 Dynamo v1.3、SGLang v0.5.16 与 Nunchaku Lite 的 primary-source
  packets 完整，并完成 14 个 pre-window spillbacks 的 identity/date 归属：1 项回写 W27、2 项回写 W28、
  11 项回写 W29；随后 ReOPD、ReflectWorld-MM、OPD²、Recursive Harness Self-Improvement、Muon
  Agentic RL、Xiaomi-Robotics-1、DSWorld、Cost-Aware Security Agents、SeerGuard 与 Environment-free API data
  完成 Full Source Review；当时尚余 4 项待审计。该过程状态已由下一条 2026-08-13 checkpoint 取代。
  fixed checkpoint 通过；W30 Historical Evidence Gate 当时仍因 blocked/cross-index gaps 保持 Open。
- 2026-08-13 exact arXiv HTML recovery 完成原 16 个 blocked candidates 的 metadata/revision、method、state/control
  flow、evaluation/ablation、limitations/appendix 与相邻章节审计；25/25 scored candidates 全部拥有 non-template
  Full Source Review，0 blocked、0 ordinary pending。broader discovery cross-index 与全历史 gate 尚未闭合。
- W30 Books Gate 通过后，refine `PLATFORM-SECURITY` 与 `AGENT-RAG`；Dynamo/SGLang 等既有正文经复核保留；
- 新增 25 行 final ledger；未新增 Part、章节或 Stable Node。

## Open Questions

1. standalone selection service 的一致性、failover 与 backpressure contract 是否已有正式文档？
2. branch-sharded KV index 在热点 prefix 与高 churn workload 下如何处理 skew？
3. typed model state 应由 model runner、cache manager 还是 scheduler 持有 ownership？
4. HiKV 的选择器能否在 commodity GPU 上以等质量条件获得端到端收益？
5. agentic cybersecurity benchmark 能否分离 model、harness 与 environment 的贡献？
6. routing decision trace 是否足以定位 stale-state、错误 placement 与最终 SLO failure？
7. staleness-adaptive trust region、self-state defense、IR-verified deployment synthesis、setwise evidence utility
   与 experience distillation 的独立复现会怎样改变当前受限机制边界？
8. OpenForgeRL 如何在 proxy retry、pod crash 和 policy refresh 并发时保证 trajectory 不丢、不重、不串版？
9. Tiered optimizer state 的 two-layer/single-author 证据能否由独立 MoE stack 复现，并验证 checkpoint、sharding 与 long-horizon convergence？

## Sources

> Access note：下列 expanded arXiv sources 最初于 2026-08-09 完成 identity/abstract discovery，
> 并于 2026-08-13 重新访问 arXiv HTML，完成全文、revision、evaluation 与 limitations 核验。

- [Google DeepMind — Gemini 3.5 Flash Cyber](https://deepmind.google/blog/introducing-gemini-3-5-flash-cyber/) — published 2026-07-21；accessed 2026-07-31
- [Google Research — SymptomAI](https://research.google/blog/symptomai-towards-a-conversational-ai-agent-for-everyday-symptom-assessment/) — published 2026-07-22；accessed 2026-07-31
- [HiKV](https://arxiv.org/abs/2607.22389) — submitted 2026-07-24；accessed 2026-07-31
- [Ground Truth First](https://arxiv.org/abs/2607.21962) — submitted 2026-07-24；accessed 2026-07-31
- [Scaling Native Multimodal Pre-Training From Scratch](https://arxiv.org/abs/2607.22043) — submitted 2026-07-24；accessed 2026-07-31
- [NVIDIA Dynamo v1.3.0](https://github.com/ai-dynamo/dynamo/releases/tag/v1.3.0) — released 2026-07-22；accessed 2026-07-31
- [SGLang v0.5.16](https://github.com/sgl-project/sglang/releases/tag/v0.5.16) — released 2026-07-25；accessed 2026-07-31
- [Hugging Face — Nunchaku Diffusers](https://huggingface.co/blog/nunchaku-diffusers) — published 2026-07-23；accessed 2026-07-31
- [SWE-Pruner Pro](https://arxiv.org/abs/2607.18213) — submitted 2026-07-20；accessed 2026-08-09
- [LLM-as-a-Coach](https://arxiv.org/abs/2607.18110) — submitted 2026-07-20；accessed 2026-08-09
- [FlashRT](https://arxiv.org/abs/2607.18171) — submitted 2026-07-20；accessed 2026-08-09
- [Self-State Attacks on Self-Hosted AI Agents](https://arxiv.org/abs/2607.17986) — submitted 2026-07-20；accessed 2026-08-09
- [Stale but Stable](https://arxiv.org/abs/2607.18722) — submitted 2026-07-21；accessed 2026-08-09
- [AgentDebugX](https://arxiv.org/abs/2607.18754) — submitted 2026-07-21；accessed 2026-08-09
- [AutoIndex](https://arxiv.org/abs/2607.18603) — submitted 2026-07-21；accessed 2026-08-09
- [Tiered Optimizer State for MoE](https://arxiv.org/abs/2607.19058) — submitted 2026-07-21；accessed 2026-08-09
- [SLAI T-Rex](https://arxiv.org/abs/2607.20145) — submitted 2026-07-22；accessed 2026-08-09
- [Rubric-Oriented Document Set Selection](https://arxiv.org/abs/2607.19747) — submitted 2026-07-22；accessed 2026-08-09
- [DocOps](https://arxiv.org/abs/2607.19865) — submitted 2026-07-22；accessed 2026-08-09
- [Decodability Supervision / RECAP](https://arxiv.org/abs/2607.20379) — submitted 2026-07-22；accessed 2026-08-09
- [ICAE-Bench](https://arxiv.org/abs/2607.21217) — submitted 2026-07-23；accessed 2026-08-09
- [AREX](https://arxiv.org/abs/2607.21461) — submitted 2026-07-23；accessed 2026-08-09
- [LLMs Get Lost in Evolving User Intent](https://arxiv.org/abs/2607.20734) — submitted 2026-07-22；accessed 2026-08-09
- [Sample-Efficient Learning from Agent Experience](https://arxiv.org/abs/2607.21051) — submitted 2026-07-23；accessed 2026-08-09
- [OpenForgeRL](https://arxiv.org/abs/2607.21557) — submitted 2026-07-23；accessed 2026-08-09

## 2026-08-13 Source-Family Books Integration

Scaling Native Multimodal Pre-Training From Scratch 的 final disposition 为 `Emerging / Experimental`：Owner `MULTIMODAL-REPRESENTATION`，Current Ch23，Legacy N/A；其受限证据只用于说明 native multimodal representation 会把 data/compute mix 纳入 backbone training contract，不保留作者 recipe 或 benchmark 为通用结论。Archive Completion Gate 仍 Open。
