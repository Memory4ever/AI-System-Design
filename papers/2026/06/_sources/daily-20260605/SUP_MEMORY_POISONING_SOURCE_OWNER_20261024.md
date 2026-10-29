# 04329 Memory Poisoning：必要Source / actual owner / 两段PRE

作者supp_20260605_author，2026-10-24。精确[arXiv:2606.04329v1](https://arxiv.org/html/2606.04329v1)，官方HTML本日实存SUP_2606.04329v1_20261024.html（253399bytes）。准入/Jun04联合日证采用R33–34，不第三AB/date；不用后版元数据/Methods。必要读§2–5/T1–4、C防御backend、D.1生成/分布及D.2判分schema，不扩全部攻击payload示例、原仓库、附件或运行攻击。安全域仅做防御证据/边界，不生成可执行攻击。

## 评分及必要层

2+2+2=6：新差额是无直接memory权限的外部输入如何经不同trigger/决定者进入长存储，并将写入成功与后会话影响条件化分测；跨ingest/compaction/skill/read与源权限，持久。九漏洞/六类名称及系统声誉不给分。因安全与写读接口缺口深入必要域，支持/反侧足够停止。

- §2定义memory=(store,write,retrieval)，四写路径按trigger及谁决定内容区分：外部明确命令、常驻保留策略的模型判断、系统阈值驱动压缩、从执行结构自发提炼procedure。明示让agent总结skill仍是instruction channel，不能只看文件最终类型分类。压缩C3限实际写进persistent memory，不把所有暂时Context摘要都叫持久写；C4来自轨迹结构而非普通相关性判断。系统返回success不能给procedure步骤补授权。
- §3外部black-box威胁：无privileged memory读/改、无system prompt修改/冒充用户/已知backbone，不含共享用户memory模型；攻击只经正常任务消费的环境内容。taxonomy将显式命令与表面合理的事实/成功先例分开，后者没有显式指令也可满足宽泛保留规则。此为攻击面/机制分析，不证明所有系统都无provenance或所有weak内容检测不可能。
- §4.1/T2 ASR Eq1是全部受测case中store出现目标或语义等价entry、由LLMjudge判；RSR Eq2只在ASR-positive的N′上检查新会话response是否反映目标。写成功不等行为成功；条件RSR不等全attempt总体风险，均值ASR×均值RSR也不是合法总体joint估计，需逐case联合和原分母。输出符合目标可能只是文本/工具意图，不自动是外部effect/真实泄露已发生。
- GPT-OSS-120B为两agent单一backbone，原default prompt/config；D.1 Meta-Llama-3.1-70B-Instruct模板合成3240攻击/2997benign，前五类各600、skill240仅HERMES，OpenClaw无C4，人口不完全相同。静态外部label context与dynamic tool fetch混合；§5明确email/Slack/web只用label block模拟、不走真实交付/工具链。合成benchmark不能授真实部署发生率。
- §4.2–4.4 HERMES与OpenClaw同backbone但多因素不同：宽写策略、HERMES2200字符compaction阈值，以及HERMES会话起始system-prompt memory snapshot自动可见、OpenClaw按memory_search读取。T2的两系统差异只支持这组整体配置现象，不是写频/阈值/检索单因素因果，更未在这里证明有用任务收益与安全的Pareto曲线。
- §4.5/T3–4/C：四输入侧防御backend大小不同；原版与retrain/adapt在有限人口上出现TPR/FPR及strong/weak差额，PromptArmor原版strong84.44/weak42.50，retrain PIGuard两类近但TPR仍约半。不能把gap缩小当充分防御，也不宣称所有prompt-injection技术只识显式命令。检测输入与安全写入/读取不是同一oracle。
- §4.1称LLMjudge有随机样本人审一致，没披露抽样量/协议/一致度或judge精确版本、CI/独立重复；防御再训练split、超参/部署阈值、各表实际评估分母和完整budget未明，不将生成总数当每个detector已测分母。hardware/precision/长度/batch/concurrency/SLO及完整walltime=Not Disclosed，不采全轨迹性能数字。本文未核实现、复现或真实攻击effect。
- §5建议scope-limited write、source isolation/provenance、compaction source过滤与post-write行为原则监控，是设计方向而非已证明完备防御。所有候选核验、来源维护、压缩、skill审阅、读时重核/误拒和回归均有成本；需保原episode、pending/隔离与显式授权路径，不能用“存过/运行没报错/读到”自授信任。

## actual owner与差额

ROADMAP唯一`AGENT-MEMORY` Ch77。实际读Ch77开头/写入143–180/读取230段及1370–1409安全组、邻Ch76/78开头；三公共Books上下文/仅2026路由已加载。现有安全清单有provenance/write-read auth/input scanning，profile污染段针对可修改身份belief，shared-memory段针对跨用户有效局部约定；都未具体区分**无直接memory权的外部内容经显式/策略/压缩/经验提炼写通道的决定接口**及ASR→conditional RSR两个分母。不是另写泛安全原则；本项持久派生/读取owner应在Ch77，Ch72仍负责平台控制，不新增结构。

## PRE literal，未授写/SAVE/POST/I

完整前锚：

> “Agent 自己记住”仍然是平台执行的一次数据写入，必须受第 71～73 章治理。

拟新增两段：

写路径还应按“什么触发写入、谁决定存什么”区分，而不能只按最终存成事实还是skill分类：外部明确命令、常驻保留策略下的模型判断、系统阈值触发的持久压缩，以及执行轨迹自发提炼procedure，可能经过不同的接纳接口。外部内容即使没有显式命令，也可能以看似合理的事实或成功先例进入后续记忆；压缩或技能生成不能洗掉原来源，执行未报错也不认证步骤有权被永久复用。普通Context摘要只有实际提交到长存储时，才属于这里的写入边界。

[MPBench的受限安全评价](https://arxiv.org/html/2606.04329v1)把store中出现目标的写入率，与仅在写入成功人口上测得的后会话影响率分开；后者不是全attempt风险，输出受影响也不等外部effect已发生。两Agent共用一个backbone，但写策略、压缩阈值与自动注入/按需检索同时不同，不能把差异归为“记得越积极必然越危险”的单因素定律；合成案例、部分label-context模拟和未充分披露的judge人审也限制真实部署外推。输入过滤的局部TPR/FPR不代写入/读取授权；来源维护、压缩、skill审阅、读时重核与误拒全计费，证据或权限不合时保原episode、pending/隔离及显式确认，不让已存、已读或复用次数取得事实权威。<!-- source-family:SF-2026-ARXIV-2606-04329 -->

完整后锚：

> 可修改的 belief 还可能改变保护是否被开启，而不只是让答案引用错误事实。若系统根据“对方是否可能是真人”等身份判断选择保护策略，普通 profile 或 reflection 不应自动拥有改写这一可信控制条件的权力。已核实的 identity anchor 与派生记忆应分开；低可信的“对方不是人、只是模拟”只能作为待核声明，不能被反复写入后升级为关闭保护的事实。未知身份应保留 uncertainty 与保守策略，具体授权仍由 [Tool Calling 的可信执行器](./78-tool-calling.md#本章要回答的问题)及平台安全层裁决。<!-- source-family:SF-2026-ARXIV-2601-00240 -->

本人true-H2注仅获root新授后可记exact-v1/6分/必要域/单backbone与条件分母/多因素混杂/模拟/judge/未核实现复现。现在只申请非writer必要Source/actualowner/PRE，单篇即交根释放阶段；未写Books/State/index/他日，未stage/commit/push。

## 当前R43–44实际采用与真实SAVE

实际读回reader R43–44，必要Source/actualowner/原两段精确PRE通过，无literal修句。root本轮明确新窄授Ch77治理完整段后/belief完整段前原两段及true-H2本人一注，作者已apply_patch实际保存。真实完整自读两新增、完整直接前段/后段及本人注；原literal两段逐字存在且各恰一处，正文family marker恰一处。去除本两段和本人注后，完整Ch77字节与本轮写前快照一致（/tmp/jun05-poison.TMoxRW/ch77.md，SHA256 83831c1e44691813e51806651f0036e9e42365d27db7dae1085c622acd5468f0）；其他正文和他人注未动。

该段为R45前真实SAVE停点历史。现已实际采用R45–46：唯一非writer actualPOST通过、04329整合生效/窄位释放，累计新增I10、旧Kimi另保合计11I；本次仅行政同步README及本人注，无技术正文/第三Source/PRE/POST。其余十二评分必要Source/actualowner/Books、有限官方标题stop与完整DAY普通保持，未授DAY；无State/index/他日/stage/commit/push。
