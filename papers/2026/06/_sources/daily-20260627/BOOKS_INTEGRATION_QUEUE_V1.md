# 2026-06-27 Books Integration Queue V1

Denominator DEN-20260627-aef6bb58. CLOSED: root wrote 14 Integrate families into 11 owners; 47 No Change and 3 Weekly Only remained unwritten; the 64/64 post-write fresh audit passed.

## AGENT-PLANNING

- Target: books/part-07-agent/79-planning.md
- Exact anchor: ## 完成证据与 Verification
- Families: SF-2026-ARXIV-2606-27806
- Owner-merged minimal delta: 语言 planner 可以保留语义 proposal authority，同时由小型 parametric transition model 检查 imagined state delta 是否满足动力学。两者分歧时应开启 targeted revision，而不是静默替换 planner 或提交 action；transition model 只做 bounded verifier，environment/controller 继续拥有最终 authority。
- Coexistence/fallback boundary: Learned transition verifier 可能与 planner 共享盲点，也不是 physics oracle；分歧或 OOD state 回退 environment validation 或人工复核。

## INFER-REQUEST-LIFECYCLE

- Target: books/part-05-inference-system/42-what-happens-during-inference.md
- Exact anchor: ## 请求状态机
- Families: SF-2026-ARXIV-2606-27906, SF-2026-ARXIV-2606-28529, SF-2026-ARXIV-2606-28565
- Owner-merged minimal delta: Inference capacity 是 phase-coupled closed loop，不是单个 kernel 数字。request record 必须区分 vision encoding、prefill、decode、queue/host work 与 device placement；kernel-level simulation 可以预测候选配置，但 promotion 必须回到目标硬件上的 task completion time 与 success。改变 control cadence 或移动瓶颈的局部加速，不自动等于更快完成成功任务。
- Coexistence/fallback boundary: Simulation 与 component latency 不证明生产 SLO 或 embodied success；mismatch、thermal drift 或 deadline miss 时回退已实测的保守 placement/control。

## MULTIMODAL-EMBODIED-VLA

- Target: books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md
- Exact anchor: ## Safety envelope
- Families: SF-2026-ARXIV-2606-28276
- Owner-merged minimal delta: Scene-generation pipeline 应把 video reconstruction、editable scene variant、policy training 与 real-world validation 保存为由 provenance 连接的独立 artifact。visual fidelity 只能决定 scene 能否进入 simulation，不拥有 sim-to-real validity；synthetic scene family 影响物理 promotion 前，policy ranking 必须与 matched real outcome 对读。
- Coexistence/fallback boundary: Reconstruction quality 与 simulator ranking 不证明 contact dynamics 或 safety；rank mismatch 或未知 embodiment 会阻断物理 promotion，并保留 real-data/controller gate。

## MULTIMODAL-GENERATIVE-PARADIGMS

- Target: books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md
- Exact anchor: ## Cache、rollback 与 exactness
- Families: SF-2026-ARXIV-2606-27732
- Owner-merged minimal delta: 并行文本生成不必只在全双向重算与纯 causal cache 之间二选一：受限 right-context side path 可以提供可编辑上下文，causal path 则保留 append-friendly state。generation identity 因而必须记录 mutable context 由哪条路径持有、哪些 cache entry 可复用，以及 provisional span 在何时提交。
- Coexistence/fallback boundary: Side path 增加参数、训练耦合与 cache-version 复杂度；要求 exact streaming 或 kernel 不支持时回退 causal generation。

## MULTIMODAL-WORLD-MODELS

- Target: books/part-03-multimodal-world-models/25-multimodal-world-models.md
- Exact anchor: ## State ownership
- Families: SF-2026-ARXIV-2606-27681
- Owner-merged minimal delta: 若预测器可以绕过声明的 state 重读原始历史，预测正确也无法识别 state 本身是否有效。应让版本化 belief state 成为 transition/prediction path 的唯一受控输入，再检查它是否保留下游 consumer 所需信息。这样 state representation 才从辅助解释升级为可审计接口。
- Coexistence/fallback boundary: Strict mediation 增加训练成本，也可能让有损 textual state 成为瓶颈；无需可识别性时，直接 latent/history access 仍是合理旧路径。

## PLATFORM-COST

