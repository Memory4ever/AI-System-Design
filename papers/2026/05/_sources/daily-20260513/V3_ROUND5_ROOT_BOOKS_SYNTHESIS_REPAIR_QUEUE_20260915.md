# 2026-05-13 Round 5 Root Books Synthesis / Repair Queue

**状态：** 作者队列完成；共享 Books 尚待 root 串行落地

本队列只覆盖独立终审核定的 Round 5 项。每项均以旧基线、约束变化、状态/控制权、代价/失败、fallback 与 exact-v1 边界构成，不得改写成论文摘要拼贴。

## `AGENT-MEMORY`

### `2605.12039` — Procedural Memory 的压缩单位应是可展开的 Contract Graph

- 旧基线：现有静态/单一责任路径在新增约束不存在时仍是合理基线。
- 约束变化：isolated skill entries 只按语义相似度检索，无法表达前置关系，也无法治理 merge/split/delete；SkillGraph 把 procedural memory 变成 typed evolving graph。
- 机制 / 状态 / 控制权：skill graph 拥有候选依赖，trajectory evidence 提出 mutation；memory controller 管理版本/合并，workflow 仍拥有执行顺序与 commit。
- Trade-off / failure：组合性换来图漂移、循环依赖、错误合并和检索成本；RL feedback 还会把当前 policy 偏差固化进 memory。
- Fallback / 共存：图证据不足时回退孤立 versioned skills、人工依赖、只读 graph snapshot 和执行时 constraint validation。
- Exact-v1 boundary：只支持所测环境与 evaluator；不证明技能关系是真因果、跨 agent 可移植或在线图更新一致。
- 正文位置：`books/part-07-agent/77-memory.md` → “Procedural Memory 的压缩单位应是可展开的 Contract Graph”

### `2605.12294` — Procedural Memory 的压缩单位应是可展开的 Contract Graph

- 旧基线：现有静态/单一责任路径在新增约束不存在时仍是合理基线。
- 约束变化：GUI agent 每屏重新解释并自由生成动作，会在长任务中反复支付 token 和决策误差；EAM 将复用 routine 编译为可搜索 Knowledge Graph。
- 机制 / 状态 / 控制权：KG 保存可执行 routine/transition，Q 只排序 path proposal；GUI observer 和 workflow runtime 仍验证当前 state 并提交 action。
- Trade-off / failure：减少重复推理但增加图陈旧、状态 alias、MCTS/Q 成本与错误 routine 复用。
- Fallback / 共存：屏幕不匹配或 path value 不可靠时回退逐步 observation/planning，要求 state precondition、动作确认和可撤销 checkpoint。
- Exact-v1 boundary：只支持 AndroidWorld 与作者训练/评估合同；不证明真实桌面安全、跨应用迁移或所报 latency 的通用性。
- 正文位置：`books/part-07-agent/77-memory.md` → “Procedural Memory 的压缩单位应是可展开的 Contract Graph”

## `AGENT-MULTI-AGENT`

### `2605.11376` — Coordination State 必须有显式 Owner 与 Commit Transition

- 旧基线：小规模直接 agent messaging 在参与者和权限固定时足够，但人口扩大后 directory、身份、协商与承诺会混成一个状态。
- 约束变化：population-scale personal-agent exchange 需要把 directory/routing、user identity、negotiation state 与 agreement commit 分权；结构化 message 不自动获得代表用户承诺的 authority。
- 机制 / 状态 / 控制权：exchange 负责 directory/routing 与 protocol state，agent 只提出 offer，用户或授权 policy 保留 agreement commit authority。
- Trade-off / failure：增加目录一致性、身份验证、消息排序和协商成本；代理偏好错误会产生越权承诺。
- Fallback / 共存：规模、身份或协议证据不足时回退小组 coordinator、显式用户 approval 与确定性 negotiation policy。
- Exact-v1 boundary：结构化 message 和 agreement proposal 不获得代表用户承诺的 authority；结论只限受测 population/protocol/agent/model/evaluator，规模或身份不满足时回退小组 coordinator、显式 approval 与确定性 policy。
- 正文位置：`books/part-07-agent/82-multi-agent.md` → “Coordination State 必须有显式 Owner 与 Commit Transition”

