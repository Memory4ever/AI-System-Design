# Nov19 本轮有界arxiv标题／题摘分批校准

## 1. 本日真实入口与第一批实际范围

五个非legacy官方Advanced请求均已返回200并保存SUP_arxiv-{model,gpu,agent,vision,world}_20261015.raw/headers/request。标题字段分别language model、GPU、agent、vision-language、world model；original-submitted Nov17–18只是发现邻域，非Nov18公开证明。size50/orderannouncedfirst，五页真实heading **41/1/35/12/3**，各短页、无Next；五页实际CS checkbox checked。92次返回去重**78身份**，与本日原18论文只Live-SWE13646/WebCoach12997两重合，**76新身份**；不搬邻日报池，不把78称当天新论文或全类召回。相关标题实际已逐一浏览；下一只相关/含糊完整AB，明确领域项可简记后停，不全分类/全年闭队列。

现有parse_discovery.py实际抽取完整abstract-full并保存各raw.extracted.json，去重身份/题摘见SUP_ARXIV_UNIQUE_20261015.json；抽取本身不等语义阅读。旧parser metadata误取More链接，不用它授日期；官方原li的Submitted/originally announced另按实际字段读。原始ID/原href配对，不跨月拼短ID。旧两重合仅按身份/版本/命题核复用，不默认current全文同旧v1。

## 2. 第一批14份完整题摘实际已读／准入提案

作者本次实际读13份指定完整AB（含abstract-full末尾Less UI残片，不截摘要）以及读取原HTML定位metadata时出现的02024完整AB，共14。不是全78 AB；公开日、当前精确版/说明、必要决定门与标准/深入采用层分别另责。暂**8窄P＋2必要决定门＋4C**，不评分或宣正式新增。

| 身份 | 原约束→实际增量→待核选择／反侧 |
| --- | --- |
| 2512.00045 RTL-to-spec | 生成spec难评价→提出faithfulness metrics及prompt比较→是否给新的可验证规格错误/测量盲点而非IC文档应用；必要决定门，只需指标/对照定义。不是因小实验/硬件领域关；原元字段December公告另责，不由ID或Submitted给Nov18 |
| 2511.21708 LostPipeline | 数据profiling/cleaning比较和user-study质量模型，原AB未指出新的模型消费条件、执行失效边界或足以改变设计的测量混杂；C，不因benchmark/应用标签自动关，不采LLM可替代工具普效 |
| 2511.17599 ProjectionPrediction | B×S×V logits中间态占存储/带宽→投影和loss同算直接消费hidden/target→训练算子边界/活跃内存选择；窄P，只机制和必要资源协议，不以摘要加速/无损宣传采用 |
| 2511.17593 vLLM-TGI | serving选择受concurrency/latency目标影响→high-concurrency throughput与single-user tail反侧→比较协议或负载边界可修正框架一刀切判断；窄P，不采24×或由PagedAttention单因果，需必要模型/版本/配置/预算资格 |
| 2511.14813 DEVAL | 认识输入变化规则不等能相应修改输出→DR recognition/application分开、变换关系评价→推理测量对象；窄P，不采15.2%普效或prompt本身因果 |
| 2511.14120 MP-PVIR | 四阶段交通事件phase/multiview诊断+报告及领域指标，未显示改变基础模型形成/执行选择的独立新资格，C；不把生成因果链当因果识别/真实安全，也不因交通domain单独关 |
| 2511.14101 APD-Agents | 角色组合/模板检索与递归component生成→是否真正约束跨页/层级布局一致性还是设计recipe；必要决定门，仅递归控制/约束及对应证据域。角色数/SOTA不足准入，不因已有Agent原理直接关 |
| 2511.14086 DEER-3D | language训练偏置留下空间predicate错误→最小predicate-aligned scene edit生成counterfactual QA再训→训练监督针对具体grounding失败；窄P，不授4–6%普适或编辑即真实空间oracle |
| 2511.14010 MoRA-RAG | hazard-specific数据库路由/chunk/verification循环及灾后QA领域提升，AB未给超出既有检索组合的新通用成立条件/失效边界；C，不采grounded/trustworthy宣传或用领域关键词硬关 |
| 2511.13892 ITS jailbreaking | 图像typography与multiturn攻击/过滤、GPT4与人工验证→输入模态/会话链与harm判定资格不同；窄P及必要安全反侧，不能以交通应用/成熟攻击组合直接排除；不实施攻击、不授全面保护或安全有效性 |
| 2511.13717 TZ-LLM | TEE权重缓存/解密与NPU world-switch成本→确定访问prefetch pipeline＋TEE最小dataplane/REE fulldriver分工→安全边界与TTFT成本选择；窄P，不采90.9%/23.2%普效或TEE安全完备 |
| 2511.13647 Part-X | 3D多任务接口分裂→结构化可执行grammar序列承载part boxes/semantic/edit并分离geometry后端→多模态表示/执行接口；窄P，语法合法不授几何正确/任意engine兼容 |
| 2511.13548 ForgeDAN | mutation同质/fitness浅与keyword判定falsepositive→多层perturbation/semanticfitness/遵从与harm双judgment→安全测量/攻击搜索条件；窄P及必要强安全反侧，不采stealth/普遍越狱有效或运行攻击 |
| 2512.02024 RxBench | prescription错误分类/临床药师人口/领域fine-tune，属于当前暂缓医学应用，未显示独立模型系统机制；实际完整AB-C，不把定位时看到的完整AB记title-only，不采human-level临床能力 |

