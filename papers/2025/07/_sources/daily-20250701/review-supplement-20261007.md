# July01补查首批独立校准：25题摘与ERNIE

复核者：Bernoulli（本轮分工独立非作者，此前作者工作为Sep01）；本轮作者：root，非原jul01_author。实际本日上下文检查点2026-10-07T18:21:26+08:00；本批裁决检查点18:26:56+08:00。仅写本文件，不代作者修改README/supplement、Books、State或index。

**本批结论：未通过（FAIL，有3处普通写回差额）。** 25题摘贡献校准建议由作者20P/5C改为**21个日期待核潜力/准入未决、4个贡献关闭**；另修Ella题摘误述，并落实已见撤回/重合标记。其余具名处置可限定通过，ERNIE新增自然日事件、2+2+2=6的受限标准审阅及Ch23具体已有覆盖/No Change为**单项PASS**。这是首批局部准入/证据/Books校准，不是全DAY；root十四源仍在整理，未审范围及全日报实际写后结论待后续DAY包。

## 1. 当前authority、窗口与真实读取范围

独立切July01重读main当前AGENTS、研究合同、Report合同、Sources使用说明/每日组/arXiv、Prompt、ROADMAP与State本日路由；实际读取[作者supplement](./supplement-20261007.md)和[README开头](../../01/README.md)，仅为窗口与旧候选事实定位，不继承旧整日通过。原精确窗口`2025-06-30T09:00:00+08:00 ～ 2025-07-01T09:00:00+08:00`及原候选0不变；本轮新增按2025-06-30完整自然日，原08:00/09:00门限不能排除本次新增同日事件。State只作路由，不改或用年度数量代替验收。

从本日五份Advanced.raw实际抽取并完整读取下表**25个唯一身份的题名、完整abstract-full、可见comments及提交/首公告月份字段**，覆盖全部20原P和全部5原C，不用作者摘录替代题摘。此处读取的是官方检索响应中的当前摘要，不声称25个exact-v1事件页或方法/评价均已读。原20P中安全、评价/设计反证均逐项核必要反侧；四普通关闭也全读，并非抽检。