## `AGENT-PLANNING`

### `2605.11706` — 从目标到状态图

- 旧基线：现有静态/单一责任路径在新增约束不存在时仍是合理基线。
- 约束变化：把 tool graph 作为检索/序列化 prompt 只能做语义 matching，早期选错后会进入非法 graph state；GRAFT 将节点与有向依赖编码进模型表示。
- 机制 / 状态 / 控制权：graph token 表示计划约束，on-policy samples 暴露自身漂移；模型只提出 plan，workflow/runtime 仍验证依赖与执行 commit。
- Trade-off / failure：减少 prompt graph 搬运却增加 tokenizer/model coupling、graph versioning 与 retraining；错误内化会更难被观察。
- Fallback / 共存：动态图或置信不足时回退外部 typed DAG、constraint checker、stepwise replan 与执行前 legality gate。
- Exact-v1 boundary：只支持所测静态 tool graph 与 legality/equality 指标；不证明真实工具成功、权限安全或动态图一致性。
- 正文位置：`books/part-07-agent/79-planning.md` → “从目标到状态图”

## `AGENT-PLATFORM`

### `2605.12087` — Agent Runtime State Machine

- 旧基线：把 intermediate output 当临时文件在短 workflow 中可行，但无法支持恢复、复算和多消费者。
- 约束变化：intermediate artifact 必须是 typed、versioned、addressable、dependency-aware 的 durable state，并明确 authoritative producer 与 downstream consumers。
- 机制 / 状态 / 控制权：typed/versioned/addressable artifact 保存 producer、dependency 与 lineage；authority 字段决定谁能 materialize/replace，数据模型本身不证明 runtime consistency。
- Trade-off / failure：持久化会增加存储、索引、schema migration、一致性与权限冲突成本。
- Fallback / 共存：authority 冲突时停止物化并回退 append-only event/log state，加人工 reconciliation。
- Exact-v1 boundary：正文必须标明 proposal/validated artifact 的差别；采用该模型会增加存储、索引、一致性与迁移成本，authority 冲突时停止 materialization，回退 append-only event/log state 与人工 reconciliation。
- 正文位置：`books/part-07-agent/84-agent-platform.md` → “Agent Runtime State Machine”

## `AGENT-WORKFLOW`

### `2605.12481` — Logical Plan 与 Physical Schedule 必须分别验收

- 旧基线：现有静态/单一责任路径在新增约束不存在时仍是合理基线。
- 约束变化：GUI 原子动作与高层 tool call 共存时，agent 不知道何时切换，且缺少 interleaved trajectories；ToolCUA 将 path choice 作为独立训练对象。
- 机制 / 状态 / 控制权：policy 提议 GUI/tool action path，tool schema 和 current UI state 约束可执行性；workflow runtime 保留权限、side effect 与 commit authority。
- Trade-off / failure：高层 tool 可缩短路径，但合成轨迹偏差、工具过用、环境漂移和 reward shortcut 会放大不可逆操作风险。
- Fallback / 共存：tool/GUI state 不一致时回退原子 GUI、重新 observation、显式 approval 与 dry-run；保留最大步数和 compensation。
- Exact-v1 boundary：只支持 OSWorld-MCP/Windows transfer 与所选模型；不证明真实桌面权限安全、所有工具可用或跨 OS 一般收益。
- 正文位置：`books/part-07-agent/81-workflow.md` → “Logical Plan 与 Physical Schedule 必须分别验收”

## `INFER-TENSORRT-LLM`

### `2605.11581` — 从逐 Kernel Launch 到 Persistent Executor