## 3. 下一普通与交接

请root转Ohm先对本批准入/代表关闭及两个必要门作实际校准；包只已读这14AB，不预签78全筛/日期/Source全。其它新相关/含糊AB继续分批，旧18/两重合精确有效层不重；SoCE单项已另交逐字PRE，不等所有arxiv完。当前无legacy、Books锁或本人工具在途，未DAY/FINAL，本日未接纳。

## 4. 第二批18完整AB实际／13P一必要门四C提案

继续实际读取去重原件中的18份完整abstract-full，不重第一批14/两旧重合；新增如下。当前累计32完整AB＝21窄P＋3必要决定门＋8AB-C，余身份尚只是标题/未读，不能称全78已筛；date/current资格分别另责，不评分。

| 身份 | 最小增量与判断／未授边界 |
| --- | --- |
| 2511.13494 LGIP | paraphrase应不变/semantic-flip应改变分开→传统retrieval分数掩盖错误偏好→多模态不变性/敏感性测量；P，不采自动flip即语义gold/所有SigLIP机制因果 |
| 2511.13478 SliDer | raster primitive扁平化丢text/image语义→可编辑SVG语义结构＋推理中render/refine→表示输出/执行消费接口；P，不采82.9%普效、重建相似即内容faithful或全编辑可逆 |
| 2511.13476 FuelAnalytics | 三role叙事/LLMjudge/可选人审与4006公交trip案例，没有新增通用形成机制/独立成立条件或评价混杂反证；C，不采97.3%或多agent因果提升 |
| 2511.13458 TrustWorkshop | 参与式pilot讨论信任与后续研究，AB未给可改变模型/系统解释的具名发现/新测量资格；C，不以user study或初步规模自动排除，未来具体证据才定点恢复 |
| 2511.13432 LastVote | 民主社会七风险/ISS多stakeholder/制度分期治理，不是本项目模型能力/系统运行的新机制；范围C，不把社会风险taxonomy搬PLATFORM owner |
| 2511.13420 VOPE | 自愿想象不能按纯factualcaption一概罚→recheck生成对象的原图presence判断→grounding对象与创作意图分账；P，不采recheck自述为内部认知或所有mitigation无效 |
| 2511.13371 CognitiveMaps | 探索/最短路径/混合训练形成不同空间策略→固定小GPT2表征/因果干预显示历史方向依赖差异→训练人口与泛化策略资格；P，不因小模型关，不授所有Transformer世界模型谱系 |
| 2511.13240 ActionBelief | static confidence校准不预测下注/查工具/受挑战动作→belief-action gap的交互条件→评价需分离静态校准与决策一致性；P，不把confidence当真实内部信念/理性或安全保证 |
| 2511.13225 Spectrograms | 图像能力不等能读speech频谱→统一style/phoneme-edit distractor下zero/fine-tuned近chance→表示消费/监督边界；P，不由有限失败证明永远需特定参数知识/所有paireddata无效 |
| 2511.13189 ViXML | 大decoder扩容量与单image embedding增modality的费用/质量替代→small视觉encoder在XMC部分配置胜textdecoder→多模态表示预算选择；P，不采“image值billions”普遍律，必要比较不照录单SOTA |
| 2511.13152 GrammarPseudo | LLMrubric伪标签/clean-noisy ratio与训练稳定相关，声称新noise训练框架但AB未给具体loss/噪声处理增量；必要决定门，仅实际noise训练规则/对照，不因语法场景或伪标签成熟直接关 |
| 2511.13131 MM-Telco | telecom任务集/领域finetune提升、未指具体新评价blindspot/模型形成或执行机制；C，不因benchmark标签排除或采用未具体化“弱点” |
| 2511.13095 BeDiscovER | temporal arithmetic强与full-document/rhetorical关系弱分开→任务粒度变化下reasoning评价盲点→能力解释；P，不采52数据集规模作贡献或所有LLM discourse失败 |
| 2511.13052 LfU | limited-dataSFT易spurious/遗忘→先undesirable更新再约束前后representation一致→regularization的扰动对象；P，不采16.8/92.1普效或已保全全部预训练知识 |
| 2511.13036 uCLIP | lowresource缺paired跨modal/跨language数据→freeze两encoder/Englishrepresentation anchors/小projection对齐→无对应pairs的监督消费；P，不把无pair说成无监督/全语言公平 |
| 2511.13029 AA-Omniscience | 正确recall与abstention需共同计量并按domain条件化→有限评分/选择人口显示总能力榜不能代知识可靠性→评价对象；P，不采index=真校准/分数最高即安全，必要scoring资格另核 |
| 2511.13023 SLMQuant | LLM量化方案迁SLM出现不同敏感性/效率profile→架构与任务条件化压缩选择；P，不采所有SLM统一规律、硬件加速/低端部署已验证 |
| 2511.13940 ParallelKittens | 算子专用overlap难随设备/负载迁移→八primitives＋统一template分解transfer/resource/overhead→多GPUkernel可编程边界；P，不采峰值/少代码行等E2E普效或已部署 |

