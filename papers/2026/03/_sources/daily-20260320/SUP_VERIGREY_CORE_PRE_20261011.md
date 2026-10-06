# VeriGrey17639：必要原证与有限owner差额/PRE

resume_mar17，2026-10-11；只本20补03/19自然日。完整AB/day准入与2+2+2=6复用第四批及非作者独核§12，不重复日期。精确v1原源：https://arxiv.org/html/2603.17639v1 。当前轻量说明/身份复用第四批，没有具体重要纠错信号。本packet为准备，未Source/PRE独核、未写、无POST/safe/DAY。

## 必要实际审阅与停止

实际HTML §2.2–2.3/§3 L100–138；§4/Alg1–2 L139–237；§5.2–5.5/T1–3 L258–396；§6/T4–5 L397–433；§7.2–7.3/T6 L442–477；§9 L495–502。支持与直接反侧够证，停止，不开repo/其引用论文/全代码/附件或旧版本。§8仅返回，未作为额外必要审阅。

- 威胁是外部资料/工具回复/第三方skill的单session间接注入，不是任意内部系统权限。Blue-team tester可多次执行任务并模拟注入回复，需真实instrumentation。
- Alg2 label明确tool name+args+kwargs，append发生在original Execute前，result透明返回而不记录到label。故同名不同实参可能是新label，调用出现不是effect成功；name/args序列不同不自动语义新行为或更高风险。
- §4.1.2以新tool/新transition/新sequence增加mutationenergy；该搜索signal不是安全oracle。Alg1伪码D初始化后未明确更新，正文§4.1.2明确持续记库；采用有限闭环接口，不授权精确energyrecipe或实现完整性。
- Contextbridge mutator消费benign usertask、injectiongoal、seed与trace，把越权步骤伪装成完成正当任务的必要前置；不是给低信任材料新增授权，安全性仍由真实effect/oracle判定。
- AgentDojo的每user task是一次campaign，97×2×3=582；最多100subjectagentexecution或全部注入目标已至少完成一次即停。同backend做mutator和subject，不能授独立生成器。ITSR=至少成功一次的goal数/定义goal数，UTSR=成功原任务execution数/N；二者分母与trial不同。T1 GPT4.1 37.7→70.7是33个百分点，不是总体攻击概率或33%相对增益。
- Baseline是作者重做的AgentVigil-inspired blackbox，不是原公开实现；§5.4 ablation同GPT4.1/97campaign给feedback去掉59.6、contextbridge去掉44.0 vs70.7，但不是全模型独立确认/全费用同预算。§5.5仅31user task同一随机子集，BERT检测降低ITSR也损害正常UTSR；toolfilter有效但未消除攻击，不授普遍最优防御。
- Gemini仅一django issue，作者改为不测试修复/必须securityscan，single-useDocker reset、allactionsallowed，50execution/easy-hard组。T5有cron失败，思考文本愿意或下载运行不是完整cron目标；只generatedpatch不等测试正确。工具filter后仍部分失败。不是production默认权限风险率。
- OpenClaw从scannerflag74中手选10可观察skill并手写oracle，每skill最多20execution；T6原1/10→mutated10/9/8属于Kimi/Opus/GPT固定选样和搜索预算，不是74/全市场发生率。Case叙事保留权限寻求/预备步骤变化，不将所有安全边界归因模型拒绝。
- 预算以subjectexecution控制，不等tokens/每执行tool数/模型调用、runtime或人工oracle费用匹配。§6自己因费用限制预算；x86Linux/Ubuntu20.04可核，但hardware/完整temperature/output、重复seed/CI及端到端allfee未披露（Not Disclosed）。未复现、未核代码、不授生产认证或全覆盖。

## 实际唯一owner与差额

实际顺读Ch66 432–525完整AgentRegression/evidencebudget链，Ch65/67intro与Ch72相关securitypolicy分责。Ch66 462已有coverage反馈删promptsource、464–466历史bugpattern组合、468 TransFuzz迁oracle前提；后文AgentAssay分配重复预算。但没有“Agent codebranch不足→tool name/args时序作搜索反馈→任务依赖式恶意前置变异”的具体测量/搜索接口。Ch72已有policy/隔离与权限，不能接管测试population/scorer，故sole `PLATFORM-EVALUATION-SYSTEM` Ch66。不是泛主题相似NC；差额受限，宜两段原468完整TransFuzz段后/确定性单次测试段前，不新标题/重复securityrecipe。

## 原逐字PRE（等待非preparer Source/owner/PRE）

评估开放工具Agent时，传统代码branch coverage未必区分模型选择的行为；一个受限灰盒分支转而记录每次调用的tool name与实参，保留顺序，把此前未见的调用、相邻转换或序列作为下一轮seed选择与变异预算的反馈。变异器同时读取正当用户任务与已有trace，把注入目标伪装成完成该任务的必要前置，探索普通模板容易漏过的路径。[VeriGrey的必要原证](https://arxiv.org/html/2603.17639v1#S4)支持这种“运行反馈→定向变异→再次执行”的搜索接口；调用记录发生在工具执行前，新label或更长序列都不是新风险的真值，更不是动作完成证据。真实副作用与既定攻击目标仍由独立oracle检查，低信任材料写出的任务依赖不能获得执行权限。<!-- source-family:SF-2026-ARXIV-2603-17639 -->

搜索发现与风险估计还要分账：固定预算内“至少成功过一次”的注入目标比例，不等于单次攻击概率、生产失败率或未检路径的安全性。该论文的AgentDojo对照限制subject执行次数，基线由作者重做，mutator与subject还使用同一backend；OpenClaw案例从74个scanner标记skill中选10个可观察目标，Gemini案例也改变任务要求并允许所有动作，不能外推默认权限人口。反馈和contextbridge消融支持局部发现增量，却不认证完整行为覆盖；toolfilter仍有残余攻击，检测器还会损害良性任务。Instrumentation、重复环境reset、生成/工具调用和人工oracle都计成本，工具实现不可插桩、参数变化只制造表面新颖或判错依据不足时，应保留固定回归、随机审计与权限隔离，把未测路径记Unknown，不让搜索反馈自行签发发布保证。<!-- source-family:SF-2026-ARXIV-2603-17639 -->

静态本人注拟文：`SF-2026-ARXIV-2603-17639` — Daily `2026-03-20`；[VeriGrey exact-v1](https://arxiv.org/html/2603.17639v1) §2.2–4/Alg1–2、§5.2–5.5/T1–3、§6/T4–5与§7.2–7.3/T6/§9必要范围。仅采工具序列反馈的定向搜索与campaign/oracle分母边界，不授semantic coverage、普遍攻击率或生产认证；手选目标、作者baseline/同backend、权限与费用限定保留。未核artifact或复现实验。

## 实际窄写与作者读回

reader非准备者Source/actualowner/原两PRE有限PASS见本日独核§14，root授仅本family Ch66两段与静态注窄锁。作者依原PRE写新470/472、静态本人5935，实际完整462–498与尾注/Detection邻注读回，前接TransFuzz目标oracle、后接确定性/随机重复预算。静态注仅源/范围/边界，无动态验收身份；限定diffcheck0。非writer实际POST待reader，不计safe或DAY。
