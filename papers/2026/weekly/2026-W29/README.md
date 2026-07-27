# AI Research Weekly — 2026-W29

> Coverage Window: 2026-07-13～2026-07-19
> Research Mode: Retrospective Backfill
> Accessed: 2026-07-31
> Backfilled: 2026-07-31
> Discovery Review Reopened: 2026-08-09
> Re-audit Status: 38/38 source families have final Books dispositions; 22 Refine, 9 No Change, 2 Weekly Only, 1 Disputed, 4 Unverified / Blocked; 34/38 Full Source Reviews complete under blocked-skip; W29 Source-Family Books Gate passed and cursor advances to W30; broader Archive/Discovery Gate remains Open

## Executive Summary

本周的最高信号是 Kimi K3 于 7 月 16 日首次公开。官方 Blog 把 2.8T MoE、hybrid attention、
low-precision training、expert-parallel static shapes、long-context prefix cache 与 supernode
部署放在同一个设计叙事里，长期价值是展示模型结构会反向约束训练和 serving runtime。
技术报告与权重在 7 月 27 日才公开，因此本周记录必须区分：

- 7 月 16 日：官方模型 Blog / first public announcement；
- 7 月 27 日：技术报告与权重，已由 7 月 29 日 Daily 深入核验。

论文侧重新播放 7 月 13～19 日的发现源后，候选从 3 篇恢复为 23 篇。除 Harness Handbook、
Ring-Zero 与 AgentCompass 外，新增 SearchOS、SEED、LongStraw、on-policy distillation、
agent failure attribution、harness-evolution evaluation、personal memory 与 world/action model
等来源。它们共同显示：长期 Agent 的主要矛盾已从“能否调用工具”扩展到共享状态、证据图、
失败归因、训练反馈和评测隔离。SearchOS 先完成全文复核；2026-08-13 exact HTML recovery 随后使
19 个新增候选中的 15 个完成全文、归周、评分与相邻章节审计，另 4 个保留为
`Unverified / Blocked Backlog`，没有被误记为 Full Source Review。
Infra 侧 Transformers 与 Ray 都是 patch
release，只记录 correctness/migration 信号，不进入 Books。

2026-08-11 Daily 的 first-public-date 去重还暴露一个未真正回写 owner week 的 family：
`Training Variable Long Sequences with Data-Centric Parallel`（arXiv:2608.07524）v1 为 2026-07-14。
随后 W30 attribution repair 又恢复 11 个 7 月 16～19 日 identities；其中 OPD²、Recursive Harness
Self-Improvement、Muon Agentic RL、Xiaomi-Robotics-1、DSWorld 与 Cost-Aware Security Agents 已完成全文、
appendix、公开 artifact（若可访问）与相邻章节审计并正式评分；SeerGuard 随后也完成论文、指标、附录、
项目页、评测仓库、模型权重与相邻章节审计；Environment-free API data 随后也完成 82 页 v1、
实现/评测附录与章节去重。2026-08-13 又恢复 15 个 expanded sources 和 4 个 spillbacks；最终只剩
Multi-Agent Exploration、AI Scientist Capability、Generative Compilation 与 LongStraw 四项 blocked。
不能从标题推断算法、state ownership 或 workload contract。

## Coverage Window and Limitations

- 对 Kimi K3 只把 7 月 16 日 Blog 中已公开的架构和系统事实归入本周；7 月 27 日技术报告
  作为 post-window verification，不改写首次发布日期。
- Hugging Face Daily Papers 的 7 月 16 日榜单用于 discovery；所有保留论文回到 arXiv v1。
- Kimi 与 Ring-Zero 的 benchmark 多为作者自报；未同时披露模型、硬件、输入输出、并发、
  精度/量化和 SLO 的数字不写成跨系统结论。
- 国内机构若只有 GitHub activity 或聚合页而无日期明确的官方材料，标记 coverage limitation，
  不依据搜索摘要补全。
- arXiv `2607.10350`（ABot-AgentOS）与 `2607.10463`（GRASP）虽在本周榜单再次出现，v1 均为
  7 月 11 日，回归 W28；Weak-to-Strong Direct OPD、LLM forecaster、PolicyShiftGuard 与
  Root Causes 同理由 v1 日期回归 W28，不按榜单日期重复计数。

## Discovery Recall Ledger

| Ledger Item | Current Count | Review Result |
| --- | ---: | --- |
| Score rows / candidate families | 38 / 38 | 34 Full Source Reviews complete；4 Unverified / Blocked Backlog；0 ordinary pending |
| Fixed source coverage | Passed | official/model and infra rows retained；Transformers/Ray patch boundaries reviewed；academic spillback identity recorded |
| Academic discovery window | Expanded | Hugging Face day feeds + arXiv v1 metadata replayed；cross-index closure pending |
| W29 Evidence Gate | Forward checkpoint passed | 4 项连续不可访问来源按 blocked-skip 规则进入 backlog；broader discovery/Historical Evidence Gate 仍 Open |

## 1. 模型与研究机构

### Source Coverage

按固定顺序扫描：

| Order | Sources | Result |
| --- | --- | --- |
| 1–5 | OpenAI；Anthropic；Apple ML Research；Google DeepMind；Google Research | Anthropic values research（7 月 13 日）保留为 evaluation signal；Google Research diffusion creativity（7 月 15 日）与 bioresilience（7 月 16 日）不改变本书系统主线 |
| 6–14 | Meta AI / FAIR；Microsoft Research；NVIDIA Research；xAI；Amazon Science；Cohere Labs；Ai2；Mistral AI；Alibaba Qwen | Qwen Code 7 月 16 日周更 Record Only；其余无高门槛模型发布 |
| 15–25 | DeepSeek；Moonshot / Kimi；Zhipu；MiniMax；ByteDance Seed；Baidu ERNIE；Tencent Hunyuan；Huawei Noah；Shanghai AI Lab / InternLM；StepFun；Xiaomi MiMo | Kimi K3 与 PerceptionBench 于 7 月 16 日首次公开；其余无可核验高门槛更新 |
| 26–27 | InclusionAI / Ant Group；Hugging Face Blog | 无需独立深入分析的模型研究 |
| Weekly | LG AI Research；Sakana AI；01.AI；Baichuan；ModelBest；BAAI；Salesforce；IBM；Databricks / Mosaic | 未发现本窗口内需提升为 Must Read 的官方发布 |

### Candidate Scoring

| Candidate | Technical Novelty | System Impact | Practical Value | Source Reliability | Project Relevance | Longevity | Total | Decision |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| Kimi K3 first public announcement | 5 | 5 | 4 | 4 | 5 | 5 | 28/30 | Must Read；已归并 Weekly；Books 已评估 |
| PerceptionBench | 3 | 3 | 3 | 4 | 4 | 4 | 21/30 | Worth Watching；与 K3 同日记录 |
| Claude values across models/languages | 3 | 3 | 3 | 5 | 3 | 4 | 21/30 | Worth Watching；Weekly only |

### Deep Analysis 1 — Kimi K3：Architecture 与 Runtime 的约束传播

- Published / First Public Version: 2026-07-16
- Technical Report: 2026-07-27（post-window verification）
- Status: Official announcement；完整机制以 7 月 27 日技术报告为准
- Primary Source: https://www.kimi.com/blog/kimi-k3

#### Why

当模型扩展到高稀疏 MoE 与超长上下文，参数规模不只是 training capacity 问题。expert
working set、attention state、低精度格式、all-to-all domain 与 prefix cache 都会进入训练
稳定性和 serving cost。

#### Principle

模型架构会形成跨层约束链：

```text
attention / MoE structure
-> optimizer and numeric format
-> expert-parallel communication shape
-> cache state representation
-> runtime kernel and routing
-> deployment topology
```

局部参数最优不保证端到端系统可部署。

#### Mechanism

7 月 16 日官方 Blog 声明 K3 为 2.8T 参数模型，使用 Kimi Delta Attention、Attention
Residuals 与 `16/896` routed experts 的 Stable LatentMoE；SFT 起使用 MXFP4 weights /
MXFP8 activations 的 QAT；expert-parallel training 强调 static shapes 与 critical path 无
host synchronization。官方还说明 KDA 改变传统 prefix caching，需要配套 vLLM 实现，并
建议在 64+ accelerators 的 supernode communication domain 部署。

#### Trade-off

更高 sparsity 降低 active compute，却把 routing balance、expert communication 和 weight
locality推到一阶问题；linear/hybrid attention 降低长序列代价，却引入 recurrent state 与
cache compatibility；低精度改善容量与带宽，却需要训练/rollout/kernel 一致性。官方 Blog
中的 scaling efficiency、价格与 benchmark 均为厂商主张，不能脱离硬件和 harness 外推。

#### Connection

知识树位置：第 14～17 章 Attention/MoE → 第 30、33～36 章训练并行 → 第 43、47～52 章
KV/runtime/scheduling。7 月 29 日 Daily 已用技术报告完整分析；本记录修正时间线，不重复
改写 Books。

#### Evolution

从 Dense full attention，到 MoE + MLA/KDA + low precision，再到 runtime-specific cache
state 与 supernode deployment，演化方向是 model/system co-design。下一步应观察开源
runtime 是否稳定承载 hybrid state paging，以及非 supernode topology 的代价。

### PerceptionBench — Evaluation Signal

Kimi Team 从 42 个既有 benchmarks 的模型失败中归纳 10 类 atomic perception capabilities，
再发布 3,000 个经过验证、尽量剥离 reasoning/knowledge confounders 的问题。长期原则是先
解耦 perception、reasoning 与 external knowledge，再解释总分；但 benchmark 构造、model
selection 与 contamination 仍需独立复核，因此不据此改写 multimodal 设计结论。

### Claude Values — Evaluation Signal

Anthropic 将 339 个高层 values 压缩为四个 axes，并比较模型和 20 种语言。官方指出四轴只
解释约 15% variation，且观察到的是 expressed values，不是模型“内在价值”。其长期启发是
post-training behavior 必须按 model × language × task distribution 分层评估，而非依赖单一
English aggregate；当前证据更适合 Weekly 与第 62 章未来 Review。

## 2. 论文与学术来源

### Candidate Scoring

| Candidate | Technical Novelty | System Impact | Practical Value | Source Reliability | Project Relevance | Longevity | Total | Decision |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| Harness Handbook | 4 | 4 | 4 | 3 | 5 | 4 | 24/30 | Worth Watching；深入分析；Weekly only |
| Ring-Zero | 4 | 4 | 3 | 3 | 4 | 4 | 22/30 | Worth Watching；Weekly only |
| AgentCompass | 3 | 4 | 4 | 3 | 5 | 4 | 23/30 | Worth Watching；深入分析；Weekly only |
| LightMem-Ego | 4 | 3 | 4 | 3 | 5 | 4 | 23/30 | Full Source Review complete；No Change — Ch73 already covers hierarchy/provenance |
| AdvancedMathBench | 3 | 3 | 4 | 4 | 5 | 4 | 23/30 | Full Source Review complete；No Change — Ch62 already covers verifier validity |
| Proxy-Guided Update Signals | 5 | 4 | 4 | 3 | 5 | 4 | 25/30 | Full Source Review complete；Refine `TRAIN-GRPO` |
| Multi-Agent LLMs Fail to Explore Each Other | 4 | 4 | 4 | 4 | 5 | 4 | 25/30 | Unverified / Blocked Backlog；coordination failure |
| Function-Aware Fill-in-the-Middle | 4 | 4 | 4 | 3 | 5 | 4 | 24/30 | Full Source Review complete；Refine `TRAIN-PRETRAINING` |
| Read It Back / SpectraReward | 4 | 3 | 4 | 3 | 5 | 4 | 23/30 | Full Source Review complete；Refine `TRAIN-GRPO` |
| Capability-Oriented Benchmark for AI Scientists | 3 | 3 | 4 | 4 | 4 | 4 | 22/30 | Unverified / Blocked Backlog；claim-conditioned evaluation |
| KnowAct-GUIClaw | 4 | 4 | 4 | 3 | 5 | 4 | 24/30 | Full Source Review complete；No Change — Ch73/80 already cover derived skills and governance |
| Tracing Agentic Failure from the Flow of Success | 5 | 4 | 4 | 3 | 5 | 4 | 25/30 | Full Source Review complete；Refine `PLATFORM-TRACE` |
| ShortOPD | 4 | 4 | 4 | 3 | 5 | 4 | 24/30 | Full Source Review complete；Refine `TRAIN-GRPO` |
| PalmClaw | 4 | 4 | 4 | 3 | 4 | 4 | 23/30 | Full Source Review complete；Refine `AGENT-PLATFORM` |
| Generative Compilation | 4 | 4 | 4 | 4 | 4 | 4 | 24/30 | Unverified / Blocked Backlog；compiler feedback loop |
| LongStraw | 5 | 5 | 4 | 3 | 5 | 4 | 26/30 | Unverified / Blocked Backlog；long-context RL system |
| SEED | 5 | 5 | 4 | 3 | 5 | 5 | 27/30 | Full Source Review complete；Refine `TRAIN-GRPO` |
| SearchOS-V1 | 5 | 5 | 5 | 4 | 5 | 4 | 28/30 | Full Source Review complete；No Change |
| On-Policy Delta Distillation（OPD²） | 5 | 5 | 4 | 4 | 5 | 5 | 28/30 | Full Source Review complete；Refine `TRAIN-GRPO` |
| Recursive Harness Self-Improvement（RHI） | 5 | 5 | 4 | 3 | 5 | 5 | 27/30 | Full Source Review complete；Refine `AGENT-WORKFLOW` |
| When Does Muon Help Agentic Reinforcement Learning? | 5 | 4 | 4 | 3 | 5 | 5 | 26/30 | Full Source Review complete；v1/v4 separated；Refine `TRAIN-GRPO` |
| Xiaomi-Robotics-1 | 5 | 5 | 4 | 3 | 5 | 5 | 27/30 | Full Source Review complete；Refine `MULTIMODAL-EMBODIED-VLA` |
| DSWorld | 5 | 5 | 4 | 3 | 5 | 5 | 27/30 | Full Source Review complete；Refine `AGENT-WORKFLOW`；speedup disputed |
| Beyond Success Rate: Cost-Aware Evaluation of Offensive and Defensive Security Agents | 4 | 5 | 5 | 4 | 5 | 5 | 28/30 | Full Source Review complete；No Change — Already Covered by Ch62；v3 only post-window verification |
| SeerGuard | 5 | 5 | 4 | 3 | 5 | 5 | 27/30 | Full Source Review complete；Refine `PLATFORM-SECURITY`；post-window artifacts separated |
| Environment-free Synthetic Data Generation for API-Calling Agents | 5 | 5 | 5 | 4 | 5 | 5 | 29/30 | Full Source Review complete；Refine `TRAIN-DATA`；post-window evidence separated |
| BadWAM | 5 | 4 | 4 | 3 | 5 | 4 | 25/30 | Full Source Review complete；Refine `PLATFORM-SECURITY` |
| From Pixels to States | 4 | 4 | 4 | 3 | 4 | 4 | 23/30 | Full Source Review complete；Refine `MULTIMODAL-WORLD-MODELS` |
| Demystifying On-Policy Distillation | 5 | 4 | 4 | 3 | 5 | 4 | 25/30 | Full Source Review complete；Refine `TRAIN-GRPO` |
| Byte-Exact KV-Cache Grafting | 4 | 4 | 3 | 2 | 5 | 4 | 22/30 | Full Source Review complete；Emerging / Disputed；Weekly only |
| Rethinking Harness Evolution Evaluation | 4 | 4 | 4 | 4 | 4 | 4 | 24/30 | Full Source Review complete；No Change — Ch62 already covers search/eval isolation |
| Distilled Reinforcement Learning for LLM Post-training | 5 | 5 | 4 | 3 | 5 | 5 | 27/30 | Full Source Review complete；Refine `TRAIN-GRPO` |
| JoyNexus | 5 | 5 | 4 | 3 | 5 | 4 | 26/30 | Full Source Review complete；Refine `PLATFORM-RESOURCE-SCHEDULING` |
| DataFlow-Harness | 5 | 4 | 5 | 3 | 5 | 5 | 27/30 | Full Source Review complete；Refine `AGENT-WORKFLOW` |
| Training Variable Long Sequences with Data-Centric Parallel | 5 | 5 | 4 | 3 | 5 | 4 | 26/30 | Full Source Review complete；Refine `TRAIN-DISTRIBUTED-TRAINING` |

