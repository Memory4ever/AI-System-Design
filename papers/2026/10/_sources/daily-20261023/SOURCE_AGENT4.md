# Oct23 Daily — SOURCE_AGENT4

仅本日29135/29139/29467/29491/29680v1/29822/29934/30041。复用[ARXIV](ARXIV.md)有效完整AB、准入、初分和官方Oct22公告mapping，不第三审/不扩源或别日。root唯一Books/Report/State writer；本作者只Source/原件/actualowner/PRE，reader非作者核；PRE不等实存或POST。MODEL5具名独核/已保存POST优先，无review-ready时推进本批。

原件提取修正：G3与G6首次附录缓存因同一输出随后附带owner查询，误拼少量中文Books尾段；该段非primary、未作论文证据。已按exact-v1当前临时HTML中原限定字节域独立重提并移除，保原有效方法/反侧/PRE；不扩源或重开未受影响结论。其他尚未保存的G7附录在独立提取后才存。

## G1 2610.29135 LaVGuard — 2+1+2=5；必要Source；拟整合

- [exact-v1](https://arxiv.org/html/2610.29135v1)，实读§3.1–4.5/式1–13、§5.1–5.5/表1–4、§6/Limitations，必要B3–B4费用/记录、F5重复单位定义、K3局部与完整响应estimand；[正文原件](agent4-source-2610.29135-v1.txt)。未核实现/复现，未遍全附录，不采用所有理论上界为现实保证。
- 外部authorizedprofile是10维强度非概率simplex；冻结Qwen2.5-7B四层tap最后16visibleprefix位置probe，数字profile不进probe。当前估计减profile后的admissible residual GMM density只决定when，posterior residualmean平移/clip所得prototype决定where；prototype甚至可能不在density levelset内，不冒合法价值真值。
- 越界且剩余双budget时，对原distribution top32候选各extendedprefix重forward，至prototype距离的有符号改善作logit方向，未评分tail置0但仍同受全vocabnormalizer，不能称只top32概率会变。nonconstant方向以固定direction作[0,1]scale KL二分，改变的是samplingkernel的位置数与实际conditionalKL；constant/零scale不花positionbudget，触发事后共同安全guard的采样仍保之前费用。所有编辑与base共用guard，taskcompatibility与contentsafety分开。
- 理论tilt的localexpected surrogate进步不等humancompatibility、终局风险下降；KL链界还依共同guard/termination/真实kernel与有限horizon，不移植到不同temperature/top-p/guard支持。此处仅采用接口/费用，不照数值控制recipe。
- 200variants/100families，familygroup140/30/30=70/15/15，3annotators+争议裁决；referencehorizon256、M32、K2、两budget+20bisection。主表mean±sd未闭合独立重复unit/seed数与硬件，F5说明应声明但未补出具体数，写Not Disclosed而不补显著。reference可执行protocol与tables source-study readouts区分；均值tokenratio=.12/KL=.04非逐响应/逐prefix严格匹配。
- baseline benignsafety.84→full.81、overrefusal.03→.08；相对SafeInfer反拒较低不等无utility损害。alltoken risksafety.89vsfull.88且benignutility.68vs.81，不写full全指标好。830ms与独立efficiency920/1200ms是不同series，不能拼P95/SLO；activecandidateattempt可多于真正editedposition，use_cache=False无KV复用，probe/32候选/guard/search/标注/拟合全付费。精确测试效应只该任务/模型，跨language/value争议/longresponse需重核。
- actual owner `PLATFORM-SECURITY` Ch72 valuefilter2605.14746完整段已有“少改安全输出不等干预后安全”与阈值支持边界，却没分content-safe内部的authorized taskpriority/profile与kernel位置/KL两种预算；补此具体controller接口，不另开价值观分类或通用道德真值分支。插点该完整段后/“单次文本脱敏也须分开…”完整段前。
- 逐字PRE：

> 同一 content-safety guard 内，还可能有与任务优先级不相容、却不触发有害内容规则的延续；可由授权 owner 声明任务 profile，让冻结 probe 只估计可见 prefix，再以相对 profile 的密度边界提出干预。边界决定何时试，候选向 prototype 的有符号进步决定 logit tilt，两者都不是价值真值或执行授权。[LaVGuard 的受限分支](https://arxiv.org/html/2610.29135v1#S4)分别限制 sampling kernel 改变的位置数与累计 conditional KL，事后被共同 guard 拒绝的采样也保留已花预算；少改位置不等少计算，候选重算甚至可尝试后不接受编辑。局部 surrogate 进步不签任务相容或全局安全，profile/语言分布变化仍须独立人审；probe、边界拟合、全部候选 forward 与控制求值都付费。授权、校准或净效用失配时保原已验解码、共同内容检查与人工澄清，不让低 KL 或偏好提案覆盖安全 policy。
>
> <!-- source-family:SF-2026-ARXIV-2610-29135 -->

### G1 完整actual上下锚快照

上段完整：

> 安全过滤还须分开“少改原本安全的输出”和“干预后真的安全”。一条[受限value-filter分支](https://arxiv.org/html/2605.14746v1#S3)保留超过阈值的next-token候选，再按原policy概率重归一；它与对全部token指数重权不同，但理想安全单调/floor依赖真实base-continuation value及每个可达prefix有非空支持，不能直接授给learned probe。对base生成且按明示judge规则判安全的完整轨迹，可用沿途最小probe分数校准阈值，在固定估计器与交换人口下限制误干预这类轨迹的期望；这不控制新policy的真实有害率、每个prompt风险或域移安全。部署有限重采样还有另一接口：所有候选都未过线时仍取最高分，会离开阈值过滤的支持，不能再继承hard floor。判安全的标签本身也可能错，cosine接近原输出和更遵从意图都不认证事实/安全质量。训练probe、生成与标注校准轨迹、全部候选forward/重采和独立效用安全回归均付费；阈值附近失准、支持为空或费用超界时，应保留可信外部policy检查、拒绝/人工路径与原已验收解码，不由一个误干预预算批准危险输出。<!-- source-family:SF-2026-ARXIV-2605-14746 -->

下段完整：

> 单次文本脱敏也须分开“什么算敏感”和“在已定义类别内怎样取舍误漏”。一个受限模型分支将autoregressive checkpoint改为双向局部attention与BIOES token classifier，一次forward后用Viterbi合法转移和bias选择敏感span；运行时调整precision–recall不等于改隐私taxonomy，新的敏感类别仍可能需要重新标注与微调。窗口和可接受输入长度也不同：长文能送入模型，不保证相距很远的别名/间接线索已连通，更不使被保留文字自动匿名化。

## G8 2610.30041 Behavioral Localization — 2+1+2=5；标准Source；已有覆盖

- [exact-v1](https://arxiv.org/html/2610.30041v1)，完整必要正文§3.1–3.2/式1–5、§4.1–4.2/表1及intro直接边界；[正文原件](agent4-source-2610.30041-v1.txt)。HTML正文到References无额外方法附录；未核代码/复现，不把少量配方缺项冒外部blocked。
- 冻结Qwen3.6-35B-A3B，在同一GPT5.5 verified-success teacherprefix上比较有textskill/无skill两条件；goldtoken logprob差G乘全词表JS作位置proposal，topk%位置fullvocab KL拟合有skill分布，另在preservation位置锚无skill分布，只训8inputembeddings。式G有符号，不自补positiveclip、loss权重、具体preservation选法/optimizer/步数；这些Not Disclosed。不由冻结backbone断言未选状态不改变。
- 图1是61successfultrainingtraces的teacherforced正goldlikelihoodgain集中度，top10%捕获96.12%不等因果必要性或实跑收益。共享280任务：103/280低于text118/280和OPCD107/280，虽高于fulltrajectory85/280；taskspecific61：35/61高于text32/61与OPCD30/61，但训练/评测taskoverlap及独立heldout协议未披露，不能断言leakage，也不能跨两个分母论证泛化。Textskill在此不是严格upperbound。
- greedy、4096token上限、600s timeout，全部SpreadsheetBench检查才成功；未披露独立重复/CI，只有该模型/该任务域，不授其他Agent/安全或全部保能力。Teacher生成与验证、两条件全forward/fullvocab分布与JS、prompt训练和真实rollout全计费；8tokens不等总训练/运行省费。
- actual owner `TRAIN-SFT` Ch29完整2602.00425段已分监督mask/完整历史/非因果/全forward成本；2602.17186完整段已比较同gold在两条件下的gain、其模型/扰动相对性与未选位置仍影响后loss；当前2610.12995 CIG完整段又明确条件gain proposal非互信息、与KLtarget分责及双forward全费。Ch75 2609.31430完整两段已承载compressed输入学习/原view baseanchor分责与软anchor不签行为。G×JS在受限softskill下是这些判断的局部selector实例，而非新的监督权限/状态链；不把组合名强加新分支。具体NC，不声称现文已有该乘积公式；局部质量反退/分母与recipe缺项留报告，不新增Books。

## 作者停点

八项必要Source/actualowner作者层齐：G1/2/3/4/6/7六个最小PRE由reader非作者必要源/owner/PRE独核，root真实保存后亦由reader六项actualPOST齐；G5/G8两个具体NC非作者通过。root已具名确认全八入Report185/189，本注仅行政同步既成具名消息，不代DAY；不重读已有效层。无源扩扫/历史恢复，无Books/Report/State写入；转WORLD2非作者必要独核，不自签本批。
## G7 2610.29934 ToM2Vec — 2+2+2=6；必要Source；拟整合

- [exact-v1](https://arxiv.org/html/2610.29934v1)，实际§2.1–2.4/式1、§3.1–3.4/表1–5、§4/表6–8及Limitations，必要A/B训练/数据与C统计+费用/Table14；[必要原件](agent4-source-2610.29934-v1.txt)。不遍falsebelief附加cases/全部prompts，不核code/复现。
- 训练partner有私有context与实际generatedthought，按sentencechunks提K−2中心hidden+首末Ktargets；main只本地view自回归K连续lastlayerhidden回馈embedding，cosine逐位匹配，K10是配置。训练两方同model共享坐标是资格，不能把异构partnerhidden直接cosine。只用此ToMloss、非taskRL；目标是否detach/全部target优化实现未核，不补frozen-target完整recipe。
- 部署不读partner真实thought/私有context，main自行预测10latent再condition自己的文字reason/action；这是privilegedtraining→localinference分责，不是运行期隐式读取他人隐私或真实mindreading。连续表示容量不证明同时覆盖多个真实hypotheses/概率校准；不能由作者abstraction叙述认证不确定性。
- Qwen3-8B基座是posttrained非裸pretrain，Overcooked3layouts×30seeds/400steps，100negotiations、1000Decrypto、100Hanabi，Capture6/Escape12seeds很小；成功/turns分母不混且并非所有对照全指标严格胜，EscapeSRtie .92且SimToM7.80turns<ours8。训练randomagent采4000states，各域配置；Negotiation500setting/24turn后按samples80/20非明示session-disjoint，不能自证独立heldout或指控泄漏。
- Overcooked106.7vsbase94.7/Language97.6；语言baseline改监督/解码接口，未闭所有token/训练totalbudget控制，不能把全部差唯一归latent或text必单假设。transfer20seed只Overcooked Gemma4/GPT5.4有限未见partner，不证明所有域/新family。Oracle有额外真实private信息，仅reference，不认证可部署真实上界。
- 300samples×3sixoptionprobes：belief/desire真值由partner续写自报、action来自真实nextaction；52.3/62.3/64.0是限定标签可读性，不是人类心理真值。contextcorrupt(换layout/诱导adversarial)PPL变化支持contextsensitivity，不隔离唯一ToM因果或实际行为necessity。**主文称negotiation显著，但C明确五McNemar比较均未显著**；按C收窄不采用主文显著。C Hanabi20/100seed表述亦不一致，保局部结果不自补统一统计或显著。
- A披露AdamWLR1e-6/batch4、QwenT1 topP.95 topK20/presence1.5，evalGemma与GPT不同配置。Table14 vanillaHF/A6000约11491.8→12641.9ms增加1150.1、16.3GB相同/训练84GB；20generationsteps与training50steps是不同测量描述，未披露完整并发/尾时延不补SLO。固定10步非固定墙钟、同peak不等零memory/KV；partnerthought采集/隐状态提取、训练、10forward与普通reason/action、probe/所有rollout均付费，不说one-time无成本。
- actual `AGENT-MULTI-AGENT` Ch82 Behavioralbelief段已有响应策略预测vs认证身份，后接CollectiveAgency定义；latent通信前段拥有真实sender表示/translator，不覆盖**只在训练读partnerthought、同坐标抽取监督、部署从自身view生成partnerlatent**。差额为训练特权与推断可见边界，不重复Ch29通用latentreasoning或Ch75context管理。精确初始belief完整段后/CollectiveAgency完整段前，Ch81/83交接已读。

逐字 PRE：

> Partner belief 也可以先在训练期学习连续表示，而不在运行期索取对方消息：同模型 self-play 时，从 partner 的实际 reasoning hidden states 抽取固定数量 targets，让 main agent 只用自己的可见 context 预测它们；共享表示坐标是逐位 cosine 对齐的前提。[ToM2Vec 的受限分支](https://arxiv.org/html/2610.29934v1#S2)部署时不再读取 partner 私有 context 或真实 thoughts，而用自产 latent 条件化后续 reasoning/action，这不是异构 hidden states 可直接互换，也不证明连续 token 已覆盖真实多种意图。Partner 自报的 belief/desire 标签与更低 thought perplexity 只支持局部预测，不能认证真实心智或唯一因果；有限跨伙伴收益也不授身份、许可或通用协作。采集 partner thoughts、表示提取/训练、固定 latent forwards 与全部交互仍付费，固定步数不等固定墙钟。伙伴、表示或实际协调质量失配时，保显式 typed message、原本地 policy 与外部协议检查，不让预测意图替对方作承诺。
>
> <!-- source-family:SF-2026-ARXIV-2610-29934 -->

完整上段：

> Agent 可从 interaction history 推断 co-player 的响应策略，并据此调整当前 action；这能在重复博弈中形成快速适应，也会产生 strategic shaping、collusion、belief poisoning 和 equilibrium drift。Runtime identity 回答“对方是谁、拥有什么权限”，behavioral belief 只回答“根据有限历史，对方可能怎样行动”，二者必须分开存储和校准。外部 policy 仍定义什么合作可接受，模型不能用预测到的互惠收益自行放宽授权。受控 repeated-game 实验证明 partner diversity 可诱发有限的 in-context adaptation，不证明现实 Agent 会自然合作或隐藏身份更安全。

完整下段：

> 把一组协作者当作一个有目标的Agent，还需要另一层建模资格，不能只因观察到合作就归一个共同utility。可先固定个体机制、聚合变量的映射与可执行干预，再检查“先在低层干预后聚合”的分布，是否与“映到高层后干预”一致；更强抽象还要求高层干预都有低层实现。[Collective Agency的受限形式化](https://arxiv.org/pdf/2605.00248v1)依赖所选rationality和因果模型，常量utility会让agency解释空泛，一步actor–critic构造及有限voting模拟也不识别真实LLM群体的隐藏目标。聚合、干预采集和surrogate拟合增加成本，学习中的nonstationarity会破坏静态模型；干预支持或预测不可靠时，保留逐Agent机制、个体/群体结果和外部权限审计，不由共识或一个拟合目标认证集体安全。<!-- source-family:SF-2026-ARXIV-2605-00248 -->
## G6 2610.29822 UserSWE — 2+1+2=5；必要Source；拟整合

- [exact-v1](https://arxiv.org/html/2610.29822v1)，必要§4.1–4.3/Alg1、§5.1–5.3/表3–5、§6，C1–C3/Alg2完整environment/judge/settlement、D2统计/D3费用；[必要原件](agent4-source-2610.29822-v1.txt)。不遍全sessioncases/各任务，未核实现/复现。
- 72tasks/42repos：22维护者明确相连双issue+50单issue改多轮，池由历史/goldpatch构造并机械/人工admit；完整pool/acceptance对evalinstrument可见而agent不可见，不由gold-derivedpool声明零泄漏。释放策略依本轮agent问答/执行结果选内容，persona链任务级预采并跨agent固定；固定what可能说与howvoice，不是固定每句回复或不同agent始终获同内容。
- 20859内部开发session中13530codechange用于8格persona，clarity×causeveracity；opening-conditionedtransition不是globaloneMarkov，aggregate不天然真实全用户分布。Persona链冻结消掉一项随机instrument差，但simulator反应依agent，未锁定全部措辞；静态clearcorrectablation50单issue同任务配对，3/4降但Kimi反升，不称所有agent通规律。
- 每turn真实测试、Judge写/不同familyReviewer inlinegate，可rewrite完整state/verdict/evidence/nextmsg；reviewunavailable停而非绕过。canonicalpass覆盖模型N，equivalenceY无validattestation还N，workspacefingerprint变更不准自报noedit，itemset不同failclosed。两个family/互换角色不等独立正确oracle，40.9%rewrite仅有变更并非gold正确率/误判率。
- 必要C3/Alg2：testrewrite必须新change且可执行；在candidate rewrittenpass+regressionallpass，base rewrittenfail，最后Reviewer行为approve才能只更新requesteditems及记录attestation。只说明有限输入合同，不形式证明所有patch语义等价；同样能错把弱rewrite批准，canonical/rawfail和改写身份须保留，不让自然语言认可冒执行。
- 单issueK5、cascadeK8，noedit按.5计，LDPR成功时(K+1−k)/K否则0。第8turn累计72分母包含早在K5终止的单issue，不是所有任务都获8次；turndiscount非tokens/墙钟。不同scaffold+model共同作为subject不等纯模型排名，拒答记unresolved。榜序随budget/metric变化只72任务局部。
- D2 taskbootstrap95%/pairedpermutation55pairs BH5%：LDPR17pairs vs首轮/全预算各5，不能由邻榜点估计断言每对显著；同task的多turn非独立样本，无额外独立训练/重复session保证。D3 availabletelemetry，agentmean但judgecost/editsmedian，tokens排cachereads；不得相加mean/median装全费，wall单位/完全硬件精度并发ND不自补。任务采集/pool/用户模拟、全部agent/tool/tests、Judge/Reviewer/rewrites/失败均计费。
- actual `PLATFORM-EVALUATION-SYSTEM` Ch66 InteractWeb完整段已分private需求/逐轮披露与相同预算，却未将**固定persona链/动态release、预算曲线、testrewrite执行资格**明确成可复查instrument。TRAILS及规范检查已说运行不是语义证书，未有改写test必须candidatepass/basefail/regression+独立行为settlement接口。最小同owner补一段在InteractWeb后/HTTP质量标题前，不另开codingbenchmark支线；Ch65/67交接已核。

逐字 PRE：

> 交互评测还应冻结可释放的信息池与任务级 persona 链，再让本轮内容随真实响应和执行结果选择；固定说话风格轨迹不等所有 Agent 获得同一消息。应报告随交互预算变化的成功曲线，并把无代码改动的讨论轮如何计价说清，轮次折扣不是 token 或墙钟预算。[UserSWE 的受限设计](https://arxiv.org/html/2610.29822v1#S4.SS3)还允许替代实现请求 test rewrite，但须实际在 candidate 通过、在 base 失败且无 regression，再由非原 Judge 的 Reviewer 核行为合同并留下 attestation；模型称等价不算执行，有限测试也不证明完整语义等价。原测试、改写与 settlement 身份须并存，跨家族复核不自动提供独立真值。构造、用户模拟、每轮执行与双侧判分全计费；模拟分布、oracle 或预算失配时，保原 canonical fail、独立人工检查与静态完整需求参照，不由更高多轮分数批准生产正确性。
>
> <!-- source-family:SF-2026-ARXIV-2610-29822 -->

完整上段：

> 交互式构建任务还须把评估者知道的完整需求与Agent每轮实际获知的信息分开保存。可从同一gold specification删去、模糊或冲突改写部分条件，让模拟用户仅回答本轮明确询问的slots，再分别记录需求恢复、实现和最终可执行结果；隐藏条件的completion因此包含主动获取信息，不能全归为对初始请求的代码能力。[InteractWeb的受限设计](https://arxiv.org/html/2604.27419v1)提供这条接口，不使模拟persona成为真实用户分布，也不让额外UI自动等同事实幻觉。完整gold直接给出、相同交互预算与独立功能/人类评价仍是必要参照；需求权重、gold到改写的对应和用户泄露规则都须可核。生成改写、模拟交互、浏览器执行、判分与人工审校均计费；恢复不了的隐藏条件保留Unknown或明确的默认许可，不让测试者私有偏好代替用户授权，低风险完整需求仍可沿原静态验收。<!-- source-family:SF-2026-ARXIV-2604-27419 -->

完整下锚（标题及其完整首段）：

> ## HTTP 成功只是质量判断的第一道门
>
> 拒答能力也应交叉真实输入缺陷与提示中的缺陷断言，而不只给模型一批坏问题。保持query、schema和reference label不变，分别给正常请求、“可能有错”及“肯定有错”提示，在真实无缺陷输入上就能检查是否只是服从指令而拒答。[PremiseSQL 的受限配对](https://arxiv.org/html/2610.22158v1)显示更高的缺陷检测可伴大量正常请求被拒；`is_valid`自述、是否生成、条件执行正确率及全部请求效用仍是不同分母。合成缺陷/双judge与可执行gold子人口不能代表自然用户所有错误；构造、执行、人审和配对调用均付费。前提无法独立核实时应澄清或Unknown，保留原schema与可靠执行检查，不让模型的否定答案自己定义问题真值。
> <!-- source-family:SF-2026-ARXIV-2610-22158 -->

## G5 2610.29680 TraceForge — 1+2+2=5；标准Source；已有覆盖

- 只[exact-v1](https://arxiv.org/html/2610.29680v1)，实读§2.1–2.4、§3.1–3.3/表1–2及§4/§5直接自限；[正文原件](agent4-source-2610.29680-v1.txt)。不混次日v2，不以当前较长版本替v1，不核artifact/复现；作者legal/terms判断不采用为本项目结论。
- 生成器读取system/user/**answer**/tools重建R，SFT仅Rloss，target来自学生Qwenfamily；critic用真实familyR与匹配generatedR辨真伪，5轮各5000online样本，骗过critic者回流critic、未骗过者成generatorDPOpreference，推断bestof4由critic选。它是答案已知的派生trace，不恢复teacherhidden computation，也不让authenticity成为stepcorrectness；critic至少generator大只是作者观察，不写普遍小模型不能judge大模型。
- 独立judge authenticityreal .66/gen .68/best4 .82只测familyresemblance，不是任务准确率/无幻觉。主文小criticheldoutpair拟合shortcut给generator无效，保留judge/选择目标失配。Teacheranswer能错，generatedR也可posthoc rationalize。
- 下游统一Qwen3.5-9B-Base，全参BF16/8H20TP4PP2/seqparallel/AdamW/no shuffle/seed42，约1600packedbatch步，单row<262144但packing长不同不等同tokenbudget。S1/S2同prompt+Fableanswers换trace，S4/S5同Solanswers换synthesizer；S3同时换answers+traces，不能当style独立ablation。**AB摘要写3500questions，正文setup明确5000pool，原内部口径冲突不替作者补解**；原语料confidential不可外部查训练数据，不阻塞论文限定的局部结果但不授provenanceclosed。
- S2末HumanEval68.29vs64.63/MBPP59.52vs52.38；HumanEvalstep600 S2 56.10<66.46且step90066.46略低末之前变化，不能称各checkpoint都胜；MBPP各测checkpoint局部领先。S4step90021.95/42.59→末3.66/6.61显示collapse不是全程差；S2HumanEval亦非单调。每cell1run、仅重复测S1step1200两次是evaluation而非trainingseedreplicate，未授显著。ARC/BoolQ无大差不等全通用能力不忘。
- 同family更易吸收/少遗忘、Qwen训练中过Claude数据等均作者假说，没有parameterdistance/因果控制；本文§5自己承认两synthesispipeline未隔离style全部差异。纯familyrewriteanswer额外variant仅essentiallysame叙述无表细节，不采用定量保证，更不背书来源合法/无需permission。
- 全familyteacher十k、generator/criticSFT+五轮DPO、best4/judge、closedteacheranswers、长sequence完整SFT与全部checkpointevaluation均计费；不宣更小adaptationcost、稳定性或端到端更省。
- actual `TRAIN-SFT` Ch29当前2603.12397完整两段明确固定QA换trace会改变跨任务行为、trace/answerloss分账及同step不同token总费；2604.01702完整段明确答案正确≠轨迹值得学、teacher–student配对与独立heldout。Ch27当前Reasoning数据完整性段亦把query/answer/trace lineage分开。此稿为派生trace另一局部生成/selection组合，但familyauthenticity不提供新的correctness权限，实测收益不足确认family因果/抗遗忘。具体NC，不称现文已覆盖五轮criticrecipe；保其匹配比较和v1反侧在报告，不新增Books命名分支。

## G4 2610.29491 RubricOpt — 2+2+2=6；必要Source；拟整合

- [exact-v1](https://arxiv.org/html/2610.29491v1)，实读§3.1–3.3/式1–9与Proposition1条件、§4.1–4.3/表1–3、Scope，必要C2完整五stage+deterministicgate及C3 matchedcontinuation；[必要原件](agent4-source-2610.29491-v1.txt)。不采用B完整proof/finiteupdate或retention保证，未核code/复现。
- Pair/labels/length-normalizedDPOobjective固定，训练时给同pair两response、policy与frozenreference相同Prefer/Avoid语境，rubrictokens不进responseloss/分母。按pair独立随机暴露并逐步撤除，最终评测不带rubric。不是用rubricscore重标pairs/当reward，也不等数学目标sumDPO完全未变；固定的是本文两臂recipe。
- 手定8factors，successful-vs-failed judgeordinalmeans差D仅关联；supply为同pair chosen−rejected factorcontrast频率，不是缺数据能力真值。Currentpolicy读自身无rubric输出的gold/外部judgefeedback，五stage诊断/综合/归因/最小改词/audit。已完整覆盖失败的条款应keep（未学会≠spec遗漏）；gate校canonical旧bytes、factor一一/PreferAvoidpair、anchor词/长度/证据eligibility；auditPASS是advisory，原f3 rewrite audit过却gate拒。Crossfactor词仅warning非必拒，deterministic不认证内容语义/安全/证据真。
- Prop1只共享参数/reference下固定方向、有限prompt/response、positiveC1policy、小eta的一阶success差；semanticprojection residual也可决定符号。本文不采用全局收敛/优化保证，语义同轴不证明真实因果或全部能力保留。
- Qwen3-4B/8B、Mistral7B，rank64/alpha128/dropout.05、LR1e-6/global64/beta1；HelpSteer3与Tulu3 within-dataset同epoch，跨dataset不同steps不能比纯数据因果。MistralTulu BBH32.45<ordinary40.40、均值45.26<45.30；Qwen4BR1许多指标仍低于instruct，不能只汇总conditioning宣传。
- **独立必要反侧**：matchedkeep/refine从同R1起点，pairs/order/reference/新AdamW/seed/exposuremask相同，仅rubric文本差；BBHrefine17.80<keep18.05，MT6.825>keep6.419但仍<R1的6.93，Arena54.5<keep54.6。Feedback与finaleval重叠，故只是对已见benchmarkfeedback适配，不是heldout递归自改善；diagnosticheldout另是measurement稳定性而非此holdout。Tulu第二轮混额外训练+编辑，不能拿R2−R1当edit独效。
- 全teacher/judge/selfdiagnosis五调用、数据评分、rubric/reference全forward、各轮训练、matchedkeepcontrol/选点全部计费，少rubrictoken不等总费小；硬件、主重复训练CI不在必要域披露，不自补显著/速度。Rubric修改只是训练spec提案，发布仍独立行为与安全验收。
- actual `TRAIN-DPO` Ch34 2604.13029完整段只有rubric用于数据eligibility，尚无**固定pairs/label下训练条件可被当前policy按specgap修词，已覆盖但未学会则keep、matchedcontinuation分开额外训练**；此长期分责最小补一段，Ch33/35交接不复述。精确位rDPO完整段后/REDIPO完整段前。

逐字 PRE：

> Rubric 也可以不参与 pair 资格或标签，而只作为训练条件：在固定 pairs、labels 与既定 response-length-normalized 目标下，让两侧回答及 policy/reference 共享同一准则语境，随后撤去语境并验 rubric-free 行为。[RubricOpt 的受限分支](https://arxiv.org/html/2610.29491v1#S3)允许当前 policy 从失败反馈提出最小条款修订，但已明确写出的要求没有学会时应 keep，不能把所有模型错误都归为规范缺词；确定性 gate 只查 canonical anchors、引用与编辑合同，不认证语义或安全。改词后的收益须与同起点、同训练预算和暴露 mask 的 keep continuation 比，而非直接减上一轮成绩；原有限比较有增有退，反馈又与最终题目重叠，不证明持续或未见任务自改善。诊断/判分、reference、全部训练与对照均付费；条款支持、保留能力或独立验收不稳时，保原固定 rubric、经审校 pairs 与普通 DPO，不由 gate 通过或局部一阶分析批准发布。
>
> <!-- source-family:SF-2026-ARXIV-2610-29491 -->

完整上段：

> 评价维度还可以先决定一对回答是否有资格进入训练，而不直接改写DPO梯度：对同一实例保留 essential 与 additional criteria，先检查 chosen 在必要项上达到声明的 full／partial 门槛，rejected 至少一项不合格或多项仅部分满足，再在获准人口内按加权评分差和重复使用上限选择 pairs。有可信 reference 的实例与无答案实例要保留不同的 rubric 来源；多次评分的 median 只降低部分波动，不把派生准则变成独立真值。[视觉rDPO的有限对照](https://arxiv.org/html/2604.13029v1)中，criteria用于外部数据构造，并未逐项进入梯度或执行GRPO；最大margin也不是全部切片最优，部分通用judge和知识指标仍退。多模型分歧种子、rubric聚合、候选rollouts、重复评分、SFT/DPO与reference更新全部计费，三份数据分阶段使用也不自动等于每轮fresh on-policy采样。必要项含糊、来源不可信或held-out行为退化时，保留经审校的普通pairs、原reference policy与独立评价，不让高分差替代标签真实性。<!-- source-family:SF-2026-ARXIV-2604-13029 -->

完整下段：

> 质量检查通过仍可能只剩少数常见回答时，可以在离线pair构造中恢复候选支持，而不改DPO目标：从同一base与instruct分别采样，用instruct改写base回答，再经安全与指令proxy过滤；只在指定reward接近的候选对中，以到其余候选的最近邻embedding距离选择更有边际多样性的一侧。[REDIPO的受限分支](https://arxiv.org/html/2605.30021v1#S2)因此匹配的是同一reward尺度，不是事实、安全或语义等价；改写也可能改变主题。按均值乘比例设阈值不对reward平移不变，均值为负时更不能把它解释为向下容差。Pair来源、过滤器、距离模型、复用上限与checkpoint选择应共同冻结，独立验收多样性、指令与行为切片；所测IFEval和MTBench仍有反退，不授无损恢复。所有base/instruct采样、改写、两两比较、judge、DPO及选点都付费；有效支持不足或质量回归时，保经审校的普通pairs与原reference，而不让自家filter替独立安全验收。<!-- source-family:SF-2026-ARXIV-2605-30021 -->
## G3 2610.29467 PreCoMem — 2+1+2=5；必要Source；拟整合

- [exact-v1](https://arxiv.org/html/2610.29467v1)，实际§2.1–2.4/式1–10、§3.1–3.5/表1–2、§4与直接C.8检索漏失/校准/延迟/新主题、C.9读取与端到端时间；[必要原件](agent4-source-2610.29467-v1.txt)。不遍全appendix/theory/code，不采Bayesian/calibratedposterior解释或生产保证。
- FACT/HYPO支持权重只operational分数，rawepisode来源指针另存，episodecache有固定容量eviction不等无限原件；TopK评分乘beliefconfidence。语义偏差+NLI矛盾得rawproxy，再乘TopK归一分数集中度ρ=1−entropy；ρ只能降低原分数，不测单项事实正确/独立支持，也可能把真实drift压到维持/等待区。LLM只提相关项和有界strength/severity等，但NLI、hypothesis内容与相关性仍是模型判断，不由deterministic更新签真值。
- 双阈maintain加强支持、profile建立低置信猜测并等待反复支持、correct为新观察写FACT(.85)并按矛盾severity软衰旧项。并非所有新事实都须先等；旧FACT不降type、可低权仍物理保留。等待hypothesis的衰减含age每turn复乘，非普通一次exponentialTTL；explicit保护/晋升阈值是当前配置，不作为通用配方。
- 3seedmean±sd、同适用backbone/embed、baseline各推荐配置；judge是gpt4.1mini+两不同prompt的Gemini2.5flash二元均值，不冒三独立真值。LoCoMo1540问题/10对话（问题非独立对话），LongMemEvalS500；分项存在反退，较大answer模型固定下memorybuilder变更只隔离对应对比。DiMo350turn×5persona/1000QA，XL1050×5/2100QA是合成drift/decoy压力，不是真实连续用户生产长期证据。
- 主ESablation把score置0使全路由maintain，不是只移除一项信号后的matched-route唯一因果；CW移除也同时改retrieval/lifecycle。此处不采用“某组件唯一造成全部提升”。
- C8 update-due targetRecall@10约89–95%，未召回则该turn不能correct；强制hit只恢复hit–miss差26–32%，不能把16–22pp关联全当检索因果。高ρ可能集中错记忆；低ρ也会延迟真实更正，AMemGym14.2% warrantedCORRECT延迟，多数后续清除不认证固定上界。Calibration是该AMemGym2829events/3seed、400blind-audit局部支持，不迁移成truth置信。
- N_eff=sum权重稳定不等物理storage/RAM/检索成本constant；默认rawbelief数近线性，LoCoMo287比O-Mem232/Ever264还多，optionalprune168牺牲低权provenance而不是无损普遍storagebound。Table26 E2E是query→answer retrieval+generation，未包含全部write/维护；gpt4omini/Qwenembed1024，硬件/并发/precision具体Not Disclosed，P95不授生产SLO。Embedding/BM25/topic、NLI、各agent、维护/原件存取与三judge全计费。
- actual `AGENT-MEMORY` Ch77 RIKA完整段已有scope/retraction/pending，但未讲**TopK读分布集中度缩放写更新、因此读miss和真实drift延迟耦合**；typedstate与信任/lineage相邻论点保留。仅补此差额，不复制三operator为通用标准，不将同家族多主题分拆owner。精确位RIKA完整段/marker后、批次写入完整段前。

逐字 PRE：

> 可撤销写入还会受本次读路径约束：若只在 Top-K beliefs 上比较新观察，未召回的旧值便无法在该轮被更正。一条[受限 consolidation 分支](https://arxiv.org/html/2610.29467v1#S2.SS4)把语义偏差与矛盾 proxy 乘以检索分数集中度，再选择维持、低置信 hypothesis 等待或软衰矛盾旧项；集中度只缩放更新，不是事实正确率，集中错记忆仍会误导，多个正确候选同分也可能延迟真实 drift。等待与晋升须保来源及撤销路径，新的更正 FACT 也不因类型或高初值自动可信；强制补回漏召项只恢复部分任务差额，不能把全部 hit–miss 差归因于 retrieval。逐项评分、NLI/LLM 提案、维护与原件回读均计费，权重总和稳定不等物理记录或存储成本有界。读漏、阈值或真实变化失配时，扩读原 episode、保留冲突/人工 pending 与静态 curated memory，不让检索熵或确定性公式自行裁决用户事实。
>
> <!-- source-family:SF-2026-ARXIV-2610-29467 -->

完整上段：

> 接纳状态也应允许被后续证据撤销，而不是一次过门便永久可信。[RIKA 的受限设计](https://arxiv.org/html/2610.21739v1)按反馈是否覆盖 claim 的实际 scope 决定即时或延后接纳，再随支持和反对更新状态；已 admitted 的项可退回 pending，派生文本从当前 canonical 集合重建。这里 relation、route 和 evidence count 仍有模型判断，specific→general 的传播也不是形式蕴含或独立样本检验；重复观察不能凭计数获得新权威。Scope、原 episode、来源与重建路径须保留，删除不能代替可撤销隔离。额外判断和维护付费，计数或关系失准、任务漂移时，回到人工 pending、原始来源和静态 curated memory，不让净支持阈值兼任真值保证。
> <!-- source-family:SF-2026-ARXIV-2610-21739 -->

完整下段：

> 批次写入还须区分验收单位：一个课程目标的完成评分，不能自动批准它积累的每条候选事实。[受限游戏 Agent 的负观察](https://arxiv.org/html/2603.17683v1#S6)中，judge 只读取目标、动态 rubric 与已有事实/候选文本，达到门限便把整批 figured-out 项晋升为 facts，供下一课程继承；错误视觉描述因内部一致而得到高分，课程流程完成却未解决任务。这里暴露的是 item-level completion 与 per-fact admission 的错配，而不证明只有感知层需要修复。应把评分实际消费的批次版本与每条证据绑定，课程推进和事实晋升分别受理，缺独立支持的项仍留 pending；这些是写入边界要求，不是原系统已实现的修复。逐项核验、原帧回读与多次模型调用增加费用，未匹配的课程完成次数不等正确学习或部署降本；证据不足时保留原观察和已有写入 Gate，而不让一个高分为整批内容签真值。<!-- source-family:SF-2026-ARXIV-2603-17683 -->
## G2 2610.29139 PAWM — 2+2+2=6；必要Source；拟整合

- [exact-v1 PDF](https://arxiv.org/pdf/2610.29139v1)，HTML404后有限PDF恢复成功；实际必要§3.1–3.3/表1–3、§4.1–4.3、§5.1–5.2/表4–5、Limitations，附录D的WebArena预测接口/E完整环境与F完整训练/表7；[必要原件](agent4-source-2610.29139-v1.txt)。不采用科学任务知识，ScienceWorld仅作为作者规划算法对照环境，不扩AIforScience；未核代码/复现。
- Actor先提tentative action，独立Qwen3.5-27B读当前真实history+该动作，输出pass则提交原提案；有pitfall预测才把guidance给冻结Sonnet4.5重新提action，最终执行后才收真实observation。每轮重建history、压缩旧observation并**移除先前guidance**，不是把预测留成事实；pass仍跑advisor，仅省actor再调用，不是该步零推理。Webprompt只中性后果预告，不生成browseraction/semanticID，actor仍可保原提案。
- Pilot同一轨迹源/相同SFT配方比较nextobservation、subgoalbounded与fullremaining预测：full在WebAcc71.1低于N/A72.7，actionchange最高不等好。posthocpitfall-only gating仍先生成全部guidance+classifier，其较少actorcalls不等全成本低；changed/unchanged词/LLM标签关联非必要因果。主结果SubGoal数与pilot略异，分别保留不拼同一次。
- 同任务三次T1采成功/失败，LLM后见对照定位pitfall；全成功仍标detour，全失败借GTguidance采成功。仅用prompt限制标签依当前可见信息，不保证无未来泄漏/teacherbias。pass下采样调发言prior，0.75Web等配置不作通用阈值。后续GRPO只更新advisor，actor冻结不等无训练或安全约束；公式有KL项但表7系数0，不写实际KLtrustregion。动态丢弃同reward组，Web先三次过滤去全成功train，余375。
- Web812分647train/165verifiedtest；Science708train/271test、30types。T0评测仍三run mean±sd/Pass@3，非完全deterministic；有限迁移只evaluation，不声称各actor都cotrain。Web主PAWM75.0±1.8→GRPO80.4±1.3，N/A72.7±.6；**Web其他baseline未做GRPO**因在线费高，故不独归selectivegate或与同RLbudget严格可比。
- E明示per-task Incus隔离写站、Map沿用；仍timeout/retry，WebRL约Science2×。HTMLparser改为保semanticID的tree、每observation20kchars hardtruncate，且**用LLMjudge替换原Web严格规则终局reward**，不能将其Acc视为未改官方harness或独立客观tasktruth。16B200/5epochSFT+GRPO、三次actorcollection/GTguidance、后见标签/筛选、每步advisor/可选actor重提、环境/重试/judge均计费，calls不等延迟或净总费，不能授生产/物理或安全。
- actual owner `AGENT-PLANNING` Ch79完整2601.08955两段已承载horizon由policy选择及模型误差/费用；紧后Ares段承载actor努力选择，但尚无**frozen blackbox先提案→advisor可沉默→仅必要重提案、逐轮去旧预测**分责。此具体调用接口值得最小补，非新worldmodel理论或Reflection事件后循环。Ch78/80交接已核，执行gate仍属Ch78，不重复训练推导。

逐字 PRE：

> 向前预测还可以只为冻结的黑盒 actor 提供可沉默的建议，而不替它选择动作：actor 先给 tentative action，独立模型检查当前真实 history 与该提案，无需干预时返回 pass，有具体 pitfall 预告才让 actor 再提一次 action；最终候选仍须原执行检查。[PAWM 的受限分支](https://arxiv.org/pdf/2610.29139v1)逐轮重建 history 并去掉旧 guidance，防止预测累积成环境事实；预测到下个有意义 milestone 与是否发言也是两项选择，更多改动作不等更可靠。后见成功/失败对照只产生 advisor 监督，prompt 限制不证明无未来泄漏，pass 比例和 outcome 更新还会改变干预习惯。每步 advisor、标签/训练、必要的 actor 重提案与环境重试均付费，少 actor calls 不等全流程降费；Web 对照未匹配其他 baseline 的 RL，终局又换成 LLM judge，不授独立任务真值或通用安全。预测失准、任务/actor 配对变化或净收益不合时，保原直接 actor、固定短 horizon 与真实 observation 后再规划，不让 pass 或预告自行批准 action。
>
> <!-- source-family:SF-2026-ARXIV-2610-29139 -->

完整上段：

> 这条分支使 planning compute 成为 state-conditioned 控制量，但增加 world-model 数据、policy 训练与误差耦合：错误 transition 可诱导错误的 $K$，更大的、未经该 transition 训练的模型也未必改善规划。步数惩罚与 episode token 归一化预算不等于 wall-clock latency、费用或完整训练成本，比较质量时应分别核这些账；原有文本模拟结果不授予物理行动或 OOD 安全。模型失准、额外调用不值得或缺少可校准状态时，应保留 reactive action、固定短 horizon，以及回到真实 tool/environment observation 后再规划的退路。

完整下段：

> 规划预算也可以在同一 actor 的每个决策步选择 reasoning effort，而不改变 lookahead 或另换 workflow。先固定一条成功的高努力轨迹，再在每个既定 history/observation 下试用有限档位，以复现功能等价 action 的最低档位作局部监督；这个标签只度量指定路径、试验次数和等价判定，既不是任务计算下界，也不认证组合这些局部选择后整条任务仍成功。Router 的 teacher rationale 与 SFT 只是选择器训练，真实 rollout 仍须独立验 trajectory outcome、工具合法性和完整费用。[Ares 的有限对照](https://arxiv.org/html/2603.07915v1)再以 outcome 与成功轨迹的平均档位 penalty 调整选择；档位 penalty 不等累计实际 tokens，失败不受该 cost 惩罚也不授全任务最小总费用。有限重试的零成功不证明任务不可解，筛选人口与 rationale 消融不授全分布保持或唯一内部因果；跨模型与检索任务仍有质量退步。路径采样、三档重试、teacher 标注、router/actor全部调用、训练和工具均计费，token缩短不自动改善墙钟或安全；状态、label或outcome失配时，保留固定已验收努力、原actor与可信tool/task gate，而不让路由预测批准真实effect。<!-- source-family:SF-2026-ARXIV-2603-07915 -->

