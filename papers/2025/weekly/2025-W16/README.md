# AI Research Weekly — 2025-W16

> Coverage Window: 2025-04-14～2025-04-20
> Research Mode: Retrospective Backfill
> Accessed: 2026-07-31
> Backfilled: 2026-07-31

## Executive Summary

本周保留 2 项长期证据：OpenAI o3 and o4-mini、MIRAS。前者把工具选择纳入 reasoning runtime，后者把 Titans 的具体 test-time memory 架构推广为可比较的记忆设计空间。

## Coverage Window and Limitations

- 以官方发布日期、GitHub Release 或 arXiv v1 归档；搜索收录日与后续修订不替代 first-public date。
- Google Scholar、OpenAlex、DBLP 用于 discovery 与去重；论文机制回到正文。Crossref 仅做 Weekly metadata 交叉检查。
- 历史回填不补造 Daily；Accessed 统一为 2026-07-31。
- benchmark 缺少模型、硬件、长度、batch/concurrency、precision/quantization 与 SLO 时不做通用结论。

## 1. 模型与研究机构

### Source Coverage

按固定机构顺序扫描 OpenAI、Anthropic、Apple、Google、Meta、Microsoft、NVIDIA、xAI、Amazon、Cohere、Ai2、Mistral、Qwen、DeepSeek、Kimi、Zhipu、MiniMax、Seed、ERNIE、Hunyuan、Huawei Noah、InternLM、StepFun、MiMo、InclusionAI 与 Hugging Face Blog。

- 保留：OpenAI o3 and o4-mini（2025-04-16）。

## 2. 论文与学术来源

按 arXiv → Google Scholar → OpenAlex → DBLP 发现与去重，回到 v1 正文核验；Crossref 只做 metadata 交叉检查。

- 保留：It's All Connected: A Journey Through Test-Time Memorization, Attentional Bias, Retention, and Online Optimization（MIRAS，arXiv v1：2025-04-17）。

## 3. AI Infra 与工程项目

按固定工程顺序扫描 PyTorch、JAX、CUDA、Triton、vLLM、SGLang、Dynamo、TensorRT-LLM、Ray、KServe、Kubeflow、Kubernetes、Transformers、Accelerate、DeepSpeed、Megatron-LM、Unsloth、MLX、llama.cpp、ONNX Runtime 与 OpenXLA。

- 本组无达到保留门槛的候选。

## Candidate Scoring

| Candidate | Technical Novelty | System Impact | Practical Value | Source Reliability | Project Relevance | Longevity | Total | Decision |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| OpenAI o3 and o4-mini | 4 | 4 | 4 | 4 | 5 | 3 | 24/30 | Must Read；只沉淀 tool-in-reasoning 的系统边界 |
| MIRAS | 5 | 5 | 4 | 5 | 5 | 2 | 26/30 | Must Read；与 W01 Titans 联读，沉淀设计空间而非榜单结果 |

### Deep Analysis 1 — OpenAI o3 and o4-mini

- First Public: 2025-04-16
- Status: Official release + system card; vendor evaluation
- Primary Source: https://openai.com/index/introducing-o3-and-o4-mini/
- Evolution Relationship: Direct Evolution

#### Why

reasoning model 从仅延长内部推理演化为在推理过程中选择并组合工具，系统能力开始由 model policy 与 tool runtime 共同决定。

#### Principle and Mechanism

官方材料披露 reasoning effort、tool access、system-level monitors 与评测脚手架；训练和路由实现未公开。

#### Trade-off and Evidence Boundary

工具可提高可验证任务能力，也引入权限、数据外泄、执行副作用、环境差异和 benchmark contamination；不能把 model score 与 agent system score混为一谈。

#### Connection and Evolution

知识树位置：第 20、29、52、62、68、74 章。Must Read；只沉淀 tool-in-reasoning 的系统边界。后续若进入 Books，必须保留旧方案仍成立的条件，并把作者实验、官方版本事实和本项目推断分开。

### Deep Analysis 2 — MIRAS

