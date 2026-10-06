# 2025-10-22 有限初筛与必要反侧

作者 Cicero。本窗 `[2025-10-21T09:00:00+08:00,2025-10-22T09:00:00+08:00)`。原响应见 FETCH.json、RECOVERY_FETCH.json；保存原件不代表正文已读。未使用他日候选池或旧 Weekly。

## 查询与实际停止

arXiv 四组均 start=0/max_results=80/submittedDate descending，发现带为 UTC `[202510210000 TO 202510220059]`，仅作发现，不是首次公开证明。完整真实编码 query 在 FETCH.json：

- model_training：cs.CL/LG，标题 attention、MoE、mixture of experts、distillation、pretraining，或 reinforcement 且全文 language model；17项。
- agent：cs.AI/IR/MA，标题 agent/agentic/RAG/memory 且全文 language model/LLM；13项。
- multimodal：cs.CV/RO，标题 world model/VLA/diffusion/autoregressive；9项。未把医学影像等整体纳入。
- systems：cs.DC/AR/PL/OS/PF，全文 LLM/large language/GPU/transformer；11项。与前组2重复，48唯一家族完整当前题摘实读。

官方 CL 月页只作相关标题查漏：身份段2510.18000～20000，实际25标题止于2510.18434。六个聚焦题目（多语言水印、剪枝、难度标签、judge评分区间、视觉文本压缩、韩语事实评价）取完整题摘，见 supplement.xml，合计54唯一家族。没有把月页2000条、25个标题或全年目录转成全文队列。

辅助搜索两组、仅首屏停止：`("October 21, 2025" OR "2025-10-21") (site:openai.com/index OR site:anthropic.com/research OR site:deepmind.google OR site:ai.meta.com) (model OR training OR inference)`；`("2025-10-21" OR "2025年10月21日") (site:qwen.ai OR site:platform.kimi.com OR site:zhipuai.cn OR site:hunyuan.tencent.com OR site:seed.bytedance.com OR site:ernie.baidu.com OR site:mimo.xiaomi.com OR site:minimax.io) (模型 OR training OR agent)`。搜索结果的年份混杂，不作覆盖/日期证据。

## 具名关闭与潜力

54题摘中以下8项在贡献/范围层关闭，日期未核不追加日期请求：18424 MedVRAgent为医疗VQA中MCTS/PPO应用；18446 LAND为CT器官条件生成；18516为钙信号解码；21820 HAIN为生物医学推理（AI for Science暂缓）；18615为boosted trees向单树蒸馏，不建立本项目foundation链；18838 PCMS为等离子体模拟GPU耦合，不是模型训练/服务机制；19012 Spark多语言ETL性能不涉及LLM执行链；19850 Prompt Decorators为符号指令词汇、scope与middleware，§4.3仅场景分析，未给出改变行为可靠性判断的可核实验或强制语义，不能借deterministic标题准入。最后一项必要风险core已读，不按论文体裁排除。

其余46家族保留潜在增量和一次日期/历史版本恢复请求，不评分、不记确定当窗候选：

| 身份组 | 实际潜力，不是采用命题 |
| --- | --- |
| 18866 LightMem、18699 Fetch、18551 SOCIA-Nabla、18515社会学习、18491 Crucible、18483 StarBench、18476意图belief、18395 MASMP、18289 Food4All、18179 adaptive coopetition | 分层记忆成本、协调/优化状态、低级视觉动作评价盲区、部分观察状态、约束接地失败与预算协作；不因任务局部或负面关闭 |
| 18314 Genesis、18477 LAFA、19861 SomeAttention、18541蒸馏后门、18358 Hydra | 攻击演化、FA planner有效性条件、hybrid消融边界、教师可信度、剪枝/OOD；必要安全/反侧见下 |
| 20222 QKCV、18849 critique/postedit、18830 MTraining、18713偏好理论、18680多教师、18927 BAPO、18583 CovMatch、18471 CodeRL、18413 Adamas、18383 MENTOR、18239 LIME | 模型表示、偏好/优化、稀疏通信负载、off-policy负优势梯度、低比特KV与工具过程奖励；不能把性能宣传当机制归因 |
| 19128 GADGET、19022 MoAlign、18716 SSD、18521 RayPose、18457 VFM-VAE、18353 DiffusionDRO、18313 OmniNWM、18291 GeoDiff | 控制安全软约束、运动表示、图像AR缓存、视觉codec、世界状态/行动条件；OmniNWM当前v6不代历史v1 |
| 19853 SpecificationRealm、18586 TokenCake、18544 SLICE、18525 SPEQ、18300 GPU tracing、2511.01866 EdgeReasoning | formal specification的前提、工具等待KV搬移、edge分段SLO、draft硬件、因果trace与latency-quality frontier；月份ID不决定首次公开日 |
| 18019水印、18030 GISP、18147难度、18196评分区间、18279视觉文本、18368 KoSimpleQA | tokenizer语言覆盖、全局迭代剪枝、difficulty-label混杂、judge区间偏置、压缩质量代价与语言/文化评价盲区 |

