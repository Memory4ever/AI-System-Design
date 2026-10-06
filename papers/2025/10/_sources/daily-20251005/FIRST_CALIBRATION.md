# FIRST — 2025-10-05 作者首批

作者Huygens；待Curie/root非作者实际校准。窗口BJT `[2025-10-04T09:00:00+08:00,2025-10-05T09:00:00+08:00)`。不采用submitted/Atom published为first-public；本包五项均只是日期隔离潜力，不评分、不进入正式候选/正面Evidence/Books。

本日四个收窄主题查询原值在`arxiv-*.receipt.json`与`acquire.py`；26次命中跨主题去重24家族，已恢复各精确v1题摘。不是年度目录题摘队列。没有把小模型、局部实验或反面结果直接排除。

## 五个潜力

| 精确原件 | 原约束 → 原文增量 → 待重新考虑 |
| --- | --- |
| [EvoEngineer](https://arxiv.org/abs/2510.03760v1)，`abs-2510.03760.raw` | CUDA代码进化只追速度会产生错误kernel → 将correctness与性能约束耦合的进化框架及91kernel评价 → 成功率与速度的联合目标/验证预算。必要core已下载，尚待实际有限阅读，不借通用验证原则评分。 |
| [Step Pruner](https://arxiv.org/abs/2510.03805v1)，`abs-2510.03805.raw` | token罚不能辨识推理步冗余且诱发合并hacking → correctness优先的step reward与步长上限停止 → 训练节省与步骤语义/奖励投机边界。v1停止机制不能用v3的“不再变短”替代。 |
| [LIBERO-PRO](https://arxiv.org/abs/2510.03827v1)，`abs-2510.03827.raw` | 标准LIBERO高分未必说明任务理解 → 对对象/初态/指令/环境的四维扰动反例 → VLA评价泛化与动作记忆的可区分性；不先采纳普遍0%或因果断言。 |
| [CPS](https://arxiv.org/abs/2510.03612v1)，`abs-2510.03612.raw` | 偏好攻击研究常给白盒/整网页控制 → 仅自有listing图文编辑的跨模态偏好操纵 → Agent第三方内容信任边界与联合攻击评价。 |
| [Graph induction](https://arxiv.org/abs/2510.03611v1)，`abs-2510.03611.raw` | needle retrieval高分不能代表密集关系推理 → 分散文本诱导图的早期memory drift → effective context按关系任务而非单needle长度判断。 |

所有原件都有完整AB及submission history；尚缺完全落窗的官方公开公告/bounds。轻量当前页未见撤回/删除标记；版本史只记录身份，不以v2/v3号默认重要修订。

## 三个代表性关闭

- [DINO survey 03606](https://arxiv.org/abs/2510.03606v1)：完整AB是既有self-distillation/mean-teacher/multi-crop路线梳理与既有表现比较，没有识别新的评价盲区/机制差额；不是因综述类型本身排除。
- [A4FN 03829](https://arxiv.org/abs/2510.03829v1)：position将感知→意图→配置的既有Agent模式移植飞行网络，AB未说明新委派/执行/可靠性条件；不是按“领域应用”一刀切。
- [HCAA 03815](https://arxiv.org/abs/2510.03815v1)：Bayesian诊断+LLM仲裁+temperature calibration组合，领域accuracy/ECE提升没有揭示新校准机制/适用边界；若necessary安全core发现原判断受影响则定点重开，不能把trustworthy标题当安全保证。

作者后续工作已收束：有界标题补检18，共42精确AB、4贡献关闭+1管理员删除+37日期潜力，19必要安全/反侧/消歧core实际有限读完，详见SCREENING/CORE_BOUNDARIES与README。上表EvoEngineer“尚待阅读”是首批提交时状态，现必要§3.1/4.1/4.2末/4.3/5.1/A.7.1已读，五测试/计时局限已记。FIRST/DAY仍待非作者，不假定通过；42AB不等Evidence完成。
