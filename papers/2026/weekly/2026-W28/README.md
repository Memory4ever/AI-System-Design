# AI Research Weekly — 2026-W28

> Coverage Window: 2026-07-06～2026-07-12
> Research Mode: Retrospective Backfill
> Accessed: 2026-07-31
> Backfilled: 2026-07-31
> Discovery Review Reopened: 2026-08-09
> Re-audit Status: 30/30 source families have final Books dispositions; 18 Refine, 6 No Change, 2 Weekly Only, 1 Emerging, 3 Unverified / Blocked; 27/30 Full Source Reviews complete under blocked-skip; W28 Source-Family Books Gate passed and cursor advances to W29; broader Archive/Discovery Gate remains Open

## Executive Summary

本周出现四项值得长期跟踪的证据：

1. Anthropic 的 Jacobian Lens / J-space 工作提供了“可读出信息不等于因果机制”的新实验
   工具，并以 intervention 检验可 verbalize representation 是否参与内部推理；
2. DeepSeek 的 DSpark 把 speculative decoding 的 verify length 从固定超参数提升为由 prefix
   survival probability 与 engine throughput profile 共同决定的在线资源决策；
3. Anthropic 的 GRAM 尝试把 dual-use knowledge 在训练期路由到可移除 modules，但仍是
   5B 以下、未进入生产的 preliminary research；
4. PyTorch 2.13 将 communication、compiler backend、loss fusion 与 FSDP overlap 同时推进，
   说明 framework 的稳定边界正在从 tensor API 延伸到 distributed/system contracts。

其中 J-space、DSpark 与 PyTorch 2.13 进入深入分析；GRAM 保留为 Emerging，不因机构来源
可靠就把实验性方法写成已解决的 capability access control。

2026-08-09 的 discovery replay 进一步恢复了 15 个原 Weekly 静默遗漏的候选。新增信号并不只是
“更多论文”：KVpop、linear-attention comparison 与 Sparse Delta Memory 补齐状态容量/访问策略的
演进；LLM-as-a-Verifier、AgentLens 与 UniClawBench 把 Agent evaluation 从最终分数推进到
trajectory、criterion、environment 与 verifier budget；asynchronous agentic RL 与 proactive memory
则暴露了 staleness、intervention timing 和 behavioral-state ownership。2026-08-13 exact-source retry
已把原 14 个 blocked scored families 中的 11 个恢复为完整 Source Review；只有 AgentLens、UP 与
Ideas Have Genomes 仍因正文不可访问进入 explicit backlog。

cross-week attribution review 还纠正了一个结构性漏项：W29/W30 已明确把 ABot-AgentOS、GRASP、
Weak-to-Strong Direct OPD、What LLM Forecasters Know、PolicyShiftGuard、Root Causes 与
DeepSearch-World 按 arXiv v1 回拨 W28，但这些 family 之前没有真正进入 W28。本轮已恢复七篇正文、
完成六维评分和完整章节审计；它们不再是 unscored identities。ReflectWorld-MM 与 ReOPD 也已完成全文、
实现/评测边界与相邻章节审计。ReflectWorld-MM 的六项 benchmark headline 保留 mixed-provenance、judge
revision 与 answer-time ablation 边界，不写成通用 memory superiority。

## Coverage Window and Limitations

- 机构 Research、arXiv 首版时间与 GitHub release time 分别核验；Hugging Face 推荐日不作为
  论文发布日期。
- Anthropic J-space 论文公开了全文、方法代码与模型实验，但核心实验集中在 Claude 系列；
  对其他架构和模型家族的普适性仍有限。
- DSpark 的生产结果是作者对 DeepSeek-V4 serving 的报告；缺失的 traffic、并发、硬件、
  输入输出长度、精度与 SLO 条件均不自行补齐。
- PyTorch release notes 中的 “up to” 性能数字只视为版本说明，不升级为通用 benchmark。
- Hugging Face 2026-W28 展示页只用于 recall；每项论文按 arXiv v1 归周。Gemma 4、Embodied.cpp、
  OrbitQuant、ResearchStudio、Wan-Streamer 等展示于本周但 v1 属于 W26/W27，作为 spillback
  交叉核验而不错误记入 W28。

## Discovery Recall Ledger

| Ledger Item | Current Count | Review Result |
| --- | ---: | --- |
| Score rows / candidate families | 30 / 30 | 19 个 `25+`、10 个 `20–24`、1 个低分；7 个 spillbacks 已正式评分 |
| Full Source Reviews | 27 / 30 | 原 9 项 + 11 scored recoveries + 7 spillback reviews；均含相邻章节与 disposition |
| Unverified / Blocked Backlog | 3 | AgentLens、UP、Ideas Have Genomes；0 ordinary pending |
| Academic discovery window | Replayed with spillback repair | 2026-07-06～07-12 按 arXiv v1 去重；later-week attribution rows 已回写 owner week 并完成审计 |
| W28 forward Candidate Gate | Passed with explicit blocked ledger | 27/30 Full Source Reviews；3 blocked；0 ordinary pending；cursor remains W29 |
| W28 discovery / Historical Evidence Gate | Open | 3 blocked families 与更广 citation/venue discovery 未闭合；fixed official/Infra checkpoint 已通过 |

## 1. 模型与研究机构

### Source Coverage

按固定顺序扫描：

| Order | Sources | Result |
| --- | --- | --- |
| 1–5 | OpenAI；Anthropic；Apple ML Research；Google DeepMind；Google Research | Anthropic J-space（7 月 6 日）与 GRAM（7 月 8 日）达到保留门槛；Google Research 其余垂直领域内容 Record Only |
| 6–14 | Meta AI / FAIR；Microsoft Research；NVIDIA Research；xAI；Amazon Science；Cohere Labs；Ai2；Mistral AI；Alibaba Qwen | 无改变本项目核心结论的模型研究；Qwen Code 7 月 9 日周更为产品迭代 |
| 15–25 | DeepSeek；Moonshot / Kimi；Zhipu；MiniMax；ByteDance Seed；Baidu ERNIE；Tencent Hunyuan；Huawei Noah；Shanghai AI Lab / InternLM；StepFun；Xiaomi MiMo | DeepSeek DSpark 以 arXiv primary 进入论文组；其余无可核验高门槛官方更新 |
| 26–27 | InclusionAI / Ant Group；Hugging Face Blog | 无独立高门槛模型研究 |
| Weekly | LG AI Research；Sakana AI；01.AI；Baichuan；ModelBest；BAAI；Salesforce；IBM；Databricks / Mosaic | 未发现本窗口内需深入分析的发布 |

### Candidate Scoring

| Candidate | Technical Novelty | System Impact | Practical Value | Source Reliability | Project Relevance | Longevity | Total | Decision |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| Anthropic J-space / Jacobian Lens | 5 | 4 | 3 | 5 | 5 | 5 | 27/30 | Must Read；已归并 Weekly；Books 已评估 |
| Anthropic GRAM | 5 | 4 | 3 | 4 | 4 | 5 | 25/30 | Must Read；Status: Emerging |

### Deep Analysis 1 — J-space：从 Readout 走向 Causal Intervention

- Published / First Public Version: 2026-07-06
- Status: Experimental
- Primary Sources:
  - https://transformer-circuits.pub/2026/workspace/index.html
  - https://github.com/anthropics/jacobian-lens

#### Why

传统 logit lens、linear probe 或 feature labeling 能说明 activation 中“可以读出什么”，却
不能证明模型实际使用了该表示。可解释性若停在 correlation，会把旁观者 scoreboard 误认成
决策机制。

#### Principle

对 layer `l` 的 residual activation `h_l`，J-lens 用跨 context 平均的 Jacobian 近似其对当前
及后续 final residual 的一阶影响：

```text
J_l = E[d h_final,t' / d h_l,t]
lens(h_l) = softmax(W_U norm(J_l h_l))
```

它不是直接假设所有层共享 final unembedding coordinates，而是显式近似 layer-to-output 的
局部映射。真正的机制证据还需要 activation swap、ablation 或 steering 后行为随之改变。

#### Mechanism

作者把与可 verbalize tokens 对应的 J-lens vectors 看作一个稀疏 subframe，并把稀疏非负组合
定义为 J-space。实验分别检查 reportability、directed modulation、internal reasoning、
flexible reuse 与 selectivity；其中 swapping 或 ablating J-space directions 用来区分“可读”
与“被使用”。

#### Trade-off

Jacobian 是局部一阶近似；跨 prompt averaging 会丢失 context-specific nonlinear structure；
token-indexed vectors 对 multi-token concepts 不完整；J-space 的 sparsity threshold 也包含
研究者选择。Claude 上的因果效应不能自动推广到所有 Transformer，更不能推出模型具有
phenomenal consciousness。

#### Connection

知识树位置：第 5 章神经网络学到什么 → 第 8 章 LLM intelligence → 第 10 章 AI future /
safety。它最可能 refine 第 5 章的 evidence ladder：behavior → decodability → intervention
→ mechanism，而不是新增“AI consciousness”孤立章节。

#### Evolution

从 logit lens、trained probe、SAE feature，到 Jacobian-adjusted lens 与 causal patching，
演化方向是让解释工具逐渐回答“表示是否影响 computation”。后续需要 open-weight replication、
non-verbal concepts 与 nonlinear interventions。

### GRAM — Worth Watching

GRAM 在每层增加按 dual-use category 划分的 auxiliary neurons；一般数据正常更新，命中敏感
类别时冻结 shared weights，只让对应 module 学习。module 删除后可移除相应能力，四类 module
理论上提供 `2^4` 种部署组合。

官方明确说明：

