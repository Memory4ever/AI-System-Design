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

但 nominal rank 只是参数化上限，optimizer 如何同时更新两个低秩因子会决定实际可用的 effective rank。若 A/B 的几何与初始化让更新方向长期退化，提高 rank 也不一定扩大有效子空间；反过来，耦合的谱更新可更接近目标 weight-space direction，却增加优化器假设、阻尼和稳定性成本。Adapter capacity 因而应同时记录 rank、初始化、optimizer transform 与实际更新谱，而不是只用 `r` 解释结果。

<!-- source-family:SF-2026-ARXIV-2609-12123 -->

还必须选择 target modules，例如：

- Attention 的 Q/K/V/O projections。
- MLP 的 up/gate/down projections。
- 其他模型特有 linear layers。

只适配 Q/V 与覆盖全部 Attention/MLP 会得到不同容量和 artifact shape。最优 rank 与位置依赖任务、数据、基座和预算，不能从 LoRA 名称推出。

Rank 也不等于任务“本质维度”的直接测量。训练成功只说明该配置足以形成某个有用 update，不证明所有任务更新都严格低秩。

静态 rank 在任务同质、kernel 依赖固定 shape 时最容易复现；输入难度差异很大时，它要么为简单样本持续支付最大容量，要么让复杂样本受限。条件容量分支可以让 router 从版本化 input feature 提出允许 rank，并在所有目标层一致截取 adapter 的前 `r` 个方向；但训练和推理必须复用同一 router、difficulty-label rule、rank set、alpha 与 target modules，不能训练时动态、部署时再凭经验固定。

rank policy 因而成为 adapter artifact identity 的一部分，也新增 router 误判、标签循环、dynamic-shape batching 碎片和更大发布矩阵。任务分布漂移、router 不稳定、延迟收益未证或静态 kernel 更重要时，固定 rank 仍是首选回退。`arXiv:2605.01959v1` 只在作者 Llama 3.2/Whisper 与 QA、数学、语音任务中验证质量和参数量；它没有披露生产 batch、硬件、端到端 latency 或 SLO，trainable parameters 减少不等于 serving cost 已下降。

<!-- source-family:SF-2026-ARXIV-2605-01959 -->

### Rank Threshold 必须绑定 Loss 与可证明假设

把某个实验中的最小可用 rank 写成通用 recipe，隐含假设不同 objective 共享同一优化几何。平方损失下可以在明确的
随机特征、NTK 与谱条件中给出充分 rank 阈值；换成 cross-entropy 后，同样的有限阈值一般不自动成立，只有再加入
PL 等条件才能恢复受限结论。经验最优 rank 还受样本量、类别数、层位置和 bias–variance 影响。

所以 rank 选择应沿 `loss + base revision + target modules + feature assumptions + evaluation slices` 出账，而不是
只记一个整数。理论阈值可缩小搜索范围，却不能取代行为验收；假设无法验证或 loss 改变时，应回到 rank sweep、
higher-rank LoRA 或 full fine-tuning。现有证据限于 Gaussian-iid/NTK 条件及少量 BERT/RoBERTa 分类实验，不支持
“任意任务 rank one 足够”之类的普遍结论。

<!-- source-family:SF-2026-ARXIV-2605-03724 -->

### 多 Expert LoRA 的 Zero-init 可能冻结 Router 分化

普通 LoRA 让一个因子以零初始化，能在开始时保持基座 forward 不变；当同一 adapter 再复制成多个 experts 时，
所有分支同时为零会产生置换对称：router 看到相同输出和梯度，无法形成 expert identity。此时“增加 experts”只增加
名义容量，没有增加可训练的条件分支。

一个充分而非唯一的 symmetry-breaking 构造，是把不同 expert 的更新限制在互不重叠的基座奇异子空间，使初始
forward 仍近似不变，但 router gradient 已可区分。收益是解除 cold-start deadlock，代价是预计算分解、expert
subspace identity 与可能错过最优更新方向；平衡损失和 routing warmup 也仍需单独验收。单 adapter、不需要条件路由
或子空间约束损害质量时，普通初始化、随机扰动或更简单的 LoRA 仍更合适。

<!-- source-family:SF-2026-ARXIV-2605-03252 -->

### 静态子空间分离之后，还要处理训练中的梯度重新耦合

