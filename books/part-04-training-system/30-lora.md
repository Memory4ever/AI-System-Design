# 第30章 LoRA

**Knowledge Tree:** Part IV Training System：模型能力如何产生
**Stable Knowledge Node ID:** `TRAIN-LORA`
**Legacy Chapter:** Ch26
**Status:** Draft

**Roadmap Intent:** 为什么低秩适配可以高效改变模型行为，而不必全量更新参数。

## 本章要回答的问题

第 29 章已经定义 SFT objective，一个预训练模型适配新任务时是否必须更新全部参数？LoRA 为什么把权重更新限制在低秩子空间，能够减少可训练参数、gradient、optimizer state 和模型变体存储？这种节省为什么不会让基座模型的前向与 activation 成本消失？

本章的核心判断是：**LoRA 冻结基座权重，只学习一个低秩增量；它改变的是参数更新的表示方式，而不是 SFT、preference optimization 或模型 forward 的基本目标。**低成本来自更小的 trainable state 与 adapter artifact，而不是模型容量被免费删除。

本章使用 `W_0` 表示冻结的基座权重，`Delta W` 表示任务更新，`d_in`、`d_out` 表示线性层输入输出维度，`r` 表示 LoRA rank，`alpha` 表示缩放系数。

## 从 Full fine-tuning 的重复状态开始

设一个线性层为：

```text
y = W_0 x
W_0 in R^(d_out x d_in)
```

Full fine-tuning 学习同样 shape 的更新：

```text
y = (W_0 + Delta W) x
Delta W in R^(d_out x d_in)
```

当模型有数十亿参数时，每个任务都可能需要：

- 全量 trainable gradients。
- Adam 一阶、二阶 optimizer states。
- 完整更新后的模型权重。
- 分布式训练中的对应通信与 checkpoint。

但下游适配通常不是从零学习整个世界。LoRA 提出一个可训练假设：有用的任务更新可以落在较低 intrinsic rank 的子空间中。

## 低秩增量怎样进入线性层

LoRA 参数化：

```text
Delta W = (alpha / r) B A

A in R^(r x d_in)
B in R^(d_out x r)
r << min(d_in, d_out)
```

前向计算变成：

```text
y = W_0 x + (alpha / r) B A x
```

`W_0` 保持冻结，只训练 `A` 和 `B`。Trainable parameter count 从：

```text
d_out * d_in
```

变成：

```text
r * (d_in + d_out)
```

LoRA 借用低秩分解思想，但通常不是先训练完整 `Delta W`，再对它做 SVD 截断。`A`、`B` 从训练开始就作为参数被直接优化。

## 一个参数量小例子

假设线性层：

```text
d_in = d_out = 4096
r = 8
```

Full update 参数量：

```text
4096 * 4096 = 16,777,216
```

LoRA 参数量：

```text
8 * (4096 + 4096) = 65,536
```

该层 trainable parameters 约为 full update 的 `0.39%`。这个比例只描述该目标矩阵；整模型比例还取决于哪些 modules 插入 LoRA、是否训练 bias、embedding 或其他参数。

常见初始化让一个 factor 随机、另一个为零，使训练开始时：

```text
Delta W = 0
y = W_0 x
```

模型先精确继承基座行为，再逐步学习 adapter update。具体初始化和 scaling 必须以实现与 checkpoint metadata 为准。

## 为什么会节省训练显存

冻结的 base parameters 不需要保存 trainable gradients 和对应 optimizer states。主要节省来自：

- Trainable parameter 数量下降。
- 对应 gradients 和 optimizer states 下降。
- 每个任务只保存 adapter，而不是完整模型副本。

但 `W_0` 仍参与 forward。为了把梯度传给更早的 trainable adapters，backward 仍可能经过基座算子并计算 activation gradients。Activation、temporary buffers 和大部分基座矩阵执行不会按 trainable parameter 比例同时下降。

因此：

```text
trainable parameters = 0.39% of a target matrix
!= training FLOPs = 0.39%
!= GPU memory = 0.39%
```

精确收益必须拆分 weights、gradients、optimizer states、activations 和 workspace。

