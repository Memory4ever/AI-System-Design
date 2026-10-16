# Dec23 本日有限 Source / 日期差额

## 1. 复用范围与真实新观察

本轮只补2025-12-22 BJT，UTC[2025-12-21T16Z,2025-12-22T16Z)。本日原SOURCE_STOPS/原README/独核按具体入口、邻接与停止复用，旧小时route不自动覆盖新增日早段，不继承Dec22报告任何来源成功。原目录上下邻接跨过新增日时，只支持有限切片判断；historical缺段不授全机构零事件。

Newton本日§3/5/9的新release notes、Qwen60/40日期投影、MiniMax独立Agent与RSS1293已经实际读到，可复用不再GET。作者本日MiniMax原Blog标题下实际Dec23，再次明确只该已知发布事件晚于新增日；未知更早卡事件另责。一次初始搜索字符串site写法失配返回泛化第三方，仅发现线索不采；随后两条明确限定minimax.io/minimaxi.com、M2.1＋2025-12-22/12月22日查询空，辅助检索止，不从空命中证明日期不存在，不展开论坛/后续文章。

## 2. 每日14来源具体终点（本轮尚非DAY）

| 来源 | 本日实际范围/增量与停止 | 处置/限制 |
| --- | --- | --- |
| SRC-OPENAI | 原Research9当前项/LoadMore有历史缺段；Newton5本日RSS200/1293条，Dec22BJT两项Atlas/Customers，原值均Dec22 00GMT | 同事件Atlas既有采用去重、不增家族/重POST，Customers原具体C有效；feed非全Research |
| SRC-ANTHROPIC | 原Research10当前/历史恢复SSL有限停止；Alignment Dec19→16→12→8→Nov | 新Dec22在邻接之后无项不代主Research历史；不重旧失败 |
| SRC-GOOGLE-AI | 原DeepMind正确page4跨Feb26–Nov25、Research2025第1页12条Dec18→Nov12；ScopeDec19T12Z/GenesisDec18T19Z | 两已知事件均早于新增日，非旧09点排除；publications历史过滤/个体firstpublic仍缺 |
| SRC-META-AI | 原global_search page3 24混合项/Dec18watermark与SAM邻接 | 不是严格历史主列表，公告不授论文firstpublic；精确历史目录缺段 |
| SRC-QWEN | Newton5本日真实page_config根60、retrieval articles40，仅读title/path/id/date/extra.date；Dec19Layered→Dec23TTS/VoiceDesign/ImageEdit邻接，新Dec22无项 | 有限数组以外缺段，不读futurebody/不授全机构零研究 |
| SRC-DEEPSEEK | 原updates Apr24/Dec1及更早条无Next、原V3小时route；本轮V3早段空 | 仅release/指定repo，不做全机构承诺 |
| SRC-MOONSHOT | 原26Blog至2024May29/最新Nov7与changelog Nov6→Oct27→Sep5；本轮KimiK2早段空 | 有限目录/指定repo，不读后续文章 |
| SRC-TENCENT-HUNYUAN | 原publicList全部11仅2026，旧Video/WorldPlay所见committed Dec23不挪；本轮T1/Video1.5/WorldPlay早段空 | 2025主目录缺段；author/commit/push不是public |
| SRC-ZAI | 原Researchpage2 18无More；Newton3/作者本轮release notes明确GLM4.7 Dec22；旧同事件core＋本轮必要current指南另责 | 发布日门已解，5分/Source/PRE Newton8通过、root1许可后真实保存及Newton10 POST通过待root读回；未知不同早稿不从目录字段授日 |
| SRC-BYTEDANCE-SEED | 原type2 year2025 page0 15/49 next20 Dec24→18→16→2；type1 18/94 next20两pinned后Oct21→Jun25 | 非严格目录/Seed1.8旧card历史仍缺；Dec24不提前，未把next当读完 |
| SRC-BAIDU-ERNIE | 原中文Blog两页Dec23→Dec9→Nov21，Preview1203完整短文只榜单/申请体验，具体C | 已知Dec23事件晚于新增日，不追时刻/后续Feb稿 |
| SRC-XIAOMI-MIMO | 原Flash Dec16不移；edd3187实际旧patch仅bibliographyURL修正，本轮早段空 | 普通维护C/同event去重，不把commit授firstpublic |
| SRC-MINIMAX | 原模型Blog12条Dec23→Oct27；作者/reader本轮已知M2.1 BlogDec23；Newton5独立Agent66行/llms54仅2026三路径无Next | Agent2025历史缺段；固定SHA初始卡内容已恢复但不同更早首次公开未证，不用模型Blog替Agent |
| SRC-ARXIV | 原四窄header/页尾与227unique，218+9完整v1 AB、9title有效；cs.CL只18600–20050相关title补检；Newton4新分层3C/总43唯一v1独核；具名current见SUP_CURRENT | 发现不是公告池，未取得individual Dec22 firstpublic；旧日期恢复已有限停止，不legacy/catchup/扩236全文 |

