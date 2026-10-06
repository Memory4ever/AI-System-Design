# 2025-12-26 非作者复核

复核者：主线程，非本日报作者 Feynman。
检查时间：2026-10-02T18:50:10+08:00。
窗口：[2025-12-25T09:00:00+08:00, 2025-12-26T09:00:00+08:00)。

## 复核范围

实际阅读本日 README、SCAN、ADMISSION 的停止点、36 项题摘准入判断和外部保留项。原始目录切片仅作为材料复用，按本日窗口重新比较，不继承 25 日候选或验收结论。另实际打开以下 exact v1 完整题摘及 Meta 官方说明；这些检查是贡献准入与风险检查，不冒称 34 项 potential 全部完成正文审阅。

| 原文 | 独立核验与边界 |
| --- | --- |
| [Code Injection](https://arxiv.org/abs/2512.21818v1) | coder/reviewer/tester 的防护与效率取舍；增加 security agent 仍可能被 few-shot 投毒。保留安全潜在增量，不把新增审查者当保证。 |
| [CoTDeceptor](https://arxiv.org/abs/2512.21250v1) | 多阶段混淆针对依赖语义推理的检测器；攻击效果必须绑定检测器、预算与数据，不推出所有 CoT 检测失效。 |
| [GateBreaker](https://arxiv.org/abs/2512.21008v1) | 路由定位与移除安全相关神经元需要模型内部访问和修改权限；不能写成普通提示词即可实施。 |
| [RoboSafe](https://arxiv.org/abs/2512.21220v1) | 近期轨迹回溯和长期预测共同产生 predicate；可执行代码不等于正确的安全条件或真实环境保证。 |
| [Few Tokens / EGA](https://arxiv.org/abs/2512.21815v1) | 按高熵解码位置分配攻击预算，反证均匀 token 重要性假设；没有采用跨模型普适攻击或孤立性能数字。 |
| [KL estimators](https://arxiv.org/abs/2512.21852v1) | 值估计与梯度估计、on/off-policy 条件必须分开；相同 KL 名称不保证相同更新目标，不泛化为所有框架实现错误。 |
| [Evaluation noise](https://arxiv.org/abs/2512.21326v1) | prediction/data/total noise 与配对测量影响采样预算；预算分配结论仍需要实际 workload 条件。 |
| [SWE-RM](https://arxiv.org/abs/2512.21919v1) | 相同 test-time ranking 表现不证明同样适合作 RL verifier；classification/calibration 需要另验。 |
| [1-bit output alignment](https://arxiv.org/abs/2512.21651v1) | v1 题摘支持跨层误差累积与朴素 output alignment 的失败；ADMISSION 的当前摘要提及 anisotropy，不据此冒称 v1 已给相同结论。 |
| [Agent code optimization study](https://arxiv.org/abs/2512.21757v1) | PR 中缺少性能验证是局部实证反例；不把代码合入或功能正确等同于资源效率提升，也不外推全部 agents。 |
| [DAM](https://arxiv.org/abs/2512.21567v1) | 实际题摘明确不是新算法。当前贡献前关闭有依据：未说明新增可执行机制、受控证据或具体失效边界；不等于所有理论重述都无价值。 |
| [Moxin variants](https://arxiv.org/abs/2512.22208v1) | 当前题摘主要是开放资产与变体及指标主张，没有新增机制说明。范围内关闭，不贬低开放资产本身。 |
| [Meta AdvGame](https://ai.meta.com/research/publications/safety-alignment-of-lms-via-non-cooperative-games/) | 官方完整题摘实际读到非零和 attacker/defender 联合在线 RL 与 pairwise preference reward；足以保留潜在机制，不足以证明控制收益、安全或效用 frontier。 |

12 个 arXiv 原文的 Submitted 字段均不作为首次公开。Meta 目录 Dec26 无时区/时刻，2512.20806v1 的 Dec23 提交也不能补齐。没有用后来版本的正文或性能主张替换历史证据。

## 来源与停止点

14 个 Daily 来源均有实际有限边界。三组 arXiv 80/42/44 有交叉，不能当 166 个唯一候选；完整月列表也只用于恢复相关身份。已读相关题摘不能被缺日期替代，但实际普通题摘差额已补齐，普通作者待办为 0。

独立确认可恢复的 Seed type1/type2 分开处理；type2 最新原始响应为 18 项、total45、next20、has_more=true，置顶与非置顶混合，不能宣称全局严格排序或完整历史。DeepMind 正确 `/blog/page/4/`、Google Research 2025 Blog 和 Anthropic Alignment 的有限 December 邻接均已恢复；撤销这部分旧隔离，不由此授予 publications、Anthropic 主 Research 或全站历史覆盖。

OpenAI、Anthropic 主 Research、Google publications、Qwen、Hunyuan、MiMo 历史或首公开缺口按 README 精确范围保留。检索失败不证明零事件；可恢复 Blog 也不替代未恢复的相邻源。

## Books 与完成条件

确认落窗候选 0，不等于潜在贡献 0 或零遗漏。34 项 arXiv potential 和 AdvGame 均保留身份、具体准入问题与日期重开条件；没有评分、没有采用长期命题，没有 Books 写入，也没有把主题相似伪装成已有覆盖。

本日无实际 Books 写入，因而没有待做的写入后复核。终态保留项不支持正面证据、Books 或无遗漏断言；只在收到逐 ID 官方首次公告、可靠首公开范围或原始历史目录时重开对应条目。

结论：通过

通过的是本日有限扫描、贡献初筛、隔离和完成条件的诚实性；不是全部历史内容、34 项正文、通用安全或性能的背书。机械校验另行执行。
