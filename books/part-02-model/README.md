# Part II 模型基础：一个 Token 如何变成答案

## Part Question

开放世界中的文本怎样被转换成张量，经 Transformer 逐层处理，再变成下一个 token 的概率？参数容量与序列容量为什么会成为两条不同的扩展轴？

## 进入条件

Part I 已经说明模型能力只是 AI System 的一层。本 Part 暂时冻结训练 recipe 和在线平台，只追踪模型语义、tensor shape 与生成状态，避免用 Runtime 优化解释模型能力。

## 演进主线

```text
Text
→ Token IDs
→ Embedding + Position
→ Self Attention + MLP
→ Residual Transformer Layer
→ Causal Decoder
→ Logits + Sampling
→ KV State
→ Parameter Capacity / Sequence Capacity
```

前十章形成生成主干；MoE 和 Long Context 分别回答“如何扩大可用参数容量”和“如何扩大可用序列状态”。它们是正交约束，不是生成流水线中的两个连续算子。

## 章节分工

- [Ch11～13](11-tokenizer.md) 建立离散输入、连续表示与位置关系。
- [Ch14～17](14-self-attention.md) 推导 Attention、Multi-Head、MLP 与可堆叠 Transformer Layer。
- [Ch18～20](18-decoder-only.md) 建立 causal generation、KV state 与输出选择。
- [Ch21](21-moe.md) 拆开 total parameters、active parameters、routing、placement 与 communication。
- [Ch22](22-long-context.md) 联合位置有效性、Attention、KV capacity、信息利用和 SLO。

## 退出契约

读完后，应能沿 shape、state 与条件概率解释一次生成，并区分模型语义与 Runtime 实现。Part III 将文本 token 的经验扩展到图像、视频、音频、环境状态和动作，但不会假设 shape 相同就意味着语义统一。