## 3. 七个原已触发 repo 的新增早段实际补核

作者本轮通过GitHub连接器逐一实际GET以下官方REST commits collection，统一参数`since=2025-12-21T16:00:00Z&until=2025-12-22T00:59:59Z&per_page=100`。七响应均成功返回`[]`，实际结束，无后台请求；空数组即该route终点，非所有branch/研究全史。它们只补原小时route未含的新增日00–09BJT早段，不重旧维护patch或扩大周源。

- https://api.github.com/repos/QwenLM/Qwen3/commits
- https://api.github.com/repos/deepseek-ai/DeepSeek-V3/commits
- https://api.github.com/repos/MoonshotAI/Kimi-K2/commits
- https://api.github.com/repos/Tencent/llm.hunyuan.T1/commits
- https://api.github.com/repos/Tencent-Hunyuan/HunyuanVideo-1.5/commits
- https://api.github.com/repos/Tencent-Hunyuan/HY-WorldPlay/commits
- https://api.github.com/repos/XiaomiMiMo/MiMo-V2-Flash/commits

原GITHUB_WINDOW的Video1.5一条/WorldPlay五条committed Dec23晚于新增日而pushed null，author早日不搬事件；MiMo edd3187 Dec22 16:47BJT只是bibliographyURL维护，实际内容C不要求firstpublic。原route空/错时条不授公开事件闭包。

## 4. 日期与按需边界

GLM已知Dec22发布可进入新增日单篇处理；Atlas已知Dec22按同事件既有采用去重。MiniMax已知BlogDec23、ERNIE已知Dec23、SeedProverDec24与Scope2/Genesis更早分别窗后/窗前，未知更早独立card/研究事件不随它们关闭。其余具名arXiv潜力需要匹配ID/版本的官方公开公告或完全落在Dec22的历史公开上下界；Submitted/API published/ID月份/一般排期不代public。源不可得终态只隔离精确依赖，不降潜力或宣无遗漏。

本日本地原记录未见实际OpenReview forum/note/PDF请求，20677的ARR文字不是已经访问OpenReview，不继承前日Reflection触发；若后续具名必要论坛实际触发，再正式添来源行。未扫描每周源/会议全站，无其他已触发来源被取消。尚有GLM root协调与six实际合并/日级，不能把本表当完成态或预签DAY。

作者另以19027完整题名＋December22、Remoe＋December22/serverless、MPK＋2512/megakernel/December22三条辅助公开日检索作有界具体补核；实际返回ScienceStack等转载/无关项，未恢复匹配的官方公开事件。搜索只作发现，不读转载为新Methods、不把其Published/正文投影授日期；停止不扩池/搜全236，不用空命中或Submitted宣布不存在。本轮普通发现/必要原证作者动作已收束，余是具名reader current差额、GLM root读回及完整six独核链，非本表预签完成。

作者已实际读Newton§12：本表1–4及七repo新早段实际独立GET全部通过，有限Source/date/按需分责成立；§11也已实核两current新增必要域。上述普通研究/具名独核差额均0，仅GLM root读回/行政与真实six DAY链未完，不用旧“待current”制造新研究。
