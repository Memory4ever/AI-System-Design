# 第11章 Tokenizer

**Knowledge Tree:** Part II 模型：一个 Token 如何变成答案
**Stable Knowledge Node ID:** `MODEL-TOKENIZER`
**Legacy Chapter:** Ch11
**Status:** Draft

**Roadmap Intent:** 文本如何被切成 token，为什么 tokenizer 会影响知识表示、上下文长度和多语言能力。

## 本章要回答的问题

神经网络只能处理有限维张量，真实文本却由开放词汇、Unicode 字符、代码、数字和不断出现的新名字组成。怎样把任意文本稳定地转换为有限词表中的整数序列，又不让词表或序列长度失控？

本章的核心判断是：**Tokenizer 是文本世界与模型计算之间的离散接口。**它不只是预处理工具，而是在 vocabulary size、sequence length、可逆性、多语言覆盖和系统成本之间选择计算粒度。

Tokenizer 的输出止于文本 token ids。id 如何进入连续空间属于第12章；第23章把离散协议扩展到 image/video/audio codec，并增加 modality、timestamp、coordinate 与 codebook identity；训练语料如何清洗、去重和治理属于第27章。文本 tokenizer 与多模态 codec 复用“离散协议”原则，但不共享相同信息损失、序列尺度或 decoder contract。

本章使用 `B` 表示 batch size，`T` 表示 token sequence length，`V` 表示 vocabulary size，`d_model` 表示模型 hidden dimension。

## Part II 的阅读主线

Part I 已经从世界观层面解释模型能力、系统交付与长期约束。从本章开始，我们把模型从黑盒展开，沿一个 token 的生命周期追踪接口与状态：

```text
第11～20章：生成主干

Text
-> Tokenizer ids
-> Embedding + Position
-> Self Attention + MLP
-> Transformer Layer
-> Decoder-only logits
-> KV state + Sampling
-> next token

第21～22章：容量扩展

Dense MLP -> MoE                 参数容量轴
Position + Attention + KV Cache -> Long Context  序列容量轴
```

因此目录顺序不完全等同于一次 forward 的算子顺序。第 11～20 章闭合生成主干；第 21 章回到第 16 章扩展 MLP，第 22 章再汇总位置、Attention 与 KV Cache 的长序列约束。先区分主干与分支，后续才不会把模型结构、生成策略和系统优化混成一条流水线。

## 为什么不能直接按词切分

最符合人类直觉的方案是把每个词作为一个 token。对句子：

```text
AI systems learn patterns
```

可以得到四个词。但真实词汇不是封闭集合。人名、拼写变化、复合词、URL、代码标识符和新术语会不断出现。若为每个词分配独立 id，词表会持续膨胀；若只保留高频词，未登录词只能统一变成 `<unk>`，不同信息被不可逆地压成同一个符号。

另一个极端是按字符切分。字符词表较小，也几乎没有 OOV，但同一段文本会产生更长序列。Transformer 的 Attention 和 KV Cache 成本依赖 token 数，字符级表示会把简单词语拆成很多计算步。

因此需要中间粒度：高频模式保留为较长 token，低频词退化成较短 subword、字符或 byte。目标不是找出语言学上唯一正确的词，而是构造可计算、可覆盖的离散词表。

## BPE：从最小单元逐步合并

Byte Pair Encoding 原本是一种压缩思想，subword BPE 将其用于开放词汇建模。简化训练过程如下：

1. 把训练文本表示为初始符号序列。
2. 统计相邻符号 pair 的频率。
3. 合并最高频 pair，生成新符号。
4. 重复直到达到目标 vocabulary size 或 merge 次数。

下面用一个小例子演示。假设语料为：

```text
low low lower
```

以字符为初始单元，并用 `</w>` 标记词尾：

```text
l o w </w>
l o w </w>
l o w e r </w>
```