## LoRA 没有改变 SFT objective

第 29 章的 masked token loss 保持不变：

```text
L_SFT(theta_adapter)
= - sum_t m_t log p_(theta_base, theta_adapter)(y_t | prefix_t)
```

变化的是可更新参数集合：

```text
grad(theta_base)    disabled
grad(A), grad(B)    enabled
```

同样，LoRA 也可以承载 DPO 或其他 objective。把 “LoRA model” 当作一种独立训练目标，会混淆 supervision、optimization algorithm 与 parameterization。

## Rank 与 target modules 决定更新空间

更高 rank 提供更大的更新子空间，也增加 trainable state、compute 和 overfitting 风险。更低 rank 更便宜，却可能限制复杂适配。

还必须选择 target modules，例如：

- Attention 的 Q/K/V/O projections。
- MLP 的 up/gate/down projections。
- 其他模型特有 linear layers。

只适配 Q/V 与覆盖全部 Attention/MLP 会得到不同容量和 artifact shape。最优 rank 与位置依赖任务、数据、基座和预算，不能从 LoRA 名称推出。

Rank 也不等于任务“本质维度”的直接测量。训练成功只说明该配置足以形成某个有用 update，不证明所有任务更新都严格低秩。

Update subspace 也可以从训练前静态选择，演进为由当前 activation 动态选择。以 attention Q/K feature magnitude
生成 transient row mask，可以让 optimizer 只更新当步被选中的 rows，而不改变 inference graph：

```text
current batch activations
→ per-head feature statistic
→ transient row selection
→ masked gradient update
→ discard mask after the step
```

这不是 LoRA：base parameters 仍可能被直接更新，也不意味着整模型 backward、activation 或 optimizer state
按 mask 比例下降。Runtime 必须决定未激活 rows 的 momentum/variance 如何演进、恢复训练是否重建相同 mask，
并监控 mask churn 与 saliency drift。LongAct 的作者实验只支持其 Qwen3-4B/8B、长上下文 RL 和 8×H800
合同下的 empirical utility；magnitude 并非稳定因果 attribution。Full update 在容量和简单性优先时仍成立，
固定 LoRA/row mask 在 artifact 小、可复现和可部署变体优先时更合适。

### High-rank Adapter 的瓶颈可能来自 Intermediate，而不是参数本身

低 rank 时，直接物化 `B @ A` 简单且兼容成熟 autograd；rank 提高、target modules 增多并叠加 gradient
checkpoint recompute 后，反复产生 dense temporary 可能先成为 memory traffic 与峰值显存瓶颈。此时优化
不是改变 LoRA/DoRA 的学习目标，而是利用数学等价式把 weight norm 展开为 base、cross 与 Gram terms，
只保留随 `d_out * r + r^2` 增长的 intermediate，再融合 compose、norm assembly 与 backward。

Runtime 需要按 training mode、shape crossover、precision、backend capability 与 compatibility guard 选择
fused backward、fused forward 或 eager fallback。这个 dispatch 是 checkpoint/runtime contract 的一部分，
不能隐藏成“同一个 kernel 在所有形状都更快”。Fused path 会带来数值非 bitwise identical、backend
portability、FSDP/DTensor full-weight assumption 与 embedding compatibility 等新边界；小 tensor 或非 CUDA
环境仍应保留 eager 实现。高 rank 的可执行性改善，也不证明高 rank 对所有任务更优。

### Parametric Recall 可能由少量顽固 Token 决定

LoRA 的 rank、target modules 和总 loss 只能描述更新空间，不能说明一条 sequence 为什么仍无法被精确复现。
在 exact-token recall 任务中，平均 token probability 可能持续改善，而整条序列成功率在少量 stubborn tokens
越过决策边界后才突然变化。由此可把 uniform token update 精化为：

```text
measure token-level recall margin
→ freeze or down-weight already-stable tokens
→ preserve gradient on stubborn tokens
→ re-evaluate sequence-level exactness and forgetting
```

