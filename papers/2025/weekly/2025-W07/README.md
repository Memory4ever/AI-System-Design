# AI Research Weekly — 2025-W07

> Coverage Window: 2025-02-10～2025-02-16
> Research Mode: Retrospective Backfill
> Accessed: 2026-07-31
> Backfilled: 2026-07-31

## Executive Summary

本周保留 2 项与长期 AI System 认知相关的证据：Online Scheduling for LLM Inference with KV Cache Constraints、Building AI for the pluralistic society。重点不是记录发布热度，而是识别其改变了哪一项约束、机制与系统 trade-off。所有结论均按首次公开时间归档，性能或能力数字不脱离作者披露的模型、硬件、精度、输入输出、并发与 SLO 条件使用。

## Coverage Window and Limitations

- 使用官方发布日期、GitHub Release 时间或 arXiv v1 时间；不使用搜索收录日和后续修订日替代 first-public date。
- Google Scholar、OpenAlex、DBLP 用于 discovery、去重和引用链检查；论文机制回到 arXiv / 作者正文。
- Crossref 仅用于 Weekly metadata 交叉检验，不作为机制证据。
- 本周为历史回填，不补造 Daily；访问日期统一为 2026-07-31。
- 厂商 benchmark 和论文实验只代表其披露条件，缺少完整 workload contract 时不做跨系统性能结论。

## 1. 模型与研究机构

### Source Coverage

按固定机构顺序扫描 OpenAI、Anthropic、Apple、Google、Meta、Microsoft、NVIDIA、xAI、Amazon、Cohere、Ai2、Mistral、Qwen、DeepSeek、Kimi、Zhipu、MiniMax、Seed、ERNIE、Hunyuan、Huawei Noah、InternLM、StepFun、MiMo、InclusionAI 与 Hugging Face Blog。

- 保留：Building AI for the pluralistic society（2025-02-13）。

## 2. 论文与学术来源

按 arXiv → Google Scholar → OpenAlex → DBLP 发现与去重，回到论文 v1 正文核验；Crossref 只做 metadata 交叉检查。

- 保留：Online Scheduling for LLM Inference with KV Cache Constraints（2025-02-10）。
- 保留：Native Sparse Attention（2025-02-16）。

## 3. AI Infra 与工程项目

按固定工程顺序扫描 PyTorch、JAX、CUDA、Triton、vLLM、SGLang、NVIDIA Dynamo、TensorRT-LLM、Ray、KServe、Kubeflow、Kubernetes、Transformers、Accelerate、DeepSpeed、Megatron-LM、Unsloth、MLX、llama.cpp、ONNX Runtime 与 OpenXLA。

- 本组无达到保留门槛的候选。

## Candidate Scoring

| Candidate | Technical Novelty | System Impact | Practical Value | Source Reliability | Project Relevance | Longevity | Total | Decision |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| Online Scheduling for LLM Inference with KV Cache Constraints | 4 | 4 | 4 | 4 | 5 | 3 | 24/30 | Must Read；作为调度第一性原理候选 |
| Building AI for the pluralistic society | 3 | 3 | 3 | 4 | 4 | 3 | 20/30 | Worth Watching；Weekly only，等待更强工程证据 |
| Native Sparse Attention | 5 | 4 | 4 | 5 | 5 | 4 | 27/30 | Must Read；与 MiniMax-01 和后续 DSA 形成演进链 |

### Deep Analysis 1 — Online Scheduling for LLM Inference with KV Cache Constraints

- First Public: 2025-02-10
- Status: arXiv v1; Experimental
- Primary Source: https://arxiv.org/abs/2502.07115
- Evolution Relationship: Principle Reuse

#### Why

连续批处理中的调度不是普通排队：请求的服务时间、KV 占用和未来 token 数互相耦合。

#### Principle and Mechanism

论文分别建模 semi-online 与 stochastic online 到达，给出平均延迟优化算法和理论边界。

#### Trade-off and Evidence Boundary

理论结果澄清了可优化范围，也证明 adversarial fully-online 情况不存在常数 competitive ratio；经验结果只绑定 Llama-70B、A100 与论文工作负载。

#### Connection and Evolution

知识树位置：第 41～43、50、52 章。Must Read；作为调度第一性原理候选。后续若进入 Books，必须保留旧方案仍成立的条件，并把作者实验、官方版本事实和本项目推断分开。

