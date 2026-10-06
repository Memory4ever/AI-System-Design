# 2025-12 arXiv 日期证据辅助恢复

检查时间：2026-10-02T17:38:45+08:00（以下请求在本轮约 17:32-17:38 执行）。

角色与边界：只调查官方日期方法和历史延期依据，不写 Daily/Books，不作作者日级完成裁判，不扩论文发现、候选池或全月库存。测试仅 `2512.00883v1` 与现有 `daily-20251217/ADMISSION_CALIBRATION.md` 所关联的 `2512.13507`。后者实际身份是 Seedance 1.5 pro Technical Report；本记录不把用户所称“模型卡”自动视为独立已核事件。没有读取旧 Weekly，未 override 继承模型，未 stage/commit/push。

## 可立即复用的结论

- **取得了 2025 年原始官方圣诞/年末延期公告**，不仅是现行 2026 假日表。公告明确区分接收且接受的区间与公告时刻，也明确延期影响新提交的公共可用性。
- **取得了官方文档的 2025 固定 Git 历史版本**，可独立核 2025 假日表及常规排期，避免滚动文档覆盖历史。
- **两个测试 ID 的 OAI `arXivRaw` 均实际返回成功**；其中版本日期仍是提交历史，`datestamp` 是元数据修改日，未见可直接用于首公告归日的字段。
- **本轮尚未取得两个 ID 的实际首次公告批次**。下文给出条件性排期换算，不将它们写成确定当窗候选或零命中证明。此次辅助结果不表示任何 Daily 完成或独立复核通过。

规则基线已实读：`AGENTS.md`、`docs/RESEARCH_CONTRACT.md` §2、`docs/REPORT_CONTRACTS.md` §2/§3.3。Daily 是北京时间前日 09:00 至当日 09:00，含起不含止；Submitted 不等于首公开；只有支持范围完全落窗才可正面采用。本文件只引用合同，不建立另一套日期规则。

## 1. 2025 年原始官方延期公告