高频 pair `l o` 可以先合并为 `lo`，随后 `lo w` 可合并为 `low`。最终可能得到：

```text
low </w>
low </w>
low e r </w>
```

`low` 因为高频获得完整 token，`lower` 仍可由 `low + e + r` 表示。BPE 学到的是语料中的频率结构，不保证 merge 边界与人类词法完全一致。

编码新文本时，必须使用固定 vocabulary 和 merge rules，不能根据单个请求重新训练。否则同一模型权重会面对不稳定 id 语义。

## Unigram 与 SentencePiece 的另一条路线

BPE 从小单元开始不断合并；Unigram Language Model 常从较大的候选 subword 集合开始，估计各 token 的概率，再逐步删除贡献较低的候选。对同一字符串，它可能存在多种切分，算法根据整体概率选择路径。

SentencePiece 的系统意义不只是实现某种算法。它可以直接从 raw sentences 训练，不要求先依赖特定语言的空格分词，从而使相同 pipeline 更容易覆盖中文、日文及混合语言。

两条路线的稳定差异是：

```text
BPE      frequent pair merging determines vocabulary
Unigram  probabilistic candidates compete as segmentations
```

具体模型采用哪种实现，需要根据其 tokenizer artifact 核验，不能从模型名称推断。

## Byte fallback 为什么重要

即使 subword 词表覆盖很广，Unicode 仍然是开放组合空间。Byte-level tokenization 或 byte fallback 为任意输入提供最终退路：无法由已有文本 token 表示时，转成底层 bytes。

这样可以避免 `<unk>` 丢失信息，但会产生代价。稀有字符可能展开成多个 byte tokens，序列更长；人类看到的一个字符也不一定对应一个 token。Emoji、组合音标和非拉丁文字尤其容易暴露这个差异。

因此要区分三层：

```text
Unicode text -> encoded bytes -> tokenizer symbols -> token ids
```

字符数、byte 数和 token 数不是同一单位。API 计费、context limit 和 KV Cache 容量通常按 token，而不是用户界面里的字符数。

## Normalization 与可逆性

编码前可能执行 Unicode normalization、大小写转换、空白处理或前缀空格规则。Normalization 可以减少表面变体，却也可能丢失原始差异。

一个 tokenizer 是否满足：

```text
decode(encode(text)) == text
```

取决于 normalization、未知符号和 decoder 规则。许多 byte-level 设计可以对广泛输入做到近似或严格可逆，但不能把可逆性当作所有 tokenizer 的天然性质。

生产系统必须把 tokenizer 版本与 checkpoint 一起管理。只替换 tokenizer 而保留模型权重，会改变 token id 与 embedding row 的对应关系，即使词表大小相同也可能完全破坏语义。

## Special tokens 是协议，不是普通文本

模型通常需要 BOS、EOS、PAD、UNK 或对话角色等 special tokens。它们属于模型输入协议，用来表达序列开始、结束、padding、角色边界或控制状态。

Special token 的风险在于，它可能在文本层看起来像普通字符串，却在 tokenizer 层被映射成保留 id。系统需要明确：

- 用户能否直接注入 special token。
- chat template 在哪里添加角色和边界。
- padding 是否参与 loss 和 Attention。
- EOS 是否既是训练标签，也是生成终止条件。

这些规则如果在训练、评估和 Serving 之间不一致，会形成隐蔽的 training-serving skew。

## Vocabulary 与序列长度的系统权衡

一段文本编码后长度为 `T`。Tokenizer 设计会同时影响后续两类成本。

更大的 `V` 往往能用更少 token 表示高频文本，但会扩大 embedding table 和输出 projection：

```text
embedding parameters = V * d_model
logits shape         = [B, T, V]
```

更小的 `V` 减少词表参数，却可能增大 `T`。标准 dense Attention 的成对关系随 `T^2` 增长，KV Cache 则近似随 `T` 增长。于是 tokenizer 会沿整条系统链传播影响：

