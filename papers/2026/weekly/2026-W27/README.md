# AI Research Weekly — 2026-W27

> Coverage Window: 2026-06-29～2026-07-05（完整 ISO week，Monday～Sunday）
> Research Mode: Retrospective Backfill
> Accessed: 2026-07-31
> Backfilled: 2026-07-31
> Discovery Review Reopened: 2026-08-09
> Re-audit Status: 34/34 score rows and 33/33 unique candidate families have final Books dispositions; 21 Refine, 7 No Change, 5 Weekly Only, plus one duplicate Seed2.0 score row; W27 Source-Family Books Gate passed and cursor advances to W28; broader Archive/Discovery Gate remains Open

## Executive Summary

本周没有发现需要以“新模型发布”写入 Books 的模型机构事件。最值得保留的证据来自三篇
系统与模型机制论文：

1. asynchronous Pipeline Parallel 研究把同步 bubble、固定一步 gradient delay、optimizer
   敏感性与 error-feedback correction 放进同一条演进链；
2. ELDR 把 PD-disaggregated MoE serving 的 Decode routing 从“只看负载”推进到同时考虑
   expert working-set locality；
3. HiLS-Attention 把 sparse-attention chunk retrieval 放进语言模型目标共同训练，说明长上下文
   稀疏化的关键不只是减少访问量，还要让选择器与下游计算共同承担错误。

6 月 30 日的 GeneBench-Pro、TabFM 与 Seed2.0 Model Card 分别提供 agent evaluation、
tabular foundation model 和 real-world model evaluation 的官方证据；6 月 29 日的
Brain2Qwerty v2 展示非侵入式 brain-signal decoding 的垂直进展。它们值得保留，但证据主要
来自发布方，且没有改变本书的通用系统结论。

扩展 discovery replay 又恢复 22 个窗口内评分行。它们把本周主线从三个孤立机制扩展为四条相互
连接的系统压力：把自然语言 specification 编译为可版本化 neural artifact；把 Agent memory 从
无限 transcript 改成 bounded typed retrieval 或可学习 memory action；把长程 Agent evaluation 拆成
过程、结果、环境与交互成本；以及把 outcome-only reward 细化为 tool contribution、Q-alignment 与
role-typed credit。经精确 identity 重试，Program-as-Weights 与其余 20 个可访问 scored families、
RESOURCE2SKILL 均完成全文、关键 Appendix、evaluation/limitations 与章节邻接；AgenticSTS 的 arXiv
HTML、Appendix、公开代码与轨迹数据亦于 2026-08-13 恢复，当前已无 source-level blocked family。

Google DeepMind 于 7 月 2 日建立的 overthinking publication page 对应 2025-10-09 首次公开的
arXiv 论文和 ACL 2026 正式发表节点，不是本周首次公开研究。本周因此只记录 publication-state
变化，不把旧思想重写成新进展。

fixed-source replay 进一步恢复两项 7 月 3 日以前的官方工程证据。NVIDIA Secure Agent Workspace
Reference Design 把长期 Agent 的风险边界从“模型是否拒绝”推进到 workspace identity、signed policy、
credential proxy、action approval 与 audit evidence 的联合 contract；TensorRT Edge-LLM v0.9.0 则只证明
特定 edge runtime 在该版本增加模型、硬件与音频/推理路径支持。前者已进入 `AGENT-PLATFORM` 的 secure
workspace lifecycle，后者保持 `Version Fact / Mechanism Not Disclosed`，没有获得 Books 机制 owner。

## Coverage Window and Limitations

- 本报告覆盖完整 ISO week：2026-06-29（Monday）至 2026-07-05（Sunday），不因跨月或
  回填批次边界截断。
- 6 月 29、30 日按 primary-source 首次发布日期进入候选评分，证据直接保留在 Weekly；
  完成整合后不再保留历史 Daily。
- 7 月 1 日 ELDR 曾触发高分事件 Daily；其机制、证据边界与 Books 决策经本次覆盖审计确认
  已完整进入 W27，因此不再保留独立历史 Daily。
- Google Scholar、Semantic Scholar、OpenAlex、DBLP 与 Hugging Face Daily Papers 只用于
  discovery、作者/机构和版本核对；日期与技术结论回到官方页面和 arXiv。
- 搜索入口无法证明每个机构“没有发布”；`No Material Update` 只表示在固定公开入口中
  未发现达到本项目门槛且日期可核验的内容。
- 论文 benchmark 若摘要未披露模型、硬件、输入输出长度、并发、精度和 SLO 全部条件，
  只保留作者实验结论，不外推到生产系统。
- Hugging Face display week 包含 6 月 28 日及更早论文；Agentic Abstention、Dockerless、
  PhysisForcing、Qwen-Image-2.0-RL、TUA-Bench、Multi-Block DLM、Evolution Fine-Tuning、
  OSWorld 2.0、DiscoBench 与 GBC 均按 arXiv v1 回拨 W26，不以推荐日伪造 W27 事件。

## Discovery Recall Ledger

| Ledger Item | Current Count | Review Result |
| --- | ---: | --- |
| Score rows | 34 | 24 high、10 mid、0 low；Seed2.0 两行共享 source family |
| Unique candidate families / review packets | 33 / 33 | Seed2.0 两个评分行共享一个 packet；全部 unique families 完成 Full Source Review |
| Completed / Unverified backlog | 33 / 0 | recovered scored families、RESOURCE2SKILL 与 AgenticSTS 均已审完 |
| Expanded academic discovery | Checkpoint landed | HF display feed 已按 arXiv v1 重新归周；citation/venue replay 仍开放；fixed official/Infra replay 已通过 |
| W27 post-forward Candidate Gate | Passed | 33/33 unique `20+` Full Source Reviews；0 ordinary pending；0 blocked；cursor advances W28 |
| W27 discovery / Historical Evidence Gate | Open | 更广 citation/venue discovery 尚未闭合；fixed-source replay 已通过 |

## 1. 模型与研究机构

### Source Coverage

按固定顺序扫描：

| Order | Sources | Result |
| --- | --- | --- |
| 1–5 | OpenAI；Anthropic；Apple ML Research；Google DeepMind；Google Research | OpenAI GeneBench-Pro 与 Google TabFM 均发布于 6 月 30 日；Google DeepMind overthinking 页面为旧预印本的 ACL 2026 publication 节点 |
| 6–14 | Meta AI / FAIR；Microsoft Research；NVIDIA Research；xAI；Amazon Science；Cohere Labs；Ai2；Mistral AI；Alibaba Qwen | Meta Brain2Qwerty v2 发布于 6 月 29 日；Qwen Code 7 月 2 日周更属于产品迭代，Record Only |
| 15–25 | DeepSeek；Moonshot / Kimi；Zhipu；MiniMax；ByteDance Seed；Baidu ERNIE；Tencent Hunyuan；Huawei Noah；Shanghai AI Lab / InternLM；StepFun；Xiaomi MiMo | Seed2.0 Model Card 首版为 6 月 30 日，纳入本周；其余无高门槛官方更新 |
| 26–27 | InclusionAI / Ant Group；Hugging Face Blog | 无需进入 Books 的新研究发布 |
| Weekly | LG AI Research；Sakana AI；01.AI；Baichuan；ModelBest；BAAI；Salesforce；IBM；Databricks / Mosaic | 未发现本窗口内、可由一手材料核验的高分候选 |

### Publication-State Change — Google DeepMind Overthinking

- Official publication page: 2026-07-02
- First Public Version: 2025-10-09（arXiv:2510.07880）
- Venue: ACL 2026
- Decision: `Record Only / Not a new 2026-07 idea`

该工作用 TRACE 将 reasoning trace 拆成最小完整 sub-thought，再构造 progression graph，
将 overthinking 从“token 太长”改写为低效探索和重复验证的 utility 问题。机制有长期价值，
但它不属于本周首次公开证据；未来若写入推理预算章节，应引用首次公开与正式发表两个日期。

### Model / Evaluation Candidate Scoring

| Candidate | Technical Novelty | System Impact | Practical Value | Source Reliability | Project Relevance | Longevity | Total | Decision |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| OpenAI GeneBench-Pro | 3 | 4 | 4 | 4 | 4 | 4 | 23/30 | Worth Watching；Weekly only |
| Google Research TabFM | 4 | 3 | 4 | 4 | 3 | 4 | 22/30 | Worth Watching；Weekly only |
| Meta Brain2Qwerty v2 | 4 | 3 | 3 | 4 | 3 | 4 | 21/30 | Worth Watching；垂直研究案例 |
| ByteDance Seed2.0 Model Card | 3 | 3 | 3 | 4 | 4 | 3 | 20/30 | Worth Watching；Weekly only |

GeneBench-Pro 的长期信号是让 realistic ambiguity 与 deterministic grading 共存，而不是
本周的厂商模型排名。TabFM 的长期信号是对二维、置换无关表格结构显式建模，并把
per-dataset training 转移为 ICL；代价转为 synthetic pretraining、context 和 distribution
shift。Brain2Qwerty v2 与 Seed2.0 分别受限于垂直采集条件和厂商 model-card 证据边界。

## 2. 论文与学术来源

### Candidate Scoring

| Candidate | Technical Novelty | System Impact | Practical Value | Source Reliability | Project Relevance | Longevity | Total | Decision |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| One-Step Gradient Delay / asynchronous Pipeline Parallel | 4 | 5 | 4 | 3 | 5 | 5 | 26/30 | Must Read；全文重审后已 refine Ch34 |
| ELDR | 4 | 5 | 4 | 3 | 5 | 5 | 26/30 | Must Read；已归并 Weekly；Books 已评估 |
| HiLS-Attention | 4 | 4 | 3 | 3 | 5 | 5 | 24/30 | Worth Watching；Weekly only |
| Google DeepMind overthinking publication node | 3 | 3 | 3 | 5 | 4 | 5 | 23/30 | 旧预印本正式发表；去重 |
| Seed2.0 Model Card | 3 | 3 | 3 | 4 | 4 | 3 | 20/30 | 首版 6 月 30 日；已在机构组记录 |
| Orca: The World is in Your Mind | 5 | 4 | 3 | 3 | 5 | 5 | 25/30 | Refine Ch10 / Experimental；review complete |
| Program-as-Weights | 5 | 5 | 5 | 4 | 5 | 4 | 28/30 | Must Read；full review complete |
| Scaling the Horizon, Not the Parameters | 4 | 5 | 4 | 3 | 5 | 5 | 26/30 | Refine Ch25 / Experimental；review complete |
| BlockPilot | 4 | 5 | 5 | 3 | 5 | 4 | 26/30 | Refine Ch44 / Experimental；review complete |
| AgenticSTS | 4 | 4 | 5 | 4 | 5 | 4 | 26/30 | Full Source Review complete — Refine `AGENT-MEMORY` / Evaluation handoff / Experimental |
| Morphing into Hybrid Attention Models | 5 | 4 | 4 | 3 | 5 | 5 | 26/30 | Refine Ch22 / Experimental；review complete |
| EvoPolicyGym | 4 | 4 | 4 | 3 | 5 | 5 | 25/30 | No Change Ch62；review complete |
| AgenticDataBench | 4 | 4 | 4 | 3 | 5 | 5 | 25/30 | No Change Ch62；review complete |
| WorldDirector | 4 | 4 | 3 | 3 | 5 | 5 | 24/30 | Refine Ch10 / Experimental；review complete |
| MemSyco-Bench | 4 | 4 | 4 | 3 | 5 | 5 | 25/30 | Refine Ch73；review complete |
| Metacognitive Feedback / Faithful Uncertainty | 4 | 4 | 4 | 3 | 5 | 5 | 25/30 | Refine Ch29 / Experimental；review complete |
| MemLearner | 4 | 4 | 3 | 3 | 5 | 5 | 24/30 | Refine Ch10 / Experimental；review complete |
| ASPIRE Agentic Skills Discovery | 5 | 5 | 4 | 4 | 5 | 4 | 27/30 | Refine Ch80 / Experimental；review complete |
| SkillCoach | 4 | 4 | 5 | 3 | 5 | 5 | 26/30 | No Change Ch62；review complete |
| TACO Tool-Augmented Credit Optimization | 5 | 5 | 4 | 3 | 5 | 4 | 26/30 | Refine Ch29 / Experimental；review complete |
| AutoMem | 5 | 5 | 4 | 3 | 5 | 5 | 27/30 | Refine Ch73 / Experimental；review complete |
| PACE proxy agent evaluation | 4 | 4 | 5 | 3 | 5 | 4 | 25/30 | Refine Ch62 / Experimental；review complete |
| Xiaomi-GUI-0 | 4 | 4 | 4 | 4 | 5 | 4 | 25/30 | No Change Ch77；review complete |
| SWE-Together | 4 | 4 | 4 | 3 | 5 | 5 | 25/30 | No Change Ch62；review complete |
| Performance-Optimization Benchmark Reliability | 4 | 5 | 5 | 4 | 5 | 4 | 27/30 | Refine Ch62；review complete |
| QVal | 5 | 4 | 5 | 3 | 5 | 4 | 26/30 | Refine Ch62 / Experimental；review complete |
| TRIAGE Role-Typed Credit Assignment | 5 | 5 | 4 | 3 | 5 | 5 | 27/30 | Refine Ch29 / Experimental；review complete |
| RESOURCE2SKILL | 5 | 5 | 5 | 3 | 5 | 5 | 28/30 | Refine Ch80 / Experimental；review complete |

