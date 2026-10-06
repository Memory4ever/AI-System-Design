# 02/13 V3 首批准入校准

窗口 2026-02-12T09:00:00+08:00 ～ 2026-02-13T09:00:00+08:00。作者 feb13_v3。旧13家族与旧Complete不复用；下列判断由完整题摘重新作出。原始abs与公告schedule已实时打开；Submitted保留而不作first-public。当前abs未见withdraw/correction标记。日期尚将用官方月列表公告标题分段核验，不能单凭旧inventory时刻。

拟入选：

1. 2602.10238 KVP：recency/attention代理不直接预测未来价值 → 仅K/V、per-head轻量策略从预计算trace学习跨budget token排序 → cache eviction要重新比较训练出的future-utility策略与手写代理。2+1+2=5，标准；潜在Books差额需具体证据，不预判已有覆盖。
2. 2602.10718 SnapMLA：MLA共享latent/RoPE导致量化敏感度和PV scale对齐不能照搬常规attention → RoPE保高精度、per-token量化与PV pipeline重构 → FP8 decode设计要分量处理并核对scale/数据流。2+2+2=6，标准，若owner有确切缺口再深入相关命题。v2 submitted 02/12 02:38 UTC不是默认本窗公开修订证据。
3. 2602.10986 TVCache：仅tool参数相同不等于state相同 → full tool history树的longest-prefix缓存匹配 → rollout tool缓存正确性需要状态身份，不按API输入直接reuse。2+2+2=6；长期缺口或冲突强制深入。非确定环境、external时变状态/隐藏随机性不由摘要证明。
4. 2602.11088 Partial TEE：precomputed noise复用减低可信区开销 → 已发表协议的confidentiality/integrity具体攻击 → 不能把partial TEE与秘密随机性复用等同安全offload。3+2+2=7，安全设计反证强制深入；不把作者层级恢复时间外推整模型/IP实测。
5. 2602.11149 long-CoT repetition：扩样本惯常优先于重放 → 在数据/compute公平条件下重放long-CoT更好且跨规模任务成立条件 → SFT数据配方需要检查多epoch轨迹内化而非默认diversity总占优。2+1+2=5标准；正文需查equal budget与直接反侧。

代表排除：2602.10133 AgentTrace；题摘提出cognitive/operational/contextual三日志类型加scope、序列、timestamp，透明性/trust主张但没有新的追踪语义/因果归因保证或区分实质机制的评价，只把已有structured logging/trace分层包装；能落PLATFORM-TRACE不构成准入。若正文有摘要未说的新对照/失效边界才定点重开，不以旧高分录入。

复核请求：核上述原增量句与评分，检查AgentTrace漏收及局部证据/反例不可按机构或成熟原则加分。
