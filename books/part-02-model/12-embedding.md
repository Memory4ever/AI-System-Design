# 第12章 Embedding

**Knowledge Tree:** Part II 模型：一个 Token 如何变成答案
**Stable Knowledge Node ID:** `MODEL-EMBEDDING`
**Legacy Chapter:** Ch12
**Status:** Draft

**Roadmap Intent:** 离散 token 如何进入连续向量空间，模型如何在向量空间里表达语义关系。

## 本章要回答的问题

Tokenizer 已经把文本转换成 `[B,T]` 的 token ids，为什么这些编号还不能直接充当模型的数值表示？一个没有大小、方向和距离含义的整数，怎样进入可微分的连续空间？Embedding 究竟是在保存词义，还是只为后续网络提供一组可学习坐标？

本章的核心判断是：**Embedding 不是把 token 翻译成固定的“语义答案”，而是把离散符号映射为可被梯度优化的初始表示。**上下文含义要到后续 Transformer layers 中才逐步形成。

本章使用 `B` 表示 batch size，`T` 表示 sequence length，`V` 表示 vocabulary size，`d_model` 表示 hidden dimension。

## 如果直接使用 token id

假设三个 token 的 id 分别是 `17`、`231` 和 `9042`。这些数字只表示词表中的行号，不表示 `231` 比 `17` 更大，也不表示数值距离具有语义。

如果把 id 作为标量送入线性层，模型会被迫把任意编号解释为有序数值。重新排列 vocabulary ids 就会改变全部输入几何，即使 tokenizer 切分结果没有变化。

正确起点是把每个 id 视为类别索引。最直接的类别表示是 one-hot：词表大小为 `V` 时，每个 token 使用 `V` 维向量，只有对应位置为 1。它消除了虚假的大小关系，却带来高维稀疏与 token 之间两两正交的问题。

## 从 one-hot 到 embedding table

设 embedding matrix 为：

```text
E in R^(V x d_model)
```

其中 `V` 是 vocabulary size，`d_model` 是模型 hidden dimension。token id `i` 的表示是 `E` 的第 `i` 行：

```text
x_i = E[i]
```

这也等价于 one-hot vector 与 `E` 相乘：

```text
x_i = one_hot(i) E
[1,V] x [V,d_model] -> [1,d_model]
```

数学上是矩阵乘法，工程实现不会真的构造 one-hot tensor，而是按 id gather 对应 rows。**Lookup 是执行方式，可训练坐标才是模型机制。**

对于 batch token ids：

```text
input_ids  [B, T]
E          [V, d_model]
X = E[input_ids]
X          [B, T, d_model]
```

这个 shape `[B,T,d_model]` 会贯穿 Position Encoding、Attention、MLP 和 Transformer Layer。

## 一个小型 lookup 例子

假设 `V=4`、`d_model=3`，embedding table 是：

```text
E = [
  [ 0.2,  0.1, -0.3],
  [ 0.0,  0.5,  0.4],
  [-0.2,  0.7,  0.1],
  [ 0.6, -0.1,  0.2]
]
```

输入 ids 为：

```text
input_ids = [[2, 0, 3]]    shape [1,3]
```

Lookup 结果只是按顺序取第 2、0、3 行：

```text
X = [[
  [-0.2,  0.7,  0.1],
  [ 0.2,  0.1, -0.3],
  [ 0.6, -0.1,  0.2]
]]                         shape [1,3,3]
```

此时模型有了可计算向量，但还不知道 token 的位置，也没有让任意 token 读取上下文。

## 向量关系从训练目标中形成

Embedding 通常随机初始化或由已有 checkpoint 加载。沿输入 lookup 路径，最终 loss 的梯度会流回本次出现 token 对应的 rows；若输入与输出共享参数，同一张表还会接收输出侧梯度，后文再区分这两条路径。

如果某些 token 在相似上下文中对预测具有相似作用，优化可能让它们形成相近方向。点积和余弦相似度可用于观察几何关系：