用互不重叠的奇异子空间初始化多个 LoRA experts，只能解决 cold start 时的置换对称。多任务训练继续推进后，
不同 rank-1 component 的梯度方向仍可能重新靠拢，使静态 expert identity 逐渐失去意义。一个条件演进分支按当前
梯度方向动态重组 components：expert 间尽量保持近似正交，expert 内则聚合相近方向，并把 grouping revision、
所用梯度窗口和 clustering 配置纳入 adapter artifact，而不是把分组当作不可见的训练临时量。

它把一次性 initialization heuristic 演进为训练期 controller，却增加额外梯度统计、CPU clustering 或整数优化、
约 22% 的作者设置训练开销，以及 group identity 抖动和 checkpoint 恢复复杂度。梯度夹角也只是 interference 的
代理，不是能力因果定义；现有结果限于作者的 SuperNI、六个 LLM 与 LoRA-expert 配置。任务同质、静态子空间已经
稳定或 regrouping 成本超过收益时，普通 LoRA、固定 experts 或 full fine-tuning 仍是更可预测的回退。

<!-- source-family:SF-2026-ARXIV-2605-05676 -->

### 固定 Rank 下，压缩距离还要回到行为影响

只最小化 adapter 的 weight-space reconstruction error，在轨迹同质、参考行为不足或部署只关心参数近似时最直接；Agent 数据同时来自不同任务和决策路径后，两个参数距离接近的更新可能对动作分布产生完全不同的影响。此时“可合并或可压缩”不能只由矩阵距离决定：应在版本化 reference histories 上比较候选更新引起的 decision-distribution change，把行为效果近似相同的方向视为冗余，再将平衡后的更新投影回固定 rank 的 tangent space，同时约束 effective-weight error 与 decision distortion。

Reference-history builder 与 evaluator 拥有被观察的行为几何，compressor 只能提出低秩投影；held-out acquisition、transfer、原能力与安全回归通过后，release gate 才能提交新 adapter。其 identity 至少绑定 base checkpoint、原 adapter/update、reference histories、behavior metric/evaluator、projection revision 与 rank；否则同一个 `r` 不能表示同一种行为容量。

这种行为感知压缩用 reference selection、Jacobian/局部几何估计和校准成本换取固定 rank 下更少的行为冲突，但局部线性近似与 reference coverage 都可能失效，稀有关键行为还可能被误判为冗余。历史不足、任务稳定或 weight approximation 已足够时，应回退标准 LoRA 投影、提高 rank 或 full fine-tuning。exact-v1 结果只覆盖作者使用的两个模型规模与两个 Agent benchmark，不证明该几何可跨任务迁移，也没有排除安全和基础能力退化。

<!-- source-family:SF-2026-ARXIV-2609-12896 -->

<!-- semantic-body-binding:SF-2026-ARXIV-2605-07850:start -->
为每个预算单独训练 LoRA 最清楚，却会产生多个不可共享的 adapter revision。若部署需要动态 rank，可让同一 adapter 的 ordered factors 形成 nested sub-ranks，并把训练目标和 artifact identity 绑定到可用 rank set；验收同时报告关键 rank 的单点质量与 rank–accuracy curve/AURAC，不能让平均曲线掩盖低 rank collapse。该路径减少多 checkpoint 成本，却依赖方向 ordering、任务分布和 kernel 支持；固定预算或某一关键 rank 不合格时，回退普通固定-rank LoRA。 [受限证据：arXiv:2605.07850v1]
<!-- semantic-body-binding:SF-2026-ARXIV-2605-07850:end -->

### Adapter Placement 也在控制知识获得与泛化边界

固定在所有 target modules 使用同一 LoRA 配置，最容易复现，却假设不同层对 acquisition、transfer 和 boundedness
承担相同责任。按 early / middle / late / full-stack 进行受控干预，可以把 placement 作为实验变量，判断某类更新
更依赖表征入口、组合层还是输出附近；但这些层位偏好是 checkpoint 与 objective 的经验属性，不是跨架构固定语义。

局部放置减少 trainable state 并可能限制副作用，却也可能漏掉跨层协同、在 distribution shift 后失效，或把局部
相关性误当成因果 owner。上线前应在 acquisition、held-out transfer、原能力回归和安全边界上联合重验；收益不稳时
回退 full-stack LoRA、重新选层或 full fine-tuning。Placement 必须进入 adapter identity，不能只记录 rank 和 alpha。

