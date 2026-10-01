# 2604.19254v1 → Ch30 写前独立裁决

复核者 root，非作者 apr02。实际读[官方 exact-v1](https://arxiv.org/html/2604.19254v1) §3.1–3.3、Table 1，并对读 `books/part-04-training-system/30-lora.md` 的 Recurrent Launch State、Merge 与后续 adapter 资产段。本记录只裁 Source Family 的 source→owner/literal，不是写后或 04/22 日级 Gate。

**窄采用 PASS**：Ch30 的固定 request `S0` 初始化与可 merge 的权重增量均未承载随层深、依赖当前 base hidden 的 shadow state。原文每层先由当前 shadow/base discrepancy 经 layer-dependent bottleneck 注入，再由 base output 更新 shadow；不能表述为所有参数跨层共享，亦不能把它等同未来 token 控制。应在 S0 之后解释“固定启动状态→按层耦合动态适配状态”的新状态所有权，作为 attached base+shadow 的绑定资产；detached shadow-only 是另一模型/发布物，不能继承 attached 的质量或身份。Table 1 如 Qwen3 8B 76.92 vs 36.09、预训 0.5B shadow 77.11 vs 62.11，直接限制功能等价。若写入，必须保留额外 shadow 执行、layer schema/初态/reset、质量与服务预算，以及 LoRA/S0/merge 仍适用的条件；训练参数量不等总计算或 serving SLO。未复现实验，写后仍需实际对读。
