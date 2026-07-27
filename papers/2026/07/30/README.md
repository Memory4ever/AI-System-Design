# AI Research Daily — 2026-07-30

> Research window: 2026-07-28 至 2026-07-30（重点核验过去 24～48 小时）
>
> Accessed: 2026-07-30（Asia/Shanghai）
>
> Scope: 官方 Research / Blog / model card、primary research papers、官方工程文档、
> RFC、重要 PR 与 GitHub Releases。
>
> Organization: 模型与研究机构 → arXiv 论文 → AI Infra 与工程项目

## Executive Summary

本轮没有发现过去 24～48 小时内、能够改变本书模型设计结论的一线模型机构正式研究发布。
主要长期信号来自三篇已核验正文的 arXiv 预印本：

1. **RARG** 把 relevance 从 top-k content filter 扩展为 corpus interaction 的
   execution prior：它不仅决定哪些文档进入候选集，还决定搜索从哪里开始、文档按什么
   顺序遍历，以及哪些局部 matches 在 observation 截断时仍可见。该机制已吸收到第 72 章。
2. **CodeNib** 把 coding-agent context 视为 data-system serving 问题：repository commit
   是 immutable base data，lexical、dense、structural artifacts 是具有不同更新语义的
   derived views。稳定结论是不同 view 必须保留 operation-specific validity boundary，
   该机制已吸收到第 71 章。
3. **Reinforcement Learning for Code Optimization** 说明“verifiable reward”仍可能被
   measurement noise、reward sparsity 与 environment drift 破坏。Sandbox、calibration、
   reward transformation 与 policy update 构成同一个训练接口，该结论已吸收到第 29 章。

三项内容都属于认知框架 refinement，而不是版本事实追加；均保留
`Status: Experimental`，不把作者 benchmark 外推为通用结论。Shieldstral 作为
policy-adaptive multimodal safety classifier 值得持续观察，但单篇模型论文尚不足以改变
Safety 或 Evaluation 章节。

基础设施侧没有新的高信号 release。vLLM `v0.26.0` 已在前一日日报和第 46 章处理；
`llama.cpp` 7 月 29 日连续构建只包含局部 sampling/security maintenance，未形成新的长期
系统机制。

## Candidate Scoring

评分维度均为 `0～5`：Technical Novelty（TN）、System Impact（SI）、Practical Value（PV）、
Source Reliability（SR）、Project Relevance（PR）、Longevity（L）。

| Candidate | TN | SI | PV | SR | PR | L | Total | Decision |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| RARG：relevance as execution prior | 5 | 4 | 4 | 3 | 5 | 5 | 26/30 | Must Read；吸收进第 72 章 |
| CodeNib：multi-view repository context serving | 4 | 5 | 4 | 3 | 5 | 5 | 26/30 | Must Read；吸收进第 71 章 |
| RL for Code Optimization：noisy reward interface | 4 | 5 | 4 | 3 | 5 | 5 | 26/30 | Must Read；吸收进第 29 章 |
| Shieldstral | 3 | 4 | 4 | 4 | 4 | 4 | 23/30 | Worth Watching；Daily only |
| llama.cpp `b10182` continuous build | 1 | 2 | 2 | 5 | 2 | 1 | 13/30 | Ignored Noise |

## 1. 模型与研究机构

### Source Coverage

按固定顺序检查官方 Research/Publications、技术 Blog、model/system card、官方
GitHub/Hugging Face organization 与 technical report，并对跨入口内容去重。

