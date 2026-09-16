# Daily Research — 2026-07-13

**规范：** V3
**窗口：** 2026-07-12T09:00:00+08:00 ～ 2026-07-13T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-09-10T16:30:00+08:00

## 1. 结论

本窗以周末后首个 arXiv 新公告批次为 owner 边界。旧报告枚举 337 个去重身份并保留 62 项，明显混入 VLA 局部方法、AI for Science、垂直 RAG、综述和局部 benchmark；本轮逐项题摘复筛并经独立 false-negative 回看后保留 13 个真正改变长期大模型/Infra 状态或控制边界的家族，49 个旧候选降为分母前关闭，入选 v1 未见 withdrawn。

关键增量是：MoE serving 的 route 必须连同 expert residency 与通信成本设计；diffusion LM 需要按迭代收敛而非 token 完成做连续批处理；低 batch tensor parallel 可以重新安排 collective 时点；KV 可被兼容 verifier 只读复用；RL post-training 的 rollout 与 update 资源可双向调度；自然语言 specification、Skill 逻辑关系和持久 Context 更新都必须把“模型提出”与“可验证提交”分开。4 项沿用既有正文，9 项新增机制已经写入对应 owner，并完成非作者逐项语义复核。

## 2. 来源覆盖

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | 历史生效边界晚于本窗 | 不适用 | 无 |
| SRC-ANTHROPIC | 历史生效边界晚于本窗 | 不适用 | 无 |
| SRC-GOOGLE-AI | 历史生效边界晚于本窗 | 不适用 | 无 |
| SRC-META-AI | 历史生效边界晚于本窗 | 不适用 | 无 |
| SRC-QWEN | 历史生效边界晚于本窗 | 不适用 | 无 |
| SRC-DEEPSEEK | 历史生效边界晚于本窗 | 不适用 | 无 |
| SRC-MOONSHOT | 历史生效边界晚于本窗 | 不适用 | 无 |
| SRC-TENCENT-HUNYUAN | 历史生效边界晚于本窗 | 不适用 | 无 |
| SRC-ZAI | 历史生效边界晚于本窗 | 不适用 | 无 |
| SRC-BYTEDANCE-SEED | 历史生效边界晚于本窗 | 不适用 | 无 |
| SRC-BAIDU-ERNIE | 历史生效边界晚于本窗 | 不适用 | 无 |
| SRC-XIAOMI-MIMO | 历史生效边界晚于本窗 | 不适用 | 无 |
| SRC-MINIMAX | 历史生效边界晚于本窗 | 不适用 | 无 |
| SRC-ARXIV | 官方新公告；337 个去重身份完成全标题巡检与含糊/高信号完整摘要筛选，并经独立 false-negative 回看恢复 3 项，13 项入选 | 已检查 | 无 |

分母前关闭包括 TSRouter、SeedSmith、OpenProver、Toward Auditable AI Scientists、临床 RAG、LionVote 的 CIFAR/ViT 局部证据和多项 VLA 架构变体；这些材料不因能映射 ROADMAP 名词而自动获得候选身份。

