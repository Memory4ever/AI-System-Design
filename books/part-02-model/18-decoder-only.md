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

### 历史状态生产与最终预测可以分开

上一分支改变了预测目标的粒度，另一条与 concept 时钟不同的分支仍保持逐 token 的因果输出，却将**历史 KV 的生产者**与**读取这些 KV 的预测容量**分开。普通深层 Decoder 的新增层也要重算全部 prompt token 的 KV；若目标是扩充模型能力而不同比例增加 Prefill，可以让较小的前段网络产出可复用 KV，再让新增的 token-local 后段只读前段 KV、负责更强的最终预测。新增后段不能写入未来位置要消费的 KV，否则“只运行前段处理长 prompt”的等价性就失效。训练时两段仍可联合更新，并非冻结旧 KV 数值；结构不变量是后段不改变 KV 的**生成路径**。它用更便宜的 bulk Prefill 换训练拓扑和推理引擎复杂度，也仍须为每个输出 token 支付完整后段计算。输入短、输出长、KV 共享实现困难或直接堆层更易维护时，标准 Decoder 继续成立。KITE/SST 的作者证据主要是训练损失、任务分数与按 Prefill/Decode 权重构造的推理成本 proxy，不是任意生产 workload 的端到端延迟证明。<!-- source-family:SF-2026-ARXIV-2609-27294 -->

### Multi-stream 把单一 Token Clock 降为接口选择

前两种分工仍可保留单一外部序列；当压力来自多路输入输出的等待时，才需要重新审视流之间的同步。单流 Decoder-only 让 thought、input 与 output 共用一个因果时钟，训练、KV 与流式协议最简单；并行工具输入、内部推理和可见输出会让单流阻塞暴露出来。multi-stream 分支为不同 stream 保持各自位置与可见性规则，再由显式 synchronization/merge point 交换状态；模型拥有 token proposal，runtime 持有 stream lifecycle、权限与外部 effect commit。

并行流可以减少等待并隔离可见输出，却引入跨流因果一致性、KV/layout、训练数据格式和 monitor blind spot；错误同步可能泄漏 private thought 或产生乱序 effect。普通聊天、工具少或审计优先时，单流协议仍是可靠基线。`arXiv:2605.12460v1` 的 §2–§7 与附录只验证作者的多流训练和实验，不证明 production scheduler 一定获益，也不替代 Agent 权限控制。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-12460 -->

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

连续状态直接回灌还多了一项输入接口合同：上一轮 decoder hidden state 与下一轮 input embedding 未必属于兼容的表示坐标。一个分支把 context-carried hidden 与当前词表分布的 top-p embedding 加权融合，再输入下一 latent transition；untied 输入/输出空间还可增加适配投影。它没有恢复逐步可见推理，也不能由 tied 与 untied 模型之间的差异唯一归因接口 mismatch，fusion、adapter、触发与停止规则必须和 checkpoint 一起验收。<!-- source-family:SF-2026-ARXIV-2602-10229 -->

[受限算术对照](https://arxiv.org/html/2602.10229v1)中，去掉 fusion 的8B配置弱于不用 latent，说明 latent 更新不是无条件改善；少量 PCA/attention probe 也不证明推理忠实或因果 collapse。课程、teacher 与接口训练增加成本，可见 tokens 变少不等同总 FLOPs 或完整生成延迟减少。回灌失配、latent 漂移或质量下降时，应恢复显式 token/CoT 或已验证的 embedding 接口，而不是仅增加不可观察的 transition 次数。

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

### 状态进入循环后，监督与停止必须重新定义

选择表示只回答了状态存在哪里，还没有回答循环中的哪些状态受到约束、何时可以停止。Decoder-only 的状态不仅是可见 token。Looped 或 latent reasoning 把部分推理迁入 recurrent hidden state 后，dense per-loop loss 只能约束 readout 可见方向；normalization 隐藏的尺度仍可能在 residual recurrence 中携带信息。在 RMSNorm/LayerNorm 隐藏 radial scale 的这一条件下，需要让尺度对 loss 可见，或从 recurrence 中移除该尺度自由度。训练 contract 因而要明确哪些 latent state 对 loss 可见、何时提交以及如何停止。

这正是减少可见 token 后增加不可观测状态、循环稳定性和调试成本的具体来源。latent state 无法校准或行为审计失败时，应回到显式 CoT、固定 loop 或普通 autoregressive decode；减少 token 不等于删除推理状态。

逐 token 停止还必须区分“这个位置不再更新”与“其他位置不再读取它”。一种自适应循环把 halting mask 设为单调：一旦停止，该位置不再更新下一轮输入 embedding，并保留其前一轮 K/V，仍允许活跃位置读取；不能为了省计算把它从因果上下文删除，也不能由 embedding 停止更新推断实现中的所有 hidden readout 都已冻结。训练也需暴露同一种状态语义，先让 gate 学会可用的更新，再逐渐引入提前停止压力；否则 gate 可能退化为全部继续或全部过早停止。停止拥有的是迭代预算，不是正确性证明或输出提交权。

这用更少状态更新交换 gate、稀疏执行和训练校准成本，FLOPs 减少未必成为 wall-clock 收益。[AdaPonderLM 的受限对照](https://arxiv.org/html/2603.01914v1)显示停止比例与正则强度会改变质量，较小模型的部分结果也低于固定循环；继续预训练的比较还需区分额外训练 token，不能把所有差异归于 gate。固定预算循环在停止器不稳、稀疏工作难以执行或审计要求一致时仍然成立；推理引擎如何跳过更新而不破坏 cache 生命周期，交给 Part V。<!-- source-family:SF-2026-ARXIV-2603-01914 -->

增加推理循环数也不自动获得深度泛化：共享 block 必须先在训练中学会反复使用其状态更新。在受控的合成多跳实验中，训练 recurrence 的覆盖范围影响增加推理循环后的收益；不同课程可能暴露不同 hop 深度，因此不能把它们的最大外推深度直接归因于动态循环。即使固定同一训练数据，更多循环也可能在已有正确状态后继续漂移，形成 overthinking，而不是单调逼近答案。普通固定深度 decoder 与固定 loop 在任务、预算或停止信号不稳定时仍是合理基线。

停止条件须分开“输出不再变化”和“已有可提交结果”。相邻循环分布的 KL 很小，可能只是停在高熵的含糊分布；一个受限替代是同时要求 KL 小与输出熵低，再决定是否停止。它增加阈值校准和逐轮 readout 成本，也不能阻止稳定、低熵的错误；熵是集中度 sensor，不是真值。作者用于解释 overthinking 的正确 token logit margin 依赖答案标签，不能直接当作线上可用停止器。该分支目前由从头训练的合成关系任务支持，不能外推到任意预训练 LLM；超出已验训练/推理循环范围时，仍应保留循环上限、固定预算与显式验证。<!-- source-family:SF-2026-ARXIV-2604-07822 -->

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
