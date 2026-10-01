# `2609.22816v1` — 目标可比较状态与反事实可识别性

- 身份与日期：[arXiv 摘要/版本页](https://arxiv.org/abs/2609.22816)、[exact-v1 HTML](https://arxiv.org/html/2609.22816v1)，访问 2026-09-23。官方 09-22 New 批次落本日报；Submitted 字段不是公开时刻。未证明作者没有更早项目页。
- 问题与旧方案：统一 visual latent 同时预测和比目标，在短 horizon、无几何语义时灵活；但若目标比较需要稳定的任务坐标，latent 的外观差异会污染终点 cost。离线 factual 轨迹又只有行为策略执行的 action，规划器却要比较未执行分支。
- 机制与责任：current observation/history 经 encoder、causal belief 和 grounder 得到 typed goal-comparable configuration，另有 128 维动态 fiber 保存不用于 terminal cost 的预测历史；recurrent transition 在 action 下更新两者。训练期从同一环境**公开 reset interface** 可重置状态收集多个 action branch，和 factual 数据共同监督；部署只读 image/action history/goal image，不拥有 simulator 特权状态。CEM 的 action proposal 仍需真实观测重规划和独立控制验证。
- 评价合同：Four environments、three independently trained seeds、固定 CEM budget；TwoRoom/Reacher/Cube 的受限收益并未延伸到 Push-T 持续接触，后者论文表内 75.7% 低于 matched LeWM 90.0%。reset 只恢复公开状态设定接口，不是完整 simulator 内存快照；控制结果来自模拟环境，没有真实机器人安全证明。作者的 planner-loop 计时、模型参数和 horizon 仅适用于文中 host/预算，不能外推平台 SLO。
- Books Decision：Ch25 已将 policy-support predictor 与 unrestricted counterfactual model 区分，本篇进一步把**目标比较变量**与**预测所需隐藏动力学**分权，并给可执行的 common-reset branch 数据合同，已嵌入原演进段而非论文列表。V2 Design Delta 2、System Reach 1、Durability 2，合计 5/9；写后独立复核通过。本笔记只验收单项，整日报状态以日报为准。
