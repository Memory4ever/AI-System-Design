# AI Research Weekly — 2025-W34

> Coverage Window: 2025-08-18～2025-08-24
> Research Mode: Retrospective Backfill / Full Discovery Replay
> Accessed: 2026-08-24
> Status: Discovery Replay Closed — 30 Scored Families / 27 Retained Full Source Reviews / 3 Low-score Closures

## Executive Summary

W34 不是只有 DeepSeek-V3.1 的发布周。按固定来源顺序重放、独立 recall 复核，并对 W35 的 revision/surfacing 候选反查 v1 后，本周建立了 30 个唯一 Source Family：27 个达到 20/30 并完成非模板化 Full Source Review，3 个低分候选完成来源、日期、评分与拒绝闭合。主线集中在五个约束迁移：Agent 从静态 tool schema 进入真实 MCP runtime，并从固定反思进入可读写 episodic memory；后训练从结果奖励进入过程、rubric 与可自验证反馈；test-time scaling 从固定采样预算进入 confidence-aware routing；多模态系统从生成 observation 进入 action-conditioned state transition 与物理行动接口；长序列与视觉生成从固定 dense interaction 进入 low-rank routing、progressive granularity 与可控 guidance。TPLA 与 AgentFly/Memento 的 v2 均在 W35 surface，但 v1 分别为 2025-08-21 与 2025-08-22，因此 owner 回拨 W34。

本周没有 `Review Pending`、`Unverified / Blocked` 或 `Disputed`。论文数字仅证明作者给定模型、数据、harness 与 evaluator 下的结果；未披露的 hardware、precision、concurrency、SLO 不作推断。Historical Books Gate 仍关闭，本文件不触发 Books 修改。

## Coverage Window and Limitations

- 以官方发布日期、GitHub Release 或 arXiv v1 为 owner date；后续 revision 只作为同一 Source Family 的演进节点。
- 固定机构扫描覆盖 OpenAI、Anthropic、Google/DeepMind、Meta、Microsoft、NVIDIA、DeepSeek、阿里/Qwen、字节、腾讯、百度、华为及 Hugging Face Research。保留 DeepSeek-V3.1 与 NVIDIA Nemotron Nano 2；其余未发现同窗口内可形成独立长期机制的官方事件。
- 学术 discovery 按 arXiv → Google Scholar → OpenAlex → DBLP → Semantic Scholar / Hugging Face discovery 回到 primary full text 核验；Crossref 仅用于 metadata 交叉检验。
- AI Infra 按 PyTorch、JAX、CUDA、Triton、vLLM、SGLang、Dynamo、TensorRT-LLM、Ray、KServe、Kubeflow、Kubernetes、Hugging Face、DeepSpeed、Megatron-LM、llama.cpp、ONNX Runtime、OpenXLA 扫描；未发现本窗口内达到 20/30 且拥有 canonical primary event date 的新增 release/RFC。
- 当前 HTML 可能对应后续 revision；所有机制描述均核对 v1 owner date，并明确 revision boundary。历史回填不补造 Daily。

## 1. 模型与研究机构

### Source Coverage

- DeepSeek-V3.1（2025-08-21）：官方 API/model contract；内部 hybrid mechanism 未公开。
- NVIDIA Nemotron Nano 2（arXiv v1 2025-08-20）：完整 technical report；v2～v4 属同一 family revision。
- 其他固定机构在本窗口未形成独立保留事件；转载、leaderboard 与缺 workload contract 的发布不计分。

## 2. 论文与学术来源

### Source Coverage

- Agent/MCP：MCPGauge、POML、MCP-Universe、LiveMCP-101、Mobile-Agent-v3、HeroBench、Dissecting Tool-Integrated Reasoning、AgentFly（current title: Memento）。
- Training/Evaluation：ToolACE-MT、Rubric Anchors、Atom-Searcher、DuPO、DeepConf。
- Multimodal/World Model：Matrix-Game 2.0、Embodied-R1、RynnEC、4DNeX、Next Visual Granularity、S²-Guidance、Precise Action-to-Video、MeshCoder。
- Model/Inference：Quantization Meets dLLMs、Intern-S1、FLARE、TPLA。
- 低分闭合：aiXiv、LLaSO、Fin-PRM；并非“未找到”，而是本轮核验后不进入 retained gate。

## 3. AI Infra 与工程项目

### Source Coverage

- 固定 release/RFC/PR 扫描完成，未发现 owner date 位于 W34 且达到保留门槛的新事件。
- PyTorch 2.8、TensorRT-LLM 0.21 等已在更早 owner week；Kubernetes v1.34/DRA GA 位于 W35，均不回拨到 W34。

## Candidate Scoring

| Candidate | Technical Novelty | System Impact | Practical Value | Source Reliability | Project Relevance | Longevity | Total | Decision |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| MCPGauge / Help or Hurdle | 4 | 4 | 4 | 4 | 4 | 4 | 24/30 | Retain — MCP benefit must be measured against tool overhead |
| ToolACE-MT | 5 | 4 | 4 | 4 | 4 | 4 | 25/30 | Retain — verifier-owned multi-turn tool data pipeline |
| Reinforcement Learning with Rubric Anchors | 5 | 4 | 4 | 4 | 4 | 4 | 25/30 | Retain — open-ended reward contract |
| HeroBench | 4 | 4 | 4 | 4 | 4 | 4 | 24/30 | Retain — executable hierarchical-plan evaluation |
| Atom-Searcher | 5 | 4 | 4 | 4 | 4 | 4 | 25/30 | Retain — atomic search-state reward assignment |
| Matrix-Game 2.0 | 5 | 5 | 4 | 4 | 4 | 4 | 26/30 | Retain — action-conditioned interactive world state |
| POML | 4 | 4 | 5 | 4 | 4 | 3 | 24/30 | Retain — prompt as versioned declarative artifact |
| Embodied-R1 | 5 | 4 | 4 | 4 | 4 | 4 | 25/30 | Retain — pointing as embodiment-agnostic interface |
| RynnEC | 4 | 4 | 4 | 4 | 4 | 3 | 23/30 | Retain — region-owned embodied perception state |
| DuPO | 5 | 4 | 4 | 4 | 4 | 4 | 25/30 | Retain — dual tasks produce intrinsic verification feedback |
| NVIDIA Nemotron Nano 2 | 5 | 5 | 5 | 5 | 4 | 3 | 27/30 | Retain — hybrid architecture, pruning and budget control co-design |
| MCP-Universe | 4 | 5 | 4 | 4 | 4 | 4 | 25/30 | Retain — execution-based real MCP evaluation |
| Quantization Meets dLLMs | 4 | 4 | 4 | 4 | 4 | 4 | 24/30 | Retain — PTQ contract changes under iterative denoising |
| Deep Think with Confidence | 5 | 5 | 5 | 4 | 4 | 3 | 26/30 | Retain — confidence-aware test-time compute routing |
| Mobile-Agent-v3 | 5 | 5 | 4 | 4 | 4 | 4 | 26/30 | Retain — environment-owned GUI trajectory lifecycle |
| LiveMCP-101 | 4 | 4 | 4 | 4 | 4 | 4 | 24/30 | Retain — parallel live-reference evaluator |
| Intern-S1 | 5 | 5 | 4 | 5 | 4 | 4 | 27/30 | Retain — scientific modality/data/reward co-design |
| DeepSeek-V3.1 | 4 | 4 | 4 | 4 | 5 | 4 | 25/30 | Retain — Version Fact / Mechanism Not Disclosed |
| 4DNeX | 5 | 4 | 4 | 4 | 4 | 4 | 25/30 | Retain — RGB/XYZ joint representation for feed-forward 4D generation |
| Next Visual Granularity Generation | 5 | 4 | 3 | 4 | 4 | 4 | 24/30 | Retain — coarse-to-fine visual token state hierarchy |
| S²-Guidance | 4 | 3 | 4 | 4 | 3 | 4 | 22/30 | Retain — stochastic self-guidance without a separately trained weak model |
| Precise Action-to-Video | 5 | 4 | 4 | 4 | 4 | 4 | 25/30 | Retain — visual action representation across embodiments |
| FLARE | 5 | 5 | 4 | 4 | 5 | 4 | 27/30 | Retain — SDPA-native low-rank gather/scatter routing |
| MeshCoder | 5 | 4 | 4 | 4 | 4 | 4 | 25/30 | Retain — executable program as editable 3D state |
| Dissecting Tool-Integrated Reasoning | 4 | 4 | 4 | 4 | 5 | 4 | 25/30 | Retain — accuracy/cost contract for tool reasoning |
| TPLA | 5 | 5 | 5 | 4 | 5 | 4 | 28/30 | Retain — shard latent KV without discarding full-head information |
| AgentFly / Memento | 5 | 5 | 4 | 4 | 5 | 4 | 27/30 | Retain — memory read/write as online agent policy adaptation |
| aiXiv | 3 | 3 | 3 | 4 | 3 | 2 | 18/30 | Reject — platform case lacks independent quality-control evidence |
| LLaSO | 3 | 3 | 4 | 4 | 2 | 2 | 18/30 | Reject — useful speech artifact, limited current owner fit |
| Fin-PRM | 3 | 3 | 3 | 4 | 3 | 3 | 19/30 | Reject — narrow domain evidence, no general reward conclusion |

## Deep Analysis

### Deep Analysis 1 — MCP 从协议兼容进入真实执行证据

静态 function-call benchmark 只验证 schema compliance；真实 MCP 还引入 discovery、长上下文、工具陌生性、动态 ground truth 与外部副作用。MCPGauge、MCP-Universe 和 LiveMCP-101 分别测量“接入 MCP 是否真的有益”、真实 server 上的 execution success，以及与 reference agent 同时执行的 temporal evaluation。演进不是“协议标准化就提高能力”，而是 `interface compatibility → executable task contract → dynamic evaluator`。代价是 server drift、credential/RBAC、外部状态和 evaluator freshness 都进入结果所有权；模型能力、agent scaffold 与环境机会必须拆开。

### Deep Analysis 2 — 奖励从终局正确进入过程状态与验证者

Rubric Anchors、Atom-Searcher、ToolACE-MT 与 DuPO 共同暴露同一约束：结果标签不足以给长轨迹分配 credit。新的机制分别把 rubric、Atomic Thought、offline verifier 与 generalized duality 变为监督状态。收益是开放任务、搜索和 tool-use 可以获得更细反馈；代价是 verifier bias、reward hacking、rubric leakage、过滤选择偏差与额外生成成本。旧的 exact-match/RLVR 在答案可程序验证时仍更简单可靠，不应被通用 judge 覆盖。

### Deep Analysis 3 — Test-time scaling 从固定预算进入置信度控制流

多数投票先生成完整 trace，再统一聚合；DeepConf 用局部 group confidence 对 trace 过滤与早停，把“多采样”改成运行时调度问题。该信号来自 token distribution，不是事实真实性概率；其收益只在给定模型、数学题、sampling budget 与阈值下成立。新的 failure mode 是 confident-but-wrong trace 被保留、低置信正确分支被过早剪枝，以及跨模型 calibration 漂移。因此 confidence 只能控制算力分配，不能替代 evidence verification。

## Full Source Review

### MCPGauge / Help or Hurdle

- **Candidate / Week / Score:** MCPGauge / 2025-W34 / 24/30。
- **Source Family ID:** `ARXIV-2508.12566`。
- **Source Type:** full paper、benchmark specification 与 evaluation artifact。
- **Event Date / First-public Date / Revision History:** arXiv v1 2025-08-18；owner 固定为 W34，后续 revision 不重复计分。
- **Direct Primary Sources:** arXiv:2508.12566 HTML/PDF 与项目材料。
- **Related Primary Sources:** MCP protocol specification；MCP-Universe、LiveMCP-101 作为同周相邻但独立 family。
- **Access and Verification Status:** Verified；全文、指标与实验表可访问。
- **Full-read Coverage:** metadata、Introduction/Related Work、MCPGauge 构造、四类指标、六模型实验、API/token cost、讨论与限制均已读。
- **Original Problem:** 接入 MCP 常被默认等价于更强 agent，但额外工具、schema 与 context 也可能伤害任务准确率。
- **Why the Previous Design Was Reasonable:** 静态 tool benchmark 可复现、成本低，适合验证 function-call syntax；工具空间小且稳定时无需真实 server。
- **Changed Constraint:** 真实 MCP suite 带来不同 server、长 schema、动态调用与 token overhead，必须同时测 benefit 与 burden。
- **Mechanism:** 160 prompts、25 datasets、30 MCP suites 与约 20K API calls；以 proactivity、compliance、effectiveness、overhead 分解 MCP 行为。
- **State Ownership:** benchmark manifest 拥有 task/tool mapping；MCP server 拥有 tool truth；agent 拥有调用决策；evaluator 拥有 outcome judgement。
- **Control Flow / Data Flow:** prompt → agent 选择/调用 MCP → server response → final answer → accuracy 与 call/token overhead 联合计量。
- **Implementation Details:** orchestration 在 RTX 3090 上运行，模型多为 API；只对实际发生 call 的样本做部分分析会引入 selection bias。
- **Evaluation Contract:** 作者报告平均 accuracy 在启用 MCP 后下降 9.5%，input-token overhead 为 3.25×～236.5×；数字绑定其六模型、160 prompts 与 30 suites。
- **Baselines / Ablations / Sensitivity / Overhead:** 对比无 MCP 与启用 MCP；覆盖不同 suite/模型，未提供 production concurrency 或 server-failure sensitivity。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** orchestration RTX 3090；商业模型 inference hardware、precision、batch、concurrency、TTFT/TPOT/SLO Not Disclosed。
- **What the Evidence Proves / Does Not Prove:** 证明协议接入可能增加成本并降低给定 benchmark 准确率；不证明 MCP 普遍有害，也不隔离 model、server quality 与 scaffold 的全部因果。
- **Limitations / Threats to Validity:** prompt selection、API version、server availability 与 tool-call conditioning 影响结果；外部工具副作用未完整纳入。
- **Trade-offs / New Failure Modes:** 统一接口换来 schema/context 膨胀、错误调用、server drift 与 credential 风险。
- **Where the Previous Design Still Applies:** 工具少、schema 固定、低延迟且可由 typed client 直接调用时，静态 integration 更简单。
- **Evolution Relationship:** `Layering / Dependency`：tool calling → MCP interoperability → MCP benefit/overhead evaluation。
- **ROADMAP Node:** `AGENT-MCP`（Ch83），handoff `PLATFORM-EVALUATION-SYSTEM`（Ch66）。
- **Target and Adjacent Chapters Read:** Ch82～84 与 Ch65～67 已定位；Historical Books Gate 关闭，未写 Books。
- **Existing Coverage:** Agent/MCP 章节已有 interface ownership；本证据新增“协议价值必须做 counterfactual measurement”的候选。
- **Integration Decision:** `Books Pending — Evidence Complete`。
- **Changed Files or Rejection Reason:** 仅更新本 Weekly；不进入 Books。
- **Open Questions:** 如何在 server/version 漂移下维护 reproducible MCP benchmark，并把安全副作用纳入 score？

### ToolACE-MT