### Deep Analysis 2 — Harness Handbook：Agent 修改前先恢复 Behavior Map

- Submitted / First Public Version: 2026-07-14 21:39:55 UTC
- Status: Experimental
- Primary Source: https://arxiv.org/abs/2607.13285

#### Why

Agent harness 的行为横跨 prompt construction、state、tools、runtime 与 error handling。
用户按 behavior 提需求，repository 却按 files/modules 组织；即使有 code search 或长上下文，
agent 仍必须恢复 behavior-to-code mapping。

#### Principle

代码库 context 不应只是更多 token，而应是可逐层展开、始终链接当前 source 的 semantic
index。抽象层负责导航，源代码负责最终 truth。

#### Mechanism

Harness Handbook 用 static analysis 与 LLM structuring 生成 behavior-centric representation；
Behavior-Guided Progressive Disclosure 从高层 behavior 导向候选实现，再对当前 source
验证位置。作者只在两个 open-source harnesses 上实验，结果不能视为普适。

#### Trade-off

Handbook 可降低定位成本，却引入生成、同步与 stale-index 风险；static analysis 对动态
registration、reflection 与 runtime configuration 的覆盖有限；若抽象页不带 provenance，
反而会制造可信但过时的“第二份真相”。

#### Connection

知识树位置：第 72～80 章 Agent/MCP/Context/Memory。它支持“progressive disclosure +
source-linked context”这一长期原则，但当前章节是否已有同义观点需在 Books batch review
中判断。

#### Evolution

从 keyword search、embedding index、whole-repo context，到 behavior map + verified
progressive disclosure，演化方向是把 context selection 变成可审计的 navigation process。

### Ring-Zero — Scaling Observation

Ring-Zero 报告把 zero-RL 扩展到 1T 参数，并加入 clipped importance sampling、
training-inference ratio correction 与 mixed-precision control。作者观察到 discovery →
sharpening 的阶段和多类 emergent reasoning behavior。由于训练数据、完整 compute、baseline
和复现条件尚不足以支持通用 scaling law，本周只保留 `Status: Experimental`，不把“规模自然
产生高质量 reasoning”写入 Books。

### Deep Analysis 3 — AgentCompass：Evaluation Object 必须拆成三层

- Submitted / First Public Version: 2026-07-15 11:11:17 UTC
- Status: Experimental
- Primary Source: https://arxiv.org/abs/2607.13705

#### Why

Agent benchmark 常把 model、harness 与 environment 绑成一套脚本，导致同一“模型分数”
实际上混入 tool adapters、timeouts、retry、sandbox 和 evaluator 差异。

#### Principle

可复现 agent evaluation 至少应把 evaluation object 分为：

```text
Benchmark: task and success contract
Harness: prompt, state, tool and execution policy
Environment: observable world and side effects
```

trajectory 是解释 failure 与 reward hacking 的必要证据，而不是附属日志。

#### Mechanism

AgentCompass 把三类组件独立配置，以 asynchronous fault-tolerant runtime 执行，并保留
trajectory analysis。论文报告支持 20+ benchmarks，但规模不是架构正确性的证明。

#### Trade-off

解耦提高复用和对比，也要求严格的 interface version、environment determinism 与 artifact
provenance；否则“可替换”只会扩大不可比组合空间。

#### Connection

知识树位置：第 62 章 Evaluation System → 第 71～80 章 Agent System。该三层拆分可能
refine 第 62 章，但应先确认现有章节是否已有 model/runtime/environment 条件化证据框架。

#### Evolution

从 final score，到 trajectory replay，再到 benchmark/harness/environment 独立版本化，
演化方向是让 agent evaluation 能区分 capability、orchestration 与 environment failure。

## 3. AI Infra 与工程项目

### Source Coverage

按 PyTorch → JAX → CUDA → Triton → vLLM → SGLang → NVIDIA Dynamo → TensorRT-LLM
→ Ray → KServe → Kubeflow → Kubernetes → Transformers → Accelerate → DeepSpeed
→ Megatron-LM → Unsloth → MLX → llama.cpp → ONNX Runtime → OpenXLA 的顺序扫描。

### Record Only

- Transformers v5.14.1，released 2026-07-16：修复 EncoderDecoderCache assisted generation、
  StaticCache + SDPA prefill、multi-device DeepGEMM 等 correctness 问题。它说明 cache
  contract 需要模型/attention path 测试，但属于 patch，不改变书稿机制。
- Ray 2.56.1，released 2026-07-17：修复 body-aware LLM router 在 direct streaming 下挂起、
  cgroup system-slice memory pressure 提示等问题。属于 implementation correctness，不新增
  runtime 原则。

## Evidence Level

| Claim | Evidence | Boundary |
| --- | --- | --- |
| K3 的架构与 runtime 声明 | Kimi 7 月 16 日官方 Blog | 官方事实；详细机制由 7 月 27 日报告补充 |
| PerceptionBench 构造方法 | Kimi 官方 benchmark page | 作者 benchmark |
| Harness Handbook / AgentCompass / Ring-Zero | arXiv v1 | `Status: Experimental` |
| SearchOS mechanism / experiments | arXiv v1 full text | 作者实验；特定 harness、`Max@3` 与预算，不外推 |
| 15 个 recovered expanded candidates + 4 spillbacks | arXiv HTML v1/v2 full text | Full Source Review complete；作者实验按各自 workload contract 保持 bounded |
| 4 个 blocked candidates | arXiv identity / metadata | `Unverified / Blocked Backlog`；正文连续不可访问，不形成机制结论 |
| Transformers / Ray fixes | GitHub official release | 版本事实，不外推 |

## Cross-Week Deduplication

- Length Penalties v2 更新于 7 月 17 日，但 v1 为 7 月 8 日，归 W28。
- AgentCompass v3 更新于 7 月 20 日，但首次公开为 7 月 15 日，主归 W29。
- Kimi K3 技术报告 7 月 27 日由现有 `papers/2026/07/29/README.md` 深入分析；本周只校正
  7 月 16 日 first public announcement。
- ABot-AgentOS、GRASP 及四项重复榜单论文均按 arXiv v1 回归 W28；W29 不重复评分。
- `Training Variable Long Sequences with Data-Centric Parallel`（2608.07524）虽使用 `2608` 编号，arXiv
  HTML 明确记录 v1 为 2026-07-14，归 W29；8 月 11 日列表只是重新索引。该异常日期与编号组合保留为
  provenance fact，不按编号月份重写 event date。

## Knowledge Tree Position

| Candidate | ROADMAP Node | Role |
| --- | --- | --- |
| Kimi K3 | Ch14–17, Ch21 → Ch30–36 → Ch43–52 | model/runtime co-design evidence |
| PerceptionBench | Ch8 → Ch62 | atomic multimodal evaluation |
| Harness Handbook | Ch72–80 | source-linked progressive context |
| AgentCompass | Ch62 → Ch71–80 | benchmark/harness/environment separation |
| Ring-Zero | Ch28–30 → Ch37 | large-scale RL training observation |
| SearchOS-V1 | Ch77；handoff Ch62、72、73、78、80 | typed shared state + continuous dispatch |
| Recursive Harness Self-Improvement | Ch77；handoff Ch62、76、78 | trajectory-local harness revision；prompt-level workflow contract evolution |
| When Does Muon Help Agentic Reinforcement Learning? | Ch29；handoff Ch35、31 | policy optimizer / credit estimator / update-scale / sharding joint recipe |
| Xiaomi-Robotics-1 | Ch23；handoff Ch24、25、10、62 | embodiment-free trajectory pretraining → embodiment/instruction alignment |
| DSWorld | Ch77；handoff Ch75、76、62、10 | exact execution → learned transition simulation → cost/fidelity routing + authoritative-state reconciliation |
| Cost-Aware Security Agents | Ch62；handoff Ch66、68 | workload-specific success/cost operating point + refusal/decontamination controls |
| SeerGuard | Ch68；handoff Ch74、77、62、10 | instruction screening → pre-execution semantic consequence prediction → deterministic authorization + actual-state reconciliation |
| Environment-free API data / ESAT | Ch23；handoff Ch74、77、62、10 | static tool examples → executable-environment trajectories → API-spec-conditioned stateful simulation → real-environment calibration |
| Recovered training / evaluation / agent set | Ch10、24、29、32、41、56、62、65、68、73、77、80 | 19 项完成全文审计；4 项 blocked backlog 单列 |

## Recommended Action

- K3 与 Xiaomi-Robotics-1 的既有 source-family integration 经技术报告、model/artifact 与相邻章节复核后保留；
  不复制厂商 benchmark 或 post-window artifact 为事件时事实。
- 本周新增正文只沉淀四条聚合机制：teacher/base policy delta 与 optimizer/sharding recipe identity；相邻 Harness
  revision 的 bounded local search；semantic consequence sensor 与 deterministic authority/actual-state
  reconciliation；variable-length batch 驱动的 admitted parallel plan。
- SearchOS、LightMem、AdvancedMathBench、KnowAct、cost-aware security、Harness evaluation 等已有明确章节
  覆盖，不重复写入。Claude values、Ring-Zero 保留 Weekly；Byte-exact KV grafting 保持 Disputed。
- 四个 blocked family 不获得机制 owner；Transformers/Ray patch 不进入 Books。

## Event-Date Daily Decision

| Date | Decision | Reason |
| --- | --- | --- |
| 2026-07-14 | Do not create | Harness Handbook 24/30，实验范围有限 |
| 2026-07-15 | Do not create | AgentCompass 23/30，单项工程论文 |
| 2026-07-16 | Retired after Weekly integration | K3、PerceptionBench 与时间边界已完整归并 W29 |
| 2026-07-17 | Do not create | 仅 patch release 与论文版本更新 |

## Books Integration Decision

`Source-Family Books Gate Passed under Blocked-skip — Archive Completion Gate Open`。38 个 family 均有最终
disposition；34 项全文审计，4 项明确 blocked。实际新增正文位于 `TRAIN-GRPO`、`TRAIN-DISTRIBUTED-TRAINING`、
`PLATFORM-SECURITY` 与 `AGENT-WORKFLOW`；K3、Xiaomi-Robotics-1 和其他 Refine family 的既有章节内容经复核
保留。没有把模型公告、patch release、作者 speedup、learned guard 或 byte-exact closed artifact 外推为通用事实。

## Ignored Noise

- 把 7 月 27 日 technical report date 当作 K3 首次发布日；
- 把厂商 benchmark 排名、token price 或内部案例当作跨模型证据；
- 以 Hugging Face upvotes 决定论文质量；
- Transformers/Ray patch 列表直接复制进书稿。

## 2026-07-31 Full Re-Audit Addendum

- Kimi K3 的 paper 首版日期修正为 2026-07-27，并与官方 blog/code 联合核验；router
  objective、static dispatch shape 与 host synchronization 的耦合写入 Ch21，不把作者
  benchmark 外推为 MoE 通用最优。
- Harness Handbook 与 AgentCompass 全文复核后判定现有 Ch77/62/80 已覆盖其稳定原则，
  不重复追加。其余候选继续 Weekly only。

## Full Source Review

### Kimi K3 first public announcement — 28/30

- **Source Family ID / Type / History**：`KIMI-K3`；first-public official blog 2026-07-16；
  arXiv:2607.24653/technical report 与 weights/model card released 2026-07-27 仅作为后续核验，
  不新增 W29 event。
- **Full-read Coverage**：已覆盖 47-page technical report 的 architecture、KDA/AttnRes、Stable
  LatentMoE、Quantile Balancing、Per-Head Muon、QAT、training/parallelism、post-training、evaluation、
  deployment/serving、limitations；联读官方 model card/weights、vLLM/SGLang recipes 与 FlashKDA path。
- **Problem / Previous Design / Changed Constraint**：dense/较低 sparsity MoE 的 dynamic routing 对灵活
  specialization 合理；2.8T/896 experts、16 activated 的规模使 imbalance、all-to-all shape、host sync、
  hybrid attention state 与 supernode fabric 成为一等约束。
- **Mechanism / Ownership / Flow**：KDA+Gated MLA 构成 hybrid sequence state，AttnRes 跨深度选择
  representation；Quantile Balancing 从 router-score quantiles 派生 allocation，fully balanced expert-
  parallel training保持 static shapes 并移除 critical-path host sync。router objective 只有能落成 executable
  dispatch shape 才有系统收益；runtime 还必须承载 KDA recurrent/prefill state、KV 和 MoE communication。
- **Evaluation Contract**：2.8T total/104B active、93 layers、69 KDA+24 Gated MLA、896 experts/16
  selected+2 shared、MXFP4 weights/MXFP8 activations、1M context；厂商 benchmark 混用 Kimi Code、
  Claude Code、Codex 等 harness，并披露 effort/temperature、fallback/refusal和部分 H20 calibration。
  这些数字不证明 architecture 组件各自因果贡献或跨 harness 公平排名。
- **What It Proves / Does Not Prove**：report/model card 证明公开 architecture、weights 与 serving contract；
  不证明 2.5x scaling efficiency 可普遍复现、90% cache hit 可迁移、supernode 之外成本相同，或 product
  case 等于 autonomous correctness。
- **Trade-offs / Evolution**：极稀疏 MoE 降 active compute，却增加 routing/communication/skew 和 static-
  shape coupling；KDA 扩展 context，但 prefix/recurrent state identity 更复杂；preserved thinking history
  提供跨 turn continuity，同时形成 harness compatibility 和 mid-session switching failure mode。旧 dense/
  standard attention 在兼容性、短 context、普通 topology 下继续成立。
- **ROADMAP / Chapters / Decision**：Ch21 主 owner，已读 Ch14、Ch20～24、Ch32～35、Ch45、Ch47～50；
  `Refine — Existing Argument` 已写入 router objective→dispatch coupling；保留 provisional 内容。

### PerceptionBench — 21/30

- **Source Family / Coverage**：`PERCEPTIONBENCH`；Kimi 2026-07-16 official report/dataset；已读由 42
  benchmarks failure attribution 构建 10 类 atomic perception、17k pool→3k release、verification、
  model evaluation 与 limitations。
- **Evidence / Limits**：decomposition 可减少 reasoning/knowledge confound，但“earliest erroneous step”仍有
  annotation ambiguity，failure-driven sample 不代表自然 deployment distribution。Ch62 已读；
  `No Change — Already Covered`。

### Claude values across models/languages — 21/30

- **Source Family / Coverage**：`CLAUDE-VALUES-CROSS-MODEL-LANGUAGE`；Anthropic 2026-07-13 report、
  taxonomy/method、cross-model/language samples、uncertainty 与 limitations 已核对。
- **Evidence / Decision**：observed language behavior 可描述 disposition 分布，不证明 stable internal
  values、causal mechanism 或 deployment safety。Ch5/27/62/68 已读；`No Change — Already Covered`。