## 3. 候选与判断

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [Sticky Routing](https://arxiv.org/html/2607.08780v1) | 2026-07-13T08:00:00+08:00 ～ 2026-07-13T09:00:00+08:00 | 训练路由连续性以降低 expert weight churn，连接模型路由与 runtime residency；3 + 3 + 3 = 9 | 深入完成 | 整合：MODEL-MOE，[Ch21](../../../../books/part-02-model/21-moe.md) |
| [Director](https://arxiv.org/html/2607.08782v1) | 2026-07-13T08:00:00+08:00 ～ 2026-07-13T09:00:00+08:00 | 在线预测后续 expert demand 并主动 placement，改变 distributed MoE 调度闭环；3 + 3 + 3 = 9 | 深入完成 | 整合：INFER-SCHEDULING，[Ch56](../../../../books/part-05-inference-system/56-inference-scheduling.md) |
| [BlockServe](https://arxiv.org/html/2607.08930v1) | 2026-07-13T08:00:00+08:00 ～ 2026-07-13T09:00:00+08:00 | 按 diffusion block 的异质收敛进度做连续批处理；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：INFER-CONTINUOUS-BATCHING，[Ch46](../../../../books/part-05-inference-system/46-continuous-batching.md) |
| [NL-PAC](https://arxiv.org/html/2607.08961v1) | 2026-07-13T08:00:00+08:00 ～ 2026-07-13T09:00:00+08:00 | 把自然语言规格歧义与监督通道不可辨识性分开，并给出不能靠增加同源标签消除的风险下界；3 + 3 + 3 = 9 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [SiFAR](https://arxiv.org/html/2607.08973v1) | 2026-07-13T08:00:00+08:00 ～ 2026-07-13T09:00:00+08:00 | 在低 batch speculate/verify 中重排 All-Reduce 同步点；3 + 3 + 2 = 8 | 深入完成 | 已有覆盖：INFER-TENSORRT-LLM，[Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md) |
| [StreamDQ](https://arxiv.org/html/2607.08993v1) | 2026-07-13T08:00:00+08:00 ～ 2026-07-13T09:00:00+08:00 | 把权重解量化移到近 HBM 数据路径，改变压缩收益的 data-movement 归属；3 + 3 + 3 = 9 | 深入完成 | 整合：INFER-TENSORRT-LLM，[Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md) |
| [SLBench](https://arxiv.org/html/2607.09016v1) | 2026-07-13T08:00:00+08:00 ～ 2026-07-13T09:00:00+08:00 | 把 Skill 中 precondition、constraint、fallback 等逻辑关系编译为可执行测试并区分 artifact、adoption 与 outcome；2 + 3 + 3 = 8 | 深入完成 | 已有覆盖：AGENT-PLATFORM，[Ch84](../../../../books/part-07-agent/84-agent-platform.md) |
| [KV-PRM](https://arxiv.org/html/2607.09153v1) | 2026-07-13T08:00:00+08:00 ～ 2026-07-13T09:00:00+08:00 | 让兼容 verifier 对 generation KV 做只读 score readout，避免重复 prefill；2 + 3 + 3 = 8 | 深入完成 | 已有覆盖：INFER-KV-CACHE，[Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) |
| [Scoped Verification](https://arxiv.org/html/2607.09175v1) | 2026-07-13T08:00:00+08:00 ～ 2026-07-13T09:00:00+08:00 | 用 typed graph 承担持久 instruction 的局部更新与结构验证，再重建带版本的文本 checkpoint；3 + 2 + 3 = 8 | 深入完成 | 整合：AGENT-CONTEXT，[Ch75](../../../../books/part-07-agent/75-context.md) |
| [Bidirectional Resource Scheduling for Disaggregated and Asynchronous RL Post-Training](https://arxiv.org/html/2607.09207v1) | 2026-07-13T08:00:00+08:00 ～ 2026-07-13T09:00:00+08:00 | 让 rollout 与 update 资源池按 backlog 双向迁移；3 + 3 + 3 = 9 | 深入完成 | 整合：TRAIN-DISTRIBUTED-TRAINING，[Ch36](../../../../books/part-04-training-system/36-distributed-training.md) |
| [WildTrace](https://arxiv.org/html/2607.09328v1) | 2026-07-13T08:00:00+08:00 ～ 2026-07-13T09:00:00+08:00 | 把长上下文答案与自然 evidence trail 同时纳入评测；2 + 2 + 3 = 7 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Shared Selective Persistent Memory](https://arxiv.org/html/2607.09493v1) | 2026-07-13T08:00:00+08:00 ～ 2026-07-13T09:00:00+08:00 | 为共享记忆增加选择性写入与 RBAC，而不是把所有观察并入共同真相；3 + 3 + 3 = 9 | 深入完成 | 整合：AGENT-MEMORY，[Ch77](../../../../books/part-07-agent/77-memory.md) |
| [Failure as a Process](https://arxiv.org/html/2607.09510v1) | 2026-07-13T08:00:00+08:00 ～ 2026-07-13T09:00:00+08:00 | 将 CLI coding-agent 失败定位到 trajectory stage，而非只看终局失败；2 + 3 + 3 = 8 | 深入完成 | 整合：PLATFORM-TRACE，[Ch69](../../../../books/part-06-ai-infrastructure/69-trace.md) |

## 4. 证据与知识整合

### [Sticky Routing](https://arxiv.org/html/2607.08780v1)
exact v1 将相邻 token 的 expert route 稳定性纳入训练目标，实验只覆盖作者模型/硬件，不能证明任意拓扑收益。Ch21 可在“路由质量不等于部署局部性”后加入：router 也可优化 residency continuity，但需付出负载均衡和 specialization 约束。

**Evidence Review 细节。**
- **机制与状态边界：** A differentiable consistency loss penalizes abrupt top-k expert changes between adjacent semantically coherent tokens; no expert architecture change is required, but the learned router now carries an inference-locality objective.
- **证据证明什么：** The reported models show that router-switch regularization can improve expert locality while retaining the evaluated quality envelope.
- **证据没有证明什么：** The paper does not establish the same benefit for large production MoEs, arbitrary tokenization, expert-parallel clusters, or workloads whose optimal experts change rapidly.
- **证据定位：** Method / identity：https://arxiv.org/html/2607.08780v1#S4; https://arxiv.org/html/2607.08780v1#S4.SS5。Evaluation：https://arxiv.org/html/2607.08780v1#S5; https://arxiv.org/html/2607.08780v1#S5.SS6。Limitations / counterevidence：https://arxiv.org/html/2607.08780v1#S6; https://arxiv.org/html/2607.08780v1#A4。
- **取舍与回退：** Locality reduces weight movement but constrains conditional capacity and adds a training hyperparameter; excessive stickiness may keep tokens on a suboptimal expert.

### [Director](https://arxiv.org/html/2607.08782v1)
方法以在线需求信号主动迁移 expert，收益受预测误差、迁移带宽和拓扑限制。Ch56 的 expert placement 段应补入预测—预取—观测—回退闭环，强调错误预置会放大尾延迟。

**Evidence Review 细节。**
- **机制与状态边界：** A reconfiguration manager predicts routing from queued requests; a relaxation-based optimizer computes a bounded placement; live migration overlaps expert movement with compute and limits downtime.
- **证据证明什么：** The prototype and approximation analysis support proactive placement under the paper's predicted-routing and migration model.
- **证据没有证明什么：** It does not prove robustness to adversarial prediction error, heterogeneous failure domains, cross-cluster migration, or production tail-SLO behavior.
- **证据定位：** Method / identity：https://arxiv.org/html/2607.08782v1#S4; https://arxiv.org/html/2607.08782v1#S5; https://arxiv.org/html/2607.08782v1#S6。Evaluation：https://arxiv.org/html/2607.08782v1#S7; https://arxiv.org/html/2607.08782v1#S8。Limitations / counterevidence：https://arxiv.org/html/2607.08782v1#S9。
- **取舍与回退：** Proactivity reduces expected communication imbalance but adds prediction error, optimization delay, migration bandwidth, placement-version state and rollback requirements.

### [BlockServe](https://arxiv.org/html/2607.08930v1)
论文把 diffusion LM 的 block 视为可独立推进但收敛时间不同的 work unit；作者 throughput 不外推到任意模型。Ch46 已区分 token completion 与 iterative convergence，并包含 block 级 admission/retirement。

**Evidence Review 细节。**
- **机制与状态边界：** Completed requests are evicted at block boundaries, heterogeneous denoising states are gathered into one dense layout, and token-budget admission refills capacity.
- **证据证明什么：** The paper reports throughput and capacity gains for two diffusion LMs under offline batching on one H200 while retaining its measured generation-quality envelope.
- **证据没有证明什么：** Online arrivals, production tail latency, fairness and multi-GPU behavior are explicitly outside the evaluation.
- **证据定位：** Method / identity：https://arxiv.org/html/2607.08930v1#S2。Evaluation：https://arxiv.org/html/2607.08930v1#S3。Limitations / counterevidence：https://arxiv.org/html/2607.08930v1#S5。
- **取舍与回退：** Smaller blocks reclaim slots sooner but add scheduling/denoising overhead; mixed-state metadata and approximate parallel decoding enlarge correctness and quality risk.

### [NL-PAC](https://arxiv.org/html/2607.08961v1)
exact v1 把模型、prompt、threshold 与输入分布固定成被审计 tuple，并证明 target-blind supervision 下存在与样本数无关的 minimax risk floor；增加同一盲通道的标签只能降低 sampling error，不能识别究竟采用了哪种解释。Qwen 2.5-3B 的单一 prompt 正证书、paraphrase 零证书和 bridge audit 只支持 model-relative ambiguity，不证明人类语义歧义或跨模型常数。Ch66 应把 specification identity、supervision-channel observability 与外部 construct validation 加入 judge/evaluator contract；无法揭示目标解释时，系统应改变信息通道或 abstain，而不是继续堆同源样本。

**Evidence Review 细节。**
- **机制与状态边界：** NL-PAC separates task ambiguity, decoding randomness, target error and channel indistinguishability; the diameter of the pointwise-admissible target class yields a minimax risk floor under target-blind supervision.
- **证据证明什么：** Under the stated model-admissibility and target-blind channel assumptions, the paper proves a lower bound that additional ambiguous supervision cannot cross.
- **证据没有证明什么：** The floor is not a universal empirical hallucination rate and depends on the fixed model, thresholded decoding law and channel assumptions.
- **证据定位：** Method / identity：https://arxiv.org/html/2607.08961v1#S2; https://arxiv.org/html/2607.08961v1#S4。Evaluation：https://arxiv.org/html/2607.08961v1#S5; https://arxiv.org/html/2607.08961v1#A3。Limitations / counterevidence：https://arxiv.org/html/2607.08961v1#S6。
- **取舍与回退：** Auditing admissible readings exposes irreducible ambiguity, but requires extra sampling and a declared supervision channel; changing the specification or collecting disambiguating evidence may be cheaper.

### [SiFAR](https://arxiv.org/html/2607.08973v1)
作者在 8×H200/NVSwitch、低 batch 条件重排通信并报告吞吐收益；不证明跨节点或高 batch。Ch49 已将同步消除写成 execution-plan 分支，并保留 topology/batch breakeven。

**Evidence Review 细节。**
- **机制与状态边界：** SiFAR uses dual buffers to remove one reuse barrier, switch-assisted redundant pull to reduce transfer work, and speculative result fetch followed by a compact validation flag and retry path.
- **证据证明什么：** Under the evaluated low-batch H200 configurations, the protocol reduces collective latency and improves end-to-end token throughput relative to the reported baselines.
- **证据没有证明什么：** It does not establish correctness or benefit across arbitrary fabrics, imbalance, process failure, larger asynchronous jobs or conventional unfused serving engines.
- **证据定位：** Method / identity：https://arxiv.org/html/2607.08973v1#S3; https://arxiv.org/html/2607.08973v1#S4.SS2。Evaluation：https://arxiv.org/html/2607.08973v1#S5; https://arxiv.org/html/2607.08973v1#S6。Limitations / counterevidence：https://arxiv.org/html/2607.08973v1#S2.SS5; https://arxiv.org/html/2607.08973v1#S9。
- **取舍与回退：** Removing expected barriers adds buffer-generation state, speculative validation and retry; standard collectives remain safer when topology support or progress assumptions do not hold.

### [StreamDQ](https://arxiv.org/html/2607.08993v1)
论文把压缩权重在 HBM 附近流式解量化，减少送往 compute 的字节；这是定制存储路径而非普通 GPU 软件等价物。Ch49 应在量化执行链加入“compressed residency → near-memory expansion → compute”分支，并保留硬件耦合代价。

**Evidence Review 细节。**
- **机制与状态边界：** DeQuantization Blocks in the HBM base die transform tagged quantized loads on the fly while preserving GPU load semantics; sideband metadata selects format and parameters.
- **证据证明什么：** The simulator supports architectural feasibility and projected benefits within its modeled HBM area, power, thermal and workload assumptions.
- **证据没有证明什么：** Simulation does not prove realized silicon timing, manufacturability, vendor adoption, or gains for small-batch memory-bound decode.
- **证据定位：** Method / identity：https://arxiv.org/html/2607.08993v1#S3; https://arxiv.org/html/2607.08993v1#S3.SS4。Evaluation：https://arxiv.org/html/2607.08993v1#S5; https://arxiv.org/html/2607.08993v1#S6。Limitations / counterevidence：https://arxiv.org/html/2607.08993v1#S7; https://arxiv.org/html/2607.08993v1#S8。
- **取舍与回退：** Near-memory execution removes GPU instructions and traffic but fixes new logic, metadata and supported quantization formats into the memory interface.

### [SLBench](https://arxiv.org/html/2607.09016v1)
exact v1 从公开 Skill 中抽取八类逻辑关系，并把高置信、高影响、可本地执行的关系编译为 86 个测试；测试同时观察 deterministic unsafe signal、Agent 是否遵循关系以及最终结果。作者六组 backbone、有限公开 Skill snapshot 与 12 项人工 clarification audit 不能证明通用 unsafe rate，也不能把 SLGuard 的相对降低外推到任意 Agent。Ch84 已要求 Skill 声明输入、权限、可写状态、终止条件和 verifier，并把 artifact quality、trajectory adoption 与 executable outcome 分层，因此本 family 作为现有命题的受限验证，不重复新增合同。

**Evidence Review 细节。**
- **机制与状态边界：** SkillLogic extracts eight relation types and test hooks from skill files; SLBench turns source-grounded, high-impact relations into executable local cases; SLGuard adds a targeted inference-time scaffold.
- **证据证明什么：** Across 86 audited cases, tested agents frequently violate logical relations and the targeted scaffold reduces violations in that controlled suite.
- **证据没有证明什么：** The 5,000-skill discovery corpus and two agent implementations do not establish a population rate for all skills or production safety.
- **证据定位：** Method / identity：https://arxiv.org/html/2607.09016v1#S3。Evaluation：https://arxiv.org/html/2607.09016v1#S3.SS3; https://arxiv.org/html/2607.09016v1#S4。Limitations / counterevidence：https://arxiv.org/html/2607.09016v1#S5; https://arxiv.org/html/2607.09016v1#Sx1。
- **取舍与回退：** Executable relation tests improve release evidence but require local fixtures, deterministic graders and maintenance as tools and skill semantics evolve.

### [KV-PRM](https://arxiv.org/html/2607.09153v1)
只有 tokenizer、位置和层状态兼容时，PRM 才能读取生成 KV；它不是任意模型间 transferable cache。Ch45 已把该用法归为受类型约束的只读派生视图。

**Evidence Review 细节。**
- **机制与状态边界：** KV-PRM swaps to a LoRA reward head on the compatible generator, appends one verify token, reads the existing K/V and maps next-token logits to a score; a preliminary branch differentiates through KV but is not part of the established read-only scoring claim.
- **证据证明什么：** For the evaluated compatible generators and reward heads, single-token KV readout reduces scorer compute/latency while preserving or improving the measured search outcome relative to text re-encoding.
- **证据没有证明什么：** The theoretical richness assumptions do not guarantee calibrated or independent verification, and the design does not transfer across incompatible models or discarded/stale caches.
- **证据定位：** Method / identity：https://arxiv.org/html/2607.09153v1#S3; https://arxiv.org/html/2607.09153v1#S4。Evaluation：https://arxiv.org/html/2607.09153v1#S5.SS2; https://arxiv.org/html/2607.09153v1#S6。Limitations / counterevidence：https://arxiv.org/html/2607.09153v1#S8。
- **取舍与回退：** State reuse removes redundant prefill but extends cache lifetime and trust scope, couples verifier deployment to model layout and risks shared blind spots.

### [Scoped Verification](https://arxiv.org/html/2607.09175v1)
GRACE 把持久 instruction 拆为 typed nodes/relations，LLM 只提出受 schema 约束的局部 edit；系统在 touched neighborhood 做结构验证、合并重叠内容，再从接受后的 graph delta 重建 deployed text checkpoint。十批 distribution shift、单一 telecom domain 与五次重复只说明 graph locality 加 consolidation 在该 harness 中优于 flat rewrite；LLM judge 的 contradiction audit 是相关证据，不证明图本身正确或跨域稳定。Ch75 应把 instruction evolution 写成 `versioned source → local proposal → schema/consistency validation → delta reconstruction → checkpoint commit/rollback`，保留短、稳定 instruction 直接人工编辑的低成本分支。

**Evidence Review 细节。**
- **机制与状态边界：** GRACE parses persistent system instructions into atomic typed graph nodes, applies schema-constrained edits, validates affected typed neighbourhoods, consolidates accumulated state and reconstructs the next textual checkpoint for inference.
- **证据证明什么：** Under a ten-batch controlled telecom shift with fixed model, tools and harness, graph-scoped validation plus active consolidation preserves later-checkpoint improvement better than the reported flat-text controls.
- **证据没有证明什么：** The evidence is domain- and harness-specific and does not establish that graph representation is always cheaper or safer than replay, retrieval or immutable prompt versioning.
- **证据定位：** Method / identity：https://arxiv.org/html/2607.09175v1#S4; https://arxiv.org/html/2607.09175v1#S4.SS3。Evaluation：https://arxiv.org/html/2607.09175v1#S5; https://arxiv.org/html/2607.09175v1#S5.SS2。Limitations / counterevidence：https://arxiv.org/html/2607.09175v1#S6。
- **取舍与回退：** Typed state improves provenance and local checks but adds parsing errors, schema evolution, graph/text divergence and consolidation policy risk.

### [Bidirectional Resource Scheduling for Disaggregated and Asynchronous RL Post-Training](https://arxiv.org/html/2607.09207v1)
论文按 rollout/update backlog 在异步阶段间迁移资源，作者实验不证明真实多租户抢占成本。Ch36 应在异步 post-training pipeline 中加入双向弹性、state drain 和 staleness 上限。

**Evidence Review 细节。**
- **机制与状态边界：** BiDiRL chooses a hot-switch-compatible resource envelope with stage-time models, then uses online profiling and bidirectional borrowing so trainers can occupy rollout GPUs and rollouters can occupy training GPUs without a full job restart.
- **证据证明什么：** Across the reported 8-32 GPU experiments, 2B-8B models and stated staleness bounds, role borrowing can reclaim measured bubbles without logically merging rollout and optimizer stages.
- **证据没有证明什么：** The speedup is workload-dependent, requires observed idle windows, and does not establish robustness to failures, arbitrary model layouts, larger fleets or different RL algorithms.
- **证据定位：** Method / identity：https://arxiv.org/html/2607.09207v1#S3.SS1; https://arxiv.org/html/2607.09207v1#S4。Evaluation：https://arxiv.org/html/2607.09207v1#S7; https://arxiv.org/html/2607.09207v1#S7.SS1。Limitations / counterevidence：https://arxiv.org/html/2607.09207v1#S8。
- **取舍与回退：** Higher utilization adds hot-switch state, layout compatibility constraints, online profiling error, admission complexity and new interference/failure domains.

### [WildTrace](https://arxiv.org/html/2607.09328v1)
其 evidence trail 评测要求答案引用长上下文内真实证据链，但仍依赖数据构造和 evaluator。Ch66 应在长上下文 slice 中增加 evidence localization、coverage 与 final-answer correctness 的分离。

**Evidence Review 细节。**
- **机制与状态边界：** WildTrace curates naturally distributed evidence trails, labels forward, intersection, comparative, temporal and counterfactual geometry, and reports scale-tier curves plus source-cluster diagnostics.
- **证据证明什么：** The evaluated systems show graded, geometry-dependent degradation rather than one universal context cliff.
- **证据没有证明什么：** The benchmark does not isolate architectural causality or guarantee that its natural trails represent private enterprise corpora.
- **证据定位：** Method / identity：https://arxiv.org/html/2607.09328v1#S2; https://arxiv.org/html/2607.09328v1#S3.SS2。Evaluation：https://arxiv.org/html/2607.09328v1#A2。Limitations / counterevidence：https://arxiv.org/html/2607.09328v1#S4。
- **取舍与回退：** Natural evidence improves ecological validity but reduces experimental control and complicates attribution across source families.

### [Shared Selective Persistent Memory](https://arxiv.org/html/2607.09493v1)
共享 memory 的写入选择、作用域和 RBAC 是系统控制面，不由生成模型隐式决定。Ch77 应在 shared memory 段加入 writer identity、authorization、conflict 和 revocation contract。

**Evidence Review 细节。**
- **机制与状态边界：** A collaborative workspace extracts typed task specifications, data schemas, tool configuration and output constraints into shared selective memory, injects compact summaries at reuse time, and refreshes underlying data without replaying the construction trace.
- **证据证明什么：** In the reported recurring workspace tasks, selective persistent state improves completion and reuse while full-history persistence degrades completion relative to no memory.
- **证据没有证明什么：** The study does not establish universal memory schemas, privacy isolation, long-term consistency or that its large token-reduction figures preserve every task-relevant detail.
- **证据定位：** Method / identity：https://arxiv.org/html/2607.09493v1#S4; https://arxiv.org/html/2607.09493v1#S5。Evaluation：https://arxiv.org/html/2607.09493v1#S6; https://arxiv.org/html/2607.09493v1#S6.SS4。Limitations / counterevidence：https://arxiv.org/html/2607.09493v1#S7。
- **取舍与回退：** Selective memory reduces context cost and stale procedural noise but moves correctness into extraction, schema versioning, access control and deletion policy.

### [Failure as a Process](https://arxiv.org/html/2607.09510v1)
论文的 CLI trajectory taxonomy 能区分 perception、planning、action 与 recovery 失效，但仅支持所测 agent/task。Ch69 应在 trace attribution 后加入 stage-aware failure evidence 与终局结果的非等价关系。

**Evidence Review 细节。**
- **机制与状态边界：** The study normalizes CLI traces and annotates three timestamps per failed run: the error that determines failure, the point after which no recovery is observed, and the first externally visible symptom; distributions are compared across scaffolds and models.
- **证据证明什么：** In this corpus, decisive errors often precede lock-in and visible failure by several actions, revealing a measurable recovery interval hidden by terminal labels.
- **证据没有证明什么：** Retrospective labels do not prove causal interventions would recover the run, and CLI coding tasks do not represent every agent environment.
- **证据定位：** Method / identity：https://arxiv.org/html/2607.09510v1#S2.SS5。Evaluation：https://arxiv.org/html/2607.09510v1#S3; https://arxiv.org/html/2607.09510v1#S3.SS1。Limitations / counterevidence：https://arxiv.org/html/2607.09510v1#S4.SS1。
- **取舍与回退：** Process-level observability enables earlier recovery policies but requires normalized event schemas, expensive annotation and careful separation of hindsight judgment from online signals.

## 5. 缺口与下一步

无

无材料请求。9 项新增机制均已写入正文：`2607.08780` 位于 Ch21“Router 连续性必须与 Expert Residency 共同设计”；`2607.08782` 位于 Ch56“Expert Residency Controller 只能优化 Placement，不能重写 Router”；`2607.08961` 与 `2607.09328` 分别位于 Ch66“监督通道本身可能存在不可消除的识别盲区”和“Evidence Trail 与最终答案必须分别验收”；`2607.08993` 位于 Ch49“Execution Plan 必须联合逻辑稀疏、Tensor Lifetime 与硬件数据流”；`2607.09175` 位于 Ch75“持久 Instruction 更新应先修改 Typed State，再重建文本 View”；`2607.09207` 位于 Ch36“Rollout 与 Update Pool 的边界可以移动，但 Policy Identity 不能漂移”；`2607.09493` 位于 Ch77“共享 Memory 需要分离选择性写入、访问权与事实状态”；`2607.09510` 位于 Ch69“Failure Attribution 必须从阶段定位升级到可证伪的因果候选”。BlockServe、SiFAR、SLBench 与 KV-PRM 的既有正文覆盖保持不变。

## 6. 复核

复核者：`/root/aug01_10`（Books 写后非作者独立复核；准入复核沿用 `/root/aug21_31`）

结论：通过

13 项的 first-public、withdrawn 状态、owner 与证据边界沿用已通过的准入复核。本轮不以 source marker 或 Review note 代替吸收，而是逐项检查 9 个新增 family 的机制正文：Ch21 的 route continuity/residency 分权，Ch56 的 demand prediction 与 SLO guard，Ch49 的 near-HBM dequantization，Ch75 的 typed instruction graph，Ch36 的 rollout/update 双向迁移与 policy identity，Ch66 的 specification identifiability 与 evidence-trail 双验收，Ch77 的 selective write/RBAC/belief state，以及 Ch69 的 stage-aware failure attribution。各段均保留旧路径、证据未证明范围、代价或回退，并与相邻段落职责一致；其余 4 项确由既有正文承载。机器校验另行通过，因此本日报闭环。