```text
cos(x, y) = (x dot y) / (||x|| * ||y||)
```

但不能把距离近当作语义的完整定义。几何由训练数据、目标、模型架构和参数化共同塑造；不同 checkpoint 的坐标系不能直接逐维比较，token embedding 的近邻也不必等同于人类定义的同义词。

更重要的是，模型不直接在初始 embedding 上完成大部分任务。后续 layers 会不断读取上下文并改写 hidden states。

## 初始表示不等于上下文表示

同一个 token id 的 lookup 结果固定，但自然语言含义依赖上下文。一个多义词出现在不同句子里，初始 embedding 相同，经过 Self Attention 与 MLP 后的 hidden state 可以不同。

需要区分：

```text
token embedding        id 对应的可训练初始向量
position representation 顺序或相对位置信息
hidden representation 经过上下文计算形成的动态状态
sentence embedding     为句子或文档任务构造的整体表示
```

它们都使用向量，却有不同粒度、训练目标和接口。把 token embedding 与 RAG 使用的 sentence embedding 混为一谈，会把模型内部状态与检索索引错误地归到同一层。检索 encoder 的升级兼容与低精度质量验收由 [Ch76 RAG](../part-07-agent/76-rag.md) 承担；本章只拥有模型输入表示及其训练接口。



## 参数量与 Tokenizer 的联动

Embedding table 参数量为：

```text
P_embedding = V * d_model
```

若每个参数占 `b` bytes，权重存储约为：

```text
M_embedding = V * d_model * b bytes
```

所以 Tokenizer 和 Embedding 不是互不相关的两章。更大词表可能缩短 token sequence，却扩大 embedding 和输出 vocabulary projection；更小词表降低表参数，却可能增大 `T`，进而增加 Attention 与 KV Cache 压力。

Embedding lookup 自身的 FLOPs 通常不高，但 table 可能较大，并且访问模式由 token ids 决定。仅就输入 lookup 路径而言，梯度支持落在本次访问的 rows；用 sparse 还是 dense tensor 表示梯度、如何通信，则取决于实现与分布式策略。共享输出矩阵的情况还须计入后文的输出侧梯度，不能从数学 lookup 直接推断整张参数表的更新范围。

## 输入与输出权重是否共享

Decoder-only 模型最终要把 hidden state 投影回 `V` 个 logits：

```text
h_t        [d_model]
W_out      [d_model, V]
logits_t   [V]
```

某些模型令 `W_out = E^T`，即 input embedding 与 output projection weight tying。这样可以减少参数，并把输入、输出词表空间联系起来。

Weight tying 是架构选择，不是 Embedding 的定义。不同模型可能使用独立矩阵、额外 normalization 或不同 bias。加载 checkpoint 时必须以模型配置和权重布局为准。

## Padding 与梯度边界

Batch 中不同长度序列通常需要 padding。PAD token 也有 id 和 embedding row，但后续 Attention mask 应阻止真实 token 读取无效 padding，loss mask 也应排除 padding target。

仅把 PAD embedding 初始化为零不能替代 mask，因为后续 bias、position 和 residual 仍可能产生非零状态。输入 padding、causal mask 与 loss masking 是三个相关但不同的约束。

## 当输入接口成为容量瓶颈

到这里，普通 Embedding 已经是一份完整的输入接口：每个 id 对应一行参数，训练改变这些参数，后续网络把它们变成上下文表示。只要词表规模、训练支持和表示预算合适，这个简单方案就足够合理，没有必要为了增加结构而替换它。

但“表里有这一行”与“这一行形成了足够可用的表示”并不是同一件事。接下来分别追问四个问题：每行需要多宽？稀有符号究竟得到什么训练信号？符号身份是否还需要在深层直接可读？局部组合的容量应放在计算网络里，还是另设词法表？这些选择可能组合使用，却不是前一个方案失败、后一个方案必然取代它的升级序列。

