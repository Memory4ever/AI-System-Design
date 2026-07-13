# 第20章 Sampling

**Knowledge Tree:** Part II 模型：一个 Token 如何变成答案
**Status:** Draft

**Roadmap Intent:** 温度、top-k、top-p、贪心解码如何影响输出风格和稳定性。

## 本章要回答的问题

Decoder-only 模型每步输出 `V` 个 logits，为什么不能说“模型已经给出了答案”？Greedy、temperature、top-k 和 top-p 怎样把概率分布变成一个 token，又分别牺牲什么？

本章的核心判断是：**Sampling 是把模型条件分布转换为单条实际生成轨迹的决策过程。**它可以改变随机性、重复、尾部风险和输出多样性，不能增加 checkpoint 中不存在的知识，也不能把低概率正确答案稳定变成高概率答案。

本章使用 `B` 表示 batch size，`T` 表示 sequence length，`V` 表示 vocabulary size。

## Logits 还不是概率

第18章得到：

```text
logits shape = [B,T,V]
```

生成下一 token 时，取每个 sequence 最后一个有效 position：

```text
z shape = [B,V]
```

`z_i` 是 token `i` 的未归一化分数。Softmax 将它转换为概率：

```text
p_i = exp(z_i) / sum_j exp(z_j)
```

数值实现通常先减最大 logit：

```text
p_i = exp(z_i-z_max) / sum_j exp(z_j-z_max)
```

减去同一常数不会改变概率，却能减少 overflow。

## 一个固定 logits 例子

假设 vocabulary 只有三个候选，logits 为：

```text
z = [2,1,0]
```

Softmax 近似得到：

```text
p = [0.665,0.245,0.090]
```

模型认为 token 0 最可能，但 token 1 和 token 2 仍有非零概率。Decoder 必须选择：总取最大值，还是按某个变换后的分布随机抽样。

## Greedy decoding：每步取最大值

Greedy 选择：

```text
token = argmax_i z_i
```

在例子中总选择 token 0。它简单、单步确定、无需随机数，但只保证当前一步概率最大，不保证整段序列联合概率最高，也不保证最终任务质量最好。

语言生成中，局部最可能路径可能进入重复、模板化或过于保守的区域。另一方面，结构化抽取、分类式输出或严格复现任务可能更需要低随机性。

## Temperature 改变分布锐度

Temperature `tau > 0` 作用于 logits：

```text
p_i(tau) = softmax(z_i / tau)
```

- `tau < 1`：分布更尖锐，高 logit 更占优势。
- `tau = 1`：保持原 softmax。
- `tau > 1`：分布更平坦，低概率 token 更容易被选中。

对 `z=[2,1,0]`：

```text
tau=0.5 -> softmax([4,2,0])   ~= [0.867,0.117,0.016]
tau=1.0 -> softmax([2,1,0])   ~= [0.665,0.245,0.090]
tau=2.0 -> softmax([1,.5,0])  ~= [0.506,0.307,0.186]
```

Temperature 不改变 logits 排名，只改变相对概率。`tau -> 0` 的极限接近 greedy，但实现通常不会真的除以 0，而是使用专门 greedy path。

## Top-k：固定保留 k 个候选

Top-k 只保留概率或 logits 最高的 `k` 个 token，其余设为 0，再重新归一化。

例子中 `k=2`：

```text
before = [0.665,0.245,0.090]
keep   = [0.665,0.245,0.000]
renorm = [0.731,0.269,0.000]
```

它直接移除长尾候选，降低抽到极低概率 token 的风险。但固定 `k` 不感知分布形状：模型非常确定时仍保留 `k` 个，模型非常不确定时又可能只保留过少候选。

## Top-p：按累计概率动态截断

Nucleus sampling 先按概率降序排列，选择累计概率达到阈值 `p` 的最小 token 集合，再归一化抽样。

对同一例子，`top_p=0.8`：

```text
token 0 cumulative = 0.665 < 0.8
token 1 cumulative = 0.910 >= 0.8
```

因此保留 token 0 和 1，结果同上：

```text
[0.731,0.269,0.000]
```

若 `top_p=0.6`，第一个 token 已超过阈值，候选集可能只剩 token 0。具体实现通常保证至少保留一个 token。

Top-p 的候选数会随分布变化：模型确定时集合小，不确定时集合大。这是它相对固定 top-k 的主要适应性。

## 参数组合的顺序很重要

常见逻辑是：

```text
raw logits
-> penalties / constraints
-> temperature
-> top-k / top-p filtering
-> renormalize
-> random sample
```

但不同框架可能采用不同 processor 顺序，top-k 与 top-p 也可能同时启用并取交集。由于这些变换通常不可交换，相同参数名不保证跨 runtime 产生完全相同分布。

因此生产系统要版本化完整 decoding config，而不是只记录 temperature。

## Random seed 与确定性边界

随机抽样需要伪随机数。固定 seed、相同 logits、相同候选处理和相同随机数消费顺序时，通常可以复现 token 选择。

但端到端确定性还可能受以下因素影响：

- Batch 中请求进入和退出改变 RNG consumption。
- 并行执行与 kernel 可能包含非确定性。
- 不同 precision 使接近阈值的 logits 排名变化。
- Runtime 版本改变 logits processor 顺序。
- 模型、tokenizer、prompt 或 adapter 不同。

