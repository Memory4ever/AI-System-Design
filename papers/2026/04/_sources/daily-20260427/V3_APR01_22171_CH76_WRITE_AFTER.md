# 2604.22171v1 MCI — 非书稿作者写后复核

2026-09-28。复用本日具名 source→owner 审阅，定点再核 [官方 exact-v1](https://arxiv.org/html/2604.22171v1) §3–5、Appendix A 与 Ch76 现行 RBAC 分区→本次两段→predictive retrieval 邻接，以及章末 `SF-2026-ARXIV-2604-22171` Review note。没有复现实验，不替代整日 Gate。

**PASS。** 新正文将谓词无关的较密邻接/clique-cover、查询期可信过滤和多起点缓解诱导子图断连放在稳定 RBAC physical partition 之后，构成真实条件性索引选择；授权判断仍归 policy/filter owner，检索结果仍需最终验证。构建、位图或拒绝采样、低选择率/高召回 beam 成本与普通 HNSW/ACORN、稳定分区、小 allowlist 的回退并列，没有声称真实 ACL churn、动态更新、生产 RAG 质量或租户隔离已验证。章末注释准确限定 CPU/L2、合成 Zipf 标签及 Appendix A 的未来工作。`git diff --check -- books/part-07-agent/76-rag.md` 通过。

本项可以作为 04/27 第 33 项真实 Integrate；工作集合仍非冻结，来源、日期例外、否定侧及整日独立语义 Gate 仍由 root 另核。
