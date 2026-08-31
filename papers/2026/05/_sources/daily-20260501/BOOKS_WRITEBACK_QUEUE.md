# 2026-05-01 Books Writeback Queue

root 已按事件时间完成共享 Books 写回；非写作者已顺读 owner 与相邻章节并完成 post-write 语义审计。审计收据：`post-write-semantic-audit.json`。

## Queue Status

| Source Family | Final Status |
| --- | --- |
| SF-2026-ARXIV-2604-27844 | applied_post_write_audited |
| SF-2026-ARXIV-2604-28138 | applied_post_write_audited |
| SF-2026-ARXIV-2605-00254 | applied_post_write_audited |
| SF-2026-ARXIV-2605-00300 | applied_post_write_audited |
| SF-2026-ARXIV-2605-00314 | applied_post_write_audited |
| SF-2026-ARXIV-2604-27306 | applied_post_write_audited |
| SF-2026-ARXIV-2604-27358 | applied_post_write_audited |
| SF-2026-ARXIV-2604-27405 | applied_post_write_audited |
| SF-2026-ARXIV-2604-27426 | applied_post_write_audited |
| SF-2026-ARXIV-2604-27536 | applied_post_write_audited |
| SF-2026-ARXIV-2604-27586 | applied_post_write_audited |
| SF-2026-ARXIV-2604-27637 | applied_post_write_audited |
| SF-2026-ARXIV-2604-27819 | applied_post_write_audited |
| SF-2026-ARXIV-2604-27855 | applied_post_write_audited |
| SF-2026-ARXIV-2604-28056 | applied_post_write_audited |
| SF-2026-ARXIV-2604-28123 | applied_post_write_audited |
| SF-2026-ARXIV-2604-28129 | applied_post_write_audited |
| SF-2026-ARXIV-2604-28175 | applied_post_write_audited |
| SF-2026-ARXIV-2604-28182 | applied_post_write_audited |
| SF-2026-ARXIV-2604-28190 | applied_post_write_audited |
| SF-2026-ARXIV-2604-27891 | applied_post_write_audited |
| SF-2026-ARXIV-2604-27467 | applied_post_write_audited |
| SF-2026-ARXIV-2604-27486 | applied_post_write_audited |
| SF-2026-ARXIV-2604-27878 | applied_post_write_audited |

## SF-2026-ARXIV-2604-27844

- Owner: `TRAIN-DISTRIBUTED-TRAINING`
- Target: `books/part-04-training-system/36-distributed-training.md#L69`
- Adjacent: `books/part-04-training-system/37-data-parallel.md#L1; books/part-04-training-system/41-distributed-training-runtime.md#L1`
- Existing owner coverage: Ch36 已拥有 collective 语义、算法/transport/topology 分层和 bandwidth/latency/overlap 成本模型。
- Missing durable delta: 尚未把 bit-exact exponent coding、GPU encode/decode critical path 与 adaptive fallback 写成同一条 compression contract。
- Proposition: 通信压缩只有在 encode/decode 不把 network bottleneck 迁移为 GPU critical-path bottleneck 时才成立；lossless exponent coding 与 collective-aware layout 以 bit-exactness 换取数据分布假设和额外 kernel/switcher 控制状态。
- Trade-off boundary: §6.6 observed tensor normality is workload-specific; paper does not prove universal distributions
- Exact primary: https://arxiv.org/html/2604.27844v1

## SF-2026-ARXIV-2604-28138

