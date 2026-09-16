# 第23章 多模态表示与融合

**Knowledge Tree:** Part III 多模态、生成与世界模型：从跨模态表示到物理行动
**Stable Knowledge Node ID:** `MULTIMODAL-REPRESENTATION`
**Legacy Chapter:** N/A
**Status:** Draft

**Roadmap Intent:** 解释图像、视频、音频与传感器信号如何变成可学习、可融合、可追溯的表示，以及 modality boundary 为什么同时是模型接口和系统状态边界。

## 本章要回答的问题

文本可以被切成 token，图像却是二维像素，视频还多一个时间轴，音频是连续波形，机器人观测又带 calibration 和 sensor clock。它们怎样进入同一个模型？“统一 token space”究竟统一了什么，又没有统一什么？为什么一个效果不错的 projector 方案在某些场景仍优于 native multimodal pretraining？

本章的核心判断是：**多模态系统的第一问题不是把所有输入变成同一 shape，而是建立可版本化的 representation contract：每个表示必须保留它来自哪种 modality、对应什么时间与空间范围、经过哪个 encoder/codec、属于哪个 artifact version，并明确哪些信息已经不可逆地丢失。**共享 backbone 可以统一计算接口，却不会自动统一语义、采样率、误差模型和数据权利。

## 为什么文本 token 的经验不能直接复制

文本 tokenizer 将字节或字符序列映射为离散 ID。即使切分不完美，离散符号通常仍保留可逆的字符串边界。图像 patch 则把局部像素压成向量；视频 token 还要同时压缩空间与时间；音频 segment 的边界可能切断音素；机器人 proprioception 的一个数值只有结合单位、坐标系和时间戳才有意义。

设原始观测为 `x_m`，`m` 表示 modality。encoder 或 codec 给出：

```text
z_m = E_m(x_m; v_m)
```

其中 `v_m` 不只是模型权重版本，还应包含预处理、分辨率、frame rate、normalization、codebook 和 calibration。若下游只保存 `z_m` 而丢失这些条件，数值 tensor 仍可读取，语义却可能已经无法解释。

因此多模态 representation 至少有四层 identity：

```text
content identity     原始样本或可追溯片段
modality identity    image / video / audio / sensor / action
coordinate identity  spatial region、timestamp、frame、reference frame
artifact identity    encoder、codec、codebook、preprocess 与版本
```

## 一个思想实验：同样是 256 个 token

假设系统收到三段长度都为 256 的 token：一段文本、一张图像和一秒音频。对 Transformer 来说，它们都可以成为 `[256, d]`；对系统设计来说，它们完全不同。

- 文本 token 可能覆盖 150～250 个词，并保持严格顺序。
- 图像 token 可能来自 `16 × 16` patch grid，邻接关系是二维的。
- 音频 token 可能覆盖固定时间窗，边界取决于采样率和 codec stride。

把 shape 统一，只解决了“可以送进同一算子”；没有回答空间位置、时间同步、信息损失、重建能力或跨模态指代。**Tensor compatibility 不是 semantic compatibility。**

## 表示演进：从专用特征到统一协议

### 阶段一：手工特征与专用模型

早期系统为每种 modality 构造不同 feature 与模型。它的优点是接口清楚、任务先验强、成本可控；缺点是跨模态信息只能在应用层晚期拼接，知识难以共享。

### 阶段二：modality-specific encoder + projector

视觉或音频 encoder 先提取连续 features，再通过 projector 映射到语言模型 embedding space：

```text
raw signal -> modality encoder -> projected features -> language backbone
```

当目标以理解为主、数据有限、希望复用成熟 encoder 时，这仍是合理的主流分支。encoder 可以独立优化感知质量，backbone 不必承担 raw-signal reconstruction。然而 projector 也成为信息瓶颈：它必须让连续 feature 适配语言 token 的计算接口，却未必能保留低层细节或支持反向生成。

### 阶段三：共享 token space

系统开始把图像、视频或音频压缩为离散 codes，与文本 ID 一起交给共享 autoregressive backbone。它的吸引力是统一 objective 与生成接口：所有 modality 都可以表示成“预测下一个 ID”。

但离散化不会免费发生。codebook size、层数和 stride 决定序列长度与 fidelity；quantization error 会进入训练分布；codec 与 backbone 版本不一致时，同一 ID 可能不再代表同一信号。统一协议减少模型接口数量，却增加 codebook governance。

### 阶段四：native multimodal representation

更进一步的设计不再把非文本输入视为语言模型外挂，而是在 pretraining 中共同学习 modality representation、cross-modal relation 与生成能力。这里的 “native” 应指训练 contract 发生变化，而不是 marketing 标签：多模态数据从一开始就参与 backbone 表示形成，loss、sampling ratio、sequence packing 与 router load 都共同决定能力。

它不必然优于 staged alignment。若高质量多模态数据不足、codec 尚不稳定或只需要专用理解能力，冻结 encoder + projector 更容易训练、验证和回滚。

Native shared parameters 也不等于所有目标共享一个 compute-optimal 数据配比。Text loss 与 multimodal loss 观察的
样本复杂度、token cost 和 capacity bottleneck 不同；增加 multimodal tokens 可能改善跨模态表示，同时挤占 text
objective 的有效 compute。系统因此不能把二者粗暴相加成一个 scalar scaling law，而应在冻结 architecture、token
semantics 和 compute accounting 后分别拟合，再观察 Pareto frontier：

```text
shared parameter budget + total compute
→ modality-specific loss surfaces
→ text / multimodal allocation frontier
→ chosen operating point + retained regression slices
```

它把 staged alignment 的“资产复用优先”演进为 native training 的“共同容量、分别计账”。收益是可以看到跨模态
transfer 与预算竞争，代价是每次数据配比、codec 或 objective 变化都可能移动 frontier；training loss 也不自动等于
downstream quality。数据 provenance 与 sampling 归第 27 章，objective/compute allocation 归第 28 章；本章只规定
representation identity 必须让这些计量可解释。数据有限、单模态质量优先或需要独立升级 encoder 时，late fusion
仍是更稳定的分支。


#### 统一 Pixel-space 仍要拆开表示与生成责任

encoder、projector 与独立 image decoder 分阶段训练时，modality boundary 清楚、组件容易替换；代价是理解表示与生成表示可能长期分叉。native pixel-space 分支让统一 Transformer 同时消费和产生更接近像素的 state，使数据配比、noise/causal objective、decoder capacity 与输出 fidelity 一起成为 representation artifact identity。共享 backbone 因而减少接口，不等于理解与生成已经共享同一证据标准。

统一训练能减少跨组件对齐，却扩大序列、显存和训练耦合，并把重建误差与语义误差混在同一更新路径。高分辨率成本不可接受、数据不足或只需单向理解时，离散 tokenizer 或冻结 encoder 仍更合适。`arXiv:2605.11061v1` 的 §2–§8 只支持作者的 pixel-level 架构、训练与图像评测；没有独立 limitations，也不能由其结果推出生产多模态系统的通用最优表示。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-11061 -->

## 连续表示、离散表示与混合表示

### 连续表示

连续 feature 保留较丰富的局部信息，适合理解、检索和精细感知；但它缺少天然离散 vocabulary，生成端通常需要独立 decoder，且不同 encoder 的 feature geometry 不可直接互换。

### 离散表示

离散 codes 可共享 categorical prediction objective，也适合缓存、传输和自回归生成。代价是 codebook collapse、rare-code mismatch、长序列和重建误差。一个 code 是否“语义化”必须由 intervention、retrieval 或 reconstruction evidence 支持，不能从可视化聚类直接推断。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-26089:start -->
离散化还要回答“沿哪个轴量化”。常见 patch-wise VQ 把每个空间位置的 feature vector 变成一个局部 code，空间网格自然提供 token identity 和生成顺序；另一条分支把覆盖整幅 feature map 的 channel 当作 codeword，于是一个 token 可以携带全局空间结构，序列也可能显著缩短。这个变化不是换一个 codebook 实现，而是同时改写 representation unit、sequence length 与 autoregressive factorization。

channel 本身没有天然的 coarse-to-fine 顺序。可以用 nested dropout 让训练频繁只保留前缀，从而在论文所测设置中诱导可截断 ordering；但该顺序是学习结果，不是 channel token 的固有性质。更短序列和较高 codebook utilization 换来全局 codeword、空间局部性、跨分辨率 resampling 和 ordering 稳定性的治理成本。若 ordering 未形成、resampler 漂移或全局 channel 混叠导致 reconstruction/generation 回归，应回退 patch/grid VQ、普通一维 tokenizer、独立 diffusion decoder，或继续保留连续 feature。现有证据只覆盖披露的图像重建、文生图模型与 matched token-budget 实验，不证明它普遍优于 patch token，也不覆盖视频、统一理解或生产吞吐。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-26089:end -->

