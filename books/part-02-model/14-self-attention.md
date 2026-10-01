# 第14章 Self Attention

**Knowledge Tree:** Part II 模型：一个 Token 如何变成答案
**Stable Knowledge Node ID:** `MODEL-SELF-ATTENTION`
**Legacy Chapter:** Ch14
**Status:** Draft

**Roadmap Intent:** 每个 token 如何根据上下文重新理解自己。

## 本章要回答的问题

Embedding 与 Position Encoding 已经让每个位置拥有向量和顺序，但 token 之间仍未交换信息。怎样让每个 token 根据当前内容决定读取谁、读取多少？Query、Key、Value、`sqrt(d_h)` 与 causal mask 分别解决什么问题？

本章的核心判断是：**Self Attention 是 content-dependent routing。**每个位置用 Query 描述自己在寻找什么，用 Key 描述自己可怎样被匹配，用 Value 提供真正被聚合的内容。

本章先完整推导单个 head。多个 head 如何拆分、组合以及 MHA/GQA/MQA 的区别属于第15章。

本章使用 `B` 表示 batch size，`T` 表示 sequence length，`d_model` 表示 hidden dimension，`H` 表示 head 数，`d_h` 表示单个 head dimension。

## 固定信息流为什么不够

如果每个 token 只经过同一个 MLP，计算可以变换单个位置，却不能让位置之间交换信息。若使用固定窗口，远距离信息必须经过很多层；若像 RNN 一样递归，信息路径和训练依赖随序列增长。

我们希望同时满足：

```text
任意位置可以直接读取其他位置
读取关系由输入内容决定
整段序列可以组织成规则矩阵计算
```

一个简单思路是让每个位置与所有位置做相似度，再按相似度加权求和。但“按什么特征匹配”和“匹配后传递什么”未必相同，因此需要分开 Q、K、V。

## Q、K、V 的角色与 shape

设当前层输入 hidden states 为（第一层来自 embedding）：

```text
X shape = [B,T,d_model]
```

单个 attention head 使用三组可学习矩阵：

```text
W_Q [d_model,d_h]
W_K [d_model,d_h]
W_V [d_model,d_h]
```

投影得到：

```text
Q = X W_Q    [B,T,d_h]
K = X W_K    [B,T,d_h]
V = X W_V    [B,T,d_h]
```

第13章的位置机制可以接在不同位置：绝对位置向量可在形成 `X` 时相加，RoPE 则作用于投影后的 Q/K，ALiBi 修改后面的匹配分数。下面先写基础 Attention；使用具体位置机制时，应在其对应位置加入变换，而不是默认所有位置信息都已写入 `X`。

- Query：当前位置正在寻找什么。
- Key：每个位置可按什么特征被匹配。
- Value：位置被读取时实际提供什么信息。

如果匹配和传值强制使用同一表示，模型不能独立控制“路由依据”与“传输内容”。Q/K/V projection 为这两个角色提供不同坐标空间。

## 从匹配分数到缩放

对每个 batch，Query 与转置后的 Key 相乘：

```text
S = Q K^T / sqrt(d_h)

[B,T,d_h] x [B,d_h,T]
-> S [B,T,T]
```

`S[b,i,j]` 表示第 `i` 个位置读取第 `j` 个位置的匹配分数。每一行对应一个 Query，列对应所有 Keys。

为什么除以 `sqrt(d_h)`？若 Q/K 各维近似独立且方差稳定，点积方差会随 `d_h` 增长。未经缩放的分数容易让 softmax 饱和，权重过早接近 one-hot，梯度变小。缩放控制 score 量级，不是为了改变 tensor shape。

## Mask 定义哪些边可以存在

Decoder-only causal attention 不允许位置 `i` 读取未来 `j>i`。可构造 additive mask `M`：

```text
M[i,j] = 0       if j <= i
M[i,j] = -inf    if j > i
```

Padding mask 则阻止读取无效 PAD positions。二者可以组合，但含义不同：causal mask 维护自回归因果顺序，padding mask 排除 batch 对齐产生的空位。

## Softmax 分配权重，Value 完成读取

将 mask 加到 scores，再按最后一维做 softmax：

```text
A = softmax(S + M)    [B,T,T]
```

每一行权重和为 1。最终读取 Value：

```text
Y = A V

[B,T,T] x [B,T,d_h]
-> Y [B,T,d_h]
```

完整单头公式为：

```text
Attention(Q,K,V) = softmax(QK^T / sqrt(d_h) + M) V
```

## 路由权重不等于独立的知识贡献

归一化权重描述的是本次路由，而不是每个位置独立贡献了多少“知识”。即使某个位置权重很小，它的 Value norm 或方向仍可能影响结果；一批位置的作用还可能互相抵消。因此研究“读取需要多少位置”时，必须先说清干预：删除尾部位置但保留原权重，与留下少数位置后重新归一化，不是同一个实验。

