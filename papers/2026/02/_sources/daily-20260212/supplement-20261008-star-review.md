# 2602.09255v1 必要审阅（作者准备，Source待独立）

[STaR](https://arxiv.org/html/2602.09255v1)，Feb11/root AB已核；2+2+2=6，停止式冲突定点深入。旧topK caption容易同物体/时间重复→query预筛诱导局部3D primitive→任务语义分布JS邻接合并→每cluster代表caption+可回读keyframe，具体改变压缩在哪个集合上执行，不把新传感器/模块组合本身评分。

staroutline IV-A/B L91–147：task-agnostic三层memory与task-conditioned evidence分开；Eq1–2全history answer-equivalence是目标非保证。Similarity floor/null task/top-k概率proxy不等于真实任务充分统计量，caption遗漏会在第一high-recall门截断后续geometry/IB，不保证恢复。Eq4 MI after−before叫loss，再stop δ>barδ；原PDF page4完整提取确认同符号（不是HTML转写），greedymerge通常不增MI故不能采用原停止数值/公式正确性。source仅可支持query诱导子集上自适应cluster职责，request corrected sign/threshold/可核实现后恢复精确recipe，不自补正确式。

stareval V–VI L150–219：NaVQA210减22窗外、7sequences最长35.9min、WH-VQA100/22min；spatial correctness容差15m/5m、temporal2min，descriptive LLMevaluator，recall仅一个±5s timestamp非完整证据/精细navigation safety。相同scene记忆长度变化非全新任意hourlong任务；spatial gain也因3Dboxcenter vs robotpose，更不能唯一归因IB。没有去IB但同representation/预算的消融，30.1s/25tasks中14.2s answer与最多3plannerround，GPT4.1mini API费/precision/SLO/repeatsCI Not Disclosed，稳定平均不授asymptotic scaling。

真实Husky30tasks、Nav2预建map/teleoperation deliberate revisits/pre-explored environment限定；4090eval，3080memoryconstruct：quantizedNVILALite2B7.2GB+perception6.2GB，1Hz，keyframe4.3GB盘存不等于memoryfree。QA/targetlocation不是未知场景全任务自动执行；待actual AGENT-MEMORY/CONTEXT owner，原worldstate真值不归此。支持窄检索机制足，停止无关各例子。
