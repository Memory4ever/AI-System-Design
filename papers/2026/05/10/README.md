# Daily Research — 2026-05-10

**规范：** V3
**窗口：** 2026-05-09T09:00:00+08:00 ～ 2026-05-10T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-09-14T21:35:36+08:00

## 1. 结论

在可核验的官方公开事件中，本窗没有通过日期与贡献 Gate 的候选 Source Family。arXiv 的首次公开以官方 scheduled announcement 为准；
2026-05-10 是周日，本窗内没有 scheduled announcement。旧材料中按 DataCite `created`、投稿时间或后来目录
回填日期归入本日的 436 个 identity、57 个候选与 29 个 Books 条目，均不能证明它们在本窗首次公开，因此不继承
其完成声明、评分或 Books 队列。它们保留为待按真实公开日重新归属的历史证据，不作为本日 denominator。

Baidu 的 ERNIE 5.1 官方页面给出的发布时间为 `2026-05-09T00:00:00Z`，即北京时间 08:00，早于本窗
起点一小时，已归属 2026-05-09。ByteDance Seed 目录中的 `2605.09233` 虽把 `PublishDate` 回填为北京时间
2026-05-10 00:00，但记录在 2026-07-03 更新，且对应 arXiv 稿件在本窗尚未进入公开 announcement；该目录字段
不能替代首次公开证据。

因此已核实公开事件中的本日候选数为 0，没有评分、Source Review 或 Books 写回；六个动态历史入口的终态
Coverage limitation 不参与零遗漏断言。作者侧扫描、日期归属、排除判断与命题级 Books compare 已完成，
非作者 fresh-context 终审进一步核对了时间、公开语义、机构入口与旧 cohort 隔离，报告闭环。

## 2. 来源覆盖

