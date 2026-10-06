# 2026-03-07 V3 当日停止点

检查时间：2026-10-01T22:53:34+08:00。作者：mar03_v3（本日独立作者）。
窗口：[2026-03-06T09:00:00+08:00, 2026-03-07T09:00:00+08:00)。

本次在换日与恢复时完整重读AGENTS、当前RESEARCH_CONTRACT、REPORT_CONTRACTS、CODEX_RESEARCH_PROMPT、ROADMAP及最新相关checkpoint；来源仅Daily14项与其arXiv主题。没有Weekly输入，没有继承旧593条逐项队列、31候选、9分或旧Books完成声明。旧报告保存在[V3_LEGACY_REPORT](./V3_LEGACY_REPORT.md)；原始HTML/题摘与版本历史只按本次实际用途复用。

## 来源执行与停止范围

源页是执行时的当前可见历史段，不是归属日的网页快照；有限目录未命中不证明全机构没有发布。必要的缺失子目录/日期均在报告中隔离。

| 来源 | 实际入口、查询与停止点 | 结果及限制 |
| --- | --- | --- |
| SRC-OPENAI | Research主页及官方news/rss.xml；实际完整XML中筛出06/07 Mar 2026，三条：Codex Security、Balyasny、Descript；03/06～07 + model/training/architecture/multimodal主题域限定搜索。 | Codex RSS为Fri, 06 Mar 2026 10:00:00 GMT（18:00BJT）。两story为Fri, 06 Mar 2026 00:00:00 GMT，正式页仅Mar06；零点可能日归一，不赋予精确首发。RSS仅支持其可见记录，不代替所有历史Research索引。 |
| SRC-ANTHROPIC | Research嵌入publishedOn列表与Engineering页；03/06～07 + model/agent/evaluation主题域限定搜索；Firefox与BrowseComp具体原文。Research邻接Feb25→Mar05 labor-market→Mar06 Firefox/Exploit→Mar13 diff-tool。 | Firefox article:published_time、JSONLD datePublished及time dateTime同为2026-03-06T10:30:00.000Z。BrowseComp正文Mar06、上述字段00Z、modified Mar18；仅相交日。labor-market是经济影响研究，不扩成社会科学队列。 |
| SRC-GOOGLE-AI | DeepMind Research当前精选与Google Research pubs（year筛选而非日级）；03/06～07 + foundation/language/multimodal/training/inference官方域搜索；WAXAL完整官方核心。 | WAXAL明确贡献关闭。current主页和year索引不能恢复目标日全部论文；历史pubs日级段/DeepMind历史发布段受限。 |
| SRC-META-AI | 官方Research返回0行；03/06～07 + model/architecture/training官方域有限补检。 | 搜索无新相关原文，不把空响应作0事件；Research历史目录缺口。 |
| SRC-QWEN | qwenlm.github.io旧Blog及重定向qwen.ai/blog；前者可见首屏2025/09/23→07/24，后者0行；03/06～07官方域模型主题补检。 | 未恢复2026本窗官方目录；不重新遍历PR活动。 |
| SRC-DEEPSEEK | 实际Research/News页面：Research Index10项至2025/05/14，Feb25 DualPath→Jun24 V4；News首5项Dec01→Apr24，View All未展开；03/06～07官方域补检。 | 可见Research段无本窗值；News隐藏历史和API子入口不能由首屏证明完整。 |
| SRC-MOONSHOT | 实际新官方www.kimi.com/en/blog/ Research19项读至2024/06/26 Mooncake；Feb09 Agent Swarm→Apr20 K2.6。 | 当前可见完整19条无March记录，没有未完成可见分页；不是全机构历史保证。旧platform Blog不承担2026目录。 |
| SRC-TENCENT-HUNYUAN | 独立按本窗对读共享[V3_HUNYUAN_LIST_RECOVERY](../V3_HUNYUAN_LIST_RECOVERY.md)：实际JS指向POST publicList，renderType0,page1,size20，total11且11项；本日官方域有限主题补检。 | 当前“全部”可见11/11，display Feb13→Apr23无March。publishedAt/display不同，不互替首公开；未重新扩GitHub或重试动态浏览器。 |
| SRC-ZAI | 当前Research页及共享[V3_OFFICIAL_DIRECTORY_RECOVERY](../V3_OFFICIAL_DIRECTORY_RECOVERY.md)独立对本窗：首可见页Aug26→Dec09，Feb21 GLM5→Mar15 GLM5Turbo，到“查看更多”止；03/06～07官方域主题补检。 | 本窗位于可见邻接日期之间；不声称后续分页或全机构历史完整。 |
| SRC-BYTEDANCE-SEED | Research/Blog当前页86行；Publication相邻Apr11→Jan27；public_papers第一页20/242，page1of13至May14；03/06～07官方域主题补检。 | Blog当前精选至Jul31，论文分页未提供历史日级定位；不将242项变逐篇队列，历史段隔离。 |
| SRC-BAIDU-ERNIE | ERNIE Blog当前列表68行，Apr15→Feb06；共2页，更旧页止2025；03/06～07官方域主题补检。 | 本窗落在可见相邻段，无相关新记录；不扩PR。 |
| SRC-XIAOMI-MIMO | 官网实际Paper8条Mar13→Feb03→Jan08；Blog15条无日期并有More；03/06～07官方域模型主题补检。 | Paper可见本窗段已检查；Blog历史日期与More边界不可恢复。 |
| SRC-MINIMAX | Blog可见76行至2025/10/27，Mar18M2.7→Feb14Forge→Feb12M2.5；03/06～07官方域主题补检。 | 可见日期段无本窗新项；不扩Agent Tech Blog历年内容。 |
| SRC-ARXIV | 下面的有限主题查询、月目录50标题补检及实际v1完整题摘；具名27项DOI接口恢复。 | 26项用官方ID公告分配+最早常规公告下界+arxiv.content findable registered上界形成落窗range；AGF下界不足仍隔离。恢复可执行，非外部故障。 |