<!-- source-family:SF-2026-ARXIV-2607-25663; daily-trace:papers/2026/07/29/README.md -->

### 初始梯度只能提出 Adapter Placement

全层部署 LoRA 是信息不足时的稳健基线，但它也把训练与部署成本平均花在贡献不同的模块上。一个更便宜的 proposal sensor 是用少量样本估计候选 adapter 的初始 projected-gradient energy，据此提出 placement；受限实验观察到能量会集中在与架构有关、对任务相对稳定的浅层 FFN down-projection。<!-- semantic-body-binding:SF-2026-ARXIV-2605-06183 -->

初始局部梯度不是最终能力的因果证明，也不能看到跨层协同。现有证据只覆盖两个 8B 模型家族和四类任务，不包含 MoE、VLM 或长期训练漂移。因此 placement proposal 必须经过 held-out regression 和部署成本 Gate；probe 不稳定或回归失败时，回退 full-stack LoRA、重新选层或 full fine-tuning。

### Adapter 内的条件容量不能使用全局统一裁剪规则

当 LoRA adapter 自身引入多个 experts 时，固定保留全部 experts 最容易复现，也避免错误删除稀有能力；随着 module 数量增长，统一 mask 又会忽略不同层的 routing concentration 与 drift。受限的演进路径是先完成 exploratory training，再按 module 分别读取 Gini、routing entropy 与 drift asymmetry，提出各自的 expert pruning mask：

```text
exploratory adapter training
-> per-module routing and drift evidence
-> module-specific pruning proposal
-> quality / coverage replay
-> commit reversible mask or restore experts
```

这改变的是 adapter 内条件容量的部署状态，不是 base MoE routing，也不证明高 rank 或更多 experts 必然有用。探索阶段本身有成本，统计噪声或长尾样本不足会错误删除必要 expert。每个 module 因此要保留最小 expert floor、mask provenance 与 rollback artifact；drift 或 quality Gate 失败时恢复原 adapter experts。作者结果只覆盖其模型与任务，不能外推到任意 base MoE、adapter 或 Serving workload。

<!-- semantic-body-binding:SF-2026-ARXIV-2604-26340:start -->
Adapter expert pruning 的 authority 属于逐 module evidence 与可回滚 mask，而不是一个跨层全局阈值。
<!-- semantic-body-binding:SF-2026-ARXIV-2604-26340:end -->

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

### Private PEFT 的 Selector 应在最终私有更新前冻结

在每一步 private training 中重新按带噪梯度选择样本或模块，会让 selection 与隐私状态反复耦合；完全随机选择更容易核算，却可能把有限预算花在低价值样本上。一个条件分支先由 private data 通过差分隐私机制产生 synthetic artifact，这一步已经消耗 `(ε_syn, δ_syn)`；selector 只读取该 DP synthetic artifact，并在最终 private LoRA/PEFT update 前冻结。对已发布 DP artifact 的 selection 是 post-processing，本身不额外消耗隐私预算，但后续私有微调仍消耗 `(ε_ft, δ_ft)`，总账必须组合两阶段的 `ε/δ`，不能把 selection 的零增量误写成整个流程免费。

这条路径用 synthetic-to-private transfer 假设换更定向的预算分配。selector 可能编码合成数据偏差，在最坏噪声下失稳，或过滤掉稀有私有行为；两阶段 `ε/δ`、邻接定义、合成机制与 selector revision 任何一项缺失都使 privacy claim 不可复算。transfer 或 robustness Gate 失败时，应回退随机/公开 selector、更保守的 DP-SGD，或不进行私有适配。现有证据只支持作者设置，不能证明任何冻结 selector 都保持效用或隐私实现正确。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-17432:start -->
Private LoRA 的 selector 可以在最终 private update 前冻结；只读取已消耗 `(ε_syn, δ_syn)` 产生的 DP synthetic artifact 时，selection 属于 post-processing，但完整流程仍需组合 synthetic generation 与 fine-tuning 的 `ε/δ` 隐私预算。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-17432:end -->

### Bit Width 与 Adapter Rank 共享同一个容量预算