| Institution | Window result | Decision |
| --- | --- | --- |
| OpenAI | 7 月 27 日 task-crossover 研究已记录于 7 月 28 日日报 | Deduplicated |
| Anthropic | 无达到门槛的一手更新 | No Material Update |
| Apple Machine Learning Research | 无达到门槛的一手更新 | No Material Update |
| Google DeepMind | Gemini 3.5 Flash Cyber 发布于 7 月 21 日，超出窗口 | Ignored Old Reappearance |
| Google Research | 最新保留项超出窗口 | No Material Update |
| Meta AI / FAIR | 无窗口内官方 Research 更新；code-optimization 论文在 arXiv 组处理 | No Material Update |
| Microsoft Research | 无达到门槛的一手更新 | No Material Update |
| NVIDIA Research | 无达到门槛的一手更新 | No Material Update |
| xAI | 最新 model/news 更新超出窗口 | No Material Update |
| Amazon Science / AGI | 最新 publication 超出窗口 | No Material Update |
| Cohere Labs | 无达到门槛的一手更新 | No Material Update |
| Ai2 | 无达到门槛的一手更新 | No Material Update |
| Mistral AI | 官方 Blog 无窗口内更新；Shieldstral 在 arXiv 组处理 | No Material Update |
| Alibaba Qwen | 最新 Qwen Code weekly 超出窗口 | No Material Update |
| DeepSeek | 官方 API changelog 无窗口内更新 | No Material Update |
| Moonshot AI / Kimi | Kimi K3 已记录于 7 月 29 日日报 | Deduplicated |
| Zhipu AI | 无达到门槛的一手更新 | No Material Update |
| MiniMax | 官方 News 无窗口内技术研究更新 | No Material Update |
| ByteDance Seed / Research | 官方 Research 入口无窗口内更新 | No Material Update |
| Baidu ERNIE | 无达到门槛的一手更新 | No Material Update |
| Tencent Hunyuan | 无窗口内官方模型/系统更新；RARG 在 arXiv 组处理 | No Material Update |
| Huawei Noah's Ark Lab / Pangu | 无达到门槛的一手更新 | No Material Update |
| Shanghai AI Laboratory / InternLM | 无达到门槛的一手更新 | No Material Update |
| StepFun | 无达到门槛的一手更新 | No Material Update |
| Xiaomi MiMo | 无达到门槛的一手更新 | No Material Update |
| InclusionAI / Ant Group | 无达到门槛的一手更新 | No Material Update |
| Hugging Face Blog | 最新官方文章超出窗口；社区文章不作为最终证据 | No Material Update |

### Evidence Level

- **官方事实**：上述日期与 release 状态来自各机构官方入口。
- **尚未验证**：部分国内机构页面缺少稳定的按日期索引；“无重要更新”只表示本轮在官方
  可发现入口中未识别到达到门槛的内容，不证明机构没有任何内部或未索引发布。
- **Recommended Action**：不修改模型章节，不重复记录 Kimi K3 或 OpenAI task crossover。

## 2. arXiv 论文

### Source Coverage

按顺序检查 arXiv `cs.AI`、`cs.CL`、`cs.LG`、`cs.DC`、`cs.IR`、`stat.ML` recent；
对 `cs.SE`、`cs.CV`、`cs.CR`、`cs.OS` 等分类按 Coding Agent、multimodal safety、
Agent runtime 与 systems 关键词过滤。

OpenReview / TMLR 未发现窗口内、状态明确且比下列论文更相关的 Accepted 项。
Hugging Face Daily Papers 用于 discovery；Semantic Scholar、Google Scholar、OpenAlex
与 DBLP 用于 related-work、metadata 与去重检查。三个新预印本尚未在这些新鲜索引中形成
稳定的独立 metadata match，因此日期、作者和版本全部回到 arXiv 原文核验。
Crossref 仅用于 Weekly 或 metadata 冲突；本轮没有 DOI / venue / version 冲突，不触发。

### RARG — Must Read：Relevance 从内容过滤器变成执行先验

- Source: primary research paper / arXiv
- Submitted: 2026-07-27 09:56 UTC
- Accessed: 2026-07-30
- URL: https://arxiv.org/abs/2607.24223
- Score: 26/30
- Status: Experimental
- Category: Agentic Search / RAG / Direct Corpus Interaction

#### Why

一次性 top-k retrieval 能高效缩小 corpus，却可能在 snippet truncation 时丢失决定性 span，
也不能随中间实体的发现动态组合证据。Direct Corpus Interaction 允许 Agent 使用 grep 与
局部 read 精确探索，但 relevance-agnostic traversal 会让有用 clues 出现过晚，并把有限的
tool/observation budget 消耗在 distractors 上。

#### Principle

Relevance 是 evidence utility 的不完美 prior。它既可用于：

```text
selection prior: what enters a candidate space
```

也可用于：

```text
execution prior:
where interaction starts
+ which documents are traversed first
+ which local matches stay visible
```

