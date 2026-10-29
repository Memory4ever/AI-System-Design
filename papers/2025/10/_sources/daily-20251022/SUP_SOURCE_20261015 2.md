# Oct22 有限 Source 与单篇准入包

## 1. OpenAI / Atlas：本日日期与 release 窄 P 提案

本日自己的 [官方 RSS 原件](openai_rss_recovery.raw)1245项重新按新增 BJT Oct21（UTC [Oct20 16:00,Oct21 16:00)）本地解析，唯一命中 Atlas，pubDate Tue,21 Oct2025 00:00:00 GMT。原旧09点窗的 Japan/WhatsApp 两项仍具体 C，但不当新增自然日事件。RSS不是 first 证明。

2026-10-15 17:08 前后实际 web 完整读 [官方发布原文](https://openai.com/index/introducing-chatgpt-atlas/)L13–91，明确 October21,2025；可确认本日机构发布，不制造秒/TZ或全网首次。web实际可读；同URL独立直取 [raw](SUP_ATLAS.raw)/[headers](SUP_ATLAS.headers)为HTTP403/9765字节，保不同响应权限，不把403原件称正文成功。当前页L20明确已deprecated，属于当前状态，非历史撤回研究；不将现在已下线写回2025未发布，也不从旧产品推出当前可用。

拟窄P仅release约束变化：浏览器登录态/历史成为Agent上下文时，官方同时规定可见性关断不读取/不建memory、历史删除关联memory，以及敏感站点需观看、logged-out执行和禁下载/文件系统等权限边界。此为具体产品读写/派生状态与权限接口，不是“有Agent”即贡献。原文同时明确隐藏指令仍可能诱导外泄/非预期操作，控制不是prompt-injection免疫或完整删除证明；未披露独立可比安全评价/实现，不采更快可靠等营销结论。当前只交准入校准，若只现有成熟控制的发布事实，Books可仅报告，但须实际比具体owner后决定，尚未授分或采用。

## 2. DeepSeek-OCR：本日机构发布与窄 P 提案

本日 [DeepSeek news原件](deepseek_news.raw)实际结构解析OCR相邻anchor：2026-01-28 OCR2、2025-10-21 DeepSeek-OCR，后者链接 https://arxiv.org/abs/2510.18234 。本轮web实际读 https://www.deepseek.com/news/ L11–13，研究索引十条对应日期明确，可恢复Oct21机构研究发布，不再因缺时区/时分秒卡住；这不认证真正最早公开。

原轮 [日期原件](ROOT-date-originals.json)中精确v1完整AB有效；本轮current https://arxiv.org/abs/2510.18234 又实际读完整AB/history，仍唯一v1 Submitted Oct21 02:41:44 UTC，无可见纠错/撤回说明。submitted与机构date-only各保字段，不互代。身份未在原54题摘内，不增加原54读取分母；本轮单独一个机构发布family，待去重/准入校准。

完整AB窄增量：用光学二维表示承载文本context，DeepEncoder低activation压高分辨率图像为受控vision-token预算，由3B MoE decoder重建；重建质量随压缩比退化，是表示/压缩接口的质量预算问题，非普通OCR领域指标。摘要性能仅作者报告，不是长期语义记忆/精确无损、端到端成本或生产复现证明。拟P后必要证据将看精确v1机制/压缩设置/反侧，不预采摘要数字。

精确原件已单次取得HTTP200/241771字节：[v1 HTML](SUP_OCRv1.html)、[headers](SUP_OCRv1.headers)，URL https://arxiv.org/html/2510.18234v1 。本节目前只AB准入及日期权限，未声称已读此HTML核心或Evidence完成；准备即交root，不等其余Source。

## 3. 停止与剩余

Atlas web有效/直取403不重复请求；DeepSeek两种日期角色明确，不追first秒。其余本日有限Source恢复、arxiv主题发现/current/date及六节仍普通待办；本包不授Source总通过、评分、Books锁、DAY或FINAL。此前误把大JSON单行打印导致输出截断，已用结构提取OCR字段补齐；不把截断当读完全字段。

已发生root§3：实际Atlas原文13–91/DS索引11–13与OCR本日HTML完整AB均已读，两个Oct21机构事件/date-only及窄贡献通过；不授安全效果或当前deprecated倒填。以下为作者实际后续证据/评分/owner判断，待root具体核验，不预签。

## 4. OCR 必要证据、5分与已有覆盖提案

作者实际精确v1 §3.1–3.5、§4.1–4.3/Tables1–4、§5–6。未核代码/实验复现，不把图题的定性例子当人评。拟采用命题为“光学传输用视觉encoder前级局部计算/压缩后的全局计算换decoder token预算，而质量/成本必须按密度、分辨率及consumer分账”，评分2+1+2=5；由于具体长期边界比较，受影响域读足，不仅AB。

§3.2：SAM window主导→两层stride2卷积→CLIP global（去原patch embedding）；1024图从4096patch到256vision tokens后再全局attention，不等于整个视觉处理只做256token。§3.2.2/T1 native64/100/256/400及dynamic n*100+256，valid/padded tokens不同；Gundam-M继续训练，不与初始多resolution训练当同一操作点。§3.5前训练encoder、再训整体，SAM/compressor冻结而CLIP可训；多stage/160 A100训练与encoder/renderer/decoder费用不由少reader token免除。

§4.1/T2仅Fox100英文页、600–1300个本模型text tokens，Tiny64/Small100；不同文本密度及分辨率的重建精度下降，作者布局/blur解释尚未独立控制。§4.2/T3–4为OmniDocBench edit distance，越小越好，不和T2 precision合并；不同系统tokens不是相同模型/训练预算对照。新闻纸Tiny .94而Gundam .122/Gundam-M .099，某些FinancialReport Gundam .289反而差于Small .079/Base .027，不能签所有文类随token单调改善。padding“valid tokens”不等实际KV/算力计费；未披露统一精度、batch/concurrency/SLO或完整端到端成本，Not Disclosed，不补。§5–6明确未来才做interleaved pretraining/needle等，OCR不足验证true context compression；多轮语义保持、无限上下文、无损和零开销不采用。

已实际重读Books适用背景/理念/指南、ROADMAP当前owner与相关checkpoint。唯一owner `MULTIMODAL-REPRESENTATION` / [Ch23](../../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)：完整478–568 rate/distortion/容量与计算放置链、576–588 artifact合同、710–737 optical输入/历史消费与读出分责，以及1492–1505章节交接已读。前两段“把页面渲染…视觉tokens/布局字符密度”与“renderer/分辨率/encoder/tokenbudget/readback”已经实际承载本次拟采用的光学表示边界；rate/distortion段明确压缩成本转交与不能排encoder/decoder费用，前移downsampling的已有分支亦解释计算放置取舍。OCR提供更早的受限实例/局部参数，不要求在这些已足够的论证上再堆一个SAM/CLIP配方。拟 Books：已有覆盖、No Change，不造新gap，不申请锁/不写书或notes。

## 5. Atlas 3分与仅报告提案

拟采用命题只为“本次browser发布声明的可见性/派生memory删除与执行权限边界”，不是安全有效性。DesignDelta1+SystemReach1+Durability1=3：局部版本控制公布，没有新可验证安全机制或持久可靠性证据，未把成熟最小权限/删除原则加分。发布核心/直接风险域和当前状态已实际读；不采速度、redteam时长为安全成功率、不可执行代码为无注入风险。

实际owner比较：`AGENT-MEMORY` [Ch77](../../../../../books/part-07-agent/77-memory.md)完整1–118、578–588、1253–1292与1630–1642；已写consent/read/write authorization、derived view lineage/correction/delete/rebuild与用途隔离/撤权不等旧派生删除。相邻 [Ch78](../../../../../books/part-07-agent/78-tool-calling.md)1–36及589–628明确executor与preventive/evidential分权、已读秘密不可撤销/具体effect仍需前置授权。它们解释了发布约束的长期原理，但不证明Atlas实现或安全效果。故仅报告这个版本的官方产品事实，不更改长期知识/不声称需要逐个禁用功能名入书；无Books写锁/改动。

## 6. Qwen 本日接口窄恢复

本日own research壳实际引用969.js；新取 [969原件](SUP_QWEN969.js)HTTP200/10114字节，实际39759/25868/44467模块给`/api/page_config?code=`、`/api/v2/article/retrieval`与language注入。没有重试旧4467.js404，不借前日成功。

本轮按本日own接口各一次：[article40](SUP_QWEN_ARTICLE.json)（[headers](SUP_QWEN_ARTICLE.headers)，HTTP200/4781799字节）与[config60](SUP_QWEN_CONFIG.json)（[headers](SUP_QWEN_CONFIG.headers)，HTTP200/72628字节），参数分别type=qwen_ai/language=en-US、code=research.research-list/language=zh-cn。实际完整40+60 compact title/path-or-id/date已读，七重合path合并后93目录身份；这是有限目录，不是93AB或未来正文队列。config最近目标邻居Sep24 Qwen3-Max与Nov13BJT DeepResearch，均无Oct21标签；article最早Nov13。不能从这100元记录证明全历史无事件。qwen-tts17的title、目录date和bodyMeta可能有历史冲突，不用future/content正文补全未观察日期；本轮只目录层，若需采用才定点读具体字段。

首个诊断误把extra整对象（含introduction）打印，输出截断，已改为40条仅title/path/extra.date及60条title/id/date分别补齐；不把截断当全读，不采用future正文或扩2026。止两个实际列表，无猜分页/全chunks/盲UI；目标历史未列artifact仍独立保留，不以零命中代无遗漏。

已发生root§5：实际SOURCE4–6与Ch23 optical/visual-history/容量合同完整局部，OCR5分/已有覆盖NoChange、Atlas3分/仅报告均通过，不写原notes；本日Qwen40+60白名单全读/100→93/7与目标邻接重算通过，不授全历史。以上无Books待写/锁，不重复Source/owner。

## 7. 其余机构有限差额与安全停止

本日原FETCH/RECOVERY/THREE_SOURCE及旧FINAL的实际审阅层，仅在身份/字段/停止范围未变时复用；不声称新增网络请求或继承上日Source。日期门改为date-only，不追秒。原字段见原README§2及SCREENING，对应十四Daily入口均保留，以下新增两个有意义恢复分支，不重原失败。

- Hunyuan：本日own index JS实际header为en/zh；正确POST api.hunyuan.tencent.com/api/blog/publicList、pageNum1/pageSize200/renderType0，仅新取zh分支一次，[raw](SUP_HUNYUAN_ZH.json)/[headers](SUP_HUNYUAN_ZH.headers)HTTP200/442610字节。实际compact 11条全部title/id/publicAt/publishedAt/displayPublishTime读完，与本日原EN9条分别保留；三时间不互代，最旧均2026Feb3，只给当前目录历史缺段。未读futurebody，不重原错误host404/超时/browser。
- Kimi：由本日原blog anchor进入[原生changelog](https://platform.kimi.com/blog/posts/changelog)，[HTML](SUP_KIMI_CHANGELOG.html)/[headers](SUP_KIMI_CHANGELOG.headers)一次200/14815字节。实际目标完整Oct2025段只有Oct27，邻居Nov6/Sep5；页面发表于Nov7和内部分段事件分责，不把0916–1015促销活动区间当Oct21技术发布。原blog25与GitHub18s失败保留，不重失败Github。观察到的日志不代所有历史artifact。
- Zai：[独立release入口](https://docs.z.ai/release-notes/new-released)一次200，[HTML](SUP_ZAI_RELEASE.html)/[headers](SUP_ZAI_RELEASE.headers)257073字节。实际8个日期heading，目标邻接Sep30/Dec22，无Oct21heading；dateModified2026Oct10不是各release日。仅必要目录/目标段权限，首个main提取连带展示future说明，不因此采用/扩未来研究。与本日Research页2累计18/hasMorefalse的历史缺段分责，不当所有发布零事件。

其余有效有限层：Anthropic本日publishedOn邻居Oct14/29（createdAt非发布）；Google官方月档p1十二标题邻居Oct22/20与DM current最旧2026May，正确pubs旧失败不重，月档不代pubs；Meta原18s失败及两种目标补检首屏不重；Seed本日type1/2年2025/US各18记录与total94/45、next20/hasMoretrue只覆盖目标邻接，量子领域C保持，Seed3D Oct22目录/Oct23blog与submission各保原字段，不因此关更早family；ERNIE p1/p2六记录/2of2和MiniMaxEN12/CN13有效有限层复用。MiniMax Agent旧May13单条现仅保历史响应，不再称未变当前目录，本轮新恢复见§8。均不全Source/全年正文，不把宽目录条目变逐篇队列。

MiMo本日Paper8/Blog15及11370v1完整AB/history有效层复用；目录Oct21路由可给该机构目录发布字段，但不自动证明全网first或重复转载有新delta。v2 Submitted Oct21 17:19:46UTC是BJT22，不能授Oct21 arxiv修订事件；尚无本日实质变化证据，保具体事件缺口，不把整个family关闭。窄查MODEL_NARROW再次出现同身份只去重，不加第二家族/分数。

本包Source有限出口待root实际回核，未知历史段不支持正面证据、Books或无遗漏断言。普通仍为arxiv后批/必要受影响域与日期六节/日级验收，不把尚未读项藏为external。

## 8. MiniMax Agent 当前目录窄恢复

root具名指出旧May13单条已非当前目录，撤销“未变当前字段”复用权限，仅保旧原件历史角色。2026-10-15约17:35 BJT，本日own各一次GET https://agent.minimax.io/docs/techblog 与显式 https://agent.minimax.io/docs/llms.txt ，均经307到agent.minimaxi.com、302到agent.minimax.cn，最终200；不是重旧失败、UI绕路或他日原件继承。

- [techblog HTML](SUP_MINIMAX_AGENT.html)/[headers](SUP_MINIMAX_AGENT.headers)：225926字节，实际main内h2/h3/a读三组完整title/date/path，止当前列表：2026-10-08“Agent越多，我越忙：我如何走出AI编程的监工困境” `/docs/techblog/coding-agent-workflow-and-skills`；2026-09-22“给Coding Agent建一座试验场” `/docs/techblog/coding-agent-eval`；2026-09-19“MiniMax Code正式开源：拆解Coding Agent背后的Harness架构” `/docs/techblog/minimax-code-harness`。
- [显式llms索引](SUP_MINIMAX_LLMS.txt)/[headers](SUP_MINIMAX_LLMS.headers)：8404字节，完整索引实际读完，三Tech路径与页面一致；无单条article body请求，未遍历其他docs条目或future正文。索引描述只是导航，不当核心技术说明已审。

旧May13 Agent Team单条与本轮三条目录各保响应身份，不把前者改成当前，也不从三条2026目录宣2025不存在。目标历史段仍受阻；定点重开需原2025Tech发布/日期或可靠历史目录，不重扫公司Blog、不继续全docs。OpenAI necessary Research403/历史段已按root指出改为受阻，RSS/Atlas有效成果不受影响。