先固定统一 base precision、再单独选择 LoRA rank，搜索空间小且 artifact 容易比较；当内存预算严格时，某层降低 bit width 释放的空间可以用于提高另一层 adapter rank，而量化误差与低秩补偿又并非独立。更完整的配置应把 per-layer bit width、rank、target modules、compute dtype 和总 memory constraint 组成联合候选：search controller 只提出可行组合，训练 run 产生 adapter，artifact builder 记录 quantized base 与 adapter 的精确配对，独立 evaluation 决定是否发布。

联合搜索可以在固定预算内重新分配表示误差和更新容量，却引入多保真 proxy bias、搜索成本、不可比较的 layer configurations 及更大的发布矩阵；较高 rank 也未必能补偿错误量化造成的能力损失。预算宽裕、任务简单或搜索证据不足时，统一精度加固定 rank 仍更清晰；任何自动配置都必须保存 search space、repair rule、seed、训练步数与最终 artifact lineage，不能只发布一个“最优”平均分。

<!-- SF-2026-ARXIV-2602-22268 -->

## Merge 与动态 Adapter 是两种资产策略

量化存储中的原位学习会产生第三种资产边界：对外仍是整数 cell/served artifact，内部却通过累积 delta、scale 或校正状态改变实际函数。同一编码字节或同一基础 checkpoint 因此不再保证同行为；registry 必须绑定更新状态、写入规则、校准和回滚点。它减少独立 adapter 的数据移动，却增加硬件特化、可复现与耐久性风险；更新频繁或审计优先时，显式 LoRA/adapter 仍更清晰。<!-- semantic-body-binding:SF-2026-ARXIV-2608-20873 -->

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

量化基座还多一层问题：训练时使用的更新，导出后是否仍由同一组数值表示。先在高精度中相加再重新量化，可能改变甚至抹去小更新；一种受限分支是固定量化 codes，只学习 scale，并在训练 forward 就使用目标格式的 scale grid。只有导出沿用相同 grid、clamp 和 layout，才能保持训练与部署所表示的权重一致。这里保持的是表示身份，不是高精度 LoRA 的表达空间或质量：scale-only 更新受固定 codes 约束；需要更自由的权重更新时，显式 runtime adapter 或不同精度仍可更合适。

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

### 多租户 Fine-tuning：从共享权重转向复用 Backbone 执行

每个租户独立运行 LoRA job，隔离清楚、失败域小，且在租户数量少或数据到达稳定时仍最容易复算；但当大量小任务
同时微调同一 base model 时，系统会反复加载相同冻结权重、执行相似 backbone 路径，并让短 job 的空隙碎片化 GPU。
只共享模型副本可以减少 weight memory，却没有自动消除不同 step、shape 与 adapter state 带来的执行空洞。

更进一步的 multiplexing 同时利用空间与时间两个维度：空间上让兼容任务共享一次 backbone execution、只在
tenant-specific adapter/update path 分叉；时间上根据各任务 ready state 和资源空隙交错推进。Runtime 因而需要显式
拥有以下身份与状态：

```text
base revision + optimizer / precision contract
tenant adapter and optimizer state
batch / step compatibility
spatial sharing group + temporal schedule epoch
failure and cancellation boundary
```

这条路线获得更高 backbone 复用和更少显存重复，却把简单 job isolation 换成跨租户耦合：一个 straggler、OOM 或
numerical mismatch 可能拖累 sharing group，调度也不能静默改变每个任务的 effective batch、sample order 或 optimizer
step。数据、gradient 和 adapter state 必须保持租户隔离，不能因为共享 forward 就共享 authority。负载低、任务异构、
需要强故障隔离或 sharing overhead 超过重复计算时，独立 job 仍更合理。MuxTune 的结果只属于作者模型、GPU、任务组合
与实现，不构成多租户训练的通用吞吐结论。

<!-- source-family:SF-2026-ARXIV-2603-02885 -->

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

在 DP federated LoRA 中，A/B component 的激活选择不能固定为全层同一模式或预设交替表；它是逐层、逐轮演化的训练控制状态。Selector 只能消费已经纳入 DP accounting 的 curvature/statistics，server 保存 selection revision、privacy accountant 与 aggregation identity；选择漂移或预算不足时回退固定 component schedule、同构 adapter 或 dense-delta aggregation。

