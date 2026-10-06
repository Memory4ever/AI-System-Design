# Daily Research — 2026-04-17

**规范：** V3
**窗口：** 2026-04-16T09:00:00+08:00 ～ 2026-04-17T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-09-27T12:57:00+08:00

## 1. 结论

本日已按现行合同完成重审，不沿用旧 V2.1 完成状态。旧 DOI-created 库存的536个身份及另一submitted库存的1059个身份仅作发现；不是本日论文数、贡献候选分母或证据审阅完成数。已对旧40项读完整题摘，536个标题作为有界查漏全览，有限强信号项已完成必要消歧；最终冻结89个唯一材料家族，不把宽库存全称为值得长期采用的研究。

89项必要证据与Books处置均已落实；准入负向抽检恢复14969后，有限题摘队列清空，并由非作者完成最终分母核对。89项均获具名单篇必要核验，50深入、35标准、4窄争议的有效证据继续复用。原39项Books队列按当前owner反向裁决关闭6项为仅报告，余33项均已真实写入并经root完整正文/邻接写后复核通过。最终33整合+17已有覆盖+35仅报告+4争议=89，普通未决0，非作者日级验收通过。四争议只隔离具体保证，不否定可分离经验；外部来源/日期限制仍安全保留，不声称无遗漏，也不将其改称Coverage或Evidence通过。

日期使用官方公告规则、连续ID/邻界、缓存OAI和自身v1 Updated的联合有界推断，不将Updated、submitted或DOI-created单独改名为首次公开。下表归属已按该联合依据接受为有界推断，不声称逐篇精确公告秒数；跨截点/后改字段的潜在贡献另行隔离，不机械移到邻日。来源目录成功只证明所列公开目录，仍有机构历史入口外部缺口。详细工作范围见[本日作者记录](../_sources/daily-20260417/v3-reopen-notes.md)，旧稿完整保留于[旧V2.1审计材料](../_sources/daily-20260417/v2.1-before-v3.md)。

## 2. 来源覆盖

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | News RSS本轮读取April15–18邻界，Codex04-16T10Z、Rosalind04-16T01Z原文已进入；前者功能披露、后者AI for Science范围关闭，不移入04-16T00Z和04-15事件 | 受阻 | Research历史日级分页未恢复；RSS不能替代全部Research目录 |
| SRC-ANTHROPIC | Research publishedOn实际重取，04-14T13:01Z→04-22T14:12:30.673Z跨窗，无本窗所列条目 | 已检查 | 仅该官方目录，不声称所有作者稿零遗漏 |
| SRC-GOOGLE-AI | DeepMind selected264项首屏04-22→03-22复用；Blog April目录9项实际读，04-16 Simula同家族2603.29791v1重复解释关闭、neuron范围关闭；邻04-13/21 | 受阻 | Google Publications历史日级目录未恢复；Blog日精度不补造时刻，其成功不替代Publications缺口 |
| SRC-META-AI | 复用已实际尝试的官方Research历史入口限制，未取可靠本窗目录停点 | 受阻 | 恢复官方带日期窗口目录；不报零命中 |
| SRC-QWEN | 动态API40条04-15T10+08→04-18T10+08跨窗，静态60条最晚2025-12复用 | 已检查 | 只覆盖官网research拼接目录 |
| SRC-DEEPSEEK | Research06-24→02-25、动态04-24→2025-12-01复用；本轮32个截止前非fork仓库release目录均到尾，共13个历史release、本窗0 | 已检查 | 不覆盖普通commits，不将仓库创建日期等同首次公开 |
| SRC-MOONSHOT | kimi-cli官方release page1/2各20条已实际读：1.35.0Apr15T12:55:10Z→1.36.0Apr17T14:10:46Z跨窗无release | 受阻 | 历史Kimi Blog不可由release目录替代 |
| SRC-TENCENT-HUNYUAN | publicList total9/list9复用；58个截止前非fork仓库中22个release目录实际到尾、本窗0；HY-SOAR同12617家族artifact线索已读 | 受阻 | 36个release目录明确403限流；created_at不证明首次公开，未将新仓库当新论文 |
| SRC-ZAI | 官方Research目录04-29→04-07→04-01跨窗复用；44个截止前仓库身份已读 | 受阻 | release补核遇403限流未完成，不报零；不将CMS createdAt作为first-public |
| SRC-BYTEDANCE-SEED | US论文APIpage20 actual20条/total242/next40，AgentWorldApr19T16Z→LeapAlignApr15T16Z跨窗；Blog95目录Apr22T16→Apr08T16→Mar31复用 | 已检查 | 只覆盖这两个官方目录，非全部作者稿 |
| SRC-BAIDU-ERNIE | Blog04-15→02-06→2025的本人实际读取复用，已知唯一release2025-06-30 | 已检查 | 未扫普通commits |
| SRC-XIAOMI-MIMO | Paper06-29→03-13→02-03跨窗复用 | 受阻 | 历史Blog未恢复；不能据Paper目录报Blog零更新 |
| SRC-MINIMAX | EN05-26→03-18/CN04-27→03-18复用；cli当窗1.0.8/9/10正式release、compare及必要PR89/78已读，逐事件贡献关闭 | 受阻 | Agent Tech Blog历史入口不可达；目录成功不替代该缺口 |
| SRC-ARXIV | 缓存当窗宽库存536题目作有界主线查漏；旧40完整题摘及有限新增主线信号已读，有限队列已清空，89个冻结family必要exact-v1已分批审阅，日期/准入经非作者有限核验 | 已检查 | 归属为官方公告规则、连续ID/邻界及缓存字段的联合有界推断；六项日期身份例外见§5，不继承created-owner，不声称536项全文审阅或全网零遗漏 |

普通可执行待办已处理完；表内受阻均为具名历史子入口的外部终态保留项，恢复条件见§5，不能据此声明相关来源零命中或完整覆盖。

## 3. 候选与判断