当前版本号及 submitted/updated 原值在四个API原件和 supplement.xml。重要修订不能由版本号推定；首次公开还缺官方历史公告或完全落窗bounds。未发现本次原页撤回标记，不为证明无标记遍历所有版本。

## 实际必要 core 阅读

以下均是精确 v1 HTML，文件名即版本；只读列出的命题，未遍历全文附件，未授候选 Evidence 完成或 Books。

- 18314 Genesis §3.1/3.2/3.4/3.6/4.1/4.2（399～997）：HTML不可见注入仅改action argument，不代表所有权限路径；ASR是pass@10且evaluation顺序学习，不是one-shot。§4.1把测试集写600，implementation写200，分母冲突保留，不能采用精确提升幅度或跨任务安全排序。
- 18541 后门 §3/4.1/5/5.1（433～735）：稀有trigger旧攻击不可靠转移，与distillation-aware常见token触发不同。Llama3.1-8B teacher/3.2-3B student，Alpaca/ShareGPT/math/code，选择best trigger呈现worst-case；跨数据集也有词共现。不能由clean prompts推出clean teacher，更不能声称所有后门都会转移。
- 18477 LAFA §III-A～D/IV-A（380～599）：三prompt planner/optimizer合并DAG，privacy继承既有FA backend及semi-honest前提，不是新密码证明。20个GPT4o生成查询、GPT4 temperature0、结构checker+人工计算结果核，不是生产恶意planner/DP budget组合验证。
- 19861 SomeAttention §2.1/2.2/3.2/4.2/5.2（316～680）：RG2B/9B、JambaMini1.6、100needle prompts/4096token，entropy top-k heads，默认generation稀疏。prefill改动会污染KV；Jamba未设置同类cache。零attention检索失败不证明所有SSM天生无检索能力；Binary实现未充分核验，不能借不合理ablation证明功能完全分离。
- 18358 Hydra §3.2/4.2/5.1（437～约760）：理论假设干净训练/测试stationary、small perturbation与noisy gradient非负对齐、Hessian差正定；不是任意剪枝必坏。M=3 head subnet ensemble、MLP merge、fusedMHA，ViT-B16/ImageNet/CIFAR、bf16 runtime1.07倍只绑定该配置，不是LLM所有OOD已校准。
- 19128 GADGET §3.3/4.3/5（495～约1346）：Eq24软penalty+梯度，不是每步投影到可行集合；理论CBF条件不能自动赋予生成轨迹硬保证。1000场景/环境、RTX3090、30采样选至少一条成功路径，collision intensity仍非零，BIT*限1s；不能说30条全安全或生产控制闭环已证明。
- 18457 VFM-VAE §3.2～4.4/5/AppD（355～约1119、2097～约2319）：冻结SigLIP2多层投影+多尺度decoder保留语义，仍有VF representation loss，不是完全消除所有alignment。REG改变latent、patch、batch256→1024、学习率等，8 B200；不能把同epoch收敛提升全部归因单个codec。只continuous latent/moderate resolution。
- 18019 水印 §3/4.3/Limitations（470～518、711～742、1390～约1414）：精确v1为17语言、500英语文本、三模型、translation攻击；当前v3摘要126语言不能静默代v1。Steam translation请求随支持语言线性增加，不防paraphrase，unsupported语言收益有限。
- 18196 judge §4.1/4.2/Limitations（328～约813）：SummEval100文档1600摘要、10%dev、Llama/Qwen≤14B，固定5级但换0-4/1-5/2-6/3-7区间，parse失败置最低/clamp。contrastive需要两模型成本，英文摘要相关性不证明所有judge unbiased，也不证明与speculation任意免费复用。
- 18368 KoSimpleQA §2.1～2.3/3.1～3.3/Limitations（330～416、669～约754）：文化事实+截至2023知识，四强模型至少一失败的选择条件，独立平台交叉核；temperature1/max2048。thinking超长未输出算NA，不能把abstain提升全归于更好不确定性。当前v2题摘938题不能当v1构造时1000目标；排行榜反转仅此受控短问任务。
- 18147 difficulty §3.1/3.2/4（367～704）：E2H-AMC人类label与GSM8K模型label同时改变数据集，cross-dataset gap不能单独因果归于label来源。60模型5fold probe，GRPO主线QwenMath1.5B单A100、单训练seed、greedy3000；checkpoint residual相关不是difficulty机制因果证明，局部反侧保留。
- 18395 MASMP §3.1/3.2/4.1/4.2（339～约535）：LLM natural-language emulates FSM而非verified transition engine，Simple64/DeepSeekV3/easybuildcontrol/winrate，不能推出复杂工程任务确定状态安全。
- 19850 decorators §3.6/4.3/6.3/6.9（1072～约1155、1580～约1633）：语义解释仍概率性、组合可能冲突；场景分析没有安全/确定生成保证，贡献关闭理由见上，不进入Books。

