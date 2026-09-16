# 2026-05-05 V3 Books 写回记录

本文件是 `books-writeback-queue.json` 的可读投影。root 已完成本轮 6 项写回；marker 与相邻交接已经作者侧回读，但仍需新的非作者 reviewer 做写后语义复核。

| Source Family | Owner / 目标 | 状态 | 精确插入位置 |
| --- | --- | --- | --- |
| `SF-2026-ARXIV-2605-01302` | `AGENT-RAG` / `books/part-07-agent/76-rag.md` | `applied_post_write_review_pending` | `Relevance 不等于 Sufficient Context` 内，relevance/sufficiency/faithfulness 三分之后、sufficiency evaluator 之前 |
| `SF-2026-ARXIV-2605-01345` | `MULTIMODAL-REPRESENTATION` / `books/part-03-multimodal-world-models/23-multimodal-representation.md` | `applied_post_write_review_pending` | `固定预算要先分配信息责任，再选择具体 Token` 内，层级预算与一次性 selector 之后 |
| `SF-2026-ARXIV-2605-01772` | `MULTIMODAL-EMBODIED-VLA` / `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md` | `applied_post_write_review_pending` | `Full-horizon Multimodal Trace 是 Versioned Proposal` 之后、Action representation 之前 |
| `SF-2026-ARXIV-2605-02178` | `TRAIN-GRPO` / `books/part-04-training-system/33-grpo.md` | `applied_post_write_review_pending` | `Mid-rollout 提前停止只能取消低边际信息轨迹` 之后、Group-relative Gradient 之前 |
| `SF-2026-ARXIV-2605-02263` | `MULTIMODAL-GENERATIVE-PARADIGMS` / `books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md` | `applied_post_write_review_pending` | Block Diffusion 主线内，固定 block size 的成立条件之后、Draft/verify 分支之前 |
| `SF-2026-ARXIV-2605-02411` | `AGENT-TOOL-CALLING` / `books/part-07-agent/78-tool-calling.md` | `applied_post_write_review_pending` | `Tool Discovery 与选择` 内，catalog shortlist/schema exposure 之后、utility admission 之前 |
| `SF-DP-RUNTIME-MONITORING` | `PLATFORM-MONITORING` / `books/part-06-ai-infrastructure/67-monitoring.md` | `applied_post_write_audited` | 本章要回答的问题 / 先定义目标，再选择可测信号 / Context generator 是 pre-failure sensor identity 的一部分 / Review notes / 四层指标 |
| `SF-EDGE-CONTINUOUS-INFERENCE-RISK-BUDGET` | `INFER-SCHEDULING` / `books/part-05-inference-system/56-inference-scheduling.md` | `applied_post_write_audited` | SLO-aware Admission / 当前能放下，不等于未来可完成 |
| `SF-FEDQUEUE-CROSS-FACILITY-QUEUE-AWARE-TRAINING` | `TRAIN-DISTRIBUTED-TRAINING` / `books/part-04-training-system/36-distributed-training.md` | `applied_post_write_audited` | 本章要回答的问题 / 单卡为什么会失败 / 从本机协作到分布式执行 / 先分清五个通信层次 / Collective 是群体语义，不是一种算法 |
| `SF-GRADIENT-GATED-DPO` | `TRAIN-DPO` / `books/part-04-training-system/34-dpo.md` | `applied_post_write_audited` | 本章要回答的问题 / 从 RLHF 的两阶段复杂度开始 / KL-constrained 最优策略 / 从 Reward Difference 到 Policy Difference / 一个 pair loss 小例子 |
| `SF-RESPONSE-PATH-TAMPERING-PROVIDER-SIGNATURE` | `PLATFORM-SECURITY` / `books/part-06-ai-infrastructure/72-security.md` | `applied_post_write_audited` | 本章要回答的问题 / 从资产与信任边界开始 / 生命周期威胁 / 隐私检测是 Policy-bound Sensor，不是安全判决 / 从独立 Span 到关系感知的本地 Sanitization |
| `SF-VDCORES-ASYNC-GPU-RESOURCE-DECOUPLING` | `INFER-TENSORRT-LLM` / `books/part-05-inference-system/49-tensorrt-llm.md` | `applied_post_write_audited` | 本章要回答的问题 / 从计算图开始 / 三类基础优化 / Execution Plan 可以修订，但只能在安全边界 Commit / 从粗粒度 Offload 到负载观测的 Tensor Placement |