- First Public: 2025-04-17（arXiv v1）
- Status: Experimental；作者论文
- Primary Source: https://arxiv.org/abs/2504.13173
- Evolution Relationship: Direct Evolution

#### Why

Titans 证明了一种 test-time neural memory 路线，但单个架构还不能回答哪些设计选择是本质的、
哪些只是实现组合。MIRAS 的问题是建立一个能同时比较 recurrent、linear attention、
test-time learning 与 retention 机制的坐标系。

#### Principle and Mechanism

论文把 sequence memory 拆成 memory architecture、attentional bias、retention gate 与
optimization algorithm 四类选择，使“写什么、保留什么、如何更新、怎样读取”可以独立推理，
再以具体变体验证该设计空间。

#### Trade-off and Evidence Boundary

统一抽象能暴露方案之间的共性，却不意味着组合空间里的每个选择都能高效实现。在线优化仍引入
稳定性、状态隔离与恢复成本；实验比较绑定作者的模型、数据和训练条件，不得外推为通用排序。

#### Connection and Evolution

知识树位置：第 14、22、73 章。它是 W01 Titans 的 `Direct Evolution`，不是对 attention、
SSM 或 retrieval 的替代宣言；第 22 章吸收设计原则，第 73 章仅解释模型内部状态与 Agent
durable memory 的语义边界。

## Full Source Review

### OpenAI o3 and o4-mini

