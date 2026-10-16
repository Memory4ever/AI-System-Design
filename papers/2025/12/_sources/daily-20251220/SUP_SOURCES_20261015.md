# Dec20 新自然日有限来源差额

## 1. Qwen本日真实目录响应

2026-10-15约17:44–17:45BJT，作者本日直接GET（每次新X-Request-Id）：

- `https://qwen.ai/api/page_config?code=research.research-list&language=en`，HTTP200，根array60。
- `https://qwen.ai/api/v2/article/retrieval?type=qwen_ai&language=en-US`，HTTP200，data.articles40。

只向作者显示白名单title/id/path/date/language及数组长度，不读后日body/content/introduction。两个响应均不是别日报存成功；路径技术线索不等继承来源结果。本次实际返回无Next字段，非假定网站全历史完备。

当前本窗唯一具名记录：page_config id=qwen-image-layered，title=Qwen-Image-Layered: Layered Decomposition for Inherent Editablity，date=2025-12-19T05:08:30.000Z；article id=14d6fc47-b33b-43df-bc60-e5c9e1edaf6a，path=qwen-image-layered，language=en-US，extra.date=2025-12-19T13:08:30+08:00。相邻元数据：Omni-Flash路径qwen3-omni-flash-20251201日期Dec9BJT；后为TTS-VC/VoiceDesign Dec23BJT与Image-Edit2511 Dec23BJT，未打开后日正文。只按官方原日期采用Dec19，不追秒。

