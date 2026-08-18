# AI Research Weekly — 2025-W33

> Coverage Window: 2025-08-11～2025-08-17
> Research Mode: Retrospective Backfill / Primary-Source Replay
> Accessed: 2026-08-24
> Audit Status: Historical Weekly Evidence Gate Passed — 36/36 Scored, 24/24 Retained Full Source Review, 12/12 Low-score Closure
> Historical Books Gate: Closed

## Executive Summary

旧版把本周写成“无保留候选”，这一结论在重新执行固定来源、arXiv v1、revision 与工程项目 replay 后被撤回。本轮核验 36 个周内唯一 owner：24 项达到 20/30 并完成非模板化 Full Source Review，12 项以来源、日期、评分与拒绝理由闭合；普通 `Review Pending`、`Unverified / Blocked` 与 family-level `Disputed` 均为 0。

证据形成四条长期演进链：长轨迹 Agent 从同步 batch rollout 走向 rollout/trainer 解耦与可恢复状态；共享 KV 从纯性能对象升级为带 tenant、privacy 与 revocation contract 的安全状态；推理从单一云端实例扩展到 cloud/device 分阶段所有权与质量—延迟路由；Agent/MCP 从“工具可调用”扩展到可审计的数据、通信拓扑与分层防御。所有性能数字仅保留在作者公开 workload contract 内，未外推为通用事实。

## Coverage Window and Limitations

- ISO owner window 为 2025-08-11 00:00～2025-08-17 23:59；论文以 arXiv v1、工程事项以官方首次公开时间归档。
- 按模型与研究机构 → arXiv/学术来源 → AI Infra/工程项目顺序 replay；Scholar、OpenAlex、DBLP、Semantic Scholar 与 Hugging Face 只用于 discovery/去重，机制结论回到 primary source。
- arXiv 后续 revision 只作为同一 Source Family 的演进节点；本周 claim 以 event-time v1 为主，后续版本仅用于核验澄清，不倒灌新实验结论。
- 历史回填不创建 Daily；本轮实际访问日期为 2026-08-24。
- 作者实验、API 模型测试和厂商工程计划均保持其证据等级；未公开 hardware、precision、batch、concurrency 或 SLO 的字段明确写 `Not Disclosed`。
- Scholar/OpenAlex 无不可变全量导出，因此本 Gate 表示固定来源 replay 与已知候选闭合，不宣称全球论文穷尽；年度 Archive Completion Gate 仍由年度索引统一管理。

## 1. 模型与研究机构

### Source Coverage

按固定机构顺序扫描一线模型公司、研究机构与 Hugging Face Blog。本周未发现可独立作为官方模型机制事件的公开发布；GPT-5 医疗评测是第三方 API benchmark，按论文证据归入低分闭合，不能反推 GPT-5 内部机制。

## 2. 论文与学术来源

按 arXiv → Scholar/OpenAlex/DBLP metadata → primary HTML/PDF/artifact replay。保留 ASearcher、RL Tricks or Traps、multi-head symbolic reasoning、两项 uncertainty work、SafeKV、BrowseMaster、LogicIF、OpenCUA、SMA、P/D-Device、pipeline LLM routing、Nested-ReFT、Shadow in the Cache、Memory Decoder、mSCoRe、verifier-guided masked diffusion、MCP-Guard、SeamlessFlow、ADMIRE-BayesOpt、SafeSieve、CRAFT-GUI 与 edge-device routing。

## 3. AI Infra 与工程项目

按 PyTorch → JAX → CUDA → Triton → vLLM → SGLang → Dynamo → TensorRT-LLM → Ray → KServe → Kubeflow → Kubernetes → Hugging Face → DeepSpeed → Megatron-LM → llama.cpp → ONNX Runtime → OpenXLA 扫描。

- 保留：vLLM `Path to vLLM 1.0 Release` RFC（2025-08-14）。它是外部接口与语义版本治理计划，不是已发布版本能力。
- PyTorch 2.8、TensorRT-LLM v0.21.0 等已归 W32；本周不重复计分。

## Candidate Scoring

| Candidate | Technical Novelty | System Impact | Practical Value | Source Reliability | Project Relevance | Longevity | Total | Decision |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| ASearcher / Beyond Ten Turns | 5 | 5 | 5 | 4 | 5 | 4 | 28/30 | Must Read；long-horizon agentic RL runtime |
| Tricks or Traps? Part I | 5 | 5 | 5 | 4 | 4 | 4 | 27/30 | Must Read；RL technique interaction evidence |
| Multi-head Transformers Learn Symbolic Multi-step Reasoning | 5 | 4 | 3 | 4 | 4 | 3 | 23/30 | Worth Watching；受限理论证据 |
| Human-Alignment and Calibration of Inference-Time Uncertainty | 4 | 3 | 4 | 4 | 4 | 3 | 22/30 | Worth Watching；calibration boundary |
| Can LLMs Detect Their Confabulations? | 4 | 4 | 4 | 4 | 4 | 3 | 23/30 | Worth Watching；uncertainty-guided probe |
| SafeKV | 5 | 5 | 5 | 4 | 5 | 3 | 27/30 | Must Read；privacy-aware shared KV state |
| BrowseMaster | 4 | 4 | 5 | 4 | 4 | 4 | 25/30 | Must Read；planner/executor browser pair |
| LogicIFGen / LogicIFEval | 4 | 4 | 4 | 4 | 4 | 3 | 23/30 | Worth Watching；executable instruction contract |
| OpenCUA | 5 | 5 | 5 | 4 | 5 | 3 | 27/30 | Must Read；open computer-use data/model stack |
| SMA membership audit | 4 | 4 | 4 | 4 | 4 | 4 | 24/30 | Worth Watching；source-aware RAG privacy audit |
| P/D-Device | 5 | 5 | 5 | 4 | 5 | 3 | 27/30 | Must Read；cloud/device state ownership |
| Neural Bandit LLM Selection for Task Pipelines | 4 | 4 | 4 | 4 | 4 | 3 | 23/30 | Worth Watching；downstream-aware routing |
| Nested-ReFT | 5 | 4 | 4 | 4 | 4 | 4 | 25/30 | Must Read；off-policy rollout cost branch |
| Shadow in the Cache / KV-Cloak | 5 | 5 | 4 | 4 | 5 | 3 | 26/30 | Must Read；KV inversion threat model |
| Memory Decoder | 5 | 4 | 4 | 4 | 4 | 4 | 25/30 | Must Read；learned plug-in memory branch |
| mSCoRe | 4 | 3 | 4 | 4 | 3 | 3 | 21/30 | Worth Watching；scalable multilingual evaluation |
| Masked Diffusion Text Style Transfer / Inference-time Scaling | 4 | 4 | 4 | 4 | 3 | 3 | 22/30 | Worth Watching；proposal/correction branch |
| MCP-Guard | 4 | 5 | 5 | 4 | 4 | 3 | 25/30 | Must Read；layered MCP detection pipeline |
| SeamlessFlow | 5 | 5 | 5 | 4 | 5 | 4 | 28/30 | Must Read；trainer-agent isolation and tag scheduling |
| ADMIRE-BayesOpt | 5 | 4 | 5 | 4 | 4 | 4 | 26/30 | Must Read；multi-fidelity data-mixture search |
| SafeSieve | 4 | 4 | 4 | 4 | 4 | 4 | 24/30 | Worth Watching；feedback-driven communication pruning |
| CRAFT-GUI | 4 | 4 | 4 | 4 | 4 | 4 | 24/30 | Worth Watching；curriculum GUI RL |
| Dynamic Quality-Latency Edge Routing | 4 | 4 | 4 | 4 | 4 | 2 | 22/30 | Worth Watching；quality-latency control policy |
| vLLM 1.0 RFC | 3 | 4 | 4 | 5 | 4 | 3 | 23/30 | Weekly Only；official interface-governance plan |
| GPT-5 Multimodal Medical Reasoning | 3 | 3 | 3 | 4 | 4 | 2 | 19/30 | Weekly Only；third-party API snapshot |
| VGGSounder | 3 | 3 | 4 | 4 | 3 | 2 | 19/30 | Weekly Only；benchmark repair case |
| MAMEX cold-start recommendation | 3 | 3 | 3 | 4 | 3 | 2 | 18/30 | Domain Only；MoE mechanism不改变主线 |
| PRECISE cyberattack compliance | 3 | 3 | 3 | 4 | 3 | 1 | 17/30 | Domain Only；critical-infra case |
| IBPS legal prediction | 2 | 2 | 3 | 4 | 3 | 2 | 16/30 | Domain Only；legal RAG/application case |
| Urban-STA4CLC | 3 | 2 | 3 | 4 | 2 | 2 | 16/30 | Domain Only；urban disaster model |
| NEXICA traffic causality | 3 | 3 | 3 | 4 | 2 | 2 | 17/30 | Domain Only；traffic-specific causal model |
| SYNAPSE-G | 3 | 3 | 3 | 4 | 3 | 2 | 18/30 | Domain Only；rare-event graph case |
| Hopfield Memorisation and Forgetting | 4 | 2 | 2 | 4 | 3 | 3 | 18/30 | Weekly Only；theory analogy，不外推 LLM memory |
| FROGENT | 3 | 3 | 4 | 4 | 3 | 2 | 19/30 | Domain Only；drug workflow case |
| HumanSense | 3 | 3 | 3 | 4 | 3 | 2 | 18/30 | Domain Only；empathetic multimodal benchmark |
| Activate Me! FHE activations | 4 | 3 | 3 | 4 | 3 | 2 | 19/30 | Emerging；FHE-specific activation trade-off |

