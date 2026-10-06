# Daily Research — 2026-03-20

**规范：** V3
**窗口：** 2026-03-19T09:00:00+08:00 ～ 2026-03-20T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-10-02T03:36:54+08:00

## 1. 结论

本日冻结1个确定家族：内部 coding-agent Monitor 的员工选择性正例与异步检测边界；1项深入完成、1项实际整合Ch66、root非作者写后复核及整日日Gate通过，不授总体漏检率、实时阻断或通用安全保证。14源与有限主题/相关标题查漏已停止；另22个arXiv及FlexTrain共23个具名潜在线索首次公开区间未能完整落窗，隔离而非候选、Evidence完成或零命中。普通待办0。旧734行报告完整保存在[原报告](../_sources/daily-20260320/V3_LEGACY_REPORT.md)，不继承644分母、19候选、9分、NoChange或EffectiveDate。原值与停止范围见[唯一停点](../_sources/daily-20260320/V3_WORKING_STOPPOINT.md)。

## 2. 来源覆盖

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | fresh官方RSS1242；仅Mar18–20邻接2条，原字段见停点 | 已检查 | 1确定Monitor；Astral在左端前，不授全机构历史 |
| SRC-ANTHROPIC | Research fresh290015B；March9条title/publishedOn全部对读 | 已检查 | 可见Research切片无本窗行，不外推News |
| SRC-GOOGLE-AI | Research March12+原page2metadata2条；DeepMind真实page3/24卡，6March原页date核 | 受阻 | Blog有限停止；pubs1–15/11569、2026count372不能定位本窗，H1 |
| SRC-META-AI | Blog第一页10+实际Next第二页12，非日期排序；Mar27/26→Mar11/10跨窗 | 受阻 | Blog可见22无本窗dated行；Research0行，H2 |
| SRC-QWEN | fresh只读article API40 title/extra.date；Mar19T04+08左端前→Mar30跨窗 | 已检查 | 当前40非全机构；无exposed total/paging，不保留dynamic gap |
| SRC-DEEPSEEK | freshNext posts16与9467B真实Research数组；Sep/Apr→Feb/Jan跨窗 | 已检查 | 原始已恢复隐藏News/Research无本窗可见行；不授全机构历史 |
| SRC-MOONSHOT | 官方Kimi/en/blog可见19 dated卡，Feb9→Apr20跨窗 | 已检查 | 停完整19可见目录；非所有GitHub release |
| SRC-TENCENT-HUNYUAN | fresh生产publicList renderType0/page1/size20，code0/11返回共11；原paired字段见停点 | 已检查 | Feb3/13→Apr23display，实际published无March；不互当firstpublic |
| SRC-ZAI | Research15可见dated项Mar15→Apr1；releaseNotes16条Feb12→Apr7 | 已检查 | 两可见切片无本窗行；不授所有News历史 |
| SRC-BYTEDANCE-SEED | fresh type1/year2026/token20/count100返回18/82,next40，Feb25→Mar20→Mar26停止；type2返回14/19,next空/hasmorefalse | 受阻 | D23 FlexTrain日字段与exact原稿firstpublic未定；未返5 Blog身份/date H5，不授19/19或扫82 |
| SRC-BAIDU-ERNIE | Blog/zh第一页10卡，Apr15→Feb6跨窗 | 已检查 | 无本窗可见行；不把next旧页成队列 |
| SRC-XIAOMI-MIMO | fresh首页Paper8/Blog15；错误/blog/壳后恢复官方/mimo-v2-pro、/mimo-v2-omni完整core，两篇贡献前关闭 | 受阻 | 两原页March18无时区day字段未当确时；H3仅15 nondated Blog的本窗dated历史切片，非正文故障 |
| SRC-MINIMAX | Blog12卡Mar18→Feb14；AgentTech真实llms→techblog.md880B仅May13 AgentTeam，独立对读19原元数据 | 受阻 | 当前dated list已可读，不授历史complete；H4仍需本窗历史dated切片，不扩guides |
| SRC-ARXIV | Submitted Mar18–19的系统28/28、模型Agent50/217、多模态50/121、优化50/82；start0/max50。官方cs.DC/2026-03?show=250返回250/346，只浏览17000–19600相关10标题查漏 | 受阻 | 四查询有重叠不可相加成日级唯一数；22完整v1题摘日期隔离；剩167/71/32及月表未展开非全量已审，宽目录非队列 |
| SRC-OPENREVIEW | D23 Seed已观察exact h2yhNcbwSL forum/PDF，api2 exactnote ChallengeRequired403 | 受阻 | 需该note/PDF firstpublic，不扩venue |
| SRC-MLSYS | D23同identity官方poster/3776完整题摘，页面会场May20日程；仅定点恢复 | 受阻 | 日程不是firstpublic；不假称新研究或已审重复 |

## 3. 候选与判断