两个离散 codec 也不是因为 token rate 接近就天然兼容。直接翻译 codebooks 时，direction、codebook index、position、effective rate 与 codec revision 都属于接口身份；桥接模型只能提出映射，waveform decode/re-encode 仍是兼容 fallback。收益是避开一次连续域往返，代价是跨 codec 误差和语言、音色、噪声域漂移，不能把有限语音实验外推为任意声学 token space 的无损互换。

<!-- source-family:SF-2026-ARXIV-2609-12563 -->

### 分层残差表示

分层 residual quantization 可以让前几层表达粗语义，后续层逐步补细节：

```text
z ≈ q_1 + q_2 + ... + q_L
```

这提供 progressive quality 与可变计算机会，却把 layer identity、缺层行为和 decoder compatibility 变成运行时 contract。只传前几层 code 可能节省 bandwidth，但不能假设所有任务按同样幅度退化。

### 混合表示

连续 semantic feature 与离散 reconstruction code 可以并存。前者帮助理解和对齐，后者支持生成。混合方案避免让单一表示同时承担所有目标，但也重新引入多路状态和融合复杂度。

音频把这条分层进一步变成运行时状态机。一个 coarse semantic stream 可以按时间推进，多个 residual
codebooks 在每个时间步补声学细节；Slow AR 拥有时间轴，Fast AR 拥有同一步的 codec depth：

```text
text / instruction / speaker turn
-> semantic-time token
-> residual acoustic codebooks
-> waveform decoder
```

它比单一 acoustic stream 更容易分离内容、音色和细节，也引入 codebook synchronization、speaker-turn
identity、streaming backpressure 与多级 cache。Fish Audio S2 的报告支持这种双层 autoregression 在其
instruction-TTS contract 中可行，不证明自然语言 style control 都被因果遵循，作者 WER 或 judge 分数也
不能跨 evaluator 外推。短音频、单 speaker 和 latency/部署简单优先时，单路 codec pipeline 仍合理。


### 统一 Visual Tokenizer 也可以拆分表示责任

让同一离散路径同时承担 topology、semantic value 与 residual texture，接口最简单，却会让重建细节和抽象语义竞争表示容量与梯度。一个分层责任分支把结构写入 attention relation，把语义写入 value，把高频纹理由独立 residual decoder 恢复；共享 tokenizer 仍是统一 artifact，但其内部 state owner 不再被误认为单一 code。

责任分解可能降低 reconstruction 与 abstraction 的梯度争用，却增加 teacher 依赖、额外 decoder、训练耦合和跨域迁移风险。分解不稳定、额外计算不合算或只需单向任务时，modality-specific encoder 或理解/生成双表示仍合理。`arXiv:2605.05646v1` 只支持作者在同 backbone、数据和 teacher 下的实验，不证明 Q/K–V 分工是唯一因果机制，也不覆盖音频、视频或生产 serving。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-05646 -->

### Rate、distortion 与下游容量必须联合选择

表示压缩率不能只由 latent channel 数或 reconstruction score 决定。若 latent 保留更多 information，下游 prior 或生成模型需要更大容量与更多 compute 才能拟合；若压得更狠，base model 的工作变轻，detail reconstruction 和 stochastic completion 的负担却转移给 decoder。于是系统 optimum 是联合问题：

```text
representation rate
<-> reconstruction distortion
<-> downstream model capacity
<-> decoder training and inference cost
```

这条路线从固定 spatial/channel bottleneck，演进到可度量的 rate，再到按 base-model capacity 选择 operating point。它没有否定传统 VAE、discrete codec 或 pixel-space model：低 latency、已有稳定 artifact、固定视觉域或需要明确 codebook identity 时，旧方案仍更合理。论文中排除 codec training 或 decoder sampling 的 FLOPs，不能被写成端到端系统更便宜。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-22691:start -->
固定 latent count 或把 posterior collapse 一律视为训练故障，是一个保守但合理的起点：decoder 过强、优化失衡，
或者任务确实需要所有 latent 时，collapse 会直接丢失有用信息。它的局限是无法区分“无用 tail 被目标函数主动剪掉”
和“重要模式被错误压掉”。在线性 Gaussian `beta`-VAE 这个严格边界内，可以把
`T = beta * sigma_dec^2 / V` 解释为归一化 information price，扫描不同 `T`，再用对 latent rescaling 不变的
posterior signal fraction 判断每个 PCA-like mode 何时停止携带 input-dependent information。此时 collapse 可能是
rate-distortion objective 的 mode-wise spectral pruning，而不必然是优化失败。

但这条 scan 只拥有提出 utility-ranked active-rank proposal 的权力。representation owner 仍须冻结 likelihood、
decoder variance、data variance、`beta` schedule、模型版本与 mode matching；最终是否采用，必须由 reconstruction、
semantic 或 generation 的下游 Gate 决定。它用多 operating-point 训练、谱匹配和归一化成本换取 data-dependent
capacity，也会受 mode rotation、mixing、degeneracy、finite optimization 与 nonlinear decoder 影响。现有 exact-v1
只在 WorldClim 的 linear-Gaussian 设置中验证 collapse threshold、marginal reconstruction utility 与 PCA weight
的一致，不解释 latent 语义，也不证明 nonlinear collapse 有益。mode identity、frontier、scan reproducibility 或
下游质量不通过时，应回退固定 latent budget、PCA/reconstruction control、降低 regularization、anti-collapse
schedule 或常规 VAE retrain。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-22691:end -->

<!-- semantic-body-binding:SF-2026-ARXIV-2609-13045:start -->
音频还揭示了一个容易被单一 rate–distortion 曲线掩盖的选择：低码率 token 是否必须独自保存波形中的全部信息。若 LLM 同时承担语义变换和说话人、韵律等声学细节，token rate 降低会把两类目标压进同一个窄瓶颈；序列虽然缩短，翻译内容与声音身份却更容易相互争用容量。一个不对称分支让低 rate VQ 只重建语义 SSL feature，服务 LLM 的内容生成；waveform decoder 再读取源语音的低层 feature，恢复 speaker/prosody。表示 owner 因而从“一个 token stream 保存一切”分成 semantic token 与 source-conditioned acoustic side channel，decoder 才负责最终波形合成。

这种分责用更短的 LLM 序列换来 source/target 时间对齐、decoder artifact identity、源说话人泄漏和额外安全边界。源音频不可继续保留、目标需要匿名化，或 online streaming 不能等待双路径对齐时，文本中间层、独立声码器或更完整 acoustic token 仍可能更合适。Kraken exact-v1 的 source-conditioning 消融只支持 Qwen3-8B、约 15 万小时训练数据、披露语言与离线 speech-to-speech translation 中的机制；小规模人评、未开放模型/代码和作者报告的 instruction-following 退化，都不支持把 325 bps 写成通用最优点或生产 streaming 保证。
<!-- semantic-body-binding:SF-2026-ARXIV-2609-13045:end -->


#### Codebook Capacity 也可以随位置递增

uniform codebook 让每个视觉 token 使用相同容量，编码、部署和兼容最简单；当序列按 coarse-to-fine 顺序增长时，累计容量可能在早期就跨过数据 uncertainty，后续位置难以继续形成层级。position-indexed schedule 先给早期 token 较小 codebook 表达粗语义，再逐步扩展后续容量承载细节；`position/order/N/K` 因而都进入 representation artifact identity，而不是只记录全局 bitrate。

递增容量可延长层级形成区间，却增加多 codebook 治理、kernel/layout 与训练不均衡，也依赖稳定的顺序语义。序列没有 coarse-to-fine 结构、兼容优先或收益不足时，uniform codebook 仍更合适。`arXiv:2605.06207v1` 只在 ImageNet 256 与作者 tokenizer/AR 设置中验证；entropy-cliff 阈值依赖数据、长度与 codebook，不能外推语言或其他视觉表示。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-06207 -->

### Representation Artifact 必须携带分辨率与下游容量合同

只按 reconstruction 选择视觉 tokenizer，在 decoder 足够大、下游任务接近像素重建时是合理起点；生成 prior 容量有限时，更高保真的 latent 反而可能更难建模。Artifact identity 应同时绑定 native-resolution/aspect-ratio policy、compression ratio、latent channels、decoder capacity 和 loss revision，再在 matched generator capacity 下比较 rate–distortion–generation Pareto frontier。

