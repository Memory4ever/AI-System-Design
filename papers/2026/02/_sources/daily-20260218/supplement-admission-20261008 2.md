# 2026-02-18 增量来源补查：准入与停止记录

执行日期：2026-10-08。新增检查窗只为北京时间2026-02-17完整自然日。原09:00窗口、78候选行/日期/评分、有效Source与Books判断不变，原件见supplement-baseline-20261008.md。没有读取Weekly反推、没有移动旧材料、没有stage/commit/push。

原件保护纠错：初始baseline误存了终端截断显示，错误receipt保留为supplement-baseline-truncated-receipt-20261008.txt而不作为冻结依据。按仅有的本轮插入边界恢复完整原文后，与只读git index原完整冻结版逐字核对：82943bytes完全一致；没有修改index。现在baseline有78原候选行/连续§4，与当前README的旧78行/连续§4均逐字一致。错误显示receipt不冒称原始文件。

## 有限范围与实际停止

读取当前AGENTS、RESEARCH_CONTRACT、RESEARCH_SOURCES使用说明/每日组/实际触发、REPORT_CONTRACTS、Prompt、ROADMAP与相关LS checkpoint；只加载本日材料。每日14源均处理，不扩每周组。官方目录先看当前入口，再按Feb17与模型/训练/推理/多模态/Agent具体主题有限辅助检索。西方/东方分组查询及原响应分别在supplement-official-west、topics、official-east1、official-east2、daily-entries与entry-body0/1/2文件。当前目录不是历史快照，空响应和无搜索命中不作为历史零命中。

arXiv的宽标题backstop来自本日旧929库存，排除旧候选后有223个标题线索；这只是标题入口，不是223项完整题摘初筛、不是当天223篇、也不形成逐项必审队列。发现入口过宽后缩到14个具有具体机制/纠错/表示反侧线索的精确v1题摘，未逐分类扫全库。实际14个完整原始题摘已保存；KernelBlaster abs cache miss，改为官方精确HTMLv1恢复。有限主题补检结束于supplement-final-narrow；没有catchup90d、月份/年份目录遍历、邻号推日期或精确时刻追查。cs.CV与cs.LG的2026-02-17单日catchup各一次失败cache miss后停止（supplement-original-recovery），未扩大窗口。

跨日只rg这14个精确ID的README作去重，没有命中当日有效候选；只读取本日报告旧事件与MapTrace旧稿的必要增量比较，不借其他日或Weekly候选扩池。

## 实际题摘准入结果

14个新arXiv家族：11潜在贡献但必要公开日尚未核、1明确窗前、2贡献关闭。另外Google MapTrace博客/旧稿同一家族与RosettaTrace各关闭1、OpenAI chatgpt-4o-latest旧公告执行事件关闭1，本次共5个具体贡献/事件关闭。另Anthropic Opus4.6重要评价更正1个独立日期冲突保留。没有确认新增当窗候选，没有新增评分或Books写入；不是“零发现”。

| 精确家族 | 实际贡献判断及边界 | 必要原件/决定核心 |
| --- | --- | --- |
| 2602.13303 Spectral Collapse | 潜在：source/target频谱差使DDIM反演latent不等isotropic Gaussian；OVG在结构梯度null-space恢复幅度。只保留通用反演条件，不靠microscopy应用准入，不采用实验收益 | new-abstracts1精确v1完整AB |
| 2602.13357 AdaCorrection | 潜在：逐timestep轻量cache有效性信号，fresh/cache自适应修正drift而非静态reuse排程。未核性能 | new-abstracts1精确v1完整AB |
| 2602.13987 ATTest | 潜在：CASE块failure定位、block_limit与analysis_plan局部重写，保留已验测试；撤回“七阶段组合无增量”的初判。分支覆盖非数值正确性、整体对比非该机制单因果消融 | new-abstracts1；attest-decision原PDF pp1–4/III.C/IV/Fig2/V |
| 2602.13993 E-DiT | 潜在机制成立，但作者repo News明确2026.2.15 Paper released，补充窗前关闭；不移动别日。机制为样本条件block depth/MLP width/router-driven cache联合控制 | new-abstracts1；project-date repo News |
| 2602.14236 Sali-Cache | 潜在：光流时序冗余与显著性空间信号，在attention前决定memory allocation；不是只报压缩榜。2.20x/100%代理尚未核，不采用质量/正确性保证 | decision-cores第3节精确abs v1完整AB L16–18 |
| 2602.14293 KernelBlaster | 潜在：profiling performance-state知识库将跨task/hardware实测rollout转入后续搜索策略，in-context更新而非weight训练。AB与intro level3数字冲突，不采用性能；current repo不证明当日已放code | original-recovery第3节精确HTMLv1题摘 L68/75后；author-artifacts作者repo |
| 2602.14302 Floe | 潜在：明确token-wise cloud概率/edge私人context分工与超时τ强制w→1回退本地当前token；rank memory/LUT deadline为相关接口，非联邦/LoRA名词组合准入。共享生成prefix、概率API可得性、privacy/strict real-time保证未核，不采用 | decision-cores第4节精确abs v1完整AB；floe-control IV.C/D L305–326 |
| 2602.14490 MoSLoRA | 潜在：heterogeneous geometry experts按input路由，含manifold switching成本/curvature stability问题。不是2024同名Mixture-of-Subspaces repo，未混用旧身份 | final-decision-cores第1节精确abs v1完整AB L16–19 |
| 2602.13530 REMem | 潜在：relative→absolute时间绑定，fact point/start/end qualifiers且不覆盖历史矛盾；find_entity_contexts提供时间operator/order/aggregation，具体改变事件检索接口，不靠episodic重命名 | new-abstracts2完整AB；semantic-core3 §3/Table1 L103–124 |
| 2602.13562 ASCL | 潜在：consult safety rule成为policy action，IFPO逆频率advantage重平衡credit。未采用安全/utility实证保证 | new-abstracts2精确v1完整AB |
| 2602.13671 MASFly | 关闭：定点§3.2的query/need cosine加权SOP检索及§3.3 feedback/agent replacement+监督周期，未识别区别于通用RAG/SOP/Watcher recipe的新恢复状态、已验证成果保留或effect边界。不是因Agent主题、缺少全文或无实施而排除，不追不影响处置的日期 | semantic-decision L110–176；semantic-core2 L165–182 |
| 2602.13855 AAR | 关闭：PCov trace fraction、PSnd NLI阈值、CTran显式冲突比例与AEff人工time/path complexity proxy形式化既有原则；未给新的可操作辨识/校准或直接设计反证。例子coverage/soundness解释互换不作为新评价成果。观点/无实现本身不是排除理由，不为已有通则改书 | new-abstracts2完整AB；semantic-core3 §4.2–5 L170–220 |
| 2602.14100 Character-aware | 潜在有限反侧：混合序列中字符仍顺序position、无序tag固定position0，uniform处理反退；相同4层/超参、3频率×12run且lemma不重叠。只核有限表示接口选择，不外推所有模型或human cognition | new-abstracts2完整AB；semantic-core3 §3 L121–168 |
| 2602.14234 REDSearcher | 潜在：graph topology与evidence dispersion双轴控制训练task difficulty。只拟该数据构建命题，不因SOTA/整套midtrain+RL组合准入 | new-abstracts2/final-decision-cores精确v1完整AB；project-date作者页Figure2无dated News |

