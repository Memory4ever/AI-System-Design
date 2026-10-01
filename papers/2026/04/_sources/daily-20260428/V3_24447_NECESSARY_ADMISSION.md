# 2604.24447v1 VLA 异构加速：必要贡献消歧（作者侧）

固定窗口仍为 `[2026-04-27T09:00:00+08:00, 2026-04-28T09:00:00+08:00)`。此文仅为工作池开放线索的 exact-v1 必要源→实际 owner 准入核；没有核实 first-public、评分、完整审阅或申请 Books 锁。

[官方 v1](https://arxiv.org/html/2604.24447v1) §3 的 CET 先用显存/控制频率做可行性门禁，再在可行 pair 中比设备成本/能耗；这是合理但 [Ch26](../../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) 当前已要求端到端 deadline、控制频率、tail/jitter 与 safety envelope，不能仅因跨 XPU 榜单入书。§4 的 VLM compute-bound、Action Expert memory-bound 也需绑定所测模型/硬件，不能写成所有 VLA 的固定算术强度。

真正可再核的差异在 §5.2–5.3：DP-Cache 在**同一次**迭代 action denoising 中用离线定好的约 20–80 步稳定段复用中间结果；V-AEFusion 在第 `t` 次控制周期开始时让 Action Expert 用上一观测的旧 KV 做前几步，再切换本次 VLM 新 KV 完成后续步。两者分别改变去噪步骤与观测版本的可见性，并非相同缓存。实际 [Ch26](../../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) 约 525–597 行已拥有异步 VLM/Action、stale observation 的版本化/回退，以及 speculative draft/phase-aware commit；但未精确写“同一次 action denoising 中可允许多少旧观测条件步”的控制旋钮。是否需要形成长期正文分支须非作者比较，而不是把整套 XPU leaderboard 添进 Ch49。

关键反证不能丢：§5.2 Table4 中 DP-Cache `S=8` 虽比 `S=4` 快，Spatial/Object/Long 成功率分别 71.6/46.1/73.4，低于 baseline 75.4/52.4/74.1；§5.2 Table5 的 Franka 单任务 50 trials，95→74 ms 同时 SR 76→70，非无损。§5.3 Table7 的旧 KV 步数从 0 增至 5/7/9，双任务成功率从 92/86 降至 88/78、50/42、10/6；不存在任意多 overlap 都安全的结论。Table9 中 Ascend 310P 818→820 ms 反向，无跨硬件统一加速。§6 Limitations 承认可能牺牲精度，更多模型/加速器与专用 Action Expert 尚待扩展。控制器依旧拥有执行与紧急停止权，本文未给开放场景物理安全保证。

作者侧建议：保留**有限贡献准入线索**，优先评估 Ch26 的“stale KV 只用于去噪早步，fresh KV 接管晚步”是否确实新增设计选择；若既有 staleness/cancellation 段已充分承载，则可 Existing/Only，不因异构硬件数字机械写书。日期、等模型精度/硬件的评价与系统成本待真正候选阶段再核；目前不是正式分母。

既存官方身份回放中本项 `v1_updated_timestamp_revision_metadata_only=2026-04-28T01:44:50Z`，晚于本窗 `01:00Z` 截点；`oai_current_datestamps=[2026-04-28]` 也只表元数据状态。两者既不能证明窗外，也不能证明 09:00 前 first-public；如准入通过，须按公告槽/同批邻界及更早作者原始发布定点核日期，未解时保留 **Date Hold**，不让贡献判断倒推日期。