本轮只检查 Daily 来源，不扫描 Weekly 来源。动态历史入口无法恢复稳定分页时按合同隔离；这类缺口不支撑正向
候选、Books 判断或“全站绝无遗漏”的断言。

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | [Research](https://openai.com/research/) 历史入口与本窗定点检查 | 受阻 | 未恢复可按 24 小时窗口分页的官方历史目录；不支持零遗漏断言 |
| SRC-ANTHROPIC | [Research](https://www.anthropic.com/research) 当前嵌入式历史数据；相邻公开事件为 2026-05-08T12:18:00Z 与 2026-05-14T17:06:12.172Z | 已检查 | 当前页面可排除已列公开事件落窗；动态目录缺稳定分页，仍不支持全站零遗漏断言 |
| SRC-GOOGLE-AI | [DeepMind Research](https://deepmind.google/research/) 与 [Google Research Publications](https://research.google/pubs/) 的本窗有界检查 | 受阻 | 历史列表日期粒度和分页不足以闭合 24 小时全站断言 |
| SRC-META-AI | [Meta / FAIR Research](https://ai.meta.com/research/) 的可见历史列表与本窗定点检查 | 受阻 | 动态目录缺稳定的历史日级分页停止点 |
| SRC-QWEN | [Qwen](https://qwenlm.github.io/) 官方历史入口与本窗定点检查 | 受阻 | 旧入口与现行目录不能稳定回溯本窗；未以搜索缺命中代替归档证据 |
| SRC-DEEPSEEK | [News / Research](https://www.deepseek.com/news/) 历史索引；相邻可见事件为 2026-04-24 与 2026-05-14 | 已检查 | 未见可唯一归属本窗的研究事件 |
| SRC-MOONSHOT | [Kimi Blog](https://platform.kimi.com/blog) 与 [MoonshotAI](https://github.com/MoonshotAI) 本窗定点检查 | 受阻 | Blog 可见列表未覆盖 2026-05，仓库也无稳定的历史日级发现页 |
| SRC-TENCENT-HUNYUAN | [Hunyuan Research](https://hunyuan.tencent.com/research)“全部”列表的既有独立停止点；相邻条目为 2026-04-30 与 2026-05-21 | 已检查 | 本次复用已独立核验的相邻日期停止点，不继承旧报告完成标签 |
| SRC-ZAI | [智谱 Research](https://www.zhipuai.cn/zh/research) 列表；相邻条目为 2026-04-29 与 2026-05-20 | 已检查 | 未见本窗事件 |
| SRC-BYTEDANCE-SEED | [Seed 论文目录](https://seed.bytedance.com/en/public_papers) 及目录 API；发现回填的 `2605.09233` | 已检查 | `PublishDate` 不是 arXiv 首次公开证据；该 family 不属于本窗候选 |
| SRC-BAIDU-ERNIE | [ERNIE Blog](https://ernie.baidu.com/blog/zh/) 及 [ERNIE 5.1 正文](https://ernie.baidu.com/blog/posts/ernie-5.1-0508-release/) | 已检查 | 页面 metadata 为北京时间 2026-05-09 08:00，明确在窗外 |
| SRC-XIAOMI-MIMO | [MiMo](https://mimo.xiaomi.com/) Papers 列表与 Blog 入口 | 受阻 | Papers 相邻日明确无本窗条目；Blog 卡片缺可复查的历史发布时间 |
| SRC-MINIMAX | [Research / Blog](https://www.minimax.io/blog) 历史列表；相邻可见事件为 2026-03-18 与 2026-05-26 | 已检查 | 未见本窗事件 |
| SRC-ARXIV | [官方 availability / announcement 规则](https://info.arxiv.org/help/availability.html) 与本窗日历换算 | 已检查 | 周五、周六没有公告；周日 20:00 ET 公告换算后晚于本窗右边界，raw public events=0 |

## 3. 候选与判断

已核实公开事件中的本窗候选分母为 0。没有把窗外发布、投稿时间、DataCite ingestion、目录回填或动态入口
缺口冒充候选；该数字不表示六个终态受限入口已证明全站零遗漏。

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |

三个排除项分别闭合如下：ERNIE 5.1 的北京时间 2026-05-09 08:00 早于本窗起点一小时，保持在
2026-05-09；Seed / arXiv `2605.09233` 在本窗只是投稿，尚未 scheduled announcement，按真实公开日
定点重开；旧 436 identities / 57 candidates / 29 Books queue 由投稿、DataCite 或回填时间形成，作为
owner-day 口径污染整体 superseded，不继承其评分、Evidence 或 Books 状态。

## 4. 证据与知识整合

### arXiv 日期语义

arXiv 官方说明，稿件通过 scheduled announcement 公开：周五和周六没有公告，周四 14:00 ET 至周五
14:00 ET 的队列在周日 20:00 ET 公告，周五 14:00 ET 至周一 14:00 ET 的队列在周一 20:00 ET
公告。由此，本报告的北京时间窗口内没有 arXiv 首次公开 batch。投稿 timestamp、arXiv ID 月份、DataCite
`created` 与 later catalog date 都只能用于身份或归属核对，不能替代公开事件。

### 两个容易误归属的事件

ERNIE 5.1 的官方时间可直接换算到北京时间 2026-05-09 08:00，因此它属于前一份 Daily。Seed 目录的
`2605.09233` 显示北京时间 2026-05-10 00:00，但相应记录在 7 月更新，且它指向的 arXiv 稿件在本窗只是
投稿而非公开。该字段最多证明后来目录如何展示 family，不能支持 05-10 的技术结论或评分。

### Books Decision

本窗没有候选，因而没有可执行的命题增量，也没有 Books queue。旧 29 项写回记录是否在 Books 中存在，
不改变其不能归属 05-10 的事实；这些材料必须先按真实公开日恢复 Source Family owner，再由对应日期重新判断
Evidence 与 Books，不允许用已有 Books 文本倒推本日报完成。

## 5. 缺口与下一步

- **独立复核：** 已由非作者检查窗口换算、arXiv cadence、ERNIE 时间、Seed 回填边界、空候选判断与旧材料隔离。
- **终态保留项 / Coverage limitation：** OpenAI、Google AI、Meta、Qwen、Moonshot 与 MiMo Blog 未恢复
  可证明本窗全站完整性的官方历史日级分页；它们不支持正面证据、Books 或无遗漏断言，也不阻止已确定来源的
  日期与候选判断。Anthropic 当前嵌入式列表可排除已列事件落窗，但同样不扩张为全站零遗漏保证。
- **定点重开条件：** 若取得上述来源覆盖本窗的官方归档快照、带可靠发布时间的历史索引，或可唯一定位到本窗的
  原始发布链接，只重开对应来源与 Source Family。
- **旧队列恢复条件：** 旧 436/57/29 cohort 只在每个 family 的 arXiv scheduled announcement 或其他独立
  官方首次公开日得到确认后，迁回真实 owner Daily；不在 05-10 内继续全文审查或写 Books。

本次归属纠错详见 [V3 Owner Reconciliation](../_sources/daily-20260510/V3_OWNER_RECONCILIATION.md)。
独立终审与身份守恒复算详见 [V3 Independent Final Audit](../_sources/daily-20260510/V3_INDEPENDENT_FINAL_AUDIT.md)。

## 6. 复核

复核者：`fresh-context:may10-independent-gate-20260914`（未参与 V3 作者重建）

结论：通过

独立复核确认窗口为左闭右开的北京时间 24 小时区间；arXiv 在窗内没有 scheduled announcement，ERNIE 5.1
与 Seed `2605.09233` 均被正确排除。旧 436/57/29 cohort 的身份数量守恒、历史文件保留且已被明确 supersede，
不会再作为 05-10 的 Evidence 或 Books queue。复核同时修正了“全来源候选为 0”的过强表述：完成状态只表示
已核实来源和终态受限来源都得到安全处置，不表示动态历史入口证明绝对零遗漏。机器校验只作为格式证据。
