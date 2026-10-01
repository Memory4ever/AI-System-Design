# 2026-04-24 四项 KV、视觉与 Agent 评价的有限非作者核

复核者 root。对读官方 exact-v1 的方法、关键对照与限制，并比较当前 Books owner；本文件只验四个既有候选的受限处置，不证明整日来源、日期、否定侧和争议项已闭合。

## `2604.21335v1` Sub-Token Routing：细粒度 V 预算不等完整服务收益

[官方 §3–4、Appendix C](https://arxiv.org/html/2604.21335v1)明确 query-independent 与 query-aware 是两条分支：前者在缺实际下游 query 时学习 V-group 保留/重建，后者以预测器在 context-token/group 上分配总预算；K 始终完整保留，所以所称 V 比例 ρ 对应的总 KV 比例为 `(1+ρ)/2`。预测未来相关性不是准确观测未知新 query，压缩后的 cache identity 也不能未经重验供任意 query 复用。附录的部分 Quest 对照更优，部分并非；MMLU、RULER、单卡/局部 forward 与预热排除的 profiling 未给生产 batching/SLO 保证。

[Ch45](../../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) 已拥有 cache identity、价值/误差预算和执行成本的长期主线。本文提供 V-group 这一受限选择粒度，不足以将它升级成默认压缩策略；保留 `2+2+2=6`、标准审阅、仅报告。若 packed 动态 group kernel、并发和跨 query 质量证据实测改变决策，再定点比较，而非先写 Books。

## `2604.21346v1` Symbolic Grounding：生成程序是特权输入上界

[官方 §3–5](https://arxiv.org/html/2604.21346v1)利用 Bongard-LOGO 的真实 drawing program 替换原像素输入，再交给 LLM 判别抽象规则；这改变了信息接口，不是已实现了像素到程序的生产感知器。Raw-image VLM 与 symbolic LLM 池、prompt/输入长度不完全匹配；部分 grounded 条件只补 query image，不等于恢复全部支持图像的感知要求。对 query action 序列作 permutation 会改变其所画物体，若沿用旧 label，其掉分不能单独证明模型理解了原视觉因果。

[Ch66](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 已要求区分真实输入、规则/alias、oracle 与受控输入干预，Ch23 负责 representation identity。此文给出符号上界的局部诊断，但无法把所有 raw-image 失败独归因于视觉 encoder，也没有可迁移的无 oracle 部署机制。维持 `2+2+2=6`、标准审阅、仅报告，不据此改写 Books 的视觉瓶颈结论。

## `2604.21480v1` Diversity-Guided User Simulation：分叉须连同环境状态恢复

[官方 §3–5 与 Appendix](https://arxiv.org/html/2604.21480v1)在指定 user turn 前保存 orchestrator、environment/tool DB、history、RNG 与计数等状态，选择 junction 并生成多条 user response，再沿同一 prefix 分叉。完整状态恢复是论文设计条件，不证明任意外部副作用已可序列化；用户意图保持由事后 judge 测得，Airline 受限切片仍有 25.27% intent miss。固定 12 trajectory 预算下，仅加 junction chooser 的独特失败任务数从 78 降至 75，之后 diversity 分支才到 80/81；errors/token 与 distinct failures 不能合并为“绝对更高效”。硬件、精度、batch、concurrency、真实 wall-clock/SLO 未披露。

[Ch81](../../../../../books/part-07-agent/81-workflow.md) 已明确 authoritative workflow state、分叉/恢复与副作用边界，[Ch66](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 已版本化评价对象与分母。该文新增的是特定 user-simulation 采样 operating point，而非通用状态合同；维持 `2+2+2=6`、标准审阅、仅报告。真实用户风险概率不能从定向失败率推出。

## `2604.21523v1` Evaluator VLM Blind Spots：不同接口的失败率分母不可直排

[官方 §2–4、Appendix B](https://arxiv.org/html/2604.21523v1)人工筛过图文退化和不应改分的变体，比较 single scoring、pairwise 与 reference-guided VLM judge。Single 看分数稳定、pairwise 看是否选择预置 gold、reference 看是否给满分，三者事件定义不同；不能将列间失败率直接当同一测量下的 judge 排名。论文自己的 invariance 切片中 pairwise 更不稳定，说明“pairwise 最可靠”只限所选 VP 协议。变体可感知不等自然生成错误分布；其它 VLM 的理由再由 Gemini judge 归纳也不是人类独立感知证明。API 温度、prompt、模型版本之外的硬件/精度/batch/concurrency/SLO 不适用或未披露。

[Ch66](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 已要求固定评价接口、scorer 和输入扰动 identity，并把 judge 视作 sensor 而非真值 owner。保留此静态图像受限测试作为仅报告例证，维持 `2+2+2=6`、标准审阅；不采作者跨接口总体排序、不改默认 judge。

四项均未改 Books。至此本日报已有 36/36 个“仅报告”候选具名有限非作者核，但中心争议、来源、日期及否定侧仍未闭合。
