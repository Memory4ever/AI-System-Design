# 第24章 多模态生成范式

**Knowledge Tree:** Part III 多模态、生成与世界模型：从跨模态表示到物理行动
**Stable Knowledge Node ID:** `MULTIMODAL-GENERATIVE-PARADIGMS`
**Legacy Chapter:** N/A
**Status:** Draft

**Roadmap Intent:** 从概率分解与状态提交出发，比较 Autoregressive、Diffusion、Masked/Block Diffusion 与混合 proposal-correction，而不是用单项 benchmark 宣布范式替代。

## 本章要回答的问题

为什么文本生成长期以 Autoregressive 为主，而图像和视频大量采用 Diffusion？Masked Diffusion 为什么能并行生成多个 token，却带来 mutable output、cache invalidation 和 streaming 难题？Block Diffusion、draft tree 和 correction loop 是同一条路线吗？

本章的核心判断是：**生成范式的差别首先是概率分解、状态可变性与 commit protocol 的差别，随后才表现为 kernel、cache 和 latency 差别。**“一次生成更多 token”不自动等于更快；“允许修正”也不自动等于更准。必须把 proposal work、verification/correction、memory、并发和输出提交一起计算。

## 从一个共同问题开始

给定条件 `c`，系统要从分布 `p(x | c)` 产生样本。不同范式选择不同的计算路径。

Autoregressive factorization：

```text
p(x | c) = Π_t p(x_t | x_<t, c)
```

Diffusion 或 masked generation 则定义一系列从噪声或未知状态到数据的 transition：

```text
x_T -> x_{T-1} -> ... -> x_0
```

两者都可能使用 Transformer，也都可能生成文本、图像或视频。真正不同的是：每步条件是什么，哪些位置可以并行改变，何时把中间状态视为最终输出。

## 为什么 Autoregressive 是合理起点

AR 将复杂联合分布拆成条件概率乘积。训练可以 teacher forcing，并行计算所有位置的 loss；推理必须依次确定 token。它的稳定优势包括：

- 与文本天然顺序一致；
- 输出 append-only，适合 streaming；
- 历史 KV 可缓存；
- 每步概率和停止条件清楚；
- target model 直接拥有最终分布。

代价是 serial depth 至少与输出长度相关。即使每步 matrix operation 高度并行，下一个 token 仍等待前一个 token 确定。图像或视频使用 raster-order AR 时，这种任意顺序还可能让局部相关性被迫经过很长路径。

## Diffusion：用迭代修正换并行状态更新

连续 diffusion 从噪声逐步 denoise；离散或 masked diffusion 从 mask/noise state 逐步恢复 token。每轮可以同时更新许多位置，因此 serial steps 不必等于 token 数。

它的优势不是“完全并行”，而是把串行维度从 output length 改成 denoising/refinement steps。代价包括：

- 多轮 full or block forward；
- 中间状态可变，cache reuse 更困难；
- streaming 前必须定义哪些 token 已 committed；
- 迭代 schedule 会影响质量、延迟和稳定性；
- likelihood、sampling exactness 和 stop condition 可能更复杂。

图像和视频往往容忍整体画面同时从粗到细修正，且用户不要求逐像素 streaming，因此 diffusion 的系统契约较自然。文本要求稳定前缀和低延迟流式输出，mutable tokens 的成本更明显。

## Masked generation：未知位置与已知位置

masked model 维护部分可见序列：

```text
known tokens + [MASK] positions
```

每轮对多个 mask 产生预测，再按 confidence 或 schedule 提交一部分。保守 schedule 一次只接纳少量高置信 token，质量更稳但并行收益有限；激进 schedule 接纳更多 token，早期错误会成为后续条件。

这解释了一个关键演进：

```text
只填充未知位置
→ 高并行填充暴露误差累积
→ 允许重写已生成 token
→ 显式训练 proposal + correction
```

后一步没有否定保守 unmask。它用更多训练与推理 work、mutable state 和提交复杂度换取更激进的并行 operating point。

## Editable tokens 与 commit boundary

### Self-revision：并行位置必须在 Commit 前保持可撤销

普通 masked diffusion 把位置从 mask 变成 token 后往往视为已解码；早期错误随后只能被其他位置条件化放大。
让已预测位置继续以 confidence-weighted token/mask 表示参与后续 denoising，可形成 provisional state，直到 block
稳定或达到阈值才 commit：

```text
self-generated noisy state
→ parallel provisional tokens + confidence
→ repeated revision
→ convergence / threshold gate
→ block commit
```

