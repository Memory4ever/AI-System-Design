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

先忽略 mask 和位置。若输入矩阵 `X` 的 token 行被同一个 permutation matrix `P` 重排，Self Attention 的输出也会按相同方式重排。它可以根据内容建立关系，却不知道某行原本是第几个位置。

直觉上，下面两段 token 集合相同，语义却不同：

```text
dog bites man
man bites dog
```

如果模型只有三个 token embeddings，而没有顺序信号，它能看到“dog、bites、man”存在，却无法区分主客体顺序。

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