```text
Tokenizer
-> sequence length
-> Attention compute
-> KV Cache capacity
-> latency / throughput / cost
```

不存在脱离语料和 workload 的“最佳词表大小”。代码、中文、英文、数字和多语言混合流量可能产生完全不同的 token efficiency。

## 从无状态预处理到会话级增量接口

一次性请求中，每次对完整文本重新执行 tokenizer 是合理设计：实现简单、结果容易与模型
artifact 对齐，而且 tokenization 通常不是主导成本。Agent 与长对话改变了这个约束。一次
trajectory 会反复提交“几乎相同的长前缀 + 很短的新后缀”；即使后端能够复用 prefix KV，
前端若仍扫描完整文本，累计 tokenization work 仍可能随会话长度快速增长。优化下游缓存以后，
瓶颈会向上游接口迁移。

不能把旧 token ids 与新后缀的 token ids 直接拼接，因为一般并不满足：

```text
tokenize(prefix) ++ tokenize(delta) == tokenize(prefix ++ delta)
```

Normalization、pre-tokenization 和 subword merge 都可能跨越拼接边界。安全的增量实现因此
不是“缓存一次函数结果”，而是维持一份可验证的会话状态：已有 token ids、它们覆盖的 byte
范围、tokenizer 内容摘要与版本，以及用于判断旧后缀何时重新稳定的边界信息。新文本到来时，
实现只重算受影响的 suffix；只有找到该 tokenizer family 可证明的稳定边界，才复用更早的
结果。找不到边界、版本变化或输入不满足适用条件时，必须扩大重算范围，最终回退到完整的
reference tokenizer。

这把 tokenizer contract 从“对同一文本通常给出相同结果”提升为更强的等价性要求：

```text
incremental_result == frozen_reference_tokenizer(full_text)
```

工程上还需要 sampled shadow verification、mismatch quarantine、显式 fallback reason，以及把
tokenizer state 与 KV state 分开管理。前者体积通常更小，可以在 KV eviction 后继续存在；但
它会新增 session affinity、replication、version invalidation、admission 和 recovery 问题。
当增量很大、tokenizer family 无法提供稳定边界，或 KV prefix 本身已经失效时，无状态完整
编码仍然是更简单、也可能更快的方案。因此增量 tokenization 与 prefix KV reuse 是
`Layering / Dependency`，不是新实现对旧实现的单向替代。

## 多语言中的隐藏不公平

如果 tokenizer 的训练语料主要来自某种语言，该语言的高频片段更容易获得较长 token；覆盖较少的语言可能被拆得更碎。对于相同语义，不同语言的 `T` 可能不同，从而影响：

- 可放入 context window 的内容量。
- 推理延迟和 token 计费。
- 梯度中各语言的有效位置数量。
- 稀有文字退化到 byte 时的表示难度。

Tokenizer 不能单独决定多语言能力，数据分布、模型容量和训练目标同样重要。但它决定了模型最初看到的离散粒度，因此必须把 token fertility 和语言切片纳入 Evaluation。

## 一个完整的 shape 接口

假设 batch 中有 `B=2` 个句子，padding 后每个句子 `T=4` 个 token：

```text
text batch
-> tokenizer
-> input_ids shape [B, T] = [2, 4]
-> attention_mask shape [B, T] = [2, 4]
```

`input_ids` 中每个值都应满足 `0 <= id < V`。这些整数没有数值距离语义。第12章会用它们索引 embedding matrix，得到 `[B, T, d_model]` 的连续张量。

## 工程验证清单

Tokenizer 接入不应只测试一句英文。至少需要验证：