- 结果是 preliminary；
- 最大实验规模为 5B，而非 frontier scale；
- 未用于任何 Claude production model；
- 评估主要是 next-token prediction，不是实际 downstream harmful capability；
- dual-use knowledge 可能与 general knowledge 无法干净分离。

因此其长期价值是提出“training-time capability compartment”这一设计方向，不是证明模型
知识已经可以可靠 ACL 化。Books 暂不写入，等待独立复现或生产级 capability evaluation。

## 2. 论文与学术来源

### Candidate Scoring

| Candidate | Technical Novelty | System Impact | Practical Value | Source Reliability | Project Relevance | Longevity | Total | Decision |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| DSpark | 5 | 5 | 4 | 3 | 5 | 5 | 27/30 | Must Read；已归并 Weekly；Books 已评估 |
| Length Penalties Make CoT Less Monitorable | 4 | 3 | 3 | 3 | 4 | 5 | 22/30 | Worth Watching；Weekly only |
| KVpop | 5 | 5 | 4 | 4 | 4 | 4 | 26/30 | Refine Ch41 / Experimental；review complete |
| LLM-as-a-Verifier | 5 | 4 | 4 | 4 | 5 | 5 | 27/30 | Full Source Review complete；No Change — Existing Evaluation contract |
| Multi-Turn On-Policy Distillation with Prefix Replay（ReOPD） | 5 | 5 | 5 | 4 | 5 | 5 | 29/30 | Full Source Review complete；Refine `TRAIN-SFT` |
| ReflectWorld-MM | 5 | 5 | 4 | 4 | 5 | 5 | 28/30 | Full Source Review complete；Refine `AGENT-MEMORY` |
| AgentLens | 3 | 4 | 4 | 3 | 5 | 5 | 24/30 | Unverified / Blocked Backlog — score provisional |
| Single-Rollout Asynchronous Optimization | 5 | 5 | 4 | 3 | 4 | 4 | 25/30 | Refine Ch29 / Experimental；review complete |
| Linear Attention Architectures | 5 | 5 | 4 | 4 | 5 | 4 | 27/30 | Refine Ch22 / Experimental；review complete |
| Sparse Delta Memory | 5 | 4 | 3 | 4 | 5 | 4 | 25/30 | Refine Ch22 / Experimental；review complete |
| UP: Unbounded Positive Asymmetric Optimization | 4 | 4 | 4 | 3 | 5 | 4 | 24/30 | Unverified / Blocked Backlog — score provisional |
| Remember When It Matters | 5 | 4 | 4 | 3 | 5 | 5 | 26/30 | Refine Ch73 / Experimental；review complete |
| RynnWorld-4D | 4 | 3 | 3 | 3 | 4 | 4 | 21/30 | Refine Ch10 / Experimental；review complete |
| AlayaWorld | 4 | 3 | 4 | 3 | 4 | 4 | 22/30 | Refine Ch10 / Experimental；review complete |
| Dual Latent Memory VLA | 4 | 3 | 3 | 3 | 4 | 4 | 21/30 | Refine Ch73 / Experimental；review complete |
| Vision as Unified Multimodal Generation | 4 | 4 | 3 | 3 | 4 | 5 | 23/30 | Refine Ch18 / Experimental；review complete |
| Infinite Worlds with Versatile Interactions | 4 | 3 | 3 | 3 | 4 | 4 | 21/30 | No Change Ch10；review complete |
| Ideas Have Genomes | 3 | 3 | 4 | 3 | 4 | 5 | 22/30 | Unverified / Blocked Backlog — score provisional |
| UniClawBench | 4 | 4 | 4 | 3 | 5 | 4 | 24/30 | No Change Ch62；review complete |
| HiLS-Attention | — | — | — | — | — | — | Deduplicated | 首版 7 月 3 日，归 W27 |
| ABot-AgentOS | 5 | 5 | 4 | 3 | 5 | 5 | 27/30 | Refine Ch80 / Experimental；review complete |
| GRASP | 5 | 4 | 5 | 3 | 5 | 5 | 27/30 | No Change Ch72；review complete |
| Weak-to-Strong Direct OPD | 5 | 5 | 5 | 4 | 5 | 5 | 29/30 | Refine Ch29 / Experimental；review complete |
| What LLM Forecasters Know but Don’t Say | 4 | 4 | 4 | 4 | 5 | 5 | 26/30 | No Change Ch5/68；review complete |
| PolicyShiftGuard | 4 | 5 | 5 | 4 | 5 | 3 | 26/30 | No Change Ch68；review complete |
| From Noisy Traces to Root Causes / STRACE | 5 | 5 | 4 | 3 | 5 | 5 | 27/30 | Refine Ch65 / Experimental；review complete |
| DeepSearch-World | 5 | 5 | 4 | 3 | 5 | 5 | 27/30 | Refine Ch77 / Experimental；review complete |

### Deep Analysis 2 — DSpark：Verify Window 是 Batch-Capacity 决策

- Submitted / First Public Version: 2026-07-06 14:28:06 UTC
- Status: Experimental
- Primary Source: https://arxiv.org/abs/2607.05147

#### Why

Parallel drafter 可以一次提出更长 token block，但 suffix token 的 acceptance probability 会
快速衰减。固定 verify length 把低存活概率 tokens 也塞进 target batch，在高并发下占用本可
服务其他请求的 verification capacity。

#### Principle

Speculative decoding 的目标不是最大化单请求 draft length，而是在 exactness 不变的前提下，
最大化 SLO 约束下的 accepted tokens per unit target capacity。verify depth 应同时取决于：

```text
expected prefix survival
× accepted-token value
- engine-specific verification opportunity cost
```

#### Mechanism

DSpark 用 semi-autoregressive drafter 在 parallel backbone 后加入轻量 sequential dependency，
缓解 block suffix quality decay；再根据每个请求的 prefix survival probabilities 与当前
engine throughput profile 动态选择 verify length。

#### Trade-off

更好的 draft dependency 与动态 window 会增加训练、校准和 runtime policy 复杂度。confidence
miscalibration、traffic shift 或 batch scheduler 变化都可能让旧 profile 失效。作者报告在
DeepSeek-V4 live traffic、相对 MTP-1 且 matched throughput 时 per-user generation speed
提高 60%～85%；未披露的模型变体、硬件、输入输出、并发、精度和 SLO 条件使该数字不能
外推。

#### Connection

知识树位置：第 44 章 speculative decoding → 第 42 章 continuous batching → 第 52 章
inference scheduling。它补充“speculation policy 与 global batch capacity 耦合”，不是只在
第 44 章比较 drafter architectures。

#### Evolution

从固定 `k`、tree drafting、parallel drafting，到 confidence- 和 load-aware verification，
演化方向是把 speculative decoding 从模型局部技巧变成 scheduler-visible resource policy。
SGLang v0.5.16 的 DSpark integration 将在 W30 作为实现证据交叉检查。

### Length Penalty 与 Monitorability

该预印本首版为 7 月 8 日，作者在 Qwen3-4B/14B 与五个 evaluation distributions 上观察到：
缩短 CoT 可保留多数答案准确率，却降低 reasoning trace 对 biasing hint influence 的暴露。
其长期提醒是“reasoning cost、answer accuracy 与 monitorability 是三个目标”，但单作者
预印本和特定实验不足以改写核心安全结论，保留 `Status: Experimental`。

## 3. AI Infra 与工程项目

### Candidate Scoring

| Candidate | Technical Novelty | System Impact | Practical Value | Source Reliability | Project Relevance | Longevity | Total | Decision |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| PyTorch 2.13 | 4 | 5 | 5 | 5 | 5 | 4 | 28/30 | Must Read；已归并 Weekly；Books 已评估 |
| Qwen Code 7 月 9 日周更 | 2 | 2 | 3 | 4 | 3 | 2 | 16/30 | Record Only |

### Source Coverage

按 PyTorch → JAX → CUDA → Triton → vLLM → SGLang → NVIDIA Dynamo → TensorRT-LLM
→ Ray → KServe → Kubeflow → Kubernetes → Transformers → Accelerate → DeepSpeed
→ Megatron-LM → Unsloth → MLX → llama.cpp → ONNX Runtime → OpenXLA 的顺序扫描。
本周只有 PyTorch 2.13 达到深入分析门槛。

### Deep Analysis 3 — PyTorch 2.13：Framework 开始显式拥有系统边界

- Released: 2026-07-08 17:39（GitHub rendered page）
- Status: Stable release；个别功能仍标记 Prototype / opt-in
- Primary Source: https://github.com/pytorch/pytorch/releases/tag/v2.13.0

#### Why

大模型训练瓶颈已不只在 eager tensor operator：collective failure、compiler backend、
loss materialization 和 communication overlap 都会决定 job 是否能扩展。若 framework 只
提供张量 API，这些职责会分散在外部 glue code 中，难以统一调试和演进。

#### Principle

Framework 的抽象边界随瓶颈下沉：把 communication、graph lowering、memory-saving fused
loss 与 sharding overlap 变成可组合 contracts，同时保留 backend 与 process-group 的替换性。

#### Mechanism

- `torchcomms` 作为新的 PyTorch Distributed communication backend，强调 fault tolerance、
  scalability 与 debuggability；
- FSDP2 可选择用 dedicated process group overlap reduce-scatter 与 all-gather；
- Inductor 加入 CuTeDSL Native DSL backend，但 release 明确标记为 Prototype；
- `nn.LinearCrossEntropyLoss` 融合 final projection/loss，避免完整 logits materialization。

#### Trade-off

更统一的 framework contract 改善组合与观测，却扩大兼容矩阵和升级面。new backend 不等于
自动优于 NCCL/UCC；FSDP overlap 需要额外 process group 与资源；fusion 会限制算子边界；
Prototype compiler backend 不能按 stable contract 书写。release 的 “up to 4x/12x” 数字缺少
本项目要求的完整 workload 条件，不作为通用结论。