## 本轮 6 项完整语义增量

### `SF-2026-ARXIV-2605-01302`

在 relevance 与 sufficiency 之间增加 query-robustness gate：旧 top-k 在 query 前提可信时仍合理；当前提可能错误或带确认偏误时，retriever 应把候选在 counterfactual query perturbation 下能否维持决策支持作为独立信号。Critic 只提出 evidence-risk proposal，原始 source 与 answer gate 仍拥有事实和提交权。该分支以额外扰动数据、critic 校准和更多 abstention 换取对迎合性检索的抵抗；critic 漂移、偏误模板覆盖不足或高风险结论时回退多源原文核验/人工。exact-v1 只证明作者 decision benchmarks 和扰动合同中的结果，不提供跨 corpus 固定阈值。

**证据边界：** 来源支持 relevance 在带偏 query 下可能系统性选择迎合性证据，并支持 counterfactual robustness 作为独立检索信号；不证明 critic score 是事实概率或可替代原始证据核验。 偏误类型、counterfactual 构造、正确答案和 critic 共享同一实验合同；结果没有证明新 corpus、领域、语言或真实恶意用户上的校准，固定阈值也不是生产常数。

**写回校验：** semantic-body marker = 1；Daily trace marker = 1；非作者写后语义复核待执行。

### `SF-2026-ARXIV-2605-01345`

把固定视觉输入扩展为 bounded active-observation 分支：全局低分辨率视图先保留 context，acquisition policy 依据当前未决 claim 选择下一 crop，evidence assembler 记录坐标、尺度、采集顺序与 budget，answer gate 决定继续、提交或拒答。旧的一次性均匀采样在低分辨率已足够或 latency 严格时仍更稳；主动采集用细节可见性换额外调用、路径依赖、漏区与尾延迟。Selector 只拥有 observation proposal，不拥有 evidence sufficiency；exact-v1 结果限作者 VLM、crop proxy 和高分辨率 benchmark。

**证据边界：** 证据支持在固定视觉 token 预算下把 observation acquisition 作为可审计的顺序控制问题；不证明 crop proposal 是充分证据，也不覆盖开放世界视觉安全。 论文明确讨论 ideal-observer 假设、backbone hallucination、连续空间近似和随机 latency；adaptive invocation 仍属未来工作，未证明 crop policy 能识别所有关键证据或满足实时 SLO。

**写回校验：** semantic-body marker = 1；Daily trace marker = 1；非作者写后语义复核待执行。

### `SF-2026-ARXIV-2605-01772`

在 immutable full-horizon trace 与逐步 reactive policy 之间增加 adaptive subgoal stack：每个 subgoal 绑定 observation revision、parent、完成条件和 validity horizon；高层 planner 只能 push/refine/backtrack proposal，低层 policy 用 fresh observation 执行，controller 验证完成后才 pop。它以局部修订降低整条计划报废成本，却新增 progress detector 误判、递归不终止、stack stale 和高低层语义漂移；动态环境或检测不可信时回退短 horizon reactive planning/全量重规划。exact-v1 只支持作者模拟与有限真实任务，不构成开放世界 safety proof。

**证据边界：** 来源支持将长程计划从固定 trace 演进为可修订 subgoal stack；不证明 anticipation 输出是环境事实，低层 controller 和 fresh observation 仍拥有执行与纠错边界。 subgoal 是否完成、何时细化和回退由学习式判断控制；论文没有证明开放世界中的 progress calibration、无限递归终止、异常恢复或安全关键物理提交。

**写回校验：** semantic-body marker = 1；Daily trace marker = 1；非作者写后语义复核待执行。

### `SF-2026-ARXIV-2605-02178`

把低边际信息检测扩展成两层 exploration controller：token 层只能提出 bounded thinking intervention，turn 层只能提出 resample/cancel；group builder 保存触发分数、阈值、policy/environment revision 与最终 membership，optimizer 不把缺失 suffix 或重采样重复当独立证据。它用减少空转换取 estimator drift、selection bias、额外 token 和 on-policy staleness；uncertainty 不等于错误，late-reward 或校准不足时回退完整 rollout/静态采样。exact-v1 只支持 WebShop、ALFWorld、Search QA 与作者配置。