## Deep Analysis

### Deep Analysis 1 — ASearcher: long trajectory changes the RL runtime contract

同步 group rollout 在轨迹长度接近时简单且合理，但 search Agent 的工具调用、网页长度和失败重试使执行时间形成长尾；单个慢轨迹会让整批训练等待。ASearcher 因而把 trajectory execution 与 model update 解耦，允许异步 rollout、动态过滤和较大的 turn budget，同时把搜索、浏览、网页压缩也放入端到端 RL action/history。

获得的是更长 horizon 与较少 batch bubble，代价是 policy staleness、trajectory version、reward attribution 和可复现性压力。作者在 Qwen2.5-7B/14B 与 QwQ-32B、GAIA/xBench/Frames 条件下报告收益；这不证明无限增加 tool turns 总会改善效果，也不证明异步训练在所有 reward/noise 条件下稳定。

### Deep Analysis 2 — SafeKV and Shadow in the Cache: KV identity includes privacy ownership

全局 prefix sharing 在同 token prefix 下复用 KV，过去的 owner 通常只含 model/version/prefix/block metadata。多租户后，命中时延与缓存内容本身都成为侧信道或敏感状态。SafeKV把 cache entry 分为 public/private，并用多级 detector、radix index、entropy monitoring 与撤销流程管理生命周期；Shadow in the Cache则从直接 inversion、collision 与 semantic injection 证明“拿到或操纵 KV”是独立威胁面。

严格 per-user isolation 最安全但损失共享收益；选择性共享提高复用率，却把 detector false negative、撤销窗口、tokenizer alignment 和监控容量加入 correctness contract。两项工作共同把 KV 从性能缓存演进为带 tenant、confidentiality、freshness、revocation 与 audit identity 的 typed state。

### Deep Analysis 3 — SeamlessFlow: Agent RL needs resumable rollout state

当 trainer 与 Agent 共用执行资源和同步阶段时，推理、tool waiting、reward 与训练 step 的不同速率制造 bubble。SeamlessFlow隔离 trainer/agent，以 centralized trajectory manager 持有部分 rollout，并用 tag scheduling 标识可运行、暂停、恢复和训练消费状态，使计算资源可以在时空上复用。

收益来自减少空转和扩大并发，代价是更复杂的 trajectory ownership、版本一致性、失败恢复和 scheduler fairness。论文对指定模型、集群与任务给出作者测量，不足以证明任意网络/工具时延下都 bubble-free。

## Full Source Review

### Full Source Review — ASearcher / Beyond Ten Turns

- **Candidate / Week / Score / Source Family / Type:** ASearcher / 2025-W33 / 28/30；`ARXIV-2508.07976`；research paper + official artifacts。
- **Event / Revision / Direct Sources:** v1 2025-08-11；v2 2025-08-13、v3 2025-09-10、v4 2025-10-26是同 family revision；https://arxiv.org/html/2508.07976v1 与 https://github.com/inclusionAI/ASearcher 。
- **Access / Full-read Coverage:** v1 Method、MDP/GRPO、training details、evaluation、case appendix 与 repository contract已核验；硬件总量未完整披露。
- **Problem / Previous Design / Changed Constraint:** 同步 batch rollout 对短且近似等长trajectory合理；search/browse latency与40+ turn长尾让慢轨迹阻塞整批，严格turn cap又限制策略学习。
- **Mechanism / State / Flow / Implementation:** executor持有browser/search/history，trainer持有policy/optimizer；异步队列传递带policy version的trajectory，动态过滤与reward进入GRPO update；网页思考被压缩以控制上下文。
- **Evaluation / Baselines / Sensitivity / Workload:** Qwen2.5-7B/14B、QwQ-32B；GAIA、xBench、Frames；Search-R1/Search-o1等baseline，turn/horizon与RL dynamics分析；precision、batch/concurrency/SLO部分 `Not Disclosed`。
- **Proves / Does Not Prove / Limitations:** 证明作者search workload中放宽horizon与异步训练共同带来收益；不证明turn越多越好、网页始终可靠或staleness可忽略。
- **Trade-offs / Failure Modes / Old Boundary:** 新增stale trajectory、reward归因、tool nondeterminism和历史压缩丢信息；短轨迹低方差环境仍适合同步batch。
- **Evolution / Owner / Chapters / Existing Coverage:** `Layering / Dependency`；owner `AGENT-WORKFLOW` Ch81（legacy Ch77），handoff `TRAIN-GRPO` Ch33 / `AGENT-RAG` Ch76；已读Ch33、Ch76、Ch80～82；书稿已有workflow state但缺长尾rollout ownership证据。
- **Integration / Open Question:** `Emerging / Experimental`，Historical Books Gate关闭；需验证staleness budget与trajectory exactly-once consumption。

### Full Source Review — Tricks or Traps? Part I

- **Candidate / Week / Score / Source Family / Type:** 2025-W33 / 27/30；`ARXIV-2508.08221`；large empirical research report。
- **Event / Revision / Direct Sources:** v1 2025-08-11；同family后续修订不重复计分；https://arxiv.org/html/2508.08221v1 。
- **Access / Full-read Coverage:** 26页正文、公式、统一复现实验、normalization/clip/loss/filter、ablation与结论已核验。
- **Problem / Previous Design / Changed Constraint:** 单项GRPO/PPO技巧在单一配置中合理；模型、reward scale与数据难度不同使经验互相矛盾且不可直接组合。
- **Mechanism / State / Flow / Implementation:** 统一infra逐项控制advantage normalization、variance term、clip、token/response loss与filter；reward distribution与gradient统计成为诊断state。
- **Evaluation / Baselines / Sensitivity / Workload:** Qwen3-4B/8B Base、easy/hard reasoning data、统一预算；逐项baseline/ablation；小reward std会放大gradient；集群、precision、SLO `Not Disclosed`。
- **Proves / Does Not Prove / Limitations:** 证明技巧效果依赖reward distribution和difficulty；不证明推荐组合对所有模型、长轨迹或不可验证reward最优。
- **Trade-offs / Failure Modes / Old Boundary:** 去variance可减极端放大但失去尺度归一；response/token loss各有长度bias；稳定尺度受控任务可沿用旧实现。
- **Evolution / Owner / Chapters / Existing Coverage:** `Direct Evolution`；owner `TRAIN-GRPO` Ch33，handoff `TRAIN-PPO` Ch32；已读Ch31～34；书稿已有条件分支，本证据补强interaction。
- **Integration / Open Question:** `Refine — Existing Argument after Books Gate`；需在long-horizon reward复测敏感度。

### Full Source Review — Multi-head Transformers Learn Symbolic Multi-step Reasoning

