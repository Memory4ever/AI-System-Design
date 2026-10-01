# 2604.25380v1 DynamicGUI：本日作者有限证据审阅

本文件只审 [官方 exact-v1 HTML](https://arxiv.org/html/2604.25380v1) 的 §3.1–3.3、§4.1–4.4、§5.1–5.4 和真实 owner 邻段；不继承旧日报的 9 分／`deep_complete`。04/29 归属暂沿本日 arXiv 公告联合批次 `2604.24765–2604.25918`，未以 HTML 页首 `28 Apr` 或 submitted 孤证宣称首公开。没有发现本文给出可核的更早独立正式正文；若出现 conference/proceedings 或项目 artifact 早公开证据，重开日期。

## 贡献准入与必要机制

题摘有具体系统问题，不因 GUI 局部应用机械拒绝：一动作一张事后截图会漏掉两动作之间出现又消失的关键状态；作者按 interruptive UI、ephemeral reference、dynamic list、content-triggered interaction 构造 149 个 online tasks／10 个应用的 DynamicGUIBench。其框架保存操作过程视频，对帧特征聚类、以 VLM 给中心帧 caption 和相关性／置信度，阈值不足就增聚类数，再以选中的历史帧提供动作上下文；另有 action-conditioned thought/action refinement 与独立 VLM reflection。这里可迁移的判断是 evaluation 的 observation sampling policy 必须与 action clock、真实 effect 检查分账，不能把一次事后截图当完整状态。

评分先限 `Design Delta 2 + System Reach 2 + Durability 2 = 6`，Standard。旧表 `3+3+3=9` 只凭研究标题及“新 benchmark”过宽：机制是现有 video/frame selection、反思与动态任务分层的有条件组合；长期增量集中在**动作间遗漏事件的 EvalSpec 切片与 observation 版本身份**，不是任意 GUI agent 一定应上此三模块，也没有 7+ 的受控安全覆盖／实际无主 owner 证据。

## 主结果、直接反证和所不能证明

- Table 3 在同一个 DynamicGUIBench、50 步时，Qwen3-VL-8B 基线 15.1%，全框架 22.1%；15 步时为 14.8%→15.5%。149 个任务有 146 feasible、3 infeasible。这个 outcome 支持受限任务集进步，不是所有平台、时延预算或权限副作用可靠性。
- Table 4 逐步消融：基线 15.1%，加 Dynamic Perceiver 17.4%，再加 refinement 仍 17.4%，加 reflection 20.8%，全框架 22.1%。因此不能把 7.0 点全归因于视频选帧或 refinement；reflection 是主要增量之一。Table 6 又把 `Ours DP` 行列为 22.1%，与 Table 4 的 DP-only 17.4% 不同；在协议/组件标签未澄清前，只采同表内部的受限比较，**隔离“仅 DP 优于 uniform 3-frame 达 22.1%”** 归因，不否定任务级全框架结果。
- Table 6 的均匀 1/3 帧平均 16.8/16.4%，但 ContentTrig 中 DP 行 15.4% 低于 baseline 19.2%；Table 5 同一 Qwen3-VL-8B 在 OSWorld 从 25.8% 到 28.4%，细分 Writer 56.5→26.1、Impress 31.8→19.6、Thunderbird 66.7→40.0。不能宣称视频/选帧单调有益。Table 7 改用 GPT-5.4-mini reflection 时总体 22.1%，同模型 Qwen reflection 11.3%；额外模型身份和成本不可忽略。
- 实际动作 hit-target、事件召回、轨迹时间戳误差、视频 capture/token/call 成本、重复运行 CI 与独立真实桌面环境外推均未在这些必要主表里被单独证明。§4.3 用前后截图和 action 让另一 VLM **改写** thought/action，不能据此声称已读到真实 DOM 或执行 effect；多模型反思文本也不能替代 task-specific evaluator。

## 真正 owner 与 Books 决策提案

实际 [Ch84 Observation Interface 必须独立于 Action Clock](../../../../../books/part-07-agent/84-agent-platform.md) 已明确单张截图遗漏动作间短暂 UI、gated keyframe、版本化 observation/time line、action receipt 和漏帧/稀释回退；[Ch78 Computer-use Action](../../../../../books/part-07-agent/78-tool-calling.md) 已要求真实 program state、effect-time completion。故**不**在 Ch84/Ch78 重复视频是必须的通用主张，也不把作者算法整体称为现有实现。

[Ch66 living-world EvalSpec](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 已有 turn 间 exogenous mutation log 与 pre/post state digest，但未明确**同一 turn 的两动作之间 transient event** 是否被 benchmark capture/replay、以及其漏失率／任务完成率要按 `InterruptUI/EphemRef/DynList/ContentTrig` 切片。最小可能增量是 Ch66 一小段：动态 computer-use 评测必须保存 event-time observation policy、可重放短暂状态与 task-specific effect verdict；比较 post-action-only、均匀帧、gated keyframe 时固定模型、工具权限、步骤/帧/token/call 预算，并同时报 missed-event 与 outcome，不能从单 benchmark 榜单或反思模型替换推导普遍收益。需 root 非作者核官方必要表、当前 Ch66 邻段与文字后才授锁；若认定 Ch84+Ch66 现有合同已充分承载，则 `No Change — Existing Coverage`／报告受限证据即可。本作者**未写共享 Books**。

停点：贡献准入与必要原文已读，日期归属仍需纳入全日联合来源 Gate；Books 仅提案，待独立 source→actual-owner 裁决，不能计整日 Gate。