它解决的是 easy tokens 反复占用梯度、甚至被过度强化的问题，却新增 threshold、mask churn 与局部记忆过拟合。
普通 instruction tuning、语义等价输出或开放式生成不应追求 exact-token recall；uniform objective 在没有可靠
token attribution 时仍更稳。How LoRA Remembers? 的作者实验只覆盖单一 8B 模型与 greedy decoding，所观察到的
约 `0.5` probability boundary 不能外推为跨 scale、sampling 和任务的普适定律，parametric recall 也不等于
reasoning 或 generalization。

## QLoRA 进一步减少冻结权重存储

LoRA 仍需加载 base weights。QLoRA 将冻结基座以 4-bit quantized representation 存储，并让梯度通过反量化计算路径流向 LoRA adapters。

两者解决连续但不同的问题：

```text
LoRA   reduce trainable model states
QLoRA  additionally reduce frozen base storage
```

QLoRA 论文还讨论 NF4、double quantization 和 paged optimizers 等设计。它们分别处理 quantization representation、量化常数开销与显存峰值，不应全部简化成“4-bit training”。

Quantized base 不代表所有计算都以 4-bit 执行，也不代表 adapter、optimizer 或 activation 使用相同精度。Compute dtype 与量化误差需要单独记录和评估。

## Merge 与动态 Adapter 是两种资产策略

### Recurrent Launch State：权重与 Prompt 之外的第三个适配面

LoRA 改变 weight delta，prefix/prompt 改变显式输入；带 recurrent state 的模型还可能允许冻结权重，仅学习每层
初始 state `S0`，在每次 request/sequence 启动时注入。它避免逐 token adapter matmul，却把适配资产变成与
recurrent layout 强绑定的 launch state：

```text
base model revision + recurrent-state schema
→ task-specific S0 + scaling/config
→ initialize recurrent layers
→ ordinary token recurrence
```

Trainer 拥有 S0 tensor、base identity、layer mapping 与训练数据；serving runtime 拥有加载、tenant routing、
batch compatibility、reset 和 eviction。Model revision 或 state layout 变化会让旧 S0 静默失效；跨 tenant 混用
则是状态污染。LoRA 在通用 Transformer、需要更大 function update 或需 merge 成独立 checkpoint 时仍然合理；
prompt/prefix 在可解释、无需训练和快速切换时仍成立。

S0 Tuning 为这一 adaptation surface 提供 Experimental 证据，但 paper/model-card 的层数、hardware 与 base identity
存在冲突，因此只沉淀接口和 lifecycle，不保留性能外推。

训练后可以把 adapter merge 进基座：

```text
W_merged = W_0 + (alpha / r) B A
```

Merge 的优势是 runtime 执行路径接近普通权重；代价是每个变体重新形成完整 weight artifact，且必须保留 base/adapter lineage 才能追踪来源。

另一种方式是在 runtime 动态加载 adapter：

```text
shared base model
+ selected adapter per request
```

它提高基座复用，却引入：

- Adapter cache、加载与 eviction。
- Batch 内 adapter compatibility。
- Base/adapter version matching。
- Tenant isolation 与访问控制。
- 不同 rank/target module 的 kernel layout。

所以 LoRA 从训练技巧自然延伸为 Model Registry 和 Serving 的模型组合协议。

### Repository-conditioned Adapter 是派生索引，不是代码真值

稳定 repository 可以直接检索相关文件或为每个 repo 训练 adapter；前者保留可引用证据但增加每请求 Context，
后者降低在线 token 却会随 commit 变旧。当 repository 数量和 revision stream 同时增长，还可以从 snapshot/diff
生成 adapter：

```text
immutable repository snapshot + ordered diffs
→ versioned repository representation / recurrent update state
→ generated adapter bound to base revision
→ task evaluation and promotion
→ invalidate or regenerate after source revision
```

Repository 与 diff 始终拥有事实 authority；representation、recurrent state 和 adapter 都是可重建的派生状态。
它把 per-repo training 移到 hypernetwork/adapter compiler，却新增 source deletion、diff reorder、压缩遗失、
generator/base compatibility 和大规模 artifact refresh。RAG 在 source 频繁变化、需要引用或高风险审计时仍更合理；
固定人工训练 adapter 在少量稳定 repositories 上更易验证。Code2LoRA 的作者实验只覆盖其 1.5B Python
assertion-completion 合同，不能证明生成 adapter 能替代 source review 或跨语言迁移。

