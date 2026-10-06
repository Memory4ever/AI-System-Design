# 03-17 增量：AgentRM 必要原证与 Books 判断

root 仅接作者明确尚未开始的 `2603.13110v1`；不扩发现，不改原候选、窗口或日期。完整题摘复用本日 `SUP_AB_THIRD_20261011.jsonl`。公开日复用本日已独核的官方公告规则与 DataCite 日级夹证：Submitted 03-13 不是公开日，03-16 的 findable/registered 上界与官方公开列表下界落同一北京时间自然日；不把 metadata 单独当公开时钟。本次再打开 exact-v1 abs，题名/作者/版本一致，当前页面无撤回说明。

## 必要审阅与贡献

原证：[exact-v1 HTML](https://arxiv.org/html/2603.13110v1)。实际读 §II、§III–V、§VI-A–D/Tables I–IX 与 §VII-A–D；不另遍历 GitHub issues、全部 framework 实现或版本史。

单一 FIFO 与按 session 截断 Context 在工作成本相近、短任务时仍合理；并发长任务、挂起和 provider 限流改变约束。原文实际提出由 gateway/API middleware 持有 execution-lane 队列、回收与 admission 状态，Context 管理器另持有 active/warm/cold 内容、压缩和休眠恢复，monitor 提供反馈。这一资源生命周期与 Context 控制分工值得核验，而不是因 OS 类比或项目名准入。评分 **2 + 2 + 2 = 6**；下列中心评价冲突触发受影响命题的深入审阅，不能通过降分或 NC 隐藏。

MLFQ 为三层任务队列与 priority boost；reaper 每 5 秒检查，挂起持 lane 超过 30 秒触发恢复，模拟中恢复成功概率设为 50%。Token bucket/AIMD/admission 与 DRF-inspired 分配仅由机制说明支持，并没有统一公平性或跨资源稳定性证明。Context value 采用 recency/importance/key-info 加权，warm SQLite、cold JSONL，压缩依赖小模型；Alg2 实际允许删除非 important 消息，并不支持无损“compress don't discard”。hibernation 的序列化说明不证明外部副作用提交、durable Workflow、versioned lease 或 exactly-once recovery。

## 中心证据冲突：不采用性能与质量保证

§VI-A 明确是根据观察模式构造的模拟负载：Normal 27 turns/3 agents/5% hang，High Load 280/10/10%，Burst 30 turns/3 秒/8%，Faulty 63/5/30%，Cascade 149/5/5–40% 波动。不是四万 issues 全量生产实验；issues 的抽样编码、实际模型/硬件/精度/token 长度、真实 concurrency/SLO、重复次数与不确定性 Not Disclosed。Context 表只给消息/token/key-msg 数量与窗口，不给 retention/quality 的充分定义、独立 evaluator 或质量估计误差。

- High Load Table II 的 P95 为 640439 → 323001 ms，降幅约 **49.6%**，不支持 §VI-D 所称同场景 86%；吞吐 14.6 → 24.5/min 是约 **67.8% 增加**，不是增加 168%；lane waste 2272 → 140 秒降约 **93.8%**，不是 96%。
- 同表 zombies 29 → **7**，不是摘要的 0 vs29；Normal/Burst 是 0，但不能拼接成 High Load 全消除。Faulty/Cascade 仍有 5/4 个 zombies，且 High Load 269 次 lags>30s，不是端到端响应保证。
- 200-turn Table VIII 的 key retention 为 **99.0%**，不是摘要的 100%；34,330 vs17,212 为压缩 token 成本，不是全链路费用。Table VI 的 No Management 100% retention 与较低 quality，也说明这两个指标不等价。
- Conclusion 45.2 requests/min 未由正文这些表的 AgentRM 行支持；没有必要材料能澄清其对应负载。不能挑选最有利场景或改写百分数后替作者证明整体中心主张。

这些是精确正文内部的直接反证，非单 seed 或未开源本身否定价值。模式说明可以保留为受限 proposal，但 advertised gains 与质量保持的中心归因尚未成立。

## Books 与终态建议（待独立复核）

实际读取 ROADMAP `AGENT-PLATFORM` Ch84 当前 **630–674** 与开篇、Ch83 尾部和 Part VII 导读。Ch84 **653** 已明确承载 lane/MLFQ/reaper/admission、Context 分层/compaction/hibernation、平台状态分权及模拟/production/lease 边界，未采用本篇宣传数字；不存在需要为本次再写一段的已核机制差额。

本 family 建议 **中心争议／暂缓**，无新 Books 写入；已有安全机制论点仍有效，不删除 Ch84，也不把“已有覆盖”当成中心争议已解决。精确重开材料只请求一次：与 Tables II/VI–IX 一致的场景和统计口径更正、retention/quality 定义与 evaluator、对应重复运行及回收/压缩消融；如要宣称 production 性能还需完整真实运行合同。外部保留不用于正面 Evidence、性能保证或无遗漏；身份/准入与必要审阅均已完成，不属于普通未读。
