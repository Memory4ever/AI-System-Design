# 04/28 余下三项贡献歧义：作者侧有界准入

旧 111 个题摘行中尚无专用 exact-v1 消歧的三条为 `.23210/.23711/.24320`。已沿原完整题摘记录重核官方 `abs/...v1` 的题名、完整摘要与版本身份。本记录只解决**是否存在值得审的项目主线增量**，不预支结论可靠、首公开归属、评分或 Books；需非作者准入校准。

| Source Family | 作者侧贡献判断 | 精确增量、证据限制 |
| --- | --- | --- |
| [2604.23210v1](https://arxiv.org/abs/2604.23210v1) | 准入待独立校准；Ch72/80 | 一般 agent reflection 用可见 reward 解释行动，危险但高 reward 的状态可能反而强化错误规则；作者以每步 1-bit danger warning 为独立反馈，累积形成可检查的自然语言安全规范，并报告 reward-only reflection 反向。这至少给“reward 不拥有安全目标真值”一个直接对照，不是纯安全术语。范围只有五个 gridworld 与五个文字 analog；“1–2 轮学会”非真实工具环境的权限/安全保证，50% spurious warning 也不证明跨环境 noise robustness。 |
| [2604.23711v1](https://arxiv.org/abs/2604.23711v1) | 准入待独立校准；Ch72/77 | 私人上下文记忆在推理时可被单次或少量 query 的黑盒/灰盒 probing 提取，风险对象不同于训练语料 memorization；若在现有 output guard/拒答下仍可泄漏，需重新考虑 memory→model→response 的访问分母。须核 attacker 可见 prompt/memory 和目标信息来源、候选集合如何判成功、单 query 与 multi-ranked token 的不同权限；摘要的“bypass detection”不能自动等于绕过 effect authorization 或一般生产泄漏率。 |
| [2604.24320v1](https://arxiv.org/abs/2604.24320v1) | 准入待独立校准；Ch33/81 | 顺序 Agent 每步只在一个 environment 采样；作者让同一 policy 同时交互多个 environment、跨轨迹共享观察，并对并行动作与状态转移的重复度分别给 reward，可能改变 rollout 样本/环境身份与 credit 而非仅加 worker。须核 SFT 阶段、parallel trajectory success 与两种 step reward 的实际 ablation、相同 interaction/tool/compute budget；ALFWorld/ScienceWorld 的“效率相当”不能推一般任务或训练吞吐，不能把 reward 多样性当任务成功真值。 |

至此原 batch 文件里 **29 条 `继续核贡献`** 均有作者侧具名后续：本轮三个新身份、前两份[五项一](./V3_FIVE_CONTRIBUTION_AMBIGUITIES.md)/[五项二](./V3_SECOND_FIVE_CONTRIBUTION_AMBIGUITIES.md)共十身份；[末段 A–E](./V3_LATE_BATCH_FINITE_TRIAGE_A.md)等已有十三身份；`.23272/.23366/.23553` 三个已有具名前关闭提案在[第二批剪枝](./V3_SECOND_BATCH_CONTRIBUTION_REPRUNE.md)；合计 3+10+13+3=29，**不是 29 个正式候选**。其中晚段已有七条拟前关闭的数量与 70/41 工作漏斗重叠，不能重复扣减；仍须非作者校准、公告日期与正式证据审阅后才能冻结分母。