### Harness Handbook — 24/30

- **Source Family / Full-read Coverage**：`HARNESS-HANDBOOK`；arXiv:2607.13285v1，first-public
  2026-07-14；已读 behavior extraction/map、handbook generation/navigation/editing、implementation、
  user/agent evaluation、ablation、limitations 和 appendix/artifact。
- **Problem / Mechanism**：evolving harness 的 behavior 分散在 registration/config/control flow 中；先从
  code 恢复行为地图/契约，再让 Agent 导航和修改，降低局部 patch 破坏隐式 behavior 的风险。
- **Evidence / Trade-offs**：作者 tasks 支持其 handbook 对代码修改的帮助；不证明 dynamic registration、
  runtime config、external service 和 stale documentation 完全恢复。文档提高可读性，也新增生成漂移、
  false completeness 和维护成本。
- **ROADMAP / Decision**：Ch77 主 owner、Ch80 handoff，已读 Ch76～80；现有 behavior map、state owner、
  invariant/readback 已覆盖。`No Change — Already Covered`。

### Ring-Zero — 22/30

- **Source Family / Full-read Coverage**：`RING-ZERO-RL`；arXiv:2607.12395v1，first-public
  2026-07-14；已读 trillion-parameter Zero-RL setup、distributed training、reward/verification、scaling、
  baselines/ablation、failure cases 与 limitations。
- **Evidence / Decision**：作者结果证明特定 model/reward/compute recipe 的 emergent reasoning trajectory，
  不证明参数规模单因果、通用 reasoning 或无 reward hacking。Ch27～30、Ch32～35 已读；
  `Emerging / Experimental`。

### AgentCompass — 23/30

- **Source Family / Full-read Coverage**：`AGENTCOMPASS`；arXiv:2607.13705v1，first-public
  2026-07-15；已读统一 infra、task/environment/harness separation、execution/grading、reproducibility、
  experiments/limitations。
- **Mechanism / Evidence Boundary**：将 model capability、harness behavior 与 environment opportunity
  分层版本化，能减少 benchmark glue 的隐性差异；作者 infra 不能消除 external service drift、seed/
  timeout bias 或 benchmark validity。
- **ROADMAP / Decision**：Ch62 主 owner，已读 Ch61～63、Ch77、Ch80；现有 evaluation object 分层已覆盖。
  `No Change — Already Covered`。

### SearchOS-V1 — 28/30

- **Source Family ID / Type / History**：`SEARCHOS-V1`；arXiv:2607.15257v1，first-public
  2026-07-16；论文链接作者 repository，但本轮 repository 页面无法稳定读取，因此代码实现细节只采用
  论文明确披露的 contract，不以 README 或搜索摘要补齐。
- **Full-read Coverage**：已读 metadata、Introduction/Related Work、schema-completion formulation、
  Shared Open Context Memory（SOCM）、continuous dispatch、四层 skill library、context/evidence/sensor
  middleware、implementation、WideSearch/GISA setup、baselines、schema/scheduling/skill ablations、
  efficiency、appendix 与 conclusion。论文未提供独立 `Limitations` 章节，此缺口保留为证据边界。
- **Original Problem / Why Previous Design Was Reasonable**：单 Agent + conversation history 在短任务中
  owner 清楚、replay 简单；静态 schema 与同步 batch 也使实验可复现。但开放域 table completion 进入长
  horizon 后，进度、证据、冲突与失败被困在各 Agent 的 Context，新增 worker 会重复搜索、产生不一致，
  同步轮次还受 straggler 限制。
- **Changed Constraint / Mechanism**：SearchOS 把任务改写为带引用的 relational schema completion，并把
  authoritative collaboration state 外置为 SOCM：`Frontier Task` 保存依赖、优先级、owner 与 attempt；
  `Evidence Graph` 保存 value、URL、supporting span、schema binding、confidence、provenance tier 与
  Support/Conflict/Refine edge；`Coverage Map` 区分 cell saturation 与 row-set completion；`Failure Memory`
  保存 failure signature、correction 与 recurrence。所有更新使用 locked read-modify-write，role-specific
  Context projection 总是由最新共享状态生成。
- **State Ownership / Control and Data Flow**：Workflow runtime 拥有 frontier、coverage、evidence 与 failure
  state；orchestrator/explorer/searcher/writer 只消费 projection 并提交 typed mutation。continuous dispatch
  在 slot 释放后立即补充 ready task；evidence-extraction middleware 要求 schema binding 与 span anchoring，
  原子更新 evidence + coverage；sensor 结合滑动窗口 coverage/evidence delta 与 iteration/search/time
  budget pressure，选择 continue、correct、backfill、drain 或 stop。分层 skill library 把可执行 access
  skill 提升为 typed tool，但不改变 Workflow 对事实状态的所有权。
- **Implementation / Evaluation Contract**：论文在 WideSearch（200 个经人工整理问题，英语/中文各
  100，覆盖 15+ domains）与 GISA（373 个结构化 query）比较 ReAct、Plan-and-Solve、
  A-MapReduce、Web2BigTable 和 Table-as-Search；主 backbone 为 GLM-5，evidence extractor 为
  Qwen3.5-35B-A3B。报告使用 `Max@3`，预算为 50 orchestrator iterations、8 parallel agents、每个
  subagent 20 searches、1,800 秒。作者报告 WideSearch item F1 80.3 / row F1 56.5，GISA set F1
  76.5；这些是 best-of-three、特定 harness 与模型组合的作者结果，不是通用 Agent scaling law。
- **Ablations / What Evidence Proves**：40-case schema ablation 支持运行时 schema refinement 优于论文中的
  fixed/oracle-fixed construction；10-case、K=8、三轮 scheduling 对照报告 wall time 629.13→476.34、
  utilization 34.6→41.7；整体 skill ablation 报告 outcome 与 cost 同时变化。它们证明在该实现和任务上，
  typed shared state、动态 dispatch 与技能组合有条件收益。
- **What It Does Not Prove / Threats**：`Max@3` 偏向最好一次运行；只有两个 benchmark；schema ablation
  还混入生成 schema 所用模型差异；全部 skill layer 同时关闭，不能分离单层因果贡献；open-set recall
  无法穷尽。span anchoring 不是 truth，中央状态、锁与 projection 会形成 bottleneck、staleness 和故障域；
  论文没有评测 crash recovery、multi-tenancy、authorization、malicious source、conflict arbitration 或
  多 writer consistency。continuous dispatch 与 GPU pipeline 只是 `Principle Reuse`，不是相同执行语义。
- **Trade-offs / Where Previous Design Still Applies / Evolution**：共享 typed state 降低 Context duplication
  和重复搜索，却新增 schema identity、atomic mutation、conflict resolution、backpressure、snapshot 与
  recovery 成本。短任务、单 writer、强顺序约束或 evidence 较少时，单 Agent/静态 schema/同步批次仍更
  简单可靠。演进关系为 `Direct Evolution`：conversation-local progress → externalized typed state →
  continuous state-aware dispatch；下一阶段压力是分布式 ownership、freshness、permission、replay 与
  fault-tolerant recovery。
- **ROADMAP / Adjacent Chapters / Decision**：Ch77 为主 owner，已读 Ch72、Ch73、Ch76～78、Ch80，并
  联读 Ch62。现有正文已明确 deterministic spine、authoritative workflow state、typed evidence、动态
  dispatch、Multi-Agent message/state 分离、failure/recovery 与 evaluation contract；SearchOS 提供新的
  条件性案例但不改变设计结论。最终 disposition 为 `No Change — Already Covered`。

### On-Policy Delta Distillation（OPD²）— 28/30

- **Source Family / History / Full-read Coverage**：`OPD2-TEACHER-DELTA`；arXiv:2607.15161v1，
  first-public 2026-07-16。已读 Abstract、Introduction/Related Work、完整 formulation、signal analyses、
  Qwen3/Gemma4 experiments、training dynamics、ablations、compute、appendix hyperparameters；并核对 8 月 5 日
  发布的 official code、trainer formulas、pinned runtime、recipes 与 evaluation adapters。后发 code 只用于
  核验 artifact，不改变 W29 event date。论文没有独立 Limitations section，未披露项保持显式。
- **Original Problem / Why Previous Designs Were Reasonable**：teacher-sequence SFT 便宜稳定但有 exposure
  bias；普通 OPD 用 student rollout 上 `log π_teacher - log π_student` 的 dense token signal，直接逼近强
  teacher，在没有可靠 scalar reward 时合理。然而 reasoning-tuned teacher 同时保留 base model 的语言/style
  preference，绝对 teacher imitation 不区分“post-training 新学到的 reasoning change”与原有 prior。
- **Changed Constraint / Mechanism**：OPD² 引入同 lineage 的 teacher-base checkpoint，定义
  `R_t^Δ = log π_teacher(y_t|s_t) - log π_teacher-base(y_t|s_t)`。先按 student top-k（论文取 1024）
  expectation centering 得到 `A_t^Δ`，再仅在 `A_t^Δ A_t^OPD > 0` 时保留更新；delta 决定幅度，原 OPD
  方向承担 convergence/safety gate。它不是把 teacher 目标替换成无约束 one-hot maximization。
- **State Ownership / Control and Data Flow**：student policy 拥有 on-policy rollout 与被更新 weights；
  reasoning-tuned teacher 拥有当前能力分布；teacher-base 拥有 lineage reference；trainer 同时 forward 三者，
  计算 top-k centered delta 与 direction gate，再把 dense per-token advantage 交给 PPO-clipped GRPO loss。
  因此 `teacher revision + teacher-base revision + tokenizer/template + student rollout version` 共同构成
  objective identity；任一 lineage 不匹配都会把 delta 变成模型差异而非 post-training change。
- **Implementation / Evaluation Contract**：100k questions 按 Math/Science/Code 1:1:1 混合，实际少于
  30k samples、每题最多一次；single completion、100 steps、max generation 8192、temperature 0.7、
  AdamW LR `5e-6`、KL coefficient 0。Qwen3-1.7B 为 1 node/8×H100；Qwen3-4B/8B 与 Gemma4-E4B
  为 4 nodes/32×H100（1 rollout + 3 training）。14 benchmarks 报 repeated pass@1 average，不作
  best-of-k。official repo 把 Qwen3/Gemma4 分别固定到不同 torch/vLLM/TRL images，并公开 recipes/adapters。
- **What Evidence Proves / Does Not Prove**：在上述 Qwen3/Gemma4、同-family teacher-base、短训练与
  benchmark contract 中，OPD² 多数平均分优于 OPD/ExOPD；delta-removal ablation 是最大退化项，支持
  delta signal 的条件性贡献。它不证明 token delta 等同“reasoning knowledge”的因果分解，不证明跨
  unrelated teacher/base、长期训练、开放任务或生产 quality；Gemma4 code average 仍低于未蒸馏 base，
  说明“最佳 distillation variant”不等于“总能力必然提升”。
- **Trade-offs / Failure Modes / Coexistence**：获得更聚焦的 post-training change signal与较好的
  capability preservation，代价是额外 teacher-base forward/state；作者测得 Qwen3 wall time 相对 OPD
  增加 24～28%、Gemma4 增加 8%，仅适用于披露的 H100 topology/100-step recipe。base/teacher
  lineage drift、top-k expectation bias、sign-gate 丢弃有效反向信号、长训退化与三模型 serving pressure
  是新 failure modes。普通 OPD 在没有 matched base 或 absolute teacher behavior 就是目标时更简单；
  verifiable RL 在需要 environment exploration/outcome optimization 时仍成立。关系为 `Direct Evolution`。
- **ROADMAP / Adjacent Chapters / Decision**：Ch29 为主 owner，已读 Ch27～30 与 Ch23 data lineage。
  现有 Ch29 只把 distillation 写成 teacher traces→SFT 分支，尚未拥有 student-on-policy token distillation
  或 teacher/base lineage-delta objective。最终 disposition 为 `Refine — New Mechanism / Experimental`；
  已写入 `TRAIN-GRPO`。

### Recursive Harness Self-Improvement（RHI）— 27/30

- **Source Family / History / Full-read Coverage**：`RECURSIVE-HARNESS-SELF-IMPROVEMENT`；
  arXiv:2607.15524v1，first-public 2026-07-17，无后续 revision。已读 Abstract、Introduction、
  problem formulation、完整 objective/algorithm/harness representation、benchmark/evaluator、三组实验、
  train-time scaling 与 component ablations、information-theoretic hypothesis、Related Work、Conclusion、
  Q&A、harness/optimizer/task/evaluator appendices 与 resource distribution。arXiv 没有列出 official code/data
  artifact，因此 implementation 只能核验到论文披露的 prompt-level protocol，不能声称存在可复现 runtime。
- **Original Problem / Why Previous Designs Were Reasonable**：population-based harness search 用多候选、
  Pareto frontier、execution trace 与 evaluator 近似全局偏好，在可支付大量 black-box runs 时能保留探索
  diversity；提高 test-time reasoning effort 则无需改 workflow，适合单次任务。对大量 task-specific
  user harness，这两条路线都会把每个新增候选或 reasoning tier 变成新的 agent run、judge 和 context 成本。
- **Changed Constraint / Mechanism**：RHI 把 harness 表示为 roles、instructions、communication contracts
  与 workflow hops 的文本规范，以前一版本为唯一局部 comparator。第 `i` 轮执行新 harness 后，judge 只比较
  `output[i]` 与缓存的 `output[i-1]`，把 pairwise preference 追加到 self-history；optimizer 读取当前
  harness 与累积 history，生成下一 revision。每轮从 population search 的多 trace/多 pair 降到一个新 trace
  加一次 pairwise judge，但这不是原 population objective 的无偏估计，而是主动改成 noisy local ascent。
- **State Ownership / Control and Data Flow**：coding agent 拥有一次 task execution；harness revision 是
  versioned prompt artifact；evaluator 拥有相邻 outputs 的 preference；self-history 保存跨 revision 的压缩
  feedback；harness optimizer 提议下一版；outer loop 用跨任务 improvement rate 决定停止。论文没有 durable
  store、并发 writer、approval、rollback 或 deployment owner，因此生产实现仍须由 Ch77 Workflow 提交版本，
  不能让 optimizer 的自然语言直接覆盖 authoritative definition。
- **Implementation / Evaluation Contract**：30 个由 job postings 合成的开放 ML research tasks，quantitative
  finance、robotics、pharmacy 各 10；输出是完整 repository，但 judge 只读取 task-specified deliverables，
  长文件按同一协议截断并控制在 evaluator context 的约 30～40%。base agent 为 Sonnet 4.6、Opus 4.7、
  Opus 4.8 的 high reasoning；与同 family xhigh/max/ultracode 比较；两个 judge families、每项三 seeds，
  同时记录 pairwise outcome、agent internal normalized cost、output tokens 与 cache read/write。没有公开
  GPU、provider scheduling、wall-clock tail SLO 或独立 human/executable ground truth。
- **What Evidence Proves / Does Not Prove**：在该 synthetic repository benchmark 与 LLM-judge contract 中，
  一至数轮 RHI 能提高相对 win count；两种模型的 output-token usage 大致持平而 performance 改善，第三种
  evidence inconclusive。contract/hop embedding 的 task clustering、mutual-information proxy 上升与
  conditional total-correlation proxy 下降，与“task-specific information flow、较少 redundant context”一致，
  但作者明确将其定性为 correlational hypothesis，不是 optimizer latent objective 的因果证明。结果不证明
  对真实仓库、不同 agent runtime、独立人类评审、安全任务或长期在线演化成立，也不证明较弱 base model
  能取代 train-time scaling；相关 ablation 显示它未稳定追平更强 model family。