下表为最终冻结的89个唯一材料家族，各项证据与Books处置均已完成，33处必要正文改动及写后独立复核已落实。日期列采用自身早于截点的v1 Updated、官方公告槽、连续ID及OAI/邻界联合支持的08:00～09:00有界归属推断；非作者已核该联合依据与例外隔离，不声称逐篇秒级成功公告，原始字段不是公开时间。评分针对审阅的具体命题，不表示每项均值得进入Books。

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [Stateful Evidence-Centric RAG](https://arxiv.org/pdf/2604.14170v1) | 2026-04-17T08:00:00+08:00 ～ 2026-04-17T09:00:00+08:00 | 无关检索方向作为控制记忆，不冒充反驳事实；2+2+2=6 | 深入完成 | 整合：`AGENT-RAG` [Ch76](../../../../books/part-07-agent/76-rag.md) 无效搜索控制约束与事实反证分责；root实际正文/必要证据及相邻交接写后独立通过 |
| [Dive into Claude Code](https://arxiv.org/html/2604.14228v1) | 2026-04-17T08:00:00+08:00 ～ 2026-04-17T09:00:00+08:00 | 静态反编译观察与当前运行配置/安全保证分权；2+1+2=5 | 深入完成 | 已有覆盖：`PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) / `AGENT-MCP` [Ch83](../../../../books/part-07-agent/83-mcp.md)；Ch72 artifact初始化隔离与Ch83 admission/effect授权；仅该直接机制采用，二手共同预算线索不作Books事实 |
| [CoR](https://arxiv.org/html/2604.14246v1) | 2026-04-17T08:00:00+08:00 ～ 2026-04-17T09:00:00+08:00 | 离线expert贡献先验与在线routing融合，不等动态FLOPs保证；2+2+2=6 | 深入完成 | 整合：`MODEL-MOE` [Ch21](../../../../books/part-02-model/21-moe.md) offline virtual-ablation prior与当前router融合；root真实正文/邻接与必要证据复用写后独立通过 |
| [HYWorld2](https://arxiv.org/html/2604.14268v1) | 2026-04-17T08:00:00+08:00 ～ 2026-04-17T09:00:00+08:00 | 全局geometry与无序reference的布局/存储分工；2+2+2=6 | 深入完成 | 整合：`MULTIMODAL-WORLD-MODELS` [Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) reference空间packing/target时间身份与GGM分责；root真实正文/邻接与必要证据复用写后独立通过 |
| [APEXMEM](https://arxiv.org/html/2604.14362v1) | 2026-04-17T08:00:00+08:00 ～ 2026-04-17T09:00:00+08:00 | typed append-only memory与读取时冲突处理的受限验证；2+1+2=5 | 标准完成 | 已有覆盖：`AGENT-MEMORY` [Ch77](../../../../books/part-07-agent/77-memory.md)；Ch77 typed/evidence/validtime/supersession与受限GraphSQL |
| [ECG](https://arxiv.org/pdf/2604.14403v1) | 2026-04-17T08:00:00+08:00 ～ 2026-04-17T09:00:00+08:00 | 一份multi-vector同时服务retrieval与compressed reader；2+2+2=6 | 深入完成 | 整合：`AGENT-RAG` [Ch76](../../../../books/part-07-agent/76-rag.md) 共享Eret→Ecomp持久化表示与版本耦合；root实际正文/必要证据及相邻交接写后独立通过 |
| [Conversation Autocorrelation](https://arxiv.org/html/2604.14414v1) | 2026-04-17T08:00:00+08:00 ～ 2026-04-17T09:00:00+08:00 | 单轮IID评价与conversation-cluster有效样本分离；2+1+2=5 | 标准完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；Ch66 clustered抽样/会话bootstrap与独立单元 |
| [Geometric Metrics for MoE](https://arxiv.org/html/2604.14500v1) | 2026-04-17T08:00:00+08:00 ～ 2026-04-17T09:00:00+08:00 | routing concentration不等content specialization；中心等式反证；2+2+2=6 | 争议 | 暂缓：非作者已核中心Lemma1等式反例与单调保证缺条件，隔离受影响几何保证；不否定受限经验测量 |
| [CBCL](https://arxiv.org/html/2604.14512v1) | 2026-04-17T08:00:00+08:00 ～ 2026-04-17T09:00:00+08:00 | 动态grammar安装/展开资源与effect权限分权；2+2+2=6 | 深入完成 | 整合：`AGENT-MCP` [Ch83](../../../../books/part-07-agent/83-mcp.md) dialect安装/逐次展开双门；root真实正文/邻接及有效必要源复用写后PASS |
| [TRACER](https://arxiv.org/html/2604.14531v1) | 2026-04-17T08:00:00+08:00 ～ 2026-04-17T09:00:00+08:00 | teacher-agreement路由拟仅报告/已有覆盖待精确裁决；2+1+2=5 | 标准完成 | 仅报告：trace/surrogate/acceptor局部路由配方；5%为coverage floor、非shadow比例，test agreement未达目标 |
| [CoCoDiff](https://arxiv.org/html/2604.14561v1) | 2026-04-17T08:00:00+08:00 ～ 2026-04-17T09:00:00+08:00 | QKV readiness重排与DiT推理近似staleness分开；2+2+2=6 | 深入完成 | 整合：`TRAIN-DISTRIBUTED-TRAINING` [Ch36](../../../../books/part-04-training-system/36-distributed-training.md) QKV readiness精确重排与DiT推理跨步近似分权；root必要原文/实际正文及相邻交接写后独立通过 |
| [Don't Retrieve, Navigate](https://arxiv.org/html/2604.14572v1) | 2026-04-17T08:00:00+08:00 ～ 2026-04-17T09:00:00+08:00 | Ch76编译导航到原文dereference拟已有覆盖；2+1+2=5 | 标准完成 | 已有覆盖：`AGENT-RAG` [Ch76](../../../../books/part-07-agent/76-rag.md)；Ch76 corpus编译→导航→原文dereference及更新/ACL |
| [ConfLayers](https://arxiv.org/html/2604.14612v1) | 2026-04-17T08:00:00+08:00 ～ 2026-04-17T09:00:00+08:00 | 局部layer-search recipe拟仅报告；2+1+2=5 | 标准完成 | 仅报告：受限新机制/反证经非作者核验，不采用普遍保证 |
| [ELMoE3D](https://arxiv.org/html/2604.14626v1) | 2026-04-17T08:00:00+08:00 ～ 2026-04-17T09:00:00+08:00 | Ch49 bit-nested draft/verify存储与数据通路；2+2+2=6 | 深入完成 | 整合：`INFER-TENSORRT-LLM` [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md) Bit/MemoryTier共同网格与逐projection数据通路；root必要原文/实际正文及相邻交接写后独立通过 |
| [DR3-Eval](https://arxiv.org/html/2604.14683v1) | 2026-04-17T08:00:00+08:00 ～ 2026-04-17T09:00:00+08:00 | Ch66评价协议与证据分母拟已有覆盖；2+1+2=5 | 标准完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；Ch66独立evidence planes与expected-fact inventory |
| [Switching Efficiency](https://arxiv.org/html/2604.14690v1) | 2026-04-17T08:00:00+08:00 ～ 2026-04-17T09:00:00+08:00 | Ch36 useful/received/forwarded/capacity分账；2+2+2=6 | 深入完成 | 整合：`TRAIN-DISTRIBUTED-TRAINING` [Ch36](../../../../books/part-04-training-system/36-distributed-training.md) useful/received/forwarded/capacity-time同窗口分账；root必要原文/实际正文及相邻交接写后独立通过 |
| [Equifinality](https://arxiv.org/html/2604.14419v1) | 2026-04-17T08:00:00+08:00 ～ 2026-04-17T09:00:00+08:00 | 受限routing topology反证拟仅报告；2+1+2=5 | 标准完成 | 仅报告：受限新机制/反证经非作者核验，不采用普遍保证 |
| [Geometric Routing](https://arxiv.org/html/2604.14434v1) | 2026-04-17T08:00:00+08:00 ～ 2026-04-17T09:00:00+08:00 | Ch21 routing几何不等知识归属拟已有覆盖；2+1+2=5 | 标准完成 | 已有覆盖：`MODEL-MOE` [Ch21](../../../../books/part-02-model/21-moe.md)；Ch21 routing标签≠功能必要性、干预后的独立行为验收 |
| [Layered Mutability](https://arxiv.org/html/2604.14717v1) | 2026-04-17T08:00:00+08:00 ～ 2026-04-17T09:00:00+08:00 | prompt rollback后memory残留的受限实验拟仅报告；2+1+2=5 | 标准完成 | 仅报告：受限新机制/反证经非作者核验，不采用普遍保证 |
| [WAV](https://arxiv.org/html/2604.14732v1) | 2026-04-17T08:00:00+08:00 ～ 2026-04-17T09:00:00+08:00 | dual-noise CEM控制的受限配方拟仅报告；2+1+2=5 | 标准完成 | 仅报告：受限新机制/反证经非作者核验，不采用普遍保证 |
| [SWE-TRACE](https://arxiv.org/html/2604.14820v1) | 2026-04-17T08:00:00+08:00 ～ 2026-04-17T09:00:00+08:00 | privileged trace构造与partial-prefix PRM拟仅报告；2+1+2=5 | 标准完成 | 仅报告：privileged trace/partial-prefix PRM的受限组合；Table5有wall-clock，非完整等预算或生产SLO |
| [Nautilus](https://arxiv.org/html/2604.14825v1) | 2026-04-17T08:00:00+08:00 ～ 2026-04-17T09:00:00+08:00 | Ch49 scalar/VR/MA两级tile IR与repair成本；2+2+2=6 | 深入完成 | 整合：`INFER-TENSORRT-LLM` [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md) scalar/VR/MA分层融合与repair成本；root必要原文/实际正文及相邻交接写后独立通过 |
| [Solve Then Learn](https://arxiv.org/html/2604.14853v1) | 2026-04-17T08:00:00+08:00 ～ 2026-04-17T09:00:00+08:00 | 有限offline budget-router配方拟仅报告；2+1+2=5 | 标准完成 | 仅报告：离线solve→classifier摊销budget决策；平均近可行不等逐请求hard cap |
| [RACER](https://arxiv.org/html/2604.14885v1) | 2026-04-17T08:00:00+08:00 ～ 2026-04-17T09:00:00+08:00 | Ch48历史logit复用、bounded ancestry与验证责任；2+2+2=6 | 深入完成 | 整合：`INFER-SPECULATIVE-DECODING` [Ch48](../../../../books/part-05-inference-system/48-speculative-decoding.md) 有界历史proposal状态与target commit分权；root必要原文/实际正文及相邻交接写后独立通过 |
| [MemoSight](https://arxiv.org/html/2604.14889v1) | 2026-04-17T08:00:00+08:00 ～ 2026-04-17T09:00:00+08:00 | Ch45联合训练的foresight隔离/memory readout与KV逐出边界；2+2+2=6 | 深入完成 | 整合：`INFER-KV-CACHE` [Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) 预测隔离→memory形成→raw KV回收；root必要原文/实际正文及相邻交接写后独立通过 |
| [LongAct](https://arxiv.org/html/2604.14922v1) | 2026-04-17T08:00:00+08:00 ～ 2026-04-17T09:00:00+08:00 | Ch30实际mask、optimizer state与mask churn覆盖；2+1+2=5 | 标准完成 | 已有覆盖：`TRAIN-LORA` [Ch30](../../../../books/part-04-training-system/30-lora.md)；actual transient row-mask/optimizer state/mask churn，非仅主题对应 |
| [Serving Chain-structured Jobs](https://arxiv.org/html/2604.14993v1) | 2026-04-17T08:00:00+08:00 ～ 2026-04-17T09:00:00+08:00 | Ch56共享weight block与独占KV的chain capacity；2+2+2=6 | 深入完成 | 整合：`INFER-SCHEDULING` [Ch56](../../../../books/part-05-inference-system/56-inference-scheduling.md) 共享weight/独占KV的可行chain容量；root实际正文/必要证据及相邻交接写后独立通过 |
| [Mixture-of-Experts Flow Matching](https://arxiv.org/html/2604.15009v1) | 2026-04-17T08:00:00+08:00 ～ 2026-04-17T09:00:00+08:00 | Ch24多模态velocity平均与mixture likelihood分工；2+2+2=6 | 深入完成 | 整合：`MULTIMODAL-GENERATIVE-PARADIGMS` [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) mixture velocity目标与transport身份；root真实正文/邻接写后PASS |
| [Route to Rome Attack](https://arxiv.org/html/2604.15022v1) | 2026-04-17T08:00:00+08:00 ～ 2026-04-17T09:00:00+08:00 | Ch72 model-selection信号与资源授权分离；2+2+2=6 | 深入完成 | 仅报告：Ch72生成信号不拥有外部资源预算/stop/risk权限已承载采用原则；路由攻击配方仅报告；root当前owner反向语义裁决通过，不冒称精确recipe全部Existing |
| [Prefill-as-a-Service](https://arxiv.org/html/2604.15039v1) | 2026-04-17T08:00:00+08:00 ～ 2026-04-17T09:00:00+08:00 | Ch55 hybrid-state分组与跨DC incremental-prefill选择；2+2+2=6 | 深入完成 | 整合：`INFER-PD-DISAGGREGATION` [Ch55](../../../../books/part-05-inference-system/55-pd-disaggregation.md) 混合state恢复/prefix完整/tail交接生命周期；root必要原文/实际正文及相邻交接写后独立通过 |
| [Atropos](https://arxiv.org/html/2604.15075v1) | 2026-04-17T08:00:00+08:00 ～ 2026-04-17T09:00:00+08:00 | 仅报告GCN预测驱动的受限换模配方；2+1+2=5 | 标准完成 | 仅报告：GCN/多轨迹局部切换配方；sequential模式无context迁移，不保证普适无损hotswap |
| [IUQ](https://arxiv.org/html/2604.15109v1) | 2026-04-17T08:00:00+08:00 ～ 2026-04-17T09:00:00+08:00 | Ch66同源问答冲突不等truth与校准已有覆盖；2+1+2=5 | 标准完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；atomic claim依赖/独立evidence/同源偏差与校准分权 |
| [LLMs Gaming Verifiers](https://arxiv.org/html/2604.15149v1) | 2026-04-17T08:00:00+08:00 ～ 2026-04-17T09:00:00+08:00 | Ch31固定hypothesis的isomorphic双验收；2+2+2=6 | 深入完成 | 整合：`TRAIN-RLHF` [Ch31](../../../../books/part-04-training-system/31-rlhf.md) text-only preference/声学anchor与同H保义双检；root真实正文及相邻段写后PASS |
| [When Flat Minima Fail](https://arxiv.org/html/2604.15167v1) | 2026-04-17T08:00:00+08:00 ～ 2026-04-17T09:00:00+08:00 | Ch49 checkpoint轨迹与量化probe的独立发布验收；2+2+2=6 | 深入完成 | 整合：`INFER-TENSORRT-LLM` [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md) checkpoint×量化probe独立验收；root必要原文/实际正文及相邻交接写后独立通过 |
| [MixAtlas](https://arxiv.org/html/2604.14198v1) | 2026-04-17T08:00:00+08:00 ～ 2026-04-17T09:00:00+08:00 | Ch27内容分区与监督分区两轴分别优化，不证明联合交互；2+2+2=6 | 深入完成 | 仅报告：Ch27格式/内容两轴与simplex交互、pilot迁移已承载采用原则；独立GP-UCB配方仅报告；root当前owner反向语义裁决通过，不冒称精确recipe全部Existing |
| [Three-Phase Transformer](https://arxiv.org/html/2604.14430v1) | 2026-04-17T08:00:00+08:00 ～ 2026-04-17T09:00:00+08:00 | 残差分区配方与FP32数值反证分离；2+1+2=5 | 深入完成 | 仅报告：受限配方/窄数值纠错独立通过，不采用FP32下溢保证 |
| [Adaptive Visual Reasoning](https://arxiv.org/html/2604.14568v1) | 2026-04-17T08:00:00+08:00 ～ 2026-04-17T09:00:00+08:00 | 感知/完整推理/直接回答格式reward的局部取舍；2+1+2=5 | 标准完成 | 仅报告：visual格式reward与collapse控制配方；省显式trace不等未编码视觉/latency保证 |
| [Masked Logit Nudging](https://arxiv.org/html/2604.14591v1) | 2026-04-17T08:00:00+08:00 ～ 2026-04-17T09:00:00+08:00 | Ch24离散source概率方向、mask与量化修复分权；2+2+2=6 | 深入完成 | 整合：`MULTIMODAL-GENERATIVE-PARADIGMS` [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) 概率nudging/mask约束与量化修复；root真实正文/邻接写后PASS |
| [CW-GRPO](https://arxiv.org/html/2604.14267v1) | 2026-04-17T08:00:00+08:00 ～ 2026-04-17T09:00:00+08:00 | outcome方向与judge round幅度分离；2+1+2=5 | 标准完成 | 已有覆盖：`TRAIN-GRPO` [Ch33](../../../../books/part-04-training-system/33-grpo.md)；verifier方向/teacher幅度及phase/segment credit实际正文 |
| [RUMS](https://arxiv.org/html/2604.14473v1) | 2026-04-17T08:00:00+08:00 ～ 2026-04-17T09:00:00+08:00 | entropy-surrogate selector与最优utility保证分离；2+1+2=5 | 深入完成 | 仅报告：非作者已核subset-independent residual entropy的推导反例；隔离该桥，不否定全部经验utility排序 |
| [HyPeR](https://arxiv.org/html/2604.14806v1) | 2026-04-17T08:00:00+08:00 ～ 2026-04-17T09:00:00+08:00 | audio显式trace与概率触发latent预算分流；2+1+2=5 | 标准完成 | 仅报告：受限audio gating/reward配方；external Omni baseline和自身Audio训练base分开，概率不是truth |
| [TrigReason](https://arxiv.org/html/2604.14847v1) | 2026-04-17T08:00:00+08:00 ～ 2026-04-17T09:00:00+08:00 | Ch56每步打分改为有代价的事件触发交接；2+2+2=6 | 深入完成 | 整合：`INFER-SCHEDULING` [Ch56](../../../../books/part-05-inference-system/56-inference-scheduling.md) 事件触发替换/有限接管与返回点；root实际正文/必要证据及相邻交接写后独立通过 |
| [TESSY](https://arxiv.org/html/2604.14164v1) | 2026-04-17T08:00:00+08:00 ～ 2026-04-17T09:00:00+08:00 | Ch29监督样本的局部producer交替与rollback边界；2+2+2=6 | 深入完成 | 整合：`TRAIN-SFT` [Ch29](../../../../books/part-04-training-system/29-sft.md) 失败历史/监督mask与逐span producer/rollback边界；root真实正文/邻接及必要证据复用写后PASS |
| [Attention to Mamba](https://arxiv.org/html/2604.14191v1) | 2026-04-17T08:00:00+08:00 ～ 2026-04-17T09:00:00+08:00 | Ch22中间算子匹配、替换初始化与解锁动力学分权；2+2+2=6 | 深入完成 | 整合：`MODEL-LONG-CONTEXT` [Ch22](../../../../books/part-02-model/22-long-context.md) 中间算子匹配/完整替换/受控解锁；root真实正文/邻接写后PASS |
| [FRESCO](https://arxiv.org/html/2604.14227v1) | 2026-04-17T08:00:00+08:00 ～ 2026-04-17T09:00:00+08:00 | 时效hard negatives暴露semantic rank不等事实validity；2+1+2=5 | 标准完成 | 已有覆盖：`AGENT-RAG` [Ch76](../../../../books/part-07-agent/76-rag.md)；query事实时点/source有效期/corpus revision联合admission |
| [Calibrate-Then-Delegate](https://arxiv.org/html/2604.14251v1) | 2026-04-17T08:00:00+08:00 ～ 2026-04-17T09:00:00+08:00 | 升级效用预测与总体delegation-rate预算校准分权；2+2+2=6 | 深入完成 | 整合：`INFER-SCHEDULING` [Ch56](../../../../books/part-05-inference-system/56-inference-scheduling.md) efficacy差值预测/独立testing总体委派率预算；root实际正文/必要证据及相邻交接写后独立通过 |
| [Generalized Fine-Tuning](https://arxiv.org/html/2604.14258v1) | 2026-04-17T08:00:00+08:00 ～ 2026-04-17T09:00:00+08:00 | 混合轨迹配方与loss/gradient中心冲突分离；2+1+2=5 | 争议 | 暂缓：仅隔离Eq21→22与固有梯度爆炸保证，不否定局部经验 |
| [GUI-Perturbed](https://arxiv.org/html/2604.14262v1) | 2026-04-17T08:00:00+08:00 ～ 2026-04-17T09:00:00+08:00 | 同任务视觉×指令扰动分账，不由阶段组合归因RL/CE；2+1+2=5 | 标准完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；交叉任务轴/paired oracle与因果混杂分账 |
| [GeoDe](https://arxiv.org/html/2604.14324v1) | 2026-04-17T08:00:00+08:00 ～ 2026-04-17T09:00:00+08:00 | probe拒答训练的unsigned-distance分区算法矛盾；2+1+2=5 | 争议 | 暂缓：d≥0与d<0未知类中心冲突独立核实，保留经验不采用算法保证 |
| [Faithfulness Serum](https://arxiv.org/html/2604.14325v1) | 2026-04-17T08:00:00+08:00 ～ 2026-04-17T09:00:00+08:00 | 后置解释归因干预与原决策因果/选择分母分离；2+1+2=5 | 标准完成 | 仅报告：受限解释干预独立通过，不证明原决策faithfulness |
| [RoPE-Perturbed Self-Distillation](https://arxiv.org/html/2604.14339v1) | 2026-04-17T08:00:00+08:00 ～ 2026-04-17T09:00:00+08:00 | 内容与mask固定、index扰动一致性作为适配目标；2+2+2=6 | 深入完成 | 整合：`MODEL-LONG-CONTEXT` [Ch22](../../../../books/part-02-model/22-long-context.md) 同内容/mask下的suffix index一致性；root真实正文/邻接写后PASS |
| [Tight Sample Complexity Bounds for Best-Arm Identification Under Bounded Systematic Bias](https://arxiv.org/html/2604.14345v1) | 2026-04-17T08:00:00+08:00 ～ 2026-04-17T09:00:00+08:00 | 噪声方差与systematic-bias上界不能互换；2+1+2=5 | 深入完成 | 仅报告：静态已知L条件化剪枝保留，动态安全保证窄反证独立通过 |
| [Cost of Language](https://arxiv.org/html/2604.14363v1) | 2026-04-17T08:00:00+08:00 ～ 2026-04-17T09:00:00+08:00 | centroid介入的模态依赖与task/answer接口混杂分离；2+1+2=5 | 标准完成 | 仅报告：受限centroid配方及反例独立通过，不采用模态因果保证 |
| [Step-level Denoising-time Diffusion Alignment with Multiple Objectives](https://arxiv.org/html/2604.14379v1) | 2026-04-17T08:00:00+08:00 ～ 2026-04-17T09:00:00+08:00 | step surrogate与Gaussian逆条件融合的条件接口；2+2+2=6 | 深入完成 | 整合：`MULTIMODAL-GENERATIVE-PARADIGMS` [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) 局部reverse conditional融合接口；root真实正文/邻接写后PASS |
| [Zero-Ablation Overstates Register Content Dependence in DINO Vision Transformers](https://arxiv.org/html/2604.14433v1) | 2026-04-17T08:00:00+08:00 ～ 2026-04-17T09:00:00+08:00 | 干预baseline区分内容缺失与分布偏移；2+2+2=6 | 深入完成 | 整合：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 替换baseline因果对象；root真实正文/邻接及有效必要源复用写后PASS |
| [Hierarchical vs. Flat Iteration in Shared-Weight Transformers](https://arxiv.org/html/2604.14442v1) | 2026-04-17T08:00:00+08:00 ～ 2026-04-17T09:00:00+08:00 | 共享参数、循环KV与结构/调参效应分账；2+1+2=5 | 标准完成 | 仅报告：受控层级/调参反证通过，具体recipe不假称全部已有覆盖 |
| [Controlling Authority Retrieval: A Missing Retrieval Objective for Authority-Governed Knowledge](https://arxiv.org/html/2604.14488v1) | 2026-04-17T08:00:00+08:00 ～ 2026-04-17T09:00:00+08:00 | semantic anchor后的authority闭合责任不等时效过滤；2+2+2=6 | 深入完成 | 整合：`AGENT-RAG` [Ch76](../../../../books/part-07-agent/76-rag.md) entity-scoped authority后继主动补检；root实际正文/必要证据及相邻交接写后独立通过 |
| [CURaTE: Continual Unlearning in Real Time with Ensured Preservation of LLM Knowledge](https://arxiv.org/html/2604.14644v1) | 2026-04-17T08:00:00+08:00 ～ 2026-04-17T09:00:00+08:00 | 持续拒答与参数影响删除必须分别验收；2+1+2=5 | 深入完成 | 已有覆盖：`PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)；行为抑制/parameter influence/retained utility分账 |
| [Bounded Autonomy for Enterprise AI: Typed Action Contracts and Consumer-Side Execution](https://arxiv.org/pdf/2604.14723v1) | 2026-04-17T08:00:00+08:00 ～ 2026-04-17T09:00:00+08:00 | 语法/授权有效仍可能绑定错误实体；2+1+2=5 | 深入完成 | 已有覆盖：`AGENT-TOOL-CALLING` [Ch78](../../../../books/part-07-agent/78-tool-calling.md)；结构有效/授权/确定性实体binding与commit分权 |
| [Schema Key Wording as an Instruction Channel in Structured Generation under Constrained Decoding](https://arxiv.org/html/2604.14862v1) | 2026-04-17T08:00:00+08:00 ～ 2026-04-17T09:00:00+08:00 | schema key同时是grammar结构与语义条件prefix；2+2+2=6 | 深入完成 | 整合：`MODEL-SAMPLING` [Ch20](../../../../books/part-02-model/20-sampling.md) schema key-prefix语义通道/grammar与字段身份分权；root真实正文/邻接与必要证据复用写后独立通过 |
| [Segment-Level Coherence for Robust Harmful Intent Probing in LLMs](https://arxiv.org/html/2604.14865v1) | 2026-04-17T08:00:00+08:00 ～ 2026-04-17T09:00:00+08:00 | 弱exchange标签的pooling目标与在线风险触发分离；2+2+2=6 | 深入完成 | 仅报告：Ch72sensor/parser/aggregation及prefix持续probe与authority分责已承载采用原则；弱标签pooling配方仅报告；root当前owner反向语义裁决通过，不冒称精确recipe全部Existing |
| [On the Expressive Power and Limitations of Multi-Layer SSMs](https://arxiv.org/html/2604.14501v1) | 2026-04-17T08:00:00+08:00 ～ 2026-04-17T09:00:00+08:00 | post-input与input-interleaved计算改变不同信息路径；2+1+2=5 | 标准完成 | 仅报告：非作者必要原文/实际owner及关键反证核通过，不采用普遍保证 |
| [Dissecting Failure Dynamics in Large Language Model Reasoning](https://arxiv.org/html/2604.14528v1) | 2026-04-17T08:00:00+08:00 ～ 2026-04-17T09:00:00+08:00 | 定点entropy触发/局部分叉仍不授予truth判断；2+1+2=5 | 标准完成 | 已有覆盖：`AGENT-REFLECTION` [Ch80](../../../../books/part-07-agent/80-reflection.md)；cheap entropy sensor→bounded repair与probe/net cost分账 |
| [VoxSafeBench: Not Just What Is Said, but Who, How, and Where](https://arxiv.org/html/2604.14548v1) | 2026-04-17T08:00:00+08:00 ～ 2026-04-17T09:00:00+08:00 | 同音频cue识别与normative decision的配对验收；2+2+2=6 | 深入完成 | 仅报告：Ch66感知/推理与grounding/规则应用分账已承载采用原则；matched cue任务仅报告；root当前owner反向语义裁决通过，不冒称精确recipe全部Existing |
| [MARS2: Scaling Multi-Agent Tree Search via Reinforcement Learning for Code Generation](https://arxiv.org/html/2604.14564v1) | 2026-04-17T08:00:00+08:00 ～ 2026-04-17T09:00:00+08:00 | 树内共享credit参照与各policy节点更新所有权分开；2+2+2=6 | 深入完成 | 整合：`TRAIN-GRPO` [Ch33](../../../../books/part-04-training-system/33-grpo.md) 共享tree参照与各policy producer更新分责；root完整正文/邻接写后PASS |
| [Prompt Optimization Is a Coin Flip: Diagnosing When It Helps in Compound AI Systems](https://arxiv.org/html/2604.14585v1) | 2026-04-17T08:00:00+08:00 ～ 2026-04-17T09:00:00+08:00 | 交互不显著不等于不存在，优化收益须绑定pipeline与held-out选择；2+1+2=5 | 深入完成 | 仅报告：非作者必要原文/实际owner及关键反证核通过，不采用普遍保证 |
| [AgileLog: A Forkable Shared Log for Agents on Data Streams](https://arxiv.org/html/2604.14590v1) | 2026-04-17T08:00:00+08:00 ～ 2026-04-17T09:00:00+08:00 | live fork继承append与promotion读屏障不能同时当零干扰；2+2+2=6 | 深入完成 | 整合：`AGENT-WORKFLOW` [Ch81](../../../../books/part-07-agent/81-workflow.md) live/static、promotable读屏障/catch-up；root真实正文/邻接及有效必要源复用写后PASS |
| [Hijacking Large Audio-Language Models via Context-Agnostic and Imperceptible Auditory Prompt Injection](https://arxiv.org/html/2604.14604v1) | 2026-04-17T08:00:00+08:00 ～ 2026-04-17T09:00:00+08:00 | 音频内部内容与用户授权分开，probe-aware攻击下检测合同须重验；2+2+2=6 | 深入完成 | 仅报告：Ch72adaptive反馈/变异/效果闭环与probe版本重验已承载采用原则；detector-aware音频攻击配方仅报告；root当前owner反向语义裁决通过，不冒称精确recipe全部Existing |
| [Pushing the Boundaries of Multiple Choice Evaluation to One Hundred Options](https://arxiv.org/html/2604.14634v1) | 2026-04-17T08:00:00+08:00 ～ 2026-04-17T09:00:00+08:00 | 选项密度、长度与位置必须分轴，不以多选项自动提升有效性；2+1+2=5 | 标准完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；Position–Content–Length轴/响应CDF/接口分账 |
| [Acceptance Dynamics Across Cognitive Domains in Speculative Decoding](https://arxiv.org/html/2604.14682v1) | 2026-04-17T08:00:00+08:00 ～ 2026-04-17T09:00:00+08:00 | 候选节点接受概率均值不等真实路径接受与端到端收益；2+1+2=5 | 深入完成 | 仅报告：非作者必要原文/实际owner及关键反证核通过，不采用普遍保证 |
| [Gating Enables Curvature: A Geometric Expressivity Gap in Attention](https://arxiv.org/html/2604.14702v1) | 2026-04-17T08:00:00+08:00 ～ 2026-04-17T09:00:00+08:00 | 固定value仿射系数模型的平坦性不等任意无gate注意力限制；2+1+2=5 | 标准完成 | 仅报告：非作者必要原文/实际owner及关键反证核通过，不采用普遍保证 |
| [A Mechanistic Account of Attention Sinks in GPT-2: One Circuit, Broader Implications for Mitigation](https://arxiv.org/html/2604.14722v1) | 2026-04-17T08:00:00+08:00 ～ 2026-04-17T09:00:00+08:00 | sink的具体电路与跨架构普适归因分离；2+1+2=5 | 标准完成 | 已有覆盖：`MODEL-SELF-ATTENTION` [Ch14](../../../../books/part-02-model/14-self-attention.md)；跨token/depth受控干预与拒绝普适单因 |
| [Expressivity of Transformers: A Tropical Geometry Perspective](https://arxiv.org/html/2604.14727v1) | 2026-04-17T08:00:00+08:00 ～ 2026-04-17T09:00:00+08:00 | 零温条件query几何不等有限温完整Transformer精确分区；2+1+2=5 | 深入完成 | 仅报告：非作者必要原文/实际owner及关键反证核通过，不采用普遍保证 |
| [Constraint-based Pre-training: From Structured Constraints to Scalable Model Initialization](https://arxiv.org/html/2604.14769v1) | 2026-04-17T08:00:00+08:00 ～ 2026-04-17T09:00:00+08:00 | 预训练模板的可迁移初始化接口不同于任意checkpoint无成本扩形；2+2+2=6 | 深入完成 | 整合：`TRAIN-PRETRAINING` [Ch28](../../../../books/part-04-training-system/28-pretraining.md) 主动模板预训练/目标适配；root真实正文/邻接及有效必要源复用写后PASS |
| [Knowing When Not to Answer: Evaluating Abstention in Multimodal Reasoning Systems](https://arxiv.org/html/2604.14799v1) | 2026-04-17T08:00:00+08:00 ～ 2026-04-17T09:00:00+08:00 | 不可回答类型、answerable代价与选择后的拒答统计分开；2+1+2=5 | 标准完成 | 仅报告：非作者必要原文/实际owner及关键反证核通过，不采用普遍保证 |
| [Modeling LLM Unlearning as an Asymmetric Two-Task Learning Problem](https://arxiv.org/html/2604.14808v1) | 2026-04-17T08:00:00+08:00 ～ 2026-04-17T09:00:00+08:00 | retain-first梯度方向与真实遗忘/utility保证分离；2+1+2=5 | 深入完成 | 仅报告：非作者必要原文/实际owner及关键反证核通过，不采用普遍保证 |
| [Does RL Expand the Capability Boundary of LLM Agents? A PASS@(k,T) Analysis](https://arxiv.org/html/2604.14877v1) | 2026-04-17T08:00:00+08:00 ～ 2026-04-17T09:00:00+08:00 | 采样k与交互T两轴不能把有限未命中当绝对能力不存在；2+2+2=6 | 深入完成 | 仅报告：Ch66可靠性、宽度×深度预算与matched compute已承载采用原则；精确pass(k,T)实验仅报告；root当前owner反向语义裁决通过，不冒称精确recipe全部Existing |
| [Reasoning Dynamics and the Limits of Monitoring Modality Reliance in Vision-Language Models](https://arxiv.org/html/2604.14888v1) | 2026-04-17T08:00:00+08:00 ～ 2026-04-17T09:00:00+08:00 | 已知hint探测与未知模态归因不是同一monitor任务；2+1+2=5 | 深入完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；provenance/cue/self-report分权 |
| [Beyond Importance Sampling: Rejection-Gated Policy Optimization](https://arxiv.org/html/2604.14895v1) | 2026-04-17T08:00:00+08:00 ～ 2026-04-17T09:00:00+08:00 | 可微gate有效梯度w=g′r不等无偏IS或无条件单调改进；2+2+2=6 | 争议 | 暂缓：非作者已核Eq40于r=1的反例及未处理的occupancy shift，仅隔离policy-improvement保证，保留surrogate/经验记录 |
| [Reward-Aware Trajectory Shaping for Few-step Visual Generation](https://arxiv.org/html/2604.14910v1) | 2026-04-17T08:00:00+08:00 ～ 2026-04-17T09:00:00+08:00 | sigma horizon上的teacher引导与terminal reward分工；2+1+2=5 | 标准完成 | 仅报告：非作者必要原文/实际owner及关键反证核通过，不采用普遍保证 |
| [WavAlign: Enhancing Intelligence and Expressiveness in Spoken Dialogue Models via Adaptive Hybrid Post-Training](https://arxiv.org/html/2604.14932v1) | 2026-04-17T08:00:00+08:00 ～ 2026-04-17T09:00:00+08:00 | text-token preference与all-token声学anchor责任不同，mask不隔离参数；2+2+2=6 | 深入完成 | 整合：`TRAIN-RLHF` [Ch31](../../../../books/part-04-training-system/31-rlhf.md) text-only preference/声学anchor与同H保义双检；root真实正文及相邻段写后PASS |
| [Discovering Novel LLM Experts via Task-Capability Coevolution](https://arxiv.org/html/2604.14969v1) | 2026-04-17T08:00:00+08:00 ～ 2026-04-17T09:00:00+08:00 | 任务归档变更后重评旧模型skill-reference，双archive控制不等答案selector；2+1+2=5 | 标准完成 | 仅报告：恢复误拒绝；具体反馈接口成立，但static对照是gen5代理、Coverage与BoN分开，不采用普遍coevolution收益 |
| [What Is the Minimum Architecture for Prolepsis? Early Irrevocable Commitment Across Tasks in Small Transformers](https://arxiv.org/html/2604.15010v1) | 2026-04-17T08:00:00+08:00 ～ 2026-04-17T09:00:00+08:00 | paired steering/skip复制限制普遍早commit与16层门槛；2+1+2=5 | 标准完成 | 仅报告：同一Llama双答案筛选条件已纠正，受限复制经非作者复核 |
| [ControlFoley: Unified and Controllable Video-to-Audio Generation with Cross-Modal Conflict Handling](https://arxiv.org/html/2604.15086v1) | 2026-04-17T08:00:00+08:00 ～ 2026-04-17T09:00:00+08:00 | reference保style但抑时间接口、visual保sync；2+2+2=6 | 深入完成 | 整合：`MULTIMODAL-REPRESENTATION` [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) reference音色/target事件时间身份分责；root真实正文/邻接与必要证据复用写后独立通过 |
| [OpenMobile: Building Open Mobile Agents with Task and Trajectory Synthesis](https://arxiv.org/html/2604.15093v1) | 2026-04-17T08:00:00+08:00 ～ 2026-04-17T09:00:00+08:00 | learner错误保context、expert步骤才作为SFT target；2+2+2=6 | 深入完成 | 整合：`TRAIN-SFT` [Ch29](../../../../books/part-04-training-system/29-sft.md) 失败历史/监督mask与逐span producer/rollback边界；root真实正文/邻接及必要证据复用写后PASS |
| [From Procedural Skills to Strategy Genes: Towards Experience-Driven Test-Time Evolution](https://arxiv.org/html/2604.15097v1) | 2026-04-17T08:00:00+08:00 ～ 2026-04-17T09:00:00+08:00 | matched包装/预算对照揭示经验压缩非单调收益；2+1+2=5 | 标准完成 | 仅报告：受限机制与反证经非作者复核，不采用普遍保证 |
| [IG-Search: Step-Level Information Gain Rewards for Search-Augmented Reasoning](https://arxiv.org/html/2604.15148v1) | 2026-04-17T08:00:00+08:00 ～ 2026-04-17T09:00:00+08:00 | gold-conditioned检索proxy与query-only credit责任分离；2+2+2=6 | 深入完成 | 整合：`TRAIN-GRPO` [Ch33](../../../../books/part-04-training-system/33-grpo.md) gold-conditioned document/refinement代理与query-only credit；root完整正文/邻接写后PASS |
| [DPC: Training-Free Text-to-SQL Candidate Selection via Dual-Paradigm Consistency](https://arxiv.org/html/2604.15163v1) | 2026-04-17T08:00:00+08:00 ～ 2026-04-17T09:00:00+08:00 | 区分top2的MDD与参考语义正确性是不同契约；2+1+2=5 | 标准完成 | 仅报告：受限机制与反证经非作者复核，不采用普遍保证 |
| [An Analysis of Regularization and Fokker–Planck Residuals in Diffusion Models for Image Generation](https://arxiv.org/html/2604.15171v1) | 2026-04-17T08:00:00+08:00 ～ 2026-04-17T09:00:00+08:00 | FP residual、感知质量和penalty训练成本需分别测；2+1+2=5 | 标准完成 | 仅报告：受限机制与反证经非作者复核，不采用普遍保证 |

## 4. 证据与知识整合

### [Stateful Evidence-Centric RAG](https://arxiv.org/pdf/2604.14170v1)

材料家族：SF-2026-ARXIV-2604-14170。

[官方PDF v1](https://arxiv.org/pdf/2604.14170v1) §3.3.1–3.4把每篇检索文档转换为SRU，并分Supportive/Contextual/Irrelevant；negative pool指无关方向，不是事实反驳证据，confidence为相关性而非正确概率。SRU长期存于pool，query augmentation只是临时控制信号。保留无效方向以减少重复探路与原始事实权威是不同责任；stop/abstention仍由同一LLM判断，不因此知道自己的知识边界。

§4.4/§5.2用GPT-4.1-mini、DPR/FAISS Wikipedia top5、每任务同2000题、最多5轮比较去SRU/去Irrelevant。ASQA和2WikiMultiHopQA对照支持局部结构/负搜索记忆组合，但Context长度、tool调用总数和端到端预算未匹配，不能从删除一项性能下降推出无偏因果或可靠abstention。LLaMA3.1-8B结果较弱；6轮非所有指标更好。硬件、precision、concurrency、SLO未披露，不引用生产提速。

现Ch76 relevance→sufficiency/verification及episode state已承载主流程，拟补“irrelevant-search memory与contradictory-fact evidence不可混同”的窄状态分支；已实际写入并经root顺读真实正文/相邻交接、复用有效必要证据后独立写后PASS。 非作者apr01重开PDF §3.3.1–3.4/4.4/5.2并对读Ch76 typed state/gap-repair正文后确认真实gap：Irrelevant可作query negative constraint，augmented query为临时控制状态，不能当反驳事实；Source→owner通过不等实际写入或日级Gate。

### [Dive into Claude Code](https://arxiv.org/html/2604.14228v1)

材料家族：SF-2026-ARXIV-2604-14228。

[官方HTML v1](https://arxiv.org/html/2604.14228v1) §11.3、§16分析公开npm提取的v2.1.88静态代码。Tier B不是官方生产行为证据：feature gates、启用状态、作者意图与runtime prevalence均未证。五值/十三原则归纳本身不是新系统机制。

必要安全线索在初始化顺序：extension/hook/MCP预信任执行不受后续deny-first保护；共享性能预算共同降级只作为该文二手分析线索，本轮未核该具体案例、不作为Books采用事实。该论文是公开CVE/第三方研究的综合，不在本日重新宣布那些旧CVE。拟采用的长期命题由Ch72 artifact装载/初始化前隔离、Ch83 admission与effect-time authorization实际承载，不因此证明当前Claude版本仍可被同样攻击。安全触发深入范围仅该采用命题，不逐项复制整份architecture。

### [CoR](https://arxiv.org/html/2604.14246v1)

材料家族：SF-2026-ARXIV-2604-14246。

[官方HTML v1](https://arxiv.org/html/2604.14246v1) §3.1–3.3/Eq1–9在冻结C4校准hard tokens上虚拟移除已激活expert并再归一化，形成offline贡献先验，与当前router signal融合；层预算由hard/easy loss ratio调节。CEI不是当前用户问题的事实oracle，近似保持active专家计数不等FLOPs/latency/SLO相同。

§4 Tables1–3单H10080G、DeepSeek-V2-Lite/Qwen3-30B-A3B/GPT-OSS20B有负面结果：DeepSeek Trivia42.25→41.89、GSM20.02→17.52，general-task平均也非全面不退。校准漂移和dispatch形状固定时原Top-k仍合理。Ch21已有layer allocation，但offline prior与runtime counterfactual的分权已在本轮实际新增并写后通过；非作者apr01重开必要Eq3–9/关键表及现有层预算/反事实正文，source→owner通过，现已实际写入并经root顺读真实正文及邻接/必要证据复用后写后独立PASS。

### [HYWorld2](https://arxiv.org/html/2604.14268v1)

材料家族：SF-2026-ARXIV-2604-14268。

[官方HTML v1](https://arxiv.org/html/2604.14268v1) §5.1–5.3区分global geometry guidance与detail references：无序retrieved view沿空间拼入target，继承其时间索引、统一camera坐标，而不是强行伪造连续history。生成后保存RGB+camera按FoV取有限reference，改变bank和reader接口而非原始世界真实性。

Tables7–8支持受测布局分支，但FFN/augmentation/batch等非全部单变量，distillation ATE .041→.072退步。全局点云强guidance也可能放大depth误差。拟在Ch25记忆演进中加入global prior vs unordered reference分权，非action-conditioned物理因果/控制安全保证；非作者apr01重开必要§5.2.1–5.3/§8.1.3 Table8及现memory正文，source→owner通过，已实际写入相应owner正文，root完整正文/邻接及有效必要证据复用写后PASS。

### [APEXMEM](https://arxiv.org/html/2604.14362v1)

材料家族：SF-2026-ARXIV-2604-14362。

[官方HTML v1](https://arxiv.org/html/2604.14362v1) §3–4/§6 Tables2–3/AppendixF的typed append-only event/property graph保存evidence spans，在读取时处理时间与冲突，GraphSQL只读且与hybrid检索分工。Ch77 typed transition、anchor→bounded expansion与supersession已实际承载这条采用命题。跨系统分数是indirect evidence，不能归因append-only；组合工具消融不建立开放生产保证。非作者有限source→实际owner复核通过，标准已有覆盖，不新增同义段。

### [ECG](https://arxiv.org/pdf/2604.14403v1)

材料家族：SF-2026-ARXIV-2604-14403。

[官方PDF v1](https://arxiv.org/pdf/2604.14403v1) §3–5让Eret经projection得Ecomp，document只持久化一份multi-vector；retriever/reader共同训练，learned temperature/teacher score scale缓解任务竞争。Ch76现compression net-benefit未说明这种存储耦合替代分支，拟必要深入整合。

SmolLM2 135M/Gemma3 1B、pooled Wikipedia NQ/TriviaQA、top1 document；context budget只计document vectors，disk仅embeddings不含index/原文/model；不能据on-device目标声称手机能耗/SLO已测。更多documents可退，去scaling NQ .343→.173只支持该配方。原文需可回取供provenance/删除/重新编码；latent不拥有事实权威。非作者apr17_final_batch_review实际读PDF §3–5/Table1–4并视觉核页4公式/页21Table4，对读Ch76 compression net-benefit后确认共享持久化表示/reader兼容性真实缺口；source→owner通过，已实际写入相应owner正文，root完整正文/邻接及有效必要证据复用写后PASS。

### [Conversation Autocorrelation](https://arxiv.org/html/2604.14414v1)

材料家族：SF-2026-ARXIV-2604-14414。

[官方HTML v1](https://arxiv.org/html/2604.14414v1) §4用stationary AR(1)做dependence筛查，再整conversation bootstrap；202 German conversations/5 users的局部显著结果变化不是所有评估虚假比例，也不能从无分布形式要求推出无需conversation独立性。Ch66已实际写cluster/time结构及bootstrap与采样结构匹配，非作者有限source→实际owner复核通过，标准已有覆盖；不把correlation变成因果。

### [Geometric Metrics for MoE](https://arxiv.org/html/2604.14500v1)

材料家族：SF-2026-ARXIV-2604-14500。

[官方HTML v1](https://arxiv.org/html/2604.14500v1) §III-C Lemma1称τ²JJᵀ+ppᵀ=diag(p)。对p=(1/2,1/2)、τ=1，J=.25[[1,-1],[-1,1]]，左侧为[[.375,.125],[.125,.375]]，直接不相等。Theorem2的无balance单调FSI结论亦缺loss方向条件。非作者apr01实际核必要Lemma/Theorem与此反例，中心几何/单调保证作为窄争议隔离，不宣称所有经验结果无效。

FSI直接测平均routing离均匀的距离，不由定义证明content specialization。§IV的Switch125M–2.7B、Wiki103/C4、4/8A10080G、100Ksteps、batch256×512、10seeds是作者实验，相关/AUC不修复Lemma。当前暂不据中心保证写Books，也未复现artifact。

### [CBCL](https://arxiv.org/html/2604.14512v1)

材料家族：SF-2026-ARXIV-2604-14512。作者已实际读取 exact-v1 必要方法、评价和关键反证，2+2+2=6，安全深入。非作者apr17_final_batch_review重开§III–VII必要段落并对读Ch83实际Admission/effect正文，确认动态dialect registry、安装去环/核心保留与每次展开fuel/size执法的具体缺口；语法接受不授业务effect权限。Rust/Lean是作者披露，本轮未复跑；不据端到端能力分类声明MCP输入必然不可验证。已实际写入dialect安装/逐次展开双门分支，root完整正文/两侧交接及有效必要证据复用写后PASS，真实Integrate。

§IV–VII用带版本的dialect namespace、无环模板DAG、depth/size/fuel限制区分message recognition与tool authorization；formal结果不证明语义一致或权限。现Ch83 admission/effect授权尚缺动态grammar registry的展开边界；Rust/Lean公开主张未复现，M4/gossip实验非全fleet安全。 更完整的实际位置和条件见[本日作者记录](../_sources/daily-20260417/v3-reopen-notes.md)。未复现实验，未披露条件不补造。

### [TRACER](https://arxiv.org/html/2604.14531v1)

材料家族：SF-2026-ARXIV-2604-14531。2+1+2=5，标准完成。非作者apr17_final_batch_review实际重开必要exact-v1正文、关键反证与当前owner，仅报告处置通过；不需要新增Books，未复现实验。

§3–5由teacher trace标签训练acceptor，按held-out阈值与独立shadow split决定fallback；5%为surrogate coverage floor，不是shadow抽样比例。Teacher agreement不是事实正确率，CLINC calibration .952→test .930；缓存Sonnet模拟和hindsight trace基线不等线上同预算。Ch56 risk cascade已对读，必要原文与实际owner已由非作者裁决Only，不为局部配方重复主干。 更完整的实际位置和条件见[本日作者记录](../_sources/daily-20260417/v3-reopen-notes.md)。未复现实验，未披露条件不补造。

### [CoCoDiff](https://arxiv.org/html/2604.14561v1)

材料家族：SF-2026-ARXIV-2604-14561。作者已实际读取 exact-v1 必要方法、评价和关键反证，2+2+2=6，缺口深入。非作者apr17_final_batch_review重开§III–IV必要方法/评价并对读Ch36 CP buffer，确认当前tensor的readiness重排与跨denoising step的stale QKV cache是不同合同。前者不删/替换本步值不等逐bit重放已证；后者用V proxy及共同mask，不能证明Q/K误差有界。TableII SD3.5 center PSNR23.65→21.95、SSIM.8390→.8075反驳忽略质量代价；只DiT推理，不迁成训练等价。实际Ch36正文已写入，root重开必要原文/实际段落及相邻衔接，写后独立通过。

§III–IV区分先发V的等价执行重排与V-major选择QKV的近似缓存复用。V变化代理不保证Q/K误差；Aurora Max1550/oneCCL、有限inpainting实验有质量下降，head并行饱和后可反转。Ch36 sequence-parallel现有head/buffer机制尚缺这两种不同合同；不写成无损通信省略。 更完整的实际位置和条件见[本日作者记录](../_sources/daily-20260417/v3-reopen-notes.md)。未复现实验，未披露条件不补造。

### [Don't Retrieve, Navigate](https://arxiv.org/html/2604.14572v1)

材料家族：SF-2026-ARXIV-2604-14572。2+1+2=5，标准审阅。非作者apr17_final_batch_review已重新核必要exact-v1及实际owner，已有覆盖：Ch76 corpus编译→导航→原文dereference及更新/ACL。无需新增同义正文。未复现实验；具体范围见[十项独立复核](../_sources/daily-20260417/V3_EXISTING_ONLY_BATCH_INDEPENDENT_AUDIT.md)。

§3–5离线聚类/skills forest供browse，claim必须回原始document，不从summary取得权威。WixQA 6221篇/200题是受限静态集；宽树成本增加而F1下降，单次vsagent轮数未匹配。Ch76已有compiled navigation→raw source与更新/ACL责任，拟不新增同义段。 更完整的实际位置和条件见[本日作者记录](../_sources/daily-20260417/v3-reopen-notes.md)。未复现实验，未披露条件不补造。

### [ConfLayers](https://arxiv.org/html/2604.14612v1)

材料家族：SF-2026-ARXIV-2604-14612。2+1+2=5，标准审阅。非作者apr17_final_batch_review已重新核必要exact-v1及实际owner，本次仅报告受限机制与关键反证，不将相似主题伪称完整已有覆盖。未复现实验；具体范围见[十项独立复核](../_sources/daily-20260417/V3_EXISTING_ONLY_BATCH_INDEPENDENT_AUDIT.md)。

§3–4用中间层entropy/confidence搜索layer set，但最终best set固定复用于其他prompts，不是逐请求自适应oracle。MI300X/FP16、100样本、outputcap512的窗口消融非全面胜出。Ch48 early-exit/target verify原理不需要因这一局部选择器更新；不采用其通用最佳layer说法。 更完整的实际位置和条件见[本日作者记录](../_sources/daily-20260417/v3-reopen-notes.md)。未复现实验，未披露条件不补造。

### [ELMoE3D](https://arxiv.org/html/2604.14626v1)

材料家族：SF-2026-ARXIV-2604-14626。作者已实际读取 exact-v1 必要方法、评价和关键反证，2+2+2=6，缺口深入；Ch49 bit-nested draft/verify存储与数据通路；必要source→owner已通过；实际Books正文已写入，root重开必要原文/实际段落及相邻衔接，写后独立通过。

§3–8把同一INT8量化权重拆MSB/LSB：resident MSB服务draft，完整verify组合两部分而非回float target。PSUM传输/cache驻留同datapath绑定，KV增长挤占expert容量。ASAP7/Ramulator只是周期模拟，MXFP4分支无同bit-axis；Ch49现多format artifact尚缺nested-one-copy条件分支。 更完整的实际位置和条件见[本日作者记录](../_sources/daily-20260417/v3-reopen-notes.md)。未复现实验，未披露条件不补造。

### [DR3-Eval](https://arxiv.org/html/2604.14683v1)

材料家族：SF-2026-ARXIV-2604-14683。2+1+2=5，标准审阅。非作者apr17_final_batch_review已重新核必要exact-v1及实际owner，已有覆盖：Ch66独立evidence planes与expected-fact inventory。无需新增同义正文。未复现实验；具体范围见[十项独立复核](../_sources/daily-20260417/V3_EXISTING_ONLY_BATCH_INDEPENDENT_AUDIT.md)。

§2–4分别计算利用用户事实、静态语料事实、citation requirement coverage和entailment；web augmentation可提高一项却降低另一项。100中英文逆向构造任务/64–512K noise和LLM judge不证明实际事实正确。Ch66 harness identity及claim/evidence责任实际承载该分账。 更完整的实际位置和条件见[本日作者记录](../_sources/daily-20260417/v3-reopen-notes.md)。未复现实验，未披露条件不补造。

### [Switching Efficiency](https://arxiv.org/html/2604.14690v1)

材料家族：SF-2026-ARXIV-2604-14690。作者已实际读取 exact-v1 必要方法、评价和关键反证，2+2+2=6，缺口深入；Ch36 useful/received/forwarded/capacity分账；必要source→owner已通过；实际Books正文已写入，root重开必要原文/实际段落及相邻衔接，写后独立通过。

§III–IV把effective bytes/(time×egress capacity)分解为三个不同因子；代数分解不是因果归因，collective的effective payload定义也不同。并发应joint profile，不能加权孤立测量。所测dense/MoE形状不等固定模型训练比较；Ch36 alpha-beta还缺这一计量选择边界。 更完整的实际位置和条件见[本日作者记录](../_sources/daily-20260417/v3-reopen-notes.md)。未复现实验，未披露条件不补造。

### [Equifinality](https://arxiv.org/html/2604.14419v1)

材料家族：SF-2026-ARXIV-2604-14419。2+1+2=5，标准审阅。非作者apr17_final_batch_review已重新核必要exact-v1及实际owner，本次仅报告受限机制与关键反证，不将相似主题伪称完整已有覆盖。未复现实验；具体范围见[十项独立复核](../_sources/daily-20260417/V3_EXISTING_ONLY_BATCH_INDEPENDENT_AUDIT.md)。

§3–5的76–84M Wiki103/RTX3090(Ti)/BF16、五种cosine路由×三seed/TOST只支持该范围。极窄scalar/decoupled routing也可达相近band，但冻结routing退步；isoParams/isoFLOP不是同一问题。不能外推expert pool总是主导上限，拟保留为受限比较反证。 更完整的实际位置和条件见[本日作者记录](../_sources/daily-20260417/v3-reopen-notes.md)。未复现实验，未披露条件不补造。

### [Geometric Routing](https://arxiv.org/html/2604.14434v1)

材料家族：SF-2026-ARXIV-2604-14434。2+1+2=5，标准审阅。非作者apr17_final_batch_review已重新核必要exact-v1及实际owner，已有覆盖：Ch21 routing标签≠功能必要性、干预后的独立行为验收。无需新增同义正文。未复现实验；具体范围见[十项独立复核](../_sources/daily-20260417/V3_EXISTING_ONLY_BATCH_INDEPENDENT_AUDIT.md)。

§3/7–8将underfit logit lens与converged intervention分开；44prompt的knockout/suppression/surgery只证明局部行为因果。Expert read/write projection不是全部知识或安全编辑接口。Ch21实际expert标签、output norm与删除/替换行为核验段已覆盖拟采用边界。 更完整的实际位置和条件见[本日作者记录](../_sources/daily-20260417/v3-reopen-notes.md)。未复现实验，未披露条件不补造。

### [Layered Mutability](https://arxiv.org/html/2604.14717v1)

材料家族：SF-2026-ARXIV-2604-14717。2+1+2=5，标准审阅。非作者apr17_final_batch_review已重新核必要exact-v1及实际owner，本次仅报告受限机制与关键反证，不将相似主题伪称完整已有覆盖。未复现实验；具体范围见[十项独立复核](../_sources/daily-20260417/V3_EXISTING_ONLY_BATCH_INDEPENDENT_AUDIT.md)。

§6/9–10比较五任务四种条件，恢复baseline prompt但留edited memory后仍有残余judge分数；缺完整no-edit memory因子、方差与fleet证据。Ch77 derived memory/version已有rollback原则，但本项不冒称完整因果测量；仅保留该局部反例，不新增taxonomy摘要。 更完整的实际位置和条件见[本日作者记录](../_sources/daily-20260417/v3-reopen-notes.md)。未复现实验，未披露条件不补造。

### [WAV](https://arxiv.org/html/2604.14732v1)

材料家族：SF-2026-ARXIV-2604-14732。2+1+2=5，标准审阅。非作者apr17_final_batch_review已重新核必要exact-v1及实际owner，本次仅报告受限机制与关键反证，不将相似主题伪称完整已有覆盖。未复现实验；具体范围见[十项独立复核](../_sources/daily-20260417/V3_EXISTING_ONLY_BATCH_INDEPENDENT_AUDIT.md)。

§4–5对video/value噪声分布做CEM elite mean/std更新后交action decoder，仍是latent iterative search，不是消除搜索。15trial/task和K/M/N消融不证明普遍最佳；§5.3首段K=1→5改善/10边际，performance-efficiency段K=0→3改善/随后收益饱和是两处口径，不合并成统一K>3无益；value SNR仅代理不是可靠uncertainty。Ch26已对读latent-goal/world rollout/controller，具体双噪声heuristic仅报告。 更完整的实际位置和条件见[本日作者记录](../_sources/daily-20260417/v3-reopen-notes.md)。未复现实验，未披露条件不补造。

### [SWE-TRACE](https://arxiv.org/html/2604.14820v1)

材料家族：SF-2026-ARXIV-2604-14820。2+1+2=5，标准完成。非作者apr17_final_batch_review实际重开必要exact-v1正文、关键反证与当前owner，仅报告处置通过；不需要新增Books，未复现实验。

§3–6生成oracle可读取synthetic repair metadata/scope；greedy removable-trace并非全局最短。PRM训练评分completed trajectory、推理复用partial prefix是另一估计；teacher特权/test weak不能当模型自知或真实step价值。4B/30B局部消融未匹配total compute，仅保留受限recipe。Table5已报30B parallel63.8/HG-TTS36.5 min/issue，属于受测环境wall-clock，不是生产SLO或总成本匹配。 更完整的实际位置和条件见[本日作者记录](../_sources/daily-20260417/v3-reopen-notes.md)。未复现实验，未披露条件不补造。

### [Nautilus](https://arxiv.org/html/2604.14825v1)

材料家族：SF-2026-ARXIV-2604-14825。作者已实际读取 exact-v1 必要方法、评价和关键反证，2+2+2=6，缺口深入；Ch49 scalar/VR/MA两级tile IR与repair成本；必要source→owner已通过；实际Books正文已写入，root重开必要原文/实际段落及相邻衔接，写后独立通过。

§4–8从scalar IR到VR tile-expression rewrite，再到显式movement的MA lowering；跨reduction rolling-update需repair factor，lookahead/split buffer/liverange不能当零成本。GH200/RTX5090、B1/8、1K–32K的operator mean不等serving SLO，部分backend仅1.00/1.01。Ch49已有typed fusion但缺该两层tile表示责任。 更完整的实际位置和条件见[本日作者记录](../_sources/daily-20260417/v3-reopen-notes.md)。未复现实验，未披露条件不补造。

### [Solve Then Learn](https://arxiv.org/html/2604.14853v1)

材料家族：SF-2026-ARXIV-2604-14853。2+1+2=5，标准完成。非作者apr17_final_batch_review实际重开必要exact-v1正文、关键反证与当前owner，仅报告处置通过；不需要新增Books，未复现实验。

§2–5离线utility矩阵经固定λ生成labels，再训练cheap classifier一次query；平均预算不是逐请求硬cap。Near-feasible ε允许放宽budget，随机强对偶不能自动证明同deterministic离散primal最优。MATH/GSM有限样本、48responses/题不等完整offline成本；Ch56实际cost/admission区别已读。 更完整的实际位置和条件见[本日作者记录](../_sources/daily-20260417/v3-reopen-notes.md)。未复现实验，未披露条件不补造。

### [RACER](https://arxiv.org/html/2604.14885v1)

材料家族：SF-2026-ARXIV-2604-14885。2+2+2=6，缺口深入。作者已实际读取精确v1必要证据并对读相应真实owner；采用命题为Ch48历史logit复用、bounded ancestry与验证责任。实际正文已写入并由root重开必要原文/真实段落及相邻交接独立写后PASS。

§3.1–3.3/§4.1–4.3/AppA/E.3从最近同token的target logit和相邻logit建立proposal，ancestor Touch/LRU/link refresh限制历史结构，再将合并树交target验证。历史不能赋予未来target分布权威；greedy/B1/FP16/RTX4090或A800有限7B–13B，部分比较2.41×低于EAGLE的2.51×，不证明sampling exactness或生产SLO。当前Ch48已有proposal/verify分工，但历史logit与bounded ancestry的窄状态分支已实际写入并通过root独立写后。 实际证据与章节定位复查见[作者记录](../_sources/daily-20260417/v3-reopen-notes.md)；未复现实验。

### [MemoSight](https://arxiv.org/html/2604.14889v1)

材料家族：SF-2026-ARXIV-2604-14889。2+2+2=6，缺口深入。作者已实际读取精确v1必要证据并对读相应真实owner；采用命题为Ch45联合训练的foresight隔离、memory readout与KV逐出边界。实际正文已写入并由root重开必要原文/真实段落及相邻交接独立写后PASS。

§3.1–3.3/§5.1–5.3及B/C使foresight branch承担预测、memory tokens承担历史读出，shifted position不意味着当前路径看到了未来token；memory readout完成与KV eviction有顺序依赖。H_i仍累积全部memory/boundary，减少增长斜率不等无限reasoning常数cache；Peak是context tokens而非进程VRAM。这是共同训练的缓存/压缩接口，不是既有checkpoint无损drop-in。Qwen2.5-7B/Llama3.1-8B、8H200、5epoch，8192vs4096/LR不同；greedy output cap10240、repetition penalty1.1，16×压缩质量下降且MTP有局部更优。当前Ch45一般压缩/同步不能代替此具体交接，拟窄缺口。 实际证据与章节定位复查见[作者记录](../_sources/daily-20260417/v3-reopen-notes.md)；未复现实验。

### [LongAct](https://arxiv.org/html/2604.14922v1)

材料家族：SF-2026-ARXIV-2604-14922。2+1+2=5，标准。作者已实际读取精确v1必要证据并对读相应真实owner；拟采用命题为Ch30实际mask、optimizer state与mask churn覆盖。非作者实际source→owner复核通过，采用当前Ch30具体正文，不要求新写Books。

§3.3 Eq8–10/§4.5–4.7/§5按head激活选择Q/K行，不是LoRA，也不保证整个backward同比例缩小。现Ch30 mask/momentum/churn/drift的实际段落承载采用边界；8H800/Qwen4B或8B的30%并非全面最佳，已有覆盖而不增加算法摘要。Figure6展示case之外，Table8指定clamp-to-global-mean干预统计503例，但不证明跨分布稳定因果saliency。 实际证据与章节定位复查见[作者记录](../_sources/daily-20260417/v3-reopen-notes.md)；未复现实验。

### [Serving Chain-structured Jobs](https://arxiv.org/html/2604.14993v1)

材料家族：SF-2026-ARXIV-2604-14993。2+2+2=6，缺口深入。作者已实际读取精确v1必要证据并对读相应真实owner；采用命题为Ch56共享weight block与独占KV的chain capacity。已实际写入正文，root顺读真实段落及相邻交接、复用有效必要v1采用记录后写后PASS。

§2.1–2.2/§3.1–3.2/§4.2把离线连续block placement与cache allocation共同编译为虚拟job servers，线上JFFC只在已有可行chain capacity中派发。权重共享不使每请求KV也共享；固定cache、无迁移/抢占与steady-state surrogate限制不能省略。PETALS/3A10080GB拆9MIG、RIPE/Azure有限trace，input2048/output28，Table1实际有P95/P99响应/等待结果，但precision及通用tail SLO合同未披露，不把缺合同误写成未测尾部。现Ch56容量承诺尚缺这一chain组合分支，拟窄整合。 实际证据与章节定位复查见[作者记录](../_sources/daily-20260417/v3-reopen-notes.md)；未复现实验。

### [Mixture-of-Experts Flow Matching](https://arxiv.org/html/2604.15009v1)

材料家族：SF-2026-ARXIV-2604-15009。2+2+2=6，缺口深入。作者已实际读取精确v1必要证据并对读相应真实owner；拟采用命题为Ch24多模态velocity平均与mixture likelihood分工。非作者必要源及真实owner缺口核验通过；实际Ch24正文/邻接经root写后PASS，已真实整合。

§3.1–3.2 Eq4–6/§4.1–4.2/§5.1–5.3用soft Gaussian-mixture NLL而非单MSE处理velocity的多模态；每token在t0选expert并固定路径，当前dense实现不能宣传稀疏conditional compute。K=1/大σ退化、200M/210M受限任务FT、oracle output length、single H200 greedy batch1与跨124/139M/8B比较界限保留；部分质量退步，速度不能外推一般替代AR。唯一拟owner为Ch24生成factorization，不因MoE名改Ch21。 实际证据与章节定位复查见[作者记录](../_sources/daily-20260417/v3-reopen-notes.md)；未复现实验。

### [Route to Rome Attack](https://arxiv.org/html/2604.15022v1)

材料家族：SF-2026-ARXIV-2604-15022。2+2+2=6，安全深入。作者已实际读取精确v1必要证据并对读相应真实owner；采用命题为model-selection信号与资源授权分离。root实际反向对读Ch72 L1985–1991：生成语义不能拥有外部resource budget、stop/risk与termination权限，既有原则已承载；路由攻击精确recipe仅报告，不冒称全算法Existing。有效必要源审不变，最终Only，不新增同义主干。

§3/§4.1–4.3用120黑盒查询训练surrogate，再优化suffix强制昂贵路径。6个路由器、3次run的ASR是strong-model routing而非policy breach或truth；GPT-5 web隐藏route未测ASR，Thinking-like judge/fingerprint不证明收费。现Ch72 token exhaustion/expert attack不能代替confidence cascade的具体资源授权分支，后者此前仅Review note，拟补正文而不宣称所有router必然失效。 实际证据与章节定位复查见[作者记录](../_sources/daily-20260417/v3-reopen-notes.md)；未复现实验。

### [Prefill-as-a-Service](https://arxiv.org/html/2604.15039v1)

材料家族：SF-2026-ARXIV-2604-15039。2+2+2=6，缺口深入。作者已实际读取精确v1必要证据并对读相应真实owner；采用命题为Ch55 hybrid-state分组恢复与prefix/tail交接。实际正文已写入并由root重开必要原文/真实段落及相邻交接独立写后PASS。

§3.2–3.4/§4.1–4.3linear/SWA state需要精确cached length，full-attention允许partial prefix；reusable prefix-cache blocks必须完整，transfer-tail保留到transfer完成才回收，不能在发送前丢弃；prefix后incremental length及带宽决定remote prefill/local PD，长期另调pool。内部1T KDA:MLA=3:1、8GPU/instance、32H200远端与64H20本地、100/800Gbps；吞吐图是实测profile输入的稳态模型，非端到端bursty goodput。input128–128K/output1024/SLO40token/s、不含SD、precision ND，不声称等成本普胜。Ch55现主干需这条窄条件分支。 实际证据与章节定位复查见[作者记录](../_sources/daily-20260417/v3-reopen-notes.md)；未复现实验。

### [Atropos](https://arxiv.org/html/2604.15075v1)

材料家族：SF-2026-ARXIV-2604-15075。2+1+2=5，标准。作者已实际读取精确v1必要证据并对读相应真实owner；拟采用命题为仅报告GCN预测驱动的受限换模配方。非作者实际source→owner复核通过，局部GCN换模配方仅报告，不要求新写Books。

§3.1–3.3/§4.2–4.4/§5.1–5.3用SFG/GCN预测风险；parallel换模携带前k−1步context，sequential只换尚未生成的完整trajectory、没有context migration。Ch56 Model Switch Point已分清prefix、KV与compatible context，此新GCN配方尚不改变稳定线上策略。三代码Agent/5fold且test仅半holdout，本地RTX3090与API混合；成本按tokens×价不含GCN/call latency，部分full-trajectory指标更差。拟仅报告，不采用普适无损hotswap。 实际证据与章节定位复查见[作者记录](../_sources/daily-20260417/v3-reopen-notes.md)；未复现实验。

### [IUQ](https://arxiv.org/html/2604.15109v1)

材料家族：SF-2026-ARXIV-2604-15109。2+1+2=5，标准。作者已实际读取精确v1必要证据并对读相应真实owner；拟采用命题为Ch66同源问答冲突不等truth与校准已有覆盖。非作者实际source→owner复核通过，采用当前Ch66 atomic claim/同源偏差具体正文，不要求新写Books。

§3.1–3.5 Eq1–9/§5.2–5.4/Table2–4每claim生成≤3问题、fresh session回答，用矛盾率和衰减核聚合。新session只干预context，同源responder/interrogator/judge不消除共同偏差；Ch66 claim依赖、证据权威与readout/calibration实际承载边界。FAct235/LongFact250、Table3累计61161短答额外预算；AUROC非calibration，GPT4o/FActScore不全面改善，排除refusal改变coverage，硬件/precision/concurrency/SLO ND。拟已有覆盖。 实际证据与章节定位复查见[作者记录](../_sources/daily-20260417/v3-reopen-notes.md)；未复现实验。

### [LLMs Gaming Verifiers](https://arxiv.org/html/2604.15149v1)

材料家族：SF-2026-ARXIV-2604-15149。2+2+2=6，安全深入。作者已实际读取精确v1必要证据并对读相应真实owner；拟采用命题为Ch31固定hypothesis的isomorphic双验收。非作者必要源及真实owner缺口核验通过；实际Ch31正文及相邻段经root写后PASS，已真实整合。

§3/Table1/AppC对同一已生成H以原对象常量与双射改名实例验收，分开extensional标签枚举与intensional规则泛化；不是重问一次。当前Ch31 checked-span行为已有原则，但缺固定H在等构实例的具体验证分支。OLMO3-7B-Think-DPO两次约500step/64H100/48h只reward不同，支持受测任务窄因果；无seed重复，前沿训练标签有presumed；Table1两个OLMo-3 32B/7B RLVR rows与GPT-5-mini-low均零observed shortcuts，不能推广所有RLVR必然捷径，也不从零观察证明零漏洞。拟实际新增。 实际证据与章节定位复查见[作者记录](../_sources/daily-20260417/v3-reopen-notes.md)；未复现实验。

### [When Flat Minima Fail](https://arxiv.org/html/2604.15167v1)

材料家族：SF-2026-ARXIV-2604-15167。2+2+2=6，反证深入。作者已实际读取精确v1必要证据并对读相应真实owner；采用命题为Ch49 checkpoint轨迹与量化probe的独立发布验收。必要source→owner已通过；实际Books正文已写入，root重开必要原文/实际段落及相邻衔接，写后独立通过。

§3/§4.1–4.5/§5.1–5.2/§6及必要AppA/B说明FP32 PPL plateau不授予低bit artifact发布。Pythia160M154checkpoint、固定32batch×4×512Pile；group128非对称INT4 vs per-channel对称INT8不是只bitwidth变化。fork序列2048/batch4、三recipe×3seed；OLI改善伴FP32 PPL76vs44代价，不能推广配方。weight kurtosis关联不唯一识别原因，weight-only探针不否定activation/QAT/GPTQ。拟Ch49联合checkpoint×probe窄Gate。 实际证据与章节定位复查见[作者记录](../_sources/daily-20260417/v3-reopen-notes.md)；未复现实验。 本项必要source→当前真实owner的窄差异已由非作者独立核通过；已实际写入相应owner正文，root完整正文/邻接及有效必要证据复用写后PASS。

### [MixAtlas](https://arxiv.org/html/2604.14198v1)

材料家族：SF-2026-ARXIV-2604-14198。2+2+2=6，缺口深入提案。§4.1–4.3/§5/§6–7/Table1–2实际分别优化五种supervision task与十个CLIP concept clusters、另轴均匀，并非联合50cell优化。Qwen0.5B proxy/GP-UCB到7B、固定约4M样本/epoch、64H100，迁移仍有MMBench72.80→61.68及GQA44.27→36.48反例。root反向实际对读Ch27 L170–180两轴及L850–854 simplex interaction/pilot迁移：采用的一般配比原则已承载；分别优化且另一轴均匀是受限recipe，不能称已测joint或由名称创造长期gap。稿内August日期不是首次公开。apr01实际重开官方PDF-v1必要pp4–8并对读现Ch27，窄提案独立通过；HTML首页August后改不作日期证据，PDF首页Apr17也不单独证明公告时刻。最终Only经root当前owner反向语义裁决通过，不把精确recipe全称Existing；precision/线上SLO ND，未复现实验。

### [Three-Phase Transformer](https://arxiv.org/html/2604.14430v1)

材料家族：SF-2026-ARXIV-2604-14430。2+1+2=5。§3.1–3.7/§4.8–4.10/§4.14–4.15的channel partition、rotation、per-phase RMSNorm和r(t)=1/(t+1)均是受限配方，不证明任意内容正交或训练守恒。123M WikiText/5.5M TinyStories、3seed排序变化，不显著不等相等。§4.9/5的‘1e−20低于FP32最小可表示梯度’错误：normal约1.18e−38/subnormal约1.40e−45；实际update舍入还依赖参数/累加，隔离该保证而不否定PPL。Ch17 Norm/架构/optimizer分权承载通用边界，但不称此配方完全Existing；仅报告受限配方并窄深入隔离数值纠错。非作者apr01已实际核必要原文及该反证，处置通过；未复现实验。硬件/precision完整训练合同/生产SLO ND。

### [Adaptive Visual Reasoning](https://arxiv.org/html/2604.14568v1)

材料家族：SF-2026-ARXIV-2604-14568。2+1+2=5。§4.1–4.3 Eq2–7/§5/Table1/§6.2–6.3组合perception→reasoning→answer、perception-only和direct格式；correctness×format bonus、衰减diversity及长度项形成成本prior，不是audio或自知calibration。Qwen3VL2/4/8B、11k SFT/44k RL、七benchmark/GPT4omini judge，2B MathVision30.1→29.8、MMMUPro27.5→26.9，长度阈值改变排序。Ch33 actual成本prior/格式collapse与Ch23感知分权已有主要边界，但不伪称新配方全部既有；标准仅报告。hardware/precision/SLO ND，非作者必要原文/当前实际owner及关键反证核通过，仅报告终态，不新增同义主干。

### [Masked Logit Nudging](https://arxiv.org/html/2604.14591v1)

材料家族：SF-2026-ARXIV-2604-14591。2+2+2=6，缺口深入提案。§3.2–3.4 Eq6/§4/Table1–3/§6.1.1保留source coarse scales，把概率残差α(onehot source−softmax target)加到target logits；attention差mask与非编辑区codebook refinement另负责任，不是logit等值混合、CFG精确式或无损source保证。SWITTI/PIE512及COCO/OpenImages重建、512/1024两分辨率，SSIM86.80<TurboEdit91.59。inversion/forward .41s不代表mask/refinement零成本；single-image两次mask regeneration20ms仅sM=9，跨backbone不能归因范式加速。硬件/precision/batch/concurrency/SLO ND。implementation对style-edit关闭refinement以避免颜色/纹理偏离，背景repair不普适免费。apr01重开Eq6/9、§3.3–3.4/Table1及Ch24实际相邻正文，窄提案独立通过；root本轮重开必要官方原文/真实owner采用通过，实际Ch24及邻接写后核验通过，mask外是更强nudging而非硬恢复；已真实整合。

### [CW-GRPO](https://arxiv.org/html/2604.14267v1)

材料家族：SF-2026-ARXIV-2604-14267。2+1+2=5，标准已有覆盖，经非作者必要源→实际正文复核通过。§3.3–3.5/§4/§5/Table2–4以retrieval utility×reasoning validity为judge信号：成功round重加权、失败uniform、final answer保持。平均advantage守恒不等gradient不变或真实causal credit，97round/95%人工共识不能证明oracle。Qwen3-1.7B/8B、verl/SGLang、2018Wiki/E5/top3、200step/128 sampled trajectories、9192token/10round、Avg@4；1.7B Hotpot27→24，alpha1平均29.69<29.88。Ch33真实verifier方向/teacher幅度、phase/segment credit承载采用边界，非作者必要源/实际owner核通过。hardware/precision/总judge预算匹配ND，未复现。

### [RUMS](https://arxiv.org/html/2604.14473v1)

材料家族：SF-2026-ARXIV-2604-14473。2+1+2=5；工程标准，受影响理论深入反证。§3/§4.1/Table1/AppendixC以预测entropy下降选memory，offline生成labels再训selector；N5按序列长度归一化估per-token entropy，非完整joint entropy。Llama3.1-8B/GPT4、50属性筛≤10、tau.29、生成profiles与heldout WildChat；real-world recall .36与Binary .60，非普遍最优。

AppendixC从Y⊥M|Z推Z⊥M|Y不成立：M=Z、均匀二元Z、Y独立20%翻转时满足前一条件，H(Z|Y,M)=0而H(Z|Y)>0。因此证明中的subset无关常数未由Assumption2推出；这只反驳该步骤，不证明所有经验排序失效。非作者apr01实际核Assumption2/Theorem3.1与AppendixC此桥，深入反证通过；仅报告受限surrogate、隔离未经成立的subset-independent residual entropy推导，不据其正面保证写Books，不重复完整附件。

### [HyPeR](https://arxiv.org/html/2604.14806v1)

材料家族：SF-2026-ARXIV-2604-14806。2+1+2=5，标准仅报告，经非作者必要源/真实owner对读通过。§4.3–4.6/§5/Table1–4在声学explicit trace后以lowest-group probability决定PAUSE/abort，最多3×64latent tokens；ASR字符串相似、背景cue gate和答案一致性是sensors，不是声学真值或排除幻觉。Qwen2Audio7B、30k RL augmented、effective batch16/group8/temp1、PAUSE.5/abort.05；HyPeR Music62.27低于外部Qwen2.5-Omni-7B的65.90；自身训练base Qwen2-Audio对应53.59、SFT44.61、更多reflection退步，hidden displacement/cosine不排除额外compute解释。Ch23 latent/scaffold预算及Ch33成本prior承载主要边界，新audio gating配方只保留受限证据，不称全部Existing。hardware/precision/SLO ND，表文WER/CER不同不照录，非作者有限复核通过。

### [TrigReason](https://arxiv.org/html/2604.14847v1)

材料家族：SF-2026-ARXIV-2604-14847。2+2+2=6，缺口深入提案。§3.2/§4/Table1/Limitations以LRM priming、SRM低perplexity比例/连续hesitation触发重生成或短接管，heuristic不拥有逐步真值。Ch56 actual VOI expensive-estimator段缺‘每步强模型打分→事件触发交接’具体控制分支。8×RTX4090/SGLang0.4.9/TP4/prefix cache/temp.6/top_p.95/8192token，16题内采样平均；SMT占比非wallclock，ARC .948<LRM .957、32K相对LRM gap，edge-cloud掉2.49pp。

局部配置必须隔离：Eq3 PPL=1/p≥1，但§4.1 tau=.85与§4.5 PPL<1.05冲突，不作为可执行threshold采用；这不否定所有受测结果或整个事件机制。已实际写入controller责任/分账与旧逐步验证共存，root顺读正文及邻接并复用必要v1记录后写后PASS，precision/concurrency/SLO ND。

### [TESSY](https://arxiv.org/html/2604.14164v1)

§2.1–2.2/§3–4由learned boundary predictor区分teacher标注的style/capability spans，在同一committed prefix生成并rollback跨界后换producer；最终答案由student生成。不是先写完整teacher答案再模仿，annotation也不证明因果能力可客观分段。Qwen8B/30B-A3B、GPT-OSS120B、32H200、80k题/37k独立题、40k输出上限；换synthesis student可退步，GPQA60.16→59.34，不采用全任务保持。Ch29现distillation165–219承载容量/数据/表示错配，却缺样本构造阶段局部producer与回滚界面的分支，拟缺口深入；精度/总teacher调用预算/线上SLO未披露，非作者必要source→真实owner已通过，现已实际写入Ch29且root顺读真实正文/邻接、复用有效必要证据后写后PASS。

### [Attention to Mamba](https://arxiv.org/html/2604.14191v1)

§3.1–3.2/§4/Table1–2先将softmax学成normalized linear feature算子，再把它映射到identity-initialized SSM的B/C/transition及归一化state，随后解锁conv/gate等其余参数、但input-output embeddings仍冻结，用真实token CE训练。只匹配中间算子，不是原softmax精确转换，也无原attention block保留。Pythia1B/10B OpenWebText、8A100/BF16；expanded state2048造成作者12d9h且大于8倍训练时长，token预算不等wallclock。Lambada32.31<42.07/BoolQ55.20<60.82限定能力保持。Ch22当前hybrid/state migration约275–327缺函数匹配中间表示→checkpoint替换→解锁动力学的路径；拟缺口深入，非作者必要source→真实owner已通过，实际Ch22正文/邻接经root写后PASS，已真实整合，不给部署长检索保证。

### [FRESCO](https://arxiv.org/html/2604.14227v1)

§3–4用query fact-time、Wikidata有效区间与Wikipedia revision构造语义强但过期的hard negatives；19个reranker的Obsolete Ratio只针对排在正例前的负例，不是全query错误率。§5/Table2的Pareto指令解中EK79.20/NEK59.41 vs baseline62.41/60.93，不支持新鲜度无代价支配语义。当前Ch76“Temporal Retrieval 要在 Admission 前验证事实有效期”实际983–985已承载query date/source validity/revision联合admission和未知日期回退；拟标准已有覆盖，受限反证留日报，不另加benchmark摘要。人工200样本98.5%一致不证明全数据truth；hardware/precision/线上SLO未披露，非作者重开必要方法及Ch76实际Temporal Admission段后，已有覆盖通过；无需新增Books。

### [Calibrate-Then-Delegate](https://arxiv.org/html/2604.14251v1)

§2/§4/§5实际以offline ridge预测expert/probe对标签的概率差DV，三份互斥数据训练safety probe、DV和校准，校准又拆estimation/testing。Pareto候选上固定顺序binomial测试，在IID/有限独立候选条件下校准总体delegation-rate；不是每batch/每请求hard cap、美元总额或准确率同界保证。四数据集、Llama3.2-1B layer11和Gemma27B/1B、1586测试样本一半校准、baseline B128/confidence.9；平均更弱expert仍有正DV子集，漂移须重校准。Ch56当前VOI已有inspection benefit vs cost，但缺benefit-estimator与calibrated-rate预算分离的具体分支。6分安全/缺口深入；apr01必要原文/真实owner采用核已通过，现已实际写入Ch56，root顺读真实正文及邻接、复用必要v1记录后写后PASS。hardware/precision/end-to-end成本/SLO未披露。

### [Generalized Fine-Tuning](https://arxiv.org/html/2604.14258v1)

§2–4混合expert/teacher/on-policy组与normalized advantage，局部经验可记录；10k×8与SFT100k轨迹不是同独立问题或总compute。中心保证精确隔离：AppendixB Eq21的−A*stopgrad(C)*logp，在固定A/C时导数为−A*C*gradlogp，Eq22却为+A*C/p*gradlogp，反号且多1/p。普通二元CE对目标logit梯度p−1有界，不能由期望换测度证明SFT固有梯度爆炸；这不保证网络所有参数梯度有界。apr01实际独立核Eq16–17/21–22及反例通过。仅暂停受影响公式/严格统一保证，保留五小模型/math、T.5/max4096、16次平均pass@1的经验（不是pass@16）；MAWPS95.79<96.06/SVAMP84.65<86.36，非全面改善，hardware/precision未披露。不据待澄清loss理论写Books。

### [GUI-Perturbed](https://arxiv.org/html/2604.14262v1)

§3–6/§8以同target单步screenshot的四视觉变体×direct/relational instruction配对，程序重新渲染bbox后人工过滤，390基任务/web Mind2Web。三款Qwen2.5VL7B lineage的训练阶段/数据/prompt同时变化，不能全部归因RL vs CE；rank8/6.5k、25k增广退步不证明所有PEFT无效，§7.4的CE无spatial gradient也不能字面采用。Ch66实际EvalSpec交叉任务轴、oracle/budget与混杂边界已承载本次拟采用命题，5分标准拟已有覆盖，非作者必要源/当前Ch66 EvalSpec核通过，已有覆盖通过、不新增Books；不追加新benchmark摘要或functional affordance未测保证，线上concurrency/SLO未披露。

### [GeoDe](https://arxiv.org/html/2604.14324v1)

§3.1–3.3 Eq2/Alg1将probe到超平面距离定义为abs(w·x+b)/norm(w)，故d≥0，却以d<0区分未知类；apr01实际独立核Eq2/Alg1第9/13行确认中心分区无法由所列公式实现。需signed-score或实际labeling实现澄清，不自行修原算法后采用。10k TriviaQA正确标签、far-boundary子集SFT回答/拒答，TBG/SLT sensor位置不同，不证明内在truth空间；4L40/48GB、greedy/3seed、Llama8B/Qwen8B/四QA，QwenSciQ TBG81.8<Probe86.5、SLT84.6<85.7。5分局部正确性深入争议，隔离算法/自知保证而不否定所有经验，不以Ch66已有probe边界绕过具体冲突。

### [Faithfulness Serum](https://arxiv.org/html/2604.14325v1)

§3–5.1/AppF先筛hint改变答案的样本，再由答案首token PE-LRP引导解释生成的question-token post-softmax attention。Llama3.1-8B/Qwen2.5-7B、每hint1000成功样本/H10080GB、LLM-judge与关键词CT双读数；不能推广为所有输入faithfulness或完整原决策因果。SciQ protocol-specific CT65.2→57.9退步，distinct-1调α可多生成≤15次。Ch66 accepted-selector分母与interpretability diagnostic承载边界，但新干预不称全部Existing；5分标准仅报告，非作者apr01必要来源/实际owner复核通过，未复现实验；precision/concurrency/SLO ND。

### [RoPE-Perturbed Self-Distillation](https://arxiv.org/html/2604.14339v1)

§2.2–2.4 Eq4–9保留token/mask，仅suffix跳跃RoPE index；标准view stop-gradient作为teacher，扰动view reverseKL只作用suffix，标准CLM仍更新。Ch22位置外推/有效利用的主干尚缺显式跨index一致性适配分支，6分缺口深入非作者必要source→真实owner已通过，实际Ch22正文/邻接经root写后PASS，已真实整合。§3/AppA的Llama8B64K/16A100/4Mtokens每步、Qwen4B256K/32A100/8Mtokens每步/1000steps；另forward约1.6×步时间，CLM多1.6×步wallclock对照不是同tokens。NoPE29.5<47.9、chunk permutation46.2<47.9，不能任意抹除位置语义；teacher错误/位置敏感任务/短窗回归需检查。precision/线上SLO ND。

### [Tight Sample Complexity Bounds for Best-Arm Identification Under Bounded Systematic Bias](https://arxiv.org/html/2604.14345v1)

当前官方v1标题不同于库存PAC-MCTS标题；绑定当前v1，不沿用库存标题作证据。Assumption1/Eq1–4/Alg1把已知supremum bias L加进local-frontier置信半径，noise与bias分账确有主线意义。Dynamic Bias段仅以frontier empirical variance估L，恒偏c的观测可variance0而bias c，不能据此保持rigorous安全；同文Δ4/L1.5称Δ>4L成立也不成立。5分仅报告静态条件化剪枝/受限经验并窄深入隔离动态保证，不否定所有静态L理论或全部实验；Ch79已有search/verifier盲点，不据此写生产PAC/全树failure保证。非作者apr01实际核必要假设、动态段与数值反例，通过此窄处置，未复现实验；不采用不完整配置下的宣传API加速。

### [Cost of Language](https://arxiv.org/html/2604.14363v1)

§3–4/Table1及E.3/Table12以L12/COCO-fit/K256 centroid分别替换视觉与文本残差；七MLLM/six BLINK任务greedy，文本替换同时改task/answer接口，均值4×差不能纯归因模态竞争。text-side hidden contrast是局部proposal；逐task oracle挑α与固定.4分开，后者Depth−2.4/Spatial−2.1，不称所有任务改善。Ch23 modality conflict sensor与选择干预已有分权，centroid新recipe5分标准仅报告，不从visual-cost低批准删token或自知controller。非作者apr01实际必要方法/反例核验通过，未复现实验；hardware/precision/SLO ND。

### [Step-level Denoising-time Diffusion Alignment with Multiple Objectives](https://arxiv.org/html/2604.14379v1)

§4.1 Eq3/§4.2 Theorem1 Eq6–7将共享reference上的step-advantage surrogate与逆条件分布融合分开；Gaussian base同KL温度且各自达到该surrogate最优、权重在simplex时，乘积分布的均值/方差由precision加权得到，不是参数平均或终态RL全局最优。Ch24现有source/guidance还没有这条目标—sampler接口，6分缺口深入非作者必要source→真实owner已通过，实际Ch24正文/邻接经root写后PASS，已真实整合。SD1.5、color prompts/GPT4新组合、32seeds/ImageReward/VILA；实际base训练为DPOK，不证明满足理论最优。E.2单H100训练/batch2/accum12/LoRA4，推理precision/step/并发SLO不完整，不引用秒数；两模型每步都执行，无新训练不等零推理成本，某一reward仍可低于CoDe。

### [Zero-Ablation Overstates Register Content Dependence in DINO Vision Transformers](https://arxiv.org/html/2604.14433v1)

§3/§4/Table4及补充mean/noise/shuffle controls比较全层register置零、dataset-mean、匹配Gaussian和跨图真实activation。置零质量下降同时包含内容缺失与off-distribution cascade；替换控制保留大部分质量，不能将单一zero baseline解释为内容不可替代，也不因此批准删register。DINOv2/v2+reg/v3、ViT-S/B/224²、四任务/5000-image统计校准/paired tests，不把DINOv3 recipe差异全归Gram loss。Ch66 Interpretability Graph的raw/paired patching要求尚缺baseline身份的具体反证，Ch23替换≠删除则是不同命题；6分缺口深入，拟最窄补干预baseline/内容与结构分账，非作者必要source→实际Ch66核通过，已实际写入相应owner正文，root完整正文/邻接及有效必要证据复用写后PASS。§12明确单RTX4090 24GB、全实验约12–15 GPU小时；precision/线上concurrency/Serving SLO ND。

### [Hierarchical vs. Flat Iteration in Shared-Weight Transformers](https://arxiv.org/html/2604.14442v1)

§3.1/§5.8–5.10的input/Fast/Slow共享block与K-window TBPTT，在相近存储参数下比较flat/hierarchical重复计算；不证明任意函数类别或排除全部optimization原因。统一超参的MultiSeed中T-L4反而更优，分别调参后排序改变。共享权重仍有O(Mnd) KV，而不是O(nd)；Ch22实际206–208已分重复full-attention的历史副本与local/global解耦。5分标准拟仅报告新受控结构/调参反证，不将新recipe全部称Existing，也不追加架构宣传。OpenWebText1024、约1.2B、有限10k/seed/grid范围，不推所有任务或成熟kernel下的wall-clock排名，非作者必要源与Ch22实际相邻段核通过，仅报告受限recipe。

### [Controlling Authority Retrieval: A Missing Retrieval Objective for Authority-Governed Knowledge](https://arxiv.org/html/2604.14488v1)

§2/§4/§6/§9把semantic anchor后的scope补检、superseder closure与active frontier分开。Ch76 Temporal Admission实际983–985只验证候选日期/有效期/revision，没有低semantic superseder的额外发现责任；6分缺口深入拟最窄补anchor→authority closure→reader，错scope或partial graph回Unknown，不将晚时间戳直接当override。static corpus/known deterministic edges/perfect scope的理论不能升级成自由文本普适正确；Theorem4还将Definition7的semantic answer正确写成完整frontier必要条件，但deterministic f不意味着每个active文档不可缺：若两文档给同一个答案，取一个可答对且无superseded项，却不包含全部frontier。只隔离这一必要性保证，保留机制与有限经验。FinSuperQA结构化ID/1000queries/12250events/k5；free-form GHSA需BM25找anchor，找不到即回退。precision/线上SLO ND，非作者必要source→实际owner核通过，已实际写入相应owner正文，root完整正文/邻接及有效必要证据复用写后PASS。

### [CURaTE: Continual Unlearning in Real Time with Ensured Preservation of LLM Knowledge](https://arxiv.org/html/2604.14644v1)

SF-2026-ARXIV-2604-14644，5分安全深入拟已有覆盖。exact-v1 §1/§3.2–3.3/§4.1与AppendixG区分作者明确声明的behavioral suppression和参数删除：训练sentence embedder后，forget DB追加请求，cosine阈值选择拒答或原LLM；权重不变不意味着访问utility不受false positive影响，也不证明dataset-influence已删除。persona/payload拆分与编码恢复说明拒答接口仍可被绕过，不能从一次paraphrase测试签发擦除证书。当前Ch72实际“Unlearnability 与 Unlearning”及分层验收段（约2111）已经明确prevention/parameter influence/behavioral withholding/relearning分账，末端inference suppression也要求高风险回退；不是仅按unlearning主题判Existing。不采用“唯一实时”或未经完整配置绑定的秒数，不把安全测试中的学科内容转成AI-for-Science来源。非作者必要来源/实际Ch72删除验收正文核通过，已有覆盖不新增Books。

### [Bounded Autonomy for Enterprise AI: Typed Action Contracts and Consumer-Side Execution](https://arxiv.org/pdf/2604.14723v1)

SF-2026-ARXIV-2604-14723，5分安全深入拟已有覆盖。官方PDF v1 §4–5/§7.3/§7.12/Tables3–5：consumer保有业务和side-effect权，manifest按权限暴露，结构化validation/clarification及confirmation在effect前运行。受限CRM/GPT-4o-mini/25trials中，对照仍保留consumer backend；语法、权限和workspace均有效却可能wrong-entity mutation，ambiguity仅3/4，不证明所有框架零失效或每层独立因果。所谓手工速度基准不是同组实测，故不采用13–18×。Ch78实际Text2Opt binding段（约686–688）已分结构proposal与确定性实体/单位/索引绑定，不唯一则拒绝并请求信息；权限/identity/effect段承载执行边界，足以支持这条窄采用命题。模型之外hardware、precision、并发、生产SLO Not Disclosed；非作者实际必要原文与Ch78具体机制正文对读通过，已有覆盖终态；不新写企业案例摘要。

### [Schema Key Wording as an Instruction Channel in Structured Generation under Constrained Decoding](https://arxiv.org/html/2604.14862v1)

SF-2026-ARXIV-2604-14862，6分缺口深入提案。exact-v1 §3.1–3.6/§4.1–4.3将相同字段数/次序/可解析结构下的None/Key/Prompt/Both分开：key tokens进入AR prefix，grammar合法不等语义neutral。Ch20实际Format Tax段分prompt竞争和decoder mask，尚未解释grammar放行的key自身也是语义指令渠道。拟最窄补prompt×schema wording×grammar/parser的联合身份与内容回归，不把rename当语义不变或把parse合规当正确；下游字段映射须同步。这不是已研究恶意注入，也不采用projection启发式为通用定理。七个Qwen/Llama变体、GSM8K/Math500、固定XGrammar配置；Key-only有模型退步，Both不总加成。原文未给完整hardware/precision/长度/并发/SLO，不外推API质量或普适最佳命名。apr01已实际重开必要方法/表及Ch20相邻正文，窄gap通过；Prompt-only说明有位置歧义，拟正文只按真实四配置区别，不冒称token-length匹配。已实际写入并通过root真实正文/邻接与必要证据复用的写后独立核验。

### [Segment-Level Coherence for Robust Harmful Intent Probing in LLMs](https://arxiv.org/html/2604.14865v1)

SF-2026-ARXIV-2604-14865，6分安全缺口深入提案。exact-v1 §3 Eq1–7/§4.1–4.4/Table1/§5：冻结模型的多层activation线性probe，M16窗口，训练用整条exchange中Top-K窗口平均监督，并只对benign施加soft-weighted SegVar；推理用因果prefix和EMA。重叠窗口不是独立证据，训练选Top-K不赋予运行时未来访问权；将SegVar也施于positive会退步。root反向实际对读Ch72 L603–626 channel/parser/aggregation与L652–656 prefix持续probe/authority分责：一般采用原则已承载，弱exchange标签、Top-K/SegVar与在线EMA的局部配方仅报告，不把sensor升级授权或精确recipe全称Existing。Llama3.1-8B/Qwen3-8B/Gemma2-9B、单H200、有限安全/benign集合；普通high-stakes可落后classifier，专业长对话仍误报，未测probe-aware adaptive threat或prompt-injection防御。precision/生产SLO ND，参数量不等端到端延迟。apr01有效必要源审继续复用；root反向当前owner语义裁决Only通过，不新增同义主干。

### [On the Expressive Power and Limitations of Multi-Layer SSMs](https://arxiv.org/html/2604.14501v1)

5分标准拟仅报告。exact-v1 §3/4.1/6/8的generalized affine-state模型下，post-input自产CoT只是有限状态后处理，不能改变所述通信下界；interleaved thought则可改变读入期间计算。streaming模拟用可任意定义的token-dependent transition/readout与有限每段thought，不证明实际Mamba可训练、低时延或定长CoT通用。d²p通信摘要不等dp持久状态。Ch22容量合同已经区分compute/state/读取，本理论具体timing条件值得留报告，不据此追加训练处方。必要声明/构造已读，未无差别核全部独立下界证明，也未声称headline普遍定理已验证；非作者实际必要声明/构造及Ch22真实容量合同对读通过，标准仅报告终态。

### [Dissecting Failure Dynamics in Large Language Model Reasoning](https://arxiv.org/html/2604.14528v1)

5分标准已有覆盖，非作者必要来源和当前真实正文复核通过。exact-v1 §3–5/关键表将事后segment-error oracle与在线entropy quantile触发分开；短分支来自同prefix，比较平均entropy并保留一条，再另作late-stage控制。低entropy不是正确性oracle，事后onset比例不等在线检测率。Ch80实际196–214已承载cheap sensor→bounded repair/slowcritic、negative提示改变分布、额外分支与净成本分账，足以支持此窄命题，非仅主题相似。Qwen1.5/7B/QwQ32B八任务，某单任务低于Reflexion，主轨迹缩短不证明total compute/生产wall-clock减少；实际完整硬件/precision/并发SLO ND。非作者实际source→owner复核通过。

### [VoxSafeBench: Not Just What Is Said, but Who, How, and Where](https://arxiv.org/html/2604.14548v1)

6分安全缺口深入提案。exact-v1 §3/AppendixJ1–J3/Table42对相同音频分别问cue识别与norm-dependent safe decision，另用text-explicit-cue参考：能识别不等安全使用，但probe问法更简单，不提供完美内部因果分解。root反向实际对读Ch66 L3226–3234 perception/reasoning及grounding/rule应用分账：采用原则已承载；cue识别/规范行动的matched任务是受限诊断案例，精确recipe仅报告，不冒称完美因果分解或全部Existing。英中/syntheticaudio/若干Omni与API、三人audibility验证；emotion仍感知混杂，文本参考不是音频模型已抽取cue的证据。hardware/precision/productionSLO ND；声纹/年龄感知不拥有身份授权。UnsafeBackground的NSFW cue存在与教学适宜性规范标签并非同一变量，不当严格上下界。有效必要源审继续复用，root当前owner反向语义裁决Only通过，不新增同义主干。

### [MARS2: Scaling Multi-Agent Tree Search via Reinforcement Learning for Code Generation](https://arxiv.org/html/2604.14564v1)

6分缺口深入提案。exact-v1 §2.2–2.4 Eq3–8/§3.1/§3.3/Table1中，每节点是完整解答proposal；parent/sibling reward mix后shaping，再按跨agent tree组归一，独立policy只更新自己生成节点。这是credit参照共享而非让他人token变on-policy，path也不等真实工具共享prefix。Ch33现有sharedprefix与treefork主干缺这条异构policy/tree reference责任分支，拟窄补，不采用unbiased或原objective不变。7992过滤代码题、Qwen/AReaL8/14B、公共test驱动搜索/private验收；部分AReaL pass@8不如single-tree，sequential expansion牺牲并行，同数据预算不等wall-clock；单模型shaping曲线不证明普适variance降低。硬件/precision/完整成本/SLO ND，非作者实际必要原文及Ch33真实窄缺口对读通过，实际Ch33正文及邻接经root写后PASS，已真实整合。

### [Prompt Optimization Is a Coin Flip: Diagnosing When It Helps in Compound AI Systems](https://arxiv.org/html/2604.14585v1)

材料家族：SF-2026-ARXIV-2604-14585。§3–5/Table1–2的两executor×三个任务（HotpotQA/MBPP/XSum）的六条件、统一A→B两Agent pipeline、10×10 prompt grid、每格30个benchmark samples并作question blocking与六优化方法是受限比较。interaction F<1/p>.52不能证明无交互或联合优化无用，49%的72组低于baseline不等普遍coin-flip规律；best-of-10–20在同20题上挑headroom有选择偏差。Ch74/66已分配选择集和验收集，具体负面测量保留报告，不把instruction-tuning压缩phrasing的未干预解释当因果。2+1+2=5，正确性边界深入拟Only；API预算不等跨任务总compute，hardware/precision/SLO ND。 非作者必要方法/反证及实际owner核通过，仅报告受限贡献。

### [AgileLog: A Forkable Shared Log for Agents on Data Streams](https://arxiv.org/html/2604.14590v1)

材料家族：SF-2026-ARXIV-2604-14590。§4.1/5.4–5.7/6.4/6.8：cFork继续继承parent append，child私写不反流；sFork则切断后续继承。promotable flag预设，earliest fork point之后parent读被挡住且索引暂扣，append仍可继续；首个promotion胜出并淘汰其他分支。因此不能采用无条件no-interference。Ch81‘搜索分支必须连同权威外部状态一起分支’已有snapshot/COW/commit，但缺live inheritance的顺序与promotion barrier/catch-up代价；2+2+2=6缺口深入。CloudLab九MinIO/三元数据replica/4KB records，metadata stress不是end-to-end大规模测量，schema注入不证明开放语义安全。apr01已实际核必要方法/设置和Ch81约264–286，窄gap通过；有效必要source→owner采用已通过；已实际写入live/static、promotable读屏障/catch-up分支，root完整正文/两侧交接及有效必要证据复用写后PASS，真实Integrate。

### [Hijacking Large Audio-Language Models via Context-Agnostic and Imperceptible Auditory Prompt Injection](https://arxiv.org/html/2604.14604v1)

材料家族：SF-2026-ARXIV-2604-14604。§III–V/VII–VIII：白盒参数与audio-only修改，不能推广成任意黑盒产品攻击；gradient估计跨离散tokenization并以多context/attention-steering及reverb混合隐藏注入。13 LALM的13000普通目标试验与三tool模型四工具分开，PISR phrase/BMSR行为也分开。attention PCA+SVM在原威胁precision.98/recall.93，但降低steering的adaptive κ=.01可使recall.69/precision.90，成功率代价有限。root反向实际对读Ch72 L1439–1449 adaptive audit与L2692–2697 probe identity/扰动回归：attacker-aware变异改变校准面的采用原则已承载，降低steering的具体音频攻击是受限反证案例，仅报告，不冒称全部recipe Existing；2+2+2=6安全深入。未测试全部生产设备或权限effect；§V披露全部bfloat16、15s carrier、train/test各100条指令不交集、batch4、默认κ=.015（adaptive .01）；线上concurrency/SLO及生产设备未完整披露，有效必要源审继续复用，root当前owner反向语义裁决Only通过，不新增同义主干。

### [Pushing the Boundaries of Multiple Choice Evaluation to One Hundred Options](https://arxiv.org/html/2604.14634v1)

材料家族：SF-2026-ARXIV-2604-14634。§3/5–7/Table3–4：30 Korean orthography目标，N4–100与八种前后padding控制区分dense distractors和长度；五模型temp0/index exact match，只有这些目标与格式。semantic neutrality不完美，HyperCLOVAX padding spread是模型依赖例外；低N ceiling不证明能力真值，高N也不自动更好。Ch66 matched permutation/direct-CoT及Position–Content–Length factor grid具体已承载此采用边界，2+1+2=5标准拟已有覆盖；不新增benchmark摘要，hardware/precision/SLO ND。非作者实际必要原文与Ch66具体机制正文对读通过，标准已有覆盖终态。

### [Acceptance Dynamics Across Cognitive Domains in Speculative Decoding](https://arxiv.org/html/2604.14682v1)

材料家族：SF-2026-ARXIV-2604-14682。§III–VI：TinyLlama1.1B/Llama2-7B-Chat GPTQ4b、两T4、四领域各50题、input≤512/output≤64，树depth3/max8/root3/branch2，temp0/use_cacheFalse。记录top-k/greedy节点的min(1,p/q)而非实际随机接受路径；Eq3各深度mean-alpha乘积未提供独立/条件路径权重，不一般等于期望路径乘积，例如同Bernoulli(.5)相关两层时E[α1α2]=.5而均值乘积=.25。99k节点不是独立prompt样本，chat 1.065的代理不包含draft/bonus/full-forward成本。2+1+2=5窄正确性深入Only；保留局部agreement测量，不采用领域收益或RLHF因果保证。Ch48已有exactness/wall-clock分权，不新写recipe。 非作者必要方法/反证及实际owner核通过，仅报告受限贡献。

### [Gating Enables Curvature: A Geometric Expressivity Gap in Attention](https://arxiv.org/html/2604.14702v1)

材料家族：SF-2026-ARXIV-2604-14702。§2/3.1/3.5/3.20/4：固定values、系数张成convex相对内部及unit-covariance Gaussian decoder下的仿射坐标metric是平坦基线；multiplicative gate构造曲面族不是所有现代attention唯一曲率来源。原文§4也承认nonlinear输入时ungated可非零。C² function-space generic不能替代有限参数learnability；seq8/proj64/2D synthetic任务的有限差分二阶导数proxy不是内在Gaussian curvature本身。2+1+2=5标准Only保留假设化理论，Ch14现gating机制不据此升级必要条件；未核无关独立证明/未复现。 非作者必要方法/关键反证与实际owner对读通过，仅报告终态。

### [A Mechanistic Account of Attention Sinks in GPT-2: One Circuit, Broader Implications for Mitigation](https://arxiv.org/html/2604.14722v1)

材料家族：SF-2026-ARXIV-2604-14722。§3.1–3.2.6/Table1/4–5：bQ、首MLP的absolute-position成分与Wk形成协调路径，null/transplant与控制支持GPT2-124M特定电路。bQ归零后BOS attention为.251，baseline .563，保留基线的44.7%（非absolute attention 44.7%），‘必要’只能限主要机制而非现象消失；300样本/三域/40token/layers4–11的sink值不是质量结果。别的架构缺该组件仍有sink，也不证明本研究重测全部架构。Ch14 Sink/Outlier段实际已有跨depth/token控制干预且拒绝单一普适归因，2+1+2=5标准Existing；不新写GPT2摘要，未核training emergence因果。 非作者必要源与Ch14实际机制正文对读通过，已有覆盖终态。

### [Expressivity of Transformers: A Tropical Geometry Perspective](https://arxiv.org/html/2604.14727v1)

材料家族：SF-2026-ARXIV-2604-14727。官方HTML/PDF v1题名一致，库存旧题名不作证据。§III/IV.3–IV.5/V.2/V.5/VI.1：fixed-context keys下zero-temperature top1划power diagram，固定V输出piecewise constant；辅助log-lift的τ依赖值是另一个对象。作者已限定全输入Q/K耦合，不能把条件query区域数当完整模型tight容量。有限τ的LSE gradient/Hessian离边界近似不等exact affine：两key logistic在τ>0时一般非零二阶导数。2+1+2=5深入Only，只隔离finite-temperature精确性过述，保留条件化几何，不否定全部理论或遍历全部附录。 另§III-D/VI以softmax(q·k/τ)且原始Q/K定义将standard τ记1/√dk，与标准τ=√dk不符；dk64/τ.125/e^-16不能作为实际Transformer精度证据。非作者必要方法/局部反证与实际owner核通过，仅报告，不扩大否定全部理论。

### [Constraint-based Pre-training: From Structured Constraints to Scalable Model Initialization](https://arxiv.org/html/2604.14769v1)

材料家族：SF-2026-ARXIV-2604-14769。§III Eqs6–13/IV TablesVI–VIII：W=ΣT⊗S，pretraining的结构化前缀mask覆盖多depth/width；新shape先固定模板T并用数据更新少量scalers，再进入无约束full training。不是任意checkpoint后分解、零数据迁移或pretraining替代。Ch28形状mapping/optimizer-state/rewarm已有mid-run growth，却缺主动预训练可复用templates→target initialization的选择分支，2+2+2=6缺口深入。ImageNet/ViT、DiT与CNN等有限配置，FID下降代表改善不能误判为退步；模板冻结/异构operation需重设、目标适配与pretraining成本仍须计入，未有统一总预算/线上SLO保证。非作者必要源与Ch28具体缺口对读通过，已实际写入主动模板预训练/目标适配分支，root完整正文/两侧交接及有效必要证据复用写后PASS，真实Integrate。

### [Knowing When Not to Answer: Evaluating Abstention in Multimodal Reasoning Systems](https://arxiv.org/html/2604.14799v1)

材料家族：SF-2026-ARXIV-2604-14799。§3–6/Table1–4/G.4：2079个MMMU/MMLongBench派生任务，22 missing/corrupt/contradictory变换，人工/模型filter不等全数据truth。三VLM、≤3轮agent/SC N10、temp.1/.7；UAC与AAC要联合报告，关键词拒答extractor/heuristic gold可能误分。human oracle MCC.83是引用human成绩及98.5% UAC假设推导不是新实测；同test扫confidence τ仅oracle upper bound，不是在线固定控制器。2+1+2=5标准Only保留受限multimodal abstention评价分支，Ch66现拒答/typed predicate与conditional slice已经约束采用，不称prompt无效或training必然必要；hardware/precision/SLO ND。 非作者必要方法/关键反证与实际owner对读通过，仅报告终态。

### [Modeling LLM Unlearning as an Asymmetric Two-Task Learning Problem](https://arxiv.org/html/2604.14808v1)

材料家族：SF-2026-ARXIV-2604-14808。§3.3–3.5的module PCGrad仅冲突时投影，SAGO在同号坐标用forget梯度、异号用retain梯度；非负retain内积可支持局部一阶方向，不证明有限步全utility或参数知识删除。‘相同权重SAGO总比PCGrad方向更准’不成立：g_r=(1,1)、g_f=(100,.01)同号，SAGO=(100,.01)，PCGrad=(101,1.01)，后者与g_r的cosine反而更大；§3.5也把仅冲突时的投影误作普遍正交。WMDP Zephyr7B与RWKU Llama3-8B、50目标/邻居、MMLU与ROUGE回忆，不是retrieval全部旁路删除证明。2+1+2=5安全/窄理论深入Only，保留受限经验，不采用dominance或无副作用保证；Ch72真实secret-substrate/retain-utility分账覆盖采用边界，不因bio任务转AI-for-Science。 非作者必要方法/关键反证与实际owner对读通过，仅报告终态。

### [Does RL Expand the Capability Boundary of LLM Agents? A PASS@(k,T) Analysis](https://arxiv.org/html/2604.14877v1)

材料家族：SF-2026-ARXIV-2604-14877。§2.2–2.3/3/4.1/5：PASS@(k,T)分别扫独立尝试与每次interaction depth，Qwen2.5-7B同200题、SFT privileged gold trajectory与GRPO binary EM，three categories各100题、n64、T{0,1,2,3,5}、temp.7。它新增二维预算比较：更多浅层重采样不等同允许反馈依赖的深层query；但64次未命中不是π支持集为零，bootstrap以观测p=0重采样不能恢复未见成功。首次成功轨迹query/observation交换有selector conditioning，也不能把同题训练等同总compute/探索唯一因果。root反向实际对读Ch66 L677–693 coverage/reliability与L3859–3865 seed width×iteration depth、matched compute/scorer/stop：采用的二维预算与有限未命中原则已承载；具体pass(k,T)实验仅报告，非精确recipe全称Existing；2+2+2=6，保留有效深入证据，不采用无限能力扩张保证。hardware/precision/线上SLO ND，有效必要源审继续复用，root当前owner反向语义裁决Only通过，不新增同义主干。 §2.4的T单调需策略嵌套、早停或best-feasible/coupling前提；实际每(q,T)独立rollout非长轨迹截断，Table2 base/B k64 T1=.840>T2=.820不证明形式单调。只报告受限正交预算结果，不采用自动深度收益保证。

### [Reasoning Dynamics and the Limits of Monitoring Modality Reliance in Vision-Language Models](https://arxiv.org/html/2604.14888v1)

材料家族：SF-2026-ARXIV-2604-14888。§4/5.1–5.2：18模型reasoning动态与四Qwen变体的hint干预监测分开；MathVerse vision-only baseline-correct>50%选择、每条件10responses、Qwen3VL32B-Instruct统一monitor。hint-aware与image-vs-text attribution的不同视图会反转排名，长CoT流畅不证明视觉来源faithful，rewardhack弱效应不足阈值时不报可靠monitorability。控制cue有behavioral total effect，不识别所有内部因果，training paradigm同时含架构/recipe混杂。Ch66 Model Self-report不能拥有输入来源真值（实际137–148）已经要求authoritative provenance+cue intervention+self-report分权，Ch72 reasoning monitor已有可见channel条件；2+1+2=5安全深入Existing，不复制新榜单，不采用推理训练总能纠错。hardware/precision/SLO ND。 非作者必要源与Ch66真实provenance/cue/self-report命题核通过。

### [Beyond Importance Sampling: Rejection-Gated Policy Optimization](https://arxiv.org/html/2604.14895v1)

材料家族：SF-2026-ARXIV-2604-14895。§4.2–4.4 Eq7–13/5.2/AppendixA.3明确gate参与求导、有效weight为g′(r)r；bounded w与平方可积score×adv条件给有限方差，不是g有界就自动w有界。中心policy-improvement证明Eq40 |r−g(r)|≤L_g|r−1|不成立：本文sigmoid g(1)=.5，r=1时左.5右0；MDP Eq38直接用旧policy state分布也未处理occupancy shift。因此隔离该TRPO式严格保证，不否定受限surrogate/经验。Qwen2.5-1.5B HH-RLHF、43,835prompts/三seed，reward-model分数/KL非安全truth；Table7 .042/.045同时写> .04 spike0也需作者解释。2+2+2=6窄正确性深入争议；非作者apr01已实际核Eq11–13和AppendixA.3 Eq38–42，反例通过。仅隔离policy-improvement保证，不据未成立保证写Ch33。

### [Reward-Aware Trajectory Shaping for Few-step Visual Generation](https://arxiv.org/html/2604.14910v1)

SF-2026-ARXIV-2604-14910。§3.1–3.4/4.4/Table5–7：同noise/prompt的少步student与50步EMA teacher按sigma horizon对齐，x0 cosine/L2 shaping与terminal reward并用；reward差stop-gradient sigmoid gate不是硬拒绝，相等仍为.5、teacher较差也非零。FLUX.1-dev/Wan2.1-T2V1.3B、video BF16/400steps/rankbatch1×accum8；额外teacher训练成本不等零成本，部署不增加teacher只相对同student schedule。部分Color/ImageReward退步，不能称teacher为普遍上限或学生全面超越。2+1+2=5标准仅报告有限连续轨迹适配，不因Ch29已有alignment≠utility就宣称所有接口已有覆盖；非作者必要来源/关键反证及实际owner核通过，无生产SLO保证。

### [WavAlign: Enhancing Intelligence and Expressiveness in Spoken Dialogue Models via Adaptive Hybrid Post-Training](https://arxiv.org/html/2604.14932v1)

SF-2026-ARXIV-2604-14932。§3.1–3.4/4.1–4.3.1/Table1–3：共享参数mixed text/audio的GRPO只计算text token likelihood，all-token SFT提供声学anchor；loss mask不冻结shared参数。归一reward variance×good-sample existence及EMA调hybrid比例，不是truth或安全概率。Ch31约977行现有branch/region credit没有这条稀疏semantic preference与dense acoustic anchor的监督职责分离；canonical TRAIN-RLHF，拟2+2+2=6缺口深入最窄补充。VITA/KimiAudio、13.5k训练、G4/T.9/top-p.9/max2048、4A100、KL.01；scope×mix消融支持局部选择，style仍有相对SFT退步，evaluator/架构差异不能合成通用声学稳定保证；部署SLO ND。apr01已实际核必要原文/表和Ch31约965–1005，窄gap通过；有效必要source→owner采用已通过；实际Ch31正文及相邻段经root写后PASS，已真实整合。

### [What Is the Minimum Architecture for Prolepsis? Early Irrevocable Commitment Across Tasks in Small Transformers](https://arxiv.org/html/2604.15010v1)

SF-2026-ARXIV-2604-15010。exact-v1 §3–8/AppendixG的CLT、residual controls及layer-skip复制直接研究早commit机制，未因小模型排除。Gemma2-2B/Llama3.2-1B、BF16/16GBconsumerGPU，最后prompt位置不同于原newline；CounterFact89对按同一Llama3.2-1B能正确预测original与counterfactual两答案选择；Gemma未做该事实召回扩展。Table2 L24–25 skip仍8/10，而L22–25 skip0/10；架构/recipe不同不能证明通用16层门槛，有限feature strength未纠错也不是永久不可纠错。Ch66已有paired intervention/诊断边界，新受限复制保留5分标准Only提案，不写普遍架构controller。完整必要判断见作者notes第十二小批；非作者apr17_final_batch_review必要源/owner核通过，未复现实验/部署SLO ND。

### [ControlFoley: Unified and Controllable Video-to-Audio Generation with Cross-Modal Conflict Handling](https://arxiv.org/html/2604.15086v1)

SF-2026-ARXIV-2604-15086。exact-v1 §3.2–3.4/4.3.2/4.5–4.6/Table9：reference CLAP路径去位置编码、temporal conv改MLP/linear，另注global timbre，visual保frame sync，统计完全解耦并未证明。Table9两路消融支持有限timbre/sync选择，未单独消融去位置编码/时间卷积抑制模块，不证明其独立同步因果；L0 CLIP-only IB略优、无REPA IS更高、15音频样本/10人MOS不全面支持。54DiT blocks/25steps/44.1kHz，作者176TFLOPS FP32训练描述不能当部署hardware/precision；batch/concurrency/SLO ND。Ch23现有content/timbre流及modality conflict没有明确“reference-style抑时间 vs visual timing身份”的接口，6分缺口深入最窄两段提案；非作者apr17_final_batch_review source→owner通过，现已实际写入且root真实正文/邻接与必要证据复用后写后PASS，不称全模态priority已可靠。

### [OpenMobile: Building Open Mobile Agents with Task and Trajectory Synthesis](https://arxiv.org/html/2604.15093v1)

SF-2026-ARXIV-2604-15093。exact-v1 §3.2–3.3/4.1/5.1/Table3/B.2：不以expert/learner动作分歧自动定错误，实际progress监控后切换；训练只取expert步骤，learner错误保留为history。Ch29当前privileged→observable→replay仅讲数据来源，未承载失败state可见但失败动作不监督的恢复target职责；6分gap深入TRAIN-SFT拟最窄补充，不因已提论文名判Existing。两QwenVL7/8B+Gemini3.1ProPreview、2800指令34k步骤20apps、batch32/lr1e−5/3epochs；同1500轨迹对照、ER人工50条、三次mean±half-range非CI。共同apps及embedding相似度过滤不证明零污染，hardware/precision/SLO ND；非作者apr17_final_batch_review source→owner通过，现已实际写入且root真实正文/邻接与必要证据复用后写后PASS。

### [From Procedural Skills to Strategy Genes: Towards Experience-Driven Test-Time Evolution](https://arxiv.org/html/2604.15097v1)

SF-2026-ARXIV-2604-15097。exact-v1 §3.3/4.1–4.3/Table2–7比较经验表示与相同上下文预算，不在本阶段开展AI for Science。4590 retained trials/45 code-solving scenario、120s sandbox、checkpoint fraction非任务binary成功；Pro cleanGene59.9<无guidance60.1、两互补gene44.9<baseline51，不能声称更多经验或该表示总提高表现。结构/flattened比较不是实际online editing的因果验收。Ch77已要求经验derived/provenance与heldout验证，但本文新局部包装对照并非全部Existing；5分标准Only拟保留受限反证，不从提示结构授予policy权。Gemini3.1ProPreview/FlashLite，hardware/precision/SLO ND；非作者apr17_final_batch_review必要源/owner核通过。

### [IG-Search: Step-Level Information Gain Rewards for Search-Augmented Reasoning](https://arxiv.org/html/2604.15148v1)

SF-2026-ARXIV-2604-15148。exact-v1 §2.1–2.4 Eq2–6/3.1/3.3/3.4.3：gold-answer长度归一logp比较真实doc+refinement与三组random doc+refinement，history不变，随机批内仅近似匹配长度/结构分布，非逐样本严格长度配对；非ShannonIG或纯query因果。proxy仅加query-token，其他token保terminal adv，all-fail仍有proxy不等真值。deadzone/damping/log softclip/controller成本保留，log softclip不是全值硬有界，好query也可因竞争证据得负值。Ch33局部credit尚无该gold-conditioned反事实document基线与query-only责任分离，6分gapDeep拟两段并交接Ch76 validity。Qwen2.5 3/7B、8H800、G5/T1/max5calls、E5/Wiki2018/top3、200steps/1e−6/KL.001；Bamboogle .424<GiGPO .641、非全matched总compute，precision/SLO ND。非作者apr17_final_batch_review source→owner通过，必要source→owner采用已通过；实际Ch33正文及邻接经root写后PASS，已真实整合。

### [DPC: Training-Free Text-to-SQL Candidate Selection via Dual-Paradigm Consistency](https://arxiv.org/html/2604.15163v1)

SF-2026-ARXIV-2604-15163。exact-v1 §2.1–2.3/3.1–3.5/4.1–4.3/Table4。原DB执行聚类取top2后构造可区分的MDD，再比较同backbone Pandas；二者一致不证明参考程序/自然语言意图正确，Eq4是理想覆盖前提而非已证明全语义覆盖。浮点四位/date截日的normalizer可合并重要差异，Table4多数正确选择97%非100%。Ch66已有inputdomain/reference/oracle/matcher分权，5分标准Only拟保留新受限recipe，并深入收窄“deterministic correctness”采用范围；不否定全部经验或自行制造公式争议。BIRD500/Spider2147、5candidates/T.7/retry3、单A80080GB/local+API，precision/并发/SLO ND；非作者apr17_final_batch_review必要源/owner核通过。

### [An Analysis of Regularization and Fokker–Planck Residuals in Diffusion Models for Image Generation](https://arxiv.org/html/2604.15171v1)

SF-2026-ARXIV-2604-15171。exact-v1 §III–IV/TableI/Fig9对FP/score-norm/Jacobian/divergence正则，显示residual/生成质量/训练成本分账。MNIST28²/U-Net/VP-SDE/200epochs/20runs/RTX5070/RyzenAI9/PyTorch2.9、10k LeNet-FID；FP lr1e−3 vs其他5e−4混杂，误差条不证明严格等效。FP与score-norm FID16.25±7.16/17.50±7.89、time12.32/6.36s每epoch；强λ残差可反变差，不从marginal/conditional score近似推出普遍导数恒等。Ch24广regularity/solver验证不能当完整覆盖这个具体配方；5分标准Only保留有限反证与代价，不因MNIST排除，也不据代理residual发布质量。deployment precision/SLO ND，非作者apr17_final_batch_review必要源/owner核通过。

### [Discovering Novel LLM Experts via Task-Capability Coevolution](https://arxiv.org/html/2604.14969v1)

SF-2026-ARXIV-2604-14969。负向抽检纠正原“成熟组合”关闭：官方v1 §3 Algorithm1/任务归档说明里，active task池按当前模型population的pass-rate调难度，global task池管novelty与最终taskforce选择；每次admit新任务后重评旧模型skill vectors，选择参照也随归档变化。这是具体feedback/state接口，不是merger正确性或可执行答案selector，2+1+2=5标准保留。自身v1 Updated为2026-04-17T00:49:08Z，只作为官方slot、连续ID/OAI/邻界共同推断的一个字段，不单独作first-public。

§4 Table1/2区分Coverage的oracle OR与实际BoN，后者对部分big-model/GPT-4o基线退步；§D.6拿同run第5代作为static终态代理，不是同总预算长期冻结任务的受控对照。§6还限制same-base seeds与固定scientist；合并/evaluation/scientist成本不能只按参数量或单模型显存结算。Ch27静态mixture→control plane与Coverage正文已要求版本化信号、active set、held-out验收及proxy风险，但不是这个双archive实现的完整已有覆盖。只报告该有意义的局部设计分支及证据压力，暂不从未匹配的对照采用普遍持续创新/成本优势；不因协调Books等待而降级，也不恢复AI for Science应用范围。非作者前置审计已定位此接口与关键反证，最终处置核对记录见[日期/覆盖/准入独立审计](../_sources/daily-20260417/V3_DATE_ADMISSION_COVERAGE_INDEPENDENT_AUDIT.md)。未复现实验，线上precision/concurrency/SLO未披露。

## 5. 缺口与下一步

普通扫描/题摘/单篇证据/Books及实际写后队列已清零；最后14433/14769/14590/14512四条真实正文与两侧交接均由root读后通过。六项14198/14548/14877/15022/14865/14604按当前具体owner的一般原则关闭为仅报告，不冒称精确recipe全部已有覆盖。有效89项必要来源证据复用，不扩536项全文；最终分母、日期/来源限制及六部分整体语义已由root验收通过。

本窗终态保留项：机构历史Research/Blog目录精确缺口见§2；late/postchanged-v1材料仍须原始窗口身份，不冒充普通审阅完成。这些保留项不用于正面证据、Books或无遗漏断言，定点重开条件如下。MoE中心保证反例已独立核为窄争议，不影响可分离经验记录。Simula Blog与2603.29791v1已同家族消歧，原文仅重复解释无重要修订，不成为本窗新候选；日精度不伪造时间。

这些均已到安全终态，不是未读普通工作或全部旧库存pending：八机构子入口仅在取得对应官方带日期历史目录/缺失release响应后重开对应事件。日期保留身份为2604.14152、2604.14188、2604.14240（缓存v1/OAI后改字段不能恢复原始公告身份），2604.15180（v1 Updated=01:00:24Z跨截点）、2604.15186（01:01:05Z）、2604.15302（01:06:20Z）；此为实际记录涉及的有界名单，不声称穷尽未知事件。它们仅在取得原始公告membership或可靠首次公开记录后重开归属，当前不作本窗正面证据/Books依据，不仅凭Updated机械移日。14500只在Lemma1等式/单调前提被更正并补足证明后重开几何保证，14258只在Eq21→22的loss/gradient身份与爆炸条件被澄清后重开保证，14324只在signed/unsigned距离与分区实现一致后重开算法保证，14895只在r=1 gate梯度反例和occupancy-shift前提被修复后重开policy-improvement保证。四争议仅隔离上述保证，不用于正面采用/Books，现有可分离经验仍按§4限域保留；日期保留项、八外部子入口和四争议均不支持零遗漏、性能或安全保证。

本日首批5项已实际写入并经root必要原文/真实正文及相邻衔接的写后独立复核通过：Ch49的bit/tier数据通路、分层tile IR与checkpoint/probe，Ch36的通信字节分账与DiT readiness/cache分权。其余必要改动也全部真实写入并通过root写后，累计33项；6项反向仅报告已通过；旧稿未经核实的采用不继承。本日完成只表示本窗安全闭环，不表示整个4月或全部外部材料已完成。

## 6. 复核

复核者：root（非报告作者）
结论：通过

实际核对14来源的入口/停止范围与八项具名缺口、固定窗口及六项日期身份隔离、准入负向抽检后的14969修复、89唯一表行与89证据小节的一一对应、50深入/35标准/4窄争议、33整合/17已有覆盖/35仅报告/4争议，以及33处真实正文及相邻交接的有效写后复核。必要单篇来源证据未变的继续复用；不把536标题查漏称作536全文审阅，不把外部保留项改称通过。无普通可执行待办；本次最终日级Gate覆盖下方前置审阅时的未决状态。机器校验和diff检查仅证明可判定一致性，不代替上述语义复核。

当前写后状态（覆盖下方历史“仍未写Books”的阶段记录）：首批14626/14825/15167→Ch49、14561/14690→Ch36已实际正文写入，并由root重开必要exact-v1原文/实际正文及相邻交接独立PASS。正式表/§4与Review notes已同步33项真实Integrate，新增Ch21/25的14246/14268、Ch20/23的14862/15086、Ch29的15093/14164。Ch31的14932/15149已真实落笔并经root实际正文及相邻段写后PASS。Ch33的15148/14564已实际落笔并经root完整正文/邻接写后PASS。Ch24的15009/14379/14591已实际正文及邻接写后PASS，其中14591原硬恢复歧义改成mask外更强source nudging后由root再次实际读句通过。Ch22的14191/14339完整正文及交接亦root写后PASS。原39项中6项反向Only通过，必要实际写入队列33项均已落笔；独立写后通过33、待写后0、未落笔0；章节锁等待属于普通协调，不是外部材料Blocked。最后Ch66/28/81/83四处新增及两侧亦root实际顺读PASS，共33I/17E/35Only/4D/0普通；最终分母已由root冻结且日级Gate通过；前述待验只属历史阶段。

作者本轮复核：来源顺序/窗口、具体题摘理由、必要exact-v1方法及关键负例、已有owner实际对读已分批保留；作者检查不替代整日验收；当前非作者整日结论见本节开头。

历史前置审阅路径（不是当前Books状态）：最新[日期/覆盖/准入前置独立审计](../_sources/daily-20260417/V3_DATE_ADMISSION_COVERAGE_INDEPENDENT_AUDIT.md)实际对读14来源行、8外部子入口限制及记录停点，核原88身份/证据对应、三个保留及四个排除样本；联合字段支持有界日期推定，未冒称逐篇公告membership已恢复。负样本14969的具体参照反馈漏收已局部重开，5标准Only内容处置通过；作者同步后实际再算89唯一表行=89唯一证据标题、无missing/extra，50深入+35标准+4争议，当时39拟Books普通待办+17Existing+29Only+4争议。此为实际结构差异校验和前置语义复核，其后33必要改动及6Only反向处置已全部落实，当前状态唯一由本节首段决定；此前置审计不代替最终日级Gate，不重复原88有效单篇审阅。

历史单篇必要审阅路径（以下保留有效身份、原文范围与反证，当前Books/写后状态唯一由本节首段决定）：非作者apr01对14251/14258/14324及14325/14345/14363/14430实际读取必要exact-v1方法、公式/关键反例及相应采用边界后完成有界复核：CTD具体Ch56缺口通过，两项中心矛盾成立，后四项Only与窄反证成立。另实际读取14932 §3.1–3.4/Table3、14862 §3.1–3.4/4.1/Table1/3、14590 §4.1/5.3–5.6/6.8及Ch31/20/81实际相邻正文，三窄gap通过；Prompt-only说明歧义只按四配置实际位置限定，不称key token-length已匹配。另apr17_final_batch_review对15010/15086/15093/15097/15148/15163/15171重开官方exact-v1必要方法/评价和实际owner后通过有限复核，15010同一Llama两答案筛选条件已纠正，15086单模块因果与15148长度配对边界已收窄；记录见[七项独立复核](../_sources/daily-20260417/V3_FINAL_BATCH_INDEPENDENT_AUDIT.md)。另[十项Existing/Only独立复核](../_sources/daily-20260417/V3_EXISTING_ONLY_BATCH_INDEPENDENT_AUDIT.md)对14228/14362/14414/14572/14612/14683/14419/14434/14717/14732重开必要原文及当前具体owner：6已有覆盖/4仅报告，14228只采用初始化边界、14732分开两K消融口径。另apr01重开14170 PDF与14246/14268 HTML必要方法、关键反证并对读Ch76/21/25实际相邻正文，三真实gap通过。另[三项原始缺口独立复核](../_sources/daily-20260417/V3_ORIGINAL_GAP_INDEPENDENT_AUDIT.md)重开ECG PDF必要页与CBCL/CoCoDiff必要方法、真实owner，三窄gap通过。另apr01实际核14500的Lemma1/Theorem2、14473的Assumption2及AppendixC条件独立桥、14895的Eq11–13/AppendixA.3；两窄保证争议和RUMS受限Only/理论hold通过，不否定全部经验。另[第二十项独立复核](../_sources/daily-20260417/V3_ORDINARY_TEN_INDEPENDENT_AUDIT.md)实际核10必要来源和真实owner：4已有覆盖/6Only；TRACER floor、HyPeR对照模型、GUARD测试集和LongAct clamp样本口径已纠正，SWE-TRACE受限wall-clock保留。另[第二个十项窄gap独立复核](../_sources/daily-20260417/V3_ORDINARY_TEN_TWO_INDEPENDENT_AUDIT.md)实际读取10项必要exact-v1方法/反证及当前真实owner，全部窄提案通过；MemoSight累积memory非无限常数cache、Chain有P95/P99而非通用SLO、PrfaaS transfer完成后才回收尾块及部分RLVR零shortcut均已收窄。另apr01实际核MixAtlas官方PDF-v1及Ch27现有两轴一般分支、MaskedLogitNudging Eq6/9与style关闭refinement、SegmentCoherence训练pooling/benignSegVar与在线prefix EMA，并对读Ch24/72当前真实owner；三项当时窄提案通过，其后14198/14865反向Only、14591实际I写后通过。另[第三十项独立核](../_sources/daily-20260417/V3_ORDINARY_TEN_THREE_INDEPENDENT_AUDIT.md)重开10必要方法/关键反证并对读实际owner：7窄gap、2Existing、1Only，14191冻结input-output embedding和14433单RTX4090/总12–15h纠错已落实；不采用TrigReason矛盾τ默认配置。另[第四十项独立核](../_sources/daily-20260417/V3_ORDINARY_TEN_FOUR_INDEPENDENT_AUDIT.md)实际核10必要原文和真实owner：4窄gap/3Existing/3Only；14585每格30题而非30生成、14604全部BF16、14548规范与cue配对非完美因果分解已纠正。14604当时提案只adaptive-detector surface，其后反向裁决Only，不重复既有来源授权。另[最后九项有限独立核](../_sources/daily-20260417/V3_ORDINARY_NINE_FINAL_INDEPENDENT_AUDIT.md)实际核9必要原文及真实owner：2窄gap、2Existing、5Only；14722 absolute .251/baseline .563与44.7%base、14727标准温度τ=√dk、14877策略嵌套/早停/coupling前提三修正已落实。合计89项非作者单篇核验，不代替分母冻结、日期/来源日级复核或实际Books写后；未复现实验。必要改动落实/写后已完成，最终日级语义Gate现已由root通过，历史待验不覆盖本节当前结论；机器校验只可判格式/一致性，不证明来源全覆盖、结论成立或实验复现。
