# 第28章 Pretraining

**Knowledge Tree:** Part IV Training System：模型能力如何产生
**Stable Knowledge Node ID:** `TRAIN-PRETRAINING`
**Legacy Chapter:** Ch24
**Status:** Draft

**Roadmap Intent:** 大规模预训练如何形成通用语言和世界知识。

## 本章要回答的问题

第 27 章已经把数据构造成 token sequences，Part II 也已经给出 Decoder-only 模型。模型怎样仅通过预测下一个 token 改变数十亿参数？Loss 下降、perplexity、训练 token 数、optimizer step 与能力增长分别是什么关系？梯度异常时，warmup、clipping、adaptive optimizer 与逐层 learning rate 分别能解决什么？为什么一次成功的 Pretraining run 不只是反复调用 `backward()`？

本章的核心判断是：**Pretraining 是在大规模数据分布上反复最小化 next-token negative log-likelihood，使参数逐步形成可复用表示与条件生成能力。**它提供通用能力底座，但 loss 下降不自动保证事实可靠、指令遵循或部署分布上的任务成功。

本章使用 `B` 表示 batch size，`T` 表示 sequence length，`V` 表示 vocabulary size，`theta` 表示模型参数，`z_(b,t)` 表示位置 `(b,t)` 的 logits，`y_(b,t)` 表示对应 target token id，`N` 表示累计参与 loss 的有效 tokens。

## 从随机参数开始会发生什么

训练开始时，Embedding、Attention 和 MLP 参数通常无法产生有意义的条件分布。给定 prefix：

```text
The capital of France is
```

随机模型可能给所有 vocabulary tokens 近似无结构的 logits。数据提供真实后继 token，loss 衡量模型分布与 target 的差距，backpropagation 再把误差信号传回所有相关参数。

单个样本只提供一个局部更新。Pretraining 的能力来自大量不同 contexts 反复约束同一组参数：语法、事实、代码模式、推理模板和文档结构必须在有限参数中形成可复用计算，而不是为每条文本创建独立规则。

这也解释了为什么“训练看过某句话”与“模型可靠掌握其中知识”不是同一命题。出现频率、上下文多样性、参数容量、优化竞争和 Evaluation 方式都会影响结果。

## Next-token objective

第 18 章已经得到 causal factorization：

```text
p_theta(x_1,...,x_T)
= product_(t=1)^T p_theta(x_t | x_<t)
```

训练张量中，位置 `t` 的 logits 用前缀 `x_<=t` 预测 label `x_(t+1)`。对一个有效位置：

```text
p_theta(y | x_<=t) = softmax(z_t)[y]
loss_t = -log p_theta(y | x_<=t)
```

Batch masked loss 可以写成：

```text
L(theta)
= - (1 / sum_(b,t) m_(b,t))
  * sum_(b,t) m_(b,t)
  * log p_theta(y_(b,t) | x_(b,<=t))
```

其中 `m_(b,t)` 为 loss mask。Padding、跨文档边界或不参与监督的位置应为 0。Logits shape 是 `[B,T,V]`，labels 与 mask shape 是 `[B,T]`。

## 一个 token loss 小例子

假设某个位置有三个候选 token：

```text
z = [2,1,0]
softmax(z) ~= [0.665,0.245,0.090]
```

若正确 target 是 token 1：

```text
loss = -log(0.245) ~= 1.407
```

若参数更新后概率变成：

```text
p = [0.25,0.65,0.10]
loss = -log(0.65) ~= 0.431
```

Loss 下降表示模型对这个 target 分配了更高条件概率。它没有说明生成时一定选中该 token，因为 Sampling 仍可能选择其他候选，也没有说明整段回答事实正确。

## Perplexity 能回答什么

### Mean Cross-entropy 也会被重尾 Token 支配

平均交叉熵保留了概率模型的标准训练语义，但少量极高损失 token 会主导曲线，使它在某些阶段与下游质量不同步。评估应同时报告 mean、median 或分位数损失，并检验它们与目标任务在当前数据、模型规模和训练阶段的 concordance；median 不是替代目标，而是定位重尾贡献的诊断传感器。收益是减少对单一平均值的误读，代价是指标选择与早停规则更复杂；分布稳定、异常尾部本就重要时，mean CE 仍是正确聚合。当前证据只展示特定训练轨迹中的失配，不能把 median CE 升格为通用质量指标。

<!-- source-family:SF-2026-ARXIV-2605-24667 -->

若平均 token negative log-likelihood 为 `L`，perplexity 定义为：

```text
PPL = exp(L)
```

它可理解为模型在该数据分布上的平均不确定性尺度。PPL 较低通常表示更好的 token prediction，但比较必须满足：

- 使用相同 tokenizer 与 tokenization。
- 使用相同 Evaluation corpus 和 loss masking。
- 明确是否包含 special tokens、padding 或不同 domains。
- 不把小幅平均差异直接解释成特定能力提升。

不同 tokenizer 会改变 token 粒度，因此跨模型直接比较 PPL 可能没有可比性。PPL 也不能替代事实、代码执行、安全或指令遵循评估。

## 一次 training step 的状态流

最小训练循环是：

```text
data batch [B,T]
-> forward
-> logits [B,T,V]
-> masked cross-entropy
-> backward gradients
-> gradient aggregation / clipping
-> optimizer update
-> scheduler step
-> metrics and checkpoint policy
```

参数更新抽象为：

```text
theta_(s+1) = theta_s - eta_s * update(g_s, optimizer_state_s)
```

`eta_s` 是第 `s` 步 learning rate，`g_s` 是当前或累积梯度。Adam 类 optimizer 还保存梯度的一阶、二阶矩估计，因此训练状态远大于单份权重。

第 35 章会说明：若 checkpoint 只保存 `theta` 而不保存 optimizer、scheduler、random state 和 data cursor，通常只能继续做新的 fine-tuning，不能精确恢复原 Pretraining trajectory。

模型结构在训练中扩容时，state contract 还要包含 parameter mapping。简单复制旧单元可以近似保持 forward function，却会把相同 optimizer moments 与 learning-rate schedule 一并复制，导致新单元沿相同梯度轨道形成 symmetry lock。受控扩容需要联合迁移：

```text
old weights + optimizer moments
→ shape-aware parameter mapping
→ activation-scale preservation
→ reset or differentiate new optimizer state
→ asymmetric rewarm for new capacity
→ loss-shock canary and rollback point
```

它用已有训练计算换取延后容量决策，却新增短期 loss shock、parallel-layout migration 与可复现性风险。从头训练在目标形状已知、稳定性优先时仍是清晰基线；“函数近似不变”也不证明 optimizer trajectory 连续。

### Dynamic Sparsity 的 Topology Update 也是 Training State Transition

Dense training 或静态 mask 让一组参数持续积累 Adam moments，状态身份简单且恢复路径成熟；dynamic sparse training 周期性 prune / regrow 后，新激活连接没有历史一阶、二阶矩，却若沿用全局 late-training step，首次更新可能远大于成熟参数。此时 loss spike 的 owner 不是 collective，而是 `mask/topology revision + regrowth initialization + local optimizer timestep/moments + learning-rate phase` 这一组训练状态。

一个受限稳定分支是在 regrowth 时重置新参数的 local timestep，并让它们经历独立 linear warm-up；随后再按 density 调整目标 learning rate，以补偿稀疏层有效 fan-in 和 warm-up 带来的保守更新。若目标还包括训练内存，gradient、Adam moments 和 timestep/index metadata 只为 active parameters 保存，并用 block-wise metadata 摊薄索引开销。mask 与 active-index owner 必须和 optimizer-state owner 原子迁移，否则 resume、regrowth 或 checkpoint restore 会把旧 moment 绑到错误连接。

它以 topology/update metadata、稀疏 kernel 适配和局部 schedule 复杂度换取较小的 cold-start spike 与 active-only state；random regrowth、density rule 与 optimizer warm-up 都是需要单独消融的分支，而不是 dynamic sparsity 的通用定理。论文只在 Adam、披露的 LLaMA/C4/OpenWebText、unstructured 与简单 block sparsity 范围内支持该机制，局部 smoothness 分析也不等于全局收敛或实际硬件加速。结构化稀疏未被 kernel 支持、非 Adam optimizer、拓扑变化不值得其控制成本或恢复一致性优先时，应保留 dense training 或静态 sparsity 作为 correctness fallback。

<!-- source-family:SF-2026-ARXIV-2606-00888 -->

### Residual Path 也可以成为随 Depth 与 Time 演化的训练状态

普通 Pre-Norm/Post-Norm 与静态 residual scaling 在第 0 步就决定所有 branch 的参与方式；Learning-rate warmup 则统一控制参数更新幅度。模型更深、更窄或拓扑更敏感时，这两个旋钮未必足以表达“不同深度何时应承担完整变换”。一个实验性分支让 residual branch scale 同时依赖 layer 和 global step：训练早期网络接近 identity，再按明确顺序逐层激活。

```text
layer index + global optimizer step + schedule revision
-> residual scale alpha(layer, step)
-> forward contribution and backward path
-> full branch activation
```

它以延迟深层学习换取早期稳定性，也把 schedule、layer mapping 与 resume step 提升为 checkpoint 语义。恢复到错误 step、改变 layer 编号或没有同步 optimizer state，都会改变实际 training trajectory。过短 schedule 没有隔离效果，过长则可能欠训练深层；浅层优先、等序或反序也不是无关实现细节。

这个分支不会否定 Pre-Norm、受控 Post-Norm、DeepNorm、静态 residual parameterization 或 LR warmup。成熟 recipe、较宽模型和恢复简单性优先时，旧方案仍更合理。长期原则是：**Residual topology 定义可学习路径，schedule 定义路径何时活跃；normalization、initialization、optimizer warmup 与 branch activation 不能互相冒充。**

## Optimizer 不是与参数化无关的旋钮

### Optimizer Recipe 也包含数据变换

同名优化器在不同 augmentation、sample mixing、label smoothing 与 gradient spectrum 下并不是同一训练机制。尤其对矩阵型更新，收益可能来自优化器与数据管线共同改变的梯度几何，而非单独的 update rule。可复现 artifact 因此必须绑定 optimizer state、数据变换、loss smoothing 与谱诊断；收益是能解释 recipe portability，代价是实验矩阵扩大。数据分布简单且梯度谱稳定时，较小的 optimizer-only contract 仍可接受。现有比较只约束作者披露的 Muon 配方，不证明某一优化器在所有视觉或语言任务上更优。

<!-- source-family:SF-2026-ARXIV-2605-24770 -->

深度扩展还要求把 **hyperparameter transfer** 与 **feature learning regime** 分开。一个 parameterization 可以让不同 depth 的 activation、gradient 和推荐 learning rate 处于可比较尺度，却仍可能让无限宽极限长期停留在初始化附近；此时 schedule 只是在同一线性化邻域内改变步长，不能凭空恢复跨层 feature learning。