- Owner: `AGENT-PLATFORM`
- Target: `books/part-07-agent/84-agent-platform.md#L50`
- Adjacent: `books/part-07-agent/81-workflow.md#L1; books/part-06-ai-infrastructure/73-production-practices.md#L1`
- Existing owner coverage: Ch84 已把 AgentRun、workflow state、tool side effect 和 terminal evidence 区分于 transcript/KV。
- Missing durable delta: 尚未具体说明 turn-boundary checkpoint 如何联合捕获 filesystem/process/tool state，以及稀疏检测如何引入 false-negative 与 co-location contention。
- Proposition: Agent recovery state 不等于 chat history：tool side effects、filesystem、process 与 runtime artifact 必须在 turn boundary 形成可提交 checkpoint；语义稀疏检测减少 checkpoint traffic，却引入 eBPF 分类误差、co-location contention 与 restore consistency。
- Trade-off boundary: §9 Conclusion — exact-v1 has no dedicated limitations section; evidence is confined to Linux sandbox workloads and evaluated C/R backends
- Exact primary: https://arxiv.org/html/2604.28138v1

## SF-2026-ARXIV-2605-00254

- Owner: `INFER-SCHEDULING`
- Target: `books/part-05-inference-system/56-inference-scheduling.md#L35`
- Adjacent: `books/part-05-inference-system/52-distributed-inference.md#L1; books/part-05-inference-system/55-inference-memory-optimization.md#L1`
- Existing owner coverage: Ch52/Ch56 已拥有 distributed inference 的 placement、network tier、hotspot 与 scheduling state。
- Missing durable delta: 尚未把 MoE expert placement、token skew、all-to-all bytes、topology cost 与 reconfiguration/failure domain 联合为一个 serving decision。
- Proposition: MoE serving topology 必须把 expert placement、token skew、all-to-all bytes、network tiers 与 replica cost 联合建模；更便宜的 topology 会把平均带宽收益换成 hotspot、reconfiguration 和 failure-domain 压力。
- Trade-off boundary: §7 Conclusion — exact-v1 has no dedicated limitations section; scenario assumptions and cost model are not universal production measurements
- Exact primary: https://arxiv.org/html/2605.00254v1

## SF-2026-ARXIV-2605-00300

- Owner: `PLATFORM-EVALUATION-SYSTEM`
- Target: `books/part-06-ai-infrastructure/66-evaluation-system.md#L35`
- Adjacent: `books/part-05-inference-system/56-inference-scheduling.md#L55; books/part-06-ai-infrastructure/69-cost-management.md#L1`
- Existing owner coverage: Ch66 已要求 benchmark 冻结 workload、evaluator、版本与 evidence；Ch69 拥有成本维度。
- Missing durable delta: 尚未把 endpoint/model configuration 定义为版本化原子对象，并在同一连续 contract 记录能耗、质量、延迟、价格与可靠性。
- Proposition: Inference benchmark 的原子对象可以是 endpoint/model configuration，而不是模型名称；能耗、质量、延迟与请求策略必须在连续、版本化 contract 中共同记录，且偏好结论不能脱离 evaluator 与 workload。
- Trade-off boundary: §6 discussion and limitations on provider drift, observability and evaluator scope
- Exact primary: https://arxiv.org/html/2605.00300v1

## SF-2026-ARXIV-2605-00314

- Owner: `PLATFORM-SECURITY`
- Target: `books/part-06-ai-infrastructure/72-security.md#L14`
- Adjacent: `books/part-07-agent/78-tool-calling.md#L42; books/part-07-agent/83-mcp.md#L40`
- Existing owner coverage: Ch72 已拥有 tool/skill 的 artifact、capability、data-flow 与 runtime-effect 审计边界。
- Missing durable delta: 尚未说明如何由自然语言和代码合成有限 SDL fact base，再由 Datalog 约束检查 source-to-sink、permission 与 effect。
- Proposition: Agent skill 审计需要把自然语言/代码能力合成为可查询的约束表示，再在调用前检查 source→sink、permission 与 effect；静态分析提高可解释性，却受表示不完备、动态行为与环境依赖限制。
- Trade-off boundary: §7 Conclusion — exact-v1 has no dedicated limitations section; static abstraction cannot prove dynamic runtime safety
- Exact primary: https://arxiv.org/html/2605.00314v1

## SF-2026-ARXIV-2604-27306