上表均仅实际AB准入方向；原机制/实验可信度不以未知日期硬排，后续只必要决定门或确有资格时深入。第一/第二批已准备即可root转Ohm实际校准，不等Sources/全部AB；现阶段未把未经核验的摘要收益或安全叙述写入Books。

## 5. 第三批14完整AB实际／六P三必要门五C提案

实际继续14个新身份完整题摘，累计46AB＝27P＋6必要决定门＋13C；仍不是全78或日期资格。原2重合方法不重；题名与原完整AB均在本日去重JSON，可独立读回。

| 身份 | 具体准入/关闭依据及边界 |
| --- | --- |
| 2601.16984 TelcoAI | sectionchunk/queryplanning/metadata/RAG文本图融合及3GPP领域指标，无新通用成立条件/失效路径足以改变模型系统解释；C，不因telecom标签关，不采92%faithfulness/原JanID授Nov18 |
| 2512.00047 AnnotationConvergence | 7500交互过程的code-stability/semantic一致性/影响不对称与embedding压缩→协调过程不等正确annotation→multiagent评价对象；P，不把convergence/维度下降证明内部alignment或真协商 |
| 2511.14136 CLEAR | 不控费用/单次成功掩多次一致性→cost/latency/efficacy/assurance/reliability条件对照→Agent选择需预算与repeatpopulation；P，不采ρ=.83生产预言/所有12benchmark结论或未经核数字 |
| 2511.14135 AdaFair-MARL | 医院协作Markovgame的Jainworkload约束/primal-dual及SOC形式，AB未建立基础模型训练/LLM委派执行或VLA策略的直接知识链；范围C，不因理论/小实验/成熟拉格朗日自动排除，也不将一般MARL类比计LLM机制 |
| 2511.14043 AISAC | 明确runtime角色/turn与depth预算/角色memory权限/trace，不因Scientific应用一概关；必要决定门仅核这些通用执行约束是实际强制资格还是配置组合，科学发现不采用、不全读取其科学case |
| 2511.13998 LoCoBench-Agent | singleturn理解不涵盖工具/恢复长交互→固定工具/10K–1M、comprehension与效率负相关→longcontextagent测量条件；P，不采相关因果或“真实开发”保证 |
| 2511.13987 MusicAnalysis | 教育/音乐分析双案例与整合综述，未给模型形成/生成音频机制/独立执行约束增量；C，不是因音乐或review标签关闭 |
| 2511.13983 MoMoE | neuralMoE末attentionblock与agent多层路径结合→是否有真正双路由消费/资源选择而非加层组合；必要决定门，原金融标题不能硬排，精确增量清楚再判，不预采synergy |
| 2511.13961 FICO | recedinghorizon/factorization通用MAPF路径规划与不确定执行、无可学模型/LLM或VLA直接机制；C，不以multiagent/robotics词自动收、不授千agent实时生产 |
| 2511.13865 CA-RCT | Entra四任务/162admins的agent辅助准确率/时间领域采用效果，AB未指出新的模型/控制机制或评价blindspot足以修正设计；C，不因RCT或企业应用标签自动关，也不采用48/43%/生产安全 |
| 2511.13860 Phishing-RCT | queueprioritization/explanation改变人工注意力分配，非机械rubberstamp的局部反侧→建议质量/人工依赖/队列收益对象不同；窄P，不采6.5×/77%普效或无自动化偏误保证，必要oracle/分母/控制资格另核 |
| 2511.13614 MarketCommunication | 同策略alignment但市场regime/competitive-collaborative收益不同、conversationquality与return零相关→通信policy与质量proxy失配条件；窄P只LLM协作测量，不采金融收益/市场普遍因果 |
| 2511.13593 O-Mem | 先semanticgrouping漏非相关却关键user信息→主动profile/event更新＋persona/topic分层检索→memory写入与检索对象；P，不采3%/latency普效或derivedprofile为用户事实 |
| 2511.13410 Mem-PAL | 合成/humanrefined个性化多session数据＋H2heterogeneousmemory，AB没说明memory消费实际增量；必要决定门只层级/异构选择机制与对照，不因中文dataset或已有RAG硬关 |

