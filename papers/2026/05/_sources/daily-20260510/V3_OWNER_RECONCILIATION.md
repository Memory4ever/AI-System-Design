# 2026-05-10 V3 Owner Reconciliation

## 当前结论

- Daily 窗口：`[2026-05-09T09:00:00+08:00, 2026-05-10T09:00:00+08:00)`。
- arXiv owner 采用 scheduled announcement / publication 语义，不采用投稿时间、DataCite `created` 或后来目录回填日期。
- 本窗 arXiv public event 为 0；已核实公开事件中的候选 denominator 为 0。动态历史入口的终态限制不参与
  “全站零遗漏”断言。
- 本文件不删除旧证据，只撤销它们作为 2026-05-10 owner-day、Evidence Gate 和 Books queue 的效力。

## 为什么旧结果失效

| 旧材料 | 旧结果 | V3 判断 |
| --- | --- | --- |
| `papers/2026/05/10/README.md` V2.1 | 以 DataCite `created` 作为 owner proxy，声明 Complete | 方法失效；0 个公开 arXiv 事件的结果偶然一致，但不能继承完成状态 |
| `INDEPENDENT_FRESH_CONTEXT_AUDIT.md` | 436 identities、57 candidates | cohort 混入本窗投稿与 later-indexed identity，不属于 05-10 public-event denominator |
| `BOOKS_WRITEBACK_QUEUE.md` | 29 个 Integrate queue | 不再是 05-10 Books queue；需逐 family 迁回真实首次公开日后重判 |
| `POST_WRITE_AUDIT_V1.md` | 29/29 Books placement 通过 | 只能说明当时检查到相应正文，不能证明 05-10 日期归属或当前 Source Review 成立 |
| 同目录 JSON、脚本与审阅附件 | 支持旧 owner replay | 保留为历史取证材料；不得被自动化重新解释为 05-10 V3 Gate |

## 三个日期锚点

1. [arXiv Availability](https://info.arxiv.org/help/availability.html) 规定周五、周六没有公告；周日 20:00 ET
   的下一批公开时间晚于本日报北京时间 09:00 右边界。
2. [ERNIE 5.1](https://ernie.baidu.com/blog/posts/ernie-5.1-0508-release/) metadata 为
   `2026-05-09T00:00:00Z`，即北京时间 08:00，早于本窗起点一小时。
3. Seed 目录中的 `2605.09233` 虽显示本窗内 `PublishDate`，但记录后来更新，且对应 arXiv 稿件当时只有
   submission event；目录字段不能替代 scheduled announcement。

## 后续使用规则

- 不从本 cohort 继承评分、Source Review、Books disposition 或完成声明。
- 逐 family 找到真实首次公开事件后，只在真实 owner Daily 定点恢复，不重跑 05-10。
- 现有 Books 正文不在本 lane 修改；其内容是否保留由真实 owner day 的 Evidence 与 Books compare 决定。
- 2026-05-10 已由未参与作者重建的 fresh-context reviewer 独立复核通过；详见
  [V3_INDEPENDENT_FINAL_AUDIT.md](./V3_INDEPENDENT_FINAL_AUDIT.md)。
