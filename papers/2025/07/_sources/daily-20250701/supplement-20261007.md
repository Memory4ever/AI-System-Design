# 2025-07-01 来源遗漏补查

作者：本轮主任务root；不是原jul01_author。当前合同/Prompt/ROADMAP与本日原报告、筛选记录已重新读取，未加载其他日报整体材料。执行日2026-10-07，补充窗口2025-06-30完整自然日，原精确窗口与有效证据保留；原正式候选0，不把以前的候选日期重新排序。完整原报告已保存baseline，不覆盖旧原件。

本轮有限来源检查、候选证据/Books判断和独立复核已完成，依据是本轮Bernoulli最终§8而不是原完成标签。只检查14每日来源与实际触发具名证据，不扫描Weekly、不创建缺失Daily。arXiv不用catchup，用具名主题Advanced/API与有界官方月表；提交日/公告年月只作发现，不冒充具体公开日。原先ERNIE因旧08:00/09:00界限隔离的材料已按本次新增自然日检查，最终为1确定候选/标准完成/具体已有覆盖，Books零写入。

原始新请求将保存同日supplement-20261007目录，逐请求保留实际URL、执行UTC钟/HTTP/错误与停止位置；成功下载不等于已读。旧SCREENING仅复用必要去重或未变实际证据，不照搬成重新扫描。Books由root协调，必要时先加载Books上下文、作唯一owner实际正文差额；当前无Books写入或采用提案。

## 本轮实际发现与首批准入判断

18:02～18:15实际新取14来源入口及必要补检，原件在`supplement-20261007/`。Google June Blog/pubs与Meta curl各40秒超时，Blog已由web入口恢复9条；其6/30条目是HOV-specific ETA地图应用，未新增基础模型/训练/推理机制，范围关闭。DeepMind真实第2页（30条，265 publications目录）跨过7/1→6/26，无6/30列表条目；只支持该精选目录范围。OpenAI RSS1251项按BJT日期过滤唯一6/30 Economic Blueprint，政策范围关闭。Qwen第2页7/22→6/27→6/26→6/5，Kimi全文目录7/11→5/6，MiMo Paper/Blog 9/19→6/4→5/12，均只在所读目录未见6/30条目。DeepSeek updates已新取，不由news默认入口替代。

arXiv五组Advanced均用`classification-computer_science=y`、cross-list include、公告年月`2025-06`到`2025-07`、倒序、size50/start0：language model、language model AND inference、language model AND reinforcement learning、world model OR vision language action、agent AND memory。各读到第1页50条，总命中3520/575/307/136/91是月级搜索规模，不是本日论文数。250次返回归并231 ID，与旧SCREENING身份55重合，176新月级线索。未把176变成候选队列或证明逐项筛选完成。选其中原v1提交含6/30、未在旧记录出现的25项实际完整题摘阅读，提交字段只用于查漏优先级，不作公开日或排除其他日期潜力的标准。其余151项仍是月级库存，不冒称明确窗外或全部关闭。cs.CL有界月表head25只作身份辅助。

25项首批判断如下；当前搜索摘要可能是晚修版本，不冒充2025-v1机制证据。全部必要具体公开日未确认，不评分、不进第3节正式候选，不进入Books。

