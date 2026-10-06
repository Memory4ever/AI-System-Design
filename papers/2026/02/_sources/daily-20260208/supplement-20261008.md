# 2026-02-08 增量来源补查停点

检查：2026-10-08；补充窗口：2026-02-07 ～ 2026-02-07（北京时间完整自然日）。
原报告窗口、nanobot 原行与§4连续前缀冻结；[完整基线](supplement-baseline-20261008.md)。只写当日 README 与本目录，不写 Books、索引或 LEARNING_STATE，不 stage/commit/push。

## 来源与有限停止

14 Daily 原入口重新打开，返回见[supplement-native](supplement-native-20261008.json)，官方域日期补检见[第一组](supplement-officialsearch-20261008.json)、[具名更正及release发现](supplement-narrowsearch-20261008.json)；域检索是有限发现，不授机构全站覆盖。
OpenAI Research→RSS 实际Feb6→Feb9邻接见[RSS字段](supplement-openai-rss-20261008.txt)。Google DeepMind Publications当前首显示页Feb5→Feb12，Research/pubs只有年份；Z.ai Research Feb2→Feb11、release Feb3→Feb12，ERNIE Feb6→Apr15，MiMo Paper Feb3→Mar13。可见邻接不扩到独立项目。
Hunyuan Research原始0行后，浏览器一次创建隐藏iab页实际64.78秒超时，结果“js execution timed out; kernel reset, rerun your request”。未取得动态“全部”列表、未称零命中；保留旧STOP的失败事实，本轮不无限重试。
Meta0行、Qwen legacy止2025-09且新动态页0行、DeepSeek首页无历史日字段、Kimi当前Blog最新2025-11-07、MiMo Blog无日期、MiniMax英/中/Agent入口本轮仅导航或重定向，皆不支撑零发布。
Seed paper offset60重定位旧STOP的窗邻接Feb9→Feb5；[原字段](supplement-seed-papers60-20261008.json)。已夹住本窗后又读offset80是无必要后扩，只Jan22/Jan20、has_more=false；[实际原件](supplement-seed-papers80-20261008.json)只保操作事实，不授本窗覆盖，立即停止。不能因total82全扫。公共页242与US接口82不一致，不据此宣称完整。
Seed Blog0本轮12可见记录、has_more=true/next20，最低可见Feb12；[原件](supplement-seed-blog0-20261008.json)与旧false不同。最初未读next20即隔离是提前停止，root DAY指出可执行差额后已续同一next20一次：success/has_more=false/next空/total23，没有返回records，见[supplement-seed-blog20](supplement-seed-blog20-20261008.json)。停止真实无后续token；总23与12可见差额无法定日，不能补造完整覆盖，不将空后页记成全部机构零发布。

arXiv主题查询四条：
1. site:arxiv.org "2026" "Feb 7" (transformer OR "language model" OR MoE OR "reinforcement learning")
2. site:arxiv.org "2026" "Feb 7" (inference OR GPU OR kernel OR distributed)
3. site:arxiv.org "2026" "Feb 7" (agent OR tool OR memory OR RAG)
4. site:arxiv.org "2026" "Feb 7" (multimodal OR "world model" OR VLA OR diffusion)

[主题结果](supplement-themes-20261008.json)。CL官方2026-02月表仅查漏相关标题，重点显示编号434附近至DLLMAgent段；读取skip400/show100的返回不等于100条逐项题摘。DC月表仅2602.06800–07699相关标题切片，见[标题](supplement-dc-titles-20261008.json)。宽CL/CV/DC响应不成为全文队列；AI25首段仅发现；LG/RO/IR月表及部分定位失败。CL直接抽取超时见[失败](supplement-cl-failed-20261008.json)。
日期恢复有限尝试官方日列表/cs.DC/2026-02-07与cs.CL同日失败，具名作者页或repo无可核日事件；[最终恢复](supplement-date-last-20261008.json)。PTT Apple仅February2026；LegalRAG作者PDF路径月精度与M2A当前repo不证首公开日。Submitted/Updated、DataCite、编号月份与公告排程不补造公开日期；仅日期不明停止，不进一步读正文/附录/owner。

## 完整题摘后潜在线索：11项，均不评分、不作当窗候选

