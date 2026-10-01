# 2026-04-24 三项系统命题「已有覆盖」的有限非作者复核

复核者 root；原报告及证据作者 apr01。对官方 exact-v1 的必要方法、实验分母与否定侧，逐项比较 `ROADMAP.md` 指定的现有章节。只签下列具体 Books 判断，不替代其余候选、来源、日期和整日报 Gate；没有独立复现实验。

## 2604.21361v1：分布式推理的时钟与因果

[官方 v1](https://arxiv.org/html/2604.21361v1) §3–6 在多节点 CPU LLM 流水线对应用时戳注入偏移，Kafka/ZeroMQ 受测，Aeron 尚未完成。实验观测到输出和吞吐仍正常、跨节点 send→receive 在时戳上可能成为负跨度。它说明 timestamp 排序不自动证明 happens-before，但不证明实际消息倒流、请求失败或通用的 3–5ms 阈值；30s health 滚窗下降也不证明物理时钟恢复。具体 CPU/model、输出长度、并发和生产 SLO 未充分披露。

`PLATFORM-TRACE` Ch69 已在“跨节点时间戳不是天然的因果顺序”明确写出 clock domain、误差/新鲜度界限、request/message dependency 与不可排序状态，并保留单机或可靠同步时使用 wall-clock 的合理性；该章已有的正是本文所需长期判断，不只是同主题名称。维持 2+1+2=5、标准审阅、具体已有覆盖，不新增 Books，也不把应用时戳实验外推为生产阈值。

## 2604.21454v1：状态更新与历史检索的组合

[官方 v1](https://arxiv.org/html/2604.21454v1) §3–5 的 AstroRecall/Collision 将更新状态和回读历史交织；OLMo3 与 Hybrid7B 在限定训练配方下比较 Instruct/Think，并将 parseable answer 与 raw accuracy 分开。Think 最大 6000 输出 token，Instruct 的预算短得多，故训练目标、架构和推理预算未完全隔离；合成任务的优势不能推出任意自然语言任务或所有 hybrid 模型更优。

`MODEL-LONG-CONTEXT` Ch22 已在 sparse/recurrent/hybrid 演进中单独写出“先更新状态，再根据该状态选择历史”需要组合能力，以及训练预算、显式推理 token 与状态容量须分账。论文是该设计判断的受限实例，不是需要另起“混合模型总胜”结论。维持 2+2+2=6、标准审阅、具体已有覆盖；不新增 Books。

## 2604.21477v1：MCP 静态发现、动态效果与可信判定分权

[官方 v1](https://arxiv.org/html/2604.21477v1) §4–8 采用 protocol-aware Tier-1 静态规则识别 P1/P2/P5/P6；跨 tool 转发与图像到 sink 的 P3/P4 需要 trace/dataflow，不能计入静态完备覆盖。六个 server 版本 36 个二元标签和 29→0 的静态 finding 只说明所测规则匹配；324 是生成计划/可运行规模，实际 trace-divergence 初测只来自 email 场景 19 runs。可信 predicate 以实际 sink effect 而非 Agent 叙述判定，不把 risk score=0 解释成所有攻击被阻断。

`PLATFORM-SECURITY` Ch72 已将 tool trace、deterministic predicate、value→transformation→sink 授权，以及声明能力与静态/动态实际行为的差异纳入一条责任链；第 66 章保留 EvalSpec 分母。论文的 rule set、六 server 分数和 D1–D5 taxonomy 不必逐项复制到长期书稿。维持 2+2+2=6、深入审阅、具体已有覆盖；不新增 Books，不声称真实 MCP 生态防护已验收。

三项只能关闭上述命题级 Books 决策；本日尚余 GPT card 的拟已有覆盖及其它候选/来源/日期独立复核。