#### Connection

知识树位置：第 31～36 章 distributed training/communication → 第 37 章 training framework
→ 第 53～55 章 compiler/kernel。现有第 32 章应继续以 collective semantics → algorithm/runtime
→ transport → topology 为主，不把 torchcomms 写成取代 MPI/NCCL/UCC 的新一层。

#### Evolution

从 framework 调用外部 collective library，到 framework 拥有 debuggability、failure handling
与 overlap orchestration，演化的是 control/observability boundary，不是 collective 数学。

## Evidence Level

| Claim | Evidence | Boundary |
| --- | --- | --- |
| J-space 具备可干预的 workspace-like properties | Anthropic full paper + code | `Status: Experimental`，主要为 Claude |
| GRAM 可按 module 移除能力 | Anthropic/AE Studio 实验 | `Status: Emerging`，≤5B、非生产 |
| DSpark 动态选择 verify length | arXiv v1，作者生产实验 | `Status: Experimental` |
| LLM-as-a-Verifier 的三条 scaling axes | arXiv v2 全文、四个 benchmark 与 appendix | 作者实验；依赖 judge/logprob/rubric contract |
| 新恢复及回拨候选 | 24 个 primary-text Full Source Reviews + 3 explicit blocked identities | 可访问者已审计；blocked 不推断机制 |
| PyTorch 2.13 新增上述系统能力 | Official stable release | 版本事实；Prototype/opt-in 单列 |

## Cross-Week Deduplication

- HiLS 虽在 Hugging Face 7 月 8 日页面出现，但 arXiv 首版为 7 月 3 日，已归 W27。
- Google DeepMind overthinking 的 7 月 2 日正式发表状态已在 W27 记录。
- Length Penalties 的 v2 为 7 月 17 日，主归属仍按 v1 的 7 月 8 日。
- MIPI、Gemma 4、Embodied.cpp、OrbitQuant、ResearchStudio、Wan-Streamer、PraMem 与 Safety
  Testing Agents 虽在 W28 展示页出现，v1 分别落在 W26/W27，回填到其 owner week 的 spillback
  队列；GORGO 的 v1 属于 W07，7 月 revision 不重记新事件。
- ABot-AgentOS（2607.10350）与 GRASP（2607.10463）的 v1 均为 2026-07-11；W29 的 7 月 15/17
  display/revision 不构成新事件。DeepSearch-World（2607.07820）v1 为 2026-07-08；W30 的 7 月 21
  Daily Papers display 只是 discovery lag。
- Weak-to-Strong Direct OPD（2607.05394）、What LLM Forecasters Know（2607.08046）、
  PolicyShiftGuard（2607.05910）与 Root Causes（2607.07702）已由 W29 attribution ledger 确认归 W28；
  七个 later-week attribution identities 已按 arXiv v1 精确日核对并完成评分，revision 不移动 owner week。
- ReOPD（2607.04763）v1 为 7 月 6 日；后续 code release 不创建 W30 新事件。它与普通 offline SFT、
  online OPD 和 RL 是不同训练分支，不按名称合并。

## Knowledge Tree Position

| Candidate | ROADMAP Node | Role |
| --- | --- | --- |
| J-space | Ch5 → Ch8 → Ch10 | interpretability evidence ladder |
| GRAM | Ch23/24 → Ch68 | training-time knowledge compartment and safety |
| DSpark | Ch44 → Ch42 → Ch52 | speculation as capacity-aware policy |
| KVpop / Sparse Delta Memory / linear-attention comparison | Ch15 → Ch41/43 → Ch50 | state capacity、access selection 与 hybrid coexistence |
| LLM-as-a-Verifier / AgentLens / UniClawBench | Ch62 → Ch76 → Ch80 | verifier contract、trajectory evidence 与 environment identity |
| Asynchronous agentic RL / UP | Ch27～29 → Ch34/37 | rollout staleness、policy update 与 stability budget |
| Proactive memory | Ch73 → Ch76/80 | intervention timing 与 behavioral-state ownership |
| World-model / VLA families | Ch18/19 → Ch70/71 | multimodal state、world prediction 与 embodied execution |
| PyTorch 2.13 | Ch32 → Ch37 → Ch53 | framework/system boundary |
| ABot-AgentOS / GRASP / DeepSearch-World | Ch80 / Ch72 / Ch77 | runtime、granularity-aware retrieval 与 verifiable search world |
| Weak-to-Strong Direct OPD / Forecasters / PolicyShiftGuard / Root Causes | Ch29 / Ch5+68 / Ch68 / Ch65 | behavioral shift、probe sensor、policy data 与 trace diagnosis |
| ReOPD | Ch29 → Ch77/80 | replayed-prefix distillation、trajectory provenance 与 environment decoupling |
| ReflectWorld-MM | Ch73 → Ch70/72/74/80 | entity-resolved perception、hierarchical memory 与 identity-critical commit ownership |

## Recommended Action

- J-space、DSpark、PyTorch 2.13 与 GRAM 的既有正文经 source packet 和相邻章节复读后保留；没有复制
  release feature list 或 benchmark headline。
- 新增的长期机制集中为 teacher-prefix replay 的双重 distribution-shift、entity-resolved longitudinal
  memory、trace dependency graph 到 root-cause candidate，以及 deterministic offline world 到 live canary
  的 promotion boundary。
- LLM-as-a-Verifier、Infinite Worlds、UniClawBench、GRASP、Forecasters 与 PolicyShiftGuard 均由现有具体
  论点覆盖；Length Penalty 与 Qwen Code 保留 Weekly。AgentLens、UP、Ideas Have Genomes 继续 blocked-skip，
  不获得 Books 机制 owner。

## Event-Date Daily Decision

| Date | Decision | Reason |
| --- | --- | --- |
| 2026-07-06 | Retired after Weekly integration | 两个高信号候选及 Books 决策已完整归并 W28 |
| 2026-07-08 | Retired after Weekly integration | GRAM、CoT monitorability 与 PyTorch 证据已完整归并 W28 |
| 2026-07-09 | Do not create | 机构与产品更新未超过已有候选 |

## Books Integration Decision

`Source-Family Books Gate Passed under Blocked-skip — Archive Completion Gate Open`。30 个 family 均有最终
disposition；27 项全文审计，3 项明确 blocked。实际新增正文位于 `TRAIN-SFT`、`AGENT-MEMORY`、
`PLATFORM-TRACE` 与 `AGENT-WORKFLOW`。J-space、DSpark、PyTorch 2.13、GRAM、KV/linear-attention 与其他
Refine family 已由当前章节的完整演进链覆盖并经复核保留。Blocked family、单篇 monitorability 结论和产品周更
没有进入长期机制正文。

## Ignored Noise

- 将 J-space 解释为模型具有主观意识的媒体化结论；
- 将 GRAM 写成已经解决 jailbreak 或 capability removal；
- 不绑定环境复述 DSpark、FlexAttention 或 fused loss 的 “up to” 数字；
- Qwen Code UI/命令更新和普通 patch PR。

## 2026-07-31 Full Re-Audit Addendum

- J-space 全文复核后确认 Ch5 的 local Jacobian/evidence ladder 与限制边界正确，无重复扩写。
- GRAM 全文复核后以 `Status: Experimental` 写入 Ch68；它是训练时 capability isolation
  分支，不替代 output-time policy。
- DSpark 全文复核确认 Ch44/52 的 adaptive verification depth；PyTorch 2.13 只抽取
  communication backend contract 写入 Ch32，不复制版本功能表。
- Length Penalties 保留 Weekly only。

## Full Source Review

### Anthropic J-space / Jacobian Lens — 27/30

- **Source Family ID / Type / Date**：`JSPACE-JACOBIAN-LENS`；Anthropic 2026-07-06 report、
  transformer-circuits full paper、code、open-model demo 与 external commentary/replication。
- **Full-read Coverage**：已覆盖 Jacobian lens construction、verbalizability、report/control/reasoning/
  flexibility experiments、causal swaps/ablation、alignment audits、counterfactual reflection training、
  base/post-training comparison、discussion 与 limitations。
- **Problem / Previous Design / Changed Constraint**：output/CoT 易观察但遗漏 silent state；SAE/NLA 可解释
  feature/activation，却未直接寻找“可被未来语言读出”的低维通道。
- **Mechanism / Ownership / Flow**：J-lens 用 output Jacobian 找提高未来词概率的内部 direction；J-space
  readout 显示候选 verbalizable concepts；swap/ablation 干预该 direction 并测 downstream behavior。
  probe owner 只拥有 approximate measurement，model activation 是被测状态，safety decision 仍需外部 eval。
- **Evidence Boundary**：Claude experiments 支持一组 representations 具有 reportability、controllability、
  flexible causal mediation；open-model replication 增强外部性。它不证明完整读取“thought”、所有模型共享
  同一 workspace、phenomenal consciousness 或 probe 不受 tokenizer/single-token 限制。
- **Trade-offs / Evolution**：readout 可用于监控/调试，但 selection bias、probe incompleteness、intervention
  side effects 和 gaming 仍在；behavioral eval 与其他 interpretability methods继续共存。关系为
  `Layering / Dependency` 于 evidence ladder。
- **ROADMAP / Decision**：Ch5 主 owner，已读 Ch4～6、Ch27、Ch62、Ch68；Ch5 已准确覆盖 local
  Jacobian→causal intervention→replication。`No Change — Already Covered`。

### Anthropic GRAM — 25/30

- **Source Family / Full-read Coverage**：`GRAM-CAPABILITY-ISOLATION`；Anthropic 2026-07-08 report、
  linked paper/code；已读 modular training/isolation、removal experiment、capability/safety evaluation、
  ablation 和 limitations。
