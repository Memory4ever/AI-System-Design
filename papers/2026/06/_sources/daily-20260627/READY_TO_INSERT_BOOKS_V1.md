# 2026-06-27 Ready-to-Insert Books Packet V1

Source denominator DEN-20260627-aef6bb58. Insert each owner block once and preserve every independent exact-v1 Review note.

## AGENT-PLANNING — books/part-07-agent/79-planning.md

Insert after: ## 完成证据与 Verification

### Owner-merged minimal durable delta

语言 planner 可以保留语义 proposal authority，同时由小型 parametric transition model 检查 imagined state delta 是否满足动力学。两者分歧时应开启 targeted revision，而不是静默替换 planner 或提交 action；transition model 只做 bounded verifier，environment/controller 继续拥有最终 authority。

### Trade-off、failure、fallback 与 coexistence

Learned transition verifier 可能与 planner 共享盲点，也不是 physics oracle；分歧或 OOD state 回退 environment validation 或人工复核。

### Source-specific exact-v1 Review notes

- SF-2026-ARXIV-2606-27806 — primary arXiv:2606.27806v1; exact-v1 URL=https://arxiv.org/html/2606.27806v1; Method=https://arxiv.org/html/2606.27806v1 — §Our approach: GILP.; LLM API ecosystem.; 4 Method: Grounded Iterative Language Planning; Evaluation=https://arxiv.org/html/2606.27806v1 — §5 Experiments; Setup.; Cost analysis.; Non-proof=https://arxiv.org/html/2606.27806v1 — §6 Discussion; 7 Limitations; 8 Conclusion。

## INFER-REQUEST-LIFECYCLE — books/part-05-inference-system/42-what-happens-during-inference.md

Insert after: ## 请求状态机

### Owner-merged minimal durable delta

Inference capacity 是 phase-coupled closed loop，不是单个 kernel 数字。request record 必须区分 vision encoding、prefill、decode、queue/host work 与 device placement；kernel-level simulation 可以预测候选配置，但 promotion 必须回到目标硬件上的 task completion time 与 success。改变 control cadence 或移动瓶颈的局部加速，不自动等于更快完成成功任务。

### Trade-off、failure、fallback 与 coexistence

Simulation 与 component latency 不证明生产 SLO 或 embodied success；mismatch、thermal drift 或 deadline miss 时回退已实测的保守 placement/control。

### Source-specific exact-v1 Review notes

- SF-2026-ARXIV-2606-27906 — primary arXiv:2606.27906v1; exact-v1 URL=https://arxiv.org/html/2606.27906v1; Method=https://arxiv.org/html/2606.27906v1 — §7.2. Methodology and Outcomes on Phi-3.5-V; Evaluation=https://arxiv.org/html/2606.27906v1 — §2. Platform and Experimental Setup; 3.1. Phase-Level Results; 6.1. Three-Backend Benchmark; Non-proof=https://arxiv.org/html/2606.27906v1 — §8. Discussion; 10. Conclusion。
- SF-2026-ARXIV-2606-28529 — primary arXiv:2606.28529v1; exact-v1 URL=https://arxiv.org/html/2606.28529v1; Method=https://arxiv.org/html/2606.28529v1 — §Optimization Methods.; B.1 Optimization Method Settings; Evaluation=https://arxiv.org/html/2606.28529v1 — §4 Experiments; 4.1 Setup; Simulation Task Setup.; Non-proof=https://arxiv.org/html/2606.28529v1 — §5 Conclusion; 6 Limitations; A.3 Assumptions and Limitations。
- SF-2026-ARXIV-2606-28565 — primary arXiv:2606.28565v1; exact-v1 URL=https://arxiv.org/html/2606.28565v1; Method=https://arxiv.org/html/2606.28565v1 — §2.1. Modern LLMs and Inference Frameworks; 3.3. Gaps in Existing Approaches; 4. Tool Architecture and Methodologies; Evaluation=https://arxiv.org/html/2606.28565v1 — §5.2. Production Kernel Microbenchmarking; 6. Experimental Setup; 7. Results and Analysis; Non-proof=https://arxiv.org/html/2606.28565v1 — §8. Conclusions; Appendix B Limitations。

## MULTIMODAL-EMBODIED-VLA — books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md

Insert after: ## Safety envelope

### Owner-merged minimal durable delta