### Deep Analysis 2 — Building AI for the pluralistic society

- First Public: 2025-02-13
- Status: Google Research official blog + research
- Primary Source: https://research.google/blog/building-ai-for-the-pluralistic-society/
- Evolution Relationship: Principle Reuse

#### Why

单一聚合偏好会把真实价值冲突压成虚假的平均答案。

#### Principle and Mechanism

研究讨论 pluralistic alignment 与 mechanism-design 视角，把不同群体偏好和社会选择规则显式纳入目标。

#### Trade-off and Evidence Boundary

表达多元偏好会增加标注、聚合与治理复杂度，也不能自动解决不可调和冲突。

#### Connection and Evolution

知识树位置：第 27、30、62、68 章。Worth Watching；Weekly only，等待更强工程证据。后续若进入 Books，必须保留旧方案仍成立的条件，并把作者实验、官方版本事实和本项目推断分开。

### Deep Analysis 3 — Native Sparse Attention

- First Public: 2025-02-16
- Status: arXiv v1; Experimental
- Primary Source: https://arxiv.org/abs/2502.11089
- Evolution Relationship: Direct Evolution

#### Why

稀疏注意力若只在 dense model 训练后裁剪，既难让模型适应稀疏模式，也常与 GPU memory
hierarchy 不匹配。

#### Principle and Mechanism

NSA 将 compressed coarse-grained selection、fine-grained token selection 与 sliding
window 组合，并从训练阶段原生使用可由硬件友好 kernel 执行的稀疏结构。

#### Trade-off and Evidence Boundary

减少长序列计算并保留局部与全局路径，但引入索引选择、负载不规则和专用 kernel 依赖；
等质量边界必须按长度与任务验证。

#### Connection and Evolution

知识树位置：第 14、22、45、50 章。Must Read；与 MiniMax-01 和后续 DSA 形成演进链。
后续若进入 Books，必须保留旧方案仍成立的条件，并把作者实验、官方版本事实和本项目推断分开。

## Full Source Review

### Online Scheduling for LLM Inference with KV Cache Constraints

- **Candidate / Week / Score:** Online Scheduling for LLM Inference with KV Cache Constraints /
  2025-W07 / 24/30。
- **Source Family ID:** `kv-constrained-online-llm-scheduling`。
- **Source Type:** arXiv 作者论文；理论模型与 trace-driven simulation。
- **First-public Date / Revision History:** v1 2025-02-10；v2 2025-02-13；v3 2025-03-05
  withdrawn；v4 2025-05-20；v5 2026-01-15。按 latest v5 阅读，归档仍以 v1 为准。
- **Direct Primary Sources:** https://arxiv.org/abs/2502.07115；
  https://arxiv.org/html/2502.07115。
- **Related Primary Sources:** 论文引用的 continuous batching、KV-cache management 与 Vidur simulator
  工作只定义比较语境，不替代本文证明。
- **Access and Verification Status:** Verified；正文、定理、算法、实验与 appendix 可访问。v3 withdrawal
  是 revision history，不表示 latest v5 仍为 withdrawn。
- **Full-read Coverage:** 已读 metadata/revisions、Introduction/Related Work、problem formulation、offline IP、
  adversarial impossibility、semi-online/stochastic model、MC-SF algorithm/complexity/proofs、synthetic 与
  LMSYS/Vidur experiments、output prediction error、discussion、conclusion 与相关 appendices。
- **Original Problem:** continuous batching 中 request 的剩余服务时间与 KV 占用随输出长度同时增长；
  调度器既要缩短平均 flow time，又不能让未来 KV 增长突破显存容量。
- **Why the Previous Design Was Reasonable:** FCFS、shortest-job-first 或“有空位就 admission”在服务时间
  已知或 memory footprint 固定时简单且低开销；真实 serving 中 preemption/recompute 也可用资源换灵活性。
- **Changed Constraint:** LLM 输出长度未知，active request 的 KV footprint 随 token 增长；错误 admission
  可能使未来批次不可行，而 adversarial fully-online arrivals 使任何 deterministic algorithm 都无
  workload-independent 常数 competitive ratio。
- **Mechanism:** 作者先以 integer program 定义 hindsight optimum，再提出 Memory-Constrained Shortest-
  First（MC-SF）：优先保留 active requests，在每轮按预测 output length 从短到长填充 batch，同时检查
  所选 requests 的未来 KV growth 是否仍满足 memory feasibility；structured arrival/prediction 假设下给出
  competitive bounds。
