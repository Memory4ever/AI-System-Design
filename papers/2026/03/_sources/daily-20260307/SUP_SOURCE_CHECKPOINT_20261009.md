# 2026-03-07 增量来源停止点

本次只补2026-03-06 BJT自然日遗漏。原窗口、19行候选日期/评分、连续§4冻结于[baseline](SUP_BASELINE_20261009.md)，旧Source/PRE/POST有效复用；未加载他日材料或改他日合同。14个Daily来源均实际有界检查，当前目录不是历史不可变快照，空页/日期隔离不签正面Coverage。抓取时间与URL、原始bytes/error在 [official](SUP_FETCH_official.json)、[arxiv](SUP_FETCH_arxiv.json)、[topics](SUP_FETCH_topics.json)、[recover](SUP_FETCH_recover.json)、[cards](SUP_FETCH_cards.json)。raw与同名txt保留本目录，Google/Descript/EVM等官方浏览输出见[primary web](SUP_WEB_PRIMARY_20261009.json)。

| source | 本轮实际有限入口/目标段 | 停点/具体边界 |
| --- | --- | --- |
| SRC-OPENAI | news/rss.xml实际筛Mar06～07：Codex Security、Descript、Balyasny；Descript官方完整核心；旧Codex/Balyasny处置复用 | Descript正式页Mar6，准入2+1+2=5；RSS整齐00GMT不赋精确时刻，但自然日无需。Balyasny成熟金融research pipeline旧EX不重读整队 |
| SRC-ANTHROPIC | research与engineering当前有限列表，Mar05→Mar06→Mar13邻近；BrowseComp官方完整核心、两官方PDF p2纠错 | Firefox旧证据复用。BrowseComp+两卡同家族3+2+3=8；无全模型/全Engineering队列，未以dated修改日代模型首发 |
| SRC-GOOGLE-AI | Research March archive page1实际12条Mar31→Mar06 WAXAL；DeepMind RSS100 record仅目标Mar03→Mar09邻段；限定官方Mar6检索含SpeciesNet | Googlecurl超时，用官方浏览；页1底页2 href为javascript:void(0)，有界?page=2超时，未恢复历史pubs/页2；DeepMind raw为gzip，本次实际解压读pubDate邻段，无Mar6record；WAXAL旧EX复用，SpeciesNet wildlife应用标题范围外，不当新模型形成 |
| SRC-META-AI | research入口curl SSL失败，官方浏览0行；site:ai.meta.com March6 research/model/training有界补检无命中 | 空页/无命中非零事件，历史Research必要段外部隔离 |
| SRC-QWEN | 新blog shell后真实retrieval API type=qwen_ai/language=en-US一次40条；按extra.date排序只读目标相邻Feb16 Qwen3.5→Mar19 MaxPreview | 当前目录目标段无Mar6，不扩PR/全机构。日期字段在extra，不用顶层未定义time |
| SRC-DEEPSEEK | 正确/en/news/当前Research10项Feb25→Jun24与News首5项Dec01→Apr24；先前/en/updates/404不当目录证据 | ViewAll停止，隐藏News/API历史未恢复，不签全机构 |
| SRC-MOONSHOT | 新kimi.com/en/blog/当前19研究项至Mooncake，Feb09→Apr20相邻 | 可见段无Mar6，不以旧platform替代新入口，不恢复删除历史 |
| SRC-TENCENT-HUNYUAN | accept-language:zh，publicList POST pageNum1/pageSize20/renderType0；11/11真实条目 | display Feb13→Apr23，无March；publicAt/published/display各保留身份，未互替历史首发 |
| SRC-ZAI | 当前research首可见15项，Aug26→Dec09，Feb21→Mar15相邻 | 查看更多停止，只签可见段，不扩整个机构 |
| SRC-BYTEDANCE-SEED | get_article_list_v2 article_type1/publish_year2026/page_token20/count100/order_descfalse；默认无locale14条BJT Feb27→Mar26；追加x-tt-locale:US18条 | 默认目标相邻BJT Mar01→Mar12；US多含目录Mar02两条，两header均无Mar06。[US raw](SUP_SEED_US.raw)/[回执](SUP_FETCH_seedlocale.json)；has_more=true/next_token40不代表遍历全年，过目标未来项即停；未恢复所有Blog/Publication |
| SRC-BAIDU-ERNIE | Blog可见Apr15→Feb06，2页旧页止2025；当前目标相邻段 | 不扩文心全机构/全部榜单 |
| SRC-XIAOMI-MIMO | 当前官网Paper/Blog标题有限段；日域名补检一次0命中 | Paper Mar13→Feb03旧有效证据复用，Blog15无日期/More不展；未用搜索0命中签无发布 |
| SRC-MINIMAX | en/CN blog当前可见至2025/10，Mar18→Feb12相邻（旧页另Feb14条） | 当前可见目标段无Mar6，不扩全部Tech Blog |
| SRC-ARXIV | 四个title主线API+官方cs月页目标100标题（skip2400/show100，04582～04779），101 actual-read exact-v1题摘 | 原93与[同MODEL分页8](SUP_MODEL_PAGINATION_20261009.md)共同裁决；71P+18A及1W外部日期/版本隔离，10EX/1OUT不评分。month ID/Submitted/current updated不作pub date，不能称全学科召回 |

