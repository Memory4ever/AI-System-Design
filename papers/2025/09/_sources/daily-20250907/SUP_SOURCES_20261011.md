# Sep07 当前来源切片与实际停止

只补 Sep06 BJT 自然日；记录当前实际获取与读取，不从旧完成标签、旧失败或别人日期继承覆盖。所有 `SUP_*.request.json` 保存原 URL/执行时间/status/bytes/SHA，对应 `.raw` 保留原件。动态数组按 JSON/HTMLParser 解析，非浏览器实际可视操作。当前目录不是历史冻结目录；有限检查不等互联网无遗漏。原旧窗口与§4由 baseline 冻结。

## 十四每日源

| ID | 当前真实入口/读取/停止（原件简称省略SUP与后缀） | 当前边界 |
| --- | --- | --- |
| SRC-OPENAI | `openai` official news RSS，1287 items以Sep06 BJT对应UTC区间选择空；前Sep05 10GMT hallucinations，后Sep08 fund。只读必要日期/title，不读1287正文。 | RSS现存集合，不证明被移除历史研究不存在；Why Language Models Hallucinate作为Sep05已公开线索，不能挪入Sep06。 |
| SRC-ANTHROPIC | `anthropic` research RSC JSON真实posts174（不是引用字符串长度47），publishedOn前Sep05 biorisk/后Sep15 economic index，目标日选择空。 | 当前有限列表，无全部历史保证。 |
| SRC-GOOGLE-AI | Research Blog `google-month` 12日期卡Sep30→Sep11，`google-month-p2`1卡Sep09，实际2of2停止。DeepMind `deepmind-history`仅直接page5有24卡Nov→July，必要六Sep文章`deepmind-sep0..5`，原published_time/原日期实际25/22/18/17/12/04，止跨本窗两侧；不请求page1–4全年正文。Research publications实际JS说明year参数不生效，改`category=2025`，checked确认：`gpub-2025-llm`15+4至page2/2，agent15+15+7至3/3，infer11无分页，multi14无分页；限定4主题仅year粒度，标题查漏不把81次出现/680年库存读成题摘队列。 | Blog/DeepMind可见历史段无Sep06卡，不授曾删除项不存在；publication目录缺日粒度，不能认作Sep06论文0。错误year参数页保留但不用于覆盖。主题日期辅助搜索受限，非zero证明。 |
| SRC-META-AI | `meta` research→`meta-results` publication真实分页链接；直接定位`meta-page5/6`各12现代日期卡，page5 Nov18→Sep15，page6 Sep08→Sep02→Jun13，现存现代层跨Sep06止；另混入2017–2020旧卡，明确非全表严格排序。不请求整年。 | 实际有界现代层已读，当前目录非完整历史快照；不把旧混排或无regex日期当0。 |
| SRC-QWEN | `qwen`官方page_config60项，date/id/draft完整必要读取，Sep06选择空；前Aug18 17:30Z image-edit/draftfalse，后Sep08 06:38Z ASR/drafttrue。 | draft时间不等正式公开；当前60项有限，非全部论文历史。 |
| SRC-DEEPSEEK | `deepseek`正确API Docs updates，Date索引Sep29→Sep22→Aug21跨本窗，必要原段已实际独读复用。 | 不沿用旧错误www路径；只现存更新页，不授全研究无遗漏。 |
| SRC-MOONSHOT | `moonshot`Kimi Blog26日期卡完整必要索引，Sep16→Sep05夹窗；止现存页无next。 | 不扩GitHub全组织，没有无条件artifact覆盖。 |
| SRC-TENCENT-HUNYUAN | `hunyuan` shell→runtime JS/Blog JS/API module恢复真实origin `api.hunyuan.tencent.com/api/blog/publicList`，`hunyuan-list-api-en`9/total9、`hunyuan-list-zh-api`11/total11，POSTpage1/size1000/renderType0全部，Unix/date/title全部读，均2026Feb03→Sep22；实际返回即末。wronghost两404保留非覆盖依据。 | 实际动态内容已可解析，不借browser未执行标签；缺2025Sep目标历史层，需原快照/具名原发布，不当0研究。 |
| SRC-ZAI | `zai/zai-p2`官方research当前15→累计18，nextPage3/hasMorefalse实际末尾；原发表字段`createAt`不同于CMS`createdAt`，最旧createAt Dec07T16Z=Dec08BJT2025，不是createdAt2026。`zai-release`正确official notes200当前8日期sections到Sep30 GLM4.6止，无更早条目/分页。 | Research与当前release均未恢复本窗历史；旧Aug11跨下界不能沿用成当前页事实。错误打印整个2026CMS对象造成截断，不将该正文当本窗研究；随后仅18title/createAt字段重核。 |
| SRC-BYTEDANCE-SEED | `seed`运行时JS真实`get_article_list_v2`，US header/year2025/count20。type1 `seed-papers-0`18/total94、非置顶Oct22→Sep22→Sep02/01→Aug13→Jun26；token20实际20 Jun20→May20，跨下界止，不走全部94。type2 `seed-blog-0`18/total45，置顶Dec/Nov/Sep09与非置顶Aug21→Jun25，已跨下界止。Title取ArticleSubContentEn.Title/IsPinned真实字段。 | 修复旧稀疏payload，不再宣称80为空/全部papers受阻；只是当前有界历史切片，置顶日期不用于停止，更早库存不是队列。 |
| SRC-BAIDU-ERNIE | `ernie`首10卡及`ernie-p2`末6卡，原日期Sep12→Aug14→Jun30，page2无Next即止；必要标题/date已读。 | 现存Blog有限，无全部研究保证。 |
| SRC-XIAOMI-MIMO | `mimo`homepage8 Paper原title/date实际读：June29/March13/Feb03/Jan08 2026，Oct21/Sep19/Jun04/May12 2025。runtime+正确6159/8557数组15 Blog（slice8+7 More，无网络分页），`mimo-blog0..14`原件全部200。两iframe shell1/2恢复`mimo-blog1-body`Sep22,2026及2body Sep21,2026原time；其余原日期2026或2025Dec。 | 数组提取误带6jobs导致blog15..20失败，明确移出研究scope，不拿jobs当Blog条目/待审；不跟有现成日期的演示视频iframe。当前15/8集合不能代完整2025Sep历史。 |
| SRC-MINIMAX | `minimax-en`12卡、CN13卡原title/date全部读，EN最早Oct27,2025；CN另有Jan15,2025 MiniMax01，不能两集合均称最早Oct27。EN当前原件已真实恢复不再写“未执行”。Agent实际3 href，`mini-agent-workflow/eval/harness`各200，`mini-llms`末技术目录同3条。JSON-LD只有dateModified Oct08,2026，无datePublished。 | 不能把modified认first-public2026，更不能编造本窗无研究；需本窗历史目录/具名原发布。只核header/目录，不读3篇2026全文或全docs。 |
| SRC-ARXIV | 四主线submitted主题query start0/max150，30/19/16/17 total=returned，82appearances/59unique，stop首面；补旧Chart/RLA2身份精确v1共61。历史date list CL/CV各400；高级检索尾斜杠404已恢复真实form无斜杠200，正确paper_id/题名范围与month仍无匹配但普通HoPE检索有一条，不能以空响应定日。原form公告只year/month。月页只CL skip250/show25及CV skip350/show25，50标题查漏；相关/含糊27+独核漏查6+2分层项完整v1/current共35已读，止此两片，不扩月。 | 96完整题摘身份，74P/20EX/2窗外；submitted/announcement年月不是公开日。74项必要日证以实际能力限制精确隔离，见DateRequest，不授全部Evidence/本日0发布。 |

## 触发与有限恢复

- arXiv精确v1 HTML仅决定准入/安全/设计反侧必要段，已准备层见 `SUP_NARROW_20261011.md`；不是96篇全文队列。BRKGA/BAME HTML404→PDF200必要页恢复，未改共享scripts。
- InterAct DOI10.1145/3747871原publisher及abs变体均403，但Crossref出版方登记published-online Aug08/JATS完整AB匹配已实际读，非注册日；窗外身份去重。RLC2025官方单篇/PDF已恢复，只用于Offline/Online WorldModel必要先稿身份，不会议全站扫描；制稿日/演示日不冒充全文公开日。Why官方原URL直连403后web原页成功恢复Sep05与04664链接，见DateRequest，不授论文全文或本窗Books。
- 官方域Sep06主题辅助搜索实际执行但返回不匹配/第三方杂项，不用搜索空/宽结果授来源0；没有跟第三方digest扩论文池。
- 已从当前原件纠正目录计数、date字段和失效路径。未取得的目标历史层仅在有限原入口/必要恢复实际结束后可列精确保留项，不替代尚可继续读取的材料。
