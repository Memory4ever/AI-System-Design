# 2604.22171v1 MCI：否定侧定点重开

本轮只审这一家族。旧 receipt 把它归为“局部模型/优化方法、没有 ownership 转移”而前分母关闭；这不是决定 Ch76 物理索引选择的有效理由。本文件复核的是[官方 exact-v1](https://arxiv.org/html/2604.22171v1) §3–5/Appendix A 与 [Ch76](../../../../../books/part-07-agent/76-rag.md) 当前 Tenant/ACL、RBAC partition、SSD Filtered ANN 和 filtered planner 相邻正文；没有复现实验或检查实现仓库。

**准入裁决：撤销前闭，暂恢复 2+2+2=6、标准完成的贡献候选。** 既有 Ch76 的可信控制面负责 allowlist、kernel 前筛或稳定 role partition，SSD superset traversal 则在最终入选前验证 filter；它们没有区分另一种物理设计：把密邻接压成 predicate-agnostic clique cover，在查询时施加异构谓词，并用多 seed 应对过滤诱发的子图断连。若 metadata/permission 组合频变、逐谓词或逐 role 重建索引过贵，这改变“何时采用稳定分区 vs 查询期通用索引”的条件选择，而不是因为数据库论文能映射到 RAG 就自动入选。可信 ACL 决策、授权版本与最终证据 admission 仍属于原 owner，MCI 只提出候选检索结构，不取得权限真值权。

**必要原文与反证。** §3.1–3.2 从稀疏 k′-NN 图挖 clique cover/局部几何加密，最终索引不依赖过滤字段；§4.1–4.2 的多 seed/beam 在遍历时仅纳入谓词有效候选。种子覆盖是启发式，§4.1 的实用选择率至少约 `O(1/√n)` 并非任意稀疏 ACL 的完整召回保证；谓词昂贵时 §4.2 需预先评估全 n 个布尔值，或以期望 `ε√n/s` 的拒绝采样换成本。§5 用十个向量集、合成 Zipf filter、L2/CPU 16 线程的 Recall@10–QPS/index size/build 对照；不是 ACL 安全、真实高频 role churn、RAG 答案真实性或线上尾延迟测试。ACORN 在 spacev10M 的 85% 召回点为 2221 QPS，高于 MCI 的 1799；deep1M 从 99.08% 到 99.9% 召回需 beam 160→2640、QPS 1391→348。Appendix A 明说当前实现是静态构建，增删只列未来启发式，不能声称动态更新已证或不需重建。

**Books 写前采用：窄 Integrate，待 root 实写和另一人写后核。** root 已独立读官方 §2–3 与当前 Ch76:134–166，认可 predicate-agnostic 拓扑压缩及任意过滤后可达性为实际缺口。我是该日报作者但未写 Ch76，已另核 §4–5/Appendix A 与上述实际 owner；同意在 Ch76 filtered ANN 主线窄补一个条件性分支：旧 kernel prefilter/RBAC 稳定分区合理；当过滤组合变化且重建代价高时，clique-cover 可复用无谓词拓扑，多 seed 缓解断连；但过滤代价、种子/极高召回成本、静态构建与 ACL authority 必须同段写清。不能写成已验证 ACL churn、生产 RAG 收益或索引自身拥有授权决定权。本轮不自行写共享 Books，也不把候选恢复当整日 Gate。

**日期：** 原始 owner receipt 保留 `v1 Submitted=2026-04-24T02:48:20Z`、`v1 Updated=2026-04-27T00:15:04Z`、DataCite initial created `2026-04-27T01:30:49Z`、OAI `2026-04-27`。单字段均非 first-public；只与 Sunday 20 ET 官方公告/ID 赋号、相邻批次及 exact-v1 身份联合有据推断 04/27 08–09 北京时间，非逐篇公开日志。