这些是作者提案，不代Ohm真实准入校准/必要门。公开日及当前event已有说明未由AB取得；安全/强反侧不以日期或工作量关，收到具体决定域即可定点补读，未把76新身份全变全文队列。

## 6. 第四批18完整AB实际／11P三必要门四C提案

实际读取最后18份相关/含糊完整AB，累计**64新完整AB＝38窄P＋9必要决定门＋17AB-C**；其余12明确题名项与两旧重合另分，78不是当天论文数。以下仍作者提案，待真实校准，不抢先新评分/关闭9决定门或日期归属。

| 身份 | 具体增量/必要问题与限定 |
| --- | --- |
| 2511.13361 MedDCR | Designer/Coder/Reflector与archive在医疗coding应用中迭代workflow，未给改变通用学习/执行资格的独立新目标/约束/失效证据；C，保不是role名即新机制、不采临床可靠性 |
| 2511.13305 SAINT | 无OpenAPI时静态endpoint模型/operation依赖图约束场景生成和执行反馈→代码可得性/调用顺序是生成资格；P，不授覆盖/开发者偏好为语义正确或全部Java安全 |
| 2511.13297 CorrectAD | 长尾failure需求→3Dlayout条件worldvideo与annotation对齐生成→针对失败的训练数据闭环；P仅学习/生成机制，不采碰撞减少数字为真实道路安全/任意planner普效 |
| 2511.13293 GHAR | trigger retrieval与双role共同MDP/reward声称联合优化，必要决定门核实际trigger/目标及rolecredit是否独立通用机制而非医疗RAGrecipe；医疗预测效果不采用，不因Science标签跳过具体可疑增量 |
| 2511.13288 M-GRPO | 异频/变长subagent调用难成batch与credit→main/subgroupadvantages＋trajectoryalignment＋跨server最小统计分离训练→RL数据/信用边界；P，不把“无跨server反传”授梯度全等价/普适稳定 |
| 2511.13248 DualTAP | router读PII与agent读task的不同消费者→PIIregionattention＋utility/privacy双objective与双population评价→隐私扰动不是只最大压制；P/必要安全反侧，不授31.6pp为隐私完备/80.8为普遍无损，不实施攻击 |
| 2511.13233 DataMarketSim | LLM买卖agent目标/行动与三交易分布拟合，无新的通用协调/执行/学习资格或设计反证，C；不采“真实市场”因果/forecast有效 |
| 2511.13158 AgentVisualProgramming | BDI/JaCaMo块编程+WoT新手automation，无基础模型/LLM学习或执行约束直接链；范围C，不将所有softwareagent类比作LLM贡献 |
| 2511.13193 DALA | freeforallcommunication→按message预期value-density竞拍发言带宽→token预算下学会选择发言/沉默；P，不采6.25M/最高分普效、经济用词不证明真实效用oracle |
| 2511.13137 ConditionalDiffusion | 高层subtaskeffect由conditionaldiffusion预测nextobservation/reward、低层共享skill/semanticmixing→学得环境预测消费于分解决策；窄P，只状态预测/训练接口，不将普通MARL总分外推foundationworldmodel/物理安全 |
| 2511.13118 EventCoder | schema变executableclass→deterministicvalidation/精确feedback参与迭代生成→结构约束与语义消歧可分；P，不将schema过等同抽取完整/事实正确，不因event应用硬关 |
| 2511.13103 STACCA | 长程交互/跨networkcritic与state-value兼容counterfactualadvantage，必要决定门只advantage新代数/假设能否直接支撑模型训练credit，还是网络控制应用；不因Transformer名收或一概一般MARL硬关，不采疫情效果 |
| 2511.13087 MEGA-GUI | one-shot空间稀释/语言歧义→双向ROIzoom＋contextrewrite、模型视觉scale反侧→grounding分辨率/语义输入选择；P，不采最高accuracy/局部grounding即真实action成功 |
| 2511.12998 PerTouch | semanticregion参数map到image可控映射＋训练semanticreplacement/参数perturbation→生成控制接口，VLM反馈/记忆另分；P，不采主观aesthetic/对齐用户意图普遍保证 |
| 2511.14131 R3 | lightweightVLNexpert/昂贵MLLM不同代价→progressmonitor三criterion在两推理mode间切换→runtime质量/费用资格；P，不采SPL普效/切换oracle完备 |
| 2511.13876 QwenCLIP | 换长contextembedding encoder＋learnableprompts用于放射报告对齐，当前医学应用暂缓且AB未给独立通用模型机制/失效边界；C，不以更长context/新名称单独收，不采临床模型效果 |
| 2511.21707 WMLM | RF作为anchorcontrastive训练multimodalGPT，必要决定门核无线rawcodec/跨modal监督对象是否新通用表示消费而非新领域对齐；不采“universalmodality”或网络智能普效 |
| 2511.13021 PragWorld | 最小语言改动/多轮entitystate与层级regularization→对话表示/shortcut测量与训练目标；P，“world”指对话局部语义状态，不挪作PartIII环境transition或真实外界状态 |