## arXiv 实际主题与边界

使用过的有限检索：

1. `site:arxiv.org "March 6 2026" ("language model" OR MoE OR Transformer OR attention OR alignment)`。
2. Mar06 + GPU/kernel/world-model/multimodal/agent主题查询；无精确匹配结果，部分结果无关。
3. 四组官方arxiv.org域限定 `"5 Mar 2026"`：language/Transformer/MoE/attention；GPU/kernel/serving/parallel；multimodal/world-model/VLA；memory/tool/agent/retrieval + language。结果主要无关，不把无搜索命中作0论文。
4. 原始官方月目录 `https://arxiv.org/list/cs/2026-03?show=500&skip=2500` 仅浏览首50标题（2603.04780→2603.04859）；对可能关系主线者读完整v1题摘和当前可见撤回/修订说明。月目录没有具体日批次header，不能证明其全部落本窗；offset2000只查原始header身份，不从中建立逐项队列。
5. date恢复只核 `https://arxiv.org/list/cs/pastweek?show=2000` 及精确 `"Fri, 6 Mar 2026" "04797"` 搜索：实际pastweek已滚到September，未恢复本窗历史batch。没有猜测日期URL充当证据。官方availability说明moderation可延迟1～4天甚至更长，Submitted不是public。日程只能提供理论最早正常公告，不授具体公开时刻。

到此停止，不扩整月/arxiv全分类。误打开2603.04891v1（OSPO组织研究）为一次ID定点错误，完整题摘确认与模型系统无关系，不把它或相邻项变新队列。

### 明确关闭样本

以下原文已实际完整题摘/官方核心审读；不评分、不做不影响处置的日期请求：