### 从 Specification 编译 Neural Program：把每次推理前移为版本化资产

Repository-conditioned adapter 仍以变化中的 source snapshot 为事实 authority；另一条分支面对的是相对稳定、
但很难用精确代码写出的自然语言 specification。每次请求都把 specification 和 input 交给大模型，能保留通用
解释能力，却把相同规则的解析成本、provider drift、privacy 与在线延迟重复支付。若规则的变化频率远低于调用
频率，可以把解析从 request path 前移到受治理的 compilation path：

```text
versioned natural-language specification
→ compiler produces pseudo-program / adapter or prefix artifact
→ behavioral evaluation under a pinned interpreter and base revision
→ sign, publish, cache and serve
→ revoke, recompile or roll back after specification / base change
```

这不是把 neural artifact 宣称为 deterministic code。它可能在模糊输入上比 regex 更有容错性，也可能静默偏离
原 specification；离线编译降低 per-call 成本，却新增 compiler drift、behavioral inspection、supply-chain identity
和不可解释 failure。可部署身份至少要绑定 specification、compiler、pseudo-program、base/interpreter、adapter、
quantization 和 runtime revision，并保存代表性输入、边界条件与拒绝行为形成的 behavioral signature。高风险规则、
频繁变化的 policy 或必须逐条解释的约束仍应保留显式程序与在线 evidence gate；远端模型调用在任务长尾且无法
预先冻结规则时也仍然合理。Program-as-Weights 的作者实验只证明其 FuzzyBench、指定 interpreter 与生成 artifact
合同中的可行性，不证明 neural program 具有代码等价性或跨任务普遍优于显式实现。

### Route 晚于 Prefill 时，兼容性必须由训练定义

按请求选择 reasoning adapter 可以避免简单请求承担完整推理成本。若 switcher 只有读完 prompt 才能判断，
最直接的方法是 route 后重跑 prefill；它语义清楚，却抵消端侧或长 prompt 的收益。复用 base-only prefill
并在 decode 才启用 adapter，则产生新的 checkpoint contract：adapter 必须在训练时就学会消费没有经过
adapter 的 prompt KV，例如显式对 prompt positions 关闭 adapter、只在 response positions 开启。

```text
base-only prefill
→ route decision
→ adapter-on decode consumes base KV
```

这不是任意 LoRA 都具备的运行时技巧。需要 prompt-side specialization 的 adapter 与这份 KV 不兼容；
false-negative routing 会丢失质量，false-positive 会增加 token、KV 和功耗。Checkpoint 因而要绑定 base、
adapter、switcher、mask policy、quantization 与 KV compatibility；runtime 还要记录 route decision 和回退。
always-on adapter 或 route 后重算在分布漂移、高风险决策或 cache 复用很小时仍更可靠。

## 多个 Adapter 能否直接相加

两个 adapters 的增量可以在权重空间相加或按系数组合，但数学上可相加不代表行为无冲突：

```text
W = W_0 + lambda_1 Delta W_1 + lambda_2 Delta W_2
```

不同 adapters 可能修改同一表示方向，组合后分布也可能超出各自训练范围。Adapter composition、merge 和 routing 都需要重新 Evaluation，不能把独立任务得分当作组合行为证明。

## Checkpoint 与可复现性

Adapter artifact 至少需要绑定：

- Base model identity 和 exact revision。
- Target module names 与 tensor shapes。
- Rank `r`、`alpha`、dropout 和 initialization。
- Tokenizer、chat template 与 training objective。
- Adapter weights 和可选 optimizer state。
- Merge state、quantization config 与 compute dtype。

只保存 `A`、`B` tensor 而不保存 base identity，可能得到 shape 可加载但语义错误的模型组合。