<!-- semantic-body-binding:SF-2025-ARXIV-250501618-COMPLETEP:start -->
更完整的 parameterization contract 同时检查：depth/width 改变后 forward 与 update scale 是否稳定，以及有限训练中 hidden representation 是否实际离开初始化并形成非懒惰特征。前者解决超参数转移，后者决定函数族能否沿训练扩展；二者失败时应先修 initialization、residual scaling 或 parameterization，再讨论 global/layer-wise LR。作者在特定模型形状、recipe 与 Cerebras CS-3 上报告的 12%–34% 只属于该 matched contract，不支持逐层动态 learning rate 的普适方向。成熟参数化在相同深度范围已验证、迁移成本高或 probe 不充分时仍应保留。
<!-- semantic-body-binding:SF-2025-ARXIV-250501618-COMPLETEP:end -->

同一个函数可以有多组等价参数。例如对低秩分解

```text
W = U V^T
```

任取正交矩阵 `Q`，都有：

```text
(U Q) (V Q)^T = U V^T
```

两组参数表达相同的 `W`，因而在当前 batch 上具有相同 forward、loss 和对 `W` 的函数级梯度；
但这并不保证 optimizer 会走出相同的 `W` trajectory。只有当更新规则对这种 basis change
保持 equivariance，参数更新才会随 `Q` 一起变换，而不会把某个任意的 factor basis 当作额外信号。

这解释了为什么 coordinate-wise preconditioner 不能被视为与模型参数化无关的数值加速器。
Adam 或 RMSProp 分别维护每个坐标的历史尺度；旋转 basis 会重新混合这些坐标，进而改变
preconditioner 和后续路径。相反，普通 Gradient Descent、shared-scalar scaling，或根据
Gram structure 构造的某些更新，可以在相应假设下保留这种对称性。

长期设计结论不是“Adam 错、GD 对”，而是：

```text
training trajectory
= objective + parameterization + initialization
+ optimizer state/update rule + schedule + data order
```

Per-coordinate adaptation 在大规模 Transformer 训练中仍可能因稀疏、异方差梯度与工程成熟度而
合理；保留 parameterization symmetry 也只是某些 implicit-bias 结论可迁移的必要条件，不是更好
generalization 或 low-rank recovery 的充分条件。2026 年一项 matrix-sensing 与小规模 Transformer
研究提供了 basis dependence 的构造性证据，但不能证明 Adam 在一般 LLM Pretraining 中劣于
其他 optimizer。

工程上，使用 factorized weights、structured adapters 或带内部 gauge freedom 的模块时，应把
optimizer、parameter groups、state dtype、initialization 和 schedule 纳入同一实验身份。除训练
loss 外，可以构造保持函数不变的 symmetry twins，检查不同 basis 下的 function-space trajectory、
held-out quality 与 optimizer-state divergence；若差异显著，就不能把参数 basis 当成无关实现细节。

另一条实验性分支不是要求 optimizer 对任意 basis 完全不变，而是在每次更新前主动选择更有利的
orthogonal coordinate system：先根据梯度或参数结构估计 rotation，再在旋转空间执行 adaptive update，
最后映射回原参数空间。它试图缓解坐标尺度失衡，但 rotation 本身成为训练状态和计算图的一部分：

```text
gradient / parameter statistics
→ estimate or update orthogonal transform
→ rotate update coordinates
→ apply preconditioned optimizer step
→ inverse map and checkpoint transform state
```

收益与代价必须一起看。更均衡的坐标可能改善特定模型的训练稳定性；额外矩阵运算、通信、transform
初始化、数值误差和跨 world-size checkpoint migration 也会增加。固定 Adam 在其成熟 kernel、状态恢复和
调参经验更重要时仍然合理。作者在有限模型和训练配置上的 loss/benchmark 改善只证明这种 actuator 可行，
不证明某个旋转规则是通用最优 optimizer。

Optimizer state 与 parameter application 也不必总是同一稠密度。Dense Adam 让每个 gradient 同时更新 moments 与
parameters，语义最清楚；实验性 masked-update 路线仍让 dense gradient 进入全部 optimizer state，只随机选择部分
parameter blocks 应用候选 update：

```text
dense gradient
→ dense first/second-moment transition
→ candidate adaptive update
→ block mask and optional alignment damping
→ sparse parameter application
```

若只用 Bernoulli mask 并按保留概率缩放，candidate update 在条件期望上可保持一致；一旦再用 gradient–momentum
alignment 做 damping，就引入了有意 bias。被 mask 的 block 也不是“冻结”：其 moments 已改变，下一步的候选 update
依赖这次 gradient。它可能在特定 heavy-tail/heterogeneous curvature 设置中改变 implicit bias，却没有减少 backward，
也不自动减少 optimizer memory 或通信；mask RNG、block identity、score EMA 与 dense-state/sparse-application 都必须
checkpoint。论文的小模型结果不能证明大规模分布式训练存在 wall-clock 收益，dense update 在实现成熟、景观较均匀或
可复现性优先时仍是基线。

### Optimizer State Allocation 也应服从参数角色

Uniform Adam 为每个参数维护同构的一阶、二阶状态，语义清楚、kernel 成熟，在参数统计相近且 memory 可接受时仍是基线。MoE 改变的是参数角色与 activation frequency：dense backbone 持续更新，experts 稀疏且按 routing 命中，router 参数少却直接控制流量。

因而一个实验性分支是按角色分配 optimizer state：backbone 保留 momentum 与 factored variance，experts 只保留 factored variance，router 保留更精确统计；共同的 write-back/rounding contract 仍需一致。它把 optimizer memory 从总参数数目的固定倍数改成结构感知预算，却新增 parameter-group policy、factorization bias、checkpoint migration 和对 gradient sparsity 的依赖。

它与 ZeRO/offload 是正交关系：本章决定保存哪些统计，Ch39 决定这些统计物理放在哪里。现有证据来自单个浅层 MoE、短训练与大多单 seed，不能写成 universal optimizer；结构均匀、factored covariance 假设不成立或恢复简单性优先时，完整 Adam 仍更合理。

### Whitening 的收益取决于 Gradient Spectrum 所在 Regime

对所有方向做统一 spectral whitening，在 pretraining gradient 较高信噪、需要扩大探索时可能比逐元素更新更有效；跨模态 action module 的低秩梯度或 RLVR 的低 SNR 会改变约束：放大 tail directions 可能同时放大噪声，并破坏先前 head specialization。Optimizer 因而不能只拥有一个“更均匀”的变换，而要让 spectrum estimator、module identity 与 training phase 共同决定是否 whitening、保留高频方向或回退通用 update。

这种 regime-aware policy 用额外 eigenspectrum 估计、阈值和 module-specific state 换稳定性；估计陈旧或 rank/SNR 判错会抑制有用探索。纯 pretraining、gradient spectrum 稳定或缺少可靠 module telemetry 时，统一 baseline 仍更容易复现。`arXiv:2605.19282v1` 的 §3–§5 只支持其 spectral failure analysis、high-pass remedy 及 VLA/RLVR experiments，Appendix M 不证明该策略跨模型、规模与训练阶段普遍成立。

<!-- source-family:SF-2026-ARXIV-2605-19282 -->

### Matrix-aware Step 可以与 Sign Step 按成本交替

Muon-style matrix update 保留二维参数块的几何结构，却要支付正交化/矩阵运算成本；sign-based update 便宜、稳定，但丢失部分方向结构。若 workload 同时受迭代成本和几何质量约束，optimizer controller 可以在两类 step 间按固定、可重放 schedule 交替：parameter-block owner 保持同一权重语义，optimizer artifact 记录 step type、state transition 与 checkpoint compatibility。

交替减少平均高成本 step，却引入 schedule、两套 state interaction 与恢复复杂度；比例选择错误可能同时失去 Muon 收益与 sign simplicity。小模型、矩阵开销不显著或结构假设不成立时，单一 AdamW/sign path 仍更合适。`arXiv:2605.19811v1` 的 §3–§5 只支持其 optimizer geometry、alternating spectral/sign descent 与所测 language-model runs，§6 不证明更低平均 iteration cost 等价于跨 workload 更优收敛。

<!-- source-family:SF-2026-ARXIV-2605-19811 -->

### Optimizer Update 要尊重参数块的对称性

统一逐元素 optimizer 简单、通用，在参数重参数化不改变功能时却可能给等价模型状态不同更新。embedding、LM head、SwiGLU block 与 MoE router 拥有不同 symmetry group；symmetry-compatible update 要求梯度变换与参数块对称性 equivariant，使 optimizer action 不依赖任意坐标表示。

收益是把架构不变量纳入更新规则；代价是块类型识别、额外矩阵/统计计算和错误 symmetry assumption。没有可靠结构元数据或收益不足时，AdamW 等通用基线仍更稳妥。exact-v1 只在其披露参数块、模型、训练 recipe 与实验中支持结论，不证明一个更新规则跨规模、数据和所有架构普遍更优。

<!-- source-family:SF-2026-ARXIV-2605-18106 -->

## Batch、tokens 与 optimizer steps 不是同一计量

设每个 optimizer step 的 global batch 为 `B_global`，有效平均 sequence tokens 为 `T_eff`：

```text
tokens_per_step ~= B_global * T_eff
N ~= steps * tokens_per_step
```

若存在 padding、packing、loss mask 或变长 sequences，`T_eff` 应按实际参与 loss 的 token 数计算，而不是配置中的 `T_max`。

增大 batch 可以提高矩阵规模和并行效率，也会减少固定 token budget 下的 optimizer steps，并改变梯度噪声与 learning-rate 选择。Gradient accumulation 可以在不一次放入全部 samples 的情况下形成更大 effective batch，但不能消除多次 forward/backward 的计算。

从本章开始，Part IV 统一使用 `B_micro` 表示每个 data-parallel rank
一次 forward/backward 接收的 micro-batch，使用
`gradient_accumulation_steps` 和 `data_parallel_degree` 表示另外两个乘数。
张量 shape 中的 `B` 仍表示当前实际输入张量的 batch 维度。完整关系在第
36 章展开：

```text
B_global = B_micro * gradient_accumulation_steps * data_parallel_degree
```

### Preconditioner 与 Gradient 共享 Batch 时会改变估计语义

用同一 minibatch 同时估计 gradient 与 curvature/preconditioner，状态简单、吞吐高，在 batch 足够大且预条件变化平缓时仍合理；但二者的统计耦合会产生 coupling bias，而 inverse/root 等非线性即使输入估计无偏也会产生 inversion bias。Cross-fit 把两类估计分到独立 microbatch，variance correction 再校正非线性偏差，因此 data cursor、microbatch identity、preconditioner revision 与 correction state 都要进入 optimizer/checkpoint 账本。