| ID | 当前题摘支持的具体潜力或关闭理由 | 首批处置 |
| --- | --- | --- |
| 2506.24019 Ella | name-centric semantic与spatiotemporal episodic memory分工；摘要明确长期15-agent活动后有unseen controlled evaluations，但本批未读协议/对照/预算，不由该场景证明普遍自治 | 潜力 |
| 2506.24120 Data Uniformity | minimum pairwise distance数据选择与GD收敛/近似误差的假设及SFT比较，需核原版本理论条件，不把均匀分布当所有数据最优 | 潜力 |
| 2506.24119 SPIRAL | self-play课程及role-conditioned advantage解决多角色训练baseline问题；局部游戏收益不直接授跨任务泛化 | 潜力 |
| 2506.24117 Biblical Hebrew | 成熟embedding对文本平行匹配的领域比较，无模型机制/评估盲区的新证据 | 关闭 |
| 2506.24106 Representation Dispersion | contextual dispersion代理与perplexity/层选择、push-away目标的可归因边界 | 潜力 |
| 2506.24086 MotionGPT3 | continuous motion latent、双流共享attention与generate-then-align减少跨模态干扰的条件 | 潜力 |
| 2506.24056 Logit-Gap Steering | first-step refusal margin代理及低困惑度suffix使防御失效的安全反证，当前2026-v修订不冒充2025事实 | 潜力 |
| 2506.24006 Word Problems Review | 题库偏向无需真实情境的s-problems，评价成功不等于context理解；当前含GPT-5不是v1证据 | 潜力 |
| 2506.24000 TTA-VLM |统一协议下accuracy与calibration/OOD/stability冲突，属评价反证，不因benchmark类别关闭 | 潜力 |
| 2506.23998 Auto-TA | 临床叙事专用角色pipeline与可选RLHF，无具体新训练/执行机制或可复用失效证据 | 关闭 |
| 2506.23982 StyleDrive | driving preference标注的规则/分布与subjective VLM、人核接口，保留具身评价潜力，非因驾驶领域整体排除 | 潜力 |
| 2506.23979 TaP | taxonomy控制多语言preference数据组成；规模180倍比较需匹配预算，不由数字单独授贡献 | 潜力 |
| 2506.23951 ClassifSAE | 分类head/activation-rate sparsity和解释指标的局部干预边界，不能把interpretable当语义真值 | 潜力 |
| 2506.23921 Trilemma of Truth | probing的transfer、真/假不对称与第三信号反证及conformal多实例接口 | 潜力 |
| 2506.23919 Goal-VLA | 生成goal image→object pose→低层控制，Reflection-through-Synthesis接口；图像合理性不是真实结果 | 潜力 |
| 2506.23906 Segmented Operations | MMV-RAM假设下segmented scan/sum映射矩阵单元，服务AI kernel，不因硬件/理论论文关闭 | 潜力 |
| 2506.23903 Ultrasound | 成熟DINO/SAM2+LoRA的超声适配与领域指标，未给主线新机制 | 关闭 |
| 2506.23825 Flash-VStream | 低容量temporal context memory指导高容量spatial augmentation检索，延迟/容量取舍 | 潜力 |
| 2506.23815 Education Assessment | Bloom/Constructive Alignment教学评估政策框架，不是模型evaluation机制研究 | 关闭 |
| 2506.23749 Program Repair Survey | 当前摘要的control-placement分类与protocol comparability audit可能改变Agent评估，不以综述名称关闭 | 潜力 |
| 2506.23743 Positional Bias | 控制选项顺序和不确定性后测Preference Fairness/Consistency，评价反证 | 潜力 |
| 2506.23670 TinyWave | hidden/attention/softlogit逐层distillation压缩interleaved speech模型的质量与执行约束 | 潜力 |
| 2506.24113 Epona | temporal dynamics与video diffusion分解、chain-of-forward处理AR误差及planning接口 | 潜力 |
| 2506.23603 Semantic Privacy SoK | 非作者必要v1 core显示语义保护对象与量化合同潜力，撤回原“分类/无新算法”关闭；均值偏差与posterior/prior KL的等价性缺条件，保留中心定义争议，不采用为安全保证 | 潜力/中心争议 |
| 2506.23601 SemDiD | embedding方向/组排斥/位置去偏改变语义多样性与Best-of-N/RL数据条件，需核质量约束及成本 | 潜力 |

作者最初20日期待核潜力/5关闭保留为初判。Bernoulli实际全部25题摘与SoK必要v1 PDF §1～5.1校准后建议21日期待核潜力/4关闭；本次已落实R1重开与R2 Ella事实纠正，不增加身份或评分。其均值不控制KL的三值反例属于复核者数学检查，不冒充作者实验或root已读完整稿。正式当前处置为21P/4C，尚待写后差额核。

Bernoulli对当前五响应可见comments轻核R3：原176/151库存内`2506.19433 Mem4Nav`当前v2官方明确2025-10-10撤回（调查潜在学术不端/自愿撤回），只作撤回排除，不裁定不端成立、不评分/采用；`2506.19481 Haskell refactoring`当前admin text overlap与`2502.07928`相关、不是撤回/抄袭裁决/已审重复，两当前题摘的角色pipeline与任务指标不足建立主线新机制，贡献关闭。必要标记abs与题摘由Bernoulli实际读取，root复用其具名结果，不写成root新抓；不扩二月扫描、全版本史或追无关公开日。两项原在176内，不把发现数加为178；25题摘身份数不变，原151库存中这两项已有具名处置，其余149未逐项裁决。其余已读25comments无可见撤回/重合标记，不授全网无标记。