- Owner: `AGENT-RAG`
- Target: `books/part-07-agent/76-rag.md#L1`
- Adjacent: `books/part-07-agent/75-context.md#L1; books/part-07-agent/77-memory.md#L1`
- Existing owner coverage: Ch76 已要求 provenance、temporal validity 与 source authority 随 retrieval evidence 传播。
- Missing durable delta: 尚未把 atomic nugget 的 validity/lifecycle 写成 ranking 前 admission 与失效淘汰状态机。
- Proposition: 可维护 RAG 的 retrieval object 不应只是 passage：带 evidence、validity interval 与 lifecycle state 的 atomic nugget 让失效事实在 ranking 前退出，并把来源冲突变成显式状态。
- Trade-off boundary: §6/§7 selected QA corpora and author metrics do not prove a universal source-authority policy
- Exact primary: https://arxiv.org/html/2604.27306v1

## SF-2026-ARXIV-2604-27358

- Owner: `AGENT-MULTI-AGENT`
- Target: `books/part-07-agent/82-multi-agent.md#L1`
- Adjacent: `books/part-07-agent/79-planning.md#L1; books/part-06-ai-infrastructure/72-security.md#L1`
- Existing owner coverage: Ch82 已区分 role、communication topology 与 orchestrator authority。
- Missing durable delta: 尚未把 delegation degree 建模为受 safety constraint 约束的运行时控制变量，并显式保留责任传播边界。
- Proposition: Delegation degree 是运行时控制变量而非静态拓扑：bilevel controller 在效用与 safety constraint 间调节子代理权限，并要求 responsibility propagation 可验证。
- Trade-off boundary: Not Disclosed — exact-v1 has no dedicated Limitations heading; bounded non-proof: exact-v1 explicitly leaves empirical validation to future work; formal assumptions do not prove deployable runtime safety
- Exact primary: https://arxiv.org/html/2604.27358v1

## SF-2026-ARXIV-2604-27405

- Owner: `PLATFORM-EVALUATION-SYSTEM`
- Target: `books/part-06-ai-infrastructure/66-evaluation-system.md#L1`
- Adjacent: `books/part-06-ai-infrastructure/67-monitoring.md#L1; books/part-06-ai-infrastructure/73-production-best-practice.md#L1`
- Existing owner coverage: Ch66 已要求版本化对象、重复采样、uncertainty 与 release gate。
- Missing durable delta: 尚未说明 aggregate delta 会掩盖 item-level 双向 churn，以及 RCI 类 harmed/helped ledger 如何进入兼容性判断。
- Proposition: 版本平均分会掩盖 item-level 双向 churn；release gate 需要 within-model reliable change、sampling variance 与 harmed/helped item ledger，而不是只比较 aggregate delta。
- Trade-off boundary: Not Disclosed — exact-v1 has no dedicated Limitations heading; bounded non-proof: two families and one benchmark do not calibrate a universal RCI threshold or production consequence
- Exact primary: https://arxiv.org/html/2604.27405v1

## SF-2026-ARXIV-2604-27426

- Owner: `PLATFORM-SECURITY`
- Target: `books/part-06-ai-infrastructure/72-security.md#L1`
- Adjacent: `books/part-04-training-system/29-sft.md#L1; books/part-06-ai-infrastructure/73-production-best-practice.md#L1`
- Existing owner coverage: Ch72 已拥有 artifact provenance、sandbox、secret 与 egress policy。
- Missing durable delta: 尚未把 local fine-tuning model code 明确视为先于 dataset access 获得执行权的供应链主体。
- Proposition: Local/offline fine-tuning is not a privacy boundary when model repository code owns the executable training path; artifact provenance, sandboxing and egress control must precede dataset access. May steal training secrets.
- Trade-off boundary: Not Disclosed — exact-v1 has no dedicated Limitations heading; bounded non-proof: demonstrated attacks do not establish ecosystem prevalence; controls depend on the actual loader/runtime boundary
- Exact primary: https://arxiv.org/html/2604.27426v1

