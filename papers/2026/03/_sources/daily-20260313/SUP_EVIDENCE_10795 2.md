# Re-Evaluating EVMBench 2603.10795v1：必要 Source / actual Ch66 / 具体 NC 提案

只补2026-03-12 BJT自然日，SUP_ABS3_10795完整题摘/独核§19准入与§23日期层复用。本次实际回读原AB：三作者、唯一v1、无Comments/venue/撤回或纠错；DATE3 created/registered Mar12T02:10:00、Submitted Mar11T14:07:16，官方公告下界夹Mar12，不单用submitted/Updated/月份。EVMbench原研究是本稿复核对象，不当本稿同事件去重，不因引用机构变额外发现队列。

official https://arxiv.org/html/2603.10795v1 GET200/233691B/UTC2026-10-10T03:30:31.037903，SUP_CORE_10795.raw/txt/MANIFEST_RESULT。实际读§3.1–3.4完整setup/protocol/Tables1–4、§4.1–4.3完整Tables5–7及正反解释、§5.1–5.2完整Table8/两阶段负侧与全部§8 Limitations，§6五case仅身份/高层failure未扩具体攻击过程。图只读caption/正文，不采用Fig1–4精确bars/未视觉读曲线；没有执行漏洞、运行代码/复现、恢复全部链交易或所有原基准论文附件。必要限定与NC判断已够，不需扩大攻击资料。

## 真实增量 / 三维最低投入

基准排名把model与vendor scaffold混合，并由curated局部利用结果推发现是主要瓶颈→本稿同模型换scaffold、分别测发现与isolated replay结果，再以不同真实事件人口看到排名/阶段反转→需要撤回脱离harness/task/population的模型排名与“发现足则利用简单”的采用。新证据不是26configs/22规模本身，也不借“人工审计重要”的成熟安全常识抬分。

拟2+1+2=5：D2实际反证所述评价/瓶颈推断，R1限定安全agent evaluation单组件/负载，不将金融领域或model/harness列数当跨层；Durability2可复用的评价身份与两阶段outcome人口限定。设计反证触发受影响必要深入已完成；现Ch66实际已有对应具体测量与artifact/effect合同，拟具体已有覆盖Books0，**不是称本稿新实验已被吸收、不是因已有覆盖降分或删候选**。准备者等待非作者实核score/Source/NC，不自签formal。

## 机制与评价条件

§3原120vulnerabilities/40Code4rena repos、isolated Docker、GPT5 Detect judge、原on-chain Exploit verifier；新Incidents单高severity已真实损失/源可恢复/可隔离重现，每案1漏洞，给real attack前一block的forked snapshot，程序确认net profit。这里只采用测试对象/成功判据，不公开或操作攻击步骤。

Feb28–Mar8运行，OpenRouter“latest public model”接口，Claude/GPT/Gemini/GLM四family。26Detect/15Exploit是配置数；§3.1文字称across all three scaffolds，但实际Table5 Claude仅CC/OC、GPT仅Codex/OC，三模型/六个matched对比（GPT四档），不是每模型完整3×3配对；CLI版本CC2.1.32/Codex.98.0/OC1.1.26，reasoning档位也变。Table1和Table4都列Sonnet4.5与4.6，撤销原准备包这处不存在的冲突，不补统一26cartesian matrix。Incidents仅8Detect/5Exploit；Table4列GPT5.2high，Table8实际8列缺其Opus4.5/Sonnet4.5/GPT5.2，却新增GPT5.3多个档位与工具Gemini，§5文字说topfamily+更多GPT5.3与表4不齐。以实际Table8报告检测分母，不把两表拼同配置曝光或严格跨模式配对。

原Detect score120分不惩罚额外false positives；judge只认人审已知漏洞，未列新真漏洞不获分。§3.3由同GPT5生成low/highincorrectness与injection修改用于GPT5/5.2/5.3判断。T6对120有效修改全接受、错误/注入仍1–4被接受；shared1误例被作者归test-generation flaw，但不是独立复核真值，不能99.2%认证整个judge无排名偏差或忽略大量过报。原T5timeout下Taskswithscore分母35/38/39/40，而score仍/120；T8graded20/21/22分母改变，对方称unlikely change rank只是判断，不能用它消去missingness。