- **Trade-offs / Failure Modes / Coexistence**：收益是低每轮搜索成本、task-specific contract 与可能更小的
  context/cache footprint；代价是 local comparator 覆盖窄、judge/order/truncation bias、single-sample noise、
  history compression 丢失反例、局部最优、revision drift 与 eval-set overfitting。论文用 cosine stabilization
  说明文本变化趋缓，不等于功能 regression 已排除。population/Pareto search 在需要 diversity 与 global
  comparison 时仍成立；deterministic Self-Harness/regression tests 在有可执行 oracle 时更可靠；单 Agent
  或固定 Workflow 在任务不易分解、coordination tax 较高时仍是默认分支。关系为 `Direct Evolution`。
- **ROADMAP / Adjacent Chapters / Decision**：Ch77 为主 owner，已读 Ch76～78，并核对 Ch62 的
  feedback-conditioned/evolving-state evaluation。Ch77 已拥有 evaluator-driven population search、lineage、
  held-out verification 与 durable state，却没有“相邻 revision + 压缩 self-history”的低成本 local-search
  分支；Multi-Agent 只需短 handoff。最终 disposition 为 `Refine — New Mechanism / Experimental`；
  已写入 `AGENT-WORKFLOW`。

### When Does Muon Help Agentic Reinforcement Learning? — 26/30

- **Source Family / History / Full-read Coverage**：`MUON-AGENTIC-RL`；arXiv:2607.16169v1
  first-public 2026-07-17，v2/v3/v4 分别为 7 月 20 日、7 月 30 日与 8 月 2 日。W29 event 以 v1 为准；
  v4 与 official repository 只作 post-window verification，不能倒写为 7 月 17 日已经具备的证据。
  已完整阅读 v1 的 metadata、Abstract、Introduction、optimizer / group-RL background、Muon update、
  GRPO/GiGPO/GraphGPO setup、learning-rate controls、training dynamics、step-credit ablation、Discussion、
  Limitations、Conclusion 与全部 appendices；另读 v4 的多 seed、0.5B～3B scale、WebShop transfer、
  update-spectrum/RMS matching、optimizer-latency diagnostics 与 official `verl-muon` 实现、配置和 FSDP 路径。
- **Original Problem / Why Previous Design Was Reasonable**：AdamW 对每个参数做 element-wise adaptive
  scaling，生态成熟且天然适配 sharded optimizer state；在 RL post-training 中，它与已有 learning-rate、KL、
  clipping、weight decay 和 checkpoint lineage 共同构成可控 baseline。Muon 对 hidden 2D matrices 的 momentum
  update 施加 Newton–Schulz orthogonalization，可能改变弱 singular directions 与有效 step scale；但 nominal
  learning rate 已不再与 AdamW 同义，所以“只替换 optimizer、沿用数字超参”不是公平或稳定的系统迁移。
- **Changed Constraint / Mechanism**：v1 在 Qwen2.5-0.5B / ALFWorld 上，把 Muon 分配给 attention/MLP hidden
  matrices，embedding、norm、tied head 和非矩阵参数仍交给 AdamW；GRPO、GiGPO、GraphGPO 共享其余 loss recipe，
  只比较 optimizer / estimator 组合。reference Muon 要看到完整 2D matrix，因此实现把 policy 设为 FSDP
  `NO_SHARD`。v4 才补上多 seed、scale/transfer 与 RMS-matched control：它把主要收益收窄为 shared
  KL/clipping recipe 下，fan-in Muon 能承受更激进的有效 hidden-matrix update；这不是 Muon 对所有 RL objective
  或 model scale 的普遍优越性证明。
- **State Ownership / Control and Data Flow**：advantage estimator 从 trajectory / anchor-state / state-graph
  产生 token/step credit；policy backward 形成 matrix gradient；parameter router 按 shape/module 决定 Muon 或
  AdamW；Muon 保存 momentum、执行五步 Newton–Schulz 并更新完整 hidden matrix；AdamW 维护 fallback parameter
  states；KL/clipping 约束 policy movement；FSDP layout 决定 optimizer 是否能取得完整矩阵。因而 recipe identity
  必须同时版本化 objective、optimizer transform、parameter assignment、scale convention、regularization、
  sharding/layout 与 model lineage，不能只记录 optimizer 名和 learning rate。
- **Implementation / Evaluation Contract**：v1 是单 seed、Qwen2.5-0.5B-Instruct、ALFWorld、200 updates，
  8×NVIDIA H20；group/train/validation batch 为 8/16/128，max prompt/response 2048/512，max environment
  steps 50，history 2，rollout/validation temperature 1.0/0.4。Muon 使用 momentum 0.95、Nesterov、5 次
  Newton–Schulz，weight decay 0.01；low-var KL coefficient 0.01。v4 扩展到五 seeds 为主、1.5B/3B 与
  WebShop，并报告一组 0.5B 五步诊断：Muon optimizer step 较慢，但该 workload 的 rollout/evaluation
  主导端到端时间；该结果不能外推到更短 rollout、更大模型或 distributed Muon。
- **What Evidence Proves / Does Not Prove**：v1 只证明在其单条 exploratory trajectories 中，Muon 的
  useful rate 与 advantage estimator / saturation headroom 有关；其 credit-quality appendix 明确是固定
  singular basis 的解释性 conjecture，并未测 update spectrum、gradient SNR 或 population uncertainty。
  v4 的多 seed 与 magnitude controls 加强了“有效更新幅度和 scale convention 是主要解释变量”的证据：
  high-rate Muon 的 hidden update RMS 大于 AdamW，RMS-matched full-budget control 消除了 late-success gain，
  tuned AdamW 在 3B GraphGPO 上接近其 AUC。它仍不证明 spectral flattening 本身因果地产生收益，也不证明
  对其他 checkpoint families、环境、长训练 horizon、regularization 或 fully sharded runtime 成立。
- **Trade-offs / Failure Modes / Coexistence**：收益是 matrix-aware transform 在特定 recipe 下扩大稳定
  update headroom，并可能提前学习；代价是 parameter routing 和两套 optimizer state、更高 optimizer latency、
  learning-rate 语义不一致、KL/clip 联合调参，以及完整矩阵可见性与 FSDP memory/scalability 冲突。新 failure
  modes 包括 nominal-rate 误配、fallback 参数与 hidden matrices 更新尺度漂移、NO_SHARD OOM、谱形解释被
  update magnitude 混淆和 saturation 下虚假“最终质量提升”。AdamW 在 sharded scale、成熟 checkpoint
  portability、较小 headroom 或调优后仍是合理分支；distributed Muon 必须证明数学 update 与 fault/restart
  semantics 后才可替换 reference implementation。关系为 `Layering / Dependency`，不是线性替代。
- **ROADMAP / Adjacent Chapters / Decision**：Ch29 为主 owner，已读 Ch28～30；另核对 Ch35 的 FSDP
  lifecycle/sharding owner 与 Ch31 的 optimizer checkpoint identity。Ch29 已有 advantage estimator、KL、
  rollout 与 policy-version contract，但尚未把 optimizer transform、parameter routing、effective update scale
  和 sharding layout 纳入同一 RL recipe identity。最终 disposition 为 `Refine — New Mechanism /
  Experimental`；已写入 `TRAIN-GRPO`，checkpoint/sharding 只作 handoff。

### Xiaomi-Robotics-1 — 27/30

- **Source Family / History / Full-read Coverage**：`XIAOMI-ROBOTICS-1`；arXiv:2607.15330v1
  first-public 2026-07-16，v2 2026-07-22。W29 event 以 v1 technical report 与 7 月 16 日 official project
  page 为准；2026-08-03 才公开的 code/checkpoints 只作 post-window artifact verification。已读 v1 的
  Abstract、Introduction、完整 model/data/training 方法、全部 scaling、real-robot adaptation 与四项 simulation
  evaluation、Related Work、Conclusion；论文无独立 Limitations/Appendix，未披露项保持显式。另读 official
  project page、repository 的 model/runtime summary、post-training/deployment surface 与 benchmark guides。
- **Original Problem / Why Previous Design Was Reasonable**：直接用 robot teleoperation 收集 task-specific
  trajectories，action 与真实 embodiment 一致、监督语义清楚，适合小规模专用 policy；但硬件占用、操作者成本、
  环境覆盖和人工 segmentation/language labeling 很快成为 data-diversity ceiling。只扩 model parameters 在有限
  robot distribution 上也会更快碰到 data bottleneck，所以“先扩大真实 robot data”并不是可以无限延伸的路线。
- **Changed Constraint / Mechanism**：该方案把 capability production 拆成两段。pretraining 使用便携 UMI
  gripper 收集的 embodiment-free real-world trajectories，切成 fixed-length clips，再由 VLM 生成 gripper/object
  state-transition descriptions；VLM backbone + DiT policy 以 observation、language、proprioception 和 VLM KV
  cache 条件化 flow-matching action chunks，另用 Choice Policies 给 VLM action auxiliary supervision。post-training
  再用 in-house robots、instruction-labeled UMI 与 open robot datasets，把状态转移描述转成 imperative instruction，
  并用统一 end-effector frame、relative delta pose、unified action vector 和 missing-dimension loss mask 对齐不同
  embodiments。它是 `embodiment-free breadth → embodiment/instruction alignment`，不是用更多 UMI data 直接替代
  real-robot data。
- **State Ownership / Control and Data Flow**：raw UMI/robot trajectories 保留 sensor/action/provenance；
  segmenter 定义 clip boundary；labeling VLM 产生 derived state-transition text；dataset builder 管理 source mixture、
  action schema/mask 与 lineage；pretraining checkpoint 拥有通用 action prior；post-training dataset/recipe 拥有
  embodiment 与 instruction mapping；evaluation harness 拥有 robot、scene、object、task、trial 和 success/progress
  contract。VLM action query 只作 auxiliary supervision，DiT attention 刻意排除这些 action-related tokens，避免
  copying shortcut；这也是 representation boundary，而非普通 implementation detail。
- **Implementation / Evaluation Contract**：论文称原始 pretraining pool 超过 100K hours，但主要 scaling
  experiments 使用约 20K hours 的 12.5/25/50/100% slices；2B/5B/10B variants 同分布比较。post-training 数据
  约 10K hours，其中 7.2K+ in-house robot、1K+ instruction-labeled UMI，另含 open datasets；sampling ratio
  为 vision-language/open robot/instruction UMI/in-house robot = 0.5/0.5/0.5/8.5。real-robot OOD evaluation 只有
  4 个 seen tasks、unseen environments/objects；downstream 4 tasks 每模型每任务 10 trials。simulation 使用
  RoboCasa、RoboCasa365、VLABench、RoboDojo 的各自 protocol；VLABench 另加入 50% CoT NTP loss。训练硬件、
  wall-clock、energy、control frequency/tail latency、seed uncertainty 与 incident/safety contract 未披露。
- **What Evidence Proves / Does Not Prove**：作者控制下的 slices 显示 data/model scale 与 action-validation error、
  post-training real-robot success 同方向，且小规模 task adaptation 和四个 simulation benchmarks 有竞争力；
  这支持“先扩大可收集的 interaction diversity，再用较昂贵 embodiment data 对齐”的可行路径。它不建立跨
  robot families 的普适 scaling law，也不证明 100K-hour quantity、auto labels 或 model size 各自的因果贡献；
  real-robot trials 少且无多 seed/置信区间，simulation/real-world contracts 不同。作者 benchmark 不能外推为
  开放部署可靠性，project page 的“no saturation”也只对已测范围成立。
- **Trade-offs / Failure Modes / Coexistence**：UMI 提高环境/任务覆盖并降低 robot occupancy，却引入
  gripper-to-robot embodiment gap、固定切片边界、VLM label hallucination、state-transition text 丢失不可见物理
  状态、action-coordinate/mask ambiguity 与 mixture imbalance。post-training 解决 action/instruction interface，
  又把能力绑定到 embodiment coverage，并可能覆盖 pretraining breadth。旧的 task-specific teleoperation 在
  safety-critical precision、罕见 embodiment 或无法可靠 retarget 的任务仍合理；simulation/video/WAM 数据在
  需要 counterfactual dynamics 或更低采集成本时是并存分支。下一阶段压力是 provenance-aware label audit、
  hardware/control-loop contract、failure recovery 与跨 embodiment held-out evaluation。关系为 `Direct Evolution`。
- **ROADMAP / Adjacent Chapters / Decision**：Ch23 为主 owner，已读 Ch23～25，并核对 Ch10 的世界模型/
  具身方向与 Ch62 的 environment/outcome evaluation。Ch23 已有 synthetic trajectory、lineage、filtering、packing，
  但尚未明确 embodiment-free interaction data 如何经 derived state-transition label、action schema 与 alignment
  stage 变成可部署 policy；Ch24/25 分别拥有 pretraining 与 instruction alignment，只需短 handoff。provisional
  disposition 为 `Refine — Existing Argument / Experimental`；既有 Source-Family integration 经复核保留。

### DSWorld — 27/30

- **Source Family / History / Access / Full-read Coverage**：`DSWORLD`；arXiv:2607.15901 只有
  v1，first-public 2026-07-17。已完整阅读 metadata、Abstract、Introduction、Related Work、state/action
  formalization、四组件架构、SFT 与 Reflective World Model Optimization、real/synthetic transition
  construction、全部 experiments、ablation/scale analysis、Limitations、Conclusion 与 Appendices A～D；并核对
  Ch75～77、Ch10 与 Ch62。论文所列 anonymous 4open.science artifact 在 2026-08-12 返回 Internal Error，
  因而实现只采用论文公开信息，artifact/code path 明确为 `Unverified / Artifact Unavailable`。
- **Original Problem / Why Previous Design Was Reasonable**：data-science Agent 通过执行 feature engineering、
  model training 与 evaluation 获得 ground-truth observation。每步真实执行虽然慢，却让 environment 而非模型
  拥有 transition truth，也使 failure、output 与 metric 能被复核；在动作成本尚低、候选数量少或结果会进入真实
  workflow 时，这是合理的默认设计。随着 RL rollout 与 test-time search 同时扩大候选数，重型 training/evaluation
  占据大部分循环时间，逐候选真实执行成为探索吞吐瓶颈；直接换成通用 LLM 又会产生 hallucinated transitions。
- **Changed Constraint / Mechanism**：DSWorld 把 workflow state 定义为
  `S_t={task, data, execution environment, logs/intermediate progress}`，由 rule-based State Constructor 规范化；
  action encoder 与两层 MLP Router 判断 `execute` 或 `simulate`，轻量操作进入真实 Compiler，昂贵操作进入
  Qwen3-8B transition Simulator。Simulator 先在约 8K 条真实/合成 transition 上 SFT，再比较 predicted/ground-truth
  next state 生成 reflection，以 GRPO 联合优化原始与 refined predictions。synthetic pipeline 从 MMTU tables、
  NumPy/Pandas operation/error/status ontology 生成 action，再由真实 Compiler 执行并经约束 verifier 过滤；所以
  learned simulation 的训练 truth 最终仍来自 execution，而不是 self-consistency。
- **State Ownership / Control and Data Flow**：authoritative state 由真实 environment、Compiler output 与
  versioned logs 拥有；State Constructor 只创建派生 view；Router 拥有 fidelity/cost decision；Simulator 输出的是
  predicted branch，不是已提交环境事实；agent policy 只能基于带 provenance 的 real/predicted observation 继续搜索。
  论文规定 Compiler 超时后改走 Simulator，但没有定义原进程是否仍运行、是否已产生部分副作用以及如何 reconcile。
  因此生产系统必须补充 cancellation、idempotency key、lease、late-result rejection 与 real-state refresh；timeout
  不能把一次 outcome unknown 静默转换成 simulated success。