第二种用法保留 direct interaction 的高分辨率，同时减少无方向探索；它不把 relevance
提升为事实、充分证据或授权。

#### Mechanism

RARG 先用 embedding retriever 把文档路径写入排序后的 scope file，再让 `ripgrep` 按该
路径顺序单线程遍历，使 document-level relevance 进入 execution order。RARG+ 额外返回
少量 query-relevant paragraphs 作为 entry point；RARG++ 再结合全局 scope query 与局部
grep pattern，对更大的 match pool rerank，使低排名文档中的高价值 excerpt 仍能进入有限
observation。

#### Trade-off

- 相比 top-k-only retrieval，它保留原文交互，但增加 embedding、scope 和 reranking 状态。
- 相比 unrestricted grep，它减少低价值 traversal，但强制单线程扫描会牺牲 raw search
  parallelism。
- Entry-point paragraphs 可加速起步，也可能锚定错误方向。
- Match reranking 改善 observation selection，却引入额外 GPU/latency 成本和 query
  construction 偏差。

#### Connection

```text
第 71 章 Context selection
→ 第 72 章 RAG retrieval / rerank / packing
→ Agentic Search 的 iterative evidence interaction
→ 第 62、80 章 Evaluation 与 Agent Platform
```

#### Evolution

top-k retrieval
→ retrieval-constructed interaction space
→ direct corpus interaction
→ relevance-aware interaction order and observation
→ future learned routing with provenance and authorization constraints

#### Evidence Level

**论文实验结论**：作者在 100-query BrowseComp-Plus、100K-document corpus 上，以
GPT-5.4-mini（medium effort）、Qwen3-Embedding-4B、单张 H20 GPU、最多 100 turns 的
设置报告：RARG++ 为 `84%` accuracy、平均 `23.9` tool calls；RISE 为 `78% / 28.7`，
DCI 为 `78% / 99.1`。扩展到 1M documents 时，作者报告 RARG++ `79%`、RISE `69%`。
这些数字绑定该 corpus、模型、embedding、tool budget、output truncation 和 judge；
不是通用 RAG 收益。

**尚未验证**：独立复现、开放 Web/动态 corpus、不同 embedding 与并发/SLO 条件下的收益，
以及 relevance errors 是否会形成新的 systematic blind spot。

#### Knowledge Tree Position

主位置为 Part VI 第 72 章 RAG；相邻连接第 71 章 Context 与第 80 章 Agent Platform。

#### Recommended Action

已 refine 第 72 章，增加“Relevance 也可以是执行先验”。只写入 Why、Mechanism、
Trade-off 和证据边界，不写入具体 RARG API 或 benchmark headline。

### CodeNib — Must Read：Repository Context 是 multi-view serving 问题

- Source: primary research paper / arXiv
- Submitted: 2026-07-28 08:25 UTC
- Accessed: 2026-07-30
- URL: https://arxiv.org/abs/2607.25431
- Score: 26/30
- Status: Experimental
- Category: Coding Agent / Context Serving / Data Systems

#### Why

Coding Agent 会在同一 evolving repository 上反复执行 lexical search、dense retrieval、
symbol navigation 与 source reads。若每个 task 都重新发现，build/index 成本被重复支付；
若无条件复用，又可能把不同 commit、不同 operation 或 stale derived state 混在一起。

#### Principle

把 repository 看成 authoritative base data：

```text
commit
→ lexical / dense / structural derived views
→ view-specific queries
→ bounded context delivery
```

Derived views 可以共享 source identity，但不能共享一个模糊的“fresh”标记。正确性依赖
operation-specific validity：vector reuse、graph repair、static navigation 和 prompt
compaction 必须分别证明适用边界。

#### Mechanism

CodeNib 为每个 commit 构建 lexical、dense 与 structural views，把结果映射回
repository-relative source ranges；manifest 记录 artifact path、commit、configuration、
status 和 supported operations。不同 view 通过各自的增量路径维护，runtime 再按 search、
navigation 或 bounded-context 请求选择相应 view。

#### Trade-off

