# 2026-06-21 Books Integration Queue V1

Denominator `DEN-20260621-83b5c89e`. CLOSED: root wrote 20 family deltas into 12 owner files; the 37/37 post-write audit passed.

## AGENT-MULTI-AGENT

- Target: `books/part-07-agent/82-multi-agent.md`
- Exact target locator: `## Message 不是 State`
- Source families: SF-2026-ARXIV-2606-22203
- Minimal durable delta: 先用 counterfactual neighbor perturbation 测 coupling gain，再以 target-interaction modality-matched group coupling 选择 consensus dynamics；随机初值 slope/bias 区分 genuine averaging 与 model prior。
- Evidence boundary: pairwise gamma 不能预测 multi-neighbor 结果且可反向排序；default agents 未自发 backfire，polarization 均为外部诱导，实验舆论任务不等于真实社会。

## AGENT-WORKFLOW

- Target: `books/part-07-agent/81-workflow.md`
- Exact target locator: `## State Machine 是基本模型`
- Source families: SF-2026-ARXIV-2606-21891, SF-2026-ARXIV-2606-21968, SF-2026-ARXIV-2606-22175
- Minimal durable delta: ARTS 在 scientific search tree 中把 hypothesis merit 与 execution quality 分开；audit node 的 code/log 后决定 repair 同一 idea 还是 pivot，并把 search history用于 scientist test-time training。 ViRGo 根据目标尺度与置信度，在 global view、patch zoom 与 attention-guided visual retrieval间路由，避免固定高分辨率同时丢 context 或浪费 token。 StickyInvoc 把昂贵 model/runtime state 的 create/destroy 与 invocation goodput 解耦：sticky task 持有 node-local state，后续 invocation 继承但不销毁，抢占时按 state owner 重建。
- Evidence boundary: scientist/executor 共偏、每 task 的 A100 训练预算与 22-task frontier 不能证明科学发现正确；human-best 和 validation score 仍受 benchmark 约束。 router confidence 可共偏，小目标/多目标阈值依赖数据；离线 benchmark 不证明实时 latency 或任意 VLM transfer。 persistent state 会引入 version、tenant isolation、eviction 与 stale-state risk；作者 workflow 不证明交互式 tail latency 或任意 preemptible site。

## INFER-GPU-MEMORY

- Target: `books/part-05-inference-system/54-gpu-memory.md`
- Exact target locator: `### Weights 与 KV 的联合 HBM 预算：可提交的运行时精度页`
- Source families: SF-2026-ARXIV-2606-22283
- Minimal durable delta: 对 ANE 的 datapath、roofline、compiler/on-disk format、weight compression、driver/firmware command protocol建立 measured/decompile-derived/predicted 三类 claim，并区分 direct private route 与 Core ML supported path。
- Evidence boundary: private runtime/driver 路径 undocumented、unsupported、version-fragile，只适合研究测量；预测项不能冒充芯片公开规格或 shipping contract。

## INFER-SCHEDULING

- Target: `books/part-05-inference-system/56-inference-scheduling.md`
- Exact target locator: `### MoE Decode：从 Queue Length 到 Expert Working Set`
- Source families: SF-2026-ARXIV-2606-21868
- Minimal durable delta: WiSP 把低资源 MoE inference 表述为 expert-weight 与 KV cache 的联合 working set：预测近期 active experts，按相同内存预算在 expert residency、KV 保留与 transfer 间分配。
- Evidence boundary: Qwen3/Kimi 的受限设备结果是在 94 GiB H100 上用 gpu-memory-utilization cap 模拟，并非真实小卡；预测错误还会同时触发 expert miss 与 KV pressure，质量保持也不等于 tail SLO。

## MODEL-SELF-ATTENTION

- Target: `books/part-02-model/14-self-attention.md`
- Exact target locator: `## 从匹配分数到读取权重`
- Source families: SF-2026-ARXIV-2606-21848
- Minimal durable delta: 把 query-key 路由改为 query-value 路由，并在 inference 预乘 query factor，只保存 value representation；QVV(3) 保持投影矩阵数同时移除 key cache。
- Evidence boundary: 等价定理依赖 value projection 的秩/子空间条件；小模型从头训练不证明可无损转换既有大模型，50% 是 attention-cache tensor 而非端到端显存。

## PLATFORM-EVALUATION-SYSTEM

- Target: `books/part-06-ai-infrastructure/66-evaluation-system.md`
- Exact target locator: `## 从答案评分到可执行证据`
- Source families: SF-2026-ARXIV-2606-21869, SF-2026-ARXIV-2606-21954, SF-2026-ARXIV-2606-22179
- Minimal durable delta: 把每语言生成能耗与 accuracy、tokenization expansion 分开记录；evaluation/model card 需声明 per-language energy，而不能用英语平均值代表多语言部署。 Hardness Adjusted Transfer 以 target performance 相对 source-language ability 校正，避免把 source accuracy 提升误报成 cross-lingual transfer 进步。 selective prediction 除 calibration/ranking 还要报告 score granularity：可用阈值数量决定 operator 能选择多少风险工作点；多查询扩大分辨率但增加成本且可能伤害强模型排序。
- Evidence boundary: 绝对能耗硬件相关；没有闭源模型，翻译 prompt 不是 native usage，作者将观测 gap 定义为可能的下界而非普遍常数。 HAT 依赖 benchmark hardness 与 source/target choice；三套 benchmark 不代表生成、方言或部署流量。 三 benchmark 与 black-box classification 不证明生成/agent risk；更细阈值不自动校准，重复查询还引入相关样本与成本。

