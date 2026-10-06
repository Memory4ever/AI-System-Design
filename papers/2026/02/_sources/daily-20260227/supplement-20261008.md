# 2026-02-27 Daily 增量来源记录

新增仅检查 **2026-02-26 北京完整自然日**；2026-10-08用户授权只补来源遗漏，原108候选行、评分、日期、原窗口及连续§4冻结。完整运行前版本为 [baseline](supplement-baseline-20261008.md)。本文件是日报的原始来源/筛选材料，不替代六部分日报及独立验收。未修改共享Books、Learning State或索引，未stage/commit/push。

执行时间：主要请求2026-10-08T12:44:34Z～12:57:11Z（北京时间20:44～20:57）；root补充RSS核读时间13:03:37Z不是其网络请求精确时刻。准入、两篇必要core及完整六部分日级验收均已获root独核通过，普通待办0；必要日期缺口隔离后不转成全文队列。原108日期/旧完成仅冻结复用，尤其旧Registered/availability组合不作本轮新增公开日期证明。

## 1. 实际来源入口及停止

请求URL、返回状态、实际时间、字节与保存位置在 [入口请求](supplement-fetch-20261008.json)、[必要官方恢复](supplement-fetch-official-20261008.json)、[发现请求](supplement-fetch-discover-20261008.json)、[API尾页](supplement-fetch-tail-20261008.json)、[精确题摘](supplement-fetch-abstracts-20261008.json)、[单次日期恢复](supplement-fetch-dates-20261008.json)。每个name对应本目录 `supplement-<name>-20261008.raw/.txt`；旧有效证据仍保持原件。

| 来源 | 2026-02-26自然日实际检查与停止 | 结果/剩余限制 |
| --- | --- | --- |
| SRC-OPENAI | 新RSS有Feb26 06:00Z Figma、10:00Z PNNL；均为旧有效事件。Feb27 00Z mental-health本次窗外，不改旧处置；Feb27 05:30Z四公告也窗外。RSS既有核心有限排除复用，不扩OpenAI工程全站。 | 该RSS历史段已有限检查；PNNL领域应用、Figma接口联动未披露新模型机制，不增候选；不可取得的旧正文不授机制验证。 |
| SRC-ANTHROPIC | 新Research原HTML166个唯一publishedOn，Feb25 20:02Z deprecation-updates-opus-3属于BJT Feb26；前界Feb23→后界Mar5。实际读完整核心及安全/不承诺/访谈偏差反侧。 | 新增Opus3退休后访问政策事件1；历史目录有限，不保证删除项召回。 |
| SRC-GOOGLE-AI | 新Google Research Feb2026目录7条，Feb17→Feb3读到尾；新DeepMind publications第一页30项，Mar10→Feb15已越过目标日，未打开更早页。Nano旧release已有效，原日期/评分冻结；原release16Z Feb26对应BJT Feb27，不把它再算Feb26新增。 | 无确定新增；Nano原spec版本请求继续隔离，不把当前后修改页面内容恢复成旧版。 |
| SRC-META-AI | Research仍200但仅57字壳，不授0；必要publication page3恢复Apr14→Feb27 VSONAR→Feb26 PAHF→Feb13及更早边界后止。PAHF同家族已官方OAI Feb19上界证窗前；VSONAR Feb27目录日不作Feb26首公开。 | 原Research历史段缺口保留；publication有限段可用，不提升全源覆盖。 |
| SRC-QWEN | 新API40条，extra.date：Feb3 CoderNext、Feb10 Image2、Feb16 Qwen3.5，均窗前；无下一页字段。 | 原目录有限已查，无新增确定事件。 |
| SRC-DEEPSEEK | 新研究主页533字导航；API updates Dec1 2025→Apr24 2026，无目标日API发布。官方站点窄Feb26搜索无新身份，仅辅助。 | dated研究历史段仍受阻；API changelog不替研究零命中。 |
| SRC-MOONSHOT | 新Kimi Blog24旧事件，最新Nov7 2025、尾May29 2024；有限官方Feb26搜索无新身份。 | Feb26 dated历史研究/发布段仍缺，不把旧首页授0。 |
| SRC-TENCENT-HUNYUAN | 首查Research仅4字动态壳；POST publicList实际pageNum1/pageSize1000，totalNum9、全部lang=en；Feb13→Apr23邻界，读到Feb3尾。 | EN9有限目录可止；中文历史Research段没有被EN列表证明，保留需中文dated列表或同日公告的具体缺口。 |
| SRC-ZAI | 新Research15项，Mar15→Feb21→更早边界，旧release-notes有效结果复用。 | 此目录有限段无新增，不扩后续release。 |
| SRC-BYTEDANCE-SEED | type1/year2026/page_token60实际19条，Feb27 CUDAAgent→Feb25 WorldGuidance/FlowPortrait→Jan27；next80实际2条Jan22/Jan20、has_more=false，止。type2/start0实际12条Feb14→更早，has_more=true/next20；实际请求20返回[]/has_more=false后止。 | 目标Feb26无目录新事件；CUDAAgent官方PublishDate日期为Feb27，旧原窗口日期请求保持，不移动原候选。 |
| SRC-BAIDU-ERNIE | 新Blog页1十条May9→Feb6→Nov21 2025，已越过目标日；无须再请求更早页2。 | 有限目录已查，无新增确定事件。 |
| SRC-XIAOMI-MIMO | 新主页Paper8，Mar13→Feb3，旧Blog Dec16 2025；15个Blog导航无date，定点Blog恢复仍旧稿。 | dated Feb26 Blog历史段仍缺，不能授完整0。 |
| SRC-MINIMAX | 新EN12/CN13条目录，Mar18→Feb12/14→Jan27/28边界；Agent TechBlog当前仅Sep22/Sep19两条，旧有效May13材料可复用但无Feb历史段。 | EN/CN目录有限段已查；Agent TechBlog历史删除/变动段不授0，需目标日dated官方历史目录或公告。 |
| SRC-ARXIV | 见下面实际失败/恢复、分页及范围收窄。 | 仅约定主题有限处理；10具名潜力首公开日未恢复，不支持候选、正面Evidence、Books或“无遗漏”。 |