- [WAXAL](https://research.google/blog/waxal-a-large-scale-open-resource-for-african-language-speech-technology/)：27语言、ASR/TTS规模与许可、社区elicitation/脚本录音是数据发布；未提出可归因的新模型机制或质量/资源设计边界。所引其他研究的domain-alignment结论不冒充本发布实验。不是按语言/规模判价值。
- [Balyasny](https://openai.com/index/balyasny-asset-management)：内部12+维评估、组织反馈、centralize/localize部署与采用率；没有新增机制或可比边界，不能把成熟原则重新记为设计贡献。
- [SparkTales 2603.04806v1](https://arxiv.org/abs/2603.04806v1)：coordinator-AI故事活动改善效率与参与，未改变模型形成或系统设计。web cache miss后实际curl完整题摘，非访问故障排除。
- [EchoGuard 2603.04815v1](https://arxiv.org/abs/2603.04815v1)：KG episodic/semantic + Log-Analyze-Reflect +领域六模式/Socratic组合与未来评估方案；未给出相对既有记忆机制的新成立条件或可归因选择。不是因“尚无实验”自动关闭。
- [WhisperAlign 2603.04809v1](https://arxiv.org/abs/2603.04809v1)：WhisperX/pyannote与Bengali切分/微调的竞赛系统组合与WER/DER，没有新的基础模型或运行时边界。
- [SCoUT 2603.04833v1](https://arxiv.org/abs/2603.04833v1)：softgroups、groupcritic与counterfactual communication credit确有traditional MARL新机制；当前题摘未建立foundation/model-driven Agent或模型系统主线关系。范围关闭不是称无学术贡献，非“多Agent”关键词自动入池。
- 标题明确的非主线补检（如2603.04785 B+tree、04787磁性鱼机器人、04793遥感RetinaNet、04804法院证据评分、04818供应链预测、04854 Sinhala法律IE）只作范围关闭，不称全文审阅，也不靠通用owner重新引入应用研究。

### 具名潜在贡献 / 日期恢复后待裁决

以下保留完整题摘阶段的潜在增量与身份，不是新的待审队列。此前将27项全部日期隔离的理由已被实际接口复合证据纠正：26项March05Submitted+官方ID公告分配规则+arxiv.content findable registered上界形成完全落窗range，见[V3_DATE_RECOVERY](./V3_DATE_RECOVERY.md)。其贡献裁决/必要审阅/Books普通待办已结束，具体准入或关闭见下文与当日报告；AGF二月Submitted下界不足仍隔离。DataCite单独不足保留，但不再误称复合推断不足；旧报告不作新证据。

| 身份 | 原文潜在增量（不等于已验证） |
| --- | --- |
| [2603.04783v1 RLSTA](https://arxiv.org/abs/2603.04783v1) | 多轮context inertia使短期reward不稳；single-turn reward anchor改变训练反馈选择。 |
| [2603.04790v1 Conditional PPO](https://arxiv.org/abs/2603.04790v1) | Diffusion整段action likelihood困难；Gaussian condition与policy iteration对齐，改变优化代价。 |
| [2603.04791v1 TimerS1](https://arxiv.org/abs/2603.04791v1) | 时间序列foundation MoE与rolling objective针对误差累积；仅模型形成机制潜在相关，不采用预测应用指标。 |
| [2603.04797v1 Helios](https://arxiv.org/abs/2603.04797v1) | 非均匀memory与空间KV布局、层次tile改变动态serving状态分配。 |
| [2603.04799v1 CSV](https://arxiv.org/abs/2603.04799v1) | 逐tuple线性LLM调用改为cluster/sampling/voting，边界为ambiguous group再分与声明误差约束。 |
| [2603.04800v1 MASQuant](https://arxiv.org/abs/2603.04800v1) | SmoothQuant共享smoothing在多模态错配；modality factors及低秩补偿针对invariance边界，而非模块名组合。 |
| [2603.04803v1 DCR](https://arxiv.org/abs/2603.04803v1) | Reconstruction/contrastive梯度冲突；在重建表示而非原输入上做对比。 |
| [2603.04805v1 AGF](https://arxiv.org/abs/2603.04805v1) | 位置与语义attention解耦潜在机制，gravity类比本身不证明增量；Submitted为Feb06且March ID，不能把提交日期当归属。 |
| [2603.04814v1 fact-memory vs long-context](https://arxiv.org/abs/2603.04814v1) | persona与factual-recall表现不同且API/cache成本break-even依赖context，不支持普遍memory赢家。 |
| [2603.04816v1 reranking scaling](https://arxiv.org/abs/2603.04816v1) | NDCG/MAP与MRR/loss不一致缩放，metric选择可能改变模型/data设计。 |
| [2603.04817v1 polarization](https://arxiv.org/abs/2603.04817v1) | 小模型物理modality线索与RGB foundation比较，domain-gap/传感noise而非模态无价值。 |
| [2603.04819v1 open-set assistance](https://arxiv.org/abs/2603.04819v1) | 开集task/user assistance grounding与synthetic diversity条件潜在相关。 |
| [2603.04820v1 auto-scoring](https://arxiv.org/abs/2603.04820v1) | 人类难度与LLM难度/encoder-decoder排序不同，潜在judge代理失效证据，不因教育场景标签先关。 |
| [2603.04822v1 VISA](https://arxiv.org/abs/2603.04822v1) | personal alignment tax语义漂移，重写value-vs-semantic目标可能改变训练取舍。 |
| [2603.04827v1 KAN multilevel](https://arxiv.org/abs/2603.04827v1) | 实际窄读HTML §1.2：forward-equivalence不授gradient evolution等价；basis变换改变preconditioning，nested interpolation还要level-complementarity，否则fine重训coarse modes。挑战等价表示可同法训练的选择，不按基础理论主题自动入。 |
| [2603.04828v1 GDS](https://arxiv.org/abs/2603.04828v1) | membership likelihood受频率/相似性混杂，gradient空间结构替代判断。 |
| [2603.04831v1 MCal](https://arxiv.org/abs/2603.04831v1) | 实际窄读HTML §2.2–3.1、4：standard affine matrix-scaling不是新机制，但以clean prediction为target可校正ablated-input attribution，挑战解释失效必须重训表示；rate-conditioned与unconditioned校准不同，含Llama3.1-8B。不是称模型内在reasoning已改善或从medical应用扩科。 |
| [2603.04836v1 text-image retrieval](https://arxiv.org/abs/2603.04836v1) | 两阶段alignment/领域适配“必要”条件待定点核，不仅以电商指标或fusion组合准入。 |
| [2603.04837v1 DBC](https://arxiv.org/abs/2603.04837v1) | Base/Moderation/DBC三臂与gray-box bypass，潜在安全行为约束对照；control清单数量不构成贡献。 |
| [2603.04839v1 SADCA](https://arxiv.org/abs/2603.04839v1) | static positive pair对抗失效，dynamic跨模态pairing/语义增强替代。 |
| [2603.04846v1 MPC Attack](https://arxiv.org/abs/2603.04846v1) | 单surrogate表征偏差，joint multi-paradigm目标改变迁移攻击条件。 |
| [2603.04847v1 GloSplat](https://arxiv.org/abs/2603.04847v1) | 显式SfM tracks持久几何anchor与photometric loss共同优化，避免早期pose drift。 |
| [2603.04848v1 HyperMVP](https://arxiv.org/abs/2603.04848v1) | Hyperbolic masked-multiview表示潜在机器人泛化约束；“withdrew from CVPR”是会议撤稿而非arxiv官方撤回，不能混淆。 |
| [2603.04851v1 shallow RLHF](https://arxiv.org/abs/2603.04851v1) | sequence harm确定后梯度信息消失及恢复惩罚的理论边界，需核假设，未采用旧Book proposal。 |
| [2603.04852v1 theorem priors](https://arxiv.org/abs/2603.04852v1) | ICL深度structural drift，历史precedence graph+执行器改变搜索空间。 |
| [2603.04857v1 FireBench](https://arxiv.org/abs/2603.04857v1) | chat-format vs enterprise/API contract盲区潜在，2400样本/11模型/六维本身不足；中心新finding尚需真实日期后定点核。 |
| [2603.04859v1 OsmosisDistill](https://arxiv.org/abs/2603.04859v1) | compact synthetic distillation artifact可hijack模型而保留utility，潜在训练资产信任边界。 |

这27项不是冻结候选池；26项现已确认完全落窗range，AGF仍隔离。此前ready曾因日期推断错误撤回，目前有限贡献/证据/Books普通工作已结束，不因Book覆盖或成本缩池。当前版本号本身不证明重要修订，未遍历全版本；具体变化只审受影响版本。

另两个非arxiv日期保留：

- [BrowseComp](https://www.anthropic.com/engineering/eval-awareness-browsecomp)与Opus/Sonnet4.6 March6 card纠错同家族：官方blog00Z疑日归一、正文仅Mar06；工程页无RSS/Atom链接，精确slug+GMT、官方X+Mar6有限补检均未取得更细首发。具体潜在反证为web+code使encrypted answer获取、mirrors破binary限制、过程合法性与答案正确分离；两card原始March6 changelog公开但无时刻。潜在贡献明确，不记负侧、不评分/Books。可接受首发RSS、时区日期区间完全落窗或dated correction精确记录。
- [Descript](https://openai.com/index/descript)：官方核心明确caption意义优先后调速→分段syllable/speaking-rate联合意义+duration，并采用dubbing较低semantic Gate；不是因客户案例标签关闭。RSS00GMT=08BJT左端前，但此整齐零点与day-only正式页可能日归一，既不作为精确窗外首发也不作为窗内候选。可接受官方精确publication或完全落窗range，不能用当前customer success数字补证明。

## 证据与 Books 停点

正式两个家族：

- Codex Security：官方RSS确时；核心How works三步及criticality feedback→threat-model→后续scan已读，旧Aardvark对应Analysis/Commit/Validation/Patching已读作局部事件去重。1+2+1=4，版本相关增量，已关闭/仅报告；84/90/50%noise/FP改进未披露受控样本和版本预算，不能归因为editable model，未扩读每个CVE。
- Firefox：官方news核心历史CVEs→未知现版本、Finding→Primitive exploits、两verifier与人工merge边界已读；Mozilla独立maintainer核心验证数据与时间版本差异已读。3+2+2=7，窄深入完成。作者结果支持任务/攻击链拆分和可重放evidence，不证明普遍攻击率、所有污染排除或通用防守优势。No Change建议给root：PLATFORM-EVALUATION-SYSTEM Ch66已具体承载artifact+environment+trace及sandbox/patch/预算边界（1669–1685），变化生效/未请求功能preservation与expert residual（1689–1698），一次污染扫描不证明全无污染（2875–2877）。已读owner引言与相邻65/67交接，未写Books。

首批准入/负侧校准由root分批实际进行。2026-10-01恢复26项复合公开range后，作者普通待办曾重开；目前完整贡献裁决、必要证据及Books比较/窄写均结束，不能以旧两家族范围验新分母。root已实际核全部19候选、八POST、有限来源/日期与负侧，整日source→report Gate通过，普通待办0；外部终态限制不作正面证据。

当前26项的贡献裁决已结束：17准入、9具体贡献/范围关闭；加Firefox与Codex Security共19唯一候选，AGF/BrowseComp/card/Descript不计确定当窗候选。CSV/DBC中心争议不删池。8处Books已实际写入（Ch33/32/54/23/77/16/79/76），全部actual POST独立通过；不得把这些批次复核当日级完成。所有必要证据与Books比较见[V3_EVIDENCE_NOTES](./V3_EVIDENCE_NOTES.md)。来源/贡献筛选已达到本日有限停止，不重扫其他March公告。

### 日期恢复后的定点贡献关闭

- 2603.04822v1 VISA：完整题摘后定点§4.5/§5；detector/translator/GRPO双代理reward和Gaussian候选的mock-finetune双层搜索是既有组合，未建立alignment-tax新成立条件。JSR是value/embedding阈值代理，不是真正保真保证，不因安全标签准入。root认可具体关闭。
- 2603.04820v1 autoscore：§5.4/6.1的890观察、多study随机效应明确architecture/tokenizer与implementation混杂；未给出可独立归因的foundation架构反证。item-wise报告与human-QWK不代理模型难度是已知评价边界，不将解释性autoregression因果写成新理论。root认可关闭。
- 2603.04819v1 assistance：原题摘潜在formation监督对照经§5及AppendixA定点裁决；multi/single训练15000/5000steps，grounding15000→16500且aug不同，内容仍是合成Overcooked任务/coaching-correction recipe，没有能改变foundation能力形成解释的独立机制或条件。不是已准入后因深审成本删除；root认可准入前关闭。
- 2603.04847v1 GloSplat：静态SfM tracks与Gaussian BA没有foundation学习/World Model transition主线关系，不因spatial-state术语入选。root认可关闭。
- 2603.04817v1 polarization：已核pre-Stokes vs post-derived augmentation及受限误差对照；改变的是专用偏振信号的传感器domain-gap，DINOv3仍冻结prior，未给新的通用foundation表示形成约束。保留局部贡献，不推广一般modality边界；按root校准关闭。
- 2603.04831v1 MCal：末轮撤回“已有affine所以不新”排除理由。定点复用精确v1 §3.1/Eq3、§3.3、§4Q1–5：target为clean f prediction，解释对象已由f改成tilde f；Q1的MRI LIME/SHAP sufficiency以维持模型confidence衡量，未给原f feature-dependence的独立真值/干预反证。Table1为rate-conditioned各p平均而Retrain固定p=.5，不是matched-rate比较；Figure7分类准确率支持wrapper功能，不认证原模型归因忠实。可证明output proxy恢复，尚未改变本项目“校准预测不解释内部因果、需独立intervention”的实际选择（Ch66 233–237）；不是以已有覆盖排除。root实际核题摘及作者此定点证据判断，保持准入前关闭，不评分/Books。
- 2603.04836v1 text-image retrieval：§2.5仍是domain CLIP适配→query alignment→MoE/bilinear与graded-engagement三hinge recipe，电商规模与局部指标不建立foundation表示形成新条件，root校准关闭，不称无学术价值。
- 2603.04839v1 SADCA：§3.2 contrastive正负样本、alternate image/text、crop/concat；§4.4同iteration dynamic/static局部transfer下降与random-negative优势已保留。未建立超出既有对抗contrastive/augmentation策略的稳定机制或设计成立条件，不凭攻击数字改写通用安全判断；root认可具体preclose。
- 2603.04846v1 MPC：§3.2 Eq5 L2-normalized concat、Eq6 cosine target吸引/source排斥与温度/ω；§4.3去MPCO、backbone及λ消融仍是ensemble受限tradeoff，未建立新adaptive weighting机制或成立条件，caption-target ASR非实际安全override，root认可preclose。
