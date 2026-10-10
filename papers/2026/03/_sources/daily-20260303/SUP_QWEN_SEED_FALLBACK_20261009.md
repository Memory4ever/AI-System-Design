# 官方目录定点恢复

执行日：2026-10-09。目标仅为本日报补充窗口 2026-03-02；不重开旧候选。

- Qwen：实际 GET `https://qwen.ai/api/v2/article/retrieval?type=qwen_ai&language=en-US`，成功返回 `data.articles` 40 条，无 total 或分页字段。读取本窗邻接元数据：Qwen3.5 2026-02-16、Max-Preview 2026-03-19；返回列表没有 03-02 项。该列表未包含此前已取得的 03-02 小尺寸发布，故不能证明本窗历史目录完整，也不撤销必要历史段限制。
- Seed：实际 GET `https://seed.bytedance.com/api/get_article_list_v2?article_type=1&publish_year=2026&page_token=20&count=100&order_desc=false`，StatusCode 0；返回 14 条，total 82、next_page_token 40、has_more true。读取 PublishDate 对应的北京时间日期与标题；该页按显示日期为 02-27、03-01、03-12、03-15、03-16、03-21、03-23～26，03-01 与 03-12 之间无显示 03-02 的论文。这只恢复论文目录的有限邻接段，不证明 Blog 或全部历史首次公开；目录收录日期不覆盖 arXiv 公开日期。

上述14条是默认locale返回，不是所有语言可见条目。root另以 `x-tt-locale: US` 实际取得18条，同样total82/next40/has_more true；新增可见两条PublishDate对应Mar02：

- [Anatomy of the Modality Gap](https://arxiv.org/abs/2603.01502v1)：完整题摘提出跨层CKA与speech-text对齐、输入统计校准不足/可能有害的反证，潜在贡献不是简单模态标签。Seed显示Mar02是可保留的官方目录日期；精确v1仅记Submitted Mar02，尚不能将目录显示日认证为arXiv首公开日。较晚ArticleID本身也不否定官方日期。此次隔离只针对论文first-public归属，不否认目录日级事实。
- [On the Residual Scaling of Looped Transformers](https://arxiv.org/abs/2606.18524v1)：完整题摘的weight-tied相关更新及N/L因子化有机制潜力；Seed显示Mar02，但所链精确v1Submitted Jun16。OpenReview早期同题名稿是恢复线索，作者数/摘要范围不同，实际入口验证页、API403，不能把其较窄命题绑定成当前多层因子化版本；也不能用六月提交日否认更早作者稿。

两条完整题摘及精确v1身份由root实际读取，supplement_20260308非作者独立复核日期权限通过；一次题名＋作者dated入口恢复未找到必要版本证据，没有全文绕日期。替代材料：Anatomy的官方首公告或明确首次公开正文日；Residual的Mar02有日期作者稿及版本对应关系。取得后只重开这两个身份，不请求时分秒、不扩其他日期。两项未评分、未成为确定新增候选、未写Books；原确定新增2家族不变，日期潜力19→21。

未取得的完整历史发布段仍是隔离的 Coverage 限制，不用于无遗漏断言。
