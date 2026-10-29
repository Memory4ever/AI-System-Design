# 01542 SCP-HNSW：位置先验、索引度量与最终去重分责

root作者，仅06-03补Jun02自然日；R122–123完整v1题摘、同DOI/登记方/findable/registered及适用日程的联合日证复用，不改旧候选归属。访问2026-10-25 BJT。当前[官方v1摘要/history](https://arxiv.org/abs/2606.01542v1)所见唯一v1，无撤回/勘误说明；[exact-v1 HTML](https://arxiv.org/html/2606.01542v1)封面写August24，故定点打开[exact-v1 PDF](https://arxiv.org/pdf/2606.01542v1)：封面实际为June2，身份/v1标记、§2–3公式/流程、§6/8评价与限制一致。采用PDF上述必要域与HTML核心相合内容，不把HTML封面当重要修订或更改Jun02公告日，也不声称已核历史字节。未读完整引用、代码或复现实验。

## 必要机制与证据边界

单文档有序chunks，保存i与N，以i/max(1,N−1)得相对位置，附加半周期sin/cos两维并按lambda缩放后归一化。给定unit semantic向量时，第二次内积由semantic项与lambda平方乘位置差cos项组成，分母为1+lambda平方。第一次查询追加零位置项，从命中分数经softmax温度加权估计位置均值mu，再以有位置项的query查同索引；候选可取第二池或两池并集，重排选择未固定成单一已验证recipe。

HNSW构图/遍历算法未改，不等旧semantic图可不重建复用：索引向量、距离与图邻接都可改变。第一次零位置query的精确内积在unit条件下只是共同rescale，但近似图搜索仍可能走不同路径，不能称exact same baseline。最终greedy只接纳与已选index距离至少g者；它是结构性去冗余规则，不是式2联合效用的最优求解，也不证明重复token已经全部消除。相邻chunk可以有互补证据，index距离不等support独立性；多区域证据的位置均值可能落在无关中段（项目推断），原§8亦明确单峰过度聚焦、表格/附录/boilerplate等失败。文档插删会改变N/位置，须绑定chunker/document revision、位置权重/温度/两池预算与索引重建；不能把位置prior当事实或授权。

§4–6工业770review/318标签投影和70case×5 OCR与HOPM共用，不算独立验证；这些是downstream描述与评审一致性，不是SCP-HNSW相对semantic HNSW、gap-only或MMR的query级受控检索比较。作者明确尚缺该比较；Recall/coverage/quality/latency和lambda/g/tau/k的表4是建议实验网格，不能写成已测结果。共享case ID缺失限制text kappa，OCR一致性不认证retrieval收益或claim真实性。具体embedding、HNSW参数、hardware/precision、真实query/文档人口、batch/concurrency/完整SLO和独立重复未在本必要域充分披露，Not Disclosed；没有模型生成长度时不补数字。两维/768约0.26%只指向量维度，不是完整索引/内存/全链费用；第二ANN、重排、索引重建和独立support回归均计费。

## 拟分、actual owner与最小提案

拟2+1+2=5：仅位置条件的索引/查询与最终gap两个不同接口，不以成熟HNSW/MMR或不相关工业金额加分；组件局部，稳定取舍可复用。原准入的潜在改变经审阅收窄为Experimental设计分支，尚无质量/性能优越证据，不因证据弱而撤掉已经成立的贡献资格。

实际读Ch76 Chunking完整局部/parent-child、Reranking/Packing的top-k与joint-set/双视图段，及单文档后验答案位置prior段，邻Ch75/77开篇与相关交接。已有论证承载overlap/冗余/分散support与预算，不应为通用原则再加分；尚未承载**先让位置改变被索引的度量，再用首检结果生成第二次query的文档位置条件**这一实验分支，区别于事后答案加权或reader前后摆放。唯一`AGENT-RAG` Ch76；可用以下一个自然段把接口与失败边界接入top-k问题，不新设算法owner或声称推荐替代MMR。若独核认为有限分支尚不足长期采用，应具体判仅报告而非假称全文已有覆盖。

完整上锚：

把 top-k 简单按 score 拼接，会让重复内容占满窗口并掩盖少数反例。

拟新增：

对一篇顺序有意义的文档，位置还可以在检索前参与度量，而不只在最后删掉相邻chunk：给每个chunk向量附加由相对位置生成的两维编码，先以零位置query检索，再从首批命中估计位置中心，构造第二次query，最后另按最小chunk间距选择。[这一实验分支](https://arxiv.org/pdf/2606.01542v1)保持HNSW算法不变，却改变索引表示与搜索邻域，不能直接沿用旧图或把第二次搜索当免费。位置中心可能压低远处的互补证据，间距规则也可能删掉必要相邻段；文档revision、位置参数和两次候选预算须共同保存。原文没有受控检索消融，工业评审亦不证明该策略提高质量，所以这里只保留可检验的接口，不授优于semantic/MMR的结论。重建、两次ANN、重排与独立证据核验均计费；多区域问题、质量或净预算不稳时，保留semantic/hybrid、普通多样性选择与原文回读，不由更分散的index位置批准支持完备。<!-- source-family:SF-2026-ARXIV-2606-01542 -->

完整直接下锚：

在交错的 search–reasoning history 中，Packing 还决定外部材料在因果序列里能看见什么。若新文档只追加在已有推理后面，它的编码便能读取旧推理；一个替代分支保留原交错 history，同时把检索文档另按新到旧复制到 question 与旧 reasoning 之前，让这一副本文档在 causal mask 下不读取那些推理。双视图分别保留操作历史和较少受旧推理影响的证据编码，并不是删除旧 history，也不等于在原 slot 重复一遍 token。[受限文档位置实验](https://arxiv.org/html/2602.09517v1)固定 gold 文档并改变 pre-search reasoning 长度，及 repeat/stack-only 对照，支持这个消费接口的局部边界；语义匹配仍只是检索证据，不获得 truth 或 authority。<!-- source-family:SF-2026-ARXIV-2602-09517 -->

本人注只在独核必要/actual gap/原PRE通过且真SAVE之后写实际状态；不预I/DAY。当前首次必要与5分/提案待独核，不扩大到其他日期或所有工业材料。
