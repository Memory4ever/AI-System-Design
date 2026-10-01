# 2026-09-29 Daily：有限尾项 B 的原文／Owner 建议

本附件只处理已独立准入的六个家族：2609.34380、2609.33889、2609.33477、2609.34785、2609.35508、2609.35587。窗口为 `2026-09-28T09:00:00+08:00 → 2026-09-29T09:00:00+08:00`。不扩池、不重跑 N1–19、不修改 Books、正式日报或学习状态；下列 I 是待非作者 PRE 审核与实际写回的建议，不是已集成或 Daily 验收。

日期依据复用本日 `screening-checkpoint.md` 的已校准 primary New 身份：DPS 为 DC Tue29 New [66]，SparsityCrossover 为 LG Tue29 New [1186]，SuffixReplay 为 AI Tue29 New [1138]，BEHAVE 为 AI Tue29 New [997]，Argus 为 OS Tue29 New，CUTLASS 为 LG Tue29 New [918]。不同抓取的列表编号不混用。结合 exact-v1 身份与官方正常公告日程，首公开批次为 `2026-09-29T08:00:00+08:00`，在窗口内；下列 Submitted 原值只绑定版本，不能单独证明首公开。已实际读取六项 exact-v1 方法、必要评价及关键反侧；未实施论文或复现实验。没有访问受阻项。

| 家族 | 评分（Design Delta／System Reach／Durability） | 实际审阅 | 最终建议 |
| --- | --- | --- | --- |
| DPS | 2+2+3=7 | 深入：IV-A–D、Alg.1、V、必要实现／质量反侧 | I，INFER-GPU-MEMORY |
| SparsityCrossover | 2+1+3=6 | 设计反证深入：§3–7、共同 kernel、质量及 amortization | I，INFER-GPU-MEMORY |
| SuffixReplay | 2+2+3=7 | 深入：§4–7、§9、近似／exact 与负侧 | I，INFER-KV-CACHE |
| BEHAVE | 2+1+3=6 | 标准并按拟采用命题深入：§3–4、B.4–5、可信边界 | I，PLATFORM-EVALUATION-SYSTEM |
| Argus | 1+1+3=5 | 标准：§2–4、ablation 与 missing-tree 反侧 | 仅报告，PLATFORM-TRACE 已有拟采用原则 |
| CUTLASS selector | 2+1+2=5 | 标准并按 owner 差额深入：§3–5、候选采样／迁移负侧 | I，INFER-TENSORRT-LLM |

## 1. DPS：Dual-Mode Precision LLM Serving with Semi-Unified Memory

