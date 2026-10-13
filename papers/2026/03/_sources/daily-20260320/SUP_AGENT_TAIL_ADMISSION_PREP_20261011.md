# 03-20 补03/19：九个既有 Agent 尾项的准入准备（非 Source/PRE/DAY）

准备者 resume_review17_18，2026-10-12独立恢复重读AGENTS、完整RESEARCH/REPORT合同、Sources使用/每日/arXiv主题、Prompt/ROADMAP、本日README/STOP及最新LS只作路由。仅原有限主题query中作者指定的九个相关/含糊title；不新发现、不继承别日、不把title池自动展开为全文队列。原窗口、Monitor日期/7分与连续§4保持。

## 1. 实际读取层次与日期边界

九篇各实际完整exact-v1题名、作者及Abstract：以下各条abs链接的L15–19（CodeScout L15–18），并轻量读取各当前同ID官方abs的header/Abstract/Comments/history。CodeScout第一次web入口失败，第二次原入口已恢复，不列为必要正文受阻。无官方withdrawn标记；不因版本号自动审全新版。

v1均Submitted03/18，仅作发现/身份，不把提交时间或月表当公开日期。作者报告已取得九个匹配DataCite DOI的registered03/19原字段；在实际读回该持久原字段前，本准备不自行确认新八项日期或加确定分母。后续仅复核自然日夹证，不追精确时分秒。17823另有实际出版方先公开上界，不用arXiv登记覆盖它。

下面八项是具体潜在增量提案，分数是准备者建议、不是自授准入PASS。所有摘要数字和强主张仍未授正文Evidence或Books采用；最小必要Source由独立准入校准后逐篇指定，不在这里预写Books。

## 2. 八个潜在贡献（待非准备者校准）

### TDAD — 2603.17973