- 旧基线：现有正文只覆盖相邻机制，不能承载原 No Change 所声称的语义。
- 约束变化：固定 deployment configuration 允许把 MegaKernel DAG 的 dynamic scheduling 从 runtime branch 上提到 compile-time search，同时以 shared-memory constraint/K-splitting适配 Ada GPU。
- 机制 / 状态 / 控制权：固定部署配置把 DAG execution-path 决策从 runtime scheduler 上提给 compile-time search；runtime 只执行已验收计划。
- Trade-off / failure：消除 branch/launch 开销但增加离线搜索、shared-memory constraint、architecture coupling；配置漂移会让固化路径失效。
- Fallback / 共存：动态 shape/config 或搜索不可信时回退普通 kernel graph/runtime scheduling。
- Exact-v1 boundary：证据只支持 exact-v1 披露的 workload、model、hardware、precision、length、batch、concurrency、SLO 与 evaluator；未披露字段为 Not Disclosed。它不证明跨部署的一般优势，也不把作者 benchmark 变成生产承诺。
- 正文位置：`books/part-05-inference-system/49-tensorrt-llm.md` → “从逐 Kernel Launch 到 Persistent Executor”

### `2605.12327` — Block Scale 也是可搜索的执行状态

- 旧基线：现有静态/单一责任路径在新增约束不存在时仍是合理基线。
- 约束变化：microscaled FP4 每组固定一张 grid 会浪费分布适配空间；多 grid 将每组格式选择编码进 scale metadata。
- 机制 / 状态 / 控制权：quantizer 为每组选择 grid，artifact 必须保存 grid/scale identity；runtime/kernel 负责忠实解码，质量 gate 保留发布权。
- Trade-off / failure：更低误差换额外 metadata、搜索、format/backend coupling；选择错误或 kernel 不支持时理论收益不转化为速度。
- Fallback / 共存：回退单一 NVFP4/MXFP4 grid、较高精度或静态 max-scale，并分别验收模型质量和端到端 latency。
- Exact-v1 boundary：只支持披露模型、group size、格式与任务；不证明所有硬件可加速、多 grid 总优于单 grid或训练收益可直接迁移 PTQ。
- 正文位置：`books/part-05-inference-system/49-tensorrt-llm.md` → “Block Scale 也是可搜索的执行状态”

## `MODEL-FFN`

### `2605.12426` — MLP 是不是“知识库”

- 旧基线：现有静态/单一责任路径在新增约束不存在时仍是合理基线。
- 约束变化：把 MLP 权重直接视为事实 key-value memory 会导出事实数线性参数需求；几何表征允许 embedding 叠加关系，而小 MLP 只做 relation-conditioned selector。
- 机制 / 状态 / 控制权：embedding 保存关系 superposition，MLP 保存通用选择规则；这与‘MLP 单独拥有事实真值’不同。
- Trade-off / failure：参数效率来自共享几何，但会引入 embedding interference、margin/维度要求和 multi-hop depth 成本。
- Fallback / 共存：结构不满足共享 attribute geometry 时仍可使用显式 retrieval、更多参数/层或传统 associative representation。
- Exact-v1 boundary：证明和经验只限 controlled setting；不能外推真实 LLM 的知识定位、可解释性、编辑安全或全部 factual recall。
- 正文位置：`books/part-02-model/16-feed-forward-mlp.md` → “MLP 是不是“知识库””

## `MODEL-SELF-ATTENTION`

### `2605.12171` — Self Attention 获得了什么

- 旧基线：现有静态/单一责任路径在新增约束不存在时仍是合理基线。
- 约束变化：‘一层 attention 足以全局交互’不等于它能以固定 heads 和简单 post-process 表达全局 parity；复杂度必须同时计 heads 与后处理函数度数。
- 机制 / 状态 / 控制权：attention heads 提供交互通道，post-process 提供非线性选择；任何一侧容量不足都不能由‘全局可见’自动补偿。
- Trade-off / failure：增加 heads/degree 可以绕开下界，但增加参数、计算与优化难度；理论 capacity 也不保证可训练。
- Fallback / 共存：需要 parity-like interaction 时使用更多层、显式 recurrence/algorithmic state 或更强后处理；普通局部任务保留单层基线。
- Exact-v1 boundary：证明的是一层模型的必要增长率，不是 Transformer 普遍失败、真实 LLM 能力上限或具体硬件成本。
- 正文位置：`books/part-02-model/14-self-attention.md` → “Self Attention 获得了什么”

