# 2026-02-20 已有 Daily 增量补查

作者：supplement_20260220；仅本日 README/_sources 写权。新增窗口北京时间 2026-02-19 完整自然日；旧 09:00 窗口、96候选及其日期/评分/有效 Source、Books 判断冻结。本轮不写 Books、LS、月索引，不 stage/commit/push。

## 1. baseline 与当前范围

启动完整副本：`/private/tmp/daily-20260220-supplement-20261008-baseline.md`，实际 107421 bytes；原 README 同为107421 bytes，SHA256均为 `e901d92dfe013c5fa008329282ac5782304ef9b10b646c19a0a27cc4fbb32d84`。原候选96行与§4连续原正文用于逐字保留核验，不用输出截断片段当baseline。当前AGENTS、研究/来源/Report合同、Prompt、ROADMAP已完整重读，LS仅路由。

## 2. 实际入口与发现停止

十四Daily入口当前raw及HTTP/bytes/执行时间见 `supp-20261008-fetch.json`；403/空响应不作0命中。机构历史切片先复用原已有效source事实，再定点核目标日邻接；不以当前目录授完整历史覆盖。

arXiv四个窄主题查询均限定 `submittedDate:[202602171900 TO 202602181900]`、start0/max200，覆盖潜在Feb19公告池但只负责发现，不证明公开日期。实际返回language104、system12、multimodal63、agent97，共276次非去重命中；每组total小于200、已达本查询末项，不分页扩历史。全查询原件 `supp-20261008-ARXIV_{language,system,multimodal,agent}.raw`；与原四组精确事件身份比对，原96和有效既有排除/保留不展开全文。扩展同义表达为distillation/neural collapse、communication、flow matching/tokenization、RAG/memory retrieval/tool calling；不是全分类队列。

官方 `list/cs.CL/2026-02?show=2000` 只返回月度ID题名、没有Feb19公告标签；仅用于有限相关题名backstop/身份恢复，1935月库存不成为逐项题摘或全文队列。两个尝试的日级list路径与Advanced announced_date页web均Cache miss，API的published/updated不作首次公开证据。

## 3. 首包完整题摘与独立校准请求

八份 exact-v1 abs实际完整题摘已读并保存在 `supp-20261008-ABS-<ID>v1.html`。当前API对16169/16543的摘要已不同于v1，以下只采用v1；不据later修订倒填。日期尚未授落窗，拟保留不评分或展开全文，等非作者准入校准后定点恢复必要公开日。

