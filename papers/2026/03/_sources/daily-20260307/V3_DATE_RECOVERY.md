# 03/07 具名日期恢复：复合公开区间

本文件覆盖此前27项“DataCite+routine schedule不能支持任何落窗range”的判断错误，不覆盖其他来源或扩大候选池。实际检查日期2026-10-01；接口均为 `https://api.datacite.org/dois/10.48550/arXiv.<ID>`，HTTP成功返回。不是DOI created当作公开时刻。

[arXiv官方availability](https://info.arxiv.org/help/availability.html)实际§ID assignments（L173–176）说明最终ID/DOI在公告时分配、不能提前提供；§schedule（L178–186）给出Wednesday14→Thursday14的最早Thursday20 Eastern公告。2026-03-05T04:04～06:34Z提交处于Wednesday23:04～Thursday01:34 EST，最早公开下界为2026-03-06T01:00Z（BJT09:00）。moderation可延迟，因此不把下界宣布成exact。

下面实际响应的state=findable、client=arxiv.content，由arXiv官方ID不可预分配与历史registered时间组合支持该ID在registered时已经公开的上界。registered不是exact publication，也不单独授公开时间；Updated只保留身份信息。对26项March05提交，采用保守半开区间 `2026-03-06T09:00:00+08:00 ～ 2026-03-06T12:00:00+08:00`，整个区间落本日窗口。原值上界实际更紧，保留如下。

AGF2603.04805v1原始Submitted为Feb06；MarchID只限公告月，不能把它的下界替换成Mar06BJT09。它仍未确认完整落窗，具名日期隔离；其余26继续贡献裁决与必要审阅，不因工作量或Books已覆盖退出。

| 精确身份 | v1 Submitted UTC | registered UTC | state / client | 日期处置 |
| --- | --- | --- | --- | --- |
| [2603.04783v1](https://arxiv.org/abs/2603.04783v1) | 2026-03-05T04:04:59Z | 2026-03-06T03:00:59.000Z | findable / arxiv.content | 完全落窗range |
| [2603.04790v1](https://arxiv.org/abs/2603.04790v1) | 2026-03-05T04:12:13Z | 2026-03-06T03:01:10.000Z | findable / arxiv.content | 完全落窗range |
| [2603.04791v1](https://arxiv.org/abs/2603.04791v1) | 2026-03-05T04:13:57Z | 2026-03-06T03:01:12.000Z | findable / arxiv.content | 完全落窗range |
| [2603.04797v1](https://arxiv.org/abs/2603.04797v1) | 2026-03-05T04:28:48Z | 2026-03-06T03:01:20.000Z | findable / arxiv.content | 完全落窗range |
| [2603.04799v1](https://arxiv.org/abs/2603.04799v1) | 2026-03-05T04:37:15Z | 2026-03-06T03:01:23.000Z | findable / arxiv.content | 完全落窗range |
| [2603.04800v1](https://arxiv.org/abs/2603.04800v1) | 2026-03-05T04:41:32Z | 2026-03-06T03:01:25.000Z | findable / arxiv.content | 完全落窗range |
| [2603.04803v1](https://arxiv.org/abs/2603.04803v1) | 2026-03-05T04:45:49Z | 2026-03-06T03:01:29.000Z | findable / arxiv.content | 完全落窗range |
| [2603.04805v1](https://arxiv.org/abs/2603.04805v1) | 2026-02-06T01:51:32Z | 2026-03-06T03:01:32.000Z | findable / arxiv.content | 仍隔离：下界不足 |
| [2603.04814v1](https://arxiv.org/abs/2603.04814v1) | 2026-03-05T05:01:30Z | 2026-03-06T03:01:44.000Z | findable / arxiv.content | 完全落窗range |
| [2603.04816v1](https://arxiv.org/abs/2603.04816v1) | 2026-03-05T05:03:07Z | 2026-03-06T03:01:47.000Z | findable / arxiv.content | 完全落窗range |
| [2603.04817v1](https://arxiv.org/abs/2603.04817v1) | 2026-03-05T05:07:03Z | 2026-03-06T03:01:48.000Z | findable / arxiv.content | 完全落窗range |
| [2603.04819v1](https://arxiv.org/abs/2603.04819v1) | 2026-03-05T05:10:47Z | 2026-03-06T03:01:51.000Z | findable / arxiv.content | 完全落窗range |
| [2603.04820v1](https://arxiv.org/abs/2603.04820v1) | 2026-03-05T05:11:08Z | 2026-03-06T03:01:52.000Z | findable / arxiv.content | 完全落窗range |
| [2603.04822v1](https://arxiv.org/abs/2603.04822v1) | 2026-03-05T05:12:26Z | 2026-03-06T03:01:56.000Z | findable / arxiv.content | 完全落窗range |
| [2603.04827v1](https://arxiv.org/abs/2603.04827v1) | 2026-03-05T05:20:03Z | 2026-03-06T03:02:03.000Z | findable / arxiv.content | 完全落窗range |
| [2603.04828v1](https://arxiv.org/abs/2603.04828v1) | 2026-03-05T05:21:51Z | 2026-03-06T03:02:04.000Z | findable / arxiv.content | 完全落窗range |
| [2603.04831v1](https://arxiv.org/abs/2603.04831v1) | 2026-03-05T05:29:09Z | 2026-03-06T03:02:09.000Z | findable / arxiv.content | 完全落窗range |
| [2603.04836v1](https://arxiv.org/abs/2603.04836v1) | 2026-03-05T05:43:45Z | 2026-03-06T03:02:16.000Z | findable / arxiv.content | 完全落窗range |
| [2603.04837v1](https://arxiv.org/abs/2603.04837v1) | 2026-03-05T05:45:26Z | 2026-03-06T03:02:18.000Z | findable / arxiv.content | 完全落窗range |
| [2603.04839v1](https://arxiv.org/abs/2603.04839v1) | 2026-03-05T05:46:16Z | 2026-03-06T03:02:21.000Z | findable / arxiv.content | 完全落窗range |
| [2603.04846v1](https://arxiv.org/abs/2603.04846v1) | 2026-03-05T06:01:26Z | 2026-03-06T03:02:32.000Z | findable / arxiv.content | 完全落窗range |
| [2603.04847v1](https://arxiv.org/abs/2603.04847v1) | 2026-03-05T06:02:50Z | 2026-03-06T03:02:33.000Z | findable / arxiv.content | 完全落窗range |
| [2603.04848v1](https://arxiv.org/abs/2603.04848v1) | 2026-03-05T06:04:01Z | 2026-03-06T03:02:34.000Z | findable / arxiv.content | 完全落窗range |
| [2603.04851v1](https://arxiv.org/abs/2603.04851v1) | 2026-03-05T06:07:07Z | 2026-03-06T03:02:39.000Z | findable / arxiv.content | 完全落窗range |
| [2603.04852v1](https://arxiv.org/abs/2603.04852v1) | 2026-03-05T06:08:50Z | 2026-03-06T03:02:40.000Z | findable / arxiv.content | 完全落窗range |
| [2603.04857v1](https://arxiv.org/abs/2603.04857v1) | 2026-03-05T06:25:50Z | 2026-03-06T03:02:50.000Z | findable / arxiv.content | 完全落窗range |
| [2603.04859v1](https://arxiv.org/abs/2603.04859v1) | 2026-03-05T06:34:06Z | 2026-03-06T03:02:53.000Z | findable / arxiv.content | 完全落窗range |

恢复接口已执行，不再列为外部故障；26项贡献/必要证据/Books普通作者工作已结束，17准入与9具体关闭见当日报告。Firefox和Codex既有证据处置不受本次错误影响；BrowseComp/card与Descript的相交day-only限制也不受这个arXiv复合证明影响。root非作者日级Gate已通过；本文件不把这些隔离项宣称正面日期证据。