## `MODEL-TRANSFORMER-LAYER`

### `2605.12466` — Recurrence 可以只占据 Decoder 的局部层段

- 旧基线：现有静态/单一责任路径在新增约束不存在时仍是合理基线。
- 约束变化：固定-depth looped Transformer 训练不稳且部署成本固定；Attractor Model 将反复 refinement 改为 fixed-point solver，并用 implicit differentiation 避免训练 memory 随 effective depth 增长。
- 机制 / 状态 / 控制权：backbone 拥有 initial proposal，solver 拥有 refinement state，convergence rule 拥有停止 proposal；输出 commit 仍需数值/任务 gate。
- Trade-off / failure：adaptive depth/constant-memory backward 换来 fixed-point 求解、收敛失败和 implicit gradient 数值风险；内部化可能失效。
- Fallback / 共存：未收敛时限制迭代、回退固定-depth Transformer/loop，保留 residual stability 与 per-sample convergence telemetry。
- Exact-v1 boundary：只支持作者规模、任务与容差；不证明任意深度免费、所有输入收敛、推理 solver 可总是删除或通用硬件收益。
- 正文位置：`books/part-02-model/17-transformer-layer.md` → “Recurrence 可以只占据 Decoder 的局部层段”

## `MULTIMODAL-GENERATIVE-PARADIGMS`

### `2605.11494` — Few-step Distillation 要在 Student 实际访问的状态上验收

- 旧基线：现有静态/单一责任路径在新增约束不存在时仍是合理基线。
- 约束变化：单步/少步 diffusion 失去多步 trajectory 中可注入随机性的接口；PCA 定向 feature perturbation 把 diversity control 移入 student 的内部表示几何。
- 机制 / 状态 / 控制权：activation geometry 拥有可扰动方向，generation model 仍拥有输出；扰动器只改变 proposal diversity，不拥有 fidelity 真值。
- Trade-off / failure：增加 PCA 校准、存储与层选择成本；feature distribution 漂移或过强扰动会破坏 alignment。
- Fallback / 共存：几何失配时关闭 perturbation，回退原 student、multi-step sampler 或外部 best-of-N，并用独立质量 gate 验收。
- Exact-v1 boundary：只证明作者模型/数据/指标下的 diversity–fidelity Pareto；不证明一般 diffusion manifold、端到端 latency 或用户偏好。
- 正文位置：`books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md` → “Few-step Distillation 要在 Student 实际访问的状态上验收”

### `2605.11722` — 从一次生成到 Plan → Generate → Validate → Retry

- 旧基线：现有静态/单一责任路径在新增约束不存在时仍是合理基线。
- 约束变化：一次生成无法可靠满足多对象、计数、属性与关系；EPIC 将 prompt 固化为 typed visual program，并以 predicate failure 路由 edit 或 resample。
- 机制 / 状态 / 控制权：visual program 拥有待满足 contract，verifier 只产出 predicate evidence，controller 选择下一 action，最终 acceptance 仍需独立 gate。
- Trade-off / failure：可定位局部失败但增加 parse/verifier/编辑成本；错误 program 会稳定地优化错误目标，循环还可能耗尽预算。
- Fallback / 共存：verifier 不确定时回退 single-pass 或 best-of-N，保留原 prompt、人工检查和最大 retry/cost budget。
- Exact-v1 boundary：只证明披露模型、predicate 集和 benchmark 的 alignment/cost；不证明开放世界视觉事实、任意 prompt 可分解或 verifier 正确。
- 正文位置：`books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md` → “从一次生成到 Plan → Generate → Validate → Retry”

