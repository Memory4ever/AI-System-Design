# Daily Research — 2026-02-01

**规范：** V3
**窗口：** 2026-01-31T09:00:00+08:00 ～ 2026-02-01T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-10-08T12:17:26+08:00
**窗口说明：** 用户授权只补遗漏；原窗口、已有候选、评分、有效证据及原§4连续正文保持，原稿见[补查前基线](../_sources/daily-20260201/baseline-before-supplement-20261008.md)。
**补充窗口：** 2026-01-31 ～ 2026-01-31

## 1. 结论

原轮从原始来源独立重建，未以旧 Daily / Weekly 的材料、评分或章节摘要反推准入。14 个每日来源均已执行有界检查；没有扫描每周来源，没有把分类或全年目录转成逐篇队列。原始记录集中在[原轮来源记录](../_sources/daily-20260201/SOURCE_RECORD.md)，[旧日报备份](../_sources/daily-20260201/LEGACY_README.md)仅供保留历史。月度来源目录中既有的旧 screening / inventory / BOOKS_WRITEBACK_QUEUE 等文件身份保留，未打开或用于原轮；原轮证据文件名单由来源记录首段限定。本次增量补查不把旧池重新变为全文队列。

原轮 OpenAI 官方 RSS 在原窗末小时有 8 个安全案例页面日期命中，归为一个 February 2026 abuse-report 家族；全部案例核心筛选后关闭：它们是既有欺诈/影响操作流程的观测与归因限制，未识别到改变具体模型、平台或评价合同的新机制或反证。它们不是 8 个正式候选，RSS时间也不被偷换为已核实首公开时间。本轮只以日期判断补充Jan31，不重审已有效关闭的案例或搬动原归属。

原轮正式当窗候选 **0 个家族**；候选证据审阅 **0**，Books 实际写入 **0**（No Change）。原轮另有 A²D 的相交日期线索，以及 Kimi-K2.5 当前技术博客事件日期不明，保留于缺口、不评分不采用；原轮非作者日级复核通过。Google Research、Meta、Qwen、MiMo Blog 等历史切片限制不能支撑“无遗漏”。

本轮补充 Jan31 自然日，14 个每日来源按清单顺序有限补查或复用未变化的有效切片，未扫描每周来源。原0＋确定新增 **1 个家族（A²D）＝1**；新4个主题线索完整题摘分为2贡献前关闭/2必要日期保留，不作为全文队列。A²D官方Seed公开日期字段为Jan31，旧时分秒交叠障碍解除；实际必要证据已读至机制、关键对照、反侧和附录算法，未复现实验。具体差额是训练独立分解策略、条件带提示探索，再以无子问题条件学习筛出的正例；它改变脚手架来源与更新责任，不证明免费自进化。root必要Source/owner PRE通过，Ch33实际写入两段及源注，root非作者POST与本轮六部分DAY通过；普通待办 **0**。精确IDL公式、完整成本与潜在线索日期继续隔离，完成不授全历史覆盖、无遗漏或通用能力保证。