收益是更清楚的估计边界，代价是额外样本、内存、同步与估计方差；小模型或一阶优化已经稳定时，普通同批估计仍更简单。`arXiv:2605.20756v1` 的 §5、§7.1、Appendix A 与 §6–§7 实验只支持其估计器；§8–§9、Appendix C 不证明校正对所有矩阵预条件器或大模型都带来净收益。

<!-- source-family:SF-2026-ARXIV-2605-20756 -->

## Learning-rate schedule 为什么决定训练轨迹

固定过大的 learning rate 可能让 loss 发散，过小则浪费计算。大模型训练常使用 warmup 后 decay 的 schedule：

```text
warmup -> peak learning rate -> decay
```

Warmup 让 optimizer states 和 activation scale 在早期逐步建立；decay 则在后期降低更新幅度。具体 schedule 不是普适定律，必须与 optimizer、batch、模型规模和 token budget 一起解释。

Gradient clipping 通过限制 gradient norm 缓解极端 update：

```text
g <- g * min(1, max_norm / ||g||)
```

它可以避免单次异常梯度破坏训练，却也可能隐藏数据异常、数值 overflow 或不合适的 learning rate。平台应同时观测 unclipped norm、clipping frequency 和 loss behavior。

### 每层是否需要不同或动态的 Learning Rate

先把“这一层实际更新了多少”写清楚。对第 `l` 个 parameter group，可抽象为：

```text
Delta_theta_l(s)
= - eta_global(s)
  * m_l(s)
  * P_l(optimizer_state_s, g_l)
```

- `eta_global(s)` 是全局 warmup / peak / decay schedule。
- `m_l(s)` 是可选的 layer/group multiplier；可以固定，也可以随 step 变化。
- `P_l(...)` 是 optimizer 根据 gradient 与 moments 产生的 preconditioned update。Adam 的 coordinate-wise adaptation
  已经让不同参数获得不同 effective step，但它不等于显式的 layer-wise learning rate。

所以“每层用同一个 learning rate”通常只是指共享 `eta_global`；真实 `Delta_theta` 早已因 gradient、Adam moments、
parameter norm、weight decay 和 clipping 而不同。是否再增加 `m_l(s)`，应由 update evidence 决定，而不是看到深度
增加就默认启用。

#### 四种经常被混淆的策略

**Global schedule。** 所有 groups 共享 warmup 与 decay，最易复现，也让 update 的时间边界一致。它在标准
Pretraining recipe、架构/初始化已稳定时通常是首选。

**Optimizer adaptation。** Adam 用一阶、二阶 moments 按坐标缩放 update，主要应对 noisy、sparse 或异方差
gradient；它不会恢复在 backward path 中已经消失的信号，也不保证各层 update-to-weight ratio 合理。

**Layer-wise / parameter-group multiplier。** Fine-tuning 中可以让靠近输入的 pretrained layers 使用较小 multiplier，
让新 task head 或上层更快适应；ULMFiT 的 discriminative fine-tuning 是这类思想的早期实例。它的理由是保留可迁移
表示并减轻 catastrophic forgetting，不是“低层梯度天然更容易爆炸”。在从零 Pretraining 中，不存在脱离架构和
数据的通用“越深 learning rate 越大/越小”规律。

**Layer-wise trust ratio。** LARS/LAMB 根据 parameter norm 与候选 update norm 形成 group/tensor-level ratio，最初用于
large-batch training 的尺度失衡。LARS 在其 CNN workload 有效，但 LAMB 论文也明确指出 LARS 在 BERT 等 Attention
模型上并不一致；这正说明 layer-wise adaptation 是 optimizer/workload branch，不是普适深度修复。

另外，第 17 章的 residual scale、gate、DeepNorm，以及本章前述 `alpha(layer, step)` progressive residual warmup，
改变的是 forward contribution 与 backward path。它们即使也依赖 layer 和 step，也不能被称为 per-layer learning rate。

#### 哪些情况下值得引入 `m_l(s)`

至少出现以下一种可重复证据时，才值得进入实验：

- Fine-tuning 中底层出现 collateral drift，而上层/新 head 明显欠适配。
- 新增或扩容参数的 optimizer state 从零开始，需要独立 rewarm；旧参数仍应保持小 update。
- Large-batch 下不同 parameter groups 的 update-to-weight ratio 跨多个数量级，并与收敛问题相关。
- 特定层的 gradient/update 长期被 clipping 或 precision floor 主导，且已排除数据、mask、loss reduction 和
  architecture 问题。
- Ablation 表明固定 multiplier 或 trust ratio 在 held-out quality、稳定性和 wall-clock 上优于只调 global schedule。

不应只根据 gradient norm 大小设 learning rate。若 `||g_l||` 小是因为 layer 已接近局部最优，强行放大会增加噪声；
若是因为 upstream Jacobian 已让 signal 消失，放大 optimizer step 只会放大残余噪声；若 parameter scale 本身较小，
绝对 update 小也可能已有很大的相对变化。更有意义的观测是：

```text
gradient_rms_l
update_rms_l
parameter_rms_l
update_to_weight_l = update_rms_l / (parameter_rms_l + epsilon)
clipping_fraction_l
overflow_or_underflow_l
held_out_delta by layer/group ablation
```

#### 动态逐层控制带来的新状态

让 `m_l(s)` 根据在线 gradient 或 validation signal 自动变化，会把 controller 变成训练状态：

```text
layer identity + global step
+ controller statistics / EMA / thresholds
+ multiplier history and bounds
+ optimizer moments and scheduler phase
```

这些状态必须进入 checkpoint，并在 DP/TP/PP ranks 上一致。否则 resume、reshard 或 layer renumbering 会静默改变
trajectory。Controller 还可能追逐 noisy batch、在 layers 间振荡、补偿错误 objective，或因 validation feedback delay
形成过时决策。固定 parameter groups 在证据不足、恢复/复算优先时更安全；动态策略应有 multiplier bounds、更新
cadence、holdout gate、rollback 与“退回 global schedule”的 fallback。

结论可以浓缩为：

```text
先修 gradient path / initialization / normalization
→ 再修 data, loss reduction and precision
→ 选择 global LR + warmup/decay + clipping guard
→ 检查 optimizer 与 per-layer update evidence
→ 最后才实验 fixed 或 dynamic layer multipliers
```

逐层 learning rate 是 update actuator，不是深层网络稳定性的第一性原理答案。

### Gradient Clipping 的正确边界与顺序

Global-norm clipping 将所有参与参数视为一个拼接向量并按同一比例缩放；per-group clipping 会改变不同 groups 的
相对方向。两者都应记录 aggregation scope、norm type、threshold 与 clipping frequency。Distributed training 中，
必须先明确 gradient 是 local、ReduceScatter shard 还是已经完成 DP reduction 的 global semantic gradient，否则
“相同 max norm”并不代表相同 update。

Mixed precision 下若 loss 被 scale，clipping 必须作用于 unscaled gradients；PyTorch AMP 官方示例也要求先
`unscale_` 再 `clip_grad_norm_`，随后才执行 optimizer step。否则 threshold 实际约束的是人为放大的 gradient。

```text
backward on scaled loss
→ aggregate / accumulate under declared semantics
→ unscale gradients
→ measure unclipped norm and non-finite state
→ clip if needed
→ optimizer step
→ scheduler step
```

Clipping 适合阻止少数异常 step 破坏 checkpoint；若长期高频触发，应降低到根因诊断，而不是继续把 threshold 调小。

#### 从 Vector Norm 进入 Matrix Spectrum

<!-- semantic-body-binding:SF-GRADIENT-CLIPPING-BEYOND-VECTOR-NORMS-A-SPECTRAL-APPROACH-FOR-MATRIX-VAL:start -->
Global-norm clipping 假设异常主要表现为整体 update magnitude；当少数数据 outlier 只放大 weight-gradient matrix 的
几个主奇异方向时，统一缩放会同时压低大量稳定方向。Spectral clipping 保留 singular directions，只钳制超过阈值
的 leading singular values，因此把 actuator 从“整个向量”细化为“矩阵的主放大模式”。阈值与 randomized truncated
SVD 近似都成为 optimizer-side state，必须记录 cadence、rank、误差和额外 kernel cost。

它获得的是更有选择性的异常抑制，不是自动更好的收敛；低秩假设失效、谱估计滞后或矩阵很小时，分解成本和近似
误差可能超过收益。频繁触发仍要求回查数据、loss、precision 与 optimizer 根因。Global norm 在通用、低开销和
分布式聚合语义清晰时继续作为默认 guard，spectral 分支只在可观测的低秩谱异常与端到端训练证据同时成立时启用。
<!-- semantic-body-binding:SF-GRADIENT-CLIPPING-BEYOND-VECTOR-NORMS-A-SPECTRAL-APPROACH-FOR-MATRIX-VAL:end -->

## Mixed precision 为什么不是简单改 dtype

FP16、BF16 或更低精度可以减少 memory、communication bytes 并利用专用硬件，但训练需要维持数值范围和累积精度。

系统可能使用：

- 低精度参数或计算。
- 更高精度 master weights 或 optimizer states。
- FP32 accumulation。
- Dynamic loss scaling，尤其用于 FP16 underflow 风险。

所以“模型以 BF16 训练”并不能唯一确定每份状态的 dtype。Checkpoint、optimizer memory 估算和 collective bytes 都必须基于实际 precision policy。

### Precision Policy 应沿误差传播路径分区

训练中的 operator 即使都表现为 GEMM，也不具有相同的误差容忍度。Forward activation 的局部误差只需
在当前输出尺度下足够小；backward 中的弱信号还会被后续乘法、跨层传播、optimizer accumulation 和漫长
训练 horizon 反复放大。因而更可靠的问题不是“这个模型用几 bit”，而是：

```text
tensor / sub-expression identity
+ numerical scale and sensitivity
+ upstream quantization error
+ downstream amplification path
+ accumulation and optimizer horizon
+ batch-noise floor
-> precision / scaling / accumulation policy
```

Attention backward 提供了一个受限但有解释力的例子。若 softmax 输出为 `P`，上游梯度为 `dP`，其
score gradient 具有如下结构：

```text
dS = P * (dP - row_sum(P * dP))
```

这里的减法会抵消共同分量，`dS` 可能远小于 `P` 或 `dP`。若在产生这个微小差值之前就粗粒度量化
`dP`，量化噪声可能超过真实信号，再经 `dQ`、`dK` 路径放大。一个 sensitivity-aware policy 可以让前向
`Q/K/V/P` 使用更低精度，同时对关键的 `dP` 或 accumulation 保留较高精度，并只量化已经完成敏感
变换后的子路径。这里的长期原则是 **precision boundary 要跟随误差形成的位置**，不是任何一组固定
dtype 或 kernel 配方。

