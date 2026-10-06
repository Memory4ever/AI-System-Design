# Daily Research — 2026-04-07

**规范：** V3
**窗口：** 2026-04-06T09:00:00+08:00 ～ 2026-04-07T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-09-26T15:17:22+08:00

## 1. 结论

本日按当前合同重审，854个原始arXiv唯一身份是标题召回库存，不是候选。旧90项完整题摘重新筛选、旧排除集42项定点完整题摘及非作者反向查漏后，共89个贡献工作家族已读到必要方法、评价与关键反证；其中46项有据推断落入本窗，43项晚字段/后改记录因缺更早公开上界独立隔离，不据 submitted/DOI created移动日期。46项中23项实际整合已过单篇非作者复核、16项具体已有覆盖、7项仅报告；独立抽检恢复的CSRS已标准审阅，不因单类几何/已有主题拒绝，也不把局部一致性proxy当真值。普通审阅/Books待办为0，apr03非作者日级验收通过；完成表示已到合同允许的安全终态，不沿用旧Complete或把隔离项当作已证实。

重要路线为量化/低秩/布局计划的条件分工、去噪与post-training的支持集控制、行动horizon与信息表示边界，以及Agent测试/判断的authority分账。新增机制已整合进章节原推理链，实验退步、模拟/硬件/任务限制与旧方案回退继续保留。3项较晚字段的旧实际Books改动（GenServe/APPA/GPU execution-idle）仍在Books，但不计入本日当窗采用；本轮不删除已核机制。

日期采用有界推断：自身v1字段早于01:00Z且无所见例外，联合连续ID/邻界、OAI批次与官方Monday20:00EDT公告slot，支持北京时间08:00～09:00区间；不是逐篇成功发布日志或Updated等于首发。晚字段只否定该家族的此项上界，不推翻早段归属。[专用日期审计](../_sources/daily-20260407/V3_DATE_RECONCILIATION.md)与[本日证据](../_sources/daily-20260407/v3-reopen-notes.md)保留推断和反例。14来源均有实际入口/停点说明，8个外部历史子入口仍隔离，不能宣称全网零遗漏。

## 2. 来源覆盖

