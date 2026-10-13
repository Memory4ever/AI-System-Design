# RPMS17831：经验消费前的粗状态筛选与规则仲裁 / 必要准备

准备者resume_review17_18，2026-10-12，仅03-20补03-19。author明确分配sole必要准备，原2+2+2=6/day准入与身份复用SUP_AGENT_TAIL_ADMISSION_PREP§5；不改日期、分数，不自授Source/PRE/Books/safe/DAY。下面是已实际读到的必要证据与最小拟稿，交author非准备者裁。

## 1. 实际必要Source范围 / 停止

[exact-v1 HTML](https://arxiv.org/html/2603.17831v1)：完整AB/引言L86–102、§3–4/Eq1–8 L119–248，§5/T1–5/§6/7/Limitations/Ethics L249–322；A.1/Algorithm1与A.2 L354–393，C.1–3/T8–10 L416–447，仅prompt消费位置必要D.2 L558–629。current abs L8–31同题三作者、完整AB、单v1及无具体Comments/撤回说明实际轻量核。未读完整References、B旧baseline表、D全部trace/E全部规则/F全部示例/G统计检验，不看图像像素，不核实现/复现。支持有限接口及关键反侧足即停，不扩query/版本史。

## 2. 真实接口与反侧

闭世界文本环境里，belief是由observation文字和上一步action经确定性pattern规则更新的位置、手持物、容器开闭和物体最近位置；不是访问环境完整world state。三层rule手册是通用策略、任务type程序、环境动作语义，在决策每步拼成提示。memory来自seen任务prior运行，R1正文233 entries冻结后评估，不是测试任务在线自改写。

目标签名partial match先取候选，ALFWorld记录signature=(location,held-object)，但Eq6实际Compat只比较手空/非空，**不核位置相等、手持物identity或容器状态**；不能将两字段signature或“state consistent”名称当完整前置条件等价。ScienceWorld另有instrument/room硬条件与progress bounded lag，需重写domain/environment规则，非同predicate直接全域迁移。对象held不是观察真值，也不由deterministic parser推出其正确。

仲裁在memory entry进入prompt前进行：与rules直接冲突的entry删除，潜在非直接冲突附warning交LLM；Alg1最后LLM生成action后直接return，没有显示对新action再执行确定性合法性/授权拦截。故只采经验提示消费资格，不采所有动作executability硬保证。规则本身人工编写，错误规则可经rules-first放大，条目级冲突也可能把行动顺序与位置线索混在一起。

评价：ALFWorld v0.3.5、134unseen/140seen、singletrial、50steps，Llama3.1 8B/70B及ClaudeSonnet4.5，greedy/max256；ScienceWorld26task/241episode/100steps、GPT4 max512、连续score。硬件/precision/并发/SLO与完整生成/手册/seen学习/检索/调用费用未披露；不能将不同backbone的两环境称model-controlled transfer。四条件冻结sharedprompt/ICL/decoding与whereapplicable memory，但rule与memory开关同时影响belief、goal及不同知识块，不能认证每个模块独立因果或共享prompt token预算。

T2 Memory-only在Look由55.6降11.1、Heat30.4降26.1；Full的Cool47.6低于Rules-only61.9。因此memory净aggregate改善不是所有任务受益，甚至rules+筛选+仲裁后仍有反退。T4不仲裁的combined47.8低于Rules-only50.7，硬/软仲裁组合59.7是固定配置的局部支持，不授普遍提升。**不要把Memory-only直接称“完全无SCF”**：§5讨论称unfiltered，但C.3另报告关闭SCF在Memory-only再掉3.7pp，说明此对照不单独认证SCF缺失的因果。精确配置若要重开强归因，需每个condition的belief/SCF/仲裁开关、prompt与逐任务paired结果。

C.1总体平均步数下降但success子集改变，且C.2早错误终止变多，不授同任务难度或latency/SLO改善。C.3R1写223与正文233、memory-only38.8/full53.0与T3的41.0/59.7不齐，不采精确learningcurve归因或强正交结论。G未核，不采用p=.008认证；保T1–5作者受限结果性质。不因这些局部矛盾将已有准入改EX/降分，有限经验消费分责仍可核。

## 3. actual唯一owner / 差额

唯一`AGENT-PLANNING`，[Ch79](../../../../../books/part-07-agent/79-planning.md)。actual完整40–83 belief/查询/先验/transition、133–166 replanning、205–263历史检索及precedence/executor边界实读。Ch77入口1–52、typedwrite76–109及1330–1369元数据/冲突评价实读；Ch78/80入口1–20实读。未把整个memory库存当Source或机械NC。

已有belief不等world truth、precondition与history图、typed memory读取资格很强，但缺具体“先按goal召回→粗手占用过滤→entry级hard/soft规则仲裁→仍由LLM提出新action”的消费接口及其残余cool反退。本差额只提议在Ch79原58 observation schema完整段后/60 prior-estimator段前两短段；Ch77仍owner持久写入/来源授权，Ch78 executor仍owner effect gate，不复制memory算法到两个章节。非准备者可裁specific NC，不为制造diff强行写。

## 4. 待非准备者裁的两逐字PRE / 静态源注

旧经验与当前目标相似，也未必适合当前状态。一个受限文本环境分支先按目标类型、对象与目的地召回冻结的经验，再用当前 belief 检查其可用条件；ALFWorld 中的轻量筛选实际上只比较手空/非空，不等于核验位置、手持对象和所有动作前置条件。随后对经验条目作规则优先仲裁：直接冲突者不进入提示，潜在冲突加警告交模型判断。[受限规则—经验对照](https://arxiv.org/html/2603.17831v1)支持把召回相关性、状态相容性与建议冲突分开，却没有在模型生成新 action 后显示独立的执行拦截。belief、人工规则与历史经验仍可能共同出错，允许进入 Context 不取得真实行动授权。<!-- source-family:SF-2026-ARXIV-2603-17831 -->

因此更多经验不应成为默认发布条件：原有限任务中，单独加经验使部分切片退化，完整筛选和仲裁后仍有任务不如仅规则。平均成功率或更少执行步数不能消除这种差异，也不能由更换模型后的另一环境成绩识别唯一机制。规则编写、seen-task学习、解析/检索和每步额外 Context 都计费；状态与规则接口不可靠时，停止采用不相容经验，保留原无记忆/已验规则基线、真实 observation 与独立执行检查。需要跨环境复用时重新核验动作语义、compatibility predicate和旧任务反退，而不是把“rules-first”名称签成通用可执行或安全保证。<!-- source-family:SF-2026-ARXIV-2603-17831 -->

静态源注：

- `SF-2026-ARXIV-2603-17831` — [exact-v1](https://arxiv.org/html/2603.17831v1)必要§3–7/Eq1–8/T1–5、A.1–2、C.1–3与D.2消费位置。仅goal召回、粗状态筛选与经验条目规则仲裁的有限接口；保occupancy非完整前置条件、belief/人工规则错误、task反退、不同模型环境及全费用。Memory-only不冒完全无SCF，不采精确learningcurve/唯一因果、动作硬阻断或真实安全。未核代码、完整统计附件或复现。

## 5. 非准备者有限核与写后链

交resume_mar17一次必要Source/actualowner/两literal/static裁；preparer不自授PASS，未获root family锁不得写Books，未actualPOST或整日DAY。后续只恢复受影响命题，不无差别重读全部附件。

## 6. root soleCh79授锁后writer窄写 / 非POST

2026-10-12 root接纳author§5有限PASS后授resume_review17_18 soleCh79本family两literal+static窄锁。实际写前42–83及原末尾source邻注顺读，写后完整42–96/new60/62与594–602本人/Draft/编排/Ares邻注回对原批准literal，schema→经验消费资格→先验估计器衔接保持。实际scoped diff只本family两段+静态注六新增行，无删改；该章diff-check无输出，其他已有修改保留不代验收。writer读回不是nonwriterPOST、不计I/safe/DAY；交author一次完整局部与本人静态注实际POST，不再循环改身份。

2026-10-12 resume_mar17非准备者实际必要Source/actualowner/两literal/static有限PASS：exact-v1 §3/Eq1–7、§4主要setup/condition、T2–5/A1–2、Limitations/Ethics与C1–3实际独读，支持及关键反侧足即止，未冒D2全部prompt或G统计全读。Eq6只有手空/非空，Alg1生成action后直接return，不成立完整前置条件/动作硬gate；T2 memory切片反退/Full Cool退、C3另关SCF继续退与R1人口数/成绩不齐都准确保留，不能套独立SCF因果。actual Ch79 42–92及200–264、Ch77相关74–105/1328–1352及78/80入口顺读；已有belief/history/precedence executor论证不能替代goal召回→粗occupancy→经验条目仲裁→LLM新action的具体分责。sole Ch79 observation schema段后/pre-estimator前两原literal与static可有限分采，原6/day不变；强普效/全执行/安全不采，规则学习、seen-memory、检索与每步Context全费用近文。告root协调reader唯一family窄锁写后，author一次nonwriter actualPOST；未Books/POST/safe/DAY。

## 7. 实际非writer POST

2026-10-12 resume_mar17实际完整顺读Ch79 36–100（本family新60/62）及593–602静态本人/邻注，回对原§4两literal与有效必要Source：正文逐字一致，observation schema→经验消费资格→环境先验估计器衔接成立。粗手占用不冒完整前置条件，entry仲裁不冒新action执行gate；共享belief/规则错误、task反退、不同backbone与全费用近文保留。本人静态源注与Draft/编排/Ares邻注准确，未修改Books或过程身份。有限actualPOST PASS，告root接纳/释放soleCh79本family锁；只单项整合，不授本日报DAY或实现复现。