数值变换也必须与数学不变量一起验证。例如 softmax score gradient 的 row sum 为零，可以支撑某些只
改变公共分量的平滑变换；对另一 operand 做表面相似的 smoothing，若需要额外 correction，就可能重新
注入量化噪声。不能因两个输入都进入同一次矩阵乘就假设它们有对称的处理空间。

Kernel 吞吐只有在 trajectory invariant 基本成立后才有意义。至少应同时比较 full-precision reference、
loss/gradient divergence、长 horizon 收敛、不同 sequence length、batch 与 optimizer 设置，以及端到端
step time。更大的 batch 可能用 gradient noise 掩盖量化误差，较短 run 也可能来不及暴露累计偏差；这两者
都不能证明低比特路径在更大模型或更长训练中稳定。全精度 backward 在敏感信号尚未定位、复现成本可
接受或训练失败代价很高时仍是合理旧方案；常规 mixed precision 适合已有成熟 scaling/accumulation 的
算子；sensitivity-aware 分区则用更复杂的 kernel、scale metadata 和验证矩阵换取进一步压缩。

低比特误差也可能不是少数孤立 outlier，而是沿 token 方向共享的 coherent mean。直接用 block extreme 定标
简单、容易映射硬件；SVD/whitening 能分离 dominant direction，却很难进入每步训练热路径。一条较窄的结构
分解是先把 activation 或 output gradient 写成 shared mean 与 residual，再分别量化和累积：

```text
X = broadcast(mean(X)) + residual(X)
-> quantize mean and residual under separate scales
-> reconstruct GEMM from residual and cross terms
```

它通过改变 quantizer 所见 distribution 保存 long-tail variation，却新增 mean reduction、subtraction、额外
cross terms 与融合要求；microbatch/sequence composition 改变时，mean 本身也是漂移状态。Averis 的受限实验
支持这种 source-aware split 在其 FP4 training graph 中缩小数值差距，不证明 column mean 是所有层、模型与训练
阶段的 dominant error，也没有公开硬件吞吐合同。Vanilla FP4 在偏置弱时更简单，FP8/BF16 在同步成本、
实现成熟度或失败代价优先时继续成立；是否采用分解必须同时看 convergence 与 end-to-end step time。

### 低比特 Training Graph：无偏不等于免费

保留高精度 master weights 最容易维持 optimizer trajectory，却让静态状态继续主导显存；直接删除 master
copy 可以降内存，但持续 rounding bias 会进入 momentum 并累积。两条实验性分支分别处理这种误差：

```text
quantized weight update
→ feed quantization residual into optimizer momentum

FP4 forward/backward
→ stochastic rounding
→ rotate and rescale backward operands
→ keep gradient estimator approximately unbiased
```

前者复用 optimizer state 承载 error feedback，新增 state semantics 与 checkpoint compatibility；后者把
rotation、microscale、re-quantization 和 hardware tile constraint 纳入 computation graph，小矩阵可能被
overhead 吞没。无偏 estimator 只约束期望误差，不自动证明有限训练 horizon、任意 optimizer 或终局质量；
BF16/FP8 在 debug、旧硬件、小矩阵或 accuracy-first 场景仍成立。低比特证据必须同时绑定 forward、
backward、optimizer state、rounding、硬件和端到端收敛，不能只报 tensor-core peak。

#### Optimizer State 的量化误差会沿时间累积

低比特 optimizer state 不是一次静态压缩。Adam 的一阶、二阶状态是跨 step 的 EMA；量化器每次读写都会改变下一次 update 的输入，因此同样的 tensor reconstruction error 可能产生两类不同的动态失败。

<!-- semantic-body-binding:SF-2025-SOLO:start -->
当 magnitude-like EMA 采用只表达非负值的粗粒度编码时，历史大值可能让新产生的小信号长期落在量化格以下；当 signed momentum 过粗时，误差又可能翻转或放大方向，逐步累积为 update variance。因而 state format、momentum coefficient、scale update、zero handling 与 checkpoint restore 必须共同成为 optimizer identity，而不能只报告“2-bit state”。Log quantization 与 precision-specific momentum 是一种受限修复：它用更复杂的编码、kernel 和迁移语义换取较低 state memory；作者实验不覆盖所有 optimizer、长周期训练、分布式恢复或任意数值格式。训练规模较小、稳定性优先或无法验证长 horizon 时，高精度 optimizer state 仍是 canonical baseline。
<!-- semantic-body-binding:SF-2025-SOLO:end -->

#### 量化前可以训练 Gauge，而不改写原 Objective

量化困难不仅取决于数值大小，也取决于在等价表示中选择了哪个 basis。某些成对正交变换在 full precision 下保持 Transformer 输出不变，却会因 element-wise quantization 不与 rotation 对易而产生不同误差。

训练期可以用 stop-gradient 的 outlier proxy 只更新 gauge/basis，让 LM weights 仍由原 objective 更新。这样把“改变模型学什么”与“选择更适合量化的等价表示”分开，却新增 optimizer/export state、MLP runtime transform 与 kernel compatibility。短 continued-training 的 fake-quantization 结果只支持机制可行，不证明 full pretraining、真实 low-bit kernel 或 serving 加速。

### 从固定 Objective 到 Feedback-guided Self-supervised Update

固定 next-token objective 的优点是反馈来源稳定、覆盖广；SFT/RL 直接使用 labels/verifier，更贴近任务但改变
训练阶段。一条中间分支让少量 downstream examples 只产生 detached gradient direction，用它选择或构造
当前 batch 的 self-supervised target，再由 learner 继续优化 pretraining loss：

```text
feedback batch → detached downstream gradient
candidate self-supervised targets → candidate pretraining gradients
choose target by local gradient alignment
learner updates only on unlabeled batch
```

它把 checkpoint-level data retuning 推进到 step-level objective selection，却不再是无条件 unsupervised：
feedback distribution、designer version 与 alignment approximation 都属于训练 identity。局部 gradient alignment
不保证长期 trajectory，更可能牺牲 general capability；无可信 verifier 或多域冲突强时固定 objective 仍更稳。

### Mid-training：能力生产链中的独立阶段

把 pretraining 直接接到 SFT/RL，边界清晰且便于归因；但长上下文、特定领域或推理能力若在基础表示中
尚不可达，post-training 往往只能改变行为而难以重建底层能力。Mid-training 在通用预训练之后继续使用
大规模 language-model objective，却有目的地调整数据 mixture、长度或难度，再交给 SFT/RL：

```text
general pretraining
→ targeted mid-training
→ retention / context restoration
→ SFT and outcome-driven specialization
```

它不是一个可随意命名的“中间 checkpoint”。阶段 identity 至少包含入口 checkpoint、数据与长度分布、
objective、token/compute budget、merge/retention policy 及出口 evaluation。定向数据能提高目标能力，也会
造成通用能力回退、污染或难度过滤器过拟合；因此需要与继续通用 pretraining、直接 SFT/RL 做 compute-
matched 对照，并保留 restoration 分支。目标分布小、demonstration 可信时直接 SFT 仍更便宜。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-02087:start -->
行为规范也可以在这里成为显式训练资产。只在后续 SFT 中提供少量“应该怎样回答”的 demonstration，数据便宜但规则往往欠指定，模型可能把表面动作泛化到错误场景；在 mid-training 先同时学习 spec 的内容、适用条件与 rationale，可以让后续 alignment example 被解释为某个版本化 policy 的实例，而不是孤立答案。

```text
versioned behavior spec corpus
→ mid-training on rule, rationale and boundary cases
→ demonstration / preference alignment
→ held-out conflict and underspecification evaluation
```

spec corpus 由 policy owner 管理，training run 只产生候选 weights；模型理解 rationale 不等于始终遵从，更不等于规则正确。该分支用额外 token、policy version coupling 和 mis-specification/poisoning surface 换更一致的归纳偏置。synthetic specs、有限模型和窄 alignment setting 不能证明普遍价值对齐；规则频繁变化、需要立即撤销或高风险授权时，运行时 policy 与 deterministic enforcement 仍不可替代。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-02087:end -->

#### Skill Artifact 是结构化能力数据，不是行为证明

普通语料提供描述，trajectory 提供一次执行过程；带接口、步骤、前后置条件和 reference 的 skill artifact 位于两者之间。
把它加入 targeted pretraining 可以让模型更早接触可组合的能力结构，但 artifact 被读入 weight 不等于能力已在真实环境中
成立。训练 identity 至少还要保存 skill source、license、版本、适用环境、依赖、coverage 与去重关系，并把执行验证留给
后续 SFT/RL/Evaluation：

```text
versioned skill artifact corpus
→ capability-structured pretraining signal
→ trajectory / environment post-training
→ executable evaluation and adoption
```

收益是减少纯自然语言描述与执行轨迹之间的结构缺口；代价是 skill 质量不均、过时接口、数据污染与虚假可执行性。
当 skill corpus 小、provenance 不清或真实 demonstration 充足时，直接用经过验证的轨迹仍更可靠。

#### 相同阶段终点不代表相同后续可训练性

Checkpoint 是否适合下一阶段训练，不能只由最终 loss 或 post-SFT benchmark 判定。两个分支即使在 SFT 后几乎同分，只要进入 SFT 前的最后 pretraining window 不同，面对同一 DPO 或 RL update 仍可能沿不同轨迹移动。因此 artifact identity 还要保存 ordered data window、入口 checkpoint、token budget 与后续 update reference，并比较 stage-wise erosion / retention，而不只看终点。

这项结论来自小模型、500M-token 受控 intervention 与特定 refusal 指标，不支持“把某类数据最后训练”的通用 recipe。它增加 lineage、matched downstream update 和能力 retention 的评估成本；在 saturated scale、其他能力或更大模型上必须重新验证。若后续阶段弱、窗口差异可忽略或 lineage 成本过高，按阶段终点评估仍是合理基线。

Mid-training objective 也可以从随机 token/span corruption 进一步利用程序结构：先抽取 function、dependency 或
call boundary，再要求模型重建被遮蔽的实现与接口。随机遮蔽在通用语料、解析器不可靠时覆盖更稳；结构感知
reconstruction 在代码依赖可恢复时能把训练压力集中到跨段语义关系：

```text
random token / span corruption
→ syntax-bounded masking
→ dependency-aware function reconstruction
→ behavior post-training and executable evaluation
```

收益是更直接地训练跨函数依赖，代价是 parser、language、teacher、repository sampling 与 corruption policy 都
进入数据/objective identity。重建成功也不等于生成的程序正确，更不证明该 objective 跨语言或跨 domain 优于
next-token baseline；必须保留未见 repository、可执行测试和通用能力 retention。解析失败、自然语言主导或目标
能力可由可信 SFT 提供时，随机 objective 仍是更便宜的旧方案。

