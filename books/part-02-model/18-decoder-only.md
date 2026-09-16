# 第18章 Decoder Only 架构

**Knowledge Tree:** Part II 模型：一个 Token 如何变成答案
**Stable Knowledge Node ID:** `MODEL-DECODER-ONLY`
**Legacy Chapter:** Ch18
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

`mask_t` 决定哪些位置贡献 loss，不改变 causal Attention 本身。具体数据格式和训练阶段属于 Part IV，本章只建立模型接口。

## Next-token 接口不要求内部状态只有一个粒度

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


### Multi-stream 把单一 Token Clock 降为接口选择

单流 Decoder-only 让 thought、input 与 output 共用一个因果时钟，训练、KV 与流式协议最简单；并行工具输入、内部推理和可见输出会让单流阻塞暴露出来。multi-stream 分支为不同 stream 保持各自位置与可见性规则，再由显式 synchronization/merge point 交换状态；模型拥有 token proposal，runtime 持有 stream lifecycle、权限与外部 effect commit。

并行流可以减少等待并隔离可见输出，却引入跨流因果一致性、KV/layout、训练数据格式和 monitor blind spot；错误同步可能泄漏 private thought 或产生乱序 effect。普通聊天、工具少或审计优先时，单流协议仍是可靠基线。`arXiv:2605.12460v1` 的 §2–§7 与附录只验证作者的多流训练和实验，不证明 production scheduler 一定获益，也不替代 Agent 权限控制。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-12460 -->

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

## 从显式 CoT 到 Latent Reasoning：减少 Token 不等于消除状态

显式 Chain-of-Thought 把中间步骤写成 token，优点是训练目标、停止条件、缓存和人工审计都复用语言模型接口；代价是每一步都要经过 vocabulary projection、采样和下一轮 Decode。将中间推理压缩成连续 latent state，可以少生成可见 token，却没有消除递归依赖：系统仍需决定 state representation、更新次数、termination、checkpoint identity 与失败恢复。

```text
explicit token trace
→ compressed visible trace
→ recurrent hidden state
→ learned latent transition with teacher guidance
```

后两个分支把成本从 token IO 移到 latent transition，并牺牲逐步可读性。训练期用完整 CoT、视觉编码或其他 teacher signal 约束 latent state，只能证明该 state 在指定任务与模型上可学习，不能证明它保留了原推理的全部语义或因果结构。推理期若只用代表 token 判断结束，还会新增 premature stop、state drift 与无法局部纠错的 failure mode。

因此显式 CoT 在高风险审计、工具副作用和需要逐步验证时仍然合理；latent reasoning 更适合中间步骤冗长、可由独立 outcome verifier 检查且 token latency 占主导的受控任务。二者是不同 observability / efficiency contract，而不是后一种对前一种的线性替代。

固定使用完整显式轨迹或固定使用 latent state，是这一设计空间的两个端点。中间分支可以先预测下一段 reasoning span 的冗余度与压缩置信度，只把高置信、低信息增量的 span 编码为 latent representation，同时让 precision-critical span 继续走显式 CoT。这里的 gate 决定的是**下一段采用哪种 reasoning representation**，不是在生成后由 target verifier 接受或回滚 proposal；因此它属于 Decoder-only 的表示与状态演进，而不是 speculative decoding 的 commit protocol。

这种选择性表示减少了部分可见 token，却新增 gate calibration、显式/latent 双路径训练和 latent error propagation。置信度失准或 distribution shift 会把本应显式保留的步骤过早压缩；高风险、需要逐步审计或 gate 未校准时，完整显式 CoT 仍是正确 fallback。现有 exact-v1 证据只覆盖论文披露的数学任务、模型、span anticipation、三阶段训练与消融，不证明压缩无损，也不证明开放域 reasoning 能获得相同结果。<!-- source-family:SF-2026-ARXIV-2605-25745 -->

### 表达能力还取决于实现中的有限精度状态语义

实数域公式常把 causal Attention 看成任意精确的加权聚合，但真实 decoder 逐位置更新的是有限精度内部状态；accumulator、舍入、求值顺序和层间组合都会改变它能稳定区分的历史。因而“架构图相同”并不保证同一表达上界，kernel 重排或精度变化也可能改变可实现的 memory semantics。

组合理论能在明确 arithmetic、mask、position 与 wiring 假设下连接 attention type 和可识别语言，但它不等于对普通 LLM 完整能力的刻画，也没有替代训练和下游实验。长期结论是：讨论 decoder expressivity 或等价实现时，必须同时声明抽象算子与执行语义；在无法证明有限精度等价时，应保留 reference path 和行为回归，而不是只凭代数重写批准替换。

<!-- source-family:SF-2026-ARXIV-2607-26988 -->

<!-- semantic-body-binding:SF-2026-ARXIV-2605-22223:start -->
有限精度之外还存在另一层上界：固定架构并不保证任意输出序列都可由某个 prompt 触达。prompt 只选择输入，decoder 的 embedding 与 decision regions 才决定输出 support；因此增加 context、Decode 时间或采样预算，可能在既有可达区域里搜索得更充分，却不会自动创造新的可达区域。在一组明确的 bounded-embedding、decision-cell 与 packing 假设下，可达序列的最大长度只随 prompt 长度线性增长，超过模型相关阈值后，可达序列占全部序列的比例会指数下降。

这是一条架构条件下的诊断上界，不是对某个自然语言答案“模型必然无法生成”的判决，也不证明训练不能改变模型相关常数。工程上应由 Evaluation owner 用 copying、cramming 与长度切片实验估计实际 cliff，并把 tokenizer、decoder、precision 与 decoding policy 固定为同一评测身份。形式假设或常数无法核实时，直接行为测试仍是 fallback；理论结果只能提出风险假设，不能替代部署 checkpoint 的验证。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-22223:end -->

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

第24章把 causal autoregressive factorization 放进更广的生成范式树。Diffusion、Masked/Block Diffusion 可以并行更新多个 provisional positions，却会增加 correction、cache invalidation 与 commit protocol；它们是不同生成 contract，不意味着 Decoder-only 被线性替代。

## 从机制演进到系统设计

Decoder-only 的状态不仅是可见 token。Looped 或 latent reasoning 把部分推理迁入 recurrent hidden state 后，dense per-loop loss 只能约束 readout 可见方向；normalization 隐藏的尺度仍可能在 residual recurrence 中携带信息。训练 contract 因而要明确哪些 latent state 对 loss 可见、何时提交以及如何停止。

减少显式 token 可以降低输出带宽，却增加不可观测状态、循环稳定性和调试成本。latent state 无法校准或行为审计失败时，应回到显式 CoT、固定 loop 或普通 autoregressive decode；减少 token 不等于删除推理状态。

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

这种统一接口简化了数据与任务表达，也把序列状态、生成串行性、Sampling 和评估复杂度带入系统。它是现代 LLM 的重要架构选择，而不是所有任务的唯一最优解。

## Review notes

本轮联章 Review 对齐了 causal factorization、tensor position 与 shifted target 的索引，并把第 19 章的状态分支和第 20 章的决策分支放回同一个 Decode step。本章仍只解释架构、mask、shifted targets 和 logits contract。Pretraining/SFT 数据与 loss 配置属于 Part IV，Prefill/Decode 的硬件执行与调度属于 Part V。

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