- **Candidate / Week / Score / Source Family / Type:** 2025-W33 / 23/30；`ARXIV-2508.08222`；theoretical paper。
- **Event / Revision / Direct Sources:** v1 2025-08-11；https://arxiv.org/abs/2508.08222 与event-time PDF。
- **Access / Full-read Coverage:** setup、GD theorem、head specialization proof、synthetic tree-path experiments与appendix assumptions已核验。
- **Problem / Previous Design / Changed Constraint:** attention常被经验解释为“多头分工”；严格证明需要可控任务，不能从可视化权重直接推因果。
- **Mechanism / State / Flow / Implementation:** 一层multi-head Transformer在树路径任务中经GD使heads对不同symbolic steps specialization；参数与attention pattern是学习状态。
- **Evaluation / Baselines / Sensitivity / Workload:** synthetic multi-step tree tasks与理论假设；实验验证趋势，hardware/precision/batch/SLO不构成核心且 `Not Disclosed`。
- **Proves / Does Not Prove / Limitations:** 在受限分布证明specialization可学；不证明真实LLM每个head有稳定语义或attention map是因果解释。
- **Trade-offs / Failure Modes / Old Boundary:** 多头增加自由度也带来冗余、symmetry和不可辨识；简单任务单头仍足够。
- **Evolution / Owner / Chapters / Existing Coverage:** `Explanatory Analogy`；owner `MODEL-MULTI-HEAD-ATTENTION` Ch15；已读Ch14～17；书稿已有机制，缺“可学得但受限”的证据边界。
- **Integration / Open Question:** `Emerging / Experimental`；真实规模specialization可辨识性待验证。

### Full Source Review — Human-Alignment and Calibration of Inference-Time Uncertainty

- **Candidate / Week / Score / Source Family / Type:** 2025-W33 / 22/30；`ARXIV-2508.08204`；research paper。
- **Event / Revision / Direct Sources:** v1 2025-08-11；https://arxiv.org/html/2508.08204v1 。
- **Access / Full-read Coverage:** uncertainty metrics、2,998题human survey、MMLU calibration、JSD-shift、appendix与limitations已核验。
- **Problem / Previous Design / Changed Constraint:** entropy是廉价online confidence signal，但“与人一样犹豫”和“答案正确概率”不是同一目标。
- **Mechanism / State / Flow / Implementation:** 从logits计算top-1、top-k/top-p/choice entropy；分别对齐人群disagreement及correctness/JSD shift，输出controller signal。
- **Evaluation / Baselines / Sensitivity / Workload:** Llama 1B/3B/8B、Mistral 7B base/instruct；Roper/Pew与MMLU；多metric比较；开放问答、closed API与SLO未覆盖。
- **Proves / Does Not Prove / Limitations:** 部分entropy在多选任务同时与群体不确定性和正确性相关；不证明token entropy等于事实置信度或可直接用于长回答。
- **Trade-offs / Failure Modes / Old Boundary:** 在线信号便宜但受prompt、tokenization、format影响；高风险判断仍可能需要multi-sample/evidence verifier。
- **Evolution / Owner / Chapters / Existing Coverage:** `Refine — Existing Argument`；owner `PLATFORM-EVALUATION-SYSTEM` Ch66，handoff `MODEL-SAMPLING` Ch20；已读Ch20、Ch66/67；已有claim confidence但缺human-alignment分离。
- **Integration / Open Question:** `Emerging / Experimental`；开放式atomic-claim calibration仍未解决。

### Full Source Review — Can LLMs Detect Their Confabulations?

- **Candidate / Week / Score / Source Family / Type:** 2025-W33 / 23/30；`ARXIV-2508.08139`；research paper。
- **Event / Revision / Direct Sources:** v1 2025-08-11；https://arxiv.org/html/2508.08139v1 。
- **Access / Full-read Coverage:** uncertainty decomposition、hidden-state aggregation probe、open-QA、misleading-context、ablation与limitations已核验。
- **Problem / Previous Design / Changed Constraint:** self-confidence/raw probability便宜，但误导context可制造“自信错误”，使流畅度与可靠性分离。
- **Mechanism / State / Flow / Implementation:** 从logits估计aleatoric/epistemic uncertainty，选salient tokens并聚合hidden states，训练response-level reliability probe。
- **Evaluation / Baselines / Sensitivity / Workload:** 多open-source LLM和open-QA；正确/误导context对照、probe baseline与feature ablation；production retrieval/SLO `Not Disclosed`。
- **Proves / Does Not Prove / Limitations:** probe捕捉部分可靠性变化且raw uncertainty会misalign；不证明模型天然“知道自己不知道”或跨domain免校准。
- **Trade-offs / Failure Modes / Old Boundary:** 需访问logits/hidden states和标注；probe漂移且受context manipulation；低风险任务仍可用cheap entropy screening。
- **Evolution / Owner / Chapters / Existing Coverage:** `Layering / Dependency`；owner `PLATFORM-EVALUATION-SYSTEM` Ch66，handoff `AGENT-RAG` Ch76；已读Ch66、Ch75～77；已有claim-evidence路径，本工作说明internal signal不能替代external evidence。
- **Integration / Open Question:** `Refine — Existing Argument after Books Gate`；需检索evidence后的claim-level recalibration。

### Full Source Review — SafeKV

- **Candidate / Week / Score / Source Family / Type:** 2025-W33 / 27/30；`ARXIV-2508.08438`；systems/security paper。
- **Event / Revision / Direct Sources:** v1 2025-08-11；https://arxiv.org/html/2508.08438v1 。
- **Access / Full-read Coverage:** threat model、three-tier detector、radix index、eviction/entropy monitor、8×H20 evaluation与limitations已核验。
- **Problem / Previous Design / Changed Constraint:** global prefix sharing提高TTFT/throughput；多租户API让cache-hit latency泄漏victim prefix，而per-user isolation损失复用。
- **Mechanism / State / Flow / Implementation:** entry持有public/private、tenant、detection、epoch；rule→Llama-3.2-1B detector→running-LLM validator，radix trees跨HBM/DRAM/SSD管理，entropy异常触发quarantine。
- **Evaluation / Baselines / Sensitivity / Workload:** SGLang、8×H20 96GB；Llama/Qwen3/DeepSeek/Phi；PII/ShareGPT/system-prompt、16 RPS；partition/global sharing与tier ablation。
- **Proves / Does Not Prove / Limitations:** 在黑盒timing attacker与tokenizer alignment下选择性共享降低攻击并保留复用；不覆盖GPU contention/shared-memory side channel，false negative有非零窗口。
- **Trade-offs / Failure Modes / Old Boundary:** detector占约2.6GB HBM并引入capacity；误判、revocation lag和entropy drift是新failure；高敏数据仍应全隔离。
- **Evolution / Owner / Chapters / Existing Coverage:** `Direct Evolution`；owner `INFER-KV-CACHE` Ch45，handoff `PLATFORM-MULTI-TENANT` Ch71 / `PLATFORM-SECURITY` Ch72；已读Ch45、Ch47、Ch71/72；书稿缺privacy visibility与revocation。
- **Integration / Open Question:** `Refine — Existing Argument after Books Gate`；需独立复现跨版本SGLang cache semantics。

### Full Source Review — BrowseMaster

- **Candidate / Week / Score / Source Family / Type:** 2025-W33 / 25/30；`ARXIV-2508.09129`；agent systems paper + artifact。
- **Event / Revision / Direct Sources:** v1 2025-08-12；https://arxiv.org/html/2508.09129v1 。
- **Access / Full-read Coverage:** planner/executor、program generation、browser contract、benchmark、ablation与failure cases已核验。
- **Problem / Previous Design / Changed Constraint:** 单prompt browser Agent适合短任务；复杂web task使一个context同时承担计划与执行而膨胀。
- **Mechanism / State / Flow / Implementation:** planner生成程序/子任务，executor持有browser state/tool results，结果回传planner修复或结束；program artifact使控制流可检查。
- **Evaluation / Baselines / Sensitivity / Workload:** web benchmarks、tool-agent baseline、planner/executor与program ablation；provider/browser并发和生产SLO以论文为限。
- **Proves / Does Not Prove / Limitations:** 在作者网页任务中职责分离提升扩展性；不证明双Agent总优于等算力单Agent，也不消除网页漂移。
- **Trade-offs / Failure Modes / Old Boundary:** 增加规划调用、program error、state serialization和replan cost；短任务仍适合单循环。
- **Evolution / Owner / Chapters / Existing Coverage:** `Layering / Dependency`；owner `AGENT-WORKFLOW` Ch81，handoff `AGENT-TOOL-CALLING` Ch78 / `AGENT-PLANNING` Ch79；已读Ch78～82；缺program artifact作为control plane。
- **Integration / Open Question:** `Emerging / Experimental`；动态网页execution trace如何version。

