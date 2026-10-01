# 04/20 否定侧第二轮：几何风险信号与联合幻觉监督

复核者：root；日报原作者：apr20_resume。2026-09-28。按当前研究合同的贡献问题，重新打开 exact-v1 的必要方法、直接对照与实际 owner；这里判断的是能否进入本窗候选，不把准入自动写成 Books，也不声称全部负侧逐篇复核。

| Family | 原判断与独立裁决 | 证据边界和 Books 对读 |
| --- | --- | --- |
| [2604.15376v1 Zoom Consistency](https://arxiv.org/html/2604.15376v1) | **恢复为 2+1+2=5，标准、仅报告。** 原“只是局部几何 sensor”把局部性当排除门槛。§3.2 的两步 crop 坐标映射，在目标仍在裁剪区且第二步定位正确时，第二次预测离 crop center 的距离可估第一步误差；这是已经执行双步定位后无需再增加同模型 forward 的备选风险信号，确实改变可试验的 sensor 选择。 | 条件破坏时（目标出 crop、第二步错、边界 clipping）等式不成立。§5.3 的跨模型 router 80.9% 对 80.1% 且 McNemar p=.19，另需第二模型调用；它不能称免费端到端路由、可校准事实概率或可靠提升。Ch23 的主动 crop 与 evidence sufficiency 已分权，Ch66 的 sensor/发布权亦已分开；本篇弱且受限的信号未改变现有长期断言，故不强加正文。 |
| [2604.15945v1 RAGognizer](https://arxiv.org/html/2604.15945v1) | **恢复为 2+1+2=5，标准、仅报告。** 原“检测头加 LoRA 是成熟多任务监督”忽略了 post-hoc 冻结 probe 与联合训练时检测 loss 通过 hidden state 更新 adapter 的具体设计分支；§3.2–3.3 与 Fig.3 直接给出状态和梯度责任，值得审阅而非标题级关闭。 | §4.1/4.2 的 AUROC 与回答指标只属于作者的闭域数据、模型、标注和切片；Text FT 使用 golden answer，而联合训练使用生成回答的带标签样本，不是只改 BCE 的严格配对消融。Llama2 的 language-quality/relevance 退步、NoCtx 69.26 低于 HallucinationProbes 72.29、标注/judge 与 group split 未充分外审，不能把内部检测概率当 truth 或生产 release gate。Ch29 的训练目标分支及 Ch66 的 sensor/评价权限已经说明一般责任；本文尚未提供足以改写两章结论的隔离因果和迁移证据。 |
| [2604.15400v1 Trajectory Commitment](https://arxiv.org/html/2604.15400v1) | **维持具名前关闭。** 同 prompt 正误 bifurcation 和 hidden-state patch 是真实干预，不因单模型直接拒绝；但最佳层间 87.5%/33.3% 对比不是同层配对或预注册层选择，matched-vs-random p=.056，24 cells 与多层搜索不足以把“幻觉是非对称 attractor”从解释性模型提升为稳定干预选择。 | 已有 Ch23/66 的可读性、干预、外部真值分离不因此改写；仅支持后续针对相同 prompt/layer/step 的待检假说。原文局部发现不删除，不能把未证明强机制说成已反驳整篇。 |
| [2604.15709v1 Bilevel Skill Optimization](https://arxiv.org/html/2604.15709v1) | **维持具名前关闭。** §3 将结构 edit、有效性/token budget gate、content bridge/refinement 与 MCTS 组成可实现搜索；不是因 Skill 或运筹任务被排除。但 §4 只有一个 ORQA skill，结构、prompt、轮数、optimizer 一起改变；没有结构搜索相对同预算内容优化或简单手工结构的分离证据。 | Ch83/84 已拥有 skill artifact、按需加载、编辑/验证/版本责任。本篇未建立这条既有责任之外的稳定结构选择边界，也不能由单任务小幅提升推通用 Agent skill 优化。 |

此次净恢复两项，工作分母从 `109/40/1` 更正为 `111 候选 / 38 贡献前关闭 / 1 首公开身份隔离 = 150 完整题摘`；26 真正写入、13 Existing、54 Only、18 争议。具体日期仍用官方公告规则、相邻 ID 批与原 OAI/版本联合推断，不能把 HTML 页眉提交日单独当首公开。该两项只有标准受限结论；若后续真实 matched 对照或跨域校准改变判断，定点重开相应 family。此文件不是整日 Gate；其余来源/负侧及正式报告仍需最终验收。
