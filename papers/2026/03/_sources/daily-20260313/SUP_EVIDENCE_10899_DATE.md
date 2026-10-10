# LookaheadKV 10899：有界先稿身份/日期恢复

2026-10-09 root 定点检查，补充窗口仍 Mar12 北京时间自然日，不改旧候选或原日期。完整v1题摘及arXiv公告日夹证复用；它们只支持arXiv事件，不能排除ICLR同家族更早公开。本文件不采用新技术结论，不比较全部版本。

实际执行两条精确标题/ID官方域查询，打开以下原始入口；未把索引摘要、相对发布时间或提交日当作公开日期：

- [OpenReview指定forum](https://openreview.net/forum?id=RVLMGPXt2i)及[指定PDF](https://openreview.net/pdf?id=RVLMGPXt2i)：当前均重定向browser challenge。指定[api2 note](https://api2.openreview.net/notes?id=RVLMGPXt2i)不可达，原作者已有403记录。普通浏览器只打开此forum，40秒加载超时；未绕过验证。
- 检索可发现[同标题under-review hashed PDF](https://openreview.net/pdf/8469527297a72579e890bd32b2ae240e2483b381.pdf)，直接打开失败。索引显示的“11 months”不是出版方公开日；其under-review标题只是先稿线索，不能据此确定首次公开日期。
- [三星官方研究目录此论文](https://research.samsung.com/research-papers/LookaheadKV-Fast-and-Accurate-KV-Cache-Eviction-by-Glimpsing-into-the-Future-without-Generation)标注ICLR、2026.04.23，并链到官方poster。此为正式会议日期，不排除更早OpenReview公开。
- [作者官方项目](https://github.com/SamsungLabs/LookaheadKV)当前README标注ICLR2026，没有论文首次公开日期。repo当前状态或提交时间不自动证明当时公开可得，不扩完整提交史。

**结论：本窗先稿日期门仍不充分，终态隔离，不评分、不作确认候选、不进入Books，不支撑无遗漏。** 恢复只需RVLMGPXt2i指定原始note的首次公开日/公开版本记录，或同稿带公开日期的作者原始发布；无需时分秒或全库日志。新材料到达后仅重开此家族归属，不重扫整日、跨日或会议全部论文。不是正文贡献被否定，也不是普通未读的外部化。
