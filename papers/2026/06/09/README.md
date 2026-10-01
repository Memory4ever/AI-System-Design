# Daily Research — 2026-06-09

**规范：** V3
**窗口：** 2026-06-08T09:00:00+08:00 ～ 2026-06-09T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-10-01T07:16:42+08:00

## 1. 结论

本轮恢复一项可靠落窗的机构研究：n-days。它把已公开漏洞上的 crash PoC、原生攻击效果和完整权限链分开评价，提示补丁公开到运行实例实际修复之间的时间压力。必要机制、关键对照与反证已深入审阅；[PLATFORM-SECURITY / Ch72](../../../../books/part-06-ai-infrastructure/72-security.md#生命周期威胁)已实际补入两个连贯段落，并经非作者来源到实际 owner、写后及邻接复核通过。不把最快受控试验写成典型生产攻击时延或全链攻击概率。

确定落窗的候选为1个唯一家族，深入完成1项、实际整合1项；非作者日级验收通过，普通待办为0。另有4项读核心后贡献前关闭（OpenAI三项及暂缓的biology研究），不因厂商名或应用热度准入。来源检查实际执行于2026-10-01，研究窗口没有移动。

旧报告的112个 arXiv 工作家族缺少首次公开上界，全部具名保留为日期缺口，不列作确定当窗候选，不计112项审阅/Books通过。旧1,235个宽发现身份不是本轮强制全文队列；旧题摘、必要证据、11处真实书稿及2处中央争议均保留在[本日唯一恢复材料](../_sources/daily-20260609/V3_RECOVERY_BLOCKERS.md#2026-10-01-当前日期隔离与有限恢复结果)。日期问题不自动推倒其他有效机制，但它们不能据旧时间推定算成本日报采用。原报告全文已在同一材料中保存，未经本轮验收的旧评分和完成标签不再作为现状。

## 2. 来源覆盖

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | [官方RSS](https://openai.com/news/rss.xml)实际1,240 items；按本窗精确pubDate取3项，逐项核心说明见§4。前邻06/08 00Z、后邻06/09 10Z停止，不读窗外正文 | 已检查 | 当前RSS保留不能证明已删除事件无遗漏 |
| SRC-ANTHROPIC | [Research](https://www.anthropic.com/research)原HTML hydration实际173 publication；本窗publishedOn两项n-days/agents-in-biology，精确13:00Z/13:20Z；只审前者必要证据、后者核心范围 | 已检查 | 当前目录保留局限；公开厂商实验不证明生产风险 |
| SRC-GOOGLE-AI | [DeepMind page2](https://deepmind.google/blog/page/2/)实际列表June→May，月份展示无法唯一归到目标日；[Research pubs](https://research.google/pubs/)实际年度目录无本日公开时间。有限日期恢复停止于此，不展开全月正文 | 受阻 | 需目标日带时区目录/原始事件；月份和年度列表不证本窗零命中 |
| SRC-META-AI | [官方publication page1](https://ai.meta.com/results/?content_types%5B0%5D=publication&page=1)目标相邻降序片段06/29→06/05→05/27，无06/08/09条目，停止在窗前；不遍历后段旧年份乱序 | 已检查 | 当前页面只证明可见片段，不证明所有repo/删除项 |
| SRC-QWEN | [Research](https://qwen.ai/research)为动态壳，旧[qwenlm目录](https://qwenlm.github.io/)不能恢复2026目标日；有限恢复后停止 | 受阻 | 必要2026目标日公开目录缺口，不能据旧目录记零 |
| SRC-DEEPSEEK | [News](https://www.deepseek.com/news/)直接HTML无可定位的本窗公开字段，有限入口未形成目标日时间证明 | 受阻 | 需目标日官方研究/发布元数据，不把当前产品页当历史零命中 |
| SRC-MOONSHOT | [Kimi Platform Blog](https://platform.kimi.com/blog)旧Overview目录不提供本窗历史事件；[kimi-code releases API](https://api.github.com/repos/MoonshotAI/kimi-code/releases?per_page=100)实际81项、0.11=06/05 10:26:45Z→0.12=06/09 03:56:11Z跨窗；[kimi-cli API](https://api.github.com/repos/MoonshotAI/kimi-cli/releases?per_page=100)100项、1.47=06/05 10:35:01Z→1.48=06/22 12:50:45Z跨窗。只读metadata与边界，不深读窗外release | 受阻 | release片段已检查无本窗条目，Platform历史Blog目录仍缺；不合并成机构零材料 |
| SRC-TENCENT-HUNYUAN | [Research](https://hunyuan.tencent.com/research)动态页；实际只读publicList POST pageNum1/pageSize100/renderType0，total9/list9。逐项publicAt/displayDate都无目标日，读完9条metadata，不读窗外论文 | 已检查 | publicAt与displayDate不同，不用展示日反推first-public；目录保留局限 |
| SRC-ZAI | [Research](https://www.zhipuai.cn/zh/research)实际可见卡片06/16 GLM5.2→05/20 ZCube，停止在目标相邻区段；不拿图片上传时间作发布日期 | 已检查 | 更多列表/删除项未证明，无全机构无遗漏断言 |
| SRC-BYTEDANCE-SEED | [论文目录](https://seed.bytedance.com/en/public_papers)首20/242、page1/13，从06/11→06/04→06/03 MetaPoint→05/29跨过本窗，未读其他日正文；Research/Blog动态子入口未取得完整目标日元数据 | 受阻 | 论文首段已检查，Blog历史目标日仍缺，不能从论文页推出Blog零命中 |
| SRC-BAIDU-ERNIE | [Blog zh](https://ernie.baidu.com/blog/zh/)page1/2可见最晚05/09及更早，停止窗前，不读page2/正文 | 已检查 | 当前保留目录不证明删除项 |
| SRC-XIAOMI-MIMO | [Paper/Blog](https://mimo.xiaomi.com/)实际Paper8，日期06/29→03/13跨窗；Blog15无日期。既有公开前端route只提供UltraSpeed06/08日历日期，无法确认09:00后的发布上界 | 受阻 | 无日期Blog及UltraSpeed相交日保留；需对应原始带时区发布日期/快照，不能记零 |
| SRC-MINIMAX | [EN](https://www.minimax.io/blog)/[ZH](https://www.minimaxi.com/blog)实际可见06/09→06/01→05/27区段。06/09卡片为[MaxProof](https://www.minimax.io/blog/minimax-maxproof-math-proof-evolution)，原页JSON-LD datePublished=2026-06-09T13:43:00.000Z，晚于截点；不是凭M3 tag新造一个本窗发布。Agent techblog未获本窗历史时间 | 受阻 | 官方Blog边界已核，undated techblog历史目标时间仍缺，不反推整源零命中 |
| SRC-ARXIV | exact-v1摘要页/版本史只有submission；正确2026-06月列表2,718与前2,000切片无每日New/Cross/Replacement header；原0字节Atom不是成功查询。07881 DataCite Submitted/Updated/Available/Created语义已核，均不证实际first-public上界，112旧身份隔离 | 受阻 | 需06/08/09官方逐日公告或同家族带时区first-public正文记录。最早正常schedule只给下界，不能排除hold或证明[08:00,09:00) |

本日只扫描每日组及必要精确原始证据；每周源未扫描，未触发其他按需发现。上述“已检查”均限实际片段，不承诺全网无遗漏；受阻部分不支持零命中或正面采用。查询/恢复方法和旧有效材料集中在[唯一packet](../_sources/daily-20260609/V3_RECOVERY_BLOCKERS.md)。

## 3. 候选与判断

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [Measuring LLMs’ impact on N-day exploits](https://www.anthropic.com/research/n-days) | 2026-06-08T21:00:00+08:00 | 补丁公开不等running fleet已修复；受限利用的准备时间改变安全交付窗口与激活验收，不能只登记新制品结束：3+2+3=8 | 深入完成 | 整合：PLATFORM-SECURITY / [Ch72生命周期威胁](../../../../books/part-06-ai-infrastructure/72-security.md#生命周期威胁)，实际两段已写、非作者写后通过 |

公开原字段为官方Research hydration `publishedOn=2026-06-08T13:00:00.000Z`、slug `n-days`，转为北京时间21:00，完全落窗。厂商Research列表与原实验共同支持同一家族，不重复计数。日期未确认的112旧家族和MiMo目录线索不在此表，也不先评分。

## 4. 证据与知识整合

### [Measuring LLMs’ impact on N-day exploits](https://www.anthropic.com/research/n-days)

实际审阅2026-06-08官方原文Setup、Results、Figures1–5及Conclusion，精确网页版本与日期字段在[恢复材料](../_sources/daily-20260609/V3_RECOVERY_BLOCKERS.md#2026-10-01-当前日期隔离与有限恢复结果)。作者控制已知漏洞、环境与成功判据：Firefox148/149已修复且公开至少90天的18个SpiderMonkey漏洞，离线Linux jsshell不是完整浏览器；漏洞/补丁build经ASan，diff去掉regression test。每模型每漏洞3 trial、每trial最多3M token。Crash只证明PoC触发，native exploit另检随机secret只在脆弱build泄露。图1取3次最快而非均值/典型时延；PoC与exploit各自最快相加未必来自同一条执行。50次一致性测试是另一个分母，不混成前组全部稳定成功。

另一实验采用21个模型cutoff后的Windows kernel CVE，WinServer2025新VM、低权限起点、离线网络、无源码、提前约2小时decompile准备；18 PoC/8完整SYSTEM链只限对应模型和协议，nonce/whoami及新编译由独立grader验证。公开模型的safeguards关闭，因此不能直接预测默认公开服务的攻击成功率。它没有测真实目标投递、evasion或完整campaign；API费用不是包括准备、人工、构建与部署的完整成本，硬件等未披露字段记Not Disclosed，Serving batch/concurrency/SLO在此不是测量对象，不写成吞吐结论。

长期可吸收的是安全交付的时间与状态差额，而非漏洞利用操作细节：实际[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md#生命周期威胁)原有identity/integrity/authorization解释生命周期边界，却没有区分patch-public、制品登记与全部running instance修复激活。新增两段接在单一WAF结论之后、匿名凭据分支之前，明确暴露窗口、运行build与剩余实例/例外、policy时限、隔离/最小权限的能力边界及canary/兼容/SLO/rollback代价，并handoff到[PLATFORM-PRODUCTION / Ch73](../../../../books/part-06-ai-infrastructure/73-production-best-practice.md)。风险还取决于可达性、权限和漏洞；受控最快时延不等生产概率。apr29_close实际亲读primary与现有owner，纠正“risk由跨度决定”后批准窄写，再独立读实际两段与相邻内容，写后通过。没有自签采用、扩大到其他漏洞附件或重写安全章。

### 贡献前关闭及窗外停止边界

[Built to benefit everyone](https://openai.com/index/built-to-benefit-everyone-our-plan)RSS06/08 01:30Z的战略/分发路线、[Confidential S-1](https://openai.com/index/openai-submits-confidential-s-1)06/08 14Z的证券公告、[Industrial policy](https://openai.com/index/industrial-policy-for-the-intelligence-age)06/09 00Z的政策建议，实际核心说明没有新增本项目机制或可改变设计的评价证据，具体贡献前关闭；不拿机构声望评分。[agents-in-biology](https://www.anthropic.com/research/agents-in-biology)13:20Z的核心是暂缓的AI for Science，保范围理由，不展开领域全文。四项均不计候选；它们的准确原始标题与URL可在恢复材料内核对。

RSS Economic Research Exchange06/08 00Z早于起点，Notion/Nextdoor06/09 10Z/12Z晚于终点；Kimi0.11/0.12和MaxProof精确日期也在窗外，只作查找停止边界，不深读或计作本日已审重复候选。

### 旧材料的必要纠正与保留

112旧arXiv身份及原README全文保存在[唯一packet](../_sources/daily-20260609/V3_RECOVERY_BLOCKERS.md#2026-10-01-当前日期隔离与有限恢复结果)。本轮纠正CHAP09751的atomic persistent transition+entry与rollback追加而非BFT真值保证；07623实际有9系统23个确定certificate probes，不能写成“没有真实模型实验”。另07881版本delay、08761 APEX4混合精度/SM成本、09686的84-Format/6Tier1范围、07631诊断干预边界也已保存。仅恢复具体必要内容，不将它们或其余未读附件冒称112篇当前Evidence全通过。

旧11处书稿实际改动有独立写后核，2中央争议的原反证仍在；这些事实不证明112事件归属当前窗。没有据日期缺口删除其他来源仍支持的正文，也不再以旧“112全部已有覆盖”覆盖本次报告状态。

## 5. 缺口与下一步

普通可执行待办：0。唯一确定候选已完成必要证据、实际Books及非作者日级验收；以下只保留外部材料重开条件。

本窗外部缺口作为终态保留项隔离，不用于正面证据、Books采用或无遗漏断言；定点重开条件如下：

- 112旧arXiv唯一家族：具名ID/精确版本及原有效内容在[同一packet](../_sources/daily-20260609/V3_RECOVERY_BLOCKERS.md#2026-10-01-当前日期隔离与有限恢复结果)。缺官方本日New/Cross/Replacement、或同家族带时区首次公开正文上界；最新PDF/HTML、Submitted、DOI登记或月份Available不能补这个事实。接受官方HTML/RSS/公告邮件导出或时间语义明确的作者公开快照；收到后只重开对应日期、去重及必要采用链，不重扫1,235宽身份。
- MiMo UltraSpeed06/08相交日历日期及无日期Blog：需要目标事件标题/route与官方带时区发布时间或可核公开快照；目前不够确认09:00后的first-public，不用于正面采用。只恢复此接口/日期，不展开窗外论文。
- Google、Qwen、DeepSeek、Kimi Platform、Seed Blog、MiMo Blog、MiniMax Agent techblog的目标历史时段目录：各源实际停止与缺少字段见§2。可接受该目标区段的原始列表或准确官方事件URL/时间；缺口不能以当前空页、旧列表或版本边界声明为零。arXiv所需日期只请求一次，不与第一项重复建队列。

材料到达前保持明确隔离；本次普通工作完成后可达安全终态，但不会宣称全部Coverage/Evidence通过。没有自动重开相邻日报、Weekly或其他月份。

## 6. 复核

复核者：apr29_close（非报告作者；root编写本日报及Ch72两段）

结论：通过

独立复核实际读完正式六部分，逐行检查14源的范围和停止点，核实n-days精确公开时间、评分、必要primary与Ch72实际两段及邻接；四项贡献前关闭均独立读取官方核心说明，RSS与Kimi release前后边界、MaxProof窗外时刻及Hunyuan列表另行核实。发现两处packet当前句仍写旧待办，已改为112日期隔离及n-days写后通过，并经复读确认。112旧身份没有扩大为全文队列，旧完整报告与有效证据保留；外部日期/来源缺口不作Coverage或Evidence通过、正面采用或无遗漏声明。普通待办为0，本窗达到合同允许的安全终态。V3格式、一致性及限定diff-check通过；脚本不代替上述语义验收。保护既有staged/unstaged，未stage、commit或push。