- **Candidate / Week / Score:** ToolACE-MT / 2025-W34 / 25/30。
- **Source Family ID:** `ARXIV-2508.12685`。
- **Source Type:** full paper、synthetic-data pipeline、artifact/evaluation。
- **Event Date / First-public Date / Revision History:** v1 2025-08-18；v2 2026-02-02、v3 2026-02-13（ICLR 2026），同一 family。
- **Direct Primary Sources:** arXiv:2508.12685 HTML/PDF 与公开项目材料。
- **Related Primary Sources:** BFCL-v3、ACEBench、tau-Bench primary benchmark definitions。
- **Access and Verification Status:** Verified；当前 revision 与 v1 owner date 均核对。
- **Full-read Coverage:** data construction、three-stage pipeline、offline verifier、training、三类 benchmark、cost、ablation、异常案例与 appendix 已覆盖。
- **Original Problem:** multi-turn tool-use 数据昂贵，直接让强模型端到端模拟容易产生不一致的 tool state 与不可验证轨迹。
- **Why the Previous Design Was Reasonable:** 单轮 synthetic function calls 易生成、易过滤，在短任务中足够；人工轨迹质量高但成本大。
- **Changed Constraint:** 长对话需要 tool result 改变后续状态，数据生成必须保持 schema、parameter、environment 与 dialogue consistency。
- **Mechanism:** 先生成 coarse full skeleton，再 mask-and-fill 逐段 refinement，最后由 offline verifier 验证轨迹并过滤。
- **State Ownership:** skeleton 拥有全局任务结构；refinement stage 拥有局部内容；verifier 拥有 acceptance；tool simulator 拥有 observation truth。
- **Control Flow / Data Flow:** task/tool spec → skeleton → masked segment refinement → verifier → accepted trajectory → SFT/evaluation。
- **Implementation Details:** 使用 Llama-3.1-8B 系列训练；8K sample 成本表公开 API calls、tokens 与价格，不能外推为任意 provider 成本。
- **Evaluation Contract:** BFCL-v3、ACEBench、tau-Bench；tau-Bench Airline base 26% 与 empty-action 现象显示 harness/answer policy 会改变 score。
- **Baselines / Ablations / Sensitivity / Overhead:** 与 multi-agent simulation 比较；移除 verifier 约降 2.4 个绝对点，移除 refinement 影响更大；有生成成本而无 production latency。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** model family 披露；training hardware、precision、batch、serving concurrency 与 SLO 不完整。
- **What the Evidence Proves / Does Not Prove:** 证明结构化生成加 verifier 在其数据与 benchmark 上优于简单 synthetic baseline；不证明 synthetic trajectory 与真实 tool deployment 等价。
- **Limitations / Threats to Validity:** verifier bias、simulator realism、benchmark leakage、tau-Bench evaluator artifact 与 provider pricing drift。
- **Trade-offs / New Failure Modes:** 降低人工成本，却新增 verifier false accept/reject、synthetic style collapse 与 simulation-to-production gap。
- **Where the Previous Design Still Applies:** 高风险工具、稀有失败模式或环境难模拟时，人工/真实日志仍应为主。
- **Evolution Relationship:** `Direct Evolution`：single-turn synthetic data → multi-turn skeleton → local refinement → verifier-gated trajectory。
- **ROADMAP Node:** `TRAIN-DATA`（Ch27），handoff `AGENT-WORKFLOW`（Ch81）与 `PLATFORM-EVALUATION-SYSTEM`（Ch66）。
- **Target and Adjacent Chapters Read:** Ch26～28、Ch80～82、Ch65～67 已定位。
- **Existing Coverage:** data pipeline 与 workflow evidence 已有 owner；本 family 补充 verifier 对 multi-turn state consistency 的责任。
- **Integration Decision:** `Books Pending — Evidence Complete`。
- **Changed Files or Rejection Reason:** 仅本 Weekly。
- **Open Questions:** verifier 如何对真实 tool side effect、权限错误与 temporal drift 做校准？

### Reinforcement Learning with Rubric Anchors

- **Candidate / Week / Score:** Reinforcement Learning with Rubric Anchors / 2025-W34 / 25/30。
- **Source Family ID:** `ARXIV-2508.12790`。
- **Source Type:** full research paper、rubric dataset 与 RL experiments。
- **Event Date / First-public Date / Revision History:** arXiv v1 2025-08-18；后续 revision 归同 family。
- **Direct Primary Sources:** arXiv:2508.12790 HTML/PDF 与 artifact。
- **Related Primary Sources:** WritingBench、Judgemark v2、EQ-Bench3、IFEval、Collie、IFScale definitions。
- **Access and Verification Status:** Verified；无外部 blocker。
- **Full-read Coverage:** rubric construction、reward formulation、Qwen-30B-A3B training、5K+ samples、>10K rubrics、open-ended/constraint benchmarks、appendix 与 validity threats 已读。
- **Original Problem:** RLVR 依赖 exact verifier，难覆盖 creative writing、style、helpfulness 等开放目标。
- **Why the Previous Design Was Reasonable:** 数学/code 的 programmatic reward 可复现、低噪声，能限制 reward hacking。
- **Changed Constraint:** 开放回答没有单一答案，需要把 task-specific quality dimensions 显式化为可审计 reward contract。
- **Mechanism:** 为 prompt 构造 rubric anchors，以 judge 对逐项标准的满足度形成 reward，再对 policy 做 RL。
- **State Ownership:** rubric dataset 拥有 quality taxonomy；judge 拥有 item scoring；trainer 拥有 reward aggregation；policy 只生成 response。
- **Control Flow / Data Flow:** prompt + rubric → response rollout → rubric judge → scalar/structured reward → policy update。
- **Implementation Details:** Qwen-30B-A3B、5K+ training samples 与 10K+ rubrics；训练 recipe 的部分 infrastructure 细节未充分披露。
- **Evaluation Contract:** Creative Writing V3、WritingBench、Judgemark v2、EQ-Bench3 与 instruction-following suites；结果属于作者 judge/harness。
- **Baselines / Ablations / Sensitivity / Overhead:** 与无 rubric/其他 post-training 比较；缺跨 judge family、adversarial rubric 与长期 reward-hacking sensitivity。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** model 披露；hardware、precision、batch、rollout concurrency 与 cost/SLO 不完整。
- **What the Evidence Proves / Does Not Prove:** 证明 rubric-anchored reward 可在其开放 benchmark 改善 score；不证明 judge score 等同人类长期偏好或事实正确性。
- **Limitations / Threats to Validity:** rubric leakage、judge self-preference、style overfitting、reward gaming、benchmark与训练 rubric 相关性。
- **Trade-offs / New Failure Modes:** 扩大 RL 覆盖面，但将 taxonomy 与 judge bias 写入模型；维护 rubric/version 成为治理成本。
- **Where the Previous Design Still Applies:** 存在 exact verifier 时优先 programmatic reward；高风险事实任务不能只靠开放 rubric。
- **Evolution Relationship:** `Alternative Branch`：exact RLVR 与 rubric-guided open-ended RL 条件共存。
- **ROADMAP Node:** `TRAIN-RLHF`（Ch31）/`TRAIN-GRPO`（Ch33），evidence owner `PLATFORM-EVALUATION-SYSTEM`（Ch66）。
- **Target and Adjacent Chapters Read:** Ch30～34、Ch65～67 已定位。
- **Existing Coverage:** Books 已区分 objective verifier 与 model judge；本证据提供开放 reward contract 的实验分支。
- **Integration Decision:** `Books Pending — Evidence Complete`。
- **Changed Files or Rejection Reason:** 仅本 Weekly。
- **Open Questions:** rubric provenance、judge disagreement 与 reward hacking 应如何进入 release gate？

### HeroBench

- **Candidate / Week / Score:** HeroBench / 2025-W34 / 24/30。
- **Source Family ID:** `ARXIV-2508.12782`。
- **Source Type:** full benchmark paper、executable simulator 与 evaluator。
- **Event Date / First-public Date / Revision History:** v1 2025-08-18；v2 2026-04-19，同一 family。
- **Direct Primary Sources:** arXiv:2508.12782 HTML/PDF、benchmark artifact。
- **Related Primary Sources:** evaluated model APIs/model cards；不以其 marketing scores 替代 benchmark contract。
- **Access and Verification Status:** Verified。
- **Full-read Coverage:** RPG environment、resource/crafting/combat/spatial mechanics、task construction、success/progress metrics、25-model evaluation、failure examples、limitations 已读。
- **Original Problem:** text-only final-answer benchmark 无法验证长程计划是否在资源、前置条件与空间约束下可执行。
- **Why the Previous Design Was Reasonable:** static QA 便宜且复现稳定，适合局部 reasoning；短链条不需要 simulator。
- **Changed Constraint:** hierarchical plan 的错误会在几十步后显现，需要环境逐步执行并拥有 feasibility truth。
- **Mechanism:** 模型输出端到端计划，RPG simulator 执行 crafting、combat、resource 与 movement，记录最终 success 和 partial progress。
- **State Ownership:** simulator 拥有世界状态与 transition；model 拥有 plan proposal；evaluator 从 executable state 计算 score。
- **Control Flow / Data Flow:** task state → plan → simulator step execution → state transition/failure → success/progress aggregation。
- **Implementation Details:** 25 个 LLM 统一进入 simulator；hardest subset 无模型解决，显示 benchmark ceiling 而非模型普遍无规划能力。
- **Evaluation Contract:** executable success + progress；没有 production agent tool latency、cost 或 human intervention SLO。
- **Baselines / Ablations / Sensitivity / Overhead:** 多模型横评；缺对 planning scaffold、replanning、tool feedback 与 context budget 的完整消融。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** API/model names 可见；hardware、precision、batch/concurrency 与 latency SLO 不适用或未披露。
- **What the Evidence Proves / Does Not Prove:** 证明静态答案会高估可执行计划能力；不证明 RPG success 可直接代表 enterprise workflow autonomy。
- **Limitations / Threats to Validity:** deterministic text environment、无视觉/随机/多 agent、任务分布有限；simulator bug 直接污染 truth。
- **Trade-offs / New Failure Modes:** evaluator 更接近 execution，却增加环境维护、state reset、hidden dependency 与 simulator overfitting。
- **Where the Previous Design Still Applies:** 局部 planning primitives 与早期 model regression 仍可先用静态 benchmark。
- **Evolution Relationship:** `Direct Evolution`：plan text quality → executable hierarchical plan → future replanning/live environment。
- **ROADMAP Node:** `AGENT-PLANNING`（Ch79），handoff `PLATFORM-EVALUATION-SYSTEM`（Ch66）。
- **Target and Adjacent Chapters Read:** Ch78～80、Ch65～67 已定位。
- **Existing Coverage:** executable evaluation contract 已有框架；本 family 补长程资源约束案例。
- **Integration Decision:** `Books Pending — Evidence Complete`。
- **Changed Files or Rejection Reason:** 仅本 Weekly。
- **Open Questions:** 加入 observation/replanning 后，如何区分 planner、memory、tool 与 environment 的失败归因？

### Atom-Searcher

- **Candidate / Week / Score:** Atom-Searcher / 2025-W34 / 25/30。
- **Source Family ID:** `ARXIV-2508.12800`。
- **Source Type:** full paper、search trajectory data 与 RL evaluation。
- **Event Date / First-public Date / Revision History:** arXiv v1 2025-08-18；同 family revision 不重计。
- **Direct Primary Sources:** arXiv:2508.12800 HTML/PDF 与 artifact。
- **Related Primary Sources:** DeepResearcher baseline 与七个 in/out-of-domain benchmark definitions。
- **Access and Verification Status:** Verified。
- **Full-read Coverage:** Atomic Thought 定义、RRM、training/evaluation、七 benchmark、ablation 与 failure boundary 已覆盖。
- **Original Problem:** deep-research 轨迹只有终局 reward，无法定位哪次 query、reading 或 synthesis 使结果变好或变坏。
- **Why the Previous Design Was Reasonable:** 短搜索链和 exact answer 可用 outcome reward；无需额外 process labeler。
- **Changed Constraint:** 长搜索包含多次 evidence acquisition，credit assignment 稀疏且错误会被后续 prose 掩盖。
- **Mechanism:** 将轨迹切分为 Atomic Thought units，由 Retrieval Reward Model 对细粒度检索/推理单元分配 reward，再优化 policy。
- **State Ownership:** browser/search environment 拥有 evidence；Atomic Thought schema 拥有 trajectory segmentation；RRM 拥有 unit reward；policy 拥有 next action。
- **Control Flow / Data Flow:** query → atomic action/thought → retrieved evidence → RRM score → accumulated reward → policy update。
- **Implementation Details:** 建于 DeepResearcher，跨七个 in/out-domain benchmarks；RRM 与 segmentation 是耦合机制。
- **Evaluation Contract:** 作者报告跨域改善；结果绑定其 search backend、retrieval corpus、base model 与 evaluator。
- **Baselines / Ablations / Sensitivity / Overhead:** RRM 单独收益很小，Atomic Thought + RRM 才显著；额外 reward-model inference cost 未形成 production SLO。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** base family 可查；training hardware、precision、rollout batch/concurrency、search latency/SLO 不完整。
- **What the Evidence Proves / Does Not Prove:** 证明细粒度 trajectory boundary 对 reward assignment 有效；不证明 RRM score 是事实可靠性或可跨 search engine 泛化。
- **Limitations / Threats to Validity:** segmentation choice、reward model bias、retrieval freshness、benchmark leakage 与 error compounding。
- **Trade-offs / New Failure Modes:** credit 更密集，但新增 reward inference、unit-boundary gaming 与局部最优查询。
- **Where the Previous Design Still Applies:** 可程序验证的短任务仍适合 outcome reward；人工 high-stakes research 需保留 source review。
- **Evolution Relationship:** `Direct Evolution`：terminal reward → atomic trajectory state → process reward。
- **ROADMAP Node:** `TRAIN-GRPO`（Ch33），handoff `AGENT-RAG`（Ch76）/`AGENT-WORKFLOW`（Ch81）。
- **Target and Adjacent Chapters Read:** Ch32～34、Ch75～77、Ch80～82 已定位。
- **Existing Coverage:** Books 有 process reward 与 RAG provenance；本 family 连接 search state 与 credit assignment。
- **Integration Decision:** `Books Pending — Evidence Complete`。
- **Changed Files or Rejection Reason:** 仅本 Weekly。
- **Open Questions:** Atomic Thought segmentation 能否在不同 agent runtime 保持 stable identity？

### Matrix-Game 2.0

- **Candidate / Week / Score:** Matrix-Game 2.0 / 2025-W34 / 26/30。
- **Source Family ID:** `ARXIV-2508.13009`。
- **Source Type:** full world-model paper、implementation 与 interactive evaluation。
- **Event Date / First-public Date / Revision History:** arXiv v1 2025-08-18；后续 revisions 同 family。
- **Direct Primary Sources:** arXiv:2508.13009 HTML/PDF、code/project materials。
- **Related Primary Sources:** SkyReels-V2-I2V-1.3B、Wan 2.1 model cards作为 base lineage。
- **Access and Verification Status:** Verified。
- **Full-read Coverage:** action-conditioned generation、streaming control、training warmup、KV cache、cache-length ablation、quality/OOD failures 与 appendix 已读。
- **Original Problem:** video generator 可生成 plausible observation，却不保证用户 action 改变后续 world state，且全历史重算无法实时交互。
- **Why the Previous Design Was Reasonable:** offline video generation追求整体视觉质量，不需要因果控制或低 latency state commit。
- **Changed Constraint:** game/world model 要持续接收动作、保持状态并低延迟生成下一 observation。
- **Mechanism:** action-conditioned autoregressive video generation；移除 text injection，基于 SkyReels/Wan lineage训练，以 KV cache 保存局部历史并流式更新。
- **State Ownership:** environment/action stream 拥有控制输入；model latent/KV 拥有生成历史；client 拥有 commit 的 action sequence。
- **Control Flow / Data Flow:** observation/history + action → cached latent context → next frames → append/evict cache → 下一 action。
- **Implementation Details:** 约 5K warmup；352×640 输出；local cache 9 latent frames 时较早出现 artifact，cache 更小在 fidelity 与成本间折中。
- **Evaluation Contract:** interactive/video metrics 与用户研究属于作者 setting；没有物理 simulator ground truth 或真实 actuator。
- **Baselines / Ablations / Sensitivity / Overhead:** 比较 base I2V 与 cache sizes；cache length 影响 coherence/latency，但硬件端到端 SLO 披露不完整。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 1.3B base lineage、resolution 披露；precision、batch、concurrency、TTFT/frame latency hardware contract 不完整。
- **What the Evidence Proves / Does Not Prove:** 证明 action-conditioned cached generation 可形成可交互视频状态；不证明 learned transition 物理正确或可安全控制机器人。
- **Limitations / Threats to Validity:** OOD 会过饱和/退化，长程 state drift、action ambiguity 与 cache truncation 破坏 consistency。
- **Trade-offs / New Failure Modes:** 低 latency 与 controllability 换来有限历史、cache invalidation、state drift 和错误累积。
- **Where the Previous Design Still Applies:** offline high-quality video、无需 action control 时 diffusion/I2V full-context 仍合理。
- **Evolution Relationship:** `Direct Evolution`：video generation → action-conditioned transition → persistent interactive state。
- **ROADMAP Node:** `MULTIMODAL-WORLD-MODELS`（Ch25），handoff `INFER-KV-CACHE`（Ch45）。
- **Target and Adjacent Chapters Read:** Ch24～26、Ch44～46 已定位。
- **Existing Coverage:** world state 与 KV identity 已有 owner；本 family 提供两者耦合的受限案例。
- **Integration Decision:** `Books Pending — Evidence Complete`。
- **Changed Files or Rejection Reason:** 仅本 Weekly。
- **Open Questions:** 长程 rollback、branching action 与 cache identity 如何共同版本化？

### POML

