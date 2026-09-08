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

还要把“持久条件副本”与这两者分开：一种迭代生成分支会保存选中的 clean-token 假设并持续覆盖后续 denoiser 输入，但底层 noisy state 仍可变化，最终输出也重新读出，而不是直接复制该假设。它用较稳定的上下文协调并行位置，代价是错误假设持续影响后续步骤；条件保留时间、底层可修改状态与外部输出提交必须分别定义，不能因算法称其为 commitment 就提前向用户承诺。

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

### Diffusion Constrained Decoding 必须验证“仍可完成”，而不只是当前合法

自回归生成每次只提交下一个 token，因此 grammar-constrained decoding 可以从当前 parser state 枚举合法后继；
masked diffusion 同时为多个位置提出分布，若只检查刚填入的 token 是否局部合法，provisional sequence 仍可能进入
再也无法补全为合法句子的死状态。约束变化后，admission 需要从“当前 token 合法”推进为“加入该 token 后，剩余
mask 仍存在至少一条可完成路径”。

一种受限分支是在每轮 proposal 时利用所有位置的并行分布做 lookahead：diffusion model 只拥有候选概率，grammar
automaton 拥有语言状态与可达性，verifier 决定 proposal 是否保留，runtime 仍独占最终 commit。这样保留了并行
proposal，却新增 lookahead search、grammar 编译、长度/终止状态和 mask ordering；grammar 复杂、可达性检查昂贵
或目标不是形式语言时，延后到完整 block 验证或使用自回归 constrained decoding 仍更简单。exact-v1 只在四个
dLLM 与三个 benchmark 上支持 syntactic-completability 机制，不证明语义正确、任意 CFG 的成本或生产尾延迟。

<!-- source-family:SF-2026-ARXIV-2602-00612 -->

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

### Output Decoder 是独立的版本化 Generation Artifact

只统计 latent denoiser 或 token generator，在 decoder 轻量、输出分辨率固定时足以近似端到端成本；视频生成中，VAE decoder 可能独自占据显著 latency 与 memory bandwidth，且它的结构、压缩率和精度会改变最终画面。generation identity 因此不能止于主模型 checkpoint：latent shape/scale、decoder revision、operator/kernel、precision、resolution 与 frame count 必须一起进入 artifact 和 evaluation contract。主生成器拥有 latent proposal，decoder 拥有 latent-to-output transform，只有最终媒体通过质量和格式 gate 后才算 committed output。

channel pruning、operator replacement 与 distillation 可以缩短 decode，却会引入重建误差、时序闪烁、分辨率/帧数外推失效和硬件特化；主模型质量不变也不能证明最终输出等价。decoder 不是瓶颈、质量容忍度低或运行条件离校准域很远时，应保留原 decoder 或逐级 fallback。优化必须报告完整 pipeline latency 与最终质量，而不能把 decoder microbenchmark 当成整个生成系统加速。

<!-- SF-2026-ARXIV-2602-19161 -->

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

因此，直接把已有 sampler 的步数调小，与专门训练少步生成器不是同一个优化。后一条分支可让冻结 teacher 评价 student 自己走到的中间状态，再把纠正信号用于训练指定步数的 student；它用离线 teacher/critic 计算和额外模型版本换较短的在线轨迹，但没有消除分布偏移，换步数也未必还能复用同一 student。比较时必须同时记录训练成本、实际网络求值次数及在线质量：一步更新可能包含额外预测或 guidance forward，不能把 step 数直接当 latency。

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

固定 cache schedule 还假设不同 sample 与 timestep 对误差同样敏感；当生成难度和 denoising phase 变化时，这会在简单样本上浪费重算、在高敏感 step 上累积偏差。另一分支把 `reuse / recompute` 建模为 trajectory-conditioned sequential decision，并将 policy 与轻量 error corrector 分开：前者分配计算，后者只修正已选择复用的状态。二者必须共享 state/step identity、quality budget 与 fallback frontier，不能用 policy confidence 代替 correctness。