设保留集合的原权重和为 `m`，保留/删除部分的加权平均 Value 分别为 `mu_S`、`mu_T`，则原输出是 `m*mu_S+(1-m)*mu_T`。只删除时的输出误差为 `(1-m)*mu_T`；重新归一化后的误差则为 `(1-m)*(mu_T-mu_S)`。小的尾部 mass 只控制系数，Value 尺度和方向仍决定实际误差；下一层非线性和最终任务 loss 还会继续改变影响。用原模型 NLL 的变化定义“retrieval capacity”，测到的是特定干预下保留原行为所需的路由支持，不是模型存储事实的数量。[受限 Attention retrieval 实验](https://arxiv.org/html/2609.37879v1)先计算完整 Attention 再选择位置，因而也不构成稀疏实现的加速证明。真实稀疏执行的质量、选择开销与缓存问题交由第45、49章处理。
<!-- source-family:SF-2026-ARXIV-2609-37879 -->

## 三 token 小例子

取 `B=1`、`T=3`、`d_h=2`，为简化令：

```text
Q = K = [
  [1,0],
  [0,1],
  [1,1]
]

V = [
  [1,0],
  [0,1],
  [1,1]
]
```

未 mask 的 score 为：

```text
QK^T / sqrt(2)
= [
  [0.707, 0.000, 0.707],
  [0.000, 0.707, 0.707],
  [0.707, 0.707, 1.414]
]
```

加入 causal mask 后：

```text
[
  [0.707,  -inf,  -inf],
  [0.000, 0.707,  -inf],
  [0.707, 0.707, 1.414]
]
```

逐行 softmax，近似得到：

```text
A ~= [
  [1.000, 0.000, 0.000],
  [0.330, 0.670, 0.000],
  [0.248, 0.248, 0.503]
]
```

聚合 `V` 后：

```text
Y ~= [
  [1.000, 0.000],
  [0.330, 0.670],
  [0.751, 0.751]
]
```

第一个 token 只能读取自己；第二个 token 可以混合前两个 Value；第三个 token 可以读取全部历史，并更偏向自己的 Value。模型训练会学习 Q/K/V，而不是使用这里手工构造的向量。

## Self Attention 获得了什么

第一，信息路径短。全局 Attention 中任意两个允许连接的位置可以在一层交互。

第二，路由依赖内容。同一个 token 在不同上下文中会形成不同 weights 与输出。

第三，训练可并行。给定完整训练序列时，所有 positions 的 Q/K/V 和 score matrix 可以用批量矩阵运算计算。

这些优势都不是正确理解的保证。模型可能学到脆弱关联，长距离位置也可能获得很小权重。Attention 提供表达与执行结构，不保证优化一定使用它。

## 它付出了什么

对单个 head，score matrix 有 `T*T` 个元素。忽略 projection 后，dense Attention 的核心计算近似为：

```text
score / aggregation compute ~ O(T^2 * d_h)
score state                 ~ O(T^2)
```

当 `T` 增长，Prefill 和训练的成对计算迅速变大。自回归 Decode 又需要不断读取历史 K/V，第19章会解释为什么缓存这些状态。

`O(T^2)` 是算法结构描述，不等于所有实现都会在 HBM 中完整保存 score matrix。执行优化可以改变中间状态与 IO，却不自动改变全局成对交互的 FLOPs。

标准计算链到这里已经闭合。接下来分别检查：短路径能表达什么、归一化怎样分配质量、哪些连接和表示可以改变，以及这些改变如何落到状态与执行上。它们是不同约束下的分支，不是标准 Attention 的连续替代步骤。

## 短信息路径的表达与学习边界

### 全局可见不等于单层能够表达全局函数

一层 Self-Attention 让任意 token 直接交换信息，却不自动拥有任意全局计算能力。对 parity 一类需要组合多个输入的函数，attention heads 只提供交互通道，后处理非线性负责选择和组合；固定 heads 与低度 post-process 同时受限时，“看见全部 token”仍不足以表达目标。增加 heads、非线性度数或层数可以绕开下界，却增加参数、计算和优化难度；需要算法式状态时，显式 recurrence 或多层 composition 仍是更自然的旧路径。exact-v1 的理论只给出单层构造的必要增长率，不是 Transformer 的普遍能力上限，也不证明理论可表达结构一定可训练。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-12171 -->

### Attention 也可以先构造特征，再由后层完成在线求解

把 Attention 只理解为“从已有 token 中复制信息”，会漏掉一种构造性能力：若 heads 按特定方式聚合上下文，它们可以先生成 polynomial 或 spline feature，后续层再在这些 feature 上近似执行 least-squares。此时 Attention 拥有的是输入相关的 featurizer 角色，求解器由后续组合层承担；这解释了 nonlinear regression 的 in-context learning 如何可能出现，而不是声称真实预训练 LLM 必然执行了该算法。<!-- source-family:SF-2026-ARXIV-2605-05176 -->

这条存在性路径依赖 polynomial/spline approximability、特定 sum-based heads 与合成 regression，数值实验也只有三组 seeds。它没有观测到通用模型内部的唯一机制，更不能把拟合成功等同于因果识别。任务近线性、context 很短或显式 solver 更可靠时，普通线性读取或外部求解仍更合适；第 17 章将继续解释非线性与多层组合怎样把这些 feature 变成更丰富的函数。

### 可解码不等于单点拥有因果控制权

线性 probe 能从某个 token position 的 hidden state 解码出 task identity，只能说明该位置含有与任务相关的可读信息，不能证明这个位置独自存储了 in-context learning 的 task template，更不能证明替换这一处 state 就足以改变输出。Attention 本来就会让信息跨位置流动，后续 residual 路径又会跨层组合这些结果；因此 task state 可能是跨 demo-output positions、跨层共同承载的分布式对象。<!-- source-family:SF-2026-ARXIV-2605-04061 --><!-- semantic-body-binding:SF-2026-ARXIV-2605-04061 -->

诊断应从相关性逐级升级为因果检验：先用 probe 定位可解码 state，再比较单位置 activation transplant、多位置 transplant 与受控 causal tracing，分别检查局部可读性、必要性和充分性。多位置干预提高了因果辨识力，却扩大实验矩阵，也可能因整段 activation transplant 把 state 推离模型原有分布；证据不足时，probe 只应充当发现工具，最终判断仍回到端到端行为和多点 ablation，不能据此选择 runtime shortcut。

现有证据只覆盖 5-shot greedy、四个 1–3B 模型及确定分类或简单转换任务；主实验样本为 50，部分支持性分析只有 10。它支持“单位置可读不等于单位置控制，task template 可能分布式承载”，不证明开放生成、复杂 Chain-of-Thought 或更大模型共享同一层位，也没有定位承载模板的最小子空间。第 17 章继续拥有多层 residual/MLP 组合，第 66 章则负责把 probe、干预与行为结果组织成通用 evaluation contract。

<!-- semantic-body-binding:SF-2026-ARXIV-2609-35663:start -->
某位置没有在原生输出中直接提供答案，不等于它未参与完成任务。复制entity时，周边context先读取entity，可以改变后续decode如何访问该entity；这与答案内容是否可从context本身读出是两个问题。诊断应分别切断context→entity和decode→entity，再恢复后一路验证行为，而不是把所有attention边一起删掉后宣布信息已丢失。若干late heads在受限干预中足以完成复制，也不授early layer可删除。

这类边级干预增加forward与恢复对照成本，post-softmax置零虽不重归一也会改变后续hidden state；必须保留模板、位置、checkpoint和干预时点。[Entity Copy v1 §2–5](https://arxiv.org/html/2609.35663v1)仅支持单Qwen模型与有限entity复制，不能证明context完全不存信息、所有任务相同层位或一般必要充分性。Probe、原生读出与因果路由应分别验收；复杂生成或干预解释不稳时，保留完整Attention与多点行为对照。
<!-- semantic-body-binding:SF-2026-ARXIV-2609-35663:end -->

### 有表达路径，还需要训练目标能辨别它

<!-- semantic-body-binding:SF-2026-ARXIV-2605-21070:start -->
Attention 的可学习性也取决于 supervision 是否能看见 score 的变化。对 mean-pooled label objective，某些
attention-score 方向在局部可能不改变聚合输出，因而下游梯度无法区分；先用 masked self-pretraining 学到带
邻近偏置的 attention state，再进行分类，可能绕过这一 blind direction。这里的增益属于特定初始化和目标的
耦合，不证明 self-supervision 普遍优于直接监督；小型受控模型、有限 seed 与简化理论也不能外推到大模型训练。
若目标或架构不满足该盲区条件，应回退 matched initialization、直接监督与多 seed 消融。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-21070:end -->

## 归一化决定质量去向，也限制 no-op

归一化还隐含一个常被忽略的约束：每一行必须把全部概率质量分给某些可见 positions。若某个 head 在当前
位置本应执行 no-op，softmax 不能直接令所有权重为零，只能把质量导向一个 value 近零或可被下游忽略的
位置。BOS、register 或显式 null token 因而可能同时承担信息聚合与“安全泄压口”，不能仅凭高 attention
weight 就断言它存储了语义。

理论上的 trigger-conditional synthetic task 已证明，在其精确构造下，softmax simplex constraint 会迫使
至少一个位置形成 sink；移除归一化后可以直接输出全零。这个结论解释了一条机制可能性，不证明真实
pretrained Transformer 的每个 sink 都只有 no-op 功能，更不证明非归一化 Attention 在语言模型上更好。
Softmax 保留稳定竞争、成熟 kernel 与清楚尺度；null/register、显式 gate 或非归一化权重则用额外状态、
缩放和训练稳定性换取 no-op 能力。设计与解释实验都应区分“结构允许的 escape hatch”和“模型实际使用
该位置承担的因果功能”。

允许 no-op 之外，Attention 还须区分没有支持证据与存在低质量证据。一个条件分支给 query 增加显式零输出 option，让它可以不把全部质量分给输入；另一条分支按 value 的特征选择性抑制噪声。前者的零 option 可形成精确 abstention，但把 value gate 当作 routing 再归一化会丢失原来的总质量 Z，不能直接视为同一个聚合算子。Query 选择与 value 过滤拥有不同职责，也不由两者名称推出完整输入已经被忽略。

更强过滤会损失有用证据：受限 FineWeb-Edu 模型中的 norm gate 在较多 junk 时反而退步，投影对齐的攻击又可绕过特征过滤。模型规模、训练切片与有限 seed 不认证任意 pretrained Transformer，未测吞吐也不支持更高生产效率。零 option、特征门与旧 null/sink 都应按相同任务、预算及可观察输出验收，并计新增参数、校准和 kernel 成本；判断失准时保留成熟 softmax、显式 null 与外部输入检查，不能用一个 gate 自签鲁棒性。 [必要机制与反证](https://arxiv.org/html/2609.22005v1)。<!-- source-family:SF-2026-ARXIV-2609-22005 -->

### Sink 与 Outlier 需要跨 Token、跨深度共同诊断

把一个高权重 token 直接称为 attention sink，容易把观察到的突出位置误当成单一原因。更完整的诊断同时跟踪 token axis 上 normalization 如何集中质量，以及 depth axis 上 residual stream 如何累积并放大 outlier；显著 token 可能是二者耦合后的结果，而不是独自拥有模型行为。因果检查因此需要逐层 attention、residual 与受控干预共同对齐。

这类分解提高解释精度，却依赖模型结构和实验假设，也增加跨层测量成本。假设不成立、干预把 activation 推离分布或不同层结论不一致时，应回退逐层 raw attention/residual 报告，不把可视化升级为唯一机制。现有证据只支持作者模型与设置，不证明每个 sink 都由同一种耦合形成。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-17887:start -->
Attention sink 不是一个 token 的固有标签，而是 token-axis normalization 与 residual depth accumulation 的待验证耦合。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-17887:end -->

### Attention Temperature 必须随 Score Gap 结构校准

长上下文中简单固定 logit scale 容易在不同长度 regime 下过于平坦或过度集中，但“随长度取平方根对数、对数或对数平方”也不是普适定律。更一般的分析把每个 attention row 中距最大 score 不同 gap 内的竞争者数量写成 gap-counting function；临界 inverse temperature 由上尾累积尺度决定，低于它时顶层竞争者仍混合，高于它时 entropy 可能坍缩。<!-- semantic-body-binding:SF-2026-ARXIV-2605-12697 -->

这给出的是对 score-family 的诊断框架，不是所有模型的自动调参公式。实际模型的 score distribution、head 角色和位置策略会改变临界尺度；假设或校准不成立时，保留已有 scale，并用长度分桶的 entropy、质量与数值稳定性共同验收。

## 路由改变前，先区分可见边与读取偏好

标准 mask 先限定哪些位置合法可见，softmax 再决定在合法位置间如何分配权重。减少候选连接、增加跨分支连接和修改已有连接的 score，是不同操作；每一种都需要保留自己的可见性与质量边界。

### Sparse Support 与 Value Normalization 是两步决策

Dense mask 预先规定全部可见边；固定 chunk sparsity 则用较低成本换取静态邻域，但不能让不同 query 选择不同范围。可微的层次化分支先用 `alpha-entmax` 选择 variable chunk support，再把第一阶段 prior 注入候选边的 pre-softmax score，最后只在已选 support 上做 sparse normalization。support selector 拥有哪些边，normalizer 决定已选边怎样分配 value mass；两者不能混成一个不可审计的权重矩阵。

动态 support 可以减少无效关系，却新增 chunk controller、索引与稀疏 kernel 复杂度，也会因 support 抖动漏掉必要 token。选择不稳定、backend 无法兑现稀疏收益或质量回归失败时，应回退 dense attention 或固定窗口。现有证据只支持作者结构和 benchmark，不能证明 variable support 普遍优于成熟 dense kernel。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-18753:start -->
层次稀疏 Attention 应先冻结可见 support，再在该 support 内归一化 Value 读取，分别验收两层错误。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-18753:end -->

粗粒度support选择还要防止block平均值掩盖少量重要key。质心可用低成本表示平均相关性，块内最大半径则提示它可能漏掉的局部偏差；完整L2半径能给单个key logit上界，但按分位数衰减半径后只剩风险分数，不能继承这个界或dense输出保证。救援分数逐block增加并不意味着原候选都会保留：若按全branch最大值设相对阈值，某block的提升也会抬高别block的入选门槛。

因此可以分别阈值化base relevance与rescue risk，再合并两mask和明确的保留窗口，让救援只增加选择、不会静默覆盖base集合。RBS的受限同backend/实际density对照支持这一选择，但小诊断集差区间包含零，未证明唯一组件因果或普遍质量保持；相同threshold也不承诺相同cardinality。半径统计、两路score/union与workspace都有成本，块大半径不等当前query真相关，prefill结果不授权decode收益。保留不足或selector成本、质量回归失配时，放宽预算并重新校准，或回dense/fixed support；KV驻留与实际kernel收益仍交缓存/runtime独立验收。 [必要机制与反证](https://arxiv.org/html/2609.20971v1)。<!-- source-family:SF-2026-ARXIV-2609-20971 -->

可训练 gate 还不一定等价于部署时的 support 删除。一种阈值分支从 post-RoPE query 预测 threshold，训练时把低分 logit 乘以 sigmoid，使其趋向零；softmax 中零 logit 仍贡献 exp(0)，并没有被删除。推理 hard pruning 则改变归一化 support。高分侧的指数近似以 gate≈1 为条件，仅 score 超过 threshold 不足；这一近似本身也不给最终输出误差保证。all-pruned 的 top-1 rescue 只是数值兜底，不能恢复全部被删语义。模型验收应分别检查训练算子、部署算子和最终行为，不能由保留率宣称 exactness。<!-- source-family:SF-2026-ARXIV-2609-20888 -->

Block skip 的理论界也须与实际统计量区分：full-covariance 的条件上界不等于用 diagonal variance surrogate 得到的 quantile estimator，后者仍会 false negative。GQA 下一个 KV block 是否搬运取决于共享它的 query-head union，不能按单 head 稀疏度直接兑现 HBM 节省。作者 H100/FP16 kernel 表中，约38% head-density 的质量点固定 block width 64，在不同 batch/length 下仅约0.72–1.12倍 dense；2.5倍来自 block width 128、10% head-density 的另一点。局部 soft/hard alignment亦不证明任意query质量。因此阈值预测、metadata/chunk reduction和训练成本都要计入，质量或实际收益不成立时回 dense/fixed support；真实缓存与kernel执行继续交第45/49章。[必要算子、统计与运行条件](https://arxiv.org/html/2609.20888v1)。

### 稀疏连接可以跨层补全可达性，但不能免费替代内容路由

单层固定稀疏图只让 token 读取少数邻居，易实现且成本稳定；如果每层按确定性置换旋转连接，同一信息可在 `O(log n)` 层内传播到全序列。它把单层的全连接搜索换成跨层组合路径，因此适合连接预算严格、通信图可预编译的分支。

这种“最终可达”不等于每层能按内容选择任意 token，也不保证有限深度、训练优化或下游质量与 softmax Attention 等价。连接调度成为 architecture identity；窗口很小、深度不足或重要关系需要即时内容路由时，应保留局部/全局 Attention 或混合层。现有证据来自小型字符模型和受限窗口，只支持连接性与局部效果，不支持通用 Transformer 替换。<!-- source-family:SF-2026-ARXIV-2609-18145 -->

### 跨推理分支增加连接，必须重新说明可见性

多条独立采样能覆盖不同路径，却要等答案完成后才由选择器整合；若同一请求的推理分支需要在生成中交换中间表示，可以在原有序列 Attention 旁增设低维 cross-thread Q/K/V 路径，再以 gate 与原输出融合。thread identity、token position 与可见前缀共同定义连接域：共享请求内的分支才是候选，batch 或 tenant identity 不能因为 flatten 成一个矩阵就消失。原 causal backbone 保留，也不自动证明新增横向边没有读取未来位置，必须单独明确其时间 mask 与缓存生命周期。

这条分支增加联合训练、分支相关性、共享错误与同步/访存成本，更多 thread 不再等于独立样本。[LACE](https://arxiv.org/html/2604.15529v1)用低维支路、gate 及 thread-group 训练提供受限机制证据，但本文 flattened SDPA 公式未明示横向时间 mask，不能据其宣称已验证无泄漏实现；在单 RTX PRO6000 Blackwell、BF16、context 50 / generation 100 的短微基准中，虽增加不足 1.3% FLOPs，四 thread step latency 仍增加约 31～38%，TPS 反而下降，这不是服务并发或 p99 结论。横向信息没有提升独立质量/选择验收、mask 语义不清或同步成本不能摊销时，保留独立采样及完成后的 voting/selection 更透明。
<!-- source-family:SF-2026-ARXIV-2604-15529 -->

### 计算预算可以进入 Attention 路由，但必须有可执行的硬边界

固定 head 集合在预算稳定、所有输入使用同一服务档位时最容易训练和部署；约束改变发生在同一模型需要覆盖多个
compute budget 时。此时可以让预算条件进入 layer/head gate：训练阶段以连续门控和显式 cost penalty 学习“预算减少时
先关闭哪些计算”，部署阶段再把它编译成 hard top-k 子图。预算控制器只提出本次可用计算集合，已编译执行计划决定
哪些 head 真正运行；soft gate 的期望成本不能直接当作 wall-clock latency。

这条路径用一套参数覆盖多个预算点，却新增 gate collapse、预算外泛化、离散化误差和不同 shape 下 kernel 效率不一致。
验收必须逐预算报告质量、实际 FLOPs、延迟和激活 head 分布，并比较独立稠密模型；若 hard gate 没有在目标 runtime
兑现成本，或任务不能容忍按预算变化的能力，固定稠密 Attention 仍是更可预测的旧方案。现有证据仅支持作者模型、
预算范围与部署转换，不证明任意 head 都可无损裁剪。<!-- source-family:SF-2026-ARXIV-2605-05697 -->

### Query-space Steering 改变的是 QK 路由

固定 activation vector steering 直接移动表示，却不说明注意力从哪里读、向哪里写。一个更局部的 actuator 是在 query space 中修改相对 QK logits，使注意力从 focus tokens 转向 tail；只投影高风险 head 上的 focus-tail key-difference component，可以在受限设置中保留部分 steering efficacy，同时减轻 utility 损失。<!-- semantic-body-binding:SF-2026-ARXIV-2605-06342 -->

这种方法依赖白盒 Attention、focus threshold、风险 head 识别和独立的 utility calibration set，不能构成通用 safety 保证。head 或 token 角色随任务漂移、utility regression 超界时，应回退不 steering、减小强度、使用输入 Gate，或把约束移到权重级后训练。

### Pre-RoPE Pair Gate 可以局部改写视觉路由

统一给所有 heads 加 visual bias，控制简单却会扰动不需要视觉增强的文本关系。更局部的分支在 RoPE 之前读取 query/key pair，生成 gate 后只对选定 GQA heads 的 visual positions 加 pre-softmax bias；位置编码和原 logits 仍保留，gate 只拥有一次受限路由修正。

这种分权减少全局扰动，却新增 gate calibration、head selection 与跨 backbone 漂移风险。当前证据只有两个 backbone 与有限 benchmark；gate 不稳定、文本能力回归或冲突检测不可信时，应回退原始 logits，而不是继续放大视觉权重。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-18359:start -->
视觉路由修正应绑定 pre-RoPE pair gate 与明确 head 集合，避免把局部需要升级为全局 Attention 偏置。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-18359:end -->

### 视觉候选集合的选择与复用

前面的 steering 和 pair gate 修改既有边的读取偏好；下面两种分支则缩小参与 Attention 的视觉候选集合。候选选择能节省多少计算，以及保留什么状态用于恢复，需要分开说明。

#### Visual Token Selection 可以复用，但 Full KV 仍是恢复边界

文档解析若每层、每个 decode step 都重新让全部视觉 token 参与路由，最稳健却反复支付相同选择成本。一个受限执行分支先在 focal layer 用 full visual attention warm up，再按当前 query 跨后续层选择视觉 token，并在 decode 中复用该选择；完整 KV 仍被保留，以便选择失准时恢复。selector 只拥有 active visual set，不拥有删除原状态或改变文本路径的权力。

它降低后续 attention 工作量，却不降低 full KV 的峰值占用，prefill 也可能因 warm-up 与选择开销退化。版面改变、query 漂移或关键 token 被漏选时，应立即回退 full visual attention。作者结果只覆盖其文档解析模型、benchmark 与硬件条件，不能外推为通用多模态加速。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-17447:start -->
视觉 token 的复用选择是可撤销的路由缓存，不是对完整视觉 KV 的永久驱逐。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-17447:end -->

#### 视觉 Token 预算应分开处理帧间与帧内冗余

<!-- semantic-body-binding:SF-2026-ARXIV-2605-23892:start -->
统一保留比例把所有 frame 和 frame 内 token 视为同质，在短视频中易于实现；长视频中，inter-frame diversity 与 intra-frame entropy 应由不同阶段估计，再提出 layer-aware token selection。Selector 只控制计算候选，几何一致性和任务精度仍拥有最终提交权。

两阶段剪枝能减少 Attention 成本，也会放大运动估计错误、丢失稀有事件，并让阈值随 layer 和视频域漂移。作者结果只覆盖披露模型与数据；几何证据不足、精度回归或场景快速变化时，应提高预算或回退 dense attention。arXiv:2605.23892v1
<!-- semantic-body-binding:SF-2026-ARXIV-2605-23892:end -->

## 改变匹配表示：从独立 Q/K/V 到条件化替代

保持 Q/K/V 的独立坐标最容易分清路由与传值。如果要合并表示、通过 latent slot 中转，或移除可学习寻址投影，就必须重新检查参数化和表达边界，不能只把变化记作缓存或 kernel 优化。

<!-- daily-20260621:model-self-attention:start -->
### Routing representation 与 cache representation 的条件合并

把 query-key 路由改为 query-value 路由，并在 inference 预乘 query factor，只保存 value representation；QVV(3) 保持投影矩阵数同时移除 key cache。

等价定理依赖 value projection 的秩/子空间条件；小模型从头训练不证明可无损转换既有大模型，50% 是 attention-cache tensor 而非端到端显存。目标模型若不满足秩/子空间条件，或转换后的质量与执行路径未通过验证，应保留独立 Q/K/V 投影与标准 K/V cache。

**Source evidence boundary**

- `SF-2026-ARXIV-2606-21848` — primary `arXiv:2606.21848v1`；exact-v1 URL=`https://arxiv.org/html/2606.21848v1`；Method=`https://arxiv.org/html/2606.21848v1 — §2 Method; §3 Value-only Cache in Autoregressive Inference`；Evaluation=`https://arxiv.org/html/2606.21848v1 — §5 Experiments`；Non-proof=`https://arxiv.org/html/2606.21848v1 — §2.2 equivalence conditions; §6 Limitations`。
<!-- daily-20260621:model-self-attention:end -->

Attention state 的经典分解保存 key 与 value，因为 query-key 决定路由、value 决定读取内容；新的因式分解可以把路由改写为 query-value 并减少缓存对象，但这同时改变模型参数化、训练目标和 runtime identity，不能被当作无语义变化的 KV 优化。

更少缓存换来重新训练、kernel 支持与分布外稳定性风险。若等价性、质量或执行路径没有在目标模型上验证，标准 Q/K/V Attention 仍是正确 fallback；FlashAttention 等执行优化继续只拥有 IO 调度，不拥有模型语义。

### Latent Routing 是 Attention 的替代分支，不是免费等价

显式 token-to-token affinity 能表达细粒度关系，但中间状态随序列长度平方增长。另一条路线让每个 token 先对固定数量的 latent mixture components 计算 responsibility，再通过共享 component 聚合信息；固定 $K$ 时，激活状态从 $O(N^2)$ 变为 $O(NK)$。这些 component 同时承担 soft routing 与 memory-slot 角色。Model owner 定义 responsibility 与 latent-slot 语义，runtime 只实现 $O(NK)$ 的物化与状态保存，release owner 则依据质量回归和目标硬件实测决定是否采用。

代价是 affinity 被限制为低秩、非负且经 latent bottleneck 的结构，长程依赖可能被过度合并；当前 causal kernel 也未必胜过成熟 SDPA 或 state-space 实现。K、训练稳定性和目标硬件共同决定收益，表达边界或 kernel 不满足时应回退 softmax attention 或混合层。

<!-- semantic-body-binding:SF-2026-ARXIV-2606.18283 -->

### Projection-free Kernel Attention 是另一种归纳偏置

Q/K 投影让模型学习“用什么坐标寻址”，表达力强但也引入参数和尺度耦合。一个替代分支直接在 hidden state 间计算 Gaussian kernel，再行归一化为 row-stochastic diffusion；bandwidth 控制局部性，Value 或原状态承载被传播的信息。它不是对标准 Attention 的执行优化，而是移除可学习寻址投影、改用距离核的不同模型族。

这样获得更明确的平滑与局部性先验，却可能无法表达非对称、内容特定的路由，并对距离尺度和高维集中敏感。结构先验合适、数据较少或需要稳定扩散时可作为分支；复杂语义寻址仍应保留 Q/K/V Attention。现有 exact-v1 只支持作者架构与实验，不证明核扩散普遍优于 learned projection。<!-- semantic-body-binding:SF-2026-ARXIV-2605-02144 -->

## 将历史压入递归状态后，写入规则成为核心约束

前面的分支改变匹配表示；递归 Linear Attention 进一步用有限状态承接历史。这里聚焦状态怎样更新、怎样控制写入尺度；显式历史、线性 Attention、SSM 与 hybrid 的整体状态取舍由[第22章](22-long-context.md)展开，标准 K/V 的缓存复用由[第19章](19-kv-cache.md)接手。

### 从固定写入规则到目标导出的递归更新

把注意力历史压进固定大小的递归状态时，旧路径常让模型直接学习一个未归一化的写入系数。这在 key 范数稳定时简单有效；但当范数变化很大，同一个系数会对应完全不同的实际更新幅度，state 可能过写或几乎不写。更稳健的演进是先把 state update 解释成逐步求解 online-regression objective，再由投影几何推导按 key 范数归一化的动态步长。模型仍可学习基础速率，更新规则却不再把输入尺度变化误当作记忆重要性。

这条分支获得更可解释的写入尺度与数值稳定性，代价是额外范数计算、epsilon 与更新规则都成为模型身份的一部分；它也没有恢复被有限状态容量压缩掉的信息。Softmax Attention 在需要精确 token 访问时仍成立，Gated Delta 一类 learned update 在数据分布稳定、kernel 更成熟时也继续共存。本节只说明 update rule 的约束来源，不把单一实验外推为线性注意力的通用优势。[受限证据：arXiv:2605.08587v1]

<!-- source-family:SF-2026-ARXIV-2605-08587 -->

### Linear Attention 的写入步长可以成为向量状态

Delta-rule linear attention 用单一 scalar gate 控制 memory update，状态小且容易 chunk 化；当不同 feature 方向曲率差异明显时，同一 gate 无法同时提供快速写入和稳定收敛。对角 preconditioner 可以通过在线 hypergradient 更新，为各维度维护不同的写入尺度，同时保留受限的 affine recurrence。<!-- semantic-body-binding:SF-2026-ARXIV-2605-13473 -->

新增的 meta-optimizer state 会放大稳定性、初始化和数值误差风险。理论保证依赖精确二次 inner loss、单调迭代或特定 comparator 等条件，不能直接外推一般 sequence learning；这些条件不成立或额外状态成本超过收益时，应回退 scalar gate 或普通 softmax Attention。

### Linear Attention 可以维护多时间尺度的有界状态

<!-- semantic-body-binding:SF-2026-ARXIV-2605-23889:start -->
单一衰减率的 recurrent linear attention 在序列统计近似均匀时状态最小；不同通道的有效记忆尺度不同后，可以用 per-channel decay 维护多时间尺度状态，并让 local attention 负责短程精确关系。长期 state 与局部窗口分责，避免一个门同时承担所有 horizon。

更细的 decay 提高适配性，却增加参数、数值漂移和 state geometry 失稳风险。exact-v1 只支持作者模型和 trajectory/reconstruction 设置；state norm、长程质量或实现稳定性 Gate 失败时，应回退统一 decay、窗口 attention 或标准 softmax attention。arXiv:2605.23889v1
<!-- semantic-body-binding:SF-2026-ARXIV-2605-23889:end -->

## FlashAttention 优化的是执行，不是模型语义

朴素 Attention 可能把 score 和 softmax 中间结果写入 HBM，再读回做后续计算。FlashAttention 使用 tiling 与 online softmax，在片上 SRAM 可容纳的小块上组织 exact attention，减少 HBM 往返和中间存储。这是决定 Attention 能否高效执行的重要优化，但它回答的是“相同语义怎样少做 IO”，而不是“token 应该怎样建立关系”。

它没有改变：

```text
Query 根据所有允许的 Keys 计算权重
再用权重聚合 Values
```

因此需要区分：

```text
Self Attention  定义模型语义与成对关系
FlashAttention  优化 exact attention 的 IO 执行
KV Cache        避免 Decode 重算历史 K/V
PagedAttention  管理运行时 KV Cache 物理存储
```

这些技术共享 Attention 背景，却属于不同知识树节点。

### 数值与实现边界

工程实现还要处理：

- Mask 在低精度下用足够小的有限值近似 `-inf`。
- Softmax 通常先减去 row maximum 避免 overflow。
- Q/K/V layout 可能为 `[B,T,H,d_h]` 或 `[B,H,T,d_h]`。
- Fused kernel 可以隐藏 reshape、transpose 与 mask，但不能改变模型含义。
- Dropout、bias 和 precision 属于具体训练配置。

阅读 kernel 或 runtime 时，应先恢复逻辑 tensor shape，再分析物理 layout。

## 改变算子之后，转换与执行必须分别验收

FlashAttention 保持已定义的 Attention 语义。下面的路径则涉及替换算子、近似冻结 teacher，或利用专门的稀疏与分块结构；先明确目标算子，再谈训练转换和执行收益，才能避免把近似质量当成 exact IO 优化的一部分。

### 替换已训练算子，先解决局部冷启动，再恢复整网行为

前面的替代聚合改变了信息路由，却不能直接继承旧 checkpoint 的行为。源与目标结构足够接近时，权重分解或映射是合理起点；差异较大、替换层随机初始化时，直接匹配最终 logits 会让浅层误差沿 residual 路径累积，深层收到的训练输入也随之失真。一条有条件的转换路径先固定 teacher：每个替换层都接收 teacher 的 hidden state，独立匹配 residual addition 前、post-o_proj 的输出，以目标能量归一化 MSE；局部初始化稳定后，恢复 student 自身整网数据流，再以 token-level KL、可选低权重 feature loss 对齐。

这增加 teacher 前向、训练语料和转换预算；同一输入下逐层回归接近，并不证明自由生成等价，仍须测完整模型与目标执行路径。[Attention Editing](https://arxiv.org/html/2604.05688v1)仅给出 Qwen3 到 MLA/GateSWA、Ascend 训练的受限证据，并要求保留的 o_proj shape 兼容，不是任意权重零训练转换。结构映射足够好、转换成本无法摊销或质量回归未通过时，旧 Attention 仍应保留；下一分支处理的是冻结算子的部署编译，而不是同一种架构重训。<!-- source-family:SF-2026-ARXIV-2604-05688 -->

### 训练时求解、部署时编译的 Attention 分支

Sinkhorn attention 在训练和推理中反复执行 matrix scaling。训练时利用双边 marginal 归纳偏置是合理的，
但部署时继续支付每次 forward 的迭代成本；简单减少迭代次数虽然更快，却会把训练好的层替换成另一个
finite operator。一个有条件的演进，是在训练结束后冻结 teacher，用未标注 calibration activation 学习
从输入到 dual potential 的映射，再以预测 dual 和固定的 two-sided entropic c-transform 构造 attention
plan。训练阶段仍保留 Sinkhorn semantics，部署阶段则把在线迭代转成可版本化的离线 compile artifact。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-12879:start -->
这条分支没有让 Attention 稀疏，也没有改变其二次复杂度：dense QK score 与 value mixing 仍然存在；
calibration dataset、teacher 的 finite-update convention、coefficient 和 activation distribution 反而成为
layer identity 的一部分。分布漂移会要求重校准，线性 dual map 也可能损失 teacher fidelity；严格 causal
mask 下的 marginal 还需要单独定义。无法摊销 compile、分布不稳或因果约束尚未闭合时，原始 Sinkhorn
仍是 fidelity baseline；不需要双边 marginal 时，row-softmax/dense attention 仍更简单。现有证据只支持
冻结层及受测 vision/text encoder replacement，不能外推为任意 decoder 的通用加速结论。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-12879:end -->

### 稀疏匹配特征需要能消费该布局的 kernel

Dense attention 的另一条演进不是减少参与交互的 token，而是减少 Q/K 用于匹配的 feature。Token sparsity
假设只有少数位置值得读取；feature sparsity 则假设内容路由可以由稀疏 feature code 近似，同时让 Value
aggregation 继续保留被选关系的语义。若只是把 Q/K 置零、仍交给 dense GEMM，算法稀疏不会自动产生 IO
收益；它需要与 sparse-code layout、索引生成和能直接消费该布局的 kernel 联合设计：

```text
dense token × dense feature matching
→ sparse token selection, or sparse Q/K feature coding
→ layout-aware score kernel
→ exact / dense fallback for unsupported shapes
```

这条分支把控制权从 token admission 移到 feature code 与 kernel contract。它可能在长序列、稀疏结构稳定且
专用 kernel 可摊销时降低计算与内存流量，却增加编码、索引、负载不均和碰撞/漏配风险；稀疏关系也不等于
语义上不重要。中短序列、feature 稀疏度不足或 backend 不支持时，dense FlashAttention 仍是更成熟的基线。
现有证据只支持作者模型和实现中的 accuracy/throughput operating point，不能证明 feature sparsity 普遍优于
sequence sparsity。<!-- source-family:SF-2026-ARXIV-2603-22300 -->

### 块内精确、块间近似只对特定算子成立

<!-- semantic-body-binding:SF-2026-ARXIV-2605-22476:start -->
固定窗口或稀疏 support 通过删除跨块边降低复杂度，在路由本来局部且被删关系无关紧要时简单有效；它却无法表达“块内关系必须保持精确，但块间仍需少量全局传播”的算子。对具有稳定 block-local 结构的 resolvent-style attention，一条更窄的路径让每个 local tile 继续执行原始 triangular solve，只把 off-block residue 汇聚到保持顺序的 reduced system，求解后再 lift 回完整位置。Operator owner 冻结 block partition、causal mask、pool/lift 和 reduced-system semantics，runtime 只能执行该冻结分解，不能把它泛化成任意 softmax sparsity。

这种 exact-local / approximate-residual 拆分只有在 block locality 足以摊销 tiling、pool/lift 和 reduced solve 时才减少工作；它增加两个执行分支、block-size 选择、预训练适配和 head-capacity failure。多属性 tracking 超过 heads、routing 变得 diffuse、残差误差或实测 latency 失败时，应回退 dense resolvent、普通 dense Attention 或已验证的 fixed-window/sparse kernel。现有证据只支持论文披露的 resolvent operator、受控 entity tracking、因果任务和 kernel 实验，不证明该分解等价于任意 softmax Attention 或适用于任意预训练 checkpoint。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-22476:end -->
<!-- source-family:SF-2026-ARXIV-2605-22476 -->

## 本章在知识树中的位置

下面沿概念依赖串起本章，位置机制的实际接入点仍分别是输入、Q/K 或 score，不是一律先修改 embedding。

```text
Embedding + Position
-> X [B,T,d_model]
-> Q/K/V [B,T,d_h]
-> scores [B,T,T]
-> contextual output [B,T,d_h]
-> Multi-Head Attention
-> Transformer Layer
```

本章以单 head 的内容路由为基础，比较了改变连接、归一化、匹配表示与状态更新的条件分支；不在这里展开多 head 组合、完整 Layer 或缓存管理。下一章接手仍未解决的问题：一套 score 几何如何同时承载多种关系？[第15章](15-multi-head-attention.md)会让多个投影子空间并行工作；[第17章](17-transformer-layer.md)再把 Attention 与 MLP、Residual、Normalization 组成完整 Layer。

## 自检问题

1. 逐位置 MLP 为什么不能让 token 读取上下文？
2. Q、K、V 为什么承担不同角色？
3. `[B,T,d_h]` 的 Q/K 为什么生成 `[B,T,T]` scores？
4. `sqrt(d_h)` 缩放解决什么数值问题？
5. Causal mask 与 padding mask 有何区别？
6. 三 token 例子中，为什么第一行权重只能是 `[1,0,0]`？
7. Dense Attention 的二次项来自哪里？
8. FlashAttention 改变了算法语义还是 IO 执行？
9. 为什么逻辑 shape 与物理 layout 必须区分？
10. Self Attention、KV Cache 与 PagedAttention 分别位于哪一层？

## 小结

Self Attention 把上下文建模转化为可微分路由：Q/K 决定连接权重，V 承载被读取内容，mask 约束允许的信息流，softmax 将分数变成归一化权重。

它用短依赖路径和规则矩阵计算换来了二次成对计算与运行时状态。理解公式、shape 和小例子后，后续 MHA、KV Cache 与推理系统才有稳定起点。

## Review notes

- [Attention retrieval capacity v1](https://arxiv.org/html/2609.37879v1) §2–4；Daily 2026-09-30。只采用 mass/Value/direction 与不同删除干预的边界；有限模型和长上下文诊断不证明事实容量或端到端加速，未复现实验。

- `SF-2026-ARXIV-2604-15529` — [LACE v1](https://arxiv.org/html/2604.15529v1)：§3–4、必要 E.1/F.1 支持同请求 cross-thread routing 分支、相关性与 microbenchmark 成本边界；横向时间 mask 未明示，不采用无泄漏保证。root 已完成必要 source→owner 窄采用核，root已顺读实际正文及相邻衔接，非作者写后通过。

本轮 Review 在已有 content-dependent routing 与 FlashAttention 边界上补齐统一 shape 和三 token 演算。Multi-Head Attention、完整 Layer 与 KV Cache 分别保留给第15、17、19章，不在本章混写。

Primary-source 校验入口：

- Ashish Vaswani et al., "Attention Is All You Need", 2017: https://arxiv.org/abs/1706.03762
- Tri Dao et al., "FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness", 2022: https://arxiv.org/abs/2205.14135

### Daily Books delta trace（2026-05—08）

<!-- daily-books-trace:SF-2026-ARXIV-2605-04061:start -->
- `SF-2026-ARXIV-2605-04061` — Daily `2026-05-07`；primary `arXiv:2605.04061v1`；Books review `books-review:SF-2026-ARXIV-2605-04061`。

  **已吸收的语义增量：** 区分 hidden state 的线性可解码性与对输出的必要/充分因果控制，并以单点、多点干预和行为验证构成诊断阶梯；结论仅限论文测试的小模型、受控 ICL 任务和样本规模。
<!-- daily-books-trace:SF-2026-ARXIV-2605-04061:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-21848:start -->
- `SF-2026-ARXIV-2606-21848` — Daily `2026-06-21`；primary `arXiv:2606.21848v1`；Books review `books-review:SF-2026-ARXIV-2606-21848`。

  **已吸收的语义增量：** 把 query-key 路由改为 query-value 路由，并在 inference 预乘 query factor，只保存 value representation；QVV(3) 保持投影矩阵数同时移除 key cache。
<!-- daily-books-trace:SF-2026-ARXIV-2606-21848:end -->
