# AI Research Weekly — 2025-W04

> Coverage Window: 2025-01-20～2025-01-26
> Research Mode: Retrospective Backfill
> Accessed: 2026-07-31
> Backfilled: 2026-07-31

## Executive Summary

本周保留 3 项与长期 AI System 认知相关的证据：DeepSeek-R1、Kimi k1.5、Chain of Agents。重点不是记录发布热度，而是识别其改变了哪一项约束、机制与系统 trade-off。所有结论均按首次公开时间归档，性能或能力数字不脱离作者披露的模型、硬件、精度、输入输出、并发与 SLO 条件使用。

## Coverage Window and Limitations

- 使用官方发布日期、GitHub Release 时间或 arXiv v1 时间；不使用搜索收录日和后续修订日替代 first-public date。
- Google Scholar、OpenAlex、DBLP 用于 discovery、去重和引用链检查；论文机制回到 arXiv / 作者正文。
- Crossref 仅用于 Weekly metadata 交叉检验，不作为机制证据。
- 本周为历史回填，不补造 Daily；访问日期统一为 2026-07-31。
- 厂商 benchmark 和论文实验只代表其披露条件，缺少完整 workload contract 时不做跨系统性能结论。

## 1. 模型与研究机构

### Source Coverage

按固定机构顺序扫描 OpenAI、Anthropic、Apple、Google、Meta、Microsoft、NVIDIA、xAI、Amazon、Cohere、Ai2、Mistral、Qwen、DeepSeek、Kimi、Zhipu、MiniMax、Seed、ERNIE、Hunyuan、Huawei Noah、InternLM、StepFun、MiMo、InclusionAI 与 Hugging Face Blog。

- 保留：DeepSeek-R1（2025-01-20 (release); 2025-01-22 (paper v1)）。
- 保留：Chain of Agents Google Research follow-up（2025-01-23；原论文首发 2024-06-04）。

## 2. 论文与学术来源

按 arXiv → Google Scholar → OpenAlex → DBLP 发现与去重，回到论文 v1 正文核验；Crossref 只做 metadata 交叉检查。

- 保留：Kimi k1.5（2025-01-22）。

## 3. AI Infra 与工程项目

按固定工程顺序扫描 PyTorch、JAX、CUDA、Triton、vLLM、SGLang、NVIDIA Dynamo、TensorRT-LLM、Ray、KServe、Kubeflow、Kubernetes、Transformers、Accelerate、DeepSpeed、Megatron-LM、Unsloth、MLX、llama.cpp、ONNX Runtime 与 OpenXLA。

- 本组无达到保留门槛的候选。

## Candidate Scoring

| Candidate | Technical Novelty | System Impact | Practical Value | Source Reliability | Project Relevance | Longevity | Total | Decision |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| DeepSeek-R1 | 5 | 5 | 5 | 5 | 5 | 4 | 29/30 | Must Read；Books Integration 前按最新版全文复核 |
| Kimi k1.5 | 5 | 4 | 4 | 5 | 5 | 4 | 27/30 | Must Read；与 R1 形成 reasoning-RL 分支比较 |
| Chain of Agents | 4 | 3 | 3 | 4 | 4 | 3 | 21/30 | Worth Watching；作为长上下文系统分支 |

### Deep Analysis 1 — DeepSeek-R1

- First Public: 2025-01-20 (release); 2025-01-22 (paper v1)
- Status: Official release + arXiv v1
- Primary Source: https://arxiv.org/abs/2501.12948
- Evolution Relationship: Direct Evolution

#### Why

当可自动验证的任务提供稳定 outcome reward 时，推理能力可以通过大规模 RL 扩展；但只优化正确性会暴露可读性、语言一致性和 reward hacking 风险。

#### Principle and Mechanism

R1-Zero 从 base model 直接进行规则奖励 RL；R1 再加入 cold-start data、reasoning-oriented RL、rejection sampling/SFT 与面向一般能力和偏好的第二阶段 RL。

#### Trade-off and Evidence Boundary

纯 RL 展示 emergence，却产生可读性与语言混杂问题；多阶段 pipeline 改善可用性，但重新引入数据生产、筛选偏差与更复杂的训练闭环。蒸馏迁移的是行为分布，不等于小模型复制完整训练机制。

#### Connection and Evolution