## SF-2026-ARXIV-2604-27536

- Owner: `INFER-SCHEDULING`
- Target: `books/part-05-inference-system/56-inference-scheduling.md#L1`
- Adjacent: `books/part-06-ai-infrastructure/66-evaluation-system.md#L1; books/part-06-ai-infrastructure/70-cost.md#L1`
- Existing owner coverage: Ch56 已由 workload/SLO/cost profile 拥有 admission 与 routing。
- Missing durable delta: 尚未覆盖黑盒服务只有 verifiable partial observations 时的 belief update、escalation value 与 budgeted stopping。
- Proposition: 黑盒服务的 stronger-path escalation 是部分可观测的预算决策：controller 必须由 verifiable observation 更新 belief，并把 expected reliability gain 与增量推理成本联合 admission。
- Trade-off boundary: Not Disclosed — exact-v1 has no dedicated Limitations heading; bounded non-proof: proxy-verifier calibration and workload stationarity limit generalization to unseen services
- Exact primary: https://arxiv.org/html/2604.27536v1

## SF-2026-ARXIV-2604-27586

- Owner: `PLATFORM-TRACE`
- Target: `books/part-06-ai-infrastructure/69-trace.md#L1`
- Adjacent: `books/part-07-agent/81-workflow.md#L1; books/part-06-ai-infrastructure/66-evaluation-system.md#L1`
- Existing owner coverage: Ch69/Ch81 已要求跨 step trace、artifact lineage 与 terminal evidence。
- Missing durable delta: 尚未把 contamination 视为可先改变 decomposition/routing、后影响最终输出的 control-flow divergence。
- Proposition: Agent contamination is a trace property: uncertain evidence can alter decomposition/routing before appearing in the final answer, so provenance must follow artifact transformations and control-flow divergence across steps.
- Trade-off boundary: Not Disclosed — exact-v1 has no dedicated Limitations heading; bounded non-proof: synthetic workflows and chosen corruption models do not quantify real-world prevalence or causal completeness
- Exact primary: https://arxiv.org/html/2604.27586v1

## SF-2026-ARXIV-2604-27637

- Owner: `PLATFORM-EVALUATION-SYSTEM`
- Target: `books/part-06-ai-infrastructure/66-evaluation-system.md#L1`
- Adjacent: `books/part-07-agent/74-prompt.md#L1; books/part-06-ai-infrastructure/73-production-best-practice.md#L1`
- Existing owner coverage: Ch66 已冻结 model、prompt、evaluator 与 workload identity。
- Missing durable delta: 尚未明确区分 common-prompt comparability 与 per-model optimized deployment contract，并记录两者对 ranking 的不同解释。
- Proposition: Cross-model evaluation must distinguish a frozen common-prompt contract from a per-model optimized deployment contract; otherwise prompt mismatch can change rankings and misattribute interface quality to model weights.
- Trade-off boundary: Not Disclosed — exact-v1 has no dedicated Limitations heading; bounded non-proof: selected optimizers, tasks and search budgets do not define a universally fair evaluation regime
- Exact primary: https://arxiv.org/html/2604.27637v1

## SF-2026-ARXIV-2604-27819

- Owner: `AGENT-MCP`
- Target: `books/part-07-agent/83-mcp.md#L1`
- Adjacent: `books/part-06-ai-infrastructure/72-security.md#L1; books/part-07-agent/78-tool-calling.md#L1`
- Existing owner coverage: Ch83/Ch72 已拥有 MCP server identity、capability 与执行边界。
- Missing durable delta: 尚未说明 benign read/write permission 如何经多 server workflow 合成为跨域泄漏，以及 canary taint 如何跨 tool edge 传播。
- Proposition: Multi-server MCP safety is an information-flow problem: individually permitted read/write tools can compose into a cross-boundary leak, so canary taint must survive tool-call edges and server identities.
- Trade-off boundary: Not Disclosed — exact-v1 has no dedicated Limitations heading; bounded non-proof: synthetic canaries and enumerated servers do not prove complete semantic non-interference
- Exact primary: https://arxiv.org/html/2604.27819v1

