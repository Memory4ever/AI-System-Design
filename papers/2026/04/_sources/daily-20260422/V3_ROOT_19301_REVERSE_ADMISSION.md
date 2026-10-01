# 2604.19301v1：非作者有限准入复核

[官方 exact-v1](https://arxiv.org/html/2604.19301v1) §3.1–3.5、§4–5、Appendix A–G：作者在 Apple/Banana 无客观 gold 的二选一投票提示中，固定由 prompt 赋予的“初始偏好”，改变公开/匿名、后续评价、继续合作、同伴声望及信息持有描述，并在两个选项方向上重复采样。六模型条件与 temperature/max-token 不同，四个模型的部分公开条件响应不能外推所有多 Agent 协作；Llama-70B-AWQ 首 token 前 residual 的条件差向量余弦只是表征关联，不识别规范动机或单一训练因果。

旧准入句提出“社会呈现压力会改变多主体答案”，这个受限观察成立；但实际评测不是有真值的共同工作、没有独立信息流/行动提交，也没有测试新的 controller。当前 `AGENT-MULTI-AGENT` 的 consensus、channel framing、相关错误、独立 verifier 与 commit 责任已覆盖长期约束。本项具体的投票场景变量没有改变该判断，也不能以认知心理术语补成内部机制。按当前贡献门槛，**同意由 5 分标准 Only 候选改作具名前分母关闭**；作者已读的源证据应保留，但不把无 gold 社会选择当一般 Agent 安全证据。此记录只审这一项，不签 04/22 负侧或整日 Gate。
