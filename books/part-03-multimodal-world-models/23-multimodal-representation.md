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

因此，最终回答错误不能直接归因于“视觉 encoder 没看见”。可以先固定 encoder，用浅层 probe 检查细节是否仍可读，再分别检查融合后的语言侧是否能访问这些信息、输出协议是否能表达它们；可恢复、可访问和可表达是三种不同能力。受限网格实验中，同样数量的 patch 可保留浅层读出所需信息，而完整模型仍无法正确输出，网格密度、对象跨 patch 边界及 readout 容量也会改变结果。它支持分段定位接口瓶颈，不唯一证明 projector 压缩、对齐或蒸馏造成失败。<!-- source-family:SF-2026-ARXIV-2604-09687 -->

新增 probe 要支付监督、训练和容量成本，也不能证明原模型已经能自行调用被读出的特征。[Grid2Matrix](https://arxiv.org/html/2604.09687v1) 的冻结 encoder、合成网格、cell/整图准确率与浅层读出仅限定这条诊断分支，不是通用视觉能力证明。细粒度坐标或结构化输出确实重要时，可比较专用 readout、显式坐标接口与原语言输出，并对最终任务重新验收；通用语义任务、诊断数据不具代表性或接口成本过高时，成熟 encoder + projector 仍合理，不能用一个 probe 结果否定它。

视觉配置本身也是诊断变量：动态 tile/grid 的离散选择可能使相邻一像素的 resize 改变完整处理配置，而不是只改变一点图像内容。回归应分别控制“同 pixels 换配置”和“同配置换 pixels”，保存 preprocess/grid identity，再看原任务的证据访问与答案；答案更稳定不等更正确，不能把配置效应直接归因于 encoder 丢失信息。局部 target knockout 配合相同数量 non-target 删除，可检验所测路径是否依赖目标 view，但不能识别所有模型共同的内部原因。

[Reading Right, Answering Wrong 的受限对照](https://arxiv.org/html/2609.25770v1)支持这组边界测试；累计多条件、annotation-assisted reading 的可读分母不是全部任务自主成功，固定低/高分辨率也令部分模型 accuracy 退步。额外图像 tokens、标注与多次调用均有成本，模型/样本/多比较范围须保留。配置不稳定或目标 cue 不可取得时，回读完整原图/原文、保留 native preprocessing 与独立任务质量 Gate，不把 guided recovery 作为通用修复保证。<!-- source-family:SF-2026-ARXIV-2609-25770 -->

持续接入新任务时，还应把感知接口漂移与语言参数累积拆开处理。共享 projector 成本低、身份简单；任务差异较大时，可以保留各任务 projector，由冻结视觉特征的任务原型对查询加权，混合的是各 projector 的输出，而不是直接平均它们的参数。语言侧则可在固定层输入与任务 LoRA delta 的局部二次目标下，累积输入二阶统计、合并参数增量。前者决定当前样本从哪个感知接口取信息，后者决定历史任务约束如何进入语言层更新；两套状态不能由一个相似度分数代管。<!-- source-family:SF-2026-ARXIV-2604-14016 -->

[受限递归合并实现](https://arxiv.org/html/2604.14016v1)的代数等价依赖固定特征、固定任务增量及可逆的完整统计矩阵，不能推出全网络最优或无遗忘；缩放、低秩截断和后续特征变化都须重新验收。该分支仍需要逐任务调优、保存 projector/原型及二阶统计，完整统计还可能有平方级存储成本。LLaVA-1.5 与 InternVL 的有限 continual-learning 对照并非各任务全面占优。任务差异小或状态预算不足时继续共享 projector，语言侧也可保留独立 adapter 或 replay；采用合并后须分别检查旧任务、新任务与接口版本，不把局部合并公式当端到端能力保证。

若新增模态需要 backbone 内部的适配容量，却必须继续复用旧 embedding 与索引，冻结原权重或把新残差初始化为零还不足以保证旧路径长期不变：训练后新残差可以非零。一个更强但有条件的接口是按模态封装深层 adapter pack，所有 gate 关闭时，hook 在任何 adapter 算术之前直接返回原计算图；单 pack 开启时，其他 pack 不参与该 forward。bitwise 保留还要求原 weights、precision、kernel、运算顺序与 batch 配置一致，而非仅要求最终张量形状相同。gate 绑定的是 encode 入口声明的执行 scope；同样的 RGB 字节可以承载 thermal 输入，不能靠内容自动识别其语义，梯度 checkpoint 的 backward 重算也须恢复相同 scope。

[Modality-Gated Deep Adapters 的有限实验](https://arxiv.org/html/2609.26182v1)支持这种明确绕过的接口，而不是所有输入的自动路由或任意混合模态保证。closed-gate 检查每模态仅一个输入，多 gate 同一 forward 与并发请求隔离未得到验证；单一 backbone 的 audio/thermal 训练又含参数量、loss 和筛选差异，gate-open 的 thermal 分类仍低于原基线。新 pack 要支付驻留内存、训练、入口管理与 scope 回归成本。多模态混合、重算或并发 scope 无法可靠隔离时，应保留 external projector、独立 adapter/model 或原编码路径；旧图精确保留与新模态任务质量是两项独立验收。<!-- source-family:SF-2026-ARXIV-2609-26182 -->

语音理解还可以把“对齐到语言空间”与“显式提供音素/词界接口”分开。在配对语音—文本监督充足时，连续projector保留更多声学信息，也能复用成熟encoder；监督受限时，冻结encoder输出的显式音素序列可以让LLM先消费一个更接近语言符号的接口，而不再只靠少量数据训练连续映射。多个音素候选可保留识别歧义，却也增加输入长度和选择成本；它不是完整声学表示，更不能代替音色、韵律或环境音。<!-- source-family:SF-2026-ARXIV-2604-09332 -->

[受限接口对照](https://arxiv.org/html/2604.09332v1)在同一冻结Whistle encoder、20小时Tatar配对数据下观察到这一分支；该encoder预训练已经含Tatar，不能称为从未见语言的泛化。英语对照的encoder训练recipe不同，也不能把所有收益归因接口。音素BPE序列甚至从113增至125tokens，词界与接口适配可能比序列缩短更重要；词表扩大也会退步。于是选择须同时验收识别误差、语言覆盖、配对监督和下游WER，数据充足或任务需要非语言声学细节时继续保留连续projector，不能把音素路线升级为所有低资源模态的默认答案。

### 阶段三：共享 token space

系统开始把图像、视频或音频压缩为离散 codes，与文本 ID 一起交给共享 autoregressive backbone。它的吸引力是统一 objective 与生成接口：所有 modality 都可以表示成“预测下一个 ID”。

但离散化不会免费发生。codebook size、层数和 stride 决定序列长度与 fidelity；quantization error 会进入训练分布；codec 与 backbone 版本不一致时，同一 ID 可能不再代表同一信号。统一协议减少模型接口数量，却增加 codebook governance。

共享 codes 还要决定保留的是像素重构还是理解语义。若每次生成视觉中间状态都先渲染成图，再交给视觉 encoder 读取，接口直观且方便人工检查，却把渲染误差和重复编码带入推理。一条条件分支以已有理解模型的行为为约束训练语义 quantizer，由生成分支预测这些 codes，再由理解分支重新处理并写入自己的 KV；像素 decoder 独立训练，只在需要可视化或像素评价时调用。省去像素往返不等于省去重新计算，也不能把生成分支的 KV 直接冒充理解状态。

这种选择用低层细节和 decoder 独立性的代价换取语义中间状态复用，还可能继承原理解模型的盲点。[LatentUM 的受限案例](https://arxiv.org/html/2604.02097v1#S3)支持 InternVL3.5-4B 路线中的表示消融、图像生成与视觉规划；它的 action-conditioned recurrent rollout 仍先渲染、再编码下一帧，不能称为已经实现全 latent World Model。细节保真优先、需要独立感知验证或闭环接口仍依赖像素时，保留独立 encoder/decoder 更合适。

<!-- source-family:SF-2026-ARXIV-2604-02097 -->

### 阶段四：native multimodal representation

更进一步的设计不再把非文本输入视为语言模型外挂，而是在 pretraining 中共同学习 modality representation、cross-modal relation 与生成能力。这里的 “native” 应指训练 contract 发生变化，而不是 marketing 标签：多模态数据从一开始就参与 backbone 表示形成，loss、sampling ratio、sequence packing 与 router load 都共同决定能力。

它不必然优于 staged alignment。若高质量多模态数据不足、codec 尚不稳定或只需要专用理解能力，冻结 encoder + projector 更容易训练、验证和回滚。

没有专用连续 encoder，也不意味着感知计算消失了：它可能在共同 backbone 内逐层形成可读表示。这里应分别测试表示 formation、后续 readout 和跨模态 routing，而不是凭某层线性 probe 或几何相似就把它命名为完整 encoder。对固定任务/层/模态的扰动，可检查该局部表示是否为所测输出所需；necessary readout 与足以替代全部感知计算、删 token 或提前退出仍是不同命题。

[Virtual Encoders 的精确 v2 证据](https://arxiv.org/html/2609.26513v2)含有限 concept probe 与两个模型的单层 Gaussian 扰动、特定 yes/no 判定；没有 activation patching 的充分性验证，PCA 子空间定义也未证明 rotation 的因果作用。新增 probe、干预强度与多重比较有成本，音频/其他模型上的相关观察不能外推共同层号或部署可省计算。证据不支持时保持功能解释的 Unknown，继续 dedicated encoder + projector、完整视觉读路径和独立任务回归，不让 native 标签代替分段验收。<!-- source-family:SF-2026-ARXIV-2609-26513 -->

复用生成式 backbone 做**理解/检索表示**还有一条条件分支：不能只把 causal attention 放开成双向，就假定原有 next-token objective 已学到适合全句比较的几何。先用 masked-token 目标适配双向读取，再用成对对比目标校准 embedding，才使 attention 形态、训练目标和下游表示用途一致；把视觉/语音 specialist 的权重或 head 接入同一 backbone 也必须逐模态验收。它节省从零训练 encoder 的成本，却可能遗忘原有语言、代码或其他能力，权重合并和多域数据只是需配对测试的缓解分支，不是固定比例的通用配方。只需生成时保留 causal 模型更简单；需要跨模态检索时则须同时检查表示质量和原能力回归。现有实验仅覆盖作者的小型 backbone 与所测 embedding/多模态任务，不能推出大模型或生产检索的普适增益。<!-- source-family:SF-2026-ARXIV-2604-02045 -->

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

同一 codebook 还承担不同优化职责：encoder 的 straight-through reconstruction/commitment 更新，不等于 code 向当前 feature 分布追踪。一个稳定训练分支按相对 assignment distance 停止梯度地缩放 STE，在有限窗口保存近期 active features、为近邻 inactive codes 提出追踪 target，并分别调 encoder/decoder 的 warmup–anneal 与 codebook 学习率。稀有 code 获得候选目标、共享投影受影响，都不等每个原 code 每步得到非零独立梯度；没有获得目标的 inactive code 可以只有零 self-target loss。

[StableVQ 的受限图像实验](https://arxiv.org/html/2609.26774v1)中组件单独仍有 NaN/低利用率，Eq 4 最匹配距离为零的数值 guard 未披露，不能称 threshold-free 完整稳定实现。不同 projector/epochs 的比较未全匹配预算，满 usage 也不保证语义或生成质量，IS/Precision 仍有反退。窗口、近邻搜索与分组优化增加训练成本；数值/质量验收失败时保留普通 VQ、EMA/reset、统一 optimizer 或连续 feature，不把 codebook 利用率升级为音频、视频或部署安全保证。<!-- source-family:SF-2026-ARXIV-2609-26774 -->

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


### 参考音色与目标事件时间轴不应共享默认控制权

完整参考音频携带音色，也携带自己的时间顺序；若目标只复用音色，事件发生时刻却由画面决定，将两路条件不加区分地注入会引入竞争。一个视频配音分支让参考路径减少位置/局部时间编码、另提供全局 timbre，画面路径继续保留目标逐帧同步身份。这里不是宣称音频已“无时间”，而是选择允许各通道控制什么：style proposal 不能自动取得目标时间轴的控制权，生成器怎样融合条件仍由下一章承接。

选择性抑制会连带丢失有用声学关系，并增加两路 encoder、训练、融合与校准成本。`arXiv:2604.15086v1` 的 ControlFoley 双条件消融支持受测组合选择，但 Table9 没有单独识别时间抑制模块的因果收益，部分 L0 切片 CLIP-only 更好；小规模主观评价也不证明统计独立、普适同步质量或线上 SLO。只需复制整段声音、两个来源本来同步或额外条件失配时，完整音频/单路表示仍合理；跨域使用应分别验音色保真、事件同步和失败切片，而非只以总分批准该分工。

<!-- source-family:SF-2026-ARXIV-2604-15086 -->

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

但 semantic 与 acoustic 的分责不能直接沿“音素是内容、音高只是声音风格”切开。在声调语言中，跨帧音高轨迹本身可以区分词义；连续 SSL features 已可读出的 lexical tone，经过逐帧离散化后仍可能被音素主导的聚类压掉。因而小词表与说话人不变性是合理旧目标，却不能替代内容保持验收：应分别检查 phone 与 tone，并检查帧序列、音素时间对齐及量化前后的信息损失，而不凭重构或单一内容指标宣布 semantic token 已保真。

条件允许时，可先量化较粗的 phone-level 表示，再对减去该 centroid 的逐帧残差建立另一 codebook，把部分声调变化留在残差路径；这会增加 alignment、双码本和时序处理成本，也不保证两层已经干净分离语义与声学。[Lexical Tone 的 exact-v1](https://arxiv.org/html/2604.07467v1) 只在 Mandarin/Yorùbá 的 HuBERT features 与元音对齐 probes 中支持这一受限分支；探测对象是 code vectors，不是端到端生成质量，且 mean pooling、RVQ 与 residual clustering 并非处处同益或等 bitrate。无需声调区分、对齐不可得或低延迟优先时，常规逐帧量化仍可保留；需要更完整音高轨迹时，应比较连续 feature 或更高容量表示，不假定提高词表就能自动补回跨帧关系。<!-- source-family:SF-2026-ARXIV-2604-07467 -->


训练责任也是 codec 身份的一部分。部署后减少 latent channels 或过滤已训练的 latent，实现简单，却让原 decoder 消费它未适配过的表示；另一条分支在训练时对 latent 做三维 wavelet 分解，固定保留部分频带，置零其余频带，再逆变换交给 learned decoder。这样 encoder、频带支持与 decoder 共同适配压缩后的信息通道；它不是把“低频”直接认作语义，也不能只凭存储量等价就与少 channel 的 codec 互换。<!-- source-family:SF-2026-ARXIV-2604-16479 -->

[受限视频 VAE 对照](https://arxiv.org/html/2604.16479v1)的 Eq5 保留四组而非只保留 LLL；部分 WebVid 重建 rFVD 和 Sky/UCF 生成 FVD 仍低于基线表现。因此频带选择、decoder 训练与下游生成应联合验收，不能从 PSNR 或高频能量推断生成质量必然改善。额外 VAE/prior 训练和分解、逆变换成本都须计入总账；无法重训、细节保真优先或频带策略不适配时，原 codec、更完整 latent 与已验证的部署后压缩继续合理。

#### Codebook Capacity 也可以随位置递增

uniform codebook 让每个视觉 token 使用相同容量，编码、部署和兼容最简单；当序列按 coarse-to-fine 顺序增长时，累计容量可能在早期就跨过数据 uncertainty，后续位置难以继续形成层级。position-indexed schedule 先给早期 token 较小 codebook 表达粗语义，再逐步扩展后续容量承载细节；`position/order/N/K` 因而都进入 representation artifact identity，而不是只记录全局 bitrate。

递增容量可延长层级形成区间，却增加多 codebook 治理、kernel/layout 与训练不均衡，也依赖稳定的顺序语义。序列没有 coarse-to-fine 结构、兼容优先或收益不足时，uniform codebook 仍更合适。`arXiv:2605.06207v1` 只在 ImageNet 256 与作者 tokenizer/AR 设置中验证；entropy-cliff 阈值依赖数据、长度与 codebook，不能外推语言或其他视觉表示。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-06207 -->

### Representation Artifact 必须携带分辨率与下游容量合同

只按 reconstruction 选择视觉 tokenizer，在 decoder 足够大、下游任务接近像素重建时是合理起点；生成 prior 容量有限时，更高保真的 latent 反而可能更难建模。Artifact identity 应同时绑定 native-resolution/aspect-ratio policy、compression ratio、latent channels、decoder capacity 和 loss revision，再在 matched generator capacity 下比较 rate–distortion–generation Pareto frontier。

这会扩大联合搜索空间和训练成本，也不能从重建分数推出语义生成质量。固定分辨率、成熟 CNN tokenizer 或低成本部署仍可保留；generator、decoder 或数据分布变化后必须重新验收。现有 exact-v1 只支持作者的视觉 tokenizer、模型容量与任务，不给出通用最优压缩率。<!-- semantic-body-binding:SF-2026-ARXIV-2605-05331 -->

表示层选择固定后再训练decoder，在融合接口稳定、预算紧时最直接；但像素重建偏好的层组合未必是生成器最容易建模的latent。另一条训练分支不搜索单一固定gate，而对同shape的frozen encoder层表示随机取非空子集、按保留层数求mean，让decoder适应不同composition；每个输入上的期望仍为全部层mean。它扰动的是层间disagreement，不证明每次抽样都保留全部信息、encoder更便宜或非线性decoded output不变，layer normalization/集合/归一化和部署fullmean必须同属representation身份。

[随机融合的受限证据](https://arxiv.org/html/2609.31620v1)进一步区分subset→pixels的decoder训练，与noisy subset→固定fulllatent target的DiT训练，两者不应共享默认最佳drop rate。固定generator及同一批sampledlatents只更换decoder，可隔离readout改变；joint训练则必须分别比较两条轴和最终质量。线性平方loss下的disagreement惩罚不是完整感知/GAN或guidedtrajectory保证；有限图像实验有native重建退步、guided中间率反退及大generator的FID/IS偏好分离。随机训练、保存多层feature和rate搜索仍有费用，其他层级/分辨率未验收时保留固定fusion/原decoder及已验证codec，不把robustness称为全场景或免费收益。<!-- source-family:SF-2026-ARXIV-2609-31620 -->

## Fusion：在哪里让模态相遇

### Early fusion

不同 modality 在 backbone 前或浅层合成一个 sequence。优势是 cross-modal interaction 充分；代价是序列更长、attention 成本更高，且强势 modality 可能支配梯度和位置预算。

### Late fusion

各 modality 独立编码，在 prediction head 或决策层融合。它保留专用模型能力和故障隔离，适合低耦合任务；但细粒度 token-region、word-frame 对齐难以形成。

### Cross-attention fusion

一种 modality 作为 queries，另一种提供 keys/values。它可以控制 interaction direction 和计算量，也把 connector capacity、query count 与 synchronization 变成显式瓶颈。

### Shared self-attention

所有 tokens 进入同一 self-attention graph。计算接口最统一，但必须明确 attention mask、position system、modality type、packing boundary 和 loss mask。没有这些元数据，同一个 sequence 中的相邻 token 可能只是打包邻居，而非语义邻居。

同一个 compact token index 未必还代表同一空间位置。多通道图像按 channel 分开 spatial attention、再在对应位置跨 channel 交互，可以减少联合 attention 的规模；但独立 patch masks 会使各 channel 留下不同位置，直接按压缩后的索引对齐就破坏了这个接口。一条训练侧分支保留原 grid coordinates，在等数量可见 patches 间用一对一最小平方距离 assignment 建立共同索引；多 channel 通过一个 reference 分别配对，把 joint 问题改成 star cost。它精确求解的是这一受限成本，不是所有 channel 间的联合最优，更不等于语义对象已匹配。

reference 随样本随机化能平衡各 channel 的对应误差，却不降低整体平均位移；共享 mask 虽保持精确位置对应，又减少独立遮罩的多样性。有限 ViT-S 与六项分类/分割任务的对照显示，单独降低平均距离不足以解释收益，重遮罩时共享方案也趋近；不能把它推广成所有 fusion 的质量定律。平方距离目标本身不保证每个共同保留 patch 都匹配自身，故不继承原文该普遍断言。assignment、坐标与 mask 身份维护增加训练成本，本文未给生产 latency/SLO；几何条件不成立、求解成本过高或收益不足时，保留共享 mask、固定遍历或完整联合 attention，并另验匹配误差与下游任务。 [必要机制与反证](https://arxiv.org/html/2609.21629v1)。<!-- source-family:SF-2026-ARXIV-2609-21629 -->

选择 fusion point 的稳定原则是：**越早融合，跨模态联合建模越强，隔离与可控性越弱；越晚融合，专用能力和治理越清楚，细粒度交互越受限。**

这并非“早融合总是更好”的排名。冻结视觉编码器、只在末端接入文本，保留通用视觉特征且易复用，却可能来不及改变 patch 层对细粒度目标的表征；在视觉中间层插入门控 cross-attention，则让文本作为条件影响视觉特征形成，而不是只对已完成的图像特征做选择。门从零初始化可先保留原视觉路径，再逐步学习条件化，但共享表示变成 prompt-dependent，缓存身份必须包含文本、adapter/gate revision；还要分别测 query steerability 与原视觉任务的保持，而不能只看一个多模态总分。

早层注入需要额外 adapter、训练和更复杂的特征治理。`arXiv:2604.02327v1` 的冻结 ViT 对照中，早融合提高了所测细粒度文本引导任务，却在一项通用视觉分类 probe 低于晚融合；这些受限结果不证明任意视觉 backbone、prompt 或下游任务都应早融合。单模态保真、独立升级与低耦合优先时，晚融合仍是合理旧路径。<!-- source-family:SF-2026-ARXIV-2604-02327 -->

融合点之外，还要核实际可见的模态集合。独立视觉与文本 encoder 保留专用特征，decoder 可用同一个 query 分别 cross-read 两组状态，再形成联合检索表示；但若训练始终附有 caption，无 caption 时的视觉支路仍可能塌缩。一条受限训练分支把单模态读出的 embedding 随机混入联合表示，并按比例删除 caption，使同一对比目标同时覆盖完整输入与缺模态输入。这是训练支持的改变，不是部署时临时删一路特征的无成本修补。<!-- source-family:SF-2026-ARXIV-2604-21326 -->

该分支增加多次表示计算、caption 比例、mixin 与负例构造的校准成本；过强混入或缺 caption 也可能损害文本—视觉语义桥。T5/CLIP 与两个改造数据集的受限消融包含纯文本切片退步，近邻重叠不等答案支持或概念真值。模态集合稳定、专用特征隔离优先时，原独立编码/晚融合仍合理；缺失模式超出训练支持时，应重新验收或回退单模态路径。检索排序及索引执行仍由第76章接手，不把表示对齐直接写成线上召回保证。

融合后的信息还可能在“示例内建立对应”与“对新 query 应用对应”之间断开。多模态 ICL 中，示例 label 对图像区域的中层 grounding，与 query 最后一个 token 读取这些示例的路径是两个对象；最终答错不能直接证明示例未被识别。一个受限补救先用示例 label 的图像 attention 熵选择中层，再把该层的区域分配注入后层 query attention，按系数混合并重新归一化。它改变的是已形成表示的访问路径，不是重新证明图像事实。<!-- source-family:SF-2026-ARXIV-2604-13403 -->

这条路径需要保存或重读 attention、选择层和调混合系数；低熵不保证正确 grounding，均匀化 attention 的退步也不能定位唯一因果来源。[作者的四模型、4-shot 对照](https://arxiv.org/html/2604.13403v1)只有受限收益和持平项，不能承诺所有任务都改善。因而应分别验收示例对应与 query 应用，信号不稳时保留直接读取原示例的基线；表示诊断在本章负责，最终任务正确性由第66章的评价合同接手。

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

零初始化还只保证起点，不保证训练后的表示兼容。向既有视频 self-attention 增加文本 cross-attention 时，新分支的输出投影置零可以保持第一轮 forward；后续更新仍取决于 Q 与 K/V 从哪一份状态产生。一条受限路线以 self-attention 后的视频状态产生新 Q，复用同层 self-attention 前文本状态的 K/V 投影与 tensor，而不是把 raw text 经另一套路径直接写入新分支。起始函数相同的两个实现，可能因此进入不同的训练轨迹。<!-- source-family:SF-2026-ARXIV-2604-16503 -->

[视频生成训练对照](https://arxiv.org/html/2604.16503v1)支持检查这项接口兼容，但相关消融同时改变 Q 与 K/V，不能把稳定性全归因于 K/V 或视为一般 manifold 定理。复用既有投影减少新增 K/V 投影工作，不等于 cross-attention 免费，也不保证更新后仍保持原函数；训练、质量回归与实际执行成本仍须验收。数据或预算不足时，冻结原路径、独立 adapter 或晚融合继续合理；需要更自由的条件化时可训练新投影，但不能用零初始化替代更新后的兼容测试。

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

同一个 selector 还可能在三个阶段看到不同信息：离线构造标签时用 gold response loss 搜索视觉 mask，训练 compressor 时用这些 mask 作监督，部署时再由不读取 gold response 的模型预测保留 token。因而构造输入、训练输入与部署输入必须分别记录，不能因为在线 selector 不访问答案，就称整个压缩流程没有特权标签或训练成本；gold loss 也只是所定义模型/回答目标下的选择信号，不是视觉证据充分性的真值。<!-- source-family:SF-2026-ARXIV-2604-17087 -->

搜索候选/代数、compressor 训练与线上 selector 需要分账，保留每个语义组至少一项也不能证明遗漏不会改变答案。原文相对 dense 的部分质量退步和不同搜索 loss 的反例要求同时验 selector、预算、内容覆盖与实际执行成本，不能把离线 mask 上界当部署收益。标签不可得、任务漂移或搜索成本不能摊销时，静态/attention selector 与 dense 回退仍合理；这里补的是同一接口跨阶段的信息责任，不取代后面的 modality/时间预算分配。<!-- source-family:SF-2026-ARXIV-2604-17087 -->

预算还与压缩发生在哪一层有关。对高 token-rate 语音，input tokens 保留声学细节，而中间层可能正在重组声学与词汇信息；深层相似度高不意味着从输入开始就能同等压缩。一个条件分支在输入端只合并严格相邻的相似 features，到较深层再允许稍宽的局部 lookback，以 mean pooling 保留分布式信息，而不是随机删 token。它改变的是表示粒度，不能把 ASR 恢复出相同文字当作音色、韵律、重叠说话人或非语音事件都无损。

压缩的层位置也改变收益：越早减少序列，越多后续计算能够省下；深层虽然最终 token 数更少，已执行的大部分 forward 无法回收，还要付 selector 成本。[Affinity Pooling 的受限证据](https://arxiv.org/html/2604.06871v1)在 Qwen2-Audio/Kimi-Audio 的语义任务中发现中层敏感、输入与深层两级合并较稳；H200 短音频的深层或双级路径却可能比原模型更慢，精细声学任务也未充分测量。层位置、lookback、阈值和任务质量因此应一起验收；需要完整声学信息、短输入或净时延不划算时，原始 token stream 与保守均匀采样仍合理。第45章接手存储后的 KV 生命周期，不把这里的 feature 合并视为精确 cache 复用。<!-- source-family:SF-2026-ARXIV-2604-06871 -->

合并规则也受 batch shape 约束。逐样本保留不同数量的 source tokens，虽能适应内容，却不便直接组成稠密 batch；一个矩阵合并分支对保留 mask 做 batch OR，只要任一样本需要某个 source 位置，整批就保留该位置，并取消它对应的融合列，避免重复计入。统一 shape 的代价是压缩率依赖 batch 组成，单样本的高压缩不能直接推算批量吞吐。<!-- source-family:SF-2026-ARXIV-2604-13432 -->

若后续生成层需要原空间网格，还须保存融合映射，把更新后的 destination 特征散布回 source 位置；恢复 shape 不等于逆转信息损失。相似度矩阵、映射状态和恢复算子都有成本，压缩应与下游网格 consumer 一起验收。[作者的视觉分类与生成对照](https://arxiv.org/html/2604.13432v1)采用不同模型、精度和 batch，部分配置牺牲质量，不能由局部算子收益推出通用端到端加速；精细空间任务、异质 batch 或恢复成本过高时，原始 token 路径仍合理。

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

预算还要分配到**哪一层删除信息**。在输入端一次性剪掉视觉 tokens，后续层就失去读取那些原始证据的机会；分阶段策略先在 segment/frame 内合并与选择，再让浅层融合保留一部分视觉信息，随后才在指定 decoder stages 继续剪枝。这是信息保留时间与计算量的另一取舍，而非只换一个重要性分数：selector、原始时间/空间位置对应、stage 与逐阶段保留数必须共同定义表示身份。受限视频实验的 input-only 对照劣于分阶段路径，支持晚一些删可能保留更多可用信息，但不证明某层已经完整、无损地转移了所有视觉内容。<!-- source-family:SF-2026-ARXIV-2604-01881 -->

阶段化增加选择、重排与执行复杂度，剪得太晚又支付了更多 Attention 计算；相似性、指令相关性与 DPP 多样性都只是保留代理，不是视觉事实的因果判据。所测 7B VideoLLM 与 A800 上的平均质量/算量不保证每个任务无损，更不是生产并发 SLO。稀有瞬时细节、模型层间信息流或问题类型不匹配时，应提高浅层保留预算、重读原视频或回退不剪枝；已验证的输入级压缩在规则、低风险负载中仍有较简单的优势。

视频内部的压缩还需要区分**全局冗余选择与局部合并边界**。仅按逆 kernel 密度逐 token 做 top-k 保留，可能把低得分但仍有意义的重复内容簇全部排除；按该得分加权采样降低整簇遗漏风险，但不保证覆盖。随后以帧内容变化划分区间，只在同一区间内合并，而不是让两个时间上不同的事件因视觉相近而共享一个代表 token。选择阶段决定保留哪些信息，区间边界决定哪些信息允许被混合，二者不能由同一个相似度阈值代替。<!-- source-family:SF-2026-ARXIV-2604-03414 -->

这条路径仍是有损表示：采样、区间判定与 merge 都需要校准，稀有瞬时证据可能被删除；保留率极低时质量也会退步。压缩器自身的时间必须加回 decoder 延迟，不能只比较压缩后的 LLM 部分。作者几款 video MLLM、A100 和固定视频任务的消融支持这组分工，不证明实时并发 SLO 或普遍无损。内容边界不稳、细节可回读性不足或压缩成本超过节省时，均匀采样、较高保留预算或 dense 输入仍合理。

attention 排名还有与相似性不同的偏差：跨帧积累较高 attention 的区域可能挤占保留预算，但累计值本身不能区分短暂尖峰与持续高值，也不是冗余或语义无用的真值。一个条件分支把当前帧空间得分与跨帧累计 attention 构成的 sink proxy 分开：前者提出保留候选，后者以软惩罚调整排名，再结合相似性阈值处理时间冗余，而不是把高 attention 位置硬判为无用。它修正的是 selector 分配规则，既不证明低 attention 缺少语义，也不证明静态显著对象不重要。<!-- source-family:SF-2026-ARXIV-2604-20937 -->

额外 attention 统计、跨帧汇总与惩罚系数需要校准，静态关键对象或短事件可能被误罚，应在细节证据不足时提高预算、回退原 attention 排名或完整输入。作者只在两类 7B video VLM、32帧和固定保留率上提供选择器消融；MCQA 与 GPT-5 评价的自由生成不是同一质量分母，部分切片仍退步，未证明90%剪枝无损或生产净加速。selector 质量交第66章按输出协议验收，驻留 KV 生命周期交第45章；soft penalty 不是安全或事实 authority。

连续控制中还要区分“平滑重要性估计”与“保留任务关键区域”。相邻 observation 变化小，复用历史 salience、用窗口和 EMA 平滑 2D/3D 特征比例及区域 attention，可以减少选择抖动；但历史若已误剪关键对象，平滑也可能延续错误。模态预算不能代替语义保护：先分别估计模态与对象/机器人区域的 salience，经窗口/EMA 平滑后形成各自的保留候选，再融合候选；第一步保留完整输入，为后续有损选择建立参照。<!-- source-family:SF-2026-ARXIV-2604-09244 -->

[受限 MLA/RLBench 消融](https://arxiv.org/html/2604.09244v1)中，模态选择加时间平滑低于不剪基线，而语义保护加时间平滑没有同样退步。这支持先检查两者的交互，不能证明某个 feature norm 或 attention 分数是真实因果重要性，也不保证任意控制任务无损。选择器计算、历史窗口与过期状态都要计入成本；新物体进入、遮挡突变或证据不足时，静态保守预算、不复用历史或完整视觉输入仍合理。第26章接手真实动作反馈，不能用 LLM 部分加速直接批准控制周期或安全 SLO。

表示稳定还有一个不同于重要性排序的陷阱：某层之后image-token几何变化小，或者用浅层状态替换深层状态后答案近似不变，不等于能把后续视觉访问删掉。替换仍让语言计算读取视觉信息，删除则改写访问合同；single-token答案、multi-token VQA与caption对这个改变的敏感度也不同。验收应把跨层替换和实际删token分开，删除时同步mask、position和KV位置，并用真实输出协议比较，而不是从probe稳定直接批准裁剪。<!-- source-family:SF-2026-ARXIV-2604-09425 -->

[六种VLM的受限对照](https://arxiv.org/html/2604.09425v1)支持“几何稳定不等于功能可删除”，但single-token答案也有退步，不能把短答案称为普遍安全路径。蒸馏可恢复部分行为，却引入额外训练和teacher依赖，caption的teacher-output相似也不是人类真值准确率。需要长答案、复杂图表或缺少协议匹配证据时保留完整视觉访问；只有实际删除、重排成本和任务回归都验收过，才能选较浅裁剪。第45章再接手存储后的KV生命周期，不能把删除表示当精确缓存复用。

更新责任还可进一步与读路径分开。浅层选择之后，深层停止更新视觉状态，但继续计算并提供它的 K/V，让文本查询仍能读取视觉证据；这与从后续层删掉视觉 tokens 不是同一操作。若 backbone 仍依赖深层视觉更新，则只冻结大部分视觉状态、让少量候选继续更新是另一条分支，而不是把“表示趋于稳定”升格为统一冻结规则。<!-- source-family:SF-2026-ARXIV-2604-16462 -->

[受限架构对照](https://arxiv.org/html/2604.16462v1)中，LLaVA 与 Qwen 对统一冻结策略的反应不同，LLaVA 的 OCR 也不能承受删除全部视觉读路径。几何熵只是选择代理，不是完整证据或因果证明；继续生成 K/V 与文本读取仍有成本，所节省的是部分状态更新工作，不能按删除比例推全部 Attention 或 KV 的收益。验收必须绑定 backbone、更新集合、读取集合及输出任务；不匹配时保留更多更新或完整视觉路径，缓存生命周期仍交由第45章负责。

一次性 prefill 剪枝适合后续证据需求稳定、预算严格的短回答；长推理中的视觉关注可能变化，原先被删的区域因而需要保留为可恢复的备用状态。一条 decode-stage 分支以当前与 prefill 的 attention 相似度触发重选，短期读取原集合与新集合的 union，再按策略回到原预算。这里保留与备用集合的 attention 分别归一化后拼接只是选择代理，不是全局概率或最优 top-k；回到原集合也不证明后续证据已经充分。

可恢复状态换来备用存储、临时扩大的 token 集合、重选和读取成本，还需核对语言历史与 KV 位置的一致性，不能称为精确恢复先前完整输入。attention 转移不是因果重要性真值，触发器会漏检；两类 VLM/L40S 的受限结果也有 TPS 或总时延退步。静态证据需求、短输出或额外状态不划算时继续使用固定剪枝；完整性优先时提高预算或回退完整输入。第 45 章接手存储后的生命周期，不由表示换入自动批准缓存复用。<!-- source-family:SF-2026-ARXIV-2604-12358 -->

### 固定表示之后，可以按未决 Claim 主动补充 Observation

一次性均匀采样或 top-k selection 在低分辨率已经足够、latency 上界严格时最容易复现；高分辨率细节只占很小区域时，它又可能在第一轮压缩中不可逆丢失。一个 bounded active-observation 分支先保留全局低分辨率 context，再由 acquisition policy 根据当前未决 claim 提出下一处 crop。Evidence assembler 记录坐标、尺度、采集顺序与预算，answer gate 决定继续、提交或拒答；selector 只拥有 observation proposal，不拥有 evidence sufficiency。<!-- semantic-body-binding:SF-2026-ARXIV-2605-01345 -->

主动取证以额外调用、路径依赖和尾延迟换取局部细节可见性，也可能因错误 crop、漏区或 backbone hallucination 形成自确认。采集策略漂移、证据完整性优先或预算不足时，应回退均匀/静态采样，必要时保留完整 tokens。exact-v1 只支持作者 VLM、crop proxy 与高分辨率 benchmark 下的机制方向，不证明 crop proposal 是充分证据或能覆盖开放世界视觉风险。

主动观察也可进入同一自回归轨迹，而不经每轮外部规划调用：离散标记提出是否继续聚焦，当前 hidden state 回归连续区域，crop 编码后作为新视觉状态接回未完成的推理。训练要分开普通答案 token 与观察动作的责任，先以文本和区域监督建立路径，再以动作收益及仅在正确回答条件下启用的面积正则约束“看哪里、看多少”。小 crop 本身不是好证据，答错时不能靠少读区域领取奖励。<!-- source-family:SF-2026-ARXIV-2604-21079 -->

该分支省去独立规划往返，却仍支付 crop 编码、新视觉 KV 与路径依赖；若持续保留新增视觉，缓存随观察数增长，不是旧完整输入的 exact 复用。错误区域会自确认，过强面积惩罚还可能删去必要细节。Qwen2.5-VL 单图任务的受限结果不覆盖视频或生产 tail；静态证据充分、额外动作不合成本时保持固定读取，取证不确定时扩大区域或回退完整观察。

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

即使总目标不变，负例之间也在竞争梯度。InfoNCE 的正例吸引项可分为 hard negative 与其余负例的概率质量；大量容易负例的总和仍可能压过单个困难负例。给 hard-negative logit 加 margin，可以改变两类排斥信号的相对分配，但也改变正例概率，不能把它解释成绝对总梯度不变的搬运。词语 concreteness 可辅助选择或调权，却只是生成质量代理，不拥有负例确实语义错误的 authority。<!-- source-family:SF-2026-ARXIV-2604-13313 -->

困难负例有假负例与生成噪声风险，全部移除容易负例又可能损害通用表示。[作者的受限对比训练](https://arxiv.org/html/2604.13313v1)中，自适应 margin 相对固定 margin 的部分收益很小，通用切片也可退步。因此应把组合关系区分与通用检索分别验收，并计入生成、筛选和训练成本；普通对比训练、人工核验的困难负例与保守固定权重继续共存，而不是把更强排斥当作对齐普遍更好的证据。

全局对齐与局部监督还要区分“输入被怎样腐化”和“哪些位置直接进入 loss”。只监督被遮蔽 patch，在学习由邻域恢复缺失内容时合理；但图像级对比目标已经收敛，不代表未遮蔽 patch 的表示能和文字概念直接对应。一个条件分支仍给 student 输入 masked view，却把 visible 与 masked patches 都纳入完整图像 teacher 的 patch-target 监督：改变的是监督支持集，不是取消遮蔽，也不是证明原模型没有局部信息。若目标同时包含全局检索与区域 grounding，应分别验收两者，不能由全局分数代替局部对齐。<!-- source-family:SF-2026-ARXIV-2604-12012 -->

这种分支增加逐 patch 目标和多目标耦合，也允许在外部图文对比信号足够稳定时只对 projection head 做 EMA、共享视觉 encoder；它没有取消 teacher head，更不保证纯自监督或任意共享配置都不坍缩。[作者的受限视觉预训练对照](https://arxiv.org/html/2604.12012v1)在冻结 encoder 的九任务、二十数据集上观察到条件收益与部分切片退步，累积 recipe 消融又不能识别所有组件的独立作用。只需要图像级检索、局部监督成本过高，或稳定性证据不足时，全局对比和完整 EMA teacher 仍是合理分支；改变监督范围后须重新检查定位、检索及训练资源，而不是把一条 recipe 当作全部下游任务的统一表示保证。

腐化位置与恢复责任也可以跨过视觉 encoder 与语言模型的边界：视觉 patch 先经 projector 进入语言空间，再对选定 token 加噪声或遮蔽，由语言模型中间层的训练期 decoder 恢复冻结视觉 encoder 的 clean patch targets，并与 patch 间关系、同图判别和答案 loss 联合训练。前述分支改变视觉预训练中的 patch 监督范围；此处检验的是视觉信息经过语言模型内部后是否仍可恢复。clean teacher feature 是表示目标，不是视觉事实真值，causal mask 也不允许借未来位置的视觉信息。<!-- source-family:SF-2026-ARXIV-2604-21343 -->

部署时撤去腐化和辅助 decoder，并不抹去训练成本。所测 LLaVA/Qwen 视觉问答的 clean 指标有退步，CKA 与 kNN 变化也不能唯一归因于语义对齐；在 latent 表示上训练腐化，不等于已证实能抵御任意测试时 pixel 污染。腐化比例、saliency 与监督层位应随模型和任务校准，并分别验收 clean 质量、视觉证据保持和污染切片。成本过高或 clean 损伤明显时，普通答案监督与已有 patch 对齐仍可共存，必要时恢复完整视觉读取，而不把重建置信度当事实证据。<!-- source-family:SF-2026-ARXIV-2604-21343 -->

检索表示若要多步整合图像、视频或文档证据，单次 encoder pass 最便宜，但可能没有足够中间计算；先生成文字 CoT 再取 embedding 增加可检查的步骤，却把多模态证据压进文字并按 token 串行付费。一个实验性中间分支在训练时先用显式推理作 scaffold，再逐步替换为少量连续 latent transitions，最终从隐藏状态取检索 embedding。它把推理预算从“可读文字 token 数”改为“latent step 数、每步 KV 和 adapter 状态”，可能降低长 CoT 延迟，却降低中间步骤的可审计性，并要求课程迁移、表示质量与检索排序一起验收。无需复杂推理的 query 仍可用单次 embedding；需要可追责的高风险判断仍应保留文字 trace 或外部证据。作者的多模态检索对照只覆盖所测 Qwen2-VL-2B、MMEB-v2 与单卡 H20 条件；latent 检索收益不证明生成推理质量或生产 SLO。<!-- source-family:SF-2026-ARXIV-2604-02073 -->

在多模态检索里，“加入推理后更接近正例”也不等于排序更好；若最近的 hard negative 同时变得更近，正负 margin 仍可能缩小。因而评估 reasoning-enhanced embedding 应记录正例增益、最难负例增益及两者之差，而不是只看 rationale 是否合理或正例 cosine。只有能在不知标签的候选邻域中稳定改善 margin，额外推理才值得其 token/latency 成本；[作者的多模态检索实验](https://arxiv.org/html/2609.29560v1)发现一些表面正向对齐却损害排序的样本，但其直接候选条件化提示并未得到可部署的稳定收益，不能把诊断指标写成已验证的在线路由器。
<!-- source-family:SF-2026-ARXIV-2609-29560 -->

长工具轨迹还可以只作为训练期表示目标，而不成为推理期的 latent 轨迹。显式图像编辑与文字解释可审计，却需要工具和多轮执行；一个受限分支分别编码原始图像问题与完整专家轨迹，用少量预测 token 学习后者的末位隐藏表示，并对轨迹分支 stop-gradient，同时保留答案监督及下一隐藏状态的辅助预测。这里压缩的是训练目标：部署时撤掉预测 token 与工具，恢复普通 VLM 前向；它不同于前述推理时仍执行 latent transitions 的检索分支。<!-- source-family:SF-2026-ARXIV-2604-08065 -->

这种蒸馏减少部署依赖，却把可检查的编辑过程换成不可直接观察的表示匹配。完整专家轨迹含最终答案，其隐藏状态不能因被预测就成为经过验证的环境状态，更不能推出模型实际执行了图像编辑或多步规划。作者只测试三类受限工具调用轨迹，部分子任务退步，没有覆盖多种工具多次调用，也未证明生产 latency/SLO；需要检查中间操作、高风险视觉判断或训练分布之外的任务仍应保留显式工具与原图证据。<!-- source-family:SF-2026-ARXIV-2604-08065 -->

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

保存真实时间元数据，也不意味着 backbone 已能读取“第几秒”。序列位置只说明先后与距离，不天然具有物理时间单位；时间定位需求可以增加独立 timestamp-token 接口，在音频特征之间插入时间标记，以预训练数字子词的语义均值初始化并冻结这些新增 embedding，再通过 SFT 学习如何消费它们。模型侧的可读时间表示与采集侧的真实时钟仍是两个 owner：前者产生定位 proposal，后者负责单位、同步误差和 provenance，不能用生成的秒数反写传感器事实。<!-- source-family:SF-2026-ARXIV-2604-13715 -->

[有限音频对照](https://arxiv.org/html/2604.13715v1)在 25 Hz 特征与 0–30 秒、0.04 秒粒度的标记网格中观察到语义初始化的收益，随机初始化反而在部分任务退步。它不是仅加几个符号而无需训练，也不证明更长音频、任意采样率或精确物理定位：词表与输入长度增加、接口 SFT 和后续训练都计入成本。原始 timestamp 必须继续归档；网格范围、时钟或模型变化时重新校准，不适配时保留原位置编码与显式时间监督，而不是让新的表示取代同步合同。

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

视觉 token 的删减还不能独立于后续数值格式决定。在全精度路径上，按问题相关性保留 patch 是合理起点；
一旦 decoder 使用低比特 weight-and-activation quantization，被保留 token 的 activation 分布也决定量化误差。
只按语义分数删减，可能丢掉对量化行为敏感的 outlier-bearing token；反过来，盲目保留数值极值又会
占用本应留给语义证据的预算。表示侧的选择器因此可以联合估计任务相关性、模拟量化残差与动态范围，
但它只提出 retained-token proposal，最终接受仍取决于目标精度下的任务质量和实际执行路径。

联合选择增加特征统计、校准依赖与选择器成本；高精度、宽松 token budget 或无需动态剪枝时，原来的
语义选择或 dense 输入仍更简单。现有证据只在受测 LLaVA、W4A4 PTQ、ScienceQA 与特定剪枝比例下
支持这种耦合，不证明数值 outlier 在所有模型中都应保留，也不证明端到端延迟收益。量化 artifact、
kernel compatibility 与 serving SLO 的验收交给第 49 章，不能由表示压缩率代替。
<!-- source-family:SF-2026-ARXIV-2604-02816 -->

### 长视频从固定输入窗口走向可回读的视觉记忆

逐帧或均匀采样适合短视频与完整证据优先的任务；固定窗口装不下持续到来的画面时，单纯压缩所有视觉 token 虽可延长输入，却仍让最终回答读取不断增长的历史。另一条受限路线把逐 clip 产生的 visual KV **派生**为两种不同状态：小容量的 context memory 随下一 clip 传播时序信息，压缩的 local memory 写入 clip memory bank；回答时再按问题检索少量 clip。写入、跨 clip 传播与按需读取因此不再由同一组活跃 KV 承担。原 clip 的时间位置、模型与压缩版本以及读回映射需要可回指，否则“找到了相关记忆”无法证明未遗漏关键帧。这是表示和证据身份的责任；真正的 KV 容量、调度与尾延迟仍由推理运行时验收。

这样做以压缩误差、检索遗漏、陈旧片段和索引/重复编码成本，换取固定回答预算下处理更长视频的可能。查询尚未知晓或全局时序关系比局部片段更重要时，按问题选取的记忆尤其可能失效，应保留密集短窗、固定采样或回读原片段的路径。[FlexMem 的原始实验](https://arxiv.org/html/2603.29252v1)只覆盖两类 LLaVA 视频模型、五项长视频与一项流视频任务，以及其单卡 GPU 条件；它的“无限长度”是迭代处理接口，不是无损、无限容量的视觉记忆，也未证明生产并发与 SLO。

<!-- source-family:SF-2026-ARXIV-2603-29252 -->

与“先为所有 clip 写入压缩记忆、提问时再读”不同，主动观察分支由当前问题决定下一次读取的时间段、帧率与模态，通过读取工具取得视觉、音频或 transcript 后再继续推理。它能避开无关输入并回看短暂事件，却把证据遗漏、读取历史与额外推理/tool round-trip 变成新的责任；少载入 token 不保证更低的端到端时延，短片或完整证据优先时，固定读取仍更简单可靠。

### 用表示几何区分重排与扩展

把 Attention 与 FFN 都概括为“融合信息”会掩盖二者可能承担的不同责任。更细的诊断可以同时观察 residual update 是否引入新的子空间，以及 token mixing 带来的信息增量：在一组受限的视觉语言模型中，Attention 更接近在已有子空间内重排跨模态关系，FFN 则更像扩展可表达方向；部分层替换实验还提示，learned visual routing 可能存在冗余。<!-- semantic-body-binding:SF-2026-ARXIV-2605-05668 -->

这不是 Attention 普遍无用的结论。证据只覆盖两个模型家族、15 个变体、七个 benchmark 和被选择的层；相关统计也不能代替端到端因果验证。若同类诊断或替换不能在目标模型与任务复现，就应保留 learned Attention，并用 causal ablation、质量回归和 serving cost 共同决定是否改变结构。

## Failure modes

### 语义锚点不是原模态的替代品

长音频可以借助 transcript 作为 semantic anchor，把声学 token 与时间轴、实体和语义片段对齐，再依据时间衰减和 accumulated attention 压缩 cache。它比只按位置裁剪更理解内容，却把 ASR 错误、语言覆盖和时间对齐偏差引入表示 identity。原始声学 token 仍拥有音色、韵律、重叠说话人与非语音事件；anchor 只能帮助选择，不能成为无损真值。

因此系统应同时保留 `raw modality span → anchor revision → fused token range` 的 provenance。低资源语言、噪声环境、实时 streaming 或 ASR 不可信时，固定窗口与原模态保留仍是更稳健的旧分支。

这个边界还必须回到训练目标。只以 transcript 监督音频到文本，对内容对齐与 ASR 是合理选择，却不直接奖励音色、韵律、说话人或环境事件的恢复；保留声学 encoder 本身不意味着这些能力已被训练。需要细粒度感知时，可以把 spoken content、paralinguistics 与 non-linguistic events 作为显式字段或独立任务，让表示与 projector 按真实目标覆盖接受评价，而不是指望语言推理补回未被监督的信息。

结构化 target 增加标签生成、验证、输出长度与多目标权重成本；字段 schema 只是接口，不因 JSON 就保证参数或语义正交解耦。相同合成来源下的受限 caption 对照支持监督设计值得选择，却未完全隔离格式、标签密度与总训练成本；主要说话人及英中覆盖不能代表重叠语音或所有语言，ASR 也可能有小幅 WER 代价。内容任务仍可保留简单 transcript 路线，感知任务则同时检查目标标签可靠性、原声学证据和内容回归，不把文本字段升级为声学真值。<!-- source-family:SF-2026-ARXIV-2604-12506 -->

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

进入几何状态之前，还需明确位置身份服务的是参考内容还是目标布局。参考图像用于提供对象身份时，直接沿用其二维位置可能把原布局一起带入生成；目标 pose 却必须绑定输出画布的位置。一条条件分支让参考 token 使用随前面参考尺寸累计偏移的坐标，目标 pose 使用自身网格坐标，并分别调节视觉与文本条件。它不是消除所有参考位置，而是避免把“从哪里取身份”与“在哪里生成”交给同一位置规则。<!-- source-family:SF-2026-ARXIV-2604-13938 -->

[受限位置分配消融](https://arxiv.org/html/2604.13938v1)支持这一 reference/pose 分责；条件偏移模块仍同时改变身份与 pose 表现，不能称一般完全解耦或无干扰。它需要额外数据、检索、adapter 与训练，有限 FLUX 对照也并非所有质量指标都最好。单一参考、布局一致或预算较紧时，统一位置规则继续合理；多参考方案须连同目标网格、参考顺序和模型版本共同验收。这里约束的是表示身份，Ch24 负责生成控制，不能据姿态条件一致就认定真实三维状态或动作可执行。

相对几何还可以由 query 所在视图定义，而不只由全局 reference 坐标给出。标定相机的 token 射线先在若干固定深度锚点升至 3D，再投影到当前 query 视图，以普通 2D RoPE 编码投影位置；深度锚点是接口假设，不是逐点测得的 depth truth。同一 view 退化为原 2D 规则，多 view 则让同一 key 在不同 query-view 下拥有不同位置视图，camera calibration 与编码器共同定义这个 derived state。<!-- source-family:SF-2026-ARXIV-2604-18747 -->

数学接口可以复用 2D attention，不代表执行只保留一份无条件通用 KV：把 query-view 维移到 batch 并重复 K/V 会增加几何计算、内存和读写，view 或标定改变后不能沿用旧 derived position。[受限重建、检测与 matching 对照](https://arxiv.org/html/2604.18747v1)有 RGBD 指标退步，联合训练 recipe 也不支持单因果归因。标定不可信、锚点范围失配或预算不足时，已有 2D 位置、显式 3D 编码和任务专用几何接口仍应共存；生成与环境状态还须各自验收，不能把位置规则升级为物理真值。

多视角共享射线字段，不一定要共享同一个 condition encoder。pinhole 与超广角 fisheye 可以都用六维 Plücker 接口，但各自的 unprojection 和方向统计仍不同；保留原生 pixel/token grid，再按 semantic camera identity 分派投影族 adapter，可以避免仅凭相同 shape 让 backbone 猜测相机类型。跨视图 attention 可在同一 latent 时刻合并不同长度的 tokens，以标定射线和 view identity 建立联系，而不把不同投影网格的二维位置直接视作可比；全局 ego-motion 与逐像素几何也应各自保留来源与职责。

[混合 rig 的受限实现](https://arxiv.org/html/2609.21712v1)用额外 adapter、标定/pose 处理与 overlap mask 换取原生视图接口；训练与推理时的投影族、语义 slot 和 token-grid packing 应一致，这是由接口推得的验收要求，不是论文已证明任意标定都可靠。现有评价没有独立隔离投影族 adapter 收益，生成/几何代理和定性长 rollout 也不证明物理闭环安全。标定、projection dispatch 或 packing 不可靠时，保留独立相机处理、已有显式几何接口或受限重标定，不把共有字段维度当作 encoder 可互换的证据。<!-- source-family:SF-2026-ARXIV-2609-21712 -->

先由独立 3D reconstruction pipeline 生成 mesh，再把结果作为多模态模型的只读输入，职责清楚且容易单独验证；当任务要求多轮理解、生成和局部编辑保持同一几何身份时，stateless sidecar 会丢失跨轮 mesh state。另一条分支把 3D primitives/mesh 表示纳入统一 token contract，并让 modality-specific experts 共享同一 identity 与 revision。

它提高跨任务连续性，却增加 tokenizer/mesh discretization、长 Context、几何一致性和编辑回滚成本。模型拥有 proposal，不拥有物理几何真值；identity 保持和生成 fidelity 也不能证明真实世界尺度或可执行性。单次重建、精确 CAD 或安全关键几何仍应由专用工具与确定性验证承担。

<!-- source-family:SF-2026-ARXIV-2605-16745 -->

相机状态也不一定只能作为外部估计器输出的只读condition。若要在同一接口里做camera-controlled生成与camera estimation，可以在canonical reference frame中，将逐像素射线方向与原点的向量和编码成三通道raxel，复用视频VAE，再用明确的modality和grid位置身份进行video/camera联合去噪。它把相机从sidecar参数变成可生成、可修订的状态；同shape和chain-rule分解仍不证明网络已学到正确joint，更不是外部估计器必定失效。<!-- source-family:SF-2026-ARXIV-2604-09429 -->

这种兼容用额外camera分支、训练耦合与几何解码换接口复用；coarse ray grid、canonical normalization、modality RoPE与VAE版本必须可追溯。[受限实现](https://arxiv.org/html/2604.09429v1)在14B视频模型外增加6B分支，decoded rays经Procrustes恢复pose，focal估计假设principal point居中。它的Plücker对照同时改变codec，不能单独归因表示更优；生成循环一致也不是外部3D真值，动态场景和内参偏离仍需验证。精确标定、安全几何或训练预算不足时，独立pose工具与只读camera conditioning继续合理，后续World Model还须验真实transition。

逐帧视频 token 仍可能把同一对象在不同视角和时间中的身份复制多次。Track-aligned 表示把稳定背景与动态对象分开，并让轨迹、相机和时间成为 token identity，从而把 frame archive 压成可修订的 4D state。它获得存储与生成上的复用，却依赖 track、camera geometry 和 static/dynamic disentanglement；视觉可重建不证明物理动力学，真实 transition 仍由下一章负责。

<!-- source-family:SF-2026-ARXIV-2609-12874 -->

## Token Hierarchy 可以承载不同时间尺度

音频等高带宽模态若只用单层离散码，要么语义结构过粗，要么 token rate 过高。分层 residual quantization 可以让上层 code 承担长程语义和结构，下层 code 补局部声学细节；相应生成器也可分为 global sequence model、local refinement 与连续 decoder。

层次化表示提高可控性，却引入 codebook synchronization、跨层 error propagation 和更复杂的 bitrate/latency 预算。它是表示分解，不证明某个公开音乐模型的质量结论可外推；Ch24 只接手后续生成与修正机制。

高频触觉进一步说明“同一时间轴”不等于“同一采样密度”。接触事件稀疏时，复制成 dense visual stream 会浪费预算并稀释信号；更合适的 contract 是为 tactile event 保存独立 rate、timestamp、sensor calibration 与稀疏预测目标，再由共享语义层消费。代价是异步对齐、漂移和缺失事件，传感器或 embodiment 改变时不能继承旧 token identity。

<!-- source-family:SF-2026-ARXIV-2609-12549 -->

## Streaming Multimodal Identity 不止是 Token Type

实时全双工系统中，用户音频、视频、文本与 assistant 输出会并发到达，输入不会在生成开始前自然结束。表示层必须把 token 绑定到 timestamp、speaker/turn、observation revision 与 interrupt frontier；fusion 只负责产生共享表示，runtime 才决定哪些输出可以继续、取消或提交。

表示可以早于完整输入形成，但模型此时允许读取多少 prefix 是另一项选择。一个闭式日程分支用输出进度、输入长度估计和预算参数构造单调 attention mask；它只决定每一步可见哪些输入，不拥有物理到达时钟、回复提交或打断权限。固定输入版的 length head 消费已完整可用的输入；真正流式的变体则只能从 arrived prefix 与上一窗口信息预测总长，以 arrived horizon 限制可见性。因果性保证以这些输入确实先到达为前提，不能将“mask不看未来”写成端到端 deadline 已满足。<!-- source-family:SF-2026-ARXIV-2609-20845 -->

这条路径增加长度 head、预测漂移和预算校准，也可能因等待不足漏证或等待过多延迟。作者 29M/四层 decoder 配冻结 CLIP/C3D/Whisper、单 T4 的实验只覆盖 window-synchronized 到达；异步到达属于条件证明，没有实测 live service。wait-k 的长度 head 职责不完全对称，流式 single run 的 test-clip bootstrap 不覆盖训练噪声；三 seed 修正还改变 ActivityNet 的最佳预算区域，LibriHeavy 差距落在 seed spread 内。因此采用可见 prefix 与实际到达的分工，不采用跨任务统一质量优胜；预测不稳或 deadline 不可验时，保留 wait-k、完整输入或外部 turn-taking，runtime 仍负责 commit/cancel，这是工程交接而非作者已验证的状态机。[必要日程与反证](https://arxiv.org/html/2609.20845v1)。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-25621:start -->
无限保留流式历史不现实，固定窗口又会丢掉远处但仍有效的跨模态证据。一个受限分支把音视频证据压成固定预算的 long/short-term memory，再由独立 hidden-state trigger 判断何时主动响应。Memory 只保存带时间与来源的 evidence，trigger 只提出 reply timing，runtime 仍拥有 commit/cancel；不能用 silence token 或模型内部触发替代外部 turn-taking authority。

持续压缩和 trigger 增加计算、时序对齐和阈值校准，压缩漏证或 false trigger 会导致过早回答或关键时刻沉默。越界时应回退固定窗口、显式 turn-taking/外部 router，或离线完整上下文。作者 benchmark 只支持所测音视频任务，不证明任意全双工服务的实时性和可靠性。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-25621:end -->

主动响应不仅需要一个触发分数，还要让训练看见“为什么现在应该响或保持沉默”。面对同一watch-out意图，可区分无关转相关的onset、已经相关但尚未通知的持续窗口、完全无关，以及相关但通知已在history中四种机会。分别监督interrupt与silent，让错过onset后仍可补发，同时避免每个重叠窗口重报；这不是把声学分类准确率直接换算成通知能力。

history中的已通知标记必须来自runtime真实交付状态，而非模型自称；表示与决策仍不拥有播放/取消commit权。事件样本构造、history更新和领域校准增加成本；cleanclip上的去重高分未证明噪声域同样成立，后者无关silence和持续召回仍低且未测history去重。固定onset拼接流的平均延迟不等实际device或用户效用保证；分布不匹配或重复/漏报超预算时保留外部eventrouter、显式确认及保守阈值，而不是让silent token替代交付验收。 [必要机制与反证](https://arxiv.org/html/2609.21183v1)。<!-- source-family:SF-2026-ARXIV-2609-21183 -->

统一 attention 可以促进跨模态协同，却也可能让高资源模态挤压另一模态。modality-specific encoder/FFN 保留专用容量，shared layer 提供交互；早统一减少接口鸿沟但增加目标竞争，晚统一更稳定却容易形成“vision laziness”。选择应随数据复杂度、模态预算和交互 deadline 变化，不存在仅凭统一程度判断优劣的结论。

### 实时多模态表示还必须拥有可中断的时间状态

离线的图文拼接可以在全部输入到齐后一次编码；full-duplex 交互中，音频、视频、文本、tool event 却在不同时间抵达，用户还可能在模型输出中途插话。表示层因而不仅要标记 modality，还要保存 timestamp、stream revision、turn ownership 与 interrupt boundary，使后续状态机知道哪些 token 已提交、哪些生成应取消、哪些观测仍可继续复用。统一 backbone 减少专用管线，却把时钟漂移、乱序、过期观测和半双工回退变成显式 failure mode；无法稳定对齐时，分模态缓冲与保守 turn-taking 仍是合理旧方案。官方公告只支持所披露系统具备统一音视频文本与全双工交互接口，没有公开这些状态字段的内部实现，也不构成通用打断或安全保证。
<!-- source-family: https://seed.bytedance.com/en/blog/seedrealtime-audio-visual-full-duplex-llm-released-toward-omni-modal-natural-interaction; daily: 2026-08-05; semantic-body-binding: interruptible-streaming-multimodal-identity -->

### 共享表示的收益来自可控的容量交换，而不是“越早融合越好”

晚融合让各模态保留专用容量，训练稳定且易隔离，却可能让视觉只在末端提供旁路信息；早融合让 attention 与 normalization 更早交换信息，但也会让文本与视觉目标竞争同一容量。一种中间分支是共享跨模态交互层、保留 modality-specific FFN 或路由容量，并按数据复杂度与 token 预算重新选择配比。它用更强 transfer 换来 routed capacity、通信和配比校准成本；在数据不足、模态分布漂移或硬实时单模态路径中，专用 encoder 与晚融合仍应共存。
<!-- source-family: arxiv:2608.05000v1; daily: 2026-08-06; semantic-body-binding: multimodal-capacity-sharing-frontier -->

从已训练好的理解模型加入生成分支时，容量隔离还要决定谁能更新共享容量，而不仅是谁能读它。一个受限分支用原模型的 activation profile 选择保留 Text/ViT expert 组，把另一组分给 VAE token，并从原 router 切片初始化；共享 expert 仍被所有模态读取。生成侧尚不稳定的 warmup 阶段允许它前向利用共享表征，却暂时截断它写回共享 expert 的梯度；之后释放该路径、限制生成梯度幅度，并让成熟理解组与新生成组使用不同 learning rate。前向共享、反向更新权和路由容量因此是三个可分别选择的旋钮，不是“隔离或统一”的二选一。<!-- source-family:SF-2026-ARXIV-2604-07753 -->

代价是 profile/分组身份、参数组 schedule 与恢复状态更复杂，也可能延迟生成学习或固化旧 specialization。有限消融中，理解任务单独使用较大 learning rate 也会退化，因而不能把遗忘全归于跨任务冲突；暂时 shielding 的早期收益也不证明全部长期收益由它单独造成。作者的 Hunyuan-A3B/专有混合数据仅支持这一条件设计，零步重分组仍有能力损失，模态平均 utilization 还需分开检查。已有稳定 recipe、分组依据不可靠或恢复简单性优先时，统一更新、小 learning rate 和显式 adapter 仍是合理基线。

### 统一架构不等于双向可用的统一语义空间

共享 backbone、token space 或 loss 只能说明不同模态在同一计算图中交互，不能证明 understanding 分支形成的方向可被 generation 分支以相同语义读取。更强的对齐证据需要跨分支干预：从一侧提取语义方向，在另一侧做 matched steering，并用 random、unrelated direction 与人工/任务结果作对照。

受控实验观察到的单向可迁移也不能自动升级为共享因果表示；概念集合、prompt 组合、投影方法与 evaluator 都可能限制结论。干预式验证换来更强证据，但增加 off-manifold steering 和 evaluator bias。因而 representation contract 应区分“共享参数”“可解码相关性”与“跨分支可操纵语义”；对齐证据不足时，modality-specific interface 和显式 adapter 仍是更稳妥的共存方案。

<!-- source-family:SF-2026-ARXIV-2607-26411 -->

即使同一模型某层最容易被 linear probe 读出，也不表示它是最有效的 steering 入口。读出在固定表示上拟合分类边界；控制则把目标与中性 centroid 的差方向去除主成分、归一化，再按该层 hidden-state norm 注入，必须与同 norm 的随机方向配对比较。[单层扫描](https://arxiv.org/html/2609.22135v1)在三个模型中测得 probe peak 与 steering peak 相隔 7/10/9 层，支持层选择不能直接从 probe accuracy 复制；但相关系数 .45/.55/.36 未满足预注册的 r<.30 条件，只满足另一项 peak-gap≥5 条件。多层注入还改变注入层数，不能把其相对单层的倍数收益当纯位置收益；logit-lens 的 H1 及统一 threshold 解释也有失败例。

层扫描、方向校准和额外 evaluator 增加成本，并带来 off-manifold 与分布迁移风险，故工程上仍需保留显式 adapter 或未干预路径作为回退。该证据限于 Qwen2.5-Omni 7B、Phi-4-Multimodal 3.8B、MiniCPM-o 4.5 的英语 text/audio/image 输入到文本输出、五 seed 扫描；hardware/precision 未披露。Joy 的多层 mapped steering 在前两模型有效，但 MiniCPM 的 Δ=.022、CI [-.064,.122] 不排零，anger 对 judge 敏感；额外 GPT-5.5 文本评估也不是人类真值。它纠正“read-best 就是 steer-best”的选择依据，不证明所有模型、输出模态或规模都可按同一方向控制。<!-- source-family:SF-2026-ARXIV-2609-22135 -->

甚至常用的标量几何指标也可能误导这一判断。视觉 token 注入受控噪声后，任务准确率可以下降，而 CKA、SVCCA 或主子空间余弦仍显得“对齐”；共享语言 MLP 的各向异性输出方向会制造这种相关性。故跨模态表示验收要同时保留任务行为、干预前后分层几何及随机方向对照，不能用一条 cosine 曲线给语义忠实性背书。这个更严格的检查增加干预与分析成本，且某些几何指标对定位层内变化仍有用；[原始干预研究](https://arxiv.org/html/2609.30210v1)限于其测试的 projector-LLM 架构和任务，不证明所有融合模型有同一机制。
<!-- source-family:SF-2026-ARXIV-2609-30210 -->

理解和生成还可能使用两套不兼容的视觉 token：前者强调语义压缩，后者强调可重建细节。共享 backbone 并不能消除这种 identity split。可选分支是让 context 与 visual generation 共享 tokenizer，并用并行 bitwise prediction 提高 autoregressive 表达效率，同时保留独立 decoder 负责生成 artifact。Tokenizer owner 持有 token/bit layout 与 rate–distortion 版本，decoder owner 持有重建合同；二者不能用“统一 token”相互代替。

统一表示降低接口分裂，却引入 bitwise independence 假设、decoder 版本耦合和理解/生成目标竞争。单一表示不能同时在所有任务上最优；当重建质量或理解能力受损时，双 tokenizer 与显式 bridge 仍是合理分支。

<!-- semantic-body-binding:SF-2026-ARXIV-2606.18249 -->

### Faithful transcription 与语义归一化是不同输出合同

通用 VLM 用语言先验修复噪声字符，在问答和理解任务中可能合理；当任务要求逐字 OCR、证件号或代码抄录时，同一机制会把异常字符串改写成更 plausible 的文本。语义正确率不能替代 character-level fidelity，representation pipeline 必须显式声明输出是 transcription 还是 interpretation。

跨系统、语言和扰动实验只能说明这种风险存在，不能证明所有 VLM 都不适合 OCR。需要 exact evidence 时，应保存 source image、使用 OCR-specialized/raw-text 路径并做字符级对齐；允许语义归一化时仍应把改写标为 derived artifact，而不是冒充原文。

<!-- source-family:SF-2026-ARXIV-2607-21617 -->

OCR-specialized 输出也不自动意味着 decoder 获得一套全新的视觉读取电路。若要区分路径重建与已有路径重新加权，可以先沿模型实际自由生成的 prefix 重放 attention，只对完整匹配 reference 且有可见图像证据的 tokens 定位候选 heads，再在独立页面切分上用等数量、每层匹配的随机 heads 做消融；同一 backbone 专门化前后的候选身份、强度与因果贡献要分别比较。受限实验中，OCR 头与文本 retrieval/copy 头有交叠，Qwen 两代专门化前后的 top-20 集合大部分保留，但消融贡献会改变。它支持“既有读取结构可以被重新利用并强化”的分支，不证明头内 features、所有未测路径或整条 circuit 完全不变，更不因表示 drift 就推出诞生了新机制。

定位增加白盒 replay、证据对齐、分层随机消融和配对训练成本，且只对合法、未截断、可精确对齐输出形成条件人口。该 Qwen2/3-VL-2B 对照还同时改变部署 prompt，不能把全部变化纯归因于权重微调；Qwen3 表格专门化前的一组目标消融不全面强于随机对照，文本整体误差也未单调改善。固定 Q/K 与 attention 后替换成对图像的目标位置 V，可推动正向 logit 差却未翻转目标 token 胜负；对照又未匹配 attention mass 与 V 差范数，故不证明该头单独充分或位置是唯一因果。生产路径仍应保留原图、字符级 fidelity 与任务回归；诊断不稳时使用完整视觉读取和外部 OCR，不根据稀疏头排名直接裁剪。 [必要机制与反证](https://arxiv.org/html/2609.21543v1)。<!-- source-family:SF-2026-ARXIV-2609-21543 -->

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

干预的单位本身也决定“阴性结果”能否排除一条路径。只替换最后位置的hidden state、答案几乎不变，不能证明视觉信息没有通过整个sequence参与仲裁；分布式表示可能需要同时交换同层多位置的状态，才改变视觉证据与语言prior的竞争。因而先声明被交换的位置、层和上下文，再用完整sequence与最后位置的matched干预比较，不能把一个局部patch失败当作视觉blindness。<!-- source-family:SF-2026-ARXIV-2604-09364 -->

这增加白盒读取、反事实构造及扰动副作用。[受限合成色彩实验](https://arxiv.org/html/2604.09364v1)中，九模型各100样本的full-sequence patch与last-position patch给出明显不同结果；MAC稳定logit crossover只是定位heuristic，不是唯一因果层。三种7B～8B模型的局部steering也有退步，不能推到所有自然图像或把可读视觉信号升级为最终truth。接口不可见、反事实不匹配或干预破坏其他内容时，应保留外部grounding、输入级反事实与实际行为对照。

在 VQ 图像 token 与语言 token 共用离散路径的架构中，早层还可能承担 codebook bias 的路由，故“视觉写入/语言读取”不能机械映射到所有 VLM 的同一层。对某个模型，定点消融早层能降低对象幻觉；在另一些模型，同样消融无效甚至破坏辨别。先用成对反事实定位 writer/reader、再检查 open-ended caption 的长度、召回与幻觉，才能判断干预有没有把模型变成只会少说的 emitter。作者 25 个模型的诊断与 500 图像 caption 测试只支持架构相关的定位法：VILA-U 的 CHAIR 改善同时伴随明显变短和召回下降，诱导的 LLaVA-VQ 没有同等稳健证据。外部 grounding 与行为评测仍拥有发布判断。<!-- source-family:SF-2026-ARXIV-2609-29048 -->

<!-- semantic-body-binding:SF-2026-ARXIV-2605-14621:start -->
同一故障也可以在单次主干计算中构造内部对照：shared early prefix 保留 prompt、history、position 与早期 grounding，late
counterfactual branch 屏蔽 image-token access，再由 contrastive decoder 比较视觉证据是否仍在后层写入。该 branch 只提出
token proposal，不能把 hidden-state 差异升级为事实真值；独立 grounding/evidence gate 仍拥有 acceptance。它减少外部图像
扰动和第二次完整 forward，却增加 white-box hidden-state、mask/cache 与 late-layer compute 依赖。模型接口不可见、cache
不兼容或内部对照失效时，应回退外部反事实、grounding verifier 与行为评测。exact-v1 只支持作者模型和实验。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-14621:end -->

音频反事实还要选择保留什么时间结构。完全移除音频适合检验有无模态影响，却会同时删除粗语义与瞬态线索；另一条受限分支把短时间变化平滑后重新编码成慢参考，让原始与慢路径在同一文本历史下预测下一个 token，再只在音频依赖较高且预测不确定的位置，对小候选集合施加正向 logit 差更新。这是时间尺度对照，不把差值当声学真值，也不证明语言 prior 已经被消除；输出仍须通过任务 grounding 评价。<!-- source-family:SF-2026-ARXIV-2604-15383 -->

对照是否有用取决于 decoder 能否利用该时间差。受测统一 audio/text decoder 的改善不意味着独立编码、拼接架构同样改善，最强模型的 speech 子集也有退步，因而不能无条件打开干预。两路编码、稳定性估计与独立 KV 状态增加 prefill 和内存成本：单 A800、3 秒音频/100 token、关闭 FlashAttention 且优化复用原路径 KV 的对照中，memory-bound batch2 decode 隐藏部分增量，但 prefill 约加倍，不是全服务零成本。时间扰动损伤语义、模型接口不可见或质量、成本不合算时，应保留原始 decode 与外部证据对照；第 49/56 章另验实际执行与 SLO。

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

- `SF-2026-ARXIV-2604-21326`（Experimental）：[MiMIC exact-v1](https://arxiv.org/html/2604.21326v1) §3–5/A.3，Daily 2026-04-24。采用跨读两模态与 single-modality mix-in/caption dropout 的缺模态训练责任；纯文本退步、T5/CLIP和改造数据集范围保留，不把FiD写成所有融合的优越性或检索真值。root必要 source→现有 owner 采用核、实际正文与相邻衔接写后非作者复核均通过；未复现实验。
- `SF-2026-ARXIV-2604-21079`（Experimental）：[Foveated Reasoning exact-v1](https://arxiv.org/html/2604.21079v1) §2.1–3.3/§4/Table3/AppC，Daily 2026-04-24。采用单自回归轨迹观察动作头、连续区域及correct-only面积训练职责；crop/KV成本、单图范围及不充分证据边界保留。root必要 source→现有 owner 采用核、实际正文与相邻衔接写后非作者复核均通过；未复现实验。

- `SF-2026-ARXIV-2604-21343`（Experimental）：[exact-v1](https://arxiv.org/html/2604.21343v1) §3.1–3.3/Eq4–12、§4.1–4.6/Table1。采用 projector 后语言空间腐化→中间层 clean-feature 恢复的训练职责；LLaVA/Qwen clean 退步、latent/pixel 扰动差别与 CKA/kNN 归因边界保留。apr02 必要 source→实际 owner 复核通过；root 已复核正文与前一训练监督分支，写后 PASS，未复现实验。

- `SF-2026-ARXIV-2604-18747`（Experimental）：[URoPE v1](https://arxiv.org/html/2604.18747v1)，Daily 2026-04-22；§3.1–3.3/Eqs1–10、§4主表/消融及0.C。采用 calibrated ray/depth-anchor→query-view projection→2D RoPE 的位置接口及 query-view batch/KV 重复的执行代价，不采深度真值、普遍几何效果或无成本复用。RGBD 退步、联合训练混杂、标定与深度范围依赖保留；6分缺口深入，root 必要源→实际 owner/literal 独立采用通过，实际正文与相邻衔接已由 root 非作者写后核验通过；未复现实验。

- `SF-2026-ARXIV-2604-20937`（Experimental）：[SToP v1](https://arxiv.org/html/2604.20937v1)，Daily 2026-04-24；§3、§4 Eq4–6、§5.1–5.4/Tables1–5及 naive sink 对照。采用累计 attention proxy 的软排名惩罚与相似性分责，不采持续高值或无用 token 真值；两7B模型/32帧/固定保留率、质量反例与未披露 runtime/SLO 保留。GPU 原披露字符串“NVIDIA GeForce A6000 48GB”不据此修补设备身份。6分缺口深入；apr20及root必要 source→实际 owner 采用通过；实际正文与相邻衔接写后非作者复核通过（root），未复现实验。

- `SF-2026-ARXIV-2604-09687`（Experimental）：[Grid2Matrix v1](https://arxiv.org/html/2604.09687v1) §2.3/3.1–3.2/4.2/5.1–5.2。采用encoder可读、融合可访问、输出可表达的诊断分责；1024patch对照不等probe/decoder容量相同，不证压缩或对齐唯一因果。合成网格、监督/训练成本与通用语义接口共存。apr01必要源→实际owner采用通过；真实正文及相邻衔接已由apr01非作者实际写后通过，未复现实验。

- `SF-2026-ARXIV-2604-15383`：[Temporal Contrastive Decoding v1](https://arxiv.org/html/2604.15383v1)，Daily 2026-04-20；§3.1–3.4/Eq1–9、§4.2–4.6、AppendixA/B Table7。只采用慢时间尺度参考、门控与decoder可见性条件；waveform/state blur不合造等价实现、speech/分离架构反例与prefill2.04×保留。apr02必要source→当前owner独立采用通过；已实际写入正文，root实际正文与相邻衔接非作者写后核验通过，未复现实验。

- `SF-2026-ARXIV-2604-17087`：[exact-v1](https://arxiv.org/html/2604.17087v1)，Daily 2026-04-21；§3.1–3.3/Algorithm1、Table1–2/5。只补同一 visual selector 的构造/训练/部署输入与成本，不误报已有特权监督原则缺失；gold response loss 非视觉真值，dense 退步与 loss 消融保留。apr02 必要 source→当前 owner 独立通过；实际正文及相邻衔接写后非作者复核通过（root），未复现实验。

- `SF-2026-ARXIV-2604-16479`（Experimental）：[exact-v1](https://arxiv.org/html/2604.16479v1) §4.1–4.3 Eq5、§5 Tables1–4。训练频带支持与 decoder 适配分责；不把频率能量当语义或生成收益保证，部分重建/生成退步与额外训练保留。root及apr02必要源→owner采用通过，实际正文及相邻衔接写后非作者复核通过（apr02）；未复现实验。
- `SF-2026-ARXIV-2604-16462`（Experimental）：[exact-v1](https://arxiv.org/html/2604.16462v1) §3、Table2、AppA Eq8–11。视觉更新与文本读K/V分责；LLaVA/Qwen策略反证、OCR完整读取与非免费执行保留。root及apr02必要源→owner采用通过，实际正文及相邻衔接写后非作者复核通过（apr02）；未复现实验。
- `SF-2026-ARXIV-2604-16503`（Experimental）：[exact-v1](https://arxiv.org/html/2604.16503v1) §3.3 Eq2–4/Fig5、§6.2/§7.2。零输出投影只保持初始forward，pre-text共享K/V与post-video Q是受限接口分支；联合消融不证明单一因果或全Attention免费。root及apr02必要源→owner采用通过，实际正文及相邻衔接写后非作者复核通过（apr02）；未复现实验。

- `SF-2026-ARXIV-2604-14016`（Experimental）：[exact-v1](https://arxiv.org/html/2604.14016v1) §4.2–4.3 Eq1–11/§5。projector 输出混合与 LoRA delta/输入二阶统计累积分责；完整局部二次目标的等价不延伸全网络，λ/截断/特征漂移与额外状态成本保留。LLaVA-1.5/InternVL、LoRA16及受限任务，不采用全切片胜。root必要原文/实际owner独立采用通过，实际正文及相邻衔接写后非作者复核通过（root）；未复现实验。
- `SF-2026-ARXIV-2604-13715`（Experimental）：[exact-v1](https://arxiv.org/html/2604.13715v1) §2.1 Eq1/§3.2 Table3。冻结数字语义初始化时间 token+接口SFT，不让 RoPE 等同物理时间；25Hz、0–30s/.04s网格、随机初始化负例及输入/训练成本保留。Qwen2-Audio/Qwen2.5-Omni7B，不能推长音频/生产SLO或传感器真值。root必要原文/实际owner独立采用通过，实际正文及相邻衔接写后非作者复核通过（root）；未复现实验。
- `SF-2026-ARXIV-2604-13938`（Experimental）：[exact-v1](https://arxiv.org/html/2604.13938v1) §3.2 Eq3–8/§4.4 Table4。reference累计坐标与target pose网格分责，DSM不是一般完全解耦；数据/检索/训练成本与非全面质量优势保留。FLUX1-dev/LoRA512/8H200、有限身份/pose对照，不采用物理状态真值。root必要原文/实际owner独立采用通过，实际正文及相邻衔接写后非作者复核通过（root）；未复现实验。

- `SF-2026-ARXIV-2604-15086` — [ControlFoley v1](https://arxiv.org/html/2604.15086v1)，Daily `2026-04-17`。采用 §3.3 的参考timbre/目标时间身份分责；Table9为双条件组合消融而非单模块同步因果，L0与主观样本限制保留。复用 `V3_FINAL_BATCH_INDEPENDENT_AUDIT.md` 15086必要原文/真实owner PASS；root已实际顺读正文与两侧/复用有效必要证据后写后独立PASS；真实整合，本批章锁释放。

- `SF-2026-ARXIV-2604-13313`（Experimental）：[exact-v1](https://arxiv.org/html/2604.13313v1) §2.3 Eq1–5/§3.2–3.3 Tables2–3。采用 hard/easy 梯度概率质量分配的条件分支，正例概率也改变；concreteness 为代理，保小增量及通用切片退步、生成与训练成本。ViT-B/32、单H200、batch1024；不推普遍表示收益。6分缺口深入；root 必要源/owner独立采用通过，实际正文写后待非作者核验；未复现实验。
- `SF-2026-ARXIV-2604-13403`（Experimental）：[exact-v1](https://arxiv.org/html/2604.13403v1) §4.1–4.2/§5.1–5.3。示例label中层grounding与query访问分账、熵选层后λ注入并renormalize；uniform干预不是唯一原因证明，持平与调参成本保留。Qwen2.5-VL7B/32B、Gemma3-12B/27B、4-shot/三seed，生产SLO Not Disclosed。6分缺口深入；root 必要源/owner独立采用通过，实际正文写后待非作者核验；未复现实验。
- `SF-2026-ARXIV-2604-13432`（Experimental）：[exact-v1](https://arxiv.org/html/2604.13432v1) §3.1/§3.3及主表。batch OR保留+取消融合列、存映射散布恢复非信息逆；不同层/精度/batch、质量与映射成本保留。A100分类与3090视觉编码等配置分开，不混kernel/端到端收益。6分缺口深入；root 必要源/owner独立采用通过，实际正文写后待非作者核验；未复现实验。

- `SF-2026-ARXIV-2604-12358`（Experimental）：[exact-v1](https://arxiv.org/html/2604.12358v1) §4.1–4.2/§5.3–5.4。采用 decode-stage 备用表示、短期 union 与回归预算的状态责任；拼接局部 softmax 非全局概率，不采用无损历史恢复或全面净加速。root 必要源/owner 与实际正文及相邻交接写后独立通过，未复现实验。
- `SF-2026-ARXIV-2604-12506`（Experimental）：[exact-v1](https://arxiv.org/html/2604.12506v1) §2.2/§3.2/§5.2 与 Appendix F。采用训练目标覆盖声学维度的条件分支；不采用 JSON 因果解耦或零 trade-off，标签/格式/预算混杂及 ASR 代价保留。root 必要源/owner 与实际正文及相邻交接写后独立通过，未复现实验。

- `SF-2026-ARXIV-2604-12012`（Experimental）：[exact-v1](https://arxiv.org/html/2604.12012v1) §3.1–3.5、§4.1–4.3/Tables2–4。masked student view 保留、visible+masked 直接监督；head-only EMA 保留 projector teacher，外部 contrastive 信号与 shared-head 不稳定限制。116M WebLI、ViT-g、512 TPUv5约两天及两阶段分辨率/批量；冻结encoder九任务二十数据集，不采用全切片胜或完整因果归因。6分实际缺口深入；必要源/owner非作者复核通过（apr02），实际正文及相邻交接写后非作者复核通过（root）；未复现实验。

- `SF-2026-ARXIV-2604-09244`（Experimental）：[exact-v1](https://arxiv.org/html/2604.09244v1) §4.3–4.4/§5.1–5.3/Table3。首步不剪、窗口/EMA平滑模态与语义 salience、候选融合；Table3 S1+S3 62.2<不剪70、S2+S3 71.5是该组合消融，另Table2四任务50%配置47.5<不剪48.8，不能混成无损保证。冻结MLA、RLBench四任务、A100-PCIE40GB/Xeon6348，precision/batch/生产控制SLO Not Disclosed；5分真实gap深入，必要源/owner非作者核通过（apr03），实际正文/相邻论证写后非作者复核通过（apr03）；未复现实验。

- `SF-2026-ARXIV-2604-09429`（Experimental）：[exact-v1](https://arxiv.org/html/2604.09429v1) §3.2–3.5/§4/Limitations。raxel=d+o三通道、coarse H/2×W/2、canonical reference、shared videoVAE与DSCA；Wan2.1T2V14B+6B ray branch，RealEstate10K/DL3DV metric-scale、480×832/12FPS。Procrustes/center principal point、Plücker codec混杂、动态场景与cycle非外部真值边界；硬件/precision/生产SLO Not Disclosed。6分真实gap深入；必要源/owner非作者采用核通过（apr03），实际正文/相邻论证写后非作者复核通过（apr03）；未复现实验。

- `SF-2026-ARXIV-2604-09332`（Experimental）：[exact-v1](https://arxiv.org/html/2604.09332v1) §3–5.3、Tables1/4/5/7。冻结Whistle预训含Tatar，20h配对适配不再FT encoder；英语对照encoder recipe不同。显式phone/wordboundary与continuous projector比较不是减token保证（113→125）、未见语言泛化或完整声学保真。Qwen3-1.7B/8B、Libri960，8A800训练recipe不作为通用推理时延。5分长期机制缺口深入；必要来源/owner准入非作者核通过（apr03），实际正文/相邻论证写后非作者复核通过（apr03）；未复现实验。
- `SF-2026-ARXIV-2604-09364`（Experimental）：[exact-v1](https://arxiv.org/html/2604.09364v1) §5–7、full-sequence patch定义与Limitations。九模型×100合成反事实、三7B～8B局部SAE steering；MAC仅heuristic，last-position阴性不排除sequence分布介导，steering不全面增益。float16/bfloat16、至多4H200/device_map auto；不是开放图像truth或生产SLO。6分长期机制缺口深入；必要来源/owner准入非作者核通过（apr03），实际正文/相邻论证写后非作者复核通过（apr03）；未复现实验。
- `SF-2026-ARXIV-2604-09425`（Experimental）：[exact-v1](https://arxiv.org/html/2604.09425v1) §3–7，六VLM的跨层替换、实际token删除、single/multi-token协议与LoRA恢复。几何稳定/替换稳定不等删除无损，caption teacher相似非人类准确率，部分短答案也退步；硬件/precision/生产并发SLO本次必要证据Not Disclosed。5分长期机制缺口深入；必要来源/owner准入非作者核通过（apr03），实际正文/相邻论证写后非作者复核通过（apr03）；未复现实验。

- `SF-2026-ARXIV-2604-08065`：[PEARL exact-v1](https://arxiv.org/html/2604.08065v1)，已读 §3.1–3.8 双前向、预测 token、stop-gradient/辅助目标和部署撤除，§4/Appendix C 轨迹覆盖及任务退步。仅采用训练期轨迹表示目标与推理期执行分离；不把隐藏表示视为物理状态或工具执行证明。V2 2+2+2=6，长期知识缺口深入；root 已独立核必要原文与实际两段，通过；两段已移至时间/provenance 交接之前，未复现实验。

- Symbiotic-MoE（Status: Experimental，SF-2026-ARXIV-2604-07753）：[exact-v1](https://arxiv.org/html/2604.07753v1) §3.2–3.3、§4.3/Table2/Figure6、Appendix B/C。采用 inherited expert/router 分组与 warmup forward-sharing/backward-shielding 的窄机制；不采用知识完整保存、普遍最优 96/32 或模态利用率即负载均衡证明。Hunyuan-A3B30B、256H20、global batch2500/约2Mtoken、500warmup、专有数据3:3:2:2；部署precision、并发/SLO未披露。作者必要源与实际正文已核，待 root 非作者写后复核；未复现实验。

- `SF-2026-ARXIV-2604-06871`（Status: Experimental）：[exact-v1](https://arxiv.org/html/2604.06871v1) §3–5/Algorithm1/Tables1–2/Limitations 支持语音 feature 压缩的层位置、局部 lookback 与净成本边界；word-alignment oracle 是诊断工具而非部署输入，细声学 fidelity 未证明。必要原文、实际正文及相邻衔接的非作者复核通过（root），不代表整日报验收。

- `SF-2026-ARXIV-2604-07467`（Experimental）：[exact-v1](https://arxiv.org/html/2604.07467v1) §2–4 支持冻结 SSL features 的量化/元音 phone-tone probe 对照；Mandarin 为170小时/400 speakers，Yorùbá 为93小时/单 speaker。帧级 LSTM 与 segment logistic probe 不同，RVQ 层数及组合容量不等于统一 bitrate；依赖 forced alignment，不含 Mandarin tone sandhi 或端到端 TTS/LLM 生成验证，不能外推所有 prosody，未复现实验。

- `SF-2026-ARXIV-2604-03414`（KiToke；Experimental）：[exact-v1](https://arxiv.org/html/2604.03414v1) §3.2–3.4/4.1、Tables4–6/B.1 支持 kernel-redundancy pivotal sampling 与 content-interval merge；10 seeds/CIs 与联合消融不证明普遍无损。LLaVA-OneVision32帧6272tokens、LLaVA-Video64帧、Qwen3VL至128帧及A100，压缩13.1ms+LLM53.1ms而非只报后者，10%保留58.2弱于59.1；precision/batch/concurrency/SLO未披露，未复现实验。

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
