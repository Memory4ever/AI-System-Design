# Daily Research — 2026-03-26

**规范：** V3
**窗口：** 2026-03-25T09:00:00+08:00 ～ 2026-03-26T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-10-12T22:30:00+08:00
**窗口说明：** 用户明确要求仅补已有2026日报遗漏；原窗口、ModelSpec事件行/日期/评分及原§4连续内容冻结，旧完成声明不代替本轮验收。
**补充窗口：** 2026-03-25 ～ 2026-03-25

## 1. 结论

原报告候选1个唯一家族 Model Spec 发布说明及 Evals 的事件行、日期、7分和原证据段落冻结，有效 Ch66 两段及旧非writer检查保留。本轮只补03-25完整自然日，不搬移旧材料；新增确定37个家族的日期/准入由非报告作者分批独立校准，来源与筛选有限范围现已冻结，连旧ModelSpec共38家族。新增32项实际整合及真实非writer写后复核通过，3项具体已有覆盖通过、没有重复写Books；DPPN/CMM两项中心主张冲突保留原6分贡献候选、暂缓Books并隔离争议正面采用，合计37安全处置。BrainMisalign经实际owner核查从仅输入embedding的Ch12修正为soleCh5表示功能干预，6分/日期不改。Gaze实际写后复核已通过，物理机器人与配方冲突仍隔离。全部新增候选已获安全处置，必要Books均落实、真实nonwriter POST并经root实际接纳；非报告作者完整六部分DAY已通过并获root实际接纳；本轮完成表示约定范围已处理到安全终态，不表示所有来源或论文中心主张得到正面验证。

原09→09窗口的23潜在线索保留原身份记录，不作为本轮23项新增证据池：19项按已读v1 Submitted与官方最早公告日下界确定不属25，PCR/TRAP已在新增候选独立处理，仅StepCache/Lightning首公开范围仍跨窗隔离。四主题 API 交叉返回84条仅为有限发现，不是84个当日新家族或逐项全文队列；本轮另两页50槽也不转全分类工作。旧报告完整保留在[原文](../_sources/daily-20260326/V3_LEGACY_REPORT.md)，不继承旧EffectiveDate或完成标签。

## 2. 来源覆盖

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | 本轮实际 RSS 782648B/1287 items，仅Mar24～26五邻接title/link/pubDate；ModelSpec旧事件冻结去重，SafetyBugBounty与03-25既有有效家族定点去重，[原字段](../_sources/daily-20260326/SUP_OPENAI_RSS_FIELDS_20261012.json) | 已检查 | 当前可恢复的定点历史切片，不认证全站；旧RSS快照不冒本轮计数 |
| SRC-ANTHROPIC | 本轮Research March九项完整publishedOn/slug/title重新提取，[原字段](../_sources/daily-20260326/SUP_DAILY_DIRECTORY_FIELDS_20261012.md)；23T23Z三篇及24T10:41Z均25自然日前，31T22:17Z后 | 已检查 | 仅当前March数组未见25，不扫描科学应用/历年全站 |
| SRC-GOOGLE-AI | ResearchMarch page1实际12 cards；DeepMind正确path3 24cards/六March日期字段独核；Research动态Next、指定Marchpage2与pubsyear失败，浏览器恢复亦timeout，[必要恢复/停止](../_sources/daily-20260326/SUP_GOOGLE_RESEARCH_RECOVERY_STOP_20261012.md) | 受阻 | 仅Research下一页与pubs本窗datedslice隔离；不授Google全Coverage/zero，已可读候选继续 |
| SRC-META-AI | Research失败；真实publication results2→3、global_search2/3及HyperAgentscanonical定点日字段，分页混旧年且缺March，TRIBEScience关闭有效，[实际范围/停止](../_sources/daily-20260326/SUP_META_RECOVERY_STOP_20261012.md) | 受阻 | 精确25 Research/publication slice隔离，非所有正文不可访问；不以search缓存或非日序夹窗授zero/完整性 |
| SRC-QWEN | 本轮实际Research官方chunk定位GET /api/v2/article/retrieval?type=qwen_ai&language=en-US，HTTP200/success/40完整id/title/extra.date和HTML meta双字段，Mar19→Mar30夹窗；[原字段](../_sources/daily-20260326/SUP_QWEN_FIELDS_20261012.json) | 已检查 | 只当前40返回，不认证删项；extra.date与旧HTML meta可不一致、均未见25，不以模板meta互代真实首发 |
| SRC-DEEPSEEK | 本轮News16完整title/date与Research Index当前SSR10dated行，Feb25→Jun24、2025Dec1→Apr24夹窗，[实际范围](../_sources/daily-20260326/SUP_DAILY_DIRECTORY_FIELDS_20261012.md) | 已检查 | 只认证当前10Research/16News有限切片，不冒本轮读旧31或删除历史 |
| SRC-MOONSHOT | 本轮Research19独立dated卡Feb9→Apr20；清单exact .com平台changelog全22 event headings至末均2025/24，pagePosted非event；[原字段/stop](../_sources/daily-20260326/SUP_KIMI_ZAI_RELEASE_FIELDS_20261012.md) | 已检查 | 仅当前两指定入口，平台26无date链接不补造；英文旧域重定向切片不同，不授已删除历史/无遗漏 |
| SRC-TENCENT-HUNYUAN | 本轮官方Research bundle恢复publicList，renderType0/page1/size20实际11/totalNum11、page2为空停止；Feb3/13→Apr23及以后全部title与display/published两原字段完整对读，[原字段/调用](../_sources/daily-20260326/SUP_HUNYUAN_FIELDS_20261012.md) | 已检查 | 仅当前公开11项，无25日新增；display与publishedAt不互代首次公开，不认证已删除历史 |
| SRC-ZAI | 本轮Research15 dated卡Mar15→Apr1；清单exact release完整当前8 title/date/core Feb12→Apr7，无next停止，[原字段](../_sources/daily-20260326/SUP_KIMI_ZAI_RELEASE_FIELDS_20261012.md) | 已检查 | 不继旧16条计数；Research/release分日不互代首发，不授删除历史/全机构零 |
| SRC-BYTEDANCE-SEED | 原UI type1/US/year2026/token20实际20/82，token40实际18/82 Apr7→Feb27后停止；type2/US/count20实际14/19、next空false/token20空，14日期均窗外；两具名paper完整v1/25门独核，[字段/停止](../_sources/daily-20260326/SUP_SEED_CURRENT_FIELDS_20261012.md) | 受阻 | 五未返身份/日期与公开筛选语义隔离；12/23是不同locale/count响应不互代，目录25Topo不代原文首公开 |
| SRC-BAIDU-ERNIE | 本轮Blog第一页10 dated卡原span/UI日序，Apr15→Feb6/Jan29夹窗，停止当前页 | 已检查 | 当前有限切片未见25，不认证删除历史/全站 |
| SRC-XIAOMI-MIMO | 首页Paper8 dated June29→Mar13→Feb3；当前15具名Blog以6metadata与9真实iframe日/月字段恢复，有限字段独核，[原字段/停止](../_sources/daily-20260326/SUP_MIMO_CURRENT_FIELDS_20261012.md) | 已检查 | 15当前返回均窗外；April2026不补日，同Flash不重家族，不认证删除历史/全机构zero或15全文已审 |
| SRC-MINIMAX | 本轮EN12/CN13dated卡Mar18→Apr27/May26夹窗；AgentTech当前.md全读为Sep19/Sep22/Oct8三项，纠正旧882B/May13不继承 | 已检查 | 仅当前可见目录，[字段/边界](../_sources/daily-20260326/SUP_DAILY_DIRECTORY_FIELDS_20261012.md)，无线索不扩历史档案 |
| SRC-ARXIV | 本轮四主题Submitted03-23T01Z～25T01Z只作发现，start0/max25系统9/9、learning25/111、多模态25/34、Agent25/163；learning/Agent各start25/max25后停止，共134槽/122身份；月相关标题只22500–23502有限查漏，[原参数/准入停止](../_sources/daily-20260326/SUP_FINAL_SOURCE_SCOPE_20261012.md) | 受阻 | NumberGeometry/StateLin及旧StepCache/Lightning首公开日范围跨窗隔离；LG0/2000未返/CV0/2000超时/其它截断标题不授全分类召回，未返页不转逐项队列 |