结果覆盖 GLUE、SQuAD、CIFAR-100、Tiny-ImageNet、严格 DP/non-IID 设置与作者比较组；不证明恶意客户端、任意 privacy definition 或所有 backbone 下无额外隐私成本。 PLATFORM-SECURITY 拥有 privacy threat/accounting；TRAIN-LORA 拥有 component-selection mechanism。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-05769 -->

## 多个 Adapter 能否直接相加

### 开放 Adapter 池需要 Composition Admission

预先批准的少量 adapter 可以由人工验证组合；开放仓库检索后，相关性不再等于可合并性。一个更强的控制面先检索候选，再以层级稀疏残差组合，并用多视图一致性检查决定 accept、reject 或 fallback。Registry 保存 backbone、layer coverage、训练来源与评测身份，composer 只提出组合，admission gate 才能发布合并 artifact。

这种路径增加检索误召回、视图相关错误和组合时延，且一致性不能证明安全或正确。租户固定、adapter 数量少或离线验证充分时，静态配置仍更稳健；证据不足时应回退单 adapter 或基座模型。现有 exact-v1 只支持作者的池、任务与审计器。<!-- semantic-body-binding:SF-2026-ARXIV-2605-01429 -->

### 跨 Backbone 合并前先检查谱兼容性

权重增量在同一 backbone 和坐标系中才有直接相加的语义；跨蒸馏版本或 video-diffusion 变体时，低秩方向可能代表不同功能。无目标数据的受限分支可以用更新的谱结构与刚性度聚类，先判断哪些 LoRA 可能共享子空间，再限制 routing 或 merge 范围。谱 gate 只拥有兼容性筛选权，不拥有下游质量证明。

它避免盲目合并，却可能把功能相近但谱不同的 adapter 拒绝，也无法观察真实数据上的交互。若有代表性目标数据，应优先做组合后评测；若坐标身份不明，回退独立加载。现有 exact-v1 仅覆盖作者的模型变体，不能给出通用兼容阈值。<!-- semantic-body-binding:SF-2026-ARXIV-2605-01929 -->

两个 adapters 的增量可以在权重空间相加或按系数组合，但数学上可相加不代表行为无冲突：

```text
W = W_0 + lambda_1 Delta W_1 + lambda_2 Delta W_2
```

不同 adapters 可能修改同一表示方向，组合后分布也可能超出各自训练范围。Adapter composition、merge 和 routing 都需要重新 Evaluation，不能把独立任务得分当作组合行为证明。

联邦训练还引入了坐标身份问题：同一个低秩权重增量可以由多组 `A/B` 因子表示，直接平均客户端因子会把任意坐标选择误当成更新语义。一个受限分支让客户端用 projector 描述更新子空间，服务端只在共识子空间与共享参考坐标中聚合，再从同一 server state 读出各客户端所需 rank；聚合 owner 持有的是 gauge-invariant update identity，而不是任一客户端的因子坐标。<!-- semantic-body-binding:SF-2026-ARXIV-2605-06733 -->

它避免恢复 dense delta，却增加子空间估计、参考坐标漂移、稀疏参与和异构 rank 的误差。共识不足、非 IID 行为回归失败或参与者可信边界不成立时，应回退 dense-delta aggregation、同构 rank 或不聚合的独立 adapter。exact-v1 的 GLUE、SuperNI、稀疏参与和异构 rank 实验只支持作者设置，不证明恶意参与、隐私约束或任意任务下都优于 FedAvg。

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

### 从持续改写共享权重到可检索的临时参数更新

持续 post-training 最直接的做法，是让每批新文档继续更新同一份模型权重。它在知识规模有限、更新经过统一验收且允许周期性发布新 checkpoint 时最简单；当文档持续到达、不同请求需要不同知识或必须撤销单份材料时，所有更新累积在共享参数里，会把遗忘、冲突与回滚边界混在一起。RAG 把知识留在模型外，避免累计 weight drift，却不能获得参数适配对下游行为的全部影响。