## SF-2026-ARXIV-2604-27855

- Owner: `PLATFORM-COST`
- Target: `books/part-06-ai-infrastructure/70-cost.md#L1`
- Adjacent: `books/part-05-inference-system/56-inference-scheduling.md#L1; books/part-06-ai-infrastructure/63-gpu-scheduler.md#L1`
- Existing owner coverage: Ch70/Ch56 已联合考虑 cost、SLO、capacity 与 placement。
- Missing durable delta: 尚未把 energy geography 作为仅在 latency、state locality、capacity 与 regulation 硬约束后才可优化的调度维度。
- Proposition: Inference placement may treat energy geography as a scheduling input only after latency, state locality, capacity and regulation become hard constraints; cheap power alone cannot own routing authority.
- Trade-off boundary: Not Disclosed — exact-v1 has no dedicated Limitations heading; bounded non-proof: analytical inputs and assumed relocatability are not measured production traces or universal grid emissions
- Exact primary: https://arxiv.org/html/2604.27855v1

## SF-2026-ARXIV-2604-28056

- Owner: `TRAIN-RLHF`
- Target: `books/part-04-training-system/31-rlhf.md#L1`
- Adjacent: `books/part-06-ai-infrastructure/66-evaluation-system.md#L1; books/part-06-ai-infrastructure/73-production-best-practice.md#L1`
- Existing owner coverage: Ch31/Ch66 已区分 reward proposal、evaluation 与 release authority。
- Missing durable delta: 尚未把 reward hypothesis 从共享 checkpoint 分叉、competence verification 与 phase-aware deployment 连成一条控制链。
- Proposition: LLM-generated reward hypotheses should fork from a shared checkpoint, pass competence-aware verification and deploy by training phase; generation quality does not grant reward release authority.
- Trade-off boundary: Not Disclosed — exact-v1 has no dedicated Limitations heading; bounded non-proof: selected environments and verifier signals do not prove reward correctness or prevent all specification gaming
- Exact primary: https://arxiv.org/html/2604.28056v1

## SF-2026-ARXIV-2604-28123

- Owner: `TRAIN-RLHF`
- Target: `books/part-04-training-system/31-rlhf.md#L1`
- Adjacent: `books/part-04-training-system/29-sft.md#L1; books/part-04-training-system/33-grpo.md#L1`
- Existing owner coverage: Ch29→Ch31 已解释 SFT 与 preference/RL 的目标差异。
- Missing durable delta: 尚未显式处理 SFT distribution drift 到 RLVR on-policy distribution 的 handoff，并给出黑盒 distillation 这一条件分支。
- Proposition: SFT→RLVR is not a neutral handoff when SFT shifts the policy distribution; black-box on-policy distillation can insert a pre-alignment bridge, trading extra rollout/teacher cost for a better RL starting distribution.
- Trade-off boundary: Not Disclosed — exact-v1 has no dedicated Limitations heading; bounded non-proof: selected models/tasks and teacher access do not establish universal benefit or cost efficiency
- Exact primary: https://arxiv.org/html/2604.28123v1

## SF-2026-ARXIV-2604-28129

- Owner: `PLATFORM-SECURITY`
- Target: `books/part-06-ai-infrastructure/72-security.md#L1`
- Adjacent: `books/part-06-ai-infrastructure/69-trace.md#L1; books/part-07-agent/75-context.md#L1`
- Existing owner coverage: Ch72 已要求跨 turn threat state 与 effect mediation。
- Missing durable delta: 尚未补充 residual activation trajectory 这一 white-box detector 分支、模型更新后的 recalibration 和 hosted-model 不可用边界。
- Proposition: Multi-turn attacks may be benign turn-by-turn yet form a residual-activation trajectory; adaptive probes add a model-specific internal signal but cannot replace effect mediation or cross-version recalibration.
- Trade-off boundary: Not Disclosed — exact-v1 has no dedicated Limitations heading; bounded non-proof: white-box activations and model-specific probes limit hosted-model use and require recalibration after updates
- Exact primary: https://arxiv.org/html/2604.28129v1