所以 `seed` 是生成配置的一部分，不是跨系统字节级复现保证。

## Sampling 为什么会影响长程行为

每步选择的 token 会进入下一步 prefix：

```text
x_(t+1) ~ p(. | x_<=t)
```

一次低概率选择会改变之后全部 logits。Sampling 因此不只是最终输出层的小装饰，而是在自回归闭环中持续改变状态轨迹。

过于 greedy 可能形成重复或单调模式；过高 temperature 或过宽 tail 可能让早期错误把序列带离高质量区域。Top-k/top-p 试图截断不可靠 tail，同时保留一定多样性。

不存在全任务通用的最佳参数。代码生成、创意写作、事实问答、结构化 JSON 和 Agent tool arguments 对随机性的容忍不同。

## EOS、停止条件和最大长度

EOS 是 vocabulary 中的特殊 token。若被选中，generation 可以结束。系统还可能使用：

- Maximum generated tokens。
- Stop token ids 或 stop strings。
- Grammar/schema constraints。
- 超时与任务预算。

Stop string 可能跨 token 边界，需要 detokenization 或增量匹配；EOS 则直接在 token 层终止。二者不能混为一谈。

若模型长期不给 EOS，max tokens 是系统安全边界。若 EOS 被错误 suppress，输出和 KV Cache 会持续增长。

## Logit penalties 与约束的边界

Repetition、frequency、presence penalties 会根据已生成 tokens 修改 logits；grammar-constrained decoding 会屏蔽不符合语法的候选。

它们都发生在 token selection 层，却解决不同问题：penalty 是启发式偏好，grammar mask 是硬候选约束。它们可能改善格式或减少重复，也可能屏蔽正确 token。

本章不展开具体 API，因为参数定义和顺序依赖实现。稳定原则是：任何 logits 变换都应进入 Evaluation 和可复现配置。

## Sampling 不能修复模型能力

降低 temperature 可以让高概率行为更稳定，但若正确答案本来概率很低，它不会创造知识。提高 temperature 可能偶尔采到正确答案，也会增加错误候选。

同样，top-p 只重分配已有分布，不判断事实正确性。Sampling 调整的是 capability 的表达与轨迹，不替代数据、训练、retrieval、tool 或 verifier。

## 工程与评估含义

生成配置应与模型版本一起评估：

- 单次成功率与 pass@k 回答不同问题。
- 平均质量会掩盖 seed 与长尾波动。
- 输出长度影响 latency、KV Cache 和成本。
- 结构化任务要测解析成功与语义正确。
- Agent 任务要测错误 action，而不只最终文本。

Sampling kernel 可以在 GPU 或 CPU 执行，是否成为瓶颈取决于 vocabulary、batch、约束复杂度和数据传输。本章不进入 scheduler 层。

## 本章在知识树中的位置

```text
Decoder hidden state
-> logits [B,V]
-> temperature / filtering / constraints
-> token id [B]
-> append token id to sequence
-> next Decode step computes and appends its K/V
-> repeat until stop
```

本章闭合一个 token 的生成循环。Part III 会解释后训练怎样改变 logits 分布，Part IV 会解释多个请求的 Decode 和 Sampling 怎样被 runtime 调度。

到这里，第 11～20 章的顺序主干已经闭合：文本变成 token ids，ids 变成带位置的 hidden states，Transformer 产生 logits 与 KV state，Sampling 选择 token 并把它追加回前缀。接下来的第 21、22 章不是 Sampling 之后的新步骤，而是回到这条主干内部，分别讨论参数容量和序列容量怎样扩展。

## 自检问题

1. Logits 与 probabilities 有什么区别？
2. 为什么 softmax 可以先减去最大 logit？
3. Greedy 为什么不保证整段序列最优？
4. Temperature 是否改变 token 排名？
5. `z=[2,1,0]` 时，较低 temperature 如何改变概率？
6. Top-k 与 top-p 的候选集规则有何区别？
7. 为什么 logits processor 顺序会影响结果？
8. 固定 seed 为什么仍不保证跨 runtime 完全复现？
9. EOS 与 stop string 分别在哪一层工作？
10. 为什么 Sampling 不能替代模型能力提升？

## 小结

Sampling 将模型给出的条件分布变成一条实际 token 轨迹。Greedy 选择局部最大值，temperature 改变分布锐度，top-k 固定候选数量，top-p 根据累计质量动态截断。

这些选择会在自回归循环中持续改变后续状态，因此必须与模型、prompt、seed、停止条件和 Evaluation 一起版本化。Sampling 控制能力如何表达，不创造模型没有的能力。

## Review notes

本轮联章 Review 明确本章是 token 生成主干的闭环点，第 21～22 章属于回看主干的容量扩展。正文仍以固定 logits 完成 temperature、top-k、top-p 的数值比较，并明确 processor 顺序和 seed 的实现边界。RLHF/SFT 属于 Part III，batch scheduling 属于 Part IV，不在本章展开。

Primary-source 校验入口：

- Angela Fan, Mike Lewis, Yann Dauphin, "Hierarchical Neural Story Generation", 2018: https://arxiv.org/abs/1805.04833
- Ari Holtzman et al., "The Curious Case of Neural Text Degeneration", 2019: https://arxiv.org/abs/1904.09751