这会扩大联合搜索空间和训练成本，也不能从重建分数推出语义生成质量。固定分辨率、成熟 CNN tokenizer 或低成本部署仍可保留；generator、decoder 或数据分布变化后必须重新验收。现有 exact-v1 只支持作者的视觉 tokenizer、模型容量与任务，不给出通用最优压缩率。<!-- semantic-body-binding:SF-2026-ARXIV-2605-05331 -->

## Fusion：在哪里让模态相遇

### Early fusion

不同 modality 在 backbone 前或浅层合成一个 sequence。优势是 cross-modal interaction 充分；代价是序列更长、attention 成本更高，且强势 modality 可能支配梯度和位置预算。

### Late fusion

各 modality 独立编码，在 prediction head 或决策层融合。它保留专用模型能力和故障隔离，适合低耦合任务；但细粒度 token-region、word-frame 对齐难以形成。

### Cross-attention fusion

一种 modality 作为 queries，另一种提供 keys/values。它可以控制 interaction direction 和计算量，也把 connector capacity、query count 与 synchronization 变成显式瓶颈。

### Shared self-attention

所有 tokens 进入同一 self-attention graph。计算接口最统一，但必须明确 attention mask、position system、modality type、packing boundary 和 loss mask。没有这些元数据，同一个 sequence 中的相邻 token 可能只是打包邻居，而非语义邻居。

选择 fusion point 的稳定原则是：**越早融合，跨模态联合建模越强，隔离与可控性越弱；越晚融合，专用能力和治理越清楚，细粒度交互越受限。**

Fusion 还包含一个常被隐藏的 commit：把上游 posterior 立即压成 argmax。硬标签省带宽、易缓存，且当上游校准很差时可能更稳；但它不可逆地删除了次优语义，后续几何或跨模态证据也无法纠正。若下游能消费有限 alternatives，应把 posterior support 作为版本化状态延迟离散化，并同时测校准、带宽和任务增量；保留完整分布不是默认答案，关键是让 commit 时点与下游纠错能力匹配。

<!-- source-family:SF-2026-ARXIV-2609-12099 -->

多个 attention slot 并行读取 additive mixture 时，彼此不知道哪些输入成分已经被解释，容易在共享梯度下重复选择同一证据。若任务需要非冗余分解，可以为每个 token 保存“尚未解释的容量”：当前 slot 读取 residual evidence，经 attention 后才提交 bounded depletion，下一 slot 读取新 revision。该状态只拥有 representation allocation，不拥有外部事实真值；顺序化本身也不保证分解正确。

Residual evidence 用较少 slot collapse 换 ordering sensitivity、串行延迟、乘性误差和 task-dependent depletion。成分天然可分、冗余无害或 latency 优先时，普通 parallel/cross attention 仍更合适。`arXiv:2605.02323v1` 的证据只来自 synthetic mixtures、FUSS audio 与 LISA decomposition；它不证明通用 Transformer attention 都需要该机制，更不能把 learned depletion 当作 factual provenance 或 correctness signal。

<!-- source-family:SF-2026-ARXIV-2605-02323 -->

理解与生成也不必被迫共享全部参数。Fully native unified model 统一 objective 和 runtime 接口，却要求从头
解决跨 modality interference；post-hoc ensemble 可独立升级组件，却产生碎片化 conditioning。中间路线复用
成熟 understanding backbone，以其 hidden state 作为 semantic interface，再挂接独立 visual generation head，
并通过分阶段冻结/解冻与 loss ratio 管理能力冲突。InternVL-U 是这一 modular hybrid 的受限案例；它说明
“共享语义接口、保留专用生成路径”是可行分支，不证明其 benchmark 排名或具体 loss 比例具有通用性。
该路线用较低重训风险换双 compute path、interface drift 与 checkpoint coupling；数据和预算允许真正 joint
pretraining 时 native path 仍可能更合适，需要独立升级生成器时 large ensemble 也继续成立。

### Full-duplex 输入让 Fusion 变成在线状态路由

前述 fusion 默认一轮输入先结束、模型再开始输出。语音助手进入 full-duplex 后，用户流可能在 assistant 生成期间
继续到达，问题不再只是“在哪一层融合”，而是新 observation 何时可见、是否打断当前生成，以及哪些状态能够被
下一 token 消费。等待 utterance 结束最容易保持一致性，但 interruption latency 高；把所有新 audio token 直接
写入同一 self-attention stream 响应快，却可能改变正在生成序列的条件并破坏可重放边界。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-10199:start -->
一个中间分支把 user stream 保持为独立、带 timestamp 与 generation epoch 的 channel，再由 channel fusion 或
external cross-attention 在显式 safe point 提交给生成器：

```text
concurrent user frames
→ modality encoder + channel-local state
→ interruption / relevance policy
→ commit at a generation boundary
→ continue, revise or cancel assistant output
```

这里 encoder 拥有声学表示，fusion layer 拥有跨 channel interaction，interruption policy 拥有控制决策，已发送
token 则属于不可撤回的外部 effect；任一层都不能把自己的 confidence 冒充用户意图。更早 commit 可降低打断延迟，
代价是 coherence、rollback 与训练/推理对齐更难；更晚 commit 保留轮次语义，却可能错过实时控制窗口。低并发、
turn-based UI 或缺乏 interruption 标注时，原来的 utterance-level late fusion 仍是更稳健的基线。公开实验只约束其
模型、对话数据与延迟设置，不提供跨设备和生产噪声的通用结论。[受限证据：arXiv:2605.10199v1]
<!-- semantic-body-binding:SF-2026-ARXIV-2605-10199:end -->

fusion 之后仍要决定不同 modality 如何竞争有限 token budget。均匀或对称 compression 最容易实现，但默认各模态拥有相同 information role；当视觉承担事件定位、音频承担补充语义时，可以让视觉 anchors 条件化音频 selection。反过来，在 ASR、音乐或遮挡场景中，audio-first 或 full-token branch 仍可能更可靠。**方向性 compression 是受任务 truth authority 约束的 policy，不是“视觉永远更重要”的架构事实。**它还需要对 modality conflict、selector drift、chunk boundary 与 abstention 做显式验证。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-06708:start -->
当输入主要由长文本组成时，把页面渲染成图像再交给视觉 encoder，可以用少量视觉 tokens 传输布局和字符密度，避免 decoder 逐字消费原始 token。这个旧路径在版面结构重要、文本极长且视觉 encoder 已经部署时有现实价值；但压缩比不是 information fidelity。视觉表示是有损的 modality transport，OCR 小字、数字、否定词和稀疏关键句可能先于 token budget 被不可逆丢失。

因此 renderer、分辨率、视觉 encoder、token budget 与 query-conditioned route 必须共同版本化；router 只决定是否采用视觉压缩，原始文本或 source-linked readback 仍拥有事实 authority。收益是缩短 decoder context，代价是视觉编码开销、精度/覆盖漂移和两条输入路径的校准成本。作者结果只约束其渲染、模型与任务，不证明 text-as-image 普遍优于 tokenizer。需要精确引用、代码、表格或长尾字符时应保留原文，路由不确定时采用 foveated readback 或直接回退文本路径。<!-- source-family:SF-2026-ARXIV-2605-06708 -->
<!-- semantic-body-binding:SF-2026-ARXIV-2605-06708:end -->

### 固定预算要先分配信息责任，再选择具体 Token

固定音视频配比与均匀时间采样容易复现，也让 latency 和显存上界可预测；当不同问题依赖的 modality 与时间区域
相近时，它仍是合理基线。约束变化发生在总 token budget 固定、而问题所需证据高度不均匀时：只提高单个 token
的排序精度，无法补救一开始就分错给 modality 或事件的预算。

<!-- semantic-body-binding:SF-2026-ARXIV-2607-25669:start -->
一种分层分配先保持全局预算守恒，再把两个决策拆开：intermodal allocator 根据 query 所表达的任务类型，在音频与
视频之间分配预算；intramodal allocator 再依据局部复杂度与时间冗余，把各自预算分到 audio segments 或 video
frames，最后才由具体 selector 决定保留哪些 tokens：

```text
fixed global budget
→ query-conditioned intermodal allocation
→ content/redundancy-conditioned intramodal allocation
→ modality-specific selection or pruning
```

分层避免让“哪种模态更相关”和“模态内部哪段更重要”共用一个不可解释分数，也要求整数化后仍守恒总预算并保留
per-modality lower bound。代价是 query-to-skill 路由、局部复杂度与冗余估计都会漂移；一旦上层分错预算，下层再好
也无法恢复被提前删除的证据。任务类型未知、模态冲突或 calibration 失效时，应回退到固定配比、保守模态下限，
必要时保留完整 tokens。exact-v1 的 Qwen2.5-Omni、H20 与所列 benchmark 只证明这一分层策略在披露压缩率下的
受限收益；未披露的 precision、batch、concurrency 与 SLO 不能由平均加速外推。
<!-- semantic-body-binding:SF-2026-ARXIV-2607-25669:end -->

