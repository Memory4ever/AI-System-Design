# 第15章 Multi-Head Attention

**Knowledge Tree:** Part II 模型：一个 Token 如何变成答案
**Stable Knowledge Node ID:** `MODEL-MULTI-HEAD-ATTENTION`
**Legacy Chapter:** Ch15
**Status:** Draft

**Roadmap Intent:** 为什么需要多个注意力头，从不同子空间捕捉关系。

## 本章要回答的问题

第14章的单个 Attention head 已能让 token 按内容读取上下文，为什么还需要多个 head？Multi-Head Attention 如何在多个投影子空间并行建立关系，又为什么会演化出 MQA 和 GQA？

本章的核心判断是：**Multi-Head Attention 不是重复计算同一份注意力，而是让多个可学习投影并行构造不同路由子空间，再把这些结果组合回统一 hidden state。**Head 数增加了表达路径，也增加了投影、layout、KV state 与并行约束。

本章使用 `B` 表示 batch size，`T` 表示 sequence length，`d_model` 表示 hidden dimension，`H` 表示 Query head 数，`H_kv` 表示 Key/Value head 数，`d_h` 表示单个 head dimension。

## 单个 head 的表达瓶颈

一个 head 对每个 Query 只产生一行归一化权重，并用同一套 Q/K/V projection 决定所有关系。它可以同时给多个位置分配权重，但全部匹配共享一个子空间和一套 score 几何。

序列中可能同时存在不同关系：

- 局部搭配与远距离依赖。
- 语法主从关系与实体指代。
- 内容相关 token 与格式边界。
- 当前位置的多种候选读取策略。

朴素方案是把单 head 的维度做得更大。容量增加了，但所有关系仍竞争同一个 score matrix。Multi-Head 的思路是让模型并行学习多组投影，每组独立产生 attention distribution。

## 从单头投影到多个 head

输入保持：

```text
X shape = [B,T,d_model]
```

常见配置满足：

```text
H * d_h = d_model
```

但这是常见设计，不是数学必然。可将大投影矩阵写为：

```text
W_Q [d_model,H*d_h]
W_K [d_model,H*d_h]
W_V [d_model,H*d_h]
```

投影后 reshape 和 transpose：

```text
Q = X W_Q -> [B,T,H*d_h] -> [B,H,T,d_h]
K = X W_K -> [B,T,H*d_h] -> [B,H,T,d_h]
V = X W_V -> [B,T,H*d_h] -> [B,H,T,d_h]
```

每个 head 独立执行第14章的公式：

```text
head_h = softmax(Q_h K_h^T / sqrt(d_h) + M) V_h
head_h shape = [B,T,d_h]
```

所有 heads 合在一个张量中：

```text
heads shape = [B,H,T,d_h]
```

## Concat 与输出投影

Head outputs 不直接相加，而是先把 head 维移回 token 后面，再 concat：

```text
[B,H,T,d_h]
-> transpose [B,T,H,d_h]
-> concat    [B,T,H*d_h]
```

随后使用 output projection：

```text
W_O [H*d_h,d_model]
Y = Concat(head_1,...,head_H) W_O
Y shape = [B,T,d_model]
```

`W_O` 让不同 heads 的信息重新混合，并把输出恢复到 residual stream 的 `d_model`。如果简单平均 heads，会提前丢失“哪部分信息来自哪个投影子空间”的自由度。

保留 concat 并不要求输出混合一定使用任意可学习的稠密矩阵。若参数和执行预算先触及边界，可以保留 Q/K/V 与各 head 的内容路由，把输出改为固定的全局混合 basis，再学习逐通道 scale 与 bias，例如 `alpha ⊙ (Y H) + beta`。固定 Hadamard 型变换用加减法组织混合，取消的是 `W_O` 的任意矩阵自由度，而不是把多个 head 平均成一个，也不减少 attention score 的 `T²` 项。basis、归一化、支持的维数和具体 kernel 都属于新架构的执行合同；固定变换可逆不代表任意已训练 `W_O` 能无损替换，后续 affine 也不恢复任意矩阵的表达范围。<!-- source-family:SF-2026-ARXIV-2603-08343 -->

