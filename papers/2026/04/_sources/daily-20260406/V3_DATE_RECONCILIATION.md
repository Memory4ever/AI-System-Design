# 2026-04-06 公开日期证据 reconciliation

核验日期：2026-09-26。范围只限 04/06～08 共用的 arXiv 日期链及本日窗口，不重审全文，不改 Report 或 Books。

## 结论

本窗为 `[2026-04-05T09:00:00+08:00, 2026-04-06T09:00:00+08:00)`。一致性复核后，**02333～03231 的永久 ID 公告分配规则、相邻批次/OAI 日级边界、官方公告 slot 与本批首中末版本元数据簇，可共同支持标明推断性质的 `[2026-04-06T08:00:00+08:00,2026-04-06T09:00:00+08:00)` 区间**。这不是逐篇精确公告时间，也不是将任一字段直接改名为 first-public。保留家族仍须核其自身版本、撤回及更早公开例外；日期链通过不等于准入、证据、Books 或整日报 Gate 通过。

此前要求实际 09:00 公告成功日志才能接受全部保留项，强于当前合同允许的有据推断，现撤销该绝对要求。06171 的晚 Updated 反例只否定字段等同，未直接反证本批的具体链；不存在具体例外时，不把整批隔离，也不重新深读有效方法证据。

## 已核的官方规则与字段

