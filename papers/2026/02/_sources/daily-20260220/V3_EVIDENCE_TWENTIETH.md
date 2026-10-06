# 02/20 第二十有限证据包：小模型 Skill / Population / Reliability

仅16653、16662、16666的必要精确v1原源与actual owner比较，不重建宽435队列。官方v1事件页本轮轻查身份/可见说明，未见撤回或纠错告示；16653现有Jun18v3、16662Jul2v2、16666后版均不借内容。复用root既已独核announcement→same-ID DOI日期桥，下界均2026-02-19T09:00:00+08:00；Registered+1秒上界依次10:51:35、10:51:49、10:51:56（北京时间）。原Submitted/Registered在各V3_DATACITE_2602.ID.json，不把注册等同公告精确时刻。

## 2602.16653v1 — Agent Skill Framework

**2+1+2=5；标准必要方法/匹配评价及直接限制完成，拟仅报告，待root独核。**

实际exact-v1 core94–114、datasets115–140、evaluation576–591及limits711–714。每task临时repo为GT skill加4–5 distractors（结果描述4–6），DI最小prompt、FSI全repo、ASI按需；评价IMDB300、FiNER403/139labels、私有保险200，主为分类/标签，不是真实多tool effect。270M至80B开放model+GPT4omini，后者因隐私不测保险。routing SkillACC与最终ClsACC/F1分开；Gemma270M/4B小hub已失效，hub扩大时局部小模型退化，所测>12B到100仍稳，不据此划全模型12B门槛。Qwen80B code较instruct好而FiNER仍逊thinking，未控制训练差异证明codeobjective唯一因果。

VRAM×min仅作者资源代理，当前必要正文未足够披露统一hardware/precision/batch/concurrency/SLO，不采用工业通用最省/全生命周期最优。加保留最近3–4turn历史后Qwen80B 5.321→10.035 GBmin/item，是此协议成本反侧而非GPU并发收益。POMDP/value-of-information是成熟描述，不证明学得最优belief/controller；层级reference例子和Claude近100%只为非匹配CLI观察。作者直接承认窄任务、smallmodel recursive reasoning原因、codeefficiency因果、SKILL.md结构仍未解决。

Actual AGENT-TOOL-CALLING Ch78:528–536已区分retrieval/confusion、skills子目标/依赖，不宣称本篇数据已有。此次必要证据只能给特定小模型与局部skillhub容量结果，尚未控制reference层级、目录相似度、model训练及推理预算形成新的跨模型成立条件；不因12B/80B局部选择建议与POMDP换名强建稳定Books规则。保留负面routing/资源证据于日报，未因NoDiff排除准入。

## 2602.16662v1 — Evaluating Collective Behaviour of Hundreds of LLM Agents

**2+2+2=6；population测量接口实际差额深入，拟窄整合，待root PRE与Ch82具体锁。**

实际core138–164/201–239、selfplay368–430、culture438–456/584–620。PGG/CRD/CPR三binary action、固定收益、20round游戏；六model（Haiku4.5/Gemini2.5Flash/GPT5mini/DeepSeekR1/Llama3.1-70B/Mistral7B）。每model/attitude512自然策略→编译算法，操作测试只确保能运行，允许逻辑错误；Llama/Mistral描述生成到600仅取可编译策略，可能筛掉复杂策略。不是每回合LLM在线决策，也无通信。Exploitative/Collective词未定义，interpretation混杂保留。

selfplay group4/16/64/256无放回抽样，组内proportion改变，normalizedpayoff不是singlemodel能力分数；模型/游戏方向不同，CRD过合作和CPR早defect不可恢复反侧保留。Culture人口512，初始均分model/attitude，每人四次4或64群体game；top64保留、其他按normalpayoff模仿gene，10%mutation，再从相应策略池重采。75%gene或200generation停，100模拟报告winner频率/末代welfare，非唯一数学equilibrium。多数exploitative胜出但CPR小组反例，不授现实用户必race-to-bottom。作者直接limits612–620承认binary/固定payoff/已知horizon、无通信、观察payoff/模仿、品牌/迁移费用省略、attitude及超参robustness未立。

Actual AGENT-MULTI-AGENT Ch82:348–352现有history→partnerbelief/currentaction与权限边界，未解释**固定预生成策略的population composition与selection operator**是另一测量身份。拟在此后只补一段：单agent收益/selfplay不替populationwelfare；可先生成/执行检查冻结策略，分别变组大小/群体组成，再显式版本化imitation/mutation/停止及个体/群体结果；它以离线compile/模拟费用换规模/可检查性，但排除在线适应通信、编译筛选偏差和selection假设不可据为真实部署预测。不让人口模拟授权限或cooperation安全，短小合作仍保持既有在线/明确规则/实际环境验证。具体算法全部参数不搬书，不新结构。

## 2602.16666v1 — Towards a Science of AI Agent Reliability

**2+2+2=6；设计反侧与中心指标冲突深入，拟争议终态隔离，待root独核。**

实际Table2 220–267、§3/aggregation268–327、setup340–370、results373–405、limits430–446及直接相关A.1.1 811–825。原14model（不是旧初筛误记15），GAIA165、τ-airline经原标签问题clean26/50；每task5runs，非reasoningT0而reasoningdefault不能同称allT0确定，5prompt改写、20%fault、mediumschema扰动、posthocconfidence、LLM safetyjudge。单scaffold/benchmark及judge不可靠直接限制，不用what-but-not-when推唯一planningcause。指标选择/aggregate主观、安全单列与tail风险对整体解释限制保存；真实事故反事实“could identify”未验证。

**中心实质问题：**Table2声明所有score∈[0,1]，C_out用二元y、同task样本mean p与unbiased sample variance s²，再 `1-s²/(p(1-p)+1e-8)`。自己的直接代数核验：二元样本恒有 `s²=K/(K-1)p(1-p)`；K=5任意mixed-success（1/5、2/5、3/5、4/5）都约-0.25，只有全0/全1为1，与声明range冲突。若改population variance，则mixed近0，也不形成文中所称独立于capability的连续区分；本轮不擅自改公式。原§3.5.1/A.1.1关于normalization隔离能力与整体趋势的采用桥接因此未建立。安全scope/soft confidence/risk等成熟原则不靠该坏指标证明。

actual PLATFORM-EVALUATION-SYSTEM Ch66:39–41重复稳定、60–68层级成功、318–333异质聚合与judge/safety分责已在正文，不借主题已有当中心支持；本篇具体12metric或趋势不写Books。拟保留争议外部终态：不采独立reliability定义/整体趋势、生产门禁或安全保证；局部trajectory/扰动只作描述。重开只需官方精确版本对C_out/samplevariance/range的纠正与实际metric实现/相应重新聚合（或另一可核原材料解决桥接），不遍历后版全部附件；现已足够判隔离，不把普通未读项换成hold。若root认为仅该component应隔离，可再收窄，仍不继承headline。

## 当前批次边界

十九包已root全部必要/实际POST通过，当前76终态/45POST、普通20。本包三项仍不计终态。无共享锁、无stage/commit/push；新Ch82段须root PRE授窄锁才写。

**后续独核结果：** root 必要源/处置通过；16653 限定仅报告5分，16666 争议只影响 C_out 和依赖聚合/independence，保其他有效描述。16662 Ch82:352/344–363 邻接与自身末注1301已 root 实际 POST 通过，锁释放。本包3项终态；其后连同二十一/二十二合为84终态、50POST、12争议、5Existing、17Only，普通12，无日级验收。