Runtime trick 不足以保证模型会修正自己的错误；training distribution 必须包含 self-generated noise。它新增
threshold calibration、oscillation、block 内最慢请求 barrier、KV/graph invalidation 和 stream rollback。标准 AR
在 exact left-to-right commit、低并发或模型未匹配 revision training 时仍然合理。DMax 是 Experimental 分支，
其 batch-1 双卡结果不能写成 serving goodput。

### 生成 Workflow 也可以被训练进 Intermediate State

复杂视觉生成可以从 one-shot prompt→image 演进为 plan→draft→inspect→refine；若 intermediate scene graph、
text plan、draft 与 correction 都进入训练对象，模型学习的是显式 workflow state，而不只是最终像素。它可能提高
约束可诊断性，却引入 plan/pixel inconsistency、self-critic correlation、更多生成步与错误 verbalization。
简单 prompt、强基础 generator 或 latency-sensitive workload 仍应 one-shot。Think in Strokes 的作者结果只支持
其 scene-graph/data contract，不证明 verbal plan 等于可解释因果或跨 modality 通用。

若生成器可以把 token 从 A 改成 B，runtime 必须区分：

```text
provisional state  模型仍可修改
committed output    已对用户、工具或下游产生承诺
```

在 UI 内部重绘一幅图通常安全；已流式发送的文本、已触发的 tool call 或已执行的 robot action 无法简单改写。于是模型机制会向系统传播：

- token revision 是否需要 retract protocol；
- radix/KV cache 怎样 invalidation；
- stop sequence 在 provisional state 中是否生效；
- request cancellation 如何清理多轮状态；
- batching 时不同 correction cadence 如何保持公平。

因此可编辑生成不是 Decoder 的一个小优化，而是新的 state machine。

实时多模态生成还可能把统一模型拆成 state-preserving deployment pipeline，而不是重新拆回互不相干的模型。
一个 thinker 保留 encoder、language/environment update、decoder 与 authoritative KV slices，performer 只执行下一
audio/video latent 的 flow solver；两者交换同一历史状态与上一生成单元，以一拍流水重叠理解和生成：

```text
multimodal observation and shared causal state
→ thinker updates semantic/world/KV state
→ performer generates next media latent
→ timestamped handoff and backpressure
→ commit visible unit or recover both sides
```

这条路线改变的是 deployment ownership，不证明模块化 pipeline 已过时。Overlap 可降低受限系统中的 model-side
latency，却新增 KV/version consistency、跨模态时钟、双侧 partial failure、backpressure 与 rolling error。Wan-
Streamer 只为其作者模型与未完整披露硬件合同提供实验性证据；低流量、严格单步一致性或不能容忍跨 stage
恢复复杂度时，串行统一模型或独立模块仍合理。

## Block Diffusion：局部自回归与块内并行

Block Diffusion 把序列分成 blocks。block 之间保持 causal order，block 内用 masked/refinement steps 并行生成：

```text
block_1 -> block_2 -> ...
within block_k: iterative parallel refinement
```

它试图在两种范式之间取 Pareto 点：保留 block-level prefix/cache 和部分 streaming，同时减少 token-level serial steps。新的 trade-off 是 block size：

- 小 block 接近 AR，cache 和 commit 简单，并行收益小；
- 大 block 并行机会更多，但 correction、verification、memory 和首块延迟增加。

固定 block size 只是策略之一。工作负载变化时，最优 size 可能依赖 entropy、prompt、硬件、batch 和 SLO。

## Draft、Verify 与 Correct 不是同一件事

### Draft + exact verification

speculative decoding 允许便宜 drafter 提议 token，再由 target 验证。若 acceptance rule 正确，可以保持 target distribution。它的目标是减少昂贵 target serial steps，不改变 target 的输出语义。

### Correction

correction 允许同一模型或 corrector 修改已经可见的 provisional tokens。它可能改善质量，但不天然保持某个 AR target distribution，也可能振荡或破坏正确 token。

### Tree proposal

一次 draft pass 可以产生多个未来位置的 marginals，并据此构造 candidate tree。target 用 tree attention 一次验证多条前缀。这里需要区分 draft surrogate probability 与 target path probability；前者适合分配 node budget，不等于后者。

三者可以组合，却拥有不同 correctness contract：

```text
draft owns proposal breadth
target owns accept/reject semantics
corrector owns mutable refinement
runtime owns commit, rollback and KV compaction
```

## 从 Specialist Head 到 Typed Unified Generation