### ERNIE 4.5 新增自然日事件

新取[官方Blog](https://ernie.baidu.com/blog/zh/posts/ernie4.5/)完整正文明确日期2025-06-30；本轮新增按自然日，原轮08:00/09:00边界不再用来排除该新增事件。原报告原候选0不变，不移动其他候选。拟贡献为共同backbone容量下shared/modality-specific参数空间与语言→多模态continued pretraining，直接回应所有模态共享导致干扰、完全隔离失去迁移的取舍。首拟2+2+2=6，标准审阅，不因机构/模型规模/47%MFU抬分。正文仅高层披露orthogonality、modality token balance、heterogeneous parallel与dynamic PD角色，不授确切公式、无遗忘、near-lossless量化或端到端吞吐。MFU/性能缺硬件、精度、数据/长度、并发/SLO及配对预算，不采用孤立数字。

长期命题owner为`MULTIMODAL-REPRESENTATION` Ch23的fusion/capacity接口，不重复归Ch21通用Top-k推导。已实际读取Ch21开头/router/容量与Ch23所指相邻段；Ch23第391～393行已清楚承载modality eligibility、shared MLP与active-budget/transfer分账，第984～993行承载共享交互层与modality-specific FFN/路由容量的共存和失败条件。Blog未给能修正这些论点的可归因新边界；Bernoulli实际完整Blog/日期/核心、Ch23第367～416与965～1012及邻接已核，单项准入/6分受限标准审阅/具体已有覆盖No Change PASS，见[独立§5](review-supplement-20261007.md#5-ernie单项pass自然日标准审阅与具体已有覆盖)。不是给ERNIE所有训练/量化/PD授覆盖，技术报告/实现/图像benchmark未读、性能未采用，无必要Books写入。

## 剩余来源与写回

Seed实际US头请求时间18:22，papers p0/20返回18+20，total94、has_more=true/next40，在7/4→6/27/6/26跨目标；BlogUS18+18 total45/next40，在7/14→6/28/6/25跨目标，默认15+18 total49。当前查漏到跨窗页停，不要求年度94/49全量队列；US确实恢复默认缺数组，不将总量差认定具名遗漏。PublishDate只为该目录日期，不替arXiv首公告；所见邻接没有June30，不能承诺所有未列资产无发布。

本轮Google pubs默认/初始year+query curl超时；实际category=2025&search=language%20model及search=2025-06-30两web入口均不可达，未获本日first-public目录，不把空响应当零命中。Google June Blog由web恢复9日期项，6/30 HOV核心L114～159另读，soft temporal clustering/weighted median与classifier投票MoE仅服务车道ETA，非基础模型稀疏专家机制，贡献关闭。Meta定日官方域搜索没有恢复具名本日研究，Research40秒失败不授历史覆盖；两当前ZAI页下界December、Hunyuan九条displayPublishTime全2026、MiniMax当前精选页缺H1，与本轮原件/旧具名边界一致。

Anthropic定日补检恢复Citations官方June30 Bedrock更新；新抓完整核心L95～120实际读，sentence chunk与Messages引用为既有功能，June30仅新增部署渠道、未披露新的保护/正确性/兼容机制，贡献关闭而非把旧API机制重新当当日贡献。15%recall/0%source hallucinations为未核internal/customer宣传，不采用；Opus3退役只是已知生命周期事件，原有效关闭复用。该两个条目不证明Research目录完整。

首批独立FAIL R1～R3已逐项写回到本记录与README，R4两处DeepMind返回数量也已修正；未通过的历史裁决原文件保留。Bernoulli最终§8于2026-10-07T18:54:29+08:00具名DAY PASS，复用未变21P4C/两标记与ERNIE单项结果，普通待办0。日期/目录及中心争议仍按具名条件终态隔离，不授正面Coverage/Evidence或无遗漏；149未逐项裁决月份库存不是强制队列。

不stage、commit、push；保护并发和原有修改。
