# 2026-06-05 V3 recovery blockers

## 当前独立恢复停点（2026-10-01）

作者sep22_resume_v3已按换日要求重读当前AGENTS、研究/Report合同、统一Prompt、Daily14源和主题、ROADMAP与相关checkpoint。窗口只为[06/04 09:00,06/05 09:00)BJT。旧71arXiv+Kimi=72完成不能继承；official-arxiv-first-public-owner-receipt-v1.json的date_semantics明确DataCite created作registration/announcement，68旧items中52confirmed/16move是登记口径而非本轮公开依据。旧V3_EVIDENCE_RECOVERED.md 16659bytes保存23恢复项的必要位置/短描述，有效具体源可核才复用，不宣称71全文通过。

当前14源有界原始入口已处理到下述有限stop与隔离终态；71旧身份不逐个重复请求同一时间接口、不无差别重读原文。Kimi一家族6分深入、Ch81两段真实写入并root非作者写后PASS；Dreaming/Endava前分母关闭PASS。新增目录cue Google Agentic RAG与SIRA v2均只列日期/版本保留，与71旧身份disjoint，共73DateHold。root最终非作者日Gate已通过，正式报告完成、普通0；73保留不是Evidence通过。未改索引/stage/commit/push。

### 本日原始入口与初步具体筛选（2026-10-01）

