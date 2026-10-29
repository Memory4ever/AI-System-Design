# 2603.08877 — Search-call 与 completion-token 预算分开执行

root 实际读取 [BCAS exact-v1](https://arxiv.org/html/2603.08877v1) §3.1–3.8、§4/Table1–2及§5–7；未核代码、全曲线或复现。SUP_EXACT_BATCH4.json完整题摘/current无撤回、owning/findable registeredMar11UTC02:00:03与同日官方公告下界复用。官方ACL LREC-1.808为May2026正式出版，未来发表不当此前全文日期。

Score 2+1+2=5；Owner AGENT-RAG/Ch76，具体预算执行接口差额深入。实际727–850的execution prior、Joint Policy、compression净收益与stop utility及Ch75/77交接已读；已有原则未具体区分tool禁用与事后token累计的权限。本项不采用最佳search次数recipe。

BCAS把剩余calls/tokens提示给模型，达到max_searches后从tool schema移除search；completion usage在一轮provider回复后累计、阈值触发退出，故不是调用前严格token admission，也不认证预算绝无越界。BM25/ParadeDB、BGE-M3和bge-rerankerv2m3；HS5与HS100 rerank5候选池不同，不能唯一归因reranker。

六模型o4mini/DeepSeekV30324/GPT4.1mini/Gemma327B/Qwen314B/Llama3.18B、三个静态QA与约467–537有效样本、同prompt scaffold而非每模型最佳；GPT4omini二元judge/600人工子样本发现5false-negative，不当全域证据faithfulness或统计安全证书。仅Hotpot467做组件消融、部分组合混杂，不授全factorial全域因果。500/1K/2K/4K/16K completion budget的o4排除是因内部reasoning计费不可见，不拼统一token效果。

T1 DeepSeek Hotpot80.48@3search→77.94 unlimited、Qwen/Llama Trivia也反退，直接限制§5“各模型数据集单调”；planning+reflection部分降质。没有pure单步non-agentic baseline，不证明Agent相对一次RAG增益；cost跨provider估算、queue/throughput/concurrency/SLO未完整披露，API失败也改变有效人口。硬件/precision/输入长度/并发不齐不补造。工具/生成/检索重排/计划反思/独立评价均计费，短最终答案correctness不是引文完整性。

## 逐字 PRE，待独核

在 Ch76 Joint Policy 的“共享harness…Static top-k…”完整段后、资源设备compression段前单段：

> 联合策略还须把 search-call 与 completion-token 两种预算分开执行：运行时可在调用额度耗尽时移除 search 工具，让模型读取剩余额度并转向回答或 abstain；但按 provider 返回后才累计 tokens，只是事后计量与停止，不等于调用前的硬上限。[有限静态 QA 对照](https://arxiv.org/html/2603.08877v1)显示 search、retriever 与生成预算的收益依任务和模型而变，更多搜索并非处处更好，planning/reflection 也可能退步，不能把“三次搜索”设为通用默认。预算状态、工具 schema 与 usage 口径应进入同一 run identity，内部 reasoning 不可见时单列而不拼统一成本；retrieval pool、reranking、生成和评价全部付费。达到预算或证据不足时保留单步/hybrid baseline、确定性停点与独立 verifier，硬成本契约还需调用前预留和明确超额处理，不能让模型自述剩余额度成为计费或答案正确性的 authority。<!-- source-family:SF-2026-ARXIV-2603-08877 -->

mar12_independent_continue 非作者实际必要 Source/date、owner与逐字 PRE 通过；root 窄写 Ch76 shared-harness 完整段后单段及本人末注，该 reviewer 实际顺读完整邻接、新段和本人末注并回对精确原证与 PRE，POST 通过。原块保留，窄锁释放；未授 DAY。