Scene-generation pipeline 应把 video reconstruction、editable scene variant、policy training 与 real-world validation 保存为由 provenance 连接的独立 artifact。visual fidelity 只能决定 scene 能否进入 simulation，不拥有 sim-to-real validity；synthetic scene family 影响物理 promotion 前，policy ranking 必须与 matched real outcome 对读。

### Trade-off、failure、fallback 与 coexistence

Reconstruction quality 与 simulator ranking 不证明 contact dynamics 或 safety；rank mismatch 或未知 embodiment 会阻断物理 promotion，并保留 real-data/controller gate。

### Source-specific exact-v1 Review notes

- SF-2026-ARXIV-2606-28276 — primary arXiv:2606.28276v1; exact-v1 URL=https://arxiv.org/html/2606.28276v1; Method=https://arxiv.org/html/2606.28276v1 — §SimFoundry outperforms state-of-the-art simulation evaluation frameworks and makes fewer assumptions.; 5.2 Sim-to-Real Policy Training; Co-training with sim and real data further improves performance.; Evaluation=https://arxiv.org/html/2606.28276v1 — §SimFoundry: Modular and Automated Scene Generation for Policy Learning and Evaluation; 5 Experiments; 5.1 Real-to-Sim Policy Evaluation; Non-proof=https://arxiv.org/html/2606.28276v1 — §6 Limitations; 7 Conclusion; Appendix C Limitations。

## MULTIMODAL-GENERATIVE-PARADIGMS — books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md

Insert after: ## Cache、rollback 与 exactness

### Owner-merged minimal durable delta

并行文本生成不必只在全双向重算与纯 causal cache 之间二选一：受限 right-context side path 可以提供可编辑上下文，causal path 则保留 append-friendly state。generation identity 因而必须记录 mutable context 由哪条路径持有、哪些 cache entry 可复用，以及 provisional span 在何时提交。

### Trade-off、failure、fallback 与 coexistence

Side path 增加参数、训练耦合与 cache-version 复杂度；要求 exact streaming 或 kernel 不支持时回退 causal generation。

### Source-specific exact-v1 Review notes

- SF-2026-ARXIV-2606-27732 — primary arXiv:2606.27732v1; exact-v1 URL=https://arxiv.org/html/2606.27732v1; Method=https://arxiv.org/html/2606.27732v1 — §3 Method; 3.4 R2LM Architecture; 3.5 Training and Inference; Evaluation=https://arxiv.org/html/2606.27732v1 — §4 Experiments; 4.1 Experimental Setup; 4.2 Main Results: Multiple-Choice Benchmarks; Non-proof=https://arxiv.org/html/2606.27732v1 — §5 Conclusion。

## MULTIMODAL-WORLD-MODELS — books/part-03-multimodal-world-models/25-multimodal-world-models.md

Insert after: ## State ownership

### Owner-merged minimal durable delta

若预测器可以绕过声明的 state 重读原始历史，预测正确也无法识别 state 本身是否有效。应让版本化 belief state 成为 transition/prediction path 的唯一受控输入，再检查它是否保留下游 consumer 所需信息。这样 state representation 才从辅助解释升级为可审计接口。

### Trade-off、failure、fallback 与 coexistence

Strict mediation 增加训练成本，也可能让有损 textual state 成为瓶颈；无需可识别性时，直接 latent/history access 仍是合理旧路径。

### Source-specific exact-v1 Review notes

- SF-2026-ARXIV-2606-27681 — primary arXiv:2606.27681v1; exact-v1 URL=https://arxiv.org/html/2606.27681v1; Method=https://arxiv.org/html/2606.27681v1 — §Proposition 2 (Non-identifiability under leaky architectures) .; Proposition 3 (Training–inference consistency) .; 4.2 Model Architecture; Evaluation=https://arxiv.org/html/2606.27681v1 — §2 Problem Setup: Text Based POMDPs; 5 Experimental Evaluation; 5.3 Evaluation Metrics; Non-proof=https://arxiv.org/html/2606.27681v1 — §7 Conclusion。

## PLATFORM-COST — books/part-06-ai-infrastructure/70-cost.md

Insert after: ## 利用率与有效利用率

### Owner-merged minimal durable delta