### Full Source Review — LogicIFGen / LogicIFEval

- **Candidate / Week / Score / Source Family / Type:** 2025-W33 / 23/30；`ARXIV-2508.09125`；benchmark/generation framework。
- **Event / Revision / Direct Sources:** v1 2025-08-12；https://arxiv.org/abs/2508.09125 与 https://github.com/mianzhang/LogicIF 。
- **Access / Full-read Coverage:** code-to-instruction、verifier、426项评测、complexity taxonomy、model comparison与error analysis已核验。
- **Problem / Previous Design / Changed Constraint:** 手写instruction benchmark规模小且判分含糊；递归/嵌套/函数调用需要executable ground truth。
- **Mechanism / State / Flow / Implementation:** 从可运行函数生成natural-language instruction，以程序结果作verifier；function/version/input成为evaluation identity。
- **Evaluation / Baselines / Sensitivity / Workload:** 426 logic-rich instructions、多SOTA LLM、type/complexity切片；hardware、precision、serving并发非研究变量。
- **Proves / Does Not Prove / Limitations:** 当前模型在该逻辑分布有缺口；不证明所有真实instruction可还原为code或verifier无语义偏差。
- **Trade-offs / Failure Modes / Old Boundary:** executable contract提高客观性但缩窄分布；自然语言多解和template leakage是风险；开放任务仍需人工评测。
- **Evolution / Owner / Chapters / Existing Coverage:** `Refine — Existing Argument`；owner `PLATFORM-EVALUATION-SYSTEM` Ch66；已读Ch66/73；已有executable evaluation，本工作补scalable generation。
- **Integration / Open Question:** `No Change — Already Covered`候选；Books Gate后只作受限案例。

### Full Source Review — OpenCUA

- **Candidate / Week / Score / Source Family / Type:** 2025-W33 / 27/30；`ARXIV-2508.09123`；dataset/model/tooling paper + artifacts。
- **Event / Revision / Direct Sources:** v1 2025-08-12；https://arxiv.org/html/2508.09123v1 。
- **Access / Full-read Coverage:** annotation infra、AgentNet、state-action/reflective trace、training、OSWorld evaluation、scaling、appendices/artifacts已核验。
- **Problem / Previous Design / Changed Constraint:** closed CUA隐藏data/action schema/failure，单一model release不能支持可重复研究。
- **Mechanism / State / Flow / Implementation:** capture tool记录OS/app observation/action；demo转为state-action与reflective CoT；model按统一action space执行，由environment verifier判定。
- **Evaluation / Baselines / Sensitivity / Workload:** 3 OS、200+ apps/sites、OSWorld-Verified等；model/data scale与test-time compute分析；高风险长期任务SLO未覆盖。
- **Proves / Does Not Prove / Limitations:** 开放data/tool/model stack支持CUA复现；34.8%作者成功率不等于通用桌面自治或安全无人监管。
- **Trade-offs / Failure Modes / Old Boundary:** capture带privacy/licensing、UI drift、replay和provenance成本；结构化场景API工具仍更可靠。
- **Evolution / Owner / Chapters / Existing Coverage:** `Direct Evolution`；owner `AGENT-TOOL-CALLING` Ch78，handoff `PLATFORM-EVALUATION-SYSTEM` Ch66 / `AGENT-WORKFLOW` Ch81；已读Ch66、Ch78～81；缺observation/action dataset生命周期。
- **Integration / Open Question:** `Refine — Existing Argument after Books Gate`；UI trace的delete/replay/consent contract待补。

### Full Source Review — SMA Membership Audit

- **Candidate / Week / Score / Source Family / Type:** 2025-W33 / 24/30；`ARXIV-2508.09105`；security/privacy research。
- **Event / Revision / Direct Sources:** v1 2025-08-12；https://arxiv.org/html/2508.09105v1 。
- **Access / Full-read Coverage:** semi-black-box threat、source attribution、zero-order optimization、image-to-text、datasets、ablation与limitations已核验。
- **Problem / Previous Design / Changed Constraint:** RAG只验answer correctness时合理；保护内容场景还需判断document/media membership及answer来源。
- **Mechanism / State / Flow / Implementation:** 对query perturbation与response变化做zero-order source attribution；多模态经受控image-to-text/feature路径，membership score绑定source identity。
- **Evaluation / Baselines / Sensitivity / Workload:** semi-black-box RAG、文本/多模态datasets、MIA baseline与source/perturbation ablation；tenant SLO `Not Disclosed`。
- **Proves / Does Not Prove / Limitations:** source attribution支持更细membership audit；不证明closed retriever、encrypted store或所有generator可迁移。
- **Trade-offs / Failure Modes / Old Boundary:** audit查询增加成本且可能成为oracle；attribution误差、media transform与index drift是风险；低敏内部RAG可用简单审计。
- **Evolution / Owner / Chapters / Existing Coverage:** `Layering / Dependency`；owner `AGENT-RAG` Ch76，handoff `PLATFORM-SECURITY` Ch72；已读Ch72、Ch75～77；缺membership leakage lens。
- **Integration / Open Question:** `Emerging / Experimental`；如何在不泄漏membership下提供citation。

### Full Source Review — P/D-Device

- **Candidate / Week / Score / Source Family / Type:** 2025-W33 / 27/30；`ARXIV-2508.09035`；distributed inference systems paper。
- **Event / Revision / Direct Sources:** v1 2025-08-12；https://arxiv.org/html/2508.09035v1 。
- **Access / Full-read Coverage:** design、controller/refiner/termination、prototype、real-trace evaluation、compatibility与conclusion已核验；独立artifact未公开。
- **Problem / Previous Design / Changed Constraint:** cloud-only一致但长期占用；device-only本地但长prefill慢；传GB级KV或频繁speculative RTT不适合抖动网络。
- **Mechanism / State / Flow / Implementation:** cloud先prefill并给有限token/可选refined prompt；device以speed controller展示且并行prefill，catch-up后接管decode；controller选token count/refinement ratio。
- **Evaluation / Baselines / Sensitivity / Workload:** Huawei端云prototype、real traces、8k等prompt、TTFT/TPOT/throughput/quality；作者报告TTFT至少降60%、cloud throughput最高15×；未披露项不外推。
- **Proves / Does Not Prove / Limitations:** 在作者同分布模型/网络下token/prompt assist改变端云占用；不证明cloud token是ground truth、任意模型可handoff或隐私已解决。
- **Trade-offs / Failure Modes / Old Boundary:** divergence、refinement丢信息、断网、version/tokenizer mismatch与display rollback；强一致任务仍适合cloud-only。
- **Evolution / Owner / Chapters / Existing Coverage:** `Alternative Branch`；owner `INFER-PD-DISAGGREGATION` Ch55，handoff `INFER-PREFILL` Ch43 / `INFER-SCHEDULING` Ch56；已读Ch43～45、Ch55/56；现有PD以cluster为主，缺device boundary。
- **Integration / Open Question:** `Emerging / Experimental`；需要端云version与rollback protocol。

### Full Source Review — Neural Bandit LLM Selection for Task Pipelines