知识树位置：第 27～30 章、第 62 章。Must Read；Books Integration 前按最新版全文复核。后续若进入 Books，必须保留旧方案仍成立的条件，并把作者实验、官方版本事实和本项目推断分开。

### Deep Analysis 2 — Kimi k1.5

- First Public: 2025-01-22
- Status: arXiv v1; Experimental
- Primary Source: https://arxiv.org/abs/2501.12599
- Evolution Relationship: Principle Reuse

#### Why

reasoning RL 的系统上限不仅由优化算法决定，也由长 rollout、采样吞吐、reward 可靠性与 train-inference mismatch 决定。

#### Principle and Mechanism

论文组合 long-context scaling、改进 policy optimization、在线数据生成与 long2short 方法，并披露训练基础设施优化。

#### Trade-off and Evidence Boundary

长 CoT 增加 test-time compute 与 rollout 成本；long2short 降低服务成本，却可能丢失探索多样性。作者 benchmark 不能外推到开放域可靠性。

#### Connection and Evolution

知识树位置：第 22、27～29、34、62 章。Must Read；与 R1 形成 reasoning-RL 分支比较。后续若进入 Books，必须保留旧方案仍成立的条件，并把作者实验、官方版本事实和本项目推断分开。

### Deep Analysis 3 — Chain of Agents

- First Public: 2024-06-04（论文）；2025-01-23（Google Research follow-up）
- Status: Google Research official blog + paper
- Primary Source: https://research.google/blog/chain-of-agents-large-language-models-collaborating-on-long-context-tasks/
- Evolution Relationship: Explanatory Analogy

#### Why

超长输入可以被拆成多个 context window 的协作处理，但这把单模型 memory 限制转化为跨 agent 信息压缩和误差传播。

#### Principle and Mechanism

worker agents 顺序读取 chunks 并传递中间表示，manager 汇总答案。

#### Trade-off and Evidence Boundary

分块扩展可处理长度，却增加调用成本、信息瓶颈和不可逆摘要误差；不应把它写成对原生长上下文的替代。

#### Connection and Evolution

知识树位置：第 22、71、75、78 章。Worth Watching；作为长上下文系统分支。后续若进入 Books，必须保留旧方案仍成立的条件，并把作者实验、官方版本事实和本项目推断分开。

## Full Source Review

### DeepSeek-R1

- **Candidate / Week / Score:** DeepSeek-R1 / 2025-W04 / 29/30。
- **Source Family ID:** `deepseekmath-grpo-r1zero-r1`；与 DeepSeekMath 的 GRPO 原始定义联读。
- **Source Type:** 官方 model release + 作者论文；论文后发表于 Nature。
- **First-public Date / Revision History:** release 2025-01-20；arXiv v1 2025-01-22；v2
  2026-01-04。本文按最新版 v2 复核，同时保留 2025 first-public identity。
- **Direct Primary Sources:** arXiv abstract、86 页 v2 PDF 全文及 appendix，
  https://arxiv.org/abs/2501.12948；https://arxiv.org/pdf/2501.12948；官方 repository/model cards。
- **Related Primary Sources:** DeepSeekMath/GRPO 原始论文 https://arxiv.org/abs/2402.03300；
  R1 distill model cards 只用于 artifact facts，不替代训练论文。
- **Access and Verification Status:** Verified；latest paper、method、evaluation、failed attempts、
  limitations 与 appendix 可访问。训练硬件规模、完整数据配方和 production serving contract 未披露。
- **Full-read Coverage:** 已读 metadata/revisions、Abstract、Introduction、Related Work、R1-Zero、
  GRPO/reward、R1 cold start/multi-stage pipeline、distillation、evaluation setup/results、failed attempts
  （PRM/MCTS）、limitations、conclusion 与关键 appendix。
- **Original Problem:** reasoning 能力通常依赖大量人工 reasoning demonstrations；若 outcome 可验证，
  能否从 base model 用 RL 激发探索，同时把 emergent behavior 变成可读、可部署的一般 assistant。
- **Why the Previous Design Was Reasonable:** SFT/cold-start demonstrations 给出格式、语言和稳定行为；
  PPO-style critic 提供 baseline；process reward 尝试更细 credit assignment。它们分别解决 sparse
  terminal reward、输出可读性与优化方差。
