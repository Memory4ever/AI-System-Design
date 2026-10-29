# Skill Is Not Document — necessary Source / owner / PRE

作者supp_20260604_author，准入日期R1通过。2+1+2=5，actual owner具体gap深入受影响部分。

## 必要Source

exact2606.03565v1。SUP_CORE...html为工具截断capture（含明文truncated，不冒完整），恢复后完整SUP_CORE_2606.03565v1_TEXT_20261024.txt（67844 chars），作者已读§1.3/2/3/4.1–4.5/5/A/B关键，reader R4已回原域，不重复已核层。支持与反侧足够停止。

§3：Qwen3Embedding0.6B InfoNCE召回与Qwen3Reranker0.6B crossencoder graded ListNet，GT3/SKIPpartner1/other0；SKIP不是评价GT，也不是一律0的负例。top20 rerank候选固定。§4.3/T7同上游pool比较才归因reranker，另一组baseline×baseline不当同pool。T10同backbone/超参数/协议比较：InfoNCE加入SKIP，Hit1/NDCG10/SetCompat均小退；rerank保grade分别+4.83/+2.18/+3.37pp而R10-0.42pp。不能从此证明全部biobjective无效。

AppB：共享L2 normalized e(s')在query q负分支梯度+ps'/tau e(q)，另query positive分支-(1-p')/tau e(q')；只描述向量上两方向拉推，不证明必抵消、CE普遍无损或容量上限定理。§1.3 relevance乘compat只是approx建模，不概率分解定理。SetCompat只在|GT|≥2上要求top-m包含完整GT；不是实际工具执行或安全，R@K本作allGT completeness非通常平均recall。AppA同top20内重排仍可伤R10，非truncation。

§2/limits：10246skills/41592accepted/32828rejected，LLM合成判拒+team专家核test并非独立生产oracle；中文skills仅246、少数方向约100query，train未全专家审，候选pool20固定。仅offline retrieval，无真实completion/总服务SLO，兼容labels或query/catalog漂移须重验。合成/清洗/标注、两stage训练、全库编码和线上召回rerank均付费；未核代码或复现。训练具体hardware未作采用命题，Not Disclosed（当前必要域）不补造。

## actual owner

已读Books三context/ROADMAP，actual Ch78“工具检索需要表达集合依赖，而不只是独立相关性”完整段及ToolQP完整后侧、Ch77末节proceduralgraph/Ch79开篇；Ch76已有relevance/utility rerank不拥有此工具集合准入/执行交接。Ch78已覆盖query-conditioned hyperedge/独立topK不足以及authority，不再次写为新贡献。gap仅：保留被合成器拒绝的组合记录→stage-specific graded监督及offline全GT top-m不认证真实执行；放在该节原25718 marker之后、ToolQP完整段之前。

## 最小PRE

完整上锚：

集合建模用组合可执行性换来更大的搜索空间、共调用数据依赖与 cardinality calibration；新工具、权限变化或 action schema 漂移会让历史超边失效。缺少可靠组合证据时，回退独立工具检索，再由确定性 schema/dependency expansion 补齐必需成员；工具集合很小或调用真正独立时，普通 Top-k 仍更透明。exact-v1 的 ToolBench 结果不证明 learned hyperedge 能跨长尾域或动态 catalog 保持有效。

<!-- source-family:SF-2026-ARXIV-2607-25718 -->

拟增两段：

组合监督也可以来自数据合成阶段被拒绝的候选，而不只来自成功共调用：保留合成器对技能组合的拒绝记录，再在给定 query 的候选池中比较将它放入共享向量召回目标，还是作为 cross-encoder 的分级排序标签。一条[受限 skill 检索分支](https://arxiv.org/html/2606.03565v1)把被拒组合中的 partner 放在 ground-truth 与普通候选之间，而不是全部当作零相关负例；在其固定配方下，分级信号改善 reranker，但加入 bi-encoder 的 InfoNCE 候选池略退。共享表示在不同 query 下同时被拉近与推远，只解释一种可能的几何压力，不证明所有双塔目标都不能学习组合关系。<!-- source-family:SF-2026-ARXIV-2606-03565 -->

验收还要把独立排名、整组覆盖与真实执行分开：要求 top-m 恰好容纳全部 m 个标注成员，只是一项离线集合指标，不证明这些 skills 当前能共同执行或具有权限。同一 top-20 候选池内重排也可能提高整组靠前的比例、同时损失较宽截断下的覆盖，不能用一个集合均值宣布无损路由。合成拒绝标签、人工审校、两阶段训练、全库编码与在线重排均需计费；标签依赖模型判断，或 query、catalog 与执行环境已变时，应保留独立相关性检索、显式依赖检查与真实任务回归，不把离线兼容代理变成执行许可。<!-- source-family:SF-2026-ARXIV-2606-03565 -->

完整下锚：

工具集合的 discovery 还可来自不同 subtask 或检索反馈产生的多个 query。若按每次命中加性累计，同一工具反复被找回会直接累加权重；一条融合支路只用该 tool 在任一列表中获得的最好 rank 汇总，不把重复命中次数直接当作额外支持。这不消除更多尝试获得极值的机会偏差，更不保证各 subtask 公平；须绑定原始 query/subtask、尝试预算、retriever 与 catalog revision。ToolQP 的局部 peak-rank 对照还低于 multi-view/reranker，不能授普遍最佳或免费高效。Query planning、各次检索、teacher/训练与汇总都计入费用；融合只改变候选发现排名，权限、schema、dependency 与执行正确性仍独立核验。预算或域变化下保留普通 Top-k/RRF、原 query 及确定性 dependency expansion，不从检索覆盖认证可执行链。

<!-- source-family:SF-2026-ARXIV-2601-07782 -->

Review note拟：`SF-2026-ARXIV-2606-03565`：2+1+2=5；exact-v1 §2–5/A/B/D.3，graded SKIP GT3/partner1/other0与stage-specific配置、top20内R10反退/SetCompat非执行；approx分解不当定理，未证全部biobjective无效。D.3先判组合，SKIP不生成query，partner映射不认证query条件兼容真值；LLM标签/team test审校/中文稀少与全部费用保留。未核实现或复现。待实际写后复核。

## A2 reader负侧定点修正已实际采用

作者回完整TEXT D.3逐原prompt实读：先给skill set，判WRITE才造query，SKIP只留reason并禁止再写问题。因此上段不再称原reject本身就是“在这个query下”的真值记录；§3把partner放进给定query训练池是proxy使用，精确映射当前必要域不认证为query条件兼容oracle。仅保stage-specific监督/评价边界，不因这一负侧改准入或冒全文不可得。