- 原文：[2609.34380v1](https://arxiv.org/html/2609.34380v1)；[身份页](https://arxiv.org/abs/2609.34380v1) Submitted 原值 `Mon, 28 Sep 2026 05:55:33 UTC`。题名、版本与上述 DC primary New 对应。
- 方法定位：IV-A–D／Alg.1 的 Semi-Unified Memory 把 persistent FP8 权重与 residual 权重分开，后者和 KV 共享物理页；pinned CPU residual 是 full 模式恢复来源。full→fast 不先重载模型，fast→full 分块异步 H2D，全部 residual tensor 恢复后才提交模式切换。一个 forward/batch 内各层用同一精度，不保证一个请求全程同精度。CUDA VMM 中 KV 的虚拟 tensor 保持映射，避免 scheduler 回收时仍有 in-flight KV 读取；residual 的可用映射与共享页状态由 manager 管理。不是普通“任意页动态降位”。
- 评价／反侧定位：V 以 vLLM 0.18.0、H100 80GB 的三个 MoE（Phi-3.5、Qwen3-30B-A3B、GLM-4.7-Flash）比较静态 FP16／FP8；BurstGPT／Azure 为缩放到达 trace，Gamma CV=2 是另一受控负载。联合 SLO 是 TTFT≤2000ms 且 max TBT≤5×Tbase，capacity 的门是≥90%请求满足联合 SLO；effective pass@1 是 SLO attainment 与实际 served pass@1 的乘积，不是纯模型准确率。低压力有无收益与静态 FP8 达到相近 SLO 的反侧；七个离线任务平均不能证明 FP16 等质、逐请求等价或 dense 模型普遍成立。full 恢复不重算已用低精度生成的 token 或其历史状态。
- Actual owner：`INFER-GPU-MEMORY` → `books/part-05-inference-system/54-gpu-memory.md`（ROADMAP 路径）。“Weights 与 KV 的联合 HBM 预算”及 2605.28095 已解释 desired/committed precision、先降位再释放／先加载再升位；HBM 分区／VMM 已有。但没有 persistent+residual 的非对称共享、KV 映射不随逻辑 free 撤销，以及 batch 模式恢复不撤销请求历史。Ch49 拥有量化 kernel，不另立精度策略 owner；Ch55/56 继续拥有容量／调度。
- 最终建议：窄 I，插入现有 Weights/KV 联合预算段，保留原 committed-state 机制，不以论文名称建新章。以下两段为 literal 提案。

> 固定精度和固定 weight/KV 分区，在质量优先、流量稳定时最容易解释，也避免运行中重载权重。突发请求让 KV 挤满 HBM 后，可以把可独立读取的低精度权重长期保留，只让高精度 residual 与 KV 共享物理容量：降到 fast 模式释放 residual 的使用权，回 full 模式则从 host 分块恢复 residual，全部恢复完成后才在 forward 边界切换。这个提交边界不同于单个请求边界；同一请求前后可能使用不同模式，恢复高精度不会撤销已经生成的低精度历史。
>
> 逻辑 free 也不等于可立即撤销所有虚拟映射：若 worker 仍有 in-flight KV 读取，共享页 manager 必须协调用途变化，而不能让 scheduler 回收直接破坏读地址。[DPS v1 IV–V](https://arxiv.org/html/2609.34380v1)采用长期 KV 映射、residual backing 与双模式 CUDA graph，因而增加 host residency、PCIe 传输、状态管理和 graph 成本。其 effective pass@1 同时含 SLO 与质量，不能证明精度等价；静态 FP8 有时已满足压力目标，低压力也可能不获益。质量门不允许模式混用、恢复带宽不足或共享页状态不可靠时，继续使用静态精度及明确的 KV 容量／admission 限制。

## 2. Where Activation Sparsity and KV-Cache Sparsity Cross in LLM Decoding

- 原文：[2609.33889v1](https://arxiv.org/html/2609.33889v1)；[身份页](https://arxiv.org/abs/2609.33889v1) Submitted 原值 `Sun, 27 Sep 2026 20:11:05 UTC`。首次公开不是按这个周日提交时间授予，而是上述 LG Tue29 primary New 批。
- 方法定位：§3–5 在 batch=1 下把 projection weight 读取视为常量 P、KV 读取视为随 n 增长，推出 `n* = P(1-rP)/(2 hKV dh (1-rKV))`；字节数／dtype 不同需带相应比例。两分支都保留完整权重与完整 KV，只减少读取，所以不是 allocated HBM 容量收益。batch 增大时 activation union 保留率 uB 与每批 KV 读取共同改变交点。独立校准 projection/KV kernel 成本后才得到 latency 交点，不能直接把 byte crossing 当最优切换长度。
- 评价／反侧定位：§4 的同一 split-K dense／sparse kernel、compiled decode 和实际文本 dense prefill 控制了 dense 路径效率；同一种 30% window 在 masked/fused/split-K 对照的不同巨大 speedup，不能解释成 policy 本身改变。A100／A6000、Llama3.1-8B 主实验及有限其他模型，50-token decode 与独立 fresh process repeats，不是线上 tail SLO。§5 的固定 window 困难远距检索反侧说明 PPL 相近不足以授任务质量；选择策略的 scoring/gather 一次成本须按实际输出长度摊销。等 PPL 预算会移动交点，名义保留率不能当质量匹配。§7 混合负载收益主要也可来自固定 composition，并未证明复杂 dispatch 必要。
- Actual owner：`INFER-GPU-MEMORY` → Ch54 “减少 Bytes”已涵盖 token/element retention、索引／ranking 成本，却没有恒定 weight-read 与增长 KV-read 的交点、完整驻留下的“仅少读”权限，以及共同高效 dense 路径／质量预算后的比较。Ch44 只交接 decode 的带宽基础；Ch49 只交接 kernel 实现，避免两处复述选择规则。
- 最终建议：窄 I，在减少 Bytes 的两种稀疏路径比较处补选择边界，不把一个受测 context 长度写成通用 threshold。literal：

> Activation sparsity 和 KV sparsity 都可能减少 decode 读取，但省掉的对象并不随 context 同样增长：batch=1 时 projection 权重读取近似固定，KV 读取随已缓存 token 数增长。因此短 context 更可能受益于少读权重，长 context 更可能受益于少读 KV；batch 增大又会让不同请求的 activation 选择取并集，削弱 weight-read 节省。这个 byte-budget 交点只是起点，还要加入各自 kernel 的固定成本、实际 dtype、layout 和选择开销。完整权重／KV 仍驻留的实现，不能把少读的 bytes 宣称为可分配 HBM 容量。
>
> 决定运行分支时，应在同一高效 dense kernel 上测两条 sparse 路径，以相同任务质量预算约束保留率，再计入 scoring、gather 和生成长度带来的摊销；更换低效 dense baseline 会人为放大同一 policy 的收益。[Sparsity Crossover v1 §3–7](https://arxiv.org/html/2609.33889v1)显示固定 window 的小 PPL 差异仍可伴随远距检索失败，选择型策略也有一次构造成本。批量、质量 gate 或输出长度改变时应重测边界，而不是只按 context 长度切换；短输出、稀疏 kernel 开销过大或质量不稳时，保留 dense 读取与简单固定 composition。

## 3. Just Let Linear States Forget the Distant Past: Prefix Caching via SuffixReplay for Hybrid LLMs

- 原文：[2609.33477v1](https://arxiv.org/html/2609.33477v1)；[身份页](https://arxiv.org/abs/2609.33477v1) Submitted 原值 `Sun, 27 Sep 2026 11:43:56 UTC`，对应 AI Tue29 primary New。
- 方法定位：§4–6 保存连续 linear-layer group 入口的稀疏 hidden-input anchors，命中时每组独立重放最近 anchors，跳过已有 full-attention KV；依赖模型的 decay/forgetting，而非恢复一个精确旧 recurrent state。受测 anchor 密度为 1/16，64-token 页保存末四行，`k=min(0.05n,kmax)` 的 k 是 replay anchors，不是原始 token。anchor sidecar 与 radix node 同 admission/eviction 生命周期，却使用独立物理 pool，因为仅 replay 时访问；页填满／传输完成后发布，先异步取 anchor 再 backfill KV，消费者等待对应 replay stream。有限 graph buckets 外回 eager；live continuation state 可直接复用，不强制所有命中近似 replay；不对齐、缺失、未发布、pending full-prefill 或不支持的 hook 回完整 prefill。
- 评价／反侧定位：§7 比较同 checkout SGLang 0.5.18 native checkpoint/cache；H80080GB 单卡、Qwen3.5-4B BF16／Qwen3.6-27B FP8，OLMoHybrid7B 只有质量测试，不能并入 serving 吞吐。matched quality ratio 不等 token/state equality，OLMo 的 RULER 平均 91.4% 及更低单项反侧限制“≥94%”概括。graphs 和保留 margin 占额外内存，不能只算 anchor bytes。§7.3 同步固定长度 exact-aligned native hits 有 replay 开销反例；交错变长请求去掉这个差距不授普遍不退步。主性能 budget 在 sweep 前固定，离线模型／任务预算也不证明跨 checkpoint 无损。
- Actual owner：`INFER-KV-CACHE` → Ch45 已有 2605.05219 的稀疏 **exact state checkpoint + 缺失 suffix**、2608.30386 的 weight-derived retention horizon／省略 state units + bounded replay，及 initializer/rollback 语义。差额不是再宣称“近似 replay 可省内存”，而是 **按 linear group 保存输入而非旧 state、各组独立 replay 与 attention KV 分工、sidecar 发布边界**。Ch22 保持 model 的 forgetting／state 原理 owner，Ch54 不重复 cache 生命周期。建议接在近似 state-units 分支后，先对照前面的 exact checkpoint，再接视频 cache。
- 最终建议：窄 I，不覆盖 exact checkpoint、不把 approximate resume 当 committed transcript 的精确 rollback。literal：

> 前面的稀疏 exact checkpoint 必须从真实旧 state 回放缺失区间；另一条近似分支不保存那个 state，而在每组连续 linear layers 的入口保留近期 hidden-input anchors。若该模型的 recurrent 更新能逐渐遗忘远处历史，Runtime 可以从短输入尾部重建近似边界状态，各 linear group 独立 replay，full-attention 层继续使用已有 KV。它与按 retention horizon 省略 state units 的方法也不同：主要缓存对象变成 group input，replay budget 必须绑定模型与质量条件，不适用于缺少有效衰减的任意 recurrent 架构。
>
> Anchor sidecar 可跟随 prefix tree 的 admission／eviction，却应区分物理放置与发布时点：只有页写完且传输完成的 anchors 才可被命中，消费者还须等待相应 replay stream；缺页、未发布或 hook 不支持时回完整 prefill，现成 live state 则不必再近似重建。[SuffixReplay v1 §4–7](https://arxiv.org/html/2609.33477v1)的配对任务分数不证明 token 或 state 等价，某些质量项与同步 exact-hit 性能仍退步，CUDA graphs、pool 及额外 headroom 也占成本。需要精确 continuation、质量预算失败或 replay 不划算时，保留 exact checkpoint／完整重算，不把近似恢复授为撤销历史的能力。

## 4. BEHAVE: Functional Behavior Modeling Enables Self-Improving Agents for Hardware Design and Verification

- 原文：[2609.34785v1](https://arxiv.org/html/2609.34785v1)；[身份页](https://arxiv.org/abs/2609.34785v1) Submitted 原值 `Mon, 28 Sep 2026 09:57:29 UTC`，对应 AI Tue29 primary New。
- 方法定位：§3–4 的 agent 共同产生 RTL 和 BehaviorIR，可在开发期检查二者一致，但最终分别对 hidden gold BehaviorIR 验证，不能让自写 reference 给自写 design 作真值。评估按 specification 允许的 transaction timing 比较 accepted input/reset/output histories，不要求与 gold 同 cycle；B.4 明确默认保序，只有 specification 授权才按 ID 或允许的 unordered matching 比较。时序限制仍单独检查，不是任意忽略 latency。
- 评价／反侧定位：seeded random/edge 与 goal-guided solver 构造有限 StimulusPool；score 内的 pass 是该池无 output mismatch 且无 safety-goal 触发，coverage 单独报告。bounded proof／optional exact analysis 只授权已编码的固定 bounds／trusted replay/query，unknown 不能当 pass，事后分析不改变评分池。B.5 的 stimulus generation／analysis 比 replay 支持面更窄，external writable memory、部分 endpoint／clock／schedule 不普遍支持。600 个人审任务 540/60 划分、60-turn／128K 限制和同 hidden gold 支持受限 agent workflow 比较；55→75 的训练曲线存在 18 vs 40 updates／不同池，不采独立算法因果。PPA 只是固定工艺库／频率／工作负载的 synthesis 与 cycle 评价，不是真实芯片验收。
- Actual owner：`PLATFORM-EVALUATION-SYSTEM` → Ch66 “先验证 Benchmark 的 Reference Artifact，再比较 Agent”已有 reference 可复现≠语义正确，以及允许多种合法实现、oracle 不得扩张需求；还没有 **允许 timing 差异的 transaction trace 比较与 design/reference 双产物分别过 hidden gold**。Ch65 的 runtime 和 Ch67 的观测都不是 oracle owner。建议在 reference/oracle 合法多实现的段落附近插入，不在硬件应用处另建 owner。
- 最终建议：窄 I，采用评价合同，不采用“自我改进”普遍结论。literal：

> 可复现的 reference 仍可能把合法实现误判：例如 specification 只约束输入接受、输出内容、顺序与允许 latency，而 reference RTL 恰好用某个固定 cycle 数。此时 oracle 应先把 transaction、reset 和 handshake 映射固定下来，在 specification 允许的 timing 差异内比较行为，并另外检查真正的时序约束；默认顺序不能静默改成无序集合。对 agent 同时生成 design 与 behavioral reference 的流程，二者一致只是一条开发反馈，最终还须各自对独立 hidden gold 验证，避免共同犯错变成自授正确。
>
> [BEHAVE v1 §3–4/B.4–5](https://arxiv.org/html/2609.34785v1)用 typed BehaviorIR 与有限 stimulus pool 实现这条路径，但无 mismatch 的 pass 不等于程序语义完备；coverage、bounded proof 的编码范围和 unresolved/unknown 应分开呈现。Protocol adapter、goal/query 编码和更充分的 replay 增加成本，generation／analysis 的支持面也小于执行回放。没有可信映射、涉及未支持 memory／clock 行为或超出固定 bounds 时，保留人工 spec 审核、已验证 reference 与任务专属测试，不能把受限 agent 分数或合成 PPA 当硬件生产成功。

## 5. Argus: Agentic, Reference-Calibrated, Tree-Guided, System-Software-Level Bottleneck Localization

- 原文：[2609.35508v1](https://arxiv.org/html/2609.35508v1)；[身份页](https://arxiv.org/abs/2609.35508v1) Submitted 原值 `Mon, 28 Sep 2026 16:05:47 UTC`，对应 OS Tue29 primary New。
- 方法定位：§2–3 在同 workload 的 idle system 测 RMV，再在受干扰状态测 PMV；Δ=PMV−RMV 的经验阈值驱动离线 Linux kernel execution-path tree 的逐层定位。每层共用 multiplexed eBPF probes／map，verifier 错误经 ReAct 修复；tree 约束合法分支，reference 才给异常差额，不是把所有 counter 交给 LLM。未给一般统计异常保证或反事实因果认证。
- 评价／反侧定位：§4 为五 victim×四 perturber×三 runs 的 60 个刻意 interference 案例；Argus 1/60 wrong vs plain 27/60、tree-only31/60、tree+probe19/60，不授生产 false-alarm 率。微基准 49ns count／201ns latency probe 是指定 fault handler 的高频测量，不是全系统无开销。pf_cow 的 3/3 abstain 原因是 tree 缺 mmap_lock/slab/RCU；“未定位”不能证明没有 bottleneck。llama.cpp 案例只证明本地 OS fault 路径诊断，未披露完整 inference precision/length/batch/SLO，不能作模型 serving 性能证据。
- Actual owner 对照：`PLATFORM-TRACE` → Ch69 的 semantic-region/profiler-round reference 已要求同观测对象／reference；successful reference-flow deviation 段已把差额降为因果候选；call-chain tree + controlled replay/config intervention 段已限定路径候选与唯一原因分离。Ch49 也已有 kernel 指标不能跨层授 root cause。Argus 的 idle calibration、静态三级树、multiplexed probes 是可检查的局部实现实例，但拟采用的长期命题“同 workload reference 校准、路径树缩小范围、缺树时 abstain 不等健康”已有 owner 推理链；其受限实验不能升级为更强一般保证。
- 最终建议：**仅报告／Books No Change**。不称全文既有，因为具体实现与 60-case ablation 是本次新证据；也不把小数据诊断提升为新通用层。日报可保留独立 5 分标准审阅与 missing-tree 反侧，不删候选、不降分、不写 I literal。

## 6. Hardware-Aware Features for CUTLASS Kernel Selection

- 原文：[2609.35587v1](https://arxiv.org/html/2609.35587v1)；[身份页](https://arxiv.org/abs/2609.35587v1) Submitted 原值 `Mon, 28 Sep 2026 16:39:31 UTC`，对应 LG Tue29 primary New。
- 方法定位：§3 不直接拿 raw template knobs 作输入，而静态推导 problem×candidate×hardware 的 wave/tail、LLC working-set/re-streaming、SMEM/register occupancy 和 pipeline fill/amortization 特征；部署无需执行候选或采 counters。408 个 BF16 candidates×17 shape groups 的离线 GH200 counters 用于选择这些机制，并在同 shape/layout 内分析相关，避免跨 shape 的规模混杂。模型学习有限合法 catalog 内的 ranking，不给绝对硬件时间或任意 kernel 最优保证；这些特征也是代理估计，不是执行测量本身。
- 评价／反侧定位：§4–5 共 4.9M measurements、GH200、指定 CUTLASS commit／CUDA13.1，warmup、repeated timings 和大于 L2 的 operand pool 控制。训练按 base shape 把四 layouts 一同划分，防 shape leakage；候选75%来自静态偏好、25%其他，训练“best”只是 shortlist best，而68组近全量 oracle 的 regret 才是另一个评价。6.2/6.4% vs nvMMH17.3% 是该测集；analytical proxy63.7% 与 ridge23.7% 反侧说明硬件解释不自动变好。Transfer 需目标域 measured shapes fine-tuning；FP8 success-only速度必须连同 coverage65.4/73.0%呈现，fusion有0.97/1.00×及 DeepBench structural>full 的反侧。固定 swizzle/rasterization/split-K 限定候选域，不能推总 runtime SLO 或全部 epilogue/precision 胜出。
- Actual owner：`INFER-TENSORRT-LLM` → Ch49 cuBLAS dynamic kernel choice 段已有 opdesc、shape/layout/precision/workspace，WaveTune 已有 macro/micro wave 与 anchor profiling，tactic cache／retile portfolio 已要求 provenance、feature schema 和 runtime eligibility。但尚未承载 **由 candidate 推导硬件行为代理而非 raw knobs 的 execution-free learned ranking、shape-group 验证与 coverage 共同授选择权**。Ch54 不重复选择器，Ch66 只交接评价协议。建议接 WaveTune/内核选择段，保留 vendor heuristic／实测 autotune。
- 最终建议：窄 I，不把所有 static estimate／learned selector 当更优，literal：

> Vendor heuristic 和实测 autotuning 在候选不多、平台固定时合理；问题是候选变大或每个新 shape 都测量过贵。一个不用执行候选的分支，是从 problem、kernel 配置与硬件常量推导它将诱发的 wave/tail、cache working-set、occupancy 和 pipeline 开销，再学习候选排序，而不是让模型从 raw tile knobs 猜物理后果。这里输出只是在已验证合法 catalog 中的选择，不是绝对运行时间或开放候选空间的最优性；部署免测也不等于训练／profiling 免费。
>
> [Hardware-Aware CUTLASS v1 §3–5](https://arxiv.org/html/2609.35587v1)还要求把同 base shape 的 layouts 共同留出，区分训练 shortlist-best 与近全量 oracle，并将选择 regret、合法候选 coverage 一起验收。特征 schema、硬件常量、dtype／fusion 和 catalog 改变时，需要绑定 revision 与目标域测量；success-only speedup 不能掩盖无可选 kernel，迁移与 fusion 也并非总胜出。离线测量、合法性过滤和模型维护仍有成本，缺覆盖、漂移或预测退步时回 vendor heuristic／有 provenance 的实测 autotune，不授 learned selector 跨精度无条件选择权。

## 交接状态

六项 exact-v1 必要源及 actual owner 对照已完成，建议五 I／一仅报告；未做独立非作者 PRE，未写 Books，未做 actual POST，未更改正式分母或 Daily acceptance。未 stage、commit、push；只新增本附件，保护原有工作树。评分未因时间、访问或 Books 决定下调。所有性能／质量数均为论文披露条件，不是本项目运行结果。

## 追加：Tail A 三项 actual POST（非写入作者）

复用范围：root 本轮已对 PolyCIM、ToolWait、PRISM 完成非作者 exact-v1→owner PRE 并实际写入的明确交接；核对 `V3_TAIL_A.md` 对应方法、反侧、owner 差额与两段 literal。此次只核实际正文、论点权限、marker 与前后边界，未重读未变原文，不把该复用说成新 Source Review；本 reviewer 没有写这三份 Books。以下是 actual POST，不替代本附件六项自己的 PRE／写后审核。

| 家族／POST | 实际正文位置 | Literal 与 marker | 前后与采用边界 |
| --- | --- | --- | --- |
| PolyCIM 2609.34351：PASS | Ch49:103/105，两自然段 | 与 Tail A 两段内容一致；`SF-2026-ARXIV-2609-34351` 唯一一次 | 原 Nautilus scalar/VR/MA 与 repair/cost 两段保留；新段在其后、Persistent Executor 前。只补 non-axis reuse→affine realignment→有限 CIM/layout；CNN 模拟／弱收益、离线成本、浮点非 bitwise 与成熟 fallback 未遗漏，未授 LLM serving／一般最优。 |
| ToolWait 2609.34663：PASS | Ch46:226/228，两自然段 | 与 Tail A 两段内容一致；`SF-2026-ARXIV-2609-34663` 唯一一次 | Trade-off 原 waiting/fairness/prefill-decode 干扰仍保留，工程实践标题与后续问题保留。新增固定 bucket × endogenous re-arrival、dummy/cache 共池反馈；slot+batch 联动、chunk≠ITL、proxy≠占用证书与原策略 fallback 清楚，不把有限静态 backend 推广成一般动态引擎。 |
| PRISM 2609.35569：PASS | Ch70:200/202，两自然段 | 与 Tail A 两段内容一致（链接前空白归一）；`SF-2026-ARXIV-2609-35569` 唯一一次 | 原 functional unit/lifecycle、不确定性两段与后续需求反弹完整保留；新增部署固定的 operational 正比例排序、embodied 差额 crossover。pairwise≠全候选最优、地域／寿命／系数假设、sunk fleet 与采购分账、调度授权和数据不足 fallback 都保留，未授真实站点／生产收益。 |

实际核查包括三项两段 literal 的空白归一匹配、各 source-family marker 数=1（只作一致性辅助），并人工读取各处前后正文作上述语义边界判断；没有靠计数替代 POST。三项均未发现新增失败或改写要求。核查只对这次三项插入及相邻旧正文负责，不认证整个旧工作树差额；没有执行 stage、commit、push 或任何 Books 修改。

本附件为新 untracked 文件，`git diff --check --no-index /dev/null <本附件>` 没有 whitespace diagnostics（exit=1 表示存在新文件差额，不是验收失败）。未以格式检查授独立语义接受或 Daily 完成。

## 追加：四个 Theme 尾项 actual POST

非写入作者 reviewer 复用 root 本轮已完成的 exact-v1→actual owner PRE，以及 `V3_THEME_TAIL.md` 四项未变化的必要源、反侧与 literal；逐项实际读取写入正文和相邻旧边界。没有重读未变源或修改 Books。先核内容，再以两段空白归一匹配／marker 各一次辅助检查。第一次辅助脚本未先去掉 Markdown blockquote 的空 `>` 行，误识为一段；修正本地解析后四项均为两段匹配，不是来源／语义失败。

| 家族／POST | 实际位置、marker 与 literal | 邻接正文和受限采用 |
| --- | --- | --- |
| Semantic Prefix Oracles 2609.35425：PASS | `INFER-SGLANG` Ch51:132/134；`SF-2026-ARXIV-2609-35425` 各一；两段与提案一致 | 原 Structured Generation 的 constraint-state／CPU／batch 成本保留，新小节位于合法 token set 总结后、原 Adapter Readiness 标题前。Safe pruning 与 completability 合同分开，token lift 要求和有限 differential／STLC/tool 反侧仍在；不授任意 tokenizer、机械实现证明或程序行为认证。 |
| RCP 2609.35739：PASS | `PLATFORM-EVALUATION-SYSTEM` Ch66:260/262；`SF-2026-ARXIV-2609-35739` 各一；两段与提案一致 | 原 soft-win→BT/Elo、conformal interval 及 exchangeability／marginal coverage／人工 fallback 仍保留，后方 Route/defer 条件正确率分解保留。未新增 heading，保持原 Judge Ranking 作用域；query 内固定顺序、跨 query unit/origin 校准与 gain 不是真值写清，冗余/互补、同源偏好与独立标签 fallback 不丢失。 |
| SpeakGR 2609.35430：PASS | `TRAIN-SFT` Ch29:390/392；`SF-2026-ARXIV-2609-35430` 各一；两段与提案一致 | 原 occupancy 的执行／label／outcome 分权及模型/任务范围保留，插入在 `2605-12913:end` 后、shared Trace 前；后者未被改写。Text subset 重归一、student continuation、teacher 同 prefix 分布而非 suffix 的权限明确；SID 检索与语言分布双评价、matched-weight 归因不足和未实证完整 RAG 都保留。 |
| TRACE 2609.33517：PASS | `AGENT-MEMORY` Ch77:184/186；`SF-2026-ARXIV-2609-33517` 各一；两段与提案一致 | 原读取前 authorization 和 Recency/source/supersession 段保留，后方跨查询累计披露与 private-read 标题保留。未新增 heading，不改变这些旧段作用域。Return epoch、逐项有效≠整组 obligations coverage、private experience source 再准入与 reset/block 清楚；view 不认证事实、explicit replacement／长缺席反侧及开放环境安全限制保留。 |

四项 actual POST 均 PASS；这个结果只覆盖本轮四处插入及相邻旧边界，不认证整个 dirty worktree 或最终 Daily。Source Review 未重新计数，本 reviewer 未写 Books／stage／commit／push。

## 追加：四个 bounded 负侧信号的独立校准

只打开指定精确事件／版本及其必要 core，不扩目录、论文库存或整篇前后版本比较。沿本日报窗口与当前合同执行：普通不准入项具体关闭；相关 release 的必要日期不明则精确隔离，而不是当零命中。

### Custom agents in Google plugins：具体关闭，修正“全体只读”概括

直接读取 [Google 官方核心全文](https://antigravity.google/blog/custom-agents-in-google-plugins) 的三 plugin 与 Play definition，日期原值 `Sep 28, 2026` 为日级、无时刻/时区。页面从已经 introduced 的 custom agents 出发，新增的是官方插件对专用 instructions/context/tools 与既有 skills 的打包、示例 workflow，而未披露新的推断／授权／验证机制或独立有效性证据；不因 release 标签和相关安全应用自动准入。

必要负侧：**不能把三个 agent 都说成 read-only**。Flutter core 明确可 apply code fixes，Firebase 可 author security rules；只有 Play pre-submission auditor 的示例明确 read-only、`permissionMode: plan` 和 diagnostic/advisory 输出。示例 instruction 与工具清单本身也不证明强制只读或真实合规。这一措辞修正不产生新的长期机制，故具体关闭、不评分、不写 Books；日期未核实不授当窗，也不为已明确不准入材料穷查时刻。若未来出现新的执行权限／保证或评价纠错，定点重开该事件，不扩 Google 插件目录。

### RiKFAD 2609.30342v2：不因版本号重复评分

直接读取 [当前精确 v2 方法／理论 core](https://arxiv.org/html/2609.30342v2) §2 的 Eq.11–16、BACD splitting／memory 与 §3 的 damping/regularizer 条件；[身份页](https://arxiv.org/abs/2609.30342v2) direct curl 成功（web cache miss 不算外部受阻）。版本历史原值：v1 `Thu, 24 Sep 2026 11:53:47 UTC`；v2 `Mon, 28 Sep 2026 11:16:29 UTC`。当前必要页未见撤回、勘误／明确 correction 标记。

当下 Ch28:473/475 已有 v1 实际采用链：momentum 平方行列统计形成 friction，而非梯度 preconditioner；完整 momentum 不省、γ=0 不继承正 damping 的指数率、防零 regularizer 改变渐近幂次、连续强凸理论不授离散随机 LLM。当前 v2 core 仍是这些对象和边界：γ>0 强凸指数收敛，γ=0 为代数率，正 regularizer 与零 regularizer 条件分别对应不同幂次；没有在指定当前信号中发现要求改变这些解释／设计选择的 delta。故对版本事件具体关闭、不重复评分／不新增家族／不改 Books；不是声称 v1/v2 全篇逐字相同。只在出现明确新机制、保证、反侧、纠错说明或 owner 冲突时定点重开，不穷比完整历史稿。

### MiniMax CLI 0.5.9：普通修复关闭，不据日级日期授窗

实际 curl 读取 [官方 changelog 精确段](https://agent.minimax.io/docs/changelog.md)，原值 `0.5.9 · 2026-09-29`，没有时刻／时区。新增 `background=N` 的根会话活跃后台数量展示，并避免根 turn 结束后列表未返回时显示为零；另有 BYOK 请求字节上限、历史读取变轻、撤回编辑及清除旧终端错误。它们是计数／请求体／UI 历史修复，不披露新任务控制、授权、effect commit 或可改变长期设计的可靠性保证；显示至少一不等任务仍真实运行。故关闭、不评分、不写 Books；日期未核实不作当窗候选，也不继续查整个 CLI 历史。若后来公开新的背景任务控制合同或错误影响系统判断的证据，再定点重开。

### MiniMax CLI 0.5.8：相关生命周期信号，必要 release 日期隔离

同一 [官方 changelog](https://agent.minimax.io/docs/changelog.md) 的原值 `0.5.8 · 2026-09-28` 只有日级、时区与精确发布时刻均 Not Disclosed。停止会话会连同终止该会话后台任务，避免继续运行／完成通知重新唤醒；switch 与 `/clear` 则保留后台。这明确改变 stop 与导航／清空操作的任务寿命合同，是相关 release 安全／生命周期信号，**不以普通 bugfix 标签关闭**。Hook 提示可回放却不进入模型 context、终端清理与排队改进是旁项，不能代替该合同。

但 Sep28 日级事件可能在本窗起点前，未知时区也不能补造 `09:00` 或按发现时刻授窗。最终为本窗外部日期终态隔离：不用于正面 Evidence／当窗分母，不进入 Books，不称该 release 已审验收或来源零命中。必要请求只一次：该版本的官方精确 publication/release timestamp（含时区），或可绑定该版本的官方发布批次和时区约定；可接受官方 release metadata，不用 CDN Last-Modified／抓取时间代替。材料到达时，只重开 0.5.8 的落窗与 lifecycle 命题，确认落窗后执行对应安全/边界证据与唯一 owner 判断，不重跑 MiniMax 全目录。

## 追加：最后五项 Theme actual POST

限定 2609.35439／35652／35469／35304／34496，非 Books 写入作者核查。本轮复用 root 明确已完成的 exact-v1 方法→actual owner PRE，以及 `V3_THEME_ROOT_PREP.md` 未变化的必要方法、反侧与窄 literal；身份、版本、采用命题没有变化，未扩源、未重新计作 Source Review。实际读取 Ch26、Ch76、Ch82 插入处和前后正文，先检查内容及权限，再用两段 literal 空白归一匹配和唯一 marker 辅助确认，不以计数代替语义 POST。

| 家族／POST | 实际位置与一致性 | 原论证保留和权限／反侧 |
| --- | --- | --- |
| RTP 2609.35439：PASS | `MULTIMODAL-EMBODIED-VLA` Ch26:301/303；两段与 literal 一致，`SF-2026-ARXIV-2609-35439` 仅一处 | 在原同步／异步 video-action 分支后、Future-to-Action 因果使用标题前。原训练支持时间表、模态一致性、deadline／controller 回退仍在；新事实 observation/control/proprioception 与 root/time/frontier/solver proposal 分账，Bridge/residual 只修未执行计划，retain 也重解当前 action。经验接受器不授 physical commit、mean/p95 反侧及 source/prefix 消融归因不足保留，没有将旧预测晋升历史或少视觉步数当 deadline。 |
| MM-ABC 2609.35652：PASS | `MULTIMODAL-EMBODIED-VLA` Ch26:180/182；两段与 literal 一致，`SF-2026-ARXIV-2609-35652` 仅一处 | 在固定点 decoder 与停止／warm-start 反侧后、learned endpoint initialization 前；旧条件化 factor 与 fixed-point body binding 不被覆盖，后方 endpoint/corrector 仍各有对象。新段区分共同 endpoint loss、网络 x/v 输出和采样 velocity，raw-input skip 会改变内部抵消噪声负担；保留低秩/few-step/网络条件、给定 allocation≠学会协调、任务退步与 controller 代价，不授 x-head 普遍优势或安全。 |
| CATok 2609.35469：PASS | `MULTIMODAL-EMBODIED-VLA` Ch26:149/151；两段与 literal 一致，`SF-2026-ARXIV-2609-35469` 仅一处 | 位于旧 codec／LIBERO component-scaling 对照后、粗 planner→连续 refiner 前；旧表示瓶颈和码本边界、后方 FIFO freshness/controller 论证保留。逐步撤去前 codes、后 codes 留晚阶段及 action state 保留早信息写清；不混成 token 的物理时间或前缀执行权。Matched annealing／native-decoder 干预受结构 mask 约束、长 code/任务退步、frozen decoder 不冻结 VLM CE 都保留。 |
| Signal or Noise 2609.35304：PASS | `AGENT-RAG` Ch76:536/538；两段与 literal 一致，`SF-2026-ARXIV-2609-35304` 仅一处 | 在原多模态 coverage／支配关系两段后、Escalation/Abstention 前。原 source truth、attention 仅诊断、单模态反事实与后方阈值授权保留；支持 edge admission 与 reader 只携 allowed-subset chunks 分开落实。`V(∅)` 的 most-frequent gold 基线不冒充 empty-context run，负交互不鉴别 interference／冗余、切片 CI 不授固定淘汰/router 权；不以诊断分数取得事实 authority。 |
| MASTraceBench 2609.34496：PASS | `AGENT-MULTI-AGENT` Ch82:759/761；两段与 literal 一致，`SF-2026-ARXIV-2609-34496` 仅一处 | 在并行 Evaluation 的原成本／风险列表后、throughput≠serving batching 及条件化分支前。原 replica/structural parallelism、topology attribution 边界和后方 evidence-flow 保留；新增 strongest initial→各 proposer final→aggregate 三层质量账，critique/verifier 不混 proposer 分母，dynamic episode 与 state-conditioned diagnostics 不同分母。AL 可负、事后 initial oracle 非线上真值、不等预算/固定对手/proxy 限制及 equal-budget/latency/fallback 未删，不以更多轮／共识授权提交。 |

五项 actual POST 均 PASS，没有发现需修改的 literal、邻接或采用边界。Source 证据未变可按上述范围复用；本核查不替代正式报告分母、来源停止、日期保留或日级 Gate，不认证整个既有 dirty diff。只追加本附件，未改 Books，未 stage、commit、push。