## PLATFORM-MONITORING

- Target: `books/part-06-ai-infrastructure/67-monitoring.md`
- Exact target locator: `## 先定义目标，再选择可测信号`
- Source families: SF-2026-ARXIV-2606-21843
- Minimal durable delta: agent identity monitor 以固定 probe 的 next-token distribution、sqrt-JSD geometry 与 magnitude homology 追踪 conditioning；但 diverse-padding 对照推翻了原 repetitive-padding drift trajectory。
- Evidence boundary: 作者自评、单模型单 agent、单日采集且无 reconstitution control；几何诊断潜力没有被真实纵向 drift 证实。

## PLATFORM-PRODUCTION

- Target: `books/part-06-ai-infrastructure/73-production-best-practice.md`
- Exact target locator: `## Capacity、Failure 与 Recovery`
- Source families: SF-2026-ARXIV-2606-22013
- Minimal durable delta: ML serving load test 以 adaptive capacity search 而非固定 traffic sweep，联合寻找满足 latency/SLO 的最大 load 与资源点，并保留 warm-up、arrival 和 model artifact identity。
- Evidence boundary: 14 个匿名生产模型偏向 recommendation/ranking；P90 七日观测吞吐可能低估真实最大 capacity，且结论不能代表 LLM continuous batching。

## PLATFORM-SECURITY

- Target: `books/part-06-ai-infrastructure/72-security.md`
- Exact target locator: `## 风险管理而不是一次性认证`
- Source families: SF-2026-ARXIV-2606-21877, SF-2026-ARXIV-2606-22019, SF-2026-ARXIV-2606-22263
- Minimal durable delta: AgentRiskBOM 在 SBOM/AIBOM/MLBOM 之外声明 autonomy、tool permission、memory、credential scope、approval gate、audit signal、inter-agent channel 与 external action，并对 release mutation 做 diff。 subliminal-learning audit 不能只看 representation 是否线性可分；只有 signal 所在 channel 与审计 probe 的 initialization/alignment 匹配时，训练前 detector 才有权解释。 Revelio 让廉价 LLM/static analysis 只生成和排序 vulnerability hypothesis，最终必须提交 executable Proof-of-Vulnerability 并由 deterministic sanitizer 复现后才报告。
- Evidence boundary: 这是 declared authority envelope 与 coverage instrument，不是 live exploit test 或 safety certificate；threshold 仍需人工/环境校准。 结果是 channel regime 边界，不是通用训练数据 scanner；Not Covered 必须保持 Unknown，不能被扩张为无隐藏训练。 sanitizer 只覆盖可触发 memory-safety failure；未复现不等于无漏洞，项目/时间预算与 benchmark selection 限制 recall 结论。

## TRAIN-DATA

- Target: `books/part-04-training-system/27-data.md`
- Exact target locator: `## Data lineage 是训练可复现性的前提`
- Source families: SF-2026-ARXIV-2606-22142
- Minimal durable delta: RoboLineage 把 rollout、review、dataset decision、training run、policy metadata、evaluation、deployment recommendation 与 next-collection plan 变成 typed lineage artifacts，agent 只能在 artifact boundary 内推进。
- Evidence boundary: robot workflow 与作者工具不能证明跨 embodiment/stack 互操作；lineage 完整不保证 reviewer 判断或 deployment recommendation 正确。

## TRAIN-DISTRIBUTED-TRAINING

- Target: `books/part-04-training-system/36-distributed-training.md`
- Exact target locator: `### 从 Phase 串行到依赖驱动的跨 Phase 重排`
- Source families: SF-2026-ARXIV-2606-22180
- Minimal durable delta: FeLoG 用 embedding-quality feedback 优先 undertrained node；activity-aware sequence compression/选择同步降低 PCIe 与网络通信，round-interleaved pipeline 重叠下一轮 sampling 与当前 training。
- Evidence boundary: quality feedback 可能偏置 sampling，选择同步会制造 stale embedding；graph workloads 与硬件不证明 LLM training 或最终收敛等价。

## TRAIN-GRPO

- Target: `books/part-04-training-system/33-grpo.md`
- Exact target locator: `### 从一个终局标量到 Typed Credit：Reward 必须匹配决策边界`
- Source families: SF-2026-ARXIV-2606-21884, SF-2026-ARXIV-2606-22043, SF-2026-ARXIV-2606-22164
- Minimal durable delta: 对 deterministic generator 构造 solver-grounded CoT 后，区分 forward-derivable procedure 与 information-free backtracking search；不可忠实前向化的 search 应外置为 catalog/search，再让模型做 bounded verification。 multimodal RLVR 的 answer reward 会先强化语言 shortcut，再在足够视觉证据/奖励强度下发生 watching transition；应监控 visual reliance 并在形成窗口干预。 多轮 RL 的难度由 decision density ρ 而非 raw horizon 单独决定；routine reward-equivalent turns 给 trajectory estimator 增方差但不增期望 signal，低 ρ 时需要 turn-level critic/credit。
- Evidence boundary: 竞赛型同生成器 testbed、LoRA 与有限模型族不建立普遍不可学习定理；catalog escape 依赖有限结构并把 search 成本移到外部。 单一模型与 video-QA task 不给出跨模型 reward 阈值；VHS 是 temporal perturbation proxy，回答正确也不证明 grounded reasoning。 推导依赖 critic error 受控与 routine turn 真正 reward-equivalent；受控环境不证明开放 agent 能可靠标出 decision turn。

