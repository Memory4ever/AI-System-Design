# Pneuma-Seeker 2603.10747v1：必要 Source / actual Ch79 / 受限 PRE ready

只补2026-03-12 BJT自然日。SUP_ABS3_10747完整题摘、独核§19准入和§23日期夹证复用；四作者一致，current exact-v1无Comments/venue/withdraw。DATE3原件实际回读Submitted Mar11T13:20:16、created Mar12T02:08:52、registered Mar12T02:08:53；依官方正常公告批次下界与registered上界夹日，不单用Submitted/Updated/月份。题摘原题为“Pneuma-Seeker: A Relational Reification Mechanism to Align AI Agents with Human Work over Relational Data”，官方exact-v1 HTML正文题为“Pneuma-Seeker: Relational Reification of Information Needs for Agentic Data Discovery and Preparation”；同ID/四作者/完整摘要对应，保留此题名层差异，不造另一家族。首页PVLDB 14(1)/2020/XXX/doiXX为模板占位，不能当实际2020发表证据。旧Pneuma是本文明确借用的Retriever，不因引用它重开全部历史。

官方https://arxiv.org/html/2603.10747v1 GET200，342051bytes，UTC2026-10-10T03:17:30.056885；SUP_CORE_10747.raw/txt/MANIFEST_RESULT保存。实际读§3完整协议、§4.1–4.2、§5.1–5.5完整动作/终止/存储，§6两完整定性例，§7 setup/7.1.1–3/7.2.1–3/7.3.1–3和完整Tables1–2。图只读caption/正文，未视觉读取Figure2–6精确bars、不采用精确图上Pareto/curve；没有核代码、复现、全历史系统/无关文献或附件。必要支持/反侧已够，此处停而不是伪造图/实现受阻。

## 实际增量与评分

模糊问题直接生成答案，把“需求解释”与“查找/计算”混在一次隐式推理里→本稿将需求外化成可由用户修改的多关系目标𝒯及答案程序S，再独立物化𝒯、执行S并保留转换DAG→设计选择变成先验收目标人口/列语义和来源覆盖，再验收执行，而不是答案流畅或查询运行就确认需求已满足。

拟1+2+2=5：D1只计局部关系目标/物化分责的实现，不把DAG、SQL、算子、动态规划或主动查询本身当发明；R2计用户需求/目标对象→数据发现/物化→答案执行的真实接口；Durability2计目标语义与数据依赖可独立修改/检查这一具体可复用界限，尤其§6跨来源年份/金额定义不同和§7.1.3缺表例改变如何解释“执行成功”。不是主线映射即潜力、不是机构/部署/领域label抬分。actual Ch79缺这一具体关系目标交接与有限负侧，必要深入仅受影响内容已完成。准备者不自签，待非准备者核score/gap/PRE。

## 原件机制 / 可采用边界

§3目标(𝒯,S)中𝒯={T1,…,Tk}是由源表通过join/filter/union/aggregate生成的derived views，不只是现有表schema；S是对𝒯的SQL/Python答案转换。先明确目标、再物化、执行S得D；用户可改列/群体定义。ProvenanceGraph记录转换节点/数据依赖，拓扑排序后附S输出脚本，可检查构造过程。**确定性脚本只认证已选操作的执行，不证明需求解释/输入数据/LLM生成语义列是真值**；本文§5.2还允许LLM生成semantic column和自由Python，不能把整条语义链称确定性正确。

§5 Conductor最多10轮，每轮situational analysis后提一组动作，包含retrieval/context extraction/(𝒯,S) manipulation/materializer/executor/用户沟通；选沟通即停，耗尽轮数则强制合成回应，不等已经物化全部或semantic acceptance。Materializer另最多10轮，可再检索/探测，先给join/union/projection参数由应用生成SQL，保留semantic join/top1和LLM列/SQL/Python fallback。DBService workspace.db按user-chat分开；这里只采用状态/查询存储，不认证安全沙箱/tenant无泄漏/事务完备。宏/微context标签不计新贡献；具体micro是用执行query探测列实际values/distribution后修目标，§7.1.2 capital例把nonempty改primary，不是模型自述confidence。

§5.3默认3queries×top10、已有Pneuma summaries，加entity regex/global scan和table-name regex enumeration；semantic match/regex不证明全集和源正确。§7.1.3identity-theft例明确无(𝒯,S)仍有enumeration工具，却遗漏州表，114392→243377为作者单例；有目标[state,metropolitan_area,num_of_reports]与union-all-name cue支持补表，不认证所有州/所有数据库从此完整。

## 评价人口、直接反侧与费用

§6不是独立用户study：真实procurement41表/15GB加Oracle FY2025 7MB，作者将两原问题当I*，手工造更模糊I+，只比较两定性案例。年份dispatch_date/created_ts、金额ordered_amount_usd/grand_total_usd与ID/dedup不同可暴露伪“结构变化”，null acknowledgement和hazardous-radioactive overlap可提示改目标，但不能统计认证用户信任或必然收敛。