- **Changed Constraint:** 大规模可验证 math/code prompts 和 rule-based outcome reward 提供较低歧义
  的反馈，而 critic/value model 又是额外大模型状态与训练成本。
- **Mechanism:** R1-Zero 从 DeepSeek-V3-Base 直接用 GRPO 和 accuracy/format rewards 做 pure RL；
  R1 加入少量 cold-start reasoning data→reasoning-oriented RL→rejection sampling 形成 reasoning 与
  non-reasoning SFT data→全能力 SFT→第二阶段 RL（verifiable reasoning + preference/helpfulness/safety）。
  Distillation 用 R1 生成数据训练更小 dense models。
- **State Ownership:** actor policy、reference policy、optimizer 与 rollout policy versions 由 training
  runtime 拥有；group rewards 属同 prompt trajectory batch；verifier/reward functions 是独立评价接口。
  生成的 CoT 不是 production workflow authoritative state。
- **Control Flow / Data Flow:** prompt→同 policy group rollouts→rule/reward evaluation→group-relative
  normalized advantage→clipped/reference-regularized update；R1 pipeline 另将 successful samples 经
  rejection/filtering 变成 SFT data，再进入第二轮 RL。
- **Implementation Details:** 论文披露 GRPO objective、accuracy/format reward、data stages、distillation
  与部分 sampling/evaluation；未披露完整 cluster topology、rollout serving implementation、policy
  synchronization cadence 或故障恢复。
- **Evaluation Setup:** math（AIME/MATH-500 等）、code（LiveCodeBench/Codeforces 等）、knowledge、
  instruction following 与 general benchmarks；比较 R1-Zero、R1、distilled models 及公开/闭源 baselines。
- **Baselines / Ablations / Sensitivity:** R1-Zero vs multi-stage R1 是关键路线对比；论文还报告 PRM
  因 step definition、annotation/reward hacking 而难扩展，MCTS 因 token search space 与 value model
  训练困难未成为主路线。不是所有组件都有严格独立 ablation。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** base/model family 已披露，
  但训练 GPU 数、precision、global batch、rollout concurrency 与 serving TTFT/TPOT contract 未完整
  公开；因此不在 Books 写成本或吞吐数字。
- **What the Evidence Actually Proves:** 在可验证任务与作者设置中，pure RL 可以出现 self-reflection、
  verification 与更长 reasoning；同时 R1-Zero 的 readability/language mixing 暴露了 pure outcome
  optimization 的边界，多阶段数据与 RL 对可用模型仍不可或缺。
- **What It Does Not Prove:** 不证明 human demonstrations 已无价值，不证明 GRPO 对所有 domain 优于
  PPO/DPO，不证明 hidden CoT faithful，也不证明蒸馏模型复制了 teacher 的训练机制或开放域可靠性。
- **Limitations / Threats to Validity:** structured output/tool use、token efficiency、language mixing、
  prompt sensitivity 与 software-engineering RL 成本仍有限；reward hacking 与 evaluator contamination
  可能存在；很多训练系统条件 Not Disclosed。
- **Trade-offs / New Failure Modes:** 移除 critic 降低 learned value state，却增加 group rollout 成本、
  within-group variance sensitivity、reward interface 风险与 policy/rollout version synchronization；
  multi-stage pipeline 改善可用性但增加 data lineage、selection bias 与 restore complexity。
- **Where the Previous Design Still Applies:** SFT/cold start 适合格式、语言与稀有行为；PPO critic 在
  group comparison 不稳定或 dense value signal 有益时仍合理；DPO 适合已有 preference pairs 且不希望
  on-policy rollout 的场景。
- **Evolution Relationship:** `Direct Evolution`：DeepSeekMath GRPO→R1-Zero pure RL→R1 multi-stage，
  三者是约束变化下的共存路线，不是后者否定前者。
- **ROADMAP Node:** Ch29 主 owner；Ch25/27/28/30 是 SFT、reward、PPO/DPO 邻接；Ch31 管多模型 checkpoint。
- **Target and Adjacent Chapters Read:** 已读 Ch24～32，重点复核 Ch27～31；并核对 Ch62 的 evaluation
  evidence 边界。