## SF-2026-ARXIV-2604-28175

- Owner: `INFER-SCHEDULING`
- Target: `books/part-05-inference-system/56-inference-scheduling.md#L1`
- Adjacent: `books/part-05-inference-system/46-continuous-batching.md#L1; books/part-06-ai-infrastructure/63-gpu-scheduler.md#L1`
- Existing owner coverage: Ch56 已由 queue、SLO 和 runtime state 拥有 request scheduling。
- Missing durable delta: 尚未把 priority 与 concurrent interference-conditioned latency prediction 联合，防止优先级把等待迁移为 GPU contention。
- Proposition: Priority-aware serving needs interference-conditioned latency prediction; priority without concurrent-execution estimates merely moves queue delay into GPU contention and can violate both classes' SLOs.
- Trade-off boundary: Not Disclosed — exact-v1 has no dedicated Limitations heading; bounded non-proof: on-premises model roster and hardware do not establish universal predictor transfer or tail-SLO behavior
- Exact primary: https://arxiv.org/html/2604.28175v1

## SF-2026-ARXIV-2604-28182

- Owner: `TRAIN-RLHF`
- Target: `books/part-04-training-system/31-rlhf.md#L1`
- Adjacent: `books/part-04-training-system/32-ppo.md#L1; books/part-04-training-system/33-grpo.md#L1`
- Existing owner coverage: Ch31/Ch32/Ch33 已覆盖 reward hacking、KL 与 rollout/update loop。
- Missing durable delta: 尚未把策略性抑制 exploration 作为独立训练阻抗，并要求 rollout diversity/update diagnostics 成为 release evidence。
- Proposition: Exploration itself is part of the RL trust boundary: a model that suppresses useful actions can resist training without overt reward hacking, so rollout diversity and policy-update diagnostics must be release evidence.
- Trade-off boundary: Not Disclosed — exact-v1 has no dedicated Limitations heading; bounded non-proof: constructed settings do not establish spontaneous prevalence in deployed models or a complete detector
- Exact primary: https://arxiv.org/html/2604.28182v1

## SF-2026-ARXIV-2604-28190

- Owner: `MULTIMODAL-GENERATIVE-PARADIGMS`
- Target: `books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#L1`
- Adjacent: `books/part-04-training-system/28-pretraining.md#L1; books/part-06-ai-infrastructure/66-evaluation-system.md#L1`
- Existing owner coverage: Ch24 已比较 AR、diffusion 与 iterative correction 的 factorization/serving 代价。
- Missing durable delta: 尚未补充 population-statistics 与 gradient batch 解耦后，Fréchet representation distance 可作为受限训练目标的分支。
- Proposition: Distributional representation distance can become a training loss by decoupling the population used to estimate statistics from the gradient batch; this trades estimator state and representation dependence for direct distribution matching.
- Trade-off boundary: Not Disclosed — exact-v1 has no dedicated Limitations heading; bounded non-proof: selected representation encoders and image workloads do not prove perceptual alignment or generalization to all modalities
- Exact primary: https://arxiv.org/html/2604.28190v1

## SF-2026-ARXIV-2604-27891

- Owner: `AGENT-WORKFLOW`
- Target: `books/part-07-agent/81-workflow.md#L1`
- Adjacent: `books/part-07-agent/75-context.md#L1; books/part-07-agent/84-agent-platform.md#L1`
- Existing owner coverage: Ch81 已说明 durable workflow state、side effect、restart 与 audit 需要外部 owner。
- Missing durable delta: 尚未明确外部 graph orchestration 不是默认：procedure 可完整入 context 时，self-routing 可避免 fragment/routing calls，但不能替代 durable commit。
- Proposition: External orchestration is an alternative branch, not a default: when the full procedure fits context and the model can track it, in-context self-routing removes routing calls and fragmentation; durable side effects, audit and restart still require external workflow state.
- Trade-off boundary: §5.2-5.3 three simulated customer-service domains, LLM judges and frontier-model capability bound the conclusion; token cost is higher in-context
- Exact primary: https://arxiv.org/html/2604.27891v1