### Deep Analysis 1 — Asynchronous Pipeline Parallel：Staleness 是联合设计问题

- Submitted / First Public Version: 2026-06-29 17:57:50 UTC
- Status: Experimental
- Primary Source: https://arxiv.org/abs/2606.30634

#### Why

同步 GPipe / 1F1B 保持相对清晰的 step 和参数版本语义，却会因 fill/drain 与 stage
不均衡留下 pipeline bubbles。异步 schedule 可以让 stages 持续推进，但不同 microbatch
看到的参数版本不再一致，吞吐收益转化为 gradient staleness 与收敛风险。

#### Principle

“异步训练是否稳定”不是 schedule 的孤立属性。schedule 决定 weight-version distance，
optimizer 决定 delay 如何改变更新方向与误差累积，correction 再决定哪些延迟误差可被反馈。
因此完整设计对象是 `schedule × optimizer × correction × checkpoint semantics`。

#### Mechanism

PipeDream-2BW 相比原始 PipeDream，将 gradient delay 限制为与 pipeline depth 无关的固定
一步。论文比较 optimizer 在该 delay 下的行为：作者实验观察到 AdamW 明显退化、Muon 更
稳健，并提出 optimizer-agnostic、受 Error Feedback 启发的 correction 进一步减轻 delay。

#### Trade-off

异步化换取更少 bubble 与更高设备利用率，同时引入多版本参数、optimizer coupling、
checkpoint/recovery 语义和复现实验复杂度。作者实验覆盖至 10B 参数并主张接近同步训练；
在更大模型、不同 workload、MoE imbalance 与生产故障条件下仍未得到独立验证。

#### Connection

知识树位置：第 28 章 Optimizers → 第 34 章 Pipeline Parallel → 第 37 章 Distributed
Training Runtime。它细化已有“bubble 与 stale parameters”的边界，不推翻同步 1F1B 作为
稳定基线的结论。

#### Evolution

```text
同步 GPipe / 1F1B：一致性较清晰，但存在 fill/drain bubble
→ 原始异步 PipeDream：提高利用率，引入多版本参数与 staleness
→ PipeDream-2BW：将 delay 约束为固定一步，但未自动消除优化误差
→ optimizer-aware robustness + error-feedback correction
→ 稳定性被改写为 schedule、optimizer 与 correction 的联合问题
```

旧方案没有被新方案否定：当确定性、恢复简单性和成熟实现优先时，同步 schedule 仍成立；
只有 bubble 成本足够高且 optimizer/correction 的证据充分时，异步分支才可能占优。

### Deep Analysis 2 — ELDR：Decode Routing 也要看到 Expert Working Set

- Submitted: 2026-07-01 05:34:38 UTC
- First Public Version: 2026-07-01
- Status: Experimental
- Primary Source: https://arxiv.org/abs/2607.00466

#### Why

PD 分离后，Prefill 必须选择 Decode worker。普通 least-load routing 假设等负载 worker 的
服务成本相近；MoE 打破了这个假设，因为 Decode step 的延迟还取决于 batch 激活了哪些
experts、相关 weights 是否形成可复用 working set。

#### Principle

路由目标不能只最小化 queue load，还要最小化请求状态与 worker memory locality 的失配。
Prefill 已经产生的 expert activations 是对后续 Decode expert demand 的一个条件性先验。

#### Mechanism

论文从 Prefill expert activations 构造 expert signature；离线用 balanced K-means 将 signature
space 分区，在线在 locality 匹配较好的 worker 子集中选择最低负载者。signature cache 与
KV cache 按 block 共同索引，使 prefix reuse 不会把预测状态与 KV ownership 拆开。

#### Trade-off

收益来自 expert weight locality，代价是 signature 生成、分区漂移、额外 metadata 和 routing
复杂度。若模型是 Dense、expert 全驻留、activation pattern 不稳定，或负载失衡远大于 locality
收益，该策略可能不成立。作者报告在三种 MoE 模型、两个 workload、最多 40 GPU 的部署上，
相对四个 load-balancing baselines 的 median TPOT 降低 5.9%～13.9%；摘要未完整披露硬件型号、
输入输出长度、并发、精度与 SLO，不能外推为通用收益。

#### Connection

知识树位置：第 21 章 MoE → 第 48 章 distributed inference runtime → 第 51 章 PD disaggregation
→ 第 52 章 inference scheduling。它补充的是“routing cost model 必须匹配 model state”，
不是新的 MoE 数学或 KV transport。

#### Evolution

从 round-robin、least-load，到 prefix/KV-aware routing，再到 expert-locality-aware routing，
演化主线是 router 逐步看到更多会改变真实 service time 的隐藏状态。下一步需要验证动态
repartition、multi-tenant fairness 与专家迁移成本。

### Deep Analysis 3 — HiLS：Sparse Attention 的选择器必须进入训练目标

- Submitted / First Public Version: 2026-07-03 05:39:00 UTC
- Status: Experimental
- Primary Source: https://arxiv.org/abs/2607.02980

#### Why

Chunk-wise sparse attention 减少 KV 访问，却可能因 chunk selection 错误丢失关键信息。
如果 selector 只接受独立 retrieval objective，它优化的相关性不一定等于 language-modeling
loss 真正需要的信息。

#### Principle

稀疏化不是单独的检索层，而是近似原 attention operator。选择概率必须影响最终 forward
computation，LM loss 才能把下游误差传回 selector。

#### Mechanism

HiLS 分层选择 landmarks；query 分别与已选 chunks 计算 attention，再用 retrieval scores
融合 chunk-specific outputs。因为 score 进入 forward，selector 可与模型端到端训练。

#### Trade-off

它用 learned selection 换取 sparse KV access，但付出 selector training、chunk granularity、
continued pretraining 和错误召回风险。作者报告超过训练长度 64 倍时 90% retrieval accuracy；
这是论文设定内的实验结论，摘要未提供足以比较生产 TTFT、HBM、并发和精度的完整条件。

#### Connection

知识树位置：第 14 章 Attention → 第 22 章 Long Context → 第 43 章 KV Cache。它强化现有
第一性原理：long context 的核心不是声明 context window，而是 accuracy、compute、memory
和 state access 的联合约束。

#### Evolution

从 dense attention，到固定 local/window sparse，再到 external retrieval 和 learned
hierarchical selection，演化方向是让近似策略逐步接受 end-to-end task loss；是否能稳定迁移
到不同 domain 与模型规模仍需后续证据。

## 3. AI Infra 与工程项目

### Source Coverage

按 PyTorch → JAX → CUDA → Triton → vLLM → SGLang → NVIDIA Dynamo → TensorRT-LLM
→ Ray → KServe → Kubeflow → Kubernetes → Transformers → Accelerate → DeepSpeed
→ Megatron-LM → Unsloth → MLX → llama.cpp → ONNX Runtime → OpenXLA 的顺序扫描官方
Release、文档、RFC 与重要 PR。fixed replay 恢复了 NVIDIA Secure Agent Workspace Reference Design
与 TensorRT Edge-LLM v0.9.0；前者是 target reference architecture，后者是版本化 edge runtime release，
均不能被写成普遍部署事实。

Qwen Code 7 月 2 日的 `/loop`、语音与 UI 周更属于 agent product surface 迭代，未提供足以
改变本书 agent runtime 设计边界的新机制，故不深入分析。

### AI Infra Candidate Scoring

| Candidate | Technical Novelty | System Impact | Practical Value | Source Reliability | Project Relevance | Longevity | Total | Decision |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| NVIDIA Secure Agent Workspace Reference Design | 4 | 5 | 5 | 5 | 5 | 5 | 29/30 | Provisional Refine — Ch80 owner；Ch68 handoff；reference-architecture boundary |
| TensorRT Edge-LLM v0.9.0 | 3 | 3 | 4 | 5 | 4 | 2 | 21/30 | Weekly Only — Version Fact / Mechanism Not Disclosed |

## Evidence Level

| Claim | Evidence | Boundary |
| --- | --- | --- |
| 一步 delay 下的退化依赖 optimizer | arXiv 论文的作者实验与理论分析 | `Status: Experimental`；实验至 10B，尚无独立复现 |
| ELDR 的 signature 与 KV block 共索引 | arXiv 正文/摘要，作者实验 | `Status: Experimental` |
| HiLS 让 retrieval score 进入 LM forward | arXiv 正文/摘要，作者实验 | `Status: Experimental` |
| GeneBench-Pro / TabFM / Brain2Qwerty 的设计与数据说明 | 各机构官方页面 | 官方事实与厂商实验，不证明通用效果 |
| Overthinking 页面不是首次公开 | 官方 publication date + arXiv submission history | 日期事实 |
| Secure Agent Workspace 的 plane、policy、credential 与 approval contract | NVIDIA official blog + reference design + OpenShell repository state | target architecture；当前 OpenShell alpha/experimental 状态不倒写成 6 月已验证部署 |
| TensorRT Edge-LLM v0.9.0 的支持矩阵与 breaking changes | official release discussion | 版本事实；不公开内部性能因果机制，不外推通用收益 |

## Cross-Week Deduplication

- Seed2.0 Model Card 首版为 2026-06-30，纳入 W27，不重复计入 7 月事件。
- Google DeepMind overthinking 论文首版为 2025-10-09；2026-07-02 只记录正式发表状态。
- Hugging Face 7 月 2 日推荐 TurboServe，但其 arXiv 首版为 2026-06-17，排除 discovery-date
  drift。
- Multi-Block DLM、OSWorld 2.0 等虽然在 W27 display feed 出现，但 v1 是 2026-06-28；连同
  其余 8 个 v1 属于 6 月 25～28 日的 family 一并回拨 W26。后续 revision 只更新 revision
  history，不移动事件周。
- Secure Agent Workspace 以 2026-06-29 official blog / reference-design publication 为 W27 event；
  2026-08-12 访问到的 OpenShell main branch 只作当前 artifact-state 边界，不视为 W27 已实现功能。
- TensorRT Edge-LLM v0.9.0 按 2026-07-03 release node 进入 W27；其中 DFlash algorithm 首发与后续
  cross-runtime integration 已分别归 W06 / W26，本周只记录 edge packaging 和 support-matrix 变化。