- **Candidate / Week / Score / Source Family / Type:** 2025-W33 / 23/30；`ARXIV-2508.09958`；routing research。
- **Event / Revision / Direct Sources:** v1 2025-08-13；https://arxiv.org/abs/2508.09958 。
- **Access / Full-read Coverage:** objective、neural contextual bandit、pipeline dependency、telecom/medical experiments、baseline与regret discussion已核验。
- **Problem / Previous Design / Changed Constraint:** 单query router只预测当前模型成功/成本；pipeline中上游输出改变下游输入，局部最优不等于端到端最优。
- **Mechanism / State / Flow / Implementation:** 每stage bandit观察context/upstream artifact，联合选择model sequence；online feedback更新success estimator并由final success/cost指导探索。
- **Evaluation / Baselines / Sensitivity / Workload:** telecom QA与medical diagnosis；single-stage/greedy baseline；provider latency、concurrency和production SLO `Not Disclosed`。
- **Proves / Does Not Prove / Limitations:** 两类pipeline中dependency-aware selection优于局部router；不证明非平稳provider、长workflow或安全约束下收敛。
- **Trade-offs / Failure Modes / Old Boundary:** exploration消耗质量/成本，feedback delay和credit assignment复杂；独立subtask仍适合简单router。
- **Evolution / Owner / Chapters / Existing Coverage:** `Direct Evolution`；owner `INFER-SCHEDULING` Ch56，handoff `AGENT-WORKFLOW` Ch81；已读Ch52、Ch56、Ch81；现有request routing缺pipeline dependency。
- **Integration / Open Question:** `Refine — Existing Argument after Books Gate`；需带SLO/failure recovery的delayed feedback评测。

### Full Source Review — Nested-ReFT

- **Candidate / Week / Score / Source Family / Type:** 2025-W33 / 25/30；`ARXIV-2508.10123`；RL post-training paper。
- **Event / Revision / Direct Sources:** v1 2025-08-13；https://arxiv.org/html/2508.10123v1 。
- **Access / Full-read Coverage:** off-policy derivation、dynamic layer skipping、bias mitigation、math benchmarks、throughput、appendix与limitations已核验。
- **Problem / Previous Design / Changed Constraint:** target生成全部rollout最简单且on-policy，但推理成本高；独立draft model又引入额外生命周期。
- **Mechanism / State / Flow / Implementation:** target layer subset作behavior policy动态skip生成；importance/off-policy correction与三类bias mitigation控制mismatch；full target消费reward更新。
- **Evaluation / Baselines / Sensitivity / Workload:** 多model size/数学benchmark；standard ReFT；tokens/s、quality、bias variants、layer sensitivity；production SLO不适用。
- **Proves / Does Not Prove / Limitations:** 作者设置下降低rollout成本并保持性能；理论无偏依赖假设，不证明大gap或长tool trajectory稳定。
- **Trade-offs / Failure Modes / Old Boundary:** layer-skip drift、importance variance与调参复杂；小模型/rollout非瓶颈时standard ReFT更简单。
- **Evolution / Owner / Chapters / Existing Coverage:** `Alternative Branch`；owner `TRAIN-GRPO` Ch33，handoff `TRAIN-PPO` Ch32；已读Ch31～34、Ch38；缺shared-layer behavior branch。
- **Integration / Open Question:** `Emerging / Experimental`；异步staleness叠加时bias如何控制。

### Full Source Review — Shadow in the Cache / KV-Cloak

- **Candidate / Week / Score / Source Family / Type:** 2025-W33 / 26/30；`ARXIV-2508.09442`；systems security paper。
- **Event / Revision / Direct Sources:** v1 2025-08-13；https://arxiv.org/html/2508.09442v1 。
- **Access / Full-read Coverage:** inversion/collision/injection attacks、KV-Cloak transform/fusion、models/hardware、ablation与limitations已核验。
- **Problem / Previous Design / Changed Constraint:** KV作进程内性能state时不单独加密；跨tenant reuse、dump或memory access使中间表示可重构输入。
- **Mechanism / State / Flow / Implementation:** 三类attacker从KV或碰撞/语义反应推断prompt；KV-Cloak对K/V作可逆矩阵obfuscation并与operator融合。
- **Evaluation / Baselines / Sensitivity / Workload:** 多模型/攻击/reconstruction metric；plain KV与protection baseline、accuracy/latency/overhead ablation；配置以论文为准。
- **Proves / Does Not Prove / Limitations:** KV并非无害缓存，作者攻击能恢复输入且obfuscation降低重构；不证明抵抗key theft、side channel或自适应新攻击。
- **Trade-offs / Failure Modes / Old Boundary:** key/transform lifecycle、fusion兼容、debug和rotation成本；可信单进程可用plain KV。
- **Evolution / Owner / Chapters / Existing Coverage:** `Direct Evolution`；owner `INFER-KV-CACHE` Ch45，handoff `PLATFORM-SECURITY` Ch72；已读Ch45、Ch49、Ch72；缺confidentiality transform branch。
- **Integration / Open Question:** `Refine — Existing Argument after Books Gate`；需与paged/prefix eviction、dump共同建模。

### Full Source Review — Memory Decoder

- **Candidate / Week / Score / Source Family / Type:** 2025-W33 / 25/30；`ARXIV-2508.09874`；architecture/domain adaptation paper。
- **Event / Revision / Direct Sources:** v1 2025-08-13；https://arxiv.org/html/2508.09874v1 。
- **Access / Full-read Coverage:** retriever imitation、decoder architecture、plug-in integration、three-domain experiments、DAPT/RAG baselines、ablation与limitations已核验。
- **Problem / Previous Design / Changed Constraint:** DAPT写入全参数且可能遗忘；RAG保持外部更新但每次检索和长context增加latency。
- **Mechanism / State / Flow / Implementation:** 小memory decoder预训练模仿retriever；与共享tokenizer的frozen LM连接，在生成路径注入domain memory，不改base weights。
- **Evaluation / Baselines / Sensitivity / Workload:** Qwen/Llama、biomed/finance/law；DAPT/RAG/adapter baseline；perplexity、latency/parameter；freshness/SLO与跨tokenizer未覆盖。
- **Proves / Does Not Prove / Limitations:** learned component是DAPT/RAG之外分支；不证明等价可引用RAG、不保证删除更新知识或跨tokenizer迁移。
- **Trade-offs / Failure Modes / Old Boundary:** 低在线检索成本换训练成本、staleness、provenance/erase困难；实时事实/citation仍适合RAG。
- **Evolution / Owner / Chapters / Existing Coverage:** `Alternative Branch`；owner `AGENT-MEMORY` Ch77，handoff `MODEL-DECODER-ONLY` Ch18 / `AGENT-RAG` Ch76；已读Ch18、Ch75～77；缺retriever-imitation decoder。
- **Integration / Open Question:** `Emerging / Experimental`；如何实现memory version/supersession/delete。

### Full Source Review — mSCoRe

- **Candidate / Week / Score / Source Family / Type:** 2025-W33 / 21/30；`ARXIV-2508.10137`；evaluation benchmark。
- **Event / Revision / Direct Sources:** v1 2025-08-13；https://arxiv.org/abs/2508.10137 。
- **Access / Full-read Coverage:** taxonomy、multilingual synthesis、complexity scaling、eight-model evaluation、process analysis与limitations已核验。
- **Problem / Previous Design / Changed Constraint:** static commonsense benchmark饱和且只给总分；跨语言文化推理需要skill/difficulty维度。
- **Mechanism / State / Flow / Implementation:** taxonomy标注skill，synthesis生成多语言题，complexity controller扩展组合深度；保留language/skill/difficulty slice。
- **Evaluation / Baselines / Sensitivity / Workload:** eight LLMs、多语言commonsense、不同size/training与complexity；artifact受synthetic generator影响。
- **Proves / Does Not Prove / Limitations:** 高complexity/低资源语言仍有缺口；不证明CoT忠实或覆盖所有文化知识。
- **Trade-offs / Failure Modes / Old Boundary:** scalable benchmark可能引入generator bias和translation leakage；人工文化评审仍需要。
- **Evolution / Owner / Chapters / Existing Coverage:** `Refine — Existing Argument`；owner `PLATFORM-EVALUATION-SYSTEM` Ch66；已读Ch66；已有slice/evolution contract。
- **Integration / Open Question:** `No Change — Already Covered`；只保留为scalable benchmark案例。

### Full Source Review — Masked Diffusion Text Style Transfer / Inference-time Scaling

