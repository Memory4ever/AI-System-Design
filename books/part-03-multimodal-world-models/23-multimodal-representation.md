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

## 连续表示、离散表示与混合表示

### 连续表示

连续 feature 保留较丰富的局部信息，适合理解、检索和精细感知；但它缺少天然离散 vocabulary，生成端通常需要独立 decoder，且不同 encoder 的 feature geometry 不可直接互换。

### 离散表示

离散 codes 可共享 categorical prediction objective，也适合缓存、传输和自回归生成。代价是 codebook collapse、rare-code mismatch、长序列和重建误差。一个 code 是否“语义化”必须由 intervention、retrieval 或 reconstruction evidence 支持，不能从可视化聚类直接推断。

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

### Rate、distortion 与下游容量必须联合选择

表示压缩率不能只由 latent channel 数或 reconstruction score 决定。若 latent 保留更多 information，下游 prior 或生成模型需要更大容量与更多 compute 才能拟合；若压得更狠，base model 的工作变轻，detail reconstruction 和 stochastic completion 的负担却转移给 decoder。于是系统 optimum 是联合问题：

```text
representation rate
<-> reconstruction distortion
<-> downstream model capacity
<-> decoder training and inference cost
```

这条路线从固定 spatial/channel bottleneck，演进到可度量的 rate，再到按 base-model capacity 选择 operating point。它没有否定传统 VAE、discrete codec 或 pixel-space model：低 latency、已有稳定 artifact、固定视觉域或需要明确 codebook identity 时，旧方案仍更合理。论文中排除 codec training 或 decoder sampling 的 FLOPs，不能被写成端到端系统更便宜。

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

理解与生成也不必被迫共享全部参数。Fully native unified model 统一 objective 和 runtime 接口，却要求从头
解决跨 modality interference；post-hoc ensemble 可独立升级组件，却产生碎片化 conditioning。中间路线复用
成熟 understanding backbone，以其 hidden state 作为 semantic interface，再挂接独立 visual generation head，
并通过分阶段冻结/解冻与 loss ratio 管理能力冲突。InternVL-U 是这一 modular hybrid 的受限案例；它说明
“共享语义接口、保留专用生成路径”是可行分支，不证明其 benchmark 排名或具体 loss 比例具有通用性。
该路线用较低重训风险换双 compute path、interface drift 与 checkpoint coupling；数据和预算允许真正 joint
pretraining 时 native path 仍可能更合适，需要独立升级生成器时 large ensemble 也继续成立。

fusion 之后仍要决定不同 modality 如何竞争有限 token budget。均匀或对称 compression 最容易实现，但默认各模态拥有相同 information role；当视觉承担事件定位、音频承担补充语义时，可以让视觉 anchors 条件化音频 selection。反过来，在 ASR、音乐或遮挡场景中，audio-first 或 full-token branch 仍可能更可靠。**方向性 compression 是受任务 truth authority 约束的 policy，不是“视觉永远更重要”的架构事实。**它还需要对 modality conflict、selector drift、chunk boundary 与 abstention 做显式验证。

## 对齐不是把向量拉近这么简单

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

### Codec-aware tokenization：稀疏性可以在视觉 Encoder 之前暴露

逐 frame 解码为 dense RGB patches 是最通用的旧方案：模型不依赖某种压缩格式，也能统一处理静态图像、
视频和编辑后的像素。长视频中它会重复编码大量相似内容。Codec-aware 路线至少有两条不同分支：

```text
decoded RGB frames
→ use codec motion/residual metadata to select sparse RGB patches

compressed video primitives
→ encode key frames plus motion/residual delta tokens directly
```

前者仍把选中区域解码为 RGB，兼容已有 vision encoder，却可能漏掉 codec metadata 未显著标记的语义变化；
后者减少重复 decode/encode work，却把 codec、GOP、motion vector、residual layout 与 tokenizer 一起变成模型
输入协议。Transcoding、随机 seek、corrupted stream、不同 codec/profile 与 frame-rate conversion 都可能改变
token identity。Dense frames 在格式多样、证据完整性优先或 codec path 不可信时仍成立。

因此“视觉 token 更少”只证明 representation rate 改变，不自动证明 TTFT、KV capacity 或 end-to-end latency
按比例下降。评估必须绑定 source codec、resolution、duration、sampling/GOP、model、hardware、precision、
batch/concurrency 与 SLO，并分别测 retained evidence、encode cost 和 downstream outcome。

## Failure modes

### Representation collision

不同 modality 或不同 codebook version 产生相同 ID，却被错误共享 embedding。解决方式不是只增加一个 type embedding，还要校验 artifact identity。

### Modality domination

数据量、loss scale 或序列长度更大的 modality 主导训练，模型看似统一，实际弱化其他能力。

### Temporal aliasing

低 frame rate 或不一致采样把不同运动映射成相似 token，后续 world model 无法恢复丢失动态。

### Train/inference mismatch

训练数据只包含高概率 codec path，生成时 rare code 或累计量化误差使 decoder 离开训练分布。过滤低置信序列可以缓解崩溃，也可能删除稀有但有效样本。

### Connector shortcut

模型依赖 caption、layout 或 metadata shortcut，而没有真正消费目标 modality。需要遮蔽、反事实和跨分布测试，而非只看平均分。

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

## 本章在知识树中的位置

Part II 给出通用 Transformer 组件；本章把单一文本 token 扩展为跨模态 representation contract。第24章进一步比较这些表示如何生成与修正；第25章要求表示支持 action-conditioned dynamics；第26章把 timestamp、coordinate 和 action schema 放进物理闭环。

训练数据、配比与 objective 归 `TRAIN-DATA` 和 `TRAIN-PRETRAINING`；线上 modality batching 与 KV 归 Part V；benchmark contract 归 `PLATFORM-EVALUATION-SYSTEM`。一个机制只有一个 owner，其他章节只消费接口。

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

## Review notes

本章仅吸收完成全文审计的机制证据。LongCat-Next 支持“分层离散 codec + shared AR backbone + modality-specific reconstruction”的受限案例，但不支持离散表示普遍优于连续 feature；Unified Latents 支持 rate、base-model capacity 与 decoder cost 联合选择，但其 artifact、公开数据与端到端成本证据不完整；OmniSIFT 支持 modality-role-aware compression 的受限分支，不支持视觉拥有普遍 truth authority。native multimodal scaling 工作只支持其论文 data/compute contract。厂商 benchmark 不进入通用结论。

- LongCat-Next / DiNA: https://arxiv.org/abs/2603.27538
- Unified Latents: https://arxiv.org/abs/2602.17270
- OmniSIFT: https://arxiv.org/abs/2602.04804
- Scaling Native Multimodal Pre-Training From Scratch: https://arxiv.org/abs/2607.22043
- Qwen-Image 2.0 Technical Report：详见 `papers/2026/weekly/2026-W20/README.md` 的 event-time Source Review。
- OneVision-Encoder（codec-guided sparse decoded-RGB tokens；Status: Experimental）:
  https://arxiv.org/abs/2602.08683
- CoPE-VideoLM（compressed-domain delta tokens；Status: Experimental）:
  https://arxiv.org/abs/2602.13191
