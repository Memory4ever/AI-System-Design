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

## A8 25359 exact-v1 必要Source（作者完成；reader按未变有效层复用EX）

采用版本 [HTML-v1](https://arxiv.org/html/2604.25359v1)，实际必要位置 §3、§4.1–4.4、§5.1–5.2、§6.6–6.7、§7及AppendixH。固定OCR markdown/AMI gold transcripts后所有模型只看text，从而隔离front-end能力，但不是原生image/audio评测；原source不同长度/98%audio hard-schema混杂仍存。21模型仅20做audio（Phi4超16K），greedy、maxout2048；GPT5/mini/R1不能完全关闭reasoning，不称严格同compute对照。GT人工并Gemini校核；text抽检5×100仍约3%残差，不能把校核当真值无误。

JSON schema gate后各semantic score还乘h，text coverage floor .95，image/audio .90；总分按schema complexity权重聚合，而全域权重13054/602/343明显text主导。exact leaf与ordered arrays会错罚同义/集合重排；AppendixE/F有实际反例，§7明说无gate敏感度和constrained-decoding对照。因此只支持“按表示阶段标注测量对象、语法/字段语义分账”，不支持audio感知差/模型普遍可靠性排名，也不将23.7%当ASR结果。尚需实际Ch66/51 owner对照后定NC或最小差额，未预支Books。

## A9 下界/主分类标题查漏新增29条完整题摘（已读，待独核）

本组由本轮官方月表主题标题独立发现，逐ID定点全2026非Weekly README查身份，不从他日候选池推名单。所有完整题摘均实际打开官方abs-v1；现仅分准入潜力/具体EX/同事件有效层和日期例外，不提前冻结候选。

| ID | 具体判断与拟贡献链 | 当前处置 |
| --- | --- | --- |
| 24785 Cloud to Edge | SBC硬件/吞吐/功率/尺寸多指标工作点，没有新增执行机制或能修正选型的反例条件；不能仅edge主题准入 | EX |
| 24794 V.O.I.C.E | incident/问卷/Reddit风险分类与群体暴露法律背景，无可验证模型/系统失效机制新增 | EX |
| 24801 Observability | 同题完整PDF官方release于Apr27公开，非Apr29新家族 | prior-public隔离，见A10 |
| 24804 RMiPO | response MI作为DPO局部调loss/超参数proxy，现无分离新选择条件的题摘证据；原具名EX理由未变 | 具体有效层复用，独核记录114 |
| 24814 SWE-QA | 新12 repo多跳MCQ与模型榜单，未隔离能修正评估或模型设计的具体盲区证据；MCQ高/低分不授真代码执行 | EX |
| 24827 IKP | 推理题饱和不等知识容量饱和 → factual probe回归total/active参数与代际系数 → 参数估算需核独立facts/编码下界及refusal混杂 | P6（2+1+3），待必要源/更早身份 |
| 24832 Blockwise MDM | 块内local AR/块级refinement是具体依赖方向分支，但原Mar18代码公开资格未可证 | 日期Hold复用，不列正面 |
| 24833 MotionBricks | 大动作库实时生成与细控制接口冲突 → modular latent backbone+smart primitives → 尺度/延迟/控制语义能否分离 | 含糊，最小core待，不因15000FPS先准入 |
| 24878 Transformer Approximations | universal approximation不给资源 → ReLU到softmax原语的target-specific资源界 → 表达可行与宽/深/精度预算应分账 | P6（2+1+3），待必要定理 |
| 24959 CoreFlow | 高维matrix小样本脆弱 → 共享row/column子空间仅core上flow、masked Riemannian补缺 → 结构共享条件与生成/压缩偏差 | P6（2+1+3），待范围/机制独核 |
| 24978 EDR | outline/reflection+dependency context+evidence stop，题摘是成熟workflow组合；原独核已核具体未隔离新边界 | 有效EX层复用，不因旧Complete |
| 25073 TBA | 搜索crash/invalid浪费小预算 → feasibility先探索+timeout/暂时blacklist再TPE → 优化器应把可行性发现和最佳点搜索分阶段 | P5（2+1+2），待源 |
| 25096 Dynamics of Delusion | 人类/聊天日志的latent influence拟合，不能因bidirectional拟合更好就识别模型内部机制或人类因果；无新模型系统设计条件 | EX（不作临床风险结论） |
| 25130 LongSumEval | QA answerability/factuality反馈再summary自修正，现题摘未区分成熟QA-eval+refinement之外的新失效/控制条件 | 含糊，最小core待 |
| 25135 FAMA | 同任务失败分类后触发固定helper subset，已有plan/feedback路由实例；原独核受限holdout/token税反侧与owner未变 | 有效EX层复用 |
| 25409 PT muP | 为probabilistic Transformer调重参数尺度，原独核为μP局部recipe/阈值，未新增主线机制边界 | 有效EX层复用；不同理论新命题须具体论证才重开 |
| 25444 ReQueR | 每solver微调成本 → 训独立refiner并adaptive solver hierarchy curriculum → one-to-many query elicitation的solver难度/泛化边界 | P5（2+1+2），待源 |
| 25467 SSF | FL subspace节通信但换基丢control残差 → projected correction+backfill保留未投影状态 → subspace切换与完整control信息分责 | P6（2+2+2），待必要源 |
| 25508 Dyna-SAuR | 学习动态的safety filter过保守 → 模型certain域/策略共同迭代扩张 → 低uncertainty与真实safe前提须分账 | P6（2+1+3），安全信号必要源待 |
| 25580 Perspective | proprietary测量工具无版本更新/终止导致benchmark失效；题摘主为治理议程，现无独立新测量反证或机制 | 倾向EX，停用事实若采用须官方核，不凭论文证明厂商状态 |
| 25611 WhisperPipe | VAD+滑动overlap buffer+动态batch的ASR工作点，原独核已有buffer/VAD实现不新增长期机制条件 | 有效EX层复用 |
| 25654 Cultural alignment | 题摘仅既有数据局限/设计guidelines与对比区分度，核心不明确为何culture变量不混难度 | 含糊，最小core待 |
| 25676 CORAL | fixed corpus mRAG无法处理文化query → evidence critique同时改语/区域corpus和query → 只重写query可能维持错误检索域 | P5（2+1+2），待源 |
| 25702 Backtranslation DPO | 将现成DPO用于英德翻译反馈，只单语言COMET增益，未给新的偏好学习机制/成立边界 | EX |
| 25783 Subliminal Steering | 具体隐性bias实验潜力不等首公开，原Apr18 README/Apr23Blog历史可见性保留 | 日期Hold复用，不列正面 |
| 25858 ICL Gaussian | 理论条件不替代有限训练规模 → dimension/context/tasks/SNR控制扫描与noisy-label benign overfit → ICL长度/信息几何成立区间 | P6（2+1+3），待源 |
| 25866 emotion SAE | SAE shared/emotion-specific分层+causal feature steering、跨数据集及LM保留 → feature可读性/因果可控与任务特异性分责 | P5（2+1+2），待源，不因emotion应用自动保 |
| 25904 Teacher Forcing | chaotic surrogate的forced regime与marginal likelihood曲率不同，Lorenz证据/动态QoI相反 → 是否直接提供可复用模型训练失配边界 | 含糊范围/必要定理待；不借WorldModel owner引入AI4Science应用 |
| 25914 DV-World | native-object/visual/ISR lifecycle benchmark的接口与judge边界已有具名Source/owner EX | 有效EX层复用 |

## A10 已有精确事件有效层复用与首公开隔离

root明确准许按研究合同§7，对本轮独立发现的具体ID定点复用他日具名有效层，禁止由旧Complete或大池批量授审。本作者实际读[25634必要反侧](../daily-20260429/V3_UNIVERSALITY_25634_REVERSE_ADMISSION.md)、[25777必要反侧](../daily-20260429/V3_SPECFED_25777_REVERSE_ADMISSION.md)及[独立source→actual-owner原裁决](../daily-20260429/V3_APR28_FINITE_SOURCE_OWNER_REVIEW.md#来源日期准入负侧的有限最终复核)：身份、v1、命题和未决匹配，无本轮新反例。25634的模型身份ROC仍未来、lexical score只是已知sensor工作点；25777 topK改target、Eq19少1/2而Eq20较窄界正确，跨网络whole-trajectory质量/时耗缺失，不超Ch48既有分布/成本合同。故两项是具名前分母EX有效复用，不重复评分、全文或Books。

本轮作者另已读[25779 Mar11作者项目](../daily-20260429/V3_SUSTAINED_GRADIENT_25779_DATE_ISOLATION.md)、[24801 Apr27作者完整PDF release](../daily-20260429/V3_ARCH_OBSERVABILITY_24801_EARLY_PUBLIC.md)，保留真实较早首发资格；不是当窗漏项，不改归属。25326/AHASD 2025/11旧README核心、25642/PTI Apr26核心README、24832/MDM Mar18代码、25783/steering Apr18README/Apr23Blog的历史public可见性不明，按各具名单篇必要公开archive/平台日志或正式发布请求复用日期Hold，不让arXiv Apr29单证覆盖相反线索。缺件不会被叫零命中或证据通过。

尚可执行普通项依A6/A7/A9与reader自有R30区推进，来源历史段仍待闭合；本日未授DAY。

## A11 作者必要Source实际停点与反侧（继续，不授日级）

本批均采用 `https://arxiv.org/html/2604.<ID>v1`；25676/25903的HTML实际404，已成功读取官方 `https://arxiv.org/pdf/2604.<ID>v1`，不是把可读PDF伪列缺件。必要Source仅审下述命题，未运行artifact或复现实验。

- **25379 SafeSupport-Q，P6**：§4.1–4.3/§5实际读。严格support约束依赖行为策略本身安全；§4.2为log数值稳定引入 `tildeπ=(1−η)π_b+η/|A|` 后，所抽取policy `π*∝tildeπ exp(Q/λ)` 在原support外仍有正概率。有限Q/η>0即构成硬安全采用的反例；Remark“只smooth target不collector”并不能认证最终提取policy安全，连续Gaussian同样不授真实安全域。FrozenLake/CartPole、5seeds与不完美DS行为结果只支持受限recipe，不采无探索风险保证。reader已实际窄核；中心强保证争议隔离，Books不正面采用。
- **25477 DDAThinker，P5**：§III-C/IV-C、TableIV/VI及limitation。冻结editor，cognitive checklist仅评`<answer>`执行计划、不评`<think>`；两reward各有独立rollout/minibatch streams及组内归一，不是先加权成单标量。TableVI weighted37.5→separate40.0仅作者固定editor/data条件；sampling ratio仍有隐式目标权重，judge/checklist不是真值，未证明分开训练普胜joint。actual Ch33 117–136已有独立人口/归一后混合、同参数梯度竞争及完整费用；此处额外独立stream是具体实现对照，拟仅报告，不为重复原则造Books。
- **25716 cross-lingual codebook，P5**：方法/阈值、Table1/2/3/5及OOD段。须分清Table2逐语言validation的低FPR工作点、另用globalτ=.66的迁移/attack实验，不能把所有低召回都称英文阈值直接迁移；四语由Google/M2M100翻译无human postedit。三种OOD模板低FPR TPR仅个位数，跨模板AUC约.59–.70；两张translated AUC表数值口径不一致，不混合headline。ASR1是通过filter后条件人口，不能当全流量成功率；canonical/diverse攻击降幅不同。拟具体owner比较，保该局部阈值反侧，不授通用防护。
- **25898 TSN-Affinity，P5**：方法/affinity、Table1/2及限制。冻结旧task mask，新任务以expert actions的CE/MSE与encoder latent Gaussian KL比较reuse/copy，部署已知task ID并恢复norm/actiondim；额外完整copy不是免费容量。Atari最佳action/latent约89.7/89.6但4/5copy，hybrid1copy约73.4；Panda latent3copy gap.670对replay1copy.729，hybrid2copy1.546反退。actual Ch30 826–855已有expert演化/冻结、proxy与task身份、容量/路由增长和行为回归分责，拟具体已有覆盖；动作physical验收仍归Ch26。
- **25073 TBA，P5**：§6.2/6.6–6.8、§8.3/9.3–9.4/12。feasible-first SA先找可行，再转有正负样本的TPE；timeout5×和临时blacklist只探索期、TPE仍全空间。timeout同用于所有optimizer，不能全部算hybrid独占。五GPU图像分类/约2000组合、5080十seed其余五seed；primary准确率.761≈random.762，浪费42%仍高TPE36%，发现vit8/10vs3/10；T4先前2/5→3/5后与TPE相同，A100仍有未触发timeout的陷阱。只保小预算结构发现/无效试验成本分账，不授普遍准确率/latency最优；owner待。
- **25444 ReQueR，P5**：§3/4.1/4.3–4.4。Refiner按group全错→较强solver、全对→较弱solver校准反馈，PPL answer-drop作leak proxy。训练仅Qwen0.6/1.7/4B非thinking+2048RL题，跨模型固定gen Avg@4/temperature.6；Table6去ASH退步，不能由此证明通用reasoning trigger或语义无泄漏。Query rewrite本身含小型求解，PPL下降不等已证泄漏，额外4B生成与多solver训练都计费；部署response token下降不等端到端低时延。拟owner比较/受限报告。
- **25467 SSF，P6**：§3全部必要机制、§4.1–4.2/Thm1假设与结论、§5.1/5.3–5.4。共享正交随机P的低维update/通信，与CPU保留完整model/control正交残差分责；每轮重建full model并算ambient gradient，不采用§3.7按r降低gradient计算的泛称，更不采intro“不引入full control”的矛盾句。收敛条件显含ρ=r/d及较小step，未授任意投影/全局最优；CIFAR-100/ResNet110四workers100epochs final45.43 vs fullSCAFFOLD52.92，原文承认非严格equal-compute，不能写质量保持或纯残差单因果。owner待。
- **25508 Dyna-SAuR，P6**：§3–5.4/§6.1–6.4/8。E是模型一定阈值内的certain-domain，不是physicalsafe证书；hyperplane filter在learned model rollout里训，再和control共同迭代。初始化dataset给两model-based baseline，另外两法预训练等transitions后才计失败，不把图作从零完整生命周期安全。10seeds/99%CI两toycontrol，Walker高维扩域不充分；Eq17把log折现moment写平均failure-time存在随机T反例，已交reader窄核，不把failure减少实验随之全部推倒。只保经验过滤接口，硬安全/mean-time解释隔离，Books待争议处置。
- **25372/25562/25634/25777**：作者已实际读对应必要原文/具名反侧；与A10及reader有效层匹配，不因本次重读再入选。25372只支持期望平均迭代的强凸ISS邻域（σ/t与dimension半径仍付费）、非LLM验证；SnapGuard low-gradientvariance加OCR无用户intent输入且截图FPR.14/截图TPR.13，不能升格授权gate；均保原具体EX，不重复评分。

25143/25289/25349三处reader必要Source/actual owner/逐字PRE通过，root已授Ch4/24/66指定单段+本人注lease；作者实际保存，非writer actual POST完整正文/两侧/本人注通过并仅修两空行，root已接纳释放。日期/来源/其余有限Source及owner仍普通，不以3项整合授DAY。

## A12 作者后批必要Source与新增官网身份（reader待独核）

- **25858 ICL，P6**：exact-v1 §2.1–2.3/§3.1–3.2/§4.1–4.2实际读。主体是单个learnable矩阵W与label-weighted empirical mean的线性分类器，不是完整softmax Transformer；SGD.01/zero init/最多1000steps、三seed，每步重新生成Gaussian任务。d/N/task batch/SNR联合扫描是具体条件诊断；把noisy context标签上的自身分类与clean新query另测，query也加噪时评价上限不同。只保此合成设置中的memorization/generalization分账与SNR条件，不采用“任意维度终到1.0”或LLM同等理论；best-validation选择、初始accuracy随batch变化及噪声标签口径仍须保原曲线而不造精确阈值。拟仅报告（有限设计诊断，不新造通用ICL recipe），reader待。
- **25866 emotion SAE，P5**：exact-v1 §3–6/Table1–4及Limitations实际读。Gemma2 2B/9B、Llama3.1 8B的residual SAEs 16K/32K，在六个label logits上分类；9870个自报情绪文本，不是开放生成/真实情绪理解证书。按零feature后logit/后层feature变化、每阶段top5%贪心反向找路径，再训乘法scale，CE+outputKL+L1；只支持所测activation intervention，不识别唯一完整自然回路。Table2总体F1涨但个别emotion/domain弱于其他steering；Gemma9B PPL13.25→14.51、Llama11.49→12.41，不把“≤10%”写语言无损，少数fewshot仍强。actual Ch16 245–282已有SAE/probe作用对象、独立最终输出/无关能力、干预成本/强度退路；此篇跨阶段具体路径只作受限报告，不扩emotion应用owner，reader待。
- **25676 CORAL，P5**：HTML404后officialPDF实际p3–9/§3–5.4/Tables1–3及Limitations。planner同时选13语言Wiki corpus与重写query，critic四维每项≥2、加权总分≥6；每corpus先top5，跨轮累积，最终top5不代表中间检索/调用同预算。planner/critic同大模型（Qwen235B或GPTOSS120B），generator Llama3.2 3B，BLEnD英文MCQ带culture身份、CLIcK文化1345题；不是从用户语言直接取得culture真值。Table3逐步加corpusselection与queryrewrite均有收益，但critic也共同增加，未严格单因果；Table2 caption称GPTOSS而数值对应Qwen有口径冲突，不直接套该归因。Wiki缺证、LLMcritic共错、开放问答/全链成本未证。拟Ch76补“query表达与source域选择两旋钮”最小差额，具体owner/拟文待。
- **25903 CTT，P5**：HTML404后officialPDF实际p3–4/6–8/15–18，§2/3.1/5–7必要段。NAS→prune→quant→KD的次序消融是在600/50/300小样本与moderate压缩上做，表7仅三种顺序，不支持“全六排列已证普遍最优”；clone quant-first latency15.6优于16.0但更占memory。最终KD恢复task accuracy是局部观察，不从N=3跨任务p>.2推等价/无损；低bit训练/算子precision与完整generation预算未充分披露，保Not Disclosed。A10080GB与i7-2600不同设备不能合headline，CodeCarbon估算不是实测碳排，训练与NAS排放未计。原先准入潜力的“顺序改变资源与质量取舍”可保，拟仅报告，非通用green最优pipeline。
- **R-DMesh官网线索纠偏**：实际读完整[官方project](https://r-dmesh.github.io/)题摘/core及[官方repo](https://github.com/Tencent-Hunyuan/R-DMesh)。base mesh/relative trajectories/rectification jump分离及Triflow有潜在长期机制，但当前网页链接的是May论文2605.13838。官方repo API `created_at=2026-04-29T07:36:06Z`只是建库，`/releases?per_page=100`为空；`/commits?per_page=100&page=1`完整44条最早Initial commit `fc2d26a451cbcbff91e6367e42fda0ed57be4dc4`在May6T17:05Z。不能把此前Apr29的repo壳时间写成正文/release公开；当日确有机制正文的资格缺件，终态隔离该资格，不倒灌现时May内容。恢复只需Apr29官方公开正文/可验证archive或公告，不扩扫May论文池；原依据保留。

## A13 每日来源的本窗有限封口（2026-10-16；历史缺层终态隔离）

以下是作者本轮实际入口/停止，不从别日Complete推覆盖。API原始目录仅供身份/日期浏览，不把全列表变成候选队列。八个不可恢复历史子层各只请求Apr29日级官方列表/当时原件；可读目录、定点检索及可用恢复已执行，缺件不授Coverage或无遗漏，不阻塞其它普通Source/Books。

| 来源 | 实际入口与停止点 | Apr29结果与限制 |
| --- | --- | --- |
| OpenAI | Research Index当前九卡Sep/Oct、LoadMore历史未恢复；[News RSS](https://openai.com/news/rss.xml)首次403后UA恢复1296条，按pubDate转BJT筛2条 | [compute infrastructure](https://openai.com/index/building-the-compute-infrastructure-for-the-intelligence-age/)为Stargate容量、选址/能源/合作披露；[cybersecurity](https://openai.com/index/cybersecurity-in-the-intelligence-age/)为五支柱治理行动计划，核心均已读，无新模型/运行时机制或受控成立边界，具体EX。Research Index的Apr29历史层仍隔离，不从RSS/搜索推完整Research零项。 |
| Anthropic | Research当前10卡/SeeMore同页，shell403、历史?page=5失败；official-domain本日主题日期检索 | BioMysteryBench完整题摘/核心为生物实证任务，按AI4Science暂缓EX，原始Apr29显示口径保留但不为已明确EX追首发时刻；不把此EX升格通用评估增量。历史Research未显示层隔离；活动webinar非新研究机制。 |
| Google | [Research April](https://research.google/blog/2026/04/)完整9条Apr29→22→21→16×2→13→9→8→3、无后页；[DeepMind page3](https://deepmind.google/blog/page/3/)May→七April→March，前三篇实际日期30/27/23 | Apr29 [ERA应用](https://research.google/blog/four-ways-google-research-scientists-have-been-using-empirical-research-assistance/)核心为流行病/宇宙学/气候/神经科学的既有Agent应用，AI4Science范围EX；不借Agent词引入。DeepMind可见有序Blog无Apr29；Publications日期过滤/历史目录仍隔离。 |
| Meta | Research首页web0line、shell不可读；恢复[Publications?p2](https://ai.meta.com/results/?content_types%5B0%5D=publication&page=2)实际为Oct2/Sep24→Jul13再混2017–21旧条，不是旧记录所述May→Apr有序段；official-domain日期检索无可读Apr29原件 | 此次p2不足日级邻界，明确隔离Research/publications Apr29历史层，不拿混排或空搜索认零；不沿无关数学条目扩池。 |
| Qwen | [官方article API](https://qwen.ai/api/v2/article/retrieval?type=qwen_ai&language=en-US)实际40条，data.articles[].extra.date；无paging键 | 27B Apr22→FlashQLA Apr28 10:00+08→Scope Apr30 12:00+08，本窗无研究条目。原本日V3 qwen-code0.15.5/PR3729为相同reasoning-replay兼容性事件及Ch84已有承载，仅具名有效层复用，不新评分/搬日期；不推全org历史零发布。 |
| DeepSeek | Research&News可读10研究/5新闻；官方[release sidebar](https://api-docs.deepseek.com/news/news260424/)实际18条，Sep10→Apr24→Dec2025 | 可见release链跨窗无Apr29。Research当前Jun24→Feb25；ViewAll历史交互未恢复，隔离其未显示日级层，不从首页能力回填。 |
| Moonshot | [Platform Blog](https://platform.kimi.com/blog)完整26卡Nov2025→May2024，无2026；原具名kimi-cli1.40事件按已有04-29身份/采用层去重，1.41官方Apr30在窗外 | Blog 2026缺层及未见技术仓库历史公开日级层隔离；不重审原CLI、不把changelog当全org事件表。 |
| Hunyuan | 首查Research超时且浏览器一次超时后从官方JS恢复[POST publicList](https://api.hunyuan.tencent.com/api/blog/publicList)，pageNum1/pageSize100/renderType0完整total9/list9；另renderType1六研究项 | 全部9项公开/显示相邻100039 Apr30与100061显示Apr23；6研究相邻Apr30/Feb13，本窗无可见Research项。publishedAt内部时间不代publicAt；当前目录不证删去历史。RDMesh Apr29建库非正文日期，见A12资格隔离。 |
| ZAI | 官方Research May20→Apr29 ScalingPain→Apr7；release-notes可见June16→Apr7模型邻界 | ScalingPain原34同事件具名审阅/Ch55/54实际POST去重，不新评分/迁归属。未发现本轮新family，不推全仓库零。 |
| Seed | [官方API](https://seed.bytedance.com/api/get_article_list_v2?article_type=1&count=20&order_desc=true&page_token=20)，x-tt-locale:US；research20条/total246/token40，May16→Apr30→Apr26→Apr23→Apr15，实际跨窗停；blog type2/token0/count20实际15条/total96，Jun19→Apr23→Apr9跨窗停 | 两有限可见层无Apr29相关发布；不沿has_more遍历所有246/96。PublishDate毫秒按原口径，不能叫逐篇首公开日志；Research精选与Publications均本轮恢复，不继续标普通未读。 |
| ERNIE | 技术Blog有序May9→Apr30Preview→Apr15→Feb6；原本日release/commit具名层定点复用 | 可见Blog无Apr29研究，不把Apr30榜单/接口文章倒入本窗；原工程兼容实例不重复入选，也不扩全Paddle仓库。 |
| MiMo | Paper8条June29→Mar13→Feb3跨窗；Blog15题无日期/More无历史页；official-domain本日日期主题补检 | 显示Paper无Apr29，Blog无日期历史层隔离；当前V2.5TTS能力/demos无新架构或受控有效条件，为具体EX且无须为EX追月内日期；不以Paper8条认证全部Blog。 |
| MiniMax | EN Blog11与CN current13条实际可读，CNMay25→AgentTeamApr27→Mar18，EN AgentTeamMay27而非Apr27；AgentTech当前3项Oct8/Sep22/Sep19 | 两语言可见层均无Apr29，不把同family目录日期分歧当新事件。AgentTech未显示的Apr29历史层保隔离，不据当前三篇授全历史零。 |
| arXiv | A2/A6十二分类的本窗相关标题与完整题摘、官方批24765–25918；CL失败已由官方月表恢复，LG/CL/CV两页、AI末页、其余单末页 | 原具名已入选/EX/日期hold按A5/A10与R30具体有效层复用；本轮只冻结独立发现、准入和实际必要Source支持的新身份，不将1154 raw ID作全文队列。 |

发现封口后只继续已具名有限Source/owner及日报融合；不会为了补计数量扩类别、跨日大池或恢复无关领域。候选冻结表在后续A14，reader未完的实际层仍是普通工作，不因本节封口当作通过。

## A14 最后两项长期差额的具体owner与PRE（未授不写）

25467的独立reader逐字PRE在R30-8，唯一ROADMAP ID是 `TRAIN-DISTRIBUTED-TRAINING`（不另建TRAINING-DISTRIBUTED节点）。作者实际Ch36 843–895完整局部、Ch35/37开篇交接已读；CPU完整control残差与当前通信坐标的分离是当前basis时效段未具体承载的差额，接受该最小单段，向root申请后才写。

25676唯一owner `AGENT-RAG` / Ch76。作者actual Ch76 79–103完整查询侧相邻段、735–748 evidence权利/成本边界及Ch75/77开篇交接已读。现有三责任层、rewritevariant及支持/竞争检索没有显式把corpus语言/区域scope作为与query独立的在线决策旋钮；不另造culture owner。拟插现“三类改进分别验证”整段后、`Query-side 也有一个容易错位的选择`之前。

逐字PRE：检索域本身也是一个独立旋钮：在错误的语种或区域语料里反复改写query，仍可能只得到主题相关却不适用的证据。一条[受限多语检索分支](https://arxiv.org/pdf/2604.25676v1)让planner分别提出corpus scope与查询表达，再用证据critique决定是否重选语料、改写或停止；同一英文问题可以指向不同地区，因此语言匹配不是culture真值。Corpus选择仍受原权限与来源身份约束，critic给出的相关、适用与充分性分数也不能代替原文支持。作者在13语言Wikipedia与两个文化MCQ任务上给出分步对照，但额外大模型critique/多轮检索未与固定路线严格同预算，最终同为top-5不代表中间成本相等，也未验证开放问答。它支付多索引、scope选择、critique与全部重检索，语料缺证时再改query也无法补出事实；scope含糊、critic共错或收益不足时，保留固定已授权语料、原query/有限多改写及独立原文核验，不让地域标签或自动停止签发正确答案。<!-- source-family:SF-2026-ARXIV-2604-25676 -->

## A15 窗口候选冻结与剩余实际层

发现封口，完整准入和本窗/去重后冻结29家族：24833/24878/24938/24940/24959/25031/25039/25073/25143/25150/25161/25182/25276/25289/25299/25349/25379/25444/25467/25477/25508/25578/25654/25676/25716/25858/25866/25898/25903。候选日期/评分/Books具体入口是[README总表的新增29行](../../30/README.md#候选总表新增29与冻结原34)，不另建第二候选投影。拟5I/3NC/17Only/4D；不把未经actualPOST或剩余独核授完成。

24827新发现官方19PINE-AI/ikp Apr27完整repo/core，历史公开资格未证，保日期Hold而非从争议降EX；与25326/25642/24832/25783四具名hold同样不计正面候选/评分。R-DMesh Apr29建库壳另隔离；24801/25779及24954更早同family公开按A10有效层保留，不倒灌本窗。以上均非隐藏缩池或工作量减分。

25143/25289/25349实际POST/root释放已完成；25467/25676得到root指定单段+本人注窄lease且已实际保存，非writer实际POST待。作者必要Source均已读，reader只余25073/25444/25858/25866/25903有限独核与24827资格核的记录落盘；README六节融合/独立DAY/保存完成态FINAL仍普通，不因来源发现封口写普通0。

## A16 六部分已保存、研究普通0，提交实际DAY

2026-10-16 09:50+08，作者已经将新增29与原34整合进同一六部分：5I/3NC/17Only/4D，全63；新增29必要Source、具体owner/处置、五真实正文/完整两侧/本人注actualPOST均由非writer通过，root接纳并释放全部五窄lease。A15历史停点中的五Source/两POST待办已由R30-9及实际格式有限回读关闭，不再普通；唯一尚待流程为本日报六部分独立DAY与保存完成态FINAL，作者不自签。

机械校验实际：V3通过；`python3 -m unittest scripts.test_report_windows` 42通过（直接运行测试文件的模块路径错误已用正确module入口重跑，不改测试/校验器）；原34完整行各一次、旧窗口一致、原连续§4 19698字符逐字保持；本日报/SUP 137本地引用无missing，README/SUP和五个指定Books的限定diff-check通过。旧来源表加引用边界、候选同一表/逐题同链接标题与冻结日期字段是文档结构修复，不改原34行或旧正文；未改合同、校验器、共享索引/LS，不stage/commit/push。

新增冻结入口现为[候选总表](../../30/README.md#候选总表新增29与冻结原34)；A15旧链接标题行政改用此处，不存在第二候选投影。五arXiv首公开资格、RDMesh建壳、八机构历史层及四中心争议均保各具体补件/重开要求，不授正面覆盖或无遗漏；其它普通执行项为0，准备交reader实际DAY。

## A17 按实际DAY保存完成态（root最小FINAL待读回）

本作者实际读回R30-10完整六项结论，非作者actual DAY通过已发生且root明确接纳。仅行政同步README状态完成、检查时间2026-10-16T09:53:38+08、§1/3/5/6普通0与真实5I、EX六abs/五core抽检及未查范围；五Books本人注均为actualPOST通过/root指定窄lease已释放。29新增=5I/3NC/17Only/4D，与原34合63=25I/4NC/24Only/10D。没有重Source或自签DAY。

完成态保存后作者实际最小读回/机械校验通过：状态/09:53:38/补充窗/冻结原档案字段正确，V3与42测试通过、63行及新增5I/3NC/17Only/4D正确、原34各一次/旧窗/19698字符连续§4保持、README/SUP最新138本地引用零missing、七文件限定cached/unstaged diff-check通过。root随后仅核字段、原34/旧窗/连续原§4保护、引用和格式FINAL，不预支其结果。来源历史、五arXiv首公开/RDMesh资格及四争议保持具体终态请求，不转正面Coverage或Books；不stage/commit/push、不写共享索引/LS，完成后本日ownership释放，由root决定fresh下一日。

## A18 root保存完成态实际最小FINAL通过，本日释放

root实际最小FINAL已通过：状态完成、检查时间09:53:38+08；原34整行各一次、原小时窗口不变、连续原§4逐字包含（root按rstrip测19695字符，作者含原段尾空白测19698，同一冻结正文）；新增29=5I/3NC/17Only/4D，总63。README128+SUP10本地目标均存在、fences成对；V3、42窗口测试及七文件cached/unstaged diff-check实际通过。root接纳R30-10语义和五真实POST，不重Source，未对外部隔离授正面证据。

本作者仅将上述真实FINAL行政同步§6并实际读回，不修改准入/证据/Books语义。本日普通0、全部五Books窄lease与作者ownership释放，root负责总checkpoint（120/279）及fresh下一日分配；本lane不自行跨日、不stage/commit/push、不改共享索引/LEARNING_STATE或并发内容。

## R30-1 独立reader范围及具体有效层复用（进行中）

复核者：supp_apr30_review_fresh，非作者。完整重载本日AGENTS、Research合同、Report V3、Prompt、Sources使用说明/每日组/arXiv主题和ROADMAP；LS仅取本日路由。Books上下文PROJECT_CONTEXT/PHILOSOPHY/WRITING亦已读。只处理Apr29自然日来源补充，原34行、旧窗和连续原§4不动；不写README、Books、共享索引或LS。作者只改A区，reader独占R30区。普通可执行发现/审阅/owner/PRE/POST/DAY尚在进行，以下不授日级完成。

- `25359v1`：定点读04-29 `V3_SOB_25359_REVERSE_ADMISSION.md`及非作者`V3_APR28_FINITE_SOURCE_OWNER_REVIEW.md`的109行，身份/版本、OCR-markdown/transcript测量对象、schema与value分账、样本/长度混杂、无原生感知权限和重开条件均与本轮A8匹配。现Ch66“五种成功事件”、artifact转换/视觉读取分责及实际音频/转录人口，Ch51合法span≠语义，仍承载拟采用原则；无新的受控反证。故复用具体必要Source→actual-owner前闭，不因本次初步P5硬造候选/Books差额；不是只以旧Complete或主题类似认EX。
- `24964v1`：actual完整abs-v1和HTML-v1入口核对后，定点复用04-29 `V3_REOPEN_NOTES.md`“贡献反向准入：2604.24964v1”及同非作者记录109行。rubric对人κ=.788 vs轨迹.508、LLM-call而非匹配actions成本、live网页漂移都已具名限定；Ch66实际checkpoint-specific assertions、rubric formation/execution和预算分账仍承载拟命题。本轮没有新增条件改变旧具体关闭，不重读全部附件、不再评分。
- `25809v1`：定点复用04-29 `V3_REOPEN_NOTES.md`对应具名段与独立记录111行，核同VLM/同图两prompt、KL门、双forward成本及coverage反退仍匹配。实际Ch23双路径段明确共同视觉偏差、gate非事实置信度、冲突回原图/拒答。故旧前闭有效，不把“evidence”名称授独立oracle，也不把局部CHAIR增益升格新知识。
- `25578v1`：旧`V3_MARCOMOE_25578_REVERSE_ADMISSION.md`与独立记录108行可复用fine-grained/Drop-Upcycling、语言频率非因果和额外1.4T训练混杂等层；本轮新增具体SiLU齐次性信号不在该链闭合范围，单独窄核，不推倒其它有效层。

## R30-2 首批必要Source的实际独核停点（进行中）

除25150受影响保证外，本批仅采用下列必要位置支持的有限命题，不称全文/复现完成。评分是初筛的命题投入，不由Books差额倒推。

- [24938v1](https://arxiv.org/html/2604.24938v1)：§3–5/Tables1–3实际核；P5保标准完成。三个8B模型、两数据/目标、七搜索的排序差异能反对普遍无用层，但C4与Commonsense170k同时变化，不隔离纯loss因果；不能把search仅1–3点写成所有设置，Qwen3 M9同目标可差7点并有灾难失败。实际Ch17“Layer冗余取决于干预协议”417–419已绑定checkpoint/操作/数据/evaluator和剪后完整回归，Ch49 595–597又有calibration-loss改变importance的具体实现，故Books已有覆盖，不另写。
- [24940v1](https://arxiv.org/html/2604.24940v1)：§3.2–3.6/§4.2–5.4/AppD实际核；P5保受限替代接口，标准完成仅报告。shared-codebook/anchor-expanded attention/组位置不是低成本普通embedding的同义词；正文sparse index-gather与后文flattened E[i]materialization未闭，不授两者同样内存省。98.7%参数降主要来自替换12层encoder，独立KD费用仍在，Table6实际比DeBERTa更慢；GPE无独立消融，仅两个classification不证LLM生成扩展，故不新增通用多义性/压缩保证。
- [25031v1](https://arxiv.org/html/2604.25031v1)：§3–4/Alg1、§7.1–7.5/Table1–2实际核；P5标准完成，仅报告AGENT-REFLECTION。roundtrip等价仅formal self-consistency，原语义可能已在T1丢掉；NLI抽核也有false positive，反复repair不能补schema缺predicate，三次预算耗尽不授faithfulness。实际Ch80 80–88已有translation/fidelity与solver分账、scoped regeneration和原检验义务保留；本篇150交通规则只支持有界stage-repair实例，不把局部UNSAT改善当新安全保证。
- [25143v1](https://arxiv.org/html/2604.25143v1)：§2–5/Tables2/4/5实际核；P6深入，梯度/AdamW更新及按task分解是不同测量对象；投影梯度在moments前与投影step在moments后不等。Table5仅modular-addition三seed，不能据摘要扩成所有操作的gradient-projection；随机rank3同样加速，不授SED唯一因果。实际Ch4 100–120已有局部gradient/optimizer与坐标预条件，却未承载per-task diagnostic与moments位置，下面给最小PRE。
- [25289v1](https://arxiv.org/html/2604.25289v1)：§2.1–2.4/Alg1–2、§3/Tables2–3实际核；P7深入。线性低维流形/高维shell仅条件近似，Gaussian support不真正disjoint；正交位移把time编码进input，不是删除所有time信息。Table2显式t的FID仍更好，spacing过大退步，不声称普遍time-free优胜或通用理论证书。Ch24现165–175噪声合同/几何/日程段未解释implicit-time与path共同设计，下面给窄PRE。
- [25299v1](https://arxiv.org/html/2604.25299v1)：§3.1–3.3/§4.1–4.3/Tables1–3实际核；P5标准完成，仅报告MULTIMODAL-GENERATIVE-PARADIGMS。中间循环只让LoRA branch递归，最后才合frozen base，而非每轮full frozen block；text不递归。新增训练、模块和循环均付费，ImageNet设置1024与Table1的256须分开，GenEval position与DPG有反退，PCA路由图不证reasoning/专家语义。此为受限inner-compute配方，不由“递归”自动授长期reasoning机制。
- [25349v1](https://arxiv.org/html/2604.25349v1)：§2.3–2.5、§3.1–3.3/Tables4–5及§4.1实际核；P6深入。检验H0均值差=0与signed-rank所需差值对称性不是同一条件；zero-mean asymmetric模拟可随n增大高拒绝。TREC只是校准偏态/尾部范围，未把53,703共享system pairs当独立重复；t-test也在小n/极偏态下失准，permutation/bootstrap未在本篇同样验证，不采“总用t”或“W检验一律无效”。Ch66现非参数estimand段未交代该具体null/shape失配，下面给窄PRE。

## R30-3 已源核与actual-owner核的有限PRE（待作者确认及root段lease，reader不写Books）

### 25143 → WORLDVIEW-WHY-MODELS-LEARN / Ch4

插槽：现“负梯度是局部下降方向”之后、“同一个函数还可以有不同参数坐标”之前。前者说明更新构成，后者转坐标度量；新段只补测量对象，不重复模型表示章节。

拟文：观察训练方向时，还要把当前loss的梯度、多个任务梯度的聚合和优化器最终step分别保存。Momentum、自适应缩放与weight decay会过滤方向；混合任务又可能彼此抵消，因此从最终更新的低秩结构反推“特征在哪里形成”，可能漏掉仍在各任务梯度中的信号。一个[受限模块算术诊断](https://arxiv.org/html/2604.25143v1)比较rolling SVD的这些输入，并在干预时区分先投影gradient再更新moments、与优化器先看完整gradient再投影step；这两条路径不是同一因果实验。随机rank-3约束也能达到相近加速，所以高方向耦合只是诊断，不证明那条子空间是学习必经之路。按任务求梯度、存窗口及成对投影增加计算与状态，toy任务/少量seed不提供LLM训练配方；诊断失配时保留原优化器、原始gradient/step与held-out质量，不按一个谱值删除更新方向。<!-- source-family:SF-2026-ARXIV-2604-25143 -->

### 25289 → MULTIMODAL-GENERATIVE-PARADIGMS / Ch24

插槽：DDPM简化loss后“噪声schedule、时间采样和预测参数化共同定义目标”之后、现“改用latent还须重新验这条加噪合同”之前。

拟文：显式把时刻交给denoiser，是同一noisy输入可能对应不同去噪目标时最直接的消歧方法，却不是time信息唯一的编码位置。一个[受限time-unconditional分支](https://arxiv.org/html/2604.25289v1)联合重训forward path与denoiser：调整噪声半径日程，使有限相邻时刻的典型高维区域更易区分；或把time位移放进近似正交方向，让输入几何携带时钟。后者仍编码time，不能称模型完全不知道时刻；线性低维流形和shell集中分析也不使Gaussian分布的support严格互斥。作者DDIM图像对照支持这一替代接口，但小图任务显式time embedding仍有更好FID，间距太大也退步。它支付日程/表示共同训练、几何校准与完整生成回归的费用，不是部署时直接拔掉time embedding；目标含糊、数据几何或质量预算失配时，保留原显式time、既有forward path与sampler。<!-- source-family:SF-2026-ARXIV-2604-25289 -->

### 25349 → PLATFORM-EVALUATION-SYSTEM / Ch66

插槽：现“非参数检验还需明确其估计的是排序概率、位置差还是组内秩”之后、“若预测与人工结合的权重也由少量标签估计”之前；读回完整相邻段后接统计推断校准主线。

拟文：选用signed-rank检验前，还要区分要检验的均值差与差值分布的形状。对于配对任务，分析对象是每题两系统得分之差D，而不是分别要求两列score正态；Wilcoxon signed-rank的常用零分布依赖D在零附近对称，均值为零本身并不满足这项条件。[IR范围的模拟与TREC校准](https://arxiv.org/html/2604.25349v1)展示了zero-mean却偏态时拒绝率可随样本增加而升高，因此“非正态就换非参数”不能作为自动规则。这不使t-test普遍可靠：小样本、极端偏态、相关任务及重复比较仍须各验假设，也不从该篇推导bootstrap或permutation已获同样保证。应冻结配对单位、目标统计量、零值/tie规则与采样结构，支付诊断、重采样或独立复核成本；条件不足时报告描述性差异、宽区间或Unknown，不由检验名称发布显著改进。<!-- source-family:SF-2026-ARXIV-2604-25349 -->

## R30-4 追加core校准与安全反证

- `25161v1`最终Books：已有覆盖PLATFORM-EVALUATION-SYSTEM，实际Ch66多解释诊断段494–504已有“共识不证干预成功”、配对执行验证、oracle共错、局部continuation非全局因果和Unknown。P5的CanTest受限oracle-repair实例并未独立校准唯一根因，不新增重复段。`24938v1`最终Books已有覆盖MODEL-TRANSFORMER-LAYER，具体位置见R30-2；`24940/25031/25299`按R30-2受限命题标准完成/仅报告，不因该处置降分。
- [25039v1](https://arxiv.org/html/2604.25039v1)：完整abs与§6.2/6.4/§7必要预算对照核，P5标准/仅报告AGENT-REFLECTION。accepted重复与low-score指纹两类缓存可减少valuator调用，embedding相似误拒不同数值、50题/小差额和近似tokens限制；重试耗尽强行accept不是verification。没有把局部cache称可靠推理或新独立truth。
- [25136v1](https://arxiv.org/html/2604.25136v1)：完整abs、§5–6核心friction框架及§8–9读，具体EX：将成熟reward shaping/DPO/group-relative/TRPO套入启发式friction，§9仍把surrogate失配与empirical verification列未决，没有新稳定条件/反证。不是仅因无大实验拒；A7的“§10”应为actual-v1 §9。
- [25182v1](https://arxiv.org/html/2604.25182v1)：完整abs、Alg1/§2.1–2.3与§3必要消融核，P5标准/仅报告AGENT-RAG。实际按query语言→全语→English的预定turn顺序，KnowledgeNorm是翻译而非独立证据；character-3-recall可被冗长答案利用，不认证语义正确。c3Reward移除影响大，不把全部增益归语言路由，四语/3B7B局部不证普遍防噪。
- [25276v1](https://arxiv.org/html/2604.25276v1)：完整abs、§3.1、§4.1–4.3/Table4与§5.1实际核，P5标准/仅报告MULTIMODAL-REPRESENTATION。caption-centric标注与direct grounding能力不等，标注后人工修边；content-aware相对rule-based仅局部收益，SFT主收益与额外CoT/RL训练不能混为唯一reflection因果。词频定义rare、同分布自家测试和四外部VTG不同人口，规模本身不作准入理由。
- [25313v1](https://arxiv.org/html/2604.25313v1)：完整abs、§3.5–3.6/§7–8读，EX：typed entity字符串替换与存在性过滤的规模化resource，无coref/NLI、无被测模型的parametric conflict确认或下游结果；200抽样四自动检查全过不证语义正确。不把资源无实测误作论文无价值。
- [25427v1](https://arxiv.org/html/2604.25427v1)：完整abs、§3.2–3.3与§4.1必要核，EX：实际采用既有Flash/Mix/DanceGRPO、RePrompt、DMD/causal/self-forcing，并未隔离本框架新失效边界；internal-model评估和未披露预算不采用宣传普遍稳定。没有只由摘要的“novel”或四阶段词汇准入。
- [25578v1](https://arxiv.org/html/2604.25578v1)：actual §2.1–2.2/Fig5窄反核：SwiGLU的SiLU不正齐次，同时缩三矩阵λ=N^(1/3)不严格等价输出乘N。均匀gate、N=8，取一个非零标量分片gate/up/down输入均1、其它分片零，缩后平均为4·SiLU(2)/8≈.8808，原dense的对应分片为SiLU(1)≈.7311。保Fig5受限loss-spike改善，但不采“数学等价”保证；纠错保护性恢复为P6深入争议/暂缓，不Books，不重复旧语言route层。重开需精确缩放实现或只缩线性分支的等价修补及相同初始化对照。
- [25379v1](https://arxiv.org/html/2604.25379v1)：actual §4.1–4.2/Prop2/Eq3–8窄独核作者反侧通过。tildeπ_b=(1−η)π_b+η/|A|与π*∝tildeπ_b exp(Q/λ)在有限Q时使unsafe action有正概率；target-only smoothing不证明extracted policy不出support。Gaussian/tanh的valid action range≠safe successor，模仿safe dataset也不授零unsafe。受限行为收集/样本观察可保，不采用硬安全保证；不因此否定全部KL-control/实证。必要保证隔离不Books，恢复需真正safe support参数化/执行shield及训练collector与最终policy分账。

## R30-5 三窄段actual POST

root授段lease后，非writer reader已逐字读取Ch4 110–126与本人注470，Ch24 161–180与本人注2928，Ch66 532–549与本人注6461（行号随并发变动，以source-family定位）。三段均与R30-3 PRE一致，前后论证由更新→诊断→坐标、噪声合同→时钟可辨性→latent几何、统计对象→signed-rank条件→权重不确定性自然交接；反证、费用与旧路线在正文。语义POST通过，不将marker或作者自读当独核。仅要求Ch4/24段前后统一单空行；作者按此有限排版修复、更新本人注后可释放lease，不授DAY。

- [25161v1 CanTest](https://arxiv.org/html/2604.25161v1)：完整abs及§4.2–4.3、§5.1–5.3/Table2、A4实际读。P5准入可保：改变的是oracle输出替换并重跑后继轨迹的定位机制，而非仅新增任务集合。RAM/LLM语义对齐、全局地图规划是privileged/有噪声oracle；“earliest individually repairable”是具体归因规则，不是唯一真实根因。§5.2以repair率证明oracle可靠，不能替代独立标签校准，尤其failure-inducing本身按repair成功选。保三模型Habitat3受限发现数及修复观察，不推生产安全；Eq7零计数初始化和reroll随机性未明确。待actual Ch66/26差额比较。
- [25150v1 symmetry](https://arxiv.org/html/2604.25150v1)：完整abs及§3.3–3.4、§5.2–5.4、§6–7/§9–10必要段实际读；函数等价扩展改变优化几何的潜力可保P6，但中心Thm5.3不可正面采用。其证明称B semi-orthogonal，而同文K=BBᵀ=diag(m,1/m,1)一般不是I；直接取其Eq8/10的H=diag(100,1)、m=2，非零谱为200与.5，越过原谱100与1。此为印刷一般interlacing命题的内部反例，不据此否定全部局部实验或存在性分析。§7亦承认无普遍改善，§10不证明GD收敛至该minima；修订标签不替代精确v1。需隔离该定理/可达性保证，待作者拟采用窄命题及actual owner。

## R30-6 下界/主分类批的准入与有限必要Source独核

本节均已实际打开完整官方abs-v1，并只续读所列必要core；不是题名表扫过或全文完成。上述重复身份不另计候选。

- `24827v1` IKP：§3.1–3.4/§4.1–4.4/§6.2/§7.6–7.7；P6深入争议/暂缓，不Books。经验bits/parameter不是自然事实不可压缩性的证明，也不能据此取得实际权重容量下界；按landmark答对层筛probe、删除非单调题后再回归同类landmark，不能把构造出的单调性当独立泛化证明，LOO亦不解除probe选择。refusal、retrieval、代际和题目覆盖会影响effective proxy；保受限知识probe观察，隔离实际参数/数学下界的强解释。
- `24878v1`：Def3.3–3.4、Lemma4.1/Thm4.1与practicality；P6标准/仅报告WORLDVIEW-WHY-MODELS-LEARN。attention-only构造还需零token/preprocess、随目标ReLU网络变化的层/头与精度，inverse-temperature可随深度和误差急增；存在性构造不是SGD可达或有限精度部署效率。此为明确资源边界实例，不把“Transformer近似一切”当新通用原则。
- `24959v1`：§3.1–3.3/§4/§5必要设计；P6标准/仅报告MULTIMODAL-GENERATIVE-PARADIGMS。固定共享row/column子空间后仅core作flow，生成误差分成几何、core流与不可约近似；人口模型假设共享子空间、二阶矩和全局velocity误差/密度正则，不是训练CNF有限样本或缺失观测恢复保证，§4明确后者未来。Solar300张与LSPF8760、随机missingness不支持任意高维数据，缺低秩时patchification本身改变表示与费用。
- `24833v1`：§5–6/§7.4/§8.1；P5标准/仅报告ROBOT-WORLD-MODEL。root/timing与pose、primitive调控及低层tracking是具体分层接口；Jetson约5ms与desktop约2ms/并行15000FPS不能合并。sim中的object/terrain特权信息在real不可得会关闭primitive，self-collision/flip和离线retarget仍在；不授硬安全/零准备实时生成。
- `25130v1`：Alg1、III.C–D/TableII–III；EX。双向QA answerability/consistency、ROUGE匹配再self-refine属于成熟QA评价反馈组合，未提供独立新失效边界；同QA模型重评自修后分数，不能自证summary真值。不是仅因benchmark规模拒。
- `25654v1`：§3–5/Table1；P5标准/仅报告PLATFORM-EVALUATION-SYSTEM。明确Portugal cue会改变测量对象，spontaneous与cued须分开；新旧culture数据的难度未匹配，substring/64token/量化/闭源backend都限制解释。Ch66实际cue/no-cue及propensity-vs-ability已有具体责任，不扩为真实文化认同或能力上限。
- `25904v1`：主文动态重建、generalized-Bayes/Louis identity与Lorenz QoI必要core；EX。受限chaotic-surrogate上的forced与marginal likelihood曲率比较沿已有方法，未建立可迁移到本书模型训练/系统选择的新条件；不是因无LLM或应用领域而拒。保该范围，不借WorldModel主题自动准入。

## R30-7 后批必要源与安全/归因反侧

- `25477v1`：actual III-C/IV-C与TableVI，P5标准/仅报告RLHF-GRPO。两reward使用独立rollout/minibatch并各自归一是实在实现，不是先加权scalar；sampling ratio仍为隐式权重，cognitive只评answer-plan、judge非真值。Ch33实际110–140已有独立人口/归一后混合与同θ竞争；37.5→40.0为固定editor局部对照，不重复造书。
- `25716v1`：actual方法及Tables1–5，P5标准/仅报告SECURITY。Table2逐语言validation下FPR≤1%的工作点，与英文校准global .66是不同口径；多样unsafe的个位数recall反例可保，不把它误说成所有英文阈值跨语结果。翻译无人工postedit、模板/OOD、survivor条件ASR与AUC口径冲突保留，不采通用防护保证。
- `25898v1`：actual方法/affinity、Table2与限制，P5标准/Books已有覆盖RLHF-CONTINUAL-LEARNING。Ch30实际820–857已有reuse/expand/freeze、task身份、proxy与capacity/routing回归责任。task-ID和norm/actiondim是额外输入，Panda .670需3copy，replay .729仅1copy，hybrid1.546；旧expert冻结不授所有任务/无成本zero forgetting。
- `25508v1`：actual§5.3 Eq17、AppendixB.2 LemmaB3/Eq28–29及D.1，P6深入争议/暂缓，不Books。Eq29最后一步把E[γ^T]替换γ^{E[T]}，对随机T不成立；γ=.5且T等概率0或2，log_.5(.625)≈.6781≠1。故Q最多给折现moment对应的确定性等价时间，不直接给平均failure-time。E是模型certain-domain非physicalsafe，30k/4M prior数据及pretraining不计入主图的生命周期成本另列；保toy任务过滤/控制实证，不因此否定全篇实验。
- `25467v1`：actual§3机制/§4.1与Thm1/§5.2–5.4；P6深入。投影通信与full-space model/control CPU残差保留是不同状态，换基后不能只旋转短control并称信息保持；每轮重建ambient model且算full gradient，不采§3.7按r减少gradient计算。理论step与误差显依ρ，ResNet110最终45.43对full52.92且非equal-compute，不授质量等价/唯一残差因果；Ch36当前879–881有basis身份和通信残差但缺control补回，给下面单段PRE。

## R30-8 25467 → TRAIN-DISTRIBUTED-TRAINING 单段PRE

插槽：Ch36现“联邦更新相关性的有限对照”整段后、“矩阵耦合 Optimizer 必须把更新本身变成 Distributed Operation”标题前。已有段解释basis时效，新增段只补heterogeneity correction的状态所有权。

拟文：联邦训练若还用control variate校正client drift，低维通信不应同时删掉完整校正状态。[一条受限随机子空间分支](https://arxiv.org/html/2604.25467v1)让各client共享同轮正交投影，只交换短坐标，却在CPU保留model与control的正交残差；换基时先从完整状态重新投影，再只更新当前子空间，未覆盖分量继续保留。这与反复旋转仅剩的低维control不同，也不意味着local gradient只需在低维计算：该方法仍重建ambient model并计算完整梯度。它支付CPU状态、投影/回填、跨设备访问与质量回归，理论步长和误差又依赖r/d；CIFAR-100对照仍弱于full SCAFFOLD，且非严格同compute，不能叫无损或把所有差额归于残差。应共同保存projector seed/revision、完整control与model残差及round身份，比较达到目标质量的总通信和时间；状态无法对齐、投影太窄或净收益不足时，保留full correction、dense updates或已有验证的压缩方案。<!-- source-family:SF-2026-ARXIV-2604-25467 -->

## R30-9 余项有限独核、最终身份纠偏与两段POST

R30-6/7的路由缩写仅为主题，正式Stable ID以ROADMAP为准：24833→`MULTIMODAL-EMBODIED-VLA`、25477→`TRAIN-GRPO`、25716→`PLATFORM-SECURITY`、25898→`TRAIN-LORA`。不创建ROBOT-WORLD-MODEL、RLHF-GRPO、SECURITY或CONTINUAL新节点。

- `25073v1`：actual §6.2/6.6–6.8、§8.3/§9.3–9.4；P5标准/仅报告INFER-TENSORRT-LLM。feasible-first再TPE、可恢复blacklist是有界搜索分支；timeout同用全部optimizer。actualTable5/6/8/9支持结构发现与invalid费用而非平均准确率统治，.761≈random.762、waste42%对TPE36%；其它GPU并非严格独占最佳。现Ch49搜索/合法性/目标硬件测量及完整费用链可容纳此实例，但无新的普遍停止或最优性条件，不为局部SA/TPE配方造书。
- `25444v1`：actual §3.1–3.3、§4.3–4.4/Table6及limitations；P5标准/仅报告AGENT-PROMPT。全错换强solver、全对换弱solver改变的是训练反馈密度，PPL差只作leak proxy；受限小Qwen池/数学可核答案不能认证通用reasoning trigger、零漏答案或O(1)完整费用。Ch74实际138–146已分设计信号/采样噪声、固定solver/population及query-level选择policy；本篇独立refiner与ASH是受限实现，不新增长期权限。
- `25858v1`：actual §2.1–2.3、§3.1–3.3/§4必要口径；P6标准/仅报告WORLDVIEW-WHY-MODELS-LEARN。主扫描是Gaussian任务上单learnable矩阵分类器，clean新query与noisy context自身分类分账；固定R与dimension-scaled SNR会改变信息量。本文曲线不支持全Transformer或任意d终达1，也不从三seed/best-validation造精确阈值；保有限诊断不造ICL通用recipe。
- `25866v1`：actual §3–6/Table1–3及limitations；P5标准/仅报告MODEL-FFN。feature ablation后logit/后层响应与稀疏乘法steering具有所测功能影响，但六label分类不认证真实情绪理解或唯一自然回路。Table2有少数emotion/domain较弱，Gemma9B PPL13.25→14.51不作“语言无损”；Ch16实际245–282分probe、activation与生成对象及无关能力回归，有限情绪路径不另扩应用owner。
- `25903v1`：actual officialPDF §5.1–5.2/Table7、主结果Table2–5、§6–7；P5标准/仅报告INFER-TENSORRT-LLM。只采用顺序与完整质量/资源共同验收：Table7仅三顺序、小样本moderate设置，quant-first clone latency还略优；主pass@1亦明显下降。KD局部恢复不证通用无损，N=3的非显著差异不证等价；CodeCarbon proxy及缺NAS/训练排放不作真实全生命周期碳排。该实例不改变现有压缩链的长期责任。
- `25676v1`：actual officialPDF §3/4.3、Table3、Limitations；P5因实际owner差额深入，A14中文PRE通过。actualCh76三责任层/variant完整邻接、证据语言与access-rights段对照后，确认query表达与corpus scope两旋钮当前未具体承载；只采用有限控制接口，不采Table2归因冲突或文化真值。

**24827日期层纠偏：** exact-v1实际指向[作者repo](https://github.com/19PINE-AI/ikp)。官方API读取created_at=`2026-04-27T15:57:55Z`，完整39条commits最早`912a9628a66d23f1a07b6de7b17056f2804ced51`为Apr27T15:57:03Z；该commit树与README实际已有同题、1400probe、89model/R².917估参核心及paper/main.pdf，不是空壳。commit/建库不证当时public，因此不以Apr29赋号覆盖此相反身份线索：从确定当窗P6D移为日期Hold，不计本窗候选/Books；R30-6内容反证保留，亦不搬去Apr28。恢复只需该commit/正文历史公开archive或平台public日志、或可信更早正式发布证据，定点重开本family日期层。

**两窄段actual POST：** root授lease、作者保存后，reader实际读Ch36 875–892/本人注2282与Ch76 76–94/本人注1866：新正文分别逐字等于R30-8与A14，完整前后从basis时效→control状态→distributed optimizer、三责任层→corpus scope→query variant自然衔接，必要反侧/费用/旧路线均近文，语义POST通过。仅要求恢复被挪走的下一标题/段落空行，作者有限修复并同步注即可释放，不重复Source。不授DAY；尚待六部分实际读回。

**明确EX分层样本：** 本轮另actual完整abs检查25358（exactv1入口cache-miss后同官方版本页恢复）、25853、24785、24814、25702、25096共6项：分别覆盖layout benchmark、图正则配方、edge硬件榜、code MCQ、DPO翻译配方与human-dialogue拟合；具体EX理由与A6/A9匹配，没有从题名或低分排除，也不从latent拟合作临床因果结论。连同R30-4四项core EX、root A5两项和精确旧层复用构成分层复核，不冒称所有EX逐篇全文；其余无纠错/安全修订信号的明确EX未逐一重读。日期/安全强保证有信号项则均在具名层窄核，不由抽样代替。

## R30-10 非作者 actual DAY（2026-10-16；通过）

复核者：`supp_apr30_review_fresh`，非README/Books作者。作者确认发现、筛选、必要Source/owner和五处写入无普通待办后，reader实际逐段读回当前六部分；不是以原完成声明、作者A16或validator替代语义审阅。前述进行中状态是相应时点停点，本节为本轮最终日级判断。

1. **窗口与发现范围。** 原小时窗/34原行的日期、评分和处置不迁移；补充仅Apr29完整自然日。核A2/A6/A13与实际目录停止及十二arXiv主题分类，24765–25918仅有界公告批合证，不以Submitted截起点、不把1154库存作逐篇队列。十四每日源均有实际入口/有限停止；reader另actual抽核Google April完整9项、Qwen API40、Seed type1的20/246/token40及BJT Apr30→26→23、Hunyuan publicList9项的可见层，与本日记录相符。未扩周源/旧Weekly或其它日期大池。
2. **准入、日期与去重。** 当前新增唯一29、原34合63；新增处置5整合/3已有覆盖/17仅报告/4争议一致。24827从内容P6D恢复到日期Hold后不计当窗评分，连同24832/25326/25642/25783及R-DMesh均在§5给身份、所缺历史public/正文、不能采用的原因与定点恢复条件。确有更早公开的24801/25779/24954不倒灌。33旧候选命中只作身份路由，各具体EX/未变必要层按R30-1/A10有效复用；25578只恢复旧链未闭合的SiLU等函数命题，未重评分其它旧EX。
3. **全部新增与负侧。** 29新增逐项已实际完成必要原始Source/关键反证和具体Books判断，见R30-2/4/6/7/9，不称复现或全部附件全文。四争议均具内部有限反例、保局部观察并隔离强保证；数学与安全信号未被一般EX理由遮住。明确EX分层实际样本为6个完整abs（25358/25853/24785/24814/25702/25096）和5个必要core（25136/25313/25427/25130/25904），另root A5独核25110/24826及定点旧有效层；纠正R30-9“四项core”的笔误，实际上述五项。其余明确无新纠错/安全/重要修订信号的EX没有逐项独立全文，不能把抽样讲作全量。机构样本另读OpenAI Apr29两篇核心与Anthropic BioMysteryBench范围，治理/容量披露和AI4Science不借主题入选。
4. **Books实际落实。** 当前ROADMAP唯一owner匹配；3已有覆盖以actual正文而非主题相似关闭。25143/25289/25349/25467/25676五个最小中文PRE、必要原源与完整前后邻接已独核，root授窄lease后作者实际写入，reader非writer actual POST全部通过。Ch4/24与后两段空行已有限读回、本人注亦匹配，root已释放；没有仅凭marker或作者自读授整合。费用、反例和旧路线近正文，不把实验范围升级为真实安全/SLO或唯一因果。
5. **六部分与终态保留。** 结论/来源表/63行候选/原连续§4加29新增证据/分窗缺口/复核的归属一致。八历史子层清楚保留未恢复范围，不支撑Coverage通过或无遗漏；日期与四中心争议均不用于正面证据或Books，后续材料只重开该层。原窗口的旧限制与旧验收有显式范围提示，不混作本轮完成。研究普通可执行项为0，剩完成态同步与root最小FINAL是行政保存/确认，不是未做的Source或Books工作。
6. **机械边界。** reader实际对baseline逐字比较原34整行（含全部日期/评分）和完整连续原§4均无差异；小时窗仍原值。候选两段间断表空行已删除并actual读回，不改原行文本；五Books新段分隔已读回。当前V3校验与限定七文件diffcheck通过，均不替代上述语义；本地137引用/42tests为作者A16机器结果，root可在完成态最小重验。Reader只修改本日SUP的R30区域，无README/Books/LS/共享索引写入，无stage/commit/push，保护此前dirty/staged/2025内容。

**结论：通过。** 本轮可据此同步README完成态和§6实际结论，再由root只做冻结保护、validator及保存后最小FINAL读回。这里的通过是有边界的日级工作完成，不是对隔离材料、机构全历史或论文所有保证的证明；未运行artifact、未复现实验。
