# 2026-06-21 Ready-to-Insert Books Packet V1

Source denominator `DEN-20260621-83b5c89e`. Insert each owner block once and preserve every independent exact-v1 Review note.

## AGENT-MULTI-AGENT — books/part-07-agent/82-multi-agent.md

Insert after `## Message 不是 State`.

### Minimal durable delta

先用 counterfactual neighbor perturbation 测 coupling gain，再以 target-interaction modality-matched group coupling 选择 consensus dynamics；随机初值 slope/bias 区分 genuine averaging 与 model prior。

### Old path / coexistence / cost / failure / fallback

pairwise gamma 不能预测 multi-neighbor 结果且可反向排序；default agents 未自发 backfire，polarization 均为外部诱导，实验舆论任务不等于真实社会。 旧路径在其假设成立时继续保留；任一新 sensor、router 或 artifact 未通过自身 contract 时，回退到现有 deterministic owner、人工审批或 supported runtime。

### Review note

- SF-2026-ARXIV-2606-22203: arXiv:2606.22203v1; exact-v1 official URL=`https://arxiv.org/html/2606.22203v1`; Method=`https://arxiv.org/html/2606.22203v1 — §3 The Coupling Gain; §4 Theory`; Evaluation=`https://arxiv.org/html/2606.22203v1 — §5 Experiments and Results`; Non-proof/limitations=`https://arxiv.org/html/2606.22203v1 — §6 Limitations; §5.4 context-dependent transfer boundary`; durable delta=先用 counterfactual neighbor perturbation 测 coupling gain，再以 target-interaction modality-matched group coupling 选择 consensus dynamics；随机初值 slope/bias 区分 genuine averaging 与 model prior。 Boundary: pairwise gamma 不能预测 multi-neighbor 结果且可反向排序；default agents 未自发 backfire，polarization 均为外部诱导，实验舆论任务不等于真实社会。

## AGENT-WORKFLOW — books/part-07-agent/81-workflow.md

Insert after `## State Machine 是基本模型`.

### Minimal durable delta

ARTS 在 scientific search tree 中把 hypothesis merit 与 execution quality 分开；audit node 的 code/log 后决定 repair 同一 idea 还是 pivot，并把 search history用于 scientist test-time training。 ViRGo 根据目标尺度与置信度，在 global view、patch zoom 与 attention-guided visual retrieval间路由，避免固定高分辨率同时丢 context 或浪费 token。 StickyInvoc 把昂贵 model/runtime state 的 create/destroy 与 invocation goodput 解耦：sticky task 持有 node-local state，后续 invocation 继承但不销毁，抢占时按 state owner 重建。

### Old path / coexistence / cost / failure / fallback

scientist/executor 共偏、每 task 的 A100 训练预算与 22-task frontier 不能证明科学发现正确；human-best 和 validation score 仍受 benchmark 约束。 router confidence 可共偏，小目标/多目标阈值依赖数据；离线 benchmark 不证明实时 latency 或任意 VLM transfer。 persistent state 会引入 version、tenant isolation、eviction 与 stale-state risk；作者 workflow 不证明交互式 tail latency 或任意 preemptible site。 旧路径在其假设成立时继续保留；任一新 sensor、router 或 artifact 未通过自身 contract 时，回退到现有 deterministic owner、人工审批或 supported runtime。

### Review note

