# 11513 当前更新稿的必要证据与 Books 判断

root 2026-10-09实际读[作者 Zenodo 原件](https://zenodo.org/records/18870116)：同作者/标题，2026-03-05 v1 已有 split、oracle 和 distraction 主张。当前[精确 arXiv v1](https://arxiv.org/html/2603.11513v1)及官方 Comments 明确为 updated draft；不能以新 ID 重计论文首次公开。这里只审当前稿，不无差别比对旧 PDF。当前事件公开日由作者本日已有日期原件确认后，才进入正式候选表；不重复计算家族分数。

## 当前稿支持与不支持什么

实际必要范围：§3–7、Tables 1–7及统计 Appendix C。小模型检索利用率是有意义的评价线索，但 gold 字符串出现不等于充分证据，Known/Unknown 是基线输出标签而非参数知识真值。Table 5 的负净收益是 noisy retrieval；§4.4 的 7B oracle 净收益为正，不能说全部 RAG 都有害。§4.3/C 的 p=.003 不满足本稿声明的 α=.002；未显著也不证明质量没有影响。三 prompt 只覆盖 3B dense pilot；Groq 8B 无 oracle 对照，架构/精度/backend 共同变化，不是隔离量化原因。误差启发式不直接测量注意力或因果利用；约 1B 阈值与更大模型需求不作长期结论。

模型/负载边界见 §3/Table 1：本地 NF4 double-quant T4，与独立 Groq FP16 分支；英文 NQ/HotpotQA、小 Wikipedia 切片。未披露的长度、并发与 SLO 不补造；不采用生产性能数字。未核 artifact、未复现实验。

## 具体 owner，不按主题直接 No Change

实际顺读 `AGENT-RAG` [Ch76 RAG不消除Hallucination](../../../../../books/part-07-agent/76-rag.md#rag-不消除-hallucination) 的完整局部，并读 Ch75/77 入口。现有正文已解释：证据出现与因果使用不同；操作性知识标签不是 latent truth；需要分别测 baseline-correct 保持与有益 context 利用；回退成本与拒绝有益证据并存。上述可安全采用的评价命题已被具体承载，不缺机制 owner。当前稿的普遍瓶颈、阈值及因果归因不被必要证据支持，不能用扩大结论制造 Books 增量。

建议最终处置：当前更新事件深入审阅后 **已有覆盖**，Books 新写 0；报告保留具体统计与对照反侧，不能称所有作者结果已证实。待非 root 实际必要 Source/owner 复核后同步正式日报；本包不授日级验收。