### Embedding Width 与 Residual Width 不必相等

上面的主线令 embedding width 直接等于 `d_model`，因为 lookup 结果可以立即进入 residual stream：

```text
input_ids [B,T]
-> E [V,d_model]
-> X [B,T,d_model]
```

这是一种简单而常见的接口，却不是数学上的强制条件。模型也可以使用较窄的 `d_embed`，再用学习到的 projection 进入 `d_model`：

```text
E          [V,d_embed]
lookup     [B,T,d_embed]
P          [d_embed,d_model]
X = E[id]P [B,T,d_model]
```

真正必须对齐的是进入 Transformer residual stream 之后的宽度，因为 Attention 输出、MLP 回投影和 residual add 都要回到同一个 `d_model`；`d_embed` 只需通过明确 projection 满足这份输入契约，也不需要等于 MLP 内部的 `d_ff`。

当词表很大时，因式分解把输入侧参数从 `V * d_model` 改为 `V * d_embed + d_embed * d_model`，用更小的词表接口换取额外投影和表示瓶颈。

这里要分清坐标数增加与信息恢复。对行向量 `e`，若 `d_embed < d_model` 且 `P` 满行秩，即 `rank(P) = d_embed`，则在精确算术下存在右逆 `R [d_model,d_embed]`，使 `PR = I`、`(eP)R = e`。升维可以保留原向量的全部信息，但输出仍只沿至多 `d_embed` 个独立线性方向变化；学习到的 `P` 并不自动满秩，极小的非零奇异值也可能使恢复对浮点误差敏感。

反过来，宽向量经过固定线性降维后，一般无法再靠升维还原。下面两张矩阵只说明这条信息边界，不代表模型实际学习的投影：

```text
P = [[1,0,1], [0,1,1]]       shape [2,3]
U = [[1,0], [0,1], [0,0]]    shape [3,2]

[a,b] P       = [a,b,a+b]
[a,b,c] U P   = [a,b,a+b]
P U           = I_2
```

窄向量经 `P` 升维，再经 `U` 可以恢复；任意宽向量先经 `U` 降维则丢掉了 `c`，只有输入本来满足 `c=a+b` 时才能恢复。类似地，若一个宽权重矩阵 `W` 恰好满足 `W=UP`，两步计算 `xUP` 与 `xW` 等价；中间宽度为 `r` 的精确分解要求 `rank(W) <= r`。超过这个秩只能近似，恢复相同 shape 不等于恢复原运算。

Factorized embedding 通常从训练开始共同学习 `E`、`P` 和后续网络，并没有一张必须无损恢复的原始宽表；但有效输入表 `EP` 的秩仍不超过 `d_embed`。后续非线性与上下文计算可以形成更丰富的状态，却不能据此保证入口容量限制不影响任务。它也改变 output head 的共享方式：若 `d_embed = d_model`，可以直接令 `W_out = E^T`；若二者不同，hidden state 必须先通过另一个投影进入 `d_embed` 才能复用 `E^T`，或者保留独立的 output matrix。输出路径的目标是保留预测所需信号，而非还原任意 hidden state；即使共享输入投影的转置，也不自动构成逆映射。