- RESOURCE2SKILL（arXiv:2606.29538）v1 为 2026-06-30；W30 feed 的 7 月展示不是新事件。当前 v4
  仅用于 revision-sensitive 机制核验，event owner 仍为 W27。

## Knowledge Tree Position

| Candidate | ROADMAP Node | Role |
| --- | --- | --- |
| Asynchronous Pipeline Parallel | Ch28 → Ch34 → Ch37 | schedule、optimizer 与 staleness 的联合设计 |
| ELDR | Ch21 → Ch48 → Ch51 → Ch52 | MoE state-aware distributed routing |
| HiLS | Ch14 → Ch22 → Ch43 | learned sparse attention and KV access |
| Overthinking | Ch20 → Ch42 → Ch62 | reasoning utility、serving cost 与 evaluation |
| GeneBench-Pro | Ch19 → Ch62 | realistic ambiguity 与 deterministic grading |
| TabFM | Ch4 → Ch14 | structured-data prior 与 ICL |
| Program-as-Weights | Ch26 → Ch55 → Ch74 | specification-to-adapter compilation 与 artifact lifecycle |
| AgenticSTS / AutoMem / MemSyco | Ch62 → Ch73 → Ch80 | bounded memory、metamemory 与 downstream memory risk |
| TACO / QVal / TRIAGE | Ch29 → Ch62 → Ch74 | tool/process credit 与 verifier boundary |
| SWE-Together / benchmark reliability audit | Ch62 → Ch77 | interactive workflow evaluation 与 benchmark validity |
| Secure Agent Workspace Reference Design | Ch80 → Ch68 | workspace lifecycle、policy/credential enforcement 与 evidence plane |
| TensorRT Edge-LLM v0.9.0 | Ch45 | edge runtime 的版本化 support / compatibility contract |
| Orca / WorldDirector / MemLearner | Ch10 | predictive latent、显式对象状态与视频 world-memory 的实验性机制 |
| FlashMorph | Ch22 | hybrid Attention placement 的全局 budgeted selection |
| Scaling the Horizon | Ch25 → Ch77 | domain-routed on-policy distillation 与 protocol ownership |
| BlockPilot | Ch44 | prefix-dependent speculative block control |
| RESOURCE2SKILL / ASPIRE | Ch80 | resource/trace → validated Skill → governed library lifecycle |

## Recommended Action

- 已吸收的核心增量是机制链而非论文摘要：specification → versioned neural program artifact；raw
  transcript → bounded typed visibility；resource/trace → governed Skill admission；ephemeral sandbox →
  long-lived secure workspace；executable benchmark → reference-first replay 与 proxy-alignment Gate。
- asynchronous Pipeline Parallel 与 ELDR 的既有正文经相邻章节复读后保留；新证据没有改变其 staleness
  correction 与 conditional-compute locality 结论，因此不重复扩写。
- GeneBench-Pro、TabFM、Brain2Qwerty、Seed2.0 与 TensorRT Edge-LLM 只保留版本/领域事实；HiLS、
  Overthinking、EvoPolicyGym、AgenticDataBench、SkillCoach、Xiaomi-GUI-0 与 SWE-Together 已被现有具体
  论点覆盖，不为增加 diff 重复写入。
- 所有 33 个唯一 source family 的最终 owner/disposition 已记录在下方 ledger。后续只在新的独立复现、
  workload contract 或冲突证据出现时重开相应 family。

## Event-Date Daily Decision

| Date | Decision | Reason |
| --- | --- | --- |
| 2026-06-29 | Weekly only | asynchronous Pipeline Parallel 26/30，但历史回填不保留 Daily |
| 2026-06-30 | Weekly only | 三个独立 primary sources 已完整整合进 W27 |
| 2026-07-01 | Retired after Weekly integration | ELDR 26/30 曾触发事件 Daily；完整证据已归并 W27 |
| 2026-07-02 | Do not create | Google DeepMind 页面对应旧预印本；避免伪造首次发布日期 |
| 2026-07-03 | Do not create | HiLS 24/30，单篇预印本且系统条件仍不完整 |

## Books Integration Decision

`Source-Family Books Gate Passed — Archive Completion Gate Open`。W27 的 33 个唯一 family 已全部完成
逐项判断：21 项 refine 既有论证，7 项由现有章节具体覆盖，5 项只保留 Weekly。实际新增正文集中在
`TRAIN-LORA`、`PLATFORM-EVALUATION-SYSTEM`、`AGENT-MEMORY` 与 `AGENT-PLATFORM`；其余 Refine 项已由
W27 前后更强的 source family 共同形成现有演进链，或在 asynchronous PP / ELDR 的既有正文中通过复核。
本周没有把作者 benchmark、publication node 或 release support matrix 外推为通用系统结论。

## Ignored Noise

- 以 Hugging Face 推荐日替代 arXiv 首版日期的条目；
- 只有 leaderboard、融资、产品 UI 或未披露条件的 benchmark 宣传；
- 旧论文的机构 publication page 重现；
- patch tag、预发布版本和没有设计说明的普通 PR。

## 2026-07-31 Full Re-Audit Addendum

- asynchronous Pipeline Parallel 已全文复核并达到机制门槛：从 variable staleness 到
  constant one-step delay，再到 optimizer-aware error feedback 的演进写入 Ch34；实验只到
  10B MoE/200B tokens，未宣称通用 wall-clock 优势。
- ELDR 全文重审确认 Ch48 已正确吸收 conditional expert/KV locality，并补足 signature、
  index ownership 与 MI300X/vLLM/Poisson workload 边界。
- HiLS 仍为单篇预印本；overthinking 的 2025 首版日期已确认。Seed2.0 两个评分行是同一
  2026-06-30 事件，分别保留 disposition 但不重复计数。

## Full Source Review

### Program-as-Weights — 28/30

- **Source Family / Type / Date**：`PROGRAM-AS-WEIGHTS`；arXiv:2607.02512v1，first-public
  2026-07-02；primary paper、完整 arXiv HTML、training/evaluation/quantization Appendices 与作者
  GitHub organization/SDK 联读。
- **Full-read Coverage**：已覆盖 Introduction/Related Work、compiler-interpreter abstraction、
  Text-to-LoRA 与 prefix-tuning 两条实现、objective、FuzzyBench construction、main baselines、
  cross-interpreter/multimodal results、mapper/no-compiler/component ablations、noise robustness、
  local execution、training hardware、quantization tables、case studies、qualitative failures、
  limitations 与 public SDK/artifact surface。
- **Original Problem / Previous Design**：显式 code/regex 对 fuzzy function 的长尾、typo 与格式漂移
  很脆弱；每个 input 调远端大模型虽合理地利用通用能力，却把 locality、reproducibility、privacy、
  provider drift 与 per-call cost 留在在线路径。传统 per-task fine-tuning/LoRA 则需要为每个新任务
  单独收集数据并训练。
- **Changed Constraint / Principle**：当同一自然语言 specification 会被重复执行很多次，系统可以把
  计算从 request time 搬到 compile time。Foundation model 不再只作为 per-input solver，而可作为
  artifact builder：`specification -> versioned neural program -> frozen local interpreter`。
- **Mechanism / State Ownership / Flow**：未训练的 Qwen3-4B pseudo compiler 先把 specification
  规范化为 description+examples；训练过的 Qwen3-4B LoRA compiler 读取 spec+pseudo+64 learned
  tokens，从 depth-aligned hidden states 生成 mixing coefficients，在共享 basis 上组合每层、每模块的
  rank-64 LoRA。冻结的 0.6B interpreter 在运行时热挂 LoRA 并把 pseudo-program prepend 到 input。
  compiler pair 拥有 generation semantics，Registry/artifact store 应拥有 base、adapter、pseudo、
  digest 与 compatibility identity；runtime 只执行显式选中的 program。
- **Implementation Contract**：每个 program 约 38.5M LoRA parameters；作者 SDK 暴露 compile/load/call，
  单个 device-resident interpreter 可切换多个 adapters。Qwen3 训练使用 10M synthetic triples、3 epochs、
  effective batch 48、max compiler/interpreter length 1280/1024、AdamW；论文披露 single B300 或
  8×H200，0.6B run 约 72 小时/3 GPUs。公开 GitHub 提供 Python/JS SDK 与 WebAssembly llama.cpp fork，
  但 organization page 不能独立证明 paper 全部实验可复现。
- **Evaluation Contract**：verified FuzzyBench split 以 specification 划分；比较 Qwen3 0.6B～32B
  prompting、API models、symbolic generation、同 base full fine-tuning 与 fixed LoRA。核心结果是作者
  exact-match setting 下 0.6B PAW 73.78%，Qwen3-32B prompting 68.70%；bf16 memory 约 1.2GB vs
  约 60GB。MacBook M3/Metal 的 Q5_K_M base + Q4_0 adapter 报告 31.6 tok/s、0.48s cold load；
  该数字没有 input/output length、并发、power 或 SLO，不能作为通用 serving 结论。
- **Ablations / Sensitivity**：compiler-generated LoRA 优于同 base full FT/fixed LoRA；简单 shared-basis
  mapper 反而优于更 expressive variants，但作者没有理论解释。Pseudo-program 对 heavy typo 有帮助，
  对 long-form image-to-markup 可能挤占 context；LoRA 与 prefix-tuning 的优劣依任务而变。Compiler
  scaling 表明确标为 inconclusive，不能声称更大 compiler 必然更强。
- **What It Proves / Does Not Prove**：证据支持“compile once, reuse locally”在论文的 single-step
  fuzzy-task distribution 上可形成可携带 adapter，并把部分在线成本转为离线编译；不证明神经 artifact
  等价于确定程序、不证明 long-horizon/compositional correctness、不证明所有 PEFT 或真实业务分布、
  也不证明 50× memory headline 可跨硬件和 workload 泛化。
- **Trade-offs / Failure Modes**：获得 locality、离线执行、per-function identity 与共享 base，付出
  compiler/interpreter 强耦合、opaque continuous binary、23MB/program storage、adapter cache/selection、
  synthetic-data bias、numerical/position errors 与新的 supply-chain risk。Spec、pseudo、adapter、base、
  quantization 和 runtime 任一错配都可能产生可加载但语义错误的函数；显式 code 在精确、可证明、
  高风险逻辑中仍是正确旧方案。
- **Evolution Relationship / ROADMAP**：`Layering / Dependency` 于 LoRA 与 Model Registry，不是 LoRA
  的替代。已读相邻章节；主 owner 为 `TRAIN-LORA`，Model Registry 管 artifact identity，Agent Platform
  管调用与授权。`Refine — New Mechanism`；已写入 specification-to-neural-program compilation。
- **Open Questions**：如何对 neural binary 做 static/behavioral inspection、签名与 revoke；如何测
  compile amortization break-even；怎样在 adapter hot-swap 下隔离 tenant/cache；能否在真实 multi-step
  workflow 中保持 compositional correctness 与可回滚性。

### OpenAI GeneBench-Pro — 23/30

- **Source Family / Date / Coverage**：`GENEBENCH-PRO`；OpenAI 2026-06-30 announcement、full PDF、
  dataset/task construction、statistical-reasoning stages、grading、baseline 与 limitations 已核对。
- **Evidence / Decision**：证明所发 benchmark 对 genomics multistage analysis 的测量范围，不证明
  wet-lab、clinical outcome 或一般 scientific autonomy。Ch62/69 已读；
  `No Change — Already Covered`。

### Google Research TabFM — 22/30

- **Source Family / Coverage**：`TABFM-ZERO-SHOT-TABULAR`；Google 2026-06-30 official report、linked
  paper/model material；已覆盖 table representation、zero-shot objective、datasets/baselines/ablation、
  scaling 与 limitations。