**证据边界：** 来源支持把 exploration progress 作为 rollout control signal；不证明 uncertainty 是 outcome verifier，也不允许 intervention/resampling 的数据在缺少 policy/version identity 时混入更新。 论文讨论 pipeline/off-policy staleness 与固定设置；uncertainty 不等于错误，低变化也可能表示已经收敛或需要长期延迟收益，错误干预会改写 on-policy 分布。

**写回校验：** semantic-body marker = 1；Daily trace marker = 1；非作者写后语义复核待执行。

### `SF-2026-ARXIV-2605-02263`

在 fixed block 旁增加 learned-boundary 分支：decoder 输出可验证的 block-end proposal，runtime 冻结 boundary/policy revision 后提交；训练可用 entropy trajectory 提供辅助 shaping，但任务 outcome/独立 verifier 仍拥有正确性。动态边界以语义步骤适配换 variable-length scheduling、cache/rollback 复杂度、reward hacking 和错误自信；短输出、静态 shape kernel 或 entropy 未校准时继续使用固定 block。exact-v1 的 reasoning benchmark 只支持该代理信号和后训练机制在作者设置中的结果。

**证据边界：** 来源支持把 block boundary 从固定超参数演进为 policy-owned generation state；不证明 entropy trajectory 是 correctness verifier，也不保证动态 block 在所有 workload 更快。 边际 entropy 下降并不等于推理正确或语义步骤结束，错误但自信的 block 也可能满足 reward；论文未证明不同 dLLM、开放生成或部署并发下的阈值和收益。

**写回校验：** semantic-body marker = 1；Daily trace marker = 1；非作者写后语义复核待执行。

### `SF-2026-ARXIV-2605-02411`

把静态 shortlist 扩展为 bounded revisable discovery state：每次 probe 保存 query/intention revision、返回 tool identities、尝试结果、预算与 parent；parallel branches 只拥有 proposal，retrieval controller 去重/合并 frontier，executor 仍逐项验证 schema、version、authorization 与 effect dependency。它用恢复早期漏检换额外模型调用、探索噪声、过期 tool memory 与 tail latency；catalog 小、接口稳定或风险高时回退静态 allowlist/typed schema。exact-v1 结果只覆盖 StableToolBench、所测模型和预算，不能作为开放生态的安全或性能保证。

**证据边界：** 来源支持 action-space discovery 在执行中成为可修订状态；不支持由 retrieval score 授权工具，也不证明返回 schema 或 effect 正确。 论文指出弱 base model 会让 memetic search 放大噪声；伪描述可能漂离真实 intent，tool memory 会过期，StableToolBench pass 也不证明动态版本、权限和副作用安全。

**写回校验：** semantic-body marker = 1；Daily trace marker = 1；非作者写后语义复核待执行。

## 2026-09-15 最小假阴性修复：root 待写回

以下四项已完成作者侧 exact-v1、评分和逐命题 Books 比较；尚未写入共享 Books，必须由 root 按日期序列写回后再交给新的非作者 reviewer。

### `TRAIN-GRPO` — `2605.01208v1`

**插入位置：** books/part-04-training-system/33-grpo.md — `DAPO 把朴素 GRPO 的运行失败拆成四处修补` 中 Dynamic Sampling 之后、`DAPO 之后，各分支继续修改不同约束` 之前

**现有命题差异：** 现有命题只覆盖“换 group membership”这条路径；未覆盖在无法或不宜补采时，通过固定 reward 边界改变 estimator 统计、保留 collapsed group 并接受有偏同号更新的替代分支。

**可写回语义增量：** 在 Dynamic Sampling 之后增加并列分支：当 reward 有稳定边界且重采样昂贵时，可仅向归一化统计加入固定 anchors，使全错/全对组的真实样本获得同号更新；variance tempering 再限制不同离散度 group 的尺度。该机制改变 estimator 语义而不产生组内排序，收益是保留稀疏 reward group，代价是边界依赖、bias、超参敏感与共同错误放大。reward 稠密、边界不可信或补采便宜时，继续使用普通 GRPO/Dynamic Sampling。

**证据边界：** exact-v1 支持 Qwen3-VL-8B 的作者 GUI/RFT 设置，不证明 anchor-normalized advantage 对其他 reward 范围、模型、环境或 production SLO 普遍有效；它也不证明同 reward rollout 之间存在可识别排序。

