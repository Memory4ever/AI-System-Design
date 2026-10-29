# 第16章 Feed Forward / MLP

**Knowledge Tree:** Part II 模型：一个 Token 如何变成答案
**Stable Knowledge Node ID:** `MODEL-FFN`
**Legacy Chapter:** Ch16
**Status:** Draft

**Roadmap Intent:** Attention 负责信息混合，MLP 负责非线性变换与知识存储。

## 本章要回答的问题

Attention 已经让 token 读取上下文，为什么每个 Transformer block 还要加入参数量和计算量都很大的 Feed Forward Network？MLP 在 token 维度上不交换信息，它究竟提供了什么？

本章的核心判断是：**Attention 负责跨 token 路由，MLP 负责对每个位置的上下文状态独立执行高容量非线性变换。**它可以形成任务相关特征和事实关联，但不能被简单描述成可逐条读取的人类知识数据库。

本章使用 `B` 表示 batch size，`T` 表示 sequence length，`d_model` 表示 hidden dimension，`d_ff` 表示 MLP 中间维度。

## 只有 Attention 会缺少什么

Attention 的核心输出是 Value 的加权组合。即使 Q/K/V projection 是可学习线性变换，聚合本身仍主要在已有 token states 之间搬运和混合信息。

模型还需要在每个位置上产生新的非线性特征：放大某些组合、抑制另一些组合，并把上下文证据映射到下一层更有用的表示。