- **Implementation / Evaluation Contract**：Simulator 为 Qwen3-8B，action encoder 为 Harrier OSS v1 0.6B，
  Router hidden dimensions 为 256/64 并用 code-execution-time pairs 训练；data synthesis 用 DeepSeek 3.2，真实
  transition 来自 DACode + ReAct。SFT 为 5 epochs、batch 32、learning rate `1e-5`；RL rollout size 8、200 steps、
  learning rate `1e-6`、max response 16K，在 4×NVIDIA A800 / VeRL 上执行；所有结果报告三次独立运行的
  mean/variance。transition evaluation 包含来自 DABench/MLE-Dojo 的 540 个合成任务和从 18,438 ranking tasks
  抽取的 471 个 Predict-before-Execute tasks；downstream training 用 105 个 MLE-Dojo tasks、10 RL steps，
  evaluation 为删去一个超 100GB task 后的 21-task MLE-Bench Lite，另有 100-task DACode experiment。
- **What Evidence Proves / Does Not Prove**：Table 1 支持 domain transition data + SFT 是主要增益来源，
  reflective GRPO 只带来较小增量；execution-status/error/output prediction 比 performance prediction 更可靠。
  Table 3 在三个 search agents、两类 backbones 的作者设置下支持约 3～6× inference-time reduction 与大体保留
  downstream score，但不证明 production tail latency、cost/SLO 或跨领域 fidelity。最重要的证据冲突是：Abstract、
  Figure 3 文字与 §5.3 声称相对 Compiler 约 14× RL-training acceleration，Table 2 却报告 Compiler 335 min、
  DSWorld 277 min（约 1.21×）；3854/277≈13.9 对应的是 DeepSeek-3.2 simulator，而不是 Compiler。图中底层原始值、
  计时口径和可运行 artifact 均不可核验，因此 `14× versus real execution` 标记 `Disputed`，不得引用为事实。
- **Trade-offs / Failure Modes / Coexistence**：learned transition model 把昂贵 execution 换成低成本预测，新增
  router false-execute/false-simulate、simulation drift、multi-step error compounding、synthetic ontology bias、
  verifier blind spot、predicted/real state identity 混淆和 timeout ambiguous outcome。作者也明确承认未覆盖 external
  tool-call transitions、复杂 workflow 仍会误预测、synthetic-to-real 有 distribution gap。real execution 在高风险
  side effect、final verification、distribution shift、低置信度与校准采样中仍成立；generic simulator 可作低成本
  baseline，但论文结果显示 accuracy 不足。下一阶段需要 uncertainty/abstention、周期性 real grounding、shadow
  validation、fidelity budget、state reconciliation 与 rollback。关系为 `Direct Evolution`，不是 simulator 替代 truth。
- **ROADMAP / Adjacent Chapters / Decision**：Ch77 为主 owner。Ch77 已拥有 deterministic spine、durable
  workflow state、retry/idempotency 与 evaluator-driven search，但尚未明确“真实执行与 learned simulation 是不同
  fidelity 的 transition provider，且 predicted state 不能夺取 authoritative ownership”。Ch75 只承接 search/planning，
  Ch76 只承接 ground-truth-conditioned reflection，Ch62 只承接 simulator calibration 与 downstream outcome contract，
  World Model 保留长期位置。最终 disposition 为 `Refine — Existing Argument / Experimental`；
  performance headline 同时为 `Disputed`，既有 Workflow fidelity contract 经复核保留。

### Beyond Success Rate: Cost-Aware Evaluation of Offensive and Defensive Security Agents — 28/30

- **Source Family / History / Full-read Coverage**：`COST-AWARE-SECURITY-AGENTS`；arXiv:2607.15263v1
  first-public 2026-07-16，v2 7 月 17 日，v3 7 月 27 日。W29 以 v1 为事件证据；v3 扩展模型与 provider
  operating conditions，只作 post-window revision verification。已完整阅读 v1 metadata、Introduction、Related
  Work、Cybench/BOTS evaluation design、refusal/cost accounting、全部结果、contamination controls、scaling、
  Limitations、Ethical Considerations、Conclusion 与 Appendices A～E；另核对 v3 新增 §4.3。interactive artifact
  页面当前无法稳定读取，故只记录论文中可核验的 artifact boundary，不声称复现 logs/dashboard。
- **Original Problem / Why Previous Design Was Reasonable**：peak success rate 适合回答“给足预算时是否可能完成”，
  对攻击能力上界与危险能力监测仍必要；token/tool-call count 也便于跨 run 采集。但生产 SOC 要为 inference、
  Splunk query、external enrichment 与 analyst attention 付费，相同成功率可能来自完全不同的成本、拒答和证据路径。
  因此只扩大 test-time compute 会把 offensive exploration 的经验错误外推到 defensive investigation。
- **Changed Constraint / Mechanism**：论文把 evaluation unit 改成 operating point：`model + task family + harness +
  cost cap + tool suite/prices + scorer + policy/refusal condition`。Cybench hard 用 39 个 sandboxed CTF、bash/python、
  hidden flag、3 attempts × 3 epochs；BOTS v1 用 31 个 scored questions、10,300 points、23 个 prerequisite-context
  questions、Splunk + limited enrichment tools、hint penalty 与 3 epochs。成本拆为 model-token ledger 与 priced-tool
  spend；预算超限按 failure，refusal 则按 benchmark semantics 单独记账。它不是新 scorer，而是把 success curve、
  marginal spend、tool discipline、policy behavior 与 contamination control 绑定为同一 Evaluation contract。
- **State Ownership / Control and Data Flow**：Inspect harness 拥有 prompt、auto-compaction、budget、tool-call、
  provider ledger 与 transcript；sandbox/Splunk/environment 拥有 executable evidence；scorer 拥有 flag 或 official
  points/hint state；provider policy/content filter 与 heuristic refusal detector 产生不同来源的 policy evidence；
  cost accountant 将 model spend 与 priced enrichment 映射到 run，benchmark registry 拥有 public-data provenance。
  retrospective cap 必须引用同一 completed trace，不能冒充新 prospective run；cache 实际命中与“按预期工具使用
  计价”的会计值也必须分开。
- **Implementation / Evaluation Contract**：ReAct-style agent 在 context 达 90% 时 auto-compaction；Agents 不知道
  token/dollar cap，但知道部分昂贵工具的 call limit。BOTS 的 Brave Search 最多 5 次，VirusTotal/WHOIS history
  各最多 3 次；论文把 Splunk、bash、python、DNS/live WHOIS 等计为零边际成本，并明确排除 Kubernetes、Splunk
  infrastructure、storage 与 analyst review，所以不是 total cost of operation。Cybench 成功率与 BOTS points/
  binary accuracy 均为三 epoch mean；scaling uncertainty 使用按 task ID 的 paired descriptive bootstrap。
- **What Evidence Proves / Does Not Prove**：在作者 runs 中，Cybench 对部分模型随 retrospective budget 增加而
  提升；BOTS 的额外 spend/tool volume 不呈同样关系，说明 workload 改变“边际预算买到什么”。更关键的是 BOTS
  no-tools controls 在有/无 prerequisite context 时仍获得很高分，证明这个公开旧 benchmark 的绝对分数不能直接
  解释为 live SOC investigation capability。它不证明某模型普遍更安全或更便宜：run matrix 是 observational，
  provider defaults/日期/effort 不完全一致，250-message cap 会截断高 tool-volume models，bootstrap 只是描述性，
  BOTS v2/v3 与真实 SOC/analyst workload 未评。v3 的 account-verification 前后差异也明确不是 causal intervention。
- **Trade-offs / Failure Modes / Coexistence**：成本感知评估让 release decision 靠近 production economics，却会
  对 price sheet、cache accounting、零成本假设、provider fallback 与预算截断高度敏感；同一 dollar cap 也可能掩盖
  latency、analyst load、risk severity 和 evidence quality。新 failure modes 包括 cheap-but-refusal-dominated system、
  high-volume tool thrashing、public-answer memorization、retrospective survival bias 与成本口径漂移。peak-capability
  benchmark 仍用于攻击上界，fresh/private incidents 用于污染更低的 operational evidence，static knowledge tests
  用于便宜回归；三者与 cost-success curve 共存。关系为 `Layering / Dependency`。
- **ROADMAP / Adjacent Chapters / Decision**：Ch62 为主 owner，已读 Ch62、66、68。Ch62 已明确要求完整 subject
  identity、Agent tools/sandbox/workflow/budget/environment、contamination controls、run-level evidence、cost/risk
  并列和 Pareto decision；Ch66 已定义 `cost_per_good_request`/outcome attribution，Ch68 已区分 refusal/policy 与
  underlying capability。该论文提供强 security-domain evidence，但没有新增未覆盖的长期机制，最终 disposition 为
  `No Change — Already Covered / Experimental Evaluation Case`；不修改 Books。

### SeerGuard — 27/30

- **Source Family / History / Access / Full-read Coverage**：`SEERGUARD`；arXiv:2607.15550 只有 v1，
  first-public 2026-07-17。已完整阅读 metadata、Abstract、Introduction、Related Work、双阶段 pipeline、
  Safety-Augmented World Model（SAWM）、数据与 multi-task training、MobileSafetyBench / instruction screening /
  MobileRisk / Next-State-QA 全部实验、ablation、latency、case study、Conclusion 与 Appendices A～C；并阅读
  Ch68、74、77、62、10。项目页、evaluation repository 与 SAWM Hugging Face weights 在 2026-08-12 已公开，
  只能作为 post-window implementation verification，不能倒写为 W29 当日 artifact 状态。
- **Original Problem / Why Previous Design Was Reasonable**：instruction-level filter 便宜、可在任何 GUI 状态之前
  拒绝明显恶意目标；执行后的 trajectory monitor 则能观察真实状态，不依赖预测。但前者看不到“当前屏幕 + 候选
  action”才产生的风险，后者对付款、发送消息、删除数据等不可逆 side effect 已经太晚。随着 Agent 从回答问题转向
  操作真实设备，安全决策必须在 action commit 前获得 state-dependent consequence evidence。
- **Changed Constraint / Mechanism**：SeerGuard 先用 `G_inst(I)` 对 instruction 做二分类与解释；通过后，每一步由
  Agent policy 生成 `a_t`，SAWM 根据 `(o_t,a_t)` 输出语义 next-state `s_hat_{t+1}`、action safety label 与理由，
  判 unsafe 即拒绝，否则才把 action 交给 environment。SAWM 基于 Qwen3-VL-8B-Instruct，以 59K general textual
  safety、33K multimodal mobile-risk、8K synthetic textual mobile-risk 和 48K Next-State-QA（总计 148K，
  safe:unsafe 约 2:1）做 multi-task SFT；multimodal labels 主要由 Qwen3-VL-30B-A3B 重标注，并加入少量人工风险案例。
- **State Ownership / Control and Data Flow**：SAWM 拥有的是 policy-bound prediction 与 risk evidence，不是真实
  environment state，也不拥有 authorization。GUI Agent 只提出 action；guard 预测可能后果；确定性 policy/tool
  executor 应结合 principal、scope、参数、side-effect class 与可选审批决定是否执行；environment 返回的 `o_{t+1}`
  才是 authoritative observation。论文 Algorithm 1 在安全标签通过后直接执行，没有把 prediction 与实际 state 的
  discrepancy 写入校准、rollback 或 policy update，因此生产实现必须额外保存 prediction provenance、actual outcome、
  mismatch、abstention、approval 和 recovery event。
- **Implementation / Evaluation Contract**：默认训练为 1 epoch、AdamW、batch 128、backbone learning rate
  `1e-6`、3% warmup、cosine schedule；论文未披露训练硬件。MobileSafetyBench 含 250 tasks（150 high-risk、
  100 low-risk），覆盖五类 mobile scenario，分别以 Qwen3-VL-8B、GPT-5.1（2026-03-10）和 Gemini-3.1-Pro-
  Preview（2026-03-14）作为 Agent backbone。四个 primitive outcomes 为 LC/LR/HC/HR；作者再定义
  `RCS_alpha = alpha*HC + (1-alpha)*LR` 与 `SUS_omega = omega*HR + (1-omega)*LC`，明确把 risk-aversion /
  safety priority 暴露为 policy weight，而不是通用 scalar truth。MobileRisk 含 102 unsafe + 102 paired safe
  trajectories，以 first-unsafe step 和 `B=5` 的 Step Score 评估；Next-State-QA 只测二元 future-state question。
- **What Evidence Proves / Does Not Prove**：在作者构造的 250-task workload 中，dual-stage guard 对三个 Agent
  backbone 都降低 `alpha=0.8` 的 RCS；SUS 的收益却依 backbone/weight 而变，例如 GPT-5.1 在 `omega=0.5`
  下降，说明 safety/utility 并非单调同时改善。SAWM 在 MobileRisk 得到 F1 0.723、Step Score 0.361，在
  Next-State-QA 得到 accuracy 0.762；这些结果支持 targeted safety augmentation 优于同组 baselines，但不证明
  binary semantic prediction 对长时延、隐式或真实生产风险可靠。Qwen-Agent 的平均任务时间 3.49→3.35 min
  主要混合了高风险任务提前拒绝，不能解释为 per-action guard overhead 为零，更不能外推 tail-latency/SLO。
- **Limitations / Trade-offs / New Failure Modes**：文本式 semantic next state 比像素生成便宜且更贴近决策，却可能
  丢失细粒度视觉状态、延迟后果与跨步组合风险；统一 model 的 instruction/action 两阶段还会产生 correlated failure。
  synthetic/re-annotated labels 引入 teacher hallucination、taxonomy bias 与二元标签过度简化；“任一步 unsafe 即拒绝”
  缺少 uncertainty、human escalation、safe action substitution 和 recovery，可能扩大 over-refusal 或形成 availability
  attack。论文没有独立 Limitations 章节，作者只在结论中把 missed fine-grained risks 与 false positives 列为后续方向；
  以上 failure analysis 中其余部分属于本项目的工程推断，不冒充作者实验结论。
- **Evolution / Coexistence**：演进链为 `instruction-only filtering → post-hoc real-trajectory monitoring →
  pre-execution state-aware consequence prediction → independent authorization / approval → actual-state validation and
  prediction reconciliation`。instruction filter 在低成本、显式恶意意图场景仍成立；post-hoc monitor 在真实结果审计、
  incident detection 与 guard calibration 中仍不可替代；deterministic rule/schema 对可形式化 invariant 仍应作为 hard
  gate。关系是安全决策时点上的 `Direct Evolution`，同时与 tool authorization 属于 `Layering / Dependency`。
- **ROADMAP / Adjacent Chapters / Decision**：Ch68 为主 owner。Ch68 已有 `model verdict is a policy-bound sensor,
  not authority` 与 model-proposal→schema→authorization→approval→execution→audit 主线，Ch74 也已拥有 side-effect、
  idempotency 与 observation trust boundary；但尚未把 state-aware consequence prediction 明确写成 instruction filter 与
  deterministic authorization 之间的独立 sensing layer。最终 disposition 为
  `Refine — New Mechanism / Experimental`；已写入 `PLATFORM-SECURITY`，其他节点只作短 handoff。

### Environment-free Synthetic Data Generation for API-Calling Agents — 29/30

