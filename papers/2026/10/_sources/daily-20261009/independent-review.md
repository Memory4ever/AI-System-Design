# 2026-10-09 独立复核依据

复核者：root；本日报告作者：supplement_20260312。窗口为北京时间2026-10-08完整自然日。下列是已实际检查的范围，不是整日报验收；必要审阅、Books实际写后与六部分复核尚待完成。

## 官方入口与首批准入

实际打开[OpenAI研究索引](https://openai.com/research/index/)：首屏两项Oct7、两项Oct6，随后Sep29；读到窗前停止，没有Oct8条目，不据此声明全网无遗漏。[Anthropic Research](https://www.anthropic.com/research)的Publications首屏两项Oct8，随后Oct1；两项官方全文和日期均已独立读取。

[The missing map of the sky](https://www.anthropic.com/research/the-missing-map-of-the-sky)采用已有跨波段inpainting与并行校准流程完成天文制图，没有新增可改变当前模型系统设计的通用机制；贡献前关闭，不把Science名称本身当排除依据。其两次Agent审查未发现观测glow仅为具名个案，不能推导所有独立审查无效，不扩读天文数据。

[OSS Scanner](https://www.anthropic.com/research/launching-opt-in-vuln-finding-service-for-open-source)准入通过：原CVD人工triage瓶颈→opt-in未人工核验报告交给maintainer验证→需要分开候选发现、报告接收与fix接受权限；3+2+3=8，深入范围为此发布/验证合同。全文明确保留原人工CVD路径，reproducer、可得时bisection/patch构成报告内容，未证明生产补丁正确。选定97项high/critical、48项目中85达CVD、11重复、1invalid，不能把88%解释为所有raw findings准确率或recall；29k候选与6k人工处理也不能当漏洞证实率。官方日期Oct8；相关评价是作者受限验证，不是独立复现。

实际读Ch72 850–910完整局部及Ch73开篇：已有security-agent trace/deterministic predicate、CGIF反例、人工release与真实修复激活边界；opt-in未经triage报告的双发布路径还需作者明确比较和逐字PRE。尚未授Books完成。

## Qwen具体载体事件

实际读取[精确tag API](https://api.github.com/repos/QwenLM/qwen-code/releases/tags/v0.25.0-nightly.20261007.8003d28042)完整body：published_at=2026-10-07T22:01:24Z，对应北京Oct8，prerelease=true。普通CI/UI/test不进入逐PR审阅队列。实际读PR12531与13376的核心说明和反侧：前者约束有损MCP别名不能扩大grant，保留deny/ask；后者先查已提交replay再发布正文，重试返回原ref/revision，不清理旧孤儿。两者merged_at均为UTC Oct6，不能把其原公开事件搬到Oct8。其他PR中段输出截断，未据标题授实现通过。

Oct1–6及Oct8日报定点检索这五PR无具体已审记录，不称已审重复。随后补读PR13515、13508、13291完整英文核心/测试说明/反侧，无截断：13515按深度识别closed参数拥有的范围，quoted XML不dispatch，但外层write_file仍拒绝，不能说恢复了原工具；13508只改scope说明、generated schema和测试payload，行为限制已由13462在main实现，不因fix标题新收机制；13291披露dispatch前intent/checkpoint、结果给模型前receipt/settlement及unknown-outcome恢复阻塞，但没有注册/启用Managed，不授生产恢复。三个merged_at仍为UTC Oct6。未运行作者测试，也未检查这些commit实际代码。nightly载体中的潜在变化仍须作者限定当前版本事件与必要核心；此处不自授候选、评分或Books采用。

## arXiv有界查漏与首批校准

实际读取[官方DC recent](https://arxiv.org/list/cs.DC/recent)的Oct8组22标题（条目13–34），以及[CL Oct8组首50标题](https://arxiv.org/list/cs.CL/recent?show=50&skip=144)。宽标题只作线索，不当候选或完整AB。独立完整读取以下四个current官方AB，均仅v1且当前页无撤回说明；公开归属依据DC Oct8列表，不用其submitted Oct7日期替代公开日期：

- [2610.09657 MemFerry](https://arxiv.org/abs/2610.09657)：DHA host computation与参数搬运/反传驻留调度，改变offload训练计算和通信取舍；可准入。
- [2610.09424 CoMoE](https://arxiv.org/abs/2610.09424)：弱PCIe/无P2P条件下host-backed token multicast与token级combine，改变路由/同步策略；可准入。
- [2610.09307 vLLM-Omni](https://arxiv.org/abs/2610.09307)：异构生成stage、connector数据面与长会话control分工，改变单decode-loop服务假设；可准入。
- [2610.09372 Expert Coupling](https://arxiv.org/abs/2610.09372)：correlated placement与attention reduce-scatter内token shuffling，不改router/expert但改跨GPU通信；可准入。

尚未独立读四项方法/实验，不采用摘要数字或授Source Review完成。其余排除项需作者记录后按来源、主题及理由抽检；未声明全分类召回。

## 后续必要证据与 Books 复核

- OSS Scanner：root通过网络恢复实际读完整FAQ（web不可达不记零命中），核对未验证报告不启90日CVD、以后人工验证从通知日起计与退出后原CVD路径。Ch72完整CGIF/repository-first邻接及作者单段拟文PRE通过，授权限该段和自身末注；实际写后待核。
- MiniMax Oct8 workflow：root实际读完整核心审计与三skills说明，2+1+2=5准入校准通过，仅采用模块测试全绿但默认入口、setting传播或background resume失效的具体反例和验证条件；单人自报不证明更多Agent/单owner/跨模型复核的因果优越。Ch84 release、trace/harness局部已读，具体拟文待核，不把通用‘应验证’当新的Books成果。
- CoMoE：root实际核精确v1 §3.1–3.3、§4.1–4.3必要对照与直接限制，包括人工barrier、NUMA与batched commit消融、高负载排队、整机/CapEx和工具调用边界。作者6分与最小host共享路径命题通过；Ch49 MixServe至device小节完整局部PRE通过。非写入者root实际核新正文245、完整局部和本人2326末注，POST通过并释放窄ownership。只采用source egress去重、token齐贡献与成本转移；不认证全拓扑、质量、恢复或生产SLO。
- MemFerry：root实际核精确v1 IV-A/B/C/D、V存储切换与442–444同步、VI-A/C/D/E必要配置与反侧。profile接口不授算法记号正确或全局最优，gradient DHA慢写、DeepSpeed buffer混杂及4训练+4辅助资源保留；Ch39 Offload/TRANSIT/full-host-cache实际邻接差额明确。必要Source通过，单段PRE/写后待核。

## 实际写后与后续裁决

前述“待核”是当时停点，以下为随后实际完成范围，不改早先查询事实：

- OSS：非写入者 root 实际读 Ch72 新871正文、860–882完整CGIF/repository-first邻接和3246自身注，回对有效launch/FAQ，POST通过；单段窄锁释放。
- MiniMax：逐字PRE通过后由报告作者写 Ch84 新827正文；root实际读818–852完整Release邻接及1166自身注，POST通过，窄锁释放。只保留具名失效路径，不采用单owner或跨模型因果优势。
- Expert Coupling：root必要v1 §V-B、VI及A-A配置独核、Ch36 Cobalt完整邻接/PRE通过。作者窄写后，root实际读775–798完整局部、新785及1852自身注，POST通过，窄锁释放。token/residual owner置换与canonical还原有同组TP/EP、SP和完整dispatcher前提，总bytes不当最忙链路，短步计时不授长期能力。
- MemFerry：逐字PRE通过后作者写Ch39新277；root实际读250–312完整Offload/TRANSIT/full-host-cache/CPU-stream邻接及412自身注，POST通过，窄锁释放。全部原有机制保留，新增只承担逐层FP/BP驻留与梯度写址接口。
- vLLM-Omni：root实际读v1 §2.2–2.6必要控制/数据/session、§5.1/5.2关键配置/失败、§5.3冷缓存和§5.6单fixture/不停音反侧、§7未来工作；Ch50 252–315异步PP完整邻接与逐字PRE通过。仅授单段及自身注写锁，实际写后尚待核；未复现、核代码或全部模型列表。
- Qwen：完整读取作者qwen-nightly记录并复用root已实际五PR必要核心，具体贡献前关闭通过。新prerelease载体不能自行证明本窗新增机制/启用Managed；不假称已审重复，不将窗前PR搬入本窗。
- 机构：实际读institution-coverage完整14源有限入口/停止与恢复范围；Meta恢复、Seed双locale、MiMo真实route日期停点有据记载。Hunyuan/Qwen新目录有限恢复仍不可用，不能称零或全网无遗漏。

vLLM-Omni随后已写：root实际独读Ch50 253–316完整PP/新276/restore/failure邻接及416自身注，回对上述必要原证，POST通过，窄锁释放。初批六项实际整合均完成写后复核。

新增四项current官方精确v1完整题摘已由root独立读完并校准：09778为序列隔离测量与重复运行稳定性协议，10508为query-side distractor暴露embedding指令失败及训练评价边界，10455为错误前提纠正轨迹与最终正确性的分离评价，10170为heading placebo及first-stage recall对结构检索因果解释的反证。准入均有具体潜在增量，不能把摘要读完/当前仅v1当必要证据完成；公开日采用作者另核的PF/IR/CL官方Oct8日期组。必要Source由非本笔记作者逐篇推进。

root随后实际定点确认PF recent的Oct8日期组58–76包含09778（5号），IR recent的Oct8组201–212包含10170（20号），CL skip144/show50的Oct8组20–44包含10508/10455（146/147号）；只证这四项本窗公开，不把页面其余日期或提交时间计成本日事件。

这些是分项实际审查，不是整日验收；剩余当窗主题分页/含糊AB、新四项Source/Books和最终六部分普通待办继续，不外部化未读工作。

## 后续四项的必要证据裁决

10508、10170由非作者review_mar11_continue实际读取方法、关键正反对照、限制及Ch76具体邻接/PRE通过。root实际核Ch76 heading至Online/UNREAL邻接，授两处单段及自身章末注窄锁；10170将path措辞明确为与chunk对应，不冒称全部native/gold，实际写后另验。

09778：root非作者实际核完整§3、§4.1～5.3与159～168结论/限制，确认context切换才reset、run内仍并发、同实例40runs carryover、rep-P50 CV与请求tail分责。累计而非factorial且无cache/thermal telemetry，32k input加512与32768配置未闭合，未采用容量/模型排序或通用经济结论。实际Ch66 Runtime导语及AgentReplay完整邻接核对后Source/PRE通过，仅授生命周期段和自身注窄写锁，实际POST另验。

10455：root非作者实际核本日必要方法、完整主表5.1/5.2及5.3、D.1行为判据、B.2参考scorer定义/529直接限制；不是被测模型内部belief。实际Ch66 1162前提识别×信息承接双轴、1852～1859 outcome×链敏感性×自足性及计算/文本干预正文承载拟采长期命题，有限Existing Coverage通过。论文三标签recipe、阈值与离线predictor不冒称都在书里，无新Books写入/不需POST。不得据此批准全部标签/部署恢复可靠性。

10508/10170随后由作者窄写Ch76新140/103；root非写入者实际读91～117 heading→Structured完整邻接、127～147 Dense/new/UNREAL完整分支及1354/1356自身注，POST通过，两窄锁释放。原heading/Structured/UNREAL论证保留，induced path措辞与有限source一致，未授答案级效用或全部任务服从。具名作者同步报告和自身注即可，不新增重复审阅。

09757日期：root实际核官方availability175/183与DataCite原始JSON doi/title/url/state/created/registered及v1日期；最早公告与已分配公开ID的登记上界同Oct8，日级夹证通过，非metadata时间单独作公开日。官方LG定点未列仍保留。正文必要证据/PRE由root作者另记entroprefill-core-review，独核另指派非作者，不自授通过。

09778随后实际写Ch66新924与5856自身注，root非writer实际918～940 Runtime→新生命周期段→AgentReplay完整marker→AgentOutcome及本人末注读完，POST通过、窄锁释放；有限采用与此前必要证据一致。

新增13份完整题摘由非作者review_mar11_continue逐项独校准通过，10179仅为准入补读intro91～102后停止，不把含糊AB自动授贡献。全部有效日期复用官方目标组，09757只用root已核两界推断；潜力准入不是Source/Books完成。最终限定arXiv完整题摘25＝21拟候选＋4具体AB排除，另2标题范围排除；机构2候选合计23家族。这个比率只描述有界相关题摘切片，非全部当天论文、全分类队列或全网召回。必要Source分别按明确ownership推进，不因数量/耗时改判缩池。

## 后续必要证据与实际写后

- 10395：review_mar11_continue 非作者必要 Source/actual owner/逐字 PRE 通过后，作者窄写 Ch17。root 非 writer 实际顺读366～410完整 Norm→算法解释→新389→Layer冗余及本人863末注，对有效原证与限定采用一致，POST通过、锁释放。不是全定理、可学习性或生产算法验收。
- 09876：supplement_20260311 非作者必要 Source/actual owner/逐字 PRE 通过后，作者窄写 Ch24。root 非 writer 实际顺读846～875 provisional/持久条件副本→新858→UI→实时pipeline及本人2321末注，POST通过、锁释放。原有状态与commit论证保持，不把空间probe或无符号target当真实解与无先验。
- 10426：root 非作者实际必要主方法123～210、关键评价211～289与直接B385～388/C392～415，actual Ch29 791～823及有效相关交接；Source/PRE通过。采用当前runtime fingerprint为示教资格，固定另一component验收与冻结选择集分责，不采用matching唯一因果、4B参数收益、普遍迁移或较低全链费用。仅授Ch29对应一段及本人末注，写后另验。
- 10332：root 非作者实际必要v1 114～199、213～318及A319～341，完整方法、关键主表/直接反侧和评分接口；actual Ch29 178～224及有效Ch28/30交接。Source/PRE通过，派生stage不替真实state/权限，3N joint score后仅action入history，200预算收益与大预算mean追平、探索性/混杂和全成本同链；不授stage唯一因果或episode改善。仅授行动接口后单段及本人末注，实际POST另验。

以上只为分项结果；最终23家族仍须全部处置及非报告作者六部分验收，不以分项通过预授日级完成。

10232有限NC：root非作者实际读取v1 160～268方法/主表、273～333可靠度/拒绝人口关键结果、348～395讨论与直接限制；actual Ch66条件证据/拒答coverage、127～141幸存分母、208～220能力与elicitation及347～355固定答案judge稳定性。必要Source与有限Existing Coverage通过：拟采行为不等能力、拒绝剔除改变人口、reliability不认证人类真值的长期界线均有具体正文。不声称已含九任务recipe、全部partial-rank分析或准确的判拒算法；不由弱相关推其唯一原因、纯潜在能力或人类说服效果。无新写/不需POST，标准5分保持。

10381实际写后：root非writer完整顺读Ch45 1550～1577历史anchor→新1564跨loop延迟入库→logit补偿→eviction及本人2140末注。有效非作者必要Source/PRE与采用一致，POST通过、锁释放；不是完整runtime或服务SLO验收。

10426/10332实际写后：root非writer完整顺读Ch29 192～211旧行动接口→新202 TPD→Context、810～832 Qwen3CoderNext→新CoTrace→synthetic artifact→privacy入口及两本人1426/1428末注，对先前有效原证和逐字PRE一致，两个POST通过、共享锁释放。原论证全部保留，未把训练标签/晋升对照授予执行权限或生产收益。

09679实际写后：root非writer实际顺读Ch33 528～552原prompt replay→新543有限horizon支出控制→error branch/quality条件分支及本人末注；独立Source/PRE与采用一致，POST通过并释放窄锁。保留virtual allocation与executed budget反馈分账、surrogate与真实learning gain边界和静态/均匀退路，不授普遍最优。

10179必要Source/PRE：root非作者实际读取exact-v1 103～213核心方法/评价与223～237直接限制，并核Ch33 243～264 suffix/answer-dependency→PRM完整交接。signal定义与credit落点分责、signed mass与执行query tokens绑定、同分可更新不等步骤真值；shuffle局部对照与筛组改变strength的混杂已保留。作者逐字单段PRE通过，仅授权该局部及本人末注，实际写后待核，不授DAY。

10179实际写后：root非writer实际顺读Ch33 246～267完整suffix→answer-dependency→新255外部观察信用→PRM→sign-preserving交接及本人3128末注；采用与有效必要Source/PRE一致，actualPOST通过、窄锁释放。保留信号真值、信用支持集和终点验收的边界，不授全训练配方或日级完成。

09877必要Source/PRE：root非作者实际核官方PDF header为v1；实际117～184/251～340/341～493/501～567/574～614方法与关键评价，以及1485～1521/1522～1593、1864～1891必要控制/费用/metric权限，不声称全§3～7、全A证明或全部附件已审。Ch49 953～970 ProbeQuant完整及1327～1349 Waterfilling邻接、Ch48/50开篇实际比较；局部FP扰动表、dispersion非所选配置置信度、共同候选clean反退与mask限定和selection非全费均支持有限逐字PRE。Source/PRE通过，仅授唯一单段与本人末注，写后另验。

10533实际写后：review_mar11_continue非作者必要Source/actual owner/literalPRE已通过后，root非writer实际顺读Ch12 288～315完整collision/MPHF→EngramNine→新298编辑接口→data-aware容量及本人403末注；与采用一致，actualPOST通过、窄锁释放。保持原hashed table固定、精确sequence overlay与真实ngram复用分责，不授无影响、免费编辑或事实认证。

09877实际写后：root非writer实际顺读Ch49 1328～1353 SchurReplay→Waterfilling→新1341局部扰动表→distribution-conditioned及本人2328末注；必要Source/PRE与采用一致，actualPOST通过、窄锁释放。未采用全理论证明、任意坏校准鲁棒或真实部署收益。

09493实际写后：supplement_20260311必要非作者Source/owner/PRE通过后，root非writer实际顺读Ch66 274～294完整sensor→Gemma2→新283幅度/方向分验→crossmodel→Evaluation Identity及本人5860末注，actualPOST通过、窄锁释放。不由状态诊断或点保留率给来源真值/发布授权签字。

分项结果现为23/23必要证据和Books处置：20实际整合，3具体已有覆盖；所有实际新正文经非writer POST，尚待最后正式六部分完整稿的日级验收，不能由本分项总数直接授DAY。

## 最终日报验收

root不是本日报作者。本轮实际完整顺读作者14:42:15提交的六部分终稿，回对本日14个到期来源的入口/查询/分页及真实停止、官方Oct8日期组与09757日级两界、23个家族全部评分/必要证据/唯一owner处置及20项非writer实际写后记录。准入校准实际覆盖全部23拟入选：arXiv21、机构2；排除的4完整AB、2标题以及Anthropic sky/Qwen五窗前PR核心均已具名独核，没有将宽查询返回量变为候选或全文队列。未独读所有宽发现标题的全文/所有附件，不授全网召回。

最终23＝20实际整合＋10455/10232/09346三项具体已有覆盖；表行与23个§4小标题一一对应，准入、必要Source和Books结果分开，普通待办0。书稿保留原有机制与邻接，新增采用是受限接口/边界，不认证实现复现、普遍性能或安全；不同作者的必要Source由非作者核，root作者09757亦经他人实际Source/PRE/POST。Hunyuan/Qwen当前研究目录访问缺口只隔离来源保证，已有可读Qwen载体独立关闭，具体dated本窗列表/快照可定点重开，不把空页记零或授Coverage。正式稿日级语义验收通过；机器校验及完成态最终同步另外执行，不替代本判断。

完成态回读：root核对14:45:57稿的状态、§1/5/6同步，重新运行V3校验通过；55个本地引用均存在，23行/23项证据、20整合/3已有覆盖一致，15个Stable owner可解析，六部分及围栏检查通过。本日Report、原始依据及15个涉及章节的限定cached/unstaged diff检查通过；工作树已有staged内容保留，本轮root未stage、commit或push。
