# 04/27 Ch76 UAE / BERAG 有限非作者写后复核

范围：仅核已写入的 `2604.22722v1` UAE 与 `2604.22678v1` BERAG 两个 Source Family、Ch76 实际段落及 UAE→ResRank→BERAG 的相邻论证；不替代 04/27 来源、日期、分母或日级 Gate，也未复现实验。审阅者 apr02 未写本次 Ch76 正文。

## UAE：正文写后 PASS

Primary：[官方 exact-v1 HTML §2.1–2.2 Eqs.1–5、§3 Table 1](https://arxiv.org/html/2604.22722v1)。效用以指定 reader 对参考答案集合的长度归一 token likelihood 定义；先以候选效用顺序训练 pairwise reward proxy，再对候选集合的 softmax reward 分布做双塔 KL 蒸馏，线上标准 ANN，不运行 teacher。Ch76 `Reranking 与 Context Packing` 开头约 286–288 行的新增两段准确区分离线训练目标与在线第一阶段检索，不把 embedding 分数升格为事实支持概率。Teacher、参考答案、候选集合与重建索引的版本职责和替代 baseline 均就近保留。

Table 1 中 UAE 在 QASPER 的 R@1/Gen-F1 为 48.15/27.0，低于 SePer 的 59.84/32.6；NewsQA 亦非所有指标领先。9 ms 是作者设置下检索阶段延迟，非离线 teacher、重索引、下游生成总时延。正文的受限表述正确。当前 Ch76 接下来的 ResRank 区分共享 encoder 的 recall 与 rerank 两种责任，UAE→ResRank 由检索目标进到两阶段协作，衔接成立。

## BERAG：正文写后 PASS

Primary：[官方 exact-v1 HTML §3 Eqs.2–6、§4.8 Table 6、Limitations](https://arxiv.org/html/2604.22678v1)。每文档条件化同一已生成 prefix、学习先验、以 token likelihood 更新文档后验并混合下一 token 分布；后验不是事实充分性或跨文档支持保证。Ch76 `文档也可以成为独立生成分支` 约 329–331 行准确表达生成状态的另一种组织方式，并承接 ResRank 后的 context packing/evidence-set 讨论。单文档 singleton mixture 不显式枚举联合证据集合；作者仍观察到部分跨文档合成，正文未误写成绝对无法合成。

Table 6 在 E-VQA K=50 下标准拼接 RAG 203.0、naive BERAG 470.2、Top-P 44.4 ms/token，只测受限 decode；正文正确保留多份 KV/重复 query、剪枝误删、BEFT 训练、prefill 与吞吐/生产 SLO 未证及拼接回退。该结果不能被表述成端到端或通用吞吐优势；现文未作此越界。

## 交接与剩余同步

实际正文两组机制与相邻主线通过有限写后复核。`git diff --check -- books/part-07-agent/76-rag.md` 通过。核查时 Ch76 两组 Source Family 标记只出现在正文约 286/288 和 329/331 行，尚未找到章末对应 Review-note 条目；请 Books 写者补齐源/写后记录，并由 04/27 作者将 `V3_EVIDENCE_REVIEW.md` 的“待写前/待实写”同步为实际 Integrate 与本审计范围。此流程同步未完成不等于正文机制不通过，更不构成 04/27 日级 Gate。