学习式 cache control 用额外训练、policy drift 与 corrector bias 换取 sample/timestep 自适应；prompt 分布、sampler 或 backbone 变化后需要重新验收。事件时证据覆盖 FLUX.1-dev、DiT 与 CogVideoX 的作者配置，不能把 headline speedup 外推为生产并发收益；低流量、短 trajectory 或校准不足时，固定 schedule 和 full recompute 仍是更可验证的基线。<!-- source-family:SF-2026-ARXIV-2607-29398 -->

### Diffusion Serving 不能直接复用 AR Token Queue

AR serving 的 ready unit 通常是“某请求的下一个 token”；masked diffusion 在同一 denoising step 共同更新多个位置，step difficulty、收敛进度和 CPU dispatch 成为新的状态。Batching 的收益来自多个请求共享一次 step forward，而不是把它们简单塞进同一 token queue；admission 需要同时约束 mask ratio、remaining steps、output budget 与 quality policy。它提高并行机会，却引入 step-level straggler、批间不同步和 dispatch overhead；短输出或单请求时，普通逐请求执行可能更简单。`arXiv:2608.23807v1` 的 LLaDA-8B + D2F LoRA、单 H200、GSM8K/HumanEval 只支持该 operating point，不能证明质量对任意 batch 都不变。

<!-- source-family:SF-2026-ARXIV-2608-23807 -->

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

### Conditional Guidance 把 Diffusion 并行策略变成逐 Step 状态

空间 patch data parallel 容易在边界引入 artifact 和 All-Gather，固定 pipeline parallel 又会让跨 step 的旧估计累积；
它们在并行形态固定、分辨率和拓扑稳定时仍是可预测基线。conditional diffusion 同时计算 conditional 与
unconditional denoising path 后，多出一条与图像 patch 不同的切分轴：两个 path 可以分到不同设备，随后再合成
guidance update；当两条 path 的 denoising discrepancy 随 step 改变时，runtime 还可以在 condition-based data
parallel 与 pipeline schedule 之间有界切换。

这使 parallel policy 必须绑定 denoising step、latent revision、conditional/unconditional branch identity、discrepancy
metric、threshold、GPU topology 与切换 epoch。model 产生两条 denoising state，scheduler 只提出 parallel plan，
runtime 在 step boundary 同步后 commit；任一 branch 缺失或版本不一致都不能继续合成。收益来自利用原本已存在的
guidance 分支，而不是免费减少模型计算；代价是双分支同步、metric calibration、切换 barrier、额外通信和随机
轨迹下的抖动。discrepancy 不稳定、单 GPU、无 classifier-free guidance 或固定计划更易捕获 graph 时，应回退静态
data/pipeline 或单设备执行。作者结果只覆盖 SDXL、SD3 与其双 RTX 3090 配置，不能外推其他模型、并发或 SLO。

<!-- source-family:SF-2026-ARXIV-2602-21760 -->

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

若生成中再插入槽位，旧位置与新画布的坐标映射、画布版本和 logits 必须一起绑定；比较分布时需明确哪些旧未决位置可比较，提交只能使用被选画布对应的预测，不能把旧画布 logits 当作新状态。以平均分布差异决定是否扩容是带额外 forward 与对齐成本的启发式，既不保证每个位置不变，也不保证原生成分布或最终延迟不变；固定画布仍是状态简单、容易验证的共存方案。

## 加速不能静默改变生成轨迹

缓存或跳步加速在多模态 Diffusion 中会复用旧的视觉与文本状态。旧状态足够接近时，它减少重复计算；随着轨迹推进，stale state 会让加速输出与未加速模型系统性分叉。因而“更快但 benchmark 仍可用”并不等于语义等价，运行时还要测量 state freshness、输出 agreement 与 refresh cost。

这形成一个明确的控制分支：短 refresh interval 提高一致性却回收较少计算，长 interval 提高速度却扩大漂移。控制器只能把 confidence 当刷新信号，不能当 correctness certificate；漂移超过预算时回退完整 refresh。该分支属于 iterative refinement，不应外推到具有不同状态语义的自回归 Decode。

