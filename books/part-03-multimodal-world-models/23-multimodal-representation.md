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

显式 instruction 的意图由用户提交；把阅读时的 gaze 作为辅助输入，则先增加了一层可错的意图推断。相同 fixation 可以被聚合为高密度句子的文本子集、保留到词位置的视觉 heatmap，或在短时间窗提取统计特征、分类后再汇聚到句子；这三条路径保留的信息和下游接口不同，不能把“都用了 gaze”当成同一条件。应绑定眼动原坐标、文本布局、时间窗、聚合规则与 consumer identity，分开观察在哪里停留和系统认为用户想要什么；派生 intent 只拥有 proposal 权限，不替代用户明确目标。<!-- source-family:SF-2026-ARXIV-2601-17676 -->

这种隐式输入减少显式表达的负担，却新增设备校准、layout drift、mind-wandering 与粒度失配。[有限阅读摘要实验](https://arxiv.org/html/2601.17676v1)中，句级 density 的评价更贴近句子选择，而词级 heatmap 的部分 lexical 指标改善不等于 semantic 指标显著；同一模型的自评也不是独立意图真值。10 人指定主题与静态眼动设备的结果不授开放用户心理识别，显式 prompt 在主观总体偏好仍有优势。表示不稳定、用户需要准确控制或系统无法解释推断时，保留原文、显式 instruction 和澄清路径；新增信号应作为可撤销辅助，而非由传感器直接签发任务目标。

由同一个输入派生另一种模态，还要分开“表示更容易被读取”和“取得了新环境信息”：把文本送入 TTS，再由 speech encoder 提供辅助表示，会引入生成模型的 prior、声学形式与计算，但没有重新观察原说话者或现场。[受限翻译对照](https://arxiv.org/html/2602.21646v1)中，text+synthetic speech 与 text+authentic speech 的两个平均指标相近且都高于 text-only，支持该模型的表示替代，不证明所有语音信息都仅来自文本或合成 prosody 等于原声。应保存原 text、TTS/encoder与配对身份，分别评价任务收益、声学信息损失与真实新增 observation；派生模态不能作为独立事实源。TTS、speech encoding、额外 token/训练和自筛选费用仍需结算，部分语言也有指标反退；text 已足够、现场声学不可丢或表示回归时，保留 text-only、原始语音及专用声学接口，而不以多一个模态名称认证独立证据。<!-- source-family:SF-2026-ARXIV-2602-21646 -->

把数值序列画进固定 canvas，也必须先检查容量而不是只检查 shape。设序列含 $N$ 个变量、周期为 $f$、编码总长度为 $L$，将每个变量按周期折成 grid，再分配到 $H\times W$ 图像的纵向 band；避免渲染时下采样至少要求 $H/N\ge f$ 与 $W\ge L/f$，其中 $L$ 包括待补全的区域。分辨率不足时，被合并的时间细节已经在输入接口丢失，不能指望更强的生成模型恢复；提高分辨率则增加视觉 token 和计算。[TimeOmni-VL v1 §3.1/4/5](https://arxiv.org/html/2602.17149v1)还用 median 定位、MAD 与标准差混合尺度及 tanh 压缩缓解 spike 和近零 MAD 的相反失真，但反变换依赖原尺度、压缩参数及变量/周期布局；有限像素精度和饱和区并不提供浮点 lossless 保证，零尺度仍须单独处理。这些元数据应随 codec identity 保留，是接口设计边界而非作者已验证的通用无损实现。其实验只在 valid/extractable 输出上计算指标，联合 CoT 消融又同时改变训练与推理，不能把收益唯一归于表示或推理步骤。周期不稳定、变量/长度超出 canvas 或数值精度不可牺牲时，连续 feature、显式数值接口仍合理；扩大 canvas、切窗或回退时都应重新声明时间范围、信息损失和成本，而非仅维持同一个 tensor shape。<!-- source-family:SF-2026-ARXIV-2602-17149 -->

音频的时间单位也不必固定为 codec frame：冻结的语音表示中，某层 activation norm 的局部峰可以提出可变长度边界，再从另一层汇聚该片段并聚类成离散 unit。边界层与内容层分工会改变 token rate、同一 context 能覆盖的时间，以及语言任务的取舍，不能仅以序列更短选择接口。[ZeroSyl 的有限对照](https://arxiv.org/html/2602.15537v1#S3)使用开发集选择层、峰阈值及滑窗，并用 100 小时语音训练聚类；冻结 encoder 不是零训练，约 52 bps 的 token 熵率也不是可重构音色的 wire codec 成本。其边界 F1 低于所比音节方法，语法收益不伴随所有 lexical 任务收益，不同 SSL backbone 与下游训练预算又限制归因。因此需把边界规则、时间范围和 codebook 一并版本化，按实际任务验收；固定 frame、显式 phone 与连续 feature 仍各有合理条件，不能把可变 unit 当作语言无关、语义纯净或已验证在线的接口。<!-- source-family:SF-2026-ARXIV-2602-15537 -->

## 表示演进：从专用特征到统一协议

### 阶段一：手工特征与专用模型

早期系统为每种 modality 构造不同 feature 与模型。它的优点是接口清楚、任务先验强、成本可控；缺点是跨模态信息只能在应用层晚期拼接，知识难以共享。

### 阶段二：modality-specific encoder + projector

视觉或音频 encoder 先提取连续 features，再通过 projector 映射到语言模型 embedding space：

```text
raw signal -> modality encoder -> projected features -> language backbone
```

当目标以理解为主、数据有限、希望复用成熟 encoder 时，这仍是合理的主流分支。encoder 可以独立优化感知质量，backbone 不必承担 raw-signal reconstruction。然而 projector 也成为信息瓶颈：它必须让连续 feature 适配语言 token 的计算接口，却未必能保留低层细节或支持反向生成。

若已有 English text 与 image/audio 的共同 embedding，却缺多语种模态配对数据，映射也可以只发生在两套 text latent 之间：冻结原 English multimodal encoders 和已有 multilingual text encoder，用相同 English captions 学习从后者到原 English text 空间的小型 map；推理时把其他语言的 text embedding 经该 map 后，与原 image/audio embedding 比较。共同 English 锚转接的是 multilingual encoder 已学到的能力，不是从 English 样本学会未预训练语言，也不把原 modal encoder 改成多语种模型。成立条件包括原 text–modality alignment 可用、caption 域匹配，以及不同语言在 multilingual 空间中的对应关系足够稳定。<!-- source-family:SF-2026-ARXIV-2601-10096 -->

这一分支节省新增模态配对监督，却增加 map 训练、encoder 版本耦合和跨语种回归。M2M 的受限检索使用归一化 embedding 的 MSE 与 batch 结构项，生成则保留尺度并撤去结构项；不能把检索余弦几何直接当 generative conditioning 合同。其合成多语音频测试仍受翻译与 caption 域失配限制，FLUX 的 sentence-level CLIP 接口替换又不能代替 token-level T5 条件，较高 IS 伴随较差 FID 和缺对象。于是要分别验收语言、模态、检索与生成；gap 不可接受时保留原 English encoder、翻译路径或真实 multilingual-multimodal 配对训练，而非由小 map 宣称通用无损迁移。[必要机制与直接反侧](https://arxiv.org/html/2601.10096v1)见 §3–4、§6–7。

当接口从一对 encoder 扩展为多个空间，独立 pair maps 仍易于局部更新，却未必满足往返或多跳一致性。已知同一批样本的对应身份时，可先标准化、必要时降到共同维度，再为每个空间拟合进入共同参考的正交 map；pair translation 由两端 map 组合。成熟的 generalized Procrustes alignment 在这个坐标系内保留几何与 cycle consistency，但不会恢复 PCA 删除的信息，也不会自动改善检索。另一分支在共同坐标上共享一个 residual MLP，让归一化向量靠近跨空间样本共识，并对偏离原方向施加软惩罚；这是以局部几何变形换取任务对齐，不是继续享有正交 map 的精确往返保证。<!-- source-family:SF-2026-ARXIV-2602-06205 -->

共同参考减少独立 pair 接口数，却不让配对数据、标准化、SVD、corrector 训练与回归成本消失。[受限多空间对照](https://arxiv.org/html/2602.06205v1)中，错误 correspondence 与弱 anchor 会使共识校正强化失配；较小平均 drift 或更好绝对检索分数也不证明任意新样本满足硬几何约束。新增 encoder、维度与配对人口须与 map/corrector 共同版本化，分别验收原任务、跨空间检索和往返误差，不从接口数推导总 runtime 为线性或无损兼容。对应不可信、生成接口需要尺度信息或校正回归时，保留纯正交共同空间、独立 pair map、原 encoder 或真实配对适配。

同一坐标map能否从一种模态搬到另一种，还需要更强的接口条件，而不只要求image anchors配对。[一个受限contrastive分支](https://arxiv.org/html/2602.17584v1#S5.SS3)先假设两模型的image–text kernel在指定域与anchor交叉上对全部样本一致、anchor矩阵可逆，再用image rank-one outer products足以span全部对称矩阵的条件，推出同一个isometry。小anchor的拟合误差低不证明这些全域假设；源维度不大于目标时，矩形map只绑定另一模态在map像空间内的projection，不能宣布额外维度也被确定；等维时才获得完整对应。部分可识别空间的分类匹配还要求signal margin大于残余交叉干扰，不能把单点cosine当semantic identity。

实际算法以同图像在两encoder的centered/normalized表示作Procrustes拟合，并保存各模态自己的mean与encoder/map版本。OxfordPets有限对照中，更灵活linear/MLP能提高image点对点cosine却恶化text迁移，说明一种模态的训练误差不能验收跨模态接口；原结果限classification-style semantics，dense ranking、fine-grained decodability和其他模态未建立保证。配对anchor、两encoder forward、均值、SVD及原/迁移任务回归仍计费，固定map也只省适用人口的重编码，不授任意新库无损升级。Kernel或维度条件不可核、域漂移或检索回归时，保留原encoder、逐模态map与真实配对适配/重新编码，不让正交几何代替任务和消费者兼容。<!-- source-family:SF-2026-ARXIV-2602-17584 -->

若目标不是把两个 encoder 接到共同坐标，而是在冻结的 image/text 空间中适配少量有标签的目标域，还可直接改交互评分：把点积换成 image·W·textᵀ，以恒等矩阵初始化 W，随后只训练上三角部分。这保留初始分数，并用结构减少可训练自由度；它是依赖坐标基的监督适配，不是从少量锚点证明全域存在唯一正交映射。上三角矩阵仍可缩放、剪切或变奇异，恒等初值也不保证训练后的角度、长度、语义与原任务不变。

[受限双线性对照](https://arxiv.org/html/2603.08942v1)支持这一小样本评分分支，不支持无损 canonical 恢复。上三角结构在不同初始化与任务下并非总能改善；用维度除过的平均正交误差较小，也可能掩盖单一方向的强放大或丢失，须分别核原任务、目标任务与真实消费者，而不把分类准确率或正负角度分布当硬几何证书。锚点标签、encoder forward/缓存、二次规模矩阵打分、训练与调参、跨任务回归均付费；任务失配、几何漂移或费用不合算时，保留原点积、纯正交 map 与真实配对适配，不由初始化批准默认迁移。<!-- source-family:SF-2026-ARXIV-2603-08942 -->

配对锚点太少时，直接把未配对 image/text 当作确定对应也会放大错误。一条受限分支先在少量真实配对上拟合线性 teacher，再让未配对两侧的 student maps 学习 teacher 给出的 soft optimal-transport 关系，并保留配对监督；它迁移集合级关系，不把每行 argmax 认证成新配对，也不证明 teacher 的几何就是语义真值。[SOTAlign 的必要对照](https://arxiv.org/html/2602.23353v1)支持该接口，但极少锚点仍失败、域失配仍有影响，充分配对上界也更强。两 encoder、teacher、Sinkhorn 迭代、大 batch 和训练均付费；主梯度式与附录使用的温度分母不一致，因此这里不采用统一梯度或消除内存瓶颈的保证。弱锚点或迁移质量不合格时，保留真实配对、原 encoder 与简单 map，不让 soft relation 冒充缺失观测。<!-- source-family:SF-2026-ARXIV-2602-23353 -->

共同坐标仍要求跨空间的样本对应关系；若两个数据集合各自只有一组真实模态配对，且只共享 pivot 模态，就不能把它们拼成同一批完整观测。[另一条受限训练分支](https://arxiv.org/html/2602.06451v1)从每个 batch 的 pivot 表示计算 Moore–Penrose 伪逆，构造跨模态与跨数据两条 pseudo-embedding 路径，再用两路结果的差异约束接口并结合对比学习。伪逆运算停止梯度，却在每个 batch 重新计算；pseudo embedding 是训练中的缺模态代理，不是恢复出来的 raw signal，也没有获得缺失观测的真值权限。原文矩阵记号的行列与 batch 对应仍须由实现核验，这里只采用双路径约束的接口，不发布其公式为已验证的可执行转换。<!-- source-family:SF-2026-ARXIV-2602-06451 -->

该分支并未取消数据集合内部的真实配对，也不能保证病态 pivot 或人口偏移下的逆映射稳定、无偏。冻结 encoder 后的 projector 线性探测与 LoRA 适配、分阶段损失、batch 伪逆及检索回归均有成本；作者局部消融中联合训练优于单独阶段，因而不能把收益全归给双路径约束，完整硬件、数值条件与总成本也未披露。所测检索 mAP 和 pseudo feature 可视化不证明生成质量或真实缺模态重建，稀有模态仍有低质量切片。对应身份、数值条件或新任务回归不可靠时，保留原 encoder、纯共同 map 与真实配对适配，不让训练代理替代新人口的实际任务验收。

因此，最终回答错误不能直接归因于“视觉 encoder 没看见”。可以先固定 encoder，用浅层 probe 检查细节是否仍可读，再分别检查融合后的语言侧是否能访问这些信息、输出协议是否能表达它们；可恢复、可访问和可表达是三种不同能力。受限网格实验中，同样数量的 patch 可保留浅层读出所需信息，而完整模型仍无法正确输出，网格密度、对象跨 patch 边界及 readout 容量也会改变结果。它支持分段定位接口瓶颈，不唯一证明 projector 压缩、对齐或蒸馏造成失败。<!-- source-family:SF-2026-ARXIV-2604-09687 -->

新增 probe 要支付监督、训练和容量成本，也不能证明原模型已经能自行调用被读出的特征。[Grid2Matrix](https://arxiv.org/html/2604.09687v1) 的冻结 encoder、合成网格、cell/整图准确率与浅层读出仅限定这条诊断分支，不是通用视觉能力证明。细粒度坐标或结构化输出确实重要时，可比较专用 readout、显式坐标接口与原语言输出，并对最终任务重新验收；通用语义任务、诊断数据不具代表性或接口成本过高时，成熟 encoder + projector 仍合理，不能用一个 probe 结果否定它。

可读性诊断还可以检查模态特有方向在语言入口是否真正有用：对 adapter 输出作 covariance 分解，以同方向的文本方差作为参考，选取候选 modality-specific directions，再在 decoder 输入删除这些方向并测量任务变化；另用非转录目标微调 decoder，检查原有音频信息能否被重新使用。它把“方向存在”“当前 decoder 使用”“目标适配后使用”分成三项，不由低语言 loss 或高 probe 分数推断语义已统一。[Modality Collapse 的必要实验](https://arxiv.org/html/2602.23136v1)中，随机删除也能降低部分 loss，matched 方向人口并不完全对称；情绪目标适配改善不证明所有特有信息都被浪费，改变 encoder 或任务也不是单一训练目标的因果控制。covariance、投影消融、标签与 LoRA/读出训练都付费。原文条件平均的 GMI 表达存在可构造反例，这里不采用其“可访问信息上限”或梯度保证；目标、人口或旁侧能力失配时，保留原输入、专用 encoder/readout 与真实非文本监督，而不按方差比直接裁掉模态信息。<!-- source-family:SF-2026-ARXIV-2602-23136 -->

视觉 encoder 的全局任务成功还可能掩盖聚合接口与局部消费者的错配：image-level 监督与全局混合可以让背景 patch 带上全图语义，因此 CLS–patch 相似度高不等于该 patch 含目标对象。[ViT 的受限 masking、训练轨迹及聚合对照](https://arxiv.org/html/2602.22394v1)中，分类准确率上升而单对象 Point-in-Box 几乎不变；移除高相似度 patch 未必伤分类。基于滤波前后变化选取 patch 聚合的分支能改善局部任务，但完整 top-K 又可退步，不能把去高范数或加 register 当充分纠偏。Lazy aggregation 是作者的机制假说：更大 patch 同时改变分辨率，窗口 attention 改善定位却损分类，都不足以唯一隔离因果。额外滤波、选样与局部标注评价有成本，应分别验收全局识别和 dense grounding；局部改进损伤原任务或预算不合算时，保留原 encoder、专用 dense head 与真实局部监督，而不由分类成功批准无损空间语义。<!-- source-family:SF-2026-ARXIV-2602-22394 -->

如果浅层 readout 已能读出某类细节，还可在不重训 encoder 的条件下重组既有分类头。对 mixed-granularity 标签域，把同一粗类的细类 weight 均值作为 base，将差向量作为 modifier；用文本检索 modifier，或用既有类别/weight 对训练 text→weight map，再以 `w_s=w_c+v_m` 构造新子类头并替换目标粗类。这里迁移的是已有表征中的区分方向，不是凭文本补造 encoder 缺失的视觉信号，跨类别解耦只是条件假设；zero-shot 也仅指无需新子类视频，不等于没有原训练和标签监督。[受限视频分类对照](https://arxiv.org/html/2602.16545v1#S3)支持这条接口，却有新视觉区别、对象计数和成功状态的失败切片。其 locality 是非目标正确数的新旧比值，不能证明逐例预测不变；从分类机制推断，即使其他旧头冻结，新增 logits 仍可能参与竞争。因此目标泛化与非目标逐例稳定须分别验收，独立 split 的平均也不认证多次累积编辑。字典、文本 map、少量标注 head 训练和回归验证都有费用，部署时延/SLO 未披露；方向迁移或质量失配时，保留原粗标签、外部 gated readout 或少量标注的 isolated head，而不是把冻结 encoder 当作无损编辑保证。<!-- source-family:SF-2026-ARXIV-2602-16545 -->

若选择共享词表作为空间 readout，还须检查监督是否强造了不存在的互斥关系：一个 vision patch 可以同时包含多个对象、任务或粒度标签，单一 one-hot Softmax 会迫使这些目标竞争。一条受限分支对 vision token 使用 multi-hot、逐词表项 Bernoulli 监督，再在当前类别域读取 raw logits；多子词类别取均值、恢复空间网格后生成 dense map。有效标注域、正例与负例人口必须分别声明：只在 valid indices 中选择高预测分数的 top-k 负例、分别平均正负损失，不等把全部无标注词表项认证为真负。[DenseMLLM 的受限对照](https://arxiv.org/html/2602.14134v1)支持这项训练目标与 readout 接口，而非共享词表已经获得所有视觉真值。完整词表计算、类别选择、空间上采样和多阶段训练仍有费用；增大分辨率并非所有指标单调改善，专用 head 也有更强切片。细节、标注覆盖或计算预算不合适时，保留专用 dense head、显式坐标读出或原文本输出，按实际任务比较，而非为“统一架构”强换监督。<!-- source-family:SF-2026-ARXIV-2602-14134 -->

分类接口的监督还可来自当前上下文而非永久 head，但必须区分封闭标签域与开放支持集合。封闭域把检索到的带标签样本提供给生成式读出，应与读取同一支持人口的 adapter/kNN 比较，不能把检索差额全算作 ICL 能力；开放域则先产生类别描述，再 leave-one-out、同步用上一轮标签更新所有样本，避免把当前样本自己的描述直接当支持。后者传播的是派生标签，不是真实类别或可靠伪监督。[受限 Open/Closed-world 对照](https://arxiv.org/html/2602.23229v1)中，随机/初始伪标签上下文可伤 zero-shot，迭代也并非所有模型和粒度都更好；标签 judge 的模板和集合偏差不能替代分类真值。检索、示例编码、额外生成轮次和更长上下文均计费，须保存样本、标签域、更新轮次与读出规则；支持污染、类别漂移或预算不合算时，保留 zero-shot、同支持集的简单检索/adapter 或真实标注 head，不让上下文中出现某标签就认证它。<!-- source-family:SF-2026-ARXIV-2602-23229 -->

正侧 probe 之外，还可做保留场景、移除目标实体的负面对照：先按明确的 detector 类别、confidence 与 mask 规则遮蔽对象，再观察模型是否仍断言该对象存在。若模型反复补出已移除实体，就说明当前输出可能由场景关联支持，而非足够的目标视觉证据；这比仅检查完整图像的答题分数更能定位“context prior 仍在生成断言”的失效切片。它不唯一识别语言先验的内部因果路径，也不因 detector 未再检出而证明所有轮廓、反射或关联线索已删除。<!-- source-family:SF-2026-ARXIV-2602-10425 -->

[MOH 的有限对照](https://arxiv.org/html/2602.10425v1)按模型失败再筛样本、跨模型取交集，因此该集合的对象断言率不是自然图像总体发生率；直接 yes/no 与自由描述也应分别计量。遮蔽与反复生成增加评价成本，纠偏后仍有残留且 VQA 质量可退步，不能把一份 preference 配方当作零幻觉或无税修复。实际 grounding 需要继续检查原图/遮蔽图 identity、实体移除范围与独立质量回归；任务不能容忍剩余对象风险时保留专用检测、证据不足时拒绝断言及人工复核，而不是让场景熟悉度替代视觉支持。

若空间证据仍在表示中，却在语言侧早层残差读取时过度集中，还可尝试不重训的局部干预：先用诊断 pass 找出高 attention 的视觉位置，再在第二次 forward 的早层将其 hidden state 按空间邻接加入周围位置，同时缩小源位置。[SCR 的受限对照](https://arxiv.org/html/2602.22469v1)支持这条 two-pass inference 分支，不是训练时的梯度 credit 分配，也不是严格守恒的搬运；邻居获得的加法会放大总表示量。低 entropy 与对象幻觉相关不能认证 grounding：随机选择 source 仍有较小收益；另加 Gaussian noise 虽增 entropy 却恶化幻觉，表明“更均匀”本身不是充分条件。边界 patch、相邻小对象和原正确预测仍会受损，部分基线的幻觉指标也更好；额外一次 forward 与 hooks 增加延迟，另行训练的 one-pass 近似不属于 training-free 路径。应绑定层、source/neighbor 规则和干预强度，同时验原任务、对象支持与新增错误；邻接混淆、质量回退或延迟不合算时，保留原 forward、专用检测和证据不足时拒绝断言，不让 entropy 变化取代真实视觉支持。<!-- source-family:SF-2026-ARXIV-2602-22469 -->

局部干预还可以不搬运空间 hidden、不生成派生图像，而在同一 forward 路径比较 early 与 late attention map，把差异作为晚层 visual-position soft-mask 的 proposal。诊断先限定候选 early 层，再按与 late map 的差异选层、对低差异位置软抑制；map/head/layer、位置集合与抑制强度共同定义 sensor 与 consumer hook，attention 差异本身不证明 grounding、唯一因果贡献或 fusion 已在某层完成。对 visual-position hidden 置零也不移除此前已传播到文本位置的全部视觉信息。[受限 LLaVA 对照](https://arxiv.org/html/2601.08151v1)扩大候选层、使用深层或过度 mask 均有退步；软抑制不等物理 token pruning，内部 hooks、map 取得和 attention 计算仍占预算。应分别验任务质量、视觉支持与总执行成本，map 不稳定、过抑制或 hook 预算不可用时保留原 forward 与外部 grounding，而不让热图变化签发视觉真值。<!-- source-family:SF-2026-ARXIV-2601-08151 -->

另一种局部干预不搬运邻接位置，而构造两份派生视图：先以 grounded/null 输出的 JS divergence 触发诊断，在有标注区域的校准集上选择 heads，再按累计 attention 质量形成 anchor mask；分别 inpaint 背景与对象，得到 anchor-only、context-only 的逐层 hidden states，以两者之差修正原路径。最后用全局与两派生视图的分布冲突比调温度；[VLI 的具体公式](https://arxiv.org/html/2601.05159v1)将温度限制在 `[1,2)`，不是任意熵最大化或已校准正确率。校准 heads、mask 与 inpainting 各有身份和误差，attention mask 不因被称为 anchor 就成为经验证的因果区域。<!-- source-family:SF-2026-ARXIV-2601-05159 -->

这种差分的理论也有条件：A.1 Eq15 显式假设对象、背景、语言三个正交的加性分量，A.2 再假设理想 inpainting；在这些假设及 `0<α<1` 下，语言项消去和所定义 SNR 的提高成立，却未证明真实非线性网络满足分解或 attention 必然正确。较强 steering、抽象问题及不聚焦的 heads 仍会退步。GT 校准、inpainting、多路 forward 与 KV 都付费；作者有限延迟表中串行 17.730s、并行 7.823s 对原路径 3.130s，不能称免费修复，并行内存还更高。派生视图破坏语义、质量或费用不合算时，保留原 readout、专用检测与外部 grounding，不让 hidden 差值签发对象真值。

差分方向还可以在生成开始时生产，再缓存给后续步骤消费，而不每步重造派生图像。一条受限视觉分支保留原输入，只为负侧随机剪掉大部分 vision tokens，在首次前向比较原/负输入的浅层 hidden，按层平均差值；后续生成把这个初始方向与当前 hidden 分别归一化，组合后恢复当前幅度，中层另从原图与增强图 tokens 读取 context。原/负输入、采样、层、对应 token 位置和缓存有效期共同定义接口；删 token 改变长度与位置，不能隐含补齐矩阵对齐，更不能因保存幅度就认证语义不变。

[One Token, Two Fates 的有限对照](https://arxiv.org/html/2603.10360v1)支持这条局部分支，但初始差分不是每步的真实幻觉原因。共同语言偏差的消除依赖相同加性分量，剪 token 后的非线性视觉—文本交互和后续状态变化未由这个假设覆盖；增广图也可能改变任务真值。局部对象问答、caption 和消融有收益，也有更强基线切片，单 token 测时不替完整 K 路 probe、编码、驻留、hooks 与调参费用。输入语义、方向有效期、旁侧任务或总预算失配时，保留原 forward、已验证的局部干预与独立 grounding，而不让 cached hidden 差分批准事实或部署。<!-- source-family:SF-2026-ARXIV-2603-10360 -->

差分方向也可以先在校准人口上汇总，而不为每个请求生产新负视图：保持原 caption，不改变它的文字条件，只用错误 caption 引导离线 diffusion 编辑图像；对多个编辑样本的 caption-token hidden 取均值，减去原图表示，再以逐层 SVD 的主要右奇异向量保存一个方向库。推理只对指定层每步 hidden 执行 `h−V_r V_rᵀh`，其中 V_r 的列为所选 r 个正交方向，把昂贵的反事实制备与在线投影消费者分开。这不同于首次请求的局部差分缓存：bank 的有效性现在依赖校准人口、编辑器、caption、LVLM、层与 rank 共同保持兼容。<!-- source-family:SF-2026-ARXIV-2603-10470 -->

差分矩阵的主要奇异方向不自动是自然幻觉的唯一原因，投影正交也不认证保留全部事实语义。[局部物体错误对照](https://arxiv.org/html/2603.10470v1)伴随 rank、扰动强度和图像 noise 敏感；文本与视觉两类 bank 联合还会退步，代理 judge 的高分不能代替独立 grounding。权重不更新仍支付错误 caption 制备、多次图像编辑、features、SVD、搜索与 bank 驻留，在线吞吐不抹掉这些费用。新人口或编辑 artifact 失配、旁侧任务回归或总预算不值得时，保留原 forward、输入特定的受限方向与外部取证，不让固定投影库授予事实发布权。

差分接口也可用于音频，但定位与干预仍是两项责任。在有正确标签的校准集上，先用最后 prompt 位置对 audio tokens 的 attention mass 定位与答题结果相关的 heads；对当前输入再运行原音频与等时长静音两次 forward，在这些 heads 所在层读取同一位置的 residual 差值，按层汇聚后加到最终读出表示。Head 只限定从哪些层取方向，并不意味着直接修改这些 heads 的输出；静音对照提供输入特定的变化方向，也没有把它分解成纯音频事实或唯一因果贡献。<!-- source-family:SF-2026-ARXIV-2603-06854 -->

这条分支可不更新 weights，却仍支付带标签的 head/强度校准、两次前向和 activation 驻留成本。[有限音频问答研究](https://arxiv.org/html/2603.06854v1)显示过强干预会退步，但其成绩表缺少与所述单次计数口径一致的汇总说明；直接 head 干预与最终 residual 干预的位置也不同，不把数值差额认证为独立 layer 因果。换模型、音频域或标签人口后需重新检查方向、任务质量与音频支持；静音改变了非目标因素、方向不稳或成本不合算时，保留原 forward、原模态证据和外部 grounding，不从更大的 listening score 推出答案更真实。

读出所需的信息也未必集中在固定的最后层接口。冻结视觉 encoder 后，可以从多个层分别取 CLS 与平均 patch summary，将这些层级表示作为 keys/values，由一个可训练 query 的 cross-attention 学习任务条件下的融合，再交给分类读出。这分开了两个选择：访问哪些层，以及在每层保留 summary 还是逐 patch 的空间细节；它不是重训 backbone，也不由 attention 热图证明原模型已经因果使用了某层。Layer、token 类型、normalization、维度补齐、preprocessing 与 readout revision 共同定义表示接口，不能由末层某个 probe 失配宣布所有最后层表示不足。

多层 summary 可减少读出端需要消费的空间 tokens，却增加中间特征提取/缓存、监督训练、容量与调参成本；平均 pooling 还可能丢掉定位线索。[受限 ViT 多任务对照](https://arxiv.org/html/2601.09322v1)中，细空间任务有末层 patch attention 更强的 slice，部分任务也更适合简单线性融合；主实验单 run 与局部 seed 检查不能授任意配置稳定性，单 query 融合也不采用文中二次复杂度宣传作为实测加速。任务只需末层语义、缓存成本过高或融合过拟合时，保留原 last-layer readout；需要空间细节时保留 patch-level 接口，并以相同训练/搜索预算重新验收。<!-- source-family:SF-2026-ARXIV-2601-09322 -->

如果 consumer 不是一个分类 readout，而是语言 decoder 的多个层，访问哪层视觉表示还须与“在哪个语言层、更新哪些 token 位置”共同定义。一个可比较的分支保留原 projector，为不同视觉 producer 层配置低秩适配，再在指定 decoder 层由视觉特征与当前 hidden state 的摘要生成门控权重；按该接口的约定，残差更新发生在 visual-token positions，不把任意文本位置改成直接视觉 cross-attention。它将 producer 层选择与 consumer 层/位置耦合，而不是仅把多层 summary 融合后送给唯一分类头；门控权重也不证明浅层必负责纹理、深层必负责推理。<!-- source-family:SF-2026-ARXIV-2601-10710 -->

这条分支增加中间特征驻留、逐层适配、门控计算与监督训练成本，不能从少量新增参数推导端到端 SLO。[受限跨层注入对照](https://arxiv.org/html/2601.10710v1)的 0.5B、半量指令数据消融中，仅增加多层投影收益很小，结合门控的局部结果更好；完整 projector 调优却以更大参数容量获得更高分，不能把全部差异归因接口。注入密度也不单调：中等密度可弱于稀疏配置。于是要同时版本化 producer 层、projector、consumer 层、位置 mask 和训练预算，并分别验收任务质量与执行成本；任务只需末层语义、训练或驻留预算不足时，保留原末层 projector，分类任务也仍可采用前述多层 summary readout。

消费端还可逐 token 决定“额外计算读什么”，而不是一律增加视觉注入层或输出推理长度。[GPRO 的受限接口](https://arxiv.org/html/2601.04442v1)在交替的 FFN 层放 controller，读取当前 hidden、原始输出 entropy 和图像特征，选择原 FFN、以视觉特征为 keys/values 的 cross-attention，或读取当前 hidden 与近期文本 context 的 MetaTrans。后两者分别增加感知重读和上下文变换，不是同一种预算动作；controller 输入、执行层与三路算子共同决定表示接口。teacher 的失败归因只提供监督代理，不识别模型内部唯一因果，raw entropy 及 `1−U` 奖励也不自动具有正确率校准资格。<!-- source-family:SF-2026-ARXIV-2601-04442 -->

内部多算并不由较少输出 tokens 抵免费用：受测 7B 的 MathVerse/MMVet 低于对应 FAST，MM-Vet 切片的平均 response 长度也有 118.8 对 114.1 的反侧，不是跨任务平均。作者训练配置用 8 H100、约 600 GPUh，还需归因标注、controller 和各算子驻留/执行；局部准确率与文本长度不能认证端到端省时。应分别验三路调用、任务质量和总执行账，视觉或 context 代理失准、训练/延迟预算不足时，保留固定接口、原 FFN 与原模型，而不是让路由选择自证 reasoning 有效。

是否读取额外模态，也可以在整份 decoder 输入上作决定，而不只在内部层选择算子。一条受限视觉分支保留 2D 主流，把几何 encoder 输出经独立 projector 编成带边界的另一段 tokens；模型先只读图像与文字，发出几何请求信号后，再追加该段进行第二次推理。训练标签由同题在有、无几何条件下的答题差异构造，因而请求表示指定模型的监督决策，不是场景真实需要几何的证书；预测几何也仍是估计。Encoder/projector、边界与请求 token、标签来源和两次输入协议须共同版本化，不能把独立通道等同于原模型不变。

[GeoSense 的有限对照](https://arxiv.org/html/2603.10370v1)支持按需输入分支，但方向、旋转与动态任务仍有退步，部分通用能力指标低于原模型；共享 LLM/projector 训练后，即使未请求几何，也没有原权重路径的精确保留保证。较低触发比例不等于全费用下降，几何编码、首次判断、第二次推理、双条件标签制备与回归均付费，未披露的特征延后计算和 cache 复用不能补造。请求失准、几何域失配、能力或总预算回退时，保留原 2D 模型、已验证的固定几何输入或原内部路由，而不以自感知概率批准新模态与部署。<!-- source-family:SF-2026-ARXIV-2603-10370 -->

当两个 encoder 保留的是不同类型的 cue，融合方向也未必应使用相同算子。低层 artifact patches 高度相似时，以它们作为 keys 的普通 cross-attention 可能把权重摊平；一条任务条件分支先将两空间映成 fake/real scores，以负 JS divergence 为 Sinkhorn cost，让 artifact→semantic 传输偏向两路判别不一致的区域，再以普通 cross-attention 完成 semantic→artifact 的条件读取。这是不同方向承担不同任务目标，不是最小语义距离对齐；fake heads、prompt、transport marginals/iterations 与两路 encoder 都须绑定，disagreement 与 attention/flow proxy 不认证真实伪造或内部因果。[有限生成图像检测对照](https://arxiv.org/html/2602.21716v1)支持 adapter 分支及参数匹配的局部收益，但 full fine-tuning 仍可更强、传输/再数字化后仍明显退步；参数匹配不等 FLOPs 或壁钟匹配，额外 encoder、预测头、Sinkhorn 和 adapter 训练均付费。任务代理失准、cue 分布变化或完整成本不合算时，保留原 encoder+projector、简单 concat 与已验证的 fine-tuning，不把非对称融合授为通用鲁棒性保证。<!-- source-family:SF-2026-ARXIV-2602-21716 -->

视觉配置本身也是诊断变量：动态 tile/grid 的离散选择可能使相邻一像素的 resize 改变完整处理配置，而不是只改变一点图像内容。回归应分别控制“同 pixels 换配置”和“同配置换 pixels”，保存 preprocess/grid identity，再看原任务的证据访问与答案；答案更稳定不等更正确，不能把配置效应直接归因于 encoder 丢失信息。局部 target knockout 配合相同数量 non-target 删除，可检验所测路径是否依赖目标 view，但不能识别所有模型共同的内部原因。

[Reading Right, Answering Wrong 的受限对照](https://arxiv.org/html/2609.25770v1)支持这组边界测试；累计多条件、annotation-assisted reading 的可读分母不是全部任务自主成功，固定低/高分辨率也令部分模型 accuracy 退步。额外图像 tokens、标注与多次调用均有成本，模型/样本/多比较范围须保留。配置不稳定或目标 cue 不可取得时，回读完整原图/原文、保留 native preprocessing 与独立任务质量 Gate，不把 guided recovery 作为通用修复保证。<!-- source-family:SF-2026-ARXIV-2609-25770 -->

问题措辞更稳定，也不证明模型真正依赖了图像：先限定语义等值的 paraphrase 人口，再分别测答案稳定、text-only/替换图像后的依赖变化与原任务 accuracy；拒答、不可解析输出和改了真值的替换图，不能混入同一个成功分母。依赖变化只是诊断，不直接认证正确 grounding。[受限 yes/no VLM 对照](https://arxiv.org/html/2602.21428v1)中，更低 flip 可伴更高 text-only agreement；单模型、单层 SAE feature 的 delta patch 与 activation-matched 随机 feature 控制支持局部干预，但 clamp 降低 flip 的同时也降低 accuracy。因此更稳与更对必须分开验收，feature 名称或 attention 热图不授唯一内部因果。额外 paraphrase 生成、白盒激活/SAE、patch 驻留与质量回归均计费，自动语义筛选也不替代人类等值校验；新人口、模型或副作用未通过时保留原编码/输出路径与完整原图，不能把局部稳定性修复升级为通用正确性或部署保证。<!-- source-family:SF-2026-ARXIV-2602-21428 -->

输入变体还可从诊断人口进入同一 decoder 的逐 token logits 合成：真实图像配多个问题变体，对每个 vocab 位置取最大 logit；原问题另以真实图像减去多个 dummy-image 输出的平均 logit，形成视觉差分，再按两套温度相加，并以第一路的相对 logit 门槛限制候选。这把变体聚合、视觉差分与 plausibility 支持集分成三项选择，不等于多数答案投票或 hidden 差分；问题改写与黑图/噪声图不天然保持语义，跨 prompt 的 raw-logit 最大值也不对各路任意常数偏移保持不变，必须绑定输入、logit/normalization、温度和门槛身份，不将合成分数认证为同一校准概率或真实因果。[SCI 的有限对照](https://arxiv.org/html/2603.07659v1)中，去掉支持集门槛可明显伤原任务，保留它仍不保证全部任务改善；按同一模型失败及变体响应筛出的 DRBench 人口也不是自然总体，需另验未筛原人口。变体制备、多路 forward、驻留和调参均计费，批处理减少串行时间不抵全部额外成本；变体改变真值、logit 比较失配或质量/预算反退时，保留原图直读、原 decode 与独立 grounding，不用跨变体更一致批准正确性。<!-- source-family:SF-2026-ARXIV-2603-07659 -->

持续接入新任务时，还应把感知接口漂移与语言参数累积拆开处理。共享 projector 成本低、身份简单；任务差异较大时，可以保留各任务 projector，由冻结视觉特征的任务原型对查询加权，混合的是各 projector 的输出，而不是直接平均它们的参数。语言侧则可在固定层输入与任务 LoRA delta 的局部二次目标下，累积输入二阶统计、合并参数增量。前者决定当前样本从哪个感知接口取信息，后者决定历史任务约束如何进入语言层更新；两套状态不能由一个相似度分数代管。<!-- source-family:SF-2026-ARXIV-2604-14016 -->

[受限递归合并实现](https://arxiv.org/html/2604.14016v1)的代数等价依赖固定特征、固定任务增量及可逆的完整统计矩阵，不能推出全网络最优或无遗忘；缩放、低秩截断和后续特征变化都须重新验收。该分支仍需要逐任务调优、保存 projector/原型及二阶统计，完整统计还可能有平方级存储成本。LLaVA-1.5 与 InternVL 的有限 continual-learning 对照并非各任务全面占优。任务差异小或状态预算不足时继续共享 projector，语言侧也可保留独立 adapter 或 replay；采用合并后须分别检查旧任务、新任务与接口版本，不把局部合并公式当端到端能力保证。

若新增模态需要 backbone 内部的适配容量，却必须继续复用旧 embedding 与索引，冻结原权重或把新残差初始化为零还不足以保证旧路径长期不变：训练后新残差可以非零。一个更强但有条件的接口是按模态封装深层 adapter pack，所有 gate 关闭时，hook 在任何 adapter 算术之前直接返回原计算图；单 pack 开启时，其他 pack 不参与该 forward。bitwise 保留还要求原 weights、precision、kernel、运算顺序与 batch 配置一致，而非仅要求最终张量形状相同。gate 绑定的是 encode 入口声明的执行 scope；同样的 RGB 字节可以承载 thermal 输入，不能靠内容自动识别其语义，梯度 checkpoint 的 backward 重算也须恢复相同 scope。

[Modality-Gated Deep Adapters 的有限实验](https://arxiv.org/html/2609.26182v1)支持这种明确绕过的接口，而不是所有输入的自动路由或任意混合模态保证。closed-gate 检查每模态仅一个输入，多 gate 同一 forward 与并发请求隔离未得到验证；单一 backbone 的 audio/thermal 训练又含参数量、loss 和筛选差异，gate-open 的 thermal 分类仍低于原基线。新 pack 要支付驻留内存、训练、入口管理与 scope 回归成本。多模态混合、重算或并发 scope 无法可靠隔离时，应保留 external projector、独立 adapter/model 或原编码路径；旧图精确保留与新模态任务质量是两项独立验收。<!-- source-family:SF-2026-ARXIV-2609-26182 -->

多种 audio encoder 的互补信息也不必先压成同一条流：共同 cross-attention 可以减小入口长度，却可能同时削弱原语音内容接口。另一条分支保留经过既有 adapter 的连续语音主流，只把音乐、环境声等互补 encoder 压成定长旁路，再以明确边界和来源顺序交给同一 frozen reader；也可以把已训练的融合流与主流并列输入，以更长入口换信息保留。Encoder/层选择、时间压缩、旁路 slots、融合顺序、分界 prompt 和各 adapter checkpoint 共同定义接口，不能由维度对齐或更多 encoder 宣布所有声学信息无损。

这种分路用额外表示和 reader tokens 换局部质量：[必要融合对照与直接反侧](https://arxiv.org/html/2603.09556v1)中，共同压缩的语音推理会退步，保留主流及并列分支在部分任务恢复，但环境声、音乐或其他推理切片仍可能更差，训练人口和初始化不同也不能只归融合算子。固定旁路 slots 要加在主流长度上，多 encoder 与更低合计 token rate 不消除编码、adapter 制备、融合、长输出及回归费用。冻结 reader 只在复用原纯文本路径时避免权重变化，不保证新音频前缀无干扰；从文本 metadata 自生成再改写成听觉口吻的 target 仍是派生监督，措辞不能证明 raw audio 真值。应分别验收语音内容、非语音感知、纯文本与总预算；旁路丢细节、源身份不可信或质量—成本失配时，保留原单 encoder、专用 readout 或连续配对适配，不让更自然的 trace 代替 grounding。<!-- source-family:SF-2026-ARXIV-2603-09556 -->

语音理解还可以把“对齐到语言空间”与“显式提供音素/词界接口”分开。在配对语音—文本监督充足时，连续projector保留更多声学信息，也能复用成熟encoder；监督受限时，冻结encoder输出的显式音素序列可以让LLM先消费一个更接近语言符号的接口，而不再只靠少量数据训练连续映射。多个音素候选可保留识别歧义，却也增加输入长度和选择成本；它不是完整声学表示，更不能代替音色、韵律或环境音。<!-- source-family:SF-2026-ARXIV-2604-09332 -->

[受限接口对照](https://arxiv.org/html/2604.09332v1)在同一冻结Whistle encoder、20小时Tatar配对数据下观察到这一分支；该encoder预训练已经含Tatar，不能称为从未见语言的泛化。英语对照的encoder训练recipe不同，也不能把所有收益归因接口。音素BPE序列甚至从113增至125tokens，词界与接口适配可能比序列缩短更重要；词表扩大也会退步。于是选择须同时验收识别误差、语言覆盖、配对监督和下游WER，数据充足或任务需要非语言声学细节时继续保留连续projector，不能把音素路线升级为所有低资源模态的默认答案。

统一 audio embedding 接口也不表示不同 encoder 保留了同一种信息。若后续需要语义内容、说话者或音色，不能先按一个平均榜单选表示，再假定换 readout 就能取回被压掉的信息：[MAEB 的受限对照](https://arxiv.org/html/2602.16008v1#S4)在同一语音数据上观察到语言与性别任务的 encoder 排序反转，监督分类强的表示也未必适合无监督聚类。这支持按目标信息与真实读出协议分别验收，不证明声学与语言信息必然不可兼得；不同模型的原生采样率、pooling 与时长限制仍是条件。训练 probe、维护预处理和覆盖长音频或更多语言都增加成本，小样本 AudioLM 关联也不能替代端到端能力评价。任务明确时专用 encoder 或连续声学接口仍合理，只有经过对应任务检验，才把共享表示交给语言模型消费。<!-- source-family:SF-2026-ARXIV-2602-16008 -->

固定目标任务后，readout 能看见哪些层、具有多少可学习容量，也会改变评价对象。只取最终层的线性 probe 成本低、接口简单，却可能遗漏中间层仍可读的任务信息；读取全部冻结层、学习凸组合与 prototype 匹配，则增加 probe 训练、标注和多层特征成本，分数不能直接视为 encoder 的固有真值。[受限音频 SSL 对照](https://arxiv.org/html/2602.16305v1)还表明，预训练 decoder 承担多少重建负担会改变信息在层间的位置；更强 decoder 与其它训练选择共同变化，不能只由 peak 后移宣布表示普遍更好，fine-tuning 排名也不等冻结表征排名。因此应把 encoder、预处理、层可见性、probe 容量与优化预算一并冻结，用实际目标验收；资源受限或最终层已足够时保留简单 probe，需要完整能力适配时保留经验证的 fine-tuning，不把 learned layer 权重升级为因果解释。<!-- source-family:SF-2026-ARXIV-2602-16305 -->

读出之前的 query-conditioned filtering 也会改变可用证据，而不只是去掉噪声。单事件问题可先用事件时间 mask 抑制无关片段；比较多事件相对运动时，同一过滤却可能删去建立关系所需的联合上下文，重叠事件也不会被时间 mask 真正分离。[受限空间音频对照](https://arxiv.org/html/2602.16334v1)中，thinking 的总体收益与 mask 质量有关，但多选题在更精确 mask 下并未改善，完整输入下的部分题型反而不及不思考模式。于是要联合冻结 query 指向、mask 支持、题型、judge 与思考预算，分别验收目标事件和关系证据，而不能把更多 reasoning 当作输入损失的补偿保证；作者的模拟 stereo 场景、关键词或语言 judge 也不代表真实空间感知真值。训练 grounding、生成中间思考和额外判分均付费；目标不清、联合关系重要或过滤不可靠时，保留完整连续声学输入与无过滤/低预算基线，不让更窄输入的局部收益替代完整任务验收。<!-- source-family:SF-2026-ARXIV-2602-16334 -->

能读出一段录音的属性，还不表示能在多段候选之间保持比较与身份绑定。当任务把录音视为候选集合，而不是一条有真实时间顺序的连续输入时，应分别保存 reference、candidate 的原始身份、展示位置与选择约束。一个不重训的分支对同一集合作多次排列，每路回答先映回原候选身份，再聚合选择；它改变的是输入呈现与决策提案，不改音频内容，也不能把多数结果当声学真值。[必要排列机制](https://arxiv.org/html/2603.09714v1#S5)相对同生成数的固定顺序 self-consistency 提供有限支持；reference 关系、位置措辞或实际时序无法保持时，不能直接套用换序。
<!-- source-family:SF-2026-ARXIV-2603-09714 -->

多候选还要按数量、语义内容、说话者、韵律、时长和环境声分别验收，不能用单录音平均分签联合理解。[有限多音频对照](https://arxiv.org/html/2603.09714v1#S4)中，减少候选同时减少干扰与随机猜错机会，因此候选变少后准确率提高不独证内部容量瓶颈；更多 CoT 也未必改善真实声学比较。排列聚合与固定顺序多采样具有相同生成数，仍须计全部音频编码、前向、生成和映回聚合费用，不由 training-free 或百分点增益承诺实时能力。投票不稳、任务具有不可打乱的顺序或预算不足时，保留原顺序单路输入、明确的候选比较及独立声学/人工核验，不以更一致的选择替代正确性。
<!-- source-family:SF-2026-ARXIV-2603-09714 -->

生成语音时，局部发音选择也可以显式进入条件输入：保留语境文字，只把目标词替换为指定音素，训练时随机对部分文本作 G2P（Grapheme-to-Phoneme）转换，让模型接触这种混合序列。[GLM-TTS 的早期说明](https://www.zhipuai.cn/en/research/147)提供了这一分支。它不同于整体音色或情绪提示，把多音字、罕见词的发音选择交给词典，却也引入 G2P、替换规则与词典版本的维护责任。公开 CER/SIM 评价未启用音素控制，不能据此证明局部控制或自然度改善；还须分别验收目标词读音、上下文韵律和未替换词的回归。不需要精确读音或无法可靠维护词典时，纯文本输入仍更简单，接口可控不等于效果已验证。<!-- source-family:SF-2025-ZAI-GLM-TTS -->

### 阶段三：共享 token space

系统开始把图像、视频或音频压缩为离散 codes，与文本 ID 一起交给共享 autoregressive backbone。它的吸引力是统一 objective 与生成接口：所有 modality 都可以表示成“预测下一个 ID”。

但离散化不会免费发生。codebook size、层数和 stride 决定序列长度与 fidelity；quantization error 会进入训练分布；codec 与 backbone 版本不一致时，同一 ID 可能不再代表同一信号。统一协议减少模型接口数量，却增加 codebook governance。

离散 codes 的另一种取舍，是不要求有限的可命名属性解释全部信号。先保留 pitch、loudness、speaker 或 content 等显式控制，再用固定数量的连续 queries 从原始声学表示读取未覆盖的变化，让属性与残余共同条件重建。残余预算越大越容易保真，也越可能绕过显式控制；训练中整组关闭残余、迫使属性独立重建，可以把“能重构”与“按属性控制”放回同一个约束，但残余并不会因此成为语义纯净或互不重叠的因素。<!-- source-family:SF-2026-ARXIV-2601-19399 -->

[RT-MAE 的有限语音对照](https://arxiv.org/html/2601.19399v1)中，不关闭残余时模型忽略属性，关闭概率过高又丢掉残余收益；残余独用仍保留部分 speaker identity，因此应分别验重构、属性编辑与旁路泄漏，而不由更高自然度代理分数认证 disentanglement。25个512维tokens、声学前处理、MAE与vocoder都付费，有限LibriSpeech/EmoV及音高移动只支持这一训练接口，未证明任意属性可控、免费codec压缩或实时SLO。属性足够、必须独立编辑或预算不足时，保留属性独用与原encoder/codec，并把残余数量、关闭策略、控制器及decoder一起版本化。

固定长度的离散 message 也可在多次观察中更新，而不是每个新 crop 都增加一段 tokens：共享的编码/解码模型消费旧 message、当前局部 crop 与相对位移，并另接新初始化的 buffer tokens 来预测下一份 message，不是在原位置直接覆盖旧状态；图像先经预训练 VAE 压缩，更新后的 message 再量化、供下一轮使用，最后以这份状态条件生成整图。训练随机化 crop 数，避免预先给未来观察保留固定槽位，并只对最后一次更新回传梯度。这把预算从“每帧生成多少 codes”转成“有限状态怎样重新分配已观察信息”，不意味着被丢弃的细节仍可恢复，后续 token 也不是独立的对象真值。<!-- source-family:SF-2026-ARXIV-2602-20731 -->

语义对齐与重构需分别验收：[COMiT 的受限对照](https://arxiv.org/html/2602.20731v1)用 DINOv2 对齐、flow reconstruction 与 local-crop 训练形成可读结构；更大模型可继续改善重构却降低语义 probe，单 global crop 已成本最低，增加 local crop 只有部分任务的有限增益。最佳 IoU token 由 gold mask 离线选择，不能当在线实体定位或内部因果；adaptive policy 的每 crop decode 与重构误差也不是通用置信度。32 GH200/200 epoch 训练、循环编码及额外 decode 都计费。VAE、message 长度/量化、crop policy、共享模型与 probe identity 应一起版本化；语义退步、细节丢失或循环费用不合算时，保留一次性 codec、更长 message 或独立 encoder/decoder，不从重构保真批准生成状态的事实用途。

共享 codes 还要决定保留的是像素重构还是理解语义。若每次生成视觉中间状态都先渲染成图，再交给视觉 encoder 读取，接口直观且方便人工检查，却把渲染误差和重复编码带入推理。一条条件分支以已有理解模型的行为为约束训练语义 quantizer，由生成分支预测这些 codes，再由理解分支重新处理并写入自己的 KV；像素 decoder 独立训练，只在需要可视化或像素评价时调用。省去像素往返不等于省去重新计算，也不能把生成分支的 KV 直接冒充理解状态。

这种选择用低层细节和 decoder 独立性的代价换取语义中间状态复用，还可能继承原理解模型的盲点。[LatentUM 的受限案例](https://arxiv.org/html/2604.02097v1#S3)支持 InternVL3.5-4B 路线中的表示消融、图像生成与视觉规划；它的 action-conditioned recurrent rollout 仍先渲染、再编码下一帧，不能称为已经实现全 latent World Model。细节保真优先、需要独立感知验证或闭环接口仍依赖像素时，保留独立 encoder/decoder 更合适。

<!-- source-family:SF-2026-ARXIV-2604-02097 -->

结构化 mask 也暴露了序列长度与词表的交换：将 run 的 start、length、class 分字段预测，二维 start 可由一个 `S²` 词表拆成两个大小 `S` 的坐标词表，却多付一个 token；合并 class×length 可缩短序列，却扩大输出词表。跨帧把 class pattern 合并后，组合数增长到 `(C+1)^N−1`，再与 length 合并还要乘长度预算，故视频压缩不能只看平均 run 数。按 class/instance 分组可缓解组合增长，但单个 tag 错误会污染整组 runs，既给的 instance 注释也不认证跨帧身份。Schema、实体/类 ID、坐标顺序、拆长 run 规则及 decoder 一起版本化，并计训练 memory/softmax 和序列费用；有限硬件上长序列会失败，不外推全分辨率收益。预算或错误作用域不合要求时，保留独立字段、更短窗口和普通 mask codec。<!-- source-family:SF-2026-ARXIV-2602-21627 -->

### 阶段四：native multimodal representation

更进一步的设计不再把非文本输入视为语言模型外挂，而是在 pretraining 中共同学习 modality representation、cross-modal relation 与生成能力。这里的 “native” 应指训练 contract 发生变化，而不是 marketing 标签：多模态数据从一开始就参与 backbone 表示形成，loss、sampling ratio、sequence packing 与 router load 都共同决定能力。

它不必然优于 staged alignment。若高质量多模态数据不足、codec 尚不稳定或只需要专用理解能力，冻结 encoder + projector 更容易训练、验证和回滚。

没有专用连续 encoder，也不意味着感知计算消失了：它可能在共同 backbone 内逐层形成可读表示。这里应分别测试表示 formation、后续 readout 和跨模态 routing，而不是凭某层线性 probe 或几何相似就把它命名为完整 encoder。对固定任务/层/模态的扰动，可检查该局部表示是否为所测输出所需；necessary readout 与足以替代全部感知计算、删 token 或提前退出仍是不同命题。

[Virtual Encoders 的精确 v2 证据](https://arxiv.org/html/2609.26513v2)含有限 concept probe 与两个模型的单层 Gaussian 扰动、特定 yes/no 判定；没有 activation patching 的充分性验证，PCA 子空间定义也未证明 rotation 的因果作用。新增 probe、干预强度与多重比较有成本，音频/其他模型上的相关观察不能外推共同层号或部署可省计算。证据不支持时保持功能解释的 Unknown，继续 dedicated encoder + projector、完整视觉读路径和独立任务回归，不让 native 标签代替分段验收。<!-- source-family:SF-2026-ARXIV-2609-26513 -->

复用生成式 backbone 做**理解/检索表示**还有一条条件分支：不能只把 causal attention 放开成双向，就假定原有 next-token objective 已学到适合全句比较的几何。先用 masked-token 目标适配双向读取，再用成对对比目标校准 embedding，才使 attention 形态、训练目标和下游表示用途一致；把视觉/语音 specialist 的权重或 head 接入同一 backbone 也必须逐模态验收。它节省从零训练 encoder 的成本，却可能遗忘原有语言、代码或其他能力，权重合并和多域数据只是需配对测试的缓解分支，不是固定比例的通用配方。只需生成时保留 causal 模型更简单；需要跨模态检索时则须同时检查表示质量和原能力回归。现有实验仅覆盖作者的小型 backbone 与所测 embedding/多模态任务，不能推出大模型或生产检索的普适增益。<!-- source-family:SF-2026-ARXIV-2604-02045 -->

冻结 encoder/projector 后，只更新语言 reasoning consumer 是另一条后训练分支：text-only SFT/GRPO 可以保留 native audio/visual I/O 接口，却不能由“没使用 AV 训练数据”推定 perception 能力不变。[受限 Omni 对照](https://arxiv.org/html/2610.02819v1)的 Thinker-LoRA 改善推理同时有感知退步，有限 native AV reinforcement 能恢复感知并保留大部分推理；本地梯度方向不是模块全局可分离定理，数据与任务不同也不支持纯 modality 因果归因。训练、生成和分目标回归均计费，input tokens 减少不等端到端成本同比下降；感知回归或接口身份变化时保留 AV 训练、冻结组件与原模型回退，算法细节仍由 SFT/GRPO owner 承载。<!-- source-family:SF-2026-ARXIV-2610-02819 -->

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

连续语义 latent 也不必承担逐采样重建的全部细节。一个音频分支用预训练 masked-autoencoder 的完整 mel-patch 表示作语义锚，再训练条件 waveform generator 补出声学细节；文本到 latent 与 latent 到波形的消费者可以分别优化。这把部分重建责任移给条件生成器，而非证明 latent 只含语义、原录音可逆或理解与生成已统一。[SemanticVocoder 的受限比较](https://arxiv.org/html/2602.23333v1)中，生成分数的局部收益伴随相对声学 codec 的重建质量退步；换 encoder 或换 decoder 的对照还同时改变预训练、容量或目标，不能唯一归因“语义化”。预训练、latent 预测、waveform 采样与多路 STFT 分支都计费，少数冻结特征读出任务也不授通用音频理解；要求原录音保真、长音频或完整成本不可验时，保留声学 codec、mel/VAE latent 与专用理解 encoder。<!-- source-family:SF-2026-ARXIV-2602-23333 -->

连续语义表示用于生成时，压缩轴也要先分清：减少空间 token 数会删去位置容量，降低每个 token 的 channel 维数则保留位置数量，但仍改变局部可携带的信息。一条受限图像分支在冻结视觉 encoder 上，先联合训练 attention compressor/decompressor 与重建 decoder，再固定两者训练 latent prior；它在所测操作点选择保留空间序列、压低 channel，而不是证明注意力层天然无损，或 channel 缩减等于序列/端到端计算同比缩减。生成目标、理解输入和重建 decoder 因而应分别携带形状、冻结版本与训练责任。

共享语义 encoder 也不能消除消费者分流：[UniCom 的受限对照](https://arxiv.org/html/2603.10702v1#S4.SS3)中，纯压缩 MHA 比 MLP 的局部理解分数更好，却仍全部低于未压缩 baseline，OCR 从55.40降到36；正文 Pathway I 的理解路径直接消费原 feature，编辑/生成使用压缩 latent，拼接完整 feature 的回补也不等纯压缩证据。不同空间/channel 操作点没有匹配总表示预算，重建指标仍有反退，精确收敛倍数口径不一，不能授语义保真或普遍加速。Codec/decoder 预训练、prior 多阶段训练、双表示投影和实际 decode 均计费；细节任务或总成本回归时，保留原连续 feature、理解/生成双表示与原 codec 操作点，不以统一 backbone 自签接口可逆。<!-- source-family:SF-2026-ARXIV-2603-10702 -->

### 离散表示

离散 codes 可共享 categorical prediction objective，也适合缓存、传输和自回归生成。代价是 codebook collapse、rare-code mismatch、长序列和重建误差。一个 code 是否“语义化”必须由 intervention、retrieval 或 reconstruction evidence 支持，不能从可视化聚类直接推断。

离散量化的不可导边界也不是鲁棒性屏障：攻击可以在量化前扰动连续 feature，再通过改变 codes 影响冻结的消费者。一条受限替换分支固定 codebook 与 downstream，仅用无标签 adversarial feature distortion 更新 encoder，使扰动输入的表示靠近原 encoder 对干净输入的表示；这是生产者兼容旧消费者的训练目标，不是逐 code 一致或所有下游安全的证明。[原版本控制](https://arxiv.org/html/2602.18252v1#S3)中，攻击失败仍可改变大量 code indices，说明索引稳定不是安全的必要条件，索引变化也不充分判有害；更大攻击半径则付出 clean/robust quality 取舍。监督与无监督分支使用不同半径、目标及更新集合，不能把跨任务差异全归因无标签训练。Encoder 训练、攻击搜索/ensemble 与逐消费者校准均计费，须绑定旧 encoder、码本、consumer、扰动范数和评价任务；兼容或 clean quality 回归、强攻击未覆盖时，保留旧 codec、连续 encoder 与独立 downstream/effect 验收，不由 tokenization 一项自签系统安全。<!-- source-family:SF-2026-ARXIV-2602-18252 -->

同一二值表示的语义监督还取决于量化前后的优化接口：sign/STE 保留离散输出，commitment 把 encoder 推近±1，却可能限制量化后 teacher 对齐所需的调整。一条受限分支在 encoder 末端用 SigLu 将输出约束在[−1,1]，去掉独立 commitment 项（α=0），再分别验收量化前、量化后与两侧的语义蒸馏；这改变梯度所遇到的范围与目标，不证明 entropy loss 数学上等于 commitment，也不把理论二值组合数当有效表示容量。其图像消融中，SigLu 后的 post-distillation 恢复了局部语义分数，但仍低于另一 pre-distillation 设置；不同表的 pre-only 人口不能拼成统一优势。teacher、附加投影/attention pool 与多目标训练均有成本，语义或重建回归时保留原 commitment、量化前监督或连续 encoder，不能只以 utilization 或组合数验收 codec。<!-- source-family:SF-2026-ARXIV-2602-14178 -->

离散索引也未必能脱离输入图像解释。一个 image-conditioned mask codec 将同一图像中的区域压成两层 residual code，再由图像条件 decoder 恢复 mask；这让输入、输出共享短 token 接口，却要求索引与原图、image encoder、两层 codebook 和 decoder 版本共同保存。两枚码不是“图像 token 加 mask token”，也不自带跨图区域语义。扩大码本可能改善重建却使语言模型更难预测；用 ground-truth codeword 匹配作奖励，也不能替代最终 mask 的几何质量。codec 的 mask 监督、词表扩展、解码与回归验收仍有成本；原图不可回读、接口变更或区域质量不合格时，保留连续区域表示或显式 segmentation head。[受限 mask-interface 证据](https://arxiv.org/html/2601.16093v1)只支持作者的图像条件 codec 与所测 MLLM，不证明两个 token 无损或通用 grounding。<!-- source-family:SF-2026-ARXIV-2601-16093 -->

同一 codebook 还承担不同优化职责：encoder 的 straight-through reconstruction/commitment 更新，不等于 code 向当前 feature 分布追踪。一个稳定训练分支按相对 assignment distance 停止梯度地缩放 STE，在有限窗口保存近期 active features、为近邻 inactive codes 提出追踪 target，并分别调 encoder/decoder 的 warmup–anneal 与 codebook 学习率。稀有 code 获得候选目标、共享投影受影响，都不等每个原 code 每步得到非零独立梯度；没有获得目标的 inactive code 可以只有零 self-target loss。

[StableVQ 的受限图像实验](https://arxiv.org/html/2609.26774v1)中组件单独仍有 NaN/低利用率，Eq 4 最匹配距离为零的数值 guard 未披露，不能称 threshold-free 完整稳定实现。不同 projector/epochs 的比较未全匹配预算，满 usage 也不保证语义或生成质量，IS/Precision 仍有反退。窗口、近邻搜索与分组优化增加训练成本；数值/质量验收失败时保留普通 VQ、EMA/reset、统一 optimizer 或连续 feature，不把 codebook 利用率升级为音频、视频或部署安全保证。<!-- source-family:SF-2026-ARXIV-2609-26774 -->

码本与 encoder 同步训练在固定离散接口下便于直接优化重建，却可能让量化误差、assignment 与 code 更新互相追逐。另一条分支在低维 latent 中，用近期样本队列估计与目标码本大小相关的扰动半径及密度，通过含 reverse-support 与体积比的 Metropolis–Hastings 步训练 decoder；训练时没有显式码本，结束后才重新编码训练集、离线 K-Means++ 建立码本，部署改用最近邻量化。[VP-VAE 的必要机制与对照](https://arxiv.org/html/2602.17133v1)因此分开了表示训练与离散产物构建，但固定估计密度下的 invariance 不等于移动队列保持真实分布，也不保证扰动支集覆盖实际聚类误差。队列/kNN、额外编码与离线聚类仍付费；50epochs/2RTX4090 的有限图像和音频重建结果不能验收后续 AR/diffusion 生成，利用率高也不等于全部质量更好，归一化对 PSNR 与 LPIPS 还可能有相反影响。需共同版本化 encoder、扰动估计和部署码本，重新验收真实量化后的质量；支集或消费者不匹配时，保留联合 VQ/STE、EMA 码本或连续 latent，不以无码本训练自签部署兼容。<!-- source-family:SF-2026-ARXIV-2602-17133 -->

<!-- semantic-body-binding:SF-2026-ARXIV-2605-26089:start -->
离散化还要回答“沿哪个轴量化”。常见 patch-wise VQ 把每个空间位置的 feature vector 变成一个局部 code，空间网格自然提供 token identity 和生成顺序；另一条分支把覆盖整幅 feature map 的 channel 当作 codeword，于是一个 token 可以携带全局空间结构，序列也可能显著缩短。这个变化不是换一个 codebook 实现，而是同时改写 representation unit、sequence length 与 autoregressive factorization。

channel 本身没有天然的 coarse-to-fine 顺序。可以用 nested dropout 让训练频繁只保留前缀，从而在论文所测设置中诱导可截断 ordering；但该顺序是学习结果，不是 channel token 的固有性质。更短序列和较高 codebook utilization 换来全局 codeword、空间局部性、跨分辨率 resampling 和 ordering 稳定性的治理成本。若 ordering 未形成、resampler 漂移或全局 channel 混叠导致 reconstruction/generation 回归，应回退 patch/grid VQ、普通一维 tokenizer、独立 diffusion decoder，或继续保留连续 feature。现有证据只覆盖披露的图像重建、文生图模型与 matched token-budget 实验，不证明它普遍优于 patch token，也不覆盖视频、统一理解或生产吞吐。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-26089:end -->

两个离散 codec 也不是因为 token rate 接近就天然兼容。直接翻译 codebooks 时，direction、codebook index、position、effective rate 与 codec revision 都属于接口身份；桥接模型只能提出映射，waveform decode/re-encode 仍是兼容 fallback。收益是避开一次连续域往返，代价是跨 codec 误差和语言、音色、噪声域漂移，不能把有限语音实验外推为任意声学 token space 的无损互换。

<!-- source-family:SF-2026-ARXIV-2609-12563 -->

如果目标是精确保留原 PCM 整数，而不是提取语义或允许波形重构误差，离散接口也可以绕开 learned codebook：先把 signed sample 映到 unsigned 区间，再按高位到低位展开为 `B=ceil(b/8)` 个 byte，共用 256-value alphabet。它用更长序列替换随 bit depth 指数扩张的 sample vocabulary，未减少每份音频的信息量；同一 token context 能覆盖的物理时间也随 byte 数缩短。[Trilobyte 的有限对照](https://arxiv.org/html/2603.08683v1)只支持这项表示取舍，低 byte masking 的额外 null 身份不是无损降低原 bit depth；采样率、signed offset、bit/byte 与 channel 顺序、block/reset 和模型版本须让两端一致。由 CE/BPB 得到的期望 coding length 不等于已验证的 bitstream，PMF 有限精度、header、终止、状态与独立 roundtrip 仍须验收。24-bit 商业人口的估算压缩率低于 FLAC，混合 bit-depth 模型也非每个人口更优；不同模型容量、token 数与数据条件不授 bit depth 的唯一因果或真实 entropy 下界。数据与概率模型训练、逐 byte AR 求值、实际 coder、模型分发/缓存和独立完整性验收均计费；吞吐、恢复或元数据失配时，保留 FLAC、原 PCM 或固定 sample 接口，不由常数词表或较低 loss 自签可部署的无损 codec。<!-- source-family:SF-2026-ARXIV-2603-08683 -->

### 分层残差表示

分层 residual quantization 可以让前几层表达粗语义，后续层逐步补细节：

```text
z ≈ q_1 + q_2 + ... + q_L
```

这提供 progressive quality 与可变计算机会，却把 layer identity、缺层行为和 decoder compatibility 变成运行时 contract。只传前几层 code 可能节省 bandwidth，但不能假设所有任务按同样幅度退化。

可变 depth 还要求训练输入、监督范围和部署消费同一份 prefix 身份。一条音频生成分支在训练时选择前 K 个 RVQ codebooks：temporal model 的当前帧输入只求和这 K 层 embedding，depth model 的 loss 也只覆盖这 K 层；部署选择 K 时，同样只消费、预测这一前缀。仅截断 loss 却仍把全部层送入输入，会让低码率部署失去训练时可见的条件；反过来，只裁输入而继续监督不可消费的层，也不是同一个接口。K、codebook 顺序、码本与 decoder revision 因此必须共同定义产物，不能把任意缺层当作合法 prefix。<!-- source-family:SF-2026-ARXIV-2602-10934 -->

这条分支用 prefix dropout 和配对语音—文本 CE 换低码率适配，并不意味着无需语义监督或每个 K 都无损。因果 codec 仍有 frame 聚合、滑动窗口和编码/解码成本；12.5 Hz token rate 不签发零缓冲或实时 SLO。作者同训练步数的有限 TTS 消融支持低码率鲁棒性，但扩大 batch 同时增加数据和 compute，跨模型/码率的重构与 ASR 指标也并非全胜。prefix 与 decoder 不兼容、细节或内容质量退化时，保留较完整 depth、普通 RVQ 或已有 teacher/staged 分支，分别验收波形、语义、缓冲和总预算。[必要接口与反侧](https://arxiv.org/pdf/2602.10934v1)见 §3–5、Appendix A/C。

“前层表达语义”还可以成为明确的 assignment 接口，而不只由重建训练自行形成：先由冻结 SSL 特征的聚类产生语义 token，把它指定为 RVQ 第一层的 code index；该 index 对应的码向量仍可随声学重建训练，后续层继续量化减去首层向量后的残差。这样固定的是离散索引身份，不是把首层向量冻结为 teacher feature，也不证明各层内容已经完全解耦。另一个分支在量化之前，让小预测头从 acoustic encoder 输出预测同一 teacher index，推理时撤去外部 SSL tokenizer；teacher 层号、聚类词表、码本与预测头版本共同定义这份接口。<!-- source-family:SF-2026-ARXIV-2602-06180 -->

约束索引与替代 teacher 都有质量代价。[STACodec 的受限语音对照](https://arxiv.org/html/2602.06180v1)中，加入 assignment 改善下游 ASR，却牺牲部分波形重构；量化前预测又使 ASR、意图分类与感知指标低于仍使用外部 teacher 的配置。两阶段预测头训练与原 codec 的总步数不同，不能将差异全部归因于蒸馏位置；去掉 teacher 的参数与 FLOPs 估算也不是端到端 latency 或实时保证。额外语义监督、聚类、预测训练和 codec 回归均须计费，码本利用率不签发语义纯度。若预测误差、词表迁移或细节损失不可接受，保留外部 teacher、普通 RVQ 或独立 semantic/acoustic 路径，继续分别验收重构和下游内容任务。

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


时间粒度还可以由文本位置决定，而不是固定-rate codec clock。一个语音分支用 CTC/Viterbi 把 transcript subword 对到声学帧，为每个文本位置保留连续 acoustic latent 和 duration，再由语言模型消费错位的 text/acoustic stream；输出文本、latent 与时长后，由局部 flow decoder 恢复对应波形片段。它减少 backbone 的声学步数，却依赖真实 transcript 对齐和相邻边界；训练 encoder 的局部窗口还可访问邻接文本位置的帧，不能因每段非自回归就宣称整条路径无未来依赖或零延迟。[TADA 的必要方法与反侧](https://arxiv.org/html/2602.23068v1)显示部分语言能力退步，增强音色 guidance 可伤内容，duration guidance 与多候选相似度选择也不是无错时长或说话人证书。额外对齐、buffer、flow steps 和候选生成均付费，预先提取 prompt transcript 的局部 H100 计时不是完整在线 SLO；时序、内容或语言能力回归时，保留固定-rate codec、单路 TTS 与完整输入等待。Ch24 拥有后续采样，表示层只声明文本索引、时间边界和消费者身份。<!-- source-family:SF-2026-ARXIV-2602-23068 -->

### 参考音色与目标事件时间轴不应共享默认控制权

完整参考音频携带音色，也携带自己的时间顺序；若目标只复用音色，事件发生时刻却由画面决定，将两路条件不加区分地注入会引入竞争。一个视频配音分支让参考路径减少位置/局部时间编码、另提供全局 timbre，画面路径继续保留目标逐帧同步身份。这里不是宣称音频已“无时间”，而是选择允许各通道控制什么：style proposal 不能自动取得目标时间轴的控制权，生成器怎样融合条件仍由下一章承接。

选择性抑制会连带丢失有用声学关系，并增加两路 encoder、训练、融合与校准成本。`arXiv:2604.15086v1` 的 ControlFoley 双条件消融支持受测组合选择，但 Table9 没有单独识别时间抑制模块的因果收益，部分 L0 切片 CLIP-only 更好；小规模主观评价也不证明统计独立、普适同步质量或线上 SLO。只需复制整段声音、两个来源本来同步或额外条件失配时，完整音频/单路表示仍合理；跨域使用应分别验音色保真、事件同步和失败切片，而非只以总分批准该分工。

<!-- source-family:SF-2026-ARXIV-2604-15086 -->

多主体reference还要同时回答“这张脸、这个音色和这句台词属于谁”。一个受限接口让同一主体的视觉/音频reference共享预留位置segment，并在video、audio和joint caption里持续使用具名anchor；reference以concat保留可选来源，结构条件另用加法注入，而不是将所有条件混成一个全局caption。位置分段是匹配proposal，不由RoPE周期性保证正交、零串扰或真实身份授权；loss排除reference区也不证明输入无法copy。[DreamID的有限200例proxy评价](https://arxiv.org/html/2602.12160v1)里reference-only身份相似更高却有copy倾向，完整分支也非所有同步/质量指标更好。配对来源、主体anchor、segment尺度、两stream及CFG版本需共同保存，数据匹配/训练、reference编码与多条件forward均计费。配对不明、主体串扰或质量回归时，保留显式单主体/声纹配对、独立同步与输出核验，而不把一致生成当身份真值。<!-- source-family:SF-2026-ARXIV-2602-12160 -->

语言响应与声学表达之间也需要明确条件的责任。只把最终文本交给 Talker，保留了要说的内容，却不一定传递上游选择的表达策略；另一条受限分支将感知描述、意图推断、响应策略与文本分开，再把策略映成显式 acoustic instruction 交给语音生成器。这里的 intent 与 strategy 是模型派生的状态，不是用户心理真值，“感知→推理→表达”的计算依赖也不等于已识别人类因果机制。[受限 Omni 对照](https://arxiv.org/html/2602.21900v1)支持可检查的策略交接，但删除策略后无法生成声学指令，只说明接口断链，并未唯一证明显式接口胜过匹配的 hidden interface；较高表达分数也不伴所有 WER/自然度改善。附加策略 token、映射模型、TTS训练/推理与 judge 都有成本，语义内容还会干扰声学一致性 proxy。策略不可信、控制预算紧或声学回归时，原 native hidden/纯文本 TTS 路径仍合理；须分别验收响应内容、指令遵守与真实语音质量，不以表达流畅反推原感知正确。
<!-- source-family:SF-2026-ARXIV-2602-21900 -->

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

高维视觉 teacher 能读出语义，却不保证像素 codec 压缩后的瓶颈仍携带同一信息；在 encoder 中间层监督和把短 latent 再展开后监督，拥有的是不同接口。一条受限分支先用冻结 VFM 的 patch features 训练紧凑 feature encoder 与辅助 feature decoder，再丢弃辅助 decoder、冻结紧凑 encoder，把它输出的同维 target 直接用于 pixel autoencoder 瓶颈。这里的 patch-wise 投影压缩 channel 而保留空间网格，cosine feature recovery 只提供训练代理，不签语义真值或无信息损失。Teacher/downsampler、pixel encoder/decoder、normalization/noise 与后续生成器须分别版本化，不能因同 shape 就当 consumer 兼容。

[GAE 的有限必要对照](https://arxiv.org/html/2603.10365v1)支持这一监督位置分支，却同时显示语义 probe、像素重构与生成质量并不处处同向；flatten 与 pooling 可改变 probe 排序，较强噪声或监督也会牺牲重构。去 KL、固定 RMS 尺度与随机 noise 是改变 codec 目标，不等 Gaussian prior、防 collapse 或任意 generator 都好学的证明。预训练 teacher、feature/pixel 训练、denoiser 与 guidance 搜索均计费，较短 denoiser 训练和局部 gFID 不能当全费用下降；下游 generation、细节或真实质量—成本验收失败时，保留原 VAE、静态 alignment/原高维 teacher 或原 codec 操作点，而不由定 norm 与 probe 通过批准新表示。<!-- source-family:SF-2026-ARXIV-2603-10365 -->

同一视觉表示既供理解、又作为生成目标时，压缩还要分配两种消费者的责任。输入侧删减 token 能让理解模型少读，却不能自动让生成模型少写；一种替代分支把稠密网格压成少量全局摘要与按空间池化的局部特征，理解路径直接读取连续表示，生成路径预测对应离散码，再由独立的条件自回归解压器展开稠密特征、交给图像 decoder。统一的是压缩接口，而不是两侧消费协议完全相同；全局查询、局部布局、码本和展开顺序需共同进入 artifact identity。

这条分支把大模型的长序列工作转交给重建模块，并非消灭细节生成成本。外部模块预训练与下游模型适配仍需计费，接口不改也不等权重不变；生成端缩短序列的收益，不能推成理解端同幅降时延。[受限统一视觉实验](https://arxiv.org/html/2603.11320v1)中，不同理解指标和生成质量均有反退，额外全局 token 与自回归展开也改变总预算。应分别验收理解、生成和包含解压的实际延迟；细节损失、展开瓶颈或无法重新适配时，保留稠密表示、理解/生成双 codec 或原压缩操作点，不把稀疏接口写成无损热插拔。<!-- source-family:SF-2026-ARXIV-2603-11320 -->

这条路线从固定 spatial/channel bottleneck，演进到可度量的 rate，再到按 base-model capacity 选择 operating point。它没有否定传统 VAE、discrete codec 或 pixel-space model：低 latency、已有稳定 artifact、固定视觉域或需要明确 codebook identity 时，旧方案仍更合理。论文中排除 codec training 或 decoder sampling 的 FLOPs，不能被写成端到端系统更便宜。

在线传输又增加消费者反馈这一操作点：为人眼填满带宽，不一定改善视频问答模型消费的证据，反而可能放大排队延迟。一个受限分支在模型自评分已趋饱和时限制码率、保留带宽余量，并按预测的任务相关区域分配编码质量；[Artic 的有限回放对照](https://arxiv.org/html/2602.12641v1)支持这种 consumer-aware 取舍，但 response confidence 与区域 grounding 都是模型代理，不是回答正确性或真实证据的证书。反馈年龄必须相对视频时间和区域预测窗记录，过期区域不能仍被当当前任务依据；不同 GCC/BBR 条件的准确率和延迟不得拼成一个收益点，作者 encoder-to-decoder 延迟也未包含模型推理。额外评分、grounding 和服务费用须计入完整回答预算；任务切换、代理失准或反馈过期时，回退保守码率、完整帧/均匀质量或重新校准，而不是永久以高自信删减表示。<!-- source-family:SF-2026-ARXIV-2602-12641 -->

压缩接口还要决定哪些变化由 latent 携带、哪些另传：若任务希望对音量增益不敏感，但 encoder 已把 global gain 缠入 latent 的方向和码字，在 encoder 后归一化不能复原原来的 shape。经典 shape/gain 分解因而可前移到 encoder 输入，把逐帧归一化的 shape 编码，另传量化 scalar gain，再由 decoder 输出经 overlap-add 和 gain 恢复。[Equalizer 的受限语音对照](https://arxiv.org/html/2602.15491v1#S3)支持这一放置条件，但 normalized 输入需要重训，额外 gain 约 400 bps 也须计入总码率；双向 encoder 的实现不能自动当在线因果 codec。较小码本的部分 PESQ/STOI 收益伴随 SI-SDR 反侧，外部 codec 又有不同训练语料，码本存储/搜索下降不等端到端加速。需要版本化归一化、低能量处理与 gain 精度，并同时验收 shape、幅度重建和总成本；不需要 gain 不变性或误差不可接受时，普通 codec 与原操作点仍应保留。<!-- source-family:SF-2026-ARXIV-2602-15491 -->

操作点还受计算放置与执行后端约束。高采样率音频 encoder 若先完成许多 residual 运算再降采样，会在随后被压缩的时间分辨率上付费；将 downsampling 前移可减少高 rate 计算，但不能把相同图改写直接复制到 decoder。[受限音频实现](https://arxiv.org/html/2602.15749v1#S2)中，encoder 可从前移与 separable convolution 获益，而 decoder 的 separable 路径触发 CUDA GEMM fallback，因而刻意不用；层名相同不等执行收益相同。Codec revision 必须绑定两侧图、backend 与 profiler 配置，分别验收重构、下游生成和完整成本；速度消融的 bf16 双 60 秒 stereo workload 未披露硬件，bundle 加速不唯一归因一种改写。训练限 instrumental music，低 latent rate 的重构也有反侧，额外 RVQ 训练和下游 context 的预算估计不能冒充零训练或实测生成 SLO。质量、格式或 backend 改变时，应重新 profiling，保留原 codec、原时间 rate 与传统两侧操作点。<!-- source-family:SF-2026-ARXIV-2602-15749 -->

操作点还要绑定 latent 的消费分布，而不只重构时的 posterior：连续 AR 预测出的 motion latent 带有误差，重构导向 learned-variance codec 未必能稳健解码这些样本。一条受限 producer 分支不预测 posterior variance，而在 codec 训练时采样小噪声尺度 σ，再用 μ+σ·ε 扰动 latent，让 decoder 学习局部容错；σ 是乘噪声的 scale，不能与 variance 混用。它和[生成路径](./24-multimodal-generative-paradigms.md#为什么-autoregressive-是合理起点)训练时扰动 teacher-forcing history 是两项独立操作：前者改变 codec，后者训练下游预测器接住偏离真实历史的前缀。表示 owner 必须分别冻结 codec/noise 身份并验收 reconstruction 与实际 rollout generation，不能以一项通过替代另一项。[有限 motion codec 替换对照](https://arxiv.org/html/2602.12370v1)支持这一接口张力，却没有识别随机 σ 的唯一因果收益或所有模态都必须这样训练；新增 codec 训练、生成 head/solver 和 decode 成本仍须分账。扰动与实际消费误差不匹配、重构退化或总预算不合算时，传统 VAE/离散 codec、原生成路径或重新联合训练仍是合理回退。<!-- source-family:SF-2026-ARXIV-2602-12370 -->

流式消费还要求 codec 自身的可见前缀与 generator 一致，而不只是给生成器加 causal mask。全局双向 latent 适合离线重构，却可能把后续帧信息提前带入当前块；另一分支按固定 stride 将帧块与其 posterior 参数 token 交错，以 causal attention 限制第 k 个 latent 只读取截至该块的帧及更早 latent，decoder 也采用对应的因果布局。[SARAH 的受限 motion codec](https://arxiv.org/html/2602.18432v1#S3.SS2)把这项表示责任与下游 causal flow generator 分开：过去 latent 在去噪时也需按当前噪声时刻构造条件，不能默认直接提供 clean past motion。两侧 mask、stride、posterior 与历史协议应共同版本化；四帧 stride 仍有聚合缓冲，音频特征与其它条件是否实际先到达、解码和整条生成费用须另验。A100 上一次生成 T=400 帧的平均 FPS 不是在线逐块 deadline，head-facing guidance 与生成分布也有取舍，不认证真实眼神或物理约束。prefix 泄漏、历史漂移或时延预算失败时，保留离线完整 codec、较保守块大小与已验收的生成路径，而不由 causal 标签批准实时闭环。<!-- source-family:SF-2026-ARXIV-2602-18432 -->

重构预训练的压缩表示也要适配实际消费者，而不只让自己的 decoder 复原原特征。直接学习任意 compact latent 能先用视频单独训练，却可能使接入 LLM 的未见视频落入不易对齐的区域；一种受限分支把 pooled 原特征作为锚点，让 compressor 学平均池化丢失的残差，再重构原特征、进行语言对齐。[CompressV 的原版本对照](https://arxiv.org/html/2602.17869v1#S3)中，无约束 latent 的对齐 loss spikes、Gaussian 约束与 residual anchor 的差异支持这一接口选择；latent holes 是作者的解释，不是所有自编码器失效的证明，也不说明平均池化无损。控制实验固定32帧/64×压缩；compressor 先预训练，该消融的 MLLM 训练仅 stage1 projector 对齐 + SFT，省略 stage2，不能把完整三阶段榜单收益全归因锚点；预训练、池化与压缩/投影仍计费，shot-change 采样也不证明事件完整性。细节损失、消费分布或对齐回归时，应保留完整特征、平均池化/选择式压缩或重新联合训练，不把重构通过当下游理解通过。<!-- source-family:SF-2026-ARXIV-2602-17869 -->

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

如果希望内容和声音风格来自不同语音，而不只是同一源的连续 side channel，还可分别输出两条离散流：先用 ASR/CTC 目标形成并冻结 semantic tokenizer，再学习 acoustic tokenizer，交给能消费不同长度条件的 decoder。训练除完整重构，还混入“完整 semantic + 随机 acoustic prefix”的 masked-mel 重建，要求局部声音条件支持整段内容生成；一种受限实现把 semantic 条件经卷积/插值相加、acoustic 条件经 cross-attention 注入。两流各自的来源语音、码本/encoder 版本、时间尺度和目标长度要保留，decoder 的 flow 训练与积分仍由第24章解释；训练中同语音 prefix 重组并不自动证明真实跨来源独立。<!-- source-family:SF-2026-ARXIV-2601-09239 -->

验收因而要把同源 reconstruction 与异源 semantic/acoustic recombination 分开，并同时看内容错误、声音身份和感知质量，而非由短码率或某个 probe 难解码认定“无泄漏”。有限中英语音对照中，去掉 speaker loss 降低声音相似度，却改善部分内容/感知指标；完整模型的重构也并非各项优于其他 codec。额外 ASR/声学训练、合成目标与迭代 decoder 都计费，重组失效、时间对齐不明、源身份不可暴露或低延迟优先时，保留 joint codec、文本中间层或已验证的源条件路径。双流只是可选表示接口，不签发内容/身份彻底解耦或实时生成保证。<!-- source-family:SF-2026-ARXIV-2601-09239 -->

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

空间边界还可能在训练 target 产生时进入 latent，而不只是最终 decoder 的接缝。周期全景中的左右像素本应相邻，普通 zero-padding encoder 却会在两端看到不同邻域；受限分支先在像素域环绕扩展，再编码并裁去多余 latent，使训练表示消费相应边界条件，而不扩大后续 DiT 序列。只在输出端 blend 或旋转采样，未必修复已经带入训练的 codec artifact。像素预处理、裁剪映射与 codec revision 因而属于同一身份；编码额外工作不等于全 pipeline 零开销，裁剪也不证明任意 receptive field 都无缝。边界不周期、映射失配或质量回归时，保留原 codec 与已验证的局部修复；[图像和视频全景对照](https://arxiv.org/html/2601.16192v1)不签发通用 geometry 或动态一致性保证。<!-- source-family:SF-2026-ARXIV-2601-16192 -->

表示层选择固定后再训练decoder，在融合接口稳定、预算紧时最直接；但像素重建偏好的层组合未必是生成器最容易建模的latent。另一条训练分支不搜索单一固定gate，而对同shape的frozen encoder层表示随机取非空子集、按保留层数求mean，让decoder适应不同composition；每个输入上的期望仍为全部层mean。它扰动的是层间disagreement，不证明每次抽样都保留全部信息、encoder更便宜或非线性decoded output不变，layer normalization/集合/归一化和部署fullmean必须同属representation身份。

[随机融合的受限证据](https://arxiv.org/html/2609.31620v1)进一步区分subset→pixels的decoder训练，与noisy subset→固定fulllatent target的DiT训练，两者不应共享默认最佳drop rate。固定generator及同一批sampledlatents只更换decoder，可隔离readout改变；joint训练则必须分别比较两条轴和最终质量。线性平方loss下的disagreement惩罚不是完整感知/GAN或guidedtrajectory保证；有限图像实验有native重建退步、guided中间率反退及大generator的FID/IS偏好分离。随机训练、保存多层feature和rate搜索仍有费用，其他层级/分辨率未验收时保留固定fusion/原decoder及已验证codec，不把robustness称为全场景或免费收益。<!-- source-family:SF-2026-ARXIV-2609-31620 -->

## Fusion：在哪里让模态相遇

### Early fusion

不同 modality 在 backbone 前或浅层合成一个 sequence。优势是 cross-modal interaction 充分；代价是序列更长、attention 成本更高，且强势 modality 可能支配梯度和位置预算。

统一 sequence 并不要求每个 token 都能消费全部专家。另一条融合分支先按表示来源限定 routed expert 的资格集合，同时让所有 tokens 经过并行 shared MLP，再相加两条输出；模态身份决定谁可被选择，共享路径提供共同容量，两者不能由 router entropy 合并成“已学会跨模态语义”。[MoST 的 exact-v1](https://arxiv.org/html/2601.10272v1)具体先对全部专家 softmax，再施加 modality mask、TopK 和加权求和，未给 mask 后重新归一规则；因此组划分、权重合同、shared/routed 参数与实际 active compute 都属于融合接口。其 HuBERT 连续输入和离散预测输出也须分开，不把共同 backbone 称为所有模态都已连续化。

共享分支能否迁移能力仍需任务与预算对照。作者同初始化、相同 routed expert 数及训练步数的局部消融，删去 shared MLP 也改变总参数与 active budget，不能授单因果或跨模态 transfer 保证；正文与表格平均分冲突、部分文本任务退步及缺少原 base 配对，也不足以证明无遗忘，更不把预训练专家分组当随机中性干预。48 A100、混合数据与额外专家训练仍有成本，precision、seed 和端到端 serving 费用未披露；资格、权重或质量合同失效时，保留原模态 encoder/projector、普通 early fusion 或独立编码的 late fusion，并分别验收各模态和共享任务。<!-- source-family:SF-2026-ARXIV-2601-10272 -->

### Late fusion

各 modality 独立编码，在 prediction head 或决策层融合。它保留专用模型能力和故障隔离，适合低耦合任务；但细粒度 token-region、word-frame 对齐难以形成。

决策层融合还可以先生成各模态的 perception 描述，再在这些文本与原输入上推理，让中间解释可检查；但生成先后不自动使观察独立。若 audio描述仍以visual描述和完整输入为条件，它就是联合推断，而不是一份新的盲音频证据；后续偏好训练奖励解释与答案一致，也不验证真实情绪或内部因果。[受限视听情绪对照](https://arxiv.org/html/2601.18321v1)使用大规模合成标签、ASR过滤与模型judge，数据、阶段和格式共同变化，不能把局部增益全归两段感知。应保存原模态、可见性、perception producer及judge版本，生成解释/偏好样本和额外训练计费；描述失真或缺模态外推失败时，回独立encoder、原始信号与真实标签核验，不把易读文本当独立感知真值。<!-- source-family:SF-2026-ARXIV-2601-18321 -->

### Cross-attention fusion

一种 modality 作为 queries，另一种提供 keys/values。它可以控制 interaction direction 和计算量，也把 connector capacity、query count 与 synchronization 变成显式瓶颈。

Fusion 还可以发生在生成器的 clean latent 入口，而不只是 denoiser 中反复读取 text condition：让 VAE 视觉 latent 作为 query、class text 提供 key/value，经 residual、Norm 与 FFN 形成新的 fused latent，再对它加 noise。原视觉 latent 保持与 class 语义对齐是两项目标，可分别用 latent reconstruction 与同 class 多 positive 对比项训练 connector；若新 latent 分布不匹配原 denoiser，是否再适配 denoiser 是第三个选择。视觉作 query 或小 MSE 都不证明 text 永不覆盖 instance 细节。[EVLF 的 class-level 数据蒸馏对照](https://arxiv.org/html/2603.07476v1)支持比较 fusion 与 denoiser 适配组合，但新增训练未等预算，类标签不授 instance/multilabel 保留；生成点落进 real 支持邻域的比例也不能当作 real 多样性召回。应保存 encoder/text/connector、融合与 noising 顺序和 denoiser revision，并计入全部构建、训练与生成费用；细节或下游质量失配时回原视觉 latent、late text conditioning 与独立目标校准，不由平均分类 gain 批准无损统一表示。<!-- source-family:SF-2026-ARXIV-2603-07476 -->

Query读取还可以在同一个encoder内形成有序读出，而不只用独立cross-attention：保留双向可见的visual prefix，接等基数learnable query suffix；visual不读取queries，各query读取全部visual与自身及前序queries，最后只把query states交给语言decoder。这个blockmask把原patch几何顺序与learned readout顺序分开，query输出是聚合状态，不是已证明的patch permutation、真实阅读因果或新增观察。[Jan27原OCR2报告](https://github.com/deepseek-ai/DeepSeek-OCR-2/blob/16ba51c72bfff2891379d56444380270366fb032/DeepSeek_OCR2_paper.pdf)的受限文档对照同时改变encoder容量、采样与标签，部分文字类型仍退步；少decoder视觉tokens不消除encoder内部前向与三阶段训练费用，生产重复率降低也不认证准确率。Mask、query集合、crop/分辨率、encoder与decoder版本须共同验收；有序读出失配、密集文字损失或完整成本不值时，保留普通visual encoder/projector、bidirectional queries与原文回读，不从两级causal计算自签一般2D理解或统一模态能力。<!-- source-family:SF-2026-DEEPSEEK-OCR2 -->

融合方向也须与部署可见性分开：局部 audio Q-Former 先形成 queries，再读取视觉 encoder 的 keys/values，可以让多模态teacher使用声音指向的视觉上下文；之后在共同词表上用teacher伪标签与soft分布监督audio-only student，部署不再获得视觉输入。训练中把gold字幕嵌入画面、按gold interval对齐，并不是自然盲ASR获得了额外事实；teacher训练与冻结蒸馏、student可更新部件须各有身份。[受限字幕辅助蒸馏](https://arxiv.org/html/2601.18393v1)的student局部WER改善远未达到teacher表现，不授完整能力无损迁移。额外视觉训练、teacher前向、对齐和标签费用不能由student部署省输入抹掉；同步、字幕权限或域条件不可靠时，回原audio-only训练、真实配对观察与独立转录评价，不让特权teacher自签部署感知质量。<!-- source-family:SF-2026-ARXIV-2601-18393 -->

当同一组 context 需要服务多个 target view，producer 是否依赖 target 也决定可复用范围。把 context 与每个 target 联合编码可保留目标条件交互，却重复支付 context 计算；改为 target-agnostic context encoder，再让各 target 独立 cross-attend，可在同一 scene、camera convention、encoder revision 下摊销 context features，但要支付预编码、驻留与条件质量损失。应分别比较相同参数/步数和相同 FLOPs：[受限 view-synthesis 对照](https://arxiv.org/html/2602.21341v1)在前一种口径较差，在更多训练数据的等算力口径改善，小数据条件下原联合路径仍合理。其 A6000、batch64 的渲染 FPS 为绕开单样本非算术瓶颈而测，不能当作 fresh-scene 单请求或端到端 SLO；重复 scene 的 scaling fit 也不授普遍数据规律。target 变化破坏条件质量、camera 身份失配或驻留预算不足时，应重新编码或保留 target-conditioned 路径，不由张量可缓存推导语义可无条件复用。<!-- source-family:SF-2026-ARXIV-2602-21341 -->

生成器未必需要在每个 block 读取同一份 text condition。一条受限分支先对 LLM 各层表示分别 LayerNorm，再作 softmax 权重的凸组合，让不同 DiT depth 选择不同层组合；gate 也可加入 timestep，但层权重可读不等于因果语义分工。表示层集合、normalization、gate revision 与 consumer depth/time 都应进入缓存身份，保存多层 feature 与额外融合/延迟并不免费。[单一 backbone 的条件融合对照](https://arxiv.org/html/2602.03510v1)中，time-only 不稳定、static 学权未优于 uniform，depth routing 也不构成通用优势；由自身最终生成 latent 回推的 SNR 和 shifted-time 局部恢复，只支持作者的失配解释，不识别唯一原因。Gate 漂移、成本过高或生成质量回归时，固定单层/mean fusion 与已验证的共享条件仍是合理接口。
<!-- source-family:SF-2026-ARXIV-2602-03510 -->

当 consumer 自身重复执行共享 block 时，fusion identity 还要区分视觉 producer layer 与 consumer recurrence pass：先从既有视觉编码器的不同深度提取 cues，再在早期共享计算中注入，后续 pass 继续修订同一 hidden state，而不是每轮获得新观察。层选择、connector、注入阶段与 recurrence budget 因而必须共同版本化；缓存多层 cues、重复计算和截断 BPTT 也有成本。[HIVE 的 exact-v1](https://arxiv.org/html/2602.05359v1)在所测 Huginn/InternViT 设置中支持这条接口分支，但相同 recurrence 下部分 OCR 与 MathVista 指标低于无层级 cues，对隐藏状态变化量的提前退出也不是任意任务质量保证。不能从其 schedule/示例代码的不一致处推导可执行的通用注入规则。cue 失配、质量回归或预算不足时，固定单层/mean fusion、无层级 recurrence 与常规非 recurrent consumer 仍可共存；最终选择须同时验收表示、任务质量与实际计算预算。<!-- source-family:SF-2026-ARXIV-2602-05359 -->

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

哪个模态提供这条读取路径，也未必由模态本性决定。在一条受限训练分支中，先用高多样性的 M1 训练 decoder，再通过 projector 接入 M2 并联合训练，M2 可以利用原有的 label-copy 路径；在相同的 `M1、M2、label` 序列结构下，从零联合训练却更依赖与 label 相邻的 M2。这说明观察到的主次至少依赖 curriculum，而不能直接称作语言或视觉的固有地位。训练顺序、示例排列与模态读取必须共同保存身份；但该对照没有独立交换 label 位置，也没有等化阶段训练总预算，不能把变化唯一归因于邻接位置。<!-- source-family:SF-2026-ARXIV-2601-20796 -->

容量变化也需在这个训练条件下解释：已有示例读取路径时，增加容量可帮助接入第二模态；单模态、固定数据多样性时，额外容量却可能更便于把对应关系记进权重。因而要分别测新 label 的上下文应用、固定 label 的参数记忆和两模态消融，而不是用更大的 decoder 或高总分替代检查。[必要机制与反侧](https://arxiv.org/html/2601.20796v1)主要来自两层受控模型，真实大模型的表示与训练数据仍有混杂；新增训练、attention 诊断和配对评价也有成本。证据或预算不足时，保留原来的直接示例读取与单模态基线，不把这条分支写成所有多模态 ICL 的优越 curriculum。

Fusion 还包含一个常被隐藏的 commit：把上游 posterior 立即压成 argmax。硬标签省带宽、易缓存，且当上游校准很差时可能更稳；但它不可逆地删除了次优语义，后续几何或跨模态证据也无法纠正。若下游能消费有限 alternatives，应把 posterior support 作为版本化状态延迟离散化，并同时测校准、带宽和任务增量；保留完整分布不是默认答案，关键是让 commit 时点与下游纠错能力匹配。

<!-- source-family:SF-2026-ARXIV-2609-12099 -->

保留多个视觉 token 后，还要问下游 reader 在当前预算下能否取出所需组合关系。额外训练 object-centric bottleneck 可把 dense patch features 聚成少量 slots；其价值不只由 shape 或“对象”名称决定，而与训练组合多样性、样本量和 reader 容量相乘。[受限组合泛化对照](https://arxiv.org/html/2602.16689v1)中，较难的 synthetic VQA 与小 reader/受限资源更有利于对象表示；dense 在较容易、样本与 reader 预算充足的条件下仍可追平或反胜，不能说所有 hard setting 都会被更多 compute 修复。正确对象属性的 oracle 也会在稀少组合上失效，所以 object token 不认证组合推理、持久身份或 world state 真值。原文的 matched FLOPs 主要针对下游，排除了 resizing cross-attention 的算量，额外 slot 预训练也须另计；验收应分开组合 holdout、reader、representation size 与完整生命周期成本。自然场景或绑定条件未验证、收益不稳定时，保留 dense/普通 cross-attention；下一步再处理多个 slots 自身是否重复分配证据。<!-- source-family:SF-2026-ARXIV-2602-16689 -->

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

光学表示也可以服务于已生成的历史，而不只压缩输入：完成一个 text chunk 后，render/视觉 encoder 将其转成 visual history，后续 chunk 按“过去 visual history + 当前 chunk text”的 consumer 可见性训练。这样尝试控制逐字生成历史增长，但改变的是后续模型消费的表示与条件分布，不是无损缩短原始文本。[VIST2 的受限机制](https://arxiv.org/html/2601.10378v1)要求 chunk、renderer、视觉 encoder、position 与 mask/objective 同版；公式中的一般 causal 分支不能单独证明旧 text 不可访问，实际 KV 回收/迁移实现和逐字 readback 并未核验，也不能把表示合同写成已经实现的 cache 节省。

这种训练可见性还应逐阶段分账：OCR warmup 仍可访问旧 text，之后的 optical language modeling 才针对 visual-history consumer，不能称全部阶段都没有旧文本。render/视觉编码、额外训练与有损字符密度的代价必须进入端到端预算；作者 8B 的部分 arXiv/Gutenberg perplexity 和数学 QA 反退，吞吐与 Glyph 相当，不能用 headline TTFT 或 FLOPs 推出普遍 3× 吞吐或质量无损。精确引用、代码与长尾字符任务仍保留原文/readback authority；chunk/layout 变化或 reader 未按同一可见性训练时，回退 text-history 路径，并分别验表示质量、实际 cache 生命周期及完整 serving 成本。<!-- source-family:SF-2026-ARXIV-2601-10378 -->

OCR 可读性与任务中实际使用视觉字符仍是两种能力。另一条渲染分支不是压缩文本，而是从 text channel 去掉问题，在原图下方的新增 canvas 随机渲染字体、颜色与字号，让训练任务必须经过已有的视觉读取路径；standalone 训练采用这种视觉问题，测试仍回到原来的图像加文本问题。[SimpleOCR 的受限对照](https://arxiv.org/html/2602.22426v1)支持这种 elicitation 选择，不能证明渲染创造了通用 OCR 能力；其 hybrid 分支仅让部分 rollout 使用视觉问题，更新却在原始输入 C_orig 上计算，不能与 standalone 协议合并。新增 RL、渲染与两种输入协议的校准都付费，长问题和低分辨率会丢字符，部分同域与混合比例切片仍反退；30×数据差异也不是等计算收益。现有 OCR 不足、问题过长或局部质量退化时，保留原始 text 输入及常规 RL 回退，分别检查能否读出字符与是否真正用它完成任务。<!-- source-family:SF-2026-ARXIV-2602-22426 -->

能读出字符，也不等于能读出字符如何被呈现。同一文本的字体 family、size、style 和 color 是另一些视觉属性，转录正确或易识别颜色的总体均值不能替它们验收；对受控 renderer 生成的图像，应保留原始属性标签，逐项比较读出，再绑定 resize、DPI、canvas、prompt 与 parser 身份。像素中的尺寸也不自动恢复原文档的绝对 point size。[FontBench 的有限对照](https://arxiv.org/html/2603.08497v1)显示 targeted LoRA 可改善部分属性，但训练后的改善不证明只是唤醒既有视觉 features，某属性不改善也不证明架构缺少必要计算 primitive。模型尺度、预训练与量化不匹配，以及相关问题、不同字体/script 和退化人口的分母，均不能由一个总分消去；文字内容与字形冲突时，应分测内容读取和视觉属性，而不从注意力图推断唯一通道因果。合成渲染与标签、属性评价、训练/量化和独立旧任务回归都有成本；原始呈现、读出或迁移未验收时，保留高保真图像、OCR 的有限内容职责与专用视觉属性工具、原 checkpoint 和 Unknown，不让正确转录批准外观理解。<!-- source-family:SF-2026-ARXIV-2603-08497 -->

### 固定预算要先分配信息责任，再选择具体 Token

同一个 selector 还可能在三个阶段看到不同信息：离线构造标签时用 gold response loss 搜索视觉 mask，训练 compressor 时用这些 mask 作监督，部署时再由不读取 gold response 的模型预测保留 token。因而构造输入、训练输入与部署输入必须分别记录，不能因为在线 selector 不访问答案，就称整个压缩流程没有特权标签或训练成本；gold loss 也只是所定义模型/回答目标下的选择信号，不是视觉证据充分性的真值。<!-- source-family:SF-2026-ARXIV-2604-17087 -->

搜索候选/代数、compressor 训练与线上 selector 需要分账，保留每个语义组至少一项也不能证明遗漏不会改变答案。原文相对 dense 的部分质量退步和不同搜索 loss 的反例要求同时验 selector、预算、内容覆盖与实际执行成本，不能把离线 mask 上界当部署收益。标签不可得、任务漂移或搜索成本不能摊销时，静态/attention selector 与 dense 回退仍合理；这里补的是同一接口跨阶段的信息责任，不取代后面的 modality/时间预算分配。<!-- source-family:SF-2026-ARXIV-2604-17087 -->

扰动下还要把视觉语义损伤与 selector 排序不稳分开。可以对同一输入、同一扰动配对运行压缩与未压缩路径，测量压缩增加的失败差额；再保持扰动图像不变，离线换回干净输入的 token 排名，检查恢复是否来自选择规则而非图像内容改变。[受限视觉压缩攻击实验](https://arxiv.org/html/2601.12042v1)用这类 clean-ranking oracle 诊断离散删选对排序扰动的放大，支持在其模型与压缩配置内检查这一失效路径，不证明已识别唯一内部因果。<!-- source-family:SF-2026-ARXIV-2601-12042 -->

这个 oracle 读取部署时未必可得的干净排名，只是特权离线诊断，不是已验证的线上 guard。评价需绑定 selector revision、删除层、保留率与扰动权限/预算，同时分别验安全鲁棒性、正常任务质量和完整选择成本；局部白盒 LLaVA/Qwen 对照不能推出所有压缩都不安全，安全差额也不等于一般语义质量损失。排序不稳时可以验证更保守的保留预算或未压缩回退，但这些仍需同威胁与质量目标下的独立检查，不能把离线恢复当作可部署防御保证。

预算还与压缩发生在哪一层有关。对高 token-rate 语音，input tokens 保留声学细节，而中间层可能正在重组声学与词汇信息；深层相似度高不意味着从输入开始就能同等压缩。一个条件分支在输入端只合并严格相邻的相似 features，到较深层再允许稍宽的局部 lookback，以 mean pooling 保留分布式信息，而不是随机删 token。它改变的是表示粒度，不能把 ASR 恢复出相同文字当作音色、韵律、重叠说话人或非语音事件都无损。

压缩的层位置也改变收益：越早减少序列，越多后续计算能够省下；深层虽然最终 token 数更少，已执行的大部分 forward 无法回收，还要付 selector 成本。[Affinity Pooling 的受限证据](https://arxiv.org/html/2604.06871v1)在 Qwen2-Audio/Kimi-Audio 的语义任务中发现中层敏感、输入与深层两级合并较稳；H200 短音频的深层或双级路径却可能比原模型更慢，精细声学任务也未充分测量。层位置、lookback、阈值和任务质量因此应一起验收；需要完整声学信息、短输入或净时延不划算时，原始 token stream 与保守均匀采样仍合理。第45章接手存储后的 KV 生命周期，不把这里的 feature 合并视为精确 cache 复用。<!-- source-family:SF-2026-ARXIV-2604-06871 -->

合并规则也受 batch shape 约束。逐样本保留不同数量的 source tokens，虽能适应内容，却不便直接组成稠密 batch；一个矩阵合并分支对保留 mask 做 batch OR，只要任一样本需要某个 source 位置，整批就保留该位置，并取消它对应的融合列，避免重复计入。统一 shape 的代价是压缩率依赖 batch 组成，单样本的高压缩不能直接推算批量吞吐。<!-- source-family:SF-2026-ARXIV-2604-13432 -->

若后续生成层需要原空间网格，还须保存融合映射，把更新后的 destination 特征散布回 source 位置；恢复 shape 不等于逆转信息损失。相似度矩阵、映射状态和恢复算子都有成本，压缩应与下游网格 consumer 一起验收。[作者的视觉分类与生成对照](https://arxiv.org/html/2604.13432v1)采用不同模型、精度和 batch，部分配置牺牲质量，不能由局部算子收益推出通用端到端加速；精细空间任务、异质 batch 或恢复成本过高时，原始 token 路径仍合理。

历史与当前观测也可承担不同预算职责。GUI 的一条受限分支先按时间距离缩小历史截图，再对当前高分辨率截图用边缘/浅层 attention 选择前景与背景，同时保留均匀空间网格；历史分支控制旧状态冗余，当前网格分支为小目标和布局留下例外。这里的历史总配额仍随帧数增长，规则包含整数化与单帧边界，不是任意长历史的常量状态；残余网格也不保证二维关系完整。[GUIPruner 的必要对照](https://arxiv.org/html/2602.23235v1)中，同预算的时间衰减、网格选择只有局部收益，剪得更早还可大幅伤任务，完整输入仍有更强切片。resize、selector、保留坐标、额外微调与输出长度均计费，视觉编码/prefill 的单设备加速不能替代 action-level 全流程 SLO；小控件、旧界面状态或任务质量失配时，增加历史/空间下限并保留原截图、均匀预算与 dense 回退。<!-- source-family:SF-2026-ARXIV-2602-23235 -->

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

模态内 selector 还可能相互依赖，而不是各自拿到预算后独立打分。一条受限分支按同步两帧 chunk，先分别用 spatial 与 temporal 差异保留视觉 tokens，再让 audio queries 读取这些已压缩的 visual keys/values，经过学习的评分器选择音频 tokens；删去视频于是也改变音频选择所依赖的证据，不能只验两端保留率。chunk/time/position 映射、两级 selector 与其训练 checkpoint 应共同进入表示身份，且需另计 cross-attention、评分和训练成本；这是部署接口推导，不是原实验已验证完整 guard。[必要方法与反侧](https://arxiv.org/html/2602.04804v1)包含 decoder 与 selector 的付费联合训练，反向路径的不同训练 recipe 不识别“必须视觉先行”的唯一原因，部分质量也低于完整输入。画外声音、视觉失配或所删画面恰是判音依据时，这条依赖会放大遗漏；应允许音频独立 selector、提高两模态下限或回退 dense 输入，不把视觉相关性当作音频充分性或端到端 SLO 保证。<!-- source-family:SF-2026-ARXIV-2602-04804 -->

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

视觉读取也可以不删 token，而从内部层与 head 提出受限的选择候选。固定层简单且成本可预测；当同一模型不同问题的视觉关注转移位置不同时，可以用相邻层 visual-attention 的变化选 basic layer，再用 softmax 前 attention-map 的 norm 筛选 head、对低排名 head 作软衰减。层变化与 head norm 是不同的内部 sensor，不是新增 observation，也不是已证实的 grounding 或因果重要性；它们不自动批准裁剪原始图像或改变视觉访问权限。<!-- source-family:SF-2026-ARXIV-2601-07359 -->

[DualPD 的局部对照](https://arxiv.org/html/2601.07359v1#S3)支持选择器及抑制强度的取舍，某些任务固定层更好，过度抑制也退步；组件比较没有充分随机 head 等因果对照。原文定义的中层 Δlogits 没有明确接到最终 aggregate，per-head 词表投影和跨 head/query 归一也不完整，不能拼成可执行解码公式。取得 attention、中间状态与 head 统计都付费，未给通用 GPU 或 tail-SLO 收益。接口未明确、选择器失配或任务质量不合算时，保留固定层、原 Decode 与完整视觉路径；答案仍由独立证据验收，而非由内部 sensor 自证。

一次性 prefill 剪枝适合后续证据需求稳定、预算严格的短回答；长推理中的视觉关注可能变化，原先被删的区域因而需要保留为可恢复的备用状态。一条 decode-stage 分支以当前与 prefill 的 attention 相似度触发重选，短期读取原集合与新集合的 union，再按策略回到原预算。这里保留与备用集合的 attention 分别归一化后拼接只是选择代理，不是全局概率或最优 top-k；回到原集合也不证明后续证据已经充分。

可恢复状态换来备用存储、临时扩大的 token 集合、重选和读取成本，还需核对语言历史与 KV 位置的一致性，不能称为精确恢复先前完整输入。attention 转移不是因果重要性真值，触发器会漏检；两类 VLM/L40S 的受限结果也有 TPS 或总时延退步。静态证据需求、短输出或额外状态不划算时继续使用固定剪枝；完整性优先时提高预算或回退完整输入。第 45 章接手存储后的生命周期，不由表示换入自动批准缓存复用。<!-- source-family:SF-2026-ARXIV-2604-12358 -->

### 固定表示之后，可以按未决 Claim 主动补充 Observation

一次性均匀采样或 top-k selection 在低分辨率已经足够、latency 上界严格时最容易复现；高分辨率细节只占很小区域时，它又可能在第一轮压缩中不可逆丢失。一个 bounded active-observation 分支先保留全局低分辨率 context，再由 acquisition policy 根据当前未决 claim 提出下一处 crop。Evidence assembler 记录坐标、尺度、采集顺序与预算，answer gate 决定继续、提交或拒答；selector 只拥有 observation proposal，不拥有 evidence sufficiency。<!-- semantic-body-binding:SF-2026-ARXIV-2605-01345 -->

主动取证以额外调用、路径依赖和尾延迟换取局部细节可见性，也可能因错误 crop、漏区或 backbone hallucination 形成自确认。采集策略漂移、证据完整性优先或预算不足时，应回退均匀/静态采样，必要时保留完整 tokens。exact-v1 只支持作者 VLM、crop proxy 与高分辨率 benchmark 下的机制方向，不证明 crop proposal 是充分证据或能覆盖开放世界视觉风险。

取得原图之后，定位与读数也可以拆成两种表示责任，而不把一次答案直接当作观察完成。一个受限图表分支先提出像素坐标，在原图上绘制定位 marker，把这张派生图回输以修正遗漏、偏移或幻觉位置，再由原图与最终位置读取数值和图例。marker 是定位 proposal 的可重读状态，不是新增真实证据；原图、坐标系、resize 与渲染身份必须一起保存，模型自己确认位置也不取得正确性权威。[必要方法与反侧](https://arxiv.org/html/2602.16455v1)支持这种先修“在哪里”、再读“是什么”的有限接口，但严格数值读数仍近零，多轮位置修正不单调。至少三次调用对一次调用并未匹配完整推理预算，渲染、重新编码与错误自确认都有成本；低成本一次读取已足够或修正不稳时保留原 one-shot，精确读数则仍需独立核验，不能借图表局部收益授予通用视觉自反思保证。<!-- source-family:SF-2026-ARXIV-2602-16455 -->

感知 codec 还可以有意降低局部信号强度而非可逆地改变 quantization step：按空间 uncertainty 将 latent 除以 `m≥1` 后量化，decoder 不反缩放，让低 SNR 区域更多由固定生成 prior 补细节。若 auxiliary decoder 只消费其中四个 channels，再由 BLIP 从该重建图生成 caption 供同一 prior 使用，caption 可不增加 wire bits，却仍是已有解码支集的派生条件，不是传来了新环境事实。必须把结构保真、感知候选与细节真实性分验；channel energy 也不等实际信息量。累计消融不足隔离各项因果，受限 runtime 中 encode 更快但 decode 更慢；entropy、aux decoder、caption 与 prior 全链付费。细节真值或 decode 预算更重要时，保留普通可逆量化、原 codec 与较保守操作点。<!-- source-family:SF-2026-ARXIV-2602-21591 -->

主动观察也可进入同一自回归轨迹，而不经每轮外部规划调用：离散标记提出是否继续聚焦，当前 hidden state 回归连续区域，crop 编码后作为新视觉状态接回未完成的推理。训练要分开普通答案 token 与观察动作的责任，先以文本和区域监督建立路径，再以动作收益及仅在正确回答条件下启用的面积正则约束“看哪里、看多少”。小 crop 本身不是好证据，答错时不能靠少读区域领取奖励。<!-- source-family:SF-2026-ARXIV-2604-21079 -->

该分支省去独立规划往返，却仍支付 crop 编码、新视觉 KV 与路径依赖；若持续保留新增视觉，缓存随观察数增长，不是旧完整输入的 exact 复用。错误区域会自确认，过强面积惩罚还可能删去必要细节。Qwen2.5-VL 单图任务的受限结果不覆盖视频或生产 tail；静态证据充分、额外动作不合成本时保持固定读取，取证不确定时扩大区域或回退完整观察。

还有一条不同于逐轮 acquisition 的静态 crop 分支：对同一图像分别进行有、无 query 的两次 Prefill，用首个生成位置的 attention 正差，经 head/layer 选择形成区域，再固定该 box 作答；同一区域 mask 还可供另一轮 logits 对比使用，但 attention selector 与 logit contrast 是两个观察对象，不能共用“定位正确”的结论。选中的层、head、正差聚合、坐标/缩放与 mask 映射应共同定义这个表示接口；这些是部署验收要求，不宣称原实验已验证完整 guard。[必要方法与反侧](https://arxiv.org/html/2602.04304v1)只支持受限 VQA/定位与短答案设置，首步 attention 不是因果充分证据，也不代表整个 Decode 中持续有效。双分支 Prefill、crop 处理和对比 logits 需要额外计算及显存，即使分派两块设备并行也不是零成本；坐标失配、crop 漏掉上下文、长答案质量或净时延不合要求时，回退全图、固定 crop 或不使用对比分支，保留原始证据与独立答案验收。<!-- source-family:SF-2026-ARXIV-2602-04304 -->

同一图像还可以在 Decode 中由受限 decider 重读，而不取得新的 crop 或现场 observation：主模型先提出 candidate tokens，margin 很小时，让另一视觉模型只读原 image、prefix tail 与这组候选，选当前 token 并生成一句派生描述，供后续有限 evidence pool 复用。[受限解码对照](https://arxiv.org/html/2602.21497v1)的 bbox 只作 annotation，不重编码到打分；同图与同源模型的 sentence 仍是 proposal，不能冒称独立 micro-observation。Candidate 外的正确 token 无法由这条选择器恢复，decider 未见原问题也会丢任务条件；raw mixture 总质量未必为1，margin 与 top probability 不授 calibrated confidence。分组件对照支持角色分工，却没有匹配全部调用预算或证明唯一 gain 因果；额外 decider、文本池与解码计费，更多调用可收益饱和，阈值随 workload 重新校准。候选漏真值、描述自确认、成本或正确性回归时，保留原 Decode、完整图像读取与独立答案 Gate，不把 repeated read 等同真正 acquisition 或事实认证。<!-- source-family:SF-2026-ARXIV-2602-21497 -->

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

训练人口还须区分‘任务至少需要哪些信号’、‘本次实际给了哪些输入’与‘哪些样本被放进同一cohort’。可以用分模态标注提出required-modality集合，再按该支持集或兼容集合组织训练、限制所暴露输入，并分别评价缺失、恰好满足与冗余信号；这改变表示的训练条件，不是在线reliability sensor，也不证明标注得到客观最小充分集。[有限多模态对照](https://arxiv.org/html/2602.11596v1)同时改变input与batch构成，不能把全部差额归给组内归一或宣称普遍降低方差；完整配方及部分单模态切片仍有反退。训练标签规则下把缺失样本标None，也不认证开放输入不足时可靠拒答，表示分离不等内部因果grounding。模态隔离生成、标注/对齐、编码、rollout和过滤历史均计费；支持集误标、shortcut或真实缺失分布失配时，回完整信号训练、静态cohort和独立缺失切片验收，事实与Unknown继续由外部证据承担。<!-- source-family:SF-2026-ARXIV-2602-11596 -->

训练分配也不必等待在线 reliability estimator：若联合训练过度依赖一条易学模态，可先对原始各路输入做 patch DCT，组合低、高频分量形成频谱比例代理，经历史 bank 平滑后，让比例较大的分支取得较小的梯度系数，或调节辅助分支 loss；原 fused loss 仍保留。这是把输入 prior 接入优化的受限选择，不是测得模型的真实因果依赖，更不等于缺模态时补回信息。[同 host 的 gradient/loss/hybrid 与频谱规则控制](https://arxiv.org/html/2602.22644v1)显示位置和代理定义会改变收益，hybrid 不在每个缺模态切片都更好，完整输入也可退步；从头训练的适用性不能直接转授 pretrained fine-tuning。输入尺度、signed 高频分母、采样窗口、bank 历史与权重参数都影响代理，正 offset 不认证分母始终安全。DCT/bank、辅助 heads 和训练回归计费，部署移除模块只省在线支路，不免除训练费用，也不能用模块孤立计时宣称端到端收益。频谱与任务贡献失配、正常质量或缺模态回归时，保留静态训练权重、原 robust host、真实监督及专用单模态回退；部署 fusion 仍需独立 reliability Gate。<!-- source-family:SF-2026-ARXIV-2602-22644 -->

训练时的伪标签选择还要把“支持够不够”与“是否仍值得学习”分开。固定标签域内，一条受限分支要求弱增强的 fused prediction 高置信，且至少一条高置信 unimodal prediction 支持同标签，再对强增强各路施加一致性；对 fused 仍高置信却未满足该条件的样本，不自动弃去或同等信任，而用噪声鲁棒损失参与训练。其[同配置选择对照](https://arxiv.org/html/2602.22917v1)中，严格全部一致并不比 fused 加至少一模态支持更好，disagreement 分支改用普通 CE 也退步；这支持可靠性与数据利用率的条件取舍，不证明 consensus 或高置信就是真值。共同错误、空选择集合和目标域变化仍需验证，同标签边际也不能推出条件分布不变。多路 encoder、增强、少量真实标签、prototype/translator 与训练都计费，派生 missing-modality feature 不能冒充观测；标签域、阈值或正常质量失配时，保留真实监督、保守选择和专用单模态路径，不把局部动作分类收益转授通用域不变性。<!-- source-family:SF-2026-ARXIV-2602-22917 -->

还有一种 reliability 相关分支只存在于训练，而不在部署新增 sensor：加入 nuisance token，允许它读取 semantic patches，却阻止 patches 反读它，再用 clean/degraded alignment、distortion contrast 与 orthogonality 约束训练表示；部署时丢弃辅助 token，只消费原语义路径。这是单向信息接口与辅助目标，不是在线 fusion gate，更不能由向量正交或预设独立性认证因果 `do` 干预。需分别回归 clean/degraded 表示与实际 retrieval/generation；有限对照中部分 encoder 的 clean 指标下降，两阶段恢复也有退步。额外 token、成对数据、训练目标与执行校验均付费，“移除支路”不等 profile 已证零成本；漂移或净收益不合要求时保留原 encoder、显式恢复和独立成对适配。<!-- source-family:SF-2026-ARXIV-2602-22013 -->

## 对齐不是把向量拉近这么简单

冻结原视觉/文本 encoder 后，为新概念优化一个可读的 text token，比重训整套模型更容易局部更新；但只把 token 拉向几张参考图，会让相似类别一起吸向相同视觉 cue，既损伤区分度，也改变原语义邻域。一条受限分支先以语言候选和视觉过滤形成局部 coarse/fine 邻域，再在其 PCA 方向上分别约束粗语义锚与细粒度负例，同时保留 image alignment；这改变适配目标的分工，不是把相似度最大当成新概念已学会。[LiteEmbed 的局部对照](https://arxiv.org/html/2601.09661v1)中，更高 image-text cosine 并不对应更高分类准确率；较高/较低方差方向的语义解释仍只由有限类别支持，候选与 encoder 版本改变后须重新验收。<!-- source-family:SF-2026-ARXIV-2601-09661 -->

这个接口保留原 CLIP 路径，却仍支付候选生成、PCA 与每个新 token 优化费用，并需分开回归原类别、竞争类别扩展与下游 consumer；冻结 backbone 不等零训练。没有 mask 真值的非零 coverage 不能证明定位正确，生成用重建目标替换 alignment 也不是同一个 token 产物无损通用。邻域误导、语义/区分度退步或费用不合适时，保留 base text token、直接参考图检索与已验证的 prompt/adapter；需要生成时另签训练目标和 decoder 接口，不以分类或检索收益自动授完整多模态兼容。

新概念也不一定要先优化一个 text token。若模型已能跨参考图辨认对象，可从每张参考图生成描述词，用词到 visual tokens 的 attention 作为选择代理，保留高分 tokens 并恢复原 patch 顺序；将这些原 projector 输出与概念名称一起缓存，后续作为 soft prompt 与新图共同读入。这省下每个新概念的梯度更新和参考图重复编码，却不把 attention 高或名称相同当作主体身份真值。多视角分别提取后拼接，也仍可能保存背景、近似对象或冲突来源。

这一[受限概念对照](https://arxiv.org/html/2603.09771v1)还按模型估计的主体面积缩减 token 数，并用一次有分割标注的校准选择层；零每概念训练不等无监督、无制备或全模型兼容。模型、projector、层/选择规则、参考顺序和名称须共同版本化，面积代理和少量 tokens 不保证细节覆盖；更多参考或更小 memory 也可能使识别、VQA、precision 或 latency 退步。校准、参考描述/attention/面积提取、存储与上下文读出、检索及原任务回归均计费；误识别、来源冲突、换模型或预算不足时，保留原参考图、普通检索/完整 tokens、经核的 token/adapter 适配和拒认，不让缓存向量批准个人身份或持久事实。<!-- source-family:SF-2026-ARXIV-2603-09771 -->

语言模型已有类别关系，也不意味着 projector 可以把任意视觉分组接入该关系。诊断跨模态泛化时，应分别声明语言预训练先验、视觉 encoder 的文本监督、leaf/hypernym 正负例暴露与图像 split；仅去掉某类别的 positive 监督，不等于该字符串从未出现。一种成对控制保留词汇层级关系，分别在同一视觉大类内或跨视觉大类重排 image–leaf 绑定，比较保留与破坏类目 coherence 时的 held-out hypernym 表现。[冻结 encoder/LM、仅训练 projector 的英语视觉 taxonomy 对照](https://arxiv.org/html/2603.07474v1)支持输入结构影响此受限泛化，但不证明语言先验无用、任意跨模态迁移或唯一内部因果；未显著差异也不等统计等价。细类监督、反事实绑定、projector 训练与按类/seed 评价均增加成本，相关类别不能扩算独立样本。关系或视觉结构不稳定、任务尚未学会时，保留真实类目监督、原 encoder/专用 readout 及独立任务评价，不凭熟悉类别名认证新模态 grounding。<!-- source-family:SF-2026-ARXIV-2603-07474 -->

### Caption 是不对称的辅助证据，不是图像替身

让视觉模型先生成 caption 再交给语言模型，复用文本推理能力且接口简单；caption 一旦遗漏或错误，又会成为强语义锚点。更稳健的分支并行保留图像直答与 caption 辅助路径，用 confidence gate、information gain 和来源权重决定融合、拒绝或回退。Captioner 只拥有 evidence proposal，原始视觉状态保持独立 identity，answer gate 决定是否采用。

双路径增加计算和校准成本，两个分支也可能共享同一视觉偏差；低分辨率、低风险或 caption 质量已知稳定时，单路径仍可用。冲突无法消解时应回到原图复核或拒答。现有 exact-v1 只支持作者的模型与视觉问答任务，不证明该 gate 给出事实置信度。<!-- semantic-body-binding:SF-2026-ARXIV-2605-01733 -->

Caption与原视频的竞争还可以进入训练reward，而不只决定推理融合。一条[有限视频分支](https://arxiv.org/html/2602.17555v1#S3.SS4)先由同一MLLM生成多粒度caption，再构造并修订带时间戳的event graph；时间先后边不自动是因果边，生成后自校也不是独立视觉真值。训练时将response到video和graph tokens的attention mass比作为代理，仅在参考答案相似度≥.4且参考时间IoU≥.3时激活；这个accuracy门依赖训练reference，不是部署时可直接签发的grounding证书，attention上升也不证明答案因果读取了视频。作者EVSG/DC与加减该reward的局部对照支持这一接口选择，但正文3B与表7B身份不一致，故不采用精确提升；caption、graph、训练和推理都使用同一baseline，还保留共同遗漏。8A100、4096prompt/2048response、8rollout/B16/1epoch之外的precision与完整总费用未披露，多次caption、graph refinement、额外graph tokens和attention reward仍计费。应绑定视频/时间窗、graph来源、token groups/聚合、accuracy gate与模型版本，并分别验收回答与定位；代理、预算或独立视觉证据失配时，保留原视频直读、稳定caption辅助或专用时序检测，不让结构与attention代替事实验证。<!-- source-family:SF-2026-ARXIV-2602-17555 -->

当对象与关系可以显式构造，caption 之外还可选择可 render 的 scene IR：先从图像预测实体、连接及带约束的 annotation，再让后续推理消费这份结构。确定性 renderer 使同一 IR 可以回画为图，但可执行、画面清晰、结构与原图一致、答案正确仍是四种验收；parse 成功不能代签 constraint fidelity。原图、坐标/实体命名、IR schema、renderer 与 annotation 身份必须共同保存，不能把合法容器当完整视觉事实。<!-- source-family:SF-2026-ARXIV-2602-18745 -->

[可 render 结构监督的受限证据](https://arxiv.org/html/2602.18745v1)来自平面教科书几何：code/caption/none 相同输入比较支持局部收益，parse 与 solve 差异小，而 annotation 正确率与 solve 更相关；相关性不证明唯一因果，segment F1 也不覆盖全部图形与度量语义。多个生成/语义验证角色使用同一模型，数值检查不消除共同错误；生成、验证、渲染与额外 IR token 训练均付费。开放图像、IR 不足以表达目标、重构或净收益不稳定时，保留原图读取、caption 辅助与专用检测/独立核验，而不把这一结构分支外推为通用视觉理解保证。

即使 canonical graph IR 不变，render/serialize 形式也可以按 query 与 consumer 选择。先在有限可验证图算法人口上，对同一 query 的多种图形布局、edge-list/set/matrix 记录正确性与 response 长度效用，再训练只读 query 的 router 选择消费形式；这不重新批准 graph 真值，也不保证任意 renderer 都完整保存标签、方向与权重。效用标签属于具体 consumer，response-only 预算还漏掉 input/render 成本；前置多形式、多次 probe、router 训练和渲染必须结算。小随机图支持集不等任意大拓扑，跨 consumer 的 response token 还可增加，不能写成通用节省。身份、成本或迁移不稳定时保留固定形式、原 IR 与独立算法验证。<!-- source-family:SF-2026-ARXIV-2602-21864 -->

Caption 的信息覆盖还可能被首句 summary 捷径掩盖：延长文本不保证 encoder 真正消费后续细节。一条受限训练分支仍保留原完整 long caption，只从新增 short-caption 分支去掉首 summary，再作不保句序的子采样，并将 PAD 前置以改变有效文字位置；它不是删掉所有长描述或 training-free 修复。[DeBias-CLIP 的必要对照](https://arxiv.org/html/2602.22419v1)支持首句与位置敏感性的局部诊断，却把句子语义可独立消费当近似条件，不能直接用于顺序决定意思的叙事。前置 padding 在 DOCCI 有退步，另一 encoder 仍残留位置偏差，short/long 目标的最佳权重也不同；attention 更均匀不证明全部细节已理解。数据改写、联合训练与跨位置/长短文本回归均有费用，故全局检索与细节覆盖分验；顺序、人口或质量失配时保留原 caption/encoder、任务监督或专用细节读出，而不把一份配方视为无损对齐。<!-- source-family:SF-2026-ARXIV-2602-22419 -->

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

目标冲突还可能来自学习信号接入的空间，而不只是 loss weight。视觉 encoder 的全局对比特征适合类别区分，diffusion reconstruction 则要求条件保留可重建细节；把两项直接作用在原 feature 上，可能让同一次更新面对相反梯度。一条受限分支先冻结 denoiser 与 encoder，训练 projector 让视觉条件接入既有 diffusion；再冻结 projector，通过 denoiser 的 predicted-noise 空间施加对比信号来更新 encoder，使同类条件的噪声预测接近、异类分离，并保留 ground-truth noise 正目标。改变的是监督接入位置与训练顺序，不是证明增加一个生成模块就免费兼得判别与细节。<!-- source-family:arxiv:2603.04803v1 -->

这个分支增加冻结生成模型的训练计算、projector 对齐与噪声采样成本；noise target 是重建目标，不是图像事实 authority。DCR 的特征散度推导依赖映射的正则性，重建近似还要求负例分离和有界噪声范数，不能据此声称任意模型梯度冲突已消失。作者在受限 CLIP/SigLIP、CC3M、Stable Diffusion 与视觉评价上比较判别和细节，SD-XL 条件接口不匹配也会退步；未证明通用下游能力或部署收益。目标不冲突、生成条件无法稳定对齐或训练预算不允许时，保留普通对比训练、独立重建与保守加权目标。[必要机制与对照](https://arxiv.org/html/2603.04803v1)见 §4.1–4.3、§5.1/5.4。

即使总目标不变，负例之间也在竞争梯度。InfoNCE 的正例吸引项可分为 hard negative 与其余负例的概率质量；大量容易负例的总和仍可能压过单个困难负例。给 hard-negative logit 加 margin，可以改变两类排斥信号的相对分配，但也改变正例概率，不能把它解释成绝对总梯度不变的搬运。词语 concreteness 可辅助选择或调权，却只是生成质量代理，不拥有负例确实语义错误的 authority。<!-- source-family:SF-2026-ARXIV-2604-13313 -->

困难负例有假负例与生成噪声风险，全部移除容易负例又可能损害通用表示。[作者的受限对比训练](https://arxiv.org/html/2604.13313v1)中，自适应 margin 相对固定 margin 的部分收益很小，通用切片也可退步。因此应把组合关系区分与通用检索分别验收，并计入生成、筛选和训练成本；普通对比训练、人工核验的困难负例与保守固定权重继续共存，而不是把更强排斥当作对齐普遍更好的证据。

共享视觉计算还会改变 pair 与负例的人口：同一图像可以在一次 causal forward 中接续多个 query turn，分别抽取 embedding，再与独立文本 target stream 做对比训练。后续 turn 的前向读取只包括图像和已有历史；训练中后续 loss 的梯度可以回到先前共享表示，这与先前 turn 前向读到未来答案不同。它摊销的是重复图像编码，不把同图多个相关 pair 变成同数量的独立图像；后续 turn 也可只作训练监督，部署仍用 initial turn 的单次 embedding。<!-- source-family:SF-2026-ARXIV-2602-06393 -->

这种扩充必须按图像与 augmentation lineage 管理负例：同图派生的其他 positive 若仍留在分母，会成为训练制造的假负例；按身份排除这些 counterpart 是局部控制，并不证明所有同图、不同问题或候选答案都语义等价。[MuCo 的受限对照](https://arxiv.org/pdf/2602.06393v1)中，去掉同图 logit mask 后 fine-tuning 表示明显退化，支持该数据构造下的身份检查；有效 pair 数、独立图像数与负例人口却同时变化，不能由计算估算签发等样本质量或端到端加速。多轮文本、合成 query/target、筛选与训练均付费，去历史的消融也只支持局部 history 分支；teacher 失真、负例身份不明或检索回归时，保留普通单对训练与真实 held-out 评价，而不继续放大相关监督。

继续适配开放的图文 encoder 时，还可能只有预训练权重而没有与当前目标匹配的训练统计。直接把 Adam moments 与全局对比目标的逐样本移动统计清零，虽然启动简单，却改变了最初几步的更新条件。一条分支先固定权重，在目标数据上累积一、二阶梯度 moments 与逐 pair 的归一化统计，再开始更新 encoder；恢复的是当前权重、数据和目标下重新估计的统计，不是找回未知的原预训练 optimizer state，也不是普通学习率 warmup。随后用平方 hinge 的 pairwise loss，使正例相似度已比负例高出 margin 时停止该 pair 的排斥梯度，避免持续把语义相近的未标注 pair 推远。停止条件只是相似度差，不认证真负例身份；margin 过大仍会过度分离假负例，过小又可能留下真负例。<!-- source-family:SF-2026-ARXIV-2601-09859 -->

这个分支用额外冻结阶段的 forward/backward、moments 和逐样本状态换取更平稳的 continued adaptation，状态仍须绑定数据、权重与 objective identity。TuneCLIP 的受限 CLIP/SigLIP、DFN 和检索对照中，完整逐样本统计相对只恢复 moments 的增量较小，监督 Flickr 上普通全局对比损失又优于 hinge；因此收益不能全归因于统计恢复或假负例纠正。作者两阶段墙钟约为单阶段的 1.5–2 倍，八卡 A100/H100、选模协议和数据变化不能外推为通用对齐收益。已有匹配状态时保留真实 resume；负例可靠时保留普通对比目标；适配退化或预算不足时回退冻结 encoder 与原检索基线。[必要机制与反侧](https://arxiv.org/html/2601.09859v1)见 §4.1–4.2、§5 与 Appendix E/H/I；通用 checkpoint 恢复语义仍由第 35 章负责。

混合模态 pair 还要分开三种校准对象：按 query 与 target 各自活跃模态平均得到双方温度，再取 pair 温度，改变的是 logit 锐度；逐行选择负例与调整 negative aggregate，改变的是梯度面对的人口；把 query 与 positive 合在同一 batch 求共享 whitening 变换，再比较两端 covariance，改变的是二阶几何，而非每个模态分别白化。几何重叠、较尖 logit 和困难负例都不拥有 pair 相关性真值，也不自动消除假负例。[受限训练机制与反侧](https://arxiv.org/html/2601.03666v1)显示过强几何权重或负例控制可退步，组件联合消融不能证明每项独立因果。训练 batch 的变换尚不是部署冻结协议；温度、负例选择、共享变换、checkpoint 与索引兼容性需要另外绑定和校准，这是工程要求，不冒称原实现已有完整 guard。额外训练、校准与漂移维护须计入预算，支持不足时保留普通固定温度对比训练及独立检索评价，不把训练几何收益授在线排序或生产 SLO。<!-- source-family:SF-2026-ARXIV-2601-03666 -->

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

但同一空间位置还不能同时代表“在哪里”和“哪个主体”。参考图像与驱动 pose 的强 pixel binding，在位置已对齐、单主体时简单有效；位置或主体数不一致时，却可能新造一个 pose-aligned 人物而丢掉参考外观。一条受限训练分支随机平移/缩放 pose、平移或复制 pose encoder 输出的 pose features，先解除默认位置绑定，再分别用 text 的主体/数量条件与 segmentation mask 重建语义和空间对应；mask-only 可把不同人的肢体拼成一个 composite，说明目标区域被选中不等于 subject correspondence 已建立。语义对应仍是生成条件，不是真实 instance identity 或观测真值。<!-- source-family:SF-2026-ARXIV-2601-11096 -->

[受限绑定对照](https://arxiv.org/html/2601.11096v1)在 frozen Wan/LoRA 与混合训练数据中支持这项接口，却未完全隔离数据配比、主体数和原生多主体 baseline；有限人评也不支持所有 identity 指标最优。训练期 unbind/mixed-data 被旁路，不代表 text、mask、pose encoders 与主体标注免费，更不保证任意 count 或主体都正确。数量、mask、外观或 motion assignment 失配时，保留原图/pose 身份、显式主体对应与较简单的已对齐单主体路径，分别验外观和运动，不由空间 mask 或语义文本替真实身份签发证明。

空间接口也可以先显式形成地图，再交给语言模型消费：从视频检测、分割与几何重建得到对象的估计 centroid、axis-aligned bounding box 和房间尺度，同时保留离散 grid 与连续 metric coordinates；随后用确定的向量、距离或 box 运算构造空间推理中间结果。确定性属于给定地图上的计算，不属于上游对象身份、尺度或物理位置真值。它与直接融合 2D/3D tokens 并存，改变的是估计几何如何变成可检查的中间接口，而不是自动获得真实世界模型或行动授权。<!-- source-family:SF-2026-ARXIV-2601-11442 -->

[受限地图推理对照](https://arxiv.org/html/2601.11442v1)在同一 25% 训练子集上，预测地图加显式推理为 58.8、移除推理为 54.0、无地图基线也为 54.0；换 ground-truth 地图达到 73.7，说明感知误差仍限制这条分支。全量训练的总体结果只有 61.0 对 60.9，Relative Direction 反而从 80.5 降到 69.8，不能把有限监督下的收益写成所有空间任务的优势。多级检测、分割、重建、map 构造与额外监督都付费，原文没有闭合端到端 latency/硬件成本；对象遮挡、单位/坐标不可靠或任务依赖地图之外的信息时，应保留原视频、直接 token 融合与独立几何/行为验证，而不由精确算术给估计地图签发物理真值。

空间规划的中间输出还可以把每个对象phrase与紧随其后的离散box交错生成，再交给独立renderer消费，而不是先写一段纯文本推理、最后才汇总布局。这个接口让对象语义与拟定区域保持显式配对；box仍是规划条件，不是观测真值、严格几何可满足证明或对象因果定位。Planner的内部self-check不成为独立verifier，renderer/model/坐标网格和grounding训练目标须分别绑定。[SCoT的受限对照](https://arxiv.org/html/2602.11980v1)里较小planner有质量退步，内部约束比率也不等strict success；两阶段grounding/aesthetic训练、额外规划tokens与render均计费，不因未改架构宣称零成本。配对、坐标或画面质量失配时，保留纯文本计划、显式layout与独立约束检查，必要时重新规划，不让流畅空间叙述替最终图像验收。<!-- source-family:SF-2026-ARXIV-2602-11980 -->

有了这些元数据，还要区分“位置如何进入 attention”与“模型能否读出时间单位”。把视频位置拆成时间、高度、宽度三轴，再分别分配旋转编码维度，是一种清晰的空间—时间接口；但按连续维度块分配时，各轴可能只得到部分频段。一个替代分支在频率维度上交错分配三轴，使每轴都覆盖较完整的频率范围。它改变位置特征的分配，不改变帧采样时刻，也不认证视频时间同步；三轴分块在短图像或原任务表现足够时仍可保留，长视频收益须在具体模型、帧数与训练条件下验证。<!-- source-family:SF-2025-QWEN3-VL -->

旋转角度又不天然等于“第几秒”。另一层接口将可读 timestamp 与视频帧交错送入 decoder，并允许以秒或时分秒表达定位结果：时间既参与内部位置计算，也成为可消费、可输出的语义条件。代价是额外输入长度、时间格式及监督的一致性；舍入、错误标注或不匹配的采样协议仍会制造定位错误。模型给出的时间只是 proposal，真实时钟和 provenance 仍由采集记录授权。[Qwen3-VL 的公开机制说明](https://qwen.ai/blog?id=qwen3-vl)同时改变位置、跨层视觉注入及训练配方，不能把联合性能全部归因于其中一个接口，更不能推出物理行动或任意长度视频的可靠性。需要这些保证时仍须检查原始时间轴与独立定位评价，而不是以可读输出替代同步校准。<!-- source-family:SF-2025-QWEN3-VL -->

位置合同还会决定输入能否等待输出。把视觉与生成文本串成单一连续编号，在离线或先看后答时简单；流式输入若必须知道上一回答长度才能给下一视频段编号，就把感知进度耦合到输出。一条替代分支让视觉和文本各自使用连续 position group，同时仍通过 cross-modal causal mask 限制能读取的视频段与文本历史：解除的是编号依赖，不是取消因果可见性，也不使 position 取代真实时钟、capture timestamp 或 provenance。<!-- source-family:SF-2026-ARXIV-2601-06843 -->

[TRUE 的 GDPE 分支](https://arxiv.org/html/2601.06843v1#S3)支持这种 position/mask 分责，固定 offset 的 GIPE 是另一选择；OSPE 的自引用式未决，不补写其执行规则。Qwen2.5-VL、20k训练样本与受测视频协议只给局部质量取舍，streaming GDPE 的 CIDEr 也低于 Interleave，流畅度不等语义正确。新增位置空间需要训练和输入身份验收；理想重叠的 sum→max 推导不证明 GPU 已并发或端到端约2×加速，额外 KV、资源与同步仍交推理层验证。编号、mask 或质量失配时，保留普通 interleave、离线编码与先看后答，而不以解除一个表示依赖宣布真实实时 SLO。

在音频中，同样可以增加独立 timestamp-token 接口，在音频特征之间插入时间标记，以预训练数字子词的语义均值初始化并冻结这些新增 embedding，再通过 SFT 学习如何消费它们。模型侧的可读时间表示与采集侧的真实时钟仍是两个 owner：前者产生定位 proposal，后者负责单位、同步误差和 provenance，不能用生成的秒数反写传感器事实。<!-- source-family:SF-2026-ARXIV-2604-13715 -->

[有限音频对照](https://arxiv.org/html/2604.13715v1)在 25 Hz 特征与 0–30 秒、0.04 秒粒度的标记网格中观察到语义初始化的收益，随机初始化反而在部分任务退步。它不是仅加几个符号而无需训练，也不证明更长音频、任意采样率或精确物理定位：词表与输入长度增加、接口 SFT 和后续训练都计入成本。原始 timestamp 必须继续归档；网格范围、时钟或模型变化时重新校准，不适配时保留原位置编码与显式时间监督，而不是让新的表示取代同步合同。

当 consumer 只需定位事件，还可改变输出接口而不增加逐秒文本生成：从 decoder 的音频 frame 表示接一个数值 head，按声明的 frame interval 转成事件时刻。这个分支把 AR 数字字符串的表达成本移到 frame-level 预测与后处理；模型仍只产生定位 proposal，采集时钟、有效范围和 provenance 继续由原始记录授权。训练与部署必须绑定 frame grid、audio encoder/decoder revision、head 和时间单位，不能把数值输出直接当物理时间事实。<!-- source-family:SF-2026-ARXIV-2602-10230 -->

[40ms网格的有限对照](https://arxiv.org/html/2602.10230v1)支持该接口与 token 定位的局部取舍，多事件桶却不都改善，单事件与多事件应分别验收。其 conditioned-on-count 公式与单事件 loss 表述不一致，不作为统一可执行 loss 或理论保证；最高局部速度比也不等所有长度、batch 与并发下的端到端收益。超出时长、采样率或事件分布时需重新校准，head 定位或质量不合适则保留 timestamp-token/显式监督和原时钟记录。

时间接口也会决定用户侧信号的含义：回答含糊的视觉问题时，整段观看的平均 gaze 不一定对应正在询问的对象。一个受限分支以 spoken question onset 选取 fixation 时窗，再作空间过滤，把坐标 marker 叠在原图上送入 VLM；它保留场景上下文，而不是把关注区域裁掉后当作完整证据。[十人受控设备实验](https://arxiv.org/html/2602.16138v1)支持这种时间×空间输入接口的局部效用，但窗口在同一数据上选择，距离相关不证明 intent 因果，crop 退步也不证明所有裁剪都无效。gaze 属于用户意图的 proposal，不是模型内部 attention、事实真值或用户授权；原图、时窗、坐标系、校准误差和过滤回退都需随输入保存。采集硬件、speech 同步、等待与判分增加成本，研究级眼动设备和大学人群不能代签消费设备可用性；信号含糊时仍保留原图 VQA 或语言澄清，而非以 gaze 替代证据和权限检查。<!-- source-family:SF-2026-ARXIV-2602-16138 -->

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

还可以在解码后的 frame feature 空间分配空间与时间预算，而不读取 codec residual：参考帧保留 $S$ 个空间 tokens，后续各帧用共享 encoder 提取 feature，再将其相对参考帧的 feature 差投影为一个 motion token，形成 $S+T-1$ 的抽象表示。这里省的是逐帧重复传入下游模型的空间 tokens，仍需编码各帧，不能与直接消费压缩视频原语、减少 decode/encode work 的分支混同。单 motion token 把时间覆盖换成每帧变化的表示瓶颈；参考帧与后续内容失配、细小新证据或复杂运动可能超出其容量。保留 dense tokens 或更新参考帧是这些条件下的工程回退选择，不是作者已实现的自动 reset，也不意味着像素无损。受测局部任务的预算收益不保证所有理解任务改善，更不能由 $S+T-1$ 推出端到端速度。

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

压缩单位还可从逐帧 patch 改为跨帧软区域。一个轨迹 tokenizer 先由 learned queries 对视觉特征软分组，再用受区域 hard mask 限制的第二级读取形成少量 tokens；多 slot 让同一区域保留不同粒度，随机 slot 数训练则改变压缩预算。软分组允许任务梯度影响区域，但前级特征仍有 stop-gradient，hard mask 也不认证对象身份或跨片段同一轨迹。[TrajTok 的必要对照](https://arxiv.org/html/2602.22779v1)依赖外部 segmentation/tracking 伪标签与大量预训练，移除 detach 或 hard mask 可退步，分辨率或深度增加也非全部任务单调获益。长视频仍分片形成 tokens，总量随片段增长；与仅能消费较短视频的 pooling 比较不能把输入覆盖收益全归因 tokenizer。伪标签、两级读取、encoder 和适配训练都计费；短视频、小对象或身份不稳时，保留普通 patch/pooling、显式 tracking 与原帧回读，而不把少量区域 tokens 当永久对象状态。<!-- source-family:SF-2026-ARXIV-2602-22779 -->

### 长视频从固定输入窗口走向可回读的视觉记忆

逐帧或均匀采样适合短视频与完整证据优先的任务；固定窗口装不下持续到来的画面时，单纯压缩所有视觉 token 虽可延长输入，却仍让最终回答读取不断增长的历史。另一条受限路线把逐 clip 产生的 visual KV **派生**为两种不同状态：小容量的 context memory 随下一 clip 传播时序信息，压缩的 local memory 写入 clip memory bank；回答时再按问题检索少量 clip。写入、跨 clip 传播与按需读取因此不再由同一组活跃 KV 承担。原 clip 的时间位置、模型与压缩版本以及读回映射需要可回指，否则“找到了相关记忆”无法证明未遗漏关键帧。这是表示和证据身份的责任；真正的 KV 容量、调度与尾延迟仍由推理运行时验收。

这样做以压缩误差、检索遗漏、陈旧片段和索引/重复编码成本，换取固定回答预算下处理更长视频的可能。查询尚未知晓或全局时序关系比局部片段更重要时，按问题选取的记忆尤其可能失效，应保留密集短窗、固定采样或回读原片段的路径。[FlexMem 的原始实验](https://arxiv.org/html/2603.29252v1)只覆盖两类 LLaVA 视频模型、五项长视频与一项流视频任务，以及其单卡 GPU 条件；它的“无限长度”是迭代处理接口，不是无损、无限容量的视觉记忆，也未证明生产并发与 SLO。

持续流还可在写入前选择何时形成新事件，而不是先为每个固定 clip 生成记忆。连续 encoder 的语义变化、motion 与预测残差可共同提出 event-admission，触发记忆更新及 decoder；这些信号只负责选择，不是真实事件边界。冻结 VideoLLM 不等于无需训练 predictor，阈值、预测器、时间范围和写入策略也应绑定版本。它用监测与校准成本减少重复处理，却可能漏掉短事件、把噪声当新事件，或因未触发而长期不更新；查询需要完整时序、阈值漂移或证据不足时，应回退固定采样、密集短窗与原片段回读。[有限 streaming 对照](https://arxiv.org/html/2601.15655v1)支持该控制分工，不证明三信号各自完整因果、无限历史无损或生产 tail-SLO。<!-- source-family:SF-2026-ARXIV-2601-15655 -->

<!-- source-family:SF-2026-ARXIV-2603-29252 -->

与“先为所有 clip 写入压缩记忆、提问时再读”不同，主动观察分支由当前问题决定下一次读取的时间段、帧率与模态，通过读取工具取得视觉、音频或 transcript 后再继续推理。它能避开无关输入并回看短暂事件，却把证据遗漏、读取历史与额外推理/tool round-trip 变成新的责任；少载入 token 不保证更低的端到端时延，短片或完整证据优先时，固定读取仍更简单可靠。

主动观察还需要把训练时的“值得再读”标签与部署时的证据充分性分开。一个受限分支用指定 base/teacher 模型对及有、无读取工具的答题结果划分 direct、adaptive 与 active 样本，再分别训练直接作答或继续采帧；这比奖励所有成功调用更能约束无目的读取，但类别反映的是该模型对和工具轨迹的相对能力，并不是画面已充分、未读片段无关的证书。特别是两模型都答错也可能被归入 active，不能由类别反推出下一次读取必能恢复答案。工程上应连同模型/checkpoint、初始采样、检索索引与采帧工具保存标签身份，并对实际读回证据独立验收；这是部署 guard 的推导，不是原实验已验证完整实现。[必要方法与反侧](https://arxiv.org/html/2602.04094v1)中的帧数节省仍需另计全视频索引、额外模型推理与工具 round-trip，固定采样在部分负载仍合理。标签迁移或读回质量不足时，保留 unknown，回退均匀采样、补读原片段或不提交答案，而不以少读帧数授完整质量/时延保证。<!-- source-family:SF-2026-ARXIV-2602-04094 -->

问题分解成多个检索 query，也不保证独立 selector 能选好证据或旧 reader 能读好所选帧。一条受限长视频分支先由低分辨率 preview 形成 queries，对密集帧计算多 query 相似度，再由可训练 sampler 选固定数量的高分辨率帧，并让 query/reader 与 sampler 接受联合任务训练。[固定帧预算及同所选帧对照](https://arxiv.org/html/2602.22932v1)中，冻结的多 query 加 top-k 可弱于单问题或均匀采样，同一批帧交给冻结 reader 也仍较弱；因此 query 分解、选择规则与 reader 适配应共同验收，但不证明所有任务必须联合训练。最终回答虽 mask 掉 preview，仍保留其派生 query/history，不是未曾消费这些信息。preview、密集 CLIP 编码、query 生成、采样器预训练/RL 与重复轨迹均计费，总计时仍比 uniform 更慢，文表开销比例冲突不采用；相似度峰值奖励不是信息充分性证书，所写 REINFORCE 梯度型量也不当可执行标量目标。证据覆盖、读出质量或净成本不合格时，保留单问题检索、静态/均匀采样与原 reader，不让更复杂选择替代原片段回读。<!-- source-family:SF-2026-ARXIV-2602-22932 -->

读回多个 region 后，还要决定它们在哪里交互。独立视觉 encoder 再由语言侧融合，适合可复用单图特征与固定输入；问题要求比较不同局部时，另一分支把当前 query embedding 与各 region 的 patch 放入同一次视觉编码，在指定层做跨 region interaction，其余层仍保留图内或窗口计算。返回语言模型的因而是已按问题相互作用的 features，而不只是独立编码结果的拼接。region 的原帧、crop 范围、回读轮次与 query 身份应随特征保留，attention 图也不能替代原始证据。<!-- source-family:SF-2026-ARXIV-2602-11073 -->

这种接口增加 query encoder、跨图计算与多轮回读费用；[有限同训练步数与移除 query/多图的对照](https://arxiv.org/html/2602.11073v1)支持局部交互分工，不证明所有任务都优于独立 encoder，更不把不同训练预算或有矛盾的每轮 latency 比例当作端到端收益。长视频的全量 joint encoding 仍可能不可承受，裁剪也会遗漏证据；预算紧、query 不稳定或 grounding 不足时，保留独立编码、固定采样和回读原片段。主动选择决定看哪里，表示交互决定如何比较已读区域，二者都不能认证未读内容无关。

### 用表示几何区分重排与扩展

把 Attention 与 FFN 都概括为“融合信息”会掩盖二者可能承担的不同责任。更细的诊断可以同时观察 residual update 是否引入新的子空间，以及 token mixing 带来的信息增量：在一组受限的视觉语言模型中，Attention 更接近在已有子空间内重排跨模态关系，FFN 则更像扩展可表达方向；部分层替换实验还提示，learned visual routing 可能存在冗余。<!-- semantic-body-binding:SF-2026-ARXIV-2605-05668 -->

这不是 Attention 普遍无用的结论。证据只覆盖两个模型家族、15 个变体、七个 benchmark 和被选择的层；相关统计也不能代替端到端因果验证。若同类诊断或替换不能在目标模型与任务复现，就应保留 learned Attention，并用 causal ablation、质量回归和 serving cost 共同决定是否改变结构。

几何变化还应由具体输入操作定义，而不能从“图中文字方向”直接推成通用 OCR 电路。可对同一图像的原版和文字移除版取 residual 差，在独立训练样本上拟合 PCA 方向，再按层投影干预；inpainting/blur 与等量非文字区域移除的对照用于检查方向是否只是编辑伪影。该方向只属于这套 encoder、层与操作，不是全部 OCR 信息或唯一文字通道。[Where Vision Becomes Text 的受限实验](https://arxiv.org/html/2602.22918v1)中，方向可跨数据集使用不等于最佳层可迁移：部分模型计数改善而阅读或空间任务退步，另一架构早层干预全面伤害；模型规模与架构又混在比较中。成对处理、方向拟合、层扫描与逐 token 投影均计费，单次 greedy 评价不授稳定增益；删除文字线索损伤正常任务或方向迁移失配时，保留原 forward、外部 OCR 与显式 readout，分别验操作特异性、干预因果和旁侧能力。<!-- source-family:SF-2026-ARXIV-2602-22918 -->

视觉steering也可先分离两类对照：把grounded与blind状态差分先平均，再相对blind时hallucination−unknown方向作投影/正交化；在校准对照中选择具有正向平均分离Δ的最深层，并用quantile阈值决定是否注入。平均、投影、层与gate的次序是干预身份，不能改成逐sample投影后平均；这只定义所测人口的一条方向，不证明已找到独立truth cause，输入根本缺证据时也不能凭steering恢复视觉事实。<!-- source-family:SF-2026-ARXIV-2602-11824 -->

[REVIS exact-v1](https://arxiv.org/html/2602.11824v1)的方向提取与阈值各用100样本，层扫描、校准、judge和部署注入均付费；去gate时模型分支可能没有收益或collapse，较强干预会伤utility，局部CHAIRI也可反退。未披露完整硬件/运行配置的TPT不授统一延迟或免费可靠性。失配、blindness或质量回归时，保留原视觉输入、外部OCR/grounding和Unknown输出，分别验支持域、回答质量及干预成本，不把更少幻觉标签当内部faithfulness。<!-- source-family:SF-2026-ARXIV-2602-11824 -->

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

分布差异不只发生在 rare code：decoder 若只见 encoder 提取的 latents，服务时却消费生成模型预测的 latents，即使格式一致也可能出现 patch-like artifacts。一条训练分支让 decoder 直接接触预测 latents 并继续接受视频重建监督，同时冻结 encoder，避免适配 decoder 时又移动生成器所学习的 latent 坐标；编码重建与预测 latent 的生成质量因此是两个需分别验收的对象。该适配增加采样与训练成本，生成分布、codec revision、latent 长度或 decoder 采样配置改变后仍需回归；更多解码步骤也可能改善一种感知指标却损失逐像素保真。受限视频对照不证明预测 latents 与真值的配对实现已独立核验，也不授通用纠错器或所有质量目标同时改善。原 encoded-latent decoder 在重建任务或预测分布已相容时仍合理，适配失败则回退该路径、保守生成配置或拒收失配 artifact。<!-- source-family:SF-2026-ARXIV-2602-04220 -->

### Connector shortcut

模型依赖 caption、layout 或 metadata shortcut，而没有真正消费目标 modality。需要遮蔽、反事实和跨分布测试，而非只看平均分。

视频中的 shortcut 还需要检验“答案应变”与“答案应保持”两种关系。单条 QA accuracy 即使很高，也可能只是从静态 cue 猜对：对 direction/order 一类 dynamic question，语义保持的 temporal reversal 或 flip 后答案应按声明关系改变；对不依赖该变换的 static question，答案则应保持不变。评测与训练因此要冻结 original/counterfactual pair、transform revision、问题路由与 expected relation，并使用 strict pair accuracy 拒绝只在一侧猜对的固定答案。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-21988:start -->
Transformation/router 只定义 expected relation，原始标签或独立 verifier 仍拥有 correctness，optimizer 只消费通过 Gate 的 paired reward；成对一致也不等于事实正确。该分支暴露单帧和语言 shortcut，却增加双路视频 rollout、router/transform lineage 与 normalization 成本，也可能因 flip/reversal 改变了本不该变化的语义而制造伪监督。若 transform validity、router agreement、pair correctness 或 general-video regression 失败，应停用 relational reward，回退 verified original examples、显式 temporal labels、完整视频评测与人工审核的 counterfactual。现有证据只覆盖作者的短视频、两类 transform 与披露模型，不证明任意视频编辑都保持语义或已学到长程因果理解。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-21988:end -->

没有可核验的 expected-answer relation 时，还可以用输出分布构造较弱的辅助监督，但它不能继承成对标签的真实性权限。一条受限训练分支为同一图像准备 clean、随机 patch mask 与扩散 noise 三个 view；先在 clean view 采样回答，再沿这一条回答的每个 prefix，分别计算当前 policy 在三种 view 下的 categorical token distribution。与任务奖励共同优化时，最大化 `KL(clean || mask)`、最小化 `KL(clean || noise)`，并对两个扰动 view 的 entropy 加负项；前者鼓励对证据删减敏感，后者鼓励对拟保语义扰动稳定，而低熵项只限制均匀分布的平凡解，不认证答案正确。它改变的是同一轨迹上的概率约束，不是让扰动各自生成答案后取得 verified pair reward。<!-- source-family:SF-2026-ARXIV-2601-06801 -->

[三视图的必要原证与直接反侧](https://arxiv.org/html/2601.06801v1)没有证明随机 mask 一定删除关键证据，或 noise 一定保持所需语义；扰动强度必须绑定任务与输入。在作者受限切片中，medical mask ratio 从0.2增至0.6反而使对应平均指标从74.3降至71.4，完整目标也不是所有单任务或组件对照都最好。额外两个 view 的 forward、沿轨迹的概率统计、正则调参与任务回归均付费，八次推理取均值不等八个训练 seed；噪声退火的有限终点也不严格为零。原文 top-p 配置互相冲突处不作为确定执行 recipe，不由整体平均提升授予普遍稳定或 genuine grounding。扰动语义、任务质量或成本越界时，停用该辅助项，保留可靠任务奖励、已验证的输入反事实和成对答案监督；分布差与低 entropy 都不能代替独立 grounding 评价。<!-- source-family:SF-2026-ARXIV-2601-06801 -->

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

多张参考图还提出另一个身份问题：二维相对 RoPE 可以描述图内位置与相对距离，却未必明确标记某个 token 属于哪张图。一个替代分支保留相对空间编码，在图组之间插入共享的可学习 separator，并叠加显式 image-index embedding，让边界与来源不只靠邻近位置推断。采用 normalized index `j/N` 时，总图数 N 改变也会改变同一 j 的编码坐标；因此显式编号不等于跨任意图数保持不变的身份。[受限多图编辑证据](https://arxiv.org/html/2601.05572v1)的两图到五图扩展主要是定性结果，部分消融仍有指标反侧，不能授任意数量泛化或无混淆保证。新增 separator、训练与输入 packing 需连同图顺序、总数和模型版本验收，这是表示接口的工程要求；图数固定、原相对位置已足够或质量未过时，保留已有 RoPE 和较少参考图，而不是让新增编码认证内容或几何真值。
<!-- source-family:SF-2026-ARXIV-2601-05572 -->

相对几何还可以由 query 所在视图定义，而不只由全局 reference 坐标给出。标定相机的 token 射线先在若干固定深度锚点升至 3D，再投影到当前 query 视图，以普通 2D RoPE 编码投影位置；深度锚点是接口假设，不是逐点测得的 depth truth。同一 view 退化为原 2D 规则，多 view 则让同一 key 在不同 query-view 下拥有不同位置视图，camera calibration 与编码器共同定义这个 derived state。<!-- source-family:SF-2026-ARXIV-2604-18747 -->

数学接口可以复用 2D attention，不代表执行只保留一份无条件通用 KV：把 query-view 维移到 batch 并重复 K/V 会增加几何计算、内存和读写，view 或标定改变后不能沿用旧 derived position。[受限重建、检测与 matching 对照](https://arxiv.org/html/2604.18747v1)有 RGBD 指标退步，联合训练 recipe 也不支持单因果归因。标定不可信、锚点范围失配或预算不足时，已有 2D 位置、显式 3D 编码和任务专用几何接口仍应共存；生成与环境状态还须各自验收，不能把位置规则升级为物理真值。

多视角共享射线字段，不一定要共享同一个 condition encoder。pinhole 与超广角 fisheye 可以都用六维 Plücker 接口，但各自的 unprojection 和方向统计仍不同；保留原生 pixel/token grid，再按 semantic camera identity 分派投影族 adapter，可以避免仅凭相同 shape 让 backbone 猜测相机类型。跨视图 attention 可在同一 latent 时刻合并不同长度的 tokens，以标定射线和 view identity 建立联系，而不把不同投影网格的二维位置直接视作可比；全局 ego-motion 与逐像素几何也应各自保留来源与职责。

[混合 rig 的受限实现](https://arxiv.org/html/2609.21712v1)用额外 adapter、标定/pose 处理与 overlap mask 换取原生视图接口；训练与推理时的投影族、语义 slot 和 token-grid packing 应一致，这是由接口推得的验收要求，不是论文已证明任意标定都可靠。现有评价没有独立隔离投影族 adapter 收益，生成/几何代理和定性长 rollout 也不证明物理闭环安全。标定、projection dispatch 或 packing 不可靠时，保留独立相机处理、已有显式几何接口或受限重标定，不把共有字段维度当作 encoder 可互换的证据。<!-- source-family:SF-2026-ARXIV-2609-21712 -->

点云理解也不必总由重几何 encoder 产生 tokens：几何 superpoints 内平均池化后，可按多条坐标 space-filling curve 排成序列，沿 token 轴做窗口低频混合，逆排序、平均和残差回到原身份，再结合稀疏图与 merging 形成紧凑输入。它用几何邻接 prior 和有损汇聚替代一部分 learned context，不是取消所有 tokenizer/训练，也不由多条排序证明任意 tie-breaking 下的严格 permutation invariance。[同数据/优化的 pooling 与混频控制](https://arxiv.org/html/2602.23153v1)支持局部分工，额外 pretraining 行须分账；拥挤场景的非欧氏长距离关系、细纹理与空间关系仍可失败，外部 segmentation proposals 也仍可提高读出。序列 FFT 与 FFN 内逐 token 的 channel FFT 必须分开，后者不构成跨 token 通信；low-frequency gate 的参数化、图邻接描述及 OT pooling 的归一化/符号未核实现，不照抄为几何保持配方。坐标排序、图/SVD、merging、LoRA 与训练均计费，tokenization FLOPs 不是完整 LLM 时延或部署 SLO。几何 prior、细粒度证据或压缩质量失配时，保留原几何 encoder、更多 tokens、显式 proposals 和专用验证，而不让紧凑表示认证真实三维状态。<!-- source-family:SF-2026-ARXIV-2602-23153 -->

已有多视图重建但只需语言定位对象时，不必立即把几何纳入统一生成模型；另一条分支在稀疏 voxel 之上维护指向实例中心的三维 group feature、权重与 ID 字典，逐 view 把 2D mask 升到 3D、投回新 view 匹配/合并，再让消费者读取 group ID、center 与 caption。这让共享对象从高维 language field 变为显式 group 及文本描述，却仍是由分割/重建派生的实例 proposal；centroid 投票和 mask 重叠不能认证同一真实对象，caption 中的关系也不是新增物理观测。[OpenVoxel 的受限对照](https://arxiv.org/html/2601.09575v1)支持这种静态读取分工，不授任意场景或 query 的无训练理解。<!-- source-family:SF-2026-ARXIV-2601-09575 -->

实例分组先做合并，还会丢掉后来 part query 需要的粒度：问相机灯仍可能返回整台相机，中心字段也未提供完整 part-of 图。Canonical caption/query 减歧义仍依赖 MLLM，较小模型甚至严重回退；需保留原 view/mask、group 合并来源和可重建路径，而非只存一份“稳定”文本。已有 scene fitting、SAM2 重 prompt、caption 与全 map 读取都付费，3min 分组估计不含全部预训练/重建、也不授生产 SLO。对象支持、视角/粒度或模型预算失配时，回读原图与细 mask，保留 learned field 或专用几何工具；需要跨轮编辑时，再把 revision 与 native 几何状态交给后续接口，而不是由 group ID 取得几何真值权限。

已有对象字典也不要求把语言提到的每个对象都强行绑定到当前地图。局部观察可能只覆盖描述的一部分；可将点云投成 BEV，再以 node ID、语义标签和像素中心提供实例表，训练模型先输出哪些描述可与当前 node 对应、哪些应为 null，随后再读出二维位置。这样把“是否有对应证据”显式放在坐标生成前，而不是用同类别最近对象填满全部引用；实例表、投影坐标和语言 binding 属于同一份接口身份，却仍都是待核 proposal。

[受限部分绑定对照](https://arxiv.org/html/2603.09826v1)以两局部区域的对象中心距离制备 valid/null 监督，推理时由模型预测，不拥有真实位置的距离 oracle。平面 BEV 和无显式边的实例表会丢高度与细节，模板查询、已有语义/实例标注也不代表自然开放描述；更好的绑定相关性不保证几何正确，原检索协议下部分距离阈值仍反退。地图构建、投影与标注、binding 监督/LoRA、额外 AR tokens 和解析、实际位置回归均计费；support 缺失、ID/坐标失配、解析失败或预算不足时，保留 null、原图/点云、专用匹配或定位工具，不让 JSON 身份和连续坐标批准导航行动。<!-- source-family:SF-2026-ARXIV-2603-09826 -->

先由独立 3D reconstruction pipeline 生成 mesh，再把结果作为多模态模型的只读输入，职责清楚且容易单独验证；当任务要求多轮理解、生成和局部编辑保持同一几何身份时，stateless sidecar 会丢失跨轮 mesh state。另一条分支把 3D primitives/mesh 表示纳入统一 token contract，并让 modality-specific experts 共享同一 identity 与 revision。

它提高跨任务连续性，却增加 tokenizer/mesh discretization、长 Context、几何一致性和编辑回滚成本。模型拥有 proposal，不拥有物理几何真值；identity 保持和生成 fidelity 也不能证明真实世界尺度或可执行性。单次重建、精确 CAD 或安全关键几何仍应由专用工具与确定性验证承担。

<!-- source-family:SF-2026-ARXIV-2605-16745 -->

碎片位姿与整体shape若各自独立推断，职责清楚，却可能把同一对象的局部证据与补全假设隔开；可选分支复用同一3D VAE，把可变长度fragment编码为decoded latent，逐层让SE(3)pose分支与whole-shape latent分支双向读取，再联合求解几何proposal。[受限消融](https://arxiv.org/html/2602.22629v1)在固定image条件下支持joint相对assembly-only的局部差额，但共享预训练prior与额外生成容量/训练不能完全拆成单adapter因果；geometry PA/CD也会漏掉对称或可互换part的语义错误。双向接口会同时传播错误：薄壳pose含糊、SDF/TSDF codec漏掉细件或将开放表面补成封闭shape，均可污染另一分支，补出的geometry不是新观测，更不是robot action。两阶段训练、21层双路、32张H200约三天与在线联合求解都付成本；codec、fragment尺度/身份或生成prior失配时，保留assembly-only、显式几何匹配/专用重建与人工验证，不用完整shape的可信外观签发物理真值。<!-- source-family:SF-2026-ARXIV-2602-22629 -->

part tokens 有独立编号，也不保证图像证据已按真实实例分配：多个 part 的联合 mesh 可以像整个场景，单个 part 却仍碎裂或重叠。独立 cross-attention 易于复用；若需要对全部 part 与 patch 一起分配覆盖预算，可在每个去噪步计算带边缘邻域 prior 的 entropic transport plan，按 part 归一化后软调节其读取的 K/V，再由原 softmax 完成 token 级融合。该[受限结构控制](https://arxiv.org/html/2602.22785v1)是全局竞争 prior，不是硬 one-to-one：正 floor 仍允许共享贡献，后续 softmax 不保持 transport marginals，非负 simplex 也不保证每个 part 有正预算。拥挤小对象可被合并漏计，普通 attention 残余分支则是保细节的共存回退；CCA 残差聚类与 argmax 可视化都不能认证实例真值。Sinkhorn、边缘估计、逐步 K/V gate 与更大 token/步数都有费用，增加 gated 层可继续改变质量/时延，单图几何 proxy 不证明真实三维身份或物理性；硬件/精度未披露时不授部署 SLO。边缘、域或 part 预算失配时，保留普通 attention、显式 segmentation 与专用几何验证，Ch24 只接手后续采样路径。<!-- source-family:SF-2026-ARXIV-2602-22785 -->

相机状态也不一定只能作为外部估计器输出的只读condition。若要在同一接口里做camera-controlled生成与camera estimation，可以在canonical reference frame中，将逐像素射线方向与原点的向量和编码成三通道raxel，复用视频VAE，再用明确的modality和grid位置身份进行video/camera联合去噪。它把相机从sidecar参数变成可生成、可修订的状态；同shape和chain-rule分解仍不证明网络已学到正确joint，更不是外部估计器必定失效。<!-- source-family:SF-2026-ARXIV-2604-09429 -->

这种兼容用额外camera分支、训练耦合与几何解码换接口复用；coarse ray grid、canonical normalization、modality RoPE与VAE版本必须可追溯。[受限实现](https://arxiv.org/html/2604.09429v1)在14B视频模型外增加6B分支，decoded rays经Procrustes恢复pose，focal估计假设principal point居中。它的Plücker对照同时改变codec，不能单独归因表示更优；生成循环一致也不是外部3D真值，动态场景和内参偏离仍需验证。精确标定、安全几何或训练预算不足时，独立pose工具与只读camera conditioning继续合理，后续World Model还须验真实transition。

逐帧视频 token 仍可能把同一对象在不同视角和时间中的身份复制多次。Track-aligned 表示把稳定背景与动态对象分开，并让轨迹、相机和时间成为 token identity，从而把 frame archive 压成可修订的 4D state。它获得存储与生成上的复用，却依赖 track、camera geometry 和 static/dynamic disentanglement；视觉可重建不证明物理动力学，真实 transition 仍由下一章负责。

<!-- source-family:SF-2026-ARXIV-2609-12874 -->

轨迹可读与最终回答能消费轨迹，也是两种不同能力。若模型已能从视频生成带 timestamp、entity ID 与坐标的 grounded track，而任务答案仅由终态位置决定，可用合成文本轨迹接答案，只对答案 token 施加监督，将已有 tracking 输出接入问答；这不等于用文本学会新的视觉 tracking。Loss mask 只移除轨迹位置的直接监督，不冻结共享语言参数，也不保证原 grounding 无回归。[SGCoT 的有限对照](https://arxiv.org/html/2603.08436v1)只支持此简化消费接口，运行时仍须从真实视频生成轨迹，身份跳转和错误终态会传给答案，不能以最终答对批准全部中间状态。Sampling rate、时间/坐标 schema、对象 cue 与模型 revision 要共同绑定，分别验收轨迹 grounding、终态读出和完整任务；模型既有 tracking 预训练、合成数据、语言适配、视频编码、轨迹生成/解析及回归测试全部计费。遮挡、相近对象或需要额外场景证据的 referring query 超出支持时，保留原视频回读、独立 tracker、短窗和 Unknown，不由结构化坐标或流畅 CoT 授真实对象身份。<!-- source-family:SF-2026-ARXIV-2603-08436 -->

若离线多视图需要一个可被新 query 读取的紧凑场景，另一条分支把全局 softmax 的 KV 关联写入固定尺寸 MLP fast weights：整个视图集合或各 shard 从同一初态计算写入梯度，再合并更新；patch values 的局部 2D 混合为写入加入邻域，随后冻结场景权重供查询。这是离线双向 scene fitting，不是因果流式记忆，也不继承通用 KV 精确回读；写入目标与生命周期由 Ch22 承接。[VGG-T3 的必要对照](https://arxiv.org/html/2602.23361v1)显示预训练初始化和局部混合有用，却仍有 camera pose 退步，并改用直接 pointmap head 避开 pose 误差传播。固定 MLP 也不等于整个定位状态固定：camera head 仍保留全部 mapping camera tokens。额外适配训练、inner updates、局部卷积、梯度通信与相机读出都计费，局部 A100 多卡计时不授全流程常量内存或 SLO；原内层 dot-product loss 的优化符号未核实现，不采用其可执行配方。要求精确位姿、逐视图证据或场景写入失配时，保留 softmax、多视图显式重建与专用定位工具，而不把可查询权重当几何真值。<!-- source-family:SF-2026-ARXIV-2602-23361 -->

## Token Hierarchy 可以承载不同时间尺度

音频等高带宽模态若只用单层离散码，要么语义结构过粗，要么 token rate 过高。分层 residual quantization 可以让上层 code 承担长程语义和结构，下层 code 补局部声学细节；相应生成器也可分为 global sequence model、local refinement 与连续 decoder。

层次化表示提高可控性，却引入 codebook synchronization、跨层 error propagation 和更复杂的 bitrate/latency 预算。它是表示分解，不证明某个公开音乐模型的质量结论可外推；Ch24 只接手后续生成与修正机制。

高频触觉进一步说明“同一时间轴”不等于“同一采样密度”。接触事件稀疏时，复制成 dense visual stream 会浪费预算并稀释信号；更合适的 contract 是为 tactile event 保存独立 rate、timestamp、sensor calibration 与稀疏预测目标，再由共享语义层消费。代价是异步对齐、漂移和缺失事件，传感器或 embodiment 改变时不能继承旧 token identity。

<!-- source-family:SF-2026-ARXIV-2609-12549 -->

## Streaming Multimodal Identity 不止是 Token Type

实时全双工系统中，用户音频、视频、文本与 assistant 输出会并发到达，输入不会在生成开始前自然结束。表示层必须把 token 绑定到 timestamp、speaker/turn、observation revision 与 interrupt frontier；fusion 只负责产生共享表示，runtime 才决定哪些输出可以继续、取消或提交。

流式视频还应分开“学会顺序”与“此刻需要读历史”两种干预。训练可将带timestamp的帧内容打乱，让模型恢复顺序后回答；推理则先读当前窗口，只有答案分布entropy高时才用pooled frame相似度从可见历史做coarse-to-fine检索并重新回答。顺序监督没有消除timestamp线索的shortcut，低entropy也只是无需检索的proposal，不是真值证明；coarse阶段漏掉的证据不能由后续fine检索自动恢复。[有限消融](https://arxiv.org/html/2602.22142v1)中，仅添加timestamp的微调会退步，顺序训练与history cache分别改变结果，仍不足以识别唯一视觉因果机制或所有任务收益。离线合成数据、额外训练、历史编码/KV与第二次回答都付费，阈值曲线和不同样本表格不授统一最优或真实deadline；检索失配、旧帧混淆或阈值失准时，保留固定近期窗口、更广原始历史与显式人工/外部查询，不将cache命中当作新观测。<!-- source-family:SF-2026-ARXIV-2602-22142 -->

训练对齐的时序支持与推理时可见的输入前缀，是另一对不能合并的身份。跨语语音不必始终提供逐词源—目标对齐：可先保留 sentence 对应关系，为目标句首与句内停顿采样延迟，让训练数据包含源句尚未结束就开始输出的轨迹，再优化质量与语义 lag。放宽的是监督配对粒度，不是去掉 transcript、TTS 时间戳或 ground-truth reference；过程奖励可以使用当前已开始句的完整译文，却不能把这份训练标签解释为部署时已经听到的输入。<!-- source-family:SF-2026-ARXIV-2602-11072 -->

这条分支先建立提前输出的 exploration support，再调整等待策略；[Hibiki-Zero 的有限反侧](https://arxiv.org/html/2602.11072v1#S4.SS7)中，只学整句结束后发声的 base 经 RL 仍未学会提前开始，去掉句内随机 silence 也使质量与 lag 退步。它不证明任意 RL 都能突破监督支持，低 lag 还可能牺牲长语音内容与音色保持。数据合成、codec 缓冲、reward 与重复生成都有成本，语义 lag 指标不是设备 wall-clock SLO；时序或质量不可验时，保留逐词对齐、完整句等待与保守 turn-taking。无论训练 reference 多完整，下一层读取日程仍只能消费实际到达的 prefix，输出 commit/cancel 继续由 runtime 决定。

流式语音还可以把“再读一点”与“输出文字”放进同一个训练词表：WAIT 表示继续消费音频，文字 token 表示提出输出；同时用因果 encoder 与 cross-attention mask 限定每个 decoder 位置能读到的音频前缀。这不是取消等待策略，而是让它与文字条件分布共同学习。一个 decoder dilation 参数把若干音频 embeddings 对应到一个逻辑输出 slot：间隔越短，对齐更细，却会让 WAIT 占据标签和 autoregressive forward；间隔越大，文字可用 slot 更少，快语速可能溢出。timestamp、alignment、dilation、prompt 占位、WAIT padding 和溢出处理应共同成为表示合同，不能把训练标签的时序对应升级为真实到达、内容正确或 runtime commit 证明。

过等待后的恢复还可单独训练：把一段文字标签向后移，制造累计 delay，但将人为插入的 WAIT 与此前历史从 loss 中屏蔽，使模型学习后续 catch-up 而不是模仿延迟；部署仍用有界音频/文字窗口，WAIT logit bias 只是质量—等待曲线的调节器。[有限语音对照](https://arxiv.org/html/2603.11578v1)中，延期微调缩短 lag 但若干翻译切片的 BLEU 退步，辅助 ASR 与 alignment、标签合成及额外训练也有成本；oracle 输出的理论 lag、generated lag、包含计算的 lag 与设备 deadline 必须分开。窗口丢失、alignment 漂移、长期 WAIT 或文字溢出时，保留外部 READ/WRITE policy、完整句等待和可复查 transcript，runtime 继续拥有交付与取消权限，不以“policy-free”或低 RTF 授予无损实时服务。<!-- source-family:SF-2026-ARXIV-2603-11578 -->

提前发声也可以只处理话语衔接，而让实质回答继续等待完整输入。一个双轨分支让小模型读取 partial ASR 选择 connective、先送 TTS，大模型在 final ASR 后再产生主回答；两轨消费的观测 revision 不同，不能把早发声写成主模型已经拥有完整输入。低 entropy/置信规则只是选择依据，诸如肯定或转折的衔接词仍可能暗示回答方向，这是需要验收的语义风险，不是天然无内容的安全填充。[DDTSR 的必要对照](https://arxiv.org/html/2602.23266v1)中，可用衔接机会因数据集大幅不同，部分主回答质量退步；同一 backbone 也不证明相同事实质量，重排与时序控制并非单因素。应分报 filler 首音、实质内容首音与最终质量，额外小模型/ASR/TTS、候选选择和远端主模型都计费，未披露远端硬件/并发不授设备 SLO；衔接不确定、最终转录反转或输出已难撤回时，保留无填充、完整输入等待及保守 turn-taking，实际播放和取消仍由 runtime 拥有。<!-- source-family:SF-2026-ARXIV-2602-23266 -->

表示可以早于完整输入形成，但模型此时允许读取多少 prefix 是另一项选择。一个闭式日程分支用输出进度、输入长度估计和预算参数构造单调 attention mask；它只决定每一步可见哪些输入，不拥有物理到达时钟、回复提交或打断权限。固定输入版的 length head 消费已完整可用的输入；真正流式的变体则只能从 arrived prefix 与上一窗口信息预测总长，以 arrived horizon 限制可见性。因果性保证以这些输入确实先到达为前提，不能将“mask不看未来”写成端到端 deadline 已满足。<!-- source-family:SF-2026-ARXIV-2609-20845 -->

这条路径增加长度 head、预测漂移和预算校准，也可能因等待不足漏证或等待过多延迟。作者 29M/四层 decoder 配冻结 CLIP/C3D/Whisper、单 T4 的实验只覆盖 window-synchronized 到达；异步到达属于条件证明，没有实测 live service。wait-k 的长度 head 职责不完全对称，流式 single run 的 test-clip bootstrap 不覆盖训练噪声；三 seed 修正还改变 ActivityNet 的最佳预算区域，LibriHeavy 差距落在 seed spread 内。因此采用可见 prefix 与实际到达的分工，不采用跨任务统一质量优胜；预测不稳或 deadline 不可验时，保留 wait-k、完整输入或外部 turn-taking，runtime 仍负责 commit/cancel，这是工程交接而非作者已验证的状态机。[必要日程与反证](https://arxiv.org/html/2609.20845v1)。

持续视频推理还可以把观察推进与文字生成拆成两个逻辑前缀：视觉、文字分别保留自己的 position axis，再用因果 mask 声明每个输出可读的已到达观测。一个双 KV 分支让视觉状态在一个 decode segment 内保持只读，文字状态继续 append；段间吸收的新帧不应被解释成已生成文字当时就见过的证据。这样避免强制所有模态排进同一位置序列，但表示接口必须把 segment、可见前缀和观测 revision 交给 runtime；具体 buffer 并发、同步与输出 commit 仍由推理系统拥有。

拆分状态并不消除 frame 编码、KV 读写或同步成本。作者的指针级 cache composition 是实现主张，未在本次核验其 kernel 或并发一致性；3B 与 7B 的质量对照也不支持统一优胜。尤其 decoder 暖启动时的首 token 计时，不能直接替代从首帧到输出的端到端延迟，论文两处口径未充分一致，因此不采用微秒响应保证。观测持续改变、deadline 紧或快照语义不能确认时，保留逐窗口完整输入、串行 interleaving 或显式同步边界，再验实际 freshness 与响应成本。<!-- source-family:SF-2026-ARXIV-2603-02872 -->

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

固定 centroid 方向仍是容易校准的干预基线，但同一偏移未必适合所有输入位置。一条条件分布分支分别收集 hallucinated/factual activations，用 per-head classifier 选择干预 heads，在两种未配对分布上拟合 Gaussian-mixture potential，再按当前位置与时间计算 drift 并注入噪声；它让修正量依赖当前 activation，而非给所有输入加同一向量。分布标签、head selection、potential 与采样规则因此成为 representation intervention 的共同身份；数学 transport 的对象是标注 activation 分布，不是可直接观察的真实“truth manifold”。

[受限原始证据](https://arxiv.org/html/2602.09528v1)只支持所测 VLM 的 object hallucination 分布干预，部分 POPE/GQA 切片仍低于固定 steering 对照，image/object 组合也非每项最优。混合分量、步数、噪声、分割和完整成本未充分披露，drift 求值与噪声不能称零额外计算，更不保证所有文本事实或能力无损。条件分布迁移、标签失真或正常能力回归时，应保留未干预、固定方向或显式 adapter 路径，以任务行为重新验收，而不由“更贴近 factual distribution”签发真值保证。<!-- source-family:SF-2026-ARXIV-2602-09528 -->

几何干预若直接用于净化表示，还要检查删掉了什么。一条无需重新训练 backbone 的分支从目标与非目标描述的 text embedding 各取 SVD 子空间，再把 image embedding 投到非目标子空间的正交补；它能移除落在该子空间内的分量，却也会移除目标方向与它重叠的部分。正交补是线性几何对象，“非目标”则由描述与编码器定义，二者不自动构成纯语义分离。描述构造、SVD/rank 选择与下游 probe 的成本仍存在，另训练的分类头不能算同一 training-free 人口；有限实验也有颜色或材质切片退步，依赖子空间重叠和非退化条件的界不能认证任意对齐。若目标信息与所谓噪声耦合，保留原表示、条件读取或显式 adapter，可能比不可逆地删除方向更稳妥。<!-- source-family:SF-2026-ARXIV-2602-05464 -->

净化也可以先限定允许修改的补空间：在当前图像定义的 hidden-dimension 视觉子空间中保留投影，再从其正交补构造 anti-prior 方向，将当前 hidden state 分为视觉、anti-prior 与剩余分量，按冲突/先验代理信号分别软缩小后两项。它与直接删除某个非目标方向不同，但保持所选视觉投影只是一条几何条件，不证明所有视觉细节、事实或后续生成都不变。[HulluEdit 的必要方法与反侧](https://arxiv.org/html/2602.22727v1)中，去 gate 可比原模型更差，完整干预也有计数能力退步；门控代理因此不能替代对象支持验收。原文 SVD 左向量与所需 hidden-dimension 基的维度表述不一致，这里只采用明确维度且相互正交的分解接口，不发布该记号为已验证实现。anchor 缓存、分解、逐 token gate 与残余缩放都计费，局部 TPS 还排除预处理；子空间失配、数字细节或原任务回归时，保留未干预、条件读取与显式 adapter，不让“不动视觉投影”升级为无损或全局稳定保证。<!-- source-family:SF-2026-ARXIV-2602-22727 -->

另一条净化分支不先给出硬正交子空间，而是在 matching image–caption 的 encoder 表示上共同训练稀疏 dictionary，用归一化 code 的相似性软约束两模态，再按各 atom 在两模态上的二阶能量比提出共享/模态特有分类和 mask。它把“删哪些方向”转为 learned code basis 与数据人口上的选择，不等于无需配对，也不由软 loss 证明潜在概念可辨、严格等能量或真实语义分离。Dictionary、配对来源、能量阈值、mask 与下游 readout 因而须共同绑定，而不是从较小 modality gap 直接签发无损表示。

净化后的检索必须区分原 encoder、完整 SAE 重建与 masked 重建；仅对重建 baseline 的保留不代表相对原模型无损。[受限 dual-encoder 实验](https://arxiv.org/html/2602.06218v1)中，LAION/COCO 的 mask 召回退步，中心化基线也可能更好，正则过强还会产生退化 features。即使内容与模态子空间正交，只有模态分量对候选的投影相同，或其差小于内容排序 margin 等额外条件，才可讨论排名保持；自适应投影仍能翻转排名。配对、SAE 训练、阈值搜索及单模态信息丢失都付费，完整成本未披露；新人口或任务回归时保留原 embedding、中心化、条件读取或显式 adapter，不把能量与字典稳定性当语义真值。<!-- source-family:SF-2026-ARXIV-2602-06218 -->

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

加入连续 reasoning tokens，并不保证模型会使用它们；完整视觉输入可能让最终答案绕过这条中间路径。一个受限训练分支保留完整图像的 intact stream，另给同题的 corrupted stream，将前者各 decoder 层的 latent states 移入后者，再分别约束答案分布和 answer 对 latent tokens 的 attention，同时保留两路 next-token 目标。它把潜在状态做成显式训练接口，而不是只增加一个可读 CoT 槽位；intact/corrupted 配对、扰动方式、转移层与 token 身份、loss 范围须共同保存。

这种特权训练转移仍付两路前向、状态拷贝与对齐成本，训练时完整图像信息不等部署时可获得的干净真值。[受限 CrystaL 对照](https://arxiv.org/html/2602.20980v1)中 blur 比若干空间扰动稳、8 tokens 优于 4/16，匹配整个 image/latent attention 图反而退步；原答案约束为 KL，所选 decoder 层的 answer→latent attention 约束为平方 Frobenius 范数，不是再一个 attention KL。对齐范围和破坏的语义必须另验，不能从 answer 改善或 attention 相似签内部推理 faithful；已发表不同预算 baseline 也不认证普遍更省数据。若扰动改变正确答案、latent 使用未得到独立检验或质量/总成本不合算，保留原视觉表示、直接微调、可读 trace 与外部 grounding，不让 latent 接口的成功自证事实或替代下述写入/读取故障诊断。<!-- source-family:SF-2026-ARXIV-2602-20980 -->

### Object Hallucination 需要分开视觉写入与语言读取

对象幻觉常被压成一个端到端错误率，但同一错误可能来自视觉证据没有进入表示，也可能来自证据存在却被语言 prior 覆盖。Dual-pathway circuit analysis 用层级定位和因果干预区分 visual-evidence write path 与 language-prior read path，使“看不到”和“不采用”成为不同故障。<!-- semantic-body-binding:SF-2026-ARXIV-2605-13156 -->

Circuit probe 依赖所测模型、层选择和干预定义，不能把相关 activation 当成唯一原因。诊断不稳定时，应回退输入/输出级的证据对齐、反事实图像和行为评测，不据单个 circuit 自动修复模型。

表示经过 contextual encoder 后，原文中哪个词说出了关系，并不决定内部哪个 token 承载它。在受控两物体生成中，随机文本 embedding 加位置的分支可由 relation head 把关系写成 image-position tag，再由 shape head 读取 tag 生成对象；T5 contextual embedding 则可把同一关系吸收到 object token 中。于是，遮掉显式 relation word 后输出关系不变，不能单独推出模型没有消费关系。应绑定 text encoder、position、token 类别与实际干预单位，再比较 head-specific ablation、tag 的 VO 注入或 object-token relation vector 替换，而不是只看 attention 强度。<!-- source-family:SF-2026-ARXIV-2601-06338 -->

[必要干预原证](https://arxiv.org/html/2601.06338v1)支持这种受限路径差异，权限只到三种 shape、两种 color、八种 relation 的 toy DiT 与所测 encoder，不能宣布所有自然图像或多物体使用同一电路；variance partition 和 attention synopsis 本身仍只是定位工具。相近 ID 关系准确率也不保证相同提示鲁棒性：添加 filler 的切片中，T5 分支关系准确率约下降40%，随机表示更稳，不能由“已有语言语义”推定关系组合一定更可靠。表示读取、白盒搜索、干预和独立质量回归均付费；未披露的完整硬件/运行预算不补成部署优势。路径或人口失配时，保留原 encoder、输入级反事实与可核对象/关系评价，不让较易解释的随机表示成为通用替代。<!-- source-family:SF-2026-ARXIV-2601-06338 -->

提示冲突还应绑定诊断人口与干预单位：[PIH 的有限计数实验](https://arxiv.org/html/2601.05201v1)先筛出原模型计数正确的图像，再施加诱导多报的 prompt，按单 head 的纠正率排名、选择模型相关 top-m 组合。干预将同一 head 全 token 输出的均值替换到各位置，不是关头，也不保证输出 magnitude 保留。因而所得排序只描述该条件人口中的提示服从，不是自然图像幻觉率或所有视觉写入路径的强弱。<!-- source-family:SF-2026-ARXIV-2601-05201 -->

内容复制、格式复制与正常任务须另计：Janus 原计数从 80.32 降至 79.41，Qwen 的正确格式复制率还会上升，不能把更少诱导内容等同所有视觉路径增强或无损裁剪。三种 7B、计数/颜色及首个非负数字的解析规则限制了人口，head/m 的选择与独立验收隔离未明；白盒干预、200–300 RTX3090 GPUh 搜索和质量回归都有费用。跨任务、解析或选择失配时，保留原模型、输入级反事实与独立行为评价，不从局部纠正率宣布唯一电路或在线普遍可用。

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

不用内部 late branch 时，也可在同一生成 prefix 下分别对完整 image+text 与 text-only 输入求 logits，以 `(1+alpha)*l_m−alpha*l_u` 形成对比输出，再用两概率分布的 symmetric KL 动态调节幅度。完整无图路径与 late-layer masked branch 不是同一计算接口或成本；较小分布差只是语言路径与视觉路径接近的代理，不认证幻觉原因或 grounding 正确。固定强度会伤部分 recall/count，动态超参也不普遍最优；额外完整 forward/KV 与分布统计付费，受测 regular decode 比两对比分支更快。绑定两输入、相同 prefix、概率与 logit 的角色及零差数值处理，并独立验收答案；过度抑制、接口失配或预算不足时回退原 Decode、固定幅度或外部 grounding。<!-- source-family:SF-2026-ARXIV-2602-22144 -->

不比较两路 logits，也可以把初始 image+prompt 的最后输入位置在最终 decoder 层的 hidden state 保存为固定 anchor，在之后每一步的指定层将当前最后位置状态与它作固定权重的凸混合，再继续后续层计算。这条静态分支干预的是内部表示，不重新输入图像、不等于 late branch mask，也不从与 anchor 更相似推出事实正确。逐层 Logit Lens 对最终 top-K 候选集的概率聚合可作 commitment-depth 诊断，但候选集取自当前模型最终分布，较早集中只是一项风险 sensor；它不能拥有外部视觉 support 的真值。<!-- source-family:SF-2026-ARXIV-2601-05939 -->

[受限三种7B视觉语言模型的对照](https://arxiv.org/html/2601.05939v1)支持静态 anchor 分支的局部取舍，不授普遍无损的“视觉加强”：LLaVA 的 AMBER coverage 从原50.4降为静态48.6，动态48.1更低，静态也并非处处胜动态。初始 hidden 读取、模型相关的层/强度校准和质量回归均有费用；动态版本为每个 token 先探测再注入而增加第二次 forward，不能把诊断成本归给仅向量混合的静态路径。v1 Eq8 的 `min(...,0)` 与正风险时增强注入的叙述冲突，故不采用该动态执行配方、不自行改成 `max`；这里只保留诊断与已明确的静态干预。Anchor 过旧、隐藏接口不可见、质量回退或预算不合算时，保留原 Decode、外部 grounding 和前面的两路对照。

音频反事实还要选择保留什么时间结构。完全移除音频适合检验有无模态影响，却会同时删除粗语义与瞬态线索；另一条受限分支把短时间变化平滑后重新编码成慢参考，让原始与慢路径在同一文本历史下预测下一个 token，再只在音频依赖较高且预测不确定的位置，对小候选集合施加正向 logit 差更新。这是时间尺度对照，不把差值当声学真值，也不证明语言 prior 已经被消除；输出仍须通过任务 grounding 评价。<!-- source-family:SF-2026-ARXIV-2604-15383 -->

对照是否有用取决于 decoder 能否利用该时间差。受测统一 audio/text decoder 的改善不意味着独立编码、拼接架构同样改善，最强模型的 speech 子集也有退步，因而不能无条件打开干预。两路编码、稳定性估计与独立 KV 状态增加 prefill 和内存成本：单 A800、3 秒音频/100 token、关闭 FlashAttention 且优化复用原路径 KV 的对照中，memory-bound batch2 decode 隐藏部分增量，但 prefill 约加倍，不是全服务零成本。时间扰动损伤语义、模型接口不可见或质量、成本不合算时，应保留原始 decode 与外部证据对照；第 49/56 章另验实际执行与 SLO。

是否启用这种对照，还应看原路径错在哪里，而不只看平均收益。在冻结同一问题、音频和输出协议后，把原始与对比答案配对，分开记录各类错误转正确、错误转另一类错误，以及原正确转错误；只有错误子集的纠正率，不能代表全人口净收益。[受限音频对照](https://arxiv.org/html/2603.09232v1)把“声称没有音频”“猜测或拒答”“附理由的错答”和“直接错答”按固定优先级分类，支持先诊断目标错误人口再选择反事实，但这些是 judge 的输出标签，不是内部推理根因；不同模型与任务的比例及收益不可直接迁移。语气更确定也不等于更正确，少见错误不能因图表省略而消失。配对生成、完整分母、标签抽核与独立校准增加费用；当原正确答案被破坏、标签或反事实语义不可靠时，保留原 decode 与外部 grounding，不用错误修复子集批准默认启用。<!-- source-family:SF-2026-ARXIV-2603-09232 -->

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

选择性视觉干预也可以保留原 visual input，改为逐 token 选择语言模型内部的对比分布。[一个受限分支](https://arxiv.org/html/2602.09825v1)结合 selected visual heads 的一致性、相邻 layer 的 token-distribution JSD，以及相邻 token 的视觉 attention JSD，动态挑选较稳定与较不稳定的 layer logits 做 contrast；随后与原输出概率加权，并把候选限制在原分布 top-20 support 内。这里的稳定性拥有 layer-selection proposal，原分布保留 candidate support，grounding evaluation 仍拥有接受权；它与先找不确定 token 再扰动视觉输入是不同接口，而不是“稳定层就是真值”。<!-- source-family:SF-2026-ARXIV-2602-09825 -->

相邻 token 未必指向同一实体，attention agreement 和 distribution stability 也可能共同稳定在错误解释上。作者的组件消融与 CHAIR/POPE 等任务都有反退，短序列中跨 token 信号较弱，候选层与加权参数依模型调整，不能授每个组件必然互补或普遍降低 hallucination。读取多层、多头及 unembedding 增加执行、HBM 与 latency 压力，training-free 不等零计算成本；原文未给完整端到端开销。Raw top-20 support 只是限制偏离，不提供模型风险校准或事实认证；grounding、语言质量或成本回归时，应保留原始 decode 或已有局部视觉干预，不把 layer contrast 变成无条件默认。

## Review notes

- `SF-2026-ARXIV-2603-10702` — Daily `2026-03-13`补查；[UniCom exact-v1](https://arxiv.org/html/2603.10702v1) §3.1–3.3/Eq1–5、§4.1–4.4完整Tables1/4/5、AppA/Table6/G。2+1+2=5，压缩轴与消费者分流具体差额深入；采用固定空间N压channel的受限操作点与Pathway I理解raw bypass，纯压缩六项退步、不同表示预算/训练费用和原codec回退近正文。不授无损、精准收敛加速、query唯一因果、全榜或生产能力；未核实现/复现。非准备者mar13_admission_review实际Source、完整owner局部及限定PRE通过；root窄写两段与本注，mar13_admission_review非writer实际顺读新增、完整局部和本人末注并回精确原证，POST通过，root回读接纳并释放窄锁；不授DAY。

- `SF-2026-ARXIV-2603-10360` — Daily 补查 `2026-03-13`；[exact-v1](https://arxiv.org/html/2603.10360v1) §2.3–2.4 Eq4–14、§3/Tables1–4与§4/Table5。2+1+2=5，首次生产/后续消费方向缓存的具体接口差额深入；root 非准备者实际必要 Source、Ch23完整局部与两段 PRE 通过，窄写两段后非 writer mar13_supplement 实际顺读新增、完整局部邻接和本末注并回对精确原证，POST通过，root接纳并释放窄锁；不授 DAY。仅采用受限接口与寿命责任；Eq10正加与图示subtract的语义差别、序列长度/位置对应、加性共同项条件均不补造为可执行实现。直接比较包含局部反退，CHAIR正文18.1对应表中Sen而非Ins；32.1/30.3ms每token与14924/14257MB不认证完整probe/编码/调参账或生产SLO。未核代码、图像像素、复现或部署。

- `SF-2026-ARXIV-2603-10370` — Daily 补查 `2026-03-13`；[exact-v1](https://arxiv.org/html/2603.10370v1) §3.1–3.3、§4/Table1、§5/Tables3–5/训练设置与直接限制。2+1+2=5，整体输入的几何请求/第二次消费协议具体差额深入；root 非准备者实际必要 Source、Ch23 完整局部与 PRE 通过，窄写两段；非 writer mar13_supplement 实际順读新增、完整局部邻接和本人末注，回对精确原证，POST 通过、窄锁释放。双条件监督不是真实必要性的因果证书，原能力退步与模型/投影更新、完整标签/执行成本近文；encoder 延后计算与 KV 复用未披露，不认证节省、图像曲线精数、代码、复现或部署。不授日级验收。

- `SF-2026-ARXIV-2603-10365` — Daily `2026-03-13`补充Mar12自然日；[GAE exact-v1](https://arxiv.org/html/2603.10365v1) §3–5/Tables1–8与直接D–I边界。2+1+2=5，compact semantic target producer及pixel瓶颈同维监督的具体缺口局部深入；只采用受限接口，readout排序、噪声/重构代价、RMSNorm非Gaussian或防collapse、全费用与旧codec退路近文。mar13_supplement准备，mar13_admission_review必要Source/actual owner/两段PRE通过；root实际写入，mar13_supplement非writer实际正文/完整邻接及本注回源POST通过，root接纳并释放窄锁；不授DAY、artifact核验或复现。

- `SF-2026-ARXIV-2603-11578` — Daily补查 `2026-03-14`；[exact-v1](https://arxiv.org/html/2603.11578v1) §3/4/5.1/5.3/6、Tables4–5、B Algorithm1/C3 Table8。2+2+2=6，WAIT/audio时钟→decoder slot与delay-mask训练的表示差额深入；BLEU/ASR反退、对齐/训练费用、oracle/generated/CA lag与真实deadline分开，Table3转换缺行不采用排名。root实际必要原源/完整owner邻接与作者逐字PRE通过，两段实际写入后由非writer mar14_supplement 顺读完整邻接、本人末注并回对精确原证，POST通过、窄锁释放；无实现核验或复现，不授普遍因果真值/实时SLO或日级验收。

- `SF-2026-ARXIV-2603-11320` — Daily补查 `2026-03-14`；[exact-v1](https://arxiv.org/html/2603.11320v1) §3/Eq1–8、§4/Tables1–4、Appendix A System/Ng。2+2+2=6，理解连续入口/生成压缩码→外部AR稠密展开的表示差额深入；质量反退、Table2/§4.3 CLIP冲突、分别训练计时、额外全局token与stage2权重适配保留，不授免费/无损/全负载加速。root必要Source/actual owner提案经非作者独立PRE通过，已窄写两段；独立复核者实际顺读新增两段、完整邻接与本人末注并回精确原证，非writer POST通过，窄锁释放；无实现核验或复现，非日级验收。

2026-03-12增量：2603.09771 exact-v1 §3–5/Tables1–3、A/B.1–6必要机制与直接反侧，2+1+2=5带概念名称的raw VP token cache具体接口gap深入；采用Eq3平均代理/保原patch顺序，不采attention为主体身份真值。COCO分割标注层校准、面积代理、任务/ref/token/runtime反退与F1汇总冲突、全费近文。root必要Source/date/具体owner/逐字PRE实际通过（独读范围见本日独核note，不反称其全附件），作者窄写LiteEmbed完整两段后/taxonomy前并顺读；root非writer实际顺读677–690完整邻接、新683/685和自身1275末注，回对必要原证/PRE，actualPOST通过，不授DAY。未核全图、代码或复现。<!-- source-family:SF-2026-ARXIV-2603-09771 -->

2026-03-12增量：2603.09826 exact-v1 §3–6/Tables1–6与D.1/D.2 Tables8–9必要文字，2+1+2=5具体部分valid/null绑定接口gap深入；采用GT局部对象中心距离制备监督与自主推理分责，不采位置oracle、无边实例表为关系图或JSON作为几何真值。模板/标注人口、阈值与模型size反退、2×4090 .23FPS范围和完整制备/训练/AR/解析/回归费用近文。root必要Source/date/逐字PRE通过，作者实际写入OpenVoxel两完整段后/统一mesh前并顺读局部及自身末注；root非writer实际顺读998–1025完整局部、新1006/1008及自身末注，回对必要原证，actualPOST通过。未核全图像、代码或复现，不授DAY。<!-- source-family:SF-2026-ARXIV-2603-09826 -->

2026-03-12增量：2603.08942 exact-v1 §4–6/式4–8/Tables1–4，仅采用identity初始化上三角bilinear监督评分，不采硬正交/无损canonical恢复。root必要Source/date/逐字PRE通过，原isometry两段后/少锚softOT前两段实际写入，root非writer已实际顺读77–99完整局部邻接、新两段与自身末注并回对原证，POST通过。维度平均proxy不约束单一方向、初始化/任务反侧、原表DTD冲突与标签/编码/二次打分/训练回归全费保留；未核全图、代码或复现。<!-- source-family:SF-2026-ARXIV-2603-08942 -->

- 2603.09556 exact-v1 §2–5/Tables1–5必要机制与直接反侧，2+1+2=5具体 primary/side fusion gap深入；P固定60额外tokens/E inference-only50Hz、合成target非raw truth、真实任务反退与完整费用保留。root非作者必要Source/date与逐字PRE实际通过；作者已写两段并顺读，root非写入者actualPOST实际通过，不授全图/代码/复现或production SLO。

- `SF-2026-ARXIV-2603-09232`：2026-03-12 补查，精确 v1 §2–6、Eq1–7/Table1。采用错误人口诊断、配对完整分母及反事实条件选择的窄差额，不采用自动 judge 标签作为内部根因、错误子集纠正率作为总体净收益或跨任务普遍改善。speech/任务退步、调参留出未披露和两路生成/状态/judge/校准费用保留；未核图像精数、代码或复现。非作者 supplement_20260312 必要 Source/日期/PRE 通过，实际顺读1217–1235完整邻接及本人末注并回对必要原证，写后复核通过；不授日报验收。

- `SF-2026-ARXIV-2603-06854` — Daily `2026-03-11`补遗漏；[exact-v1](https://arxiv.org/html/2603.06854v1) §3–7/Tables1–4。必要源由作者与 review_20260311 独核，root 实际读取§3–4并比较本章视觉差分及Ch22/24接口；只采用head定位、输入特定 residual 方向和最终读出干预的分责。Table1计数汇总与干预位置归因限制近正文，不采用精确gain/significance或音频真值。非写入者 supplement_20260311 实际顺读新增两段、完整局部邻接和末注，并回对必要原证，写后复核通过。未核代码/复现，不授日级完成。

- `SF-2026-ARXIV-2601-17676` — Daily `2026-01-28` 增量；[exact-v1](https://arxiv.org/html/2601.17676v1) §3–6，gaze 三粒度表示与 inferred-intent 权限，2+1+2=5；句级评价匹配、设备/人口/explicit 控制和自评边界近文。jan28_review 实际必要原源/owner/PRE通过，root先授窄锁；jan28_review 实际完整局部邻接、新两段与自身末注POST通过，不授DAY；未核artifact或复现实验。

- `SF-2026-ARXIV-2601-11096` — Daily `2026-01-20`增量；[CoDance exact-v1](https://arxiv.org/html/2601.11096v1) §3.2/3.3/4.1–4.3必要命题。2+1+2=5，位置/subject对应的具体差额深入；pose 输入平移/缩放及 pose encoder 输出特征平移/复制 unbind，text+mask语义/空间rebind，mask-only composite失效近文。保留混数据/solo声明、有限多主体baseline与identity反側、训练旁路不免encoders费用；不授真实instance身份或arbitrarycount保证。root实际必要原源与Ch23 actual709–728 PRE通过；POST发现feature unbind对象误写为reference latent，已按§3.2改为pose encoder输出的pose features；root实际正文724/726、完整邻接718–731与本注1211修正后POST通过，窄锁释放，不授日级。未核artifact或复现。

- `SF-2026-ARXIV-2601-11442` — Daily `2026-01-20`增量；[Map2Thought exact-v1](https://arxiv.org/html/2601.11442v1) §3/4、Tables1–3。2+1+2=5，metric map→确定几何 consumer 的 owner gap 深入；采用估计对象/尺度与算术分责，保留同25% map+CoT/无CoT/无map、GT上界、全量近持平/RelDir退步及额外感知/监督成本，不认证物理truth或端到端效率。root实际必要原证/actual owner PRE通过并授窄锁；作者已实际顺读新正文、完整上下邻接及本注，root 实际顺读 718–738 与本注 1207，POST 通过，窄锁释放。未核artifact/复现，非日级验收。

- `SF-2026-ARXIV-2601-06801` — Daily `2026-01-14` 增量；[DVRP exact-v1](https://arxiv.org/html/2601.06801v1) §3/4、Limitations及B/D必要实施/扰动反侧，2+1+2=5，三view同clean轨迹token-KL与负entropy辅助目标差额深入。random mask/noise语义是假设，medical强mask及full单项反退、额外计算与八次推理非训练多seed近文；top-p冲突和有限退火非零不修recipe，不采用safe regularizer或genuine grounding保证。peer必要原证/actual owner完整局部PRE通过，root授窄锁；作者已实际顺读正文、完整局部邻接及本注，root非写者已实际顺读正文、完整局部邻接及本注，actual POST通过，窄锁释放。未核实现/复现，非DAY。

- `SF-2026-ARXIV-2601-06338` — Daily `2026-01-14` 增量；[Circuit Mechanisms exact-v1](https://arxiv.org/html/2601.06338v1) §3、§4.1–4.4、§5及§6必要讨论，3+1+2=6，text contextualization改变relation载体/干预单位差额深入。head ablation、VO注入、shape2 relation vector操作仅授受控因果，T5 filler约40%反退与toy人口/白盒成本近文。peer必要原证/actual owner完整邻接PRE通过，root授窄锁；作者已顺读新正文/完整局部邻接及本注，root非写者已实际顺读新正文、完整局部邻接与本注，actual POST通过，窄锁释放。未核实现/复现，非DAY。

- `SF-2026-ARXIV-2601-07359` — Daily `2026-01-14` 增量；[DualPD exact-v1](https://arxiv.org/html/2601.07359v1) §3/4 Tables3/5。2+1+2=5，layer-shift/head-norm受限sensor差额深入；Δlogits→aggregate及projection/归一未决隔离，静态层/过抑制反侧和统计费用近文。peer必要原证/actual owner PRE通过、root授窄锁；作者实际完整局部邻接顺读；root 非写者 actual POST 已通过（新正文、完整局部邻接与自身末注），未复现，不授DAY。
- `SF-2026-ARXIV-2601-06843` — Daily `2026-01-14` 增量；[TRUE exact-v1](https://arxiv.org/html/2601.06843v1) §3.1/3.3–3.4/4。2+2+2=6，GDPE position-group与causal mask差额深入；OSPE自引用隔离，CIDEr反侧/训练协议/理想重叠非实测GPU/SLO近文。peer必要原证/actual owner PRE通过、root授窄锁；作者实际完整局部邻接顺读；root 非写者 actual POST 已通过（新正文、完整局部邻接与自身末注），未复现，不授DAY。

- `SF-2025-QWEN3-VL` — Daily `2025-09-23`；[官方发布说明](https://qwen.ai/blog?id=qwen3-vl) Model Updates：Interleaved-MRoPE 的三轴频段分配与 timestamp/frame 输入接口。只采用公开表示机制，不由联合模型更新宣称单因素性能、时钟同步或行动可靠性；未核实现或复现实验。跨层视觉读出已有正文承载，不重复展开。

- `SF-2026-ARXIV-2602-22629` — Daily `2026-02-28`；[CRAG exact-v1](https://arxiv.org/html/2602.22629v1) §3–5、Tables1–2，blocks23–49/50–59/65–79；2+1+2=5，具体shared decoded-VAE与双向fragment/shape接口差额深入；codec失真双向传播、matched-image但容量/训练混杂、geometry非语义/物理证据和成本近文。actual owner为MULTIMODAL-REPRESENTATION而非机器人assembly；feb28_vla_last7非原packet作者必要原证/owner复核后窄写，正文/完整邻接/末注已顺读；root非写入者actual POST通过，未核artifact或复现，不授日级完成。

- `SF-2026-ARXIV-2602-21627`：[v1 §III–IV / 长序列限制](https://arxiv.org/html/2602.21627v1)，字段 L/V 与 tag 错误作用域；既给 instance 不推断 tracking。`SF-2026-ARXIV-2602-21591`：[v1 UGAQ / auxiliary / runtime](https://arxiv.org/html/2602.21591v1)，不反缩放、派生 BLIP 条件与 decode 反退。`SF-2026-ARXIV-2602-22013`：[v1 §3 / 表1、3–4](https://arxiv.org/html/2602.22013v1)，训练单向辅助 token、推理删除，不采因果独立或零成本保证。`SF-2026-ARXIV-2602-21864`：[v1 §4 / 表8](https://arxiv.org/html/2602.21864v1)，consumer-relative query router 与 response-only 费用盲区，不采 log penalty 为指数或全迁移节省。`SF-2026-ARXIV-2602-22144`：[v1 Eq.6–8 / 表22及固定幅度反侧](https://arxiv.org/html/2602.22144v1)，两完整输入路径而非 late branch；不采语言 prior 唯一原因。五项均非原 packet 作者核必要原证/actual owner 后窄写，root已实际顺读正文、完整邻接与自身末注，POST通过，未运行代码或复现。

- `SF-2026-ARXIV-2602-20731` — Daily `2026-02-26`；[COMiT exact-v1](https://arxiv.org/html/2602.20731v1) §3.1–3.5/4.1–4.3。2+2+2=6，固定 message 重分配/crop 与梯度时钟差额深入；旧 message 加新 buffer、共享 encode/decode、VAE 输入、gold-mask 离线选择/大模型语义反退及循环总费/一次 codec 回退近文。root 必要原源/actual owner PRE 通过授两段窄锁；作者已实际顺读正文/完整邻接与自身末注，root 非作者 actual POST 通过。未核 artifact/复现，非日级验收。

- `SF-2026-ARXIV-2602-22394` — Daily `2026-02-28`；[exact-v1](https://arxiv.org/html/2602.22394v1) §4–6、Tables3/8/9。3+1+3=7，全局聚合与 dense 消费差额深入；lazy hypothesis、patch 分辨率混杂、window trade-off、全 K 反退及原路径近正文，不授所有 ViT/MLLM 因果或通用无损。root 必要原源/actual owner PRE 通过；实际正文、完整邻接与自身末注经 root 非作者 POST 通过，窄锁释放。未核实现/复现，不授日级完成。

- `SF-2026-ARXIV-2602-17869` — Daily `2026-02-24`；[CompressV exact-v1](https://arxiv.org/html/2602.17869v1) §3.2/§4.3/Appendix A.4。2+1+2=5，实际消费分布与 residual feature anchor 差额深入；loss spikes 支持接口分支，holes 只作者解释；消融省略stage2，压缩/训练成本及旧路径保留，不授全榜单因果或理解无损。root 必要原源/actual owner PRE 通过并授一段窄锁；作者实际正文与完整邻接写后顺读，root 实际核修正正文、完整邻接与自身末注，非作者 POST 通过，窄锁释放。未运行实现或复现，非日级 Gate。

- `SF-2026-ARXIV-2602-14178` — Daily `2026-02-18`；[UniWeTok exact-v1](https://arxiv.org/html/2602.14178v1) §3.1–3.3/Eqs2–3/9、必要§4/Table2与3。2+1+2=5，bounded encoder/去commitment与teacher消费的具体接口差额深入；不采entropy==commitment或2^128有效容量。PreDistill55.26/SigLuPost41.51及不同表人口、训练费用保留。root必要原源/actual owner PRE通过并授单文件窄锁；root实际正文、完整邻接与末注非作者POST通过，锁释放。未复现或核代码，非日级Gate。

- `SF-2026-ARXIV-2602-10934` — Daily `2026-02-13`；[CAT exact-v1 PDF](https://arxiv.org/pdf/2602.10934v1) §3–5、A/C必要段。2+1+2=5，输入sum/loss/部署同RVQ prefix身份差额深入；配对CE、frame/window buffer、不同bitrate与fixed-step不同compute反侧就近保留。root必要原源及current owner/相邻PRE通过授Ch23窄锁，实际两段及末注已写，root实际核正文、完整邻接与末注，非作者POST通过、窄锁释放，不授日级；未核代码/复现或全部图形。

- `SF-2026-ARXIV-2602-10425` — Daily `2026-02-13`；[MOH exact-v1](https://arxiv.org/html/2602.10425v1) §3.2–3.3/§4 Table2–3；2+1+2=5，实际视觉证据失效反侧深入；failure-selected/context-only诊断、mask不保证完全删除、分母/质量税均正文承载，不写DPO配方。root必要原源与actual owner PRE通过授窄锁，实际正文/邻接已由root非作者POST通过；未授日级，未复现。

- `SF-2026-ARXIV-2602-06218` — Daily `2026-02-10`；[Cross-Modal Redundancy exact-v1](https://arxiv.org/html/2602.06218v1) §3/Eq1、§4–6及AppC/E/H/I/J/K必要段。2+2+2=6，paired learned dictionary→energy mask具体gap深入；不采无instance matching、concept identifiability/equality、无条件ranking或无损。六dualencoder/1M matching LAION、exp8/l0=20，LAION/COCO召回退、center反侧、β退化与重建baseline分账；hardware/precision/完整训练搜索成本未披露，未核实现/复现。root必要源/owner及实际正文、邻接、末注POST已通过，窄锁释放；日级Gate未授。

- `SF-2026-ARXIV-2602-06205` — Daily `2026-02-10`；[Multi-Way Representation Alignment exact-v1](https://arxiv.org/html/2602.06205v1) §3–4、AppA1/C1–2/E。2+1+2=5，具体共同参考与共享非线性校正差额定点深入；GPA本身是成熟机制，GCPA的软trust与归一化不授硬isometry/cycle或总O(M) runtime。MASSIVE/TED/Flickr8k必要对应、anchor与局部noise反侧保留，模型间std非独立runCI；完整优化配置/hardware/precision/总成本未披露，未核实现/复现。root必要源/owner写前通过，root实际正文/邻接及末注非作者POST通过；日级Gate未授。

- `SF-2026-ARXIV-2602-06180` — Daily `2026-02-10`；[STACodec exact-v1](https://arxiv.org/html/2602.06180v1) §2.1–2.3 Eq6–14、§3配置及§4/Tables1–2。2+2+2=6，具体index身份与码向量分责缺口定点深入；LibriSpeech960h、50Hz、8×1024、单A6000/b32，原STA280K与SPD90K+160K非等总预算，baseline多官方checkpoint/HASRD报告值。只采用接口与质量反侧，不采无损解耦或参数/FLOPs对runtime保证，precision/独立重复统计未披露；未核artifact/复现。root必要原源与具体owner写前核通过并授窄锁，root实际顺读L172–185正文及末注，非作者POST通过；日级Gate未授。

- `SF-2026-ARXIV-2602-05464` — Daily `2026-02-07`；[OD-CRL exact-v1](https://arxiv.org/html/2602.05464v1) §3 SVD/null-space projection、结果与Appendix B/C。2+2+2=6，具体噪声正交补同时删除target overlap缺口深入，不采纯语义保证或未量化cross-subspace/非退化bound；clustering/linear probe与fashion MLP预算分账。root必要源/owner写前通过；实际正文/邻接及末注root实际非作者POST通过，未复现。

- `SF-2026-ARXIV-2602-04220` — Daily `2026-02-06`；[One-DVA exact-v1](https://arxiv.org/html/2602.04220v1) §3.1–3.3/3.5、§4.1/4.3/4.4。原2+2+2=6，具体distribution gap深入，只采用encoded→predicted latents exposure及冻结encoder/适配decoder、重建与生成质量分账，不称sample/GT配对实现已审或通用corrector。steps与PSNR/rFVD取舍、generation非全面胜出、额外48×80G/多阶段训练成本保留，未复现。root必要源/owner写前通过，正文及源注经root实际顺读正文、前后邻接与末注，非作者POST通过，日级Gate未通过。

- `SF-2025-ZAI-GLM-TTS` — Daily `2025-12-11`；[官方文章](https://www.zhipuai.cn/en/research/147)原HTML `time dateTime=2025-12-10T16:00:00.000Z`，支持文章事件，非仓库创建或commit即公开。必要机制来自文章 Phoneme-in 及 [固定早期README](https://github.com/zai-org/GLM-TTS/blob/40cf8f3f2c0e2bb035f479051d3d1a0aa4421730/README.md) Phoneme-in、RL Alignment、Evaluation；root通过GitHub contents API实际读blob `927d27400fc8025044e803068368d0be25e2e7f3`。只采用局部随机G2P混合训练/词典指定读音接口，CER/SIM without phoneme不授该控制有效；RL权重当时Coming Soon，不采用12/17后续论文、性能数字或生产流式保证。root实际核原文、音素接口前后及Ch24/25后局部整合；非写入者Popper实际重读官方Phoneme-in/评价与固定早期README完整core，对读新增单段、前后理解侧音素/阶段三及Ch24时长/Ch25环境转移职责，2026-10-02T20:15:20+08:00 POST通过；未运行代码，不授日级完成。

- Daily 2026-03-07：[DCR exact-v1](https://arxiv.org/html/2603.04803v1) §4.1–4.3、§5.1与§5.4/Table4。只补predicted-noise接入位置及两阶段冻结；映射/negative/norm假设、CC3M/SD2.1/LoRA16与基线预算差异、SDXL接口退步保留，不授通用梯度冲突消除。root实际必要原文/正文及邻接非作者POST通过；未复现实验。

- `SF-2026-ARXIV-2603-02872` — Daily 2026-03-05；[exact-v1](https://arxiv.org/html/2603.02872v1) §3.2–3.4、§4.1–4.4/Tables1–2、Appendix C–D。采用模态位置轴、可见前缀与 decode-segment 只读观察状态的接口分责；未核 pointer composition kernel/并发一致性，不采口径冲突的微秒端到端 TTFT、3B统一质量优胜或生产SLO。7分必要深入；root 已实际对读必要原文、正文与邻接，非作者 POST 通过，未复现。

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

- `SF-2026-ARXIV-2602-04094` — Daily `2026-02-06`；[VideoBrain exact-v1](https://arxiv.org/html/2602.04094v1) §3–4及必要反侧。原2+2+2=6，具体active-observation label/cost gap深入。direct/adaptive/active由base/teacher和工具答题结果定义，不等证据充分；both-wrong active与排除base-correct/teacher-wrong人口保留，索引/额外forward及固定采样反侧不授普遍预算优势。部署identity guard为工程推导，不宣称作者已实现；不采未计索引成本的数字。未运行代码或复现；jan01_v3实际必要原源/owner写前通过，root授本段窄锁；root实际新增正文/前后邻接及末注POST通过，日级Gate未验。

- `SF-2026-ARXIV-2602-04304` — Daily `2026-02-06`；[Visual Attention Querying exact-v1](https://arxiv.org/html/2602.04304v1) 必要§3–5。原2+2+2=6，具体±query双Prefill selector与同box logit contrast gap深入；首步attention正差/head/layer聚合仅区域代理，坐标对应与两branch显存/时间、短答条件保留，不授因果定位或全Decode恒定开销。未复现；jan02_v3实际必要原源及Ch23:428–461写前核通过并授≤1段，jan02_v3实际新增正文/前后邻接及末注POST通过，日级Gate未验。

- `SF-2026-ARXIV-2602-04804` — Daily `2026-02-06`；[OmniSIFT exact-v1](https://arxiv.org/html/2602.04804v1) 必要§3–4。原2+2+2=6，具体video selector→audio importance依赖gap深入；two-frame spatial/temporal选择、压缩visual KV与audio Q分权，107K paidSFT联合decoder/VGAS、额外cross-attention及部分质量反侧保留。反向OmniZip训练recipe不同，不授方向唯一因果、视觉总充分或通用SLO/无损；部署identity/fallback为工程推导，未复现。jan02_v3实际必要源/Ch23:369–418写前核通过并授窄段；jan02_v3实际新增正文/前后邻接及末注POST通过，日级Gate未验。

- `SF-2026-ARXIV-2602-03510` — Daily `2026-02-05`；[Semantic Routing exact-v1](https://arxiv.org/html/2602.03510v1) §3.3–3.4/Eq2–10、Table1与§5.2/5.3。原2+2+2=6，具体gap深入由owner校准为MULTIMODAL-REPRESENTATION；采用逐层LN/凸融合与DiTdepth-conditioned接口，不重复Ch24生成objective。Time-only/static-weight反侧、SNR自身最终latent参考及shift解释边界/额外延迟保留，不授唯一因果或8%无成本。未运行代码或复现；root已实际核必要源/owner及282行正文、Cross-attention/fusion邻接与末注，POST通过；日级Gate待验。

- `SF-2026-ARXIV-2601-03666` — Daily `2026-01-09`；[e5-omni exact-v1](https://arxiv.org/html/2601.03666v1) §2.2–2.4、§3.1/3.3–3.6、Appendix B。原2+2+2=6，pair温度、negative人口及joint Q/P共享W的Cov是不同训练接口；batch几何不授相关性真值、部署W/索引协议或每组件因果，γ/λ反侧与成本保留。未复现；jan01_v3实际必要原源与owner写前通过、root协调释放Ch23窄锁，jan01_v3已实际正文/前后邻接/源注POST通过，日级Gate未验。

- `SF-2026-ARXIV-2601-05572` — Daily `2026-01-13`；[Generalized multi-image editing exact-v1](https://arxiv.org/html/2601.05572v1) §3.2/§5–6。原评分保持，具体owner差额深入；仅采用separator/index补相对RoPE，j/N随N改变；2→5定性/消融反侧，不授通用性能/安全保证。未运行代码或复现实验；root实际必要原源/现owner写前核通过并授窄锁；root实际正文/前后邻接及末注非作者POST通过。

- `SF-2026-ARXIV-2601-09239` — Daily `2026-01-16`；[DSA-Tokenizer exact-v1](https://arxiv.org/html/2601.09239v1) §3–5/Table1–3/limits/C。2+2+2=6，dual discrete source/length与reconstruction/recombination分责gap深入；只采用冻结semantic与prefix条件重组接口，probe不授no-leak/独立性，speakerloss反侧与迭代decoder成本相邻。不复制Ch24 flow机制；root必要primary/现owner写前通过并授窄锁，作者已顺读两段及speech/tone邻接，root已实际核正文L238–252/末注1081，非作者POST通过，锁释放。未运行代码或复现实验，日级Gate未授。

- `SF-2026-ARXIV-2601-09322` — Daily `2026-01-16`；[exact-v1](https://arxiv.org/html/2601.09322v1) §3–5/Table1、A1/A9–10/A15。2+2+2=6，frozen 多层 CLS+AP→single-query fusion 的表示选择差额深入；不授 attention 因果、普遍最后层不足或 O(L²) 加速，spatial-loss/AAT/linear 反侧和特征缓存/训练搜索成本相邻。root必要原源/owner写前通过；正文两段L71/73、L61–79邻接与末注已由root非作者POST通过，锁释放；日级未授，未运行代码或复现。

- `SF-2026-ARXIV-2601-09859` — Daily `2026-01-17`；[TuneCLIP exact-v1](https://arxiv.org/html/2601.09859v1) §4.1–4.2/Algorithm1/Eq8–9、§5 与 Appendix E/H/I。2+2+3=7；采用冻结权重统计重估与 margin 足够即停止 pair 排斥的 continued adaptation 分支，不授原预训练状态恢复、真负例识别或通用无损。监督反侧、moments 归因与两阶段成本相邻。未核实现或复现实验；root实际必要原源/owner写前通过并授窄锁，root已实际核两段正文、前后邻接及末注，非作者POST通过；日级Gate未授。

- `SF-2026-ARXIV-2601-10096` — Daily `2026-01-17`；[M2M exact-v1](https://arxiv.org/html/2601.10096v1) §3–4、§5必要配置及§6–7。2+2+2=6，English 共享 text-space 锚转接已有多语能力的接口 gap 深入；不授未预训练语言学习/通用无损，normalized retrieval 与 generation 目标分开，synthetic audio/FLUX token-conditioning 反侧与版本成本相邻。未核实现或复现实验；root必要原源/owner写前通过并授窄锁，root已实际核两段正文、前后邻接及末注，非作者POST通过；日级Gate未授。

- `SF-2026-ARXIV-2602-06393` — Daily `2026-02-10`；[MuCo exact-v1 PDF](https://arxiv.org/pdf/2602.06393v1) §4.1–4.2、§5.1–5.3/Table5/6/7。2+2+2=6，specific gap深入：共享图像 causal 多轮监督与同图 counterpart mask，相关pair非独立image、后续gradient非forward future leakage；单pair/无history反侧和合成/训练完整成本保留。Table2与正文M-BEIR数字不一致，不采用headline；未视觉截图验证、实现核验或复现。root必要原源/owner写前通过，root实际正文L509–525与末注1093非作者POST通过，锁释放；日级Gate未授。

- `SF-2026-ARXIV-2601-10272` — Daily `2026-01-17`；[MoST exact-v1](https://arxiv.org/html/2601.10272v1) §3/Algorithm1、§4.2/§6、Table2/5与B1/B2/D1。2+2+2=6，typed eligibility 与 parallel shared 分责 gap 深入；未补 mask 归一，matched routed 数不等总参数/active compute，均值冲突和退步相邻，不授中性分组、transfer 因果或无遗忘。未核实现或复现；root必要原源/owner写前核通过，root已实际顺读两段正文、前后邻接及末注，非作者POST通过，锁释放；日级Gate未授。

- `SF-2026-ARXIV-2602-06451` — Daily `2026-02-10`；[BrokenBind exact-v1](https://arxiv.org/html/2602.06451v1) §3 Eq5–12/Algorithm1、§4.3/Table9/§5。2+1+2=5，only-pivot 跨集合双 pseudo-path 约束的 confirmed gap 定点深入；每 batch 伪逆 stop-gradient 不授 missing-raw truth、bias-free、数值稳定或可执行矩阵配方。LP+LoRA/分阶段训练、mAP 口径与 rare modality 反侧、真实配对/纯 map 退路近正文；hardware/precision/batch 数值条件与全成本未披露。未核实现或复现；root必要原源/owner与实际正文L71/73、前后L59–83及末注1135非作者POST已通过，锁释放；日级Gate未授。

- `SF-2026-ARXIV-2601-10378` — Daily `2026-01-17`；[VIST2 exact-v1](https://arxiv.org/html/2601.10378v1) §2–3、§4.1/4.3–4.4、Tables3/6/8及B/D。2+2+2=6，completed chunk→visual history 的 representation consumer gap 深入；训练可见性不授已核 KV 回收/无损 readback，OCR warmup/OLM 分责、质量反退和全成本近正文，不采 3× 吞吐。未核实现或复现；root必要原源/owner写前通过并授窄锁，root实际两段/前后邻接及末注非作者POST通过，窄锁释放；日级Gate未授。

- `SF-2026-ARXIV-2601-10710` — Daily `2026-01-17`；[CLI exact-v1](https://arxiv.org/html/2601.10710v1) §3 Eq4–9、§4.3/Table4及密度直接反侧。2+1+2=5，producer 层×LLM consumer 层/visual positions 的具体接口差额最低必要深入采用；不授任意文本注入、层功能因果或普遍末层瓶颈。参数容量、半量训练条件、驻留/门控成本与 density 非单调近正文，原末层 projector/summary readout 共存。未核实现或复现；root必要原源/owner写前通过，已实际顺读正文L77–93与末注L1147，非作者POST通过，Ch23锁释放；日级Gate未授。

- `SF-2026-ARXIV-2601-12042` — Daily `2026-01-22`；[CAA exact-v1](https://arxiv.org/html/2601.12042v1) §3/4.2/5.1/5.3及F.3。2+2+2=6，受影响安全差额深入：压缩/未压缩paired扰动与同扰动图像clean-ranking oracle分离selector不稳和语义损伤；oracle为特权离线诊断，不授部署guard、普遍因果或通用安全保证。保留白盒权限、层/保留率、正常质量与选择成本边界；未核实现或复现。root必要原源/owner写前通过；正文L409/411、邻接L403–417与本末注已由root实际顺读，非作者POST通过，Ch23窄锁释放；Daily 2026-01-22 日级语义Gate经root独立复核通过并授权完成；来源终态缺段与其他材料中心争议仍隔离，不授无遗漏或普遍安全保证。

- `SF-2026-ARXIV-2602-09528` — Daily `2026-02-12`；[exact-v1](https://arxiv.org/html/2602.09528v1) §2.3–2.4/Table1–2/4。具体 owner 差额受影响深入：input-conditioned activation drift/noise；非 truth manifold、零成本或全能力保证。root 必要原源/具体 owner 写前通过并授窄锁；root 已实际顺读两段、完整邻接与本末注，非作者 POST 通过，窄锁释放。未核代码/复现，非日级 Gate。

- `SF-2026-ARXIV-2601-16093` — Daily `2026-01-24`；[SAMTok v1](https://arxiv.org/html/2601.16093v1) §2.1–2.3/3.2/B/D，7分必要深入。采用 image-conditioned 两 residual code 的 mask 接口身份，非 image token+mask token；codeword reward 与几何质量分责、容量非单调与 codec 成本近正文。root 必要原源/owner 写前通过，正文/前后邻接与末注root POST通过、锁释放；未核代码或复现。
- `SF-2026-ARXIV-2601-16192` — Daily `2026-01-24`；[360Anything v1](https://arxiv.org/html/2601.16192v1) §3.3/4.1–4.4/0C，7分必要深入。采用 wrap→encode→crop 的训练 target 边界职责，非通用无缝/几何或全 pipeline 零成本。root 必要原源/owner 写前通过，正文/前后邻接与末注root POST通过、锁释放；未核代码或复现。
- `SF-2026-ARXIV-2601-15655` — Daily `2026-01-24`；[Event-VStream v1](https://arxiv.org/html/2601.15655v1) §4–6，7分必要深入。采用连续变化/运动/预测残差提出 event-admission，与 fixed clip/readback 分责；predictor训练、误漏和无 unbounded/tail-SLO保证近正文。root 必要原源/owner 写前通过，正文/前后邻接与末注root POST通过、锁释放；未核代码或复现。

- `SF-2026-ARXIV-2602-09825` — Daily `2026-02-12`；[SAKED exact-v1](https://arxiv.org/html/2602.09825v1) §3/Alg1、§4 Tables1–5、B.2/C。2+1+2=5，动态stability-conditioned layer contrast具体gap深入；visual/head/layer/adjacent-token一致性仅sensor，原top20是candidate support，非calibrated truth。组件/任务反退与跨模型调参、完整runtime/HBM成本未披露近正文；beam5不称greedy，未核实现或复现。独立reviewer必要source、root具体owner写前通过，实际正文/邻接与末注经root实际非作者POST通过、窄锁释放；不授日级Gate。

- `SF-2026-ARXIV-2601-20796` — Daily `2026-01-30`；[exact-v1](https://arxiv.org/html/2601.20796v1) §3/4及A.3.7/Table8，2+2+3=7。仅采用先M1训练再joint接M2与从零joint在固定序列的主次反侧、容量与ICL/IWL分账；非所有late fusion优越、label位置独立因果或生产模型通用规律。训练预算差、两层toy与实际大模型混杂近正文。root必要原源/实际owner PRE及实际正文/邻接/末注POST通过，非日级Gate。未核代码或复现实验。

- `SF-2026-ARXIV-2602-10230` — Daily `2026-02-13`；[exact-v1](https://arxiv.org/html/2602.10230v1)，必要方法/关键评价/直接反侧见本日 V3_EVIDENCE_SIX；2+1+2=5，具体owner差额深入。只采用decoder audio frame→数值时间head与真实clock分责，不采用矛盾loss/通用60倍。root实际必要原源与current owner/邻接PRE通过；root实际正文、前后邻接与末注非作者POST通过，窄锁释放，日级未授；未运行代码或复现实验。

- `SF-2026-ARXIV-2602-11072` — Daily `2026-02-13`；[exact-v1](https://arxiv.org/html/2602.11072v1)；Hibiki-Zero exact-v1 §3.2–3.3/4.7与Tables5–6。2+2+2=6，sentence-delay exploration support与训练reference/arrivedprefix差额深入；不授无timestamp/无GT、zero latency、所有质量/音色保持或生产安全。root必要原源/current owner及邻接PRE通过并授窄锁；root已实际顺读新增两段、前后交接与末注，非作者POST通过，未核代码/复现，日级未授。

- `SF-2026-ARXIV-2602-11073` — Daily `2026-02-13`；[exact-v1](https://arxiv.org/html/2602.11073v1)；必要证据与直接反侧见本日 V3_EVIDENCE_CSIX_FOUR。2+1+2=5；query条件跨region feature接口差额深入，不授attention真值、性能比例或所有任务更快。root已实际核必要原源/current owner及邻接PRE并授窄锁；root已实际顺读新增两段、邻接与末注，非作者POST通过，窄锁释放，未核代码/复现，日级未授。

- `SF-2026-ARXIV-2602-12370` — Daily `2026-02-17`；[LLaMo exact-v1](https://arxiv.org/html/2602.12370v1) §3.2–3.4/Eq3、§4.4/Table5、§5/7与§8/Table6。2+2+2=6，codec producer→continuous AR消费具体接口差额深入；仅采reconstruction/rollout双验收与codec noise scale和history扰动分账，不授σ唯一因果、所有模态必需、mixed-prefix冻结不变或batch1实时保证。局部替换、训练stage/数据筛选混杂、task scaling反侧、采样/codec成本保留在本日报。root必要原源/现owner PRE通过；实际1段/完整邻接作者已顺读，root非作者实际POST通过，窄锁释放；未核代码/复现，非日级Gate。

- `SF-2026-ARXIV-2602-15491` — Daily `2026-02-19`；[exact-v1](https://arxiv.org/html/2602.15491v1) §2–5/Eq9与 gain/codebook 消融；2+1+2=5，增益敏感性与 pre-encoder shape/gain 放置条件深入。需重训/400bps/双向 encoder、SI-SDR 与外部训练语料反侧保留，不授在线实现或码本倍数为端到端加速。root 必要原源及 actual owner PRE 通过并授窄锁；作者已顺读正文/完整邻接，root 实际正文/完整邻接/末注非作者 POST 通过，窄锁释放，未核实现或复现，非日级 Gate。

- `SF-2026-ARXIV-2602-15537` — Daily `2026-02-19`；[exact-v1](https://arxiv.org/html/2602.15537v1) §3–5/Table1–2；2+1+2=5，冻结表示的边界层/内容层分工与时间 unit 取舍深入。聚类训练及开发选择、边界 F1 与 lexical 反侧、SSL/预算混杂保留，不授零训练、wire codec 成本或语言无关语义 unit。root 必要原源及 actual owner PRE 通过并授窄锁；作者已顺读正文/完整邻接，root 实际正文/完整邻接/末注非作者 POST 通过，窄锁释放，未核实现或复现，非日级 Gate。

- `SF-2026-ARXIV-2602-15749` — Daily `2026-02-19`；[exact-v1](https://arxiv.org/html/2602.15749v1) §2.1/§4.1–4.4/Table1；2+1+2=5，encoder计算前移/decoderbackend fallback差额深入。质量/rate、instrumental训练、额外RVQ与profiling费用及估计context限制保留，不授全系统加速/SLO。root必要源/actual owner PRE通过授一段窄锁，作者正文/完整邻接已顺读、root非作者实际正文/完整邻接/末注POST通过，窄锁释放；未核实现/复现，非日级Gate。

- `SF-2026-ARXIV-2602-16008` — Daily `2026-02-20`；[MAEB exact-v1](https://arxiv.org/html/2602.16008v1) §2.2/3/4.1–4.2/5。2+2+2=6，目标信息×readout排序反侧深入；只采用有限encoder选择条件，不授n4 AudioLM普遍预测、信息不可兼得或全部原生pipeline相同。root必要原源/actual owner PRE通过授一段窄锁；作者实际正文及完整邻接已顺读，root实际正文/完整邻接/末注非作者POST通过，窄锁释放；未运行实现或复现，非日级Gate。

- `SF-2026-ARXIV-2602-14134` — Daily `2026-02-18`；[DenseMLLM exact-v1](https://arxiv.org/html/2602.14134v1) §3/Eq2–5、必要评价/配置与分辨率及专用 head 反侧。2+1+2=5，multi-label/valid-annotation/negative population 的具体接口差额深入；共享词表不是空间真值，top-k不认证全部无标注真负，readout与训练/词表费用近正文。root 必要源/actual owner PRE及实际正文/完整邻接与末注POST通过；未核实现或复现，非日级。

- `SF-2026-ARXIV-2602-12641` — Daily `2026-02-17`；[exact-v1](https://arxiv.org/html/2602.12641v1) 必要方法、关键对照及直接限制；2+1+2=5，实际 owner 差额定点深入。root 必要原源/owner PRE 通过并授一段窄锁；仅采用正文的条件分支，不授泛化性能、正确性或安全保证。作者正文及完整邻接已顺读，root 非作者实际正文/完整邻接/末注 POST 通过，窄锁释放；未核 artifact 或复现，非日级验收。

- `SF-2026-ARXIV-2602-16305` — Daily `2026-02-20`；[BAT/CGP exact-v1](https://arxiv.org/html/2602.16305v1) §4/Table1/5.2–5.3/Table4/6。2+1+2=5，layer visibility/probe capacity/pretrain decoder评价对象差额深入；不复制目标信息排序原则，不授later-is-better或普遍SOTA，probe/标注/decoder预算与简单readout共存。root必要原源/actual owner PRE通过；作者及root实际正文/完整邻接/自身末注顺读，非作者POST通过，窄锁释放；未核代码或复现，非日级验收。

- `SF-2026-ARXIV-2602-16334` — Daily `2026-02-20`；[exact-v1](https://arxiv.org/html/2602.16334v1) §3.2–6/7、Table3与B.3。2+1+2=5，query-filter×题型×thinking反侧差额深入；AGM为temporal mask非重叠声源分离，模拟/keyword与GPT-5-mini judge/预算限制保留，不采普遍reasoning协同或速度。root必要source/actual owner PRE通过，作者与root实际正文/完整邻接/自身末注顺读，非作者POST通过，窄锁释放；未复现，非日级验收。

- `SF-2026-ARXIV-2602-16455` — Daily `2026-02-20`；[ChartVSR exact-v1](https://arxiv.org/html/2602.16455v1) §2.3/3.3/4.1/4.4与Tables4–6。2+1+2=5，where→原图marker回读→what表示差额深入；三call预算、严格读数近零和多轮不单调、自确认非真值近正文。root必要原源/actual owner PRE通过并授一段窄锁；作者正文/完整邻接已顺读，root非作者实际正文/完整邻接/自身末注POST通过，窄锁释放；未核代码/复现，非日级验收。

- `SF-2026-ARXIV-2602-17149` — Daily `2026-02-21`；[TimeOmni-VL exact-v1](https://arxiv.org/html/2602.17149v1) §3.1/4.1–4.2/5；2+1+2=5，finite canvas 容量及 normalization metadata 差额深入。避免下采样不授浮点无损，零尺度/饱和与视觉 token 成本近正文；valid-output 评价及联合 CoT 不作单因果。root必要原源/actual owner PRE通过并授窄锁；作者正文/完整邻接及自身末注已顺读，非作者POST通过，窄锁释放；未核代码/复现，非日级验收。

- `SF-2026-ARXIV-2602-16689` — Daily `2026-02-20`；[exact-v1](https://arxiv.org/html/2602.16689v1) §3.1–3.2/4.1–4.4与B3/C。2+1+2=5，object bias×diversity/sample/reader预算条件差额深入；dense仅easier/充分样本与reader旧支路，downstream matched非fullpipeline、oracle非组合证书、synthetic非realworldstate近正文。root必要source/actual owner PRE通过；作者实际顺读及root正文/完整邻接/自身末注POST通过，未核实现/复现，非日级验收。

- `SF-2026-ARXIV-2602-18252` — Daily `2026-02-24`；[exact-v1](https://arxiv.org/html/2602.18252v1) §3/Eq1–2、§4–5、Appendix A。2+2+2=6，encoder-only old-feature anchor、冻结码本/consumer的鲁棒替换具体差额安全深入；clean/robust取舍、不同radius/objective非因果与index变化非安全充分/必要代理近正文。root必要原源/actual owner PRE通过并授窄锁；作者实际正文/邻接与末注顺读，root非作者实际正文/完整邻接与自身末注POST通过，锁释放。未核实现或复现，非日级验收。

- `SF-2026-ARXIV-2602-16138` — Daily `2026-02-20`；[IRIS exact-v1](https://arxiv.org/html/2602.16138v1) §2.1–2.7/3.1–3.3/3.5与Limitations。2+1+2=5，question-onset×fixation overlay/原图接口差额深入；同数据窗口、GT/judge权限、crop反侧和硬件/同步成本近正文。root必要原源/actual owner PRE通过；作者正文/完整邻接已顺读，root非作者实际正文/完整邻接/自身末注POST通过，锁释放；未核代码/复现，非日级验收。

- `SF-2026-ARXIV-2602-17133` — Daily `2026-02-21`；[exact-v1](https://arxiv.org/html/2602.17133v1) §3.1–3.2.4/Eq3–12、§4/Table1–2/A2/B1/C。2+1+2=5，无码本扰动训练→离线码本部署差额深入；固定估计密度条件不授真实分布/量化误差匹配，重建/生成、质量反侧与队列/聚类费用近正文。root 必要原源/actual owner PRE通过并授一段/末注窄锁；作者实际正文及完整邻接已读，root非作者实际正文/完整邻接及自身末注POST通过，窄锁释放。未核实现/复现，非日级验收。

- `SF-2026-ARXIV-2602-18432` — Daily `2026-02-24`；[exact-v1](https://arxiv.org/html/2602.18432v1) §3.2 causal VAE/Eq2–3、§3.3历史噪声条件与§4控制/直接反侧。2+1+2=5，codec/generator两侧prefix差额深入；stride缓冲/输入实际到达、T400平均FPS≠在线deadline和guidance质量取舍近文，不授真实物理/生产实时保证。root必要原源/actual owner PRE通过并授一段/自身末注窄锁；作者实际正文/完整邻接及自身末注已顺读、限定diff-check通过，窄锁释放，root非作者实际正文/完整邻接及自身末注POST通过。未核实现/复现，非日级验收。

- `SF-2026-ARXIV-2602-16545` — Daily `2026-02-20`；[exact-v1](https://arxiv.org/html/2602.16545v1) §3–4/§6.1–6.6。2+1+2=5，base/modifier readout 转移差额深入；旧头冻结仍竞争是工程推断，正确数 ratio 非逐例稳定，单次 split 与新视觉反侧/费用/回退近文。root 必要源/actual owner PRE 通过；作者正文/完整邻接已读，root 非作者实际正文/完整邻接/自身末注 POST 通过，窄锁释放。未核实现/复现。

- `SF-2026-ARXIV-2602-18745` — Daily `2026-02-25`；[exact-v1](https://arxiv.org/html/2602.18745v1) §3.2/4.5/B/I。2+1+2=5，可render scene IR 的结构/annotation 与 syntax 差额深入；同模型角色、相关非因果、平面图像/多阶段成本与原图回退近文，不授完全可验证或通用视觉能力。root实际必要源/owner PRE通过授两段窄锁；作者实际正文、完整邻接与自身末注顺读及限定diff-check通过，root非作者 actual POST通过，窄锁释放。未核实现/复现，非日级验收。

- `SF-2026-ARXIV-2602-17555` — Daily `2026-02-21`；[exact-v1](https://arxiv.org/html/2602.17555v1) §3.3–3.4/Eq10–11、§4.3/Table3/Implementation Details。2+1+2=5，具体owner差额深入；caption→temporalgraph与accuracy门控video/graph attention训练代理；模型身份冲突/非causaltruth/同源与额外费用近正文，不授普遍保证。root必要原源/actual owner PRE通过并授窄锁；作者实际正文/完整邻接/自身末注已顺读，root非作者已实际独读正文/完整邻接/自身末注，POST通过，窄锁释放。未核实现或复现，非日级Gate。

- `SF-2026-ARXIV-2602-17584` — Daily `2026-02-21`；[exact-v1](https://arxiv.org/html/2602.17584v1) §5.3–5.5/6/7.1/7.5/8。2+1+2=5，unimodal map向othermodality迁移的crosskernel条件具体深入；Sym spanning、rectangular只projection、mean/版本依赖、灵活map反侧、分类域/费用与回退近正文，不授普遍无损升级。root必要原源/actual owner PRE通过并授窄锁；作者正文/完整邻接/自身末注已实际顺读，root非作者实际正文/完整邻接/自身末注POST通过，窄锁释放。未核实现/复现，非日级Gate。

- `SF-2026-ARXIV-2602-21341` — Daily `2026-02-27`；[Scaling View Synthesis Transformers exact-v1](https://arxiv.org/html/2602.21341v1) §2–4/6/10.2。2+2+2=6，target-agnostic producer复用与target-conditioned质量/compute口径差额深入；A6000B64非单请求、scene/camera身份与驻留费用/原联合回退近文。root必要源/actual owner PRE通过授单段窄锁；root非作者已实际独读正文/完整邻接/自身末注，POST通过，窄锁释放，未核实现或复现，非日级Gate。

- `SF-2026-ARXIV-2602-21428` — Daily `2026-02-27`；[PSF-Med exact-v1](https://arxiv.org/html/2602.21428v1) §2–4/A/B/Q.5–6。2+2+3=7，semantic等值人口与stability/modalitydependence/accuracy三诊断分开；delta patch/随机控制有限权限、稳却错与SAE/评价费用近文，不授临床部署、swap真值或通用因果。root必要源/actual owner PRE通过授单段窄锁；root非作者已实际独读正文/完整邻接/自身末注，POST通过，窄锁释放，未核实现或复现，非日级Gate。

- `SF-2026-ARXIV-2602-21646` — Daily `2026-02-27`；[Synthetic speech-guided translation exact-v1](https://arxiv.org/html/2602.21646v1) §3–4/Table5–6，blocks19–62/89–97。2+1+2=5，same-text派生模态与新环境observation差额深入；TTS/modelprior非独立事实/原说话者观测，synthetic/authentic有限同protocol平均不认证全部声学信息，费用/语言反退与text-only/rawspeech回退近文。root必要源/actual owner PRE通过并授单段窄锁；作者正文/完整邻接/自身末注已实际顺读，root非作者已实际独读正文/完整邻接/自身末注，POST通过，窄锁释放；未核实现或复现，非日级Gate。

- `SF-2026-ARXIV-2602-21497` — Daily `2026-02-27`；[Evidence-Calibrated Reasoning Decoding exact-v1](https://arxiv.org/html/2602.21497v1) §3–4/§5，blocks36/46/49–52/65/71/73–81。2+2+2=6，candidate-limited same-image decider/pool与真实acquisition分工差额深入；bbox非重编码crop、候选外truth无法recover/无原问题、rawmargin非calibratedconfidence，有限角色控制/新增费用与原decode/完整图像Gate回退近文，不授uniquegain因果或事实认证。root必要源/actual owner PRE通过并授单段窄锁；作者正文/完整邻接/自身末注已实际顺读，root非作者已实际独读正文/完整邻接/自身末注，POST通过，窄锁释放；未核实现或复现，非日级Gate。

- `SF-2026-ARXIV-2602-22419` — Daily `2026-02-28`；[DeBias-CLIP exact-v1](https://arxiv.org/html/2602.22419v1) §3–5、Table5；2+1+3=6，首summary/位置捷径差额深入。保留完整long-caption loss，only新增short分支去summary、句独立近似、PAD局部反退及训练费用近正文；不授training-free或细节理解证书。root必要原源/actual owner PRE通过并授一段及自身末注窄锁；root已实际核新正文、完整邻接和自身末注，非作者POST通过，窄锁释放；未核artifact/复现，不授日级完成。
- `SF-2026-ARXIV-2602-21716` — Daily `2026-02-27`；[TranX-Adapter exact-v1](https://arxiv.org/html/2602.21716v1) §3–5/Table4–5。2+1+2=5，双cue不同融合方向/负JS任务目标差额深入；scores/flow非truth、fulltune与退化反侧/总费用回退近正文。root必要原源/actual owner PRE通过；作者实际正文/完整邻接/自身末注顺读，root非作者实际正文/完整邻接/自身末注POST通过，窄锁释放。未核实现/复现，非日级Gate。

- `SF-2026-ARXIV-2602-22469` — Daily `2026-02-28`；[SCR exact-v1](https://arxiv.org/html/2602.22469v1) §3/Eq1与§4–6/关键反侧。2+1+3=6，early-residual 空间读取差额深入；two-pass inference 非训练credit、非守恒加法、entropy非grounding、新错/边界失败与延迟/one-pass训练费用近正文。root必要原源及actual owner PRE通过并授单段及自身末注窄锁；作者写后顺读实际正文及邻接，root非作者实际POST并对Uniform-Smooth/Gaussian-noise分离句窄回核通过，窄锁释放。未核artifact/复现，非日级Gate。

- `SF-2026-ARXIV-2602-22426` — Daily `2026-02-28`；[SimpleOCR exact-v1](https://arxiv.org/html/2602.22426v1) §4–5/Limitations。2+1+3=6，elicitation 与压缩差额深入；standalone与hybrid C_orig更新协议分开，OCR/resolution、混合反退及额外RL费用近文。root必要原源/actual owner PRE通过并授单段及自身末注窄锁；作者实际正文及完整邻接顺读，root非作者实际正文/完整邻接/自身末注POST通过，窄锁释放。未核实现/复现，非日级Gate。

- `SF-2026-ARXIV-2602-21900` — Daily `2026-02-27`；[EmoOmni exact-v1](https://arxiv.org/html/2602.21900v1) §4–5/Table2–3，2+2+2=6；显式strategy→acousticinstruction交接差额深入；派生intent非心理truth/因果识别、去strategy断链非matchedhidden因果、WER/自然度反侧、全费与native/纯text回退近文。root必要原源/actualowner PRE与实际正文268、完整邻接258–284及自身末注1345非作者POST通过，窄lease释放；未核artifact/复现，非日级验收。

- `SF-2026-ARXIV-2602-22142` — Daily `2026-02-27`；[exact-v1](https://arxiv.org/html/2602.22142v1) §3–4/Table2–4，2+2+2=6；具体owner差额深入：ordertraining与current-first entropy recall；timestamp-only反退、coarse漏证、有限人口/阈值与总费用/原历史回退近正文。root必要原源/actual owner PRE通过并授窄lease；作者及root非作者已实际顺读正文/完整邻接/自身末注，POST通过，窄lease释放。未核实现/复现，非日级Gate。

- `SF-2026-ARXIV-2602-20980` — Daily `2026-02-26`；[exact-v1](https://arxiv.org/html/2602.20980v1) §3.3–3.4/4.3，2+1+2=5，latent跨损坏路径消费接口真实差额深入。两路CE/answer KL与answer→latent平方Frobenius约束分责，全attention反退/blur/8tokens与特权训练双路费用保留；不授内部faithfulness/普遍数据效率。非原packet作者必要原证/actual owner PRE、root授窄锁；作者实际正文/完整邻接/自身末注顺读，root非写入者POST通过。未核artifact/复现，非日级验收。

- `SF-2026-ARXIV-2602-22727` — Daily `2026-02-28`；[HulluEdit exact-v1](https://arxiv.org/html/2602.22727v1)。2+1+3=6，必要 blocks0–114、172–175、185–190；视觉补空间/anti-prior 与残余分别软缩放；所选投影非事实保真，SVD 基维度、门控反退、计数/预处理费用隔离。非原 packet 作者 feb28_ch23_finish 独立必要原证/实际 owner PRE完成；窄段已融入正文，作者实际正文/完整邻接及自身末注顺读；root 非写入者已实际独读正文、完整邻接与自身末注，POST通过，窄锁释放。未核实现或复现实验，非日级 Gate。

- `SF-2026-ARXIV-2602-22779` — Daily `2026-02-28`；[TrajTok exact-v1](https://arxiv.org/html/2602.22779v1)。2+2+2=6，必要 blocks20–51、68–100、104–119；soft grouping/hard-mask 读取与 slot 粒度；stop-gradient、伪标签、片段增长/输入覆盖混杂和 pooling 回退近文。非原 packet 作者 feb28_ch23_finish 独立必要原证/实际 owner PRE完成；窄段已融入正文，作者实际正文/完整邻接及自身末注顺读；root 非写入者已实际独读正文、完整邻接与自身末注，POST通过，窄锁释放。未核实现或复现实验，非日级 Gate。

- `SF-2026-ARXIV-2602-22918` — Daily `2026-02-28`；[Where Vision Becomes Text exact-v1](https://arxiv.org/html/2602.22918v1)。2+1+3=6，必要 blocks25–128；成对文字移除方向、操作特异性和分层干预；伪影对照、阅读/空间反退、层迁移非同一性及原 forward 回退近文。非原 packet 作者 feb28_ch23_finish 独立必要原证/实际 owner PRE完成；窄段已融入正文，作者实际正文/完整邻接及自身末注顺读；root 非写入者已实际独读正文、完整邻接与自身末注，POST通过，窄锁释放。未核实现或复现实验，非日级 Gate。

- `SF-2026-ARXIV-2602-23068` — Daily `2026-02-28`；[TADA exact-v1](https://arxiv.org/html/2602.23068v1)。2+2+2=6，必要 blocks25–99；文本位置 acoustic latent/duration 接口；邻域边界、语言/音色质量取舍、ASR/flow/候选费用与固定-rate 回退近文。非原 packet 作者 feb28_ch23_finish 独立必要原证/实际 owner PRE完成；窄段已融入正文，作者实际正文/完整邻接及自身末注顺读；root 非写入者已实际独读正文、完整邻接与自身末注，POST通过，窄锁释放。未核实现或复现实验，非日级 Gate。

- `SF-2026-ARXIV-2602-23136` — Daily `2026-02-28`；[Modality Collapse exact-v1](https://arxiv.org/html/2602.23136v1)。2+2+2=6，必要 blocks20–83、94–120、162–171；covariance 方向删除与非转录 decoder 适配分开；随机删除/人口混杂近文，条件平均 GMI 可构造反例，信息上限与梯度保证隔离。非原 packet 作者 feb28_ch23_finish 独立必要原证/实际 owner PRE完成；窄段已融入正文，作者实际正文/完整邻接及自身末注顺读；root 非写入者已实际独读正文、完整邻接与自身末注，POST通过，窄锁释放。未核实现或复现实验，非日级 Gate。

- `SF-2026-ARXIV-2602-23229` — Daily `2026-02-28`；[Open/Closed ICL exact-v1](https://arxiv.org/html/2602.23229v1)。2+1+3=6，必要 blocks31–45、53–85、151–154；封闭支持人口、开放 leave-one-out 同步派生标签；judge/zero-shot 反侧、重复编码和轮次费用近文。非原 packet 作者 feb28_ch23_finish 独立必要原证/实际 owner PRE完成；窄段已融入正文，作者实际正文/完整邻接及自身末注顺读；root 非写入者已实际独读正文、完整邻接与自身末注，POST通过，窄锁释放。未核实现或复现实验，非日级 Gate。

- `SF-2026-ARXIV-2602-23235` — Daily `2026-02-28`；[GUIPruner exact-v1](https://arxiv.org/html/2602.23235v1)。2+1+3=6，必要 blocks19–95、117–127、165–166；历史 resize 与当前前景/背景/网格预算分开；历史增长/整数边界、早剪质量反退及局部计时非 action SLO 近文。非原 packet 作者 feb28_ch23_finish 独立必要原证/实际 owner PRE完成；窄段已融入正文，作者实际正文/完整邻接及自身末注顺读；root 非写入者已实际独读正文、完整邻接与自身末注，POST通过，窄锁释放。未核实现或复现实验，非日级 Gate。

- `SF-2026-ARXIV-2602-23266` — Daily `2026-02-28`；[DDTSR exact-v1](https://arxiv.org/html/2602.23266v1)。2+2+2=6，必要 blocks32–108、137–144；partial/final ASR 两轨观测身份及 filler/content 首音分账；衔接机会/质量反侧、语义风险与完整等待回退近文。非原 packet 作者 feb28_ch23_finish 独立必要原证/实际 owner PRE完成；窄段已融入正文，作者实际正文/完整邻接及自身末注顺读；root 非写入者已实际独读正文、完整邻接与自身末注，POST通过，窄锁释放。未核实现或复现实验，非日级 Gate。

- `SF-2026-ARXIV-2602-23333` — Daily `2026-02-28`；[SemanticVocoder exact-v1](https://arxiv.org/html/2602.23333v1)。2+2+2=6，必要 blocks24–89；连续语义锚与条件波形生成器的重建责任；重建质量反侧、非单因素控制、预训练/采样费用及声学 codec 回退近文。非原 packet 作者 feb28_ch23_finish 独立必要原证/实际 owner PRE完成；窄段已融入正文，作者实际正文/完整邻接及自身末注顺读；root 非写入者已实际独读正文、完整邻接与自身末注，POST通过，窄锁释放。未核实现或复现实验，非日级 Gate。

- `SF-2026-ARXIV-2602-23353` — Daily `2026-02-28`；[SOTAlign exact-v1](https://arxiv.org/html/2602.23353v1)。2+2+2=6，必要 blocks29–110、120–126，286–304只定点核梯度；配对 teacher→未配对 soft transport 关系；Eq12 teacher||student 无方向冲突，温度分母冲突隔离，弱锚点/域偏与 paired 回退近文。非原 packet 作者 feb28_ch23_finish 独立必要原证/实际 owner PRE完成；窄段已融入正文，作者实际正文/完整邻接及自身末注顺读；root 非写入者已实际独读正文、完整邻接与自身末注，POST通过，窄锁释放。未核实现或复现实验，非日级 Gate。

- `SF-2026-ARXIV-2602-23361` — Daily `2026-02-28`；[VGG-T3 exact-v1](https://arxiv.org/html/2602.23361v1)。2+2+2=6，必要 blocks29–59、61–88、99–106；离线 whole-view 写入固定 MLP 与相机 token 旁路并存；pose/softmax 反侧、camera 状态增长、目标符号及通信口径隔离。非原 packet 作者 feb28_ch23_finish 独立必要原证/实际 owner PRE完成；窄段已融入正文，作者实际正文/完整邻接及自身末注顺读；root 非写入者已实际独读正文、完整邻接与自身末注，POST通过，窄锁释放。未核实现或复现实验，非日级 Gate。

- `SF-2026-ARXIV-2602-22785` — Daily `2026-02-28`；[SceneTransporter exact-v1](https://arxiv.org/html/2602.22785v1)。2+1+2=5，具体 owner 差额深入；必要 blocks21–87、109–124、149–164，全局 part/patch 软覆盖 prior 与 K/V gate；hard exclusive、零预算/边缘退化保证隔离，拥挤漏计、同配置控制、token/步骤费用与普通 attention 共存近正文。非原 packet 作者 feb28_ch23_finish 独立必要原证/实际 owner PRE完成；作者实际正文/完整邻接及自身末注顺读，root 非写入者已实际独读新增正文、完整邻接与自身末注，POST通过，五项窄锁释放。未核实现/复现，不授日级 Gate。

- `SF-2026-ARXIV-2602-22917` — Daily `2026-02-28`；[SSMDG exact-v1](https://arxiv.org/html/2602.22917v1)。2+1+2=5，具体 owner 差额深入；必要 blocks19–79、84–98，fused 加一条高置信支持与 non-consensus robust reuse 分工；共享错误/空集合、边际非条件不变、派生 missing feature 与增强/标签/训练费用近正文。非原 packet 作者 feb28_ch23_finish 独立必要原证/实际 owner PRE完成；作者实际正文/完整邻接及自身末注顺读，root 非写入者已实际独读新增正文、完整邻接与自身末注，POST通过，五项窄锁释放。未核实现/复现，不授日级 Gate。

- `SF-2026-ARXIV-2602-22932` — Daily `2026-02-28`；[MSJoE exact-v1](https://arxiv.org/html/2602.22932v1)。2+1+2=5，具体 owner 差额深入；必要 blocks28–119、133–141、156–169，多 query/sampler/reader 共同消费接口；同帧 reader 对照、冻结多 query 反侧、preview 派生身份、总费用与原采样回退近文。Table4 总耗时与正文比例冲突、Eq9 梯度型标量写法及相似度奖励权限隔离，不授普遍联合训练必要性。非原 packet 作者 feb28_ch23_finish 独立必要原证/实际 owner PRE完成；作者实际正文/完整邻接及自身末注顺读，root 非写入者已实际独读新增正文、完整邻接与自身末注，POST通过，五项窄锁释放。未核实现/复现，不授日级 Gate。

- `SF-2026-ARXIV-2602-22644` — Daily `2026-02-28`；[FRM/MWAM exact-v1](https://arxiv.org/html/2602.22644v1)。2+1+2=5，具体 owner 差额深入；必要 blocks4–32、32–89、155–176、183–203、231–232，212–214仅小 batch 反侧；输入频谱 proxy/bank 到训练 gradient/loss 分配，非在线 truth/reliability；signed 分母、pretrained 适用性、完整/缺模态局部反退、PCR 基线和模块孤立成本近文。不采用 NTK/输入频谱的因果依赖保证，不遍历全 proof/artifact。非原记录作者 feb28_ch23_finish 独立必要原证/actual owner PRE完成；作者正文/完整邻接/自身末注顺读，root 非写入者已实际独读新增正文、完整邻接与自身末注，POST通过，五项窄锁释放；未核实现/复现，不授日级 Gate。

- `SF-2026-ARXIV-2602-23153` — Daily `2026-02-28`；[Fase3D exact-v1](https://arxiv.org/html/2602.23153v1)。2+1+2=5，具体 owner 差额深入；必要 blocks17–73、79–86，几何 pooling→多 SFC token-axis window 混频→compact 输入；channel FFT 非 token 交互、严格排列不变及 gate/graph/OT 配方隔离，clutter/纹理/空间失败与独立 encoder/更多 tokens 回退近文，pretraining/proposals 和 tokenizer-only FLOPs 分账。非原 packet 作者 feb28_ch23_finish 独立必要原证/actual owner PRE完成；作者正文/完整邻接/自身末注顺读，root 非写入者已实际独读新增正文、完整邻接与自身末注，POST通过，五项窄锁释放；未核实现/复现，不授日级 Gate。

- `SF-2026-ARXIV-2601-04442` — Daily `2026-01-10`；[GPRO exact-v1](https://arxiv.org/html/2601.04442v1) §3.1–3.3/Eq1–6及必要任务/长度/训练反侧。2+2+2=6，consumer 逐 token 额外感知/上下文 operator 的具体差额深入；teacher/entropy 非因果校准、7B反退、内部计算费用与原 FFN 回退近文。非原作者 jan10_books_audit 必要原证/actual owner PRE通过，记录于本日 post-audit-20261007.md §3；作者实际正文/完整邻接/自身末注已顺读，root 非写入者实际正文/完整邻接/自身末注 POST通过（GPRO长度已依POST限定MM-Vet切片），未核实现/复现，不授日级 Gate。

- `SF-2026-ARXIV-2601-05159` — Daily `2026-01-10`；[VLI exact-v1](https://arxiv.org/html/2601.05159v1) §3/Eq1–14、A.1–3/Eq15–22、E/Table4。2+2+2=6，GT-head 校准/双派生视图 hidden 差分具体差额深入；Eq15显式正交条件已纠偏，未授真实网络满足理论、mask因果真值或免费修复；温度上界、强 steering/抽象任务反侧与原路径回退近文。非原作者 jan10_books_audit 必要原证/actual owner PRE通过，本日 post-audit §3；作者实际正文/完整邻接/自身末注已顺读，root 非写入者实际正文/完整邻接/自身末注 POST通过，未核实现/复现，不授日级 Gate。

- `SF-2026-ARXIV-2601-05201` — Daily `2026-01-10`；[PIH exact-v1](https://arxiv.org/html/2601.05201v1) §3–4/AppD。2+2+2=6，baseline-correct 条件人口/mean-output 干预/内容与格式分账具体差额深入；top-m选择隔离未明、Janus正常计数与Qwen格式反侧、搜索/回归费用及原模型回退近文。非原作者 jan10_books_audit 必要原证/actual owner PRE通过，本日 post-audit §3；作者实际正文/完整邻接/自身末注已顺读，root 非写入者实际正文/完整邻接/自身末注 POST通过，未核实现/复现，不授日级 Gate。

- `SF-2026-ARXIV-2601-05939` — Daily `2026-01-13` 增量；[CEI exact-v1](https://arxiv.org/html/2601.05939v1) §3.2、§4.1–4.3/Eq6–8、Table3/Limitations。2+1+2=5，static last-input final-hidden anchor与诊断分责差额深入；动态Eq8符号冲突隔离不授recipe，coverage反侧、两forward成本与原路径共存近文。jan10_books_audit独立必要原证/actual owner PRE通过，root授Ch23窄锁；作者正文/完整局部邻接已顺读，root非写入者实际正文/完整邻接/自身末注POST PASS，窄锁释放。未核实现或复现，非日级Gate。

- `SF-2026-ARXIV-2601-09661` — Daily `2026-01-16`；[LiteEmbed exact-v1](https://arxiv.org/html/2601.09661v1) §3/Table2、A4/A5/A7。2+2+2=6，概念text token适配的alignment/discrimination具体gap深入；PCA/邻域非普适语义真值，5000步非零训练、generation换目标/coverage非mask正确及全部成本/原路径近文。root实际必要原证及owner PRE通过并授两段/自身note顺序窄锁；作者已实际顺读正文与627–658完整局部邻接及自身末注，root非作者实际独读627–652完整局部邻接/新正文及自身末注POST PASS，Lite锁释放。未核实现/复现，非日级Gate。

- `SF-2026-ARXIV-2601-09575` — Daily `2026-01-16`；[OpenVoxel exact-v1](https://arxiv.org/html/2601.09575v1) §4.1–4.3/Table1–5、A/C/E必要原证。2+2+2=6，centroid/group dictionary/caption派生载体的具体 owner gap 深入；SAM2/IoU合并非真实实例、caption非物理观测、part query被吞及小MLLM反退、已有scene fitting/全map请求成本近文。root实际必要原证及owner PRE通过并授两段/自身note顺序窄锁；作者已实际顺读928–956完整局部邻接与自身末注，root非作者实际独读928–956完整邻接/940,942新正文及自身末注POST PASS，Ch23锁释放。未核实现/复现，非日级Gate。

- `SF-2026-ARXIV-2601-08151` — Daily `2026-01-15`补充；[exact-v1](https://arxiv.org/html/2601.08151v1) §3–5.6/Eq1–4/Tables1–3。2+1+2=5，early-vs-late attention-difference到late visual soft-mask接口差额深入；热图非grounding/唯一因果，visual位置干预非删除全部传播信息、非physical pruning，候选层/过mask反侧与hooks/map费近文。review_jan15_delta实际必要原源/owner PRE通过，root授单段/自身末注锁；作者实际正文与完整邻接顺读，review_jan15_delta非作者actual正文/完整邻接及本末注POST通过，锁释放。未核实现/复现，非DAY。

- `SF-2026-ARXIV-2601-19399` — Daily `2026-01-29` 增量；[RT-MAE exact-v1](https://arxiv.org/html/2601.19399v1) §2.1–2.3/§3.1/Table1–2/τ及pitch消融。2+1+2=5，属性+残余双接口及整组dropout防旁路的具体gap深入；残余身份泄漏、代理MOS与有限编辑边界近文，不授MᵀV维度式实现。root实际必要Source/Ch23 owner PRE通过并授两段窄锁；作者已顺读正文与完整邻接，root非作者实际正文158–174完整邻接及自身末注POST通过，窄锁释放，未复现，非日级Gate。

- 2026-01-28 来源遗漏补查，arXiv:2601.18321v1：本日具名必要 Source 复用；resume_20260128_audit 实际逐字拟文、对应正文完整局部邻接 PRE 通过，root授本段与自身末注窄锁。已写入，resume_20260128_audit 非作者实际正文、完整局部邻接与自身末注 POST 通过，窄锁释放；直接反侧/费用与失败回退近正文，未核artifact/复现。<!-- source-family:SF-2026-ARXIV-2601-18321 -->
- 2026-01-28 来源遗漏补查，arXiv:2601.18393v1：本日具名必要 Source 复用；resume_20260128_audit 实际逐字拟文、对应正文完整局部邻接 PRE 通过，root授本段与自身末注窄锁。已写入，resume_20260128_audit 非作者实际正文、完整局部邻接与自身末注 POST 通过，窄锁释放；直接反侧/费用与失败回退近正文，未核artifact/复现。<!-- source-family:SF-2026-ARXIV-2601-18393 -->
- 2026-01-28 来源遗漏补查，DeepSeek-OCR2 Jan27 原repo稿（tree 16ba51c72bfff2891379d56444380270366fb032，PDF blob d99bcf673675f22f3dfcd9196c1384c818d8cff2）：2+2+2=6，ordered suffix readout具体接口差额深入；resume_20260128_audit 实际原PDF必要 Source、图5/式1与Ch23完整局部邻接/拟文 PRE 通过，root授一段与自身末注窄锁。已写入，resume_20260128_audit 非作者实际403–437完整邻接、415正文与自身1544末注 POST 通过，窄锁释放；非patch permutation/真实2D、训练混杂/局部退步/无GT生产重复率与完整计算反侧近文。未核artifact/复现，非日级验收。<!-- source-family:SF-2026-DEEPSEEK-OCR2 -->

- `SF-2026-ARXIV-2602-04202` — Daily `2026-02-05` date-only补充；[VTok exact-v1](https://arxiv.org/html/2602.04202v1) §3.1–3.2/Eq13–15、§4.1–4.4/Tables1–5。2+2+2=6，decoded-frame shared-feature reference residual与codec residual来源/成本差额深入；单motion瓶颈、参考失配与dense/更新参考回退为工程推断，不授自动reset或无损。T3非训练LLaVA Video-MMMU41.3→41.2反侧保留；T5 FPS/frames-per-token及token数方向冲突隔离，不授默认采样recipe、g_phi训练细节、统一离散词表或通用效率。root实际必要Source/owner PRE通过并授本段及自身末注单owner锁；作者实际写入并顺读局部完整邻接，root非作者实际800–840完整邻接、826正文及自身末注POST通过，窄锁释放。未核实现/复现，非日级验收。

- `SF-2026-ARXIV-2602-11824` — Daily `2026-02-14`补查；[REVIS exact-v1](https://arxiv.org/html/2602.11824v1) §3–7，先average grounded−blind后project blind hall−unknown、正向平均分离Δ最深层与quantile gate；100extract+100calibration、gate collapse/强注入损utility/CHAIRI反侧及TPT无hw，不授truth cause或修复缺失视觉。2+2+2=6，实际owner差额受影响深入。root/reviewer必要Source及actual owner/完整邻接与逐字拟文PRE通过，root授两段+本末注窄锁；作者已写并顺读完整邻接，review_20260214已实际独核新正文、完整邻接及本末注，非作者actual POST通过，root释放窄锁，不授DAY。未核artifact/复现。 本轮补查事件的首次公开日期未证，必要Source/PRE/实际POST研究仍有效，但不计本日已确认新增成果；归属只按[本日日报§5](../../papers/2026/02/14/README.md#5-缺口与下一步)的57日期请求定点重开，不撤正文或补造公开日。

- `SF-2026-ARXIV-2602-11596` — Daily `2026-02-14`补查；[MAPLE exact-v1](https://arxiv.org/html/2602.11596v1) §3–5/T1–4，2+2+2=6；signal-support/实际input/training-cohort分责差额必要深入。分模态标注不授最小充分真值，input+batch混杂、归一身份/方差理论、合成None与CRW因果中心不采用，负侧/全費/回退近文。非作者必要Source/actual逐字PRE通过，root授单段/本人note窄锁；作者实际新643/完整618–661与本人note顺读；reviewer非writer actualPOST通过，root释放窄锁，不授DAY；未核artifact/复现。 本轮补查事件的首次公开日期未证，必要Source/PRE/实际POST研究仍有效，但不计本日已确认新增成果；归属只按[本日日报§5](../../papers/2026/02/14/README.md#5-缺口与下一步)的57日期请求定点重开，不撤正文或补造公开日。

- `SF-2026-ARXIV-2602-11980` — Daily `2026-02-14`补查；[exact-v1](https://arxiv.org/html/2602.11980v1)，2+2+2=6，必要Source经review_20260214非作者限定通过，actual MULTIMODAL-REPRESENTATION owner/完整邻接与逐字拟文PRE通过，root授本一段及自身末注窄锁；作者实际新段/完整局部及本注顺读，非writer实际正文、完整局部邻接及本人末注actualPOST通过，root释放窄锁。具体费用、直接反侧及失配回退近正文，不授全recipe、普遍正确/因果/性能保证、实现复现或DAY。 本轮补查事件的首次公开日期未证，必要Source/PRE/实际POST研究仍有效，但不计本日已确认新增成果；归属只按[本日日报§5](../../papers/2026/02/14/README.md#5-缺口与下一步)的57日期请求定点重开，不撤正文或补造公开日。

- `SF-2026-ARXIV-2602-12160` — Daily `2026-02-14`补查；[exact-v1](https://arxiv.org/html/2602.12160v1)，2+2+2=6，必要Source与actual唯一owner/逐字拟文PRE经非作者通过，root授本段及本人末注窄锁；作者已顺读实际正文与完整局部邻接，非writer实际正文、完整局部邻接及本人末注actualPOST通过，root释放窄锁。费用、直接反侧、争议边界与旧路径回退近正文；未核完整执行recipe、实现或复现，不授DAY。 本轮补查事件的首次公开日期未证，必要Source/PRE/实际POST研究仍有效，但不计本日已确认新增成果；归属只按[本日日报§5](../../papers/2026/02/14/README.md#5-缺口与下一步)的57日期请求定点重开，不撤正文或补造公开日。

- `SF-2026-ARXIV-2603-07474` — Daily `2026-03-11`补查；[Taxonomic Generalization exact-v1](https://arxiv.org/html/2603.07474v1) 方法/实验与必要超参数（SUP_CORE_07474.txt 119–268、708–740），2+1+2=5；具体语言先验×视觉coherence成对控制差额定点深入。保留negative字符串暴露、同leaf图像split、类别/seed相关人口与不显著≠等价边界，不授任意迁移或唯一因果。review_mar11_continue实际必要Source、Ch23完整局部与逐字PRE通过，root授本段/自身末注窄锁；作者已写，写后完整657–733邻接与878–902交接已实际顺读，本注及Source195–217回对；review_mar11_continue实际新正文、完整局部邻接及本末注非writer POST通过，root释放窄锁，不授DAY。未核artifact或复现。

- `SF-2026-ARXIV-2603-07476` — Daily `2026-03-11`补查；[EVLF exact-v1](https://arxiv.org/html/2603.07476v1) §3.2/4.1–4.3/Alg1、§5.1–5.4/Table5/7及limitations（SUP_CORE_07476.txt 93–179、492–551、584–638、645–648），2+1+2=5，确认clean latent入口与双目标/denoiser适配差额定点深入。只采class-level接口与有限联合对照，保留额外训练、coverage生成点分母、全部费用与旧路径，不授instance无损或普遍质量/性能。review_mar11_continue实际必要Source与Ch23完整局部/交接及逐字PRE通过，root授本段/自身末注窄锁；作者已写，作者实际401–441完整邻接与1055–1069/700–714跨目标交接已顺读，写后415–429/本注及Source117–145回对；review_mar11_continue实际新正文、完整局部邻接及本末注非writer POST通过，root释放窄锁，不授DAY。未核artifact或复现。

- `SF-2026-ARXIV-2603-07659` — Daily `2026-03-11`补充Mar10自然日；[SCI exact-v1](https://arxiv.org/html/2603.07659v1) §3/Eq1–7、§4/Table3–5必要说明及B/C/Table6–8（72–108、144–156、309–566、772–885；未采Table2全库存或Table5精确checkbox）。2+1+2=5，确认logit聚合/视觉差分/支持集三接口差额定点深入；cross-prompt logit身份、筛选人口、mask反侧与完整费用近文，不授真实因果、普遍robust或概率校准。review_mar11_continue必要Source/actual owner/逐字PRE经root接纳并授本段及本人注窄锁；作者已actual顺读完整局部，review_mar11_continue非writer实际新正文/完整局部邻接/本人末注POST通过，root已释放窄锁，不授DAY。未核artifact/复现。

- `SF-2026-ARXIV-2603-09714` — Daily `2026-03-12`补查；[MUGEN exact-v1](https://arxiv.org/html/2603.09714v1) §2–6/Tables1–3，2+1+2=5；多候选order/remap identity缺口深入。限无真实顺序语义集合及同10generation有限对照，候选数量/chance/干扰混杂、投票非gold、额外编码/生成费用近正文；不采用Fig3精确曲线/内部容量因果、普遍排列不变、完整执行recipe/实时SLO或代码复现。root实际必要Source/date/owner逐字PRE通过并授两段与本注窄锁；supplement_20260312实际写入并顺读完整邻接，root非writer实际151–184局部、新161/164与本末注回对必要原证，actualPOST通过/窄锁释放，不授DAY。

- `SF-2026-ARXIV-2603-08436` — Daily `2026-03-11`补查；[VET-Bench/SGCoT exact-v1](https://arxiv.org/html/2603.08436v1) §2–5/7–8/F（SUP_CORE_08436.txt84–196/886–908），2+2+2=6。只采用已有video-grounded tracking→文本合成终态answer读出差额，lossmask非冻结/不授tracking无回归、真实轨迹/终态/任务分测及全部费用/原视频tracker退路近文。三杯有限结果与k≥5任意长度条件理论分离、有限91%与预训练费用反侧保本日证据，不采全B证明/pixels/内部因果。review_mar11_continue必要Source/actual owner与逐字PRE、root实际owner认可并授仅本段及自身注窄锁；作者actual998–1038完整邻接已读、已写；review_mar11_continue非writer实际998–1040完整邻接/新1018与本人1606注POST通过，root接纳并释放锁，不授DAY。未核artifact/复现。

- `SF-2026-ARXIV-2603-08497` — Daily `2026-03-11`补查；[FontBench exact-v1](https://arxiv.org/html/2603.08497v1) §3–6/Table1必要Qwen配对/Table2全部、B2–3/D/G（SUP_CORE_08497.txt126–194/327–444/1013–1033/1247–1266/1490–1498），2+1+2=5，字体属性读出差额与data-vs-capacity因果反侧定点深入。转录与appearance分测、render/parser/相关人口身份、FT改进非预存feature证书/失败非缺primitive、全部费用与专用readout/Unknown退路近文；精数/脚本稀疏/训练量化冲突保本日日报。review_mar11_continue必要Source/actual owner/逐字PRE经root接纳并授本段及本人注窄锁；作者actual526–553完整邻接与既有Ch22/24入口已读，已写入；review_mar11_continue非writer actual新增段/完整局部邻接与本人注POST通过，root接纳并释放锁，不授DAY。未核全库存、pixels、artifact或复现。

- `SF-2026-ARXIV-2603-08683` — Daily `2026-03-11`补查；[Trilobyte exact-v1](https://arxiv.org/html/2603.08683v1) §3–5/Table1必要全行/setup/transfer（CORE105–331），2+1+2=5。rawPCM byte接口对lossy semanticcodec的资源替代具体差额深入；常词表非短序列、CE/BPB估算非wire/roundtrip、metadata与24bit商业反侧/全费用及FLAC原PCM退路近文，比例/容量混杂只保本日证据。review_mar11_continue必要Source/actual唯一owner及逐字PRE通过，root授原272source注后/残差标题前单段与本人注窄锁；作者actual252–285完整邻接与Ch22/24交接已读并落实，review_mar11_continue非writer actual252–291完整邻接/新274及本人1632注POST通过，root接纳并释放本项窄锁。不授DAY、全附录/pixels、可执行coder、artifact核验或复现。

- `SF-2026-ARXIV-2603-10470` — Daily `2026-03-13`补查；[exact-v1](https://arxiv.org/html/2603.10470v1) §3 Eq1–11/必要§4主对照与反侧，2+1+2=5。mar13_admission_review非准备者实际Source/Ch23跨校准人口bank差额/PRE通过，未中心化SVD仅称主要奇异方向、不称统计方差。root两段融入cached差分与音频接口之间；不授唯一因果、全部事实保留或合并不同beam/吞吐协议，离线制备费用近文。未核artifact或复现；mar13_admission_review 实际非 writer 顺读新增两段、完整邻接与本注并回必要原证，POST 通过；root 回读并接纳，窄锁释放，不授 DAY。