能耗归因应先把一次 model run 拆成 layer/operator measurement，再拟合 architecture-level proxy。可复用 cost model 必须把每次测量绑定到 device、precision、batch/shape 与 utilization regime，然后针对目标 graph 重组；否则 whole-model estimate 会隐藏究竟是哪类 layer 改变 operating point。

### Trade-off、failure、fallback 与 coexistence

Layer recomposition 可能遗漏 fusion、memory hierarchy 与 concurrency interaction；生产真值仍由 whole-run meter 持有，漂移时重校 layer model。

### Source-specific exact-v1 Review notes

- SF-2026-ARXIV-2606-27841 — primary arXiv:2606.27841v1; exact-v1 URL=https://arxiv.org/html/2606.27841v1; Method=https://arxiv.org/html/2606.27841v1 — §3 Methodology and Experimental Set-up; 3.2 Layer-Wise Energy Estimation Framework; Evaluation=https://arxiv.org/html/2606.27841v1 — §3 Methodology and Experimental Set-up; 3.1 Experimental Protocol; 4 Results; Non-proof=https://arxiv.org/html/2606.27841v1 — §5 Discussion; 6 Conclusion。

## PLATFORM-EVALUATION-SYSTEM — books/part-06-ai-infrastructure/66-evaluation-system.md

Insert after: ### Evaluator 可以主动制造 Probe，但不能冒充被动观察

### Owner-merged minimal durable delta

Evaluation 必须分开 generator 能产生什么，与 release selector 能可靠识别什么。对 formalization，type acceptance 与 semantic equivalence 是两个独立 signal；对 repeated sampling，answer coverage 与 selection accuracy 必须分报，并显式记录 correlation/modal ceiling。增加 sample budget 不能修复无法识别已覆盖答案的 oracle 或 selector。

### Trade-off、failure、fallback 与 coexistence

Semantic judge 与 selector 都可能错误或相关；uncovered/undecidable 必须保持 Unknown，高风险分歧交回独立 verification 或人工。

### Source-specific exact-v1 Review notes

- SF-2026-ARXIV-2606-28013 — primary arXiv:2606.28013v1; exact-v1 URL=https://arxiv.org/html/2606.28013v1; Method=https://arxiv.org/html/2606.28013v1 — §Methods.; 5.1 Per-method cell decomposition; 5.4 A predictive regularity: stratum-rates are method-invariant; Evaluation=https://arxiv.org/html/2606.28013v1 — §4 Experimental Setup; 5 Experimental Results and Analysis; Non-proof=https://arxiv.org/html/2606.28013v1 — §6 Discussion and Limitations; 7 Conclusion。
- SF-2026-ARXIV-2606-28661 — primary arXiv:2606.28661v1; exact-v1 URL=https://arxiv.org/html/2606.28661v1; Method=https://arxiv.org/html/2606.28661v1 — §Proposition 1 (Design effect of test-time sampling) .; Two-stage design effect.; Evaluation=https://arxiv.org/html/2606.28661v1 — §1 Introduction and roadmap; 2 Test-time sampling is cluster sampling; Non-proof=https://arxiv.org/html/2606.28661v1 — §6 Conclusion。

## PLATFORM-MONITORING — books/part-06-ai-infrastructure/67-monitoring.md

Insert after: ## Monitoring 也会改变系统

### Owner-merged minimal durable delta

Training-instability monitoring 应在 aggregate loss 发散前读取 mechanism-adjacent state：attention spectrum、router/load state 与 update statistic 是分别校准、绑定 checkpoint 的 sensor。它们可以触发暂停、诊断或 rollback，但不能自动拥有 root-cause truth；sensor 漂移或相互冲突时必须 abstain，并保留最近已验证 checkpoint 作为 fallback。

### Trade-off、failure、fallback 与 coexistence

Pre-loss signal 可能噪声大且依赖 family；它们保持 observe-first，缺失校准时 abstain，不能自动干预训练。

### Source-specific exact-v1 Review notes

- SF-2026-ARXIV-2606-28116 — primary arXiv:2606.28116v1; exact-v1 URL=https://arxiv.org/html/2606.28116v1; Method=https://arxiv.org/html/2606.28116v1 — §Mechanism-Driven Monitors for Preemptive Detection of LLM Training Instability; Training-stability monitors.; 5 Designing Module-Specific Monitors from First Principles; Evaluation=https://arxiv.org/html/2606.28116v1 — §Mechanism-Driven Monitors for Preemptive Detection of LLM Training Instability; 1 Introduction; Non-proof=https://arxiv.org/html/2606.28116v1 — §6 Limitations; 7 Conclusion。

