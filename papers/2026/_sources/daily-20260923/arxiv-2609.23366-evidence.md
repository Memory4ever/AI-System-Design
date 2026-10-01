# `2609.23366v1` — Recurrent state 的可遗忘语义边界

- 身份与日期：[arXiv 版本页](https://arxiv.org/abs/2609.23366)、[精确 v1 全文](https://arxiv.org/html/2609.23366v1)，访问 2026-09-23；官方 09-22 New 公告归本窗，09-20 投稿标记不单独证明公开。
- 问题与旧方案：压缩/收缩 recurrent state 可抑制噪声、数值漂移和容量成本，但 state 几何距离或 rank 不足以判断删掉的方向是否影响未来行为；显式 token history 的代价高但可回看。
- 机制与条件：以未来实验的完整条件分布定义 predictive quotient；同 future 的内部状态处于同一 fiber，exact corrector 必须在 quotient 上为恒等。在局部 regular、fixed-point、rank k 的条件下，d 维 hidden state 最多可抹 d−k 个独立方向。有限部署 probe bank W 与独立 audit bank U 在声明 domain、generative access 与 metric coverage 下给有限测试保证；未审未来不被认证。
- 证据边界：论文定理并不证明任意训练好的 LLM 符合光滑/可达/覆盖前提；连续可区分的 predictive states 不能在有限欧氏维度承诺正半径任意噪声精确恢复。受控模拟/MuJoCo 与 HAR stream 只支持作者定义的 probe 与状态修复设置，不是生产安全证书。
- Books Decision：`MODEL-LONG-CONTEXT` Ch22 已讨论 fixed-state 碰撞和遗忘，但缺少区分“冗余状态”与“未来语义”的明确判据；已在 Context switch/有损摘要后加入条件性语义纤维与独立 audit。V2 评分 2 + 1 + 3 = 6/9；写后独立复核通过。