- **Candidate / Week / Score / Source Family / Type:** 2025-W33 / 22/30；`ARXIV-2508.10995`；generative-model paper。
- **Event / Revision / Direct Sources:** v1 2025-08-14；v2 2025-08-18为同family revision，不计W34新事件；https://arxiv.org/abs/2508.10995 与event-time HTML/PDF。
- **Access / Full-read Coverage:** masked diffusion、verifier guidance、sampling/control、style datasets、AR/diffusion baselines、ablation与limitations已核验。
- **Problem / Previous Design / Changed Constraint:** AR按序生成易缓存但局部错误难回改；masked diffusion可修正却需决定重采样区域和约束。
- **Mechanism / State / Flow / Implementation:** state含masked/unmasked token与verifier score；每轮proposal后verifier选择低质量区域重新mask/correct，直到stop budget。
- **Evaluation / Baselines / Sensitivity / Workload:** style-transfer datasets、多baseline、quality/style/content metrics与guidance ablation；hardware/precision/latency以作者设置为限。
- **Proves / Does Not Prove / Limitations:** verifier在该任务引导correction；不证明diffusion替代AR或verifier无reward hacking。
- **Trade-offs / Failure Modes / Old Boundary:** 并行修正换多轮compute、verifier依赖和commit不确定；低延迟streaming仍适合AR。
- **Evolution / Owner / Chapters / Existing Coverage:** `Alternative Branch`；owner `MULTIMODAL-GENERATIVE-PARADIGMS` Ch24；已读Ch20、Ch24、Ch48；已有branch，本工作补verifier commit。
- **Integration / Open Question:** `Emerging / Experimental`；需等算力/等SLO比较。

### Full Source Review — MCP-Guard

- **Candidate / Week / Score / Source Family / Type:** 2025-W33 / 25/30；`ARXIV-2508.10991`；security framework + benchmark。
- **Event / Revision / Direct Sources:** v1 2025-08-14；https://arxiv.org/html/2508.10991v1 。
- **Access / Full-read Coverage:** threat taxonomy、three-stage pipeline、70,448样本、A100/RTX4090 implementation、baseline/latency与limitations已核验；event-time dataset availability有限。
- **Problem / Previous Design / Changed Constraint:** auth/WAF适合传统API；MCP metadata和returned content能携带semantic injection、tool poisoning和exfiltration。
- **Mechanism / State / Flow / Implementation:** fail-fast static→fine-tuned E5→LLM arbitrator；uncertain回落stage-2 threshold；proxy持有policy/signature/model version和decision trace。
- **Evaluation / Baselines / Sensitivity / Workload:** 2,153 attack + 3,105 benign；SafeMCP/Shield/Scan与多LLM；A100 40GB训练、RTX4090 24GB、CUDA12.9；arbitrator影响latency。
- **Proves / Does Not Prove / Limitations:** 分层检测在synthetic-heavy benchmark给出成本/召回trade-off；不证明阻止真实execution或未见攻击，89.63%平均accuracy不能直接作gate。
- **Trade-offs / Failure Modes / Old Boundary:** static false positive、model drift、arbitration latency和benchmark leakage；强schema/allowlist应先用确定性policy。
- **Evolution / Owner / Chapters / Existing Coverage:** `Layering / Dependency`；owner `AGENT-MCP` Ch83，handoff `PLATFORM-SECURITY` Ch72 / `PLATFORM-GATEWAY` Ch62；已读Ch62、Ch72、Ch83/84；缺typed escalation evidence。
- **Integration / Open Question:** `Emerging / Experimental`；需真实MCP server replay。

### Full Source Review — SeamlessFlow

- **Candidate / Week / Score / Source Family / Type:** 2025-W33 / 28/30；`ARXIV-2508.11553`；distributed RL systems paper。
- **Event / Revision / Direct Sources:** v1 2025-08-15；https://arxiv.org/html/2508.11553v1 。
- **Access / Full-read Coverage:** isolation、trajectory manager、tag scheduling、partial rollout、implementation、evaluation/ablation与limitations已核验。
- **Problem / Previous Design / Changed Constraint:** co-located synchronous RL在同速阶段简单；agent rollout/tool wait和trainer compute速率不同，产生GPU bubble。
- **Mechanism / State / Flow / Implementation:** trainer/agent隔离；central manager持有trajectory chunk、policy tag、pause/resume、consumption state；scheduler按tag匹配资源。
- **Evaluation / Baselines / Sensitivity / Workload:** 指定reasoning/agent tasks、model size与GPU cluster；对主流RL framework比较bubble/throughput/scaling；未披露项不外推。
- **Proves / Does Not Prove / Limitations:** 作者集群中tag scheduling减少bubble；不证明所有tool workload零bubble或跨故障域exactly-once。
- **Trade-offs / Failure Modes / Old Boundary:** manager热点、tag mismatch、stale policy、partial rollout泄漏和恢复复杂；小规模仍适合同步co-location。
- **Evolution / Owner / Chapters / Existing Coverage:** `Direct Evolution`；owner `TRAIN-DISTRIBUTED-TRAINING` Ch36，handoff `TRAIN-GRPO` Ch33 / `TRAIN-CHECKPOINT` Ch35 / `AGENT-WORKFLOW` Ch81；已读Ch33～38、Ch81；缺resumable trajectory state machine。
- **Integration / Open Question:** `Refine — Existing Argument after Books Gate`；manager HA、reward exactly-once和staleness SLO待补。

### Full Source Review — ADMIRE-BayesOpt

- **Candidate / Week / Score / Source Family / Type:** 2025-W33 / 26/30；`ARXIV-2508.11551`；training-data optimization + run dataset。
- **Event / Revision / Direct Sources:** v1 2025-08-15；https://arxiv.org/html/2508.11551v1 。
- **Access / Full-read Coverage:** mixture objective、multi-fidelity BO、scale transfer、pretraining/IFT、460 runs、ablation/sensitivity与limitations已核验。
- **Problem / Previous Design / Changed Constraint:** 手工mixture在少量domain/低成本时合理；数据源增多、full run昂贵且小模型最佳配比可能不迁移。
- **Mechanism / State / Flow / Implementation:** BO把weights作black-box配置；multi-fidelity acquisition选择model scale/预算，observation更新surrogate，最终高fidelity验证。
- **Evaluation / Baselines / Sensitivity / Workload:** 1M～7B、pretraining/IFT、数十datasets；mixture baseline、transfer/fidelity ablation；作者最大实验搜索速度提升>500%，不可外推。
- **Proves / Does Not Prove / Limitations:** mixture是带成本sequential decision并有小到大transfer证据；不证明权重跨architecture/objective稳定。
- **Trade-offs / Failure Modes / Old Boundary:** surrogate bias、fidelity mismatch、evaluation noise与search budget；成熟固定配比仍更简单。
- **Evolution / Owner / Chapters / Existing Coverage:** `Direct Evolution`；owner `TRAIN-DATA` Ch27，handoff `TRAIN-PRETRAINING` Ch28 / `PLATFORM-COST` Ch70；已读Ch27/28、Ch66、Ch70；补multi-fidelity control loop。
- **Integration / Open Question:** `Refine — Existing Argument after Books Gate`；license/quality约束如何进入acquisition。

### Full Source Review — SafeSieve

- **Candidate / Week / Score / Source Family / Type:** 2025-W33 / 24/30；`ARXIV-2508.11733`；multi-agent systems + artifact。
- **Event / Revision / Direct Sources:** v1 2025-08-15；https://arxiv.org/html/2508.11733v1 。
- **Access / Full-read Coverage:** semantic init、historical complementarity、0-extension、pruning、six benchmarks、ablation、injection与heterogeneous analysis已核验。
- **Problem / Previous Design / Changed Constraint:** dense communication在小团队保证可达；规模增长带token tax/噪声/攻击面，固定top-k可能删关键路径。
- **Mechanism / State / Flow / Implementation:** edge持有semantic compatibility与historical contribution；权重从heuristic转向experience，0-extension聚类后更新mask/node。
- **Evaluation / Baselines / Sensitivity / Workload:** DeepSeek-V3、GPT-4o-mini、Llama3、Qwen、Kimi；六benchmarks；GPTSwarm/G-Designer/AgentPrune/Dropout与component ablation。
- **Proves / Does Not Prove / Limitations:** 作者graph减少12.4%～27.8% token并保持结果；不证明等算力single-agent headroom穷尽或真实workflow attribution可靠。
- **Trade-offs / Failure Modes / Old Boundary:** edge credit噪声、history lock-in、cluster collapse和gaming；小团队可保留dense graph。
- **Evolution / Owner / Chapters / Existing Coverage:** `Direct Evolution`；owner `AGENT-MULTI-AGENT` Ch82，handoff `PLATFORM-COST` Ch70；已读Ch70、Ch81～84；已有communication tax，补topology state evolution。
- **Integration / Open Question:** `Emerging / Experimental`；需等token/等调用single-agent验证。