**相邻交接：** Ch33 拥有 advantage estimator；GUI grounding、abstention 与动作证据仍由 Agent/Embodied 章节承载。

### `PLATFORM-SECURITY` — `2605.01913v1`

**插入位置：** books/part-06-ai-infrastructure/72-security.md — `模型内部路由、训练数据与 Weight Repair 都进入攻击面` 中 fine-tuning safety regression 段落之后

**现有命题差异：** 现有命题覆盖样本风险与事后 weight repair，却未说明 downstream update 即使保持 task utility，也可能沿 safety-mediating subspace 漂移，以及如何在训练时限制该投影。

**可写回语义增量：** 在训练安全回归中增加 representation-geometry 分支：把 base-aligned refusal subspace 作为版本化 reference sensor，训练 owner 记录 update 在该 subspace 上的投影并可施加惩罚；它只能限制已识别方向，不能签发安全结论。收益是提前暴露/抑制下游适配导致的安全漂移，代价是白盒访问、layer/reference 选择、utility 约束和错误保留。geometry 不稳定、模型不可见或任务必须使用重叠方向时，回退冻结/adapter 隔离、较小 update 与完整行为安全回归。

**证据边界：** exact-v1 支持所列开源模型、benchmark 与受控 fine-tuning stress；不证明 refusal geometry 是普适因果机制，也不取代行为 red-team、adaptive attack、utility regression 或独立 release gate。

**相邻交接：** Ch72 拥有安全传感器和 release gate；训练章节只说明 update artifact/optimizer identity，不复制安全机理。

### `TRAIN-LORA` — `2605.01959v1`

**插入位置：** books/part-04-training-system/30-lora.md — `Rank 与 target modules 决定更新空间` 之后、`Rank Threshold` 分支之前

**现有命题差异：** 现有命题没有覆盖 sample-conditioned rank router，也未把训练—推理 rank policy、difficulty-label provenance 和动态 shape serving 成本纳入 adapter identity。

**可写回语义增量：** 在静态 rank 之后增加条件容量分支：router 只能从版本化 input feature 提出允许 rank，训练与推理必须复用同一 policy；adapter identity 同时绑定 router、difficulty-label rule、rank set、alpha 与 target modules。它用按样本分配容量换来 router 误判、标签循环、dynamic-shape/batching 碎片与更大发布矩阵。任务同质、kernel 需要静态 shape、latency 未证或 router 不稳定时，固定 rank 仍是首选 fallback。

**证据边界：** exact-v1 只支持作者 QA/数学/语音任务与小规模 Llama/Whisper；trainable-parameter 减少不等于 FLOPs、latency 或 fleet cost 改善，也不证明 rank policy 跨任务可迁移。

**相邻交接：** Ch30 拥有 adapter capacity identity；serving 的 batching/shape 成本只向 Inference 章节短交接。

### `MULTIMODAL-REPRESENTATION` — `2605.02323v1`

**插入位置：** books/part-03-multimodal-world-models/23-multimodal-representation.md — `Fusion：在哪里让模态相遇` 之后、`固定预算要先分配信息责任，再选择具体 Token` 之前

**现有命题差异：** 现有命题仍把多 slot attention 看作一次或彼此独立的预算分配；没有表示“哪些输入成分已被前一 slot 解释”的可变状态，因此未覆盖 additive superposition 下重复选择同一成分的 failure mode。

**可写回语义增量：** 增加 residual-evidence 分支：当多个并行 slot 会在 additive mixture 上重复解释同一成分时，为每个 token 保存尚未解释的容量；slot 输出后才提交 bounded depletion，下一 slot 读取新 revision。收益是非冗余分解，代价是顺序化、ordering sensitivity、乘性误差和 task-dependent depletion。component 可分、冗余可接受或时延优先时，普通 parallel/cross attention 仍更合适；该 state 只表示 representation allocation，不是外部事实证据。

**证据边界：** exact-v1 仅支持 synthetic、FUSS audio 与 LISA workload；不证明该机制适用于通用 LLM attention，也不允许把 learned evidence depletion 当作 factual provenance 或 correctness signal。

**相邻交接：** Ch23 拥有 representation allocation state；通用 attention 数学仍在 Ch14，不能把该受限案例写成 Transformer attention 的普遍结论。