### 加速后的输出必须与未加速轨迹建立一致性边界

缓存或跳步能减少 diffusion 的重复计算，但“最终观感尚可”不能证明它仍在执行同一生成过程：stale visual state 与已生成文本状态可能把内容推向另一条轨迹。运行时应把 refresh interval、state revision 与同模型 full-compute 输出的一致性作为联合验收量；缩短 refresh 可以提高一致性，却会交还一部分加速收益。该检查只约束近似分支的语义漂移，不保证两个随机样本逐点相同；一致性或 freshness 超界时应恢复更密集刷新或全量重算，固定 schedule 在分布稳定时仍是可预测基线。
<!-- source-family: arxiv:2607.29079v1; daily: 2026-08-03; semantic-body-binding: accelerated-generation-state-agreement -->

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

## Refinement 位置也可以成为条件计算状态

在并行 refinement 中，不同位置距离稳定状态的远近不同，继续给所有 token 相同 expert budget 会把计算浪费在已经收敛的位置。条件计算可以读取 block-relative position、当前 refinement step 与收敛 frontier，为未稳定位置分配更多专家容量；它没有改变最终 commit owner，却把“还需要多少计算”从固定超参变成运行时状态。收益是减少无效计算，代价是训练—推理联合校准、router 抖动和调度复杂度；短轨迹、负载稳定或状态估计不可靠时，固定预算仍是可验证基线。`arXiv:2608.01784v1` 只支持作者 Diffusion-MoE 配置，不能外推为所有生成模型的通用加速。<!-- source-family:SF-2026-ARXIV-2608-01784 -->

## Few-step Distillation 要在 Student 实际访问的状态上验收

把多个 teacher step 压成一个 student transition 时，离线 teacher trajectory 是合理起点，但 student 的早期并行提交会改变后续 context，使真实状态逐步离开监督分布。更稳妥的 on-policy 分支从 student 自己生成的 partial state 出发，由冻结 teacher 提出 outcome-aligned future candidates，并只提交仍保持 rollout outcome 的最长前缀；验证失败就缩短 transition。收益是减少 function evaluations，代价是在线采样、teacher 计算与一致性判定误差；高风险或状态漂移明显时，多步 refinement 仍是正确性基线。`arXiv:2608.02942v1` 只在作者数学和代码 benchmark 上支持该质量—效率前沿。<!-- source-family:SF-2026-ARXIV-2608-02942 -->

## 双向生成中的 Cache 是可变状态，不是只读前缀

diffusion 或 masked refinement 会反复修改序列两侧，传统只追加 KV cache 的不变量不再成立。复用稳定 affix 可以减少重算，但 request-specific anchor 与被更新位置必须重新计算，并把 timestep、mask 和版本纳入 cache identity。错误地沿用自回归前缀语义会产生静默污染；保守全重算仍是低复用或高变化率下的正确基线。
<!-- source-family: arxiv:2608.26140v1; semantic-body-binding: bidirectional-affix-cache-mutability -->

进一步的近似分支只复用 token identity 已冻结的 prompt K/V，并以 response state neighborhood 与 decoder margin 判断可变区域是否仍可复用。Prompt reuse 因而是受状态距离约束的 proposal，不是 AR 式 exact prefix：mutable response 必须刷新，越界就回退 full refresh。它用距离估计与误差校准换取较少重算，也会引入阈值漂移和静默近似误差；高风险输出或 state 快速变化时，完整刷新仍是基线。

<!-- source-family: arxiv:2608.08086v1; daily-trace: papers/2026/08/11/README.md; semantic-body-binding: reversible-response-cache-state-neighborhood -->

## Object Permanence 与 Addressable History 是两个 Gate

视频生成能够在短片段中维持对象外观，不代表系统拥有可寻址、可更新的长期环境状态。环形或有界历史机制可以扩展可引用的过去，但仍需分别验证对象身份持续性和历史容量；两者都通过，也不能自动推出 action-conditioned causal transition。它是生成状态管理的进化，不应被误写成完整 world model。
<!-- source-family: arxiv:2608.26794v1; semantic-body-binding: video-object-permanence-vs-history-capacity -->

