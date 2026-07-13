# 第18章 Decoder Only 架构

**Knowledge Tree:** Part II 模型：一个 Token 如何变成答案
**Status:** Draft

**Roadmap Intent:** 为什么主流 LLM 采用自回归 Decoder Only。

## 本章要回答的问题

第17章已经构造出可堆叠 Transformer Layer，为什么通用生成模型通常只保留 causal decoder stack？Encoder-only、encoder-decoder 与 decoder-only 分别规定了怎样的信息流和任务接口？

本章的核心判断是：**Decoder-only 架构用一个 causal next-token objective 统一了训练和生成接口。**任意任务只要能表达为“给定前缀，继续生成序列”，就可以共享同一参数栈；代价是输出天然串行，双向理解与输入输出分工不再由独立模块显式提供。

本章使用 `B` 表示 batch size，`T` 表示 sequence length，`V` 表示 vocabulary size，`d_model` 表示 hidden dimension，`L` 表示 layer 数。

## Transformer Layer 还缺什么

一个 Layer 只定义：输入 `[B,T,d_model]`，经过 Attention、MLP、Residual 和 Norm，输出相同 shape。它没有规定：

- token 可以读取左侧、右侧还是另一段序列。
- 哪些 positions 需要预测。
- 输入与输出是否使用不同模块。
- 最终 hidden state 怎样映射到 vocabulary。

模型架构通过 Attention mask、模块组织和训练目标回答这些问题。

## 三种主要组织方式

### Encoder-only

Encoder-only 通常允许每个 token 双向读取整段输入：

```text
token_i <-> all input tokens
```

它适合分类、表示学习、序列标注和 masked-token prediction。由于当前位置能看到右侧内容，不能直接用同一前向结果做严格自回归生成。

### Encoder-decoder

Encoder 先双向处理输入，Decoder 通过 cross-attention 读取 encoder states，并用 causal self-attention 生成输出：

```text
source -> encoder states
target prefix -> decoder self-attention + cross-attention -> next token
```

这种结构显式区分输入与输出，适合翻译、摘要等 sequence-to-sequence 任务，但需要两套 stack 或至少两类模块和 cross-attention 接口。

### Decoder-only

Decoder-only 把指令、上下文、示例和答案放进同一 token sequence，只使用 causal self-attention：

```text
all previous tokens -> predict next token
```

任务边界由文本格式、special tokens、mask 和 loss positions 表达，而不是由独立 encoder/decoder 模块固定。

## Causal language modeling

给定 token sequence：

```text
x_1, x_2, ..., x_T
```

Decoder-only 模型分解联合概率：

```text
p(x_1,...,x_T) = product_(t=1)^T p(x_t | x_<t)
```

这个公式把目标 token 记作 `x_t`，条件是它左侧的 `x_<t`。映射到模型张量时，输入位置 `t` 已经包含前缀 `x_<=t`，该位置的 logits 参数化的是：

```text
p(x_(t+1) | x_<=t)
```

也就是说，概率分解与 shifted targets 是同一件事的两种索引视角。Causal mask 保证位置 `t` 只能读取 `<=t` 的输入，label 再向左错开一位，避免未来 token 泄漏。

堆叠 `L` 层后得到：

```text
H_L shape = [B,T,d_model]
```

经过 final norm 和 vocabulary projection：

```text
logits = H_L W_vocab

W_vocab [d_model,V]
logits  [B,T,V]
```

每个位置都有一组 `V` 维 logits，对应下一 token 候选的未归一化分数。

## Shifted targets 小例子

文本 token 化后假设为：

```text
[BOS, The, sky, is, blue, EOS]
```

训练时输入和 label 错开一位：

```text
input : [BOS, The, sky, is, blue]
label : [The, sky, is, blue, EOS]
```

若 `B=1`、`T=5`：

```text
input_ids [1,5]
hidden    [1,5,d_model]
logits    [1,5,V]
labels    [1,5]
```

位置 0 根据 `BOS` 预测 `The`，位置 3 根据 `[BOS,The,sky,is]` 预测 `blue`。训练可以一次并行计算所有 positions，因为正确历史 tokens 已经由数据提供，同时 causal mask 阻止读取未来 labels。

## Teacher forcing 与生成串行性的差异

训练时每个位置读取真实历史 token，这常称为 teacher forcing。完整序列已知，因此 positions 可以并行执行。

推理时未来 token 不存在。模型先生成 `x_(t+1)`，把它追加到 prefix，才能生成下一步：

```text
prefix
-> forward
-> logits for next token
-> choose token
-> append token
-> repeat
```

所以 Transformer 训练 token 维度并行，不代表自回归 generation 也并行。同一请求的输出依赖链是 Decoder-only 推理延迟的根源。

## 为什么 Decoder-only 适合通用 LLM

第一，目标统一。网页、代码、对话和文档都可以转成 token stream，使用同一个 next-token objective。