### Adaptive Depth：计算量也可以成为训练出的状态

固定层数让每个 token 走相同计算图，最适合 dense batching、kernel fusion 与可预测 latency。若模型将同一
block 重复应用，并学习 token-level exit/continue policy，就能把“多深”从架构常数变成条件计算决策；
再用 latent-step reward 同时约束 accuracy 与 compute，可把 recurrent depth 纳入训练目标。

这条分支用潜在的 token-level compute 节省换来 exit calibration、不同 token 进度、batch divergence、
KV/activation identity 与恢复复杂度。它在作者受限实验中是 `Status: Experimental`，不能据此断言实际
wall-clock 或 energy 一定下降。硬件偏好规则 shape、SLO 要求稳定、exit policy 漂移或缺少专用 kernel 时，
固定深度仍是更好的系统设计。

## Activation checkpointing 移动了什么瓶颈

Backpropagation 需要 forward activations。全部保留会占据大量显存；activation checkpointing 只保存部分边界，backward 时重新计算中间 activations：

```text
less saved activation memory
<-> more recomputation FLOPs
```

它减少的不是 parameters、gradients 或 optimizer states。第 39 章 ZeRO 主要处理 model-state redundancy，两者解决不同 memory categories，可以组合。

Checkpoint 这个词在这里容易混淆：activation checkpointing 是计算图重算策略；第 35 章的 training checkpoint 是持久化恢复状态。

## Scaling 不是只增加参数

第 7 章已经说明 Scaling Laws 是经验规律。Pretraining 需要同时分配：

```text
model parameters
training tokens
compute budget
data quality and mixture
```

只增大参数而训练 tokens 不足，模型可能 undertrained；只增加重复低质量 tokens，也不会获得与独立高质量数据相同的收益。Compute-optimal 分配是特定模型家族、数据和预算下的经验决策，不是永恒常数。

Pretraining loss 曲线还不能直接解释具体能力。某些能力只在合适 prompting、post-training 或 Evaluation 中显现；另一些平均 loss 改进可能集中在高频简单 tokens。

### Scaling-law Pilot 也是有预算的实验调度

预先跑固定网格再拟合 scaling law，在候选规模少、单次实验便宜且目标区间接近观测区间时最透明。实验成本随规模快速增长后，pilot 本身已经是一项预算分配：不同 run 成本不同，对高成本 target region 的外推信息量也不同。

<!-- semantic-body-binding:SF-2026-ARXIV-2604-22753:start -->
一种条件分支把待跑配置、成本、当前拟合后验与目标区域写成 versioned experiment state，每一步选择最能减少目标区外推不确定性的下一项实验，再用新结果更新选择策略。Scheduler 只拥有实验 proposal；训练结果、拟合模型和独立 holdout 共同决定 scaling-law artifact 是否可用。它能把预算集中到信息量高的 runs，却依赖不确定性校准、候选池与成本 proxy，且一次或近视选择可能错过更好的组合。后验不可信、目标区改变或需要审计可比性时应回退预定义 grid。作者只在其 scaling-law tasks 与 mixture approximation 下展示效果，不证明可安全规划任意大模型训练。
<!-- semantic-body-binding:SF-2026-ARXIV-2604-22753:end -->

### Training Budget 与 Test-time Compute 必须放进同一生命周期目标

传统 early stopping 只观察 validation curve，并隐含假设部署时每个请求只产生一个答案。这个旧方案在
single-pass latency 严格、部署量大或没有可靠 verifier 时最清楚。若部署允许对同一问题采样多个候选并搜索或
验证，模型 checkpoint 与 test-time budget 就共同决定任务质量：较早停止训练可能以更高的每请求推理成本
补回部分差距。

```text
choose checkpoint c and test-time budget K
to satisfy quality and latency constraints
while minimizing
training_compute(c) + deployment_volume * inference_compute(c, K)
```

这不是“少训练一定更省”。Learning-curve 与 `K`-quality curve 都是估计；Pass@K 只说明候选集合覆盖，
不等于 selector 能稳定产出一个正确答案。Verifier、并行 sampling capacity、output length、tail latency、
refresh frequency 和 deployment volume 变化后，原先的 break-even 会移动。高流量长期服务通常会把节省的
一次性训练 FLOPs 重新付给推理；低频专用模型、训练极贵且可并行验证的任务则可能采用另一 operating point。

TTC-aware early-stopping 的预印本在有限模型、checkpoint 和代码/数学 benchmark 上展示了联合选择的可行性；
它没有证明其 curve family 能外推到更大模型或开放任务。长期结论是：**early-stop decision 必须携带预期部署
workload，而不是只携带 validation loss；上线后也要用实际 query volume、K、quality 与 SLO 重算生命周期账本。**

### Activation Sparsity 可能来自 Optimizer–Activation Coupling

把激活稀疏视作架构或数据的静态性质，会忽略初始化阶段的方向性更新。正偏激活配合标准 loss 时，权重可能出现系统性 negative drift，逐步把更多 unit 推入非激活区，并在少数剩余路径形成 spike。

这条解释要求联合观察 activation distribution、weight drift、gradient 与 optimizer state；它不是“负漂移总是有害”或默认正则收益。初始化、activation、normalization 或 objective 改变后机制可能消失；证据不匹配时回到常规稳定性诊断，而不是机械修正权重符号。

它相对只看 loss/gradient norm 的收益，是把异常进一步定位为可检查的 optimizer–activation coupling，从而决定应调整初始化、激活、归一化还是更新规则；代价是额外采集分层 activation/weight/optimizer 统计，并引入可能干扰训练的诊断或 actuator。现有 exact-v1 只覆盖其形式化例子与披露的 architecture、initialization、activation 和 optimizer 实验，不证明其他组合存在同方向漂移，也不提供通用在线控制器。

<!-- source-family:SF-2026-ARXIV-2605-17659 -->

### Regularization 必须匹配 Deployment Shift 的方向

不知道部署偏移方向时，均匀分散的正则化是合理 baseline，因为它不押注某一脆弱轴；如果 shift direction 已被可靠观测，matched penalty 才能把容量集中到真正变化的子空间。Training run identity 因而要绑定 shift hypothesis、penalty axis、estimator revision 与 held-out shift set，不能只记录一个正则系数。

定向约束可能降低 residual error，却会在轴选错时制造新的 residual floor，并增加估计与调参成本；未知或快速变化的分布应回退 even-spread baseline。arXiv:2605.22800v1 的理论和深网实验只支持论文假设与受测设置，不构成所有架构和真实部署偏移下的普遍定理。

<!-- source-family:SF-2026-ARXIV-2605-22800 -->

## 训练稳定性是多层系统问题

Loss spike 或 NaN 可能来自：

- 异常或极长 data batch。
- Learning rate、initialization 或 optimizer 配置。
- Low-precision overflow/underflow。
- Collective、硬件或 silent data corruption。
- 恢复 checkpoint 后状态不一致。
- 不同 ranks 读取到不同 batch 或参数。

因此监控不能只有平均 loss。至少应关联：

- Per-domain loss、token throughput 和 data source。
- Learning rate、gradient norm、clipping 与 overflow。
- GPU memory、step time、straggler 与 collective time。
- Skipped steps、retries、hardware errors。
- Checkpoint save/restore validation。

训练平台的价值，是把模型信号、数据身份与系统信号放在同一条 timeline 上。

### Operator-normalized Risk 把异常信号变成有预算的 Recovery Proposal

全局 gradient norm 在训练 recipe 稳定、算子尺度近似可比时，是发现整体爆炸的便宜 sensor；把不同 operator 的 raw norm 直接排序，则会把长期尺度差异误当作风险。更细的 runtime controller 可以让每个 monitored unit 维护自己的历史 baseline：长窗口 ratio 感知相对自身历史的偏离，短窗口 delta ratio 感知突发变化。两者只提交 risk signal；backend 预先声明哪些 operator、branch、block 或 layer 是 recoverable unit，以及各自有哪些低成本与 recovery execution path。

控制器再在 hard recovery budget、阈值与 lock interval 下选择少量高风险单元切换路径，其余单元继续低成本执行。这样改变的是每个 training step 的 execution routing，而不是 loss、numerical format 或 optimizer authority；controller statistics、threshold revision、recovery budget 与实际 route receipt 都必须进入 checkpoint / trace。收益是在少数局部异常出现时避免整步永久升级高精度，代价是额外 norm reduction、history state、route fragmentation，以及异常在不可恢复单元传播时的漏检。

该机制依赖 backend observability、可恢复执行单元和兼容的 recovery implementation；历史均值受污染、风险阈值漂移、budget 过小或频繁 lock 都可能让控制器错过故障或过度回退。论文的结果绑定 activation-quantization、DeepSeek-style mixed-precision 与 LLaMA-2 13B stress settings，不证明跨 backend 的通用低精度稳定性。缺少 operator identity、recovery path 或 matched high-precision canary 时，应继续使用全局 clipping、loss scaling、skip/retry 或整步高精度 fallback。

<!-- source-family:SF-2026-ARXIV-2606-00539 -->

### “训练仍在运行”与“会得到好模型”之间隔着多层证据

超长训练最危险的误判，是把一条平滑下降的 training loss 当成最终质量证明。训练信号更适合作为分层证据：每一层能排除一部分故障，却没有任何单一信号可以提前担保 checkpoint 的产品价值。

| 信号层 | 主要观测 | 能支持的结论 | 不能单独证明 |
| --- | --- | --- | --- |
| Objective | training/validation loss、per-domain loss、PPL | 当前 objective 在声明的数据与 mask 上是否改善，是否出现过拟合或 domain divergence | 事实性、指令遵循、安全与产品任务质量 |
| Update | gradient norm、update-to-weight ratio、clipping frequency、optimizer moments | 是否存在爆炸、消失、异常 step 或 group-wise update 失衡 | 梯度方向是否代表正确数据与目标 |
| Numerical | non-finite count、loss scale、overflow/underflow、skipped step、activation/logit range | mixed-precision path 是否还能产生有限、可执行的 update | 有限数值是否与高精度 reference 足够等价 |
| Data | source/domain mix、effective tokens、duplication、length、mask、batch identity | 实际消费分布是否符合 data contract，异常 loss 能否定位到样本 | 数据本身是否无偏、真实、合法或覆盖部署长尾 |
| System | step time、tokens/s、memory、collective、straggler、ECC/Xid、retry | 计算是否持续推进，故障或降速来自哪个 runtime/resource path | 高 utilization 是否产生正确的参数轨迹 |
| Evaluation | held-out loss、capability/safety suites、sample review、scaling probe | 中间 checkpoint 的可观察能力、回退与趋势 | 未测分布上的最终泛化，或未来规模必然延续当前趋势 |