- **Evidence / Decision**：作者实验支持特定 tabular distributions 的 transfer，不证明替代 domain
  feature engineering、causal inference 或 production data validation。Ch23/24/62 已读；
  `No Change — Already Covered`。

### Meta Brain2Qwerty v2 — 21/30

- **Source / Coverage**：Meta 2026-06-29 official report、study protocol、sensor/data/decoder 和 participant
  limitations 已核对。
- **Decision**：垂直 BCI case 的 measurement/ethics 边界重要，但没有通用 AI Infra 新机制；
  `Weekly Only — Version/Product Fact`。

### ByteDance Seed2.0 Model Card — 20/30

- **Source Family / History**：`SEED2-MODEL-CARD`；arXiv:2607.00248v1，first-public 2026-06-30；
  institution row 与 paper row 指向同一事件，不作两个 unique retained event。
- **Coverage / Decision**：model card 的能力、安全、evaluation 与限制已核对；训练/runtime 内部细节不足，
  厂商 benchmark 不外推。`Weekly Only — Version/Product Fact`。两条评分行共享本 disposition。

### One-Step Gradient Delay / asynchronous Pipeline Parallel — 26/30

- **Source Family ID / Type / Date**：`ASYNC-PP-ONE-STEP-DELAY`；arXiv:2606.30634v1，
  first-public 2026-06-29。
- **Full-read Coverage**：已覆盖 delayed-update abstraction、optimizer/hyperparameter sweeps、error
  feedback、theory、2B/10B MoE、PipeDream comparison、discussion/limitations、全部 sensitivity、
  architecture/training、memory/runtime appendices。
- **Problem / Previous Design / Changed Constraint**：synchronous PP 保持 minibatch semantics 和成熟
  optimizer behavior，bubble 是合理成本；MoE 降低 compute/communication ratio，bubble/idle cost 上升，
  促使重新检查 Async PP 是否必然不稳定。
- **Mechanism / Ownership / Flow**：PipeDream variable stage delay→2BW 将所有 stage 固定为 one-step
  delay并仅多 stash 一份 weight；optimizer 用上一 step gradient，error-feedback-inspired update 以
  `2u(t-1)-u(t-2)` 补偿。schedule 决定 staleness shape，optimizer state 决定是否稳定，不能分开选型。
- **Evaluation Contract**：135M/360M optimizer sweeps，2B 和 10B MoE；10B 训练 200B FineWeb-Edu
  tokens，比较 sync/async、AdamW/Muon 等，含 batch/LR/momentum/error-feedback ablation。它证明 fixed
  one-step delay 在这些 recipes 中可接近 sync loss，不证明真实 pipeline implementation 的端到端
  throughput、fault recovery、larger-scale stability 或所有 optimizer。
- **Trade-offs / Evolution**：去 bubble 换取非等价优化语义、weight stash、恢复/重放复杂度；高 momentum
  和 error feedback 缓解 delay 但改变 dynamics。sync PP 在高风险 recipe、浅 pipeline 和 bubble 可控时
  仍成立。关系为 `Direct Evolution`。
- **ROADMAP / Chapters / Decision**：`TRAIN-PIPELINE-PARALLEL` 主 owner，已读目标与相邻章节；现有
  内容准确。`No Change — Already Covered`，保留该修改。

### ELDR — 26/30

- **Source Family ID / Type / Date**：`ELDR-MOE-DECODE-ROUTING`；arXiv:2607.00466v1，
  first-public 2026-07-01；论文与 vLLM implementation path 联读。
- **Full-read Coverage**：已覆盖 MoE decode locality motivation、signature design、balanced clustering/
  online routing、prefix-cache coherence、implementation、micro/end-to-end evaluation、ablation、sensitivity
  和 discussion；论文无独立 limitations 章节，assumptions 单独记录。
- **Problem / Previous Design / Changed Constraint**：PD disaggregation 中 JSQ/P2C 对 dense decode 合理；
  MoE batch latency由 distinct active expert set 主导时，纯 load balance 会破坏 expert weight reuse。
- **Mechanism / Ownership / Flow**：prefill hook 按 KV block 记录 expert-selection histogram，IDF/layer mask
  形成 signature；offline balanced K-means 为 decoder 建 centroid；handoff 将 block signatures 求和，router
  在 locality band 内选择 least-loaded decoder。signature 与 KV block 同生命周期，避免 partial-hit/eviction
  不一致；engine/kernel 不变。
- **Evaluation Contract**：5-node、40×MI300X、400Gbps NDR、vLLM 0.21rc1/ROCm7.2/NIXL；Qwen3、
  GPT-OSS、Gemma 等 MoE，8P16D 等 topology，Poisson 20–100qps、120s+30s warmup、output 512/
  ignore_eos，与 Random/RR/JSQ/P2C/Domain 比较。结论仅属这些 model/workload/topology。
- **Trade-offs / Failure Modes**：locality 减少 expert weight working set，新增 calibration drift、signature
  cache、load/locality冲突、prefix/KV identity 和 worker churn；dense model/低 domain structure 仍适合普通
  load balancing。关系为 `Layering / Dependency` 于 PD routing。
- **ROADMAP / Decision**：Ch48 主 owner，已读 Ch47～52、Ch59；现有 conditional service cost 已覆盖。
  `No Change — Already Covered`，保留 `INFER-DYNAMO` 既有内容。

### HiLS-Attention — 24/30

- **Source Family / Full-read Coverage**：`HILS-ATTENTION`；arXiv:2607.02980v1，first-public
  2026-07-03；已读 LogSumExp/chunk-mass 问题、hierarchical selector、training objective、evaluation、
  ablation、appendix 与 limitations。
- **Evidence / Trade-off**：论文说明 mean-pooled chunk key 对 peaked logits 的表达边界，并用训练耦合
  selector 改进稀疏检索；作者结果不证明无限 context、跨 model/data 稳定或 production SLO。稀疏收益
  换来 selector error、training coupling、index/state 和 fallback。Ch14/17/43/50 已读；
  `Emerging / Experimental`。

### Google DeepMind overthinking publication node — 23/30

- **Source / History**：arXiv:2510.07880 first-public 2025-10-09；2026-07-02 是正式 publication page，
  不作为新机制首发。全文的 structural tasks、intervention、evaluation 和 limitations 已核对。
- **Decision**：`No Change — Already Covered`；仅记录 revision/publication，避免 revision duplication。

### NVIDIA Secure Agent Workspace Reference Design — 29/30

- **Source Family / Type / Date**：`NVIDIA-SECURE-AGENT-WORKSPACE`；NVIDIA official technical blog
  published 2026-06-29，reference design last-updated node 2026-06-28；官方架构、security/governance、
  operating-property 文档与 OpenShell artifact state 联读。2026-08-12 的 repository main branch 只记录
  当前实现边界，不倒写为 event-date capability。
- **Original Problem / Previous Design / Changed Constraint**：chat endpoint 只生成内容时，API gateway、
  application sandbox 和短时 credential 足以形成合理边界；Agent 开始运行数小时、修改文件、访问多个
  business systems 并产生外部副作用后，风险状态跨进程、tool、credential、workspace 和 policy version
  持续存在，单次 model refusal 不再拥有完整 authority。
- **Mechanism / State Ownership / Flow**：reference design 把 presentation endpoint 与 managed execution
  workspace 分离；workspace / VM 绑定 user、agent、goal、tools、services、data、write scope、review 与
  logging policy。signed policy bundle 由 control plane 管理，sandbox 在执行边界强制；credential proxy
  向 provider 注入短期凭据而不把 raw secret 暴露给 Agent；系统变更先经过 typed policy decision / human
  approval，再由 tool executor 执行并生成 audit evidence。gateway 负责 identity、quota、RBAC 与 rate
  limit，GitOps / signed runtime policy 管理 desired state。
- **Implementation / Operating Contract**：官方 reference deployment 以 per-user managed VM、default-deny
  egress、centralized logging 与 OpenShift/Azure 路径表达 target architecture；OpenShell 当前仓库把 gateway、
  sandbox、policy engine 与 privacy router 分开，并说明 filesystem/process policy 在创建时锁定、network /
  inference policy 可热更新。仓库同时明确标为 alpha、single-player；Kubernetes 与 GPU support 为 experimental，
  因此不能把 reference design 写成已验证 multi-tenant production product。
- **What Evidence Proves / Does Not Prove**：primary sources 证明 NVIDIA 定义并公开了 workspace-level
  isolation、policy、credential、approval 与 evidence contract；不证明所有 plane 已完整实现、不证明 vendor-
  neutral interoperability、multi-tenant isolation strength、failure recovery 或性能开销，也没有 workload / SLO
  benchmark 可外推。
- **Trade-offs / Failure Modes / Coexistence**：长期 workspace 提供 blast-radius、secret non-disclosure 与
  replay evidence，代价是 VM lifecycle、policy distribution、approval latency、log privacy、credential-proxy
  availability 和 control/execution version skew。只读、短时、无副作用任务仍可使用较轻 application sandbox；
  高权限长程 Agent 才需要完整 managed workspace。关系为 `Layering / Dependency`，不是 sandbox 的替代。
- **ROADMAP / Chapters / Decision**：Ch80 主 owner，已读 Ch79～80 与 Ch68；Ch80 已有 three-plane、AgentRun、
  identity/delegation/approval 主线，本项补全 workspace 作为隔离与生命周期单元；Ch68 只做 policy/credential
  enforcement handoff。`Refine — New Mechanism / Reference Architecture`；workspace isolation lifecycle
  已写入 `AGENT-PLATFORM`。

### TensorRT Edge-LLM v0.9.0 — 21/30

- **Source Family / Type / Date**：`TENSORRT-EDGE-LLM-0.9.0`；official GitHub release discussion，
  released 2026-07-03；核对 release feature list、breaking changes 与前后 source-family relation。
- **Problem / Changed Constraint**：edge runtime 需要在有限硬件、模型格式、multimodal preprocessing 与
  speculative-decoding artifacts 之间维持明确 compatibility；旧版本保持较窄矩阵可降低维护复杂度，新版本
  为 DGX Spark、DFlash、Qwen3-Omni NVFP4、Gemma4 与 C++ audio input 扩大 surface。
- **Mechanism / State and Flow**：release 公开的是 support / packaging contract，而非内部设计论文。可核验
  状态包括 target hardware/model、audio preprocessing/server input path、NVFP4 MoE target config 和 speculative
  artifact naming；具体 kernel、scheduler、memory ownership 与性能因果机制为 `Not Disclosed`。
- **Evidence Boundary / Trade-offs**：release 证明这些接口与兼容性变化存在，也记录 decode regression fixes；
  不证明相对其他 runtime 的 latency、energy、quality 或 SLO。更宽支持矩阵换来 config/artifact migration、
  regression surface 与 release pinning 成本；旧版本在固定模型/硬件且 migration 风险较高时仍合理。
- **ROADMAP / Decision**：Ch45 主 owner，已读 Ch44～46；`Weekly Only — Version Fact / Mechanism Not
  Disclosed`。DFlash mechanism 不在本周重复计分，Books 不修改。

### Orca: The World is in Your Mind — 25/30

- **Source / Coverage**：`ORCA-UNIFIED-LATENT-WORLD-MODEL`；arXiv:2606.30534v1，first-public
  2026-06-29；当前 HTML 已到 v3，因此事件日期按 v1、机制按 revision 联读。已覆盖 next-state
  objective、冻结 backbone/readout probes、125K 小时视频/160M annotations、representation 与
  downstream evaluation、ablation、failure cases 和 limitations。
- **Mechanism / Evidence Boundary**：Orca 不直接以文本 label 监督每一种能力，而把跨视频、语言、动作的
  未来状态预测作为共享 latent objective，再用冻结表示上的 readout 检查多种能力是否共存。作者实验支持
  “predictive objective 可形成可迁移表示”这一受限结论；不证明 latent state 是因果世界模型，也不证明
  真实控制、长程 intervention 或 production SLO。
