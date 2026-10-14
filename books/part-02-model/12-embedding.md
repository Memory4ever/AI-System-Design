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

跨 checkpoint 扩展词表时，一种合理初始化是先用共享 token 的 donor rows 表示新增行，再把相同线性系数用于 base rows。这保留了词表身份之间的锚点关系，却没有保留两个模型的全部几何与读出：donor 中对某个内部特征或输出方向的低响应，不推出迁移后的 base 行仍低响应。新增行、共享锚点、迁移算子及 base 的 embedding/output head 因而共同定义组合产物；只验 donor 的近邻或整体任务质量，不能把其行为信任自动传给组合后的模型。

这条边界要求迁移后再验新增 token 的发出行为、原任务回归，以及不同上下文和采样条件，而不是取消旧的 lookup 或所有线性初始化。一个受限攻击实验通过修改 donor artifact 并利用已知 base 几何构造了这种差异；它不证明任意模型对都会受害，也不提供完备防御。后续 fine-tuning 可能抑制异常，额外调整行范数则又改变了被验收的产物。分词和 token-ID 的联合版本交接仍由 [Ch11 Tokenizer](./11-tokenizer.md#vocabulary-adaptation-是-tokenizer-与-checkpoint-的联合迁移) 承担，本章只拥有行几何及其与后续读出的耦合。

当所有新增 token 都从旧词表的同一个均值行开始，它们在初始 lookup 中没有彼此差异；后续 SFT 是否能及时分开，要由监督与实际训练检验，不能预先认定必然不可恢复。随机初始化给出差异，却未必对齐旧语言表示。另一条付费初始化分支先用 paired text 与新 token 序列训练新增 rows、保留冻结骨干，再进入下游适配；输入/输出若 tying，必须按真实共享参数保存同一更新身份，不能一面更新新行一面声称别名 output head 完全冻结。<!-- source-family:SF-2026-ARXIV-2604-02324 -->

[Grounded Token Initialization 的受限对照](https://arxiv.org/html/2604.02324v1)支持这项语言配对接口，但额外 grounding、后续适配预算及原稿配置口径参与收益，不把全部差额归为初始化时点。较丰富的行几何不认证语义正确，部分检索指标仍退步；SID构造、paired监督、embedding阶段训练与下游SFT均计费。监督不可靠、别名/词表身份不一致或质量回归时，保留mean/random/donor初始化与普通适配，联合验新符号区分、发出行为和旧任务，不由谱或近邻读数自签恢复保证。

词表扩展后的model merge也不能把所有行当作同一来源的可平均参数。一条新增speech tokens的有限分支，让embedding与output head的旧词表行取原模型、新speech行取适配stage，再仅对其它同形参数插值；输入行、输出行与token type因此各有来源身份，不能用没有新行的基座去平均新增符号。保旧行仍不等旧函数保持，因为其它层和后续训练会改变读出。[有限stage/merge对照](https://arxiv.org/html/2604.00007v1)恢复部分text/vision能力，却牺牲相对未merge stage的ASR/TTS；共享旧行也平均与全Stage1词表有不同取舍，不授typed-row万能最优。额外stage、merge、重训和回归均计费；行身份、shape或旧新任务不兼容时，保留独立模型、原词表路径与明确的局部适配，不能由保留原embedding行自签零遗忘。<!-- source-family:SF-2026-ARXIV-2604-00007 -->

连续输出目标还会改变这组坐标是否可辨识。Categorical softmax 的分母让正确 token 与其他候选竞争；若改为只回归目标 embedding 的方向、最小化 $1-\cos(E_y,H)$，同时让目标表与预测器一起移动，则把所有非零目标行和所有输出置于同一方向就能得到零 loss。这是 complete collapse，不只是某些方向的 dimensional collapse；训练 loss 低因而不能单独验收符号区分能力。[匹配初始化的有限对照](https://arxiv.org/html/2602.17287v1#S4.SS5)中，random/NMT/regularized-NMT 初始化只要继续训练目标表，未加约束的连续输出都退至BLEU0；冻结目标表或对它加入great-circle sliced dispersion 可以恢复部分区分，但随机初始化下正则分支33.2仍低于冻结表33.9，不证明正则普遍更好。冻结目标限制适配，分散正则则增加投影、排序、采样与权重调参费用，并可能损害其他层的表示；34M WMT19/singleH100/50k步的翻译结果不能外推为语言模型语义真值或量化加速因果。需要共同训练目标时，应同时验收目标可分性与任务质量；退化或预算不足时，保留冻结目标、原categorical输出或已核验的局部正则，不用几何diversity替代语义与下游质量。<!-- source-family:SF-2026-ARXIV-2602-17287 -->

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



### 固定模型也可以接收经过训练的连续输入

用文本传递辅助知识，优点是可直接检查、无需进入模型内部接口；代价是背景越长越占用输入预算。当 base 参数必须保持冻结而又允许 input embedding 接口时，一条受限分支让独立 expert 先自回归生成背景，读取最后 token 的 late hidden state，再用单独训练的 projector 对齐到 base 的 embedding 空间，替换 prompt 中一个固定 anchor slot。[GAG 的输入适配机制](https://arxiv.org/html/2601.08209v1)先适配 expert，再冻结 expert/base、只训练 projector；它不是把任意向量直接塞进词表，也不是检索 encoder 升级或 base 的循环推理状态。作者在关闭路由、固定领域的消融中，以倒数第四层 `L₂−4` 读出优于更早层及省去适配阶段的变体；这只支持局部接口资格，不证明通用隐藏层可直接互换。<!-- source-family:SF-2026-ARXIV-2601-08209 -->

这里的“一 token”只限制 base 输入带宽，不免除 expert 生成、模块适配与路由开销，也不能保留文本证据的逐句可追溯性。原型最近邻可以在 general peer 与 domain module 之间选择，但 argmax 不是 OOD abstention，增加新原型还可能重划旧路由区域；选择激活的结果不能全归因于连续表示。单一领域假设、数字/单位压缩、跨领域组合和接口分布漂移仍需独立测试。若需要精确引用、内部输入接口不可得或适配/路由未验，文本背景与检索证据仍是合理退路；冻结 base 参数不等于整个系统行为不变。

连续输入还可以承载经 client encoder 编码的整段 prompt，而不只是一份 expert 的单 token 摘要：把 token hidden states 按连续 k 个位置求均值，降低传输序列长度，再由 server projector 对齐到 decoder 的 embedding 空间，作为多 token prefix。此时文本 token ids 与检索用 sentence embedding 都不是 server 的直接输入；encoder、pooling 粒度和 projector 共同定义一份需要训练的接口。一个受限分支先联合适配 encoder、projector 与 server LoRA，再冻结 client encoder，只让 server 在扰动后的表示分布上适配 projector/LoRA；冻结 client 不等于 server 可直接消费任意版本的表示。<!-- source-family:SF-2026-ARXIV-2604-06831 -->

Pool 会丢失局部顺序和细节，扰动又改变 server 的输入分布，因此带宽减少与任务效用必须联合验收。[PPFT 的必要接口与有限对照](https://arxiv.org/html/2604.06831v1#S3)只支持所测 encoder/decoder 和 QA 人口下的适配分支，未传原始 prompt 不等于没有语义、输出或 label 泄漏；server 仍接收可能敏感的明文 target label，局部 inversion attacker 的重构分数也不是完整隐私保证。Client 编码、两阶段训练、pool/projector 与完整 decoder 都付费，降序列长度不是端到端等比例加速。表示版本、精确数字/单位、噪声分布或效用不合格时，保留已验收的原文本/连续输入接口与更小压缩，并由安全 owner 独立决定跨信任边界的暴露资格。

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

独立输出头还会留下一个容易误读的坐标自由度。固定产生 hidden vector 的整个函数 `h=f(x)`，令输出类别向量为 `e_i`、logit 为 `h·e_i`；给所有类别共同加同一个向量 `v`，新 logits 只多出所有类别相同的 `h·v`，softmax 的分子、分母同时乘相同因子，因而每个输入的预测分布完全不变。这个等价类只改独立输出头，不改输入表和 `f`；如果头与输入 tying 后一起平移，`f` 也可能改变，不能直接沿用证明。额外 normalization 或非 softmax 读出也须另核，不能把它搬到任意表示或相似度模型。

保持预测不变，却不一定保持类别向量的 cosine。对不同向量 `a≠b`，共同平移 `v=−(a+b)/2` 后两者为相反的非零向量，cosine 是 `−1`；选择 `v=−a+(b−a)/2` 后两者为同向非零向量，cosine 是 `+1`。[精确输出头反例](https://arxiv.org/html/2603.29488v1)因此排除了不说明参数化便把 cosine 当作预测概率或语义关系的普遍保证，而没有证明某个固定 checkpoint 的所有 cosine 统计都无用。解释时应明确测的是输入还是输出、头是否独立及坐标约定，并用预测概率、任务行为或受控干预验证；这些诊断仍有采样/评价成本，也不替代原来的 lookup、共享权重或已验收模型。<!-- source-family:SF-2026-ARXIV-2603-29488 -->

普通转置共享适合参数预算优先的路径；若还要求线性 hidden→logits→embedding 的往返恢复，可将输入表与输出头耦合为下面的左逆构造，其中 `Z [V,d]` 列正交，`T [d,d]` 可逆，作者以 SPD 参数化学习 T：

```text
E = Z T^(-1), W_out = T Z^T, Z^T Z = I_d
W_out E = I_d, E W_out = Z Z^T != I_V  (d < V)
```

这只约束线性接口，不使 softmax、token 选择或语义成为逆运算；从旧表的 polar factor U 初始化 `Z=U,T=I` 也会改变原 lookup，不是无损 retie。默认冻结 Z、只学习 T 时仍需 FP32 solve、额外 `hT` 计算和 conditioning 验证；训练 Z 则另付正交维护成本，数值 ridge 不保证精确正交。受限 scratch、部分 teacher 与 LoRA 对照仍有质量退步，代数 alignment 达到构造值不是独立质量测量。接口或数值验收失效、额外成本不值得时，保留普通转置共享或独立输出头，不把左逆条件升级为普遍更稳定或更好的语言模型。<!-- source-family:SF-2026-ARXIV-2602-04556 -->

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

较窄的线性表并不是唯一的参数共享方式。如果词表参数挤占了上下文网络的预算，也可以只保留较小的共享 codebooks，再由可训练的非线性函数生成每个 id 的输入向量。一条受限分支把 id 分解成多维离散坐标，按各坐标查共享表、求和得到 seed，再经投影、归一化、sigmoid 和 B-spline 基函数的可分离聚合生成 `d_model` 维表示。它仍输出同一份 residual 输入契约，却不再等价于固定的低秩线性表 `EP`；共享的是生成函数及坐标表，而不是预设 token 的语义邻接。id 的多维排列是任意词表编号的编码，连续插值能力不能证明相邻编号语义相近，也不允许把离散 token 本身当作连续变量。<!-- source-family:SF-2026-ARXIV-2601-22040 -->

这条分支把存储换成了入口计算，必须与普通 lookup 分账。[Leviathan 的受限 scratch 对照](https://arxiv.org/html/2601.22040v1)只覆盖约 60–420M 模型和固定 token 流：同 backbone 对照同时改变输入生成器与输出 tying，不能把收益全归因于输入表示；同参数对照则把省下的预算用于更深的网络，既不同计算量，也不同串行深度。模型仍保留独立的词表输出头，须另计其参数与计算，不能用输入表压缩比例代表整模型压缩。作者报告的训练吞吐下降说明参数更少不等于 lookup 更便宜；硬件未披露，不能据此给线上延迟保证。采用时应同时验 held-out 质量、训练与推理成本、输出头配置及预算重分配，无法承受额外计算或未获局部净收益时，保留较宽 lookup、线性因式分解或原来的 tying 分支。接下来仍要检查这些表示获得了什么训练支持，不能只因生成器共享参数就认定稀有符号已被学会。

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

`n-gram` 是连续 `n` 个 token 的局部组合。以序列 `A B C` 为例，在 `C` 所在位置可以读取以它结尾的 `B C`、`A B C`；自回归路径只使用当前及过去 token，不能提前读取未来。组合数量很大，逐项建立独立词表代价高，因此可以用 hash 将组合映射到有限表的行，用多路 hashed lookup 读出并聚合。但查到局部模式，不等于它适合当前上下文；融合可以发生在输入端，也可以成为指定层的旁路：

```text
token ids
→ overlapping n-grams
→ multiple hashes and table lookups
→ lexical memory vector
→ input fusion or context-gated layer injection
→ contextual computation
```

层内注入需要分开“读哪个地址”与“采用多少内容”。[Engram 的受限架构](https://arxiv.org/html/2601.07372v1#S2)保留普通输入表和输出头，将多路 n-gram 读出拼接为 `e_t`，再以当前层的 `h_t` 门控。以下使用列向量，`d_mem` 是读出宽度，`d_model` 是 residual 宽度，`W_K/W_V` 将前者投影到后者；论文的单分支形式为：

```text
k_t = W_K e_t,  v_t = W_V e_t
alpha_t = sigmoid(RMSNorm(h_t)^T RMSNorm(k_t) / sqrt(d_model))
u_t = alpha_t v_t
```

这里的 Query 来自已有上下文，Key/Value 来自词法表；sigmoid 调节该位置读出的强度，不是在全部历史位 置间做 softmax。门控后的序列再经短程、逐通道的因果卷积与非线性，连同 `u_t` 加回同宽 residual，随后继续 Attention/MLP。因而同一词串可命中相同地址，却在不同上下文中产生不同注入；它不是用查表替代指代消解或全局 Attention，也不是读取一条已认证的事实。

地址只依赖已知 token，允许提前准备读出；门控必须等待当前层状态，不能把完整注入也当作静态缓存。投影、门控、卷积和搬运仍有成本，早层注入与隐藏搬运延迟所需的前置计算还可能冲突。门控只学习抑制不合适的信号，不保证消除多义性或碰撞；应分别验查找、上下文使用、质量回归及端到端成本，未获净收益时保留普通 Embedding。层内 residual 组合由 [Ch17](17-transformer-layer.md)承担，本章只拥有词法读出到动态表示的接口。

这种 lexical memory 以较低计算量读取局部模式，但有限 hash 表面临碰撞：不同组合可能共享行，相互干扰更新。多路 hash 能提供不同的读出路径，却不保证完全消除碰撞。表变大后，还要面对分片、热点行访问不均、checkpoint 布局和推理缓存身份；table 与 hash 映射变化后，同名 token 序列的表示也可能变化，不能忽略缓存所依赖的模型资产版本。

所以参数容量与计算容量必须一起分配：向词法表倾斜过多预算，会挤压用于上下文计算的专家或网络深度。收益取决于这些预算之间的联合取舍，单一模型族的 scaling curve 不能外推成通用参数分配定律。[Ch21 MoE](21-moe.md)把另一部分容量分配给按需执行的专家；这里的查表分支与它是可比较、可组合的选择，不是它的必然后继。小词表、内存受限或 lexical shortcut 风险较高时，普通 token embedding 仍更清楚：模型应学会依上下文使用局部模式，而不是只凭熟悉的词串作答。

消除地址碰撞也是一条可比较的分支，而不自动等于提高学习质量。对预先固定的高频 n-gram 集合，可以用最小完美哈希（MPHF）为成员分配互不碰撞的槽，另用 fingerprint 检查输入是否属于该集合；未命中的组合仍回到普通 hash 表。MPHF 的无碰撞保证只属于建表时的成员集合，不能替 fingerprint 证明任意非成员都不会误判。新增的成员判断、冷热分流与表身份也须随模型资产一起维护。

受限的 [EngramNine 对照](https://arxiv.org/html/2601.16531v1)将 500K hash 容量改分为 100K 热槽与 400K 冷槽，在 GPT-2 125M backbone、FineWeb-Edu 100M-token 数据集、约 82M 训练 token、两次 seed 与 A100 40GB 的条件下，最终 validation loss 接近，吞吐却下降约 11–12%。这说明更明确的地址隔离可能付出执行成本，而未在该条件下获得可分辨的质量收益；但容量重分配同时变化，不能把全部差异只归因于碰撞。冷热 gate 及 loss 轨迹的关联也没有证明碰撞是有益 regularizer，或无碰撞必然导致因果性的路由固化。应把成员查找正确性、参数分配、学习结果与运行成本分账，保留普通 hash 基线，不外推为大规模 MoE 或所有语料上的结论。<!-- source-family:SF-2026-ARXIV-2601-16531 -->

已有词法容量还可成为受限编辑接口，但改一个问法命中的行不等改好了同一事实：不同表达触发不同 n-gram，同一个 n-gram 又可能被多表达复用。可以先冻结 decoder，为多表达求共同的 memory-representation 目标，再把表达到真实 n-gram 的共享关系写成联合匹配问题，以长度/频率的复用惩罚分配更新。[受限编辑对照](https://arxiv.org/html/2610.10533v1)采用精确 token 序列索引的累计更新 overlay，激活时加到读出，原 hashed tables 保持固定；这避免新增编辑被地址碰撞耦合，不消除相同 n-gram 的语义复用或全网络输出影响。线性解属于所用加性聚合，门控或上游依赖变化须重建优化关系；原问法命中、跨表达迁移、未改知识保留和任务质量分别验收，部分指标仍退步，post-edit 准确率也可能用新纠正掩盖旧正确丢失。表达制备、反传求目标、共享系统求解、频率统计与随编辑增长的 overlay 均计费，decoder 冻结不等免费或正确事实已获认证；覆盖、保留或成本不合格时保留普通查表与已有知识更新路径，不由编辑成功给任意关联问法签字。<!-- source-family:SF-2026-ARXIV-2610-10533 -->

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

- `SF-2026-ARXIV-2604-02324` — Daily2026-04-04补Apr3；[GTI exact-v1](https://arxiv.org/html/2604.02324v1)必要§2–4.3/6/7.2–7.4，2+1+2=5，newrows paired语言grounding具体差额深入。保tie别名/额外stage预算与公共指标反退，原main/A配方不齐不作复现recipe或纯init因果，geometry不授语义。supp_apr04_reader actualSource/Ch12逐字PRE通过，root授两body/本人note窄锁，作者实写顺读；supp_apr04_reader已实际新增两body/完整局部邻接及本人note nonwriterPOST通过，作者同步实读，窄锁释放；未核代码/复现。

- 对话增量审计（2026-10-10）：[Engram exact-v1](https://arxiv.org/html/2601.07372v1) §2.1–2.5/Eq1–6 支持确定性读出、上下文门控和指定层 residual 注入；正文采用单分支解释，不展开 mHC。回对[官方演示代码](https://github.com/deepseek-ai/Engram/blob/main/engram_demo_v1.py)时注意其 gate 另有 signed-square-root 变换，且 Attention/MoE 为 mock，不当作论文公式逐项等价或生产实现。未运行代码、复现实验或确认任何闭源产品采用；性能数字与通用收益未纳入正文。

- `SF-2026-ARXIV-2601-16531` — Daily `2026-01-27` 增量；[exact-v1](https://arxiv.org/html/2601.16531v1) §3–5/Table3/limitations（本日必要原件 blocks25–134、160–165）。2+2+2=6，针对查找无碰撞与学习质量/运行成本分账的具体缺口深入；只采用静态 MPHF+fingerprint 热集合与 hash 冷回退、受限等参数近似 loss/吞吐对照。容量重分混杂、两 seed、fingerprint 非成员误判及 gate 关联非因果保留，不采用有益 regularizer 或普遍路由固化。root 实际 source/PRE、两段正文/完整邻接及末注 POST 通过；按其复核纠正数据集 100M 与实际约 82M 训练 token 的配置区分。未核实现或复现实验。

- `SF-2026-ARXIV-2601-22040` — Daily `2026-01-31`；[exact-v1](https://arxiv.org/html/2601.22040v1) §3–4.5/§6，2+1+2=5，针对非线性共享 id→输入表示接口缺口深入。仅采用共享坐标/codebooks→生成器与参数/计算分账；iso-body 的 tying 混杂、iso-param 的深度/吞吐代价、任意 id 拓扑及原硬件未披露保留。root 实际必要源及 PRE 窄差额通过，正文、前后及末注经非作者实际 POST 通过（输出头指代已按复核纠正）；未运行代码或复现实验。

本轮 Review 保留了已迁移材料中的向量化、余弦相似度和矩阵计算直觉，并补齐 batch shape、小型 lookup、weight tying 与 padding 边界。本章不展开 Position Encoding、Attention 或向量检索。

Primary-source 校验入口：

- `SF-2026-ARXIV-2601-00065`（Experimental）：[exact-v1](https://arxiv.org/html/2601.00065v1) §3–4.3、§5.1–5.3、Appendix B 支持 donor 系数复用时的组合行为边界。作者五个小模型、20 directed pairs 的 SER 是目标 token 发出率，不是实际 harm；一轮 LoRA 抑制后的恢复还额外修改了行范数，不采用“未经修改仍持续穿透”的说法。迁移后回归是验证方向，非完备防御；[必要证据与采用命题](../../papers/2026/01/_sources/daily-20260106/tokenforge-source-owner-proposal.md) 已经 root 原源、source→owner 及实际写后复核通过，未复现实验。
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

- `SF-2026-ARXIV-2602-04556` — Daily `2026-02-06`；[PIT exact-v1](https://arxiv.org/html/2602.04556v1) §3–5及A.3，2+2+2=6，针对 coupled Z/T left-inverse 接口的具体缺口深入。采用列正交与可逆条件下 W_out E=I_d，不授 E W_out=I_V、softmax/token/语义可逆；teacher 初始化非无损，freeze-Z/可训-T、FP32 solve/额外 hT 和 conditioning 成本保留。不采 Cholesky 对角 clamp 等价 eigenvalue clamp 或 ridge 精确 Stiefel，Table1 scratch/teacher590及LoRA反侧不作普效。jan01_v3 实际必要 source→owner 写前独立核通过，root 授窄锁；实际写后 POST 与日级 Gate 待验，未运行代码或复现实验。

- `SF-2026-ARXIV-2601-08209` — Daily `2026-01-15`；[GAG exact-v1](https://arxiv.org/html/2601.08209v1) §4.1–4.3/Eq5–14、Table3/4 oracle-routing消融、§9限制。2+2+2=6，具体embedding-input gap深入，仅采用frozen-base/projector条件输入接口，不采用science领域优势或near-oracle通用可靠激活。late读出L₂−4非早层；一token只计base带宽，expert AR成本/原型重划路由/单域与数值单位反侧保留。未运行代码或复现；root实际必要源/owner写前通过并授窄锁，作者已核两段实际正文及前后交接，root已实际核正文、前后交接与末注，非作者POST通过；日级Gate未授。

- `SF-2026-ARXIV-2602-17287` — Daily `2026-02-21`；[exact-v1](https://arxiv.org/html/2602.17287v1) §2.1/Eq2–3、§2.3/3/Eq7–9、§4.1–4.2/4.5/Table3与Limitations。2+1+2=5，continuous-output同移目标零loss不可辨识的具体owner缺口深入；区分complete/dimensionalcollapse，冻结与sliced-dispersion有限恢复/反退、其他层损伤及额外费用近文。不采用Gram维度误写、entropy即semantic或量化因果。root必要原源/actual owner PRE通过并授窄锁；作者实际正文/完整邻接及自身末注已顺读，root非作者已实际读取正文、完整邻接及自身末注，POST通过，窄锁释放。未核实现或复现，非日级验收。

- `SF-2026-ARXIV-2610-10533` — Daily `2026-10-09`；[EngramEdit exact-v1](https://arxiv.org/html/2610.10533v1) §2–4/6及A.3/B.2/B.4必要范围，2+1+2=5；多表达共享ngram联合更新/精确sequence overlay差额深入，加性/gated边界、保留反退/人口与全费近文。review_mar11_continue非作者必要Source/actual Ch12 owner/逐字PRE通过，root授本段与本注窄锁；作者实际写后完整邻接和本注已顺读，root非writer实际288–315完整邻接、新298及本人403注actualPOST通过，锁释放。未核全证明、像素、代码或复现，不授DAY。

- `SF-2026-ARXIV-2603-29488` — Daily `2026-04-02`补`04-01`；[exact-v1](https://arxiv.org/html/2603.29488v1) §2/common-shift proof、§3–4 反例与界限，`3+1+3=7`。只采用 fixed `f`/独立输出头的 softmax 等价类与 distinct 非零 pair 的 cosine ±1 构造，不授输入表/tying/CLIP 通用不变性、所有固定参数统计无用或概率-语义保证。单位向量 toy 与符号错误不采用，v2 sigmoid 扩展不回填；未核代码或复现实验。

- `SF-2026-ARXIV-2604-00007` — Daily2026-04-03；[exact-v1](https://arxiv.org/html/2604.00007v1)§3.1/4.2/7.1/Table9及必要Table11，2+2+2=6，仅expanded-vocab old/new embedding/head rows与同形参数merge来源分责；保Stage1/shared-row反侧、ASR/TTS退步与全部stage费用，不授零遗忘或全模态最优，未核实现/复现。

- [PPFT exact-v1](https://arxiv.org/pdf/2604.06831v1) p3–4/§3.1–3.4及§4.1–4.3；深入，仅采用 pooled continuous prefix 及两阶段参数/消费兼容边界，不采完整隐私保证或全费加速；必要证据、逐字正文与实际写后独立复核通过，未核代码或复现。<!-- source-family:SF-2026-ARXIV-2604-06831 -->
