# Jan28 补充窗口的有限来源停点

补充窗口2026-01-27北京自然日；本轮请求实际时间2026-10-08T07:05～07:06+08，各JSON保存原URL/checked/raw。这里只汇总已发生的检查，不重新扫描，不以旧Oct4/09:00窗口SOURCE_STOPS代本轮。原旧记录保留。14每日源，没有触发每周来源。

| 来源 | 本轮入口与停止 | 结果与可用权限 | 必要外部保留 |
| --- | --- | --- | --- |
| SRC-OPENAI | news RSS空响应/403；复用原Introducing Prism核心说明与贡献关闭 | 受阻；原关闭有效，不支持无遗漏 | 当窗Research dated目录/具体漏项原发布 |
| SRC-ANTHROPIC | Research本轮空响应/403；原Jan27窄query只商业合作，复用关闭 | 受阻；不把商业发布当研究增量 | 当窗Research dated目录 |
| SRC-GOOGLE-AI | Research Jan2026月页本轮原响应6054字符；本次可见Jan28～Jan12（NeuralGCM）标题段与两篇原blog判断复用；DeepMind旧discover/blog空响应，当前列表不覆盖历史 | 受阻仅DeepMind历史覆盖；Google Research本月段已检查，ATLAS/scaling旧研究无新事件 | DeepMind当窗dated目录/具体原发布，不重扫Google有效段 |
| SRC-META-AI | Research本轮57字符interstitial | 受阻，壳不授零命中 | 当窗dated研究目录 |
| SRC-QWEN | qwen.ai/blog本轮4字符壳；原旧github入口最新2025-09-23不代Jan2026 | 受阻 | 当窗dated Blog/Research目录或具体原发布 |
| SRC-DEEPSEEK | /en/news/本轮可见5条精选news+10条Research Index；Jan28 OCR2/Jan12 Engram/Dec31 mHC相邻 | 受阻仅历史完整性；OCR2经Jan27原repo首稿日期/贡献核验恢复为新增61之一 | 精选之外当窗原发布/dated目录；OCR2旧hold已解除，不用Jan28news倒填 |
| SRC-MOONSHOT | platform旧blog1178字符；本日Kimi官方Jan27日精度/core原说明已root独核 | 受阻仅历史完整性；K2.5本轮calendar date已准入，最小Books覆盖通过，不再列时分秒hold | 当窗历史完整dated目录；不请求已采用K2.5精确时刻 |
| SRC-TENCENT-HUNYUAN | Research4字符脚本壳；本轮首查隐藏浏览器30秒超时/重置，原70秒/35秒失败仅旧记录 | 受阻，未读“全部”列表，不授零命中 | 能实际读取当窗dated all列表/相关原发布 |
| SRC-ZAI | Research15条时间排序，从Aug26读到Dec9，Feb2与Jan19夹Jan27，更多从更旧开始 | 已检查该可见时间排序段，无当窗条目 | 无必要正文缺口；不宣称全站无遗漏 |
| SRC-BYTEDANCE-SEED | API type1 year2026/orderasc/page0/count30实际20/total82、next20；按北京日期Jan20首、Jan22、Jan27 ID1378/1612、随后Jan29 ID1339/1611已跨窗停止；type2实际20/total23首Feb12 ID1939越窗，next20不扩扫 | 已检查窗口相关可见升序段；Jan27 Visual Generation/Keel官方完整题摘/root必要采用有效 | 不把82库存扩为队列；本日高层AB权限不授Jan28方法、SeedVisual必要机制未披露已Only |
| SRC-BAIDU-ERNIE | 本轮第1页10条，Jan29→Jan15→Jan8，尾Nov21；原下一页2025年停止复用 | 已检查可见排序段，未见Jan27 | 无必要正文缺口；不授全机构召回 |
| SRC-XIAOMI-MIMO | 当前首页10129字符，无完整Paper/Blog日期；原Jan2026窄query未恢复 | 受阻，当前产品页不是历史覆盖 | 当窗dated研究目录/具体漏项 |
| SRC-MINIMAX | 本轮blog日期可见12条，Jan27 M2-her被Feb12/Dec23夹；原核心说明已独核 | 已检查可见排序段；M2-her calendar日已准入并Only，不再列精确时间hold | vendor未披露因果/总预算不当机制证据；不授全站遗漏保证 |
| SRC-ARXIV | 四原API submittedJan26～27/orderasc/start0/max150：model实际150/total231已读到Jan27T08:49Z，越过Jan26截止；multi53/53、agent103/103、system49/49均读完返回；截止后不是本日候选。加原377窄registration相关标题有界补检、68 exact-v1完整相关题摘、80 identity/date恢复；模型未取第151页 | 已检查约定四主题与相关标题有限补检；冻结56新arxiv候选，跨分类家族去重；Submitted只发现，日期由原exact身份、公告下界+已deposit上界联合 | 旧10首次公开日仍必要缺口（见下）；不称全部分类召回、68全文审阅、377贡献或时间字段单独认定 |

## 旧10日期保留的本轮有界恢复

只核已有10个exact-v1官方AB identity与本轮DataCite精确arxiv身份，不抓全年会议/旧revision/全文。16986、16987、17006、17037、17042、17050、17063、17082、17086、17087均有本轮精确DOI/arxiv.content身份与Jan27 created上界03:39:25～03:41:43Z，但v1 Submitted分别Jan5/Jan5/Jan14/Jan20/Jan20/Jan21/Jan22/Jan23/Jan23/Jan23，最早公告下界跨Jan27自然日；Available只有月精度，Updated/OAI datestamp不等首次公开。新metadata未补必要下界，不能因created全落Jan27就恢复为当窗候选。

当前终态隔离：不正面采用、不进入新增61、不以日期不确定缩减已准入60；原64与原窗口不搬移。精确请求仍每ID仅一次：官方首次公开day映射、当日announcement列表，或不能回溯改变的首公开正文日志，足以判定北京日是否Jan27。到达只重开该ID的日期/必要贡献层，不重跑一月。v2后来提交、修改字段与同稿title均不能替v1首公开。

旧native holds按本次自然日口径分别更新：K2.5/M2-her/Keel已由Jan27官方日精度与身份通过，不追时分秒；Seed Visual同日高层事实已审但方法未披露Only。OCR2已定点恢复Jan27原repo发布/公开访问与精确首稿，旧hold解除；完整题摘、必要Source/Ch23单段PRE与实际POST通过，新增61=原60+此新恢复1，不再请求首公开时刻。