- Precompute/reuse 降低重复 discovery，却增加 build、storage、manifest 和 invalidation 成本。
- Static views 可降低部分查询 latency，但不完整覆盖 live language-server semantics。
- 多 view 提高 evidence diversity，也让 routing、freshness 和 cost accounting 更复杂。
- Context compaction 可减少 trajectory tokens，但其质量/成本 operating point 依赖模型，
  不是统一最优策略。

#### Connection

```text
第 71 章 Context assembly / identity
→ 第 72 章 lexical + dense retrieval
→ 第 79 章 MCP delivery
→ 第 80 章 Agent runtime and evidence plane
```

#### Evolution

task-local grep/read
→ disconnected reusable indexes
→ source-aligned multi-view context serving
→ concurrent publication, recovery and cost-based routing

#### Evidence Level

**论文实验结论**：作者使用 25 个 repositories 的 100 个 snapshots；本地 inference 通常为
单张 NVIDIA H100 PCIe 80 GB，CPU 实验为两颗 Intel Xeon Gold 5416S，FAISS 单线程。
只有在增量结果与 independent rebuild 匹配的 transitions 上，作者报告 graph/vector
median update speedup 为 `8.67× / 25.44×`。1,000 个 navigation requests 中只有
`632` 个 normalized location sets 与 live provider 匹配；`4.72×` 只是这个兼容子集上的
warm marginal live/static latency ratio，不是端到端 workload speedup。五个模型的
context-policy 实验使用 frozen top-10 candidates、16-turn cap，报告相对 paired
grep/read 减少 `50%～87%` provider-reported trajectory tokens；cache-adjusted cost 和
Prefill latency 未测。

**尚未验证**：concurrent updates、atomic publication、multi-tenancy、recovery、learned
online scheduling 和真实 SWE task resolution gain。论文自己也把这些列为下一系统边界。

#### Knowledge Tree Position

主位置为 Part VI 第 71 章 Context；第 72、79、80 章是相邻消费者。

#### Recommended Action

已 refine 第 71 章，增加 derived-view lifecycle 与 operation-specific validity boundary。
不把 CodeNib 作为通用组件推荐，不写入条件不足的性能数字。

### Reinforcement Learning for Code Optimization — Must Read：Measurement 是 Reward Interface

- Source: primary research paper / arXiv
- Submitted: 2026-07-28 16:52 UTC
- Accessed: 2026-07-30
- URL: https://arxiv.org/abs/2607.25970
- Score: 26/30
- Status: Experimental
- Category: GRPO / RLVR / Code Optimization / Evaluation Environment

#### Why

Correctness verifier 通常给出相对稳定的 pass/fail。把 execution time 直接加入 reward 看似
只是增加一个 objective，实际上会同时引入 measurement noise、service drift、threshold
fragility、reward sparsity 和更多 all-equal groups。若更快程序的真实差异小于 timing
noise，GRPO 会把随机排序当成 advantage。

#### Principle

当 environment observation 决定 reward 时：

```text
policy
→ sandbox measurement
→ reward transformation
→ advantage
→ gradient
```

Measurement system 就是 training interface。它的 hardware、load、sandbox version、
timeout、aggregation、calibration 与 drift 都必须进入 experiment identity。

#### Mechanism

论文先构造能放大正确实现之间 duration 差异的 optimization tests，并校准 execution
sandbox；再比较 correctness/optimization 的 gated、additive、multitask 与 ranking
rewards。上线昂贵 GRPO 前，作者用 stored calibrated durations 和 sampled human solutions
运行轻量 offline simulator，筛掉 reward 太 sparse、too saturated、too flat 或 too noisy
的 environment configurations。

#### Trade-off

- 更长、更可区分的 tests 提高 signal-to-noise，却提高 rollout execution 成本。
- Binary/bucketed reward 可过滤部分 timing noise，但丢失细粒度差异。
- Reference ranking 提供相对尺度，却引入 stored-duration drift 与 calibration lifecycle。
- Offline simulator 能降低搜索成本，但只模拟 environment 对 stronger samples 的响应，
  不模拟 policy 如何学习，不能替代 online RL。
- Same-prompt、same-time grouping 可减弱难度差异和短期 drift，不能消除 shared sandbox
  bias 或长期环境变化。

#### Connection

```text
第 27 章 reward specification
→ 第 29 章 group-relative advantage
→ execution sandbox / rollout system
→ 第 62 章 Evaluation identity and uncertainty
```