## Reflection

生成范式不是从“串行”走向“并行”的单向进步史。系统用并行草拟换来了 mutable state，用修正换来了额外 forward，用更大候选空间换来了 verification 和 memory。真正的演进，是让这些成本与输出承诺被显式管理。

### Early convergence 与 high confidence 不是同一个 Commit 证据

并行去噪最初常用当前位置的边际置信度决定是否提前提交；它便宜，却把“这一步很确定”误写成“后续步骤不会再改变”。约束变化是多个位置共同修正时，单点高置信仍可能被后续条件关系推翻。更严格的 runtime 可以追踪一个 token 在连续 denoising steps 中是否已经稳定，把 early-convergence signal 与边际 confidence 联合用于 provisional-to-committed transition。

这会减少不必要的更新，却增加跨步状态、滞回阈值与误提交风险；稳定检测仍不是联合分布正确性的证明。检测不可靠、输出有外部副作用或 exactness 优先时，应延后到 block verifier 或完整 denoising 结束再 commit。该分支补充本章的 mutable-state 路线，不宣称它普遍优于 confidence schedule。[受限证据：arXiv:2605.10980v1]

<!-- source-family:SF-2026-ARXIV-2605-10980 -->

## Review notes

- 2026-09-01 可变 canvas 的状态绑定：<https://arxiv.org/html/2608.30922v1> §3.2、Algorithm 与 C–F。平均 JS 不覆盖已提交/新增位置，不构成无损证明；always-expand 对照同时改变判定和 expanded forward，不能隔离 JS 判定因果。三模型四任务及 MI210 测量不外推生产 SLO。

- `SF-2026-ARXIV-2609-04531`，Status: Experimental：exact-v1 §2.4、§3.1/3.3、§5与B.5支持student中间轨迹监督及按K分别训练的少步分支。仅采用公开代码生成设置下的机制；不采用任意权重下稳定反向映射保证，也不把K、NFE与wall-time等同。https://arxiv.org/html/2609.04531v1

- `SF-2026-ARXIV-2602-00612`（Status: Experimental）：primary=`arXiv:2602.00612v1`；Method=`§3 Methodology`；Evaluation=`§4.1 Benchmark`；Non-proof=`§7 Conclusion`。证据只支持 dLLM 在所测 CFG benchmark 中用并行位置分布做 lookahead、拒绝不可完成 proposal；不证明语义正确、任意 grammar 复杂度或生产延迟。
- `SF-2026-ARXIV-2602-21760`（Status: Experimental）：primary=`arXiv:2602.21760v1`；Method=`§4.2 Hybrid Parallel Inference Framework；§4.3 Adaptive Switching via Denoising Discrepancy`；Evaluation=`§5.2 Main Results`；Non-proof=`§5.3 Ablation Study`。证据绑定 SDXL/SD3、作者实现与双 RTX 3090，不证明其他 diffusion family、拓扑、并发和 tail-SLO。

- `SF-2026-ARXIV-2602-19161`（Status: Experimental）：exact-v1 的 §3.1～3.3 定义 VAE decoder pruning、operator optimization 与三阶段 distillation，§4.1～4.3 及 Appendix B.2～B.3 给出作者质量、消融与 pipeline latency，§5/Impact Statement 不证明跨 decoder、分辨率、frame count、硬件或端到端生成等价。https://arxiv.org/html/2602.19161v1

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

- `arXiv:2609.01043v1`（2026-09-02 Daily）：[§4.1、Appendix A](https://arxiv.org/html/2609.01043v1)支持 input-overlay-only 与 mutable noisy state、final argmax 的区别；stored label 不直接复制到输出。§4.2–4.3的oracle/条件独立理论不认证 learned sampler 闭环无偏，§5及Appendix D的GenPPL/entropy排序不等任务正确率或线上latency；仅吸收三类state/commit接口边界。

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
