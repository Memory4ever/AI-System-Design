# Part III 多模态、生成与世界模型：从表示到物理行动

## Part Question

当输入不再只是文本，系统怎样表示不同模态、生成可修正输出、预测环境转移，并最终把模型 proposal 接入具有真实副作用的行动闭环？

## 进入条件

Part II 已经建立 token、Transformer、KV 与生成语义。本 Part 复用这些组件，但为 modality、time、space、provenance、mutable state、action schema 和 safety 增加独立契约。

## 演进主线

```text
Raw multimodal signal
→ versioned representation
→ autoregressive or iterative generation
→ action-conditioned world transition
→ trajectory / action proposal
→ controller and safety envelope
→ environment observation and correction
```

四章不是“多模态应用列表”。它们逐步扩大状态责任：Ch23 定义表示身份，Ch24 定义生成与 commit，Ch25 定义可修正环境状态，Ch26 才允许 proposal 进入物理控制。

## 章节分工

- [Ch23](23-multimodal-representation.md) 拥有 modality representation、fusion、alignment 与 provenance identity。
- [Ch24](24-multimodal-generative-paradigms.md) 比较 AR、Diffusion、Masked/Block Diffusion 的 factorization、并行、cache 与 commit。
- [Ch25](25-multimodal-world-models.md) 区分视频生成、环境预测、causal control 与 persistent world state。
- [Ch26](26-multimodal-embodied-vla.md) 连接 perception、VLA proposal、low-level controller、sim-to-real 与 physical safety。

## 退出契约

读完后，应能区分“生成看起来合理的 observation”与“预测可干预的环境 transition”，也能说明模型 action proposal 为什么不能拥有最终执行权。Part IV 接手这些能力的数据、目标与训练状态，而不重新定义它们的语义。