- **Candidate / Week / Score:** OpenAI o3 and o4-mini / 2025-W16 / 24/30。
- **Source Family ID:** `openai-o3-o4mini-2025-04`。
- **Source Type:** 官方产品发布、33 页 System Card；没有公开 technical report、训练代码或模型权重。
- **First-public Date / Revision History:** 发布与 System Card 均为 2025-04-16；发布页后来加入 o3-pro 更新，System Card 在线版也有后续 addenda，本审计只把 2025-04-16 的 launch evidence 归入本周。
- **Direct Primary Sources:** OpenAI release；OpenAI o3/o4-mini System Card PDF。
- **Related Primary Sources:** OpenAI Preparedness Framework v2；后续 Codex/Operator addenda 只用于识别 source family，不反投影到 launch model。
- **Access and Verification Status:** Verified；发布页与 33 页 System Card 已读完。内部训练、router 和 tool-policy 实现未公开。
- **Full-read Coverage:** release 的 reasoning、vision、tool use、benchmark conditions、access；System Card 的 disallowed-content、jailbreak、vision、bias、第三方评估、CBRN/cyber/autonomy/self-improvement、SWE-bench/OpenAI PR/SWE-Lancer 方法、限制与 appendix。
- **Original Problem:** 仅延长 hidden reasoning 不能处理需要检索、计算、文件/图像变换或外部执行的任务；把工具固定在模型外部 workflow 又会限制模型在推理中自适应选择步骤。
- **Why the Previous Design Was Reasonable:** 独立 orchestrator 更易授权、审计和确定性重试；对简单任务，单次模型调用避免 tool latency、权限与副作用风险。
- **Changed Constraint:** reasoning workload 开始需要在同一推理轨迹中组合 web、Python、文件、图像与 memory，并按任务难度分配更多 test-time compute。
- **Mechanism:** 官方只证明模型被训练成在 chain of thought 中选择和组合 ChatGPT tools，并可把 image transformations 纳入 reasoning；RL recipe、tool-selection objective、router architecture、hidden trace 与 tool feedback training 均为 `Not Disclosed`。
- **State Ownership:** model policy 产生 tool intent；ChatGPT/Responses runtime 拥有 tool catalog、execution、memory 与结果回注；授权和副作用状态不属于模型参数。
- **Control Flow / Data Flow:** user/context → reasoning model → tool intent → host executes web/Python/file/image operation → observation 回到 reasoning → answer。具体 checkpoint、retry、parallelism 与 cancellation contract 为 `Not Disclosed`。
- **Implementation Details:** reasoning-effort setting、完整工具面和内部 tool scaffold 被披露；模型规模、训练 token、hardware、precision、tool router 与 serving topology 为 `Not Disclosed`。
- **Evaluation Setup:** 发布页的 benchmark 均为官方评测；AIME tool-use 示例给 Python，SWE-bench 使用固定 477 个 verified tasks、内部编辑/debug scaffold 与 4 tries 估计 pass@1；System Card 还含外部 assessor、cyber range、OpenAI PR 与 wet-lab protocol 评测。
- **Baselines / Ablations / Sensitivity:** 主要比较 o1、o3-mini、GPT-4o 及 helpful-only/safety-tuned checkpoints；没有公开 tool-policy ablation，也没有把同模型的 tools-on/off 在所有任务上系统控制。发布页明确警告带 Python 的 AIME 结果不可与无工具模型直接比较。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** model 为 o3/o4-mini launch candidates；reasoning effort 在部分评测为 high。硬件、precision、input/output length、batch、concurrency 与服务 SLO 均 `Not Disclosed`，因此不保留通用性能数字。
- **What the Evidence Actually Proves:** 该产品版本能在厂商 scaffold 中把工具调用放进 reasoning loop；System Card 展示了特定模型/脚手架/评测下的能力与风险测量，并说明多项 benchmark 结果依赖 tools 和 scaffold。
- **What It Does Not Prove:** 不证明模型独立拥有工具、工具调用安全、所有 Agent workload 的任务成功率、内部 tool router 机制或与无工具/不同 scaffold 系统的可比 Pareto 优势。
- **Limitations / Threats to Validity:** vendor-selected datasets；部分内部数据与 graders 不公开；checkpoint/scaffold 在代际间变化；外部评估样本与 elicitation 有限；产品页面会持续更新。
- **Trade-offs / New Failure Modes:** tool access 增强可验证计算和环境交互，同时引入权限扩大、prompt injection、数据外泄、执行副作用、tool/schema drift、observation poisoning、费用与长尾 latency。
- **Where the Previous Design Still Applies:** 可确定编程流程、只读简单问答、高风险动作及严格 SLO 场景仍应优先 deterministic workflow、显式 verifier 或 no-tool model path。
- **Evolution Relationship:** `Direct Evolution`（o1-style extended reasoning → reasoning 中的 tool choice）；与 Workflow/Tool executor 是 `Layering / Dependency`，不是模型取代控制平面。
- **ROADMAP Node:** Ch20、Ch52、Ch62、Ch68、Ch74；Ch74 为系统边界 owner。
- **Target and Adjacent Chapters Read:** Ch51–53、Ch61–63、Ch67–69、Ch73–75 已读。
- **Existing Coverage:** Ch74 已明确“模型只提案、host 执行/授权/验证”，Ch68 覆盖 prompt injection 与 least privilege，Ch62 覆盖 subject/environment/scaffold identity；发布事实没有增加可公开的内部机制。
- **Integration Decision:** `Weekly Only — Version/Product Fact`；tool-in-reasoning 的训练机制未公开。
- **Changed Files or Rejection Reason:** 不改 Books；不从产品能力反推 tool policy。
- **Open Questions:** tool-selection reward、tool observation representation、跨工具并行/重试、权限反馈是否进入 policy、不同 reasoning effort 的 latency/cost curve均未公开。

### MIRAS — It’s All Connected

