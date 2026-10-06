# 2026-10-20 独立复核

复核者：root（非报告作者）。窗口为北京时间 2026-10-19 自然日；本记录不验收暂停中的历史补查。

## 1. 首批准入校准

实际打开官方 [cs.CL recent](https://arxiv.org/list/cs.CL/recent) 与 [new](https://arxiv.org/list/cs.CL/new)：后者标题为 Monday, 19 October 2026，226 个事件，104 new、42 cross-list、80 replacements。recent 的 146 个该日条目不能代替 replacements 检查，也不把 226 条变成必须深审的队列。查询与标题范围按主题限定。

实际完整读过两条官方摘要、当前 Comments 和 submission history：

- [2610.23818v1](https://arxiv.org/abs/2610.23818v1)：lossy verification 改变分布后，接受长度提高与最终回复长度增加可能抵消；摘要提出固定 prompts、12 target/drafter 对，联合测完成长度、验证轮次、wall-clock 与任务准确率。可条件准入，因为它挑战把 acceptance length 当端到端速度的判断；数字是作者待核实验，不先作为普遍结论。Submitted Oct16 不替代 Oct19 公开列表。
- [2610.23254v1](https://arxiv.org/abs/2610.23254v1)：低 IPI ASR 可能混入忽略攻击或未完成合法任务，不足以证明有效拒绝。摘要提出十一种 2–14B agents、两个受限 benchmark、label-blind judge 与任务/攻击联合 outcome。可条件准入，需核 judge 分类、分母、系统提示混杂和 utility 边界，不能由低 ASR 推断安全保证；官方页当前未见撤回说明，Submitted Oct16 不作为公开日期。

以上仅准入与日期入口校准，不等于必要 Source、Books 比较或整日验收。主线外应用、仅任务指标与传统语言学材料应具体关闭；不得把有新名称/可映射章节当作贡献。

## 2. 两项必要 Source 与具体 owner 差额

### 2610.23818v1 — Acceptance Is Not Speed

实际读取[精确 HTML](https://arxiv.org/html/2610.23818v1) §2.1–2.3、§3.1–3.7、§4–5与Limitations；不是以摘要代替审阅。评分3+2+2=7：修正接受长度作为完成速度代理的评价判断，限所测解码边界。

§2区分拒绝、residual与bonus三个替换位置。每轮平均提交量为接受draft长度加一个纠正/bonus token；固定每轮费用近似下，完成轮次之比是回复长度比乘以平均每轮提交量的反比。若放宽verification也改变完成长度，固定输出长度的tokens/s不能代替完成同一组prompt的时间。固定完成长度和保持target law的exact路线仍是合理基线。

§3是五种training-free规则、六数据集、十二target/drafter组合的360 cells；主计时在vLLM0.26.0单H100、batch1、T1/top-p1/draft6，非服务并发或SLO测试。精度未作为本笔记采用数字的依据；正文不搬吞吐数字。主pair仅单次case/arm，少量pair补seed；case bootstrap不是训练或所有部署方差。部分方法/后端只改acceptance未改residual，不能把全部结果归给同一完整实现。匹配接受长度也并非所有设置可达。

实验支持“长度、轮次、每轮费用与正确率必须共同检查”，不支持所有有损规则必然更慢：若干cell更短，亦有保存准确率且减少轮次的条件。budget截断、少量题、T1/draft6主设置和单栈限制保留；低target概率token与继续推理有关联，未证明一切长度增长的内部因果。强行结束推理的有限恢复实验不成为通用stop配方。未核代码或复现。

具体比较：`INFER-SPECULATIVE-DECODING` Ch48“Lossless Verification 是分布契约”已有分布变化、质量和tokens/s不能独立证明更快；紧接Nucleus分支前尚缺“完成长度内生变化→轮次核算”的明确关系。全文关键词定点检查未发现length inflation/长度膨胀/回复长度/完成长度现成段，拟补下述机制，非重讲一般goodput。已读Ch47分页边界与Ch49执行计划开篇，不让此处接管cache或编译owner。

拟正文（尚未写入，待非作者必要复核）：

> 分布改变还会改变完成一条回答需要走多远。令严格与放宽验证的平均完成长度为L_s、L_r，每轮平均提交token数为g_s、g_r，忽略尾轮取整时，验证轮次之比近似为R_r/R_s≈(L_r/L_s)(g_s/g_r)。因此每轮多接受一些token，若同时延长推理轨迹，未必减少完成原任务所需的轮次；即使轮次减少，verify shape与已提交长度相关的费用也可能上升。该关系是近似成本记账，不是每个请求的随机比值恒等式。
>
> 评价这种分支应在同一组prompt、停止条件与质量目标下，联合保存实际完成长度、未完成/截断人口、验证轮次和端到端时间，而不是为两种策略强行截成同一输出长度后只报tokens/s。有限实验显示长度膨胀可能抵消接受量收益，也存在更短或准确率保留的设置，不能据此宣布所有有损验证无效。增加重复运行、计时和任务验收有成本；只有要求保持原target law时，继续采用exact verification，允许分布变化的应用则另行验收这份质量—完成时间取舍。

### 2610.23254v1 — Ignored, Not Refused

实际读取[精确 HTML](https://arxiv.org/html/2610.23254v1) §3、§4.1和Table3、Limitations、AppD judge/quote/human协议。评分3+2+2=7，安全评价反证；不为复核扩成全模型安全审计。

攻击者仅控制tool output，不改变system/user/tool/model。十一小模型、两benchmark、三精度共66 cells；失败攻击标签的人口不是所有请求。分类区分真正识别并拒绝、识别却不执行、无识别忽略和机械故障；quote substring验证只能支持可见理由引用，不能证明隐式认知。label-blind judge、150条作者人工校准和与原benchmark的一致率均不构成独立全人口安全真值。量化后较低ASR可能只是工具能力受损。

ATOM在同一次受攻击任务中联合记录攻击成功S与合法任务完成U，区分安全有用/安全失能/不安全有用/完全劫持。NRP以clean utility乘(1−ASR)是不同人口的组合proxy，不能改称联合安全有用概率。system policy的interdict/authorize改变authority framing，并非无信息的同义改写；该policy比较缺对应utility测量。两静态benchmark、greedy、小模型和单judge不支持生产风险、规模趋势或防御保证。未核实现或复现。

具体比较：`PLATFORM-EVALUATION-SYSTEM` Ch66已有风险预算曲线、layered evaluator、拒答/成本曲线及表面伤害迁移，但上述安全段未明确区分低ASR的忽略/机械失败与同次合法任务联合结果。拟在“攻击预算是一条风险曲线”标题前补两段，把“成功是什么”放在“尝试几次”的前提；安全运行时authority仍归Ch72。已读Ch65调度与Ch67监控开篇，测量不越界变成防御。

拟正文（尚未写入，待非作者必要复核）：

> 在讨论攻击预算之前，先确认一次攻击失败究竟意味着什么。低攻击成功率可能来自识别并拒绝不受信任指令，也可能只是没有注意到它、输出无法解析或工具执行失败；后几种情况不能证明模型理解了权限边界。应把攻击是否达成与同次合法任务是否完成联合记录，区分安全且有用、安全但失能、不安全却仍完成用户任务，以及被完全劫持；必要时再用可核trace和独立标签分析拒绝、忽略与机械故障，而不从一句自报理由反推内部安全能力。
>
> clean任务完成率乘以一减攻击成功率，只是跨人口的组合代理，并不等于同一次受攻击执行中安全且有用的概率；二者只有补充可检验的关联假设后才可能联系。工具输出注入的受限实验说明这份区分有实际必要，但模型judge、可见推理引用和有限人工校准仍有误判，量化或更强拒绝prompt也可能以合法任务能力为代价。联合标签、真实副作用检查和人工校准增加成本；低风险回归可保留ASR快速信号，高风险发布须同时验任务效用和威胁模型，不由攻击失败自动签发安全放行。

以上Source由root实际审读。core恢复agent已实际核精确原文与当前书段两侧，PRE通过；root随后将23818两段写入Ch48分布契约节、23254两段写入Ch66攻击预算标题之前，各新增自身末注。23254按PRE明确policy对照未测utility，不将其写成已测代价。core随后实际读完整新增、两侧及本人注，非writer POST两项均通过；这两项整合生效，不等整日报验收。

## 3. 四项 RO 的实际 Books 写后复核

root 是四项必要 Source 作者，不是此次 Books writer；`oct20_author_resume` 已独立核精确 v1 的采用机制、反侧与当前 owner，随后在授权窄范围实际写入。root 本次实际读回 Ch26 104–124 的 ActiveAlign 两段及两侧、978–1001 的 classifier-guidance 两段及两侧，Ch66 1526–1553 的 IMEP 两段及两侧，Ch72 3249–3270 的 TRACO 两段及两侧，并逐项读自身 Review notes。四项真实 POST 通过，已通知 writer 行政同步末注并释放 ownership。

检查重点：AP 终点只是可行子集，不称部署分布相等；classifier 需要目标本体成功数据、保 pose 混杂/锁腕反退；IMEP 净差、任一翻转、事实特异干预和共享执行分母分开，局部撤证不误作整篇撤回；TRACO 明确白盒构造特权、部署 user 指令不改、位置进度不等接触成功，不从攻击结果推出防御有效。八段均保机制附近费用、替代路径与失败边界，未改 root 原有 23254 段或用户 staged 内容。只验这些实际写入，不授整日报完成。

## 4. Core 首批必要原证的局部独核

root 实际独核 22454 精确 v1 的位置/表单与内容分账、sink 控制、§5–6 预算/计时及 §8 反侧；23048 §3.4 的 writer 估计边界/无边界回退/整条 GRPO、§4.3 同初始化/系数/归一化与随机边界/后缀对照；23051 Th4.1 有限编码/有限 H/Lipschitz 前提、Prop5.1 累计 action-value argmax 包含条件及 tie；23213 §3 的 early/final gate、candidate-blind panel、§4.1 配置/总 input-output token 与异构替换混杂。有限命题通过，不采用主表数字为普遍收益。

已授 core writer Ch21/31/33/82 最小正文差额的独立 ownership；当前只完成 Source 和写入授权，实际 POST 仍须保存后逐项检查。22507/22511/22820 及其具体 NC 尚未由 root 完整结束独核，不借这四项通过覆盖其余工作。全日仍有普通可执行待办。

更新：四处已实际保存。root 本次完整读回 Ch21 250–268、Ch31 1252–1278、Ch33 1280–1310、Ch82 62–78 的新增及直接两侧，并逐项读本人末注。四项真实非 writer POST 通过：22454 分开 form/content 与短输入反退；23051 保累计 action-value、argmax 包含与错误 tie；23048 后缀只屏蔽外部指导、仍有 GRPO outcome，writer 非真值；23213 保 agreement 漏检、candidate-blind 非误差独立、异构能力混杂和完整 token 成本。正文不冒称已复现、通用增益或运行安全，旧有效段与来源绑定未被覆盖。可同步末注并释放这些新增位，不授整份日报完成。

## 5. MM 十一项的必要原证与具体 Books 判断

root 实际独立读精确 v1 的采用域：23279 Lens 的共享 pre-merger features、mask/文本双路监督和 bbox 依赖；22957 QART 的 query-support 重建、slot 增长/停止与 batch1 反侧；23324 CatchUp 的深度陈旧状态、邻 token transition 估计及恢复误差；23854 MFlow §3–5 的 soft-PCA gain、velocity loss 与 t=0噪声/t=1数据的解析逆端点；23263 SCALE §3–5、Tables5–7 的 real/self contrast、PatchMix、单次 stop-gradient 与理想支持条件；22975 Sink-Sparse §3–5 的离线静态 mask、完整支持 pooled KV/logsumexp 支路和近二次费用；22499 JAVIS §3–5 的共享 speech hidden、双 decoder、lookahead chunk 和同步/语音质量反侧；23795 PPMem §3–5/Tables3–5 的变长 plane pool、写替换/遮挡质量与几何反馈；23542 MIST §3–8 的 execution-before-memory 配对与 oracle 选择边界；23423 Momentum §3–4/Tables2–4/B 的 world rollout/observer 解耦、每 rig 八相机而非八 rig、inactive 复制和生成/真值 reference 分账。并未核代码、复现或全部附录。

十项按实际 owner 在 Ch23/24/25 写入，writer 为 root；oct20_systems_resume 已实际读完整新增、直接两侧与本人注，通过非 writer POST，记录在 SYSTEMS_READER_POST_CORE.md A/C。MFlow 与前文 MeanFlow 的时钟相反，独立读者指出后已最小补明，并实际读回通过。不得从本条推整日报完成。

23531 PONDER：root 实际读 §3.1–3.5、重 mask 的匹配对照与固定 R 预算。冻结 generator，位置 policy 可重遮已填位置；N+2R 决策和固定 R 不等自适应停止；group-relative 更新无 PPO clipping，FIDgrad 是人口 Gaussian plug-in 的局部影响代理，不是单图真值。2+1+2=5，No Change — Existing Coverage：Ch24 当前 L822 的完整正文已具体解释 frozen predictor、下一可见集合、重 mask、固定 horizon 非提前 commit、全部费用及旧 sampler 回退。FID population reward 的本篇实现仅保报告，不冒称已有公式完全覆盖。

## 6. 首批 systems 与新增 Core 的真实写后复核

root 实际读首11 systems 每处完整新增、直接两侧及自身末注：Ch36 BaGuaLu2/MailRail/异构 communicator，Ch48 BS-Spec，Ch49 DIFFLET/TileDRAM，Ch54 KV Residency/MemLLM/HBFSim，Ch56 Dataflow，Ch63 PairSight。逐项保 credit/状态/执行 ownership、模拟与真实硬件分账、局部反侧和全部费用，非 writer POST 全通过，已通知 oct20_author_resume 同步，必要独立 Source 另在 SYSTEMS_REVIEW.md。ScaleRAN Ch63 的分位人口/条件 deadline、合作边界、wide-MLP 反侧和 fallback 新段亦实际完整读回通过。

Core 22507 RealCLI 的 §2–4.3/B2–3 已实际读：同目标不同信息预算，不把 J 组合代理当联合事件；Ch66 当前过程评价与 human-team 正文已承载，具体 NC。22820 CES §3.1–3.7/4.5/6 已实际读：程序追加/cache 非 compaction，teacher-forced 修正不证明自主纠错；Ch18 当前程序状态与错误执行正文已承载，具体 NC。22511 AuditKIT §7.1–7.3/8.5–8.7/9 已实际读：call-set 不等 turn/dependency、any_of 非成功 oracle、不可观察不等 no-call；Ch66 最小新段实际保存后，root 完整读新增/直接两侧及本人注，真实非 writer POST 通过。

Core 22380 TrustMix、22438 rank、22467 self-distillation 的新增与两侧/本人注已实际读回：outer trust domain 非重采样，W/Δ 与谱定义非混用，teacher refresh 非继承初始安全，三项 POST 通过。22512 PI、22539 WebMix、22543 SPOT 亦实际完整读回通过：即时 PI utility 不等撤去 PI 后学习；source bank/router 训练不等 target 全免示范；stale token 与顺序 proposal 分开、完整 state 副本/位置索引 noise 条件不由同 seed 代替，approx cache 不继承 lossless。独立必要 Source 由 SYSTEMS_READER_POST_CORE.md B1–B7 承载；只验已保存的这些差额，不授 DAY。

## 7. Systems 末批六项的必要独立 Source

root 实际读精确 v1 必要原文，不以摘要或作者笔记替代：23662 §III–IV、VI及PushT反侧，h同时消耗求解和物理执行时间，reblocking恒等不证明最优，均匀误差/Lipschitz假设不当在线安全盾；23271 方法/生成与推理、同mask容量对照及limitations，任务ID产生delta后普通执行不等runtime MoE，存储非active memory、公式系数未决不采用；23127 dynamic/successor训练、短MPC、ablation及A4，D与条件期望S分责，精确组合只在充分确定latent/冻结精确模型等条件，不交换一般期望；23002 mask/inpainting/CE定义、部分控制主表与real limits，兼容mask合并非冲突解算，command贴合非physical保证，any-time最小CE非特定时刻；22496 architecture/skill memory/guard、rehearsal与冻结评测、air-fryer反侧，编译技能与backend权限分开，Unsure/接管计入评测、不采用零示范或全无人成功；23769 graph/Dijkstra/offline与RL、ablation/threshold，距离可随回退变差，视觉近邻非可达证明，阈值及离线建图费用均保留。

这六项的有限命题通过，评分及具体owner沿ARXIV_SYSTEMS §9。oct20_systems_resume为Books writer，已获Ch25/26的各至多两段窄写授权，须先比较现有正文。保存后由root实际完整新增/直接两侧/本人注POST，当前不预支写后或日级通过。

## 8. RO末批、Systems前三及两项有限漏收恢复

root 已实际读RO7六项新增/直接两侧及本人注：Ch25 ORD/HIJP，Ch26 MambaAct/LAW/VLAFabric/RePlanMem，真实非writer POST全部通过。边界包括语义/视觉记忆与事实owner分责、Mamba刷新而非任意上下文无损、动作rate/坐标与物理反馈、memory查询/更新成本及RePlan带历史与重规划混杂。22471 Astra具体NC已实际读Ch66身份/reset、固定预算和wall-clock人口正文，不以主题类似作NC。

23056 ThoughtBlocks的Ch82两段及直接两侧/本人注、22899 ProvableAuthority的Ch78两段及直接两侧/本人注亦已root实际完整读回，非writer POST通过；前者保R/C依赖、causal render、质量反退、payload解析估算及完整成本，后者保当前status/digest/原子额度预留、未知commit对账及无形式/攻击证明。22882具体NC实际读Ch82 population个体/福利、mutation/selection及selfplay≠bestresponse/candidate与horizon边界，新增受限博弈实验保报告，不另增重复正文。

有限抽检确认漏收22631 JUPE、23071 BeforeRetrieval后仅补这两项，不重开无关发现。22631的必要Source由非作者systems独立读E1；root实际核Ch66 judge competence/leniency和AnswerOnly×truth四格/justification对照已具体承载，7分、已有覆盖，不降分或假写新机制。23071由systems作Source作者E2，root独立打开精确HTML §3–4、标签/阈值/selection与单seedrecipe/失败限制：call admission、call后harm与no-call harm不同，plaintext-refusal迁移有限且不证明不耦合；缺matched benign-only/direct-call/joint控制，不用少harmcall代安全放行。6分安全深入通过；author获Ch78至多一段差额比较/写位，待保存后root实际POST。全日仍进行中。

## 9. 最后七项真实写后通过；等待完整报告复核

23071由author实际写Ch78一段后，root完整读回84–112的直接邻接及本人末注，非writer POST通过：工具准入与响应两层测量、有限SFT迁移和未隔离因果、benign/no-call人口、副作用范围及服务器authority均留在正文，未把拒绝训练说成完全不能迁移，也未签发通用安全。

Systems六处已保存，root实际完整读Ch25 195–220及本人注，Ch26 662–690、1004–1032、1250–1276、1400–1429、1438–1467及六项本人注，非writer POST全部通过。D/S分责和条件、mask command与物理闭环、已知task-ID参数生成与重建误差、solver/commitment共同时间和静态h反侧、图进度的alias/非单调性、RAX冻结测试/真实碰撞与四次clean分母均在相应正文近旁，直接前后论证可衔接；未静默删除旧机制或替代独立controller。六项各两段，没有把整份论文摘要追加章末。

全部本日已授权新书位可释放，writer仅行政同步既成POST。当前逐项必要Source与Books差额无待办；Report仍须合并有限64家族并由非Report作者实际检查完整六节，不能用本条替代日级验收。历史cursor维持用户暂停，不换日、不扩发现、不stage/commit/push。

最终定点QA：root实际核报告64行＝54整合/10已有覆盖，54项新增均在18个唯一Books正文owner中有唯一family marker；本地引用无缺失、节点可解析、18本日改动Books加报告的围栏闭合。此为结构/落点检查，不替代已分批完成的语义核验。23056数字句另由root实际核精确原文§4.1–4.2/Table2及B.4后，writer仅补模型/任务/平均口径与未披露推理精度，root实际读回Ch82 427–435通过，未将Beacon训练BF16冒充推理精度，不重做已有效Source或POST。

本日V3与unstaged diff-check通过；全cached仍有运行前2025Sep原始HTTP头CRLF/EOF及2026May JSON EOF空白，不改index。窗口回归实跑41/42通过，旧标题纠正测试与现同精确URL规则的冲突保留，本日未改脚本/合同，不宣称全回归通过。完整报告非作者验收仍由systems读者执行。

## 10. 完成态实际读回

systems非Report作者已实际读完整六节及64个证据段并在SYSTEMS_READER_POST_CORE §G通过日级语义验收，root完整消费该回执。core据此行政保存完成态，检查时间2026-10-20T11:44:19+08:00。root随后实际读回header/§1/§5/§6：状态完成、Books纳入、64＝54整合/10已有覆盖，五外部子范围仍隔离、历史仍暂停，没有普通待办。root保存后重跑本日V3及unstaged diff-check通过，未改validator/合同或既有index。验收仅指本日合同范围，不授无遗漏、外部缺段覆盖通过、全部回归通过或历史任务完成；不stage、commit、push。