- **State Ownership:** 单 worker scheduler 拥有 waiting/active set、预测 output length 与 memory budget；
  每个 request 拥有 prompt size、已生成 tokens 和剩余 service estimate。模型未定义 distributed ownership、
  replicated KV 或 admission lease。
- **Control Flow / Data Flow:** arrivals→waiting queue→每个 unit-time round 先保留 active requests→按 shortest
  predicted output 尝试 admission→future-memory check→selected batch 生成一个 token→更新 KV/remaining work→
  completion release memory。
- **Implementation Details:** paper model 假设 once-started non-preemptive、每个 batch round 单位时间、单 worker
  容量 `M`；MC-SF 逐轮最坏 `O(M^2)`。这不是 vLLM/SGLang production scheduler implementation。
- **Evaluation Setup:** synthetic 中 `M=30–50`、prompt size 1–5、output 1 到 `M-s`、200 trials；trace-driven
  使用 LMSYS-Chat-1M 的 10K subset，以 words proxy tokens，在两张互联 A100 上的 Llama-2-70B 参数经
  Vidur simulation，比较 all-at-once 与 Poisson arrivals。
- **Baselines / Ablations / Sensitivity:** 比较 hindsight optimum、FCFS、SJF/MC-SF variants；prediction error
  取 `epsilon=0.2/0.5/0.8`，并测试约 10% reserve。作者的平均 ratio 接近 1 只属于这些 simulated
  distributions，不是 production tail guarantee。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** hardware 为 2×A100，model
  Llama-2-70B；precision、tensor parallel details、真实 tokenization、batch/concurrency cap 与 TTFT/TPOT
  SLO 未构成完整 contract。实验把 words 当 tokens，且由 simulator 产生，不是 live serving measurement。
- **What the Evidence Actually Proves:** adversarial unknown-output scheduling 存在理论不可优化边界；在论文
  的单 worker、non-preemptive、bounded prediction assumptions 下，显式 future-KV feasibility 与 shortest-
  first 可以得到理论界，并在作者 simulation 中接近 hindsight optimum。
- **What It Does Not Prove:** 不证明 MC-SF 是 production 最优策略，也不覆盖 multi-worker routing、prefix
  reuse、chunked prefill、preemption/recompute、heterogeneous models、fairness、priority 或 tail-SLO。
- **Limitations / Threats to Validity:** output upper-bound prediction 是关键假设；underestimate 可触发 cache
  clearing、evict/requeue/retry；真实 arrival/length correlation、token latency 与 scheduler overhead 被简化；
  trace experiment 是 simulation。
- **Trade-offs / New Failure Modes:** future-feasibility 减少 memory dead-end，却可能保守 admission、牺牲长
  request fairness；shortest-first 会 starvation；reserve 抗误差但降低 utilization；`O(M^2)` selection 与预测
  drift 增加 control-plane cost。
- **Where the Previous Design Still Applies:** 输出短且窄分布、memory 富余或 fairness/priority 更重要时，
  FCFS/round-robin 仍合理；支持抢占/重算的 runtime 可选择更激进 admission；offline/batch workload 可用
  全局优化而非 online heuristic。
- **Evolution Relationship:** `Principle Reuse`：从只看当前 free blocks，演进到把 future KV growth 作为
  admission invariant；并非指定某个框架必须实现 MC-SF。
- **ROADMAP Node:** Ch52 主 owner；Ch41～43 提供 batching/KV phase 前提，Ch50 提供 memory contract。
- **Target and Adjacent Chapters Read:** 已读 Ch41～43、Ch50～52，核对 continuous batching、KV ownership、
  SLO/fairness 与 admission control 的既有论述。
- **Existing Coverage:** Ch52 已覆盖 workload-aware scheduling 与公平性，但需在 Evidence Gate 后判断是否
  欠缺“未来 KV 可行性不是当前容量检查”的形式化解释；不能把论文算法直接写成 production prescription。
- **Integration Decision:** `Refine — Existing Argument`；主 owner Ch52，只吸收 impossibility 与 future-KV feasibility。
  future-feasibility invariant 与 prediction/fairness trade-off。