- **Candidate / Week / Score:** Prompt Orchestration Markup Language / 2025-W34 / 24/30。
- **Source Family ID:** `ARXIV-2508.13948`。
- **Source Type:** full HCI/PL paper、language/tooling artifact 与 case studies。
- **Event Date / First-public Date / Revision History:** v1 2025-08-19；论文说明所有 findings 基于 2025-02 snapshot。
- **Direct Primary Sources:** arXiv:2508.13948 HTML/PDF、POML repository/docs。
- **Related Primary Sources:** PomLink/TableQA case artifacts；不将 SDK marketing 当独立证据。
- **Access and Verification Status:** Verified。
- **Full-read Coverage:** markup model、semantic tags、CSS-like presentation、templating、IDE/SDK、两 case studies、N=7 user study 与 accessibility limitations 已读。
- **Original Problem:** 大型 prompt 把角色、数据、格式与 presentation 混成不可审查字符串，修改格式会意外改变语义。
- **Why the Previous Design Was Reasonable:** 简单 prompt 直接拼接成本最低、行为显式；低复用场景不需要 DSL。
- **Changed Constraint:** 多模态/表格/文档、多人协作、版本控制与格式敏感性要求把 logical content 和 presentation 分离。
- **Mechanism:** component markup 表达 roles/tasks/examples，specialized tags 接入 heterogeneous data，CSS-like styles 控制 presentation，templating 负责动态参数。
- **State Ownership:** source document 拥有 logical prompt；style 拥有 rendering；compiler/SDK 拥有 serialization；runtime 拥有最终 model input。
- **Control Flow / Data Flow:** component tree + data + styles → renderer/compiler → concrete prompt → model；snapshot 应记录 compiler/style/data version。
- **Implementation Details:** 单个约 30 行 prompt 可派生 73,926 styles；数字说明组合空间，不等价于质量提升。
- **Evaluation Contract:** PomLink/TableQA case studies + 7 人、90 分钟 user study；样本小，主要证明 usability feasibility。
- **Baselines / Ablations / Sensitivity / Overhead:** 比较 conventional prompting；缺大团队 longitudinal study、token/latency overhead 与跨模型 format sensitivity。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 非模型训练论文；model/provider 与 prompt length 局部披露，hardware、batch、concurrency、SLO Not Disclosed。
- **What the Evidence Proves / Does Not Prove:** 证明 prompt 可被分解为 versionable artifact；不证明 POML 普遍提高 accuracy 或优于所有 template engine。
- **Limitations / Threats to Validity:** 小 user study、Feb snapshot、accessibility weaknesses、renderer/version drift 与格式对模型的不可预测影响。
- **Trade-offs / New Failure Modes:** 可维护性提升，但新增 compiler bugs、style-semantic leakage、dependency/version lock 与 escaping risk。
- **Where the Previous Design Still Applies:** 短且一次性的 prompt 用 plain text 更透明；高风险 input 仍需 runtime validation。
- **Evolution Relationship:** `Direct Evolution`：string prompt → template → typed component tree + presentation layer。
- **ROADMAP Node:** `AGENT-PROMPT`（Ch74），handoff `PLATFORM-MODEL-REGISTRY`（Ch59）与 `PLATFORM-PRODUCTION`（Ch73）。
- **Target and Adjacent Chapters Read:** Ch73～75、Ch58～60、Ch72～73 已定位。
- **Existing Coverage:** prompt engineering 与 artifact identity 已有分工；POML 是受限实现案例。
- **Integration Decision:** `Books Pending — Evidence Complete`。
- **Changed Files or Rejection Reason:** 仅本 Weekly。
- **Open Questions:** prompt compiler、model version 与 rendered bytes 应如何组成可回滚 identity？

### Embodied-R1

- **Candidate / Week / Score:** Embodied-R1 / 2025-W34 / 25/30。
- **Source Family ID:** `ARXIV-2508.13998`。
- **Source Type:** full technical report、dataset、model/artifact 与 simulation/robot evaluation。
- **Event Date / First-public Date / Revision History:** v1 2025-08-19；v2 2026-04-06（ICLR 2026）为同 family revision。
- **Direct Primary Sources:** arXiv:2508.13998 HTML/PDF、Embodied-Points-200K 与 code/model materials。
- **Related Primary Sources:** SIMPLEREnv 与 XArm task definitions。
- **Access and Verification Status:** Verified；current v2 与 v1 date 区分。
- **Full-read Coverage:** four pointing abilities、dataset pipeline、3B model、two-stage RFT/multi-task reward、11 benchmarks、SIMPLEREnv、8 real tasks、robustness 与 limitations 已读。
- **Original Problem:** VLM 的语言/视觉表示与不同 robot 的 low-level action schema不一致，形成 seeing-to-doing gap。
- **Why the Previous Design Was Reasonable:** end-to-end VLA 可直接优化动作，固定 embodiment 与充分 demonstration 下最短路径有效。
- **Changed Constraint:** data scarcity 与 embodiment heterogeneity 要求一个可跨平台复用的中间接口。
- **Mechanism:** 以 point/region 作为 embodiment-agnostic intermediate representation；Embodied-Points-200K + 两阶段 Reinforced Fine-tuning + multi-task reward 学习四类 pointing ability。
- **State Ownership:** VLM 拥有 high-level point proposal；camera calibration/robot adapter 拥有 point→action mapping；controller 与 environment 拥有执行/反馈。
- **Control Flow / Data Flow:** observation+instruction → pointing reasoning → calibrated action primitive → controller → environment transition → new observation。
- **Implementation Details:** 3B VLM；作者报告 11 benchmarks、SIMPLEREnv 56.2%、8 个 XArm tasks 87.5%，均绑定其 setup。
- **Evaluation Contract:** simulation 与真实 XArm zero-shot tasks；任务定义、camera/calibration、controller scaffold 是 score 的一部分。
- **Baselines / Ablations / Sensitivity / Overhead:** 对比强 VLM/VLA baselines并做 curriculum/reward/pointing ablation；实时 control latency 与 calibration sensitivity 不完整。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 3B model；训练/部署 hardware、precision、batch、control frequency 与 safety SLO 不完整。
- **What the Evidence Proves / Does Not Prove:** 证明 pointing interface 在其 11 benchmarks 与 8 XArm tasks 可迁移；不证明它拥有 low-level control、长期 world state 或开放环境安全性。
- **Limitations / Threats to Validity:** 少量 robot/task、camera calibration、sim-to-real gap、视觉扰动范围与 controller contribution。
- **Trade-offs / New Failure Modes:** 降低 embodiment coupling，却把 calibration、point ambiguity、occlusion 与 controller error 变成新边界。
- **Where the Previous Design Still Applies:** 高频、接触丰富、动力学敏感任务仍需 embodiment-specific policy/controller。
- **Evolution Relationship:** `Layering / Dependency`：VLM perception → point interface → low-level controller，而非 VLM 直接替代控制器。
- **ROADMAP Node:** `MULTIMODAL-EMBODIED-VLA`（Ch26）。
- **Target and Adjacent Chapters Read:** Ch25～27 已定位。
- **Existing Coverage:** Ch26 已区分 high-level reasoning 与 real-time controller；本 family 支撑 interface 分层。
- **Integration Decision:** `Books Pending — Evidence Complete`。
- **Changed Files or Rejection Reason:** 仅本 Weekly。
- **Open Questions:** pointing confidence、calibration drift 与 human override 如何进入 safety envelope？

### RynnEC

- **Candidate / Week / Score:** RynnEC / 2025-W34 / 23/30。
- **Source Family ID:** `ARXIV-2508.14160`。
- **Source Type:** full technical report、model/checkpoint、benchmark 与 code。
- **Event Date / First-public Date / Revision History:** v1 2025-08-19；v2 2025-11-18，同一 family。
- **Direct Primary Sources:** arXiv:2508.14160 HTML/PDF 与 GitHub model/benchmark materials。
- **Related Primary Sources:** base general-purpose VLM lineage与 RynnEC-Bench specification。
- **Access and Verification Status:** Verified。
- **Full-read Coverage:** region encoder、mask decoder、egocentric data pipeline、RynnEC-Bench、object property/segmentation/spatial evaluation、artifact 与限制已读。
- **Original Problem:** whole-frame video tokens难以给 embodied agent 提供可操作对象的稳定 region identity。
- **Why the Previous Design Was Reasonable:** global visual representation适合 caption/QA，计算简单且无需维护 mask state。
- **Changed Constraint:** embodied interaction 要知道“哪一个对象、在哪里、可如何作用”，需要 region-level perception output。
- **Mechanism:** 在通用 video MLLM 上增加 region encoder 与 mask decoder，支持 point/mask interaction；用 egocentric video pipeline 缓解 3D annotation scarcity。
- **State Ownership:** video encoder 拥有 temporal features；region/mask modules 拥有 object-local representation；downstream planner/controller 拥有 action semantics。
- **Control Flow / Data Flow:** egocentric frames + region query → region encoding → mask/object/spatial response → planner handoff。
- **Implementation Details:** compact architecture 与 RynnEC-Bench；code、checkpoints、benchmark公开，后续 v2 未改变 owner week。
- **Evaluation Contract:** object property、segmentation、spatial reasoning；不是 closed-loop robot success evaluation。
- **Baselines / Ablations / Sensitivity / Overhead:** 对比 region/video MLLM baselines；缺长期 tracking、occlusion、sensor delay 与 controller ablation。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** model/checkpoint披露；训练 hardware、precision、video length/batch、streaming latency/SLO 不完整。
- **What the Evidence Proves / Does Not Prove:** 证明 region-centric modules 改善其 perception benchmarks；不证明“embodied cognition core”可独立完成行动闭环。
- **Limitations / Threats to Validity:** benchmark自建、egocentric synthetic/annotated distribution、region tracking continuity 与 action evaluation缺失。
- **Trade-offs / New Failure Modes:** 提高 object locality，却新增 mask drift、region ID instability、decoder overhead 与 downstream schema mismatch。
- **Where the Previous Design Still Applies:** 全局 scene QA/caption 无需 region query时，普通 video MLLM 更简单。
- **Evolution Relationship:** `Layering / Dependency`：global video representation → region-owned state → action planner。
- **ROADMAP Node:** `MULTIMODAL-REPRESENTATION`（Ch23）与 `MULTIMODAL-EMBODIED-VLA`（Ch26）。
- **Target and Adjacent Chapters Read:** Ch22～24、Ch25～27 已定位。
- **Existing Coverage:** multimodal identity 与 embodied handoff 已有 owner；本 family 是 region-level案例。
- **Integration Decision:** `Books Pending — Evidence Complete`。
- **Changed Files or Rejection Reason:** 仅本 Weekly。
- **Open Questions:** region identity 在长视频、遮挡与多摄像头间如何 version/merge？

### DuPO

- **Candidate / Week / Score:** DuPO / 2025-W34 / 25/30。
- **Source Family ID:** `ARXIV-2508.14460`。
- **Source Type:** full paper、preference optimization experiments 与 artifact。
- **Event Date / First-public Date / Revision History:** arXiv v1 2025-08-20；无跨周重复 owner。
- **Direct Primary Sources:** arXiv:2508.14460 PDF/source 与 project materials。
- **Related Primary Sources:** translation/back-translation dual learning、DPO/RLVR primary methods。
- **Access and Verification Status:** Verified。
- **Full-read Coverage:** generalized duality、pair construction/filtering、preference objective、translation/math setups、ablation、compute overhead 与 appendix 已读。
- **Original Problem:** RLVR需昂贵 verifier且局限可验证任务；传统 dual learning 又要求严格 inverse task。
- **Why the Previous Design Was Reasonable:** exact verifier 在数学/code 信噪比高；严格 translation dual pair 有清晰 cycle consistency。
- **Changed Constraint:** 希望在无人工标签、非严格双向任务上获得 intrinsic feedback，同时避免错误 pseudo-label 自强化。
- **Mechanism:** 构造 generalized dual problems，让一个方向的输出在另一方向被验证并形成 preference pairs；unknown-component selection 过滤数学 pair，再做 dual preference optimization。
- **State Ownership:** dual-task constructor 拥有 pair relation；filter/verifier 拥有 acceptance；policy/reference model 拥有 preference optimization state。
- **Control Flow / Data Flow:** prompt → candidate solution → dual problem → reconstructed/verified signal → preference pair → DPO update。
- **Implementation Details:** translation 与 math；Seed-X-7B、DeepSeek-R1-Distill-Qwen 1.5B/7B、Qwen3-4B 等，结论不可跨 workload 无条件外推。
- **Evaluation Contract:** translation/math benchmarks；不同 task 的 dual relation 强度不同。
- **Baselines / Ablations / Sensitivity / Overhead:** 与 SFT/DPO/RLVR/dual baselines 比较；data filtering ablation 显著，paper承认额外生成/验证 overhead。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** model sizes披露；hardware、precision、batch、rollout concurrency、cost/SLO 不完整。
- **What the Evidence Proves / Does Not Prove:** 证明 generalized dual feedback 在其任务改善 preference learning；不证明任意任务都存在可靠 dual 或能替代 external evidence。
- **Limitations / Threats to Validity:** dual mismatch、self-confirming errors、filter selection bias、compute amplification 与 narrow task families。
- **Trade-offs / New Failure Modes:** 减少人工标签，却增加双向生成成本和 correlated verifier errors。
- **Where the Previous Design Still Applies:** 有 exact verifier 时 RLVR更直接；不存在可信 dual mapping 时应保留人工/外部评审。
- **Evolution Relationship:** `Alternative Branch`：external verifier reward 与 intrinsic dual feedback 条件共存。
- **ROADMAP Node:** `TRAIN-DPO`（Ch34），handoff `PLATFORM-EVALUATION-SYSTEM`（Ch66）。
- **Target and Adjacent Chapters Read:** Ch33～35、Ch65～67 已定位。
- **Existing Coverage:** DPO preference contract已有；本 family 新增 preference data 的 intrinsic provenance。
- **Integration Decision:** `Books Pending — Evidence Complete`。
- **Changed Files or Rejection Reason:** 仅本 Weekly。
- **Open Questions:** 如何检测 dual verifier 与 policy 的相关错误，而不是把一致性误当正确性？

### NVIDIA Nemotron Nano 2

- **Candidate / Week / Score:** NVIDIA Nemotron Nano 2 / 2025-W34 / 27/30。
- **Source Family ID:** `ARXIV-2508.14444`。
- **Source Type:** vendor technical report、open weights/model card 与 training/inference evaluation。
- **Event Date / First-public Date / Revision History:** v1 2025-08-20；v2 08-21、v3 08-25、v4 09-02。当前 HTML 为 v4，W34 只拥有 v1 event。
- **Direct Primary Sources:** arXiv:2508.14444 versions、NVIDIA model cards/weights。
- **Related Primary Sources:** Minitron pruning/distillation 与 Mamba2 primary references。
- **Access and Verification Status:** Verified；revision boundary 显式记录。
- **Full-read Coverage:** architecture、20T-token pretraining、pruning/distillation、128K extension、SFT/GRPO/DPO/RLHF、reasoning budget、A10G evaluation、limitations/model card 已读。
- **Original Problem:** dense Transformer 在边缘/单 GPU 长上下文 reasoning 上受 memory 与 decode throughput 限制。
- **Why the Previous Design Was Reasonable:** homogeneous Transformer stack成熟、kernel生态强、attention提供灵活全局交互。
- **Changed Constraint:** 需在 A10G 22GiB/BF16、128K与高吞吐条件下保持 reasoning/model quality。
- **Mechanism:** 62-layer hybrid stack（6 attention、28 FFN、28 Mamba2）；12B pretrain 后剪枝到 9B，distillation 恢复；5% truncated reasoning traces训练预算控制。
- **State Ownership:** architecture config拥有 layer types；pruning recipe拥有 parameter lineage；post-training data拥有 reasoning mode；runtime拥有 cache/state与budget control。
- **Control Flow / Data Flow:** 20T-token FP8 pretrain → pruning/distill → 128K extension → ~90B-token post-training → serving mode/budget。
- **Implementation Details:** 20T pretraining tokens、~90B post-training tokens、128K；hybrid层数与 12B→9B lineage公开。
- **Evaluation Contract:** 单 A10G、BF16、1K/8K与8K/16K prompt/output场景；作者报告相对 Qwen3-8B 约3×～6× throughput，只适用于该 contract。
- **Baselines / Ablations / Sensitivity / Overhead:** 与 dense/open models 比较并覆盖 pruning/distill；缺跨 GPU、并发、量化与严格 SLO 曲线。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** A10G 22GiB、BF16、9B、128K、两组 I/O length 披露；batch/concurrency、TTFT/TPOT percentile不完整。
- **What the Evidence Proves / Does Not Prove:** 证明 hybrid+pruning可在作者 A10G workload 提升 throughput并保持其 benchmark；不证明普遍优于 dense Transformer或 Mamba2 单独贡献。
- **Limitations / Threats to Validity:** vendor benchmark、revision内容变化、训练数据可审计性、hardware-specific kernels 与 quality/throughput coupling。
- **Trade-offs / New Failure Modes:** 降低 active compute/memory，却增加 heterogeneous layer kernels、state管理、pruning lineage与调参复杂度。
- **Where the Previous Design Still Applies:** 大集群、成熟 attention kernels、需稳定 arbitrary retrieval 时 dense Transformer仍合理。
- **Evolution Relationship:** `Direct Evolution`：dense stack → hybrid state-space/attention → structured pruning/distillation → explicit reasoning budget。
- **ROADMAP Node:** `MODEL-TRANSFORMER-LAYER`（Ch17）、`TRAIN-PRETRAINING`（Ch28）、`INFER-REQUEST-LIFECYCLE`（Ch42）。
- **Target and Adjacent Chapters Read:** Ch16～18、Ch27～29、Ch41～43 已定位。
- **Existing Coverage:** hybrid layer、pruning与 request budget 分散在三个 owner；后续 Books 只允许短 handoff。
- **Integration Decision:** `Books Pending — Evidence Complete`。
- **Changed Files or Rejection Reason:** 仅本 Weekly。
- **Open Questions:** v1→v4具体实验修订、跨 hardware kernel maturity 与并发下的 state-memory curve？