### Full Source Review — CRAFT-GUI

- **Candidate / Week / Score / Source Family / Type:** 2025-W33 / 24/30；`ARXIV-2508.11360`；GUI agent RL paper。
- **Event / Revision / Direct Sources:** v1 2025-08-15；v2 2026-03-13为同family revision，不计后续周新事件；https://arxiv.org/html/2508.11360v1 。
- **Access / Full-read Coverage:** curriculum、GRPO、trajectory/action、benchmarks、baseline/ablation、errors与limitations已核验。
- **Problem / Previous Design / Changed Constraint:** uniform sampling适合难度近似；GUI reward稀疏/horizon不同，过难不给信号、过易浪费rollout。
- **Mechanism / State / Flow / Implementation:** 按difficulty/progress形成curriculum，观察screenshot/state输出action，environment success作reward，scheduler选task bucket。
- **Evaluation / Baselines / Sensitivity / Workload:** GUI benchmarks、多baseline与curriculum ablation；model/hardware/action budget按论文，真实OS drift/SLO未覆盖。
- **Proves / Does Not Prove / Limitations:** curriculum改善作者环境效率/成功；不证明difficulty跨app稳定或可直接生产自治。
- **Trade-offs / Failure Modes / Old Boundary:** curriculum bias、forgetting、reward hacking、UI drift；dense reward/小任务集可uniform train。
- **Evolution / Owner / Chapters / Existing Coverage:** `Layering / Dependency`；owner `TRAIN-GRPO` Ch33，handoff `AGENT-TOOL-CALLING` Ch78 / `PLATFORM-EVALUATION-SYSTEM` Ch66；已读Ch33、Ch66、Ch78；补GUI state/action contract。
- **Integration / Open Question:** `Emerging / Experimental`；需跨OS/app和failure recovery测试。

### Full Source Review — Dynamic Quality-Latency Edge Routing

- **Candidate / Week / Score / Source Family / Type:** 2025-W33 / 22/30；`ARXIV-2508.11291`；edge inference optimization。
- **Event / Revision / Direct Sources:** v1 2025-08-15；https://arxiv.org/html/2508.11291v1 。
- **Access / Full-read Coverage:** queue/channel/model formulation、routing policy、objective、simulation/trace、baseline/sensitivity与limitations已核验。
- **Problem / Previous Design / Changed Constraint:** static local/cloud route适合固定网络；channel、queue、device能力和query difficulty变化使固定阈值失效。
- **Mechanism / State / Flow / Implementation:** controller观察channel/queue/query/model，在local/edge/model间决策；reward联合quality、latency、resource cost在线更新。
- **Evaluation / Baselines / Sensitivity / Workload:** wireless edge simulation/trace、多model option、static/greedy与weight sensitivity；真实pricing/privacy/concurrency未完整披露。
- **Proves / Does Not Prove / Limitations:** 作者环境中dynamic route改善objective；不证明quality proxy可靠或跨网络泛化。
- **Trade-offs / Failure Modes / Old Boundary:** exploration、state estimation、version drift、tail latency；稳定单设备仍适合static policy。
- **Evolution / Owner / Chapters / Existing Coverage:** `Direct Evolution`；owner `INFER-SCHEDULING` Ch56，handoff `PLATFORM-GPU-SCHEDULER` Ch63；已读Ch56、Ch62/63；补network/device state。
- **Integration / Open Question:** `Emerging / Experimental`；quality estimator calibration与privacy constraint待补。

### Full Source Review — vLLM 1.0 RFC

- **Candidate / Week / Score / Source Family / Type:** 2025-W33 / 23/30；`VLLM-RFC-22932`；official engineering RFC。
- **Event / Revision / Direct Sources:** issue opened 2025-08-14；https://github.com/vllm-project/vllm/issues/22932 ；未来1.0 release为同family后续event。
- **Access / Full-read Coverage:** motivation、V0/V1 context、external interface cleanup、semver proposal与discussion已核验；非实现/release artifact。
- **Problem / Previous Design / Changed Constraint:** 快速演进时内部重构优先合理；V1进入production后，external API compatibility和semver成为平台contract。
- **Mechanism / State / Flow / Implementation:** RFC拟以1.0清理external interfaces并转semver；actual API/migration code/final behavior当时未冻结。
- **Evaluation / Baselines / Sensitivity / Workload:** 无benchmark；hardware/model/precision/length/batch/concurrency/SLO `Not Applicable / Not Disclosed`。
- **Proves / Does Not Prove / Limitations:** 仅证明2025-08-14公开规划；不证明计划完成、日期兑现或runtime性能变化。
- **Trade-offs / Failure Modes / Old Boundary:** stable API降低迁移成本但限制breaking cleanup；pre-1.0实验接口可高迭代。
- **Evolution / Owner / Chapters / Existing Coverage:** `Version Fact / Mechanism Not Disclosed`；owner `INFER-VLLM` Ch50，handoff `PLATFORM-PRODUCTION` Ch73；已读Ch49～52、Ch73；已有versioned runtime contract。
- **Integration / Open Question:** `Weekly Only — Version/Product Fact`；等待实际release/migration evidence。

## Low-score Source / Date / Rejection Closure

| Candidate | Source Family ID | First-public / Revision | Primary Source | Closure |
| --- | --- | --- | --- | --- |
| GPT-5 Multimodal Medical Reasoning | `ARXIV-2508.08224` | v1 2025-08-11；v2 2025-08-13 typo修订 | https://arxiv.org/abs/2508.08224 | 19/30；第三方API benchmark未公开内部机制，医疗结论受prompt/API snapshot约束 |
| VGGSounder | `ARXIV-2508.08237` | v1 2025-08-11；v2同周，后续v3～v5为revision | https://arxiv.org/abs/2508.08237 | 19/30；benchmark修复重要，但不改变多模态系统owner |
| MAMEX | `ARXIV-2508.08042` | v1 2025-08-11 | https://arxiv.org/abs/2508.08042 | 18/30；recommendation-domain adaptive MoE，未形成通用routing/placement contract |
| PRECISE | `ARXIV-2508.08190` | v1 2025-08-11 | https://arxiv.org/abs/2508.08190 | 17/30；critical-infrastructure compliance案例，依赖domain threat model |
| IBPS | `ARXIV-2508.07592` | v1 2025-08-11 | https://arxiv.org/abs/2508.07592 | 16/30；legal prediction/RAG应用，不改变长期RAG/governance框架 |
| Urban-STA4CLC | `ARXIV-2508.08976` | v1 2025-08-12 | https://arxiv.org/abs/2508.08976 | 16/30；灾后土地利用domain model，系统可迁移性不足 |
| NEXICA | `ARXIV-2508.09447` | v1 2025-08-13 | https://arxiv.org/abs/2508.09447 | 17/30；交通因果发现案例，未改变通用state/evaluation contract |
| SYNAPSE-G | `ARXIV-2508.09544` | v1 2025-08-13 | https://arxiv.org/abs/2508.09544 | 18/30；rare-event graph augmentation，证据局限domain dataset |
| Hopfield Memorisation and Forgetting | `ARXIV-2508.10765` | v1 2025-08-14 | https://arxiv.org/abs/2508.10765 | 18/30；数学机制可作类比但不能外推现代LLM memory |
| FROGENT | `ARXIV-2508.10760` | v1 2025-08-14 | https://arxiv.org/abs/2508.10760 | 19/30；drug-design multi-agent/MCP领域workflow，物理实验闭环不足 |
| HumanSense | `ARXIV-2508.10576` | v1 2025-08-14 | https://arxiv.org/abs/2508.10576 | 18/30；empathetic benchmark，未形成新的multimodal runtime contract |
| Activate Me! | `ARXIV-2508.11575` | v1 2025-08-15 | https://arxiv.org/abs/2508.11575 | 19/30；FHE-specific activation有价值，尚不足改变通用FFN/serving结论 |