| ID / 精确题名 | 原约束 → v1实际增量 → 具体选择 | 初筛处置 |
| --- | --- | --- |
| 2602.16034 FeDecider: An LLM-Based Framework for Federated Cross-Domain Recommendation | 异域LoRA更新幅度导致聚合偏向 → 分享方向而非幅度、每客户学习他域权重 → 模型适配合并要分开坐标方向与本地权重，不能只按领域推荐指标排除 | 潜在贡献，TRAIN-LORA；需机制/幅度对照；缺首次公开日期 |
| 2602.16169 Discrete Stochastic Localization for Non-autoregressive Generation | draft分布漂移使remasking步数贵 → 单SNR-invariant denoiser跨连续corruption与masked端点训练 → sampler步效不必只靠新增推理策略，训练通道的适用条件需核 | 潜在贡献，MULTIMODAL-GENERATIVE-PARADIGMS；v1只保MDLM/ReMDM命题，不借v2的random-order/hybrid48；缺首次公开日期 |
| 2602.15984 Verifier-Constrained Flow Expansion for Discovery Beyond the Data | 既有flow只采高数据区 → 定义strong/weak verifier并在noised空间做受约束entropy/mirror-descent expansion → verifier角色改变生成支集/有效性约束，不只是分子任务指标 | 潜在贡献，MULTIMODAL-GENERATIVE-PARADIGMS；一般生成方法与纯AIforScience应用区分请求校准；缺首次公开日期 |
| 2602.16543 Vulnerability Analysis of Safe Reinforcement Learning via Inverse Constrained Reinforcement Learning | 黑盒victim无梯度/真约束 → demonstration与黑盒环境交互拟surrogate constraint/policy → 安全controller的观测攻击权限不能只按victim白盒访问判断 | 潜在贡献，MULTIMODAL-EMBODIED-VLA/安全交接；v1不是current-v2的no-query、仅demonstration命题；需主线范围校准及必要日期 |
| 2603.06603 Scale Dependent Data Duplication | 小模型近duplicate梯度仍表面相关 → scale后semantic duplicate梯度更一致与finite unique pool loss处罚 → 去重及scaling extrapolation需随模型能力/独特人口变化 | 潜在贡献，TRAIN-DATA；Submitted Feb18不证明公开，March ID不作为排除日期证据；必要首次公告/作者dated正文尚缺 |
| 2602.16503 Interpretability-by-Design with Accurate Locally Additive Models and Conditional Feature Effects | GAM/GA2M到局部阈值shape functions及region-aware backfit → tabular监督分类/回归解释性折中 | 范围关闭：未建立foundation model/当前系统机制或相应理论假设迁移；不是因小模型而排除，日期无需恢复 |
| 2602.16564 A Scalable Approach to Solving Simulation-Based Network Security Games | network PSRO中top-k设备过滤、beam search、量化state Q缓存与k-hop invalidation → 网络博弈应用效率 | 拟范围/贡献关闭：未给当前模型计算/LLM Agent/state机制的可迁移新条件；缓存命名/系统类比不足，供代表EX校准 |
| 2602.16634 Enhanced Diffusion Sampling: Efficient Rare Event Sampling and Free Energy Calculation with Diffusion Models | BioEmu equilibrium到thermodynamic unbiased估计、Umbrella/Meta/ΔG算法 → 分子动力学rare-event与free-energy | AIforScience暂停范围关闭；不借生成owner重引入物理观察量应用，日期无需恢复 |

明确领域题名在发现层关闭：2602.16020 molecular crystal、16249 microscopy segmentation、16548 RNA inverse design、16656 solar polar field、16523 quantum state preparation、16525 smart grids、16063 local energy markets；未将这些题名扩成全文队列。2603.00104 Alpha-RF完整摘要已读：neural Maxwell simulator+RL RF-filter设计，范围关闭AIforScience/领域电磁设计，不把amortized inference叫通用模型突破。

## 4. 机构定点复核初步

- OpenAI Feb19 Alignment Project资助原文与原有效关闭身份一致，不重列候选；Research HTTP403不证明无事件。Google Gemini3.1Pro Feb19官方正文已完整核心复查：preview、benchmark与demo，没有新增可核机制/受控资源条件；复用贡献关闭，model card发布日期只是独立事件线索，需有限核其评价/安全说明是否另有贡献。
- Anthropic dated Research嵌入列表目标邻接Feb18 measuring-agent-autonomy → Feb23 persona-selection/AI-fluency；停止跨窗段，不把CMS `_updatedAt`当发布。ZAI Research目标邻接Feb11→Feb21，ERNIE博客Feb6→Apr15，MiniMax en Feb14/12→Mar18。这些当前可恢复目录与原有效事实相同；未恢复历史删除事件继续隔离。

## 5. 当前停点

root于2026-10-08实际独读八exact-v1完整题摘，五潜力准入/三EX校准通过。15984通用生成机制不因分子demo全部关闭；16543只可保SafeRL observation/constraint威胁接口，不借VLA成功或v2权限。早先本文件16543题名已按exact-v1正式题名纠正（不是另一篇/新家族）。

## 6. 必要日期/精确版本有限恢复与请求

实际本轮查询见fetch记录及以下具名路径；提交、Atom、DOI、编号和搜索索引不证明首公开。没有日期而暂未读必要正文不称Evidence完成。