分类、检测、分割、深度与多视角几何传统上各自使用专用 head、loss 和 decoder。这一结构在单任务、固定输出
shape 与严格延迟下仍最强：类型约束直接写在 architecture 中，非法输出空间较小。但能力数增多后，每个新任务
都带来独立训练、部署和评估接口，跨任务知识也难以共享。

统一生成不是简单把所有 target 转成字符串，而是把类型边界从专用 head 移到 versioned sample contract：

```text
visual inputs
+ task and output-schema instruction
→ native text / image / mixed provisional response
→ deterministic typed decoder
→ boxes | masks | dense maps | camera records
→ task-specific invariant and evaluator
```

生成模型拥有 provisional response，schema/parser 拥有从 token 或 image record 到 typed object 的 commit，
下游 evaluator 仍按任务语义判定 correctness。共享 generator 因而可以复用 representation 与训练数据，但不会
消除 modality-specific codec、coordinate frame、mask topology 或 camera convention。reserved token、parser 与
annotation conversion revision 必须进入 artifact identity；否则同一 checkpoint 在不同 decoder 下会产生不同
系统行为。

这条路线用接口复用和 cross-task transfer 换来 parser/schema drift、invalid output、coordinate quantization、
pseudo-label provenance 和 capability interference。专用 head 在硬实时、强校准 dense output 或安全关键几何中
仍然合理；统一生成适合任务族持续扩展且 typed decoder 可严格验证的场景。作者跨多个视觉任务的结果只支持
其转换数据与 evaluator 合同，不证明一种 response representation 对所有视觉 workload 都最优。

### Exploration 是训练计算轴，不是新的生成真值

单一监督 target 最容易复现，也避免额外 candidate generation；当同一条件存在多个合理 mode 时，它却可能把一次
任意匹配当成唯一正确路径。另一条训练分支为同一输入生成多个候选匹配，按预先声明的 scorer 选择其中一个再更新
模型，使训练更接近推理时的 mode commitment：

```text
condition + target set
→ sample multiple candidate matches
→ score under frozen matching contract
→ select one training trajectory
→ update generator
```

这让 exploration 成为除模型规模和每样本计算之外的第三条训练计算轴，但没有创造更可靠的 ground truth。候选数增加
会线性或超线性放大生成与筛选成本，选择器偏差还会把某种 mode 固化成训练偏好。固定单匹配在数据近单峰、预算紧或
scorer 不可信时仍合理；多候选探索只在候选多样性、selection contract 和单位训练预算收益一起验证时成立。作者的
受限 scaling curve 不能证明它会普遍替代 AR、diffusion 或 masked generation，只说明 training-time sampling policy
本身也需要被版本化和计量。

## 一个统一的成本模型

端到端时间不能只数模型 forward 次数：

```text
T_total = T_queue
        + T_encode
        + T_proposal
        + T_verify_or_correct
        + T_state_management
        + T_decode_output
```

吞吐也不能只报告 tokens/s。对于 mutable generation，应同时报告：

- committed tokens/s，而非 provisional updates/s；
- quality 在同一 scorer 下是否等价；
- block/tree/correction 使用的额外 memory；
- batch、concurrency、length、precision、hardware；
- TTFT、inter-token latency 或最终 completion latency；
- rollback、cache compaction 和 scheduler overhead。

如果论文为每个 dataset 事后选择最佳 tree budget，它证明“存在有效 operating point”，不等于已经给出线上 controller。

## 文本、图像和视频为何不能共享一套性能结论

文本通常要求 prefix correctness、streaming 和 stop/tool semantics；图像更关心最终 sample quality，允许整幅反复修正；视频还要保持 temporal consistency，单次 token 数和 decoder cost 很高。

因此同一个生成范式在不同 modality 上的瓶颈不同：

| Workload | 主要提交边界 | 常见主瓶颈 |
| --- | --- | --- |
| 文本 | prefix / token | serial decode、KV、streaming correctness |
| 图像 | final image / preview stage | denoising steps、latent decoder、resolution |
| 视频 | clip / frame window | temporal state、3D attention、decode bandwidth |
| action | action chunk / control deadline | freshness、safety、不可逆副作用 |

不能从图像 diffusion 的并行性推断文本 serving 也会同样加速，更不能把 video quality 当作 action correctness。

## Training / Inference mismatch

AR teacher forcing 训练看到正确前缀，推理看到自己的历史输出；diffusion training 看到人工 noise/mask distribution，推理看到由模型 schedule 产生的中间状态。两者都有 exposure mismatch，只是形式不同。