来源与贡献筛选已安全终态；确定候选仅以下1家族。23项日期隔离不评分、不进入此表；完整題摘读足潜在贡献不等正文证据审阅。

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [How we monitor internal coding agents for misalignment](https://openai.com/index/how-we-monitor-internal-coding-agents-misalignment/) | 2026-03-19T18:00:00+08:00 | 员工选择性正例不能估总体FNR，异步completion后检测不能授执行前prevention；2+2+3=7 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)3914/3916两段，root实际POST通过 |

## 4. 证据与知识整合

### [How we monitor internal coding agents for misalignment](https://openai.com/index/how-we-monitor-internal-coding-agents-misalignment/)

官方RSS原`Thu, 19 Mar 2026 10:00:00 GMT`定本窗事件。采用core Our approach/Limitations/Towards a safety case/Road ahead（原L35–77），作者另读分类案例L178–339，不以案例数授总体安全。公开监测使用内部fullhistory/CoT/tooltrace与human triage，当前completion后30min审阅；捕获所有employee-escalations是选择性正例，open-ended FNR仍未定量，synthetic sabotage control作者自述容易，synchronous blocking仍未来。未覆盖bespoke/local traffic及私有trace访问条件保留；没有复现实验或独立实现审计。

Ch66原detector0段已有零命中≠零风险，但没有上述selection与intervention时间对象差异。本日保留旧matched twin/adjudication路径，3914/3916融入两段与Review note；EvalSpec检测/干预/预防分账明确为本书推断，不复制产品堆砌。作者实际读owner相关论点与65exit/67intro；root实际core→正文3888–3928前后链及note/交接POST通过，锁已释放。

## 5. 缺口与下一步

普通待办0；root整日日级独立验收通过。没有继续可执行的日期/core队列，不扩217/121/82或venue。未来材料到达只重开具名受影响项。

以下D1–23及H1–5均为本窗终态保留项，不支持正面证据、Books或无遗漏断言；仅在指定材料返回时按下述身份/入口定点重开，不支撑正面Coverage/Evidence通过。

D1–22 exact-v1题摘与各exact DOI字段实际核：18897/19133/19057/18815/18718/18567/19233/19131/19092/18636/18742/19335/19220/18373/17435/17456/17803/18383/19199/19201/19172/18534。Submitted不是公开时间；官方ID在公告时才分配，20EDT对应次日08BJT，D1–14/D18–22的最早可能常规公开08与登记上界10点后或更晚跨右09，D15–17跨左09。Updated、月表membership不能补公开上界，因此23项不是当窗确定候选。D23 FlexTrain Seed PublishDate1773936000000仅目录整日字段；原OR受challenge，MLSys题摘只有会场日程。每家族精确请求其exact-v1公告timestamp/真实batch及正文可取上界或作者/venue firstpublic；D7 workshop、D15 ASPLOS只定点原稿，D23需h2yhNcbwSL publicnote/PDF首公开。完整原值与逐项身份见停点，后批11完整原文保存[题摘](../_sources/daily-20260320/V3_ABSTRACTS_11.md)。

历史切片H1 Google pubs本窗可定位导出；H2 Meta Research本窗可读publication列表；H3 MiMo15 nondated Blog的本窗dated切片，两必要原页已恢复且贡献关闭；H4 MiniMax AgentTech本窗历史dated列表，当前880B/May13不证明本窗；H5 Seed14/total19未返5身份/date或差额解释。均外部终态，不支持Coverage/Evidence正面通过、Books或无遗漏保证。

具名分层负侧：ACP18829v1必要安全core的single-use ET/attenuated delegation/immutable correlation与retry配置，未识别新增适用约束或协议failure-boundary证据；heuristic risk不授安全估计、traceability不防collusion，不因组件组合自动排。ODA19016v1通用HPC综述未新增本项目执行/状态/validity条件；ICLAD19497v1 tabular监督统一与任务排行未识别主线新边界；18660病理应用仅标题范围关闭、未宣称完整题摘。MiMo Pro配置/继承Hybrid/MTP与排行、Omni共享encoder/backbone及future prediction泛述，未披露新的长期设计机制/条件；不是缺全配置/ablation单独排，不授榜分归因或部署安全。六项详细理由和实际读到范围见停点。

## 6. 复核

复核者：root（非作者；分批准入/具名安全负侧、Monitor实际POST与最终整日日Gate通过）。

结论：通过

root实际核18897/19133/19057及19092/19131/18636/19335共7个完整v1题摘/history，具体potential通过、日期仍隔离，未授数字或普遍因果/全文Evidence。Monitor必要core L35–77→两实际Books段与3888–3928邻接、65/67交接及note实际POST通过。负侧root实际ACP完整题摘和§3.1–3.7/§5.2–6.3、MiMo Pro7–32/Omni17–27核心，三项具体关闭通过。其余15个arXiv/1 FlexTrain仅作者完整题摘，ODA/ICLAD未称root抽核、病理仅标题；未复核宽库存全部正文。最终同步后V3 validator（含本地引用）及限定README/_sources/Ch66的git diff --check实际PASS；Ch66既有其他日期改动保留，静态检查不替代日级语义验收。

root最终实际完整读本日六部分与唯一停点，检查14源/四主题及相关标题有限停止、23项原日期与逐项重开请求、六项具名负侧分层记录、OR/MLSys定点触发与五历史限制、候选7分采用边界和Books结果，日级Gate通过。不是对23潜在项授全文Evidence、对未抽核负侧授全量验证，亦不是无遗漏或隔离来源的正面Coverage保证。