| 身份 | 已实际恢复与不足 | 本窗终态与定点重开 |
| --- | --- | --- |
| 16034 FeDecider | exact-v1 abs只有Submitted Feb17；作者仓库 `https://github.com/Xinrui17/FeDecider` 当前只有README，未有dated论文首次公开；题名+Feb19/作者域定点搜索没有必要原公告 | 日期保留；需同ID Feb19官方announcement或作者明确dated首次正文；不以仓库creation/commit代替论文公开，不开展采用链 |
| 16169 DSL | exact-v1 abs只有Submitted Feb18；当前API摘要已换，另发现2605.12836同题作者重叠，不能据此重算原v1首次日期；题名+Feb19/作者/代码定点补检只见索引提交日期和另OpenReview匿名稿 | 日期保留；需16169v1精确首次公告或同正文作者dated公开；不借May版本机制，不穷比全部revision |
| 15984 Flow Expansion | exact-v1 abs只有Submitted Feb17；OpenReview IfDYQbsWf4 forum browser-challenge，api2及api official均403（原件JSON保存）；conference原件只写ICLR2026，作者LinkedIn只可定位April宣传，未证明首次Feb19 | 日期保留；需精确首次公告/作者dated正文或OpenReview明确publication-date公开原note；不把forum created/submission当发布，不遍历会议 |
| 16543 SafeRL | exact-v1 abs只有Submitted Feb18；作者 `jialiangfan.com` news仅 `[Feb 2026] ... now available on arXiv`，无day（保存JIALIANG-date）；定点题名搜索恢复xjDgITlk7a匿名稿线索，索引年份不证明公开日 | 日期保留；需Feb19原announcement或作者day-dated同版正文；不借JST索引Updated Feb19或v2 no-query；不继续无关攻击全文 |
| 2603.06603 Duplication | exact-v1保留Submitted Feb18但March编号本身不证公开；作者Abhay publications只2026（原件ABHAY-date），StanfordCS191 Winter2026页面/作者稿只是学期/年；题名+day定点搜索无必要day | 日期保留；需原官方首次announcement或作者dated同正文；不授March归属，不为日期展开scaling全文 |
| Gemini3.1Pro Model Card | 官方HTML明确 `Published 19 February 2026` 支持card发布事件；实际取PDF875842 bytes/封面Feb2026，但GCS HEAD `last-modified: Thu, 23 Apr 2026 11:01:09 GMT`、generation1776942069092818，存在窗后artifact变化。当前PDF p7 Cyber成本归一化DeepThink反侧与p3/MRCR1M反侧已读，只作必要恢复线索，不能证明Feb19历史正文有这些实验 | 仅历史内容版本保留；需Feb19原card/PDF或官方明确该两条原始dated说明，定点核p3/7所需内容即可，不索全部附件。发布事实不因April修改被否定，当前反侧不进入本窗候选/Books或安全保证 |

以上五个日期项+一个card版本项均精确隔离，不作为正面候选、Books或覆盖断言。一次材料请求合并于此；可用原入口已有限恢复，普通日期工作0。旧A2H/21早Submitted/六跨截止/16100等原保留与有效争议仍沿原报告不变，不合并为新候选数。

## 7. Source实际停止补充

原有效历史检查切片在README保留；本轮只处理差额，以下不授无遗漏。