- **Candidate / Week / Score:** MIRAS / 2025-W16 / 26/30。
- **Source Family ID:** `google-miras-titans-test-time-memory`。
- **Source Type:** arXiv 作者论文（Experimental）；无官方代码/artifact 链接。
- **First-public Date / Revision History:** arXiv v1 2025-04-17；截至访问日只有 v1。
- **Direct Primary Sources:** arXiv abs、HTML 与 26 页 PDF（2504.13173）。
- **Related Primary Sources:** Titans（2501.00663）作为直接前序；论文自身比较 Transformer++、RetNet、GLA、Mamba/Mamba2、DeltaNet/Gated DeltaNet、TTT 与 hybrid baselines。
- **Access and Verification Status:** Verified；正文、数学推导、实验、ablation、related work、proof appendix 与 experimental setup 全读。作者代码、独立复现与部署报告不存在。
- **Full-read Coverage:** metadata；Introduction/Background；associative-memory 定义；FTRL 与 learning-retaining 两种视角；attentional-bias/retention variants；Moneta/Yaad/Memora；parallel training；LM、scaling、RULER NIAH、ablation；conclusion、proof 与 setup。
- **Original Problem:** 固定大小 recurrent memory 要压缩不断增长的历史，但现有路线分别改变 learning rule、forget gate 或 memory shape，缺少能解释这些选择为何相关的统一坐标系。
- **Why the Previous Design Was Reasonable:** softmax attention 保留 token-level 可寻址状态且训练并行；Hebbian/delta linear memory 计算便宜、可扫描；Titans 用深 MLP memory 提高表达力。每条路线都在其原始 compute/memory 约束下合理。
- **Changed Constraint:** 长序列把 KV 的线性状态与 quadratic prefill 推向瓶颈；固定容量 memory 又暴露 overwrite、noise sensitivity 与 retention 不足，需要把“写什么、怎样保留、如何优化”分开设计。
- **Mechanism:** 把 sequence memory 定义为 key→value 的 associative operator，以 attentional-bias objective 决定写入偏好、retention regularizer 决定遗忘、memory architecture 决定容量、online algorithm 决定更新。Moneta 使用 p-norm bias，Yaad 使用 Huber/复合 retention，Memora 使用 KL/Bregman 类选择，并以近似和 chunked gradient construction 支持并行训练。
- **State Ownership:** 每层/每 memory block 的参数化 memory state 在 sequence model forward/test-time loop 内拥有；outer-loop weights 在训练系统拥有。它不是 Agent durable memory，也不自带 provenance/ACL/delete semantics。
- **Control Flow / Data Flow:** token 投影为 k/v → 当前 memory 预测 v → loss gradient/online rule 与 retention gate 更新 W_t → query 从更新后的 memory 读出 → residual backbone；训练时把递归更新重写/近似成可并行 chunk computation。
- **Implementation Details:** 纯 recurrent variants 使用两层 MLP memory；论文给出 p/Huber/KL bias、elastic-net/Lq/Bregman retention 和 update equations。训练 context 默认 4096；部分 scaling 实验把 context 从 2K 提到 32K。
- **Evaluation Setup:** FineWeb-Edu 用于 LM/commonsense，C4 用于 scaling；120M/340M/760M/1.3B，分别训练 15B/15B/30B/100B tokens；RULER single NIAH 在 1K–8K；340M/760M 比较 context scaling；architectural table只披露 layer/dim/head/peak LR/token。
- **Baselines / Ablations / Sensitivity:** 与 Transformer++、RetNet、GLA、Mamba/Mamba2、DeltaNet/Gated DeltaNet、TTT 和 hybrid 比较；p∈{1,1.5,2,2.8,3,3.2,4}、q∈{2,3,4,5}；Yaad 去 retention、input-dependent delta、L1/L2 分量或以 linear memory 替换 MLP。p 不呈单调收益，q 会改变长 context scaling。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 模型/token/训练长度如上；hardware、precision、global batch、optimizer-state placement、throughput、memory footprint、concurrency 与 online SLO 均 `Not Disclosed`。
- **What the Evidence Actually Proves:** 在作者的中小规模训练与选定 LM/commonsense/RULER 设置中，四维设计选择能产生行为不同的 recurrent variants；retention、bias 与 nonlinear memory 的消融均影响结果。
- **What It Does Not Prove:** 不证明 1.3B 以上可扩展性、生产吞吐/延迟优于 attention、所有任务上胜出、长期状态可恢复隔离，或某个 p/q 是通用最优。论文结论“更强”仍是单组作者实验。
- **Limitations / Threats to Validity:** 只有 v1、无代码/独立复现；hardware 与系统成本不披露；baseline 结果部分引用前作；NIAH 是 synthetic recall；只到 1.3B/100B tokens；没有真实长文、多租户、checkpoint/rollback 或 corruption 测试。
- **Trade-offs / New Failure Modes:** 固定状态降低 KV 增长，但在线更新引入顺序依赖、写入漂移、catastrophic overwrite、数值稳定性、状态隔离/恢复和训练并行近似误差；更深 memory 增加每 token compute。
- **Where the Previous Design Still Applies:** 精确回看任意 token、短上下文、高并行训练、成熟 kernel/serving 支持或需要可预测 cache lifecycle 时，attention/KV 仍合理；retrieval 仍负责外部可追溯知识。
- **Evolution Relationship:** 对 Titans 是 `Direct Evolution`（单架构 → 四维设计空间）；对 attention/linear RNN 是 `Explanatory Reframing`，不是替代证明。
- **ROADMAP Node:** Ch14、Ch22、Ch73；Ch22 为主 owner，Ch73 仅做 state-semantics handoff。
- **Target and Adjacent Chapters Read:** Ch13–15、Ch21–23、Ch72–74 已读。
- **Existing Coverage:** Ch22 已写出 memory architecture、attentional bias、retention、update rule 四轴及其把瓶颈从 KV 移到在线状态；Ch73 已严格区分 model-internal 与 durable Agent memory。需到 Books Gate 再核对现有文字是否保留实验边界与新 failure modes。
- **Integration Decision:** `Refine — Existing Argument`；主 owner Ch22，作为 test-time memory 设计空间抽象。
- **Changed Files or Rejection Reason:** 已复核 `books/part-02-model/22-long-context.md` 与 Ch73 的状态边界。
- **Open Questions:** 真实硬件吞吐、distributed state partition、checkpoint/rollback、跨请求 isolation、更新状态的精度与长期漂移，以及更大规模训练能否保持收益。

