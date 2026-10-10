# Jan28 retention 两家族 joint PRE — 尚待独立字面核

18261 v1作者已实际§2/3.1–3.4/4.1–4.2/Tables2–3，peer必要Source完成：NEW-task empirical diagonal Fisher→quantile rawgradient mask/output-neuron aggregate，与EWC old-task softpenalty区别。2+1+2=5，具体保护人口差额深入；不采α公式/文本矛盾配方、不授AdamW step保持。18255 v1作者实际§3/Alg1/4.2/5/Table1，peer实际完整必要Source：临时anchor短训collectgrad→SVD→reset→project rawnewgrad，再AdamW。2+1+2=5，具体anchor几何与中心structural-safety反侧深入；小最优grad不认证curvature、实际step未project、task反退/anchor预算未披露，不采do-no-harm。

Owner `TRAIN-SFT` Ch29。作者实际读888–917 continual regime→rotation→单refusal冲突SVD→EMA finaldelta mask→static base synthetic/output敏感性→softprompt protection全局部，Ch28小结和Ch30开篇。现有907–909承载当前batch EMA与最终delta，911承载synthetic base output，913–915承载最坏softprompt；没有NEW-task Fisher统计人口与真实anchor临时探测/恢复真model这两种来源分工。拟联合两段插于909后/911前，不追加论文标题或新节。

## 拟正文

保护分数来自哪一组数据，还应与“保护什么”分开。新任务样本上的 empirical diagonal Fisher 可以按分位选择参数，再按一个输出 neuron 的输入连接聚合成整行的训练资格；这与用旧任务 Fisher 为偏离原参数加软惩罚不同，也不能把新任务统计量直接叫作历史知识的重要性。另一条历史探测分支保留少量旧任务 anchors，在临时模型副本上短训、收集 LoRA gradients，以 SVD 提议保护基，再回到未被探测更新的真模型，把新任务 raw gradient 投影为 `(I−UUᵀ)g`。两者分别回答当前任务哪些坐标可训练、历史样本在当前参数附近建议避开什么方向，不是同一份“知识位置图”。<!-- source-family:SF-2026-ARXIV-2601-18261 --><!-- source-family:SF-2026-ARXIV-2601-18255 -->

数据人口、aggregation、anchor 覆盖、探测步数、子空间 rank 与 optimizer state 必须一起记录：新任务 mask 不认证旧任务保持，anchor gradient 也不等旧任务 Hessian 或全部敏感方向。屏蔽或正交化 raw gradient 只约束该 proposal；AdamW 的预条件、历史 moments 与 decay 仍可能使最后 delta 离开保护集合，有限步非线性损失更不由一阶关系保证。[Fisher-mask 的局部对照](https://arxiv.org/html/2601.18261v1)存在保持—可塑性权衡，精确保护比例的内文冲突不作配方；[anchor-projection 的四任务对照](https://arxiv.org/html/2601.18255v1)只有代码切片的有限结果，其他旧任务仍退步，也没有统一 anchor/训练预算。统计、临时探测与 SVD 付费；代理失配、实际 delta 漂移或 retention 回归时，保留真实 replay、较小更新、独立 adapter 或上一分支的最终 delta 锁定，而不是让 mask 或正交名称自签无遗忘保证。

## 拟自身 notes

每家族分别加自身note，Source/PRE/POST角色与实际范围；不提前写POST或DAY。