| 来源 | 实际本轮与停止 | 权限/缺口 |
| --- | --- | --- |
| SRC-OPENAI | Research403；window+research定点恢复Alignment Project datedFeb19原说明，资助身份与原有效关闭一致 | 原关闭复用；历史Research切片未恢复隔离，403不是无事件 |
| SRC-ANTHROPIC | 当前嵌入dated Research列表读Feb18 autonomy→Feb23 persona/fluency跨窗，停止此区段 | 当前可恢复列表已检查，CMS updatedAt不作事件；历史删除不认证 |
| SRC-GOOGLE-AI | DeepMind Research当前入口；Research pubs curl timeout、web恢复仅year/title排序(1–15/11600)，不全扫；Google Blog Feb19 Gemini正文核心有效原关闭；card历史精确版保留见§6 | 当前目录不能恢复Feb19历史主题切片，隔离；不据当前card旧日期倒填 |
| SRC-META-AI | Research reset；官方Blog首屏与原9卡片Mar10以后身份相同；page2实际curl reset，目标日期+model窄搜索无可恢复原目录 | 历史分页受阻终态隔离，不把空检索证明0 |
| SRC-QWEN | 旧Blog及/blog home bundle初步受限后，恢复官方GET `https://qwen.ai/api/v2/article/retrieval?type=qwen_ai&language=en-US`：success=true/data.articles实际40，extra.date+path目标邻接2026-02-16 qwen3.5→2026-03-19 qwen3.5-max-preview，已到此返回末；不展开窗外正文 | 动态当前40名单已检查，未将repo单系列News或无正文root授完整历史Coverage；仅当前可恢复名单，不认证删除条目 |
| SRC-DEEPSEEK | 当前官网入口，旧有效Research/update切片复用Apr24→Dec1,2025边界，Feb19定点官方域补检未恢复新必要事件 | 已检查可用部分，缺完整历史目录隔离；无可见命中不授全0 |
| SRC-MOONSHOT | Platform Blog当前27条最晚Nov7,2025已到末；官方org本轮curl25s timeout，未遍历repo/commit | 不存在本窗原blog切片；隔离，不把org作为paperfirstpublic |
| SRC-TENCENT-HUNYUAN | 从Research实际JS确定api.hunyuan.tencent.com publicList POST，pageNum1/pageSize100/renderType0，en9/zh11与原身份一致；displayPublishTime目标前Feb13与Feb3 | 真9/11末项已到，未展开窗外正文；只授此返回列表，wronghost未作0 |
| SRC-ZAI | 官方Research当前dated目录目标邻接Feb11→Feb21；原Feb12GLM5/Feb3OCR release切片复用 | 跨窗段停止，不合并CMS UTC更新时间与显示日 |
| SRC-BYTEDANCE-SEED | 实际GET `/api/get_article_list_v2` article_type1/2,publish_year2026,page_token空,count20,order_descfalse；首POST404错误已纠正，不作0；type1实际20/total82/next20/has_more，BJT目标邻接Feb13→Feb25；type2实际9/total23/next20/has_more，BJT Feb14→Apr1。与原IDs完全一致 | 按实际升序跨窗段停止，不称82/23全读完，不追无关后页 |
| SRC-BAIDU-ERNIE | 官方博客首10 dated cards Apr15→Feb6→Jan29跨窗；同原身份 | 目标边界停止；不认证删除历史 |
| SRC-XIAOMI-MIMO | 官网/Blog当前说明与Paper index8文件身份，旧有效Mar13→Feb3 paper切片复用；新目录页没有发布日 | Paper可用部分已检查；Blog历史date slice未恢复隔离，不以目录文件时间反算 |
| SRC-MINIMAX | en与cn当期dated cards，分别ForgeFeb14/Feb12及M2.5Feb12→Mar18邻接；Agent技术blog原May13单项有效切片复用 | 同language独立边界停止；原technical历史缺片不被主blog全覆盖 |
| SRC-ARXIV | 四窄查询276次非去重发现皆total<200达末、194身份，实际路由80原候选+23具名V3原EX/hold+91差额；差额55完整AB、36明确题名关闭。官方CL月列表只limited title backstop，LG月列表curl20s在1.8MB/3.15MB截断，不使用截断回复作全名单；Advanced公告day请求返回form error，官方表单明确Announcement仅year/month粒度 | 不把submitted query或月announced当day。最终27潜力+原日期限制隔离；窄来源覆盖只按实际查询，不授全学科/互联网召回 |

以下§8修正先前将原query出现视为有效关闭的路由：旧记录的“后月ID”不是日期证据。只重开实际受影响身份，不把276次命中变成全文队列。

## 8. 四query身份路由与受影响集合

实际276次命中去重为194身份；原四query去重185，本轮相对原query新增25身份：16063/16169/2603.00104/16503/16523/16525/16543/16548/16564/16609/16642/15984/16020/16054/16086/16092/2603.06603/16229/16249/16498/16601/16634/16656/16034/16587（未列前缀均2602）。新query身份不等于新候选。