- **Source Family / History / Access / Full-read Coverage**：`ENVIRONMENT-FREE-API-DATA` / ESAT；
  arXiv:2607.16900v1 first-public 2026-07-18，v2 为 7 月 21 日。W29 以 82 页 v1 为事件证据；已阅读
  metadata、Introduction、Related Work、三阶段 method、全部 AppWorld/OfficeBench results、judge/simulator
  quality、dataset comparison、Conclusion、data/yield/failure/coverage、training/inference、task synthesis、simulator、
  agent、trajectory judge、synthetic app suite 与 example trajectories 等全部相关 appendices。v2 与 Apple Research
  页面只作 post-window revision/affiliation verification；未发现作者公开 code/data artifact，因此不声称可复现。
  已读 Ch23、74、77、62、10。
- **Original Problem / Why Previous Design Was Reasonable**：真实 API endpoint、可执行 sandbox 和预填 backend
  能让 trajectory 的 response 与 final side effect 来自 authoritative environment，并用 executable verifier 过滤；对
  高风险 write、真实 error semantics 和 final release evaluation，这仍是最可靠旧方案。但每接入一个新 API family
  都要实现 backend、构造多样 state、隔离副作用并支付执行成本，训练数据覆盖速度被 environment engineering 限制。
  早期 static/single-turn synthetic tool data 更便宜，却不训练跨 call state tracking、read-after-write 与错误恢复。
- **Changed Constraint / Mechanism**：ESAT 把输入收缩为 versioned API specifications。Stage 1 以 difficulty、
  read/write/mixed、task focus、app/API count 组成 360 类 buckets，结合 inverse-frequency sampling 生成、judge、
  intent-level rewrite tasks；Stage 2 由 teacher Agent 逐步发 API call，simulator 根据 API schema、arguments、task、
  frozen user/time 与同一 task 内该 app 的 accepted history 合成 response；Stage 3 对完整 trajectory 多次 judging，
  只保留 majority-positive samples。它把“完整环境实现”替换成“specification + derived virtual state + layered checks”，
  而不是删除 state。
- **State Ownership / Control and Data Flow**：API specification 拥有 typed contract；bucket/coverage ledger 拥有
  synthesis distribution；每个 task/app 独立 rolling history 是 simulator 的派生 virtual state，task 结束即清空；
  teacher Agent 只提出 call；deterministic validator 拥有 input/type/constraint 与 output schema verdict；LLM simulator
  生成 semantic response；read-only GET 才进入 simulator-judge，POST/PATCH/DELETE 在结构通过后直接接受；
  trajectory judge 拥有 retention decision。没有 backend transaction log 或真实 final state，因此 write acknowledgment
  与后续 history 都是 synthetic claims，不能升级为 side-effect ground truth。
- **Implementation / Evaluation Contract**：task generator/judge/rewriter 用 GLM-4.7-FP8；teacher/simulator 用
  GLM-5.1-FP8；trajectory filter 用 Gemini-3.1-Pro。AppWorld 457 APIs/9 apps，Test-N 168、Test-C 417；
  OfficeBench 使用 20 APIs/8 apps，经排除 OCR-dependent/unsolvable 后为 26 个 two-app、46 个 three-app tasks。
  ESAT-AW7 为 340 APIs/7 apps 的约 9K trajectories，ESAT-S52 为 52 个 synthetic apps/1,017 APIs 的约 6K，
  AWT 是 90 个真实 AppWorld train tasks × 8 rollouts 经 executable verifier 后留下 634 条。SFT context 32,768、
  per-device batch 1、AdamW `2e-5`、1% warmup、linear decay、平均约 4 samples packing；<14B 用 8×H100，
  ≥14B 用 8×B200；默认 10 epochs，Qwen3.5 为 5；evaluation temperature 1、每 task 8 samples、报告 pass@1
  mean/std，step cap 50/30。未披露 synthesis hardware、token/dollar cost、wall time 或 production SLO。
- **What Evidence Proves / Does Not Prove**：在作者设置中，ESAT SFT 对 Qwen3/Qwen3.5 1.7B～27B 在两个
  benchmark 普遍优于各自 zero-shot；ESAT-S52-AW7 也普遍优于仅 634 条 AWT，但数据规模、teacher、filter 与
  domain breadth 不匹配，不能解释为 synthetic trajectory 天生优于 real execution。Gemini trajectory judge 对 720 条
  real-environment trajectories 的 accepted precision 为 95.2%，200 条 balanced human sample 上 agreement 95%、
  kappa 0.90；但论文未报告 recall/真实 class prevalence，不能据此断言过滤器完整。对 1K accepted trajectories
  约 27K simulated calls 的 93.7% validity 仍由 GPT-5.1 judge 给出，脚注只说另一 frontier model 趋势相近，
  不是 executable proof。response >2K tokens 的 failure 达 23%，说明 fidelity 明显受 output length 影响。
- **Limitations / Trade-offs / New Failure Modes**：per-app history 降低 context 成本和跨 app 污染，却可能漏掉
  shared entity、credential、transaction 或 cross-app invariant；同一 simulation rules 同时喂给 simulator/judge，
  产生 correlated blind spot。write call 不做 semantic judge 是显式 cost/fidelity trade-off，容易接受合法 schema 下的
  不可能 mutation、重复副作用或错误 acknowledgment。task/trajectory 过滤的大量丢弃、multi-app yield 偏低、
  OfficeBench 仅 14/20 APIs 被覆盖，也说明 coverage ledger 不能只看 raw generated count。无独立 Limitations 章节；
  作者只直接量化 response-length failure 与数据分布偏斜，其余是本项目工程推断。
- **Evolution / Coexistence**：演进链为 `single-turn mocked tool examples → real executable environment + verifier
  → spec-only stepwise simulator with state history/schema/judge → hybrid curriculum + sampled real execution → production
  shadow/outcome validation`。ESAT 适合 bootstrap 新 API、扩大 low-risk SFT breadth；real environment 在 final
  evaluation、write semantics、error/latency/rate-limit、security/policy 与 calibration 中仍成立。关系为 `Direct Evolution`，
  与 DSWorld 的 execution/simulation routing 是 `Principle Reuse`，但一个生成训练数据、一个加速 search transitions，
  不能互换。
- **ROADMAP / Adjacent Chapters / Decision**：Ch23 为主 owner。Ch23 已把 synthetic data 分为 model-judge 路线与
  executable specification compilation，并强调 simulator/version/verifier lineage；但 ESAT 补出第三个长期分支：仅有
  API specification 时，如何显式建立 derived state、确定性 schema checks 与 model-judged semantic checks，再用少量
  real environment 校准，而不是把“自洽”写成“可执行”。Ch74 承接真实 tool/side-effect contract，Ch77 承接 durable
  authoritative workflow state，Ch62 承接 judge/executable evidence boundary，Ch10 承接 world-model analogy。
  最终 disposition 为 `Refine — Existing Argument / Experimental`；现有 Data/Workflow 主线经复核保留。

### LightMem-Ego — 23/30

- **Source / Coverage**：`LIGHTMEM-EGO`；arXiv:2607.11487v1，first-public 2026-07-13；已读 streaming
  capture、short/long-term hierarchy、asynchronous consolidation、multimodal retrieval、evaluation 与结论。
- **Mechanism / Evidence**：原始连续记录适合保留证据，却不适合直接进入有限 context；系统把时间戳流先写入
  short-term store，再异步提炼 long-term memory，查询同时检索近期与长期状态。作者的小规模 object、conversation、
  life-query 实验只证明 prototype 的可行性，未证明跨设备 identity、删除、隐私与长期 consolidation 正确性。
- **Evolution / Decision**：raw history → hierarchical retrieval → asynchronous consolidation；新增 stale summary、错误合并和
  provenance 丢失风险。Ch73 已有 source/derived memory、promotion、supersession、delete 与 rollback，故
  `No Change — Already Covered`。

### AdvancedMathBench — 23/30

- **Source / Coverage**：`ADVANCEDMATHBENCH`；arXiv:2607.11849v1，2026-07-13；已读 245-item ProverBench、
  888-trajectory VerifierBench、约 2k expert labels、1.2k repaired positives、GRPO meta-verification、8-pass
  pessimistic verification、baselines、ablation 和 appendix protocol。
- **Mechanism / Evidence**：最终答案不能证明自然语言 proof 有效，因此 ground truth 同时记录 validity、fatal/recoverable
  errors、first fatal step 与 rationale，再用 held-out 94 examples 校准 verifier。作者结果证明 polarity-only judge 会高估
  verification；未证明 94-item held-out set 能代表所有数学分布，也未消除 meta-verifier 自身偏差。
- **Evolution / Decision**：answer match → process labels → rationale/error localization → verifier-of-verifier；这正是 Ch62
  已有 evaluation object 与 verifier validity contract，故 `No Change — Already Covered`。

### Proxy-Guided Update Signals — 25/30

- **Source / Coverage**：`PROXY-GUIDED-UPDATE`；arXiv:2607.11505v1，2026-07-13；已读 reward-optimization / distribution-
  matching 分析、三阶段 P-OPD、cross-scale/sequential/cross-generation transfer、calibration sensitivity 与 appendix recipe。
- **Mechanism / Evidence**：先在低成本 proxy 上探索，再用 expert/base 的 token log-ratio
  `Δφ=log πφ+−log πφ` 表示相对 update direction；target 用自身 frozen base 约束 `Δθ`，避免把 proxy 的绝对分布直接复制。
  Qwen-family math/code 实验支持相对 signal 可迁移，但不证明跨 tokenizer、架构或远距离 policy family 仍保持语义。
- **Evolution / Decision**：teacher output imitation → same-state OPD → lineage-relative update transfer；收益是探索复用，代价是
  proxy/target state alignment、calibration coefficient 与错误方向放大。`Refine — Existing Argument / Experimental`，Ch29 owner。

### Function-Aware Fill-in-the-Middle — 24/30

- **Source / Coverage**：`FUNCTION-AWARE-FIM`；arXiv:2607.12463v1，2026-07-14；已读 PDG/AST target selection、
  function complexity/inferability scoring、CoT-middle construction、mid-training setup、agent/code benchmarks、ablation 与 limitations。
- **Mechanism / Evidence**：普通 left-to-right code 只训练“调用后继续”；function-aware FIM 按 caller/callee/sibling dependency
  选取可由上下文推断的完整函数，将外部返回值插回 reasoning 的结构同构显式化。作者实验限 Python，默认 rationale 依赖
  Gemini teacher，跨语言与跨 base 验证不完整。
- **Evolution / Decision**：token-local FIM → dependency-aware function hole → tool-observation-compatible mid-training；新增 parser、
  teacher provenance 与 corpus-selection bias。`Refine — Existing Argument / Experimental`，Ch24 owner，Ch74 handoff。

### Read It Back / SpectraReward — 23/30

- **Source / Coverage**：`SPECTRAREWARD`；arXiv:2607.11886v1，2026-07-13；已读 prompt-likelihood reward、self-reward
  variant、training setup、four image benchmarks、reward-backbone ablation、EOS/VAE appendix 与 limitations。
- **Mechanism / Evidence**：不让 MLLM 直接打分，而是在 image-conditioned teacher-forced pass 中计算原 prompt 的可恢复
  likelihood，把 image→text readback 当 alignment signal。它减少 judge prompt decomposition，却受 reward MLLM 视觉理解约束，
  更偏 explicit semantics，物理常识、美学与隐式关系需要互补 reward。
- **Evolution / Decision**：scalar judge → decomposed checks → likelihood-based inverse task signal；可能引入 prompt-copy shortcut 和
  reward-backbone blind spot。`Refine — Existing Argument / Experimental`，Ch29 owner，Ch62 handoff。

### KnowAct-GUIClaw — 24/30

- **Source / Coverage**：`KNOWACT-GUICLAW`；arXiv:2607.12625v1，2026-07-14；已读 Know–Route–Act–Reflect、host/GUI
  subagent split、memory/skill evolution、benchmarks、experimental logs 与 conclusion。
- **Mechanism / Evidence**：trajectory 完成后反思并把可复用经验提升为 memory/skill，再由 router 在后续任务选择；这能避免每次
  从零规划，但 evaluation 不能证明 promotion 无污染、跨版本 skills 仍有效或个人数据治理完备。
- **Evolution / Decision**：保存轨迹 → 检索轨迹 → derived skill → routed execution；Ch73/80 已明确 provenance、promotion、
  review、delete、rollback 与 runtime governance，故 `No Change — Already Covered`。

### Tracing Agentic Failure from the Flow of Success — 25/30

- **Source / Coverage**：`SUCCESS-FLOW-FAILURE-TRACE`；arXiv:2607.12747v1，2026-07-14；已读 Oat one-class
  formulation、representation extraction、Neural CDE/gated control path、top-k/conformal detection、OOD alignment、baselines、
  ablations、appendix 与 stated future work。
- **Mechanism / Evidence**：只用成功轨迹拟合连续 latent dynamics；失败轨迹中偏离 learned success flow 的 steps 被视为候选根因。
  3-layer CDE、PCA-64、success 80/20 split 与 conformal threshold 在作者 agent benchmarks 有效，gating 改善 OOD AUROC；
  deviation 仍是 attribution，不是 causal proof，success distribution 漂移会制造 false positive。
- **Evolution / Decision**：failure labels → success-only anomaly detection → calibrated step candidates；收益是降低标注成本，代价是
  representation access、normality drift 与 causal ambiguity。`Refine — Existing Argument / Experimental`，Ch65 owner，Ch62 handoff。

### ShortOPD — 24/30

- **Source / Coverage**：`SHORTOPD`；arXiv:2607.13124v1，2026-07-14；已读 pruning/OPD objective、repetition detector、
  EMA horizon controller、Qwen3-4B 25%-pruning experiment、matched baselines、domain ablation、training details 与 limitations。
- **Mechanism / Evidence**：压缩后正确 trajectory 可能只是 probability demotion；student on-policy states 由原模型提供 dense token
  targets。早期 repetitive suffix signal 很低，controller 以 repetition、clean truncation、effective length 的 EMA 缩短/增长 rollout
  horizon，并 checkpoint control state。作者数据支持该 workload 的 token/time 节省，不证明更重 pruning 或其他 model family。
- **Evolution / Decision**：off-policy recovery → fixed-horizon OPD → damage-aware closed-loop horizon；新增 loop-detector error、controller
  oscillation、domain coverage 和 teacher compute。`Refine — Existing Argument / Experimental`，Ch29 owner，Ch52 handoff。

### PalmClaw — 23/30

- **Source / Coverage**：`PALMCLAW`；arXiv:2607.13027v1，2026-07-14；已读 native sessions/memory/skills/tools、context
  assembly、agent loop、tool execution、MobileTask/AssistantBench、deployment traces 与 permission/workspace boundary cases。
- **Mechanism / Evidence**：GUI action 对兼容性合理，却产生长而脆弱的动作链和过宽权限；PalmClaw 把 agent state 留在设备，并用
  typed arguments/results 与 tool-specific boundaries 暴露 device capabilities。作者的 success/time 数字是特定 device、task、baseline
  结果，不证明所有 app 都可由 native tools 覆盖或 isolation 已达到 production security。
- **Evolution / Decision**：remote GUI control → on-device agent runtime → capability-scoped device tools；新增移动端资源压力、tool supply
  chain 与 local data lifecycle。`Refine — Existing Argument / Experimental`，Ch80 owner，Ch68/74 handoff。

### SEED — 27/30

- **Source / Coverage**：`SEED-OPD`；arXiv:2607.14777v1，2026-07-16；已读 SFT analyzer warm-up、on-policy trajectory
  collection、skill extraction、ordinary/skill-context rescoring、joint RL+distillation、ALFWorld/WebShop/search QA、multimodal extension、
  sample-efficiency tables、hyperparameters 与 appendix examples。
