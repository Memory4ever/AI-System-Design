# AgentDID 2604.25189v1：有限非作者复核

范围：只核 [exact-v1 §III-A、§IV-C、§V](https://arxiv.org/html/2604.25189v1) 的威胁模型、context-hash 报文及 Theorem 1，并对读 Ch72 的签名边界与 Ch84 的 AgentRun/credential 责任。不核日期归属，不声称复现攻击或审完全部实现。

## 反证

Definition 1 和 Theorem 1 都允许攻击者腐化任意 agent，但要求 Verifier 诚实。§IV-C 由 Holder 自行计算并签署 `h_holder`，Verifier 验签并比较本地 `h_verifier`。若 Holder 已被腐化并控制自己的 operational key/响应逻辑，可以在真实上下文 `S_H != S_V` 时直接用自己的 key 签署 `h(S_V)`；Verifier 的两项可见检查仍通过。这里既未伪造**其他身份**的签名，也未构造哈希碰撞。§V 证明中“签名合法且值非真实状态就必有签名伪造”的推导缺少可信状态测量或等价约束，因此印刷出的强 `state forgery negligible` 保证不能由列出的密码学假设推出。

这是对论文所述威胁模型与协议的逻辑反例，不是对作者原型的实测入侵。DID/VC 对特定 key/发行方的身份与凭据有效性仍可作较窄结论；readiness probe 只证明当次受测的可观察行为，不证明未测能力或未来状态。

## Owner 与处置

Ch72 已明确“签名只证明某身份签过，不证明内容安全”，Ch84 已把 credential/liveness 与高风险 effect 的独立 Gate 分开。原文没有推翻这两个结论。支持作者侧 `Design Delta 3 + System Reach 2 + Durability 3 = 8/9` 的深入/争议提案，仅作为需防止强安全保证误用的反证，不将 AgentDID 的 `trustless runtime state verification` 写成已验证机制，也不因该项修改 Books。若出现作者勘误、可信执行证明或更窄的 honest-Holder threat model，再重开相应命题；日级日期、来源和否定侧 Gate 仍由本日 owner 独立闭合。