194的互斥路由：原96候选表中80精确身份复用；23具名原有效判断复用；91没有有效旧处置，其中55完整题摘语义检查、36明确领域题名关闭。55中首包八exact-v1+AlphaRF共9、受影响增补46；判为27潜力日期未定、28贡献/范围关闭。55不表示必要证据完成。原query185的存在只证发现，不证已筛；旧“后月ID”范围理由在本轮撤销，凡相关含糊都按完整题摘重开。

23非候选复用的具体依据：`V3_ADMISSION_NEXT.md` B3完整题摘关闭16038/16085/16131/16201/16467/16640/16105/16512及16238；`V3_QUERY_LEADS.md`完整题摘关闭16039/16209/16742、16736一次core关闭；`V3_CORE_DECISIONS.md`16343 codec标签只影响专门spoof-detector、16608成熟IG融合无新归因条件；16241撤回依据在`V3_EVIDENCE_SEVENTEENTH.md`。日期/身份保留16740/16741/16746/16760/16763见`V3_QUERY_LEADS.md`，16200 thesis首公开与16100同版identity冲突见`V3_CORE_DECISIONS.md`。共16关闭（含撤回）+7原保留，不使用V2.1的435账本代替这些V3判断。

增补46完整AB采用四个本輪Atom原件的官方完整summary；current为v2的P-GRPO/RoboLayout/CADReasoner/PhysGen/STAR/V2X另取exact-v1 abs原件，未借later增量。16343额外读过当前AB但归原处置复用，不加55计数。标题/摘要身份都可在上述原件定点复查，不伪称读过全文。以下22为首包五潜力之外的准入校准请求，全部仅潜力、不评分/候选/Books。