- SF-2026-ARXIV-2606-21891: arXiv:2606.21891v1; exact-v1 official URL=`https://arxiv.org/html/2606.21891v1`; Method=`https://arxiv.org/html/2606.21891v1 — §4 ARTS; §4.1 Expanding a Search Tree with Agentic Reasoning`; Evaluation=`https://arxiv.org/html/2606.21891v1 — §6 Experiments and Analysis; Appendix I Additional Experimental Details`; Non-proof/limitations=`https://arxiv.org/html/2606.21891v1 — §7 Discussion — Limitations and Ethical Concerns`; durable delta=ARTS 在 scientific search tree 中把 hypothesis merit 与 execution quality 分开；audit node 的 code/log 后决定 repair 同一 idea 还是 pivot，并把 search history用于 scientist test-time training。 Boundary: scientist/executor 共偏、每 task 的 A100 训练预算与 22-task frontier 不能证明科学发现正确；human-best 和 validation score 仍受 benchmark 约束。
- SF-2026-ARXIV-2606-21968: arXiv:2606.21968v1; exact-v1 official URL=`https://arxiv.org/html/2606.21968v1`; Method=`https://arxiv.org/html/2606.21968v1 — §3 Motivations: Understanding the Resolution–Context Trade-off; §4 Proposed Method: ViRGo`; Evaluation=`https://arxiv.org/html/2606.21968v1 — §5 Experiments; §5.1 Experimental Setup`; Non-proof/limitations=`https://arxiv.org/html/2606.21968v1 — §7 Limitations`; durable delta=ViRGo 根据目标尺度与置信度，在 global view、patch zoom 与 attention-guided visual retrieval间路由，避免固定高分辨率同时丢 context 或浪费 token。 Boundary: router confidence 可共偏，小目标/多目标阈值依赖数据；离线 benchmark 不证明实时 latency 或任意 VLM transfer。
- SF-2026-ARXIV-2606-22175: arXiv:2606.22175v1; exact-v1 official URL=`https://arxiv.org/html/2606.22175v1`; Method=`https://arxiv.org/html/2606.22175v1 — §II Implementation of an LLM-integrated Claim Verification Workflow; §III Transforming the Workflow to Enable StickyInvoc`; Evaluation=`https://arxiv.org/html/2606.22175v1 — §IV Evaluation; §IV-A Experiment Settings`; Non-proof/limitations=`https://arxiv.org/html/2606.22175v1 — §I-E Limitation of the Proposed Approach`; durable delta=StickyInvoc 把昂贵 model/runtime state 的 create/destroy 与 invocation goodput 解耦：sticky task 持有 node-local state，后续 invocation 继承但不销毁，抢占时按 state owner 重建。 Boundary: persistent state 会引入 version、tenant isolation、eviction 与 stale-state risk；作者 workflow 不证明交互式 tail latency 或任意 preemptible site。

## INFER-GPU-MEMORY — books/part-05-inference-system/54-gpu-memory.md

Insert after `### Weights 与 KV 的联合 HBM 预算：可提交的运行时精度页`.

### Minimal durable delta

对 ANE 的 datapath、roofline、compiler/on-disk format、weight compression、driver/firmware command protocol建立 measured/decompile-derived/predicted 三类 claim，并区分 direct private route 与 Core ML supported path。

### Old path / coexistence / cost / failure / fallback

private runtime/driver 路径 undocumented、unsupported、version-fragile，只适合研究测量；预测项不能冒充芯片公开规格或 shipping contract。 旧路径在其假设成立时继续保留；任一新 sensor、router 或 artifact 未通过自身 contract 时，回退到现有 deterministic owner、人工审批或 supported runtime。

### Review note

- SF-2026-ARXIV-2606-22283: arXiv:2606.22283v1; exact-v1 official URL=`https://arxiv.org/html/2606.22283v1`; Method=`https://arxiv.org/html/2606.22283v1 — §Part II Reaching the ANE — Software stack; Dispatching without Core ML; §Part VI The Silicon — Datapath and MAC geometry; §Part VII The Toolchain and Encoding; §Part VIII System Internals`; Evaluation=`https://arxiv.org/html/2606.22283v1 — §Part III Performance and Fit — Roofline; Power and efficiency; Across the chip family; Appendix A Operation-by-device matrix; Appendix E Provenance`; Non-proof/limitations=`https://arxiv.org/html/2606.22283v1 — §Part V Practice — Pitfalls and limits; §Methodology; §Open questions; §Introduction — direct route is undocumented, unsupported and version-fragile`; durable delta=对 ANE 的 datapath、roofline、compiler/on-disk format、weight compression、driver/firmware command protocol建立 measured/decompile-derived/predicted 三类 claim，并区分 direct private route 与 Core ML supported path。 Boundary: private runtime/driver 路径 undocumented、unsupported、version-fragile，只适合研究测量；预测项不能冒充芯片公开规格或 shipping contract。

