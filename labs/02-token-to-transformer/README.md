# Lab 02 — Token to Transformer

## Lab Question

一个离散 token 怎样经过表示、位置、内容相关路由和非线性变换，成为 Decoder-only 模型的下一 token 分布？

## Why This Lab Exists

固定窗口 n-gram 或 bag-of-words 在局部统计任务中便宜有效，却不能稳定表达长距离依赖与内容相关交互。
Transformer 让 token 根据当前内容选择信息来源，但同时引入 masking、residual、normalization 与 shape contract。

## Books / Stable Node Mapping

| Stable Node | Chapter | Role in This Lab |
| --- | --- | --- |
| `MODEL-TOKENIZER` / `MODEL-EMBEDDING` / `MODEL-POSITION-ENCODING` | Ch11～13 | 输入表示链 |
| `MODEL-SELF-ATTENTION` / `MODEL-MULTI-HEAD-ATTENTION` | Ch14～15 | 内容相关路由 |
| `MODEL-FFN` / `MODEL-TRANSFORMER-LAYER` | Ch16～17 | token-wise transformation 与 residual path |
| `MODEL-DECODER-ONLY` | Ch18 | 自回归组合 owner |

## Prerequisites

- 完成 Lab 01。
- 理解 softmax、cross entropy、矩阵 shape 与 batch/sequence/hidden dimensions。

## System Under Test

小词表、短序列、单层到多层的 Decoder-only Transformer。每个模块公开输入输出 shape，中间 state 可与
reference implementation 对齐。

## Baseline

从 unigram/bigram 或固定窗口 MLP 开始；它们在短依赖、小词表和严格 latency 下仍可能更合适。

## Step-by-Step Experiments

1. 实现可逆的最小 tokenizer contract，验证 encode/decode、unknown 与 padding identity。
2. 实现 token embedding 与 position encoding，观察没有位置时的 permutation ambiguity。
3. 手工实现 single-head causal attention，对齐 mask、scale、softmax 与 reference output。
4. 扩展 Multi-Head Attention 与 MLP，分别检查 head concat、projection 和 token-wise semantics。
5. 组合 normalization、residual 与 Transformer Layer，比较 Pre-Norm/Post-Norm 的 gradient path。
6. 堆叠为 Decoder-only LM，完成 teacher-forced loss，并逐层记录 activation/gradient。

## Expected Artifacts

- 最小 tokenizer、逐模块 Transformer 与 reference parity tests。
- 一份可用于 Lab 03 Decode 的小模型 checkpoint 和 shape/state contract。

## Invariants

- Causal position 不读取未来 token。
- Padding 不改变有效 token 输出；shape、dtype 与 mask semantics 明确。
- 拆分实现与 PyTorch reference 在数值 tolerance 内一致。

## Failure Injection

- 移除 position、反转 causal mask、遗漏 scaling、交换 head layout、破坏 residual 或 normalization 顺序。
- 用全相同 token、极长/极短序列和极端 logits 检查数值稳定性。

## Measurements

- Per-module numerical error、loss、gradient norm、activation range。
- Sequence length 对 attention FLOPs、memory 与 wall-clock 的影响。

## Acceptance Criteria

- [ ] Tokenizer 到 logits 的完整链路可逐层复现并与 reference 对齐。
- [ ] Causal、padding、position 与 residual invariants 均有负向测试。
- [ ] 能解释 attention 与 MLP 分别改变什么，而不是把 Layer 当黑盒。
- [ ] 输出 checkpoint 和 module contract 可被 Lab 03 加载。

## Trade-offs and Alternatives

更多 heads/layers 增加容量，也增加 memory、optimization 和执行成本。固定窗口、RNN 或 convolution 在局部依赖、
流式约束或硬件预算下仍有价值；本 Lab 只建立 Transformer 主干，不宣称它是所有序列问题的唯一方案。

## Reflection Questions

1. Position information 为什么不能由 token embedding 自动唯一恢复？
2. Attention 的 state 与 MLP 参数各自承担什么能力？
3. 哪个错误最容易被最终 loss 掩盖，却会破坏后续 KV Cache？

## Next Lab Handoff

向 Lab 03 交付 deterministic checkpoint、tokenizer、causal mask、逐层 shape 以及 full-sequence forward reference；
下一步把 teacher-forced 全序列计算改成逐 token runtime。

