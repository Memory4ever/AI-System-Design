# `2609.22910v1` — 视觉调用的必要性与证据使用

- 身份与日期：[arXiv 版本页](https://arxiv.org/abs/2609.22910)及[精确 v1 全文](https://arxiv.org/html/2609.22910v1)，访问 2026-09-23；官方 09-22 New 公告落入本窗。HTML 内 09-19 是投稿标记，不单独证明公开时间；更早作者渠道尚未核定。
- 问题与旧方案：最终答对可来自调用前已知信息；执行了 crop 也不证明使用了返回像素。outcome-only reward 与统一调用惩罚在工具便宜、错误代价低或无需归因时简单合理，但无法判别“必要且用到证据”的调用。
- 机制与状态：固定实际调用前 prefix `h_i`，比较直接作答、原 crop 返回真实像素、同一 crop 参数返回 K 个同尺寸随机图块。真实相对直接作答是 decision value，真实相对随机像素是 evidence value；两者超过 deadzone 且终答正确才返还调用成本，其他调用付 rent。训练 owner 计算受限过程 reward，executor 仍控制工具 schema、授权和 effect；本文只处理只读图像 crop，没有一般工具的 null return。
- 评价合同：同 cold start/prompt pool/budget，在 V*、HR-Bench 4K/8K 等视觉任务和 Qwen2.5-VL-7B、Qwen3-VL-8B 上比较；原文主要结果包括 89.5%、80.2%、76.4%，不能脱离模型与题集外推。K 个随机参考之外还有 answer-now 和 real 两个额外评分分支，即每个审计调用的评分开销随 K+2 增加；单通道消融也改变其他训练细节，不能单归因归一化方式。未证明多次调用的独立归因、随机图块完全无目标、线上 SLO 或生产授权。
- Books Decision：`AGENT-TOOL-CALLING` Ch78 已有“可用不等于应调用”的 utility admission 和视觉按需取证，但尚未分离 need 与 pixel-use，故在该处补受限反事实判据，旧固定预处理与规则调用保留；`TRAIN-GRPO` 只作奖励尺度 handoff。V2 评分 2 + 2 + 2 = 6/9。书稿写后独立复核通过。