### MCP-Universe

- **Candidate / Week / Score:** MCP-Universe / 2025-W34 / 25/30。
- **Source Family ID:** `ARXIV-2508.14704`。
- **Source Type:** full benchmark paper、real-server harness 与 execution evaluators。
- **Event Date / First-public Date / Revision History:** arXiv v1 2025-08-20；同 family revisions 不重计。
- **Direct Primary Sources:** arXiv:2508.14704 HTML/PDF 与 benchmark repository。
- **Related Primary Sources:** 11 MCP server implementations、MCP specification、evaluated model/API docs。
- **Access and Verification Status:** Verified。
- **Full-read Coverage:** six domains/11 servers、task creation、format/static/dynamic evaluators、ReAct/Cursor setup、results、long-context/unknown-tool failures 与 appendix 已读。
- **Original Problem:** 静态 function-call benchmark 不覆盖真实 server、temporal truth、长程 interaction 与陌生工具空间。
- **Why the Previous Design Was Reasonable:** mock tools可冻结环境、快速 regression，适合 syntax 与 local planning。
- **Changed Constraint:** repository、browser、finance、3D、navigation、search 等真实任务会随时间与外部 state 改变。
- **Mechanism:** 六域、11 real MCP servers；format evaluator 检查协议，static evaluator检查稳定内容，dynamic evaluator实时获取 ground truth。
- **State Ownership:** server拥有 external state；dynamic evaluator拥有 time-aligned truth；agent拥有 plan/tool call；harness拥有 transcript。
- **Control Flow / Data Flow:** task → agent/ReAct → MCP calls → live state → evaluator按 format/static/dynamic 路径判定。
- **Implementation Details:** 覆盖 large tool space与长 context；enterprise Cursor未优于标准 ReAct 是该版本/配置结果。
- **Evaluation Contract:** 作者报告 GPT-5 43.72%、Grok-4 33.33%、Claude-4.0-Sonnet 29.44%；绑定六域/11 server、当时 API 与 harness。
- **Baselines / Ablations / Sensitivity / Overhead:** 多 agent/model横评；缺 server outage、credential、rate-limit、prompt budget 与 evaluator freshness sensitivity。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** API models披露；hardware/precision不可见，context随step快速增长；batch/concurrency/latency/cost SLO不完整。
- **What the Evidence Proves / Does Not Prove:** 证明真实 MCP execution 显著难于静态 tool use；不证明低 score 完全由 model capability造成。
- **Limitations / Threats to Validity:** server drift、API version、network、rate limits、dynamic evaluator correctness 与 domain coverage。
- **Trade-offs / New Failure Modes:** realism提高，但复现性下降，并引入 credential、side effect、temporal leakage 与 evaluator race。
- **Where the Previous Design Still Applies:** CI regression仍需 frozen mock server；live benchmark适合定期 readiness而非每次 unit test。
- **Evolution Relationship:** `Direct Evolution`：static schema → real MCP server → time-aware executable evidence。
- **ROADMAP Node:** `AGENT-MCP`（Ch83）与 `PLATFORM-EVALUATION-SYSTEM`（Ch66）。
- **Target and Adjacent Chapters Read:** Ch82～84、Ch65～67 已定位。
- **Existing Coverage:** MCP interface与 executable evaluation已有 owner；本 family补 dynamic truth。
- **Integration Decision:** `Books Pending — Evidence Complete`。
- **Changed Files or Rejection Reason:** 仅本 Weekly。
- **Open Questions:** 怎样保存可重放 snapshot，同时不把动态任务退化为静态 mock？

### Quantization Meets dLLMs

- **Candidate / Week / Score:** Quantization Meets dLLMs / 2025-W34 / 24/30。
- **Source Family ID:** `ARXIV-2508.14896`。
- **Source Type:** full systematic-study paper、PTQ implementation 与 artifact。
- **Event Date / First-public Date / Revision History:** v1 2025-08-20；v3 2026-03-13，后发表期刊；owner 保持 W34。
- **Direct Primary Sources:** arXiv:2508.14896 versions、official code。
- **Related Primary Sources:** LLaDA-8B、Dream-7B、GPTQ、AWQ、SmoothQuant、QuaRot、DuQuant primary sources。
- **Access and Verification Status:** Verified；当前 v3 与 v1 date 区分。
- **Full-read Coverage:** dLLM masking/denoising、activation outliers、四 RQ、three models、quantization baselines、benchmarks、appendix 与 validity boundary 已读。
- **Original Problem:** AR LLM 的 PTQ经验未必适用于反复 denoise、full attention 的 diffusion language model。
- **Why the Previous Design Was Reasonable:** GPTQ/AWQ/SmoothQuant 针对 AR matrix/operator 分布成熟，权重量化可直接降低 memory。
- **Changed Constraint:** dLLM 在多个 denoising step重复使用 activation，outlier 与量化误差可能沿 refinement传播。
- **Mechanism:** 系统比较 weight-only 与 weight-activation PTQ；分析 bit-width、method、task category、model type，并观察 activation outliers。
- **State Ownership:** quantizer拥有 scale/group/calibration；dLLM scheduler拥有 mask/denoise state；runtime拥有 quantized kernels。
- **Control Flow / Data Flow:** calibration samples → scale/rotation/quantized weights → iterative masked denoising → task metrics。
- **Implementation Details:** LLaDA-8B-Base/Instruct、Dream-7B；weight-only group-wise per-channel group size 128；128 WikiText2 samples（AWQ用 Pile）；activation per-token。
- **Evaluation Contract:** 多 task/category/model；作者结论为 weight-only 4-bit通常可用，W-A 8-bit可容忍而4-bit仍难，不能跨未来 dLLM 无条件外推。
- **Baselines / Ablations / Sensitivity / Overhead:** GPTQ vs AWQ、SmoothQuant/QuaRot/DuQuant；比较 bit/model/task，缺真实 kernel latency、energy与 denoise-step SLO。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 7B/8B与 bit-width披露；GPU、batch/concurrency、sequence length、latency/energy SLO 不完整。
- **What the Evidence Proves / Does Not Prove:** 证明 AR PTQ排序在其三 dLLM 上发生变化且4-bit activation困难；不证明 diffusion universally需要独立 quantizer。
- **Limitations / Threats to Validity:** 仅三早期 dLLM、PTQ非 QAT、缺 production kernels、current v3相对 v1可能补实验。
- **Trade-offs / New Failure Modes:** memory降低，但 iterative error、mask-step sensitivity、outlier clipping 与 kernel fragmentation增加。
- **Where the Previous Design Still Applies:** AR模型与 weight-only deployment仍可沿用成熟 PTQ；W8A8是更稳健 dLLM baseline。
- **Evolution Relationship:** `Principle Reuse`：AR PTQ principle迁移到 dLLM，但 calibration/error contract改变。
- **ROADMAP Node:** `MULTIMODAL-GENERATIVE-PARADIGMS`（Ch24）与 `INFER-TENSORRT-LLM` execution owner（Ch49）。
- **Target and Adjacent Chapters Read:** Ch23～25、Ch48～50 已定位。
- **Existing Coverage:** generation paradigm与 execution-plan量化已分 owner；本 family是跨章 handoff案例。
- **Integration Decision:** `Books Pending — Evidence Complete`。
- **Changed Files or Rejection Reason:** 仅本 Weekly。
- **Open Questions:** denoise step、mask schedule 与量化 scale是否应联合自适应？

### Deep Think with Confidence

- **Candidate / Week / Score:** Deep Think with Confidence / 2025-W34 / 26/30。
- **Source Family ID:** `ARXIV-2508.15260`。
- **Source Type:** full paper、test-time algorithm 与 extensive appendix/ablation。
- **Event Date / First-public Date / Revision History:** arXiv v1 2025-08-21；无跨周重复 owner。
- **Direct Primary Sources:** arXiv:2508.15260 HTML/PDF/source。
- **Related Primary Sources:** Qwen3、GPT-OSS model cards；AIME/HMMT/BRUMO task definitions。
- **Access and Verification Status:** Verified。
- **Full-read Coverage:** token entropy/confidence、average/group/lowest/tail confidence、offline/online algorithms、math evaluation、threshold/warmup/filter/metric ablations 与 limitations 已读。
- **Original Problem:** self-consistency固定生成大量完整 traces，边际 accuracy下降且 token cost高。
- **Why the Previous Design Was Reasonable:** majority vote 不依赖额外 verifier，implementation简单；样本独立时提高解题稳定性。
- **Changed Constraint:** 大 budget 下大量低质量 trace 可在生成早期识别，需要把 compute allocation变为 online control。
- **Mechanism:** token confidence为 top-k token negative average log-probability；滑动窗口形成 group confidence，以 lowest/local signals过滤 trace，online阶段结合 warmup与 consensus threshold早停。
- **State Ownership:** model logits拥有 confidence signal；scheduler拥有 trace pool、warmup、threshold与 budget；vote aggregator拥有 final answer。
- **Control Flow / Data Flow:** parallel samples → token/group confidence → prune/retain → consensus check → early stop or continue → weighted/filtered vote。
- **Implementation Details:** 典型 group window 1024/2048；online warmup 16；threshold/retention等是 workload policy而非模型真值。
- **Evaluation Contract:** Qwen3/GPT-OSS、数学任务、最高 512 traces；AIME25作者报告最高99.9%与最多84.7% token reduction，是高预算/特定配置结果。
- **Baselines / Ablations / Sensitivity / Overhead:** majority/global confidence baseline；τ=0.95在 Qwen3-32B/AIME24保 accuracy并省 token，τ更激进开始掉点；warmup、retention、metric均消融。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** model与trace budget披露；hardware、precision、parallel concurrency、wall-clock、TTFT/TPOT/SLO不完整。
- **What the Evidence Proves / Does Not Prove:** 证明 local confidence可在其 math workload更有效分配采样预算；不证明 confidence是 calibrated correctness/factuality probability。
- **Limitations / Threats to Validity:** confident-wrong、跨模型 calibration drift、数学答案可投票、trace correlation与高 warmup cost。
- **Trade-offs / New Failure Modes:** 省 token并可能提 accuracy，但引入阈值调度、低置信正确分支被剪与错误共识早停。
- **Where the Previous Design Still Applies:** 小 budget、开放回答无 stable vote、或 confidence不可取时多数投票/外部 verifier仍合理。
- **Evolution Relationship:** `Direct Evolution`：fixed sample budget → post-hoc confidence selection → online confidence-aware routing。
- **ROADMAP Node:** `INFER-SCHEDULING`（Ch56），handoff `MODEL-SAMPLING`（Ch20）和 `PLATFORM-EVALUATION-SYSTEM`（Ch66）。
- **Target and Adjacent Chapters Read:** Ch19～21、Ch55～57、Ch65～67 已定位。
- **Existing Coverage:** sampling与scheduler已有 budget owner；本 family提供局部 signal与 sensitivity。
- **Integration Decision:** `Books Pending — Evidence Complete`。
- **Changed Files or Rejection Reason:** 仅本 Weekly。
- **Open Questions:** 非数学任务如何用 external evidence校准 confidence，并避免 correlated traces造成虚假共识？

### Mobile-Agent-v3

- **Candidate / Week / Score:** Mobile-Agent-v3 / 2025-W34 / 26/30。
- **Source Family ID:** `ARXIV-2508.15144`。
- **Source Type:** full system paper、GUI-Owl model、environment/RL infrastructure 与 code。
- **Event Date / First-public Date / Revision History:** v1 2025-08-21；v2 2025-09-01，同一 family。
- **Direct Primary Sources:** arXiv:2508.15144 HTML/PDF 与 GitHub/model materials。
- **Related Primary Sources:** AndroidWorld、OSWorld benchmark/environment definitions。
- **Access and Verification Status:** Verified。
- **Full-read Coverage:** multi-OS cloud environment、self-evolving trajectory production、GUI-Owl capabilities、async RL、trajectory-aware relative policy optimization、benchmarks、ablation 与 limitation boundary 已读。
- **Original Problem:** GUI agent缺真实交互轨迹，静态 screenshots无法训练长期 action semantics与 recovery。
- **Why the Previous Design Was Reasonable:** supervised grounding/planning数据安全可控；单 OS emulator易复现。
- **Changed Constraint:** Android/Ubuntu/macOS/Windows 的状态、UI drift、长轨迹与稀疏成功信号要求可重置环境和持续数据生产。
- **Mechanism:** cloud virtual environments生成 query并验证轨迹，GUI-Owl迭代改进数据；fully asynchronous RL + trajectory-aware relative policy optimization做 online alignment。
- **State Ownership:** environment manager拥有 OS snapshot/reset；trajectory store拥有 provenance；validator拥有 correctness；policy/trainer拥有 rollout与update。
- **Control Flow / Data Flow:** environment state → query → GUI actions/observations → correctness validation → trajectory curation → async RL → new policy。
- **Implementation Details:** GUI-Owl-7B覆盖 grounding/QA/planning/action；framework可组合 multi-agent，但不是增加 agent 数就必然更强。
- **Evaluation Contract:** 作者报告 GUI-Owl-7B AndroidWorld 66.4/OSWorld 29.4，Mobile-Agent-v3 73.3/37.7，TRPO OSWorld 34.9；版本/scaffold关键。
- **Baselines / Ablations / Sensitivity / Overhead:** 比较模型/framework与 RL variants；缺 cloud cost、reset failure、UI version drift与 human takeover sensitivity。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 7B披露；训练硬件、precision、async worker count、action latency、并发/SLO不完整。
- **What the Evidence Proves / Does Not Prove:** 证明 environment+trajectory+async RL co-design在其 GUI benchmarks有效；不证明 unattended production autonomy或跨 app 安全。
- **Limitations / Threats to Validity:** benchmark version、environment determinism、validator errors、self-generated data bias、credential/side-effect风险。
- **Trade-offs / New Failure Modes:** 扩大数据与闭环学习，却新增环境成本、stale policy rollout、trajectory contamination与 destructive action。
- **Where the Previous Design Still Applies:** 高风险 GUI 流程仍应规则化 workflow/human approval；静态 grounding benchmark适合早期 regression。
- **Evolution Relationship:** `Direct Evolution`：static GUI data → resettable environment → self-evolving trajectories → async online RL。
- **ROADMAP Node:** `AGENT-WORKFLOW`（Ch81），handoff `TRAIN-GRPO`（Ch33）与 `PLATFORM-EVALUATION-SYSTEM`（Ch66）。
- **Target and Adjacent Chapters Read:** Ch80～82、Ch32～34、Ch65～67 已定位。
- **Existing Coverage:** durable workflow与 environment evaluation已有；本 family连接 trajectory production与async policy update。
- **Integration Decision:** `Books Pending — Evidence Complete`。
- **Changed Files or Rejection Reason:** 仅本 Weekly。
- **Open Questions:** stale rollout、OS snapshot identity、human override与 credential boundary如何统一记录？

### LiveMCP-101