- **Trade-off / Evolution**：从单任务 supervised encoder 到统一预测表示，获得跨任务复用，代价是数据规模、
  objective ambiguity、probe dependence 与 observational correlation；显式 task-specific model 在监督充分、
  风险高或需要可解释 state 时仍合理。关系为 `Principle Reuse`，不是语言模型的替代。
- **ROADMAP / Decision**：已读 Ch9～10、Ch22、Ch62；Ch10 已明确“视觉逼真不等于因果正确”，但尚缺
  objective→latent state→readout 的机制链。`Refine — Existing Argument / Experimental`，主 owner
  `MULTIMODAL-WORLD-MODELS`；与其他 world-model families 共同形成现有正文。

### Scaling the Horizon, Not the Parameters — 26/30

- **Source / Coverage**：`AGENTS-A1-LONG-HORIZON-OPD`；arXiv:2606.30616v1，first-public 2026-06-29；
  已覆盖 task protocols、100K trajectories、约 45K 平均 trajectory length、Qwen3.5-35B-A3B student、
  domain-routed on-policy distillation、salient-vocabulary loss、evaluation 与 long-run cases。论文没有独立
  limitations 章节，case analysis 与披露缺口单列。
- **Mechanism / Ownership**：每个 domain 由专用 teacher 生成偏好信号；当前 student 在对应 environment
  产生 on-policy trajectory，tool/user/environment tokens 只作为 context、不计 student loss；domain router
  拥有 teacher/protocol 绑定，training ledger 必须绑定 environment、verifier 与 trajectory policy version。
  salient-vocabulary objective 只提高关键 token 的监督权重，不等价于获得新的规划模块。
- **Evidence Boundary / Trade-off**：作者结果支持该 35B MoE student 在论文任务集合中受益于 domain-routed
  OPD；标题中的 “trillion-parameter performance” 是比较性主张，不证明跨任务等价。收益以多 teacher 成本、
  protocol heterogeneity、长 trajectory storage、verifier bias 与 teacher inconsistency 为代价；短任务、稳定
  demonstration 仍可用普通 SFT/distillation。
- **ROADMAP / Decision**：已读 Ch23～25、Ch29、Ch77；Ch25 已有 on-policy context distillation 和
  teacher snapshot state，但尚缺 domain router/protocol ownership。`Refine — Existing Argument /
  Experimental`，主 owner Ch25，Ch77 仅 handoff；不在 Gate 前修改 Books。

### BlockPilot — 26/30

- **Source / Coverage**：`BLOCKPILOT-ADAPTIVE-SPECULATION`；arXiv:2606.31315v1，first-public
  2026-06-30；已读 learned block-length formulation、label construction、model integration、math/code/chat
  evaluation、temperature/sensitivity、baselines、ablation 与 offline-label cost。
- **Mechanism / State Flow**：固定 verify length 对不同 prefix 合理性不同。BlockPilot 从当前 hidden state
  预测本轮可安全提交的 block length，runtime 再以该长度执行 draft/verify；controller state 与 target/drafter
  版本、sampling contract 和 rollback 语义必须共同绑定。论文披露 32B、k=2 label generation 约
  25 秒/样本，说明控制器并非免费。
- **Evidence / Failure Modes**：作者实验只证明输入相关 block policy 在所测模型、任务和 decoding 设置中
  改善其 latency/acceptance trade-off；不证明跨硬件、并发和 SLO 的通用收益。新增 predictor error、distribution
  drift、额外训练/label 成本及过长 block 的 wasted verification；稳定 acceptance 分布下固定长度仍更简单。
- **ROADMAP / Decision**：已读 Ch40、Ch44～46；Ch44 已把 verify length 定义为受 acceptance、batch 和
  queue 影响的控制变量，但缺输入级 learned controller。`Refine — Existing Argument / Experimental`，
  主 owner Ch44；不保留作者 headline 数字。

### Morphing into Hybrid Attention Models / FlashMorph — 26/30

- **Source / Coverage**：`FLASHMORPH-HYBRID-ATTENTION-CONVERSION`；arXiv:2606.30562v1，first-public
  2026-06-29；已覆盖 morphable layer、global gate optimization、linearization regularization、20M synthetic
  retrieval-token calibration、conversion/evaluation、placement comparisons 与 conclusion。论文没有独立
  limitations 章节，冻结 backbone 与 calibration assumptions 明确列为边界。
- **Mechanism**：旧的逐层替换/独立评分忽略 layer 间互补性。FlashMorph 在同一可 morph network 中为各层
  建 gate，在全局 budget 下联合选择保留 softmax 或换成 linear branch；训练只优化轻量 gates/linear branches，
  冻结原 backbone。它优化的是 layer placement，不是证明 linear attention 与 softmax 等价。
- **Trade-off / Evolution**：相对固定周期 hybrid，联合 gate 可利用冗余与互补，但结果依 calibration data、
  branch family、budget 和 linearization approximation；转换后仍需 continued training/quality validation。
  从头训练的 native hybrid 在有完整训练预算时仍合理。关系为 `Direct Evolution` 于 hybrid placement。
- **ROADMAP / Decision**：已读 Ch14、Ch17、Ch22；Ch22 已覆盖 hybrid linear/softmax 的共存理由，但未覆盖
  “逐层独立判断→全局 budgeted placement”的演进。`Refine — Existing Argument / Experimental`，主 owner
  Ch22；不把单篇转换实验写成通用 recipe。

### EvoPolicyGym — 25/30

- **Source / Coverage**：`EVOPOLICYGYM-POLICY-EVOLUTION-BENCH`；arXiv:2607.02440v1，first-public
  2026-07-03；已读 task/environment construction、严格 visibility/budget、hidden held-out evaluation、
  leaderboard、diagnostics 与 limitations/proxy caveats。
- **Mechanism / Evidence**：benchmark 把 policy evolution 约束为同一可见信息、预算和 hidden tests，减少
  “更强 scaffold 获得更多机会”造成的混淆。它证明的是 harness 在该 controlled contract 下的表现差异，
  不证明某模型拥有一般 self-improvement，也不证明 proxy diagnostics 是真实 causal explanation。
- **Trade-off / Chapters**：控制变量提升内部可比性，却牺牲真实 workflow 的开放工具、动态预算和部署
  副作用；真实系统评估仍要保留 environment identity、cost 与 external outcome。已读 Ch62、Ch77～80；
  Ch62 已有 subject/environment/budget binding 与 feedback-conditioned policy。
- **Decision**：`No Change — Already Covered / Experimental Evaluation Case`。其价值是支持 Ch62 已有
  不变量，不形成新的长期机制；保留 Weekly 供后续独立 benchmark 交叉验证。

### AgenticDataBench — 25/30

- **Source / Coverage**：`AGENTICDATABENCH`；arXiv:2607.01647v1，first-public 2026-07-02；已覆盖
  433 skills、15 vertical domains、real-business/synthetic task construction、四类 harness、grading、skill
  profile、results 与披露限制；论文没有独立 limitations 章节。
- **Evidence Boundary**：该工作把 Data Agent 从单一 overall score 拆到 skill/domain/harness slices，能揭示
  data alignment、cleaning、visualization 等差异；但任务采样、grader 和 harness 仍共同定义被测对象，不能把
  leaderboard 直接归因于 base model，也不证明真实企业数据权限、schema drift 或 workflow reliability。
- **Trade-off / Chapters**：更细 taxonomy 增加诊断价值，也带来 skill label overlap、frequency weighting 和
  slice multiplicity；长期结论应是“评估对象须绑定 model+harness+environment”，不是某 Agent 排名。已读
  Ch62、Ch69、Ch77。
- **Decision**：`No Change — Already Covered`。Ch62 已明确四层评估对象、slice 与 uncertainty；该 benchmark
  作为领域案例保留，不重复正文。

### WorldDirector — 24/30

- **Source / Coverage**：`WORLDDIRECTOR-PERSISTENT-DYNAMIC-MEMORY`；arXiv:2607.02517v1，first-public
  2026-07-03；已读 3D trajectory planning→2D projection、appearance condition、dynamic context memory、
  asymmetric routing、chunked generation、evaluation 与 dynamic-context/condition-drop ablation。
- **Mechanism / State Flow**：高层 LLM 产生 dynamic-object trajectory，projector 将其变成视频生成条件；
  appearance bank 保持视觉身份，context memory 检索离开后重新进入的 dynamic entities，上一 chunk 末帧成为
  下一 chunk 初始条件。规划 state 与像素 synthesis 解耦，避免只依赖生成模型隐式记住对象。
- **Evidence / Failure Modes**：ablation 支持 dynamic context 对论文场景的 identity persistence 有贡献；
  不证明“无长度上限”、因果物理正确或闭环控制。新增 trajectory projection error、memory identity collision、
  chunk drift 与 planner/synthesizer inconsistency；短片或无重入对象时普通 conditional video generation 仍合理。
- **ROADMAP / Decision**：已读 Ch10、Ch22、Ch73；持久对象状态服务于 world simulator，而非用户/Agent
  memory，主 owner 应是 Ch10。`Refine — Existing Argument / Experimental`，Ch73 只作状态所有权 handoff；
  不把视觉质量外推为 world-model correctness。

### MemSyco-Bench — 25/30

- **Source / Coverage**：`MEMSYCO-MEMORY-RISK`；arXiv:2607.01071v1，first-public 2026-07-02；已读
  memory-induced sycophancy taxonomy、scenario construction、memory systems/backbones、retrieval 与
  post-retrieval error decomposition、results、judge protocol 和 limitations。
- **Mechanism / Evidence**：benchmark 将当前 query 与历史 memory 制造成一致、冲突、应忽略、应约束或应
  更新等条件，再区分“没有检索到正确 memory”和“已检索却作出错误决策”。作者分析中约 61–62% 的错误
  发生在 relevant memory 已被取回之后，支持 post-retrieval policy 是独立风险面；不证明该比例能外推到
  production users、其他 memory schema 或安全关键任务。
- **Trade-off / Evolution**：从 retrieval hit-rate 走向 downstream-use evaluation，新增 personalization 与
  factual/policy authority 冲突的测量；但 synthetic scenarios、judge 与 backbone choice 仍限定结论。没有
  memory 的 stateless Agent 在低重复、强事实 authority 场景仍可能更安全。
- **ROADMAP / Decision**：已读 Ch71～73、Ch62、Ch68；Ch73 已覆盖 Fact State 与 Retrieval-policy State，
  本文补强“读到了也可能不该采用”的 risk gate。`Refine — Existing Argument / Evaluation Evidence`，主
  owner `AGENT-MEMORY`；与 memory-risk families 共同形成现有正文。

### Reinforcement Learning with Metacognitive Feedback — 25/30

- **Source / Coverage**：`RLMF-FAITHFUL-UNCERTAINTY`；arXiv:2606.32032v1，first-public 2026-06-30；
  已覆盖 intrinsic-confidence extraction、metacognitive feedback/advantage、两阶段训练、cMFG/cMFG*、
  numerical/factual tasks、data-selection comparisons、ablations 与 metric caveats。
- **Mechanism**：模型先从自身生成状态产生 metacognitive prediction，再把预测与实际 correctness 的一致性
  转成 advantage/reward，推动 verbalized uncertainty 对齐内部信号。state owner 不只是 policy checkpoint，
  还包括 confidence extractor、feedback model、binning/support 与 reward version；否则恢复训练会改变目标。
- **Evidence / Failure Modes**：作者实验支持所测 8B models/tasks 的 uncertainty expression 改善，并展示
  cMFG 原定义会受 confidence distribution/binning 影响；不证明语言表达等于 calibrated probability、跨域
  truthfulness 或自我监督可免外部 ground truth。新增 self-signal collapse、reward hacking 和 metric selection。
