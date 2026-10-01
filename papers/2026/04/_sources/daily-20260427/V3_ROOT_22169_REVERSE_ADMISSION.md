# 04/27 ReCast：旧泛化前关闭的定点逆向准入

复核者：root；日报作者：apr01。复核日期：2026-09-28。此记录只裁 `2604.22169v1` 的贡献准入与必要原文/owner，不代签 158 项排除组、14 来源或整日 Gate。

[官方 exact-v1](https://arxiv.org/html/2604.22169v1) 的核心不是“又一项推荐任务提升”：§2–4 在离线单目标 next-item、稀疏二元 hit reward 下，把 `G` 个 rollout 的**搜索宽度**与实际进 actor old-log-prob/ref/反传的**更新宽度**分开。全零组用可由目标输出构造的正 anchor 替换最低结构分项，再以任务命中最强正例和结构接近的 hard negative 作两项局部更新；没有合法负例时跳过。task reward 与结构分数分权，后者只作组内选择。方法只改组内信号构造，不能由此声称无偏、保持原采样分布或普遍适用在线 RL。

[Ch33 GRPO](../../../../../books/part-04-training-system/33-grpo.md) 已有全零组、Dynamic Sampling/固定边界 anchor、SFT↔GRPO 分支，以及 `G` 增大提高生成/评价/存储成本。但现文尚未把“扩大搜索可能有益，却未必让所有 rollout 进入 actor 更新”作为同一状态/成本合同解释；这使此项越过仅能映射章节的准入线。建议恢复为本窗 **候选**，初判 `Design Delta 2 + System Reach 2 + Durability 2 = 6`，标准审阅；Books 暂待作者核对原文与邻章后再作独立写前判断，不能以本记录直接改为 Integrate。

证据边界：§5.1 的五项 RecIF-Bench 任务、Qwen3-1.7B 主模型，scale 1.7B/8B/14B，64 Ascend NPU 同硬件比较；§5.5 的 8B、`G=32`、相同 OpenOneRec pipeline/初始化和预算下，step `371.54→77.00s`、actor update `211.04→12.71s`，且 old/ref/actor 前确实物理过滤非活跃样本。性能变化主要由进入 actor 的 token 减少，不可把 16.6× actor 数字当 end-to-end 加速、跨硬件结论或质量/SLO 保证。插入的 ground-truth anchor 与自采样 rollout 不同来源；若要写进 Books，应说明 producer/behavior-policy 身份和潜在 off-policy/selection bias，不能把这一步描述为普通 on-policy 采样。可靠 target/结构语义和离线标签是必要条件；缺少它们时普通 GRPO/Dynamic Sampling 仍成立。

原 arXiv v1 页标 2026-04-24（提交/版本日）不自动证明 04/27 窗口首公开；作者须继续按该日官方公告批次、相邻 ID 与版本记录的组合核日期。只在这个归属成立后计入本日冻结分母。当前裁决是**恢复待日期确认的贡献候选**，不是整日日报完成。
