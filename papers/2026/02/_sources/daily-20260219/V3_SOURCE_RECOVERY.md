# 本日有限来源恢复

实际执行时间2026-10-05T00:35:38+08:00附近；只恢复02/19窗口，不复用其他Daily覆盖结论。以下补充来源入口本身不改变论文first-public，也不把历史目录内容扩成全文队列。

## SRC-TENCENT-HUNYUAN

Research动态入口与浏览器此前有限恢复未能取得历史全列表；本日先GET错误host路径404（不是无事件），再按官方具体接口实际POST `https://api.hunyuan.tencent.com/api/blog/publicList`，JSON `{"pageNum":1,"pageSize":20,"renderType":0}`，Content-Type application/json、Accept-Language zh-CN，200/code0。

[原始完整响应](V3_hunyuan_publicList_page1.json) totalNum9且list9；实际读九条title/publicAt/displayPublishTime。最早CL-bench publicAt1770112927=02/03 10:02:07Z，GradLoc1770971763=02/13 08:36:03Z；之后display日期跳04/23（其publicAt实际07/06）及04/30，再到7～9月。所有publicAt/display字段均未本窗命中。停止page1已返回9/9，不继续历史。此结论只覆盖该publicList发布目录，不能把Research全部论文/未归档事件称无遗漏；独立arXiv主题切片仍有效。

## SRC-BYTEDANCE-SEED

实际取得[官方论文页](V3_seed_public_papers.html)，其当前page1为20/242、Aug18～May14，不能代本窗。有限读取该页实际引用的[官方JS](V3_seed_main.js)，明确Publication=1/Blog=2、GET `/api/get_article_list_v2`、query参数article_type/count/order_desc/publish_year/page_token；不执行代码、不扫其他bundle。

本日实际GET `https://seed.bytedance.com/api/get_article_list_v2?article_type=1&count=100&order_desc=false&publish_year=2026`，[原响应](V3_seed_type1_2026_asc.json)20条、next_page_token20、total82、has_moretrue。实际只浏览按PublishDate升序至第19条首次跨截止：Jan19→Feb12（FLAC raw1770912000000=Feb12 16Z）→Feb24（FlowPortrait raw1771948800000=Feb24 16Z），即停止；前后非本窗条目不初筛/评分，不翻page2。

Blog同参数article_type2，[原响应](V3_seed_type2_2026_asc.json)9条、total23。实际只浏览至第4条首次跨截止：Feb11 Seedance2、Feb12 Seedream5Lite、Feb13 Seed2→Mar31招聘，即停止，后面不形成候选。目录PublishDate是官方索引发布字段，UpdateTime/ArticleID均未当论文first-public。两有限目录本窗无条目，覆盖该API的历史切片，不宣称机构一切事件无遗漏。

## SRC-MOONSHOT

平台Blog已实际读当前可见2025年末及更早条目，不能闭合2026/02目录。又本日GET[官方组织页](V3_moonshot_org.html)200，实际读README当前research/service/infra项目与10/42可见repos，最新更新时间Oct2～Aug3。Repository Updated不是本窗release或首次公开。当前Kimi3、AttentionResiduals等未来项目不送入本日；目标历史发布列表未恢复，保留精确02/18～19原官方event/archive请求，不为“无标记”遍历42repos历史。

## SRC-MINIMAX

当前Blog可见Aug13～Mar18不能闭合本窗；AgentTechBlog页面少量导航此前已读。本日有限GET `https://agent.minimax.io/docs/techblog.md`：不follow返回307/0，随后实际follow到官方minimaxi文档200，[原Markdown](V3_minimax_techblog.md)829bytes。正文只有2026/05/13 AgentTeam一项，非目标日期；不继续该项目正文或按llms.txt全站扫。仍未恢复主Blog的02/18～19历史切片，留必要目录缺口，不称零事件。
