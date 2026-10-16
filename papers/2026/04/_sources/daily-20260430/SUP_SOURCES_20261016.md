# 2026-04-30 来源遗漏补充（2026-10-16）

## A1 范围、冻结与独立性

本轮作者：supp_apr30_author_fresh。按当前 AGENTS、研究合同、Report V3、Prompt 和每日来源主题独立执行。仅补北京时间 **2026-04-29 ～ 2026-04-29**；用户要求原 34 家族整行（含日期与评分）、旧 `2026-04-29T09:00:00+08:00 ～ 2026-04-30T09:00:00+08:00` 窗和连续原 §4 正文保持，冻结依据见 [baseline](baseline-before-supplement-20261016.md)。旧完成声明不授本轮验收。未扫描每周来源、未重跑旧 Weekly/Live、未修改 Books/共享索引/LEARNING_STATE，也不 stage、commit、push。

仅把官方本窗目录的相关标题当查漏线索，再读完整题摘判断具体贡献；不从旧 Complete、历史候选池或整类库存推准入。首次公开日期以官方公告/赋号规则和精确版本身份联合确认，Submitted 不单独代表公开。当前日期执行为北京时间 2026-10-16，后续修订不能倒灌本窗。

## A2 实际入口与停止点（进行中）

- arXiv：`https://arxiv.org/list/cs.AI/2026-04?skip=4000&show=2000` 实际取得末页（官方动态总数 5027/5030；数量不作当天论文数）；以 2604.248xx–25918 的本窗边界线索浏览模型/Agent/训练与安全标题。`cs.DC/AR/PL/OS/PF/IR/MA/RO` 月表 `skip=0&show=2000` 取得各自末页；`cs.CL/LG/CV` 另检查 `skip=2000&show=2000` 末段，只有相关标题才读题摘；未做整类逐篇关闭。CL 的首次 web 入口 429、export API 一次失败，不以空响应认零；shell 官方原始入口可恢复。月表仅发现，精确 v1 页作身份、题摘与轻量撤回/修订信号检查。
- OpenAI：Research 首页实查；尚缺历史 Research Index 页，不能据首页认 Apr29 无发布。补检 `site:openai.com "Apr 29, 2026" research` 出教育 agents 通讯和状态故障页，前者是采用/协调介绍、后者无公开失效机制，不凭主题关联入选。
- Anthropic：Research 首页实查；日期补检命中 [BioMysteryBench](https://www.anthropic.com/research/Evaluating-Claude-For-Bioinformatics-With-BioMysteryBench)。2026-04-29，完整核心说明为真实生物数据任务、专家及模型对比，按当前 AI for Science 暂缓排除，不借 evaluation owner 重新纳入。
- Google：DeepMind Research 首页实查；当前首页非 Apr29 历史闭合证据，Publications/News 历史段尚普通待办。
- Qwen：旧主页仅至2025/09并明确重定向 qwen.ai，后者尚待；不认零。
- DeepSeek：首页 Research 列表实查，More 历史层待恢复。
- Moonshot：Kimi Blog 可读列表仅至2025/11，2026历史层与官方仓库仍待，不能据此认零。
- Hunyuan：首查官方 Research web 超时，仍需浏览器定点恢复；不是不适用。
- ZAI：Research 时间序列实查：05/20 ZCube → 04/29 Scaling Pain → 04/07 GLM-5.1。Scaling Pain 已在原34家族，去重且不重复评分；本轮未发现新family。
- Seed：Research 目录实查可见05/16 Charon→04/26 MegaScale-Omni→04/22 Seed3D2；Publications历史层尚待，不能把精选序列作全覆盖。
- ERNIE、MiMo、MiniMax：本轮官方入口已请求，具体日期段与停止点待补录。

## A3 首批准入校准包（完整题摘已读；待 root 独立校准）

日期目前待完成公告批合证，以下为首批未经去重校准的拟入选；A5裁决后仅25359保留拟入选，其他五项为有效事件去重，不新评分/不移动旧归属。原初拟分仅保留过程依据，不能当本轮候选分母。

| 身份 | 具体准入依据 | 拟最低评分/必要证据 |
| --- | --- | --- |
| [2604.25080v1 CacheFlow](https://arxiv.org/abs/2604.25080v1) | 旧恢复按单请求重算或I/O二选一 → token/layer/GPU并行并把batch资源争抢纳入two-pointer调度 → KV恢复选择须在共享batch资源下优化而非逐请求局部最优 | 2+2+3=7；精确v1方法、batch对照及拥塞代价 |
| [2604.24971v1 PolyKV](https://arxiv.org/abs/2604.24971v1) | 每agent独立KV与单上下文压缩分开 → 一次共享非对称有损KV注入多个独立reader → 共享前缀容量收益与有损误差、扩写隔离应分账 | 2+2+2=6；是否真实零拷贝共享/解压和并发分叉语义是关键反证 |
| [2604.25899v1 Pythia](https://arxiv.org/abs/2604.25899v1) | serving把agent调用作通用流量 → 通过workflow接口暴露角色/依赖带来的可预测性 → 缓存、长上下文争抢与扩缩容可按工作流联合决策 | 2+2+3=7；精确v1接口/预测失误及生产trace与实验边界 |
| [2604.25050v1 DiscreteRTC](https://arxiv.org/abs/2604.25050v1) | flow动作块RTC靠额外inpainting修正 → 离散diffusion把已承诺动作冻结、原生unmask其余 → 连续执行的commit边界可由训练生成机制直接承载 | 2+2+3=7；动作延迟/冻结位置/early-stop真实对照 |
| [2604.24920v1 SUDP](https://arxiv.org/abs/2604.24920v1) | 让agent取bearer secret使瞬时注入成为持久权能泄露 → requester提规范operation、user授权fresh grant、custodian一次redeem → secret-use权限可操作绑定而不把可重用凭证交给模型 | 2+2+3=7；精确v1威胁模型、nonce/规范化/消耗原子性与密钥擦除假设 |
| [2604.25359v1 Structured Output Benchmark](https://arxiv.org/abs/2604.25359v1) | schema合规被当作提取可靠性 → text-normalized三来源隔离感知与结构输出、leaf-value另评 → grammar通过不授内容正确，需核数据/指标混杂 | 2+1+2=5；协议与上下文长度反证，非原始多模态能力对比 |

代表排除：

- [2604.25110v1 Knowledge Distillation Must Account for What It Loses](https://arxiv.org/abs/2604.25110v1)：完整题摘是position与既有损失分类/Distillation Loss Statement倡议，没有新增失效证据或可验证的新保存机制。不能仅因谈不确定性、安全或蒸馏便准入；当前无撤回/纠错信号。
- [2604.24826v1 A Comparative Evaluation of AI Agent Security Guardrails](https://arxiv.org/abs/2604.24826v1)：题摘只有四产品在作者数据上的recall/TNR排行榜，未给新失败机制或评价混杂证据；先范围内明确EX，不为无关日期核验扩审。安全主题本身不构成安全纠错信号。
- Anthropic BioMysteryBench：AI for Science 暂缓（见A2），并非没有学术价值。
- ZAI Scaling Pain：原34中同事件有效具名审阅复用，只去重，非新增/非EX。

## A4 当前真实待办

首批准入独立校准、公告日期合证、其余相关题摘、十四每日来源历史层、拟入选的必要原文和Books具体owner比较、必要窄写/实际POST、六部分日报融合与独立DAY均未完成。没有自签或预支完成。

## A5 首批准入 root 独核与跨日有效层去重（2026-10-16 08:29+08）

root 实际打开25359/25110/24826的exact-v1官方abs完整题摘/notice后：25359保P5，具体潜力限text-normalized三来源的评价身份隔离；必要Source须核normalization、GT、长度及21模型比较，不把数据规模或已有schema≠semantics单独称新增长期知识。25110和24826按A3具体理由EX可保；未发现本页显式withdraw/erratum，版本标签不触发全历史深审。

本轮定点ID检索2026非Weekly README候选表，再只读命中的04-29具体§4：24920 SUDP已有Ch72 operation-bound secret-use正文与POST；24971 PolyKV已发现uint8/3bit表示及每agent解压与池bytes/并发peak混淆，中心争议隔离；25050 DiscreteRTC原生mask训练/冻结前缀/近端早停已有Ch26正文与POST；25080 CacheFlow三维依赖/批资源和boundary activations已有Ch45正文与POST；25899 Pythia workflow/session/role低权限身份、预测回退已有Ch56正文与POST。精确v1事件、采用命题和未决均匹配，故五项分层有效复用，不再重读全文/评分/入Apr30候选，也不移动04-29旧小时日期。

同一标题线索集合的33个已入选ID均指向04-29原候选行：24920/24921/24927/24952/24953/24955/24957/24971/25050/25072/25080/25098/25102/25109/25203/25213/25235/25249/25306/25380/25421/25491/25591/25636/25800/25819/25855/25859/25872/25891/25899/25907/25917；其余尚未被本次身份检索命中的36条相关标题才继续完整题摘贡献筛选。身份命中本身只支持去重路由，不把这33项称本轮新深审，也不沿旧池扩发现。

## A6 窗口边界纠偏与其余首批完整题摘（待独核）

不能以submitted cutoff把24833/24834当公告批下界。root提供且本作者实际打开官方规则[赋号与公告](https://info.arxiv.org/help/availability.html)：ID于公告时赋予、不能回填；早提交可延后公开。仅日期合证复用官方原始DataCite两侧 [24764](../daily-20260429/SUP_DATE_24764_20261016.raw.json) / [24765](../daily-20260429/SUP_DATE_24765_20261016.raw.json)：created分别Apr28/Apr29；另本日原始来源的25918/25919相邻批边界为Apr29/Apr30。月表、公告槽和exact-v1身份共同支持Apr29批 **24765–25918**，不是单篇提交或DOI时间单证。发现已补看24765–24833主题标题；既有24806/24809/24819/24820等按身份去重，不迁原归属。该批的主题发现不是全1154个ID逐篇队列。

以下全部已读官方完整abs-v1题摘。标题、原件均为 `https://arxiv.org/abs/2604.<ID>v1`，必要证据优先同ID的 `/html/` 版；此处尚未冻结候选。首公开资格保留亦先定点查全README，不能只凭未在§3命中认新。

| ID | 原约束 → 具体增量 → 设计判断 | 拟评分 | 状态 |
| --- | --- | --- | --- |
| 24938 | 通用layer redundancy排名 → calibration objective可比search更大改变排名 → PPL校准不代签下游剪枝 | 2+1+2=5 | 拟准入，待源 |
| 24940 | 单embedding/多anchor扩展贵 → VP单矩阵、组位置共享、context重权 → 多anchor的token/参数与表达取舍 | 2+1+2=5 | 拟准入，待源 |
| 24964 | 长程web二元成功压缩过程 → rubric级判分、人类对齐与score/step → 任务完成与效率分账 | 2+1+2=5 | 拟准入，待源 |
| 25031 | formalization无标签忠实性难证 → roundtrip二次形式化等价、诊断修复 → 等价一致性不等原意正确 | 2+1+2=5 | 拟准入，待源 |
| 25143 | AdamW更新轨迹当特征形成信号 → per-task gradient SVD恢复诊断、随机rank3也加速 → diagnostic与唯一因果分离 | 2+1+3=6 | 拟准入，待源 |
| 25150 | 宽度收益只看参数容量 → 等价symmetry改变Hessian条件与可达性 → 函数不变亦可改变优化几何 | 2+1+3=6 | 拟准入，待必要定理 |
| 25161 | end-to-end失败不定位能力 → capability oracle引导mutation/归因 → failure attribution需核oracle及因果权限 | 2+1+2=5 | 拟准入，待源 |
| 25289 | 无time DDIM差但FM可行 → noisy manifold分离/路径决定time可辨性 → conditioning必要性是路径/分布条件 | 2+2+3=7 | 拟准入，待定理/反例 |
| 25299 | diffusion图像token难递归 → joint attention内递归+稀疏module gate → 模型深度与共享参数可换额外latent compute | 2+1+2=5 | 拟准入，待源 |
| 25326 | operator同步或失控异步浪费 → NPU/PIM task解耦+entropy/history/time控制 → draft调度与物理验证资源联合 | 2+2+2=6 | 04-29§5已有首公开资格保留，先恢复必要日期，暂不授本窗 |
| 25349 | Wilcoxon被默认无分布安全 → IR成对差值条件下TypeI失控证据 → 评价假设不是选非参数名词 | 2+1+3=6 | 拟准入，待必要统计假设 |
| 25359 | 原生多模态与提取混杂 → 固定text-normalized输入及多层schema/value指标 → 评价链按阶段分界 | 2+1+2=5 | root准入通过，A8必要源已备 |
| 25372 | ZO普遍额外维度率惩罚 → ISS有界扰动下FO同衰减至邻域 → 比较收敛率须带噪声/半径/代价条件 | 2+1+3=6 | 拟准入，待必要定理 |
| 25379 | penalty仍探索不安全 → safe-support行为策略、KL Bellman与分阶段提policy → 不离开支持域的安全/探索前提 | 2+1+3=6 | 拟准入，待必要安全条件 |
| 25477 | 编辑质量混planner/editor → fixed-editor双atomic checklist反馈 → planner动作计划与最终视觉reward分账 | 2+1+2=5 | 拟准入，待源 |
| 25562 | 大VLM检测截图注入贵 → 视觉梯度稳定/反色OCR动作词双sensor → 视觉间接注入可测廉价特征但非安全oracle | 2+2+2=6 | 拟准入，待源 |
| 25634 | provenance需内部/水印、验证贵 → rankfrequency族拟合与CPU triage → 词汇异常与事实真值严格分离 | 2+1+2=5 | 拟准入，待源 |
| 25642 | decode steering累积残余幻觉 → prefill一次性modality-aware K/V分治 → cache注入位置与后续生成失效分账 | 2+1+2=5 | 04-29§5已有首公开资格保留，先恢复必要日期 |
| 25716 | 英文codebook跨语高AUC当安全 → OOD unsafe多样性低FPR recall崩落 → canonical template迁移非语义安全保证 | 2+1+2=5 | 拟准入，待源 |
| 25777 | federated ensemble全概率通信贵 → topK重建与acceptance bias界 → 压缩后聚合分布不是原target | 2+2+2=6 | 拟准入，待源 |
| 25779 | 一步subliminal梯度理论不授多步 → MNIST持续alignment及干预 → 多步机制证据与mitigation残留分账 | 2+1+3=6 | root提示Mar11更早项目正文线索，先资格核，不评分正面 |
| 25898 | CORL replay有memory/离线分布差 → action compatibility+latent similarity路由稀疏subnet → reuse须task/action域绑定 | 2+1+2=5 | 拟准入，待源 |
| 25903 | 压缩多组件只看各自收益 → pipeline ordering消融与质量/时耗/碳成本 → 顺序收益须端到端同质量/硬件比较 | 2+1+2=5 | 拟准入，待源 |

明确EX（完整题摘后，不要求为无关日期再追溯）：25085是经济principal-agent资源欺诈审计博弈，无模型/Agent系统机制增量；25358提出新layout集合及semantic/spatial合成分数，题摘未给能修正设计的新增盲区/混杂证据，规模/排行榜不足；25853在BERT分类使用已有label-propagation similarity图正则，未给改变表示学习边界或设计选择的新条件/反证，不能仅因新loss名准入。上述共同理由待分层独核校准，不作为全量排除验收。

## A7 九项含糊题摘的最小core（非惯性全文）

- 24954 Nemotron：精确v1 §2原生比例patch、pixelshuffle、2-frame Conv3D、audio30秒clip与时间interleave确有可核机制；但[NVIDIA官方更早Apr28发布](https://blogs.nvidia.com/blog/nemotron-3-nano-omni-multimodal-ai-agents/)已连模型、权重与技术正文，arXiv Apr29不单独证明family首发。先日期/事件资格核，不以厂商声望入选。
- 25039 Dual-Track：§6.2/7.3/8，不只是双agent组合；已接受math fingerprint和低分fingerprint两类reject cache避valuator，同50题下200/400/500 token仅2百分点、CI重叠、600tokens同70%；embedding cache约60%低于lexical70%，相近数学文本误拒可修正。具体cache身份/反馈边界可作P5（2+1+2），待独核。
- 25136 FPO：§6/§8/结论，clarify/verify/refuse显式动作，现有reward/DPO/GRPO/TRPO加入friction proxy，未给可验证的新控制稳定条件或经验结果，§10承认实施验证未来。当前倾向EX：概念重述不因formalism升级为机制；不是“没有大实验就无价值”。
- 25182 CroSearch-R1：Alg1/§2/§3，只在查询语言→其它语→English的预定阶段检索；KnowledgeNorm翻译，跨语rollout与c3Recall reward有直接消融。4语Qwen2.5-3/7B上缺c3Reward降最大；可P5受限报告“增加语言也可引噪，原语anchor+按需跨语补证”，不说普遍防噪保证。
- 25276 OmniVTG：§3.1/Fig1c/Table4，timestamp densecaption相对直接grounding更准，稀有词覆盖后人工修边；Self-Correction的content-aware reflection相对rule-based虽受限但直接对照可核。可P5保“数据标注接口与目标任务能力不等价”，不是仅收大数据集。
- 25313 Faithfulness-QA：§3.5–3.6/§7–8仅typed实体字符串替换+存在性检查，无coref/NLI/真实parametric-conflict检测，暂无训练/LLM行为结果；“99k冲突已制造”不能由实体换名推出。当前倾向EX：既有entity-substitution规模化resource，没有新增机制边界证据；保具体局限而不把自动检查100%叫忠实性证书。
- 25427 Video Posttrain：§3.2依DanceGRPO/MixGRPO、§3.3依Causal/SelfForcing，四段既有机制拼装；§4.2只internal-model GSB+31%、PE+20%，未披露分母/对照预算或能改变机制选择的条件。当前倾向EX，不把宣传广义worldmodel结论采用。
- 25578 Marco-MoE：§2.2把dense FFN切细expert，softmax平均需补N；lambda=N^(1/3)同时缩放SwiGLU三个权重被称数学等价，但SiLU非正齐次须反核。来自已有Drop-Upcycling的全新组合不单独入选；“继承信号尺度与router归一化不匹配”及相关loss-spike消融是可核P6（2+2+2），拟必要深审受影响公式。
- 25809 IECD2：§3.1–3.2仅同VLM不同prompt双分布，symKL gate融合，并无独立evidence oracle；Table4对gate有直接对照。倾向P5“同源提示分歧sensor可改变解码但不升级grounding权限”，是否有长期差额须实际owner核，不凭主题误收。

## A8 25359 exact-v1 必要Source（作者完成，待独立核）

采用版本 [HTML-v1](https://arxiv.org/html/2604.25359v1)，实际必要位置 §3、§4.1–4.4、§5.1–5.2、§6.6–6.7、§7及AppendixH。固定OCR markdown/AMI gold transcripts后所有模型只看text，从而隔离front-end能力，但不是原生image/audio评测；原source不同长度/98%audio hard-schema混杂仍存。21模型仅20做audio（Phi4超16K），greedy、maxout2048；GPT5/mini/R1不能完全关闭reasoning，不称严格同compute对照。GT人工并Gemini校核；text抽检5×100仍约3%残差，不能把校核当真值无误。

JSON schema gate后各semantic score还乘h，text coverage floor .95，image/audio .90；总分按schema complexity权重聚合，而全域权重13054/602/343明显text主导。exact leaf与ordered arrays会错罚同义/集合重排；AppendixE/F有实际反例，§7明说无gate敏感度和constrained-decoding对照。因此只支持“按表示阶段标注测量对象、语法/字段语义分账”，不支持audio感知差/模型普遍可靠性排名，也不将23.7%当ASR结果。尚需实际Ch66/51 owner对照后定NC或最小差额，未预支Books。
