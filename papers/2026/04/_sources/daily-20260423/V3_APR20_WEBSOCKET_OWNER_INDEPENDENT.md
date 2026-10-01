# Apr23 WebSockets 增量API处理：有限非作者采用核

复核者：apr20_resume；作者：root。实际重读当前AGENTS/研究合同/来源/Report/Prompt/ROADMAP；仅核本日 `V3_EVIDENCE_REVIEW.md` 两段literal、[OpenAI原工程文章](https://openai.com/index/speeding-up-agentic-workflows-with-websockets/)核心四节与当前Ch62相邻责任。不扩API全站、发布历史或厂商性能复现；未写Books，非写后或日Gate。

原文“API bottleneck”说明旧模型约65TPS与Spark特殊Cerebras约1000TPS是不同model/hardware，此前45%TTFT是多个sprint优化。完整history重复validation/rendering与tokenization在工具循环中累积，GPU越快越可成为瓶颈。上线“Keeping API familiar”明确保留 `response.create`、`previous_response_id` 与connection-scoped in-memory response/input/output/tool namespaces/rendered tokens；部分validators/classifiers处理new input、旧routing复用、billing交叠都有原文支持。`response.append`只属于弃用的单长response原型，不能写成上线接口。

当前 `PLATFORM-GATEWAY` / [Ch62](../../../../../books/part-06-ai-infrastructure/62-gateway.md) 的“LLM请求改变传统代理假设”实际列重试副作用、token预算、KV locality、streaming与reasoning effort；Gateway/EPP/engine各拥有外部策略、endpoint选择和模型执行。已有观测分解及Stateful Failover保留session identity/兼容转换/重建责任，但**未解释API前处理的connection-local rendered state与只处理delta的分支**。新增位置在request假设与Gateway/EPP交接之间合适；不是重复KV分页、Agent长期memory或一般会话迁移。

两literal source→实际owner **采用通过**：第一段的瓶颈变化、前序identity/增量前处理有原始机制；第二段资格变化/增量验证/显式重建为明确标注的系统设计推断，不冒充厂商已公开实现或安全证明。连接局部缓存不是durable restore，文章没有断线/跨连接迁移或全部classifier正确性保证。旧状态与模型/工具/策略身份不能由持久transport自动合资格；正文保短stateless请求共存、内存与失效代价及收益分解，且不抄40%普律。2+2+2=6合理，实际owner缺口触发必要深入，不因OpenAI/安全词或up-to数字统一深审。

批准仅限当前两段及唯一来源注释；还须作者实际写入、相邻顺读与另一人的真实写后核，不能先记整合。RSS Apr22 10:00Z窗口依据沿用作者实际记录，本次未重抓RSS或替代日级来源/日期Gate。

## 实际写后通过

作者写后，本人实际顺读Ch62:57–78（预算/effort旧段→新标题与两段→Gateway/EPP交接）及Review:240。两段真实存在，第一段保API/CPU状态与KV/Agent memory分账；第二段明确“从系统设计上”，保身份资格、组合校验非自动证明、断线/跨连接保证未披露、重建/stateless回退及性能不归因。未把弃用append原型或up-to40%写成普遍正文。相邻admission最终责任与三角色交接未覆盖/错置，源→owner最小增量已落正文。**actual write-after PASS**，不是Apr23日级Gate；未重抓不变来源。
