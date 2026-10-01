# 2604.20199v1 → Ch76 实际写后非作者核

复核者：apr20_resume；书稿写入者：root。对照[官方 exact-v1](https://arxiv.org/html/2604.20199v1) §2.1–2.3、§3/Table 5、Appendix C 与先前[必要源→实际 owner 独立核](V3_APR20_THREE_RAG_TOOL_INDEPENDENT.md)，本次只顺读[Ch76](../../../../../books/part-07-agent/76-rag.md)约352–403行新增正文、两侧 relevance/sufficiency 与 query robustness 交接及章末 `SF-2026-ARXIV-2604-20199` Review note。未重读全文附件、未复现实验、未改共享书稿/04/23 正式报告；不签 04/23 日期/来源/分母/整日 Gate。

**实际写后 PASS。** 源文 §2.1 的同一 BGE-M3 multilingual top-50 候选池与 reranker top-5，可支持新增的“检索候选已有跨语证据时，重排仍可能挤掉异语关键文档”具体失效；正文按证据语言而非 query language 将候选覆盖、重排留存、sufficiency 和答案支持拆为不同验收对象，比原一般 relevance→sufficiency 关系增加可执行的分层条件。它紧接旧的相关性/充分性分工，后接 query robustness，未把 reranker 升为事实来源或 answer gate。单语/低风险下旧路径仍保留，语言识别、标注、池构造及语料不均衡成本也在实际正文。

最关键限制在正文与 Review note 均正确保留：§2.1 的 language-wise estimated oracle 用**已知答案分数**跨组择优，只是离线上界，不是生产可用 selector；LAURA 测的是 reranker，不能归因 retriever/generator 同时改善；MKQA 13 语言的 character 3-gram recall 小幅均值改善及 Appendix C 个别语言反退不是 fact support、所有语言公平或端到端生产性能。原 source→owner 核指出的具体缺口已由实际正文补齐，不再把本篇记为泛化 Existing 或仅因相似主题无改动。章末 Review note 明列 exact-v1、Daily 归属、采用范围及未复现实验；`git diff --check` 对目标章通过。此 PASS 仅及该窄整合的真实写后，不代替 04/23 整日 Gate。