非线性变换出现的位置也需要随输入粒度检验，而不只是统计一共多少个 FFN。当一个符号被展开成多个空间 token，首轮 Attention 接收到的可能仍是尚未形成局部特征的线性输入；在聚合前先做逐位置非线性变换，是不同于只在聚合后处理的设计假设。[有限视觉算术 diffusion 对照](https://arxiv.org/html/2604.17673v1)中，单层 Attention→FFN 在较细 tokenization 下失败，前置 FFN 或加深到两层可以恢复；它不证明所有 Transformer 都必须采用 FFN sandwich，也不由 Fourier 表征吻合推出唯一因果电路。输入拆分、深度、参数/训练和采样预算、独立任务结果应一起比较；更细 token 与额外变换都付费，原 tokenization 或更多层已够用时仍可保留标准交替，不按这一合成任务的成功直接替换生产 block。<!-- source-family:SF-2026-ARXIV-2604-17673 -->

朴素方案是继续堆叠更多 Attention。这样能反复交换信息，却不一定提供足够的逐位置非线性容量。Transformer 因而交替使用两类操作：

```text
Attention  across tokens
MLP        within each token position
```

## 标准两层 FFN

输入 hidden states 为：

```text
X shape = [B,T,d_model]
```

`d_ff` 通常大于 `d_model`。两层 FFN 可写为：

```text
U = X W_up + b_up
A = activation(U)
Y = A W_down + b_down
```

其中：

```text
W_up   [d_model,d_ff]
b_up   [d_ff]
W_down [d_ff,d_model]
b_down [d_model]

U [B,T,d_ff]
A [B,T,d_ff]
Y [B,T,d_model]
```

同一组权重应用于 batch 中每个 token position。MLP 不沿 `T` 维混合，所以每个位置可并行执行。

## 为什么先扩维再压回

如果只做一个 `d_model x d_model` 线性变换，并且没有 activation，它可以与其他线性 projection 合并，不能形成新的非线性函数类别。

扩展到更大的 `d_ff`，让模型在高维中构造更多中间 features；activation 引入条件选择；`W_down` 再把这些 features 组合回 residual stream。

可以把它理解为：

```text
d_model state
-> many candidate features in d_ff
-> nonlinear gating / activation
-> recombine into d_model
```

这只是计算直觉。某个中间 neuron 是否稳定对应一个人类概念，需要因果实验，不能从结构本身推出。

扩维是否带来可用的新方向，可以先在固定输入人口与采样位置上测中间activation的中心化协方差，再比较参与率、谱熵及主谱与尾部随宽度怎样变化。[受限FFN谱对照](https://arxiv.org/html/2510.00537v1#S3)提供了这条诊断轴，而不是把参数数或一个effective-rank直接改名任务容量。样本数/相关性、中心化、gate前后位置和down projection都会影响解释；低方差方向仍可能被后层放大或承载罕见任务，局部谱与perplexity相关不授删尾、剪宽或改Norm的因果权限。均匀谱本就能使文中合成rank指标取高值，不能由此认证“既不坍塌也不过度分散”的最佳分配。采集、协方差/特征分解、完整训练与width/recipe搜索及任务回归都付费；测量、质量或净预算不合时，保留成熟dense/gated宽度与实际同预算对照，不以一份低rank或好看的谱替代函数和最终行为验收。<!-- source-family:SF-2025-ARXIV-2510-00537 -->

这个计算直觉还要区分输入空间与参数空间：对ReLU这类分段线性activation，固定同一输入区域的binary gate，会让该FFN对输入表现为affine map，却不让同时更新的多层权重变成一个线性参数：在正区域固定gate的标量两层例中，两组权重`(1,1)`与`(3,3)`的输出平均为`5x`，平均权重`(2,2)`的输出却是`4x`。这是由本章两层乘积直接得到的数学边界，不是某篇论文的平均模型保证；只有其余变换与gate固定、仅一个线性参数块变化时，才有相应的函数平均条件。[一个有限DualCopy提案](https://arxiv.org/html/2604.02990v1#S3)将冻结结构副本产生的binarymask与可训练定量副本分开，后者才参与跨客户端平均；它用双份权重储存与额外结构前向换固定选择路径，trainable数并不因此减半。所测CNN的warm-start/central calibration和部分反退只支持这项条件设计，不授Transformer/MoE迁移、joint参数平均等函数平均或全域收敛。gate或目标分布需要变化时，保留原activation/完整微调与独立质量验收，不能仅因“区域内线性”签发合并正确性。<!-- source-family:SF-2026-ARXIV-2604-02990 -->

## 一个逐位置小例子

取单个 token state：

```text
x = [1,-1]          d_model=2
```

令：

```text
W_up = [
  [1,0,1],
  [0,1,1]
]                    shape [2,3]
```

忽略 bias，得到：

```text
u = x W_up = [1,-1,0]
```

使用 ReLU：

```text
a = ReLU(u) = [1,0,0]
```

再令：

```text
W_down = [
  [1,0],
  [0,1],
  [1,1]
]                    shape [3,2]
```

输出：

```text
y = a W_down = [1,0]
```

如果 batch 中另一个 token 有不同 `x`，它使用同一组矩阵独立计算。例子展示 activation 如何选择中间 features，没有发生 token 间读取。

## Activation 改变条件计算

早期 Transformer 使用 ReLU，后续模型常使用 GELU、SiLU 或 gated variants。Activation 决定中间特征怎样被平滑或硬性抑制。

ReLU：

```text
ReLU(x) = max(0,x)
```

SiLU：

```text
SiLU(x) = x * sigmoid(x)
```

不同 activation 的数值范围、平滑性和 kernel 支持会影响训练与执行，但不能脱离具体模型声称某一种始终更好。

非线性也可以由投影后的Gaussian响应构成：先对输入作可学习affine投影，再用`exp(-y²/2)`形成平滑响应，多个分量线性组合；不约束混合系数为概率时，它就是一类函数参数化，不是已归一化的density。[GMNM的受限提案](https://arxiv.org/html/2510.06660v1#S3)印式中的连续线性投影可合为一次affine，随后外平方的quadratic rank至多1，不能直接替代任意高维正定Mahalanobis；若中间另有非线性，必须明确实际算子，不能借未取得的证明补齐。有限CNN head/AE channel重权和LSTM对照不认证LLM全FFN的表达、训练或效率，缩卷积匹配参数也改变了另一条件。全部投影/指数、宽度与kernel、选参/训练和独立任务回归均付费；算子或净质量不合时保ReLU/SiLU、普通MLP或GLU，不由Gaussian名称、逼近定理借用或局部最小loss批准通用收敛与净速。<!-- source-family:SF-2025-ARXIV-2510-06660 -->

## GLU 与 SwiGLU 为什么多一条分支

Gated Linear Unit 类结构让一条分支产生候选内容，另一条分支产生 gate。常见抽象形式：

```text
U = X W_up
G = X W_gate
A = activation(G) elementwise_mul U
Y = A W_down
```

Shape 为：

```text
U,G,A [B,T,d_ff]
Y       [B,T,d_model]
```

SwiGLU 使用 SiLU 作为 gate activation：

```text
SwiGLU(X) = SiLU(X W_gate) elementwise_mul (X W_up)
```

Gate 允许模型根据当前 token state 动态调节哪些 candidate features 通过。代价是多一个 `d_model x d_ff` projection，因此实际模型常调整 `d_ff`，在参数预算下比较，而不是保持所有维度不变。

Gate还应与可执行的activation sparsity分开：非ReLU的值不必精确为零，仍可在指定质量容差内删去一部分小幅分量；一个[受限FFN比较](https://arxiv.org/html/2509.00454v1)按保留L1质量改变mask，再分别测input、gate和相乘后intermediate的任务退化。最稀疏的位置未必最省计算：等intermediate生成后再删，up/gate投影已经付费；从input提前选列影响更多后续工作，若靠predictor预知intermediate支持，还要支付预测与误选成本。99%的平均任务工作点不是每个token或任务的保证，阈值也随模型、训练recipe、位置与数据变化；outlier和有限精度还会改变可见小值。应把mask地址/规则、剩余质量与真正跳过的矩阵工作分别保存，完整选择、预测、索引与回归均计费；任务或净收益失配时，提高保留下限并回dense/已验稀疏路径，不由较高零比例宣布更强语义能力或实际加速，物理layout与kernel由第49章承接。
<!-- source-family:SF-2025-ARXIV-2509-00454 -->

稀疏门控的验收还需按层、phase与任务拆开：一个受限bank-wise分支为每层增加低秩predictor，在固定channel bank内只保部分通道，hardforward配softsurrogate继续训练。[局部fallback对照](https://arxiv.org/html/2606.10722v1#S6.SS2)中，短任务和整体长窗均值接近dense，仍可在特定长CWE读出出现cliff；只将一层的prompt末问答后缀换成校准denseactivation，可救回部分CWE，却不修NIAH且伤MMLU，不能把它叫恢复全部记忆或通用长窗补丁。应共同记录predictor、bank/mask、layer、prefill/decode与校准人口，分别验远程检索、局部读出和短任务；GPU若仍先算denseup/gate，activechannel少也不省这两项投影。预测/选择、稀疏布局、额外参数/训练、fallback与双侧回归都计费；读出、质量或真实省算不合时，保留原dense/较轻稀疏和不启局部修补，不由较低loss、平均稀疏率或一个召回恢复点批准能力保持。<!-- source-family:SF-2026-ARXIV-2606-10722 -->

当同一基础模型要随任务、风格或 persona 切换时，还可固定主权重，把条件控制放到 activation 的斜率：以条件文本作为 query、当前层状态作为 key/value 做低维 cross-attention，加层身份后生成相对 1 的偏移 beta，再以 `x*sigmoid((1+beta)*x)` 控制 SwiGLU gate，beta=0 回到原 SiLU。给定控制量后的 FFN 仍逐位置执行，但控制器读取条件与序列状态，整条适配路径不能再被描述成只有当前 token 的局部非线性。这以新增控制器、条件版本耦合和每层执行开销换少量可训练参数；冻结 base 不保证不遗忘或遵从任意 persona，条件错配、held-out 任务退步或额外费用不合时，保留原 SiLU/普通 prompt 或独立适配。有限 Llama/Mistral 对照仅证明这条控制接口可行，不授普遍优势或推理加速。[受限证据](https://arxiv.org/html/2605.01973v1) <!-- source-family:SF-2026-ARXIV-2605-01973 -->

## 参数量与 FLOPs

忽略 bias，标准两层 MLP 参数量约为：

```text
P_FFN ~= 2 * d_model * d_ff
```

Gated MLP 约为：

```text
P_gated ~= 3 * d_model * d_ff
```

每个 token 都执行这些 dense projections，因此计算随 `B*T` 近似线性增长：

```text
FLOPs_FFN per layer ~ O(B*T*d_model*d_ff)
```

Attention 对 `T` 有成对项，MLP 对 `T` 近似线性，但 `d_ff` 往往较大。实际哪个模块更耗时取决于 sequence length、模型 shape、precision、kernel 和硬件，不能只比较复杂度阶数。

两条 gated 分支也不必都由当前 hidden state 做 dense projection。一个替代分支将 candidate 内容改成按原始 token ID 和 layer 寻址的表 `U_layer[token]`，仍用 `SiLU(X W_gate)` 根据当前上下文筛选它，再经 `W_down` 返回 residual stream。这里减少的是 up projection 的计算，不是删除上下文：静态 candidate 与动态 gate 分责；用同样的表替换 gate，或保留 up 只另加表，并不具有相同的函数与训练行为。[STEM 的受限消融](https://arxiv.org/html/2601.10639v1)支持这一接口区别，不证明任意模型均可无损替换。<!-- source-family:SF-2026-ARXIV-2601-10639 -->

代价从每 token 的投影转向约 `V*d_ff*L` 的表存储、训练 optimizer state 与表项搬运，tokenizer 和 layer identity 因而成为地址的一部分。已知输入 ID 可以预取、去重或缓存表项；Decode 的下一个 token 要等当前完整 forward 后才确定，不能把它当作事先已知。CPU offload 还支付通信、cache miss 与更新回写成本，条件命中率和理论 FLOPs 都不能认证端到端延迟。350M/1B、受控 tokens/FLOPs 的局部结果不授生产 SLO 或通用长上下文无损；存储与通信不合算、context gate 失配或质量退步时，成熟 dense/gated FFN 仍是合理选择，而不是所有 FFN 必须转成查表。

有了可寻址表，也不能把行局部更新当成行为局部写入：地址复用、动态 gate 与 shared readout 仍会把变化传到未写实体；允许同时更新 shared projection 又是另一份写权限。[受限后挂记忆对照](https://arxiv.org/html/2610.21553v1)中，训练 completion 全命中仍伴随新问法严格匹配失败和未写实体 intrusion，词面或首 token 命中不能认证完整事实已经接入。对 mounted pre-write 模块的 residual anchoring 只保护指定 reference 切片，不等于原基座全行为保持；应分别检查训练表达、新问法、未写实体、其他关系与完整 continuation。地址表及 dense optimizer state、额外 anchor 前向与回归都计费，行梯度 mask 不自动带来稀疏状态内存；语义转移或保留不通过时，保留原 checkpoint、限制写权限或使用可追溯外部记忆。<!-- source-family:SF-2026-ARXIV-2610-21553 -->

### 相同预算也不等于相同训练行为

参数和 FLOPs 让比较有了共同尺度，但它们仍不能回答两条分支怎样共同学习。因此还要把结构的表达差异与特定训练条件下的证据分开。

这个乘法不能只解释成“多一个 gate”。非 gated FFN 依靠 activation 后的加性组合，GLU 则让两条可学习分支共同决定局部 kernel 与 conditioning，因而改变训练可达的函数区域。旧 FFN 在参数、kernel 与稳定性预算更紧时仍是合理基线；gated 分支获得更强的条件交互，却增加 projection、初始化耦合和执行成本，conditioning 变差时应回退非 gated FFN 或缩小 gate branch。

`arXiv:2605.20749v1` 的 §4 分析与 §3.3、§5、Appendix C 实验只支持 NTK/two-layer 及作者规模下的可达性差异；§6 不证明 SwiGLU 在所有深度、优化器或硬件上都更优。

<!-- source-family:SF-2026-ARXIV-2605-20749 -->

更强的等价条件也要谨慎：两种参数化可以在 change-of-basis 后计算完全相同的函数，却不在各自默认的 Euclidean gradient 下走同一训练路径。若 `w=A^T u`，梯度满足 `grad_u=A grad_w`；在一个基底做普通下降，换到另一个基底就带入由 `A` 决定的 preconditioning。因此 forward-equivalence 不能替代 optimizer、参数度量和 learning-rate 的联合比较，原有 dense MLP 也不因存在等价 spline 表示而自动过时。<!-- source-family:arxiv:2603.04827v1 -->

多分辨率训练还需要两项不同条件：coarse-to-fine transfer 应精确保留已学函数及相同输出 loss，而 fine-level 更新应纠正 coarse level 尚不能表达的模式。只有前一项，新增参数也可能继续优化已学的平滑方向，浪费 refinement。[spline 基底的受限回归对照](https://arxiv.org/html/2603.04827v1)以等 FLOPs、L-BFGS 和五次初始化支持这一区分，不证明所有深网或优化器都有相同收益。构造嵌套基底、transfer 与稳定 preconditioning 增加成本；无法保持函数、fine modes 学不动或成本不合算时，仍应使用固定分辨率与已验证的 dense/gated MLP，而不是只凭表达容量批准扩层或加宽。

Dense projection 让每个输出直接组合全部输入，表达和成熟 GEMM 路径都清楚；参数预算紧时，也可将方阵投影改成输入/输出对角缩放之间的多级成对块乘积。每级 pairing `P_l` 决定哪些坐标交换信息，stage depth `L` 决定可组合的交互路径，rotation 块与一般可训练 `2×2` 块又有不同自由度；这改变的是可达函数集合，不是把任意 dense 权重无损压缩。每级约 `O(n)`，全投影约 `O(nL)`，中间 activation、反向和多级 kernel 仍付费；teacher 与学生采用相容结构的有限对照不能授未知任务容量等价。CPU 受测窄宽配置出现快慢反转，也说明结构参数少不等于真实执行快：布局、stage 开销与硬件 kernel 必须一起测，未获质量与总成本验收时仍保留 dense/gated FFN，而非用渐近阶取代成熟 GEMM。<!-- source-family:SF-2026-ARXIV-2512-23905 -->

当目标是替换已训好的逐位置函数，而不是改变训练参数化时，也可先把输入和输出投影到较低维坐标，在该坐标中为每个输出拟合有界的符号函数，再重建回 residual stream。这减少了函数搜索的维度，却不保证保留 dense FFN 的表达能力；必须分别对照原层、投影后仍保留原函数、投影后的代理以及删层/恒等路径，才知道质量损失来自压缩还是代理近似。低维表达式可读，也不证明它是模型原先唯一使用的内部算法。<!-- source-family:SF-2026-ARXIV-2602-21307 -->

符号搜索、缓存中间激活和逐输出拟合增加离线成本，变量或算子集合扩大时可能迅速变贵。[受限 MLP 替换](https://arxiv.org/html/2602.21307v1)的投影控制几乎解释了全部 perplexity 增量；三层、同域 WikiText-2、关闭 KV cache 的 full-forward 吞吐不授长序列 decode 或生产 SLO。投影丢失信息、跨域质量退步或端到端成本不合算时，保留原 dense/gated 层；这是一条可验证的近似分支，不是让所有 MLP 变成公式。

## Linear 为什么最终成为 GEMM

模型公式按 `[B,T,d]` 表达语义，GPU library 通常先把 batch 与 token positions 合并成矩阵的行：

```text
M = B * T
K = d_model
N = d_ff

X_2d = reshape(X, [M,K])
U    = X_2d W_up          [M,K] x [K,N] -> [M,N]
```

Down projection 则交换中间维度与输出维度：

```text
Y = A W_down              [M,d_ff] x [d_ff,d_model]
```

因此一个 Linear layer 的主要计算可以交给 General Matrix Multiplication（GEMM）。若把一次 multiply 和一次 add 各计为一个浮点操作，单次 dense GEMM 的主项约为：

```text
FLOPs_GEMM ~= 2 * M * N * K
```

这个映射解释了为什么模型 shape 会直接进入硬件效率：

- Training 或长 Prefill 的 `M=B*T` 较大，通常有更多独立 tiles 可占满 GPU。
- Decode 中每次只有少量新 token，`M` 可能很小；权重相同，GEMM 却可能无法形成足够并行工作。
- `K/N` 的对齐、dtype、layout 和 epilogue 会约束可用 Tensor Core kernel。
- SwiGLU 有两次 up/gate GEMM、elementwise gate 和一次 down GEMM；它不是一条不可分割的数学指令。

这里必须保持层次边界：`reshape([B,T,d] -> [B*T,d])` 不改变每个 token 独立通过 MLP 的模型语义；cuBLAS、DeepGEMM 或 fused kernel 只是实现这份矩阵契约的不同 execution paths。第49章再解释它们怎样做 tiling、数据搬运、指令调度和硬件适配。

## MLP 是不是“知识库”

研究发现某些 FFN activations、weights 或中间 features 与事实、模式和可解释概念相关，修改它们也可能影响特定输出。这为“MLP 承载部分知识关联”提供了实验入口。

但必须限制结论：

- 知识可能分布在 Attention、MLP、embedding 与多层组合中。
- 单个 neuron 可对多个模式响应。
- 可从 activation 读出信息，不等于模型因果使用它。
- 同一事实可能依赖 context 和多个计算路径。

因此更准确的表述是：MLP 提供高容量逐位置非线性特征变换，并参与存储和调用训练中形成的关联；它不是可按 key 直接检索的数据库表。

MLP的reader和writer还应按同一个channel配对阅读：只看两组权重各自的norm或spectrum，会漏掉谁把何种检测结果写回哪条方向。共同重排两侧只是重命名，单侧重配则可保留这些集合统计却改变函数；pre-norm层的有效reader还包含activation导数和normalization Jacobian。[受限耦合测量与干预](https://arxiv.org/html/2610.29340v1)发现多数强pair的writer反向作用于自己的reader，但这是所测输入panel上的局部符号，不证明完整residual更新全局收缩，也不等每个neuron都向logits写入同一概念。重配同时改变谱形，损失关联和删除代价不能只归某一对称性；Jacobian、重配、干预与续训均付费。需要解释或编辑时，保留原模型、真实行为/非目标回归与多路径证据，不由负cosine或几何core自行批准剪枝、事实修改或安全保证。<!-- source-family:SF-2026-ARXIV-2610-29340 -->

同一神经元的多个输出方向也允许比整颗置零更窄的修改。保持activation不变，把writer向量v改为v+c·u_s，可将某个unembedding方向u_s上的投影推向目标；但其他token j的投影同时改变c·u_jᵀu_s，readout方向不正交时不保其他输出。被编辑neuron未激活的输入在该局部贡献上不变，也不等于所有其他上下文或完整模型行为不变。一次定向重写与删除潜在表示因此是不同命题。

[OVE精确v1](https://arxiv.org/html/2606.18767v1#S3)以同位置神经元置零作对照，支持writer方向而非单纯地址定位会改变已知前缀续写；四种编辑mode又有不同抑制与局部性代价。贪婪短续写变化不认证无法恢复，逐edit重置的median结果也不能替累计安全：原文仍有未覆盖记忆、灾难性尾部及连续编辑崩溃，且未测改写提示迁移。语料预挖、定位、权重修改与完整非目标/累计回归均付费；支持或局部性不过关时保留原checkpoint、较窄干预或外部可追溯记忆，不把单方向、低中位损伤或高覆盖宣称隐私擦除。<!-- source-family:SF-2026-ARXIV-2606-18767 -->

定位候选neuron也可以先把“对输入扰动有反应”与“朝指定输出方向写入”结合：由两组首token的unembedding均差定义读出方向，将它与每个down-projection列的耦合乘上原/扰动输入的activation差，只把高分项交给后续消融、patch和恢复测试。这个两次forward的提名不是完整因果验证；跨层传播、normalization和prompt聚合会破坏简单可加解释，取绝对值或RMS后还须另保符号。[Perturbation probing的受限对照](https://arxiv.org/html/2604.27401v1#S3)主要改变首token gap与拒绝模板，不能由模板翻转推出安全知识删除或完整生成已顺从。Token集合、扰动、层/地址、剂量和读出对象需共同绑定，完整validation sweep、生成判分与非目标回归都计费。模板proxy失准、分布式路径或normalization使提名失效时，保留原checkpoint、其他归因方法和直接行为验证，不让高importance自行授权权重或激活编辑。<!-- source-family:SF-2026-ARXIV-2604-27401 -->

候选neuron还可以先相对两个不同控制人口提名：对指定答案概率取activation×gradient并聚合，减去只保选项/格式而去掉问题的人口得分，再排除国家名阅读理解中同样突出的地址。[受限双控制分支](https://arxiv.org/html/2510.08284v1#S3)把格式依赖与名称读取分别列为替代解释，却不使剩余地址成为纯文化或唯一知识槽位；去问题也改变信息和输入分布，按原答案概率加权更偏向模型原本已会的样本。Token聚合、控制标签、层/地址和跨国家标准化须共同保存，局部梯度近似不认证大幅置零或联合移除的精确因果。Mask诊断与挑整组模块训练是不同干预，后者还改变层、模块类型和可训练几何，不能由候选少就授免遗忘；原有限对照已有常识/语言推断大幅退步，也有文化代理反升。全部控制数据、概率/反向、筛阈、随机mask、模块训练与目标/非目标回归均付费。控制失配、损伤或迁移不稳时，保原checkpoint、较窄直接干预与外部知识证据，不由归因热图或局部top项签发知识隔离、文化真值和安全编辑。

<!-- source-family:SF-2025-ARXIV-2510-08284 -->

语义关系的干预还要注明被改变的是哪一个读出对象。一个稀疏特征子集可以提高线性probe对某关系的margin，移除同一子集也可以使probe改判；这只是在固定probe空间定义的sufficiency/necessity，不等于后续网络会因果使用它、更不认证next-token或完整生成的关系正确。[有限WordNet对照](https://arxiv.org/html/2603.17624v1#S3.SS4)同时比较Attention、MLP和完整post-residual，并显示关系种类、模型及提示改变时的读出与干预效果不同；不能由近邻cosine、某个peaklayer或“高sufficiency”把关系当作单一可编辑槽位。采用时应分别冻结有向关系标签、template、probe/SAE revision与干预位置，另验原模型输出、无关关系和上下文回归；这是工程验收要求，不冒称原论文已验证生成编辑。特征选择、字典训练与重复干预都付费，probe shift不稳、标签方向或selection口径未闭合时，保留原checkpoint与外部关系证据，不从probe成功提交权重变更。<!-- source-family:SF-2026-ARXIV-2603-17624 -->

读出关联之后，还可在冻结权重下直接测试生成时的gate介入，但必须明确地址：对gated MLP的非线性后gate选定维度，在与另一内容分支相乘及输出投影之前缩放、加偏移或置零，而不是修改整个residual或权重。一个受限语音生成分支先按目标情绪匹配与内容误差筛选成功样本，再从其激活概率差别选稀疏地址，以同情绪、跨情绪及等稀疏随机掩码比较输出。筛选人口、模型/layer、hook位置、掩码与强度共同定义该干预；相关地址和局部效果不证明单一情绪槽位，也不证明它与内容能力正交。<!-- source-family:SF-2026-ARXIV-2603-17231 -->

[生成gate干预的有限对照](https://arxiv.org/html/2603.17231v1)同时暴露情绪、内容与自然度的不同边界：情绪匹配可升而内容误差恶化，自然度仍近似不变；其中内容WER取模型伴随输出的text而非独立转录生成audio，不能把它当作音频逐词保持证书。自动与人选地址只部分重合，跨speaker/情绪迁移也有反退，语言decoder和下游synthesis的局部对照不授唯一因果位置。识别、judge、人工筛选、强度搜索、额外生成与回归均付费；失配或内容退步时，保留原forward、保守强度及独立音频/文本检查，不从冻结weights或听感自然推出无损控制。<!-- source-family:SF-2026-ARXIV-2603-17231 -->

权重编辑也须分开“直接问新事实能够回答”与“把它接入后续关系仍能够回答”。rank-one update 改变一个事实的直接 recall，并不保证组合问题会沿同样路径访问该关联；把同一编辑复制到更多层可以在受限两跳任务中提高可用性，却同时扩大对无关事实和流畅性的干扰。[rank-one editing 的局部反证](https://arxiv.org/html/2601.04600v1)在 GPT-J 的有限 MQuAKE/CounterFact 人口中展示这种取舍，不能由直接回答失败定位唯一 hop-layer，也不证明所有编辑方法失效。因此编辑验收应冻结目标事实、问题/context 与 decoding，分别检查直接 recall、多跳组合、locality 和 fluency，并计入定位、重复更新与回归成本；这是由反证导出的工程要求，不是作者已验证的普遍编辑证书。组合或局部性回归不过关时，保留可信 checkpoint、限制编辑范围或用可追溯外部检索承载可变事实，不能用单问答成功把权重当数据库事务提交。<!-- source-family:SF-2026-ARXIV-2601-04600 -->

编辑覆盖的 key 还取决于模型先怎样构造输入状态，而不只取决于写了哪一层。在两个受测 masked DLM 中，双向 Attention 先把关系措辞写入可见实体位置，早层 MLP 再消费这份关系与方向相关的表示；同一事实的不同问法因而可能落在一个区域，而非共用实体的单一点。Mask-native patch 与关系消息移除/替换支持这条局部访问路径，但 window tracing 的晚峰不等第二个独立存储处，单层 MLP 也未成为唯一因果事实槽；causal AR 相同位置不能看右侧关系，更不意味着所有 AR 问法都无法反向回答。

[Factual Access State 的有限构造](https://arxiv.org/html/2610.27580v1#S3)据此为各查询方向构造多份 mask/context views，共同拟合一个 value 并沿平均 whitened key 更新；它不是为每种问法各存一条事实。反向方向仍须另覆盖，结构化 spans、value 求解、mask 分布 covariance 和多 view 回归都付费。同一表示也可逐 entity 读作 retrieval query，却依赖给定 spans 和有限候选预算，不能从可读性推通用 RAG 最优。匹配 view 数量后仍有局部收益，但 forced-choice 成功不等自由问答可靠，编辑后的自然问题仍常答错，局部 top-rank 保持也不保全分布；访问区域、span 或质量回归不稳时，保留原 checkpoint、较窄单次编辑与可追溯外部证据，不把新 key 接口签成事实真值或数据库事务。<!-- source-family:SF-2026-ARXIV-2610-27580 -->

编辑应在哪些层发生，与当前输入是否该消费这份编辑，是两项控制。一个受限多模态分支先用单次forward中每层FFN前后的目标answer log-prob差，提议后半网络的待改层，再由MEND-style editor生成更新；推理在最早待改层前取原模型表示，经学习的对比空间与edit anchor比较，仅过阈值才启用这些更新，否则保原权重。[LDKE的有限接口](https://arxiv.org/html/2605.29826v1#S3)因此分开层提名和输入路由，不由logit-lens差得到因果定位或事实真值。相关查询迁移、同图无关实体保持和路由误触发应分测，cosine分离也不证明无泄漏；顺序编辑后原模型分布漂移会让editor失效，所测十次编辑已严重退化，不能当持久可组合数据库。全部定位前向/目标投影、梯度editor、router训练与每次门控及回归都付费；anchor、阈值或连续更新失配时，保原checkpoint、受限单次编辑和可追溯外部检索，不由单样本纠正授权后续权重变更。<!-- source-family:SF-2026-ARXIV-2605-29826 -->

输入级路由只回答当前查询是否消费一份编辑，不能决定持续累积的编辑池何时需要重建。可单独维护编辑记忆时，一条替代分支把观测到的编辑错误率作为维护触发信号：先剪除失效部分，再对失败样本重聚、重训并重新整合，而不是永久追加每次更新或无条件融合。由此，维护触发、当前记忆池和实际消费它的模型/路由版本必须分开管理；新事实能否回答、换问法能否迁移、非目标行为能否保持也要分开验收。

[编辑池维护的有限对照](https://arxiv.org/html/2510.01879v1#S2)支持研究这条生命周期，不提供已闭合的无损合并配方：方差目标与多样性说明、高低损失样本的处理和融合公式仍有不一致，不能据此直接复刻保证。较高综合分数也可伴随局部性退步；与编辑前输出一致不等事实正确，文本困惑度更低也不等幻觉更少。剪除、聚类、重训、融合及独立回归均付费，所报维护吞吐还低于主要比较方法。触发阈值、编辑顺序或保留测试失配时，应保留可回退的池/模型版本、较窄编辑或可追溯外部检索，不以持续修复命名批准无遗忘、免费维护或数据库事务。

<!-- source-family:SF-2025-ARXIV-2510-01879 -->

### MLP 不必独自保存每条事实

把 MLP 权重解释成逐条事实的 key-value memory，容易导出事实数量与参数近似线性增长的图景；如果 embedding space 已把实体、属性和关系组织为可叠加几何结构，小 MLP 可以复用同一 relation-conditioned selection rule，而非为每条事实分配独立槽位。参数效率来自表示与选择规则分工，也带来 embedding interference、margin/维度要求和多跳深度成本。几何结构不成立或需要可更新 provenance 时，显式 retrieval、更多参数或层仍更可靠。exact-v1 的证明和实验限于受控结构，不能定位真实 LLM 的全部知识、保证编辑安全，或把 MLP 宣称为唯一知识 owner。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-12426 -->

## 从 Dense MLP 到 MoE

Dense MLP 对每个 token 激活同一组参数。扩大 `d_ff` 会同时增加总参数和每 token compute。

第21章 MoE 会把一组 dense MLP 替换成多个 experts，并让每个 token 只选择少数 experts：

```text
Dense MLP: every token -> same full MLP
MoE:       each token -> selected expert MLPs
```

这使总参数容量与 active parameters 部分解耦，却引入 router、load balance 和 All-to-All。MoE 是本章机制的条件化扩展，不是 Attention 的替代。

## 参数也可以成为运行时生成的有界状态

MoE 在预先训练的参数池中选择计算路径，并不为每次请求重新生成参数。若变化来自用户或会话中的新数据，则需要区分另一种条件化方式：改变少量实际参与计算的权重。

固定 FFN 最容易版本化、缓存和部署；当 live data 持续变化时，另一条实验性分支让一个生成器为当前样本或会话产生低秩 weight modulation，再用受限在线更新调整该状态。它改变的不是“无限增加模型参数”，而是把少量条件权重从静态 artifact 移到带输入、版本和生命周期的 runtime state。

这种适配以额外生成计算、状态隔离和回滚复杂度换取快速个性化。在线生成的权重必须绑定 base checkpoint、数据 provenance、rank/shape、会话和有效期，并由独立评价决定是否接纳；否则污染会跨请求扩散。现有小规模实验不能证明无限容量、持续学习稳定性或生产收益，条件不满足时固定 FFN、adapter 或外部 retrieval 仍是更可控的路径。<!-- source-family:SF-2026-ARXIV-2609-18842 -->

## 工程实现边界

MLP 主要由大 GEMM、activation 和 elementwise multiply 组成。高性能实现会考虑：

- 将 `[B,T,d]` 映射为 `M=B*T` 的 GEMM，并针对 Training、Prefill 与 Decode 的不同 `M` 选择 kernel。
- GEMM shape 与 Tensor Core 对齐。
- Bias/activation/gate fusion。
- Activation memory 与 recomputation。
- Tensor Parallel 的 column/row partition。
- Quantization 对不同 projections 的误差。

这些优化可以改变吞吐与显存，不能改变 checkpoint 定义的 activation 和 matrix shapes。

## 本章在知识树中的位置

```text
Attention output [B,T,d_model]
-> MLP up projection [B,T,d_ff]
-> nonlinear / gated features
-> down projection [B,T,d_model]
-> residual stream
-> Dense MLP may extend to MoE
```

第15章完成多头信息混合，本章完成逐位置非线性变换；第17章将二者与 Residual、Normalization 组合成一个可堆叠 Layer。

## 自检问题

1. Attention 和 MLP 分别沿哪个维度组织信息？
2. `W_up` 与 `W_down` 的 shape 分别是什么？
3. 为什么没有 activation 的多层线性变换仍等价于线性变换？
4. 小例子中 ReLU 选择了哪些中间 features？
5. `d_ff` 增大带来什么容量和计算代价？
6. SwiGLU 的两条 up branches 分别做什么？
7. 标准 MLP 与 gated MLP 参数量为何不同？
8. 为什么不能把 MLP 简化为人类可读知识库？
9. MoE 怎样扩展 Dense MLP？
10. 为什么序列较短时 MLP 仍可能是主要计算来源？
11. `X [B,T,d_model]` 进入 up projection 后，GEMM 的 `M/N/K` 分别是什么？
12. 为什么相同权重在长 Prefill 与单 token Decode 中可能获得完全不同的 GPU 效率？

## 小结

MLP 与 Attention 分工明确：Attention 在 token 之间路由信息，MLP 在每个 token 内构造和组合非线性 features。扩维提供容量，activation 或 gate 提供条件选择，down projection 恢复 residual stream shape。

在执行层，`[B,T,d]` 会被映射成 `M=B*T` 的 GEMM；这解释了为什么相同模型语义会因 Training、Prefill、Decode 的 `M/N/K` 不同而产生不同硬件效率。MLP 参与形成模型知识与计算特征，但知识是分布式、上下文化的。这个边界既避免低估 MLP，也避免把权重矩阵误解成可直接读取的事实表。

## Review notes

- `SF-2025-ARXIV-2510-00537`：Daily2025-10-03补Oct02；[Spectral FFN exact-v1](https://arxiv.org/html/2510.00537v1#S3)，2+1+2=5/activation谱诊断具体gap深入。仅固定采样人口/位置的covariance与主尾谱比较，不采完整hook、统一指数或剪枝配方；保SUI均匀谱反侧/分母与非整数rank、gate印式未闭、finite correlated样本/下游放大、窄宽Norm反退和全部重训/采集/分解/搜索回归费。未核全表/图像素/代码或复现，不授谱因果或LLM净速度。R21原分/日门复用；root R58必要/actualowner/整体PRE与窄授通过，真实SAVE/fullselfread后root R60唯一实际POST通过，指定窄位生效释放；仅行政同步既成，不预DAY。

- `SF-2025-ARXIV-2510-06660` — Daily2025-10-10补Oct09BJT；[GMNM exact-v1](https://arxiv.org/html/2510.06660v1)，2+1+2=5，作者A28唯一必要§3/5/T2–6/6，Jason R38纠错反侧通过。只投影Gaussian非线性/概率与算子资格；Eq3 affine合并/rank1反侧不否定全部多component逼近，亦不采任意SPD等价/GMMdensity UAT到本结构，supp未取得。保µ固定/缩conv预算混杂、最小testloss选后及硬件batch未披、全宽投影/训练费，不采LLM全FFN/脑专化或净速度，未核实现复现；PRE/SAVE/完整自读/solePOST只实际后到。 Jason R44整体PRE窄授、A34真实SAVE/完整自读与限定QA、R45唯一actualPOST已通过，指定窄位释放；仅同步既成事实，不预DAY。

- `SF-2026-ARXIV-2606-10722` — Daily2026-06-11补Jun10；[exact-v1](https://arxiv.org/html/2606.10722v1)§3–6/B必要，2+1+2=5。只bankpredictor语义/局部phase后缀fallback及CWE-NIAH-MMLU取舍，保密集upgate仍付费/额外参数WD与全费，不授全记忆恢复/4x墙钟或expertbalance无用。未核实现/复现；reader§84必要/actualowner/唯一PRE通过并依root委托窄授后已真实保存，reader§87唯一实际完整新增/两侧/本人注POST通过，指定窄位生效释放，不预DAY。

- `SF-2026-ARXIV-2610-29340` — Daily2026-10-23，Oct22公开；MODEL_SOURCE M14必要精确v1原域/反侧及actual owner和原单段PRE由独立reader具名通过，2+1+3=6。root只按此位实际保存，保原论点、全部费用与适用边界；未核完整artifact或复现。独立reader已完整核新增、直接两侧与本人源注，实际写后通过，不授DAY。

- `SF-2026-ARXIV-2610-27580` — Daily2026-10-22，[Factual Access State exact-v1](https://arxiv.org/html/2610.27580v1)§2–4/C/D/F/G必要域，2+2+2=6。只masked双向relation-key接口与多view共value/平均key、读写消费条件，保early联合非唯一MLP槽、reverse另覆盖、matched-view/QAEdit自然回答反侧、自然context非open corpus及全费；不授事实真值/数据库事务或RAG普优。作者E17/reader R64必要Source/具体owner/PRE通过，actualPOST另见本日REVIEW；未核实现或复现。

- `SF-2026-ARXIV-2604-27401` — Daily2026-05-02补May1；v1§2–6及L必要层，2+1+2=5，coupling×扰动提名/实际因果分工差额深入。保RMS/abs符号、norm/下游传播、logit/模板/完整行为与CAA分类器待rerun；不授RLHF唯一因果、安全删除或普遍优势。未核artifact/复现；reader R42必要Source/owner/逐字PRE通过，root授本单段+本人注窄lease；作者已保存并顺读，reader非writer actual正文/完整两侧/本人注POST R44通过，root接纳并释放窄lease；作者仅行政同步既成状态并实际读回，不授DAY。

- `SF-2026-ARXIV-2602-21307` — Daily `2026-02-27`；[SymTorch exact-v1](https://arxiv.org/html/2602.21307v1) §4.1/5.1，PCA/原MLP/符号代理/identity对照及KV-off完整forward。2+1+3=6，具体函数近似缺口深入，仅采用投影与代理误差分账、离线搜索与dense/gated回退；不采用后版吞吐、跨域无损、内部算法唯一解释或生产SLO。root必要原源/实际owner PRE及实际正文/完整邻接/自身末注非作者POST通过，窄锁释放。未核代码或复现实验，不授整日完成。

- `SF-2026-ARXIV-2601-04600` — Daily `2026-01-10`；[exact-v1](https://arxiv.org/html/2601.04600v1) §4/5.1/5.2 Table2–3与§7 key-drift/跨层copy代价。原3+1+2=6，设计反证对应具体缺口深入，只采用edit recall与多跳access分账及复制干预的locality/fluency成本，不采Eq1形状、唯一hop-layer因果或普遍编辑失败。工程验收与回退为受限推断；未核代码或复现实验。root必要原源/实际owner写前通过；jan02_v3实际正文244–267及本注非作者写后复核通过，未重复原源审阅，日级Gate待验。

- Daily 2026-03-07：[KAN multilevel exact-v1](https://arxiv.org/html/2603.04827v1) §3/Eqs16–17、§4/Definition1/§4.3、§5.1/Table2。只吸收forward-equivalence≠默认gradient geometry及exact-preserving transfer与complementary relaxation分离；等FLOPs/L-BFGS/N5的函数回归和高方差保留，不采用PINN应用或通用训练加速。root准入与窄锁通过，作者实际写入，root实际原文/正文及邻接独立POST通过；未复现。

本章覆盖标准 FFN、SwiGLU、参数/FLOPs 与逐位置小例子，并将“知识存储”限制为可验证的机制命题。MoE 只建立接口，完整 router 与系统 trade-off 保留给第21章。

Primary-source 校验入口：

- Ashish Vaswani et al., "Attention Is All You Need", 2017: https://arxiv.org/abs/1706.03762
- Noam Shazeer, "GLU Variants Improve Transformer", 2020: https://arxiv.org/abs/2002.05202
- Mor Geva et al., "Transformer Feed-Forward Layers Are Key-Value Memories", 2020: https://arxiv.org/abs/2012.14913
- NVIDIA cuBLAS documentation（GEMM / cuBLASLt execution contract）: https://docs.nvidia.com/cuda/cublas/

- `SF-2026-ARXIV-2512-23905` — Daily `2026-01-02`；[Rethinking Dense Linear Transformations: Stagewise Pairwise Mixing (SPM) for Near-Linear Training in Neural Networks exact-v1](https://arxiv.org/html/2512.23905v1) §3–4、§9.1/9.3–9.5。5分具体operator gap深入，仅采用pairing/stage-depth容量与`O(nL)`执行预算、结构teacher及CPU kernel crossover；不授GPU/Large-LM普遍速度。B32/B256、NLL2.58nats/BPC3.03与1000/800steps不统一，因此隔离联合质量/速度headline，不否有效局部接口与全部实验。未运行代码；root必要原源/具体owner写前通过，实际正文/邻接及末注写后经root非作者复核通过。

- `SF-2026-ARXIV-2601-10639` — Daily `2026-01-17`；[STEM exact-v1](https://arxiv.org/html/2601.10639v1) §3.1 Eq4、§3.4、§4受控预算与§4.4直接消融。2+2+2=6，标准必要补读后长期采用深入核：只采用静态 up 地址保留 context gate 的计算/存储替代分支；不采知识因果、cache-hit性能保证或生产SLO。表/optimizer/CPU通信、decode未知 next token、有限350M/1B预算及dense共存相邻。root必要原源/具体owner写前通过，root实际正文/邻接及末注非作者POST通过，窄锁释放；未核实现或复现，日级未授。

- `SF-2026-ARXIV-2603-17624` — Daily `2026-03-20`；[SemanticRelations exact-v1](https://arxiv.org/html/2603.17624v1) §3.1–3.4/EqLD、FR、DR、§4.1–4.3/T2–6与§5/7。只采probe干预对象及relation/template联合验收边界，不采方向表口径、冗余唯一解释或next-token编辑保证；base dense/WordNet/SAE选择与成本限制保留。未核代码或复现实验。

- `SF-2026-ARXIV-2603-17231` — [EmotionNeurons exact-v1](https://arxiv.org/html/2603.17231v1)必要§3/Eq1–8、§4/T1、§5/T2–6与直接迁移/内容反侧、§6。仅成功人口→postactivation gate稀疏地址→生成控制的接口与分验；保伴随text WER非audio转录、judge/人选差别、强度/迁移反退和全费，不授语义纯净、唯一因果、内容正交/无损或完整部署保证，未核代码/复现。

- `SF-2026-ARXIV-2604-02990` — 04-07补04-06自然日；FedSQ exact-v1 III-A/B/Alg1、IV/T1。仅采用固定input gate下输入affine与joint参数平均分离，5x/4x为本章公式的数学推断，不是论文保证；DualCopy存储与trainable分账、binary surrogate、central schedule及CNN反退保留，不授Transformer迁移或联邦收敛。root非作者已实际核必要Source、具体owner/逐字PRE与写后正文/完整邻接/本人note，POST通过；作者同步本记录后释放窄锁。未核artifact/复现，不授日级完成。

- `SF-2026-ARXIV-2604-17673` — Daily2026-04-22补Apr21；[exact-v1](https://arxiv.org/html/2604.17673v1) §3–4及AppA/C/E/G/H必要，2+1+2=5。仅采用输入粒度×首轮聚合前非线性/深度的有限替代检验；toy无序operandpair划分、Fourier吻合非唯一因果、classifier与训练/heldout分母边界保报告，额外token/训练/采样全费。fresh实际必要Source及root actual owner/A49单段逐字PRE通过并授窄lease，作者写入并顺读局部；root实际非writer正文/完整邻接/本人注POST通过，lease释放，作者仅行政同步并实际读回，不授实现复现或DAY。

- `SF-2026-ARXIV-2605-01973` — Daily2026-05-06补May05；[MeGan exact-v1](https://arxiv.org/html/2605.01973v1) §5.1–5.3/6/Tables4–7、A2/A7/B2必要；2+1+2=5。只采条件query/层状态key-value、相对1的activation slope偏移接口，保混合对照/失败persona与全部控制器费用，不授冻结base即不遗忘、全局稳定或推理加速。root实际必要Source/具体owner及修后A4 PRE通过，授SwiGLU末尾指定单段及本注窄位；作者已保存并实际self-read；root非writer实际完整正文/两侧/本人注POST通过，指定窄lease释放；仅同步既成事实，不授DAY；未核代码或复现。

- `SF-2026-ARXIV-2610-21553` — Daily2026-10-17窗10-16；[exact-v1](https://arxiv.org/html/2610.21553v1) §3–6/8必要，2+2+2=6。只采addressed memory的row/shared-readout写权限与mounted-reference约束，保50事实toy、训练命中/新问法/未写实体分验、首token词面非完整事实与dense optimizer/anchor全费，不授生产模型完整知识写入。root实际必要Source/具体owner与最小PRE通过并授单段/本人注；作者已保存并自读，root实际正文/完整直接两侧/本人注POST通过。未核实现/复现，不授DAY。

- `SF-2025-ARXIV-2509-00454` — Noether，Daily2025-09-04补Sep3；[exact-v1](https://arxiv.org/html/2509.00454v1) exact-v1 §2–4/AppB.1–2必要，2+1+2=5。仅functional sparsity与gated FFN删点/已付工作分责，保critical平均非逐任务、outlier/阈值迁移/虚拟稀疏非净加速与全费，不采max-p冲突公式/未来模型普遍性，未看全表/像素/代码或复现。Ohm§53实际必要Source/评分/具体owner/逐字PRE通过，root协调完整Gate projection预算段后/persona条件斜率首段前单段位；已按批准稿真实保存，作者已完整self-read；Ohm§68一次真实非writer完整新增/完整直接两侧/本人注POST通过，依root已协调本指定窄位即时生效释放。仅同步既成事实，不授整日DAY。

- `SF-2026-ARXIV-2605-29826` — Daily2026-05-30补May29；exact-v1必要Source/当前owner/A57原PRE由唯一reader R103实际通过，首次2+1+3=6；只层提名与输入级delta消费，保非因果、同图局部性/顺序十次漂移、时间文表冲突与全费。root协调授2601-04600后本原单段+本人注，作者实际保存；唯一reader R106已实际读完整新增/直接两侧/本人注POST通过并释放，未核实现/复现，不预DAY。

- `SF-2025-ARXIV-2510-01879` — Hilbert，Daily2025-10-04补Oct03BJT；[REPAIR exact-v1](https://arxiv.org/html/2510.01879v1)§2.2–2.5/3.3旧有效必要复用，§3.1–3.2/T3–4/C T5–6/T8及F7正文新缺层经R286；2+2+2=6。仅错误率触发编辑池剪除/失败样本重聚重训/再整合与维护频率取舍；保variance/样本选择/merge配方未闭、Rel/Gen/Loc分责、PPL非事实真值、局部性退步与更慢维护/全费。不授零遗忘、精确融合算法或生产能力，未核像素/代码/权重或复现；整体PRE/真实SAVE/selfread/唯一POST只按本日canonical实际层，不由本注预签。

- `SF-2025-ARXIV-2510-08284` — Aquinas，Daily2025-10-11补Oct10；Godel R102 exact-v1 §3–5/式1–11/T2/A/B/G/H/J首次必要完整消费，449806B原件。2+1+2=5，仅缺问题格式控制与国家名读取控制双人口提名/后续mask诊断和模块训练分责差额深入；保概率加权/局部Taylor、控制mask数量与层型混杂、ComQA/QNLI大幅反退和全部费，不采纯文化/唯一槽位或免遗忘。未核全国家表/图像素/代码/复现；整体PRE/真实SAVE/完整自读/solePOST只本日canonical后到真实层。