## arXiv查询与停止

四条使用submittedDate:[202603041900 TO202603051900]、start0/max_results100/sortBy=submittedDate/sortOrder=ascending，只作有限发现窗口，不作为公开窗口：

- MODEL：ti:"language model" OR ti:transformer OR ti:MoE OR ti:alignment OR ti:reasoning OR ti:optimization；total118，start0/max100后同query start100/max18实际取得完整余18标题，7明确范围外/3重复/8相关或含糊再读exact-v1；raw SUP_TOPIC_MODEL.raw/SUP_TOPIC_MODEL_P2.raw，回执SUP_FETCH_modelpage2.json。已知可执行分页不作终态故障。
- SYSTEM：ti:LLM OR ti:inference OR ti:GPU OR ti:kernel OR ti:training OR ti:communication，AND cats cs.DC/cs.AR/cs.PL/cs.OS/cs.PF/cs.LG；total22。raw SUP_TOPIC_SYSTEM.raw。
- MULTI：ti:multimodal OR ti:"world model" OR ti:VLA OR ti:"vision language" OR ti:diffusion OR ti:representation；total60。raw SUP_TOPIC_MULTI.raw。
- AGENT：ti:agent OR ti:memory OR ti:retrieval OR ti:tool OR ti:planning；total70。raw SUP_TOPIC_AGENT.raw。

以上不是全部返回均准入；明确医疗/科学应用/硬件器件等题目只作标题范围检查；主线相关项完整v1题摘读101（93原包+8余页），非全部query家族完整AB。100条相关标题补检只作有限发现，未将全部月库存变AB/fulltext任务。API返回current revision，因此04678专门重读v1纠正，不回填v3机制。初步SUP_API_*宽query（datewhole-day，各max100）与SUP_LIST_CS skip2000、DC月页只作路由诊断，发现范围过宽即退役，没有拿它们组成新完整队列/覆盖分母。

日期恢复有界官方query：site:arxiv.org "Fri, 6 Mar 2026" (04514/04549/04715/04918)、site:arxiv.org "6 March 2026" (04716/04956/05500)、site:arxiv.org "Fri, 6 Mar 2026" "new submissions"；本轮具名再核04514/04549/04716/04918与05087/05193/05500均无announcement record。不是重试已知失败advanced日期查询。LPWM作者链接OpenReview forum与api2一次challenge/error，保留[浏览原始](SUP_LPWM_WEB_20261009.json)/SUP_OPENREVIEW_LPWM.raw/SUP_LPWM_DATE.raw；搜索Jan26摘要不能代公告。EVMbench实际official Feb18，OUT不计3月新家族。其余P/A精确隔离，不评分/不Books/不fulltext补日期。

普通旧事件不重跑，旧AGF与CSV/DBC/HyperMVP终态理由不变。本次新增两官方的必要证据已读；root已窄写Ch66/Ch24各两段与自身note，作者非写入者实际源→正文完整邻接/末注[POST](SUP_BOOKS_POST_20261009.md)通过。root非报告作者已实际完成本次增量六部分DAY复核：有限query/stop、两官方core/card p2、89潜力独立准入/EX与版本信号、Books及非写入者POST、外部隔离/冻结/V3/限定检查通过，无未修点。普通作者待办0，报告状态完成；不授全Coverage/Evidence或无遗漏。此日ownership已交还root，不领取下一日。

新增状态核：04676 v2 May07明确撤回，原因是实验/analysis需实质修订，W隔离不采用；05094 v2 Mar27因暂不拟公开传播撤回、v3 May13当前非withdraw，不能误认v1/全family撤回。只核abs状态，不扩全文或原19。独立93 AB核验窄修05120/05185 P→A，04532 stable support/ranking、04678 structure reward/no explicit RM+supplement DPO、04716 M/M/1 TTFT/TPOT资源长度关系；未扩题摘无支持机制。
