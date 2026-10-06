# FGR 的唯一 owner 与逐字 PRE

root 实际 Source 2+1+2=5 已通过。ROADMAP `AGENT-RAG` / `books/part-07-agent/76-rag.md`，现检索表示/完整MaxSim/router/多向量训练及Ch75/77交接已作者实际读。唯一差额：保原文档ranking，新增document-token→query relevance readout给span，index/compute取舍与positive-only no-evidence资格；不同于完整query-to-document检索或后LLM抽取。

完整左锚：

> 完整 late interaction 为每个 query token 寻找文档内匹配再求和，适合需要保留多种意图且可承担精排的负载；预算不允许消费全部 query views 时，另一分支用这些 token 表示训练一个 router，硬选单个 view 进入检索，而不是把它们平均或宣称仍计算完整 SumMaxSim。[受限路由原证](https://arxiv.org/html/2601.06389v1#S3)支持这条近似目标选择，不认证选中 view 对任意 query 都充分；其 STE 前后说明相反，不据此补完整训练 recipe。MS MARCO MRR@10 为 .372、完整 sum-max 为 .384；query30/document200、768维、10万文档/T4 的 112.04→14.48秒约8倍测量，不能写成30倍端到端加速或服务SLO。文档view存储的§3.2与§5口径未闭合，也不能凭单query view声称每文档常数单向量存储；router训练、encoder/索引构建与回归均付费。多意图、迁移或质量退化时保留完整多向量精排及单向量/hybrid基线，而不是让路由分数拥有答案支持权。<!-- source-family:SF-2026-ARXIV-2601-06389 -->

右锚现完整“单向量退化也不能只归咎于维度不够…”多行论证，保持全部。之间拟两段：

late interaction 还可以把“文档排得多高”与“其中哪些token对query相关”分开输出。保留原retrieval ranking，另让document token经过residual FFN后，对query tokens寻找最高匹配，再以sigmoid与span监督学习逐token relevance。这反转的是局部读出的消费方向，不是将原query-to-document求和分数当作每个span的证据；只用positive documents训练又偏向总找一个相关区域，不能由该head认证文档完全没有证据或所得片段充分支持最终claim。<!-- source-family:SF-2026-ARXIV-2604-00242 -->

[有限span对照](https://arxiv.org/html/2604.00242v1)中140个query/document pairs经三位human标注，局部F1较一个LLM抽取器略高但未证统计优势，retrieval recall仍可低于原ColBERT。选择在线计算新表示可不扩大既有index，却增加候选转换与读出；预计算则约需两倍index，不能同时领取零存储和零计算。单RTX3090/top100的组件时间不授完整RAG或生产SLO，参数计数冲突也不作为精确省费依据。span错位、negative-document支持缺失或完整预算不合算时，保留原retrieval score、原文回读及独立evidence admission/抽取，不将relevance或较小片段当事实、faithfulness或来源授权。<!-- source-family:SF-2026-ARXIV-2604-00242 -->

本人末静态注一条：`SF-2026-ARXIV-2604-00242` — Daily2026-04-03；[exact-v1](https://arxiv.org/html/2604.00242v1)§2–4/Tables1–2及必要0.A，2+1+2=5，仅document-to-query span readout与index/inline费用分责；不自补Eq4索引，保positive-only/no-evidence资格、recall/有限人评、110/140M冲突与全部费用，不授faithfulness/truth/服务SLO，未核实现/复现。

当前PRE及窄锁待核；不写其它Ch76family。actual后给root完整邻接和位置供nonwriter POST，不授DAY。

root实际全文PRE/当前左右锚通过并授两段+本人注锁；作者逐字落实Ch76 310/312（303–323完整邻接）及本人1762注，实际顺读/限定diff通过。root实际该处正文完整左右邻接/本人注nonwriter POST PASS，原ranking/反向span读出/positive-only资格和费用正确，旧段保留；锁释放，可同步真Integration，不授DAY。旧申请态只履历。