## 2. 来源覆盖

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | [官方RSS](https://openai.com/news/rss.xml)只恢复Jan28～Feb3邻接日期段；8个Feb1 00:00GMT案例核心全读，前侧Jan29 data-agent、后侧Feb2 Codex app；[记录](../_sources/daily-20260201/finite_lists_final.json) | 已检查 | 页面只标February1且指向February报告，不证明首公开；因贡献已关闭，不追加无关日期追查 |
| SRC-ANTHROPIC | [Research](https://www.anthropic.com/research)官方publishedOn；Jan29 19:13:26.601Z coding-skills至Feb5 zero-days，无本窗条目；174元数据仅日期定位 | 已检查 | 当前目录不是历史快照；不声称全机构无其他渠道公开 |
| SRC-GOOGLE-AI | [DeepMind page4](https://deepmind.google/blog/page/4/)相关Jan22/Jan29/Feb11片段及Project Genie原文Jan29；[Google Research](https://research.google/pubs/)当前按年入口及限定日期主题补检 | 受阻 | Research动态历史窗口未恢复；搜索无命中不证明覆盖 |
| SRC-META-AI | [Research](https://ai.meta.com/research/)动态空响应；[results第3页](https://ai.meta.com/results/?content_types%5B0%5D=publication&page=3&sort_by=relevance)有限发布日期片段 | 受阻 | 按relevance排序，不能当完整时间序列排除Jan31事件 |
| SRC-QWEN | [旧入口](https://qwenlm.github.io/)跳转；[新Blog](https://qwen.ai/blog)及qwen3-max-thinking定点页面只得动态壳 | 受阻 | 未恢复本窗官方发布目录/原始日期；搜索摘要不是日期证明 |
| SRC-DEEPSEEK | [官方news](https://www.deepseek.com/news/)可见研究10项，Jan28 OCR2至Feb25 DualPath跨窗；停止该相邻日期段 | 已检查 | 不推广为所有仓库/页面历史完整性 |
| SRC-MOONSHOT | [Platform Blog](https://platform.kimi.com/blog)当前26项均2025；官方组织首页→K2.5原文；[模型卡](https://huggingface.co/moonshotai/Kimi-K2.5)Jan29模板changelog | 受阻 | 当前PARL技术博客无首公开/重要修订日期，不确认为本窗事件 |
| SRC-TENCENT-HUNYUAN | [Research](https://hunyuan.tencent.com/research)浏览器超时后，从官方前端公开API恢复“全部”：page1,size1000,renderType0，total9/返回9，最早publicAt Feb3 18:02:07+08；组织与T1主页有界补检；[原始字段](../_sources/daily-20260201/hunyuan_metadata.json) | 已检查 | 当前最早Feb3不证明1月历史从未存在；保留历史目录限制 |
| SRC-ZAI | [官方Research](https://www.zhipuai.cn/zh/research)Jan19 Flash至Feb2 GLM-OCR、Feb11/21片段；发布说明当前页补检 | 已检查 | 发布说明未恢复1月历史切片，不能给全渠道零发布保证 |
| SRC-BYTEDANCE-SEED | [论文升序API](https://seed.bytedance.com/api/get_article_list_v2?article_type=1&publish_year=2026&count=100&order_desc=false)page1实际20项，Jan29→Jan31 A²D→Feb2 SPARKLING已实际读，过窗停止；本次[API原件](../_sources/daily-20260201/supplement-seed-api-20261008.json)仍20/total82,next20,has_moretrue；Blog原类型2返回9、最早Feb12有效复用 | 已检查 | 本轮只按官方显示Jan31日期准入A²D；Submitted与UpdateTime均不替公开。Blog返回9/total23与next20之后未读，不作全量覆盖证明 |
| SRC-BAIDU-ERNIE | [官方Blog](https://ernie.baidu.com/blog/zh/)第1页Jan29 PaddleOCR-VL1.5→Feb6 ERNIE5；已跨窗，止于第1页 | 已检查 | 不声称第2页所有历史内容完成题摘 |
| SRC-XIAOMI-MIMO | [官网](https://mimo.xiaomi.com/)Paper Jan8→Feb3 HySparse；当前Blog15卡 | 受阻 | Blog没有可用历史发布日期，Paper日期不替Blog背书 |
| SRC-MINIMAX | [英文Blog](https://www.minimax.io/blog)Jan27→Feb12/14；[中文](https://www.minimax.cn/blog)Jan28→Feb12；[Agent完整当前列表](https://agent.minimax.io/docs/techblog.md)只有May13 | 已检查 | 中英显示日期不强行统一；当前Agent列表不能证明历史无其他资料 |
| SRC-ARXIV | [官方公告规则](https://info.arxiv.org/help/availability.html)本窗为周五20EST至周六20EST，无常规公告；4组有界主线主题补检+六分类二月首25标题页尝试 | 已检查 | 多分类cache-miss；不拿提交时间、当前recent或搜索无结果证明首公开/全学科召回 |

实际主题、查询式、分页/停止点及原始记录见[来源记录](../_sources/daily-20260201/SOURCE_RECORD.md)。arXiv 的 Sunday–Thursday 20:00 Eastern 公告包括新稿、替换、撤回与cross-list，冬季相应北京时间次日09:00；下个常规公告Feb2 09:00落在本窗之外。这只限定arXiv公告，不排除官网先行公开。

补查停止：OpenAI实际RSS Jan29→Feb1邻接没有Jan31显示项；Anthropic原Jan29UTC→Feb5元数据有效复用，不由当前首屏补授覆盖；DeepMind page4、DeepSeek Jan28→Feb25、Z.ai Jan19→Feb2、ERNIE第1页Jan29→Feb6及MiniMax中文Jan28→Feb12均在相邻日期过窗停止。Moonshot的26项Platform列表均2025；Hunyuan官方Research失败后按原有效恢复路径重新取得API total9/return9日期字段，最早publicAt仍Feb3，不证明历史从未有1月项。Meta/Qwen动态空页、Google Research按年入口、MiMo无日期Blog在一次Jan31限定官方域名补检后保留历史缺段，不把空搜索当作零发布。MiniMax当前Agent列表访问失败不抹去原有效May13记录。

arXiv只做Jan31四组主题（模型架构/训练/上下文；多模态/生成/World Model/VLA；GPU/编译/通信/缓存；Agent/RAG/记忆/评价）补检，返回4个相关或含糊条目完整题摘；二月首25 CL/DC/RO标题页各一次失败，停止恢复，不转分类全队列。官方规则仅证明本日无常规公告，Submitted Jan31不授Jan31公开。查询结果Hope Speech/NetWorld贡献前关闭，HyperOffload/GRASP必要日期保留；NetWorld关闭因已有diffusion/MF等组合在无线三任务仅报领域指标，未指明改变主线设计的独立机制或受控失效边界，而非因cs.NI标签。新原件、实际顺序和限制见[本轮补查](../_sources/daily-20260201/supplement-20261008.md#1-有限来源与停止)，覆盖仅限所列切片，不宣称全机构/全学科无遗漏。

## 3. 候选与判断

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [Adaptive Ability Decomposing for Unlocking Large Reasoning Model Effective Reinforcement Learning（A²D）](https://arxiv.org/html/2602.00759v1) | 2026-01-31 | outcome-only探索低信息→proxy评价训练分解策略、低无提示成功率时带提示探索并无子问题条件内化正例→重考虑脚手架来源与训练责任；2+1+2=5 | 深入完成 | 整合：TRAIN-GRPO [Ch33](../../../../books/part-04-training-system/33-grpo.md) Group Size中PrefixRL后两段，root Source/PRE通过、实际写入；root非作者POST通过 |

原轮候选表无行，保持原0候选；A²D只按补充Jan31自然日新增，不搬动原日期归属。K2.5以及新HyperOffload/GRASP的日期/事件身份保留项不放入本表。没有以摘要阅读充当标准/深入审阅，也没有给尚未确认落窗的材料评分。

## 4. 证据与知识整合

没有正式候选需要采用。8个OpenAI案例全部核心筛选和逐例理由见[安全案例记录](../_sources/daily-20260201/SOURCE_RECORD.md#8个安全案例全部核心筛选1个家族0个正式候选)。关闭并非要求安全案例必须有controlled benchmark，而是没有识别到具体系统合同的新失效/反证增量：Cyber Special Operations的拒绝与操作者后续行动描述不证明跨provider因果；Date Bait的人类/API协作不证明新增agent控制机制；Romance案例明确限制碎片证据可比性。若后来有新的控制边界证据，仅重开相应案例。

Books判断为 **No Change**：没有已核实当窗且通过贡献筛选、证据审阅的新增论点，未改写任何Books文件；并非声称所有保留机制已被书稿覆盖。本轮不需要申请共享Books ownership，也未新增结构收纳章节。

### [Adaptive Ability Decomposing for Unlocking Large Reasoning Model Effective Reinforcement Learning（A²D）](https://arxiv.org/html/2602.00759v1)

以上连续正文是原轮结果，完整保留；不作为本轮补查完成声明。本轮根据官方Seed API PublishDate确认Jan31显示日期，UpdateTime及arXiv Submitted不作公开日期来源。root已独立校准完整题摘、官方字段与§2.2–2.3的潜在贡献，原稿的“整天字段与9点窗口仅相交”障碍不再适用于自然日。

实际读§2.2–2.3、§3.1/Table1、§3.3/Table2–3及提示依赖反侧、App7格式与App8/Alg1。decomposer的quality reward是proxy多次尝试至少一正确，乘format reward后训练；reasoner先无hint采样，低成功率才增加带子问题探索，正例限额选取后在不包含子问题的question+diversity-prompt条件下辅助学习。代理结果不证明每个子问题正确，无hint部署能力需单独评测，不把该流程称纯on-policy或无外部信息的免费能力增长。

作者四个3–8B模型/八数学任务、prompt2048/response6144、batch128/minibatch32、32rollouts、temperature/top_p均1，报告8次评价均值而非8训练seed。GRPO64rollout对照未匹配decomposer/proxy/离线注释/额外guided全部预算，完整hardware、precision、wall-clock与evaluator实现为Not Disclosed；concurrency/SLO不属于本文评价目标。Table2提示移除/选择/多样prompt反侧支持有限协议的责任分离；Table1 Qwen7B OMATH-H 2.9→1.8、Table3 REINFORCE++ MATH500 73.6→72.7不支持每任务普胜。

Eq3/5名为NLL却写π而无log，附录算法只引用原式，未给独立修复；无正例分母/空集处置亦未明确。该精确目标/实现隔离，不照抄或自行纠正文献；只采用文字明确的条件探索/筛选/去提示学习接口，方法和直接反侧足够即STOP。Ch33已有POPE/PrefixRL人工/外部prefix conditioning及suffix奖励更新、scaffold退火；新差额是固定proxy训练decomposer与guided-positive/no-subquestion辅助更新分责。root实际核[owner PRE](../_sources/daily-20260201/supplement-owner-pre-20261008.md)后授窄锁，已将两段融入Ch33 Group Size的PrefixRL后、selector前，附近保留完整预算、局部负向、无hint测试和原式不采用的边界；作者已顺读正文/完整邻接与自身源注，root非作者实际独读两段/405–433完整邻接与自身末注后POST通过、窄锁释放，不自授日级完成。

## 5. 缺口与下一步

本窗已隔离的外部 **终态保留项**：

1. [A²D / arXiv:2602.00759v1](https://arxiv.org/html/2602.00759v1)：原日期交叠限制已按本轮Jan31自然日解除，不再索取时分秒；精确IDL目标仍因Eq3/5与NLL命名不一致、无正例处置不明而隔离。只恢复作者勘误或精确公开实现的对应目标，不影响已可支持的文字接口判断，不采用免费/等总成本保证。
2. [Kimi-K2.5当前技术博客](https://www.kimi.ai/blog/kimi-k2-5)：PARL/critical-steps相关内容有潜在机制，但当前页无首公开或重要修订日期；Jan29官方模板changelog是窗前事件，不等于该博客内容发布日期。需要带日期的原始公开/修订记录；不以图片路径日期、Git作者提交或媒体发布日期补时刻。当前不评分、不Books，恢复只查此事件。
3. 历史来源切片：Google Research、Meta relevance结果、Qwen动态Blog、MiMo无日期Blog；Hunyuan当前最早Feb3、Z.ai当前release-note和MiniMax当前Agent列表也不能重建Jan31所有历史渠道。当前可用官方入口/有界补检实际范围已保存，恢复条件是相应来源本窗日期目录/原始公告或可靠快照；只定点恢复受影响入口与窗口，不把缺失当零命中。上述限制不支撑“无遗漏”或正面Coverage通过。

4. 新线索 [HyperOffload / 2602.00748](https://arxiv.org/abs/2602.00748)、[GRASP / 2602.00475](https://www.michaelpsenka.io/grasp/)：完整题摘及有限原入口日期恢复已做；现有Submitted/索引日期、无日期项目页不足证明Jan31官网先行公开。两项分别有图级remote-memory调度与lifted-state规划的潜在机制，均不评分、不进入正式候选/Books。需要带公开日期的官方公告或可靠历史原稿快照，不需时分秒；只定点重开这些事件，晚期PMLR不改变首公开归属。NetWorld已依据具体贡献理由关闭，不追加不影响处置的日期请求。

本轮普通待办 **0**；有界发现/必要证据已STOP，root非作者Source/PRE、实际POST及六部分DAY通过。以上隔离项不支持正面证据、Books采用或无遗漏断言；必要日期或历史切片以后取得时，仅按所列位置定点重开。窗外Project Genie Jan29、HySparse Feb3仅作停止边界，不扩张本次窗口，不顺带重跑其他日期。本日结束，不续跑下一日期。

## 6. 复核

复核者：root（非报告作者 feb01_v3）。

结论：通过

root核对14行来源的实际查询、停止位置与限制，定点读取RSS/Anthropic日期提取、Hunyuan原始字段、Seed接口片段及动态页恢复记录；没有将当前目录当历史全量。准入校准实际读取全部8个OpenAI安全案例的Actor / Behavior / Impact，收窄Cyber / Date Bait关闭理由，避免把所有安全案例泛化排除；候选0，因而没有待复核的正面采用。另独立重新打开arXiv公告规则、A²D完整题摘与版本页及K2.5技术博客，确认两个潜在线索不能仅凭Submitted、整天字段或无日期正文授予落窗。没有逐条重复检查所有窗外目录项、所有附件或整个机构历史。报告、来源记录与实际没有Books改动一致；No Change不是“全部潜在知识已有覆盖”。§5外部限制隔离及重开条件完整，普通待办0。

机器校验：`python3 scripts/validate_research.py --report papers/2026/02/01/README.md` 通过；本日报未暂存范围的 `git diff --check` 通过。机器校验不能替代上述语义验收，既有暂存区不在本日修改范围。

本轮补查作者：supplement_20260201。

复核者：root（非报告作者、非Ch33写入者）。

结论：通过。

root实际逐项读取本轮六部分增量、14源有限主题/查询/停止和历史限制，实核Seed ID1523的PublishDate与UpdateTime分离及Jan29→Jan31→Feb2相关跨窗段。全部新增1项A²D的完整题摘与精确v1必要方法、关键评价、局部负向、Eq3/5/App8实际核查，Source/owner PRE通过；另实际完整读取HyperOffload/GRASP潜在贡献题摘与日期保留依据，及NetWorld/Hope Speech两关闭项题摘、具体贡献理由，没有用学科标签自动关闭。Ch33新两段与405–433完整邻接、章末自身源注实际独读后POST通过，原POPE/PrefixRL和下一selector的衔接保留。本轮六部分DAY通过，普通待办0；未检查全部机构历史、全部原始目录条目或无关附件，不把有界覆盖/隔离项签作无遗漏。

完成态机器检查：本日V3、13新JSON合法、11本地引用0缺失、原0候选与原§4连续字节/原窗口保留，以及本日与Ch33限定cached/unstaged diff-check通过；校验不代替上述语义验收。原轮复核仅按未变层级复用，本轮独立记录另列如上。未改公共合同/索引/state，未stage/commit/push，本日结束。
