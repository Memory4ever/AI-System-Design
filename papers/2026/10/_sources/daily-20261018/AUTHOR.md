# Daily 2026-10-18 — 作者记录

作者：`oct18_missing`。独占本日 README 和本目录作者材料；既有 `REVIEW.md` 为 `live_oct18_reader` 的旧日程前置记录，保留，不把它当准入、Source 或 DAY。

## A1 — 首批准入校准请求

本窗：2026-10-17 ～ 2026-10-17（北京时间）。当前 AGENTS、Prompt、RESEARCH_CONTRACT、REPORT_CONTRACTS、来源说明/每日组/arXiv 主题范围、完整 ROADMAP 已重读。运行前工作区有大量其他 staged/unstaged 变更，均保护，不 stage/commit/push。

当前先交一个拟入选事件和四个分层排除样本；其余每日来源继续有限检查，不把此批当最终候选分母。

1. **拟入选：DeepSeek Search & Fetch（2026-10-17 官方开放事件）**。身份/日期：[Change Log](https://api-docs.deepseek.com/updates/#date-2026-10-17)，本地 `deepseek_updates.raw.html` 与 `.visible.txt` 第24–32行。核心说明完整读：`deepseek_search.visible.txt` 全文。准入句：Agent 需要在线检索但检索与正文获取具有不同成本和失败语义 → 本次开放两个独立只读 JSON endpoint，并明确空 Search 结果、不可用 content、Fetch security/site-policy 失败、独立 account/domain QPS → 需要分别判断发现、正文取得与重试，而非把有 URL 当已取得证据。拟分 1+2+2=5，标准审阅；不把未公开 SEO/GEO 过滤或厂商性能宣传当机制。拟 owner `AGENT-RAG` 或 `AGENT-TOOL-CALLING` 尚待具体正文比较；当前文档不是不可变当日快照，不把所有现行字段都反推为当天逐字发布。
2. **拟排除：同日 DeepSeek-V4.1-Flash-1017 Update**。完整官方核心说明与评价脚注已读，同上 `deepseek_updates.visible.txt` 第31–57行。API/价格保持不变，列榜单与任务时长/输出长度宣称，未披露产生收益的新架构、训练/推理机制及可比完整预算；不足以改变长期设计解释。不因版本号或更高分数入选。无撤回、纠错或安全新约束信号。未评分。
3. **窗外日期样本：Gemini 4 Argon 发布及安全说明**。由本次 DeepMind News 的 October 卡片进入两篇原文；官方均标 2026-10-13，非本窗，不重复准入。安全说明原文不是仅因 safety 标签关闭；读其日期后确认窗外，具体原文与日期在 `web-events.json` 和后续日期证据。原件恢复不继承 Oct17/19 的来源覆盖。
4. **范围样本：Google Research “Grounding AI agents in biological reality: Building blocks for autonomous wet labs”**。本次官方 Blog 列表标题与 2026-10-16 原日可见；直接指向生物 wet-lab 应用，处于 ROADMAP 明确暂缓的 AI for Science，不以 Agent/Robotics 词重新引入。无相关纠错/安全信号；标题范围明确即停止，不扩成全文队列。
5. **窗外产品样本：MiniMax M3.1 Flash**。本次官方 Blog 首屏明确 2026-10-19，窗外；只恢复身份/日期，不搬入 10-17。

原件：`fetch_results.json` 为本次实际抓取时间/入口/结果，`web-initial.json`、`web-second.json`、`web-directories.json`、`web-events.json` 为本次网页读取。当前普通待办：其余动态入口有限恢复、候选独立准入、必要证据与 owner 比较、六部分/日级复核。未自签通过。

## A2 — 首批准入独立校准后的改判

复核者 `root` 实际完整阅读本地 DeepSeek guide 与 A1 后，指出 A1 将成熟接口语义误计为本次设计贡献。作者接受这一具体误判依据，**Search & Fetch 在候选前关闭、不评分**；A1 的拟分 1+2+2=5 和拟 owner 未获采用，不是已完成的标准审阅或 Books 判断。

原文能支持的是 2026-10-17 开放 search/fetch API，以及现行指南所列只读 JSON、查询与取文分离、空结果/取文失败、按账户/域限流等接口事实。它没有披露新的检索、抓取或 Agent 执行机制，也没有对照证据揭示旧设计的新失效边界；“URL 不等于正文”“区别重试”等是借用的成熟原则，不能据此制造新增贡献。现行文档不是当日不可变快照，不能将所有字段反推为当日首创。核心说明与相关失败说明均已读；发布记录未见影响此处置的纠错/撤回信号。Flash-1017 同样在贡献筛选关闭，不评分。其余 A1 分层排除经 root 首批校准未发现共同误判；日级来源/全部六节尚待独立验收。

## A3 — 有限检查停点与外部材料边界

2026-10-20 13:12～13:28 +08:00 实际请求；原始批次见 `fetch_results.json`，后续网页读取保存在各 `web-*.json` 与 `webPublication*.json`。正文快照 `*.raw.html` / `*.visible.txt` 不是历史快照，不声称还原目标日逐字网页。只用其中明确事件日期与当前轻量纠错信号；未继承相邻 Daily 的候选或覆盖。恢复时重读适用合同、ROADMAP、本目录与本报告；本窗不扩大。

- **OpenAI**：Research index 直接请求 403，网页读取恢复其最新 9 卡（Oct19 至 Sep29）；RSS 前 30 项止 Oct2。Itau RSS 为 `Fri, 16 Oct 2026 19:00:00 GMT`，官方正文日历标 Oct16；未用小时过滤排除。完整核心正文由 `web-limited.json` 保存：IARA 编排、Customer DNA 业务上下文、文档/任务量与业务效率，未披露新的训练、执行或可归因系统机制。即使按 RSS 北京时间落 Oct17，也因贡献不足关闭，不再为不影响处置的日期请求材料。
- **Anthropic**：Publications 首页 10 项，Oct16 五项，经 Oct12/9 到 Oct8，未点 See more。早于窗的安全标题只作日期退出，不宣称证据审阅完成。
- **Google**：DeepMind Blog 的 October 2026 卡与第一处 September 边界；逐项恢复 Argon 发布/安全/Robotics 均 Oct13、EmbeddingGemma2 Oct6、端侧反诈 Oct14；抗菌肽标题直接属暂缓科学应用。Research Blog 首 10 项 Oct16 至 Sep24（先见 Sep29 边界）；wetlab 为范围排除，其他窗外。Pubs 默认页仅 15/11622 条，年份粗粒度，不扩全年。三个明确相关的目录身份定点恢复：GroupDPO=arXiv:2604.15602，v1 Apr17/v2 Sep1；Black Box to Toolbox=Zenodo 19700278（published Apr13、created/modified Apr22，区分字段）；multi-chiplet TPU co-design=作者 LATTE'26 programme 中 March23 同题作者与下载链接，PDF 一次 timeout。前两者原始版本远早于窗口；后者只能支持同题工作已有 March23 workshop 关联且未见 Oct17 新事件，不把 programme 日期改名为论文首次公开。保留年级索引无法证明按日穷尽的缺口。记录见 `webPublicationIdentity.json`、`webPublicationDate.json`。限量日期补检 query `site:research.google/pubs/ "October 17, 2026" "model"`、`site:deepmind.google "October 17, 2026"` 无结果，只作线索限制。
- **Meta**：Research HTTP200 但正文仅标题；Blog 可读首 10 卡 Jul27 至 Mar10/Apr6（编辑排序，不是严格倒序），无目标日卡；`site:ai.meta.com/blog "October 17, 2026"` 无结果。不能称目录逐日穷尽，隔离 Research 动态目录缺口。
- **Qwen**：旧入口明确迁往 qwen.ai；Blog、Research 与具名 `blog?id=qwen3_next` 均 HTTP200 94344-byte shell，只剩 Qwen；网页解析也空。一次浏览器运行时恢复失败（模块导入错误），没有冒称 UI 已读；旧站 underscore/hyphen 两个具名路径实际 404。窄查询 `site:qwen.ai/blog "2026/10/17"` 命中该 slug，但只显示 `undefined minute` / `0 words`，不能确认正文身份、日期或贡献。终态隔离，非零命中保证、非候选、无评分。
- **Moonshot**：Platform Blog 当前页 26 条，自 Nov7 2025 起；org 页首 10/42 仓库仅作线索，updated 不作 release 日期。因 kimi-code updated Oct19，实际追加 `https://github.com/MoonshotAI/kimi-code/releases`（13:26:59+08，HTTP200）首页首 10 releases newest Oct14、下至 Sep4；`https://www.kimi.com/code/docs/en/kimi-code/whats-new.html`（13:27:18+08，HTTP200）首 3 段 Desktop1.1.0/CLI2.2.0 Oct14 到 CLI2.1.0 Sep23。此前猜测 kimi-cli/guides 路径 404，精确导航成功，不是保留 gap。
- **Hunyuan**：Research loader 恢复官方 API baseURL；主域误试 404 后，`https://api.hunyuan.tencent.com/api/blog/publicList` 实际 POST `{renderType:0,pageNum:1,pageSize:20}`（13:20:50+08）中/英均 HTTP200 code0，到末 total11/9，见 `hunyuan_directory.json` 与原 JSON。中文最新 publicAt Sep22、英文最新 Sep23；displayPublishTime 与 publicAt 保留原字段，不因显示时间不同合并/改造。无 Oct17 条目，不继续旧页。
- **Z.ai**：Research 最新 15 卡 Aug26 至 Dec2025，没有目标日；停当前目录，不扫描 GitHub 普通更新。
- **Seed**：Research 特色/最新与 Publications；Papers 第 1 页 20/246，page1/13、显式 newest-to-oldest，最新 Sep28、下到 May26即停止；无日期的精选 SeedRealtime 定点恢复官方原文 Aug5。误猜 /en/blog 为空，但不代替已读 Research/Papers。
- **ERNIE**：Blog 第1/2页，最新 May9 2026 到 Nov21 2025；按可见日期停止，不扩第2旧页。
- **MiMo**：主页 Paper 8 项，最新 Jun29；Blog 15 标题无日期，当前 loader 恢复实际 route。定点原文 tool-call-repetition Sep27、V2.6 article Sep22、code-long-horizon Jun10、tilert Jun8、V2.5 inference May30；材料研发标题属暂缓科学应用（恢复 shell 无正文，不当已审）。未给余下 Blog 标题逐一伪造日期，不声明全站无事件，保留无日期目录限制。相邻 Oct19 缓存只用于定位 URL，所有上述原文已本日实际请求。
- **MiniMax**：Blog 当前首6卡 Oct19 M3.1 Flash、Aug13、Jul31、Jun9、Jun1、May27；Agent Tech Blog 共3卡 Oct8、Sep22、Sep19。只按日期退出，不复用他日分数/审阅。两入口未见 Oct17 卡。
- **arXiv**：本次 actual availability 原件与旧 R1/root 独立核验一致。Sun–Thu 20:00 Eastern、Fri/Sat 无常规公告；本窗对应 Oct16 Fri 晚 EDT，无常规批次。不因此推断其他机构为零，也不把周末提交当公告；未制造跨分类宽队列。

当前可执行收尾：整理六部分、结构校验、交 root 完整独立 DAY；无新增候选、无需 Books 变更。Google 年级索引、Meta 动态 Research、Qwen 具名空壳、MiMo 无日期目录的限制写入报告 §5，不支持覆盖穷尽、正面证据、Books 或性能/安全保证。

## A4 — MiMo 剩余可执行导航恢复（取代 A3 的 MiMo gap）

root 指出 Oct11 材料已有可执行导航，不能把剩余日期未读改称外部终态。已只拿其路径及 Oct19 iframe URL 作导航，不继承日期判断，并于本次 2026-10-20 13:31～13:33+08 实际取回当前官方页面与 route/frontmatter。

先误猜各 `/article.html` 得404，改用实际 Blog route 得壳，再按原导航实际请求8个 `/index.html` iframe，均HTTP200并重定向相应无后缀原件：`mimo-v2-omni`、`mimo-v2-pro`、`mimo-v2-tts` 均 March18th2026；`mimo-v2-5` April22nd；`mimo-v2-5-pro` April27th；`mimo-v2-5-asr`、`mimo-v2-5-tts` 仅标April2026（整月均窗外，不补造日）；`mimo-v2-flash` December16 2025。原件保存为本目录 `mimo_*_iframe.raw.html` / `.visible.txt`。与先前已恢复5篇技术原文合计覆盖首页13个主线技术标题的日期。

同时实际HTTP200读 Blog HSS 与 Safety（`mimo_v2_flash_hss_date.*`、`mimo_v2_flash_safety_date.*`），当前页正文日期均December22 2025；当前4752 route/frontmatter分别2025-12-19/18（`mimo_routes_current.raw.html`，13:31:26，官方CDN 743278bytes）。记录差异，不能混成精确首公开日，但全部远早于Oct17；未见需要本窗处理的Oct17修订/纠错信号。不将安全评估当新论文重审，也不因“安全”词跳过真实日期核验。材料研发剩1标题明确科学应用按范围关闭，壳不当已读正文。

由此删除 MiMo 外部gap，有限检查停于主页Paper/Blog实际所列材料及具名Safety，不扩产品文档、法律页或全站。此前 A3 的“其余主线日期未读”已解决；现在普通待办仅结构/链接检查与root完整六节DAY。

## A5 — Meta publications 实际恢复与检查

为避免现成导航未读即终态，实际请求官方 `https://ai.meta.com/results/?content_types%5B0%5D=publication`（13:35:22+08，HTTP200，285775bytes）与 `https://ai.meta.com/results/?page=2&content_types%5B0%5D=publication`（13:36:27，HTTP200，277161bytes），保存 `meta_publications.*`、`meta_publications_p2.*`。page1 24卡中当代段首12卡为Oct19 Glimmer、Oct14十项医学应用、Oct13 AutoformBench；继而混排2016～2021旧卡。page2亦24卡，当代段Oct2→Sep24/7/6→Aug4→Jul29/17，之后旧卡。仅将具名原页日历日期用于窗口定位，没有把数学/医学宽列表转为全文队列，没有把旧卡说成严格倒序。止page2当前段及首处旧卡，不翻更旧页；两页可见当代日期段无Oct17。

本次已恢复带日期的官方publication入口，替代A3“只能Research空壳/Blog首屏”的缺口描述。Research首页本身仍空，但不因单一路径空而称所有原始入口耗尽；删除Meta终态gap。结论只覆盖上述有限研究入口及停止点，不声称互联网无遗漏。结构校验通过，本日README/AUTHOR尾随空白0，10个本地引用全部存在；独立DAY仍待root。