- **Candidate / Week / Score:** LiveMCP-101 / 2025-W34 / 24/30。
- **Source Family ID:** `ARXIV-2508.15760`。
- **Source Type:** full benchmark paper、live tools 与 parallel-reference evaluator。
- **Event Date / First-public Date / Revision History:** v1 2025-08-21；v2 2026-05-22，同一 family。
- **Direct Primary Sources:** arXiv:2508.15760 HTML/PDF 与 artifact。
- **Related Primary Sources:** MCP specification与各 server primary docs。
- **Access and Verification Status:** Verified；v2 current内容不改变 v1 owner。
- **Full-read Coverage:** 101 queries、tool coordination、parallel reference plan、evaluation pipeline、frontier model experiments、seven failure modes、risk discussion 已读。
- **Original Problem:** live tool结果随时间变化，离线 gold answer会陈旧，导致正确 agent被误判或错误 agent因旧答案获分。
- **Why the Previous Design Was Reasonable:** frozen expected output复现性高，静态 API/数据足够时成本低。
- **Changed Constraint:** weather/search/market等动态工具必须在相同时刻产生 comparison truth。
- **Mechanism:** target agent与执行validated plan的 reference agent并行调用真实 MCP tools；实时 outputs支持 temporal alignment evaluation。
- **State Ownership:** reference plan拥有 intended procedure；live servers拥有 current data；target/reference transcripts拥有 evidence；evaluator拥有 comparison rule。
- **Control Flow / Data Flow:** query → target与reference并行 execution → live tool responses → output normalization/comparison → diagnosis。
- **Implementation Details:** 101 real-world multi-tool queries；七类错误覆盖 planning、parameterization、output handling。
- **Evaluation Contract:** frontier LLM success低于60%是其 101 queries、当时 server/API与 evaluator结果；不能当通用 agent success rate。
- **Baselines / Ablations / Sensitivity / Overhead:** 多模型/agent比较和 error taxonomy；缺 network jitter、reference-plan error、rate limit与 repeated-run variance完整分析。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** API模型可见；hardware/precision不可见；parallel evaluation增加 calls/cost，latency/concurrency/SLO不完整。
- **What the Evidence Proves / Does Not Prove:** 证明 parallel live reference可缓解 stale gold；不证明 reference agent永远正确，也不完全隔离 external nondeterminism。
- **Limitations / Threats to Validity:** 两路请求仍可能观察不同瞬时状态；validated plan可过时；server outage与 side effects影响判定。
- **Trade-offs / New Failure Modes:** temporal validity提高，但成本翻倍、race condition、reference contamination与不可重放性增加。
- **Where the Previous Design Still Applies:** deterministic tools应继续用 frozen gold；live parallel只用于动态 subset。
- **Evolution Relationship:** `Direct Evolution`：static gold → timestamped live evidence → parallel reference execution。
- **ROADMAP Node:** `AGENT-MCP`（Ch83）与 `PLATFORM-EVALUATION-SYSTEM`（Ch66）。
- **Target and Adjacent Chapters Read:** Ch82～84、Ch65～67 已定位。
- **Existing Coverage:** dynamic evaluator是 MCP-Universe 的相邻分支；同周不合并 Source Family。
- **Integration Decision:** `Books Pending — Evidence Complete`。
- **Changed Files or Rejection Reason:** 仅本 Weekly。
- **Open Questions:** 如何记录 temporal tolerance与reference-plan version，使失败可复盘？

### Intern-S1

- **Candidate / Week / Score:** Intern-S1 / 2025-W34 / 27/30。
- **Source Family ID:** `ARXIV-2508.15763`。
- **Source Type:** full technical report、open model/artifacts 与 extensive training/evaluation。
- **Event Date / First-public Date / Revision History:** v1 2025-08-21；v2 2025-08-24，均在 W34，同一 family。
- **Direct Primary Sources:** arXiv:2508.15763 v1/v2、model card、code/data artifacts。
- **Related Primary Sources:** InternLM/InternVL lineage与 scientific benchmark definitions。
- **Access and Verification Status:** Verified；v2为周内 revision，计一次。
- **Full-read Coverage:** 241B/28B MoE、dynamic scientific tokenizer、5T continued pretraining、SFT mixture、offline/online RL、Mixture-of-Rewards、science/multimodal evaluation、ablation与 appendix 已读。
- **Original Problem:** 通用 tokenizer/data/reward对 SMILES、FASTA、scientific diagrams 与跨学科 reasoning效率低，单一 benchmark reward又易偏科。
- **Why the Previous Design Was Reasonable:** static tokenizer稳定、通用 corpus规模大、统一 reward pipeline维护简单。
- **Changed Constraint:** scientific modalities有可识别结构、稀有 token frequency与多任务冲突，需要 modality-aware representation和多 source reward。
- **Mechanism:** 241B total/28B active MoE；rule/tag检测 scientific strings并用不同 tokenizer/orthogonal embeddings；5T continued tokens（>2.5T science）；SFT mixture ablation；offline+online RL与 >1000 tasks Mixture-of-Rewards。
- **State Ownership:** detector/tokenizer拥有 modality segmentation；embedding spaces拥有 representation identity；data mixer拥有 sampling；reward registry拥有 task/verifier mapping；router拥有 expert activation。
- **Control Flow / Data Flow:** modality detection → specialized tokenization/embedding concat → MoE pretraining → curated SFT mixture → task-routed rewards → RL update。
- **Implementation Details:** report宣称 SMILES token compression >70%；是其 tokenizer/data结果，不能等同下游质量提升。
- **Evaluation Contract:** scientific text/multimodal/general benchmarks；数据 component先 atomic validation再 compositional mixture validation。
- **Baselines / Ablations / Sensitivity / Overhead:** tokenizer/data mixture/reward等有ablation；缺完整 hardware、per-task reward conflict、routing load与 serving cost曲线。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 241B/28B、5T与>2.5T science tokens披露；hardware、precision、batch/concurrency、serving SLO不完整。
- **What the Evidence Proves / Does Not Prove:** 证明 scientific modality/data/reward co-design在作者 suite有效；不证明统一模型普遍优于领域模型或 dynamic tokenizer没有 robustness cost。
- **Limitations / Threats to Validity:** 巨量作者自建数据、benchmark contamination、detector/tag错误、dynamic tokenization context sensitivity、MoR conflict不可见。
- **Trade-offs / New Failure Modes:** 压缩与领域能力提升，却新增 tokenizer identity、embedding alignment、reward routing与 mixture governance复杂度。
- **Where the Previous Design Still Applies:** 通用自然语言、跨域稳定性优先时 static tokenizer/统一 embedding更简单；窄科学任务可用专用模型。
- **Evolution Relationship:** `Layering / Dependency`：general MoE → scientific modality representation → curated data mixture → task-routed post-training。
- **ROADMAP Node:** `MODEL-MOE`（Ch21）、`MULTIMODAL-REPRESENTATION`（Ch23）、`TRAIN-PRETRAINING`（Ch28）、`TRAIN-GRPO`（Ch33）。
- **Target and Adjacent Chapters Read:** Ch20～24、Ch27～29、Ch32～34 已定位。
- **Existing Coverage:** owners已存在；不得把 Intern-S1写成一个跨章产品清单。
- **Integration Decision:** `Books Pending — Evidence Complete`。
- **Changed Files or Rejection Reason:** 仅本 Weekly。
- **Open Questions:** tokenizer/artifact compatibility、MoR conflict与 expert load如何进入 reproducible training contract？

### DeepSeek-V3.1

- **Candidate / Week / Score:** DeepSeek-V3.1 / 2025-W34 / 25/30。
- **Source Family ID:** `DEEPSEEK-V3.1-2025`（W39 Terminus为 corrective revision）。
- **Source Type:** official release/API changelog、open weights/model card/tokenizer/chat template；无独立 technical report。
- **Event Date / First-public Date / Revision History:** 2025-08-21；2025-09-22 V3.1-Terminus纠错，不能倒写为初始事实。
- **Direct Primary Sources:** DeepSeek API updates、V3.1 Base/Instruct artifacts、tokenizer/template与 thinking/tool docs。
- **Related Primary Sources:** DeepSeek-V3/R1 lineage、V3.1-Terminus、V3.2-Exp/V3.2。
- **Access and Verification Status:** Verified for version/artifact/API contract；internal hybrid training/router Not Disclosed。
- **Full-read Coverage:** release/API/model card/template、mode aliases、128K、tool interface、840B continued-pretraining disclosure与 benchmark notes 已读；无 report故不能声称 method/ablation已公开。
- **Original Problem:** separate chat/reasoning checkpoints让 fleet、parser与 rollback分裂，而 agent workload希望 reasoning中调用工具。
- **Why the Previous Design Was Reasonable:** 专用 R1/V3 行为清晰、可独立SLO和回滚；direct请求不承担 reasoning tokens。
- **Changed Constraint:** 同一128K endpoint需按请求提供 think/non-think并复用 tool ecosystem。
- **Mechanism:** 可核实的只有 `deepseek-chat` non-thinking、`deepseek-reasoner` thinking、同一 V3.1 family、strict function calling beta与840B continued tokens；内部 mode control未公开。
- **State Ownership:** API alias/router拥有 mode mapping；artifact/template拥有 serialization；runtime拥有 reasoning/tool parser；workflow拥有 tool authority。
- **Control Flow / Data Flow:** request+alias → artifact/template → thinking/direct generation → tool proposal/parser → workflow；内部训练流 Not Disclosed。
- **Implementation Details:** weights与 tokenizer/template公开；optimizer、parallelism、quantization和 parser reference contract不完整。
- **Evaluation Contract:** 官方 SWE-bench/Multilingual/Terminal-bench与 reasoning efficiency；hardware、sampling、scaffold、token budget、concurrency不完整。
- **Baselines / Ablations / Sensitivity / Overhead:** 与前代/R1-0528比较；无 hybrid-vs-separate、mode contamination、tool post-training消融。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 128K、840B continued tokens披露；hardware、precision、batch/concurrency、TTFT/TPOT/SLO Not Disclosed。
- **What the Evidence Proves / Does Not Prove:** 证明 hybrid mode成为公开 API/artifact contract；不证明单 checkpoint普遍优于双 fleet或其内部路由方式。
- **Limitations / Threats to Validity:** mechanism披露不足、benchmark条件缺失、strict beta；一个月后出现 language/abnormal-character corrective release。
- **Trade-offs / New Failure Modes:** 减少 fleet分裂，却新增 alias漂移、reasoning-state/parser compatibility与 template migration。
- **Where the Previous Design Still Applies:** 强SLO隔离、需独立回滚或 runtime不支持 reasoning/tool channels时双 fleet仍合理。
- **Evolution Relationship:** `Direct Evolution`：V3 chat + R1 → V3.1 hybrid public contract → Terminus correction → V3.2 integration。
- **ROADMAP Node:** `MODEL-SAMPLING`（Ch20）、`TRAIN-RLHF`（Ch31）、`INFER-REQUEST-LIFECYCLE`（Ch42）、`INFER-DYNAMO`（Ch52）、`PLATFORM-GATEWAY`（Ch62）、`AGENT-PROMPT`（Ch74）。
- **Target and Adjacent Chapters Read:** 对应 owner相邻章节已定位；Books Gate关闭。
- **Existing Coverage:** artifact/parser/routing contract已有；V3.1主要是 version fact。
- **Integration Decision:** `Weekly Only — Version/Product Fact / Mechanism Not Disclosed`。
- **Changed Files or Rejection Reason:** 不改 Books；机制未公开且既有 chapters已覆盖接口原则。
- **Open Questions:** internal mode control、exact harness、Terminus修正范围与独立 serving evidence。

### 4DNeX

- **Candidate / Week / Score:** 4DNeX / 2025-W34 / 25/30。
- **Source Family ID:** `ARXIV-2508.13154`。
- **Source Type:** full paper、project page、dataset/reconstruction pipeline 与 generation experiments。
- **Event Date / First-public Date / Revision History:** arXiv v1 2025-08-18；当前公开版本仍为 v1，owner 固定 W34。
- **Direct Primary Sources:** arXiv:2508.13154 HTML/PDF、4DNeX project page。
- **Related Primary Sources:** Wan2.1、DUSt3R、MonST3R、MegaSaM 与 TrajectoryCrafter 的 primary papers/artifacts。
- **Access and Verification Status:** Verified；正文、公式、实验、ablation、appendix 与 limitations 可访问。
- **Full-read Coverage:** metadata、Introduction/Related Work、4DNeX-10M preprocessing、static/dynamic pseudo-annotation、RGB/XYZ formulation、fusion、LoRA architecture、experiments、user study、VBench appendix 与 limitations 已读。
- **Original Problem:** optimization-based 4D generation计算昂贵且不稳定，feed-forward方法又通常需要 video input，无法从单图生成显式动态 3D state。
- **Why the Previous Design Was Reasonable:** 多视角/video reconstruction拥有更充分几何约束；per-scene optimization在小规模高质量资产上可以换取精细一致性。
- **Changed Constraint:** 希望单图、一次前向、可批处理地产生 dynamic point cloud，同时复用 video diffusion prior，训练数据却缺真实4D ground truth。
- **Mechanism:** 把动态点云改写为 pixel-aligned RGB+XYZ的“6D video”，沿宽度融合两种 modality；冻结 VAE、用 rank-64 LoRA适配 Wan-DiT，并以 pseudo 3D/4D annotations训练。
- **State Ownership:** dataset pipeline拥有 pseudo geometry/provenance；RGB/XYZ token identity拥有 appearance/geometry correspondence；generator拥有 conditional distribution；轻量 post-optimization拥有 camera/depth recovery。
- **Control Flow / Data Flow:** 单图+初始 XYZ → VAE与width-wise fusion → flow-matching DiT → paired RGB/XYZ sequence → dynamic point cloud → novel-view renderer。
- **Implementation Details:** 4DNeX-10M含约9.2M pseudo-annotated frames；32张A100、batch 32、5K iterations、480×720每 modality、AdamW与1e-4 cosine schedule。
- **Evaluation Contract:** 与 image/video-to-4D baselines在 novel-view video、VBench、人评与效率上比较；geometry truth主要来自 pseudo annotation与rendered proxy，不是现实交互正确性。
- **Baselines / Ablations / Sensitivity / Overhead:** 比较 optimization/feed-forward family与 channel/batch/frame/height/width fusion，并验证 XYZ initialization、normalization、mask；未覆盖 multi-object interaction或真实4D label sensitivity。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 32×A100、Wan2.1 base、rank-64 LoRA、batch 32与分辨率披露；precision、serving concurrency、latency/SLO Not Disclosed。
- **What the Evidence Proves / Does Not Prove:** 证明 joint RGB/XYZ representation可在作者数据和rendering contract下支撑单图 feed-forward 4D generation；不证明其是 causal world model，也不证明 point cloud可安全替代环境 transition truth。
- **Limitations / Threats to Validity:** pseudo-label bias、单物体/非交互场景、temporal prior不足、real 4D ground truth缺失，以及当前 revision后续可能改变实验细节。
- **Trade-offs / New Failure Modes:** 去掉逐场景重优化换来吞吐与可扩展性，却把 reconstruction error固化进训练数据，并新增 RGB/XYZ alignment、camera recovery与 hallucinated geometry风险。
- **Where the Previous Design Still Applies:** 有多视角观测、要求精确几何或可接受离线优化时，reconstruction/optimization pipeline仍更可信。
- **Evolution Relationship:** `Direct Evolution`：multi-frame reconstruction / per-scene optimization → pseudo-annotated joint representation → feed-forward image-to-4D；与 action-conditioned world model只是依赖关系。
- **ROADMAP Node:** `MULTIMODAL-REPRESENTATION`（Ch23），handoff `MULTIMODAL-WORLD-MODELS`（Ch25）。
- **Target and Adjacent Chapters Read:** Ch22～26 已定位；Books Gate关闭。
- **Existing Coverage:** Books已有 representation identity与 world-model边界；本 family补充“appearance/geometry joint tokenization”案例，不将其提升为可控环境模型。
- **Integration Decision:** `Books Pending — Evidence Complete`。
- **Changed Files or Rejection Reason:** 仅本 Weekly。
- **Open Questions:** 如何用 real 4D observations、interaction与 uncertainty标注校准 pseudo geometry，并为 revision/rollback保留 scene-state provenance？

### Next Visual Granularity Generation