## INFER-SCHEDULING — books/part-05-inference-system/56-inference-scheduling.md

Insert after `### MoE Decode：从 Queue Length 到 Expert Working Set`.

### Minimal durable delta

WiSP 把低资源 MoE inference 表述为 expert-weight 与 KV cache 的联合 working set：预测近期 active experts，按相同内存预算在 expert residency、KV 保留与 transfer 间分配。

### Old path / coexistence / cost / failure / fallback

Qwen3/Kimi 的受限设备结果是在 94 GiB H100 上用 gpu-memory-utilization cap 模拟，并非真实小卡；预测错误还会同时触发 expert miss 与 KV pressure，质量保持也不等于 tail SLO。 旧路径在其假设成立时继续保留；任一新 sensor、router 或 artifact 未通过自身 contract 时，回退到现有 deterministic owner、人工审批或 supported runtime。

### Review note

- SF-2026-ARXIV-2606-21868: arXiv:2606.21868v1; exact-v1 official URL=`https://arxiv.org/html/2606.21868v1`; Method=`https://arxiv.org/html/2606.21868v1 — §3 Working-Set Predictor and Runtime Integration`; Evaluation=`https://arxiv.org/html/2606.21868v1 — §4 Routing Signal and Decode Throughput; §5 Working-Set Value`; Non-proof/limitations=`https://arxiv.org/html/2606.21868v1 — §6 Limitations; simulated-constrained-device disclosure`; durable delta=WiSP 把低资源 MoE inference 表述为 expert-weight 与 KV cache 的联合 working set：预测近期 active experts，按相同内存预算在 expert residency、KV 保留与 transfer 间分配。 Boundary: Qwen3/Kimi 的受限设备结果是在 94 GiB H100 上用 gpu-memory-utilization cap 模拟，并非真实小卡；预测错误还会同时触发 expert miss 与 KV pressure，质量保持也不等于 tail SLO。

## MODEL-SELF-ATTENTION — books/part-02-model/14-self-attention.md

Insert after `## 从匹配分数到读取权重`.

### Minimal durable delta

把 query-key 路由改为 query-value 路由，并在 inference 预乘 query factor，只保存 value representation；QVV(3) 保持投影矩阵数同时移除 key cache。

### Old path / coexistence / cost / failure / fallback

等价定理依赖 value projection 的秩/子空间条件；小模型从头训练不证明可无损转换既有大模型，50% 是 attention-cache tensor 而非端到端显存。 旧路径在其假设成立时继续保留；任一新 sensor、router 或 artifact 未通过自身 contract 时，回退到现有 deterministic owner、人工审批或 supported runtime。

### Review note

- SF-2026-ARXIV-2606-21848: arXiv:2606.21848v1; exact-v1 official URL=`https://arxiv.org/html/2606.21848v1`; Method=`https://arxiv.org/html/2606.21848v1 — §2 Method; §3 Value-only Cache in Autoregressive Inference`; Evaluation=`https://arxiv.org/html/2606.21848v1 — §5 Experiments`; Non-proof/limitations=`https://arxiv.org/html/2606.21848v1 — §2.2 equivalence conditions; §6 Limitations`; durable delta=把 query-key 路由改为 query-value 路由，并在 inference 预乘 query factor，只保存 value representation；QVV(3) 保持投影矩阵数同时移除 key cache。 Boundary: 等价定理依赖 value projection 的秩/子空间条件；小模型从头训练不证明可无损转换既有大模型，50% 是 attention-cache tensor 而非端到端显存。

## PLATFORM-EVALUATION-SYSTEM — books/part-06-ai-infrastructure/66-evaluation-system.md