- **Existing Coverage:** Ch29 已写入 R1-Zero→R1 完整演进、pure RL 与 multi-stage 同时成立、PRM/
  MCTS failed attempts 与不得泛化的边界；当前内容已按 v2 revision 与最终 Gate 复核。
- **Integration Decision:** `Refine — Existing Argument`；主 owner Ch29，保留 pure RL→multi-stage→distillation 演进。
  与 limitation，不追加发布摘要。
- **Changed Files or Rejection Reason:** 已复核 `books/part-03-training-system/29-grpo.md`；不外推作者 benchmark。
- **Open Questions:** open-domain/non-verifiable reward 的扩展、rollout policy freshness、reward
  contamination、token efficiency 与可恢复 multi-stage checkpoint contract。

### Kimi k1.5

- **Candidate / Week / Score:** Kimi k1.5 / 2025-W04 / 27/30。
- **Source Family ID:** `kimi-k1-5-long-cot-rl-runtime`。
- **Source Type:** 官方作者 technical report / arXiv（Experimental）。
- **First-public Date / Revision History:** v1 2025-01-22；v2 2025-03-05；v3 2025-05-28；
  v4 2025-06-03；按 v4 全文复核。
- **Direct Primary Sources:** https://arxiv.org/abs/2501.12599；
  https://arxiv.org/html/2501.12599。
- **Related Primary Sources:** Mooncake、Megatron、vLLM 只作为论文披露 infrastructure dependencies；
  未把其独立 benchmark 合并为 k1.5 证据。
- **Access and Verification Status:** Verified；method、RL infrastructure、evaluation/ablation 与 appendix
  可访问。proprietary model/weights、完整训练数据与 cluster size 未公开。
- **Full-read Coverage:** 已读 metadata/revisions、Introduction、long-CoT SFT、online policy mirror-
  descent variant、reward/data/sampling、long2short 四路线、pretraining、partial rollouts、hybrid
  train/inference deployment、checkpoint engine、sandbox、evaluation、ablation、conclusion 与 appendix。
- **Original Problem:** long-CoT RL 需要昂贵且长度差异极大的 rollouts；若按完整 trajectory 同步迭代，
  长样本形成 straggler，并使 training GPU 等待 inference；服务又承受更高 token cost。
- **Why the Previous Design Was Reasonable:** 完整 on-policy rollout 语义清楚、实现简单；分离 training/
  inference pools 保持 runtime 独立；long CoT 允许更充分探索。这些选择在短 rollout 和资源充足时合理。
- **Changed Constraint:** context 扩展到 128K、multimodal/verifiable tasks 与大规模 RL 后，tail length、
  weight transfer、GPU idle time 和 sandbox throughput 共同成为训练系统瓶颈。
- **Mechanism:** online policy mirror-descent variant 用 binary/rule or learned reward 与 KL regularization；
  curriculum/prioritized sampling 和 length reward 提升样本效率；partial rollout 以固定 token budget 分段，
  未完成 segment 进入 replay buffer，当前 segment 保持 on-policy、历史 segment 可复用；long2short 采用
  weight merge、shortest-correct rejection sampling、DPO 或 length-aware RL。
- **State Ownership:** central master 协调 rollout workers、trainer、reward models 与 replay buffer；
  replay buffer 持有 segment/trajectory state；etcd 持有 hybrid deployment global metadata；Checkpoint
  Engine 管 vLLM lifecycle 与 transferred model shards；sandbox 持执行环境 state。
- **Control Flow / Data Flow:** prompt→async rollout segments→replay buffer→reward/code execution→trainer
  update；train phase offload Megatron，Mooncake/RDMA 传 converted weights 给 vLLM→rollout→终止 vLLM
  释放 CUDA graph/NCCL/driver memory→恢复 training。
- **Implementation Details:** Kubernetes sidecars colocate Megatron/vLLM；shared-memory HF conversion 处理
  PP/EP 后保留 TP shards；Checkpoint Engine + etcd 广播状态；code sandbox 用 crun、cgroup reuse、
  tmpfs overlay。切换时间与 sandbox 数字是作者环境结果。
- **Evaluation Setup:** text、math/coding、vision reasoning；MMLU/IF-Eval/C-Eval、AIME 2024/MATH-500/
  LiveCodeBench/Codeforces、MMMU/MathVista/MathVision；long vs short CoT、context/model-size scaling、
  negative gradients、curriculum sampling 与 long2short 比较。
