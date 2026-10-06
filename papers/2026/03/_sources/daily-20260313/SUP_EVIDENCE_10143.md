# 2603.10143v1 必要 Source / owner 判定提案

补充窗仅 2026-03-12 BJT 自然日。作者实际读 `SUP_CORE_10143.raw` 的 §3、Table1、Eq1、Algorithm1、§4–6、Appendix A Table4；未读取完整实现/全部提示，未宣称复现。准入、日级日期复用第二包与独立 ledger；本文件尚不授正式候选/Books。

## 实际方法与决定反侧

- BM25 top20 → BGE top5；可选 rewrite 的 lexical-overlap 阈值 .3 与 evidence 阈值 .5 来自50训练查询手调，约8%/12%触发，非隔离归因实验。Llama3-8B生成答案、rationale与引用，GPT-4o verifier赋8类标签。
- Table1 的 CORRECT-MISSING 是结论正确但 cited documents 不支持；CORRECT-ADDITIONAL 又容许正确外部知识。Eq1把所有 CORRECT-* 都置为 `I_j=1`，因此单条 CORRECT-MISSING 可得 Faith=1。这一评分不能同时作为引用支持已验收的证明；不是声称答案必然错误。
- Algorithm1 line12 Generate，line13 Verify，line14仍返回原 `ŷ,R,E,V`，没有按 verifier 标签修复、拒绝或阻断发布的分支。因此“corrigible”在此实现为诊断标签，不是执行中的纠错 Gate。

## 关键评价与资格

- PubMed23M固定语料，BioASQ yes/no、PubMedQA yes/no/maybe；训练示例为模型生成，结果除注明外采用 similarity-selected demonstrations，ID过滤只在ID可用时实施、固定seed兜底。不能把所有设置视为完全相同污染条件。
- Table2：自身 Vanilla 为82.3/70.0，rationale85.8/73.0，BGE87.4/72.5，Dynamic最佳89.1/71.0。MIRAGE外部结果使用不同backbone与MedCorps四检索器，不是“更小模型”公平单因素对照。Table3的BGE BioASQ3-shot比0-shot低1.3、PubMedQA0-shot比Vanilla低.5；dynamic在PubMedQA各k也未优于自身0-shot。不授普遍shot/reranker收益。
- Appendix A为便利选择的4例、2个人工标注者，同4例GPT judge；作者明确不能统计外推。Table4 LLM .94与人工 .85/.65是该4例描述，Q2 .75/.50/.83、Q3 .75/.30/.93等存在明显分歧；不把它解释为已建立校准或普遍人机一致性。正文提κ/F1但这个4例表不是可推广κ/F1证据。
- Single-point accuracy，无重复/CI；Llama3-8B加GPT-4o verifier与检索/改写有附加调用、延迟及成本，硬件/precision/线上SLO不披露。未打开代码、未断言实际可执行纠错。

## 当前唯一 owner 与实际差额

唯一 owner 为 ROADMAP `PLATFORM-EVALUATION-SYSTEM`，实际文件 `books/part-06-ai-infrastructure/66-evaluation-system.md`；不是以biomedical/RAG主题归到应用章。

作者实际读当前 Ch66 1140–1162（尤其1155/1157）及3798–3818（尤其3808/3810完整段）：前者要求回答准确率与可复查支持分开，后者将citation precision、claim coverage、answer accuracy另列，不从自动分数签发事实/内部faithfulness，支持不稳定回到人工与Unknown。Ch76 403–435、590–625也已实际读，分别区分citation correctness、faithfulness/task success与证据充分性/真值及abstain/escalate；为handoff，不能第二owner重述评价合同。

具体差额是本稿标签定义与Eq1的可构造冲突，以及Verify后原样return这一执行接口，不是抽象“已有RAG评价”。当前Books已有长期测量/发布资格，不能把本稿Faith协议或4例均值写成新可靠方法；不声称已经吸收本稿实验。

## 提案（待非作者独核）

影响2 + 冲击1 + 长期2 = 5；设计/反证触发必要深入，以上已完成必要方法、关键评价与反侧。拟终态 `争议/暂缓`、Books0：保留候选及具体反证，不采用其faithfulness/运行纠错中心保证。不是普通未读或外部受阻。

不提出逐字Book写入；若root裁为已有覆盖，应明确上述实际稳定合同与本稿新协议未采用，而非“摘要已吸收”。重开条件仅为可区分答案正确与引用支持的评分定义、实际修复/拒绝控制流、或匹配评价/人审统计；不扩全附件。