## Evidence Level

- 官方 Blog / Release 只证明公开事实；未公开实现保持未知。
- arXiv v1 默认 Status: Experimental；作者实验不等于独立复现。
- 跨来源连接是本项目推断，以 Evolution Relationship 标记。

## Cross-Week Deduplication

- 同一技术后续 revision 与工程集成回链首次公开周。
- 新版本不覆盖旧方案；年度索引记录 old constraint → new mechanism → new failure mode。

## Knowledge Tree Position

- OpenAI o3 and o4-mini → 第 20、29、52、62、68、74 章（Direct Evolution）
- MIRAS → 第 14、22、73 章（Direct Evolution；第 22 章为主 owner）

## Recommended Action

- OpenAI o3 and o4-mini：Must Read；只沉淀 tool-in-reasoning 的系统边界
- MIRAS：Must Read；与 W01 Titans 联读，refine 第 22 章

## Event-Date Daily Decision

历史回填不创建 Daily；事件与证据边界直接保留在本 Weekly。

## Books Integration Decision

Books Gate 已完成。该周候选的最终 disposition 已写入各自 Full Source Review；没有评分候选的周保持 No Material Update，不为制造 diff 修改 Books。


## Ignored Noise

- 忽略旧内容重发、二手转述、缺条件 benchmark 与纯可用性更新。
- discovery 排名和引用量不替代 novelty、reliability 或 longevity。

## Repository Changes

- 新增 papers/2025/weekly/2025-W16/README.md。
- 更新 books/part-02-model/22-long-context.md。
- 更新 books/part-06-agent/73-memory.md（边界 handoff）。

## Open Questions

- MIRAS 的四维设计空间如何映射到可部署 runtime 的隔离、checkpoint 与 rollback contract，仍待实现证据。
- o3/o4-mini 未公开训练与路由实现；不从产品能力反推其内部机制。

## Sources

- OpenAI o3 and o4-mini — https://openai.com/index/introducing-o3-and-o4-mini/（First Public: 2025-04-16；Accessed: 2026-07-31）
- OpenAI o3 and o4-mini System Card — https://cdn.openai.com/pdf/2221c875-02dc-4789-800b-e7758f3722c1/o3-and-o4-mini-system-card.pdf（First Public: 2025-04-16；Accessed: 2026-07-31）
- MIRAS — https://arxiv.org/abs/2504.13173（First Public: 2025-04-17；Accessed: 2026-07-31）
- MIRAS full text — https://arxiv.org/html/2504.13173（v1；Accessed: 2026-07-31）