- **Baselines / Ablations / Sensitivity:** 与公开/闭源模型及 ReST/uniform sampling 比较；较小模型可用
  更长 CoT 追近较大模型，但较大模型通常 token-efficient；具体表格混合不同 provider/eval 来源，
  不能当严格同环境系统 benchmark。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 最终 RL context 128K；模型规模、
  training GPU 数、precision、global batch 和 rollout concurrency 未完整披露；sandbox 表基于 16-core
  machine；没有 production TTFT/TPOT SLO。
- **What the Evidence Actually Proves:** 作者系统把 variable-length rollout、weight handoff 与 executable
  reward 视为同一 RL data plane，并展示 partial rollout/hybrid deployment 的具体 state flow；long2short
  是 token-efficiency 分支，而非证明 long CoT 已无必要。
- **What It Does Not Prove:** 不证明 partial rollout 在任意 policy objective 下无 bias，不证明作者
  benchmark 等同开放域可靠性，也不证明 terminate/restart vLLM 是所有系统的最优资源回收方案。
- **Limitations / Threats to Validity:** proprietary model/data/cluster；没有独立复现；partial historical
  segments 的 staleness/importance correction 细节不足；conclusion 明确长-context RL efficiency、
  credit assignment 与 overthinking 仍未解决。
- **Trade-offs / New Failure Modes:** 分段减少 straggler，却引入 trajectory identity、buffer consistency、
  stale prefix 与 loss masking；colocation 提高 utilization，却增加 lifecycle coordination、weight format
  conversion、global metadata 和 restart failure；sandbox 成为安全/容量边界。
- **Where the Previous Design Still Applies:** 短 rollout 可直接同步生成；严格 on-policy 要求高时可拒绝
  historical reuse；独立 training/inference pools 在隔离与易运维优先时仍合理；long CoT 在高难任务仍
  是探索分支。
- **Evolution Relationship:** `Principle Reuse` with R1 on reasoning RL；在 system 层形成完整 rollout
  state lifecycle，不是 GRPO 或 R1 的同义实现。
- **ROADMAP Node:** Ch29（reasoning RL boundary）与 Ch31（state/checkpoint）候选；Ch34/36/37 负责
  parallel/runtime；Ch52/59 只接资源调度 handoff。
- **Target and Adjacent Chapters Read:** 已读 Ch27～37，重点 Ch29、31、32、34、36/37；并核对
  Ch46、Ch52 与 Ch59 的 inference/cluster scheduling 边界。
- **Existing Coverage:** Ch29 已有 rollout/update pipeline 但未展开 partial rollout；Ch31 已定义 RLHF
  多模型 consistent snapshot；是否加入 k1.5 案例需与后续 RL runtime 候选去重。
- **Integration Decision:** `Refine — Existing Argument`；主 owner Ch29，新增 partial-rollout trajectory lifecycle。
  是 rollout state ownership 与 lifecycle，不是 model benchmark。
- **Changed Files or Rejection Reason:** 已更新 `books/part-03-training-system/29-grpo.md`，保留 staleness、credit 与恢复边界。
- **Open Questions:** partial rollout 的 policy-lag correction、segment-level credit assignment、etcd/
  replay recovery、sandbox trust 与 train-inference artifact equivalence。

### Chain of Agents

- **Candidate / Week / Score:** Chain of Agents / 2025-W04 / 21/30。
- **Source Family ID:** `chain-of-agents-long-context-followup`。
- **Source Type:** 2024 NeurIPS/arXiv 作者论文 + 2025 Google Research 官方 follow-up Blog。
- **First-public Date / Revision History:** 论文 arXiv v1 首发 2024-06-04；Google Research Blog 发布
  2025-01-23。原 Weekly 把 Blog 日期当候选 first public，现纠正为“2025 官方 follow-up”，不是
  2025 新论文。
- **Direct Primary Sources:** https://arxiv.org/abs/2406.02818；
  https://arxiv.org/html/2406.02818；Google Research 官方 Blog。
- **Related Primary Sources:** NeurIPS 2024/OpenReview 页面；arXiv 正文作为可访问完整版本。
- **Access and Verification Status:** Verified；论文 method、experiment、analysis、ablation、limitations
  与 appendix 可读；closed model internals 与 API latency/cost 明细未披露。