- **Candidate / Week / Score:** Next Visual Granularity Generation / 2025-W34 / 24/30。
- **Source Family ID:** `ARXIV-2508.12811`。
- **Source Type:** full paper、released code/models 与 ImageNet experiments。
- **Event Date / First-public Date / Revision History:** v1 2025-08-18；v2 2026-02-28（ICLR 2026），同一 family，机制描述以 current revision核验而 owner不移动。
- **Direct Primary Sources:** arXiv:2508.12811 HTML/PDF、作者 project/code/model links。
- **Related Primary Sources:** VAR、MAR、VQGAN与ImageNet evaluation definitions。
- **Access and Verification Status:** Verified；正文、appendix、released artifacts与 revision history可访问。
- **Full-read Coverage:** visual granularity construction、sequence factorization、structure-aware RoPE、content prediction/generator training、ImageNet setup、scaling、comparison、ablation、extreme cases、limitations与appendix已读。
- **Original Problem:** raster-order AR忽略二维结构并积累早期错误，next-scale方法又把图像强制为固定金字塔，缺少由内容结构定义的 coarse-to-fine state。
- **Why the Previous Design Was Reasonable:** 固定 token/raster或scale order易于 causal factorization、cache与并行实现；在文本或规则网格上 ownership清晰。
- **Changed Constraint:** 图像对象和局部纹理不服从单一读取顺序，需要在相同空间分辨率上逐步增加 unique visual tokens，保留层级可控性。
- **Mechanism:** 先将图像聚类为由少到多的 visual-granularity states，再 autoregressively预测下一 granularity；structure-aware RoPE联合编码 modality、cluster hierarchy与2D位置。
- **State Ownership:** tokenizer/clusterer拥有 granularity identity；AR model拥有 state transition；content generator拥有每级细节恢复；sampling order拥有 exposure-bias边界。
- **Control Flow / Data Flow:** image tokens → hierarchical clustering → empty/coarse state → next-granularity prediction → content fill → refined image state。
- **Implementation Details:** 在ImageNet class-conditional setup训练多种规模并公开代码/模型；当前证据聚焦标准图像生成，text-conditioned/video workload不在合同内。
- **Evaluation Contract:** FID/IS及与VAR等模型的同域比较；论文报告多个规模下FID小幅改善，数字只绑定其ImageNet tokenizer、training recipe和sampling budget。
- **Baselines / Ablations / Sensitivity / Overhead:** 对比AR/diffusion/VAR family，消融结构RoPE、granularity设计和极端结构；缺跨数据域、缓存行为与production latency sensitivity。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 参数规模和ImageNet设置披露；完整hardware、precision、batch、sampling concurrency与SLO未统一披露。
- **What the Evidence Proves / Does Not Prove:** 证明可学习 granularity sequence是固定raster/scale之外的有效生成分支；不证明该factorization普遍优于 diffusion，也不证明小幅FID差异可跨 evaluator迁移。
- **Limitations / Threats to Validity:** 仅class-conditional ImageNet、cluster/tokenizer bias、不同模型训练预算难完全等价、current v2后发细节不可倒写进v1事件。
- **Trade-offs / New Failure Modes:** 更贴近视觉层级并提供结构控制，但新增 clustering state、stage count、跨级错误传播与artifact兼容问题。
- **Where the Previous Design Still Applies:** 文本、低分辨率或cache/simple decoder优先时 raster AR仍直接；高并行采样和连续空间质量优先时 diffusion仍合理。
- **Evolution Relationship:** `Alternative Branch`：raster AR / next-scale AR / diffusion ↔ next-visual-granularity refinement，不是单向替代。
- **ROADMAP Node:** `MULTIMODAL-GENERATIVE-PARADIGMS`（Ch24），handoff `MULTIMODAL-REPRESENTATION`（Ch23）。
- **Target and Adjacent Chapters Read:** Ch22～25 已定位。
- **Existing Coverage:** 生成范式章节已有factorization比较；本 family补充content-defined hierarchy，不改变各分支共存结论。
- **Integration Decision:** `Books Pending — Evidence Complete`。
- **Changed Files or Rejection Reason:** 仅本 Weekly。
- **Open Questions:** granularity identity如何跨 tokenizer/version稳定，且在serving中怎样缓存、rollback并度量每级纠错价值？

### S²-Guidance

- **Candidate / Week / Score:** S²-Guidance / 2025-W34 / 22/30。
- **Source Family ID:** `ARXIV-2508.12880`。
- **Source Type:** full paper、training-free diffusion guidance method、T2I/T2V experiments。
- **Event Date / First-public Date / Revision History:** v1 2025-08-18；v2 2025-09-11、v3/v4 2026-03-02/04（ICLR 2026），同一 family。
- **Direct Primary Sources:** arXiv:2508.12880 HTML/PDF与作者代码声明。
- **Related Primary Sources:** classifier-free guidance、AutoGuidance/weak-model guidance及所测SD3.5、HunyuanVideo/Wan等模型材料。
- **Access and Verification Status:** Verified；当前正文、理论appendix、T2I/T2V实验和ablation可访问；代码发布状态以source页面为准。
- **Full-read Coverage:** Gaussian-mixture分析、sub-network hypothesis、stochastic block dropping、guidance公式、unbiased-estimation appendix、T2I/T2V setup、FID/HPS/CompBench/VBench、drop ratio/interval/scale ablations与限制已读。
- **Original Problem:** CFG可过度放大一个deterministic model的次优预测；另训weak model做negative guidance又增加训练、选择与部署成本。
- **Why the Previous Design Was Reasonable:** CFG无需额外 classifier且已成为稳定baseline；已有weak model时AutoGuidance能利用独立偏差方向。
- **Changed Constraint:** production未必有匹配weak model，希望只用现有checkpoint在inference时构造可用的自我负向参照。
- **Mechanism:** 每个denoising step随机drop约10% transformer blocks形成sub-network prediction，并从主模型guided prediction中减去其Monte Carlo/self-guidance方向；中间约80% noise interval应用更稳。
- **State Ownership:** base checkpoint拥有主预测；随机mask拥有sub-network identity；sampler拥有guidance scale、drop ratio与noise interval；evaluator只拥有输出质量判定。
- **Control Flow / Data Flow:** prompt/noise → full forward + stochastic dropped forward → guidance combination → next denoising state → image/video。
- **Implementation Details:** training-free但每step增加额外forward；一次stochastic application的收益/成本优于多次，drop过多导致质量下降。
- **Evaluation Contract:** T2I使用FID、HPSv2.1、T2I-CompBench等，T2V使用作者选定质量/运动指标；结论绑定所测base models、guidance scales和sampling schedule。
- **Baselines / Ablations / Sensitivity / Overhead:** 对比CFG与其他guidance，消融fixed block、drop ratio、noise interval、self-guidance scale和重复次数；缺真实serving吞吐、跨seed tail与失败重放成本。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** base model和sampling配置部分披露；统一hardware、precision、batch/concurrency、latency/SLO不完整。
- **What the Evidence Proves / Does Not Prove:** 证明随机sub-network可在作者T2I/T2V合同下改善CFG输出；不证明“内部不确定性”已被校准，也不证明额外forward在任意SLO下划算。
- **Limitations / Threats to Validity:** aesthetic/model-based evaluator bias、revision drift、stochastic variance、强依赖architecture block semantics与guidance超参。
- **Trade-offs / New Failure Modes:** 免去weak-model训练与artifact管理，却增加per-step compute、随机性、seed复现和mask/backend兼容风险。
- **Where the Previous Design Still Applies:** latency/energy敏感或CFG已满足质量时继续用CFG；已有可验证small teacher/weak model时显式双模型更易审计。
- **Evolution Relationship:** `Alternative Branch`：CFG → external weak-model guidance 或 stochastic self-guidance，非替代所有sampler。
- **ROADMAP Node:** `MULTIMODAL-GENERATIVE-PARADIGMS`（Ch24），handoff `INFER-EXECUTION`（Ch50）。
- **Target and Adjacent Chapters Read:** Ch23～25、Ch49～51 已定位。
- **Existing Coverage:** Books已有proposal/correction与iterative sampling成本；本 family补充checkpoint内部sub-network guidance案例。
- **Integration Decision:** `Books Pending — Evidence Complete`。
- **Changed Files or Rejection Reason:** 仅本 Weekly。
- **Open Questions:** 如何将额外forward的quality gain换算成energy/latency frontier，并保证seed、mask与backend revision可重放？

### Precise Action-to-Video Generation Through Visual Action Prompts

- **Candidate / Week / Score:** Precise Action-to-Video / 2025-W34 / 25/30。
- **Source Family ID:** `ARXIV-2508.13104`。
- **Source Type:** full paper、multi-domain action/video data pipeline与controllable video experiments。
- **Event Date / First-public Date / Revision History:** arXiv v1 2025-08-18；owner固定W34。
- **Direct Primary Sources:** arXiv:2508.13104 HTML/PDF与project artifact。
- **Related Primary Sources:** EgoVid/Ego4D、RT-1、DROID、CogVideoX、SAM-2/CoTracker primary sources。
- **Access and Verification Status:** Verified；method、data construction、experiments、ablation与limitations均可访问。
- **Full-read Coverage:** action representation、hand/gripper skeleton recovery、ControlNet/DiT injection、three-dataset setup、generation/action metrics、joint training、held-out skills、representation/architecture ablations和limitations已读。
- **Original Problem:** text action含歧义，robot-centric joint/end-effector state又绑定embodiment与camera，难以在human/robot、多视角数据间共享action-conditioned video model。
- **Why the Previous Design Was Reasonable:** 固定机器人与校准相机下，joint/end-effector state最精确、controller接口直接；text适合低成本弱控制。
- **Changed Constraint:** 需要统一高DoF human-hand与不同robot gripper动作，并利用大规模heterogeneous video而不先对齐所有kinematic schema。
- **Mechanism:** 把3D structural dynamics投影成2D skeleton/mesh/depth visual action prompt，通过ControlNet为主、DiT/LoRA为辅注入预训练video generator；joint training复用跨域interaction dynamics。
- **State Ownership:** skeleton extraction pipeline拥有action proxy；camera/projection拥有view identity；generator拥有observation transition；真实controller仍拥有可执行action truth。
- **Control Flow / Data Flow:** video/robot trajectory → skeleton recovery/render → initial frame + visual action sequence → conditioned DiT → predicted interaction video → fidelity/dynamics evaluator。
- **Implementation Details:** EgoVid子集约200K training clips、约120 frames/30fps；与RT-1、DROID联合训练，使用tracking/optical-flow filtering与ControlNet/LoRA适配。
- **Evaluation Contract:** PSNR、SSIM、LPIPS、FVD、ST-IoU与SAM-2 J&F绑定EgoVid/RT-1/DROID及作者prompt extraction；video quality不等于policy success。
- **Baselines / Ablations / Sensitivity / Overhead:** 对比text、raw agent state、single/joint training，消融skeleton/mesh/depth与ControlNet/main branch；mesh/depth更精确但acquisition更贵。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** datasets、clip规格、base architecture与adapter披露；training hardware、precision、batch、serving concurrency/control-frequency/SLO不完整。
- **What the Evidence Proves / Does Not Prove:** 证明visual action proxy可在三数据集改善作者video dynamics合同并支持cross-domain training；不证明生成video构成causal simulator或可直接控制真实robot。
- **Limitations / Threats to Validity:** 2D prompt缺3D cues、skeleton recovery error、camera dependence、model-based tracking metric与held-out skill样本有限。
- **Trade-offs / New Failure Modes:** 获得跨embodiment共享与低成本标注，却丢失force/depth/contact state，并可能生成视觉正确但物理不可行的transition。
- **Where the Previous Design Still Applies:** 单一robot、精确calibration与closed-loop control下原生joint/action state仍是canonical；text仍适合粗粒度story control。
- **Evolution Relationship:** `Layering / Dependency`：agent-specific action state → projected visual action interface → predicted observation；不是VLA policy的直接替代。
- **ROADMAP Node:** `MULTIMODAL-WORLD-MODELS`（Ch25）与`MULTIMODAL-EMBODIED-VLA`（Ch26）。
- **Target and Adjacent Chapters Read:** Ch24～27 已定位。
- **Existing Coverage:** Books已有action-conditioned transition与physical-action边界；本family补充跨embodiment visual interface证据。
- **Integration Decision:** `Books Pending — Evidence Complete`。
- **Changed Files or Rejection Reason:** 仅本 Weekly。
- **Open Questions:** 2D proxy如何携带depth/contact/force uncertainty，并在closed-loop controller中校验物理可行性与rollback？

### FLARE

- **Candidate / Week / Score:** FLARE / 2025-W34 / 27/30。
- **Source Family ID:** `ARXIV-2508.12594`。
- **Source Type:** full paper、PyTorch implementation、PDE/long-sequence experiments与released dataset。
- **Event Date / First-public Date / Revision History:** v1 2025-08-18；v2 2025-10-15、v3 2026-01-30，同一 family；current revision用于机制核验。
- **Direct Primary Sources:** arXiv:2508.12594 HTML/PDF、FLARE.py repository与LPBF dataset。
- **Related Primary Sources:** vanilla attention、Linformer、PerceiverIO、Transolver/LNO、PyTorch SDPA/FlashAttention contracts。
- **Access and Verification Status:** Verified；method、code path、spectral analysis、benchmarks、ablation与appendix可访问。
- **Full-read Coverage:** low-rank derivation、encode/decode SDPA、head-wise latent slices、spectral proof、PDE/LRA/million-point setup、runtime/memory、all ablations、dataset protocol与implementation appendix已读。
- **Original Problem:** dense self-attention在百万mesh points上形成O(N²) time/memory；显式低秩projection又绑定固定token order并引入O(NM) layer parameters。
- **Why the Previous Design Was Reasonable:** dense attention保留任意pair interaction，短序列和语言模型上kernel成熟；latent workspace适合需要深层全局变换的任务。
- **Changed Constraint:** 无序超长mesh需要线性global communication、可解释rank bound，并复用现有fused SDPA backend。
- **Mechanism:** 每head用M个独立latent queries先gather `N→M`、再以交换Q/K的第二次SDPA scatter `M→N`；组合operator rank≤M且complexity O(NM)，无latent self-attention。
- **State Ownership:** per-head latent slice拥有routing subspace；K/V projections拥有input-dependent content；SDPA backend拥有kernel dispatch；mesh tokens保持原顺序无关identity。
- **Control Flow / Data Flow:** N input tokens → head-specific cross-attention gather → M latent values → symmetric decode/scatter → N outputs → residual MLP。
- **Implementation Details:** 两次`torch.nn.functional.scaled_dot_product_attention`、scale=1；百万点DrivAerML在单H100 80GB、batch 1、mixed precision、500 epochs运行，无offload/distributed training。
- **Evaluation Contract:** 六类PDE/engineering surrogate、million-point geometry与LRA；论文报告在单H100特定实现的速度/内存及relative L2 error，不能外推LLM decode或所有GPU。
- **Baselines / Ablations / Sensitivity / Overhead:** 与vanilla/PerceiverIO/GNOT/LNO/Transolver比较；消融M、block数、projection depth、head dimension、shared/independent latents和latent self-attention。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** H100 80GB、1M points、batch1、mixed precision与FP32 microbenchmark均披露；online concurrency、TTFT/TPOT/SLO不适用/未披露。
- **What the Evidence Proves / Does Not Prove:** 证明SDPA-native gather/scatter可在作者scientific workloads提供受控低秩global mixing和可扩展性；不证明低秩瓶颈适合causal LLM或精确注意力等价。
- **Limitations / Threats to Validity:** 任务集中PDE/mesh、current v3较v1有扩展、rank bottleneck丢失高频interaction、作者benchmark与kernel/backend版本耦合。
- **Trade-offs / New Failure Modes:** O(NM)和fused-kernel compatibility换来rank cap、M调优、head subspace collapse与不同深度容量不足。
- **Where the Previous Design Still Applies:** 短序列、需要高秩token interaction或已有FlashAttention足够快时dense attention仍更稳；latent self-attention适合需要独立workspace变换时。
- **Evolution Relationship:** `Alternative Branch`：dense attention / explicit projection / latent workspace ↔ head-wise low-rank routing。
- **ROADMAP Node:** `MODEL-ATTENTION`（Ch14），handoff `INFER-EXECUTION`（Ch50）与`TRAIN-DISTRIBUTED-TRAINING`（Ch36）。
- **Target and Adjacent Chapters Read:** Ch13～15、Ch35～37、Ch49～51 已定位。
- **Existing Coverage:** Books已有attention complexity/kernel contract；本family补充“mathematical rank bound + standard SDPA”联动案例。
- **Integration Decision:** `Books Pending — Evidence Complete`。
- **Changed Files or Rejection Reason:** 仅本 Weekly。
- **Open Questions:** 在causal masking、KV cache、variable length与multi-GPU下，latent routing的identity、communication和quality frontier是否仍成立？

### MeshCoder