## `PLATFORM-EVALUATION-SYSTEM`

### `2605.11195` — 评估对象有四个层次

- 旧基线：用单一 fairness score 汇总 DP model 在固定评估面上的行为，适合窄任务但会隐藏层级差异。
- 约束变化：DP 对 logit-level 与 output-level social bias 的影响不一致，说明 privacy claim 与 fairness claim 必须按行为层级分开验收。
- 机制 / 状态 / 控制权：DP training 产生一个版本化 model；sentence/logit、completion、classification 与 QA evaluator 分别拥有各自行为证据，privacy accountant 不拥有 fairness 真值。
- Trade-off / failure：增加四类 gate、解析与切片成本；unparseable output 和 metric disagreement 会让聚合结论失真。
- Fallback / 共存：各层证据冲突时保留独立 privacy/fairness gates，限制发布范围并要求跨模型重测。
- Exact-v1 boundary：把 privacy 与 fairness 保留为独立 gate：ε=2 只说明该 VaultGemma setting，四类 surface 的 bias 变化不能合并为单一结论；跨模型/部署需重测。
- 正文位置：`books/part-06-ai-infrastructure/66-evaluation-system.md` → “评估对象有四个层次”

### `2605.11202` — Runtime and Service Evaluation

- 旧基线：单请求 API/模型测试能发现显式错误，但把 serving engine 当稳定 substrate。
- 约束变化：timed multi-request trace 应成为 inference-engine fuzzing workload artifact；crash/hang/performance 之外还要以 controlled replay 与 log-prob oracle 捕获 silent corruption。
- 机制 / 状态 / 控制权：timed trace 拥有并发 workload identity，灰盒 signals 指导 mutation，controlled replay/log-prob oracle 只确认可重现的 engine failure。
- Trade-off / failure：fuzzing 消耗执行预算并受 nondeterminism、oracle drift、telemetry 可见性与 replay cost 限制。
- Fallback / 共存：oracle 不稳时回退 deterministic regression trace、engine invariant check 与 maintainer confirmation。
- Exact-v1 boundary：trace/oracle 只证明可重放的所测 serving-layer failure；nondeterminism、oracle drift 或 replay cost 超预算时，退回 deterministic regression traces、engine invariant checks 与人工/maintainer confirmation。
- 正文位置：`books/part-06-ai-infrastructure/66-evaluation-system.md` → “Runtime and Service Evaluation”

### `2605.11209` — Agent Regression Testing 需要分配 Evidence Budget

- 旧基线：uniform sampling 对普通错误率简单无偏，但在 five-nines rare failure 下成本过高。
- 约束变化：CEM 学习的 failure-prone sampling distribution 是 rare-failure evidence allocator，不是真实 failure rate owner；必须保留 unbiased audit、importance accounting 与 fallback。
- 机制 / 状态 / 控制权：CEM proposal Q 只分配高风险样本预算；importance weights 将观测还原到目标分布 P，confidence interval 才拥有 failure-rate statement。
- Trade-off / failure：proposal support 不足、重尾 importance weight 或 ESS 过低会扩大方差乃至产生错误置信。
- Fallback / 共存：保留 uniform/stratified audit floor；importance accounting 失败时停止发布稀有错误率。
- Exact-v1 boundary：Q 只分配 evidence budget，不拥有真实 failure rate；importance accounting 失效、support 缺失或 ESS 过低时回退 uniform/stratified audit，并单独报告 proposal 与目标分布。
- 正文位置：`books/part-06-ai-infrastructure/66-evaluation-system.md` → “Agent Regression Testing 需要分配 Evidence Budget”

### `2605.12120` — 评估对象有四个层次