Insert after `## 从答案评分到可执行证据`.

### Minimal durable delta

把每语言生成能耗与 accuracy、tokenization expansion 分开记录；evaluation/model card 需声明 per-language energy，而不能用英语平均值代表多语言部署。 Hardness Adjusted Transfer 以 target performance 相对 source-language ability 校正，避免把 source accuracy 提升误报成 cross-lingual transfer 进步。 selective prediction 除 calibration/ranking 还要报告 score granularity：可用阈值数量决定 operator 能选择多少风险工作点；多查询扩大分辨率但增加成本且可能伤害强模型排序。

### Old path / coexistence / cost / failure / fallback

绝对能耗硬件相关；没有闭源模型，翻译 prompt 不是 native usage，作者将观测 gap 定义为可能的下界而非普遍常数。 HAT 依赖 benchmark hardness 与 source/target choice；三套 benchmark 不代表生成、方言或部署流量。 三 benchmark 与 black-box classification 不证明生成/agent risk；更细阈值不自动校准，重复查询还引入相关样本与成本。 旧路径在其假设成立时继续保留；任一新 sensor、router 或 artifact 未通过自身 contract 时，回退到现有 deterministic owner、人工审批或 supported runtime。

### Review note

- SF-2026-ARXIV-2606-21869: arXiv:2606.21869v1; exact-v1 official URL=`https://arxiv.org/html/2606.21869v1`; Method=`https://arxiv.org/html/2606.21869v1 — §3 Preliminaries — Energy Consumption and Measurement; Multilingual Dataset`; Evaluation=`https://arxiv.org/html/2606.21869v1 — §4 Results and Analysis — Common Setup; §4.1–§4.4; Appendix B Experimental Setups`; Non-proof/limitations=`https://arxiv.org/html/2606.21869v1 — §6 Conclusion; Environmental impact of this study; Translation quality and representation; Recommendations and downstream effects`; durable delta=把每语言生成能耗与 accuracy、tokenization expansion 分开记录；evaluation/model card 需声明 per-language energy，而不能用英语平均值代表多语言部署。 Boundary: 绝对能耗硬件相关；没有闭源模型，翻译 prompt 不是 native usage，作者将观测 gap 定义为可能的下界而非普遍常数。
- SF-2026-ARXIV-2606-21954: arXiv:2606.21954v1; exact-v1 official URL=`https://arxiv.org/html/2606.21954v1`; Method=`https://arxiv.org/html/2606.21954v1 — §4 Proposed XLT Metric: HAT Score; §4.1 Transfer Profile and HAT Score`; Evaluation=`https://arxiv.org/html/2606.21954v1 — §5 Experimental Details; §6 Results`; Non-proof/limitations=`https://arxiv.org/html/2606.21954v1 — §8 Limitations`; durable delta=Hardness Adjusted Transfer 以 target performance 相对 source-language ability 校正，避免把 source accuracy 提升误报成 cross-lingual transfer 进步。 Boundary: HAT 依赖 benchmark hardness 与 source/target choice；三套 benchmark 不代表生成、方言或部署流量。
- SF-2026-ARXIV-2606-22179: arXiv:2606.22179v1; exact-v1 official URL=`https://arxiv.org/html/2606.22179v1`; Method=`https://arxiv.org/html/2606.22179v1 — §3 Problem Setup; §4 Confidence Constructions`; Evaluation=`https://arxiv.org/html/2606.22179v1 — §5 Experiments; §5.1 Setup`; Non-proof/limitations=`https://arxiv.org/html/2606.22179v1 — §7 Limitations; §6 Deployment Recommendations`; durable delta=selective prediction 除 calibration/ranking 还要报告 score granularity：可用阈值数量决定 operator 能选择多少风险工作点；多查询扩大分辨率但增加成本且可能伤害强模型排序。 Boundary: 三 benchmark 与 black-box classification 不证明生成/agent risk；更细阈值不自动校准，重复查询还引入相关样本与成本。