[ALBERT 的 §3.1 与 §4.4](https://arxiv.org/html/1909.11942v6)提供因式分解设计与宽度对照实验，支持这是一条可行分支，没有证明普遍无损。验收应固定 tokenizer、数据与可比较的训练预算，同时比较 held-out loss、任务质量及稀有符号／语言切片，并把允许的退化范围与参数、显存、吞吐收益一起规定；压缩已有表时，重构误差只是额外诊断，不能代替行为测试。质量收益不足时保留较宽接口，checkpoint layout 与 weight-tying contract 也应随架构选择一起冻结。

### 共享矩阵中的稀有符号：先检查训练支持

压缩宽度解决的是参数预算，却没有回答一行参数有没有得到合适的训练。普通 lookup 为每个 token 保留独立的行，能避免不同符号被接口强制合并；但沿输入路径，一个符号出现得越少，就越少有机会通过具体上下文学习如何被使用。若输入、输出共享矩阵，还必须检查第二条梯度路径。

为什么一个 token 从未作为正确答案出现，输出侧仍会更新它？考虑没有额外 bias、直接共享 `E` 的输出头。用 `h` 表示一个预测位置的 hidden vector，`y` 表示正确 token，`e_j = E[j]` 表示第 `j` 行，则：

```text
z_j = h dot e_j
p_j = exp(z_j) / sum_k exp(z_k)
L   = -log(p_y)

output-side gradient:
∂L/∂e_j = (p_j - 1[j=y]) h
```

这里 `1[j=y]` 是指示函数，相等时为 1，否则为 0；公式只计算经过输出头的梯度贡献，把 `h` 在这条局部路径上视为给定。共享参数还要加上输入路径经过 `h` 回传的贡献。对本次并非正确答案的 token，输出侧梯度为 `p_j h`，通常并不为零：softmax 的分母包含它，训练不仅提高正确答案的相对分数，也调整其他候选。

因此，“没有输入 lookup 更新”“没有作为 label 的正向监督”和“参数完全没有更新”是三件不同的事。对训练中未见的输出类别，缺少正向监督，却仍承受输出归一化与正则化的影响。在特征有界、GD/SGD 步长足够小，且 weight decay 相对未见类概率足够强等条件下，不同未见输出行可能趋近。若输入侧共用这些行，新符号除了难以生成，也可能因初始表示过于相似而难以区分；这是特定训练条件下的风险，不是 weight tying 必然破坏符号区分的结论。<!-- source-family:SF-2026-ARXIV-2604-21632 -->

针对这种风险，干预必须对应具体缺口。增加训练中的符号多样性是在补监督支持；冻结或周期性重置部分行是在改变参数更新；增加 copy head 则是在改善从上下文到输出的读出。能把一个符号复制出来，不等于输入表示已能区分它与另一个符号，所以 copy 路径不能自动替代输入侧修复。

受限逻辑模型及 Gemma unused-row 实验支持这一风险，但也暴露干预成本：冻结行会损害 C4 loss，行的 cosine 相似也不足以单独证明推理失败。来源中未限定学习率的收缩 Lemma 缺少小步长前提，GD 条件更不能直接担保 AdamW。实际新增符号时，应先核初始化、输入出现频率与输出监督，再同时测符号区分和原语言质量，选择必要的局部干预，而非永久冻结整张表。<!-- source-family:SF-2026-ARXIV-2604-21632 -->

### 一次输入注入不足时，按层保留符号身份

补足训练支持之后，还存在另一个独立问题：符号的身份信息以什么方式到达深层？标准 Transformer 通常只在入口按 id 查表，之后传递的是不断被上下文改写的 hidden state。这样做简单，也不意味着身份信息必然被丢失；后续网络可以保留所需差异。只有当稀有符号的表示不足，或不同符号在相似上下文中变得难以区分时，才有理由增加一条可直接读取原始 id 的路径。

这条路径不负责替模型理解上下文，而是让每层仍能读取“当前是哪一个符号”。一种实现是为同一 token 建立 `K` 张独立的可训练记忆表，称为 memory banks。每个 bank 按 id 读出并归一化向量；这些与上下文无关的向量在一次 forward 中计算一次，供各层复用。与普通 Embedding 相比，改变的是符号身份的可访问位置，而不只是把入口向量加宽。

然而，每层都同样强地加入身份向量，也可能妨碍有益的上下文化。因此，每层用当前 hidden state 计算 bank 的混合权重，称为 router；各层使用自己的路由参数，构成 depth-conditioned routing。另设一个向量恒为零的 null bank，让网络能选择少注入，而非被迫使用全部记忆。若 `M_k(i)` 是第 `k` 个 bank 对 token `i` 的读出，`α_{ℓ,k}` 是第 `ℓ` 层在该位置的 softmax 权重，其混合关系可写成：

```text
M_(K+1)(i) = 0                     # null bank
sum_(k=1..K+1) α_(ℓ,k) = 1
m_ℓ(i) = sum_(k=1..K+1) α_(ℓ,k) M_k(i)
```

`m_ℓ(i)` 与该层 residual stream 以兼容的向量宽度相加。bank 的读出由 token identity 决定，但混合权重依赖当前上下文；这区分了“记住符号”与“本层怎样使用符号”。完整的层计算在 [Ch17 Transformer Layer](17-transformer-layer.md)展开，本章只解释新增的身份表示路径。

EmbeddingMemory 的受限案例给出了理论动机和多个语言模型及下游实验，但不能证明所有 rare-token failure 都来自单次注入，也未证明大规模 serving 下的内存或吞吐收益。独立表增加参数，逐层混合增加路由计算，复用读出仍有缓存成本；注入过强也可能压制有用的上下文差异。只有增量收益和路由稳定性均得到验证，才值得保留该路径；否则一次性 embedding 仍是更简单的基线。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-06216 -->

### 从 Token Row 到 Hashed N-gram Capacity

逐层读取单个符号的身份，并不等于直接表示多个符号的组合。普通 lookup 给每个 token 一个初始向量，组合关系交给后续网络计算；这避免了为大量组合另存参数，在内存受限时尤其合理。但如果常见局部组合占用了很多学习与计算预算，就可以追问：是否应为这些组合另外保留可查表的容量？

`n-gram` 是连续 `n` 个 token 的局部组合。以序列 `A B C` 为例，在 `C` 所在位置可以读取以它结尾的 `B C`、`A B C`；自回归路径只使用当前及过去 token，不能提前读取未来。组合数量很大，逐项建立独立词表代价高，因此可以用 hash 将组合映射到有限表的行，用多路 hashed lookup 读出并聚合，再与 token embedding 一起进入上下文网络：

```text
token ids
→ overlapping n-grams
→ multiple hashes and table lookups
→ aggregate with token embedding
→ contextual layers
```

这种 lexical memory 以较低计算量读取局部模式，但有限 hash 表面临碰撞：不同组合可能共享行，相互干扰更新。多路 hash 能提供不同的读出路径，却不保证完全消除碰撞。表变大后，还要面对分片、热点行访问不均、checkpoint 布局和推理缓存身份；table 与 hash 映射变化后，同名 token 序列的表示也可能变化，不能忽略缓存所依赖的模型资产版本。

所以参数容量与计算容量必须一起分配：向词法表倾斜过多预算，会挤压用于上下文计算的专家或网络深度。收益取决于这些预算之间的联合取舍，单一模型族的 scaling curve 不能外推成通用参数分配定律。[Ch21 MoE](21-moe.md)把另一部分容量分配给按需执行的专家；这里的查表分支与它是可比较、可组合的选择，不是它的必然后继。小词表、内存受限或 lexical shortcut 风险较高时，普通 token embedding 仍更清楚：模型应学会依上下文使用局部模式，而不是只凭熟悉的词串作答。

扩大词法容量之后，前一节的训练支持问题又以另一种形式出现：新增行究竟被访问、更新了多少次？如果大部分数据集中在少数高频 token，均匀扩表可能只是增加大量接近初始化的冷行。一条数据感知分支为高频 token 保留专用槽，再按经过平滑的频率质量，将尾部 token 分到更新压力较均衡的桶中。稀疏桶可以直接分配行，并利用空余行作为附加的 alias 读出；拥挤桶则通过多路 hash 聚合，分散碰撞干扰。这里均衡的是访问与更新压力，不是保证不同概念已获得独立语义。

这条分支与直接 hash 固定 n-gram 也有区别：它先按 token 查表，再让带门控的局部 causal 卷积与非线性提取器读取相邻表示，形成随局部内容变化的组合特征。查表仍不依赖上下文，提取器却会依局部内容决定哪些信号应保留；因此一次 hash 命中本身不是成熟语义。不同提取器和 gate 的作用还需验证，不能仅凭访问频率更平均便认定表示不再冗余。<!-- source-family:SF-2026-ARXIV-2604-21724 -->

最后还要决定把组合特征交给谁使用：注入 Attention 的 value 路径，是增加供上下文读取的内容；注入层间 residual，是改变下一层接收的状态。value 注入可以保留当层已计算的 Query/Key（匹配向量），但当层输出及后续表示仍会变化，不能据此声称不增加计算。[Ch14 Self Attention](14-self-attention.md)解释匹配与内容读出的区别，[Ch17 Transformer Layer](17-transformer-layer.md)解释 residual 的组合，本章保留词法表、提取器与注入位置之间的设计关系。

共享表与预取也仍要支付参数、host/device 搬运和缓存成本。受限模型与内存配置中，2× 容量可优于 4×，而层位消融又与参数量混杂；这些结果既不证明扩容单调改善，也不证明零 FLOPs。采用该动态分支时，应把 table、hash、提取器、gate 和层位共同验收，并同时检查更新覆盖、碰撞与任务质量，不把带宽估算当作线上延迟保证。预算紧或词法捷径风险高时，静态 lookup 仍应保留为对照。<!-- source-family:SF-2026-ARXIV-2604-21724 -->

## 表示几何怎样诊断，不能证明什么

前面的分支改变了宽度、训练支持、身份路径或词法容量，最后都要回答同一个验收问题：表示是否更有用？参数量和 tensor shape 只能说明存了多少数，余弦近邻只能说明某种距离下谁更接近，都不能直接证明任务能力。几何诊断的价值在于定位可能的问题，再设计实验，而不是用一条曲线代替质量验收。

### 先分清向量宽度、维度读数与任务能力

`d_model` 是每行存储的坐标数；“内在维度”则试图描述点集或分布局部变化需要多少维。一个平面可以放在三维坐标里，坐标数与平面的维度并不相同。但模型的表示分布不是一个已知平面，只能从有限样本估计，而且必须先说明估计的数学对象。

因此还要进一步分清三件事：估计器在有限样本上的**读数**，对某个测度或支持集所定义的**数学维度**，以及模型在任务中的**可用能力**。测度描述概率质量如何分布，支持集描述分布可能出现的位置；它们的维度定义也不能任意互换。维度读数可以提出容量假设，却没有直接给出任务能力或可删除的参数数目。

### 为什么最近邻读数会受少数行支配

一类估计器只比较每个向量到最近两个邻居的距离。记这两个距离为 `r_1`、`r_2`，且 `r_2 >= r_1`；在相应采样假设下，距离比 `r_2/r_1` 的分布被用来推算维度。对这类读数而言，许多比值接近 1 可能被解释为较高维度，而不是“邻居几乎一样远，所以表示一定简单”。

问题在于，比值接近 1 还可能来自另一种几何：少数行的向量范数很短，成为大量其他行共同的最近邻，这样的公共邻居称为 hub。许多向量到这些 hub 的距离相近，便可能抬高维度读数。这解释的是估计器对样本几何的敏感性，不是模型真的增加了有效容量。

可以在分析副本上比较等量随机裁剪与短范数裁剪，再把裁掉的行加回，或改变归一化后重新测量，检查读数是否受 hub 支配。这些操作不等于从部署模型中删除 token；裁剪后的较低读数也不是“真实维度”或容量冗余的证明。保留原始表保证部署对象不变，改变分析样本或距离则帮助定位测量敏感性，二者回答不同问题。

### 层间曲线也不能替代能力证明

同样地，即使逐层估计曲线先升后降，也不能仅凭曲线断言表示自由度先增长再收缩；邻居距离、采样分布和度量一变，读数就可能改变。这里还有一个有用的数学边界：pointwise dimension 描述某点附近的概率质量随观察半径缩小而如何变化，回答的是分布的局部结构，而不是预测任务能解决多少种问题。

对满足相应条件的固定映射，可以用 Lipschitz 条件约束这种局部维度。Lipschitz 的含义是输出距离至多为输入距离的某个固定倍数，不能把任意小的输入差异放大为任意大的输出差异。将输入分布经过这样的映射得到输出分布时，在相关测度与映射条件下，适当定义的 pointwise 维度不增；经验估计曲线却未必跟踪这个数学量。不能据此给所有 Attention、离散路由或任意支持集套用同一个定理。有限词表、有限长度 token 序列形成的离散支持，在经典维度定义下甚至可以为零，这也不意味着其上下文表示没有丰富的任务能力。<!-- semantic-body-binding:SF-2026-ARXIV-2604-20276 -->

因此，一次有意义的几何诊断需要说明分析的是输入表还是某层 hidden state、如何采样、采用什么距离和估计器，以及究竟声称哪个对象改变了。较便宜的曲线可以帮助定位变化，最后仍须用符号区分、语言质量或相应下游任务验证设计判断，不能独自充当架构裁剪或发布依据。这也使本节回到章节主线：Embedding 提供可学习坐标，但坐标的几何不是语义与能力本身。

## 本章在知识树中的位置

```text
Tokenizer
-> token ids [B,T]
-> Embedding lookup
-> X [B,T,d_model]
-> Position Encoding
-> Self Attention / MLP
-> contextual hidden states
```

第11章决定离散符号怎样切分，本章决定这些符号如何进入连续优化空间；第13章再提供顺序，第14章开始让表示根据上下文变化。

## 自检问题

1. Token id 为什么不能当作有序标量？
2. Embedding lookup 为什么与 one-hot matrix multiplication 等价？
3. `[B,T]` 如何变成 `[B,T,d_model]`？
4. 小例子中的 lookup 执行了什么，没有执行什么？
5. 为什么余弦相似度不能作为语义的完整定义？
6. Token embedding、hidden representation 和 sentence embedding 有何区别？
7. Vocabulary size 为什么同时影响参数量和序列长度？
8. 为什么 `d_embed` 可以不同于 `d_model`，而 residual stream 的宽度必须统一？升维可恢复已有向量，为什么仍不保证较窄接口没有质量损失？
9. Weight tying 共享了哪两个矩阵？当 `d_embed != d_model` 时还需要什么接口？
10. 为什么零 PAD embedding 不能替代 Attention/loss mask？
11. Embedding 为什么只是上下文计算的入口？
12. 未见 label 的行为什么仍会得到输出侧梯度？为什么这不等于获得了足够的符号监督？
13. 逐层身份记忆与局部词法容量分别解决什么问题，为什么二者都不是上下文化的替代品？
14. 几何估计读数改变时，怎样区分模型改变与测量方法改变？

## 小结

Embedding 把无序类别 id 映射为可学习的连续坐标。Lookup 与 one-hot 乘法等价，但前者避免物化巨大稀疏向量。训练目标逐步塑造向量几何，而后续 Transformer 才把固定初始坐标改写成上下文表示。

这一层也建立了第一个稳定 tensor contract：token ids 最终必须变成 `[B,T,d_model]` 才能进入 residual stream。常见实现让 lookup 直接产生该宽度，factorized embedding 则先得到 `[B,T,d_embed]` 再显式投影；从这里开始，模型结构与 GPU 上的张量计算正式连接起来。

额外的身份或词法路径是否有用，取决于训练支持、上下文使用方式及参数与执行预算；几何读数只能帮助诊断，不能独自证明收益。无论选择哪条分支，这些表示都还没有解释同一符号位于不同位置时的差别。下一章会在不混淆符号身份与顺序的前提下，引入位置关系。

## Review notes

本轮 Review 保留了已迁移材料中的向量化、余弦相似度和矩阵计算直觉，并补齐 batch shape、小型 lookup、weight tying 与 padding 边界。本章不展开 Position Encoding、Attention 或向量检索。

Primary-source 校验入口：

- `SF-2026-ARXIV-2604-20276`（Experimental / narrow Disputed branch）：[exact-v1](https://arxiv.org/html/2604.20276v1) §2–5/Appendix A–B 与 [独立审阅](../../papers/2026/04/_sources/daily-20260423/V3_APR02_20276_FINITE_INDEPENDENT.md)。正文仅吸收估计读数、测度维度和任务容量的分账；不采用 Appendix B 缺少闭包条件的普遍支持集 Hausdorff 单调表述，也不把作者 LLM 几何观测当作通用发布收益。[非作者实际写后复核](../../papers/2026/04/_sources/daily-20260423/V3_APR20_20276_CH12_WRITE_AFTER_INDEPENDENT.md)通过，未复现实验；[04/23 日期](../../papers/2026/04/_sources/daily-20260423/V3_ROOT_20276_FINITE_EVIDENCE.md)为公告批次与多字段合取的有界推断，不是逐篇公开日志，整日 Gate 仍待核。
- `SF-2026-ARXIV-2604-21724`（Experimental）：[exact-v1](https://arxiv.org/html/2604.21724v1) §4.1–4.5/Algorithm1、§5。采用训练频率感知的 row 分配、局部 extractor 与逐层注入分支；2×/4×、层位参数混杂、host/device 与执行成本保留，不采零成本或普遍单调扩容。apr02 必要 source→实际 owner 复核通过；root 已复核正文与相邻静态 lookup 分支，写后 PASS，未复现实验。
- `SF-2026-ARXIV-2604-21632`（Experimental）：[exact-v1](https://arxiv.org/html/2604.21632v1) §3–6/Appendix A、E。采用未见 label 行仍受 softmax 梯度影响的条件分支，区分输入表示与 copy 读出；无学习率限定的收缩保证、AdamW 外推与冻结行的 C4 代价保留。apr02 必要 source→实际 owner 复核通过；root 已复核正文与相邻 tying 分支，写后 PASS，未复现实验。

- [A Hub of Short Rows Inflates Intrinsic Dimension Estimation, 2608.29702v1](https://arxiv.org/html/2608.29702v1)：§3–7 与 B–D 的邻距、trim/add-back 及估计器控制支持上述测量敏感性；不外推为真实维度、无用 token 或通用宽度冗余。§3 的 top-decile 措辞与后续 shortest-norm 定义不一致，采用后者明确实验定义；GLM 归一化后仍有明显变化，不采用“归一化总能消除效应”的强说法。
- Tomas Mikolov et al., "Efficient Estimation of Word Representations in Vector Space", 2013: https://arxiv.org/abs/1301.3781
- Ofir Press, Lior Wolf, "Using the Output Embedding to Improve Language Models", 2017: https://arxiv.org/abs/1608.05859
- Ashish Vaswani et al., "Attention Is All You Need", 2017: https://arxiv.org/abs/1706.03762
- Zhenzhong Lan et al., "ALBERT: A Lite BERT for Self-supervised Learning of Language Representations", 2019（factorized embedding parameterization）: https://arxiv.org/abs/1909.11942
- Scaling Embeddings in Large Language Models（hashed n-gram capacity；作者 scale/serving contract）:
  https://arxiv.org/abs/2601.21204
- [TIDE: Every Layer Knows the Token Beneath the Context, 2605.06216v1](https://arxiv.org/html/2605.06216v1)：§3.2 的独立 memory banks、逐层 router、null bank 与加性注入支撑 EmbeddingMemory 的机制说明。保留理论动机和受限任务证据，不将多路径直接等同于所有稀有 token 问题已解决，或大规模 serving 成本已验证。