随着 adapter 从单一 low-rank delta 演进到 block-granular、跨层共享、data-routed 或 orthogonal update space，
artifact contract 还要保存 method/schema revision、router/projection state、weight-tying、TP layout、conversion
history 与 backend compatibility。一个库“支持某方法”只证明 implementation 已进入对应 release，不证明各方法
在同一 model/data/hardware/precision/SLO 下可互换。PEFT 0.19.0 的 release family 说明生态正在扩大这种选择面，
同时也暴露 lossy conversion、schema proliferation 与 patch-level identity；成熟 LoRA 在 portability、审计和
mixed deployment 上仍是合理默认。

## 与 Distillation 的边界

Distillation 让 student model 学习 teacher 的输出或中间行为，通常改变模型本体或架构。LoRA 则在同一基座上参数化增量。

二者可以组合：例如先用 teacher 生成 demonstrations，再通过 LoRA 训练 student/base adapter。但它们解决的问题不同：

```text
LoRA          cheaper parameter update and model variants
Distillation  capability transfer into a student
```

## 本章在知识树中的位置

```text
pretrained base
-> SFT or preference objective
-> low-rank parameter update
-> LoRA / QLoRA adapter checkpoint
-> merge or dynamic adapter serving
-> Model Registry / runtime policy
```

本章承接第 29 章的 objective，改变训练状态与模型资产成本。第 35 章继续处理 adapter checkpoint 的恢复和 lineage；Part V 处理动态 adapter 的执行，Part VI 处理其资产治理。

## 自检问题

1. LoRA 为什么不等于对原权重直接做 SVD？
2. `A`、`B` 的 shape 怎样保证 `BA` 与 `W_0` 对齐？
3. 参数量小例子为什么不能直接推出整模型显存比例？
4. 冻结 base weights 后，哪些计算和 activation 仍然存在？
5. LoRA 与 SFT objective 分别位于哪个层次？
6. Rank 与 target modules 分别控制什么？
7. QLoRA 比 LoRA 额外减少了哪类状态？
8. Merge 与动态 adapter Serving 各有什么系统代价？
9. 多个 adapters 数学可组合为什么不保证行为兼容？
10. Adapter checkpoint 为什么必须绑定 exact base revision？

## 小结

LoRA 用 `BA` 低秩因子表示任务更新，显著减少 trainable parameters、gradients、optimizer states 和每任务 artifact。它保留基座模型的大部分计算，并以受限更新空间换取成本与资产复用。

QLoRA 继续压缩冻结基座存储，merge 与动态加载则把训练选择传播到 Serving。LoRA 的完整系统价值不只在“参数少”，而在 base、adapter、objective、checkpoint 和 runtime 之间形成可管理契约。

## Review notes

- Code2LoRA（repository-conditioned generated adapter；Status: Experimental）:
  https://arxiv.org/abs/2606.06492

- Program-as-Weights（specification-to-neural-program compilation；Status: Experimental）:
  https://arxiv.org/abs/2607.02512

- How LoRA Remembers?（stubborn-token exact recall；Status: Experimental）:
  https://arxiv.org/abs/2605.30260

- S0 Tuning（recurrent launch-state adaptation；Status: Experimental / Artifact Identity Inconsistent）:
  https://arxiv.org/abs/2604.01168

本轮 Review 保留低秩增量、QLoRA 和动态 Serving 主线，补齐参数 shape、数值例子、initial state、SFT objective 接口、activation 边界、adapter composition 与 checkpoint metadata。Preference optimization 仍属于第 31～34 章。

Primary-source 校验入口：

- Edward J. Hu et al., "LoRA: Low-Rank Adaptation of Large Language Models", 2021: https://arxiv.org/abs/2106.09685
- Tim Dettmers et al., "QLoRA: Efficient Finetuning of Quantized LLMs", 2023: https://arxiv.org/abs/2305.14314
- Efficient Reasoning on the Edge（post-prefill routing 与 training-defined KV compatibility；
  Status: Experimental）: https://arxiv.org/abs/2603.16867
- Scaling DoRA（Status: Experimental；factored norm、fused kernel 与 compatibility dispatch）:
  https://arxiv.org/abs/2603.22276