<!-- semantic-body-binding:SF-2026-ARXIV-2607-24794:start -->
视频内部还要区分局部细节问题与跨事件问题。只按 query-frame similarity 取全局 top-k，容易把预算集中到同一
高分片段；先解析 query 的 temporal granularity，再把候选帧组织为时间连续的事件、按事件相关性与覆盖分配固定
frame budget，能在不增加总帧数时保留更合适的时间证据。这里 query parser、temporal-semantic graph 与 event
clustering 共同拥有的是 evidence-routing proposal，不是视频事实或因果结构；下游回答与 Evaluation 才能判断所选
证据是否充分。额外的 LLM parsing、CLIP、聚类与图传播增加 latency，并会因错误实体、错误事件边界或稀有瞬时证据
造成不可逆遗漏。解析不稳定或证据完整性优先时，应回退 uniform/static-query sampling；预算允许时直接使用 dense
frames。exact-v1 仅在三种 MLLM、四个 LongVideoQA benchmark 与固定 frame budget 下支持作者结果，不证明该
selector 可在任意视频、实时 SLO 或开放问题上识别全部关键证据。
<!-- semantic-body-binding:SF-2026-ARXIV-2607-24794:end -->

### 固定表示之后，可以按未决 Claim 主动补充 Observation

一次性均匀采样或 top-k selection 在低分辨率已经足够、latency 上界严格时最容易复现；高分辨率细节只占很小区域时，它又可能在第一轮压缩中不可逆丢失。一个 bounded active-observation 分支先保留全局低分辨率 context，再由 acquisition policy 根据当前未决 claim 提出下一处 crop。Evidence assembler 记录坐标、尺度、采集顺序与预算，answer gate 决定继续、提交或拒答；selector 只拥有 observation proposal，不拥有 evidence sufficiency。<!-- semantic-body-binding:SF-2026-ARXIV-2605-01345 -->

主动取证以额外调用、路径依赖和尾延迟换取局部细节可见性，也可能因错误 crop、漏区或 backbone hallucination 形成自确认。采集策略漂移、证据完整性优先或预算不足时，应回退均匀/静态采样，必要时保留完整 tokens。exact-v1 只支持作者 VLM、crop proxy 与高分辨率 benchmark 下的机制方向，不证明 crop proposal 是充分证据或能覆盖开放世界视觉风险。

### 任务贡献与当前可靠性不能共用一个 Gate

静态融合或单一 gate 默认“某模态通常有用”就等于“当前样本值得信任”。任务贡献回答的是长期问题：在目标
workload 中，文本、图像或音频各自提供什么信息；sample-specific reliability 回答的是当前问题：这次 observation
是否因噪声、缺失、冲突或 domain shift 而失真。两种 signal 应先分别估计，再由 fusion policy 合成：

```text
modality representation
├─ task-contribution sensor
└─ sample-specific reliability sensor
             ↓
calibrated fusion policy
→ conflict / abstention / single-modality fallback
```

可靠性估计器拥有的是 policy hint，不是真值概率。用 predicted variance、confidence 或 reconstruction error 调整
权重，可以避免一条受污染模态拖累全部表示；但估计器自身也会漂移，并可能在相关噪声下共同自信。它用额外
训练、校准和故障切片换取 sample-adaptive fusion。数据稳定或 calibration evidence 不足时，静态权重、late fusion
与单模态 fallback 仍更可解释。相关受限实验只证明特定情感数据、模型、硬件和随机种子下的分支可行性，不支持
把 inverse variance 外推为跨任务 truth authority；第 66 章负责验证 calibration、risk–coverage 与 abstention。

## 对齐不是把向量拉近这么简单

### Caption 是不对称的辅助证据，不是图像替身

让视觉模型先生成 caption 再交给语言模型，复用文本推理能力且接口简单；caption 一旦遗漏或错误，又会成为强语义锚点。更稳健的分支并行保留图像直答与 caption 辅助路径，用 confidence gate、information gain 和来源权重决定融合、拒绝或回退。Captioner 只拥有 evidence proposal，原始视觉状态保持独立 identity，answer gate 决定是否采用。

双路径增加计算和校准成本，两个分支也可能共享同一视觉偏差；低分辨率、低风险或 caption 质量已知稳定时，单路径仍可用。冲突无法消解时应回到原图复核或拒答。现有 exact-v1 只支持作者的模型与视觉问答任务，不证明该 gate 给出事实置信度。<!-- semantic-body-binding:SF-2026-ARXIV-2605-01733 -->

跨模态 alignment 至少包含三种不同目标：

1. **语义对齐**：文字 “red cup” 与对应视觉区域表达相近概念。
2. **时空对齐**：语言片段、音频事件、视频 frame 与动作发生在对应位置和时间。
3. **行动对齐**：表示不仅描述相似，还能支持正确 action 或状态转移。

contrastive loss 可以改善全局语义检索，却不保证像素级定位；captioning loss 能连接语言与图像，却可能依赖语言先验而忽略视觉；reconstruction loss 保存低层信息，却不保证语义可分。实际系统常采用多目标：

```text
L = λ_sem L_semantic
  + λ_rec L_reconstruction
  + λ_temp L_temporal
  + λ_act L_action
```

权重不是纯训练超参数，它定义模型优先保留什么信息。某种 benchmark 的提升不能证明 representation 在所有下游任务上更完整。

## 时间、空间与 provenance 必须进入状态

视频、音频和传感器融合最危险的错误常不是 tensor shape，而是时间错位。系统至少要记录：

```text
sample timestamp
capture duration / frame interval
sensor clock and synchronization quality
spatial frame / camera intrinsics / extrinsics
transform or augmentation lineage
encoder / codec / codebook version
```

若一段视觉 token 与动作 token 相差 200 ms，模型仍能计算 attention，却可能学习到错误因果关系。若 augmentation 改变左右方向而 action label 未同步，数据表面合法，控制语义已经被破坏。

provenance 还决定删除与再训练。当原始图像因授权被撤回时，系统需要知道哪些 clip、embedding、index、codec cache、checkpoint 和 evaluation run 受影响。多模态表示因此不是“训练前处理细节”，而是资产生命周期的一部分。

端到端 temporal benchmark 失败时，仅知道“时间表示不够”仍无法定位修复 owner。可以在 encoder、projector 与 LLM 接口分别训练同一 Arrow-of-Time probe：若 encoder 可解码而 projector 后消失，优先修复 connector/fusion，而不是盲目增加 frames 或扩大语言模型。probe 只拥有 bottleneck diagnosis，不拥有 temporal-understanding 或因果真值。<!-- semantic-body-binding:SF-2026-ARXIV-2605-07568 -->

逐层探针增加对照与校准成本，也会受帧数和 probe capacity 影响；高可解码性不保证模型真正使用该信号。结果不可复现或 probe 与行为脱钩时，应回退遮蔽/反事实任务与端到端 temporal benchmark。exact-v1 的 16-frame、Q-Former/time-preserved MLP 和作者 temporal tasks 不证明通用视频理解、更长视频或 Serving 收益。

## Conditional compute 与 modality routing

MoE 可以让不同 token 选择不同 experts。观测到某些 experts 对视觉或音频 token 使用率更高，只能说明 router 在当前数据与 objective 下形成相关性；不能直接命名为固定的“视觉专家”。

路由的系统约束包括：

- modality mix 改变时 expert load 是否漂移；
- 视频长序列是否让少数 experts 过载；
- padding 与无效 frames 是否进入 router 统计；
- expert placement 是否与 modality data locality 冲突；
- router、codec 和 backbone 升级后，旧缓存是否仍有效。

因此 native multimodality 会把表示问题传递给 communication 和 scheduling，而不是消除它们。

## Training 与 Serving 的边界

本章定义 representation contract；第27～29章负责数据配比、pretraining 与 instruction alignment。训练时必须区分 raw-sample count、seconds/frames、codec tokens 和 loss-bearing tokens，否则“多模态 token 数”没有稳定含义。

Serving 侧还要面对 modality-specific admission：一张高分辨率图像、十秒视频和一段文本不能仅按请求数计费。runtime 应在 encode 前估计 token expansion、decoder/refiner 成本、deadline 与 cache policy。具体 batching、KV 和 SLO 归 Part V，但其输入 contract 由本章产生。

### Edge split 把 fused latent 变成通信接口

