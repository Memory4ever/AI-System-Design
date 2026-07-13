# 第23章 数据

**Knowledge Tree:** Part III Training System：模型能力如何产生
**Status:** Draft

**Roadmap Intent:** 数据质量、分布、清洗、去重、配比决定模型上限。

## 本章要回答的问题

Part II 已经解释模型怎样把 token 变成答案，但参数最初并不知道语言、代码或世界知识。什么数据应该进入训练？为什么“更多 token”不等于“更多有效能力”？清洗、去重、配比、污染控制与 provenance 怎样共同决定模型最终优化的是哪个分布？

本章的核心判断是：**训练数据不是等待模型消费的原料，而是对模型行为分布的可执行 specification。**收集、过滤、去重、配比和采样共同定义经验风险中的样本权重；数据 pipeline 的任何偏差，都会通过梯度进入 checkpoint。

本章使用 `x` 表示一个训练样本或 token sequence，`q(x)` 表示训练数据分布，`q_k(x)` 表示第 `k` 个数据域的分布，`alpha_k` 表示该域的采样权重，`T` 表示 sequence length，`N` 表示训练 token 数。

## Part III 的能力生产链

Part III 不按工具目录组织，而按能力与训练状态怎样演化组织：

```text
Data
-> Pretraining
-> SFT / LoRA
-> Preference data and reward
-> PPO / GRPO / DPO
-> Checkpoint
-> Distributed Training
-> TP / PP / ZeRO
-> Megatron / DeepSpeed runtime
```

第 23～30 章主要回答“优化什么行为”，第 31～37 章主要回答“怎样可靠保存并扩展这段优化过程”。后半段不能反过来证明前半段的数据和目标正确；更高 GPU utilization 只意味着更快执行既定训练 specification。

## 先从“把互联网都抓下来”开始

最朴素的数据方案是收集尽可能多的网页、书籍、代码和对话，然后直接进行 next-token training。它看似最大化覆盖，实际会同时引入：

- 重复页面、镜像站点和模板文本。
- 垃圾内容、SEO 文本、乱码和机器生成污染。
- PII、版权、许可和删除请求风险。
- 语言、领域与时间分布失衡。
- Evaluation benchmark 或答案泄漏。
- 极端长短样本和不可控 token efficiency。

模型不会自动知道哪些内容是“高质量事实”，哪些只是高频重复。若某段文本出现一千次，它在经验风险中获得的权重就可能接近一千个独立样本，即使重复并没有增加新信息。

所以数据工程的目标不是让磁盘尽可能满，而是构造一个有来源、可解释、可复现、与能力目标匹配的训练分布。

## 数据分布就是优化权重

Pretraining 最小化训练分布上的期望 loss：

```text
R(theta) = E_(x ~ q)[L(theta; x)]
```

实际只能使用有限数据集：

```text
R_hat(theta) = (1 / n) * sum_(i=1)^n L(theta; x_i)
```

如果数据来自 `K` 个 domains，可以把采样分布写成：

```text
q(x) = sum_(k=1)^K alpha_k * q_k(x)

alpha_k >= 0
sum_k alpha_k = 1
```

`alpha_k` 不是中性的 loader 参数。它决定每个 domain 产生梯度的频率。代码占比增加，可能提升代码能力，也可能压缩自然语言、特定语言或长尾知识的有效训练预算。

数据配比因而是一种多目标优化：不同 domain 的 loss、能力收益、重复率、质量和合规成本并不相同。不存在脱离模型规模、token budget 与 Evaluation 的通用最优比例。

## 一个三域配比小例子

假设训练每 1000 个 sequences 期望采样：

```text
Web   alpha_web  = 0.60 -> 600 sequences
Code  alpha_code = 0.25 -> 250 sequences
Math  alpha_math = 0.15 -> 150 sequences
```

若原始数据库存量为：

```text
Web  = 90%
Code = 8%
Math = 2%
```

那么训练分布已经对 Code 和 Math 做了上采样。若 token budget 固定为 `N`，增加 `alpha_math` 不会凭空增加预算，而是在重新分配其他 domains 的训练机会。