proposal-correction training 会显式生成错误中间状态，让模型学习修正。但 synthetic error 是否覆盖真实 rollout error，仍取决于 corruption process。过强 corruption 可能让模型学会恢复不现实噪声，过弱 corruption 又无法处理 aggressive decoding 的错误。

## Cache、rollback 与 exactness

### Commitment Policy 可以从未来稳定轨迹学习

固定置信阈值或 block schedule 假设所有 token 的收敛速度相似。对于迭代修正生成，可以从完整去噪轨迹标注“该位置何时之后不再变化”，训练 token-local controller 预测 commitment，并用动态 threshold 决定冻结位置。它把 commit owner 从静态规则变为受限 learned policy，可减少无效更新；代价是监督依赖未来轨迹、分布漂移会导致过早锁定，且 rollback 更复杂。若 controller 未校准，原有保守固定 schedule 仍是 fallback。现有证据只覆盖冻结模型上的 plug-in 控制器，不证明其保持自回归式 exactness。

<!-- source-family:SF-2026-ARXIV-2605-24697 -->

AR append-only KV 最容易复用。block 或 editable generation 若修改早期 token，受影响的 attention state 必须重算或版本化。一个安全的 cache key 至少包含：

```text
model + tokenizer/codec + prompt prefix
+ generation algorithm + block/revision identity
+ adapter/quantization + position policy
```

speculative exactness 只在 acceptance/sampling rule 与 target distribution 对齐时成立。浮点 kernel、quantization 或 logit processor 差异也可能让“理论 exact”与具体 runtime 的 bitwise 路径不同。生产系统应区分 distributional correctness、deterministic replay 和 semantic quality。

diffusion trajectory 还存在另一类 cache：在相邻 denoising state 变化足够小时，复用完整 denoiser output。它不是 AR KV Cache 的 exact historical state，而是带 error budget 的 approximation。一个可治理的复用 policy 至少同时拥有：

```text
model / sampler / conditioning identity
sensitivity calibration profile
latent displacement and timestep gap
quality tolerance
max consecutive reuse / max staleness
cached output and refresh anchor
```

固定 skip schedule 在 workload 稳定、控制面简单时仍合理；sample-sensitive policy 可以把实际 trajectory displacement 纳入决策，却增加 calibration drift、一阶近似误差和局部小误差累积。NFE reduction 也不能直接等同端到端 latency 或 goodput。更长期的方向是让局部 sensitivity 成为 global error-budget scheduler 的输入，而不是让每一步 threshold 独立决定全部质量预算。

比“整层复用或整层刷新”更细的一条分支，是预测下一 denoising step 中哪些 token/patch state 会显著变化，
只重算这部分 mutable set，并保留一小组动态 sink 维持全局信息流。它把 cache policy 从固定 spatial mask
推进为 trajectory-conditioned refresh：selection 由当前 latent/confidence 产生，refresh 后必须更新对应 cache
version，未选位置只能在校准误差预算内复用。

这种机制新增 selector cost、变化位置漏检、sink 漂移、irregular gather 与不同请求 mutable-set shape 的 batching
损失。模型 confidence 不是 cache-validity probability；作者在 diffusion LM 上的实验也不能外推到 append-only
AR Decode。固定全刷新在 step 数少、变化广泛或 exactness 优先时仍是基线；固定 mask 在 shape 稳定、graph
capture 重要时更容易工程化。

### Cache 误差是沿生成轨迹演化的状态

把 diffusion cache 的误差看成每个 site 的固定 representation mismatch，适合静态校准，却忽略先前修正会改变后续输入。trajectory-consistent calibration 沿 corrected history 逐步估计 site-local prior，使 cache 决策读取当前生成轨迹而非一次性误差表；收益是减少累计偏差，代价是离线 prior、prompt 分布和采样 schedule 共同进入 artifact identity。prior 漂移或未覆盖 cache policy 时应回退 base cache 或 full computation。现有证据只覆盖披露图像模型、H800 与采样路径，不能外推在线并发或分布外 prompt。

<!-- source-family:SF-2026-ARXIV-2605-24870 -->

## Scheduling：并行机会也需要被分配

更大 block、更多 tree nodes 或更多 correction loops可能提高单请求进度，也会占用更多 verification compute 和 workspace。高并发下，scheduler 可能更愿意服务多个小请求，而不是让一个请求扩展巨大 tree。

因此 generation policy 应暴露预算：

```text
proposal budget
verification budget
mutable window
deadline
quality / exactness requirement
```

model 产生 confidence，runtime 根据 queue、memory 和 SLO 选择 operating point。把 threshold 或 tree size 固定在模型代码里，会让系统失去跨工作负载调度能力。

