# 2604.26340v1 — Ch30 非作者写后复核

复核者：root；2026-09-29。仅验收这一项 Books Integration，不替代 04/30 日级来源、日期、分母或整体语义 Gate。

- 官方 [exact-v1 §III-C–F / Algorithm 1 / Table I–II](https://arxiv.org/html/2604.26340v1) 与 [Ch30 实际正文](../../../../../books/part-04-training-system/30-lora.md)的前后段已重读。正文将旧可回滚 mask 与新一次性物理裁除区分开，明确 expert 参数、Adam moments、gate 坐标和后阶段优化目标的状态迁移；与邻接的 placement / activation-selected update 分支衔接顺畅，不只是标签或论文名。
- 印刷算法固定 `E_w=1`，不是以 drift 达标为在线触发器。正文和 Review note 均保留此边界。Table I throughput 只计最终训练阶段；Qwen3-8B / ScienceQA 的 AEP 96.40 低于对称 MoE 97.08，正文以反向切片保留，不宣称无条件收益。此处数字仅用于核验作者受限实验，非通用性能保证。
- 完整探索 checkpoint、质量回归与旧 mask 回退在正文中明示为工程验收要求，不冒称论文已证明结构性删除可逆。论文未提供独立生产复现或长期漂移验证；书稿保持 Experimental。

结论：`Integrate` 实际正文与相邻论证写后通过。其余 04/30 候选及日级 Gate 仍由当日作者与独立复核继续完成。