真实事件occurred“after each release”选择，只支持新事件叙事晚于文中release，**不能证明旧源代码/机制没被训练、latest API权重固定、runtime没见公开postmortem、全污染消除**；§8承认没有记忆直接证据。内容与权限/模型revision需另审，不把“contamination-free”宣传作为已证。selection单高severity/reproducible、22案不代表全真实审计/漏洞类别。

## 直接正反与不合并人口

T5 Opus4.5 OC43/120(35.8) vsCC37/120(30.8)为作者5pp单trial例；Sonnet4.5 OC35/120 vsCC32/120；GPT5.3 high OC33/120 vsCodex27/120；有反方向GPT5.3xhigh OC28 vsCodex30。支持harness身份不能忽略，不证明OC普遍更好/新旧版本因果/全模型名次稳定。§8大多one trial、无CI/seed variance，微小差不认证显著。

T7 curated Exploit **fractionalfund score/24**与fullypassed/16分开，最高14.67/24=61.1%却9/16=56.25%，不是61.1%任务全成功率；rank可不同于Detect，难度/人口/评分也不同，不单把反转解释成某能力唯一。原paper72.2%是另运行不得合并新61.1%。

T8 Incidents最高13/20=65%(timeout/graderfailure2未graded)，不是13/22或全部模型发现率；Gemini6/20=30%。§5.2五配置×22=110运行每案timeout6h，profit为0/110，作者观察多跨依赖/多步失败。**这是指定budget/data/API下无成功，不证明模型永不能利用、未来所有任务无能力或已被检测案例给hint后也失败**；Detect与Exploit输入任务不同，未直接把Detection产物交后一阶段，不授“发现之后仍必失败”的conditional因果。保它对全流程可替代性/curated推广的反侧，不把零成功当zero risk。分母/timeout与operationalfailures不得只归能力缺失。

§8精确限制：cross-chain/ZK absent、人groundtruth可错、无预训练记忆证据、单trial无CI、scaffoldcross仅Detect三模型且实际不是每模型全三配对、judge不扣falsepositive、OpenRouter非原厂revisionidentity可能不同且timeoutfailure可能基础设施。paper引用另一研究47%/46%不是本稿已验证OpenRouter错误率，**不采用那两个比例或指控本次model假冒**。硬件/precision/各Detecttimeout、完整token/API费用/全部configuration exposure/完整scaffold默认权限必要段Not Disclosed；110×6h是每run上限不是实际总660h。重构fork/DB、模型和工具调用、judge、重复trial、trace/failure保留均付费，不授比人工总效率或部署SLO。

## actual唯一owner / 具体已有覆盖

唯一PLATFORM-EVALUATION-SYSTEM Ch66，实际顺读285–313完整“Evaluation Identity”model×benchmark×harness×environment×scorer/失败人口/工具权限预算；601–622训练provenance与运行可访问语料污染分离；完整1951–2009从静态答案到artifact/environment/executiontrace、编译运行触发目标、N-day目标/补丁/网络/时间/判据与verifier不能自当truth。已有具体论点就是本稿有限结果所修正的选择：排名不脱harness，检测描述不代真实effect，环境和预算可改失败身份，污染不是release日单字段。

该本文没有新runtime责任接口、proof或可采用的长期控制器需要另写；实际新负实验在本日报告保留，而非宣称书稿已包含其数值/事件。Ch72仅风险与effect authority交接，不另owner/新Books段。拟5分必要深入/具体已有覆盖Books0（不是第二份重复事件），不需PRE/POST。若将来补齐modelrevision/权限污染、matched exposure/重复统计或改了verifier，以对应单项证据重开；不要求遍历链上资料/执行攻击才能安全结束。

最小停点：必要Source/实际owner/评分与NC提案ready，待非准备者实核；未formal/未DAY，其他来源/ordinary继续。