- **ROADMAP / Decision**：已读 Ch27～30、Ch62；Ch29 已说明 measurement 是 reward interface，本文增加
  intrinsic signal 也须由外部 outcome 校准。`Refine — Existing Argument / Experimental`，主 owner Ch29，
  Ch62 handoff；传统 external verifier 在高风险/可验证任务仍成立。

### MemLearner — 24/30

- **Source / Coverage**：`MEMLEARNER-VIDEO-WORLD-MEMORY`；arXiv:2606.31734v1，first-public
  2026-06-30；已读 architecture、write/read/update mechanism、training、100 videos/13 scenes/16.7h setup、
  baselines、ablations、failure cases 与 limitations。
- **Mechanism / Evidence**：模型把跨片段的 entity/state observations 写入显式 memory，再由当前 frame/query
  选择性读取和更新，使 video world model 不必把长期状态完全压进短窗口 hidden state。作者结果证明的是
  该小规模环境中 memory module 对 persistence 的贡献，不证明开放世界、超过约 5 characters 的组合状态、
  因果 dynamics 或真实控制。
- **Trade-off / Evolution**：从纯 recurrent/video context 到显式可更新 state，获得跨 chunk persistence，
  代价是 entity binding、write pollution、capacity、stale state 与 read latency；短序列、低实体数时隐式 state
  仍更简单。关系为 `Layering / Dependency`。
- **ROADMAP / Decision**：已读 Ch10、Ch22、Ch73；主 owner Ch10，Ch73 只复用 write/read ownership 原则。
  `Refine — Existing Argument / Experimental`，不把有限 simulator 结果写成通用 memory 架构。

### ASPIRE Agentic Skills Discovery — 27/30

- **Source / Coverage**：`ASPIRE-AGENTIC-SKILL-DISCOVERY`；arXiv:2607.00272v1，first-public
  2026-06-30；已读 primitive traces、skill proposal/dedup/validation、library、transfer evaluation、real-robot
  demonstrations、Appendix 与 limitations。
- **Mechanism / State Flow**：系统从成功 primitive trace 中提出 parameterized skill，经过语义/执行验证后
  写入 library，后续任务检索、绑定参数并执行；library owner 必须保存 source trace、environment/tool version、
  validator evidence、supersession 与 rollback，而不能只存 prompt。论文流程仍依赖 Claude Opus 4.6 1M
  等组件，且 real robot 不是无监督 lifelong deployment。
- **Evidence / Failure Modes**：实验支持论文 tasks 中 skill reuse/transfer；不证明开放世界长期自治。新增错误
  abstraction、near-duplicate skills、parameter binding、environment drift 与 unsafe reuse。固定 workflow 在任务
  稳定、验证成本高时仍合理。
- **ROADMAP / Decision**：已读 Ch73～80；Ch80 已有 Skill registry/provenance，但缺 trace→candidate→
  validation→publish 的 lifecycle。`Refine — Existing Argument / Experimental`，主 owner Ch80，Ch74/77
  handoff；Gate 前不修改 Books。

### SkillCoach — 26/30

- **Source / Coverage**：`SKILLCOACH-RUBRIC-GROUNDED-TRAINING`；arXiv:2607.01874v1，first-public
  2026-07-02；已读 rubric induction、skill library、trajectory diagnosis/coaching、offline SFT construction、
  task/model evaluation、ablation、judge setup 与 limitations。
- **Mechanism / Evidence**：SkillCoach 先从 tasks/trajectories 形成 rubric-grounded skills，再以 criterion-level
  diagnosis 生成 coaching supervision，而非只用最终胜负。作者结果支持 selected offline SFT tasks 的提升；
  不证明 rubric 是 ground truth、不证明在线自改进或任意 task transfer。
- **Trade-off / Failure Modes**：获得可诊断的 criterion attribution，付出 rubric leakage、LLM-judge bias、
  skill overlap 和训练分布锁定；有确定 verifier 时直接 outcome/test evidence 仍优先。
- **ROADMAP / Decision**：已读 Ch25、Ch62、Ch76、Ch80；Ch62 已分离 rubric formation、criterion execution
  与 ranking，本文是该框架的 training-side reuse。`No Change — Already Covered / Experimental Case`；
  不因一个 coaching pipeline 重复正文。

### TACO Tool-Augmented Credit Optimization — 26/30

- **Source / Coverage**：`TACO-TOOL-CREDIT-OPTIMIZATION`；arXiv:2606.30251v1，first-public
  2026-06-29；已读 tool-augmented rollout、outcome-regime decomposition、credit objective、training、
  verifiable-task evaluation、ablations 与 limitations。
- **Mechanism**：TACO 按 tool/action 与最终 outcome 的组合把 trajectory 分成四类，对成功/失败且用/不用
  tool 的 tokens 施加不同 credit，而不是把同一 scalar reward 均匀广播到所有生成 token。credit owner 必须
  绑定 tool call/result、verifier、policy version 与 outcome；否则 role labels 会错配。
- **Evidence / Failure Modes**：作者实验限于 single-call、可验证任务，支持 typed credit 在该分布有用；
  不证明 multi-tool、delayed side effect 或 noisy outcome。新增错误归因、鼓励无必要 tool call、稀疏 regime
  与 verifier exploitation；短、单步任务的 sequence reward 仍合理。
- **ROADMAP / Decision**：已读 Ch29、Ch62、Ch74；Ch29 已有 token/trajectory credit 边界，但缺
  tool-role×outcome typed decomposition。`Refine — Existing Argument / Experimental`，主 owner Ch29。

### AutoMem — 27/30

- **Source / Coverage**：`AUTOMEM-MEMORY-SPECIALIST-EVOLUTION`；arXiv:2607.01224v1，first-public
  2026-07-01；已读 specialist architecture、meta-level proposal/evaluation loops、memory program evolution、
  game environments、baselines、ablations 与 limitations。
- **Mechanism / Ownership**：通用 Agent 不直接改写自己的 global memory policy；独立 memory specialist
  根据 episode evidence 提议 read/write policy，meta loop 在隔离 environment 中评估并选择版本。系统必须
  区分 task policy、memory policy、specialist checkpoint、evaluation episodes 与 promoted version。
- **Evidence / Failure Modes**：作者游戏实验支持 separate specialist + meta-selection 的收益；episode reset、
  synthetic games 和 independent specialist 限制外推，不证明跨用户 continuous memory。新增 optimizer-over-
  memory overfitting、promotion bias、版本漂移与 rollback complexity；静态 memory policy 在稳定任务仍合理。
- **ROADMAP / Decision**：已读 Ch73、Ch76、Ch80；Ch73 已有 derived memory/governance，本文补充 policy
  evolution 应在 evidence gate 外循环中发生。`Refine — Existing Argument / Experimental`，主 owner Ch73。

### PACE Proxy Agent Evaluation — 25/30

- **Source / Coverage**：`PACE-PROXY-AGENT-EVAL`；arXiv:2607.02032v1，first-public 2026-07-02；已读
  proxy construction、feature/selection procedure、leave-one-out/calibration、benchmarks、cost comparison、
  sensitivity 与 distribution-shift limitation。
- **Mechanism / Evidence**：PACE 从少量 full-agent runs 学习 proxy，在相同 task/model/harness distribution
  中选择能预测 expensive outcome 的便宜 signals。proxy model、calibration split、target agent/harness 和
  validity window 都是评估状态。它支持筛选/优先级，不应替代 final executable evaluation。
- **Trade-off / Failure Modes**：节省 evaluation cost，代价是 proxy Goodhart、distribution shift、ranking
  inversion 与 calibration debt；release gate、高风险 claim 仍需 full evaluator。
- **ROADMAP / Decision**：已读 Ch62、Ch66、Ch77；Ch62 已有 cheap→expensive cascade，但未明确 proxy 的
  distribution-bound validity。`Refine — Existing Argument / Experimental`，主 owner Ch62。

### Xiaomi-GUI-0 — 25/30

- **Source / Coverage**：`XIAOMI-GUI-0-REAL-DEVICE-AGENT`；arXiv:2606.31410v1，first-public
  2026-06-30；已读 real-device data/infrastructure、planner/executor、local reflection/replan、memory tags、
  training/evaluation、baselines、static/off-policy limitations 与 real-environment constraints。
- **Mechanism / State Flow**：planner 维护 task plan，executor 在真实 device observation 上行动；局部失败
  触发 reflection/replan，memory tags 记录可复用交互线索。device state、app/version、action coordinate、
  permission、side-effect 与 replay evidence 必须由 workflow/harness 拥有，模型文本不是 authoritative state。
- **Evidence / Failure Modes**：官方/论文结果证明该模型+harness 在所测 devices/tasks 的表现，不证明跨 OS、
  dynamic apps 或生产安全。新增 coordinate drift、stale observation、unintended side effect 和不可重放外部状态；
  确定 UI automation 在稳定流程仍更可靠。
- **ROADMAP / Decision**：已读 Ch62、Ch74～77；Ch77 已有 deterministic spine、replan、side-effect evidence，
  机制已覆盖。`No Change — Already Covered / Experimental System Case`。

### SWE-Together — 25/30

- **Source / Coverage**：`SWE-TOGETHER-INTERACTIVE-EVAL`；arXiv:2606.29957v1，first-public
  2026-06-29；已读 issue/task reconstruction、stateful user simulator、interaction protocol、grading、models、
  baselines、analysis 与 limitations。
- **Mechanism / Evidence**：benchmark 不是在静态 issue 上一次作答，而由 simulator 根据当前 patch、问题和
  对话状态发出后续 clarification/feedback，使被测对象成为 feedback-conditioned policy。它支持“交互会改变
  排名/失败类型”的受限结论，不证明 simulator 等价真实 maintainer，也不证明 production repo autonomy。
- **Trade-off / Chapters**：交互提高现实性，却引入 simulator policy、turn budget、state leakage 与 judge
  variance。静态 benchmark 仍适合 cheap regression 与 deterministic comparison。已读 Ch62、Ch77；Ch62
  已完整覆盖 snapshot→feedback-conditioned policy。
- **Decision**：`No Change — Already Covered`，作为独立实证链接保留。

### Are Performance-Optimization Benchmarks Reliably Measuring Coding Agents? — 27/30

- **Source / Coverage**：`PERF-BENCH-RELIABILITY`；arXiv:2607.01211v1，first-public 2026-07-01；当前
  HTML v2，已联读 v1 event。已覆盖 740 reference patches、four clouds/12 machine-round replays、metric
  recomputation、hard-tail analysis、discussion、threats to validity 与 released-artifact caveats。
- **Mechanism / Evidence**：论文把 reference patch 先跨机器重放，只有所有 rounds 满足原构造规则才进入
  后续分析；再比较 geometric/penalty 等 scoring aggregation。它证明一部分 performance labels 对 machine
  和 score formula 敏感，尤其接近零收益时；不证明其保守 all-replay rule 是唯一正确标准。
- **Trade-off / Failure Modes**：更严格 replay 减少噪声 label，却可能丢弃真实但环境敏感的优化；多次测量
  增加成本，reference artifact 仍可能不完整。应绑定 hardware/software/workload/statistic，而不是把分数直接
  当 Agent capability。
- **ROADMAP / Decision**：已读 Ch62～66；Ch62 已有 noisy measurement/replay contract，但本论文提供
  cross-machine reference validation 与 score-sensitivity 的强机制证据。`Refine — Existing Argument`，
  主 owner Ch62。

### QVal — 26/30

- **Source / Coverage**：`QVAL-DENSE-SIGNAL-EVALUATION`；arXiv:2606.32034v1，first-public
  2026-06-30；已读 state-action Q alignment、dataset construction、direct-prompting/other signal families、
  multiple environments/models/modalities、ranking/statistical analysis 与 discussion；无独立 limitations 章节。