<!-- semantic-body-binding:SF-2026-ARXIV-2606-15734:start -->
一种中间分支把每份文档产生的低秩 gradient/update 预先计算为带 `base model、document、objective、optimizer 与 revision` 身份的 artifact，存入索引；请求到来时只检索相关更新，在隔离的模型视图中临时应用，响应结束后丢弃或回滚。这样把共享 checkpoint 的发布权留给训练控制面，把 query-specific adaptation 降为可撤销的运行时派生状态。若原始 language-modeling gradient 只擅长重构文档，还需要用独立 query/task contract 训练检索与更新映射；命中相关文档并不自动证明更新方向对当前任务有用。
<!-- semantic-body-binding:SF-2026-ARXIV-2606-15734:end -->

该路径用 gradient bank 容量、检索误配、临时权重物化、并发隔离和供应链审计换取可撤销适配。错误 update 可能污染一个请求，多个 update 的组合也没有天然交换律；因此 runtime 必须限制 rank、norm、作用层和生命周期，并在质量或安全 gate 失败时回退 base model、RAG 或经完整训练验收的持久 adapter。知识稳定、请求共享度高或每次临时更新成本过大时，定期训练并发布普通 LoRA 仍然更合理。

### 条件化机制分支与共存边界

主线之外仍存在若干只在特定前提下成立的设计分支。下面按状态与控制权的变化说明它们解决的问题、新增代价及回退边界；来源身份和实验限制统一留在章末 Review notes。

<!-- semantic-body-binding:SF-2026-ARXIV-2606-28479:start -->
用 matched-update controls 分离 DP guarantee、pseudonymization 与 optimizer-step memorization effect。
<!-- semantic-body-binding:SF-2026-ARXIV-2606-28479:end -->

### 训练便宜不等于部署便宜

LoRA 降低的是适配参数与训练成本；若上线时仍把 adapter 合并进完整 dense 模型，推理 FLOPs、内存访问和 kernel 形态未必下降。面向部署预算的 distillation 需要进一步决定保留哪些 rank、层或结构，把训练出的能力编译成真正满足 latency/memory budget 的 student。收益是把 PEFT 与 serving cost 连起来，代价是额外 teacher run、结构搜索和能力损失；多租户需要快速切换 adapter 时，保留 LoRA runtime 反而可能比生成多个 student 更合适。[受限证据：arXiv:2605.04341v1]

<!-- source-family:SF-2026-ARXIV-2605-04341 -->

### Procedural knowledge 可能超出低秩更新的容量边界

LoRA 对局部风格、格式或低维行为偏移高效，是因为目标更新近似落在低秩子空间；多步条件程序同时包含分支、状态转移和终态约束时，提高 rank 也未必恢复整条过程。此时“对话看似完成”与 terminal success 必须分开验收，否则局部步骤拟合会掩盖程序失败。

有限模型、任务和 rank 的实验只反证“继续加 rank 必然解决”，SVD 能量也不等于因果必需维度。若程序可外置，workflow/tool 加 verifier 往往比把控制逻辑全部压进 adapter 更可审计；若能力必须进入参数且低秩 gate 失败，应升级 full fine-tuning。LoRA 仍适合更新子空间稳定、验证充分的任务，而不是被后发方案静默替代。

<!-- source-family:SF-2026-ARXIV-2607-21612 -->

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

## 从机制演进到系统设计

LoRA 从一次低成本微调演进到多租户、持续变化的 adapter lifecycle 后，低秩矩阵不再只是训练参数，而是带 base revision、objective、contributor、priority 与撤销语义的独立 artifact。去中心化或边缘场景还要求系统明确谁拥有 contribution、怎样合并、参与者退出时如何 unlearn，以及何时需要重训。

细粒度 adapter 提高复用和个性化，却增加组合冲突、base 漂移、merge 顺序和 provenance 成本。校正或 unlearning 只有在目标 contribution 可定位、效果可验证时才可提交；否则保留旧 adapter、隔离租户或回退完整微调。参数更少不等于 runtime、registry 和安全状态更简单。

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

### 从学习适配器到生成适配器：只有低维且可复用时才成立

LoRA 通常把适配器视为需要通过梯度学习得到的模型状态；另一条分支是由模型直接生成任务专用适配器。后者省掉逐任务优化循环，但把误差来源从“训练是否收敛”改成“生成出的高维参数是否足够精确”。因此它只在适配状态维度较低、能够跨多个样本复用、生成与校验成本低于一次优化时更有吸引力；高维或长序列适配仍更适合常规训练。系统不应按方法名称选择，而应比较适配器维度、复用次数、生成误差预算和回退训练成本。
<!-- source-family: arxiv:2608.21386v1; semantic-body-binding: emitted-specialist-operating-regime -->

