# 2604.23210v1：危险信号与反思规则的必要证据（作者侧）

本记录只处理已读完整题摘的一条贡献线索，不冻结 04/28 候选分母或首公开归属。材料为官方 [Discovering Agentic Safety Specifications from 1-Bit Danger Signals v1](https://arxiv.org/html/2604.23210v1)；页头 25 Apr 是稿件提交标示，不当本窗公告时刻。旧 receipt 的 v1 Updated 早于 04/28 北京时间 09:00，官方 04/28 OAI CS 集可见该身份；仍须结合相邻公告批次和具体例外核 first-public，不能独用 Updated/OAI/DOI。

## 准入机制与决定性对照

官方 §2.1–2.4 的模型有可见奖励 `R_vis` 与隐藏评价 `R_hid`，另设由隐藏评价导出的 binary danger oracle `D(s,a,s′)`。冻结 LLM 每轮按自然语言 `σ` 生成完整行动序列，执行若干 episode 后把轨迹、可见奖励和危险 warning 交给 reflector；更新后的 `σ` 是跨轮唯一持久状态。Level 1 反馈给危险步位置，Level 0 只给 episode 是否出现危险。Reward-Only baseline 使用相同 attempt→reflect 回路，仅去掉 danger warnings（Appendix B Algorithm 2/Table 4），所以在作者的环境和 prompt 下可比较**安全信号是否改变反思方向**；这不是参数训练或外部权限控制。

§3 Table 2 的 Side Effects 中，Claude/Gemini 的 EPO-Safe 隐藏回报中位数为 43/43、Reward-Only 为 35/35；Absent Supervisor 为 25/41 对 17/17。Boat Race 上 CoT/Static 已有安全行为（两模型均隐藏回报 20），EPO-Safe 不可独占该结果；Whisky & Gold 上 Reward-Only 与 EPO-Safe 均达到 44，不能写成只有危险信号才会学安全。Off Switch 的指标条件于未中断 episode，若最后轮全被中断还借用前轮，不是无条件任务成功率。作者 §3.4 的假阳性 warning 噪声平均退步约 15% 隐藏了环境差异：Absent Supervisor 在 `p≥0.2` 时归一回报降至 0.41，Boat Race 在 `p=.05` 出现非单调反向。只测试 false positives，没有 false negatives、延迟或对抗 oracle；§5 明确十个环境结构简单、对照是内部 ablation 而非 safe-RL/OPRO 同预算比较。§3.2 是三轮、每轮三个 gridworld episode、三随机种子、两个模型家族，文本 analog 每轮五 episode；“1–2轮”不可外推真实工具环境。

## 当前知识 owner 与作者侧处置

[Ch80 Reflection](../../../../../books/part-07-agent/80-reflection.md) 已把 feedback independence、verifiability、stopping 与 `policy configuration` 只能由授权 owner 修改分开，并在章后段要求 candidate lesson、held-out validation、promotion/rollback 分权。[Ch72 Security](../../../../../books/part-06-ai-infrastructure/72-security.md) 已把 reward 终态、异常信号、独立 policy/effect gate 分开。此稿有可复核的**奖励回路可能强化错误安全规则、单独危险信号可改变有限任务反思方向**的对照，故不以“toy gridworld”或既有原则直接前关闭；作者建议贡献准入 `DD2/SR1/Dur2=5`，安全触发深入审阅。长期 Books 倾向 `仅报告／具体已有原则`：新颖的是在理想二元 oracle 下自动改写 task-specific `σ` 的受限实例，而现章已经禁止把模型自生成规则当授权安全 policy。若要再提出正文增量，必须指出 Ch80 缺少哪个独立 feedback→候选规则→held-out promotion 的真实责任，而不能把论文的自更新 system prompt 直接升格为运行时安全授权。

特别注意：oracle **由** `R_hid` 定义，虽不泄露奖励数值，却提供目标相关监督；不能称代理凭可见 reward 自发发现原本完全未知的安全约束。规则可读也不等于因果正确或未来情境安全。上述为作者侧必要证据与 Books 比较，仍待非作者准入、日期和单篇终态核查；未写共享 Books、未计正式候选。