- **Mechanism / Evidence**：current policy 同时充当 actor 与 analyzer，从完成轨迹提取 hindsight skill；同一 action 在普通与 skill-
  augmented context 下的 probability shift 成为 dense on-policy signal，与 sparse outcome RL 联合优化。它缓解 credit assignment，
  但 analyzer 与 actor 共演化会形成 self-confirmation、skill staleness 与错误经验放大。
- **Evolution / Decision**：outcome-only RL → static teacher skill distillation → policy-synchronous derived skill signal；作者 benchmark 不证明
  open-world stability。`Refine — Existing Argument / Experimental`，Ch29 owner，Ch73 handoff。

### BadWAM — 25/30

- **Source / Coverage**：`BADWAM`；arXiv:2607.15207v1，2026-07-16；已读 threat model、action-only / imagination-
  preserving attacks、query optimizer、closed-loop suites、ablation、transfer、defenses 与 appendix query accounting。
- **Mechanism / Evidence**：小视觉扰动可以让 executed action 偏离，同时以 future-preserving regularization 保持 imagined future 接近
  clean prediction；这直接否定“看起来合理的 imagined state 可单独充当 action safety proof”。作者闭环实验是 WAM-specific attack
  evidence，不证明所有 world models 同样脆弱或现有 detector 均无效。
- **Evolution / Decision**：action model → coupled world-action model → imagination/action consistency verifier；新增双通道攻击面、adaptive
  attacker 和 detector calibration。`Refine — Existing Argument / Experimental`，Ch68 owner，Ch10/62 handoff。

### From Pixels to States — 23/30

- **Source / Coverage**：`PIXELS-TO-STATES`；arXiv:2607.14076v1，2026-07-15；已读 survey taxonomy、action control、
  explicit/latent/entangled state、persistence、latency 与 90-hour Black Myth data-engine design。
- **Mechanism / Evidence**：纯 observation prediction 对短期视觉连续合理，但交互世界还要执行 rule-governed state transition、保持长期
  consequence 并满足实时闭环；action→state→observation 把 authoritative state 从 pixels 中分离。论文主要是 taxonomy 与 dataset，
  不是对某一 state representation 的因果 benchmark。
- **Evolution / Decision**：video continuation → action-conditioned pixels → explicit/structured world state；旧 pixel model 在开放视觉生成仍
  成立。`Refine — Existing Argument / Experimental`，Ch10 owner，Ch77 handoff。

### Demystifying On-Policy Distillation — 25/30

- **Source / Coverage**：`DEMYSTIFYING-OPD`；arXiv:2607.13399v1，2026-07-15；已读 OPD role study、teacher/student
  mismatch、two length-exploitation modes、advantage clipping/log compression、seven benchmarks、appendix configurations 与 limitations。
- **Mechanism / Evidence**：OPD 更像 exploration catalyst 而非 capability-ceiling breaker；teacher/student gap 会让 token guidance 与 task
  correctness 错位，聚合 objective 又可能通过过长 padding 或过短 answer 被利用。clipping/log compression 限制 signal extremes，
  但阈值依赖 capacity gap，证据主要来自可验证数学任务。
- **Evolution / Decision**：unconditional token guidance → pathology diagnosis → regulated update signal；旧弱/同源 teacher 在低 mismatch
  下仍合理。`Refine — Existing Argument / Experimental`，Ch29 owner。

### Byte-Exact KV-State Grafting — 22/30

- **Source / Coverage**：`KV-CACHE-GRAFTING`；arXiv:2607.14431v1，2026-07-15；已读 exactness definition、own-position
  constraint、flywheel protocol、deterministic measurements、routing/paging cases、negative results、limitations 与 reproducibility boundary。
- **Mechanism / Evidence**：在 pinned deterministic build、相同 architecture/configuration 与原位置恢复时，作者用 SHA-equal logits / zero
  KL 验证 serialized KV reuse；recurrence 与 held-out transfer 必须分开。核心 graft engine 是 proprietary，部分比较使用不同 benchmark
  的 vendor anchors，单作者/closed suite 不能支持其普遍 capability、energy 或 context claims。
- **Evolution / Decision**：ephemeral prefix cache → persistent exact state artifact → verified-state routing；只在 own-position exact，misroute、
  stale verification、disk paging 与 architecture identity 成为新 failure modes。`Emerging / Disputed — Weekly Only`，Ch41 provisional owner。

### Rethinking Harness Evolution Evaluation — 24/30

- **Source / Coverage**：`HARNESS-EVOLUTION-EVAL`；arXiv:2607.12227v1，2026-07-14；已读 matched-budget search baselines、
  same-benchmark leakage、held-out transfer、Terminal-Bench experiments、analysis 与 limitations。
- **Mechanism / Evidence**：harness evolution 本身是反复读取 task feedback 的 search，必须与相同 feedback/inference budget 的 test-time
  search 比较，并把 search tasks 与 held-out evaluation 分离。作者结果也表明 benchmark 若 model-limited 或 harness-insensitive，自动
  evolution 的边际收益会很小。
- **Evolution / Decision**：single final score → budget-matched search accounting → held-out harness transfer；Ch62 已有 harness identity、
  adaptation budget 与 evaluation isolation，故 `No Change — Already Covered`。

### Distilled Reinforcement Learning for LLM Post-training — 27/30

- **Source / Coverage**：`DISTILLED-RL`；arXiv:2607.17247v1，2026-07-19；已读 RL/OPD analysis、reverse importance
  sampling、ratio clipping、negative reset、geometric normalization、math/code experiments、ablations 与 appendix settings。
- **Mechanism / Evidence**：teacher/student likelihood ratio 只重新分配 positive-advantage trajectory 内的 token-level RL signal；negative
  samples reset 为普通 RL penalty，sequence-wise geometric mean normalization 避免 teacher scale 系统性改变 response weight。
  作者实验支持特定 family 的 selective knowledge transfer，不证明 arbitrary cross-family logits 可比较或 teacher knowledge 必然正确。
- **Evolution / Decision**：outcome RL → unconditional OPD → reward-gated teacher reweighting；新增 likelihood calibration、ratio clipping
  bias 与 teacher-policy availability。`Refine — Existing Argument / Experimental`，Ch29 owner。

### JoyNexus — 26/30

- **Source / Coverage**：`JOYNEXUS`；arXiv:2607.16074v1，2026-07-17；已读 Training/Inference/Environment service
  decomposition、SFT/RL/eval flows、tenant state、global queues、group batching、realistic workload replay、controlled simulation 与 conclusion。
- **Mechanism / Evidence**：resident shared VLM backbone 与 tenant-private action module、optimizer、rollout、policy version 分离；compatible
  schemas 可合并 shared forward，再拆回 private loss/backward/update。作者明确 group-batching 数字只覆盖可共享 forward，multi-tenant
  trace 也允许单 tenant wall time 变长，不等于 end-to-end/SLO 普遍改善。
- **Evolution / Decision**：exclusive job allocation → disaggregated model/environment services → state-isolated multi-tenant multiplexing；新增
  fairness、version freshness、failure isolation 与 accounting。`Refine — Existing Argument / Experimental`，Ch56 owner，Ch67 handoff。

### DataFlow-Harness — 27/30

- **Source / Coverage**：`DATAFLOW-HARNESS`；arXiv:2607.16617v1 first-public 2026-07-18，v2 2026-07-24；已读
  Skills、MCP live registry/state、typed incremental mutation、structural validation、WebUI synchronization、12-task evaluation、ablation、
  build logs 与 limitations；v2 只作 post-window verification。
- **Mechanism / Evidence**：free-form script 的输出不是 platform-owned artifact；agent 通过 typed mutations 修改 authoritative DAG，MCP
  提供 live schema/state，UI 与 conversation 同步同一对象。93.3% 是单 agent/model、12-task、platform-specific observed pass rate；
  schema validation 不保证 semantics，尚未证明 provenance、concurrent editing 与 recovery。
- **Evolution / Decision**：NL→script → grounded mutation API → durable editable workflow；新增 mutation transaction、revision conflict、
  semantic verifier 与 rollback。`Refine — Existing Argument / Experimental`，Ch77 owner，Ch79/80 handoff。

### Training Variable Long Sequences with Data-Centric Parallel — 26/30

- **Source / Coverage**：`DATA-CENTRIC-PARALLEL`；arXiv:2608.07524v1 metadata 明确为 2026-07-14；已读 DCP-inter/
  DCP-intra、profiling/search、gradient accumulation、dynamic checkpointing、32×H200 experiment、ablation、implementation appendix 与 limits。
- **Mechanism / Evidence**：static parallel config 在 variable lengths 下让 slow batch 决定 iteration；DCP-inter 按 sequence length profile
  选择 sequence-parallel size，并调整各 batch accumulation steps 使执行时间靠拢；DCP-intra 再按 memory/length 动态减少不必要
  recomputation。作者最高 2.88× 绑定 32 H200、两个 Transformer 与三组合成长度分布，不外推为通用速度。
- **Evolution / Decision**：one-model-one-plan → bucketed static plans → batch-driven runtime selection；新增 profiling drift、collective group
  reconfiguration、accumulation/convergence 和 checkpoint state。`Refine — Existing Argument / Experimental`，Ch32 owner，Ch34/59 handoff。

## Expanded Candidate Review Queue

2026-08-13 exact HTML retry 恢复 15/19 项正文；另 4 个 spillback 也全部恢复并完成全文审计。
以下 4 项连续重试仍不可访问，按用户授权的 blocked-skip 规则保留。它们不得被统计为 Full Source
Review，也不阻塞 forward cursor；访问恢复后仍须补完正文、artifact 与相邻章节核验。

| Candidate | Source Family / First-public | Primary Source | ROADMAP Owner | Review Focus | Status |
| --- | --- | --- | --- | --- | --- |
| Multi-Agent LLMs Fail to Explore Each Other | `MULTI-AGENT-EXPLORATION-FAILURE` / 2026-07-13 | https://arxiv.org/abs/2607.11250 | Ch78 | exploration regret、polarization、communication topology | Unverified / Blocked Backlog |
| Capability-Oriented Benchmark for AI Scientists | `AI-SCIENTIST-CAPABILITY-BENCH` / 2026-07-13 | https://arxiv.org/abs/2607.11079 | Ch62 | claim type、assumption validity、code-versus-science evidence | Unverified / Blocked Backlog |
| Generative Compilation | `GENERATIVE-COMPILATION` / 2026-07-15 | https://arxiv.org/abs/2607.13921 | Ch77 | compiler feedback during decoding、state/latency boundary | Unverified / Blocked Backlog |
| LongStraw | `LONGSTRAW` / 2026-07-16 | https://arxiv.org/abs/2607.14952 | Ch29 | 2M-token RL parallelism、memory budget、quality contract | Unverified / Blocked Backlog |

### Date-corrected spillbacks

- ABot-AgentOS (`2607.10350`) v1 为 2026-07-11，回归 W28；7 月 15/17 日只是 v2/v3。
- GRASP (`2607.10463`) v1 为 2026-07-11，回归 W28。
- Weak-to-Strong Direct OPD (`2607.05394`)、What LLM Forecasters Know (`2607.08046`)、
  PolicyShiftGuard (`2607.05910`) 与 Root Causes (`2607.07702`) 均按 v1 回归 W28。

### Cross-Week Spillback Closure — 4 Identities

四项均已恢复全文、正式评分并纳入上方 Full Source Review。DataFlow-Harness v1 归 W29、v2 只作
post-window verification；`2608.07524` 的编号/date 异常按 arXiv metadata 原样保留，不进行推断性校正。

## Final Books Integration Ledger

| # | Candidate / Source Family | Final disposition | Stable owner / evidence |
| ---: | --- | --- | --- |
| 1 | Kimi K3 announcement | Refine — Existing Argument | MODEL-MOE；router→dispatch/runtime constraint 已复核 |
| 2 | PerceptionBench | No Change — Already Covered | PLATFORM-EVALUATION-SYSTEM；perception/reasoning confound 已覆盖 |
| 3 | Claude values across models/languages | Weekly Only — Behavioral Study | 不改变系统设计 contract |
| 4 | Harness Handbook | No Change — Already Covered | AGENT-CONTEXT / AGENT-PLATFORM；progressive evidence context 已覆盖 |
| 5 | Ring-Zero | Weekly Only — Experimental | TRAIN-GRPO；证据不足以改变 distributed RL 结论 |
| 6 | AgentCompass | No Change — Already Covered | PLATFORM-EVALUATION-SYSTEM；subject/harness/environment split 已覆盖 |
| 7 | LightMem-Ego | No Change — Already Covered | AGENT-MEMORY；hierarchy/provenance 已覆盖 |
| 8 | AdvancedMathBench | No Change — Already Covered | PLATFORM-EVALUATION-SYSTEM；verifier validity 已覆盖 |
| 9 | Proxy-Guided Update Signals | Refine — Existing Argument | TRAIN-GRPO；proxy 不能越过 outcome Gate |
| 10 | Multi-Agent exploration failure | Unverified / Blocked | 无机制 owner；等待 primary text |
| 11 | Function-Aware FIM | Refine — Existing Argument | TRAIN-PRETRAINING；dependency-aware code objective |
| 12 | SpectraReward | Refine — Existing Argument | TRAIN-GRPO；inverse-task reward 受 reward-model 边界限制 |
| 13 | AI Scientist capability benchmark | Unverified / Blocked | 无机制 owner；等待 primary text |
| 14 | KnowAct-GUIClaw | No Change — Already Covered | AGENT-MEMORY / AGENT-PLATFORM；derived Skill governance 已覆盖 |
| 15 | Success-flow failure tracing | Refine — Existing Argument | PLATFORM-TRACE；anomaly attribution 不等于 causal proof |
| 16 | ShortOPD | Refine — Existing Argument | TRAIN-GRPO；damage-aware rollout-horizon controller |
| 17 | PalmClaw | Refine — Existing Argument | AGENT-PLATFORM；on-device capability-scoped tools |
| 18 | Generative Compilation | Unverified / Blocked | 无机制 owner；等待 primary text |
| 19 | LongStraw | Unverified / Blocked | 无机制 owner；等待 primary text |
| 20 | SEED | Refine — Existing Argument | TRAIN-GRPO；policy-synchronous derived-skill signal |
| 21 | SearchOS-V1 | No Change — Already Covered | AGENT-WORKFLOW；authoritative typed state 已覆盖 |
| 22 | OPD² | Refine — New Mechanism | TRAIN-GRPO；matched-base policy-delta objective |
| 23 | Recursive Harness Self-Improvement | Refine — New Mechanism | AGENT-WORKFLOW；adjacent-revision local search |
| 24 | Muon for Agentic RL | Refine — New Mechanism | TRAIN-GRPO；optimizer/update-scale/sharding recipe identity |
| 25 | Xiaomi-Robotics-1 | Refine — Existing Argument | MULTIMODAL-EMBODIED-VLA；embodiment-free→alignment 已吸收 |
| 26 | DSWorld | Refine — Existing Argument | AGENT-WORKFLOW；simulation fidelity / authoritative-state recovery |
| 27 | Cost-aware security agents | No Change — Already Covered | PLATFORM-EVALUATION-SYSTEM；success/cost operating point 已覆盖 |
| 28 | SeerGuard | Refine — New Mechanism | PLATFORM-SECURITY；semantic sensor→deterministic Gate→reconciliation |
| 29 | Environment-free API data | Refine — Existing Argument | TRAIN-DATA；simulated transition data 与 real calibration |
| 30 | BadWAM | Refine — New Mechanism | PLATFORM-SECURITY；imagined-state consistency 不是 action proof |
| 31 | From Pixels to States | Refine — Existing Argument | MULTIMODAL-WORLD-MODELS；authoritative state 与 pixels 分离 |
| 32 | Demystifying OPD | Refine — Existing Argument | TRAIN-GRPO；capacity-gap/pathology-regulated update |
| 33 | Byte-Exact KV-State Grafting | Disputed / Emerging | INFER-KV-CACHE；closed engine 与 cross-benchmark anchors 不足 |
| 34 | Harness Evolution Evaluation | No Change — Already Covered | PLATFORM-EVALUATION-SYSTEM；budget/search split 已覆盖 |
| 35 | Distilled RL | Refine — Existing Argument | TRAIN-GRPO；outcome-gated teacher reweighting |
| 36 | JoyNexus | Refine — Existing Argument | PLATFORM-RESOURCE-SCHEDULING；state-isolated multi-tenant services |
| 37 | DataFlow-Harness | Refine — Existing Argument | AGENT-WORKFLOW；typed authoritative DAG mutation |
| 38 | Data-Centric Parallel | Refine — New Mechanism | TRAIN-DISTRIBUTED-TRAINING；batch-driven admitted plan selection |