- **Mechanism / Evidence**：QVal 用后续 return/target Q 对齐来衡量每步 dense score 是否真的保留长期 outcome
  排序，而不是先训练完整 policy 再看终局。它支持便宜比较 supervision signals，并发现所测设置中简单 direct
  prompting 很强；不证明该 signal 在训练闭环仍最优，也不替代 policy learning evaluation。
- **Trade-off / Failure Modes**：获得早期筛选速度，付出 target-Q estimation、behavior-policy coverage、
  horizon truncation 与 offline correlation 风险；被筛出的 signal 仍需 end-to-end training/held-out outcome。
- **ROADMAP / Decision**：已读 Ch29、Ch62；Ch62 已有 scorer evidence，但缺“dense signal 先验证与 long-
  horizon return 对齐”的 gate。`Refine — Existing Argument / Experimental`，主 owner Ch62，Ch29 handoff。

### TRIAGE Role-Typed Credit Assignment — 27/30

- **Source / Coverage**：`TRIAGE-ROLE-TYPED-CREDIT`；arXiv:2606.32017v1，first-public 2026-06-30；
  已读 role taxonomy、credit estimator、training/control flow、search/reasoning experiments、baselines、10-run
  protocol（search exception）、ablation 与 limitations。
- **Mechanism**：trajectory tokens/actions 先按 proposal、critique、verification 等 role 分型，再按 role 与
  outcome 估计 credit，使同一最终 reward 不再等权传播。role assigner、trajectory schema、credit estimator、
  policy checkpoint 与 verifier 必须共同版本化；分类错误会系统性改变 gradient。
- **Evidence / Failure Modes**：作者实验支持所测任务的 role-typed credit；不证明 taxonomy 跨 Agent/harness
  稳定，search single-run 也限制不确定性判断。新增 role leakage、estimator bias、rare-role variance 与额外
  inference cost；短 homogeneous trajectory 仍可用 sequence-level advantage。
- **ROADMAP / Decision**：已读 Ch29、Ch62、Ch74～78；Ch29 已覆盖 trajectory/token credit，本文提供
  action-role 中间层。`Refine — Existing Argument / Experimental`，主 owner Ch29；不得把作者结果外推成
  通用 multi-agent credit recipe。

### RESOURCE2SKILL — 28/30

- **Source / History / Coverage**：`RESOURCE2SKILL-MULTIMODAL-WIKI`；arXiv:2606.29538v1，first-public
  2026-06-30，故从 W30 display feed 回拨 W27；当前 HTML 为 v4，revision-sensitive 联读。已覆盖四阶段
  pipeline、skill tuple/schema、five deterministic gates、hierarchical retrieval、MCP execution、offline/online
  pool separation、七领域/四 backends evaluation、source/representation/selection ablations、human A/B、failure
  cases、storage schema 与 limitations。
- **Problem / Previous Design / Changed Constraint**：把原始视频、代码库、文章或 reference artifact 直接塞入
  context 是合理的通用旧方案，却让长资源、视觉/时序细节与执行片段难以在每次任务中稳定绑定；纯 Agent
  自生成 trace skill 又受已知能力上限。重复 authoring tasks 使离线蒸馏、版本化与复用开始值得其治理成本。
- **Mechanism / Ownership / Flow**：construction operator 将 source 转成
  `(taxonomy path, text, visual, code, metadata/provenance)`；五个 deterministic gates 检查 schema、provenance、
  duplicate、modality 与 executable smoke test。MetaBrowse 先按 taxonomy/BM25 缩小候选，再由 model 选零个或
  多个 skills；code 可经同一 MCP surface 直接执行。缺口触发 online acquisition，但临时 pool 与 offline
  default library 隔离，不静默污染主索引。
- **Evaluation Contract / Evidence**：七个 commercial-authoring domains，每域 matched 80 briefs，四个
  GPT backends；artifact 主要由 GPT-5.4 vision judge、Reaper 由 audio judge，另有 200 个 blinded human votes。
  ablation 支持 source diversity、multimodal entry、hierarchy/selection 与 online gap-filling 在该合同内有贡献；
  不证明 raw-resource RAG 的 matched-budget 比较（论文明确未做），不证明无 programmatic tool/public resource
  的领域，也不证明 judge score 是生产 outcome。
- **Trade-offs / Failure Modes**：获得可检索、可执行、带 provenance 的 procedural memory，付出 distillation
  latency、library growth、validation/versioning、parameter binding 和 selection cost。失败案例显示 partial
  grounding、unresolved formulas、过度字面组合可比 no-skill 更差；raw retrieval/hand-authored skills 在资源少、
  task 稳定或高风险需人工验证时仍合理。
- **Evolution / ROADMAP / Decision**：`Direct Evolution`：raw resource retrieval → distilled text/code skill →
  multimodal hierarchical skill → controlled online acquisition。已读 Ch72～74、Ch77、Ch79～80；Ch80 已有
  Skill artifact/provenance，但缺 source ingestion、deterministic acceptance 与 online/offline pool boundary。
  `Refine — New Mechanism / Experimental`，主 owner `AGENT-PLATFORM`；Context/RAG 只保留 retrieval handoff，
  resource-to-Skill admission 已写入正文。

### Recovered Full Source Review — AgenticSTS — 26/30

- **Source / Coverage / Version**：已读 arXiv:2607.02255v1（2026-07-02）HTML 的 architecture、五层 memory
  contract、fixed-A0 decomposition、cross-backbone probe、auto-mode ladder、同代码 accumulating-context variant、
  external-agent comparison、统计附录、完整 prompt exhibits；并核验作者 GitHub 与公开 trajectory dataset。
- **Original Problem / Previous Design / Changed Constraint**：把 transcript、tool calls 与 reflection 逐轮追加，
  在短任务里忠实且实现简单；长程决策却让输入随 horizon 增长，并混合 rule、state、episode 与 strategy，难以
  归因某层 evidence。需要的不只是更大 context，而是明确每次 decision 被允许看见什么。
- **Mechanism / State Ownership / Flow**：每次决策从新 user message 开始，由固定 protocol `L1`、state schema
  `L2`、retrieved rules `L3`、episodic summary `L4` 与 triggered skills `L5` 合成；不附加跨决策 raw transcript。
  `L1/L2` 固定，`L3` 按 patch 更新，`L4/L5` 只有 postrun writer 可修改并带 condition/SHA。memory state 因此从
  无类型历史变成有 owner、预算、mutability 与 ablation handle 的 visibility contract。
- **Evaluation / What It Proves**：298 条 completed trajectories 中，fixed-A0 五条件每 cell 10 runs；skill rows
  的观察值为 6/10，no-scaffold 3/10，但 Fisher test 与 Wilson interval 不支持显著性排名。跨 backbone 每 cell
  仅 5 runs，Gemini-derived frozen store 提升 Qwen mean score、降低 DeepSeek mean score且两者均 0/5 wins。
  作者还对比两个 transcript-accumulating agents，但 harness、batching 与 action protocol 不匹配。因此证据支持
  bounded typed contract 的可审计性与成本边界，不证明其普遍优于 matched accumulating-context agent。
- **Trade-offs / Failure Modes / Previous Design Boundary**： bounded retrieval 控制 prompt growth、支持逐层审计，
  但引入 retrieval miss、stale rule、summary loss、skill contamination、writer governance 与 backbone-sensitive
  transfer。短 horizon、强缓存或要求逐字取证时，raw transcript 仍是合理 source of truth；typed memory 应保留
  provenance 与回退路径，而非覆盖原始轨迹。
- **Evolution / ROADMAP / Decision**：`Direct Evolution`：append history → retrieve history → typed bounded memory
  contract → postrun-derived episode/skill with provenance。已读 Ch71～74；主 owner Ch73，Ch62 只保留小样本、
  harness confounding 与 reusable trajectory handoff。`Refine — New Mechanism / Experimental`；bounded typed
  visibility 已写入 `AGENT-MEMORY`。

## Final Books Integration Ledger

| # | Candidate / Source Family | Final disposition | Stable owner / evidence |
| ---: | --- | --- | --- |
| 1 | GeneBench-Pro | Weekly Only — Domain Evaluation Fact | PLATFORM-EVALUATION-SYSTEM；领域 benchmark 不改通用 EvalSpec |
| 2 | TabFM | Weekly Only — Model/Product Fact | MODEL-ARCHITECTURE；未公开可迁移系统机制 |
| 3 | Brain2Qwerty v2 | Weekly Only — Research Fact | MULTIMODAL-REPRESENTATION；领域采集合同不足 |
| 4 | Seed2.0 Model Card | Weekly Only — Model Card Fact | MODEL-ARCHITECTURE；能力/训练声明不反推机制 |
| 5 | Asynchronous Pipeline Parallel | Refine — Existing Argument | TRAIN-PIPELINE-PARALLEL；fixed delay 与 optimizer/error-feedback 演进已复核 |
| 6 | ELDR | Refine — Existing Argument | INFER-DYNAMO；conditional-compute locality 已复核 |
| 7 | HiLS-Attention | No Change — Already Covered | MODEL-ATTENTION；selector error 与 sparse access 边界已有具体论点 |
| 8 | Overthinking publication node | No Change — Revision Dedup | PLATFORM-EVALUATION-SYSTEM；2025 family 的 publication-state node |
| 9 | Seed2.0 duplicate score row | Duplicate Source-Family Row | 同 #4；不重复计算 unique disposition |
| 10 | Orca world model | Refine — Existing Argument | MULTIMODAL-WORLD-MODELS；action-conditioned latent transition |
| 11 | Program-as-Weights | Refine — New Mechanism | TRAIN-LORA；specification-to-neural-program compilation |
| 12 | Scaling the Horizon | Refine — Existing Argument | TRAIN-DISTILLATION；domain-routed on-policy distillation |
| 13 | BlockPilot | Refine — Existing Argument | INFER-SPECULATIVE-DECODING；prefix-conditioned block control |
| 14 | AgenticSTS | Refine — New Mechanism | AGENT-MEMORY；bounded typed visibility and post-run writer |
| 15 | FlashMorph | Refine — Existing Argument | MODEL-ATTENTION；global budgeted hybrid placement |
| 16 | EvoPolicyGym | No Change — Already Covered | PLATFORM-EVALUATION-SYSTEM；policy/environment identity 已覆盖 |
| 17 | AgenticDataBench | No Change — Already Covered | TRAIN-DATA；Agent data contract 已覆盖 |
| 18 | WorldDirector | Refine — Existing Argument | MULTIMODAL-WORLD-MODELS；explicit object/world state |
| 19 | MemSyco-Bench | Refine — Existing Argument | AGENT-MEMORY；memory-risk 与 sycophancy evidence boundary |
| 20 | Metacognitive Feedback | Refine — Existing Argument | AGENT-REFLECTION；feedback provenance and authority |
| 21 | MemLearner | Refine — Existing Argument | AGENT-MEMORY；video/world-memory derived state |
| 22 | ASPIRE | Refine — Existing Argument | AGENT-PLATFORM；trajectory-to-Skill admission |
| 23 | SkillCoach | No Change — Already Covered | AGENT-PLATFORM；fault-localized patch / held-out Gate 已覆盖 |
| 24 | TACO | Refine — Existing Argument | TRAIN-REINFORCEMENT-LEARNING；tool/process credit boundary |
| 25 | AutoMem | Refine — Existing Argument | AGENT-MEMORY；derived memory admission and rollback |
| 26 | PACE | Refine — Existing Argument | PLATFORM-EVALUATION-SYSTEM；process/outcome evidence split |
| 27 | Xiaomi-GUI-0 | No Change — Already Covered | AGENT-TOOLS；GUI action/environment contract 已覆盖 |
| 28 | SWE-Together | No Change — Already Covered | AGENT-WORKFLOW；interactive collaboration harness 已覆盖 |
| 29 | Performance-Optimization Benchmark Reliability | Refine — New Mechanism | PLATFORM-EVALUATION-SYSTEM；reference-artifact replay |
| 30 | QVal | Refine — New Mechanism | PLATFORM-EVALUATION-SYSTEM；dense proxy/future-return alignment |
| 31 | TRIAGE | Refine — Existing Argument | TRAIN-REINFORCEMENT-LEARNING；role-typed credit assignment |
| 32 | RESOURCE2SKILL | Refine — New Mechanism | AGENT-PLATFORM；multimodal resource-to-Skill admission |
| 33 | NVIDIA Secure Agent Workspace | Refine — New Mechanism | AGENT-PLATFORM；long-lived workspace isolation lifecycle |
| 34 | TensorRT Edge-LLM v0.9.0 | Weekly Only — Version Fact | INFER-EXECUTION；support matrix 不构成机制证据 |

