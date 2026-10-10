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

顺序还会改变每个 conditional 的学习难度，不只是串行步数。对没有天然输出顺序、且依赖结构可核的离散变量，可以先学习 MRF，再比较其诱导的 AR parent sets；未来变量被边缘化后可能产生高阶依赖，原图邻居少不等当前 conditional 的 parent 少。一条受限启发优先减小最大 parent 数，再减少达到该最大值的 conditional 数；顺序、图估计、条件模型阶数与样本身份必须共同冻结。

[有限 Ising 对照](https://arxiv.org/html/2602.20394v1)分开有限样本统计误差与截断高阶项的系统误差，并用多数据集/采样重复验收 moment error；它不是全分布 fidelity、全局最优排序或 LLM 顺序改写保证。图学习、条件拟合与排序均付费，近似结构和难采样分布会削弱收益；依赖不可核、自然顺序具有语义或误差/费用不合算时，保留原 raster/自然顺序和全条件模型，不从图稀疏直接授并行或无损采样。<!-- source-family:SF-2026-ARXIV-2602-20394 -->

减少这段 serial depth 的一条分支，是把每步的条件目标从单 token 改成一个 `p×p` patch 的联合分布：跨 patch 仍按 raster-order AR，并以 block-causal mask 组织条件，但 patch 内不再把各 token 当作独立分类抽样。一个 conditional diffusion/flow head 在同一 patch 的 binary-token 空间联合迭代，学习组内依赖；binary bit 的组合数不等实际可用容量，学得的 head 也不认证精确联合采样。[受限 next-patch 对照](https://arxiv.org/pdf/2602.14041v1)支持这条 factorization/预测接口，而非只凭增加并行宽度消除依赖。它用 head 迭代、额外训练与块内计算换更少的外层 AR steps；更大 patch 的吞吐改善可以伴 FID 退步，外 family 的 backbone 或训练不同也不能唯一归因该机制。局部一致性、head 质量或完整费用不满足目标时，应缩小 patch 或保留普通单-token AR，而不是把并行提交直接当作无损加速。<!-- source-family:SF-2026-ARXIV-2602-14041 -->

第 23 章给出了表示的重构和语义契约，本章还必须问一个不同的问题：**这种表示是否容易被当前生成路径逐步预测？**
视觉 encoder 的高维连续 latent 即使能重构图像，单个 latent token 的分布仍可能比低维 VAE latent 难建模。
在 teacher forcing 下，AR 看到真实历史；生成时却要以自己的连续预测作下一步条件，高维误差会随步骤进入后续条件。
因此，重构分数不能替代生成质量、误差滚动或推理成本的验收。

一种受限分支先校准 token 分布，再在训练时扰动真实历史，让预测器练习接住偏离数据流形的前缀；它以更复杂的
表示归一化和训练噪声换生成容错，却不能靠更低训练损失证明最终图像更好。若扰动不匹配真实 rollout、
生成质量仍落后或稳定性优先，沿用重构导向 VAE 仍是合理选择。[RAE-AR 的图像实验](https://arxiv.org/html/2604.01545v1)
只支持所测 encoder、AR 架构、训练设置与指标下的这条表示—生成张力；其消融中归一化单独使用并非总有益，
结果也不证明高维语义 latent 已普遍追平 VAE。<!-- source-family:SF-2026-ARXIV-2604-01545 -->

当 AR 的一步变为预测下一尺度的视觉码时，历史扰动训练还取决于 decoder 实际读取什么。可以扰动已有尺度的 code indices，要求恢复原 top-1 目标；但旧 VAR 的 accumulated-feature 输入不必与统一 decoder 的这项 self-correction 目标兼容。受限对照中该组合退步，直接 residual/code-index 输入则改善，作者把 feature complexity 作为解释假说，而非已识别的唯一原因。因此 tokenizer/codebook、尺度历史、输入表示、扰动及目标必须与 decoder 分别冻结和配对验收，不能由某种 codec 易重构就推断修正训练一定有效。它支付额外训练和输入适配成本；质量或兼容性不足时，保留原 scale-history 输入、普通 teacher forcing 或重新训练，而不授离散码普遍优越。可选的 diffusion refiner 是另一消费分支，可能改局部结构或身份并另付采样成本；理论 FLOPs 比例不能代替同质量的端到端墙钟。<!-- source-family:SF-2026-ARXIV-2601-02204 -->

尺度历史还改变稀疏计算的坐标：在固定网格上复用已选 flat token ID 很简单，但下一尺度的 query 区域变大，历史 KV 又来自不同尺度，直接复制这些 ID 不再表示同一关系。一个受限分支先把 query 区域映射到新网格，再把 KV 索引分解为来源尺度与局部坐标，按相对尺度对齐后投影；稀疏 pattern 的迁移与上一步 dense/sparse 输出差额的近似重用是两个对象，后者不能冒称精确 Attention 或无损 cache。[SparVAR 的必要方法与对照](https://arxiv.org/html/2602.04361v1)支持这项分工，但不消除细节损坏、误选和尺度失配；映射、gather、额外 cache 与校准也须计入端到端预算，局部 kernel 加速不是 request 收益。坐标或质量验收失败时，应重新选择、增加保留范围或回退 dense 计算，而不为省算力静默改变生成尺度与历史身份。<!-- source-family:SF-2026-ARXIV-2602-04361 -->

在同一尺度内，稀疏化还要决定哪些 layer/token 可以少算，而不是只减少生成尺度。一个分支先用低 entropy token 比例定位开始剪枝的尺度，再用代表尺度的 SVD 统计区分 global/detail layers，最后用 token entropy 决定细粒度保留率。三层选择共同消费原尺度历史；entropy 是受测语义 salience 的 proxy，不是真值，正的最小剪枝率也不授 global layer 完全不剪的硬保证。[ToProVAR 的必要控制](https://arxiv.org/html/2602.22948v1)中粗 scale+layer 的 GenEval .679、加入 token 后 .690，说明粒度与质量目标需要共同验收，而非越少 token 越好。<!-- source-family:SF-2026-ARXIV-2602-22948 -->

计算这些统计本身也付费：直接物化 attention entropy 会破坏原 fused attention 的内存路径，可在 online softmax 中累计额外 xlogx 统计，并另计代表尺度的 SVD。Infinity-2B 的同配置对照 without FAE1.10秒、with FAE .61秒；8B 的 SVD 全层约49.84ms，不能把它当免费或普遍常数。作者单 L40/Batch1 质量—延迟结果并未同时保持所有 preference/DPG 子指标，精度和 serving SLO 未在必要材料披露。统计失准、细节退步或总费不值时，应增加保留率或回到原 dense/frequency 路径，不把剪枝 heuristic 提升为语义保持保证。

逐 token 概率可预测，还不等于部分 prefix 已能被质量 sensor 辨认。第 23 章的 coarse-to-fine 表示若经训练形成早期全局语义，可以把候选 prefix 重建成中间图，再用 verifier 保留 beam；grid/raster prefix 只覆盖局部，填补后的中间图可能误导评价，更适合完整 Best-of-N，或支付 lookahead 成本后再判断。因此 representation ordering、partial reconstruction 与 search protocol 必须一起选择，不能把任意一维序列称为语义有序。<!-- source-family:SF-2026-ARXIV-2604-15453 -->

这种搜索支付重复 detokenization、branching 与 verifier 成本；NFE 中一次生成和一次评判并不具有相同 wall-clock，多步 flow decoder 的重建甚至可能成为主要瓶颈。更多搜索也可能提高自身 verifier 分而降低外部质量，缺失的语义 prior 不能靠无限搜索预算普遍补回。ordered prefix 不稳定、解码成本无法摊销或 verifier 未在独立指标上验收时，保留普通 AR、完整 Best-of-N 或 grid/lookahead 路径。[SoTo 的受限图像比较](https://arxiv.org/html/2604.15453v1)支持这条选择条件，不证明视频、文本普遍受益，也不证明无需预训练的生成。

空间生成还可以把一步从token改成相互重叠的crop/ring：从内部向外扩展，新边缘并行生成，旧区域继续修正。历史区和new edge使用不同可见性mask，避免尚未生成的边缘倒灌旧区；这改变了生成与修订的单位，而非仅替换raster顺序。重叠crop的条件分解本身不授任意token联合分布的精确性，修改旧区也使依赖它的attention state重新失效，不能直接继承append-only KV或把并行称为全无mask。<!-- source-family:SF-2026-ARXIV-2512-24639 -->

该路径支付重叠计算、历史修正、训练/生成条件混合和mask/state管理成本。顺序加入模块的消融不等全factorial，更多steps也不是全部质量指标单调提高；未核code/cache实现、硬件和并发时，不采用吞吐倍率或免费revision结论。细节反复改坏、重算难以摊销或要求稳定流式commit时，保留普通AR、完整候选搜索或固定生成块，并按真实质量与端到端预算选择，不让空间并行替代状态验收。

局部视频编辑还有另一种计算分工：固定待编辑的时空 mask，适当膨胀后仅 gather 对应 noisy latent 与条件 token，让 local 分支生成并 scatter 回输入 latent；它不反复修改任意旧区域，而是把局部改写范围与全局控制分开。单靠局部 token 可能丢失光照、位置和运动背景，[EditCtrl 的受限分支](https://arxiv.org/html/2602.15031v1)因此再读取降采样到256×256的全局背景，通过轻量 temporal 控制提供上下文，训练先学 local、再加入 global，避免从头联合训练的不稳定。这里没有“只付 mask 成本”：完整输入编码、global 分支、膨胀与边界 blending、VAE 解码仍付费，mask 也不是完美语义边界。global 带来控制收益同时把局部比较 FPS 从4.90降到4.67，LPIPS/CLIP 亦非全部优于 VACE；作者 FPS 排除 VAE 编解码，不能签发高分辨率端到端实时保证。高速运动、边界污染或全局语义失配时，应扩大检查范围、重新验收 mask 或回退全视频/普通编辑路径；本文的条件性 gather/scatter 分工不认证未遮区域零变化。<!-- source-family:SF-2026-ARXIV-2602-15031 -->

局部文字生成还须把同一 ROI 的监督分到不同 consumer，而不是把局部 latent 的匹配直接当作字形已正确：一种分支在文字 mask 内重权 latent velocity loss，另在 VAE 解码后的 RGB 图上比较边缘形状；前者约束 denoising 表示，后者约束最终像素的局部形状，两者均不签发文字语义或人类形状真值。字符条件、mask、decoder 与 edge extractor 的 identity 共同限定目标，错误 mask/参考字形或边缘也可能把错误约束得更强。[受限文字编辑对照](https://arxiv.org/html/2601.08321v1)的顺序消融不是完整因子归因，OCR 改善不能抵销其他感知指标退步；训练更新范围的原文冲突不作冻结 recipe。VAE decode、edge 提取、teacher-label/字形条件与训练均付费；mask 不可靠、文字/背景质量冲突或预算不足时扩大检查范围，回退完整编辑与独立 OCR/人工验收，不让 latent 或边缘 loss 互相认证输出。<!-- source-family:SF-2026-ARXIV-2601-08321 -->

### Autoregressive 不必等于 Append-only Final Text

经典 AR 每步直接提交一个 final-order token，因此最容易 streaming 和复用 KV；要在前文中修改内容时，通常只能重新生成。一个条件分支是不再对“最终文本顺序”自回归，而是对可变 canvas 的 edit-history actions 自回归：`INSERT(token)` 写入当前位置，`MOVE(Δ)` 改变 cursor，`STOP` 提交当前 canvas。模型仍然保持单步 next-action interface，却可以回退并在中间插入内容；可修订性因此来自 action/state 表示，不来自并行 denoising。

这条分支使“AR 还是 Diffusion”不再是“只能追加还是能修改”的同义词，但交换的不是免费修订：解码仍在 action space 中串行，移动和冗余编辑会增加步数，训练依赖编辑轨迹，而 mutable canvas 使 prefix KV、可见输出和 rollback 都需要新 identity。当输出必须低延迟流式提交、编辑轨迹难以构造或平均 action count 不能覆盖修订收益时，普通 append-only AR 仍是更强的旧路径。`arXiv:2609.20830v1` 只支持其 cursor-action 机制、小规模 continuation 实验与作者评判协议，不证明大模型质量、长文档 editing、真实 serving latency 或对 diffusion 的普遍优势。

<!-- source-family:SF-2026-ARXIV-2609-20830 -->

### 视频 AR 可以分离帧内精确路由与跨帧记忆

对视频把所有历史 token 放进同一个 softmax，最忠实但跨帧成本随序列迅速增长；只保留压缩 recurrent state 又可能丢失当前帧细节。一个分层分支让帧内 token 继续使用 exact local softmax，同时以 linear recurrent memory 承载跨帧历史。关键的状态边界是：同一帧的所有 token 都读取相同的 pre-update memory，只有 clean forward 完成后才提交下一帧 state；否则帧内并行会被隐式执行顺序污染。

这条路径以更低跨帧成本换 memory drift、历史细节损失和新的 clean-pass commit 纪律。长程一致性不足、状态异常或任务依赖精细历史时，应回退 full attention、短窗口重算或两者混合。现有证据只支持作者的视频模型与受测数据，不证明 linear memory 能替代任意视频历史，也不授权 runtime 偷改帧边界。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-16579:start -->
视频自回归可以让帧内 softmax 保持精确，而把跨帧历史演进成在 clean pass 后提交的 recurrent memory。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-16579:end -->

另一条流式视频分支不将所有历史立即压入同一 recurrent memory，而让近期帧保留局部窗口、较远帧在淘汰前先累积进线性 history state；局部窗口还可按 block importance 稀疏计算。状态移交次序是先更新历史统计、再释放原 KV，不能先淘汰后假设记忆已经保留。近期可寻址条目与压缩远期历史承担不同责任，固定大小统计不意味着任意旧帧细节仍可找回，也不是可控环境状态的证明。

把这一结构直接装入尚未形成稳定表示的少步生成器，可能压缩噪声并加剧漂移。因此训练可先用 dense attention 蒸馏，再启用 hybrid history/local paths；训练与推理共同采用相同 temporal position cap，并以同初始 noise 的 teacher rollout 对首步 latent 作正则。这个分支支付额外训练、teacher目标构建和历史近似成本，不是免费缩小窗口。作者 Wan1.3B、单 H100、832×480及30秒定量协议只支持所测质量/执行，长视频展示不证明无限稳定，更强 sparsity 也有退步。精细历史或位置外推验收失败时，应保留更长窗口、dense基线或重新训练；本章拥有生成状态迁移，第25章仍须另验 action-conditioned environment transition。

<!-- source-family:SF-2026-ARXIV-2604-10103 -->

历史压缩还有一条不同于 recurrent state 的视频分支：保留固定长度的当前 noisy window，把历史 clean frames 按远、中、近期采用不同的时间与空间 patch 粒度，再用首帧 anchor 约束外观。它让近期细节与远期轮廓承担不同责任，而不是把所有历史保成同精度 token；局部位置重索引限制了接口长度，却不恢复已经压缩掉的旧细节。

推理继续消费自己生成的历史，因此训练可对历史逐帧加入扰动，模拟累积误差而非只见干净 teacher-forcing 条件。该分支支付额外训练、历史压缩与 anchor 依赖，并与 coarse-to-fine 采样、少步蒸馏分别验收；降低 motion 可能改善某些 smoothness/aesthetic 指标，不等于所有质量都更好。[Helios v1 §3.1–3.3、§5.1–5.4](https://arxiv.org/html/2603.04379v1) 的去 anchor、去 frame-aware corruption 消融支持受测长视频中的局部收益，不证明任意长度稳定或通用实时吞吐。精细历史、运动或身份一致性退化时，保留更短生成段、更大历史窗口或既有 dense 路径。<!-- source-family:SF-2026-ARXIV-2603-04379 -->

外部参考条件也不能直接当作已经生成的历史：历史 KV 表示自产轨迹，参考图像/控制 latent 却可能要被所有未来 chunk 同时访问，其双向可见性、位置与缓存责任不同。[流式 VACE 的受限适配](https://arxiv.org/html/2602.14381v1)把参考条件放到并行 Context Blocks，输出 residual hints 给只处理视频轨迹的生成分支，从而不必将参考 token 塞进 generated-history KV。条件 encoder 的 inactive/reactive 两条流还需分别维护缓存；inpainting 的 reactive cache 可造成 ghosting，因而跳过该缓存，不能把条件分支缓存一概视为安全复用。已有权重可重用不等于没有运行成本：作者局部配置的单 chunk 从539增到698ms，另一配置 inpainting 从741增到958ms，测量仅 inference 的15 chunks、另有3 warm-up，不含完整流式端到端责任。reference-to-video fidelity 可明显退化，较长序列仍需 reanchor；条件身份或质量验收失败时，保留原完整条件生成、短段重算或重新锚定，而不把训练免费与推理实时、历史正确性混为一谈。<!-- source-family:SF-2026-ARXIV-2602-14381 -->

历史压缩是否可用，还取决于 encoder 学习过什么检索目标。只重建两端 keyframes，可能让中间帧的信息在压缩时消失；一个分支在预训练时随机抽取任意历史时间位置，要求从压缩表示重建这些帧，再把 encoder 接入 AR 生成。低分辨率分支保留轮廓，高频 residual 另投到生成器较大的 hidden space；这是在信息目标和表示路径上补偿细节，不是证明固定长度 token 已无损保存所有旧帧。

随机位置可重建也不等于任务相关 world state 可恢复，更不保证消费自产历史的无限连续镜头稳定。额外 encoder 预训练、高频分支与适配都要计入总预算；相同 AR 训练步数不能当作相同总训练成本，重建指标、外观身份和运动一致性也须分别验收。[Frame Preservation 的受限视频对照](https://arxiv.org/html/2512.23851v1)支持所测模型中的这一目标分工，但密集剪辑数据中的局部漂移改善不授予长单镜头保证，较多上下文仍增加计算。任意位置检索或生成质量失败时，保留原帧、更长近期窗口或较短生成段；第25章仍须另验动作条件下的环境状态，而不能由帧重建代替。<!-- source-family:SF-2026-ARXIV-2512-23851 -->

## Diffusion 与 Flow Matching：用迭代更新组织生成状态

连续 diffusion 从噪声逐步 denoise；离散或 masked diffusion 从 mask/noise state 逐步恢复 token。每轮可以同时更新许多位置，因此 serial steps 不必等于 token 数。

它的优势不是“完全并行”，而是把串行维度从 output length 改成 denoising/refinement steps。代价包括：

- 多轮 full or block forward；
- 中间状态可变，cache reuse 更困难；
- streaming 前必须定义哪些 token 已 committed；
- 迭代 schedule 会影响质量、延迟和稳定性；
- likelihood、sampling exactness 和 stop condition 可能更复杂。

图像和视频往往容忍整体画面同时从粗到细修正，且用户不要求逐像素 streaming，因此 diffusion 的系统契约较自然。文本要求稳定前缀和低延迟流式输出，mutable tokens 的成本更明显。

迭代路径也不规定每轮必须用全 Attention 主干。固定 diffusion 目标与采样接口后，一个卷积分支可在低分辨率 latent 上用大核 depthwise convolution 混合空间，再以 pointwise 扩张、响应归一和多尺度 skip 组织通道与上下文；class/time 条件通过自适应归一的调制进入 block。把通道扩张放在 depthwise 之后，可以避免在扩张空间支付该卷积成本，但条件调制、多尺度 activation、训练与最终 codec 仍付费。[有限 ImageNet 对照](https://arxiv.org/html/2603.09408v1)支持这条主干选择，不把较少 forward FLOPs 或训练步数当端到端加速，部分质量指标和更大 kernel 仍反退，也不能据此推出视频或任意条件生成同样占优。局部归纳偏置、条件质量或完整成本失配时，原 U-Net、DiT 与更强全局交互仍应共存；比较的是同一质量目标下的完整配置，而不是把卷积与 Transformer 排成必然替代的年代顺序。<!-- source-family:SF-2026-ARXIV-2603-09408 -->

每轮主干还可以分开输出网格与内部计算人口：保持 N 个 spatial tokens 的短 head，从它们读取到 K 个 learned latent tokens，让主要 blocks 在 latent 空间工作，再通过 Write 回原 N 个位置并完成短 tail。分组 Read/Write 限制跨域 attention 的范围和成本，但 head、tail、跨域搬运与最终 codec 仍随输出尺寸付费，不能说完整生成成本已与分辨率解耦。若希望同一 artifact 支持多个 K，可以在训练时随机保留各组 latent 的前缀；同一轮各组共享前缀长度，使运行预算成为经过训练的接口，而不是从已有 DiT 任意删 token。早位置接受更多训练只是一种重要性组织方式，不认证每个 latent 的语义，也不是 runtime 为各区域独立分配预算。

这条分支保留输出的细网格，以内部 latent 人口换取质量/计算旋钮，却需要新的 Read/Write、分组与 prefix-budget artifact identity。[受限图像实验](https://arxiv.org/html/2603.12245v1)用相近训练 FLOPs 对齐时同时改变了有效 batch，不能把收益只归因于 prefix 顺序；大模型迁移又支付蒸馏与额外训练成本，低预算仍会损失细节和条件质量。低预算也可充当 guidance 的弱分支，但它仍需第二次模型调用，并改变原 full-budget CFG 的 velocity 近似，不保证相同采样行为；原文视频实验未验证同样的 multi-budget 合同。预算或分组未经训练、条件失配、细节退步或端到端费用不值得时，应回到完整 latent 人口、原全空间主干与已验证 guidance，而不是用较低 FLOPs 代替质量或在线 SLO 验收。<!-- source-family:SF-2026-ARXIV-2603-12245 -->

迭代路径的验收还不能只看沿途点的density：高维分布的mode未必位于典型样本区域，较高learned likelihood也不自动代表较好的感知过渡。一个受限诊断分支先把两个endpoint沿probability-flow ODE映到噪声空间，再演化并重参数化连接它们的string；用有限温度的局部walkers、区域拒绝与EMA估计路径，能比较mode-seeking与更接近样本区域的过渡。这是learned-score下的有限路径探索，不是精确物理能量路径、普遍收敛或保持原采样分布的保证。[图像latent实验](https://arxiv.org/html/2602.22122v1)展示低likelihood路径也可能更像样本，但未以独立人审或完整质量指标认证这一判断，原文空的温度schedule区间不作为recipe。多string点、walkers、ODE求值、重参数化和小步长增加计算，近数据区域的score误差仍会误导路径；质量或成本不可验时，保留原始sampler、较短路径与独立感知评价，不以likelihood单项择优。<!-- source-family:SF-2026-ARXIV-2602-22122 -->

### DDPM：从可采样的加噪过程得到训练目标

先固定数据空间与尺度；第23章决定 x_0 是像素还是 latent，这里把它当作干净样本，c 是条件。DDPM 选择逐步高斯加噪：beta_t 是第 t 步噪声方差，alpha_t = 1-beta_t，alpha_bar_t 是前 t 步 alpha 的乘积。由高斯组合可直接抽样任意噪声层级，无须训练时完整走过前向链：

```text
q(x_t | x_(t-1)) = N(sqrt(alpha_t) x_(t-1), beta_t I)
x_t = sqrt(alpha_bar_t) x_0 + sqrt(1-alpha_bar_t) epsilon
epsilon ~ N(0, I)
L_simple = E_(x_0,c,t,epsilon) ||epsilon - epsilon_theta(x_t,t,c)||^2
```

一次训练更新只需抽数据、时刻和噪声，让网络预测加入的 epsilon。这个常用简化损失对各时刻的权重不同于原始变分界，不能把普通噪声 MSE 直接叫作精确负对数似然。噪声 schedule、时间采样和预测参数化因此共同定义了目标，不是部署时可任意替换的标签。

去噪目标也可以用于修订不希望继续生成的具体实例，而不先把它概括成一个可擦除的 prompt 概念。在一个受限分支中，先为原图制作保留背景结构、改变目标身份或属性的 surrogate；训练仍把原图加噪后的 x_t 交给网络，却用这个 x_t 与 surrogate 计算新的噪声 target。这与直接把替代图加入普通训练不同：输入来源和所指 clean endpoint 被有意拆开，改变了局部去噪映射。原图、编辑目标、surrogate revision、噪声 schedule 和预测参数化应共同进入修订身份；其余样本仍支付 retain loss，时间权重和冲突梯度处理只提出保持—修订的取舍，不认证整条生成分布无损。

[Prompt-free instance unlearning 的有限原证](https://arxiv.org/html/2603.10445v1)只覆盖一个无条件 DDPM 和一个条件 SD3，后者用相同 prompt 的100个生成图代替不可访问的训练 retain 数据；这不是全模型能力保留的证据。目标图加噪再重建后的 SSCD 下降、同 seed 输出相近与 FID 是不同 proxy，不能由阈值通过宣称所有条件下再生成概率为零或训练贡献已彻底移除。更强编辑也损害保留质量，surrogate 制作、双目标反传、adapter 与重复评估都计费；目标身份、retain 覆盖或质量不可信时，停止这条修订、保留原模型与独立过滤或人工核验，不能由替代图和局部相似度自签删除完成。<!-- source-family:SF-2026-ARXIV-2603-10445 -->

时间采样还可以由训练中的去噪误差在线分配：按噪声 σ 分箱，维护 FIFO 残差、EMA、最低样本数及刷新规则，再把目标强调量 ρ 换成采样密度 π∝ρ/w，其中 w 是单样本 loss 权重。即使 w 固定，训练期望中实际进入的是 πw，因此这在重分配 effective objective，而不是自动保持原目标的无偏 importance sampling。Gaussian I-MMSE 把 Bayes 最优去噪误差与 entropy slope 联系起来；当前网络的 MSE 同时包含模型未拟合误差，不能直接称为测得真实 entropy。<!-- source-family:SF-2026-ARXIV-2602-18647 -->

[在线分箱方法与反侧](https://arxiv.org/html/2602.18647v1)复用已有 forward 的残差，但 buffer、插值、刷新和估计失准仍有费用；低噪声 gate、稀少分箱或陈旧 EMA 会改变覆盖，未显式保留最小采样质量时还可能缺少更新该箱的机会。受测图像 EDM 中，固定 w 只换 π 的 continuous 对照与同时换权重的 discrete 对照须分开，达到基线 FID 所需的训练样本数也不等 wall-clock；部分数据无加速或质量更差，不授普遍最优分配。proxy 不可靠、覆盖不足或质量回归时，保留已验收的固定 sampler/权重与完整采样路径，并独立检查训练分配和推理网格，而不是由一个 entropy 类比批准同时换掉两者。

采样时没有 x_0 可用。网络的噪声预测被换算成反向高斯均值，采样器从近似标准高斯的终态出发，依次更新：

```text
mu_theta = (x_t - beta_t / sqrt(1-alpha_bar_t)
                   * epsilon_theta(x_t,t,c)) / sqrt(alpha_t)
x_(t-1) = mu_theta + sigma_t z
z ~ N(0,I) for t>1; z=0 at the final sampling step
```

sigma_t 和时刻序列属于采样器配置。训练可随机抽一个时刻，不意味着部署能把整条反向链省成一次 forward；跳步、换方差或换求解器都需要重新验收。加噪分布、网络拟合与有限步采样各自可能引入误差，后文的少步、纠偏和缓存都建立在这三个对象已分清的前提上。

噪声还可以按空间位置分配，而不只按采样时间调整。一个受限 restoration 分支用输入图像产生可学习 map，经 latent 投影后调节 Gaussian perturbation 的局部强度；另一条文本条件描述退化与内容，分别改变去噪输入和语义条件。这里 map 与描述都只是模型给出的 proposal：投影不保原像素排序，较大的扰动不认证真实不确定性，语义更自然也可能偏离原观测。[有限超分对照](https://arxiv.org/html/2603.09125v1)中，加入质量描述改善部分感知代理，却损失部分忠实度，不能把代理分数当作真实细节恢复。Map/文本生成、额外编码、训练与解码均计费；退化域、空间校准或保真验收失配时，保留均匀噪声、原条件模型和更保守的重建路径，不从单步去噪签发完整低延迟或原信息无损保证。<!-- source-family:SF-2026-ARXIV-2603-09125 -->

对于逐帧视频，条件 c 的历史部分在当前帧的 denoising steps 之间没有变化，但 causal diffuser 仍可能每步重复处理它。一个替代分支把历史计算从反向链中拆出来：causal encoder 每帧读取一次历史 clean frames 与控制条件，帧内双向、帧间因果地产生固定 context；framewise decoder 每一步将该 context 与当前 noisy frame 的 tokens 拼接，只做帧内去噪。这里复用的是独立学得的条件表示，不是把旧 noisy hidden state 当作精确 cache；两模块需联合 next-frame 训练。低分辨率配方可给历史加噪以练习自产前缀，而高分辨率迁移又让 encoder 在训练时读取当前帧的高噪声版本、推理时读取纯 Gaussian，并用额外训练与 self-rollout 蒸馏适配，不能把 clean-history 的输入合同原样搬过去。<!-- source-family:SF-2026-ARXIV-2602-10095 -->

分离减少了随 denoising steps 重复的跨帧工作，却增加独立 encoder、固定 context、历史状态与训练成本，首帧费用也不能漏算。[SCD 的必要方法与对照](https://arxiv.org/html/2602.10095v1)在单 H100 80GB、batch1、832×480 的受测配置中支持这项职责取舍，但 1.6B 与 1.3B 基线参数不匹配，部分 semantic quality 较低，不授等质量普遍提速或线上 SLO。较深层仍有跨帧 attention，采样后段的表示相似性也下降，故固定 context 只是近似，不证明历史充分统计、原 joint 分布无损或真实 world state。decoder 深度、历史范围、训练适配和采样预算须共同验收；历史细节或质量不够、费用无法摊销时，保留完整 causal diffuser、更多跨帧计算或原采样路径，而不由 once-per-frame 把必要历史判断永久冻结。

当观测能明确写成线性等式时，还可在预测的 clean endpoint 上求最小修正，再与噪声重组继续采样。这里“最小”由正定 metric 决定：骨架图 Laplacian 加正 ridge 可让关节共同承担修正；相同线性误差为零，并不意味着 Euclidean 修正与拓扑耦合修正生成同样自然的运动。硬等式还需对应 $AR^{-1}A^\top$ 可逆或另有明确的合法解定义，不能对冗余、矛盾条件照搬普通逆。[受限 motion 对照](https://arxiv.org/html/2602.22742v1)支持这份 metric—质量取舍，但脚滑或文本一致性仍可落后；精确2D投影也不认证3D真值、非线性接触或全 posterior 正确。投影、求逆、重组和网络调用均付费，条件不满足或输出验收失败时，保留显式 conditioning、原 sampler 与独立约束校验，动作提交仍归第26章。<!-- source-family:SF-2026-ARXIV-2602-22742 -->

若希望最终样本满足显式 proxy 约束，初始 Gaussian 却通常不在该集合中，直接要求每步都留在最终集合并不合理。一条替代采样分支先用覆盖初始违例的 relaxation 扩大 barrier 集合，再随反向采样收缩到目标集合；每步把模型 drift 与已采样 noise increment 共同交给最小修正 QP。这里的状态是初始样本、relaxation schedule、barrier、采样网格和修正量，不是新的环境 observation。QP 还需在当前 active tube 上可行，只有目标边界梯度非零并不足够；有限步的一阶 Taylor 条件也留下非线性残差，不能直接当作连续 white-noise 路径或最终硬约束证书。<!-- source-family:SF-2026-ARXIV-2602-21429 -->

[受限收缩采样对照](https://arxiv.org/html/2602.21429v1)在 PushT 同100步设置减少了所定义的 action 平均变化违例，但约增加34%采样时间；平均相邻 velocity 变化不是物理 jerk、每步最大 rate 或真实执行安全。learned semantic barrier 可对不合格样本给高分，latent decoder 也未必把潜约束精确传到 pixel。Path-measure KL 与最终 marginal KL须分开，不能把前者的控制能量等式直接搬成后者或“最接近原分布”保证。Barrier 求值、梯度/QP与完整求解费用仍计入预算；不可行、残差/decoder失配或超时时，拒绝该候选或退回经过验收的普通 sampler，并重新检查最终输出。生成器只拥有 proposal，真实动作仍由第26章的 observation/controller 验收与提交，不能借经验零 proxy 违例越过这条边界。

冻结 prior 也不等于用它求带观测条件的 posterior 不再付 guidance 费用。常见 point-estimate guidance 需要经过 denoiser 的 VJP；一条已有的 VJP-free 分支以辅助随机状态解耦模型输入，近似把 denoiser Jacobian 换成 `(1/α)I`，等价于忽略 noise predictor 的 Jacobian，而不是原导数已精确等于该矩阵。给定潜空间的线性 Gaussian mask likelihood 时可利用 conjugacy 采样，但 nonlinear encoder/decoder 不会把 pixel mask 自动变成同一个线性合同。[当前理论与编辑对照](https://arxiv.org/html/2602.14157v1)进一步限定这项近似权限：细薄 mask 可以因 codec 压缩而泄漏，dilation 又会扩大需修改的区域，不能把背景重构误差称为被观察像素精确保留。solver、codec、guidance 与推理成本仍须分账，FLUX 编辑对照也有反侧；此分支不总优于 fine-tuned inpainting。观测合同、细节保真或净费用不足时，保留原 sampler、已校准的 guidance 或专用适配模型，不把冻结权重与免 VJP 升级成免成本、无损编辑。<!-- source-family:SF-2026-ARXIV-2602-14157 -->

Gaussian 噪声下，posterior mean 足以把平均残差换成 marginal score，这解释了平方去噪回归为何是合理接口；改变噪声分布后，这份充分性不自动保留。对可归一化、具有相应可微与可积条件的 elliptical noise，一条替代分支从 posterior 平均 noise log-gradient 求 score。若噪声由形状参数 β 与尺度矩阵 Σ 定义，求值残差的 energy 必须与它们匹配；β=2 的 Gaussian 情形退化为 mean residual，非 Gaussian 情形通常需要整个 posterior 的加权残差期望，而不是把原 MSE mean 直接代入。所谓 path derivative 在这里固定 posterior measure，只对残差函数的求值位置求导，不能连同生成 posterior 的路径一起微分。<!-- source-family:SF-2026-ARXIV-2512-23818 -->

这个接口让 noise law、posterior learner 和 score 求值分别接受核验，没有消除学习或采样成本。训练必须覆盖部署所用的噪声参数族；有限 posterior samples 引入 Monte Carlo 误差与额外调用，求解器仍有积分误差，零残差处不光滑的 energy 还需检查定义和可积条件。受限二维分布实验及其近似参考不证明任意模型质量更好，也不把非 Gaussian 更新升级为通用 reverse SDE。posterior 失配、样本预算不足或净收益未验收时，保留 Gaussian mean/MSE 接口与原有 sampler，而不由一个能量公式批准任意临时换噪声。

若 posterior mean 直接由经验数据逐点加权计算，读取支集又成为独立于求解步数的预算。高噪声时权重较分散，需要较广的 aggregation，但粗筛可更宽松；低噪声时权重可集中，aggregation 可以减少，却更怕漏掉真正近邻。一条受限分支仍先扫描全部数据的低维 proxy，随噪声下降扩大精确比较的候选池、缩小最终加权支集，分开召回精度与聚合数量。[必要方法与反侧](https://arxiv.org/html/2602.16498v1)的误差界针对真实 posterior logit 的 top-k 与有限数据半径，不证明 proxy 已召回该集合，也不把较宽上界变成高噪声必须全扫的下界。低维全数据扫描、样本驻留、近邻筛选与有限步求解仍付费，经验 exact score 在低噪声还可能记忆训练样本；相对 U-Net oracle 的局部 MSE 改善并非未知真 score 或生成泛化的保证。召回或近似质量不足时，保留更广支集与已验收神经 score，不照录与数据量解耦或逐 step 加速为端到端收益。<!-- source-family:SF-2026-ARXIV-2602-16498 -->

学习到的 denoiser 还要区分单步与整条采样轨迹的记忆：低噪声的一次去噪没有复现近邻训练样本，不排除轨迹已在较早区间取得并携带该样本的信息。[分噪声诊断与 denoiser-swap 控制](https://arxiv.org/html/2602.17846v1#S3)在有限图像模型中，把记忆集中到中间噪声区间；替换该区间与只换端点的效果不同，说明不能由端点行为或 train–test MSE gap 单独认证生成泛化。它不是所有模型共享一个危险噪声带，也不是近邻相似度自动构成隐私证明；理论的 Gaussian 几何与实际 learned denoiser须分账。减少特定区间训练是待验的质量–记忆取舍，需支付分尺度诊断、训练与完整轨迹采样成本，并绑定噪声路径、模型、近邻判据和数据人口；质量或记忆回归时保留原训练分布、完整 sampler 与独立样本审计，不以一处低 memorization score 放行整条生成路径。<!-- source-family:SF-2026-ARXIV-2602-17846 -->

固定生成器并不意味着 reference conditioning 可以原样注入。风格与主体特征可能共享方向，直接删除全部 subject subspace 会连同风格一起丢掉；一个替代分支先识别受 style 支持的方向，再从其余内容方向中提议衰减，将细、中、粗粒度 residual 分别送入对应生成尺度，并在汇总后约束总注入范数。这分开了“选择哪些证据”“送到哪里”和“注入多少”三项职责；subspace overlap 只调节衰减，不能被解释为风格与主体已经语义解耦，feature-change cap 也不证明 semantic leakage 为零。

校准集合、reference coverage、子空间估计和注入计算都付费；按主体不同 appearances 构造的集合与一次复用设置之间仍有适配边界，不能假设任意 reference 通用。冻结 SDXL/InstantStyle 的受限对照以 CLIP 差值等代理测泄漏，而非匿名化或安全保证；完全不注入的低泄漏可能同时丢掉风格，收紧 cap 也会损伤主体指标。局部 reference/prompt 与 disjoint stress tests 不替任意生成分布认证，完整运行成本、精度和 SLO 未披露。校准失配或内容/风格回归时，保留普通 prompt、原 adapter 或已验收的更保守过滤，而不由残差范数自签语义保真。 [必要机制与反证](https://arxiv.org/html/2609.21242v1)。<!-- source-family:SF-2026-ARXIV-2609-21242 -->

注入量之外，对象特征要送到哪里、风格又作用在哪个接口，也需要分开。一个冻结 diffusion 编辑分支先用 head-averaged cross-attention 为两个 prompt stream 分别选 source 与 destination positions，再把各 head 的输出拼成完整 feature vector，按特征/位置匹配将 blend 对象的信息送入 replacement 的 destination；这不是仅替换 attention weights，两个位置集合也不必互斥。另一条 self-attention 分支通过局部统计/残差调制与 style K/V substitution 改变外观；K/V 被替换时，先前调制主要经仍保留的 Query 与后续 hidden state 影响结果。对象位置迁移与风格调制因此是可分别校准的控制接口，不是内容与风格已被严格语义解耦。<!-- source-family:SF-2026-ARXIV-2601-08011 -->

这条路径增加多个 prompt stream、特征驻留与运输矩阵求解成本，不能由“无需训练”推出便宜。[TP-Blend 的 SD-XL 局部对照](https://arxiv.org/html/2601.08011v1)显示选择阈值、融合强度与残差配置会改变 coverage/替换/风格取舍；CLIP、LPIPS 与纹理指标不证明任意编辑语义正确或几何无损。原文运输约束与 Sinkhorn 更新的总质量不相容，Gaussian 宽度的频率解释也不一致，故这里只采用两接口的分工，不采用该 exact solver 配方、物理频带或结构保证。完整时延/内存与公平运行预算未披露；位置匹配、背景保真或成本回归时，保留普通 prompt、原 adapter、局部 mask/inpainting 与分别验收的编辑步骤。

对象遗漏也可以通过 key 的消费接口提出修正，而不只把已有 attention weights 放大。一条受限分支先按原 prompt 生成基线图，由视觉语言模型提出 present 与 missing 短语；将 missing 短语替换成占位符，与原 prompt 在同一表示坐标里取差，作为缺失条件的 key 更新 proposal。早段去噪再用基线 present 短语的平均 attention 作目标，在线调注入强度。图像与判定模型、两份 prompt、token 映射、投影位置、层与 step 都须绑定；contextual 表示差不一定只含一个概念，模型称 missing 也不等真实遗漏或目标位置。

[Delta-K 的有限对照](https://arxiv.org/html/2603.10210v1)支持这条条件消费分支，但改一个 key 也会经 Softmax 分母影响其他对象；固定单层 query 的局部假设不能签整条轨迹无干扰。原文投影前后位置、强度优化目标与若干配置未统一，不据此补造精确执行配方；注意力拟合仍需独立验收目标完成、既有对象和原画质。局部组成分数提高伴部分质量下降和生成变慢，完整基线生成、VLM 判定、表示与 map 驻留、在线优化都计费。遗漏判定、坐标或预算失配时，保留原 prompt、已验证的固定 guidance、区域条件与独立输出检查，不用更集中的 attention 批准语义保持。<!-- source-family:SF-2026-ARXIV-2603-10210 -->

Reference guidance 也不必重新运行一条 source reconstruction trajectory：可反序读取已缓存的 inversion states，在 target 采样早段逐步替换指定频带，再释放约束完成生成。需要适配长宽和分辨率时，各轴按长度归一的相对频率阈值，比固定二维坐标门槛更明确地声明控制范围；连续沿宽、沿高替换改变了控制算子，不是原二维 mask 的语义等价转换，也不保证频带恰好对应纯 style 或 content。<!-- source-family:SF-2026-ARXIV-2601-19115 -->

[FBSDiff++ 的有限 SD1.5 对照](https://arxiv.org/pdf/2601.19115v1)支持取消 reconstruction 后减少 inversion 预算的局部分支；只测有限尺寸与 proxy 质量，保留强度又与 text fidelity 交换。缓存、DCT、inversion/target 步数、图像 decoder 与预处理都计成本，表中 50 vs 1000 步的总时间不成为通用 8.9 倍或 SLO。局部 latent mask 不能自签原像素严格不变，尺寸/编辑/保真未通过时，保留高精度 inversion、source reconstruction、显式 inpainting 与原频率控制，并独立验收未编辑区域和目标完成。

逐帧干净reference还可能与编辑区域本身冲突：完整上下文帮助保持身份与背景，却也向生成器提供了需要改掉的旧唇形。受限视觉配音编辑分支据此把结构、唇形与纹理目标分配给经过校准的噪声区间，并只在对应区间激活所训练的adapter；它不是统一训练后任意切换时刻，也不是所有多模态任务都服从同一三阶段律。作者四设置对照中，完整条件editor对统一目标不稳定，而inpainting没有相同交互，说明成立条件包含reference可见性与编辑任务。区间搜索、合成paired数据、分阶段训练和部署adapter均付费；conditioning或noise schedule改变时应重验，编辑/保真冲突未解决则保留局部mask/inpainting或原编辑路径，而不把更多上下文自动视为更强监督。<!-- source-family:SF-2026-ARXIV-2512-25066 -->

视觉配音也可以保留预训练生成器，而把编辑状态与随机性分别管理。一条受限 flow 编辑分支同时维护 source 与 target 的带噪轨迹，以两种条件下的 velocity 差和 source 状态增量更新 target，再用模型估计的扰动延续 source，而非每步独立重抽噪声。它改变耦合轨迹的组织，不由变量重写认证 target 分布无偏，也不把取消逐步随机抽样变成整个过程确定。[有限唇同步对照](https://arxiv.org/html/2603.09084v1)中，身份与部分画质改善仍伴同步或风格化成功率反退，联合音画编辑只有定性支持且会产生音频伪影。双条件求值、初始扰动、codec 与校准均付费；源条件、同步或背景保真失配时，保留独立随机路径、原 FlowEdit、训练式 adapter 与显式区域编辑，不从 training-free 推出免费或背景无损。<!-- source-family:SF-2026-ARXIV-2603-09084 -->

参考图的旧内容与编辑目标冲突时，还可先分开保留关系和新关系的条件身份。设原 scene graph 为 `G`、编辑后为 `G'`：只把交集 `G∩G'` 转成 source prompt，用于 inversion 与后续 guidance；target prompt 则组合新关系 `G'\G` 与该交集，不把需要删除的旧关系重新送入 source。[VENUS 的受限 source 消融](https://arxiv.org/html/2601.07219v1#S4)支持这项条件接口，交集只表示 parser 给出的稳定语义关系，不是像素 mask、完整背景或保真保证；另用 ground-truth target prompt 的文字编辑模式不能混成同一 graph-diff 实验。局部保真改善伴随 EditVal accuracy 低于所列 SGEdit，其他 backbone 的 PSNR/LPIPS 也有退步，不能用 CLIP 或 fidelity 代替编辑完成。scene parsing、关系转文字、77-token 截断、inversion 与 CFG 均有费用，所印每图时间不授普遍速度；parser/关系缺失或编辑与保真冲突时，应回到普通 prompt、局部 mask/inpainting 和独立编辑验收。<!-- source-family:SF-2026-ARXIV-2601-07219 -->

生成时的 semantic distinction 何时可读，还可以按所问区别单独诊断，而不是用一个全局 entropy 代表所有内容。一条受限分支为非穷尽语义类别构造二分对比，累积 conditional 与 reference 的重构差形成 likelihood-ratio，再跟踪相应 posterior entropy 随 noise 的变化。不同 distinction 因此可以得到不同观察时窗；这是一份特定分区与模型条件下的测量接口，不自动授权该时刻 commit 或说明最终语义正确。 [必要定义与边界](https://arxiv.org/html/2602.09651v1)。<!-- source-family:SF-2026-ARXIV-2602-09651 -->

reference 被近似成 complement、二分先验固定为0.5，都不等真实类别人口；guidance 改变期望分布后读数还可成为 cross-entropy，而非原 posterior entropy。prompt 变换可能同时改变多个属性，model 条件误校准也会错移时窗；额外两支求值、区间/scale 搜索与质量选择均付费，有限图像曲线不授统一 phase transition 或免费 gate。分区、近似或质量失配时，保留原 schedule、固定 guidance 与独立语义验收，不让诊断曲线接管采样接受权。<!-- source-family:SF-2026-ARXIV-2602-09651 -->

### Flow Matching：先指定概率路径，再学习移动方向

另一种构造直接规定噪声到数据的概率路径，并回归沿路径移动的 velocity。为避免与上面的 DDPM 时间方向混淆，这里使用 s：s=0 是噪声，s=1 接近数据。取独立噪声 epsilon、干净目标 y 和小的正数 sigma_min，一条易采样的条件路径是：

```text
a_s = 1 - (1-sigma_min) s
X_s = a_s epsilon + s y
u_target = dX_s/ds = y - (1-sigma_min) epsilon
L_CFM = E ||v_theta(X_s,s,c) - u_target||^2
```

sigma_min>0 时终点仍含少量噪声；趋近零才得到常见的噪声—数据直线插值极限。训练知道 y 和 epsilon，所以目标可计算；部署只见当前 x、s 和条件 c。平方回归在给定当前状态后学习条件目标的平均速度，在论文的密度与正则条件下，这与匹配边际概率路径的目标有相同参数梯度，而不是要求模型复原每个训练配对。

生成时从噪声开始积分 `dx/ds = v_theta(x,s,c)`；最简单的 Euler 更新是 `x_(s+ds) ≈ x_s + ds * v_theta(x_s,s,c)`。训练配对走直线，不代表平均后的速度场沿每条生成轨迹也笔直，更不保证一步积分准确。Flow Matching 是训练目标与路径构造，ODE solver 是数值执行方式，两者不是同一个组件。

少样本图像微调还可以联合改变数据视图与一次更新的组成：从同一原图裁出整体、部件与细节，保留 root 和粒度标签，在 aspect-ratio buckets 之间累积同 root 各视图的梯度，再统一做 optimizer step。粒度标签还可决定训练 time 分布或 loss 权重；两者是不同接口，与更新中的 group 大小和归一化共同定义 effective objective，不是自动保持原目标的无偏采样。这把语义相关视图放在同一次更新中，而不是给原 MSE 凭空增加 pairwise penalty。<!-- source-family:SF-2026-ARXIV-2603-10785 -->

这条分支以检测、裁剪/超分、数据 provenance 与分组调度换更集中且可协调的监督；多个 crop 仍来自同一图，不能算独立新数据，错误 part–whole 或伪细节也会被共同强化。残差 Gram 与 Jacobian 链式恒等式不保证未知 NTK 下的梯度冲突减少，需另测梯度与独立质量/旧能力回归。[有限 FLUX/SDXL 对照](https://arxiv.org/html/2603.10785v1)中的相对人审/judge 排名支持启发式探索，不认证普遍优化稳定；预算使用估计训练时长与附近 checkpoint，另有预处理费用，不能把较短 checkpoint 优势直接称精确端到端节省。分组归一化、语义视图或质量/费用失配时，保留原完整图、标准 bucketing 与已验收的 time/weight 方案；原 Flow Matching 目标和 solver 责任仍分别验收。

“数据的有效维数较低”也不能单独签发有限步 sampler 的保证。一条受限 rectified-flow 分析用 bounded support 与 covering number 描述 intrinsic complexity，但 deterministic Euler 还依赖所学 velocity 的均方误差、Jacobian/trace 等高阶近似条件以及两端加密的 U-shaped 网格；随机路径变换可以不要求这组高阶导数，仍须控制 velocity 误差。几何复杂度、估计误差和数值执行因此是不同责任，不能从前者推出有限训练网络自动满足后两者。<!-- source-family:SF-2026-ARXIV-2601-15500 -->

[必要假设与终点限制](https://arxiv.org/html/2601.15500v1#S4)的 TV 比较只到倒数第二个、仍含 Gaussian 扰动的 endpoint：精确低维目标与全维近似支集不同，终点 TV 可为1，不能写成精确流形收敛。网格截断、学习误差、导数验收与额外随机求值都付费；learned drift 在高维/端点处仍可退化，stochastic 不天然优胜。初版高阶误差条件符号及非零均值 Gaussian 示例尚有未决冲突，不采用完整定理常数或据此归因实测速度；条件、质量或净预算未确认时，保留原 velocity/score 训练、已验收 Euler/Heun 和单独的终点质量评价。

目标若只支持在低维 manifold 上，density 必须相对该支持的 volume 定义，不能直接套 ambient Lebesgue density。[一个受限定理](https://arxiv.org/html/2602.22486v1)在 compact、无边界、正 reach、足够光滑且 intrinsic dimension `d≥3` 的 manifold、正下界 Hölder density 与特定 velocity-Jacobian 条件下，把 W2 误差分为支持恢复、density 估计和采样统计项；相应指数由 `d` 控制，不等计算与常数不依 ambient `D`。结论还使用设计的分段网络类、exact empirical minimizer、时间网格及 early stop；支持项可以比 minimax 更慢，不能把 density-dominant 条件下的 near-optimal 说成所有数据和 sampler 的保证。实际训练误差、几何常数、端点截断及有限步 solver 仍需分别计费和验收，数值中 `d=2` 的例子不在该定理范围，RK45/Euler 图也不是等 NFE 或墙钟加速证明。条件或净预算不成立时保留原 score/velocity 训练与已验收 solver，不由低维统计指数签发实用训练收敛或免费采样。<!-- source-family:SF-2026-ARXIV-2602-22486 -->

若生成目标只要求有限统计量，完整 marginal score/velocity 也不是唯一接口。一条 moment-guided 分支保存插值路径的 `m_t=E[φ(I_t)]`，通过 `G_t=E[∇φ∇φᵀ]` 的线性系统分别求 moment transport 与噪声补偿，构成 SDE drift；在初始 moments 匹配且耦合解存在时，它保持这些 moments，不复原插值的完整分布。目标是所选 φ 约束下的最大熵 p*，不是任意真实 pdata；Gram 奇异、有限粒子与积分误差仍需处理。[MGD 的必要机制与数值反侧](https://arxiv.org/html/2602.17211v1)把一般 σ→∞ 的最大熵速率明确列为 conjecture，不能由 moment 保持授有限噪声精确采样。同一 bimodal 分布只换 φ，就可从较小噪声改为约100倍积分成本才接近目标；统计量表达能力、粒子/Gram估计、求解与噪声预算共同付费，也不能把 moment-compression 当生成语义保真。目标需全分布、Gram不稳或净成本不合算时，保留 learned score/velocity 与原 sampler，区分建模误差和采样误差。<!-- source-family:SF-2026-ARXIV-2602-17211 -->

直接学习可逆映射是另一种分工：把输入映为观测分量和latent分量，用监督误差约束观测，再以critic匹配观测与latent的联合分布，最后用inverse产生给定观测下的候选样本。它把条件分布误差移到模型类、critic和训练泛化，而不是交给数值solver；逆可计算也不等于posterior已校准。有限critic给出的variational值通常只是所选模型类能看见的差异，拟合值低仍可能漏掉critic无法表达的分布差。<!-- source-family:SF-2026-ARXIV-2602-20480 -->

[受限定理](https://arxiv.org/html/2602.20480v1)以realizability、整个映射T及其inverse的统一双Lipschitz约束、uniformgeneralization、有限高阶矩及逐渐消失的critic近似gap，把训练误差连到正概率观测集合上的Wasserstein误差；有限矩放宽bounded-support，不删除其余条件，也不签每个观测点的真posterior。更强critic增加采样、容量与saddle优化费用，重尾/稀有观测还改变误差常数；应分别检查critic表达、表示信息、实际条件质量和总成本。条件或净预算无法确认时，保留已校准density/score模型与原sampler、缩小采用域或交给独立条件验证，不让训练loss自己取得分布真实性权限。

端点也可以从无结构 Gaussian 改成外部表示附近的分布，而不只把表示当额外 conditioning。一个受限图像编辑分支用固定视觉 encoder 的 patch features 经 PCA 形成几何代理 `y`，以 `N(y,b²I)` 为共享端点，各域独立训练本域 VAE latent 到自身表示端点的 bridge；源图直接编码或经 source bridge 反演后，target bridge 从该端点反向生成。原分支以 t=0 表示数据、t=T 表示表示端点，不能套用上面的 s 方向。独立域训练不需跨域成对样本，但给定共享 y 后的条件独立及跨域对齐仍是建模假设，实际 encoder 不是 oracle；b=0 也不提供 fidelity 证书。[自然图像必要对照](https://arxiv.org/html/2602.16664v1#S5.SS3)还包括 SiT 全模型或 SD3-M attention 再训练与新增 projection，不是免费 zero-shot。较强几何 prior 适合外观/风格变化，却会抑制大形变，放松它又可能扭曲背景；sketch、silhouette 等表征鸿沟也会失效。encoder/PCA、域模型、端点方差、projection 与 sampler 必须共同版本化，训练、反演和 vector-field control 全部计费；H200 batch1 的跨配置平均墙钟不是 tail SLO，CLIP/DINO 与亮度结构代理不是语义真值。prior 或净收益不成立时，原 Gaussian 路径、已验收反演、显式 mask/inpainting 仍合理，不由局部结构保持授全域真实像素或临床保证。<!-- source-family:SF-2026-ARXIV-2602-16664 -->

Solver 的阶数也可以按当前路径状态选择，而不是所有时刻固定 Heun：一条受限分支缓存相邻 velocity，以 relative-curvature/secant 代理提议 Euler 或多一次求值的 Heun，并离线搜索时间分配。严格局部 Wasserstein 界要求真实轨迹导数在区间上的 population supremum；有限差分与旧 cache 并不提供这个上界，因而这里只让它们提出工作量分配，不签 runtime 误差证书。[必要 solver 对照](https://arxiv.org/html/2602.12624v1)还有固定 Heun 的部分质量反退，部分比较同时改了 stochastic churn，不能把收益全部归给时间分配。校准、搜索、额外求值和 cache 维护都付费，NFE 不等 wall-time；实际步长方向、质量或成本不合适时，保留固定 Euler/Heun、原 noise 配置与已验收时间网格。<!-- source-family:SF-2026-ARXIV-2602-12624 -->

调整 solver 阶数之外，也可以先学习数值时间怎样分配。一个受限分支以局部 Euler 误差代理和到达终点的约束训练可依赖状态的 clock，先按时间取训练轨迹 clock 的经验均值，固化成非均匀网格，再将其增量和归一到总 horizon。训练控制器与部署 sampler 因而是两个 artifact：线上只复用网格，不继续运行 actor 或误差代理；增量和恰好等于 horizon 只保证数值端点命中，不保证生成样本正确。网格必须绑定 score/velocity model、solver、原时间方向和训练人口，不能把“自适应训练”写成每个请求都在自适应采样。<!-- source-family:SF-2026-ARXIV-2601-18681 -->

固化省去逐步 controller 调用，却支付额外 actor/critic、轨迹、JVP 和时间导数训练，并丢弃状态依赖；何时平均网格足以替代状态控制，仍需目标 workload 验收。[有限 EDM 对照](https://arxiv.org/html/2601.18681v1)仅固定 score、solver 等条件比较时间网格，低/中 NFE 有收益而高 NFE 可与原 EDM 打平，不授任意质量指标最优、训练收敛或 production latency。局部误差目标、FID、实际 NFE 与总训练/推理费用应分开测，端点归一不使负向时间或域漂移自动安全。迁移质量下降、状态差异重要或校准成本不合算时，保留原 EDM 网格、固定 Euler/Heun 或逐状态控制，而非由一条离线平均曲线签发通用采样保证。

历史函数求值还可以构成多步 forecast，而不只作为旧 feature 直接复用：一条受限分支用 Adams–Bashforth 历史预测推进轨迹，在真实 model evaluation 时用 Adams–Moulton correction 与 relative feature drift 提议以后跳过多少次求值。[原版本的控制流与对照](https://arxiv.org/html/2602.18093v1#S3)中，J=0才刷新函数值并测 drift，J>0只按历史预测推进、倒数 horizon，不提供每个跳步的实时误差监测；history 启动与前一函数值的 guard 未充分披露，不能据伪码补成完整 cookbook。收益要求局部轨迹足够可预测，强变化、长跳步或阈值失配会损质量；历史驻留、真实刷新、correction与校准均计费，NFE节省不自动等于端到端速度。阈值与质量目标须绑定模型、solver、时间网格和CFG，质量/成本不合适时保留全求值多步 solver、Euler/Heun与更短 horizon，不让 drift proxy 取得生成正确性证书。<!-- source-family:SF-2026-ARXIV-2602-18093 -->

端点配对还会改变“当前状态对应哪个干净端点”的解释。独立配对通常让回归学条件平均；对平方代价的 population OT coupling，若其势函数 `φ` 为 proper、lower-semicontinuous convex，且路径系数 `α_t, β_t` 为正，插值的逆可写成 `x_1 = prox_((α_t/β_t)φ)(x_t/β_t)`，从而用该端点表达速度。[必要 prox 分析](https://arxiv.org/html/2602.12683v1)把 coupling 和路径几何联系起来，即使目标人口位于低维支集也不要求势函数处处可微；但有限 minibatch OT 与近似网络不是该 population 对象，不能继承其唯一端点或未核终端收敛证书。构造 OT、训练势/速度与数值积分都需预算，toy、TwoMoons 和 MNIST 的局部验证不授权 foundation 模型质量保证；配对或支持域失配时，保留独立配对、原 conditional-mean 训练和已验收 solver，而非用 prox 名称宣称任意生成轨迹已上流形。 <!-- source-family:SF-2026-ARXIV-2602-12683 -->

端点也不必总按独立 noise/data 配对。一条受限桥匹配分支先从数据出发，以能计算 energy 的 prior 为终点，训练有记忆的 forward coupling；其中仍交替做沿路径匹配与 terminal conditional matching，并非一次训练消除所有交替。随后冻结 forward，从它产生的端点配对监督 backward bridge。真正最优 coupling 才授予相应 reciprocal-process 的精确条件，有限网络学得的近似 coupling 与低 FID 不能证明全局 Schrödinger bridge 最优。<!-- source-family:SF-2026-ARXIV-2602-15396 -->

这把配对构造变成额外训练和采样预算：prior energy 的系数过小可能留下低密度覆盖缺口，过大又增加曲率与有限步求解压力。[ASBM 的必要对照](https://arxiv.org/html/2602.15396v1#S3)在 CIFAR10/FFHQ 的特定 UNet 和 solver 下支持这条分支，但 backward 的600 epochs还要加 forward coupling，合计约2100而非零前处理；20/50次 forward 求值也需分账。少步蒸馏的部分 precision 低于基线，不能由 FID 或 recall 改善推出全质量支配。能量、覆盖或构造成本不合适时，独立端点、普通 score/flow matching 与已验收多步 solver 仍合理。

网络的输出参数化还不必与训练 loss 所在空间相同。多步求解或先压成 latent，在容量与质量预算成立时仍合理；若直接生成像素使每个 patch 的观测维度很高，有限网络拟合 image-like 输出与拟合混合噪声的 velocity，可能遇到不同的表示压力。一个少步分支让网络直接输出 image-like field，再按指定路径与时间关系转换成区间平均 velocity，以其 JVP 构造 MeanFlow 的 velocity-space 监督。这里改变的是预测接口，不是把 velocity loss 换成图像重构 loss，也不是直接保证一步更新准确。[受限像素对照](https://arxiv.org/html/2601.22158v1)在相同 backbone、固定 token 数、优化器和训练 epoch 下，高 patch 维度的两种输出明显分化，低 patch 维度却几乎没有差异；这一条件性结果不证明 velocity prediction 普遍失败。<!-- source-family:SF-2026-ARXIV-2601-22158 -->

这条接口的时间方向须单独记录：原分支用 t=1 表示噪声、t=0 表示数据，不能直接套用上面的 s。对于一般的 0<r<t 区间，所输出 field 不保证已经位于数据 manifold；边界关系与局部实验只是设计依据，不是全区间流形定理。转换、JVP、时间对采样与可选感知 encoder 都付费，感知 loss、优化器和 guidance 的收益也不能全部归给输出参数化，1 NFE 更不等端到端成本。容量、patch 维度、时间采样或独立质量验收失配时，保留 latent 表示、原 velocity head 与经过验收的多步求解，而不由单步可行性宣布它们过时。<!-- source-family:SF-2026-ARXIV-2601-22158 -->

当连续 representation 接近定范数时，概率路径还可以选择在球面上移动，而不只给欧氏直线的端点归一化：将 data/noise 端点单位化，以 SLERP 定义训练路径，把预测 velocity 投影到当前位置切空间，再用 exponential-map 更新并重新归一。路径、切向预测与数值更新必须一起匹配，不能只改 loss 名称或只归一终点。 [受限表示生成对照](https://arxiv.org/html/2602.10099v1)中，同小模型路径比较支持这一接口分支，但近恒范数与局部改善不证明全部语义只在角度、容量不足不存在或几何是唯一根因。<!-- source-family:SF-2026-ARXIV-2602-10099 -->

球面采样还须与 decoder 的半径分开验收：单位方向可以相同，送入 decoder 的幅度不同仍会改变质量，不能把 norm 从交付合同删除。原文单 sinc 权重并未闭合所有切向扰动的误差等价，训练与 Algorithm 2 的时钟也有歧义，因此不照录其完整 solver 配方或收敛保证。受限 recall、容量与半径反侧以及投影、归一和积分成本保留；支持域、decoder 幅度或质量不合算时，欧氏 Flow、单独校准归一接口与已验收多步 solver 继续成立。<!-- source-family:SF-2026-ARXIV-2602-10099 -->

因此 DDPM 的 noise prediction 与 Flow Matching 的 velocity prediction 不能脱离时间方向、路径和输出参数化互换。二者都把训练回归变成可执行的生成更新，也都留下初始化、近似误差和求值预算。NFE 统计网络求值而不是输出 token；guidance 分支、多阶段 solver、分辨率和 decoder 还会改变一次求值的真实成本。旧的多步采样在质量与预算已验收时仍是基线，少步路线必须说明自己减少了哪一类误差、又接受了什么近似。

当高分辨率生成已有 coarse layout，少步 refinement 又要求大的局部更新时，不一定要先把该布局完整反演回 Gaussian noise；可在像素插值、VAE 重编码后，对重叠 patch 只做浅 DDIM 反演，再用 few-step 模型补细节，并分别治理 seam blend 和注入噪声。[PixelRush 的受限对照](https://arxiv.org/html/2602.12769v1)支持这一 spatial/cascade 分支，但浅反演本身有 IS 微退，直接换成一步模型又损质量；组件表是累计消融，不是全 factorial 因果，噪声在原多步路径上还会反退，不能照搬统一 blend/noise 系数。它生成新细节，不保证恢复真实高分辨率像素；base generation、VAE、反演、patch overlap 与多级 cascade 都计入完整预算，one-step 不代表全流程一次求值。结构、接缝或质量失败时，保留更深反演、多步 refinement、原噪声和低分辨率路径，而非由较低 NFE 宣告这些旧方案过时。 <!-- source-family:SF-2026-ARXIV-2602-12769 -->

NFE 预算还会改变条件采样的统计对象：终点重要性权重在高维退化时，可在中间时窗把确定性 Flow 改成保持理想边际的随机路径，用 look-ahead likelihood 提议粒子、重采样，再在终点以真实 likelihood 与 look-ahead 的比率修正；这与上段补空间细节不同，处理的是采样人口与权重，不是像素恢复。[TFTF 的条件推导](https://arxiv.org/html/2602.12932v1)依赖理想目标、精确转移、有限有界权重及粒子数趋于无穷；learned field、Euler–Maruyama 近似和有限粒子不取得同一精确分布证书。增大 proposal variance 或省略 velocity Jacobian 后，必须按实际 proposal 重算权重，不能把中间平滑 likelihood 偷换为终点目标。受限对照在条件准确率与图像质量上各有反退，粒子驻留、网络求值、likelihood 梯度与重采样均计费；权重退化、目标不可核或费用超过收益时，保留确定性采样、普通重要性采样与原 guidance 路径。 <!-- source-family:SF-2026-ARXIV-2602-12932 -->

多个输出之间需要统计协调，也不必都加入跨输出 attention。一个受限多 stem 分支让每个 stem 保持独立 compute graph，却把同一 mix 的随机 stem subset 组成训练 group，共享 group 内初始高维噪声；推理按同样接口共享噪声，并可选择以先生成部分 submix 再条件生成其余部分的两遍路径。它耦合的是训练/采样人口与初始化，不是让一条 graph 读取另一条的状态，也不是推理时临时设相同 seed 就等于经过这种联合训练。 [必要机制与消融](https://arxiv.org/html/2602.09891v1)。<!-- source-family:SF-2026-ARXIV-2602-09891 -->

共享 noise 不认证独立 stem 的语义或同步正确：仅推理共享的对照可退步，one-pass 质量也可落后逐 stem 的 K-pass，two-pass 是条件质量与成本分支而非免费最优。由 silence 阈值构成的活动二值条件只标记活动人口，训练该通道还可能使 FAD/CLAP 退步，不能从高活动 F1 推出音乐正确性。训练 group、噪声、submix 条件与完整求值/decoder 费用需共同记录；噪声协议失配、质量或活动控制退步时，保留独立噪声、原逐 stem 路径或经过验收的两遍条件方案，不由省跨 stem attention 外推任意输出集合的可控性。<!-- source-family:SF-2026-ARXIV-2602-09891 -->

guidance 的两次求值也不必来自去掉 conditioning 的两支。[Sparse Guidance](https://arxiv.org/html/2601.01608v1)保持同一参数 θ、时刻和条件 c，只以不同 token sparsity γ 构成强、弱 capacity branch，再用 `ω D_strong(c)+(1−ω)D_weak(c)` 外推；它不是低成本 unconditional CFG，去条件的组合另有定义。两支各自 forward、随机 subset 以及 routing 暂绕后回填或 masking 的不同状态损失都要计费，ω 与两支 γ 需联合校准，并保留训练 sparsity 设置的兼容性。局部 attention 省算不能直接当作端到端吞吐收益：decoder、路由、质量与多样性可能改变净成本，受限图像/T2I 对照不授任意模型普效。分支失配或质量/多样性退步时，回退已验收的 dense sampling 或 CFG；这是一条以 capacity gap 提供信号的替代分支，不静默覆盖原条件差分的机制。<!-- source-family:SF-2026-ARXIV-2601-01608 -->

负分支还可以保留正条件的部分共享上下文，而不完全清空条件或削弱主干 capacity。一个受限分支将编码后的文本位置分为 content 与 context-aggregating 两组，先把 content 状态替换为匹配的空条件分支状态，再随退化预算替换聚合组；正支减去这份部分退化负支，仍采用原两支外推形式。默认替换全部 content、保留聚合组时无须组内排名；其他预算才在指定 denoiser 层提取 attention 排序，并可复用首步排名。它改变的是条件差分的参照对象，不是删除 sequence 位置，也不是对所有模型重新训练 unconditional 分支。<!-- source-family:SF-2026-ARXIV-2603-10780 -->

这种分组只在受测 tokenizer、聚合状态与模型接口下成立：[有限分组对照](https://arxiv.org/html/2603.10780v1)对 COCO 预测做 SVD 得到的近正交子空间是诊断代理，不是已知真实 manifold 或全轨迹无干扰证明。分组消融支持局部配置，组内 PageRank 却非必要；图像质量仍有反退，CLIP/VQA 不授语义真值。两支求值、空条件状态与 hooks、排名或缓存，以及 block/scale 校准继续计费，非默认预算的局部计时不签所有模型 SLO。条件布局或排名漂移、质量和完整费用不合算时，保留原 CFG、dense/capacity reference 与独立生成验收，不让部分上下文保留自签语义无损。<!-- source-family:SF-2026-ARXIV-2603-10780 -->

guidance reference也可以来自同一采样轨迹的历史，而非再计算去条件或低capacity网络。一条连续Flow分支保存与latent同形的velocity EMA，当前步用 `v + α(v−m)` 外推，随后为下一步更新历史；初始化、时间网格、衰减和update顺序都属于sampler state。它复用已算velocity而不新增网络求值，但有CFG时仍支付原两支求值，EMA驻留与向量算术也需计费；历史reference不是精确unconditional或独立弱模型。<!-- source-family:SF-2026-ARXIV-2602-20360 -->

[有限Euler采样对照](https://arxiv.org/html/2602.20360v1#S4)支持该历史分支的局部质量收益，却额外搜索了强度、衰减与guidance时窗；过强外推或与强CFG叠加会退步。低NFE、较好FID和不增加network evaluation须分别验收，不授分布保持、wall-clock减半或所有生成任务的收益。配置与轨迹变更、质量或多样性未通过时，减弱或关闭历史外推，回退原Euler/已校准CFG与capacity分支，而不让陈旧EMA自动接管新的采样协议。

reference 还可以是一组目标样本，而非单个条件或轨迹历史。只希望提高某类输出概率时，分类器/CFG guidance 仍是直接分支；需要拟合有限参考人口的模式与比例时，可以在 reverse sampling 中加入 empirical MMD 梯度：生成 batch 内的排斥项维持分散，reference attraction 项推动分布匹配，prompt×latent product kernel 再让相关文本条件加权参考样本。这里 reference 编码、kernel/带宽、batch 和 guidance schedule 都成为 sampler state，batch 内 coupling 也不等于独立单样本条件更新。[受限方法与图像对照](https://arxiv.org/html/2601.08379v1)支持这条替代接口，但 iid reference 与有界平滑条件下的 cross-term 集中界只约束梯度估计，不证明有限求解器或 decoder 输出已服从目标 law。参考稀疏、kernel 失配与高维估计仍可能退步；reference 编码/驻留和成对 kernel work 增加费用，training-free 不等于免费。质量、覆盖或净预算不可信时，应增加已验收参考、重校准，或回退原 guidance/专用适配，不让 distribution matching 名称接管最终语义验收。<!-- source-family:SF-2026-ARXIV-2601-08379 -->

增加 guidance 条件也不等于约束更强。单一明确类别时，固定安全 reference 便宜且可解释；多个有害类别的 noise 差分方向在同一 latent 和 timestep 上可能对立，简单组合会稀释本应压低的类别。一条受限分支每步分别求各 keyword 条件的 guidance，与当前 prompt 的差分比较 cosine，只把最相符的一类交给原安全 steering；它改变 reference 选择而不重新训练 denoiser。文本投影另有选择接口：比较各有害子空间的 projection residual，再只采用所选子空间，不能与 latent 时间动态选择当作同一实现。

Cosine 或小 residual 是所给 keyword/模型下的对齐代理，不是真实有害语义，也不保证混合多类风险同时消除。[CASG v1 的受限 SD1.5 对照](https://arxiv.org/html/2602.20880v1)支持固定/错类/平均 reference 的局部失效边界，但 harmful 率依赖 Q16/NudeNet，SAFREE 分支 FID 仍退步；需要独立内容与正常效用验收，不能由 sampler 自签发布安全。各类别求值仍付费：50 step、单 H100 的七类 latent 分支约 2.58 倍原 SLD 时长，text projection 增费不同。类别失配、过度内容改变或预算超限时保留已验收的固定 reference、较保守采样与外部过滤/人工审查；training-free 不取消模型求值或平台的安全裁定权。<!-- source-family:SF-2026-ARXIV-2602-20880 -->

单一 keyword reference 也可以换成从有限图像人口构造的多原型条件：对含目标概念与 near-miss prompt 的图像 embedding 作差并聚类，再只优化 soft prompt，使冻结文本 encoder 的全局表示接近各图像 centroid；采样时按当前 prompt 提议选中的 prototype，把它作为额外 negative CFG 条件。这改变的是条件库的制备和使用，不是删除 denoiser 权重或训练数据影响；配对种子、全部成对差分与聚类仍可能混入内容和随机性，global embedding 接近也不认证完整 token 条件等价或唯一概念方向。[原型负引导的受限对照](https://arxiv.org/html/2603.08271v1)中，正文 threshold 与算法无检查的选择口径未闭合，不能据此补通用无命中 recipe；有限 detector flag、攻击和保留质量指标也不授全部概念或合法请求的安全与无损。Base weights 冻结仍支付成对图像生成、编码/聚类、soft-prompt 优化、条件检索及额外 denoiser 求值，prototype bank、prompt/near-miss、encoder、阈值和 scale 都须随 sampler 保存。覆盖或条件漂移、合法效用下降与预算失配时，保留原 negative prompt、较保守 guidance 与独立内容过滤/拒生成；外置 policy 和真实输出验收拥有发布权，不让 prototype cosine 自签安全。<!-- source-family:SF-2026-ARXIV-2603-08271 -->

条件也不必由 prompt 一次编码后始终固定。复杂指令可先在固定 prompt/image prefix 上递归更新连续 hidden state：把前一步状态直接作为下一次模型输入，而不先生成离散中间文本；联合训练条件 encoder 与 DiT，并用分步图像目标和只作用于末态的文本参照，使推理状态成为可学习的条件接口。这里推理轮次 `τ` 与 denoising time `t` 是两条不同轴：训练可监督各推理轮次对应的完整生成轨迹，部署则先更新 latent 条件，再解码末态，不是让每个去噪步都重新生成一幅中间图。末态与参考 hidden state 接近，也不证明逻辑成立或得到了外部事实。<!-- source-family:SF-2026-ARXIV-2603-12252 -->

[受限联合训练](https://arxiv.org/html/2603.12252v1#S4)先监督中间和末态，再缩短第二阶段、只对末态传播训练信号；参数仍会更新，不能把中间 no-grad 误写成旧推理链被永久冻结。过多末态训练会损伤中间轨迹，给每一步加语义监督也可能退步；合成任务的专训均值不等统一模型或通用视觉推理能力，部分统一任务仍落后对照。分步标签、teacher/人工构造、联合适配、额外 latent 求值与最终完整 denoising 都有成本，应分别验收质量、独立约束正确性与总预算。标签、latent 深度或行为回归不稳时，保留静态条件、显式计划/已验收指导和外部任务验证，不让流畅图像或不可见的“思考”自行取得发布权。

guidance 还应区分条件进入网络的接口。序列文本经 attention 提供局部语义，pooled text 也可经 MLP 生成各层 modulation；改变后者不是在最终 velocity/noise 输出上做 CFG。[一个受限全局条件分支](https://arxiv.org/html/2602.09268v1)保持原 prompt 的序列路径，在 modulation 上加入 `w[y(p+,t)−y(p−,t)]` 正负方向；其 dynamic 选择按 layer 而非 timestep 改变。已有 pooled 路径可直接消费该差分，但 CLIP-free 模型需要另行训练适配接口，不能把二者都称为 training-free。<!-- source-family:SF-2026-ARXIV-2602-09268 -->

全局 modulation 不保证语义解耦：较大 scale 会压过原 prompt，受测模型也有 pooled 路径 inactive 的情况。局部审美或复杂度改善伴随 relevance、defect 或视频 smoothness 退步，文本到图像 correspondence 仍未解决；新增适配数据、MLP 训练与求值成本需单列。因而先验证具体模型的条件路径、layer/scale 与质量维度，接口无效或要求精确对应时保留已验收的 attention 条件、CFG 与更保守 scale，不从偏好结果批准任意生成任务。<!-- source-family:SF-2026-ARXIV-2602-09268 -->

检查 pooled 条件时，还须先分开语义 `y` 与共同 timestep `t`：对 `c=y+t` 测得高 cosine 或低 participation ratio，可能只是共同时间分量遮住差异，不证明 class embedding 都相同，更不度量真实信息维数。一个受限对照中 combined REPA 条件 cosine 接近 1，单独 `y` 却明显较低；是否可删坐标应由具体 mask、timestep、消费者和实际生成质量另验。约 39% tail 剪枝仍有部分质量小退，约 66% 的 FID/IS 已显著退步，不能称普遍无损；tiny signal 也可能被 downstream 使用。稀疏向量不自动减少 dense 主干墙钟，诊断、mask 校准与 runtime 核费；语义/质量或执行预算未通过时保留完整条件与低剪枝路径。<!-- source-family:SF-2026-ARXIV-2602-21596 -->

对同一 prompt 联合生成多个视频时，独立 sampling 在不需协调输出集合时最直接；DPP 等排斥目标可以提高批内多样性，却可能把同一视频内的帧推离连贯轨迹。一个有条件的分支用 latent proxy 分别计算 diversity 与 temporal consistency 的梯度，后者非零时只删去前者与它负对齐的分量，保留正交和正对齐部分。这比把两个 loss 任意加权多了一项局部方向约束，但只保证一次足够小的更新不在一阶近似下降低所选 proxy，不认证有限采样轨迹、真实语义一致性或每个 prompt 的质量。[必要采样机制与直接对照](https://arxiv.org/html/2602.15287v1)使用学习得到的 embedding/interpolation proxy，不能把避免在线 decoder 反传解释成无需前置训练。<!-- source-family:SF-2026-ARXIV-2602-15287 -->

这条分支仍支付离线 decoder/encoder、proxy 训练、联合输出梯度和完整 flow 采样成本。受限 Wan2.1-1.3B、50 steps、十个给定 prompt 的主对照还同时改变 latent embedding，只有同一 learned branch 的去调节消融更接近方向约束的局部作用；其中 video-level 多样性可改善，frame-level Vendi 仍落后 DPP，temporal MSE 虽优于 DPP却差于独立 sampling，故不是全质量支配。Proxy 漂移、参考梯度退化、细节损失或净费用不合算时，应回退已验收的 IID、保守 DPP/guidance 或重校准，而不能把表示上的一致性签作物理运动与 World Model 状态证书。

若运动要求难以仅由 prompt 稳定表达，还可以先把对象位置、尺度、旋转与可见性编成有限运动 primitive，利用对象 crop/mask 和背景渲染 coarse-motion scaffold，再让生成模型补细节。这把外部运动脚本与视觉生成分责：脚本可确定性执行其支持的轨迹，却不认证语言模型提议的状态、接触关系或动力学正确。[一个受限视频生成分支](https://arxiv.org/html/2601.09255v1)在当前 flow 状态估计 clean latent 与 implied noise，仅用 motion mask 替换 clean 估计中的参考区域，再以相同时刻和原 implied noise 重构状态；保留这个噪声分量不等于保持原生成密度，后续 learned updates 也不保证最终严格沿脚本轨迹。

coarse scaffold 因而是采样约束 proposal，而非物理证书或 World Model 的 action outcome。关键帧生成/编辑、分割、脚本拟合、渲染、编码和迭代 refinement 都需分账；无需训练不等于没有前置调用或完整 stage 成本。受限对照中，更换基础模型的 no-plan 组不能独立归因规划收益，global SDEdit 与 masked refinement 同时改变空间选择和 re-noising，也不能单独证明 noise consistency 的因果效果。脚本支持域、mask、身份保真或质量/成本失配时，保留普通 I2V、已验收的 SDEdit 或更保守局部编辑，而不由局部观感指标批准任意物理运动。<!-- source-family:SF-2026-ARXIV-2601-09255 -->

二维投影还可能把交近、遮挡的不同点轨迹编成相似控制输入。一个受限条件分支分别编码点的初始身份与当前运动：初始位置保留对应关系，逐时坐标、派生深度与编辑 mask 表达运动和可见区域；任意局部参考帧另供外观条件，而不是只由首帧同时承担身份、外观和后续运动。[FlexAM 的必要接口与对照](https://arxiv.org/html/2602.13185v1)还把控制密度交给 timestep 条件，使稀疏与密集轨迹不被默当同一支持域。新增 VAE/CNN adapter、tracking/depth/分割及完整采样都需计费；派生深度不是物理真值，稀疏子集的不同采样人口和定性消融也不证明各部件独立因果。相机旋转改善仍可伴随平移退步，外观保真、轨迹质量与净成本应分别验收；点身份、遮挡或密度失配时，保留已验收的二维 scaffold、密集控制或普通 I2V，不由局部画面指标认证物理运动正确。<!-- source-family:SF-2026-ARXIV-2602-13185 -->

相机与角色姿态易互相代偿时，分阶段训练还可先消除一部分数据混杂：先用 canonical A/T 静态姿态建立角色基础，再训练相机编码器——先冻结主干、随后联合更新——最后加入 orbit 轨迹适配。这里 Stage II 并非始终冻结；canonical 数据条件与训练次序共同定义接口，不仅是已有 motion/camera 两编码器的改名。<!-- source-family:SF-2026-ARXIV-2601-05722 -->

[受限角色视频对照](https://arxiv.org/html/2601.05722v1)中不分阶段的 joint 路径可忽略 camera，支持这条条件化分支；Fig7主要为定性比较，46K专有角色/120K视频与阶段预算未充分匹配，不授唯一因果或所有主干泛化。Canonical 数据制作、相机适配和 orbit 训练均付费；姿态支持不足、镜头控制失效或净质量回退时，保留原独立/联合控制、普通I2V与更简单 scaffold，不以分阶段标签认证几何或动力学真值。

控制条件的表示还要处理二维投影丢失的手部关节信息，以及相机运动与手运动的歧义。一个受限分支把渲染的二维 skeleton 编成视频 latent，再把三维关节/手腕运动编码注入同一 patch 表示；相机的 Plücker 条件保留独立 encoder，先分别训练手和相机控制，再联合适配，而不要求单一二维轨迹同时承担投影、灵巧姿态与视角变化。[Generated Reality 的必要混合接口](https://arxiv.org/html/2602.18422v1#S3)因而扩展了外部控制的表达域，不把它变成真实动力学证书。新增运动/相机编码、分阶段训练与完整视频采样均付费，pose/camera 的派生评价仍是 proxy，联合控制也有单控制分支更好的反侧。14B 模型的机制评价不能与另一个蒸馏 5B causal 部署合并为同一操作点；后者 H100/Quest3 的 11 FPS、约 1.4 秒延迟及仅 conditioning 的局部开销，不认证现代 VR deadline 或物理动作安全。遮挡、漂移、投影或联合控制失配时，应保留较简单二维 scaffold、独立控制与普通 I2V，按控制误差、视觉质量和总时延分别验收。<!-- source-family:SF-2026-ARXIV-2602-18422 -->

干净运动 scaffold 是外部已给条件；若运动本身也需要生成，则可让 motion 与 video 成为两个共同推进的 noisy producer，而不把其中一支伪装成固定真值。一个分支先将 SMPL 的 normal/part 渲染编码为 motion latent，再与 video latent 同步去噪；两支交互后，原 motion latent 继续进入下一 motion block，融合 latent 则供独立的 3D readout head 使用，motion 还经零初始化线性接口注入 video。生成状态的推进与融合表示的读取是不同 consumer。[CoMoVi 的 Eq3–11 及直接消融](https://arxiv.org/html/2601.10632v1)中，把融合结果直接替换 motion block 输入反而退步，故不能概括为任意双向融合均有益。<!-- source-family:SF-2026-ARXIV-2601-10632 -->

这种联合生成增加第二条主干、motion 域适配、监督 head 与共同采样费用；派生的 CameraHMR motion 标签和渲染 latent 并非真实 3D 或物理证书。24 A100、BF16、81 frames 的局部设置及约15分钟生成5秒视频，只支持该预算下的接口可行性，不是生产延迟；不同模型/训练预算的基线也不单独认证融合收益。视频观感、motion readout 与物理有效性仍须分别验收，不能由共生成推出可执行动作或 World Model 状态。teacher 标签、motion 支持域或预算不合算时，已给干净 pose/scaffold 条件、普通 I2V 加独立 pose extraction 与更保守的局部控制继续成立。

同样是一阶更新，velocity的求值位置也可以不同。一个lookahead分支先估计下一状态，再在该状态与下一时刻求值，用前视修正替代仅在当前状态求值；理想implicit forward-value需要知道尚未求出的更新，不是部署可直接调用的oracle，实际估计只在其平滑性、网格与近似条件下受控。局部阶数、更新iterations、NFE、可复用的缓存和真实时间应分别记录，不能由“仍是一阶”推断同样成本，也不能把减少iterations当减少网络调用。有限步/特定数据对照并非处处优于原solver；估计失配或额外求值不划算时，保留当前状态Euler、已有高阶solver或更多步数。<!-- source-family:SF-2026-ARXIV-2512-24927 -->

### 反向核与训练状态分别约束哪些误差

增加网络容量、优化训练与增加采样步数，并不都在修复同一个误差。单高斯 reverse kernel 是易拟合、易采样的基线；若一步条件分布需要更丰富的形状，可以采用固定高斯 components 与由有限特征驱动的 ReLU logits。在真实 reverse kernel 确实经这些特征分解、密度满足相应正性、连续性与矩等假设时，输出 conditional KL 可以由 terminal 分布不匹配及逐步 mixture/logit 近似误差共同上界。这个分解把 kernel 表达性与初始化分布分开，不是声称所有单高斯模型都有同一个严格误差下界。<!-- source-family:SF-2026-ARXIV-2604-13470 -->

在 exact terminal matching 下的任意精度逼近，是模型类的存在性结论，不证明有限数据、实际优化器或少步预算能找到该模型；仅扩大 mixture 与网络也不会消除上界中的 terminal mismatch 项。更多 components、特征和 logits 带来参数、校准与采样成本，给定特征充分性本身也须另验，高维构造并不解决维数代价。实际选择仍要分别检查训练误差、初始化、求解器与质量/成本；单高斯 kernel、成熟 schedule 或更长 horizon 在其质量预算成立时继续合理，不由表达性定理直接宣布部署优势。

迭代误差还改变训练状态的支持范围。只在 clean sample 的前向加噪状态上训练，在模型 rollout 与训练路径接近时简单有效；若自生成状态逐步偏离，训练可以从当前模型的一次 detached CFG Euler step 构造局部偏轨迹状态，再用同一 noise endpoint 重加噪，监督其 velocity 回到原 clean anchor。这样把纠偏责任前移到训练状态，而不是只修改采样器，或在完整生成后用 terminal reward 评价。

该构造指定了局部训练 target，不证明任意偏轨迹状态都对应唯一 Bayes 真值，也没有覆盖完整推理分布。额外 CFG forward、辅助噪声点与 loss 权重增加训练成本；受限 SD3.5 结果、相同步数和不同适配方式不能当作匹配总 compute，各噪声分支也并非全指标更好。稳定 SFT、求解器改进和 reward-based 后训练各有成立条件；只有偏轨迹纠偏、质量/多样性及净成本在本模型得到独立验收，才采用这种训练 support 扩展，不把它升级为 RL 的替代品。<!-- source-family:SF-2026-ARXIV-2604-12617 -->

若同一图像的各 patch 可以在不同噪声时刻训练，只平衡平均噪声仍可能让几乎每个训练样本含有接近 clean 的局部信息；其他位置利用这份信息时，从纯噪声出发的部署起点就缺少相应训练支持。一条替代采样分支先选择允许的最干净 patch 时刻上界，再在更噪一侧采样其余 patch，而不是只约束均值。这个上界约束训练状态的可用信息，并不表示有限样本里一定有 patch 恰好取到上界。<!-- source-family:SF-2026-ARXIV-2604-19141 -->

训练支持的调整也不自动批准自适应去噪。额外的 difficulty head 只能以速度预测误差提供相对难度代理，让较易 patch 先推进、再与难处对齐；它不是校准的不确定性或最优资源分配真值。受测配置有质量退步，固定 NFE 也不等于相同 wall-clock；head 训练、异步调度和整模型 forward 都须计成本。代理失准或净收益不成立时，统一噪声时刻、同步采样器和原生成路径仍是可核验的回退。

多回合音频编辑还有 history 与 target 的联合噪声支持问题：若训练始终提供干净的上一回合音频，相关 target 容易通过复制条件来预测；若所有回合共用一个噪声时刻，又不一定见过部署时“干净 history、纯噪声 target”的组合。一条条件分支对各生成回合分别采样噪声时刻，再让当前回合消费先前音频与文本上下文，扩展这个组合的训练支持，而不改变干净 history 在部署时作为条件的职责。[AudioChat 的必要方法与直接对照](https://arxiv.org/html/2602.17097v1)还改变了 understanding/generation 层接口，因此其 SCT 架构对照不是独立噪声采样的单因素因果验证。冻结 codec、3.6B 模型、多阶段训练与完整迭代采样仍需计费，私有数据及当时未发布模型也限制复核；editing-preservation 是模型 sensor 差值，不是真实音频相等，受测接口不胜全部指标，更不授实时 SLO。若 history–target 支持或净收益未验收，单回合条件编辑、统一时刻训练及已验收的原生成路径仍可保留。<!-- source-family:SF-2026-ARXIV-2602-17097 -->

联合音视频编辑还要逐流声明 preserved 与 regenerated 支持集，而不能继承同一 mask 的承诺。一条双 MMDiT/cross-attention 分支以 video latent 的 binary mask 指定视觉保留域，但 audio 全程从 scratch 生成；音频先更新、再供 video 更新及时间 RoPE 对齐只是耦合机制，不认证原声保真或真正同步。即便画面某区被保留，也不得据此批准其声音未改变。两分支、AV 数据、低清全帧/高清 keyframe 与 refiner 都付费，厂商有限人评没有 architecture ablation 或完整 matched budget，不能把偏好唯一归给 cross-attention。各流保留验收、同步与净成本不稳定时，保留独立音/视频编辑或明确全流重生成，不把联合生成的观感当 World Model 真值。<!-- source-family:SF-2026-ARXIV-2602-21818 -->

### 连续高斯去噪迁往离散文本时，采样路径也要重验

把 token 映射到连续 embedding 后复用图像 DDPM，保留了成熟的训练目标和采样器，看似只改变数据表示；但若干净数据集中在分离的离散模态，去噪后期的分布会变成多峰。单步均值更新可能把轨迹带到模态之间的低密度区，下一步预测便以训练时少见的状态为条件。失败不一定表示模型从未学到目标 token，也可能来自求解器与离散数据几何不匹配；因此只比较最终 loss 或固定步数不够，还须检查不同噪声阶段的轨迹质量。临界区间取决于噪声 schedule，不能把某篇实验的时间阈值写成通用常数。

一条条件分支是在该区间改用重新从前向噪声分布采样的更新，并在训练中让模型更常见到自己的上一步预测。它能降低错误前缀持续传播的风险，却改变了采样分布：这种更新不是原 DDPM reverse process 的严格求解器，较高正确性可能以多样性下降为代价；self-conditioning 又增加训练成本。若任务重视分布忠实度、已使用更平滑的连续 latent，或质量—多样性验证不通过，原求解器、离散 diffusion 或 AR 仍可能更合适。现有解释来自可测密度的层级玩具模型，文本、代码和蛋白质实验仅验证所测配置；同类更新在受测连续图像任务反而有害，不能外推为通用 diffusion 加速或质量方案。[原始研究](https://arxiv.org/html/2604.02028v1)支持这一受限机制。<!-- source-family:SF-2026-ARXIV-2604-02028 -->

连续score模型还有一个局部敏感性问题：同样大小的score误差，在不同轨迹位置不一定造成同样的终点偏移。对正且光滑的热扩散密度，score `s=∇log p` 的演化对应Burgers型方程；在可作二元分解的模态边界，两个分量的log-ratio给出一个随噪声下降而变陡的tanh界面。对称两高斯的中心边界中，反向时间的局部扰动增长率为 `(a²−σ_τ²)/σ_τ⁴`，只有低于分岔噪声尺度才为正。这个解析例子解释了为何模态选择附近的积分误差可以被放大，也提醒我们不能仅凭平均score误差认定每条生成轨迹同样可靠。<!-- source-family:SF-2026-ARXIV-2604-07404 -->

它提供的是受假设约束的机制解释，不是已经验证的新生产sampler。额外检查局部score变化或在敏感区增加求解步骤会支付诊断/NFE成本；实际网络的近似误差、多个模态交汇和随机反向过程仍需单独验证，不能把对称二元中心轨迹的解析增长率套给全部数据。固定schedule在分布平滑、预算明确且质量已验收时仍合理；几何诊断只有与真实模型的质量、多样性和端到端成本对照成立后，才可用于调整schedule，而不能由理论建议直接宣布加速或无损。

若求解器还消费 score 的 Jacobian，函数拟合与导数拟合又是两道不同门槛：小的加权 L2 score 误差不能单独排除低振幅、高频误差的导数仍很大。一条受限统计理论在有界低维 Hölder 数据加 Gaussian 噪声、指定平滑模型类与 ERM 条件下，把 Jacobian 误差同时绑定到函数误差、高阶加权 Sobolev 控制和噪声尺度；它不是任意神经网络只要训练 MSE 小，自动微分就可信的保证。高阶正则的全局控制实际难以强制，维数常数、低噪声敏感性与校准/导数估计成本也没有消失。因而需要分别验收函数近似、导数近似和有限步 solver 误差；只需 score 的普通采样路径仍可使用原模型和求解器，不能为启用导数而把上述条件界升级成完整 ODE 误差或真实生成质量保证。<!-- source-family:SF-2026-ARXIV-2512-24378 -->

若数据能由平滑的 Gaussian mixture 表示，还可先用其解析 score 构造 reference flow，把学习 score 的误差从求解器诊断中拿掉，再由生成的 noise–sample pairs 训练单次映射。这里 training-free 只描述解析 score 路径，不描述后续 neural map；需要分别记录数据近似、有限步积分和压缩拟合误差，不能用 reference solver 更准替最终映射放行。<!-- source-family:SF-2026-ARXIV-2601-19740 -->

[受限 GMM 理论与实验](https://arxiv.org/html/2601.19740v1)的 Euler L2 界依赖固定均值半径和受控协方差谱，L∞ 对数维数界另要对角协方差；常数还会随小特征值恶化。部分 L∞ 试验改变了均值人口且使用 full covariance，不能继承该定理的完整保证；拟合单 map 的误差又可主导积分误差。GMM 密度近似、每步 mixture 求值、reference 采样和 MLP 训练都计成本，维数趋势不认证媒体质量或部署 SLO。数据近似或谱条件失配时，保留 learned score、更多步/既有 solver 与独立终态评价；需要压缩时单独验收 fit 误差，而不是把“无需 score 训练”写成无需训练或无误差生成。

若 denoiser 连当前 noise level 都没有读取，误差还需多分一项：把多个噪声尺度混合训练的 population MSE 解，等于按给定 noisy observation 的 noise-level posterior，对各尺度条件去噪结果取平均。它不是已知噪声模型的同一接口；使用者须同时核验 denoising 学习误差与噪声尺度估计误差，而不能只看到不输入 timestep 就宣布省掉了其不确定性。在一组有界 support、低 intrinsic metric-cover complexity 相对高 ambient dimension、指定加权 population L2 学习误差与 noise prior 条件下，单个高维 noisy sample 可提供尺度估计的信息；这些条件说明一种 blind denoising 分支为何可能成立，不是任意图像或 latent 都能可靠估噪的保证。<!-- source-family:SF-2026-ARXIV-2602-09639 -->

这个分支的比较 metric 还依赖原数据 support 的 projection，不能直接当作可在线计算的语义距离或 FID 替代；有限步 exponential-Euler 的条件结论也不能迁往任意 sampler 或 masked language model。理论 prior、实验 prior 与实验更新并非同一完整处方，初始化 KL 与正文 Corollary 的噪声参数还有未闭合关系，因此不采用其完整生成保证。训练、posterior/尺度估计与实际采样成本仍须测量；若 support、尺度识别或质量/费用验收不成立，应保留显式 noise conditioning 与已校准求解器，不把“blind”升级成更通用、更便宜或已消除求解误差。<!-- source-family:SF-2026-ARXIV-2602-09639 -->

Blind denoiser 也不等于 schedule-free sampler。即使网络只读取 noisy state、没有显式时间输入，求解器仍可按已知 schedule 组合 `v=μ(t)u+ν(t)f(u)`；同一状态下 denoiser 的估计误差因而被 `|ν(t)|` 放大为 velocity 误差。[原版本的参数化分析](https://arxiv.org/html/2602.18428v1#S6)说明要同时检查估噪/去噪质量与该增益；控制ν增益是一种限制误差放大的手段，实际误差还取决于去噪误差的衰减，不自动证明最终采样质量，ν可能大也不证明实际误差一定失控。小型 matched 实验有高维 rings 上 blind noise-prediction 同样成功的反侧，另表借用既有研究，不能合成普遍参数化优劣。训练、尺度识别、时间系数和数值积分仍计费；域、路径或误差增益失配时保留显式 noise conditioning 与原 sampler，不把少一个网络输入误写成消除 schedule 或统一的生成保证。<!-- source-family:SF-2026-ARXIV-2602-18428 -->

同样的分责还会出现在推理时引导中：若目标分布是 base distribution 按已给定的终点权重 `w` 重加权，一个可学习的接口以 base 样本的加噪状态为输入、`w` 为回归标签，估计该状态下终点权重的条件期望 `h`，再把 `∇log h=∇h/h` 加到 base score。这里有三个不同对象：回归值、输入梯度和最终的对数引导；不需要 `w` 的梯度，不表示不必训练估计器或每步计算引导梯度。仅有小的值拟合误差不能保证后两者可靠，分母还需要受控的正下界。一条受限理论用带梯度惩罚的回归，把正则偏差、导数模型类复杂度与梯度误差分账；令惩罚趋零并不能免费继承梯度保证，其低噪声界也变敏感。采用时须另外计入估计器训练、每步求梯度与截断/早停成本，并确认正值和导数约束能在实际模型强制或验收；这些假设不是任意神经网络默认成立，也不替未知 reward 背书。条件或净收益不成立时，保留原 base sampler、降低引导强度或使用已校准的保守引导，不由这一接口直接宣布完整分布误差、质量或安全保证。<!-- source-family:SF-2026-ARXIV-2601-06514 -->

若不愿另训 h estimator，还可沿冻结生成器的随机转移取 Monte Carlo terminal samples，用终点 reward weight 与转移分布的 score 估计 h 的梯度，再以受控分母形成 correction；reward 无需可微，但转移/score 接口、base support、样本预算与正分母仍须成立。[DOIT 的受限分支](https://arxiv.org/html/2602.16198v1#S6.SS1)把每步完整 terminal rollouts 进一步换成 one-step lookahead，并复用当前 score 形成终点 surrogate；它减少 score-network求值，不等于没有 reward 调用，也不继承完整 rollouts 的理论精确性。低 h/罕见高奖励事件会放大方差，floor、引导强度和时窗都改变误差；有限美学 reward 对照均值相近不证明终态分布等价，报告的运行时间还排除了 reward evaluation。MC、reward query与score导数成本不合算、支持或质量回归时，保留受训 h、较保守引导或原 base sampler，不由“training-free”授普遍高奖励保证。<!-- source-family:SF-2026-ARXIV-2602-16198 -->

终点权重若有特定代数结构，还可以先问目标能否借 base score oracle 构造，而不一律把它交给估计器。一个受限连续分支在有界 support、全噪声尺度的精确 score 下，用平移查询加已知向量实现 linear reward tilt；低 rank 的半正定二次奖励再借 Hubbard–Stratonovich 写成这些线性目标的 mixture，但潜变量权重含各目标的 normalizer，不能直接抽 Gaussian 后就当已采到倾斜分布。[必要条件与反侧](https://arxiv.org/html/2602.16570v1)要求额外估 normalizer、离散潜变量网格和多次 oracle 求值，规模随 rank 增长；正负号、rank 与矩阵 entry scale 因而共同决定可行性。rank-one 半负定的困难构造含指数大的 entries，只排除不随矩阵范数付费的通用多项式算法，不证明所有负奖励都难。上述 W2 条件结论也不迁往误差未知的 learned score 或生产便宜：tilt 会把查询带离 base 人口，原拟合误差未必控制该路径。oracle、support 或预算不成立时，保留受训 h、MC 与已校准的保守 guidance，而不是因低 rank 或可解析奖励就跳过目标质量与完整成本验收。<!-- source-family:SF-2026-ARXIV-2602-16570 -->

非自回归文本生成也不必只在离散 token 上做 observation denoising。分层连续 latent diffusion 先由 Text VAE 建立稳定 text↔latent artifact，再由 block-causal DiT transport global semantic prior，最后由 conditional decoder 完成 local token realization；这把 global organization 与 surface realization 分成两个可独立失败的状态。收益是语义压缩与跨连续模态路线，代价是 VAE information loss、两阶段训练/版本耦合和额外 decoder；重构或 scaling gate 失败时回退 token AR/离散 diffusion。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-07933:start -->
把 Text VAE、latent diffusion 和 token decoder 分阶段冻结训练最容易定位失败；端到端 joint training 能让表示与生成共同适配，却也可能让 encoder 缩放、diffusion loss 和 decoder reconstruction 相互追逐而 collapse。训练 artifact 应保存 encoder/diffusion/decoder revisions、diffusion-to-encoder warmup、decoder noise、loss weights 与 time sampling，并分别验收 reconstruction、latent smoothness、PPL/diversity 和 NFE。任一阶段不稳时回退 staged freeze、离散 diffusion 或 AR，不能用单一生成分数掩盖表示塌缩。 [受限证据：arXiv:2605.07933v1]
<!-- semantic-body-binding:SF-2026-ARXIV-2605-07933:end -->

证据覆盖 8 个 benchmark、严格匹配的约 2B AR/LLaDA baselines 与至约 2000 EFLOPs scaling；不证明更大规模、真实 serving latency、质量等价或统一多模态能力。MULTIMODAL-REPRESENTATION 提供 latent identity；本章拥有 generation factorization。

另一条语言连续分支不依赖 image/Text VAE：把 token 学成 unit-sphere 上的 16D embedding，经 Gaussian corruption 后在 block 内连续去噪，最终以 categorical logits readout 返回离散 token，再按 block commit；clean AR prefix 的 KV 可跨去噪步复用。这里的 denoiser、embedding geometry 与类别 readout 是共同 artifact，不是把 image VAE decoder 改名。[受限 3B/8B 对照](https://arxiv.org/html/2610.02665v1)提供这条生成分解，不证明统一多模态或相对优化 AR 的端到端优势。<!-- source-family:SF-2026-ARXIV-2610-02665 -->

连续轨迹转离散 token 还需独立验收低 NFE 几何：readout 主要在 clean endpoints 训练，4/8-step 有明显质量损失，当前 PDD teacher 又关闭 self-conditioning，不能假定 student 继承原 teacher 的全部路径条件。匹配 denoiser calls 的局部高阶 solver 对照复用 DDIM-tuned CFG/ST，而非各 solver 独立调优；off-manifold 诊断只是局部推断。最终类别 readout 也计入总调用，蒸馏、引导分支与 decoder 敏感性均有成本；低步数回归时保留较多步骤、原采样或 token AR，不由连续表示授 few-step 无损保证。

连续文本去噪还可保留 token 空间，增加同序列的粗粒度辅助状态。固定 token-to-cluster 映射取自预训练 embedding 聚类，两种编码在每个位置拼接；序列不变长，但通道、输出与目标增加。同一网络联合去噪，通道可采用不同 schedule/churn，最终只解码 token、丢弃 cluster。这不是先提交粗类别再预测词，也不赋予 cluster 外部真值；映射、编码、loss 与 sampler 属于共同 artifact。

[HCDLM v1](https://arxiv.org/html/2610.08738v1)的约135M模型对照中，随机 cluster 未重现语义 cluster 的收益，但共享/分通道 schedule 随 entropy 各有胜负，早期 churn 可反退。聚类、通道与调参都付费，固定单层辅助类别不证明深层级、大模型或 few-step 无损。匹配 token-unigram entropy 下的 GenPPL 也不是语义正确或服务收益；质量或预算不成立时，单通道连续路径、离散 diffusion 与 token AR 仍是合理分支。<!-- source-family:SF-2026-ARXIV-2610-08738 -->

生成器的中间状态也可以来自视觉 refinement target，而不是文字计划。一个文生图分支将 draft、refine、final 三帧作为联合 latent trajectory，用 flow matching 训练同一视频 backbone，并仅解码末帧。为避免原 causal video VAE 的时间压缩把早期 draft 与后帧耦合，各帧分别进入 encoder 的初始单帧 window；这改变的是监督状态与 codec 接口，不是修复已被证明的未来泄漏。[CoF-T2I 的局部机制](https://arxiv.org/html/2601.10061v1)从噪声联合去噪整个三帧序列，没有逐帧 AR commit，也不能由三个输出的平均质量递增认定内部因果自纠错。<!-- source-family:SF-2026-ARXIV-2601-10061 -->

该分支支付三帧 latent 计算、合成 refinement 数据与 judge 成本，节省末帧以外的 decoding 不等于整个 pipeline 免费。Wan2.1 14B 的受限同设置对照中，target-only 为 .81、连续 VAE 为 .83、独立帧 VAE 为 .86；但连续基线把三帧补成五帧，layout 与序列长度也改变，不能把差额唯一归因于独立性。Imagine-Bench 的 spatiotemporal 子项还从中帧到末帧退步。64K 数据、1800 步、batch64 与 1024 平方输入不证明等 FLOPs，硬件、精度、采样预算和端到端耗时未披露。codec 身份、轨迹或净收益未验时，保留 target-only T2I 或普通视频生成路径；真正的因果状态提交仍按前面的 AR/runtime 边界另验。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-06548 -->

从成熟 AR checkpoint 转向 masked diffusion 时，表示能力与生成顺序不必同时从零学习。一个受限迁移路径冻结 AR teacher，用逐层 representation alignment 保留已有表示几何，同时让 student 通过 masked-denoising objective 重学可修订的 generation path。teacher 只拥有表示目标，diffusion objective 与 sampler 拥有新路径；表示接近不能授予行为等价或输出提交权。<!-- semantic-body-binding:SF-2026-ARXIV-2605-06885 -->

这条路径以 teacher compute、同构架构耦合和 alignment/objective 冲突换较低的数据重学成本。架构不同、表示失配或质量 Gate 失败时，应回退普通 diffusion continued training 或保留 AR。exact-v1 只覆盖同构 Qwen3 0.6B/1.7B/4B、作者代码任务和 0.8B/50B 数据条件，不证明跨架构迁移或 diffusion 普遍替代 AR。

### Timestep Embedding 也是可写入的控制通道

Diffusion scheduler 通常把 timestep 当成公开、无害的去噪坐标；若该 embedding 可被外部组件替换或调制，
它也能成为绕过普通内容输入的隐蔽信息通道。控制面因此必须把 scheduler、timestep encoder 与其参数
纳入 artifact identity，限制可写主体，并在 provenance/audit 中记录实际 embedding 路径。这个边界可以
同时用于防止隐蔽注入与声明生成来源，却增加签名、兼容与运行时校验成本；封闭、固定 scheduler 的离线
pipeline 仍可保持简单配置。现有证明与实验只说明受测 diffusion 架构存在该通道，不证明任意模型都可
可靠隐藏或检测信息。
<!-- source-family:SF-2026-ARXIV-2605-00935 -->

### Continuous 与 Discrete Flow 的等价是有条件的

把 continuous flow 与 categorical discrete flow 分开设计，在通常情况下是合理的：前者在连续状态中学习 velocity field，后者直接规定 token state 的转移与提交。但在一组严格条件下，两者可以建立可检查的接口。若 target 是 one-hot categorical state，source 按位置乘积分解且对坐标置换对称，不在 tie 或 threshold 上分配概率质量；同时 lifted coupling 与 position-wise argmax 兼容，并满足给定初始类别后的条件独立，那么 continuous convex interpolation 经 argmax 投影，会诱导出 discrete convex-interpolant conditional path。

这条 duality 的关键并不是“连续与离散本来相同”，而是揭示了 **source geometry 会改变 categorical transition 的有效时间**。连续 source 中任意两个坐标的 gap distribution 决定离散路径的 effective coefficient：Gaussian source 的类别切换会随 vocabulary 增大而延后，bounded uniform source 的时间尺度由 support width 控制，而 centered negative-exponential source 的对应表达式不显式依赖 vocabulary size。于是 source law 不再只是采样实现细节；它必须与 coupling、schedule、vocabulary 和训练 revision 一同成为 generation artifact，schedule calibration 也必须针对这组 identity 完成。

状态与控制权仍需分清。source、coupling 与 schedule 拥有“何时跨过类别边界”的条件路径；learned vector field 拥有实际 transport；sampler 与 runtime 拥有数值求解、token revision 和 commit。数学上的 path equivalence 不允许 runtime 把未校准的 source 替换成另一个 source，也不证明两个 learned marginal dynamics 会自然一致。破坏乘积分解、置换对称、无 tie、argmax-compatible lift 或 coefficient matching 中任一条件，定理就不能继续充当接口保证；bounded source 还可能在 continuous endpoint 之前使 discrete coefficient 饱和，迫使 velocity 的有效区间重新限定。

因此，采用新 source 或 schedule 的收益是可以显式控制类别转移 timing，代价是增加 source/coupling/schedule 的版本耦合、重新训练或校准以及 sampler compatibility 验证。已经围绕 Gaussian source 或既有 schedule 训练并验收的模型仍应保留原路径；不满足上述假设、需要 mask-source 语义，或无法证明替换后 vector field 与 commit 行为兼容时，也应回退原 source 与 schedule。现有证据给出了条件定理和证明，但经验部分只有 OpenWebText 上 10K-step 的 single run 与小型 toy trajectory；它不证明某种 source 的生成质量普遍更高，也不证明训练稳定性、吞吐或 serving SLO 获益。

<!-- source-family:SF-2026-ARXIV-2609-10863 -->

离散 flow 的概率接口还可以先对中间伪目标求和，而不是每次抽一个伪 clean 类别。对逐维类别状态、full-support prior 与指定线性条件路径，denoiser 的 clean 后验可显式加权各条件转移率；采样仍产生离散下一状态，但其转移概率可以缓存并由新模型重算，供后训练消费。可微的是这条概率计算，不是离散样本路径本身。prior、graph size、类别维度、时刻、有限步规则与 old 轨迹概率须绑定；按高 reward buffer 更新起点统计，或从优质图局部重新加噪再生成，都改变探索人口，不能只凭网络权重相同就宣称概率身份未变。

[Graph-GRPO 的有限一般图对照](https://arxiv.org/html/2603.10395v1)支持这个概率接口，但 row sum 为一不够：有限步的留在原状态概率还须非负，连续率不能未经步长验收直接变成可执行 categorical 分布。逐步 clipped surrogate、单样本 KL 项与整轨迹换测度也要分开，不补造精确全路径梯度或防 hacking 保证。固定64-node、小训练集的结构指标有收益和反侧，不同表的外部 baseline 配置不能合并成匹配预算结论；group rollout、率与 reward 重算、buffer、refinement 和预筛均付费。概率、覆盖或净质量不成立时，保留原条件率采样、已验收的有限步规则与 de-novo 路径，不由解析式批准全部生成质量或服务加速。<!-- source-family:SF-2026-ARXIV-2603-10395 -->

条件source还能改变训练与部署的可用信息合同。用目标样本、class或其他κ学习Gaussian source参数，可以让初始状态更贴近终点、降低轨迹曲率；但若κ只在训练时可见，直接部署这个source就无法采样，强KL约束回标准Gaussian又可能失去收益。中间分支在训练时连续插值条件Gaussian与标准Gaussian的**参数**，让同一velocity model见过这段source族；部署有κ时选择插值位置，没有κ时从已训练的标准Gaussian端点出发，不调用条件source预测器。这是训练覆盖的兼容分支，不是任意已训练模型允许换source。<!-- source-family:SF-2026-ARXIV-2604-09181 -->

它用额外source网络、联合训练和插值/KL权重校准换低步数质量，仍受Gaussian形式限制；KL过低或部署插值位置不合适可在较高NFE下退步。[MixFlow的受限实验](https://arxiv.org/html/2604.09181v1)只覆盖CIFAR10及64×64 FFHQ/AFHQ，不证明文本条件、全域覆盖或wall-clock/SLO改善；正文目标与伪代码的KL对象也不能合成一个已验证exact objective。原source已稳定验收、κ缺失而标准Gaussian分支质量未通过，或联合训练成本不合算时，应保留原Gaussian source和多步solver；第49/56章另验执行与调度成本。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-11311:start -->
Source identity 不只约束单个样本的 marginal，也约束一批样本怎样共同覆盖可能结果。Independent Gaussian seeds 在单图生成和故障隔离时最简单；若目标是让同一 prompt 的 gallery 在保持每张图 `N(0,I)` marginal 不变的同时扩大相互差异，可以显式设计 batch-level joint noise coupling。Coupling owner 只决定初始样本间的相关结构，denoiser 与 sampler 仍拥有单样本生成路径，gallery evaluator 才判断 diversity 是否值得采用。

联合 coupling 用批间依赖、额外采样状态和校准成本换多样性控制，也会降低复现与 failure isolation。当前证据只覆盖 SD1.5、SDXL、SD3、2,000 个 COCO prompts、三图 gallery 和作者指标，不证明其他 sampler、gallery size 或生产 SLO。单图、强复现、独立故障边界或 coupling 未校准时，应回退 independent seeds。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-11311:end -->

### Velocity 目标的混合表示与 Transport 分支身份需要分开

条件平方回归合理地估计局部平均 velocity，普通 marginal FM 并不会因多峰数据而在数学上失效；但在有限容量、少 solver steps 与多峰方向的工程约束下，可以改用 Gaussian-mixture likelihood，以 responsibility 分配 velocity targets。路径还可在每个 token 的起点选择一个 expert，并在整个 transport 中冻结该身份，使“目标怎样表示局部方向”与“这条轨迹由哪个分支承担”分开；这不是每一步重新执行动态 Top-K，也不是换 source 就自动获得兼容性。

混合目标增加 router、experts 与 encoder/decoder 的训练和执行成本，分支不可识别会让责任分配失效；K=1 或大方差也存在退化，当前 dense experts 不能当成第21章稀疏计算收益。`arXiv:2604.15009v1` 的 YAN/MoE-FM 仅覆盖任务微调的约200M/210M模型、单H200/B1/greedy与各方法oracle length，bAbI仍有质量落后；不同模型规模和该长度条件不支持普遍替代AR或服务SLO优势。原目标已验收、分支收益不足或质量回归时，普通FM/AR及更多solver steps继续成立。

<!-- source-family:SF-2026-ARXIV-2604-15009 -->

### 预测空间也可以从 Flat Vocabulary 改为树上的条件分支

离散 diffusion 通常在每个待修订位置预测完整词表，语义最直接，却重复支付大输出 head 的计算和存储。一个条件分支先将 token 组织为树：前向过程从叶子逐级退到祖先，反向过程在当前父节点条件下预测子节点，训练目标按层分解再合成。它改变的是中间状态和去噪路径，不只是为原目标套一个 hierarchical softmax；树、各层 schedule、目标权重和采样步数分配必须作为同一生成 artifact。<!-- source-family:SF-2026-ARXIV-2604-03537 -->

较小 head 能把资源转给 backbone，却把粗层错误、聚类偏差与跨层预算分配引入生成链：过重的粗层 loss 或过多粗层采样步在作者设置中会退步，小模型也没有全面超过既有分支。受限 OpenWebText、512-token 和四张 RTX3090 的结果支持资源重新分配的可能性，不证明大型模型、长上下文或服务尾延迟收益。树的条件划分不稳定、额外层次抵消 head 节省或质量验收失败时，flat vocabulary diffusion 仍是更简单的基线。

连续与离散分支也可以共用一个 backbone，而不强迫它们共用表示和输出头。数值若被拆成文本 token，精度与跨度可能受词表切分限制；一个混合类型分支把归一化 scalar 经冻结 numeric codec 与可训练 projection 放进指定 placeholder，数值加 Gaussian noise，文本和类别仍作 masked corruption。共享时钟的双向模型同时预测两类状态，数值回归与 masked-token CE 分别定义；采样一轮内更新 token 与 numerical state，最后再反归一化。[受限联合生成对照](https://arxiv.org/html/2602.22586v1)显示分布形状和跨字段复制准确率并不是同一目标，复制型任务中 AR 仍可更好；共享 noise schedule 也可能不合适。Numeric codec 预训练、LoRA、双 loss 校准及逐轮采样均付费，不能把共享模型当作自动保真或免费加速。Codec 支持域、联合依赖或费用不成立时，保留文本化数值、显式规则校验或独立两类生成器。<!-- source-family:SF-2026-ARXIV-2602-22586 -->

## Masked generation：未知位置与已知位置

masked model 维护部分可见序列：

```text
known tokens + [MASK] positions
```

每轮对多个 mask 产生预测，再按 confidence 或 schedule 提交一部分。保守 schedule 一次只接纳少量高置信 token，质量更稳但并行收益有限；激进 schedule 接纳更多 token，早期错误会成为后续条件。

逐位置排序之外，还可先由 duration predictor 划定 speech-frame segments，以当前预测的平均 confidence 选择一个 segment，再在段内按随机顺序逐 frame 揭示。这里分开了“先处理哪一段”与“段内下一位置及其取值”两级接口；duration 是时长提案，confidence 也不是语义真值，不能把这条[受限语音分支](https://arxiv.org/html/2601.08450v1)写成 Top-K frames 并行或独立 Mel-bin 概率已给出 frame joint posterior。单 speaker 的局部评价中，duration MOS 仅与基线相当，更大的 K 改善 MCD/F0 却损 UTMOS，质量对象不能合并成普胜。Duration/encoder/vocoder、反复 full forward、排序与训练都付费；时长边界失配、质量回归或预算不合适时，保留固定顺序、逐位置保守 schedule 与原条件生成。<!-- source-family:SF-2026-ARXIV-2601-08450 -->

若希望模型适应更大批量的提交，还可把“先揭示哪些位置”作为训练条件，而不把教师填入的内容当作正确答案。一条受限分支从教师去噪轨迹取得 unmask 顺序，即使教师最终回答错误也可使用该顺序；学生在相应部分可见状态上，仍以原始 gold token 计算 masked-position CE。这把调度经验与内容标签的权限分开：顺序监督尝试降低并行恢复的难度，不认证该顺序最优或最终答案正确。教师轨迹采集、课程阶段和 adapter 训练都新增成本，单加噪声训练也可能退步；推理期 active、stabilizing 与 completed 状态影响重算和缓存资格，不能由训练过该顺序推出已提交状态永远精确。较少 forward 或更高 tokens-per-forward 也不等同包括训练、刷新与调度的总成本改善；顺序迁移、质量或实际预算不合适时，保留原 gold 监督、保守 schedule 与全量重算。<!-- source-family:SF-2026-ARXIV-2601-07568 -->

顺序来自teacher、内容仍由gold监督，与把同一次teacher生成的中间mask状态和最终文本一起用作训练标签，是两种不同身份。后一分支保留状态与终点的配对，再以teacher/reference的conditional likelihood提出偏好，并按较早揭示的位置加重path CE；teacher内容可以错误，早揭示权重也不是因果credit。[必要对照](https://arxiv.org/html/2602.12262v1)只支持teacher条件轨迹训练，teacher与更新后的student共享中间marginal仍是假设，不能由初始化相同推出部署占用分布已覆盖或真实joint KL已最优。Teacher生成、reference刷新/采样、likelihood和全参数训练都计费；少步质量、原full-step能力、输出长度及实际step/墙钟须分验，恢复完整decoding仍可能退步。轨迹支持或费用不成立时，保留原gold内容监督、clean蒸馏与完整保守decoding，不因模仿顺序便授予正确提交。<!-- source-family:SF-2026-ARXIV-2602-12262 -->

训练顺序若由当前模型在线选择，还须核验前向 mask law，而不只问顺序是否有用。一个 teacher-forced 分支按当前 confidence 揭示 gold token；只有对固定部分可见状态，forward probability 可写成与 clean sequence 无关的因子乘上已揭示 token 匹配指示时，Bayes 归一化才消去该因子，保留原 data conditional。模型选择顺序本身不自动满足这份条件，多个位置的独立预测也不等于精确 joint posterior。<!-- source-family:SF-2026-ARXIV-2602-10314 -->

[PUMA 的必要条件与局部对照](https://arxiv.org/html/2602.10314v1)支持这一训练分支，但 streaming chain、refresh 和 K scheduler 增加状态与计算，低 threshold 或去掉 scheduler 也会退步。125M 模型的 iteration-to-target 不授同 FLOPs 或服务加速，AR 初始化预算也需计算；有限 latent/oracle 条件下的复杂度结论不能迁往任意 LM。mask law、近似 joint 或质量/费用失配时，固定 mask、原 gold 监督与保守 reveal schedule 仍是清楚的回退。

位置监督也可以来自离线的“正确 token 比最佳错误 token 更占优势”排序，而不改变在线的 token predictor。这个 Gt-Margin 需要 gold，因此只能生成训练顺序；另一个 planner 读取 prompt、部分可见状态及 predictor 的 argmax 补全 hypothesis，学习在该状态先揭示哪些位置。由 oracle rank 构造不同已揭示人口，再用 ranking loss 训练 planner，改变的是 where-to-unmask 接口，不是让推理期获得 gold 内容或证明每次提交都正确。<!-- source-family:SF-2026-ARXIV-2602-09501 -->

[Where-to-Unmask 的必要对照](https://arxiv.org/html/2602.09501v1)中，独立 LLaDA-8B LoRA+MLP planner 只在前半段排序，后半段回到普通 Margin；全程 planner 更差，Sudoku 的混合路径也低于 Margin。Gold/rank 采集、额外模型训练与 planner forward 均需计入成本，固定长度、每步一 token 的质量实验不证明低延迟或并行吞吐；正文与附录还存在 GSM 长度配置不一致。任务、长度或额外计算不合适时，保留高 confidence/Margin、原内容监督和保守 schedule，不把 oracle 的离线优势写成可部署的通用质量增益。<!-- source-family:SF-2026-ARXIV-2602-09501 -->

提交门槛之前，还可以先限制哪些位置有资格参与本轮预测：滑动窗口以最左侧未解码位置为起点，同时约束窗口长度与其中的 mask 数，再接纳窗口内超过 confidence 门槛的位置。若另规定每轮至少提交最高置信的一项，低于门槛也可能被接纳；这是推进规则，不是正确性保证。训练采用大块 semi-causal attention 时，窗口只能在既定块内细分，不能任意跨越训练时的 attention 边界。窗口外的 prefix 或 prefix/suffix KV 可暂时复用，active 区间仍需重算，并按新提交 token 数周期性重建缓存；“已经提交”不等于该 KV 永久精确。窗口、门槛、强制推进与缓存刷新应作为同一解码配置验收，记录额外重算和真实端到端成本；更大窗口或更少刷新不保证质量、延迟单调改善，验收失败时保留全量重算、固定块或保守提交。<!-- source-family:SF-2026-ARXIV-2601-02076 -->

位置排序还可以先探索不同的部分提交状态，而不搜索 token 值：从同一 masked state 分别揭示不同位置，各位置仍填 predictor 的 argmax，再以累计的每步平均 confidence 排序 candidate。一个条件分支让每个 beam 分别检查门槛：有高置信位置时并行提交这些位置，否则逐位置扩展；合并候选后，只有最高分候选来自 parallel 模式，下一轮才缩为单一路径，若最佳候选来自 position search，则保留预设 beam 宽度。这里调度器决定 where-to-unmask 和探索多少状态，内容 predictor 仍决定 what-to-fill；分数不是 joint likelihood 或正确性概率，剪枝也不撤回已经提交的 token。<!-- source-family:SF-2026-ARXIV-2602-10953 -->

这种切换把 position beam 预算与 parallel commit 预算分开，但付出多路 forward、状态复制、排序和门槛校准成本。固定每步并行数会损害所测位置搜索的质量收益，更多 beam 也可能只增加时延；[SOAR 的受限对照](https://arxiv.org/html/2602.10953v1)中，它仍可慢于 adaptive-parallel greedy，部分 Dream/GSM 设置甚至慢于普通 greedy。单 A100 的整套 benchmark 时间不证明生产并发或 tail SLO，confidence 与 AR-ness 的相关也不证明普遍 entropy-sink 因果。搜索不合算、分数失准或稳定流式提交优先时，保留逐位置 greedy、保守 schedule 或已有并行门槛，独立验收任务质量、真实墙钟和内存。

前瞻搜索还可以同时比较位置与所填 token 值，而不只累计已走路径的 confidence：先提出若干 candidate actions，各自暂时填入后再 forward 剩余 mask，按其 marginal entropy 减少量减本轮所填 token 的不确定性代价排序。一条[局部信息增益采样分支](https://arxiv.org/html/2602.18176v1#S3)用这个模型代理挑选行动，高 confidence 时可跳过候选搜索；entropy 不是事实信息，独立 marginals 也不等于正确 joint posterior或全局最优计划。此处 cost 是所填位置的模型不确定性，不是执行费用；这只是局部 heuristic，不授全局最优计划。共享 prefix KV 可降低复制量，却仍有 K×N candidate forwards、随 N 增长的 activation 与排序成本；batch 并行仅在硬件/内存条件合适时隐藏部分墙钟，不能删掉计算，bypass 还改变被搜索的人口。任务质量、输出长度、阈值、cache 与实际预算须共同验收；代理失准、内存或重算费用过高时，保留 greedy confidence、原 position beam 或保守并行提交，不把更少剩余熵当作正确提交证书。<!-- source-family:SF-2026-ARXIV-2602-18176 -->

固定块与固定 confidence 门槛还可以分别调整，而不是用一个“难度”分数同时决定边界和提交量。一条受限分支在前块完成后，对剩余 masked 位置重新 forward，以相邻位置预测熵的最大正向 shift 提议下一块右边界；最大 shift 低于阈值时合并尾部。另一个控制器用当前块起始平均熵相对截至当前的最大块平均熵，以及块内去噪过程的平均熵变化，调整 unmask 门槛。前者控制分块，后者控制块内并行提交；剩余位置的 shift 与历史最大块平均熵不是同一个状态。两者应连同模型、生成长度、阈值和 cache 模式共同验收，计入重分块 forward、熵计算、缓存刷新与校准成本。把 shift 解释为语义边界依赖有效词表近似均匀、块内平滑和边界搜索空间明显扩张等假设，不能因此证明块间独立、KV 精确或已提交 token 正确；受测任务也有质量退步。额外计算抵消收益、阈值失准或 cache 近似未通过质量检查时，固定块、保守 confidence 门槛与全量重算仍是合理回退。<!-- source-family:SF-2026-ARXIV-2602-04399 -->

并行提交还要区分 predictor 没学准与 sampler 把联合分布拆开两种误差。即使每个未知位置的条件分布都精确，同一轮在只看已提交 token 的条件下独立填多个位置，仍可能丢失块内依赖。一条受限 tau-leaping 分支按与 token 值独立的随机 ordered partition 分块，将 learning error 与平均条件 total correlation 分开；两者之和上界最终输出 KL，perfect predictor 时 factorization term 等于保留 partition 的 joint KL，不能反推它就是最终 KL 或必然的非零输出误差。依赖 profile 描述随机已揭示集合下的剩余条件相关，并给出 finite-K schedule 的精确 factorization objective，使预算优先分到相关性更强的阶段，而非仅凭 sampler 名称或每轮 token 数选步数。

最优 stationarity 不自动保证唯一解：shooting/bisection 要另有单调条件；profile 随长度一致收敛到连续严格正极限、且使用固定递增光滑 schedule 时，优化只改变 N/K 的 leading constant。特定退化的 exchangeable-mixture profile 才展示同 logarithmic 步数下不同 factorization 阶，不能转成通用 LM 质量定律；随机块大小也不等同固定逐位置计划。完整 profile 要付离线估计与优化成本，模型条件误差、有限样本及 coefficient 差分会污染它，toy exact-target 检查不是已部署语言模型或真实 latency/SLO 证据。profile、独立分块或成本条件不成立时保留原 confidence schedule、固定块或逐位置 sampler，并以实际输出质量、生成预算与墙钟独立验收。 [必要机制与反证](https://arxiv.org/html/2609.21960v1)。<!-- source-family:SF-2026-ARXIV-2609-21960 -->

但“单条路径更稳”与“多次采样能探索不同有效路径”是两个目标。在 self-scoring 且每次提交都满足给定置信门槛的条件下，高置信 gating 会给整条序列的熵设上界：继续提高局部确定性，可能改善一次生成，却压缩多样本搜索的有效分支。若任务要比较多条推理或代码候选，不能只用 `pass@1` 选择 unmask 策略；还应在相同采样预算下检查 `pass@k`、序列多样性与计算成本。一条实验性替代分支不是随机放开所有位置，而是让候选 token 的得分兼顾后续可达的序列空间；精确 lookahead 不可计算时，可用 mean-field 近似提出局部修正并批量采样。它用额外前向计算和近似偏差换探索空间，既不精确采样全局目标，也未在所有受测任务上胜过高置信路径。低预算、单答案质量优先时，保守提交仍合理；不能把[这项研究](https://arxiv.org/html/2604.00375v1)的条件性熵界外推到所有 diffusion decoder 或 AR 生成。<!-- source-family:SF-2026-ARXIV-2604-00375 -->

提交顺序也可以区分“这个位置自身很确定”与“它会影响其余位置的预测”。在给定单层 Softmax、块内 attention 近似不变及已解码位置能代表总体平均等假设下，可由 attention 的列和近似衡量后一种影响，并优先提交高影响位置；这优化的是可计算的近似目标，不是任意多层模型的全局序列 likelihood。并行分支再把低置信位置的最大影响设为动态门槛，只提交超过该门槛的位置，避免用固定数量强行放大并行度。

这仍是有损的解码选择：attention 不是真值或独立性证明，低置信组为空时的实现也需要明确规则。实际融合 kernel 不显式产生整张 attention，因而可在小 sub-block 内提取分数，再跨层与 head 聚合；新增访存、提取成本和子块近似必须计入真实延迟，不能把理论 FLOPs 除峰值算力当实测时间。[受限实验](https://arxiv.org/html/2604.08564v1)中平均任务分数改善，但部分模型/任务的并行分支仍低于其他 sampler，且单 A6000 的 tokens/s 不证明生产并发或 tail-SLO。短任务、严格流式提交或提取成本过高时，原 confidence schedule 与逐位置生成仍合理。<!-- source-family:SF-2026-ARXIV-2604-08564 -->

即使只用 confidence 选位置，也有两个不同的随机控制对象：token temperature 改变一个位置“填什么”的概率分布，position temperature 改变“先填哪里、这一轮提交多少”的分布。前者增大不等于后者也应增大。位置控制可以对 confidence 温度化后无放回抽取固定数量，也可以对每个位置作带阈值的随机接纳；它们改变 reveal order 与并行度，而不是把 confidence 变成正确性概率。需要多样本搜索时，这种分账比用一个温度同时代表内容探索和提交保守程度更清楚。

代价是多一组 schedule/阈值及搜索配置，更多随机位置也可能更早固化错误；候选间最终的 self-consistency 或外部 selector 又是第三个独立验收对象。[受限比较](https://arxiv.org/html/2604.09921v1)只支持 LLaDA-8B/Dream-7B、block32 与长度256等设置，位置随机化并非全部配置都更好；NFE 少不等同 wall-clock 或生产 SLO，四张 A100 上固定72小时的 RL 对照也不是固定更新次数的 sampler 因果实验。低预算、单答案或稳定流式需求下，固定高置信 schedule 仍合理；温度控制与上面的影响排序是可组合的选择，而非保证更高质量的替代定律。<!-- source-family:SF-2026-ARXIV-2604-09921 -->

训练路径的概率归因还应与推理期揭示顺序分账：任意顺序可以先绕过高不确定位置，但在需要探索逻辑分叉的任务中，这种自由未必保留更多有效解路径；应在相同 token/step 与多样本预算下比较 order 与 `pass@k`，不能把 fork 附近的熵关联当作普遍因果证明。一条[受限训练分支](https://arxiv.org/html/2601.15165v1)固定 autoregressive 路径，以可计算的 policy probability 执行 GRPO，而仍允许同一 masked model 在推理时使用 parallel sampler；固定训练路径不等于取消并行，也不认证推理联合分布精确或位置条件独立。额外 RL、概率重算与 sampler 校准都有成本，训练比较不能冒充纯解码顺序消融，少 step 也不等于低墙钟；探索或质量回归时，保留原训练目标、保守揭示顺序与分别验收的推理配置。<!-- source-family:SF-2026-ARXIV-2601-15165 -->

训练数据的布局也会与提交策略耦合。把同一题的多条 teacher trajectory 合在一个 canvas，再以 gold-conditioned summary 作监督，可以训练模型消费互相冲突的路径；推理时对每个 reasoning block 分配更新预算，块内再按 confidence 选位置。Gold 只属于训练标签，双向可见的 blocks 并没有因此成为统计独立对象；外部 AR scorer 的 prefix likelihood 差也不是数据独立性证明。[训练布局×解码的受限对照](https://arxiv.org/html/2602.23225v1)显示，未适配模型被强制并行可退步，适配后也不是所有 token 预算都应强制并行。Teacher 采样、summary 构造、SFT 与全 canvas attention 均需计费，较少串行步骤不直接证明墙钟加速。监督或质量预算不适合时，Long-CoT、普通 arbitrary-order 与保守提交仍是有效分支。<!-- source-family:SF-2026-ARXIV-2602-23225 -->

这解释了一个关键演进：

```text
只填充未知位置
→ 高并行填充暴露误差累积
→ 允许重写已生成 token
→ 显式训练 proposal + correction
```

后一步没有否定保守 unmask。它用更多训练与推理 work、mutable state 和提交复杂度换取更激进的并行 operating point。

可修订路径还可以改变反向时刻之间的耦合，而不改变理想的单时刻 conditional marginal。给定真实 clean token `x`，将原 reverse posterior 与重新加噪分布混为 `κ q(s|t,x)+(1−κ)q(s|x)`，对原 `q(t|x)` 边缘化后两项都回到 `q(s|x)`；κ=1 保留原 ancestral 路径。这个恒等式描述给定 clean x 的条件分布，不是数据 tokens 相互独立，也不取消 masking/uniform prior 的区别。

[Duo++ 的必要推导与对照](https://arxiv.org/html/2602.21185v1)在部署时用 learned denoiser 代替真实 x，故理想 marginal 恒等式不保证 learned endpoint 正确或任意步数收敛。κ、prior、schedule、denoiser 和 CFG/nucleus 共同定义 sampler；MCQ 多数仍落后 MDLM，训练 curriculum 的 GPU-hours 节省也不是 serving 加速。重加噪可能引入错误，额外迭代、词表运算和训练成本需与质量另验；质量或总预算不成立时，保留原 ancestral/保守 unmask 路径，不由相同理想边缘分布签实际等价。<!-- source-family:SF-2026-ARXIV-2602-21185 -->

重写位置还可以承担临时工作空间，不只是修复错误。一个受限理论例子要求采样长度n的均匀even-parity bit序列，而不是给定输入计算parity：第一轮生成n-1个独立临时变量y，并固定末位y为0；第二轮把各位置改写为相邻y的XOR（首位与初始0异或）。临时变量由相邻输出共享，最终序列因此具有偶校验相关性；每轮given当前可见状态的位置预测仍条件独立，相关性不是一次独立填充凭空产生的。若一经揭示就永久冻结，同一位置便不能先保存这种中间符号、再成为最终输出。

[该构造及下界](https://arxiv.org/html/2512.25014v1)只比较L=n、没有额外CoT工作空间、predictor与揭示选择器都是固定深度/poly-size AC0 circuit的exact sampler：冻结路径不能常数轮采样该分布，允许revision的路径可两轮完成。这不是任意Transformer或近似分布的下界。一般circuit的空间复用构造又需O(log d)深度的每步控制，目标深度d增长时不能称作固定深度；迭代轮数、工作空间、每轮全序列计算与硬件墙钟必须分账。重写还增加状态版本、训练覆盖和对外commit成本；无法训练可靠的中间状态、需要尽早流式发布或预算不足时，保守unmask与AR仍合理，理论存在性不证明实际模型学会了构造或服务更快。<!-- source-family:SF-2026-ARXIV-2512-25014 -->

允许重写还要解决训练见过哪一种错误。均匀词表替换提供容易生成的噪声，却可能远离模型自己会产生的语言错误；一个条件分支先从 masked input 采样当前模型的预测，再分别在 masked sequence 与 self-predicted sequence 上学习恢复同一干净序列。解码时，已填位置不立即成为硬条件，而是以 top-1 probability 加权 token embedding 与 MASK embedding，并校正混合后的范数；待填位置按从左到右的连续前缀推进，已有位置继续修订。训练噪声来源与中间状态接口因此共同变化，不是只降低 unmask 阈值。<!-- source-family:SF-2026-ARXIV-2604-08302 -->

这种不确定性载体有明确成本与边界：当前模型采样和两类训练输入增加训练工作，self-distilled target 仍可能保留原模型错误；低置信混合也不等于完整词表概率状态。连续两轮 top-1 不变或全位置高置信可以作为 block 的启发式结束条件，却不证明答案正确、原分布等价或全局收敛。作者消融中，未作这种 on-policy 训练的软输入路径失效，而作过训练后，软混合在最激进设置明显优于硬条件；部分高并行切片仍略低于原 checkpoint。质量优先、训练预算不足或 streaming 必须尽早发布时，保守 mask schedule 仍合理；新 checkpoint、软状态规则与停止阈值应作为同一生成 artifact 验收，不能当作无损 speculative decoding。

允许重写之后，下一问题是**在提交前该修正哪里**。只看单条 denoising chain 的 confidence，可能把早期错误锁定为后续共同条件；一条可选的 inference-time 分支让数条不同 reveal order 的路径并行推进，用它们在同一位置的分歧提出待核 span，再在检索到的证据条件下局部 remask、重新生成。路径分歧只拥有“值得复核”的 proposal 权，不能当事实概率；各路径一致也可能一致地错误，最终 claim 仍要由外部证据或拒答 Gate 验收。普通 confidence schedule 在知识稳定、预算紧或低延迟 streaming 时仍更合适。

多路径和局部修正增加峰值显存、检索与输出等待；若证据库过时或 span 定位错误，修正还可能引入新错误。现有 LLaDA-8B/Dream-7B 的 QA 与 hallucination 实验只支持受测 masked diffusion 路径：作者在 exact-match 标签下的检测 AUROC 低于一个训练式基线，换用 LLM judge 标签才高于该基线；四张 H200 上约 1.3× wall-clock 也不等于生产并发/SLO 收益。不能由此推断模型已经“知道自己不知道什么”，或把该机制移植为所有 AR/连续 diffusion 的通用防幻觉器。<!-- source-family:SF-2026-ARXIV-2604-01624 -->

错误检测也可以通过训练覆盖，而不必再次改变生成基座。联合训练生成器与错误检测器便于共享优化，却也让检测对象随更新漂移；一条替代分支先完成生成器 SFT，固定其参数，再只训练消费中间 hidden state 的 correction head。为了让检测头看到持续存在的模型错误，可以在更腐坏的状态采样该固定生成器的预测，再把这些预测注入上下文更丰富的状态，学习它们相对 clean target 的正确性。这里改变的是错误样本与上下文的配对，以及检测对象的身份，不是外部事实验证，也不要求把生成器再次共同训练。<!-- source-family:SF-2026-ARXIV-2601-06428 -->

[DSC 的受限结构证据](https://arxiv.org/html/2601.06428v1#S4)支持固定 generator、独立 head 和上述 FCA 配对链，不能直接授予完整动态 remask 配方：原文 BCE 的 target=1 表示正确，后面的同一 score 却被称为 error probability 并按最高值选择，方向未决，不能自行取反补齐；NoRemask 表格与随后文字也有数值冲突，不采用其普遍恶化论证。检测 head、额外 remask、blocked-index queue 与更多 iteration 均付费，没有通用即插即用或端到端加速保证。错误采样不匹配、sensor 校准不足或额外预算不合算时，保留共同训练、原生成器及保守 unmask；冻结参数只固定被测对象，不认证检测正确或最终答案可靠。

软状态还有一条不重训 backbone 的条件分支：只对尚未提交的位置，用截断预测分布的 embedding 均值与 MASK 混合，让相邻位置先消费暂定意图；预测分布连续两轮变化过大时退回 MASK，高 confidence 才转为不可撤回的 token。这与上面的 self-predicted 双输入训练不同：旧模型仍可能不熟悉软输入，JS reset 也只检测不稳定，既不是 correctness verifier，也不重开已提交位置。[Rejection Mixing 的局部对照](https://arxiv.org/html/2602.22868v1)中混合系数和阈值会改变质量，部分并行配置仍退步；词表混合、JS 与更多迭代都付费。原伪码仅等待全部位置提交，没有独立进度界，不能认证一般终止。部署需另设预算与退路；软状态、质量或进度失配时，保守 mask schedule、重算或 AR 继续成立。<!-- source-family:SF-2026-ARXIV-2602-22868 -->

多路径生成也可以把探索与最终解答分开，而不让一个路径的终点直接提交。对每条 diffusion trace，PRM 在它自己的 prefix 下评分；选择高分步骤及一条完整 anchor，再把带分数的材料交给 AR solver 重新解答。跨 trace 拼接改变了 prefix，原分数不能自动迁为新链可靠性，按步骤位置排序也不证明依赖一致；因此重算仍是生成，不是独立验证。[受限 stitching 对照](https://arxiv.org/html/2602.22871v1)支持同 solver 下的选择取舍，但错误高分、缺失子推导和更多路径反退仍存在。多路径驻留、PRM、通信与最终 solver 共同计费，原文不同 forward 口径不支持统一免费并行结论；预算紧或分数失配时，保留单路径、best-trace 与独立答案 verifier。<!-- source-family:SF-2026-ARXIV-2602-22871 -->

### 生成范式差异要拆成 Objective 与 Commit Policy

AR 与 masked diffusion 的输出差异不能全部归因于“单向或双向”训练目标。受控对照把 objective 与 confidence-based remasking 分开后表明，双向目标和迭代 commit policy 会分别改变 token entropy 与错误修正路径；因此比较生成范式时必须冻结模型规模、训练数据与采样预算，再单独改变其中一个状态。<!-- semantic-body-binding:SF-2026-ARXIV-2605-12522 -->

这些观察只覆盖所测语言模型和 evaluator，不证明某种范式普遍更有创造力或更可靠。无法隔离变量时，应回退端到端质量、延迟和 exactness 合同，不从文本风格反推内部机制。

跨范式比较还要把训练 bound 与生成测量分开：mask 与 uniform corruption 的 variational bound 松紧不同，较低 NELBO 或其 perplexity 不自动给实际输出质量排序。一个可复核的接口是在明确训练预算、数据和模型规模/结构的比较口径后，扫描各自 sampler 的步数，再绑定同一外部 scorer、输出长度、数值精度/entropy 与真实吞吐预算，比较各自达到质量目标的可行点。[受限 dLLM 对照](https://arxiv.org/html/2602.15014v1)使用 Llama2-7B GenPPL 和单 H100 80GB 上各模型可容纳的最大 power-of-two batch 拟合跨规模 Pareto；这是该 scorer、无条件生成和适配 batch 下的选择，不是一般质量定律或公平生产 SLO。另一个数学评价让所有 family 单 token 从左到右、batch 1 生成，因而不证明并行 diffusion 的数学吞吐优势。扫描、调参及外部评分都有成本，低 GenPPL 也不认证任务正确性；目标、评估器或预算变化时重测 frontier，条件无法对齐时保留已验收 sampler/AR，而不从一个训练 bound 或 step 数宣布范式胜负。<!-- source-family:SF-2026-ARXIV-2602-15014 -->

### 训练反向核也可以引入共享 Route Latent

Objective 与 commit policy分离之后，还需检查训练反向核能表达哪些联合依赖。逐位置 factorized reverse distribution 便宜且可并行，却可能让多个位置独立选出互不相容的 token；另一条分支用离散 route latent 的混合表示反向核，让条件化于 route 的专家分布仍可并行，而对 route 求混合后恢复部分相关性。训练时以可看 clean data 的 posterior router 教给只看 noisy state 的 prior router，推理只使用后者；route 在 token/层级参与计算，并非整条序列固定给一个专家。这也不同于额外训练连续 latent VAE。

离散 route 引入 router matching、straight-through sampling 和专家容量成本；E-MoE 的[§3/§5及Appendix B.3](https://arxiv.org/html/2609.37533v1)中训练为梯度估计保留 top-2 分支，推理前向选择一个 active expert，不等于总参数、FLOPs或 wall-clock只剩一个专家。作者在toy、MNIST与128-token LM1B小模型上的低NFE质量改进，随步数增多会缩小，部分已有 diffusion baseline 和 AR 仍更强；没有真实 LLM reasoning 或生产端到端时延证据。因此 factorized核、保守提交和 AR 仍是容量、路由校准或运行时成本不可接受时的基线，不从 latent 表示能力推导已验证的联合正确性。<!-- source-family:SF-2026-ARXIV-2609-37533 -->

### Uniform Corruption 的目标与 Token Time 是两种训练接口

离散 corruption 的类别也约束 objective。Mask corruption 明确告诉模型哪些位置未知；uniform corruption 则可能把任意位置替换成看起来正常的 token，使同一全局 timestep 难以表达各位置的可靠性。原 reverse-process ELBO 的均匀平滑项在忠实拟合该过程时有其意义，但在少步生成、复用 AR checkpoint 的目标下，过强平滑可能抑制 clean-token 预测。一个受限分支移除该平滑约束，保留抑制错误类别和提高 clean target 的更新，再为每个 token 提供不同的随机 time hint，以其边际均值保持全局时间。hint 是有噪条件，不是暴露真实 corruption 身份的 oracle。

这种选择同时改变训练目标与条件接口，不等于推理时自动获得 self-correction。LUDI 的[方法及对照](https://arxiv.org/html/2609.35817v1)在小模型上隔离 loss 变化，但7B转换还包含 block-causal attention、label shift 与辅助 AR loss，不能把所有收益单归于 loss。理想每步推进 token 数不等于真实加速；端到端推理与 loss operator 的局部提速、显存减少是不同分母，须在相同模型、batch、长度、精度和硬件条件下分别验收，不能由算子或理论并行度替 serving 作保证。原 ELBO、masked objective 与 AR 在过程忠实性、腐化身份不确定或 few-step质量未过 Gate 时继续成立。<!-- source-family:SF-2026-ARXIV-2609-35817 -->

### Masked Diffusion 的训练预算可以按 Locality 重分配

均匀采样 mask pattern 简单且无偏，但会反复训练相距很远、条件信息薄弱的位置。语言具有局部依赖时，可以重分配预测位置与可见 context，使每次更新更常覆盖有信息的邻域，从而改善同预算下的训练效率。<!-- semantic-body-binding:SF-2026-ARXIV-2605-13026 -->

这种加速依赖 locality bias，可能削弱远程依赖和全局一致性。现有实验不能证明任意语言或长上下文任务都受益；长程 slice 回归时，应回退均匀 mask、混合采样或显式增加远程依赖样本。

### 局部条件重采样可以复用预训练语言分布

从均匀 corruption 重新训练 masked diffusion，能够让训练目标与多轮修正完全对齐，但会放弃成熟 causal 或 masked LM 已经学到的条件分布。另一条受限分支把单位置 mask-infilling 看成局部 transition：每一步固定其余 token，只重新采样一个或一组位置；预训练 LM 提供条件分布或 energy proxy，Glauber-style sampler 通过反复局部 revision 逼近由这些条件共同定义的序列分布。<!-- semantic-body-binding:SF-2026-ARXIV-2605-04291 -->

这里改变的是 generation path，而不是凭空获得新的语言真值。模型只拥有局部 proposal，sampler 拥有位置选择、transition schedule 与 provisional state，runtime 仍拥有停止与外部 commit。复用已有权重可降低从零学习条件分布的门槛，却把成本移到更多 NFE、混合时间、mutable cache 和收敛诊断；有限步输出不等于已经到达 stationary distribution。受限证据还包含显著训练算力，未覆盖 streaming 与生产端到端 SLO。低延迟、append-only 或无法验证混合质量时，causal AR 仍是更可靠的回退路径。

复用已有LM条件之外，也可以为指定的离散加噪路径重新学习条件：若forward每步只改变一个坐标，canonical reverse需要的配置概率比率可约成“该坐标在其余坐标给定时”的条件概率比率。模型以噪声时刻、位置与其余状态学习局部partial energy，再经类别归一化构成条件分布；这把学习对象从global density或任意全局score改成逐时刻条件，但要求分母与支持有效，不让单点proposal自动认证完整joint。<!-- source-family:SF-2026-ARXIV-2602-20293 -->

逐位置训练、noise schedule与串行采样仍有成本，terminal混合误差、reverse估计误差与初始化误差也须分别验收；uniform worst-case条件不能由平均loss直接推出。[有限离散分布实验](https://arxiv.org/html/2602.20293v1#S5)中，soft-noise没有稳定胜过hard-noise，小样本后者更好，故不能把更多denoising步骤自动视为优于AR的证据。局部MLP、二值图像及低阶分布指标不授大词表语言质量或端到端加速；条件误差、混合或净费用未验收时，保留预训练条件重采样、原离散kernel和普通AR分支。

### AR 权重可以成为 Masked Diffusion 的兼容起点

从零训练 masked language model，attention pattern 与初始化都为双向修正服务，接口清楚但无法复用成熟 AR checkpoint；直接把整段序列改成双向可见，又会让 observed prompt 变成可修改状态并破坏 causal condition。兼容分支可以保留 prompt 内的 causal attention，只让 masked target 内部双向交互：prompt 仍是冻结条件，target 才拥有 provisional、可反复修正的 token state。

```text
observed prompt: causal and immutable
masked target: bidirectional and revisable
→ iterative target refinement
→ declared target commit
```

这使 AR initialization 能迁移到 diffusion training，但代价是 attention mask 的训练—推理差异、多轮 forward 与 target cache 的可变性。受限的 matched GPT-2 Medium/WikiText 实验只说明它优于对应 diffusion baseline；同规模 fine-tuned AR 仍更强，超过 512 tokens 与远域迁移还会退化。因此它是 AR→masked diffusion 的兼容桥，而不是 diffusion 已取代 AR 的证据。长文本、严格 streaming 或域外稳定性优先时，应回退 causal AR；只有 target revision 的质量与端到端成本都重新验收后才采用该分支。

<!-- source-family:SF-2026-ARXIV-2607-25157 -->

迁移时的 logit 蒸馏也要声明预测对象。AR teacher 的 next-token logits 条件化于 clean causal prefix，并不天然适合学生在腐化 target 的同一位置预测原 token。一个 blockwise 兼容分支先把 AR 模型改造并训练为固定块宽的 diffusion anchor，再让渐进合并后的学生读取与 teacher 相同的 corrupted state，在同位置对齐输出分布。这把兼容性责任落在 teacher 的训练支持、block/mask 与位置映射上，而不是只共享 tokenizer 或复制 checkpoint。<!-- source-family:SF-2026-ARXIV-2604-16514 -->

anchor 训练与多阶段蒸馏增加总预算，block 合并也改变并行读取与修订范围；冻结某个 teacher 不省掉其构造成本。原文固定 block 的多模态对照中 ChartQA 有质量退步，总训练预算没有完全匹配，不能称 AR 权重已经无损转成任意 diffusion 执行。没有相同 corruption/position 支持、长回答或域外质量失准时，应保留已有 AR、较小 block 或重新训练的 masked model；runtime 仍须另验迭代次数与实际时延，训练 logit 对齐不签发生产吞吐。<!-- source-family:SF-2026-ARXIV-2604-16514 -->

### Equilibrium Layer 把深度从训练图移到推理求解状态

视觉 AR 堆叠固定层数时，训练 activation memory 与推理计算深度一起增长；隐式 equilibrium layer
把重复变换表达为固定点，只保存求解所需状态，并允许部署时选择迭代预算。它获得训练内存与推理
深度的部分解耦，却把代价转移到固定点收敛、implicit differentiation、停止阈值与每个样本不同的
迭代次数。求解不收敛、延迟尾部不可接受或硬件更适合静态图时，应回退固定深度网络。作者视觉任务
结果只支持披露模型与求解器，不能证明 equilibrium 结构普遍改善视觉 AR 质量或生产吞吐。
<!-- source-family:SF-2026-ARXIV-2605-01220 -->

共享层也可以显式执行有限次loop，不要求固定点收敛。仅按最大loop数训练时，中间深度的状态未必可直接输出；因此可让同一图的完整深度作teacher，随机选严格中间prefix作student，对teacher预测停止梯度，同时两个分支仍更新共享参数。监督从真实目标逐步转向self-distillation，使较少loop也成为被训练过的输出配置。它改变的是中间深度的监督合同，既不同于implicit differentiation，也不是没有额外head/loss的免费adaptive depth。<!-- source-family:SF-2026-ARXIV-2604-09168 -->

这用训练目标和输出head成本换部署时可选的深度—质量曲线，参数复用却不省去每个loop的实际计算；共享block太小、loop远超训练范围时仍会退步。[ELT受限实证](https://arxiv.org/html/2604.09168v1)的MaskGIT/MAGVIT和DiT、ImageNet/UCF配置支持这种prefix监督，单独一层重复32次仍明显弱于更宽的unique block，不能把重复深度当无限表示容量。需要静态延迟、没有中间输出验收或loop外推失效时，固定深度网络仍合理；runtime必须把unique层数、训练最大loop、实际loop与sampler步骤一起记入生成身份，不能把FLOPs或参数量直接当生产吞吐。

训练有限递归还可以改变状态初始化和监督落点，而不只改变可输出的深度。单步去噪训练从腐化目标恢复答案，却没有直接训练同一转移被连续应用后的结果；一种替代是仍从腐化目标初始化，展开有限 k 次共享转移，只监督窗口末端，并让梯度穿过整个短窗口。它给中间路径提供面向末端恢复的训练压力，与同图完整深度指导中间 prefix 的蒸馏不同，也不要求对完整长轨迹做反传。<!-- source-family:SF-2026-ARXIV-2604-18839 -->

短窗口增加 activation 和多次求值成本，目标腐化也未覆盖推理时所有自生状态，不能由恢复准确率证明模型执行了规划。[受限递归实验](https://arxiv.org/html/2604.18839v1)同时改变模型配置、数据和展开长度，pass@2 与候选选择不等一次调用能力；扰动自身轨迹的 SPRM 分支在一项 7M reARC 对照中还低于原基线。超出训练窗口或状态分布后仍须独立验收，不能从短窗目标推出长程稳定；单步 denoising、固定深度与长轨迹反传分别在成本和任务约束下共存。

## Editable tokens 与 commit boundary

Commit 也可以用 candidate future dependence，而非当前 confidence，作为条件 sensor：同一模型在 No-Future（NF）与 Future-Aware（FA）的预测分布之间比较，future 来自模型自己的候选假设，不是尚未发生的真实 token。窗口、NF/FA 调用、分布距离与可见输出边界要共同版本化；训练截断参数 `α` 不能被误当 runtime confidence threshold。<!-- source-family:SF-2026-ARXIV-2604-23994 -->

候选生成与双条件求值增加成本，错误未来可能让稳定分布仍指向错误答案；cache 或 confidence 选择也有反向切片。受限 block64 实验不保证真实未来正确或外部提交安全；未来假设不稳、预算超界或接口无法延迟 commit 时，回退固定 block、原 confidence/schedule 或自回归路径。

“并行解码”不能由模型名称或一次 forward 更新的位置数推断。对 masked diffusion LM，应从 sampler 的实际 accept events 重建 token 何时进入不可再改状态；同一步若同时接受多个位置，这些 token 之间可能只有 block-level 偏序，而不存在可解释的逐 token 生成顺序。于是 sampler revision、accept rule、commit granularity 与可见输出顺序都属于 generation artifact；把观测 block size 当成模型固有因果顺序，会给缓存、流式输出和审计制造虚假依赖。

这种追踪增加事件记录和分析成本，且单一 checkpoint、sampler 与有限任务上的 commit 行为不能代表整个 diffusion family。若下游严格依赖全序、输出具有不可逆副作用或 sampler 无法暴露 accept event，应延迟外部提交或回退自回归路径。

<!-- semantic-body-binding:SF-2026-ARXIV-2606-14620 -->

Commit记录还必须区分“模型按schedule接受的token”与“外部组件写入的token”。在可暴露中间状态的masked diffusion runtime里，仅有早期refusal或高confidence不足以保证后续路径仍受同一安全条件约束：受限干预实验中，重新mask已接受区域再写入短肯定prefix，能够改变后续生成；但只remask或只写prefix均未取得同样结果，不能简化成“任意编辑都会绕过安全”。这是状态修改权与commit provenance的具体边界，而非黑盒普通用户自动拥有的攻击能力。

因此，generation owner应把允许的repair与不可信状态改写分开，并记录accept event、修改来源与可见输出边界。只检查mask数量不增加，能检测该实验的remask路径，却挡不住不改mask的logit干预，也不能替代输入/输出安全检查；若用重mask作审计，应把诊断forward与真实状态writeback隔离。两种7B/8B模型、固定greedy/linear schedule和单judge的受控结果不证明整个diffusion范式普遍不安全，更不证明作者提出的防御已被验证。第72章继续拥有权限与安全gate；本章只说明可修订生成路径需要怎样的状态边界。<!-- source-family:SF-2026-ARXIV-2604-08557 -->

接受规则还有一条介于单步 confidence 与严格 block 顺序之间的历史分支。只允许当前 block 解码最容易维护依赖；未来 block 的分布可能已稳定时，可以把当前预测分布作为 anchor，与该位置最近若干步的预测分布计算衰减加权 KL，再按一致性阈值提前解除 mask。这与只比较相邻两步不同，新增的状态是逐位置历史分布、anchor 和阈值，而不是凭高 confidence 自动跨 block commit。

历史一致只能说明近期分布接近，不证明答案正确或下一步永不改变；较短 history 或过宽阈值会过早接受，过严阈值则继续支付等待，缓存和 KL 计算也增加成本。[AHD 的受限实验](https://arxiv.org/html/2604.08964v1)及 bounded-embedding 分析支持这一选择分支，不证明生成质量或外部副作用安全；受测模型/任务中的 step 减少更不能直接当任意服务延迟收益。短 history 无法可靠判断、分布漂移或下游依赖固定 block 顺序时，原 block schedule 与延迟外部提交仍是合理回退。<!-- source-family:SF-2026-ARXIV-2604-08964 -->

### 并行与少步生成必须声明依赖、轨迹和状态边界

讨论一步生成之前，还要区分训练样本的插值路径与采样ODE的轨迹。把独立噪声样本和数据样本作直线插值，并不使条件平均速度产生的flow map自动成为直线；在相应正则与矩条件下，普通affine插值要产生精确直流，需要确定性端点coupling，而不是随机独立配对。充分方向还要求该transport的Jacobian满足相应半正定条件，不能将任意确定性coupling称为充分。若流的全加速度确实为零，一次初始速度评价可精确积分；训练出来的近似velocity却仍有估计误差，这不是“训练路径直，所以一NFE无损”的保证。

独立端点也不一概阻止精确直流：非退化Gaussian端点可以加入协方差专门匹配的独立Gaussian辅助噪声，构造零全加速度的条件流；但相同的两段分离uniform混合，在独立端点、连续样本路径和时间上一致Lipschitz速度等条件下已有不可能例子。[存在性与障碍分析](https://arxiv.org/html/2604.15439v1)因此限定的是某类过程的结构可行性，不是所有多峰目标、所有神经生成器或任意维少步算法均不可行。改变coupling、增加前置transport估计或保留弯曲轨迹的多步solver，会改变计算与误差分工；不能确认所用过程满足这些条件时，应保留经验质量—NFE验收与原solver回退，不以定理替代实际训练和部署验证。<!-- source-family:SF-2026-ARXIV-2604-15439 -->

少步蒸馏还要区分“每一步分布匹配”与“多步组合一致”。各噪声水平的局部输出都接近 teacher，仍可能在连续应用更新时漂移；一条条件分支在分布匹配之外，约束直接一步与经过中间时刻的两步更新接近同一终点。它是 learned flow map 的近似组合正则，不是数学上的精确半群保证，也不应把回归一致性单独当作生成质量目标。

训练时提供更密的 teacher 状态，也不要求部署时输出所有中间状态。若终点监督太稀疏，一条辅助分支可将原输出头扩为 K 个并行通道，共享 backbone，同时拟合 teacher 区间内选定的状态；把原终点权重复制到各通道后，用加权辅助损失训练，推理只交付最后一个通道。这里增加的是训练读出和监督密度，不是让 student 真正沿连续轨迹求解 K 次，也不把拟合有限状态视为 PFODE 的精确积分证书。[有限图像蒸馏实验](https://arxiv.org/html/2602.15971v1)的少步配置有局部收益，但 ImageNet 的三步及以上结果反而退化；CIFAR 的 Optuna 权重搜索再迁移到 ImageNet，也不是同一端到端搜索预算的比较。额外 teacher 状态存储、输出头、反传与权重调参均要计入成本，报告的训练时间和 FID 不认证生产延迟或 SLO。部署只保留终点头是这条分支的接口选择，不自动保证辅助状态可组合；质量或训练预算不合适时，仍可保留终点监督、减少辅助通道或增加原 solver 步数。<!-- source-family:SF-2026-ARXIV-2602-15971 -->

连续 one-hot 文本还要选择与解码相符的时钟：若 argmax 解码的信息主要在末段出现，按 one-hot decoding error 的下降重参数化训练与采样时间，可以把预算移到真正改变 token 决策的区间；这不是图像 log-SNR 的机械复用。一条受限少步分支先冻结 flow language model，以 learned Euler-step correction 学习 average-velocity 的组合接口，再把 teacher 与校正压缩到一个 flow-map 模型；两阶段区分原瞬时场、校正与交付 map，而不是从独立端点的线性插值推出一步精确。组合损失仍只是近似正则；[170M文本实验](https://arxiv.org/html/2602.16813v1)中 Euler校正/MSE 优于 logit-denoiser校正/CE，但 GenPPL 较低也可能伴随 entropy 塌缩，更多步数并非每个质量指标都改善。全文词表反传增加约30%的训练时间/显存，第一阶段的双模型和后续压缩训练也需计入；LM1B/OWT的有限生成指标不认证通用能力或生产SLO。时间坐标、质量/多样性或训练预算不成立时，原多步 solver、离散 diffusion 或 AR 路线仍合理。<!-- source-family:SF-2026-ARXIV-2602-16813 -->

组合约束还可以显式覆盖不同子轨迹接口：以 t→1 的终点 map 学一致性，以起止时刻重合的 diagonal query 学 instantaneous velocity，再以 0→t 的 noise-to-intermediate map 学习进入中间 noisy state。增加右端时间条件与 teacher/JVP 目标，使同一参数化在终点、局部和起点边界承担不同监督；采样可先用 Euler 启动一段，再切换 consistency map，不等于每步重新注入独立噪声，也不同于仅把 coarse action 再去噪。<!-- source-family:SF-2026-ARXIV-2602-10764 -->

三种接口增加训练目标、时间条件和 JVP 成本，并不把近似 map 变成精确可组合的 solver。[受限双端训练实验](https://arxiv.org/html/2602.10764v1)的匹配消融支持 noise-to-intermediate 分工与混合采样，但移除 velocity normalization 的两步结果反而略好，不能称每个组件逐点必要；原文部分平方拆分和算法记号也不足以背书完整公式无误。JVP 与所述 FSDP/FlashAttention 路径不兼容及较高显存限制规模；接口失配、质量或训练成本越界时，保留普通 consistency、instantaneous 多步 solver 或原蒸馏路径，以实际质量—预算验收而不是少步名称决定部署。

外层去噪步数也不必等于每次都完整运行同一深网络的次数。一个视频蒸馏分支在每个外 denoising transition 运行一次 backbone，再固定该外步 features，由较轻的 conditional flow head 从噪声开始多次修正 transition target；下一外步仍重新计算 backbone，不是跨步无限复用缓存。训练先用 transition/MeanFlow 目标初始化 head，再以 distribution distillation 展开全部 inner steps 反传；主干不冻结或 detach，内层也不是 AR 历史生成。新增控制变量是外步 M、内步 N 和 head 深度 H 的预算分工，不认证 teacher 轨迹或分布精确保持。<!-- source-family:SF-2026-ARXIV-2601-09881 -->

这用 head 重复求值、两阶段训练、fake score 和 discriminator 换取较细的质量—计算取舍。TMD 的 effective NFE 按执行 DiT blocks 归一，不包含完整 pipeline 的墙钟、VAE 或服务成本；Wan2.1 的受限实验中，14B 两外步配置并未超过两步基线，单步收益不能外推所有预算。KD warmup 对单步有益却可损害两步，concat 融合也有收敛不稳，说明初始化、融合与步长仍需共同验收。质量退化、训练预算过高或 inner-loop 收益不足时，应保留原多步 solver、增加完整 backbone 求值或固定 student；不能从 fractional NFE 宣称生产吞吐或 SLO。[必要接口与反侧](https://arxiv.org/html/2601.09881v1)见 Algorithm1–2、§3–4 和 Appendix A/B。

少步生成也可只改变 continuous head，而不重新训练条件历史。一个 streaming gesture 分支由 AR backbone 管理 causal history，每个 token 的 flow head 生成连续 motion latent，再交给 VAE decoder；冻结 AR 与 VAE 后，可在缓存的条件上只蒸馏 head。ODE teacher 提供 warmup 目标，distribution matching 的辅助 head 提供后续训练信号。这分开了条件状态更新与连续采样预算，而不是把离散 token 改名成连续量就消除了表达和误差问题。

one-NFE 只计该 head，不包含 AR、decoder、buffer 与条件缓存成本。训练缓存的条件与部署自产生的 motion history 可能失配，须另验 streaming 累积误差及端到端延迟；BEAT2 的受限主 speaker 结果不认证任意角色、时长或实时 SLO，FGD 两表的尺度冲突也不拼接为同一质量点。缓存身份或生成质量不成立时，应刷新条件、增加 head 求值或保留原多步 sampler；较轻 head 不自动获得整个 pipeline 的质量与时延保证。 [必要机制与反证](https://arxiv.org/html/2609.21576v1)。<!-- source-family:SF-2026-ARXIV-2609-21576 -->

少步 action 生成还有一条不同的采样分工：共享网络既学习完整区间的 average velocity，也通过起止时间相同的 diagonal query 学习 instantaneous velocity。先以全局平均场从初始噪声跳到 coarse action，再混入初始噪声（或独立新噪声），以局部 diagonal 场完成修正；两次评价承担不同尺度的误差，而非单纯重复同一 solver。若 re-noise 写为 `alpha*eta+(1-alpha)*coarse`，旧误差被缩小只说明这一步的代数作用，不证明新状态分布等于训练 marginal，也不能从固定区间传播界推出 NFE 越多误差必然指数增长。

[受限双场采样实验](https://arxiv.org/html/2602.13718v2)在同 MeanFlow checkpoint、RoboMimic 每任务100 episodes 下，plain 1/2/4/16 NFE 为78/78/72/60，去掉 re-noise 的配置为24，完整分支约95/95.5，支持这套 global/local 分工而非任意增加步数。重置噪声、双 query 训练与额外局部评价都要付费；Thor 实机共享300 demonstrations、encoder/controller/backbone 的比较仍未完全拆开精度与决策等待的因果影响，19ms动作推理排除了约95ms camera，WM得分也不是成功率，Transport任务还低于两个多步基线。无法保持噪声/时间条件、任务漂移或质量收益不足时，应回退已验证的多步 solver；动作是否安全提交仍由第26章负责。<!-- source-family:SF-2026-ARXIV-2602-13718 -->

AR 视频又把误差带入下一 chunk 的 KV：低步数生成的历史与同一 generator 更密步数的自产生 reference 历史，不是同一 conditioning distribution。训练时混合不同步数的自产生 rollout，并将弱历史条件下的输出关系特征对齐到更密步数的 reference，可以同时覆盖 cache 质量变化和组合误差。代价是额外 rollout、reference 与正则计算，过强一致性也可能压低运动变化。[Salt 的受限实验](https://arxiv.org/html/2604.03118v1#S3)覆盖 Wan 2.1 与 Self Forcing 等视频路线，使用私有 I2V 数据；所测短/长视频指标不证明任意时长稳定、真实 serving SLO 或 cache 成为环境真值。质量退化时增加采样步数、缩短生成 horizon 或恢复原训练配方仍合理。

自产历史与reference的耦合还可以双向训练：共享权重的few-step路径先产生历史，multi-step路径在该历史条件下学习当前真实flow，再以stop-gradient区间位移反教few-step路径。部署仍只运行few-step，但reference已适应部署历史，而不是始终消费另一种teacher-forced历史；history producer、reference与梯度边界必须分别声明。

共享权重不等于训练只有一个模型或没有辅助成本，online fake-score分支、rollout与多步reference都要另计。有限Mutual Forcing消融支持这条耦合，同预算SC/DMD混合目标消融不隔离整个双向loop，也不证明训练全成本匹配，个别同步/语音质量也有反退，更不支持无限视频稳定。耦合失稳或质量收益不覆盖训练成本时，普通teacher forcing、独立蒸馏和已验证的self-forcing配方继续成立。 [原文必要机制与限制](https://arxiv.org/html/2604.25819v1)。
<!-- source-family:SF-2026-ARXIV-2604-25819 -->

训练匹配有误差的历史，还要区分**历史写入质量**与**实际读取集合**。一条原生稀疏 AR 视频分支保留完全去噪的历史为 persistent anchors，local 窗口承载近邻和当前去噪；退出 local 的候选先由 coarse pooling 提名，再在有限 anchor/sink 预算内选择。读取时 persistent 与 local Top-K 进入同一 masked softmax，训练阶段就用这套动态 cache/mask，而非密集训练后才裁去旧历史。pool summary 只有提名权，被丢掉的细节不会因摘要存在而无限可恢复。<!-- source-family:SF-2026-ARXIV-2604-21221 -->

这把有限活跃读取预算变成模型训练责任，却增加 anchor 维护、选择、反向传播和部署 mask 一致性的成本。[受限 Sparse Forcing 对照](https://arxiv.org/html/2604.21221v1)中，移除 persistent 状态可更快却损害质量，短片也有退步切片；Wan 1.3B、有限 20/60 秒生成与 kernel 测量不证明无限长稳定性或完整服务 SLO。动态选择漂移、关键细节丢失时应提高历史预算，必要时回退 full-history/dense 或重新训练；第 49 章再验收具体稀疏 kernel 和 KV 物理驻留，本章只拥有生成训练与状态读取语义。

沿去噪时间的缓存也可从“直接复用旧feature”改成“根据近期feature预测下一次中间计算”。一条学习分支按noise阶段分配predictor与history窗口，用history投影和timestep调制形成残差；先以完整base轨迹监督，再混入predictor自身历史训练，使训练输入覆盖部署预测误差。这与沿chunk复用、KV写入纪律不同：得到的仍是当前block计算的近似值，不是已验证环境状态，时间网格、history来源、stage边界与predictor revision须共同保存。<!-- source-family:SF-2026-ARXIV-2602-20497 -->

[有限生成对照](https://arxiv.org/html/2602.20497v1#S4.SS3)中，小跳步时stage拆分的增益很小，扩大预测跨度仍损害保真；更少FLOPs也不等同比例wall-clock改善，另有轨迹采集、预测器训练、历史驻留与刷新费用。质量proxy、参考一致性和在线成本须分别验收，不把短prompt池中的缓存收益签成泛生成保证。采样网格/条件漂移、历史误差或净费用不合适时缩短预测跨度、刷新完整feature或回退全算/已校准复用，保留原chunk及精确KV提交分支。

训练让模型适应有误差的历史之后，推理加速仍要守住写入历史的边界。常见的 DiT 缓存复用相邻去噪步的 block 输出；当每个视频 chunk 只做少数去噪步，步间差异可能太大。这时可改沿相邻 **chunk** 在相同 `(denoising step, block)` 位置复用 residual，并让当前结构与 action 条件共同决定是否重算。复用的是中间计算的近似值，不是已经提交的环境状态；每个 chunk 最终写入持久 KV 的 clean forward 仍须完整计算，以免近似误差成为下个 chunk 的历史条件。<!-- source-family:SF-2026-ARXIV-2604-20289 -->

这条分支以额外 residual/fingerprint 状态和门控计算换取少步生成中的 DiT 工作量，却继承运动突变、长期漂移、动作条件漏检和错误复用的风险。一个受限单模型、短时七相机实验显示：若连 KV 更新也近似计算，画面与全算基线的差异显著扩大；它不提供真实控制安全或更长 horizon 的证明，论文中关于该消融 skip-rate 方向的表文也不一致。分布漂移、行动急变、状态身份不匹配或保真优先时，应强制重算相关 block、缩短复用跨度或退回全算。第 25 章继续负责 action-conditioned 世界状态，第 26 章负责物理动作的安全提交；本章只拥有生成计算缓存与 KV 写入纪律。

<!-- source-family:SF-2026-ARXIV-2604-03118 -->

组合一致性还会改变监督量的合法替换。普通flow matching中，conditional velocity在给定当前状态后的期望等于marginal velocity；这支持单点平方回归，却不意味着把它代入整条轨迹的**全导数平方**后仍是同一目标。展开后还会出现由模型Jacobian和conditional covariance共同决定的项，参数相关，不能简单叫作不影响优化的常数。这是目标函数变化引入的约束，不是conditional flow matching普遍错误。

当少步输出已经偏离真实轨迹，仅改善局部一致性未必消除这部分分布误差。一条受限整流分支保留模型 diagonal-time 的 velocity 作为真实数据 marginal 的估计器，同时用辅助模型学习“由当前 generator 自产 clean sample、再重加噪”得到的 fake marginal；两者在同一噪声状态上给出差额，再经 stop-gradient 反馈少步生成器。两个估计器分别对应真实数据与自产分布，不能把 fake-estimator 当固定 teacher，也不能把这一附加反馈误写成全部替代 conditional FM 监督。

这增加辅助模型训练、自产样本和额外 velocity 计算，估计误差仍会传入整流目标。[FlowConsist 的必要方法与反侧](https://arxiv.org/html/2602.06346v1)支持上述角色分工，但原 KL 推导有梯度记号歧义，残差的轨迹积分也不证明误差范数单调，所以这里不授 exact-KL 下降或必然消除轨迹 drift。作者有限图像实验按 CFG 搜索最佳质量，整流后较高 CFG 还可能降低多样性、使 FID 退步；训练初始化、辅助成本、采样步数与 CFG 工作点须一起比较。估计器失准、多样性下降或总预算不合算时，保留原 FM 目标、较多步 solver 与已验证的一致性配方，不由单个最佳 FID 决定替换。<!-- source-family:SF-2026-ARXIV-2602-06346 -->

另一个容易混淆的对象是训练 loss 与样本空间的移动方向。以真实样本吸引、生成样本排斥来提出 drift，可以再用 scalar stop-gradient loss 训练生成器；但这不保证该样本空间向量场等于某个固定势函数的梯度。即使未归一化的径向场可积，依赖当前位置的归一化因子也可能破坏 Jacobian 对称性、引入 curl。保留方向或训练 loss 可计算，都不能单独保证“沿同一个全局目标下降”。

这不是说所有 drift 都不保守：Gaussian kernel 有 score identity，匹配核的替代归一化也能恢复相应 log-density-ratio 势；但生成分布随训练改变、目标侧停止梯度时，每轮的场仍会变化。[原始分析](https://arxiv.org/html/2604.06333v1)支持这些具体对象与条件的区分，MNIST/Fashion 小型 pixel-space 实验不证明修正普遍提高完整生成系统。替换归一化会改变稳定性和训练行为，需与质量、多样性和预算配对验收；原有非保守更新若经验目标已通过验收，或普通 score/flow matching 的条件更清楚，仍可保留，不能仅因可写势函数就批准替换。<!-- source-family:SF-2026-ARXIV-2604-06333 -->

一条有条件的少步训练分支用模型自身marginal velocity构造shortcut，同时保留FM分量维护该估计器。[SnapFlow](https://arxiv.org/html/2604.05656v1)用两步Euler目标避免显式求昂贵全导数，但它仍是数值近似，不是精确flow map；模型预测偏差也会进入自产生目标。额外teacher/shortcut计算和目标混合换少步能力，质量回归时须保留多步solver与原FM训练。其冻结VLM、单A800、30k步与LIBERO重复初态的证据不能推成真实机器人安全或端到端闭环等倍加速；第26章消费动作/环境结果，不重述本节训练目标。<!-- source-family:SF-2026-ARXIV-2604-05656 -->

<!-- semantic-body-binding:SF-2026-ARXIV-2605-20187:start -->
固定数量地同时提交 masked positions，默认这些变量之间的依赖足够弱；这在规则任务中简单，却会把强相关位置
过早冻结。一个受限分支从 hidden states 一次估计 pairwise conditional mutual information，构造依赖图，再只
并行提交相互影响较小的变量。它用额外估计器和图调度换取更有依据的并行度，但 MI 误差、图阈值和未建模高阶
依赖会造成错误 commit。Sudoku 与蛋白任务只证明作者设置；依赖估计或一致性检查失败时，应回退更小 block、
更多 refinement step 或逐位置提交。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-20187:end -->

<!-- semantic-body-binding:SF-2026-ARXIV-2605-20199:start -->
连续 diffusion language model 的弯曲轨迹需要较多 function evaluations；flow-matching 微调可以把现有路径拉直，
让 sampler 用更少步接近同一终点。这里改变的是 trajectory geometry 和 solver budget，不是免费减少计算：额外
训练、直线路径的近似误差与任务分布漂移都要计入。比较必须同时冻结训练预算、NFE、解码器和质量指标；作者的
question generation、simplification 与 paraphrase 结果不支持通用文本生成。少步质量退化时应回退原 solver 或
增加 NFE。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-20199:end -->

<!-- semantic-body-binding:SF-2026-ARXIV-2605-20235:start -->
score singularity 提供另一种两阶段解释：先沿强法向分量把高维样本压向低维 manifold，再沿流形细化密度；在
给定正则与几何假设下，样本复杂度可以由 intrinsic dimension 而不是 ambient dimension 主导。收益是把生成难度
拆成 reach-manifold 与 model-on-manifold，代价是奇异 score、数值刚性和 manifold 假设都进入 solver contract。
Stacked-MNIST、CelebA 变体与分子实验不能证明真实多模态分布满足这些假设；假设或积分稳定性不成立时，应回退
常规 score model、显式正则与经验 solver validation。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-20235:end -->

把 guidance 沿估计切向移动，也不意味着有限步仍留在高密度区域：切向位移会经曲率产生二阶法向偏离。一条保留 host prior 的分支把 guidance 拆为法向与切向，按法向的一阶长度和切向的曲率二阶预算共同选步幅，例如用 `r_N + K r_T²/2 ≤ R` 限制允许的 departure；两部分不能靠方向相反就抵消。这个几何预算依赖正则 level set、有效 tubular neighborhood 与受控高阶导数，余项也须保留，不是任意 learned score 下的流形保持定理。共享标量 dual 选择两个方向的幅度，再以实际目标的 Armijo 检查接受步长，几何提案与目标下降是两道验收。

score/Jacobian 只是未知几何的估计；周期性检查后重用 scale，不给中间每一步重新签发 acceptance。局部消融中 Armijo 本身已有明显收益，完整方法更好，但不能把全部收益归给几何投影；Jacobian、curvature 与 line-search 增加内存和时间，改用较少步数的快配置也不等于相同步预算免费改进。图像重建及固定 prompt/seed 的 CFG 对照不证明 exact posterior、语义保证或无限轨迹安全。估计失配、线搜索失败或成本不合算时，应回到 host solver、小步 guidance 或更频繁的实际目标验收，而不让上次接受的尺度越过状态变化继续生效。 [必要机制与反证](https://arxiv.org/html/2609.21251v1)。<!-- source-family:SF-2026-ARXIV-2609-21251 -->

<!-- semantic-body-binding:SF-2026-ARXIV-2605-20547:start -->
当目标从静态 marginal 扩展到 time-dependent latent process，训练对象还要声明“匹配哪个状态转移”。
Generator matching 通过 pushforward generator 定义 conditional objective，并在给定 regularity 条件下证明它与
marginal objective 具有相同参数梯度。它提供的是目标等价的理论接口，不是生产实现或任意过程的稳定性保证；
正则条件、链式 rotational generator 或数值实现无法验证时，应回退已知的固定端点 flow/diffusion objective。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-20547:end -->

语音识别消费扩散语言模型时，还须选择它提供的是整句排序还是逐位置分布。对 CTC 的 n-best 候选，masked diffusion 可以用多次扰动后的重建分数作重排；互补 masks 让每个 token 在一对 forward 中都贡献分数，但这些归一化 pseudo-scores 不是精确整句联合 likelihood。若 uniform-state diffusion 在每轮为所有位置给出完整词表分布，则可以用 CTC greedy collapse 后每个 token 对应的首帧、在 non-blank 词表上重归一的声学分布，与该位置的语言分布做 log-linear 融合，再采样下一轮状态。<!-- source-family:SF-2026-ARXIV-2604-14001 -->

两种接口的状态对象不同，不能把重排分数直接塞进位置解码，也不能将首帧对齐启发式和插值权重当作精确 posterior。CTC 对齐、词表、噪声起点、Monte Carlo/denoising 次数共同进入消费合同，额外 forward 与候选预算须计成本。作者的 LibriSpeech、有限模型规模与词表实验中，AR joint decoding 仍更强，不证明普遍低延迟或所有识别任务获益；接口不兼容、预算不足或质量退步时，CTC、AR 融合与只做受限 n-best 重排仍是共存分支，输入声学表示的身份继续由第23章负责。

解码消费合同之外，同一个语音识别模型若要兼顾离线全上下文和流式短右视野，训练时还得决定**让哪一个输出对象在两种可见条件下保持一致**。只在辅助 CTC head 对齐 frame-synchronous posterior，不能替最终 Transducer 的预测负责；受测实验里，这种一致性甚至损害流式 RNNT。一条受限替代分支让同一输入分别通过离线和 chunk-limited 编码，在有效的 `(t,u)` lattice 位置对完整 RNNT 词表分布施加一致性约束。它把跨模式监督放在实际解码分布上，而不是把 CTC 辅助目标当成可互换代理。<!-- source-family:SF-2026-ARXIV-2604-19079 -->

这仍需两种模式前向和 RNNT 训练；现场计算 log-softmax/KL、反向重算只是减少完整 joint 张量物化，不使监督免费。chunk、右上下文和左侧重算共同决定理论等待与真实执行成本，极短右视野下质量仍可退步。作者的受限 FastConformer/英语数据、32 A100 训练与 greedy batch-128 结果支持这一监督对象选择；`C+R` 是理论 latency，不是在线 tail SLO，XL 数据量的表格与正文口径也不能合成一个受控预算。目标分布或成本不合适时，保留独立离线/流式模型、single-mode 训练或辅助 CTC 的原用途，不把“模式一致”升级为普遍最优解。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-20946:start -->
语音生成还可把 speech token 与内部 reasoning token 交错到同一训练序列，使模型在发声单元之间保留可学习的
中间状态。它改变 token type、时间戳、可见性和 commit cadence，却不证明内部 reasoning 等于事实正确或可解释
因果；隐藏 token 泄漏、音频延迟和状态错位会成为新失败面。作者任务与模型之外，应保留不暴露中间状态的普通
speech generation，并让外部 verifier 而非 reasoning token 拥有正确性判断。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-20946:end -->

发声的提交节奏还受波形渲染器影响，不能只看语言模型是否逐 token 输出。旧的 chunk renderer 等待有限右侧上下文，可以改善局部声学连续性，本来就能逐块流式输出；另一条分支让 Talker 沿时间轴自回归地产生当前帧的主码，再用固定步数的轻量自回归模块补齐**同一帧**的残余 codebooks，交给只读左侧上下文的 Code2Wav。Qwen3-Omni 的公开架构及具名技术报告支持这一区分：MTP 在这里补的是帧内码层，不是独立并行生成未来多个时间帧；改变的是首帧进入波形合成前的 block-context 等待，而非取消时间依赖。<!-- source-family:SF-2025-QWEN3-OMNI -->

这种分工仍要支付主码生成、残余预测、波形解码及跨模块 buffer 的费用；降低稳态生成时间不保证首包或高并发延迟不变。其技术报告把首包各阶段相加，并显示并发增加时首包明显变长，不能用 RTF 小于1替代端到端 SLO；也没有同模型、同训练预算的 renderer 单因素对照来证明所有收益都来自因果 ConvNet。码本与 decoder 不匹配、声学质量退步或资源预算不足时，保留 chunk/lookahead 或专用 TTS 的旧分支仍合理。已播放的音频不能靠后续重写回滚，因此表示层的时间位置和码本身份之外，生成层还必须管理缓冲、取消与实际播放边界。<!-- source-family:SF-2025-QWEN3-OMNI -->

交错生成还须问清两种可见输出能否按同一节奏前进。文本 token 与语音 codec token 的编码率不同；固定交错步长或等待强制对齐，会让某一通道被另一通道拖住。一个条件分支把 text 与 speech 放进同一生成序列，并对已生成 prefix 限制累计 speech/text token 比不超过该样本的全局比例，使文本可以先给出可解释前缀，后续语音再跟进。它处理的是输出单位的单调次序，不把逐词文字与声学帧变成精确一一对应；具体比例若依赖完整样本统计，在线未知终点时仍须声明估计或回退，不能凭训练约束直接宣称生产硬保证。

单流布局可减少两条生成轨之间的同步状态，却把 codec、type delimiter、prefix 缓冲、取消与回退放进同一提交合同。受限 [Qwen3.5-Omni exact-v1](https://arxiv.org/html/2604.15804v1) 的 ARIA 采用这样的 prefix-rate 约束，Talker 仍以 RVQ/MTP 与因果 codec 生成波形；Table2 仅给内部 vLLM/compile/CUDA Graph 设置下的 theoretical first-packet latency，且 8 并发时视频首包明显变长。它未单独消融 ARIA，也没有证明在线全局比率已可知、任意语言都低延迟或真实 tail SLO；比率失配、对齐质量不稳或跨模态回退复杂时，固定 chunk / 双 track 的旧分支仍合理。Thinker 与 Talker 的状态交接依然是后文独立的部署问题。<!-- source-family:SF-2026-ARXIV-2604-15804 -->

输出节奏之外，交错生成还可以为不同 token 类型选择不同执行深度，而不改变 codec 的时间层级。一个有损替代分支让文本保持完整 Transformer 深度，语音位置按固定周期在浅层输出与完整执行之间交替；冻结基座后用完整模型的输出分布训练浅层 prediction head，再以独立质量切片选择退出层。teacher history 上浅层 codec token 不同却有相近感知代理，只提供可试的线索，不证明这些 token 回馈后仍稳定。[必要方法](https://arxiv.org/html/2603.09215v1#S4.SS2)还要在后续完整步骤补算早退位置缺失的深层 KV；周期执行不会把先前已发出的 token 改成完整模型采样，也不继承第48章 target verification 的分布保证。<!-- source-family:SF-2026-ARXIV-2603-09215 -->

这用训练与保存额外 head、选择周期及补算 cache，换取发出部分语音 token 时较浅的路径。[有限对照](https://arxiv.org/html/2603.09215v1#S5)中，固定浅层自回馈和部分 entropy 策略会退化，但某个 confidence 配置仍保留更高语义分数；周期方案也有任务退步，预测 MOS 接近不代表答案正确。平均退出层降低只统计 token 发出的深度，不等包括 KV 补算、语音渲染与排队的 FLOPs 或墙钟加速。head、codec、退出层与周期应共同定义生成身份，并分别验收文本语义、speech–text 对齐、音质和完整成本；误差积累、状态回填或质量预算不成立时，保留全深度生成、经校准的 confidence 分支或独立 speech decoder，不把同一 shallow policy 直接用于文本。<!-- source-family:SF-2026-ARXIV-2603-09215 -->

若任务只需生成语音，另一种粗细分解也不能与 RVQ 的 residual codebook 层级混同。残差 codebook 是同一时间位置上由粗量化到细量化；时间分辨率链先把首个 acoustic codebook 的 token 序列降采样，生成较稀的节奏骨架，再逐级提高 token rate 并在每级做 masked refinement。后一级同时读取前一级结果、文本和说话人条件；共享 decoder 节省参数，却不消除每级迭代、跨级错误传播或条件状态的版本责任。训练时扰动前级 token，只能提高受测扰动下的鲁棒性，不能保证粗节奏错误总能被细级修好。<!-- source-family:SF-2026-ARXIV-2604-19330 -->

这条时间链把一部分局部音素规划移给粗 token，并没有取消总时长估计：作者实际仍用 G2P 与 duration predictor 确定 utterance length，再据此分配各级 mask 序列。一级或独立 semantic→acoustic 的旧路径在短音频、成本敏感或跨级条件不稳时仍合理。作者的有限英文语音实验中，增加时间层级改善部分 WER，但 SeedTTS 大模型切片仍有退步；共享参数量不等总计算、自然度或 streaming SLO 优势，硬件、precision 与真实首包延迟未形成可外推合同。

固定视频时窗又增加一项不同的约束：总语义正确不代表生成语音能在给定片段内自然说完。先翻译、再统一加速或减速，在宽松时窗和小幅偏差下简单合理；目标语言的音节率、句长和停顿改变后，后处理可能损害自然度，却无法修复内容分配。另一条设计分支在内容生成阶段就提供目标时长与语言相关的音节率提示，按句子或自然停顿分块，并保留周边语境，使语义与时长共同影响输出，而非只在最终波形上补救。这些提示是规划代理，最终是否落窗仍须由实际语音渲染结果验收。

两项质量目标也未必总能兼得。字幕翻译可以优先语义完整，配音则可能在语义底线之上接受更紧凑表达，以满足同步窗口；不能用一个综合分数隐藏这样的工作负载分支。分块与重试增加对齐、上下文传递和质量审核成本，过短窗口、邻块指代断裂、语速预测失准仍会失败，必要时应改写、重分块或保留人工/后处理路径。公开应用案例只支持这条联合约束设计的可行性线索，没有受控消融来分离模型、提示和工作流收益，也不证明任意语言或实时 SLO；具体训练与生成内部机制未披露。<!-- source-family:SF-2026-OPENAI-DESCRIPT-20260306 -->

### Few-step Distillation 要在 Student 实际访问的状态上验收

Student 从 teacher 权重初始化，也不意味着 distillation 后继承相同 memorization：新的 objective、teacher trajectory 与 student 更新会重新分配 near-copy 和泛化。应在蒸馏前后分别记录生成质量、样本相似度及来源证据，不用 SSCD 阈值 0.6 或 p95 当 privacy bound；copy/provenance release gate 仍独立。<!-- source-family:SF-2026-ARXIV-2604-23552 -->

蒸馏、重复样本对照与相似度审计增加训练/评价成本，student SSCD 下降不必保持质量：作者 ImageNet 7k FID 20.14→28.65 为反向例。该有限图像实验及简化谱解释不证明隐私或版权安全；质量退化、复制证据不清或新域迁移时，保留 teacher/多步采样并重新验收，不由加速学生自动继承发布许可。

除了验收 student 访问状态，还要区分在同一 noisy state 上提供什么目标。一条受限分支让 few-step teacher 在同一 x_t 给出 velocity 与 feature anchor，再与原 distribution-matching 中 real teacher 的 score、critic 的分布估计共同训练；局部轨迹/特征目标与目标分布目标承担不同责任，前者不会自动证明后者正确，额外锚也可能与分布方向冲突。[K-DMD 的有限对照](https://arxiv.org/html/2601.08303v1)没有 matched DMD-only 控制，不能把全部稳定性或质量收益归为这一个机制；28→4步仍有指标退步。LoRA 切换可共享部分权重，不免额外 teacher forward、feature 驻留或 critic 训练，encoder/decoder 与部署量化也须入端到端账本；手机一次 forward 与 GPU 最大可放 batch 的 FPS 不合成 hard latency/SLO。目标失配、student 状态漂移或总费用不值时，保留原 DMD/一致性路径、更多采样步骤或 teacher，而不以少步数自动继承质量。<!-- source-family:SF-2026-ARXIV-2601-08303 -->

<!-- semantic-body-binding:SF-2026-ARXIV-2605-06376:start -->
#### Continuous Schedule 用 Coverage 换掉固定 Anchor 的盲区

离散 distribution matching 在少量固定时刻对齐，训练和实现都简单；few-step student 实际访问的 off-trajectory state 可能落在 anchor 之间，形成 truncation drift。Continuous-time 分支随机采样轨迹长度，并让 student velocity 在非锚点状态上对齐目标分布，把“覆盖了哪些状态”变成训练合同的一部分，而不是只增加一个更强 loss。

更连续的 coverage 减少固定 anchor 盲区，却提高状态采样、稳定性与校准成本。现有结果只覆盖 SD3-Medium、Longcat-Image、作者 metrics 与 few-step setting，不证明其他 modality、backbone 或生产 latency。off-trajectory state 不可靠或训练发散时，应回退 discrete DMD、consistency distillation 或增加 sampling steps。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-06376:end -->

<!-- semantic-body-binding:SF-2026-ARXIV-2605-07924:start -->
Few-step flow distillation 不一定受 student capacity 限制；若 teacher trajectory 用盲目随机 midpoint 构造，target 本身就可能偏离高质量路径。训练端可让冻结 teacher 生成多个 midpoint candidate，再由仅训练期可见的 energy navigator 选择 target，student runtime 不携带该 navigator。它用额外 teacher/energy compute 换更好的低 NFE trajectory，也会继承 energy bias 并压低 diversity；tau、teacher、energy 与 source distribution 必须进入训练身份，entropy 或任务质量越界时回退普通 DFM trajectory、更多 sampling steps 或统一 distillation。 [受限证据：arXiv:2605.07924v1]
<!-- semantic-body-binding:SF-2026-ARXIV-2605-07924:end -->

训练期选择 target 时，还要区分 reward 评价的是当前 student 的原始输出，还是将写入监督的构造目标。一个 distribution-matching 分支先从 detached student 输出出发，结合固定 real score 与在线 fake score 构造 implicit regression target，再解码该目标并评分，以评分差调节正负更新。这样让分布匹配负责提出更新方向，让 reward instrument 检查拟采用的目标，而不是用早期 raw sample 的低分直接否定目标；被评分的目标仍不等于最终生成质量的独立真值。<!-- source-family:SF-2026-ARXIV-2604-19009 -->

这一路径用 fake estimator、VAE 解码、target grouping 与额外 reward 调用换取更具体的监督选择，也继承 reward bias、估计器漂移和可解码支持的限制。作者受测 SDXL/SD3 设置并非所有质量指标都胜出，少步 NFE 也不能替代总训练成本或生产延迟。目标偏离支持、质量或多样性回归时，原 distribution matching、普通 reward 后训练与更多步采样仍应并列比较；不能由局部目标评分推断所有梯度冲突已消除。

少步学生的画面质量已可接受时，统一重加噪与均匀critic拟合仍是简单基线；但学生近静止状态上的弱重加噪可能使teacher后验仍靠近静止模式，强运动样本又可能更难被fake-score拟合。可把两条训练压力分开：用当前rollout与paired目标的时间变化亲和度调节base schedule和teacher-specific方向转折prior的混合，再按同noise-bin的预测logFM残差，把mean-one、停止梯度的权重分配给critic loss。前者改变teacher看见的状态，后者只改变已有critic更新内的拟合份额，不改其回归target；评估交互fidelity的表示与预测拟合困难的表示不必相同。

[受限视频蒸馏对照](https://arxiv.org/html/2609.31349v1)把采样和critic重权分别删除，支持这套分工，但方向转折只在exact-flow正则条件下关联posterior变化，不是真实运动证书。亲和度、预测器或归一化未定义时应回退base/uniform；更强noise会伤外观，过强困难权重会伤典型样本。Teacher profiling、paired feature与在线MLP仍有训练费用；相同步数不等总算力，两个planning任务的平均提高主要来自一项，physics评分还可偏好静止输出。换teacher/schedule或超出已测interaction时重估profile、分别验运动/外观与总成本，保留原DMD或更多采样步，物理提交仍由controller负责。<!-- source-family:SF-2026-ARXIV-2609-31349 -->

<!-- semantic-body-binding:SF-2026-ARXIV-2605-09536:start -->
统一 trajectory distillation 把所有时间间隔视为同一种误差，在 denoising dynamics 平稳时简单；但相邻时刻的局部变化与跨越较远时刻的全局变化可能需要不同监督。Temporal-aware 分支从冻结 teacher trajectory 中构造 privileged targets，再按时间距离分配蒸馏目标；训练 artifact 保存 teacher、trajectory 和时间策略，runtime 只选择已经通过质量—速度验收的 operating mode。

更少采样步数是以 teacher rollout、轨迹偏差和额外训练成本换来的，远近状态划分错误还可能同时伤害速度和质量。现有证据仅覆盖作者模型、数据、实现与 evaluator，不证明跨任务、硬件、长度或生产尾延迟的普遍收益。Student 轨迹离开校准区域、diversity 下降或目标任务改变时，应回退原始 diffusion steps 或统一 distillation。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-09536:end -->

把多个 teacher step 压成一个 student transition 时，离线 teacher trajectory 是合理起点，但 student 的早期并行提交会改变后续 context，使真实状态逐步离开监督分布。更稳妥的 on-policy 分支从 student 自己生成的 partial state 出发，由冻结 teacher 提出 outcome-aligned future candidates，并只提交仍保持 rollout outcome 的最长前缀；验证失败就缩短 transition。收益是减少 function evaluations，代价是在线采样、teacher 计算与一致性判定误差；高风险或状态漂移明显时，多步 refinement 仍是正确性基线。`arXiv:2608.02942v1` 只在作者数学和代码 benchmark 上支持该质量—效率前沿。<!-- source-family:SF-2026-ARXIV-2608-02942 -->

另一条离线分支不直接预测最终 clean sample，而让 student 一次提出多个连续 denoising transitions，并拟合 teacher trajectory 的 mean velocity。它把 sequential denoise 改成 multi-step proposal，避免每个被压缩 step 都依赖 JVP 或 finite difference；scheduler 可以选择少量 student evaluations，但仍必须把 proposal 看作有损近似，而不是 exact 跳步。

受限实验在披露的 LTX、Wan 与 Qwen-Image 设置中支持 4–8 NFE 的质量—diversity operating points，却不证明 NFE 等于 wall time、data-free distillation 跨域稳定或 mode collapse 已消失。发布 gate 应联合比较真实 latency、峰值内存、sample diversity、目标质量和失败时回退原始多步 denoiser；分布漂移、diversity 下降或 student 轨迹越界时，多步 teacher sampler 仍是正确 fallback。

<!-- source-family:SF-2026-ARXIV-2607-26004 -->

减少采样步数之外，还可以改变每一步使用的模型容量：在latent、时间参数化和condition接口兼容的大、小模型之间，按离线校准的阶段先用大模型建立结构，中段用小模型，再回大模型修正。这种大—小—大capacity schedule并未自动减少NFE，而是在相同求值次数下交换单步成本与轨迹误差。结构相似度与细节质量观察及同latent上的velocity差只能帮助提出切换区间，不是在线质量oracle，也不保证所有视频质量维度保持；换模型、任务或schedule必须重校准。两套权重驻留、加载和switch均付费，不能由block计算量直接推出端到端SLO；代理失配或质量回归时，保留统一大模型路径或更保守的切换区间。<!-- source-family:SF-2026-ARXIV-2512-24724 -->

#### Any-step Flow Map 把步数变成运行时状态

固定少步 distillation 为某个 step count 优化，部署改变延迟预算时常需另一套 student。Any-step flow-map distillation 学习非相邻时间间的映射，使运行时可按预算选择跳转长度；获得的是可调 latency-quality frontier，代价是跨多种步长训练并维护跳转一致性。<!-- semantic-body-binding:SF-2026-ARXIV-2605-13724 -->

任意步数并不保证任意 schedule 都稳定，长跳转会放大误差。视频 diffusion 的现有证据不外推其他模型或生产尾延迟；质量或一致性越界时，应增加 steps、回退固定 student 或完整 solver。

#### 少步生成的 Diversity Control 可以进入内部表示，但不能绕过质量 Gate

单步或少步 diffusion 丢失了多步 trajectory 中反复注入随机性的接口。受限分支可在 student 实际访问的 activation geometry 中寻找 PCA 方向并施加定向扰动，使 diversity control 从采样时刻移入内部表示。扰动器只拥有候选多样性，生成模型仍拥有输出，独立 evaluator 决定 fidelity 是否可接受。它增加方向校准、存储、层选择和 distribution drift 风险；几何失配或扰动破坏 alignment 时，应关闭该分支并回退原 student、多步 sampler 或外部 best-of-N。exact-v1 只支持作者模型和指标下的 diversity-fidelity Pareto，不证明存在通用 diffusion manifold 或端到端时延优势。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-11494 -->

### Self-revision：并行位置必须在 Commit 前保持可撤销

<!-- semantic-body-binding:SF-2026-ARXIV-2605-25820:start -->
并行解码若只按单 token confidence 选择同一步提交位置，可能把视觉上指向同一区域的冗余 token 一起锁死。一个多模态分支用 token-image attention overlap 构造 Visual Redundancy Index，再优先提交 grounding 互补的位置。这个指标只拥有 selection proposal：attention overlap 不是因果 grounding，也不能证明 token 语义正确。

读取 attention 与组合选择会增加 runtime 和调度开销，信号失配还可能漏掉文本依赖或把关键同区域 token 误判为冗余。此时应回退 confidence top-k、减小并行 K、允许重开，或使用顺序 AR/完整迭代。作者 backbone 与任务范围只支持这一选择策略，不证明它对所有多模态生成都更快或更准。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-25820:end -->

#### 用跨步分布不稳定性分配 Revision Budget

每一步重算所有未提交 token 最容易保持算法对称，却把相同计算花在已经稳定和仍剧烈变化的位置。一个选择性分支比较相邻 denoising step 的 top-K 分布，只重新开放高动态 token，并通过自对比重掩码把计算集中到不稳定区域。Sampler 拥有 refresh proposal，commit policy 仍决定哪些位置不可再改。

Top-K 差异只是稳定性代理，可能漏掉排序不变但概率显著漂移的错误，也会引入阈值和额外状态。短序列、并行硬件充足或 exact trajectory 更重要时，全量 revision 仍是可靠基线；现有 exact-v1 结果只支持作者模型、步数与数据集。<!-- semantic-body-binding:SF-2026-ARXIV-2605-01373 -->

若目的不是重新开放动态位置，而是永久停止稳定位置的计算，状态语义就变成不可逆的分支：对已经预测的位置联合检查 confidence 与跨步 local KL，达到门槛后不再计算其 query 与 FFN，但保留每层缓存的 key/value，供仍活跃的位置继续读取。停止更新不等于移除上下文，也不等于该 token 已被证明正确；缓存会继续影响后续预测，lock 的身份、层和生命周期必须保持一致。<!-- source-family:SF-2026-ARXIV-2602-06412 -->

对固定位置的受限误差界，需要无 remask、未锁定轨迹未来 KL 几何衰减及 logits/log-softmax 平滑等条件；它不是所有活跃位置经 stale KV 反馈后的全网误差或 AR 分布保证。平均 KL 曲线也不能证明逐位置未来 tail，低 local KL 不能自动替代全局耦合条件。[必要证据](https://arxiv.org/html/2602.06412v1)在短序列中有 perplexity 反退，小 batch 短生成又可能因不规则 cache 与 packing 无实际时延收益，少 GEMM 不等于 serving SLO。质量要求更严、未来条件可能改变或 runtime 不划算时，应保留全量重算、允许重开的 revision，或原 sampler；选择永久 lock 时必须接受无法在原路径内修正该位置的代价。

重开已预测位置还面临 context 与验证的冲突：把 seed 的输入重掩码可以检查其原预测，却会同时抽走其他位置 drafting 所需的上下文。一个受限分支为同一步保留两种 attention 视图：其他 query 继续读取前步 seed 的缓存 KV；验证 seed 自身时，再把它的 self-diagonal 恢复为当前 mask 计算出的 KV。这样不必让所有 draft 共同承受一次上下文替换，但必须维护前步 cache 与当前输入的身份和刷新边界；seed 不能连续被选作验证对象，错误或过期 cache 仍会影响其他位置。

对固定 query、固定 off-diagonal KV 的单个 attention row，可以减去旧 diagonal contribution、加入新 contribution并重归一化；这个局部校正精确，不代表跨层表示已做真正 leave-one-out，也不消除经其他位置传回的间接泄漏，更不证明 AR target distribution 的 exact sampling。[原始证据](https://arxiv.org/html/2602.06161v1)的 KV 消融同时取消 cache override 和 diagonal correction，不能据此单独归因其中之一；attention drift 相关性也只是选择代理。验证仍须允许 keep、replace 或 remask，并计入 cache/校正与反复修订成本；cache 失配或质量不稳时，缩小并行提交、全量重算或原 sampler 仍是必要回退。<!-- source-family:SF-2026-ARXIV-2602-06161 -->

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

#### Iterative Generation 允许安全状态被重新 Mask

AR token 一经提交便只能在后续补救，而 masked diffusion 的中间 token 仍是可修改状态。安全 sensor 可以在 denoising step 间对 latent steering，并把高风险或低置信位置重新 mask 后再生成；这把防护从一次输入/输出过滤推进为逐步 proposal-correction loop。<!-- semantic-body-binding:SF-2026-ARXIV-2605-13043 -->

安全 sensor 的误报会造成反复 remask、质量下降或无法终止，漏报则仍会提交有害序列。证据只支持所测模型、攻击和 evaluator；校准漂移或迭代超预算时，应回退独立输入/输出 policy gate，并保留最大重试次数和拒绝路径。

### 生成 Workflow 也可以被训练进 Intermediate State

复杂视觉生成可以从 one-shot prompt→image 演进为 plan→draft→inspect→refine；若 intermediate scene graph、
text plan、draft 与 correction 都进入训练对象，模型学习的是显式 workflow state，而不只是最终像素。它可能提高
约束可诊断性，却引入 plan/pixel inconsistency、self-critic correlation、更多生成步与错误 verbalization。
简单 prompt、强基础 generator 或 latency-sensitive workload 仍应 one-shot。Think in Strokes 的作者结果只支持
其 scene-graph/data contract，不证明 verbal plan 等于可解释因果或跨 modality 通用。

这个 workflow 不一定要由多个部署模型串接。一条统一模型分支把交错的文本诊断、子目标、当前图像与更早图像一起纳入短纠正轨迹训练，再在推理时由同一模型继续文本→图像修订；文本中的内容记忆负责保留原请求和已满足条件，历史图像则提供可回读的生成状态。[UniT 当时官方稿](https://ai.meta.com/research/publications/unit-unified-multimodal-chain-of-thought-test-time-scaling/)的多模型管线用于合成训练数据，不等于部署仍需三个模型；其 nested text/image guidance 也新增控制参数。内部 verification 仍可能幻觉、反复纠正本不存在的问题或让子目标冲突，因此“会写诊断”不授独立真值，基座能力不足也不会因延长链条自动补齐。训练、轨迹筛选和历史图像条件都有成本；低风险、简单请求或严格延迟条件下，single-pass 继续合理。

运行时还须区分模型自行停止与预算强制继续：抑制过早 EOS、追加继续编辑指令并在上限截断，可以让短训练轨迹产生更长修订链，却只改变停止策略，不证明新增轮次必然改善质量。该官方稿以生成图像数比较顺序修订与并行 best-of-N，未匹配 wall-clock，也排除选择器和 verification 费用；“更少图像达到某质量”不能写成等比例端到端加速。顺序路径利用前轮诊断，代价是串行依赖和更长历史；并行候选仍可能更适合低延迟。应分别核验质量、完整计算/内存成本与实际延迟，设定可拒绝的轮次上限，并在退化、冲突或预算不合算时回退直接生成或并行选择。作者的训练配方消融支持这些行为的联合价值，不单独证明三个内部行为各自的因果收益。
<!-- source-family:SF-2026-META-UNIT -->

若生成器可以把 token 从 A 改成 B，runtime 必须区分：

```text
provisional state  模型仍可修改
committed output    已对用户、工具或下游产生承诺
```

还要把“持久条件副本”与这两者分开：一种迭代生成分支会保存选中的 clean-token 假设并持续覆盖后续 denoiser 输入，但底层 noisy state 仍可变化，最终输出也重新读出，而不是直接复制该假设。它用较稳定的上下文协调并行位置，代价是错误假设持续影响后续步骤；条件保留时间、底层可修改状态与外部输出提交必须分别定义，不能因算法称其为 commitment 就提前向用户承诺。

尚未解码的探索状态还可以与 noisy sample 分开：在每个 denoising step 内，让递归网络反复更新潜状态和读出候选，只将读出的空间信号经 adapter 交给冻结生成器；中间潜状态不必是一幅可展示图像，也不要求每次更新都单调变好。这不同于持续覆盖输入的 clean-token 副本，也不将 sampler 内一次状态更新当作外部 commit。[受限像素约束对照](https://arxiv.org/html/2610.09876v1)支持这条分工，但无符号目标训练不等无空间先验：条件与输出位置失配时，增加潜 token 仍不能恢复规则满足；晚段错误难修，部分视觉质量指标也会退步。递归、adapter、两阶段训练与状态驻留均付费，跨步保留或早段集中计算须另验，probe 读出的最终样本倾向不认证真实解。空间对应、质量或预算失败时，保留普通生成/显式约束与独立输出检查，不以内部探索批准发布。<!-- source-family:SF-2026-ARXIV-2610-09876 -->

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

固定 prefix token 还不等于固定 prefix hidden state：双向模型的已提交位置仍可读取 active block，后者每次修订都会改变其表示，直接冻结这些 KV 因而是近似。密集 OCR 尤其暴露这种差异：提前锁定错误 EOS 或绝对 offset 后，即使视觉条件很强，也难把后续片段整体移回正确位置。一个条件分支同时在训练和采样中采用局部块，再以 block-causal attention 阻止旧块读取新块，使其 KV 可精确复用；仅在推理时分块不能代替这份训练支持。[受限 OCR 对照](https://arxiv.org/html/2602.16872v1)中，双向 B256 的 edit distance 从全重算 .067 增至近似缓存 .566，block-causal 训练的缓存分支为 .192，却有更高 throughput，因此不能称三倍等质量或所有块宽都改善。更小块会改变提交频率、质量和资源摊销；缓存资格来自模型可见性，不来自 token confidence。训练、重算与缓存成本均须计入，强刚性输出、误差或域外质量失准时，保留双向全重算、保守较小块或 AR，不把图像约束自动视为 token 独立性证明。<!-- source-family:SF-2026-ARXIV-2602-16872 -->

块内反复 refinement 还提供了另一种可摊销对象：不是把尚未提交 token 的 KV 当稳定 prefix，而是缓存“这一块应读取哪些历史位置”的稀疏索引。一条受限分支先在当前 block 全为 MASK 时执行一次 exact attention，按各 query head 的重要位置及共享 KV head 的投票构造索引，再让本 block 后续 denoising steps 复用。索引绑定当前 block、层、KV head、prefix 与预算；进入下一 block 要重新探测，不能把不同 mask 内容下的经验重合率解释成永不漂移的路由。逐层分配还要核实际 floor/union 后的总预算，最低保留量并不自动满足名义的全局上限。<!-- source-family:SF-2026-ARXIV-2602-14209 -->

这把每一步独立选择位置的成本换成首步 dense probe、索引维护及后续漏读风险；可省几次 denoising 决定能否摊销，而非单看稀疏 kernel 倍数。[MAGE exact-v1 §3–5/B](https://arxiv.org/html/2602.14209v1)在 Fast-dLLM 1.5B/7B、单 H100 的受限对照中，首步探测占用显著，低 step 数未必更快，32K needle 的所有稀疏分支仍退步；可选适配又需索引选择、稀疏前向和 exact teacher 三次前向，不是免费恢复质量。索引漂移、质量或摊销条件不成立时，回 exact attention、重新探测或放宽预算；这一选择不授分布 exactness，也不代替请求并发、物理 KV 搬运与尾延迟的执行层验收。

训练时还要检查“标签从哪条路径进入预测”，而不只检查 attention mask。若 query 已由本 block 的 clean token 构造，即使它只读取先前 blocks 的 KV，仍可能携带待预测标签；反过来，干净的 query 也不能读取含本 block 标签的 KV。一条双流分支让普通 causal stream 学习完整条件分布，让 strict stream 的初始表示及可见 KV 都只来自严格先前的 clean blocks，两流共享参数，但保留不同信息集。这样，“排除当前块”成为 query 构造、KV 来源与 mask 的联合合同，不是画出严格三角 mask 就自动成立。<!-- source-family:SF-2026-ARXIV-2601-16971 -->

共享权重不等于共享全部计算；双流训练增加 attention/FLOPs，推理时把块内条件项并行化又引入近似，不能由防泄漏推出原联合分布无损或通用加速。[ARMD exact-v1 §3–4](https://arxiv.org/html/2601.16971v1) 的 125M/345M 语言模型实验支持这条训练分支及其质量取舍，不是大模型迁移或生产 SLO 证明。依赖较强、质量优先或并行成本不合算时，保留普通逐 token causal 路径；下面的 clean/masked 迁移则还要另外处理本块因果位置与 next-token 对齐，不能与 strict stream 混成同一可见性规则。

即使 query/KV 合同已经排除 target 内容，任意顺序生成仍可能面对另一个问题：原序列中语义相邻的位置，与实际生成顺序中最近、可汇总已见内容的位置不再一致。让 query 携带待预测位置、key 携带已观测 token 的原位置，可以修正位置配对，却未必让单流同时适合内容汇总与任意位置预测。[D-RoPE 的受限分析](https://arxiv.org/html/2602.16092v1#S4)把这称为 structural–semantic locality 张力；其小规模字符模型在短序列接近 masked baseline、长序列退步，只支持这一假设的局部诊断。论文没有直接双流对照，因此不能从单流退步推出双流必要定理，也不能把防泄漏本身当 locality 问题已经解决。双流是否值得新增 attention 与训练成本，仍须按长度、目标与架构对照验收；短序列、固定顺序或预算有限时，单流和普通 causal 路径继续合理。<!-- source-family:SF-2026-ARXIV-2602-16092 -->

任意顺序还可以把生成单位从单位置改成一组位置：query 表达本次待填的位置，content 表达此前已经提交的组，再以排列后的组序列提供监督。这样，组间顺序与组内并行成为独立设计选择；从单位置、连续小组逐步过渡到排列分组的 curriculum，解决的是已有 causal 模型如何学习新的条件信息集，而不是仅改推理期 mask。它与前面的 target-free 可见性合同相容，却是生成顺序和迁移训练的另一条分支，不是位置编码修正的直接后代。

推理可以反复评价未完成位置，再按 confidence 或 entropy 动态选择下一组提交，以额外 forward 换取较少的串行提交轮数；同组各位置的条件预测并不证明精确 joint distribution。[A3 的受限迁移与采样对照](https://arxiv.org/html/2601.13228v1#S3)支持课程和选择策略影响质量，但使用约2B-token适配、不同初始化与训练预算，不能把模型间差距唯一归为生成机制或数据量。动态重评估、排列监督及组宽都增加训练/采样成本，也不自动获得稳定 KV 或生产加速；条件依赖强、质量优先或预算不足时，保留固定小组和逐 token AR。下文的 clean/masked 因果迁移使用不同的可见性与连续提交规则，不能把两者合并为一种无损并行解码。<!-- source-family:SF-2026-ARXIV-2601-13228 -->

### 因果模型也能学习并行块，但不是无损改变原分布

块内并行不必以双向attention为前提。另一条迁移分支拼接clean与masked序列：clean stream保持普通causal loss，masked位置只看先前clean blocks及本块的因果mask位置，并维持next-token logits的右移对齐。并行块扩大后，可见真实前缀减少；保留clean-stream AR目标便是在训练新路径时继续练习原路径，而不是无需训练的解码加速。

推理按从左到右的置信阈值接纳连续token，至少前进一步；阈值放宽会用不完整块内条件换更少forward，不能像exact speculative verifier那样保持原AR checkpoint分布。单token回退也只是新checkpoint的AR模式。缓存还要区分稳定prefix与mask假设：重算已填块的clean KV再推进，在batch实现中快样本会等待慢样本。于是token/forward的收益可能被额外块计算、cache刷新与同步吃掉；质量或严格streaming优先时仍保留普通AR。

[MARS](https://arxiv.org/html/2604.07023v1)在Qwen2.5-0.5B/7B、greedy短输出上的消融支持上述迁移；clean/masked拼接增加训练成本，较低阈值损伤格式遵循，不同cache粒度与batch也出现慢于AR的配置。相同epoch不意味着相同训练FLOPs，平均benchmark改善不是保分布或通用SLO证明。本章拥有生成目标/commit边界，cache与batch执行再交给推理章节。<!-- source-family:SF-2026-ARXIV-2604-07023 -->

因果可见性、监督位置与提交粒度其实是三个独立选择，并不一定需要 clean 辅助流。一条单流分支把 corrupted prefix 输入严格 causal decoder，仍在全部位置预测右移后的原 token，而不只监督被 mask 的位置；推理再按块提出和接纳多个 token。这样保留了 next-token 对齐，却没有恢复被腐化前缀中的真实信息。尤其序列起点没有足够上下文时，均匀腐化会迫使模型在信息不足处学习；限制 mask 到较晚的 soft tail、按此前 mask 密度调整 loss 权重，是在修改训练信息量与权重分配，不是由 causal mask 自动得到完整 AR 条件分布。<!-- source-family:SF-2026-ARXIV-2601-22031 -->

这条分支用块内置信度决定当前接纳位置，完整块提交后才作为稳定 KV 前缀继续；达到硬迭代上限时强制填满块会减少调用，也可能带来重复与质量退化。[CARD 的局部对照](https://arxiv.org/html/2601.22031v1)支持上述三种选择与 soft-tail/权重取舍，但其 1B、300B-token 训练的平均任务结果仍低于 AR 基线，不能证明并行块无损替代逐 token 生成。生成评价明确采用 batch 128；训练硬件未披露，附录的 attention/configuration 描述与主文还有冲突，因此不从所报加速推导训练效率或任意并发下的收益。信息不足、质量或严格 streaming 优先时，保留普通 AR 或更小块，执行层另计 cache 刷新、同步与端到端成本。

多模态多轮数据还带来一个不能仅靠“块间因果”解决的泄漏边界：一轮回答很短时，固定大小的最后一块可能包含下一轮用户提示；若块内双向读取，这些未来提示便会参与当前回答的预测。因而可见性需要同时绑定 token 的 role、modality 与 turn，而不能只绑定绝对位置或 block 编号。一条迁移分支只腐化 response text，把不变的视觉表示保留在 clean stream，让 noisy block 读取先前 clean context，并在当前 response 结束处截断块；clean stream 仍按 token-causal 目标训练。它既避免跨轮未来信息，又省掉 noisy stream 中重复的视觉表示，但不能由训练期 loss 下降推断开放对话已没有泄漏。

这也解释了为什么已经对齐的 AR VLM 可以直接学习上述生成接口，而不必先把文本 backbone 改成 diffusion、再重建视觉对齐；两条训练路径的初始化知识并不相同，有限预算下直接迁移更好不能证明二者具有相同能力上限。推理中可由 causal 模式先产生首 token，再并行提出余下位置，按 causal 验证的匹配前缀接纳并裁剪 KV；这不是任意采样分布的自动 exactness 证明。[Fast-dVLM 的受限实验](https://arxiv.org/pdf/2604.06832v1)中，长回答质量仍低于原 AR 基线，单 H100、batch 1 的吞吐也不能代替生产 SLO。多轮边界、mask 规则、训练目标与缓存裁剪必须作为同一 artifact 验收；长推理质量或严格因果接口优先时，原 AR 路径仍合理。<!-- source-family:SF-2026-ARXIV-2604-06832 -->

### Block Boundary 也可以成为受约束的生成状态

固定 block 在静态 shape kernel、短输出和低调度复杂度优先时仍是稳健基线；不同语义步骤长度差异很大时，同一 block size 会让简单段过度迭代、复杂段过早 commit。一个 learned-boundary 分支允许 decoder 提出可验证的 block-end，runtime 冻结 boundary 与 policy revision 后再提交；训练可以用 entropy trajectory 做辅助 shaping，但任务 outcome 或独立 verifier 仍拥有正确性。<!-- semantic-body-binding:SF-2026-ARXIV-2605-02263 -->

动态边界用更贴合语义步骤的并行度换 variable-length scheduling、cache/rollback 复杂度、reward hacking 与错误自信。边际 entropy 下降既不等于推理正确，也不等于步骤结束；未校准、开放生成或部署并发使收益不稳定时，应回退固定 block。exact-v1 只支持作者 reasoning benchmark 与后训练设置，不能证明动态 block 在所有 workload 更快。

不训练新的 boundary head，也可以把当前置信轨迹用作前瞻范围的 proposal：从已提交及高置信连续前缀之后的第一个低置信位置拟合 confidence cliff，周期性更新 logistic 曲线，再据此选择下一次并行计算的 horizon。这里要分开拟合的 anchor 与实际 commit 阈值；散点位置已接纳不等于连续 cursor 可以跨过未提交位置，边界收紧也仍是任务相关配置。它以拟合、动态 shape 与调度状态换少做无效远端预测，不能把 raw confidence 当作正确性或授予新边界自由提交的权限。

[PACE-dLLM 的理论与受限评价](https://arxiv.org/html/2609.26249v1)进一步限定了这条分支：oracle yield 要求单调 eligibility probability、独立同分布的轨迹形状与截断饱和收益，理论中的概率并不是运行时拟合使用的 raw confidence；更大的固定块也可能取得相同 oracle NFE。单 H100、batch 1、固定生成长度且关闭部分 KV 优化的对照只隔离 decoding 规则，Dream 分支甚至更慢，不能据此证明完整 stack、所有长度或质量目标都受益。平坦、非单调或退化拟合应按已声明的边界回退固定块/单 token 路径；任务正确性 Gate 与端到端延迟验收仍独立于 horizon proposal。<!-- source-family:SF-2026-ARXIV-2609-26249 -->

## Draft、Verify 与 Correct 不是同一件事

### 跨分辨率 Draft 需要显式 Semantic Lock

图像或视频始终在高分辨率状态上迭代，最容易保持统一语义，却会把大量计算浪费在已经稳定的区域。另一条分支先生成低分辨率 draft，由独立验证器标记语义稳定区域并冻结 semantic lock，只对未锁定区域恢复高分辨率 state 继续计算。低分辨率状态拥有 proposal，不拥有最终像素真值；lock 必须绑定尺度、区域、验证器和可重开条件。

这用验证和跨尺度映射成本换 selective compute，也可能把早期错误锁死或在边界产生不连续。细节密集、全局结构持续变化或验证器不可靠时，应回退全分辨率迭代或允许全局 rollback。现有 exact-v1 只证明作者 workload 下的质量/计算权衡。<!-- semantic-body-binding:SF-2026-ARXIV-2605-02152 -->

跨尺度还有一条不锁定最终像素的preview分支：先用低分辨率状态筛选seed或prompt，选好后重新运行标准高分辨率生成，而非把LR结果上采样后继续当作完整HR轨迹。它要求检查downsampler `D` 与velocity是否近似可交换；不成立时，用短窗口缓存的HR velocity校正LR更新，selector与correction共同决定预览能否保留有用语义。<!-- source-family:SF-2026-ARXIV-2604-09227 -->

这把大量候选的HR成本换成有条件的LR筛选，却增加downsampler选择、早期HR计算和缓存漂移；commutator小是局部近似，不是完整HR等价或任意flow天生scale-compliant。[受限Flux/SD3.5实验](https://arxiv.org/html/2604.09227v1)以A100上的quality、LR/HR相似和实测latency比较，不能把预览速度直接当最终图像交付速度。细节影响选择、近似失效或筛选成本不合算时，直接HR采样仍合理；选择结果也不能跳过最终HR质量验收。

跨尺度状态也可以由受训的latent映射接入高分辨率生成，而不先解码成像素、插值后再编码。此时latent重建、解码后的像素误差与相邻帧差分是三个不同目标：latent接近不保证没有block artifact，逐帧像素好也不保证时间一致。高分辨率refinement还可分别限定低通分支进入attention的高噪声阶段、高通分支进入FFN的低噪声阶段；频带、算子位置与训练噪声支集需一起绑定，不能将它们统称一个通用课程或认证频率因果。[受限对照](https://arxiv.org/html/2602.11564v1)中更高分辨率的平均质量仍退步，普通LoRA也有较差FID；数据筛选/锐化与接口共同变化，不保证所有质量提高。中间codec往返被省去，最终decode、像素监督训练、latent映射及expert计算仍付费，不能用单模块速度授整条4K实时。跨尺度失真、时序回归或总费不合算时，保留RGB级联、普通latent插值与原HR采样，并验最终输出而非只验latent。<!-- source-family:SF-2026-ARXIV-2602-11564 -->

### Draft + exact verification

speculative decoding 允许便宜 drafter 提议 token，再由 target 验证。若 acceptance rule 正确，可以保持 target distribution。它的目标是减少昂贵 target serial steps，不改变 target 的输出语义。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-14305:start -->
对 masked diffusion，target distribution 本身也必须先定义清楚：若同一 corrupted input 上的 clean positions 被独立预测，
posterior factorization error 会让并行位置组合成不一致结果；prefix-conditioned clean-token factorization 改变的是 target
distribution construction。其上的 speculative verifier 只负责更快地采样并保持该 target，不能把“目标如何分解”和“目标如何
加速”合并为一个 correctness owner。prefix 依赖增加串行性和实现复杂度；收益不稳定或 verifier contract 不完整时，应回退
普通 DLLM target、较小 block 或完整 target sampling。exact-v1 只支持作者 Method 与实验，不证明所有 DLLM 都需要同一分解。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-14305:end -->

### Correction

correction 允许同一模型或 corrector 修改已经可见的 provisional tokens。它可能改善质量，但不天然保持某个 AR target distribution，也可能振荡或破坏正确 token。

### Diffusion Bridge 可以替换局部层，但不能冒充独立语言模型

<!-- semantic-body-binding:SF-2026-ARXIV-2605-14368:start -->
直接把完整 Transformer 改成 diffusion LM 会同时改变表示、生成目标与 runtime，难以判断收益来自哪里。一个受限分支先用
geometry proxy 选择 diffusion-friendly hidden interface，再以 conditional diffusion bridge 替换 lower layers；保留的
suffix 与 LM head 继续负责 token recovery。bridge 拥有中间表示 proposal，不拥有最终语言分布。它减少重建范围，却增加
bridge size/depth/compute 与 suffix coupling；几何 proxy 失配、接口漂移或恢复质量下降时，应回退原 Transformer 或更浅
replacement。exact-v1 的结果不证明 standalone diffusion LM，也不支持跨 backbone 无损替换。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-14368:end -->

<!-- semantic-body-binding:SF-2026-ARXIV-2605-09603:start -->
普通 masked diffusion 只把尚未决定的位置从 mask 变成 token，因而一旦早期错误被 unmask，后续步骤通常只能在其周围继续填充。显式 edit state 把这条不可逆路径改成“并行 proposal → insertion/deletion/replacement proposal → refinement 验证 → commit”：corrector 可以重开已经可见的位置，但 runtime 仍拥有版本、预算和最终提交权。

可撤销修正提高了错误恢复能力，却增加训练目标、编辑步骤、状态对齐和不收敛风险；它也不自动保持某个自回归 target distribution。现有结果只支持作者披露的语言模型、任务和 evaluator，不能外推为所有 diffusion LM 的质量保证。编辑振荡、延迟预算紧或 exactness 要求高时，应回退保守 mask schedule、限制 revision 次数，或直接使用 AR。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-09603:end -->

生成状态可撤销之后，还可以改变下一步揭示哪个 slot，而不只改变 token proposal。一条受限路径将 slot 顺序作为搜索动作，在 slot 内仍按自回归生成，用当前 slot confidence 与完整后续 rollout 的平均 confidence 混合评分，再按访问次数选择下一 slot；它是揭示顺序的 look-ahead，不是下节 target 验证。两个分数仍来自同一模型，不取得答案真值或精确目标分布。[必要顺序与探索对照](https://arxiv.org/html/2602.12586v1)显示，探索不足时更多 simulation 可强化高 prior 的错误，约九倍搜索还增加近线性生成成本；不同 slot/serial 配置也不全是单变量顺序实验。搜索 token、额外 forward、探索预算及独立质量须一起计量；自信失准或收益不抵成本时，保留 greedy/sequential slot、原并行路径或独立 verifier，而不是只增加 rollout。
<!-- source-family:SF-2026-ARXIV-2602-12586 -->

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

连续 latent diffusion 没有每步可提交的 parser state，形式语法还可作为软引导而非 masked proposal 的硬 admission。一个受限分支先把字符 DFA 对齐到词表，使同一合法字符串的全部 tokenizations 都有接受路径；给定各位置相互独立的 decoder marginals，再把 token 概率汇成状态转移矩阵，以矩阵连乘计算接受质量，并对其对数反传到 noisy latent。[Diffinity 的必要机制](https://arxiv.org/html/2602.12468v1)在该独立 decoder 分布内精确计算质量，但高噪声时它只是实际条件分布的 proxy；增加 soft guidance 不保证最终一次 argmax 满足语法，更不认证语义。词表对齐、自动机存储、每步梯度和完整 diffusion 仍需计费，零接受路径或自动机过大时这个接口不可用；受限 JSON 对照还采用不同 padding 协议且合法率低于 AR baseline，质量指标只对 passing population 计算，不能写为全质量支配。应独立验证最终合法性、通过率、质量与总成本，失败时保留完整输出校验/修复、masked 可完成性 verifier 或 AR constrained decoding，不由形式质量代理继承普遍 conditional-convergence 保证。<!-- source-family:SF-2026-ARXIV-2602-12468 -->

形式语言可完成性之外，并行输出还可能需要全局 all-different 约束。例如，N 个文档各用一个唯一、单 token 的 identifier 表示，N 个排名 slot 独立取最大概率会重复或遗漏，局部 token 合法不能保证最终是一个排列。一个分支在每轮只允许尚未占用的 identifier，按 `(概率, slot, identifier)` 排序后逐对接纳，每个 slot 与 identifier 最多使用一次，再按置信度 remask；另一个分支只做一次全 mask forward，形成 N×N 的 marginal 概率矩阵 `P`，以 `−log P_ij` 作 cost 求一一 assignment。模型拥有 relevance proposal，assignment 拥有排列有效性；后者最小化的是 slot-marginal surrogate，不是模型的真实 joint 排列概率，也不认证排名语义正确。<!-- source-family:SF-2026-ARXIV-2602-12528 -->

这一选择把有效性与 relevance 分开验收，却增加 N² 矩阵、matching 或 K 轮 forward/remask 成本；已可见 slot 的保留规则也限制后续修正。[DiffuRank 的受限对照](https://arxiv.org/html/2602.12528v1)在相同文档集下修复 raw permutation 的重复/遗漏，但最终 ranking 另有 postprocess，不能把 raw 有效率当最终检索质量；增加 K 也并非单调提高 NDCG。其 vanilla Transformers 延迟比较不证明部署并发或尾延迟。identifier 无法单 token 编码、候选集太大、matching 预算或 relevance 回归不合格时，AR listwise、pointwise scoring 或先评分再确定性排序仍是合理退路，不把 Hungarian 算法本身说成新的生成机制。

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

同一个 typed object 也未必只有一种学习上等价的序列：绝对坐标直接描述位置，相对坐标描述连续增量，两者可以解析为同一 geometry，却把不同距离依赖与累积误差交给 generator。[受限 SVG 对照](https://arxiv.org/html/2602.21461v1)中，小模型的相对坐标取得更高 OCR 辨认比，却有更差几何距离，较大模型的绝对坐标则在两项都更好；parse 合法、可辨认和 geometry 因而必须分开验收，不能仅按较短命令或单项分数选 serialization。OCR 比值可超过100，不是绝对准确率；坐标舍入、采样几何 evaluator、模型容量和数据阶段均属于比较合同，额外数据的两阶段收益也不证明唯一 staging 因果或最低参数门槛。只覆盖 Latin 单 path 的实验不能担保任意 topology、fill/stroke 或 SVG 程序；训练、数据规范化、输出长度与 typed 验证增加成本，表示或几何回归时保留较简单 schema、原 serialization 或专用 head。<!-- source-family:SF-2026-ARXIV-2602-21461 -->

### Any-to-any AR 把 Modality Type 移入同一生成序列

Typed unified generation 仍可保留不同任务的输出 decoder；更进一步的 any-to-any AR 分支把每种模态都编码为 decoder-only sequence，使图像、文本、音频或其他离散表示既可成为条件，也可成为下一段输出，而不为每个方向增加独立 head 和 loss。Checkpoint 拥有 modality tokenizer/codec、type delimiter、sequence order 与共享 decoder；runtime 拥有 typed segment 的状态和提交边界，下游 decoder 仍验证每种输出的可解释格式。

共享 factorization 减少任务接口分裂，并允许 chained generation 把一种模态的 provisional output 再作为另一模态的条件；但这不是独立 self-verification，因为两次生成共享权重、输入和误差。统一参数会引入 modality interference，长媒体 token 也会放大序列成本、KV residency 与调度不公平。某一模态需要强校准专用 head、codec 失配或共享训练造成负迁移时，应保留 specialist model/head；现有 exact-v1 只支持作者任务中的 specialist/multitask 对比与 chained generation，不证明所有模态共享表示或损失最优。

<!-- source-family:SF-2026-ARXIV-2607-25948 -->

跨模态共享训练仍有一个更具体的缺口：分别学会 text→image、image→3D，不保证前者生成的图像能被后者一致重构。成对数据充足、完整三模态数据稀缺时，可以先训练独立条件任务，再加入带已知 camera pose 的 view tokens 和交错的 text→image→3D→posed image 序列，让后续模态读取同一 prefix 中的前序状态。共享 backbone 可以保留 conditioning/generation 双流与各模态 output heads；“统一”不要求抹去每种 codec 和输出分布。

这条分支用额外的成组数据、长序列与梯度耦合换取跨模态一致性约束，仍须检查 synthetic data 偏差、几何重构和任务间干扰。[Omni123](https://arxiv.org/html/2604.02289v1#S4.SS5)的 2.2B、256 H100 训练案例在预训练后仍使用三模态及六视角成组数据，不是“仅凭成对数据就证明闭环一致性”；作者所测生成/编辑结果也没有分离训练配比与架构的全部因果贡献。数据或算力不足、某一方向质量更重要时，独立条件模型和显式转换仍是合理分支。

<!-- source-family:SF-2026-ARXIV-2604-02289 -->

### 理解能力可以监督生成表示，但不能兼任生成真值

共享生成器减少任务接口分裂，却不保证 noised generative representation 保留了理解任务需要的语义。一个有条件的
训练分支冻结已有 understanding expert，让它从生成路径的中间表示重述 caption 或回归视觉特征，使理解目标的梯度
进入 generator；semantic re-caption、prompt masking 与 metaquery 则用于减少目标 token 泄漏和简单复制条件。
这里 frozen expert 只拥有 gradient proposal，最终生成质量仍由与其独立的任务 evaluator 判定。

这种 layering 用既有理解先验换更强的语义约束，也会把 captioner 或 visual encoder 的偏差蒸馏进生成器，并可能与
像素细节目标发生梯度冲突。现有证据限于 BAGEL-7B、5K iterations 以及作者的图像生成/编辑数据与 judge；PCA
可视化不构成因果证明，也没有覆盖视频、音频或生产 serving。理解先验失配、发生 supervision leakage 或 specialist
质量更稳定时，应回退 generation-only objective、独立理解/生成模型或更窄的辅助损失。

<!-- source-family:SF-2026-ARXIV-2605-05781 -->

理解先验还可在 inference 时成为显式条件，而不只给生成器辅助梯度。原生 text encoder 在已有 T2I 路径稳定时仍合理；一条受限分支先由冻结 MLLM 将原 prompt 改写为增强文本 $t^*$，让 $t^*$ 继续经过原生 text encoder，同时以同一文本和 learnable queries 经 flow bridge 生成视觉 feature，再由逐层 injection adapter 注入冻结 T2I。这里增强文本替换原 prompt，并非 raw prompt 原样并列；两路条件分开保留，也不是用外来 feature 强行取代原生编码器。虚拟 feature 来自同源文本 proposal，不是独立真实 reference，更不认证生成图像符合世界事实。<!-- source-family:SF-2026-ARXIV-2601-04706 -->

选择视觉表示时，还要区分真实 feature 的重构能力与近似伪 feature 下的稳健性。[双条件桥接的必要对照](https://arxiv.org/html/2601.04706v1)中，真实 feature 重构较强的 encoder 对 forged 近似也可能更脆；noise/cosine proxy 不证明唯一误差因果。FLUX 的 GenEval、DPG 和 MeiGen 的部分指标仍退步，冻结旧权重也不授整个 pipeline 理解无损或所有任务改善。额外 MLLM、2B bridge、1B injection 及其训练都有成本，披露的 0.49s 仅属 bridge，不是端到端实时或轻量证明。表示或任务失配时，保留 native text-only、真实 reference 条件与独立生成评价，不把同源条件的一致性当自验证。

### Discrete Causal State 与 Continuous Flow State 可以交错，但不能混成一个身份

Any-to-any AR 把模态都放进同一离散序列，接口最统一，也便于沿 causal order 复用语言推理状态；它的代价是连续视觉变换必须先离散化，媒体 token 又会拉长 generation path。另一条条件分支不是把 VLM 与 flow 串成两个互不相知的模型，而是在层间交错两种状态：causal language stream 保留离散条件和推理顺序，invertible flow stream 维护连续视觉变换，crossing skip connection 只负责交换表示。

这种结构减少两阶段 pipeline 的语义断点，却把 checkpoint identity 扩展为 `shared causal mask + flow depth + vertical connection + staged-training revision`；任一侧升级都会改变联合目标、跨流 cache 与生成状态，不能只复用另一个 stream 的验收结果。共享表示还会引入 modality interference 与训练阶段耦合。理解或生成任务不需要共享状态、两侧校准失败，或升级后无法重做联合验收时，专用模型和显式两阶段 pipeline 仍是更稳健的回退。

[受限证据](https://arxiv.org/html/2605.08029v1)只支持作者架构、分阶段训练与所测理解/生成基准；统一 NLL 不证明所有任务共享 backbone 最优，也不提供生产 serving latency、跨流 cache invalidation 或故障恢复结论。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-08029 -->

<!-- semantic-body-binding:SF-2026-ARXIV-2605-20316:start -->
从头联合训练不是获得双向生成的唯一入口。已有 text-to-image checkpoint 在 image prior 值得保留、数据与算力受限时，
可以冻结 text encoder，只用 LoRA 与新增 text heads 把 `image time` 和 `text time` 分开；text→image、image→text、
joint generation 与 partial-text completion 由此成为同一二维时间状态空间里的不同轨迹，而不是把两种状态压成一个
timestep。Checkpoint identity 也随之扩展为 base revision、LoRA、text head、双时间 schedule 与 token insertion
规则。

薄适配降低训练成本，却把两条时间轴、跨模态接口和 schedule compatibility 变成新的故障面；小数据也不足以补齐
外部知识与复杂 VQA。分辨率、数据或 text task 越出验证域时，应回退单向生成器配独立 caption/VQA 模型，或进行
完整 multimodal pretraining。现有 evidence 只支持 exact-v1 的 matched-LoRA、有限 SD3/FLUX 与 joint/VQA 设置，
不证明这种迁移合同可替代大规模统一训练。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-20316:end -->

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

### Parallel Progress 与 Active Compute 是两条独立成本轴

Block denoising 每次参数读取可以推进多个 token，因此主要减少串行 NFE；结构化稀疏或 spike execution 则尝试减少一次 forward 中真正活跃的 channel/operation。两者组合时，成本模型必须同时记录每次迭代提交多少有效 token，以及硬件实际执行多少 active traffic。只报告 NFE 会忽略一次 forward 的工作量，只报告 sparsity 也会忽略多轮 denoising 和状态管理。

一个受限 neuromorphic 分支用 token-level roofline 区分 memory-bound 与 compute-bound：参数读取占主导时，多 token progress 可摊薄搬运；可跳过的 inactive channels 足够多且硬件真正利用时，稀疏才减少计算或访问。它用训练目标、spike representation 与专用硬件耦合换 active traffic，不能把作者翻译任务中的能量或吞吐外推普通 GPU，更不能把 NFE 减少写成端到端 SLO。若稀疏利用不足、fallback kernel 更慢或设备不支持跳过，应回退普通 block diffusion；append-only streaming 仍可回退 AR。

<!-- source-family:SF-2026-ARXIV-2607-24841 -->

### Refinement 位置也可以成为条件计算状态

在并行 refinement 中，不同位置距离稳定状态的远近不同，继续给所有 token 相同 expert budget 会把计算浪费在已经收敛的位置。条件计算可以读取 block-relative position、当前 refinement step 与收敛 frontier，为未稳定位置分配更多专家容量；它没有改变最终 commit owner，却把“还需要多少计算”从固定超参变成运行时状态。收益是减少无效计算，代价是训练—推理联合校准、router 抖动和调度复杂度；短轨迹、负载稳定或状态估计不可靠时，固定预算仍是可验证基线。`arXiv:2608.01784v1` 只支持作者 Diffusion-MoE 配置，不能外推为所有生成模型的通用加速。<!-- source-family:SF-2026-ARXIV-2608-01784 -->

latent可以不只由神经denoiser产生：已知几何、材质类型、光源和相机时，物理模拟也能提出待解码的特征。不过VAE通道包含有符号值、边缘强调和非辐射式遮挡响应，不能把RGB能量规则原样搬入。一个受限分支在同一scene中拟合有符号transport及额外响应，再由单view训练的residualrefiner修补latent与几何buffers对应的误差；几何/光照控制属于scene接口，最终颜色与细节仍由refiner/decoder决定，不是latent值获得物理真值。

该分工把模拟约束与codec残差分开，却要支付每scene校准、path sampling和refiner训练；未知scene重建及跨scene泛化未验证。线性latent估计无偏不保证非线性refine/decode后的RGB无偏，错误响应式也不能冒充物理保真。受限equal-error例在latent终点省时、解码RGB却因decoder更慢，因此必须先声明输出终点；细节混叠、极端光源或换codec失败时保留RGBpathtracing后encode、重新校准scene或原神经生成分支，不由局部render速度授予端到端优势。 [必要机制与反证](https://arxiv.org/html/2609.21054v1)。<!-- source-family:SF-2026-ARXIV-2609-21054 -->

生成分辨率固定，也不意味着每个区域必须一直持有同样大小的 patch。可用 quadtree 布局在粗区域合并 token、在细节区域保留小 patch，并把 scale 交给受训的解码接口；denoising 中依据 clean estimate 更新布局，让 token budget 成为质量与计算之间的条件分支。这改变了模型输入和位置/尺度接口，不能只在现成模型外删 token 就保证相同质量，布局估计和更新也消耗计算。<!-- source-family:SF-2026-ARXIV-2610-12307 -->

[当前可变预算实验](https://arxiv.org/html/2610.12307v1)在低预算时出现明显质量退步，训练或微调条件的改变也不能全部归因于布局机制。动态刷新布局的质量实验与为了 graph 优化而冻结 warm-up 布局的计时并非同一执行合同；局部 H100 forward 收益不证明完整生成服务 SLO。固定 patch 在质量容忍度低、布局刷新成本大或后端不支持动态 token 时仍合理。进一步评价最终输出，还必须把下面的 decoder 本身算作独立 artifact。

### Output Decoder 是独立的版本化 Generation Artifact

只统计 latent denoiser 或 token generator，在 decoder 轻量、输出分辨率固定时足以近似端到端成本；视频生成中，VAE decoder 可能独自占据显著 latency 与 memory bandwidth，且它的结构、压缩率和精度会改变最终画面。generation identity 因此不能止于主模型 checkpoint：latent shape/scale、decoder revision、operator/kernel、precision、resolution 与 frame count 必须一起进入 artifact 和 evaluation contract。主生成器拥有 latent proposal，decoder 拥有 latent-to-output transform，只有最终媒体通过质量和格式 gate 后才算 committed output。

Decoder 的条件接口还须保留时间对应。直接把压时的 3D encoder feature 接回 3D decoder，在原 codec 的时序分布不兼容时可能形成重影；一条受限替代从逐帧 2D encoder 提取空间细节，只在最后两个 upsampling block 已建立 latent slice 与输出 frame 一对一对应的位置注入，经融合模块与受训的 causal LoRA 适配。3D 分支仍承载时序变换，2D skip 只提供对齐的细节条件，不能任意提前接入尚混合多个帧的层；这改变 decoder 的输入和配对合同，而不是证明原 skip 必然读取未来。<!-- source-family:SF-2026-ARXIV-2512-24227 -->

逐帧对应只限定这一局部接口，不授整条生成管线在线因果性，也不使 detail encoder、feature 驻留、adapter 与额外训练免费。[有限重建/编辑对照](https://arxiv.org/html/2512.24227v1)在重建训练中用真值编码 latent 近似生成 latent，部分指标仍退步，阶段组合并非完整 factorial，数据改变也有独立效应；不能把更清晰的重建拼成所有生成质量或实时全链保证。换 temporal stride、帧数、latent 分布或 codec 后，应重新校准 frame 对应与最终时序质量；不兼容或收益不足时，保留原 3D decoder、独立逐帧路径或重新训练配对接口，而不由局部对齐跳过输出验收。

channel pruning、operator replacement 与 distillation 可以缩短 decode，却会引入重建误差、时序闪烁、分辨率/帧数外推失效和硬件特化；主模型质量不变也不能证明最终输出等价。decoder 不是瓶颈、质量容忍度低或运行条件离校准域很远时，应保留原 decoder 或逐级 fallback。优化必须报告完整 pipeline latency 与最终质量，而不能把 decoder microbenchmark 当成整个生成系统加速。

<!-- SF-2026-ARXIV-2602-19161 -->

如果论文为每个 dataset 事后选择最佳 tree budget，它证明“存在有效 operating point”，不等于已经给出线上 controller。

### Pixel Diffusion Decoder 需要独立的重建与预算 Gate

<!-- semantic-body-binding:SF-2026-ARXIV-2605-23902:start -->
VAE decoder 在 latent 表示稳定时便宜，但高分辨率细节可能受固定重建器限制；generative pixel decoder 可以把 latent revision、sigma-aware conditioning、pixel sampler 与 early termination 写成独立 decode artifact。停止规则只提出完成候选，重建质量和预算 Gate 决定是否提交。

生成式 decoder 提高细节自由度，却增加采样成本、随机性与高分辨率稳定性风险。作者实验只支持披露模型与最高分辨率条件；重建、时延或内存越界时，应回退 VAE decoder、cascade 或较低分辨率路径。arXiv:2605.23902v1
<!-- semantic-body-binding:SF-2026-ARXIV-2605-23902:end -->

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

视频内部还要区分跨帧关系的粒度：同空间位置的 temporal attention 在位移小时便宜且保留局部运动先验，直接连接所有时空 token 则付出更大的关系矩阵；一个受限替代先把每帧 token 矩阵经可学习行、列投影形成 Q/K/V，再由整帧相似度得到共享的跨帧权重，与原逐位置 temporal 分支并行融合。共享权重改变了哪些位置共同读取其他帧，不等于恢复所有逐 token 关系；行压缩仍有损，投影、时间平方项与新增训练也仍付费。[有限视频对照](https://arxiv.org/html/2603.09721v1)支持这条参数化选择，而不支持与 full-3D Attention 表达等价或任意长度稳定；冻结 Latte 后的新增容量与数据未获完整匹配控制，部分 flickering 指标反退。直接替掉预训练局部分支还会失去时间连贯，因此大位移收益、压缩细节或完整质量—成本验收不足时，应保留局部路径、减弱压缩或回退原 dense 生成器。<!-- source-family:SF-2026-ARXIV-2603-09721 -->

### 关联记忆模块不能跨模态直接外推

Hash-keyed O(1) associative memory 在文本中可能为重复局部 token pattern 提供捷径，但受控负结果显示，它移入 AR 图像生成后未必承担同样的 retrieval 功能。图像 token 的局部重复、顺序结构与语义身份不同，模块名称相同不代表机制角色相同。<!-- semantic-body-binding:SF-2026-ARXIV-2605-13179 -->

这是一条反外推证据而不是“Engram 永远无效”的结论。若新模态上没有 retrieval ablation、命中率与生成质量的共同证据，应保留普通 Transformer 路径，不以文本任务收益批准图像系统复杂度。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-20309:start -->
但“不能直接外推”也不等于视觉关联记忆没有可行边界。一条更窄的路径把 exact n-gram registry 当作显式地址，只在
匹配 span 时向冻结生成 backbone 注入 concept residual；no-trigger 路径完全不激活该分支。这样，trigger registry、
concept adapter 与 activation record 共同形成可审计的 personalization state，而不是把记忆能力归因于整个模型。

显式 lexical address 换来局部激活和便宜模块化，也把 tokenizer 兼容、组合 trigger 冲突与 registry provenance
带入生成合同；初步视频结果仍不能证明跨帧身份稳定。未命中、跨 tokenizer 或视频一致性失败时，应关闭 memory
branch，回退冻结生成器、普通 LoRA/adapter 或更强视觉状态注入。现有证据只覆盖 exact-v1 的 SD1.5/SD3.5、初步
Wan2.2 与定性小样本，没有与 DreamBooth/LoRA 做 matched benchmark。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-20309:end -->

## Training / Inference mismatch

AR teacher forcing 训练看到正确前缀，推理看到自己的历史输出；diffusion training 看到人工 noise/mask distribution，推理看到由模型 schedule 产生的中间状态。两者都有 exposure mismatch，只是形式不同。

Framewise AR还可同时改变codec与训练支持，而不只换生成head：causal temporal编码后逐帧作multi-scale量化，下一帧消费过去frame KV与当前coarser scale；训练对bit codes施加随时间增长的扰动，让后一帧首scale继承前帧扰动范围，并以random causal window改变可见历史。它把部分误差带入跨帧训练条件，却不证明人工bitflip等同真实rollout分布，也不与只缩小反传窗口或任意cache复用等价。<!-- source-family:SF-2026-ARXIV-2601-05966 -->

[受限UCF/作者内部视频对照](https://arxiv.org/html/2601.05966v1)的tokenizer使用Infinity空间预初始化、2000epochs/batch128；rFVD61仍差于Omni42，randommask的quality提高而semantic66.64→65.89退步。4B输出384×672/8FPS、高dynamic漂移与完整ARattention成本都是边界，20秒定性续写不是长一致性证明。30steps/.86s缺已核硬件及匹配总预算，不授单机制13倍加速或SLO。Codec适配、corruption校准、训练及完整解码计费；漂移或质量/成本不合算时，保留原codec/full-history训练、较低corruption与独立rollout验收。

视频序列变长后，还要区分**模型看到的历史窗口**和**本步参与优化的窗口**。直接缩短训练片段、生成时只用上一块作条件，可以降低训练成本，却改变了模型学习与使用的依赖。另一条分支保留优化窗口之前的完整真实历史作为前向条件，对这些历史表示停止梯度，只在随机、重叠的局部窗口计算目标；推理仍按完整历史进行标准 AR。这减少反传范围，而不是宣称长程依赖已经消失。<!-- source-family:SF-2026-ARXIV-2604-07402 -->

这种局部优化仍会改变哪些位置获得更新，也不会消除 rollout error。作者的视频实验中，局部目标单独使用仍明显弱于完整训练；增加首帧窗口采样和相邻表示差异惩罚后，才改善受测质量。惩罚轨迹上相邻表示的距离不等于约束网络 Jacobian，更不能证明全局 Lipschitz 稳定。重叠窗口、采样分布与连续性权重成为新的训练状态，过度平滑也会损失运动变化。只有在任务质量、时间一致性和真实训练成本同时验收时，才值得采用这一分支；短视频、强长程依赖或收益不稳定时，完整序列训练仍是更透明的基线。

proposal-correction training 会显式生成错误中间状态，让模型学习修正。但 synthetic error 是否覆盖真实 rollout error，仍取决于 corruption process。过强 corruption 可能让模型学会恢复不现实噪声，过弱 corruption 又无法处理 aggressive decoding 的错误。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-22765:start -->
离散 diffusion 的 artifact 也不能只由 corruption marginal 标识。同一个 clean-data prediction 经 bridge plug-in、marginalization / denoiser 或 score parameterization，可以对应不同的 reverse target；把 uniform process 提升到 absorbing-state representation，理论上可能保留 joint law，却仍改变 network target、loss conversion 与 sampling operations。因而可复现身份至少要联合版本化 corruption marginal、parameterization、loss conversion 和 sampler，不能把“forward noise 相同”当成训练与推理等价。

这种重参数化能暴露更清晰的 target、remasking 或 predictor-corrector 路径，却增加 auxiliary state、corrector steps、conversion 与 learned posterior approximation error。理论 joint-law 等价不意味着 factorized learned sampler 精确，也不证明某种 UDM/MDM 在其他 workload 上普遍更优。转换、假设或近似无法核验时，应冻结并回退原 denoiser/sampler pair，以完整 quality-cost frontier 而不是单一 objective 或 step 数比较方案。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-22765:end -->

反向离散过程还可把“何时离开当前状态”与“离开后去哪里”分开参数化。CTMC的off-diagonal rate写成exit rate λ与destination分布r的乘积；相应path-space KL可以分成Poisson timing误差，加上真实exit rate加权的categorical direction误差。可训练conditional surrogate与marginal目标保一阶梯度，需要forward量不依赖参数、reverse rates正且可微以及微分积分交换等条件；这不自动保证有限训练稳定或神经网络找到全局解。absorbing-mask特例中rate由noise schedule固定，才退化为熟悉的masked-token交叉熵；uniform corruption允许重复跳转，两者不能因同叫diffusion就共用训练与sampler假设。

这条分解让模型分别学习转移强度与去向，却增加一个rate head以及rate—步长校准责任。Euler需要λΔt≤1才能形成合法跳转/停留概率；τ-leaping一次时间步可抽取多个jump，并在新状态重新计算destination，因而时间步数不等network evaluations。[受限离散生成研究](https://arxiv.org/html/2604.15694v1)的163M、长度512与统一Gemma-2评分仅提供其TinyStories/OWT质量证据，有限样本genPPL不天然成为数学上界，更不证明线上延迟或所有模型优越。OWT主表与附录的sampler披露不一致，不能补造统一协议或据此归因方法排名；rate或概率合法性无法验证、质量—真实成本不改善时，应增加时间分辨率或回退已验证的mask/schedule与原denoiser，而不是只按step数宣布加速。<!-- source-family:SF-2026-ARXIV-2604-15694 -->

改变每步的跳转概率之外，还可以改变不同时间步之间如何共享随机性。独立地抽取“本步是否更新”容易让部分位置更新不足、另一些反复改写；一条分层事件调度分支为每个位置保留累计跳转质量 S 与一次抽取的均匀随机相位 θ，跨过 θ 加整数的阈值时才触发更新，再从原来的去向分布选择 token。它保留单次去向接口，却把调度状态从当前序列扩展为“序列、累计质量、相位与已触发计数”；恢复生成时也必须保留这些跨步状态，不能仅凭相同可见 token 假定后续采样等价。这是采样器的替代分支，不是 absorbing-mask 或连续时间精确模拟的自然升级。<!-- source-family:SF-2026-ARXIV-2601-02799 -->

[精确版本的必要边界](https://arxiv.org/html/2601.02799v1)是：固定累计质量或固定逐步概率序列时，随机舍入的更新计数具有正确均值，方差不超过四分之一；神经模型的概率随状态变化后，相位又与历次更新耦合，不能把这个计数结论直接变成原 Markov 过程或终态分布的精确保证。低 NFE 的有限文本与图像结果只支持相应质量—预算比较，不证明墙钟加速或通用安全；按风险重排相位还会破坏原均匀性条件。新增跨步状态、耦合和分布偏差必须与更新次数方差分别评价；若任务更重视原过程的可解释分布或回归失败，独立逐步决策与已验证的 sampler 仍是合理选择。

在 absorbing-mask 这条分支中，离散化也可分别处理空间条件与时间速率：每步固定当前已揭示状态及模型给出的去向分布，却用 mask schedule 的解析时间因子重标度跳出速率，积分 hazard 决定保留 MASK 的概率；最后一步再令 MASK 概率为零。它不等把整个 rate 在时间上常数冻结，也不是 uniform corruption 的同一采样器。[精确 mask 理论分支](https://arxiv.org/html/2602.15008v1)把 score 学习、初始化与步内忽略条件依赖的误差分别计入；依赖结构较小才支持更少迭代的条件，合法非负、有限且去向总量非零的 score 是必要接口。uniform 情形的下界限定该 τ-leaping 的 path KL 与熵分离人口，不能签发所有输出分布或所有 sampler 的复杂度下界。较少 steps 仍要支付维度、词表与模型求值费用，理论没有实测 LM 质量或端到端加速；依赖/score误差大、率不合法或预算不满足时，增加时间分辨率、刷新空间条件并回退已校准的 mask/sampler pair，而非由末步 unmask 认证正确样本。<!-- source-family:SF-2026-ARXIV-2602-15008 -->

另一种时间—空间分责来自已有 First-Hitting Sampler：按 absorbing-mask 过程抽取下一次揭示的时间与位置，再由 learned conditional 选择该位置的 token，每次只揭示一个。对长度 d、真实数据无 MASK、全时间积分 score-entropy 误差受控的条件，[受限定理](https://arxiv.org/html/2602.22505v1)把恰 d 次采样后的 KL 误差界定为学习误差，没有另加时间离散化项；这不表示 learned conditional 无误，也不说明同时独立揭示多个 token 继承该界。相对地，Euler 的直接 TV 分析能从 all-MASK singleton 初始化，仍分别支付初始化、score 估计、有限步和 early-stop 误差；constant-step Euler 的构造下界不是所有 sampler 的下界。FHS 的 d 次模型求值及词表选择仍有费用，理论未提供真实 LM 质量或墙钟加速，不能只按 step 数替换生产路径。数据含 MASK、积分误差不可控或质量—成本不合算时，保留原 denoiser/sampler、较细时间分辨率与独立终态评价。<!-- source-family:SF-2026-ARXIV-2602-22505 -->

固定 corruption schedule 最透明，但有利的生成顺序也可以成为训练变量：在固定辅助位置上先插入 MASK、再揭示 token，以每个干净样本条件下的 CDF 定义两类 hazard，收缩未插入位置后得到可变长度序列。CDF 的起终点保留约定的终态接口，generator 在部署时仍只从当前可见序列预测 rate 与 token，而不读取训练用的完整答案。目标路径本身依赖参数后，更新必须同时处理采样分布的 score-function 项与 loss 的直接梯度，不能套用“forward target 固定”的分解。<!-- source-family:SF-2026-ARXIV-2602-18695 -->

[学习顺序的必要反侧](https://arxiv.org/html/2602.18695v1)是 schedule 可能把大部分事件推到端点，以压低 rate-weighted prediction loss，却没有学得更好的生成；混合 CDF prior 与逐位置 endpoint 软惩罚只约束这一退化，并非硬质量证书。受测 star graph 中，固定 unmask 参数反而比完全自由稳定，共享 backbone 也可能明显退步；双中间样本、辅助 rate 网络和估计方差都付费。有限 τ-leaping、nucleus 与 confidence reveal 仍改变实际采样，不继承连续目标的精确终点分布；proxy、覆盖或净收益失准时，保留固定 schedule/原 denoiser，并增加时间分辨率和终态验收，而不是把 learned order 直接等同于更少步骤或普遍规划能力。

冻结模型也可以在推理时改变目标 marginal，而不先训练新权重。若目标是原分布的 annealing、多条件 product 或 reward tilt，单改一个位置的 logits 不等于整段目标已实现；一条离散过程分支联合构造新的转移 rate 与路径 weight，用有限步更新候选状态、累计 weight，再在粒子间重采样并重置权重。改变的是 sampler 所追踪的目标与候选人口，而非让 reward 认证事实；learned posterior ratio、rate、schedule、步长与粒子数须一起标识，有限粒子与时间离散也不能继承精确目标分布的保证。[Discrete Feynman–Kac Correctors exact-v1](https://arxiv.org/html/2601.10403v1)支持这个接口，不在此采用完整收敛证明或科学应用结论。

该分支用更多候选和求值换目标控制：多个条件仍需各自 forward，reward tilt 可能逐一评价所有可转移状态，weight 集中又会造成粒子退化；rate—步长不满足概率合法性时不能继续执行。受限 LLaDA-8B 代码对照以四粒子比较单粒子无重采样，在固定128输出长度、验证集调参及五seed下局部改善，并未匹配完整计算预算或证明端到端延迟优势。更可解析的输出也不等于任务正确，更多粒子并非无限增益。Ratio/target 不可信、粒子有效支持不足、真实质量—成本不改善时，保留原 denoiser/sampler、固定 guidance 或独立 outcome 选择，而不把标量温度、奖励上涨或无新训练当作免费且精确的控制。<!-- source-family:SF-2026-ARXIV-2601-10403 -->

有了局部转移接口，后训练仍不必全部转成轨迹上的 policy gradient。终态序列 likelihood 难算时，一条有条件的替代从冻结 base 的终态样本和 reward 出发，用指数 reward 权重形成 masked 中间状态的条件矩，再匹配局部 unmask posterior；mask hazard 将局部误差连接到受条件的终态 KL。这样需要共同标识 base 条件律、corruption schedule、reward 与样本 buffer，而不是直接照搬 AR token ratio：Training 负责 reward/KL 目标，本章负责终点重加权如何成为局部生成目标。<!-- source-family:SF-2026-ARXIV-2604-18739 -->

该匹配依赖相应条件期望；有限优化、近似 base posterior、旧 buffer 或 confidence reveal 都不自动继承理论结果。control variate 条件无偏也不意味着任意 reward 和系数下每个样本 target 都是合法概率，采用前须核非负性和实际 loss 接口。[受限 tilt-matching 实验](https://arxiv.org/html/2604.18739v1)的 LLaDA8B、LoRA、block32 与 8H100 训练只支持指定任务分支，MATH/GSM 仍弱于一项比较方法，过强倾斜会退步。额外 rollout、中间 mask 状态与优化不能省略计账；条件目标不可靠或质量回归时，原 masked objective、固定 guidance 与已验证的轨迹 RL 仍是可解释的共存方案。

Diffusion 的 supervision granularity 也不应被默认为全程固定。高噪声阶段主要恢复全局布局，低噪声阶段才逐步承载
局部纹理；始终对齐同一个 teacher layer 或尺度，会把非平稳生成过程压成静态目标。一条受限分支让 router 根据
SNR/timestep 选择粗到细的 representation guidance，但 router 只拥有指导尺度，不拥有最终 sample correctness。

动态 guidance 用额外 teacher features、router state 和训练复杂度换更匹配的监督；冻结 VAE 的层级未必对应另一种
backbone 或 modality，router 也可能学到数据集特有 shortcut。无法验证分层特征和时序匹配时，静态 alignment 或
无额外 representation supervision 仍是更可复现的基线。现有证据只覆盖指定 SiT、VAE 与图像数据集，不证明该
粒度演进可直接迁移到文本、视频或所有 diffusion 模型。

<!-- source-family:SF-2026-ARXIV-2605-03317 -->

指导信号的粒度变化，还不同于直接改变 denoiser 的输入 token 网格。一条动态执行分支先为较大 patch 训练新的 embedding、de-embedding 与位置接口，并用冻结 teacher 和 FFN LoRA 蒸馏，使同一 backbone 能消费不同 patch size；推理时根据历史 latent 第三差分的 patch variance 分位数，每个 step 选择一个全局 patch size，并非同一步混用局部网格。[受限动态 patch 对照](https://arxiv.org/html/2602.16968v1)因此只让 scheduler 无需额外训练，整个生成管线并不 training-free。Token 减少改变注意力工作形状，却增加适配训练、调度和质量校准：Wan 视频的 VBench 随加速下降，FLUX 若干指标也退步；组合缓存的倍率不归给该机制独享，所测阈值与速度、质量也并不逐项单调。这个代理不认证离散误差或最终 sample correctness，具体硬件、精度和端到端 SLO 未披露时更不能据 step/token 计数承诺生产加速。新 patch 接口不稳、细节或真实质量—成本验收失败时，保留原细网格与静态 guidance，而不是假定早期粗 patch 对所有模型无损。<!-- source-family:SF-2026-ARXIV-2602-16968 -->

每步选择一个全局 patch size 仍把整张图分配为均匀网格；若不同区域的细节需求不同，另一条架构分支可在同一步使用非均匀 token 集合。先在完整二维网格上用局部 encoder 汇集邻域信息，再按内容相似度选择保留位置，让主 denoiser 在短序列上计算，同时保留各 token 的原二维坐标。输出不能直接当成完整下一步状态：以置信度加权的空间平滑和最近保留位置映射回填网格，再由完整网格 decoder 与保留细节的残差生成预测。这里的 boundary confidence 管表示选择，不是物体边界真值，也不改变 sampler 所需的完整状态接口。<!-- source-family:SF-2026-ARXIV-2603-06351 -->

非均匀表示把计算集中到选定位置，却增加完整网格 encoder/decoder、路由、回填和平滑成本；平均压缩率的软目标也不是每个请求的硬计算上限，batch 补齐还会交还部分节省。[受限图像对照](https://arxiv.org/html/2603.06351v1)在随机保留位置与学习位置之间发现局部质量差异，但参数匹配和 FLOP 匹配并非同一配置，部分 recall 仍退步，不签发通用语义分割或 serving 加速保证。由旧 checkpoint 迁移还需适配新的表示与 conditioning；冻结相关条件接口、加短期 activation 对齐可以帮助稳定，但原 teacher 训练和额外恢复成本仍在。路由遗漏、回填失真或完整质量—成本不改善时，均匀细网格与原 denoiser 继续成立。

另一条空间加速分支不先训练新 patch 接口，而在原生成器上维护完整 latent 与逐级扩大的 anchor 集合：每步只将当前 anchors 送入 DiT，将其 velocity 嵌回原位置，再为空缺位置插值，使未实际求值的状态仍沿近似场演进。准备加入新 anchors 时，由上步预测 clean latent 的空间 prior 与当前 noise 幅度构造该位置 target，再转入较大集合。Selector 保原位置，lifter 不改已计算 anchor 值；这只保证与少上下文的计算结果一致，不等原完整 attention 场或真实中间分布。Clean proposal、noise/seed、active 集合、插值与 transition schedule 须和完整 state 一起标识，不能把少 tokens 或相同 noise 幅度当作语义/统计无损证书。

[JiT 的有限必要原证](https://arxiv.org/html/2603.10744v1)支持这一 training-free sampler 选择，但有限时间 micro-flow 的 limit 与伪代码直接 target 赋值不是已核连续实现，局部 velocity variance 也只提名新增位置。单 A800/FLUX 对照的 FLOP 倍率不等墙钟或完整请求收益，较激进分支的多项质量指标仍低于50NFE，晚加入细节与过稀初始集合亦会退步。完整 latent、邻域插值、排序、状态重造和 VAE 都计费，profile 与 schedule 校准也不因无训练而免费；细节/结构、target 分布或真实 quality-cost 验收失配时，增加保留集合、提前全网格或回退原 full-token sampler 与已验 steps，而不由投影恒等式签发 artifact-free 生成。<!-- source-family:SF-2026-ARXIV-2603-10744 -->

因此，直接把已有 sampler 的步数调小，与专门训练少步生成器不是同一个优化。后一条分支可让冻结 teacher 评价 student 自己走到的中间状态，再把纠正信号用于训练指定步数的 student；它用离线 teacher/critic 计算和额外模型版本换较短的在线轨迹，但没有消除分布偏移，换步数也未必还能复用同一 student。比较时必须同时记录训练成本、实际网络求值次数及在线质量：一步更新可能包含额外预测或 guidance forward，不能把 step 数直接当 latency。

少步轨迹之外，student 的网络结构也能成为压缩对象，但删层、缩短采样与表示迁移不是同一种误差。一条受限分支先用层内噪声消融给深层 dual-stream blocks 分组，保留组内代表层并平均相邻被删层的权重；平均参数并不等于复合原层的函数。它先用 teacher 的 cluster-end hidden states 对改变过的层作局部恢复，再作全模型恢复；另一分支把文本/图像投影接成 single-stream，并以拼接后的 teacher hidden states 对齐，不能把两种压缩的联合收益全部归给某一次平均或 stream 变化。[受限视频 student 对照](https://arxiv.org/html/2602.17047v1)中的风格、多样性仍有退步，数据先验的解释也未成为独立因果结论；calibration、teacher targets 和分阶段恢复不是免费。作者披露的四阶段训练合计1872 GPU-hours仅覆盖相应训练，不是完整数据生产与部署费用。压缩后真实质量—成本不改善、局部恢复不足或更换模态不再支持原对齐时，保留原深层/dual-stream teacher 或单独已验证的少步 student，而不是用参数平均认证生成函数等价。<!-- source-family:SF-2026-ARXIV-2602-17047 -->

### 训练表示与部署表示可以分离，但迁移上限必须显式

latent diffusion 借助 VAE 降低训练与推理成本，却让生成质量受 latent bottleneck 和 decoder 约束。一个替代分支用
latent teacher 生成合成图像训练 pixel-space generator，部署时移除 VAE；这把 latent model 从在线执行组件改成训练数据
producer，pixel model 才拥有最终生成状态。收益是解除线上 codec 约束，代价是 synthetic source 的质量上限、额外生成
成本与 teacher bias。teacher 覆盖不足或高分辨率细节未通过独立验收时，应保留 latent pipeline 或混合真实数据；
现有证据仅覆盖作者的 1024/4K 设置与受测 teacher。

<!-- source-family:SF-2026-ARXIV-2605-12013 -->

### Latent Reuse 受 Subspace Shift 约束

复用已有 diffusion latent space 可以节省重新训练 encoder 的成本，但新数据若离开原 latent subspace，或噪声沿不受支持方向增长，denoiser 会在错误几何上拟合。可拒绝的复用合同应测量 subspace overlap、shift 与噪声，而不是只比较重建样例。<!-- semantic-body-binding:SF-2026-ARXIV-2605-13448 -->

理论边界只覆盖论文假设与合成/受限分布，不能给出所有真实数据的阈值。shift 指标或 downstream quality 失效时，应重新训练表示、扩大 latent capacity，或回退像素/原表示空间。

### 连续 Latent 与离散 Token 需要分别拥有版本

<!-- semantic-body-binding:SF-2026-ARXIV-2605-23605:start -->
纯 masked diffusion 直接在 token state 上修正，接口单一但可能承担过重的全局组织；latent-augmented 分支先由 autoencoder 压缩，再用 latent prior 与 few-step distillation 生成全局状态，最后由 discrete decoder 还原 token。AE、prior、distillation 和 decoder 是可独立失败的 artifact，不能合并成一个模型版本。

分层表示减少部分生成步数，却会新增 reconstruction loss、跨阶段漂移和 decoder 幻觉。作者实验不证明连续 latent 对所有文本任务更优；latent 失真、decoder 不忠实或联合校准失败时，应回退纯 masked diffusion、更多 steps 或自回归解码。arXiv:2605.23605v1
<!-- semantic-body-binding:SF-2026-ARXIV-2605-23605:end -->

## Cache、rollback 与 exactness

### 双向生成中的 Cache 是可变状态，不是只读前缀

diffusion 或 masked refinement 会反复修改序列两侧，传统只追加 KV cache 的不变量不再成立。复用稳定 affix 可以减少重算，但 request-specific anchor 与被更新位置必须重新计算，并把 timestep、mask 和版本纳入 cache identity。错误地沿用自回归前缀语义会产生静默污染；保守全重算仍是低复用或高变化率下的正确基线。
<!-- source-family: arxiv:2608.26140v1; semantic-body-binding: bidirectional-affix-cache-mutability -->

进一步的近似分支只复用 token identity 已冻结的 prompt K/V，并以 response state neighborhood 与 decoder margin 判断可变区域是否仍可复用。Prompt reuse 因而是受状态距离约束的 proposal，不是 AR 式 exact prefix：mutable response 必须刷新，越界就回退 full refresh。它用距离估计与误差校准换取较少重算，也会引入阈值漂移和静默近似误差；高风险输出或 state 快速变化时，完整刷新仍是基线。

<!-- source-family: arxiv:2608.08086v1; daily-trace: papers/2026/08/11/README.md; semantic-body-binding: reversible-response-cache-state-neighborhood -->

### Block Cache 可以从历史条目演进为固定大小的递归状态

Block diffusion 先完成一个 block、再让后续 block 读取已提交历史，使 cache 与流式提交重新可用；若历史仍由 attention K/V 表示，cache 容量和每步读取成本仍随上下文线性增长。另一条分支把已提交 block 写入 state-space mixer 的递归状态，并在训练时使用与该状态更新一致的 block-causal objective。这样 cache 不再保存所有历史条目，而保存固定大小的 sufficient-state proposal；相对于同一受训计算，它可以是 exact state transition，而不是部署时临时加入的近似淘汰。

常数大小只约束 state footprint，不保证信息无损、无限长度泛化或所有任务质量不变。模型必须在有限 state 中压缩历史，训练目标、mixer、block size 与 state revision 共同成为 artifact identity；需要逐项引用原文或任意历史细节时，attention cache 仍可能更可靠。作者的 3B 模型、300B-token 训练与最长 256k 测试支持其 attention/Mamba/hybrid 对照，不证明固定状态会普遍替代 KV，也不能把单流或受测 batch 吞吐外推生产 SLO。<!-- source-family:SF-2026-ARXIV-2609-11998 -->

### Commitment Policy 可以从未来稳定轨迹学习

固定置信阈值或 block schedule 假设所有 token 的收敛速度相似。对于迭代修正生成，可以从完整去噪轨迹标注“该位置何时之后不再变化”，训练 token-local controller 预测 commitment，并用动态 threshold 决定冻结位置。它把 commit owner 从静态规则变为受限 learned policy，可减少无效更新；代价是监督依赖未来轨迹、分布漂移会导致过早锁定，且 rollback 更复杂。若 controller 未校准，原有保守固定 schedule 仍是 fallback。现有证据只覆盖冻结模型上的 plug-in 控制器，不证明其保持自回归式 exactness。

视频轨迹的错误还具有时间局部性：若 verifier 能定位首个失败时刻，从最近已验证的 clean prefix 重新生成后缀，通常比每次回到根节点重采样更节省预算。Search controller 持有 prefix lineage、verifier receipt 与 restart budget；生成模型只提出新的 suffix，不能把未验证前缀自行标成稳定状态。

Temporal backtracking 的收益依赖错误可定位且任意前缀可继续生成。Verifier 误判会固化坏状态，前缀恢复也可能需要额外训练；因此定位不可靠、状态无法恢复或轨迹依赖高度全局时，应回退 root-level best-of-N。受限导航和机器人视频任务上的 matched-budget 结果，不构成通用视频质量或物理正确性保证。

<!-- semantic-body-binding:SF-2026-ARXIV-2606.13861 -->

<!-- source-family:SF-2026-ARXIV-2605-24697 -->

AR append-only KV 最容易复用。block 或 editable generation 若修改早期 token，受影响的 attention state 必须重算或版本化。一个安全的 cache key 至少包含：

```text
model + tokenizer/codec + prompt prefix
+ generation algorithm + block/revision identity
+ adapter/quantization + position policy
```

Diffusion 与编辑模型还要进一步区分“持续变化的 sample state”和“整条去噪轨迹不变的 condition prefix”。当
single-stream DiT 以 token-causal mask 表示文本/指令、以 chunk-level mask 表示条件图像，并保证后续 noisy image
只能读取这个静态前缀时，runtime 可以只在首个 denoising step materialize condition K/V，之后复用该前缀；这不是
近似跳过 denoiser，而是利用 mask contract 中已经存在的不变依赖。收益是减少重复 condition compute，代价是 cache
identity 必须同时绑定 model/codec revision、mask layout、condition 顺序、分辨率、sampler/timestep 与 adapter；任一
条件、局部编辑标记或版本变化却继续复用，都会把旧条件静默带入新 trajectory。无法证明这些身份完全相同时，安全
回退仍是每一步重新计算 condition context。当前原始证据只公开作者架构与实现说明，缺少可外推的硬件、并发、SLO
与独立性能复现，因此只支持这一依赖与失效合同，不支持普遍速度或质量优势。

<!-- source-family:SF-2026-QWEN-QWEN-IMAGE-2.1 -->

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


同一 trajectory 内复用状态之外，还可以把其他请求的 latent 当作语义 donor，而不是当作当前请求的有效缓存。一条 text-to-video 分支先匹配 prompt 中的 entity，再用旧视频 latent 的 K/V 与当前 prompt 调制后的 Q 计算 attention；受测实现只替换 denoising steps 2/3/4 的首个 spatial block，避开首步噪声 Q 与后续 block 的污染。它改变了复用的权限：entity 相似只给非 exact 的生成线索，不证明旧 state 对当前请求有效，因此还需校准质量漂移、同步 latent 与检索索引的淘汰，并计入 lookup、驻留存储和错误 donor 的成本。作者主实验预置全部 entity 命中，与另一方法 75% whole-prompt 命中及不同 step 数的比较，不能单独归因于这个接口；时序测试的 entity 命中率降到 52%，也不提供生产负载保证。miss 时完整生成、同请求内的 mutable-cache 路线以及 exactness 优先时的全量刷新仍各有适用条件，多 entry 融合与跨/内请求联合策略尚未解决。[受限证据：arXiv:2602.16132v1]

#### Early convergence 与 high confidence 不是同一个 Commit 证据

并行去噪最初常用当前位置的边际置信度决定是否提前提交；它便宜，却把“这一步很确定”误写成“后续步骤不会再改变”。约束变化是多个位置共同修正时，单点高置信仍可能被后续条件关系推翻。更严格的 runtime 可以追踪一个 token 在连续 denoising steps 中是否已经稳定，把 early-convergence signal 与边际 confidence 联合用于 provisional-to-committed transition。

这会减少不必要的更新，却增加跨步状态、滞回阈值与误提交风险；稳定检测仍不是联合分布正确性的证明。检测不可靠、输出有外部副作用或 exactness 优先时，应延后到 block verifier 或完整 denoising 结束再 commit。该分支补充本章的 mutable-state 路线，不宣称它普遍优于 confidence schedule。[受限证据：arXiv:2605.10980v1]

多个位置各自具有高边际置信度，也不保证它们组成的 joint configuration 一致。一个受限分支在 commit 前加入 pairwise compatibility，并以 mean-field / fixed-point 更新修正各位置的 marginal score；它减少“单点都合理、组合却冲突”的并行提交，但增加二阶计算，且 pairwise 近似仍看不到高阶依赖。短 block、依赖弱或额外校正成本超过并行收益时，保守顺序提交与 target block verification 仍更清楚。作者在特定 discrete diffusion reasoning/code 任务上的结果只支持该近似的局部质量—延迟取舍，不提供通用 joint correctness。

<!-- semantic-body-binding:SF-2026-ARXIV-2606-15805 -->

跨 denoising steps 的稳定还可以和**同一次 forward 的层内稳定**分开。后者比较末层候选在之前若干层是否持续一致，并检查 confidence 是否回落；它减少候选不稳定性，却仍不知道上游未定 token 会不会改变联合答案。一个左到右的提交策略因此再累计当前位置之前、尚未被本轮选择的 masked positions 的熵，只在这个 unresolved-context budget 内接纳候选。累计范围包含未通过候选筛选的位置，而不只是准备同时提交的集合；高置信 token 也不豁免该预算，没有位置通过时再回退局部窗口内的单点提交。

这把单点 confidence、层内 persistence 和上游条件不确定性作为不同观测，而不是 joint correctness 证明。RPD 的[§3–4对照](https://arxiv.org/html/2609.36452v1)支持受测 diffusion LM 的质量—解码时间取舍，但 block变体没有同一全局熵规则，最快配置也并非总是完整策略；减少 NFE 不保证更高 TPS，某些任务完整策略仍慢于 Fast-dLLM。强依赖超出左到右熵proxy、阈值漂移或 verifier 要求 exactness 时，应保留保守顺序或完整 block verification。<!-- source-family:SF-2026-ARXIV-2609-36452 -->

<!-- source-family:SF-2026-ARXIV-2605-10980 -->

#### 逐属性 Commitment 把 Steering 时机变成状态

统一 timestep 施加 steering 的前提，是各属性在去噪轨迹中的形成速度近似一致；它简单、可复算，也不会额外引入属性控制器。离散 diffusion 同时承担内容、风格与安全属性后，这个前提会失效：过早干预尚未稳定的属性会破坏流畅性，过晚干预又失去控制窗口。更稳妥的接口是由只读 probe 估计每个属性的 commitment 进度，再由调度器选择干预时点；probe 只提供观测，不能直接冻结 token 或越过最终生成策略。

逐属性 schedule 用额外探测、校准和轨迹监督换取更细的可控性，也新增 probe 漂移、属性耦合和干预相互覆盖等 failure mode。属性少且形成时机稳定时，统一 schedule 仍是更便宜的基线；校准不足时应回退保守晚干预。`arXiv:2605.10971v1` 的 §3–§5 与 Appendix F 只支持作者的离散 diffusion、属性与延迟设置，不证明这一时序控制可无损迁移到任意生成模型。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-10971 -->

### Cache 误差是沿生成轨迹演化的状态

把 diffusion cache 的误差看成每个 site 的固定 representation mismatch，适合静态校准，却忽略先前修正会改变后续输入。trajectory-consistent calibration 沿 corrected history 逐步估计 site-local prior，使 cache 决策读取当前生成轨迹而非一次性误差表；收益是减少累计偏差，代价是离线 prior、prompt 分布和采样 schedule 共同进入 artifact identity。prior 漂移或未覆盖 cache policy 时应回退 base cache 或 full computation。现有证据只覆盖披露图像模型、H800 与采样路径，不能外推在线并发或分布外 prompt。

<!-- source-family:SF-2026-ARXIV-2605-24870 -->

复用的对象也必须明确。把旧的整个 block output 直接替换当前结果，可能一并抹掉前层刚更新的 residual；一个受限分支只缓存 ATTN/FFN 模块的增量输出，让 residual 路径继续消费当前 input。它在每个 interval 的全算锚点比较各 block feature 的变化，以相邻锚点 CKA 作为排序 proxy，再逐步增加复用范围；相似度并不是删除该 block 的因果收益，也不能取消周期性全算。<!-- source-family:SF-2026-ARXIV-2512-24195 -->

部分 refresh 还要保存 block-specific token 集合：从 warmup cross-attention 选出的集合只在相应 ATTN 分支重算，不能推成所有 FFN 都可局部更新或每步已重新确认语义重要性。[有限图像对照](https://arxiv.org/html/2512.24195v1)中更长 interval、更激进复用和额外局部 refresh 并非所有质量或速度指标单调改善；CKA、聚类、feature 驻留与重算都计成本。模型、condition 或 schedule 改变后应重新校准；细节退步或排序失配时缩短 interval、扩大 refresh，最终回完整计算，不把训练免除误写成校准和缓存免费。

同一个 feature 内部也未必适合使用同一种时间估计。一个受限分支先从参考输入求固定右奇异子空间，对后续 feature `F` 使用投影 `F V_k V_k^T`：这不是对每个新输入重新求最佳低秩近似，而是复用参考 artifact。主子空间分量用 EMA 估计后续变化，正交残差则保持最近锚点的值；低能量不等于对输出不重要，固定 basis、保留 rank 和采样 schedule 都进入 cache identity。参考分解、投影与两份状态增加预处理和驻留成本，更长复用 interval 在有限图像/视频对照中也会降低质量；与其他加速基线计算的 PSNR 不等于对原完整模型的保真。输入漂移或细节退步时应重新校准、增加全算锚点，最终回完整计算或已验收的 whole-feature 路径，不能把 FLOPs 减少直接当作墙钟或并发收益。<!-- source-family:SF-2026-ARXIV-2601-07396 -->

视频生成还可以让 refresh policy 读取 token 的运动强度：静止区域延长复用，运动边界更频繁重算，
从而把固定 cache interval 改成内容条件化的误差预算。motion estimator 只拥有 recompute proposal，
生成器输出与质量 Gate 仍拥有提交权；估计偏差会在快速运动、遮挡或镜头切换处累积，因此需要最大
复用步数和 full-recompute fallback。它用额外运动估计、分支调度与 cache metadata 换减少重算，
只适用于作者受测的自回归视频生成路径，不等同于任意视频模型的无损 cache。
<!-- source-family:SF-2026-ARXIV-2605-01725 -->

多个视频 chunk 同时处于去噪时，全局 step 又不足以描述缓存年龄。每个 active chunk 应分别记录自己的 denoising phase、全算锚点和累计 displacement；一条经验分支先在各 chunk 的早期阶段强制重算，再累计相邻状态的相对变化，超过阈值便刷新该 chunk 并重置计数。另一路历史预算只管理已经完成去噪的 clean KV：它与 active denoising KV 分区，chunk 完成后再合入历史并在有限预算内选择。这分开了中间计算复用、未完成状态与已完成历史压缩，不能让同一全局时刻替代各自的 cache identity。<!-- source-family:SF-2026-ARXIV-2602-10825 -->

分区、阈值累计与历史选择增加 metadata、selector 和驻留成本，两种近似还可能叠加质量损失。[FlowCache 的受限视频对照](https://arxiv.org/html/2602.10825v1)中，chunk reuse 与进一步 KV 压缩的 PhysicsIQ 均低于完整计算，局部感知分数保持不授物理一致或无损历史；原文的单调性推导也不足以建立一般误差保证。运动突变、条件改变、质量或预算回归时，应逐 chunk 强制刷新、扩大历史预算，最终回退完整计算与完整历史；不同 backbone、chunk 长度和去噪步数需要重新校准，不把缓存倍数直接当线上 SLO。

固定 cache schedule 还假设不同 sample 与 timestep 对误差同样敏感；当生成难度和 denoising phase 变化时，这会在简单样本上浪费重算、在高敏感 step 上累积偏差。另一分支把 `reuse / recompute` 建模为 trajectory-conditioned sequential decision，并将 policy 与轻量 error corrector 分开：前者分配计算，后者只修正已选择复用的状态。二者必须共享 state/step identity、quality budget 与 fallback frontier，不能用 policy confidence 代替 correctness。

学习式 cache control 用额外训练、policy drift 与 corrector bias 换取 sample/timestep 自适应；prompt 分布、sampler 或 backbone 变化后需要重新验收。事件时证据覆盖 FLUX.1-dev、DiT 与 CogVideoX 的作者配置，不能把 headline speedup 外推为生产并发收益；低流量、短 trajectory 或校准不足时，固定 schedule 和 full recompute 仍是更可验证的基线。<!-- source-family:SF-2026-ARXIV-2607-29398 -->

### Velocity Decomposition 以周期性 Full Forward 约束近似误差

<!-- semantic-body-binding:SF-2026-ARXIV-2605-23381:start -->
每个 denoising step 完整前向最容易保证状态一致，却重复计算变化缓慢的分量；velocity-decomposition 分支在周期性 full-forward anchor 之间估计中间 step，把 anchor interval 与估计状态写入 sampler identity。近似只拥有 proposal，误差 Gate 决定是否继续复用。

减少前向次数会换来累积误差、interval 调参与分布漂移。exact-v1 只支持作者模型、schedule 和测量；误差超界、场景变化过快或质量回归时，应缩短 interval，最终回退完整 denoise。arXiv:2605.23381v1
<!-- semantic-body-binding:SF-2026-ARXIV-2605-23381:end -->

### Diffusion Serving 不能直接复用 AR Token Queue

AR serving 的 ready unit 通常是“某请求的下一个 token”；masked diffusion 在同一 denoising step 共同更新多个位置，step difficulty、收敛进度和 CPU dispatch 成为新的状态。Batching 的收益来自多个请求共享一次 step forward，而不是把它们简单塞进同一 token queue；admission 需要同时约束 mask ratio、remaining steps、output budget 与 quality policy。它提高并行机会，却引入 step-level straggler、批间不同步和 dispatch overhead；短输出或单请求时，普通逐请求执行可能更简单。`arXiv:2608.23807v1` 的 LLaDA-8B + D2F LoRA、单 H200、GSM8K/HumanEval 只支持该 operating point，不能证明质量对任意 batch 都不变。

<!-- source-family:SF-2026-ARXIV-2608-23807 -->

视频编辑还面临另一种迁移：离线双向 diffusion 能看到完整片段，直播编辑只能读到当前及历史帧。直接把离线编辑分支接到因果 backbone，会让源视频跨帧条件偷看未来，且两种 backbone 的 feature space 不一定对齐。一条受限路线先冻结生成 backbone，让控制分支按帧独立编码输入，并将控制更新方向与双向→因果转换的主导方向分离；这样学到的编辑条件才有机会转移到流式模型，而不是把整个视频编辑器重新训练一遍。收益是重用离线控制能力，代价是受限的跨帧条件表达、特征正交近似和转移后的时间一致性风险。已知未来全片、质量优先时，原双向编辑仍更适合；严格实时且原模型表征不兼容时，专门训练因果编辑器仍可能更可靠。单 H100 的作者流式速度只属于其任务与配置，不构成生产帧率保证。<!-- semantic-body-binding:SF-2026-ARXIV-2609-24788 -->

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

### 先定位真正承载语义的生成窗口，再讨论动态调度

把每一个 denoising step 都视为同等重要，最容易实现和复现，也能避免误删关键计算；它的代价是即使某些阶段几乎不依赖条件输入或全局交互，系统仍支付完整 guidance 与通信成本。一个更谨慎的演进不是直接学习“哪些 step 可以跳过”，而是先把 conditional/unconditional score gap 与 global/approximately-local score gap 当作诊断信号，再用 windowed intervention 检查：只在某段时间移除 conditioning 或全局交互时，最终语义和结构究竟何时显著受损。

这类 critical-window 证据可以帮助划分阶段预算，却不授予 runtime 自动跳过计算的正确性。诊断 owner 只提出“哪些窗口可能 load-bearing”，scheduler 仍须绑定 sampler、模型、分辨率、condition identity 与质量门来选择计划；窗口漂移、局部算子并不真正局部、或条件之间存在耦合时，应回退全程计算。现有结果只覆盖 ImageNet DiT-XL 与 SD3-medium，且截断 attention 只是近似 local denoiser；两个 critical window 的接近是受测配置中的经验观察，不是所有 diffusion trajectory 的普适定理。<!-- source-family:SF-2026-ARXIV-2605-04830 -->

图像或视频 diffusion 还可以把 patch granularity 变成 trajectory policy：早期或低变化阶段使用 coarse patch，细节阶段回到 fine patch。这里必须分开两层：artifact 先通过训练获得多种 patch shape 的语义能力，runtime 才能依据 latent history 和 threshold 选择 shape。“选择规则在 test time 运行”不等于整个方案 training-free。

这种 adaptive granularity 减少单请求 token 数，也新增 latent-history state、threshold calibration、shape switching 与多分支 artifact identity；不同请求选择不同 shape 时，还可能破坏 batching、graph capture 与 kernel reuse。固定 fine patch 在 worst-case detail、可预测 shape 和成熟 kernel 场景仍成立。若论文的 threshold table、hardware、precision 或配置记录相互矛盾，Books 只能吸收机制与 failure mode，不能吸收精确 speedup。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-22050:start -->
生成完成后再运行 copy detector 并重试，在检测器可靠、重跑成本可接受时最容易隔离状态；固定 guidance、prompt 或 latent 调整也保持控制面简单，却不能随当前 trajectory 的异常强度变化。若目标是保留当前 denoising path、同时更早压制潜在复制，可以从 clean reference prompts 为每个 timestep 与模型版本冻结 latent update、latent norm 和 reconstructed initial-latent 的经验区域。Sensor 只报告轨迹偏离强度，sampler controller 才能按预先定义的 mild/strong policy 对 provisional state 做有界 rescale；独立 copy、provenance 与 privacy gate 仍拥有最终 acceptance。

这条路径避免每次 abort-and-regenerate，却增加 reference distribution、threshold、逐 step 状态与漂移风险：正常但稀有的样本可能被压回均值，不呈相同动力学的复制又可能漏过。Out-of-region 不是训练记录身份，in-region 也不证明安全，更不证明权重已经删除数据。Reference coverage、false-positive rate、copy audit、semantic fidelity 或 scheduler transfer 失败时，应停用 adaptive projection，回退 detect-then-retry、已验证静态 sampler、独立来源检查或训练侧 filtering/unlearning。现有证据只覆盖论文披露的 Stable Diffusion、sampler、校准集与 SSCD-style 指标。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-22050:end -->
<!-- source-family:SF-2026-ARXIV-2605-22050 -->

控制也可以作用于生成网络内部的 activation，而非只缩放 latent trajectory。在不改 base weights 的部署分支中，先用 source/target prompt 双路径比较指定 FFN 层的 importance，按阈值及 source 小于 target 的条件构造 mask，并保存 source activation 的均值；新去噪路径只在 masked 位置注入该冻结值，其余位置保留当前 activation。这是推理时的条件性 patch，不是删除训练数据、权重中的概念或版权信息；model revision、层集合、准备 prompt、阈值、去噪 schedule 与 mask/activation artifact 必须共同标识这次干预，不能跨模型或路径静默复用。

单概念 patch 有效也不授权任意组合：多概念 mask 的逻辑 OR 会扩大覆盖，重叠位置的 source 值平均又改变了注入分布，原有限实验中十概念组合已出现明显生成退化。因而组合后的抑制指标、非目标语义与画质必须重新验收，不能把若干单项测试的通过相加成完整安全保证。training-free 只表示没有参数训练，仍有双路径准备、artifact 保存与逐步注入成本；当前证据仅为作者 Stable Diffusion 1.5、有限 detector/攻击集与质量指标，正文和附录的 step 配置不一致，不采用统一复现 recipe 或生产 SLO。换 schedule、模型或组合后回归时，应停用该 patch、恢复已验证 sampler，并保留独立内容与来源检查；activation patch 不能接管最终安全 acceptance。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-07701:start -->
固定 classifier-free guidance scale 在任务和各去噪阶段的控制需求近似稳定时最容易复现；离散文本 diffusion 中，过强 guidance 会牺牲流畅性与多样性，过弱又无法满足任务约束，而且合适强度会随 provisional state 改变。可把每一步的 scale 视为有界 action，让 policy 读取当前 diffusion state，在 task-level reward 下学习 guidance trajectory；sampler 仍拥有 token revision 与 commit，policy 只提议控制量。

该分支用额外策略训练、状态编码和 reward coupling 换 task/step 自适应，也新增 policy drift、terminal-reward shortcut 与不可解释的早期锁定。任务、sampler 或 reward revision 改变而未重新校准时，应回退固定 CFG 或保守 heuristic schedule。exact-v1 的结果只支持作者所测离散 diffusion 任务，不证明动态 guidance 会取代固定 guidance。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-07701:end -->

奖励引导还需要明确奖励模型看到的输入与生成器收到的梯度是不是同一对象。直接用 token 概率的平均 embedding 可以平滑反传，却可能偏离只见过离散 token 的奖励模型训练分布；改为 hard token 并用 straight-through 反传，则前向输入与代理梯度又不一致。一条折中分支按归一化 token entropy 混合 soft 平均和采样 token embedding，前向在高 entropy 时更靠近离散输入，反向通过 stop-gradient 仍只沿 soft 路径。这控制的是 embedding 近似与输入分布的取舍，不证明无偏离散奖励梯度，也不把 entropy 变成答案正确率。生成器与奖励模型的 tokenizer、embedding 接口、temperature、优化步数和 token commit 策略需要共同标识；白盒奖励模型反传增加推理成本，更高自身奖励也可能伴随外部质量或多样性下降。现有证据限于兼容 tokenizer 的 Dream 与 Skywork 奖励模型组合，增加优化步数并非单调改善；兼容性、独立质量验收或预算不合算时，应保留普通 sampler 或 best-of-N，而不是把奖励分数的上涨当作自动通过。<!-- source-family:SF-2026-ARXIV-2602-05000 -->

减少 guidance 的双路径求值还有一条训练侧替代：在同一 noisy input 和 time 上，为较浅层增加受训的线性 readout，让它与最终输出预测相同 clean/velocity 对象。若较浅输出为 `D_i`、最终输出为 `D_f`，推理可以取 `D_i + w(D_f-D_i)`，用同一次 backbone forward 的内部深度差作为弱参照，而不是另跑无条件分支。这要求 checkpoint 在训练时加入相应辅助损失；不能把任意中间 activation 当合格 denoiser，也不是现成模型无需适配即可免费减少求值。<!-- source-family:SF-2026-ARXIV-2512-24176 -->

共享 forward 也共享误差：内部参照不提供独立真值，较深 readout、更多 heads、更强外推或更长作用区间并非单调改善。[必要图像对照](https://arxiv.org/html/2512.24176v1)中的可选 stop-gradient/EMA 训练目标与推理 guidance 是两种参数权限，不应合并归因；新增 head、辅助训练和校准仍付成本。数据、模型或 sampler 改变后需复查质量与多样性，内部差值失配时关闭外推、回原 denoiser 或成熟 CFG。有限 toy 分布及作者图像模型不能证明普遍 manifold 因果、所有质量保持或生产吞吐。

#### Guidance 可以前移到 Prior，但误差会集中到初始状态

标准 classifier-free guidance 在每个 velocity evaluation 都运行条件与无条件分支，语义清楚但网络求值翻倍。条件 prior 分支把 guidance control 前移到初始噪声分布的均值/方差，用小型 prior 完成一次 steering 后执行单 pass sampling；runtime 由此减少 forward count，却把条件逼近误差集中到 prior artifact、guidance scale 与 sampler identity。

这种替代只在一阶近似和校准范围内接近标准 CFG，并新增 prior 漂移与初始偏差难以逐步修正的风险。guidance scale 越界或质量下降时，应回退 dual-pass CFG，两者可按 workload 共存。`arXiv:2605.06124v1` 的实验限于 MNIST、CIFAR、ImageNet 256、U-Net/DiT-B/2 与单 RTX4090；作者延迟不能外推生产并发或 tail SLO。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-06124 -->

运动condition还能同时改变不同模态的生成初态与控制输入。仅把同一文字prompt送给video/audio两支，实现简单，却未规定二者的运动时序为何一致；一个条件分支把同一2D轨迹用于视频局部flow endpoint，同时把position、velocity和acceleration等运动量送入音频condition。首帧latent沿轨迹搬运，运动区外仍从Gaussian出发；sparse轨迹区以soft mask和区域均衡loss避免被背景面积稀释，音频gate控制初始干扰。<!-- source-family:SF-2026-ARXIV-2604-09057 -->

共享运动状态换同步控制，却引入trajectory抽取、latent搬运、区域权重和双模态训练耦合。[受限AV实验](https://arxiv.org/html/2604.09057v1)的video-only和audio-only配置在不同指标各有优势，joint不全面最好；2D tracking和motion/audio相关也不证明物体质量、接触、3D动力学或空间声学真值。轨迹有误、场景不支持latent搬运或单模态质量优先时，独立生成和原noise prior仍可保留；物理反馈由World Model/Embodied章节另外验收，不能从同步画面直接推断可执行世界。

参考视频提供的运动还可能带着原主体的形状，不能直接把它当成目标对象应遵循的轨迹。一条参考控制分支先由reference cross-frame attention的Top-K对应抽取运动field，再用目标foreground mask与视觉feature建立source→target匹配、消解冲突，并把warp后的field交给latent guidance；后续生成因此消费的是经过形状对应的motion proposal，而不是target语义或真实运动的证书。抽取、mask、匹配、平滑和guidance优化均付准备与执行成本，需共同绑定reference/target、坐标、frame、feature与去噪step身份；attention对应错位时，后续warp可把源形状错误持续传入目标，更强guidance本身不能证明对应已修复。有限motion指标与人工偏好测的是不同对象，也并非所有消融都支持完整分支更好；对应不稳或成本/质量不合算时，保留无参考的原生成器与直接轨迹条件，并按目标质量分别验收。<!-- source-family:SF-2026-ARXIV-2601-01955 -->

多事件视频还有另一种时间错配：把叙事拆成逐段短prompt，动作更容易出现，却会在分段生成与拼接时丢主体和背景的连续性；保留完整prompt，则同一帧的视觉query可能同时读取几个互不相干的动作。若事件区间已给定或可粗略规划，一条条件分支保留完整文本作为共同context，只在较早去噪阶段调整cross-attention：由subject词的注意力估计运动区域，使该区域内属于当前帧区间的query强化对应event tokens、削弱其他event tokens，未归入事件的文本仍作全局条件。这是**条件消费的时序路由**，不是删除其他文字、重写生成状态，也不是让attention map取得物体位置真值。<!-- source-family:SF-2026-ARXIV-2604-19473 -->

局部bias减少多事件干扰，却依赖事件分段、subject词定位和运动mask；分段错位会把正确动作压错时间，背景或多主体被误mask也会破坏一致性。它还增加attention探测与规划调用，受限Wan/CogVideoX实验的作者评分和单A100、81帧时间比较不能外推生产并发、物理可信度或tail SLO；多prompt基线生成帧数也不严格相同。无法可靠分段、mask不稳或成本/质量验收不通过时，保留无bias的完整prompt、短段生成或人工时间脚本，不能把局部路由当作视频生成的统一默认值。

条件消费的时序路由与可编辑的事件状态，还可以作为两条替代分支。音效生成若把事件位置、时段和声音属性显式保存，再为每个事件独立生成segment并混合，编辑时就可以仅增删、retime或重新生成对应track，而不必重做全部内容；图像/视频推断的定位仍是proposal，不是声音来源或接触事实。该模块化路径适合局部创作，却可能把遮挡、多声源和混响关系拆错，独立segment也不自动保跨事件声学一致性。视频推理的外部API、多个生成调用、混合及人工校正都付费，单次音频生成耗时不能代表全链延迟；定位失配或强耦合声场下，保留人工事件脚本、整体生成与联合校正，不凭有争议的时间/音色/音量评分认证生成质量。<!-- source-family:SF-2026-ARXIV-2512-24731 -->

相机条件还有一个训练期问题：静态或多视角数据容易取得 degraded rendering 与真实目标的配对，野外单目视频却没有每条新视角轨迹的真值。一条替代分支先从稀疏关键帧重建动态 Gaussian，并在短邻域近线性运动假设下插值；训练时用新相机轨迹做可见性裁剪与不同宽度的深度均值滤波，再把退化结果 render 回原视角，以原视频作为监督。RGB、depth、空区 mask 与相机 embedding 送入 control branch，冻结视频生成 backbone，只训练条件消费路径。这使单目数据可用于学习合成退化修正，但补出的细节仍是生成假设，不是新视角几何真值；重建、渲染与控制分支也增加准备和训练成本。遮挡、关键帧间隔或缺乏三维线索的二维图像超出假设时，应保留真实多视角监督、直接几何基线与独立几何验收，不能用画质改善宣称物理一致。<!-- source-family:SF-2026-ARXIV-2601-00393 -->

与训练退化修正不同，静态场景的相机轨迹还允许改变交付视频的计算分工：不为每个 frame 执行 diffusion，而先生成少量关键视图，从生成视图重建并对齐 3D Gaussian，再沿目标相机轨迹渲染密集 frames。一条受限实现由首图与 poses 预测关键帧数量，再均匀选取位置；数量预测不等于学会原 coverage 算法选出的具体位置，更不证明全像素可见或最优覆盖。生成器只提出稀疏视觉内容，几何重建和 renderer 消费其结果，不把生成画面提升为真实三维或 persistent world state。<!-- source-family:SF-2026-ARXIV-2601-09697 -->

这一分工可摊销静态新视角视频的生成成本，却新增 count predictor 的训练、稀疏视图生成、重建、affine 坐标对齐及 chunk 衔接成本；affine 拟合不是物理位姿证书，局部 chunk 也不证明全局长程一致。公开 GH200、256²、静态相机视频只支持作者的局部质量/资源取舍：插值时间不能替代包含关键帧与重建的端到端时间，部分 FID 对照退步、无 chunk 的 FVD 也较原生成器更差。动态物体、遮挡空洞、模糊细节或坐标漂移超出该分支时，保留密集相机条件生成、普通 I2V 或真实多视角重建；不能由画质或渲染速度推导物理可信度与生产 SLO。

增加新 pose 是扩大视角覆盖的一条合理路径，但若稀疏输入留下的主要空洞位于原视野边缘，也可以固定外参、缩短焦距扩展 FOV。此时必须同步更新光线与几何对应条件，将原输入保留在新视野中心；粗重建图像编码成 latent 后，加噪到当前相同噪声尺度，再按空区 mask 与生成 latent 混合。生成器补内容，重建器消费这些 proposal，两者都不因 pose 固定而获得未知几何真值。

[这一受限扩视野分支](https://arxiv.org/html/2512.25073v1)仍需粗 3DGS 训练、重采样和最终 refinement；没有微调 denoiser 不代表整个链路免训练。Opacity mask 也不是几何正确率，粗结构错位或所有输入均遮挡时，生成与再训练会传播同一错误。质量指标与混合频率有相反取舍，不能把一种画质提升当成统一改善；支持不足时保留真实新视角、直接几何重建或原密集生成，另行验收几何和完整成本。<!-- source-family:SF-2026-ARXIV-2512-25073 -->

相机控制与动画内容的时间还应分开：输出frame index描述要交付的序列位置，不等于场景内容所处的动画时间。将source/target各自的camera与animation-time分别编码，时间压缩器再把RGB帧时间映射到latent步，才能表达同一运动的retime与新视角，而不是用一个position index兼任两种控制。该路径依赖temporal warp监督与合成camera×time网格覆盖；估姿和首段尺度对齐只是评价协议，不是绝对metric或真实三维真值。网格构造、时间压缩与条件训练都付费，有限画质/位姿指标不授任意4D一致、persistent world state或生产SLO；时间支持不足、估姿不稳或跨camera对齐失败时，保留原动画时钟、固定相机与单控制分支。<!-- source-family:SF-2026-ARXIV-2512-25075 -->

<!-- semantic-body-binding:SF-2026-ARXIV-2605-06667:start -->

### Camera 与 Motion Condition 可以在 Denoising 中分阶段交接

固定 camera 或 pose-only control 在单主体、镜头简单时更稳定；同时强加 pose 与 depth 到所有 denoising step，可能在后期把局部运动和高频细节过度约束。一个条件分支让早期 pose+depth 锁定 global geometry，后期只保留 pose，使 camera/depth control 在粗结构收敛后交还给 motion/detail generator。Condition scheduler 只拥有约束强度，生成状态仍由 denoiser 更新，独立几何与运动 gate 决定是否接受。

分阶段控制改善相机遵循与动作自由度的取舍，也会引入 pose/depth 校准误差、切换时刻敏感、遮挡和多角色冲突。现有证据只覆盖固定 backbone、作者 benchmark 与 human preference，不证明真实 3D consistency。输入对齐或 schedule 失稳时，应回退 pose-only、固定 camera 或训练式 controller。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-06667:end -->

中间几何也可以先生成，再交给外观分支消费，而不只是随去噪时刻减弱已有 depth 条件。一条受限视频分支在共享 DiT 中排列 depth 与 RGB 两个 latent 流，各用自己的 timestep 调制；训练轮流固定 RGB 为纯噪声去预测 depth，或固定 clean depth 标签去生成 RGB。部署先完成 depth，再固定这份预测、重新初始化 RGB 噪声执行第二条去噪 loop。稀疏对象点与相机重投影只提供控制线索；截断或删去部分轨迹后恢复完整 depth 是训练支持，不把生成几何批准为观测事实或已学物理定律。

[Motion Forcing 的有限视频对照](https://arxiv.org/html/2603.10408v1)支持这项生成条件交接，运动和物理 proxy 改善仍伴 FVD 反退；不同输入与两阶段工作量不构成所有变量相同的因果对照。训练消费 clean depth、部署消费预测 depth，几何误差和域外编辑需要分别验收，能查看中间结果不等已有 verifier。点/相机/深度标签制备、共享模型训练、两个 latent 流和两条采样 loop 都付费；密集小对象、遮挡或条件支持失配时，保留单阶段 I2V、更明确的控制与独立几何/视频检查，而不由画面逼真批准 World Model 的动作后果或机器人执行。<!-- source-family:SF-2026-ARXIV-2603-10408 -->

控制信号还可以按它提供的信息拆开，而不让一套 dense pose 同时承担对象外观和交互位置。一个视频生成分支用腕点与不含形状的对象 box 描述稀疏运动，另给对象 reference、整场景 reference 与遮罩背景；冻结原生成主干，在克隆的条件分支中按空间/时间接口组装并注入残差。对象参考 tokens 的 attention logits 可被额外放大，使外观线索更易参与去噪；这改变条件的竞争权重，不把 box 或更强 attention 变成合法接触、形变或物理转移约束。训练时对 motion/background 条件作随机缺省，让同一接口支持编辑、首帧或首尾条件，但缺省能力仍依赖训练支持。

[受限交互视频对照](https://arxiv.org/html/2603.09883v1)支持稀疏条件与参考外观分责，不认证真实 world state、任意对象或低总成本。不同基线读取的骨架、音频及编辑结果并不相同，辅助训练又增加数据，质量指标也并非全部改善；须分别验条件遵循、对象保形、运动和最终视频。原主干虽冻结，条件分支训练、参考/遮罩构造、VAE与每步去噪仍计费，缺省/尺度/坐标和模型版本须共同绑定。非刚体、复杂形状分割或训练支持失配时，保留更密集的pose/depth、原inpainting/专用控制和独立视频验收，不用逼真画面批准实体交互或机器人动作。<!-- source-family:SF-2026-ARXIV-2603-09883 -->

多对象控制还可按运动假设分配跨帧读取，而不对所有实例使用同一种 guidance。一个受限分支先从 motion graph 提出逐帧 box 与类别：静止区域读取同一参考帧，刚体区域读取对齐的共享形状模板，非刚体区域则比较 feature 对应与 box 推得的局部位移。这改变条件的 support 和软偏好，不把 2D box、nearest-neighbor 对应或 attention 修改变成真实刚体、形变或硬运动约束。[有限两主干对照](https://arxiv.org/html/2603.09104v1)还依赖防实例遗漏的原控制模块，较高运动幅度可伴其他质量损失，类别错误、罕见语义和视角变化仍可能失败。Graph、模板、对应搜索、额外优化与调参均付费；混合运动、遮挡或条件验收不可靠时，应保留统一 guidance、更明确的参考/pose 与原生成路径，而不是从 training-free 推出任意对象可控。<!-- source-family:SF-2026-ARXIV-2603-09104 -->

对象参考还可以同时含静态图像与动态视频，而不把两者默认为同一时间条件。一条受限分支先将图像 feature 沿时间广播、将视频 feature 重采样到目标时间，再按各对象的位置和尺度逆向 warp 到共同的 latent canvas；模态 mask 声明来源，重叠时由用户指定的前景优先抑制背景条件。这分开了参考内容、时间对齐与空间布局，不把 tracker 的尺度、可见性或软遮罩提升为真实遮挡和硬运动约束。[有限图像参考对照](https://arxiv.org/html/2603.08850v1)支持控制接口，动态混合参考仍只有定性评价，文本一致性也可退步。分解、tracking、codec、全模型适配与采样都付费；小对象、遮挡、参考冲突或时空对齐失配时，保留单参考、显式 mask/pose 与原条件路径，不由组合 canvas 签发背景严格不变或实体交互正确。<!-- source-family:SF-2026-ARXIV-2603-08850 -->

## 生成后训练：轨迹概率、反馈与信用分配

控制 guidance 不等于更新生成器；后者必须先把采样路径上的概率、评价对象和信用分配说清楚。这里保留生成过程的语义边界，PPO/GRPO 等优化规则与训练系统实现交给 Part IV。

Expert图像监督还可以随当前policy样本更新一个discriminator，而不是固定SFT目标或把其分数当独立真值。若反馈可微，一条受限路径以local-linear single-step denoising近似连接终点评分与vector field；若只消费scalar反馈，则以CFM loss差构造ratio surrogate进行更新。这两种接口决定训练梯度路径与费用，不是同一个flow likelihood，也不把实际近似变成exact或无偏policy gradient。[必要实验](https://arxiv.org/html/2602.12155v1)中scalar路径在较长训练后可collapse，可微路径也并非相同预算下每项更好；expert/current-policy配比、BC启动、CFG评价配置与discriminator版本须分开验收。Expert生成/过滤、在线rollout、discriminator训练和反传均付费，代理reward上涨不认证真实偏好或消除hacking。近似、专家支持或质量/预算不成立时，保留原SFT、固定guidance或受控外部reward，PPO/GRPO更新规则仍交Training owner，不照搬完整flow surrogate等价。<!-- source-family:SF-2026-ARXIV-2602-12155 -->

少步且确定的生成路径还可以把终态反馈移交给可微 surrogate：在冻结当前 condition、sampler 与后续映射下，把 noisy state 续推到 endpoint 并取得外部 scalar 评分，再让 surrogate 按组内 advantage 的方向与绝对标准化权重学习；更新 generator 时停止 surrogate 参数梯度，但下一轮仍重训它，不能混成永久冻结 reward model。确定续推只消去该固定映射下的 continuation 随机性，不认证 reward 真值、surrogate 无偏或 joint loop 收敛。[TDM-R1 的受限对照](https://arxiv.org/html/2603.07700v1)提供这一替代分支，模型 proxy 与 EMA reference 不替独立质量评价，局部消融也未完整匹配总预算。Endpoint rollout、surrogate 与 fake-score 更新、reference 与额外梯度均计费；评分或分布漂移、代理过拟合或质量回归时，保留原监督/固定 guidance、可信外部评价或可执行的 terminal-RL 分支，不由低方差提名自授偏好保持。<!-- source-family:SF-2026-ARXIV-2603-07700 -->

### Reward 更新需要先定义采样路径上的 Policy

调节 guidance 是在既有生成器外选择控制量；直接更新离散 flow 的 rate model 则需要另一种概率接口。它输出转移速率，并不直接给出最终样本的 likelihood，因而不能照搬 AR 的最终序列 ratio。一条分支先把当前时间和离散状态作为内层 MDP 的 state，将下一状态作为 action；在合法 Euler 步长下，跳转概率为 rate×步长，留在原状态的概率为一减去总离开概率。这样 policy 拥有的是一步转移概率，terminal reward 才评价完整样本，policy gradient 可沿实际采样轨迹计算，而不必先估计难算的终态 marginal。<!-- source-family:SF-2026-ARXIV-2604-06491 -->

代价是额外 rollout、reference 计算、轨迹方差与步长耦合；概率非负和归一化不成立时，这条接口本身就无效。离散轨迹上的目标等价不意味着连续时间过程无离散误差，路径约束也不自动等于终态分布约束。[原始方法](https://arxiv.org/html/2604.06491v1)提供这种构造，经验验证仅为特定DNA生成与代理reward，不支持文本质量、物理有效性或服务SLO；本章只吸收一般概率接口，不开展AI for Science领域路线。缺少可靠reward或质量回归不通过时，预训练flow与固定guidance仍是基线；PPO/GRPO的更新规则由Training章节拥有。

### 融合逆条件分布不等于融合模型参数

多个目标各自训练后，组合接口还可以是同一reference下的局部reverse conditional，而不是平均参数或随机换模型。共同reference policy、相同KL温度、各base达到局部step surrogate最优、Gaussian逆条件以及非负归一化权重成立时，weighted product可由precision加权均值/方差闭合。这个闭式只说明局部概率接口；它不是原terminal-reward RL的全局最优证书，也不允许省略reference、variance与所优化目标的兼容性检查。

`arXiv:2604.14379v1` 的 MSDDA 经验base用DPOK，没有证明达到全部surrogate最优条件；各base每步仍要执行，无新训练不等无推理开销。受限SD1.5/DrawBench颜色及新组合prompts、每prompt32seeds和ImageReward/VILA评价中，w=.8的一项reward .65低于CoDe .66，不能据不完整执行配置宣称全面支配或生产秒数优势。Reference/温度不兼容、局部Gaussian近似失效或额外求值不合算时，单个已验收模型与原固定guidance仍是透明的共存路径；最终样本质量需独立验收，不能由融合定理代替。

<!-- source-family:SF-2026-ARXIV-2604-14379 -->

### Diffusion RL 的 Credit 可以沿 Denoising Trajectory 分配，但 Reward 仍须可验证

<!-- semantic-body-binding:SF-2026-ARXIV-2605-15458:start -->
只对最终视频打分的 RL 在 evaluator 可靠、生成步数少时实现简单，却无法指出哪一段 denoising trajectory 破坏了全局结构。SDE-GRPO 把 flow/diffusion 采样写成随机轨迹，在组内比较结果并将 credit 分配回中间步骤；对 maze、FlowFree、Sokoban 这类可由程序验证的任务，还可提高早期步骤的权重，因为全局布局通常先于局部纹理形成。sampler 拥有生成 trajectory，reward program 拥有任务判定，step schedule 只拥有 credit weighting。

更密 credit 以额外 rollout、轨迹存储和方差估计为代价；早期加权会牺牲局部质量，并可能让模型利用 verifier 漏洞。exact-v1 的 §4.1–4.3、§5.1–5.4、§6.1–6.3、§7 与 Appendix C.1 只支持这些程序可验证任务，不证明开放视频语义或人类偏好同样可分解。reward 不可验证、trajectory 成本过高或局部质量回归时，应回退监督训练、固定 schedule 或仅在终态使用独立 evaluator。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-15458:end -->

<!-- semantic-body-binding:SF-2026-ARXIV-2605-22967:start -->
长 denoising trajectory 的端到端反传保留完整依赖，却让显存和计算随展开长度增长。Learned relay state 可以在
阶段边界压缩前段信息，再对后段执行 truncated BPTT；它把优化压力从保存全部状态转成维护 relay-interface
fidelity 与 stage revision。收益是有界反传窗口，代价是未编码依赖丢失、阶段兼容和额外 relay compute。作者
实验不证明任意 diffusion process 都能无损截断；relay validation 或跨阶段一致性失败时，应回退 full backprop、
更短 unroll，或使用可检查的静态显式 state。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-22967:end -->

### SDE-consistent RL 必须绑定 Exploration 与 Finite-step Transition

<!-- semantic-body-binding:SF-2026-ARXIV-2605-23522:start -->
只优化 ODE 或终态 reward 时路径简单，但不能显式控制随机 exploration；SDE-consistent 分支把 exploration schedule、有限步 transition 和 reward rollout 共同版本化，使训练采用的随机过程与实际 sampler 更一致。Reward 仍只评价披露目标，不能替代生成正确性的独立 Gate。

随机轨迹提高探索，却增加方差、稳定性和近似误差。exact-v1 只支持作者假设、sampler 与实验；transition 近似失真、方差失控或质量退化时，应回退 ODE、既有 sampler 或监督训练。arXiv:2605.23522v1
<!-- semantic-body-binding:SF-2026-ARXIV-2605-23522:end -->

### Metric-geometry Reward 只能提出几何改进方向

<!-- semantic-body-binding:SF-2026-ARXIV-2605-23903:start -->
单一视觉 reward 容易混合 rotation、translation 与外观质量；metric-geometry 分支把几何分量分账，并让 3D estimator 产生 reward proposal。Estimator 不拥有真实几何，最终仍需传感器、可执行约束或独立几何 Gate。

更细 reward 改善 credit assignment，却可能被 generator 利用 estimator 漏洞，或在域外相机和场景上失配。exact-v1 只支持作者数据、GRPO 和 estimator；sensor 不可靠、几何回归或 reward hacking 出现时，应回退 SFT、确定性几何检查或不启用该 reward。arXiv:2605.23903v1
<!-- semantic-body-binding:SF-2026-ARXIV-2605-23903:end -->

## 从一次生成到 Plan → Generate → Validate → Retry

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

音频生成提供了另一条层级分支：粗粒度 acoustic token 由 AR 路径负责长程结构与条件一致性，细粒度
token 再用固定步数并行补全局部质感。它把“所有声学细节都串行生成”改成 coarse commit 与 fine
refinement 两级状态，用更低串行深度换取 tokenizer 层级、跨层对齐和并行补全误差。结构错误必须回退
重生成 coarse stream；只修细节不能挽救节奏或语义。作者 human arena 与消融只支持其模型、tokenizer
和音乐任务，不证明该 factorization 可直接迁移到语音、任意采样率或生产延迟。
<!-- source-family:SF-2026-ARXIV-2605-01790 -->

这里的 plan 是 provisional control state，不是模型已经正确理解约束的证明；validator 也必须拥有版本、阈值、
false-positive/false-negative 与覆盖范围。Retry 若复用同一错误 plan 只会重复失败，若完全重建则增加 latency、
compute 和 output variance；streaming 一旦播放前缀，rollback boundary 还会变成用户可见协议。小模型、低风险、
严格 latency 或 validator 不可靠时，direct generation 与简单 post-filter 仍然成立。

视频 plan 还可以把一个现象拆成有顺序的事件条件，而不让单一 prompt 兼任全部时间位置。一个受限分支用检索到的公式和推断参数提出事件与 scene graph，再逐事件修订描述、编辑 keyframe，并按预测时间跨度在 latent 中插值作为带噪生成条件。公式、事件和视觉 anchor 分别承担约束、顺序与外观责任，但参数仍由模型猜测，线性过渡也不保接触、守恒或真实因果。[有限事件视频对照](https://arxiv.org/html/2603.09094v1)只支持这条时变条件接口；自动物理评价不是 action-conditioned transition 证据，更多事件还可能积累编辑错误，多物理组合与部分指标仍失败。检索、推理、逐帧编辑、编码、视频采样和独立验收均付费；事件、时间或条件不可靠时，保留单 prompt、可信 keyframe 与原生成路径，不把可看的事件链批准为可执行世界模型。<!-- source-family:SF-2026-ARXIV-2603-09094 -->

触发重试与消费诊断内容也必须分开验收。判定“不满足”后重新采样，可能只因换了随机样本就改善，而没有按 rationale 修改目标区域；因此应在原请求不变时，有界扰动诊断中的关键语义，观察修改是否随内容改变。一种受限路径先把请求拆成可检查的视觉 tuples，再将逐项判定转为明确 edit 指令，以包含反馈和局部纠正的监督训练建立消费接口；judge 提供的观察仍不是独立视觉真值。<!-- source-family:SF-2026-ARXIV-2604-13491 -->

这增加 tuple 形成、VQA、反馈、训练与 edit 调用的成本，也会把同源 judge 的错误传给纠正器。作者对选中“不满足”样本的整体分数在扰动前后持平，不能证明每个样本都绕过 rationale；显式反馈的轮次与颜色切片也并非全面更好。故局部修正须同时检查原请求、未指定区域保持和真实结果，不能让反馈生成者自授成功；诊断不稳、编辑破坏其他约束或预算紧张时，保留全图重生成、直接生成及外部检查，而不是强迫每次继续自反思。

图像修正还必须先选择保留合同：edit要保留特定像素资产、对象或身份，regeneration可以只保留语义意图并重新生成。后一分支可让模型消费ViT提取的初始图像语义和原prompt，而不沿用原VAE像素latent或中间edit instruction；相应input/initial/final triplet训练也应匹配重生目标，不把它在语义任务上的收益转写成像素或identity保持保证。

删去原像素条件可能减少其局部束缚，却增加身份漂移和资产丢失，视觉encoder仍可能漏掉细节。受限RvR benchmark支持特定重生分支，不证明所有编辑优越，数据生成、训练和多步采样也不能称免费。需要精确资产保持、mask局部修改或可审计差异时，原edit/inpainting与独立保持性验收继续合理。 [原文必要机制与限制](https://arxiv.org/html/2604.25636v1)。
<!-- source-family:SF-2026-ARXIV-2604-25636 -->

同一个生成中的纠正 proposal 还可能需要与候选选择使用不同目标。理解分支从当前 look-ahead 图像与用户请求提出 `c_ideal`，经 CLIP 图文相似度损失、decoder 与 look-ahead 的梯度生成有界 latent 修正；之后不默认最后一次修正最好，而以原始 `c_user` 对推进后的候选重新评分。这把内部理想描述的生成权与用户请求下的选择目标分开，但二者仍可能共享同一表征偏差，CLIP 不是独立真值，梯度链式项也不自动构成正交或流形投影。<!-- source-family:SF-2026-ARXIV-2604-13540 -->

候选选择能够拒绝过度修正，却不能消除理解错误或评分盲区；额外理解 forward、look-ahead、decoder backprop 和多候选评分都在 critical path 上。作者 H800 上的受限生成实验存在更多迭代及 counting/position 切片退步，不能以“无需重训”称免费，也不保证内部目标与原请求始终一致。原请求独立验收、修改预算与可撤销状态须保留；信号不可靠或成本不合算时，回退普通 sampler、固定 guidance 或外部选择，训练期 anchor 与此推理期 proposal 不混为同一责任。

Amazon 的 LLM-based TTS 工程材料支持“显式计划、生成后检查与有限重试可组成一条工程路径”，但没有公开
可复现实验 artifact、模型内部实现、并发或 tail-SLO contract；因此这里只吸收状态机，不外推质量数字或
内部机制。

<!-- semantic-body-binding:SF-2026-ARXIV-2609-13006:start -->
在 video diffusion 中，plan 还可以从生成前说明书演进为生成中的 addressable revision state。VLM 先把对象、动作、深度和运动强度编译为 kinematic conditions；迭代优化阶段再用 object-centric gradient routing，只向当前主动对象对应的 latent 区域传播修正，尽量不扰动被动环境。Planner 拥有 provisional physical constraints，gradient router 只拥有局部更新 proposal，base generator 产生候选 trajectory，独立 validator 才决定修改是否可以 commit；“被 mask 的区域没有更新”不等于真实环境必然静止。

这条分支以推理期 backprop、VLM/API 调用、mask 对齐和更多显存换取局部可控性。Plan 错误与 gradient routing 错误会形成共因，过窄 mask 会冻结本应变化的环境，过宽 mask 又退化为全局重写；keyframe 增加还会累积规划误差。低约束、短视频或 latency 优先时，direct generation 仍是合理基线。Physics-aware video generation exact-v1 的组件消融和受限人评只支持给定基座、3–5 个 keyframes 与 PhysGenBench 下的局部机制，不证明系统获得一般物理定律、复杂接触正确性或实时生产能力。
<!-- semantic-body-binding:SF-2026-ARXIV-2609-13006:end -->

可控视频中的 kinematic plan 还要区分并行分量、时间串接与离散接触，不能把多个动作名称直接当作可相加的物理定律。一个受限生成分支先把文字分成 motion sequence 与数值/定性参数，再由各运动模块提出同一初始状态下的位移；作用于不相交状态分量时可相加，顺序动作则以上段终态作为下段初态，接触时另用有质量条件的跃迁模块重置状态。轨迹再指导视频 latent 的局部旋转/缩放与有界混合；文字解析、动力学候选与外观生成拥有不同的误差来源，不由渲染流畅补齐参数或接触正确性。

这种可组合接口限定在二维、少量运动类别与简单两体接触。平移/旋转存在滚动约束时独立相加仅是近似，稠密接触、关节链与超范围动力学不获保证；从一个跟踪轨迹选择近似 prior 并正则微调也不能识别通用物理法则。受限评价中，运动 invariant 可较稳定而轨迹误差已经爆增，较远结构偏移与部分早期窗口外推明显失败，因此应把 invariant、轨迹和视觉质量分开验收。解析、tracking、prior 搜索、适配与 latent 调制都付费，公开视频的派生轨迹也不是无误差真值；耦合强、标注/参数不可靠或预算不足时，回到可信 simulator/人工轨迹、较简单运动条件或普通生成，不从局部一致性分数签发物理保真。 [必要机制与反证](https://arxiv.org/html/2609.21455v1)。<!-- source-family:SF-2026-ARXIV-2609-21455 -->

### 复杂视觉生成需要显式 Plan、Predicate 与 Retry Budget

一次生成在对象、计数、属性和关系较多时难以同时满足全部约束。更可控的路径先把 prompt 编译为 typed visual program，再由 verifier 对每个 predicate 产生 evidence，controller 据失败类型选择局部 edit 或 resample；program 拥有待满足合同，verifier 不拥有事实真值，最终 acceptance 仍由独立 gate 提交。可定位修复换来 parse error、verifier blind spot、循环和额外生成成本；错误 program 还会稳定优化错误目标。无法可靠分解或验收时，应回退 single-pass/best-of-N、人工检查和最大 retry/cost budget。exact-v1 只证明披露 predicate 与 benchmark 范围，不覆盖开放世界事实和任意 prompt。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-11722 -->

### Generator 作为工具时，生成状态仍需外部选择与验证

图像生成器可以把视觉 state 变换为新的 observation proposal，支持后续比较或推理；但图像质量与任务正确性不是同一变量。生成器只拥有 proposal，selector/verifier 必须检查几何、语义和目标约束后才提交下一状态。<!-- source-family:SF-2026-ARXIV-2609-16409 -->

多 sample 与验证提高覆盖，也增加延迟和选择错误，生成幻觉还可能被后续推理放大。六项任务与特定模型不证明通用视觉 reasoning 改善；校验不足时回退固定视觉工具、原始 observation 或文本推理。

## 长视频：历史身份、连续性与可读范围

短片质量、长时一致性、可寻址历史与可交互世界状态是不同的验收对象。下面的分支先约束生成器能读回什么，再讨论跨窗口修复；它们不能替第25章完成环境转移验证。

### Object Permanence 与 Addressable History 是两个 Gate

视频生成能够在短片段中维持对象外观，不代表系统拥有可寻址、可更新的长期环境状态。环形或有界历史机制可以扩展可引用的过去，但仍需分别验证对象身份持续性和历史容量；两者都通过，也不能自动推出 action-conditioned causal transition。它是生成状态管理的进化，不应被误写成完整 world model。
<!-- source-family: arxiv:2608.26794v1; semantic-body-binding: video-object-permanence-vs-history-capacity -->

### Entity-centric Video Memory 把对象身份与帧历史分离

<!-- semantic-body-binding:SF-2026-ARXIV-2605-23610:start -->
保留完整 frame history 在短视频中最可靠，长度增加后成本随时间增长；entity-centric 分支用 entity ID、latent patches、update budget 与 shot script 维护可寻址对象状态。它解决“对象是谁、何时更新”，不等于已经证明物理世界的因果一致性。

稀疏对象记忆降低历史成本，却会引入 identity swap、关系丢失和脚本先验偏差。exact-v1 只支持作者视频与 evaluation；对象身份不稳、关系回归或场景超出脚本时，应回退 keyframe/full-frame history 或扩大可见窗口。arXiv:2605.23610v1
<!-- semantic-body-binding:SF-2026-ARXIV-2605-23610:end -->

### 长视频历史选择需要有限预算与遗漏检查

<!-- body-source:SF-2026-ARXIV-2606-22370 -->
长视频生成不能无限复制完整历史 KV；按 prompt-history 相关性选择可读历史，把 cache budget、selection error 与 continuity 绑定同一运行时状态。 这项变化只在 exact-v1 披露的 workload、状态身份和评估合同内成立；只覆盖受测长单镜头生成；selection miss 会破坏长期一致性，不能外推到可交互 world state。 因此旧路径在这些新增约束不存在、证据条件不足或失败回退被触发时仍然成立，不能被新的局部结果静默覆盖。

上述预算压力还不能只按 token 总数解释。长交错文本—图像生成的 token-matched 对照中，图像重历史与等长文本历史产生不同失效：大量无关 visual patches 可能参与 attention 竞争，保留更多历史反而污染当前合成。一个条件分支先做一次完整历史的 dense probing，在浅层按文本 block 相关性、在深层按 VAE image block 相关性分别选择历史，再固定这两套可见集合用于后续 diffusion/flow steps；丢弃未选 tokens，而不是将它们压成仍参与竞争的特征。它管理的是当前生成器能读取的条件，不创建第25章的持久事实世界状态。

这条路径以预先 dense pass、模型内部状态访问、分层 mask 与选择错误换取较小后续 KV 和较少无关竞争；dense probe 本身不能漏算为零成本。作者 BAGEL、50 story templates、固定文本只生成图像的受限比较支持该分支，text/visual selection 与人工 semantic oracle 不可互换，也没有普遍的“最多四张图”容量常数。判断器版本在表注与正文之间另有不一致，不能照录唯一 evaluator recipe，更不以 micro-workload 的加速证明生产 SLO。选错早期身份锚点、模型/层变化或质量回归时保留完整历史、带 anchor 的窗口及重新校准，不让稀疏历史自行批准连续性。<!-- source-family:SF-2026-ARXIV-2603-07540 -->

### 长视频窗口中的频谱责任分工

扩大生成窗口通常试图直接换取全局一致性，但它也可能使 attention feature 的奇异谱过度集中，让低频结构压制局部细节。一个条件化分支是把全局低秩 guidance 与局部高秩 reconstruction 分责：前者约束跨窗口的长程结构，后者恢复窗口内的细粒度变化，从而避免预先把表示硬拆成“appearance”和“motion”。<!-- semantic-body-binding:SF-2026-ARXIV-2605-06509 -->

这个分工依赖谱集中确实是主要故障来源。现有证据只覆盖 Wan2.1、LTX-Video 和作者的评价设置，SVD 成本、复杂镜头运动及跨 backbone 稳定性仍未证明。谱假设不成立或质量收益不足时，应回退 overlap/local-window、显式 feature partition，或以训练方式获得的长视频机制，而不是把频谱修复当作统一答案。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-06924:start -->
长视频不能只把上一段末帧当下一段条件；一旦主体离场再出现、环境发生非线性变化，open-loop chaining 会把早期误差持续放大。生成 runtime 可为每段执行 `retrieve → synthesize → frame/video-level refine → update`，由版本化 multimodal memory 保存实体、环境与叙事进展，mode controller 只在已声明的 extrapolation/interpolation 分支中选择，最终 clip gate 才提交可见段。它用额外生成、检索与 self-review 换长程一致性，也会继承同源 evaluator 偏差、memory drift 和 mode-switch 错误；状态不可信或预算不足时回退短段、固定模式、人工 storyboard 或整段重生成。 [受限证据：arXiv:2605.06924v1]
<!-- semantic-body-binding:SF-2026-ARXIV-2605-06924:end -->

<!-- semantic-body-binding:SF-2026-ARXIV-2605-20476:start -->
当整段 conditioning 与 anchor 可预先确定时，还可以把左到右的 `K` 段 critical path 改成 sparse-to-dense
anchored tree：先生成稀疏锚点，再在相邻 anchor 之间分层并行 infill，使串行深度接近层级数，并把单次误差约束在
anchor-bounded span。它不是 rolling memory 的无条件升级；rolling path 适合条件逐步到达和在线 streaming，
anchored tree 则要求未来边界可知、双向 infill 可靠。

层级并行减少 horizon-compounding drift，却会让坏 anchor 污染整个子树；弱 motion guidance、动态镜头、多镜头和
纯 text-to-video 也未满足当前证据前提。Anchor quality 或 continuity Gate 失败时，应回退短窗 AR、overlap
refinement、整段重生成或人工 storyboard。exact-v1 只支持 Wan2.1+VACE 的五类 condition 与 LTX-2.3 静态镜头
实验，不证明任意长视频都获得同样关键路径缩短或一致性收益。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-20476:end -->

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

### Transparency 不是单一的“可解释程度”

可读 token bottleneck 或可干预中间变量只提供 variable transparency：我们能命名并操纵某些状态。它不自动给出 algorithmic transparency，因为并行去噪或多步 refinement 的实际计算路径仍可能很深；也不自动给出 safety monitorability，因为可观察变量未必对危险行为具有稳定、可校准的因果关系。生成系统应分别记录变量接口、有效串行深度和安全 sensor contract，不能用其中一项替代另外两项。

显式中间变量便于 probe 与控制，却可能增加架构约束、额外 step 和错误解释；更短的可观察路径也不保证语义忠实。纯 AR 或 opaque diffusion 在只要求输出质量、且外部 verifier 足够时仍可成立。现有证据只为特定 diffusion language model 提供 opaque serial-depth 的界与局部 probe，架构和训练各自造成多少透明度仍未分离，因此不能外推为通用安全优势。
<!-- source-family:SF-2026-ARXIV-2606-20560 -->

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

<!-- semantic-body-binding:SF-2026-ARXIV-2609-12691:start -->
图像编辑进一步要求把“执行目标指令”和“保留未指定上下文”拆成不同训练状态。只优化 text–image alignment 会鼓励模型重画整幅图，只优化 source similarity 又会阻止必要修改；一个受限分支分别编码 instruction、source image 与 source spatial latent，再让冻结 VLM 从目标图像产生 descriptive anchor，由可训练 aligner 比较生成图与 anchor 的 token distribution，把语义残差经低噪声单步估计传回 generator。VLM 只提供 training-time gradient proposal，generator 保留生成权，独立 evaluator 才判断编辑是否成功；anchor 不能凭自身输出成为视觉真值。

这样可以在不增加线上 verifier 的情况下前移语义约束，却增加冻结模型偏差、单步梯度近似、训练显存和 identity-preservation 冲突。关系词、组合约束或 anchor 遗漏会把错误方向稳定地写入生成器；局部几何明确时，pixel/perceptual loss 仍更直接。IABEdit exact-v1 的 RealEdit/MagicBrush 对照支持该责任分解在受测设置中的可行性，但部分感知指标并非最优，且论文训练 FLOPs 的绝对值与百分比互相冲突，因此成本数字不得进入长期结论。
<!-- semantic-body-binding:SF-2026-ARXIV-2609-12691:end -->

### 离散编辑的概率引导与量化修复不是同一道验收

不重训编辑目标也可以利用预训练离散VAR的source状态：先保留source coarse scales，再沿 `onehot(source)−softmax(prediction)` 的概率方向对target logits加nudging，以source/target两次cross-attention passes的差构造编辑mask。Mask外以更强source nudging约束保留，再可对量化残差做局部codebook投影与修复；它分开了目标编辑、区域保持与离散重建职责，不是source/target logits等值混合、通用精确CFG或背景无损保证。Style edit会关闭refinement，因此量化修复也不是所有编辑模式的固定步骤。

Mask、额外passes与refinement都有成本，错误mask和codebook误差还会损伤背景，应分别验收编辑语义与重建保持。`arXiv:2604.14591v1` 的SWITTI/512–1024受测PIE/COCO/OpenImages中，PIE512 inversion/forward各.41秒不表示其余成本为零；20ms mask统计只single-image/sM=9，SSIM86.80低于TurboEdit91.59，跨backbone指标不能证明普遍更快更好或受控范式加速。GPU/precision/batch/concurrency/SLO在必要设置未披露，不能补造；mask失配、重建退步或预算不合算时，原生成器、显式source约束或其他已验收编辑路线仍合理。

<!-- source-family:SF-2026-ARXIV-2604-14591 -->

编辑进入长视频后，还要按 segment 管理执行依赖，而不只按 token 或区域分配保留强度。在采用反演的分支中，同一 segment 必须先取得自身 inversion state 才能 edit；可流水重叠的是不同 segment 的工作，不能把两阶段写成同段独立执行或零通信。SSIM 与估计运动可提议只显式编辑选中帧，再重建跳过帧并用跨段 overlap 修整边界，但 proxy 不保证被跳帧仍满足新编辑语义；更密 keyframes 和 overlap 可能改善质量，也增加反演、编辑、补帧、buffer 与边界处理成本。验收应分开编辑支持、插值失真和端到端排程，不能用分段估算、相同步数或跨帧图像 CLIP 相似度认证无限长度稳定、prompt alignment 或请求 SLO。强运动、大结构修改、补帧或边界质量回归时，仍回到 dense/full-segment 编辑与独立验收。<!-- source-family:SF-2026-ARXIV-2512-24026 -->

source-token 约束可以保留未指定区域，却也会把原运动的细纹理带入新视频；并非约束越强就越忠实。离散 coarse-to-fine 分支直接编码 source、缓存 source 条件下指定 token 的概率，在 edit-pass 比较同一 token 的支持变化，再与 edit argmax 竞争；attention 与 scale 只调局部保留容忍度，不拥有区域真值。较早 scale 固定结构，较晚 scale 撤除 source 约束让细节重生，这不同于对全部 logits 做固定 nudging 或重新反演连续轨迹。

这要付 source forward、概率/attention 缓存和校准成本，也可能因错误 anchor 或释放过早损伤保留区域。前一 scale residual 可以提议最后高分辨率 scale 的计算 mask，被剪 token 仍进入输出头而非变成已经验证的内容；同预算随机剪枝对照支持局部选择，但更快配置仍有质量下降。固定 backbone/seed/短片对照不认证任意编辑或完整请求 SLO；大结构变化、mask 失配或质量回归时，回原生成器、显式局部编辑/inpainting 或更高保留预算，不由 two-pass 提速授背景无损。 [必要机制与反证](https://arxiv.org/html/2609.21268v1)。<!-- source-family:SF-2026-ARXIV-2609-21268 -->

### 固定长度 Diffusion 把长度预测变成 Admission 决策

自回归生成可以逐 token 停止，固定长度 diffusion LM 却需要在去噪开始前分配响应槽位；因此 length predictor 实际上拥有一次 admission-time compute budget。预测偏长会浪费并行迭代，预测偏短则可能截断语义并触发扩容或整段重试，破坏原本的延迟优势。动态长度只有在预测开销、重试策略和 SLO 一起计入时才成立；长度高度不确定或输出必须完整时，保守上界或自回归分支仍更可靠。[受限证据：arXiv:2605.04215v1]

<!-- source-family:SF-2026-ARXIV-2605-04215 -->

若生成中再插入槽位，旧位置与新画布的坐标映射、画布版本和 logits 必须一起绑定；比较分布时需明确哪些旧未决位置可比较，提交只能使用被选画布对应的预测，不能把旧画布 logits 当作新状态。以平均分布差异决定是否扩容是带额外 forward 与对齐成本的启发式，既不保证每个位置不变，也不保证原生成分布或最终延迟不变；固定画布仍是状态简单、容易验证的共存方案。

固定画布中若同一个 EOS 同时表达“语义已经结束”和“剩余位置只是 padding”，训练会把内容终止与空间占位混为一个状态。独立的 VOID token 可以让 sampler 先管理空白槽位，再让 EOS 专注语义提交；length/admission、denoising 与 final commit 因而拥有不同 owner。它以新增 token、objective 和 runtime compatibility 换更清楚的终止语义，不能从单一 masked-diffusion 实验外推所有生成范式；自回归逐 token 终止仍是更自然的共存分支。

<!-- semantic-body-binding:SF-2026-ARXIV-2606.17999 -->

## 加速不能静默改变生成轨迹

缓存或跳步加速在多模态 Diffusion 中会复用旧的视觉与文本状态。旧状态足够接近时，它减少重复计算；随着轨迹推进，stale state 会让加速输出与未加速模型系统性分叉。因而“更快但 benchmark 仍可用”并不等于语义等价，运行时还要测量 state freshness、输出 agreement 与 refresh cost。

这形成一个明确的控制分支：短 refresh interval 提高一致性却回收较少计算，长 interval 提高速度却扩大漂移。控制器只能把 confidence 当刷新信号，不能当 correctness certificate；漂移超过预算时回退完整 refresh。该分支属于 iterative refinement，不应外推到具有不同状态语义的自回归 Decode。

刷新信号还可以分成离线 prior 与在线内容两层。全程固定间隔容易审计，但同一个模型的不同 timestep、layer 和 module 对复用/剪枝未必同样敏感；一条分支先用少量完整生成建立“缓存多远或减少多少计算后，局部 feature 与 full-compute 结果相差多少”的统计，将其保存为模型特定 prior，在全量刷新预算内提议 schedule，再在实际生成中选择需要重新计算的 token 位置。离线 prior 回答计算分配，在线选择回答当前内容位置；局部 cosine 差额既不是最终质量，也不是本次轨迹的真实误差上界。<!-- source-family:SF-2026-ARXIV-2603-07057 -->

[受限敏感度加速对照](https://arxiv.org/html/2603.07057v1#S3)支持这种校准与部署分责，不支持“一次建模永久有效”。模型、solver、步数或数据分布改变后要重新检验 prior；提议出的 schedule 还须检查边界、可达性和实际输出，不能由印刷伪代码的最优性说法跳过这些检查。原文的调度转移与剪枝率方向有未闭合处，只保留公开机制的有限提案，不补造已验证实现。离线生成/缓存峰值、prior 维护、在线选择、refresh 与实际 denoiser 都计费；FLOPs 倍率不能替代墙钟时间或请求 SLO，高加速还会损害质量。Prior 漂移、局部误差不能预测输出或成本不合算时，保留固定间隔、更密刷新与原生成器，仍由独立质量检查决定近似是否可用。<!-- source-family:SF-2026-ARXIV-2603-07057 -->

### 加速后的输出必须与未加速轨迹建立一致性边界

缓存或跳步能减少 diffusion 的重复计算，但“最终观感尚可”不能证明它仍在执行同一生成过程：stale visual state 与已生成文本状态可能把内容推向另一条轨迹。运行时应把 refresh interval、state revision 与同模型 full-compute 输出的一致性作为联合验收量；缩短 refresh 可以提高一致性，却会交还一部分加速收益。该检查只约束近似分支的语义漂移，不保证两个随机样本逐点相同；一致性或 freshness 超界时应恢复更密集刷新或全量重算，固定 schedule 在分布稳定时仍是可预测基线。
<!-- source-family: arxiv:2607.29079v1; daily: 2026-08-03; semantic-body-binding: accelerated-generation-state-agreement -->

<!-- semantic-body-binding:SF-2026-ARXIV-2605-22723:start -->
Gaussian DDPM 只匹配 reverse mean 时，会保留沿完整生成路径累积的 covariance error；在论文假设下，匹配 full reverse covariance 可改善离散 path KL 的收敛阶。显式协方差不可承受时，matrix-free Lanczos 用 covariance-vector products 近似所需矩阵函数，以更多算子调用换取无需构造完整矩阵。Sampler owner 必须把 covariance estimator、Lanczos iteration、residual tolerance 与 step schedule 共同版本化。

更好的理论阶数不等于真实数据上的感知质量或低延迟收益，Lanczos iteration 还引入计算和数值误差。exact-v1 的 Gaussian/score regularity、图像任务和受测设置不能外推到任意 diffusion workload；假设、residual 或端到端质量不满足时，应回退 mean-only sampler、更多 steps 或对角/低秩 covariance，并保留 full-compute reference trajectory。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-22723:end -->

量化又会把当前去噪器输出的偏差写入多步 solver 的历史。只修当前输出，仍可能让它与已有history不一致；另一分支把solver需要的整段输出window作为待估state，以平滑轨迹外推作prior、当前量化输出作observation，递归更新当前及历史entry，再把posterior mean交原solver。目标是同一量化轨迹 latent x 处的 full-precision denoiser 输出，不是原始 full-precision 整条采样轨迹；它不把采样latent改为环境真state，也不改变原solver的数值更新定义。开头history不足时只返回有效entry、降低外推阶数，不能填造过去观察。<!-- source-family:SF-2026-ARXIV-2609-21407 -->

这条路径支付offline FP/quantized配对校准、posterior state与在线filter成本。按step/channel聚合并逐element修正省掉crosschannel/spatial covariance，却依赖这种共享统计关系；非Gaussian的LMMSE结论还需要有限二阶矩、噪声相互/时间不相关并与初始state不相关等条件，不是任意量化误差下的Bayesian保证。作者W4A4/20步和两种solver结果主要测对FP生成的分布差，不保证真实质量，部分ImageReward退步且UniPC有cell不最优；单image BF16 CPU-offload比较也不能证明普遍加速。0.25 MiB仅校准统计量，不是完整运行峰值；校准总成本与生产SLO未披露。校准轨迹与部署状态偏离、滤波失稳或成本不值得时，保留原quantized solver、更高精度/密集求值及local correction；既有freshness/完整reference仍负责一致性验收。[必要模型与反证](https://arxiv.org/html/2609.21407v1)。

### 已 Finalize 的 diffusion block 也可能需要可控重开

block diffusion 把局部结果 finalize 后可以并行推进后续计算，但早期错误会被后续 Context 固化。需要编辑时，不能直接覆盖 token 而保留依赖它的 cache/state；正确演进是 `reopen -> invalidate dependent KV/state -> refine -> reverify -> recommit`，并让 commit revision 成为下游 identity。

可重开提高纠错能力，却增加回滚范围、重复计算和并发一致性。只有 verifier 发现的收益超过 invalidation 成本时才启动；低风险生成或依赖扇出很大时，重新生成整个 suffix 仍更简单可靠。

<!-- source-family:SF-2026-ARXIV-2607-22663 -->

## 本章在知识树中的位置

第18章解释 Decoder Only AR，第20章解释 token sampling；本章把 AR 放进更宽的生成范式树，并拥有 mutable generation、block refinement 与 commit boundary。第25章只在生成状态同时表达 action-conditioned environment transition 时才称其为 World Model。

本章拥有加噪/概率路径、noise/velocity 预测目标与 sampler 的对应关系，因为它们共同定义 generation semantics；Part IV 第28章接手如何优化这些目标及训练稳定性，后训练章节接手反馈驱动的参数更新。线上 KV、batching、speculative verification 与 scheduler 分别由 Ch45～48、Ch56 拥有，本章不重复其框架实现。

## 从机制演进到系统设计

生成范式的演进不是 AR 被 Diffusion 线性取代，而是 factorization、并行度与 correction authority 的重新分配。AR 每次提交一个 token，状态简单但串行；masked、block 或 diffusion 路线并行提出多个 provisional positions，再以迭代修正换吞吐。混合方案进一步把 proposal、verification、rollback 和 commit 拆开。

并行生成只有在质量合同、cache invalidation 和停止规则都被版本化后才成立。它获得并行度，却增加迭代次数、临时状态、拒绝/回滚以及训练—推理 mismatch；短输出、严格 exactness 或 correction 成本高时，AR 仍可能更优。图像、视频和文本的 evaluator、长度与硬件路径不同，不能共享未经条件化的性能结论。

## 面试与自检问题

1. 为什么 diffusion 的 serial steps 少于 token 数仍不保证更快？
2. masked generation 中 provisional 与 committed token 有何区别？
3. Block Diffusion 如何在 AR 与 full-sequence diffusion 之间取舍？
4. correction 与 exact speculative verification 的 correctness contract 有何不同？
5. 为什么 draft marginal 不能当作 target path probability？
6. mutable token 会怎样影响 KV cache 和 streaming？
7. 一个离线 best-budget benchmark 为什么不等于线上 controller？
8. 哪些场景下 append-only AR 仍是更好的工程选择？
9. DDPM 的前向加噪、noise-prediction loss 和反向采样均值如何相接，哪个对象在部署时不可见？
10. Flow Matching 的条件直线路径为什么不保证部署时一 NFE 精确生成？

## Research Outlook

下一阶段压力是让 generation policy 成为 runtime 可控制对象：根据 entropy、queue、memory、deadline 和 output side effect 动态选择 block、proposal、correction 与 commit；同时建立跨 runtime 可复现的 committed-goodput 与 exactness 测试。

## Reflection

生成范式不是从“串行”走向“并行”的单向进步史。系统用并行草拟换来了 mutable state，用修正换来了额外 forward，用更大候选空间换来了 verification 和 memory。真正的演进，是让这些成本与输出承诺被显式管理。

## Review notes

- `SF-2026-ARXIV-2603-10408` — Daily补查 `2026-03-13`；[Motion Forcing exact-v1](https://arxiv.org/html/2603.10408v1) §3.1–3.5/Eq1–8、§4/Tables1–2及§5直接限制，2+1+2=5。root非准备者实际必要原证、完整Camera/Motion与CoMoVi邻接及逐字PRE通过后窄写两段；mar13_supplement非writer实际顺读两段、完整Camera/Motion至稀疏control邻接和本人末注，回对双mode/MPR/DDIM接口，POST通过，root核回执并释放窄锁，不授DAY。只采共享双clock的固定另一流训练、先预测depth再固定消费的生成接口；clean-label训练/预测部署、两loop预算、FVD反退、点/相机信号非几何真值与物理/机器人保证隔离近文。未核artifact、图像点值、视频或复现。

- `SF-2026-ARXIV-2603-10395` — Daily补查 `2026-03-13`；[exact-v1](https://arxiv.org/html/2603.10395v1) Algorithms1/2、§3、A.1–3、B/C必要配置及一般图Table1/7；2+1+2=5。root非准备者实际必要原证、Ch24完整局部及两段PRE通过后窄写；mar13_supplement非writer实际顺读新两段、完整continuous/discrete至source邻接和本人末注，回对A.3 Eq28/29，POST通过，root核回执并释放窄锁，不授DAY。只采有限clean期望率→实际转移概率重算接口；有限Euler非负、prior人口、clipped/single-sample KL与整轨迹保证隔离。一般图反侧/配置与成本近文，不采Science SOTA、实现复现或生产能力。

- `SF-2026-ARXIV-2603-10210` — Daily补查 `2026-03-13`；[exact-v1](https://arxiv.org/html/2603.10210v1) §4/Alg1、§5/Tables1–7与A/B/D直接边界。2+1+2=5，遗漏判定→mask-prompt key proposal→早段在线强度的具体接口差额深入；非准备者 mar13_admission_review 实际必要 Source、Ch24完整局部与两段PRE通过；root窄写后，非写入者 mar13_supplement 实际顺读新增、完整局部邻接及本人末注并回对必要原证，POST通过，窄锁释放，不授DAY。to_k输入与projected K、Eq8梯度范数与Alg1 Adam(loss)、Main/App强度/步数披露差异不补造精确recipe；共同Softmax分母、固定Q/单block及真实region条件不授全轨迹无干扰。Table5实际质量/时间反侧近文，未认证全baseline/VLM/在线优化费用、实现、复现或生产SLO。

- `SF-2026-ARXIV-2603-12252` — 2026-03-14 补查；[exact-v1](https://arxiv.org/html/2603.12252v1) §4.2/Eq4–11、§5/Tables1–3、§6、必要AppendixC/D/E。2+2+2=6，具体条件状态/双时钟接口差额深入；采用latent递归与末态解码分开、两阶段训练和回退边界，不采用隐藏思考即证明、全任务支配或参数冻结保证。Table1专训均值与unified分开，具体退步列定位经独核纠正；AppendixC未充分给独立算法验证，不采用Sudoku行列和为唯一性证书。root必要Source/完整owner局部/PRE，mar14_supplement独立原证、实际owner与逐字PRE通过后root窄写；mar14_supplement实际顺读新增两段、完整邻接与本人末注并回对必要原证，nonwriter POST通过，不授日级完成。未核代码或复现。

- `SF-2026-ARXIV-2603-10785` — 2026-03-13 补查；[SGA exact-v1](https://arxiv.org/html/2603.10785v1) §3–4、必要E/F与Algorithms1–2。只采用root-linked视图、grouped update与粒度time/weight共同recipe接口；同位置Gram/NTK身份不保证不同crop梯度冲突减少，Eq6平均与Alg2归一化交接未核，不认证完整可执行loss。预处理15–30min、估计训练时长及附近checkpoint不授精确33%端到端省算；静态小域质量/成本反侧近正文。mar13_supplement 必要Source/实际owner提案、mar13_admission_review 独立Source/PRE、root必要原证和完整CFM局部通过后窄写，5分定点深入；mar13_admission_review 已实际顺读新增正文、完整CFM邻接与本条末注，并回对必要原证，非writer POST通过。未核代码或复现，不授日级完成。

- `SF-2026-ARXIV-2603-09104` — Daily `2026-03-12`补查；[exact-v1](https://arxiv.org/html/2603.09104v1) §3–5/Eq1–16/Tables1–4。2+1+2=5，motion分类/跨帧读取gap深入；不采硬geometry/flowtruth或Eq15确定recipe，metric反侧、raresemantic/view边界和额外计算保留。未核像素/实现/复现；Source/date/逐字PRE经mar12_independent_continue独立复核通过，root授单段/本人末注窄锁，root非作者已实际顺读正文/完整邻接与本末注，actualPOST通过，窄锁释放；未授DAY。

- `SF-2026-ARXIV-2603-09094` — Daily `2026-03-12`补查；[exact-v1](https://arxiv.org/html/2603.09094v1) §3–5/Eq1–11/Tables1–4。2+1+2=5，event文本/keyframe时间接口gap深入；Eq7文本凝缩为全局positive/negative，不采逐帧切text、真实physics/causaltransition、σ²recipe或未列PhysHPO精确差，slice反侧/积错与完整条件生成费用保留。未核图像/实现/复现；Source/date/逐字PRE经mar12_independent_continue独立复核通过，root授单段/本人末注窄锁，root非作者已实际顺读正文/完整邻接与本末注，actualPOST通过，窄锁释放；未授DAY。

- `SF-2026-ARXIV-2603-09125` — Daily `2026-03-12`补查；[QUSR exact-v1](https://arxiv.org/html/2603.09125v1) §2–4/Eq1–9/Tables1–2。2+1+2=5，空间noise与qualitycondition分责gap深入；不采calibrated aleatoric/硬clip/标准DDPM或真实细节保证，忠实度反侧、baseline来源与MLLM/编码成本保留。未核像素/实现/复现；Source/date/逐字PRE经mar12_independent_continue独立复核通过，实际写入获root窄锁，root非作者已实际顺读正文/完整邻接及逐字PRE，actualPOST通过，窄锁释放；未授DAY。

- `SF-2026-ARXIV-2603-09408` — Daily `2026-03-12`补查；[FCDM exact-v1](https://arxiv.org/html/2603.09408v1) §3–6/Tables2–7、B/G必要反侧。2+1+2=5，conditional convolution与sampling成本轴gap深入；有限ImageNet、fp32/硬件分账、FLOPs近似与metric反退，不采普遍训练/端到端加速。未核像素、代码或复现；Source/PRE经mar12_independent_continue独立复核通过，root非作者已实际顺读正文/完整邻接及逐字PRE，actualPOST通过，窄锁释放；未授DAY。

- `SF-2026-ARXIV-2603-09721` — Daily `2026-03-12`补查；[FrameDiT exact-v1](https://arxiv.org/html/2603.09721v1) §3/§5–6、A1/B1/B3及Tables2–6。2+1+2=5，具体frame-level权重与local temporal共存差额深入；不采A1无条件等价、manifold保证或唯一归因，FVD/FVMD/FID与T2V配置、退步与费用见证据记录。未核图像精数、代码或复现；Source/PRE经mar12_independent_continue独立复核通过，root非作者已实际顺读正文/完整邻接及逐字PRE，actualPOST通过，窄锁释放；未授DAY。

- `SF-2026-ARXIV-2603-08271` — Daily `2026-03-11`补查；[exact-v1](https://arxiv.org/html/2603.08271v1) SUP_CORE105–310/312–368/499–513 Alg1/§3/setup/T1/必要T2/§4.3/Conclusion；Fig4仅caption正文，非全T3/Appendix/pixels。2+2+2=6，安全条件库与owner差额深入必要内容。review_mar11_continue Source/actualCh24 262–283与Ch23/25交接PRE、root逐字单段接纳并授CASG后/pooled前窄锁。作者actual260–286完整原局部，采用多prototype制备/negative条件与外置真实安全权限，threshold/算法不闭合、冻结base非零费用与保留质量反侧/退路近文；细项指标留本日证据。已写，review_mar11_continue非writer实际260–286完整邻接/new274及本人1871注POST通过，root接纳并释放Ch24本项锁，未授DAY/实现复现。

- `SF-2026-ARXIV-2603-07057` — Daily `2026-03-11` 补充；[exact-v1](https://arxiv.org/html/2603.07057v1) §3/Eq2–6/Alg1、§4/Table1–5、必要 A.2–A.4/B.1。2+1+2=5，离线 timestep/layer/module prior 与在线 content 选择分责缺口深入；不采伪代码可达性/边界未闭合后的最优保证或正 λ 下反方向的剪枝率保证。Proxy 非最终质量，OFS 包含生成费用，不与纯 generation 双计；FLOPs 非 latency，质量退步/漂移与全部成本近文。review_mar11_continue 必要 Source 独核通过，root actual owner/PRE/必要原证后窄写；非写入者 supplement_20260311 已实际回对必要原证并顺读新正文、完整局部邻接与自身末注，POST 通过；未核 artifact/复现，不授日级完成。

- `SF-2026-ARXIV-2603-06351` — Daily `2026-03-10`补遗漏；[DC-DiT exact-v1](https://arxiv.org/html/2603.06351v1) §3.1–3.5、§4.1–4.4：同一步非均匀表示与完整状态回填的架构分支。保留软平均预算、完整网格计算、批补齐、参数/FLOP对照差异与 teacher 前置训练；不采用语义边界真值、硬容量或全流程加速保证。root 已读必要原证并核本章及Ch23/25交接；非写入者 supplement_20260310 实际顺读新增两段、完整局部邻接及末注并回对上述必要原证，写后复核通过。未核代码或复现实验，不授日级完成。

- `SF-2026-ARXIV-2603-07540` — Daily `2026-03-11`补查；[UniLongGen 精确v1](https://arxiv.org/html/2603.07540v1) §3/5/6.1–6.2/6.4/6.6。作者与review_20260311必要Evidence独核通过，root实际核心、owner/Ch23/25交接后窄写两段。仅采token-matched视觉竞争、dense双深度probe与固定分层visibility，文本预给非joint rollout、oracle不替代、完整费用/选择错失近文。表注GPT-4o/HPSv2与正文GPT-5.2/HPSv3身份冲突不补造；不授统一event容量或生产加速。非写入者supplement_20260311已实际顺读新增正文、完整局部邻接及本注并回对必要原证，POST通过，不授DAY；未核实现或复现。

- `SF-2026-OPENAI-DESCRIPT-20260306` — Daily `2026-03-07`补充；[官方应用说明](https://openai.com/index/descript/) March 6，2+1+2=5，已确认具体长期知识差额，定点深入受影响内容，不上调评分。仅采用翻译内容与配音时窗联合约束、语言相关音节率、自然停顿分块及字幕/配音质量门槛的受限设计分支。厂商应用数据缺少受控消融，模型配置、样本及运行条件未披露，不采用为通用收益或内部机制证明；未核 artifact 或复现。supplement_20260307非写入者实际源→新正文/完整邻接与本末注POST通过。

- `SF-2026-ARXIV-2601-19740` — Daily `2026-01-29` 增量；[exact-v1](https://arxiv.org/html/2601.19740v1) §2/Assumption1/Eq20、§3/Assumption3、Theorems8–9、§3.3/4.1–4.2。2+1+2=5，解析 score/reference solver 与压缩拟合分责的具体差额深入；均值半径/谱/对角假设、人口失配及 fit 主导反侧近正文。root 有效 Source/PRE 复用并重新授两段/自身末注窄锁；作者已实际顺读正文及完整邻接，root 非作者实际320–340完整邻接/正文及自身末注POST通过，窄锁释放。未核实现/复现，非日级验收。

- `SF-2026-ARXIV-2601-19115` — Daily `2026-01-29` 增量；[FBSDiff++ exact-v1 PDF](https://arxiv.org/pdf/2601.19115v1) p7–9 §3.2/Algorithms2–3、p18–22 ablation/Tables1–6。FBSDiff 家族的新机制事件，不重复评分，重要机制事件受影响内容深入；inversion-cache 替 reconstruction guidance 与 per-axis relative band 接口、有限尺寸/proxy、50 vs 1000 步预算与背景泄漏边界近正文。root 实际必要 Source/owner PRE 通过并授两段/自身末注窄锁；作者已实际顺读正文及完整邻接，root 非作者实际177–195完整邻接/正文及自身末注POST通过，窄锁释放。未核实现/复现，非日级验收。

- `SF-2026-ARXIV-2601-18681` — Daily `2026-01-28` 增量；[exact-v1](https://arxiv.org/html/2601.18681v1) §2.2/3.1–3.2/4.2/5.1–5.3/6/C，2+1+2=5，learned-clock→time-only固化与endpoint增量归一的owner具体差额深入。Euler误差proxy不授FID最优/HJB训练收敛；部署无actor/Q、额外JVP/time-derivative训练、35NFE打平与状态依赖丢弃近文。root实际必要Source/Ch24原邻接/PRE通过且授两段窄锁，顺序及固化措辞按其修正；root实际完整局部邻接、新两段与自身末注POST通过，窄锁释放，不授DAY。未核artifact或复现实验。

- `SF-2026-ARXIV-2601-15500` — Daily `2026-01-24`补查；[exact-v1](https://arxiv.org/html/2601.15500v1) §4.1–4.4/Assumptions4.3–4.4、U-shaped网格/Theorem4.5与§5 learned-velocity反侧。2+1+3=6，sampler知识差额深入；只采用intrinsic complexity不替代velocity/导数/blurredendpoint条件，完整定理符号与Gaussian展示冲突终态隔离，不私修作者公式。root必要原证及actual owner193–210 PRE通过授窄锁；作者实际正文/完整邻接/自身末注顺读，root非写入者实际194–221邻接与自身末注1816 POST通过，窄锁释放，不授日级。未核代码/复现，未采用FLUX定性cost优势。

- `SF-2026-ARXIV-2601-06428` — Daily `2026-01-14` 增量；[DSC exact-v1](https://arxiv.org/html/2601.06428v1) §3.2/4/5。2+1+2=5，固定generator/head与FCA错误-上下文配对差额深入；BCE correct=1/error最高选择方向、NoRemask表文数字冲突分别隔离，不补1−g或普遍恶化；head/remask/queue费用近文。peer必要原证/actual owner PRE通过、root授窄锁；作者实际完整局部邻接顺读；root 非写者 actual POST 已通过（新正文、完整局部邻接与自身末注），未复现，不授DAY。

- `SF-2026-ARXIV-2601-05966` — Daily `2026-01-13` 增量；[exact-v1](https://arxiv.org/html/2601.05966v1) §4.1–4.2/5/A/C；causalcodec/framewise scale与inherited错误支持；rFVD/mask反侧/8FPS/drift/硬件unknown近文；2+2+2=6，具体差额深入。jan10_books_audit必要原证/actual owner PRE通过、root授窄锁；作者完整邻接已顺读，root非Books写入者已实际读正文/完整邻接/自身末注，POST PASS；窄锁释放。未核实现/复现，非日级Gate。

- `SF-2026-ARXIV-2601-05722` — Daily `2026-01-13` 增量；[exact-v1](https://arxiv.org/html/2601.05722v1) §3.2–3.3/4.4–4.5/Fig7；canonical→camera冻结再joint→orbit差额深入，定性/预算未控及原控制共存近文；2+1+2=5，具体差额深入。jan10_books_audit必要原证/actual owner PRE通过、root授窄锁；作者完整邻接已顺读，root非Books写入者已实际读正文/完整邻接/自身末注，POST PASS；窄锁释放。未核实现/复现，非日级Gate。

- `SF-2026-ARXIV-2601-04706`（Experimental）：Daily `2026-01-10`补查；[exact-v1](https://arxiv.org/html/2601.04706v1) §3/Eq2–6、§4.3.2/Table1及AppA1。采用增强t*→native text encoder与text-forged视觉条件分别注入，不写raw prompt不变或伪feature为独立真值；真实重构/forged稳健性分账。FLUX GenEval .6518→.6436、DPG83.66→83.01与MeiGen反退保留；2BBridge/1BInjection、500k/200Mpairs与80k/13M、0.49s bridge局部人口不授全pipeline无损/E2E轻量/并发SLO。jan10_books_audit必要源/具体owner PRE经root采纳并授窄锁；本轮转作者写入并顺读完整局部邻接，root非写入者已实际核正文/完整局部邻接/自身末注POST通过（本日post-audit-20261007.md §7），不授日级Gate，未运行模型或复现。

- `SF-2025-QWEN3-OMNI`：2025-09-22 [官方 Blog](https://qwen.ai/blog?id=qwen3-omni) Architecture，以及具名补证 [2509.17765v1](https://arxiv.org/html/2509.17765v1) §2.4～2.5、Tables1～2和§5.2；后续报告细节不伪装为首发时全部已相同。旧分支仅定点对照 [Qwen2.5-Omni v1 §2.4](https://arxiv.org/html/2503.20215v1)：chunk streaming已有lookahead，不是整句离线等待。采用帧内码层/时间帧/renderer等待的区分，不采普遍音质、MoE降低KV IO或端到端低延迟保证；未核实现或复现实验。

- `SF-2026-ARXIV-2602-22586` — Daily `2026-02-28`；[exact-v1](https://arxiv.org/html/2602.22586v1) §2.2–2.5、blocks32–72/94–98/117–118/182/195–198，2+1+2=5；具体owner差额深入：连续数值codec、共享clock与双loss接口；copy负侧、shared schedule/codec费用和AR回退。root非原prepared作者实际必要原证/当前owner复核并窄融正文，未遍历附件、未核artifact或复现；final_audit 非写入者已实际读取正文/完整邻接/自身末注，POST通过，不授日级完成。

- `SF-2026-ARXIV-2602-22742` — Daily `2026-02-28`；[exact-v1](https://arxiv.org/html/2602.22742v1) §3–5、blocks50–70/97–119，2+1+2=5；具体owner差额深入：SPD图metric的clean-endpoint投影；Gram可逆条件、foot/text质量反侧和非物理保证。root非原prepared作者实际必要原证/当前owner复核并窄融正文，未遍历附件、未核artifact或复现；final_audit 非写入者已实际读取正文/完整邻接/自身末注，POST通过，不授日级完成。

- `SF-2026-ARXIV-2602-22868` — Daily `2026-02-28`；[exact-v1](https://arxiv.org/html/2602.22868v1) blocks30–51/65–70/85–87，2+1+3=6；具体owner差额深入：未提交M/C与hard T分责、JS只重置未提交状态；阈值/全路径费用与不保证进展。root非原prepared作者实际必要原证/当前owner复核并窄融正文，未遍历附件、未核artifact或复现；final_audit 非写入者已实际读取正文/完整邻接/自身末注，POST通过，不授日级完成。

- `SF-2026-ARXIV-2602-22871` — Daily `2026-02-28`；[exact-v1](https://arxiv.org/html/2602.22871v1) §3–4、blocks27–47/50–65/74–83，2+2+2=6；具体owner差额深入：PRM prefix限定、stitch后AR重算；chronology非依赖证书、总预算与单path回退。root非原prepared作者实际必要原证/当前owner复核并窄融正文，未遍历附件、未核artifact或复现；final_audit 非写入者已实际读取正文/完整邻接/自身末注，POST通过，不授日级完成。

- `SF-2026-ARXIV-2602-23225` — Daily `2026-02-28`；[exact-v1](https://arxiv.org/html/2602.23225v1) blocks30–60/66–83/86–100，2+2+2=6；具体owner差额深入：多轨canvas+summary与训练/解码分验；高预算forced反側、非语义独立与费用。root非原prepared作者实际必要原证/当前owner复核并窄融正文，未遍历附件、未核artifact或复现；final_audit 非写入者已实际读取正文/完整邻接/自身末注，POST通过，不授日级完成。

- `SF-2026-ARXIV-2602-21596`：[v1 表2、4](https://arxiv.org/html/2602.21596v1)，combined `y+t` 与单独 `y` 几何、coordinate intervention 与生成质量分账；不采 66% 无损或主干加速。`SF-2026-ARXIV-2602-21818`：[v1 §3 video mask / audio-from-scratch 与评价](https://arxiv.org/html/2602.21818v1)，逐流 preservation 合同、级联费用及有限人评，不授同步保证。两项非原 packet 作者必要原证/owner PRE 后窄写；root已实际顺读正文、完整邻接与自身末注，POST通过，未复现。

- `SF-2026-ARXIV-2602-20880` — Daily `2026-02-26`；[CASG exact-v1](https://arxiv.org/html/2602.20880v1) §3 Table1/§4–5/AppD6。2+1+2=5，安全受影响深入；多类方向相消与 category-conditioned choice、latent 每步 cosine 与 text projection 接口分责、detector 权限/FID 反退/2.58x 求值费用及回退近文。非原 packet 作者必要原源/actual owner PRE 通过，root 授窄锁；作者写后正文/完整邻接及自身末注顺读，root 非写入者 actual POST 通过。未核 artifact/复现，非日级验收。

- `SF-2026-ARXIV-2602-22486` — Daily `2026-02-28`；[exact-v1](https://arxiv.org/html/2602.22486v1) §3–4/必要manifold-density-velocity假设与W2分项；intrinsic指数/ambient费用、exact ERM/earlystop及solver分责。2+1+3=6，具体owner差额深入，限制与原分支回退近正文。root实际必要原源/owner PRE通过并授窄lease；作者正文/完整邻接/自身末注已顺读，root非作者已实际独读正文/完整邻接/自身末注POST通过，窄lease释放。未核实现/复现，非日级Gate。

- `SF-2026-ARXIV-2602-22505` — Daily `2026-02-28`；[exact-v1](https://arxiv.org/html/2602.22505v1) §3 Assumption1/Theorem2/3、§4 Assumption2/Proposition2/Theorem4/5。2+1+3=6，Euler/FHS 的误差责任差额深入；仅采用 no-MASK 与 integrated score-entropy 条件下 d 次 FHS 无额外离散化项，不授并行 reveal、所有 sampler 下界或墙钟加速。未遍历全部 proof；root 必要原源/actual owner PRE 通过，实际正文、完整邻接与自身末注经 root 非作者 POST 通过，窄锁释放。未核实现/复现，不授日级完成。

- `SF-2026-ARXIV-2602-21429` — Daily `2026-02-27`；[Constricting-CBF exact-v1](https://arxiv.org/html/2602.21429v1) §3–6/A.2。2+2+3=7，初始化relaxation→收缩tube→已知采样noise/QP接口深入；feasibility/Taylor残差、PushT同100步成本、learnedbarrier/latentdecoder与physical提交边界近文。pathKL冒final等式与连续white-noise硬保证明确不采用；不隔离有效有限经验。root必要源/actual owner PRE通过授两段窄锁；root非作者已实际独读正文/完整邻接/自身末注，POST通过，窄锁释放，未核实现或复现，非日级Gate。

- `SF-2026-ARXIV-2602-20497` — Daily `2026-02-26`；[exact-v1](https://arxiv.org/html/2602.20497v1) §3.2/Eq4–7、Table4、§7.1–2/Table8。2+2+2=6，按noise阶段历史feature预测与GT→closedloop训练差额深入；N5 stage微增益/N10保真退步、predictor/轨迹/驻留和刷新费用、不同模型硬件/质量proxy分账近正文，不授环境真值或总费普胜。root实际必要源/owner PRE及正文（写时556/558）、完整552–568/自身1741末注非作者POST通过，锁已释放；此次仅同步自身末注，不重排正文或27新增21429。未核代码/复现，非日级Gate。

- `SF-2026-ARXIV-2602-14381` — Daily `2026-02-18`；[exact-v1](https://arxiv.org/html/2602.14381v1) §3–4必要范围。2+2+2=6，reference条件与generated-history缓存分工差额深入；inactive/reactive、ghosting、额外latency/memory、inference-only及reference/长序列反侧保留，非普遍实时或质量无损。root 必要源/actual owner PRE通过，实际正文/完整邻接及本末注经root非作者POST通过，窄锁释放；未核artifact/复现，非日级。

- `SF-2026-ARXIV-2602-15031` — Daily `2026-02-18`；[exact-v1](https://arxiv.org/html/2602.15031v1) §3–4/Table3与必要§5边界。2+2+2=6，dilated-mask local与256global temporal控制分责差额深入；训练先后、全输入/codec费用、global FPS成本与LPIPS/CLIP反侧近正文。不采用全部成本只随mask或4K端到端实时/零质量损失。root 必要源/actual owner PRE通过，实际正文/完整邻接及本末注经root非作者POST通过，窄锁释放；未核artifact/复现，非日级。

- `SF-2026-ARXIV-2602-12586` — Daily `2026-02-17`；[exact-v1](https://arxiv.org/html/2602.12586v1) §3、Tables1–2、§4/6及C.1。2+1+2=5，slot-order/self-confidence look-ahead具体owner差额深入；不授target verification/答案truth，低探索反退、非matched参数与额外generation预算近正文。root必要源/actual owner PRE通过并授窄锁；作者已顺读单段与完整邻接，root实际正文/完整邻接/末注非作者POST通过，窄锁释放；未运行实现或复现实验，不授日级Gate。

- `SF-2026-ARXIV-2602-12624` — Daily `2026-02-17`；[exact-v1](https://arxiv.org/html/2602.12624v1) §3/Eqs6–13/Alg1、§4与C.1。2+1+2=5，solver-order/secantproposal与true-sup界的具体差额深入；不采用literal负步长配方/严格runtime Wasserstein证书，stochastic配置、离线搜索/NFE与质量反侧近正文。root必要源/actual owner PRE通过并授窄锁；作者已顺读单段/完整邻接，root实际正文/完整邻接/末注非作者POST通过，窄锁释放，未核实现或复现，非日级Gate。

- `SF-2026-ARXIV-2602-15008` — Daily `2026-02-18`；[CTMC sampling exact-v1](https://arxiv.org/html/2602.15008v1) §2.2/3.1–3.2、Th1–3、Algorithm1及Eq18–19，exactPDF对照。2+2+2=6，mask时间重标度/空间冻结与结构依赖误差差额深入；score/init/dependence、末步去mask、合法rate/非零去向、uniform τ-leaping path-KL限定均保留。iteration bound不等真实dS计算/硬件成本，不授实测质量/速度。root必要源/actual owner PRE及实际正文/完整邻接与末注非作者POST通过，窄锁释放；未核实现或复现，非日级。

- `SF-2026-ARXIV-2602-13185`，Experimental：[FlexAM exact-v1](https://arxiv.org/html/2602.13185v1) §3–4 与必要对照；初始点 identity、当前 motion/depth/mask、局部外观及密度条件分责，不授物理真值或全质量支配。冻结主干/控制训练、稀疏人口差异、qual-only ablation、camera translation 反退和 tracker/采样成本保留；必要原源与实际 owner PRE 已 root 独核，单段实际正文/完整邻接/末注经 root 非作者 POST 通过，锁释放；未复现实验，不授日级完成。

- `SF-2026-ARXIV-2602-15396` — Daily `2026-02-19`；[exact-v1](https://arxiv.org/html/2602.15396v1) §3.1–2/Algorithm1、Tables2–5及必要配置。2+2+2=6，具体coupling差额深入；只采forward学习后冻结的端点监督条件，保留AM/terminalCM交替、approx非optimal、coverage/曲率、2100总训练与forward求值成本/precision反侧。root必要源/actualowner PRE通过；实际正文、邻接及末注root独立POST通过，未核实现或复现。

- `SF-2026-ARXIV-2602-12528` — Daily `2026-02-17`；[DiffuRank exact-v1](https://arxiv.org/html/2602.12528v1) §4.3/5.1/5.3/5.4.2。2+1+2=5，具体 owner gap 受影响深入，仅采用 all-different permutation/slot-marginal assignment surrogate，预算、反侧及回退近正文；不授 joint 语义、普遍质量/物理或完整约束保证。root 必要原源/actual owner PRE通过并授窄锁；root 已实际核正文/完整邻接与本末注，非作者 POST 通过，窄锁释放。未核代码或复现，日级未验。

- `SF-2026-ARXIV-2602-10953` — Daily `2026-02-13`；[SOAR exact-v1](https://arxiv.org/html/2602.10953v1) §3.2–3.3/Tables1–3/§4.3–4.5。2+1+2=5，具体position beam/parallel-origin collapse接口差额深入；score非joint probability、不可回改commit、beam成本与adaptive-parallel反侧近正文。root必要原源/current owner/邻接PRE通过；root实际核当前正文300–333（新增316/318）及末注，非作者POST通过、窄锁释放，不授日级；未核代码或复现。

- `SF-2026-ARXIV-2602-10825` — Daily `2026-02-13`；[FlowCache exact-v1](https://arxiv.org/html/2602.10825v1) §3、Tables1–4/6及B/C/D2。2+2+2=6，具体多active chunk phase/age与completed-clean/active KV责任差额深入；不采用争议单调定理、全部quality无损或原Eq20实现。metadata/选择成本、PhysicsIQ反侧、full计算/历史回退近正文。root必要原源/current owner/邻接PRE通过；root实际核正文1180–1203、邻接与末注，非作者POST通过、窄锁释放，不授日级。未核代码或复现。

- `SF-2026-ARXIV-2602-10764` — Daily `2026-02-13`；[Dual-End CM exact-v1](https://arxiv.org/html/2602.10764v1) §4/Alg1、Table3–4/§6。2+1+2=5，终点/diagonal/noise-to-intermediate子轨迹接口缺口定点深入；保留非精确组合、去norm两步反侧、争议公式不采用与JVP执行限制，不授少步无损或生产速度。root必要原源与current owner/邻接PRE通过授窄锁；root已实际核正文、前后邻接与末注，非作者POST通过（Ch24 noise-to-intermediate定点措辞已同步），窄锁释放，不授日级。未核代码或复现。

- `SF-2026-ARXIV-2601-16971` — Daily 2026-01-27；[ARMD exact-v1](https://arxiv.org/html/2601.16971v1) §3 双流构造与 §4 质量/计算对照。2+2+2=6，query 与 KV 同时排除本 block 标签的具体可见性缺口定点深入；不与 MARS 的 clean/masked stream 对齐规则混同，不采用无损并行、通用速度或大模型保证。未运行实现或复现实验；root 非作者实际原源→690–692正文/邻接及本注写后复核通过，日级 Gate 待验。

- `SF-2026-ARXIV-2602-06161` — Daily `2026-02-10`；[exact-v1](https://arxiv.org/html/2602.06161v1) §5.1–5.3、AppB.1–4、§6.1/6.4/6.5。6=2+2+2，因局部 exactness 的具体采用边界深入；root 必要原源及 owner 写前核通过。只采用 seed draft/verify 两视图和 fixed-Q/off-diagonal 单 row 校正，不授全网无泄漏、分布精确或通用速度；joint KV 消融及 drift 相关代理反侧保留。LLaDA/Dream、4×H200、greedy/block64有限作者结果，未核代码或复现；root 实际正文/邻接及源注非作者POST通过，日级Gate未授。

- `SF-2026-ARXIV-2602-04399` — Daily `2026-02-06`；[Swordsman exact-v1](https://arxiv.org/html/2602.04399v1) §3.1–3.3/Eq13–16、§4.1–4.3/Table1与§5。原2+2+2=6，具体两个控制对象接口gap深入；只采用remaining entropy-shift分块与历史最大块平均熵/块内变化调门槛的分工，不授语义独立、cache exactness、通用质量/端到端加速。三DLM/H200/长度512与固定块32局部配置、质量反侧及额外forward/阈值成本保留，未复现。jan01_v3必要原源→owner写前独立核通过，root授窄写；root实际读取Ch24 255–266及本注，实际POST通过，日级Gate未验。

- `SF-2026-ARXIV-2601-02076` — Daily `2026-01-07`；[DCD exact-v1](https://arxiv.org/html/2601.02076v1) §5.1–5.3、模型协议、§6.3–6.4及hardware/limitations。2+2+2=6，eligible window/强制推进与temporary KV刷新接口缺口深入；不授prefix永久精确、跨训练块重排或通用质量/成本收益，A100与A800等不同资源对照不合并。root实际必要源与Ch24 owner写前及实际新增段/邻接/末注非作者POST通过；未运行代码或复现。

- `SF-2026-ARXIV-2601-01955` — Daily `2026-01-07`；[MotionAdapter exact-v1](https://arxiv.org/html/2601.01955v1) §3.2–3.4/4.1/4.3/4.4/8.2。2+1+2=5，具体reference形状→target motion correspondence缺口深入；采用抽取/warp/guidance接口与匹配失败、成本及回退，不授物理真值。MF full .550低于no-extraction .772，20人偏好为另一protocol；10.5min/49帧/4090不作免费生成或通用性能。root已实际必要源/owner写前及实际一段、邻接与末注非作者POST通过；未运行代码或复现。

- `SF-2026-ARXIV-2601-02204` — Daily `2026-01-07`；[NextFlow exact-v1](https://arxiv.org/html/2601.02204v1) §3.2.1/8.2与受影响消融。2+2+2=6，具体输入—self-correction兼容反证gap深入；仅采用accumulated feature与direct residual/code-index输入的受限对照，complexity只是作者假说。optional refiner可改结构/default off，理论FLOPs不作同质量walltime。root必要原源/owner与实际正文/邻接/末注POST通过；未运行代码或复现。

- `SF-2026-ARXIV-2601-01608` — Daily `2026-01-07`；[exact-v1](https://arxiv.org/html/2601.01608v1) §3.2/Eq6–8、§4.1–4.2/4.4、A.2，2+2+2=6，具体 guidance 分支身份/成本缺口深入。采用同θ同condition不同γ的两支、双forward与subset/训练兼容及ω×γ联合校准；有限ImageNet/T2I/H200结果不授普遍variance或吞吐保证。root 必要源与 owner/邻接写前及实际一段/末注 POST 通过，未复现。

- `SF-2026-ARXIV-2601-00393` — Daily 2026-01-06；[NeoVerse exact-v1](https://arxiv.org/html/2601.00393v1) §3.1 bidirectional motion、§3.2 sparse keyframe/degradation/conditioning、§3.3 generation、§4.4 degradation 与 Appendix E。仅采用 synthetic degradation→回 render 原视角配原视频→frozen backbone/control branch 的训练接口及短邻域、遮挡、二维/文字失败边界；不授真实新视角几何、action causality、通用 speedup 或生产 SLO。root 非作者必要原源→owner 写前及实际正文/相邻衔接写后复核通过；未运行代码或复现实验。

- `SF-2026-ARXIV-2601-00267` — Daily 2026-01-06；[ActErase exact-v1](https://arxiv.org/html/2601.00267v1) §3.1–3.3/Alg1/Eqs3–9、§4.1–4.2/4.5、Appendix A.1–A.3/C。采用 frozen source activation/mask 的部署条件身份、OR/重叠平均组合失效与准备成本；不授权重/数据删除、完备安全或通用性能。50/30 step 配置冲突隔离，有限 detector 与 FID/CLIP 不等真实 harm 真值。root 必要原源→实际 owner 写前及实际正文/相邻衔接非作者写后复核通过；未复现。

- `SF-2026-ARXIV-2603-04379`：[Helios exact-v1](https://arxiv.org/html/2603.04379v1) §3.1–3.3、§5.1–5.4/Table5；只采用多尺度历史压缩与训练模拟误差的受限分支，不采用通用 FPS 或无限稳定保证。Daily 2026-03-06，实际必要源及正文邻接写后非作者 root 复核通过；未复现实验。

- Daily 2026-09-30，Experimental：[LUDI v1](https://arxiv.org/html/2609.35817v1) §3–4、[RPD v1](https://arxiv.org/html/2609.36452v1) §2–4/Tables1–2、[E-MoE v1](https://arxiv.org/html/2609.37533v1) §3/Eqs5–11/§5/AppendixB.3。分别只吸收 uniform objective与token-time接口、同pass层内稳定＋unresolved-context提交、离散route混合核及train/infer router边界；受测模型与局部成本不外推生产，未认证全文定理或复现实验。sep30_evidence_check必要来源审阅并写入，实际正文/相邻衔接待root非作者写后复核，不能自验通过。

- **生成基础桥核验：** DDPM 采用 [arXiv:2006.11239v2](https://arxiv.org/abs/2006.11239v2) §2–3，重点核对 Eq.(4)、(11)、(12)、(14) 与 Algorithm 1/2 的加噪、损失权重和采样接口；正文以条件 c 扩展无条件记号，不引入其性能结果。Flow Matching 采用 [arXiv:2210.02747v2](https://arxiv.org/abs/2210.02747v2) §2–4，重点核对 CFM 梯度等价条件、Eq.(14)、(20)–(23) 的 Gaussian 条件路径与 ODE；正文用 s 区别 DDPM 的时间方向，并保留 sigma_min>0 的终点近似。本次仅核这些基础命题及与相邻段落的交接；既有案例的来源标记和实验边界保留，不声称全章来源均已重新事实审阅。

- `SF-2026-ARXIV-2604-19009`：[exact-v1](https://arxiv.org/html/2604.19009v1) §3.1–3.3/Eqs1–7/Alg1、§4.1–4.4/Tables1–4，Daily 2026-04-22。采用 detached student→fixed real/online fake score→implicit regression target→VAE 解码 reward 的训练监督接口，而非 reward 直接证明原输出或目标梯度正确。SDXL/SD3 的非全胜指标、target grouping/fake estimator/reward 成本及 NFE 非总 compute 保留。root 必要来源→Ch24 写前、实际正文及邻接写后非作者复核均通过；未复现实验，不代替整日报 Gate。
- `SF-2026-ARXIV-2604-19141`：[exact-v1](https://arxiv.org/html/2604.19141v1) §3.1–3.3/Eqs3–4、§4.1–4.4/Figures3–4/7–8/Tables1–2、AppA.1/B.1–B.2，Daily 2026-04-22。采用 patch 噪声时刻上界与平均噪声不同的训练支持条件，difficulty head 是误差代理而非校准不确定性；有限质量退步、head/异步管理成本及固定 NFE 非 wall-clock 保留。root 必要来源→Ch24 写前、实际正文及邻接写后非作者复核均通过；未复现实验，不代替整日报 Gate。

- `SF-2026-ARXIV-2604-21221`：[exact-v1](https://arxiv.org/html/2604.21221v1) §3.1–3.5、§4.1–4.5/Tables 1–3；Daily 2026-04-24。仅吸收训练期内生 persistent/local 稀疏读取和 masked-softmax 状态合同，coarse pool 不保证被删历史可恢复。Wan 1.3B、有限时长与移除 persistent 的速度—质量反向保留；不外推无限生成或完整线上 SLO。root 已完成必要源→当前 owner 写前复核，且实际正文与相邻衔接写后非作者复核通过；未复现实验。

- `SF-2026-ARXIV-2604-19079` — Daily `2026-04-22`；[exact-v1](https://arxiv.org/html/2604.19079v1) §2.1–2.4/Eq1–5、§3.1–3.4、§4/Tables1–2。仅采用两种可见 context 下最终 RNNT `(t,u)` 完整词表分布一致性与辅助 CTC 反向证据；双模式前向、现场 loss/recompute、0.16s 退步、32 A100/128M/120k 小时范围保留。XL 的表格240k与正文280k口径未合并，`C+R` 是理论等待而非 tail SLO；root 已完成必要来源→当前 Ch24 owner 独立写前复核，实际正文/邻接已由 root 非作者写后复核通过，见 papers/2026/04/_sources/V3_ROOT_CH24_TWO_WRITE_AFTER_20260928.md，未复现实验。

- `SF-2026-ARXIV-2604-19330` — Daily `2026-04-22`；[exact-v1](https://arxiv.org/html/2604.19330v1) III-A/B Eq1/Fig2、IV-A–G/TablesI–V。采用时间降采样首 codebook 链与 RVQ residual-codebook 层级的区别，仍保 G2P+duration predictor 的总长度责任、逐级 masked passes/前级噪声/成本及 SeedTTS 局部退步；参数共享不证明 total compute、首包或自然度普遍更好。root 已完成必要来源→当前 Ch24 owner 独立写前复核，实际正文/邻接已由 root 非作者写后复核通过，见 papers/2026/04/_sources/V3_ROOT_CH24_TWO_WRITE_AFTER_20260928.md，未复现实验。

- `SF-2026-ARXIV-2604-20289`（Experimental，部分 Disputed）：[exact-v1](https://arxiv.org/html/2604.20289v1) §2–5/Table1–3，Daily 2026-04-23。采用跨chunk按 `(step,block)` residual 缓存与 clean KV-update pass 强制全算；只支持作者 X-World、四步、七相机12 FPS、13段约22秒同分布轨迹、单 Zhenwu 810E PPU/BF16 DiT 部分。VAE/I/O/跨设备与端到端SLO未测；Table3移除KV保护的PSNR 53.384→21.461虽提示受限污染，但skip 71.3%→62.8% 与§4.2“增加约9个百分点”矛盾，隔离后者及由其导出的比较。apr20_resume已完成非作者 source→当前 Ch24 owner及实际正文/相邻段写后复核（`daily-20260423/V3_APR20_LAST_TWO_INDEPENDENT.md`），未复现实验。

- `SF-2026-ARXIV-2604-19473` — Daily `2026-04-22`；[exact-v1](https://arxiv.org/html/2604.19473v1) §3.2–3.4/Eq1–11、§4.1–4.4/Tables1–4。采用完整prompt下 frame×subject/event interval 的受限 cross-attention bias，不把attention mask、GPT-4o评分或物理连贯性当独立真值；时段可由用户/GPT-4o-mini/均分给出，T2V早20%与I2V早40%去噪受测。Wan2.2 StoryEval 48.3→56.2，单独EAM为51.9；单A100、480×832/81帧846→863s含平均2.65s分段调用，multi-prompt帧数约81×事件数不严格匹配。precision、batch、concurrency、tail SLO未披露；root已完成必要来源→当前owner写前及实际正文/相邻衔接写后独立复核，见本日 `V3_ROOT_19473_WRITE_AFTER.md`，未复现实验。

- `SF-2026-ARXIV-2604-15804` — Daily `2026-04-20`；[exact-v1](https://arxiv.org/html/2604.15804v1) §2.4–2.5 / Tables1–2。ARIA 只为单流 text/speech prefix-rate 提供受限机制；输入 video 约160ms temporal-ID、AuT 6.25Hz/40M 小时属不同表示或训练分支，不把全部质量或延迟归 ARIA。Table2 Flash 音频/视频 1 并发235/426ms、8 并发352/1625ms，Plus 为435/651→955/1980ms，均 theoretical；硬件/precision/完整队列 SLO、ARIA 单独消融与在线全局比率取得方式未披露。不采用跨模型/语言全胜或生产保证。root 必要 source→实际 owner 写前通过，且已核 apr20_resume 的实际正文、相邻交接与本条证据边界，非作者写后复核通过；未复现实验。

- `SF-2026-ARXIV-2604-18739` — Apr22；[exact-v1](https://arxiv.org/html/2604.18739v1) §3.1–3.3/Eqs11–19、§4.3–4.4。terminal 指数倾斜→局部条件匹配，base/schedule/buffer 假设、sample target 非自动 simplex、有限训练/质量成本边界已入正文；root 写前必要来源与真实 owner 采用、实际正文与相邻衔接非作者写后均通过，未复现。
- `SF-2026-ARXIV-2604-18839` — Apr22；[exact-v1](https://arxiv.org/html/2604.18839v1) §3.1–3.3/Eq6–7、§4.4–4.5/Table1。腐化 target→短递归窗末端监督不同于 prefix distill；SPRM 退步、配置/数据/候选混杂与长程未证保留。root 写前必要来源与实际 owner 采用、实际正文与相邻衔接非作者写后均通过，未复现。

- `SF-2026-ARXIV-2604-15439` — Daily2026-04-20；[v1](https://arxiv.org/html/2604.15439v1) Def1–4/P1–C4/T5/T6/C12及P10必要反例。random affine sample与conditional ODE直流区分进入并行/少步主线；充分方向PSD Jacobian、Gaussian特调辅助噪声及两个分离uniform混合的有限no-go条件保留，不外推任意多峰/全维。root必要source→actual owner窄采用及实际正文/相邻写后通过，非日Gate。
- `SF-2026-ARXIV-2604-15694` — Daily2026-04-20；[v1](https://arxiv.org/html/2604.15694v1) §4.1/P4.8/absorbing特例、§4.2/AppD两sampler及§5必要评价。Poisson timing+真实rate加权destination进入joint artifact链；conditional/marginal一阶假设、Euler合法性与τstep不等NFE保留。163M/512/TinyStories/OWT、Gemma2 finite-sample genPPL不是数学上界，OWT协议分歧不补造；hardware/precision/batch/SLO未披露。root写前及实际正文/相邻写后通过，不称复现或日级完成。

- `SF-2026-ARXIV-2604-15453`：[SoTo v1](https://arxiv.org/html/2604.15453v1)，Daily 2026-04-20；§3–5.5/§7、D.3、E.4、G。采用 ordered prefix→partial reconstruction→beam 的条件分支，保留 matched 2D 比较、NFE≠时间、detokenization 成本及 verifier hacking/弱 prior 反例；不采用 Appendix B 全局界。apr02 必要 source→实际 owner 独立采用通过；root 实际正文与相邻衔接非作者写后核验通过，未复现实验。

- `SF-2026-ARXIV-2604-16514`：[exact-v1](https://arxiv.org/html/2604.16514v1)，Daily 2026-04-21；§3.1–3.2/Algorithm1、Table4。采用 AR next-token 与 same-position corrupted-state 蒸馏的监督支持区分；固定 block anchor、多阶段预算与 ChartQA 反例保留，不采用普遍无损迁移或训练 compute 匹配。apr02 必要 source→当前 owner 独立通过；实际正文及相邻衔接写后非作者复核通过（root），未复现实验。

- `SF-2026-ARXIV-2604-10103`，Experimental：[exact-v1](https://arxiv.org/html/2604.10103v1) §3.2–3.5、§4.1及主表。采用evicted-only线性history与local窗口分责、evict前移交、dense→hybrid训练和position/teacher-target身份；不推无损无限记忆、causal world model或任意负载SLO。apr02必要来源→实际owner及真实正文/相邻衔接写后复核通过，未复现实验。

- `SF-2026-ARXIV-2604-13470`（Experimental）：[exact-v1](https://arxiv.org/html/2604.13470v1) §2.3、§3.1–3.4、§4 Proposition4.1/Theorem4.2/Remark4.3；采用 reverse-kernel 表达性、逐步近似与 terminal mismatch 分层，保留有限特征/正则假设、exact matching 与高维成本，不把上界项当所有架构严格下界或可学/部署优势。root本轮必要源→实际owner采用通过；本次实际正文与相邻交接已由 root 非作者写后核验通过，未复现实验。
- `SF-2026-ARXIV-2604-13491`（Experimental）：[exact-v1](https://arxiv.org/html/2604.13491v1) §3.2/Table2、§4、§6.2/Table5/AppendixA.3；采用 retry trigger 与 rationale 内容消费分离，368/2212选中No整体.82持平不推逐例bypass；显式反馈、第三轮与颜色反例及VQA/edit成本保留。root本轮必要源→实际owner采用通过；本次实际正文与相邻交接已由 root 非作者写后核验通过，未复现实验。
- `SF-2026-ARXIV-2604-13540`（Experimental）：[exact-v1](https://arxiv.org/html/2604.13540v1) §4.2–4.3/Eq6–12、§5.1/5.4；采用 CLIP(c_ideal) 梯度 proposal 与 CLIP(c_user) 选择目标分开，不采用正交projection/独立truth/免费；H800、look-ahead/backprop、多候选及K5和任务切片退步保留。root本轮必要源→实际owner采用通过；本次实际正文与相邻交接已由 root 非作者写后核验通过，未复现实验。
- `SF-2026-ARXIV-2604-14001`（Experimental）：[exact-v1](https://arxiv.org/html/2604.14001v1) §3.1–3.2/Eq4–8、§4；采用 MDLM 互补mask pseudo-score 重排与USDM dense vocab/首CTC帧非blank归一融合分离，不冒充精确joint likelihood/posterior；LibriSpeech有限架构/词表、MC/NFE成本与AR joint更强保留。root本轮必要源→实际owner采用通过；本次实际正文与相邻交接已由 root 非作者写后核验通过，未复现实验。

- `SF-2026-ARXIV-2604-15009`（Experimental）：[YAN/MoE-FM v1](https://arxiv.org/html/2604.15009v1)，Daily `2026-04-17`。采用§3.1–3.2/Eq4–6/§4–5/Table1的mixture likelihood responsibility与起点冻结token transport分支；普通FM非数学无效、dense非稀疏、退化/oracle length/bAbI反例保留。复用 `V3_ORDINARY_TEN_TWO_INDEPENDENT_AUDIT.md` §7及root当前必要采用PASS；本次root顺读真实完整正文及相邻交接写后PASS（14591歧义修后再次读句通过），未复现实验，不预支日级Gate。
- `SF-2026-ARXIV-2604-14379`（Experimental）：[MSDDA v1](https://arxiv.org/html/2604.14379v1)，Daily `2026-04-17`。采用§4.1/Eq3/§4.2 Theorem1/Eq6–7/§5的局部reverse conditional融合接口；共同reference/KL/Gaussian/surrogate最优条件、DPOK未证最优、多base执行与reward退步保留。复用 `V3_ORDINARY_TEN_THREE_INDEPENDENT_AUDIT.md` §8及root当前必要采用PASS；本次root顺读真实完整正文及相邻交接写后PASS（14591歧义修后再次读句通过），未复现实验，不预支日级Gate。
- `SF-2026-ARXIV-2604-14591`（Experimental）：[Masked Logit Nudging v1](https://arxiv.org/html/2604.14591v1)，Daily `2026-04-17`。采用§3.2/Eq6、§3.3/Eq9、§3.4、§4/Table1及§6.1.1/Table4的source概率方向加logits、两pass mask及局部codebook修复；style关refinement、非CFG/无损、mask成本/SSIM退步保留。apr01旧转传收据不是新审阅或原附件；root本轮已定点重开官方必要原文/实际Ch24交接，必要采用PASS；本次root顺读真实完整正文及相邻交接写后PASS（14591歧义修后再次读句通过），未复现实验，不预支日级Gate。

- `SF-2026-ARXIV-2604-09921`，Experimental：[exact-v1](https://arxiv.org/html/2604.09921v1) §2.2、§3.1–3.2、§4.1–4.3、§6；采用 token/position sampling 分责，不采用一般并行正确性。理想化 anchor/fork 与 TLC K=1 的证明不外推，precision、线上 batch/concurrency/SLO 未完整披露；NFE、固定时长训练与最终 selector 分账。apr01 必要源/真实 owner 提案及实际正文与相邻交接的写后独立核验通过。

- `SF-2026-ARXIV-2604-12617`（Experimental）：[exact-v1](https://arxiv.org/html/2604.12617v1) §2.3 Eq6–12/Algorithm1、§3.1–3.5。采用 own detached 单步与 same-noise clean-anchor 纠偏训练；不采用唯一 Bayes 真值、完整 inference support 或同总 compute 优势。root 必要源/owner 与实际两段及相邻交接写后独立通过，未复现实验。

- `SF-2026-ARXIV-2604-09227`（Experimental）：[exact-v1](https://arxiv.org/html/2604.09227v1) §3 Eq4–11/Alg1、§4–5/AppendixB。D–velocity commutator与stored HR局部修正；preview筛seed/prompt后HR重跑，不是LR上采样exact续算。Flux1dev/SD3.5L、A100、PixArt30K随机5000prompts（2–1885chars）、受测500轨迹；5step局部cosine不作普适solver/交付SLO保证，precision/batch/生产并发SLO未披露。6分gap深入，必要源/owner非作者核通过（apr03），实际正文/相邻论证写后非作者复核通过（apr03）；未复现实验。
- `SF-2026-ARXIV-2604-09057`（Experimental）：[exact-v1](https://arxiv.org/html/2604.09057v1) Methods、Tables2–5/AppendixF–G/Limitations。video轨迹搬运endpoint+soft mask/等区域loss，audio8D kinematics conditioning，2D非物理因果。Ovi720×720/5s、32A100/bf16、batch32/30ksteps、50代表视频；单模态与joint指标各有反例，生产并发/SLO未披露。6分gap深入，必要源/owner非作者核通过（apr03），实际正文/相邻论证写后非作者复核通过（apr03）；未复现实验。

- `SF-2026-ARXIV-2604-09168`，Experimental：[exact-v1](https://arxiv.org/html/2604.09168v1) §3 ILSD/Eq1–2、§4.1–4.2/Figure8与Limitations。同图full-depth target stop-grad，中间prefix共享θ；ImageNet256/UCF16×128×128、codebook1024、270epochs，DiT SD1.4VAE/batch512/500k/512DDPM/CFG3。N1×L32 FID10.30、超过Lmax退步限制‘任意深度’，硬件/precision/生产SLO Not Disclosed，不宣称无额外训练成本或NFE即wall-clock。未复现实验；本次必要来源、实际正文及相邻论证的非作者独立复核通过（root）。
- `SF-2026-ARXIV-2604-09181`，Experimental：[exact-v1](https://arxiv.org/html/2604.09181v1) §3–4/Alg1–2、§5/§6.1–6.2。Gaussian μ/Σ参数连续插值而非Bernoulli二分量抽样；κ=x1仅训练可见时部署standardGaussian。低β对高NFE有反收益，FFHQ4NFE不全面更好；Eq5与Alg1 KL对象不同，不采用exact目标一致性保证。CIFAR10/FFHQ/AFHQ64、作者FID/NFE；硬件/precision/生产SLO Not Disclosed，不推NFE等于latency。未复现实验；本次必要来源、实际正文及相邻论证的非作者独立复核通过（root）。

- `SF-2026-ARXIV-2604-08564`，Experimental：[exact-v1](https://arxiv.org/html/2604.08564v1) §3.1–3.2、§4、Table1/§5.1–5.5。column-sum order 的证明依赖单层与固定 attention 近似；实际取 sub-block 并平均层/head。Fast-dLLM-v2 1.5B/7B、LLaDA1.5-8B，单 A6000、GSM8K/MATH/HumanEval/MBPP；1.5B Parallel MATH31.02低于Confidence32.24，7B Parallel MATH51.88低于Entropy51.92。precision、输入输出长度、batch、并发与生产SLO在采用证据中未披露；峰值FLOPs估算不当实测成本。本次必要原文与实际正文/相邻交接已由root独立复核通过；未复现实验。

- DMax（Status: Experimental，SF-2026-ARXIV-2604-08302）：[exact-v1](https://arxiv.org/html/2604.08302v1) §3.1–3.2 Eq3–10/Algorithm1、§4.1–4.3/Table1–3。采用 on-policy 错误噪声、soft token/MASK 输入与启发式停止的耦合，不采用原分布保持/全局收敛/事实正确保证。LLaDA-2.0-mini，训练八H200、两epoch、batch8、block32，0.7M math/1M code self-distillation；推理两H200 TP、batch1、generation2048，precision/生产并发/SLO未披露。Table3软路径未OPUT为0%，OPUT后最激进soft约90.4%而hard68.2%；部分Table1切片低于原checkpoint，TPF与TPS分开。作者必要源和实际正文已核，待root非作者写后；未复现实验。

- `SF-2026-ARXIV-2604-08964`，Experimental：[exact-v1](https://arxiv.org/html/2604.08964v1) §3.3/Eq4–7、§4.1/阈值与history消融、AppD/E。current-distribution anchor→历史加权KL→future-block unlock；bounded embeddings 的过去分布接近不证明未来正确。LLaDA-8B/1.5 默认256 generation/32 block、history6，MMaDA/DIFFA另测；default阈值0.01与消融0.02最佳属不同设置，不能写成统一recipe。DIFFA Wildvoice2.76<2.80，非全部任务质量改善。hardware/precision/batch/concurrency/tail-SLO未在所采用证据披露，不采用通用latency倍率。root 已完成必要原文与实际正文/相邻链路的写后独立复核，通过，本地实验未复现。

- `SF-2026-ARXIV-2604-06333`（Status: Experimental）：[exact-v1](https://arxiv.org/html/2604.06333v1) §2–5/§6 支持 sample-space drift 的归一化与可积性条件；不否认参数空间 scalar surrogate loss，不采用固定全局下降或普遍质量增益保证。必要原文、实际正文及相邻衔接的非作者复核通过（root），不代表整日报验收。

- `SF-2026-ARXIV-2604-08557`（Status: Experimental）：[exact-v1](https://arxiv.org/html/2604.08557v1) §3–4、§6/Limitations。v1 TrajHijack只支持可观察/修改中间denoising状态的white-box威胁模型；LLaDA-8B-Instruct/Dream-7B-Instruct，64步，greedy与deterministic linear schedule，HarmBench159及固定50行为消融，Claude Sonnet单judge。两组件各自0%不等于组合无效，gradient增强反而退步；monotonic mask check只是定义性挡该路径，其他防御属建议未验证。模型/硬件/精度/生产并发/SLO不能从ASR外推；未复现实验，本次写后独立复核通过（root）。

- `SF-2026-ARXIV-2604-07404`，理论受限：[exact-v1](https://arxiv.org/html/2604.07404v1) §4/§5.4/§6.1–6.3/§7.1/§11.2–11.3。采用heat→score/Burgers与指定positive smooth binary decomposition的局部界面解释、对称Gaussian中心反向扰动增长；`τ=σ_noise²/2`、`σ_τ²=σ_0²+2τ`，不是物理时间或所有轨迹全局Lyapunov保证。恒等式与局部积分必要式已核，不把非高斯数值示例、机器精度identity检查当trained模型实验；没有对真实U-Net/多模态生成验证新的adaptive sampler或速度质量收益，三模态junction/learnedcurl/stochastic correction仍未闭合。正文“平均score误差不足以逐轨迹保证”是基于局部敏感性的设计推断，不是作者报告的MSE比较实验。2+1+2=5因知识缺口深入，未运行实现，待root独立写后复核。

- `SF-2026-ARXIV-2604-07402`（Experimental）：[exact-v1](https://arxiv.org/html/2604.07402v1) §4.1–4.4、§5.2、§6.1–6.2 与 Appendix D/E。正文采用完整历史条件与局部 loss/gradient 的分离，不采用 Eq10 的全局 Lipschitz/误差保证。实验限 OmniTokenizer、110/343M、17帧256²、四张A100与作者视频数据；Table2 的 Local-Opt 单独质量退化、窗口重叠与连续性权重反证均保留，未复现实验。

- `SF-2026-ARXIV-2604-06491`，Experimental：[exact-v1](https://arxiv.org/html/2604.06491v1) §3.4、§4.1–4.3、§5及§7。采用合法Euler一步概率构造inner MDP的接口，不采用普适terminal-TV或无误差保证；DNA代理评价不证明大模型文本、真实功能或生产收益。apr01已独立核对必要原文与实际正文；未复现实验。

- [MARS 2604.07023v1](https://arxiv.org/html/2604.07023v1)，Experimental；§3.1–3.4、Tables2–5、Limitations与AppendixA。采用causal双流训练、AR-loss保留及近似连续接纳；1/B为干净上下文位置的计数proxy，不是能力保证。Table2所谓compute-matched只匹配epoch，AppendixA披露MARS每阶段约两倍H200-hours；速度表固定GSM8K256题、Qwen2.5-7B、τ=.95、batch4/8/16，推理GPU数未独立说明，不外推生产并发。

- `SF-2026-ARXIV-2604-06832`（Experimental）：[官方 PDF v1](https://arxiv.org/pdf/2604.06832v1) §3.2–3.4/Figure3、§4.1–4.5/Tables1–2。采用 response-only corruption、clean-only vision、turn-end truncation 与 causal 验证/KV 裁剪的接口分支。Qwen2.5-VL-3B、block curriculum 2→32、两项 CE 权重均0.5；单 H100 batch1，优化路径含 SGLang/W8A8 FP8，不将该优化吞吐当未量化 baseline 的通用收益。短回答平均 MDM73.3/AR74.0，MMMU-Pro-V 长回答21.4/26.3，spec24.6，不能称无损。两路径采用已对齐VLM与text-only LLM不同初始化，所谓相同ceiling仅作者假设。本轮必要正文和实际上下文已作者核对，待root非作者写后复核；未复现实验。

- `SF-2026-ARXIV-2604-03537`（Experimental）：[exact-v1](https://arxiv.org/html/2604.03537v1) §3.1–3.4、§4、Tables1–2 与 level-weight/step 消融。仅层内过程具所述 CTMC 解释，跨层阈值有奇点；overall ELBO按层求和。head节省后模型深度重配不是所有变量不变的比较，small/base结果有例外，粗层权重/步数不是越大越好。未复现实验；本次写后独立复核通过（root）。

- [2604.05656v1](https://arxiv.org/html/2604.05656v1)，Theoretical / Experimental；§3.3–3.4及§4、AppendixF。采用conditional/marginal替换在不同目标下的边界与有限步shortcut；不沿用全文中无条件的“方差处处非零”或真实机器人加速推测，FM仍保留，LIBERO模拟和推理计时分账。

- `SF-2026-ARXIV-2604-01624`，Status: Experimental：[exact-v1 §3–6 与 Limitations](https://arxiv.org/html/2604.01624v1) 用随机 reveal order 的跨链分歧定位、证据条件局部 remask；只测试 LLaDA-8B/Dream-7B 与作者 QA/RAGTruth 协议。LLaDA 的 EM-AUROC 76.4 低于 DynHD 84.2，LLM-judge 重标后才为 86.5；8 链在 4×H200 的约 1.3× wall-clock 伴随约 1.67× 峰值显存，不证明开放域真值置信或生产 SLO。

- Qwen-Image-2.1（Status: Experimental）：[官方发布与仓库](https://github.com/QwenLM/Qwen-Image-2.1)披露 32 层 single-stream DiT、token-causal / chunk-level mixed mask，以及 condition image 与 instruction 的 prefix KV reuse；只采用由公开架构直接支持的 cache identity 与 invalidation 合同。作者页面没有完整披露可比较的 hardware、batch/concurrency、SLO、独立复现与不确定性，因而不采用 headline quality/performance 结论。

- `SF-2026-ARXIV-2605-04291`（Status: Experimental）：[exact-v1](https://arxiv.org/html/2605.04291v1) 支持用预训练 causal/masked LM 的条件分布定义 Glauber-style 局部重采样，并以多轮 revision 换取全局纠正；有限步 sampler 不证明 stationary convergence，训练/NFE 成本、streaming 与生产 SLO 也未被普遍证明。
- `SF-2026-ARXIV-2605-06885`（Status: Experimental）：[exact-v1](https://arxiv.org/html/2605.06885v1) 支持在同构 Qwen3 模型和作者代码任务中以逐层表示对齐辅助 AR→masked-diffusion 迁移；不证明行为等价、跨架构迁移或普遍质量优势。

- 2026-09-01 可变 canvas 的状态绑定：<https://arxiv.org/html/2608.30922v1> §3.2、Algorithm 与 C–F。平均 JS 不覆盖已提交/新增位置，不构成无损证明；always-expand 对照同时改变判定和 expanded forward，不能隔离 JS 判定因果。三模型四任务及 MI210 测量不外推生产 SLO。

- `SF-2026-ARXIV-2609-04531`，Status: Experimental：exact-v1 §2.4、§3.1/3.3、§5与B.5支持student中间轨迹监督及按K分别训练的少步分支。仅采用公开代码生成设置下的机制；不采用任意权重下稳定反向映射保证，也不把K、NFE与wall-time等同。https://arxiv.org/html/2609.04531v1

- `SF-2026-ARXIV-2602-00612`（Status: Experimental）：primary=`arXiv:2602.00612v1`；Method=`§3 Methodology`；Evaluation=`§4.1 Benchmark`；Non-proof=`§7 Conclusion`。证据只支持 dLLM 在所测 CFG benchmark 中用并行位置分布做 lookahead、拒绝不可完成 proposal；不证明语义正确、任意 grammar 复杂度或生产延迟。

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

- `SF-2026-ARXIV-2602-16132` — Daily `2026-02-20`；[CHAI exact-v1](https://arxiv.org/html/2602.16132v1) §3.2–3.3、§4.1–4.4与§6。2+2+2=6，跨请求 entity donor 的旧 K/V 与当前 Q 接口差额深入；首步/首block限制、非exact污染、索引同步淘汰、lookup/存储预算与miss全量路径保留，不把预置100%命中或3.35×归为单机制因果/生产能力。root必要source/actual owner PRE及实际正文/完整邻接/末注非作者POST通过，窄锁释放；未核实现或复现，非日级Gate。

- `SF-2026-ARXIV-2602-16198` — Daily `2026-02-20`；[DOIT exact-v1](https://arxiv.org/html/2602.16198v1) Eq9/Alg1–2/§5 A5.1–A5.3/Th5.4/T1/§7及C4必要反側。2+2+2=6，无h训练的transition-score MC与full→surrogate接口差额深入；rare-event/正分母/support/score导数、reward调用与runtime排除、实际Alg2非理论exact在正文，不搬TV公式或通用oracle性能。root必要source/actual owner PRE通过授一段窄锁；作者正文/完整邻接已顺读，root实际正文/完整邻接/末注非作者POST通过，窄锁释放，未核实现或复现，非日级Gate。

- `SF-2026-ARXIV-2602-16092` — Daily `2026-02-20`；[exact-v1](https://arxiv.org/html/2602.16092v1) §2–5与§6 Limitations。2+1+2=5，防标签泄漏与locality张力的具体差额深入；不授two-stream必要性、无直接双流对照或大模型因果结论。root必要原源/actual owner PRE通过授一段窄锁；作者正文/完整邻接已顺读，root实际正文/完整邻接/末注非作者POST通过，窄锁释放；未核实现或复现，非日级Gate。

- SF-2026-ARXIV-2606-27732 — primary arXiv:2606.27732v1; exact-v1 URL=https://arxiv.org/html/2606.27732v1; Method=https://arxiv.org/html/2606.27732v1 — §3 Method; 3.4 R2LM Architecture; 3.5 Training and Inference; Evaluation=https://arxiv.org/html/2606.27732v1 — §4 Experiments; 4.1 Experimental Setup; 4.2 Main Results: Multiple-Choice Benchmarks; Non-proof=https://arxiv.org/html/2606.27732v1 — §5 Conclusion。

### Daily Books delta trace（2026-06—08）

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
- `SF-2026-ARXIV-2607.27372` — Daily `2026-07-31`；primary `arXiv:2607.27372v1`；Books review `books-review:SF-2026-ARXIV-2607.27372`。

  **已吸收的语义增量：** 新增证据边界：Explorative Modeling factors the training loop over multiple candidate matches and trains on the selected match, making sampling during training closer to inference-time mode commitment. Exploration becomes a third compute axis, but multiplies candidate-generation cost and introduces selection bias; author scaling curves do not prove a universal replacement for AR or diffusion. 该 delta 已进入 `books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#L211`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607.27372:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-24841:start -->
- `SF-2026-ARXIV-2607-24841` — Daily `2026-07-29`；primary `arXiv:2607.24841v1`；正文锚点“Parallel Progress 与 Active Compute 是两条独立成本轴”。
  证据限翻译任务与作者 neuromorphic setting，不支持跨平台能量、普通 GPU 或生产 SLO 外推。
<!-- daily-books-trace:SF-2026-ARXIV-2607-24841:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-25157:start -->
- `SF-2026-ARXIV-2607-25157` — Daily `2026-07-29`；primary `arXiv:2607.25157v1`；正文锚点“AR 权重可以成为 Masked Diffusion 的兼容起点”。
  证据限 matched GPT-2 Medium/WikiText 与所测长度/迁移设置；同规模 tuned AR 仍更强，不支持替代结论。
<!-- daily-books-trace:SF-2026-ARXIV-2607-25157:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-25948:start -->
- `SF-2026-ARXIV-2607-25948` — Daily `2026-07-29`；primary `arXiv:2607.25948v1`；正文锚点“Any-to-any AR 把 Modality Type 移入同一生成序列”。
  证据限作者任务中的 specialist/multitask 与 chained-generation 对比；自生成跨模态评分不是独立 verifier。
<!-- daily-books-trace:SF-2026-ARXIV-2607-25948:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-26004:start -->
- `SF-2026-ARXIV-2607-26004` — Daily `2026-07-29`；primary `arXiv:2607.26004v1`；正文锚点“Few-step Distillation 要在 Student 实际访问的状态上验收”中的 multi-step proposal 分支。
  证据限作者披露模型与 4–8 NFE 设置；NFE 不等 wall time，也不证明跨域稳定或消除 mode collapse。
<!-- daily-books-trace:SF-2026-ARXIV-2607-26004:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2605-02263:start -->
- `SF-2026-ARXIV-2605-02263` — Daily `2026-05-05`；primary `arXiv:2605.02263v1`；Books review `books-review:SF-2026-ARXIV-2605-02263`。

  **写回边界：** fixed block size 增加 learned-boundary 条件分支，但 boundary 只是待 runtime 冻结和验证的 proposal；entropy trajectory 不证明 correctness，静态 shape 或阈值失配时仍使用固定 block。
<!-- daily-books-trace:SF-2026-ARXIV-2605-02263:end -->

- `SF-2026-ARXIV-2512-25014`：[exact v1](https://arxiv.org/html/2512.25014v1) §2 sampler/circuit定义，§3 Theorems3.1–3.3及O(log d)每步构造，§4 Theorems4.1/4.2/4.5和证明/末remark。采用临时符号与最终输出身份分离、revision回收workspace及uniform even-parity采样的受限AC0分离；不是parity输入计算、任意Transformer lower bound或硬件速度证明。必要原源、限定命题及实际正文/邻接已由root非作者复核通过；理论不要求hardware benchmark，未运行实现或复现实验。

- `SF-2026-ARXIV-2512-23851` — Daily `2026-01-02`；[Pretraining Frame Preservation in Autoregressive Video Memory Compression exact-v1](https://arxiv.org/html/2512.23851v1) §3.1–3.2、§4.1–4.5/Tables1–3。只采用随机历史位置重建、LR/high-frequency路径与额外预训练分账；重建不证明world state、固定memory或无限连续shot可靠，quality/evaluator分别限定，硬件为作者H100/A100训练披露而非生产Serving测量。7分必要证据深入、未复现；root必要原源与owner写前核通过，root实际正文/前后邻接及末注写后非作者复核通过。

- `SF-2026-ARXIV-2512-25066` — Daily `2026-01-02`；[From Inpainting to Editing exact-v1](https://arxiv.org/html/2512.25066v1) §3.1–3.3/4.3、C.1/C.3、F四设置。5分具体gap深入仅承载完整reference条件与编辑区域目标冲突、受校准stage adapter的训练/部署代价；D/E规模与耗时口径未统一，不采用通用三阶段律、25秒同质量或生产实时保证。未运行代码；root必要源/owner与实际正文/前后邻接写后非作者复核通过。

- `SF-2026-ARXIV-2512-24724` — Daily `2026-01-02`；[FlowBlending exact-v1](https://arxiv.org/html/2512.24724v1) §3.3、§4–6/Tables2–3。6分capacity schedule具体gap深入，限兼容latent/time/condition下离线阶段切换及代理/切换成本；小模型中段不授NFE减少、全部质量保持或生产SLO。未运行代码；root必要原源/owner与实际正文/邻接写后非作者复核通过。

- `SF-2026-ARXIV-2512-24927` — Daily `2026-01-02`；[Are First-Order Diffusion Samplers Really Slower? A Fast Forward-Value Approach exact-v1](https://arxiv.org/html/2512.24927v1) §3.1/Algorithm1、§3.2 Assumption1/Theorems3–4、§4–5/Table4。5分求值位置与实际成本gap深入，限lookahead近似/理想implicit分责及有限步反例；不授oracle可部署、固定NFE普胜或墙钟保证。未运行代码；root必要原源/owner与实际正文/邻接写后非作者复核通过。

- `SF-2026-ARXIV-2512-24731` — Daily `2026-01-02`；[EchoFoley: Event-Centric Hierarchical Control for Video Grounded Creative Sound Generation exact-v1](https://arxiv.org/html/2512.24731v1) §6.1、B.2 execution/B.3/B.4。5分具体event-state gap深入，限独立segment编辑/retime/regenerate/mix与定位/声学耦合/API预算；Temp/Timb/Vol口径争议不采用，不授生成质量或实时全链。未运行代码；root必要原源/owner写前通过，实际正文/邻接写后经root非作者实际复核通过。

- `SF-2026-ARXIV-2512-25075` — Daily `2026-01-02`；[SpaceTimePilot exact-v1](https://arxiv.org/html/2512.25075v1) §3.3 Eq3、time compressor/Table5及camera protocol反侧。6分animation-time identity gap深入，采用frame-index/动画时间、source-target camera/time分账及temporal-warp/合成网格支持条件；pose estimator/尺度对齐不是真值，不采用通用4D或生产SLO。未运行代码；root必要原源/owner写前通过，正文/邻接写后经root非作者实际复核通过。

- `SF-2026-ARXIV-2512-24639` — Daily `2026-01-02`；[From Sequential to Spatial: Reordering Autoregression for Efficient Visual Generation exact-v1](https://arxiv.org/html/2512.24639v1) §3/Eq1/Algorithm1/NAM/TPT及Tables1–4。7分采用overlap crop/ring并行、历史修正/newedge mask与mutable context分责；Eq1不授token joint exactness、cache免费或全无mask，非factorial及moreSteps反侧保留。未运行代码；root必要原源/owner通过，实际正文/前后邻接及末注写后经root非作者复核通过。

- `SF-2026-ARXIV-2512-24227` — Daily `2026-01-02`；[Mirage exact-v1](https://arxiv.org/html/2512.24227v1) §3.2.1/Eq2与Tables2–4。6分具体decoder接口gap深入，采用最后两frame-aligned upsampling层的2D detail/3D temporal分工及条件/成本回退；GTlatent近似、非factorial与数据效应分别保留，不授未来泄漏定理、全链onlinecausal或实时SLO。未运行代码；root必要原源/owner写前通过，实际正文/邻接及末注已由root非作者写后实际复核通过。
- `SF-2026-ARXIV-2512-24195` — Daily `2026-01-02`；[CorGi exact-v1](https://arxiv.org/html/2512.24195v1) §3.2–3.4/Eq2–6、§4.1–4.3/Tables1–3。6分具体cache-object gap深入，仅采用module增量/current residual分责、interval锚点及ATTN局部refresh；CKA不是因果贡献，质量/成本非单调，不授生产SLO。未运行代码；root必要原源/owner及实际正文、邻接与末注非作者写后复核通过。
- `SF-2026-ARXIV-2512-24176` — Daily `2026-01-02`；[Internal Guidance exact-v1](https://arxiv.org/html/2512.24176v1) §3.2/Eq3–5、§4.1–4.3/Eq6–7、§5.2/Tables2–4及AppendixE。6分内部弱参照gap深入，限同输入/time受训readout与同forward外推；训练预算、相关误差和非单调反侧保留，不授任意checkpoint插件、manifold真值或生产SLO。未运行代码；root必要原源/owner及实际正文、邻接与末注非作者写后复核通过。

- `SF-2026-ARXIV-2512-23818` — Daily `2026-01-02`；[Energy-based Tweedie exact-v1](https://arxiv.org/html/2512.23818v1) §2.1–2.2、§3–4/Eq12–13/17/20、§5.4.1、§6及A.2。7分采用固定posterior的score求值接口、noise β/Σ匹配与Gaussian mean充分性边界；训练参数支持、Monte Carlo与solver成本保留，二维有限seed/importance近似不授全域质量或通用reverseSDE。未运行代码；root必要原源与具体owner写前通过，实际正文/前后邻接及末注写后经root非作者复核通过。

- `SF-2026-ARXIV-2512-24378` — Daily `2026-01-02`；[Implicit score matching meets denoising score matching: improved rates of convergence and log-density Hessian estimation exact-v1](https://arxiv.org/html/2512.24378v1) Assumption3.1/Lemma3.2(ii)、Definitions3.3/3.6、Theorem3.7与受影响Jacobian证明路径。7分只采用函数/导数误差分责及高阶Sobolev、Gaussian噪声/模型类条件；不采用未核div分支或全ODE/硬件/真实生成保证。未运行实现；root必要原源/具体owner写前通过，实际正文/前后邻接及末注写后经root非作者复核通过。

- `SF-2026-ARXIV-2512-24026` — Daily `2026-01-02`；[PipeFlow exact-v1](https://arxiv.org/html/2512.24026v1) §4.1–4.4、§5.3、§8.1–8.3与§10。6分具体segment依赖gap深入，仅采用同段inversion→edit、跨段流水/overlap与skip重建的质量/成本分账；不采Eq7–9时间公式、图像CLIP作prompt alignment、无限长度或零通信保证。未运行代码；root必要原源/具体owner写前通过，实际正文/邻接及末注写后经root非作者复核通过。

- `SF-2026-ARXIV-2602-04361` — Daily `2026-02-06`；[SparVAR exact-v1](https://arxiv.org/html/2602.04361v1) §3–4、Appendix A.1 query/KV Decompose-Align-Project。原2+2+2=6，具体scale-coordinate gap深入，仅采用query-region与KV来源尺度/局部坐标迁移、近似residual重用分责；A.2 Eq4索引边界与main flat-ratio/appendix精确一致性子命题不采用，局部5.61x不授request收益。细节/误选、gather/cache成本与dense回退就近保留。未运行代码或复现；root必要原源/具体owner写前通过，root实际Ch24 52–68正文/邻接及1770末注POST通过；日级Gate未验。

- `SF-2026-ARXIV-2602-05000` — Daily `2026-02-07`；[EntRGi exact-v1](https://arxiv.org/html/2602.05000v1) §3/Algorithm1/Eqs1–8、§4/Figure5及Appendix A。原2+2+2=6，奖励输入/代理梯度接口gap深入，仅采用entropy混合的forward/backward分工与兼容性、白盒成本和独立质量退路；embedding近似界不授无偏离散梯度，Top@1/Avg@4不等人类质量，BoN与gradient方法未匹配完整算力，更多优化步数有反侧。未运行实现或复现；root实际必要原源/owner写前通过，root实际1185正文/1179–1189邻接及1774末注非作者POST通过；本日日级Gate未验。

- `SF-2026-ARXIV-2601-07568` — Daily `2026-01-14`；[d3LLM exact-v1](https://arxiv.org/html/2601.07568v1) §3.1 order-only/gold CE、§3.2状态、§4/Table5及Appendix A.6/A.7。原2+2+2=6，具体teacher-order与content-label权限缺口深入；仅采用揭示顺序的训练条件与gold监督分账，不采TPF/AUP全成本、跨target EAGLE公平普胜或缓存永久精确。未运行代码/复现；root必要原源与具体owner写前通过，jan01_v3实际正文258–276/新增266及1778末注非作者写后复核通过；未授日级Gate。

- `SF-2026-ARXIV-2601-07396` — Daily `2026-01-14`；[SVD-Cache exact-v1](https://arxiv.org/html/2601.07396v1) §3/Eqs8–9、Tables1–3、Figure5 与限制。原2+1+2=5，具体 feature 内两估计分支缺口深入，仅采用固定参考投影、principal EMA 与 residual hold；不授新输入最佳 SVD、通用阈值或无损复用。accelerated-baseline PSNR 与原模型保真分开；硬件/精度及完整预处理、驻留预算未充分披露，不授端到端 SLO。未运行代码或复现；root 必要原源与具体 owner 写前通过；jan01_v3 实际1100正文/前后邻接与1782末注非作者写后复核通过，日级 Gate 未授。

- `SF-2026-ARXIV-2601-06514` — Daily `2026-01-14`；[Doob's Matching exact-v1 PDF](https://arxiv.org/pdf/2601.06514v1) §3.3 Eqs3.13/3.16–3.19、§4.1–4.3及Eq4.3的positive lower bound/受约束模型类。原2+2+2=6，具体terminal-weight回归→gradient/log-guidance接口缺口深入，仅采用值/导数/正分母与付费训练、低噪声分账；不采用任意网络默认满足假设或完整W2/真实生成保证。PDF首页Jan13与arxivv1Jan10身份保留，HTML later build日期不当实质修订。未运行实现/复现；root必要原源、PDF身份与具体owner写前及实际正文/邻接、末注写后通过；日级Gate未授。

- `SF-2026-ARXIV-2601-08011` — Daily `2026-01-15`；[TP-Blend exact-v1](https://arxiv.org/html/2601.08011v1) §3.3 Eq5–15、3.4 Eq16–19、§4.1/4.3。2+2+2=6，具体对象位置 full-head 输出迁移与局部 style-KV/残差接口缺口深入；不采用不相容运输约束/Sinkhorn exactness、σ频率解释或几何/语义保真保证。SD-XL/有限组合样本、proxy指标、coverage/强度反侧与矩阵/多stream成本近正文保留；未运行代码或复现。root实际必要源与具体owner写前通过并授窄锁；root实际正文/前后邻接及末注非作者POST通过，日级Gate未授。

- `SF-2026-ARXIV-2602-06346` — Daily `2026-02-10`；[FlowConsist exact-v1](https://arxiv.org/html/2602.06346v1) §3/§4.1–4.2 Eq7/10–11、§5必要CFG/消融/多样性反侧及AppA方差身份/AppB配置。6=2+2+2，既有conditional/marginal方差项之外，real diagonal-estimator与自产重加噪fake-estimator的stop-gradient整流分工具体gap深入；不静默修Eq9梯度记号、不采exact KL下降/误差范数单调。131M/676M ImageNet256有限CFG搜索与pretrained SiT/REPA预算分开，aux训练成本/高CFG diversity反退保留；硬件/precision/seed/SLO未披露，未核代码/复现。root必要原源/owner写前通过，root非作者实际正文/邻接与末注POST通过，不授日级Gate。

- `SF-2026-ARXIV-2601-09255` — Daily `2026-01-16`；[exact-v1](https://arxiv.org/html/2601.09255v1) III-B/C Eq8–12、IV必要对照。6分对象脚本 coarse-motion scaffold→masked clean 替换/保 implied noise 的具体接口差额深入；不授原密度保持、物理证书或最终轨迹保证，模型更换与 mask/re-noising 混杂不作独立因果。完整 stage 成本与普通 I2V/SDEdit 回退相邻；root 原源/owner 写前通过，root 非作者实际正文/邻接与末注 POST 通过，窄锁释放，未运行代码或复现。

- `SF-2026-ARXIV-2602-06412` — Daily `2026-02-10`；[SureLock exact-v1](https://arxiv.org/html/2602.06412v1) §2 Alg1/Thm1、§3 Tables2–4、§5及AppC/D。6=2+2+2，revision/reopen至永久compute-deactivation而KV仍可读的具体gap深入；固定row/A1–4条件不外推全网或exactness，原active-set文字/算法含糊不采用。短序列PPL及runtime反侧、packing代价和退路近正文；硬件/precision/seed/SLO未披露，未核代码或复现。root必要原源/owner写前通过，root实际L571–589正文邻接与末注非作者POST通过，锁释放；不授日级Gate。

- `SF-2026-ARXIV-2601-09881` — Daily `2026-01-17`；[TMD exact-v1](https://arxiv.org/html/2601.09881v1) Algorithm1–2、§3.1–3.2、§4.1–4.3、必要 A/B。2+2+3=7；每外 denoise 新 backbone、内 conditional head 复用本外步 features 与全 inner-step 反传的预算接口，不是外 AR 或冻结主干。NFE 非 E2E、14B 两步/warmup/fusion 反侧与训练成本相邻。未核实现或复现实验；root必要原源/owner写前通过；root实际两段/前后邻接及末注非作者POST通过，窄锁释放；日级Gate未授。

- `SF-2026-ARXIV-2601-10061` — Daily `2026-01-17`；[CoF-T2I exact-v1](https://arxiv.org/html/2601.10061v1) §2.1–2.2、Table3/4/7与C2/D。6分joint latent supervision/independent frame codec具体gap深入；native causal非futureleak、三帧joint非AR、pad5混杂/局部退步/预算与fallback近正文。未核实现或复现；root必要原源/owner写前通过，root实际两段/前后邻接及末注非作者POST通过，窄锁释放；日级Gate未授。

- `SF-2026-ARXIV-2601-10403` — Daily `2026-01-17`；[DFKC exact-v1](https://arxiv.org/html/2601.10403v1) §2–3/Algorithm1、§4.2、D.2–D.3。2+2+2=6，frozen masked-model target→joint rate/weight/resampling具体gap深入；不采完整proof/exactfinite或protein成果，learnedratio/step合法性、M4vsM1非matched预算、all-transition rewardcost与有限语言反侧/退路相邻。root实际必要原源/owner写前通过并授窄锁；root已实际核两段/前后邻接及末注，非作者POST通过，窄锁释放，未核artifact或复现；日级Gate未授。

- `SF-2026-ARXIV-2601-09697` — Daily `2026-01-16`；[exact-v1](https://arxiv.org/html/2601.09697v1) §3–5/Tables1–4/A1–4必要段。2+2+2=6，仅深入采用静态camera sparse-view生成→重建/对齐→密集render的具体分工；count非选位置/覆盖保证，全部阶段成本、affine/chunk、静态限定与FID/FVD反退相邻。不授真实几何、persistent state或生产SLO；未核artifact/复现。root必要原源/owner写前通过并授Ch24窄锁，root实际两段/前后邻接1247–1258及本末注非作者POST通过，窄锁释放；日级未验。

- `SF-2026-ARXIV-2601-10632` — Daily `2026-01-17`；[CoMoVi exact-v1](https://arxiv.org/html/2601.10632v1) §3 Eq3–11、§4.5直接fused反退及必要训练/评价限制。2+2+2=6，标准必要方法后对长期采用接口深入核：两个noisy producer共同denoise，Eq6原motion推进而fused仅供3D head，区别外部clean scaffold；不授物理/3D真值或全部基线单因果。teacher标签、双branch预算与旧条件生成退路相邻。root必要原源/具体owner写前通过，root实际正文/邻接及末注非作者POST通过，窄锁释放；未核实现或复现，日级未授。

- `SF-2026-ARXIV-2601-15165` — Daily `2026-01-23`；[The Flexibility Trap exact-v1](https://arxiv.org/html/2601.15165v1) §3～5/Appendix A；2+1+2=5，设计反证与训练路径/推理 sampler 契约 gap 深入。采用 AR policy probability 归因与 parallel sampler 分账，不授 fork 因果律、joint exactness 或 conditional independence；训练预算与 token/step 非墙钟限制近正文。未核 artifact/复现；root 必要原源/owner 写前通过，实际一段/前后邻接与末注经 root 非作者 POST 通过，窄锁释放；root日级语义验收通过（完成态机器检查见Daily）。

- `SF-2026-ARXIV-2602-09501` — Daily `2026-02-12`；[Where-to-Unmask exact-v1](https://arxiv.org/html/2602.09501v1) §3.3/Gt-Margin、§4 rank-conditioned masks/独立 planner/PiRank与Table2、B/C.1。2+1+3=6，具体 where/what 接口差额深入；仅离线 gold 排序→在线预测 hypothesis planner与前半/后半 Margin fallback，不授推理 GT、低开销、并行吞吐或通用质量最优，Sudoku反退/长度冲突邻近。root 必要 source→owner 写前通过，实际两段/完整邻接/本末注非作者 POST 通过，未核代码/复现，非日级 Gate。

- `SF-2026-ARXIV-2602-09268` — Daily `2026-02-12`；[Rethinking Global Text Conditioning exact-v1](https://arxiv.org/html/2602.09268v1) §3–5/Eq3、6.1–6.3/Table1–4、H/J。2+1+3=6，pooled modulation 与 sequence attention 接口差额深入；只采用 layer-dependent 正负 modulation 分支，现成路径不训练与 CLIP-free 适配需训练分清，高scale忽略原prompt/inactive路径/对应失败及质量反退邻近。root 必要 source→owner 写前通过，实际两段/完整邻接/本末注非作者 POST 通过，窄锁释放；未核代码/复现，非日级 Gate。

- `SF-2026-ARXIV-2602-09639` — Daily `2026-02-12`；[Blind Denoising exact-v1](https://arxiv.org/html/2602.09639v1) §3.1–3.7/A1–3、G.3、B.3–B.4。2+1+3=6，noise-level posterior/估计误差分账与 support-projection metric 的具体差额深入；仅采用有界 support/metric-cover/加权学习误差等条件性接口，不采用 Corollary 完整参数处方、通用收敛、零成本或唯一 DDPM 失败原因。B.4 初始化 KL 为 R²/(2σ0²) 与正文小 σ0 未闭合，理论/训练 prior 与更新不合并；13M UNet、4H100、有限 PSNR/视觉示例不授生产质量，precision/重复训练/FID/端到端成本未披露。未核实现或复现；root 必要源/owner 写前通过，实际两段、完整邻接与本末注非作者 POST 通过，窄锁释放；日级 Gate 未授。

- `SF-2026-ARXIV-2602-10099` — Daily `2026-02-12`；[RJF exact-v1](https://arxiv.org/html/2602.10099v1) §2–5/Alg1–2、Tables3–5、B。2+1+3=6，具体球面 path/tangent/update 与 decoder radius 差额深入，sinc/时钟歧义不照录，有限路径反侧不授唯一几何根因/语义保真或无成本。独立reviewer必要source、root实际owner写前通过；实际正文、邻接与末注经root非作者POST通过，窄锁释放；未核实现或复现，非日级Gate。

- `SF-2026-ARXIV-2602-09891` — Daily `2026-02-12`；[Stemphonic exact-v1](https://arxiv.org/html/2602.09891v1) §3–5/Tables1–3。2+2+2=6，具体独立 compute graphs/group-noise 统计 coupling 差额深入；推理同 seed 非联合训练或语义证书，one/two/K-pass 质量费用及 silence 活动通道反退近正文。root必要source/实际owner写前通过；实际正文、邻接与末注经root非作者POST通过，窄锁释放；未核实现或复现，非日级Gate。

- `SF-2026-ARXIV-2602-09651` — Daily `2026-02-12`；[Partitioned Entropy exact-v1](https://arxiv.org/html/2602.09651v1) §4–6/B。2+1+2=5，具体owner差额深入：distinction-specific时窗诊断，非穷尽二分/prior.5/complement近似与guide后crossentropy；非commit/免费；未核实现或复现。必要source独立通过、root实际owner写前通过；实际正文、邻接与末注经root非作者POST通过，窄锁释放；非日级Gate。

- `SF-2026-ARXIV-2601-22158` — Daily `2026-01-31`；[pMF exact-v1](https://arxiv.org/html/2601.22158v1) §4/Eq8–12/Algorithm1、§5/Table2–4及必要 Appendix A。2+2+2=6，输出参数化与 velocity loss 接口差额定点深入；只采用高 patch 维度/有限容量下的条件性分工，不授一般 r 的 manifold 保证、最终 FID 单因果或生产速度。时间方向、JVP/采样/感知 encoder 成本与 latent/多步回退近正文。未核实现或复现；root 必要原源与实际 owner 写前通过，实际正文157–185/邻接及末注1898经 root 非作者 POST 通过，窄锁释放，不授日级 Gate。

- `SF-2026-ARXIV-2601-22031` — Daily `2026-01-31`；[CARD exact-v1](https://arxiv.org/html/2601.22031v1) §3.1–3.4、§4/Table1、§5/Table4–5、Appendix B/D。2+2+2=6，单流 corrupted-prefix 全位置监督与 causal visibility/block commit 分离的具体接口差额深入；不采用 MI/随机猜测普遍性或同 AR 吞吐保证。generation batch 128 与训练硬件 Not Disclosed 分开，附录 attention/schedule 配置冲突、早 prefix 信息不足及硬限强填反侧留在采用边界。未核代码/复现；root 必要原源与实际 owner PRE 通过，实际正文722/724、完整邻接与末注经 root 非作者 POST 通过，窄锁释放，不授日级 Gate。

- `SF-2026-ARXIV-2602-10314` — Daily `2026-02-13`；[exact-v1](https://arxiv.org/html/2602.10314v1) §3–4与必要Appendix A.2 L408–422；只采forward-law因子与clean无关的Bayes条件，不采用L434权重展示瑕疵、任意multi-position exact或通用复杂度。refresh/threshold/K成本与退步近正文。root必要源与实际owner PRE通过，具体差额受影响深入；实际正文/完整邻接与末注已经root非作者实际POST通过，窄锁释放，不授日级。未核代码或复现。

- `SF-2026-ARXIV-2602-15014` — Daily `2026-02-18`；[Discrete Diffusion Language Models exact-v1](https://arxiv.org/html/2602.15014v1) §3–5。2+2+2=6，具体 owner 评价接口差额受影响深入；仅采不同 variational bound 与实际 sampler 质量/预算分账、特定 scorer/最大适配 batch 的拟合 frontier，保留单 token LTR math 非并行加速、数值熵/评价/硬件与调参成本。root 必要原源与实际 owner/相邻 PRE 通过；实际正文、完整邻接及末注已经 root 非作者 POST 通过，窄锁释放，日级未验。未运行实现或复现实验。

- `SF-2026-ARXIV-2602-14209` — Daily `2026-02-18`；[MAGE exact-v1](https://arxiv.org/html/2602.14209v1) §3–5/Algorithm1 与必要 Appendix B。2+2+2=6，具体 block 内 sparse-index 有效期/first-probe 摊销差额受影响深入；只采本 block 首 all-MASK exact probe 与后续索引复用，不采用后版平均 query 理论、恒定路由、严格全局 K 或通用质量/SLO 保证。低 step 摊销反侧、32K needle 退步与三前向适配成本近正文；未核实现或复现。root 必要源/actual owner 与相邻 PRE 通过，实际两段、完整邻接及末注非作者 POST 通过，窄锁释放，非日级验收。

- `SF-2026-ARXIV-2602-15287` — Daily `2026-02-19`；[exact-v1](https://arxiv.org/html/2602.15287v1) §III–IV/Eq5–22/TablesI–II。2+2+2=6，具体采样gap受影响深入；只采删negative-alignment joint-diversity梯度分量的一阶非零proxy条件，不授finite trajectory/全质量/物理保证。主embedding变动、局部samebranch消融、Vendi-f与IID-MSE反側和offline proxy费用近正文；root必要源/actualowner PRE及实际正文/完整邻接与末注非作者POST通过，窄锁释放，未核代码/复现。

- `SF-2026-ARXIV-2602-12468` — Daily `2026-02-17`；[exact-v1](https://arxiv.org/html/2602.12468v1) §3/Alg1、§4/Tables1–2/成本与A硬件。2+1+2=5，continuous decoder-independent regular-acceptance mass梯度的具体owner差额深入；全tokenization、high-noise proxy、最终argmax非hard有效、JSON不同padding/负面、passing population与automaton反传成本近正文。root必要源/actualowner PRE通过并授窄锁；作者实际单段及完整邻接已读，root非作者实际正文/完整邻接/末注POST通过；未运行实现或复现实验，非日级Gate。

- `SF-2026-ARXIV-2602-14041` — Daily `2026-02-18`；[BitDance exact-v1 PDF](https://arxiv.org/pdf/2602.14041v1) §3.2–3.3/Eq3/5–7、§4.2及必要设置/消融。2+2+2=6，patch-joint factorization/head 的具体差额深入；保留 head 迭代/训练、patch-size 质量交换、bit 组合非实际容量、非 exact 与跨 family 配置边界，不授无损或普遍端到端加速。root 必要源/actual owner PRE及实际正文/完整邻接与末注POST通过；未核代码或复现，非日级。

- `SF-2026-ARXIV-2602-14157` — Daily `2026-02-18`；[DInG exact-v1](https://arxiv.org/html/2602.14157v1) §2/3、必要§4编辑对照与codec/mask限制。2+1+2=5，理论近似与pixel/latent观测合同差额深入；既有 VJP-free 不作本论文独创，denoiser scaled-identity/noise-Jacobian忽略与linear conjugacy不授nonlinear pixel等价。thin mask/dilation、FLUX对照反側、solver/codec/cost与原路径回退近正文。root 必要源/actual owner PRE及实际正文/完整邻接与末注POST通过；未核实现或复现，非日级。

- `SF-2026-ARXIV-2602-12683` — Daily `2026-02-17`；[exact-v1](https://arxiv.org/html/2602.12683v1) 必要机制、关键对照与直接限制；2+1+2=5，实际 owner 差额定点深入。仅采用正文条件分支，不授普遍性能/正确性或终端证明；root 必要原源/owner PRE通过并授窄锁，作者正文/完整邻接已顺读，root非作者实际正文/完整邻接/末注POST通过，窄锁释放；未核实现或复现，非日级Gate。

- `SF-2026-ARXIV-2602-12769` — Daily `2026-02-17`；[exact-v1](https://arxiv.org/html/2602.12769v1) 必要方法、关键对照与直接限制；2+1+2=5，实际owner差额定点深入。只采用正文条件机制，额外预算/局部反側与回退相邻，不授真实像素恢复、全部质量或一求值全流程保证；root必要原源/actualowner PRE通过并授窄锁，作者正文/完整邻接已顺读，root非作者实际正文/完整邻接/末注POST通过，窄锁释放；未核artifact或复现，非日级Gate。

- `SF-2026-ARXIV-2602-12932` — Daily `2026-02-17`；[exact-v1](https://arxiv.org/html/2602.12932v1) 必要方法、关键评价与直接限制；2+2+2=6，实际 owner 差额定点深入。只采用正文条件机制与明确有限适用范围，不授有限粒子/离散求解真实分布精确性；root 必要原源/actual owner PRE 通过并授窄锁，作者正文/完整邻接已顺读，root 非作者实际正文/完整邻接/末注 POST 通过，窄锁释放；未核 artifact 或复现，非日级 Gate。

- `SF-2026-ARXIV-2602-16813` — Daily `2026-02-21`；[FMLM exact-v1](https://arxiv.org/html/2602.16813v1) §2–4、§5/Tables1–3与§6。2+2+2=6，one-hot decode-error时间坐标与冻结FLM/Euler校正→单map压缩接口的具体差额定点深入；不授严格半群、一步无损/通用能力或生产SLO，entropy/GenPPL反侧及双模型/词表训练成本近正文。root必要原源/actual owner PRE、实际正文与完整邻接的非作者POST通过；未核实现或复现，非日级Gate。

- `SF-2026-ARXIV-2602-16872` — Daily `2026-02-21`；[exact-v1](https://arxiv.org/html/2602.16872v1) §4–7/Tables1–3、Training Configuration/B1与直接Limitations。2+2+2=6，prefix-hidden/cache与rigid OCR反侧具体差额深入；8A10040GB/BF16/200ksteps/B8/p=.98，有限EN OCR，不授三倍等质量/全cache保证。root必要原源/actual owner PRE通过并授窄锁；作者已实际顺读正文/完整邻接，root正文/完整邻接/末注POST通过；未运行实现/复现，非日级验收。

- `SF-2026-ARXIV-2602-16498` — Daily `2026-02-20`；[GoldDiff exact-v1](https://arxiv.org/html/2602.16498v1) §3.1–3.5/Theorem1、必要A.1/4.1/4.3。2+1+2=5，coarse recall与aggregation支集反向噪声预算差额深入；真实top-k界不保proxy recall/全轨迹gap，全N低维扫描、oracle非真score/记忆与费用近正文。不采71x端到端或N解耦，冲突超参配方不采用。root必要源/actual owner PRE通过并授一段窄锁；作者正文/完整邻接已顺读，root非作者实际正文/完整邻接/自身末注POST通过，窄锁释放；未核实现/复现，非日级验收。

- `SF-2026-ARXIV-2602-16570` — Daily `2026-02-20`；[exact-v1](https://arxiv.org/html/2602.16570v1) §2/Alg1/Th4.1 caveat/Th5.2/Alg2–3/6。2+1+2=5，linear query-shift与quadratic sign/rank/entry-scale差额深入；HS mixture含Z权重不引用未统一系数，exactscore/bounded support、normalizer/grid成本与NSD指数entries边界近正文。root必要原源/actual owner PRE通过并授一段窄锁；作者正文/完整邻接已顺读，root非作者实际正文/完整邻接/自身末注POST通过，锁释放；未核实现/复现，非日级验收。

- `SF-2026-ARXIV-2602-16968` — Daily `2026-02-21`；[exact-v1](https://arxiv.org/html/2602.16968v1) §3/Eq1–5与§4–5/Tables2–4；2+2+2=6，输入token网格与guidance尺度分权差额深入。新patch接口/LoRA蒸馏成本、全局每step选择、VBench/CLIP及阈值非单调反侧近正文；不授全pipeline无训练/组合倍率独享或无损SLO。root必要原源/actual owner PRE通过；作者正文/完整邻接及末注已顺读，root非作者实际正文/完整邻接及末注POST通过，窄锁释放；未核实现/复现，非日级验收。

- `SF-2026-ARXIV-2602-17047` — Daily `2026-02-21`；[exact-v1](https://arxiv.org/html/2602.17047v1) §2/Eq1–4/Algorithm1、§2.1.3–3.4与Table1。2+2+2=6，cluster-end targets 的局部→全局恢复与 single-stream 拼接对齐差额深入；权重平均非函数复合、联合变化/指标退步与1872 GPU-hours训练费用近正文。root必要source/actual owner PRE通过并授一段/自身末注窄锁；作者正文/完整邻接已顺读，root非作者实际正文/完整邻接及自身末注POST通过，窄锁释放。未核实现/复现，不授全指标/完整端到端加速，非日级验收。

- `SF-2026-ARXIV-2602-17846` — Daily `2026-02-24`；[exact-v1](https://arxiv.org/html/2602.17846v1) §3–5/denoiser-swap与gap训练控制。3+1+2=6，step vs trajectory memory设计修正深入；分尺度诊断、有限图像/几何条件、quality–memorization与训练/采样成本近正文，不统一危险噪声带或认证privacy。root必要source/actual owner PRE通过；作者正文/完整邻接及末注顺读、root非作者实际正文/完整邻接/自身末注POST通过，锁释放；未核实现/复现，非日级验收。

- `SF-2026-ARXIV-2602-18093` — Daily `2026-02-24`；[exact-v1](https://arxiv.org/html/2602.18093v1) §3.2/4、Table2、Appendix C/H。2+1+2=5，AB history forecast/J0真实刷新具体差额深入；J>0无逐步δ、startup未披露、质量/阈值/刷新成本近正文，不授完整算法或统一加速。root必要source/actual owner PRE通过；作者正文/完整邻接及末注顺读、root非作者实际正文/完整邻接/自身末注POST通过，锁释放；未核实现/复现，非日级验收。

- `SF-2026-ARXIV-2602-18428` — Daily `2026-02-24`；[exact-v1](https://arxiv.org/html/2602.18428v1) §6/Eq19–22、§7。2+1+2=5，blind model/scheduled sampler与ν增益误差分责具体差额深入；D128 noise-prediction成功反侧/Table3借用不混因果、训练/时间系数/积分成本近正文，不授无schedule或全质量保证。root必要source/actual owner PRE通过；作者正文/完整邻接及末注顺读、root非作者实际正文/完整邻接/自身末注POST通过，锁释放；未核实现/复现，非日级验收。

- `SF-2026-ARXIV-2602-18176` — Daily `2026-02-24`；[exact-v1](https://arxiv.org/html/2602.18176v1) §3/Eq5、Fig2 caption与AppendixF。2+1+2=5，candidate action后forward剩余marginal entropy/cost差额深入；IG−cost与caption反向不一致、model proxy/K×N/activation/cache/bypass人口近正文，不授全局最优或免费batch。root必要source/actual owner PRE通过并授窄锁；作者正文/完整邻接及末注实际顺读、限定diff-check通过，锁释放，root非作者实际正文/完整邻接/自身末注POST通过。未核实现/复现，非日级验收。

- `SF-2026-ARXIV-2602-17097` — Daily `2026-02-21`；[exact-v1](https://arxiv.org/html/2602.17097v1) §4.1–4.2/Eq10–12、§5.4/Table4、B2/C2/D。2+2+2=6，turn-wise noise 与 clean-history/target 联合支持差额深入；SCT 非 noise 单因素因果，private/unreleased、sensor/指标反侧和完整训练/采样费用近正文。root 必要原源/actual owner PRE 通过并授一段/自身末注窄锁；作者实际正文及完整邻接已读，root 非作者实际正文/完整邻接及末注 POST 通过，窄锁释放。未核实现/复现，非日级验收。

- `SF-2026-ARXIV-2602-18422` — Daily `2026-02-24`；[exact-v1](https://arxiv.org/html/2602.18422v1) §3.1–3.2混合控制与训练、§4反侧、§5 5B部署/§6限制。2+1+2=5，2D/3D与hand/camera歧义分工差额深入；14B评价与5B部署分开、proxy/联合反侧/VR时延与完整成本近文，不授真实物理/生产实时保证。root必要原源/actual owner PRE通过并授一段/自身末注窄锁；作者实际正文/完整邻接及自身末注已顺读、限定diff-check通过，窄锁释放，root非作者实际正文/完整邻接及自身末注POST通过。未核实现/复现，非日级验收。

- `SF-2026-ARXIV-2602-16664` — Daily `2026-02-20`；[exact-v1](https://arxiv.org/html/2602.16664v1) §4.1–4.3/4.5、自然图像§5/§6、AppendixE运行配置与F自然图像限制。2+1+2=5，encoder-centered endpoint/domain bridge差额深入；共享语义仅假设、b0非保证、额外训练与大形变/representation-gap反侧近正文，不纳临床效果。root 必要原源/actual owner PRE通过；作者正文/完整邻接已读，root 非作者实际正文/完整邻接/自身末注 POST通过，窄锁释放；未运行实现/复现。

- `SF-2026-ARXIV-2602-15971` — Daily `2026-02-20`；[exact-v1](https://arxiv.org/html/2602.15971v1) §3.1/Algorithm4、匹配§4设置与反侧、权重搜索。2+2+2=6，parallel teacher-state 辅助监督与终点交付具体差额深入；有限状态非连续积分证书，ImageNet≥3步反退、teacher/辅助头/Optuna成本及旧solver回退近正文。root必要原源/actual owner PRE通过并授窄锁；作者实际正文/完整邻接已读，root非作者实际正文/完整邻接/自身末注POST通过，窄锁释放。未核实现/复现，非日级验收。

- `SF-2026-ARXIV-2602-17211` — Daily `2026-02-21`；[exact-v1](https://arxiv.org/html/2602.17211v1) §3.1–3.2/Eq12–21、§4.1 Conjecture4.1、§5.1.1–5.1.2。2+1+3=6，finite moment path vs full distribution 差额深入；解存在/Gram奇异、p*非pdata、一般速率为猜想及同分布换φ约100倍积分反侧近正文，不授任意有限σ精确采样。root必要源/actual owner PRE通过并授窄锁，作者实际正文/完整邻接已读，root 非作者实际正文/完整邻接及自身末注 POST通过，窄锁释放；未核实现/复现，非日级Gate。

- `SF-2026-ARXIV-2602-18647` — Daily `2026-02-25`；[exact-v1](https://arxiv.org/html/2602.18647v1) §2–6/8、Algorithm1及Appendix D。2+2+2=6，online loss-proxy 分箱及 fixed w 不等固定 effective expectation 差额定点深入；proxy/覆盖/刷新、权重对照与训练样本≠wall-clock 近正文，不授 Bayes entropy 或最优配置。root 必要原源/actual owner PRE 及非作者实际正文/完整邻接/自身末注 POST 通过，锁释放；未核实现或复现，非日级验收。

- `SF-2026-ARXIV-2602-18695` — Daily `2026-02-25`；[exact-v1](https://arxiv.org/html/2602.18695v1) §3/5/6、D.5.2及E。2+2+2=6，data-dependent target hazard/endpoint与联合学习退化差额定点深入；双样本/aux成本、固定unmask和shared反侧、有限sampler不继承精确保证近正文。root必要原源/actual owner PRE通过并授两段窄锁；作者实际正文、完整邻接与自身末注顺读，root 非作者 actual POST 通过，窄锁释放，未核实现或复现，非日级验收。

- `SF-2026-ARXIV-2602-20293` — Daily `2026-02-26`；[exact-v1](https://arxiv.org/html/2602.20293v1) §2/3/4/5.1–2。2+1+2=5具体gap深入，single-site canonicalratio/局部condition学习、sup误差非平均loss/softnoise反侧近正文；不采用原AR unrolling式索引不一致、science域结果、LLM/生产优势。root必要源/actual owner PRE通过并授两段+自身末注窄锁；作者actual正文/完整邻接及本末注顺读，root非作者actual正文447–470/自身末注2099 POST通过，锁释放。未核artifact/复现，非日级验收。

- `SF-2026-ARXIV-2602-20360` — Daily `2026-02-26`；[exact-v1](https://arxiv.org/html/2602.20360v1) §3/Eq12–13、§4.1/Table1/ablation与强CFG反侧。2+1+2=5具体历史velocity reference gap深入；旧m用于当前外推，m_next只入下一步，额外state/算术/搜索与强CFG反退近正文。不采用精确unconditional/分布保持或零总费/性能保证。root actual必要源/owner PRE通过，授两段+自身末注窄锁；作者actual正文/完整218–228/末注已顺读，root非作者actual正文218–228/自身末注2105 POST通过，锁释放。未核artifact/复现，非日级验收。

- `SF-2026-ARXIV-2602-20480` — Daily `2026-02-26`；[exact-v1](https://arxiv.org/html/2602.20480v1) §3/Assumption3.1/Theorem3.1、finitecritic与moment必要反侧。2+1+2=5，critic loss与conditionaldistribution校准差额定点深入；整个T/inverse统一双Lipschitz、有限矩/criticgap及正概率观测集合非逐点保证近正文，saddle/采样/容量费用与独立条件验证保留。root实际必要源/owner PRE通过并授两段+自身末注窄锁；作者实际正文/完整邻接及末注顺读，root非作者actual正文194/196、完整184～203与自身末注2125 POST通过，窄锁释放。未核artifact/复现，非日级Gate。

- `SF-2026-ARXIV-2602-21461` — Daily `2026-02-27`；[VecGlypher exact-v1](https://arxiv.org/html/2602.21461v1)。2+1+2=5，同geometry输出serialization的容量/双metric条件差额深入；OCR比值非accuracy、两阶段预算/Latin单path局部及原schema回退近文，不授scale门槛/通用topology。root必要源/actual owner PRE通过并授单段窄锁；作者实际正文/完整邻接/自身末注已顺读，root非作者已实际独读正文/完整邻接/自身末注，POST通过，窄锁释放，未核实现或复现，非日级Gate。

- `SF-2026-ARXIV-2602-22122` — Daily `2026-02-27`；[exact-v1](https://arxiv.org/html/2602.22122v1) §2–4/Fig4–6，2+1+2=5；具体owner差额深入：pointdensity与typical/感知路径；有限score/temperature与全计算边界，空schedule不采用，不授物理或采样分布保证近正文。root必要原源/actual owner PRE通过并授窄lease；作者及root非作者已实际顺读正文/完整邻接/自身末注，POST通过，窄lease释放。未核实现/复现，非日级Gate。

- `SF-2026-ARXIV-2602-20394` — Daily `2026-02-26`；[exact-v1](https://arxiv.org/html/2602.20394v1) §2.2–2.4/3.1–3.3，2+1+2=5，AR parent-set/顺序与conditional学习难度真实差额深入。未来边缘化诱导依赖、d/K启发、有限moment-error与统计/截断误差/图估计费用保留，不授最优排序/LLM/无损采样。必要原证/actual owner PRE经root授窄锁；作者实际正文/邻接/自身末注已读，root非写入者实际正文/完整邻接与自身末注POST通过。未运行artifact/复现，非日级验收。

- `SF-2026-ARXIV-2602-21185` — Daily `2026-02-26`；[exact-v1](https://arxiv.org/html/2602.21185v1) §3 Eq11/12、A1.2与§5反侧，2+2+3=7，真实clean条件marginal与joint reverse path差额深入。learned代入不继承恒等式，κ/prior/schedule/model共同身份、MDLM反侧/训练curriculum和serving费用分责近文。非原packet作者原证/actual owner PRE、root授窄锁；作者实际正文/邻接/自身末注已读，root非写入者实际正文/完整邻接与自身末注POST通过。未运行artifact/复现，非日级验收。

- `SF-2026-ARXIV-2602-22948` — Daily `2026-02-28`；[exact-v1](https://arxiv.org/html/2602.22948v1)，2+1+2=5；当前作者非原packet作者必要原源/actual owner具体差额深入，root once准入通过并授窄锁。作者实际正文/完整邻接/自身末注已順读；final_audit非原作者必要原源/actual owner独核通过，root非写入者实际正文/完整邻接/自身末注POST通过，窄锁释放；未核实现/复现，非日级。

- `SF-2026-ARXIV-2601-08379` — Daily `2026-01-15`补充；[exact-v1](https://arxiv.org/html/2601.08379v1) §4 Eq5–8/Alg1、§5 Eq10–11、§6 Tables1–4/§7。2+2+2=6，finite-reference population guidance 的具体 gap 深入；只采用 attraction/repulsion 与 prompt×latent kernel接口，cross-term集中界不授最终sampler/decoder law，稀疏reference/kernel及4090/50step额外费用反侧保留。root必要原源/actual owner PRE通过授窄锁，作者实际新段/前后邻接及自身末注顺读；root实际240–259完整邻接与自身末注POST通过，窄锁释放。未运行artifact/复现，非日级。

- `SF-2026-ARXIV-2601-08321` — Daily `2026-01-15`补充；[exact-v1](https://arxiv.org/html/2601.08321v1) §3.2–3.5/Eq1–3/§4 Tables1–4。2+1+2=5，ROI latent-velocity与decoded RGB edge两个consumer差额深入；mask/edge非语义真值、VAE/条件/标注费用与OCR/LPIPS分账近文，不采freeze冲突recipe。review_jan15_delta实际原源/owner PRE通过，root授单段/自身末注锁；作者actual正文/完整邻接顺读，review_jan15_delta非作者actual正文/完整邻接及本末注POST通过，锁释放。未核实现/复现，非DAY。

- `SF-2026-ARXIV-2601-08303` — Daily `2026-01-15`补充；[exact-v1](https://arxiv.org/html/2601.08303v1) §3.1–3.3/Eq4–10/§4 Tables1–2/Fig8、AppA/C/H。2+2+2=6，同x_t few-step teacher velocity/feature与realteacher/critic分布责任差额深入；无matched DMD-only不授稳定性单因果，LoRA共享非免费、少步质量/完整encoder-decoder费用近文。review_jan15_delta实际原源/owner PRE通过，root授单段/自身末注锁；作者actual正文/完整邻接顺读，review_jan15_delta非作者actual正文/完整邻接及本末注POST通过，锁释放。未核实现/复现，非DAY。

- `SF-2026-ARXIV-2601-08450` — Daily `2026-01-15` 增量；[exact-v1](https://arxiv.org/html/2601.08450v1)；2+1+2=5，review_jan15_delta必要原证/actual owner具体PRE通过，root授该处单段及自身末注窄锁；仅采用接口分工，局部反侧/完整费用与旧路径回退近文，不采不完整solver或普遍性能/安全保证。作者正文完整邻接已顺读，review_jan15_delta已实际独读新段/完整邻接及自身末注，actual POST通过，root窄锁释放。未运行实现/复现，非日级验收。

- `SF-2026-ARXIV-2601-07219` — Daily `2026-01-14`增量；[exact-v1](https://arxiv.org/html/2601.07219v1) §4.2–4.3、5.2/5.4 Tables2–6必要机制/反側；2+1+2=5，source交集与target新关系+交集的具体gap深入。语义关系不授pixel保真、GTTP另一模式不混同graphdiff，accuracy/fidelity与parser/inversion/77token费用近正文；不授普遍速度。root必要源/actual owner PRE通过并授一段窄锁；作者实际正文/完整邻接及本注已顺读，root非writer实际新正文/完整邻接及本注actualPOST通过，窄锁释放。未核artifact/复现，非DAY。
- `SF-2026-ARXIV-2603-09883` — Daily `2026-03-12`补查；[DISPLAY exact-v1](https://arxiv.org/html/2603.09883v1) §3–4/Eq1–3/Tables1–2、Appendix0.A/0.D/0.F。2+1+2=5，对象参考与稀疏条件接口差额定点深入；logit偏置非物理约束、不同基线输入/MTT数据混杂、质量反侧与完整费用近文。root作者必要Source/date/PRE经supplement_20260312独立复核通过，root实际两段写入并保留原schedule及后训练交接；非writer实际顺读1532–1564完整邻接、新1546/1548及本人2315，回对有效原证和逐字PRE，actualPOST通过，不计日级完成。未核视频像素、全部附件、代码或复现。

<!-- supplement-20260122-review-note -->

- `SF-2026-ARXIV-2610-09876` — Daily `2026-10-09`；[PaTh exact-v1](https://arxiv.org/html/2610.09876v1) §3–5与C/H/K/L/N必要范围，2+1+2=5；未解码探索状态与frozen painter接口的具体gap深入，空间anchor失败、晚段/质量反退及全费用近文。supplement_20260311非作者必要Source/actual owner/逐字PRE通过，root授本段与本注窄锁；作者写后顺读，root非writer实际846–875完整邻接、新858和本人2321注POST通过，锁释放。未核像素、代码或复现，不授DAY。

- `SF-2026-ARXIV-2601-13228` — Daily `2026-01-22`增量；[A3 exact-v1](https://arxiv.org/html/2601.13228v1) §3.1–3.3/4.3。2+2+3=7；只采用group/query-content监督、curriculum与未完成位置动态commit分支，不重复target-free双流，不称精确joint或保原AR分布；重评估/训练成本、初始化和预算比较条件近正文。root必要原源与实际owner PRE通过并授窄锁；作者实际正文/完整邻接顺读，root非作者actual POST通过，窄锁释放。未核实现或复现，不授日级验收。
- `SF-2026-META-UNIT` — Daily `2026-02-12`补充；[2026-02-11官方稿](https://ai.meta.com/research/publications/unit-unified-multimodal-chain-of-thought-test-time-scaling/) §3.1–3.3、§5.1–5.4/Tab5。2+1+2=5，统一模型内化text-image correction/强制round预算差额定点深入；图像计数非wall-clock、内部verification非真值、三行为训练配方消融与退化/冲突/base限制近正文。root实际必要原件Source/owner PRE通过并授两段及本末注窄锁；作者实际正文/完整邻接已读，root非作者实际两段、820–850完整邻接及本末注POST通过，窄锁释放。未核实现或复现，不授DAY。
- `SF-2026-ARXIV-2602-10095` — Daily `2026-02-12`补充；[SCD exact-v1](https://arxiv.org/html/2602.10095v1) §4.1–4.2/5.1–5.3、§6.1–6.2/Table1–3、§7。2+2+2=6，once-per-frame E/stepwise D职责的具体gap深入；lowres clean-history与高rescurrent-noisy适配分开，固定context近似、残余crossframe/late-step不稳定与训练/首帧费用近正文。不是matched质量/参数或普遍速度、SLO、world-state保证。root实际必要原源Source/owner PRE通过并授两段及本注窄锁；作者写后顺读，root非作者实际161/163、完整151–175邻接及2275末注POST通过，窄锁释放，不授DAY。未核实现或复现实验。
- `SF-2026-ARXIV-2602-12262` — Daily `2026-02-14`补充；[T3D exact-v1](https://arxiv.org/html/2602.12262v1) §2/3/4/5/7、D/C.2。2+2+2=6，teacher状态/终点配对与原order+gold分支具体差额深入；shared intermediate marginal仅假设、teacher/reference费用及full-step反侧近正文。非作者必要Source和root actualowner逐字PRE通过，root授单段及自身末注窄锁；作者实际正文/邻接与本注顺读，root非writer实际新436/1534、完整连续邻接及2273–2281自身末注POST通过，窄锁释放。未核实现/复现，不授DAY。 本轮补查事件的首次公开日期未证，必要Source/PRE/实际POST研究仍有效，但不计本日已确认新增成果；归属只按[本日日报§5](../../papers/2026/02/14/README.md#5-缺口与下一步)的57日期请求定点重开，不撤正文或补造公开日。
- `SF-2026-ARXIV-2602-12155` — Daily `2026-02-14`补充；[FAIL exact-v1](https://arxiv.org/html/2602.12155v1) §2/3/4/6/7、Eq1–4/Tables1–8。2+2+2=6，可微与scalar反馈的flow训练梯度路径差额深入；single-step近似/loss-ratio proxy、collapse及全训练费用反侧近正文。非作者必要Source和root actualowner逐字PRE通过，root授单段及自身末注窄锁；作者实际正文/邻接与本注顺读，root非writer实际新436/1534、完整连续邻接及2273–2281自身末注POST通过，窄锁释放。未核实现/复现，不授DAY。 本轮补查事件的首次公开日期未证，必要Source/PRE/实际POST研究仍有效，但不计本日已确认新增成果；归属只按[本日日报§5](../../papers/2026/02/14/README.md#5-缺口与下一步)的57日期请求定点重开，不撤正文或补造公开日。

- `SF-2026-ARXIV-2602-11564` — Daily `2026-02-14`补查；[exact-v1](https://arxiv.org/html/2602.11564v1)，2+2+2=6，必要Source经review_20260214非作者限定通过，actual MULTIMODAL-GENERATIVE-PARADIGMS owner/完整邻接与逐字拟文PRE通过，root授本一段及自身末注窄锁；作者实际新段/完整局部及本注顺读，非writer实际正文、完整局部邻接及本人末注actualPOST通过，root释放窄锁。具体费用、直接反侧及失配回退近正文，不授全recipe、普遍正确/因果/性能保证、实现复现或DAY。 本轮补查事件的首次公开日期未证，必要Source/PRE/实际POST研究仍有效，但不计本日已确认新增成果；归属只按[本日日报§5](../../papers/2026/02/14/README.md#5-缺口与下一步)的57日期请求定点重开，不撤正文或补造公开日。

- `SF-2026-ARXIV-2603-09215` — Daily `2026-03-12`补查；[SPAR-K exact-v1](https://arxiv.org/html/2603.09215v1) §4.1–4.2、§5；2+1+2=5，text/speech条件执行深度与缺失deepKV的具体差额深入。oracle history不等真实浅层回馈，额外head训练、cache补算及选择费用近正文；exit depth不授墙钟，预测MOS/Whisper WER/GPT judge与语义分账，GLM confidence较高平均分及任务反侧保留。v2窗外不倒填；root实际必要Source、原日期字段及逐字PRE通过并写入；非writer supplement_20260312实际顺读704–732完整邻接、新正文及自身末注并回对v1§4.2/5，POST通过，锁释放。未核实现、复现或完整SLO，不授日级验收。

- `SF-2026-ARXIV-2603-07700` — Daily `2026-03-11`补查；[TDM-R1 exact-v1](https://arxiv.org/html/2603.07700v1) 必要原证99–194/513–549/1138–1155，2+2+2=6；确定性余轨迹与逐轮 surrogate 的梯度分责具体差额深入。review_20260311必要Source有效复用，review_mar11_continue实际Ch24 1544–1576 owner/PRE及126–194绝对标准化权重/sg(φ)措辞定点复核通过，root授本段与本人末注窄锁。未给std=0 guard，不称权重实现硬界；条件方差不等reward正确性/无偏或收敛。作者实际写入；review_mar11_continue非writer实际正文/完整邻接及本注POST通过，root释放窄锁，不授DAY、实现核验或复现。

- `SF-2026-ARXIV-2603-08850` — Daily `2026-03-12`补查；[HECTOR exact-v1](https://arxiv.org/html/2603.08850v1) §3–5/Eq4–7/Tables1–2。2+1+2=5，静/动态reference time/canvas与用户priority gap深入；不采singleanchor尺度、真实遮挡/physics、strictbackground或低全费，quant仅image/混合qual与全模型训练代价近文。Source/date/actual owner/逐字PRE经mar12_independent_continue独核通过，root授本单段/本人注窄锁；未核像素/实现/复现，root非writer实际正文、完整邻接及本人末注actualPOST通过，锁释放，不授DAY。

- `SF-2026-ARXIV-2603-09084` — Daily `2026-03-12`补查；[OmniEdit exact-v1](https://arxiv.org/html/2603.09084v1) §3–6/Eq3–12/Algorithms1–2/Tables1–3。2+1+2=5，source/target耦合轨迹与扰动估计具体gap深入；不采Eq8反号或Alg2未闭合recipe、target无偏终态或全流程确定性，同步/GSR反侧、qual-only AV与完整费用近文。Source/date/actual owner/逐字PRE经mar12_independent_continue独核通过，root授本单段与本人注窄锁；作者实际写入，未核外部视频、实现或复现，root非writer实际193–207完整正文邻接与本人2361注actualPOST通过，锁释放，不授DAY。

- `SF-2026-ARXIV-2603-10445` — Daily `2026-03-13` 补查；[Prompt-free instance unlearning exact-v1](https://arxiv.org/html/2603.10445v1) IV-A/C、V-A及VI-A/D。2+1+2=5，原图加噪输入与编辑 endpoint 联动的具体目标缺口局部深入；重建 SSCD 非生成概率或彻底遗忘证明、retain 人口与费用/质量反侧近正文。IV-B Eq31/46 的 ridge 更新符号反例另留日报证据，不依赖该理论整合机制。准备者 mar13_admission_review 必要 Source/实际 owner 与两段 PRE 经 root 非作者实核通过，root 窄写两段和本注；mar13_admission_review 实际非 writer 顺读正文、完整邻接和本注 POST 通过，窄锁释放，不授 DAY。未核代码或复现。

- `SF-2026-ARXIV-2603-12245` — Daily `2026-03-14` 补查；[ELIT exact-v1](https://arxiv.org/html/2603.12245v1) §3.3–3.4/4.1–4.5/5/C。2+1+2=5，固定空间输出与训练过的可变内部 latent 人口具体差额深入；双 guidance 的算子变化、batch/视频人口限制、Qwen 条件质量反侧及全费用近正文，不采普遍分辨率解耦或在线加速保证。mar14_supplement 必要 Source/owner/PRE 经 root 非准备者实际复核通过，root 窄写两段与本注；mar14_supplement 实际非 writer 顺读两段、完整局部邻接及本注 POST 通过，窄锁释放，不授 DAY。未核代码/像素或复现。

- `SF-2026-ARXIV-2603-10744` — Daily `2026-03-13` 补查；[JiT exact-v1](https://arxiv.org/html/2603.10744v1) §3.1–3.4/Eq5–9/Alg1、§4/Table1、A.2/A.4及直接限制。2+1+2=5，完整状态/稀疏速度与新 anchor target 的具体差额深入；少上下文不等 full attention、噪声幅度非统计保证、FLOP/墙钟与质量反侧及回退近文。mar13_supplement 准备必要 Source/owner/PRE，root 非准备者实际原证与局部邻接复核通过后窄写两段及本注；mar13_supplement 实际顺读写后正文、相邻交接与本注并回对原证，非 writer POST 通过；局部写入验收，不授 DAY。未核实现、像素/视频或复现。

- `SF-2026-ARXIV-2603-10780` — Daily `2026-03-13` 补查；[exact-v1](https://arxiv.org/html/2603.10780v1) §3–5 Eq2–11/§6 Tables1–4与直接消融/AppB Algorithm2及C.1/C.3。2+1+2=5，mar13_admission_review 非准备者实际 Source、Ch24 条件布局差额与两段 PRE 通过，root 窄写于 capacity reference 与历史 EMA 之间。只采用 content/context-aggregating 分组、空条件状态替换与首步排名缓存接口；不授真实 manifold、全轨迹语义保真、PageRank 必要性或默认预算通用 SLO。两支与制备/校准费用、质量反侧和回退近文；未核实现或复现。mar13_admission_review 实际非 writer 顺读新增两段、完整邻接与本注，回必要原证 POST 通过；root 回读接纳，窄锁释放，不授 DAY。