这个例子也说明“数据占比”必须注明单位。按 documents、characters、bytes 或 tokens 统计，会得到不同结果；训练计算最直接对应的是实际进入 loss 的有效 tokens。

## Quality filtering 在过滤什么

质量不是单一分数。数据 pipeline 可能组合：

- 规则过滤：语言、长度、字符分布、重复符号、HTML 结构。
- 内容分类器：教育价值、可读性、主题、安全或垃圾概率。
- Source-level policy：来源许可、可信度、时间与地域。
- Model-based filtering：使用模型对文本质量或目标相关性评分。

过滤器会降低明显噪声，也会带来选择偏差。规则可能误伤代码、公式、方言或低资源语言；模型过滤器会继承评分模型的偏好；过度追求“教科书风格”可能减少真实世界多样性。

因此过滤策略需要同时报告 retention rate 和分布变化，而不能只报告“删除了多少低质量数据”。删除前后各语言、领域、长度和来源发生了什么，才决定模型看见了什么。

## 去重为什么改变梯度而不只是节省磁盘

Exact dedup 可以删除完全相同的 documents；near dedup 则要识别局部修改、模板替换或大段重叠。粒度可以是 document、paragraph、sequence 或 substring。

去重带来三类作用：

1. 减少重复样本对梯度的过度权重。
2. 在固定 token budget 下释放位置给更多独立内容。
3. 降低模型逐字记忆与 benchmark overlap 风险。

但去重不是“越强越好”。法律条文、代码模板、引用和常用表达天然重复；激进去重可能删除有效频率信号，或对短文本产生过高误判。

还必须明确去重集合：只在单个 shard 内去重，会漏掉跨 shard 重复；只在训练集内部去重，也不能发现训练与 Evaluation 之间的 contamination。

## Contamination 为什么破坏评估因果

若 benchmark 问题、答案或高度相似变体出现在训练数据中，模型得分无法清楚区分泛化与记忆。污染检查至少要区分：

```text
exact match
substring / n-gram overlap
near duplicate
semantic or transformed overlap
```

匹配越宽，召回越高，误报也越多。没有单一 detector 能证明数据绝对无污染。

更稳健的系统做法是：

- 在训练前冻结 Evaluation 集和 contamination policy。
- 保存匹配算法、阈值与删除记录。
- 对 benchmark 发布时间与数据抓取时间做 provenance 检查。
- 对高风险评估同时报告 contaminated/clean slices。
- 不把一次扫描结果写成永久“无污染”证明。

污染治理属于 Evaluation correctness，而不只是数据清洁度。

## Tokenizer、切分与 Packing 的边界

第 11 章已经解释 Tokenizer 的模型接口。本章关心的是固定 tokenizer 下，数据怎样形成训练 sequences：

```text
documents
-> tokenize
-> token stream
-> truncate / split / pack
-> input_ids [B,T]
-> labels [B,T]
```

将多个短 documents pack 到同一长度 `T`，可以减少 padding 并提高有效 token ratio。但系统必须明确 document boundary、EOS、position ids、Attention mask 和 loss mask。错误 packing 可能让本不相关文档互相读取，或让 label 跨边界预测。

截断也不是无害操作。总在文档尾部截断，会系统性减少结论、答案或长程结构；只保留短样本则会让模型缺少长上下文训练分布。

## Data lineage 是训练可复现性的前提

一个 dataset version 不能只由 bucket path 表示。至少需要记录：

- Source snapshot、抓取时间、许可与 provenance。
- 解析、normalization、过滤和去重代码版本。
- Tokenizer 与 vocabulary version。
- Domain mixture、sampling weights 和 random seed。
- Shard manifest、样本/token count 与 checksums。
- Evaluation exclusion 和 contamination policy。
- 删除、纠错与合规变更历史。

训练读取的应是不可变 manifest，而不是会被原地覆盖的目录。否则同一个 experiment config 在不同日期可能读到不同数据，却仍产生相同的“dataset name”。

