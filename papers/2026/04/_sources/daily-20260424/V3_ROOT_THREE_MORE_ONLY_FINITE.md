# 2026-04-24 三项标准候选的有限非作者复核

复核者 root，2026-09-28。只审下列家族的贡献、实验分母和具体 Books 处置；不替整日报冻结候选或验收所有来源。均读 arXiv 精确 v1 的决策相关正文，并对照实际 owner；未复现。

## 2604.21765v1 PrismaDV

[官方正文](https://arxiv.org/html/2604.21765v1) §4–6 将数据 profile、下游任务代码的数据流、隐含假设和可执行约束分成不同责任，§5.2–5.3 的 failure precision 只在约束失败时提供有用反馈；任务成功且约束通过不能证明它能捕捉新错误。旧的人工测试/静态列约束在任务稳定时简单可审计，联合 prompt 更新与受限失败反馈增加生成、调用和维护预算。EIDBench 的 60 项任务由 LLM 辅助生成并人工检查，包含 ML 与非 ML 任务；这不是大模型训练数据流水线的独立生产验证，也不能把训练 proxy 的非降等同于新任务收益。`AGENT-WORKFLOW` 的候选、失败反馈和独立 evaluator 分权已有通用论点；本篇提供具体数据校验 operating point，但证据不足以改写 AI System 数据责任或将其算法设为默认。2+1+2=5，标准审阅、仅报告；非作者必要命题复核通过。

## 2604.21611v1 Verbal Process Supervision

[官方正文](https://arxiv.org/html/2604.21611v1) §3 的 actor 权重固定，由 supervisor 给 step-level 文字 critique，随后条件重生成；它不是梯度 RL，也不是执行环境的局部 reward。旧 episode-end 反思调用少，在错误可整体定位时合理；逐步 critique 换来更细反馈，也增加强 supervisor 的调用与错误反馈风险。§4/Table 5 中 SC@5 的“matched compute”仅近似 actor token，Reflexion 使用同 supervisor 但全调用/硬件/费用未完全配平；强 actor 在某些 pair 下变差，固定点措辞没有可验证的普遍收敛前提。`AGENT-REFLECTION` 已具体区分 critic 介入价值、反馈真值和额外预算；这组受限 pair/任务实验没有形成需要另改长期正文的结论。2+2+2=6，标准审阅、仅报告；非作者必要命题复核通过。

## 2604.21579v1 Metamorphic Testing and Memorization

[官方正文](https://arxiv.org/html/2604.21579v1) §III–IV 在语义保持代码变换后重测程序修复；原始至少一次能修复的 bug 才进入该比较，闭源/开源采样数也不等。Defects4J 的下降与 GitBug-Java 平均较弱的结果需分开；原输入低 NLL 与变形后下降的关联不能识别训练泄漏，也不能证明 patch 语义正确。旧只测原 benchmark 容易漏掉表面敏感性，但增加变形、执行与白盒 NLL 读取也引入成本和只适用于开放权重的分支。`PLATFORM-EVALUATION-SYSTEM` 已明确污染因果归因需要主动暴露干预；本篇只能作为受限黑盒稳健性诊断，不应以关联推翻该证据门槛。2+2+2=6，标准审阅、仅报告；非作者必要命题复核通过。

三项都没有据名称或 ROADMAP 映射直接写入 Books。日报的其余候选、日期例外和来源缺口仍需单独验收，当前状态 `进行中`。