§7 filtered KramaBench六域88题（12/4/9/17/28/18），有tabular-domain应用但拟采用的是一般目标/执行接口，不采用science端点。M4 MacBook Air16GB/Python3.12.12/o3-2025-04-16/text-embedding-3-small；三系统仅localtables，关闭web/crawl/knowledge store。DS-Guru Biomedical限5样本行，Astronomy连1行也986955tokens而被省略；smolagents看schema/sample<=5并可执行Python。回答sets/lists计F1，其余正确比例；重复trial/seed、判分者/独立标注细则、CI、模型precision/concurrency/SLO在采用必要段Not Disclosed，表STD是题目runtime分散不是准确率CI。

正文说micro action在4/5域改善，而六域overall人口不同；不从未读Figure2精确bars补消融数值或宣称每域/唯一模块收益。(𝒯,S)消融去掉define+materialize，只剩context extraction直接作答，改变多项执行责任，不能单归因schema文本。正文Biomedical94.44%与9题的F1口径保原，不推17/18或每题binary。gpt4.1-mini平均49.95%只比smolagents高1.14百分点，未有CI不认证显著。

完整Table2反侧近结论：Environment Pneuma LLM126.08+nonLLM3.62s，smol73.96+3.96，DS40.25+5.85；Legal106+2.92对76.48+3.73和32.16+.78；Wildfire94.41+3.36对68.64+4.34、DS27.92+62.10，总时有退步。Memory Legal116MB高smol43/DS25；Biomedical186高smol135。1GB scalability固定两表一问题，Pneuma58.74+.37、smol39.94+15.75、DS11.73+51.71，不能所有规模更快；§7.2.2文字称1GB DS-Guru overtakes两者，却按披露加和DS63.44s>Pneuma59.11s>smol55.69s，原句与该点数值矛盾，隔离精准速度断言，不补造原曲线或否定接口。smol1.9GB更省是noisy string触发换pipeline，非单纯规模曲线。Token定价只作者2026Feb27口径，非当前价格/全链费用；索引/summaries/embeddings、内容scan、目标协商、双loop/probes/materialization/LM、持久视图/DAG、人审均计费，不补造端到端省算。

## actual唯一owner与差额

ROADMAP唯一AGENT-PLANNING，books/part-07-agent/79-planning.md。实际顺读96–187完整decomposition/dependency/replanning及compiled-domain/schema与predicate-first交接，342–393全部Goal/Project2Task/Verification；Ch75完整1–148包括派生表context/current observation权威分工。Ch79现177–183有固定domain artifact/签名→可执行求解及语义≠可执行，355–372有task contract/objective/owner/input/output，但**没有可由用户修订的目标derived-relations集合𝒯与其答案程序S分开、data probe后修目标/按目标物化并展示完整转换依赖**。不是“计划可验证”成熟原则重复；同章已有原编译/签名分支继续保留。Ch75只交接bounded evidence working set，Ch76只交接源检索/覆盖，Ch78只交接工具执行权限，不增加多个owner。

建议在Ch79编译domain artifact两完整段177–179后、predicate-first新分支181前插入两段；承接原“参数/schema错误仍会错误交付”，说明目标仍可协商时不应过早固定solver。不新结构、不写章末论文摘要。

## 逐字两段 PRE（待非准备者核）

若需求本身仍在变化，先固定 solver 也可能过早：用户可能尚未决定“哪个群体、哪些字段、按什么口径”才算满足问题。一条关系数据分支把这份解释外化成目标关系集合与其上的答案程序；目标列、语义和群体定义可由用户修订，数据物化则负责用已检索源构造这些关系，最后执行程序得到答案。对表内容不确定时，先查询实际值、分布和结构，再改目标或补来源，而不是让字段名、几条样本或流畅答案暗中决定统计人口。转换依赖图与可重跑脚本使构造过程可检查；它们展示的是已编码操作怎样产生结果，不证明目标忠实于用户、源数据完整或语义生成列真实。

[Pneuma-Seeker 的有限对照](https://arxiv.org/html/2603.10747v1#S7)中，显式目标关系帮助一条多表统计补齐遗漏来源，主动查询也修正了把非空 capital 都当国家首都的筛选；但消融同时改变目标定义与物化责任，两个人工构造的模糊需求案例不认证普遍收敛或用户信任。目标协商、数据检索与探测、物化、模型调用、依赖记录和人工检查都有成本，某些数据集的总时间或内存反而高于直接作答基线。应分别验收目标语义、来源覆盖、程序执行与答案；预算耗尽后的回应也可能仍不完整。目标口径漂移、数据不齐或执行无法可靠确认时，回到澄清、原始数据与简单可检验查询，不让确定性运行替用户确认需求已满足。<!-- source-family:SF-2026-ARXIV-2603-10747 -->

最小停点：必要支持/反侧与actual owner差额已够，拟5/PRE交非准备者；未写Books、未正式候选、未DAY，不为精确图/无实现或普遍保证扩范围。
