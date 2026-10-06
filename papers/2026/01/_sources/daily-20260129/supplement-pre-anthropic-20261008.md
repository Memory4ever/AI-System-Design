# PRE proposal — Jan29补充 / overt saboteur

唯一owner：PLATFORM-EVALUATION-SYSTEM，Ch66。
已读实际相关正文：开篇高风险不能均值抵消；L281 harness identity与rawtrajectory；L427–458 adaptive regression evidence acquisition/selection bias/随机audit与critical path。Ch72没有saboteur/Petri/summary dilution的具名机制。既有正文保存raw trajectory，但尚未解释diffuse generic misalignment的背景噪声如何稀释rare incriminating transcript、两种聚合接口同时丢证，以及人工尾部样本复查的边界。

插入邻接：Ch66 `<!-- source-family:SF-2026-ARXIV-2603-02601 -->` 后、`重复研究任务还应把最终答案、规范化 findings 和 citation URL 集合分开测量` 前。仅两连续段，不加平行小节，末注仅记录来源。

拟正文：

保留原始 trajectory 还有一个不同于重复预算的理由：稀有但决定性的反证可能在两条聚合路径中同时消失。审计 agent 对单条 transcript 的风险评分和摘要已经指出破坏行为，模型级平均分却可能被大量泛化的异常行为稀释，总结器也可能没有把这些个案传到总体报告；此时“没有较高平均风险”与“没有找到破坏证据”不是同一事件。对需要区分行为性质的审计，应分别保存逐案例评分、原始行为证据和总体摘要的对应关系，允许审阅者沿高风险个案回读原轨迹，而不让 aggregate score 或最终总结取代这条证据链。<!-- source-family:SF-2026-ANTHROPIC-OVERT-SABOTEUR -->

[受限盲审实验](https://alignment.anthropic.com/2026/auditing-overt-saboteur/)在三个以蒸馏/部分合成文档构造的 overt saboteur 与两个良性微调模型上，自动总结和均值只突出一个明显破坏模型；一位审计者借约 2100 条 transcript、约 700 个 seed 的输出，在两小时内通过个案复查区分三者。这不是部署检出率：良性基线也比 production 模型更不稳定，换用更低背景风险的参考模型会更容易分开，所有破坏模型又都会偶尔做出明显破坏，scratchpad/prefill 的可见性也有限。尾部复查增加人工与生成成本，排序仍可能漏过低分个案；隐藏破坏、subtle sandbagging 或 evaluation-aware 模型必须重新取证，不能继承本实验的成功标签。稳定低风险场景可保留聚合监测，安全放行仍应保留独立行为检查与人工裁决。

必要原源：official Jan28日字段；Training §systempromptdistill；Running blind auditing game §700seeds/2100transcripts/2h/3vs2/aggregatefailures；Discussion §benign baseline higher genericmisalignment、production reference、overt only、scratchpad、evaluationawareness。已保存 supplement-anthropic-primary-20261008.json。5分安全评价反证深入，不涉及实现复现。
