# Jan13 有限原始入口恢复

窗口仍为 `[2026-01-12T09:00:00+08:00,2026-01-13T09:00:00+08:00)`；以下是 root 实际调用返回后的定位摘要，不是历史全站召回证明。原先失败的猜测 URL 不用作覆盖证据。

- Qwen：2026-10-03T01:19:03+08:00，`https://qwen.ai/api/page_config?code=research.research-list` 的 research 数组实际60条。已读每条题名/日期的紧凑字段，最新记录为2025-12-23，窗口命中为空；该旧目录本身缺2026切片，因此不能证明本窗没有发布。恢复需求仅为本窗官方历史目录/事件正文，不扩全年旧题。
- Hunyuan：`POST https://api.hunyuan.tencent.com/api/blog/publicList`，`page=1,size=20,renderType=0`，实际9条，现有日期范围2026-02-03～2026-09，未恢复本窗历史条目。浏览器主 Research 超时不被解释为零发布；API只支持当前有限列表事实。
- Seed 论文：2026-10-03T01:20:32+08:00，`https://seed.bytedance.com/api/get_article_list_v2?article_type=1&count=20&order_desc=false&publish_year=2026`，header `x-tt-locale: US`。实际19条，`total=82,has_more=true,next=20`；用 `ArticleMeta.PublishDate` 原 epoch-ms，不用 create/update，当前升序首条为2026-01-19T16:00:00Z，所读页至2026-02-24T16:00:00Z，已越过本窗而停止。返回数与声明count的差额、历史已删/未列事件未恢复，不能作零遗漏证明；不继续后面全部82条。
- Seed Blog：同API，`article_type=2,count=20,order_desc=false,publish_year=2026`，实际14条，`total=19,has_more=false`、空next；最早可见2026-02-11T16:00:00Z。原返回数/total差额隔离，不将空下一游标解释为完整历史。旧 `/api/article/get_list` 的404仅是入口诊断，不进入本窗来源结论。
- 其他Daily原始入口、RSS、有限月页、Kimi release原body与四主题arXiv查询分别保留在SOURCE_*、FIRST_META_AND_KIMI、ARXIV_THEME_SEARCH、ARXIV_TITLES。四主题140行去重122个题名线索仅是Submitted缓冲发现，不是122篇本窗候选或全文。

以上三机构历史切片若出现准确官方事件记录，只定点重开对应窗口/材料；现有正面候选不从这些目录缺口推导。Google pubs、Meta无正文及MiMo未定日期的限制由各原返回限定，不授全机构无发布。