- **Full-read Coverage:** 已读 metadata、Introduction/Related Work、Algorithm 1、worker/manager stages、
  complexity proof、9-dataset setup、RAG/full-context/multi-agent baselines、lost-in-middle analysis、
  manager/order/multi-path ablations、limitations、implementation appendix 与官方 Blog 全文。
- **Original Problem:** RAG 可能漏掉低语义相似度但必要的 hop；full context 超过 window 或出现
  lost-in-the-middle。问题是如何在有限窗口内遍历全部 source 并保留跨 chunk evidence。
- **Why the Previous Design Was Reasonable:** RAG 只读少量相关 chunks，成本低且 provenance 清晰；
  full context 避免显式摘要链，在长度可容纳且模型有效利用时保真；两者仍是强 baseline。
- **Changed Constraint:** source 长度超过单模型有效窗口，任务还要求跨 chunk multi-hop reasoning 或
  non-query summarization，单次 retrieval/query relevance 不足。
- **Mechanism:** 按原顺序切 chunks；worker `W_i` 接收 query、当前 chunk 与上一 worker 的自然语言
  communication unit `CU_{i-1}`，输出 `CU_i`；最后独立 manager 只读 `CU_l` 生成答案。论文理论上
  将 dense full-context encoding 从 `O(n^2)` 写为分块 `O(nk)`，但仍有逐 worker decoding/call latency。
- **State Ownership:** `CU_i` 是 chain-local derived message，由下一 worker 消费；manager 只拥有最终
  synthesis call。没有 durable authoritative shared state、retry log、tenant identity 或 provenance
  pointer contract。
- **Control Flow / Data Flow:** source→ordered chunks→sequential worker calls/压缩更新→final manager；
  multi-path variant 改变阅读顺序并用 vote/judge 聚合。串行 chain 的 critical path 随 chunk 数增长。
- **Implementation Details:** 同一 backbone 通常用于 workers/manager；8K worker window；task-specific
  instructions 让 CU 成为 evidence/summary/code summary。论文没有公开 production orchestration code
  或 failure recovery semantics。
- **Evaluation Setup:** HotpotQA、MuSiQue、NarrativeQA、Qasper、QuALITY、QMSum、GovReport、BookSum、
  RepoBench-P；PaLM 2 text-bison/unicorn、Gemini Ultra、Claude 3 Haiku/Sonnet/Opus；按任务使用 F1、
  exact match、ROUGE geometric mean 或 code similarity。
- **Baselines / Ablations / Sensitivity:** Vanilla full-context、RAG（300-word chunks + reranker）、parallel
  Merge、Hierarchical；ablation 去 manager、right-to-left/permutation、multi-path vote/judge；manager 与
  order 均显著影响结果，表明不是“多 agent 数量”本身产生收益。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 论文披露 model API/window 与
  dataset 平均长度/agent 数，但 hardware、precision、batch、concurrency、wall-clock latency、cost 和
  production SLO 均 Not Disclosed。
- **What the Evidence Actually Proves:** 在作者 9 datasets/6 models 设置中，顺序 communication+manager
  比所选 RAG/full-context/parallel multi-agent baselines 更好，并缓解部分 lost-in-the-middle；worker
  state compression 与 manager 分工是可被 ablation 的机制。
- **What It Does Not Prove:** 不证明输入“无限”可无损处理，不证明优于所有 modern long-context/RAG，
  不证明 communication unit 保留 provenance/correctness，也不证明 multi-agent 自主协作优于固定 workflow。
- **Limitations / Threats to Validity:** 论文承认 LLM-to-LLM communication 未专门训练、未探索 debate，
  cost/latency 仍需 routing 优化；serial summary error 可累积，closed APIs 与 benchmark metrics 限制复现。
- **Trade-offs / New Failure Modes:** 全 source traversal 换来线性 call/token cost和 serial latency；
  bounded CU 是信息瓶颈，早期误删不可恢复；顺序敏感、manager confusion、provider drift 与 retry
  duplication 成为新故障。
- **Where the Previous Design Still Applies:** query 可检索且证据稀疏时 RAG 更便宜；source 能完整放入
  effective context 且需要高保真时 full context 更简单；有结构化 state/parallelizable tasks 时 DAG/
  typed artifacts 优于自然语言串行链。