这些信号必须按 `run / checkpoint / step / data batch / rank` 对齐。一次 loss spike 与同一步的 gradient spike、异常 batch、loss-scale backoff、collective retry 或 device error 相关联，才可能把“现象同时发生”推进到可检验的根因假设。只看全局平均会把单个 domain、layer、rank 或 expert 的退化稀释掉；只看最细粒度指标又会产生噪声和监控成本，因此应保留 global trend、分层 slice 与按事件下钻三档视图。

判断是否值得继续投入剩余训练预算，还需要预先定义 gates，而不是在曲线出现后解释：相对小规模或先前 run 的 loss/token 轨迹是否落在容差带内，held-out quality 是否随 compute 改善，关键能力是否回退，数据与系统异常是否已被解释，最近 checkpoint 是否通过 restore/continuation canary。通过这些 gates 只能说明“当前 trajectory 仍值得继续”，不能证明最终模型一定优秀；最终结论仍属于独立 Evaluation。

### Elastic Recovery 的目标不是“重新跑起来”

超大规模训练把故障恢复从 process restart 提升为 trajectory correctness。若坏掉的 accelerator
被替换、slice 重新划分或 collective group 重建，平台还要回答：重新开始的 step 是否消费了
同一批 tokens，optimizer/scheduler/RNG 是否来自同一提交点，以及疑似 silent corruption 之后
哪些 step 必须回滚。

```text
detect fault or corruption
→ choose last validated commit point
→ restore model / optimizer / scheduler / RNG / data cursor
→ rebuild topology and shards
→ deterministically replay or explicitly start a new trajectory
```

传统的固定 topology checkpoint 仍然合理：它的状态映射简单、恢复路径更容易验证。Elastic
slice replacement 用更高的 resharding、replay 与一致性复杂度，换取长时间训练对频繁硬件故障
的容忍。公开技术报告可以证明这种 resilience contract 已进入 frontier training system，但不能
在没有 checkpoint continuity、data cursor 与 RNG 细节时断言 bitwise exact recovery。第 35 章
拥有持久状态，第 36～41 章拥有 topology/runtime；本章只规定恢复后不能静默改变训练语义。

### 自主训练控制必须被 Safety Envelope 包围

固定 learning-rate schedule、gradient clipping 和人工停机容易复现，也是默认基线；在长时间训练和运行时 stress 下，它们对突发 spike、degraded run 或资源浪费反应较慢。optimizer 之上的 control layer 可以读取 versioned telemetry，提出调低步长、暂停、回滚等 bounded actions，但 action budget、cooldown、approval 与 human override 必须由训练控制面持有。

收益是更快限制损失扩散和无效 compute；代价是 controller 误判、观测延迟、控制振荡以及对 telemetry 的新依赖。证据不足、动作越界或 controller 自身异常时，应恢复静态 recipe/停止训练，而不是自主扩大权限。exact-v1 只支持其披露 simulator/recipe 与 stress runs，不证明真实超大规模训练的稳定性、效率或最优控制策略。

<!-- source-family:SF-2026-ARXIV-2605-19008 -->

## Pretraining 没有解决什么

Next-token training 可以形成广泛能力，却不直接规定模型应如何响应用户。互联网文本包含描述、争论、错误和危险行为；“预测文本分布”与“遵循意图”不是同一目标。

因此后续能力生产分成几条路径：

```text
Pretraining  learn broad conditional structure
SFT          imitate desired demonstrations
RLHF/DPO     optimize relative preferences
LoRA         parameterize a cheaper task-specific update
```

这些阶段可以增加、改变或损伤已有行为。Post-training 不是给模型添加一个无风险 UI 层，而是在继续修改参数分布。

### 条件化机制分支与共存边界

主线之外仍存在若干只在特定前提下成立的设计分支。下面按状态与控制权的变化说明它们解决的问题、新增代价及回退边界；来源身份和实验限制统一留在章末 Review notes。

<!-- source-family:SF-2026-ARXIV-2605-28760 -->

无法或不愿保留 backward graph 时，zeroth-order fine-tuning 可用成对参数扰动的 forward score 估计更新方向；它把训练的主要成本从反向传播转成多次推理。Optimizer owner 仍必须拥有 perturbation seed、objective、direction estimate 与 update commit，推理 runtime 只能作为批量 forward executor，不能因执行请求而取得参数更新权。

这条分支减少 autograd/activation state，却增加估计方差、forward 次数、参数同步和对噪声尺度的敏感性；维度很高或 objective noisy 时可能比反向传播更贵、更不稳定。梯度可得且显存允许时，一阶优化仍是默认；黑盒、低内存或少量可训练参数场景才值得尝试。exact-v1 的系统结果只属于披露模型、任务与硬件，不证明 serving engine 普遍能高效替代训练 runtime。

<!-- semantic-body-binding:SF-2026-ARXIV-2606-06888:start -->
数据受限的预训练会反复消费同一 token，普通 scaling law 因而不再只由总 token 数决定。Masked-input regularization 把重复样本的一部分输入随机遮蔽，以降低记忆化并改变 compute/data 最优点；证据只覆盖作者固定 architecture、optimizer、至多 1.4B 参数和 400M unique tokens，不能外推为任意重复率下的通用最优策略。
<!-- semantic-body-binding:SF-2026-ARXIV-2606-06888:end -->

### Optimizer State 也必须服从数据与硬件契约

在差分隐私训练中，先过滤梯度再加噪并不只是一个数据预处理步骤：过滤改变了创新项的条件分布，直接影响 AdamW 的一阶、二阶矩估计。若继续沿用未过滤 DP-SGD 的 bias correction，优化器会把过滤造成的统计偏差误当成真实方向尺度。Filter-aware correction 能补偿这类偏差，但依赖过滤器和噪声模型被准确记录；模型失配时，保守的 DP-SGD 或重新校准仍是必要 fallback，而不能因为 loss 下降就假定隐私与收敛同时成立。

<!-- source-family:SF-2026-ARXIV-2605-03425 -->

低秩分解也只有映射到硬件支持的执行结构时才会产生真实吞吐。将低秩参数化与 2:4 structured activation sparsity 联合设计，可能同时降低算术与内存成本；代价是稀疏模式、kernel 可用性和精度恢复一起成为训练 artifact 的一部分。没有对应 kernel 或 workload 不能维持结构稀疏时，普通 dense/low-rank 训练仍可能更快。

<!-- source-family:SF-2026-ARXIV-2605-03667 -->

最后，非平稳目标会暴露 optimizer memory 的差异：Adam 的自适应矩帮助快速跟踪，却也会把旧阶段统计带入新阶段；SGD 忘得更快，但在噪声和尺度不均衡时适应较慢。因此 optimizer 选择不是“谁普遍更好”，而是 drift rate、投影约束、阶段边界与状态重置策略的联合决定。[受限证据：arXiv:2605.03425v1、2605.03667v1、2605.04269v1]

<!-- source-family:SF-2026-ARXIV-2605-04269 -->

### 稳定训练从经验 Trick 走向显式几何与预算控制

当激活尺度和更新方向只靠 clipping、normalization 等经验规则约束时，训练稳定性往往表现为“换一组超参数就失效”。更可解释的分支是把 activation scale 与 update geometry 写成显式 manifold constraint，使允许的参数移动、数值范围和恢复条件都能被测量。它以额外投影、约束计算和可能受限的可达解空间，换取更清楚的稳定边界；约束与真实 loss geometry 不匹配时必须回退到未约束优化并重新校准，而不是把低 loss 当作约束正确的证明。

同理，optimizer configuration 不应永远是静态配方。给定 wall-clock、memory、energy 或 trial budget，系统可以把 optimizer、学习率和正则组合当作有成本的控制选择，通过小规模测量更新 cost/performance model，再决定是否扩大训练。收益是把调参预算显式化；代价是代理 workload 与完整训练之间可能错配。预算太小、phase 转移或数据分布变化时，保守的已验证 recipe 仍是合理 fallback。

### Weight Decay 通过全局参数交互改变 Sharpening

把 weight decay 理解成每个参数独立的局部摩擦，便于解释正则化，却不足以说明深网接近 edge-of-stability 时的曲率演化。更新所有参数的收缩会改变层间尺度与组合函数，进而通过全局交互影响 progressive sharpening；因此“加入 decay 后更稳定”不能只归因于单点 gradient 变小。

这条机制要求把 decay、learning rate、normalization、architecture、loss curvature 与参数范数一起做 matched run。它能解释特定设置中的稳定性变化，却不证明 weight decay 对所有模型都提高稳定性；强 decay 还可能损害拟合或改变最终 function。架构、数据或 optimizer 不匹配时，应回退经验证的原 schedule，并用 loss spike、谱/曲率、update ratio 与下游质量共同判断。

<!-- source-family:SF-2026-ARXIV-2605.16622 -->

<!-- source-family:SF-DEMYSTIFYING-MANIFOLD-CONSTRAINTS-IN-LLM-PRE-TRAINING -->
<!-- source-family:SF-BUDGET-AWARE-AUTO-OPTIMIZER-CONFIGURATOR -->

### 低精度 Optimizer State 需要保持完整基底

直接把二阶 preconditioner 压到低精度，在小状态或条件数温和时能节省显存；大模型训练中，量化后的 basis 缺失会让更新方向失真。Optimizer owner 可以重参数化 preconditioner：用被更新的 basis vector 与未改变的向量共同维持完整基底，再以 BF16 存储。收益是降低状态开销并保留方向结构，代价是 basis 维护、正交误差和实现复杂度；数值漂移或 tested regime 外的谱结构会使收益失效，应回退到更高精度状态或更简单 optimizer。exact-v1 只支持论文五组实验和 Appendix C 的限制，不证明所有模型、硬件与长训练 horizon 的稳定性。<!-- source-family:SF-2026-ARXIV-2605-26327 -->

## 本章在知识树中的位置

```text
versioned data q(x)
-> causal next-token loss
-> gradients and optimizer state
-> repeated parameter updates
-> pretrained checkpoint
-> SFT / LoRA / preference optimization
```

第 27 章决定训练分布，本章决定基础 objective 与训练循环；第 29 章将目标收窄到指令 demonstrations。第 35～41 章再解释这段循环怎样被持久化并扩展到多 GPU。

在 Compute 横线上，第 14、17 章定义的 operator graph 到这里第一次成为反复执行的 training workload；第 37 章继续把单个 operator step 分布到多个 devices。这个连接属于执行映射的逐层展开，不表示训练 objective 与 Tensor Parallel 是同一层设计。

### Optimizer 也在选择参数空间中的方向尺度

把所有参数共享一个标量 learning rate，隐含假设是不同更新方向对 loss 的敏感度相近。深层 Transformer
并不满足这个假设：少数主导奇异方向可能对过大步长非常敏感，大量 bulk directions 却仍可承受更积极的
更新。逐参数自适应方法、矩阵正交化更新和统一标量步长因此不是简单的“谁更先进”，而是在估计不同粒度的
可行 update geometry。

