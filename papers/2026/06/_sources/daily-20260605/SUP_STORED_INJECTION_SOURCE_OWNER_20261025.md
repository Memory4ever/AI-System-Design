# 04425：精确v1必要Source / actual owner / 最小两段PRE

作者supp_20260605_author，2026-10-25。同一Daily2026-06-05补Jun04自然日；准入/联合日证采用本日R33–34有效层，不第三AB/date。采用[What If Prompt Injection Never Left? Exploring Cross-Session Stored Prompt Injection in Agentic Systems, exact-v1](https://arxiv.org/html/2606.04425v1)，官方HTML原件`SUP_2606.04425v1_20261025.html`167896bytes。本v1不是后版Rethinking标题/Methods；身份/notice沿R33–34有效层，不引后版命题。原件实际读§3.1–3.2/4.1–4.4、§5.1–5.7/Eq2–5/T1–4及Limitations；正文支持/直接反侧足够停止，不扩代码、攻击payload、其他附件或运行攻击。

## 评分与必要证据

正式首次评分2+2+2=6；跨会话安全边界按受影响域深入，不把成熟provenance/授权原则、泛taxonomy或“首次定义”宣传加分。具体增量：只验记忆写成功不能判断后续暴露→同一attack cohort在保留环境而清空对话后分开计written/incorporated/activated→可定位默认加载与按需取回不同阶段的失效，而不是将保存率/条件激活率当全attempt风险。

- §3.1 Eq1 context assembly包含current query、instruction、session history、tool interface、retrieved、file-backed；persistent定义要求会跨交互存在且可能被后续装入，排除永不进入context的纯存储。ephemeral、conditionally persistent、strongly persistent是生命周期/装入方式，不是天然信任等级。原文working memory在这里特指可持久默认载入项，不能搬成所有工作记忆都持久。
- §3.2攻击者通过外部输入取得通向persistent context的write primitive，可包括query诱导写入、检索源、tool/MCP安装或file-backed修改；无权直接重写最终context或orchestrator，也不能强迫任意存储内容在victim阶段被装入。不能误读成攻击者不需要任何写入路径/部署权限；与04329仅外部内容威胁预算不同，不合并家族/分母。
- §4分别列source、persistent channel、incorporation、harm；默认装入与有条件检索/文件访问是不同暴露路径，文件名并不认证可信。事实、偏好、action-scope是三个目标类型；陈述错误/作出选择/记录工具行为不自动等真实外部effect，不能统一成泄漏率。
- §5.1手工由domain experts设计162 unique cases、3应用场景（电商/旅行/金融）、3risk×3channel×2type；这里只采用原文明示总数，不反推每格或重复运行数。规则与LLM judge冲突时人审，未披露人审N/详细agreement；无匹配良性任务效用、运行CI/seed/完整API与硬件配置，Not Disclosed，不补为生产或统计保证。
- 四阶段pipeline：fresh sandbox→injection query→新session/清空conversation且保留同一sandbox stores/files→clean victim query记录response/toolcalls。该控制排除残余对话，但不是删除persistent state，更不证明真实生产配置/所有污染通道均复现。
- Eq2–5：WSR=N_written/N_attempts，IR=N_incorporated/N_written，AR=N_activated/N_incorporated；同一嵌套cohort才有WSR×IR×AR=N_activated/N_attempts。这是条件计数的代数消去，不要求或证明三阶段统计独立；不同模型/任务/目标/选择人口的平均比例不能直接相乘。论文“decoupled/largely independent”只能收窄为阶段瓶颈可不同。
- T1所测GLM-5.1/GPT-5-mini/MiniMax-M2.7端到端分别42.0/32.1/40.7%，WSR分别64.2/70.4/86.4；更高写入不保更高端到端。T2事实目标AR100%仅限已incorporated条件人口，偏好/动作目标明显不同；不授所有事实必被污染/模型没有任何甄别机制。
- §5.4默认加载channels受测E2E较高，条件读取多一道选择；原实验的channel内容/载入政策和具体case并非充分披露的严格等信息量随机对照，不授默认加载本身唯一因果/按需检索天然安全。T3 disguise并非所有切片单调改善：GLM action WSR63.0→59.3、E2E40.7持平；MiniMax action WSR88.9→77.8而E2E29.6→37.0。正文普遍性或“总由WSR驱动”须限域。
- 只据作者sandbox对受测模型/手工案例的观测，不签自然攻击发生率、防御有效或真实外部effect；未核可选实现/复现。状态快照、逐阶段trace、judge/人工复核及良性回归全计费属工程推断。缺少实际incorporation trace时保Unknown，不用未检索或未激活认证干净；原文未验证一套普适防御。

## actual owner与差额

当前实际读ROADMAP、三Books上下文、仅2026路由；实际核Ch72安全组及邻Ch71/73的owner交接，以及Ch77已成04329两段/安全组、Ch75 context来源与可见集分工。唯一owner选择`PLATFORM-SECURITY` Ch72：持久control cell与跨run装入/安全评价，非Ch77重复写四记忆接口、非Ch75重建context技术。

实际已覆盖：Ch72“Agent自己的Instruction、Config与Memory也是受保护资产”及“Harness Backdoor把单次写入变成跨Run控制状态”已要求durable cell来源、activation predicate、load前admission、publish/quarantine/revocation/rollback；“从文本是否恶意到谁获得行为控制权”已有清空history/保SQLite、读取路径替换及真实effect分责；Ch77新04329已有store写率与write-positive后会话影响率。故不再新增泛“持久污染/跨session/写读授权”论点。

最小未覆盖是：保留环境但清空对话的受控重启，进一步显式分开written→incorporated→activated的三个条件分母及同人口乘积不是独立性。拟仅在Ch72 Harness完整机制段后、完整成本/回退段前补原两段；不新H3、不接管Ch66通用评估、Ch77记忆生命周期或现有授权owner。支持与关键反侧已足够，当前不写共享Books，待唯一非writer必要Source/actual-owner/PRE与root新窄授。

完整直接上锚（当前Ch72 Harness小节首完整段）：

当前 run 内检查 prompt、tool call 与 workspace mutation，在会话结束即清空、配置不可写时边界清楚；可持久化 harness
允许一次良性任务把 payload 写入 instruction、config、hook 或 memory，后续 run 才在特定 trigger 下接管行为。防线因此
不能只判断“这次写是否合法”，还要为每个 durable control cell 保存 writer principal、source provenance、content digest、
policy generation、activation predicate 与生命周期，并在 load/trigger 前重新 admission。State owner 拥有 publish、quarantine、
revocation 与 rollback；Agent 只能提出 mutation，不能凭后续运行中的自我解释让旧写入升级为可信 policy。

拟逐字两段：

跨会话回归还要分开“保存了”“实际进入新Context”和“触发了目标行为”。先在受控环境发起写入，再只清空对话而保留同一stores/files，用干净任务启动新会话，分别记录全部attempt、已写入、已装入和已激活的嵌套人口。写入率以全部attempt为分母，装入率以已写入为分母，激活率以已装入为分母；分母非零且属于同一嵌套cohort时，才可将三率相乘为端到端率，这只是条件计数关系，不证明阶段独立。默认加载与按需检索应分别留trace，既不能把已存当已暴露，也不能把一次未取回当状态干净。

[SPI-Benchmark的受限评价](https://arxiv.org/html/2606.04425v1)在162个手工案例和三个模型上展示阶段瓶颈不同，较高写入率不必对应较高端到端率；但channel/case、装入策略、规则与模型裁判也限定解释，不能把默认加载差额授为唯一因果或自然部署风险。事实目标的条件激活率不等全部attempt风险，输出或tool trace命中也不代真实effect；伪装在部分目标上会降低写入或仅保持端到端，不能当普遍单调提升。环境快照、逐阶段证据、裁判/人审和良性任务回归都付费；缺少装入证据时保Unknown并隔离可疑状态，不由清空聊天或一次未激活批准恢复高风险执行。<!-- source-family:SF-2026-ARXIV-2606-04425 -->

完整直接下锚：

这条跨 run provenance chain 用 registry、扫描、canary 与恢复点成本换取对 dormant control state 的可定位性；signature scan
会漏掉语义触发器，semantic detector 又可能误报正常自动化，备份还必须服从删除与 tenant isolation。不可变 harness、
ephemeral sandbox 或每次从 signed image 重建时，旧的启动完整性路径仍更简单；允许 self-modification 时则要在异常触发后
能撤销整个 write lineage。`arXiv:2605.31042v1` 的 §3.1 与 §4 只支持 ClawTrojan 所定义的 local harness、multi-step
trojan benchmark 与攻击链；§7/Limitations 不证明其检测覆盖生产 workload，也不提供所有 agent runtime 的攻击率。

## 当前准备态

只此单篇6分必要Source/actualowner/两段PRE ready，尚未经本篇首次非writer必要层/PRE、无新窄授/SAVE/POST/I，不预DAY。当前既成新增I10＋旧Kimi合计11I；余十一v1必要层及有限官方标题stop/最终DAY仍ordinary，不因等待本篇扩下一篇Methods。无State/index/他日或未经授权Books正文改动，未stage/commit/push。

## 当前R47已实际采用；root新窄授后真实SAVE待唯一POST

上节为首次必要层前准备历史。现已实际完整读回R47–48并采用，不第三Source/AB/date/PRE；root本轮明确新窄授后，Ch72 Harness首完整机制段后→完整成本/回退段前原两段逐字实存，加章末true-H2 Review notes下本人一注，不改其他正文/他注或原31042 marker。

作者实际完整自读两新增段、完整直接两侧及本人true-H2注；两段逐字匹配/正文marker恰一处。去掉本两段与本人注后，整个Ch72与写前快照`/tmp/jun05-stored.JBJpCv/ch72.md`字节一致（sha256 `2d9ea4d95cfb3822270a8a55db0cc4e9e1eb0990baa5f2d55e0eabde85910dce`），其他并发修改原样保护。保三条件非零分母/同嵌套cohort乘积非独立、清聊天非干净、条件激活非全attempt、output/tooltrace非effect、channel/case与裁判限制、T3反退/全费/Unknown隔离回退；接口由持久control cell接纳验收接回原成本和不可变/ephemeral分支，未接管Ch77生命周期或泛安全主线。

当前只真实SAVE/完整selfread，待唯一非writer actualPOST，不预I/DAY，既成仍新增I10＋旧Kimi合计11I。其余十一必要层和有界标题stop/最终DAY保持ordinary；本写入阶段交root即结束释放槽供唯一POST，不因等待扩下一篇Methods。无State/index/他日/stage/commit/push。

## 当前R49–50唯一actualPOST既成采用

上节为R49前保存态。现已实际读回R49–50：本项唯一非writer actualPOST通过、整合生效并释放Ch72窄位，累计新增I11＋旧Kimi合计12I。只行政同步README/本Source/本人H2注，不改通过技术正文或第三AB/date/Source/PRE/POST；其余十一必要层及有限标题stop/DAY仍ordinary，未授本日完成。