- **Evolution Relationship:** 与 long context/RAG 是 `Explanatory Analogy`；从系统角度更接近 fixed
  sequential workflow，不应因多次调用就写成 autonomous multi-agent replacement。
- **ROADMAP Node:** Ch71 主 owner 候选（context compression/derived state）；Ch72 对比 RAG；Ch78
  只接 coordination/message-state boundary。
- **Target and Adjacent Chapters Read:** 已读 Ch22、Ch70～73、Ch75～78；重点复核 Ch71/72/78。
- **Existing Coverage:** Ch71 已说明 compression loss、source links 与 typed state；Ch78 已说明 fixed
  role sequence 更像 workflow、message 不是 authoritative state。论文没有突破这些框架。
- **Integration Decision:** `No Change — Already Covered`；Ch71 的 compression/provenance 与 Ch78 的 topology/state 边界已覆盖。
  context compression 与 Ch78 message/state 具体段落完成去重。
- **Changed Files or Rejection Reason:** 不改 Books；论文没有证明链式摘要替代 long context 或 retrieval。
  一般的 context/workflow/multi-agent framework 覆盖，且论文是 2024 evidence。
- **Open Questions:** CU provenance/rollback、error detection、parallelism、retry idempotency、真实 API
  cost/SLO，以及后续 structured handoff 是否能缓解 serial information bottleneck。

## Evidence Level

- 官方 Blog / Release 只证明公开的产品、版本与项目事实；未公开实现标记为未知。
- arXiv v1 属于作者实验结论，默认 Status: Experimental，不等于独立复现或通用生产结论。
- 本周没有使用社区观点支撑机制结论；跨来源连接属于本项目推断，已通过 Evolution Relationship 标记。

## Cross-Week Deduplication

- 事件按 first-public date 归属本周；后续 revision、模型卡补充和工程集成回链本周，不重复创建新事件。
- 与前后周出现的同一技术只在年度索引建立演进关系，不把新版本写成对旧方案的静默替代。

## Knowledge Tree Position

- DeepSeek-R1 → 第 27～30 章、第 62 章（Direct Evolution）
- Kimi k1.5 → 第 22、27～29、34、62 章（Principle Reuse）
- Chain of Agents → 第 22、71、75、78 章（Explanatory Analogy）

## Recommended Action

- DeepSeek-R1：Must Read；Books Integration 前按最新版全文复核
- Kimi k1.5：Must Read；与 R1 形成 reasoning-RL 分支比较
- Chain of Agents：Worth Watching；作为长上下文系统分支

## Event-Date Daily Decision

历史回填不创建 Daily。事件日期与 evidence boundary 直接保留在本 Weekly。

## Books Integration Decision

Books Gate 已完成。该周候选的最终 disposition 已写入各自 Full Source Review；没有评分候选的周保持 No Material Update，不为制造 diff 修改 Books。


## Ignored Noise

- 未保留旧内容重发、缺少 primary source 的转述、未绑定 workload contract 的 benchmark 宣传和纯产品可用性更新。
- discovery 数据库的相关性排序与引用量不作为 Technical Novelty 或 Source Reliability 的替代指标。

## Repository Changes

- 新增 papers/2025/weekly/2025-W04/README.md。
- 更新 books/part-03-training-system/29-grpo.md。

## Open Questions

- 纯 outcome reward 在开放域、不可自动验证任务中的可扩展边界仍未解决。
- long-rollout 的训练收益如何与 serving reasoning budget 联合优化，仍需跨系统证据。
- Chain of Agents 的中间摘要错误能否被可靠检测和恢复，尚未验证。

## Sources

- DeepSeek-R1 — https://arxiv.org/abs/2501.12948（First Public: 2025-01-20 (release); 2025-01-22 (paper v1)；Accessed: 2026-07-31）
- Kimi k1.5 — https://arxiv.org/abs/2501.12599（First Public: 2025-01-22；Accessed: 2026-07-31）
- Chain of Agents paper — https://arxiv.org/abs/2406.02818（First Public: 2024-06-04；Accessed: 2026-07-31）
- Chain of Agents Google Research follow-up — https://research.google/blog/chain-of-agents-large-language-models-collaborating-on-long-context-tasks/（Published: 2025-01-23；Accessed: 2026-07-31）