## PLATFORM-SECURITY — books/part-06-ai-infrastructure/72-security.md

Insert after: ## 风险管理而不是一次性认证

### Owner-merged minimal durable delta

Robot middleware 会把 OCR、speech 与 range-derived state 序列化进高优先级 model context，因此 role label 不能建立信任。provenance 与 integrity check 必须沿 sensor data 经 middleware transformation 进入 prompt 的路径传播，并在 actuation 前保留 cross-modal consistency check 与 controller-side deny/hold path；未知或冲突的 sensory context 不得继承 system authority。

### Trade-off、failure、fallback 与 coexistence

证据只覆盖特定 ROS 2 transformation 与 attack，不覆盖所有 sensor/model；provenance 缺失或 modality 冲突时，在 action 前 fail closed。

### Source-specific exact-v1 Review notes

- SF-2026-ARXIV-2606-28649 — primary arXiv:2606.28649v1; exact-v1 URL=https://arxiv.org/html/2606.28649v1; Method=https://arxiv.org/html/2606.28649v1 — §II-C Security of ROS-Based Systems; III-A System Model; IV Methodology; Evaluation=https://arxiv.org/html/2606.28649v1 — §V Experimental Results; V-B Firewall Defense Evaluation; V-C Firewall Bypass Analysis; Non-proof=https://arxiv.org/html/2606.28649v1 — §III Threat Model; VI Discussion; VI-C The Sensory Vector as a Distinct Threat。

## TRAIN-DISTRIBUTED-TRAINING — books/part-04-training-system/36-distributed-training.md

Insert after: ### 从 Phase 串行到依赖驱动的跨 Phase 重排

### Owner-merged minimal durable delta

知识蒸馏 runtime 不应强迫 teacher inference 与 student training 共用一份并行方案，而应按两类 workload 分别分片。它们的参数驻留、activation lifetime、batch shape 与通信 critical path 均不同；真正的 handoff 是 student update 消费的版本化 teacher output，而不是共享 rank topology。

### Trade-off、failure、fallback 与 coexistence

非对称方案增加 handoff buffering 与 topology search；teacher/student footprint 相近时，共享方案仍更简单。

### Source-specific exact-v1 Review notes

- SF-2026-ARXIV-2606-27797 — primary arXiv:2606.27797v1; exact-v1 URL=https://arxiv.org/html/2606.27797v1; Method=https://arxiv.org/html/2606.27797v1 — §Optimizing Teacher-Student Partitioning for Scalable Knowledge Distillation on HPC Systems; 2 Background: LLM Training and Parallelism; 2.1 LLM Training; Evaluation=https://arxiv.org/html/2606.27797v1 — §3 Testing Setup; 4 GKD Analysis and Improvements; 4.1 Experimental Results; Non-proof=https://arxiv.org/html/2606.27797v1 — §6 Conclusions。

## TRAIN-LORA — books/part-04-training-system/30-lora.md

Insert after: ## Checkpoint 与可复现性

### Owner-merged minimal durable delta

Privacy-preserving adaptation 需要 matched-update causal ladder。在固定 base revision、adapter identity 与 training budget 后，pseudonymization、differential privacy 与 optimizer/update-count effect 必须独立变化；否则 memorization 降低无法归因给 privacy mechanism。DP 继续拥有 formal guarantee，empirical probe 只测量给定 attack 下的 leakage。

### Trade-off、failure、fallback 与 coexistence

Matched control 增加实验成本，empirical attack 的 recall 也有边界；未测到 leakage 不是 privacy guarantee，不确定时保留更严格 data/DP path。

### Source-specific exact-v1 Review notes

- SF-2026-ARXIV-2606-28479 — primary arXiv:2606.28479v1; exact-v1 URL=https://arxiv.org/html/2606.28479v1; Method=https://arxiv.org/html/2606.28479v1 — §III Threat Model and Methodology; Evaluation=https://arxiv.org/html/2606.28479v1 — §VI Utility Evaluation; Non-proof=https://arxiv.org/html/2606.28479v1 — §III Threat Model and Methodology; III-A Threat Model; VII Discussion。