- **Mechanism / Evidence Boundary**：将特定 dual-use capability 更集中地路由到可移除 module，试图在
  training-time 创建 off-switch；作者实验只证明给定 architecture/data/task 的 capability suppression，
  不证明 shared weights 无残留、无法重学/重建或替代 output/runtime policy。
- **Trade-offs / Evolution**：比 output filter 更早隔离 capability，但增加 module routing、quality spillover、
  capability taxonomy、audit/removal verification 和 retraining bypass。与 policy 是 `Layering`，非替代。
- **ROADMAP / Decision**：Ch68 主 owner，已读 Ch27、Ch67～69；`Refine — Existing Argument` 已以
  `Status: Experimental` 写入 Ch68；保留 provisional 内容。

### DSpark — 27/30

- **Source Family ID / Type / Date**：`DSPARK-ADAPTIVE-SPECULATION`；arXiv:2607.05147v1，
  first-public 2026-07-06；论文与 artifact 联读。
- **Full-read Coverage**：已覆盖 semi-autoregressive proposal、confidence scheduling、verify-window、
  correctness、implementation、models/hardware/workloads、baseline、ablation/sensitivity/overhead、limitations。
- **Problem / Mechanism**：固定 draft length 简单且适合稳定 acceptance；token confidence 波动使固定窗口
  在易处少推进、难处多浪费。DSpark 按 confidence 动态决定并行 proposal/verification depth，target
  model 保持 authoritative acceptance，scheduler 需看到 variable compute/KV rollback。
- **Evidence Boundary / Trade-off**：作者实验支持其 model/hardware/decoding settings 的 speedup；不证明
  confidence 跨模型/版本 calibrated、multi-tenant batch/fairness 或 tail SLO。自适应窗口获得接受率/并行度，
  新增 calibration drift、batch fragmentation、rollback state 和 decision trace。
- **ROADMAP / Decision**：Ch44 主 owner、Ch52 handoff，已读 Ch43～45、Ch51～52；现有正文已覆盖。
  `No Change — Already Covered`，保留 Ch44/52 provisional 内容。

### Length Penalties Make CoT Less Monitorable — 22/30

- **Source Family / History / Coverage**：`COT-LENGTH-MONITORABILITY`；arXiv:2607.09786v1，
  first-public 2026-07-08；PDF 全文的 training objective、monitorability metrics、experiments、ablation、
  limitations 已核对（HTML 不可用）。
- **Evidence / Decision**：作者实验支持某些 length pressure 下可观察 reasoning trace 减少/改变，不证明
  hidden reasoning 必然增加或所有 concise training 不安全。Ch8/27/62/68 已读；
  `Emerging / Experimental`，不写 Books。

### PyTorch 2.13 — 28/30

- **Source Family ID / Type / Date**：`PYTORCH-2.13-COMMS`；GitHub v2.13.0 release
  2026-07-08、RELEASE cadence、torchcomms/ProcessGroup documentation、RFC/PR/code paths。
- **Full-read Coverage**：已核对 communication backend lifecycle、API/ownership、collective semantics、
  failure/timeout/cancellation、compatibility/deprecation 与 release notes；其他 feature 不作为本书机制。
- **Problem / Mechanism**：历史 ProcessGroup 把 collective 和 framework execution 强耦合，对训练图方便；
  serving/independent communication workload 需要更明确的 communicator、memory/stream、lifecycle 和
  backend boundary。torchcomms signal 是 framework 将通信责任独立化，不是 NCCL/UCC 的替代。
- **Evidence Boundary / Trade-off**：release/code 证明 2.13 behavior；未来 API 可变。抽象提高 backend
  portability/ownership clarity，增加 compatibility surface、semantic mismatch 和 failure translation。
- **ROADMAP / Decision**：Ch32 主 owner，已读 Ch31～35、Ch57～59；`Refine — Existing Argument` 已
  写入 communication backend contract；保留 provisional 内容，不复制 feature list。

### Qwen Code 7 月 9 日周更 — 16/30

- **Source / Verification**：官方 weekly update 日期和功能状态已核对；无 architecture/runtime mechanism
  或独立 evidence。
- **Score / Decision**：16/30 维持；`Weekly Only — Version/Product Fact`。

### LLM-as-a-Verifier — 27/30

- **Source Family ID / Type / History**：`LLM-AS-VERIFIER-SCALING`；arXiv:2607.05391v1
  first-public 2026-07-06，v2 2026-07-07；论文、HTML appendix 与公开 code link 联读。
- **Full-read Coverage**：已覆盖 Introduction/Related Work、MDP 与 trajectory 定义、score-token
  expectation、Bradley–Terry preference、Probabilistic Pivot Tournament、granularity/repetition/
  criterion ablations、Terminal-Bench V2/SWE-Bench/RoboRewardBench/MedAgentBench、progress proxy、
  SAC/GRPO dense reward、harness generalization、budget analysis、case study、limitations 与 RL appendix。
- **Original Problem / Previous Design / Changed Constraint**：discrete LLM judge 简单、便宜，适合
  单答案；长 trajectory 与多候选搜索带来 ties、position bias、compound-rubric bias 和 selector budget。
  当生成侧存在较大 oracle `pass@N` headroom 时，系统瓶颈从“再采样”转向“能否可靠选中”。
- **Mechanism / State Ownership / Flow**：verifier 对有序 score tokens 的 log-probability distribution
  求期望，并对 criterion 与 repeated evaluations 平均；pairwise score 进入 Bradley–Terry probability。
  ring pass 让候选各占一次 A/B position，top-k pivots 再与其余候选比较，将全量 `O(N^2)` 降为
  `O(Nk)`。verifier 拥有 probabilistic judgment，不拥有 environment truth；task harness/executable grader
  仍拥有 outcome contract。
- **Evaluation Contract**：scaling experiment 使用 Gemini 2.5 Flash、Terminal-Bench 200 trajectory
  pairs；主表分别固定 Capy/mini-swe-agent 等 harness 与候选池。论文报告 granularity、repetition、criteria
  decomposition 均改善 pairwise accuracy，并在四个 benchmark 上提高 best-of-N selection。RL appendix
  固定 baseline hyperparameters：LIBERO DSRL-SAC 5 seeds/1.5M steps；MATH 上 Qwen3-8B、group size 16、
  64 groups/batch、max 512 tokens、`beta=0.1`。这些是作者实验，不是通用 verifier SLA。
- **What It Proves / Does Not Prove**：证据支持在给定 verifier、rubric、candidate pools 与 harness 下，
  连续概率分数和预算化重复评估比 coarse discrete judge 更能区分候选；不证明“LLM verifier 等同
  ground truth”、chronological score correlation 能检测所有失败、或跨模型/领域自动校准。
- **Trade-offs / Failure Modes**：获得更细 signal 和可调 budget，付出额外 model calls、latency、
  logprob availability、criterion design 与 correlated-bias 风险。PPT 可能在早期 ring pass 错过真正强
  candidate；将同一 verifier 同时用于 ranking、monitoring 与 RL reward 会放大 reward hacking。
- **Evolution / ROADMAP / Adjacent Chapters**：关系是 `Layering / Dependency`：executable outcome
  verifier 不被取代，model verifier 位于其前的筛选/诊断层。已读 Ch61～63、Ch76、Ch80；Ch62 已明确
  覆盖 scorer hierarchy、criteria/ranking 分层、trajectory claim 与 verifier audit，故 provisional
  disposition 为 `No Change — Already Covered`；现有 scorer hierarchy 已经具体承载该结论。

### Multi-Turn On-Policy Distillation with Prefix Replay（ReOPD）— 29/30

- **Source Family / History / Coverage**：`REOPD-PREFIX-REPLAY`；arXiv:2607.04763v1，first-public
  2026-07-06；已读 Abstract、Introduction/Related Work、完整 formulation 与 proof、Algorithm 1、
  math/search/multi-environment experiments、baselines、schedule/prefix-source/pool ablations、efficiency、
  Limitations；并核对 official project、repository、data/training scripts 与 artifact contract。
- **Original Problem / Why Previous Designs Were Reasonable**：offline teacher-trace SFT 便宜且稳定，但
  student inference 会离开 teacher prefixes；fully online OPD 在 student 自己会访问的 histories 上提供
  dense teacher conditionals，却要求每次 update 重新执行 environment 与 teacher queries。两者分别优先
  reuse 与 student occupancy，在单轮或环境便宜时都合理；multi-turn tool environment 才放大成本与
  compounding shift。
- **Changed Constraint / Mechanism**：ReOPD 重放 teacher trajectory 的完整 prefix 与 observations，只让
  student 在被监督的当前 step 自己生成 action，再以 teacher per-token conditional 做 KL target；environment
  不在线执行。作者把理想 interactive objective 与 replay objective 的 gap 分解为 student-occupancy mismatch
  和 teacher-reliability error，并用 `p_t ∝ κ^t` 的 step-decay sampling 偏向早期、低 shift prefixes。
- **State Ownership / Data and Control Flow**：teacher RL run / artifact store 拥有带 observation 的 versioned
  prefix pool；student rollout policy 只拥有当前 step action；teacher service 拥有 conditional target；trainer
  拥有 sampling schedule、loss 与 weight update；environment 在 student distillation loop 中不拥有 live
  state。数据流为 `teacher RL trajectories → prefix pool → sampled (trajectory, step) → student action →
  teacher token distribution → KL update`。这不是 complete student rollout，也不是 reward-weighted RL。