图像或视频 diffusion 还可以把 patch granularity 变成 trajectory policy：早期或低变化阶段使用 coarse patch，细节阶段回到 fine patch。这里必须分开两层：artifact 先通过训练获得多种 patch shape 的语义能力，runtime 才能依据 latent history 和 threshold 选择 shape。“选择规则在 test time 运行”不等于整个方案 training-free。

这种 adaptive granularity 减少单请求 token 数，也新增 latent-history state、threshold calibration、shape switching 与多分支 artifact identity；不同请求选择不同 shape 时，还可能破坏 batching、graph capture 与 kernel reuse。固定 fine patch 在 worst-case detail、可预测 shape 和成熟 kernel 场景仍成立。若论文的 threshold table、hardware、precision 或配置记录相互矛盾，Books 只能吸收机制与 failure mode，不能吸收精确 speedup。

### 从一次生成到 Plan → Generate → Validate → Retry

Autoregressive media generation 的状态机不能永远停留在“给定 prefix，继续采样”。当输出同时受内容、时序、
韵律、音色或安全约束时，直接生成仍然合理：路径短、延迟低，也不需要维护额外控制状态；它的边界是错误
往往要到完整 artifact 产生后才暴露，局部修复又可能破坏其他约束。

一种 `Layering / Dependency` 演进是先生成可检查的 plan，再生成高带宽 token，最后用独立 validator 决定
commit、bounded retry 或 fallback：

```text
request + locale / speaker / policy identity
→ content / timing / control plan
→ autoregressive media tokens
→ acoustic / semantic / policy validation
→ commit | regenerate with diagnosis | fallback
```

这里的 plan 是 provisional control state，不是模型已经正确理解约束的证明；validator 也必须拥有版本、阈值、
false-positive/false-negative 与覆盖范围。Retry 若复用同一错误 plan 只会重复失败，若完全重建则增加 latency、
compute 和 output variance；streaming 一旦播放前缀，rollback boundary 还会变成用户可见协议。小模型、低风险、
严格 latency 或 validator 不可靠时，direct generation 与简单 post-filter 仍然成立。

Amazon 的 LLM-based TTS 工程材料支持“显式计划、生成后检查与有限重试可组成一条工程路径”，但没有公开
可复现实验 artifact、模型内部实现、并发或 tail-SLO contract；因此这里只吸收状态机，不外推质量数字或
内部机制。

## 失败模式与旧方案适用边界

### Error amplification

并行接受多个相互条件化不足的 token，会让一次错误污染整个 block。保守 AR 或小 block 在错误代价高时仍合理。

### Correction oscillation

corrector 反复在多个 token 之间切换，耗尽预算且无法形成 commit。需要最大 revision 次数、置信滞回或 verifier。

### Cache inconsistency

token 已修改而 KV、radix tree 或 downstream parser 未失效，产生隐蔽的错误状态。

### Oracle policy

实验离线选择最佳 threshold/budget，线上没有相同信息。应单独验证 controller，而非沿用 oracle 上界。

### Framework mismatch

tree mask 落到较慢 kernel、dynamic shape 破坏 graph capture，算法减少 steps 却增加 wall time。旧的单路径 AR 在成熟 kernel、高并发和短输出下可能更快。

## 工程实践

选择生成范式时按顺序回答：

1. 输出何时产生不可撤销副作用？
2. 质量目标要求 exact target distribution，还是允许新的 learned distribution？
3. workload 更看重 TTFT、streaming cadence 还是 final completion？
4. 硬件和 runtime 是否支持 block/tree mask、dynamic shape 与 KV compaction？
5. proposal/correction 的额外计算能否被 acceptance 或并行进度偿还？
6. policy 是固定参数、模型置信度控制，还是 scheduler 预算控制？
7. Evaluation 是否使用 committed output 和完整 workload contract？

### 条件化机制分支与共存边界

主线之外仍存在若干只在特定前提下成立的设计分支。下面按状态与控制权的变化说明它们解决的问题、新增代价及回退边界；来源身份和实验限制统一留在章末 Review notes。

<!-- semantic-body-binding:SF-2026-ARXIV-2606-27732:start -->
Diffusion-LM 可用 asymmetric bidirectional sidecar 提供受控右上下文，同时让主干保留可缓存的单向状态。它以额外 sidecar 参数和融合开销换 parallel correction；若右上下文收益抵不过 cache invalidation 和迭代成本，仍回到纯 AR 或无缓存的双向分支。
<!-- semantic-body-binding:SF-2026-ARXIV-2606-27732:end -->

### Distributional Distance 可以成为受限训练目标