- **Candidate / Week / Score:** MeshCoder / 2025-W34 / 25/30。
- **Source Family ID:** `ARXIV-2508.14879`。
- **Source Type:** full paper、Blender Python API/paired dataset pipeline与executable reconstruction experiments。
- **Event Date / First-public Date / Revision History:** v1 2025-08-20；v2 2025-08-22，同一 W34 family，不重复计分。
- **Direct Primary Sources:** arXiv:2508.14879 HTML/PDF与公开project/artifact links。
- **Related Primary Sources:** Blender Python、Infinigen-Indoor及Shape2Prog/PLAD primary sources。
- **Access and Verification Status:** Verified；正文、appendix、training recipe、evaluation与limitations可访问。
- **Full-read Coverage:** API/part dataset、part-to-code与object-to-code models、assembly、triplane tokenizer、training、reconstruction/editing/understanding、ablation、完整category tables和limitations已读。
- **Original Problem:** 直接mesh/point generation难编辑，旧shape DSL只覆盖简单primitives，复杂3D对象又缺大规模object-code pairs。
- **Why the Previous Design Was Reasonable:** 小DSL语法受控、易执行验证，简单CAD primitive下泛化和安全边界清晰。
- **Changed Constraint:** 需要表达上百parts与复杂topology，同时让输出可执行、可编辑，并从raw point cloud恢复semantic structure。
- **Mechanism:** 扩展Blender Python procedural APIs，先合成part-code pairs训练part model，再为Infinigen objects生成约1M object-code pairs；triplane tokenizer把point cloud映射到LLM tokens生成分part脚本。
- **State Ownership:** point cloud拥有observed geometry；part segmentation/tokenizer拥有representation；script拥有editable/executable artifact；Blender runtime拥有rendered mesh truth。
- **Control Flow / Data Flow:** point cloud → triplane tokens → multimodal LLM → Blender Python script → sandbox execution → mesh → CD/IoU与editing evaluation。
- **Implementation Details:** part model 64×A100约1周、20 epochs、batch512；object model 64×A100约2天、10 epochs、batch256；输入随机4,096～16,384 points并做rotation/scale/noise augmentation。
- **Evaluation Contract:** execution后采100K mesh points算L2 Chamfer Distance并用32³ voxels算IoU；shape editing/understanding另测，主要来自Infinigen/human-made categories。
- **Baselines / Ablations / Sensitivity / Overhead:** 与Shape2Prog、PLAD等比较并消融representation/components；缺organic shapes、真实扫描noise、sandbox security与script runtime tail。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 64×A100、epochs/batch/input points披露；precision、script length、serving concurrency、execution latency/SLO未完整披露。
- **What the Evidence Proves / Does Not Prove:** 证明程序化artifact可在作者synthetic-domain合同下提高可编辑重建；不证明任意3D对象可安全重建，也不证明CD/IoU涵盖semantic correctness。
- **Limitations / Threats to Validity:** human-made bias、Infinigen synthetic gap、无color、API vocabulary限制、generated code可能无效/昂贵或产生副作用。
- **Trade-offs / New Failure Modes:** 获得可执行/可编辑state和semantic parts，却把geometry能力绑定API版本、runtime sandbox、code validity与dataset self-training bias。
- **Where the Previous Design Still Applies:** organic/free-form geometry或只需visual fidelity时直接implicit/mesh generation更自然；高安全环境可继续用小DSL。
- **Evolution Relationship:** `Direct Evolution`：small shape DSL → expressive procedural API → part-decomposed executable program；与agent artifact workflow为原则复用。
- **ROADMAP Node:** `MULTIMODAL-REPRESENTATION`（Ch23），handoff `AGENT-WORKFLOW`（Ch81）与`PLATFORM-SECURITY`（Ch72）。
- **Target and Adjacent Chapters Read:** Ch22～24、Ch80～82、Ch71～73 已定位。
- **Existing Coverage:** Books已有artifact-producing workflow与representation identity；本family提供3D executable artifact受限案例。
- **Integration Decision:** `Books Pending — Evidence Complete`。
- **Changed Files or Rejection Reason:** 仅本 Weekly。
- **Open Questions:** 如何对generated Blender code做capability sandbox、deterministic replay、API migration与semantic-part correctness验证？

### Dissecting Tool-Integrated Reasoning

- **Candidate / Week / Score:** Dissecting Tool-Integrated Reasoning / 2025-W34 / 25/30。
- **Source Family ID:** `ARXIV-2508.15754`。
- **Source Type:** full empirical paper、ReasonZoo benchmark与cost-aware metrics。
- **Event Date / First-public Date / Revision History:** arXiv v1 2025-08-21；owner固定W34，DBLP/DOI metadata回链同一family。
- **Direct Primary Sources:** arXiv:2508.15754 PDF/abstract与ReasonZoo evaluation definitions。
- **Related Primary Sources:** evaluated Qwen3、DeepSeek-R1、ToRL/CIR model papers/cards和Python tool runtime contract。
- **Access and Verification Status:** Verified；PDF、metadata与benchmark definitions可访问；无独立reproduction。
- **Full-read Coverage:** motivation/related work、九类ReasonZoo任务、PoT/MT-TIR/TIT设置、PAC/m-PAC/AUC-PCC公式、model comparisons、token-budget curves、tool attribution、regression cases、appendix与limitations已读。
- **Original Problem:** tool reasoning常只报最终accuracy，无法回答收益是否跨域、是否只是更长trace，以及tool何时把原本正确答案变错。
- **Why the Previous Design Was Reasonable:** exact-answer benchmark简单、易比较；数学Python工具的正确率提升可直接观察，早期无需统一cost curve。
- **Changed Constraint:** 多种tool integration strategy、模型规模和token budget并存，需要把performance与reasoning cost放在同一evaluation contract。
- **Mechanism:** ReasonZoo覆盖九类数学/非数学reasoning；PAC衡量达到performance threshold所需token cost，AUC-PCC聚合budget-performance frontier，并做tool-related correction/regression attribution。
- **State Ownership:** task/evaluator拥有answer truth；tool runtime拥有execution truth；agent拥有call/trace；meter拥有token cost；metric aggregator拥有threshold/frontier解释。
- **Control Flow / Data Flow:** task → CoT或PoT/MT-TIR/TIT → tool execution/observation → answer → accuracy + token-cost trace → PAC/AUC-PCC与归因。
- **Implementation Details:** 比较Qwen3多规模、DeepSeek-R1及tool-trained models；Python interpreter是主要工具，token proxy不等于wall-clock/GPU/monetary cost。
- **Evaluation Contract:** 九类ReasonZoo accuracy、PAC/m-PAC、AUC-PCC与不同token budgets；结论绑定作者prompts、tool sandbox、sampling和evaluator。
- **Baselines / Ablations / Sensitivity / Overhead:** no-tool CoT对比PoT/MT-TIR/TIT，并按模型规模、任务类别和budget分析；缺真实API latency、tool failures、concurrency与安全副作用。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** model names与最高约32K token budget披露；hardware、precision、batch/concurrency、tool latency/SLO Not Disclosed。
- **What the Evidence Proves / Does Not Prove:** 证明在作者benchmark中tool可同时改善部分accuracy/cost frontier且也会造成correct-to-wrong regression；不证明tool普遍增强“内在推理”或token少等同系统成本低。
- **Limitations / Threats to Validity:** Python工具偏置、benchmark与prompt sensitivity、model function-call competence差异、token-only cost proxy、tool side effect缺失。
- **Trade-offs / New Failure Modes:** deterministic computation可减少算术/搜索错误，却新增错误代码、tool observation污染、call overhead和原本正确trace被干扰。
- **Where the Previous Design Still Applies:** 工具无收益、低延迟或answer可由短CoT稳定得到时no-tool path仍合理；高风险tool必须先有permission/verifier。
- **Evolution Relationship:** `Direct Evolution`：accuracy-only tool benchmark → task/category attribution → performance-cost frontier；与MCP execution benchmark为互补层。
- **ROADMAP Node:** `AGENT-TOOL`（Ch78），handoff `PLATFORM-EVALUATION-SYSTEM`（Ch66）与`INFER-SCHEDULING`（Ch56）。
- **Target and Adjacent Chapters Read:** Ch77～79、Ch65～67、Ch55～56 已定位。
- **Existing Coverage:** Books已有模型能力/工具机会/系统成本分离；本family补充cost-aware metric但不把PAC当production cost。
- **Integration Decision:** `Books Pending — Evidence Complete`。
- **Changed Files or Rejection Reason:** 仅本 Weekly。
- **Open Questions:** 如何把wall-clock、GPU、tool价格、failure retry和side-effect risk合并到可校准的tool-value frontier？

### TPLA

- **Candidate / Week / Score:** TPLA / 2025-W34 / 28/30。
- **Source Family ID:** `ARXIV-2508.15881`。
- **Source Type:** full systems paper、TransMLA implementation artifact、checkpoint-conversion与H800 inference experiments。
- **Event Date / First-public Date / Revision History:** v1 2025-08-21；v2 2025-08-25，仅为同一 family revision；owner固定W34，不能按W35 surface date重计。
- **Direct Primary Sources:** arXiv:2508.15881 v1/v2 HTML/PDF、`fxmeng/TransMLA` repository。
- **Related Primary Sources:** DeepSeek MLA、GLA、FlashAttention-3、tensor parallelism与prefill/decode disaggregation primary sources。
- **Access and Verification Status:** Verified；v1全文、公式、实验、ablation、limitations与artifact identity可访问。
- **Full-read Coverage:** metadata/revision、MLA/GLA/matrix absorption、RMSNorm/softmax slicing、Hadamard/PCA reparameterization、TPLA/GLA等价关系、PD separation、commonsense/LongBench、throughput/TTFT、ablation与limitations已读。
- **Original Problem:** MLA把KV压成单一latent，但tensor parallel decode时每张GPU仍复制完整latent，随TP degree增加会丢失相对GQA的per-device cache优势。
- **Why the Previous Design Was Reasonable:** 单设备或低TP下MLA压缩显著且完整head可访问全latent；复制latent避免跨shard近似误差，prefill也能用矩阵吸收高效计算。
- **Changed Constraint:** 32K长上下文和multi-GPU decode变成memory-bandwidth bound，需要每卡只读本地latent shard，同时不从头重训MLA checkpoint。
- **Mechanism:** 同时切分latent和每个attention head的input dimension，各卡独立做local RMSNorm/softmax attention后AllReduce output；用Hadamard平衡norm slicing、PCA缓解softmax slicing，并在prefill保留MLA、decode切TPLA。
- **State Ownership:** checkpoint/projection weights拥有可吸收变换；每卡拥有local latent shard；TP collective拥有full-head output合并；prefill/decode router拥有phase-specific graph选择。
- **Control Flow / Data Flow:** prompt在MLA prefill生成compressed latent → KV按TP shard分发/驻留 → decode query与projection同维切分 → local attention → AllReduce output → next token。
- **Implementation Details:** drop-in加载DeepSeek-V3与Kimi-K2 MLA checkpoints；FlashAttention-3兼容；作者在两张H800上比较MLA/GLA/TPLA与separated prefill，并实现Hadamard/PCA weight reparameterization。
- **Evaluation Contract:** commonsense与LongBench验证conversion质量；32K context下作者报告DeepSeek-V3/Kimi-K2 decode speedup 1.79×/1.93×，TTFT与throughput绑定两张H800、其batch/context/configuration。
- **Baselines / Ablations / Sensitivity / Overhead:** 比较MLA、GLA、TPLA，逐项切RMSNorm/softmax并消融Hadamard/PCA、PD separation与group partition；AllReduce成本和g>2稳定性是显式边界。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 2×H800、DeepSeek-V3-0324（移除MoE）与Kimi-K2-Base、最高32K context披露；precision、完整batch/concurrency、network topology与production SLO不完整。
- **What the Evidence Proves / Does Not Prove:** 证明MLA checkpoint可在作者H800/TP=2合同下转换为sharded latent decode并保留大部分benchmark质量；不证明任意TP degree/network都获益，也不证明training-free conversion无精度损失。
- **Limitations / Threats to Validity:** PCA把信息集中到前维，g>2可能失效；Hadamard不能同时保证softmax乘积平衡；模型移除MoE、只测两卡且v2后发细节会影响外推。
- **Trade-offs / New Failure Modes:** 降低per-device KV bandwidth并复用checkpoint，却新增local normalization/softmax approximation、collective latency、phase graph切换、weight transform与conversion rollback复杂度。
- **Where the Previous Design Still Applies:** 单GPU、短context、TP低或interconnect差时原MLA更简单；可重新训练且愿牺牲每head容量时GLA可能减少转换近似。
- **Evolution Relationship:** `Direct Evolution`：MLA compressed cache → replicated latent under TP → sharded latent/head dimensions + AllReduce；PD separation是layering而非TPLA本体。
- **ROADMAP Node:** `INFER-KV-CACHE`（Ch45），handoff `INFER-PD-DISAGGREGATION`（Ch55）、`INFER-EXECUTION`/`INFER-TENSORRT-LLM`（Ch49）。
- **Target and Adjacent Chapters Read:** Ch44～46、Ch48～50、Ch54～56 已定位；Books Gate关闭。
- **Existing Coverage:** Books已有KV identity、TP collective与PD phase边界；本family补充“模型表示压缩必须与device sharding共同设计”的机制证据。
- **Integration Decision:** `Books Pending — Evidence Complete`。
- **Changed Files or Rejection Reason:** 仅本 Weekly；从错误W35归属回拨W34，不触发Books/年度索引。
- **Open Questions:** TP>2、MoE保留、跨节点collective、mixed precision与真实continuous-batching下，conversion error和latency frontier如何变化？

### AgentFly / Memento

- **Candidate / Week / Score:** AgentFly / Memento / 2025-W34 / 27/30。
- **Source Family ID:** `ARXIV-2508.16153`。
- **Source Type:** full agent/memory paper、AgentFly repository、deep-research benchmark experiments。
- **Event Date / First-public Date / Revision History:** v1 2025-08-22，标题 *AgentFly: Fine-tuning LLM Agents without Fine-tuning LLMs*；v2 2025-08-25改名 *Memento: Fine-tuning LLM Agents without Fine-tuning LLMs*；同一family owner在W34。
- **Direct Primary Sources:** arXiv:2508.16153 v1/v2 HTML/PDF、`Agent-on-the-Fly/AgentFly` repository。
- **Related Primary Sources:** GAIA、DeepResearcher、HLE、SimpleQA benchmark definitions，以及作者所用GPT-4.1/o4-mini model/API contracts。
- **Access and Verification Status:** Verified；event-time v1、current metadata、method、implementation、evaluation、ablation与artifact均可访问。
- **Full-read Coverage:** M-MDP formalization、parametric/non-parametric memory read/write、planner/executor implementation、case bank、training/online update algorithms、GAIA/DeepResearcher/HLE/SimpleQA、continual/OOD/token-cost ablations、appendix与failure discussion已读。
- **Original Problem:** 固定prompt/reflection workflow部署后不能从新经验适应，而对底层LLM做持续gradient fine-tuning昂贵、慢且需要模型权重权限。
- **Why the Previous Design Was Reasonable:** 静态workflow容易审计和回滚；离线fine-tuning能把行为压入参数，在分布稳定且数据充足时推理路径更短。
- **Changed Constraint:** deep-research agent持续遇到新网站、工具与任务，希望仅用环境反馈在线改进planner，同时复用不可训练的closed/API LLM。
- **Mechanism:** 将agent建模为memory-augmented MDP；Case Bank保存成功/失败episodic tuples，non-parametric分支按embedding Top-K读取并append写入，parametric分支学习Q-function选择高utility cases并更新memory policy。
- **State Ownership:** base LLM只拥有语言policy且冻结；Case Bank拥有episodic history/provenance；retriever/Q-function拥有selection policy；environment/evaluator拥有reward；planner/executor拥有当前trajectory。
- **Control Flow / Data Flow:** task/state → 从Case Bank读取相似cases → planner生成计划 → tool executor与environment交互 → evaluator reward → 写入新case/更新Q-function → 后续task复用。
- **Implementation Details:** deep-research实现交替case-based planning和tool execution；作者比较offline/online executor及parametric/non-parametric CBR，planner/executor示例使用GPT-4.1与o4-mini；底层LLM不更新但Q-function可有gradient。
- **Evaluation Contract:** GAIA validation/test、DeepResearcher七数据集、HLE与SimpleQA；论文报告GAIA Pass@3、F1/PM、五轮continual curves与OOD gains，均绑定作者scaffold、live tools、judge和API版本。
- **Baselines / Ablations / Sensitivity / Overhead:** 对比CoT、RAG、无CBR、offline/online executor及其他deep-research agents；消融memory size、K、parametric/non-parametric、continual iteration、OOD与token cost；小而curated memory优于无限增长。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** planner/executor model names和部分token cost披露；provider hardware、precision、context truncation、batch/concurrency、tool latency与SLO Not Disclosed。
- **What the Evidence Proves / Does Not Prove:** 证明外部episodic memory read/write可在作者deep-research合同下改善冻结LLM agent，并显示live tools有时也会伤害开放域结果；不证明agent真正在线学习通用策略，也不证明memory不会累积错误。
- **Limitations / Threats to Validity:** benchmark/judge与API漂移、case leakage、semantic similarity假设、奖励噪声、不断增长memory、failed-case污染和标题revision造成身份混淆。
- **Trade-offs / New Failure Modes:** 避免LLM fine-tuning并获得快速适应，却把policy state外移到memory/retriever，引入provenance、supersession、delete、poisoning、staleness与retrieval latency。
- **Where the Previous Design Still Applies:** 高合规、流程稳定、必须deterministic replay时静态workflow更合适；有权重权限和稳定大样本时fine-tuning可减少在线memory依赖。
- **Evolution Relationship:** `Direct Evolution`：保存trajectory → 检索相似case → 基于reward改写/选择memory policy；不是对base LLM权重的fine-tuning。
- **ROADMAP Node:** `AGENT-MEMORY`（Ch77），handoff `AGENT-WORKFLOW`（Ch81）、`PLATFORM-EVALUATION-SYSTEM`（Ch66）。
- **Target and Adjacent Chapters Read:** Ch76～78、Ch80～82、Ch65～67 已定位；Books Gate关闭。
- **Existing Coverage:** Books已有derived memory与workflow state ownership；本family补充M-MDP read/write和在线case-selection证据，必须保留“frozen LLM ≠ no gradient anywhere”边界。
- **Integration Decision:** `Books Pending — Evidence Complete`。
- **Changed Files or Rejection Reason:** 仅本 Weekly；event-time标题保留，current title作为revision alias，不在W35重计。
- **Open Questions:** case provenance、reward disagreement、poisoning检测、supersession/delete与Q-function rollback如何进入production memory contract？

