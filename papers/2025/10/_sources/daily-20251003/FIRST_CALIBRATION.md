# 2025-10-03 首批独立准入校准请求

作者Huygens，不自审。以下完整精确v1 AB已实际读，原件[Atom](exact-v1.raw)。尚未确证first-public落窗；请求先校准贡献理由和日期隔离，不授正面Evidence。

| 身份 | 原有约束 → 实际增量 → 待核选择 |
| --- | --- |
| 2510.01565v1 TetriServe | DiT混合分辨率/期限下固定sequence parallel度低效 → 逐denoising step调整并行度、离散round联合打包 → 同质量约束下SLO与GPU小时取舍，而非Agent工作流调度 |
| 2510.03346v1 KVComm | 自然语言通信有信息损失/生成成本，hidden-state通信有集中偏差 → attention importance加Gaussian prior按层选KV对 → KV作为通信介质的选择性成本/质量边界，而非相似prefix缓存复用 |
| 2510.01656v1 AsyPPO | LLM大critic在稀疏reward/长轨迹下成本与偏差大 → mini-critics按不相交prompt shards训练、分歧用于advantage masking与entropy过滤 → 可计算critic和策略更新信号取舍；不是异步PPO/陈旧rollout算法 |
| 2510.02230v1 RLVR diversity | pass1提高常被当整体推理能力提高 → 多响应探测显示pass256可下降及多样性变化 → 最优单样本与覆盖率是否不同；保留局部模型/训练条件反侧，不因小模型排除 |
| 2510.02554v1 ToolTweak | 工具schema不变常被当调用界面稳定 → name/description搜索改变tool selection → 权限之外的接口元数据威胁；必要core仅有限检查、BSR不等恶意动作完成 |

代表排除（完整AB已读）：2510.01582v1 ImageNetThink是双teacher推理数据资源，题摘未给新的机制/评价盲区；2510.02243v1 AccurateRAG是加工/FT/评价流程及局部QA收益，未辨识组合失效或新增系统机制；2510.01553v1 IoDResearch科学知识探索属ROADMAP明确暂缓，并非按Agent标题强引入。

所有ID属于本日自己主题查询或有限相关标题补检，没有全年目录逐篇队列。需要root独立打开精确AB与日期史；其他普通筛选继续，不等待全部日完成。
