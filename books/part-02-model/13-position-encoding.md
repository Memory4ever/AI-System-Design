# 第13章 Position Encoding

**Knowledge Tree:** Part II 模型：一个 Token 如何变成答案
**Stable Knowledge Node ID:** `MODEL-POSITION-ENCODING`
**Legacy Chapter:** Ch13
**Status:** Draft

**Roadmap Intent:** 为什么 Transformer 需要位置信息，以及绝对位置、相对位置、RoPE 的差异。

## 本章要回答的问题

Embedding 产生 `[B,T,d_model]` 表示，但如果交换两个 token 的位置，Self Attention 为什么不能仅凭内容知道谁先谁后？绝对位置、相对位置和 RoPE 分别把顺序放进模型的哪个位置？

本章的核心判断是：**Position Encoding 不是附加序号，而是打破 Attention 对排列的对称性，使模型能区分顺序并表达位置关系。**不同方案的根本差异在于：把位置加入 token representation，加入 attention score，还是作用于 Query/Key 的几何变换。

为了先理解位置如何进入模型，本章暂把 Query/Key 视为用于匹配内容的两组向量；第14章再完整推导它们与 Value 的关系及 Attention 计算。

本章使用 `B` 表示 batch size，`T` 表示 sequence length，`d_model` 表示 hidden dimension，`d_h` 表示单个 Attention head dimension。

## 为什么纯 Self Attention 看不见顺序

先在精确算术中忽略 mask 和位置。若输入矩阵 `X` 的 token 行被同一个 permutation matrix `P` 重排，Self Attention 的输出也会按相同方式重排。这个理想算子可以根据内容建立关系，却不知道某行原本是第几个位置。

直觉上，下面两段 token 集合相同，语义却不同：

```text
dog bites man
man bites dog
```

在这个理想算子中，如果模型只有三个 token embeddings，而没有顺序信号，它能看到“dog、bites、man”存在，却无法区分主客体顺序。