| exact-v1身份 / 题名 | 原约束 → 实际增量 → 可改变的选择 |
| --- | --- |
| 2603.10009 Personalized Group Relative Policy Optimization for Heterogenous Preference Alignment | 群内exchangeable假设混异质偏好 → preference-group历史reward归一化替当前batch → advantage人口需分责；TRAIN-GRPO |
| 2603.10011 Gemma Needs Help: Investigating and Mitigating Emotional Instability in LLMs | distress输出并非base家族固定属性 → base/instruct方向相反、280pair DPO抑制跨tone/length负侧 → posttraining行为评价不以基础能力推安全；TRAIN-DPO |
| 2603.06604 Know When You're Wrong: Aligning Confidence with Correctness for LLM Error Detection | reward训练后confidence不等correctness → anchor归一分数与post-RL selfdistill/SFT恢复 → confidence触发检索需绑定训练历史；TRAIN-RLHF/评价 |
| 2603.00105 LIDS: LLM Summary Inference Under the Layered Lens | summary相似度不授theme关键词显著性 → BERT-SVD方向、重复prompt不确定性与SOFARI/FDR → 主题解释应保统计错误预算；PLATFORM-EVALUATION-SYSTEM，不授summary真值 |
| 2603.05522 RoboLayout: Differentiable 3D Scene Generation for Embodied Agents | semantic layout不等可达 → 显式agent reachability及冻结其他物件local refinement → 场景条件需机器人能力接口；MULTIMODAL-EMBODIED-VLA |
| 2603.12270 Task-Specific Knowledge Distillation via Intermediate Probes | teacher正确表征被vocab projection/答案格式污染 → frozen hidden probe labels替output logits → distill监督对象可绕readout瓶颈；TRAIN-PRETRAINING |
| 2603.12271 Diagnosing Retrieval Bias Under Multiple In-Context Knowledge Updates in Large Language Models | single-update通过不授连续更新 → 多历史有效值时earliest保留/latest衰退且diagnostic flatter → context更新正确性须测endpoint与冲突历史；MODEL-LONG-CONTEXT |
| 2603.12272 ActTail: Global Activation Sparsity in Large Language Models | uniform projection稀疏放大质量损失 → 重尾exponent理论配置各projection budget → 稀疏budget需权重异质条件；INFER-TENSORRT-LLM |
| 2603.12273 Aligning Language Models from User Interactions | raw followup无显式reward被弃 → hindsight条件token分布回蒸馏当前policy → 可从user互动学习而非只pair preference；TRAIN-RLHF |
| 2603.00110 Learning Physics from Pretrained Video Models: A Multimodal Continuous and Sequential World Interaction Models for Robotic Manipulation | video pretrain与动作接口分离 → shared连续video/action physical tokens+AR transition → video能力到控制需表示接口，不授simulation物理真值；MULTIMODAL-WORLD-MODELS |
| 2605.00005 Cloud Is Closer Than It Appears: Revisiting the Tradeoffs of Distributed Real-Time Inference | 通信抖动默认cloud不适合control → sensing频率/throughput/network/safety形式边界 → 控制部署看端到端deadline条件而非只RTT；MULTIMODAL-EMBODIED-VLA，May编号不证明日期 |
| 2603.08726 Data-Rate-Aware High-Speed CNN Inference on FPGAs | pool/stride后层速率使full-unroll闲置 → multi-pixel rate-aware配置保持连续dataflow → 小模型执行也可给资源利用约束；INFER-TENSORRT-LLM |
| 2602.16362 How Reliable is Your Service at the Extreme Edge? Analytical Modeling of Computational Reliability | consumer容量波动不能由平均throughput保证 → bounds-only vs历史MLE概率、series/parallel/partition allocation → streaming可行性需容量满足概率；INFER-SCHEDULING |
| 2602.16480 SRFed: Mitigating Poisoning Attacks in Privacy-Preserving Federated Learning with Heterogeneous Data | 加密聚合隐藏poison且NonIID冲突 → decentralized functional encryption+layerprojection clustering → privacy与Byzantine过滤必须联合权限；TRAIN-DISTRIBUTED-TRAINING |
| 2602.16182 World Model Failure Classification and Anomaly Detection for Autonomous Inspection | 可预测输出不判success/OOD → 两CP decision functions分success/knownfailure/anomaly → worldmodel到行动acceptance需分失败与分布外；MULTIMODAL-WORLD-MODELS |
| 2602.16681 VETime: Vision Enhanced Zero-Shot Time Series Anomaly Detection | vision全局与1D时域local互失 → reversible image+patch时间对齐/dynamicfusion → 跨模态事件须保shared timeline，不由单榜选表示；MULTIMODAL-REPRESENTATION |
| 2602.16037 Optimization Instability in Autonomous Agentic Workflows for Clinical Symptom Detection | continuedprompt优化默认更好 → lowprevalence下sensitivity oscillation/active指导恶化而retrospective selector稳定 → 优化停止/验收不只accuracy；AGENT-WORKFLOW，限一般优化failure不采用临床判断 |
| 2602.16174 Edge Learning via Federated Split Decision Transformers for Metaverse Resource Allocation | globalFL同质聚合且local全模型贵 → local embedding/prediction+cloudshared layers → 异质DT客户端边界可分参数与训练责任；TRAIN-DISTRIBUTED-TRAINING |
| 2602.16379 Label-Consistent Data Generation for Aspect-Based Sentiment Analysis Using LLM Agents | agent流程收益与prompt增强混杂 → 同模型同instruction匹配baseline、label preservation与modelpretraining交互 → synthetic验证loop需拆机制和student能力；TRAIN-DATA，限局部对照 |
| 2602.16188 Deep TPC: Temporal-Prior Conditioning for Time Series Forecasting | frozenLM浅时间cue逐层消失 → 多深度time-token crossattention仅训modules → 时间语义可与signal分开多深注入；MULTIMODAL-REPRESENTATION |
| 2602.16629 Almost Sure Convergence of Differential Temporal Difference Learning for Average Reward Markov Decision Processes | convergence依state-visit localclock无法非tabular推广 → standard diminishingLR onpolicy nstep收敛及offpolicy三个条件 → average-reward训练不能借不实行clock的理论；MULTIMODAL-EMBODIED-VLA，限RL控制假设 |
| 2603.06605 Structure-Aware Set Transformers: Temporal and Variable-Type Attention Biases for Asynchronous Clinical Time Series | grid需impute/set丢时序与type → 可学习timescale与typeaffinity attentionbias及10深度fusion → eventtokenizer不只避discretization，还须恢复时间/类型关系；MULTIMODAL-REPRESENTATION，限一般表示接口不采用ICU结论 |