- 旧基线：现有静态/单一责任路径在新增约束不存在时仍是合理基线。
- 约束变化：模型在 advisory prompt 中维护专业规范，不代表在实际 drafting/action framing 中仍遵从；principal hierarchy 必须作为 domain × task framing × stakeholder 的行为合同测量。
- 机制 / 状态 / 控制权：scenario contract 拥有冲突角色与规范，model output 只是行为证据；release gate 必须按 framing/domain/model slice 保留层级结果。
- Trade-off / failure：更贴近部署冲突，却增加专业规范定义、专家标注和时变模型成本；平均聚合会掩盖局部 authority inversion。
- Fallback / 共存：证据不足时回退明确 policy hierarchy、工具/权限 gate、人工复核和 domain-specific abstention，不让模型自报意图替代行为测试。
- Exact-v1 boundary：只支持所测法律/医疗场景和模型；不证明真实事故率、内部动机、全部职业规范或未来模型稳定性。
- 正文位置：`books/part-06-ai-infrastructure/66-evaluation-system.md` → “评估对象有四个层次”

### `2605.12131` — 第一个不变量：评估声明必须绑定完整对象

- 旧基线：只发布 headline score 在一次性比较中便宜，但丢失 rollout、失败和 reporting rule 后无法重算。
- 约束变化：Agent evaluation 的 publication bundle 应同时保存 rollout record、声明的 views/reporting rules 与 dropped-runs manifest，使报告分数可追溯到同一证据对象。
- 机制 / 状态 / 控制权：rollout record 保存 episode evidence，view/rule registry 负责派生分数，drops manifest 暴露被排除项；bundle 只拥有可追溯性，不拥有结果正确性。
- Trade-off / failure：完整 rollout 带来隐私、体量、许可和维护成本；缺失或错误 rule 仍可生成可复算的错误结论。
- Fallback / 共存：采用最小可审计 view、hash/受控访问与 drops manifest；rollout 缺失时降级为不可复现声明。
- Exact-v1 boundary：隐私/体量限制时发布最小可审计 view、drops manifest 与 hash/受控访问；rollout 缺失时降级为不可复现声明，不能让 headline score 通过 release gate。
- 正文位置：`books/part-06-ai-infrastructure/66-evaluation-system.md` → “第一个不变量：评估声明必须绑定完整对象”

## `PLATFORM-MONITORING`

### `2605.12265` — 小 Monitor 需要专门训练其检测边界

- 旧基线：现有正文只覆盖相邻机制，不能承载原 No Change 所声称的语义。
- 约束变化：多任务单 token classifier SFT 对相邻 domain、thinking classification 和 summarization 有部分 transfer，但完全换 prompt/同 domain 时会误用训练规则；general instruction stage 可缓解。
- 机制 / 状态 / 控制权：training mixture/stage 拥有 monitor representation 的更新分布；monitor 仅产生风险 evidence，policy/release gate 保留裁决权。
- Trade-off / failure：相邻域 transfer 换 task-rule leakage、prompt shift 和 loss dilution；训练可能让 edge case 更差。
- Fallback / 共存：domain/prompt shift 未验收时回退 prompted/specialized monitor、保留 general instruction data 与独立 holdout。
- Exact-v1 boundary：证据只支持 exact-v1 披露的 workload、model、hardware、precision、length、batch、concurrency、SLO 与 evaluator；未披露字段为 Not Disclosed。它不证明跨部署的一般优势，也不把作者 benchmark 变成生产承诺。
- 正文位置：`books/part-06-ai-infrastructure/67-monitoring.md` → “小 Monitor 需要专门训练其检测边界”

## `PLATFORM-SECURITY`

### `2605.12122` — Unlearning 必须分开参数擦除与推理拒答