OpenAI本日独立读取官方[RSS](https://openai.com/news/rss.xml)1240items按[June04 01UTC,June05 01UTC)过滤，实际两条：[Dreaming](https://openai.com/index/chatgpt-memory-dreaming/) `Thu, 04 Jun 2026 09:00:00 GMT`=17BJT；[Endava](https://openai.com/index/endava-frontiers/) `Thu, 04 Jun 2026 12:00:00 GMT`=20BJT。旧Dreaming仅日历DateHold已被原时钟解决。Dreaming核心§memory/evaluate/scalable实际读：后台综合在2025已存在，新发布的具体合成实现与约5倍compute比较条件未披露；三个目标的示例未增加超出现有temporal anchor/freshness/use边界的机制。初拟前分母关闭、未评分，待root有限negative校准；不因没有benchmark泛关、不采用未审图中数字。Endava核心43–111是企业工作方式推广与客户叙述，不提供新执行/评价机制，初拟前分母关闭待校准；不展开DavaFlow企业官网或示例旅游/消费外链。

Kimi两官方release API：0.10.0 id334363633，published_at `2026-06-04T13:46:30Z`、updated_at13:50:09Z；0.10.1 id334501678，published_at `2026-06-04T17:35:34Z`、updated_at17:39:56Z；draft/prerelease均false，两事件合一家族。release核心全读。393 exact[commit](https://github.com/MoonshotAI/kimi-code/commit/beb12ac0216818a5c5eda24fb304e4ab01792784)三个必要实际patch已读：`apps/kimi-code/src/tui/controllers/session-event-handler.ts`、`apps/kimi-code/src/tui/goal-queue-store.ts`、`packages/agent-core/src/session/store/session-store.ts`。队列是TUI session目录的upcoming-goals.json，不是全部SDK/RPC通用scheduler；goal completion→cleared snapshot→turnend→idle且queuedMessages空才尝试晋升，paused/cancelled/blocked不等同完成。创建active goal后才dequeue/send，文件直接writeFile、mutation锁是进程内；不能据持久JSON称跨进程atomic/exactly-once。fork丢弃upcoming-goals文件与custom.goal，意图不会随拷贝自动继承。拟6=2+2+2深入受影响机制/兼容，必要remaining为383reload、399OAuthendpoint风险、443goal crash及owner差额；不遍历UI/title/Nix等无关patch或plans中的任务指令，不把代码阅读称测试运行。

本日独立日期恢复：官方短`/list/cs.CL/260605` HTTP404，不当空；正确`/list/cs.CL/2026-06?skip=0&show=25`为月2718 ascendingIDs且无dailyheaders；officialadvanced明确announcement只year/month。exact[05241v1](https://arxiv.org/abs/2606.05241v1)只给[v1]Wed03Jun07:11:36UTC提交，不给June05公開上界；有限官方域June05公告/search-time-contamination announced搜索未获原公告，返回窗外提交论文仅作搜索局限，未纳入候选/新池。旧DataCite created依据失效的71身份须保留精确日期请求，不将month/index/submission/normal最早schedule拼成08–09公开区间；不存在71原文必须复审的普通队列。

### 有限负侧校准（root PASS）

root非作者独立读Dreaming核心39–69、time freshness257–262与scalable301–305，并对Ch77:273–289实际temporal/freshness/use边界核准：前分母关闭PASS，不是整篇已有覆盖或否定产品，也不为图中未审数字另扩任务。Endava43–111官方core同样关闭PASS。RSS时刻沿作者本日独立取回记录；不拿日历拼造精确。两项不评分、不列候选、不改Books。

### Kimi必要受影响源续读（必要范围完成，非整份release保证）

383 exact[15d71b5](https://github.com/MoonshotAI/kimi-code/commit/15d71b5130d949c35d9dc2641e807e08d72dce48)的reload.ts、kimi-tui.ts、core-impl.ts、session/index.ts及kimi-harness.ts必要patch实际读：运行turn时拒绝reload；否则重载provider/plugin/runtime cache、关闭ready agents的cron并flush metadata/MCP/log、再resume同session；TUI撤销旧approval/question handlers并重订阅。runtimeOverride保留、不重建覆盖runtime；不是任意live热更新或恢复外部effect的保证。443 exact[15a4c64](https://github.com/MoonshotAI/kimi-code/commit/15a4c64e5cea45c9f72d8c889f306f1f964a8ac6)实际goal.ts+回归测试patch：从detach的sendNormalUserInput调用改为保host receiver的成员调用；是具体TUI crash修正，不宣称算法/长期性能增益，测试代码读过但未运行。

399 exact[232ed87](https://github.com/MoonshotAI/kimi-code/commit/232ed874d41de777e6ff9c539ac22d830d0b5c3a)风险patch必要managed-kimi-code.ts/auth.ts/model-provider.ts/refresh-providers.ts/constants.ts已读：credential key按normalized oauthHost+API baseUrl组合计算（非默认组合用SHA256前16hex），login/config provision/runtime解析同环境ref；env override与configured ref不匹配则选择expected slot，而非把默认credential直接发送到新endpoint。model provider与model refresh同步ref。该机制分离credential slot身份，不证明endpoint可信/TLS/任意custom oauthRef安全；复杂别名/canonicalization与hash碰撞不作安全定理。toolkit必要函数已在下段实际补读；不是全release安全通过。

399 toolkit.ts必要patch亦实际读齐：manager cache key将storageName与normalized oauthHost分开绑定；login/provision/force-refresh/device-login retry沿同一manager/ref，status/logout/usage/feedback也消费对应slot。不证明任意外部endpoint安全、不把JSON hash当authorization。此具体兼容/credential路由事实仅报告，原权限/凭证authority原则不重复新增正文。

### Kimi source→actual owner与真实写后（root PASS）

当前Ch81:92–135实际有activation/head与Task State Alignment的dispatch前对齐，但没有将持久future objective与active goal分开、等待complete-clear/turn-end后晋升及fork不自动复制执行意图的具体取舍。拟`AGENT-WORKFLOW` Ch81 Task State Alignment尾SF2605-19314之后→相对指代前两段，不触其他日期正文。必要源为393三实际patch，383/399/443的受影响兼容/风险事实只报告。下面literal获root非作者393必要源→actual-owner pre PASS后授权，已实际按最新文件写入Ch81:118/120（唯一SF-KIMI-CODE-0-10）。root亲读两段及前后衔接、复用其独立exact393核，真实写后PASS并释放锁。最终计1I；不以拟文替代实际写入：

> 连续目标不必一次全部送入主 Agent 的可执行上下文：把将来的 objective 保存在独立队列，当前状态只持有 active goal，能避免未来任务干扰当前完成判定。晋升下一目标至少应区分“模型宣称完成”、runtime清除当前目标、当前turn结束和dispatch空闲；暂停、取消或阻塞都不是完成。Kimi Code 0.10.0的限定TUI实现将upcoming-goals.json与active goal分开，并在上述完成/清除/turn-end条件及queued-message为空后尝试晋升。队列因此保存待执行意图，不是工具授权，也不是普通conversation memory。
>
> 队列持久化仍不保证原子晋升：原实现使用进程内mutation lock和直接文件写入，创建active goal后才移除队列项、发送输入，移除失败可能留下已创建但尚未发出的目标。跨进程并发或崩溃恢复需要另核active/queued/transcript的一致性，不能把JSON存在当exactly-once receipt。fork丢弃active与queued goals展示了另一条边界：拷贝历史不自动继承未来执行意图；希望续接时须由新branch的owner重新受理（工程推断）。低风险单会话可保留轻量队列，高风险effect仍服从既有pre-state authority、checkpoint与effect ledger验收。

### 早期有限停止（过程快照，由下方最终stop取代）

Anthropic Research本日58行首10/curated September→August，没有历史day切片；必要remaining为SeeMore/原HTML六月目标字段，不以首页无标题称无事件。DeepMind Research309行latest精选September/August→May，publication无dayclock；GoogleResearch目标页仍待本日有限核。Meta blog原入口本次web400timeout，不记0命中，原publication路由尚可重试。DeepSeek news39行实际researchJune24→Feb25/dynamicsSept10→Apr24，目标切片无记录，动态查看更多局限保留。

Hunyuan本日fresh publicList POST page1/100/renderType0返回code0/total9/list9，全publicAt/displayPublishTime/publishedAt已核原值，publicAt July06→April30夹住June04/05，无本窗条目；目录字段不证明链接论文first-public，不扩9全文。Z.ai Research175行前14完整日期标题，June16→May20目标前stop，无June04/05目录记录。Seed public_papers实际page1/13的1–20/242，June04电子动力学属于暂缓science、June03 MetaPoint目录日历在目标起点前，不拿它确认paper公开；May29后停止，不扩242。Baidu中文Blog page1/2最新May09→April30→2025Nov，目标前停止不翻旧page2。Qwennews只读page_config已返回array17，必要remaining为实际date字段/Research配置；不套06/04零命中结论。

### 最终有限来源stop与日期隔离（2026-10-01T08:33:07+08:00）

Anthropic Research原HTML实际173个publishedOn字段：chemist `2026-06-05T20:57:00.000Z`、Navigator `2026-06-03T18:00:00.000Z`、对应news `2026-06-03T10:55:00.000Z`夹住目标；目标June04没有记录。chemist明确窗外且是暂缓science，不再继承旧日报归属。只过滤原目录字段，不把全部173正文算已审。

Google Research Generative AI第一页12目录读至June03→May28；NLP第一页读至June05 Agentic RAG→May19；Machine Intelligence首12仅至August21，观察到分页link点击错误，有限原HTML请求timeout/0bytes，目标June04/05官方域检索只有Agentic RAG及heart-health领域应用。后者按ROADMAP暂缓范围关闭；55页不展开。DeepMind curated latest和年级publication缺目标历史批次，本窗主题覆盖局限保留。

[Agentic RAG](https://research.google/blog/unlocking-dependable-responses-with-gemini-enterprise-agent-platforms-agentic-rag/) core104–194实际读：query fanout/跨corpus planner与sufficient-context检查draft、snippets、missing reason/feedback后迭代；评测仅FramesQA、LLM judge，配置与成本细项未披露，不能把34%或90.1%当通用保证。原页只有June5日历，HTML两次0bytes，缺原发布timezone/clock，不能证明完全落窗。当前不评分/不采用；恢复原发布时间后只深审对应具体差额，不扩Google全部论文。

Meta publication实际page1成功一次、June05 SIRA→May27→May26后混入旧库存；后续相同入口两次web不可用，不无限重试。SIRA当前官方页面完整摘要与[exact-v2](https://arxiv.org/abs/2605.06647v2)完整摘要/版本史均已读：v1 `Thu,7May2026 17:54:29UTC`；v2 `Thu,4Jun2026 21:56:21UTC`，只有submission而非公開上界。原v1摘要未含BrowseComp-Wikipedia，v2明确增加该hard-search/无index-enrichment对照，因此撤销旧“非重要修订已去重”泛断言。目录June05日历不证明论文v2首次公开时刻，PDF CDN有限一次cachemiss；保留v2身份与潜在具体评价增量，不采用未核数字，不全文重审或提前计E/I。请求exact-v2公开receipt并确认官方PDF对应版本，取得后只重开受影响机制/对照。

Qwen只读page_config实际news17（最大2025-04-28T20:00:00Z）、Research60（最大2025-12-23T05:08:30Z），两配置无目标日期；本日有限官方域June04/05检索只返回chat分享噪声，不能补2026研究目录。Moonshot PlatformBlog全部可见27条显式日期最新2025Nov07，2026模型事件历史目录仍有限；Kimi两个exact releases已处理，不代全org commit审计。

MiMo本日Paper8日历June29→March13覆盖目标前后；Blog15无日期。fresh官方4752.2908c99e.js 688092bytes实际June-date四次（EN/ZH各CodeJune10与UltraSpeedJune08），pipeline原routeMay30；没有June04/05明示frontmatter，不以undated routes证明零。MiniMax本日EN/中文主Blog目录June09→June01→May停；Agent TechBlog仅15行壳，观察到llms.txt index并读，只有当前使用文档、无六月历史dated blog条目，不扩48用户指南。两源历史分支与Google/Qwen/arXiv均保留具体目录缺口。

Hunyuan/Z.ai/Seed/Baidu/DeepSeek本日实际有限stop见前段，身份/字段只证明原目录范围；不沿他日无命中、不要求全部旧正文。五类需恢复的历史入口为Google目标主题/DeepMind批次、Qwen2026目录、MiMo dated Blog、MiniMax Agent历史Blog、arXiv本批公开列表；原始可用入口已有限尝试，重新取到目标primary feed/时钟才重开，绝不用于覆盖无遗漏断言。

### 73具名终态日期保留（非候选/Evidence/Books通过）

以下71旧exact-v1各仅请求一次：对应原始官方公开批次/公告、作者带timezone的公开正文receipt或可信原快照，需给first-public上界与已知提交下界而非DataCiteCreated/Updated。统一日期口径和有限官方入口失败适用于这71身份，不逐个重放同一接口；原评分/审阅快照在后文保留但不计本轮。Google/SIRA两新cue不在71中；共73unique，均未正面采用、未新增Books、未标证据完成。不是73篇必要源全审。

| 身份 | 缺口/终态 | 采用边界 |
| --- | --- | --- |
| [Search-Time Contamination in Deep Research Agents: Measuring Performance Inflation in Public Benchmark Evaluation](https://arxiv.org/abs/2606.05241v1) | DateHold：旧登记/推定时刻非公开证据；缺该 exact-v1 first-public 上界 | 不列本轮候选、不评分、不计I/E；原必要证据仅保留 |
| [Statistically Reliable LLM-Based Ranking Evaluation via Prediction-Powered Inference](https://arxiv.org/abs/2606.05308v1) | DateHold：旧登记/推定时刻非公开证据；缺该 exact-v1 first-public 上界 | 不列本轮候选、不评分、不计I/E；原必要证据仅保留 |
| [A Taxonomy of Runtime Faults in Model Context Protocol Servers](https://arxiv.org/abs/2606.05339v1) | DateHold：旧登记/推定时刻非公开证据；缺该 exact-v1 first-public 上界 | 不列本轮候选、不评分、不计I/E；原必要证据仅保留 |
| [Stability vs. Manipulability: Evaluating Robustness Under Post-Decision Interaction in LLM Judges](https://arxiv.org/abs/2606.05384v1) | DateHold：旧登记/推定时刻非公开证据；缺该 exact-v1 first-public 上界 | 不列本轮候选、不评分、不计I/E；原必要证据仅保留 |
| [VASO: Formally Verifiable Self-Evolving Skills for Physical AI Agents](https://arxiv.org/abs/2606.05395v1) | DateHold：旧登记/推定时刻非公开证据；缺该 exact-v1 first-public 上界 | 不列本轮候选、不评分、不计I/E；原必要证据仅保留 |
| [Trust, but Don't Verify: Epistemic Blind Spots in LLM Source Evaluation](https://arxiv.org/abs/2606.05403v1) | DateHold：旧登记/推定时刻非公开证据；缺该 exact-v1 first-public 上界 | 不列本轮候选、不评分、不计I/E；原必要证据仅保留 |
| [When Evidence is Sparse: Weakly Supervised Early Failure Alerting in Dialogs and LLM-Agent Trajectories](https://arxiv.org/abs/2606.05414v1) | DateHold：旧登记/推定时刻非公开证据；缺该 exact-v1 first-public 上界 | 不列本轮候选、不评分、不计I/E；原必要证据仅保留 |
| [Zero knowledge verification for frontier AI training is possible](https://arxiv.org/abs/2606.05433v1) | DateHold：旧登记/推定时刻非公开证据；缺该 exact-v1 first-public 上界 | 不列本轮候选、不评分、不计I/E；原必要证据仅保留 |
| [ADK Arena: Evaluating Agent Development Kits via LLM-as-a-Developer](https://arxiv.org/abs/2606.05548v1) | DateHold：旧登记/推定时刻非公开证据；缺该 exact-v1 first-public 上界 | 不列本轮候选、不评分、不计I/E；原必要证据仅保留 |
| [An Embarrassingly Simple Detector for Model Extraction Attacks in Large Language Model API Traffic](https://arxiv.org/abs/2606.05725v1) | DateHold：旧登记/推定时刻非公开证据；缺该 exact-v1 first-public 上界 | 不列本轮候选、不评分、不计I/E；原必要证据仅保留 |
| [Membrane: A Self-Evolving Contrastive Safety Memory for LLM Agent Defense](https://arxiv.org/abs/2606.05743v1) | DateHold：旧登记/推定时刻非公开证据；缺该 exact-v1 first-public 上界 | 不列本轮候选、不评分、不计I/E；原必要证据仅保留 |
| [SentinelRAG: Synthetic Sentinel Knowledge for RAG Database Copyright Protection](https://arxiv.org/abs/2606.05787v1) | DateHold：旧登记/推定时刻非公开证据；缺该 exact-v1 first-public 上界 | 不列本轮候选、不评分、不计I/E；原必要证据仅保留 |
| [From Risk Classification to Action Plan Remediation: A Guardrail Feedback Driven Framework for LLM Agents](https://arxiv.org/abs/2606.05805v1) | DateHold：旧登记/推定时刻非公开证据；缺该 exact-v1 first-public 上界 | 不列本轮候选、不评分、不计I/E；原必要证据仅保留 |
| [Steering Vectors are an Adversarial Attack Surface](https://arxiv.org/abs/2606.05958v1) | DateHold：旧登记/推定时刻非公开证据；缺该 exact-v1 first-public 上界 | 不列本轮候选、不评分、不计I/E；原必要证据仅保留 |
| [The Self-Correction Illusion: Role Relabeling Gates Explicit Error Flagging in Large Language Models](https://arxiv.org/abs/2606.05976v1) | DateHold：旧登记/推定时刻非公开证据；缺该 exact-v1 first-public 上界 | 不列本轮候选、不评分、不计I/E；原必要证据仅保留 |
| [HUSH-Bench: Measuring Memory-Use Boundaries for Sensitive History in Conversational Agents](https://arxiv.org/abs/2606.06055v1) | DateHold：旧登记/推定时刻非公开证据；缺该 exact-v1 first-public 上界 | 不列本轮候选、不评分、不计I/E；原必要证据仅保留 |
| [From Reward-Hack Activations to Agentic Risk States: Context-Calibrated Mechanistic Monitoring in LLM Agents](https://arxiv.org/abs/2606.06223v1) | DateHold：旧登记/推定时刻非公开证据；缺该 exact-v1 first-public 上界 | 不列本轮候选、不评分、不计I/E；原必要证据仅保留 |
| [From Failed Trajectories to Reliable LLM Agents: Diagnosing and Repairing Harness Flaws](https://arxiv.org/abs/2606.06324v1) | DateHold：旧登记/推定时刻非公开证据；缺该 exact-v1 first-public 上界 | 不列本轮候选、不评分、不计I/E；原必要证据仅保留 |
| [WebMCP Tool Surface Poisoning: Runtime Manipulation Attacks on LLM Agents](https://arxiv.org/abs/2606.06387v1) | DateHold：旧登记/推定时刻非公开证据；缺该 exact-v1 first-public 上界 | 不列本轮候选、不评分、不计I/E；原必要证据仅保留 |
| [Will the Agent Recuse, and Will It Stop? Measuring LLM-Agent Compliance with In-Band Governance Signals at the Access Door and Mid-Flight](https://arxiv.org/abs/2606.06460v1) | DateHold：旧登记/推定时刻非公开证据；缺该 exact-v1 first-public 上界 | 不列本轮候选、不评分、不计I/E；原必要证据仅保留 |
| [BIDENT: Heterogeneous Operator-level Mapping for Efficient Edge Inference](https://arxiv.org/abs/2606.05271v1) | DateHold：旧登记/推定时刻非公开证据；缺该 exact-v1 first-public 上界 | 不列本轮候选、不评分、不计I/E；原必要证据仅保留 |
| [SET: Stream-Event-Triggered Scheduling for Efficient CUDA Graph Pipelines](https://arxiv.org/abs/2606.05495v1) | DateHold：旧登记/推定时刻非公开证据；缺该 exact-v1 first-public 上界 | 不列本轮候选、不评分、不计I/E；原必要证据仅保留 |
| [ColBERTSaR: Sparsified ColBERT Index via Product Quantization](https://arxiv.org/abs/2606.05568v1) | DateHold：旧登记/推定时刻非公开证据；缺该 exact-v1 first-public 上界 | 不列本轮候选、不评分、不计I/E；原必要证据仅保留 |
| [AsyncWebRL: Efficient Asynchronous Reinforcement Learning for Multi-Step Visual Web Agents](https://arxiv.org/abs/2606.05597v1) | DateHold：旧登记/推定时刻非公开证据；缺该 exact-v1 first-public 上界 | 不列本轮候选、不评分、不计I/E；原必要证据仅保留 |
| [AdaPLD: Adaptive Retrieval and Reuse for Efficient Model-Free Speculative Decoding](https://arxiv.org/abs/2606.05742v1) | DateHold：旧登记/推定时刻非公开证据；缺该 exact-v1 first-public 上界 | 不列本轮候选、不评分、不计I/E；原必要证据仅保留 |
| [QCFuse: Query-Aware Cache Fusion via Compressed View for Efficient RAG Serving](https://arxiv.org/abs/2606.05875v1) | DateHold：旧登记/推定时刻非公开证据；缺该 exact-v1 first-public 上界 | 不列本轮候选、不评分、不计I/E；原必要证据仅保留 |
| [Beyond Greedy Chunking: SLO-Aware Sliding-Window Scheduling for LLM Inference](https://arxiv.org/abs/2606.05933v1) | DateHold：旧登记/推定时刻非公开证据；缺该 exact-v1 first-public 上界 | 不列本轮候选、不评分、不计I/E；原必要证据仅保留 |
| [Demystifying NVSHMEM: A System-Level Analysis on Symmetric Memory and Device-Initiated Operations in GPU Communication](https://arxiv.org/abs/2606.05951v1) | DateHold：旧登记/推定时刻非公开证据；缺该 exact-v1 first-public 上界 | 不列本轮候选、不评分、不计I/E；原必要证据仅保留 |
| [Learning to Route LLMs from Implicit Cost-Performance Preferences via Meta-Learning](https://arxiv.org/abs/2606.06178v1) | DateHold：旧登记/推定时刻非公开证据；缺该 exact-v1 first-public 上界 | 不列本轮候选、不评分、不计I/E；原必要证据仅保留 |
| [RedKnot: Efficient Long-Context LLM Serving with Head-Aware KV Reuse and SegPagedAttention](https://arxiv.org/abs/2606.06256v1) | DateHold：旧登记/推定时刻非公开证据；缺该 exact-v1 first-public 上界 | 不列本轮候选、不评分、不计I/E；原必要证据仅保留 |
| [Tangram: Unlocking Non-Uniform KV Cache Compression for Efficient Multi-turn LLM Serving](https://arxiv.org/abs/2606.06302v1) | DateHold：旧登记/推定时刻非公开证据；缺该 exact-v1 first-public 上界 | 不列本轮候选、不评分、不计I/E；原必要证据仅保留 |
| [Vortex: Efficient and Programmable Sparse Attention Serving for AI Agents](https://arxiv.org/abs/2606.06453v1) | DateHold：旧登记/推定时刻非公开证据；缺该 exact-v1 first-public 上界 | 不列本轮候选、不评分、不计I/E；原必要证据仅保留 |
| [You Only Index Once: Cross-Layer Sparse Attention with Shared Routing](https://arxiv.org/abs/2606.06467v1) | DateHold：旧登记/推定时刻非公开证据；缺该 exact-v1 first-public 上界 | 不列本轮候选、不评分、不计I/E；原必要证据仅保留 |
| [What Should Agents Say? Action-state Communication for Efficient Multi-Agent Systems](https://arxiv.org/abs/2606.05304v1) | DateHold：旧登记/推定时刻非公开证据；缺该 exact-v1 first-public 上界 | 不列本轮候选、不评分、不计I/E；原必要证据仅保留 |
| [Executable Schema Contracts: From Automatic Ingestion to Multi-Source Retrieval](https://arxiv.org/abs/2606.05415v1) | DateHold：旧登记/推定时刻非公开证据；缺该 exact-v1 first-public 上界 | 不列本轮候选、不评分、不计I/E；原必要证据仅保留 |
| [Data Flow Control: Data Safety Policies for AI Agents](https://arxiv.org/abs/2606.05679v1) | DateHold：旧登记/推定时刻非公开证据；缺该 exact-v1 first-public 上界 | 不列本轮候选、不评分、不计I/E；原必要证据仅保留 |
| [Entropy-Based Observability for AI Agent Behavior](https://arxiv.org/abs/2606.05872v1) | DateHold：旧登记/推定时刻非公开证据；缺该 exact-v1 first-public 上界 | 不列本轮候选、不评分、不计I/E；原必要证据仅保留 |
| [EMBER: Efficient Memory via Budgeted Evidence Retention for Long-Horizon Agents](https://arxiv.org/abs/2606.05894v1) | DateHold：旧登记/推定时刻非公开证据；缺该 exact-v1 first-public 上界 | 不列本轮候选、不评分、不计I/E；原必要证据仅保留 |
| [IA-RAG: Interval-Algebra-Driven Temporal Reasoning for Dynamic Knowledge Retrieval](https://arxiv.org/abs/2606.06044v1) | DateHold：旧登记/推定时刻非公开证据；缺该 exact-v1 first-public 上界 | 不列本轮候选、不评分、不计I/E；原必要证据仅保留 |
| [Beyond Similarity: Trustworthy Memory Search for Personal AI Agents](https://arxiv.org/abs/2606.06054v1) | DateHold：旧登记/推定时刻非公开证据；缺该 exact-v1 first-public 上界 | 不列本轮候选、不评分、不计I/E；原必要证据仅保留 |
| [Beyond Semantic Organization: Memory as Execution State Management for Long-Horizon Agents](https://arxiv.org/abs/2606.06090v1) | DateHold：旧登记/推定时刻非公开证据；缺该 exact-v1 first-public 上界 | 不列本轮候选、不评分、不计I/E；原必要证据仅保留 |
| [TOKI: A Bitemporal Operator Algebra for Contradiction Resolution in LLM-Agent Persistent Memory](https://arxiv.org/abs/2606.06240v1) | DateHold：旧登记/推定时刻非公开证据；缺该 exact-v1 first-public 上界 | 不列本轮候选、不评分、不计I/E；原必要证据仅保留 |
| [ToolChoiceConfusion: Causal Minimal Tool Filtering for Reliable LLM Agents](https://arxiv.org/abs/2606.06284v1) | DateHold：旧登记/推定时刻非公开证据；缺该 exact-v1 first-public 上界 | 不列本轮候选、不评分、不计I/E；原必要证据仅保留 |
| [TokenMizer: Graph-Structured Session Memory for Long-Horizon LLM Context Management](https://arxiv.org/abs/2606.06337v1) | DateHold：旧登记/推定时刻非公开证据；缺该 exact-v1 first-public 上界 | 不列本轮候选、不评分、不计I/E；原必要证据仅保留 |
| [Agent Memory: Characterization and System Implications of Stateful Long-Horizon Workloads](https://arxiv.org/abs/2606.06448v1) | DateHold：旧登记/推定时刻非公开证据；缺该 exact-v1 first-public 上界 | 不列本轮候选、不评分、不计I/E；原必要证据仅保留 |
| [Autoregressive Diffusion World Models for Off-Policy Evaluation of LLM Agents](https://arxiv.org/abs/2606.05558v1) | DateHold：旧登记/推定时刻非公开证据；缺该 exact-v1 first-public 上界 | 不列本轮候选、不评分、不计I/E；原必要证据仅保留 |
| [CLaaS: Continual learning as a service for sample efficient online learning](https://arxiv.org/abs/2606.05559v1) | DateHold：旧登记/推定时刻非公开证据；缺该 exact-v1 first-public 上界 | 不列本轮候选、不评分、不计I/E；原必要证据仅保留 |
| [Statistical Priors for Implicit Preferences: Decoupling Skill Selection as a Local Harness in Personal Agents](https://arxiv.org/abs/2606.05828v1) | DateHold：旧登记/推定时刻非公开证据；缺该 exact-v1 first-public 上界 | 不列本轮候选、不评分、不计I/E；原必要证据仅保留 |
| [The Evaluation Blind Spot: A Stereological Theory of Benchmark Coverage for Large Language Models](https://arxiv.org/abs/2606.05169v1) | DateHold：旧登记/推定时刻非公开证据；缺该 exact-v1 first-public 上界 | 不列本轮候选、不评分、不计I/E；原必要证据仅保留 |
| [ERRORQUAKE: Heavy-Tailed Error Severity Distributions in Open-Weight Large Language Models](https://arxiv.org/abs/2606.05170v1) | DateHold：旧登记/推定时刻非公开证据；缺该 exact-v1 first-public 上界 | 不列本轮候选、不评分、不计I/E；原必要证据仅保留 |
| [AppAgent-Claw: CLI Is All You Need for GUI Automation](https://arxiv.org/abs/2606.05171v1) | DateHold：旧登记/推定时刻非公开证据；缺该 exact-v1 first-public 上界 | 不列本轮候选、不评分、不计I/E；原必要证据仅保留 |
| [LANTERN: Layered Archival and Temporal Episodic Retrieval Network for Long-Context LLM Conversations](https://arxiv.org/abs/2606.05182v1) | DateHold：旧登记/推定时刻非公开证据；缺该 exact-v1 first-public 上界 | 不列本轮候选、不评分、不计I/E；原必要证据仅保留 |
| [State commitment learning: training language models to distinguish computation from memory](https://arxiv.org/abs/2606.05201v1) | DateHold：旧登记/推定时刻非公开证据；缺该 exact-v1 first-public 上界 | 不列本轮候选、不评分、不计I/E；原必要证据仅保留 |
| [Domain-Conditioned Safety in Frontier Computer-Using Agents: A 793-Episode Browser Benchmark, a Coding-Domain Cross-Reference, and a Reproducibility Audit of Recent Red-Teaming](https://arxiv.org/abs/2606.05233v1) | DateHold：旧登记/推定时刻非公开证据；缺该 exact-v1 first-public 上界 | 不列本轮候选、不评分、不计I/E；原必要证据仅保留 |
| [DeployBench: Benchmarking LLM Agents for Research Artifact Deployment](https://arxiv.org/abs/2606.05238v1) | DateHold：旧登记/推定时刻非公开证据；缺该 exact-v1 first-public 上界 | 不列本轮候选、不评分、不计I/E；原必要证据仅保留 |
| [SentinelBench: A Benchmark for Long-Running Monitoring Agents](https://arxiv.org/abs/2606.05342v1) | DateHold：旧登记/推定时刻非公开证据；缺该 exact-v1 first-public 上界 | 不列本轮候选、不评分、不计I/E；原必要证据仅保留 |
| [Ahoy: LLMs Enacting Multiagent Interaction Protocols](https://arxiv.org/abs/2606.05390v1) | DateHold：旧登记/推定时刻非公开证据；缺该 exact-v1 first-public 上界 | 不列本轮候选、不评分、不计I/E；原必要证据仅保留 |
| [Agents' Last Exam](https://arxiv.org/abs/2606.05405v1) | DateHold：旧登记/推定时刻非公开证据；缺该 exact-v1 first-public 上界 | 不列本轮候选、不评分、不计I/E；原必要证据仅保留 |
| [The Granularity Gap: A Multi-Dimensional Cross-Generational Audit of Sycophancy in Gemini Models](https://arxiv.org/abs/2606.05183v1) | DateHold：旧登记/推定时刻非公开证据；缺该 exact-v1 first-public 上界 | 不列本轮候选、不评分、不计I/E；原必要证据仅保留 |
| [Learned Subspace Compression for Communication-Efficient Pipeline Parallelism](https://arxiv.org/abs/2606.05484v1) | DateHold：旧登记/推定时刻非公开证据；缺该 exact-v1 first-public 上界 | 不列本轮候选、不评分、不计I/E；原必要证据仅保留 |
| [AdaPlanBench: Evaluating Adaptive Planning in Large Language Model Agents under World and User Constraints](https://arxiv.org/abs/2606.05622v1) | DateHold：旧登记/推定时刻非公开证据；缺该 exact-v1 first-public 上界 | 不列本轮候选、不评分、不计I/E；原必要证据仅保留 |
| [Do More Agents Help? Controlled and Protocol-Aligned Evaluation of LLM Agent Workflows](https://arxiv.org/abs/2606.05670v1) | DateHold：旧登记/推定时刻非公开证据；缺该 exact-v1 first-public 上界 | 不列本轮候选、不评分、不计I/E；原必要证据仅保留 |
| [AdaMEM: Test-Time Adaptive Memory for Language Agents](https://arxiv.org/abs/2606.05684v1) | DateHold：旧登记/推定时刻非公开证据；缺该 exact-v1 first-public 上界 | 不列本轮候选、不评分、不计I/E；原必要证据仅保留 |
| [SubtleMemory: A Benchmark for Fine-Grained Relational Memory Discrimination in Long-Horizon AI Agents](https://arxiv.org/abs/2606.05761v1) | DateHold：旧登记/推定时刻非公开证据；缺该 exact-v1 first-public 上界 | 不列本轮候选、不评分、不计I/E；原必要证据仅保留 |
| [When Tools Fail: Benchmarking Dynamic Replanning and Anomaly Recovery in LLM Agents](https://arxiv.org/abs/2606.05806v1) | DateHold：旧登记/推定时刻非公开证据；缺该 exact-v1 first-public 上界 | 不列本轮候选、不评分、不计I/E；原必要证据仅保留 |
| [Asuka-Bench: Benchmarking Code Agents on Underspecified User Intent and Multi-Round Refinement](https://arxiv.org/abs/2606.05920v1) | DateHold：旧登记/推定时刻非公开证据；缺该 exact-v1 first-public 上界 | 不列本轮候选、不评分、不计I/E；原必要证据仅保留 |
| [Evolving Agents in the Dark: Retrospective Harness Optimization via Self-Preference](https://arxiv.org/abs/2606.05922v1) | DateHold：旧登记/推定时刻非公开证据；缺该 exact-v1 first-public 上界 | 不列本轮候选、不评分、不计I/E；原必要证据仅保留 |
| [Epistemic Injustice in Language Models: An Audit of Pretraining Filters and Guardrails](https://arxiv.org/abs/2606.05936v1) | DateHold：旧登记/推定时刻非公开证据；缺该 exact-v1 first-public 上界 | 不列本轮候选、不评分、不计I/E；原必要证据仅保留 |
| [Dense Contexts Are Hard Contexts: Lexical Density Limits Effective Context in LLMs](https://arxiv.org/abs/2606.06203v1) | DateHold：旧登记/推定时刻非公开证据；缺该 exact-v1 first-public 上界 | 不列本轮候选、不评分、不计I/E；原必要证据仅保留 |
| [LLMs Can Leak Training Data But Do They Want To? A Propensity-Aware Evaluation of Memorization in LLMs](https://arxiv.org/abs/2606.06286v1) | DateHold：旧登记/推定时刻非公开证据；缺该 exact-v1 first-public 上界 | 不列本轮候选、不评分、不计I/E；原必要证据仅保留 |
| [CollabSim: A CSCW-Grounded Methodology for Investigating Collaborative Competence of LLM Agents through Controlled Multi-Agent Experiments](https://arxiv.org/abs/2606.06399v1) | DateHold：旧登记/推定时刻非公开证据；缺该 exact-v1 first-public 上界 | 不列本轮候选、不评分、不计I/E；原必要证据仅保留 |
| [Google Agentic RAG](https://research.google/blog/unlocking-dependable-responses-with-gemini-enterprise-agent-platforms-agentic-rag/) | DateHold：June05相交日历、原HTMLclock两次取不到；恢复原发布timezone/clock | 只有core具体贡献线索，不评分/不计本轮候选/Books |
| [SIRA 2605.06647v2](https://arxiv.org/abs/2605.06647v2) | DateHold：June04 21:56UTC为提交，MetaJune05为日历；缺exact-v2公开receipt与官方PDF版本身份 | 重要修订线索非源PASS；不继承非重要去重，不采用新数字 |

### 最终非作者日Gate（root PASS）

root实际通读正式六部分、packet最终stop/两新DateHold与73具名表，计73rows=72unique arXiv（71旧exact-v1+SIRAv2）+Google且disjoint；核14到期源和五具名历史缺口。1家族双release正确窗口、6分深入、actual Ch81两段及衔接真实写后通过；两release API原时钟/false flags独立核，393必要源复用其实际独立读。Dreaming/Endava负侧复用有效非作者核心/owner核。旧72/67E/4Only/1I与旧Complete明确legacy，不毁有效正文、不计本轮采用。普通0，安全终态通过，73日期/来源隔离不称Evidence通过或零漏。完成态V3+三文件scoped diffcheck再实际通过后交接06/08，不新增审计文件或索引写入。

## 旧快照（非本轮分母、日期或Evidence/Books验收）

> **2026-09-11 update：** 下方 Books trace-to-body 队列已被非作者 final fresh audit 覆盖。最终分母为 71 Candidate / 635 Close；旧 8 项 Integrate 全部为 `已有覆盖`，new Integrate = 0，正文缺口 = 0。当前唯一报告侧 blocker 是最终 71 项 Candidate 的 Evidence 与逐项 Books Decision。

## Denominator

可读基线为 706 raw / 68 prior / 638 closure proposals。502 项共用 incremental closure 理由被反例击穿后已逐题重审，其余 136 项也完成 title-first、边界项完整摘要复核。权威分母冻结为 Candidate 76 / Close 630：old prior 保留 52、关闭 16；old closure 恢复 24、维持关闭 614。AppAgent-Claw（2606.05171）、LANTERN（2606.05182）、state commitment learning（2606.05201）与 DeployBench（2606.05238）恢复；long-horizon credit（2606.05263）因仍是局部 RL credit 方法而关闭。逐项依据与 FP/FN 抽查见 V3_SCREENING_LEDGER.md。当前 blocker 转为 24 个新恢复 Candidate 的评分/Evidence/Books Decision，以及下列 surviving Integrate 的 Books trace-to-body。

## Books write queue

当前八项旧 Integrate 均只找到 trace，没有独立 semantic-body-binding：

| Source Family ID | Target file | Trace anchor | 正文队列 |
| --- | --- | --- | --- |
| SF-2026-ARXIV-2606-05304 | books/part-07-agent/82-multi-agent.md | daily-books-trace:SF-2026-ARXIV-2606-05304（约 870 行） | 补写 action-state communication 的消息语义/拓扑边界 |
| SF-2026-ARXIV-2606-05679 | books/part-06-ai-infrastructure/72-security.md | daily-books-trace:SF-2026-ARXIV-2606-05679（约 2164 行） | 补写 agent data-flow policy 的控制点与执行边界 |
| SF-2026-ARXIV-2606-05933 | books/part-05-inference-system/56-inference-scheduling.md | daily-books-trace:SF-2026-ARXIV-2606-05933（约 1267 行） | 补写 sliding-window/SLO 调度机制与适用边界 |
| SF-2026-ARXIV-2606-05951 | books/part-04-training-system/36-distributed-training.md | daily-books-trace:SF-2026-ARXIV-2606-05951（约 1535 行） | 补写 symmetric memory/device-initiated communication 的系统边界 |
| SF-2026-ARXIV-2606-06090 | books/part-07-agent/77-memory.md | daily-books-trace:SF-2026-ARXIV-2606-06090（约 1547 行） | 补写 memory-as-execution-state 的 owner 与恢复边界 |
| SF-2026-ARXIV-2606-06240 | books/part-07-agent/77-memory.md | daily-books-trace:SF-2026-ARXIV-2606-06240（约 1553 行） | 补写 bitemporal contradiction resolution 的时态语义 |
| SF-2026-ARXIV-2606-06256 | books/part-05-inference-system/45-why-kv-cache-speeds-up.md | daily-books-trace:SF-2026-ARXIV-2606-06256（约 1488 行） | 补写 head-aware reuse/SegPagedAttention 的命中与失效边界 |
| SF-2026-ARXIV-2606-06453 | books/part-05-inference-system/47-pagedattention.md | daily-books-trace:SF-2026-ARXIV-2606-06453（约 247 行） | 补写 programmable sparse-attention serving 的块管理与回退边界 |

单独 trace 修正队列：SF-2026-ARXIV-2606-05304 的 Daily 2026-06-04 改为 2026-06-05；其余七项日期正确。正文队列只在候选 survives 当前分母后消费。


## 旧正式§3/§4原始保留（非本轮日期、候选或Books验收）

以下是06/05恢复前旧报告的材料/证据快照，保存其有效必要位置，不继承旧72/67E/4Only/1I标签；旧表08–09推定公开区间均未经本轮核准，不能拿本块支持本轮正面采用。尤其2606.06203旧正文保留但不计本轮I。该快照中‘完成/已核/已有覆盖’仅为当时作者判断，并非本次非作者验收。

## 3. 候选与判断

以下为旧72家族候选快照，均未获本轮日期/证据/Books验收，不是当前确定入选；原有效证据与正文保留。恢复后仅把有真实落窗和具体贡献依据的事件列回正式当窗表。

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [Kimi Code 0.10.0 / 0.10.1](https://github.com/MoonshotAI/kimi-code/releases/tag/%40moonshot-ai/kimi-code%400.10.0) | 2026-06-04T21:46:30+08:00 ～ 2026-06-05T01:35:34+08:00 | goal queue 与显式 config/session reload 把连续目标和运行配置变为可观察状态；2+1+2=5 | 标准完成 | 已有覆盖：`AGENT-WORKFLOW` — [章节](../../../../books/part-07-agent/81-workflow.md) |
| [Search-Time Contamination in Deep Research Agents: Measuring Performance Inflation in Public Benchmark Evaluation](https://arxiv.org/abs/2606.05241v1) | 2026-06-05T08:00:00+08:00 ～ 2026-06-05T09:00:00+08:00 | 3+3+2=8；exact-v1 与当前 claim 一致，owner=`PLATFORM-EVALUATION-SYSTEM` | 深入完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM`（[books/part-06-ai-infrastructure/66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)) |
| [Statistically Reliable LLM-Based Ranking Evaluation via Prediction-Powered Inference](https://arxiv.org/abs/2606.05308v1) | 2026-06-05T08:00:00+08:00 ～ 2026-06-05T09:00:00+08:00 | 3+3+2=8；exact-v1 与当前 claim 一致，owner=`PLATFORM-EVALUATION-SYSTEM` | 深入完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM`（[books/part-06-ai-infrastructure/66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)) |
| [A Taxonomy of Runtime Faults in Model Context Protocol Servers](https://arxiv.org/abs/2606.05339v1) | 2026-06-05T08:00:00+08:00 ～ 2026-06-05T09:00:00+08:00 | 3+3+3=9；exact-v1 与当前 claim 一致，owner=`AGENT-MCP` | 深入完成 | 已有覆盖：`AGENT-MCP`（[books/part-07-agent/83-mcp.md](../../../../books/part-07-agent/83-mcp.md)) |
| [Stability vs. Manipulability: Evaluating Robustness Under Post-Decision Interaction in LLM Judges](https://arxiv.org/abs/2606.05384v1) | 2026-06-05T08:00:00+08:00 ～ 2026-06-05T09:00:00+08:00 | 3+3+2=8；exact-v1 与当前 claim 一致，owner=`PLATFORM-EVALUATION-SYSTEM` | 深入完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM`（[books/part-06-ai-infrastructure/66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)) |
| [VASO: Formally Verifiable Self-Evolving Skills for Physical AI Agents](https://arxiv.org/abs/2606.05395v1) | 2026-06-05T08:00:00+08:00 ～ 2026-06-05T09:00:00+08:00 | 3+3+2=8；exact-v1 与当前 claim 一致，owner=`AGENT-WORKFLOW` | 深入完成 | 已有覆盖：`AGENT-WORKFLOW`（[books/part-07-agent/81-workflow.md](../../../../books/part-07-agent/81-workflow.md)) |
| [Trust, but Don't Verify: Epistemic Blind Spots in LLM Source Evaluation](https://arxiv.org/abs/2606.05403v1) | 2026-06-05T08:00:00+08:00 ～ 2026-06-05T09:00:00+08:00 | 3+2+3=8；exact-v1 与当前 claim 一致，owner=`PLATFORM-EVALUATION-SYSTEM` | 深入完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM`（[books/part-06-ai-infrastructure/66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)) |
| [When Evidence is Sparse: Weakly Supervised Early Failure Alerting in Dialogs and LLM-Agent Trajectories](https://arxiv.org/abs/2606.05414v1) | 2026-06-05T08:00:00+08:00 ～ 2026-06-05T09:00:00+08:00 | 2+2+2=6；exact-v1 与当前 claim 一致，owner=`PLATFORM-MONITORING` | 深入完成 | 仅报告：当前窗口上下文，不形成独立长期机制 |
| [Zero knowledge verification for frontier AI training is possible](https://arxiv.org/abs/2606.05433v1) | 2026-06-05T08:00:00+08:00 ～ 2026-06-05T09:00:00+08:00 | 3+3+2=8；exact-v1 与当前 claim 一致，owner=`PLATFORM-SECURITY` | 深入完成 | 已有覆盖：`PLATFORM-SECURITY`（[books/part-06-ai-infrastructure/72-security.md](../../../../books/part-06-ai-infrastructure/72-security.md)) |
| [ADK Arena: Evaluating Agent Development Kits via LLM-as-a-Developer](https://arxiv.org/abs/2606.05548v1) | 2026-06-05T08:00:00+08:00 ～ 2026-06-05T09:00:00+08:00 | 2+2+3=7；exact-v1 与当前 claim 一致，owner=`PLATFORM-EVALUATION-SYSTEM` | 深入完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM`（[books/part-06-ai-infrastructure/66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)) |
| [An Embarrassingly Simple Detector for Model Extraction Attacks in Large Language Model API Traffic](https://arxiv.org/abs/2606.05725v1) | 2026-06-05T08:00:00+08:00 ～ 2026-06-05T09:00:00+08:00 | 2+2+2=6；exact-v1 与当前 claim 一致，owner=`PLATFORM-SECURITY` | 深入完成 | 已有覆盖：`PLATFORM-SECURITY`（[books/part-06-ai-infrastructure/72-security.md](../../../../books/part-06-ai-infrastructure/72-security.md)) |
| [Membrane: A Self-Evolving Contrastive Safety Memory for LLM Agent Defense](https://arxiv.org/abs/2606.05743v1) | 2026-06-05T08:00:00+08:00 ～ 2026-06-05T09:00:00+08:00 | 2+2+2=6；exact-v1 与当前 claim 一致，owner=`PLATFORM-SECURITY` | 深入完成 | 已有覆盖：`PLATFORM-SECURITY`（[books/part-06-ai-infrastructure/72-security.md](../../../../books/part-06-ai-infrastructure/72-security.md)) |
| [SentinelRAG: Synthetic Sentinel Knowledge for RAG Database Copyright Protection](https://arxiv.org/abs/2606.05787v1) | 2026-06-05T08:00:00+08:00 ～ 2026-06-05T09:00:00+08:00 | 1+2+2=5；exact-v1 与当前 claim 一致，owner=`PLATFORM-SECURITY` | 深入完成 | 已有覆盖：`PLATFORM-SECURITY`（[books/part-06-ai-infrastructure/72-security.md](../../../../books/part-06-ai-infrastructure/72-security.md)) |
| [From Risk Classification to Action Plan Remediation: A Guardrail Feedback Driven Framework for LLM Agents](https://arxiv.org/abs/2606.05805v1) | 2026-06-05T08:00:00+08:00 ～ 2026-06-05T09:00:00+08:00 | 1+2+2=5；exact-v1 与当前 claim 一致，owner=`PLATFORM-SECURITY` | 深入完成 | 已有覆盖：`PLATFORM-SECURITY`（[books/part-06-ai-infrastructure/72-security.md](../../../../books/part-06-ai-infrastructure/72-security.md)) |
| [Steering Vectors are an Adversarial Attack Surface](https://arxiv.org/abs/2606.05958v1) | 2026-06-05T08:00:00+08:00 ～ 2026-06-05T09:00:00+08:00 | 2+2+2=6；exact-v1 与当前 claim 一致，owner=`PLATFORM-SECURITY` | 深入完成 | 已有覆盖：`PLATFORM-SECURITY`（[books/part-06-ai-infrastructure/72-security.md](../../../../books/part-06-ai-infrastructure/72-security.md)) |
| [The Self-Correction Illusion: Role Relabeling Gates Explicit Error Flagging in Large Language Models](https://arxiv.org/abs/2606.05976v1) | 2026-06-05T08:00:00+08:00 ～ 2026-06-05T09:00:00+08:00 | 2+2+3=7；exact-v1 与当前 claim 一致，owner=`AGENT-REFLECTION` | 深入完成 | 已有覆盖：`AGENT-REFLECTION`（[books/part-07-agent/80-reflection.md](../../../../books/part-07-agent/80-reflection.md)) |
| [HUSH-Bench: Measuring Memory-Use Boundaries for Sensitive History in Conversational Agents](https://arxiv.org/abs/2606.06055v1) | 2026-06-05T08:00:00+08:00 ～ 2026-06-05T09:00:00+08:00 | 2+2+3=7；exact-v1 与当前 claim 一致，owner=`AGENT-MEMORY` | 深入完成 | 已有覆盖：`AGENT-MEMORY`（[books/part-07-agent/77-memory.md](../../../../books/part-07-agent/77-memory.md)) |
| [From Reward-Hack Activations to Agentic Risk States: Context-Calibrated Mechanistic Monitoring in LLM Agents](https://arxiv.org/abs/2606.06223v1) | 2026-06-05T08:00:00+08:00 ～ 2026-06-05T09:00:00+08:00 | 2+2+2=6；exact-v1 与当前 claim 一致，owner=`PLATFORM-MONITORING` | 深入完成 | 已有覆盖：`PLATFORM-MONITORING`（[books/part-06-ai-infrastructure/67-monitoring.md](../../../../books/part-06-ai-infrastructure/67-monitoring.md)) |
| [From Failed Trajectories to Reliable LLM Agents: Diagnosing and Repairing Harness Flaws](https://arxiv.org/abs/2606.06324v1) | 2026-06-05T08:00:00+08:00 ～ 2026-06-05T09:00:00+08:00 | 3+3+3=9；exact-v1 与当前 claim 一致，owner=`AGENT-PLATFORM` | 深入完成 | 已有覆盖：`AGENT-PLATFORM`（[books/part-07-agent/84-agent-platform.md](../../../../books/part-07-agent/84-agent-platform.md)) |
| [WebMCP Tool Surface Poisoning: Runtime Manipulation Attacks on LLM Agents](https://arxiv.org/abs/2606.06387v1) | 2026-06-05T08:00:00+08:00 ～ 2026-06-05T09:00:00+08:00 | 2+3+3=8；exact-v1 与当前 claim 一致，owner=`AGENT-MCP` | 深入完成 | 已有覆盖：`AGENT-MCP`（[books/part-07-agent/83-mcp.md](../../../../books/part-07-agent/83-mcp.md)) |
| [Will the Agent Recuse, and Will It Stop? Measuring LLM-Agent Compliance with In-Band Governance Signals at the Access Door and Mid-Flight](https://arxiv.org/abs/2606.06460v1) | 2026-06-05T08:00:00+08:00 ～ 2026-06-05T09:00:00+08:00 | 3+3+3=9；exact-v1 与当前 claim 一致，owner=`PLATFORM-SECURITY` | 深入完成 | 已有覆盖：`PLATFORM-SECURITY`（[books/part-06-ai-infrastructure/72-security.md](../../../../books/part-06-ai-infrastructure/72-security.md)) |
| [BIDENT: Heterogeneous Operator-level Mapping for Efficient Edge Inference](https://arxiv.org/abs/2606.05271v1) | 2026-06-05T08:00:00+08:00 ～ 2026-06-05T09:00:00+08:00 | 2+2+2=6；exact-v1 与当前 claim 一致，owner=`INFER-TENSORRT-LLM` | 深入完成 | 仅报告：当前窗口上下文，不形成独立长期机制 |
| [SET: Stream-Event-Triggered Scheduling for Efficient CUDA Graph Pipelines](https://arxiv.org/abs/2606.05495v1) | 2026-06-05T08:00:00+08:00 ～ 2026-06-05T09:00:00+08:00 | 3+3+3=9；exact-v1 与当前 claim 一致，owner=`INFER-SCHEDULING` | 深入完成 | 已有覆盖：`INFER-SCHEDULING`（[books/part-05-inference-system/56-inference-scheduling.md](../../../../books/part-05-inference-system/56-inference-scheduling.md)) |
| [ColBERTSaR: Sparsified ColBERT Index via Product Quantization](https://arxiv.org/abs/2606.05568v1) | 2026-06-05T08:00:00+08:00 ～ 2026-06-05T09:00:00+08:00 | 2+2+2=6；exact-v1 与当前 claim 一致，owner=`AGENT-RAG` | 深入完成 | 已有覆盖：`AGENT-RAG`（[books/part-07-agent/76-rag.md](../../../../books/part-07-agent/76-rag.md)) |
| [AsyncWebRL: Efficient Asynchronous Reinforcement Learning for Multi-Step Visual Web Agents](https://arxiv.org/abs/2606.05597v1) | 2026-06-05T08:00:00+08:00 ～ 2026-06-05T09:00:00+08:00 | 2+3+2=7；exact-v1 与当前 claim 一致，owner=`TRAIN-DISTRIBUTED-TRAINING` | 深入完成 | 已有覆盖：`TRAIN-DISTRIBUTED-TRAINING`（[books/part-04-training-system/36-distributed-training.md](../../../../books/part-04-training-system/36-distributed-training.md)) |
| [AdaPLD: Adaptive Retrieval and Reuse for Efficient Model-Free Speculative Decoding](https://arxiv.org/abs/2606.05742v1) | 2026-06-05T08:00:00+08:00 ～ 2026-06-05T09:00:00+08:00 | 2+2+2=6；exact-v1 与当前 claim 一致，owner=`INFER-SPECULATIVE-DECODING` | 深入完成 | 已有覆盖：`INFER-SPECULATIVE-DECODING`（[books/part-05-inference-system/48-speculative-decoding.md](../../../../books/part-05-inference-system/48-speculative-decoding.md)) |
| [QCFuse: Query-Aware Cache Fusion via Compressed View for Efficient RAG Serving](https://arxiv.org/abs/2606.05875v1) | 2026-06-05T08:00:00+08:00 ～ 2026-06-05T09:00:00+08:00 | 2+2+2=6；exact-v1 与当前 claim 一致，owner=`INFER-KV-CACHE` | 深入完成 | 已有覆盖：`INFER-KV-CACHE`（[books/part-05-inference-system/45-why-kv-cache-speeds-up.md](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)) |
| [Beyond Greedy Chunking: SLO-Aware Sliding-Window Scheduling for LLM Inference](https://arxiv.org/abs/2606.05933v1) | 2026-06-05T08:00:00+08:00 ～ 2026-06-05T09:00:00+08:00 | 3+3+3=9；exact-v1 与当前 claim 一致，owner=`INFER-SCHEDULING` | 深入完成 | 已有覆盖：`INFER-SCHEDULING`（[books/part-05-inference-system/56-inference-scheduling.md](../../../../books/part-05-inference-system/56-inference-scheduling.md)) |
| [Demystifying NVSHMEM: A System-Level Analysis on Symmetric Memory and Device-Initiated Operations in GPU Communication](https://arxiv.org/abs/2606.05951v1) | 2026-06-05T08:00:00+08:00 ～ 2026-06-05T09:00:00+08:00 | 3+3+3=9；exact-v1 与当前 claim 一致，owner=`TRAIN-DISTRIBUTED-TRAINING` | 深入完成 | 已有覆盖：`TRAIN-DISTRIBUTED-TRAINING`（[books/part-04-training-system/36-distributed-training.md](../../../../books/part-04-training-system/36-distributed-training.md)) |
| [Learning to Route LLMs from Implicit Cost-Performance Preferences via Meta-Learning](https://arxiv.org/abs/2606.06178v1) | 2026-06-05T08:00:00+08:00 ～ 2026-06-05T09:00:00+08:00 | 2+2+2=6；exact-v1 与当前 claim 一致，owner=`INFER-SCHEDULING` | 深入完成 | 已有覆盖：`INFER-SCHEDULING`（[books/part-05-inference-system/56-inference-scheduling.md](../../../../books/part-05-inference-system/56-inference-scheduling.md)) |
| [RedKnot: Efficient Long-Context LLM Serving with Head-Aware KV Reuse and SegPagedAttention](https://arxiv.org/abs/2606.06256v1) | 2026-06-05T08:00:00+08:00 ～ 2026-06-05T09:00:00+08:00 | 3+3+3=9；exact-v1 与当前 claim 一致，owner=`INFER-KV-CACHE` | 深入完成 | 已有覆盖：`INFER-KV-CACHE`（[books/part-05-inference-system/45-why-kv-cache-speeds-up.md](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)) |
| [Tangram: Unlocking Non-Uniform KV Cache Compression for Efficient Multi-turn LLM Serving](https://arxiv.org/abs/2606.06302v1) | 2026-06-05T08:00:00+08:00 ～ 2026-06-05T09:00:00+08:00 | 2+2+2=6；exact-v1 与当前 claim 一致，owner=`INFER-KV-CACHE` | 深入完成 | 已有覆盖：`INFER-KV-CACHE`（[books/part-05-inference-system/45-why-kv-cache-speeds-up.md](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)) |
| [Vortex: Efficient and Programmable Sparse Attention Serving for AI Agents](https://arxiv.org/abs/2606.06453v1) | 2026-06-05T08:00:00+08:00 ～ 2026-06-05T09:00:00+08:00 | 3+3+2=8；exact-v1 与当前 claim 一致，owner=`INFER-PAGED-ATTENTION` | 深入完成 | 已有覆盖：`INFER-PAGED-ATTENTION`（[books/part-05-inference-system/47-pagedattention.md](../../../../books/part-05-inference-system/47-pagedattention.md)) |
| [You Only Index Once: Cross-Layer Sparse Attention with Shared Routing](https://arxiv.org/abs/2606.06467v1) | 2026-06-05T08:00:00+08:00 ～ 2026-06-05T09:00:00+08:00 | 2+2+2=6；exact-v1 与当前 claim 一致，owner=`INFER-PAGED-ATTENTION` | 深入完成 | 已有覆盖：`INFER-PAGED-ATTENTION`（[books/part-05-inference-system/47-pagedattention.md](../../../../books/part-05-inference-system/47-pagedattention.md)) |
| [What Should Agents Say? Action-state Communication for Efficient Multi-Agent Systems](https://arxiv.org/abs/2606.05304v1) | 2026-06-05T08:00:00+08:00 ～ 2026-06-05T09:00:00+08:00 | 3+3+3=9；exact-v1 与当前 claim 一致，owner=`AGENT-MULTI-AGENT` | 深入完成 | 已有覆盖：`AGENT-MULTI-AGENT`（[books/part-07-agent/82-multi-agent.md](../../../../books/part-07-agent/82-multi-agent.md)) |
| [Executable Schema Contracts: From Automatic Ingestion to Multi-Source Retrieval](https://arxiv.org/abs/2606.05415v1) | 2026-06-05T08:00:00+08:00 ～ 2026-06-05T09:00:00+08:00 | 3+3+2=8；exact-v1 与当前 claim 一致，owner=`PLATFORM-FOUNDATIONS` | 深入完成 | 已有覆盖：`PLATFORM-FOUNDATIONS`（[books/part-06-ai-infrastructure/57-what-is-ai-platform.md](../../../../books/part-06-ai-infrastructure/57-what-is-ai-platform.md)) |
| [Data Flow Control: Data Safety Policies for AI Agents](https://arxiv.org/abs/2606.05679v1) | 2026-06-05T08:00:00+08:00 ～ 2026-06-05T09:00:00+08:00 | 3+3+3=9；exact-v1 与当前 claim 一致，owner=`PLATFORM-SECURITY` | 深入完成 | 已有覆盖：`PLATFORM-SECURITY`（[books/part-06-ai-infrastructure/72-security.md](../../../../books/part-06-ai-infrastructure/72-security.md)) |
| [Entropy-Based Observability for AI Agent Behavior](https://arxiv.org/abs/2606.05872v1) | 2026-06-05T08:00:00+08:00 ～ 2026-06-05T09:00:00+08:00 | 1+2+2=5；exact-v1 与当前 claim 一致，owner=`PLATFORM-MONITORING` | 深入完成 | 已有覆盖：`PLATFORM-MONITORING`（[books/part-06-ai-infrastructure/67-monitoring.md](../../../../books/part-06-ai-infrastructure/67-monitoring.md)) |
| [EMBER: Efficient Memory via Budgeted Evidence Retention for Long-Horizon Agents](https://arxiv.org/abs/2606.05894v1) | 2026-06-05T08:00:00+08:00 ～ 2026-06-05T09:00:00+08:00 | 2+2+2=6；exact-v1 与当前 claim 一致，owner=`AGENT-MEMORY` | 深入完成 | 已有覆盖：`AGENT-MEMORY`（[books/part-07-agent/77-memory.md](../../../../books/part-07-agent/77-memory.md)) |
| [IA-RAG: Interval-Algebra-Driven Temporal Reasoning for Dynamic Knowledge Retrieval](https://arxiv.org/abs/2606.06044v1) | 2026-06-05T08:00:00+08:00 ～ 2026-06-05T09:00:00+08:00 | 2+2+3=7；exact-v1 与当前 claim 一致，owner=`AGENT-RAG` | 深入完成 | 已有覆盖：`AGENT-RAG`（[books/part-07-agent/76-rag.md](../../../../books/part-07-agent/76-rag.md)) |
| [Beyond Similarity: Trustworthy Memory Search for Personal AI Agents](https://arxiv.org/abs/2606.06054v1) | 2026-06-05T08:00:00+08:00 ～ 2026-06-05T09:00:00+08:00 | 2+2+3=7；exact-v1 与当前 claim 一致，owner=`AGENT-MEMORY` | 深入完成 | 已有覆盖：`AGENT-MEMORY`（[books/part-07-agent/77-memory.md](../../../../books/part-07-agent/77-memory.md)) |
| [Beyond Semantic Organization: Memory as Execution State Management for Long-Horizon Agents](https://arxiv.org/abs/2606.06090v1) | 2026-06-05T08:00:00+08:00 ～ 2026-06-05T09:00:00+08:00 | 3+3+3=9；exact-v1 与当前 claim 一致，owner=`AGENT-MEMORY` | 深入完成 | 已有覆盖：`AGENT-MEMORY`（[books/part-07-agent/77-memory.md](../../../../books/part-07-agent/77-memory.md)) |
| [TOKI: A Bitemporal Operator Algebra for Contradiction Resolution in LLM-Agent Persistent Memory](https://arxiv.org/abs/2606.06240v1) | 2026-06-05T08:00:00+08:00 ～ 2026-06-05T09:00:00+08:00 | 3+3+3=9；exact-v1 与当前 claim 一致，owner=`AGENT-MEMORY` | 深入完成 | 已有覆盖：`AGENT-MEMORY`（[books/part-07-agent/77-memory.md](../../../../books/part-07-agent/77-memory.md)) |
| [ToolChoiceConfusion: Causal Minimal Tool Filtering for Reliable LLM Agents](https://arxiv.org/abs/2606.06284v1) | 2026-06-05T08:00:00+08:00 ～ 2026-06-05T09:00:00+08:00 | 2+2+3=7；exact-v1 与当前 claim 一致，owner=`AGENT-TOOL-CALLING` | 深入完成 | 已有覆盖：`AGENT-TOOL-CALLING`（[books/part-07-agent/78-tool-calling.md](../../../../books/part-07-agent/78-tool-calling.md)) |
| [TokenMizer: Graph-Structured Session Memory for Long-Horizon LLM Context Management](https://arxiv.org/abs/2606.06337v1) | 2026-06-05T08:00:00+08:00 ～ 2026-06-05T09:00:00+08:00 | 2+2+2=6；exact-v1 与当前 claim 一致，owner=`AGENT-MEMORY` | 深入完成 | 已有覆盖：`AGENT-MEMORY`（[books/part-07-agent/77-memory.md](../../../../books/part-07-agent/77-memory.md)) |
| [Agent Memory: Characterization and System Implications of Stateful Long-Horizon Workloads](https://arxiv.org/abs/2606.06448v1) | 2026-06-05T08:00:00+08:00 ～ 2026-06-05T09:00:00+08:00 | 3+3+3=9；exact-v1 与当前 claim 一致，owner=`AGENT-MEMORY` | 深入完成 | 已有覆盖：`AGENT-MEMORY`（[books/part-07-agent/77-memory.md](../../../../books/part-07-agent/77-memory.md)) |
| [Autoregressive Diffusion World Models for Off-Policy Evaluation of LLM Agents](https://arxiv.org/abs/2606.05558v1) | 2026-06-05T08:00:00+08:00 ～ 2026-06-05T09:00:00+08:00 | 2+2+2=6；exact-v1 与当前 claim 一致，owner=`PLATFORM-EVALUATION-SYSTEM` | 深入完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM`（[books/part-06-ai-infrastructure/66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)) |
| [CLaaS: Continual learning as a service for sample efficient online learning](https://arxiv.org/abs/2606.05559v1) | 2026-06-05T08:00:00+08:00 ～ 2026-06-05T09:00:00+08:00 | 2+2+2=6；exact-v1 与当前 claim 一致，owner=`AGENT-PLATFORM` | 深入完成 | 已有覆盖：`AGENT-PLATFORM`（[books/part-07-agent/84-agent-platform.md](../../../../books/part-07-agent/84-agent-platform.md)) |
| [Statistical Priors for Implicit Preferences: Decoupling Skill Selection as a Local Harness in Personal Agents](https://arxiv.org/abs/2606.05828v1) | 2026-06-05T08:00:00+08:00 ～ 2026-06-05T09:00:00+08:00 | 1+2+2=5；exact-v1 与当前 claim 一致，owner=`AGENT-PLATFORM` | 深入完成 | 已有覆盖：`AGENT-PLATFORM`（[books/part-07-agent/84-agent-platform.md](../../../../books/part-07-agent/84-agent-platform.md)) |
| [The Evaluation Blind Spot: A Stereological Theory of Benchmark Coverage for Large Language Models](https://arxiv.org/abs/2606.05169v1) | 2026-06-05T08:00:00+08:00 ～ 2026-06-05T09:00:00+08:00 | 2+2+2=6；完整题摘与 exact-v1 正文给出长期合同增量，owner=`PLATFORM-EVALUATION-SYSTEM` | 标准完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM`；正文锚点[“从‘已见切片均值’到 Blind-spot Mass”与“平均值、切片与不确定性”](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [ERRORQUAKE: Heavy-Tailed Error Severity Distributions in Open-Weight Large Language Models](https://arxiv.org/abs/2606.05170v1) | 2026-06-05T08:00:00+08:00 ～ 2026-06-05T09:00:00+08:00 | 2+2+2=6；完整题摘与 exact-v1 正文给出长期合同增量，owner=`PLATFORM-EVALUATION-SYSTEM` | 标准完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM`（[books/part-06-ai-infrastructure/66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)) |
| [AppAgent-Claw: CLI Is All You Need for GUI Automation](https://arxiv.org/abs/2606.05171v1) | 2026-06-05T08:00:00+08:00 ～ 2026-06-05T09:00:00+08:00 | 2+2+2=6；完整题摘与 exact-v1 正文给出长期合同增量，owner=`AGENT-TOOL-CALLING` | 标准完成 | 已有覆盖：`AGENT-TOOL-CALLING`（[books/part-07-agent/78-tool-calling.md](../../../../books/part-07-agent/78-tool-calling.md)) |
| [LANTERN: Layered Archival and Temporal Episodic Retrieval Network for Long-Context LLM Conversations](https://arxiv.org/abs/2606.05182v1) | 2026-06-05T08:00:00+08:00 ～ 2026-06-05T09:00:00+08:00 | 2+2+2=6；完整题摘与 exact-v1 正文给出长期合同增量，owner=`AGENT-MEMORY` | 标准完成 | 已有覆盖：`AGENT-MEMORY`（[books/part-07-agent/77-memory.md](../../../../books/part-07-agent/77-memory.md)) |
| [State commitment learning: training language models to distinguish computation from memory](https://arxiv.org/abs/2606.05201v1) | 2026-06-05T08:00:00+08:00 ～ 2026-06-05T09:00:00+08:00 | 2+2+2=6；完整题摘与 exact-v1 正文给出长期合同增量，owner=`AGENT-MEMORY` | 标准完成 | 已有覆盖：`AGENT-MEMORY`（[books/part-07-agent/77-memory.md](../../../../books/part-07-agent/77-memory.md)) |
| [Domain-Conditioned Safety in Frontier Computer-Using Agents: A 793-Episode Browser Benchmark, a Coding-Domain Cross-Reference, and a Reproducibility Audit of Recent Red-Teaming](https://arxiv.org/abs/2606.05233v1) | 2026-06-05T08:00:00+08:00 ～ 2026-06-05T09:00:00+08:00 | 2+2+2=6；完整题摘与 exact-v1 正文给出长期合同增量，owner=`PLATFORM-SECURITY` | 标准完成 | 已有覆盖：`PLATFORM-SECURITY`（[books/part-06-ai-infrastructure/72-security.md](../../../../books/part-06-ai-infrastructure/72-security.md)) |
| [DeployBench: Benchmarking LLM Agents for Research Artifact Deployment](https://arxiv.org/abs/2606.05238v1) | 2026-06-05T08:00:00+08:00 ～ 2026-06-05T09:00:00+08:00 | 2+2+2=6；完整题摘与 exact-v1 正文给出长期合同增量，owner=`PLATFORM-EVALUATION-SYSTEM` | 标准完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM`（[books/part-06-ai-infrastructure/66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)) |
| [SentinelBench: A Benchmark for Long-Running Monitoring Agents](https://arxiv.org/abs/2606.05342v1) | 2026-06-05T08:00:00+08:00 ～ 2026-06-05T09:00:00+08:00 | 2+2+2=6；完整题摘与 exact-v1 正文给出长期合同增量，owner=`AGENT-PLATFORM` | 标准完成 | 已有覆盖：`AGENT-PLATFORM`（[books/part-07-agent/84-agent-platform.md](../../../../books/part-07-agent/84-agent-platform.md)) |
| [Ahoy: LLMs Enacting Multiagent Interaction Protocols](https://arxiv.org/abs/2606.05390v1) | 2026-06-05T08:00:00+08:00 ～ 2026-06-05T09:00:00+08:00 | 2+2+2=6；完整题摘与 exact-v1 正文给出长期合同增量，owner=`AGENT-MULTI-AGENT` | 标准完成 | 已有覆盖：`AGENT-MULTI-AGENT`（[books/part-07-agent/82-multi-agent.md](../../../../books/part-07-agent/82-multi-agent.md)) |
| [Agents' Last Exam](https://arxiv.org/abs/2606.05405v1) | 2026-06-05T08:00:00+08:00 ～ 2026-06-05T09:00:00+08:00 | 2+2+2=6；完整题摘与 exact-v1 正文给出长期合同增量，owner=`PLATFORM-EVALUATION-SYSTEM` | 标准完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM`（[books/part-06-ai-infrastructure/66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)) |
| [The Granularity Gap: A Multi-Dimensional Cross-Generational Audit of Sycophancy in Gemini Models](https://arxiv.org/abs/2606.05183v1) | 2026-06-05T08:00:00+08:00 ～ 2026-06-05T09:00:00+08:00 | 2+2+2=6；完整题摘与 exact-v1 正文给出长期合同增量，owner=`PLATFORM-EVALUATION-SYSTEM` | 标准完成 | 仅报告：当前窗口上下文，不形成独立长期机制 |
| [Learned Subspace Compression for Communication-Efficient Pipeline Parallelism](https://arxiv.org/abs/2606.05484v1) | 2026-06-05T08:00:00+08:00 ～ 2026-06-05T09:00:00+08:00 | 2+2+2=6；完整题摘与 exact-v1 正文给出长期合同增量，owner=`TRAIN-DISTRIBUTED-TRAINING` | 标准完成 | 已有覆盖：`TRAIN-DISTRIBUTED-TRAINING`（[books/part-04-training-system/36-distributed-training.md](../../../../books/part-04-training-system/36-distributed-training.md)) |
| [AdaPlanBench: Evaluating Adaptive Planning in Large Language Model Agents under World and User Constraints](https://arxiv.org/abs/2606.05622v1) | 2026-06-05T08:00:00+08:00 ～ 2026-06-05T09:00:00+08:00 | 2+2+2=6；完整题摘与 exact-v1 正文给出长期合同增量，owner=`PLATFORM-EVALUATION-SYSTEM` | 标准完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM`（[books/part-06-ai-infrastructure/66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)) |
| [Do More Agents Help? Controlled and Protocol-Aligned Evaluation of LLM Agent Workflows](https://arxiv.org/abs/2606.05670v1) | 2026-06-05T08:00:00+08:00 ～ 2026-06-05T09:00:00+08:00 | 2+2+2=6；完整题摘与 exact-v1 正文给出长期合同增量，owner=`PLATFORM-EVALUATION-SYSTEM` | 标准完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM`（[books/part-06-ai-infrastructure/66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)) |
| [AdaMEM: Test-Time Adaptive Memory for Language Agents](https://arxiv.org/abs/2606.05684v1) | 2026-06-05T08:00:00+08:00 ～ 2026-06-05T09:00:00+08:00 | 2+2+2=6；完整题摘与 exact-v1 正文给出长期合同增量，owner=`AGENT-MEMORY` | 标准完成 | 已有覆盖：`AGENT-MEMORY`（[books/part-07-agent/77-memory.md](../../../../books/part-07-agent/77-memory.md)) |
| [SubtleMemory: A Benchmark for Fine-Grained Relational Memory Discrimination in Long-Horizon AI Agents](https://arxiv.org/abs/2606.05761v1) | 2026-06-05T08:00:00+08:00 ～ 2026-06-05T09:00:00+08:00 | 2+2+2=6；完整题摘与 exact-v1 正文给出长期合同增量，owner=`AGENT-MEMORY` | 标准完成 | 已有覆盖：`AGENT-MEMORY`（[books/part-07-agent/77-memory.md](../../../../books/part-07-agent/77-memory.md)) |
| [When Tools Fail: Benchmarking Dynamic Replanning and Anomaly Recovery in LLM Agents](https://arxiv.org/abs/2606.05806v1) | 2026-06-05T08:00:00+08:00 ～ 2026-06-05T09:00:00+08:00 | 2+2+2=6；完整题摘与 exact-v1 正文给出长期合同增量，owner=`AGENT-TOOL-CALLING` | 标准完成 | 已有覆盖：`AGENT-TOOL-CALLING`（[books/part-07-agent/78-tool-calling.md](../../../../books/part-07-agent/78-tool-calling.md)) |
| [Asuka-Bench: Benchmarking Code Agents on Underspecified User Intent and Multi-Round Refinement](https://arxiv.org/abs/2606.05920v1) | 2026-06-05T08:00:00+08:00 ～ 2026-06-05T09:00:00+08:00 | 2+2+2=6；完整题摘与 exact-v1 正文给出长期合同增量，owner=`PLATFORM-EVALUATION-SYSTEM` | 标准完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM`（[books/part-06-ai-infrastructure/66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)) |
| [Evolving Agents in the Dark: Retrospective Harness Optimization via Self-Preference](https://arxiv.org/abs/2606.05922v1) | 2026-06-05T08:00:00+08:00 ～ 2026-06-05T09:00:00+08:00 | 2+2+2=6；完整题摘与 exact-v1 正文给出长期合同增量，owner=`AGENT-PLATFORM` | 标准完成 | 已有覆盖：`AGENT-PLATFORM`（[books/part-07-agent/84-agent-platform.md](../../../../books/part-07-agent/84-agent-platform.md)) |
| [Epistemic Injustice in Language Models: An Audit of Pretraining Filters and Guardrails](https://arxiv.org/abs/2606.05936v1) | 2026-06-05T08:00:00+08:00 ～ 2026-06-05T09:00:00+08:00 | 2+2+2=6；完整题摘与 exact-v1 正文给出长期合同增量，owner=`PLATFORM-SECURITY` | 标准完成 | 已有覆盖：`PLATFORM-SECURITY`（[books/part-06-ai-infrastructure/72-security.md](../../../../books/part-06-ai-infrastructure/72-security.md)) |
| [Dense Contexts Are Hard Contexts: Lexical Density Limits Effective Context in LLMs](https://arxiv.org/abs/2606.06203v1) | 2026-06-05T08:00:00+08:00 ～ 2026-06-05T09:00:00+08:00 | 2+2+2=6；完整题摘与 exact-v1 正文给出长期合同增量，owner=`MODEL-LONG-CONTEXT` | 深入完成 | 整合：`MODEL-LONG-CONTEXT`（[Ch22「相同 Token Length 仍可能承载不同 Information Load」](../../../../books/part-02-model/22-long-context.md)） |
| [LLMs Can Leak Training Data But Do They Want To? A Propensity-Aware Evaluation of Memorization in LLMs](https://arxiv.org/abs/2606.06286v1) | 2026-06-05T08:00:00+08:00 ～ 2026-06-05T09:00:00+08:00 | 2+2+2=6；完整题摘与 exact-v1 正文给出长期合同增量，owner=`PLATFORM-SECURITY` | 标准完成 | 已有覆盖：`PLATFORM-SECURITY`（[books/part-06-ai-infrastructure/72-security.md](../../../../books/part-06-ai-infrastructure/72-security.md)) |
| [CollabSim: A CSCW-Grounded Methodology for Investigating Collaborative Competence of LLM Agents through Controlled Multi-Agent Experiments](https://arxiv.org/abs/2606.06399v1) | 2026-06-05T08:00:00+08:00 ～ 2026-06-05T09:00:00+08:00 | 2+2+2=6；完整题摘与 exact-v1 正文给出长期合同增量，owner=`PLATFORM-EVALUATION-SYSTEM` | 标准完成 | 仅报告：当前窗口上下文，不形成独立长期机制 |

候选分母最终冻结为 72；上表覆盖 48 个 prior、23 个 closure-recovered arXiv family 与 1 个厂商 release family。最终 disposition：67 项已有覆盖、4 项仅报告、1 项已整合、0 项结构候选、0 项暂缓。旧 8 项 Integrate 均依据 Review notes 前正文重判 Existing；2606.06203 的 lexical-density 增量已写入 Ch22 并通过 post-write 反例审计。

## 4. 证据与知识整合

### [Kimi Code 0.10.0 / 0.10.1](https://github.com/MoonshotAI/kimi-code/releases/tag/%40moonshot-ai/kimi-code%400.10.0)

官方 GitHub Release 的 `published_at` 分别为 `2026-06-04T13:46:30Z` 与 `2026-06-04T17:35:34Z`。0.10.0 暴露 goal queue 与配置、session reload/toggle，0.10.1 是同一 Source Family 的紧随修补；这些记录证明版本接口，不证明 queue 的持久化、exactly-once、故障恢复或生产可靠性。`AGENT-WORKFLOW` 已覆盖 versioned workflow state、配置快照、恢复与提交边界，因此不新增正文。

归档保留旧 exact-v1 的 Method/Evaluation/Limitations；只在 identity/claim 不变时复用，旧 Books comparison 不继承。独立 audit 已把八项旧 `Integrate` 全部改判 `已有覆盖`：当前 Review notes 前正文已分别承载 message/state ownership、security data-flow enforcement、SLO-aware scheduling、remote-memory collective、bitemporal memory 与 sparse-attention execution contract。对 23 项恢复候选继续做反例审计后，2606.05169 改为 Existing Coverage，2606.06203 的新增量已整合进 Ch22；因此 new Integrate = 1，正文缺口 = 0。以下 23 项为本轮新恢复 Candidate 的同标题、同 URL Evidence；48 个 prior 的完整审阅继续由 [V2_1_EVIDENCE_ARCHIVE.md](../_sources/daily-20260605/V2_1_EVIDENCE_ARCHIVE.md) 提供。

### [The Evaluation Blind Spot: A Stereological Theory of Benchmark Coverage for Large Language Models](https://arxiv.org/abs/2606.05169v1)

`arXiv:2606.05169v1`；正文定位：The curse of benchmark dimensionality.；Corollary: benchmark domination ⇏ \not\Rightarrow capability domination.。用有效维度、不可见 capability profile 与稳定 benchmark core 修正“排行榜分数等于覆盖”的评测结论。 Evaluation：Counterfactual validation.；Evaluation monoculture.。 Limitations：8 Discussion；Takeaways and limitations.；不外推到未列出的模型、任务、硬件、并发或生产 SLO。 Books：`已有覆盖`，owner=`PLATFORM-EVALUATION-SYSTEM`；正文锚点“从‘已见切片均值’到 Blind-spot Mass”已经把已采样均值与未覆盖 capability/state mass 分开，“平均值、切片与不确定性”又限定 slice coverage 与 release authority。该论文只增加 stereological 解释框架，不改变现有长期合同。完整记录见 [V3_EVIDENCE_RECOVERED.md](../_sources/daily-20260605/V3_EVIDENCE_RECOVERED.md)。

### [ERRORQUAKE: Heavy-Tailed Error Severity Distributions in Open-Weight Large Language Models](https://arxiv.org/abs/2606.05170v1)

`arXiv:2606.05170v1`；正文定位：2 Method；Query benchmark.。证明 accuracy 与 error-severity distribution 不可约，要求发布时同时报告尾部严重度。 Evaluation：Human validation.；Severity-aware evaluation.。 Limitations：7 Discussion；8 Limitations and misuse；不外推到未列出的模型、任务、硬件、并发或生产 SLO。 Books：`已有覆盖`，owner=`PLATFORM-EVALUATION-SYSTEM`；当前正文已覆盖相应 state/control/evaluation contract，new Integrate=0。 完整记录见 [V3_EVIDENCE_RECOVERED.md](../_sources/daily-20260605/V3_EVIDENCE_RECOVERED.md)。

### [AppAgent-Claw: CLI Is All You Need for GUI Automation](https://arxiv.org/abs/2606.05171v1)

`arXiv:2606.05171v1`；正文定位：3 Method；3.1 System Overview。把 GUI workflow 固化为 record-once/replay-many skill，并用分层定位与 validation-coupled execution 取代运行时推理。 Evaluation：3.8 Execution, Validation, and Observability。 Limitations：5 Discussion；6 Conclusion；不外推到未列出的模型、任务、硬件、并发或生产 SLO。 Books：`已有覆盖`，owner=`AGENT-TOOL-CALLING`；当前正文已覆盖相应 state/control/evaluation contract，new Integrate=0。 完整记录见 [V3_EVIDENCE_RECOVERED.md](../_sources/daily-20260605/V3_EVIDENCE_RECOVERED.md)。

### [LANTERN: Layered Archival and Temporal Episodic Retrieval Network for Long-Context LLM Conversations](https://arxiv.org/abs/2606.05182v1)

`arXiv:2606.05182v1`；正文定位：3 Method。在 compaction 前归档每轮，并以零 LLM-call hybrid retrieval 恢复状态；明确延迟与跨模型边界。 Evaluation：4.4 Evaluation Metrics；Human validation of LLM judge.。 Limitations：7 Discussion；8 Limitations；不外推到未列出的模型、任务、硬件、并发或生产 SLO。 Books：`已有覆盖`，owner=`AGENT-MEMORY`；当前正文已覆盖相应 state/control/evaluation contract，new Integrate=0。 完整记录见 [V3_EVIDENCE_RECOVERED.md](../_sources/daily-20260605/V3_EVIDENCE_RECOVERED.md)。

### [State commitment learning: training language models to distinguish computation from memory](https://arxiv.org/abs/2606.05201v1)

`arXiv:2606.05201v1`；正文定位：1.3 Method overview；3 Method。显式区分临时 computation 与 persistent committed state，以 counterfactual erasure 定义可训练、可验收的状态合同。 Evaluation：4.3 Experiment 1: main results；4.4 Experiment 2: training-objective ablation。 Limitations：6 Discussion；8 Limitations；不外推到未列出的模型、任务、硬件、并发或生产 SLO。 Books：`已有覆盖`，owner=`AGENT-MEMORY`；当前正文已覆盖相应 state/control/evaluation contract，new Integrate=0。 完整记录见 [V3_EVIDENCE_RECOVERED.md](../_sources/daily-20260605/V3_EVIDENCE_RECOVERED.md)。

### [Domain-Conditioned Safety in Frontier Computer-Using Agents: A 793-Episode Browser Benchmark, a Coding-Domain Cross-Reference, and a Reproducibility Audit of Recent Red-Teaming](https://arxiv.org/abs/2606.05233v1)

`arXiv:2606.05233v1`；正文定位：2 The CUA-HandCrafted Benchmark；Appendix A Benchmark Detail: Sites, Channels, Canary, Release。跨 browser/coding surface 复现 prompt injection，直接推翻把旧 ASR 外推到 frontier CUA 的安全结论。 Evaluation：3 Results；Results.。 Limitations：6 Discussion: RL Optimization Is the Gap；7 Limitations；不外推到未列出的模型、任务、硬件、并发或生产 SLO。 Books：`已有覆盖`，owner=`PLATFORM-SECURITY`；当前正文已覆盖相应 state/control/evaluation contract，new Integrate=0。 完整记录见 [V3_EVIDENCE_RECOVERED.md](../_sources/daily-20260605/V3_EVIDENCE_RECOVERED.md)。

### [DeployBench: Benchmarking LLM Agents for Research Artifact Deployment](https://arxiv.org/abs/2606.05238v1)

`arXiv:2606.05238v1`；正文定位：3.1 Task Formulation；3.2 Benchmark Construction。用从 fresh machine 到隐藏实验验证的完整 pipeline 定义 research artifact deployment release gate，并定位 self-stop 错误。 Evaluation：3.3 Evaluation；4 Experiment。 Limitations：6 Conclusion；不外推到未列出的模型、任务、硬件、并发或生产 SLO。 Books：`已有覆盖`，owner=`PLATFORM-EVALUATION-SYSTEM`；当前正文已覆盖相应 state/control/evaluation contract，new Integrate=0。 完整记录见 [V3_EVIDENCE_RECOVERED.md](../_sources/daily-20260605/V3_EVIDENCE_RECOVERED.md)。

### [SentinelBench: A Benchmark for Long-Running Monitoring Agents](https://arxiv.org/abs/2606.05342v1)

`arXiv:2606.05342v1`；正文定位：2.3 Benchmark Tasks；3 Evaluation Protocol and Metrics。把长期 Agent 的持续轮询改写为 event monitoring；同时量化 completion、reaction time 与 resource use。 Evaluation：2.3.3 Task Validation；3 Evaluation Protocol and Metrics。 Limitations：5 Discussion and Limitations；7 Conclusion；不外推到未列出的模型、任务、硬件、并发或生产 SLO。 Books：`已有覆盖`，owner=`AGENT-PLATFORM`；当前正文已覆盖相应 state/control/evaluation contract，new Integrate=0。 完整记录见 [V3_EVIDENCE_RECOVERED.md](../_sources/daily-20260605/V3_EVIDENCE_RECOVERED.md)。

### [Ahoy: LLMs Enacting Multiagent Interaction Protocols](https://arxiv.org/abs/2606.05390v1)

`arXiv:2606.05390v1`；正文定位：2.2 Implementing Protocol-Based Agents；3 Architecture。让 Agent 动态选择并并发 enact declarative interaction protocol，改变多 Agent 控制协议 ownership。 Evaluation：5 Evaluation。 Limitations：未设独立 Limitations 标题；以 exact-v1 的 Conclusion 和实验设置为 claim 边界；不外推到未列出的模型、任务、硬件、并发或生产 SLO。 Books：`已有覆盖`，owner=`AGENT-MULTI-AGENT`；当前正文已覆盖相应 state/control/evaluation contract，new Integrate=0。 完整记录见 [V3_EVIDENCE_RECOVERED.md](../_sources/daily-20260605/V3_EVIDENCE_RECOVERED.md)。

### [Agents' Last Exam](https://arxiv.org/abs/2606.05405v1)

`arXiv:2606.05405v1`；正文定位：2 Benchmark Design and Dataset Construction；2.1 Benchmark Design Principles: What Tasks are We Looking for?。用可验证、长期、经济真实 workflow 与 living task pool 替代静态短 benchmark 的发布评测合同。 Evaluation：3 Evaluation Pipeline；3.3 Evaluation Modes。 Limitations：6 Conclusion；不外推到未列出的模型、任务、硬件、并发或生产 SLO。 Books：`已有覆盖`，owner=`PLATFORM-EVALUATION-SYSTEM`；当前正文已覆盖相应 state/control/evaluation contract，new Integrate=0。 完整记录见 [V3_EVIDENCE_RECOVERED.md](../_sources/daily-20260605/V3_EVIDENCE_RECOVERED.md)。

### [The Granularity Gap: A Multi-Dimensional Cross-Generational Audit of Sycophancy in Gemini Models](https://arxiv.org/abs/2606.05183v1)

`arXiv:2606.05183v1`；正文定位：2.1. Framework Implementation；2.3. Experimental Design。证明 refuse/comply 不能代理 sycophancy severity，给 safety evaluation 的粒度与 judge 边界。 Evaluation：2.5. Evaluation Instruments；2.6. Human-Centered Validation。 Limitations：8. Discussion；9. Limitations；不外推到未列出的模型、任务、硬件、并发或生产 SLO。 Books：`Only report`；该项保留为当前窗口的评测/方法论上下文，不形成新的长期知识 owner。 完整记录见 [V3_EVIDENCE_RECOVERED.md](../_sources/daily-20260605/V3_EVIDENCE_RECOVERED.md)。

### [Learned Subspace Compression for Communication-Efficient Pipeline Parallelism](https://arxiv.org/abs/2606.05484v1)

`arXiv:2606.05484v1`；正文定位：1 Introduction；2 Related works。对 pipeline stage activation 建立可学习正交压缩、token anchor 与 streaming codebook sync 的通信合同。 Evaluation：3.4 Empirical Validation；4.2 Main Results。 Limitations：5 Conclusion；不外推到未列出的模型、任务、硬件、并发或生产 SLO。 Books：`已有覆盖`，owner=`TRAIN-DISTRIBUTED-TRAINING`；当前正文已覆盖相应 state/control/evaluation contract，new Integrate=0。 完整记录见 [V3_EVIDENCE_RECOVERED.md](../_sources/daily-20260605/V3_EVIDENCE_RECOVERED.md)。

### [AdaPlanBench: Evaluating Adaptive Planning in Large Language Model Agents under World and User Constraints](https://arxiv.org/abs/2606.05622v1)

`arXiv:2606.05622v1`；正文定位：E.1 Benchmark Traits Elaboration。用逐步揭示 world/user constraint 的多轮 protocol 测试状态累积与 replanning，而不是完整 prompt 的一次性规划。 Evaluation：3 Experiment；3.1 Experiment Setup。 Limitations：5 Conclusion；6 Limitations；不外推到未列出的模型、任务、硬件、并发或生产 SLO。 Books：`已有覆盖`，owner=`PLATFORM-EVALUATION-SYSTEM`；当前正文已覆盖相应 state/control/evaluation contract，new Integrate=0。 完整记录见 [V3_EVIDENCE_RECOVERED.md](../_sources/daily-20260605/V3_EVIDENCE_RECOVERED.md)。

### [Do More Agents Help? Controlled and Protocol-Aligned Evaluation of LLM Agent Workflows](https://arxiv.org/abs/2606.05670v1)

`arXiv:2606.05670v1`；正文定位：2.1 Agent Workflow Design；3 Evaluation Protocol。将 single/fixed/evolving MAS 置于统一 loader、tool、answer、usage 与 trajectory logging substrate，修正“更多 Agent 更好”的比较。 Evaluation：2.2 Agent Evaluation Frameworks；3 Evaluation Protocol。 Limitations：5 Discussion；6 Conclusion；不外推到未列出的模型、任务、硬件、并发或生产 SLO。 Books：`已有覆盖`，owner=`PLATFORM-EVALUATION-SYSTEM`；当前正文已覆盖相应 state/control/evaluation contract，new Integrate=0。 完整记录见 [V3_EVIDENCE_RECOVERED.md](../_sources/daily-20260605/V3_EVIDENCE_RECOVERED.md)。

### [AdaMEM: Test-Time Adaptive Memory for Language Agents](https://arxiv.org/abs/2606.05684v1)

`arXiv:2606.05684v1`；正文定位：1 Introduction；2 Related Work。分离 offline long-term trajectory 与在线 short-term strategy memory，明确 post-deployment adaptation 的状态更新边界。 Evaluation：4.2 Main Results；Appendix D Efficiency Analysis。 Limitations：5 Conclusion；Appendix E Limitations；不外推到未列出的模型、任务、硬件、并发或生产 SLO。 Books：`已有覆盖`，owner=`AGENT-MEMORY`；当前正文已覆盖相应 state/control/evaluation contract，new Integrate=0。 完整记录见 [V3_EVIDENCE_RECOVERED.md](../_sources/daily-20260605/V3_EVIDENCE_RECOVERED.md)。

### [SubtleMemory: A Benchmark for Fine-Grained Relational Memory Discrimination in Long-Horizon AI Agents](https://arxiv.org/abs/2606.05761v1)

`arXiv:2606.05761v1`；正文定位：1 Introduction；2 Methodology。将长期 memory 分成 preservation、retrieval、downstream reasoning，并显式测试 complementary/nuanced/contradictory 关系。 Evaluation：2.2 Evaluation Overview and Taxonomy；3.3 Main Results。 Limitations：4 Discussion；6 Conclusion；不外推到未列出的模型、任务、硬件、并发或生产 SLO。 Books：`已有覆盖`，owner=`AGENT-MEMORY`；当前正文已覆盖相应 state/control/evaluation contract，new Integrate=0。 完整记录见 [V3_EVIDENCE_RECOVERED.md](../_sources/daily-20260605/V3_EVIDENCE_RECOVERED.md)。

### [When Tools Fail: Benchmarking Dynamic Replanning and Anomaly Recovery in LLM Agents](https://arxiv.org/abs/2606.05806v1)

`arXiv:2606.05806v1`；正文定位：3 The ToolMaze Framework；3.5 Evaluation Framework and Metrics。用 DAG topology 与显式/隐式、瞬时/永久 tool failure 定义 fault-recovery contract 和 PRR。 Evaluation：2.2 Robustness and Risk Evaluation；3.2 The 𝒞 × 𝒫 \mathcal{C}\times\mathcal{P} Evaluation Matrix。 Limitations：5 Conclusion；Limitations；不外推到未列出的模型、任务、硬件、并发或生产 SLO。 Books：`已有覆盖`，owner=`AGENT-TOOL-CALLING`；当前正文已覆盖相应 state/control/evaluation contract，new Integrate=0。 完整记录见 [V3_EVIDENCE_RECOVERED.md](../_sources/daily-20260605/V3_EVIDENCE_RECOVERED.md)。

### [Asuka-Bench: Benchmarking Code Agents on Underspecified User Intent and Multi-Round Refinement](https://arxiv.org/abs/2606.05920v1)

`arXiv:2606.05920v1`；正文定位：3.1 Evaluation Framework；DAG-Based Evaluation Protocol。把 underspecified intent、deployed browser test 与用户反馈纳入多轮代码 Agent 验收，而不是一次性完整规格。 Evaluation：3.1 Evaluation Framework；Automated Evaluation。 Limitations：6 Conclusion；Limitations；不外推到未列出的模型、任务、硬件、并发或生产 SLO。 Books：`已有覆盖`，owner=`PLATFORM-EVALUATION-SYSTEM`；当前正文已覆盖相应 state/control/evaluation contract，new Integrate=0。 完整记录见 [V3_EVIDENCE_RECOVERED.md](../_sources/daily-20260605/V3_EVIDENCE_RECOVERED.md)。

### [Evolving Agents in the Dark: Retrospective Harness Optimization via Self-Preference](https://arxiv.org/abs/2606.05922v1)

`arXiv:2606.05922v1`；正文定位：G.2 Per-Method Decomposition。以历史轨迹、coreset、self-validation 与 pairwise preference 更新 harness，明确无外部标签下的控制状态演化。 Evaluation：5 Experiments and Results；5.3 Comparison with Validation-Feedback Optimization。 Limitations：6 Discussion；7 Conclusion；不外推到未列出的模型、任务、硬件、并发或生产 SLO。 Books：`已有覆盖`，owner=`AGENT-PLATFORM`；当前正文已覆盖相应 state/control/evaluation contract，new Integrate=0。 完整记录见 [V3_EVIDENCE_RECOVERED.md](../_sources/daily-20260605/V3_EVIDENCE_RECOVERED.md)。

### [Epistemic Injustice in Language Models: An Audit of Pretraining Filters and Guardrails](https://arxiv.org/abs/2606.05936v1)

`arXiv:2606.05936v1`；正文定位：1 Introduction；F1. Disagreement of filters and guardrails.。联合审计 pretraining filter 与 inference guardrail，证明词表控制点产生双阶段 epistemic erasure，修正数据/发布边界。 Evaluation：3.6 Evaluation Setting；Appendix A Detailed results on study of epistemic erasure of marginalised identities。 Limitations：Limitations；不外推到未列出的模型、任务、硬件、并发或生产 SLO。 Books：`已有覆盖`，owner=`PLATFORM-SECURITY`；当前正文已覆盖相应 state/control/evaluation contract，new Integrate=0。 完整记录见 [V3_EVIDENCE_RECOVERED.md](../_sources/daily-20260605/V3_EVIDENCE_RECOVERED.md)。

### [Dense Contexts Are Hard Contexts: Lexical Density Limits Effective Context in LLMs](https://arxiv.org/abs/2606.06203v1)

`arXiv:2606.06203v1`；正文定位：Appendix A Benchmark details: evaluation prompts and dataset construction；MK-NIAH System Prompt.。在固定长度与位置下证明 lexical density 缩小 effective context，修正只按 token length/position 判断长上下文容量的结论。 Evaluation：4 Results；4.1 Experiment Settings。 Limitations：5 Discussion and Limitations；不外推到未列出的模型、任务、硬件、并发或生产 SLO。 Books：`已整合`，canonical owner=`MODEL-LONG-CONTEXT`；Ch22 [“相同 Token Length 仍可能承载不同 Information Load”](../../../../books/part-02-model/22-long-context.md) 已在 Review notes 前完整写入旧基线、密度约束、EvalSpec 状态、收益、测量代价、混杂 failure 与 fallback，且保留 exact-v1 证据边界。完整记录见 [V3_EVIDENCE_RECOVERED.md](../_sources/daily-20260605/V3_EVIDENCE_RECOVERED.md)。

### [LLMs Can Leak Training Data But Do They Want To? A Propensity-Aware Evaluation of Memorization in LLMs](https://arxiv.org/abs/2606.06286v1)

`arXiv:2606.06286v1`；正文定位：3 Proposed Method: Propensity-Aware Memorization Evaluation。分离 worst-case extractability 与 ordinary-use propensity，并给 deterministic corpus tracing，修正 memorization 安全评测合同。 Evaluation：3 Proposed Method: Propensity-Aware Memorization Evaluation；3.1 Propensity-Capability Evaluation Settings。 Limitations：6 Discussion；7 Conclusion；不外推到未列出的模型、任务、硬件、并发或生产 SLO。 Books：`已有覆盖`，owner=`PLATFORM-SECURITY`；当前正文已覆盖相应 state/control/evaluation contract，new Integrate=0。 完整记录见 [V3_EVIDENCE_RECOVERED.md](../_sources/daily-20260605/V3_EVIDENCE_RECOVERED.md)。

### [CollabSim: A CSCW-Grounded Methodology for Investigating Collaborative Competence of LLM Agents through Controlled Multi-Agent Experiments](https://arxiv.org/abs/2606.06399v1)

`arXiv:2606.06399v1`；正文定位：3.1 System Architecture；4 Benchmark Experiments。以可控 interaction condition 和 action-level internal-state probe 将多 Agent collaborative competence 与任务总分分开。 Evaluation：4.1 Experiment Setup；4.2 Evaluation。 Limitations：6 Conclusion；7 Limitations；不外推到未列出的模型、任务、硬件、并发或生产 SLO。 Books：`Only report`；该项保留为当前窗口的评测/方法论上下文，不形成新的长期知识 owner。 完整记录见 [V3_EVIDENCE_RECOVERED.md](../_sources/daily-20260605/V3_EVIDENCE_RECOVERED.md)。

### [Search-Time Contamination in Deep Research Agents: Measuring Performance Inflation in Public Benchmark Evaluation](https://arxiv.org/abs/2606.05241v1)

精确版本 `2606.05241v1` 的机制与适用条件：研究定义 metadata、question-context、explicit-answer 三层 STC，并从 search traces 检测泄漏、重算去污染结果。browser trace 持有检索证据，benchmark owner 保存题目身份，contamination auditor 决定样本是否计分。

完整方法、评价、关键反证与未披露字段见[该家族的原文审阅](../_sources/daily-20260605/V2_1_EVIDENCE_ARCHIVE.md#260605241--search-time-contamination-in-deep-research-agents-measuring-performance-inflation-in-public-benchmark-evaluation)；复用精确版本的证据，不继承旧报告完成标签或旧 owner。当前 Books 处置为已有覆盖：`PLATFORM-EVALUATION-SYSTEM`（[books/part-06-ai-infrastructure/66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md))；现有正文对照及采用边界以本报告当前判断为准。

### [Statistically Reliable LLM-Based Ranking Evaluation via Prediction-Powered Inference](https://arxiv.org/abs/2606.05308v1)

精确版本 `2606.05308v1` 的机制与适用条件：PRECISE 用 prediction-powered inference 将大规模 judge predictions 与小规模 human residual correction 合成 bias-corrected ranking metric，并为 Precision@K 压缩 output-space computation。human labels 是校准数据，judge scores 是辅助信号，estimator 持有置信区间控制。

完整方法、评价、关键反证与未披露字段见[该家族的原文审阅](../_sources/daily-20260605/V2_1_EVIDENCE_ARCHIVE.md#260605308--statistically-reliable-llm-based-ranking-evaluation-via-prediction-powered-inference)；复用精确版本的证据，不继承旧报告完成标签或旧 owner。当前 Books 处置为已有覆盖：`PLATFORM-EVALUATION-SYSTEM`（[books/part-06-ai-infrastructure/66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md))；现有正文对照及采用边界以本报告当前判断为准。

### [A Taxonomy of Runtime Faults in Model Context Protocol Servers](https://arxiv.org/abs/2606.05339v1)

精确版本 `2606.05339v1` 的机制与适用条件：研究对473 repositories中的837 fault threads做 bottom-up coding，形成11大类、27子类/73 leaf faults，并按 interaction、tool、schema、state、安全和取消路径分配故障类型。issue evidence 是数据，taxonomy 是诊断状态，maintainer/release process 掌握修复控制。

完整方法、评价、关键反证与未披露字段见[该家族的原文审阅](../_sources/daily-20260605/V2_1_EVIDENCE_ARCHIVE.md#260605339--a-taxonomy-of-runtime-faults-in-model-context-protocol-servers)；复用精确版本的证据，不继承旧报告完成标签或旧 owner。当前 Books 处置为已有覆盖：`AGENT-MCP`（[books/part-07-agent/83-mcp.md](../../../../books/part-07-agent/83-mcp.md))；现有正文对照及采用边界以本报告当前判断为准。

### [Stability vs. Manipulability: Evaluating Robustness Under Post-Decision Interaction in LLM Judges](https://arxiv.org/abs/2606.05384v1)

精确版本 `2606.05384v1` 的机制与适用条件：protocol 先固定 initial decision，再施加 repeated/neutral、anti-baseline 与 counterbalanced target challenges，用 ERS 等指标分离稳定性、可逆性和定向操纵。conversation state 是新增数据，judge 持有 verdict，evaluation harness 控制挑战顺序。

完整方法、评价、关键反证与未披露字段见[该家族的原文审阅](../_sources/daily-20260605/V2_1_EVIDENCE_ARCHIVE.md#260605384--stability-vs-manipulability-evaluating-robustness-under-post-decision-interaction-in-llm-judges)；复用精确版本的证据，不继承旧报告完成标签或旧 owner。当前 Books 处置为已有覆盖：`PLATFORM-EVALUATION-SYSTEM`（[books/part-06-ai-infrastructure/66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md))；现有正文对照及采用边界以本报告当前判断为准。

### [VASO: Formally Verifiable Self-Evolving Skills for Physical AI Agents](https://arxiv.org/abs/2606.05395v1)

精确版本 `2606.05395v1` 的机制与适用条件：VASO 将 skill 表示为 planner-facing interface 与 formal state/action proposition contract，迭代生成 labeling function、model checking counterexample 和 skill refinement。contract 持有安全状态，robot plan 是数据，verifier 掌握执行前授权。

完整方法、评价、关键反证与未披露字段见[该家族的原文审阅](../_sources/daily-20260605/V2_1_EVIDENCE_ARCHIVE.md#260605395--vaso-formally-verifiable-self-evolving-skills-for-physical-ai-agents)；复用精确版本的证据，不继承旧报告完成标签或旧 owner。当前 Books 处置为已有覆盖：`AGENT-WORKFLOW`（[books/part-07-agent/81-workflow.md](../../../../books/part-07-agent/81-workflow.md))；现有正文对照及采用边界以本报告当前判断为准。

### [Trust, but Don't Verify: Epistemic Blind Spots in LLM Source Evaluation](https://arxiv.org/abs/2606.05403v1)

精确版本 `2606.05403v1` 的机制与适用条件：实验正交操纵 methodology register 与 numerical validity，比较单源识别和多源 influence。source text/number 是证据数据，synthesis model 持有权重分配，validity probe 检查是否调用已具备的识别能力。

完整方法、评价、关键反证与未披露字段见[该家族的原文审阅](../_sources/daily-20260605/V2_1_EVIDENCE_ARCHIVE.md#260605403--trust-but-dont-verify-epistemic-blind-spots-in-llm-source-evaluation)；复用精确版本的证据，不继承旧报告完成标签或旧 owner。当前 Books 处置为已有覆盖：`PLATFORM-EVALUATION-SYSTEM`（[books/part-06-ai-infrastructure/66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md))；现有正文对照及采用边界以本报告当前判断为准。

### [When Evidence is Sparse: Weakly Supervised Early Failure Alerting in Dialogs and LLM-Agent Trajectories](https://arxiv.org/abs/2606.05414v1)

精确版本 `2606.05414v1` 的机制与适用条件：attention-based predictor 从整体 label 学稀疏 turn evidence，再以 risk estimate 驱动可调 alert/stop policy。partial trajectory 是数据状态，risk model 更新 failure belief，threshold controller 掌握中止/升级。

完整方法、评价、关键反证与未披露字段见[该家族的原文审阅](../_sources/daily-20260605/V2_1_EVIDENCE_ARCHIVE.md#260605414--when-evidence-is-sparse-weakly-supervised-early-failure-alerting-in-dialogs-and-llm-agent-trajectories)；复用精确版本的证据，不继承旧报告完成标签或旧 owner。当前 Books 处置为仅报告：当前窗口上下文，不形成独立长期机制；现有正文对照及采用边界以本报告当前判断为准。

### [Zero knowledge verification for frontier AI training is possible](https://arxiv.org/abs/2606.05433v1)

精确版本 `2606.05433v1` 的机制与适用条件：方案预提交 training specification，采集 inter-node network observations，并在线生成 intermediate-computation Merkle commitments，使用具 native tensor primitives 的 zkVM 抽查/证明。trainer 持有执行状态，commitments/telemetry 是审计数据，verifier 掌握合规判定。

完整方法、评价、关键反证与未披露字段见[该家族的原文审阅](../_sources/daily-20260605/V2_1_EVIDENCE_ARCHIVE.md#260605433--zero-knowledge-verification-for-frontier-ai-training-is-possible)；复用精确版本的证据，不继承旧报告完成标签或旧 owner。当前 Books 处置为已有覆盖：`PLATFORM-SECURITY`（[books/part-06-ai-infrastructure/72-security.md](../../../../books/part-06-ai-infrastructure/72-security.md))；现有正文对照及采用边界以本报告当前判断为准。

### [ADK Arena: Evaluating Agent Development Kits via LLM-as-a-Developer](https://arxiv.org/abs/2606.05548v1)

精确版本 `2606.05548v1` 的机制与适用条件：The manuscript holds the coding developer model fixed, gives every framework an isolated Docker environment, validates that generated code actually imports the target framework, and runs uniform adapters over four benchmark families. This turns documentation usability, repair effort and resulting agent behavior into separate observables. The experiment covers 51 Python frameworks and 204 framework–benchmark pairs, but the reported generation cost and success are conditional on the frozen documen（完整论证及边界见下方原文审阅，不以此摘录代替它）

完整方法、评价、关键反证与未披露字段见[该家族的原文审阅](../_sources/daily-20260605/V2_1_EVIDENCE_ARCHIVE.md#260605548--adk-arena-evaluating-agent-development-kits-via-llm-as-a-developer)；复用精确版本的证据，不继承旧报告完成标签或旧 owner。当前 Books 处置为已有覆盖：`PLATFORM-EVALUATION-SYSTEM`（[books/part-06-ai-infrastructure/66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md))；现有正文对照及采用边界以本报告当前判断为准。

### [An Embarrassingly Simple Detector for Model Extraction Attacks in Large Language Model API Traffic](https://arxiv.org/abs/2606.05725v1)

精确版本 `2606.05725v1` 的机制与适用条件：The detector aggregates statistical discrepancy over sequences of API queries instead of judging each request in isolation, with per-dataset results and implementation details. Detection depends on window, benign traffic, attacker adaptation and model endpoint; it does not prove attribution or justify automatic punishment without policy review. 在本次复核中，`PLATFORM-SECURITY` 是 canonical owner；论文改变或测量的是该节点内的 state/data/control boundary，不把作者实现提升为通用产品结论。

完整方法、评价、关键反证与未披露字段见[该家族的原文审阅](../_sources/daily-20260605/V2_1_EVIDENCE_ARCHIVE.md#260605725--an-embarrassingly-simple-detector-for-model-extraction-attacks-in-large-language-model-api-traffic)；复用精确版本的证据，不继承旧报告完成标签或旧 owner。当前 Books 处置为已有覆盖：`PLATFORM-SECURITY`（[books/part-06-ai-infrastructure/72-security.md](../../../../books/part-06-ai-infrastructure/72-security.md))；现有正文对照及采用边界以本报告当前判断为准。

### [Membrane: A Self-Evolving Contrastive Safety Memory for LLM Agent Defense](https://arxiv.org/abs/2606.05743v1)

精确版本 `2606.05743v1` 的机制与适用条件：Membrane stores contrastive attack/benign experience and updates retrieval/decision state as new attacks arrive, measuring both jailbreak blocking and over-refusal. Online safety memory can adapt faster than weights but can also be poisoned or authorize false positives; the retrieved signal must not own the final action. 在本次复核中，`PLATFORM-SECURITY` 是 canonical owner；论文改变或测量的是该节点内的 state/data/control boundary，不把作者实现提升为通用产品结论。

完整方法、评价、关键反证与未披露字段见[该家族的原文审阅](../_sources/daily-20260605/V2_1_EVIDENCE_ARCHIVE.md#260605743--membrane-a-self-evolving-contrastive-safety-memory-for-llm-agent-defense)；复用精确版本的证据，不继承旧报告完成标签或旧 owner。当前 Books 处置为已有覆盖：`PLATFORM-SECURITY`（[books/part-06-ai-infrastructure/72-security.md](../../../../books/part-06-ai-infrastructure/72-security.md))；现有正文对照及采用边界以本报告当前判断为准。

### [SentinelRAG: Synthetic Sentinel Knowledge for RAG Database Copyright Protection](https://arxiv.org/abs/2606.05787v1)

精确版本 `2606.05787v1` 的机制与适用条件：SentinelRAG injects synthetic, detectable knowledge into a retrieval database so suspicious reproduction can provide a provenance signal while ordinary query utility is monitored. The attack/utility experiments support the chosen retrievers and sentinel construction, but adaptive attackers, false positives and database transformation define the boundary; the watermark is evidence, not automatic enforcement authority. 在本次复核中，`PLATFORM-SECURITY` 是 canonical owner；论文改变或测量的是该节点内的 state/data/control （完整论证及边界见下方原文审阅，不以此摘录代替它）

完整方法、评价、关键反证与未披露字段见[该家族的原文审阅](../_sources/daily-20260605/V2_1_EVIDENCE_ARCHIVE.md#260605787--sentinelrag-synthetic-sentinel-knowledge-for-rag-database-copyright-protection)；复用精确版本的证据，不继承旧报告完成标签或旧 owner。当前 Books 处置为已有覆盖：`PLATFORM-SECURITY`（[books/part-06-ai-infrastructure/72-security.md](../../../../books/part-06-ai-infrastructure/72-security.md))；现有正文对照及采用边界以本报告当前判断为准。

### [From Risk Classification to Action Plan Remediation: A Guardrail Feedback Driven Framework for LLM Agents](https://arxiv.org/abs/2606.05805v1)

精确版本 `2606.05805v1` 的机制与适用条件：The framework turns a risk classification into a structured remediation plan for an agent workflow. This can make a guardrail response more actionable than allow/deny alone, but a generated plan is a proposal: policy, authorization, human escalation and post-action verification must remain external owners. 在本次复核中，`PLATFORM-SECURITY` 是 canonical owner；论文改变或测量的是该节点内的 state/data/control boundary，不把作者实现提升为通用产品结论。

完整方法、评价、关键反证与未披露字段见[该家族的原文审阅](../_sources/daily-20260605/V2_1_EVIDENCE_ARCHIVE.md#260605805--from-risk-classification-to-action-plan-remediation-a-guardrail-feedback-driven-framework-for-llm-agents)；复用精确版本的证据，不继承旧报告完成标签或旧 owner。当前 Books 处置为已有覆盖：`PLATFORM-SECURITY`（[books/part-06-ai-infrastructure/72-security.md](../../../../books/part-06-ai-infrastructure/72-security.md))；现有正文对照及采用边界以本报告当前判断为准。

### [Steering Vectors are an Adversarial Attack Surface](https://arxiv.org/abs/2606.05958v1)

精确版本 `2606.05958v1` 的机制与适用条件：The attack optimizes benign-looking contrast pairs so their derived steering vector preserves a named attribute on benign prompts while increasing jailbreak behavior. Threat-model, multi-model and internal-analysis results support the tested steering pipeline; access assumptions and evaluator coverage bound the claim. 在本次复核中，`PLATFORM-SECURITY` 是 canonical owner；论文改变或测量的是该节点内的 state/data/control boundary，不把作者实现提升为通用产品结论。

完整方法、评价、关键反证与未披露字段见[该家族的原文审阅](../_sources/daily-20260605/V2_1_EVIDENCE_ARCHIVE.md#260605958--steering-vectors-are-an-adversarial-attack-surface)；复用精确版本的证据，不继承旧报告完成标签或旧 owner。当前 Books 处置为已有覆盖：`PLATFORM-SECURITY`（[books/part-06-ai-infrastructure/72-security.md](../../../../books/part-06-ai-infrastructure/72-security.md))；现有正文对照及采用边界以本报告当前判断为准。

### [The Self-Correction Illusion: Role Relabeling Gates Explicit Error Flagging in Large Language Models](https://arxiv.org/abs/2606.05976v1)

精确版本 `2606.05976v1` 的机制与适用条件：The intervention keeps answer bytes fixed but changes whether the chat template labels them as the model's own or another actor's output. Verification and adversarial-mirror experiments support role-conditioned error flagging, showing that failure can be an access/policy gate rather than absent error knowledge. It does not prove faithful internal reasoning or universal correction across templates. 在本次复核中，`AGENT-REFLECTION` 是 canonical owner；论文改变或测量的是该节点内的 state/data/control boundary，不把作者实现提升为通用产（完整论证及边界见下方原文审阅，不以此摘录代替它）

完整方法、评价、关键反证与未披露字段见[该家族的原文审阅](../_sources/daily-20260605/V2_1_EVIDENCE_ARCHIVE.md#260605976--the-self-correction-illusion-role-relabeling-gates-explicit-error-flagging-in-large-language-models)；复用精确版本的证据，不继承旧报告完成标签或旧 owner。当前 Books 处置为已有覆盖：`AGENT-REFLECTION`（[books/part-07-agent/80-reflection.md](../../../../books/part-07-agent/80-reflection.md))；现有正文对照及采用边界以本报告当前判断为准。

### [HUSH-Bench: Measuring Memory-Use Boundaries for Sensitive History in Conversational Agents](https://arxiv.org/abs/2606.06055v1)

精确版本 `2606.06055v1` 的机制与适用条件：RBI-Eval varies sensitive, benign and irrelevant histories to measure whether memory shifts a response when that use is warranted. The benchmark distinguishes access from justified use; it does not establish user intent, universal privacy norms or production policy correctness. 在本次复核中，`AGENT-MEMORY` 是 canonical owner；论文改变或测量的是该节点内的 state/data/control boundary，不把作者实现提升为通用产品结论。

完整方法、评价、关键反证与未披露字段见[该家族的原文审阅](../_sources/daily-20260605/V2_1_EVIDENCE_ARCHIVE.md#260606055--hush-bench-measuring-memory-use-boundaries-for-sensitive-history-in-conversational-agents)；复用精确版本的证据，不继承旧报告完成标签或旧 owner。当前 Books 处置为已有覆盖：`AGENT-MEMORY`（[books/part-07-agent/77-memory.md](../../../../books/part-07-agent/77-memory.md))；现有正文对照及采用边界以本报告当前判断为准。

### [From Reward-Hack Activations to Agentic Risk States: Context-Calibrated Mechanistic Monitoring in LLM Agents](https://arxiv.org/abs/2606.06223v1)

精确版本 `2606.06223v1` 的机制与适用条件：Activation scores identify a policy tendency; entropy and decision context determine when it is likely to become an unsafe next action. Gameable environments and steering experiments support layered monitoring, but transfer and causal specificity remain weak. 在本次复核中，`PLATFORM-MONITORING` 是 canonical owner；论文改变或测量的是该节点内的 state/data/control boundary，不把作者实现提升为通用产品结论。

完整方法、评价、关键反证与未披露字段见[该家族的原文审阅](../_sources/daily-20260605/V2_1_EVIDENCE_ARCHIVE.md#260606223--from-reward-hack-activations-to-agentic-risk-states-context-calibrated-mechanistic-monitoring-in-llm-agents)；复用精确版本的证据，不继承旧报告完成标签或旧 owner。当前 Books 处置为已有覆盖：`PLATFORM-MONITORING`（[books/part-06-ai-infrastructure/67-monitoring.md](../../../../books/part-06-ai-infrastructure/67-monitoring.md))；现有正文对照及采用边界以本报告当前判断为准。

### [From Failed Trajectories to Reliable LLM Agents: Diagnosing and Repairing Harness Flaws](https://arxiv.org/abs/2606.06324v1)

精确版本 `2606.06324v1` 的机制与适用条件：HTIR binds failed trajectory spans to provenance, control-flow and artifact-effect edges before a scoped harness patch is admitted; its held-out gains do not establish causal correctness outside the four benchmark harnesses. 在本次复核中，`AGENT-PLATFORM` 是 canonical owner；论文改变或测量的是该节点内的 state/data/control boundary，不把作者实现提升为通用产品结论。

完整方法、评价、关键反证与未披露字段见[该家族的原文审阅](../_sources/daily-20260605/V2_1_EVIDENCE_ARCHIVE.md#260606324--from-failed-trajectories-to-reliable-llm-agents-diagnosing-and-repairing-harness-flaws)；复用精确版本的证据，不继承旧报告完成标签或旧 owner。当前 Books 处置为已有覆盖：`AGENT-PLATFORM`（[books/part-07-agent/84-agent-platform.md](../../../../books/part-07-agent/84-agent-platform.md))；现有正文对照及采用边界以本报告当前判断为准。

### [WebMCP Tool Surface Poisoning: Runtime Manipulation Attacks on LLM Agents](https://arxiv.org/abs/2606.06387v1)

精确版本 `2606.06387v1` 的机制与适用条件：The attack changes an MCP tool surface during an active session, so tool identity and authorization cannot be checked only at discovery time; the experiments bound exploitability, not all MCP clients or transports. 在本次复核中，`AGENT-MCP` 是 canonical owner；论文改变或测量的是该节点内的 state/data/control boundary，不把作者实现提升为通用产品结论。

完整方法、评价、关键反证与未披露字段见[该家族的原文审阅](../_sources/daily-20260605/V2_1_EVIDENCE_ARCHIVE.md#260606387--webmcp-tool-surface-poisoning-runtime-manipulation-attacks-on-llm-agents)；复用精确版本的证据，不继承旧报告完成标签或旧 owner。当前 Books 处置为已有覆盖：`AGENT-MCP`（[books/part-07-agent/83-mcp.md](../../../../books/part-07-agent/83-mcp.md))；现有正文对照及采用边界以本报告当前判断为准。

### [Will the Agent Recuse, and Will It Stop? Measuring LLM-Agent Compliance with In-Band Governance Signals at the Access Door and Mid-Flight](https://arxiv.org/abs/2606.06460v1)

精确版本 `2606.06460v1` 的机制与适用条件：In-band deny and stop signals are evaluated as two different control points, showing that recognition does not imply mid-flight termination; the pilot does not prove enforceable governance without an external reference monitor. 在本次复核中，`PLATFORM-SECURITY` 是 canonical owner；论文改变或测量的是该节点内的 state/data/control boundary，不把作者实现提升为通用产品结论。

完整方法、评价、关键反证与未披露字段见[该家族的原文审阅](../_sources/daily-20260605/V2_1_EVIDENCE_ARCHIVE.md#260606460--will-the-agent-recuse-and-will-it-stop-measuring-llm-agent-compliance-with-in-band-governance-signals-at-the-access-door-and-mid-flight)；复用精确版本的证据，不继承旧报告完成标签或旧 owner。当前 Books 处置为已有覆盖：`PLATFORM-SECURITY`（[books/part-06-ai-infrastructure/72-security.md](../../../../books/part-06-ai-infrastructure/72-security.md))；现有正文对照及采用边界以本报告当前判断为准。

### [BIDENT: Heterogeneous Operator-level Mapping for Efficient Edge Inference](https://arxiv.org/abs/2606.05271v1)

精确版本 `2606.05271v1` 的机制与适用条件：BIDENT 离线 profile H2D、dispatch、kernel、D2H 与能耗，将 operator-PU choice 编成 weighted execution graph 并求 shortest path。profile DB 持有 cost state，operators/tensors 是数据，mapper 掌握 placement。

完整方法、评价、关键反证与未披露字段见[该家族的原文审阅](../_sources/daily-20260605/V2_1_EVIDENCE_ARCHIVE.md#260605271--bident-heterogeneous-operator-level-mapping-for-efficient-edge-inference)；复用精确版本的证据，不继承旧报告完成标签或旧 owner。当前 Books 处置为仅报告：当前窗口上下文，不形成独立长期机制；现有正文对照及采用边界以本报告当前判断为准。

### [SET: Stream-Event-Triggered Scheduling for Efficient CUDA Graph Pipelines](https://arxiv.org/abs/2606.05495v1)

精确版本 `2606.05495v1` 的机制与适用条件：SET 为每 worker 绑定 stream、pre-instantiated graph 和独立 buffers，用 event chaining/work stealing 在完成时派发下一 job。per-stream buffer 持有 in-flight state，CUDA events 是控制信号，scheduler 掌握 worker/slot 所有权。

完整方法、评价、关键反证与未披露字段见[该家族的原文审阅](../_sources/daily-20260605/V2_1_EVIDENCE_ARCHIVE.md#260605495--set-stream-event-triggered-scheduling-for-efficient-cuda-graph-pipelines)；复用精确版本的证据，不继承旧报告完成标签或旧 owner。当前 Books 处置为已有覆盖：`INFER-SCHEDULING`（[books/part-05-inference-system/56-inference-scheduling.md](../../../../books/part-05-inference-system/56-inference-scheduling.md))；现有正文对照及采用边界以本报告当前判断为准。

### [ColBERTSaR: Sparsified ColBERT Index via Product Quantization](https://arxiv.org/abs/2606.05568v1)

精确版本 `2606.05568v1` 的机制与适用条件：ColBERTSaR interprets product-quantized document-token representations as learned sparse terms and retains MaxSim as the scoring distinction. Cross-language retrieval experiments report competitive effectiveness and index sizes roughly 53–77% of a one-bit PLAID index, with a larger gap on technical terminology. This is a proof-of-concept index representation result: it does not disclose production query latency, update cost, cache behavior, end-to-end RAG quality or generalize beyond the tested （完整论证及边界见下方原文审阅，不以此摘录代替它）

完整方法、评价、关键反证与未披露字段见[该家族的原文审阅](../_sources/daily-20260605/V2_1_EVIDENCE_ARCHIVE.md#260605568--colbertsar-sparsified-colbert-index-via-product-quantization)；复用精确版本的证据，不继承旧报告完成标签或旧 owner。当前 Books 处置为已有覆盖：`AGENT-RAG`（[books/part-07-agent/76-rag.md](../../../../books/part-07-agent/76-rag.md))；现有正文对照及采用边界以本报告当前判断为准。

### [AsyncWebRL: Efficient Asynchronous Reinforcement Learning for Multi-Step Visual Web Agents](https://arxiv.org/abs/2606.05597v1)

精确版本 `2606.05597v1` 的机制与适用条件：AsyncWebRL overlaps rollout, update and policy refresh with an everlasting pool, moves screenshots behind lightweight references, and corrects mixed policy versions during training. It also replaces a per-trajectory `1/|τ|` normalizer whose interaction with longer failed trajectories weakened negative token gradients. The authors report 2.4–2.9× pipeline speedup and shorter trajectories under their web-agent/browser/GPU configuration, but hardware, concurrency, precision and service SLO are not （完整论证及边界见下方原文审阅，不以此摘录代替它）

完整方法、评价、关键反证与未披露字段见[该家族的原文审阅](../_sources/daily-20260605/V2_1_EVIDENCE_ARCHIVE.md#260605597--asyncwebrl-efficient-asynchronous-reinforcement-learning-for-multi-step-visual-web-agents)；复用精确版本的证据，不继承旧报告完成标签或旧 owner。当前 Books 处置为已有覆盖：`TRAIN-DISTRIBUTED-TRAINING`（[books/part-04-training-system/36-distributed-training.md](../../../../books/part-04-training-system/36-distributed-training.md))；现有正文对照及采用边界以本报告当前判断为准。

### [AdaPLD: Adaptive Retrieval and Reuse for Efficient Model-Free Speculative Decoding](https://arxiv.org/abs/2606.05742v1)

精确版本 `2606.05742v1` 的机制与适用条件：AdaPLD retrieves and reuses prior continuation patterns without a trained draft model and adapts proposal length/ reuse based on acceptance. Main, component and stochastic-decoding tests support the selected LMs/benchmarks; cache lookup overhead, stale patterns and target verification remain. 在本次复核中，`INFER-SPECULATIVE-DECODING` 是 canonical owner；论文改变或测量的是该节点内的 state/data/control boundary，不把作者实现提升为通用产品结论。

完整方法、评价、关键反证与未披露字段见[该家族的原文审阅](../_sources/daily-20260605/V2_1_EVIDENCE_ARCHIVE.md#260605742--adapld-adaptive-retrieval-and-reuse-for-efficient-model-free-speculative-decoding)；复用精确版本的证据，不继承旧报告完成标签或旧 owner。当前 Books 处置为已有覆盖：`INFER-SPECULATIVE-DECODING`（[books/part-05-inference-system/48-speculative-decoding.md](../../../../books/part-05-inference-system/48-speculative-decoding.md))；现有正文对照及采用边界以本报告当前判断为准。

### [QCFuse: Query-Aware Cache Fusion via Compressed View for Efficient RAG Serving](https://arxiv.org/abs/2606.05875v1)

精确版本 `2606.05875v1` 的机制与适用条件：QCFuse uses chunk-anchor probing and critical-layer localization to select which cached tokens need recomputation, avoiding a full-context/all-layer selection pass that would stall pipelined cache fusion. SGLang experiments cover TTFT, context scaling, bandwidth, request load, quality and ablations, but results remain model, dataset, cache-link, recompute-budget and SLO specific. 在本次复核中，`INFER-KV-CACHE` 是 canonical owner；论文改变或测量的是该节点内的 state/data/control boundary，不把作者实现提升为通用产品结论。

完整方法、评价、关键反证与未披露字段见[该家族的原文审阅](../_sources/daily-20260605/V2_1_EVIDENCE_ARCHIVE.md#260605875--qcfuse-query-aware-cache-fusion-via-compressed-view-for-efficient-rag-serving)；复用精确版本的证据，不继承旧报告完成标签或旧 owner。当前 Books 处置为已有覆盖：`INFER-KV-CACHE`（[books/part-05-inference-system/45-why-kv-cache-speeds-up.md](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md))；现有正文对照及采用边界以本报告当前判断为准。

### [Beyond Greedy Chunking: SLO-Aware Sliding-Window Scheduling for LLM Inference](https://arxiv.org/abs/2606.05933v1)

精确版本 `2606.05933v1` 的机制与适用条件：SlidingServe predicts batch latency, assigns multi-level priority and constructs chunks over a scheduling window rather than greedily optimizing one iteration. Goodput, overload, transient-load, ablation and predictor-fidelity experiments support the tested serving stack; prediction error, workload drift and starvation remain failure modes, and results are bound to the reported model/hardware/load/SLO contract. 在本次复核中，`INFER-SCHEDULING` 是 canonical owner；论文改变或测量的是该节点内的 state/data/control boundar（完整论证及边界见下方原文审阅，不以此摘录代替它）

完整方法、评价、关键反证与未披露字段见[该家族的原文审阅](../_sources/daily-20260605/V2_1_EVIDENCE_ARCHIVE.md#260605933--beyond-greedy-chunking-slo-aware-sliding-window-scheduling-for-llm-inference)；复用精确版本的证据，不继承旧报告完成标签或旧 owner。当前 Books 处置为已有覆盖：`INFER-SCHEDULING`（[books/part-05-inference-system/56-inference-scheduling.md](../../../../books/part-05-inference-system/56-inference-scheduling.md))；现有正文对照及采用边界以本报告当前判断为准。

### [Demystifying NVSHMEM: A System-Level Analysis on Symmetric Memory and Device-Initiated Operations in GPU Communication](https://arxiv.org/abs/2606.05951v1)

精确版本 `2606.05951v1` 的机制与适用条件：The source traces symmetric-memory allocation/registration, remote address computation, device-initiated RMA, proxy or IBGDA paths, ordering, collectives and protocol selection. System experiments can explain when device-side one-sided communication avoids host orchestration, but conclusions are version/topology/interconnect specific and must not be turned into generic bandwidth claims. 在本次复核中，`TRAIN-DISTRIBUTED-TRAINING` 是 canonical owner；论文改变或测量的是该节点内的 state/data/control boundary，不把作者实现提升为通用产品（完整论证及边界见下方原文审阅，不以此摘录代替它）

完整方法、评价、关键反证与未披露字段见[该家族的原文审阅](../_sources/daily-20260605/V2_1_EVIDENCE_ARCHIVE.md#260605951--demystifying-nvshmem-a-system-level-analysis-on-symmetric-memory-and-device-initiated-operations-in-gpu-communication)；复用精确版本的证据，不继承旧报告完成标签或旧 owner。当前 Books 处置为已有覆盖：`TRAIN-DISTRIBUTED-TRAINING`（[books/part-04-training-system/36-distributed-training.md](../../../../books/part-04-training-system/36-distributed-training.md))；现有正文对照及采用边界以本报告当前判断为准。

### [Learning to Route LLMs from Implicit Cost-Performance Preferences via Meta-Learning](https://arxiv.org/abs/2606.06178v1)

精确版本 `2606.06178v1` 的机制与适用条件：MetaRouter treats preference profiles as contextual-bandit tasks and meta-learns fast adaptation to limited feedback. In/out-of-distribution tests support the tested model pools; preference drift and feedback/reward bias remain. 在本次复核中，`INFER-SCHEDULING` 是 canonical owner；论文改变或测量的是该节点内的 state/data/control boundary，不把作者实现提升为通用产品结论。

完整方法、评价、关键反证与未披露字段见[该家族的原文审阅](../_sources/daily-20260605/V2_1_EVIDENCE_ARCHIVE.md#260606178--learning-to-route-llms-from-implicit-cost-performance-preferences-via-meta-learning)；复用精确版本的证据，不继承旧报告完成标签或旧 owner。当前 Books 处置为已有覆盖：`INFER-SCHEDULING`（[books/part-05-inference-system/56-inference-scheduling.md](../../../../books/part-05-inference-system/56-inference-scheduling.md))；现有正文对照及采用边界以本报告当前判断为准。

### [RedKnot: Efficient Long-Context LLM Serving with Head-Aware KV Reuse and SegPagedAttention](https://arxiv.org/abs/2606.06256v1)

精确版本 `2606.06256v1` 的机制与适用条件：RedKnot reuses cached context selectively across attention heads and introduces segmented paged attention to serve non-contiguous reused state. Long-context results support reported models/configurations; reuse identity, precision, prefix overlap, concurrency and SLO must remain explicit. 在本次复核中，`INFER-KV-CACHE` 是 canonical owner；论文改变或测量的是该节点内的 state/data/control boundary，不把作者实现提升为通用产品结论。

完整方法、评价、关键反证与未披露字段见[该家族的原文审阅](../_sources/daily-20260605/V2_1_EVIDENCE_ARCHIVE.md#260606256--redknot-efficient-long-context-llm-serving-with-head-aware-kv-reuse-and-segpagedattention)；复用精确版本的证据，不继承旧报告完成标签或旧 owner。当前 Books 处置为已有覆盖：`INFER-KV-CACHE`（[books/part-05-inference-system/45-why-kv-cache-speeds-up.md](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md))；现有正文对照及采用边界以本报告当前判断为准。

### [Tangram: Unlocking Non-Uniform KV Cache Compression for Efficient Multi-turn LLM Serving](https://arxiv.org/abs/2606.06302v1)

精确版本 `2606.06302v1` 的机制与适用条件：Tangram calibrates stable head budgets offline, reserves them at scheduling, uses ragged page tables and precomputes load balance. vLLM evidence supports reported workloads; head stability, quality, GPU, turns, concurrency and SLO are required conditions. 在本次复核中，`INFER-KV-CACHE` 是 canonical owner；论文改变或测量的是该节点内的 state/data/control boundary，不把作者实现提升为通用产品结论。

完整方法、评价、关键反证与未披露字段见[该家族的原文审阅](../_sources/daily-20260605/V2_1_EVIDENCE_ARCHIVE.md#260606302--tangram-unlocking-non-uniform-kv-cache-compression-for-efficient-multi-turn-llm-serving)；复用精确版本的证据，不继承旧报告完成标签或旧 owner。当前 Books 处置为已有覆盖：`INFER-KV-CACHE`（[books/part-05-inference-system/45-why-kv-cache-speeds-up.md](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md))；现有正文对照及采用边界以本报告当前判断为准。

### [Vortex: Efficient and Programmable Sparse Attention Serving for AI Agents](https://arxiv.org/abs/2606.06453v1)

精确版本 `2606.06453v1` 的机制与适用条件：Vortex moves sparse-attention interpretation into a programmable runtime and lowers it into kernels and scheduling state; reported speed/accuracy slices remain model, GPU, precision and length conditional. 在本次复核中，`INFER-PAGED-ATTENTION` 是 canonical owner；论文改变或测量的是该节点内的 state/data/control boundary，不把作者实现提升为通用产品结论。

完整方法、评价、关键反证与未披露字段见[该家族的原文审阅](../_sources/daily-20260605/V2_1_EVIDENCE_ARCHIVE.md#260606453--vortex-efficient-and-programmable-sparse-attention-serving-for-ai-agents)；复用精确版本的证据，不继承旧报告完成标签或旧 owner。当前 Books 处置为已有覆盖：`INFER-PAGED-ATTENTION`（[books/part-05-inference-system/47-pagedattention.md](../../../../books/part-05-inference-system/47-pagedattention.md))；现有正文对照及采用边界以本报告当前判断为准。

### [You Only Index Once: Cross-Layer Sparse Attention with Shared Routing](https://arxiv.org/abs/2606.06467v1)

精确版本 `2606.06467v1` 的机制与适用条件：Shared routing reuses one sparse index across layers to reduce indexing work, trading layer-specific selectivity for reuse; its accuracy and efficiency evidence is architecture- and workload-bound. 在本次复核中，`INFER-PAGED-ATTENTION` 是 canonical owner；论文改变或测量的是该节点内的 state/data/control boundary，不把作者实现提升为通用产品结论。

完整方法、评价、关键反证与未披露字段见[该家族的原文审阅](../_sources/daily-20260605/V2_1_EVIDENCE_ARCHIVE.md#260606467--you-only-index-once-cross-layer-sparse-attention-with-shared-routing)；复用精确版本的证据，不继承旧报告完成标签或旧 owner。当前 Books 处置为已有覆盖：`INFER-PAGED-ATTENTION`（[books/part-05-inference-system/47-pagedattention.md](../../../../books/part-05-inference-system/47-pagedattention.md))；现有正文对照及采用边界以本报告当前判断为准。

### [What Should Agents Say? Action-state Communication for Efficient Multi-Agent Systems](https://arxiv.org/abs/2606.05304v1)

精确版本 `2606.05304v1` 的机制与适用条件：PACT 把每次 agent output 投影为 public action-state record，再写入 shared history。private reasoning 归各 agent，action/state delta 是公共数据，projection policy 掌握跨 agent 暴露控制。

完整方法、评价、关键反证与未披露字段见[该家族的原文审阅](../_sources/daily-20260605/V2_1_EVIDENCE_ARCHIVE.md#260605304--what-should-agents-say-action-state-communication-for-efficient-multi-agent-systems)；复用精确版本的证据，不继承旧报告完成标签或旧 owner。当前 Books 处置为已有覆盖：`AGENT-MULTI-AGENT`（[books/part-07-agent/82-multi-agent.md](../../../../books/part-07-agent/82-multi-agent.md))；现有正文对照及采用边界以本报告当前判断为准。

### [Executable Schema Contracts: From Automatic Ingestion to Multi-Source Retrieval](https://arxiv.org/abs/2606.05415v1)

精确版本 `2606.05415v1` 的机制与适用条件：系统用 closed-world field catalog 约束 schema discovery，确定性推断 keys/hierarchy，并以同一 executable schema 驱动 extraction、dedup、KG linking 与多工具 retrieval。schema/version 持有契约，provenance graph 是状态，router 控制查询路径。

完整方法、评价、关键反证与未披露字段见[该家族的原文审阅](../_sources/daily-20260605/V2_1_EVIDENCE_ARCHIVE.md#260605415--executable-schema-contracts-from-automatic-ingestion-to-multi-source-retrieval)；复用精确版本的证据，不继承旧报告完成标签或旧 owner。当前 Books 处置为已有覆盖：`PLATFORM-FOUNDATIONS`（[books/part-06-ai-infrastructure/57-what-is-ai-platform.md](../../../../books/part-06-ai-infrastructure/57-what-is-ai-platform.md))；现有正文对照及采用边界以本报告当前判断为准。

### [Data Flow Control: Data Safety Policies for AI Agents](https://arxiv.org/abs/2606.05679v1)

精确版本 `2606.05679v1` 的机制与适用条件：The paper separates a data-use/release policy from SQL or tool-call correctness and compares logical provenance with physical enforcement paths. This makes combination, derivation and disclosure effects explicit at action time; the prototype assumes trusted mediation and cannot undo disclosure after data leave the boundary. 在本次复核中，`PLATFORM-SECURITY` 是 canonical owner；论文改变或测量的是该节点内的 state/data/control boundary，不把作者实现提升为通用产品结论。

完整方法、评价、关键反证与未披露字段见[该家族的原文审阅](../_sources/daily-20260605/V2_1_EVIDENCE_ARCHIVE.md#260605679--data-flow-control-data-safety-policies-for-ai-agents)；复用精确版本的证据，不继承旧报告完成标签或旧 owner。当前 Books 处置为已有覆盖：`PLATFORM-SECURITY`（[books/part-06-ai-infrastructure/72-security.md](../../../../books/part-06-ai-infrastructure/72-security.md))；现有正文对照及采用边界以本报告当前判断为准。

### [Entropy-Based Observability for AI Agent Behavior](https://arxiv.org/abs/2606.05872v1)

精确版本 `2606.05872v1` 的机制与适用条件：The framework defines action, trajectory and tool entropy, information gain, exploration efficiency and robustness entropy, then demonstrates them on controlled and learning-roadmap agents. These lightweight signals can reveal behavioral collapse or churn but are descriptive proxies: high entropy is not quality and low entropy is not failure. 在本次复核中，`PLATFORM-MONITORING` 是 canonical owner；论文改变或测量的是该节点内的 state/data/control boundary，不把作者实现提升为通用产品结论。

完整方法、评价、关键反证与未披露字段见[该家族的原文审阅](../_sources/daily-20260605/V2_1_EVIDENCE_ARCHIVE.md#260605872--entropy-based-observability-for-ai-agent-behavior)；复用精确版本的证据，不继承旧报告完成标签或旧 owner。当前 Books 处置为已有覆盖：`PLATFORM-MONITORING`（[books/part-06-ai-infrastructure/67-monitoring.md](../../../../books/part-06-ai-infrastructure/67-monitoring.md))；现有正文对照及采用边界以本报告当前判断为准。

### [EMBER: Efficient Memory via Budgeted Evidence Retention for Long-Horizon Agents](https://arxiv.org/abs/2606.05894v1)

精确版本 `2606.05894v1` 的机制与适用条件：EMBER turns streaming episodes into source-backed evidence capsules, retains a budgeted cover before the future query is known and selects a chain at read time. Experiments test retention and answerability, but probe errors can discard future-critical evidence and generated capsules remain derived state that must preserve source identity and rebuild. 在本次复核中，`AGENT-MEMORY` 是 canonical owner；论文改变或测量的是该节点内的 state/data/control boundary，不把作者实现提升为通用产品结论。

完整方法、评价、关键反证与未披露字段见[该家族的原文审阅](../_sources/daily-20260605/V2_1_EVIDENCE_ARCHIVE.md#260605894--ember-efficient-memory-via-budgeted-evidence-retention-for-long-horizon-agents)；复用精确版本的证据，不继承旧报告完成标签或旧 owner。当前 Books 处置为已有覆盖：`AGENT-MEMORY`（[books/part-07-agent/77-memory.md](../../../../books/part-07-agent/77-memory.md))；现有正文对照及采用边界以本报告当前判断为准。

### [IA-RAG: Interval-Algebra-Driven Temporal Reasoning for Dynamic Knowledge Retrieval](https://arxiv.org/abs/2606.06044v1)

精确版本 `2606.06044v1` 的机制与适用条件：IA-RAG represents events as intervals and applies interval algebra when decomposing and retrieving temporal queries. The evaluation supports the covered temporal query types; extraction mistakes, incomplete event boundaries and the cost of relation expansion remain failure modes. 在本次复核中，`AGENT-RAG` 是 canonical owner；论文改变或测量的是该节点内的 state/data/control boundary，不把作者实现提升为通用产品结论。

完整方法、评价、关键反证与未披露字段见[该家族的原文审阅](../_sources/daily-20260605/V2_1_EVIDENCE_ARCHIVE.md#260606044--ia-rag-interval-algebra-driven-temporal-reasoning-for-dynamic-knowledge-retrieval)；复用精确版本的证据，不继承旧报告完成标签或旧 owner。当前 Books 处置为已有覆盖：`AGENT-RAG`（[books/part-07-agent/76-rag.md](../../../../books/part-07-agent/76-rag.md))；现有正文对照及采用边界以本报告当前判断为准。

### [Beyond Similarity: Trustworthy Memory Search for Personal AI Agents](https://arxiv.org/abs/2606.06054v1)

精确版本 `2606.06054v1` 的机制与适用条件：MemGate evaluates memory records before retrieval/use, treating privacy and harmful personalization as an admission decision rather than a prompt-only instruction. The threat model and experiments support the tested memories and attacks; classifier error, distribution drift and bypass through derived memories remain. 在本次复核中，`AGENT-MEMORY` 是 canonical owner；论文改变或测量的是该节点内的 state/data/control boundary，不把作者实现提升为通用产品结论。

完整方法、评价、关键反证与未披露字段见[该家族的原文审阅](../_sources/daily-20260605/V2_1_EVIDENCE_ARCHIVE.md#260606054--beyond-similarity-trustworthy-memory-search-for-personal-ai-agents)；复用精确版本的证据，不继承旧报告完成标签或旧 owner。当前 Books 处置为已有覆盖：`AGENT-MEMORY`（[books/part-07-agent/77-memory.md](../../../../books/part-07-agent/77-memory.md))；现有正文对照及采用边界以本报告当前判断为准。

### [Beyond Semantic Organization: Memory as Execution State Management for Long-Horizon Agents](https://arxiv.org/abs/2606.06090v1)

精确版本 `2606.06090v1` 的机制与适用条件：MAGE stores branches in a hierarchical state tree and derives active context only from the current valid path. Grow, Compress, Maintain and Revise bound context and isolate invalid traces. MemoryArena evidence supports the tested agents; bad validation or summary can still corrupt a whole subtree. 在本次复核中，`AGENT-MEMORY` 是 canonical owner；论文改变或测量的是该节点内的 state/data/control boundary，不把作者实现提升为通用产品结论。

完整方法、评价、关键反证与未披露字段见[该家族的原文审阅](../_sources/daily-20260605/V2_1_EVIDENCE_ARCHIVE.md#260606090--beyond-semantic-organization-memory-as-execution-state-management-for-long-horizon-agents)；复用精确版本的证据，不继承旧报告完成标签或旧 owner。当前 Books 处置为已有覆盖：`AGENT-MEMORY`（[books/part-07-agent/77-memory.md](../../../../books/part-07-agent/77-memory.md))；现有正文对照及采用边界以本报告当前判断为准。

### [TOKI: A Bitemporal Operator Algebra for Contradiction Resolution in LLM-Agent Persistent Memory](https://arxiv.org/abs/2606.06240v1)

精确版本 `2606.06240v1` 的机制与适用条件：TOKI types common merge heuristics as bitemporal operators with isolation preconditions, dual rows and keyed judge provenance. Proofs define replay consistency and audit preservation; the limited workload comparison claims no system superiority. 在本次复核中，`AGENT-MEMORY` 是 canonical owner；论文改变或测量的是该节点内的 state/data/control boundary，不把作者实现提升为通用产品结论。

完整方法、评价、关键反证与未披露字段见[该家族的原文审阅](../_sources/daily-20260605/V2_1_EVIDENCE_ARCHIVE.md#260606240--toki-a-bitemporal-operator-algebra-for-contradiction-resolution-in-llm-agent-persistent-memory)；复用精确版本的证据，不继承旧报告完成标签或旧 owner。当前 Books 处置为已有覆盖：`AGENT-MEMORY`（[books/part-07-agent/77-memory.md](../../../../books/part-07-agent/77-memory.md))；现有正文对照及采用边界以本报告当前判断为准。

### [ToolChoiceConfusion: Causal Minimal Tool Filtering for Reliable LLM Agents](https://arxiv.org/abs/2606.06284v1)

精确版本 `2606.06284v1` 的机制与适用条件：CMTF uses precondition/effect contracts to compute a minimal next-step tool frontier, reducing menus and token cost without relying only on semantic similarity. Its success depends on complete/correct contracts and state tracking. 在本次复核中，`AGENT-TOOL-CALLING` 是 canonical owner；论文改变或测量的是该节点内的 state/data/control boundary，不把作者实现提升为通用产品结论。

完整方法、评价、关键反证与未披露字段见[该家族的原文审阅](../_sources/daily-20260605/V2_1_EVIDENCE_ARCHIVE.md#260606284--toolchoiceconfusion-causal-minimal-tool-filtering-for-reliable-llm-agents)；复用精确版本的证据，不继承旧报告完成标签或旧 owner。当前 Books 处置为已有覆盖：`AGENT-TOOL-CALLING`（[books/part-07-agent/78-tool-calling.md](../../../../books/part-07-agent/78-tool-calling.md))；现有正文对照及采用边界以本报告当前判断为准。

### [TokenMizer: Graph-Structured Session Memory for Long-Horizon LLM Context Management](https://arxiv.org/abs/2606.06337v1)

精确版本 `2606.06337v1` 的机制与适用条件：TokenMizer turns session history into a graph whose summaries and links are mutable derived state; graph maintenance buys bounded context but adds stale-edge, summary-loss and rebuild failure modes. 在本次复核中，`AGENT-MEMORY` 是 canonical owner；论文改变或测量的是该节点内的 state/data/control boundary，不把作者实现提升为通用产品结论。

完整方法、评价、关键反证与未披露字段见[该家族的原文审阅](../_sources/daily-20260605/V2_1_EVIDENCE_ARCHIVE.md#260606337--tokenmizer-graph-structured-session-memory-for-long-horizon-llm-context-management)；复用精确版本的证据，不继承旧报告完成标签或旧 owner。当前 Books 处置为已有覆盖：`AGENT-MEMORY`（[books/part-07-agent/77-memory.md](../../../../books/part-07-agent/77-memory.md))；现有正文对照及采用边界以本报告当前判断为准。

### [Agent Memory: Characterization and System Implications of Stateful Long-Horizon Workloads](https://arxiv.org/abs/2606.06448v1)

精确版本 `2606.06448v1` 的机制与适用条件：The profiling harness separates memory construction, retrieval and answer generation, exposing a write-path/read-path cost frontier; ten systems and two suites characterize workloads but do not rank every production memory architecture. 在本次复核中，`AGENT-MEMORY` 是 canonical owner；论文改变或测量的是该节点内的 state/data/control boundary，不把作者实现提升为通用产品结论。

完整方法、评价、关键反证与未披露字段见[该家族的原文审阅](../_sources/daily-20260605/V2_1_EVIDENCE_ARCHIVE.md#260606448--agent-memory-characterization-and-system-implications-of-stateful-long-horizon-workloads)；复用精确版本的证据，不继承旧报告完成标签或旧 owner。当前 Books 处置为已有覆盖：`AGENT-MEMORY`（[books/part-07-agent/77-memory.md](../../../../books/part-07-agent/77-memory.md))；现有正文对照及采用边界以本报告当前判断为准。

### [Autoregressive Diffusion World Models for Off-Policy Evaluation of LLM Agents](https://arxiv.org/abs/2606.05558v1)

精确版本 `2606.05558v1` 的机制与适用条件：ADWM factors a policy-guided trajectory distribution into action-conditioned one-step transitions and alternates an evaluation LLM with latent diffusion denoising. Four agent benchmarks span dense, shaped, continuous and sparse reward; evaluation policies differ from behavior policies, and ranking correlation plus component ablations test the world-model estimator. The manuscript itself notes ground-truth episode uncertainty and an embedding adapter tied to the evaluation model family. Logged-su（完整论证及边界见下方原文审阅，不以此摘录代替它）

完整方法、评价、关键反证与未披露字段见[该家族的原文审阅](../_sources/daily-20260605/V2_1_EVIDENCE_ARCHIVE.md#260605558--autoregressive-diffusion-world-models-for-off-policy-evaluation-of-llm-agents)；复用精确版本的证据，不继承旧报告完成标签或旧 owner。当前 Books 处置为已有覆盖：`PLATFORM-EVALUATION-SYSTEM`（[books/part-06-ai-infrastructure/66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md))；现有正文对照及采用边界以本报告当前判断为准。

### [CLaaS: Continual learning as a service for sample efficient online learning](https://arxiv.org/abs/2606.05559v1)

精确版本 `2606.05559v1` 的机制与适用条件：CLaaS wraps collection, replay, asynchronous parameter updates and checkpoint exposure behind a chat-compatible service. The experiment uses 100 adversarial instruction-hierarchy scenarios split into five non-stationary stages; an adaptive attacker changes as the defender learns, and the paper compares forward/backward transfer across update methods. This demonstrates a prototype adaptation loop, not production safety under broad workloads or model families. Asynchrony makes policy version, samp（完整论证及边界见下方原文审阅，不以此摘录代替它）

完整方法、评价、关键反证与未披露字段见[该家族的原文审阅](../_sources/daily-20260605/V2_1_EVIDENCE_ARCHIVE.md#260605559--claas-continual-learning-as-a-service-for-sample-efficient-online-learning)；复用精确版本的证据，不继承旧报告完成标签或旧 owner。当前 Books 处置为已有覆盖：`AGENT-PLATFORM`（[books/part-07-agent/84-agent-platform.md](../../../../books/part-07-agent/84-agent-platform.md))；现有正文对照及采用边界以本报告当前判断为准。

### [Statistical Priors for Implicit Preferences: Decoupling Skill Selection as a Local Harness in Personal Agents](https://arxiv.org/abs/2606.05828v1)

精确版本 `2606.05828v1` 的机制与适用条件：The proposed personal-agent harness keeps a local statistical prior over user skill preferences and separates skill selection from remote language interpretation. This improves privacy and latency boundaries when preferences are stable, while sparse observations, drift and incorrect local priors can route the wrong action. 在本次复核中，`AGENT-PLATFORM` 是 canonical owner；论文改变或测量的是该节点内的 state/data/control boundary，不把作者实现提升为通用产品结论。

完整方法、评价、关键反证与未披露字段见[该家族的原文审阅](../_sources/daily-20260605/V2_1_EVIDENCE_ARCHIVE.md#260605828--statistical-priors-for-implicit-preferences-decoupling-skill-selection-as-a-local-harness-in-personal-agents)；复用精确版本的证据，不继承旧报告完成标签或旧 owner。当前 Books 处置为已有覆盖：`AGENT-PLATFORM`（[books/part-07-agent/84-agent-platform.md](../../../../books/part-07-agent/84-agent-platform.md))；现有正文对照及采用边界以本报告当前判断为准。
