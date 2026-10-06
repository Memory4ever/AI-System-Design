# CommonSyn18361：必要 Source / actual owner / 最小 PRE（作者准备）

resume_mar18，只本21补BJT03/20；root已经决定准入的最小§3.2–3.4/T3/T7独校PASS，不代表本Source/PRE已独核。未写Books/未获锁，不计safe/DAY。

## 身份与必要日期

[official exact-v1完整题摘/history](https://arxiv.org/abs/2603.18361v1) 实际当前v2Apr18，不采用窗外修订/不全版本diff，comment仅21pages/7figures，无已见accepted/withdraw/correction/先公开会议信号。实际[DataCite](https://api.datacite.org/dois/10.48550/arxiv.2603.18361) created03/20T02:10:49Z、registered50Z/statefindable；v1Submitted03/18T23:58:37Z、Updated03/20T00:24:12Z、Available2026-03，v2Apr18/UpdatedApr21不采用。官方本批次与同日注册夹证有限支持BJT03/20 arXiv事件，不补精确公告时刻或“其他地方未先发”。保旧窗口/候选。

原质量过滤能保单句可读，却不保证同条件与跨条件的多样性→原文用概念组内候选质量准入+组内关系分数，再跨池联结单句质量与全局关系proxy→重新考虑选择集合的尺度及最终学生Q–D是否与数据proxy一致。拟2+1+2=5，新增curation组件替代接口，不为借用多样性原则、11模型或普遍Pareto加分；待非准备者裁。

## 必要证据和直接反侧

实际读[exact-v1 HTML](https://arxiv.org/html/2603.18361v1) §3.1–3.4/Eqs1–3、§4.1–4.5/Tables1–7、§6–7与A实现配置；决定准入的原有效最小core复用，但后续评价233–279原中间截断已实际244打开补足。未遍B–G案例/完整11模型表/全prompt/代码，不声称复现。

- §3 two-anchor概念组扩1–3bridge；Qwen2.5-72B T1.0、3生成策略各4，≤22words，先keywordcoverage过滤。不是扩展到任意seq2seq或开放故事输入；bridge“不漏test”只为特定概念/三元组检查，不证预训练或全语义泄漏不存在。
- 每概念组Q<4删，再用SimCSE的组内平均1−cos选top8；汇合后对整个候选池用平均1−cos作Dglobal，按Q+Dglobal取83184句。**global分数是在原完整pool计算、不是最终选中集合的重新优化**；max diversity单项也不保证互补关系或覆盖全尾部。|group|=1的Eq1分母/不足8候选处理未披露，不采用精确recipe。
- §3.4 GeminiFlash scorer，与§4.5说Q-basedGPT4o并“如§3.4”、§6明确GPT4o只能独立evaluator不能scorer矛盾；A又写Gemini。因此具体scorer/version、同scorer公平对照未闭合，不授precision recipe/独立无偏质量真值。Q1..10与D1−cos未说明尺度归一，sum权重不证明两个目标等权。
- §4.1 GPT4o在shuffle模型/人类reference的pair做WinTie，Overall=Coverage×WinTie；概念字符串覆盖不证commonsense真，乘两个率不自动等逐item联合成功；SimCSE既筛选又作SelfCos/Vendi评价存在共享proxy。无需因此排除具体Q–D取舍，但不拿其坐标作为一般语义空间/能力真值。
- T1 final20742groups/83184sentences vsCommonGen32651/67389，平均句长14.19 vs10.54；同sample数量对照不等同token/独特概念/总生成和筛选预算。A LoRAr96/α192、Unsloth/A100、generatorT1/scorer/evaluatorT0（A末‘bothcases T0’与前述模型decodeT1未闭合）；epoch/实际训练token/全总GPU时长/硬件precision/batch/concurrency/SLO与独立多seed CI未齐，不能称端到端更省或统一因果。
- T3 dyn质量48.3/D24.6、multi40.4/36.3、pool47.2/31.4、final44.7/34.2，不普遍同时超所有设计；T7Q46.1/30.8、G41.4/35.1、QG43.3/34.2、final44.7/34.2，仅匹配选定对照的受限取舍。T2 Llama vanillaD35.1→final34.2，T4ROCvanilla38.8→38.6，T5CSQA2 51.8→49.0/avg63.8→63.7，不授全面Pareto或所有迁移不退。
- §6 pairwisecandidatepool有扩规模瓶颈（O(n²)朴素式但可否均值分解实现未核），teacher/English/keyword目标限制、不同evaluator未核；§7社会/表征bias留future，不能把模型质量proxy当部署无偏许可。optionalcode未发布不阻塞论文支持的有限接口，但不冒实现核验。

## actual唯一owner与具体差额

actual ROADMAP/PROJECT_CONTEXT/LEARNING_PHILOSOPHY/WRITING_GUIDE已fresh，`TRAIN-DATA` / [Ch27](../../../../../books/part-04-training-system/27-data.md)，actual244–289及258–270重读完整，Ch26/28开篇交接。现252–254过滤bias/保留分布，264–266 PGE joint质量与集合proxy、分块丢跨块关系与全部费用已承载一般Q–D与独立能力验收；但未写**一个条件组内quality admission后local relation筛，再跨组global relation与quality合用**的两尺度候选接口。建议PGE段后/现268数据覆盖×可训练面前只一段，保旧jointmask分支/随机coverage退路，不写新的dataset产品节。是否具体差额足以采用、或现文已足应NC，由非准备者按actual论点裁；不因费时或scorer冲突伪NC。

## 最小逐字 PRE（待独核/窄锁）

正文：若同一输入条件有多种候选，集合多样性还可拆成组内与跨组两种尺度。一条受限分支先对每个概念组的候选做独立质量准入，再按候选与同组其他句子的平均 embedding 距离保留局部变体；汇合后才将单句质量与相对整个候选池的关系分数共同用于全局选择。组内不重复，不保证跨组覆盖；相对原池较远，也不保证最终选中集合真正互补。因此概念组、quality scorer、embedding、局部保留及全局成员须分别绑定，不能由一个联合分数接管语义真值。[有限合成与学生训练对照](https://arxiv.org/html/2603.18361v1#S4)支持比较这两尺度的取舍，但质量优先、diversity优先与混合选择占据不同位置，并非所有模型或迁移任务都同时获益；原文scorer身份与评价口径也不完全一致，不移植其精确配方或宣称普遍Pareto改善。扩候选、质量打分、局部/全局关系计算和学生训练均计费，相同句数不是同token或总预算；仅适合概念到文本的有限证据不授任意合成任务。下游质量、长尾覆盖或净预算退步时，保留可信原语料、单项过滤、随机/分层集合与原joint选择分支，以独立任务切片验收，而不让数据proxy自行认证能力。<!-- source-family:SF-2026-ARXIV-2603-18361 -->

静态注：- `SF-2026-ARXIV-2603-18361`：[CommonSyn exact-v1](https://arxiv.org/html/2603.18361v1)，必要§3/Eqs1–3、§4.1–4.5/Tables1–7、§6–7与A配置；仅组内quality/localrelation→跨组globalrelation选择接口，保scorer身份/共享proxy、Q–D与任务反退、人口/预算及Englishkeyword范围；不采精确recipe、普遍Pareto/泄漏豁免或全费用最优。未核代码/复现/全部附件。

必要机制/评价/关键反证已足够；当前仅prepared，等待root非准备者裁Source/date/actualowner/PRE，不写Books/safe/DAY。

## root 非准备者：必要 Source / owner / PRE 有限通过

决定准入的§3.2–3.4/T3/T7已实际独读校准且命题未变，本次复用；另实际打开精确v1 §4.1–4.5/T3–7、§6–7，确认CSQA2/ROCStories反退、共享SimCSE代理、质量与全局关系尺度、scorer自相矛盾及原池排名限制。official exact-v1身份和DataCite日期定点核验，只保原批次BJT03-20有限归属，不采用窗外v2或推断不存在先前公开。

root actual Ch27 240–280完整质量过滤/PGE joint/后续适配分支与相邻Ch26/28交接核验：一般joint quality/diversity已有，但组内质量准入/局部关系再跨组相对原池排名的两尺度分支是具体差额。原5分、一PRE与静态注有限PASS；“独立质量准入”只指单独步骤，不认证scorer独立无偏。全部收益/预算与scorer冲突近文，未授最优recipe、普遍Pareto或复现。授作者唯一Ch27在PGE完整段后一次窄写及本人注，root实际POST后才计safe，不授整日DAY。

## root 非写入者 actual POST：通过

实际读取Ch27新268及258–280完整邻接，PGE整体集合分支→两尺度局部/原池排名→适配预算顺读成立；本人末注及MM-Zero/MCQ/GASP邻注已实际回读。逐字回对原PRE、必要原证及采用范围：不以原池高距离认证最终集合互补，不以scorer或共同proxy授真值，全费用与局部反退近正文。正文与本人注各唯一，限定diff-check通过；接纳此项实际整合，释放Ch27窄锁，不授本日DAY。
