# 14 每日来源：本窗独立恢复记录

本窗为 2025-07-03 09:00 ～ 2025-07-04 09:00 BJT。2026-10-07 独立阅读原始材料，不读取其他 Daily/Weekly 的判断。相同 URL 的缓存是机构原响应及请求凭据，不是其他日报的候选/评分。

缓存根：`../daily-20250701/`，每个 `.raw` 配同名 `.request.json`；抓取于 2026-10-06 15:46～16:12 UTC，HTTP 状态见请求凭据。Anthropic 使用 `../daily-20250721/anthropic.raw` 与 `.request.json`，抓取 2026-10-06T15:46:56Z，HTTP 200。本次本日抽取见 [institution-inspection.txt](./institution-inspection.txt)；Google/Meta 的本次 web 恢复见 [google-search.json](./google-search.json)。

| 来源 | 读取原始材料与窗口内判定 | 停止与边界 |
| --- | --- | --- |
| SRC-OPENAI | [RSS 原件](../daily-20250701/openai-rss.raw)及请求凭据，XML 1247 item；窗口筛选无匹配。邻接为 Jul1 10:00 GMT Genspark 与 Jul8 07:00 GMT AFT | RSS 中本窗记录检查结束；Research HTML 原请求403，不能保证网站其他事件全集 |
| SRC-ANTHROPIC | [Research 原件](../daily-20250721/anthropic.raw)内嵌 publishedOn 历史项；本窗无匹配。June27 06:51Z / 06:05Z 两项之后最近研究为 July15 00:00Z | 已核同一历史 payload 的本窗；不是仅按当前可见10行判断。存活历史目录不保证被删除事件恢复 |
| SRC-GOOGLE-AI | [Google Research 七月月页](https://research.google/blog/2025/07/)9条标题至Jul2声音定位，之后为Jul9 MedGemma；DeepMind真实Blog page5/6已恢复，Jul9 MedGemma至Jun26 Gemma3n跨窗；pubs 原请求超时 | 两个现存Blog本窗无条目；pubs目录仍受阻，不宣称整个Google无事件；[DAY恢复](./DAY-RECOVERY.md) |
| SRC-META-AI | 原 research 请求连接重置；本次 web 同URL无正文（0行） | 历史目录不可读；停止空响应，不作零事件 |
| SRC-QWEN | [Blog p1](../daily-20250701/qwen.raw)、[p2](../daily-20250701/qwen-page2.raw)，p2从Jul22跨至Jun27/26，均不落窗 | 到p2越过窗口下界，当前保留的日期有序Blog无当窗条目；不是全机构所有artifact |
| SRC-DEEPSEEK | [主页](../daily-20250701/deepseek.raw)、[官方更新](../daily-20250701/deepseek-updates.raw)；日期从Aug21至May28跨过本窗，无Jul3/4记录 | 公开更新目录本窗检查结束；主页非完整research历史目录，覆盖仅该官方更新 |
| SRC-MOONSHOT | [Blog](../daily-20250701/kimi.raw)历史日期Jul11下一个为May6，本窗无条目 | Blog保留列表跨过下界；不把之后Kimi-K2发布移入本窗 |
| SRC-TENCENT-HUNYUAN | [Research](../daily-20250701/hunyuan.raw)只有动态skeleton；[publicList](../daily-20250701/hunyuan-public-list.raw) pageNum=1/pageSize=100/renderType=0，totalNum=9，包含当前Blog而非2025全部Research论文 | 替代payload不能代表Research“全部”；root报告浏览器30秒初始化失败属协调者有限恢复，本作者未亲自浏览器核查；历史目录受阻 |
| SRC-ZAI | [Research](../daily-20250701/zai.raw)、[page2](../daily-20250701/zai-page2.raw) 可见/内嵌日期最低到2025年12月，未到七月 | ?page=2非已证实有效历史翻页；保留真实停点与缺失历史目录 |
| SRC-BYTEDANCE-SEED | Research/public_papers原件；article_type=2/year=2025 tokens0/20/40 Blog JSON 有payload且末页has_more=false，邻接Jul14与Jun28无本窗条目。article_type=1 tokens0/40/60/80缺sub_article_list，token20仅一篇Jun12 SwiftSpec | Blog本窗恢复有据；paper total94 与payload不一致，不能称94篇完整覆盖；论文当窗目录受阻 |
| SRC-BAIDU-ERNIE | [Blog p1](../daily-20250701/ernie.raw)、[p2](../daily-20250701/ernie-page2.raw)，2/2末尾Jun30 ERNIE4.5，上一条Aug14，无本窗条目 | Blog2/2读尾；不把Jun30系列发布重新归本窗 |
| SRC-XIAOMI-MIMO | [主页](../daily-20250701/mimo.raw)现存8 Paper日期独立提取，从Sep19跨至June4，本窗无Paper条目；原题名/日期见[DAY恢复](./DAY-RECOVERY.md) | Paper保留列表本窗检查结束；Blog历史payload仍缺，不证明全站零 |
| SRC-MINIMAX | [Blog](../daily-20250701/minimax.raw)、[?page=2](../daily-20250701/minimax-page2.raw)同一标题序列，止于2025-10-27，未到七月 | 伪分页不支持历史覆盖，保留本窗历史条目payload请求 |
| SRC-ARXIV | 本日四主题API首20标题+8个精确题摘，记录见 [SCREENING](./SCREENING.md) | API submitted与公开批次不同；没有恢复本窗正式历史公告标题列表；七项日期保留，不作零事件 |

对受阻机构合并请求可恢复的2025-07-03/04主线历史研究目录（真实分页/响应payload）及命中原公告时区。Google pubs、Meta、Hunyuan全部论文、Z.ai、Seed论文、MiMo Blog、MiniMax均不支持“无遗漏”。原件到达后只重开本窗该源，不重复失败路径或全站历年扫描。