这个分支用更小的可学习混合空间换取参数与算术预算，同时要求其余投影在训练中适应固定 basis。实际收益仍须比较质量、训练时间和完整推理路径，而不能把算术复杂度降低直接写成加速保证。[受限实现与评价](https://arxiv.org/html/2603.08343v1)只在较小训练模型上检验质量，较大随机初始化配置的执行测量不证明同规模模型已训练可用；小配置存在速度反侧，成熟 GEMM 与尚未优化的变换实现也可能抵消理论节省。任务需要更自由的 head 重组、维数或 kernel 不支持、质量或总时间回归时，保留稠密 `W_O`。这与下面扩大匹配空间的设计是不同预算分支，不能共用一项表达力或速度结论。

输出投影混合已经聚合好的 head；若要改变 softmax 之前谁能与谁匹配，就需要另一种接口。一条受限分支先在 head 轴分别线性混合 Q/K/V，给每个 head 生成 P 组 pseudo-tokens，再把原长度 N 交错成 NP 个虚拟位置，按这些位置执行 causal attention 与 RoPE。这不是增加输出 W_O，也不是 GQA 减少 KV heads；它扩大匹配空间，同时把全局 attention 的每 head 工作量推到 O(P²N²d)。[必要机制与预算控制](https://arxiv.org/html/2602.21371v1#S4)通过局部窗口/周期性全局层约束比较预算，但 FLOP 近似匹配和 FlashAttention 兼容不等于 KV、位置编码、训练或延迟免费。无位置的代数包含关系也不授旧 RoPE checkpoint 无损转换；有限任务有反退，预算紧或改动接口未验收时仍保留 MHA/GQA，而不把更多可表达关系当成已学可靠算法。<!-- source-family:SF-2026-ARXIV-2602-21371 -->

Head轴也可以承担预先声明的几何结构，而不只自由分化或扩展虚拟位置：对一个有限旋转群`G`，先把每个点的特征提升为各局部frame下的表示，再将frame轴并入head/channel布局，按相对群元素共享Q/K/V及MLP的线性映射。[一条受限群等变构造](https://arxiv.org/html/2510.03511v1#S3)使群内输入旋转对应frame轴置换，最终readout与位置条件仍须另验；12/24/60个三维旋转组成的有限子群不是任意SO(3)旋转，外部frame或绝对位置也可能破坏端到端对称。固定总宽`|G|C`时，增大群会挤压每frame通道，参数共享不免lifting、展开/缓存与训练费用，更不保证任务质量单调。恒定key并省去softmax的线性卷积分支又是另一算子，不能由重排乘法把一般softmax Attention也称为线性执行；序列长度、宽度、群与最终质量必须分别验收。目标对称性、容量或全链预算不合时，保留普通MHA、已验位置编码/增强和标准Attention，不由较少参数或几何名称批准无损替换、任意旋转泛化与净加速。

<!-- source-family:SF-2025-ARXIV-2510-03511 -->

## 一个两 head 小例子

设 `d_model=4`、`H=2`、`d_h=2`。某个 token 在两个 heads 聚合后的输出分别为：

```text
head_1 = [1.0, 0.0]
head_2 = [0.2, 0.8]
```

Concat 得到：

```text
z = [1.0, 0.0, 0.2, 0.8]    shape [4]
```

若为了演示令 `W_O` 为 `4x4` identity，最终输出就是 `z`。真实训练中的 `W_O` 会学习如何混合这四个分量。这个例子说明 heads 的输出被保留后再组合，而不是先压成一份平均结果。

多个 heads 是否真的分别对应“语法头”“指代头”，需要实验验证。可视化某个 attention pattern 只能提供行为线索，不能保证每个 head 有稳定、单一的人类概念。

## Head 怎样分化，又为什么会冗余

`H` 是训练前写进架构的超参数，不是模型先观察问题、再像 MoE router 一样动态决定要启动多少个 heads。标准 MHA/GQA 的一次 forward 会生成全部 Query heads，并沿 checkpoint 固定的分组执行 Attention；MoE router 选择的是 FFN Experts，不能替代 Attention head 的路由语义。

不同 heads 接收同一批 token、服务同一个最终 loss，但各自拥有不同投影参数，并通过不同 score matrix、concat 位置与 `W_O` 路径接收梯度。随机初始化和训练过程会打破完全对称，使它们可能形成互补路由；这不是“每个 head 被分配一个领域”的监督，也不保证最终彼此独立。即使初始化时令投影近似正交，联合优化也可以再次把它们推向相关子空间。

因此，多头结构提供的是**可分化的表达路径**，不是 `H` 份必然有效的独立能力。已有剪枝研究表明，特定训练模型和任务中的一些 heads 可在较小质量变化下移除；这能证明冗余可能存在，却不能推出所有层、所有输入都有同一组“无效 heads”，也不能把 post-hoc 分析直接等同于生产加速。真正跳过 head 需要训练期 pruning、gating 或稀疏执行 contract，并让 checkpoint、kernel 与评估共同支持。

Head轴还可以被组织成多个ensemble成员的计算接口，而不只是删掉冗余头：从共同基座剪出不同head集合，以分组投影保各成员的读取路径，再让它们消费共享的MLP，并在序列或深度布局中保留member身份。[Hydra的受限对照](https://arxiv.org/html/2510.18358v1)用这种计算共享减少重复，但平均MLP与共同预训练并不保持各独立模型的原函数，也不能把成员分歧当作独立、已校准的不确定性。应分别验分类质量、分歧/校准和完整执行成本；所测BERT的ensemble基线还共享预训练，有限BF16计时不是所有硬件的单模型费用。剪枝、成员恢复训练、分组activation与全部分支均计费；多样性、质量或净预算失配时，保留原MHA、真正独立成员或单个已验模型，不由一次forward名称批准独立证据与普遍鲁棒性。

<!-- source-family:SF-2025-ARXIV-2510-18358 -->

固定总容量H之外，还可以让输入决定当前启用多少head、以及启用哪些head：用globalpooling分别产生预算标量与head排序，训练先加权全部head，推理再只消费硬选集合。预算与身份是两项接口，不由较小权重证明对应计算已跳过，也不由平均pooling获得token级难度真值。[BudgetFormer的受限encoder提案](https://arxiv.org/html/2604.22583v1)恰有soft训练与hard推理的资格差：原文entropy项符号与探索/稀疏解释相反，最少一head与纯floor写法也冲突，未核实现前不照录完整recipe。全部训练head、selector、Q/K/V/O及FFN仍计费，按head比例估FLOPs/碳不代表真实时延、显存或能耗；测试兼作validation及任务退步也限制泛化。预算、mask、稀疏kernel或质量未验时，保留固定MHA/GQA与已验静态剪枝，不让head少或热图更集中签发全模型加速及语义必要性。<!-- source-family:SF-2026-ARXIV-2604-22583 -->

BOS 上的注意力概率质量集中只是一个诊断模式，移除某个 head 对当前任务影响小，也不证明它永远没有可训练容量。资源允许时，可以把定点恢复作为 pruning/gating 之外的替代分支：重初始化选中 head 的 Q/K/V 投影，将其 output projection 置零以降低初始残差扰动，再冻结其他参数，只对目标参数短训。[BLOOM 的受限实验](https://arxiv.org/html/2603.09616v1#S3)支持这条方法分支，而不证明所有 sink 都源于同一位置病因或所有被剪 heads 都值得恢复。冻结权重也不冻结共享 residual stream 的输入，目标头改变后，未改头的 attention 行为仍可能漂移，因此干预验收不能只看选中 heads。<!-- source-family:SF-2026-ARXIV-2603-09616 -->

恢复的诊断容量与最终任务效用必须分账：按 BOS mass 阈值重新变“健康”，不等于 held-out 质量、语言分布和真实任务保持。该实验的完整手术只在 BLOOM-1b7 上验证，出现 held-out perplexity 上升和生成语料印记；额外健康头的单 seed、单列瞬时训练 loss 改善也不能签发通用收益。训练语料、阈值、短训预算与全模型回归均有成本，原文斜率公式/表与“高索引斜率更陡”的归因冲突不在这里采用。质量回退或预算无法摊销时，保留原 heads，或继续采用已验证的 pruning/gating 与实际执行路径，而不是用一张 head-health 图替代质量验收。<!-- source-family:SF-2026-ARXIV-2603-09616 -->

head的干预单位也不必是整个输出上的固定方向。一个受限分支分别拟合可信与扰动activation的混合分布，离线按运输耦合选择目标component，在线依据当前membership实施局部均值修正。[Scalpel的必要机制](https://arxiv.org/html/2602.09541v1)由此区分component概率调节与全head平移；row argmax的映射不是在线执行完整Schrödinger bridge，membership或熵也不是答案truth。组件拟合、probe选择与离线耦合均付费，有限POPE二值人口、head选择和自适应输入仍影响结果，部分模型/切片有反侧。分布漂移或效用回归时应降低/关闭干预，保留原attention与独立输出验证，不由局部混合模型签发事实或安全性。 <!-- source-family:SF-2026-ARXIV-2602-09541 -->

选择干预对象还可以先解释一批样本上的head输出，而不只看attention热图：把unembedding中的语义token方向作为固定字典，用多样本稀疏拟合挑出能解释目标概念方差的heads，再作rescaling或sign inversion。[HeadPursuit的受限对照](https://arxiv.org/html/2510.21518v1#S3)用同layer/count的随机head和LogitLens作反侧，支持有限概念选择的差额，却不证明概念只存这些head；改它们还会改变后续间接贡献。字典不全、线性近似和共享语义会带来旁损，增加颜色词也可能降低整体caption质量；毒性proxy下降不认证全部有害输出被阻断。activation采集、字典筛选/拟合、全部干预与任务/安全回归均计费。选择或行为保持未验时，保原head、较弱干预与独立输出验证，不由少数head可控签发语义真值、无损编辑或安全保证。

<!-- source-family:SF-2025-ARXIV-2510-21518 -->

## 为什么 head 数不是越多越好

给定固定 `d_model`，增加 `H` 通常会减小 `d_h`。更多 heads 提供更多独立路由分布，但每个 head 的表示维度更小。

Head 数还受工程条件约束：

- `H*d_h` 与 projection shape 必须匹配。
- Q/K/V reshape 和 kernel 要支持目标 layout。
- Tensor Parallel 常要求 head 数能被并行度整除。
- Head 太小可能降低 GEMM 或 attention kernel 效率。
- Head 太多会增加 metadata、调度和 KV head 选择复杂度。

因此 `H` 是模型容量、每头维度与执行效率的联合选择。

同一attention预算内，更多head与更宽head还应按目标能力比较，不能只用token平均loss代替长上下文检索。固定总投影宽度与query/KV头数比时，可以减少head数量、增加每头Q/K/V维度，同时基本保持参数、算术与KV元素预算。[从头训练的受限对照](https://arxiv.org/html/2610.32213v1)在相同的混合局部/全局Attention、部分RoPE与训练token条件下，较宽head的长检索均分更高，但最低NTP loss并不总选择它；这不是对所有架构的最优head维度。对称配置的预算匹配也不能移给另加QK或V容量的非对称模型，后者参数与KV预算更大。原比较仍有任务反退，短任务平均不降也不等每个任务无损；评估目标、位置编码和训练阶段应与head配置共同保存。

检索收益也不能全归因于attention投影在长上下文训练中学得更多：把两类Attention的Q/K/V/O矩阵固定在相同PT checkpoint，继续训练其余参数后，宽head的平均优势仍存在。不过head-wise QK-RMSNorm的gain仍更新，输入表示也会变化，所以这不是冻结整个Attention函数，更未单独证明MLP或embedding是唯一原因。Full CPT与Frozen CPT的差同时改变可训参数身份和数量，不能将均分差解释成参数数量的纯因果。该结论来自有限0.6B三run与3B单run、每任务100样本的RULER及特定CPT/SFT协议；不保证所有run/任务/长度单调，也未给出相同预算下的完整kernel延迟或Serving SLO。更宽head若与位置编码、并行整除、kernel或真实任务不合，应保留已验MHA/GQA配置，并分别验长检索、短任务、训练与执行总费用，不由同参数或低loss签发无损与净加速。<!-- source-family:SF-2026-ARXIV-2610-32213 -->

Head预算还可以在同一算子的两条读出分支间分配：分别计算两张softmax图，再用带系数的差分作用于共同Value内容，让较少的第二分支head供多个第一分支复用。这里改变的是差分结构的容量与共享，不是普通GQA只共享KV，也不由“signal/noise”命名证明两个分支已各自识别真实信号和噪声；相减后的系数不再是单一非负概率图。

[Grouped Differential Attention的受限对照](https://arxiv.org/html/2510.06949v1#S2.SS2)提示适度非对称与只扩第一分支可以形成替代配置，但比例过强会退步，数学及其他分项也非全优。成长实验同时改变head数量，不能当纯比例因果；共享索引、V形状和KV数量口径未闭时，不拼成已验实现。全部预训练阶段、投影/差分/归一、状态共享与独立任务回归都计费，匹配声明的FLOPs不等实机无overhead或服务加速；形状、质量或净费用不合时，保留原对称差分或普通MHA/GQA，不由更多有效head或局部均分签发通用最优容量与无损扩张。<!-- source-family:SF-2025-ARXIV-2510-06949 -->

预算也可在层间重新分配，而不要求每层使用相同head数和宽度；还可给某个head拟合较窄的Q/K student，再检验它是否保留所需读出。[受限分配与近似研究](https://arxiv.org/html/2510.03784v1#S4)把信息提取head数、投影宽度和目标tail误差分开，但总attention宽度只是代理，不是相同完整参数、FFN或训练预算，构造上界也不保证SGD达到实际最优。这与后文不改乘积的坐标重写不同：低秩student会引入近似，未旋转QK的SVD不自动覆盖RoPE的全部位置对。即使完整有限logit范围下有按有效support大小约束的softmax扰动界，causal mask/位置bias也须另验；很小的attention-entry MSE仍可能给Value聚合及任务输出带来大误差，不能据此统一削窄后层。投影/SVD、student拟合、各层shape与位置结构、全模型质量回归、训练搜索及真实kernel/KV费用都须计入；条件或净收益不合时保原均匀MHA/GQA或已验压缩，不把局部维度减少当全模型无损加速。<!-- source-family:SF-2025-ARXIV-2510-03784 -->

把多个 heads 放进同一 fused kernel，可以减少中间存储与启动成本，却不能据“最后只有一个聚合输出”就假定任意 dense 多头、跨层计算都能按实例数摊薄。单个 head 难算，不自动证明 `L×H` 个实例同样难算；这需要单独的 direct-sum 论证。[受限理论构造](https://arxiv.org/abs/2603.11332v1)把独立问题编码到各 head 与层，在 sum-aggregation、每 head 宽 `m=Θ(log N)`、`L/H` 与序列长度 `N` 多项式相关、逐项输出误差至多 `1/(10N)` 时，给出基于 3-OV/SETH 假设的 `LHN^(2−o(1))` 最坏情形时间下界。它不是各 head 必须串行的调度定理；concat 推广还要重参数化宽度，不能直接拿论文的 `m` 代替固定 `d_model` 下的 `d_h`，更不证明每个已训练 checkpoint 都没有冗余。<!-- source-family:SF-2026-ARXIV-2603-11332 -->

大宽度分支则把完整 softmax 计算与多个独立矩阵乘积联系起来：允许实数加减乘除及 `exp/ln` 的扩展算术电路，可通过同量级成本抽取偏导恢复各乘积。其 `m=Θ(N)` 构造得到 `LHN^(ω−o(1))−O(LHN²)` 的电路规模下界，其中 `ω` 是矩阵乘法指数，`ω>2` 时前项才支配减项；对象是所有输入与可变权重的精确计算，不是推理时需要执行反向，也不是 Word-RAM、有限精度或生产延迟下界。Full-attention、宽度和最坏情形条件不能自动搬给 causal mask、共享 KV 或实际数据分布。因此，保持原 dense 算子时仍可通过融合、layout 和并行改善常数与 IO；省略计算则须明确近似误差、结构、共享或剪枝合同，并验收质量与总成本。条件不符时保留成熟 dense MHA/GQA，不把理论下界解释为所有加速都不可能，也不让不同计算模型下的一项速度测量反证该定理。

## MHA、MQA、GQA 为什么出现

标准 Multi-Head Attention 中 Query、Key、Value 都有 `H` 个 heads：

```text
MHA: H_q = H_kv = H

Q [B,H,T,d_h]
K [B,H,T,d_h]
V [B,H,T,d_h]
```

自回归推理中，每个 KV head 的历史 K/V 都要进入 KV Cache。为了减少 cache 和 memory bandwidth，可以让 Query heads 共享较少的 K/V heads。

Multi-Query Attention：

```text
MQA: H_q = H, H_kv = 1

Q [B,H,T,d_h]
K [B,1,T,d_h]
V [B,1,T,d_h]
```

Grouped-Query Attention：

```text
GQA: H_q = H, 1 < H_kv < H

Q [B,H,T,d_h]
K [B,H_kv,T,d_h]
V [B,H_kv,T,d_h]
```

GQA 把 Query heads 分组，同一组共享一个 KV head，在 MHA 表达自由度与 MQA cache 效率之间折中。

这里的“共享”是一项架构约束与 inductive bias，不是先证明组内若干 KV heads 数学上相似，再做无损合并。从头训练 GQA 时，每组从一开始就只有一套 `W_K/W_V`，Query heads 会共同适应该表示；把既有 MHA checkpoint 转成 GQA 时，才需要聚合旧 K/V projections 并继续训练，转换结果也不是 runtime 等价改写。

MQA 把约束推到极端：不同 Query heads 仍能产生不同 attention weights，决定“查哪些位置”，但所有 heads 共用同一套 Key 索引特征和 Value 内容表示。GQA 保留多个 KV groups，使不同组还能学习不同的“怎样被匹配”和“取回什么”。所以从 MHA 到 GQA 再到 MQA，是 `H_kv`、KV 带宽与表示瓶颈之间的连续取舍，不是发现所有 KV heads 都相似后的必然终点。

K 与 V 的头数还可以分开选择，而不沿用统一的 `H_kv`：当稀疏 Value 聚合已经较便宜，保留较多 Value heads、合并部分 Key heads，可以继续削减 QK 匹配的成本。这是改变模型表示瓶颈的架构分支，不是对任意 GQA checkpoint 的无损 kernel 改写；若两侧 head 宽均为 `d_h`，每层 KV elements 的一般式为 `B*T*(H_k+H_v)*d_h`，前述公式是 `H_k=H_v=H_kv` 的特例。[SAGA 的受限转换](https://arxiv.org/html/2610.04753v1)通过 logit matching 合并 K、同步重排 Q/V/O 并蒸馏，还为稀疏 PV 使用近似阈值；阈值跨步复用和固定候选 buffer 溢出丢项均改变近似语义，内存安全不等数值无损。短序列的阈值/收集开销及 multi-key retrieval 退步必须保留，长序列计时不能替另一长度的质量验收。转换、蒸馏、阈值与布局适配都付费；匹配质量、检索或实际净费用不合格时保留原 GQA/MHA，而不把更少 Key heads 当作普遍更优的终点。<!-- source-family:SF-2026-ARXIV-2610-04753 -->

除了缩KV，还可在保持每头宽度不变时缩Query头数，并让Q投影与concat后的O输入同时变窄，再映射回原hidden宽；这不同于固定总投影宽、仅把更少heads做得更宽。此时score与Value聚合的工作量随`H_q*N²*d_h`下降，仍为二次序列计算，历史KV却继续由`H_kv`决定。[SQA的受限架构对照](https://arxiv.org/html/2510.01817v1#S3)据此区分全序列计算与Decode带宽目标：对称配置可能比原GQA保留更多KV，Query路由更少也改变表达容量，不能由相同hidden输出或cache大小批准原checkpoint无损转换、两阶段任意切换或同速。短context的小模型质量已有退步，单A100长序列forward收益不验证对应长度的质量、完整训练或服务SLO；减少比例也不能当总成本倍率。原训练/转换、全部投影/FFN、KV与layout及独立质量回归均计费；路由容量、Decode驻留或净收益不合时，保留原MHA/GQA、较温和静态配置和已验稀疏窗口，不以更少Query heads替质量验收。

<!-- source-family:SF-2025-ARXIV-2510-01817 -->

## 一个 GQA 分组例子

假设：

```text
H = 8
H_kv = 2
```

则每个 KV head 服务 4 个 Query heads：

```text
Q heads 0..3 -> KV head 0
Q heads 4..7 -> KV head 1
```

相较 `H_kv=8` 的 MHA，K/V projection 与 cache head 数下降到四分之一。Query 计算仍有 8 个 heads，模型没有减少 Query 路由数。

这不是 runtime 可对任意 MHA checkpoint 无损打开的选项。`H_kv` 决定模型参数 shape 和训练语义，必须由架构与 checkpoint 支持。

## 参数与 KV 状态的连接

忽略 bias，标准 MHA 的四个 projection 参数近似为：

```text
P_MHA ~= 4 * d_model^2
```

这里假设 `H*d_h=d_model`。GQA/MQA 主要减少 K/V projection 输出维度，Query 与 output projection 不一定减少同样比例。

推理 KV Cache 的核心 head 维度则由 `H_kv` 决定：

```text
KV elements per layer ~= 2 * B * T * H_kv * d_h
```

第19章会加入 layer 数 `L`、dtype bytes 和请求生命周期，完整推导 cache 容量。本章只建立模型架构到 `H_kv` 的接口。

减少 KV heads 不是参数共享的唯一轴。每个 head 在 softmax 之前通过 `W_Q W_K^T` 决定匹配，在 softmax 之后通过 `W_V W_O` 影响读出；分别把这些乘积沿 head 轴堆成三阶张量，可以用核心张量与各轴基矩阵联合分解，而非只给每个 head 一张独立低 rank 矩阵。这条分支同时约束 head 与两端特征子空间，rank 决定表达自由度和压缩幅度；指定 rank 下能够表达 MHA/GQA/MLA 的参数形式，不证明任意既有 checkpoint 无需近似、训练即可替换。推理时保存的是两个 down-projection 的 latent，若共享 down projection 才可只存一份；同 rank 的 cache 可以与 MLA 相同，更多 attention 参数节省不再自动增加 KV 节省。<!-- source-family:SF-2026-ARXIV-2603-30033 -->

位置与 kernel 接口也须随这份分解一起验收。原来在每头 Q/K 中间施加 RoPE，不能直接当作因式分解后的无损操作；把旋转移到 latent key 维度可以保留相对位置形式，却改变频率和算子配置，不是原 RoPE checkpoint 的 drop-in 改写。[Tucker 的必要对照](https://arxiv.org/html/2603.30033v1)先形成每头 query 再接共享 latent KV 的 GQA kernel，专用 core kernel 仍属未来工作；从头训练的 1B 模型中，GQA8 的 loss 2.61 对比一个 Tucker 配置的 2.69，参数/iteration 成本降低仍有质量代价。所测单 H100、BF16、batch1、cached length4096 的研究 decode mean 不授生产吞吐或 tail SLO。rank 搜索、初始化/训练、latent 投影与布局转换都付费；质量、位置或 backend 未通过时，保留原 MHA/GQA/MLA，而不是按参数压缩比例推延迟倍数。

压缩宽度之后，还可以在较窄的Q/K/V表示里直接完成标准softmax Attention，再由O映回residual宽度，而不是先重构完整宽度再读取；缩Q总宽与缩KV总宽、共享KV heads仍是不同配置轴。为补窄表示的瓶颈，[一条受限压缩分支](https://arxiv.org/html/2510.04476v1#S2)在Q/K上加入因果局部序列/通道混合及组均值残差，让一半V heads另读前一位置的embedding；这改变了寻址与传值条件，不是既有checkpoint的无损layout开关。卷积首端/跨设备halo、组广播、归一/RoPE与shift状态必须和训练同版；常数长度历史也不等零通信。较窄投影降低主Attention的二次项系数，却不改变序列平方阶或自动保语义容量；按参数和KV匹配后把容量转给MLP/expert，也不是相同compute下孤立替换attention。受测dense配置及V-shift消融仍有质量退步，H100/BF16局部kernel的forward与noncausal backward计时不授causal训练或decode净速，原decode测量尚留后续。全部重训、局部混合、cache/halo、编译融合与独立长窗质量回归都计费；容量、条件或净收益不合时，保原MHA/GQA/MLA或较温和压缩，不由参数/KV比率批准通用TP最优、无损或端到端SLO。<!-- source-family:SF-2025-ARXIV-2510-04476 -->

压缩KV还可以把token身份作为额外的静态条件，而不只改变共享投影的rank：先由当前hidden生成低秩latent，再上投影为KV；各层按tokenID查表、投影成gate，与已展开KV逐元素相乘并归一化后，再分给各head读取。[受限embedding-gate分支](https://arxiv.org/html/2509.16686v1)以更多词表参数和求值换取较窄的动态状态，门并非直接乘在最小latent上，静态身份也不包含全部上下文。若只保存latent与位置旁路，还必须能恢复对应tokenID、gate表和模型版本；不同历史位置的gate及归一项不同，不能无条件沿用普通MLA的固定矩阵吸收。双线性交互的项数不证明任意高阶映射或压缩无损，较少cache元素也不等总驻留或decode更快，局部任务仍有反退。查表/投影、乘法归一、KV重建、加载与传输、训练及完整请求回归都计费；词表、质量或净预算不合时，保留原MLA、较宽latent或完整Attention，不从active参数或cache比例签发端到端SLO。

<!-- source-family:SF-2025-ARXIV-2509-16686 -->

## Multi-Head 与 Tensor Parallel

Attention projection 的 head 维度提供自然切分边界。不同 GPU 可以持有不同 Query/KV heads，局部计算后再在 output projection 周围聚合。

但不能简单认为“一张卡一个 head”。实际 Tensor Parallel 会考虑矩阵 column/row partition、GQA 的 KV replication、head divisibility 和 collective placement。第37章负责完整 TP 机制；本章只指出模型 head layout 会约束并行布局。

## 从共享 KV 到可执行的压缩状态

减少 KV heads 回答了总状态有多大；分布式部署继续追问每个设备究竟要持有、读取多少状态。因而下面两条路线是不同约束下的架构分支，不是 MQA 必然继续替代 GQA 的下一代。

### 压缩状态还必须暴露可执行的分片轴

MQA、GQA 与低秩 KV 压缩都试图减少每个 token 留下的状态，但“总状态更小”不等于“每个设备读取的状态也按并行度下降”。把全部 KV heads 压进一个共享 latent state，在单卡或较小 Tensor Parallel 下很合理；当 Decode 受每个 rank 的 HBM 带宽限制时，这个共享对象却可能需要在每个 rank 复制，形成新的 bandwidth floor。

因此架构压缩还要回答一个运行时问题：压缩后的坐标是否保留了可以映射到设备的 partition axis。一条可行演进是把单个 latent state 分成多个独立 latent heads，每个 head 在本地完成上投影和 Attention，再在输出边界聚合：

```text
shared latent KV
-> multiple latent heads
-> head-to-rank placement
-> local projection and attention
-> output aggregation
```

它以更多 projection、聚合、初始化耦合和 checkpoint/kernel 复杂度，换取 per-rank KV 读取随并行度缩减的可能。增加 latent heads 还会改变多路求和的 variance，不能被当作纯 layout rewrite。反过来，在 TP 较小、通信比 HBM 读取更贵或成熟 kernel 更重要时，单 latent MLA、GQA 乃至 MHA 仍可能是更好的设计。

这里的长期原则是：**模型状态的 shape 同时定义表达空间和系统可分片性。**第37章负责实际 placement 与 collective；本章只负责确保模型架构没有在压缩状态时无意删除运行时所需的切分维度。


### 同一 Attention 权重可以暴露多条 KV 路径，但前提必须在训练时成立

分片轴处理的是跨设备布局；另一类约束来自同一模型在不同硬件上会遇到不同的计算/带宽比例，此时才需要考虑多条预先训练并验证的执行路径。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-15250:start -->
普通 MHA、GQA 与 MQA checkpoint 的投影形状不同，runtime 不能在部署时把它们当成可无损互换的 cache policy。GQLA 的条件分支是在模型设计与训练阶段建立共享权重，使同一 checkpoint 同时支持 MQA-absorb 的 compact-cache 路径和 per-group GQA 的 expanded-cache 路径；runtime 再依据 hardware roofline、Tensor Parallel 布局与当前 memory/compute 压力选择已验收的执行视图。模型权重拥有语义，runtime 只拥有路径选择，不能现场发明新的 attention factorization。

多路径身份必须绑定 checkpoint、group/repetition factor、projection transformation、precision、TP layout 与路径校验结果。compact path 节省 KV 却可能增加 compute，expanded path 反之；训练/转换成本和双路径回归也随之增加。exact-v1 只支持 §3 的 GQLA/TransGQLA 与 §4–5 所测模型和硬件，不证明任意既有 checkpoint 可无损改写。roofline 未校准、路径数值不一致或实现只支持一种布局时，应回退冻结的 MHA/GQA/MQA 单一路径。<!-- source-family:SF-2026-ARXIV-2605-15250 -->
<!-- semantic-body-binding:SF-2026-ARXIV-2605-15250:end -->


## 怎样区分路由分工、参数坐标与行为证据

到这里，多头结构的计算与状态代价已经明确，但一个 head 究竟做了什么，还不能仅由数量、可视化或参数值读出。下面区分三类容易混淆的问题：路由是否有用、训练动力学是否独立，以及参数坐标是否唯一。

### 注意力图与平均传播只是诊断线索

注意力图中看起来不同的读取模式，首先只是待验证的行为线索。把这类诊断量直接变成训练目标，还会改变它原先作为线索的意义。例如，放大 matched 与 mismatched demonstrations 的注意力行距离，可以仅通过把权重集中到不同格式 token 而接近指标上限，并不保证取回了与答案有关的 Value。因而“路由对上下文更敏感”与“模型更会利用上下文”必须由独立行为对照区分；训练代理、测量代理与最终能力验收不能互相替代。这不否定注意力分析，而是要求被直接优化的解释指标重新接受行为检验。

平均 attention 可以解释群体表征传播趋势，但 context-specific routing 与 value computation 位于对平均的 deviation 中；把 mean-field fit 当成单个输入的机制解释，会掩盖稀有 head、token 和样本路径。<!-- source-family:SF-2026-ARXIV-2609-16382 -->

统计分解提供诊断视角，不等于因果证明。有限 corpus/model 且部分 family 需单独处理；个例、安全或精确 attribution 场景应回退真实 activation measurement、ablation 与干预。

解释head还可提出一个可执行替身，而不只给attention图配文字：让程序从原token序列直接产生候选attention矩阵，用原测量样本修订并在留出输入上选proxy，再在真实forward里替换矩阵、保留Value与后续网络，分别观察拟合误差和行为变化。程序能运行只是接口成立，JSD或IoU高只是路由近似；都不证明恢复了原head唯一算法，也不使Value聚合与任务结果自动等价。

[程序化attention的受限对照](https://arxiv.org/html/2606.19317v1#S2)先替换最好拟合的head，仍有大量难以拟合的部分；同分布perplexity、域外选择题与完整生成是不同验收人口，低比例替换的改善还可能来自pruning。模型与简单语料上的局部保留不授全LM符号解释或加速。测量全部maps、模型生成/执行/筛选程序、替换forward与非目标回归均付费；支持、causal mask或行为不稳时，保原head、真实activation干预与独立任务测试，不由可读代码代替机制证据。<!-- source-family:SF-2026-ARXIV-2606-19317 -->

固定 head 身份也不固定它在每个任务中的角色。保持输入事实不变，分别改变任务指令或内部 task state，再比较同一 head 对哪些事实响应、扰动如何传到后续组件，以及替换该 head 怎样影响答案；influence 与 answer importance 是不同干预量，不能靠两张 attention 图或一个总分互代。[有限 graph-task 对照](https://arxiv.org/html/2610.13895v1#S2)中，匹配当前状态的局部 response map 比平均 map 更能预测同prompt干预效果，但影响包含中间组件路径，依赖选定方向、幅度和位置，少数head恢复也只占整体task切换的小部分。配对构题、activation measurement、随机控制与恢复均增加成本；新prompt或任务尚未验证时，保留真实干预和非目标行为回归，不把该局部映射当通用线性回路或选择性安全编辑证书。<!-- source-family:SF-2026-ARXIV-2610-13895 -->

### 几何分离不等于训练独立

即使进一步约束各 head 的 score 或输出方向近似正交，也不能推出它们的训练动力学彼此独立。各 head 仍读取同一 token trajectory，并在共享 residual stream 与最终 loss 中相遇；球面归一化下的径向投影还会把一个 head 的更新影子带入另一个 head 的能量变化。因而，总体能量存在下降方向，不代表每个 head 的局部能量或聚类过程都单调。只有在额外的 Radial Dominance 等充分条件成立时，才能把更强的逐 head 单调性当作理论结论，而不能把它写成真实 Transformer 的普遍事实。<!-- semantic-body-binding:SF-2026-ARXIV-2605-04279 -->

这条边界没有否定 head 正交化：它仍可作为减少表示重叠的 inductive bias。代价是新增约束与优化耦合，且“几何上更分离”仍需任务行为、因果干预和可执行 kernel 分别验收。相关理论主要依赖 sphere-normalized、score symmetry、scalar 或 equiangular 等受限设定，不证明 heads 已获得独立人类功能；条件不成立时，应回到联合系统的 loss、residual state 与端到端行为，而不是据单 head 能量作提交判断。

### 换基等价不等于功能冗余

另一个层次的冗余发生在同一 head 的参数坐标内部，而不是多个 heads 做了相同工作。以下 `W_Q/W_K/W_V` 均指该 head 对应的投影块，而非前文全部 heads 合并后的大矩阵。暂不加入位置旋转和 bias，沿本章行向量记法，任取可逆的 `d_h × d_h` 矩阵 `S`，令 `W_Q' = W_Q S`、`W_K' = W_K S^{-T}`，则 `W_Q' W_K'^T = W_Q S S^{-1} W_K^T = W_Q W_K^T`，所以全部输入的 score 与 attention weights 不变。Value 与该 head 对应的输出块 `W_O^(h) [d_h,d_model]` 也有类似换基：`W_V' = W_V R`、`W_O^(h)' = R^{-1} W_O^(h)`。参数可以不同，执行的函数却相同；这叫参数化的不唯一性，不能据单个坐标大小给特征赋予唯一语义。

这种换基不会自动减少 heads、矩阵 shape 或 FLOPs，也不保证优化器按相同轨迹训练。GQA 共享 K/V 后，组内换基必须共同兼容共享参数；RoPE 又要求变换保留位置旋转结构，不能套用任意可逆矩阵。因此，可辨识程度、head 功能冗余与可兑现的推理加速是三个不同问题：前者要固定参数等价关系，后两者仍须任务因果验证与 checkpoint/kernel 合同。第16章的非线性 FFN 也不能照搬这里两个线性因子的任意换基。[受限证据：QK/OV 因子化与共享结构约束，arXiv:2609.01231v1 §4](https://arxiv.org/html/2609.01231v1)

一般换基不省计算，但已有低秩乘积还可选择一份含identity块的表示：对每头QK或VO乘积，若选出的r行或列确实独立，可写成`[I;C]B`或`B[I,C]`，把原来两份自由因子中的r²个系数改为直接复制。跨head对齐同一组连续坐标位置，再融合切片、重复与乘加，才有机会把代数省项兑现为投影节省，而不是减少heads或序列score的二次项。[BDA首版的受限重写](https://arxiv.org/html/2510.01718v1#S3)仍受位置与数值合同约束：普通RoPE把旋转插在Q/K之间，不能继承未旋转乘积恒等；decoupled配置只能重写non-RoPE通道，VO另行验收。随机矩阵几乎处处满秩不保证训练后basis良态，first/last残差选择也不认证浮点全输出或梯度等价；保内积更不自动保范数、距离型KV策略。单A6000投影kernel与有限PPL/BLEU对照不授完整服务加速，离线分解、layout/kernel、原KV、训练和独立数值/质量回归都付费。位置结构、conditioning或净收益不合时，保留原投影、已验低秩/latent路径与成熟GEMM，不由参数坐标等价批准无损迁移。

<!-- source-family:SF-2025-ARXIV-2510-01718 -->

### 从观察 Head 到有条件地干预轨迹

理解参数等价关系之后，还要区分“解释一个 head”和“修改它来改善输出”。后者多了一份干预收益与副作用都必须验证的责任。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-21770:start -->
固定 activation steering 对所有生成步骤施加同一方向，在错误模式稳定时实现简单；若错误表现为特定 attention head 沿轨迹偏离低维 correctness manifold，这种全程干预会同时扰动原本正确的步骤。一个条件分支把 head-to-manifold distance 当作 trajectory sensor，只在越过校准阈值时把状态投影回已学子空间。距离只拥有 intervention proposal，端到端 verifier 才拥有正确性判定。

该分支需要白盒 activation、对比轨迹、子空间和阈值校准，并增加逐步监测开销；过强投影会损坏正确轨迹。exact-v1 的受测模型、任务和 head 不能证明 correctness manifold 跨模型稳定，也不能把 proximity 当作 correctness certificate。head/任务漂移、阈值失校或 utility regression 超界时，应关闭投影，回退无 steering、较弱静态 steering 或外部 verifier-guided retry。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-21770:end -->

多语言任务还要把语言形式与答案内容作为两个干预目标，而不是给所有失败共用一个“正确性方向”。一条受限诊断分支分别构造含义相同但语言错误的输入、语言正确但含义被破坏的输入，再将干净轨迹的 head activation patch 回对应条件；在 teacher-forced 的参考输出前缀上比较预测变化，用来选择后续 steering 候选。两种 corruption、参考前缀及观察 token 位置共同定义 sensor，不能把位置间的 KL 差或可干预性直接称为模型自然使用的唯一语言无关 code。部署时应分别验语言遵循与内容正确性，定位有效也不保证自由生成有效：[必要机制与反侧](https://arxiv.org/html/2602.04613v1)中 token 0 也可能有用，低资源语言和较强缩放仍会失败。对比构造、白盒 patch、位置与强度校准增加成本；目标与 utility 验收不成立时，关闭该干预，回退显式语言指令、较弱 steering 或无 steering，而不继承普遍的少量 head 控制保证。<!-- source-family:SF-2026-ARXIV-2602-04613 -->

干预粒度也不一定是整个 head 或整层向量。用列向量记法写线性输出 `y = Σ_i x_i W[:,i]`，每项由一个输入 scalar 与对应权重列组成；它与本章行向量 `x W` 的记法互为转置，这种 activation unit（AU）不是 neuron、head 或 SAE feature 的同义词。一条受限分支先在目标/非目标对比输入中按 activation 差的符号一致性选 AU，再按排名给当前输入 scalar 施加 `x_i → (1+γ_i)x_i` 的缩放。排序只是干预候选，不识别唯一内部因果；负向 γ 足够大时 `1+γ_i` 可以为负，不能称为保符号控制。对比 pairs、矩阵/层坐标、选择数 k 与强度 α 都需要任务内校准，细粒度选择仍增加定位和监测成本，也可能伤害无关能力；更少单元不保证更好。独立目标与 utility 回归失效时应关闭该分支，回退无 steering、较弱粗粒度 steering 或外部 verifier，而不由受限激活排序签发功能控制保证。<!-- source-family:SF-2026-ARXIV-2602-04428 -->


## 本章在知识树中的位置

```text
Single-head Self Attention
-> H parallel routing subspaces
-> concat [B,T,H*d_h]
-> output projection [B,T,d_model]
-> MHA / GQA / MQA
-> Transformer Layer / KV Cache
```

第14章定义单 head 路由，本章定义多 head 组合。多个位置的信息已经汇入当前位置，但还需要在这个位置内部组合特征、形成非线性变换；第16章接手这一问题，第17章再将两者组成完整 layer。第19章使用本章的 `H_kv` 推导运行时状态。

## 自检问题

1. 把单 head 维度做大与增加多个 heads 有什么结构差异？
2. Q/K/V 怎样从 `[B,T,d_model]` reshape 为 `[B,H,T,d_h]`？
3. 为什么 head outputs 先 concat 再经过 `W_O`？
4. 固定 `d_model` 时，增加 `H` 会怎样改变 `d_h`？
5. MHA、MQA、GQA 的 `H_kv` 分别是多少？
6. `H=8,H_kv=2` 时 Query heads 如何分组？
7. GQA 主要减少哪部分参数和运行时状态？
8. 为什么 runtime 不能为任意 checkpoint 无损切换 MHA 到 MQA？
9. Head layout 为什么会约束 Tensor Parallel？
10. Attention head 的可视化为什么不等于完整机制解释？
11. 为什么同一 loss 可以让 heads 分化，却不能保证每个 head 都独立有效？
12. GQA 的共享为什么是训练约束，而不是组内 KV 相似性的定理？

## 小结

Multi-Head Attention 让多个投影子空间并行构造上下文路由，再通过 concat 和 output projection 恢复统一 residual stream。它扩展了单 head 的表达路径，同时引入 head dimension、layout 与并行约束。

MQA 和 GQA 进一步把 Query head 数与 KV head 数解耦，用共享 K/V 换取更低 KV Cache 和 memory bandwidth。这条模型架构选择会在第19章变成具体推理容量。

## Review notes

本人注：`SF-2025-ARXIV-2510-18358` — Locke，Daily2025-10-23补Oct22；exact-v1 §4.2–4.3/5.1–5.3必要，2+1+2=5，仅member/head轴与共享MLP差额深入。保共同基座不等独立ensemble、函数非严格保持、分类反退及训练/所有分支全费，不采普适noise定理或通用单模型时延；未核实现/复现。整体PRE/SAVE/全自读/sole actualPOST仅本日实际层。

- `SF-2026-ARXIV-2610-32213`，Daily2026-10-27；exact-v1 §2/3/5.1及A3/B3/B4关键配置/完整表与直接反侧首次必要，未采用全部retrievalhead阈值分析/entropy或representation因果/逐图像素。R163 3+1+2=6，仅同预算headallocation的NTP-v-retrieval排序与attentionprojection更新归因纠错深入；CPT tokenmean NTP不是只测短context。保3:1SWA/FA、partialRoPE64/θ100、100BPT/8BCPT、固定GQAratio/不把asymmetric1.25×KV配置当matched、0.6B三runSD/3B单run、RULER100/task及Full/Frozen同PT配对；QK-RMSNorm仍可训、冻结projection非固定attentionmap、trainablecount/identity未隔离、任务/seed/长度反侧与无kernel/SLO。未读全probe/图像素/代码或复现；PRE/SAVE/selfread/solePOST仅后到真实层。

- `SF-2025-ARXIV-2510-03511` — Arendt，Daily2025-10-08补Oct07；原7，直接采用root R245唯一exact-v1 S3–4/S5.1–2/C/D1–3/G/H/I2/J2/M4/T7必要，不第二Methods。仅有限群frame/head轴及相对群共享参数差额；保R∈G非全SO3/反射、APE/外frame破对称、固定总宽/每frame容量与lift费、恒key/no-softmax线性非一般Attention重排、群/任务反退与配置冲突/全搜索费。不采全Euclidean/通用净速或Science因果，未核实现/全部像素/训练复现；PRE/SAVE/fullselfread/solePOST只本日canonical真实后到层，不以本注预签。

- `SF-2025-ARXIV-2510-04476` — Arendt，Daily2025-10-08补Oct07；原2+2+3=7，直接采用root R187首次exact-v1 S2–5/T2–5/B1/D1必要，不第二Methods；HTML A1仅header未冒code已核。只latent内完整Attention与QK局部/组均值、半头V-shift的补偿结构，区别SQA缩Hq/普通KV共享；保Hq/Hkv/dh与bytes分责、MLP/expert重分非equalcompute、dense/组件反退/T3T4 loss不一/MoE300vs350M口径、H100BF16局部kernel与noncausal backward、decode未测、TP/CP/halo及全部费用。不采无损转换/通用TP最优/zero通信或全模型净速，未核像素/kernel/code/集群复现。A179原稿经R195整体PRE、A181真实SAVE/fullselfread/QA后，R196唯一actualPOST通过，I49生效/指定窄位释放；本尾仅同步既成事实，不重POST或授DAY。

- `SF-2025-ARXIV-2510-06949` — Daily2025-10-10补Oct09BJT；[GDA exact-v1](https://arxiv.org/html/2510.06949v1)，2+1+2=5，作者A16唯一首次必要§2–3/T1–4/Limitations。仅双softmax差分的非对称head共享/分支增长差额，保noise名称非truth、Eq7索引/V与T1KV12未闭、GSM8K/Hella反退、成长40vs32heads与160B+80B全费，不采完整recipe/无overhead/最优比例或净SLO。未核实现/复现；PRE/SAVE/fullselfread/唯一POST仅本日实际后到，不预签。 Jason R25整体PRE、实际SAVE/完整自读/限定QA及R27唯一actualPOST已通过；窄位释放，仅同步既成状态。

- `SF-2025-ARXIV-2510-03784` — Arendt，Daily2025-10-08补Oct07；原2+2+3=7，直接采用root R75首次exact-v1 S3–7/B/C/D/F必要，不第二Methods。仅层间head/宽度分配及单head低秩student分层验收；保D为width代理非全param/compute、构造非SGD、完整finite-logit/effective-support限制、漏R/causal反例及attention MSE非Value/task误差，RoPE/SVD/F sweep混杂与全部训练/拟合/搜索费。不授通用最优、后层皆瘦、全模型无损或净速，未核像素/代码/复现；root R81实际owner/原稿整体PRE直接窄授，作者真实SAVE/fullselfread后root R83唯一actualPOST通过，指定窄位即时释放；仅同步既成末态，不预DAY。

- `SF-2025-ARXIV-2510-01817` — Hilbert，Daily2025-10-04补Oct03；SQA exact-v1 §3–6/表1–3必要，2+1+2=5，固定dhead缩Q/O与Hq算力/Hkv驻留差额深入。保二次长度/整数分组、表达改变与短质量长forward分账、同KV非同速/多KV反侧和所有训练转换费用；不授drop-in无损、动态phase已实现、大小模型质量保持或全训练/生产净速。未核代码/全部图像素/复现；PRE/POST只按唯一reader实际记录同步。

- `SF-2025-ARXIV-2510-01718` — Hilbert，Daily2025-10-04补Oct03；BDA exact-v1 §3/Alg1–5/4.1–4.2/5/AppB–D必要，2+2+2=6，identity-block低秩乘积/连续坐标执行gap深入。保独立basis/数值残差与RoPE/非旋转通道、内积非范数、投影非整服务、PPL非严格相同/梯度不等与全费；不采architecture-agnostic lossless、几乎处处满秩代conditioning、所有KV压缩兼容或免训练成本。未核AppA全证明/4.3全部pruning/代码/全部图像素/复现；PRE/POST只同步唯一reader实际记录。

- `SF-2025-ARXIV-2509-16686` — Socrates，Daily2025-09-24补Sep23；[EG-MLA exact-v1](https://arxiv.org/html/2509.16686v1)方法/式1–8、直接实验与效率/必要A/C/F，2+1+2=5，作者15首备→Helmholtz R16一次actual必要采用，R12日门/原分复用。只采tokenID静态gate与contextualKV参数化/动态静态容量分责；保固定吸收/满rank二次与分片sum-concat桥未证、总参数/active不同、任务/decode反退及全部费用，不采完整实现或通用精确并行recipe、无损压缩/零额外计算/SLO。未核全部附件、像素、代码或复现；作者18原三项/Helmholtz R20整体纯PRE通过，root本轮fresh明确正文/本人注新窄授后已真实保存，完整新增/直接两侧/本人注已自读，Helmholtz R160唯一actualPOST已实际通过，I1生效且指定正文/本人注窄位释放；本尾仅同步既成行政事实，不第三Source/PRE/POST或授DAY。

- `SF-2026-ARXIV-2604-22583` — Daily2026-04-28补Apr27；2+1+2=5，R28.25实际IV～VI必要Source/date；howmany预算与whichhead、soft全算训练/hard推理消费资格，entropy符号/最少一head/全FLOPs和碳代理冲突隔离，固定H与真实kernel/质量回退近文。reader actual owner/逐字PRE通过，root授指定单段+本人注窄lease；作者已保存并顺读完整邻接；reader R28.39实际非writer POST通过，root接纳并释放指定窄lease，仅行政同步本人注。未核实现/复现，不授DAY。

- `SF-2026-ARXIV-2603-11332` — 2026-03-14 补查；[exact-v1 PDF](https://arxiv.org/pdf/2603.11332v1) §2.1–2.2/Definitions2.7–2.8、Theorems3.1/4.4/5.1、必要梯度抽取接口、§6与AppendixC。2+2+2=6，具体长期缺口定点深入；sum/concat宽度重参数化、1/(10N)逐项误差、可变W/X、exact-real eAC及减项保留，不授causal/GQA、Word-RAM、硬件延迟或固定checkpoint保证。mar14_supplement 必要Source/实际owner提案与root实际独立原证/完整H选择至MHA邻接通过后窄写；mar14_supplement 已实际回对必要原证并顺读新增正文、完整局部邻接及本人末注，非writer POST通过、窄锁释放，不授日级完成。未核代码或复现，不重复推导全部证明。

- `SF-2026-ARXIV-2603-09616` — Daily `2026-03-12`补查；[exact-v1](https://arxiv.org/html/2603.09616v1) §3、§4.1–4.7、§5.1–5.5/Appendix B–C。2+1+3=6，中心位置归因反侧额外深入；只采用目标 QKV 重初/output 置零/gradient mask 短训与冻结参数不冻结共享输入的条件分支。health/任务效用分账、held-out 与语料印记反侧、单 seed 与有限模型边界近文；斜率公式/表冲突隔离。C4 validation split 用于训练，Table3 所谓 held-out 样本划分未由本轮实现核验，不把局部 PPL 写作独立泛化认证。未执行代码/复现实验；必要 Source 与逐字 PRE 由非作者 review_mar12 实际核通过；root 窄写后 review_mar12 已实际顺读新正文、完整局部邻接与自身末注并回对必要原证，POST 通过，不授日级完成。

- `SF-2026-ARXIV-2602-21371`：exact-v1 §4、实验与local/global预算说明；只采用softmax前head混合/虚拟位置与P²成本分责。图示和方法window缩放不同，不混用；理想无position证明不授RoPE转换，未核实现或复现。 非原 packet 作者必要原证/actual owner PRE 与窄写完成；root 已实际顺读正文、完整邻接与自身末注，POST 通过。

本章只扩展多头结构，不重复第14章 softmax 小例子，也不提前展开第19章完整 KV Cache 容量。后续 Review 应继续区分 Query head 与 KV head，并以 checkpoint config 核验 `H`、`H_kv` 和 `d_h`。

- `SF-2026-ARXIV-2605-04279`（Status: Experimental）：[exact-v1](https://arxiv.org/html/2605.04279v1) 支持在论文假设下区分总能量梯度流、per-head monotonicity 与 radial-shadow coupling；Radial Dominance 是充分条件。证据不支持把受限动力学外推为任意真实 Transformer 的 head 独立性、功能分工或训练保证。

Primary-source 校验入口：

- Attention Sensitivity Is Not Enough（Status: Experimental）：https://arxiv.org/html/2609.00064v1 。§3–5 的单模型受控实验支持注意力代理优化与行为改善不等价；分离 regularizer/evaluation loader 后仍须保留单模型、主要单 seed 与有限任务边界，不据此声称全部 in-context learning 消失或某一种 anchoring 独有优势。

- Multi-Head Low-Rank Attention（Status: Experimental）: https://arxiv.org/abs/2603.02188

- Ashish Vaswani et al., "Attention Is All You Need", 2017: https://arxiv.org/abs/1706.03762
- Paul Michel et al., "Are Sixteen Heads Really Better than One?", 2019: https://arxiv.org/abs/1905.10650
- Noam Shazeer, "Fast Transformer Decoding: One Write-Head is All You Need", 2019: https://arxiv.org/abs/1911.02150
- Joshua Ainslie et al., "GQA: Training Generalized Multi-Query Transformer Models from Multi-Head Checkpoints", 2023: https://arxiv.org/abs/2305.13245

- `SF-2026-ARXIV-2602-04428` — Daily `2026-02-06`；[AUSteer exact-v1](https://arxiv.org/html/2602.04428v1) §3–5及Appendix B/C，2+2+2=6，仅对 scalar-granularity steering 与成本边界的具体缺口深入。AU 是输入 scalar × 权重列，contrastive sign-consistency 与排名缩放不证明 neuron/head/SAE 等价或内部唯一因果；负缩放不授保符号，k/α 任务相关，部分 utility 切片退步保留。激活数量与跨实现 baseline 不作端到端速度证据，不采用普遍 fewer-is-better 或全附录理论。root 必要原源→具体 owner 已核并授窄锁；root 实际正文/279–299前后邻接及341源注 POST 通过，日级 Gate 待验，未复现实验。

- `SF-2026-ARXIV-2602-04613` — Daily `2026-02-06`；[Meaning and Language exact-v1](https://arxiv.org/html/2602.04613v1) §3–6。原2+2+2=6，具体双corruption × teacher-forced观察位置接口缺口深入；语言/含义分别构造与输出验收，patch/位置KL不授唯一内部code或普遍1%控制。token0、低资源语言、强α及utility反侧和白盒校准成本保留。未运行代码或复现；root实际必要原源/owner写前通过，root实际Ch15 275–301含287新段及345末注POST通过，日级Gate未验。

- `SF-2026-ARXIV-2602-09541` — Daily `2026-02-12`补遗漏；[exact-v1](https://arxiv.org/html/2602.09541v1)。本日具名必要方法、关键评价与直接反侧由root独立Source限定通过，actual owner/局部邻接及逐字拟文PRE通过后授窄锁；作者已写最小差额，review_20260214非作者实际新正文、完整局部邻接及本人末注POST通过，窄锁释放，不授DAY。原件与配置/中心争议边界见本日同名前缀review笔记；未核artifact或复现。

- `SF-2026-ARXIV-2603-08343` — Daily `2026-03-11`补遗漏；[exact-v1](https://arxiv.org/html/2603.08343v1) §4–6：固定 head-mixing basis 与可学习 affine 是改变架构自由度的替代分支，不是任意 checkpoint 的等价替换。保留小模型质量范围、随机初始化大配置与实际 kernel 成本边界；root 已读必要方法、评价与反侧，并核 Ch14/16 交接后写入正文。非写入者 supplement_20260311 已实际回对原证并顺读新增两段、完整局部邻接与末注，写后复核通过，不授日级完成；未运行代码或复现实验。

- `SF-2026-ARXIV-2603-30033` — Daily `2026-04-02`补`04-01`；[exact-v1](https://arxiv.org/html/2603.30033v1) §2 张量参数族、§3 KV/latentRoPE/kernel 接口、§4 Table3与相关质量/配置，`2+2+2=6`，具体三轴参数化缺口必要加深。只采 head 与特征轴共享及参数/cache分账；同rank MLA cache、latent旋转改变频率、research kernel和有限训练质量反退近文。不照抄 Eq9/13 记号为完整实现，不授任意checkpoint等价、参数比例延迟倍数或生产SLO；未核代码或复现。

- `SF-2026-ARXIV-2610-13895` — Daily2026-10-13，窗10-12；[exact-v1](https://arxiv.org/html/2610.13895v1)必要位置、采用边界与actual-owner差额见[本日模型证据](../../papers/2026/10/_sources/daily-20261013/model-evidence.md)。today_models准备必要Source/逐字PRE，root独立定点Source/PRE通过后授本局部与本人末注窄锁；today_models已最小写入，root已实际顺读新增正文、完整局部邻接、diff及本人末注，nonwriter POST通过，窄锁释放，不授DAY。保正文限定与原路径，未核代码、复现或生产SLO。

- `SF-2026-ARXIV-2610-04753` — Daily2026-10-07，Oct6自然日；[exact-v1](https://arxiv.org/html/2610.04753v1)必要机制/转换/阈值及短序列、multi-key反侧，2+2+2=6。仅Hk/Hv解耦和近似/转换分责，非无损runtime替换；root R7必要Source/date/owner通过，本稿literal PRE及实际POST另记，未核代码或复现，不授DAY。

- `SF-2025-ARXIV-2510-21518`：Daily2025-10-28补Oct27；exact-v1§3–5/限制必要、2+1+2=5，安全干预深入。writer支持/反侧待sole校准；仅SOMP语义字典选择head，保随机layer控制/间接作用/词与分类器proxy、CIDEr旁损与全费，不采唯一因果或安全归零。未核实现/复现，完整PRE/SAVE/全自读/solePOST只本日后到事实。
