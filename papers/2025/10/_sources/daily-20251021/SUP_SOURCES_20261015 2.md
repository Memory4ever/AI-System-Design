# Oct21 有限 Source 差额

不继承 Oct20 source 成功。本日原 FETCH/THREE_SOURCE_RECOVERY/SCREENING 与原 FIRST/FINAL 中身份/字段/范围未变的真实独核仍有效，重读其本日记录后只恢复具体差额；失败不重试 legacy、浏览器或 UI 绕过，不对未来正文/历年 Source 扩扫。

## 1. Qwen：本日 own 引用恢复，不再停壳

原 qwen_research_recovery.raw 明确引用 `/0.0.85/js/969.js`，Research route 依赖亦有969；本轮实际取 [SUP_qwen969.js](./SUP_qwen969.js) HTTP200/10114 bytes。模块44467给 `/api/v2/article/retrieval` 和 `research.research-list`，39759给 page_config，25868给真实参数 `language`。不是重试旧猜测4467.js的404，也不靠他日成功签本日。

实际两 GET 15秒/retry0：`https://qwen.ai/api/v2/article/retrieval?type=qwen_ai&language=en-US` HTTP200/4781799 bytes，[原件](./SUP_qwen_articles.json)40 article；`https://qwen.ai/api/page_config?code=research.research-list&language=zh-cn` HTTP200/72628 bytes，[原件](./SUP_qwen_config.json)60 config。原 API 返回嵌正文但本人只提取 path/title/extra.date，未读未来 body；config只读 id/title/date，未读 introduction。

100 records/93目录身份/7同path overlap。60 config 最晚旧邻接 Sep24 Qwen3-Max，下一现可见 Nov13 DeepResearch；40 article extra.date 最早亦 Nov13。各日期保原 ISO 字段，不补 first-public，不把目录断层当全历史无 Oct20。未使用误 `lang` 参数。本轮不再取未来文章、全 bundle 或用壳200当历史目录。

## 2. Hunyuan：中文接口差额

本日旧 hunyuan.raw 指向 index-I3I3bCf9.js；本轮取该 own index HTTP200/542746 bytes，实际核 API host `https://api.hunyuan.tencent.com` 与语言 `en`/`zh`；Blog own `index-CUQAWQeM.js` 200/10220 引用 `index-cEoitnb7.js`，后者200/429明确 `/api/blog/publicList` POST。均本日保存 SUP_hunyuan_*，不是猜 host 或复用前日响应。

实际 `POST https://api.hunyuan.tencent.com/api/blog/publicList`，JSON pageNum1/pageSize20/renderType0，header accept-language:zh，HTTP200/442610 bytes，[SUP_hunyuan_zh.json](./SUP_hunyuan_zh.json) totalNum11/list11。只读全部 id/title/publicAt/publishedAt/displayPublishTime，未读未来 content。最旧100025：publicAt1770112929、publishedAt1770092288、displayPublishTime1770092288；100061三个分别1783244694/1782308557/1776873600，不把三时间混成同一发布字段。它们均2026，目标2025历史缺段；本日旧英文9响应角色保持，不冒新抓英文9。止中文p1/总11，不扩未来正文或浏览器。

## 3. Kimi changelog 差额

`https://platform.kimi.com/blog/posts/changelog` 实际200/14815 bytes，15秒/retry0，原件 [SUP_kimi_changelog.raw](./SUP_kimi_changelog.raw)。实际读正文目标邻接：发布日期头2025-11-07不是所有条目事件日；正文 Nov6→Oct27→区间0916–1015→Sep5。Oct27为CLI/快速开始文档与促销结束等，区间含测评信息/cache列表下线；没有将该区间补出Oct20事件。不扩组织历史或全部文档，旧GitHub失败保留，不重旧失败请求。

## 4. Google/Atlas 与本日旧来源有效层

Google本篇原Oct20方法发布按 [ALBUM](./SUP_GOOGLE_ALBUM_20261015.md) 已 actual 校准，后续评分/owner/PRE独立；Atlas官网Oct21 date-only排对应发布不属本轮新增Oct20，原RSS午夜字段仍只feed，不重追秒。正确pubs旧timeout/必要历史缺段保持，不把Blog替代pubs；Meta原有限失败/辅助query不命中不当无事件，不重失败。

作者本轮重新解析本日旧RSS原件1245条的全部pubDate，按新增Oct20完整BJT（UTC `[2025-10-19T16:00Z,2025-10-20T16:00Z)`）过滤得0条；这是真实feed字段局部0，不是全Research无事件。与原09点窗口Atlas1条两个不同filter保留，不改原件/旧窗口，不把feed日当first-public。Google相册5分/真实Ch24一段及自身note经root§3–5实际Source/date/PRE/POST及行政读回已全闭合、窄锁已释放，无该单项待办，不重写正文。

本日原非作者实际层可精确复用：OpenAI RSS1245条日期/原Atlas core；Anthropic publishedOn目标Oct14/29邻接；DeepSeek十Research/OCR题摘；Kimi原Blog邻接；Zai原p2累计18至Dec7/hasMorefalse；Seed正确US两类2025页0各18/total94与45/next20/has_moretrue且目标邻接跨至Oct9/Sep9；ERNIE末页6条Oct16/Nov7邻接；MiMo8Paper/15Blog与11370v1必要core；MiniMax英12/中文Oct27至Jan15/Agent独立2026-05-13原md。这些是本日旧证的有限目录或必要core，不是本轮新抓字段、不授2025完整历史/全年完读。Seed量子/Google恒星科学应用原关闭保持，不重原文；各入口首查及失败角色详原FETCH/FINAL，不删改。

本轮新Qwen/中文Hunyuan/Kimi changelog有限字段包已 prepared，可由root立即独核。其余本日旧有效层只按原角色复用，历史缺段明确不授Coverage/Evidence或无遗漏；本包不授整日DAY。
