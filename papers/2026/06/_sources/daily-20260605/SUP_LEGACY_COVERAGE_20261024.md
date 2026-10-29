# 原小时窗覆盖原块

只存原历史依据；本轮自然日覆盖以README当前表与SUP_ORG_DELTA为准。

以下为旧小时窗原覆盖：

只处理本窗的大模型架构、训练/后训练、推理资源、平台评价/安全、Agent执行状态与多模态主线；不扫Weekly，不将目录全部领域条目变成候选。下表的“已检查”限实际原入口与停止范围；受阻部分已隔离，不支持零命中或全来源无漏项。

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | 官方[RSS](https://openai.com/news/rss.xml)实际1240条按窗口过滤，2条原pubDate与两核心已读；Dreaming=June04 09UTC、Endava=12UTC | 已检查 | 两项前分母关闭经root校准；不展开全部图表或客户外链，不把后来update当本窗事件 |
| SRC-ANTHROPIC | [Research](https://www.anthropic.com/research)首屏及原HTML173个publishedOn；目标前后为Navigator June03 18UTC、news10:55UTC、chemist June05 20:57UTC；本窗字段无条目 | 已检查 | 结果限官方目录字段；chemist明确窗外且science范围暂缓，不沿旧calendar归属 |
| SRC-GOOGLE-AI | [DeepMind Research](https://deepmind.google/research/) curated latest/年级publication；Google Research GenerativeAI第一页读至June03→May28，NLP至June05 AgenticRAG→May19，MachineIntelligence首12至August21；分页click错误/原HTMLtimeout，两条目标官方域查询 | 受阻 | AgenticRAG core实际读但June05日历交窗、两次原HTML0bytes缺时钟；MachineIntelligence/DeepMind目标历史主题批次不完整，有限stop不扩55页 |
| SRC-META-AI | Blog入口timeout；[publication page1](https://ai.meta.com/results/?content_types%5B0%5D=publication&page=1)实际成功至June05 SIRA→May27→May26后混旧库存；SIRA官方完整摘要、exact-v2完整摘要/版本史已读，CDN PDF一次cachemiss | 已检查 | SIRA日期/官方PDF版本身份隔离；不能沿旧“非重要修订”去重，目录日历不证明公开时刻，不读全部旧库存 |
| SRC-QWEN | qwenlm.github.io redirect/qwen.ai壳→只读page_config：news17最新2025Apr28、Research60最新2025Dec23；本日有限官方域June04/05查询仅chat分享噪声 | 受阻 | 2026目标原始研究目录缺口；旧77配置不证明本窗零材料，不扩旧正文 |
| SRC-DEEPSEEK | 官方[研究与动态](https://www.deepseek.com/news/)研究June24→Feb25、动态Sept10→Apr24，停止目标前 | 已检查 | 动态“查看全部”局限保留；只证明可见目录，不作全仓commit审计 |
| SRC-MOONSHOT | [Platform Blog](https://platform.kimi.com/blog)全部可见27条最新2025Nov07；官方GitHub exact0.10.0/0.10.1 release API时钟/flags与393/383/399/443必要patch | 已检查 | Kimi一家族深入；旧Blog不代表2026所有模型事件，代码阅读不是运行测试或生产SLO |
| SRC-TENCENT-HUNYUAN | Research壳→fresh只读POST publicList pageNum1/pageSize100/renderType0：code0/totalNum9/list9全publicAt/display/published字段，publicAt July06→April30夹住目标 | 已检查 | 无本窗publicAt条目仅限该9条目录；display不是publicAt，字段不自动证明论文first-public |
| SRC-ZAI | 官方Research全部日期目录前14，June16→May20后停止 | 已检查 | 可见日历片段无本窗条目，不制造论文公开时刻，不读旧全文 |
| SRC-BYTEDANCE-SEED | [public_papers](https://seed.bytedance.com/en/public_papers) page1/13首20，June04 electron-dynamics范围暂缓、June03 MetaPoint在本窗日历之前、May29停止 | 已检查 | 不拿目录日历证明linked paper first-public，不扩242条/science正文 |
| SRC-BAIDU-ERNIE | 官方[中文Blog](https://ernie.baidu.com/blog/zh/) page1/2最新May09→April30→更早，已到目标前不翻旧page2 | 已检查 | 可见目录无本窗条目，不声称全部仓库release已扫 |
| SRC-XIAOMI-MIMO | 官方Paper8日期June29→March13、Blog15无日期；fresh4752.2908c99e.js 688092bytes，EN/ZH Code June10、UltraSpeed June08、pipeline May30 | 受阻 | undated Blog不能证零；需目标发布clock/原目录快照，不读15窗外全文 |
| SRC-MINIMAX | 本日EN/中文Blog June09→June01→May停止；AgentTechBlog15行壳，所链llms.txt当前48行使用目录已读、无历史dated Blog | 受阻 | 主目录无可见本窗条目；Agent历史分支缺口独立隔离，不以壳/index作零命中，不读48用户指南 |
| SRC-ARXIV | 旧owner receipt68items显式DataCitecreated口径无效；source/submission receipts不存在。历史day短路404，正确2026-06月2718无dayheaders，advanced公告仅year/month；exact05241v1原页和有限目标公告搜索 | 受阻 | 71具名first-public上界未证；各主题本批原始公开目录不可恢复，不扩706宽列表/整月2718/全部原文，不把404作空批次 |

