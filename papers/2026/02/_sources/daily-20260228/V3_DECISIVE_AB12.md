# AB12 四个具名含糊事实：一次决定性 core（待非作者校准）

精确 v1 完整题摘和 current Comments已读；仅恢复决定准入的事实，得到以下作者判断即停止，不把全部framework/proof变成审阅义务。2项拟窄IN5，1项哲学/定义论证EX，1项有技术潜力但家族公开日期保留。无新safe/Books lease。

## 23239 Agency and Architectural Limits：拟 EX，不评分、不进 Books

[原abs](https://arxiv.org/abs/2602.23239v1)为完整原题摘；HTML404后恢复 [精确PDF](V3_PDF_2602.23239.pdf)，必要pp7–11及13–16实际读，p14含Table2已视觉核。公开题摘是“优化系统不能norm-responsive”的强反证信号，故不能仅以哲学标题关闭。

原论证把 genuine agency定义为非可交易规范+非推断中断，随后把“constitutive optimization”限定为所有决定均来自可交易scalar、内部没有独立中断。p14的specification conflict主要由定义和有限softpenalty不能硬约束得出；p15–16明确把external filter/hybrid排出 agency定义，未给可检验的新控制接口、独立运行反例或可操作的全系统不可能边界。RLHF训练scalar并不逻辑推出部署只能无约束argmax；在指定可判定约束的有限action域先过滤再argmax，即可保该scope的硬约束，与“任意开放规范覆盖已解决”是不同主张。原文把lexicographic saturation解释为exchange也没有给formal可行集条件。

因此只保哲学定义下的说法，不把它授为LLM/Agent系统无法采用hardgate的科学反证；已有成熟“softreward不替代external enforcement”不足以构成本项目新增贡献。未声称已审全部appendices或所有哲学命题无价值。current v2 Mar01窗外，无相关撤回/纠错标记；日期不影响此准入关闭，不另造日期请求。此风险EX须root读上述必要原页独校。

## 23253 SPARR：拟 IN 2+1+2=5

[v1](https://arxiv.org/html/2602.23253v1) blocks26–40/65–79实际读到决定位置。原“sim-base+real-residual”本身成熟；具体新条件是base只读state、real residual读image/proprio并额外消费base action，对真实小插接任务有w/o-base-action直接控制；TableII两任务相同base下，加入该consumer context改善成功和cycle，需重新考虑 residual是否只消费当前observation，还是也显式消费被冻结base的proposal。TableI demo-update只在部分cycle更好（01036从4.31变5.45），不是全部效率无税。

成功轨迹由base动作均值+原Gaussian方差抽noise组合得到，不需human residual labels；仍需预抓物体、合理zero-shot支持、自动reward/success detector。原base goal在实机使用人工得到GT pose+synthetic±1mm noise，非自然pose estimator完整误差测试；sparse成功由3mm/5degree规则定义，不能等同每一精密装配物理有效性。base近零成功、反光小孔80%与实机oracle限制保留，不能用“无需human expertise”授无校准/无人工环境配置。

Submitted02/26 17:26:13Z、registered02/27 03:06:19Z；arXiv事件区间02/27 09:00～11:06:20+08。无后续重要说明。潜力是consumer输入可选条件，不是论文名/asymmetry包装；标准必要config/更广控制及actual Ch26 owner尚普通待办，root准入后继续。

### 23253 必要审阅与 actual owner（2026-10-06）

后续：root非写入者实际读Ch26完整694–716及自身末注，actual POST通过；本项证据/实际整合终态，非日级Gate。

feb28_vla_last7非原packet作者实际核精确v1 III–IV/V、blocks26–40/45–79。state base Gaussian mean+real residual读取双RGB/EEpose/velocity/force/torque与baseaction，原Cartesianimpedance跟踪incrementalpose；pseudo residual从base sigma的zero-meanGaussian采样，仅成功trajectory作demo，RLPD demo/RL各半+faster-than-median update，不需human residual action label却仍需humanGTgoal/预抓/reward。原goal是人工完成插接得到GT再xy±1mmnoise，真posepipeline未直接作为输入；3mm/5°success rule不认证全部assembly接触。sim128env/25Mstep一天，挑10/100个sim>99%任务，real20成功demo+0.5h/15Hz、20eval；4090 policies/JetsonOrin controller，HIL有human数据/干预是oracle非同权限预算。

TableII base-input removal两任务同框架支持context选择，TableI01036 demo-update cycle4.31→5.45反退；roundhole反光仅80%、OODbaseaction residual不能全correct、base近零成功/自动success依赖是直接边界。image residual只排除objectpose输入，不授没有任何测量/感知误差。score2+1+2=5保留，Ch26已有endpoint residual/counterfactual训练但未含state-sim-base→image-real-residual显式消费baseproposal及该支持条件；窄融Sim-to-real，预算/GTnoise/回退近文。原v1提交17:26:13Z、registered03:06:19Z/本窗09:00～11:06:20+08/当前家族事实复用本日未变证据，不默认旧revision对比。实际正文/完整邻接/自身末注顺读；root非写入者actual POST通过，本项终态，非日级Gate，未核artifact/复现。

## 23258 AgentDropoutV2：拟 IN 2+1+2=5

2026-10-06 后续必要原证/actual owner终态：fresh非原packet作者实际必要blocks29–41/46–63/70–76，触发条件只拥有检索资格、定义才供rectifier判断；γ1 reset和K/T非单调、groundtruth teacher权限/调用費用。采用2+1+2=5，具体差额深入后窄融AGENT-REFLECTION/Ch80正文297/299，完整289–309，末注452；final_audit必要原源/actual owner非写入者独核通过，root实际正文/完整邻接/自身末注POST通过，已同步并释放窄锁。精确v1身份/家族日期沿用本日原字段和政策下界、同ID注册秒上界，只支持09:00～11:06:28+08半开范围，不授注册首公开；未核实现/复现或全证明，非日级。

[v1](https://arxiv.org/html/2602.23258v1) blocks29–63/70–76读到决定位置。RAG/errorbank/rectify/reject成熟组合不足；具体可核增量是按indicator的trigger-condition而非完整name/definition检索，matched随机5对照与generic indicator对照显示 **context-eligible诊断支持集改变rectification的成立条件**；增迭代2→3→4、K3/5/8不单调，不能从更多反思/检索推质量递增。该局部受控结论会改变检索哪些经验/给多少纠错预算，而非用“firewall”命名授权安全。

每条indicator由teacher读取GT失败trajectory挖出，rectifier用role/current input+definition打violation flag；all retrieved pass也未认证真实正确。任何一条flag触发retry/reject，低剩余message数触发reset，reset不是安全共识保证，外部预算/终局验收仍必要。Qwen3-4B/8B非thinking、GPT4.1mini selector、GPT4o mining、Qwen3Embedding，maxchat6/retry3/K5/gamma1、rectifierT0其他.7，仅math/code局部，对OOD/missingindicator无完整证书。尚未核所有config/artifact，不声称实现safe。

Submitted02/26 17:31:43Z、registered02/27 03:06:27Z；arXiv事件区间02/27 09:00～11:06:28+08。v2May/v3Sept窗外，无当前重要纠错标记，不做默认diff。实际owner/标准成本界继续在准入之后，不因已有Bank主题相似直接授整合。

## 23286 SPARTA：技术潜力保留，家族日期未授

[原v1](https://arxiv.org/html/2602.23286v1) full title/AB/current Comments、blocks34–55实际读到一次决定位置。post-order/SQL execution是成熟原则，独立增量是empty时从已非空的intermediate tuples生成why-not目标、定位blocking predicate再只改对应clause；相同600成功queries的no-provenance对照4722vs8253调用，支持局部oracle/refinement预算接口。保修predicate改变问题分布、LLM抽事实与verbalization不自动真值、人工SQL/schema检验必要；不是仅多hop规模榜单。

原current与v1Comments明确ICLR2026。[官方OpenReviewPDF](https://openreview.net/pdf?id=8KE9qvKhM4)同题/作者/摘要身份已实际核；索引“7months ago”只搜索年龄，不是首公开日期。官方[forum](https://openreview.net/forum?id=8KE9qvKhM4) browser-verification challenge，api2 notes403见 `V3_FETCH_AB12_SPARTA_FAMILY.json`。缺官方first-public pdate/可支持本窗新事件的版本说明，不能凭Submitted02/26 17:59:51Z与registered02/27 03:07:10Z授家族首次；不列确定当窗候选/Books，不无限追查完整评审/历稿。恢复该forum初次公开记录或本窗实质新事件所需局部证据时只重开该ID。

2026-10-06 fresh非旧作者23239风险EX独核：实际精确v1 PDF pp7～11、13～16读取定义、两机制、RLHF归因、Table2及hard filters/hybrid/lexicographic排除段。原文以genuine agency/constitutive optimization定义排除external enforcement，训练scalar不能推出部署仅unconstrained argmax；有限可判定action域先过滤再argmax可保该scope硬约束，并不声称开放规范全覆盖。没有独立新控制接口或可检验全系统不可能边界，成熟soft reward不替代hard enforcement不足新增项目贡献。结论EX/不评分/不Books，不否定全部哲学命题，不审全附件或跨日归属。

2026-10-06 root非作者一次准入原段独核：23253 29–40/65–79（72及后局部返回截短，实际65–71/75/78/79读到）；23258 29–41/70–76。两项窄IN5通过，仅授准入；后续必要标准证据/日期/actual owner继续，未授Books/日级完成。