## 代表性事件关闭

RosettaTrace：Google原始完整摘要显示蛋白redesign reward/rollout/search及复用，没有改变通用模型或基础设施判断的具体独立增量；本轮AI for Science暂缓，范围关闭。MapTrace：官方Feb17博客已读123–168，精确旧稿2512.19609v1摘要及Table2/§6定点比较，其critic准确率/误报与fine-tune机制是旧事件；2M发布数量本身不足新机制。本次增量关闭不否认旧稿价值，也没有顺带重跑旧日。原件在calibration-originals、abstract-map-delta、decision-cores。

OpenAI chatgpt-4o-latest：限定日期搜索曾命中API Deprecations官方信号，经root指出不能仅看Research首页而漏处置后，实际定点读官方原文L1140–1146。2025-11-18已通知Feb17移除snapshot并给gpt-5.1-chat-latest替代；Feb17是既定shutdown生效日，不是此合同首公开日，目标段落没有另外改变协议/兼容要求或新机制。具名关闭本次增量，不据此声称用户迁移已验证或runtime真停止。原段保留supplement-openai-deprecation-20261008.json，不扩整个deprecations历史。

## 一次有限必要日期恢复

11潜在项的精确v1原始页面缺公开日。Submitted/页面arXiv印刷日期、Atom published、DataCite Created/Registered/Updated、编号/月目录、搜索相对Published标签均没有拿来单独认定新增公开日。旧78公开区间不按本轮新字段标准推倒或搬移。

在单日catchup恢复失败后，进行了3组精确作者dated-artifact检索（author-date1/2/3）：SpectralCollapse、AdaCorrection、ATTest、Sali-Cache；KernelBlaster、Floe、MoSLoRA、REMem；ASCL、Character、REDSearcher。已知作者repo/project再一次定点检查：ATTest、KernelBlaster、REMem、ASCL均未见必要first-paper公开日；REDSearcher作者页无dated News；E-DiT作者News确定Feb15窗前。没有遍历repo commit史、下载全部附件或更换到secondary镜像的Submitted日期。MoSLoRA搜索碰到2024同名repo，身份不同已拒绝。不为2项贡献关闭追日期。

因此11项必要公开日期保留：不用于新增候选、正面证据、Books或无遗漏断言；不将它们视为普通全文待办，也不降分或转EX。统一一次请求作者dated首次paper artifact或官方original announcement，须绑定精确家族/版本并落2026-02-17北京时间自然日；收到后只重开相应项，再按评分/采用命题审读方法、关键评价/反侧和实际owner差额。

Opus4.6更正独立保留：当前card索引changelog提示Feb17 HLE with tools 53.1→53.0/3作弊实例漏检，官方news却将同样更正脚注标为Feb23。必要当日card版本/事件日期相互冲突；web PDF 400、urllib403、curl有限下载不完整导致pypdf EOF，实际必要正文未恢复，不能拿索引当完整card。详见supplement-opus46-recovery-20261008.md。恢复须官方当日card artifact或官方明确区分事件日期，不能仅用Updated或继续整份下载/revision史。此项不重写旧Sonnet4.6原判断。

## Books与停止

本轮没有新增确定落窗候选，11潜在日期项与1重要修订日期冲突都已隔离。新增Books NoChange是必要日期/事件身份未成立而不采用，不是“11项全部已被Books覆盖”。未请求共享Books写锁、未写新引用/正文/LS/index，也未改旧38整合、31覆盖、3仅报告、6争议处置。若材料恢复，按对应Stable owner和完整相邻内容核具体差额后再提逐字最小拟文，取得owner锁/非writer POST后才写。

普通可执行工作0：有限扫描/筛选、报告处置与root独立DAY已通过，实际独核见supplement-independent-20261008.md末。新增外部精确保留12项，机构目录历史完整性继续按报告§2隔离，不授正面Coverage/Evidence或无遗漏。完成态同步后重跑可判定检查，不以作者自签替代root验收。没有启动下一日。