实际入口：[2025 年 11 月官方月档案](https://blog.arxiv.org/2025/11/)，点开其中年末延期文章。12 月月档案本轮仅显示 endorsement 文章，不能由此断言没有假日公告；相关公告发布在 11 月。

原始文章：[Attention Authors: Temporary changes to announcement schedule due to end-of-year holidays](https://blog.arxiv.org/2025/11/21/temporary-changes-to-announcement-schedule-due-to-end-of-year-holidays-2025/)。页面署名 Kat Boboris，发布日期 `November 21st 2025`（公告文章发布日期仅日精度，页面未披露其发布时间区）。正文排期明确使用 `ET`，不是从文章发布日期反推。

以下保留正文日期数字及排期语义，接收区间含起不含止；条件为正文所说的 received and accepted，不只是作者提交按钮时间：

| 延期事项 | 原文 ET 接收且接受区间 | 原文 ET 恢复公告时刻 | 北京时间换算 | 按默认窗口的排期归属 |
| --- | --- | --- | --- | --- |
| Christmas / Winter Break；12-25 不公告 | 2025-12-24 14:00 至 2025-12-26 14:00 | 2025-12-28 20:00 ET | 区间 2025-12-25T03:00:00+08:00 至 2025-12-27T03:00:00+08:00；公告 2025-12-29T09:00:00+08:00 | 排期位于 Daily **2025-12-30** 起点，不属于 12-29 窗口 |
| Winter Break；12-30 不公告 | 2025-12-29 14:00 至 2025-12-31 14:00 | 2025-12-31 20:00 ET | 区间 2025-12-30T03:00:00+08:00 至 2026-01-01T03:00:00+08:00；公告 2026-01-01T09:00:00+08:00 | 排期位于 Daily **2026-01-02** 起点，不能截入 12 月 |
| New Year；2026-01-01 不公告 | 2025-12-31 14:00 至 2026-01-02 14:00 | 2026-01-04 20:00 ET | 区间 2026-01-01T03:00:00+08:00 至 2026-01-03T03:00:00+08:00；公告 2026-01-05T09:00:00+08:00 | 排期位于 Daily **2026-01-06** 起点；只保留跨年边界依据，不扩本次调查 |

时区换算是本调查的计算：这些日期美国东部为标准时间 UTC-05:00，北京 UTC+08:00，相差 13 小时。官方排期精度到分钟；表中 `:00` 秒用于表示排期点，不声称已观测到逐篇正文恰在该秒上线。

**支持**：2025 年指定节日的新提交公共可用性延期及明确恢复排期；09:00 恰落边界时进入下一个 Daily 的计算。
**不支持**：某个 ID 已被接受并实际进入上述批次；审核延迟不存在；延期日对应北京时间 Daily 所有其他来源均无事件；排期时刻就是每篇文章实测上线时刻。

## 2. 官方 availability 历史版本

实际 GitHub API query：

```text
https://api.github.com/repos/arXiv/arxiv-docs/commits?path=source/help/availability.md&until=2026-01-01T00%3A00%3A00Z&per_page=2
```

返回首项原字段：`sha=95c71658adbaa987dc2ba1105ef9c5201ecde4ce`；`commit.committer.date=2025-08-06T17:21:19Z`；`commit.message=add 2025 holidays`。第二项 `782dfdf015f67b22cfea0e5398a5c9d3ebca8b49`，`2025-07-18T12:17:20Z`，`clarify availability.md`。这些是文档版本时间，不能当作论文公开时间。

成功实际请求并 Base64 解码 `content`：

```text
https://api.github.com/repos/arXiv/arxiv-docs/contents/source/help/availability.md?ref=95c71658adbaa987dc2ba1105ef9c5201ecde4ce
```

可复查固定版本：[availability.md at 95c7165](https://github.com/arXiv/arxiv-docs/blob/95c71658adbaa987dc2ba1105ef9c5201ecde4ce/source/help/availability.md)。网页读取本轮 Cache miss，但上述官方 API 返回了该版本完整正文，不能把网页失败记为正文未取得。

实际正文 `2025 Holidays` 中的 12 月原字段是 `Thursday 25 December`、`Tuesday 30 December`；单列 `2026 Holidays` 的 `Thursday 1 January`。日期表本身仅日精度，具体恢复区间用 §1 原始公告支持。

同一固定版本说明：公开发生于 scheduled announcement process；moderation 可延迟；最终 ID 随公告分配，其月份是首公告月份而非保证提交月份。常规表的必要两行均为 Eastern US：周四 14:00 至周五 14:00 -> 周日 20:00；周五 14:00 至周一 14:00 -> 周一 20:00。排期规则支持推定路径，不给个体审核完成证明。

## 3. 接口字段能支持什么

| 官方入口 | 本轮核到的字段/语义 | 支持与限制 |
| --- | --- | --- |
| [Advanced Search](https://arxiv.org/search/advanced) | announcement date 支持 year/month；排序使用 v1 announced year/month | 月粒度身份/首公告月份；不支持日窗。现有校准中的日粒度 `announced_date_first` 空响应不能作为零证据。本轮重读表单，未重复扩查该主题池 |
| [API User's Manual §3.3.2.1 / §5.2](https://info.arxiv.org/help/api/user-manual.html) | entry `published` 为 v1 submitted 日期；entry `updated` 为所取版本 submitted 日期；feed `updated` 属查询结果刷新 | 秒精度也不改变字段语义，不能把 `published` 字面名称当首公告；不要与 RSS item `pubDate` 混同 |
| [OAI 官方说明](https://info.arxiv.org/help/oa/index.html) | `arXivRaw` 有版本历史；header `datestamp` 是记录最后修改；OAI 同步以更新日而非提交日筛选 | 可恢复提交版本和元数据修改，但不是首公告查询。文档所述 OAI 通常 22:30 ET 才提供元数据也不是论文首公开时刻 |
| [RSS 官方规格](https://info.arxiv.org/help/rss_specifications.html) | item `pubDate` 是公告日期；`arxiv:announce_type` 区分 new、replacement、cross listing；`lastBuildDate` 是频道刷新 | 有历史原始 item 且 ID/version 与 `new` 匹配时是更合适的公告证据路径；替换/交叉公告不能当首次公开。规格示例的 00:00 偏移时间是批次日期编码，不能未核批次标签与排期就把午夜当实测上线时刻。此轮未取得两 ID 历史 RSS item |

DOI `created`、HTML generated 日期本轮未查，不用它们替代首公开。只查当前 HTTP Date 也只能得到本次响应时间，不能恢复 2025 的可用性。

## 4. 两个限定测试 ID

### 2512.00883v1

官方 [abs v1](https://arxiv.org/abs/2512.00883v1) 实读 Submission history 原字段：`[v1] Sun, 30 Nov 2025 13:11:56 UTC`。精度秒，UTC；它是提交，不是首公开。当前 browse month 为 `2025-12`。

成功实际 OAI query：

```text
https://oaipmh.arxiv.org/oai?verb=GetRecord&identifier=oai:arXiv.org:2512.00883&metadataPrefix=arXivRaw
```

原字段：`responseDate=2026-10-02T09:38:17Z`（本次响应，UTC 秒）；header `datestamp=2026-08-05`（元数据修改日，仅日，字段不显式附偏移）；`version[v1]/date=Sun, 30 Nov 2025 13:11:56 GMT`（提交历史，GMT 秒）。返回还包含 v2/v3/v4，但本轮不审其贡献或事件。

**条件推定，未定案**：v1 提交折合 2025-11-30 08:11:56 EST，位于周五 14:00 至周一 14:00 常规队列；若按常规接受且未进一步延迟，公告排期为 2025-12-01 20:00 EST = 2025-12-02 09:00 北京，位于 Daily **12-03** 起点。不能将提交日直接归为 11-30/12-01 Daily。`2512` 和官方历史 ID 规则支持 12 月首公告月份，不支持“必为 12-01 ET 批次”。仍缺该 ID 的实际 `new` 公告或等效官方接受/公告证明。

### 2512.13507（Seedance 1.5 pro）

官方 [abs](https://arxiv.org/abs/2512.13507) 实读：v1 `Mon, 15 Dec 2025 16:36:52 UTC`；v2 `Tue, 16 Dec 2025 16:58:55 UTC`；v3 `Tue, 23 Dec 2025 17:38:46 UTC`。当前页是 v3，不把它当已取到 v1 公告记录。

成功实际 OAI query（HTTP 200，XML）：

```text
https://oaipmh.arxiv.org/oai?verb=GetRecord&identifier=oai:arXiv.org:2512.13507&metadataPrefix=arXivRaw
```

原字段：`responseDate=2026-10-02T09:37:52Z`；header `datestamp=2025-12-24`；`version[v1]/date=Mon, 15 Dec 2025 16:36:52 GMT`；v2/v3 的 GMT 数值与 abs 的 UTC 提交历史一致。精度与语义同上一例；`datestamp=12-24` 不能用于首公开归日。

**条件推定，未定案**：v1 是 12-15 11:36:52 EST，常规接受且无额外延迟时排期为 12-15 20:00 EST = 12-16 09:00 北京，进入 Daily **12-17** 起点。这提供现有 12-17 校准的定点核验方向，不是已证实落窗。v2 是另一个事件，不可拿其提交时间替代 v1 首公开；官方发布 Blog 的日字段也不自动证明论文正文的公开时刻。本调查不判断贡献或重要修订。

## 5. 实际失败入口与停止位置

- `https://export.arxiv.org/api/query?id_list=2512.00883v1,2512.13507v1`：实际 HTTP **429**，响应 `Rate exceeded.`；不是零条，也未取得 Atom entry。停止重试该接口，OAI 已取得身份/提交字段。
- 两个 §4 OAI URL 在网页工具不可访问，但本机 HTTP 请求成功；以实际 XML 为依据，不能把网页工具失败泛化为官方 OAI 不可用。
- `https://arxiv.org/list/cs.CV/2512?skip=0&show=25`：网页 Cache miss；HTTP 请求 **404**。`https://arxiv.org/list/cs.MM/2512?show=2000`：网页 Cache miss。没有遍历全月标题/候选，也未获得可复查公告分组。
- `https://arxiv.org/catchup/cs.CV/2025-12-16`、`https://arxiv.org/catchup/cs.MM/2025-12-02`：网页 Cache miss；这两条是测试恢复路径，未验证历史日期语法/保留期限，不称为已恢复批次。
- `https://status.arxiv.org/` 仅当前状态；`https://status.arxiv.org/history` 网页失败。当前页官方编辑链接指向 `https://github.com/arXiv/arxiv-status/edit/main/docs/index.html`，网页读取 404。未继续遍历 status Git 历史；2025 假日原始公告与 availability 固定版本已经足以支持本次排期目标。
- 搜索实际使用了限定词 `site.blog.arxiv.org "2025" "Christmas"`、`site.blog.arxiv.org "2025" "holiday" "announcement"`、`site.blog.arxiv.org "December 25" "2025"` 及官方域限定的 `2025 holiday announcement December Christmas`；搜索没有直接恢复目标文章，转到官方 2025-11 月档案后取得。检索空白不作不存在证明；第三方搜索命中不作日期证据。
- 原始 `raw.githubusercontent.com` 的 2025-07 版本请求连接 reset；使用 §2 GitHub contents API 成功取得更适用的 2025-08 固定版本。不把获取文档方式的差异当内容冲突。

定点重开条件：两个 ID 各自与 v1 对应的官方首次 `new` RSS/email/list 公告记录，或可核实的官方逐篇公告/公共可用时间及其字段定义。若只有批次日期，须先核标签时区、其与晚间排期的对应关系，再换算窗口；若取得时间范围跨 09:00，仍保留缺口。没有该证据前，不从 Submitted、ID 相邻编号或一般排期补造首公开时刻。
