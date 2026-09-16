# 2026 年 5 月 arXiv 公告批次日期依据

本文件只保存五月 Daily 重建所复用的日期证据，不替代研究合同。

## 官方规则

- arXiv 的 [Availability of submissions](https://info.arxiv.org/help/availability.html) 说明：最终 arXiv ID 在作品进入 scheduled announcement 时分配，不能提前生成或回填。
- 同一页面给出的常规公告时刻为 Sunday～Thursday 20:00（US Eastern），Friday 与 Saturday 不公告。2026 年 5 月未列入该页的 arXiv holiday exception。
- 2026 年 5 月处于 EDT（UTC−04:00），因此 20:00 EDT 对应次日 00:00 UTC、北京时间次日 08:00。

## 单篇归属方法

单篇论文不能只用提交时间、DataCite `created` 或当前 OAI `datestamp` 决定 Daily owner。五月重建仅在以下证据一致时，将公开时刻记为对应公告批次的北京时间 08:00：

1. arXiv abstract/version history 确认身份、v1 提交记录与版本状态；`submitted` 只说明作者提交时间，早于公告日可能来自 moderation hold，不能据此把论文移到更早的 Daily；
2. initial DataCite registration 落入该批次；若 OAI 仍保存首次 datestamp，则应与它一致。当前 OAI datestamp 已被后续 revision 覆盖时，只把该字段记为 revision metadata，不因此制造日期缺口；
3. arXiv ID、月份、exact-v1 identity/version history 和官方公告节奏相容。

该时刻是由官方批次规则推导的公开时刻，不表述为单篇 abstract 页面直接披露的 timestamp。initial registration 缺失或冲突、ID/version identity 异常，或者无法将 registration 与官方批次对应时，保留具体日期缺口，不补造时刻；只有当前 revision datestamp 较晚不构成冲突。