- **Changed Files or Rejection Reason:** 已更新 `books/part-04-inference-system/52-inference-scheduling.md`；MC-SF 不写成生产处方。
- **Open Questions:** multi-worker/prefix-aware extension、prediction calibration、preemption cost、tail SLO、
  priority/fairness 与 scheduler complexity 如何共同进入 workload contract。

### Building AI for the pluralistic society

- **Candidate / Week / Score:** Building AI for the pluralistic society / 2025-W07 / 20/30。
- **Source Family ID:** `google-pluralistic-annotation-and-evaluation`。
- **Source Type:** Google Research synthesis Blog + linked peer-reviewed primary papers/datasets。
- **First-public Date / Revision History:** synthesis Blog 2025-02-13；核心证据来自 2021、2023、2024 的
  DICES、GRASP、D3/D3CODE、diversity-aware annotation 等工作；不是一项全新的 2025 experiment。
- **Direct Primary Sources:** https://research.google/blog/building-ai-for-the-pluralistic-society/；
  https://aclanthology.org/2024.naacl-long.190/；
  https://aclanthology.org/2024.safety4convai-1.2/；
  https://research.google/pubs/dices-dataset-diversity-in-conversational-ai-evaluation-for-safety/。
- **Related Primary Sources:** https://aclanthology.org/2021.law-1.14/；Blog 所列 FAccT 2024 cross-cultural
  analysis、D3CODE/DICES repositories 与 multi-perspective modeling paper。
- **Access and Verification Status:** Verified as a synthesis family；ACM PDF 对自动访问返回 403，但 Blog、
  ACL papers、DICES publication/repository 和公开 metadata 足以核验本文使用的机制边界；被阻挡的 PDF
  不作为独占 claim 依据。
- **Full-read Coverage:** 已读 Blog 全文及 linked GRASP 20 页、diversity-aware annotation 8 页、annotator-
  level release 6 页；核对 datasets、metrics、simulation setup/results、ethical considerations、limitations、
  privacy 风险与 Blog 的 controllable/extensible/transparent value framing。
- **Original Problem:** subjective safety/offensiveness labels 常被 majority vote/average 压成单一 ground
  truth，从而把稳定的群体分歧误当 annotation noise，并可能静默抹去 minoritized perspectives。
- **Why the Previous Design Was Reasonable:** 单标签便于 supervised training、inter-rater agreement 与标准
  accuracy；对客观或由 policy 明确定义的任务，专家 adjudication/aggregation 仍可降低噪声和成本。
- **Changed Constraint:** 全球部署与 safety evaluation 需要识别 socio-cultural 与 intersectional variation；
  但对每个 item 做高 replication annotation 成本过高，且并非所有 demographic axes 对每个 task 都相关。
- **Mechanism:** GRASP 用 in-group/cross-group cohesion、group association index 与 permutation significance
  test 找出 task-specific group associations；diversity-aware protocol 先以高 replication pilot 找敏感群体，
  再按 target policy 动态 upsample relevant raters；保留 annotator-level labels 让下游显式选择聚合规则。
- **State Ownership:** dataset owner 持有匿名 annotator-level label、demographic attributes、content category
  和 collection consent；policy owner 必须显式拥有 target metric（如 recall/precision）与 aggregation rule；
  model 不应隐式成为价值冲突的唯一 owner。
- **Control Flow / Data Flow:** pilot items+parallel ratings→GRASP/association detection→按 content type 选择
  relevant rater groups→assignment policy 采样 full-scale annotations→保存分布而非只保存 majority label→
  按 deployment policy 训练/评测并审计 subgroup effects。
- **Implementation Details:** diversity-aware paper 在 DICES-350 上做 1,000 次 simulation：50 pilot、300 test，
  每项从 identified group 至少 3/5 raters；gold 由每项约 120 ratings 构造。GRASP 分析 DICES-350 与 D3，
  permutation tests 避免不成立的 independence assumption。
- **Evaluation Setup:** DICES-350 为 350 conversations 的高 replication safety labels；D3 为 4,554 items、
  4,309 raters、每 item 24 ratings，覆盖 8 geo-cultural regions。simulation 优化 unsafe recall，不是 live
  data-collection trial。