## Low-score Source and Rejection Closure

### aiXiv — 18/30

- **Source Family / Identity:** `ARXIV-2508.15126`，*aiXiv: A Next-Generation Open Access Ecosystem for Scientific Discovery Generated by AI Scientists*。
- **Date / Revision:** v1 2025-08-20；v2 2025-12-17，同一 family。
- **Score Verification:** 3 + 3 + 3 + 4 + 3 + 2 = 18/30。
- **Primary Source Read:** arXiv abstract、architecture/evaluation sections与公开 platform description；身份和日期已唯一定位。
- **Rejection Reason:** multi-agent proposal/review/revision platform具有工程启发，但质量提升主要由作者自评、judge与平台内循环证明，缺独立长期 scientific validity、fraud/adversarial review 与 provenance rollback证据；不升级为通用 AI-science governance结论。
- **Disposition:** `Weekly Only — Low-score Closure`；无 pending 材料请求。

### LLaSO — 18/30

- **Source Family / Identity:** `ARXIV-2508.15418`，*LLaSO: A Foundational Framework for Reproducible Research in Large Language and Speech Model*。
- **Date / Revision:** v1 2025-08-21；本周 owner 已核对。
- **Score Verification:** 3 + 3 + 4 + 4 + 2 + 2 = 18/30。
- **Primary Source Read:** paper metadata、12M alignment/13.5M instruction datasets、3.8B reference model、LLaSO-Eval与公开 artifact scope。
- **Rejection Reason:** 全栈开放对 speech-language reproducibility有价值，但当前 Books 没有独立 speech owner，且 normalized 0.72/“surpasses comparable models”受作者 normalization 与 workload约束；不能据此改变通用 multimodal/training design。
- **Disposition:** `Weekly Only — Low-score Closure`；artifact可在未来 speech owner形成时回审。

### Fin-PRM — 19/30

- **Source Family / Identity:** `ARXIV-2508.15202`，*Fin-PRM: A Domain-Specialized Process Reward Model for Financial Reasoning in Large Language Models*。
- **Date / Revision:** v1 2025-08-21；v2 2026-05-04，同一 family。
- **Score Verification:** 3 + 3 + 3 + 4 + 3 + 3 = 19/30。
- **Primary Source Read:** trajectory-aware PRM、3K trajectories、Monte Carlo/LLM judge/financial knowledge multi-source labels、SFT selection/Best-of-N/RL三场景与 CFLUE/FinQA evaluation。
- **Rejection Reason:** step+trajectory reward是已知 process-reward branch的金融域实例；3K自建轨迹、LLM judge与领域 verifier耦合，尚不足以形成跨域 reward owner更新。
- **Disposition:** `Weekly Only — Low-score Closure`；若未来出现独立金融 verifier reproducibility再升级。

## Cross-Week Deduplication and Spillback

- `DINOv3`、`SSRL`、`Thyme`、`BeyondWeb`、`XQuant`、`Ovis2.5`、`ComoRAG`、`MM-BrowseComp` 与 `Mind the Generation Process` 的 arXiv v1 位于 2025-08-13～16；即使 Hugging Face 在 08-18～20 surface，也归 W33，不在 W34 重计。
- `Chain-of-Agents` 的首次公开为 2025-08-06，归更早 week。
- `TPLA`（arXiv:2508.15881）v1 为 2025-08-21、v2 为 2025-08-25；`AgentFly`（arXiv:2508.16153）v1 为 2025-08-22，v2 于 2025-08-25 改名 `Memento`。两项均归 W34并已完成评分与 Full Source Review；08-25 revision/surfacing不创建 W35 owner。
- Nemotron Nano 2 v2 在本周、v3/v4在后续周，但都回链 `ARXIV-2508.14444`；Intern-S1 v1/v2均在本周，只计一次。
- DeepSeek-V3.1-Terminus 是 W39 corrective revision，保留独立事件角色但 source packet回链 `DEEPSEEK-V3.1-2025`。

## Evidence Level

- **Official / Version Fact:** DeepSeek-V3.1只证明公开 API、artifact与 mode contract；内部机制为 `Mechanism Not Disclosed`。
- **Primary Research / Experimental:** 26篇 retained论文均完成正文与关键 appendix覆盖；性能数字只在作者 model、data、harness、evaluator下成立。
- **Implementation Artifact:** code/model/benchmark可提升复核强度，但不等同 independent reproduction。
- **Project Inference:** 跨 source family 的演进关系是本项目归纳，不伪装成论文结论。

## Knowledge Tree Position

- MCPGauge / MCP-Universe / LiveMCP-101 → `AGENT-MCP` + `PLATFORM-EVALUATION-SYSTEM`。
- ToolACE-MT / Atom-Searcher / Mobile-Agent-v3 → `TRAIN-DATA`或`TRAIN-GRPO` → `AGENT-WORKFLOW`。
- Rubric Anchors / DuPO → `TRAIN-RLHF`、`TRAIN-GRPO`、`TRAIN-DPO` → evaluation handoff。
- Matrix-Game 2.0 / Embodied-R1 / RynnEC → `MULTIMODAL-WORLD-MODELS`、`MULTIMODAL-EMBODIED-VLA`、`MULTIMODAL-REPRESENTATION`。
- 4DNeX / Next Visual Granularity / S²-Guidance / Precise Action-to-Video / MeshCoder → `MULTIMODAL-REPRESENTATION`、`MULTIMODAL-GENERATIVE-PARADIGMS`、World Model / Embodied handoff。
- Nemotron Nano 2 / Quantization Meets dLLMs / Intern-S1 / FLARE → Model、Training 与 Inference execution owners，禁止写成产品清单。
- Dissecting Tool-Integrated Reasoning → `AGENT-TOOL` + `PLATFORM-EVALUATION-SYSTEM` + scheduling cost handoff。
- TPLA → `INFER-KV-CACHE`，handoff `INFER-PD-DISAGGREGATION`与execution owner；AgentFly/Memento → `AGENT-MEMORY`，handoff `AGENT-WORKFLOW`与evaluation owner。
- DeepConf → `MODEL-SAMPLING` → `INFER-SCHEDULING` → `PLATFORM-EVALUATION-SYSTEM`。
- POML → `AGENT-PROMPT`，artifact identity handoff到 Platform；DeepSeek-V3.1保持 Weekly-only version fact。

## Recommended Action

- 保留 27 个已完成 Source Review 的 source family，等待 2025 年 Historical Evidence Gate 总体通过后再逐 family执行 Books Integration。
- 不以低分项制造 Books diff；aiXiv、LLaSO、Fin-PRM保留可回溯 rejection closure。
- 后续年度 reconciliation应把 W33/W35 spillback写回各自 owner week，而不是在 W34重复评分。

## Event-Date Daily Decision

Historical Backfill 不创建 Daily；所有高分事件、真实日期、revision与 evidence boundary直接保留在本 Weekly。

## Books Integration Decision

`Historical Books Gate Closed`。本周只完成 Weekly Evidence Gate；除 DeepSeek-V3.1明确为 `Weekly Only` 外，26个 retained research family均为 `Books Pending — Evidence Complete`。本次不修改 Books、ROADMAP、年度索引或 Learning State。

## Independent Review Checkpoint

- **Denominator reconciliation:** 评分表共30个唯一 Source Family；19个高分（25～30）、8个中分（20～24）、3个低分，总计30。27个 retained family与3个低分 rejection closure逐项对应，没有未计分 gap。
- **Review completeness:** 27/27 retained family均有非模板化 Full Source Review；3/3低分 family均记录 primary source、first-public date、六维评分、Total与非模板拒绝理由。`Review Pending = 0`。
- **Date and revision review:** TPLA（2508.15881）v1 2025-08-21、AgentFly（2508.16153）v1 2025-08-22均由W34拥有；2025-08-25的v2与AgentFly→Memento标题变更仅为W35 revision/surfacing，不建立第二个owner或重复评分。
- **Deduplication review:** 30个 Source Family ID与primary identifier均唯一；W33 spillback、W35 revision-only surfacing及后续revision correction均已在Cross-Week ledger显式路由。
- **Fact-boundary review:** TPLA的吞吐/TTFT数字保留作者两张H800、指定模型与序列设置，不外推为通用收益；AgentFly/Memento明确区分冻结base LLM与可由gradient更新的Q-function，未把memory policy adaptation写成LLM weight fine-tuning。
- **Structure review:** Candidate Scoring、27个Full Source Review、3个Low-score Closure、Books disposition、Sources与Gate账目一致；标题层级、Markdown结构与来源日期已独立复核。
- **Checkpoint status:** `Independent Review Passed — Weekly Evidence Gate may reclose`。

## Weekly Gate Audit

| Check | Result |
| --- | --- |
| ISO coverage | Pass — 2025-08-18～2025-08-24，Monday～Sunday |
| Scored families | Pass — 30 rows / 30 unique Source Families |
| High score | Pass — 19 rows at 25～30 |
| Medium score | Pass — 8 rows at 20～24 |
| Low score | Pass — 3 rows below 20 with source/date/score/rejection closure |
| Full Source Review | Pass — 27/27 retained rows |
| Review Pending | 0 |
| Unverified / Blocked | 0 |
| Disputed | 0 |
| Revision ownership | Pass — v1 owner dates and later revisions separated |
| Cross-week duplicate | Pass — W33 spillback、W35 revision-only surfacing与后续 corrections均已枚举 |
| Independent Reconciliation | Pass — TPLA与AgentFly/Memento均按v1回拨W34；30-row denominator、30个唯一family与W35 revision-only路由一致 |
| Candidate Evidence Gate | **Passed** |
| Discovery Replay | **Closed** |
| Historical Books Gate | **Closed by annual policy** |

## Ignored Noise

- 忽略转载、HF surfacing date伪装成 v1 date、旧论文重发、无 primary evidence leaderboard与缺 workload contract的 benchmark marketing。
- survey、单一 prompt trick、仅有 abstract/announcement而无机制与 artifact的条目不进入评分表；它们不是 `Review Pending`。
- 固定 AI Infra scan 中不属于本周 owner date 的 release不重复归档。

## Repository Changes

- 重建 `papers/2025/weekly/2025-W34/README.md`：由1个候选恢复为30个评分 family；独立 recall复核先补回7个遗漏，再由W35 revision反查回拨TPLA与AgentFly/Memento，最终补齐27个 Full Source Review、3个低分闭合、spillback与 Gate账目。
- 未修改年度索引、Learning State、Books、ROADMAP；未 stage、commit或push。

## Open Questions

- MCP live benchmark如何同时获得 temporal validity、可重放性与 side-effect安全？
- rubric/process/dual reward如何记录 verifier provenance、disagreement与 reward-hacking证据？
- confidence-aware test-time routing如何在开放任务上接入 external evidence calibration？
- action-conditioned world state、KV/cache identity与 physical controller rollback如何统一？
- 2025年度 Evidence Gate通过前，26个 Books Pending family均不得提前宣称已集成。

## Sources

- MCPGauge / Help or Hurdle — https://arxiv.org/abs/2508.12566（v1: 2025-08-18；Accessed: 2026-08-24）
- ToolACE-MT — https://arxiv.org/abs/2508.12685（v1: 2025-08-18；Accessed: 2026-08-24）
- Reinforcement Learning with Rubric Anchors — https://arxiv.org/abs/2508.12790（v1: 2025-08-18；Accessed: 2026-08-24）
- HeroBench — https://arxiv.org/abs/2508.12782（v1: 2025-08-18；Accessed: 2026-08-24）
- Atom-Searcher — https://arxiv.org/abs/2508.12800（v1: 2025-08-18；Accessed: 2026-08-24）
- Matrix-Game 2.0 — https://arxiv.org/abs/2508.13009（v1: 2025-08-18；Accessed: 2026-08-24）
- POML — https://arxiv.org/abs/2508.13948（v1: 2025-08-19；Accessed: 2026-08-24）
- Embodied-R1 — https://arxiv.org/abs/2508.13998（v1: 2025-08-19；Accessed: 2026-08-24）
- RynnEC — https://arxiv.org/abs/2508.14160（v1: 2025-08-19；Accessed: 2026-08-24）
- DuPO — https://arxiv.org/abs/2508.14460（v1: 2025-08-20；Accessed: 2026-08-24）
- NVIDIA Nemotron Nano 2 — https://arxiv.org/abs/2508.14444（v1: 2025-08-20；Accessed: 2026-08-24）
- MCP-Universe — https://arxiv.org/abs/2508.14704（v1: 2025-08-20；Accessed: 2026-08-24）
- Quantization Meets dLLMs — https://arxiv.org/abs/2508.14896（v1: 2025-08-20；Accessed: 2026-08-24）
- aiXiv — https://arxiv.org/abs/2508.15126（v1: 2025-08-20；Accessed: 2026-08-24）
- Mobile-Agent-v3 — https://arxiv.org/abs/2508.15144（v1: 2025-08-21；Accessed: 2026-08-24）
- Fin-PRM — https://arxiv.org/abs/2508.15202（v1: 2025-08-21；Accessed: 2026-08-24）
- Deep Think with Confidence — https://arxiv.org/abs/2508.15260（v1: 2025-08-21；Accessed: 2026-08-24）
- LLaSO — https://arxiv.org/abs/2508.15418（v1: 2025-08-21；Accessed: 2026-08-24）
- LiveMCP-101 — https://arxiv.org/abs/2508.15760（v1: 2025-08-21；Accessed: 2026-08-24）
- Intern-S1 — https://arxiv.org/abs/2508.15763（v1: 2025-08-21、v2: 2025-08-24；Accessed: 2026-08-24）
- DeepSeek-V3.1 — https://api-docs.deepseek.com/updates（First Public: 2025-08-21；Accessed: 2026-08-24）
- 4DNeX — https://arxiv.org/abs/2508.13154（v1: 2025-08-18；Accessed: 2026-08-24）
- Next Visual Granularity Generation — https://arxiv.org/abs/2508.12811（v1: 2025-08-18；v2: 2026-02-28；Accessed: 2026-08-24）
- S²-Guidance — https://arxiv.org/abs/2508.12880（v1: 2025-08-18；v4: 2026-03-04；Accessed: 2026-08-24）
- Precise Action-to-Video — https://arxiv.org/abs/2508.13104（v1: 2025-08-18；Accessed: 2026-08-24）
- FLARE — https://arxiv.org/abs/2508.12594（v1: 2025-08-18；v3: 2026-01-30；Accessed: 2026-08-24）
- MeshCoder — https://arxiv.org/abs/2508.14879（v1: 2025-08-20；v2: 2025-08-22；Accessed: 2026-08-24）
- Dissecting Tool-Integrated Reasoning — https://arxiv.org/abs/2508.15754（v1: 2025-08-21；Accessed: 2026-08-24）
- TPLA — https://arxiv.org/abs/2508.15881（v1: 2025-08-21；v2: 2025-08-25；Accessed: 2026-08-24）
- AgentFly / Memento — https://arxiv.org/abs/2508.16153（v1: 2025-08-22；v2 title revision: 2025-08-25；Accessed: 2026-08-24）
