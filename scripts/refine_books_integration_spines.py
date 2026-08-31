#!/usr/bin/env python3
"""Replace template-shaped Daily insertions with chapter-owned mechanism spines.

The original source-family blocks are preserved verbatim under Review notes.
The main body receives one durable synthesis owned by the chapter.
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path


SYNTHESIS: dict[str, str] = {
    "books/part-02-model/21-moe.md": """MoE 最初只把 Dense MLP 的全部激活改成 top-k 条件激活；在 expert 数量和并行规模继续增长后，真正的新约束不再只是平均负载，而是 router state 是否稳定、specialization 是否形成，以及 token flow 能否被当前 topology 高效执行。相同 token id 也不意味着相同内部路径，因此 routing pattern 可以作为诊断信号，却不能直接拥有正确性结论。\n\n这条演进把 router 从一个局部分类器变成模型与 runtime 共享的受观测状态：训练侧同时检查 load、specialization 与 collapse dynamics，执行侧再决定 placement、dispatch 和 grouped GEMM。收益是扩大总容量并保留条件计算；代价是路由漂移、热点 expert、All-to-All 与诊断成本。Dense MLP 在规模较小或通信主导时仍是更稳健的分支，静态 load-balance 指标也仍是必要但不充分的 baseline。""",
    "books/part-02-model/22-long-context.md": """Long Context 的第一阶段是扩大可见窗口，随后压力依次转移到位置外推、Prefill 二次复杂度、KV 容量和信息利用率。因而后续方案不是同一条速度排行榜，而是多条条件分支：稀疏 selector 减少读取，sliding/prefix policy 保留不同类型的历史，recurrent 或 parametric state 把跨段信息迁出显式 token window。\n\n这些机制共同要求 context state 带有位置、可见性、预算、更新规则和 fallback identity。更小的状态换来更低 memory/compute，却会引入 selector drift、中间证据丢失、写入污染和训练—推理可见性不一致。需要完整回看、selector 未校准或状态语义变化时，应回退 dense context、检索或更大 KV；位置扩展本身不能证明模型真正利用了远距离证据。""",
    "books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md": """生成范式的演进不是 AR 被 Diffusion 线性取代，而是 factorization、并行度与 correction authority 的重新分配。AR 每次提交一个 token，状态简单但串行；masked、block 或 diffusion 路线并行提出多个 provisional positions，再以迭代修正换吞吐。混合方案进一步把 proposal、verification、rollback 和 commit 拆开。\n\n并行生成只有在质量合同、cache invalidation 和停止规则都被版本化后才成立。它获得并行度，却增加迭代次数、临时状态、拒绝/回滚以及训练—推理 mismatch；短输出、严格 exactness 或 correction 成本高时，AR 仍可能更优。图像、视频和文本的 evaluator、长度与硬件路径不同，不能共享未经条件化的性能结论。""",
    "books/part-03-multimodal-world-models/25-multimodal-world-models.md": """从视频生成进入 World Model 的关键约束变化，是输出不再只需“看起来合理”，而要在给定 action 后保持可修正的 environment transition。系统因此从下一帧生成，演进到 latent state、action-conditioned rollout、持久 landmark/memory 与 observation reconciliation；state owner 必须区分预测状态、已观测事实和计划假设。\n\n更长的 imagined rollout 可以降低真实交互成本，却会累积 model bias、state drift 和不可观测变量。生成质量只证明感知 plausibility，不能证明 causal controllability；simulator 或 persistent memory 也不能自动获得真实环境 authority。出现冲突时应以新 observation 修正或丢弃预测 state，并保留短 horizon、真实环境 replay 和人工验证作为共存路径。""",
    "books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md": """VLA 把多模态表示推进到物理行动后，约束从“生成正确描述”变为“在有限 control frequency 内产生可执行且可恢复的动作”。演进路径因此是视觉语言 proposal → typed affordance/trajectory → action chunk → low-level controller → environment transition → observation correction；高层模型拥有意图和候选，实时 controller 与 safety envelope 拥有最终执行边界。\n\n层级控制减少高层模型的实时压力，也允许复用 policy pool，但增加 calibration、handoff、latency 和 state-staleness 风险。仿真成功、视频质量或离线 action accuracy 都不能代替实机闭环；controller 超时、sensor drift 或分布外接触发生时，应缩短 action chunk、降级到保守 controller 或交还人工。旧的模块化 perception/planning/control 在安全边界明确时仍然成立。""",
    "books/part-04-training-system/27-data.md": """训练数据从静态语料集合演进成有版本的生产系统：采集和过滤决定候选分布，去重与 repeat policy 决定 compute 是否反复消费同一信号，mixture/controller 决定不同 domain 在训练阶段获得多少预算，synthetic-data pipeline 则把 generator、validator 与 lineage 引入数据面。\n\n新的控制能力改善覆盖和成本，却会引入 controller reward 偏差、合成错误放大、semantic near-duplicate 漏检和 provenance 断裂。数据 owner 因而必须保存 source、transform、sample、split、mixture、checkpoint consumption 与删除证据；行为或 feature attribution只能提供复核线索，不能替代删除/重训对照。固定 mixture、人工抽样和保留原样本仍是 drift 或归因不可靠时的 fallback。""",
    "books/part-04-training-system/28-pretraining.md": """预训练优化最初用统一 optimizer 与全局 learning-rate schedule 管理所有参数；规模扩大后，width、depth、token budget、batch、warmup 和参数方向的敏感度发生非线性交互。因而 learning rate 不应按层数机械动态调整，而应先以 matched probe 判断哪些方向或尺度真正触及 stability boundary。\n\n局部 spectral probe 或邻近规模 sweep 可以减少统一步长的过保守与过激，却增加测量噪声、控制状态和额外训练成本。任何外推都必须冻结 data、optimizer、schedule、precision 与 token budget；超出验证尺度时重新校准，而不是把局部幂律当成普遍规律。统一 schedule 在观测不足或收益不覆盖复杂度时仍是 canonical baseline。""",
    "books/part-04-training-system/30-lora.md": """LoRA 从一次低成本微调演进到多租户、持续变化的 adapter lifecycle 后，低秩矩阵不再只是训练参数，而是带 base revision、objective、contributor、priority 与撤销语义的独立 artifact。去中心化或边缘场景还要求系统明确谁拥有 contribution、怎样合并、参与者退出时如何 unlearn，以及何时需要重训。\n\n细粒度 adapter 提高复用和个性化，却增加组合冲突、base 漂移、merge 顺序和 provenance 成本。校正或 unlearning 只有在目标 contribution 可定位、效果可验证时才可提交；否则保留旧 adapter、隔离租户或回退完整微调。参数更少不等于 runtime、registry 和安全状态更简单。""",
    "books/part-04-training-system/31-rlhf.md": """偏好训练最初把人工比较压缩成固定 Reward Model；当 policy 持续变化后，静态 rubric 会逐渐失去区分度，feedback 的 rater identity、产生时间和适用 domain 也会改变 reward 的含义。演进方向因此是把 preference、rubric/spec、reward model、policy revision 与独立 evaluator 分离版本，而不是让 policy 与 judge 在同一闭环中共同漂移。\n\n动态 rubric、spec learning 或 on-policy distillation可以提高适应性，却会放大 reward hacking、judge correlation、density mismatch 与评价成本。它们必须通过 frozen holdout、独立 outcome evidence 和 rollback gate；反馈不足或评估失去区分力时，回退静态 rubric、SFT 或人工 adjudication。几何差异只有在 data、step 和 learning rate 匹配时才可归因于 objective。""",
    "books/part-04-training-system/33-grpo.md": """GRPO 去掉 critic 后，把主要状态转移到同 prompt rollout group、相对 reward 与 policy freshness。规模扩大时，瓶颈不只在公式：domain curriculum、group straggler、stale rollout、update ratio、reward density 和 supervisory repair 共同决定有效 credit。controller 可以利用 gradient transfer 或运行时风险选择 domain/group，但不能拥有最终 correctness。\n\n这类控制减少无效 rollout 或 critic 状态，却引入更多采样、估计噪声、跨域干扰和 collapse gate。收益必须在相同 rollout/token/optimizer budget 下比较；gradient conflict、verifier drift 或 policy divergence 越界时，应回退 proportional mixture、同步 rollout 或 PPO/SFT 分支。PPO 与 GRPO 是 credit fidelity、variance 和 compute 的条件分支，而不是新旧替代。""",
    "books/part-04-training-system/36-distributed-training.md": """分布式训练从同步 homogeneous collective 出发，因为它最容易保持单机更新语义；跨地域、异构链路、稀疏更新和 RL pipeline 扩大后，阻塞同步开始浪费资源。新的分支用 topology-aware collective、bounded-staleness queue、factored/gossip update、block-local objective 或 fused optimizer path 移动通信和 memory 压力。\n\n每次放松同步都会增加 version、acceptance、convergence 和 failure state。runtime 可以重排通信或接收候选 update，但不能静默改变 global batch、loss weighting 与 optimizer semantics；吞吐提升也必须和收敛、分歧、恢复及 checkpoint identity共同验收。链路稳定、规模较小或质量边界严格时，同步 collective 仍是最可靠的基线。""",
    "books/part-05-inference-system/42-what-happens-during-inference.md": """请求生命周期最初以一次 prompt→response 为边界；会话、Agent 和交互式多模态 workload 出现后，request 之外还存在 idle、tool wait、state mutation 和下一 decision point。runtime 因而可以在空闲期准备 speculative state，或按 confidence 选择后端，但所有准备结果必须绑定 base-state identity，并在用户输入或环境变化时失效。\n\n提前计算和 confidence routing 可以降低命中路径延迟，却会消耗闲时资源并引入 false accept、stale state 和路由偏差。只有 acceptance gate 能原子提交新状态；任何 identity mismatch 都回到普通 Prefill/Decode。单次无状态请求仍是最简单、最容易隔离的分支。""",
    "books/part-05-inference-system/43-prefill.md": """Prefill 的原始优势来自已知 prompt 的 token 并行；长 Context 与异构硬件把瓶颈进一步推向 memory orchestration、chunk pipeline、weight movement 和 cache blocking。执行计划因此从单个大 GEMM 演进到按 chunk、memory tier 和 device topology 安排工作，同时仍要产生与 dense Prefill 相同的初始 logits 与 KV identity。\n\n更细粒度的 pipeline 可以降低峰值和通信等待，却增加调度、packing、跨 chunk依赖及专用 kernel 成本。shape、hardware 或 cache assumption 改变时必须重新 profile；短 prompt、通用硬件或可移植性优先时，普通 dense Prefill 仍更合适。""",
    "books/part-05-inference-system/44-decode.md": """Decode 从逐 token kernel loop 演进成长期驻留的状态推进器后，故障恢复也从重启整个服务下沉到 token/KV/checkpoint boundary。Persistent kernel 或 JIT checkpoint 可以减少 launch 和恢复成本，但必须记录最后已提交 token、KV revision 与外部 stream effect，避免恢复后重复输出或重复副作用。\n\n更细恢复粒度换来 device-resident metadata、checkpoint overhead 和更复杂的 communicator failure handling。状态无法证明一致或客户端已观察的输出不可撤销时，应回退请求级重算或终止，而不是猜测续跑。短请求和低故障率 workload 仍可能不值得承担持续 checkpoint 成本。""",
    "books/part-05-inference-system/45-why-kv-cache-speeds-up.md": """KV Cache 最初保存全部历史以换取 exact reuse；容量压力出现后，设计沿四条轴分化：共享要求完整 identity，相对位置或跨模态复用需要 correction；eviction 选择保留状态；quantization 改变表示精度；tiering 把已驱逐状态变成可恢复而非永久删除。\n\n这些机制把 cache manager 从 allocator 提升为有版本的状态 owner，但不能改变模型语义。更小 HBM 占用换来 selector/quantizer drift、position mismatch、transfer latency 和质量回归；每条路径都要保留 dense/full-precision fallback，并以 model、tokenizer、position/mask、adapter、precision 和 revision 检查兼容性。完整 KV 在短 Context、高风险或复用率低时仍是正确基线。""",
    "books/part-05-inference-system/48-speculative-decoding.md": """经典 speculative decoding 以共享条件和 exact acceptance 保持 target distribution；当 verifier、网络或长 Context 成本上升后，分支扩展到 response-level cascade、稀疏 target attention、edge-cloud offload 和 asymmetric context。此时 proposal、verification 与 commit 的接口仍相同，但不一定继续拥有 exactness。\n\n降低 verifier 成本可以增加 accepted progress，却引入 router error、稀疏读取遗漏、WAN RTT、Context mismatch 和新的质量阈值。只有 target-aligned matched arm 能区分算法差异与 dtype/framework 噪声；低 acceptance、schema-critical request 或 invariance screen 失败时，应回到 dense target 或普通 autoregressive decode。""",
    "books/part-05-inference-system/49-tensorrt-llm.md": """Execution engine 从调用通用 kernel library 演进到 JIT、superoptimization 和 profile-guided search 后，搜索器只能提出 plan，correctness validator 与 target hardware measurement 才能提交 plan。模型 graph、dtype/layout、kernel、memory schedule 与 serving config 必须形成同一可重建 artifact。\n\n专用 plan 能压低局部 kernel 成本，却增加搜索时间、shape specialization、数值偏差和 artifact explosion。硬件、batch、precision 或模型 revision 变化后必须失效并重新验证；通用 library 路径始终作为 coverage 和 correctness fallback。单次 benchmark 的最快 kernel 不能外推为完整 Serving engine 的最优计划。""",
    "books/part-05-inference-system/54-gpu-memory.md": """GPU memory 优化从单一 HBM 容量规划演进到 locality、tiering、compression 与异构 device 的联合执行。Weights、KV、workspace 和 communication buffer具有不同可预测性与生命周期：chiplet placement 要与 layout 协同，长状态可以下沉 DRAM/CXL/NVMe，MoE weights 可按激活相关性 staging，压缩格式则必须与 GEMM tiling共同调度。\n\n每减少一类常驻 bytes，通常都会增加 prefetch miss、decode bandwidth、remote access、metadata 或质量回退。低比特甚至可能通过更多 reasoning tokens 抬高总成本，因此验收单位应是完成请求/任务所需的峰值 memory、latency、energy 和 output quality，而不是单个 tensor 的压缩比。状态不可预测或迁移成本主导时，常驻 HBM 与未压缩布局仍更可靠。""",
    "books/part-05-inference-system/56-inference-scheduling.md": """推理调度从 FIFO/静态 batch 演进到持续观察 token progress、KV residency、runtime drift 与 SLO slack；Agent 和多模态 workload 又把 owner 上移到 conversation 或 workflow DAG。scheduler 不再只决定“下一个请求”，还要权衡 critical path、prefix reuse、movement、thinking budget、thermal/energy 与 fairness。\n\n更丰富的 state 可以改善 makespan 和资源利用率，却增加预测误差、饥饿、tenant interference 和控制面成本。真实 queue/page/completion state 仍由 runtime 拥有，workflow 只提供 dependency hint；估计失准时回退 aging、EDF、FIFO 或保守 admission。局部 prefix hit、平均 throughput 或单请求 latency都不能单独成为全局目标。""",
    "books/part-06-ai-infrastructure/57-what-is-ai-platform.md": """AI Platform 的演进起点是共享脚本和集群资源；随着 artifact、训练、Serving、Evaluation 与 Agent 状态相互依赖，平台必须分离 declarative desired state、runtime observed state 和 evidence-backed release decision。Controller 可以协调生命周期，却不能把资源就绪冒充模型质量或业务完成。\n\n统一控制面提高复用和治理能力，也增加 schema、migration、reconciliation 与 blast radius。小团队或一次性实验仍可使用更薄的脚本路径；进入多租户和生产后，所有自动动作都应有 identity、policy、receipt 与 rollback。""",
    "books/part-06-ai-infrastructure/59-model-registry.md": """Registry 从保存权重文件演进为模型交付身份图：base、adapter、tokenizer、data/objective、checkpoint、quantization、runtime compatibility、evaluation evidence 和 deployment decision 必须可追溯。规模化 PEFT 进一步说明，一个 base 可以对应大量租户 adapter，版本和访问边界不能只靠文件名表达。\n\n更完整的 lineage 支持复现、promotion 和 rollback，却增加元数据一致性与存储治理成本。缺少兼容性或 evidence 的 artifact 只能处于 candidate 状态，不能被 registry 的“已注册”误解为“可生产发布”；简单目录仍可用于本地实验，但不承担跨团队 release authority。""",
    "books/part-06-ai-infrastructure/63-gpu-scheduler.md": """GPU scheduler 最初按卡数和显存做 placement；异构 accelerator、MIG、拓扑与动态并行出现后，资源必须表达 capability、locality、sharing mode、health 和可重配置成本。调度器选择 placement，runtime 决定算子和通信，二者通过可验证 profile 交接，而不是互相猜测。\n\n更精细的 typed resources 提高利用率，却增加碎片、reconfiguration latency、profile drift 和 fairness问题。capability 不可验证、拓扑快速变化或隔离要求严格时，应回退整卡、静态 pool 或保守 quota。理论可放置不等于满足训练/推理 SLO。""",
    "books/part-06-ai-infrastructure/66-evaluation-system.md": """Evaluation 从单一 benchmark 分数演进为版本化的决策证据系统。首先冻结 subject、dataset/environment、metric/judge 和 run identity；随后对 calibration、slice、uncertainty 与复现参数建模；当评估成本或开放任务使完整真值不可得时，再引入顺序检验、受控子集、可执行 predicate、typed reasoning trace 或 abstention。\n\n更自动的 evaluator 能扩大覆盖，却会引入 judge bias、leakage、aggregation degrees of freedom、相关样本和未编码目标。任何分数只有在其 EvalSpec 和适用分布内成立，release authority 必须独立于产生分数的模型；低功效、漂移或 oracle 不完整时结论应为 inconclusive，而不是强行排序。人工评审、完整 benchmark 和真实 environment outcome始终作为高风险 fallback。""",
    "books/part-06-ai-infrastructure/67-monitoring.md": """Monitoring 从被动收集 metrics 演进到能解释 workload 和 failure onset 的 sensor system。Metric、log、trace、probe 与 context generator 都有自己的版本、采样和成本；主动 probe 可以制造可诊断信号，但必须与真实用户流量分开标记。\n\n更丰富的传感器提高定位能力，却增加 overhead、privacy 风险、cardinality 和 observer effect。Monitoring 只拥有 observed state，不拥有“系统是否足够好”的最终判断；采样缺失或 sensor identity 漂移时，应保留 unknown，而不是以低错误率推断质量。Evaluation 和 release policy消费这些证据但保持独立。""",
    "books/part-06-ai-infrastructure/69-trace.md": """Trace 从请求 spans 演进到跨 model、tool、workflow 和 environment 的语义因果链后，必须同时记录执行顺序、数据/状态依赖、版本与外部 effect。只有这样，终局 failure 才能回溯到首次有害 commitment，而不是把相关步骤误当原因。\n\n更细 trace 提高 replay 和 attribution，却带来数据量、隐私、采样偏差和跨系统 clock/identity 问题。关键 action 与 state transition 需要不可丢的 receipt，普通高频 span 可以采样；trace 缺口存在时只能缩小 claim，不能由流畅 narrative 补全不存在的事件。""",
    "books/part-06-ai-infrastructure/70-cost.md": """成本核算从 GPU-hour 扩展到一次可交付结果的完整资源图：训练 token、checkpoint、Serving bytes、KV transfer、tool/API、evaluation、失败重试、人工复核和 idle capacity 都应归属明确 workload。局部加速只有减少了端到端关键路径或容量成本，才构成系统收益。\n\n更精细的 activity-based accounting 提高决策质量，却增加归因和采集开销。数据缺失时应报告区间和未分配成本，而不是伪造单一精确数字；小规模实验仍可使用简化核算，但不能把 vendor headline 或 kernel speedup 直接升级为 TCO 结论。""",
    "books/part-06-ai-infrastructure/72-security.md": """AI security 的演进主线是从文本输出审查转向可执行 effect 的控制。Prompt、retrieved data、skill/tool package 和 agent message 都是不可信输入；proposal、authorization、issue、execution、observation 与 rollback 必须分别有 owner。尤其外部调用在 issue-time 已可能泄露，事后 cleanup 不能撤销已发送数据。\n\n更细的 capability、taint、policy graph 和 executable probe 能约束跨步骤 harm，却增加 overtaint、policy incompleteness、组合状态和运行开销。模型、judge 或自然语言 approval 都不能成为最终 authority；无法证明身份、权限或 effect predicate 时必须拒绝、sandbox 或人工升级。静态扫描和单轮 guard 仍是 defense-in-depth，但不能替代 lifecycle 与 trajectory evidence。""",
    "books/part-07-agent/74-prompt.md": """Prompt 从临时文本演进成影响行为和权限边界的版本化输入 artifact。system instruction、task data、retrieved evidence 与 tool result必须保留来源和优先级，不能因为拼接到同一 Context 就获得同等 authority。\n\n模板化和自动优化提高复用，却增加 injection、版本漂移和隐式 policy 变化。Prompt 只能提出行为约束，真实授权仍由 Tool/Workflow/Platform执行；高风险请求或来源冲突时，应缩小能力、请求澄清或拒绝，而不是让更长提示词代替 enforcement。""",
    "books/part-07-agent/75-context.md": """Context 从 token 拼接演进为带类型和生命周期的运行时 state：task contract、working evidence、tool output、safety rule 与历史草稿有不同 retention 和 correctness 要求。统一截断或摘要在内容同质时合理；长任务中则需要 type-aware compression、pinned rules、externalized state 与显式 invalidation。\n\n更细的 Context policy降低 token 成本，却引入分类错误、compaction cliff、stale summary 和 provenance 丢失。压缩结果必须能够回到原始 evidence，规则冲突或置信度不足时回退完整 Context、检索或人工确认；Context 是当前运行状态，不等于跨任务持久 Memory。""",
    "books/part-07-agent/76-rag.md": """RAG 从 top-k 相似度检索演进到 evidence admission 和闭环预算控制。Query、candidate generation、rerank、dedup、context allocation、answer attribution 与 abstention 是不同阶段；高相关不等于足够证据，shared index 的 population density 和跨租户 crowding 也会改变召回行为。\n\n更多检索可以提高 recall，却增加噪声、token 成本、污染传播和错误置信。系统应冻结 corpus/index/embedding revision，记录候选为何被选、模型是否实际使用证据，并在 coverage 不足或来源冲突时拒答。小语料、稳定查询或 exact lookup 场景中，简单 top-k 仍可能是更透明的 baseline。""",
    "books/part-07-agent/77-memory.md": """Agent Memory 从追加历史演进成受治理的持久状态系统。写入前要区分事实、计划、经验和派生摘要；读取要同时考虑 relevance、valid time、provenance、ACL 与版本；更新/删除需要 supersession、before-image、conflict visibility 和可恢复 transaction，而不是静默覆盖旧值。\n\n结构化、共享或可学习 memory 提高长期连续性，却引入污染、相关 evaluator bias、并发 writer、遗忘不完整和 retrieval drift。writer、verifier 与 reader authority 应分离；低置信 transition 保留旧版本和 raw trajectory，跨租户默认隔离。短任务或状态无法可靠验证时，不持久化往往比有损记忆更安全。""",
    "books/part-07-agent/78-tool-calling.md": """Tool Calling 从生成函数名和参数演进到 proposal→validate/simulate→authorize→execute→observe→recover 的 effect protocol。Schema 只描述接口；状态前置条件、principal、预算、幂等性、外部 side effect 和结果 receipt共同决定一次调用能否提交。\n\n模拟器、constraint decoder 和 recovery path 可以减少错误执行，却会引入环境差异、latency 和新的可信组件。emulator 成功不证明真实工具安全，文本 refusal 也不证明没有 effect；验证失败或结果不可逆时必须拒绝、sandbox 或人工批准。简单只读工具仍可采用更薄的调用路径。""",
    "books/part-07-agent/79-planning.md": """Planning 从一次性计划文本演进到可执行、可修正的搜索状态。节点要绑定前置条件、环境观察、候选 action、commit point、预算和 verifier；test-time search可以动态扩展候选或分配 thinking time，但只有环境证据才能提交下一状态。\n\n更多搜索提高找到可行路径的机会，却增加延迟、branch explosion、stale observation 和 verifier bias。deadline、风险或工具成本越界时应缩短 horizon、选择保守 plan 或交还 Workflow/人工；固定流程在环境稳定时仍比开放搜索更可预测。""",
    "books/part-07-agent/81-workflow.md": """Workflow 从顺序 prompt chain 演进为 durable dependency graph：logical step、artifact、tool effect、checkpoint、retry、compensation 与 human gate 都是可重放状态。Agent 可以提出下一步，runtime 持有执行和恢复，verifier 判断 artifact 是否满足前置/退出契约。\n\n更自动的 research、coding 或 dialogue loop 提高吞吐，却会累积 fabrication、stale dependency、重复 side effect和不可判定 claim。只有可机器检查的部分才能自动推进；不可见、不可修复或外部真实性不明的结果必须进入人工 owner。短、无副作用任务仍可使用简单 chain，但不能据此推断长任务可靠性。""",
    "books/part-07-agent/82-multi-agent.md": """Multi-Agent 从广播全部对话演进到 typed role、message、shared state 与 topology。收益来自独立证据和真正的责任分解；当错误相关时，多数票可能放大失败，因此系统还要保存 minority evidence、校准 verifier/flip precision，并把 communication 和 verification delay纳入调度。\n\n更多 Agent 增加探索和并行度，也增加趋同、冲突、消息成本、权限扩散和 deadlock。protocol runtime 可以检查兼容 emission、safety/liveness 和 delegation scope，却不能证明消息内容为真；低独立性或验证预算不足时，单 Agent、独立 proposals 或人工 adjudication 更合适。""",
    "books/part-07-agent/83-mcp.md": """MCP 把工具和资源发现标准化后，新的压力从“能否连接”转向“组合后是否仍满足身份、权限和数据约束”。单个 server/schema 通过检查不代表工具链安全；host需要对来源、capability、Data Facts、side-effect class 和跨 server 组合做 admission。\n\n统一协议降低集成成本，却扩大 supply-chain、confused-deputy 和组合权限风险。协议层只传递声明与结构，Platform/Security 才拥有信任和执行决策；缺少 provenance、版本或可撤销性时，应限制为只读、隔离会话或拒绝连接。专用直连接口在边界更窄时仍可共存。""",
    "books/part-07-agent/84-agent-platform.md": """Agent Platform 把模型调用扩展为有状态、可行动的生命周期控制面：model/tool routing、harness、workspace、observation、budget、policy、execution record 与 outcome receipt必须使用同一 run identity。开放任务还要求保存 harness history、specialization route、人工介入和 rollback，而不是只优化一次 benchmark。\n\n更丰富的平台可以跨任务复用能力，却增加 capture/retention、sandbox、routing drift 和 control-plane blast radius。模型或自动 controller只能提出 action 和资源分配；policy、environment verifier 与 release gate拥有提交权。简单 chat 或无副作用 assistant 不需要完整平台，但一旦进入持久 state 和外部 action，就必须沿 Context→Memory→Tool→Workflow→Evidence闭环。""",
    "books/part-01-worldview/05-what-neural-networks-learn.md": """模型内部表示从“能重构某个概念”走向“能被独立监督读出并在新 probe 上稳定复现”时，证据强度才真正上升。语言化解释、activation correlation 与 reconstruction score 可以提出候选机制，却不能单独证明模型在任务中使用了该表示；需要把 decodability、intervention、fresh-probe monitoring 与外部行为结果分开。\n\n更强的诊断提高可解释性，也会引入 probe capacity、label leakage 与 observer effect。解释器无法跨分布复现或 intervention 不改变行为时，应回退为相关性证据而不是因果结论；模型学到的表示仍由 data、objective 与 architecture 共同限定。""",
    "books/part-02-model/13-position-encoding.md": """位置表示从固定或旋转编码走向更长窗口时，必须区分静态相关、训练过程中通道如何形成，以及删除或扰动该通道后的因果效果。最终 probe 相似不等于模型真实依赖该位置通道，外推长度也不等于可用信息距离同步增加。\n\n更复杂的位置机制可以改善长度泛化，却增加数值精度、频率别名和训练—推理不一致。消融或长序列行为不稳定时，应回到已训练窗口、分段 Context 或显式检索；绝对、相对、RoPE 与 ALiBi 仍是不同 workload 下的条件分支。""",
    "books/part-02-model/14-self-attention.md": """Attention state 的经典分解保存 key 与 value，因为 query-key 决定路由、value 决定读取内容；新的因式分解可以把路由改写为 query-value 并减少缓存对象，但这同时改变模型参数化、训练目标和 runtime identity，不能被当作无语义变化的 KV 优化。\n\n更少缓存换来重新训练、kernel 支持与分布外稳定性风险。若等价性、质量或执行路径没有在目标模型上验证，标准 Q/K/V Attention 仍是正确 fallback；FlashAttention 等执行优化继续只拥有 IO 调度，不拥有模型语义。""",
    "books/part-02-model/18-decoder-only.md": """Decoder-only 的状态不仅是可见 token。Looped 或 latent reasoning 把部分推理迁入 recurrent hidden state 后，dense per-loop loss 只能约束 readout 可见方向；normalization 隐藏的尺度仍可能在 residual recurrence 中携带信息。训练 contract 因而要明确哪些 latent state 对 loss 可见、何时提交以及如何停止。\n\n减少显式 token 可以降低输出带宽，却增加不可观测状态、循环稳定性和调试成本。latent state 无法校准或行为审计失败时，应回到显式 CoT、固定 loop 或普通 autoregressive decode；减少 token 不等于删除推理状态。""",
    "books/part-03-multimodal-world-models/23-multimodal-representation.md": """多模态表示从简单拼接演进到有类型的共享空间后，系统必须同时管理任务贡献与 observation reliability：一个 modality 对任务有用，不代表它在当前样本中可靠。时间、空间、modality、encoder revision 与 provenance 因而成为 representation identity 的一部分。\n\n更细的 routing、uncertainty weighting 与 token compression 能节省共享容量，却会引入 calibration drift、语义 anchor 错误和跨语言/流式累积偏差。融合证据不足时应保留 modality-specific path、原始输入或保守 late fusion；native multimodal training 仍是多目标 capacity allocation，而不是自动抹平 modality boundary。""",
    "books/part-04-training-system/29-sft.md": """SFT 从完整 response 的统一 token loss 演进到有条件的 supervision allocation：syntax-complete block、under-modeled tail、shared-perception span 或 teacher/student aware span 都是在回答“哪些示范信号值得当前 update 消费”。样本选择器可以提出稀疏监督，但 objective 与最终能力回归仍拥有提交权。\n\n更集中的梯度提高有效预算，却可能丢失 easy-sample regularization、放大 selector bias 或造成能力回退。选择器未校准、共享感知假设不成立或 tail 过窄时，应回到完整 response SFT；SFT 继续拥有行为模仿，偏好与长期 credit 交给后续分支。""",
    "books/part-04-training-system/32-ppo.md": """PPO 的 critic 从通用 return estimator 演进到因果 credit、privileged input 与长度自适应 GAE 后，核心仍是把 rollout outcome 转成可控 advantage，而不是把 value estimate 当成真值。结构化环境或额外观测可以减少 delayed-reward ambiguity，但必须与 policy 可用信息和 evaluation boundary 分开。\n\n更强 critic 降低方差，也会增加偏置、泄漏、额外模型状态和训练成本。因果假设不成立、value range 漂移或 privileged signal 不可部署时，应回到标准 GAE、更保守 clipping、GRPO 或 SFT；Reward correctness 仍不由 PPO 本身解决。""",
    "books/part-04-training-system/34-dpo.md": """DPO 把 online rollout 与 critic 移出主路径后，训练状态集中到 preference pair、reference policy、beta 与 campaign history。重复 campaign 说明“保留旧能力”与“积累下一轮如何训练的知识”不是一件事，strategy/evaluator memory 需要独立版本；preference noise 与 update scale 也必须拆开诊断。\n\n更薄的运行时换来对数据覆盖、reference identity 和 beta 的更高敏感度。chosen probability 下降、噪声主导或 campaign 间目标冲突时，应回到 SFT、人工数据修复或 online PPO/GRPO；DPO 是偏好优化的条件分支，不是 RLHF 的无条件替代。""",
    "books/part-04-training-system/35-checkpoint.md": """Checkpoint 从周期性磁盘快照演进到异步保存、内存 recovery generation 与逻辑 shard 替换后，恢复单位从整个 job 缩小为可证明一致的 committed state。只有不可重建的 optimizer/model state 需要复制，失败节点可按 shard identity 接管；但 corruption、错误分类和全局依赖仍要求持久快照。\n\n更快恢复换来 spare capacity、复制流量、generation tracking 与更复杂的故障语义。状态一致性无法证明或失败不是 fail-stop 时，必须回退持久 checkpoint/restart；load 成功依然不等于 RNG、optimizer、data cursor 与外部副作用都正确恢复。""",
    "books/part-04-training-system/38-pipeline-parallel.md": """Pipeline Parallel 从固定 stage 与同步 microbatch schedule 出发，因为它最容易保持 forward/backward 依赖；层成本、异构链路或动态 workload 变化后，stage balance、schedule 和 activation movement 需要联合优化。runtime 可以重排 microbatch，却不能改变 global batch、loss weighting 或 tied-weight consistency。\n\n更动态的 pipeline 降低 bubble，却增加 schedule state、跨 stage failure、activation pressure 和可复现性成本。模型较小、stage 稳定或通信主导时，固定 1F1B/GPipe 仍更可靠；任何 source-specific schedule 都必须在相同训练语义和收敛合同下比较。""",
    "books/part-05-inference-system/46-continuous-batching.md": """Continuous Batching 的调度量子最初是 autoregressive token iteration；block diffusion 等生成范式把它改成 denoise cycle，完成 block 后可立即回收 slot，并在不同 denoising state 间重新 packing。scheduler 必须同时约束 token、memory 与 provisional-state budget，而不是只数 active requests。\n\n更细的 slot reuse 提高 occupancy，却增加异质状态对齐、临时结果与 commit boundary。denoise state 不兼容、质量合同不清或 batch 重排成本过高时，应回到同阶段 batching 或普通 AR iteration；determinism 与 preemption 仍需独立验证。""",
    "books/part-05-inference-system/47-pagedattention.md": """PagedAttention 从解决连续 KV 分配碎片，演进到 prefix sharing、copy-on-write 与可编程 sparse index 后，page table 成为请求可见性的状态边界。Agent workload 可以通过索引选择减少读取，但 kernel 只能执行已声明的 sparse pattern，不能证明被跳过的信息不重要。\n\n更灵活的分页和稀疏读取降低 HBM 浪费，却增加 metadata、index drift、共享隔离和数值验证成本。pattern 未校准、请求高风险或 page identity 不一致时，应回到 dense attention 或私有 KV；分页优化继续保持模型语义不变这一基本合同。""",
    "books/part-05-inference-system/50-vllm.md": """vLLM 这类 engine 的职责从单一 CUDA Serving 扩展到多 backend 后，执行身份必须包含 compiler/runtime version、dispatch target 与真实 kernel path。平台声明“允许使用某 accelerator”不能替代 observed dispatch receipt，否则性能和正确性都无法归因。\n\n更多 backend 提高可移植性，却增加 feature gap、fallback silence 与 profile drift。目标设备或 kernel 未被运行时证据确认时，应回到已验证 backend 或明确标记 CPU/GPU fallback；framework 名称本身不拥有硬件执行事实。""",
    "books/part-05-inference-system/51-sglang.md": """SGLang 从语言程序与 Radix cache 演进到异构多模态执行图后，workflow activation、跨角色 tensor/KV identity 与 physical execution 需要由可分离但可提交的 Control Flow、Data Flow、Compute Flow 共同表达。全局 KV takeover 可以复用更多状态，却不能模糊 owner 与 eviction authority。\n\n更强 orchestration 增加 metadata、layout compatibility、atomic eviction、故障恢复与 runtime coupling。跨角色状态无法证明兼容时，应回到阶段内 cache、显式 data edge 或独立 engine；一次 pipeline 成功不能替代受控性能与恢复验证。""",
    "books/part-05-inference-system/52-dynamo.md": """Dynamo 类分布式 runtime 从 queue/KV-aware routing 演进到显式 state edge 后，data edge 与 KV-state edge 必须分别表达 compatibility、fork、compose、transfer、evict 与 recompute policy。edge/cloud split 还要求把语义 work 与网络/算力资源联合路由，而不是把模型切分当成固定部署常量。\n\n显式状态编排提高复用和可迁移性，却增加全局 index、epoch、无线/网络预测和失效一致性。状态 identity 或资源模型失准时，应回到本地执行、固定 split 或无共享路由；本章拥有 runtime plane，具体 PD handoff 继续交给第 55 章。""",
    "books/part-05-inference-system/53-kserve-llm.md": """LLM Serving topology 从固定 model Pod 演进到 base-plus-extension 与复合 model graph 后，控制面需要表达共享 base、按请求装载的 adapter/extension、named walks、loop/stream 与 component placement。声明式 topology 拥有 desired state，runtime 才拥有实际 cache、walk 与执行状态。\n\n更灵活的 graph 提高复用，却增加 extension compatibility、placement、冷启动和动态循环治理。graph 无法冻结、extension 身份不明或 controller 不支持恢复时，应回到固定 stage DAG 或独立 deployment；第 61 章继续拥有通用服务资源生命周期。""",
    "books/part-05-inference-system/55-pd-disaggregation.md": """P/D 分离从固定两池演进到网络、KV tier、MoE expert、power 与 accelerator 都参与的条件化切分后，handoff state 必须绑定 request、segment、KV format、precision、pool epoch 与 fabric path。Spectrum/heterogeneous/async 分支分别移动字节、角色与 barrier，但都不能改变已提交 token 语义。\n\n分离可改善阶段利用率，却增加传输、量化、拥塞 externality、pool ratio 与 failure recovery。handoff 成本超过计算收益、共享 fabric 饱和或 state identity 不一致时，应回到 colocated serving、固定角色或重算；P/D/A/F 是共存分支，不是层层取代。""",
    "books/part-06-ai-infrastructure/62-gateway.md": """Gateway 从认证与负载均衡入口演进到跨站点、跨 provider 和 Agent protocol 的策略控制点后，routing decision 必须绑定 model/provider identity、capability、queue/runtime、WAN state、privacy policy、session 与 receipt。Gateway 可以选择路径，却不能同时拥有不可验证的明文和执行 authority。\n\n集中策略提高复用与治理，却增加 session stickiness、transport translation、enclave attestation 和单点 blast radius。receipt、身份或重试幂等性无法证明时，应回到直连、固定 provider 或人工批准；engine scheduler 继续拥有 token work，GPU scheduler 继续拥有 Pod placement。""",
    "books/part-06-ai-infrastructure/71-multi-tenant.md": """多租户从 Namespace 与 quota 隔离扩展到共享 resident backbone 后，兼容的 forward prefix 可以 group batch，但 action head、optimizer、rollout、policy version 与私有 loss/backward 必须在 tenant 边界前拆分。共享计算不等于共享训练状态或发布权限。\n\n更高利用率换来侧信道、错误聚合、noisy neighbor 和 provenance 复杂度。prefix、policy 或 trust level 不兼容时，应回到独立 batch、独立 process 或专属 GPU；隔离强度必须随数据、状态和副作用风险提升。""",
    "books/part-06-ai-infrastructure/73-production-best-practice.md": """Production 从固定 traffic sweep 与人工配置演进到 telemetry→proposal→sandbox evaluation→guarded apply→rollback 的闭环后，模型或 Agent 只拥有候选变更，control plane 持有版本与提交权。capacity search 也必须绑定 warm-up、arrival、artifact 与 SLO，而不是把单点吞吐当作可发布容量。\n\n自动闭环缩短调优周期，却增加试验流量、错误 cost model 与回滚状态。证据不足、blast radius 不可控或 rollback 未演练时，应停在 shadow/canary 或人工审批；生产成熟度由可恢复的决策链衡量，不由工具数量衡量。""",
    "books/part-07-agent/80-reflection.md": """Reflection 从生成一段自评文字演进到可治理的 skill/strategy revision 后，candidate lesson、decision history、held-out evaluation、rejected alternative、promotion 与 rollback 必须分离。随机 masking 或新任务 slice可以估计某条 skill 的增量价值，但 verifier 与 policy 不能在同一证据上共同漂移。\n\n持久反思提高跨任务复用，却会引入自证偏差、skill dependency、权限扩散和错误经验固化。held-out 失败、因果贡献不稳定或新任务回退时，应拒绝 promotion、恢复旧 skill 或交还人工；短任务的一次反思仍只是一条候选诊断。""",
}

SPINE_HEADING = "## 从机制演进到系统设计"
LEGACY_SPINE_HEADING = "## 集成后的机制主线"


BLOCK_START = re.compile(
    r"^<!-- ((?:recovered-daily|june29-owner|daily-20260627|daily-20260628)[^:]*:[^:]+):start -->$"
)


def move_template_blocks(text: str) -> tuple[str, list[str]]:
    lines = text.splitlines()
    review = lines.index("## Review notes") if "## Review notes" in lines else len(lines)
    blocks: list[str] = []
    index = 0
    while index < review:
        match = BLOCK_START.match(lines[index])
        if not match:
            index += 1
            continue
        end_marker = f"<!-- {match.group(1)}:end -->"
        try:
            end = lines.index(end_marker, index + 1)
        except ValueError as exc:
            raise ValueError(f"missing marker {end_marker}") from exc
        blocks.append("\n".join(lines[index : end + 1]).strip())
        del lines[index : end + 1]
        review -= end + 1 - index
        while index < len(lines) and not lines[index].strip() and index > 0 and not lines[index - 1].strip():
            del lines[index]
            review -= 1
    return "\n".join(lines).rstrip() + "\n", blocks


def insert_spine_and_records(text: str, spine: str, blocks: list[str]) -> str:
    text = text.replace(LEGACY_SPINE_HEADING, SPINE_HEADING)
    if SPINE_HEADING not in text:
        anchor = next(
            (candidate for candidate in ("## 自检问题", "## 面试与自检问题") if candidate in text),
            None,
        )
        if anchor is None:
            raise ValueError("chapter lacks a supported self-check anchor")
        text = text.replace(anchor, f"{SPINE_HEADING}\n\n{spine}\n\n{anchor}", 1)
    if blocks:
        text = text.rstrip() + "\n\n### Source-family integration record\n\n" + "\n\n".join(blocks) + "\n"
    return text


def transform(root: Path, relative: str) -> tuple[str, bool]:
    path = root / relative
    before = path.read_text(encoding="utf-8")
    moved, blocks = move_template_blocks(before)
    after = insert_spine_and_records(moved, SYNTHESIS[relative], blocks)
    return after, after != before


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()

    changed = []
    for relative in sorted(SYNTHESIS):
        after, differs = transform(args.root, relative)
        if not differs:
            continue
        changed.append(relative)
        if args.write:
            (args.root / relative).write_text(after, encoding="utf-8")
    print(("updated" if args.write else "would update") + f": {len(changed)} chapters")
    for relative in changed:
        print(relative)


if __name__ == "__main__":
    main()