## 小结

LoRA 用 `BA` 低秩因子表示任务更新，显著减少 trainable parameters、gradients、optimizer states 和每任务 artifact。它保留基座模型的大部分计算，并以受限更新空间换取成本与资产复用。

QLoRA 继续压缩冻结基座存储，merge 与动态加载则把训练选择传播到 Serving。LoRA 的完整系统价值不只在“参数少”，而在 base、adapter、objective、checkpoint 和 runtime 之间形成可管理契约。

### Continual LoRA 需要把 Program Memory 与共享权重分开

连续把新任务写入同一 LoRA 会产生干扰，而为每个任务永久保存完整 adapter 又让检索和存储线性增长。Program memory 可以把可复用的参数更新单元作为有身份的程序保存，在新任务到来时检索、组合并再适配；共享 backbone 保持稳定，memory owner 管理程序来源、兼容性与淘汰。<!-- semantic-body-binding:SF-2026-ARXIV-2605-13162 -->

检索错误、组合冲突和 memory 膨胀会把遗忘转化为路由故障。现有 continual-learning 结果只支持所测任务序列；兼容性或 held-out performance 下降时，应回退独立 adapter、rehearsal 或重新训练，不把未知程序自动写入长期资产。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-07494:start -->
Continual VLM 不应把固定 MoE adapter pool 当作永久能力目录。训练面要独立拥有 expert evolution：何时复用、扩展、冻结或淘汰 expert；推理面只根据版本化 task prototype 提出 sparse selection，并保留 frozen base 的 zero-shot fallback。分权能限制遗忘和无关 adapter 干扰，却会造成 pool growth、prototype drift、错误 task identification 与额外路由成本；识别或预算不可靠时回退固定 adapter、共享 LoRA、rehearsal 或 frozen base。 [受限证据：arXiv:2605.07494v1]
<!-- semantic-body-binding:SF-2026-ARXIV-2605-07494:end -->

### Adaptation Support 与 Support 内变换应分开

普通 PEFT 往往在一个参数化里同时决定“哪些方向能更新”和“这些方向如何变化”。更清晰的分工让 support selector 根据 downstream gradient 提出可更新子空间，再让 orthogonal transform 只在其中改变方向；任务 loss 与 held-out gate 保留选择真值。它能提高有限 rank 的利用率，却增加梯度估计、子空间更新和 optimizer coupling，错误 support 会永久冻结所需方向。信号弱、任务多变或选择不稳定时，应回退固定 principal/coordinate support、普通 LoRA 或 full tuning，并按行为而非矩阵距离验收。exact-v1 只支持 matched-budget 的受测任务，不证明跨模型最优 support 或 orthogonality 自动防遗忘。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-11872 -->

### 低秩更新还可以避开 Skill-critical Subspace，但 Probe 不是能力真值

<!-- semantic-body-binding:SF-2026-ARXIV-2605-24549:start -->
普通 LoRA 让任务梯度在选定低秩空间内自由更新，目标兼容且回归充分时最简单；当知识注入开始损害既有 reasoning
skill，约束才从“rank 是否足够”变成“更新是否穿过能力关键方向”。一种条件分支先冻结模型，用 singular-vector
feature probe 标记 skill-critical subspace，再约束 LoRA 增量在其外部或低干扰方向中学习。probe 只提出保护区域，
最终能力保留仍由独立回归集拥有验收权。

两阶段投影增加 probe 数据、谱分解和训练成本；分布失配或表征旋转会保护错误子空间，也可能压掉新任务真正需要的
方向。exact-v1 只支持作者模型、任务和消融中的 PALoRA 分支，不证明 reasoning 能被固定线性子空间完整表示。probe
稳定性、知识获得或 held-out retention 不通过时，应回退普通 LoRA 加全量回归，必要时停止注入或选择更可隔离的
adapter/全量训练方案。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-24549:end -->
<!-- source-family:SF-2026-ARXIV-2605-24549 -->

## Review notes