- Target: books/part-06-ai-infrastructure/70-cost.md
- Exact anchor: ## 利用率与有效利用率
- Families: SF-2026-ARXIV-2606-27841
- Owner-merged minimal delta: 能耗归因应先把一次 model run 拆成 layer/operator measurement，再拟合 architecture-level proxy。可复用 cost model 必须把每次测量绑定到 device、precision、batch/shape 与 utilization regime，然后针对目标 graph 重组；否则 whole-model estimate 会隐藏究竟是哪类 layer 改变 operating point。
- Coexistence/fallback boundary: Layer recomposition 可能遗漏 fusion、memory hierarchy 与 concurrency interaction；生产真值仍由 whole-run meter 持有，漂移时重校 layer model。

## PLATFORM-EVALUATION-SYSTEM

- Target: books/part-06-ai-infrastructure/66-evaluation-system.md
- Exact anchor: ### Evaluator 可以主动制造 Probe，但不能冒充被动观察
- Families: SF-2026-ARXIV-2606-28013, SF-2026-ARXIV-2606-28661
- Owner-merged minimal delta: Evaluation 必须分开 generator 能产生什么，与 release selector 能可靠识别什么。对 formalization，type acceptance 与 semantic equivalence 是两个独立 signal；对 repeated sampling，answer coverage 与 selection accuracy 必须分报，并显式记录 correlation/modal ceiling。增加 sample budget 不能修复无法识别已覆盖答案的 oracle 或 selector。
- Coexistence/fallback boundary: Semantic judge 与 selector 都可能错误或相关；uncovered/undecidable 必须保持 Unknown，高风险分歧交回独立 verification 或人工。

## PLATFORM-MONITORING

- Target: books/part-06-ai-infrastructure/67-monitoring.md
- Exact anchor: ## Monitoring 也会改变系统
- Families: SF-2026-ARXIV-2606-28116
- Owner-merged minimal delta: Training-instability monitoring 应在 aggregate loss 发散前读取 mechanism-adjacent state：attention spectrum、router/load state 与 update statistic 是分别校准、绑定 checkpoint 的 sensor。它们可以触发暂停、诊断或 rollback，但不能自动拥有 root-cause truth；sensor 漂移或相互冲突时必须 abstain，并保留最近已验证 checkpoint 作为 fallback。
- Coexistence/fallback boundary: Pre-loss signal 可能噪声大且依赖 family；它们保持 observe-first，缺失校准时 abstain，不能自动干预训练。

## PLATFORM-SECURITY

- Target: books/part-06-ai-infrastructure/72-security.md
- Exact anchor: ## 风险管理而不是一次性认证
- Families: SF-2026-ARXIV-2606-28649
- Owner-merged minimal delta: Robot middleware 会把 OCR、speech 与 range-derived state 序列化进高优先级 model context，因此 role label 不能建立信任。provenance 与 integrity check 必须沿 sensor data 经 middleware transformation 进入 prompt 的路径传播，并在 actuation 前保留 cross-modal consistency check 与 controller-side deny/hold path；未知或冲突的 sensory context 不得继承 system authority。
- Coexistence/fallback boundary: 证据只覆盖特定 ROS 2 transformation 与 attack，不覆盖所有 sensor/model；provenance 缺失或 modality 冲突时，在 action 前 fail closed。

## TRAIN-DISTRIBUTED-TRAINING

- Target: books/part-04-training-system/36-distributed-training.md
- Exact anchor: ### 从 Phase 串行到依赖驱动的跨 Phase 重排
- Families: SF-2026-ARXIV-2606-27797
- Owner-merged minimal delta: 知识蒸馏 runtime 不应强迫 teacher inference 与 student training 共用一份并行方案，而应按两类 workload 分别分片。它们的参数驻留、activation lifetime、batch shape 与通信 critical path 均不同；真正的 handoff 是 student update 消费的版本化 teacher output，而不是共享 rank topology。
- Coexistence/fallback boundary: 非对称方案增加 handoff buffering 与 topology search；teacher/student footprint 相近时，共享方案仍更简单。

## TRAIN-LORA

- Target: books/part-04-training-system/30-lora.md
- Exact anchor: ## Checkpoint 与可复现性
- Families: SF-2026-ARXIV-2606-28479
- Owner-merged minimal delta: Privacy-preserving adaptation 需要 matched-update causal ladder。在固定 base revision、adapter identity 与 training budget 后，pseudonymization、differential privacy 与 optimizer/update-count effect 必须独立变化；否则 memorization 降低无法归因给 privacy mechanism。DP 继续拥有 formal guarantee，empirical probe 只测量给定 attack 下的 leakage。
- Coexistence/fallback boundary: Matched control 增加实验成本，empirical attack 的 recall 也有边界；未测到 leakage 不是 privacy guarantee，不确定时保留更严格 data/DP path。