增补24 AB排除（加首包4共28）：10012军事refusal排行与已有abliteration仅域内answer-rate/能力取舍；29848 AgentFixer旧rule/judge诊断+prompt/code修改未建新条件；29847 CAD局部render-refine与scan协议未建model通用grounding条件；08725三个硬件的一个PicoSAM任务排名未揭示新执行/可迁移资源条件；16053治疗criteria使用已有MODPO对照未新增通用优化机制/约束；16061 shadow-variable是缺失业务结果的统计识别，LLM只是proxy来源；16435 causal softprior/hierarchicalDQN专注tabularAFE，未新增foundation/LM训练条件；16626 MEG生物tokenization属暂停科学应用；16430 OCR已有模型fine-tune vs新拼backbone的目标语言rank/latency未控制架构/预训练预算；16738边fog/cloud+PPO/voting是IIoT任务模块拼接未建新执行条件；16298 MultiCW只新balanced/OOD任务人口及排行；16578 poetry workshop艺术产物未给model/state机制；16290 Arabic sharedtask只是已有model方言训练；16019 MedProbCLIP旧Gaussian/variationalbottleneck作用临床retrieval，未新增通用表示机制；15958 DocSplit新任务/pageorder及度量不提供原评价混杂证据；16747 LiveClin临床判断/新caseboard为暂停科学应用且无证“withoutleakage”；00102 socialrobot四建议+illustrative case未给可检验新机制；16502 DressWild已有VLM pose-normalize+featurefusion仅garment pipeline；16611 gloss/style latentadapter只目标艺术控制，无新disentanglement条件；16073 ScenicRules传统driving规则优先图与scenario无foundationmodel接口；16468 HPMixer旧周期/MLP/wavelet/patch组合仅forecast排行，无新的表示或学习条件；16385 scenecompletion成熟channel/spatialgate提高NYUv2/local小物件，不授worldstate或行动接口；16569 Arc2Face既有identity模型应用morph检测，未给新威胁权限或模型安全边界；06607 V2X干扰games比较传统MARL的topology效果，未建立LM Agent/当前学习机制的新条件。排除日期不影响处置，不请求日期。

36题名关闭（未称读完整AB）：暂停科学/临床/生物应用15951/16050/16749/16216/16264/16273/16320/16523/16548/16684/16696/17726/16006/16020/16110/16249/16422/16656/16554/16585/16650/16703；传统特定领域预测/资源/文本任务16730/16735/16062/16063/2603.04433/16516/16525/16590/16607/2603.00112/16140/16186/18506/16678。原完整title身份在四raw内；这里只据明确题名语义关闭，不称通用方法无学术增量，不授全学科召回。

27潜力的必要日期依赖为各自exact-v1首次公开day，不是Submitted/当前Atom或March/MayID。§6五项各自恢复点保持；上述22项共享官方day公告恢复失败（Advanced announced_date实际formerror、日级list不能恢复）而必要信息分别仍缺，当前只能隔离，不能把API首次submitted填公开列。可接受替代为同身份官方Feb19首次announcement或作者day-dated首次完整正文；每项只在该身份恢复，不查精确时刻、整月或全部revision。它们不正面采用、不评分、不写Books，不称已做标准/深入Evidence。card历史artifact另1，合计28新终态保留；root已实际逐条读新增22完整AB（P-GRPO/RoboLayout/PhysGen/STAR另读保存exact-v1），新增22潜力准入校准通过；代表EX10012/29848/15958/16298/16738/06607/16061/16385完整AB独核维持具体排除，未授其他EX全量独核。仅potential校准，不授长期贡献/Source/日期/Books或日级通过。普通题摘筛选已完成，不再扩全文。

## 9. 后补22必要日期的有限补检停止

<!-- 本节有限恢复记录保持；最终非作者结论见§10。 -->