计数：`Refine 22 / No Change 9 / Weekly Only 2 / Disputed 1 / Unverified-Blocked 4`。四个 blocked family
没有根据标题或摘要补写机制，Disputed family 也没有进入长期结论。

## Repository Changes

- 删除已被 W29 完整吸收的 `papers/2026/07/16/README.md`；
- 全文重审后 refine Ch21 的 router-to-dispatch coupling；
- Harness Handbook 与 AgentCompass 判定为现有章节已覆盖，未重复写入；
- 未修改 ROADMAP 或章节结构。
- 2026-08-09 discovery replay 将 W29 从 6 个恢复为 26 个 scored source families；新增
  SearchOS 全文 Source Review，并校正 6 项 W28 spillback。
- 2026-08-11 disposition review 将 19 项未读候选逐项转入 `Unverified / Blocked Backlog`；
  current-review pending 清零，forward cursor 推进 W30；未修改 Books。
- 2026-08-12 将 2608.07524 的 7 月 14 日 source identity 从 8 月 11 日去重记录实际回写 W29；
  当时保持 unscored blocked；2026-08-13 已恢复正文并闭合评分。fixed official/Infra checkpoint 通过，未修改 Books。
- 2026-08-12 关闭 W30 的 11 项 W29 attribution identities：逐项恢复 arXiv ID、v1 date 与 owner week，
  OPD²、Recursive Harness Self-Improvement、Muon Agentic RL、Xiaomi-Robotics-1、DSWorld 与
  Cost-Aware Security Agents、SeerGuard、Environment-free API data 随后完成全文、
  appendix、评分与相邻章节审计；OPD²、Muon 与 Xiaomi-Robotics-1 另核验 official code；DSWorld 所列
  artifact 当前不可访问并显式保持 Unverified；SeerGuard 的当前 project/evaluation/model artifacts 只作
  post-window verification；Environment-free API data 的 v2/Apple page 也只作 post-window verification；
  其余 3 项当时仅完成 metadata/abstract identity review，保持 unscored blocked；未把摘要当作 Full Source Review。
- 2026-08-12 对剩余三项 W30→W29 attribution backlog 再执行 access review：Distilled RL 的 arXiv
  HTML/PDF 与作者仓库、JoyNexus 正文、DataFlow-Harness 正文与 artifact 均未能越过已保存的访问策略。
  三项当时按用户授权的 blocked-skip 规则保持 unscored，不以摘要推断 mechanism/evaluation，也不阻塞 forward
  sweep；该状态随后被 2026-08-13 exact HTML recovery 取代。
- 2026-08-13 exact arXiv HTML retry 恢复 15/19 expanded candidates 与全部 4 个 spillbacks；逐篇覆盖
  metadata、method、state/control flow、evaluation/ablation、limitations/appendix 与相邻章节，形成 19 个
  non-template Full Source Reviews。Distilled RL、JoyNexus、DataFlow-Harness、Data-Centric Parallel 正式评分；
  其余 4 项连续失败后按 blocked-skip 保留。最终账目为 38 scored / 34 reviews / 4 blocked / 0 ordinary pending。
- W29 Books Gate 通过后，refine `TRAIN-GRPO`、`TRAIN-DISTRIBUTED-TRAINING`、`PLATFORM-SECURITY`
  与 `AGENT-WORKFLOW`；K3/Xiaomi 既有 integration 经复核保留；
- 新增 38 行 final ledger；未新增 Part、章节或 Stable Node，cursor 进入 W30。

## Open Questions

1. K3 的 hybrid state paging 与 prefix cache 是否能由多个 runtime 独立复现？
2. Behavior Handbook 如何检测 dynamic registration 与 configuration-only behavior？
3. Agent evaluation 的 environment artifact、seed、timeout 与 external service 应如何版本化？
4. PerceptionBench 的 atomic decomposition 是否能减少而非重分配 annotation ambiguity？
5. 非 supernode topology 下，K3 expert communication 与 hybrid state transfer 的代价如何变化？
6. 四个 blocked source 恢复后，Multi-Agent exploration、AI-scientist capability、Generative Compilation、LongStraw
   是否会改变当前 blocked-skip disposition？
7. SearchOS 的中央 SOCM 在 worker crash、并发 writer、恶意 evidence 与跨 tenant 环境下如何恢复？
8. DCP 的 per-batch parallel group / recomputation selection 如何与 elastic process groups、optimizer step semantics
   和 checkpoint restart 组合，而不把 profiling drift 变成 correctness drift？
9. JoyNexus 的 tenant-private optimizer/policy version 在 shared forward、failure retry 和 queue preemption 时如何建立
   transactional snapshot 与 fairness/SLO accounting？
10. OPD² 的 teacher/base lineage delta 能否跨独立训练 recipe 保持意义，还是只在同源 checkpoint family
    中可靠？sign gate 与 top-k centering 各自怎样影响 capability preservation 和长期收敛？
11. RHI 的相邻版本 judge 能否在 held-out regression、独立 executable checks 与 branch/rollback 加入后，
    仍保持每轮低成本？task-specific harness 何时应提升为跨任务共享组件？
12. distributed Muon 如何在保留完整矩阵变换语义的同时兼容 FSDP sharding、optimizer checkpoint、
    elastic restart 与 mixed-optimizer parameter routing？跨 model lineage 时 effective update scale 如何校准？
13. embodiment-free trajectory 的 state-transition auto labels 如何建立抽样 human audit、temporal-boundary
    QA 与 cross-embodiment provenance？哪些控制/安全状态无法由视觉语言描述恢复？
14. DSWorld 的约 14× training-speedup headline 与 Table 2 的 335/277 min 应如何对齐？artifact 恢复后，
    timeout fallback 是否真的取消原执行并完成 authoritative-state reconciliation？
15. SeerGuard 的 semantic next-state prediction 如何用真实 `o_{t+1}` 持续校准？面对不确定、多步延迟风险时，
    何时应 abstain、请求审批或切换到确定性 hard gate，而不是二元拒绝？
16. ESAT 的 per-app simulated history 如何表达跨 app transaction、shared identity 与 eventual consistency？
    write API 仅做 schema validation 时，怎样用 sampled real execution 校准 impossible mutation、duplicate effect 与 rollback？

## Sources

> Access note：本节 expanded arXiv sources 最初于 2026-08-09 完成 identity/abstract discovery；
> 除下文明确列出的 4 个 blocker 外，其余对应正文于 2026-08-13 重新访问并完成全文核验。

### 模型与研究机构

- Kimi Team, “Kimi K3: Open Frontier Intelligence,” first published 2026-07-16; accessed
  2026-07-31:
  https://www.kimi.com/blog/kimi-k3
- Kimi Team, “Introducing PerceptionBench,” published 2026-07-16; accessed 2026-07-31:
  https://www.kimi.com/blog/perception-bench
- Anthropic, “Claude’s values across models and languages,” published 2026-07-13; accessed
  2026-07-31:
  https://www.anthropic.com/research/claude-values-models-languages
- Kimi Research index, accessed 2026-07-31:
  https://www.kimi.com/en/blog/
- Qwen Code Weekly Updates, accessed 2026-07-31:
  https://qwenlm.github.io/qwen-code-docs/en/blog/updates/

### 论文与发现索引

- Wang et al., “Harness Handbook,” submitted 2026-07-14; accessed 2026-07-31:
  https://arxiv.org/abs/2607.13285
- Tang et al., “Ring-Zero,” submitted 2026-07-14; accessed 2026-07-31:
  https://arxiv.org/abs/2607.12395
- Chen et al., “AgentCompass,” submitted 2026-07-15; accessed 2026-07-31:
  https://arxiv.org/abs/2607.13705
- Chen et al., “LightMem-Ego,” submitted 2026-07-13; accessed 2026-08-09:
  https://arxiv.org/abs/2607.11487
- Kong et al., “AdvancedMathBench,” submitted 2026-07-13; accessed 2026-08-09:
  https://arxiv.org/abs/2607.11849
- Fu et al., “Proxy Exploration and Reusable Guidance,” submitted 2026-07-13; accessed 2026-08-09:
  https://arxiv.org/abs/2607.11505
- Choi et al., “Multi-Agent LLMs Fail to Explore Each Other,” submitted 2026-07-13; accessed 2026-08-09:
  https://arxiv.org/abs/2607.11250
- Wang et al., “Function-Aware Fill-in-the-Middle,” submitted 2026-07-14; accessed 2026-08-09:
  https://arxiv.org/abs/2607.12463
- Huang et al., “Read It Back,” submitted 2026-07-13; accessed 2026-08-09:
  https://arxiv.org/abs/2607.11886
- Shi et al., “Are LLMs Ready for Scientific Discovery?,” submitted 2026-07-13; accessed 2026-08-09:
  https://arxiv.org/abs/2607.11079
- Li et al., “KnowAct-GUIClaw,” submitted 2026-07-14; accessed 2026-08-09:
  https://arxiv.org/abs/2607.12625
- Yeh et al., “Tracing Agentic Failure from the Flow of Success,” submitted 2026-07-14; accessed 2026-08-09:
  https://arxiv.org/abs/2607.12747
- Zhang et al., “ShortOPD,” submitted 2026-07-14; accessed 2026-08-09:
  https://arxiv.org/abs/2607.13124
- Cai et al., “PalmClaw,” submitted 2026-07-14; accessed 2026-08-09:
  https://arxiv.org/abs/2607.13027
- Mündler-Sasahara et al., “Generative Compilation,” submitted 2026-07-15; accessed 2026-08-09:
  https://arxiv.org/abs/2607.13921
- Zhou et al., “LongStraw,” submitted 2026-07-16; accessed 2026-08-09:
  https://arxiv.org/abs/2607.14952
- Wu et al., “SEED,” submitted 2026-07-16; accessed 2026-08-09:
  https://arxiv.org/abs/2607.14777
- Zhang et al., “SearchOS-V1,” submitted 2026-07-16; accessed 2026-08-09:
  https://arxiv.org/abs/2607.15257
- Li et al., “BadWAM,” submitted 2026-07-16; accessed 2026-08-09:
  https://arxiv.org/abs/2607.15207
- Li et al., “From Pixels to States,” submitted 2026-07-15; accessed 2026-08-09:
  https://arxiv.org/abs/2607.14076
- Wang et al., “Demystifying On-Policy Distillation,” submitted 2026-07-15; accessed 2026-08-09:
  https://arxiv.org/abs/2607.13399
- Schelpe, “Byte-Exact KV-Cache Grafting,” submitted 2026-07-15; accessed 2026-08-09:
  https://arxiv.org/abs/2607.14431
- Wang et al., “Rethinking the Evaluation of Harness Evolution for Agents,” submitted 2026-07-14;
  accessed 2026-08-09: https://arxiv.org/abs/2607.12227
- “Training Variable Long Sequences with Data-Centric Parallel,” arXiv HTML v1 metadata 2026-07-14;
  full text accessed 2026-08-13: https://arxiv.org/abs/2608.07524
- Xiaomi-Robotics-1: https://arxiv.org/abs/2607.15330
- Xiaomi-Robotics-1 official project page: https://robotics.xiaomi.com/xiaomi-robotics-1.html
- Xiaomi-Robotics-1 official code/artifact: https://github.com/XiaomiRobotics/Xiaomi-Robotics-1
- On-Policy Delta Distillation: https://arxiv.org/abs/2607.15161
- On-Policy Delta Distillation official code: https://github.com/naver-ai/opd2
- Recursive Harness Self-Improvement: https://arxiv.org/abs/2607.15524
- When Does Muon Help Agentic Reinforcement Learning?: https://arxiv.org/abs/2607.16169
- When Does Muon Help Agentic Reinforcement Learning? official code/artifact:
  https://github.com/x66ccff/verl-muon
- DSWorld: https://arxiv.org/abs/2607.15901
- DSWorld v1 full text: https://arxiv.org/html/2607.15901v1
- DSWorld code/artifact（2026-08-12 unavailable）: https://anonymous.4open.science/r/DSWorld
- Beyond Success Rate: Cost-Aware Evaluation of Offensive and Defensive Security Agents:
  https://arxiv.org/abs/2607.15263
- Beyond Success Rate v1 full text: https://arxiv.org/html/2607.15263v1
- Frontier Evals interactive artifact（2026-08-12 unavailable）: https://evals.frontier.security
- SeerGuard: https://arxiv.org/abs/2607.15550
- SeerGuard v1 full text: https://arxiv.org/html/2607.15550v1
- SeerGuard official project: https://seerguard.github.io/
- SeerGuard official evaluation code and benchmarks: https://github.com/Autonomous-Agent-Team/SeerGuard
- SAWM official model weights: https://huggingface.co/xue-26/SAWM
- Environment-free Synthetic Data Generation for API-Calling Agents: https://arxiv.org/abs/2607.16900
- Environment-free API data v1 full paper: https://arxiv.org/pdf/2607.16900v1
- Apple Machine Learning Research page（post-window verification）:
  https://machinelearning.apple.com/research/environment-free
- Distilled Reinforcement Learning for LLM Post-training, full text accessed 2026-08-13:
  https://arxiv.org/abs/2607.17247
- JoyNexus, full text accessed 2026-08-13: https://arxiv.org/abs/2607.16074
- DataFlow-Harness, v1 and current revision read 2026-08-13: https://arxiv.org/abs/2607.16617
- Hugging Face Daily Papers, discovery only, 2026-07-16; accessed 2026-07-31:
  https://huggingface.co/papers/date/2026-07-16
- Google Scholar: https://scholar.google.com/
- Semantic Scholar: https://www.semanticscholar.org/
- OpenAlex: https://openalex.org/
- DBLP: https://dblp.org/

### AI Infra

- Transformers v5.14.1 official release, released 2026-07-16; accessed 2026-07-31:
  https://github.com/huggingface/transformers/releases/tag/v5.14.1
- Ray 2.56.1 official release, released 2026-07-17; accessed 2026-07-31:
  https://github.com/ray-project/ray/releases/tag/ray-2.56.1

## 2026-08-13 Source-Family Books Integration

Xiaomi-Robotics-1 已通过 Source-Family Books Gate：Owner `MULTIMODAL-EMBODIED-VLA`，Current Ch26，Legacy N/A。其 `embodiment-free interaction breadth → derived state-transition labels → embodiment/action alignment → real-robot evidence` 路线融入 `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md`，而 data selection/provenance 的实现 handoff 到 `TRAIN-DATA` / Ch27 / Legacy Ch23。少量 real-robot trials、未披露 hardware/control SLO 和 post-window artifact 边界均保留。Archive Completion Gate 仍 Open。