Fréchet 类表示距离通常用于训练后评估，因为 batch 内同时估计 population statistics 与反向传播会带来偏差和不稳定。把统计 population 与 gradient batch 解耦后，它可以成为直接 distribution-matching loss，但需要维护 estimator state，并继承 representation encoder 的语义偏差。该路线适合明确表示空间与分布目标的生成 workload；它不证明 perceptual alignment，也不能从图像结果外推所有模态，样本级 likelihood 或任务损失仍是重要共存分支。

<!-- source-family:SF-2026-ARXIV-2604-28190 -->

### 固定长度 Diffusion 把长度预测变成 Admission 决策

自回归生成可以逐 token 停止，固定长度 diffusion LM 却需要在去噪开始前分配响应槽位；因此 length predictor 实际上拥有一次 admission-time compute budget。预测偏长会浪费并行迭代，预测偏短则可能截断语义并触发扩容或整段重试，破坏原本的延迟优势。动态长度只有在预测开销、重试策略和 SLO 一起计入时才成立；长度高度不确定或输出必须完整时，保守上界或自回归分支仍更可靠。[受限证据：arXiv:2605.04215v1]

<!-- source-family:SF-2026-ARXIV-2605-04215 -->

## 本章在知识树中的位置

第18章解释 Decoder Only AR，第20章解释 token sampling；本章把 AR 放进更宽的生成范式树，并拥有 mutable generation、block refinement 与 commit boundary。第25章只在生成状态同时表达 action-conditioned environment transition 时才称其为 World Model。

训练 objective 归 Part IV；线上 KV、batching、speculative verification 与 scheduler 分别由 Ch45～48、Ch56 拥有。本章定义它们要执行的 generation semantics，而不重复框架实现。

## 从机制演进到系统设计

生成范式的演进不是 AR 被 Diffusion 线性取代，而是 factorization、并行度与 correction authority 的重新分配。AR 每次提交一个 token，状态简单但串行；masked、block 或 diffusion 路线并行提出多个 provisional positions，再以迭代修正换吞吐。混合方案进一步把 proposal、verification、rollback 和 commit 拆开。

并行生成只有在质量合同、cache invalidation 和停止规则都被版本化后才成立。它获得并行度，却增加迭代次数、临时状态、拒绝/回滚以及训练—推理 mismatch；短输出、严格 exactness 或 correction 成本高时，AR 仍可能更优。图像、视频和文本的 evaluator、长度与硬件路径不同，不能共享未经条件化的性能结论。

### 从局部结果到可执行的系统边界

<!-- body-source:SF-2026-ARXIV-2606-22370 -->
长视频生成不能无限复制完整历史 KV；按 prompt-history 相关性选择可读历史，把 cache budget、selection error 与 continuity 绑定同一运行时状态。 这项变化只在 exact-v1 披露的 workload、状态身份和评估合同内成立；只覆盖受测长单镜头生成；selection miss 会破坏长期一致性，不能外推到可交互 world state。 因此旧路径在这些新增约束不存在、证据条件不足或失败回退被触发时仍然成立，不能被新的局部结果静默覆盖。

## 面试与自检问题

1. 为什么 diffusion 的 serial steps 少于 token 数仍不保证更快？
2. masked generation 中 provisional 与 committed token 有何区别？
3. Block Diffusion 如何在 AR 与 full-sequence diffusion 之间取舍？
4. correction 与 exact speculative verification 的 correctness contract 有何不同？
5. 为什么 draft marginal 不能当作 target path probability？
6. mutable token 会怎样影响 KV cache 和 streaming？
7. 一个离线 best-budget benchmark 为什么不等于线上 controller？
8. 哪些场景下 append-only AR 仍是更好的工程选择？

## Research Outlook

下一阶段压力是让 generation policy 成为 runtime 可控制对象：根据 entropy、queue、memory、deadline 和 output side effect 动态选择 block、proposal、correction 与 commit；同时建立跨 runtime 可复现的 committed-goodput 与 exactness 测试。

## Reflection

生成范式不是从“串行”走向“并行”的单向进步史。系统用并行草拟换来了 mutable state，用修正换来了额外 forward，用更大候选空间换来了 verification 和 memory。真正的演进，是让这些成本与输出承诺被显式管理。

### Early convergence 与 high confidence 不是同一个 Commit 证据

并行去噪最初常用当前位置的边际置信度决定是否提前提交；它便宜，却把“这一步很确定”误写成“后续步骤不会再改变”。约束变化是多个位置共同修正时，单点高置信仍可能被后续条件关系推翻。更严格的 runtime 可以追踪一个 token 在连续 denoising steps 中是否已经稳定，把 early-convergence signal 与边际 confidence 联合用于 provisional-to-committed transition。