一个实验性分支先用小规模 probe 估计各层更新谱，再把主导方向与 bulk directions 分开分配 step scale：

```text
layer-local gradient/update matrix
→ event-time spectral probe
→ head / bulk sensitivity estimate
→ bounded directional step allocation
→ loss-spike, update-ratio and downstream checks
```

它解决的是统一步长在不同谱方向上的过保守或过激，不是证明每层都应有独立、持续变化的 learning rate。
收益需要用相同 token budget、batch、precision、warmup、clipping 与 optimizer state 做 matched comparison；新增代价是
probe 成本、谱估计噪声、层间尺度漂移与更多控制状态。模型规模、数据分布或训练阶段改变后，旧谱先验必须重估；
当训练稳定、可观测性不足或控制复杂度超过收益时，统一 schedule 仍是更可靠的 baseline。

### Distillation 要分开 Prefix Provenance 与 KL Direction

Teacher-forced SFT、student-prefix DAgger、offline RL 和 on-policy distillation 常被统称为“向 teacher 学习”，但它们分别改变生成 trajectory 的 owner 与 KL 的方向。相同 teacher 在不同 prefix distribution 上给出的 target 不等价，forward/reverse KL 又对 mode coverage 与 mode seeking 有不同压力。

训练合同因此要冻结 prefix provenance、teacher/student revision、KL direction、sampling 与长度 curriculum；KL mixing 或 entropy-gated curriculum只是条件分支。它们用更多控制状态换 accuracy/diversity/compute 的折中，也可能造成 off-policy mismatch 和 coverage collapse；证据不足时回到单一、可重放的 SFT objective。

<!-- source-family:SF-2026-ARXIV-2605-16826 -->

## 从机制演进到系统设计

预训练优化最初用统一 optimizer 与全局 learning-rate schedule 管理所有参数；规模扩大后，width、depth、token budget、batch、warmup 和参数方向的敏感度发生非线性交互。因而 learning rate 不应按层数机械动态调整，而应先以 matched probe 判断哪些方向或尺度真正触及 stability boundary。

局部 spectral probe 或邻近规模 sweep 可以减少统一步长的过保守与过激，却增加测量噪声、控制状态和额外训练成本。任何外推都必须冻结 data、optimizer、schedule、precision 与 token budget；超出验证尺度时重新校准，而不是把局部幂律当成普遍规律。统一 schedule 在观测不足或收益不覆盖复杂度时仍是 canonical baseline。

## 自检问题

1. Next-token loss 怎样从 `[B,T,V]` logits 与 `[B,T]` labels 得到？
2. 小例子中 target probability 提高为什么会降低 loss？
3. Perplexity 跨 tokenizer 比较为什么可能无效？
4. `B_global`、effective tokens 和 optimizer steps 有何区别？
5. Gradient accumulation 节省了什么，没有节省什么？
6. Warmup、decay 与 gradient clipping 分别约束什么？
7. Mixed precision 为什么不能由一个 dtype 名称完整描述？
8. Activation checkpointing 与 training checkpoint 有什么不同？
9. Loss 下降为什么不直接证明事实可靠或指令遵循？
10. Pretraining 状态为什么不仅包含模型权重？
11. 两组参数表达同一个函数时，为什么 Adam 仍可能产生不同的 function-space trajectory？
12. 为什么 forward output 的量化误差可接受，不代表同一精度也适用于 backward 的弱梯度？
13. 如何区分真正的低比特收敛证据与被 batch noise 或较短 training horizon 掩盖的偏差？
14. 为什么允许 test-time sampling 后，early stopping 必须绑定 deployment volume、verifier 与 SLO？
15. Adam 的 per-coordinate adaptation 为什么不等于显式的逐层 learning rate？
16. 哪些 evidence 才足以支持 fixed 或 dynamic layer multiplier？
17. Mixed precision 与 distributed accumulation 下，gradient clipping 应在什么语义边界执行？
18. Training loss、gradient、数值、数据、系统与 Evaluation 信号分别能排除什么，又不能证明什么？
19. 为什么超长训练的 continue/stop gate 只能判断 trajectory 是否仍值得投入，不能担保最终模型质量？

## Module-wise Gradient SNR 是诊断信号，不是默认学习率配方

<!-- semantic-body-binding:SF-REVEALING-MODULAR-GRADIENT-NOISE-IMBALANCE-IN-LLMS-CALIBRATING-ADAM-VIA-:start -->
全局 learning rate 与 Adam 的逐参数自适应在大多数稳定训练中足够清楚；当不同 module 的 gradient signal-to-noise ratio 长期失衡，统一 schedule 可能让高噪声模块反复消耗更新预算。此时可以把 module-wise SNR 作为是否启用 group LR multiplier 的诊断输入：先证明失衡稳定存在，再对受影响模块有界调整，并把 estimator、window、module grouping 与 optimizer state 写入 checkpoint identity。

这个 actuator 可能减少无效更新，却增加估计噪声、跨阶段漂移和更多控制状态；低 SNR 也可能是数据稀缺或目标冲突的症状，不能只靠降低 LR 掩盖。估计未校准、训练阶段快速变化或收益不显著时，回退全局 schedule 与 Adam 基线。[受限证据：arXiv:2605.05794v1]
<!-- semantic-body-binding:SF-REVEALING-MODULAR-GRADIENT-NOISE-IMBALANCE-IN-LLMS-CALIBRATING-ADAM-VIA-:end -->

## 小结

Pretraining 用大规模 next-token prediction 把数据分布转化为参数更新。Cross-entropy 定义局部误差，optimizer 与 schedule 决定更新轨迹，参数块对称性限定哪些更新在重参数化后仍应等价；batch、precision、activation memory 和分布式执行决定这条轨迹能否在可接受成本内完成。

固定 recipe 是可复现基线；长程 stress 下可以增加受 safety envelope 约束的控制层，但它只能提出有界动作，不能替代训练目标与人工 override。预训练 checkpoint 是通用能力底座，不是最终产品行为；它是否可靠还需要独立 Evaluation 与后续训练约束。

## Review notes

- `SF-2026-ARXIV-2604-22753`（Status: Experimental）：exact-v1 支持把 scaling-law fitting 写成 heterogeneous-cost、target-region-aware 的 sequential experiment selection；mixture approximation、one-step policy 与 cost proxy 限制其外推。https://arxiv.org/abs/2604.22753v1

- Skill Pretraining（structured capability artifact as mid-training data；Status: Experimental）：
  https://arxiv.org/abs/2608.26563v1
  - 证据边界：作者构造与模型实验支持 skill artifact 作为训练信号；不证明数据中的接口可执行、跨环境迁移或
    可取代真实 trajectory / verifier。

- Spectral Allocation / SAMuon（direction-aware optimizer step allocation；Status: Experimental）：
  https://arxiv.org/abs/2608.25990v1
  - 证据边界：当前证据来自论文披露的 124M、300M、1B 规模和有限 batch/任务；不证明 frontier-scale
    训练、不同架构或任意数据分布都应采用相同 head/bulk profile。

- Final-window pretraining lineage and downstream-update response（matched post-SFT endpoint 不等于同一可训练性；Status: Experimental）：https://arxiv.org/html/2607.25063v1

- GaugeQuant: Online Learning of Quantization-Optimal Bases from LLM Symmetries（arXiv:2607.20757v1；Status: Experimental）：https://arxiv.org/html/2607.20757v1
  - 证据边界：支持两个模型、短 continued-training 设置中的 learned symmetry basis 与 fake-quantization perplexity；不证明端到端速度、硬件支持、完整预训练稳定性、通用低比特鲁棒性，或 proxy 会最小化真实 quantized loss。

- Structure-aware function reconstruction mid-training（Status: Experimental）:
  https://arxiv.org/abs/2607.12463v1

本章只负责 next-token objective、训练 step、token/batch 计量、optimizer state 与训练稳定性。数据治理留在第 27 章；SFT 和 preference optimization 留在第 29、31～34 章；collective、state sharding 和 framework runtime 留在第 36～41 章。

2026-W10 的 SageBwd 案例用于补全 backward sensitivity、precision boundary 与 convergence contract。
其公开实验仍限于作者的小模型与固定训练设置，相关 repository 也未定位到可核验的独立实现；因此
正文不保留吞吐数字，也不把该 precision partition 写成通用 recipe。

Progressive Residual Warmup 用于补足 residual branch activation 的 `layer × time` 状态与恢复边界；其固定 schedule、训练规模和稳定性结果只作为 Experimental evidence。

本轮训练健康审计把 objective、update、numerical、data、system 与 Evaluation 信号分层，并明确 continue/stop gate 的证明边界；指标集合参考 Megatron Core 当前官方 observability contract，但正文不把某一框架的 metric 名称写成通用标准。

Primary-source 校验入口：

- Diederik P. Kingma, Jimmy Ba, "Adam: A Method for Stochastic Optimization", 2014: https://arxiv.org/abs/1412.6980
- Yang You, Igor Gitman, Boris Ginsburg, "Large Batch Training of Convolutional Networks", 2017（LARS）:
  https://arxiv.org/abs/1708.03888
- Yang You et al., "Large Batch Optimization for Deep Learning: Training BERT in 76 minutes", 2019（LAMB）:
  https://arxiv.org/abs/1904.00962
- Jeremy Howard, Sebastian Ruder, "Universal Language Model Fine-tuning for Text Classification", 2018:
  https://arxiv.org/abs/1801.06146
- PyTorch AMP gradient clipping example:
  https://docs.pytorch.org/docs/stable/notes/amp_examples.html#gradient-clipping
- NVIDIA Megatron Core training metrics（版本化 instrumentation evidence）:
  https://docs.nvidia.com/megatron-core/developer-guide/nightly/user-guide/observability/metrics.html
- Alec Radford et al., "Improving Language Understanding by Generative Pre-Training", 2018: https://cdn.openai.com/research-covers/language-unsupervised/language_understanding_paper.pdf
- Tom B. Brown et al., "Language Models are Few-Shot Learners", 2020: https://arxiv.org/abs/2005.14165
- Jared Kaplan et al., "Scaling Laws for Neural Language Models", 2020: https://arxiv.org/abs/2001.08361
- Jordan Hoffmann et al., "Training Compute-Optimal Large Language Models", 2022: https://arxiv.org/abs/2203.15556
- Gemini 2.5 Technical Report（training-resilience bounded case）:
  https://arxiv.org/abs/2507.06261
- Devender Singh, "The Loss Does Not See the Basis, but Adam Does"（Status: Experimental）:
  https://arxiv.org/abs/2608.05136
- Jintao Zhang et al., "SageBwd: A Trainable Low-bit Attention", 2026（Status: Experimental；公开实现尚未定位）:
  https://arxiv.org/abs/2603.02170