[具名Blog](https://qwen.ai/blog?id=qwen-image-layered)本次0可读行，必要技术证据改由作者所链exact-v1与官方仓库取得，不冒Blog正文可读；[官方仓库](https://github.com/QwenLM/Qwen-Image-Layered)News明确Dec19模型及权重release、Dec18论文声明及Dec22Demo分别记事件。当前README后加vLLM-Omni不倒签Dec19能力。Newton§4已实际原仓库准入/日期与Ch24邻接；作者本次实际读Introduction/News/Note/QuickStart/Deploy/Showcase，具体必要方法与采用另见SUP_QWEN_SOURCE。

## 2. MiniMax独立Agent入口

本日实际打开 `https://agent.minimax.io/docs/techblog` 全部66行及其明确链接 `https://agent.minimax.io/docs/llms.txt` 全部54行。TechBlog只有三条具名2026-10-08、09-22、09-19，底部无分页；索引列对应三个techblog path，与目标2025-12-19无条目。仅读入口/索引题名、日期与导航，不读2026正文、不用其方法支撑本日。旧模型Blog12条Dec23→Oct27有效切片仍独立复用，不能代Agent。

这完成本日可执行的独立Agent有限入口，不能证明2025入口当时不存在或全历史零事件。缺口精确为2025-12-19 Agent历史目录/具名事件；官方历史列表或具名原始Dec19事件到达才定点重开，不反复当前入口，不扩扫后日、不UI绕过。

## 3. 其它原有效层与差额边界

本日SOURCE_STOPS实际14源固定邻接/有界失败按各自范围复用，不冒所有来源对新自然日都零事件。Anthropic两Dec19官方date-only现已通过Newton3/root实际读回，本表不再称其缺offset或日精度受阻；新Source/PRE另包。Scope2旧完整row/公开字段/6分与真实整合冻结不重。MetaDec18四watermark同core/论文别事件仅定点去重；无明确Dec19新release不搬日。Seed、Hunyuan、GooglePublications等必要历史缺段按原精确边界保留，不能由目录未见项声明无遗漏。

OpenAI旧reader实际200/1243RSS、相邻Dec18→Dec22字段为同日原有效层；旧[Dec19 01Z,Dec20 01Z)0不能自动变新[Dec18 16Z,Dec19 16Z)0。仅已实际见到的Dec18条目00/11/12GMT均在新窗前，Dec22在后；仍缺Research历史/全渠道完整上下界，不新启RSS/legacy、不从旧小时窗零条外推。其它具体目录与artifactcommit身份按原停止点，不为换自然日重Methods/代码或全pool。

Google自然日早段按Newton12实际精确去重层修明：T5Gemma2同一release原published字段Dec18 18:30UTC=Dec19 02:30BJT，处于本次新增自然日，但前一已有日报完整候选row/对应§4的6分/Ch18真实整合及非writerPOST均有效；Newton只为本项身份实际读该两段，作者复用此窄层，不搬前日报冻结日期/重复候选、评分或T5书注，也不把paper first自动去重。Genesis旧Dec18 19UTC=Dec19 03BJT同属新日早段，仍按原科学应用贡献关闭，不以旧小时窗外作为本轮排除理由，不重科学正文。GooglePublications历史缺段并未因此恢复。

以上只是来源有限层，非日级完成；arXiv自然日公开归属/标题受影响项/current差额和六节仍继续。

## 4. repo自然日差额：实际原响应与精确去重

2026-10-15约17:56–17:57BJT。旧GITHUB_WINDOW只查询Dec19 01Z至Dec20 01Z，不能替代新自然日Dec18 16Z至Dec19 16Z。作者本次逐仓实际HTTP200读取同七repo main commits route，使用`?since=2025-12-18T00%3A00%3A00Z&until=2025-12-19T23%3A59%3A59Z`两天元数据缓冲，解析官方embedded JSON的commitsRefRoute；逐实际committedDate再过滤新自然日，原filters/hasNextPage均实际看，不相信查询参数按秒生效。先用Video1.5九小时差额route，实际返回同Dec19三项，表明不能按until字符串假定小时精度，故使用有界两日缓冲后逐字段排除。

| repo | 原响应/停止 | 新自然日committer线索 |
| --- | --- | --- |
| QwenLM/Qwen3 | groups0，hasNextPage=false | 0，仅该route |
| deepseek-ai/DeepSeek-V3 | groups0，hasNextPage=false | 0，仅该route |
| MoonshotAI/Kimi-K2 | groups0，hasNextPage=false | 0，仅该route |
| Tencent/llm.hunyuan.T1 | groups0，hasNextPage=false | 0，仅该route |
| Tencent-Hunyuan/HunyuanVideo-1.5 | 原3项，endCursor60783e704160023913bee78f0b47036d393d4dfa 2，无Next | 40d5b27/Dec19 18:40:31BJT、85c5343/15:25:27、36916f8/12:14:57；本日旧有效三patch原身份不变 |
| Tencent-Hunyuan/HY-WorldPlay | 原10项，endCursor1588e1336e842b03b0a7860c654ebd7c46bb065e 9，无Next | 8项：c914f2a/20:04:43、76f5eaf/16:55:59、86cfe35/16:20:20、a8f09f2/16:05:32、86988c0/02:23:09、8b0b8b9/01:44:59、b26dfb3/01:44:45、d290dee/01:42:45；日期均Dec19BJT |
| XiaomiMiMo/MiMo-V2-Flash | groups0，hasNextPage=false | 0，仅该route |

WorldPlay另两条a25c55d/Dec18 18:13:36BJT、b52fe0a/18:10:00BJT在新窗前，不搬日。新覆盖四个凌晨commit并非新方法待全部二读：实际GET `https://github.com/Tencent-Hunyuan/HY-WorldPlay/commit/a8f09f2fab5b3cfc7b1cac6783312e586d6c596a.patch` HTTP200/48117bytes，只抽取并实际读六个From/Date/Subject/diff文件名确认身份，顺序b52fe0a、a25c55d、d290dee、b26dfb3、8b0b8b9、86988c0，与旧本日SOURCE_STOPS已实际完整展开六patch的精确a8身份相同。复用其有效代码层，不重全文/双版；旧文字把六项统称“Dec18”不准确，本轮只纠正前两Dec18、后四Dec19BJT，merge自身时间不成为新的机制事件。

所有实际返回pushedDate=null。committer/author仍不证明artifact何时公开，Video1.5局部状态/兼容潜力不删，WorldPlay有效同代码/README去重不增加家族；无运行/速度/异常恢复保证。该有限差额未扩repo、未扫月历史，保存后无运行中shell会话。
