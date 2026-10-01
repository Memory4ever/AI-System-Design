# 2604.25189v1 AgentDID：中央状态保证的作者侧窄纠错提案

身份：[官方 exact-v1](https://arxiv.org/html/2604.25189v1)，由旧泛化前闭在[第三批完整题摘反查](./V3_REVERSE_TITLE_ABSTRACT_BATCH3.md)恢复为贡献潜在；其 ID 在本日 04/29 08:00 北京公告的窄批链，未以 v1 `submitted` 单证首公开。此文件只读 §III-A、§IV-B/C、§V Theorem 1 与 §VI-A/B 的必要原文，并对读实际 [Ch72 身份/签名与执行证明](../../../../../books/part-06-ai-infrastructure/72-security.md)、[Ch84 AgentRun/credential](../../../../../books/part-07-agent/84-agent-platform.md) 相邻命题。不读全部参考文献/代码，不声称复现攻击或验证实现。

## 原文有效部分与中心冲突

- §IV-C 静态身份阶段：Verifier 发一次性 nonce；Holder 用自己的 operational key 对 VP（含所需 VC）签名，Verifier 解析 DID、核 VP/issuer/subject/有效期。它在可信 issuer、key 未泄漏的条件下支持“这次响应由相应 key 持有人提出，所附 credential 仍有效”这一窄身份结论。它不天然给工具效果授权，也不证明 credential 的现实属性恒真。
- §IV-C 动态阶段实际上只有两类可见证据：readiness probe 要求 holder 回答 task、调用指定工具、满足 timeout；context consistency 则由 holder **本地计算**其 serialized context hash，再用自身 `sk_op` 签名发给 Verifier，与后者本地 hash 比较。§VI-A/B 的原型测试是 Sepolia DID/VC 加 Python/LangChain、Qwen API 的一项摘要/hash/时钟 probe；`1v1→50v50` 总流程约 `13.5s`、吞吐 `0.07→3.25 TPS` 是该设置的性能，不是对已攻陷 holder 的真实内存状态取证。
- §III-A 明写 adversary **may control or compromise an AI agent**，让它谎报 context/workload/capabilities；Definition 1 又允许腐化任意 agent 子集，仅要求 Verifier 诚实。§V Theorem 1 在这些条件下宣称任意 state forgery 接受概率可忽略，并在证明中假定签名合法的 `h_holder` 必然来自 holder **真实**内部 context（否则必是伪造签名或 hash 碰撞）。该步不成立：若被攻陷的 Holder 控制自己的 `sk_op` 与响应逻辑，即使真实状态 `S_H ≠ S_V`，仍可直接签署 `h(S_V)`（例如保有先前一致序列而实际内部状态已变）并发送。Verifier 见合法签名与相等 digest 会接受，不需要伪造他人签名，也无须找哈希碰撞。除非另外假设可信执行／远程证明或内部状态不可由 Holder 自报，协议不能推出“签名哈希＝真实上下文”。这只否定**印刷定义/证明对受控 Holder 的状态真实性保证**，不自动否定 DID/VC 的密码学身份窄性质，也不声称原型代码实际被利用。
- Readiness probe 同样只证明所给 probe 的**可观察响应**在该时刻成立；它不能证明未测工具/权限、probe 后持续状态或内部 intent。§V 将成功伪装指定工具轨迹排除在 threat model 外，只能在这个限制下讲受限 readiness，不可作为一般能力真实性定理。

## V3 暂行处置与独立核问题

若原文对 corrupt Holder 的允许和 §IV-C 哈希发起方无额外隐藏约束，作者侧倾向按真实安全保证冲突触发深入，不以“只是 DID 组合”前闭；拟 `Design Delta 3 + System Reach 2 + Durability 3 = 8/9`、`深入／争议`、Books **暂缓正面采用**。Ch72 当前已写“签名只证明某身份签过，不证明内容安全”及 attestation boundary；Ch84 已把长期 credential/liveness 与真实 effect Gate 分开，故在争议未由独立核稳住前**不改共享 Books**，也不把协议包装为已获形式安全的 Existing。可保留受限 DID/VC 身份、即时 probe 可观察结果和原型吞吐；应隔离 `state forgery negligible`、`trustless runtime state verification` 的强保证。若后续原始勘误将威胁模型改为仅 honest Holder、增可信状态 attestation，或对 hash 报文给出独立绑定真实内存的机制，再定点重开受影响保证。

请非作者只核 §III-A Definition 1、§IV-C context-hash 步骤、§V Theorem 1/证明和 Ch72/84 的实际上述命题，明确反例是否成立、评分/Books 是否应调整；不要因该项重审其所有 DIDs、全篇附录或本日其他候选。本提案不是独立 PASS、不是日期或日级 Gate。