Lineage 还连接到 checkpoint：只有知道某个 checkpoint 看过哪些 data versions、到哪个 data cursor，才能解释能力变化、恢复训练或执行删除影响分析。

## Streaming 与随机性

大规模数据常无法先完全 shuffle 到单机文件。系统会在 shards、workers 和局部 buffer 上执行多级随机化。

这里要区分：

```text
statistical shuffle quality
deterministic replay
distributed worker partition
```

Shuffle buffer 太小可能产生 source clustering；不同 worker 重复读取会改变样本权重；故障恢复若只恢复 optimizer step 而不恢复 data cursor，可能重复或跳过数据。

所以 data loader 不是训练外围组件。它参与定义实际 `q(x)`，并与第 31 章 Checkpoint 的可恢复状态直接相连。

## 数据质量不能只看 validation loss

Validation loss 能回答 held-out distribution 上的平均预测质量，却可能掩盖：

- 某些语言或领域退化。
- Memorization、PII 与版权风险。
- Benchmark contamination。
- Toxicity、安全与偏见。
- 长上下文、代码执行或事实时效性问题。

数据实验应把 model outcome 与 pipeline changes 连接起来。至少同时记录 token-level loss、能力切片、memorization/privacy tests、数据覆盖和训练效率。

DataComp-LM 一类 controlled data benchmark 的价值也在这里：保持模型与计算预算相对可比，才能把质量差异更可信地归因到数据策略，而不是隐藏在规模变化中。

## 本章在知识树中的位置

```text
Raw sources
-> provenance / policy
-> parsing / filtering / dedup / decontamination
-> domain mixture q(x)
-> tokenize / pack / shard / sample
-> Pretraining loss
-> Checkpoint capability
-> Evaluation and feedback
```

本章定义能力生产链的输入分布。第 24 章解释 next-token objective 怎样消费这些 tokens；第 31 章负责保存 data cursor 与 dataset identity；Part V 再把 lineage、权限和治理组织成平台能力。

## 自检问题

1. 为什么训练数据应被视为行为 specification，而不是被动原料？
2. Domain mixture 中 `alpha_k` 怎样影响梯度频率？
3. Documents 占比与 tokens 占比为什么可能不同？
4. Quality filter 为什么会产生新的选择偏差？
5. 去重为什么会改变经验风险，而不只是节省存储？
6. Training dedup 与 benchmark decontamination 有什么不同？
7. Packing 需要同时维护哪些边界和 masks？
8. 为什么 dataset name 不足以支持可复现训练？
9. Data cursor 为什么属于 checkpoint 状态？
10. Validation loss 为什么不能单独证明数据更好？

## 小结

数据 pipeline 通过过滤、去重、配比和采样构造训练分布 `q(x)`。模型优化的不是抽象的“互联网知识”，而是这条 pipeline 实际提供、按特定频率出现的 token sequences。

更可靠的数据系统必须同时管理质量、覆盖、重复、污染、provenance、合规和可复现性。数据决定能力生产的上游边界，也决定后续任何 loss 下降究竟代表什么。

## Review notes

本章将数据定位为经验风险的分布 specification，并建立 Data、Tokenizer、Pretraining、Checkpoint 与 Evaluation 的接口。具体 next-token loss 留给第 24 章；SFT demonstration 与 preference data 分别留给第 25、27 章；平台级数据权限和治理留给 Part V。

Primary-source 校验入口：

- Colin Raffel et al., "Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer", 2019: https://arxiv.org/abs/1910.10683
- Katherine Lee et al., "Deduplicating Training Data Makes Language Models Better", 2021: https://arxiv.org/abs/2107.06499
- Jeffrey Li et al., "DataComp-LM: In Search of the Next Generation of Training Sets for Language Models", 2024: https://arxiv.org/abs/2406.11794
- Luca Soldaini et al., "Dolma: an Open Corpus of Three Trillion Tokens for Language Model Pretraining Research", 2024: https://arxiv.org/abs/2402.00159
- Zekun Deng et al., "Investigating Data Contamination for Pre-training Language Models", 2024: https://arxiv.org/abs/2401.06059
