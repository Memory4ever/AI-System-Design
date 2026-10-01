# 04/23 三项 RAG / Tool 非作者有限核

审阅人：apr20_resume；本日作者：root。只读[作者三项证据提案](V3_ROOT_THREE_RAG_TOOL_EVIDENCE.md)、下列官方 exact-v1 决定性方法/主表与反证，并对读实际 [Ch76 RAG](../../../../../books/part-07-agent/76-rag.md)、[Ch78 Tool](../../../../../books/part-07-agent/78-tool-calling.md)、[Ch30 LoRA](../../../../../books/part-04-training-system/30-lora.md)、[Ch66 Evaluation](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 的相关相邻命题。未读全部附件/后稿、未确认 04/23 first-public、未改日报或共享 Books，不替日级 Gate。

## 19899 MetaRAG reproduction：5 分准入 PASS；窄 Existing PASS

[官方 exact-v1](https://arxiv.org/html/2604.19899v1) §4–6：复做结果保相对方向、绝对分数下降；旧 prompt 与 hybrid sparse/dense 细节不可得、闭源 model revision 更改，原数值不可当可复算不变量。§5.3 Table 3 用同一 2WikiMultiHopQA 500 题/GPT-3.5 切片调阈值，原 .4 不再是最好，.2 优于 .1 与 .4，说明停止/追加检索策略与 model/harness identity 共同变。§5.5 Table 5 中 SIM-RAG 与 MetaRAG 的相对方向随模型和 reranker 反转，不能把“MetaRAG 总优”作为通则。

成本必须用正确分母：§5.5.2 Table 6 在 HotpotQA **500题 retrieval-only** 配置下，GPT-3.5 MetaRAG 是 14.85 model requests/question、30,064.5 tokens/request、47.85 seconds/request、全500题模型费用 $37.66；RAG 是 1 request/question、870 tokens/request、0.5 seconds/request、全500题 $1.3。表的 `Lat./req.` 不是每题端到端 latency，更不是生产 p95；其 token/req 数大也不能未经原实验计费定义改写。作者提案已准确标 47.85 为每请求，建议正式写时连同 `retrieval-only/500题/全数据费用` 同列，避免把不同指标拼成统一系统 SLO。

实际 Ch76 已具体分开 evidence sufficiency/stop/retrieval budget 与 reranker 的证据排序，Ch66 已明写 `model × benchmark × harness × environment × scorer` 的复现身份。这里可保的阈值/排序/代价命题均有 owner；完整 MetaRAG recipe 不需要再次写 Books。5 分是受限复现与成本反证，不是只因 RAG 题材入选，也不能声称原算法整体已写入；`No Change — Existing Coverage` 只指上述具体命题。

## 20148 Meta-Tool：5 分准入 PASS；窄 Existing PASS

[官方 exact-v1](https://arxiv.org/html/2604.20148v1) §3.2–3.4/§5.4 Tables 2–4：文档+5-shot 与 227.8M hypernetwork 生成 LoRA、value-guided beam 是同一实验中被测的不同责任；FSM 只约束 JSON syntax/type，不能替真实工具 outcome。最干净的负对照是**固定相同 prompt**下打开/关闭 hypernetwork，四项每 benchmark 成功率相同，平均 47.0%；不是所有生成式 adapter 普遍无益。去 few-shot 而保文档从 47.0% 降 25.5%，去两者至 3.5%；这些是 Llama-3.2-3B-Instruct、每 benchmark 50 题与作者 prompt 下的局部结果，缺训练/推理总成本配对与更大模型迁移。§5.4 的 47.0% 是四任务平均，不能说每个任务都等于 47%。

实际 Ch78 已将 syntax/route correctness/最终 effect 与 tool-result authority 分账；Ch30 约 618–620 和 656–660 已要求将外部 workflow/tool 与 adapter 相比，并把生成 adapter 的维度、复用、生成误差及回退训练成本作为条件。本文提供单一 tool-use 负例，而非新的普遍参数适配定律；窄 `Existing` 可以指向这两条具体决策，不能说论文全部系统已在书稿。5 分标准候选保“同 prompt 复杂参数适配无边际收益”的有限反证，Books No Change。

## 20199 All Languages Matter：5 分准入 PASS；Existing 需收窄为 Only，或另走窄 Books Gate

[官方 exact-v1](https://arxiv.org/html/2604.20199v1) §2.1–2.2/§3/Table 5/Appendix C：13 语言、BGE-M3 top-50→reranker top-5 的普通路径，与“按候选文档语言分组、各取 top-5、用**已知答案得分最大值**挑语言”的离线 estimated upper limit 不同。后者用后验 answer label，不能当在线 selector。LAURA 用多模型生成质量构造 reranker 训练正例，MKQA test 的 character 3-gram recall 相对原 reranker 主表平均仅约 +1.0～1.95 点；附录 Table 10 一些语言还退步，如 Llama+BGE 英文 70.1→69.8、韩文 25.5→24.9。`character 3-gram recall` 不是事实支持、许可或人类答案质量，论文只训练 reranker，未证明 retriever/generator 改造或所有语言公平。

与作者提案不同，实际 Ch76 虽已详细拥有**一般** relevance→evidence sufficiency→reader utility 分账与 oracle 不可上线，但未有“同一多语言候选池中，query/high-resource language 的排序偏置可能掩盖更有用的异语证据；按证据语言切片验收候选覆盖、rerank 和答案支持”的具体边界。不能以一般 ROADMAP/主题映射把该新增条件称为已具体 Existing。建议本篇 `2+1+2=5` 标准 `Only`，保跨语言证据选择的有限反例与后验 oracle/负面语言切片；若 root 判断此边界足以改变长期 RAG EvalSpec，则另作最窄 source→Ch76 提案、非作者写前核、共享锁实写及写后核，完成前不得先记 Integrate。无论哪一路，不能把作者 language-group oracle 当实时选择器，也不能以平均 3-gram 改进批准答案 truth。