[exact-v1完整AB](https://arxiv.org/abs/2603.17973v1)，Pepe Alonso。原只看issue resolution容易漏掉通过测试回归 → AST code-test依赖图与加权影响检索给出应验证的测试上下文，并提出程序式TDD提示反而增回归的局部对照 → 需要分开验收任务修复与既有行为保持、检索上下文与步骤指令的作用。不是仅给coding场景换名或GraphRAG成熟术语；测试级反证与实际patch反馈选择有准入潜力。拟2+2+2=6，候选owner `PLATFORM-EVALUATION-SYSTEM` / Ch66（若实际机制为Agent验证选择，再核唯一owner，不能预先跨章重复）。100/25/10不同子集及多个模型/框架不合并成同分母或普遍效果。

[当前v2轻量页](https://arxiv.org/abs/2603.17973)新增Sergio Yovine/Victor A. Braberman，题摘不再声称10-instance auto-improvement 12→60、0回归；表数3→7且措辞区分模型/框架。此是具体评价信号，后续只定点v2受影响评价/该10子集资格，不把旧v1强主张继续照录，也不全diff/展开repo历史。Submitted03/19的v2不直接当本日新公开事件。

### DebugLM — 2603.17884

[exact-v1完整AB](https://arxiv.org/abs/2603.17884v1)，Wenjie Jacky Mo等六作者；[当前页](https://arxiv.org/abs/2603.17884)仅v1、无具体修订信号。多阶段异质训练后行为难以归到某数据源 → 训练输出与独特source tag的关联，并依数据源触发test-time拒答而不改参数 → 需要判断模型自报tag是否真能作为可追溯来源/定点修复资格，及保utility的适用边界。新命题不是外部日志/一般provenance原则；必要Eq2–6后窄纠为训练标签→debug输出读出与另训输入控制tag→匹配拒答两种条件接口，不是生成标签后的运行时门。拟2+2+2=6，owner待核 `TRAIN-DATA` 或 `TRAIN-SFT` 中唯一训练语义节点；不把learned association直接当因果影响/真实训练溯源。早期消息7仅粗建议，正式提案按新增局部机制Durability2，不借成熟责任原则给3。

### The Silent Thought / FLAIR — 2603.17837

[exact-v1完整AB](https://arxiv.org/abs/2603.17837v1)，Donghang Wu等七作者。常规post-hoc thinking增加说话后等待 → 听用户期间将上一latent embedding递归给下一步，ELBO式teacher-forcing支持无显式reasoning标签训练 → 需要重新考虑full-duplex感知/latent状态/回应时序与泄漏、额外计算预算。不是仅语音应用或人类认知类比。拟2+2+2=6，候选 `MULTIMODAL-REPRESENTATION` / Ch23 的causal streaming接口，实际读后唯一owner再定；不先授无额外latency或严格因果。早期粗建议7同样不借causality成熟原则提高Durability。

[当前v5页](https://arxiv.org/abs/2603.17837)Comments仅Accepted ICML2026、Abstract内容同；看到v2–5history不自动全diff。无具体撤回/纠错/变更机制说明，不把accepted当旧先稿或当前额外事件。

### RPMS — 2603.17831

[exact-v1完整AB](https://arxiv.org/abs/2603.17831v1)，Zhenhang Yuan/Shenghai Yuan/Lihua Xie；[当前页](https://arxiv.org/abs/2603.17831)仅v1。环境动作precondition与belief漂移互相放大 → 检索规则先验约束、按当前belief过滤episodic记忆、rules-first处理冲突，并报告不ground的记忆在部分任务有害 → 需要重新考虑何时旧经验可提升而非破坏可执行动作。不因已知rule/state/memory组合直接排；条件性记忆反证与冲突资格可核。拟2+2+2=6，候选唯一 `AGENT-PLANNING` / Ch79（与Ch77只交接适用性）。ALFWorld134、不同骨干及ScienceWorld不授物理动作安全或普遍transfer。

### CodeScout — 2603.17829

[exact-v1完整AB](https://arxiv.org/abs/2603.17829v1)，Lintang Sutawika等十一作者；[当前页](https://arxiv.org/abs/2603.17829)仅v1。repository localization常依专门静态graph工具 → 复用coding环境、设计reward/RL训练仅有Unix terminal的搜索Agent，并比较多个SWE-bench族任务 → 需要核何种训练/输出资格使普通工具能承担代码定位、怎样与复杂scaffold成本共存。摘要已明确训练环境/reward/optimization是贡献方向，可信度细节缺失不作为EX。拟2+2+2=6，候选 `AGENT-TOOL-CALLING` / Ch78 或训练objective的唯一owner，必要Source后定。2–18×尺寸与closed-model接近是未核对照，不先授更小Agent普遍替代或免费。

### Governed Memory — 2603.17787

[exact-v1完整AB](https://arxiv.org/abs/2603.17787v1)，Hamed Taheri；[当前页](https://arxiv.org/abs/2603.17787)仅v1。因组合贡献是否仅有通用术语，另定点读[exact-v1 §1.3/§3](https://arxiv.org/html/2603.17787v1) L109–123/137–146：组织/实体partition之外，session跟踪先前注入context只交delta；typed属性与开放事实分账、每property rubric驱动schema反馈。多step治理payload反复注入与schema质量漂移 → 具体session-delta交付/属性级自评更新接口 → 需要核规则版本/会话身份、质量反馈是否把自评当真值，及token收益是否只是累积cache。拟2+2+2=6，候选sole `AGENT-MEMORY` / Ch77，治理/执行边界由邻章交接。只确认可核机制，不授生产认证、零泄漏/100%compliance、N250/500或LoCoMo可比性；未读所有七附录/代码。

### Facts as First Class Objects — 2603.17781

[exact-v1完整AB](https://arxiv.org/abs/2603.17781v1)，Oliver Zahn/Simran Chana；[当前页](https://arxiv.org/abs/2603.17781)仅v1。context内单次准确并不等于长期保存约束 → 比较hash-addressed tuple与prompt memory在容量、摘要压缩、级联goal drift以及对抗embedding查询下的有限证据，再提出density-adaptive switching → 需要分开完整上下文能力与经过compaction后的identity/constraint保持、按任务密度选择检索策略。具体负侧证据值得核，即使旧Books有外部记忆并存。拟2+2+2=6，候选sole `AGENT-MEMORY` / Ch77。100%、O(1)、252×和architectural结论都待必要基线/输入资格/路由实现核，不先把oracle-key lookup与开放检索等同。

### CoVerRL — 2603.17775

[exact-v1完整AB](https://arxiv.org/abs/2603.17775v1)，Teng Pan等九作者。label-free majority reward随一致性增强可能塌多样性并自信强化同错 → 同一模型轮换generator/verifier，majority给verifier噪声标签、verifier再筛pseudo-label → 需要核交替训练可否摆脱共偏而不是自我确认，监督人口/错误多样性及预算如何分责。新训练环与consensus trap反证有潜力，不因负侧/数学题局部排。拟2+2+2=6，候选sole `TRAIN-GRPO` / Ch33。自验55→85或4.7–5.9提升不先授独立正确性或真正co-evolution。

[当前v2页](https://arxiv.org/abs/2603.17775)作者拼写差异（Guiyang Hou/Wenqi Zhang）但Abstract内容同，Comments仅project/code；无具体结果纠错说明。保各精确版本作者字段，不机械全diff或把v2later公开搬本日。

## 3. Functional Modules 17823：具体先公开同稿信号，拟窗前处理

[arXiv exact-v1完整AB/current](https://arxiv.org/abs/2603.17823v1)六作者Yanke Yu/Jin Li/Ying Sun/Ping Li/Zhefeng Wang/Yi Zheng，Comments AAAI-26 Oral且仅v1。只因这个具体信号定位[出版方40749](https://ojs.aaai.org/index.php/AAAI/article/view/40749)，实际当前L18–34同题六作者、同ULCMOD/IterD摘要，L40–45明确Published2026-03-14、DOI10.1609/aaai.v40i41.40749、pp34503–34511。

[正式PDF40749/44710](https://ojs.aaai.org/index.php/AAAI/article/download/40749/44710) p0–1实际文字核标题（Function/Functional局部词形）、全部六作者、Abstract及intro dual neuron-sample partition/IterD/同Qwen2.5评价身份；[arXiv v1 HTML](https://arxiv.org/html/2603.17823v1) L47–88/103–117同内容与身份（其HTML题名也用Function）。因此不是仅accepted或search年龄；出版方公开正文上界03/14（即使BJT次日仍早于03/19），当前arXiv无具体delta/纠错信号，拟窗前同稿、不在本补日评分或Books。并未证明最早首日或全稿所有字节完全相同；上述身份/机制足此同家族日期判断，不读所有数学/eval附件。该项有研究潜力，但本日归属不成立，不冒贡献EX或已审跨日dup。

## 4. 交独立校准

作者已持久[九Agent尾项必要日字段](./SUP_FINITE_TAIL_SCREENING_20261012.md)，reader实际定点读其L5–19完整九title/DOI/created/registered及URL身份说明，并回本日[日夹证](./SUP_FIRST_DATE_FIELDS_20261011.md)有效官方availability约束。九registered均UTC03/19、即BJT03/19；与Submitted03/18的官方ID/DOI不预发及最早可能03/19BJT下界合用，八个无具体先稿信号的v1首次arXiv事件日区间完整落03/19。此是日级夹证推断，不把created/注册本身当paper全球firstpublic或精确发布时刻；17823出版方03/14正文上界优先，不让03/19arXiv登记重置归属。没有重新HTTP抓这九JSON，而是复用author具名实际原字段层，身份/version/事件匹配未变化。

日期足身份门即停，交resume_mar17非准备者逐项完整AB/current/必要同稿日期校准；本准备者不自己授Source/PRE/safe/DAY、不改Report/LS/Books或旧分母。当前八项潜力只是提案，尚有可执行必要证据与Books判断，不用普通未读作为外部受阻。不开作者own其余42有限尾题摘。

## 5. resume_mar17 非准备者准入/date校准

2026-10-12实际重读本日适用合同/ROADMAP/README/STOP，仅这九项。独立打开八exact-v1完整AB（TDAD/DebugLM/FLAIR web16–19；RPMS/CodeScout/Gov/Facts/CoVerRL官方exact-v1 HTTP200完整blockquote）和九current官方abs的完整AB/Comments/history；Gov决定准入实际§1.3 109–123/§3 137–146，另定点§5.3 179–183/§7.2–7.5 203–216以核真正的session delta与属性反馈，不遍其余附件。DataCite九exact id/title/url及登记字段本次作者实际HTTP200已SUP_FINITE_TAIL_SCREENING持久，reader定点夹证有效；八本日首次arXiv事件03/19成立，不授权全球firstbody。17823实际出版方18–34同题六作者/ULCMOD/IterD、40–45 Published03/14和DOI，与reader正式PDF及v1HTML身份证据复用，足同家族窗前去重，不要求全稿字节相同或最早首日。

逐项独校：
- TDAD17973：修复通过不等回归保持；实际AST测试影响上下文与单纯TDD指令的反向对照有评价/选择差额，2+2+2=6准入。v2摘要去10子集自动改进数字，但正文§5.5/T7与结论仍保留12→60/0%，不是正式撤回或正文纠正；仅核受影响评价，不授v1 headline或全部版本diff。
- DebugLM17884：训练数据source tag被模型学习并在debug模式随回答读出；另训控制tag与训练样本source匹配时拒答、不匹配时保留原回答，不是生成tag再触发运行时门。两种条件监督确实改变可观察/修复接口而非外部provenance换名，2+2+2=6准入；learned tag不证因果责任。此句按必要Eq2–6窄纠，不重开日期/评分或其他家族。
- FLAIR17837：说话期间递归latent与ELBO teacherforcing产生在线状态/训练时序差额，不是一般“边听边想”口号，2+2+2=6准入；严格因果/无额外latency待必要证据，不借成熟causal原则加Durability3。
- RPMS17831：结构规则与belief筛记忆的成立条件，以及不ground memory在部分任务退化的直接反证可修正“越多经验越好”；2+2+2=6准入，不授动作安全或所有模块独立因果。
- CodeScout17829：既有coding环境改定位任务与特定reward/RL使标准terminal替代专门graph scaffolding的有限对照有取舍潜力，2+2+2=6准入；不是仅尺寸更小数字，未披露细节进入必要审阅而非EX。
- Gov17787：仅AB四成熟模块名不够；实际session记录critical已投递sections而supplementary不登记可后续升级，与属性级replay/diagnostic/refine的具体消费者区分，支持有限delivery/schema评价条件核，2+2+2=6准入。不能把普遍governance/isolation作为贡献，也不自动新写Books；必要Source应核版本变化/恢复与同预算控制，若已有正文具体承载则NC。
- Facts17781：跨compaction的约束丢失与embedding对抗facts、density-switch提供负控制潜力，2+2+2=6准入；hash查找输入资格与开放检索不等价，O1/252x/architectural普遍性不采用。
- CoVerRL17775：共识陷阱与同一模型两角色交替标签/filter有训练反馈差额，2+2+2=6准入；majority teacher并非独立真值，不把共进描述当证明。
- FunctionalModules17823：出版方03/14同稿公开上界优先；不入本补日、不评分、不写Books。非贡献EX或“已审跨日dup”；真实03/14归属只留恢复线索，本日不接前日源审。

八项仅准入校准PASS，不授Source/采用数字/Books/PRE/POST/safe/DAY。最小必要审阅仍按明确命题和直接反侧逐项执行，不自动把所有附件或多个章节展开为队列；未读不是外部受阻。