- **Implementation / Evaluation Contract**：Qwen3 family teacher/student；math 使用 6.4K DAPO prompts 与
  Python tool，search 使用 6.5K NQ/HotpotQA prompts、2018 Wikipedia、E5 top-3；均先有 2K cold-start
  trajectories。OPD/ReOPD 使用相同 batch、200 steps、LR 1e-6，默认 `κ=0.6`；evaluation 覆盖六个 math
  与七个 QA benchmarks。公开 repo 说明 one-step replay、prefix-pool construction 和 math/search artifacts。
- **What Evidence Proves / Does Not Prove**：在上述 contract 中，ReOPD 对 math 平均值高于 OPD、search
  基本持平，并在 student training 中不调用 tool；early-step、decay、prefix-source 和 mixed-checkpoint-pool
  experiments 支持 reliability-aware prefix selection。它不证明 4–9× 对所有 environment/hardware 成立，
  不证明 step index 是精确 reliability estimator，也不证明 teacher-pool coverage 足够覆盖 deployment
  histories；`mixed pool ≈ stationary pool` 只在一个 Qwen math setting 得到验证。
- **Trade-offs / Failure Modes / Coexistence**：复用历史 trajectories 降低在线环境、tool 和多环境部署成本，
  但新增 pool coverage、trajectory/environment/teacher version identity、stale observations、prefix support、
  teacher conditional calibration 与 sampling-bias 风险。online OPD 在 environment 便宜、需要 failure
  recovery exploration、teacher 在 student histories 上可靠时仍成立；offline SFT 在没有 teacher logits 或
  只需行为复制时更简单。关系为 `Direct Evolution`，不是替代。
- **ROADMAP / Adjacent Chapters / Decision**：Ch29 为主 owner，已读 Ch27～30，并联读 Ch77/80 的
  trajectory、workflow 与 rollout ownership。现有 Ch29 只写了 reasoning-trace SFT 分支，尚未区分
  teacher-prefix replay 的 two-sided shift，因此 disposition 为 `Refine — New Mechanism / Experimental`；
  已写入 `TRAIN-SFT`。

### ReflectWorld-MM — 28/30

- **Source Family / History / Full-read Coverage**：`REFLECTWORLD-MM-ENTITY-MEMORY`；
  arXiv:2607.09759v1，first-public 2026-07-06，v2 2026-07-14。已读 metadata/revision、
  Introduction/Related Work、完整 architecture、memory equations、implementation、六项 benchmark、
  provenance table、answer-time ablations、qualitative cases、stream/agent/dashboard appendices；并核对
  official repository identity。论文没有独立 Limitations section，故缺失项不能被视为已经验证。
- **Original Problem / Why Previous Designs Were Reasonable**：固定 Context、frame/clip summary 与 flat
  feature store 适合 bounded video：状态简单、查询局部、无需长期 identity reconciliation。open-ended
  stream 中，同一人或物体跨时段重现，frame-centric history 难以把分散 observation 累积为可更新事实，
  全量 Context 又使 token、latency 与 storage 随历史增长。
- **Changed Constraint / Mechanism**：perception front-end 在 bounded working memory 中生成
  entity-resolved observations；episodic memory 由 observation→trace→schema 分层；semantic memory 围绕
  entity 执行 Add/Update/Delete/no-change consolidation，并以 `w ← w + (1-w)γ`（论文取 `γ=0.2`）
  强化重复证据；procedural rules 反向约束感知与 notification resolution。这里的增量不是 memory
  taxonomy 本身，而是把 entity identity 设为 longitudinal evidence 的 join key 与 semantic update target。
- **State Ownership / Control and Data Flow**：stream gateway 拥有输入连接；perception model 拥有候选
  observation，但 entity resolver 才能提交 identity；working memory 拥有当前 segment/event continuity；
  persistent store 分别拥有 episodic、semantic 与 procedural records；consolidator 拥有 derived edits；
  retrieval agent 只读取，不成为 truth authority；deterministic rule resolver 拥有 notification、dedup 与
  cooldown。low-latency path 在 per-user lock 下先提交 identity-critical fields，异步 enrichment 随后
  reconcile，避免慢 enrichment 阻塞 live stream。
- **Implementation Contract**：论文实现使用 GPT-5-mini 做 perception/consolidation、GPT-5 做 query
  agent、`text-embedding-3-small` 1536-dimensional index，并以 local ONNX utilities 辅助感知。working
  memory 约为 100-word summary、三个 recent segments、最多八个 targets；每五个 observations consolidation，
  current segment 不作为自身证据；Update/Delete 必须指向已有 fact ID，identity facts 被保护。gateway
  支持 RTSP、files、webcams、HTTP 与 smartphone WebRTC。以上均是该版本实现事实，不是通用参数。
- **Evaluation Contract / Provenance**：六项 benchmark 混合 multiple-choice option matching 与
  M3-bench GPT-5-mini judge；因原 GPT-4o judge 不再可用，仅 GPT-5、M3-Agent 与本系统在 M3 上按新 judge
  重跑。WorldMM 只在 VideoMME-Long 重跑，其他多项 baseline 数字来自原论文。answer-time ablation
  复用同一已构建 memory 并阻断 retrieval component，没有重新构建 write-side state，因此只能作为组件
  价值的 lower bound，不能因果隔离 perception、identity resolution 或 consolidation。
- **What Evidence Proves / Does Not Prove**：结果支持在披露的模型、memory backend 与评测协议中，
  entity association、hierarchical retrieval 与 persistent external memory 对 entity-sensitive/long-video QA
  有效；同一 GPT-5 query agent 相对无该 memory 的对照也提供局部支持。它不证明 months-scale storage/
  retrieval bounded、所有 baseline 在同一 judge 下公平、自动 semantic updates 正确、real-time tail SLO、
  multi-tenant isolation、privacy/deletion、crash recovery 或通用 superiority；M3 absolute accuracy 仍低。
- **Trade-offs / New Failure Modes / Coexistence**：获得跨时间 entity continuity、revisable semantic view 与
  bounded query working set，代价是 identity false merge/split、consolidation hallucination、protected identity
  fact 难纠正、episodic store 持续增长、stale enrichment、privacy/biometric risk 与 rule-trigger side effects。
  bounded video、短 history 或 exact playback 仍可使用 flat/full-context 路线；entity-centric memory 只在
  persistent entities 与跨时关联构成 workload 时更合理。关系为 `Layering / Dependency`，不是替代。
- **ROADMAP / Adjacent Chapters / Decision**：Ch73 为主 owner，已读 Ch72～74 与 Ch80，并检查 Ch70 的
  world-state 边界。现有 Ch73 已拥有 episodic/semantic/procedural taxonomy、typed transition、provenance、
  consolidation 与并发原则；论文新增的章节级缺口是 perception/entity resolver/consolidator/retrieval/rule
  resolver 的 owner separation，以及 identity-critical synchronous commit 与 asynchronous enrichment 的
  failure boundary。因此 disposition 为 `Refine — New Mechanism / Experimental`；已写入 `AGENT-MEMORY`。

### KVpop — 26/30

- **Source / Coverage**：`KVPOP-LEARNED-EVICTION`；arXiv:2607.05061v1，first-public 2026-07-06；
  当前 HTML v2。已读 future-attention target、boundary loss、transposed-attention target implementation、
  stateless/mLSTM scorer、running top-k/FlexAttention、Qwen3 4B/8B evaluation、ablation 与 limitations。
- **Mechanism / State**：每 head 保留 sink、recent protected window 与 long-range top-k。token 到 eviction
  boundary 时才按未来 attention mass teacher target 决定 keep/drop；stateful scorer 可利用 protected-window
  期间累积的近未来 evidence。cache budget、scorer state、decay、base checkpoint 与 sparse kernel 必须共同
  版本化，且 eviction 是不可逆状态转移。
- **Evidence / Trade-off**：作者实验支持该 retrofit 在披露模型/任务下以 bounded cache 保留部分 dense
  quality；不证明通用 workload/SLO。获得恒定 cache 上界，付出 future-target approximation、scorer training、
  delayed-state、错误永久删除与专用 kernel。保留全 cache 的 sparse retrieval 在质量优先时仍合理。
- **ROADMAP / Decision**：已读 Ch19、Ch22、Ch41、Ch43、Ch50；主 owner Ch41，Ch22 handoff。`Refine —
  Existing Argument / Experimental`：补充“稀疏读取≠有界持久状态”和 boundary-time predictive eviction。

### Single-Rollout Asynchronous Optimization — 25/30

- **Source / Coverage**：`SARO-AGENTIC-RL`；arXiv:2607.07508v1，first-public 2026-07-08；已读
  single-rollout objective、rollout-logprob importance sampling、double-sided token clipping/masking、skip-
  observation GAE、value-model/frozen-attention training、math/SWE/online-writing evaluation、ablations/limitations。
- **Mechanism / State**：异步 actor 消费单条 trajectory；rollout engine 保存逐 token behavior logprob，learner
  用当前/behavior ratio 严格裁剪，observation tokens 不传播 advantage；critic 更新更频繁并冻结 attention。
  rollout policy、logprob、environment observation mask、critic/actor versions 是不可丢失的训练状态。
- **Evidence / Trade-off**：作者只在 Qwen3-30B-A3B、reasoning/coding/simulated preference shift 上验证；
  不证明所有 asynchronous RL。减少 group rollout 成本，增加 critic、behavior-probability storage、lag masking
  和单样本 variance；同步/group-relative 方法在短 rollout、critic 不可靠时仍成立。
- **ROADMAP / Decision**：已读 Ch28～30、Ch34、Ch77；Ch29 已覆盖 cross-policy probability coordinates，
  本文补充 observation-token boundary 与 single-rollout critic branch。`Refine — Existing Argument /
  Experimental`，主 owner Ch29。

### Linear Attention Architectures — 27/30

