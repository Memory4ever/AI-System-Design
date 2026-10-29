# 第18章 Decoder Only 架构

**Knowledge Tree:** Part II 模型：一个 Token 如何变成答案
**Stable Knowledge Node ID:** `MODEL-DECODER-ONLY`
**Legacy Chapter:** Ch18
**Status:** Draft

**Roadmap Intent:** 为什么主流 LLM 采用自回归 Decoder Only。

## 本章要回答的问题

[第17章](./17-transformer-layer.md)已经构造出可堆叠 Transformer Layer，并说明在采用 causal 信息流时应满足 prefix invariance；但 shape 稳定、因果信息流正确，还没有定义模型应该预测什么。为什么通用生成模型通常只保留 causal decoder stack？Encoder-only、encoder-decoder 与 decoder-only 分别规定了怎样的信息流和任务接口？

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

这种结构显式区分输入与输出，适合翻译、摘要等 sequence-to-sequence 任务。标准实现分别运行 decoder self-attention 与 cross-attention，承担 encoder/decoder stack 和额外接口的参数与执行成本；但信息流分工不要求每种 Attention 永远由独立参数实现。一个替代分支共享 encoder 输入、decoder 输入与输出 embedding，并让 decoder Query 同时读取 encoder states 和 causal target prefix：两段状态共同投影为 K/V，在同一个 softmax 中归一化，由 mask 管理 source 与 target 的可见性。它不是两个独立 softmax 输出相加，合并模块也不意味着保留原函数。