root有限补充[DeepMind RSS原响应](supplement-deepmind-rss-root-20261008.raw)：100items/69499byte；NanoBanana2 Feb26T16:01:50Z=BJT Feb27，本次补充Feb26窗外；其余可见事件Feb19及更早，无BJT26条目。13:03:37Z是root核读时间而非网络请求exacttime。这里只证明该feed有限结果，不授Publications/删除历史全覆盖。

辅助搜索2026-10-08：arxiv“26 Feb 2026” language model/world model/GPU，随后“2026-02-26”2602 language model/“Thu,26Feb2026”agent；Google Research/DeepMind Feb26；DeepSeek/Moonshot/MiMo/Meta Feb26各官方域限定。前几组搜索无返回只记检索受限，不作为阴性证据。Meta仅恢复PAHF/publication3旧身份；Google仅Nano旧家族，不改变其冻结日期。IOAgent具名身份检索恢复作者2025原发表事实（下文）。

## 2. arXiv查询修复与限定发现

四个Advanced主题（model/system/agent/multimodal）确实请求 `date-from_date=2026-02-26&date-to_date=2026-02-26&date-date_type=announced_date_first`。实际返回表单错误 **End date must be later than start date**，同时官方页面说明announcement只支持年月。保存的4份303xx字节响应是错误表单，不是论文列表/0命中，不能授覆盖。

改为两条有界路线：

- DataCite仅发现：`doi:10.48550/arxiv.2602* AND registered:[2026-02-25T16:00:00Z TO 2026-02-26T15:59:59Z]`，分别与model、system、multimodal/agent主题相交。实际306/99/232，451唯一发现；3份meta均单页、links无next。Registered、DOI年月、Updated和Submitted均不当公开日期。宽命中中的quantum/天体/无线通信/传统ELT等标题只作范围外查漏，不逐个题摘/关闭成队列；与原候选、具名记录、原精确题摘比较后只处理相关新标题差额。
- 官方Atom API：12个合同分类中的LLM/language model/foundation model/Transformer/GPU/agent/diffusion/world model，与`submittedDate:[202602250000 TO 202602262359]`相交，仅用来弥补漏术语/分类发现。实际totalResults532；start0返回200、start200返回200、start400返回132后止。API published是首次submission，不据此授首公开。全部仅相关标题查漏；其中延迟到后月的ID和Feb26提交引入大量潜在窗外线索，立即收窄至上面的Feb26有限发现与既有记录交集，不把532变成AB/全文队列，也未扩后周/全月。