- **Source / Coverage**：`LINEAR-ATTN-COMPARISON`；arXiv:2607.07953v1，first-public 2026-07-08；已读
  common recurrence derivations、mixer/optimizer/stack matrix、350M/15B-token controlled runs、sequence-length
  timing、larger DeltaNet、CLER/CLVR cross-layer routing、reproducibility rules、discussion/evidence limitations。
- **Mechanism / Evidence**：论文把多种 linear Attention 写成 recurrent associative-memory update，并展示
  mixer、optimizer、hybrid stack 共同决定 operating point；CLVR 把 lower-layer write value 投到 aligned hidden
  stream，优于直接转发 delta error，但效应小。single-run/uneven sweeps 不支持“最佳架构”排名。
- **Trade-off / Evolution**：pure recurrence 获得长度 scaling，hybrid softmax 补 quality；更强 memory update
  往往更慢。旧 softmax 在 retrieval/训练成熟度优先时仍合理。`Principle Reuse` 于跨层 residual routing，
  不是取代 Attention。
- **ROADMAP / Decision**：已读 Ch14～17、Ch22；Ch22 已有 hybrid 主线，但缺 mixer×optimizer×stack
  作为联合 contract。`Refine — Existing Argument / Experimental`，主 owner Ch22。

### Sparse Delta Memory — 25/30

- **Source / Coverage**：`SPARSE-DELTA-MEMORY`；arXiv:2607.07386v1，first-public 2026-07-08；已读
  sparse read/write update、learned initial parametric state、isoFLOP/model-scale experiments、RULER、hybrid
  ablation、memory-utilization/kernel analysis、compute resources 与 limitations。
- **Mechanism / State**：SDM 把 Gated DeltaNet 的 dense matrix state 换成大 explicit slot table，每 token 只
  sparse read/write 少量 slots；learned initial table 承担 parametric memory，runtime table 承担 sequence state。
  二者 checkpoint/生命周期不同，不应统称一个 memory。
- **Evidence / Trade-off**：作者到 8B 的实验支持更大 sparse state 改善部分 ICL/long-context tasks；但 8B
  training 约慢 1.49×，state memory 可接近 model parameters、kernel MFU 仍受限。Full Attention 的 exact
  retrieval 与 resource-constrained 场景仍成立。
- **ROADMAP / Decision**：已读 Ch15、Ch19、Ch22、Ch43、Ch50；主 owner Ch22。`Refine — Existing
  Argument / Experimental`：增加“计算稀疏不等于状态便宜”与 parametric/runtime state 分界。

### Remember When It Matters — 26/30

- **Source / Coverage**：`PROACTIVE-MEMORY-AGENT`；arXiv:2607.08716v1，first-public 2026-07-09；
  已读 two-phase memory agent、structured bank、intervention policy、Terminal-Bench/τ²-Bench、SETA SFT/
  GRPO、ablations、transfer 与 preliminary limitations。
- **Mechanism / State**：独立 memory process 每步先更新 structured bank，再输出
  `<context_for_action>` 或 `<no_intervention>`；action agent 保持冻结。memory bank 与 intervention policy
  分属事实状态和 activation policy，silent action 是合法决策而非 retrieval miss。
- **Evidence / Trade-off**：作者实验支持 selective intervention 优于 passive/always-on variants，并只显示
  小规模 transfer；不证明跨环境长期自治。收益是降低遗忘/重复，代价是额外 call、interrupt distraction、
  stale memory 与 intervention-policy drift；短任务/显式 context 仍无需独立 agent。
- **ROADMAP / Decision**：已读 Ch71～73、Ch76～77；Ch73 已分离 Fact State 与 Retrieval-policy，本文
  补强 intervention timing。`Refine — Existing Argument / Experimental`，主 owner Ch73。

### RynnWorld-4D — 21/30

- **Source / Coverage**：`RYNNWORLD-4D`；arXiv:2607.06559v1，first-public 2026-07-07；已读 RGB-depth-
  flow representation、frozen backbone/policy head、world/policy datasets、generation/geometric/motion metrics、
  robot evaluation、ablations、hardware/training 与 limitations。
- **Mechanism / Evidence**：同步 RGB-DF latent 把 appearance、geometry、motion 暴露给 inverse/flow policy，
  避免每 action 重做完整 video denoising；作者闭环结果不证明 latent 具有一般因果世界模型。当前约 9Hz on
  RTX 5090、egocentric/multi-view 边界禁止外推实时控制。
- **Trade-off / Decision**：显式 geometry/motion 提高 control interface，代价是 depth/flow acquisition、
  diffusion latency、sensor alignment 与 sim/real bias。已读 Ch10、Ch18、Ch62；`Refine — Existing Argument /
  Experimental`，主 owner Ch10，Ch18 只 handoff multimodal state。

### AlayaWorld — 22/30

- **Source / Coverage**：`ALAYAWORLD-RUNTIME`；arXiv:2607.06291v1，first-public 2026-07-07；已读
  camera/action conditioning、anchor-tree/spatial indexing、streaming generation、qualitative/user evaluation、
  comparison、runtime discussion 与 limitations。
- **Mechanism / Evidence**：spatial cache/index 按位置而非 recency 找 anchor，支持 loop closure 与长 detour；
  但静态 spatial cache 难表达 dynamic objects，且依赖 depth/geometry。论文以 qualitative evidence 为主，
  不证明物理正确或生产 latency。
- **Trade-off / Decision**：从 rolling context 到 spatially keyed state，获得地点 continuity，新增 geometry
  estimation、branch/index 和 dynamic-state inconsistency。已读 Ch10、Ch71、Ch73、Ch77；主 owner Ch10，
  `Refine — Existing Argument / Experimental`。

### LaMem-VLA / Dual Latent Memory — 21/30

- **Source / Coverage**：`DUAL-LATENT-VLA-MEMORY`；arXiv:2607.07608v1，first-public 2026-07-08；
  已读 short/long vault、curator/weaving/action modules、training、real/sim robot evaluation、baselines/ablations；
  无独立 limitations 章节，披露缺口单列。
- **Mechanism / Evidence**：curator 把近期 visual evidence 与长期 semantic/action-continuity 分入双 vault，
  再以 dual-scale latent weaving 条件化 action diffusion。作者结果支持所测 manipulation tasks，不证明 vault
  内容可解释、跨 embodiment 或 lifelong stable。
- **Trade-off / Decision**：比固定 frame window 更有时间跨度，付出 latent contamination、vault update、
  phase misclassification 与不可审计状态；短 Markov tasks 仍适合 current observation。已读 Ch10、Ch18、
  Ch73；主 owner Ch73，`Refine — Existing Argument / Experimental`。

### Vision as Unified Multimodal Generation — 23/30

- **Source / Coverage**：`VISION-UNIFIED-GEN`；arXiv:2607.06560v1，first-public 2026-07-07；已读
  text/image dual decoding、task instruction/schema、dataset mixture、detection/OCR/keypoint/dense geometry tasks、
  training/evaluation、ablations/appendices；无独立 limitations 章节。
- **Mechanism / Evidence**：symbolic outputs 用 next-token CE，dense maps 用 VAE latent/rectified flow，同一
  native decoders 取代 task-specific heads。它统一的是 interface/training surface，不是同一 tokenization，亦不
  证明所有 vision tasks 共享最优 decoder。
- **Trade-off / Decision**：减少专用 heads，增加 schema/prompt、mixed-loss balance、decoder latency 与 metric
  heterogeneity；固定 dense-prediction head 在实时/精度关键任务仍合理。已读 Ch18、Ch23、Ch62；`Refine —
  Existing Argument / Experimental`，主 owner Ch18。

### Infinite Worlds with Versatile Interactions — 21/30

- **Source / Coverage**：`INFINITE-WORLDS`；arXiv:2607.07534v1，first-public 2026-07-08；已读 causal
  chunk pretraining、real-time distillation、action/text intervention、pilot/director harness、evaluation、hardware
  claims、discussion 与 limitations。
- **Mechanism / Evidence**：world stream 以前序 chunks、pose/action/prompt 条件生成，harness 编排 user/world
  intervention。论文自述最关键限制：离开 context 后重访区域会再生成而非真正 recall；故“infinite”只指
  streaming horizon，不是 persistent identity 或 causal world state。
- **Trade-off / Decision**：连续生成换来 chunk drift、harness state、false persistence 与 distillation quality；
  authored simulator 在确定规则/安全控制仍成立。已读 Ch10、Ch73、Ch77；`No Change — Already Covered /
  Experimental Case`，Ch10 已明确 visual stability≠world memory。

### UniClawBench — 24/30

- **Source / Coverage**：`UNICLAW-PROACTIVE-EVAL`；arXiv:2607.08768v1，first-public 2026-07-09；已读
  Docker/live-browser/file tasks、step checkpoints、hidden supervisor/user simulator firewall、capability taxonomy、
  cross-framework evaluation、token costs、analysis 与 limitations。
- **Mechanism / Evidence**：hidden supervisor 持有细粒度 completion criteria，只向 user simulator 暴露 coarse
  progress，避免 ground-truth leakage；被测对象绑定 model+framework+environment。论文证明该 harness 的
  framework/token/performance差异，不证明 production proactivity。
- **Trade-off / Decision**：动态任务更真实，却增加 environment drift、checkpoint authoring、simulator bias
  与高 token cost；static deterministic tests 仍适合 regression。已读 Ch62、Ch77、Ch80；Ch62 已覆盖相同
  object/evidence boundary，`No Change — Already Covered`。

### Blocked Primary-Source Backlog — 3 Candidates