这会减少不必要的更新，却增加跨步状态、滞回阈值与误提交风险；稳定检测仍不是联合分布正确性的证明。检测不可靠、输出有外部副作用或 exactness 优先时，应延后到 block verifier 或完整 denoising 结束再 commit。该分支补充本章的 mutable-state 路线，不宣称它普遍优于 confidence schedule。[受限证据：arXiv:2605.10980v1]

<!-- source-family:SF-2026-ARXIV-2605-10980 -->

## Review notes

- `SF-2026-ARXIV-2606-22370` — primary `arXiv:2606.22370v1`；Method=`arXiv:2606.22370v1 §3 Method`；Evaluation=`arXiv:2606.22370v1 §4 Experiments`；Non-proof=`arXiv:2606.22370v1 §5 Conclusion and long-single-shot scope`；Artifact=`Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review`。

- Vision as Unified Multimodal Generation（typed unified output contract；Status: Experimental）:
  https://arxiv.org/abs/2607.06560v1
- Explorative Modeling（多候选匹配与 selection-conditioned training；Status: Experimental）:
  https://arxiv.org/abs/2607.27372v1

- Amazon Science TTS planning/validation engineering evidence（Status: Experimental；Artifact Not Available）:
  https://www.amazon.science/blog/improving-quality-and-robustness-in-llm-based-text-to-speech-systems
- DMax（self-revising diffusion decode；Status: Experimental）: https://arxiv.org/abs/2604.08302
- Think in Strokes（interleaved visual generation workflow；Status: Experimental）:
  https://arxiv.org/abs/2604.04746

LLaDA2.1 与 ProSeCo 支持“并行草拟暴露错误累积后，引入 editable/correction state”的相邻分支；DDTree 支持“一次 block-diffusion marginal breadth 可用于构造受预算约束的验证树”；Multi-Block Diffusion 仅作为实验性 block-level 分支。Focus-dLLM 支持“预测下一步会变化的位置 → selective state refresh + dynamic sink preservation”的受限 cache 分支，但其 confidence 不是 cache-validity 概率，也不能外推到 AR Decode。DDiT 支持“multi-shape artifact 先于 adaptive runtime policy”的受限机制，但 threshold 表与两组 headline speedup contract 存在内部矛盾，精确收益保持 `Disputed`。SenCache 支持 sensitivity-bounded approximation cache 的受限分支，但其 calibration、quality metric 与单硬件 latency contract 不能外推到生产 serving。这些工作均不证明 Diffusion 会普遍替代 AR。

dLLM framework 进一步说明，统一软件抽象不等于抹平生成语义。跨 MDLM、BD3LM 或其他 diffusion-LM pipeline
复用 API 时，可交付 artifact 仍需绑定 sampler、noise/remask schedule、parallel commit ordering、EOS/padding、
cache approximation 与 framework revision；否则同名 checkpoint 在两个 runtime 中可能不是同一生成过程。
框架减少 recipe duplication，却新增 adapter semantic drift 与默认参数误用。原作者 pipeline 在新 objective、
特殊 post-processing 或框架尚未覆盖的机制上继续合理；本章吸收的是 generative-process artifact identity，
不把 dLLM 的作者结果外推为 diffusion-LM 的通用收益。

- Focus-dLLM（confidence-guided mutable-state refresh；Status: Experimental）: https://arxiv.org/abs/2602.02159

- LLaDA2.1: https://arxiv.org/abs/2602.08676
- ProSeCo: https://arxiv.org/abs/2602.11590
- DDTree: https://arxiv.org/abs/2604.12989
- Multi-Block Diffusion Language Models: https://arxiv.org/abs/2606.29215
- Wan-Streamer（state-preserving thinker/performer pipeline；Status: Experimental）:
  https://arxiv.org/abs/2606.25041
- Diffusion Templates: https://arxiv.org/abs/2604.24351
- DDiT: https://arxiv.org/abs/2602.16968
- SenCache: https://arxiv.org/abs/2602.24208
- dLLM framework（generative-process artifact identity；Status: Experimental）:
  https://arxiv.org/abs/2602.22661

### Daily integration evidence trace

#### Source-specific exact-v1 Review notes