#### Evolution

correctness-only RLVR
→ naive correctness + timing reward
→ calibrated environment + robust reward mapping
→ offline screening + online GRPO
→ continuously monitored reward services

#### Evidence Level

**论文实验结论**：DMC-Optim 来自 12,275 个 raw problems，保留 2,723 个 cleaned problems，
并构造 430,215 个 correctness tests 与 352,740 个 optimization tests。作者报告在其
`top-50% pass@1` 定义下，Qwen 2.5 7B 从 `18.0%` 提升到 `31.3%`，CWM 32B 从
`30.7%` 提升到 `50.4%`；online RL 使用每次 `8～32` GPU nodes、持续数小时到数天，
offline simulator 则是单 CPU node、分钟级筛选。论文未给出可外推为通用 code-serving
latency 的硬件/SLO 结论；这里只把数字视为作者在该数据、sandbox、reward 与模型条件下的
训练实验。

**尚未验证**：独立复现、跨语言与真实生产 workload 泛化、不同 cluster load 下的
calibration 稳定性，以及 simulator diagnostics 对其他 reward domains 的预测力。

#### Knowledge Tree Position

主位置为 Part III 第 29 章 GRPO；相邻连接第 27、28、30 章和 Part V 第 62 章。

#### Recommended Action

已 refine 第 29 章，明确 verifiable reward 仍包含 measurement system，并增加 noisy
continuous reward 的诊断与实验顺序。不复制 paper recipe，不把 code timing 结论外推到
所有 GRPO。

### Shieldstral — Worth Watching

- Source: primary research paper / arXiv
- Submitted: 2026-07-28 15:27 UTC
- Accessed: 2026-07-30
- URL: https://arxiv.org/abs/2607.25857
- Score: 23/30
- Status: Experimental

论文提出 3B policy-adaptive multimodal safety classifier，把 heterogeneous moderation
taxonomies 统一为 policy-conditioned binary QA，并报告约 54.1M curated/generated
samples。它说明“小型专用 classifier + runtime policy”可能比把 moderation 固定在一个
taxonomy 中更易演化。

当前只核验到论文原文与作者实验，尚无独立复现，也未验证 policy translation、跨语言
calibration、拒绝边界或生产 false-positive/false-negative cost。现有第 68 章已覆盖
policy enforcement、model output 非授权与分层安全控制；单篇模型报告尚不足以改变核心
结论。因此保留 Daily，等待 model card、weights、evaluation artifacts 或第三方复现。

## 3. AI Infra 与工程项目

### Source Coverage

按固定顺序检查官方 Releases、Release Notes、文档、RFC 与重要 PR：

| Project | Latest verified signal | Decision |
| --- | --- | --- |
| PyTorch | `v2.13.0` 发布于 7 月 8 日 | Outside Window |
| JAX | 无窗口内高信号正式 release | No Material Update |
| CUDA | 无窗口内高信号正式 release | No Material Update |
| Triton | 无窗口内高信号正式 release | No Material Update |
| vLLM | `v0.26.0` 发布于 7 月 27 日，已在 7 月 29 日处理 | Deduplicated |
| SGLang | `v0.5.16` 发布于 7 月 25 日 | Outside Window |
| NVIDIA Dynamo | `v1.3.0` 发布于 7 月 22 日 | Outside Window |
| TensorRT-LLM | latest stable `v1.2.1` 超出窗口 | No Material Update |
| Ray | `2.56.1` 发布于 7 月 17 日 | Outside Window |
| KServe | `v0.19.0` 发布于 6 月 14 日 | Outside Window |
| Kubeflow | 无窗口内高信号正式 release | No Material Update |
| Kubernetes | 无窗口内 AI System 机制更新 | No Material Update |
| Hugging Face Transformers | latest `v5.14.1` 发布于 7 月 16 日 | Outside Window |
| Hugging Face Accelerate | latest `v1.14.0` 发布于 6 月 11 日 | Outside Window |
| DeepSpeed | latest `v0.19.2` 发布于 6 月 16 日 | Outside Window |
| Megatron-LM | latest Core `0.18.2` 发布于 7 月 21 日 | Outside Window |
| Unsloth | 无窗口内高信号正式 release | No Material Update |
| MLX | 无窗口内高信号正式 release | No Material Update |
| llama.cpp | `b10182` 于 7 月 29 日发布 | Ignored Continuous Build |
| ONNX Runtime | 无窗口内高信号正式 release | No Material Update |
| OpenXLA | 无窗口内高信号正式 release | No Material Update |