上述目录只复用身份与原字段，窗口归属和贡献另判。必要 artifact 为表外：[dataset](https://github.com/openai/model_spec_dataset)、[harness](https://github.com/openai/model_spec_evals)，只读取拟采用命题需要的 README，不扫描所有 GitHub release。本轮有限来源与准入停止见[当前范围](../_sources/daily-20260326/SUP_FINAL_SOURCE_SCOPE_20261012.md)和[本日最新停点](../_sources/daily-20260326/SUP_WORKING_STOP_20261012.md)；旧停点仅作历史原窗记录。

本轮补充发现：[四窄主题query](../_sources/daily-20260326/SUP_TOPIC_DISCOVERY_20261012.json)限定 Submitted03-23T01Z～03-25T01Z 作发现，start0/max25；系统9/9、学习25/111、多模态25/34、Agent评价25/163。[学习/Agent第二页](../_sources/daily-20260326/SUP_TOPIC_PAGE2_20261012.json)各start25/max25后停止，未返页不当全文待办。原API可能返回后来版本，相关项另读完整精确v1题摘。官方月列表仅在相邻22500–23502 ID段浏览相关标题作新命名查漏；LG0/2000切片未返回、CV0/2000一次12s超时，其它截断页只读实际相关标题，ID不是日期证明，也不授全分类召回。14源有限停止层已经独核，GoogleResearch/Meta/Seed精确缺口仍隔离，不授其正面Coverage或历史zero；旧表完成标签不代替本轮六部分验收。

新候选采用日级夹逼：实际读[arXiv官方公开流程](https://info.arxiv.org/help/availability.html)规定的最早公告日下界，再以同ID/arXiv provider/DOI的findable登记日上界确认；二者同03-25BJT才落本窗。Submitted、v1Updated、registered单字段均不是公告，QA可延迟，不补造时刻。[首6题摘/日期](../_sources/daily-20260326/SUP_FIRST_EXACT_ABSTRACT_DATE_20261012.json)与[provider原值](../_sources/daily-20260326/SUP_FIRST_PROVIDER_FIELDS_20261012.jsonl)已独核。

## 3. 候选与判断

三维为 Design Delta、System Reach、Durability，各0～3。只给确定落窗且通过贡献筛选的家族评分；主文、suite与代码为同一发布家族，不重复计数。5～6分项遇实际Books缺口/纠错/设计反证时，已定点深入足以支持该命题和直接反侧，不改原分、不无差别遍历附件；细节见§4与独立记录。

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [Model Spec 发布及 Evals](https://openai.com/index/our-approach-to-the-model-spec) | 2026-03-25T18:00:00+08:00 | 从条款可追溯推进到条款—场景—local rubric的测量校验，分开rubric、grader与人工标签故障，并明确角色skip和相关评分边界；2 + 2 + 3 = 7 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM，[Ch66“长篇Policy要先编译成Versioned Atomic Tenets”](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)既有论证内两段 |
| [SortedRL exact-v1](https://arxiv.org/abs/2603.23414v1) | 2026-03-25 | 将长尾harvest、有限prompt pool与discard/restart或逐段真实behavior-prob恢复分开，改变rollout/update batch耦合选择；2 + 2 + 3 = 7 | 深入完成 | 整合：TRAIN-GRPO，[Ch33 Partial Rollout](../../../../books/part-04-training-system/33-grpo.md)，实际两段与自身来源注非writer POST通过 |
| [PCR exact-v1](https://arxiv.org/abs/2603.23049v1) | 2026-03-25 | prefix-tree前视replacement、层级重叠和queue SSD预取联动，使复用命中与搬运critical path共同设计；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖：INFER-KV-CACHE，[Ch45“从反应式Recall到预测式Prefetch”](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)实际waiting-prefix→tree/tiers→layer overlap→identity/fallback正文 |
| [CPU-Induced Slowdowns exact-v1](https://arxiv.org/abs/2603.22774v1) | 2026-03-25 | CPU供给不足可经tokenization、kernel launch、collective/IPC造成GPU idle，process separation/graphs不免host容量合同；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖：INFER-SCHEDULING，[Ch56 Host Control Plane容量合同](../../../../books/part-05-inference-system/56-inference-scheduling.md)实际affinity/launch/tokenization/shared-memory/progress预算与溯源正文 |
| [TRAP exact-v1](https://arxiv.org/abs/2603.23117v1) | 2026-03-25 | 低信任物理观察可改变自生成CoT并影响动作，可信指令/传输不授闭环忠实性；2 + 2 + 3 = 7 | 深入完成 | 整合：MULTIMODAL-EMBODIED-VLA，[Ch26 Safety envelope](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)，实际两段/自身注nonwriter POST通过 |
| [Persistent Structural Memory exact-v1](https://arxiv.org/abs/2603.22858v1) | 2026-03-25 | 稳定外坐标与routing-bias/learning-rate先验迁移分别测试，使坐标稳定性不等于迁移有效；2 + 1 + 3 = 6 | 争议 | 暂缓：MODEL-LONG-CONTEXT，[Ch22](../../../../books/part-02-model/22-long-context.md)，mapping公式/表差值与统计协议冲突，见§4/5 |
| [CMM exact-v1](https://arxiv.org/abs/2603.22871v1) | 2026-03-25 | contraction/连续latent dynamics与防塌缩作为recursive推理替代分支，须分开稳定平衡与推理正确；2 + 1 + 3 = 6 | 争议 | 暂缓：MODEL-TRANSFORMER-LAYER，[Ch17](../../../../books/part-02-model/17-transformer-layer.md)，必要稳定条件不推出收缩保证，见§4/5 |
| [VISOR exact-v1](https://arxiv.org/abs/2603.23495v1) | 2026-03-25 | 保存完整visual bank而独立分配读取/改写层及多budget子图router，压缩输入与减少交互不是同接口；2 + 2 + 3 = 7 | 深入完成 | 整合：MULTIMODAL-REPRESENTATION，[Ch23 Fusion](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)，实际两段/自身注nonwriter POST通过 |
| [TRACE spatial exact-v1](https://arxiv.org/abs/2603.23404v1) | 2026-03-25 | singlepass从egovideo自生房间坐标camera/entity文本协议并保原视频问答，估计schema非真实pose；2 + 1 + 3 = 6 | 深入完成 | 整合：MULTIMODAL-REPRESENTATION，[Ch23几何问答](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)，实际两段/自身注nonwriter POST通过 |
| [ARGENT exact-v1](https://arxiv.org/abs/2603.23311v1) | 2026-03-25 | cone aperture域/clipping可使方向目标失效，改angle/intra减权/norm分责并审评价人口；2 + 1 + 3 = 6 | 深入完成 | 整合：MULTIMODAL-REPRESENTATION，[Ch23对齐](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)，实际两段/自身注nonwriter POST通过 |
| [ReVal exact-v1](https://arxiv.org/abs/2603.23355v1) | 2026-03-25 | 独立logitQ/V trajectory residual与FIFO再求值更新，使一次性policy-only更新成为可比较替代；2 + 2 + 3 = 7 | 深入完成 | 整合：TRAIN-PPO，[Ch32](../../../../books/part-04-training-system/32-ppo.md) |
| [Sparser Faster Lighter exact-v1](https://arxiv.org/abs/2603.23198v1) | 2026-03-25 | sparse packing/CUDA能否兑现L1形成的不规则稀疏，零化参数与执行节费分开；2 + 2 + 3 = 7 | 深入完成 | 整合：INFER-TENSORRT-LLM，[Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md) |
| [WildWorld exact-v1](https://arxiv.org/abs/2603.23497v1) | 2026-03-25 | 帧同步action/state/skeleton/camera/depth与actionfollowing/statealignment分测，使pixel质量不能代动作状态合同；2 + 2 + 3 = 7 | 深入完成 | 整合：MULTIMODAL-WORLD-MODELS，[Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) |
| [Foveated Diffusion exact-v1](https://arxiv.org/abs/2603.23491v1) | 2026-03-25 | gaze条件mixed-resolution token训练/采样使生成空间预算按观察者条件分配；2 + 2 + 3 = 7 | 深入完成 | 整合：MULTIMODAL-GENERATIVE-PARADIGMS，[Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)，16968后/06351前两段及本人静态注 |
| [VTAM exact-v1](https://arxiv.org/abs/2603.23481v1) | 2026-03-25 | future visuo-tactile共同表示接joint deformationproxy训练/动作接口，代理与真实力分验；2 + 2 + 3 = 7 | 深入完成 | 整合：MULTIMODAL-EMBODIED-VLA，[Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) |
| [RealMaster exact-v1](https://arxiv.org/abs/2603.23462v1) | 2026-03-25 | geometry anchor propagation生成pairedvideo后蒸馏无anchor部署，制备/交付条件分责；2 + 1 + 3 = 6 | 深入完成 | 整合：MULTIMODAL-GENERATIVE-PARADIGMS，[Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [I3DM exact-v1](https://arxiv.org/abs/2603.23413v1) | 2026-03-25 | viewfeature评分/implicitwarp/可靠区域注入把memory匹配与targetview对齐分开；2 + 2 + 3 = 7 | 深入完成 | 整合：MULTIMODAL-WORLD-MODELS，[Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)，MemLearner末后/Controlflow前两段及本人静态注 |
| [ABot-PhysWorld exact-v1](https://arxiv.org/abs/2603.23376v1) | 2026-03-25 | decoupledDPO discriminator/actioncontextblock与物理/动作分测，不让likelihood质量代物理正确；2 + 2 + 3 = 7 | 深入完成 | 整合：MULTIMODAL-WORLD-MODELS，[Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) |
| [ViBe exact-v1](https://arxiv.org/abs/2603.23326v1) | 2026-03-25 | RelayLoRA两stage分别跨模态/分辨率，部署丢第一stage使训练适配与交付组合分开；2 + 1 + 3 = 6 | 深入完成 | 整合：MULTIMODAL-GENERATIVE-PARADIGMS，[Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [Gaze-Regularized VLA exact-v1](https://arxiv.org/abs/2603.23202v1) | 2026-03-25 | aggregated gaze KL作为训练attention prior，非部署实时eye tracking或解释真值；2 + 1 + 3 = 6 | 深入完成 | 整合：MULTIMODAL-EMBODIED-VLA，[Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)，12193完整末段后/虚拟视角前两段及本人注 |
| [InterDyad exact-v1](https://arxiv.org/abs/2603.23132v1) | 2026-03-25 | MetaQuery将conversation条件转可查询motionprior，反应时机与render/lips分责；2 + 1 + 2 = 5 | 深入完成 | 整合：MULTIMODAL-GENERATIVE-PARADIGMS，[Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)，18600完整段后/velocityEMA前实际两段/本人注 |
| [GO-Renderer exact-v1](https://arxiv.org/abs/2603.23246v1) | 2026-03-25 | objectlocal xyz在ref/target成对条件注入，reference负时间与targettimeline分离；2 + 1 + 3 = 6 | 深入完成 | 整合：MULTIMODAL-GENERATIVE-PARADIGMS，[Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)，实际两段/自身注nonwriter POST通过 |
| [SafeSeek exact-v1](https://arxiv.org/abs/2603.23268v1) | 2026-03-25 | 可微binarymask跨粒度归因安全电路并限定部件更新，孤立neuron/稀疏率不能代功能完整性；2 + 2 + 3 = 7 | 深入完成 | 整合：PLATFORM-SECURITY，[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [Activation Watermarking exact-v1](https://arxiv.org/abs/2603.23171v1) | 2026-03-25 | secret-key激活扰动改变adaptive攻击者信息条件，监测须绑定key/算法可见性与FPR；2 + 2 + 3 = 7 | 深入完成 | 整合：PLATFORM-SECURITY，[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)，只v1不继v3身份，key-boundary末后/message-account前实际两段与本人注通过 |
| [CCMA exact-v1](https://arxiv.org/abs/2603.23159v1) | 2026-03-25 | VLM teacher conformal uncertainty/diversity引导visionstudent acquisition，校准与选择条件分验；2 + 1 + 2 = 5 | 深入完成 | 整合：TRAIN-DATA，[Ch27](../../../../books/part-04-training-system/27-data.md) |
| [Brain Misalignment exact-v1](https://arxiv.org/abs/2603.23091v1) | 2026-03-25 | 保language模型目标而反向脑预测适配并匹配比较，干预对语言能力的作用需独立归因；2 + 1 + 3 = 6 | 深入完成 | 整合：WORLDVIEW-REPRESENTATION，[Ch5](../../../../books/part-01-worldview/05-what-neural-networks-learn.md)，直接表示/能力形成非脑域应用 |
| [Memory Augmented Routing exact-v1](https://arxiv.org/abs/2603.23013v1) | 2026-03-25 | memory可改变correctness却不改confidence路由，smallmodel知识访问与路由/费用须分账；2 + 1 + 2 = 5 | 标准完成 | 已有覆盖：AGENT-MEMORY，[Ch77](../../../../books/part-07-agent/77-memory.md)，受约束读取/router只执行计划及评分/写权限分离的具体正文；局部反证非memory普遍优于规模 |
| [EVA exact-v1](https://arxiv.org/abs/2603.22918v1) | 2026-03-25 | query-driven先计划后选观察，读取schedule/三stage训练支持与视频生成workflow分责；2 + 1 + 3 = 6 | 深入完成 | 整合：MULTIMODAL-REPRESENTATION，[Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) |
| [EchoKV exact-v1](https://arxiv.org/abs/2603.22910v1) | 2026-03-25 | 从部分KV网络补残差、标准/压缩模式切换使保存表示与decoder消费分开；2 + 2 + 3 = 7 | 深入完成 | 整合：INFER-KV-CACHE，[Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)，切回不自动等无损 |
| [VLGOR exact-v1](https://arxiv.org/abs/2603.22892v1) | 2026-03-25 | VLM预测futurestate/action且counterfactual prompts造imaginedrollouts，真实支持与预测数据policy影响分验；2 + 1 + 3 = 6 | 深入完成 | 整合：MULTIMODAL-WORLD-MODELS，[Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)，12063末后/Dreamer前实际两段与本人注通过 |
| [DDSR exact-v1](https://arxiv.org/abs/2603.22908v1) | 2026-03-25 | 全target entropy与人口阈值分配双teacher，再分别校验outputJS与gradientdiscrepancy监督；2 + 1 + 2 = 5 | 深入完成 | 整合：TRAIN-SFT，[Ch29](../../../../books/part-04-training-system/29-sft.md) |
| [Contextual invariance exact-v1](https://arxiv.org/abs/2603.23485v1) | 2026-03-25 | 等价任务微小无信息语境可改变bias测量，控制marginals后残余须分验；2 + 1 + 3 = 6 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)，TRACE末后/3DGS前两段及本人注 |
| [SpecEyes exact-v1](https://arxiv.org/abs/2603.23483v1) | 2026-03-25 | large初筛/small完整tool-free答案、answer-separability gate与parallel funnel使完整链提前终止条件可验；2 + 2 + 3 = 7 | 深入完成 | 整合：AGENT-WORKFLOW，[Ch81](../../../../books/part-07-agent/81-workflow.md)，原lossyroute末后/Clarification前两段及本人注 |
| [Test Evolution exact-v1](https://arxiv.org/abs/2603.23443v1) | 2026-03-25 | 语义改变/保持变体对照显現旧行为对齐与词面漂移，coverage不能批准修订；2 + 1 + 3 = 6 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)，SpecOps末后/VeriEnv前两段及本人注 |
| [MemCollab exact-v1](https://arxiv.org/abs/2603.23234v1) | 2026-03-25 | 同task异构trajectory对比抽constraints、按类别检索，使共享记忆与专属风格资格分开；2 + 2 + 3 = 7 | 深入完成 | 整合：AGENT-MEMORY，[Ch77](../../../../books/part-07-agent/77-memory.md)，07711末后/Query-local前实际两段与本人注通过 |
| [3DCity-LLM exact-v1](https://arxiv.org/abs/2603.23447v1) | 2026-03-25 | target/neighbor/global条件分路及任务granularity选择，人工target与scene置零构成具体表示替代；2 + 1 + 2 = 5 | 深入完成 | 整合：MULTIMODAL-REPRESENTATION，[Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)，OpenVoxel末后/partialbinding前实际两段与本人注通过 |
| [UniGRPO exact-v1](https://arxiv.org/abs/2603.23500v1) | 2026-03-25 | interleaved文本/图像共享单trajectory，去CFG分叉与velocityMSE改变rollout/regularization接口；2 + 2 + 3 = 7 | 深入完成 | 整合：MULTIMODAL-GENERATIVE-PARADIGMS，[Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)，生成后训练首段后/Expert前实际两段与本人注通过 |
| [SIMART exact-v1](https://arxiv.org/abs/2603.23386v1) | 2026-03-25 | sparse3DVQVAE把复杂part/kinematics共同表示容量与信息支持一起验，token减少不授可动真值；2 + 1 + 2 = 5 | 深入完成 | 整合：MULTIMODAL-REPRESENTATION，[Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)，16745末后/fragment前实际两段与本人注通过 |

## 4. 证据与知识整合

### [Model Spec 发布及 Evals](https://openai.com/index/our-approach-to-the-model-spec)

必要套件：[Model Spec Evals](https://alignment.openai.com/model-spec-evals/)。

官方 RSS 原值 `Wed, 25 Mar 2026 10:00:00 GMT` 是主文的公开时刻；主文“同时发布”所链接 suite，因此同一发布事件落窗，不把 Evals 的日期显示擅自补成另一个时刻。作者实际读主文、suite 的 dataset/grading/limitations，以及必要 dataset/harness README；没有复现实验或认证全部实现。

Dataset针对225条款建立596短文本场景，local rubric只说明该场景对应的部分规范。人工构造合规/不合规假想答案用来查rubric误译、grader误用和人工标签错误，而不是假定条款清楚就评分正确。Blog的配置为20 target samples和五次grader评分取中位数、6～7判合规；harness默认target/grader各一次，不能把默认运行称为Blog结果复现。Dataset README指向2025-12-18 Spec，公开API消息角色限制导致9例skip：要保留有效分母，不能把未运行义务当通过。

这是受限测量方法，不是校准概率或部署安全率。五次同grader采样不能消除共同rubric偏差；短文本、日常、非对抗场景不覆盖工具/多模态/真实Agent长交互。原结果没有重要性或生产流量加权，旧模型按新政策测还混入训练年代差异。没有采用速度/吞吐结论，hardware、precision、长度、batch、concurrency、SLO性能条件不适用；具体grader、场景及阈值仍必须随评价协议固定。

对照当前[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)的atomic-tenets段：原有多轮规范编译与finding追溯，但未在该链中展开“rubric本身先被人类正反例检验”和角色无法保真时的skip分母。实际将两段插在该机制之后、Annotator/Policy Identity之前；保留原规范编译、多轮对抗成本和旧静态rule适用条件。新段落交接为：条款可追溯 → 测量翻译正确性 → 重复评分的偏差边界 → annotator/policy身份。来源标记为 `SF-2026-OPENAI-MODEL-SPEC-EVALS-20260325`；Review notes只保存精确配置与限制，不承载机制正文。mar01已实际原core、owner/邻接写后PASS；最后新增role-skip句亦独立实际核验，不把作者自检当验收。

具名负侧：XR完整核心是源码模板/提示与既有API封装，60内部prompt/5次模拟器实验混合framework bug和不存在API，没有独立归因出新的执行/适用边界；Lyria3 Pro时长与结构控制发布未披露新内部机制或受控的质量/成本边界，旧SynthID/过滤器重述不另当机制增量。TRIBE是fMRI/临床预测研究，属暂缓Science而非本项目世界状态机制。CoDesign综述完整v1题摘归纳data movement、quantization、scheduling与层级角色，未提出可检验的新LLM设计边界；不是因为“综述”标签一律排除。上述只是具体关闭依据，不代表全部原始库存均已全文审阅。

### [SortedRL exact-v1](https://arxiv.org/abs/2603.23414v1)

实际必要§3/§4.1–4.4/Table1/Fig5–6支持有限prompt pool、只接纳当轮完整新轨迹时丢弃旧partial/restart，以及恢复时保存逐段真实behavior分母的接口；不把ratio可算当无偏、bubble ratio当MFU或rollout throughput当全训练省费。只oversubscribe、过大grouping与partial在LogicRL退化，GSM8K/AMC亦有反退；§4.3 AIME叙述与Table1结果身份排列冲突保留，不自行修复为普勝。Ch33原Partial已有persistent prefix/version/terminal，却缺上述两合同/anti-starvation差额；经独核和root窄锁已写两段与静态来源注，reader实际完整邻接/两段/本人注逐字POST通过，非DAY。具体[Source/两PRE](../_sources/daily-20260326/SUP_SORTEDRL_SOURCE_PRE_20261012.md)保存混合集群/算法/预算与采用边界，未复现。

### [PCR exact-v1](https://arxiv.org/abs/2603.23049v1)

§2.2/4/6/8支持prefix祖先依赖、leaf eviction、pending queue前视与SSD→DRAM预取，再以layer load/compute/offload重叠隐藏搬运；前提是每层传输可被计算覆盖。Only-Down在小KV优于Up-Down、arrival/window依赖和SSD读写口径差异保留，尾延迟叙述不授生产SLO。Ch45现正文的完整waiting-prefix→tree future-use→tier-prefetch→layer-overlap→identity/fallback已经承载拟采用联动，前host/decode与后timedcommit交接完整；本轮非作者必要源与实际邻接核验已有覆盖，不造重复diff。

### [CPU-Induced Slowdowns exact-v1](https://arxiv.org/abs/2603.22774v1)

§III–VI必要段的tokenizer/launch/collective与shared-memory轮询证据支持host供给影响GPU执行；加核只缓解相应瓶颈，慢reader同步结构不能由CPU数量简单消除。只采用v1所测物理core/SMT-off、4/8GPU与固定attacker/victim负载，不借v3agentic摘要或新版倍率、当前云价格。Ch56现正文的host-affinity/launch/tokenization/shared-memory/progress预算→隔离/准入→GPU提交→idle溯源与近文成本/旧GPU-first回退已经具体覆盖。本轮非作者实际必要源和完整邻接通过No Change。两项具体[Source/当前正文比较](../_sources/daily-20260326/SUP_PCR_CPU_SOURCE_NC_20261012.md)不继承缺失旧POST标签，未复现。

### [TRAP exact-v1](https://arxiv.org/abs/2603.23117v1)

实际§3–7/T1–6说明用户instruction不变时物理观察污染可影响自生成CoT与动作，但不同decoder对CoT/指令会竞争，CoT-only并非统一优于/劣于联合路径；真实15trial中13/15至少一步推理变化与5/15完成重定向目标必须分开。transfer/scene-related universal/长任务边界保留，Eq8歧义不采完整recipe，detector只是建议未驗证。非作者纠正Eq5抽取误读后，作者回读原MathML确认正常teacher-forcing；未把错误写入Books。Ch26现middleware直接改写内部计划的分支没有承载感知→自生成推理污染接口，已准备两段[Source/PRE](../_sources/daily-20260326/SUP_TRAP_SOURCE_PRE_20261012.md)经必要独核/root锁已写于12717后/abstention前，真实nonwriter POST通过，不把普通工作写成外部受阻。

### [VISOR exact-v1](https://arxiv.org/abs/2603.23495v1)

实际§3–6/Eq1–3/T1–4支持完整visual bank的CA读取与可选SA改写分责、多budget子图混合训练后router选择，不把tokens未删称所有信息/质量无损。CA-only细粒度不足、强packing反退、部分dense任务更好；离线label correctness/loss与配置搜索不是在线真值。Transformer FLOPs排encoder，原§6计时为可容纳所有方法的最大batch而非已知异batch，具体batch/请求负载未披露，不能授任意单请求/SLO/全费净加速。非作者纠错后Source/实际Ch23差额/两PRE通过；HIVE完整段之后/Shared标题之前经root批准已写两段与本人注，真实nonwriter完整邻接/注POST通过。[必要原证/精确PRE](../_sources/daily-20260326/SUP_VISOR_SOURCE_PRE_20261012.md)保存训练/路由/参数费用。

### [TRACE spatial exact-v1](https://arxiv.org/abs/2603.23404v1)

实际§3–4/T1–4的singlepass先生成房间参考、camera path与entity文本registry，再让答案仍见视频，改变的是自生空间描述消费接口而非可信tracker/BEV几何。米坐标/离散8向是估计，去trajectory有部分改善，静态schema可损agentstate；MCQ/MRA和单/双stage人口不合并或唯一因果。Ch23已有SGCoT训练track读出与Loc3R监督hidden不实际覆盖此接口，Source/具体差额/两PRE独核通过；拟SGCoT08436完整原段之后、下一17625离线重建段之前，不移动其间结构分组/VGG-T3原段。[必要证据/PRE](../_sources/daily-20260326/SUP_TRACE_SPATIAL_SOURCE_PRE_20261012.md)；经root批准实际两段与本人注已写，nonwriter真实完整邻接/注POST通过，全部制备/读取费用保留。

### [ARGENT exact-v1](https://arxiv.org/abs/2603.23311v1)

实际§3–7/Eq1–9/T1–3与必要训练预算支持cone aperture定义域/clipping→angle目标、intra/inter减权与norm分责。Small分类与scale/AP反侧、对全部pair减权退化均保留；PEP角度映射只是score，AUC/AP不授概率校准，模型清洗522/1000人口与移除相似negative提高检索不独证它们全部假负例。Ch23具体taxonomy/projector段缺此方向目标合同，必要Source/差额/两PRE独核通过；拟07474完整段后/Caption标题前，经root批准实际两段与本人注已写，nonwriter真实完整邻接/注POST通过。[原证/两PRE](../_sources/daily-20260326/SUP_ARGENT_SOURCE_PRE_20261012.md)含GRIT/CC3M、384M训练样本和全部制备/训练/评价费用，未复现。

### [GO-Renderer exact-v1](https://arxiv.org/abs/2603.23246v1)

贡献决定接口§3和必要§4–5/T1–2/F5–6独核通过：object-local xyz在reference/target各自与外观/noise成对条件注入，reference负RoPE把参照与target历史分开，构成可核接口增量，不因组合或渲染应用排除。负RoPE借前例，g3仅局部；错proxy直接失败，多reference/额外训练混杂，CLIP/DINO非物理真值，T2未列声称的PSNR/SSIM不补造。原6分/候选保留，actualCh24具体差额/PRE独核与root批准后，仅18524末后/生成后训练前两段和本人注已写，nonwriter POST通过；[必要Source](../_sources/daily-20260326/SUP_GORENDERER_ADMISSION_SOURCE_20261012.md)不授strict consistency、materials解耦或实时费用保证。

### [Persistent Structural Memory exact-v1](https://arxiv.org/abs/2603.22858v1)

实际§3/7–10/12/Eq13/T3/5/6，并因中心冲突定点读同v1 PDF §4.3–4.4/9/12/T5–6，支持稳定外坐标、权重重置后保留先验的局部设计，但未能确认宣称的结构迁移机制。Eq13线性差值与紧接ratio例示不是同一mapping；T6两组可直接相减的差值分别为.002/.007，不是所列.013/.000；摘要17seed显著与正文/PDF 7seed无显著也未恢复成同一统计协议。p>0.05不能证明普适无迁移，平均非负亦不能证明never reduces。原6分贡献候选保留，非报告作者必要原式/表/协议与实际Ch22独核通过安全暂缓，不以成熟“身份需稳定”原则替代本文新命题或制造Books成果。[证据与重开位置](../_sources/daily-20260326/SUP_DPPN_SOURCE_HOLD_20261012.md)保留冲突双方；未复现，不采用迁移有效或普适不可能的正面保证。

### [CMM exact-v1](https://arxiv.org/abs/2603.22871v1)

实际§3.1–3.6/Eq20–34、§4.1–4.4/T1–11与§5表明连续latent动力学是值得核验的recursive替代分支，但只检查第一必要Hurwitz条件不保证稳定，更不保证全局收缩/唯一且正确的平衡；diag(1,-2)具有负trace却有不稳定方向。原MathML/TeX核验Eq23线性化与Eq24 J=F′−I后的Eq29/31再次扣I问题并非抽取丢符号。受限Sudoku/Maze对照还混有loss、batch/accum、lr/noise和预算变化，部分配置反退，64步累积不证明少计算，FMA归因仍推测。原6分候选保留，非作者必要证明/训练反侧与actualCh17独核通过中心HOLD；不让benchmark进步补上稳定保证的逻辑桥，也不以泛泛“需验稳定”造正文差额。[原证/反例和重开条件](../_sources/daily-20260326/SUP_CMM_SOURCE_HOLD_20261012.md)，未核代码/复现；不写Books或授部署保证。

### [ReVal exact-v1](https://arxiv.org/abs/2603.23355v1)

必要§4–5/Eq2–3/Alg1/T1/F3–9及A/C/D/E支持logitQ/V的独立trajectory residual与FIFO重新求值更新合同，未闭合的两种rewardshaping/Bellman桥和Eq4漏value梯度不被采用。完全同参数零reward时初始residual为零，不证明π相同即Q相同、唯一optimal或value校准。Reference reset改变锚点、negative reward/β及fresh+replay预算共同影响学习；任务反退、GPQA叙述/表值与6.3/7.5h算术冲突保留，4.3x singleprompt steps非全训练净加速。原[Source/两PRE](../_sources/daily-20260326/SUP_REVAL_SOURCE_PRE_20261012.md)经独核/root批准已落实Ch32 VRER末后/朴素surrogate前及自身静态注，作者完整邻接回读，真实nonwriter POST通过，未复现。

### [Sparser Faster Lighter exact-v1](https://arxiv.org/abs/2603.23198v1)

实际§2.2–4.3/Eq1–4/Alg1–3/T1/§6与必要A.1文字/B.1–2.1支持gate GEMM epilogue按tile packing、gate模式融合up/down与训练hybrid/transpose分责。B2.1超量先discard/nextsync flag，仅允许系统扩容量/retry，实际恢复闭环未披露，不能授已验证rollback或静默提交安全。T1小模型训练慢、2B显存+22.3%/microbatch变化与质量反退，8H100PCIe/BF16/2048seq固定操作点保留；从头训练activation稀疏非任意densecheckpoint资格，forward input-token/ms不授decodeSLO。必要[Source/两PRE](../_sources/daily-20260326/SUP_SPARSEPACK_SOURCE_PRE_20261012.md)独核/root批准后仅Ch49 PolyCIM完整末段后/Persistent标题前两段与自身注已写，作者回读通过，nonwriter POST通过，未核代码/复现。

### [InterDyad exact-v1](https://arxiv.org/abs/2603.23132v1)

必要§3–5/Eq1–7/T1–2支持逐声学帧query将音频/首帧/text语境映为motion prior，再将人物空间注入与发声者嘴部guidance分责；latent逐点误差/时间差分不是几何位置真值。保训练阶段顺序口径冲突、同encoder评价/固定0.5秒代理、身份反退与只双人/侧脸定性边界，不照录recipe或实时/严格解耦保证。actualCh24跨模态null之后没有这条训练桥，经reader必要Source/owner/PRE、root窄锁和真实nonwriter完整邻接/本人注POST，已实际两段整合并获root接纳释放；[必要证据与两PRE](../_sources/daily-20260326/SUP_INTERDYAD_SOURCE_PRE_20261012.md)，未核实现/复现。

### [CCMA exact-v1](https://arxiv.org/abs/2603.23159v1)

必要§3–4与A–H校准/协议/T2支持support-union上JS→studententropy→候选内diversity接口；E实际固定平均集合大小，不能授有限样本真实类coverage，rank4真实类/前三support是直接反例，shift/adaptive桥不采用。保teacher差异消失时退化、精心子池反慢、task反退/空并集处理未披露与全部编码/cluster/标注/重训费用。actualCh27在线selector之后的具体差额与原两PRE通过，root批准已实际窄写；真实nonwriter完整邻接/本人注与必要原证POST已通过，不以作者自检授日级DAY。[必要原证/PRE](../_sources/daily-20260326/SUP_CCMA_SOURCE_PRE_20261012.md)，未核实现/复现。

### [Memory Augmented Routing exact-v1](https://arxiv.org/abs/2603.23013v1)

必要III–VI/T1–V支持“路由健康不等QA正确”的局部反侧，logprob线性归一不是正确率校准；保持原5分不排除。LoCoMo仅一会话152QA/steady-state预装，LongMemEval500底库只100分层QA；warm probe截断上下文与memory-only不同，不授完全归因，temporal与hybrid部分任务反退。EffCost按总参数的估算不等MoE实际费用、美元投影不等实付，未授普遍memory胜规模或持续收敛。actualCh77受约束读取中router只executionplan/事实支持provenance、评分/写权限分离已具体承载该采用命题，经必要Source→完整邻接独核已有覆盖，不造正文/末注diff。[具体依据](../_sources/daily-20260326/SUP_MEMORYROUTE_SOURCE_NC_20261012.md)，未核实现/复现。

### [Brain Misalignment exact-v1](https://arxiv.org/abs/2603.23091v1)

必要§3–5/F2–6与A probe身份/B–C readout支持指定读出能力反向适配＋permuted控制的干预资格；保LM匹配p值口径与无显著差异冲突、不是equivalence检验、有限head非全信息删除或唯一因果、GPT2及task反侧。研究是直接LLM表示功能，不按脑数据Science应用排除，也不授脑对齐普适必要/安全。actualCh12明确只inputembedding接口，整模型contextualstate干预改由soleCh5表示功能链承载，原6分/日期保持。必要Source/owner修正/PRE与root批准后实际两段/本人注及nonwriter完整邻接POST通过；[具体原证/两PRE](../_sources/daily-20260326/SUP_BRAINMISALIGN_SOURCE_PRE_20261012.md)，未核实现/复现。

### [DDSR exact-v1](https://arxiv.org/abs/2603.22908v1)

必要III/IV/T1–V/F3–8及V限制支持全targetentropy/nt的同labelspace双teacher配权，少样本分支可降低更自信CLIP的份额，不是逐样本argmax或校准正确率。Eq9不同维参数梯度cos的共同坐标/共享身份与二阶责任未披露，prototype记号/零熵guard也未闭合，不采完整recipe。保nt大小与内容混杂、VisDA与BBC同avg和多task反退，全部teacher/额外forwardbackward/训练费用未由步数抹去。actualCh29蒸馏privacy前的具体差额经必要Source/PRE和root批准实际两段/本人注写入，nonwriter完整邻接/必要原证POST通过；[原证/两PRE](../_sources/daily-20260326/SUP_DDSR_SOURCE_PRE_20261012.md)，原5分、未核实现/复现。

### [Gaze-Regularized VLA exact-v1](https://arxiv.org/abs/2603.23202v1)

必要§3–5/T1–6及B/C/D/E/F直接反侧支持训练时合成gaze heatmap约束attention prior，部署退出gaze生成链而仍消费RGB/language/proprioception；不是在线eyetracker、attention解释真值或安全闭环。future-window/algorithm口径未闭合，same-v1 §4/T4称实际机器人测试而F782–783称未测，两者均保留但物理正面结果/完整recipe不采用。零热图uniform guard实际存在，不自造缺口；strongbias/earlytask/foveation反退、realhumangaze另variant与费用均保留。经必要独核/root窄锁，实际两段与本人静态注写于Ch26 12193完整末段后/虚拟视角前；reader真实完整邻接/本人注POST通过，root接纳释放。[必要原证与两PRE](../_sources/daily-20260326/SUP_GAZE_SOURCE_PRE_20261012.md)，未核代码/复现。

### [WildWorld exact-v1](https://arxiv.org/abs/2603.23497v1)

root独占准备，reader必要原§3–6/T1与actualCh25差额/PRE已实际独核：引擎action/state与renderer RGB同步记录不授全隐藏状态可见，2D骨架tracker先在GT上仅43.23%坐标准确，不能用它自动归一生成器状态正确率；future GT全条件渲染与初态递归预测分开。段级judge的人审agreement排约5%争议段，200手选片段、过滤/自动行为人口和费用保留，不授物理安全/通用长程。root按已通过两PRE窄写于Ch25前置readout测量校准完整段之后/evaluationcontract之前及静态注；reader真实nonwriter POST与root接纳释放通过。[必要Source/实际owner与PRE](../_sources/daily-20260326/SUP_WILDWORLD_SOURCE_PRE_20261012.md)，未核artifact/像素/复现。

### [RealMaster exact-v1](https://arxiv.org/abs/2603.23462v1)

实际§3–6/T1–2/F6–7文字支持首尾appearance锚+逐帧edge造pair，再以clean-reference adapter学习生成target、部署退出锚制备链却仍消费输入视频；§6实时streaming为future，不提升为已实现因果推理。ArcFace过滤/评价共享、8→16FPS重复帧、代理/偏好与motion继承限制保留，CARLA定性非受控transfer/精确保真。必要Source/actualCh24具体差额/PRE经reader/root通过后，实际仅12013完整段及marker之后/LatentReuse之前两段及本人静态注；真实nonwriter完整邻接/注POST通过并获root接纳释放。[必要证据与两PRE](../_sources/daily-20260326/SUP_REALMASTER_SOURCE_PRE_20261012.md)，未核代码/视频像素/复现。

### [ViBe exact-v1](https://arxiv.org/abs/2603.23326v1)

必要§3–4/Eq5–6/T1–2与suppVRAM支持训练在W0+ΔW1条件下优化ΔW2、交付改用原W0+ΔW2的artifact组合，而非功能解耦已证。适配仅图像不抹主干视频监督，仍coarse-to-fine，GCLFA/HFATO未闭合recipe不采用；指标反退、4Kwidth/未披露配置与全部费用保留。actualCh24 13448完整两段后/连续latent版本前两段及静态注经独核/root窄锁落地，真实nonwriter完整邻接/本人注POST与root接纳释放通过。[必要Source/两PRE](../_sources/daily-20260326/SUP_VIBE_SOURCE_PRE_20261012.md)，未核artifact/视频像素/复现。

### [EchoKV exact-v1](https://arxiv.org/abs/2603.22910v1)

实际§3–5/Eq1–7/T1–4、B/T5与C/T6支持group首层global+本层localfeature按token预测缺失KV，再由KV-MSE到attention-output MSE训练；preRoPE/partialfeature单位与固定模型身份绑定，不等basiscodec或直接跨层读取。切回标准算子不自动恢复已丢历史，保原/重算是项目状态合同推断而非论文已实现的无损恢复；ratio反退/T4人口不闭和全费用隔离。actualCh45 randomdepth完整末后/两basis分支前原两PRE+静态注落地，reader真实POST/root接纳释放通过。[必要Source/PRE](../_sources/daily-20260326/SUP_ECHOKV_SOURCE_PRE_20261012.md)，未核kernel/复现或授SLO。

### [EVA exact-v1](https://arxiv.org/abs/2603.22918v1)

实际§3–5/T1–3/6.1–6.6支持query-only初态与time×density×resize联合取得视觉，uniformdense仍可选，计划/同baseCSV/ROUGE/反思均不认证充分grounding。stage/数据/预算混杂、文表身份冲突、650等效帧非真实人口、noisyquery与工具round全费用保留，不由少tokens授wallclock加速。actualCh23主动读取首完整段之后/DAVE标签前两PRE与本人注经独核/root授权落地；真实nonwriter完整邻接/本人注POST/root接纳释放通过。[必要Source/PRE](../_sources/daily-20260326/SUP_EVA_SOURCE_PRE_20261012.md)，未核code/逐图/复现。

### [I3DM exact-v1](https://arxiv.org/abs/2603.23413v1)

root独占准备必要§3–4/Eq5–7/T1–2与S1/S3–5，reader实际原证/owner/PRE独核：每candidate与lastframe锚/targetrays产生空间误差代理，patchwise互补选择与另一支对齐消费分责；负分/零canvas不授可见概率或全局最优，冻结VAE仍有输入梯度。静态reversal/Pi3代理非真实动态，视觉指标反退、generatedbank漂移与线性费用保留。root实际两段/本人注仅写于Ch25 MemLearner末后/Controlflow前，reader真实完整邻接POST/root接纳释放；[必要Source/PRE](../_sources/daily-20260326/SUP_I3DM_SOURCE_PRE_20261012.md)，未核artifact/全部图像/复现。

### [Foveated Diffusion exact-v1](https://arxiv.org/abs/2603.23491v1)

必要§3.2/Eq5–10/§4–5/T1–2与A/B/T3/E支持给定mask的同图HR/LR双VAE目标、整条短mixedlayout采样及splitdecode/blend；仅RoPE不兼容，codec边界/周边损失不被少tokens消除。pseudo-gaze不是eyetracker，自报偏好p>.05非等价，random/saliency/box支持不可任意互换，真实eye-trackedstreaming为future；模型命名与未披露计时/全部费用近文保留。actualCh24 16968完整末后/06351原段前两PRE及本人注经独核/root授权实际写，真实nonwriter完整邻接POST/root接纳释放。[必要原证/PRE](../_sources/daily-20260326/SUP_FOVEATED_SOURCE_PRE_20261012.md)，未核code/全部示例/复现。

### [VTAM exact-v1](https://arxiv.org/abs/2603.23481v1)

必要§3–5/Eq1–10/T1–2与A/B/C315支持future visuo-tactile共同表示训练及动作头joint deformationproxy目标，proxy非标定力；StageII frozenbackbone与gradient宣传/动作schema不闭合隔离。小量/连续trial、不同基线训练、定性预测与30Hz执行≠1Hzpolicy完整deadline保持，制备训练推理全费不省略。独核/root窄锁后实际Ch26 Contact旧第三完整段后/ExpForce前两PRE和本人注，真实nonwriter完整邻接POST/root接纳释放；[必要Source/PRE](../_sources/daily-20260326/SUP_VTAM_SOURCE_PRE_20261012.md)，未核code/全部图/复现。

### [ABot-PhysWorld exact-v1](https://arxiv.org/abs/2603.23376v1)

必要§2–6/Eq1–2/T1–3支持calibrated pose/gripper的2D多channel actionmap条件及proposer/scorer分开的有限偏好接口，不以借用DPO/VACE当新数学。VLM问题/判断的共同偏差、zeroInit非功能保持、视觉反退/样本划分未披露/固定view无closedloop与N候选/参考/制备训练费近文保留。独核/root窄锁后仅Ch25 crossEmbodiment完整段后/URDF前两PRE和注实际落地，真实nonwriter完整邻接POST/root接纳释放；[必要原证/PRE](../_sources/daily-20260326/SUP_ABOT_SOURCE_PRE_20261012.md)，不授严格physics/OOD/零费或实机安全，未核code/全部图视频/复现。

### [SafeSeek exact-v1](https://arxiv.org/abs/2603.23268v1)

必要§3–5/Eq1–15/T1–2与A/D支持按unit身份学习binarymask、保留/移除双验证及限定参数修复分责；dual mask非精确互补，完备/正交和helper冻结recipe不采用。已知trigger权限、非零ASR/效用反退、初始化/人口口径不闭和全费保留，不授未知adaptive或部署安全。独核/root窄锁后Ch72 Benign第二完整末段后/DecodingConstraint前两PRE与注实际写，真实nonwriter完整邻接POST/root接纳释放；[必要原证/PRE](../_sources/daily-20260326/SUP_SAFESEEK_SOURCE_PRE_20261012.md)，未核code/全部图/实施攻击或复现。

### [Activation Watermarking exact-v1](https://arxiv.org/abs/2603.23171v1)

必要§3–6/Alg1/T1–5与B/C/D支持secret-bound activation detector、answer聚合与payload身份分责；perentity阈值不认证多entity家族FPR，输出检测不等stream阻断或payload精确恢复，unlimitedadaptive安全无证明。训练改key需模型/阈值重适配；部分任务/效用反退、T1/T3协议差及secretgame代理人口隔离，全部训练/生成/探测计费。独核后实际Ch72 key-boundary末后/message-account前两段+本人注，真实nonwriter POST获root接纳；[必要Source/PRE](../_sources/daily-20260326/SUP_ACTWM_SOURCE_PRE_20261012.md)，未核artifact/全部图/复现。

### [VLGOR exact-v1](https://arxiv.org/abs/2603.22892v1)

必要§3–5/Eq1–3/T1–2与A/B支持joint futureimage/action预测与受限prompt-edited离线policy数据消费接口，不采用RGB→simreward未披露转换或连续/离散schema统一recipe。真实与生成比例/制备人口不闭、有限三seed/几何proxy及额外监督费用保留，不授反事实正确、physics/净收益或安全。实际Ch25 12063后/Dreamer前两段与本人注经真实nonwriter POST/root接纳，保全部相邻旧块；[必要Source/PRE](../_sources/daily-20260326/SUP_VLGOR_SOURCE_PRE_20261012.md)，未核实现/全部图/复现。

### [3DCity-LLM exact-v1](https://arxiv.org/abs/2603.23447v1)

必要§3.2–4/Eq1–6、§5/T4–5/T8–12和§6支持target、relativepos邻域与global分别投影/concat，人工target与scene置零，不是自动物体grounding。名称、分割、坐标与judge代理资格及质量反退保持，平均task时间不等净SLO，制备/编码/训练全计费。实际Ch23 OpenVoxel末后/partialbinding前两段与本人注真实POST/root接纳；[必要Source/PRE](../_sources/daily-20260326/SUP_CITY_SOURCE_PRE_20261012.md)，不授空间/隐私/规划真值，未核全部任务表/实现/复现。

### [UniGRPO exact-v1](https://arxiv.org/abs/2603.23500v1)

必要§3–6/Eq1–8/T1/B及F3–5文字支持单轮text-prefix→image条件的terminalcredit和velocity正则目标分责；训练去CFG而评价恢复CFG，未认证完整轨迹/终态分布等价。借用RatioNorm不是trueimportance，terminalreward非推理正确，SFT/分辨率/中止预算与共享评价偏差、反退/所有候选参考奖励和解码费用保留。实际Ch24生成后训练首段后/Expert前两段及本人注真实POST/root接纳；[必要Source/PRE](../_sources/daily-20260326/SUP_UNIGRPO_SOURCE_PRE_20261012.md)，不授多轮/无损/hacking消除/完整recipe，未核全部图点值/code/复现。

### [SIMART exact-v1](https://arxiv.org/abs/2603.23386v1)

HTML404后实际同v1 PDF必要§3–6/T1–3与B/T4/C/D/T6支持zero/default、occupied显式地址重建和part几何—符号metadata共同身份。B选定8³/4096与Table5系统prompt16×8×8/8192身份未闭，不采统一配置recipe；16³→8³聚合桥确有，不误记此处矛盾。输出token人口、36人工资产、异输入基线、网格fidelity/meshgraph分割及属性非物理真值和全费保留。实际Ch23 16745后/fragment前两PRE与本人注真实POST/root接纳；[必要Source/PRE](../_sources/daily-20260326/SUP_SIMART_SOURCE_PRE_20261012.md)，不授通用OOM消除/无损或真实控制，未核全部PDF视觉/视频/code/复现。

### [MemCollab exact-v1](https://arxiv.org/abs/2603.23234v1)

必要§3–5/Eq1–8/Alg1–2/T1–3/A/C/D/G支持同task跨模型轨迹差异→trigger/enforce/avoid候选构造与分类后读取。Weak-only配对未双标签验证，MATH1000+500与总500划分及Llama正文/table身份未闭；softguidance非无偏或指数剪枝证明，平均turn不是净费，反退/单seed与全制备成本保留。实际Ch77 07711后/Query-local前两段+本人注真实POST/root接纳；[必要Source/PRE](../_sources/daily-20260326/SUP_MEMCOLLAB_SOURCE_PRE_20261012.md)，不授通用迁移或事实权限，未核实现/全部轨迹图/复现。

### [Contextual invariance exact-v1](https://arxiv.org/abs/2603.23485v1)

必要Results/Methods/Discussion/F1–4文字/T1/Eq1–2支持固定target下非targetcue/null/order条件分布诊断。原joint由marginal乘积定义时ΔC≤0，与19–52%不可约比例不闭，强CbD/因果解释隔离，不影响独立诊断接口。Binary无偏norm、valid过滤/279角色人口、量化不同/有限复测和全费用保留，不授单prompt真值或通用公平安全。实际Ch66 TRACE第二段后/3DGS前两段+本人注经真实nonwriter POST/root接纳；[必要Source/PRE](../_sources/daily-20260326/SUP_CBD_SOURCE_PRE_20261012.md)，未核全部补图/代码/复现。

### [SpecEyes exact-v1](https://arxiv.org/abs/2603.23483v1)

必要§3–5/Eq1–16/T1/F3–6文字支持large初筛→small完整tool-free回答→min-token受限gate/residual预算，现Ch81基本lossyroute已有覆盖，只补独立校准/复杂度成本差额。Margin非正确概率，holdout/最佳point未闭，singlequery依赖非跨query串行；ThymeHR8K反慢/mean质量退和全部前端、拒绝后重复成本保留。已按root窄锁实际旧route完整段后/Clarification marker前两PRE+注，真实nonwriter POST/root实际接纳通过；[必要Source/PRE](../_sources/daily-20260326/SUP_SPECEYES_SOURCE_PRE_20261012.md)，不授exactspeculation/通用吞吐界/无损或行动安全，未核全部曲线/代码/复现。

### [Test Evolution exact-v1](https://arxiv.org/abs/2603.23443v1)

设计反证必要§3–7/T1–2/F4–9文字支持new-failing tests回旧版+changedregion的条件归因及生成测试oracle分责。成功baseline人口非完整理解，SPC有限旧tests不能证全等价；>99%为失败测试分母，coverage-match≠assertion相同，fresh再生成非维护，文数字/模型身份冲突与所有失败制备尝试全费保留，不推memorization内因果。已按root窄锁实际Ch66 SpecOps末后/VeriEnv前两PRE+本人注，真实nonwriter POST/root实际接纳通过；[必要Source/PRE](../_sources/daily-20260326/SUP_TESTEVOLUTION_SOURCE_PRE_20261012.md)，不授全bugfinding或任意软件变更安全，未核全部程序/实现/复现。

## 5. 缺口与下一步

本轮扫描、准入、逐项必要审阅及Books均已处理到安全终态；没有未读材料、待写Books或未完成单篇POST。普通扫描、筛选、必要审阅、Books与独立复核待办0；下面的必要日期、来源及中心争议为隔离的本窗终态保留项，不用于正面Evidence、Books或无遗漏/性能/安全保证。材料以后到达只定点重开。

本补充窗口中心争议终态保留项：DPPN22858v1需要恢复Eq13与例示mapping一致的可执行定义、T6差值及17/7seed同实验身份/统计协议，才能重开结构迁移结论→Ch22；CMM22871v1需要正确线性化、J定义和充分稳定/收缩假设及训练保证，并分离loss/预算混杂，才能重开递归推理稳定保证→Ch17。作者与非作者已读必要中心原证和直接反侧；两项不当访问故障、不降分排除或改称已有覆盖，不用于正面迁移/安全/性能保证，不写Books。明确数学/协议勘误与可核新原证为可接受替代，不请求无关附件。

以下23项是原09→09窗口的终态保留记录，不默认全部属于03-25新增队列；只重开受本轮日期/贡献变化影响的身份。PCR和TRAP已通过本自然日夹逼并在§3处理，其原窗请求不被伪装成原候选搬移；其他潜力不支持正面Evidence/Books/Coverage保证。

以下保留原窗23身份的历史准入命题，不代表本补充窗口仍有23个材料请求；日期差额已收窄为19窗外、PCR/TRAP已处理、仅2日级缺口：

| 身份/精确版本 | 必须进一步判定的命题 |
| --- | --- |
| [2603.23640v1](https://arxiv.org/abs/2603.23640v1) | Edge持续热约束改变端侧serving边界 |
| [2603.24652v1](https://arxiv.org/abs/2603.24652v1) | pruning隐藏/logit稳定不等生成probability轨迹稳定 |
| [2603.24579v1](https://arxiv.org/abs/2603.24579v1) | MARCH孤立checker与多Agent纠错控制 |
| [2603.24533v1](https://arxiv.org/abs/2603.24533v1) | UIVoyager分叉轨迹监督与训练控制 |
| [2603.24517v1](https://arxiv.org/abs/2603.24517v1) | AVO变体内核与Agent训练调度 |
| [2603.24440v1](https://arxiv.org/abs/2603.24440v1) | CUA连续视频/运动学相对稀疏截图的信息损失 |
| [2603.24587v1](https://arxiv.org/abs/2603.24587v1) | DreamerAD shortcut latent及reward/GRPO路径 |
| [2603.24584v1](https://arxiv.org/abs/2603.24584v1) | TAG原观察与object-erased预测差值的steering |
| [2603.24581v1](https://arxiv.org/abs/2603.24581v1) | LatentWAM几何蒸馏压缩与动作动态 |
| [2603.24506v1](https://arxiv.org/abs/2603.24506v1) | PhyGenesis无效轨迹纠正与条件生成 |
| [2603.24458v1](https://arxiv.org/abs/2603.24458v1) | OmniWeaving交错跨模态对齐；新增机制相对组合的准入事实仍未定 |
| [2603.24329v1](https://arxiv.org/abs/2603.24329v1) | GameplayQA角色/时间/决策密度评价盲区 |
| [2603.24270v1](https://arxiv.org/abs/2603.24270v1) | ScrollScape全景时序先验与ScanPE/ScrollSR |
| [2603.24060v1](https://arxiv.org/abs/2603.24060v1) | v1 SOMA三组件是否产生新可靠性条件尚未定；不改用后版RoboHarness身份 |
| [2603.24558v1](https://arxiv.org/abs/2603.24558v1) | LensWalk自适应观察时间/密度是否构成新接口条件 |
| [2603.24586v1](https://arxiv.org/abs/2603.24586v1) | TRACE人类部分context与judge混杂 |
| [2603.24278v1](https://arxiv.org/abs/2603.24278v1) | TopoMesh监督/预测DMC同拓扑对应 |
| [2603.24570v1](https://arxiv.org/abs/2603.24570v1) | Anti-I2V双空间防御；不由摘要采用防护率 |
| [2603.23117v1](https://arxiv.org/abs/2603.23117v1) | TRAP从patch经CoT到VLA动作的安全反证 |
| [2603.25583v1](https://arxiv.org/abs/2603.25583v1) | RobotFlywheel factor-space collection/training；Seed日期与Submitted不一致 |
| [2603.23049v1](https://arxiv.org/abs/2603.23049v1) | PCR prefix-tree lookahead/层加载并发/SSD预取改变queue与reuse关系 |
| [2603.28795v1](https://arxiv.org/abs/2603.28795v1) | StepCache任务验证→局部patch/fallback；不能把局部可验证性外推所有任务 |
| [2604.03279v1](https://arxiv.org/abs/2604.03279v1) | Lightning TTS精度脆弱性与NoC/SRAM/LoFi联合设计；不由单成本数采用 |

原23身份的本次日级差额已实际独核：[legacy日期差额](../_sources/daily-20260326/SUP_LEGACY_DATE_DELTA_20261012.md)。19项由官方最早公开下界排除03-25（QA只可延迟），不再请求其精确首日/时刻；PCR/TRAP两项已在新增候选安全处理。仅StepCache28795/Lightning03279的提交下界至findable登记上界跨本日，不能由月份、ID或Updated补造公开日。这里不承接另日报队列，不以窗外题摘冒本日证据。

必要日级材料请求仅四身份：[StepCache28795v1](https://arxiv.org/abs/2603.28795v1)/[Lightning03279v1](https://arxiv.org/abs/2604.03279v1)、[NumberGeometry23577v1](https://arxiv.org/abs/2603.23577v1)/[StateLin23571v1](https://arxiv.org/abs/2603.23571v1)，恢复能确认首次公开日的官方announcement/公开批次或同稿作者最初公开日期，并使区间不跨03-25边界；不追时分秒、不重请求现有题摘/PDF。未确定落窗前不评分、不进候选或Books、不支持zero/Coverage。MetaKube贡献已具体排除，不再为无影响日期另请求；FairnessRec/ethicalprobe/visualICL真实最早26仅作窗外潜在线索。收到原字段只重开对应日期/准入，不重全月或承接其它日报。

来源限制：Google pubs/Research下一页本窗dated slice；Meta Research/publication本窗slice；Seed type2当前US14/19少5项的身份/日期或公开筛选语义；arXiv仍受影响的日级公开范围。MiMo15必要日/月字段已恢复并独核，不再请求同一dated材料；这些有限范围不认证删除历史。请求具体切片而非精确时分秒，不要求全机构全历史export，也不将有界主题未展开页转成永久逐项任务。

## 6. 复核

复核者：mar01（原报告非作者；旧有效检查保留）；supp_mar26_reader（本轮非报告作者）。

结论：通过

supp_mar26_reader作为非本轮报告作者完整六部分DAY实际验收通过，root已读回接纳；旧报告有效检查仅复用未变化层，不代替本轮验收。

mar01实际完整读六部分、唯一停点、四主题参数/返回数、RSS六行、20项exact身份/原日期与EXTRA四题摘/字段；对23保留项核日期和采用隔离，不称23项全文审计。具名分层实际核CoDesign完整v1题摘及SOMA/Omni/Lens准入消歧，Lyria265～294、TRIBE40～53、XR必要core；四负侧理由通过，不授84交叉返回全审或全学科召回。唯一ModelSpec的必要主文/suite/dataset/harness以及Ch66两段/role-skip句实际POST通过，本轮又读2838～2884邻接与4245源注，Blog20/5与harness默认1/1边界准确。完成态V3校验、本日报/来源/Ch66限定diff-check通过；格式检查不代替上述语义判断。旧有效证据完整保留，未stage、commit或push。

本轮实际独核记录：[SUP_INDEPENDENT_REVIEW_20261012.md](../_sources/daily-20260326/SUP_INDEPENDENT_REVIEW_20261012.md)。首批30与残余五新增、Seed两项共37新增完整v1题摘/日级门/准入通过；残余三EX及ReqFusion/Human可靠性/物理保证反侧实际定点核，代表性排除按来源/主题/理由分层校准，不授134槽/122身份全题摘或全学科召回。32项必要Source/具体Books差额/PRE/实际写入及真实nonwriter完整邻接与本人注POST均获root实际接纳；PCR/CPU/MemoryRoute三具体NC与DPPN/CMM中心HOLD安全处置通过。14到期来源与实际触发已有限停止（GoogleResearch/Meta/Seed及四日级必要材料隔离），普通单篇工作0；本文件完整六部分DAY已由非报告作者实际验收通过（独核§51）；未将格式检查冒语义验收。

本轮完成态V3字段/一致性校验通过；本日报和具名source/Books限定`git diff --check`通过，本地引用均存在。机器实际比较原ModelSpec整行、原窗口与连续原§4均不变；候选表38＝旧整合1＋新增整合32＋已有覆盖3＋中心争议2。此为结构/冻结检查，与非报告作者六部分DAY分别成立；未stage、commit或push。

本轮明确排除分层独校实际10个具名样本：Scope的CoDesign23668/HPC22542/GoCoMA16377/PhysSkin23194四项，Safety/Learning的UniDial23160/OPF23004两项，决定接口MetaKube23580一项，以及残余ReqFusion23482/SealedExam23292/HumanMultiAgent23271三项，分别覆盖归纳/一般HPC类比、领域融合或物理动画应用、成熟工具接口与局部负面应用、无新条件的RAG/门控组合、schema/测量协议/串行动作组合等理由。样本均实际题摘校准，MetaKube、ReqFusion和Human的可靠性/物理保证必要负侧定点独读；本批所有已具名纠错、安全、设计反证信号均处理，未以负面/小结果/已有章节或机构名称拒收。其余标题已明确范围外的条目未独读全部题摘或正文，未返页与122身份不称全审；若出现同理由错误只重开受影响集合，不授分层样本为全量验证。