仅对Semantic Privacy SoK关闭含糊定点补读[精确v1 PDF](https://arxiv.org/pdf/2506.23603v1)的§1定义/式(1)(2)、§2 gap/比较表、§3.3、§4保护条件及§5.1量化需求；未审完整参考文献、所有引用原论文或复现。v1 HTML404后PDF可读，不能包装为必要全文不可得。当前v2 abs身份/版本及HTML入口也可读，但本次必要core裁决只据v1，不借v2倒填。

另完整读本日[ERNIE官方Blog文字原件](./supplement-20261007/ernie-release.txt)，核raw日期/核心；实际读Ch23第367～416与965～1012行，包含指定391～393、984～993及邻接。未读取图像benchmark的像素/逐项数字，未读链接技术报告、仓库实现或复现实验；这些不支持本次性能采用，也未被列为普遍附件队列。

本次新联网仅限SoK必要core及已见标记的官方abs：2506.23603 current/v1 HTML/v1 PDF/v2 HTML、2506.19433、2506.19481、2502.07928。返回后实际钟检查点18:24:27、18:25:35；不是重新抓取五Advanced的HTTP起止时间，不写入/覆盖原件。无catchup，无其他日扫描。

## 2. 有界入口与计数核对

独立用标准HTMLParser解析五Advanced.raw及对应request JSON，不依赖作者手算。原请求checked UTC区间为10:03:51.453812～10:03:58.045336，各HTTP200/returncode0，只有checked字段，不补造结束钟。

| 简称/原件 | 实际查询与停止 |
| --- | --- |
| M：[model](./supplement-20261007/arxiv-advanced-model.raw) | all=`"language model"`，1～50/3520，Next start50 |
| S：[systems](./supplement-20261007/arxiv-advanced-systems.raw) | 上述短语AND inference，1～50/575，Next start50 |
| T：[training](./supplement-20261007/arxiv-advanced-training.raw) | 上述短语AND `"reinforcement learning"`，1～50/307，Next start50 |
| V：[multimodal](./supplement-20261007/arxiv-advanced-multimodal.raw) | 单一all查询值为`"world model" OR "vision language action"`，1～50/136，Next start50；不把输入的OR字样自行认定为两个独立召回集合 |
| A：[agent](./supplement-20261007/arxiv-advanced-agent.raw) | all=agent AND memory，1～50/91，Next start50 |

共用computer_science=y、include cross-list、announced_date_first、size50/start0、首公告倒序。实际Query声明范围为**2025-06-01～2025-07-31包含首尾**，不是06/30单日。所有五组均止第一页，Next未取；上下重复Next链接不是另两页。没有把3520等月级总命中或Next当必读队列。

独立重算250次返回、231唯一ID；与旧[SCREENING](./SCREENING.md)身份交集55，新增月份线索176。25表均在这176内、与旧集合交集0；余151只是未逐项裁决的月级库存，不授窗外、关闭或未审全文待办。25条均首公告June2025、v1 submitted June30，前者缺具体日、后者不等于首次公开。选择submitted June30只是本批查漏优先级，不授权排除其他日期的潜力。本次不验收全来源召回或单日arXiv覆盖。

跨查询重复的TTA-VLM/Goal-VLA全文本在去除检索高亮引入的空白后相同；完整25字段无缺项。这个机械提取核对不是250项语义阅读或精确版本证据。

## 3. 全25项逐项独立校准

P只指贡献潜力/准入未决的保留权限；具体日未成立，不评分、不列确定当窗候选、不进入Books。括号为上表原件与1-based结果序号，便于定点复查。本表包括所有原P和5C。

| 身份/位置 | 裁决与具体采用边界 |
| --- | --- |
| 2506.24019 Ella（A1） | P维持，理由须修：name-centric semantic与spatiotemporal episodic memory分工可改变记忆接口；摘要明确15-agent长期活动后有unseen controlled evaluations，不是未见控制任务验证。协议/对照未读，仍不授普遍自治或因果收益。见R2。 |
| 2506.24120 Data Uniformity（M3） | P：minimum pairwise distance数据选择与GD/近似误差假设连接训练效率；需核数据度量、定理条件和预算，不授所有任务越均匀越好。当前9月修订不当v1。 |
| 2506.24119 SPIRAL（M4） | P：自博弈课程与role-conditioned advantage对应多角色baseline压力；不将游戏奖励验证、八任务宣传升级通用推理迁移。当前3月2026稿另隔离。 |
| 2506.24117 Biblical Hebrew（M5） | C维持：成熟embedding与cosine/Wasserstein用于已知古文本平行检测比较，题摘未提出主线组件机制、评价混杂或受控失效新条件；非因古语言领域或benchmark名称排除。日期不另追。 |
| 2506.24106 Representation Dispersion（M6） | P：dispersion用于无标数据难度/层选择及push-away训练干预；相关性与干预收益分开，不能把proxy当语义能力或统一因果。当前2026稿不倒填。 |
| 2506.24086 MotionGPT3（M8） | P：continuous latent、双流共享attention、generate-then-align对应量化误差与跨模态干扰；训练阶段/参数/预算须分账，不授无干扰或2x/4x普遍收益。 |
| 2506.24056 Logit-Gap Steering（M9） | P，必要安全反侧：首step refusal/affirmation margin及in-distribution suffix挑战perplexity过滤；gap优化与ASR相关有内生性，威胁权限/搜索预算/防御控制未核。2026 camera-ready不当2025成果，不采用ASR或速度比。 |
| 2506.24006 Word Problems（M12） | P，评价反侧：s-problem题库构念与真实context reasoning分离可改变模型评价；教育使用愿景不作贡献，PISA/GPT-5及当前8月稿不回填v1；不授全部LLM不会理解。 |
| 2506.24000 TTA-VLM（M13） | P，必要评价反侧：统一协议下accuracy与calibration/OOD/stability分离、training-time tuning交互；方法数量/榜单不是准入理由，不授所有TTA无价值。 |
| 2506.23998 Auto-TA（M14） | C维持：临床叙事主题分析的专用角色pipeline/可选RLHF，题摘未披露新执行、训练条件或可复用失败对照；不能因医疗或组合标签本身关闭，亦不授免人工编码的可靠性。 |
| 2506.23982 StyleDrive（M15） | P收窄：单一“正确驾驶”评价不能承载人类偏好差异，rule/distribution/VLM/human标注接口有具身评价潜力；不是仅凭VLM标签收整类驾驶应用。不授真实驾驶安全/偏好因果收益，实际标注方法和可比协议待证据。 |
| 2506.23979 TaP（M16） | P：taxonomy控制多语言偏好数据组成对应覆盖/数据生产约束；需核生成/筛选成本和等预算，不由180倍数量比较授机制因果或普遍最优。 |
| 2506.23951 ClassifSAE（M17） | P：classifier head与activation-rate sparsity及外部encoder解释指标提供可检验干预对象；不能把文本分类局部指标称语义真值或直接采用causality宣传。 |
| 2506.23921 Trilemma（M23） | P，必要设计反侧：probe transfer、真/假不对称、第三信号及MIL/conformal接口挑战单一veracity方向；不授“neither”普遍正确性、可迁移truth oracle或内部知识证明。 |
| 2506.23919 Goal-VLA（M24） | P：goal-image→object-pose→低层控制及Reflection-through-Synthesis改变VLM/action接口；合成图像自校验不等真实环境验证，不能授zero-shot全部embodiment或安全执行。 |
| 2506.23906 Segmented Operations（M25） | P：MMV-RAM计算假设与segmented scan/sum映射矩阵单元、Ascend case study服务AI kernel；理论假设/矩阵向量资源与端到端成本须核，非LLM主模型或硬件论文不构成排除。 |
| 2506.23903 Ultrasound（M26） | C维持：DINO/SAM2+LoRA的多器官适配及15/3数据划分支持领域泛化测试，题摘未给可迁移表示/适配新机制条件或重要失效反证；非因医疗/小模型关闭，不否定全文学术价值。 |
| 2506.23825 Flash-VStream（M32） | P：低容量temporal context/information-density指导高容量spatial retrieval，支持质量/缓存/延迟取舍；长视频理解不自动等真实流式端到端响应，SOTA/实时保证未核。 |
| 2506.23815 Education Assessment（M34） | C维持：Bloom/Constructive Alignment与高校许可/教师培训建议是教学评估政策，不是模型能力evaluation或执行机制反证；不能混同学生评估和模型评估。 |
| 2506.23749 Program Repair Survey（M38） | P：控制逻辑所在位置的独立编码维度及benchmark variant/fault-localization protocol audit可改变Agent设计/比较权限；不因survey关闭，也不按66数量准入。当前2026摘要不证明2025已有完整audit。 |
| 2506.23743 Positional Bias（M39） | P，评价反侧：翻转选项、控制uncertainty，区分Preference Fairness/Position Consistency；局部任务不可授bias普遍指数规律，需核uncertainty构造与替代解释。 |
| 2506.23670 TinyWave（M47） | P：hidden/attention/softlogit逐层蒸馏与interleaved speech压缩可核质量-执行边界；不由2B、3x或93～97%授权真实时延/commodity部署，当前10月稿隔离。 |
| 2506.24113 Epona（V1） | P：temporal dynamics/video diffusion分解、chain-of-forward与trajectory接口面对AR误差/定长分布约束；FVD不是planner safety，分钟生成不等真实闭环，多模块收益须分离。 |
| 2506.23603 Semantic Privacy SoK（S8） | **C→P，带中心定义争议。** necessary v1 core披露具体保护量与威胁/阶段边界，不应只按“分类/无新保护机制”关闭；不授其等价性、评级或保护有效性。见R1，日期未证仍不评分/采用。 |
| 2506.23601 SemDiD（T5） | P：embedding方向、跨group排斥、位置去偏对应语义而非词法diversity及BoN/RL数据接口；quality threshold/优化定义/解码预算待核，不授保证或作者速度/精度数字。 |

## 4. 三处具名FAIL差额与可复用范围

### R1：Semantic Privacy SoK关闭重开

[v1 PDF](https://arxiv.org/pdf/2506.23603v1)§1式(1)(2)将推断量偏差和posterior/prior KL写为等价保护条件；§2/Table2及§4/Table4给具体威胁/阶段/保护比较。准入应保留保护对象/量化合同的潜力与中心争议，而非要求综述必须提出新防御算法或新实验才有贡献。评级/引用尚未独立重编码，不授新安全保证。

**本复核的数学反侧，不是作者实验：** 仅均值约束不足以推出分布KL约束。取语义变量值域`{-1,0,1}`，prior=`(1/4,1/2,1/4)`，posterior=`(1/2,0,1/2)`，两者均值为0；参考量R=0时式(1)左端0可过δ=0，但KL(posterior||prior)=ln2，不能过ε=0.1。这是检验其所述等价性缺条件的示例，不否定所有信息增益隐私定义，也不将其中心争议降分/删条替代审阅。

作者普通写回：2506.23603撤回原C，改日期待核潜力/定义争议，初批建议21P/4C；不增加身份、评分或正式候选。必要日公开或原版本精确修正/假设到达后定点重开；当前不比较/写Ch72正文，不授Books已有覆盖。HTML404不能阻挡已可读PDF的本次定点判断；必要core已由非作者读完，不挂为待作者重新泛读全文。

### R2：Ella题摘误述修正

作者写“未见控制任务验证”，但A1完整摘要明确长期15-agent社会活动之后有unseen controlled evaluations。这不是没有控制评价，而是本批未读其协议、对照、预算和归因。P与发现分母维持，只纠正必要事实和评价权限；不因修正而采用普遍自治，不新增全文队列。

### R3：已见当前标记须具名落盘

对五响应250次comments做机械信号筛查，只为检查已见相关纠错；不是250条贡献初筛，也不是完整版本史检索。发现以下两项位于原176/151库存范围，虽不在25表，也不能因未选表而忽略已见标记。本复核已轻核官方当前页，无需作者重抓月份页：

- [2506.19433 Mem4Nav](https://arxiv.org/abs/2506.19433)：官方当前v2明示withdrawn，版本史2025-10-10撤回，说明调查潜在学术不端、作者自愿撤回。只记撤回排除，不裁定不端已成立；不评分、不采用、不进Books、不追公开日让旧版入选，No PDF不是普通访问故障。摘要仍可见不使其有效。
- [2506.19481 Haskell refactoring](https://arxiv.org/abs/2506.19481)与[2502.07928](https://arxiv.org/abs/2502.07928)：前者admin note为text overlap，当前均v1、相关作者有交集而非完全相同；两题摘都为analysis/refactoring/verification等角色与任务指标。重合不是撤回、抄袭裁决或有效旧审阅去重。定点完整题摘足以本轮贡献关闭：未见超出任务pipeline/指标的新执行机制或受控失效边界；不因Haskell领域排除。保留关系标记，不为不采用的明确关闭项泛读两篇全文或追不影响处置的公开日；若以后有具名新机制/纠错才定点重开，不扫描二月。

作者须把这两个已见身份的处置加入自己的原始记录和最终报告必要边界；它们已计入176，不能加发现数或加进25题摘表假称此前已读27。本复核另读两标记页及重合另一篇，实际角色/范围分账。本次未发现25表自身有撤回/重合comments，但不授全网/全部版本无标记。

除R1～R3外，20原P的受限保留、其余4C的具体关闭及当前版本/年月隔离通过。这些独立结果可复用；后续只核作者具名差额，不能把单层误述或改判推倒其余有效题摘校准。

## 5. ERNIE单项PASS：自然日、标准审阅与具体已有覆盖

### 日期与评分

[官方Blog](https://ernie.baidu.com/blog/zh/posts/ernie4.5/)本日新取request为2026-10-07T10:04:31.751767+00:00，HTTP200；raw可见2025年6月30日，`article:published_time=2025-06-30T00:00:00+00:00`，JSON-LD datePublished/dateModified亦同。按日期即可归新增自然日2025-06-30；旧小时窗的08:00边界只对原轮成立，不排除新增自然日，不移动原候选0或其他旧归属。

**准入/2+2+2=6/受限标准审阅PASS。** 评分对象是本次公开架构路线：全共享容量易干扰、全隔离弱迁移→shared与modality-specific参数并存及语言到多模态continued pretraining→容量共享/专用分工与训练演进取舍。Design Delta2、System Reach2、Durability2可接受；不是将MoE名字、47%MFU、机构权威或当前Books覆盖计分，也不因已有覆盖降低材料评分。

### 标准证据的权限

完整文字披露共享/专用容量和联合训练、高层orthogonality/token balance、多维位置、异构并行/负载平衡、PD角色、后训练及工具入口；可采用的是厂商公开设计路线，不是机制有效性已经独立实证。无精确eligibility mask/正交loss/负载算法/PD转换协议，不将其名字扩成实现保证。

文字有多模型/benchmark比较，却没有可归因的shared-vs-specific/continued-training配对消融，不授文本无遗忘、near-lossless量化、SOTA或端到端吞吐。并行/FP8被提及不等MFU测量的具体hardware/precision/batch/长度/总预算已绑定；实际硬件型号、配对预算、并发/SLO/评价细节均未在本批采用命题中核验。图像表未读取，不使用其孤立数字。官方文字范围内机制、利益主张、成本缺项与边界已足以支持这个受限6分标准结论；不授技术报告深审、artifact核验、复现或生产性能。

### Ch23具体已有覆盖/No Change：PASS

唯一owner为`MULTIMODAL-REPRESENTATION`，不是Ch21通用Top-k。实际读取[Ch23融合接口](../../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md#fusion在哪里让模态相遇)及其邻接：

- 当前第391～393行已承载modality eligibility与parallel shared MLP，分开资格、权重、active budget、transfer及无遗忘权限；不是泛泛“多模态已写过”。它的具体MoST softmax/mask次序不冒充ERNIE实现。
- 第984行与991～993行明确全共享/高资源挤压、shared interaction与modality-specific FFN/路由容量的共存，以及数据复杂度、token预算、通信/校准成本、分布漂移/硬实时单模态条件与late fusion回退。第986～989流式时间身份和第996～998梯度更新权为邻接不同机制，未被拿来证明ERNIE内部实现。

这些现有具体论点已承载本次拟保留的容量分工与共存条件。Blog未给可核新归因/失败边界来修正它们，故当前声明范围内已有覆盖/No Change通过，无必要Books修改；不是将所有ERNIE训练/量化/PD细节授已有覆盖。orthogonality等只高层提及且未采用为长效机制，不请求按名写新段，不触发共享写入。此处只读现有正文，不改变书稿或声称ERNIE已提供以上全部限制的实验。

root可依据此单项结果继续其本日作者工作，不等无关月库存；后续DAY检查作者实际写入的新增事件日期、6分/标准/已有覆盖与边界即可，单项PASS不等本日完成。

## 6. 精确交还与后续DAY边界

**普通可执行交还：** root只落实R1 SoK C→P/21P4C与中心定义争议、R2 Ella评价事实、R3撤回/重合具名处置；复用本次已读core及ERNIE单项结果。root正在做的Seed locale/十四源整理、报告六节与最终DAY仍属作者正常工作，不能称外部故障，本复核未越权验收它们。

日期待证潜力不评分、不入当窗确定候选/Books，不作零发布或无遗漏；需官方日announced/list的ID/事件映射或可信原作者首公开记录后定点恢复必要精确版本。月公告/submitted/一般日程不补造日期，当前2026修订不能回填2025。未读的方法/附件是未审范围，不是泛称访问失败；151库存/五组Next、全月和全部分类不变强制队列。

当前只完成本批局部独立校准，**不授全DAY或年度新增验收数**。原有效审阅/旧候选不动。后续DAY包到达，先核这三处实际写回与全日六节/来源停点、逐候选/Books终态，已通过内容复用，不重审25/ERNIE或广月库存。本文件不改作者结论，也不预授修后通过。

写入范围仅本文件；不stage/commit/push，不执行Git写操作，不改README/Books/State/index、作者记录/原件或其他日期。既有AM/A/未跟踪与并发修改保持。落盘检查另记，不用结构校验替代上述语义结论。

2026-10-07T18:31:36+08:00落盘检查：本文件25行/25唯一身份、4个C维持与1个C→P一致；10个本地链接目标存在、围栏闭合、尾空白0，限定只读diff无诊断。当时保护性摘要129个对象中116未变，包括Ch23、July01作者README/supplement、五Advanced及ERNIE原件、当前合同和索引；13处外部并发变化为State与其他Books。18:33:42再核为115未变、14处外部变化，新增作者README并发写入；本复核没有写入、撤销或覆盖这些变化，Ch23及本批来源原件未变，不据其他Books变化作验收。

**实际V3结果：未通过，退出码1。** 作者README第48行审阅结果写为`待审阅（作者已读完整Blog与必要反侧，待独立核）`，校验器报`候选审阅结果无效`；这是作者新增字段的普通接口修正，不是外部隔离或本批语义反证。root应将说明移出枚举字段，并依据本文件ERNIE单项PASS同步`标准完成`及受限`已有覆盖`结论，不自授全DAY通过。本复核不修改作者README。三项语义差额仍为FAIL R1～R3，ERNIE单项PASS；交root正常写回后定点复核，等待后续DAY包。

## 7. 实际写后与DAY裁决（2026-10-07 18:46）

复核者：Bernoulli，本轮独立非作者；作者root。**本次DAY结论：未通过（FAIL，仅余R4来源数量同步）。** R1～R3实际写后、ERNIE候选/受限标准证据/具体Books决定及六节隔离均通过；不是因必要论文未审、月库存未清或外部材料未到而不通过。下述一处现稿事实差额属于普通可执行写回，未完成前不授日报完成。此前首批FAIL及旧机器结果保留为历史，当前机器结果以本节为准。

### 已解决差额与六节实核

- **R1 PASS：** supplement当前25表及表后说明已为21日期潜力/4关闭，SoK撤销按“分类/无新算法”关闭，保留保护量合同潜力与均值/KL等价性中心争议。README第1、2、5、6节对应同步；日期/版本未决不计正式候选、不评分、不采用为安全保证、不进Books。复核者数学反例未冒充作者实验或root全文阅读。
- **R2 PASS：** Ella行明确unseen controlled evaluations；未读的是协议、对照、预算和归因，不再称没有控制验证，不新增全文任务或普遍自治采用。
- **R3 PASS：** 两库存内身份在supplement与README第5节具名处置，Mem4Nav只作官方撤回排除、未裁定不端已成立；Haskell text overlap不作撤回/抄袭/有效审阅去重，两当前题摘的贡献关闭复用本复核结果。176分母、25表身份及旧候选0不变；151库存中2项具名处置后，其余149未逐项裁决，不增加新发现数或伪造27题摘阅读。
- **ERNIE PASS复用：** README第3节实际为2025-06-30、2+2+2=6、`标准完成`、`MULTIMODAL-REPRESENTATION` Ch23已有覆盖；第4节承载精确所读官方Blog、具体容量命题/邻接、未披露公式与性能权限，第5节不再把旧小时门限列为新增事件缺口。原候选0保留，本轮新增唯一确定家族1、受限标准及Books决定完成1、Books写入0成立。既有Ch23覆盖未变，不重复读取Blog/图像/报告/代码或书稿。

实际读当前README六节及作者supplement写回。开头保留授权补充自然日、原窗口和原0候选；第1节漏斗数量不混月库存；第2节14每日ID无缺行、未加入Weekly或无触发按需全站队列；第3节唯一确定候选为ERNIE；第4节TM/L0原证据仅作隔离恢复资料、不转正或先授Books差额；第5节将普通窄核与外部保留分开；第6节具名Bernoulli且保留原轮root对jul01_author的有效独立范围，未以本轮root自审代替本复核。进行中/未通过现状没有提前计日级通过，最终元数据只能依据实际最终裁决同步。

### 有限来源范围、实际阅读与外部隔离

本轮不联网、不重新抓源、不重读未变25题摘或176库存。复用§1～5的全25准入/安全反侧、必要SoK v1 core、两当前标记及ERNIE单项检查；复用原轮有效18题摘样本范围，不声称这些均由Bernoulli本次新读或把样本扩大为全部旧SCREENING验证。保护性只读摘要比对的21对象（五Advanced的raw/txt/request、ERNIE三原件、SCREENING、baseline、Ch23）全部与首批核验时一致；摘要比对不是新的全文阅读。

本次新增只读本日已保存的有限来源请求元数据、分页/目录日期与必要新增事件核心：OpenAI RSS机械核1251项及唯一June30 Economic Blueprint；Qwen/Kimi/MiMo/DeepSeek所列邻接日期；Seed四US响应的实际数组、PublishDate及next token；Hunyuan9条日期；Z.ai两页目录；DeepMind第2页30个列表身份/日期；MiniMax英中文当前列举边界；Anthropic Citations文字第85～130行。Citations正文明确June30是Bedrock可用渠道更新，句子分块/引用接口不能重算为该日新机制；15%及0%等宣传未采用。Google HOV核心与June Blog的web恢复范围复用root具名实际记录，本次未新读其web全文或把curl超时原件称为成功正文。

Seed实际papers0/20为18+20条、total94、next20/40；Blog0/20为18+18条、total45、next20/40，跨目标邻接日期与作者记录相符，不以has_more=true要求全部库存。Hunyuan返回9条均2026，不能将HTTP200授2025历史覆盖；Z.ai首页下界12/09、`?page=2`下界12/07，没有目标六月段；MiniMax当前精选入口缺目标段，不能凭跨年上下界排除June30发布。DeepMind为精选目录，7/1→6/26邻接成立，非Google Publications首公开清单。实际有限停止本身不支持全组织/全学科无遗漏。

14源均已获得处理与明确限制，现稿7行`已检查`只指所列入口，另7行`受阻`有外部终态边界；不是14源正面Coverage通过。外部隔离可终态保留且不阻塞其他工作：

- TM、L0、旧SCREENING具名潜力及新21潜力缺官方具体首次公开日/必要事件身份；恢复条件为官方日公告或准确ID映射、可信原作者首公开正文日期，只恢复落窗家族精确版本与必要采用命题。submitted、公告月份、一般日程或后修摘要不能替代；SoK另须原版本假设/修正澄清中心定义争议，不先作安全保证。
- Anthropic/Meta历史Research、Google Publications本日首公开目录、Hunyuan旧“全部”、Z.ai/MiniMax目标段，以及Seed未列资产/locale口径限制，均不支持全源零发布或完备召回。可接受具名本日官方历史段/正文日期或当期官方快照，材料到达只重开相应来源/身份，不把未列全库存作为普通强制队列。
- 149新月库存没有逐项裁决，不授窗外或贡献关闭；撤回与已明确贡献关闭的身份不追不影响处置的公开日。所有日期/来源/中心争议保留项不作候选正面证据、评分、Books、无遗漏或性能/安全保证。仅未读但不依赖的附件不是必要正文故障。

### R4：仅需校正DeepMind实际返回数

README第27行仍写`DeepMind真实page/2/25条`，supplement第11行仍写`第2页（25条，265 publications目录）`。实际[已保存raw](./supplement-20261007/deepmind-pubs-p2.raw)有**30个`list-group__item`、30个Publication链接、30唯一身份**，首条A Pragmatic View of AI Personhood（2025-10-30），末条QuestBench（2025-03-28）；所读[文字副本](./supplement-20261007/deepmind-pubs-p2.txt)对应30条。目录总量265、页码2及7/1→6/26的目标邻接未变。

root只需把上述两处数量25同步为30，保留精选目录/首公开缺口、原阅读与停止边界，不额外抓页、不将新增5个列表身份变成论文题摘队列，不改变候选或评分。该返回数量错误不能以V3通过掩盖，也不是外部隔离。本节已提供真实实际范围，但不代作者改正式报告自包含的错误数量。

机器实际顺序：本轮开始时状态字段附说明触发枚举错误；作者随后改为纯`标准完成`，同标题同URL对应又触发一处标题错误；作者随后同步第4节标题。**18:45复跑V3退出0，检查1份V3通过**，仅证明现稿接口一致性。限定`git diff --check`无诊断，README本地链接目标无缺失、六标题/14唯一每日ID齐全。机器通过不替代上述R4事实修正或本日语义裁决。只写本独立文件、不改README/supplement/Books/State/index，不stage/commit/push；旧review与原件保留。

精确停点：R1～R3/ERNIE/六节隔离已PASS，**DAY仅剩R4两处25→30写回后定点核**；没有再读25/176、复抓源、Books写入或跨日任务。修正到达后复用本节其余有效判断，只核两处实际数量与最终机器/限定diff结果，再给最终日级通过；未修正前不计验收日数。

## 8. R4窄写后与最终DAY PASS

复核者：Bernoulli（独立非作者；本轮作者root）。实际检查时间2026-10-07T18:54:29+08:00。只核README第27行与supplement第11行，两处均已将DeepMind第2页25改为30；目录总量265、页码2、7/1→6/26邻接及有限精选范围不变。R4解决，不重读其他来源、25题摘、176库存或未变化候选/Books正文。

**最终日级结论：通过（DAY PASS）。** 复用§7已通过的R1～R3、ERNIE唯一新增候选的2025-06-30自然日/6分受限标准审阅/Ch23具体已有覆盖及六节终态隔离；原候选0不动、新增候选1、相应证据与Books决定完成1、Books实际写入0。当前没有未处理的研究、来源扫描、筛选、候选审阅或Books修改普通工作，最终作者元数据可据此具名裁决同步，不再挂非作者复核待办。

日期身份/原版本必要证据、SoK中心定义争议、具名历史目录不可恢复与未列资产范围，继续按§7精确恢复条件隔离；不进入正面证据、评分或Books，不支撑全源Coverage/Evidence通过、无遗漏或性能/安全保证。149未逐项裁决月份线索不变强制队列，撤回/贡献关闭处置不因通过而转正。材料到达只定点重开受影响身份/来源。

本次实际复跑V3退出0、检查1份V3通过；限定三文件`git diff --check`无诊断。机器结果只作接口一致性，日级语义结论依据具名独立核。写入仅本独立文件追加本节；原轮review与本文件历史FAIL保留，不改作者README/supplement、Books、State、index或执行Git写操作。July01至此交还root同步，不自动启动July02。