<!-- semantic-body-binding:SF-2026-ARXIV-2609-11058:start -->
端云拆分的旧路径，要么把原始图像、音频和文本全部上传，要么让每个模态分别跨边界传输 feature 或架构特定 activation。前者把无线链路变成瓶颈，后者又把服务端紧耦合到多个 encoder 的内部形状。对通信受限且任务相对稳定的部署，可以在端侧先完成模态专属编码与融合，再把一个 task-aware fused latent 压缩为有版本的表示接口，由服务端 projector 或 decoder 恢复成模型可消费的 token 或 soft prompt。

这个接口不能只写一个 latent dimension。它至少要固定 encoder、fusion 与 compressor 版本，模态集合及时间对齐，缺失模态和 provenance 标记，dtype/quantization、压缩预算，以及训练时优化的任务目标。这样做把“跨模态语义如何融合”和“跨链路传多少字节”合并为一个可审计合同；但压缩 latent 不是隐私证明，服务端也不能假设它对未来未知任务保留了全部原始事实。

主要 trade-off 是任务适配性换通信量：task-aware 压缩可能在当前判别任务上近似保真，却丢掉未来检索、生成或安全审计需要的信息；端侧编码与融合本身也消耗算力、内存和能量，当带宽充足时，编码开销可能超过传输收益。现有证据只覆盖单一图文匹配任务和估算网络条件，没有真实端侧能耗、并发、无线抖动或隐私攻击验证。因此系统应保留 fallback：任务漂移或审计要求高时上传原始或较低压缩表示，多任务难以共享瓶颈时保留 per-modality feature 或 late fusion，链路不再受限时允许绕过端侧压缩；不要把一次任务内精度接近解释成通用多模态表示已经无损。
<!-- semantic-body-binding:SF-2026-ARXIV-2609-11058:end -->

### Codec-aware tokenization：稀疏性可以在视觉 Encoder 之前暴露

逐 frame 解码为 dense RGB patches 是最通用的旧方案：模型不依赖某种压缩格式，也能统一处理静态图像、
视频和编辑后的像素。长视频中它会重复编码大量相似内容。Codec-aware 路线至少有两条不同分支：

```text
decoded RGB frames
→ use codec motion/residual metadata to select sparse RGB patches

compressed video primitives
→ encode key frames plus motion/residual delta tokens directly
```

长视频还存在另一种可复用性：背景和对象外观在一段时间内近似不变，而运动证据持续变化。把两者继续编码成同一种逐帧 token，会让 invariant content 重复占用容量。Video tokenizer 可以分离 time-invariant scene token 与 dynamic motion token，并只在明确的 scene/epoch 范围内广播前者；representation identity 必须同时携带时间范围、场景版本与失效条件，镜头切换、遮挡或快速运动时立即重新编码。

Tokenizer owner 持有 TIV/TV 分解、scene/epoch scope 与 invalidation；decoder 只消费已验证的 token identity，镜头切换时无权继续广播旧 TIV。

这种分解减少重复计算，却会让错误的 invariant 判断跨帧传播。场景边界不可靠或视频很短时，dense frame token 仍更简单；现有证据只绑定作者 tokenizer、视频数据和压缩设置，不构成通用质量或速度保证。

<!-- semantic-body-binding:SF-2026-ARXIV-2606.17590 -->

前者仍把选中区域解码为 RGB，兼容已有 vision encoder，却可能漏掉 codec metadata 未显著标记的语义变化；
后者减少重复 decode/encode work，却把 codec、GOP、motion vector、residual layout 与 tokenizer 一起变成模型
输入协议。Transcoding、随机 seek、corrupted stream、不同 codec/profile 与 frame-rate conversion 都可能改变
token identity。Dense frames 在格式多样、证据完整性优先或 codec path 不可信时仍成立。

因此“视觉 token 更少”只证明 representation rate 改变，不自动证明 TTFT、KV capacity 或 end-to-end latency
按比例下降。评估必须绑定 source codec、resolution、duration、sampling/GOP、model、hardware、precision、
batch/concurrency 与 SLO，并分别测 retained evidence、encode cost 和 downstream outcome。

另一条分支不是改变视频的编码格式，而是由当前问题决定下一次读取的时间段、帧率与模态，通过读取工具取得视觉、音频或 transcript 后再继续推理。它能避开无关输入并回看短暂事件，却把证据遗漏、读取历史与额外推理/tool round-trip 变成新的责任；少载入 token 不保证更低的端到端时延，短片或完整证据优先时，固定读取仍更简单可靠。

### 用表示几何区分重排与扩展

把 Attention 与 FFN 都概括为“融合信息”会掩盖二者可能承担的不同责任。更细的诊断可以同时观察 residual update 是否引入新的子空间，以及 token mixing 带来的信息增量：在一组受限的视觉语言模型中，Attention 更接近在已有子空间内重排跨模态关系，FFN 则更像扩展可表达方向；部分层替换实验还提示，learned visual routing 可能存在冗余。<!-- semantic-body-binding:SF-2026-ARXIV-2605-05668 -->

这不是 Attention 普遍无用的结论。证据只覆盖两个模型家族、15 个变体、七个 benchmark 和被选择的层；相关统计也不能代替端到端因果验证。若同类诊断或替换不能在目标模型与任务复现，就应保留 learned Attention，并用 causal ablation、质量回归和 serving cost 共同决定是否改变结构。

## Failure modes

### 语义锚点不是原模态的替代品

长音频可以借助 transcript 作为 semantic anchor，把声学 token 与时间轴、实体和语义片段对齐，再依据时间衰减和 accumulated attention 压缩 cache。它比只按位置裁剪更理解内容，却把 ASR 错误、语言覆盖和时间对齐偏差引入表示 identity。原始声学 token 仍拥有音色、韵律、重叠说话人与非语音事件；anchor 只能帮助选择，不能成为无损真值。

因此系统应同时保留 `raw modality span → anchor revision → fused token range` 的 provenance。低资源语言、噪声环境、实时 streaming 或 ASR 不可信时，固定窗口与原模态保留仍是更稳健的旧分支。

### Representation collision

不同 modality 或不同 codebook version 产生相同 ID，却被错误共享 embedding。解决方式不是只增加一个 type embedding，还要校验 artifact identity。

### Modality domination

数据量、loss scale 或序列长度更大的 modality 主导训练，模型看似统一，实际弱化其他能力。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-19250:start -->
最终 hallucination rate 只能说明发生了冲突，不能定位谁在控制表示。一条机制诊断把 attention heads 分为分布式的 hallucination-driving path 与少量 resisting path，并用独立 hidden-state probe 判断当前样本是否存在模态冲突；只有 sensor 触发时才抑制 driving heads。这样把“检测冲突”和“改变融合控制权”分成两个状态，避免全局删 head 破坏正常输入能力。

条件干预仍依赖标注 probe、prefill 因果分析与 head identity，视觉证据本身错误时还可能放大另一种幻觉。sensor 漂移、模型 revision 改变 head 角色或真值模态不确定时，应回退原始路径、外部 evidence check 或 abstain。现有结果只覆盖五个开源 MLLM、MMMC 与 SCI-SemanticConflict，并把视觉作为真值，不能证明开放环境或其他冲突类型的稳定性。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-19250:end -->

### Temporal aliasing

低 frame rate 或不一致采样把不同运动映射成相似 token，后续 world model 无法恢复丢失动态。

### Train/inference mismatch

训练数据只包含高概率 codec path，生成时 rare code 或累计量化误差使 decoder 离开训练分布。过滤低置信序列可以缓解崩溃，也可能删除稀有但有效样本。

### Connector shortcut

模型依赖 caption、layout 或 metadata shortcut，而没有真正消费目标 modality。需要遮蔽、反事实和跨分布测试，而非只看平均分。

视频中的 shortcut 还需要检验“答案应变”与“答案应保持”两种关系。单条 QA accuracy 即使很高，也可能只是从静态 cue 猜对：对 direction/order 一类 dynamic question，语义保持的 temporal reversal 或 flip 后答案应按声明关系改变；对不依赖该变换的 static question，答案则应保持不变。评测与训练因此要冻结 original/counterfactual pair、transform revision、问题路由与 expected relation，并使用 strict pair accuracy 拒绝只在一侧猜对的固定答案。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-21988:start -->
Transformation/router 只定义 expected relation，原始标签或独立 verifier 仍拥有 correctness，optimizer 只消费通过 Gate 的 paired reward；成对一致也不等于事实正确。该分支暴露单帧和语言 shortcut，却增加双路视频 rollout、router/transform lineage 与 normalization 成本，也可能因 flip/reversal 改变了本不该变化的语义而制造伪监督。若 transform validity、router agreement、pair correctness 或 general-video regression 失败，应停用 relational reward，回退 verified original examples、显式 temporal labels、完整视频评测与人工审核的 counterfactual。现有证据只覆盖作者的短视频、两类 transform 与披露模型，不证明任意视频编辑都保持语义或已学到长程因果理解。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-21988:end -->