从理想算子进入有限精度实现时，这项对称结论需要重新限定：浮点加法不结合，固定 left-associative 的归约顺序可以破坏一般排列等变性。[受限理论构造](https://arxiv.org/html/2601.16450v1)的无 mask、无位置编码网络仍保留首两个位置交换的对称，也存在长序列表示碰撞；舍入带来的顺序依赖并不等于完整、可靠的位置坐标。这个构造既不证明现实 GPU kernel 都具有同一行为，也不授真实 LLM 的长度阈值或训练可学性，不能用它把显式位置编码当作多余。

因此位置 owner 必须区分三件事：理想算子的排列对称、具体 precision/reduction order 的数值行为，以及模型可稳定使用的位置输入。仅观察到舍入使输出不同，不能证明模型已学会主客体或距离；尚未建立可验证的顺序机制时，仍应保留训练与推理一致的显式位置编码。下文先沿这个可控的位置接口推导方案。<!-- source-family:SF-2026-ARXIV-2601-16450 -->

RNN 的递归计算天然携带时间步，CNN 的 kernel 连接隐含局部位置；纯粹的、无 mask 的 Self Attention 没有这些连接结构，因此需要另一个顺序来源。传统 Transformer 选择显式位置编码；局部或递归混合也可能把顺序写入 hidden state。需要的是可被模型使用的位置关系，而不是每一层都必须附加一份位置向量。

## 最直接方案：绝对位置向量

设 token embedding 为：

```text
X in R^(B x T x d_model)
```

为每个 position `p` 构造向量 `P_p in R^(d_model)`，再相加：

```text
H_0[b,p,:] = X[b,p,:] + P_p
H_0 shape   = [B,T,d_model]
```

相加保持 shape 不变，让后续投影同时读取 token 内容和位置。最简单的 `P` 可以是 learned embedding table：

```text
P in R^(T_max x d_model)
```

优点是模型自由学习每个位置；代价是需要预设 `T_max`，未训练位置没有自然定义，而且参数把位置当成彼此独立类别。

位置向量如何与内容结合，也属于表示设计，而不只是选用哪种编码。相加保持接口简单；concat再投影让模型学习两路组合，逐token scalar gate则在共享维度上调节内容与位置的比例，局部卷积gate还能读取位置邻域。这些分支支付额外参数、计算与训练校准，不保证gate更适合所有长度。[固定encoder的受限配对对照](https://arxiv.org/html/2601.05807v1)支持同时比较编码与fusion operator，但只覆盖小模型文本classification；不同corpus的长度和任务混杂，不能外推为decoder生成或长Context通用优势。原加法已稳定、预算紧或长度迁移未验收时，应保留add基线，不把更复杂融合当作位置编码的必然下一代。<!-- source-family:SF-2026-ARXIV-2601-05807 -->

## Sinusoidal encoding 为什么出现

原始 Transformer 使用不同频率的正弦和余弦：

```text
PE(pos, 2i)     = sin(pos / 10000^(2i / d_model))
PE(pos, 2i + 1) = cos(pos / 10000^(2i / d_model))
```

其中：

- `pos` 是位置；
- `i` 是二维频率对索引；
- `d_model` 是向量维度。

低维对变化较快，高维对变化较慢，多个频率共同为位置提供编码。由于三角函数的平移关系，`PE(pos+k)` 可以由 `PE(pos)` 的线性组合表示，这为模型利用相对偏移提供结构。

Sinusoidal encoding 不需要为每个位置学习独立参数，也可以计算训练长度之外的位置。但“公式可计算”不等于模型能有效使用任意更长位置。模型仍只在有限长度分布上优化，第22章会处理这种外推边界。

## 一个绝对位置小例子

假设 `d_model=2`，同一 token embedding 为：

```text
x = [1.0, 0.0]
```

位置向量为：

```text
P_0 = [ 0.0, 1.0]
P_1 = [ 0.84, 0.54]
```

相加后：

```text
h_0 = x + P_0 = [1.0, 1.0]
h_1 = x + P_1 = [1.84, 0.54]
```

同一个 token 因位置不同得到不同输入状态。这个例子只说明位置被注入，不说明后续模型必然学会距离或顺序规则。

## 为什么还需要相对位置

很多任务更关心“相距多远”和“谁在谁之前”，而不是绝对索引。例如局部依赖在位置 10 与 11、位置 100 与 101 可能具有相似意义。

Relative Position Representation 可以直接让 attention score 或 value 聚合依赖 `i-j`：

```text
score(i,j) = content_score(i,j) + relative_bias(i-j)
```

具体方法可能使用可学习向量、bucketed distance 或额外 score term。共同原则是：位置关系进入 token pair 的交互，而不是只在输入端相加一次。

优势是相同相对距离可以跨绝对位置共享；代价是 score 计算、索引和实现更复杂，超出训练距离时仍需要定义 clipping、bucket 或 extrapolation 行为。

## ALiBi：把距离偏好直接写进匹配分数

ALiBi（Attention with Linear Biases）不向 hidden state 加位置向量，而是按 head 为较远的
key 加线性负 bias。对 causal Attention，可把距离项简写为：

```text
score_h(i,j)
= content_score_h(i,j) - m_h * (i-j),  j <= i
```

不同 slope `m_h` 让不同 heads 具有不同的距离偏好；它用一个简单的线性项表达局部性，而不是给每个位置学习独立向量。这个实数公式的有限精度边界，在比较几种位置机制后再讨论。

## RoPE：把位置变成旋转

Rotary Position Embedding 不把位置向量直接加到 hidden state，而是对 Query 和 Key 的二维子空间执行与位置相关的旋转。

对二维向量 `x = [x_1,x_2]`，位置 `m` 的旋转可写为：

```text
R(m,theta) = [ cos(m*theta)  -sin(m*theta)
               sin(m*theta)   cos(m*theta) ]

x_m = R(m,theta) x
```

实际 `d_h` 维 Query/Key 会被分成多个二维 pair，每对使用不同频率 `theta_i`：

```text
q_m = R_m q
k_n = R_n k
```

关键性质来自旋转矩阵：

```text
q_m^T k_n
= q^T R_m^T R_n k
= q^T R_(n-m) k
```

点积中的位置影响只与相对偏移 `n-m` 有关。RoPE 因而在保留绝对相位的同时，让 attention score 自然携带相对位置结构。

这也给出一种内容变化时仍能偏好特定相对位置的条件分支：若某个 head 的 pre-RoPE Query/Key **activation** 在不同 token 上集中于近似相同方向，且范数与 token-pair 系数变化很小，其二维 pair 的点积可近似为相对位移上的 Fourier 项；幅度与相位近乎不变时，位置曲线便可能主导该 head 的注意力。这里低秩的是受测激活，不是投影权重；仅看到 rank-one、却未控制方向符号和尺度变化，也不足以得到内容近不变的曲线。[受限研究](https://arxiv.org/html/2601.08297v1)的频段干预进一步改变局部位置偏好，但不证明所有模型都依赖同一频段。

该分支不能把 RoPE 变成通用的“语义无关定位器”：自然文本与随机 token 实验采用不同强度阈值，不能据此声称相同阈值下的 OOD 保持；特定 head 的近不变性也不等于整层或最终输出不依赖内容。训练理论只覆盖有共同方向、正交语义坐标与指定频率条件的受限两层模型、目标及优化设定，不认证真实 LLM 都会沿这条路径学会位置规则。频段诊断还增加采样与干预成本，未证明权重压缩或长上下文收益；这些条件未满足时，仍保留一般的内容相关 Query/Key 与原 RoPE 机制，而不据低秩观察删减权重。<!-- source-family:SF-2026-ARXIV-2601-08297 -->

## 一个 RoPE 小例子

假设二维 Query 与 Key 都是：

```text
q = k = [1,0]
```

每个位置旋转 90 度：

```text
position 0: R_0 q = [1,0]
position 1: R_1 k = [0,1]
```

二者点积为 0。若 Query 和 Key 都位于 position 1，它们都旋转为 `[0,1]`，点积仍为 1。这个极简例子展示：共同平移不会改变相对关系，不同位置差会改变匹配。

真实 RoPE 使用多组频率，不会每个位置都旋转 90 度；例子只用于验证相对几何。

相对 reading-order 距离仍没有唯一指定文本结构：相同 token 序列可以被不同 paragraph 边界分段。将 paragraph、sentence、token 坐标分配给不同 RoPE channel 后，可以只改 paragraph 坐标、保持其余坐标和 token 序列不变，检验结构信号是否影响表示。但“出现压缩”本身不证明模型用了真实层级；[受控研究](https://arxiv.org/html/2609.23551v1)的随机 paragraph 轴也产生 compression。其更强的检查是在每个精确 token distance 内比较 paragraph 位移，再按 pair count 加权，同时对照架构、频段、密度和训练预算匹配、每个训练 step 重采样的随机轴；仅线性距离残差或粗 distance bins 不足以消除混杂，旧 bins 甚至能翻转 WikiText 的符号。

真实与随机层级的 compression depth 差在 Code/WikiText 的区间排零，却在 OpenWebText 的 CI [-.059,.093] 不排零；depth 也不等于可稳定识别的 minimum 位置，更不是已识别内容机制或 Riemannian 度量。实验仅为八层/八头、d=512、context 1024、5,000 steps、三 seed，hardware/dtype 未披露；document-cluster bootstrap 刻画固定 corpus 内的抽样，三 seed 方向不构成正式显著性证明。相对 flat RoPE，WikiText/OpenWebText 还付出小 validation-loss 代价，未测大模型、下游或 serving 收益。故层级坐标改变的是需验收的结构假设；真实结构未胜过 matched-random null 或质量 Gate 失败时，flat RoPE 仍应保留，而非因出现几何压缩就推荐新编码。<!-- source-family:SF-2026-ARXIV-2609-23551 -->

## 连续二维位置编码需要显式坐标身份

<!-- semantic-body-binding:SF-2026-ARXIV-2605-23719:start -->
固定二维表或二维 RoPE 在规则 lattice 和有限分辨率下容易实现；连续二维分支把坐标映射为可计算函数，并从代数结构派生 relative relation，使不规则采样或分辨率变化不必重新查表。Position identity 因而要包含坐标系、lattice、函数 revision 与数值精度，而不能只记录最大长度。

连续函数改善几何外推，却增加数值敏感性、坐标规范和任务失配风险。exact-v1 只支持作者理论假设与实验设置，不保证任意视觉网格或尺度都优于既有方案；稳定性、aliasing 或下游质量 Gate 失败时，应回退二维 RoPE、learned table 或目标分辨率内的离散位置。arXiv:2605.23719v1
<!-- semantic-body-binding:SF-2026-ARXIV-2605-23719:end -->

训练位置的采样分布也是设计变量，而不只是选择 RoPE 或 ALiBi。一条受限分支在训练时排序采样 `[0,1)` 内的随机浮点坐标，使相同序列长度见到不同间距；推理则用确定性坐标 `(2i−1)/(2 max(n_train,n_infer))`，将训练与测试长度放入同一有界支持。这让训练人口不再只覆盖固定整数步长，却不能从坐标永远有定义推出无限长度质量。[作者小模型实验](https://arxiv.org/html/2602.14050v1)有三 seed 合成任务与 GPT-2-base 对照，也有随机分布失配及下游不改善的反侧，未测生产时延/SLO。作为我们的系统推断：若增量生成真的改变该 `max` 分母，旧 token 坐标随之改变，依赖位置的既有 KV 不能直接沿用，须冻结既定长度口径或重算；当分母不变时没有这一额外失效。该 cache 推论不是作者已测结果，质量、预算或身份无法保持时仍用固定坐标与原编码。<!-- source-family:SF-2026-ARXIV-2602-14050 -->

从二维扩到点云时，坐标参数化与频段分配也须联合验收，而非增加一个空间轴便获得几何等变。[SoPE 的有限对照](https://arxiv.org/html/2602.22716v1#S4)保留序列 index `t`，把三维坐标变为 `r/θ/φ`，再分配 RoPE pairs 并混合多个坐标尺度；`t` 不是观测时钟，相位中的球坐标差也不等欧氏距离或旋转/平移等变。作者室内三维检测中，四轴均分会低于原方案，偏重序列的分配改善；Cartesian 分支加入多尺度也有收益，不能把总增量唯一归球坐标。原点、轴向、角度 wrap/奇点与尺度变换的数值责任仍须由实现显式处理，这是我们的采用条件，不是论文已证明的通用协议；原稿也未完整指定每个变换。频段搜索、坐标规范与训练计费，规划展示不授实机安全或长程泛化；数据支持、数值或质量失配时保留 Cartesian、多轴原 RoPE 或固定离散位置。<!-- source-family:SF-2026-ARXIV-2602-22716 -->

## Position 方案的设计取舍

| 方案 | 位置进入哪里 | 主要优势 | 主要边界 |
| --- | --- | --- | --- |
| Learned absolute | 与 token embedding 相加 | 灵活、实现直接 | 固定表长度，外推弱 |
| Sinusoidal absolute | 与 token embedding 相加 | 无额外位置参数，可计算新位置 | 训练外长度仍不保证有效 |
| Relative position | Attention pair score/value | 直接共享相对距离 | 计算与索引更复杂 |
| ALiBi | Attention score 的 head-specific 线性 bias | 机制简单，直接表达距离偏好 | slope、长度与有限精度共同形成有效窗口 |
| RoPE | 旋转 Query/Key | 点积自然依赖相对偏移 | 频率与长度外推仍有边界 |

表格描述机制层差异，不代表所有现代模型只会选择其中一种。具体实现可能叠加 bias、局部窗口或 scaling 方法。

## Causal mask 不是 Position Encoding

Decoder-only 模型使用 causal mask 阻止位置 `i` 读取未来位置 `j>i`。Mask 定义“哪些连接允许存在”，Position Encoding 定义“允许连接的位置之间有什么顺序关系”。

Mask 首先约束可见性，它不直接提供一张可控的距离编码表。不过，不对称的可见集合会影响聚合后的 hidden state，因此“没有显式位置编码”并不等于“没有任何顺序信号”。双向模型也需要某种位置来源，不能仅靠 token 内容恢复次序。

### 局部混合可以产生隐式位置，但读取它仍有条件

显式编码的优点是位置关系由设计者指定，容易检查和控制；代价是频率、窗口与数值实现必须和训练一致。另一条条件分支不在 global Attention 中额外加入编码，而是在此前的 sliding-window Attention 或递归混合中形成与距离相关的状态。相邻位置读取重叠的局部历史，hidden state 因而可能比远端更相关；固定局部窗口也使这一相关结构不必随总序列长度增长而被平均稀释。

但“附近 hidden states 更相似”还不是“global Attention 更偏好附近”。设距离为 `d` 的跨位置二阶矩为 `G(d)=E[x_i x_(i-d)^T]`；Q/K 投影将它读成 logit，近远差异取决于该矩阵差与投影方向的对齐。独立、零均值的随机 Q/K 初始化，其期望读取未必有 recency bias；学习后的投影也可选择、弱化甚至反转这条信号。Residual addition、normalization 和 MLP 是否保留它，还受输入相关性及相应近似假设约束。

因此这不是 RoPE 或 ALiBi 的无条件替代，而是“局部混合形成信号 → 中间变换保留 → 全局投影有效读取”的架构分支。它减少显式位置设计，却增加对训练形成的通道和混合配置的依赖，距离信号也不等同于精确坐标。受限的 120M/350M 模型实验与 mean-profile 理论支持这一解释，尚未证明无限长度外推或任意 MLP 都保序；需要固定窗口、目标长度和任务上的行为测试。信号读取不稳定、精确相对关系重要时，显式编码仍是合理选择。
<!-- source-family:SF-2026-ARXIV-2609-38109 -->

## 位置有定义之后，还要验证它是否可用

几种机制已经给出了位置进入模型的方式，接下来有两种不同的失败：数学上可区分的远距离关系可能在有限精度执行中消失，坐标看起来不同也不保证模型能在任务中利用这种差别。

### ALiBi 的有限精度窗口

不同 slope `m_h` 让部分 heads 更偏向局部位置。在线性 bias 的数学定义中，任意有限距离
都有一个实数 score；但 softmax 实际在有限精度上计算。当距离增大到使
`exp(score_h(i,j) - max_score_h)` 下溢为零时，对应连接的 attention weight 会精确变成零。
于是系统形成一个没有在模型配置中声明的**隐式有效窗口**：位置仍可编号、pair 仍被计算，
该 head 却已经无法从远端 token 取回信息。

这个边界不能只由 advertised context length 判断。它同时依赖 slope、dtype、content logits、
softmax/kernel 实现以及是否 clamp。其系统含义是：

- “位置函数在该距离有定义”不等于“有限精度执行仍保留可观测连接”；
- 只看平均 perplexity 可能掩盖少数 heads、特定距离与 retrieval slice 的失效；
- 若设计本意就是局部 Attention，显式 window/sparse mask 通常比先计算再依赖 underflow
  更容易定义语义、节省工作并测试边界；
- clamp bias、调整 slope、对距离取对数或 soft-cap logits 都是在改变归纳偏置，不能被当作
  数值上等价的通用修复。

2026 年一项小规模实验在若干 ALiBi pretrained models 与 148M decoder 训练中观察到这一
failure mode，也发现默认 ALiBi 在部分 retrieval 设置中仍是强 baseline，多个缓解方案并不
稳定叠加。因此这里沉淀的是 `Status: Experimental` 的数值契约与验证方法，而不是“ALiBi
已失效”或某个替代方案已经胜出。旧方案在训练窗口、目标 dtype 与实测 retrieval 范围内仍然
成立；超出这些条件时才需要重新校准。

## 从坐标可辨识到行为可验证

### “可计算”还不等于“可唯一辨识”

RoPE 在任意整数位置都能计算旋转，因此比固定 learned table 更容易延伸；但表示是否唯一还取决于频率、有限维度、token projection 和判定协议。需要分别检查 position inversion/aliasing 与 token inversion/aliasing：同一表示可能无法唯一恢复位置，也可能让不同 token-position 组合在所用 protocol 下不可区分。

这个边界不是说 RoPE 必然失效，而是说多 head、多 layer 或更长公式定义本身不能自动消除表示碰撞。实际系统仍需在目标长度、dtype、频率配置和任务上验证；碰撞或行为退化时，回退训练窗口、缩放/重训、分段 Context 或显式检索。理论协议与作者 indexing 实验只限定其假设下的表示能力，不证明所有真实模型都达到最坏情形。

<!-- source-family:SF-2026-ARXIV-2605-15514 -->

位置表示从固定或旋转编码走向更长窗口时，必须区分静态相关、训练过程中通道如何形成，以及删除或扰动该通道后的因果效果。最终 probe 相似不等于模型真实依赖该位置通道，外推长度也不等于可用信息距离同步增加。

调整 RoPE 的频率坐标，与对 attention signal 的谱幅度乘一个平滑窗，也是不同对象：前者改变旋转相位，后者改变对应分量的幅度，不能把连续高通滤波的 sinc/ringing 论证直接赋给 frequency initialization。[CoPE exact-v1](https://arxiv.org/html/2602.05258v1)提出低频软变换并给出有限长窗对照，但其幅度窗证明不认证频率替换的普遍等价；精确默认比例叙述不一致时，不应拼成可执行配置。初始化替换、64K continued pretraining 与推理期 YaRN 扩窗需分别记录身份和成本，所谓 drop-in 不等于无再训练验证；GPQA 等切片仍可低于 hard clipping。变换失配、短窗质量退步或成本不值得时，保留原 RoPE 频率、已训练窗口、经独立校准的 scaling 或分段检索，不由长窗平均收益覆盖这些共存边界。<!-- source-family:SF-2026-ARXIV-2602-05258 -->

更复杂的位置机制可以改善长度泛化，却增加数值精度、频率别名和训练—推理不一致。消融或长序列行为不稳定时，应回到已训练窗口、分段 Context 或显式检索；绝对、相对、RoPE 与 ALiBi 仍是不同 workload 下的条件分支。

### 隐藏坐标的相似不能替代输出分布的几何

前面的 aliasing 检查问编码是否保留了可区分关系；这里再问：换一种内部坐标后，观察到的距离变化是否真的对应行为变化。这是评价位置干预的边界，不是另一种位置编码方案。

<!-- semantic-body-binding:SF-2026-ARXIV-2609-11063:start -->
在固定模型、固定基底内，用 cosine 或 Euclidean distance 比较带位置信息的 hidden state，是便宜而有用的实现诊断；但它隐含了“隐藏坐标本身可比较”的旧约束。只要对隐藏空间做一个由下游权重抵消的可逆重参数化，hidden-state 距离就可能显著改变，而 next-token 分布完全不变。因此，跨层、跨 checkpoint 或跨实现比较位置表征时，隐藏空间对齐只能回答“坐标是否相似”，不能独立回答“行为是否等价”。

行为层的比较应转向模型实际提交的 categorical next-token law：在词表、tokenization、上下文和输出粗粒化方式一致时，可用 Hellinger distance 或其局部 Fisher–Rao metric 衡量小扰动造成的输出变化。这个接口把位置条件化后的内部状态投影到可观察行为，但并不反向证明某个唯一位置坐标，也不取代 hidden probe 对具体实现的诊断；两类测量回答的是不同问题。

Fisher geometry 还可以把“以最小输出扰动完成一次局部编辑”写成自然梯度式控制问题，但代价是估计度量、阻尼与矩阵自由求解，有限幅度编辑还必须重新线性化。理论下界可能在真实模型上很松，输出一致也可能掩盖任务层面的长程失败。因此 fallback 仍是：在固定基底内保留 hidden probe，同时执行直接的输出分布、长度外推与下游任务测试；没有这些交叉证据时，不把几何对齐提升为位置机制已被因果使用的结论。该边界来自一组受控路由编辑和数学构造，不能外推为任意模型、任意尺度的全局保证。
<!-- semantic-body-binding:SF-2026-ARXIV-2609-11063:end -->

## 工程约束

位置机制会影响多个系统边界：

- `T_max` 或 RoPE 配置必须与 checkpoint 一致。
- KV Cache 必须与生成缓存时所用的位置变换和 position ids 保持一致；position index 错误会污染后续 Decode。
- Prefix reuse、sequence packing 和 sliding window 必须正确维护 position ids。
- Padding、left padding 与 right padding 可能改变 position id 构造。
- 扩展 context length 不能只修改配置，还要验证模型有效利用和系统容量。
- 对 score-bias 方案按 head、distance、dtype 观察 logits、非零 attention fraction 与 retrieval，
  不能用“kernel 没报错”证明远距离仍可访问。

这些问题说明 position id 是模型运行时状态的一部分，而不是 UI 层的 token 序号。

## 本章在知识树中的位置

```text
Embedding X [B,T,d_model]
-> add / apply position information
-> positioned states [B,T,d_model]
-> Q/K projection and Self Attention
-> Long Context constraints
```

这张图表示概念依赖，不要求所有位置机制都先改写 `X`：绝对位置向量在输入端相加，RoPE 在 Q/K 投影后旋转，ALiBi 则在 score 上加入距离偏置。本章负责这些接入方式；第14章会展开它们所连接的完整 Attention 计算；第22章再讨论长度外推、计算、KV Cache 和有效利用的联合约束。

## 自检问题

1. 为什么没有位置机制的 Self Attention 对输入排列具有对称性？
2. Learned absolute position 的 table shape 是什么？
3. Sinusoidal encoding 为什么使用多组频率？
4. 公式可以计算更远位置，为什么不保证模型能有效外推？
5. Relative position 与 absolute position 把关系放在不同的什么位置？
6. RoPE 对哪些张量执行旋转？
7. `R_m^T R_n = R_(n-m)` 表达了什么相对关系？
8. Causal mask 和 Position Encoding 分别约束什么？
9. KV Cache 为什么必须维护正确 position index？
10. 为什么 context extension 不属于本章的单点结论？
11. 为什么一个数学上有定义的 ALiBi score 仍可能在有限精度 softmax 中形成隐式窗口？

## 小结

Transformer 取消递归后获得并行性，也失去了天然顺序。Position Encoding 通过绝对向量、相对 score 或 Query/Key 旋转重新提供顺序结构。

Learned 与 sinusoidal absolute encoding 在输入端加入位置，relative representation 直接改变 pair 交互，RoPE 则用旋转让点积依赖相对位移。它们解决“模型如何看到位置”，不单独解决“模型能否有效使用任意长上下文”。

## Review notes

- `SF-2026-ARXIV-2601-16450` — Daily `2026-01-27`；[exact-v1](https://arxiv.org/html/2601.16450v1) §2.2–4.2 与 §5.1 构造开头。3+1+3=7，深入只修正精确算术对称性移植有限float时的条件；fixed left-associative、ties-even、正确舍入exp/ReLU属于该网络定义，首二交换与长序列碰撞反侧保留。不采用一般GPU归约、实际LLM长度阈值或舍入替代位置编码。root必要原源/具体owner写前核通过并授窄锁；root实际22/31/33/35与32–42前后交接非作者POST通过，日级Gate待验。未运行代码或复现实验。

- `SF-2026-ARXIV-2601-05807` — Daily `2026-01-13`；exact-v1 §3–9。采用编码与fusion共同验收的条件分支，scalar gate不是普遍featurewise融合；paired小encoder classification与跨corpus长度混杂保留，不授generative长Context收益。未复现；root必要源/owner写前通过，实际写后待复核。

- [Local mixing without explicit PE v1](https://arxiv.org/html/2609.38109v1) §III–VI、Appendix A；Daily 2026-09-30。只采用局部相关、Q/K对齐与expected recency的条件解释；无显式PE不等无顺序，有限实验不证明任意长度，未复现。

本章完整推导 absolute、relative 与 RoPE 的机制差异，并将 causal mask、context extension 与位置机制分开。后续 Review 任何 RoPE scaling 或最大长度结论都应移到第22章，并针对具体模型与训练分布核验。

Primary-source 校验入口：

- Ashish Vaswani et al., "Attention Is All You Need", 2017: https://arxiv.org/abs/1706.03762
- Peter Shaw, Jakob Uszkoreit, Ashish Vaswani, "Self-Attention with Relative Position Representations", 2018: https://arxiv.org/abs/1803.02155
- Jianlin Su et al., "RoFormer: Enhanced Transformer with Rotary Position Embedding", 2021: https://arxiv.org/abs/2104.09864
- Christopher Schröder et al., "When Attention Goes Blind: Numerical Failure in ALiBi Positional Encodings"（Status: Experimental）, 2026: https://arxiv.org/abs/2608.03994

### Daily Books delta trace（2026-06—08）

<!-- daily-books-trace:SF-2026-ARXIV-2606-21249:start -->
- `SF-2026-ARXIV-2606-21249` — Daily `2026-06-20`；primary `arXiv:2606.21249v1`；Books review `books-review:SF-2026-ARXIV-2606-21249`。

  **已吸收的语义增量：** 位置表示的训练动力学需要区分静态相关、训练演化与因果消融，最终 probe 相似度不能证明模型真的使用该位置通道
<!-- daily-books-trace:SF-2026-ARXIV-2606-21249:end -->

- `SF-2026-ARXIV-2602-14050` — Daily `2026-02-18`；[exact-v1](https://arxiv.org/html/2602.14050v1) §3/Algorithm1、§4必要对照/反侧。2+1+2=5，训练随机间距与推理max-length坐标具体差额深入；只采用有界支持/有限实验，不授无限长度质量，cache分母改变的重算责任明确为系统推断。root必要源/actualowner PRE通过，实际正文/邻接与末注经root非作者POST通过，窄锁释放；未核实现或复现，非日级验收。

- `SF-2026-ARXIV-2601-08297` — Daily `2026-01-15`；[exact-v1](https://arxiv.org/html/2601.08297v1) §4.1–4.2/Eq9–10、4.4 与 §5.1–5.3/讨论。2+1+3=6，特定 head 激活方向/范数近不变→Fourier 位置曲线的具体缺口深入；不把 activation 低秩当权重低秩、不同阈值 OOD 当同强度保证或受限训练定理当 LLM 普遍规律。频段反侧、成本及旧内容相关分支保留，不采未来压缩/长上下文收益。未运行代码/复现实验；root 实际必要原源及 owner 写前核通过并授窄锁，root已实际核正文、前后交接及末注，非作者 POST 通过；日级 Gate 未授。

- `SF-2026-ARXIV-2602-22716` — Daily `2026-02-28`；[exact-v1](https://arxiv.org/html/2602.22716v1) §4–5必要方法/消融，2+1+3=6；fresh非旧作者独核prepared原证与actual owner，3D坐标×序列/空间频段预算差额。均分反退/Cartesian控制、序列index非clock、非几何等变、数值条件与搜索训练费用近文；root授Ch13窄写ownership，作者实际正文/完整邻接顺读，root非作者实际正文、完整邻接及自身末注POST通过，窄锁释放。未核实现/复现，非日级Gate。