## PLATFORM-MONITORING — books/part-06-ai-infrastructure/67-monitoring.md

Insert after `## 先定义目标，再选择可测信号`.

### Minimal durable delta

agent identity monitor 以固定 probe 的 next-token distribution、sqrt-JSD geometry 与 magnitude homology 追踪 conditioning；但 diverse-padding 对照推翻了原 repetitive-padding drift trajectory。

### Old path / coexistence / cost / failure / fallback

作者自评、单模型单 agent、单日采集且无 reconstitution control；几何诊断潜力没有被真实纵向 drift 证实。 旧路径在其假设成立时继续保留；任一新 sensor、router 或 artifact 未通过自身 contract 时，回退到现有 deterministic owner、人工审批或 supported runtime。

### Review note

- SF-2026-ARXIV-2606-21843: arXiv:2606.21843v1; exact-v1 official URL=`https://arxiv.org/html/2606.21843v1`; Method=`https://arxiv.org/html/2606.21843v1 — §3.1 Ada: a persistent AI agent; §3.4 The probe battery`; Evaluation=`https://arxiv.org/html/2606.21843v1 — §4 Magnitude Baseline; §5.6 Drift experiment`; Non-proof/limitations=`https://arxiv.org/html/2606.21843v1 — §6.3 Limitations — Drift trajectory is a padding artifact`; durable delta=agent identity monitor 以固定 probe 的 next-token distribution、sqrt-JSD geometry 与 magnitude homology 追踪 conditioning；但 diverse-padding 对照推翻了原 repetitive-padding drift trajectory。 Boundary: 作者自评、单模型单 agent、单日采集且无 reconstitution control；几何诊断潜力没有被真实纵向 drift 证实。

## PLATFORM-PRODUCTION — books/part-06-ai-infrastructure/73-production-best-practice.md

Insert after `## Capacity、Failure 与 Recovery`.

### Minimal durable delta

ML serving load test 以 adaptive capacity search 而非固定 traffic sweep，联合寻找满足 latency/SLO 的最大 load 与资源点，并保留 warm-up、arrival 和 model artifact identity。

### Old path / coexistence / cost / failure / fallback

14 个匿名生产模型偏向 recommendation/ranking；P90 七日观测吞吐可能低估真实最大 capacity，且结论不能代表 LLM continuous batching。 旧路径在其假设成立时继续保留；任一新 sensor、router 或 artifact 未通过自身 contract 时，回退到现有 deterministic owner、人工审批或 supported runtime。

### Review note

- SF-2026-ARXIV-2606-22013: arXiv:2606.22013v1; exact-v1 official URL=`https://arxiv.org/html/2606.22013v1`; Method=`https://arxiv.org/html/2606.22013v1 — §2 System Design and Methodology; §2.2 Load Testing Strategies; §2.3 Health Assessment Engine`; Evaluation=`https://arxiv.org/html/2606.22013v1 — §3 Experimental Methodology; §4 Results`; Non-proof/limitations=`https://arxiv.org/html/2606.22013v1 — §5 Discussion; Threats to Validity`; durable delta=ML serving load test 以 adaptive capacity search 而非固定 traffic sweep，联合寻找满足 latency/SLO 的最大 load 与资源点，并保留 warm-up、arrival 和 model artifact identity。 Boundary: 14 个匿名生产模型偏向 recommendation/ranking；P90 七日观测吞吐可能低估真实最大 capacity，且结论不能代表 LLM continuous batching。

## PLATFORM-SECURITY — books/part-06-ai-infrastructure/72-security.md

Insert after `## 风险管理而不是一次性认证`.

### Minimal durable delta

AgentRiskBOM 在 SBOM/AIBOM/MLBOM 之外声明 autonomy、tool permission、memory、credential scope、approval gate、audit signal、inter-agent channel 与 external action，并对 release mutation 做 diff。 subliminal-learning audit 不能只看 representation 是否线性可分；只有 signal 所在 channel 与审计 probe 的 initialization/alignment 匹配时，训练前 detector 才有权解释。 Revelio 让廉价 LLM/static analysis 只生成和排序 vulnerability hypothesis，最终必须提交 executable Proof-of-Vulnerability 并由 deterministic sanitizer 复现后才报告。