## SF-2026-ARXIV-2604-27467

- Owner: `PLATFORM-EVALUATION-SYSTEM`
- Target: `books/part-06-ai-infrastructure/66-evaluation-system.md#L1`
- Adjacent: `books/part-04-training-system/31-rlhf.md#L1; books/part-06-ai-infrastructure/73-production-best-practice.md#L1`
- Existing owner coverage: Ch66 已要求 evaluator identity、sandbox、terminal evidence 与 workload version 进入 release evidence；Ch31 已把 verifier signal 与 reward proposal 分离。
- Missing durable delta: 尚未把 special-judge synthesis、test-case parallel execution、multi-node sandbox 与 configuration-driven suite 写成训练和评测共享的 code-verification evidence runtime。
- Proposition: 代码 verifier 不是附属脚本，而是训练与评测共享的 evidence runtime：special-judge synthesis、test-case parallelism、multi-node sandbox 和配置化 suite 共同决定 reward truth、吞吐与可复现性。
- Trade-off boundary: §7 Limitations: generated judges, selected code tasks, sandbox policies and author infrastructure do not prove arbitrary-program correctness or universal RL stability
- Exact primary: https://arxiv.org/html/2604.27467v1

## SF-2026-ARXIV-2604-27486

- Owner: `INFER-TENSORRT-LLM`
- Target: `books/part-05-inference-system/49-tensorrt-llm.md#L220`
- Adjacent: `books/part-06-ai-infrastructure/72-security.md#L1; books/part-06-ai-infrastructure/66-evaluation-system.md#L1`
- Existing owner coverage: Ch49 已解释 PTX/SASS 的架构绑定、post-compilation optimization 与独立 correctness/SLO gate。
- Missing durable delta: 尚未解释 reverse lifting 时 type state 如何由统一 register file 恢复、冲突时为何必须 fail closed，以及 typed LLVM IR 怎样成为二进制审计和迁移的中间证据。
- Proposition: GPU binary lifting 的关键不是语法翻译，而是从统一 register file 恢复 typed state、显式 control flow 与 multi-instruction semantics；conflict detection 决定何时必须拒绝生成可执行 IR。
- Trade-off boundary: §6 evaluation cannot validate MUFU, texture or full SIMT behavior through an x86 backend; supported architectures/instructions bound correctness and require fail-closed handling
- Exact primary: https://arxiv.org/html/2604.27486v1

## SF-2026-ARXIV-2604-27878

- Owner: `PLATFORM-EVALUATION-SYSTEM`
- Target: `books/part-06-ai-infrastructure/66-evaluation-system.md#L1`
- Adjacent: `books/part-07-agent/76-rag.md#L1; books/part-06-ai-infrastructure/67-monitoring.md#L1`
- Existing owner coverage: Ch66 已区分任务成功、过程 evidence、evaluator version 与 release authority。
- Missing durable delta: 尚未明确 simulator 的 behavioral realism 与 tester reliability 是两个可能冲突的 evaluation contract，并要求 canonical session schema、loss accounting 和 ranking-validity evidence 分开出账。
- Proposition: Simulator evaluation must separate behavioral realism from tester reliability：像不像真人与能否保持系统 ranking 是两个可能冲突的 contract，必须共享 canonical session schema、loss accounting 与 runtime applicability metadata。
- Trade-off boundary: §8 Limitations: dataset/language/simulator coverage is finite; correlations do not prove causal transfer to production users or unseen retrieval systems
- Exact primary: https://arxiv.org/html/2604.27878v1