## Evidence Level

- **Primary-source verified:** 24/24 retained均回到event-time arXiv HTML/PDF、official repository或official RFC，并完成Method/Evaluation/limitations/artifact边界记录。
- **Author experimental evidence:** 所有paper benchmark均视为作者实验；未披露字段不补推。
- **Official engineering fact:** vLLM RFC仅证明公开计划，不证明release完成或runtime行为。
- **Project inference:** 跨论文演进与Stable Node映射为本项目判断，已与作者结论分离。
- **Ordinary pending / blocked / disputed:** `Review Pending = 0`；`Unverified / Blocked = 0`；family-level `Disputed = 0`。

## Independent Review Checkpoint

- **Denominator / score review:** Candidate Scoring逐行复算为36个唯一owner；12项25～30分、12项20～24分、12项低于20分，六维分项与`Total`不一致为0。
- **Evidence review:** 24/24 retained逐包复核primary identity、event-time版本、Method/Implementation、Evaluation与limitations；12/12低分候选均有primary source、first-public/revision、最终分数和非模板拒绝边界。
- **Date / revision / spillback review:** owner window复核为2025-08-11～2025-08-17；同周revision合并进同一family，W01～W32 owner与后续revision仅回链、不重复评分，未发现需要转移的新owner。
- **Dedup / owner review:** 以`Source Family ID + primary identifier + first-public date`复核36个评分owner，无候选名或family重复；每个retained机制均有一个canonical Stable Node owner，跨章只保留handoff。
- **Fact boundary review:** 作者benchmark、第三方API观察、官方RFC事实与本项目演进推断已分层；未披露hardware、precision、batch、concurrency和SLO没有补推，vLLM 1.0没有写成已发布能力。
- **Structure review:** H1唯一、标题层级无跳跃、3项Deep Analysis、24项Full Source Review、12项low-score closure、代码围栏平衡、尾随空白为0；scoped diff check通过。
- **Final Gate:** `Historical Weekly Evidence Gate = Passed`；`Review Pending = 0`、`Unverified / Blocked = 0`、family-level `Disputed = 0`。Historical Books Gate继续关闭，不据此修改Books。

## Cross-Week Deduplication

- `AIOS` `2403.16971v5`、`MADAM-RAG` `2504.13079v2`、`CodeJudgeBench` `2507.10535v2`、`StepFun-Prover` `2507.20199v3`由更早v1周拥有；本周revision不计分。
- `GTPO` `2508.04349v2`、`IRL-VLA` `2508.06571v2`、`Memp` `2508.06433v2`、`Block` `2508.03611v2`、`Shuffle-R1` `2508.05612v2`、`DSperse` `2508.06972v2`回链W32。
- `FreeKV` `2505.13109v2`、`FRUGAL` `2411.07837v3`、`Rollout Roulette` `2502.01618v5`只记录revision，不倒灌W33。
- ASearcher、VGGSounder同周revision各合并一个评分owner；vLLM RFC与未来1.0 release保持同family不同event node。

## Knowledge Tree Position

| Evolution chain | Canonical owner | Handoffs |
| --- | --- | --- |
| reward normalization / off-policy / rollout runtime | `TRAIN-GRPO` Ch33；`TRAIN-DISTRIBUTED-TRAINING` Ch36 | `TRAIN-PPO` Ch32、`TRAIN-CHECKPOINT` Ch35、`AGENT-WORKFLOW` Ch81 |
| inference-time uncertainty / executable evaluation | `PLATFORM-EVALUATION-SYSTEM` Ch66 | `MODEL-SAMPLING` Ch20、`AGENT-RAG` Ch76 |
| KV privacy identity / isolation / obfuscation | `INFER-KV-CACHE` Ch45 | `PLATFORM-MULTI-TENANT` Ch71、`PLATFORM-SECURITY` Ch72 |
| cloud/device and pipeline routing | `INFER-SCHEDULING` Ch56 | `INFER-PD-DISAGGREGATION` Ch55、`PLATFORM-GPU-SCHEDULER` Ch63 |
| computer-use / browser workflow | `AGENT-TOOL-CALLING` Ch78；`AGENT-WORKFLOW` Ch81 | `AGENT-PLANNING` Ch79、`PLATFORM-EVALUATION-SYSTEM` Ch66 |
| learned/domain memory | `AGENT-MEMORY` Ch77 | `AGENT-RAG` Ch76、`MODEL-DECODER-ONLY` Ch18 |
| MCP / multi-agent communication security | `AGENT-MCP` Ch83；`AGENT-MULTI-AGENT` Ch82 | `PLATFORM-SECURITY` Ch72、`PLATFORM-COST` Ch70 |
| data mixture optimization | `TRAIN-DATA` Ch27 | `TRAIN-PRETRAINING` Ch28、`PLATFORM-COST` Ch70 |

## Recommended Action

- Weekly evidence已闭合；Historical Books Gate继续关闭，本轮不修改Books。
- Books Gate开放后优先审计SafeKV/Shadow、SeamlessFlow/ASearcher、P/D-Device、ADMIRE与OpenCUA；其余按各Review disposition处理。
- vLLM RFC保持`Weekly Only — Version Fact`，等待实际release/migration artifact。

## Event-Date Daily Decision

Historical Backfill不补造Daily；所有事件按first-public date直接记录在本Weekly。

## Books Integration Decision

Historical Books Gate关闭。24个retained family仅完成evidence packet与owner定位；本轮没有把Weekly摘要写入Books，也没有把`Emerging`、`Version Fact`或作者benchmark外推为长期机制结论。

## Ignored Noise

- 忽略转载、榜单、无primary evidence产品对比、旧论文重发与仅因推荐日期落在本周的条目。
- API benchmark不用于反推闭源模型训练/runtime；domain paper若不改变AI System contract则低分闭合。
- 同一arXiv family的revision、镜像与聚合站条目不重复评分。

## Repository Changes

- 重建本README：旧“空周”stub替换为36个唯一owner、24项Full Source Review、12项低分closure、revision/spillback与Gate。
- 未修改年度索引、Learning State、Books、ROADMAP或其他Weekly；未stage、commit或push。

## Open Questions

- 长轨迹RL的policy staleness、reward exactly-once与trajectory recovery如何形成统一SLO？
- KV cache在prefix sharing、paged eviction、tenant isolation与obfuscation同时启用时，identity和revocation顺序如何定义？
- cloud/device handoff发生token divergence或断网时，用户可见输出由谁commit/rollback？
- uncertainty probe与external evidence verifier组合后，claim-level confidence如何校准？
- multi-agent pruning是否能在等总token/等模型调用的single-agent baseline下保持收益？

## Sources

- https://arxiv.org/html/2508.07976v1
- https://arxiv.org/html/2508.08221v1
- https://arxiv.org/abs/2508.08222
- https://arxiv.org/html/2508.08204v1
- https://arxiv.org/html/2508.08139v1
- https://arxiv.org/html/2508.08438v1
- https://arxiv.org/html/2508.09129v1
- https://arxiv.org/abs/2508.09125
- https://arxiv.org/html/2508.09123v1
- https://arxiv.org/html/2508.09105v1
- https://arxiv.org/html/2508.09035v1
- https://arxiv.org/abs/2508.09958
- https://arxiv.org/html/2508.10123v1
- https://arxiv.org/html/2508.09442v1
- https://arxiv.org/html/2508.09874v1
- https://arxiv.org/abs/2508.10137
- https://arxiv.org/abs/2508.10995
- https://arxiv.org/html/2508.10991v1
- https://arxiv.org/html/2508.11553v1
- https://arxiv.org/html/2508.11551v1
- https://arxiv.org/html/2508.11733v1
- https://arxiv.org/html/2508.11360v1
- https://arxiv.org/html/2508.11291v1
- https://github.com/vllm-project/vllm/issues/22932
- https://github.com/inclusionAI/ASearcher
- https://github.com/mianzhang/LogicIF
