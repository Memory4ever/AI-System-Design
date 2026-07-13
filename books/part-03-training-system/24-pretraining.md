# 第24章 Pretraining

**Knowledge Tree:** Part III Training System：模型能力如何产生
**Status:** Draft

**Roadmap Intent:** 大规模预训练如何形成通用语言和世界知识。

## 本章要回答的问题

第 23 章已经把数据构造成 token sequences，Part II 也已经给出 Decoder-only 模型。模型怎样仅通过预测下一个 token 改变数十亿参数？Loss 下降、perplexity、训练 token 数、optimizer step 与能力增长分别是什么关系？为什么一次成功的 Pretraining run 不只是反复调用 `backward()`？

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

第 31 章会说明：若 checkpoint 只保存 `theta` 而不保存 optimizer、scheduler、random state 和 data cursor，通常只能继续做新的 fine-tuning，不能精确恢复原 Pretraining trajectory。

## Batch、tokens 与 optimizer steps 不是同一计量

设每个 optimizer step 的 global batch 为 `B_global`，有效平均 sequence tokens 为 `T_eff`：

```text
tokens_per_step ~= B_global * T_eff
N ~= steps * tokens_per_step
```

若存在 padding、packing、loss mask 或变长 sequences，`T_eff` 应按实际参与 loss 的 token 数计算，而不是配置中的 `T_max`。

增大 batch 可以提高矩阵规模和并行效率，也会减少固定 token budget 下的 optimizer steps，并改变梯度噪声与 learning-rate 选择。Gradient accumulation 可以在不一次放入全部 samples 的情况下形成更大 effective batch，但不能消除多次 forward/backward 的计算。

完整关系在第 32 章写成：

```text
B_global = B_micro * accumulation_steps * data_parallel_degree
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

## Mixed precision 为什么不是简单改 dtype

FP16、BF16 或更低精度可以减少 memory、communication bytes 并利用专用硬件，但训练需要维持数值范围和累积精度。

系统可能使用：

- 低精度参数或计算。
- 更高精度 master weights 或 optimizer states。
- FP32 accumulation。
- Dynamic loss scaling，尤其用于 FP16 underflow 风险。

所以“模型以 BF16 训练”并不能唯一确定每份状态的 dtype。Checkpoint、optimizer memory 估算和 collective bytes 都必须基于实际 precision policy。

## Activation checkpointing 移动了什么瓶颈

Backpropagation 需要 forward activations。全部保留会占据大量显存；activation checkpointing 只保存部分边界，backward 时重新计算中间 activations：

```text
less saved activation memory
<-> more recomputation FLOPs
```

它减少的不是 parameters、gradients 或 optimizer states。第 35 章 ZeRO 主要处理 model-state redundancy，两者解决不同 memory categories，可以组合。

Checkpoint 这个词在这里容易混淆：activation checkpointing 是计算图重算策略；第 31 章的 training checkpoint 是持久化恢复状态。

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

第 23 章决定训练分布，本章决定基础 objective 与训练循环；第 25 章将目标收窄到指令 demonstrations。第 31～37 章再解释这段循环怎样被持久化并扩展到多 GPU。

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

## 小结

Pretraining 用大规模 next-token prediction 把数据分布转化为参数更新。Cross-entropy 定义局部误差，optimizer 与 schedule 决定更新轨迹，batch、precision、activation memory 和分布式执行决定这条轨迹能否在可接受成本内完成。

预训练 checkpoint 是通用能力底座，不是最终产品行为。它学到什么由数据、objective、容量和优化共同决定；它是否可靠还需要独立 Evaluation 与后续训练约束。

## Review notes

本章只负责 next-token objective、训练 step、token/batch 计量、optimizer state 与训练稳定性。数据治理留在第 23 章；SFT 和 preference optimization 留在第 25、27～30 章；collective、state sharding 和 framework runtime 留在第 32～37 章。

Primary-source 校验入口：

- Diederik P. Kingma, Jimmy Ba, "Adam: A Method for Stochastic Optimization", 2014: https://arxiv.org/abs/1412.6980
- Alec Radford et al., "Improving Language Understanding by Generative Pre-Training", 2018: https://cdn.openai.com/research-covers/language-unsupervised/language_understanding_paper.pdf
- Tom B. Brown et al., "Language Models are Few-Shot Learners", 2020: https://arxiv.org/abs/2005.14165
- Jared Kaplan et al., "Scaling Laws for Neural Language Models", 2020: https://arxiv.org/abs/2001.08361
- Jordan Hoffmann et al., "Training Compute-Optimal Large Language Models", 2022: https://arxiv.org/abs/2203.15556
