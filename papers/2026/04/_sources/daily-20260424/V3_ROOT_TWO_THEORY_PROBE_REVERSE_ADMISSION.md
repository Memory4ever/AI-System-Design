# 2026-04-24：两项局部诊断的准入反查

复核日：2026-09-29；复核者 root（非本日作者）。原题摘回放收据已把 `2604.20923` 和 `2604.21286` 判为贡献前关闭，正式日报却分别列为 5 分“仅报告”。本次以两份 exact-v1、已有作者必要审阅和非作者方法复核，重新检查**能否改变本书长期 AI System 判断**；不删除任何已有实验/反证笔记。

- [ILDR 2604.20923v1](https://arxiv.org/pdf/2604.20923v1)：类间 centroid/类内 scatter 的几何比值，固定阈值预警 grokking，在 modular arithmetic 与 S5 小模型有受限预测价值；但其 Table 9 早停后 accuracy 可低至 7.1%，阈值和 seed 范围不构成训练完成/release contract。第 5 章已经区分“表示几何诊断”和“held-out 行为验收”。本项新增的是该代数任务的局部探针/操作点，而非跨模型可复用控制或纠正现有论点，正式候选应前分母关闭。原 `V3_EVIDENCE_NOTES.md` 和 `V3_ROOT_FOUR_TRANSPORT_EVALUATION_FINITE.md` 保留，说明其局部实验证据仍是真的；只是先前把完成源审读误作通过项目准入。
- [Cross-Entropy Is Load-Bearing 2604.21286v1](https://arxiv.org/html/2604.21286v1)：预注册 TinyConv/CIFAR-10、10 个 paired seeds 检查 predictive-coding energy probe 的 CE 输出假设。latent-movement 预设操作检查失败，结果主要隔离该探针在此小架构的 objective/logit scale 条件；不能推出大语言模型自我置信度读取或改变 Ch66 既有 scorer/calibration 比较合同。作者实验和有限反证保持有效，但没有本项目的直接长期设计 delta，转具名前分母关闭。原 `V3_EVIDENCE_NOTES.md` 与 `V3_ROOT_FOUR_MEMORY_AGENT_PROBE_FINITE.md` 保留。

两项均不继续追完整首发史，不在正式日报评分，也不进入 Books。若未来出现对 LLM 训练/推理或平台发布决策的直接、可迁移验证，按 Source Family 定点重开。这个改判不把所有理论或诊断论文机械排除；真正修正基础结论的反证仍可准入。