- `SF-2026-ARXIV-2605-06733`（Status: Experimental）：[exact-v1](https://arxiv.org/html/2605.06733v1) 支持以共识子空间与共享参考坐标聚合异构 rank LoRA；证据限作者 GLUE、SuperNI、稀疏参与和客户端设置，不覆盖恶意参与者、通用隐私保证或任意非 IID 任务。

- [Scale-QLoRA v1](https://arxiv.org/html/2609.04526v1)，2026-09-07 Daily：§3目标 scale grid 下的训练/导出权重身份、§4–6有限任务与表达边界。正文不采用通用质量/速度优势；exact merge 以 codes、grid、clamp、layout 一致为条件，不等于高精度 LoRA。未独立复现 artifact。

- `SF-2026-ARXIV-2602-22268`（Status: Experimental）：exact-v1 的 §3.1～3.3 定义 bit-width/rank 联合问题、多保真 evolutionary search 与 Bayesian refinement，§4.1～4.5 及 Appendix E 固定作者模型、任务、search efficiency 与消融；§5/Impact Statement 和 task-wise appendix 不证明自动搜索跨模型、预算或 workload 普遍最优。https://arxiv.org/html/2602.22268v1

- `SF-2026-ARXIV-2604-26340`（Status: Experimental）：exact-v1 支持 LoRA-MoE exploratory training 后的 per-module Gini、routing entropy 与 drift-aware expert pruning；不证明该策略适用于任意 base MoE、adapter、任务或生产 SLO。https://arxiv.org/abs/2604.26340v1

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

### Daily integration evidence trace

#### Source-specific exact-v1 Review notes

- SF-2026-ARXIV-2606-28479 — primary arXiv:2606.28479v1; exact-v1 URL=https://arxiv.org/html/2606.28479v1; Method=https://arxiv.org/html/2606.28479v1 — §III Threat Model and Methodology; Evaluation=https://arxiv.org/html/2606.28479v1 — §VI Utility Evaluation; Non-proof=https://arxiv.org/html/2606.28479v1 — §III Threat Model and Methodology; III-A Threat Model; VII Discussion。

#### Source-specific exact-v1 Review notes

- `SF-2026-ARXIV-2606-22878` — primary `arXiv:2606.22878v1`; Method=`arXiv:2606.22878v1 — §Priority-Aware Learning-Unlearning Correction for Dynamic Decentralized LoRA Fine-Tuning Thanks: N. Yang, Y. He, S. Wang, and C. Yin are with the Beijing Laboratory of Advanced Information Network, and the Beijing Key Laboratory of Network System Architecture and Convergence, Beijing University of Posts and Telecommunications, Beijing 100876, China (emails: {yangnuocheng, heyechen, sihuawang, ccyin}@bupt.edu.cn). Thanks: Z. Chen and T. Q. S. Quek are with the Information Systems Technology and Design Pillar, Singapore University of Technology and Design, 487372, Singapore (emails: zihan_chen@mymail.sutd.edu.sg, tonyquek@sutd.edu.sg).; §III System Model and Problem Formulation; §III-A Dynamic Decentralized LoRA System`; Evaluation=`arXiv:2606.22878v1 — §IV Problem Analysis and Proposed Method; §IV-B Correction Gap Analysis under DGD; §V-C Ablation Study`; non-proof=`arXiv:2606.22878v1 — §VI Conclusion`; fallback=该 family 的 failure pressure 是：However, the dynamic nature of practical decentralized edge networks, where devices may dynamically join or leave the collaborative training process, requires the system to continuously adapt to new data while selectively removing prior contributions. 披露的 evaluation signal 是：To address this challenge, we propose a priority-aware learning-unlearning correction framework based on orthogonal LoRA that can enhance the knowledge evaluation through topology adjustment. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。

### Daily Books delta trace（2026-06—08）

<!-- daily-books-trace:SF-2026-ARXIV-2606-15734:start -->
- `SF-2026-ARXIV-2606-15734` — Daily `2026-06-15`；primary `arXiv:2606.15734v1`；Books review `books-review:SF-2026-ARXIV-2606-15734`。

  **已吸收的语义增量：** continual post-training可把document-specific gradient变成indexed retrievable artifact，在query时临时apply并在请求后rollback，避免shared-weight cumulative drift
<!-- daily-books-trace:SF-2026-ARXIV-2606-15734:end -->