- **Baselines / Ablations / Sensitivity:** stratified-random rater assignment 为 baseline；论文报告 recall
  79.5→83.0、precision 96.5→96.3，但 gold threshold 使 92% items 为 unsafe，且只测试一个 dataset/
  target policy；结果不得泛化成“diversity 一定无损 precision”。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 这是 socio-technical data/evaluation
  study，不涉及 model hardware/precision/serving SLO；计算成本主要来自 annotation replication 与
  permutation tests，公开论文未给统一 infrastructure contract。
- **What the Evidence Actually Proves:** 在两个 datasets 中可检测到 task-dependent/intersectional systematic
  disagreement；在特定 DICES simulation 与 recall policy 下，targeted rater assignment 比已分层的随机池
  提高 recall、几乎不改变 precision。
- **What It Does Not Prove:** 不证明 demographic group 内观点同质，不证明所有分歧都应保留或本地化，
  不解决不可调和价值冲突，也不证明 2025 Blog 提供了新的 alignment algorithm。
- **Limitations / Threats to Validity:** demographic buckets 简化身份；single-dataset simulation、人工 harm
  categories、target threshold 和 US-heavy DICES 限制外推；收集 identity 增加 privacy/consent/re-identification；
  group association 只定位差异，不解释原因。
- **Trade-offs / New Failure Modes:** 可见性与 minority recall 提升，代价是 collection cost、policy choice、
  demographic data protection、small-group statistical instability、stereotyping 与治理争议；动态 sampling
  还可能把旧 association 固化为 future allocation bias。
- **Where the Previous Design Still Applies:** 客观标注、专家知识或法律/平台已确定唯一 policy 时，
  prescriptive labels/adjudication 仍合理；低风险探索可先用随机多样池，再由 evidence 决定是否 targeted。
- **Evolution Relationship:** `Principle Reuse`：从“disagreement=measurement noise”演进到“disagreement
  可能是需建模与治理的 signal”；不是 majority vote 的全面否定。
- **ROADMAP Node:** Ch62 主 owner（evaluation contract/rater uncertainty）；Ch68 接 demographic data 与
  governance risk；Ch27/30 仅作 alignment handoff。
- **Target and Adjacent Chapters Read:** 已读 Ch27、30、61～69，重点核对 Ch62 与 Ch68 对 rater distribution、
  policy owner、privacy 和 evidence boundary 的覆盖。
- **Existing Coverage:** 现有 Ch62 已要求拆分 model/harness/rater uncertainty，Ch68 已覆盖隐私与治理；
  该 source family 可能提供具体机制案例，但尚未证明应修改 core conclusion。
- **Integration Decision:** `No Change — Already Covered`；Ch62 已要求保留 rater distribution/uncertainty，Ch68 已有治理边界。
  后续 rater-uncertainty sources 去重。
- **Changed Files or Rejection Reason:** 不改 Books；2025 Blog 是既有论文族的综合说明，没有新增独立机制。
- **Open Questions:** policy owner 如何民主/合规地产生，如何保护 demographic attributes，如何处理小群体
  power、时间漂移与 mutually incompatible preferences。

### Native Sparse Attention

- **Candidate / Week / Score:** Native Sparse Attention / 2025-W07 / 27/30。
- **Source Family ID:** `native-sparse-attention-to-deepseek-dsa`；后续与 DeepSeek-V3.2-Exp/DSA/V3.2 联读。
- **Source Type:** arXiv 作者论文；algorithm+Triton kernel+author evaluation。
- **First-public Date / Revision History:** v1 2025-02-16；v2 2025-02-27。按 v2 阅读。
- **Direct Primary Sources:** https://arxiv.org/abs/2502.11089；
  https://arxiv.org/html/2502.11089。
- **Related Primary Sources:** FlashAttention-2、GQA、DeepSeekMoE 及 H2O/InfLLM/Quest/Exact-Top 定义 baseline；
  后续 DSA papers/releases 不能倒推 NSA 的 production adoption。
- **Access and Verification Status:** Verified；正文、公式、kernel design、evaluation、discussion 与 appendix
  可访问；未发现作者公开的完整训练/kernel artifact，因此复现状态 Not Disclosed。
- **Full-read Coverage:** 已读 metadata/revisions、Introduction/Related Work、inference-only sparse attention
  failure、trainability、三分支公式、GQA-shared selection、Triton kernel、pretraining setup、general/LongBench/
  AIME evaluations、baselines、training/decoding efficiency、alternative failures、visualization、conclusion。
