# Part I 世界观：先建立问题地图

## Part Question

AI 为什么从单个学习算法演化成包含模型、训练、推理、平台与 Agent 的系统？面对快速变化的技术，哪些约束和判断方法可以长期复用？

## 进入条件

本 Part 假设读者理解普通软件与分布式系统，但不要求已经掌握神经网络公式。它先建立语言和边界，避免后续把模型能力、Runtime 性能与平台治理混成同一问题。

## 演进主线

```text
规则系统的边界
→ 从数据中学习
→ 学习表示而非手写特征
→ 内容相关的信息路由
→ Scaling 扩大可复用能力
→ 对齐、工具与系统交付
→ 从单机实验走向受治理的行动闭环
```

这不是“旧技术被新技术淘汰”的年表。每次迁移都保留旧方案成立的条件，并追踪成功之后新增的 compute、memory、data、reliability 与 governance 压力。

## 章节分工

- [Ch1](01-why-learn-ai-system.md) 定义为什么研究对象必须是 AI System，而不只是 Model。
- [Ch2](02-ai-history.md) 追踪能力生产方式如何改变，以及瓶颈为何迁移。
- [Ch3](03-global-knowledge-tree.md) 把能力生产、交付、治理与行动放进统一知识树。
- [Ch4～5](04-why-models-learn.md) 从优化与表示解释模型为何能够学习，以及“学到什么”的证据边界。
- [Ch6～8](06-why-transformer-changed-the-world.md) 解释 Transformer、Scaling 与 LLM 能力如何形成，同时保留可靠性边界。
- [Ch9](09-ai-system-evolution.md) 从系统责任而非模型年代重建 AI System 演化。
- [Ch10](10-future-of-ai.md) 用长期约束检验未来方向，不做产品时间表。

## 退出契约

读完后，应能把新技术放回“能力生产、能力交付、控制治理、行动闭环”之一，并先询问约束、状态和证据，而不是从产品名称开始判断。Part II 随后把这张宏观地图落实到一个 token 的具体计算路径。