### llama.cpp `b10182` — Ignored Noise

官方 release 记录 `suppress_tokens` sampling handling 的内部移动、删除旧字段与未展开的
security maintenance。它是项目连续构建的一部分，没有 RFC、行为迁移说明或足以形成
长期 AI System 结论的机制变化。安全问题描述缺少威胁模型、受影响版本和 advisory，
因此既不猜测影响，也不写入书稿。

### Evidence Level

- **官方事实**：release tag、时间与摘要来自各项目官方 GitHub Release 页面。
- **工程判断**：版本活跃不等于知识树发生变化；连续 build 和 model-support list 默认不
  进入长期知识库。
- **尚未验证**：未展开的 llama.cpp security note 是否会产生独立 advisory；若后续出现
  CVE、threat model 或 migration guidance，再触发复核。

## Books Integration

### Integration Decision

按日报顺序逐项定位 ROADMAP 节点并阅读目标与相邻章节：

| Candidate | Existing coverage | Update type | Integration |
| --- | --- | --- | --- |
| RARG | 第 72 章已有 retrieval、rerank、packing，但缺少 relevance 对 interaction execution 的作用 | 认知框架更新 | Refine 第 72 章 |
| CodeNib | 第 71 章已有 assembly、identity、cache，但缺少 heterogeneous derived-view lifecycle | 机制与工程边界补全 | Refine 第 71 章 |
| RL for Code Optimization | 第 29 章已有 reward/verifier 与 all-equal groups，但 measurement noise 尚未成为训练接口 | 机制与实验设计补全 | Refine 第 29 章 |
| Shieldstral | 第 68、62 章已有 safety policy 与 evaluation framework | 单模型事实更新 | Daily only |
| llama.cpp `b10182` | 既有 sampling/edge runtime 原则未变化 | 版本维护事实 | Ignored |

三项书稿更新没有改变 ROADMAP 结构，也没有推翻既有结论。它们把已有判断扩展为：

- Context 不只是一段文本，也可能是从具有不同 validity contract 的派生视图交付出的
  bounded result。
- Retrieval relevance 不只控制进入 Context 的内容，也可在 Agentic Search 中控制
  interaction order 和 observation budget。
- Verifiable reward 的 measurement environment 本身会被 policy 优化，必须进入训练
  identity、calibration 与 drift control。

因此同步更新 `docs/LEARNING_STATE.md`。本轮没有重大结构决策，不更新
`docs/DECISIONS.md`。

## Recommended Action

- **已完成**：第 71 章加入 Context Serving 的 derived-view lifecycle 与
  operation-specific validity boundary。
- **已完成**：第 72 章加入 Agentic Retrieval 中 relevance-as-execution-prior 的机制与
  适用边界。
- **已完成**：第 29 章加入 noisy continuous reward 的 measurement、calibration、
  sparsity 与 drift 原则。
- **已完成**：同步更新 `docs/LEARNING_STATE.md` 的 Part III 与 Part VI 稳定认知。
- **继续观察**：Shieldstral 的 model card、weights、policy adaptability evaluation 和
  第三方复现。
- **不处理**：不为模型机构“无更新”制造书稿变化，不追加 llama.cpp continuous build。

## Ignored Noise

- Google DeepMind Gemini 3.5 Flash Cyber 页面日期为 2026-07-21，属于旧内容重现。
- StateAct 在 Hugging Face Daily Papers 于 7 月 28 日获得关注，但 arXiv 首次提交为
  2026-07-24，超出 72 小时窗口；它的 state-grounding / finish-gate 机制可留待 Weekly，
  不伪装成当日新论文。
- Hugging Face community articles 的热度、upvote 与作者评论只作为 discovery signal。
- 模型榜单、缺少 workload/hardware/SLO 约束的性能 headline、普通媒体与转载均未进入。
- `llama.cpp` 高频自动 release 不按 tag 数量累积为系统趋势。

