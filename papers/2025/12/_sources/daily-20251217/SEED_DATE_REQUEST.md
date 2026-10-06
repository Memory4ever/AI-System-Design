# Seedance Blog 个体日期恢复，供 root 校准

实际检查：2026-10-02T17:53:50+08:00。不是 arXiv 个体公告证明，也不是独立验收。

官方公开前端 `main.897993d4.js` 实际调用 `/api/get_article_list_v2`，传入 `article_type`、`publish_year`、`page_token`、`count`、`order_desc`；未猜测私有接口。实际请求：

```text
GET https://seed.bytedance.com/api/get_article_list_v2?article_type=2&publish_year=2025&count=20&page_token=0&order_desc=true
```

响应 `BaseResp.StatusCode=0`，`total=49`、`has_more=true`、`next_page_token=20`；实际首批15行。Blog 的相邻展示日期：Seed Prover1.5 Dec24、Seed1.8 Dec18、Seedance Dec16、GR-RL Dec2；之后 Nov27 至 July23，说明该页已越过本窗。仍核置顶规则，不把首位当排序证明。

个体原字段（省略无关封面/邮件等）：

```text
ArticleMeta.ID = 1817
ArticleMeta.ArticleID = 1765883631909
ArticleMeta.ArticleType = 2
ArticleMeta.PublishDate = 1765882058000
ArticleMeta.UpdateTime = 1788415475000
ArticleMeta.Status = 2
ArticleMeta.StatusEn = 2
ArticleMeta.StatusZh = 2
ArticleMeta.IsPinned = true
ArticleSubContentEn.Title = Sound and Vision, All in One Take | The Official Release of Seedance 1.5 pro
ArticleSubContentEn.TitleKey = sound-and-vision-all-in-one-take-the-official-release-of-seedance-1-5-pro
```

`PublishDate` 毫秒 epoch 换算（作者计算）：`2025-12-16T10:47:38Z` = `2025-12-16T18:47:38+08:00`，完全落窗。它对应已读 [官方 Blog](https://seed.bytedance.com/en/blog/sound-and-vision-all-in-one-take-the-official-release-of-seedance-1-5-pro) 的展示发布日期，和 arXiv 提交、论文目录人工午夜日期是不同事件。

请求 root 独立核该字段是否足以授 Blog 发布落窗，以及是否还需更明确字段定义。作者不从字段名推 arXiv first-public，不把 UpdateTime/ArticleID 当更早公开证明。若校准认可，家族只计一次 Blog 发布事件；必要机制/实验继续读精确 v1 技术报告，且注明 v1 个体公告日期本身仍未核。
