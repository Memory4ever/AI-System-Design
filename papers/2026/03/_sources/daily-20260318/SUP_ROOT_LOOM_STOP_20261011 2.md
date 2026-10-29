# LOOM：暂停时的 root 审阅停点

用户于2026-10-11要求立即暂停。本文件仅保存已读依据，不是 Source/PRE/POST 或日报验收通过声明；未写入 Books。

精确材料：[2603.15279v1](https://arxiv.org/html/2603.15279v1)。已实际读 §3.1–3.3、§4.1–4.2/Tables1–3、Appendix B/C/D 的必要部分及 G 限制；无需重新遍历全文或附件。

- 方法是保留有限 data/noise 配对，在每批内重配并保存全局 permutation；不是 population OT oracle。多 noise cache 用于缓解固定噪声过拟合，seed 存储不是零训练成本。
- Appendix B 直接给出小批停在次优匹配的反例。cost 不增不等于唯一 permutation 收敛；相同 cost 的 tie 更新尚不能从该证明推出映射最终不变。若正文拟采用定理，须收窄到已支持范围，不沿用全局最优或稳定映射保证。
- 少 NFE/FID 是特定无条件图像、ADM/solver 的质量与求值权衡。CIFAR10 4-cache 的134-NFE FID4.41并不支配 OT-CFM 134-NFE3.57；FFHQ 表也不支持任意低NFE严格支配。
- Appendix D 同1000epoch/4×RTX3090明确17.3h对13.9h，不采“无额外计算成本”。不同数据的epoch变化不证明总预算免费；precision、推理batch/concurrency/SLO未披露。
- Appendix G：条件生成须处理 label-conditional source marginal，朴素 coupling 会引入偏置；不能外推到条件 foundation model。

已实际定位 `MULTIMODAL-GENERATIVE-PARADIGMS` / Ch24 的端点配对论证（现行259–267附近）：population prox 与 learned forward bridge 已有，有限持久匹配的状态、过拟合和费用是可比较差额。作者拟准备两段 PRE，但 root 尚未读其逐字稿、未授 Ch24 写锁；不计实际整合。

恢复：先读当前 AGENTS/研究与 Report 合同、本日停点，再复用上述有效阅读，核对作者必要证据笔记与逐字 PRE；独立复核后才决定实际 Books 写入，写后仍须非写入者 POST。暂停期间不继续研究、写书或分配其他日期。