- 旧基线：现有静态/单一责任路径在新增约束不存在时仍是合理基线。
- 约束变化：普通 sparse reconstruction SAE 让多个概念共享 feature，压制目标概念时会连带损伤非目标内容；concept-aware clustering 把删除边界移到表示 support。
- 机制 / 状态 / 控制权：cluster assignment 只提出被抑制 feature support；unlearning controller 与行为/evidence gate 仍拥有删除 commit 与验收权。
- Trade-off / failure：更精准抑制换来 cluster leakage、概念重叠、表示漂移和新训练成本；错误分离仍会产生 collateral damage。
- Fallback / 共存：分离证据不强时回退模型版本隔离、prompt/output guardrail、重新训练或更宽行为评估，并保留原 artifact。
- Exact-v1 boundary：只证明作者 benchmark 中的行为抑制/保真指标；不证明知识已从权重移除、跨 prompt 不可恢复或合规删除完成。
- 正文位置：`books/part-06-ai-infrastructure/72-security.md` → “Unlearning 必须分开参数擦除与推理拒答”

## `TRAIN-GRPO`

### `2605.12380` — Asynchronous RL 必须把 Policy Staleness 写进 Advantage

- 旧基线：现有静态/单一责任路径在新增约束不存在时仍是合理基线。
- 约束变化：固定 clipping/off-policy 超参把 trust-region 与 behavior mismatch 预先混在一起，task、scale 或 rollout execution 改变就需重调；batch ratio distribution 可作为当前 mismatch state。
- 机制 / 状态 / 控制权：behavior/current-policy ratio 拥有 staleness evidence，ESS controller 分配 update trust；objective 不把 rollout engine 差异藏进固定超参。
- Trade-off / failure：减少手调但可能被小 batch、重尾 ratio 或数值误差误导；保留非零高-ratio signal 也会增加 variance。
- Fallback / 共存：ESS 不稳时回退固定 clip/KL、fresh on-policy rollout、丢弃超龄样本和 trainer–rollout numerical identity audit。
- Exact-v1 boundary：只支持所测 policy、task 和 batch regime；不证明免调参、异步任意陈旧仍稳定或所有 mismatch 都可由 ratio 识别。
- 正文位置：`books/part-04-training-system/33-grpo.md` → “Asynchronous RL 必须把 Policy Staleness 写进 Advantage”

## `TRAIN-LORA`

### `2605.11872` — Rank 与 target modules 决定更新空间

- 旧基线：现有静态/单一责任路径在新增约束不存在时仍是合理基线。
- 约束变化：orthogonal PEFT 往往把 adaptation support 与 support 内 transformation 混在同一参数化；LOFT 将两者分开并让 downstream gradient 选择 support。
- 机制 / 状态 / 控制权：support selector 决定可更新子空间，orthogonal transform 只在其内改变方向；任务 loss/held-out gate 仍拥有选择真值。
- Trade-off / failure：task-aware support 提高预算利用率，却增加梯度估计、子空间更新与 optimizer coupling，错误 support 会冻结所需方向。
- Fallback / 共存：信号弱或任务多变时回退固定 principal/coordinate support、普通 LoRA 或 full tuning，并按行为而非矩阵距离验收。
- Exact-v1 boundary：只支持 matched-budget 的受测任务；不证明 orthogonality 自动防遗忘、跨模型最优 support 或部署成本优势。
- 正文位置：`books/part-04-training-system/30-lora.md` → “Rank 与 target modules 决定更新空间”

## `TRAIN-PRETRAINING`

### `2605.11570` — 训练稳定性是多层系统问题

- 旧基线：现有静态/单一责任路径在新增约束不存在时仍是合理基线。
- 约束变化：loss/accuracy 只能从训练外部看到结果，无法及早定位层内结构是否进入坏区间；OUI 把 activation pattern 作为 label-free early observable。
- 机制 / 状态 / 控制权：activation statistic 是早期 sensor，只能提出 schedule/regularization 调整；optimizer controller 与 held-out evidence 保留 commit authority。
- Trade-off / failure：可提早预警，但增加逐层统计和校准；activation 稳定可能是假稳态，sensor 还可能被 architecture change 破坏。
- Fallback / 共存：OUI 未校准时继续以 loss、gradient、held-out 与 checkpoint recovery 联合判断，先 shadow 观察再允许控制器动作。
- Exact-v1 boundary：支持‘activation 可作为补充训练状态’的假设，不支持单一 OUI 阈值、普适 early stopping 或自动调参最优性。
- 正文位置：`books/part-04-training-system/28-pretraining.md` → “训练稳定性是多层系统问题”

