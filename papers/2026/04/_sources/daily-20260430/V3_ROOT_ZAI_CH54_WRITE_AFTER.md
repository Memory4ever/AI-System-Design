# 04/30 智谱 LayerSplit → Ch54 非作者实际写后核

复核者 root；书稿作者 apr01。仅核 [智谱官方《Scaling Pain》](https://www.zhipuai.cn/zh/research/159)（页面标 2026-04-29 16:00 北京时间）§“优化：KV Cache分层存储LayerSplit”，以及 `books/part-05-inference-system/54-gpu-memory.md` 中 Peer GPU 与下一节之间新增的两段及章末 Review note。不代替 04/30 整日 Gate。

**结论：通过，限于这一 Source Family 的必要 Books 写后。**原文明确旧 Context Parallel 在每个 rank 保留全层 KV，LayerSplit 改为各 rank 按层持有，持有者在 Attention 前广播；Indexer 计算与 KV 广播重叠，最后仍有 Indexer Cache 广播开销。Ch54 把“机会性 peer 副本”接到“CP 固定冗余”的新约束，再把层存储 owner 与计算消费 rank 分开；没有误写为权重流送或 CPU offload，也没有让广播就绪之前的数据进入计算。下一节仍回到 memory hierarchy 的管理权，衔接成立。

作者只在 GLM-5.1、约 90% prefix hit、40k–120k Coding Agent Prefill 条件下报告 10%–132% 吞吐提高；硬件、precision、并发、TTFT 尾部和 SLO 在该节未充分披露。正文保留短上下文、低命中、弱互联、故障域及隔离优先时的全 rank KV/常规层级回退。约八分之一 Indexer 广播仅为该配置量级，不当通用常数；“层与请求身份一致才能消费”是工程安全推断，不冒充厂商公开实现验收。未运行代码或复现实验。
