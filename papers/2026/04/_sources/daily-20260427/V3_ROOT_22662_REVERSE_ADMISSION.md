# 04/27 负侧独立准入复核：2604.22662v1

复核者 root；非 04/27 日报作者。只裁决这项旧前分母关闭是否成立，不签整日 Gate。实际复读[官方 exact-v1](https://arxiv.org/html/2604.22662v1) §2.1、§3.1–3.2、§4.2、§5.1–5.3、§6/Limitations，并对读 `PLATFORM-EVALUATION-SYSTEM` Ch66 的“解释对象、受众、evidence、release owner 分责”段。

旧“只有 measurement/context”关闭理由不充分。作者在统一 amortized 计算/固定界面下比较八类 Shapley 语义，以无解释条件为对照，37 名参与者、3,735 次受限 tabular risk case review 分别测量客观判断准确、时延、主观清晰度与信心。该设计至少提供了一个与本项目评价合同有关的反例：解释 proxy 或更高信心不能自动替人类决策效果背书。Table 3 的若干解释条件提高信心，但准确率没有稳定改善；这是**该受限研究的无可靠改善证据**，不是证明所有解释在任何 AI/LLM 系统都无效。五数据集、低时延 tabular 风险工作流、37 人和受控界面限制了对 LLM 解释、长期行为与真实组织治理的外推。

准入改为保留、建议 `Design Delta 2 + System Reach 1 + Durability 2 = 5` 标准审阅，唯一 owner `PLATFORM-EVALUATION-SYSTEM`。Books 暂建议**仅报告**：Ch66 已要求按解释对象与受众分别定义 evaluator，且不能把 attribution proxy 当发布授权；但目前未明确“confidence 上升与 objective decision 不同步”的人机验收轴。要不要把这条原则写进正文，仍须日报作者完成与相邻 Ch66 的实际 gap 判断，并核是否有直接 LLM/Agent 证据可承载，不可凭 tabular Shapley 的局部统计写成通用结论。旧前关闭应撤销，日期需独立确认，不能把此单项准入通过当 04/27 分母冻结。
