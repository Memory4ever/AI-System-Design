# 2025-11-20 有限来源与恢复边界

作者Dalton；2026-10-04T17:51:20+08:00。BJT窗口 `[2025-11-19T09:00:00+08:00,2025-11-20T09:00:00+08:00)`。本日独立执行，不继承19或12月Coverage；未扫Weekly或其他月份研究队列。旧网页中的其他年月标题仅用于定位边界，不转题摘/全文待办。

## 原入口与停止

| ID | 实际入口、query/分页及停止 | 当前能证明 / 不能证明 |
| --- | --- | --- |
| SRC-OPENAI | Research当前入口及Nov19定日官网有限搜索；官方RSS原始XML按本窗UTC过滤4项，2个Codex入口00Z单独核身份，核心见RSS包 | 1拟入选external-testing、2框架/产品排除、1暂缓科学路线关闭。当前feed不是历史Research索引完整快照；未列/删除项隔离 |
| SRC-ANTHROPIC | 本日原Research GET200，Flight解码publicationList.posts=171，只筛目标区间日期/身份；Nov21→Nov12相邻界及其他Nov元数据，无本窗条目。先前官方域Nov19有限查询首页仅返回Nov18合作 | 当前原目录目标段已恢复，不需读171份题摘；不认证历史删除、未列内容或原版本。原HTML/receipt本日保存 |
| SRC-GOOGLE-AI | DeepMind当前页、Research pubs过滤入口；2025官方blog第1页12条Dec18→Nov12且共9页，停第1页；S2ST原核心实际读。两次原HTMLcurl连接超时，CUA首查39秒超时；两轮精确timestamp查询首页未恢复时刻 | S2ST潜在准入但Nov19自然日不能归窗。当前pubs没有目标历史切片，不拿博客替代全部publications。精确重开条件为目标列表/官方事件时刻 |
| SRC-META-AI | Research动态0行；publications page4到SAM3三篇Nov19、SoCE Nov18、Nov11后混旧年，blog page2非单调，停4/2；相关题摘/core实际读，两次直抓连接超时、精确日期查询未得 | SAM3/SAM3D Objects/Body潜在保留，非严格排序不授历史全覆盖；同URL SAM3.1 Mar2026更新隔离，不能当原SAM3收益 |
| SRC-QWEN | 旧站显示Sep23及更早；实际Research链接qwen.ai/research 0行，原HTML200动态壳。本次CUA createBrowserTab超时83.9458秒并reset，未返回tab/DOM | [浏览器停点](QWEN_BROWSER_STOP.md)不是看见零条目。需要本窗官方历史列表/原响应，不反复空路径、不授Coverage |
| SRC-DEEPSEEK | home More→news页，实际研究可见Nov27→Nov1，动态Dec1→Sep29，停可见边界；查看全部为button，无web可点URL，未操作 | 只支持可见目标区间的有限检查，不声称隐藏/删除条目无遗漏；不扩大GitHub全组织扫描 |
| SRC-MOONSHOT | Kimi Blog原页及changelog实际Nov7/Nov6→Oct27，停当前可见列表；GitHub仅身份备用未扩组织 | 只支持官方可见列表目标边界，不对组织全部artifact作零事件结论 |
| SRC-TENCENT-HUNYUAN | Research原入口0行/HTML6893字节，CUA50秒超时reset；user提供身份线索后实际POST publicList pageNum1/pageSize20/renderType0，total9/list9，只有2026且renderType1/2 | API成功不等于2025 Research恢复；停page1，未构造未知endpoint/参数遍历。最小请求本窗Research历史目录/官方原响应 |
| SRC-ZAI | Research原页15条More；本日下载前端page.js核router page+1及URLSearchParams，真实GET?page=2累计18、hasMore=false、nextPage3，最早Dec7且非单调，停第2页；release notes Dec8→Sep30另读 | 页面分页已耗尽，11月历史缺段仍保留；release notes不能替代Research，不继续不存在的第3页 |
| SRC-BYTEDANCE-SEED | 实际GET get_article_list_v2，header x-tt-locale:US，publish_year2025/count20/order_desc=true，type1/2各page_token0→20。pinned单列，regular分别Oct22/Oct23以下，20页已更早，停止20 | type1是论文total94，type2是Blog total45；raw文件名papers(type2)/blogs(type1)反置不改变实际响应身份。has_more仍true/next40，停止理由是已越目标边界，不是假称分页耗尽 |
| SRC-BAIDU-ERNIE | 官方中文blog第1页10条至Nov21，实际第2页6条Nov11→Jun30，页码2/2，停2 | 当前两页的目标可见边界已检查；未认证删除项或全组织无遗漏 |
| SRC-XIAOMI-MIMO | Paper8条实际Jan8,2026→Oct21,2025；Blog15标题无日期、有More；停止有限目录及定日恢复 | Paper可见边界能检查；Blog有日期的目标More段未恢复，不能由Paper目录替代。最小请求Blog目标日期列表 |
| SRC-MINIMAX | EN12/CN13当前模型博客Dec23→Oct27（CN更早Jan15），停各可见列表；独立Agent tech入口本日HTML/Markdown/llms.txt实际核，techblog当前只列May13,2026一项 | 模型博客不替代Agent Tech历史；2025目标techblog目录/快照保留。llms站内上游相对链接属于原源，不改成本地文件 |
| SRC-ARXIV | 四窄主题query及learning/multimodal收窄，focus7标题；官方CL月表只锚定skip800和目标skip650/700，各show50，停750。不扩全月1527/all，不把宽107/45/44变全题摘队列 | 两批30个exact-v1完整题摘实际读：28潜在/2关闭请求；current仅30身份标题/updated/comments轻检。候选公开时间仍需原公告/可靠界，Submitted不替代public；没有全学科召回断言 |