| Candidate | First-public | Source Family | Blocked Primary Source | ROADMAP Owner | Claims explicitly not verified |
| --- | --- | --- | --- | --- | --- |
| AgentLens | 2026-07-07 | `AGENTLENS-TRAJECTORY-EVAL` | https://arxiv.org/abs/2607.06624 | Ch62/80 | production review labels、formal verifier coupling、nightly regression |
| UP asymmetric optimization | 2026-07-08 | `UP-RL-OBJECTIVE` | https://arxiv.org/abs/2607.06987 | Ch29 | positive/negative ratio asymmetry、stability and exploration ablations |
| Ideas Have Genomes | 2026-07-09 | `SCIENTIFIC-LINEAGE-EVAL` | https://arxiv.org/abs/2607.08758 | Ch62/77 | lineage ground truth、novelty leakage、workflow evidence |

2026-08-13 exact-source retry 已恢复并审完原 14 项中的 11 项。以上 3 项仍无法读取 primary text；末列只
声明不得从标题、摘要或旧 pending focus 推断的机制，不是论文结论。它们不计 Full Source Review、不修改
Books，原评分只保留 provisional discovery priority。按 blocked-skip 规则进入 backlog，不阻止 forward cursor。

### Recovered Cross-Week Spillbacks — 7 Identities

七项 primary text 均已恢复，并按 v1 日期确认属于 W28；其六维评分已进入 Candidate Scoring，完整 Source
Review 如下。后续 revision 只更新 evidence boundary，不移动 owner week。

### ABot-AgentOS — 27/30

- **Source / Coverage**：`ABOT-AGENTOS`；arXiv:2607.10350v1，first-public 2026-07-11；当前 v3。
  已读 planning/skill execution/verification、multimodal graph memory、edge-cloud runtime、benchmark/memory
  evaluation、split-gated self-evolution、training pipeline、Appendices 与 limitations。
- **Mechanism / Evidence**：OS layer 隔离 scene plan、skill sandbox、multi-stage verifier、memory writer/query
  与 controller；失败诊断只生成 evo-asset candidate，经 safety gate 后从后续 split 生效，避免测试污染。
  论文部分表格由 GPT-5.4 同时作为 writer/answerer/judge，且完整 benchmark 尚待发布，不能外推 production。
- **Trade-off / Decision**：统一 runtime 获得跨 embodiment orchestration，代价是 plane coupling、LLM-judge
  circularity、memory/evolution contamination 与 edge-cloud failure。已读 Ch73、Ch77、Ch80；`Refine —
  Existing Argument / Experimental`，主 owner Ch80，Ch73 handoff。

### GRASP — 27/30

- **Source / Coverage**：`GRASP-GRANULARITY-RAG`；arXiv:2607.10463v1，first-public 2026-07-11；已读
  semantic/keyword/search/read/stop actions、sentence→parent paragraph observation、RL reward、multi-hop QA、
  baselines/ablation、infrastructure 与 limitations。
- **Mechanism / Evidence**：policy 先以 sentence-level semantic/lexical search 探索，再按 parent identifier
  读取 paragraph 验证，最后 stop/answer；它联合决定 query、retriever、granularity 与 stopping。gold supporting-
  fact reward 限制开放域外推，作者排名不证明真实 Web。
- **Trade-off / Decision**：细粒度 search 降低 context，paragraph read 恢复证据完整性，代价是多动作 RL、
  reward annotation、tool latency 与 premature stop。已读 Ch72、Ch77；Ch72 已有同一 joint policy，`No Change
  — Already Covered / Experimental Case`。

### Weak-to-Strong Direct OPD — 29/30

- **Source / Coverage**：`DIRECT-OPD-WEAK-TO-STRONG`；arXiv:2607.05394v1，first-public 2026-07-06；
  已读 policy-log-ratio derivation、on-policy top-k objective、teacher pairs/students、AIME experiments、compute/
  response-length/KL ablations、composition 与 limitations。
- **Mechanism / Evidence**：转移对象不是弱 teacher 最终 policy，而是其 post-RL 相对 pre-RL reference 的
  token log-ratio，且在强 student 自己访问的 prefixes 上计算。这把小模型 RL shift 变成 dense reward；只有
  teacher/reference shift 在 student states 上仍有意义时才成立。
- **Trade-off / Decision**：避免模仿弱 teacher 上限，代价是双 teacher checkpoint、top-k coverage、KL/
  length sensitivity 与 on-policy query cost。已读 Ch25、Ch27～30；`Refine — Existing Argument /
  Experimental`，主 owner Ch29。

### What LLM Forecasters Know but Don’t Say — 26/30

- **Source / Coverage**：`FORECAST-PROBE-CALIBRATION`；arXiv:2607.08046v1，first-public 2026-07-09；
  已读 representation-pooling probes、calibration, evidence ablation/diversion、pre-reasoning triage/retrieval、
  leakage controls、OOD stress、temperature/probe sweeps 与 caveats。
- **Mechanism / Evidence**：intermediate activation probe 在论文 splits 中比 verbal confidence 校准更好，并能
  检测 prompt evidence 改变但 CoT 未反映的 behavior shift；probe 是相关 sensor，不是 model truth/causal
  proof。作者结果不能外推所有 forecasters/models。
- **Trade-off / Decision**：可用于 triage/retrieve/monitor，新增 probe data、layer/model coupling、leakage 与
  gaming。已读 Ch5、Ch62、Ch68；Ch5/68 已有 interpretability evidence ladder，`No Change — Already
  Covered / Experimental Case`。

### PolicyShiftGuard — 26/30

- **Source / Coverage**：`POLICYSHIFTGUARD`；arXiv:2607.05910v1，first-public 2026-07-07；已读
  compositional policy text/data construction、same-image policy shifts、training/evaluation、latency、ablation、
  dataset metadata 与 limitations。
- **Mechanism / Evidence**：guardrail 输入必须绑定 content 与 policy bundle；同一 image 在不同 policy 下可
  翻转，故 content classifier 不能拥有最终 authority。实验限 static images、structured English policy，未覆盖
  video/multiturn/dynamic Web。
- **Trade-off / Decision**：runtime policy adaptation 提升可更新性，增加 policy parser/version、conflict、
  latency 与 audit。已读 Ch62、Ch68；Ch68 已有 Policy-as-Data，`No Change — Already Covered`。

### From Noisy Traces to Root Causes / STRACE — 27/30

- **Source / Coverage**：`STRACE-ROOT-CAUSE`；arXiv:2607.07702v1，first-public 2026-07-08；已读
  dependency graph、failure mining/filtering、causal slice/backtracking、root-module localization、optimization、
  three benchmarks、ablation/cost 与 limitations。
- **Mechanism / Evidence**：以 harness/code/tool/prompt 依赖先验把 linear trace 变 graph，再从 failure node
  回溯 corrupted flow，排除无关并行 branches，输出可编辑 module target。它是 structure-guided attribution，
  不是从 observational logs 证明真实 causality，且要求 white/gray-box visibility。
- **Trade-off / Decision**：减少 full-trace noise/cost，新增 dependency-prior error、selector bias 与错误 patch
  target。已读 Ch62、Ch65、Ch76～77；`Refine — Existing Argument / Experimental`，主 owner Ch65，
  Ch62 handoff。

### DeepSearch-World — 27/30

- **Source / Coverage**：`DEEPSEARCH-WORLD`；arXiv:2607.07820v1，first-public 2026-07-08；当前 v2。
  已读 deterministic Wikipedia search/visit environment、trajectory generation/rejection/quality filtering、evolving
  SFT、asynchronous training、benchmarks/ablation、prompts 与 limitations。
- **Mechanism / Evidence**：verifiable offline world 将 search/visit action 绑定 deterministic corpus/URL，强
  teacher 生成 trajectories，answer correctness rejection sampling 为主要 gate，accepted data 迭代训练 student。
  Wikipedia-only 与 evolving SFT 不证明 live-Web transfer、freshness 或高层 planning 注入。
- **Trade-off / Decision**：确定环境降低成本/variance，付出 corpus closure、tool-schema simulation gap、teacher
  bias 与 self-distillation narrowing。已读 Ch23、Ch29、Ch62、Ch77；`Refine — Existing Argument /
  Experimental`，主 owner Ch77，Ch23 handoff。

## Final Books Integration Ledger

