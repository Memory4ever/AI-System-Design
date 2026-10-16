# Dec20 Anthropic：两项独立窄命题与逐字PRE

## 1. 身份、日期与实际证据角色

2026-10-15T17:41:53+08:00。Boyle实际打开[Bloom](https://alignment.anthropic.com/2025/bloom-auto-evals/)与[Activation Oracles](https://alignment.anthropic.com/2025/activation-oracles/)原作者当前页，两页明确December19,2025；Newton§3及root实际读回已确认本轮Dec19自然日日门足够，不追旧09点/offset。不是论文submitted日：AO的2512.15674旧论文事件与本日Blog研究披露另责。同一页面当前所见未见撤回/更正提示，不证明全部中间修订。未运行模型、代码或复现实验。

本日旧Feynman完整必要域按精确身份/拟命题复用：Bloom四阶段、seed/config、diversity、40例人工judge校准、self-bias、compute与limitations；AO注入/训练/未参与训练fine-tuned模型审计、Secret Side Constraint反侧、非mechanistic及解释器自行推断限制。作者本次实际读AO当前完整核心与末段，Bloom当前读顶部至四阶段/核心评价所呈现0–101行，不冒新读304行全页。Newton§3实际新读AO必要域、Bloom日期并明确复用旧必要层。

## 2. Bloom：评分、采用域、owner对读

准入链：固定题库冻结了prompt却难按新行为扩展 → 由行为描述/seed配置生成场景并作交互评价 → 配置复现与实际场景人口、诱发率必须分责。评分拟2+2+2=6：重要的生成式评估对象边界；生成器/rollout/judge跨界；稳定的配置与人口区别。不计工具开源、四阶段名称、机构权威或发布数字。具体长期缺口故按受影响域深入，不扩为全部安全benchmark。

唯一owner `PLATFORM-EVALUATION-SYSTEM`，Ch66。作者实际读当前1758–1792完整“Benchmark生成器”节、1529–1546主动probe/回滚分支及完整两侧：已有generator/filter/scorer影响任务人口、保存recipe、主动干预/branch预算的原则，不含“同seed/config重新生成测试”与固定prompt复现的明确分母差额。Ch65调度、Ch67观测的开头交接本日已读；不把生成器配置改写为调度或遥测机制。只提一个自然段，不新增标题/marker，不动现有原文或他注。

证据限定：Understanding/Ideation/Rollout/Judgment与diversity决定生成样本；user/tool response可模拟，非真实effect验证；elicitation率只属于所生成测试。9/10 model organisms结果不是未知部署人口真值；40例/12行为human校准、基于Claude错误调prompt和self-bias不授全场景judge有效性。多阶段模型、变体、重复rollout/judge及人工校准均有成本，不采用普遍优越或风险基率数字。

## 3. Bloom逐字PRE / 完整锚点 / 本人note

位置：Ch66“Benchmark生成器也会塑造被评估的任务人口”中，完整段末“任务生成、优化 patch 与可执行环境的受限证据，不能把其排行榜外推为开放部署能力。”之后；下一完整段以“候选检索也会在分类器之前改写评测人口。”开始。上段完整全文在本日实际读取1758–1778；下段Favia完整原文至family marker实际读至1780。根应在授锁前实际确认当前锚点与并发差额，不能由此包推定空diff。

逐字正文草案（单自然段）：

生成测试时还要区分冻结配置与冻结题目：给定行为描述、seed及各阶段模型/提示配置后，再生成不同情景与对话，同一配置的重跑并不保证相同prompt人口；多样性与变体数、模拟用户或tool回复、rollout停止规则及judge共同决定本次测到什么。[Bloom的受限评价](https://alignment.anthropic.com/2025/bloom-auto-evals/)支持把配置、实际生成场景、完整轨迹与评分分别保存，报告的是该生成过程下的行为诱发率，不是部署风险基率或全行为覆盖。模拟tool后果不认证真实effect，少量人工judge校准、模型organism对照及为已见错误调整prompt也不提供独立全人口真值；多阶段生成、变体、重复rollout/judge和人工复核都计费。需要逐题回归时保留冻结prompt测试，需要探索新行为时才增配生成分支；生成或judge失配时回退人工核过的固定样本与独立行为验证，不由seed相同或零次诱发签发安全。

逐字本人末note草案（保存时只记实际发生层）：

- `SF-2025-ANTHROPIC-BLOOM` — Daily2025-12-20补Dec19自然日；[原作者Blog](https://alignment.anthropic.com/2025/bloom-auto-evals/)，2+2+2=6，具体配置/题目人口缺口深入。只采seed/config与实际scenario/rollout/judge分责；保模拟tool非effect、有限human校准/model-organism/self-bias及全部生成/复核成本，不授风险基率/覆盖保证。Boyle作者；实际Source/PRE及写后状态仅按随后真实发生记录，未核代码或复现，不授DAY。

## 4. Activation Oracles：评分、采用域、owner对读

准入链：固定property probe需要预先声明被读属性 → 以目标activation作为额外输入、受训解释器接受开放问题并审计未参与其训练的fine-tuned模型 → 把可提问的读取接口与泛化/真值验证分开。评分拟2+1+2=5：重要读取机制；单个诊断组件，不借用所有安全生命周期抬Reach；稳定的解释器/目标表示分责。因具体长期缺口受影响深入，非整份论文或全版本比较。

唯一owner拟 `PLATFORM-EVALUATION-SYSTEM` Ch66，而非Ch5：采用的是诊断sensor的可访问输入/问题与OOD审计条件，不重写表示如何形成。作者实际完整读Ch5当前368–389，包括trained-interpreter/null-input两段及上下文；它处理adapter bias/标签先验，不承载AO第1层注入、原target层身份与fine-tune迁移。实际读Ch66当前Scope2前后300–375完整相关正文、4441–4445后续AO confidence完整段及两侧；Scope2处理重建/输出扰动/解释预测/干预，后续2605.26045处理confidence calibration，不含本次问答型activation读取。不是同名即已有覆盖，也不拿后续校准当Dec19原发布证据。

采用必要域：target不同层activation送入AO第1层residual的placeholder位置，prompt保target层号；SPQA/分类/自监督context训练带来先验，不是直接透视。未见fine-tuned activation的AO在四审计任务中三项最好或并列，Secret Side Constraint反侧保留；差分activation也只是诊断输入。解释器可能超出目标表示自行组合/猜测，不exhaustive、不mechanistic，不能由流畅文字认定target已有结论或因果机制。访问activation、解释器训练、重复forward及独立验证付费。

## 5. AO逐字PRE / 完整锚点 / 本人note

位置：Ch66Scope2完整第二段末“解释不稳定时回到独立行为测试，不能让更稀疏的图取得发布权。”之后；下一完整段以“内部状态变化的大小与可干预方向也须分开验收：”开始，全文至2610.09493 family marker。上为本日实际冻结Scope2两段，下为来源冲突direction/梯度/等层范数对照完整段；两侧作者已实际读。此处不改旧Scope2/他note，未获root窄位前不写。

逐字正文草案（单自然段）：

固定属性probe之外，还可把目标模型的activation作为额外输入，训练另一个模型接受自然语言问题并给出诊断；[Activation Oracles的受限分支](https://alignment.anthropic.com/2025/activation-oracles/)把不同target层的向量注入解释模型第1层的placeholder位置，再在提示中保留原target层号，故采集层、注入位置、问题与解释器训练人口都属于sensor身份。它在未参与解释器训练的fine-tuned模型上展示部分迁移，不等于通用内部真值：四项审计中仍有Secret Side Constraint反侧，回答也可能来自解释器自身推断或猜测，而非目标模型已经表示该结论；这不是完整因果机制恢复或穷尽审计。activation访问、解释器训练、多次forward及独立行为验证均有成本；属性明确且标签可靠时固定probe仍合理，迁移或解释不稳时保留原输入/activation与外部行为测试，不让可提问或可读解释取得编辑、发布或安全认证权。

逐字本人末note草案（保存时只记实际发生层）：

- `SF-2025-ANTHROPIC-ACTIVATION-ORACLES` — Daily2025-12-20补Dec19自然日；[原作者Blog](https://alignment.anthropic.com/2025/activation-oracles/)，2+1+2=5，问答型activation sensor具体缺口深入。只采target层/解释器第1层placeholder/问题/训练人口与OOD审计分责；保Secret Side Constraint、解释器自行推断、非mechanistic/非exhaustive及全部访问/训练/forward费用，不采内部真值或安全保证。Boyle作者；实际Source/PRE及写后状态仅按随后真实发生记录，未核代码或复现，不授DAY。

两项评分/唯一owner/采用域/逐字PRE交Newton实际校准；root先读Source与当前完整邻接再决定是否授具体窄位。本包不是写许可、已整合、POST或DAY；无内部send_input，落盘供root转，作者继续本日有限Source/date/six。

## 6. root1窄许可后真实保存 / 作者完整顺读

Newton5已实际两项Source/分数/owner/逐字PRE通过；root实际读当前两锚点/Ch5null/后AOconfidence/Ch65–67边界后ROOT_REVIEW§1授两不同窄位。作者写前实时读Ch66完整Scope2两段/来源冲突后段，生成器完整filter段/Favia后段及末前注；实际unstaged0、cached8、基线index3519f71。首次patch因末前注手抄不匹配拒绝，第二次因hunk顺序拒绝，两次均实际回查unstaged0，未部分写入；按正文先后顺序重新apply_patch真实成功，不改许可文字或他原文。

作者随后实际顺读当前339–347完整AO新增/Scope2前两段/来源冲突后段与其后编辑段，1774–1785完整Bloom新增/filter前段/Favia后段与工件核验段；末前注及两本人note全文实际读。正文逐字等于§3/§5 PRE，只各一自然段，不加标题/marker、不改旧Scope2/他注。自身notes仅记录已经发生的Newton5/root1写前层和保存，不预POST。限定unstaged diff实际8add/0del（两正文+两note和空行），cached8仍保持；两层diffcheck均exit0。未stage/commit/push，未写State/index或其它Books。

随后已发生：Newton8实际Bloom完整新增/两侧/本人note POST通过，Newton9实际AO同范围POST通过；root2实际全文读Source6、Newton8/9、两新增/上下完整段/两本人notes与前注及两层diffcheck，真实接纳两整合并释放两窄位。作者按该许可仅同步两本人note尾部行政状态，不改正文/他注，不重Source/PRE/POST收据；两整合不代DAY，当前无本项余锁。