计数以 33 个唯一 source family 为准：`Refine 21 / No Change 7 / Weekly Only 5`；第 9 行仅记录
Seed2.0 跨来源表重复关系，不形成第二个 family 或第二次 Books 决策。

## Blocked Primary-Source Backlog

2026-08-13 精确 identity 重试现已恢复原 22 个 backlog identities 的全部 HTML 正文；Orca、Scaling the
Horizon、BlockPilot、Morphing into Hybrid Attention、EvoPolicyGym、AgenticDataBench、WorldDirector、
MemSyco-Bench、Metacognitive Feedback、MemLearner、ASPIRE、SkillCoach、TACO、AutoMem、PACE、Xiaomi-GUI-0、
SWE-Together、Performance Benchmark Reliability、QVal、TRIAGE 与 RESOURCE2SKILL 现均已完成 method、
evaluation、limitations/披露缺口、关键 Appendix 和相邻章节审计，普通 review pending 已清零。

AgenticSTS 也已完成上述全文、统计边界、公开 artifact 与相邻章节审计。W27 当前无 source-level blocked family；
Forward Candidate Evidence Gate 以 33/33 通过，cursor 进入 W28。更广 discovery 与全历史 Historical Evidence
Gates 仍保持 Open。

## Repository Changes

- 删除已被 W27 完整吸收的 `papers/2026/06/29/README.md` 与
  `papers/2026/06/30/README.md`；
- 删除已被 W27 完整吸收的 `papers/2026/07/01/README.md`；
- 补全 W27 为 2026-06-29～2026-07-05 的完整 ISO week，不再按月份截断；
- 全量重审后 refine Ch34、Ch48；
- 更新 `CODEX_DAILY_RESEARCH_PROMPT.md`，固化 Live Daily 每日生成、历史回填只生成
  Weekly，以及 Weekly 只在 Sunday 按完整 ISO week 生成的规则；
- 同步更新现有 Daily Research 自动化的条件式 Weekly 流程（自动化配置不在仓库内）；
- 验证并保留 `books/part-04-training-system/38-pipeline-parallel.md` 的 asynchronous PP 演进；
- refine `books/part-05-inference-system/52-dynamo.md` 的 conditional service cost；
- W27 从 9 个评分行扩展为 34 个评分行、33 个 unique families；RESOURCE2SKILL 完成全文后评分为
  28/30。共 33/33 unique `20+` families 完成非模板化 Full Source Review，AgenticSTS blocker 已恢复，
  0 ordinary pending；Forward Candidate Evidence Gate 通过并推进 W28；10 个 display-feed spillback 按
  v1 回拨 W26；
- W27 Books Gate 通过后，refine `TRAIN-LORA` 的 specification-to-neural-program artifact、
  `AGENT-MEMORY` 的 bounded visibility、`AGENT-PLATFORM` 的 resource/trace-to-Skill admission 与 secure
  workspace lifecycle，以及 `PLATFORM-EVALUATION-SYSTEM` 的 reference replay / proxy alignment；
- asynchronous Pipeline Parallel 与 ELDR 的既有正文经全文和相邻章节复核后保留，不重复添加论文摘要；
- 新增 34 行 final ledger，闭合 33 个唯一 source family 的 owner、去重关系和最终 disposition；
- 未修改 ROADMAP、未新增章节或 Part。

## Open Questions

1. Muon 对 fixed one-step delay 的稳健性能否扩展到更大模型、MoE 与生产故障恢复？
2. Prefill expert signature 在长输出、tool calling 或 domain drift 下能维持多长预测有效期？
3. expert locality 与 prefix locality 冲突时，router 应怎样把两类复用收益放进同一 cost model？
4. HiLS 的 selector error 能否在 production trace 上转换为可观测的 quality/SLO guardrail？
5. synthetic benchmark / pretraining 与真实 scientific、tabular workload 的 gap 如何量化？
6. ELDR 的 routing metadata freshness、ownership 与故障恢复 contract 应由哪个组件负责？
7. Neural program artifact 应怎样做 behavioral signature、supply-chain verification、revoke 与 rollback？
8. Secure Agent Workspace 的 multi-tenant isolation、workspace recovery 与 policy-version skew 是否有公开
   failure-test / production evidence？
9. TensorRT Edge-LLM v0.9.0 的支持矩阵能否提供绑定硬件、模型、精度、长度、并发和 SLO 的公开验证？
10. resource/trace-derived Skill 的 temporary pool、跨模态 dedup 与 held-out evaluator 能否在真实 catalog 中提供
    可复现的误接纳率、撤销延迟和权限传播证据？

## Sources

### 模型与研究机构

- OpenAI, “Introducing GeneBench-Pro,” published 2026-06-30; accessed 2026-07-31:
  https://openai.com/index/introducing-genebench-pro/
- Google Research, “Introducing TabFM: A zero-shot foundation model for tabular data,”
  published 2026-06-30; accessed 2026-07-31:
  https://research.google/blog/introducing-tabfm-a-zero-shot-foundation-model-for-tabular-data/
- Meta AI, “From Brain Waves to Words: Brain2Qwerty Offers a New Path to Communication
  Without Surgery,” published 2026-06-29; accessed 2026-07-31:
  https://ai.meta.com/blog/brain2qwerty-brain-ai-human-communication/
- Google DeepMind, “Towards Structural Understanding of LLM Overthinking,” publication page
  dated 2026-07-02; accessed 2026-07-31:
  https://deepmind.google/research/publications/203490/
- Anthropic Research, accessed 2026-07-31:
  https://www.anthropic.com/research
- Google Research Blog, accessed 2026-07-31:
  https://research.google/blog/
- ByteDance Seed Blog, accessed 2026-07-31:
  https://seed.bytedance.com/en/blog
- Qwen Code Weekly Updates, accessed 2026-07-31:
  https://qwenlm.github.io/qwen-code-docs/en/blog/updates/

### 论文与发现索引

- Zmushko et al., “One-Step Gradient Delay is Not a Barrier for Large-Scale Asynchronous
  Pipeline Parallel LLM Pretraining,” submitted 2026-06-29; accessed 2026-07-31:
  https://arxiv.org/abs/2606.30634
- Choi et al., “ELDR,” submitted 2026-07-01; accessed 2026-07-31:
  https://arxiv.org/abs/2607.00466
- Hu et al., “Hierarchical Sparse Attention Done Right,” submitted 2026-07-03; accessed
  2026-07-31:
  https://arxiv.org/abs/2607.02980
- Zhang et al., “Towards Structural Understanding of LLM Overthinking,” first submitted
  2025-10-09; accessed 2026-07-31:
  https://arxiv.org/abs/2510.07880
- ByteDance Seed, “Seed2.0 Model Card,” submitted 2026-06-30; accessed 2026-07-31:
  https://arxiv.org/abs/2607.00248
- Hugging Face Daily Papers, discovery only, 2026-06-29 and 2026-06-30; accessed
  2026-07-31:
  https://huggingface.co/papers/date/2026-06-29
  https://huggingface.co/papers/date/2026-06-30
- Hugging Face Daily Papers, discovery only, 2026-07-02; accessed 2026-07-31:
  https://huggingface.co/papers/date/2026-07-02
- Google Scholar: https://scholar.google.com/
- Semantic Scholar: https://www.semanticscholar.org/
- OpenAlex: https://openalex.org/
- DBLP: https://dblp.org/
- Hugging Face Weekly Papers, display week 2026-W27（discovery only；按 arXiv v1 归周），
  accessed 2026-08-09: https://huggingface.co/papers/week/2026-W27
- Zhang et al., “Program-as-Weights,” arXiv:2607.02512v1, first-public 2026-07-02,
  accessed 2026-08-09: https://arxiv.org/abs/2607.02512
- Program-as-Weights full HTML: https://arxiv.org/html/2607.02512v1
- Program-as-Weights author artifacts/SDKs: https://github.com/programasweights
- Orca: https://arxiv.org/abs/2606.30534
- Scaling the Horizon: https://arxiv.org/abs/2606.30616
- BlockPilot: https://arxiv.org/abs/2606.31315
- AgenticSTS: https://arxiv.org/abs/2607.02255
- Morphing into Hybrid Attention Models: https://arxiv.org/abs/2606.30562
- EvoPolicyGym: https://arxiv.org/abs/2607.02440
- AgenticDataBench: https://arxiv.org/abs/2607.01647
- WorldDirector: https://arxiv.org/abs/2607.02517
- MemSyco-Bench: https://arxiv.org/abs/2607.01071
- Metacognitive Feedback: https://arxiv.org/abs/2606.32032
- MemLearner: https://arxiv.org/abs/2606.31734
- ASPIRE: https://arxiv.org/abs/2607.00272
- SkillCoach: https://arxiv.org/abs/2607.01874
- TACO: https://arxiv.org/abs/2606.30251
- AutoMem: https://arxiv.org/abs/2607.01224
- PACE: https://arxiv.org/abs/2607.02032
- Xiaomi-GUI-0: https://arxiv.org/abs/2606.31410
- SWE-Together: https://arxiv.org/abs/2606.29957
- Performance-Optimization Benchmark Reliability: https://arxiv.org/abs/2607.01211
- QVal: https://arxiv.org/abs/2606.32034
- TRIAGE: https://arxiv.org/abs/2606.32017
- RESOURCE2SKILL: https://arxiv.org/abs/2606.29538

### AI Infra

- PyTorch Releases, accessed 2026-07-31:
  https://github.com/pytorch/pytorch/releases
- vLLM Releases, accessed 2026-07-31:
  https://github.com/vllm-project/vllm/releases
- SGLang Releases, accessed 2026-07-31:
  https://github.com/sgl-project/sglang/releases
- NVIDIA Dynamo Releases, accessed 2026-07-31:
  https://github.com/ai-dynamo/dynamo/releases
- NVIDIA, “How to Govern Autonomous Agents in Enterprise AI Factories,” published
  2026-06-29; accessed 2026-08-12:
  https://developer.nvidia.com/blog/how-to-govern-autonomous-agents-in-enterprise-ai-factories/
- NVIDIA Secure Agent Workspace Reference Design, last updated 2026-06-28; accessed 2026-08-12:
  https://docs.nvidia.com/enterprise-reference-architectures/secure-agent-workspace-reference-design/latest/index.html
- NVIDIA Secure Agent Workspace reference architecture, accessed 2026-08-12:
  https://docs.nvidia.com/enterprise-reference-architectures/secure-agent-workspace-reference-design/latest/reference-architecture.html
- NVIDIA OpenShell repository, current artifact-state boundary; accessed 2026-08-12:
  https://github.com/NVIDIA/OpenShell/
- NVIDIA TensorRT Edge-LLM v0.9.0 release discussion, released 2026-07-03; accessed 2026-08-12:
  https://github.com/NVIDIA/TensorRT-Edge-LLM/discussions/123