### `2605.12492` — Optimizer Update 要尊重参数块的对称性

- 旧基线：现有静态/单一责任路径在新增约束不存在时仍是合理基线。
- 约束变化：Adam/Muon 的 additive update 会同时改变方向与 singular spectrum；Pion 用左右 orthogonal transformations 将谱固定，只优化权重几何。
- 机制 / 状态 / 控制权：optimizer 拥有坐标/变换 proposal，正交参数化保证谱不变；training objective/held-out evidence 决定这种 invariant 是否仍合适。
- Trade-off / failure：稳定谱换来矩阵变换开销，并可能禁止任务所需的 spectrum adaptation；数值近似会破坏严格正交。
- Fallback / 共存：固定谱成为瓶颈或成本过高时回退 AdamW/Muon/混合 optimizer，并按参数角色、梯度谱和 loss trajectory 选择。
- Exact-v1 boundary：只支持作者规模、数据和实现；不证明固定谱普适最优、超大模型效率或等价于更好泛化。
- 正文位置：`books/part-04-training-system/28-pretraining.md` → “Optimizer Update 要尊重参数块的对称性”

## `TRAIN-RLHF`

### `2605.11387` — Reverse KL 会把“找到高奖励”收缩成单一路径

- 旧基线：现有静态/单一责任路径在新增约束不存在时仍是合理基线。
- 约束变化：RL 微调生成式 policy 时，成功率优化会压缩原有多模态行为；轨迹级 mode discovery 与互信息奖励改变了 diversity state 的训练责任。
- 机制 / 状态 / 控制权：mode inference 只提供 diversity proposal，任务 reward 仍拥有 success 方向；MI regularizer 在同一 policy update 中保护已发现行为支路。
- Trade-off / failure：保留多样性会与单一 reward optimum 竞争；mode inference 漂移、mode alias 与过度分裂会把奖励写错轨迹。
- Fallback / 共存：mode 证据不稳或单一路径已满足部署目标时，回退常规 RL fine-tuning、显式 entropy/KL 约束及独立行为覆盖评估。
- Exact-v1 boundary：只支持披露机器人任务、policy、数据量与 evaluator；不证明真实机器人安全、任意 mode 完备性或跨 embodiment 收益。
- 正文位置：`books/part-04-training-system/31-rlhf.md` → “Reverse KL 会把“找到高奖励”收缩成单一路径”

### `2605.12480` — 从二元偏好到分布条件化的连续 Reward

- 旧基线：现有静态/单一责任路径在新增约束不存在时仍是合理基线。
- 约束变化：joint audio-video diffusion 的单一 global advantage 会混合不一致目标、跨 modality gradient 与稀疏同步区域；OmniNFT 将 credit 按 modality/layer/region 分配。
- 机制 / 状态 / 控制权：各 reward channel 只为对应 modality branch 提供 credit；cross-modal layers 保留共享梯度，region weight 负责 decision-density，而非一个标量拥有全部目标。
- Trade-off / failure：分权可减少 gradient interference，却增加 reward calibration、branch routing 和 gradient surgery complexity；错误归因会牺牲另一模态。
- Fallback / 共存：指标冲突或路由不稳时回退 global reward + conservative KL、冻结受影响分支，或分阶段单模态训练后联合验收。
- Exact-v1 boundary：只支持 LTX-2 与所选 benchmark/evaluator；不证明跨模型通用、真实同步质量、无 reward hacking 或训练稳定性。
- 正文位置：`books/part-04-training-system/31-rlhf.md` → “从二元偏好到分布条件化的连续 Reward”

