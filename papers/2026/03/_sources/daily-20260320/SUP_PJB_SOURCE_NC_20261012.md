# 2603.17386v1：分层检索诊断的必要审阅

root sole准备；复用本日题摘校准、已核身份/公开日及原2+1+2=5。实际 exact-v1 https://arxiv.org/html/2603.17386v1 §3.1–3.4、§4/T1–5、§5与直接限制，不读无关图例或检索整站。这里“投资决策”指检索组件投入，不是金融投资。

## 原证与限定

固定297 JD/197674 CV/2242正相关标签；BM25和dense先pool，doubao筛选/Kimi二元judge，约20%query人工抽检。qrels只正例，missing无法区分已审negative与未pool，评价统一零gain不认证其真实不相关。六domain与rule-based reasoning taxonomy是诊断切片，非人类trace或真实推理深度。完整corpus与固定候选rerank须分开，固定depth20；query macro平均仍不解释所有低频类别。

两0.6B retriever×四QU/rerank组合；Qwen3-8B改写/8B rerank。T2–4体现CRE上rerank局部改善，但Qwen上的所有模块组合反退；QU+RR并非相加收益，serial/parallel切片方向不同。摘要的“reranking稳定改善”须按正文模型/切片收窄，不照录通用设计；domain-adapted对照训练数据/预算未匹配，不推“领域训练必需”或改写丢结构的唯一因果。运行硬件、precision、训练完整费用、并发/latency/SLO及统计不确定性未完整披露；新judge/改写/全corpus编码/重排/分层审校都有费用。不授匿名化消除fairness风险、招聘资格、上线效益或BM25/hybrid普遍结论。

## 实际 Books 判断：已有覆盖

canonical `PLATFORM-EVALUATION-SYSTEM`/Ch66，实际完整“平均值、切片与不确定性”718–746及“评价相对于分布”629起：保存per-example/domain/difficulty等关键slices，切片支持量与统计结构决定可采用结论，关联不等原因。实际Ch76 77–87 document/query/answer分层与query proposal权限、312–317按domain/corpus评recall/正负例/最终support；其现有retrieval/rerank固定池与真实召回分责也承载本次模块组合边界。相邻Ch75/77入口已读，任务还是受限retrieval diagnostic，不建立招聘或金融知识owner。

本稿的稳定增量是这些已写机制的受限新反侧；未证明需加入独立公式/新模块或新的可泛化设计条件。**No Change — Existing Coverage**，不写Books、不删证据、分数不变。保具体source条件与负面结果供Report引用，不以主题相似直接判覆盖，也不以NC降低准入分母。

待非准备者核验必要Source及实际覆盖；未完成日前验收。

## 非准备者有限Source/actual覆盖裁（resume_review17_18）

2026-10-12仅本20独立上下文，实际exact-v1 §3.1–3.4/§4/Tables1–5/§5直接反侧与current abs已读；不授全部图例、代码或复现。必要评价保完整297 query/197674 CV/2242正例、模型pool与20% query人审抽检、正例qrels/未标注非真negative、depth20和query macro、模型×module×domain/reasoning切片人口。Table4 CRE rerank在parallel-only .2257低于baseline .2389，即使其总体均值改善；Qwen各组合反退，QU+RR非加法。分层名称是规则启发式，不认证真实推理深度；不采domain training必需或结构丢失的唯一因果，硬件/precision/CI/全调用训练预算和生产SLO未完整披露。

实际Ch66平均/切片/不确定性完整718–746及分布责任、Ch76 query权限77–90、迁移人口/recall与reader support 312–320和有限judged pool/unknown机制1340–1352、相邻Ch75/77入口已读。Ch66已要求per-example/slices、支持量、相关结构和独立留出验证；Ch76已明确旧pool未标注不能当irrelevant、补审后同qrel版本重新比较和成本，且检索/排序/reader支持分验。这些具体论点承载本材料模块相依/切片反退、稀疏正例标注与固定池对真实召回的边界，不仅是检索主题相似。有限Source与具体NC PASS，原5/date不变、不写Books，模型和切片反侧留Report；不授领域公平/招聘资格、全部模型收益或DAY。