### Old path / coexistence / cost / failure / fallback

这是 declared authority envelope 与 coverage instrument，不是 live exploit test 或 safety certificate；threshold 仍需人工/环境校准。 结果是 channel regime 边界，不是通用训练数据 scanner；Not Covered 必须保持 Unknown，不能被扩张为无隐藏训练。 sanitizer 只覆盖可触发 memory-safety failure；未复现不等于无漏洞，项目/时间预算与 benchmark selection 限制 recall 结论。 旧路径在其假设成立时继续保留；任一新 sensor、router 或 artifact 未通过自身 contract 时，回退到现有 deterministic owner、人工审批或 supported runtime。

### Review note

- SF-2026-ARXIV-2606-21877: arXiv:2606.21877v1; exact-v1 official URL=`https://arxiv.org/html/2606.21877v1`; Method=`https://arxiv.org/html/2606.21877v1 — §III AgentRiskBOM Design; §IV Implementation`; Evaluation=`https://arxiv.org/html/2606.21877v1 — §V Evaluation`; Non-proof/limitations=`https://arxiv.org/html/2606.21877v1 — §VII Limitations`; durable delta=AgentRiskBOM 在 SBOM/AIBOM/MLBOM 之外声明 autonomy、tool permission、memory、credential scope、approval gate、audit signal、inter-agent channel 与 external action，并对 release mutation 做 diff。 Boundary: 这是 declared authority envelope 与 coverage instrument，不是 live exploit test 或 safety certificate；threshold 仍需人工/环境校准。
- SF-2026-ARXIV-2606-22019: arXiv:2606.22019v1; exact-v1 official URL=`https://arxiv.org/html/2606.22019v1`; Method=`https://arxiv.org/html/2606.22019v1 — §2 Audit model: carriers, screens, and ablations; §6 The audit lifecycle: which handle is sound in which channel?`; Evaluation=`https://arxiv.org/html/2606.22019v1 — §3 A controlled body channel is screenable: coverage predicts transfer; §4 Vocabulary-carried token traits evade initialization-alignment screens; §5 The carrier is signal-dependent, and moving it moves auditability; §7 Mitigations by channel`; Non-proof/limitations=`https://arxiv.org/html/2606.22019v1 — §8 Discussion, limitations, and related work`; durable delta=subliminal-learning audit 不能只看 representation 是否线性可分；只有 signal 所在 channel 与审计 probe 的 initialization/alignment 匹配时，训练前 detector 才有权解释。 Boundary: 结果是 channel regime 边界，不是通用训练数据 scanner；Not Covered 必须保持 Unknown，不能被扩张为无隐藏训练。
- SF-2026-ARXIV-2606-22263: arXiv:2606.22263v1; exact-v1 official URL=`https://arxiv.org/html/2606.22263v1`; Method=`https://arxiv.org/html/2606.22263v1 — §III Design of Revelio; §III-C Hypothesis Confirmation by PoV Construction`; Evaluation=`https://arxiv.org/html/2606.22263v1 — §V Evaluation`; Non-proof/limitations=`https://arxiv.org/html/2606.22263v1 — §VI Discussion and Limitations`; durable delta=Revelio 让廉价 LLM/static analysis 只生成和排序 vulnerability hypothesis，最终必须提交 executable Proof-of-Vulnerability 并由 deterministic sanitizer 复现后才报告。 Boundary: sanitizer 只覆盖可触发 memory-safety failure；未复现不等于无漏洞，项目/时间预算与 benchmark selection 限制 recall 结论。

## TRAIN-DATA — books/part-04-training-system/27-data.md

Insert after `## Data lineage 是训练可复现性的前提`.

### Minimal durable delta