- [IGMiRAG](https://arxiv.org/abs/2602.07525v1)：图/超图记忆组织错位导致割裂且昂贵检索→层级异构超图、问句控制深度/窗口、双焦点锚点及双向扩散→可能改变关联检索的资源分配。
- [Benchmarking Legal RAG](https://arxiv.org/abs/2603.03300v1)：专家人工枚举被当ground truth→错误分析分离检索/推理并发现参考标注遗漏→先审参考答案再排模型能力，非仅法律领域指标。
- [M2A](https://arxiv.org/abs/2602.07624v1)：初始化静态概念难随长交互增量演化→不可变RawMessageStore与可更新SemanticMemoryStore、ChatAgent/MemoryManager职责分离→在线派生记忆刷新与证据溯源边界。
- [Parallel Track Transformers](https://arxiv.org/abs/2602.07306v1)：TP频繁GPU同步限制推理→架构并行track降低同步依赖→质量与通信协同设计；Apple作者页仅月精度。
- [Multi-Agentic Distributed Inference](https://arxiv.org/abs/2602.07215v1)：异构资源/模态难静态调度→长程规划、短程prompt调度与本地部署agent用实时遥测和历史分工→自适应分布式推理控制的潜在替代；组合名及收益数字不作为已证明机制。
- [Free Energy Mixer](https://arxiv.org/abs/2602.07160v1)：shared凸平均无法逐通道选择→value-conditioned逐通道log-linear posterior，温度连续平均/选择→模型读出语义的替代设计，camera-ready本身不定日。
- [Statistical Correction Pruning](https://arxiv.org/abs/2602.07375v1)：启发式易受outlier影响且重建昂贵→channel统计importance calibration与analytic energy compensation，无梯度/二阶重建→低成本剪枝质量取舍。
- [DLLM Agent](https://arxiv.org/abs/2602.07451v1)：AR/DLLM agent收益易混workflow/监督→同DeepDiver与轨迹finetune对照，揭示结构化tool-call失效与context-action masking→范式比较须约束工具schema及泄漏；局部负侧不排除。
- [Intent Mismatch](https://arxiv.org/abs/2602.07338v1)：LiC被归因模型能力不足→结构性意图歧义与Mediator-Assistant→区分交互intent resolution与扩模/训练。理论不自动排除，尚未核假设证明。
- [Anchored Decoding](https://arxiv.org/abs/2602.07120v1)：记忆复制风险→安全参考模型约束逐步预算并声称序列级界、byte跨词表融合→可控解码risk-utility设计，非法律安全保证。
- [SED-SFT](https://arxiv.org/abs/2602.07464v1)：CE mode collapse压缩RL探索→按token探索空间选择性entropy regularization/masking→SFT多样性与准确性对后续RL的影响；3B/7B及数学推理实验不是范围外理由。

前三完整AB：[原件](supplement-fast-release-and-ab-20261008.json)；PTT/Multi-Agentic：[原件](supplement-fullab-and-fast-20261008.json)及[完整定位](supplement-coreslices-20261008.json)；FEM/Pruning/DLLM/Intent/Anchored：[原件](supplement-models-ab-20261008.json)；SED：[完整AB](supplement-last-core-20261008.json)。这些只有Submission history或月级作者目录，不证Feb7首公开。题摘读完不是核心证据审阅完成。收到官方公开日/列表或可验证作者公开事件才定点重开日期，落窗后才评分及投入必要核心。

## 关闭与身份修正

- [Progressive Searching](https://arxiv.org/abs/2602.07297v1)：完整AB给出低维候选→渐进高维细化以降检索耗时，未给决定贡献的独特成立条件；目前只到通用多阶段检索流程与收益宣称，算法名及RAG关系不足准入。贡献前关闭，日期未核、不为不改变处置另建日期请求。root已实际读完整AB并校准此关闭。
- [Open TutorAI](https://arxiv.org/abs/2602.07176)：完整AB以适应性、实时响应和教学需求为动机，具体新增是LLM+3Davatar、onboarding偏好配置、内容/反馈门户和analytics；未给新的学习、状态更新、执行控制或可靠性成立证据。不是因教育领域退出，而是应用组合/engagement不足贡献。[完整AB](supplement-last-core-20261008.json)。
- 2602.07362误当Ternary ID实际是纯braid topology；身份纠正后范围外关闭，不作为模型数学潜在项。SED误ID07489失败后已纠正07464；Ternary真实ID07374只在CL标题恢复，未作题摘准入或确定候选，不展开新队列。保留[误检原件](supplement-models-ab-20261008.json)及[正确标题](supplement-last-core-20261008.json)。
- Seed Protenix与BABE标题明确生物结构/生物领域benchmark，按暂缓AIforScience关闭，不读无关全文，不把它们当本窗事件。

## 当窗新增两项的准入与必要证据

Healthcare更正：旧intro容易将HIPAA-ready延伸到个人integrations→Feb7 Changelog明确provider/payer范围，正文provider与personal分区及opt-in/no-train声明→改变厂商声明归属而非推出个人HIPAA保证。2+2+1=5，纠错触发受影响核心深入审阅，仅报告。原官方[全文229行](supplement-probe0-20261008.json)intro L19–21/provider L37–58/personal L59–66/Changelog L209–211。root独立实际读已通过窄命题。
Fast mode：同Opus4.6档位服务选择→Feb7 release以speed参数提供research preview、premium pricing/waitlist→新增接口及成本采用边界，未披露内部算法/SLO。1+2+1=4，关闭/仅报告。官方canonical https://platform.claude.com/docs/en/release-notes/overview ，[Feb7原件](supplement-last-core-20261008.json)L368–370，root已fresh实读。当前fast文档后续更新不能倒填本日。厂商up to2.5x未作为可部署承诺；除model之外workload/hardware/precision/length/batch/concurrency/SLO/evaluator为Not Disclosed。

## 精确入口差额恢复

root指出安全可用入口后，只做当前入口的有限恢复，不带其他日候选/判断：Qwen GET /api/v2/article/retrieval?type=qwen_ai&language=en-US 回40文章，只抽title/extra.date（无额外分页），Feb3→Feb10未有Feb7目录项，见[supplement-qwen-title-date](supplement-qwen-title-date-20261008.json)。首请求head120000截断导致JSON坏；第二extra投影输出过长；它们只保实际失败，不授完整。原请求改仅title/date后完整40字段；不读窗外body，不扩新材料。
DeepSeek /news/ native原17任意ISO日期包含整页dateModified2026-09-29，已排除；同本日HTML解Next payload并JSON解析真实posts为16条（14news＋2product），不是footer计数，见[title/date/type/slug/paperUrl及实际href](supplement-deepseek-title-date-20261008.json)。仅新闻/产品posts，不声称独立Research目录，相关窗口两侧为2025-12-01 V3.2→2026-04-24 V4-preview，见[原生返回](supplement-recovery-deepseek-news-20261008.json)，只核metadata、不审窗外正文。别日所谓5动态＋10Research不是本日原数组，不沿用其数目/日期结论；本日独立Research历史目录仍未核且不授零发布。MiniMax [EN native](supplement-recovery-minimax-en-20261008.json)实际12标题/日期恢复Jan27→Feb12相邻，CN [native](supplement-recovery-minimax-cn-20261008.json)实际13项Jan28→Feb12，同样夹Feb7；此前把web只显6项误沿到native的判断已纠正，不保错误CN缺口。仅Agent导航限制继续隔离。

Hunyuan按root核方法：POST https://api.hunyuan.tencent.com/api/blog/publicList；Content-Type application/json；Accept-Language zh；payload pageNum=1/pageSize=12/renderType=0。第一次作者误投影全j含body而非metadata，响应code0/totalNum11但工具108753token截断，[真实失败](supplement-hunyuan-api-20261008.json)不授覆盖，也未采用窗外正文。原请求只六字段修复取得[完整11项metadata](supplement-hunyuan-metadata-20261008.json)，id100025 displayPublishTime1770092288/publicAt1770112929都北京Feb3；id100015三日期1770971794都Feb13；夹Feb7。其余字段不一致不外推首次公开，不读窗外body，不扩页/队列。仅Blog公开API当前11条，不证明Research“全部”历史论文完整；原浏览器失败及这个范围限制继续保留。

Seed Blog的原“可继续后页→受阻”误判已纠正为实际next20空返回/无后续token的具体限制；没有新增Feb7事件或扩候选队列。

root（独立于报告作者supplement_20260208）已实际完成本轮DAY终判通过：新增2必要原证/评分与仅报告、11完整题摘日期隔离、两完整AB关闭、14有限来源含Seed实际next20与Hunyuan11、六部分及旧行/窗口/连续§4冻结。普通待办0；无Books新对象，不需要POST或共享写入。完成是安全终态，不授未知历史目录/日期正面Coverage、零发布或无遗漏；后续只按具名证据到达定点重开。完成态实际结构/引用/冻结/diff检查记日报，不stage/commit/push，本日结束，不自行接下一日。
