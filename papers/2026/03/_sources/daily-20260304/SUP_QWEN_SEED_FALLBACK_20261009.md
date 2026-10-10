# 官方目录定点恢复

执行日：2026-10-09。目标仅为本日报补充窗口 2026-03-03；不重开旧候选。

- Qwen：实际 GET `https://qwen.ai/api/v2/article/retrieval?type=qwen_ai&language=en-US`，成功返回 `data.articles` 40 条，无 total 或分页字段。读取本窗邻接元数据：Qwen3.5 2026-02-16、Max-Preview 2026-03-19；返回列表没有 03-03 项。该列表未包含已知 03-02 小尺寸发布，故不能证明本窗历史目录完整；原 QwenCode 同事件审阅保留，不由此重扫全部 releases。
- Seed：实际 GET `https://seed.bytedance.com/api/get_article_list_v2?article_type=1&publish_year=2026&page_token=20&count=100&order_desc=false`，StatusCode 0；返回 14 条，total 82、next_page_token 40、has_more true。读取 PublishDate 对应的北京时间日期与标题；该页按显示日期为 02-27、03-01、03-12、03-15、03-16、03-21、03-23～26，03-01 与 03-12 之间无显示 03-03 的论文。这只恢复论文目录的有限邻接段，不证明 Blog 或全部历史首次公开；目录收录日期不覆盖 arXiv 公开日期。

上述14条是默认locale返回。root另以 `x-tt-locale: US` 实际取得18条，同样total82/next40/has_more true；BJT邻接增加Mar02两条而仍无Mar03目录项。只核本日目录段，不把Mar02全文或题摘变成本日队列；locale差额不证明隐藏历史完整。

本次实际恢复未建立新增本窗家族，不产生评分或 Books 写入。未取得的完整历史发布段仍是隔离的 Coverage 限制，不用于无遗漏断言。
