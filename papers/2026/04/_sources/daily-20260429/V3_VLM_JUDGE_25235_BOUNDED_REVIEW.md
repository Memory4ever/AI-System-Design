# 2604.25235v1：视觉 Judge 的排序与绝对评分分账

作者侧有界审阅，非独立 Gate。原始来源：[official exact-v1 HTML](https://arxiv.org/html/2604.25235v1)、[official v1 identity](https://arxiv.org/abs/2604.25235v1)。本篇属于本日 `24765–25918` 的官方公告批次联合链（见 [本日检查点](./V3_REOPEN_NOTES.md)）；v1 页的 `28 Apr 2026`/submitted **不是**单独的首公开时刻，若有更早独立正文公开仍须具名重开。它已在 106 份完整题摘、70 项潜在线索内，不增加工作池分母。

## 准入、评分和真实 owner

旧“VLM judge 可排序”主题本身不足以准入；本篇可检验的增量是：在同一视觉评价数据的任务切片里，排序相关性与可用的绝对评分区间不等价；若成立，EvalSpec 不能只报汇总相关系数，还需按任务和标注协议验收绝对分数的区间宽度、覆盖率与失效切片。这个局部评价边界与 [ROADMAP 的 PLATFORM-EVALUATION-SYSTEM / Ch66](../../../../../ROADMAP.md)、[Ch66 现有 Judge Ranking 论点](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)直接相关。Ch66 已经要求局部比较/全局区间、held-out judge–human residual、exchangeability、task competence、marginal 非条件保证与 release-owner 决策，不能把“首次提出 ranking≠scoring”或通用 CP 作为新 Books 缺口。

拟 `Design Delta 2 + System Reach 2 + Durability 2 = 6`：受限的跨视觉任务 EvalSpec 分账可能改变证据解释，既有 conformal 算法不是其贡献。按 6 分标准审阅；因**印刷有限样本保证和关键 boundary-adjustment 结果存在直接冲突**，仅对这些中央保证触发深入核验。拟 `争议／暂缓 Books`，隔离统计保证与不可信归因；保留有条件的经验观察，不把本篇当作 Ch66 的保证依据。不是整篇否定，也不要求遍历代码、其他版本或所有附录。

## 必要原文与可以保留的受限观察

- §3.1–3.3、§4：把 1–5 评分位置的五维 token log-prob 向量交给 R2CCP；MLLM-as-a-Judge 5,717 个实例/14 类，每例单标注；Polaris 8,726 个图文对、多个标注者均值、单一 captioning 任务。三位 judge、50/50 calibration/test、10 个随机切分、目标 coverage 90%。这些是作者实验条件，不是生产系统校准实现。
- Tables 1–3：三 judge exact accuracy 32.1%–34.2%；LLaVA-Critic 原始 R2CCP 平均 coverage `.900`、宽度 `3.05/4`，ChartQA Pearson `.507` 而区间宽度 `3.08/4`。AesBench `2.08` 对 InfographicsVQA `3.50` 显示切片差异；较高相关性不授予可信绝对分。Table 5 的 Mondrian easy 组边界调整宽度 `3.55→2.96`，hard 组 `3.63→3.78`，即相对分配 calibration burden，不是所有组同时更窄。Appendix F.3 的 GT=1 coverage `88.9%` 也提醒 marginal 不保证该切片。
- Table 7 的 `3.05→0.68` 宽度比较同时改变了任务种类、标注人数、标签形式、分数分布和 judge 在任务上的能力；不能从 `4.5×` 唯一归因于“标注质量”，也不能说换标注制度必得 4.5×。Appendix G.3 中 CoT prompt 相关性改善但 exact accuracy `33.9%→32.2%`，与“排序更好就评分更可靠”相反；不把其未控制的 token/logprob 路径说成唯一机制。

## 两项印刷保证的窄隔离

1. §3.2 Eq. 3–4 明写 `f(x)` 在 calibration set 上训练，同时用该 calibration set 的 nonconformity scores 取分位，并直接称仅凭 exchangeability 有有限样本 `P(Y∈C(X))≥1−α`。Appendix A.4 明确 R2CCP 两层 MLP 在 calibration set 交叉熵训练、随后同集阈值。常规 split-conformal 的秩论证要求阈值样本与已固定的拟合模型适当分离；印刷协议没有交代再次切分、cross-fitting 或可替代的有效修正。因此**论文所写协议不足以推出所称 distribution-free finite-sample guarantee**。这不证明作者经验 test coverage 数值必错，也不证明其私有代码一定复用了同一行；重开需明确拟合集/阈值集身份及有效性证明或可核代码。
2. §3.3 Eq. 5 后和 Appendix A.4 把所谓 boundary adjustment 描述为 `[l,u]→[ceil(l),floor(u)]`，同时称它“只扩张区间”并令覆盖率上升。对整数标签 `y∈{1,…,5}`，`y∈[l,u]` 当且仅当 `y∈[ceil(l),floor(u)]`，所以这项**印刷端点变换既不增覆盖，也不增宽**；但 Table 1–2 给原始 `.900/3.05` 到调整 `.981/3.60`。Eq. 5 还另写 nonconformity-score 调整，可能实际使用的是不同的构造，现有描述不足以还原该结果。只隔离“印刷端点变换解释及相关 adjusted coverage/width 的因果”，不声称实际实现无效或所有实验错误。重开需给可执行的边界变换、标签判定和复算输出。

## 当前处置

作者侧认为该家族具有项目相关的受限评价反证，不能因 CP 已成熟而前分母关闭；但**不能采用**印刷的有限样本保证、调整后 98% coverage 或“标注质量单独驱动宽度”作为长期正面结论。Ch66 已具体承载任务切片、judge–human residual、marginal/conditional 分账和 release Gate；在中央定量构造澄清之前，本篇不提供可信的新 Books 机制，拟 `暂缓`。待非作者核上述两点及既有 Ch66 差异；本篇通过不等于本日来源、日期或独立日 Gate。
