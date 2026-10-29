# 2603.09185 — DEO必要Source与Ch76差额（Source/PRE/actualPOST通过）

[DEO exact-v1](https://arxiv.org/html/2603.09185v1)。第二包root已实际完整AB准入通过。作者实际完整§3/4/5/7、Eq1–4及Tables1–6；题摘/current只有v1、comment空，未见纠错/accepted先稿信号，未核代码/复现，不扩大参考文献。

## 日期、评分与实际机制

SUP_EXACT_BATCH2.json v1 Mar10UTC04:47:15；owning arxiv.content/findable DOI registeredMar11UTC02:07:28上界＋official availability no-advance finalID/DOI/deadline最早Mar11BJT08下界，同BJT日夹证arxiv日；不拿Submitted/Updated/registered单独public，原字段待root独核。

2+1+2=5：只改写query不必修复否定相似关系→冻结encoder/corpus只在线优化query向量靠近正子查询/远离负子查询并保留原query→查询控制与语义/预算的稳定差额；单retrieval组件，评分不采用成熟contrastive/LLM扩写本身作为新原理。Ch76具体gap进一步定点深入。

§3 GPT4.1nano temp.1生成P/N结构子查询，再用冻结encoder CLS embedding。Eu从E(q)初始化，Eq4为λp mean||e−p||² −λn mean||e−n||² +λo||e−eo||²，用Adam固定步后cosine/FAISS排序。不是encoder训练、document向量更新或新index，也不是通过硬predicate删除所有含排除属性的文档。没有外部corpus relevance训练labels，仍有LLM decomposition/encoding与在线gradient优化费用。

必要数学边界（本书分析，非作者定理）：展开Eq4为c||e||²−2b·e+const，c=λp−λn+λo，b=λp meanP−λn meanN+λo eo。无额外norm/domain constraint时c>0才有有限唯一最小点b/c；c<0无下界，c=0且b非零也无下界。原文未披露优化中的projection/约束，不能凭cosine ranking下游归一推回上游loss有界。默认textλp=λn=1, λo=.2→c=.2；Table5的λo=.2,λp=1,λn=2→c=−.8，取一维P=N=eo=0得L=−.8e²即反例。Table5所试有限20步可有收益，不等该配置loss收敛；作者没有正式全部配置收敛定理，不把这个边界升级整篇Disputed。§4.3.4超过100step排名下降是直接经验反侧，固定步/原query一致性与可行域需联合验收，不能用loss更低签语义更好。解析最小点是公式推断而非已经实现或matched提速证据。

## 评价与直接反侧

§4.1 NegConstraint MAP@100/nDCG@10、NevIR Pairwise、COCO-Neg Recall@5。BGE-small/large-en-v1.5/M3文本，OpenAI CLIP/laion400m/datacomp/NegCLIP跨模态；text20step/λo.2、imageλo1，非相同编码器/协议统一定律。Table1 BGElarge MAP.6299→.7327/nDCG.7139→.7877；NevIR仍.2552→.2776（绝对得分低，仅局部改善，不能说否定可靠）。Table2 CLIP Recall@5.4792→.5392是6个百分点不是6%相对。其他models亦有限提升，不授allmodalities。Table6 decompositionAVG .6451/.7312、RRFk60 .6641/.7417、full .7379/.7946对baseline .6374/.7250，支持固定这套变体中优化作用，但不证明与所有Rocchio/闭式加权/硬过滤比最优；AVG里正负子查询的合并细节未核实现。

Tables3–4 GPTnano优Qwen2.5-1.5B但小模型仍收益，依赖分解质量不能忽略；§5.1以GPT4.1mini二元judge分解91.76%只是同类LLM代理，不是独立人工gold。Table5所有有限tested组合优baseline不授任意权重稳健；§4.3.4 text20～50稳定、image约50peak、100后下降，图像全部点未独读，不造每个step的值。§5.2 PCA+top5 improved query选择性例子不是因果/最坏排除保证；gold用作可视化标记，不据此声称优化训练用了gold。

§5.3 Ryzen7 5800X/64GB，20/50step总.016/.035秒；RTX3060 12GB .033/.095秒只query参数优化，不是LLM decomposer/encoder/FAISS/reader端到端成本。硬件只该micro stage，precision/AdamLR、K/M分解数量、全部sample/runseed/CI、索引规模/完整topk批次、concurrency/tailSLO/API价格 Not Disclosed，不能填造。§7主要限制分解正确性与跨audio未测。本轮不用GitHub可选artifact证明实现或复现。

## actual owner/PRE提案

唯一owner `AGENT-RAG`：[Ch76](../../../../books/part-07-agent/76-rag.md)。实际1–32开篇、49–89完整局部、1290–1310 negative-control局部、Ch75/77开篇已读。query variant预测与LLM多路融合不承载query-only向量优化；1298负向控制是历史irrelevant方向，不是本次query的排除属性，不能作主题NC。拟在query variants两段后、Document-side reader-utility排序前两段，保留原query、多路与reader分责。

查询侧的控制也可以发生在向量而非文本改写上。编码器与文档索引不变时，先把同一信息需求拆成“希望包含”与“希望排除”的子查询，再仅优化当前 query 向量，使它靠近前者、远离后者，同时保留原向量的一致性项。这是在固定表示空间内改变排序提案，不是训练新 encoder，也不等硬过滤满足所有排除条件；子查询仍可能误解否定范围，文档与最终答案还须按原问题验收。[必要方法](https://arxiv.org/html/2603.09185v1#S3)所用正距离减负距离的平方损失，还应检查正项总权重是否大于负项；无额外可行域约束时，反向条件可使目标无下界，更多优化步不能直接解释为语义更准确。<!-- source-family:SF-2026-ARXIV-2603-09185 -->

这种 query-only 分支省去模型重训与重新索引，却增加分解调用、子查询编码、梯度步骤和选择预算。[有限否定检索对照](https://arxiv.org/html/2603.09185v1#S4)中它优于直接扩写的 AVG/RRF 变体，过多步骤仍会退化，否定 pairwise 得分也远非可靠排除；参数优化的毫秒计时不含分解、编码与完整检索/回答成本。应把原 query、子查询、权重和有限步预算绑定为同一次查询身份，分别验收相关性、排除条件与真实总费用。分解不可信、目标越界或排序退步时，保留原 query、已核多路融合与可验证字段过滤，不把较远的负向 embedding 当作证据反驳、访问授权或答案真值。<!-- source-family:SF-2026-ARXIV-2603-09185 -->

拟本人末注：SF-2026-ARXIV-2603-09185，Daily2026-03-12补查；v1§3/4/5/7、Eq4/Table1–6，2+1+2=5，query-only优化差额深入；参数权重有界条件为本书直接代数分析，不授作者全配置收敛或整篇中心Disputed。decomposition judge/有限ranking与end-to-end费用分开，negative子查询不等事实反证/硬过滤。root必要原源/原日期/PRE及写后POST待核；未核代码/复现，不授DAY。

## 实际落地与POST（更新上面原提案状态）

root实际官方v1§3–5/7、Eq4/Tables1–6、原日期字段、actual Ch76 queryvariant→readerutility局部/negativecontrol及75/77开篇Source/PRE通过，授作者仅两段/本人末注窄锁。作者按建议明确吸引项＋原query一致性项总权重对排斥项，实际写Ch76新83/85及本人末注，顺读75–105完整局部；root作为非writer实际顺读75–103完整邻接、新两段与本人末注，回原Eq4/评价/退化/费用，actualPOST通过并释放窄锁。条件向量排序不授硬排除或reader答案真值、c=0平坦/无下界与有限步差额保留。未核代码/复现，不授DAY。