## 工程决策框架

设计多模态系统时，先回答：

1. 任务需要理解、生成，还是两者都要？
2. 哪些信息必须可逆，哪些可以有损？
3. 最小时间和空间分辨率是什么？
4. encoder/codec 是否可独立升级，缓存如何失效？
5. fusion 发生在哪里，谁拥有 attention mask 和 packing boundary？
6. 每种 modality 的计量单位是什么？
7. provenance、授权、删除如何传播到 derived artifacts？
8. 线上需要的 latency、streaming 与 edge placement 是否允许复杂 decoder？

若这些问题没有答案，“统一多模态模型”还只是模型名称，不是系统设计。

### 条件化机制分支与共存边界

主线之外仍存在若干只在特定前提下成立的设计分支。下面按状态与控制权的变化说明它们解决的问题、新增代价及回退边界；来源身份和实验限制统一留在章末 Review notes。

<!-- semantic-body-binding:SF-2026-ARXIV-2607-10599:start -->
多模态融合应分开任务贡献与 observation reliability：贡献 router 用 leave-one-out task degradation 学习某模态是否有用，独立 uncertainty head 估计逐模态 log variance，再以 inverse-variance 权重校准 fusion gate。它避免把“有用”误写成“当前样本可靠”，代价是额外反事实监督与校准漂移。
<!-- semantic-body-binding:SF-2026-ARXIV-2607-10599:end -->

### Native 3D Token 把几何从 Sidecar 变成可修订状态

先由独立 3D reconstruction pipeline 生成 mesh，再把结果作为多模态模型的只读输入，职责清楚且容易单独验证；当任务要求多轮理解、生成和局部编辑保持同一几何身份时，stateless sidecar 会丢失跨轮 mesh state。另一条分支把 3D primitives/mesh 表示纳入统一 token contract，并让 modality-specific experts 共享同一 identity 与 revision。

它提高跨任务连续性，却增加 tokenizer/mesh discretization、长 Context、几何一致性和编辑回滚成本。模型拥有 proposal，不拥有物理几何真值；identity 保持和生成 fidelity 也不能证明真实世界尺度或可执行性。单次重建、精确 CAD 或安全关键几何仍应由专用工具与确定性验证承担。

<!-- source-family:SF-2026-ARXIV-2605-16745 -->

逐帧视频 token 仍可能把同一对象在不同视角和时间中的身份复制多次。Track-aligned 表示把稳定背景与动态对象分开，并让轨迹、相机和时间成为 token identity，从而把 frame archive 压成可修订的 4D state。它获得存储与生成上的复用，却依赖 track、camera geometry 和 static/dynamic disentanglement；视觉可重建不证明物理动力学，真实 transition 仍由下一章负责。

<!-- source-family:SF-2026-ARXIV-2609-12874 -->

## Token Hierarchy 可以承载不同时间尺度

音频等高带宽模态若只用单层离散码，要么语义结构过粗，要么 token rate 过高。分层 residual quantization 可以让上层 code 承担长程语义和结构，下层 code 补局部声学细节；相应生成器也可分为 global sequence model、local refinement 与连续 decoder。

层次化表示提高可控性，却引入 codebook synchronization、跨层 error propagation 和更复杂的 bitrate/latency 预算。它是表示分解，不证明某个公开音乐模型的质量结论可外推；Ch24 只接手后续生成与修正机制。

高频触觉进一步说明“同一时间轴”不等于“同一采样密度”。接触事件稀疏时，复制成 dense visual stream 会浪费预算并稀释信号；更合适的 contract 是为 tactile event 保存独立 rate、timestamp、sensor calibration 与稀疏预测目标，再由共享语义层消费。代价是异步对齐、漂移和缺失事件，传感器或 embodiment 改变时不能继承旧 token identity。

<!-- source-family:SF-2026-ARXIV-2609-12549 -->

## Streaming Multimodal Identity 不止是 Token Type

实时全双工系统中，用户音频、视频、文本与 assistant 输出会并发到达，输入不会在生成开始前自然结束。表示层必须把 token 绑定到 timestamp、speaker/turn、observation revision 与 interrupt frontier；fusion 只负责产生共享表示，runtime 才决定哪些输出可以继续、取消或提交。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-25621:start -->
无限保留流式历史不现实，固定窗口又会丢掉远处但仍有效的跨模态证据。一个受限分支把音视频证据压成固定预算的 long/short-term memory，再由独立 hidden-state trigger 判断何时主动响应。Memory 只保存带时间与来源的 evidence，trigger 只提出 reply timing，runtime 仍拥有 commit/cancel；不能用 silence token 或模型内部触发替代外部 turn-taking authority。

持续压缩和 trigger 增加计算、时序对齐和阈值校准，压缩漏证或 false trigger 会导致过早回答或关键时刻沉默。越界时应回退固定窗口、显式 turn-taking/外部 router，或离线完整上下文。作者 benchmark 只支持所测音视频任务，不证明任意全双工服务的实时性和可靠性。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-25621:end -->

统一 attention 可以促进跨模态协同，却也可能让高资源模态挤压另一模态。modality-specific encoder/FFN 保留专用容量，shared layer 提供交互；早统一减少接口鸿沟但增加目标竞争，晚统一更稳定却容易形成“vision laziness”。选择应随数据复杂度、模态预算和交互 deadline 变化，不存在仅凭统一程度判断优劣的结论。

### 实时多模态表示还必须拥有可中断的时间状态

离线的图文拼接可以在全部输入到齐后一次编码；full-duplex 交互中，音频、视频、文本、tool event 却在不同时间抵达，用户还可能在模型输出中途插话。表示层因而不仅要标记 modality，还要保存 timestamp、stream revision、turn ownership 与 interrupt boundary，使后续状态机知道哪些 token 已提交、哪些生成应取消、哪些观测仍可继续复用。统一 backbone 减少专用管线，却把时钟漂移、乱序、过期观测和半双工回退变成显式 failure mode；无法稳定对齐时，分模态缓冲与保守 turn-taking 仍是合理旧方案。官方公告只支持所披露系统具备统一音视频文本与全双工交互接口，没有公开这些状态字段的内部实现，也不构成通用打断或安全保证。
<!-- source-family: https://seed.bytedance.com/en/blog/seedrealtime-audio-visual-full-duplex-llm-released-toward-omni-modal-natural-interaction; daily: 2026-08-05; semantic-body-binding: interruptible-streaming-multimodal-identity -->

### 共享表示的收益来自可控的容量交换，而不是“越早融合越好”

晚融合让各模态保留专用容量，训练稳定且易隔离，却可能让视觉只在末端提供旁路信息；早融合让 attention 与 normalization 更早交换信息，但也会让文本与视觉目标竞争同一容量。一种中间分支是共享跨模态交互层、保留 modality-specific FFN 或路由容量，并按数据复杂度与 token 预算重新选择配比。它用更强 transfer 换来 routed capacity、通信和配比校准成本；在数据不足、模态分布漂移或硬实时单模态路径中，专用 encoder 与晚融合仍应共存。
<!-- source-family: arxiv:2608.05000v1; daily: 2026-08-06; semantic-body-binding: multimodal-capacity-sharing-frontier -->

### 统一架构不等于双向可用的统一语义空间

共享 backbone、token space 或 loss 只能说明不同模态在同一计算图中交互，不能证明 understanding 分支形成的方向可被 generation 分支以相同语义读取。更强的对齐证据需要跨分支干预：从一侧提取语义方向，在另一侧做 matched steering，并用 random、unrelated direction 与人工/任务结果作对照。

受控实验观察到的单向可迁移也不能自动升级为共享因果表示；概念集合、prompt 组合、投影方法与 evaluator 都可能限制结论。干预式验证换来更强证据，但增加 off-manifold steering 和 evaluator bias。因而 representation contract 应区分“共享参数”“可解码相关性”与“跨分支可操纵语义”；对齐证据不足时，modality-specific interface 和显式 adapter 仍是更稳妥的共存方案。

<!-- source-family:SF-2026-ARXIV-2607-26411 -->

理解和生成还可能使用两套不兼容的视觉 token：前者强调语义压缩，后者强调可重建细节。共享 backbone 并不能消除这种 identity split。可选分支是让 context 与 visual generation 共享 tokenizer，并用并行 bitwise prediction 提高 autoregressive 表达效率，同时保留独立 decoder 负责生成 artifact。Tokenizer owner 持有 token/bit layout 与 rate–distortion 版本，decoder owner 持有重建合同；二者不能用“统一 token”相互代替。