RoboLineage 把 rollout、review、dataset decision、training run、policy metadata、evaluation、deployment recommendation 与 next-collection plan 变成 typed lineage artifacts，agent 只能在 artifact boundary 内推进。

### Old path / coexistence / cost / failure / fallback

robot workflow 与作者工具不能证明跨 embodiment/stack 互操作；lineage 完整不保证 reviewer 判断或 deployment recommendation 正确。 旧路径在其假设成立时继续保留；任一新 sensor、router 或 artifact 未通过自身 contract 时，回退到现有 deterministic owner、人工审批或 supported runtime。

### Review note

- SF-2026-ARXIV-2606-22142: arXiv:2606.22142v1; exact-v1 official URL=`https://arxiv.org/html/2606.22142v1`; Method=`https://arxiv.org/html/2606.22142v1 — §3 Method; §3.2 Agent-Native Governance Over Lifecycle Artifacts; §3.5 Data Health, Training Integration, and Version Governance`; Evaluation=`https://arxiv.org/html/2606.22142v1 — §4 Experiments; §4.1 Experimental Setup`; Non-proof/limitations=`https://arxiv.org/html/2606.22142v1 — §5 Limitations and Discussion`; durable delta=RoboLineage 把 rollout、review、dataset decision、training run、policy metadata、evaluation、deployment recommendation 与 next-collection plan 变成 typed lineage artifacts，agent 只能在 artifact boundary 内推进。 Boundary: robot workflow 与作者工具不能证明跨 embodiment/stack 互操作；lineage 完整不保证 reviewer 判断或 deployment recommendation 正确。

## TRAIN-DISTRIBUTED-TRAINING — books/part-04-training-system/36-distributed-training.md

Insert after `### 从 Phase 串行到依赖驱动的跨 Phase 重排`.

### Minimal durable delta

FeLoG 用 embedding-quality feedback 优先 undertrained node；activity-aware sequence compression/选择同步降低 PCIe 与网络通信，round-interleaved pipeline 重叠下一轮 sampling 与当前 training。

### Old path / coexistence / cost / failure / fallback

quality feedback 可能偏置 sampling，选择同步会制造 stale embedding；graph workloads 与硬件不证明 LLM training 或最终收敛等价。 旧路径在其假设成立时继续保留；任一新 sensor、router 或 artifact 未通过自身 contract 时，回退到现有 deterministic owner、人工审批或 supported runtime。

### Review note

- SF-2026-ARXIV-2606-22180: arXiv:2606.22180v1; exact-v1 official URL=`https://arxiv.org/html/2606.22180v1`; Method=`https://arxiv.org/html/2606.22180v1 — §5 FeLoG; §5.1 Feedback-coupled Sampling-Training Model; §5.2 Activity-aware Communication`; Evaluation=`https://arxiv.org/html/2606.22180v1 — §6 Experimental Results; §6.1 Experimental Setup`; Non-proof/limitations=`https://arxiv.org/html/2606.22180v1 — §7 Conclusions and experimental generalizability boundary`; durable delta=FeLoG 用 embedding-quality feedback 优先 undertrained node；activity-aware sequence compression/选择同步降低 PCIe 与网络通信，round-interleaved pipeline 重叠下一轮 sampling 与当前 training。 Boundary: quality feedback 可能偏置 sampling，选择同步会制造 stale embedding；graph workloads 与硬件不证明 LLM training 或最终收敛等价。

## TRAIN-GRPO — books/part-04-training-system/33-grpo.md

Insert after `### 从一个终局标量到 Typed Credit：Reward 必须匹配决策边界`.

### Minimal durable delta

对 deterministic generator 构造 solver-grounded CoT 后，区分 forward-derivable procedure 与 information-free backtracking search；不可忠实前向化的 search 应外置为 catalog/search，再让模型做 bounded verification。 multimodal RLVR 的 answer reward 会先强化语言 shortcut，再在足够视觉证据/奖励强度下发生 watching transition；应监控 visual reliance 并在形成窗口干预。 多轮 RL 的难度由 decision density ρ 而非 raw horizon 单独决定；routine reward-equivalent turns 给 trajectory estimator 增方差但不增期望 signal，低 ρ 时需要 turn-level critic/credit。