第二，模块统一。只有一种主要 Transformer stack，不需要为每种任务设计独立 head 或 encoder-decoder 接口。

第三，运行时任务定义灵活。Instruction、few-shot examples、retrieved context 和 tool results 都可以作为 prefix，模型继续条件生成。

第四，Scaling 路径简单。数据和模型扩大时，训练 pipeline 可以围绕同一自监督目标组织。

这些优势解释了 decoder-only 成为通用生成模型的重要路线，不证明它在分类、双向表示、翻译或所有资源约束下始终优于其他架构。

## 统一接口带来的代价

Decoder-only 将所有内容放进同一 sequence，带来几个 trade-off：

- 输出逐 token 串行，latency 随生成长度累积。
- 长输入和输出共同占用 context 与 KV Cache。
- 输入、指令、工具结果和答案需要通过模板与 special tokens 区分。
- 双向理解要在 causal 条件下形成，而不是显式看到右侧。
- 开放生成的 Evaluation 比固定分类 head 更复杂。

系统因此需要 Tokenizer contract、chat template、KV Cache、Sampling 和停止条件共同完成一次生成。

## Loss mask 与“所有 token 都训练”

Pretraining 常对大量有效 positions 计算 next-token loss。Instruction tuning 可能只对 assistant response positions 计算 loss，而把 system/user tokens 作为条件。

这仍然可以使用同一 decoder-only stack：

```text
loss = sum_t mask_t * CrossEntropy(logits_t, label_t)
```

`mask_t` 决定哪些位置贡献 loss，不改变 causal Attention 本身。具体数据格式和训练阶段属于 Part III，本章只建立模型接口。

## Output projection 与 weight tying

第12章提到 input embedding matrix：

```text
E [V,d_model]
```

若使用 weight tying：

```text
W_vocab = E^T [d_model,V]
```

模型用同一组词表坐标完成输入 lookup 与输出评分。是否共享取决于 checkpoint，不能把它当作 decoder-only 必然条件。

## 从 logits 到 token 还差一步

Decoder stack 的直接输出不是文字，也不是唯一 token，而是 `[B,T,V]` logits。生成时通常只使用每个 sequence 最后一个有效 position 的 logits：

```text
next_logits shape = [B,V]
```

第20章会解释 greedy、temperature、top-k 和 top-p 怎样从这组 logits 选出实际 token。选出的 id 再通过 tokenizer decoder 转回 bytes/text。

## 本章在知识树中的位置

```text
token ids
-> Embedding + Position
-> L causal Transformer Layers
   |-> per-layer K/V -> KV Cache（第19章）
   `-> hidden [B,T,d_model]
       -> vocabulary projection [B,T,V]
       -> Sampling（第20章）
       -> next token -> append -> next Decode step
```

本章把第 11～17 章组成完整 causal language model。一次 Decode step 同时产生两类结果：供未来步骤复用的逐层 K/V，以及供当前步骤选 token 的 logits。第 19 章沿状态分支解释 KV Cache，第 20 章沿决策分支解释 Sampling，二者共同闭合自回归循环。

## 自检问题

1. Transformer Layer 与完整模型架构之间还缺哪些定义？
2. Encoder-only、encoder-decoder、decoder-only 的 Attention 信息流有何区别？
3. Causal factorization 如何表达序列概率？
4. `[B,T,d_model]` 怎样投影为 `[B,T,V]`？
5. Shifted input/label 为什么错开一位？
6. 为什么训练 positions 可并行，而生成仍串行？
7. Decoder-only 为什么能用 prefix 表达多种任务？
8. Loss mask 与 causal mask 分别控制什么？
9. Weight tying 共享哪两个接口？
10. Logits 为什么还不是最终 token？

## 小结

Decoder-only 用 causal mask 与 next-token objective 把一个 Transformer stack 变成通用条件生成模型。训练时 shifted targets 提供所有位置的监督，推理时模型必须逐步生成并追加 token。

这种统一接口简化了数据与任务表达，也把序列状态、生成串行性、Sampling 和评估复杂度带入系统。它是现代 LLM 的重要架构选择，而不是所有任务的唯一最优解。

## Review notes

本轮联章 Review 对齐了 causal factorization、tensor position 与 shifted target 的索引，并把第 19 章的状态分支和第 20 章的决策分支放回同一个 Decode step。本章仍只解释架构、mask、shifted targets 和 logits contract。Pretraining/SFT 数据与 loss 配置属于 Part III，Prefill/Decode 的硬件执行与调度属于 Part IV。

Primary-source 校验入口：

- Alec Radford et al., "Improving Language Understanding by Generative Pre-Training", 2018: https://cdn.openai.com/research-covers/language-unsupervised/language_understanding_paper.pdf
- Jacob Devlin et al., "BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding", 2018: https://arxiv.org/abs/1810.04805
- Colin Raffel et al., "Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer", 2019: https://arxiv.org/abs/1910.10683