- Progressive Residual Warmup（Status: Experimental）: https://arxiv.org/abs/2603.05369
- CompleteP（depth-wise HP transfer 与 non-lazy feature learning 的联合 parameterization contract；Status: Experimental）：https://arxiv.org/html/2505.01618v1
  - 证据边界：12%–34% 只属于作者模型形状、training recipe 与 Cerebras CS-3；不推出逐层动态 learning rate 的普适方向。
- SkewAdam / Tiered Optimizer State（exact v1 + event-time commit；Status: Experimental）：https://arxiv.org/html/2607.19058v1
  - 证据边界：6.78B total / 440M active、128 experts、约 81.9M tokens，H200 为主且有 H100/MI300X follow-up；不证明大规模 distributed wall-clock 或普遍收敛。
- FLOP-Efficient Training / TTC-aware Early Stopping（Status: Experimental）:
  https://arxiv.org/abs/2601.01332
- ECO Quantized Training（optimizer-state error feedback；Status: Experimental）:
  https://arxiv.org/abs/2601.22101
- SOLO（低比特 optimizer EMA 的动态误差与 precision-specific momentum；Status: Experimental）：
  https://arxiv.org/html/2505.00347v1
  - 证据边界：受限模型与训练设置中的 2-bit Adam-state 结果不覆盖所有 optimizer、长 horizon、分布式 checkpoint 或故障恢复；高精度 state 仍是稳定性基线。
- Quartet II（FP4 rotation/debiasing computation graph；Status: Experimental）:
  https://arxiv.org/abs/2601.22813
- ARO（optimizer update 的 adaptive rotation；Status: Experimental）:
  https://arxiv.org/abs/2602.09006
- Magma（dense optimizer state + masked parameter application；Status: Experimental）:
  https://arxiv.org/abs/2602.15322
- Learning What to Predict（feedback-guided self-supervised task construction；Status: Experimental）:
  https://arxiv.org/abs/2601.22108
- SPARKLING（state-aware width expansion；Status: Experimental）: https://arxiv.org/abs/2602.02472
- PRISM（targeted mid-training stage contract；Status: Experimental）: https://arxiv.org/abs/2603.17074
- LoopRPT（learned recurrent depth；Status: Experimental）: https://arxiv.org/abs/2603.19714

### Daily integration evidence trace

- `2026-05-04 / SF-2026-ARXIV-2605-02087` — exact-v1 `arXiv:2605.02087v1`；正文吸收 versioned behavior-spec midtraining 与 mis-specification boundary，不替代 runtime policy/enforcement。

#### 2026-06-29 source-specific Review notes

Review note：`SF-2026-ARXIV-2606-29158`；Method `https://arxiv.org/html/2606.29158v1 — §3 Power Laws for Optimal Learning Rates; 6 Explaining Nonlinear Scaling via Implicit Effective Learning Rate Schedule`；Evaluation `https://arxiv.org/html/2606.29158v1 — §4 Experiment Design; 5 Main Results`；未证明边界 `https://arxiv.org/html/2606.29158v1 — §7 Conclusions and Limitations`。

### Source-family integration record

<!-- june29-owner:TRAIN-PRETRAINING:start -->
### 2026-06-29 约束变化与机制增量

**Owner-merged 正文（覆盖 `SF-2026-ARXIV-2606-29158`）。** 现有 Pretraining 正文分离 optimizer、schedule、batch/tokens 与 scaling identity，但没有记录普通 LR 对 model/data scale 的非线性以及 effective LR 与 D-axis 外推的不同可靠域。 因此本次把这些增量合并到同一知识 owner：固定比例或单变量外推学习率会把 width、depth、token budget 与 schedule 的非线性交互折叠掉；训练控制面应把这些轴和 optimizer/schedule revision 一起冻结后再外推。额外 sweep 提高成本，超出已测尺度时回退邻近规模校准而非沿幂律盲推。 共同代价与回退边界是：只覆盖 GPT-2-style 22M-707M、FineWeb 5B-100B tokens、WSD 与 AdamW/AdamH；论文明确显示 log-linear LR 仅局部成立，不能外推到其他架构、optimizer 或更大规模。超界时重新 sweep 邻近尺度。

<!-- june29-owner:TRAIN-PRETRAINING:end -->

### Daily Books delta trace（2026-06—08）

<!-- daily-books-trace:SF-SPARSE-REPEATED-TRAINING:start -->
- `SF-SPARSE-REPEATED-TRAINING` — Daily `2026-06-01`；primary `arXiv:2606.01155v1`；Books review `books-review:SF-SPARSE-REPEATED-TRAINING`。

  **已吸收的语义增量：** The sparse data-constrained scaling law jointly models unique-token volume, repetition, effective parameters, and sparsity, so repeated-epoch pretraining must choose model size and sparsity against a data-saturation boundary instead of applying dense Chinchilla allocation or sparsity gains independently. 证据边界：The fitted law is empirical over the disclosed scale, corpus diversity, sparsity process, and compute regime; it does not prove the same optimum for frontier-scale mixtures, changing token quality, optimizer changes, or real hardware efficiency, which the paper explicitly separates from theoretical FLOPs.
<!-- daily-books-trace:SF-SPARSE-REPEATED-TRAINING:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-06888:start -->
- `SF-2026-ARXIV-2606-06888` — Daily `2026-06-06`；primary `arXiv:2606.06888v1`；Books review `books-review:SF-2026-ARXIV-2606-06888`。

  **已吸收的语义增量：** Exact-v1 adds a source-specific mechanism and evaluation boundary not fully represented by the current owner proposition. The delta remains bounded by exact-v1 and does not transfer commit authority to an adjacent owner.
<!-- daily-books-trace:SF-2026-ARXIV-2606-06888:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-11387:start -->
- `SF-2026-ARXIV-2606-11387` — Daily `2026-06-10`；primary `arXiv:2606.11387v1`；Books review `books-review:SF-2026-ARXIV-2606-11387`。

  **已吸收的语义增量：** 在 Pretraining 章节补一段 staged promotion：小实验是扩容决策 receipt，不是大规模结果的缩小版证明；保留 scale inversion 与 distributed-effects failure。
<!-- daily-books-trace:SF-2026-ARXIV-2606-11387:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-16768:start -->
- `SF-2026-ARXIV-2606-16768` — Daily `2026-06-16`；primary `arXiv:2606.16768v1`；Books review `books-review:SF-2026-ARXIV-2606-16768`。

  **已吸收的语义增量：** 深 Transformer 稳定训练可把 architecture warm-up 与 optimizer warm-up 分离，使曲率/残差路径逐步启用而非只缩小 learning rate
<!-- daily-books-trace:SF-2026-ARXIV-2606-16768:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-21514:start -->
- `SF-2026-ARXIV-2606-21514` — Daily `2026-06-20`；primary `arXiv:2606.21514v1`；Books review `books-review:SF-2026-ARXIV-2606-21514`。

  **已吸收的语义增量：** 深网训练的 river-valley dynamics 要把表示阶段与低曲率收敛阶段区分；统一 learning-rate heuristic 会掩盖 late-stage failure
<!-- daily-books-trace:SF-2026-ARXIV-2606-21514:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-12463:start -->
- `SF-2026-ARXIV-2607-12463` — Daily `2026-07-15`；primary `arXiv:2607.12463v1`；Books review `books-review:SF-2026-ARXIV-2607-12463`。

  **已吸收的语义增量：** 新增证据边界：Program-dependency analysis selects function targets under complexity/inferability criteria; the model reconstructs the missing function with generated rationale before existing agentic post-training. 该 delta 已进入 `books/part-04-training-system/28-pretraining.md#L1`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-12463:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-19058:start -->
- `SF-2026-ARXIV-2607-19058` — Daily `2026-07-22`；primary `arXiv:2607.19058v1`；Books review `books-review:SF-2026-ARXIV-2607-19058`。

  **已吸收的语义增量：** 新增证据边界：SkewAdam keeps momentum plus factored variance for the dense backbone, factored variance without momentum for experts, and exact variance for the router. Parameter role becomes the state-allocation key; this is orthogonal to ZeRO sharding and state quantization. 该 delta 已进入 `books/part-04-training-system/28-pretraining.md#L1`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-19058:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-20757:start -->
- `SF-2026-ARXIV-2607-20757` — Daily `2026-07-23`；primary `arXiv:2607.20757v1`；Books review `books-review:SF-2026-ARXIV-2607-20757`。

  **已吸收的语义增量：** 新增证据边界：Direct Evolution: post-training/random rotation -> symmetry-preserving learned basis during training -> quantized artifact with explicit runtime transform cost 该 delta 已进入 `books/part-04-training-system/28-pretraining.md#L486`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-20757:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-25063:start -->
- `SF-2026-ARXIV-2607-25063` — Daily `2026-07-28`；primary `arXiv:2607.25063v1`；Books review `books-review:SF-2026-ARXIV-2607-25063`。

  **已吸收的语义增量：** 新增证据边界：Direct Evolution: checkpoint identity by weights/loss -> stage endpoint evaluation -> ordered data-window lineage -> matched downstream update and erosion response as part of artifact suitability. 该 delta 已进入 `books/part-04-training-system/28-pretraining.md#L527`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-25063:end -->

<!-- daily-books-trace:SF-2026-SPECTRAL-ALLOCATION:start -->
- `SF-2026-SPECTRAL-ALLOCATION` — Daily `2026-08-27`；primary `arXiv:2608.25990v1`；Books review `books-review:SF-2026-SPECTRAL-ALLOCATION`。

  **已吸收的语义增量：** 当前书稿 diff 已把以下长期机制写入该 owner：在 held-out data 上按 momentum singular directions 探测 loss-optimal step，区分 volatile head 与 tolerant bulk；SAMuon/SAMuon-lite 对 bulk 放大；并保留边界：仅小到中型模型；静态 spectral prior 在 frontier scale、不同 architecture 与长期稳定性上未证明。 相邻章节对读：books/part-04-training-system/27-data.md#L103;books/part-04-training-system/29-sft.md#L55。Data 拥有 sampling weights，SFT 拥有 conditional demonstration objective；optimizer 的 spectral update geometry 属于 Pretraining。
<!-- daily-books-trace:SF-2026-SPECTRAL-ALLOCATION:end -->

<!-- daily-books-trace:SF-2026-SKILL-PRETRAINING:start -->
- `SF-2026-SKILL-PRETRAINING` — Daily `2026-08-28`；primary `arXiv:2608.26563v1`；Books review `books-review:SF-2026-SKILL-PRETRAINING`。

  **已吸收的语义增量：** 补足 skill artifact 作为结构化 capability data 的边界。
<!-- daily-books-trace:SF-2026-SKILL-PRETRAINING:end -->