- SF-2026-ARXIV-2606-27732 — primary arXiv:2606.27732v1; exact-v1 URL=https://arxiv.org/html/2606.27732v1; Method=https://arxiv.org/html/2606.27732v1 — §3 Method; 3.4 R2LM Architecture; 3.5 Training and Inference; Evaluation=https://arxiv.org/html/2606.27732v1 — §4 Experiments; 4.1 Experimental Setup; 4.2 Main Results: Multiple-Choice Benchmarks; Non-proof=https://arxiv.org/html/2606.27732v1 — §5 Conclusion。

### Source-family integration record

<!-- daily-20260627:MULTIMODAL-GENERATIVE-PARADIGMS:start -->
### Owner-merged minimal durable delta

并行文本生成不必只在全双向重算与纯 causal cache 之间二选一：受限 right-context side path 可以提供可编辑上下文，causal path 则保留 append-friendly state。generation identity 因而必须记录 mutable context 由哪条路径持有、哪些 cache entry 可复用，以及 provisional span 在何时提交。

### Trade-off、failure、fallback 与 coexistence

Side path 增加参数、训练耦合与 cache-version 复杂度；要求 exact streaming 或 kernel 不支持时回退 causal generation。

<!-- daily-20260627:MULTIMODAL-GENERATIVE-PARADIGMS:end -->

### Daily Books delta trace（2026-06—08）

<!-- daily-books-trace:SF-ORDER-AGNOSTIC-CHAIN-RULE:start -->
- `SF-ORDER-AGNOSTIC-CHAIN-RULE` — Daily `2026-06-01`；primary `arXiv:2606.00997v1`；Books review `books-review:SF-ORDER-AGNOSTIC-CHAIN-RULE`。

  **已吸收的语义增量：** Order-agnostic masked language models expose conditionals that need not compose into one coherent joint distribution; reveal order therefore becomes part of the decoding contract rather than a harmless scheduler choice. 证据边界：Reported likelihood shifts and uniform-spreading effects are specific to evaluated models and schedules; they do not prove that every diffusion language model is incoherent or inferior to autoregression.
<!-- daily-books-trace:SF-ORDER-AGNOSTIC-CHAIN-RULE:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-13426:start -->
- `SF-2026-ARXIV-2606-13426` — Daily `2026-06-12`；primary `arXiv:2606.13426v1`；Books review `books-review:SF-2026-ARXIV-2606-13426`。

  **已吸收的语义增量：** diffusion model 的 speculative block proposal 必须由 target-model block verifier统一 commit/rollback，才能把并行候选与 exact output distribution 分开
<!-- daily-books-trace:SF-2026-ARXIV-2606-13426:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-13496:start -->
- `SF-2026-ARXIV-2606-13496` — Daily `2026-06-12`；primary `arXiv:2606.13496v1`；Books review `books-review:SF-2026-ARXIV-2606-13496`。

  **已吸收的语义增量：** diffusion serving cache 应把 denoising step、state identity 与误差预算绑定，在 step-level reuse 与 recompute 间动态选择
<!-- daily-books-trace:SF-2026-ARXIV-2606-13496:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-15805:start -->
- `SF-2026-ARXIV-2606-15805` — Daily `2026-06-15`；primary `arXiv:2606.15805v1`；Books review `books-review:SF-2026-ARXIV-2606-15805`。

  **已吸收的语义增量：** discrete diffusion并行commit需用pairwise compatibility修正marginal confidence，避免独立高置信token组成冲突configuration
<!-- daily-books-trace:SF-2026-ARXIV-2606-15805:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-06560:start -->
- `SF-2026-ARXIV-2607-06560` — Daily `2026-07-08`；primary `arXiv:2607.06560v1`；Books review `books-review:SF-2026-ARXIV-2607-06560`。

  **已吸收的语义增量：** 新增证据边界：Convert heterogeneous annotations into a shared sample contract—visual inputs, natural-language task/schema instruction, and a text/image/mixed response that can be deterministically decoded back into boxes, masks, dense maps or camera records—so one generative model can learn many vision tasks without task-specific heads. 该 delta 已进入 `books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#L183`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-06560:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607.27372:start -->
- `SF-2026-ARXIV-2607.27372` — Daily `2026-07-30`；primary `arXiv:2607.27372v1`；Books review `books-review:SF-2026-ARXIV-2607.27372`。

  **已吸收的语义增量：** 新增证据边界：Explorative Modeling factors the training loop over multiple candidate matches and trains on the selected match, making sampling during training closer to inference-time mode commitment. Exploration becomes a third compute axis, but multiplies candidate-generation cost and introduces selection bias; author scaling curves do not prove a universal replacement for AR or diffusion. 该 delta 已进入 `books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#L211`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607.27372:end -->
