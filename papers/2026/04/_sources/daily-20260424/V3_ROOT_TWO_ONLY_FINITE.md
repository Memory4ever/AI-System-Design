# 2026-04-24：两项仅报告候选的有限非作者复核

复核者：root；2026-09-29。范围仅为 `2604.21611v1` 与 `2604.21268v1` 的必要机制、评价边界、Books 判断；不替代整日来源、日期和候选分母验收。二者均复查官方 exact-v1，不沿用报告作者的结论作为证明。

## 2604.21611 — Verbal Process Supervision

- 原文 [§3.1–3.3、§4.2–4.4](https://arxiv.org/html/2604.21611v1) 的 actor 参数固定；强 supervisor 给逐步文字批评，actor 在下一轮条件生成中使用它。这是 inference-time 反馈粒度与调用预算的实验，不是参数更新、可执行局部 reward 或已证明的 fixed-point 收敛。
- 比较并未证明全成本等价：SC@5 约匹配五倍 actor token 而不调用 supervisor；Reflexion 使用同一 supervisor 但只给 outcome critique；未列逐调用完整 token、硬件、wall time。Table 2–4 的轮数并不单调，强 actor 在若干组合中被批评后退步；Pearson 相关不能识别唯一因果。单次实验与小题集的准确率不外推为部署成功率。
- 对读 [Ch80 Stopping Policy 与选择性 critic](../../../../../books/part-07-agent/80-reflection.md)：该章已经明确无限反思成本、critic 误判、ECR/EIR 与 verifier/预算拥有停止权。本文给 step-level verbal feedback 的受限案例和 actor–supervisor 配对压力，但不足以改写默认设计为“每步调用强 critic”。`仅报告`成立；不宣称论文全部细节已入书。保留原候选与六分、必要审阅。

## 2604.21268 — GUI Propose-then-Critic

- 原文 [§4.1–4.3、§5.1–5.4](https://arxiv.org/html/2604.21268v1) 用同一 MLLM 的两个 prompt 角色生成一组屏幕坐标、渲染 marker、再排序选 top-1；训练时 proposer 的准确度/覆盖与 critic 的 top-1/NDCG 分开给 reward，EMA 表示训练成熟度，不是 critic 正确性证明。
- Table 2 的 Oracle@5 是“至少一个坐标进入 GT box”的候选覆盖上界，Top-1 才是最终选择；两者都不证明点击后的任务完成、动作权限或安全。几何对照需要八次独立生成，与一轮多候选加一次 critic 的 token/wall-clock 预算并不相同；不同切片存在低于原模型的结果。因此作者的局部 GUI grounding 改善不能升级为一般 Agent 可靠性结论。
- 对读 [Ch33 的完整回答组与同回答候选集分账](../../../../../books/part-04-training-system/33-grpo.md)及 [Ch78 的工具调用与真实反馈边界](../../../../../books/part-07-agent/78-tool-calling.md)：共同训练/候选内 credit、proposal 与执行权的长期设计分界已经存在。GUI marker/ranking 是受限实现案例，未建立需修改通用训练或工具权限结论的独立合同。`仅报告`成立；不把 Ch33/78 说成完整覆盖这篇方法。

两个核验仅关闭对应 `仅报告` Books 处置的独立语义问题。首次公开日期及全日负侧准入仍按本日报其他记录处理；未据此标记 Daily Complete。