## 7. 十二题名范围关闭提案／两本日旧重合

当前12题名明确领域切片，没有将其自动抽取的abstract当实际已读：2511.13891（遥感gully检测）、2511.13801（ArabicGospel传统文本变体分类）、2511.13526（医学indicatorKG）、2511.13523（临床reportOCR）、2511.13517（ransomware的BERT/RoBERTa分类解释比较）、2511.13505（publicnarratives应用）、2511.13381（儿科临床能力评价）、2511.13378（Peirce手稿知识提取）、2511.13182（罗马尼亚diacritic恢复对比）、2511.13107（临床CONSORT遵从评估）、2512.00048（patientinteraction临床知识）、2511.13948（超声心动图测量/解读）。这些不显示独立通用模型/系统机制链；当前医学应用按ROADMAP暂缓，传统NLP/领域分类不凭LLM名称收。不宣这些title已全文/贡献审阅或精确公开日通过，实际相关纠错/主线反证信号若出现只恢复对应项。

两重合为2511.13646 Live-SWE与2511.12997 WebCoach，本日旧精确v1准入/必要证据/反侧/root层有效，不重复读全部方法；新current/事件说明只具名轻核，不能由同名或ABsame授当前无变化。至此作者本轮实际分层为**78身份＝64新AB（38P/9必要门/17C）＋12title-C提案＋2旧重合**；旧18不另加入78或并成他日池。未完成的是实际准入独核/九决定门、必要current/date、有限来源出口和完整six，不预DAY/FINAL。