原始web查询/实际页标在 `WEB_FIRST_*`、`WEB_META_RELEASES_GOOGLE_LIST.json`、`WEB_DAILY_05_08.json`、`WEB_DAILY_09_13.json`、`WEB_DAILY_BOUNDARIES.json`、`WEB_DAILY_RECOVERY.json`，完整结果与停止位置留存。curl每项有同名receipt，记录请求、HTTP、字节、起止时间；Google/Meta失败只有receipt，不能称下载到原HTML。Hunyuan/Seed请求体及header在各receipt原值中。不新增独立账本要求，正式报告自包含关键范围。

## arXiv实际查询与题摘范围

system为DC/AR/OS/PF/PL+LLM或language model+GPU/memory/parallel，Submitted Nov17–19，start0/max25，13标题读完；learning为CL/LG+language model/Transformer+optimization/generalization/learning theory/representation，Nov18–19，总107仅首25标题；multimodal为CV/RO+foundation/vision-language/world model+training/architecture/reasoning，Nov18–19，总45首25标题；agent为AI/CL/IR/MA+language model+tool calling/agent memory/retrieval augmented/multi-agent，Nov18–19，22标题读完。日期过滤只用于发现，不认证落窗。

learning改Nov18+language model+optimization/generalization/learning theory，总44首25；multimodal同主题改Nov18为22；最后learning focus改LLM/language model+pre-training/generalization bound/RL theory/optimization stability，Nov18–19，7标题后结束。全部真实query/sort/start/max在XML同名receipt，未翻后续宽页。完整exact-v1题摘与逐项理由在[首批14](ARXIV_FIRST_CALIBRATION.md)及[尾部16](NARROW_TAIL_CALIBRATION.md)，不是30份已证实结论。

current轻检没有明示withdrawn；Chronology v2 explicit corrected footnote已核v1/v2精确HTML，只有仓库脚注/链接所见差异能采用，不断言全稿未变。15005数学反侧涉及score常数项和相似变换熵不变，已核必要公式，待root独立确认；不是无实验理论统一排除。其他晚版不回填v1，版本号变化不授重要修订。

## 有限日期恢复与精确重开

Google/Meta自然日timestamp两轮官方域有限搜索未恢复；Physical Intelligence原blog发现后web受阻、curl429反机器人，二次官方域搜索只有原题和二手日期，二手Nov17不当官方public。FailSafe原abs只列Submitted，pi-star current只列v1/v2提交史；本日实际读[arXiv availability](WEB_OFFICIAL_DATE_BOUNDARY.json) L170–189，确认moderation可延后、公告与提交不同、常规schedule不足以补造本窗时刻。当前帮助的2026 holiday不当2025日历证明。

同一原帮助L175–176明确编号月份对应首次arXiv公告且不可backdate：这为 `2602.00003` 的arXiv事件提供2026年2月下界，不把Nov18,2025的API v1字段当Nov公告。作者可能更早在其他原源公开正文仍需具名原稿证据；请求root定点核这项日期身份推断，不将它确定为20候选，也不由编号单独推断所有公开渠道。其他Nov编号仍无法给本窗精确下界。

潜在贡献不因日期含糊改判消失。对各exact-v1最小请求是官方实际公告/作者首公开快照，或原始首次可访问上下界完全落窗；材料到达只重开对应身份/事件。API published/updated、论文编号和常规20ET均不充当精确public时刻；跨09的上界不反证窗外。不为日期恢复逐一展开30份实验或owner。目录缺段各最小请求见上表，均不用于正面Coverage/Evidence、Books或无遗漏。

本日未发现需扩扫注册按需来源的新会议批次/协议release触发；pi.website是具名论文必要表外原源，不是整站Daily扫描。普通作者来源收口已到上述有限停止；准入校准、必要受影响单项复核及最终日级仍待root，不能自授完成。
