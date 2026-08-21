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

## 小结

Pretraining 用大规模 next-token prediction 把数据分布转化为参数更新。Cross-entropy 定义局部误差，optimizer 与 schedule 决定更新轨迹，batch、precision、activation memory 和分布式执行决定这条轨迹能否在可接受成本内完成。

预训练 checkpoint 是通用能力底座，不是最终产品行为。它学到什么由数据、objective、容量和优化共同决定；它是否可靠还需要独立 Evaluation 与后续训练约束。

## Review notes

本章只负责 next-token objective、训练 step、token/batch 计量、optimizer state 与训练稳定性。数据治理留在第 27 章；SFT 和 preference optimization 留在第 29、31～34 章；collective、state sharding 和 framework runtime 留在第 36～41 章。

2026-W10 的 SageBwd 案例用于补全 backward sensitivity、precision boundary 与 convergence contract。
其公开实验仍限于作者的小模型与固定训练设置，相关 repository 也未定位到可核验的独立实现；因此
正文不保留吞吐数字，也不把该 precision partition 写成通用 recipe。

Progressive Residual Warmup 用于补足 residual branch activation 的 `layer × time` 状态与恢复边界；其固定 schedule、训练规模和稳定性结果只作为 Experimental evidence。

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
- FLOP-Efficient Training / TTC-aware Early Stopping（Status: Experimental）:
  https://arxiv.org/abs/2601.01332
- ECO Quantized Training（optimizer-state error feedback；Status: Experimental）:
  https://arxiv.org/abs/2601.22101
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
