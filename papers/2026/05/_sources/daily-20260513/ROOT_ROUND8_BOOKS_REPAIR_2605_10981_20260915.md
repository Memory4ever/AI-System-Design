# 2026-05-13 Round 8 Books Repair — 2605.10981

- 触发：fresh non-author reviewer 指出原正文把 `beta`、`gamma`、`xi` 误写为并列旋钮，与 exact-v1 的 ratio transformation 会消去 `beta` 对 margin 定义的影响相冲突。
- 修复：明确 SimPO 中 `beta` 的 sample-filtering 作用与 `gamma` 的 dataset-gap dependence；明确 ξ-DPO 用 chosen/rejected reward ratio 消去 `beta` 对 margin 定义的影响，并以单一、有界 `xi` 取代 `beta/gamma` 对目标 margin 的耦合调节。
- 保留边界：`xi` 的初始化仍依赖训练前 gap 分布；ratio normalization、distribution drift 与 late-stage target-likelihood collapse 仍需监控，DPO/SimPO 保留为 fallback。
- 状态：root 语义修复已落盘，等待未参与写入的 fresh non-author reviewer 复核后才能关闭 2026-05-13 Gate。