旧官方CL/LG/DC分类目录原件只复用本日既有相关身份段的标题查漏，不重新全月逐项AB；旧195精确题摘和218身份的有效判断不重审。新精确v1完整题摘实际17篇；另外旧IOAgent的core仅围绕可能错排与首公开身份定点恢复。

17篇：10项存在下表具体贡献潜力，7项在完整题摘后明确关闭。root实际读全部17完整题摘，收紧21535/21750/21849三项为EX；仅21552/21858决定准入的事实含糊，各读一次必要core后保留受限潜力。无withdrawal/correction/security标记的新潜力项已轻量检查当前官方event页Comments与version说明；版本号变化不触发全revision遍历。ProactiveMobile有Feb26 v2的submission，但无公开日/实质修订说明，不授本日重要修订；请求只限具体v1/v2事件说明，不据此重读所有版本。

## 3. 10项具体贡献潜力与必要日期请求

所有项已读链接精确v1完整题摘及当前官方版本/Comments。最初13具名潜力各仅一次OAI GetRecord恢复，返回version dates、最新header datestamp和announcement月字段（若有），均未给同ID本次事件的具体公开日；其中21535/21750/21849后经root贡献校准关闭，不再保留日期请求，实际13次响应仍保原件。余10项不把这些字段组合成当窗证明，不评分、不全文绕过date、不进入Books，不把必要材料请求当审阅完成。

共同必要材料：同ID精确v1首次公开日期的官方公告/历史列表，或作者/项目原始带日期公开正文公告（必须可识别版本，优于当前回填时间）。对ProactiveMobile另接受指认Feb26重要v2公开事件的原修订公告。只要能确认公开日期即可，不请求时分秒；取得后只重开该身份的日期/贡献及必要证据，不重跑整月或旧108。