| # | Candidate / Source Family | Final disposition | Stable owner / evidence |
| ---: | --- | --- | --- |
| 1 | Anthropic J-space / Jacobian Lens | Refine — Existing Argument | WORLDVIEW-WHAT-NEURAL-NETWORKS-LEARN；decodability→intervention ladder 已复核 |
| 2 | Anthropic GRAM | Emerging / Experimental | PLATFORM-SECURITY；training-state compartment 只作受限分支 |
| 3 | DSpark | Refine — Existing Argument | INFER-SPECULATIVE-DECODING；dynamic verify-depth policy 已复核 |
| 4 | Length Penalties Make CoT Less Monitorable | Weekly Only — Experimental Claim | PLATFORM-EVALUATION-SYSTEM；单篇结果不足以改写 monitorability |
| 5 | KVpop | Refine — Existing Argument | INFER-KV-CACHE；learned eviction 与 future-access evidence |
| 6 | LLM-as-a-Verifier | No Change — Already Covered | PLATFORM-EVALUATION-SYSTEM；probabilistic scorer 不拥有 truth |
| 7 | ReOPD | Refine — New Mechanism | TRAIN-SFT；teacher-prefix replay 与 two-sided shift |
| 8 | ReflectWorld-MM | Refine — New Mechanism | AGENT-MEMORY；entity-resolved longitudinal memory |
| 9 | AgentLens | Unverified / Blocked | 无机制 owner；等待 primary text |
| 10 | Single-Rollout Asynchronous Optimization | Refine — Existing Argument | TRAIN-GRPO；rollout staleness / update ownership |
| 11 | Linear Attention Architectures | Refine — Existing Argument | MODEL-ATTENTION；state capacity/access coexistence |
| 12 | Sparse Delta Memory | Refine — Existing Argument | MODEL-ATTENTION；sparse recurrent state branch |
| 13 | UP asymmetric optimization | Unverified / Blocked | 无机制 owner；等待 primary text |
| 14 | Remember When It Matters | Refine — Existing Argument | AGENT-MEMORY；intervention timing / behavioral state |
| 15 | RynnWorld-4D | Refine — Existing Argument | MULTIMODAL-WORLD-MODELS；4D predictive state |
| 16 | AlayaWorld | Refine — Existing Argument | MULTIMODAL-WORLD-MODELS；interactive world transition |
| 17 | Dual Latent Memory VLA | Refine — Existing Argument | AGENT-MEMORY；latent control / episodic state boundary |
| 18 | Vision as Unified Multimodal Generation | Refine — Existing Argument | MULTIMODAL-GENERATIVE-PARADIGMS；shared generation factorization |
| 19 | Infinite Worlds with Versatile Interactions | No Change — Already Covered | MULTIMODAL-WORLD-MODELS；interaction/world-state boundary 已覆盖 |
| 20 | Ideas Have Genomes | Unverified / Blocked | 无机制 owner；等待 primary text |
| 21 | UniClawBench | No Change — Already Covered | PLATFORM-EVALUATION-SYSTEM；dynamic environment identity 已覆盖 |
| 22 | ABot-AgentOS | Refine — Existing Argument | AGENT-WORKFLOW；split-gated evo-asset admission |
| 23 | GRASP | No Change — Already Covered | AGENT-RAG；granularity/retrieval/stopping joint policy 已覆盖 |
| 24 | Weak-to-Strong Direct OPD | Refine — New Mechanism | TRAIN-SFT；relative policy-shift transfer |
| 25 | What LLM Forecasters Know | No Change — Already Covered | WORLDVIEW-WHAT-NEURAL-NETWORKS-LEARN；probe 只是 sensor |
| 26 | PolicyShiftGuard | No Change — Already Covered | PLATFORM-SECURITY；Policy-as-Data 已覆盖 |
| 27 | STRACE / Root Causes | Refine — New Mechanism | PLATFORM-TRACE；dependency-graph root-cause view |
| 28 | DeepSearch-World | Refine — New Mechanism | AGENT-WORKFLOW；offline-world→live-promotion boundary |
| 29 | PyTorch 2.13 | Refine — Existing Argument | TRAIN-DISTRIBUTED-TRAINING；communication backend contract 已复核 |
| 30 | Qwen Code weekly update | Weekly Only — Version/Product Fact | AGENT-PLATFORM；无公开新机制 |

计数：`Refine 18 / No Change 6 / Weekly Only 2 / Emerging 1 / Unverified-Blocked 3`。Blocked 项没有根据
标题、摘要或旧 focus 反推机制，也没有获得 Books owner。

## Repository Changes

- 删除已被 W28 完整吸收的 `papers/2026/07/06/README.md` 与
  `papers/2026/07/08/README.md`；
- refine 第 5、32、44、52、68 章；
- GRAM 仅以 `Status: Experimental` 的训练状态分支进入 Ch68；PyTorch 2.13 只沉淀
  communication backend contract，未复制 release feature list；Length Penalty 未写 Books。
- 2026-08-09 恢复 15 个漏项；2026-08-12 补回 9 个后续周 attribution identities；2026-08-13 exact-source
  retry 后闭合为 30 families、27 Full Source Reviews 与 3 explicit blocked；
- Books Gate 通过后，refine `TRAIN-SFT`、`AGENT-MEMORY`、`PLATFORM-TRACE` 与 `AGENT-WORKFLOW`；
  既有 J-space、DSpark、PyTorch、GRAM 及 KV/Attention 内容经复核保留；
- 新增 30 行 final ledger；未新增 Part、章节或 Stable Node，cursor 进入 W29。

## Open Questions

1. J-space 的 intervention results 能否在 open-weight、不同 tokenizer 与非语言模型上复现？
2. DSpark 的 confidence calibration 怎样随 batch composition 与 target model revision 更新？
3. torchcomms 与 ProcessGroup/NCCL/UCC 的长期责任边界是什么？
4. CoT compression 的 cost saving 是否必须同时设置 monitorability guardrail？
5. GRAM module 删除后，如何证明相关能力不能由 shared weights 恢复或重建？
6. scheduler 应暴露哪些 trace 与 calibration 指标来解释 DSpark verify-window 决策？
7. learned KV eviction 的 future-attention supervision 是否能跨 workload、topic shift 与 model revision？
8. verifier 的 granularity/repetition/criteria budget 如何按 risk slice 自适应，而不把同源 bias 放大为 reward？
9. asynchronous agentic RL 的 rollout staleness 与 memory intervention 的 stale state 能否使用统一 freshness contract？
10. AgentLens、UP 与 Ideas Have Genomes 的 event-version primary text 恢复后，是否改变 blocked-skip disposition？

## Sources

### 模型与研究机构

- Anthropic, “A global workspace in language models,” published 2026-07-06; accessed
  2026-07-31:
  https://www.anthropic.com/research/global-workspace
- Gurnee et al., “Verbalizable Representations Form a Global Workspace in Language Models,”
  published 2026-07-06; accessed 2026-07-31:
  https://transformer-circuits.pub/2026/workspace/index.html
- Anthropic Jacobian Lens code, accessed 2026-07-31:
  https://github.com/anthropics/jacobian-lens
- Anthropic, “An off switch for dual-use knowledge in AI models,” published 2026-07-08;
  accessed 2026-07-31:
  https://www.anthropic.com/research/off-switch-dual-use
- Google Research Blog, accessed 2026-07-31:
  https://research.google/blog/

### 论文与发现索引

- Cheng et al., “DSpark,” submitted 2026-07-06; accessed 2026-07-31:
  https://arxiv.org/abs/2607.05147
- Little, “Length Penalties Make Chain-of-Thought Less Monitorable,” submitted 2026-07-08;
  accessed 2026-07-31:
  https://arxiv.org/abs/2607.09786
- Kwok et al., “LLM-as-a-Verifier,” v1 submitted 2026-07-06; full HTML and appendix
  accessed 2026-08-09: https://arxiv.org/abs/2607.05391
- Hauzenberger et al., “KVpop,” v1 submitted 2026-07-06; accessed 2026-08-09:
  https://arxiv.org/abs/2607.05061
- Podivilov et al., “AgentLens,” v1 submitted 2026-07-07; accessed 2026-08-09:
  https://arxiv.org/abs/2607.06624
- Hou et al., “Single-Rollout Asynchronous Optimization,” submitted 2026-07-08; accessed
  2026-08-09: https://arxiv.org/abs/2607.07508
- Cerruti et al., “Linear Attention Architectures,” submitted 2026-07-08; accessed 2026-08-09:
  https://arxiv.org/abs/2607.07953
- Cabannes et al., “Sparse Delta Memory,” submitted 2026-07-08; accessed 2026-08-09:
  https://arxiv.org/abs/2607.07386
- Fan et al., “UP,” submitted 2026-07-08; accessed 2026-08-09:
  https://arxiv.org/abs/2607.06987
- Wu et al., “Remember When It Matters,” submitted 2026-07-09; accessed 2026-08-09:
  https://arxiv.org/abs/2607.08716
- W28 restored world-model, VLA and evaluation families, accessed 2026-08-09:
  https://arxiv.org/abs/2607.06559 ; https://arxiv.org/abs/2607.06291 ;
  https://arxiv.org/abs/2607.07608 ; https://arxiv.org/abs/2607.06560 ;
  https://arxiv.org/abs/2607.07534 ; https://arxiv.org/abs/2607.08758 ;
  https://arxiv.org/abs/2607.08768
- Hugging Face 2026-W28 display feed, discovery only; accessed 2026-08-09:
  https://huggingface.co/papers/week/2026-W28
- Hugging Face Daily Papers, discovery only, 2026-07-08; accessed 2026-07-31:
  https://huggingface.co/papers/date/2026-07-08
- ABot-AgentOS: https://arxiv.org/abs/2607.10350
- GRASP: https://arxiv.org/abs/2607.10463
- Weak-to-Strong Direct OPD: https://arxiv.org/abs/2607.05394
- What LLM Forecasters Know: https://arxiv.org/abs/2607.08046
- PolicyShiftGuard: https://arxiv.org/abs/2607.05910
- Root Causes: https://arxiv.org/abs/2607.07702
- DeepSearch-World: https://arxiv.org/abs/2607.07820
- ReflectWorld-MM: https://arxiv.org/abs/2607.09759
- ReflectWorld-MM official implementation: https://github.com/addxai/ReflectWorld
- Multi-Turn On-Policy Distillation with Prefix Replay（ReOPD）: https://arxiv.org/abs/2607.04763
- ReOPD official project page: https://baohaoliao.github.io/ReOPD/
- ReOPD official code: https://github.com/BaohaoLiao/ReOPD
- Google Scholar: https://scholar.google.com/
- Semantic Scholar: https://www.semanticscholar.org/
- OpenAlex: https://openalex.org/
- DBLP: https://dblp.org/

### AI Infra

- PyTorch 2.13.0 official release, released 2026-07-08; accessed 2026-07-31:
  https://github.com/pytorch/pytorch/releases/tag/v2.13.0
- PyTorch release cadence, accessed 2026-07-31:
  https://github.com/pytorch/pytorch/blob/main/RELEASE.md
- Qwen Code Weekly Updates, accessed 2026-07-31:
  https://qwenlm.github.io/qwen-code-docs/en/blog/updates/