统一表示降低接口分裂，却引入 bitwise independence 假设、decoder 版本耦合和理解/生成目标竞争。单一表示不能同时在所有任务上最优；当重建质量或理解能力受损时，双 tokenizer 与显式 bridge 仍是合理分支。

<!-- semantic-body-binding:SF-2026-ARXIV-2606.18249 -->

### Faithful transcription 与语义归一化是不同输出合同

通用 VLM 用语言先验修复噪声字符，在问答和理解任务中可能合理；当任务要求逐字 OCR、证件号或代码抄录时，同一机制会把异常字符串改写成更 plausible 的文本。语义正确率不能替代 character-level fidelity，representation pipeline 必须显式声明输出是 transcription 还是 interpretation。

跨系统、语言和扰动实验只能说明这种风险存在，不能证明所有 VLM 都不适合 OCR。需要 exact evidence 时，应保存 source image、使用 OCR-specialized/raw-text 路径并做字符级对齐；允许语义归一化时仍应把改写标为 derived artifact，而不是冒充原文。

<!-- source-family:SF-2026-ARXIV-2607-21617 -->

## 本章在知识树中的位置

Part II 给出通用 Transformer 组件；本章把单一文本 token 扩展为跨模态 representation contract。第24章进一步比较这些表示如何生成与修正；第25章要求表示支持 action-conditioned dynamics；第26章把 timestamp、coordinate 和 action schema 放进物理闭环。

训练数据、配比与 objective 归 `TRAIN-DATA` 和 `TRAIN-PRETRAINING`；线上 modality batching 与 KV 归 Part V；benchmark contract 归 `PLATFORM-EVALUATION-SYSTEM`。一个机制只有一个 owner，其他章节只消费接口。

## 从机制演进到系统设计

多模态表示从简单拼接演进到有类型的共享空间后，系统必须同时管理任务贡献与 observation reliability：一个 modality 对任务有用，不代表它在当前样本中可靠。时间、空间、modality、encoder revision 与 provenance 因而成为 representation identity 的一部分。

更细的 routing、uncertainty weighting 与 token compression 能节省共享容量，却会引入 calibration drift、语义 anchor 错误和跨语言/流式累积偏差。融合证据不足时应保留 modality-specific path、原始输入或保守 late fusion；native multimodal training 仍是多目标 capacity allocation，而不是自动抹平 modality boundary。

### 从局部结果到可执行的系统边界

<!-- body-source:SF-2026-ARXIV-2606-22565 -->
多模态 CoT 的收益瓶颈常在视觉 representation 而非文字 reasoning 长度；系统要分开 visual extraction、reasoning token 与最终 task evidence。 这项变化只在 exact-v1 披露的 workload、状态身份和评估合同内成立；benchmark/model slice 不证明所有 modality；reasoning trace 也不等于因果使用的视觉证据。 因此旧路径在这些新增约束不存在、证据条件不足或失败回退被触发时仍然成立，不能被新的局部结果静默覆盖。

## 面试与自检问题

1. 为什么 `[T, d]` shape 相同不表示两种 modality 已经对齐？
2. continuous feature projection 在什么条件下优于离散 unified tokens？
3. codebook version 为什么会影响 cache identity？
4. early、late 和 cross-attention fusion 的主要 trade-off 是什么？
5. semantic alignment、temporal alignment 与 action alignment 有何区别？
6. 为什么看到 MoE routing correlation 不能直接宣称出现了语义专家？
7. 多模态请求为什么不能只按 request count 做 admission？
8. 如何验证模型没有使用 caption 或 layout shortcut？

## Research Outlook

长期问题不是找到唯一 tokenization，而是建立可迁移的 modality contract：表示能否在 fidelity、sequence length、reasoning、generation 和治理之间形成可选择的 operating points；不同 codec/backbone 能否安全组合；time/space/provenance identity 能否被训练、runtime 和 evaluation 共同消费。

## Reflection

如果把多模态简化为“更多输入类型”，系统会在数据、缓存、计费和验证阶段重新付出隐藏成本。真正统一的不是所有信号的物理性质，而是它们进入模型前后都有清楚的身份、损失边界和可验证接口。

### 从统一表示到可观测、可裁剪的跨模态状态

多模态模型把不同输入映射进共享表示后，不能仅凭最终答案判断视觉证据是否真正参与了生成。视觉 token 上的
attention spectrum 可以成为 hallucination risk 的在线 sensor，并在 decoding 时调整候选；但 probe 只拥有风险提议权，
不能把相关性当作事实真值。它依赖 grid visual token，且现有结果未覆盖更大模型与 reasoning-intensive workload；
传感器失校准时应回退外部 grounding、独立 verifier 或保守拒答。

<!-- source-family:SF-2026-ARXIV-2605-11559 -->

固定 token budget 下，纯视觉重要性排序会忽略音频已经解释掉的画面。audio-guided selection 先估计跨模态冗余，再
保留音频无法替代的视觉 token，并在时间轴上合并相近状态。收益是把预算分给互补信息，代价是音频预测器偏差、
同步误差与关键静默画面被误删；音频缺失、噪声大或安全任务要求完整视觉 provenance 时，应回退单模态保守保留。
现有证据仅支持作者六个 audio-visual benchmarks 与受测模型。

<!-- source-family:SF-2026-ARXIV-2605-11605 -->

表示身份还可能从 ISP 后的 RGB 扩展到 measurement-domain evidence。把原始传感读数、camera conditioning 与 exposure
supervision 纳入样本和 checkpoint，可以减少 ISP 丢失物理信息后的不可逆猜测；同时也引入相机标定、raw schema、隐私和
设备漂移。只有下游任务确实依赖测量域信息且采集链可版本化时才值得使用，否则标准 RGB/VLM 接口仍更便于迁移。
论文结果限其相机、数据、任务与模型，不证明所有视觉语言系统都应消费 raw measurements。

<!-- source-family:SF-2026-ARXIV-2605-11727 -->

当文字 CoT 难以表达空间中间态时，还可以把文字与辅助图像写入统一 canvas，再压缩为连续 latent reasoning state。
这让布局、OCR 与视觉草图参与后续推理，却牺牲部分可检查性，并把 canvas codec、压缩器和 token budget 变成新的状态
身份；OCR/layout 失败会污染整条链。高风险任务仍应保留可读 trace、外部工具和最终证据验收，不能把 latent state
当作可解释证明。现有证据只覆盖作者的 VLM reasoning benchmarks。

<!-- source-family:SF-2026-ARXIV-2605-11856 -->

### Object Hallucination 需要分开视觉写入与语言读取

对象幻觉常被压成一个端到端错误率，但同一错误可能来自视觉证据没有进入表示，也可能来自证据存在却被语言 prior 覆盖。Dual-pathway circuit analysis 用层级定位和因果干预区分 visual-evidence write path 与 language-prior read path，使“看不到”和“不采用”成为不同故障。<!-- semantic-body-binding:SF-2026-ARXIV-2605-13156 -->

Circuit probe 依赖所测模型、层选择和干预定义，不能把相关 activation 当成唯一原因。诊断不稳定时，应回退输入/输出级的证据对齐、反事实图像和行为评测，不据单个 circuit 自动修复模型。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-14621:start -->
同一故障也可以在单次主干计算中构造内部对照：shared early prefix 保留 prompt、history、position 与早期 grounding，late
counterfactual branch 屏蔽 image-token access，再由 contrastive decoder 比较视觉证据是否仍在后层写入。该 branch 只提出
token proposal，不能把 hidden-state 差异升级为事实真值；独立 grounding/evidence gate 仍拥有 acceptance。它减少外部图像
扰动和第二次完整 forward，却增加 white-box hidden-state、mask/cache 与 late-layer compute 依赖。模型接口不可见、cache
不兼容或内部对照失效时，应回退外部反事实、grounding verifier 与行为评测。exact-v1 只支持作者模型和实验。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-14621:end -->

### 感知到了，不等于行动会使用该模态

多模态模型在普通问答中识别音频或视觉信息，并不能证明冲突出现时会让该模态改变结论。评价需要把 perception、对误导 premise 的 rejection 与最终 action use 分开；否则模型可能“说出看见了什么”，却继续服从文本先验。<!-- semantic-body-binding:SF-2026-ARXIV-2605-13737 -->

现有 500-clip 长视频 benchmark 只提供受限测量，不能覆盖所有模态冲突和真实行动风险。跨模态冲突结果不稳定时，系统应保留独立的 evidence gate 和人工升级路径，而不是让 fusion score 直接拥有决策权。