- **Original Problem:** post-hoc sparse/eviction 既让 pretrained model 在 inference 偏离训练分布，也无法
  降低 long-context training 成本；token-level random gather 虽稀疏却可能比 dense block kernel 更不适合 GPU。
- **Why the Previous Design Was Reasonable:** full attention 提供连续、可微、易由 FlashAttention 优化的标准
  path；inference-only pruning 无需重训已有 checkpoint；fixed window/sink pattern 简单且延迟可预测。
- **Changed Constraint:** long-context pretraining/SFT/RL 也要降计算；sparsity 必须在训练时可学习，同时访问
  pattern 要匹配 Tensor Core、SRAM/HBM 与 GQA shared-KV 的数据复用。
- **Mechanism:** 三个独立 K/V branch：learned overlapping block compression 提供 coarse global path；复用
  compression attention scores 做 top-n continuous-block selection 提供 fine-grained path；sliding window
  隔离 local shortcut。GQA group 内汇总 importance、共享 selected blocks，三路输出由 learned gates 聚合。
- **State Ownership:** model parameters 拥有 compression MLP、branch K/V 与 gates；每 token/query 的
  compression score 推导 selection indices；runtime/kernel 拥有 sparse block index 与 KV layout；window/
  selected/compressed state 生命周期不同，不能把 selector 当无状态算子。
- **Control Flow / Data Flow:** K/V sequence→overlapping compression blocks→query-compressed attention scores→
  映射并汇总为 selection-block scores→GQA-group top-n continuous blocks；并行读取 local window→三 branch
  attention→gate aggregation。训练端梯度经 branch/gates 流动，top-n 本身仍是离散选择。
- **Implementation Details:** selection kernel 以 GQA group 为 query load 单位，将共享、连续 KV blocks 拉入
  SRAM，并把 query/output loop 放到 Triton grid；目标是消除跨 heads 的重复 KV transfer并平衡 SM work。
  compression/sliding branches复用 FlashAttention-2-compatible kernels。
- **Evaluation Setup:** 27B total/3B active、30 layers、hidden 2560；GQA 4 groups/64 heads，q/k 192、v 128；
  MoE 72 routed+2 shared、top-6；270B×8K tokens pretrain，再以 YaRN continued training/SFT 到 32K；NSA
  `l=32,d=16,l'=64,n=16,w=512`，与 full-attention model 训练到 convergence。
- **Baselines / Ablations / Sensitivity:** full attention、H2O、InfLLM、Quest、Exact-Top；LongBench 统一
  sparsity；另以 3B model 比 clustering、auxiliary-loss/heuristic block selection 与 cold-start 1000 steps。
  未提供对 l/d/n/w、gate、每 branch 的完整 sensitivity，也无不同 hardware generation portability study。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** efficiency 为 8×A100、同为 Triton
  NSA vs Triton FlashAttention-2；64K 报告 forward 最高 9×、backward 6×。decoding 的 11.6×是按 KV
  access volume 得到的 expected speedup，不是同等完整 end-to-end measured latency；precision/batch/SLO
  未完整披露。
- **What the Evidence Actually Proves:** 在作者 27B/3B training/eval contract 中，native sparse model 可稳定
  收敛并在 general/long-context/reasoning tests 与 full attention 可比或更好；硬件 aligned continuous-block
  pattern 在同 backend microbenchmark 降低 attention forward/backward cost。
- **What It Does Not Prove:** 不证明 NSA 普遍优于 full attention、不证明 reasoning gain 来自 sparsity 而非
  stochastic/training effects、不证明 expected decoding speedup 等于 production TTFT/TPOT/goodput，也不证明
  selector 对所有 domains/lengths 保留关键 token。
- **Limitations / Threats to Validity:** author-only experiment、单 architecture family 与 A100；缺 independent
  replication/code artifact；top-n selection、gate collapse、selector miss 与跨硬件 kernel portability 没有充分
  sensitivity；论文没有独立 limitations section。
- **Trade-offs / New Failure Modes:** 获得 lifecycle-wide sparsity，却增加 compression/selection/window 三份
  K/V parameters/state、index generation、special kernel 与 tuning surface；shared GQA selection 提升 reuse 但
  可能牺牲 per-head recall；selector miss 是静默质量故障，kernel/layout mismatch 会吞掉理论 sparsity 收益。