## 8. Ohm13真实升级与13182纠错信号定点恢复

作者已实际读Ohm§13：第四批十八完整AB通过；reader另实际读2512.00048完整AB，确认其临床模拟DAG及固定策略嵌入system prompt没有LLM finetune或通用执行资格增量，故在reader层升级为AB-C，而不是title-C。本人不把reader的阅读冒为本人已读，既有64/12是本人当时层；九必要门仍普通，不以日期未知关闭。

随后作者实际读本日新metadata的78个版本/Submitted/Comments/Journal字段，发现**2511.13182具体metadata纠错说明**，只恢复该受影响项。实际直开[当前官方abs](https://arxiv.org/abs/2511.13182) L8–31及[精确v2官方abs](https://arxiv.org/abs/2511.13182v2) L28–68，当前v3为Nov21修订、history明确v2 withdrawn；v2页面本身明确由作者撤回、无PDF，Comments说明原提交metadata有错并将替换，v2作者字段含Mihai Dan Nadas而当前为Mihai Nadas。仅据此确认具名撤回/metadata信号，不补造撤回的科学错误、v3已解决全部问题或整个家族所有版本撤回；Submitted Nov18亦不作公开日。

作者在这两原件实际读完完整AB：比较多模型/多prompt的Romanian diacritic restoration与echo baseline，AB报告模型间和prompt差异，未给通用表示/优化机制、可改变系统解释的具体反例或新的评价混杂资格。故**当前v3为实际AB-C、v2撤回版本不得入选/评分/Books**；不扩其全部实验或双版全文，metadata范围信号不自动授权采用科学结论。原题名关闭须由此实际处理覆盖，不以“无纠错”概括。官方记录保存于`SUP_WEB_CORRECTION_META_20261015.json`（另含Meta目录有限字段），无本项采用链需清除。

两方实际阅读层分别为：writer 65新完整AB（38P/9minimum/18C）＋11title＋2旧重合；reader§13为65新完整AB（38P/9minimum/18C）＋11title＋2旧重合，但两方新增第65项不同。合并真实证据层是**78身份＝66新完整AB（38P＋9minimum普通＋19AB-C）＋10title-C＋2旧重合**；不是两方各自已读66或全部current通过。请root转Ohm定点核13182纠错/当前AB处置及这个非重复归并，不重其余64AB或所有版本史。

## 9. 实际独核18–19后有效分层／不重全池

作者现已完整读Ohm16–19：13182具名纠错与当前AB-C、三minimum及后六minimum均通过，最终78＝66新完整AB（44窄P/22AB-C）＋10title-C＋2旧重合。作者与reader的第65项不同由§8保留真实层，不倒改作者已读数量。Mem-PAL/STACCA原v1必要机制由Ohm18实际核，作者current v2层与之分责，按精确命题复用不重方法。

四必要安全影响域与46 current轻核已Ohm19实际读回，通过的是有限字段/采用边界，不是44个家族标准/深入Evidence完成。日期责任已精确归并为新44＋原17（含这两dup且不含已采用机构事件SoCE）＝61论文，再加LPLB一个artifact共62；未知资格不评分/正式/Books，不从Submitted/版号/citation/公告月份补日。九门/13182/current/四安全不再挂普通全稿队列；仅来源尾包Qwen本日fresh字段及完整six独核待回，不预DAY/FINAL/计数。