| 身份与精确版本 | 完整题摘里的实际潜力（不是证据结论） | 官方v1 Submitted，仅作身份线索 | 本次缺口/重开 |
| --- | --- | --- | --- |
| [Revisiting Text Ranking in Deep Research，2602.21456v1](https://arxiv.org/abs/2602.21456v1) | agent query的web-search语法与ranker训练query错配；固定BrowseComp-Plus corpus、两agent/五retriever/三reranker比较并重写为自然问句，可能修正“dense检索通用最优”的局部选择。 | 2026-02-25T00:18:07Z | 需21456v1同ID具体首次公开日；仅取得后核query rewrite归因/固定corpus边界。 |
| [GPOcc，2602.21552v1](https://arxiv.org/abs/2602.21552v1) | 可见surface prior不等volumetric occupancy；沿camera ray内推Gaussian及training-free streaming fusion改变表示/累计状态。 | 2026-02-25T04:16:54Z | 需21552v1首次公开日；之后核同depth prior对照与不可观测体积假设。 |
| [MIGRASCOPE，2602.21553v1](https://arxiv.org/abs/2602.21553v1) | MI质量/冗余/协同/marginal contribution把retriever选择从单pipeline排名转为互补性分析。 | 2026-02-25T04:19:06Z | 需21553v1首次公开日；之后核MI估计对象、ensemble选择与独立评价。 |
| [Power and Limitations of Aggregation，2602.21556v1](https://arxiv.org/abs/2602.21556v1) | principal-agent stylized模型区分feasibility/support扩张与binding-set收缩，给同模型aggregation何时扩大elicitable outputs的必要/充分条件。 | 2026-02-25T04:23:50Z | 需21556v1首次公开日；之后核理论假设，不把toy reference实验外推一般协作。 |
| [MultiAnimate，2602.21581v1](https://arxiv.org/abs/2602.21581v1) | 单人动画直接扩多人导致identity/occlusion冲突；mask-driven assigner/adapter＋只两人训练到多人测试的组合泛化机制。 | 2026-02-25T05:06:58Z | 需21581v1首次公开日；之后核identity表示、人数分布/occlusion反侧。 |
| [RLHF Reward Shift and Clipped KL，2602.21765v1](https://arxiv.org/abs/2602.21765v1) | generalization拆prompt/rollout采样、reward分布shift及sampled KL clipping误差，改变clipping阈值/数据预算解释。 | 2026-02-25T10:36:17Z | 需21765v1首次公开日；之后核OU近似、泛化界假设及“optimal threshold”范围。 |
| [StoryMovie，2602.21829v1](https://arxiv.org/abs/2602.21829v1) | 正确ground实体仍错对白/关系；script-subtitle LCS对齐监督提供关系grounding的局部对照，可能修正视觉grounding评价充分性。 | 2026-02-25T12:01:05Z | 需21829v1首次公开日；之后核judge/scoring人口和训练数据/预算混杂，不照录89.9%。 |
| [ProactiveMobile，2602.21858v1](https://arxiv.org/abs/2602.21858v1) | latent intent推断与63API可执行序列、多答案可行性人口的主动agent评价，潜力在无显式命令时intent/action正确性分责而非仅新benchmark名字。 | 2026-02-25T12:32:37Z | 需21858v1首次公开日，或指认v2重要公开修订的日期/差额；之后核authorization与多答案evaluator，19.15%非泛用主动能力。 |
| [Hidden Topics，2602.21939v1](https://arxiv.org/abs/2602.21939v1) | 间接list experiment与direct questioning冲突、placebo对照可能揭response framing评价盲点；不先把输出叫真实hidden beliefs或alignment faking。 | 2026-02-25T14:24:47Z | 需21939v1首次公开日；之后核量词/模型采样、placebo和替代解释，不采纳敏感belief实在性。 |
| [Dream-SLAM，2602.21967v1](https://arxiv.org/abs/2602.21967v1) | dreamed跨时空图/未观测结构融合真实观察并影响长程探索；潜力在模型先验、观测状态与planning的融合/失败边界。 | 2026-02-25T14:48:49Z | 需21967v1首次公开日；之后核生成幻觉如何受观测约束/行动反馈纠正。 |

## 4. 分层明确关闭与旧判断定点澄清

以下不是因“小模型/理论/负面”拒绝，也不因为能映射节点准入。日期不影响这些明确贡献关闭，除IOAgent旧发表身份外不追加日期请求。

- [Pseudo-View Enhancement，2602.21535v1](https://arxiv.org/abs/2602.21535v1)：diffusion伪帧双向修复及Gaussian管理是重建配方/领域质量改进，完整题摘没有建立foundation/world-state新机制或适用反证；不能仅因使用diffusion保留。
- [From Words to Amino Acids，2602.21750v1](https://arxiv.org/abs/2602.21750v1)：已有LLM depth inefficiency探测迁到6蛋白模型/3训练objective，未给新通用depth机制或反证；属于当前暂缓的AI for Science，不能借模型层owner引回领域验证。
- [Meta-FC，2602.21849v1](https://arxiv.org/abs/2602.21849v1)：通用图像watermark借meta-learning和feature consistency抗distortion，未关联foundation/生成归属或模型水印新边界，不从watermark关键词升级模型安全贡献。

- [2602.21302v1](https://arxiv.org/abs/2602.21302v1)：单次示范、简化rope模型、QP传播task误差到动作，7种rope硬件迭代/transfer是具体贡献，但题摘未建立模型能力形成/基础策略或通用AI系统新机制；当前是非基础模型控制法在flying knot的场景验证，不从rope结果制造VLA通则。
- [2602.21827v1](https://arxiv.org/abs/2602.21827v1)：α-fraction观测processing time的tight竞争比有理论价值；正文题摘只定义一般单机online jobs，不建立LLM运行时、GPU执行/状态或模型训练关系，不能仅类比调度owner收录。
- [2602.22041v1](https://arxiv.org/abs/2602.22041v1)：多车/机器人轨迹中group causal responsibility解决overdetermination，场景仿真；并非LLM委派、foundation policy或模型驱动planning机制，不能仅有“agents”映射Ch82。
- [2602.22100v1](https://arxiv.org/abs/2602.22100v1)：300 teleoperation demonstrations、force-torque＋fixed camera、五connector几何得到>90%成功率；题摘未给网络/融合选择的成立边界或新的学习机制，具体工业装配BC比较不足改变主线解释。不是因模型规模/机器人排除。

旧 [IOAgent，2602.22017v1](https://arxiv.org/html/2602.22017v1) 定点core读IV-C/VI-F/Fig6：pairwise merging并行层级，四诊断片段＋引用、Llama3-70B同prompt例子中one-step丢stride/引用，而tree保留。该有限例子不能支持原文“全部模型/13片段不能merge”的一般声明，但可有局部表示/聚合条件潜力，不继续用“成熟模块组合”否认一切贡献。

必要OAI恢复有新身份事实：Comments为“Published in Proceedings of IPDPS2025”、DOI `10.1109/IPDPS64566.2025.00036`；[作者2025 Publications](https://aesareen.github.io/publications/)同身份完整题摘与[官方2025会议程序](https://www.ipdps.org/ipdps2025/2025-advance-program.html)列IOAgent。此为旧2025论文后挂arXiv，无当前同窗重要修订说明。关闭本次首次公开事件，保留局部潜力线索，不按2026 arXiv ID重分家族或制造本日采用；原EX记录及其原件保持，补充澄清其关闭依据，未扩2025全文或改变既有候选。

## 5. 新增确定事件的必要审阅

[Anthropic Opus 3 deprecation update](https://www.anthropic.com/research/deprecation-updates-opus-3)：官方Research `publishedOn=2026-02-25T20:02:00.000Z`与文章JSON-LD datePublished相同，属于BJT2026-02-26；页面显示Feb25是原作者日期口径，保留原字段，不以当前检索时间归属。JSON-LD `dateModified=2026-09-09T21:14:42.000Z`；本轮采用当前官方精确版本对历史政策的明确描述，不冒称恢复Feb26原payload。轻量当前官方检查未见撤回/纠错/安全或需改变此受限政策判断的标记，不遍历无变化revision。

核心全文实际已读（Continued access / Respecting model preferences / Where we go next）：正式retired不等所有服务访问立即关闭，Opus3在付费claude.ai继续可用、API可申请；厂商称维护成本约随服务模型数量线性增加，因此暂不承诺每个未来模型同政策。至少3个月每周essay由人工审核/代发，不编辑且veto门槛高；这不是模型自主发布权限。Retirement interview是context可偏的elicitation，作者明确模型moral status仍不确定，不证明模型福利或意识。这里是访问政策事实，不把未披露的可扩展权重保全、风险控制协议或意识判断写进Books，也无性能benchmark/代码复现声明。1+1+2=4，关闭并仅报告，Books新写0。

## 6. 作者检查与独立验收

两项必要core的受限准入：GPOcc §3.2/3.3/3.4 Eq4/5/9沿camera ray从surface depth向volume布Gaussian，借用probabilistic splat并用top1 class confidence作fusion权重、γ<0.5偏新观测，global Gaussian memory可增量维护scene表示；不是action dynamics，top1权重不等校准概率。ProactiveMobile §4.2/Table4使用Gemini2.5-Pro功能等价judge判SR，FTR另评no-action人口；F1 fallback忽略参数/order且不改SR。Think+Rec+Func对Rec+Func的局部SR19.15→7.38/FTR14.77→2.21取舍可修正评价理解，不证明设备真实执行、consent或安全。两篇各一次core，下载/局部准入不冒充必要证据完成；日期仍缺，不评分/Books。实际坐标与[请求元数据](supplement-fetch-clarify-20261008.json)对应 `supplement-core_21552-20261008.txt`、`supplement-core_21858-20261008.txt`，root独核同段后同意受限潜力。

作者检查：17精确v1题摘＋Opus核心说明；10必要公开日未能恢复安全隔离；7完整题摘明确关闭；IOAgent旧发表/局部反侧身份澄清；十四每日入口、失败与真实分页已保。候选差额1，原108不变，总109；全部原候选及连续§4须逐字机械冻结核对。

非作者root已实际读完整六部分差额、14来源stop/失败恢复、17完整题摘（10日期潜力/7EX）、两必要core限定及Opus当前版本界限，DAY通过；具体独立验收以本日README §6为准。本文件不把作者自查写成独立通过。其他日期、Weekly、共享Books和巨大既有dirty均未触及。