本轮实际web六批共22个具名查询，不是零结果：第一批 `"Personalized Group Relative Policy Optimization" "February"`、`"Gemma Needs Help" "February"`、`"Task-Specific Knowledge Distillation via Intermediate Probes" "February"`、`"Aligning Language Models from User Interactions" "February"`；第二批 `"RoboLayout" "February"`、`"Cloud Is Closer Than It Appears" "February"`、`"ActTail" "February"`、`"Diagnosing Retrieval Bias" "February"`；第三批 `"Know When You're Wrong" "2603.06604" publication`、`"LIDS" "LLM Summary Inference" "February"`、`"Data-Rate-Aware High-Speed CNN" "February"`、`"Learning Physics from Pretrained Video Models" "February"`；第四批 `"How Reliable is Your Service at the Extreme Edge" publication`、`"SRFed" "February"`、`"World Model Failure Classification" "February"`、`"VETime" "February"`；第五批 `"Optimization Instability in Autonomous Agentic Workflows" "February"`、`"Edge Learning via Federated Split Decision Transformers" "February"`、`"Label-Consistent Data Generation" "February"`、`"Deep TPC" "February"`；第六批 `"Almost Sure Convergence of Differential Temporal Difference Learning" "February"`、`"Structure-Aware Set Transformers" "February"`。每query仅本次返回结果；未翻月列表/后页，未打开无关项。

结果仅恢复身份/作者页面/索引，未取得必要first-public day：ResearchTrend的10009/16037用Feb17、AlphaXiv的Robo/PhysGen/Probe/16182用Feb18与Submitted一致，不能升格公开；[SciRate06604](https://scirate.com/search?q=au%3ABenjamin_Y+in%3Acs)显示Mar10与[ArxivSignals06604](https://arxivsignals.io/papers/2603.06604)一致，但这不是原官方公告或首次作者正文，不据此授March owner。[J-GLOBAL16362](https://jglobal.jst.go.jp/en/public/202602213559062933)分publicationFeb18/updateFeb19，与arXiv submitted搜索结果区分，不用update证明公开。[AIModels16362](https://www.aimodels.fyi/papers/arxiv/how-reliable-is-your-service-extreme-edge)显示Published2/19但辅助权限不够；[PaperityVETime](https://paperity.org/p/374354132/vetime-vision-enhanced-zero-shot-time-series-anomaly-detection)也仅索引February19。[Idan作者列表](https://www.idanshenfeld.com/collection-archive/)有12273精确作者身份但无首次day，且另一同题2025不同作者必须分家族。ResearchGate多数仅February2026或DOI，不授day；其正文节选不用作Evidence。未拿空匹配/搜索日期填公开列。普通有界恢复已达到当前停止，27身份仍各保原公告/作者dated首次正文请求，不无限搜索。

## 10. 本轮非作者日级验收

复核者：root；结论：通过，仅验收增量补查安全终态，不重新认证冻结96项的原日期。

实际核四窄查询参数/返回末项、十四来源有限停止及其失败权限；Qwen当前40条extra.date实际复核，当前目录不证明历史删除项。276跨组命中归194身份而非276当窗论文：80原候选、23具名有效旧判断、91差额。首批8题摘沿实际独核复用；新增22完整AB逐条读，P-GRPO/RoboLayout/PhysGen/STAR另读保存exact-v1，均仅获潜在增量校准，不授公开日期、长期结论或必要Source完成。实际抽读10012/29848/15958/16298/16738/06607/16061/16385八个分层EX，并补16569/16019两个带安全措辞的EX；各自具体领域/组合或评价缺增量理由维持，不以小模型/局部理论统一排除。其余明确EX不称全量独核。

27潜力的必要首次公开日及card1历史内容版本均具名隔离。实际card HEAD的April23改写不能倒填Feb19内容，官方发布日期不因此被否定。没有新增确定候选或Books写入，日期保留不推动全文队列；本轮六部分、原96行/窗口/连续§4逐字保留与精确重开条件通过。没有普通可执行扫描、筛选、审阅或写入未完；允许作者转完成态复验，未恢复的历史目录/日期/内容不授Coverage/Evidence、无遗漏或安全性能保证。未stage、commit、push。
