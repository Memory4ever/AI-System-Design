# 2025-09-16 定点恢复

最新处理结果：root单项`INDEPENDENT_CODEX_REVIEW.md`实际独核通过，Codex正式5分标准完成/仅报告，Books0；旧“新普通待办”作为恢复过程保留，不再重复请求同项。日级未通过，其他源/安全/误排独核仍待。

MiniMax单源窄补：本日重新执行`https://www.minimaxi.com/blog`单次20秒上限，HTTP200/144114bytes，原`minimax-cn-recovery.raw`。实际解析非script正文13条，从2026Aug13至2025Jan15，Oct27→Jan15跨本窗下界，停止Jan15；没有本窗条目。原“历史目录未恢复”泛化保留项撤回，仅保留删除历史/其他未公开修订不保证。没有继承别日抓取或展开这13条全文。

作者Tesla；2026-10-06T12:23:47+08:00开始，12:26+08:00整理。只重开OpenAI事件归属和DeepSeek历史入口。旧抓取/失败保留，不授日级完成。

## 官方RSS：事件分离

`https://openai.com/news/rss.xml` curl单次20秒上限，HTTP200；原XML为`openai-rss-recovery.xml`，解析1247个item，只按本窗UTC `[2025-09-15T01:00Z,2025-09-16T01:00Z)`筛选，不把全年库存作为审阅队列。

| 事件 | RSS原pubDate | 北京时间与处置 |
| --- | --- | --- |
| Introducing upgrades to Codex | Mon, 15 Sep 2025 10:00:00 GMT | 2025-09-15T18:00:00+08:00，落16日报；准入校准普通待办，不再datehold |
| How people are using ChatGPT | Mon, 15 Sep 2025 03:00:00 GMT | 2025-09-15T11:00:00+08:00，落窗；核心是消费者采纳/经济用途分类，不显示模型或执行机制增量，关闭该切片 |
| Addendum to GPT-5 system card: GPT-5-Codex | Mon, 15 Sep 2025 00:00:00 GMT | 2025-09-15T08:00:00+08:00，窗外；不算16日报新事件，也不重开15日 |

Codex原核心`https://openai.com/index/introducing-upgrades-to-codex/`本轮web成功、curl403（保留`codex-release-recovery.raw`），身份/正文可复用`16finalcore.json`，本轮再次实际阅读GPT-5-Codex、CLI/cloud及安全段落。页面Sep23更新明确分离，不用于Sep15归属。动态thinking、短请求/长任务的资源分配及477→500任务分母是可校准的局部预算/评价边界；控制策略与训练配方Not Disclosed，不能据93.7%或7小时个例宣称通用SLO/可靠性。沙箱/联网/人工review的公开执行边界不等于安全保证。作者拟2+2+1=5，仅在root确认具体增量后扩展受影响审阅；不是用分数倒推准入。

## DeepSeek原入口实际执行

`https://www.deepseek.com/updates`单次20秒上限，HTTP404；原响应`deepseek-updates-recovery.raw`具有`DeepSeek | 404`和`app-not-found`，不是空历史列表。web同入口及尾斜线、无www/en变体均访问失败，保留`16recoveryupdates.json`。主站`/en/news/`实际可见Research Index从Oct21跨至May14，但News只有至Sep22及View All按钮，不以此授完整历史。

定点转到官方原始`https://api-docs.deepseek.com/updates/`，curl20秒上限HTTP200，原响应`deepseek-changelog-recovery.raw`。实际HTML文本读取Sep29、Sep22、Aug21连续日期和相应核心，最早停止Aug21已越本窗下界；不是仅搜索摘要。Sep22V3.1-Terminus与Aug21V3.1夹住本窗，没有本窗条目。仅授保留Change Log切片检查，不授全机构删除历史/论文/仓库修订无遗漏。web超时不否定curl成功。

## 新普通待办

root请独立校准Codex release的具体贡献及拟5分最低投入；若通过，再由作者处理受影响方法/评价/安全边界与Books判断。旧作者ready在此窄重开后撤回，不把root校准或作者未扩展的审阅写成外部保留项。原arXiv日期保留和其他已有效初筛不重跑。