本次只处理14个每日来源，不扩扫每周组。[原始入口与停点](../_sources/daily-20260407/v3-reopen-notes.md#每日机构来源已取得的有界停点)保存查询细节；下表区分可判定的目录结果与已隔离的外部限制，不声称全网零遗漏。

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | [Research](https://openai.com/research/)与research/publication sitemap；04/06 Safety Fellowship是人才计划、非技术贡献，已排除。sitemap lastmod不作首发字段 | 受阻 | 历史Research/Publications分页和首发时点不能从当前索引恢复；不记零命中。官方当窗归档/带公开时间的列表到达后只重开该入口 |
| SRC-ANTHROPIC | [Research](https://www.anthropic.com/research)嵌入publishedOn跨窗相邻04/02T10:56Z→04/07T09:35Z→04/09T16:34Z；中项北京时间17:35晚于截点 | 已检查 | 仅官方Research目录范围，没有确定当窗条目 |
| SRC-GOOGLE-AI | [Google Research四月Blog](https://research.google/blog/2026/04/)可见月列表04/03→04/08之间无条目；定点查[Publications](https://research.google/pubs/)及DeepMind | 受阻 | Blog已处理，历史Publications/DeepMind正文公开目录停点仍不可证；官方当窗导出到达后定点重开，不把全年publication库存当当天 |
| SRC-META-AI | [Blog](https://ai.meta.com/blog)04/06Alta Daily/SAM属于领域应用，正文不足本项目机制贡献；04/08Muse Spark窗外；[Research](https://ai.meta.com/research/)历史目录不可读 | 受阻 | 仅Research子入口历史列表隔离；需要官方当窗目录/原文时间，不以Blog排除证明全部研究无命中 |
| SRC-QWEN | [动态40项](https://qwen.ai/api/v2/article/retrieval?type=qwen_ai&language=en-US)+[静态60项](https://qwen.ai/api/page_config?code=research.research-list)，邻近04/02T04:00+08→04/15T10:00+08 | 已检查 | 本次Research公开列表无当窗文章；不外推全部作者稿 |
| SRC-DEEPSEEK | [官方索引](https://www.deepseek.com/news/)研究邻近06/24→02/25，动态04/24→2025/12/01 | 受阻 | 当前“查看全部”的历史停点不能取得；已隔离，官方完整目录或当窗原文到达后重开 |
| SRC-MOONSHOT | [Platform Blog](https://platform.kimi.com/blog)当前可见最新2025/11/07；Kimi-K2/MoBA官方release API均0条 | 受阻 | Blog未覆盖2026/04历史，0release不证明研究零命中；需要历史Blog/研究原文公开时间 |
| SRC-TENCENT-HUNYUAN | [公开目录API](https://api.hunyuan.tencent.com/api/blog/publicList)POST pageNum1/pageSize100/renderType0，9/9读完，04/23直接跳02/13 | 已检查 | 该官方目录无当窗条目；作者在其他渠道稿件由arXiv独立去重 |
| SRC-ZAI | [Research157](https://www.zhipuai.cn/zh/research/157)GLM-5.1显示04/07 16:00，正文为版本能力/benchmark公告；GLM-5官方release API0条 | 受阻 | 页未明示时区；北京本地推定已过截点，但不能作确定日期排除。仅线索不入分母、不评分/Books；官方时区/首次公开证明可重开 |
| SRC-BYTEDANCE-SEED | [论文目录API](https://seed.bytedance.com/api/get_article_list_v2?article_type=1&count=20&order_desc=true&page_token=40)，US locale页0/20/40/60越过边界；04/07T16:00Z→03/31T12:00Z | 已检查 | 显示时间范围内无当窗目录条目；外链arXiv使用其正文首发批次，不按站点收录移动日期 |
| SRC-BAIDU-ERNIE | [Blog](https://ernie.baidu.com/blog/zh/)04/15→02/06；[ERNIE releases](https://api.github.com/repos/PaddlePaddle/ERNIE/releases?per_page=100)唯一条目2025/06/30 | 已检查 | 所查Blog/release无当窗条目，不代表所有普通commit或未列仓库 |
| SRC-XIAOMI-MIMO | [Paper/Blog](https://mimo.xiaomi.com/)Paper06/29→03/13/02/03；MiMo/MiMo-VL/MiMo-V2-Flash官方release API0条 | 受阻 | Paper/release已处理；Blog未给历史公开时间，隔离该子入口，官方日期归档到达后重开 |
| SRC-MINIMAX | [英文Blog](https://www.minimax.io/blog)05/26→03/18；[中文Blog](https://www.minimaxi.com/blog)重定向路径恢复日期目录，05/25→04/27→03/18，无本窗列项；M2/M2.5/One-RL官方release API0条 | 受阻 | 英文/中文所见目录与列出release已处理；Agent Tech Blog历史时间单独隔离，官方当窗归档可重开；M2.7仓库04/09窗外 |
| SRC-ARXIV | 854个连续ID03232～04934的原始唯一身份全标题查漏，旧90完整题摘重筛、旧排除集42定点完整题摘及非作者反向抽检；v1字段/相邻ID/OAI批次/官方slot交叉核早段区间，精确原文证据在§4 | 已检查 | 不是854项逐摘要或逐全文；46项支持有据当窗推断，43项贡献工作家族因晚字段/后改记录缺更早公开上界而单独隔离，详见§5。Updated不是公开动作，未据其精确秒数定首发 |


## 3. 候选与判断

46个当窗唯一家族按同一贡献门槛评审；公开时间为完全落窗的有据范围，而非原始字段秒级首发。8项新增准入来自对错误泛化拒绝理由的定点重审，日级独立抽检另恢复03647；不按关键词或有ROADMAP owner自动保留。43个日期保留家族在§5，不参与当窗分母或正式评分。最后8项普通写后复核和03647标准审阅/仅报告处置均已完成，最终集合的独立日级验收通过。

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [Knowledge Packs: Zero-Token Knowledge Delivery via KV Cache Injection](https://arxiv.org/html/2604.03270v1) | 2026-04-07T08:00:00+08:00 ～ 2026-04-07T09:00:00+08:00 | 精确prefix KV与独立知识包拼接不等价，零token仍消费状态；2 + 2 + 2 = 6 | 深入完成 | 已有覆盖：INFER-KV-CACHE [Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) |
| [ABTest: Behavior-Driven Testing for AI Coding Agents](https://arxiv.org/html/2604.03362v1) | 2026-04-07T08:00:00+08:00 ～ 2026-04-07T09:00:00+08:00 | 真实bug-pattern×action生成交互fuzzing，并分开检测precision与失败率；2 + 2 + 2 = 6 | 深入完成 | 整合：实际正文已由root独立来源/写后复核通过；PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [AEGIS: Scaling Long-Sequence Homomorphic Encrypted Transformer Inference via Hybrid Parallelism on Multi-GPU Systems](https://arxiv.org/pdf/2604.03425v1) | 2026-04-07T08:00:00+08:00 ～ 2026-04-07T09:00:00+08:00 | 加密ciphertext layout与跨GPU通信计划必须联合编译；2 + 2 + 2 = 6 | 深入完成 | 整合：实际正文已由root独立来源/写后复核通过；INFER-TENSORRT-LLM [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md) |
| [The Tool Illusion: Rethinking Tool Use in Web Agents](https://arxiv.org/html/2604.03465v1) | 2026-04-07T08:00:00+08:00 ～ 2026-04-07T09:00:00+08:00 | 工具封装收益受使用模型能力、界面状态与library上下文税约束；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：AGENT-TOOL-CALLING [Ch78](../../../../books/part-07-agent/78-tool-calling.md) |
| [Unveiling Language Routing Isolation in Multilingual MoE Models for Interpretable Subnetwork Adaptation](https://arxiv.org/html/2604.03592v1) | 2026-04-07T08:00:00+08:00 ～ 2026-04-07T09:00:00+08:00 | 语言routing重叠决定expert更新域，固定router不交支持才保留他语；2 + 1 + 2 = 5 | 深入完成 | 整合：实际正文已由root独立来源/写后复核通过；MODEL-MOE [Ch21](../../../../books/part-02-model/21-moe.md) |
| [Are LLM-Based Retrievers Worth Their Cost? An Empirical Study of Efficiency, Robustness, and Reasoning Overhead](https://arxiv.org/html/2604.03676v1) | 2026-04-07T08:00:00+08:00 ～ 2026-04-07T09:00:00+08:00 | query扩写与轻retriever测量成本分开，relevance不是真值概率；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：AGENT-RAG [Ch76](../../../../books/part-07-agent/76-rag.md) |
| [LightThinker++: From Reasoning Compression to Memory Management](https://arxiv.org/html/2604.03679v1) | 2026-04-07T08:00:00+08:00 ～ 2026-04-07T09:00:00+08:00 | 可逆summary/raw visibility区别不可恢复压缩；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：AGENT-MEMORY [Ch77](../../../../books/part-07-agent/77-memory.md) |
| [Your Agent is More Brittle Than You Think: Uncovering Indirect Injection Vulnerabilities in Agentic LLMs](https://arxiv.org/html/2604.03870v1) | 2026-04-07T08:00:00+08:00 ～ 2026-04-07T09:00:00+08:00 | 间接注入hidden-state sensor位置有受限差异，不获得授权权力；2 + 2 + 2 = 6 | 深入完成 | 已有覆盖：PLATFORM-SECURITY [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [VLA-Forget: Vision-Language-Action Unlearning for Embodied Foundation Models](https://arxiv.org/html/2604.03956v1) | 2026-04-07T08:00:00+08:00 ～ 2026-04-07T09:00:00+08:00 | VLA分阶段遗忘需retain/forget双轴，统计冲突不支持物理安全；2 + 1 + 2 = 5 | 标准完成 | 仅报告：见§4受限理由 |
| [TraceGuard: Structured Multi-Dimensional Monitoring as a Collusion-Resistant Control Protocol](https://arxiv.org/html/2604.03968v1) | 2026-04-07T08:00:00+08:00 ～ 2026-04-07T09:00:00+08:00 | 519 detector实验与20/7分权小实验不得合并；3 + 2 + 2 = 7 | 深入完成 | 整合：PLATFORM-TRACE [Ch69](../../../../books/part-06-ai-infrastructure/69-trace.md) |
| [Causality Laundering: Denial-Feedback Leakage in Tool-Calling LLM Agents](https://arxiv.org/html/2604.04035v1) | 2026-04-07T08:00:00+08:00 ～ 2026-04-07T09:00:00+08:00 | 拒绝反馈邻接启发式有误报与延迟漏报，不是完整因果推断；3 + 2 + 2 = 7 | 深入完成 | 整合：PLATFORM-SECURITY [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [OP-GRPO: Efficient Off-Policy GRPO for Flow-Matching Models](https://arxiv.org/html/2604.04142v1) | 2026-04-07T08:00:00+08:00 ～ 2026-04-07T09:00:00+08:00 | flow低noise比率病态限制off-policy复用到前段；2 + 2 + 2 = 6 | 深入完成 | 整合：实际正文已由root独立来源/写后复核通过；TRAIN-GRPO [Ch33](../../../../books/part-04-training-system/33-grpo.md) |
| [Adaptive Action Chunking at Inference-time for Vision-Language-Action Models](https://arxiv.org/html/2604.04161v1) | 2026-04-07T08:00:00+08:00 ～ 2026-04-07T09:00:00+08:00 | 多proposal熵增量选择action commit horizon，非校准安全风险；2 + 2 + 2 = 6 | 深入完成 | 整合：实际正文已由root独立来源/写后复核通过；MULTIMODAL-EMBODIED-VLA [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) |
| [Rashomon Memory: Towards Argumentation-Driven Retrieval for Multi-Perspective Agent Memory](https://arxiv.org/html/2604.03588v1) | 2026-04-07T08:00:00+08:00 ～ 2026-04-07T09:00:00+08:00 | argument graph保留多观点冲突，但八观察四query不足生产验证；2 + 1 + 2 = 5 | 标准完成 | 仅报告：见§4受限理由 |
| [Representational Collapse in Multi-Agent LLM Committees: Measurement and Diversity-Aware Consensus](https://arxiv.org/html/2604.03809v1) | 2026-04-07T08:00:00+08:00 ～ 2026-04-07T09:00:00+08:00 | embedding多样性不等独立误差，小committee改善与run方差同阶；2 + 1 + 2 = 5 | 标准完成 | 已有覆盖：AGENT-MULTI-AGENT [Ch82](../../../../books/part-07-agent/82-multi-agent.md) |
| [Emergent Inference-Time Semantic Contamination via In-Context Priming](https://arxiv.org/pdf/2604.04043v1) | 2026-04-07T08:00:00+08:00 ～ 2026-04-07T09:00:00+08:00 | 推理时priming也可污染能力，nonsense对照限制只fine-tune有风险的判断；2 + 1 + 2 = 5 | 深入完成 | 已有覆盖：PLATFORM-SECURITY [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [Profile-Then-Reason: Bounded Semantic Complexity for Tool-Augmented Language Agents](https://arxiv.org/html/2604.04131v1) | 2026-04-07T08:00:00+08:00 ～ 2026-04-07T09:00:00+08:00 | profile/guarded workflow有界repair需确定operator，强观察依赖保留ReAct；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：AGENT-WORKFLOW [Ch81](../../../../books/part-07-agent/81-workflow.md) |
| [Self-Execution Simulation Improves Coding Models](https://arxiv.org/html/2604.03253v1) | 2026-04-07T08:00:00+08:00 ～ 2026-04-07T09:00:00+08:00 | learned execution feedback依赖专训，纯scaffold可退步且非执行oracle；2 + 2 + 2 = 6 | 深入完成 | 整合：AGENT-TOOL-CALLING [Ch78](../../../../books/part-07-agent/78-tool-calling.md) |
| [Robust LLM Performance Certification via Constrained Maximum Likelihood Estimation](https://arxiv.org/html/2604.03257v1) | 2026-04-07T08:00:00+08:00 ～ 2026-04-07T09:00:00+08:00 | 人工gold与judge标签共同估failure/TPR/FPR，先验区间有bias代价；2 + 2 + 2 = 6 | 深入完成 | 整合：实际正文已由root独立来源/写后复核通过；PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Emergent Compositional Communication for Latent World Properties](https://arxiv.org/html/2604.03266v1) | 2026-04-07T08:00:00+08:00 ～ 2026-04-07T09:00:00+08:00 | 离散通信重组冻结world features有选择效应，非普遍物理因果；2 + 1 + 2 = 5 | 标准完成 | 仅报告：见§4受限理由 |
| [When Sinks Help or Hurt: Unified Framework for Attention Sink in Large Vision-Language Models](https://arxiv.org/html/2604.03316v1) | 2026-04-07T08:00:00+08:00 ～ 2026-04-07T09:00:00+08:00 | vision sink层间输入改变使干预不可相加，oracle选层不等部署policy；2 + 1 + 2 = 5 | 标准完成 | 仅报告：见§4受限理由 |
| [Learning Additively Compositional Latent Actions for Embodied AI](https://arxiv.org/html/2604.03340v1) | 2026-04-07T08:00:00+08:00 ～ 2026-04-07T09:00:00+08:00 | 局部同scene action可加的latent约束依赖短运动/旋转过滤；2 + 2 + 2 = 6 | 深入完成 | 整合：实际正文已由root独立来源/写后复核通过；MULTIMODAL-EMBODIED-VLA [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) |
| [Olmo Hybrid: From Theory to Practice and Back](https://arxiv.org/html/2604.03444v1) | 2026-04-07T08:00:00+08:00 ～ 2026-04-07T09:00:00+08:00 | hybrid同预算/scaling证据受形状recipe和任务退步限定，少tokens不等wallclock；2 + 2 + 3 = 7 | 深入完成 | 整合：MODEL-LONG-CONTEXT [Ch22](../../../../books/part-02-model/22-long-context.md) |
| [Rethinking Token Prediction: Tree-Structured Diffusion Language Model](https://arxiv.org/html/2604.03537v1) | 2026-04-07T08:00:00+08:00 ～ 2026-04-07T09:00:00+08:00 | 词表树条件head改变显存分配及跨level误差/采样预算；2 + 1 + 2 = 5 | 深入完成 | 整合：实际正文已由root独立来源/写后复核通过；MULTIMODAL-GENERATIVE-PARADIGMS [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [Selective Forgetting for Large Reasoning Models](https://arxiv.org/html/2604.03571v1) | 2026-04-07T08:00:00+08:00 ～ 2026-04-07T09:00:00+08:00 | CoT与答案遗忘分开测，低ROUGE不是参数擦除或不可恢复证明；2 + 2 + 2 = 6 | 深入完成 | 已有覆盖：PLATFORM-SECURITY [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [The Format Tax](https://arxiv.org/html/2604.03616v1) | 2026-04-07T08:00:00+08:00 ～ 2026-04-07T09:00:00+08:00 | 上游格式prompt税和decoder mask分离，freeform再格式化有双调用成本；2 + 2 + 2 = 6 | 深入完成 | 整合：MODEL-SAMPLING [Ch20](../../../../books/part-02-model/20-sampling.md) |
| [VectraFlow: Long-Horizon Semantic Processing over Data and Event Streams with LLMs](https://arxiv.org/html/2604.03855v1) | 2026-04-07T08:00:00+08:00 ～ 2026-04-07T09:00:00+08:00 | 概率typed event抽取与确定性NFA分层，negation必须有限within窗口；2 + 2 + 2 = 6 | 深入完成 | 整合：AGENT-WORKFLOW [Ch81](../../../../books/part-07-agent/81-workflow.md) |
| [From Prompt to Physical Action: Structured Backdoor Attacks on LLM-Mediated Robotic Control Systems](https://arxiv.org/html/2604.03890v1) | 2026-04-07T08:00:00+08:00 ～ 2026-04-07T09:00:00+08:00 | 结构化命令有效不代表physical action授权，verifier延迟和残余攻击需保留；2 + 2 + 2 = 6 | 深入完成 | 已有覆盖：PLATFORM-SECURITY [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [Predict, Don't React: Value-Based Safety Forecasting for LLM Streaming](https://arxiv.org/html/2604.03962v1) | 2026-04-07T08:00:00+08:00 ～ 2026-04-07T09:00:00+08:00 | prefix未来伤害rollout监督区别终局标签复制，预测sensor非authority；2 + 2 + 2 = 6 | 深入完成 | 已有覆盖：PLATFORM-SECURITY [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [DRAFT: Task Decoupled Latent Reasoning for Agent Safety](https://arxiv.org/html/2604.03242v1) | 2026-04-07T08:00:00+08:00 ～ 2026-04-07T09:00:00+08:00 | latent extractor联合原trajectory判安全，稀疏证据不能被显式summary替代；2 + 2 + 2 = 6 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Position: Science of AI Evaluation Requires Item-level Benchmark Data](https://arxiv.org/pdf/2604.03244v1) | 2026-04-07T08:00:00+08:00 ～ 2026-04-07T09:00:00+08:00 | item response矩阵暴露构念/answer-key因子，aggregate总分难定位有效性；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Vocabulary Dropout for Curriculum Diversity in LLM Co-Evolution](https://arxiv.org/html/2604.03472v1) | 2026-04-07T08:00:00+08:00 ～ 2026-04-07T09:00:00+08:00 | 词表硬mask改变课程探索可行域，多样性提升不保证solver收益；2 + 1 + 2 = 5 | 标准完成 | 仅报告：见§4受限理由 |
| [Focus Matters: Phase-Aware Suppression for Hallucination in Vision-Language Models](https://arxiv.org/html/2604.03556v1) | 2026-04-07T08:00:00+08:00 ～ 2026-04-07T09:00:00+08:00 | phase-aware视觉focus改变hallucination operating point，CHAIR好不等全部F1好；2 + 1 + 2 = 5 | 标准完成 | 仅报告：见§4受限理由 |
| [Unlocking Prompt Infilling Capability for Diffusion Language Models](https://arxiv.org/html/2604.03677v1) | 2026-04-07T08:00:00+08:00 ～ 2026-04-07T09:00:00+08:00 | response-only masking限制dLM prompt infilling，架构双向不保证已学能力；2 + 1 + 3 = 6 | 深入完成 | 整合：TRAIN-SFT [Ch29](../../../../books/part-04-training-system/29-sft.md) |
| [Testing the Limits of Truth Directions in LLMs](https://arxiv.org/html/2604.03754v1) | 2026-04-07T08:00:00+08:00 ～ 2026-04-07T09:00:00+08:00 | truth方向跨prompt/layer/task不稳定，probe不拥有自动纠错权；2 + 1 + 3 = 6 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Automated Attention Pattern Discovery at Scale in Large Language Models](https://arxiv.org/html/2604.03764v1) | 2026-04-07T08:00:00+08:00 ～ 2026-04-07T09:00:00+08:00 | attention pattern探测与干预必要/充分分开，大量置零可崩溃；2 + 1 + 2 = 5 | 标准完成 | 已有覆盖：MODEL-SELF-ATTENTION [Ch14](../../../../books/part-02-model/14-self-attention.md) |
| [ACES: Who Tests the Tests? Leave-One-Out AUC Consistency for Code Generation](https://arxiv.org/html/2604.03922v1) | 2026-04-07T08:00:00+08:00 ～ 2026-04-07T09:00:00+08:00 | LOO测试ranking避免自评价但平均better-than-random假设不是自动真值；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [SoLA: Leveraging Soft Activation Sparsity and Low-Rank Decomposition for Large Language Model Compression](https://arxiv.org/html/2604.03258v1) | 2026-04-07T08:00:00+08:00 ～ 2026-04-07T09:00:00+08:00 | 高贡献FFN原通道与其余whitened SVD分工，统一预算rank分配有次优/退步条件；2 + 1 + 2 = 5 | 深入完成 | 整合：INFER-TENSORRT-LLM [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md) |
| [KiToke: Kernel-based Interval-aware Token Compression for Video Large Language Models](https://arxiv.org/html/2604.03414v1) | 2026-04-07T08:00:00+08:00 ～ 2026-04-07T09:00:00+08:00 | inverse-density采样降低重复簇遗漏风险，内容区间限定merge边界且不保证无损；2 + 1 + 2 = 5 | 深入完成 | 整合：MULTIMODAL-REPRESENTATION [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) |
| [Zero-Shot Quantization via Weight-Space Arithmetic](https://arxiv.org/html/2604.03420v1) | 2026-04-07T08:00:00+08:00 ～ 2026-04-07T09:00:00+08:00 | 同坐标donor QAT差分迁移有负迁移，test oracle幅度选择不能冒充部署zero-shot；2 + 1 + 2 = 5 | 深入完成 | 整合：INFER-TENSORRT-LLM [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md) |
| [Fast Cross-Operator Optimization of Attention Dataflow](https://arxiv.org/html/2604.03446v1) | 2026-04-07T08:00:00+08:00 ～ 2026-04-07T09:00:00+08:00 | buffer保留、loop order与recompute共同决定跨算子dataflow，模拟最优非实机保证；2 + 1 + 2 = 5 | 深入完成 | 整合：INFER-TENSORRT-LLM [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md) |
| [Minos: Systematically Classifying Performance and Power Characteristics of GPU Workloads on HPC Clusters](https://arxiv.org/html/2604.03591v1) | 2026-04-07T08:00:00+08:00 ～ 2026-04-07T09:00:00+08:00 | 默认频率profile的两个近邻分别借用power和性能频率曲线，非hard cap或通用SLO；2 + 1 + 2 = 5 | 深入完成 | 整合：PLATFORM-COST [Ch70](../../../../books/part-06-ai-infrastructure/70-cost.md) |
| [DiffSparse: Accelerating Diffusion Transformers with Learned Token Sparsity](https://arxiv.org/html/2604.03674v1) | 2026-04-07T08:00:00+08:00 ～ 2026-04-07T09:00:00+08:00 | learned layer×step成本在全局稀疏预算下离线DP，静态schedule有质量反例；2 + 1 + 2 = 5 | 深入完成 | 整合：INFER-TENSORRT-LLM [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md) |
| [Diagonal-Tiled Mixed-Precision Attention for Efficient Low-Bit MXFP Inference](https://arxiv.org/html/2604.03950v1) | 2026-04-07T08:00:00+08:00 ～ 2026-04-07T09:00:00+08:00 | 近远序列tile使用不同MXFP精度，双packing开销与远距检索退步须联合验收；2 + 1 + 2 = 5 | 深入完成 | 整合：INFER-TENSORRT-LLM [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md) |
| [RUQuant: Towards Refining Uniform Quantization for Large Language Models](https://arxiv.org/html/2604.04013v1) | 2026-04-07T08:00:00+08:00 ～ 2026-04-07T09:00:00+08:00 | uniform midpoint失配对应centroid，分布变换与可选output-loss校准分开核算；2 + 1 + 2 = 5 | 深入完成 | 整合：INFER-TENSORRT-LLM [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md) |
| [Stabilizing Unsupervised Self-Evolution of MLLMs via Continuous Softened Retracing reSampling](https://arxiv.org/html/2604.03647v1) | 2026-04-07T08:00:00+08:00 ～ 2026-04-07T09:00:00+08:00 | 局部重采样改变proposal，频率ratio连续reward不拥有真值；2 + 1 + 2 = 5 | 标准完成 | 仅报告：有新分支，同预算归因与baseline口径仍不足稳定采用 |

## 4. 证据与知识整合

采用作者exact-v1的必要方法、评测与关键反证；未运行作者代码或复现实验。评分是贡献工作判断，不是置信概率；缺失硬件/precision/length/batch/concurrency/SLO不补造。新增段落均在现有论证内，期望收益不代替真实生产验收。

### [Knowledge Packs: Zero-Token Knowledge Delivery via KV Cache Injection](https://arxiv.org/html/2604.03270v1)

Source Family：`SF-2026-ARXIV-2604-03270`；本次采用exact-v1；自身早字段、邻界/连续ID、OAI批次及官方slot支持上述当窗区间推断，不把提交日或Updated秒数当首发。[原文](https://arxiv.org/html/2604.03270v1) §2–5、limitations。Exact-prefix KV 等价要求 checkpoint、canonical chat template、position 与 causal prefix 相同；把两份独立前缀缓存直接拼接不等价，既有 RoPE 位置也不能只靠旋转修复缺失的 conditioning。作者实际 bank routing 是 top fact 文本重新 prefill：4 MB/5K facts 主要存 text+embedding，不是预生成 KV 容量；“zero token”不免除 attention 的 context、内存或位置约束。Qwen3/Llama3.1-8B、FP16、A100-80GB、700 HotpotQA 同前缀实验支持缓存等价，100 样本 accumulation 与15 coding tasks steering 不支持一般事实或能力保证。Ch45 已有 prefix/checkpoint/template/position identity 和失败回退，该缓存身份与回退命题已有覆盖；value steering 仅保留受限实验，不扩写成“知识包可替代上下文”。拟2+2+2=6，深入完成（纠正宣传口径）。

当前处置：已有覆盖，具体正文对照见本日记录；owner `INFER-KV-CACHE`，[Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)。详细证据与未决差异见[本日审阅记录](../_sources/daily-20260407/v3-reopen-notes.md)。

### [ABTest: Behavior-Driven Testing for AI Coding Agents](https://arxiv.org/html/2604.03362v1)

Source Family：`SF-2026-ARXIV-2604-03362`；本次采用exact-v1；自身早字段、邻界/连续ID、OAI批次及官方slot支持上述当窗区间推断，不把提交日或Updated秒数当首发。[原文](https://arxiv.org/html/2604.03362v1) §3–5。400 bug reports 归为47 interaction patterns×128 action types，兼容组合647tests；固定 repo workspace 执行后用JSON/artifact checks标记，再人工确认。Claude/Codex/Gemini五配置共3235次单次运行，1573flags中642人工确认，40.8%为检测precision，不是Agent错误率；§3.5过滤不完整run，因此已分析flags不能推所有执行的failure prevalence；368 minor failures 也不是严重安全事故。Ch66 outcome witness 已区分判定链，但从已知 bug pattern×action 生成交互测试且将检测 precision 单独验收是具体增量。拟2+2+2=6，本次拟采用命题已深入审阅，root必要源与写后独立复核通过。

当前处置：整合，实际正文已由root独立来源/写后复核通过；owner `PLATFORM-EVALUATION-SYSTEM`，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)。详细证据与未决差异见[本日审阅记录](../_sources/daily-20260407/v3-reopen-notes.md)。


实际落笔位置： Ch66 Agent Regression中的历史bug-pattern×action构造与检测precision分账。 证据限制写入正文与Review notes；root非作者已通过必要源与实际正文复核，未复现实验，整日Gate仍须单独验收。

### [AEGIS: Scaling Long-Sequence Homomorphic Encrypted Transformer Inference via Hybrid Parallelism on Multi-GPU Systems](https://arxiv.org/pdf/2604.03425v1)

Source Family：`SF-2026-ARXIV-2604-03425`；本次采用exact-v1；自身早字段、邻界/连续ID、OAI批次及官方slot支持上述当窗区间推断，不把提交日或Updated秒数当首发。[原文](https://arxiv.org/html/2604.03425v1) §4–5。按modulus-chain dependency优先、token coherence其次的placement层级安排ciphertext layout，并联合RNS slice reduction/operator reorder隐藏comm；PyTorch FX compiler生成加密执行计划。BERT-Base/SST-2而非LLM decode，128-bit CKKS、N=2^16、slots=2^15、Q=35/P=4/boot14；2×A6000-48GB NVLink与4×A100-40GB，后者2048输入端到端仍约5036s。GPU移植Cinnamon/Hydra排除原ASIC/ISA/interconnect特性，不能当完整硬件同预算比较。Ch72已有FHE隐私分支，潜在增量是加密layout与通信执行计划共同编译，不是FHE总体实用性结论。拟2+2+2=6，本次拟采用命题已深入审阅，root必要源与写后独立复核通过。

当前处置：整合，实际正文已由root独立来源/写后复核通过；owner `INFER-TENSORRT-LLM`，[Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md)。详细证据与未决差异见[本日审阅记录](../_sources/daily-20260407/v3-reopen-notes.md)。


实际落笔位置： Ch49 kernel生成前的密文layout/parallel axes/通信共同编译；Ch72威胁模型handoff。 证据限制写入正文与Review notes；root非作者已通过必要源与实际正文复核，未复现实验，整日Gate仍须单独验收。

### [The Tool Illusion: Rethinking Tool Use in Web Agents](https://arxiv.org/html/2604.03465v1)

Source Family：`SF-2026-ARXIV-2604-03465`；本次采用exact-v1；自身早字段、邻界/连续ID、OAI批次及官方slot支持上述当窗区间推断，不把提交日或Updated秒数当首发。[原文](https://arxiv.org/html/2604.03465v1) §3–4。WALT、SkillWeaver、Hybrid-Agent与五backbone、两webbench对照，tool synthesis的模型/使用者能力差、UI-state-dependent control和library retrieval/inspection开销决定收益；多工具不等于更广任务覆盖。任务与站点范围受限；不是禁止Tools或证明工具无效。已对读Ch78的接口粒度、组合selector、工具发现及执行分权正文：封装并不消除UI-state控制和使用者reasoning，library inspection成本随颗粒度进入总预算。2+2+2=6标准完成，采用该条件边界已有覆盖；本论文受限web排名不改为工具无效的结论。

当前处置：已有覆盖，具体正文对照见本日记录；owner `AGENT-TOOL-CALLING`，[Ch78](../../../../books/part-07-agent/78-tool-calling.md)。详细证据与未决差异见[本日审阅记录](../_sources/daily-20260407/v3-reopen-notes.md)。

### [Unveiling Language Routing Isolation in Multilingual MoE Models for Interpretable Subnetwork Adaptation](https://arxiv.org/html/2604.03592v1)

Source Family：`SF-2026-ARXIV-2604-03592`；本次采用exact-v1；自身早字段、邻界/连续ID、OAI批次及官方slot支持上述当窗区间推断，不把提交日或Updated秒数当首发。[原文](https://arxiv.org/html/2604.03592v1) §3–5、Appendix C。同类任务的经验激活频次及specificity ratio、共享CV与绝对频次决定浅/中/深expert选择；target语言exclusive浅/深与中层共享不同，冻结未选expert与router。Qwen3-30B-A3B/Phi-3.5-MoE、single H200、BF16、3epochs、batch2×acc8、lr2e-5；128/6144和16/512只减少gradient/optimizer state，不消除全部resident weights/activations。Appendix C exact preservation要求固定router且routing支持集不相交，不是现实所有语言无干扰定理。Table3 Phi Bengali46.89低于TopK49.51，target gains不证明总优；Table5 pruning也使多种其他语言大幅下降，不能照抄“causally language-exclusive”。Ch21现有capacity/routing主线未明确参数更新域应随层级language overlap校准，拟2+1+2=5；需据这些反证收窄整合命题。

当前处置：整合，实际正文已由root独立来源/写后复核通过；owner `MODEL-MOE`，[Ch21](../../../../books/part-02-model/21-moe.md)。详细证据与未决差异见[本日审阅记录](../_sources/daily-20260407/v3-reopen-notes.md)。


实际落笔位置： Ch21可部署模块之后的routing overlap与post-training参数更新域。 证据限制写入正文与Review notes；root非作者已通过必要源与实际正文复核，未复现实验，整日Gate仍须单独验收。

### [Are LLM-Based Retrievers Worth Their Cost? An Empirical Study of Efficiency, Robustness, and Reasoning Overhead](https://arxiv.org/html/2604.03676v1)

Source Family：`SF-2026-ARXIV-2604-03676`；本次采用exact-v1；自身早字段、邻界/连续ID、OAI批次及官方slot支持上述当窗区间推断，不把提交日或Updated秒数当首发。[原文](https://arxiv.org/html/2604.03676v1) §3.5、§5–6。BRIGHT12tasks/14retrievers，4×H100-80GB、FP16、CUDA12.4/Torch2.8/Transformers4.57、median3runs。文档embedding缓存时query测量不含index build或生成reasoning query成本，因此轻encoder长query附加推理近零不能称整个augmentation免费。长文保留/short chunking改变语料与证据覆盖，不能只归因encoder参数；数学/代码query全五扩写源退步。BM25 fusion可伤强retriever、DAT退步；top1score预测gold in top-k AUROC仅.508–.611为discrimination，不是概率校准。Ch76的query-dialect、packing/coverage、score≠truth及hybrid实际正文已对读，具体已有覆盖；2+2+2=6、标准完成。

当前处置：已有覆盖，具体正文对照见本日记录；owner `AGENT-RAG`，[Ch76](../../../../books/part-07-agent/76-rag.md)。详细证据与未决差异见[本日审阅记录](../_sources/daily-20260407/v3-reopen-notes.md)。

### [LightThinker++: From Reasoning Compression to Memory Management](https://arxiv.org/html/2604.03679v1)

Source Family：`SF-2026-ARXIV-2604-03679`；本次采用exact-v1；自身早字段、邻界/连续ID、OAI批次及官方slot支持上述当窗区间推断，不把提交日或Updated秒数当首发。[原文](https://arxiv.org/html/2604.03679v1) §3–4、Appendix C。Commit形成summary/raw关联，Expand/Fold控制visibility，不把raw永久丢弃；无Expand/Fold消融与同dataset训练对照支持可逆控制的局部分支。Qwen3-30B-A3B-Thinking、8GPU/3epochs；Vanilla6625trajectories与3677分解为42633instances的数据不等预算，lr/batch/max sequence也不同，不能把全部性能差归因memory mechanism。Timing总concurrency32，但TokenSkip按batch32而其他按question-level32，比较依赖serving实现。Ch77“从不可逆Summary到可切换Raw/Summary Visibility”正文已直接承载相同论点与backtracking/thrashing/provenance边界；已有覆盖 `AGENT-MEMORY`，拟2+2+2=6，标准完成。

当前处置：已有覆盖，具体正文对照见本日记录；owner `AGENT-MEMORY`，[Ch77](../../../../books/part-07-agent/77-memory.md)。详细证据与未决差异见[本日审阅记录](../_sources/daily-20260407/v3-reopen-notes.md)。

### [Your Agent is More Brittle Than You Think: Uncovering Indirect Injection Vulnerabilities in Agentic LLMs](https://arxiv.org/html/2604.03870v1)

Source Family：`SF-2026-ARXIV-2604-03870`；本次采用exact-v1；自身早字段、邻界/连续ID、OAI批次及官方slot支持上述当窗区间推断，不把提交日或Updated秒数当首发。[原文](https://arxiv.org/html/2604.03870v1) §3.1–3.3、Table1/3/4。AgentDojo Banking改造为16tasks×9objectives×4IPI=576scenarios，九open backbones；统计behavior/entropy部分只在hijacked failures上，不是所有请求分布。RepE从baseline aligned/hijacked paired traces取hidden state，按格式筛选后80/20train/test并选layer；tool-input位置通常强于function-call，但Llama cosine例外。高AUC/TPR@FPR5%没有adaptive攻击、不同suite或真正production阻断保证。Ch72已有learned sensor与deterministic action authorization分权，本结果为该既有分支的局部位置/阈值证据；拟2+2+2=6，安全深入完成，倾向已有覆盖，不把“robust circuit breaker”升级为安全证明。

当前处置：已有覆盖，具体正文对照见本日记录；owner `PLATFORM-SECURITY`，[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)。详细证据与未决差异见[本日审阅记录](../_sources/daily-20260407/v3-reopen-notes.md)。

### [VLA-Forget: Vision-Language-Action Unlearning for Embodied Foundation Models](https://arxiv.org/html/2604.03956v1)

Source Family：`SF-2026-ARXIV-2604-03956`；本次采用exact-v1；自身早字段、邻界/连续ID、OAI批次及官方slot支持上述当窗区间推断，不把提交日或Updated秒数当首发。[原文](https://arxiv.org/html/2604.03956v1) §3–4、Table4、Appendix B/D。Forget/retain gradients和ratio选择vision/projector/upper action-backbone层，依次LoRA编辑并用PCGrad避免目标冲突；近邻boundary set只降低浅遗忘，不构成erasure。OpenVLA-7B/pi0fast、OXE/PushT、BF16或FP16、rank16；GA可更强forget却伤utility，去retain term亦伤TSR。正文5seeds与Appendix“final should3seeds”、4000instances与5000/1200/1200、FC定义CE与表中指标口径未完整对齐；hardware只写single modern GPU，不能复述宣传百分比为确定受控结论。保留机制为approximate分阶段编辑，但尚不足新增physical safety结论；Ch72已有多substrate probe/retain-utility边界。拟2+1+2=5，标准完成，仅报告且列证据限制，不把这些统计冲突变成普通待审。

当前处置：仅报告，保留局部证据/反证而不提高为长期采用保证；owner `PLATFORM-SECURITY`，[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)。详细证据与未决差异见[本日审阅记录](../_sources/daily-20260407/v3-reopen-notes.md)。

### [TraceGuard: Structured Multi-Dimensional Monitoring as a Collusion-Resistant Control Protocol](https://arxiv.org/html/2604.03968v1)

Source Family：`SF-2026-ARXIV-2604-03968`；本次采用exact-v1；自身早字段、邻界/连续ID、OAI批次及官方slot支持上述当窗区间推断，不把提交日或Updated秒数当首发。[原文](https://arxiv.org/html/2604.03968v1) §3–5、Table2/5、limitations。五维每步独立LLM calls+七stateful heuristics+intent analyzer，trajectory换ID清状态；independent calls不证明独立误差。BashArena/ClaudeSonnet4/GPT4.1-mini，519样本的bash_heuristic在threshold.3 safety82.1%/usefulness69.2%、.5为70.8%/93.9%。Table5分权100%只对应earlier run阈值.3 n=20、.5 86% n=7，不能与519合并。5或6API calls、手调weights、nonadaptive attack。Ch69正文及Review notes已分别纠正519组合detector实验与earlier run分权20/7小样本，作者已核实际修订；3+2+2=7深入完成，不用小样本结果支持一般抗合谋保证。

当前处置：整合已实际写入并由日报作者写后核验；owner `PLATFORM-TRACE`，[Ch69](../../../../books/part-06-ai-infrastructure/69-trace.md)。详细证据与未决差异见[本日审阅记录](../_sources/daily-20260407/v3-reopen-notes.md)。

### [Causality Laundering: Denial-Feedback Leakage in Tool-Calling LLM Agents](https://arxiv.org/html/2604.04035v1)

Source Family：`SF-2026-ARXIV-2604-04035`；本次采用exact-v1；自身早字段、邻界/连续ID、OAI批次及官方slot支持上述当窗区间推断，不把提交日或Updated秒数当首发。[原文](https://arxiv.org/html/2604.04035v1) §2.5/3.7/7/9.2–3。拒绝结果本身可泄露秘密，但所谓Counterfactual edge仅denied action→下一tool call的时间邻接heuristic，既误拒紧邻良性动作又漏延迟chain，不是perfect causal inference。Min-reachable trust依赖真实field provenance/ingestion labels，不能自授declassification。三人工攻击场景只比较flat citation与graph其余policy layers固定，没有frontier LLM benchmark；AppleM4Pro48GB、warmup后median100次、session数十tools/数百nodes的<1ms不外推长histories。Ch72既有Deny-disclosure段已明确counterfactual edge只是邻接启发式、包含良性FP及延迟chain FN，并限定三手工场景与M4Pro median实验；3+2+2=7纠错深入完成，作者已核实际正文及边界。

当前处置：整合已实际写入并由日报作者写后核验；owner `PLATFORM-SECURITY`，[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)。详细证据与未决差异见[本日审阅记录](../_sources/daily-20260407/v3-reopen-notes.md)。

### [OP-GRPO: Efficient Off-Policy GRPO for Flow-Matching Models](https://arxiv.org/html/2604.04142v1)

Source Family：`SF-2026-ARXIV-2604-04142`；本次采用exact-v1；自身早字段、邻界/连续ID、OAI批次及官方slot支持上述当窗区间推断，不把提交日或Updated秒数当首发。[原文](https://arxiv.org/html/2604.04142v1) §4–5、ablation。每condition至多一个最高reward且衰减老样本，mixed group用G−1fresh+1buffer；保留current/old per-step clip，用old/off的sequence correction另外加权，避免clip错误参照旧buffer policy。低noise方差趋零使importance ratios病态，off-policy只复用前段、末段当前policy重生成。Reward筛选及group相对优势意味着实验稳定不等于unbiased，较高buffer比例也发散。SD3.5-M/Wan2.1-1.4B、EvalGen/text规则/PickScore及unseen quality metrics；“34.2%steps”不等于同wall-clock/质量普遍无损，GPU/precision等未见完整声明。Ch33 off-policy ratio主线需对读其flow-matching低noise分支；拟2+2+2=6，采用深入核验，待具体Books裁决。

当前处置：整合，实际正文已由root独立来源/写后复核通过；owner `TRAIN-GRPO`，[Ch33](../../../../books/part-04-training-system/33-grpo.md)。详细证据与未决差异见[本日审阅记录](../_sources/daily-20260407/v3-reopen-notes.md)。


实际落笔位置： Ch33 Staleness objective actuator之后的低噪声阶段replay admission。 证据限制写入正文与Review notes；root非作者已通过必要源与实际正文复核，未复现实验，整日Gate仍须单独验收。

### [Adaptive Action Chunking at Inference-time for Vision-Language-Action Models](https://arxiv.org/html/2604.04161v1)

Source Family：`SF-2026-ARXIV-2604-04161`；本次采用exact-v1；自身早字段、邻界/连续ID、OAI批次及官方slot支持上述当窗区间推断，不把提交日或Updated秒数当首发。[原文](https://arxiv.org/html/2604.04161v1) §4、§5.1.2/5.1.5/5.2。N并行samples估continuous covariance entropy+gripper discrete entropy，Eq5取平均entropy的最大增量点并设下限ξ，不是校准风险分数。GR00TN1.5、冻结Eagle2/projector仅训diffusion-head，8×A800mixed precision；LIBERO40tasks各50rollouts/RoboCasa100rollouts，实机Realman+Mycobot两个RGB视角、50demos/任务、20trials/任务、600steps上限。GR00T N1.5/LIBERO/single A800样本1/20/40推理83/106/157ms（推理precision/实时控制SLO：Not Disclosed），Table4 success随samples非严格单调，不能沿正文称continuously提高。下限避免jerky mode跳变，却扩大open-loop；样本entropy可能错过共同偏差，不是安全guarantee。Ch26固定chunk/observation freshness可补统计proposal决定commit horizon的条件分支；拟2+2+2=6，本次拟采用命题已深入审阅，root必要源与写后独立复核通过。

当前处置：整合，实际正文已由root独立来源/写后复核通过；owner `MULTIMODAL-EMBODIED-VLA`，[Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)。详细证据与未决差异见[本日审阅记录](../_sources/daily-20260407/v3-reopen-notes.md)。


实际落笔位置： Ch26 Action Chunk时间契约后的多proposal entropy/horizon分支。 证据限制写入正文与Review notes；root非作者已通过必要源与实际正文复核，未复现实验，整日Gate仍须单独验收。

### [Rashomon Memory: Towards Argumentation-Driven Retrieval for Multi-Perspective Agent Memory](https://arxiv.org/html/2604.03588v1)

Source Family：`SF-2026-ARXIV-2604-03588`；本次采用exact-v1；自身早字段、邻界/连续ID、OAI批次及官方slot支持上述当窗区间推断，不把提交日或Updated秒数当首发。§2–4/ObservationsAndLimitations：各观点拥有OWL/RDF子图，query-dependent Dung attack graph可选择、组合或显式保留冲突，不强迫制造统一真值。ClaudeSonnet4.6 temperature0、三perspectives/八observations/四queries，37次encoding calls/query最多7次；无RAG/raw-memory定量baseline，attack质量依赖prompt，未测规模或interactive latency。标准完成5分；仅保留受限proof-of-concept，不把四query视为新的可靠memory采用契约。

当前处置：仅报告，保留局部证据/反证而不提高为长期采用保证；owner `AGENT-MEMORY`，[Ch77](../../../../books/part-07-agent/77-memory.md)。详细证据与未决差异见[本日审阅记录](../_sources/daily-20260407/v3-reopen-notes.md)。

### [Representational Collapse in Multi-Agent LLM Committees: Measurement and Diversity-Aware Consensus](https://arxiv.org/html/2604.03809v1)

Source Family：`SF-2026-ARXIV-2604-03809`；本次采用exact-v1；自身早字段、邻界/连续ID、OAI批次及官方slot支持上述当窗区间推断，不把提交日或Updated秒数当首发。已对读Ch82“Verification与Aggregation”“同根报告可以帮助读懂证据，却不能按独立观察累加”。Embedding正交未消同root误差，n100小差/一到三run不足新几何置信保证。2+1+2=5标准完成，已有覆盖AGENT-MULTI-AGENT。

当前处置：已有覆盖，具体正文对照见本日记录；owner `AGENT-MULTI-AGENT`，[Ch82](../../../../books/part-07-agent/82-multi-agent.md)。详细证据与未决差异见[本日审阅记录](../_sources/daily-20260407/v3-reopen-notes.md)。

### [Emergent Inference-Time Semantic Contamination via In-Context Priming](https://arxiv.org/pdf/2604.04043v1)

Source Family：`SF-2026-ARXIV-2604-04043`；本次采用exact-v1；自身早字段、邻界/连续ID、OAI批次及官方slot支持上述当窗区间推断，不把提交日或Updated秒数当首发。[PDF](https://arxiv.org/pdf/2604.04043v1) pp1–5。HTMLv1封面August24与PDFv1April7不符，采用PDF精确v1。三Claude snapshot、temperature.5、10primingconditions×100trials，随机五数字order后dinnerparty20figures；customregex+手工semantic类别的darkhits，不是广义harm or jailbreakrate。Nonsenseformatcontrol支持内容/格式两因素可能，但smallmodel缺representation和capabilitygated仅作者推测，无内部probe/模型同预算因果对照；Opus比Sonnet幅度弱，不能写能力越强必更不安全。2+1+2=5，安全深入完成。已对读Ch72“Prompt Injection与Tool Boundary”“Instruction Hierarchy必须携带Authenticated Provenance”和“Context Reconstruction不能提升Principal Authority”：风险发生在推理时共享上下文及示例重建，而非只有参数更新后才出现；内容/格式标签不建立隔离，effect authority仍属于独立executor。该长期边界已有覆盖；本论文dark-hits类别、Claude快照及可能的scaling解释仅留日报，不提高为新普遍因果。

当前处置：已有覆盖，具体正文对照见本日记录；owner `PLATFORM-SECURITY`，[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)。详细证据与未决差异见[本日审阅记录](../_sources/daily-20260407/v3-reopen-notes.md)。

### [Profile-Then-Reason: Bounded Semantic Complexity for Tool-Augmented Language Agents](https://arxiv.org/html/2604.04131v1)

Source Family：`SF-2026-ARXIV-2604-04131`；本次采用exact-v1；自身早字段、邻界/连续ID、OAI批次及官方slot支持上述当窗区间推断，不把提交日或Updated秒数当首发。[原文](https://arxiv.org/html/2604.04131v1) §2.2、Proposition2.2、§3。LLM先profile有限workflow、deterministicroute/execution/verifier，最多一次repair，再末端reason；“确定性”明示每operator deterministic前提，不证明semanticplan正确。四backbones×六benchmark共24pair，PTR16胜，但HotpotQA四model均输react，高observationdependence仍react；meanlatency/APIprice不构成tailSLO，需冻结providerrevision。2+2+2=6标准完成。已对读Ch81的typed workflow、deterministic executor、bounded repair与动态planning回退：operator确定性只保证执行语义，不自动保证plan正确，强observation依赖任务仍需动态决策。本例已有覆盖，不因formal notation另写同一架构。

当前处置：已有覆盖，具体正文对照见本日记录；owner `AGENT-WORKFLOW`，[Ch81](../../../../books/part-07-agent/81-workflow.md)。详细证据与未决差异见[本日审阅记录](../_sources/daily-20260407/v3-reopen-notes.md)。

### [Self-Execution Simulation Improves Coding Models](https://arxiv.org/html/2604.03253v1)

Source Family：`SF-2026-ARXIV-2604-03253`；本次采用exact-v1；自身早字段、邻界/连续ID、OAI批次及官方slot支持上述当窗区间推断，不把提交日或Updated秒数当首发。§6.2–6.4/Table3–6与§8已补。普通Qwen3-32B/CWM仅在推理时套self-RLEF scaffold，多项pass指标下降；联合训练后的改善不能归因于多轮模板本身。DMC公测初错修对17.0%、初对改错1.2%，私测分别10.4%/5.0%，模拟执行的可见测试与隐测正确性并不相同。Oracle real execution仍较强；大整数/复杂运算和单文件竞赛题边界，不证明repository执行等价。2+2+2=6标准完成，需把learned simulator限定为有误差的反馈sensor，不获得真实执行oracle的权威。

当前处置：整合，真实正文与root非作者来源/写后复核已通过；owner `AGENT-TOOL-CALLING`，[Ch78](../../../../books/part-07-agent/78-tool-calling.md)。详细证据与未决差异见[本日审阅记录](../_sources/daily-20260407/v3-reopen-notes.md)。

### [Robust LLM Performance Certification via Constrained Maximum Likelihood Estimation](https://arxiv.org/html/2604.03257v1)

Source Family：`SF-2026-ARXIV-2604-03257`；本次采用exact-v1；自身早字段、邻界/连续ID、OAI批次及官方slot支持上述当窗区间推断，不把提交日或Updated秒数当首发。[原文](https://arxiv.org/html/2604.03257v1) §3–5、约束实现说明。少量人工gold与大量noisy judge标签联合估计failure rate、TPR/FPR；CMLE用先验区间换低方差但区间误指定有bias风险，UMLE不要求这些anchor。实测Jigsaw nM50/nJ10000、Qwen2.5-.5classifier/Llama3.1-8judge，transfer仅同model in-domain HateSpeech锚点.948/.063与目标.939/.053；全数据reference约束不是实际零成本oracle，未测任意域外安全。Projected gradient固定200steps/lr1e−6与启动labelbudget需计入。拟2+2+2=6标准完成；Ch66 judge校准已承认gold anchor与分布漂移，CMLE区间借方差与偏差的具体分支待实际owner对读，不声称无偏普适保证。

当前处置：整合，实际正文已由root独立来源/写后复核通过；owner `PLATFORM-EVALUATION-SYSTEM`，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)。详细证据与未决差异见[本日审阅记录](../_sources/daily-20260407/v3-reopen-notes.md)。


实际落笔位置： Ch66 PPI之后的prior interval约束judge-noise MLE。 证据限制写入正文与Review notes；root非作者已通过必要源与实际正文复核，未复现实验，整日Gate仍须单独验收。

### [Emergent Compositional Communication for Latent World Properties](https://arxiv.org/html/2604.03266v1)

Source Family：`SF-2026-ARXIV-2604-03266`；本次采用exact-v1；自身早字段、邻界/连续ID、OAI批次及官方slot支持上述当窗区间推断，不把提交日或Updated秒数当首发。[原文](https://arxiv.org/html/2604.03266v1) 方法/实验。冻结DINOv2/VJEPA2、2×5符号Gumbelmessage，80seed中54%按后验PosDis>.4分为compositional；这不是预注册普遍概率。最好code93.8/新训练92.2/holistic87.5含选择效应，CIFAR未见27%vschance20/rawNN50、真实Physics101/CoPhy外推条件不同。通信重组冻结feature，不证明新perception或普遍causal representation。2+1+2=5标准完成，仅报告受限世界模型机制例证，尚不足改长期设计。

当前处置：仅报告，保留局部证据/反证而不提高为长期采用保证；owner `MULTIMODAL-WORLD-MODELS`，[Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)。详细证据与未决差异见[本日审阅记录](../_sources/daily-20260407/v3-reopen-notes.md)。

### [When Sinks Help or Hurt: Unified Framework for Attention Sink in Large Vision-Language Models](https://arxiv.org/html/2604.03316v1)

Source Family：`SF-2026-ARXIV-2604-03316`；本次采用exact-v1；自身早字段、邻界/连续ID、OAI批次及官方slot支持上述当窗区间推断，不把提交日或Updated秒数当首发。§4–5.3/Table1–2已补。Learnedgate并无oracletasklabels，32layers独立训练，greedystacking后的收益小于各层之和，前序gate改变后序输入分布；增加L19会降、再增L6改善，不能写可独立相加。2+1+2=5标准完成，受限局部门控例证仅报告，未建立超出Ch23 encoder/fusion与Ch14 attention诊断的长期新采用规则。

当前处置：仅报告，保留局部证据/反证而不提高为长期采用保证；owner `MULTIMODAL-REPRESENTATION`，[Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)。详细证据与未决差异见[本日审阅记录](../_sources/daily-20260407/v3-reopen-notes.md)。

### [Learning Additively Compositional Latent Actions for Embodied AI](https://arxiv.org/html/2604.03340v1)

Source Family：`SF-2026-ARXIV-2604-03340`；本次采用exact-v1；自身早字段、邻界/连续ID、OAI批次及官方slot支持上述当窗区间推断，不把提交日或Updated秒数当首发。§4.1–4.4及A.2已補读Implementation/PolicySetup/Results/DesignFactors/Findings。过滤较大robotrotation以使same-scene短时间加法近似合理；共同Villa-X/PaliGemma3B/15Ksteps/batch512、50%ID+50%Bridge，不是大模型全局actiongroup定律。PreVQ运动量校准较好而additivity较弱，IDM无stopgrad崩溃/错误位置explode，FDM更稳；新loss收益有simulation与realrobot对照但不证明所有motion闭环。2+2+2=6标准完成，是否在Ch26补局部compositional representation分支由具体正文差异裁决。

当前处置：整合，实际正文已由root独立来源/写后复核通过；owner `MULTIMODAL-EMBODIED-VLA`，[Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)。详细证据与未决差异见[本日审阅记录](../_sources/daily-20260407/v3-reopen-notes.md)。


实际落笔位置： Ch26 action-facing interface之后的短scene加性约束，默认FDM与IDM sg对照分开。 证据限制写入正文与Review notes；root非作者已通过必要源与实际正文复核，未复现实验，整日Gate仍须单独验收。

### [Olmo Hybrid: From Theory to Practice and Back](https://arxiv.org/html/2604.03444v1)

Source Family：`SF-2026-ARXIV-2604-03444`；本次采用exact-v1；自身早字段、邻界/连续ID、OAI批次及官方slot支持上述当窗区间推断，不把提交日或Updated秒数当首发。重开 [exact-v1](https://arxiv.org/html/2604.03444v1) §2–5、Table 1–2 和消融。与 Olmo 3 的 7B/6T 预训练对照把 75% sliding-window attention 换为可有负特征值的 GDN、保留 3:1 交错 attention；形状为了相近参数/吞吐调整，不能称所有变量完全相同。较少训练 tokens 达到同 loss/MMLU 不等于 wall-clock 加速，Code/GenQA 及部分 held-out 项退步，DPO 也非全面收益。理论 state-based recall 比较依赖计算复杂度假设；不能将训练收益完全归因于该定理。Ch22 已有 GDN 的写入/擦除与全局 attention 互补，本次真正增量是受控 scaling 与表达性/任务退步的条件化证据，而非再写一段“hybrid更好”。2+2+3=7，深入完成；Ch22 GDN机制后已加入状态先更新/后读历史、固定预算与target-token两侧验收、任务退步/recipe及wall-clock边界，并由日报作者对读原文核验。

当前处置：整合已实际写入并由日报作者写后核验；owner `MODEL-LONG-CONTEXT`，[Ch22](../../../../books/part-02-model/22-long-context.md)。详细证据与未决差异见[本日审阅记录](../_sources/daily-20260407/v3-reopen-notes.md)。

### [Rethinking Token Prediction: Tree-Structured Diffusion Language Model](https://arxiv.org/html/2604.03537v1)

Source Family：`SF-2026-ARXIV-2604-03537`；本次采用exact-v1；自身早字段、邻界/连续ID、OAI批次及官方slot支持上述当窗区间推断，不把提交日或Updated秒数当首发。重开 [exact-v1](https://arxiv.org/html/2604.03537v1) §3–4、Table 1–2 与 level-weight 消融。词表递归 K-means 等深叶子树把 flat head 改成 parent-conditioned child prediction，forward 到祖先、reverse 向 children，跨层 ELBO 分解不等于直接沿用 hierarchical softmax 的训练目标。OWT、序列512不packing、131B训练tokens，small/base head减少后重配更深attention层；4×24GB RTX3090约束下比较显存/吞吐。small PPL不及HDLM，base略好；binary深树的coarse-level ELBO更大，强行增加高层权重反而退步，512采样steps均分两层胜过过量给粗层。未证明大型语言模型、长上下文或实际服务SLO收益。Ch24现有masked/层级diffusion解释需对照是否缺少“预测空间分解→head资源重配→层间误差/采样预算”的机制分支。拟2+1+2=5；标准审阅完成，本次拟采用命题已深入审阅，root必要源与写后独立复核通过。

当前处置：整合，实际正文已由root独立来源/写后复核通过；owner `MULTIMODAL-GENERATIVE-PARADIGMS`，[Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)。详细证据与未决差异见[本日审阅记录](../_sources/daily-20260407/v3-reopen-notes.md)。


实际落笔位置： Ch24 Masked前的树上条件预测、分层ELBO与资源预算分支。 证据限制写入正文与Review notes；root非作者已通过必要源与实际正文复核，未复现实验，整日Gate仍须单独验收。

### [Selective Forgetting for Large Reasoning Models](https://arxiv.org/html/2604.03571v1)

Source Family：`SF-2026-ARXIV-2604-03571`；本次采用exact-v1；自身早字段、邻界/连续ID、OAI批次及官方slot支持上述当窗区间推断，不把提交日或Updated秒数当首发。§4.2和消融已补。TOFU4K与19.7K医学隐私样本、Llama3.2-1B/Nemotron8B；reasoning与finalanswer分别对重训模型计算ROUGE差距，不能由低ROUGE推断知识已经从参数擦除。3%forget子集CoT替代可缩小重训差距，遗忘gradient过强则retain效用下降，retain-gradient缓解；未证明对抗恢复、所有推理路径或可组合隐私保证。2+2+2=6安全深入完成。采用范围仅输出行为与retain/forget双轴，不把作者“低分说明不知道”写入Books。

当前处置：已有覆盖，具体正文对照见本日记录；owner `PLATFORM-SECURITY`，[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)。详细证据与未决差异见[本日审阅记录](../_sources/daily-20260407/v3-reopen-notes.md)。

### [The Format Tax](https://arxiv.org/html/2604.03616v1)

Source Family：`SF-2026-ARXIV-2604-03616`；本次采用exact-v1；自身早字段、邻界/连续ID、OAI批次及官方slot支持上述当窗区间推断，不把提交日或Updated秒数当首发。重开 [exact-v1](https://arxiv.org/html/2604.03616v1) §3–7、Table 5 与 Appendix评测声明。完整prompt/few-shot/task/GCD factorial；6 open3B–32B模型、4API、MATH500/GPQA198/ZebraLogic500/WritingBench500、JSON/XML/Markdown/LaTeX。同prompt比较GCD，72 cells中显著39、prompt-alone36、GCD15；不是39/72都来自GCD。两轮先freeform再reformat降低损失但增加调用、latency与约双tokens；thinking在部分任务退步，WritingBench不成立。MATH依赖gpt-5.4-nano等价judge，writing依赖gpt-5.2，不是人工绝对真值。只测呈现格式，作者明确禁止外推编码正确性约束的tool arguments/code/test generation。Ch20“Logit penalties与约束的边界”内部已补“格式损失要先定位在Prompt，还是Decoder”，分开上游条件分布变化与mask干预、格式合规与内容正确，并保留两调用成本/模型任务例外及单调用共存；Ch78只handoff。2+2+2=6，深入完成。日报作者已写后核验；root非作者独立重开Table1/§4.2–4.3/Table5/AppD/E及相邻Ch20，批准本项实际Integrate；未复现实验，不代表整日Gate已通过。

当前处置：整合，root独立来源/写后复核已通过；owner `MODEL-SAMPLING`，[Ch20](../../../../books/part-02-model/20-sampling.md)。详细证据与未决差异见[本日审阅记录](../_sources/daily-20260407/v3-reopen-notes.md)。

### [VectraFlow: Long-Horizon Semantic Processing over Data and Event Streams with LLMs](https://arxiv.org/html/2604.03855v1)

Source Family：`SF-2026-ARXIV-2604-03855`；本次采用exact-v1；自身早字段、邻界/连续ID、OAI批次及官方slot支持上述当窗区间推断，不把提交日或Updated秒数当首发。[原文](https://arxiv.org/html/2604.03855v1) §3–5、limitations。LLM生成typed/timestamped events，entity key下NFA维护Take/Ignore/Proceed；共享rule编译、隔离instance state，skip-till-any-match，否定要求within且窗尾才接受。256 clinical notes/5patterns、GPT-4o-mini与Qwen3-8/4B；full-context baseline GPT F1=.675、14.6M tokens，semantic-pattern retrieval约3.1M、F1=.848/.862/.822。这是语义抽取与确定性时序分工的机制证据，不是医学方法；未披露一般stream lateness/watermark、生产latency或抽取真值保证。Ch81已有temporal verifier，但否定有限窗与probabilistic extraction隔离为具体分支。拟2+2+2=6，标准完成，采用则深入核验。

当前处置：整合，真实正文与root非作者来源/写后复核已通过；owner `AGENT-WORKFLOW`，[Ch81](../../../../books/part-07-agent/81-workflow.md)。详细证据与未决差异见[本日审阅记录](../_sources/daily-20260407/v3-reopen-notes.md)。

### [From Prompt to Physical Action: Structured Backdoor Attacks on LLM-Mediated Robotic Control Systems](https://arxiv.org/html/2604.03890v1)

Source Family：`SF-2026-ARXIV-2604-03890`；本次采用exact-v1；自身早字段、邻界/连续ID、OAI批次及官方slot支持上述当窗区间推断，不把提交日或Updated秒数当首发。[原文](https://arxiv.org/html/2604.03890v1) III-A–D/IV-A–D。ROS2 JSON→cmd_vel的执行桥，poisoned LoRA把触发词绑定最终结构化命令，区别仅污染自然语言reasoning且后续JSON转换未传播。四7–9B受害模型、Llama3-8B verifier，Turtlesim与Yahboom实车；平均ASR约83%→20%但不是零，DeepSeek微调后latency波动被排除，不能把剩下稳定模型延迟称全模型结果。GPU/precision/seed及逐模型样本量=`Not Disclosed`。安全深入完成2+2+2=6；已对读Ch72“Prompt Injection与Tool Boundary”和“VLA威胁模型必须延伸到物理反馈”，明确typed schema→policy/authorization→真实执行是不同责任，verifier不代controller safety或物理effect receipt。该长期边界已有覆盖；仅保留ROS/Turtlesim/一类实车的局部反例，不推广全部VLA。

当前处置：已有覆盖，具体正文对照见本日记录；owner `PLATFORM-SECURITY`，[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)。详细证据与未决差异见[本日审阅记录](../_sources/daily-20260407/v3-reopen-notes.md)。

### [Predict, Don't React: Value-Based Safety Forecasting for LLM Streaming](https://arxiv.org/html/2604.03962v1)

Source Family：`SF-2026-ARXIV-2604-03962`；本次采用exact-v1；自身早字段、邻界/连续ID、OAI批次及官方slot支持上述当窗区间推断，不把提交日或Updated秒数当首发。重开 [exact-v1](https://arxiv.org/html/2604.03962v1) §2–5、Table 3–5、Appendix E。监督目标是给定prompt/prefix、proposal continuation分布下终局伤害judge的期望，不把unsafe-final标签粗贴所有前缀；MC rollout与linear head形成预测式sensor。Llama1/3/8B并迁移Gemma/Qwen tokenizer，3seeds；on-time定义at/before unsafe sentence end，response_loc全unsafe令precision100%，不能读成通用零误报。max reduction更早阻断却FPR更高，mean作平衡。H100、HF StaticCache、1024-token prefix后1024步、100runs；70B两卡，2.4–9.5ms仅steady-state配对，不是多租户端到端保证。guard score受generator/judge/rollout覆盖限制，不是事实正确率或安全authority，外部authorization/buffer/commit gate仍需保留。Ch72已有streaming sentence-commit；本次可能增量是“检测已越界→预测future harm”的监督/误阻断分支。拟2+2+2=6，安全采用命题深入完成；等待根任务实际Books判定。

当前处置：已有覆盖，具体正文对照见下述说明；owner `PLATFORM-SECURITY`，[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)。详细证据与未决差异见[本日审阅记录](../_sources/daily-20260407/v3-reopen-notes.md)。


具体已有覆盖： Ch66 Counterfactual Localization已有固定prefix下continuation重采样的条件风险；Ch72 Streaming Guard完整Sentence已有buffer/fence/abort authority。学习式head仅risk sensor，不需要重复新增授权机制。

### [DRAFT: Task Decoupled Latent Reasoning for Agent Safety](https://arxiv.org/html/2604.03242v1)

Source Family：`SF-2026-ARXIV-2604-03242`；本次采用exact-v1；自身早字段、邻界/连续ID、OAI批次及官方slot支持上述当窗区间推断，不把提交日或Updated秒数当首发。§4.1–4.2/§5/Limitations/E.4：QwenGuard4B/Qwen4/8B/Llama3.1-8B四backbones、synthetic AuraGen及LLM/human标注ASSE/RJudge。Extractor输出latent仍加原trajectory供Reasoner，16尾tokens与移除模块有对照；ExplicitReasoning的GPT5.2模型/成本不齐，不能单归latent。tSNE可分不证明attention稀释因果，漏检跨步骤hijack/destination/不可逆writes、误检正常security词；未验证实际权限、ratelimit、多租户/层级控制，seed数量不完整披露。安全深入完成6分，latent监测不获得可读解释或授权权力；具体采用或已有覆盖已完成，见下述处置。

当前处置：已有覆盖，具体正文对照见下述说明；owner `PLATFORM-EVALUATION-SYSTEM`，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)。详细证据与未决差异见[本日审阅记录](../_sources/daily-20260407/v3-reopen-notes.md)。


具体已有覆盖： Ch66 Raw Score→Claim Sensor/Failure Direction已经承载内部sensor、标签/校准与原始证据/独立authority。tail-query extractor是受限实现，不证明faithful latent或改变最终授权。

### [Position: Science of AI Evaluation Requires Item-level Benchmark Data](https://arxiv.org/pdf/2604.03244v1)

Source Family：`SF-2026-ARXIV-2604-03244`；本次采用exact-v1；自身早字段、邻界/连续ID、OAI批次及官方slot支持上述当窗区间推断，不把提交日或Updated秒数当首发。[PDF v1](https://arxiv.org/pdf/2604.03244v1) pp4–7/§5.1–5.2/§6与HTML定点交叉。旧10M/155K库存字段不用；PDF v1§6为225Kitems、64bench、8Mresponses，与HTML相同，不能把这项误称为HTML污染。66旧模型×567MMLU items与72新模型×1000Pro items的CTT difficulty依赖被测模型样本，不能跨组直接比较；BabiQA三个factor簇由answer-key解释，提示测到了作答偏好而非单一deduction。GLRM的MMLU-Pro四因子由GPT5初标再人工修订，外部相关仅描述性、非定论或因果能力本体。2+2+2=6标准完成，Ch66内部构念/生态噪声正文已对读，不以公开数据量自动写Books。

当前处置：已有覆盖，具体正文对照见下述说明；owner `PLATFORM-EVALUATION-SYSTEM`，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)。详细证据与未决差异见[本日审阅记录](../_sources/daily-20260407/v3-reopen-notes.md)。


具体已有覆盖： Ch66 Benchmark相关性分解共同构念与生态噪声已分开shared factor、task-specific variance与metadata effects，不把描述因子当因果能力；本篇为已有构念诊断的受限证据。

### [Vocabulary Dropout for Curriculum Diversity in LLM Co-Evolution](https://arxiv.org/html/2604.03472v1)

Source Family：`SF-2026-ARXIV-2604-03472`；本次采用exact-v1；自身早字段、邻界/连续ID、OAI批次及官方slot支持上述当窗区间推断，不把提交日或Updated秒数当首发。§5.1/6.1/Ablations/B.3已补。2H200/verl/vLLM、baseQwen3-4/8B、五iteration、三seed；85%/75%词表retain不能反写成drop率。最终checkpoint固定避免bestposthoc；4B75%多样性上升却solver36.5<38.3、85%39.3改善，capacitymatched8B收益较好，crossscale和instruct失效。Mask是allowed_token_ids可行域约束，不是单纯entropyreward。2+1+2=5标准完成；Ch33已有“探索增加不保证可学课程”的主线，对读硬mask新分支是否值得采用。

当前处置：仅报告，保留局部证据/反证而不提高为长期采用保证；owner `TRAIN-GRPO`，[Ch33](../../../../books/part-04-training-system/33-grpo.md)。详细证据与未决差异见[本日审阅记录](../_sources/daily-20260407/v3-reopen-notes.md)。

### [Focus Matters: Phase-Aware Suppression for Hallucination in Vision-Language Models](https://arxiv.org/html/2604.03556v1)

Source Family：`SF-2026-ARXIV-2604-03556`；本次采用exact-v1；自身早字段、邻界/连续ID、OAI批次及官方slot支持上述当窗区间推断，不把提交日或Updated秒数当首发。§5Models/Baselines/DPPconfiguration/Quantitative/InferenceEfficiency与D.4已补。Architecture-specific mask60/35/65/40%，greedyencoderfocusintervention可降CHAIR但Qwen/InternVL POPE及F1部分下降；平均attention不是truth，选取DPP/硬mask保CLS。相对PGD AUE开销减少但GPU/并发/SLO未披露，不沿“negligible”写无成本。2+1+2=5标准完成，仅报告受限hallucination operatingpoint与互补decoder方法，不推广所有visualtokens或越过事实验证。

当前处置：仅报告，保留局部证据/反证而不提高为长期采用保证；owner `MULTIMODAL-REPRESENTATION`，[Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)。详细证据与未决差异见[本日审阅记录](../_sources/daily-20260407/v3-reopen-notes.md)。

### [Unlocking Prompt Infilling Capability for Diffusion Language Models](https://arxiv.org/html/2604.03677v1)

Source Family：`SF-2026-ARXIV-2604-03677`；本次采用exact-v1；自身早字段、邻界/连续ID、OAI批次及官方slot支持上述当窗区间推断，不把提交日或Updated秒数当首发。[原文](https://arxiv.org/html/2604.03677v1) §2–5。SFT只maskresponse会训练出prompt不宜被反向infilling的条件偏差；fullsequence随机mask prompt+response、全maskedtokenloss，后接response-only细化为条件分支。Fewshot已知response反推prompt，多候选用fewshot验收后固定复用，不是test逐题用gold泄漏。LLaDA/Dream、SummEval/GSM8K；本文§3.3叙述64.8而Table1 publicLLaDA prepend69.8且不同case含义不能合并；FS+RO不同template/receiver未全面更优，§4.2叙述数值与表亦有不一致，不照录宣传。Bidirectional结构不能独立保证SFT后可用能力。拟2+1+3=6标准完成；mask support决定可执行generation direction已在Ch29正文细化并通过独立采用复核。

当前处置：整合，真实正文与root非作者来源/写后复核已通过；owner `TRAIN-SFT`，[Ch29](../../../../books/part-04-training-system/29-sft.md)。详细证据与未决差异见[本日审阅记录](../_sources/daily-20260407/v3-reopen-notes.md)。

### [Testing the Limits of Truth Directions in LLMs](https://arxiv.org/html/2604.03754v1)

Source Family：`SF-2026-ARXIV-2604-03754`；本次采用exact-v1；自身早字段、邻界/连续ID、OAI批次及官方slot支持上述当窗区间推断，不把提交日或Updated秒数当首发。已对读Ch66“可解码Failure Direction不拥有自动纠错权”和activationoracle/taskcalibration段；probe含预测信息不代表干预解耦、需targetmodel/task×prompt×layer/slice校准和行为回归，本例不提供独立部署truthauthority。2+1+3=6标准完成，已有覆盖PLATFORM-EVALUATION-SYSTEM。

当前处置：已有覆盖，具体正文对照见本日记录；owner `PLATFORM-EVALUATION-SYSTEM`，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)。详细证据与未决差异见[本日审阅记录](../_sources/daily-20260407/v3-reopen-notes.md)。

### [Automated Attention Pattern Discovery at Scale in Large Language Models](https://arxiv.org/html/2604.03764v1)

Source Family：`SF-2026-ARXIV-2604-03764`；本次采用exact-v1；自身早字段、邻界/连续ID、OAI批次及官方slot支持上述当窗区间推断，不把提交日或Updated秒数当首发。已实际对读Ch14“可解码不等于单点拥有因果控制权”的probe→single/multiposition→causaltracing/端到端回退。本项2+1+2=5标准完成，pattern/knockout是受限诊断证据，既有正文已覆盖读出/必要/充分/多点控制的层级，不为新任务复制一套因果owner。本项已有覆盖MODEL-SELF-ATTENTION。

当前处置：已有覆盖，具体正文对照见本日记录；owner `MODEL-SELF-ATTENTION`，[Ch14](../../../../books/part-02-model/14-self-attention.md)。详细证据与未决差异见[本日审阅记录](../_sources/daily-20260407/v3-reopen-notes.md)。

### [ACES: Who Tests the Tests? Leave-One-Out AUC Consistency for Code Generation](https://arxiv.org/html/2604.03922v1)

Source Family：`SF-2026-ARXIV-2604-03922`；本次采用exact-v1；自身早字段、邻界/连续ID、OAI批次及官方slot支持上述当窗区间推断，不把提交日或Updated秒数当首发。§4.2–4.3及Assumption4再次核原文。仅passmatrix主表HumanEval收益不能略过MBPPPass5仍低directinference；Hard区全部方法≤1/14，average-test质量假设在真实部署未知，不能用LOO消除所有相关错误。标准完成2+2+2=6；独立testing truth与ranking owner需分离。LOO-AUC的受限估计不改变既有独立test authority与consensus相关错边界，具体对照见下述处置。

当前处置：已有覆盖，具体正文对照见下述说明；owner `PLATFORM-EVALUATION-SYSTEM`，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)。详细证据与未决差异见[本日审阅记录](../_sources/daily-20260407/v3-reopen-notes.md)。


具体已有覆盖： Ch66 相关采样压低Selection上限与独立task tests/heldout验收已分开候选相关错、selector和正确性authority；LOO estimator不是测试真值，better-than-random假设不自动成立。

### [SoLA: Leveraging Soft Activation Sparsity and Low-Rank Decomposition for Large Language Model Compression](https://arxiv.org/html/2604.03258v1)

Source Family：`SF-2026-ARXIV-2604-03258`；exact-v1，自身早字段/连续ID/OAI与官方slot支持有据当窗区间，不把Updated当公开动作。

[exact-v1](https://arxiv.org/html/2604.03258v1)，Method、Table4、Prime Neurons 消融和 Inference Efficiency。非零 SiLU 不支持把低幅度通道直接硬剪；保留高贡献 FFN 通道，剩余块用 activation-whitened SVD，并在同内存预算下按保留奇异值能量选择各矩阵 rank。rank 取16倍数；整数问题由贪心得到次优解，不是全局最优。Table4 的 Llama2-13B/20% 配置 PPL 从uniform6.18到adaptive6.52，说明自适应并非每个指标必胜；Prime比例与校准样本仍是recipe。质量覆盖Llama2-7/13/70B、Mistral7B、WikiText2/zero-shot常识/5-shotMMLU；效率只是RTX4090上序列2048对应矩阵操作、10^3次中位数，不是端到端Serving、concurrency或SLO，precision未在该段披露。评分拟 **2+1+2=5**，标准必要证据完成；Ch54“减少Bytes”只是压缩类别，Ch49“双稀疏/量化不自动加速”也未解释高贡献原块与剩余低秩的分工及统一预算rank分配。实际采用 **INFER-TENSORRT-LLM / Ch49** 压缩执行分支，独立必要源/写后核验已通过；

当前处置：整合；owner `INFER-TENSORRT-LLM`，[Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md)。真实正文已落笔，root已独立重开必要原文并核对章内位置/边界；其中KiToke inverse-density与DiffSparse稀疏预算措辞按反馈纠正并自查。未复现实验。

### [KiToke: Kernel-based Interval-aware Token Compression for Video Large Language Models](https://arxiv.org/html/2604.03414v1)

Source Family：`SF-2026-ARXIV-2604-03414`；exact-v1，自身早字段/连续ID/OAI与官方slot支持有据当窗区间，不把Updated当公开动作。

[exact-v1](https://arxiv.org/html/2604.03414v1) §3.2–3.4、§4.1、Tables4–6、AppendixB.1。仅按逆kernel密度逐token top-k保留可能排除低得分但有意义的重复簇，加权/pivotal采样降低整簇遗漏风险但不保证覆盖；帧差分的绝对量/局部对比/相对比例定内容区间，只在区间内merge，非重新发明merge。Table5含10seeds/CIs，Table6区间与weighted merge联合消融支持各自贡献；阈值用100视频/分位和轻量搜索，不能称无需校准。LLaVA-OneVision32帧6272tokens、LLaVA-Video64帧及Qwen3VL至128帧，四video任务/A100；Table4压缩13.1ms+LLM53.1ms=66.2ms而非只报后者，10%保留均分58.2vs59.1，1%进一步退步。precision/batch/concurrency/SLO未披露；信息不可逆、稀有瞬时证据仍有风险。拟 **2+1+2=5** 标准证据完成。Ch23“固定预算先分信息责任”“Temporal aliasing”已有事件覆盖/分阶段裁剪，却未区分全局冗余选择与禁止跨内容区间合并这两层控制；实际采用 **MULTIMODAL-REPRESENTATION / Ch23** 对应段内窄分支，而非添加论文列表。

当前处置：整合；owner `MULTIMODAL-REPRESENTATION`，[Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)。真实正文已落笔，root已独立重开必要原文并核对章内位置/边界；其中KiToke inverse-density与DiffSparse稀疏预算措辞按反馈纠正并自查。未复现实验。

### [Zero-Shot Quantization via Weight-Space Arithmetic](https://arxiv.org/html/2604.03420v1)

Source Family：`SF-2026-ARXIV-2604-03420`；exact-v1，自身早字段/连续ID/OAI与官方slot支持有据当窗区间，不把Updated当公开动作。

[exact-v1](https://arxiv.org/html/2604.03420v1) §4–7。同架构、同pretrained初始化的 donor普通微调/QAT差分，乘lambda加到receiver后再做3bit per-channel对称weight-only模拟PTQ；bias/norm/patch/head保持高精度，无rotation/smoothing。lambda=1有负迁移；§6.2 receiver test-set oracle sweep只展示经验上界，不能说部署已zero-shot选好幅度或“方向普适”；现实held-out calibration是作者建议，仍待验证。范围ViT任务，未证明LLM/kernel加速、硬件、batch/concurrency/SLO。精确v1题摘已经纠正旧库存后发摘要污染。拟 **2+1+2=5** 标准证据完成；Ch49“Post-quantization Recovery”是token动态补偿、“Anchor Artifact”是同anchor派生格式，均不覆盖跨任务donor差分的坐标兼容、负迁移与oracle幅度依赖。实际采用 **INFER-TENSORRT-LLM / Ch49** 静态量化artifact恢复的实验性替代分支，不外推ViT结果为LLM/kernel加速。

当前处置：整合；owner `INFER-TENSORRT-LLM`，[Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md)。真实正文已落笔，root已独立重开必要原文并核对章内位置/边界；其中KiToke inverse-density与DiffSparse稀疏预算措辞按反馈纠正并自查。未复现实验。

### [Fast Cross-Operator Optimization of Attention Dataflow](https://arxiv.org/html/2604.03446v1)

Source Family：`SF-2026-ARXIV-2604-03446`；exact-v1，自身早字段/连续ID/OAI与官方slot支持有据当窗区间，不把Updated当公开动作。

[exact-v1](https://arxiv.org/html/2604.03446v1) §III–VI、VII-A–E。跨算子保留tile只有与计算顺序/loop boundary匹配才消DRAM重读；softmax前的partial sum不可任意跨传播。Pseudo nested-loop共同表达tiling、compute order、buffer层级和recompute，离线symbolic domination pruning再用query矩阵枚举。所谓最优限于§V声明模型与枚举空间：能耗假设计算量不随映射变化，latency取compute/DRAM瓶颈；不保证真实accelerator全局最优。1410 Timeloop对照为intra-operator模型核验，不等于fusion实机验证。两个NVDLA/TPU-like模拟配置（4 arrays、1/4MB、60/128GB/s、1GHz、28nm能耗表），BERT512–16K/GPT3-13B/PaLM62B training/prefill；无生产decode/batch/concurrency/SLO。TileFlow其order/buffer搜索预固化、runtime仅MCTS tiling；Chimera为TileFlow重现，不能写所有baseline同成本独立实现。Pareto稀疏、recompute对PaLM有利而BERT/GPT未明显同益；buffer可容纳全部矩阵时差异消失。拟 **2+1+2=5** 标准证据完成。Ch49“Layout Plan跨算子/单独验Cost Model”已分solver与估价，“联合Tensor Lifetime”已说fusion，但未解释**buffer保留与compute ordering必须共同选**及recompute作为同空间条件分支；已在该论证内落实最小增量，数字不入Books，单篇独立采用通过。

当前处置：整合；owner `INFER-TENSORRT-LLM`，[Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md)。真实正文已落笔，root已独立重开必要原文并核对章内位置/边界；其中KiToke inverse-density与DiffSparse稀疏预算措辞按反馈纠正并自查。未复现实验。

### [Minos: Systematically Classifying Performance and Power Characteristics of GPU Workloads on HPC Clusters](https://arxiv.org/html/2604.03591v1)

Source Family：`SF-2026-ARXIV-2604-03591`；exact-v1，自身早字段/连续ID/OAI与官方slot支持有据当窗区间，不把Updated当公开动作。

[exact-v1](https://arxiv.org/html/2604.03591v1) §4.1–4.3、§5.1–5.3、§7.1/7.4/8。两个近邻分别消费power/TDP分布和kernel-duration-weighted SM/DRAM特征，默认频率只profile一次新负载，再借reference的frequency-scaling曲线；offline簇是解释层，runtime只需近邻，不混称cluster直接拥有决策。功率目标可选择p90，性能目标单独约束允许退化，QwenMoE的两个近邻不同。MI300X8卡节点192GB、1300–2100MHz cap实测；A100 PCIe40GB节点只有utilization研究，因无权限未做相同cap，不能宣称跨厂商控制验证。energy delta/1–2ms+EMA来自噪声取舍，边界idle截去，不等于整机账；Llama2/3 vLLM batch1/8/32，训练torchtune32/64，QwenMoE case batch32。Qwen功率预测约5%超目标，是反例而非hard bound；PerfCentric两例守5%不证明线上tailSLO。§8明确跨vendor计数器不等价，phase/input/model漂移不能自动借同近邻。拟 **2+1+2=5** 标准证据完成；Ch70“执行中闲置/Deep Idle”和“组件/阶段Power Budget”没有双profile-neighbor借频率曲线机制，已在后者内窄补，profile identity/失败回退是平台采用推论而非作者已保证。日期有据推断可恢复，单篇独立采用通过。

当前处置：整合；owner `PLATFORM-COST`，[Ch70](../../../../books/part-06-ai-infrastructure/70-cost.md)。真实正文已落笔，root已独立重开必要原文并核对章内位置/边界；其中KiToke inverse-density与DiffSparse稀疏预算措辞按反馈纠正并自查。未复现实验。

### [DiffSparse: Accelerating Diffusion Transformers with Learned Token Sparsity](https://arxiv.org/html/2604.03674v1)

Source Family：`SF-2026-ARXIV-2604-03674`；exact-v1，自身早字段/连续ID/OAI与官方slot支持有据当窗区间，不把Updated当公开动作。

[exact-v1](https://arxiv.org/html/2604.03674v1) §3.2、§4.1–4.3、AppendixA.4–A.6。learned layer×step×candidate-rate成本矩阵经DP分配全局sparsity，token-ranking为可替换组件；STE+teacher/student LPIPS蒸馏更新成本模型，两阶段先保full-step warm start再合step/layer成本重新分配。DP约30秒是离线且训练4–10小时，推理使用预计算配置，不是实时动态求解器；最优针对预测成本与离散空间，不是质量全局最优。PixArtα20step/FLUXschnell4/DiT-XL2-50及Wan1.3B，10K COCO/WebVid captions/类别条件、无GT图像训练，作者报8 MI250“80GB”不额外证明硬件规格；COCO30K、ImageNet50K、VBench950prompt/4750video/256²/2秒8fps。Wan§4.1为25steps而结果Table3为20，需按各自口径，不合成统一服务claim；DiT FID2.26→2.81退步。两阶段比单阶段受测FID较好，更细候选0.125反而较差；512²迁移是受限模型实验，训练token memory仍贵。precision/batch/concurrency/SLO未披露。拟 **2+1+2=5** 标准证据完成。Ch49已有静态template/cache误差guard与runtime chunk调度，但不含**训练期全局误差/稀疏预算分配→静态部署artifact**和取消固定full-step的learned条件分支；已在“Execution Plan联合Tensor Lifetime”原diffusion段内窄补，不增加通用SLO保证。

当前处置：整合；owner `INFER-TENSORRT-LLM`，[Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md)。真实正文已落笔，root已独立重开必要原文并核对章内位置/边界；其中KiToke inverse-density与DiffSparse稀疏预算措辞按反馈纠正并自查。未复现实验。

### [Diagonal-Tiled Mixed-Precision Attention for Efficient Low-Bit MXFP Inference](https://arxiv.org/html/2604.03950v1)

Source Family：`SF-2026-ARXIV-2604-03950`；exact-v1，自身早字段/连续ID/OAI与官方slot支持有据当窗区间，不把Updated当公开动作。

[exact-v1](https://arxiv.org/html/2604.03950v1) §4–6、Algorithm1/Table3及tile消融。causal tile的近对角QK用MXFP8、远处MXFP4，V保FP16；融合双份量化、编码、packing和scale转换以避免预处理吃掉kernel节省。OnlineSoftmax复用并不使量化attention精确等价；对角窗是近邻敏感性代理，远距离检索可失败。单B200/Triton，Llama3.1-8B/3.2-3B、LongBench2.5K–30K，与PyTorchBF16 SDPA比较；Table3 passage_retrieval_en在3B为80→37，平均升分不能盖住任务退步。batch/concurrency/生产SLO未披露，不能把kernel吞吐称全服务收益。拟 **2+1+2=5** 标准证据完成；Ch49“FlashAttention”及“量化前诊断分布”分别覆盖IO/tile与channel变换，未覆盖sequence tile近远精度分区及双格式预处理融合成本。实际采用 **INFER-TENSORRT-LLM / Ch49** 在attention执行主线的窄分支，保留远距检索退步与dense回退。

当前处置：整合；owner `INFER-TENSORRT-LLM`，[Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md)。真实正文已落笔，root已独立重开必要原文并核对章内位置/边界；其中KiToke inverse-density与DiffSparse稀疏预算措辞按反馈纠正并自查。未复现实验。

### [RUQuant: Towards Refining Uniform Quantization for Large Language Models](https://arxiv.org/html/2604.04013v1)

Source Family：`SF-2026-ARXIV-2604-04013`；exact-v1，自身早字段/连续ID/OAI与官方slot支持有据当窗区间，不把Updated当公开动作。

[exact-v1](https://arxiv.org/html/2604.04013v1) §3–5、Eq13、Tables4–6。uniform bin的centroid条件不等于只控制outlier最大值；block Householder/Givens先调整激活分布，再可选学习global reflection以最小化Transformer block output discrepancy。§5.2区分不优化reflection参数的RUQuant与较慢的+fine-tune，不能把“约一分钟”归于两阶段梯度训练。Llama1 7–30B、Llama2 7/13B、Llama3 8B；WikiText2校准128×2048、C4/WikiText2/5任务、W4A4/W6A6、softmax未量化、L20校准；Table4的LH仅微小收益且有部署代价，Table6是3090、prefill2048、batch1/4/16的layer-wise时间，不是完整服务/SLO。拟 **2+1+2=5** 标准证据完成；Ch49“量化前先诊断分布/Rotation Scope”已有group与变换次数，却没有uniform midpoint失配的centroid解释及output-loss校准这条条件分支。实际采用 **INFER-TENSORRT-LLM / Ch49** Numeric Plan内最小增量，保持普通rotation共存。

当前处置：整合；owner `INFER-TENSORRT-LLM`，[Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md)。真实正文已落笔，root已独立重开必要原文并核对章内位置/边界；其中KiToke inverse-density与DiffSparse稀疏预算措辞按反馈纠正并自查。未复现实验。

### [Stabilizing Unsupervised Self-Evolution of MLLMs via Continuous Softened Retracing reSampling](https://arxiv.org/html/2604.03647v1)

Source Family：`SF-2026-ARXIV-2604-03647`；exact-v1；自身v1 Updated=2026-04-07T00:25:30Z联合连续ID/邻界、OAI批次及官方slot支持本日08:00～09:00有据推断，Updated不是首次公开动作。apr03日级反向抽检恢复该家族，原“单类几何+成熟组合”拒绝过宽。

[原文](https://arxiv.org/html/2604.03647v1) §3.2.2 Eq6–8/§4、Tables1–4、AppA.2.4–A.6：8条母轨迹固定在长度的.7处截断，每条续采5条；新增40条是条件proposal，不是独立全局采样。合集答案频率作为base reward，再用局部续采频率/base频率的ratio经tanh有界调整。它是局部稳定性proxy，不是正确性oracle；固定位置未证明就是semantic pivot，错误prefix可稳定产出同一错误，视觉扰动依赖语义不变假设。理论contrast-factor比较是在理想分布/reward-gap模型下，不证明实际clipped神经GRPO收敛到真值。

Qwen2.5-VL7BInstruct、Geometry3K/GeoQA/MMR1训练及四视觉数学benchmark，8×A80080GB、veRL/vLLM、15epoch、batch256、prompt/response上限1024/1536、PPOmini64/micro8，precision、生产concurrency/SLO及seed不确定性未披露。Table3/4采样数/截断率非单调；Table5有SFR/RRM/VSP组件对照，但MajorityVote行恰与Table1未训练base相同、不同于Table1 MM-UPT，不能合并baseline或宣称同总采样预算的因果收益。评分 **2+1+2=5**，标准完成、Experimental、未复现实验。

当前处置：仅报告。Ch33“Verifier Error可能在组内相关”“Exploration必须与Verified Progress对齐”已有共同偏差/proxy真值边界，但没有完整承载此新连续reward/proposal分支，故不伪称已有覆盖；当前同预算归因和MajorityVote/MM-UPT口径不足以采用为稳定设计选择。root已认可这个具体处置，不需为增加书稿自动升级审阅。后续同预算/明确baseline勘误可定点重开Books判断。

## 5. 缺口与下一步

以下43个日期项与8个来源缺口均为本窗终态保留项，不用于正面证据、Books采用或无遗漏断言；定点重开条件为相应官方公开上界/历史目录/明示时区恢复，具体身份与必要材料逐项见下表及§2。本窗普通可执行待办为0。

43个贡献工作家族的日期上界目前不能完全落窗。晚Updated可能是入库/元数据更改而非首次公开，故不机械移到次日，也不据早段批界自动恢复；需要具体家族截点前的官方公开记录/归档，取得后只重开相应归属与Books决定。现有证据/评分工作稿保留于[本日记录](../_sources/daily-20260407/v3-reopen-notes.md)和[原报告留存](../_sources/daily-20260407/v2.1-report-before-v3.md)，不是本窗采用或未审完的借口。

| 家族 / 精确材料 | 原始v1 Updated字段（不是首发） | 保留的工作证据 / 重开条件 |
| --- | --- | --- |
| [PRAISE: Prefix-Based Rollout Reuse in Agentic Search Training](https://arxiv.org/html/2604.03675v1) | 2026-05-08T01:09:23Z | 复用prefix回答密化search credit，但共享evaluator会漂移；必要证据已审，不支持当前日期采用。需该家族截点前官方公开上界，届时只重开归属/Books决定 |
| [ClawArena: Benchmarking AI Agents in Evolving Information Environments](https://arxiv.org/html/2604.04202v1) | 2026-04-07T01:00:41Z | 动态信息groundtruth与belief revision须拆评，框架/模型subset不可横比；必要证据已审，不支持当前日期采用。需该家族截点前官方公开上界，届时只重开归属/Books决定 |
| [Three Phases of Expert Routing: How Load Balance Evolves During Mixture-of-Experts Training](https://arxiv.org/html/2604.04230v1) | 2026-04-07T01:02:12Z | MFG诊断路由负载相变受softmax/congestion假设，不能直接决定训练；必要证据已审，不支持当前日期采用。需该家族截点前官方公开上界，届时只重开归属/Books决定 |
| [Combee: Scaling Prompt Learning for Self-Improving Language Model Agents](https://arxiv.org/html/2604.04247v1) | 2026-04-07T01:03:11Z | 并行prompt经验reduce不满足代数结合律，需context version与bounded fan-in；必要证据已审，不支持当前日期采用。需该家族截点前官方公开上界，届时只重开归属/Books决定 |
| [3D-Stacked NMP, LLM Decoding, Systolic Array Microarchitecture, Multi-Core Scheduling](https://arxiv.org/html/2604.04253v1) | 2026-04-07T01:03:22Z | near-memory形状与buffer成本共同决定placement，模拟不是已造芯片；必要证据已审，不支持当前日期采用。需该家族截点前官方公开上界，届时只重开归属/Books决定 |
| [APPA: Adaptive Preference Pluralistic Alignment for Fair Federated RLHF of LLMs](https://arxiv.org/html/2604.04261v1) | 2026-04-07T01:03:42Z | 本地冻结偏好reward vectors由中央policy更新，非联邦参数平均；必要证据已审，不支持当前日期采用。需该家族截点前官方公开上界，届时只重开归属/Books决定 |
| [How Well Do Agentic Skills Work in the Wild: Benchmarking LLM Skill Usage in Realistic Settings](https://arxiv.org/html/2604.04323v1) | 2026-04-07T01:07:03Z | Skill载入、选择、检索、适配须分别测，非curated可低于无Skill；必要证据已审，不支持当前日期采用。需该家族截点前官方公开上界，届时只重开归属/Books决定 |
| [GENSERVE: Efficient Co-Serving of Heterogeneous Diffusion Model Workloads](https://arxiv.org/html/2604.04335v1) | 2026-04-07T01:07:51Z | T2I/T2V共置deadline调度在step边界恢复状态，总体SAR不能隐藏视频退步；必要证据已审，不支持当前日期采用。需该家族截点前官方公开上界，届时只重开归属/Books决定 |
| [GUIDE: Interpretable GUI Agent Evaluation via Hierarchical Diagnosis](https://arxiv.org/html/2604.04399v1) | 2026-04-07T01:11:18Z | 可恢复subtask错误与终局success聚合不等于每步hard AND；必要证据已审，不支持当前日期采用。需该家族截点前官方公开上界，届时只重开归属/Books决定 |
| [Relative Density Ratio Optimization for Stable and Statistically Consistent Model Alignment](https://arxiv.org/html/2604.04410v1) | 2026-04-07T01:12:00Z | relative密度比有界与参数梯度/有限样本人类偏好保证不同；必要证据已审，不支持当前日期采用。需该家族截点前官方公开上界，届时只重开归属/Books决定 |
| [ShieldNet: Network-Level Guardrails against Emerging Supply-Chain Injections in Agentic Systems](https://arxiv.org/pdf/2604.04426v1) | 2026-04-07T01:13:04Z | 网络effect sensor补文本盲区，但已发生exfiltration不能提前撤销；必要证据已审，不支持当前日期采用。需该家族截点前官方公开上界，届时只重开归属/Books决定 |
| [Beyond Few-Step Inference: Accelerating Video Diffusion Transformer Model Serving with Inter-Request Caching Reuse](https://arxiv.org/html/2604.04451v1) | 2026-04-07T01:14:13Z | 跨请求DiT中间feature复用需要时段/区域/质量边界，不是token KV；必要证据已审，不支持当前日期采用。需该家族截点前官方公开上界，届时只重开归属/Books决定 |
| [HDP: A Lightweight Cryptographic Protocol for Human Delegation Provenance in Agentic AI Systems](https://arxiv.org/pdf/2604.04522v1) | 2026-04-07T01:19:37Z | issuer统一key多跳provenance不等named-agent亲签，离线撤销用expiry折中；必要证据已审，不支持当前日期采用。需该家族截点前官方公开上界，届时只重开归属/Books决定 |
| [Multilingual Prompt Localization for Agent-as-a-Judge: Language and Backbone Sensitivity in Requirement-Level Evaluation](https://arxiv.org/html/2604.04532v1) | 2026-04-07T01:20:10Z | judge语言改变需求判定，不能与solver能力差异混为一谈；必要证据已审，不支持当前日期采用。需该家族截点前官方公开上界，届时只重开归属/Books决定 |
| [Mapping the Exploitation Surface: A 10,000-Trial Taxonomy of What Makes LLM Agents Exploit Vulnerabilities](https://arxiv.org/html/2604.04561v1) | 2026-04-07T01:21:39Z | goal reframing单模型显著不证明心理taxon普遍因果或免疫；必要证据已审，不支持当前日期采用。需该家族截点前官方公开上界，届时只重开归属/Books决定 |
| [The Energy Cost of Execution-Idle in GPU Clusters](https://arxiv.org/html/2604.04745v1) | 2026-04-07T01:33:15Z | 驻留execution-idle与deep idle分账，packing/clock收益需测尾延迟；必要证据已审，不支持当前日期采用。需该家族截点前官方公开上界，届时只重开归属/Books决定 |
| [DeepStack: Scalable and Accurate Design Space Exploration for Distributed 3D-Stacked AI Accelerators](https://arxiv.org/html/2604.04750v1) | 2026-04-07T01:33:28Z | 硬件与多维parallelism联合DSE需验证模型误差，搜索不保证全局最优；必要证据已审，不支持当前日期采用。需该家族截点前官方公开上界，届时只重开归属/Books决定 |
| [Your Agent, Their Asset: A Real-World Safety Analysis of OpenClaw](https://arxiv.org/html/2604.04759v1) | 2026-04-07T01:34:30Z | memory/identity/executable持久毒化需load与activation再admission；必要证据已审，不支持当前日期采用。需该家族截点前官方公开上界，届时只重开归属/Books决定 |
| [GPU Acceleration of TFHE-Based High-Precision Nonlinear Layers for Encrypted LLM Inference](https://arxiv.org/pdf/2604.04783v1) | 2026-04-07T01:35:55Z | TFHE非线性精度/PBS batch与转换成本决定隐私执行边界；必要证据已审，不支持当前日期采用。需该家族截点前官方公开上界，届时只重开归属/Books决定 |
| [Full-Duplex-Bench-v3: Benchmarking Tool Use for Full-Duplex Voice Agents Under Real-World Disfluency](https://arxiv.org/html/2604.04847v1) | 2026-04-07T01:39:16Z | speech工具成功与filler/firstcall/factual完成时刻必须分开验收；必要证据已审，不支持当前日期采用。需该家族截点前官方公开上界，届时只重开归属/Books决定 |
| [The Role of Generator Access in Autoregressive Post-Training](https://arxiv.org/html/2604.04855v1) | 2026-04-07T01:39:43Z | chosen-prefix control与logit observation分轴，稀有prefix可达性限制探索；必要证据已审，不支持当前日期采用。需该家族截点前官方公开上界，届时只重开归属/Books决定 |
| [Synthetic Sandbox for Training Machine Learning Engineering Agents](https://arxiv.org/pdf/2604.04872v1) | 2026-04-07T01:40:53Z | 合成环境先拥有可执行契约和反馈，训练cheap不等同测试端到端快；必要证据已审，不支持当前日期采用。需该家族截点前官方公开上界，届时只重开归属/Books决定 |
| [Rethinking Exploration in RLVR: From Entropy Regularization to Refinement via Bidirectional Entropy Modulation](https://arxiv.org/html/2604.04894v1) | 2026-04-07T01:41:45Z | binary group成功率分别调正负advantage，不能简化为提高entropy；必要证据已审，不支持当前日期采用。需该家族截点前官方公开上界，届时只重开归属/Books决定 |
| [A Frame is Worth One Token: Efficient Generative World Modeling with Delta Tokens](https://arxiv.org/pdf/2604.04913v1) | 2026-04-07T01:42:37Z | delta历史预测与空间重建anchor分权，BoM最近真值不提供概率校准；必要证据已审，不支持当前日期采用。需该家族截点前官方公开上界，届时只重开归属/Books决定 |
| [TriAttention: Efficient Long Reasoning with Trigonometric KV Compression](https://arxiv.org/html/2604.04921v1) | 2026-04-07T01:42:59Z | pre-RoPE统计和未来距离prune需校准revision，长递归仍弱于FullKV；必要证据已审，不支持当前日期采用。需该家族截点前官方公开上界，届时只重开归属/Books决定 |
| [RoboPhD: Evolving Diverse Complex Agents Under Tight Evaluation Budgets](https://arxiv.org/html/2604.04347v1) | 2026-04-07T01:08:18Z | 同evaluation budget范式比较不证明autoresearch普遍支配；必要证据已审，不支持当前日期采用。需该家族截点前官方公开上界，届时只重开归属/Books决定 |
| [Decocted Experience Improves Test-Time Inference in LLM Agents](https://arxiv.org/pdf/2604.04373v1) | 2026-04-07T01:09:36Z | derived lesson任务依赖且记忆规模非单调，retrieval相关性不是效用；必要证据已审，不支持当前日期采用。需该家族截点前官方公开上界，届时只重开归属/Books决定 |
| [Don't Blink: Evidence Collapse during Multimodal Reasoning](https://arxiv.org/html/2604.04207v1) | 2026-04-07T01:01:03Z | 视觉衰减风险任务依赖，entropy加vision有迁移退步且attention非因果；必要证据已审，不支持当前日期采用。需该家族截点前官方公开上界，届时只重开归属/Books决定 |
| [REAM: Merging Improves Pruning of Experts in LLMs](https://arxiv.org/html/2604.04356v1) | 2026-04-07T01:08:54Z | expert artifact merge需对齐和逐层重校准，路由频次不等稀有任务importance；必要证据已审，不支持当前日期采用。需该家族截点前官方公开上界，届时只重开归属/Books决定 |
| [DP-OPD: Differentially Private On-Policy Distillation for Language Models](https://arxiv.org/html/2604.04461v1) | 2026-04-07T01:14:57Z | student发布DP不保护teacher API所见prompt，clip/accountant对象需分清；必要证据已审，不支持当前日期采用。需该家族截点前官方公开上界，届时只重开归属/Books决定 |
| [Beyond Fixed Tests: Repository-Level Issue Resolution as Coevolution of Code and Behavioral Constraints](https://arxiv.org/html/2604.04580v1) | 2026-04-07T01:22:54Z | code/test共进化提升内部fitness，相关错误仍需外部spec和hidden oracle；必要证据已审，不支持当前日期采用。需该家族截点前官方公开上界，届时只重开归属/Books决定 |
| [From Curiosity to Caution: Mitigating Reward Hacking for Best-of-N with Pessimism](https://arxiv.org/html/2604.04648v1) | 2026-04-07T01:27:27Z | RM-feature OOD penalty限制BoN reward hacking，非概率校准/通用真值；必要证据已审，不支持当前日期采用。需该家族截点前官方公开上界，届时只重开归属/Books决定 |
| [Cog-DRIFT: Exploration on Adaptively Reformulated Instances Enables Learning from Hard Reasoning Problems](https://arxiv.org/html/2604.04767v1) | 2026-04-07T01:34:55Z | 困难题选择/填空课程改变可达reward信号，强teacher筛选和pass64零需限定；必要证据已审，不支持当前日期采用。需该家族截点前官方公开上界，届时只重开归属/Books决定 |
| [How Alignment Routes: Localizing, Scaling, and Controlling Policy Circuits in Language Models](https://arxiv.org/html/2604.04385v1) | 2026-04-07T01:10:27Z | 低读出贡献gate可有因果控制，多层carrier不能只看单点DLA；必要证据已审，不支持当前日期采用。需该家族截点前官方公开上界，届时只重开归属/Books决定 |
| [Justified or Just Convincing? Error Verifiability as a Dimension of LLM Quality](https://arxiv.org/html/2604.04418v1) | 2026-04-07T01:12:29Z | 错误可核验性与准确率分轴，rater受说服不等能识别错误；必要证据已审，不支持当前日期采用。需该家族截点前官方公开上界，届时只重开归属/Books决定 |
| [MUXQ: Mixed-to-Uniform Precision MatriX Quantization via Low-Rank Outlier Decomposition](https://arxiv.org/html/2604.04701v1) | 2026-04-07T01:30:14Z | 必要原文/章内差异已记录；需截点前官方公开上界，只定点恢复日期与采用 |
| [Don't Waste Bits! Adaptive KV-Cache Quantization for Lightweight On-Device LLMs](https://arxiv.org/html/2604.04722v1) | 2026-04-07T01:32:00Z | 原文时间单位/量化测量另有争议；需作者澄清与公开上界 |
| [LPC-SM: Local Predictive Coding and Sparse Memory for Long-Context Language Modeling](https://arxiv.org/html/2604.03263v1) | 2026-04-11T04:37:54Z | 组件效益反证保留为仅报告工作稿，需更早公开依据才确定日期 |
| [Preservation Is Not Enough for Width Growth: Regime-Sensitive Selection of Dense LM Warm Starts](https://arxiv.org/html/2604.04281v1) | 2026-04-07T01:04:47Z | 必要原文/章内差异已记录；需截点前官方公开上界，只定点恢复日期与采用 |
| [Hallucination Basins: A Dynamic Framework for Understanding and Controlling LLM Hallucinations](https://arxiv.org/html/2604.04743v1) | 2026-04-07T01:33:09Z | 必要原文/章内差异已记录；需截点前官方公开上界，只定点恢复日期与采用 |
| [Beyond the Global Scores: Fine-Grained Token Grounding as a Robust Detector of LVLM Hallucinations](https://arxiv.org/html/2604.04863v1) | 2026-04-07T01:40:06Z | 必要原文/章内差异已记录；需截点前官方公开上界，只定点恢复日期与采用 |
| [Agentic Code Optimization via Compiler-LLM Cooperation](https://arxiv.org/html/2604.04238v1) | 2026-04-07T01:02:40Z | 必要原文/章内差异已记录；需截点前官方公开上界，只定点恢复日期与采用 |
| [LOCALUT: Harnessing Capacity-Computation Tradeoffs for LUT-Based Inference in DRAM-PIM](https://arxiv.org/html/2604.04523v1) | 2026-04-07T01:19:38Z | 必要原文/章内差异已记录；需截点前官方公开上界，只定点恢复日期与采用 |

8个外部历史子入口为OpenAI Research/Publications、Google Publications/DeepMind、Meta Research、DeepSeek查看全部、Kimi历史Blog、Z.ai公开时区、MiMo历史Blog、MiniMax Agent Tech Blog。§2所见目录/版本已经处理，缺口不支持无命中或Books结论；官方当窗目录/原文时间恢复后只补该子入口。外部隔离不要求重复抓整月。

本窗可执行待办为0。46项当窗家族已逐项处置为23整合、16已有覆盖、7仅报告；root已完成最后8项必要源/实际正文复核，03647独立抽检恢复后的标准审阅/仅报告处置亦已落实。apr03最终集合的独立日级Gate通过。日期43项与8来源限制仍精确隔离，恢复条件见上表和§2，取得对应材料后只重开受影响项。

## 6. 复核

复核者：apr03（非本日报作者）
结论：通过

实际审读14来源的入口/停点/缺口与日期审计，核对46唯一候选、46证据标题集合、评分算术、23实际Books落点；复用root对单篇必要exact-v1与真实正文/相邻论证的有效独立复核，不无差别重读全部附件。此前apr01反向抽核16项，8恢复当窗、8日期/争议隔离；本轮apr03另定点抽核六条完整官方v1题摘，必要时核方法，恢复03647标准审阅后以具体反证裁为仅报告。原45项未变化的有效审阅复用，没有重扫854原始身份。详见[非作者日级记录](../_sources/daily-20260407/V3_DAY_GATE_INDEPENDENT_AUDIT.md)。

写后复核修正KiToke inverse-density、DiffSparse全局稀疏预算、AEGIS placement hierarchy、RISE activation frequency；04161 latency绑定GR00T N1.5/LIBERO/single A800及precision/SLO未披露，03362补不完整run过滤边界。最终46=23整合/16已有覆盖/7仅报告，普通pending为0；43日期项与8来源缺口保持不用于正面证据的隔离状态。不声称全部排除项已抽检、来源零遗漏或作者实验已复现。

机器校验：`scripts/validate_research.py --report papers/2026/04/07/README.md`及本次文件范围`git diff --check`通过；它们仅证明格式/可判定一致性。修改限本日作者文件与获准Books小批次；未stage、commit或push，未覆盖其他日期或共享checkpoint。