## 官方材料与恢复

DeepSeek-OCR 2510.18234完整官方题摘与version history实读；压缩/OCR质量代价可关联表示和上下文，但10/21新闻日名与submitted不是精确first-public，暂不采用。Seed3D 2510.19944完整题摘/历史实读，directory PublishDate=BJT10/22零点却v1submitted=10/22 18:16:32UTC，Blog10/23；目录日期不能代表正文已在本窗公开。MiMo2510.11370v1题摘与history实读：v1submitted10/13，v2submitted10/21 17:19:46UTC；本窗内submitted不证明公开或重要变化，不重复评分。

Hunyuan初次恢复误用主站 `/api` 得404，保留原件与真实记录；own index bundle确认API origin后实际 `https://api.hunyuan.tencent.com/api/blog/publicList` POST pageNum1/pageSize200/renderType0，code0/totalNum9，各标题日期最旧2026/02/03，停止页1。有限browser15s超时。不是普通404未处理，也不是2025无事件。

Qwen旧主页迁移，新 `https://qwen.ai/blog` 实际curl200保存qwen_new.raw，文本shell；web0行。浏览器两次visibility不支持、去参数后15s超时；这是较早Blog恢复，不证明Research不可达或历史末页。

## 07:23～07:26 本日三项定点来源恢复

本次fresh合同/22窗口/停点后独立请求，未复用21响应。实际请求时间/状态见THREE_SOURCE_RECOVERY.json。旧FETCH的Google `year/query`不能证明有效年份/主题过滤；正确`https://research.google/pubs/?category=2025&search=language%20model`18s超时、0字节，header原件保留；web同URL失败，有限停止，不由Blog替代论文入口。

官方RSS `https://openai.com/news/rss.xml` 200/759641字节，XML实际1245 item，以原pubDate解析UTC `[2025-10-21 01:00,2025-10-22 01:00)`，命中两项：Japan Economic Blueprint `Wed, 22 Oct 2025 00:00:00 GMT`；WhatsApp transition `Tue, 21 Oct 2025 17:00:00 GMT`。这只证明feed字段，不擅称首公开时刻。两个官方原文正文均实际读至结尾，工具原响应保存openai_rss_official_web_original.json：日本文章提出政策、教育/基础设施投资与宏观增长愿景，不披露模型/训练/执行机制，贡献前关闭，未扩其经济政策PDF；WhatsApp说明平台政策变化后的2026/01/15渠道结束与账户关联/聊天历史迁移，未披露新状态协议/可靠性机制或实验证据，贡献前关闭。没有因访问/日期而关闭潜力，亦不作Books已有覆盖判断。

新`https://qwen.ai/research` curl200/94344字节，web0行，原件是CSR、matchedIds layout/home而非带日期Research列表。own本日main.js实际research route→p_research-index.js，两者及HTML指向的5fb222f6.js皆200，另实际4467.js404。Research模块实际使用X=44467的uZ/fA/cy，cy GET参数type=qwen_ai/language=en-US，将静态过滤数据与$.data.articles合并；三份已取JS未取得相应endpoint常量/历史列表。原文件与header为qwen_recovery_main/research/shared/4467，止四资源，不无限取全部chunks或猜测接口。普通新入口恢复已做，剩余为必要2025目录/日时刻材料缺失，不证明无事件。

root FIRST_INDEPENDENT_REVIEW六v1+四分层题摘已实际通过，继承具体潜力/日期隔离结论，不自行授DAY。上述新增来源及两公告关闭只交root窄回核；未重新下载54题摘或13core。
