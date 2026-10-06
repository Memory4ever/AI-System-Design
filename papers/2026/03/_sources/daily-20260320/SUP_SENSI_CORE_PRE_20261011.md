# Sensi17683：课程完成到整批事实晋升的窄证据

resume_mar17，fresh03-20补03-19。2+1+2=5、完整AB/必要日期与一次准入消歧独核§6有效复用。本次[exact-v1](https://arxiv.org/html/2603.17683v1)§3.3、§4.1–4.5/Eq9–17/Listings1–4、§5/6/Table2、§9及B单turn算法必要L134–420/438–442/536–576实际核；不读全部AppendixA实例/repo/版本diff。本文Sensi v1/v2是系统迭代，不混成arXiv版本。

## 可采用事实与真实反侧

FrameDiff读连续两帧rendered image→JSON变化，Player1读frame/diff/旧guess/K/facts/目标/评分feedback后更新lists；Player2只消费这些摘要/目标后提动作。MetricGen每课程item一次，SenseScore每turn；Listing4只有item、生成rubric、facts、figured_out文本，无frame/独立环境真值。都是Gemini3.1Pro不同调用，并非独立模型/训练源。≥8分将课程item标completed，Eq10把当时整K晋升fact，作为下一课程的累计上下文。B算法具体是先SenseScore旧K_(t−1)→旧K整批promote→Player1产生新K_t，不能描述为先评当轮新观察再写入；正文Eq10的t索引不能机械拼成完整实现。无需repo才能支持“课程级评分用于批次事实晋升”的明确接口。

Table2 GPT5.1ThinkingHigh的系统v1解2关，Gemini3.1Pro系统v2解0关；不同backbone/组件同时变化，非控制架构因果。F3约32turn只是illustrative、变化未量化；Agentica reported1600–3000未匹配backbone/任务/成功或学习完成定义。32课程完成不等32次学到正确规则；不采50–94×/humanlike/直接降费用。高评分但错误facts的Eq17/§6.4是作者明确负观察，足反驳“完成=真实学会”的采用权；不授error率、所有游戏或仅perception单因。§9(5)自认scorer内部一致而非truth，§7与Conclusion“架构validated/onlyperception”缺独立perfact核验、matchedbackbone/grounding干预，不采用。

每turn至多五LLM调用，MetricGen仅新item时一次；frame渲染/JSONdiff、SQLite维护、reset/全部交互与prompttoken成本存在。作者未充分披露真实全模型版本/请求预算、token/latency、重复seed/人数、不确定性或全费用；不将tries比直接换墙钟/成本。课程handdesigned，不称自主课程发现或梯度学习。Environment observation、hypothesis、scorer与事实标签权限各分开。

## actual owner：具体差额而非主题

实际完整Ch77 L78–147已读：write/hold五分支、per-target evidence/version、accepted/pending隔离、L129高trustpoison/accepted≠truth、L141–147失败反思pending。Ch80 L45–95真实self-score漏检/反馈独立及环境反证，Ch81 L78–112真实activation/pre-state/judge权限，Ch78入口1–40交接已读。既有覆盖强，不能再写通用“DB不是真值”“samejudge共偏”段。

仍有窄差额：不是单条write或全局信任打分，而是**课程item的一个完成分数批准整批K的事实状态，随后批次被下一课程继承**。同一个item-levelpass并未逐条核K，B旧K先评分再晋升使读取/写入对象版本也须绑明。拟Ch77 L129完整poison段及familymarker后，per-item value分支之前仅一段，补不同验收单位及具体已观察cascade；不向Ch80/81重复理论。若独核认为现L108–129已完整承载该粒度差额，可具体NC指明，但不能凭memory主题或为缩待办作NC。未授锁。

## 逐字PRE（待非准备者）

批次写入还须区分验收单位：一个课程目标的完成评分，不能自动批准它积累的每条候选事实。[受限游戏 Agent 的负观察](https://arxiv.org/html/2603.17683v1#S6)中，judge 只读取目标、动态 rubric 与已有事实/候选文本，达到门限便把整批 figured-out 项晋升为 facts，供下一课程继承；错误视觉描述因内部一致而得到高分，课程流程完成却未解决任务。这里暴露的是 item-level completion 与 per-fact admission 的错配，而不证明只有感知层需要修复。应把评分实际消费的批次版本与每条证据绑定，课程推进和事实晋升分别受理，缺独立支持的项仍留 pending；这些是写入边界要求，不是原系统已实现的修复。逐项核验、原帧回读与多次模型调用增加费用，未匹配的课程完成次数不等正确学习或部署降本；证据不足时保留原观察和已有写入 Gate，而不让一个高分为整批内容签真值。<!-- source-family:SF-2026-ARXIV-2603-17683 -->

静态注：`SF-2026-ARXIV-2603-17683` — [exact-v1](https://arxiv.org/html/2603.17683v1)§4–6/Listings1–4/Eq9–17/Table2/§9与B单turn时序。仅课程完成→整批facts继承的验收粒度/版本错配与作者负观察；不采50–94×、onlyperception或架构已验证。系统v1/v2换backbone、循环/全调用费用保留；未核代码或复现。

## 采用边界/一次重开请求

若未来采用中心sample效率或“修perception即可成功”，仅一次请求同backbone/同任务完成与成功分母、逐事实groundtruth/批次版本trace及独立grounding干预和全LLM费用；当前有限负观察不依赖该强结论。待非准备者Source/实际owner/逐字PRE裁，不预授safe或DAY。