[T5Gemma 2 的局部架构消融](https://arxiv.org/html/2512.14856v1#S2)展示了这种参数冗余与质量之间的取舍，同时保留一个反例：只在每六层中的 global 层保留 cross-attention，平均质量下降更大。这是在 Gemma 2 2B 初始化、400B tokens 和 PrefixLM+KD 配置下得到的局部对照，不是最终 Gemma 3 配方的全任务无损证明，也未给出端到端加速或节能的受控证据。Encoder-decoder 因而仍有设计空间，但不能据此宣称它普遍取代 decoder-only；跨架构比较还需要分开数据、训练预算和后训练配方。<!-- source-family:SF-2025-GOOGLE-T5GEMMA-2 -->

输入与输出职责还可以分配给已预训练的外部模块，而不重新训练中央语言模型：多语encoder先把源文本变成状态，经学习到的映射交给冻结的语言模型；中央模型仍逐token生成英语序列，再把相应hidden经另一映射作为多语decoder的cross-attention K/V，由目标语言标记控制最终输出。这改变的是语言输入、中央计算与目标语言表达的组合接口，不是省去英语中间生成，也不证明冻结参数使知识能力必然不变。不同tokenizer产生的序列未必逐位置对应；同一中央输出再经encoder得到的表示可提供兼容监督，但相似度与放松匹配不认证语义等价、顺序或全部内容保真。<!-- source-family:SF-2026-ARXIV-2603-17512 -->

这一组合要同时验输入理解、中央结果和最终目标语言表达，不能用平均翻译分数把三者合成一个“语言无关知识core”证书。[有限XBridge对照](https://arxiv.org/html/2603.17512v1#S4)中，一些语言方向及decoder输出仍退步，额外decoder也比只运行原语言模型更慢。两侧映射与cross-attention训练、机器翻译数据、额外encoder/英语生成/目标decoder及接口回归都付费；部署应共同绑定三个checkpoint、两侧tokenizer、映射和取层位置，再分别检查内容保持、语言遵守与端到端预算。语言覆盖、接口或质量不适配时，保留原native生成、显式translate-test或重新适配，而不把外部表达流畅当成中央结论正确。

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

也就是说，概率分解与 shifted targets 是同一件事的两种索引视角。Causal mask 在 Attention 路径上声明位置 `t` 只能读取 `<=t` 的输入，label 再向左错开一位，由此建立 next-token learning 的局部信息边界。

但 mask 只是 Attention 路径的声明，不是整个 Decoder block 已经满足因果性的证明。跨位置 normalization、并行 scan、fused kernel 或错误的状态复用仍可能把未来信息带回当前位置。因此，第 17 章把完整实现的因果性提升为可观测的 **prefix invariance**：同一前缀单独运行与作为更长序列前缀运行时，前缀位置的输出必须在数值容差内一致。这里先定义架构 contract，完整行为审计由该不变量闭合。

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

当任务本来已知右侧文字时，还可以保留待生成部分的左到右分解，而另给它一份位置感知的条件副本：副本保留原位置编码、内部可双向读取，主序列读取副本和自己的causal前缀，只对未知目标计loss。[受限的任意条件分支](https://arxiv.org/html/2606.14943v1#S3)不把原未来节点直接开放给所有位置，因为该节点若也读取了主序列中间目标，后续层会把目标信息绕回更早预测。已知条件的producer与目标历史因此必须隔离，条件集合/原位置/可见图和loss资格共同定义接口。一次teacher-forced前向能评价多项条件概率，不等于一次就生成全部未知tokens，也不证明不同查询已与原模型的同一joint精确兼容。副本长度、条件构造/适配和全部顺序生成都付费，条件分布与原AR质量亦有取舍；条件权限、跨层隔离或结果未过时，保普通causal续写、已验FIM/encoder–decoder，不由相同checkpoint形状批准任意条件与免费生成。

<!-- source-family:SF-2026-ARXIV-2606-14943 -->

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

位置 0 根据 `BOS` 预测 `The`，位置 3 根据 `[BOS,The,sky,is]` 预测 `blue`。训练可以一次并行计算所有 positions，因为正确历史 tokens 已经由数据提供；causal mask 阻断未来位置的 Attention edge，而完整实现是否仍存在其他跨位置泄漏，需要用第 17 章的 prefix invariance 行为审计确认。

## Loss mask 与“所有 token 都训练”

Shift 确定了每个位置的正确答案，接下来还要决定哪些答案参与优化。Pretraining 常对大量有效 positions 计算 next-token loss。Instruction tuning 可能只对 assistant response positions 计算 loss，而把 system/user tokens 作为条件。

这仍然可以使用同一 decoder-only stack：

```text
loss = sum_t mask_t * CrossEntropy(logits_t, label_t)
```

`mask_t` 决定哪些位置贡献 loss，不改变 causal Attention 本身。具体数据格式和训练阶段属于 Part IV，本章只建立模型接口。

## Teacher forcing 与生成串行性的差异

训练时每个位置读取真实历史 token，这常称为 teacher forcing。完整序列已知，因此 positions 可以并行执行。

这说明的是训练输入为何能并行给出，不是模型一次前向就能生成所有未知 token。要看清两者的差别，还需把 hidden state 到词表评分、再到实际 token 的接口补全。

## Output projection 与 weight tying

前面的 `[B,T,V]` logits 来自 hidden state 的词表投影；输入端则使用[第12章](./12-embedding.md)的 input embedding matrix：

```text
E [V,d_model]
```

若使用 weight tying：

```text
W_vocab = E^T [d_model,V]
```

模型用同一组词表坐标完成输入 lookup 与输出评分。是否共享取决于 checkpoint，不能把它当作 decoder-only 必然条件。

Decoder的hidden state也可以服务于非文字输出，但必须更换并训练目标读出，而不是让词表概率自动成为数值预测。一个受限回归分支冻结LLM token表示，以一个可学习latent query反复cross-attend这些状态，再输出scalar；训练split上的target normalization和Huber loss属于这份任务head，不能在测试人口重估尺度。与参数匹配MLP的有限对照支持该读出选择，ranking reward还可能改善相关排序而不改善RMSE，WMT和STS也有收益差异，故不能说backbone天然拥有通用精确数值知识。冻结前向、head训练/优化与多次候选ranking都计费；任务、尺度或完整预算失配时，保留简单linear/MLP readout、普通numeric-text输出与独立回归验收，不由一个任务head替代标准next-token生成接口。 [必要机制与反侧](https://arxiv.org/html/2604.01206v1)。<!-- source-family:SF-2026-ARXIV-2604-01206 -->

若消费者的输出空间已经有限，还可绕开词表生成，直接为候选内容评分：让候选和决策位置经过原主干 contextualization，再复用预训练 attention 的 Q/K 作为匹配读出，不必另添随机初始化的 head。这仍需任务适配，不是原 checkpoint 天然会决策。[受限空间任务对照](https://arxiv.org/html/2610.22276v1)中，各种读出没有全任务赢家；数值区间和图像区域还需按声明的单位、codebook、溢出和原图坐标逐级细化，早层选错会排除真答案。训练把所有 stage 的 teacher-forced loss 放进一次 causal forward，不使部署时依赖自身选择的 stage 并行；crop 重编码、多点树展开、候选 context 与适配均计费。范围不完整、开放回答或质量回归时，原 AR、显式任务 head 与可靠 parser 仍合理，少 answer tokens 不认证通用空间能力或行动安全。<!-- source-family:SF-2026-ARXIV-2610-22276 -->

## 从 logits 到 token 还差一步

Decoder stack 的直接输出不是文字，也不是唯一 token，而是 `[B,T,V]` logits。生成时通常只使用每个 sequence 最后一个有效 position 的 logits：

```text
next_logits shape = [B,V]
```

[第20章](./20-sampling.md)会解释 greedy、temperature、top-k 和 top-p 怎样从这组 logits 选出实际 token。选出的 id 再通过 tokenizer decoder 转回 bytes/text；它同时作为下一次前向的输入，生成循环才真正闭合。

## 从训练前向到逐步生成

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

把这条训练与生成链放回任务选择，就能看见单一 stack 的收益。第一，目标统一。网页、代码、对话和文档都可以转成 token stream，使用同一个 next-token objective。

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

## 保留 Next-token 接口，内部状态可以怎样分工

至此，标准 Decoder-only 的训练与生成接口已经完整。接下来的问题不是这条基线是否过时，而是在特定压力下，哪些内部职责可以拆开：预测目标是否只能逐 token 定义，所有预测层是否都必须生产历史 KV，以及不同输入输出是否必须共用一条流。下面三种分支改变的是不同约束，不构成先后替代关系。

### 内部预测粒度可以不同于输出粒度

普通 Decoder-only 让表示、监督与生成都沿同一个 token 时钟推进。它的优势不只是结构简单：每个位置都有与最终输出
同构的密集监督，KV Cache、vocabulary projection 与流式 runtime 也共享明确的 token identity。只要单 token 粒度足以
形成需要的抽象，或实现成熟度、可审计性与稳定 latency 更重要，这仍是正确基线。

新的压力在于，跨多个 token 的表示在标准 next-token prediction 中只是间接产生，目标本身没有要求模型预测下一段
内部状态。一个可共存的层次化分支保留 token-level NTP 和最终 token 输出，同时把中间状态按固定 span 聚合，再在较慢的
concept 时钟上预测下一个 learned latent target：

```text
token states
→ span pooling + product-quantized concept vocabulary
→ autoregressive next-concept prediction
→ shift by one complete span and repeat to token resolution
→ token decoder → next token
```

关键不在把若干 token 改名为“概念”，而在明确两条时钟间的状态与因果 owner。checkpoint 必须共同版本化 span size、
codebook 与 segment layout、concept module、cross-module residual route 和多目标权重；runtime 还要区分 observed token、
由已完成 span 形成的 concept、predicted concept 与允许注入的 token position。预测状态只有在向后移动一个完整 span 后
才能反馈 decoder，否则 concept target 会把未来 token 泄漏给当前 next-token loss。训练时，codebook fitting、concept
prediction 与 NTP 也应分别声明 stop-gradient：谁更新 token encoder、谁只更新 codeword、谁保证最终 token 接口，不能
由一个含糊的“联合 loss”代替。

这条路径获得显式多 token 预测目标和较短的 concept sequence，却增加独立 autoregressive state，并需要防范 codebook
漂移或坍塌、固定边界错配、concept prediction error accumulation，以及跨模块状态物化、memory traffic 和小 kernel 开销。训练使用真实
concept history、推理递归使用预测 concept 时，还会出现第二层 teacher-forcing mismatch；causal shift 只能防止信息泄漏，
不能消除这种 drift。若只需要多个未来 token 的辅助监督，MTP 是不引入 learned codebook 的较小分支；若 concept-aware
kernel、长上下文验证或状态审计尚不成熟，应回退普通 NTP，而不是把双粒度结构当成 Decoder-only 的必然替代。

现有 exact-v1 作者证据在 OLMo-3/Dolma、约 8.94B 参数和 5.73T token 训练中证明这类联合路径可以规模化训练；
参数/计算对齐与渐进消融支持其训练-loss 增量不只是简单增加 Vanilla FLOPs。证据仍不证明 codeword 对应人类可解释概念，
也不证明其普遍优于 NTP/MTP：主训练没有 long-context 结果或独立重复 run，Stage 2 的下游增益明显缩小且部分任务回退，
analytical FLOPs 又没有计入状态物化、memory traffic 与 launch overhead。因此这里吸收的是**内部预测粒度可以与外部生成
粒度分离，但必须显式维护跨粒度 causality 与 state identity**，不是作者的通用性能排序。训练目标和 optimizer 的实现继续
交给第 28 章。<!-- source-family:SF-2026-ARXIV-2609-10715 -->

多个未来位置也可以共享随机输入来形成联合样本，而不只是各自预测一个边缘分布：先给k个独立uniform变量，再让因果noise-conditioned网络用前缀噪声共同决定一块k个token，避免显式枚举词表的k次方组合。[受限语言模型分支](https://arxiv.org/html/2606.10820v1#S3)先蒸馏单token映射，再由旧k模型两次rollout教2k；递归inverse-CDF只证明理想映射存在，不保证学到的单pass保持原AR分布。它用固定输出stride换更规整的batch，却把分布误差交给训练：k较大仍损质量，noise-conditioned低NLL或外部Gen-PPL较低都不等更好文本。Noise KV只属本轮，下一轮须重新处理已生成真实tokens，不能把临时noise当永久历史；多轮teacher/全模型训练、实际dense mask、重处理与完整服务回归都付费。证据仍是约百M模型与固定短completion，不签任意大模型/EOS/连续batching SLO；需要原分布保证时保留exact speculative verification，准备或质量不合时回到普通AR/MTP，不以固定k输出自动批准无损采样。<!-- source-family:SF-2026-ARXIV-2606-10820 -->

随机性也可以进入逐token decoder的内部，而不只用于最后抽样或一次提出多个未来token：在中间层为每个位置引入随机latent，将其映射后加入后半部读取的K/V，外部仍按普通因果顺序生成token。[一个受限的变分条件分支](https://arxiv.org/html/2510.17558v1#S3)让训练和prompt Prefill使用额外非因果encoder，为已知整段文本推断latent；继续生成时不再运行该encoder，而从预定prior采样。因此训练时能解释已知文本的posterior，与部署时可使用的prior不是同一个输入接口，新增随机状态也不自动对应可解释计划或正确推理。

为避免encoder把待预测文本直接藏进latent，可用重建目标与posterior/prior的KL代价共同约束，并以free-bits阈值决定何时开始处罚；阈值不是每条样本信息量的硬上界。容量太低可忽略latent，太高又可能出现训练cross-entropy更好、prior生成和下游表现反而崩坏。共享部分decoder减少了专属encoder计算，却不免额外block、离散采样/梯度近似、Prefill和完整训练费用；知识与多选任务仍有反退，较少新增参数不证明净服务加速或可替换CoT。Posterior/prior失配、质量或预算不合时，保留普通decoder与显式推理，不把不可见随机状态当作faithfulness或新能力的证书。

<!-- source-family:SF-2025-ARXIV-2510-17558 -->

### 历史状态生产与最终预测可以分开

前述多粒度分支改变了预测目标的粒度，另一条与 concept 时钟不同的分支仍保持逐 token 的因果输出，却将**历史 KV 的生产者**与**读取这些 KV 的预测容量**分开。普通深层 Decoder 的新增层也要重算全部 prompt token 的 KV；若目标是扩充模型能力而不同比例增加 Prefill，可以让较小的前段网络产出可复用 KV，再让新增的 token-local 后段只读前段 KV、负责更强的最终预测。新增后段不能写入未来位置要消费的 KV，否则“只运行前段处理长 prompt”的等价性就失效。训练时两段仍可联合更新，并非冻结旧 KV 数值；结构不变量是后段不改变 KV 的**生成路径**。它用更便宜的 bulk Prefill 换训练拓扑和推理引擎复杂度，也仍须为每个输出 token 支付完整后段计算。输入短、输出长、KV 共享实现困难或直接堆层更易维护时，标准 Decoder 继续成立。KITE/SST 的作者证据主要是训练损失、任务分数与按 Prefill/Decode 权重构造的推理成本 proxy，不是任意生产 workload 的端到端延迟证明。<!-- source-family:SF-2026-ARXIV-2609-27294 -->

### Multi-stream 把单一 Token Clock 降为接口选择

前两种分工仍可保留单一外部序列；当压力来自多路输入输出的等待时，才需要重新审视流之间的同步。单流 Decoder-only 让 thought、input 与 output 共用一个因果时钟，训练、KV 与流式协议最简单；并行工具输入、内部推理和可见输出会让单流阻塞暴露出来。multi-stream 分支为不同 stream 保持各自位置与可见性规则，再由显式 synchronization/merge point 交换状态；模型拥有 token proposal，runtime 持有 stream lifecycle、权限与外部 effect commit。

并行流可以减少等待并隔离可见输出，却引入跨流因果一致性、KV/layout、训练数据格式和 monitor blind spot；错误同步可能泄漏 private thought 或产生乱序 effect。普通聊天、工具少或审计优先时，单流协议仍是可靠基线。`arXiv:2605.12460v1` 的 §2–§7 与附录只验证作者的多流训练和实验，不证明 production scheduler 一定获益，也不替代 Agent 权限控制。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-12460 -->

因果生成顺序也不必等于最终display顺序：模型可逐步产生marker与cursor来打开/结束编辑，把新token插入、替换或删除已生成文本；inverse-edit扰动训练让它学习位置与修复，而非只学习下一个可见字。此时generation clock仍因果，parser维护display位置与可见性；删除仅从后续attention和最终输出隐藏旧span，不物理释放历史KV。K/V可存unrotated并按本次编辑位置旋转，缓存精确限定在这套Chain-of-Edits语义，不等重排文本后普通decoder重新前向。这个分支增加pointer/marker训练、segment/packing和仍保留的历史状态；[AutoIndexer v1](https://arxiv.org/html/2610.12545v1)的单corruption诊断中插入常不触发，exact repair远低于teacher-forced定位率，能力保持也只限matched-LoRA对照。质量、cursor或预算不稳定时，原追加式AR及外部显式编辑仍合理；显示修订不撤销已发送内容或外部effect。<!-- source-family:SF-2026-ARXIV-2610-12545 -->

## 从显式 CoT 到 Latent Reasoning：减少 Token 不等于消除状态

前面的分支重新安排了目标、KV 生产者或外部流，但没有要求取消中间可见 token。若瓶颈恰恰来自把每一步推理都写出来，才会进入另一个表示选择。显式 Chain-of-Thought 把中间步骤写成 token，优点是训练目标、停止条件、缓存和人工审计都复用语言模型接口；代价是每一步都要经过 vocabulary projection、采样和下一轮 Decode。将中间推理压缩成连续 latent state，可以少生成可见 token，却没有消除递归依赖：系统仍需决定 state representation、更新次数、termination、checkpoint identity 与失败恢复。

下面按中间状态的可见程度排列这些选择；箭头表示解释顺序，不表示技术谱系，也不表示每种方法都必须经过前一阶段：

```text
explicit token trace
→ compressed visible trace
→ recurrent hidden state
→ learned latent transition with teacher guidance
```

压缩可见轨迹还可以采用离散的计划前缀，而不取消其后的文本推理：先用学习到的 codec 将下一段计划压成有限 slots 的码本 ID，把这些 ID 映射为扩展词表中的特殊 token，再交替生成计划前缀与显式 CoT。这样减少的是计划表达，不是全部 reasoning token；码本、slot 数、特殊 token 映射与模型 checkpoint 必须作为同一接口发布，不能把旧模型里的 ID 直接换成新 codec 的意义。教师计划生成、codec 训练与模型适配都要计入预算，量化瓶颈或错误计划还会把偏差传给后续文本；码本可解码不证明实际推理忠实，少量计划 token 也不保证总 token 更少。需要独立 outcome verifier，并在任务、codec 或模型变化后重新校准；高风险审计、压缩失效或计划不可验证时，完整文本计划与显式推理仍是合理回退。<!-- source-family:SF-2026-ARXIV-2512-24014 -->

另一条分支不把连续状态一直留在主模型内部，而让主模型先产生少量 seed hidden states，经投影接口交给浅层自回归 decoder 展开为可见文本，再把这段文本接回主模型上下文继续生成。它压缩的是主模型需要承担的中间展开，不是取消文本、递归依赖或全部生成计算；main model、seed/projector、外部 decoder、触发位置及回填后的 KV/context identity 应作为同一发布接口验证。教师步骤与接口训练、decoder 调用和文本回填后的重新 Prefill 都要付费，按生成长度估出的主模型调用数不能当作实际 latency。固定 token 块还可能切断语义步骤，困难任务的质量反侧也说明可解码不等于忠实或正确推理；需以独立 outcome 验证决定是否采用，接口变化、粒度失配或恢复失败时回到完整显式 CoT。<!-- source-family:SF-2026-ARXIV-2602-04246 -->

后两个分支把成本从 token IO 移到 latent transition，并牺牲逐步可读性。训练期用完整 CoT、视觉编码或其他 teacher signal 约束 latent state，只能证明该 state 在指定任务与模型上可学习，不能证明它保留了原推理的全部语义或因果结构。推理期若只用代表 token 判断结束，还会新增 premature stop、state drift 与无法局部纠错的 failure mode。

连续更新也可显式锚在input embedding空间：冻结词嵌入，让小head从hidden预测相邻CoT嵌入的位移；先在原trace上提出替换，再用第二次前向消费连续状态，只对answer做token监督、对位移做训练。推理执行固定K次位移后回文字，因此K、head与冻结embedding共同定义接口。[受限GLR对照](https://arxiv.org/html/2606.02248v1#S4)把K加文字都计为步骤，在小预算有优势，大K会漂移，大预算下显式CoT又常更准；成功样本长度也不是全输入成本。两pass、teacher与全部latent前向均付费，异解码器的step数不证明墙钟加速或推理忠实；预算或质量失配时，缩短K、恢复显式CoT及独立outcome验证，不由可见文字变短签发净效率。<!-- source-family:SF-2026-ARXIV-2606-02248 -->

连续推理也可以先修一块状态，再追加下一块，而不每步只回灌一个向量：把显式步骤编码为有限latent slots，在当前block内双向去噪/反复改写，跨block只读已经提交的前缀，最终答案另走AR读出。[LaDiR的受限分支](https://arxiv.org/html/2510.04573v1#S3)因此允许局部修订，不允许任意回改旧block；可解码的中间句子也不证明它们因果决定最终答案。先用teacher-forced latent训练、再让答案监督穿过可微采样轨迹，是两阶段监督而非自动成为RL；训练已知块数与部署learned stop仍须分别验收。多样性引导改变同batch候选的耦合与law，原距离系数并非全域排斥、零带宽及solver接口未闭，不能照为稳定recipe；P@100有真解也不表示部署已有selector。Codec/双模型训练、solver反传、全部block/候选、答案与可选解释解码和独立验证均付费，math与Countdown的不同协议不拼成同工作点。Stop、修订质量或全预算不合时，保较短固定block、显式CoT与可信solver/verifier，不由少可见token或高重构率批准无损语义、faithfulness和通用最优。<!-- source-family:SF-2025-ARXIV-2510-04573 -->

连续推理也可以不固定走同一条 latent 链，而让每一步从条件密度采样，并另行预测是否停止；训练时再用答案质量与长度惩罚定义希望保留的轨迹分布。[一个受限的流平衡分支](https://arxiv.org/html/2606.16222v1#S3)利用完整 latent prefix 的唯一前驱，在多个子轨迹上拟合平衡残差，并配合答案监督与渐弱的 rationale prior；这不同于只最大化一条路径的回报，但有限训练并不保证精确后验、正确模式全保留或推理忠实。训练中的标准答案不能成为部署输入，微分 entropy 也不能直接证明语义多样性或存在通用最优阈值。若为中间 prefix 提前解码答案来估 flow，其评分、全部 rollout、prior 与子轨迹计算都付费；多条短链还须累计全部链的工作，不能只报单链长度。停止器、采样坐标、任务或净质量失配时，保留固定预算 latent、显式 CoT 和独立 outcome 验证，不由更短不可见轨迹批准更低总时延或可靠答案。

<!-- source-family:SF-2026-ARXIV-2606-16222 -->

连续状态直接回灌还多了一项输入接口合同：上一轮 decoder hidden state 与下一轮 input embedding 未必属于兼容的表示坐标。一个分支把 context-carried hidden 与当前词表分布的 top-p embedding 加权融合，再输入下一 latent transition；untied 输入/输出空间还可增加适配投影。它没有恢复逐步可见推理，也不能由 tied 与 untied 模型之间的差异唯一归因接口 mismatch，fusion、adapter、触发与停止规则必须和 checkpoint 一起验收。<!-- source-family:SF-2026-ARXIV-2602-10229 -->

[受限算术对照](https://arxiv.org/html/2602.10229v1)中，去掉 fusion 的8B配置弱于不用 latent，说明 latent 更新不是无条件改善；少量 PCA/attention probe 也不证明推理忠实或因果 collapse。课程、teacher 与接口训练增加成本，可见 tokens 变少不等同总 FLOPs 或完整生成延迟减少。回灌失配、latent 漂移或质量下降时，应恢复显式 token/CoT 或已验证的 embedding 接口，而不是仅增加不可观察的 transition 次数。

中间状态也可以不由decoder逐步生成再回灌：在question后预先放入固定special-token blocks，一次前向计算这段latent workspace，再自回归生成最终answer。为了让这些位置承担计算，先为各block附显式推理步骤readout，并用block-causal mask禁止后续memory读取这些teacher-forced文字；再切换为各block预测同一final answer，固定部署预算与最终readout。[RiM的受限机制](https://arxiv.org/html/2605.30343v1#S3)改变了中间计算的输入/监督接口，不证明人类式记忆、无限推理深度或latent faithfulness；一次Prefill仍支付额外位置的attention、KV和全部层计算。任一block答对的oracle覆盖不等固定最终block已实现，16次选点split也不是16次独立训练。全部trace制备、两阶段适配/优化器重置、mask实现、选点和answer生成均计费，单请求实测接近direct-answer不授并发SLO；任务、mask、预算或独立outcome不合时，保显式CoT、已验recurrent latent或直接回答，不因不可见步骤更少取消审计。<!-- source-family:SF-2026-ARXIV-2605-30343 -->

冻结主模型也不意味着中间输入状态必须固定：可以在问题后放一块latent embedding，把它作为每个请求自己的搜索变量，反复扰动候选、以冻结模型的输出分数评价，再将选中的状态交给最终文本decoder。[这条受限输入状态优化分支](https://arxiv.org/html/2510.04182v1#S3)不同于学习通用latent transition，也不是对答案token policy更新模型权重；候选状态、评分位置/函数、搜索分布及最终readout须分开验收。Top-k负log概率的均值只是这些概率几何均值的变换，不能不看符号和k就叫“更高确定性”，更不认证正确答案；在causal模型中，若评分仍读附加latent之前的prompt位置，还根本不能感知该latent，故位置索引必须实际闭合后才可复用优化recipe。单probe随机更新、最佳分数选态与最后一步也不是同一提交规则，短步的一阶方向分析不保证有限步或有噪搜索改善结果。每题所有prompt/latent前向、词表读出、状态历史、调参选择与最终生成均计费，少可见token不表示较低总时延；原有限任务亦有质量反退。评分资格、位置、预算或独立outcome不合时，保未调latent、普通显式CoT与外部verifier，不由自评分更大、状态不可见或权重冻结批准正确性、推理忠实或通用省费。<!-- source-family:SF-2025-ARXIV-2510-04182 -->

因此显式 CoT 在高风险审计、工具副作用和需要逐步验证时仍然合理；latent reasoning 更适合中间步骤冗长、可由独立 outcome verifier 检查且 token latency 占主导的受控任务。二者是不同 observability / efficiency contract，而不是后一种对前一种的线性替代。

显式轨迹还可以选择有限的操作语义粒度，而不必记录任意自由文本：由解释器模板产生局部状态转移，并对稀有stack/control模式作专项采样，让模型学习可检查的局部规则。外部runtime在call/return时清理非活跃帧，可使在线输入更接近活跃工作空间而非累计全部轨迹；帧身份、局部输入和清理规则必须明确，模型不拥有随意删除执行状态的权限。

有限token-level正确率不能替代自治full-run成功，语言的计算完备性也不证明有限精度、有限窗口模型对任意程序可靠。受限MicroPy/PENCIL证据依赖外部scaffold、有限primitive及合成程序，模板和采样都增加数据/runtime成本；语义超范围、帧管理不可信或需要完整审计时，保留确定性解释器、完整显式trace与独立执行验证，不将scaffold称为新decoder架构。 [原文必要机制与限制](https://arxiv.org/html/2604.25166v1)。
<!-- source-family:SF-2026-ARXIV-2604-25166 -->

### 少生成 Token 之前，先验证 Latent Steps 是否必要

在选择 latent 路径前，还要检查它是否真的承担中间计算。将多个 token embedding 按概率混合，首先表示的是词表不确定性；标点或无关词的混合不等于同时搜索多条语义推理路径。可在固定模型和任务下移除 latent steps、用离散 token 替换指定 soft step，并与行为和实体级 readout 对照：如果不经过这些步骤仍能正确回答，增加了内部状态也未证明模型依赖它完成推理。Readout 只能观察其可读方向，不能单凭 entropy 或线性投影宣称内部没有其他算法。

这一必要性检查也有条件边界。[受控研究](https://arxiv.org/html/2604.06374v1)中，fine-tuned GPT-2 的 ProsQA 表现从六个 latent steps 的 99.0% 到移除 steps 的 96.6%，提示许多答案可由 shortcut 得到；浅层从零训练模型却明显依赖 latent steps，更深模型的这种优势又缩小。后者采用不同的逐 hop 监督，不能将差异全部因果归于 pretraining，也不能据此否定所有 recurrent 或 RL-trained latent reasoning。因而 latent state 的采用需要任务结果、必要性干预和实际成本共同支持；仅输出少、soft-token entropy 高或可投影出正确实体都不足以替代这些证据。<!-- source-family:SF-2026-ARXIV-2604-06374 -->

即使 latent steps 不能直接移除，也还需核对中间状态是否沿预期 rollout 传播。共享 teacher/student 的 answer-boundary 监督可能只学到局部 bridge，再由最终输入直接完成 readout；答案正确不说明每一步都承担对应计算。冻结的 state readout 与 clean/corrupted activation patch 应共同定位路径，并保留仅正确样本、读出函数和任务条件；probe 不可读不等于不存在其他编码。<!-- source-family:SF-2026-ARXIV-2602-00449 -->

压缩路径是否可行也取决于任务状态转移。受控模算术中，复合模的非双射映射可以收缩历史状态差异，允许 late-state 瓶颈；非零乘子下的素数模双射没有同样的收缩条件。有压缩可能不等于训练必然采用该路径，这个解释也不是自然语言推理定律。更换监督边界或任务后需重做路径干预，额外 probe 与 patching 都增加验证成本；无法验证时，保留显式 trace 与独立执行，不以 latent slots 数作为 faithfulness 保证。

### 压缩置信度决定表示，不决定结果提交

固定使用完整显式轨迹或固定使用 latent state，是这一设计空间的两个端点。中间分支可以先预测下一段 reasoning span 的冗余度与压缩置信度，只把高置信、低信息增量的 span 编码为 latent representation，同时让 precision-critical span 继续走显式 CoT。这里的 gate 决定的是**下一段采用哪种 reasoning representation**，不是在生成后由 target verifier 接受或回滚 proposal；因此它属于 Decoder-only 的表示与状态演进，而不是 speculative decoding 的 commit protocol。

这种选择性表示减少了部分可见 token，却新增 gate calibration、显式/latent 双路径训练和 latent error propagation。置信度失准或 distribution shift 会把本应显式保留的步骤过早压缩；高风险、需要逐步审计或 gate 未校准时，完整显式 CoT 仍是正确 fallback。现有 exact-v1 证据只覆盖论文披露的数学任务、模型、span anticipation、三阶段训练与消融，不证明压缩无损，也不证明开放域 reasoning 能获得相同结果。<!-- source-family:SF-2026-ARXIV-2605-25745 -->

决定进入 latent 后，还可继续选择哪一条内部计算路径：在下一动作词表中加入少量 operator 标记，与可见 token 竞争；选中标记时，让共享 synthesizer 读取当前 context 与该类型的 query，再经专属 projection 生成 latent 位置并回灌。[受限 typed-operator 对照](https://arxiv.org/html/2606.16360v1#S3)用轨迹边界启发式训练这些路径，再学习调用选择；交换或共享路径的退步支持保留其身份，却不证明‘规划、状态、过程’已经成为可形式验证的语义。按成功轨迹的超预算调用施罚只是训练偏好，不是运行时硬上限；在调用位置重用整轨迹 advantage，也不是该次调用独立贡献的真值。Query、projection、调用位置与预算应随 checkpoint 绑定，全部 synthesis、latent KV 与后继生成都计费。单请求较 CoT 快并不保证比其他策略快，省可见 token 也不授全链 SLO；角色、预算或独立答案质量失配时，保留单一 latent 路径、固定预算或显式 CoT，不能让 operator 名称替审计和结果验证。

<!-- source-family:SF-2026-ARXIV-2606-16360 -->

### 重复主干时，工作状态与串行深度可以分别设计

让同一主干反复更新hidden state，最简单也最省额外接口；但当前计算与跨轮保留信息必须挤在同一份表示里。一个替代是在直接主干路径之外，为当前token维护额外的门控工作状态：按本轮输出决定保留旧状态和写入投影的比例，再把读出的状态加回下一轮输入。[StateLoop的受限对照](https://arxiv.org/html/2610.35544v1#S5)将每轮重置、持续保留及不同更新单元分开，支持持续保留的局部增量，却也显示重置支路本身已有收益，不能将全部提升归于记忆。该状态沿loop轴更新，不是自动替代历史token的KV；可选token混合器还会增加自己的缓存。额外门控、投影、训练和执行都有成本，状态或净收益未验时，普通直接回灌仍是清楚的基线。<!-- source-family:SF-2026-ARXIV-2610-35544 -->

保存状态之外，还可以缩短等待状态的串行路径：先用轻量预测器估计同一前缀的后续loop输入，把多个深度放入并行batch，再用已完成的较早状态修正暂算输出。[LoopFold](https://arxiv.org/html/2610.35556v1#S3)联合训练主干与预测/校正器，目标是有限stage下的预测质量，不是精确复原原顺序轨迹。这用额外并行计算和KV换更短串行深度；“目标深度相同”“训练FLOPs相同”和“延迟相近”是不同对照，低计算预算仍可能由普通loop领先，共享KV也可能省容量却变慢。并行余量不足、模型未经这种路径训练或要求原函数保持时，保留顺序loop，不能把预测状态当作已经完成的精确计算。<!-- source-family:SF-2026-ARXIV-2610-35556 -->

### 状态进入循环后，监督与停止必须重新定义

选择表示只回答了状态存在哪里，还没有回答循环中的哪些状态受到约束、何时可以停止。Decoder-only 的状态不仅是可见 token。Looped 或 latent reasoning 把部分推理迁入 recurrent hidden state 后，dense per-loop loss 只能约束 readout 可见方向；normalization 隐藏的尺度仍可能在 residual recurrence 中携带信息。在 RMSNorm/LayerNorm 隐藏 radial scale 的这一条件下，需要让尺度对 loss 可见，或从 recurrence 中移除该尺度自由度。训练 contract 因而要明确哪些 latent state 对 loss 可见、何时提交以及如何停止。

这正是减少可见 token 后增加不可观测状态、循环稳定性和调试成本的具体来源。latent state 无法校准或行为审计失败时，应回到显式 CoT、固定 loop 或普通 autoregressive decode；减少 token 不等于删除推理状态。

循环边界的normalisation还须与block内部Pre-Norm及最终readout分开。对已训练checkpoint，只在推理时移除边界操作，会改变后续block和读出接收的状态分布；即使最后一步归一与读出代码不变，也不能沿用旧兼容性。[受限loop对照](https://arxiv.org/html/2610.31943v1#S4)中，删除已训边界操作的失败与从头不使用它的较好深度外推可以同时成立，不能据前者证明该操作是所有loop架构的必需组件，也不能据后者直接修改任意发布模型。

验收应分别看状态尺度、有效输出格式与正确行为；尺度未爆炸仍可能失去答案，较低readout熵也可能只是输出一个稳定错误。只重训head部分恢复，不说明受损的全部计算只在head；末block与readout共同适配又另付训练费。比较推理深度时还要按各自训练loop数r0报告K/r0，并配平实际layer applications，固定K可能同时混入不同overshoot与compute。有限小模型的非显著差异不证等价，状态增长带来阻尼也只是待验解释；额外重训、不同K/seed和质量回归都计费，迁移或停止证据不足时保留原拓扑/训练预算、固定loop与显式验证，不由norm曲线或多循环直接认证稳定净收益。
<!-- source-family:SF-2026-ARXIV-2610-31943 -->

逐 token 停止还必须区分“这个位置不再更新”与“其他位置不再读取它”。一种自适应循环把 halting mask 设为单调：一旦停止，该位置不再更新下一轮输入 embedding，并保留其前一轮 K/V，仍允许活跃位置读取；不能为了省计算把它从因果上下文删除，也不能由 embedding 停止更新推断实现中的所有 hidden readout 都已冻结。训练也需暴露同一种状态语义，先让 gate 学会可用的更新，再逐渐引入提前停止压力；否则 gate 可能退化为全部继续或全部过早停止。停止拥有的是迭代预算，不是正确性证明或输出提交权。

这用更少状态更新交换 gate、稀疏执行和训练校准成本，FLOPs 减少未必成为 wall-clock 收益。[AdaPonderLM 的受限对照](https://arxiv.org/html/2603.01914v1)显示停止比例与正则强度会改变质量，较小模型的部分结果也低于固定循环；继续预训练的比较还需区分额外训练 token，不能把所有差异归于 gate。固定预算循环在停止器不稳、稀疏工作难以执行或审计要求一致时仍然成立；推理引擎如何跳过更新而不破坏 cache 生命周期，交给 Part V。<!-- source-family:SF-2026-ARXIV-2603-01914 -->

停止头给出的分布还不是执行计划。设它预测在第`t`轮停止的概率为`p_t`，期望轮数`E[N]=Σ t·p_t`只是分布均值；按累计概率阈值退出得到的是另一项实际轮数`N_exit`，少量留在最后一轮的概率就可能让执行仍到上限。同批请求等待最深token时，付费轮数又接近`max_i N_exit,i`而非逐token平均。因此评估应同时保留预测均值、声明退出规则下的实际轮数与指定batch的付费轮数，并在相同可运行深度/质量基线下比较，而不以头的低均值签发加速。

训练监督也要对齐真正的退出读出：只对全部轮次state的加权混合评分，不保证某一轮或提前截短混合能独立预测；按停止概率给每轮readout评分，又可能让头很少选择的早轮缺少有效训练，需要另验早停prior与目标的共同作用。[有限从头预训练对照](https://arxiv.org/html/2610.32246v1#S6)支持这一区分，但更浅训练的固定预算基线会缩小优势，未测的depth-wise调度也不能被宣布无效。额外监督、逐轮readout、gate、重排与cache处理都有费用；退出质量或真实吞吐不合算时，保留固定loop、匹配深度的专门模型与原上下文读取，而非把少量理论计算直接等同服务净收益。
<!-- source-family:SF-2026-ARXIV-2610-32246 -->

增加推理循环数也不自动获得深度泛化：共享 block 必须先在训练中学会反复使用其状态更新。在受控的合成多跳实验中，训练 recurrence 的覆盖范围影响增加推理循环后的收益；不同课程可能暴露不同 hop 深度，因此不能把它们的最大外推深度直接归因于动态循环。即使固定同一训练数据，更多循环也可能在已有正确状态后继续漂移，形成 overthinking，而不是单调逼近答案。普通固定深度 decoder 与固定 loop 在任务、预算或停止信号不稳定时仍是合理基线。

停止条件须分开“输出不再变化”和“已有可提交结果”。相邻循环分布的 KL 很小，可能只是停在高熵的含糊分布；一个受限替代是同时要求 KL 小与输出熵低，再决定是否停止。它增加阈值校准和逐轮 readout 成本，也不能阻止稳定、低熵的错误；熵是集中度 sensor，不是真值。作者用于解释 overthinking 的正确 token logit margin 依赖答案标签，不能直接当作线上可用停止器。该分支目前由从头训练的合成关系任务支持，不能外推到任意预训练 LLM；超出已验训练/推理循环范围时，仍应保留循环上限、固定预算与显式验证。<!-- source-family:SF-2026-ARXIV-2604-07822 -->

在某轮已能读出正确答案，也不表示该hidden state已能停止更新并供后续位置复用。可以把三件事分开干预：在指定loop检查计算结果，继续运行观察答案是否保持，再从该轮冻结状态、让依赖它的后续计算继续执行。缓存一个已验证答案与冻结生成它的全部hidden state不同；后者可能同时携带尚未完成的顺序、时间或交互信息。只用最后位置/固定exit监督而得到的保持性，也不代表随机位置或更长执行预算下同样稳定。

[有限Mealy-machine与递归maze诊断](https://arxiv.org/html/2610.19768v1)中，正确读出、延后保持与freeze复用确有分离；成对swap能支持所测位置对后续计算的counterfactual sufficiency，却不证明唯一符号编码，freeze失败亦不证明信息已经丢失。多轮诊断、状态保存与干预都增加费用，部分forward匹配不等同完整反传/FLOPs匹配；用clean未来最后变化定义的到达时间是离线oracle，不能直接充当线上停止器。没有可核验复用边界时，保留统一执行预算、原recurrent更新和独立任务验证，不把延后若干loop当跨任务通用修复配方。<!-- source-family:SF-2026-ARXIV-2610-19768 -->

### 循环中的读取位置与表示更新也不必同时冻结

即使监督与停止有了明确约束，每一轮是否都要重新查找全部历史，仍是独立的成本问题。循环深度还带来另一种可分离的状态：模型可能较早确定“去哪里读”，但隐藏表示仍需多轮更新才能决定“怎样使用”。在所测 recurrent decoder 中，早期全局 Attention 可发现 query 的 block-level working set；后续循环仅复用这些位置，仍用当轮 Query/Key/Value 重新计算集合内权重与表示，而不是冻结 attention matrix 或停止推理。这样把反复全局路由的计算换成 support 选择误差、稀疏 kernel 和 discovery 深度调参；若 support 随任务继续变化，必须延长全局发现或回退全 Attention。作者证明依赖收敛与非退化间隔假设，实验只支持所测 recurrent backbone/任务的 attention 工作量与质量取舍，不是普通单遍 decoder 的通用加速。具体执行优化交给推理章节。<!-- source-family:SF-2026-ARXIV-2609-27373 -->

## 更多内部状态，不等于无条件扩大表达能力

上述分支都增加了对状态的选择，但不能只按状态数量、循环次数或架构图推断能力。还必须分别检查实现能保留什么区别，以及固定模型的输出空间允许哪些结果。

### 有限精度决定实际状态语义

实数域公式常把 causal Attention 看成任意精确的加权聚合，但真实 decoder 逐位置更新的是有限精度内部状态；accumulator、舍入、求值顺序和层间组合都会改变它能稳定区分的历史。因而“架构图相同”并不保证同一表达上界，kernel 重排或精度变化也可能改变可实现的 memory semantics。

组合理论能在明确 arithmetic、mask、position 与 wiring 假设下连接 attention type 和可识别语言，但它不等于对普通 LLM 完整能力的刻画，也没有替代训练和下游实验。长期结论是：讨论 decoder expressivity 或等价实现时，必须同时声明抽象算子与执行语义；在无法证明有限精度等价时，应保留 reference path 和行为回归，而不是只凭代数重写批准替换。

<!-- source-family:SF-2026-ARXIV-2607-26988 -->

### 固定模型还受到输出可达性的约束

<!-- semantic-body-binding:SF-2026-ARXIV-2605-22223:start -->
有限精度之外还存在另一层上界：固定架构并不保证任意输出序列都可由某个 prompt 触达。prompt 只选择输入，decoder 的 embedding 与 decision regions 才决定输出 support；因此增加 context、Decode 时间或采样预算，可能在既有可达区域里搜索得更充分，却不会自动创造新的可达区域。在一组明确的 bounded-embedding、decision-cell 与 packing 假设下，可达序列的最大长度只随 prompt 长度线性增长，超过模型相关阈值后，可达序列占全部序列的比例会指数下降。

这是一条架构条件下的诊断上界，不是对某个自然语言答案“模型必然无法生成”的判决，也不证明训练不能改变模型相关常数。工程上应由 Evaluation owner 用 copying、cramming 与长度切片实验估计实际 cliff，并把 tokenizer、decoder、precision 与 decoding policy 固定为同一评测身份。形式假设或常数无法核实时，直接行为测试仍是 fallback；理论结果只能提出风险假设，不能替代部署 checkpoint 的验证。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-22223:end -->

改变执行协议则是在讨论另一台机器，而非反驳固定接口的输出上界。[条件 simulation 研究](https://arxiv.org/html/2601.08061v1)令外部 operational string 持续增长，每轮从其开头消费窗口、把生成的一或两符号追加末尾，并按特殊 halt 控制规则推进；只有 injective codebook 使全部1857条 universal Lag rules 都被确定、精确执行，才推出该协议下的通用计算。普通有限窗口 next-token Decode、某次平均任务正确率或任意自然语言提示都没有自动满足这些条件。

随机网络冻结也不等于整个 pipeline 无训练：该分支训练 encoder/decoder，并以 learned codebook 上的最近邻离散输出连接规则；外部串增长、编码、逐规则验收与运行时间均需预算。有限初始化的成功实验不保证任意随机网络或训练搜索成功，条件 simulation 更不保证可学性、容易编程或实际效率。协议、精度或规则一致性未验时，保留标准 next-token 接口、有限状态/输出边界和直接任务测试，不能由形式通用性签发部署能力。<!-- source-family:SF-2026-ARXIV-2601-08061 -->

## 回到生成循环：状态复用与选择 Token 分别交给谁

无论是否采用上述受限分支，标准 next-token 接口仍是理解后续推理系统的基线。把本章结构重新接回第 11～17 章，可以同时看到持久状态和当前决策两条路径：

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

本章把第 11～17 章组成完整 causal language model。一次 Decode step 同时产生两类结果：供未来步骤复用的逐层 K/V，以及供当前步骤选 token 的 logits。[第19章](./19-kv-cache.md)沿状态分支解释 KV Cache，[第20章](./20-sampling.md)沿决策分支解释 Sampling，二者共同闭合自回归循环。

[第24章](../part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)把 causal autoregressive factorization 放进更广的生成范式树。Diffusion、Masked/Block Diffusion 可以并行更新多个 provisional positions，却会增加 correction、cache invalidation 与 commit protocol；它们是不同生成 contract，不意味着 Decoder-only 被线性替代。

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
11. 为什么 causal mask 是 Attention 路径的声明，而 prefix invariance 才是整个 Decoder block 的行为不变量？

## 小结

Decoder-only 用 causal factorization、Attention 路径上的 causal mask 与 next-token objective，把一个 Transformer stack 变成通用条件生成模型；完整 stack 还必须满足 prefix invariance，架构声明才真正成为可验证的因果行为。训练时 shifted targets 提供所有位置的监督，推理时模型必须逐步生成并追加 token。

这种统一接口简化了数据与任务表达，也把序列状态、生成串行性、Sampling 和评估复杂度带入系统。它是现代 LLM 的重要架构选择，而不是所有任务的唯一最优解。内部 concept、multi-stream 和 latent recurrence 分别改动不同状态职责，收益必须与因果边界、监督、停止和可观测性一起判断。

下一章先回到最普通的生成循环：每追加一个 token，历史位置的 K/V 是否还需要重新计算？[第19章](./19-kv-cache.md)会从因果前缀不变性推导哪些状态可以缓存、为何不缓存历史 Query，以及省下计算后新增的显存与生命周期成本。

## Review notes

- `SF-2026-ARXIV-2606-14943` — Daily2026-06-17补Jun16；exact-v1 §3/4.1–4.3/5/A采样范围必要，原2+2+2=6，仅position-aware条件副本/原LTR与多层间接泄漏差额深入。保singlepass评价非生成、条件支持与跨queryjoint非保证、PPL/infilling反侧与GT边界MAUVE/全费，不授无损或任意condition最优；未核全表/图像素/代码/复现。root§102有限必要/actualowner/完整三件PRE通过，作者已真实SAVE并完整自读，root§105唯一实际完整POST通过，窄位生效释放，不预DAY。

- `SF-2026-ARXIV-2610-35544` / `SF-2026-ARXIV-2610-35556` — Daily2026-10-28，精确v1；分别§3–5状态/reset/GRU控制及§3–5预测校正/配平/消融/限制。5与6分，实际状态/执行路径差额深入；只采用独立工作状态及并行预测校正两替代分支，保训练、额外状态/FLOPs/KV、低预算反侧与非顺序函数等价。不报告普遍加速，未复现实验；独核见本日REVIEW。

- `SF-2025-ARXIV-2510-04573` — Arendt，Daily2025-10-08补Oct07；原2+2+3=7，直接采用root R210 exact-v1 S2.1–2/S3–4/A3–6/T1–8必要，不第二Methods。只block内latent修订/跨block因果提交及最终answer分责；保Stage2可微监督非RL、训练GT块数/learned stop、Eq6距离大时吸引/零带宽/velocity接口未闭、math与Countdown协议分开、teacherforcing重构非因果faithful、P100需selector/实际verifier与所有费用。不采完整guidance recipe/独立样本/全任务净优，未核代码/图像素或训练生成复现；PRE/SAVE/POST仅本日canonical真实后到层。 R228唯一actualPOST/I56已通过，指定窄位生效释放；本尾仅正常同步本人既成态，不改正文/他态或授DAY。

- `SF-2025-ARXIV-2510-04182` — Arendt，Daily2025-10-08补Oct07；原2+2+3=7，作者A155 exact-v1 S3–5/T1–6/AppA–C必要，root R164关键原reward/索引/表/proof独核后一次采用。仅逐题input latent搜索与冻结LLM/评分producer/最终readout分责；保Eq4负log/k/全序列Pi vsN+i未闭、Gaussian平滑目标/单probe/衰减sigma、beststate/laststate区别、B1仅小步一阶与B2未证明实际随机迭代、T1/T6反退/T3AIME24更慢/T5配置差、task调参人口及全部前向/搜索/生成费。不补sign/索引/可运行recipe，不授新能力、通用更确定/正确或净速；未核曲线像素/代码/日志/复现，PRE/SAVE/POST仅本日canonical真实后到层。 root R168唯一actualPOST通过，指定正文/本人注窄位释放；本尾仅同步既成态，不重正文/研究/POST或预DAY。

- `SF-2026-ARXIV-2606-10820` — Daily2026-06-11补Jun10；[exact-v1](https://arxiv.org/html/2606.10820v1)§3/4/C1/D1D2，2+1+3=6。只noise jointmapping/1→2→4准备与noise临时KV，保百M/短context、质量反侧、不同teacher/NLL条件、O(k²)真实训练与FP16→FP32额外准备、NFE非全费，不采用无损/通用serving或MDLM一般lowerbound。未核代码/复现；reader§26必要/actualowner/唯一PRE通过，root窄授后作者真实保存，reader§28唯一实际POST通过，窄位释放；不预签日级。

- `SF-2026-ARXIV-2606-02248`：2+1+2=5；exact-v1 §3–4必要；冻结embedding位移/两pass与K+text预算，保大K漂移/大预算CoT反超、成功人口和异decoder不可比wallclock。 未核代码或复现。独立必要Source/owner/逐字PRE通过，root实际保存；非writer `jun03_next_reader` 已真实读取完整新增、完整直接两侧与本人注，唯一actualPOST通过（本日SUP_NEXT_REVIEW_20261024，末项R20）；本句只同步既成结果，不授完整DAY。

- `SF-2025-GOOGLE-T5GEMMA-2` — Daily `2025-12-19`；[官方release](https://blog.google/innovation-and-ai/technology/developers-tools/t5gemma-2/) `datePublished=2025-12-18T18:30:00Z`，当前修改于2026-03-19，不授论文首次公开。必要证据为 [2512.14856v1](https://arxiv.org/html/2512.14856v1) §2–3、Table1–5；采用全embedding共享、K/V共享投影与joint normalization的架构分支，以及局部质量取舍。Table1无重复/误差条，不授严格非劣性；最终约2T UL2配方与局部400B消融分开，跨模型数据/预算不完全受控，不采用普遍质量优势、throughput或能耗保证。root实际核原文、原Encoder-decoder段、Ch17/19邻接后替换该局部；非写入者Feynman实际对读exact v1 §2–3/Table1与已核Table2–5、新两段及Encoder-only/Decoder-only前后衔接、Ch17/19开篇，2026-10-02T20:07:56+08:00 POST通过；不授日级完成，未复现实验。

- `SF-2026-ARXIV-2604-07822`（Status: Experimental）：[exact-v1](https://arxiv.org/html/2604.07822v1) §4、§6.1–6.3 与 Limitations。采用训练 recurrence/推理 recurrence/课程 hop 范围分账，以及 KL-only premature halt 的受限反例；同12-hop数据下动态与R=8都外推到19-hop，不写动态循环普遍胜出。正确 token margin仅为有标签诊断，KL+entropy不保证真值；6分因具体知识缺口深入，root 已独立核必要原文与实际正文，通过，未复现实验。

- `SF-2026-ARXIV-2604-06374`（Status: Experimental）：[exact-v1](https://arxiv.org/html/2604.06374v1) §3–7 支持 soft-token 混合、latent-step 必要性与容量/监督条件的受限对照；不把 logit-lens 观察当完整内部算法证明。必要原文、实际正文及相邻衔接的非作者复核通过（root），不代表整日报验收。

本轮联章 Review 对齐了 causal factorization、tensor position 与 shifted target 的索引，并把第 19 章的状态分支和第 20 章的决策分支放回同一个 Decode step。本章仍以架构、mask、shifted targets 和 logits contract 为主线；内部状态分支只保留与这些接口有关的机制及已有证据边界。Pretraining/SFT 数据与 loss 配置属于 Part IV，Prefill/Decode 的硬件执行与调度属于 Part V。

Primary-source 校验入口：

- Alec Radford et al., "Improving Language Understanding by Generative Pre-Training", 2018: https://cdn.openai.com/research-covers/language-unsupervised/language_understanding_paper.pdf
- Jacob Devlin et al., "BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding", 2018: https://arxiv.org/abs/1810.04805
- Colin Raffel et al., "Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer", 2019: https://arxiv.org/abs/1910.10683
- ReGuLaR（teacher-guided variational latent reasoning；Status: Experimental）: https://arxiv.org/abs/2601.23184
- NCP-ArchPreview（joint token/concept autoregression；Status: Experimental；exact-v1 PDF）: https://arxiv.org/pdf/2609.10715v1

### Daily Books delta trace（2026-06—08）

<!-- daily-books-trace:SF-2026-ARXIV-2606-24898:start -->
- `SF-2026-ARXIV-2606-24898` — Daily `2026-06-13`；primary `arXiv:2606.24898v1`；Books review `books-review:SF-2026-ARXIV-2606-24898`。

  **已吸收的语义增量：** Looped LM 的dense per-loop cross-entropy只控制readout可见变量；RMSNorm/LayerNorm隐藏radial scale时，recurrent residual仍携带scale，必须让scale对loss可见或从recurrence移除。
<!-- daily-books-trace:SF-2026-ARXIV-2606-24898:end -->

- `SF-2026-ARXIV-2602-00449` — Daily `2026-02-04`；[exact-v1](https://arxiv.org/html/2602.00449v1) §3–7及Appendices C/D/E/F/G/H/I。6分设计反证深入，只采用CODI合成模算术中的bridge/readout bypass与任务收缩条件；3-layer/2-head GPT2-style、clean-correct过滤、linear probes/activation patch及teacher-loss和distillation消融不授自然语言定律或通用训练因果。素数模解释限定非零乘子，probe不可读不证明无其他编码，未复现实验。root必要原源与owner写前复核通过，root实际正文及前后交接写后复核通过，日级Gate通过。

- `SF-2026-ARXIV-2512-24014` — Daily `2026-01-02`；[iCLP exact-v1](https://arxiv.org/html/2512.24014v1) §4.2–4.3、§5及Tables1–3。6分具体接口缺口深入，仅采用离散LP计划前缀与显式CoT交替、codec/词表/checkpoint耦合及teacher训练成本；六slots与2048码本是作者设置，不授faithfulness或普遍总token减少，TheoremQA正文370.2与表270.2冲突数字不采用。未运行实现或复现实验；root必要原源与具体owner写前通过，root实际正文279、266–295邻接及411末注非作者写后复核通过，日级Gate待验。

- `SF-2026-ARXIV-2602-04246` — Daily `2026-02-06`；[CoLT exact-v1](https://arxiv.org/html/2602.04246v1) §3–6。2+2+2=6，具体接口缺口深入，仅采用 seed→外部自回归decoder→可见文本回入main 的替代分支。教师步骤/decoder训练、初始化与文本回填成本、固定token块粒度及MATH困难任务反侧就近保留；主模型调用估算不是实测latency，Eq4记号与全部生成loop可微不采用，可读不授faithfulness。root必要原源及owner写前通过；root实际正文283、279前置离散plan与后续latent分支/总结及419末注POST通过，本日日级Gate未验，未运行代码或复现实验。

- `SF-2026-ARXIV-2601-08061` — Daily `2026-01-15`；[random AR operational-string simulation exact-v1](https://arxiv.org/html/2601.08061v1) §3–7、Theorem1/Corollary3及Methods E。2+2+2=6，conditional external-string machine接口差额深入；不反驳固定接口可达性，不把冻结随机网络等同全pipeline无训练，不授任意随机网络/自然prompt/效率。未运行代码或复现实验；root实际必要原源/现owner写前核通过，实际正文与前后邻接非作者POST通过；日级Gate未授。

- `SF-2026-ARXIV-2602-10229` — Daily `2026-02-13`；[exact-v1](https://arxiv.org/html/2602.10229v1)，必要方法/关键评价/直接反侧见本日 V3_EVIDENCE_SIX；2+1+2=5，具体owner差额深入。只采用hidden→input embedding融合接口/adapter与质量反退，非untied因果、非faithfulness或少总compute。root实际必要原源与current owner/邻接PRE通过；root实际正文、前后邻接与末注非作者POST通过，窄锁释放，日级未授；未运行代码或复现实验。

- `SF-2026-ARXIV-2603-17512` — [XBridge exact-v1](https://arxiv.org/html/2603.17512v1)§3–5/Limitations、A1–4及必要Tables1/2/6–10；仅冻结LM与多语encoderdecoder的两侧映射/英语中间序列/输出K/V接口及分验边界。relaxedOT非语义等价、lambda/表口径、局部反退/推理变慢与全费用限制保留；未核代码/复现，不授全语言保真或生产性能。

- `SF-2026-ARXIV-2604-01206` — Daily2026-04-03；[exact-v1](https://arxiv.org/html/2604.01206v1)§3.1–3.3/4.1/C3.3–3.6，2+1+2=5，仅single-query scalar readout与next-token/targetscale接口分责；保parameter-matched/STS tie、ranking≠RMSE和冻结前向/训练/候选费用，不授数值真值或全任务/SLO，未核实现/复现。

- `SF-2026-ARXIV-2610-12545` — Daily2026-10-13；[AutoIndexer exact-v1](https://arxiv.org/html/2610.12545v1)§2–3/5/AppA.1–3及必要protocol，2+2+2=6，causal generation/display编辑具体gap深入。CoE缓存不授普通fresh-forward等价，deletedspan不物理freeKV，pointer/marker/inverseedit训练及有限exactrepair/matchedLoRA反侧保留。root必要Source/实际owner/邻接及PRE独核通过，today_institutions已按窄锁写入，作者顺读正文/完整局部邻接与本注；root已实际读正文/完整局部邻接和本注非writer POST通过，六owner窄锁释放；不授DAY。未核代码、复现或生产SLO。

- `SF-2026-ARXIV-2610-19768` — Daily2026-10-16窗10-15；[exact-v1](https://arxiv.org/html/2610.19768v1)必要Source/实际命题与反侧见本日LIVE A9/R16及root具名独核层，2+1+3=6，具体owner差额深入。只采本两段的测量/状态接口，不授因果真值、普遍质量/加速或部署停止保证，全部费用、直接反侧与旧路径近正文。reader A9/R20逐字PRE通过，root授指定两段与本人注窄lease；作者已保存并实际读回，独立reader R21实际正文、完整邻接与本人注POST通过，root接纳并释放指定窄lease；作者仅行政同步本注并实际读回，不授DAY。未核代码/复现。

- `SF-2026-ARXIV-2610-22276` — Daily2026-10-17窗10-16；[exact-v1](https://arxiv.org/html/2610.22276v1) §3–4/E.1–2必要，2+2+2=6。只采contextual candidate/nativeQK与分层controller消费，保全量语言适配、head对照无全胜、pilot非release/多点反侧和crop/tree全费，不授全任务单forward或行动安全。root已实际Source/owner/PRE通过并授权；作者已保存并自读，root实际正文/完整直接两侧/本人注POST通过，未复现，不授DAY。

- `SF-2026-ARXIV-2605-30343` — Daily2026-05-30补May29；exact-Mayv1必要Source/当前MODEL-DECODER-ONLY具体gap与A63原PRE由唯一reader R113通过，首次2+2+3=7。仅固定输入workspace与两阶段监督/teacher-readout mask分责，保最终readout与oracle/16选点分责、全部Prefill/LoRA/训练费与显式旧路，未核实现/复现。root授10229完整反侧后/显式CoT适用段前本原一段+本人注，作者实际保存，唯一reader R116已实际读完整新增/直接两侧/本人注POST通过并释放，不预DAY。

- `SF-2026-ARXIV-2606-16222` — Daily2026-06-17补Jun16；exact-v1 §3/4.2/T4–5/Limits/B2/C1–2必要，原2+1+2=5，仅随机可变长latent/utility分布拟合与prefix评分全费具体差额深入。保finite非精确后验、entropy非语义信息/通用阈值、Eq20不私补KL配方、RPR单项反退与多链总费，不授普遍GRPOcollapse/faithfulness或服务SLO；未核全部主表/代码/复现。root§68整体必要/actualowner/逐字PRE通过并窄授；作者已真实SAVE，root§69已唯一实际完整POST通过，本指定窄位生效释放，不预DAY。
- `SF-2026-ARXIV-2606-16360` — Daily2026-06-17补Jun16；exact-v1 §3/4/5.1/5.3–5.4/7/E3–5/F1–2/I必要，原2+2+2=6，仅typedaction/queryprojection/synth与软预算/调用位置重权具体差额深入。保θ更新口径冲突、不补hardmask、role非形式语义、单seed/任务与计时排除及全费，不授独立credit/免遗忘或SLO；未核完整forgetting附件/代码/像素/复现。root§70整体必要/actualowner/逐字PRE通过，作者真实SAVE，root§73唯一实际完整POST通过，指定窄位生效释放，不预DAY。

- `SF-2026-ARXIV-2610-32246` — Daily2026-10-27，精确v1§2/4/6/7/8，2+2+2=6，退出读出/训练目标与expected-realized-paid三成本差额深入。保loss×prior、shallowbaseline/gradientreach混杂、KV质量条件、gather局部负例/未测depthwise和有条件预检界；不采普遍无加速或部署SLO。未核实现/全图/复现，PRE/实际POST以本日REVIEW为准，未DAY。

- `SF-2026-ARXIV-2610-31943` — Daily2026-10-27，exact-v1 §3–6/完整4.3必要，3+1+2=6，只边界normalisation/训练-末层-readout兼容与K/r0/compute分责。保原norm隐尺度条件、released competencegate/小模型causal分开、head额外训练/settling未证、非显著不授等价及全费；不采任意架构去norm、无界loop或净速，未核全附件/源码或复现。实际独核/POST见本日REVIEW。

- SF-2025-ARXIV-2510-17558 — Socrates，Daily2025-10-22补Oct21；exact-v1 §3/4.2–4.5/6必要，2+1+2=5，仅中层随机条件与训练/prefill posterior、生成prior的差额。保free-bits非硬信息界、encoder偷传/latent忽略、有限任务反退与采样/训练全费；不采自由意志、替代CoT/RL、全能力或净加速保证，未核实现/复现。整体PRE/SAVE/自读/sole actualPOST只本日canonical实际层。