[arXiv availability](https://info.arxiv.org/help/availability.html)说明永久 ID/DOI 不能提前提供，ID 在公告的自动流程中分配，月份对应首次公告月份；常规公告为 Sun–Thu 20:00 美国东部时间。2026 年 4 月采用 EDT（UTC−04），本日对应 `2026-04-06T00:00:00Z`／北京时间 08:00。官方列出的 2026 假日没有 04/05～07，但仍允许临时延期；规则是预期时刻，不是本轮已取得的历史成功公告记录。

[官方公告流程说明](https://arxiv.github.io/zzz_archived_arxiv-submission-core/announcement_process.html)中，Announced 操作更新 ID、version 和 announcement timestamp。它支持状态和分配顺序，未在本轮提供 2026 年这三批的实际时间日志，也没有证明整批所有正文同时在 08:00 可访问。

必须区分三个不同的 `updated`：

- [Atom API 手册](https://info.arxiv.org/help/api/user-manual.html)中的 entry `published`/`updated` 是首次／所取版本的提交处理日期；exact-v1 时二者相等。feed 顶层 `updated` 是查询 feed 的更新时间。均不改名为首次公开时间。
- DataCite `attributes.updated` 是 DOI 记录被触动的时间；其 [created/registered 说明](https://support.datacite.org/docs/what-does-the-doi-last-updated-mean)区分系统建档与 Handle 注册，不能直接当论文公开分钟。
- 旧笔记称“v1 Updated”的值实际来自 `attributes.dates[dateType=Updated,dateInformation=v1]`，不是 Atom entry `updated`。它由 `arxiv.content` 客户提交，是版本元数据线索，但尚未取得 arXiv 对该字段与首次公告时刻的确定映射。

## 本轮实际取得的边界

| 身份与原始入口 | DataCite created（UTC） | dates Updated / v1（UTC） | Submitted / v1（UTC） | 可证明与不可证明 |
| --- | --- | --- | --- | --- |
| [2604.02332](https://api.datacite.org/dois/10.48550/arxiv.2604.02332) | 2026-04-03T02:09:29Z | 2026-04-03T01:06:18Z | 2026-04-02T17:59:59Z | 前邻 ID 的注册落在更早日期；不是 04/06 公告名单。 |
| [2604.02333](https://api.datacite.org/dois/10.48550/arxiv.2604.02333) | 2026-04-06T01:23:49Z | 2026-04-06T00:00:04Z | 2026-01-06T11:05:01Z | 与 04/06 批次起点相容；Jan Submitted 不与 Apr ID 矛盾。 |
| [2604.03231](https://api.datacite.org/dois/10.48550/arxiv.2604.03231) | 2026-04-06T01:45:01Z | 2026-04-06T00:51:19Z | 2026-04-03T17:59:51Z | 与该批次尾部相容；不能把版本元数据更新别名为公开时刻。 |
| [2604.03232](https://api.datacite.org/dois/10.48550/arxiv.2604.03232) | 2026-04-07T02:36:29Z | 2026-04-07T00:00:04Z | 2026-01-18T12:37:27Z | 与下一批相容；注册日期晚不单独证明没有更早公开。 |

上述注册时间都在北京时间 09:00 之后，单凭注册不能缩成 08:00～09:00，也不能反向证明正文晚公开。此次区间判断采用的是官方 slot、公告赋号、连续相邻批次与本批首中末元数据簇的组合，而非注册单字段；其合理推断性质和未证明逐篇分钟的边界必须保留。

本轮有一个直接反例：[2604.06171](https://api.datacite.org/dois/10.48550/arxiv.2604.06171) 的 created/registered 为 `2026-04-09T01:43:04Z`，而 `dates Updated/v1=2026-04-29T01:00:58Z`。因此“v1 Updated 必等于首次公告”不能作为公共规则。不能反向把所有较晚 Updated 认作正文较晚公开；这个反例只撤销字段等同假设。

## 有界恢复已尝试

1. [官方历史月列表](https://arxiv.org/list/cs.CL/2026-04?skip=0&show=2000)实际返回 April 标题/身份列表（本页 2000/2532 条）。本轮另取原始 HTML 核 `<h1>`～`<h6>`：仅有 Computation and Language 与 Authors and titles for April 2026 两个标题，没有按日 `<h3>` 分组；不读取全池论文。它与当前 `recent` 页含日期分组的结构不同。
2. `/list/cs.CL/260406` 与 `/list/cs.CL/2026-04-06` 本轮网页工具未取得有效历史日列表；不把猜测路径失败写成 arXiv 不存在日数据。
3. [官方 OAI Raw 单篇](https://export.arxiv.org/oai2?verb=GetRecord&identifier=oai:arXiv.org:2604.03232&metadataPrefix=arXivRaw)实际返回 header datestamp `2026-04-07`，v1 date 为 Jan18 Submitted，没有小时级公告上界；它不能补齐本窗截止证据。
4. 有界 Wayback CDX 查询官方 `arxiv.org/list/cs.CL/new` 的 04/05～09 抓取记录连接失败；calendar captures 入口超时。没有取得存档，不宣称存档不存在。
5. 官方 arxiv-browse 的公开 tree 中只定位到 DOI/metadata 测试项，没有在本轮取得 DataCite 版本 Updated 到公告时刻的映射。到此停止通用入口探索，不扩为全组织代码审计。

## 最小 Materials Request 与恢复条件

去重请求 ID：`DATE-ARXIV-APR06-08-PUBLIC-BATCH`；04/07、04/08 引用同一请求，不各自重新搜全年。

本请求现收窄为具体例外的恢复入口，不再作为 04/06 整批通过的必需条件。04/07/08 只对保留家族中跨截点或存在更早公开线索的项请求材料。可接受：

- arXiv 当日正式公告名单／邮件／可核存档，带对应批次日期和明确时区，并说明该名单在 09:00 截点前已公开；或
- arXiv canonical announcement record／日志，直接给本轮保留家族的 first-announcement 与正文公开时间；或
- 官方对版本 `Updated` 的明确映射及可复查首公告历史，加上真实批次公开完成上界。不能仅提供当前同版本 Updated 值。

需要恢复的对象限于当前拟保留家族及决定边界的相邻 ID，不请求 449 raw 条目全文。取得材料后检验推断区间是否完全落窗，再处理确切跨日项；不自动移动整批，不重新使用 Submitted/DOI-created 作为公开时刻。Report 和 Books 终态仍由主任务分别验收。
