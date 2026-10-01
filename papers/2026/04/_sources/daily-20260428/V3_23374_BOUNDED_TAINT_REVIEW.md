# 2604.23374v1：Agent 来源传播与安全授权分开验收

本页只处理 04/28 既有开放线索，非正式候选/评分/Books 决定。固定窗口为北京时间 `[2026-04-27 09:00, 2026-04-28 09:00)`。旧 receipt 的 v1 `Updated=2026-04-28T00:36:12Z`、当前 OAI `2026-04-28` 与公告批次相容，却都不单独证明 first-public；官方 v1 页头 `25 Apr` 是稿件/提交标示。

[官方 exact-v1](https://arxiv.org/html/2604.23374v1) §3–4 明确区分三种传播：内容经 paraphrase 保留语义、内容不见于参数但改变 sink 决策、以及存储/检索后跨会话重新进入 context。DCPG 在 memory 写入与读出间维持来源 lineage；真正判定延至 sink event：先做 lexical/semantic/multi-fragment 明示内容检查，若仍有来源 lineage 而无明示内容，再把该来源替成中性且 schema-compatible 的内容重问 agent，观察 sink 是否仍发生。此反事实 probe 的 judge confidence 是自报分数，非经校准的因果概率；多来源逐个替换亦不能穷尽交互效应。审计在完成执行后进行，**不能**冒充不可逆 effect 之前的实时阻断。

§5.1/TaintBench 用 20 个开源框架实例化共同模板共 400 scenario、200 positive；标签是模板级来源传播而非 action harm，两作者审查模板及代表轨迹、每 scenario 五次运行三次命中聚合。Table 3 的 ToolEmu/ InjecAgent 是原 unsafe 标签，不能与 TaintBench 的 propagation F1 合成一个防护率；ToolEmu 过滤为 79 个 injection-like cases。§5.3/Table 5 隐式控制组 40 例中召回 37，语义组 85 例召回 75；§5.4 仍有 13 FN、16 FP，尤其 paraphrase/跨会话丢失和 topical-overlap/模型既有知识误归因。§5.5 所报每 execution unit 平均 0.25 秒是离线审计成本，反事实分析另消耗平均 457 auditor tokens，不是线上许可路径的 p99 或全 Agent 成本。

[Ch72 Containment 与多 Agent 委派段](../../../../../books/part-06-ai-infrastructure/72-security.md)已有跨节点 source/delegation/memory→irreversible sink 的 provenance，以及 sink 前 deterministic policy；[Memory Origin Confusion 段](../../../../../books/part-06-ai-infrastructure/72-security.md)亦有持久来源和 effect receipt 分权。论文因此**不是**首次指出应做 source→sink，且其离线 detector 不能取代已有 authorizer。现文尚未把“同一来源的显式内容传播与只改变 sink 选择的隐式控制”分作两种审计对象，也未说明 memory 读出只恢复 lineage、必须等 sink 才能判断传播。这是可能的窄证据/诊断增量：Ch72 可在委派信息流段将离线事后 localization 和在线 effect-time authority 相邻分层；Ch66 只拥有 propagation 标签与 unsafe 标签的评价分母，不另建重复 owner。若非作者认为现有 provenance/反事实主线已完整承载，可判受限 Existing/Only，不因作者称“first comprehensive”自动写书。

作者侧结论：保留贡献线索供非作者 source→actual-owner 与日期核。正式评分、深入审阅是否触发、Books 写前锁均未取得；不改当前工作池/候选分母。旧 receipt 的 `deep_complete/No Change` 仅是历史字段。