- encode/decode round trip 与 normalization 预期。
- 中文、英文、代码、数字、emoji 和异常 Unicode。
- special tokens、chat template、padding、truncation 和 EOS。
- 与 checkpoint 声明的 vocabulary、id mapping 和配置一致。
- 目标流量中的 token length 分布，而不是只看字符长度。
- tokenizer 版本变化后的离线评估与容量影响。
- 长会话增量路径与 frozen reference 的逐 id 等价、fallback 与 mismatch quarantine。
- tokenizer session state 与 KV Cache 的 identity、lifetime、eviction 和恢复边界。

## 本章在知识树中的位置

```text
Raw text
-> normalization
-> subword / byte segmentation
-> token ids [B, T]
-> Embedding [B, T, d_model]
```

Tokenizer 是 Part II 的入口，也是 Part I 宏观约束第一次落到具体 tensor contract 的位置。它定义模型的离散输入接口，也提前决定了后续参数、Attention、KV Cache 和 Serving 成本的一部分。

本章只拥有 text ↔ token ID。第23章拥有 raw modality ↔ continuous/discrete multimodal representation；把 image code 称为 token 不会让它自动继承文本的可逆性、边界或序列成本。

这份接口会跨 Part 延续：第 27 章在固定 tokenizer 下构造训练 sequences，
第 29 章把 special tokens 与 chat template 纳入 SFT protocol，第 42 章要求
Serving 以同一 tokenizer artifact 还原请求。任一环节独立替换 normalization、
vocabulary 或 role tokens，都会形成 training-serving skew。

## 自检问题

1. Word-level tokenizer 为什么会遇到开放词汇问题？
2. Character-level tokenizer 用什么代价换取 OOV 覆盖？
3. BPE 的 merge 是如何从小语料统计得到的？
4. BPE 与 Unigram 的搜索方向有什么不同？
5. Byte fallback 为什么能减少 `<unk>`，又为什么可能增加 token 数？
6. 为什么替换 tokenizer 会破坏原 checkpoint？
7. Vocabulary size 为什么同时影响 embedding 参数和 Attention 成本？
8. Special tokens 为什么应被视为协议？
9. Tokenizer 如何造成多语言 token efficiency 差异？
10. `[B,T]` 的 token ids 为什么不能直接作为连续数值输入模型？
11. 为什么 `tokenize(A) ++ tokenize(B)` 一般不等于 `tokenize(A ++ B)`？
12. 增量 tokenization 为什么需要 reference equivalence、版本绑定与安全回退？

## 小结

Tokenizer 在无限文本空间和有限模型词表之间建立可复现映射。Subword 方法在词级 OOV 与字符级长序列之间折中，byte fallback 提供开放输入覆盖，special tokens 则建立模型协议。

这个选择会一路影响 embedding 参数、sequence length、Attention、KV Cache、成本和多语言公平性。Tokenizer 不是语言学答案，而是 AI System 的第一份模型接口契约。

## Review notes

本轮联章 Review 补充了 Part II 的主干与扩展分支地图。本章仍止于 token ids，不展开 embedding 训练，也不把 tokenizer training 混入 Part IV 的数据治理。后续 Review 应以具体 checkpoint 的 tokenizer artifact 核验 normalization、special-token 和 byte fallback 行为，避免把某个库的默认配置写成通用机制。

Primary-source 校验入口：

- Rico Sennrich, Barry Haddow, Alexandra Birch, "Neural Machine Translation of Rare Words with Subword Units", 2016: https://arxiv.org/abs/1508.07909
- Taku Kudo, John Richardson, "SentencePiece: A simple and language independent subword tokenizer and detokenizer for Neural Text Processing", 2018: https://arxiv.org/abs/1808.06226
- Taku Kudo, "Subword Regularization: Improving Neural Network Translation Models with Multiple Subword Candidates", 2018: https://arxiv.org/abs/1804.10959
- Zhenyu Zhang, Zhichao Cao, "TokTier: Exact Stateful Tokenization for Agentic LLM Serving", 2026（Status: Emerging；作者实验，不外推性能数字）: https://arxiv.org/abs/2607.29678
