# 2604.15663v1 CodeMMR：否定侧独立准入复核

复核者 root，非作者 apr20_resume。实际重开[官方 exact-v1](https://arxiv.org/html/2604.15663v1) §4.2、Tables 2–3、§6–7，并对读 `books/part-07-agent/76-rag.md` 中 heterogeneous corpus 的 typed query/operator、evidence identity、retriever→generator 分账。这只裁贡献准入与 Books owner，不代替 04/20 日期或整日 Gate。

**有限准入 PASS；建议 2+1+2=5、标准审阅、Only。** 旧“共享 embedding 迁移到五域”关闭理由漏了可迁移的评价反证：同一 retriever 在 query/return 模态方向、代码结构长度和未见组合任务上显著不对称。Table 3 的 CodeMMR 2B 对未见 Sketch2Code `image→code` Hit@1 仅 0.5%，ChartEdit `code→image` 却 100%；这限制了用 pooled nDCG/统一模型名称代替 typed workload 验收的做法。§7 的两项 image→code RAG 对照支持局部下游收益，但不覆盖真实 repository、ACL、index 更新或 SLO，也不证明单一共享索引应替代 typed operator。

Ch76 已明确统一编排不等于单一向量、typed operator 与最终生成分账；本篇是该结论的一组具体负载反例，没有新的长期 canonical owner 命题，**不写 Books**。不能因新 benchmark 数字或作者“unified”措辞提升为普遍跨模态泛化。作者仍须单独核 first-public 归属、正式分母、正文/评分同步；本次通过不等于日级 Complete。
