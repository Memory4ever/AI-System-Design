# 11650 QChunker：actual delta最低关闭提案

mar14_supplement；第六窄P/Mar13 arXiv日期及venue必要性独核有效复用，不再以ACM403制造日期缺口。exact-v1 GET200/294435B/UTC2026-10-10T01:29:12.215690，SUP_NECESSARY_11650.raw/txt及FINAL_MANIFEST_RESULT。本人实际§3.1–3.4/所有ChunkScore式、有限几何论证、完整Table1与§4.1–4.6/结论；不读HChem构建附件/提示catalog/代码/全部参考或复现。

P保留：普通固定分割丢跨chunk上下文→question-outline采样partition、adjacent PPL ratio+feature-centered Gram regularized logdet选局部候选，再用原document缺失知识rewrite→改变ingestion局部选择器。具体新增是proxy组合与模型pipeline配置，**拟1+1+2=4最低关闭/仅报告Books0**，不把已有PPL/Gram determinant、源内引用和多角色名字另计重要机制或长期知识缺口。未因已有Books或费用缩掉准入。

§3.1–3.2明确globallyoptimal仅问题定义；实际搜索只有outline采样subset S，source-only completion是model审查/生成要求而非可执行事实保持保证。四角色串行，并非实现一个新的分布式执行语义；三个Qwen2.5-3B SLM各45K监督由DeepSeek-R1生成，baseline没有匹配这部分额外监督/建库费用，不能归全部收益给score本身。模型float16、A80080G，bge-base-zh-v1.5/Milvus/topK8固定，datasettrainCRUD/Omni、另外两domain测试；保持作者范围，不称总成本/SLO公开或全部pipeline实现正确。

§3.3 LI=PPL(c_i|c_prev)/PPL(c_i)是条件预测proxy，干扰context可提高PPL，未证明必在[0,1]或独立事实；SD=K^-1 logdet(Z^T J_d Z+αI)测embedding几何，不证明语义完整/独立与groundtruth一一对应。标准Gram体积恒等式成立，却不能自证“高质量语义必线性独立”；regularization/feature-scale与chunk数/长度仍在目标中。§4.5 λ按CRUD downstream ROUGE-L Pearson选择.3，再报其它domain>.85；不授完全下游独立/所有workload无需重校准。

Table1所有十二overlap指标与w/o-refine反侧已读；三次独立重复/t-test作者声明支持受测局部效果，但没有给完整置信区间/端到端费用。移除completion同时改变rewrite/context暴露，未匹配文本长度/调用和监督，不能唯一归因“semantic compensation”。§4.6 rewritten PPL下降不是忠实事实或无幻觉证明；HChem为生成QA和化学场景也不借作新Science贡献。既有4题目准入是局部选择替代，必要支持与关闭理由够即停。

精确v1 title/六作者/AB与current说明之前已actual核，未见具名撤回/纠错/已知early稿；WWW后发表日不迁移本公开日。待非Source作者实际必要原证/评分关闭独核后正式，不自授Evidence/DAY，无Books修改。
