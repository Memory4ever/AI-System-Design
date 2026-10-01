# 2604.26197v1 HLTM：Ch77 写前有限采用包（未授权、未实写）

窗口身份仍按本批官方公告槽、连续 ID 与邻界作 `[04/30 08:00,09:00)` 北京的有据推断，不把 arXiv 页面 `Submitted 29 Apr` 当首次公开。本文件仅供非作者 source→actual-owner 采用审阅；不改变当前 33 家族暂定工作数或正式 Books Decision。

## 最窄新增命题与实际 owner

官方 [exact-v1](https://arxiv.org/html/2604.26197v1) §3.2 把项目—招聘席位—组织等稳定业务实体定义为树节点，不是按 embedding 聚类造语义簇。§3.5.1 在查询 identity 对应的 subtree **先作 hard candidate filter**；§3.7 修改 leaf 时只重建该 leaf 及祖先聚合。因而拓扑同时决定授权候选域、多粒度聚合域和失效重算域。现 [Ch77 Memory](../../../../books/part-07-agent/77-memory.md) 在约 245–266 行分别讲 `ACL→coarse candidate`、graph/hierarchical index 的适用条件，在 445–461 行讲逻辑 revision 与物理 relocation，后文讲 supersession/deletion；这些并未将**三种域由同一稳定业务层级绑定**作条件性索引选择。唯一 owner 为 Ch77 的 retrieval/index 演进，不另写 Ch76 的普通文档检索或 Ch84 的权限策略。

建议在 Ch77 “Embedding top-k…graph/hierarchical index…”段之后、Memory retrieval evaluation identity 之前融入两段（仅 literal 提案，未写共享书稿）：

> 当 Memory 已有稳定的业务实体层级，索引拓扑还可以服从授权 scope，而不由 embedding 相似性聚类决定。以项目、席位、组织等实体作为节点，查询先凭独立的身份策略限定可读子树，再在其中组合 facet、可回答问题和 summary 视图检索；一次叶子更新沿该业务树重算祖先。这样同一结构同时规定候选可见范围、多粒度聚合范围与增量失效范围。它不是“树形摘要保证隐私”：身份映射、ACL 修订、跨实体关系与原文事实仍由各自 owner 验证，不能让聚合节点或向量排序越过授权过滤。
>
> 稳定层级、多层重复查询和频繁局部更新时，离线聚合可换取较短在线读路径；代价是 LLM 聚合可能合并或删去细节，祖先重算随层数与更新频率放大，scope 迁移/撤权还要处理旧索引和缓存。原来源所谓“lossless incremental”只比较同一规则下的更新索引与 full rebuild，不等于摘要无信息损失或授权变更自动传播。业务层级不稳定、跨 scope 查询多、原文真值要求高或低复用时，先过滤的 flat authorized retrieval 与原文回读仍是合理基线。

## 必要原文、反例与停止点

- §3.2、§3.5.1、§3.7 支持同一业务树的 scope/rebuild 机制；§3.4 允许 parent aggregation 时可选 prune 低显著细节，故不能把“lossless”提升为 source fact 保全保证。§4.8 是作者隐私讨论，不是动态 ACL 或重置缓存的形式化证明。
- §4.1/4.5 的主 benchmark 是 120 queries、50 documents，参考答案由三人多数票；表 2 中 retrieval precision 为 RAG `.774`、HLTM `.761`，recall 为 full-context `.831`、HLTM `.757`。不能写为所有召回/精度维度最优。作者另称生产部署，但该表并非百万文档生产 tail-latency 或删除事故率证据。
- 采用判据：非作者应确认本章尚无同一业务树承担 `authorized scope + aggregate region + invalidation frontier` 的实句。若已有，按具体命题 Existing 或 Report Only；若三者绑定确属空缺且原受限范围可保留，才授权上述窄正文。无需重读整篇附件或展开所有引用文献。
