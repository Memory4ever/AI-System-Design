# 2026-05-05 V3 边界准入反证卡

**范围：** 独立终审点名的 5 个边界 family 与 1 个 Evaluation anti-case。本文不重扫来源，也不处理其他日期。

反证问题统一为：现有约束是什么，exact-v1 新增了哪个可核验状态/数据/控制机制，这个变化是否会改变长期 AI System 选择？仅“主题相关”或能映射 ROADMAP 不能准入。

## `2605.01799v1` — Embody4D

- 现有约束：单目机器人视频缺少多视角 observation，直接收集真实视角成本高。
- 新机制：由 3D-aware synthesis 构造训练集，以 warped-latent confidence 在 copy/repair/inpaint expert 间路由，并强化 interaction region。
- 决定：`Retain`。它把 novel-view 数据的派生状态、置信路由与真实闭环验证分开，足以进入 Evidence Review；最终 `No Change`，因为 Ch25 已经分开视频生成、projective 4D state 与可执行 transition。
- 边界：真实实验很小，极端视角与固定源视角仍失败，49 帧约需两分钟；不能作为实时 world-state truth。

## `2605.01896v1` — M2-REPA

- 现有约束：RGB、depth、mask 的单一 alignment target 容易抹掉模态专属先验。
- 新机制：先分离 modality-specific feature，再分别对齐对应 expert，并以 decoupling regularizer 保持互补。
- 决定：`Retain`。它改变多模态 world-model 的训练表示接口；最终 `No Change`，因为 Ch23 已把语义、时空、行动和重建目标分责，且明确不同 modality 可以拥有专用容量。
- 边界：结果继承 expert bias，增加训练成本，只在作者生成模型和数据上验证。

## `2605.01948v1` — Phone2Act

- 现有约束：专用 teleoperation hardware 与 robot-specific collection stack 限制 VLA 数据规模。
- 新机制：手机 6-DoF pose、可替换 ROS 2 bridge、同步多相机/robot-state recorder 与 LeRobot serialization 形成明确数据接口。
- 决定：`Retain`。它改变采集数据的 schema、同步与 hardware bridge owner；最终 `No Change`，因为 Ch27 已要求 teleoperation 派生数据绑定输入设备、robot schema、时间/provenance 与真实闭环 admission。
- 边界：130 episodes、一个任务和一台 Dobot 不能证明跨 embodiment 可迁移。

## `2605.02525v1` — Semantic Autonomy Stack

- 现有约束：所有指令都调用 VLM 会产生秒级延迟，session-local 状态又无法复用已验证偏好。
- 新机制：确定性 resolver 先处理稳定路径，歧义才升级 VLM；验证后的偏好按 global/operator/robot scope 提升为共享 digest。
- 决定：`Retain` 且深入审阅。它改变 fast/slow 语义路由与 memory promotion；最终 `No Change`，因为 Ch77 已规定 stable/transient、scope、promotion、访问权与 capability gate。
- 边界：只验证一个 4B 模型、两台相似机器人、兼容 graph/POI identity；巨大 latency 比例不能外推。

## `2605.02757v1` — Seeing Realism from Simulation

- 现有约束：全量 sim-to-real video transfer 昂贵，且视觉 domain gap 不能由增加模拟样本自动消失。
- 新机制：segmentation/caption 条件化 transfer 保存 action trajectory，以 diffusion feature reuse 降成本，并用 coreset 选择增强分母。
- 决定：`Retain`。它改变 data transform、cache 与 subset-selection identity；最终 `No Change`，因为 Ch27 已要求 synthetic/teleoperation transform、coreset、lineage 与真实 held-out/closed-loop gate。
- 边界：视觉逼真不证明接触动力学和 action semantics 保持，coreset 会漏掉 rare safety tail。

## `2605.02443v1` — HalluScan anti-case

- 现有约束：hallucination evaluation 必须冻结 subject、dataset、scorer、run identity、校准、风险覆盖和不确定性。
- 新机制：HalluScore composite metric 与 Adaptive Detection Routing；但“72 configurations”来自 `6 methods × 4 model families × 3 domains`，实质只有每域 8 条、共 24 条样本。
- 决定：`Pre-denominator Closure`。HalluScore 与专家只有中等相关 `r=0.41`，ADR 的 `2×` 成本结论绑定同一 benchmark、metric 和 routing setup；没有改变 Ch66 的通用 evaluation contract。
- 重开条件：跨数据集独立人工校准、稳定置信区间，或出现足以改变 release-grade evaluator routing contract 的新证据。