### 可复用 Multimodal Perceiver 可以缩小适配面，但不能消除边界转换

<!-- semantic-body-binding:SF-2026-ARXIV-2605-15300:start -->
常规 VLM 以 modality-specific encoder 加 projector 接入语言模型，在视觉分布固定、目标 backbone 单一时最清晰；每换一个语言模型都重新训练 projector，则把适配成本和 alignment drift 复制到每个组合。一个替代分支先训练较小的可复用 VLM perceiver，让其语言块在目标 LLM 之前完成初步视觉—文本对齐，再把紧凑表示交给不同下游 backbone。perceiver 拥有跨模态表示 proposal，目标 LLM 仍拥有生成状态，接口 schema 与评测 gate 决定两者是否兼容。

复用减少重复训练，却没有让 modality boundary 消失：中间语言块增加 compute，token/schema 不匹配会破坏可移植性，适配过强还可能覆盖原有语言能力。exact-v1 的 §2.1–2.3、§3、§4.1–4.5、Appendix C/D 与 §6 只支持作者模型和任务，不证明任意 LLM 可无损接收该表示。兼容性、延迟或跨域 grounding 回归时，应回退普通 ViT+projector，或为目标模型保留独立 adapter。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-15300:end -->

### 视觉 Contrastive 校准应由不确定性按 Token 启用

<!-- semantic-body-binding:SF-2026-ARXIV-2605-23344:start -->
对所有视觉 token 统一增加对比干预，在 grounding 普遍不足时实现简单，却会同时扰动已经稳定的表示。更窄的分支先以 token-level uncertainty 找到候选位置，再施加局部视觉扰动并比较分支，只把它作为 representation calibration proposal；grounding 与任务 evaluation 才拥有接受权。

选择性干预减少无效计算，但会继承 uncertainty sensor 的偏差，并可能因扰动构造错误而强化伪相关。作者实验只支持披露模型和任务，不能证明该分数是普遍可靠的 epistemic uncertainty；校准漂移、grounding 回归或额外成本不合算时，应回退原始 decode 或不启用 contrastive branch。arXiv:2605.23344v1
<!-- semantic-body-binding:SF-2026-ARXIV-2605-23344:end -->

## Review notes

- `SF-2026-ARXIV-2605-07568`（Status: Experimental）：[exact-v1](https://arxiv.org/html/2605.07568v1) 支持逐层 Arrow-of-Time probe 定位 encoder/projector/LLM bottleneck；16-frame 与作者 temporal benchmarks 不证明可解码信号具有因果作用、通用视频理解或生产收益。

- Google Agentic Video（官方机制说明）：https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-agentic-video-in-gemini/ — 首发How it works支持query-conditioned时间/帧率/模态读取；不采用缺完整可复算合同的通用token、价格或准确率headline。后续开发指南只用于核验读取上下文与计账边界，不把新型号倒填首发。

- `SF-2026-ARXIV-2606-22565` — primary `arXiv:2606.22565v1`；Method=`arXiv:2606.22565v1 §2 Problem Formulation; §3 Strengths and Pitfalls; §4 Shallow Visual Reflection`；Evaluation=`arXiv:2606.22565v1 §5 Experiments`；Non-proof=`arXiv:2606.22565v1 §Limitations`；Artifact=`Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review`。

- VoxZip（transcript-anchored temporal audio KV compression；Status: Experimental）: https://arxiv.org/abs/2608.08569

本章仅吸收完成全文审计的机制证据。LongCat-Next 支持“分层离散 codec + shared AR backbone + modality-specific reconstruction”的受限案例，但不支持离散表示普遍优于连续 feature；Unified Latents 支持 rate、base-model capacity 与 decoder cost 联合选择，但其 artifact、公开数据与端到端成本证据不完整；OmniSIFT 支持 modality-role-aware compression 的受限分支，不支持视觉拥有普遍 truth authority。native multimodal scaling 工作只支持其论文 data/compute contract。厂商 benchmark 不进入通用结论。

- LongCat-Next / DiNA: https://arxiv.org/abs/2603.27538
- Unified Latents: https://arxiv.org/abs/2602.17270
- OmniSIFT: https://arxiv.org/abs/2602.04804
- MRUF（task contribution 与 sample-specific reliability 分离；Status: Experimental）：
  https://arxiv.org/abs/2607.10599v1
- Scaling Native Multimodal Pre-Training From Scratch: https://arxiv.org/abs/2607.22043
  - 证据边界：exact v1 支持其 decoder-only MoE、71M–3B activated-parameter 与披露 token budget 下的 modality-specific scaling/Pareto 现象；硬件、精度、完整数据 provenance 未披露，不能外推为通用 allocation law。
- Qwen-Image 2.0 Technical Report：详见 `papers/2026/weekly/2026-W20/README.md` 的 event-time Source Review。
- OneVision-Encoder（codec-guided sparse decoded-RGB tokens；Status: Experimental）:
  https://arxiv.org/abs/2602.08683
- CoPE-VideoLM（compressed-domain delta tokens；Status: Experimental）:
  https://arxiv.org/abs/2602.13191

### Daily Books delta trace（2026-06—08）

<!-- daily-books-trace:SF-2026-ARXIV-2607-24794:start -->
- `SF-2026-ARXIV-2607-24794` — Daily [2026-07-29](../../papers/2026/07/29/README.md)；primary [arXiv:2607.24794v1](https://arxiv.org/html/2607.24794v1)。

  **已吸收的语义增量：** 固定长视频帧预算从全局相似度排序演进为 query temporal granularity 与 event coverage 联合分配；selector 只提出 evidence route，不拥有事实，解析或覆盖不可靠时回退 uniform/static sampling 或 dense frames。
<!-- daily-books-trace:SF-2026-ARXIV-2607-24794:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-25669:start -->
- `SF-2026-ARXIV-2607-25669` — Daily [2026-07-29](../../papers/2026/07/29/README.md)；primary [arXiv:2607.25669v1](https://arxiv.org/html/2607.25669v1)。

  **已吸收的语义增量：** 固定全局 token budget 被拆为 query-conditioned intermodal allocation 与 content/redundancy-conditioned intramodal allocation；总量和模态下限保持可审计，上层路由失效时回退固定配比或完整 tokens。
<!-- daily-books-trace:SF-2026-ARXIV-2607-25669:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-10599:start -->
- `SF-2026-ARXIV-2607-10599` — Daily `2026-07-13`；primary `arXiv:2607.10599v1`；Books review `books-review:SF-2026-ARXIV-2607-10599`。

  **已吸收的语义增量：** 新增证据边界：Separate task contribution from observation reliability: a contribution router is supervised by leave-one-out task degradation, while a distinct uncertainty head predicts modality-wise log variance and inverse-variance weights calibrate the final fusion gate. 该 delta 已进入 `books/part-03-multimodal-world-models/23-multimodal-representation.md#L175`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-10599:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-22043:start -->
- `SF-2026-ARXIV-2607-22043` — Daily `2026-07-27`；primary `arXiv:2607.22043v1`；Books review `books-review:SF-2026-ARXIV-2607-22043`。

  **已吸收的语义增量：** 新增证据边界：Native multimodal pretraining turns shared capacity allocation into a multi-objective Pareto decision because text and multimodal losses prefer different parameter and token budgets. 该 delta 已进入 `books/part-03-multimodal-world-models/23-multimodal-representation.md#L69`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-22043:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2608-08569:start -->
- `SF-2026-ARXIV-2608-08569` — Daily `2026-08-10`；primary `arXiv:2608.08569v1`；Books review `books-review:SF-2026-ARXIV-2608-08569`。

  **已吸收的语义增量：** VoxZip 先用 ASR transcript 作为 semantic anchor 对齐并融合 audio tokens，再以时间衰减 accumulated attention 做动态淘汰。Qwen3-Omni 六个 audio benchmark 支持作者范围内的压缩结论；ASR 错误、跨语言语音和实时 streaming 的累积偏差仍是 failure boundary。
<!-- daily-books-trace:SF-2026-ARXIV-2608-08569:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2605-01345:start -->
- `SF-2026-ARXIV-2605-01345` — Daily `2026-05-05`；primary `arXiv:2605.01345v1`；Books review `books-review:SF-2026-ARXIV-2605-01345`。

  **写回边界：** 固定视觉 token 选择扩展为按未决 claim 主动获取 crop 的受限分支；selector 只提出 observation proposal，evidence assembler 与 answer gate 保留充分性和提交权，开放世界覆盖与实时 SLO 未被证明。
<!-- daily-books-trace:SF-2026-ARXIV-2605-01345:end -->