- **Where the Previous Design Still Applies:** 短 context、未重训 checkpoint、kernel portability优先或 quality
  risk 不可接受时 full attention 仍合理；fixed window/eviction 适合 streaming 或 inference-only retrofit；
  dense attention 是验证 selector recall 的必要 reference path。
- **Evolution Relationship:** `Direct Evolution`：post-hoc sparse inference→trainable、hardware-aligned lifecycle
  sparsity；后续 DSA 若改变 selector mechanism，应保留 NSA 的问题定义与共存条件而非覆盖。
- **ROADMAP Node:** Ch22 主 owner；Ch14 提供 attention math，Ch45 提供 kernel mapping，Ch50 提供 KV/memory
  handoff。
- **Target and Adjacent Chapters Read:** 已读 Ch14、Ch21～23、Ch44～46、Ch49～50；重点重新核对当前
  provisional Ch22 NSA 段落与前后 attention evolution。
- **Existing Coverage:** Ch22 已有 NSA provisional integration，但需在 Evidence Gate 后修正 11.6×为
  expected memory-volume result，并确保三分支 state、GQA shared selection、old-design validity 与 unknowns
  完整表达。
- **Integration Decision:** `Refine — Existing Argument`；主 owner Ch22，与 DSA family 联读。
  才能最终判定。
- **Changed Files or Rejection Reason:** 已复核 `books/part-02-model/22-long-context.md` 的 learned sparsity、kernel alignment 与 selector failure。
- **Open Questions:** selector recall/quality telemetry、index/gate checkpoint compatibility、跨 H100/Blackwell/
  non-NVIDIA kernel portability、end-to-end serving gain、DSA 如何继承或改变 state ownership。

## Evidence Level

- 官方 Blog / Release 只证明公开的产品、版本与项目事实；未公开实现标记为未知。
- arXiv v1 属于作者实验结论，默认 Status: Experimental，不等于独立复现或通用生产结论。
- 本周没有使用社区观点支撑机制结论；跨来源连接属于本项目推断，已通过 Evolution Relationship 标记。

## Cross-Week Deduplication

- 事件按 first-public date 归属本周；后续 revision、模型卡补充和工程集成回链本周，不重复创建新事件。
- 与前后周出现的同一技术只在年度索引建立演进关系，不把新版本写成对旧方案的静默替代。

## Knowledge Tree Position

- Online Scheduling for LLM Inference with KV Cache Constraints → 第 41～43、50、52 章（Principle Reuse）
- Building AI for the pluralistic society → 第 27、30、62、68 章（Principle Reuse）
- Native Sparse Attention → 第 14、22、45、50 章（Direct Evolution）

## Recommended Action

- Online Scheduling for LLM Inference with KV Cache Constraints：Must Read；作为调度第一性原理候选
- Building AI for the pluralistic society：Worth Watching；Weekly only，等待更强工程证据
- Native Sparse Attention：Must Read；与 MiniMax-01 和后续 DSA 形成演进链

## Event-Date Daily Decision

历史回填不创建 Daily。事件日期与 evidence boundary 直接保留在本 Weekly。

## Books Integration Decision

Books Gate 已完成。该周候选的最终 disposition 已写入各自 Full Source Review；没有评分候选的周保持 No Material Update，不为制造 diff 修改 Books。


## Ignored Noise

- 未保留旧内容重发、缺少 primary source 的转述、未绑定 workload contract 的 benchmark 宣传和纯产品可用性更新。
- discovery 数据库的相关性排序与引用量不作为 Technical Novelty 或 Source Reliability 的替代指标。

## Repository Changes

- 新增 papers/2025/weekly/2025-W07/README.md。
- 更新 books/part-02-model/22-long-context.md。

## Open Questions

- fully-online、未知输出长度下的调度仍没有 workload-independent 最优策略。
- pluralistic preference aggregation 的 policy owner 与审计 contract 仍待工程证据。
- NSA 的 selector quality、irregular load 与跨硬件 kernel portability 仍需独立验证。

## Sources

- Online Scheduling for LLM Inference with KV Cache Constraints — https://arxiv.org/abs/2502.07115（First Public: 2025-02-10；Accessed: 2026-07-31）
- Building AI for the pluralistic society — https://research.google/blog/building-ai-for-the-pluralistic-society/（First Public: 2025-02-13；Accessed: 2026-07-31）
- Native Sparse Attention — https://arxiv.org/abs/2502.11089（First Public: 2025-02-16；Accessed: 2026-07-31）