## Repository Changes

本次运行修改：

- `papers/2026/07/30/README.md`
- `books/part-06-agent/71-context.md`
- `books/part-06-agent/72-rag.md`
- `books/part-03-training-system/29-grpo.md`
- `docs/LEARNING_STATE.md`

未新增孤立 chapter，未修改 `ROADMAP.md` 或 `docs/DECISIONS.md`，未执行 commit、push 或
破坏性 Git 操作。

## Open Questions

1. RARG 的 execution prior 在 embedding 排名系统性偏置、动态 Web corpus 或多租户 ACL
   下是否仍能改善 search convergence？
2. CodeNib 的 per-view validity contract 如何扩展到 concurrent edits、atomic publication、
   recovery 与跨 tenant cache isolation？
3. Noisy reward service 是否需要像 production dependency 一样提供 calibration SLO、
   sentinel suite、versioned reference durations 与 quarantine policy？
4. Shieldstral 的 policy adaptability 是训练时覆盖多 taxonomy，还是能在运行时可靠适配
   unseen policy？False-positive/false-negative cost 如何按业务风险校准？
5. `llama.cpp b10182` 的 “address security issues” 是否会补充正式 advisory、受影响版本和
   migration guidance？

## Sources

访问日期均为 2026-07-30。

### Model and Institution Sources

- OpenAI Research: https://openai.com/research/index/
- Google DeepMind News: https://deepmind.google/discover/blog/
- Google DeepMind, Gemini 3.5 Flash Cyber, published 2026-07-21:
  https://deepmind.google/blog/introducing-gemini-3-5-flash-cyber/
- Meta AI Blog: https://ai.meta.com/blog/
- Mistral AI News: https://mistral.ai/news/
- Hugging Face Blog: https://huggingface.co/blog
- ByteDance Seed Research: https://seed.bytedance.com/research
- MiniMax News: https://www.minimax.io/news

### Paper Primary Sources

- Jiangnan Li et al., “A New Role for Relevance: Guiding Corpus Interaction in
  Agentic Search”, submitted 2026-07-27:
  https://arxiv.org/abs/2607.24223
- Zhongming Yu et al., “CodeNib: A Multi-View Data System for Serving Repository
  Context to Coding Agents”, submitted 2026-07-28:
  https://arxiv.org/abs/2607.25431
- Pierre Chambon et al., “Reinforcement Learning for Code Optimization”,
  submitted 2026-07-28:
  https://arxiv.org/abs/2607.25970
- Antonia Calvi et al., “Shieldstral”, submitted 2026-07-28:
  https://arxiv.org/abs/2607.25857
- StateAct, submitted 2026-07-24:
  https://arxiv.org/abs/2607.22798
- Hugging Face Daily Papers, 2026-07-28:
  https://huggingface.co/papers/date/2026-07-28
- Hugging Face Daily Papers, 2026-07-29:
  https://huggingface.co/papers/date/2026-07-29
- OpenReview / TMLR submissions:
  https://openreview.net/submissions?venue=TMLR

### AI Infra Primary Sources

- PyTorch `v2.13.0`, released 2026-07-08:
  https://github.com/pytorch/pytorch/releases/tag/v2.13.0
- vLLM `v0.26.0`, released 2026-07-27:
  https://github.com/vllm-project/vllm/releases/tag/v0.26.0
- SGLang `v0.5.16`, released 2026-07-25:
  https://github.com/sgl-project/sglang/releases/tag/v0.5.16
- NVIDIA Dynamo `v1.3.0`, released 2026-07-22:
  https://github.com/ai-dynamo/dynamo/releases/tag/v1.3.0
- KServe `v0.19.0`, released 2026-06-14:
  https://github.com/kserve/kserve/releases/tag/v0.19.0
- Ray `2.56.1`, released 2026-07-17:
  https://github.com/ray-project/ray/releases/tag/ray-2.56.1
- Hugging Face Transformers `v5.14.1`, released 2026-07-16:
  https://github.com/huggingface/transformers/releases/tag/v5.14.1
- llama.cpp `b10182`, released 2026-07-29:
  https://github.com/ggml-org/llama.cpp/releases/tag/b10182