### Old path / coexistence / cost / failure / fallback

竞赛型同生成器 testbed、LoRA 与有限模型族不建立普遍不可学习定理；catalog escape 依赖有限结构并把 search 成本移到外部。 单一模型与 video-QA task 不给出跨模型 reward 阈值；VHS 是 temporal perturbation proxy，回答正确也不证明 grounded reasoning。 推导依赖 critic error 受控与 routine turn 真正 reward-equivalent；受控环境不证明开放 agent 能可靠标出 decision turn。 旧路径在其假设成立时继续保留；任一新 sensor、router 或 artifact 未通过自身 contract 时，回退到现有 deterministic owner、人工审批或 supported runtime。

### Review note

- SF-2026-ARXIV-2606-21884: arXiv:2606.21884v1; exact-v1 official URL=`https://arxiv.org/html/2606.21884v1`; Method=`https://arxiv.org/html/2606.21884v1 — §4 Method: Solver-Grounded Synthetic CoT and the Experiment Ladder`; Evaluation=`https://arxiv.org/html/2606.21884v1 — §5 Results; §6 Anatomy of the Failures`; Non-proof/limitations=`https://arxiv.org/html/2606.21884v1 — §8.2 Threats to validity; §10 Limitations`; durable delta=对 deterministic generator 构造 solver-grounded CoT 后，区分 forward-derivable procedure 与 information-free backtracking search；不可忠实前向化的 search 应外置为 catalog/search，再让模型做 bounded verification。 Boundary: 竞赛型同生成器 testbed、LoRA 与有限模型族不建立普遍不可学习定理；catalog escape 依赖有限结构并把 search 成本移到外部。
- SF-2026-ARXIV-2606-22043: arXiv:2606.22043v1; exact-v1 official URL=`https://arxiv.org/html/2606.22043v1`; Method=`https://arxiv.org/html/2606.22043v1 — §2 Setup — Task and model; Visual-hacking diagnostic (VHS); Held-out OOD evaluation; Trajectory fleet`; Evaluation=`https://arxiv.org/html/2606.22043v1 — §3 Onset is real and seed-robust; §4 Reward strength: a monotone dose–response with formation–reversal asymmetry; §5 A critical intervention window; §6 What changes inside: representation probe; Appendix A Reproducibility and diagnostic details`; Non-proof/limitations=`https://arxiv.org/html/2606.22043v1 — §8 Discussion and limitations — Limitations`; durable delta=multimodal RLVR 的 answer reward 会先强化语言 shortcut，再在足够视觉证据/奖励强度下发生 watching transition；应监控 visual reliance 并在形成窗口干预。 Boundary: 单一模型与 video-QA task 不给出跨模型 reward 阈值；VHS 是 temporal perturbation proxy，回答正确也不证明 grounded reasoning。
- SF-2026-ARXIV-2606-22164: arXiv:2606.22164v1; exact-v1 official URL=`https://arxiv.org/html/2606.22164v1`; Method=`https://arxiv.org/html/2606.22164v1 — §2 Preliminaries; §3 The Signal Dilution Problem`; Evaluation=`https://arxiv.org/html/2606.22164v1 — §4 Experimental Setup; §5 Results`; Non-proof/limitations=`https://arxiv.org/html/2606.22164v1 — §7 Discussion; Appendix A assumptions; Appendix B Diluted Doors`; durable delta=多轮 RL 的难度由 decision density ρ 而非 raw horizon 单独决定；routine reward-equivalent turns 给 trajectory estimator 增方差但不增期望 signal，低 ρ 时需要 turn-level critic/credit。 Boundary: 推导依赖 critic error 受控与 routine turn 真正 reward-equivalent；受控环境不证明开放 agent 能可靠标出 decision turn。

