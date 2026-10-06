# 当前日期字段与包络

执行：2026-10-04；当前 curl/Node fetch 取得各家族 DataCite exact DOI；下列 submitted 仅用于最早可公告排程，registered 仅最迟上界，不是实际公开时刻。官方规则：https://info.arxiv.org/help/availability.html （ID/DOI在公告时才赋值；Eastern Mon14–Tue14→Tue20，可能延迟不提前）。只有提交在2026-02-09T19:00Z至2026-02-10T19:00Z间且登记在本窗的，推定 arXiv 首公开在 [2026-02-11T01:00Z, registered+1second)，完全落本窗。更早提交者不能仅靠本包络确认归属，需官方批次或更早公开佐证。尚需各拟入选项轻查原始event page的先行公开/纠错信号，日期包络不免除版本身份核验。

API模板：https://api.datacite.org/dois/10.48550/arxiv.<id>

```text
2602.09297	{"submitted":{"date":"2026-02-10T00:27:45Z","dateType":"Submitted","dateInformation":"v1"},"created":"2026-02-11T03:00:54.000Z","registered":"2026-02-11T03:00:55.000Z","url":"https://arxiv.org/abs/2602.09297"}
2602.09725	{"submitted":{"date":"2026-02-10T12:29:02Z","dateType":"Submitted","dateInformation":"v1"},"created":"2026-02-11T03:11:11.000Z","registered":"2026-02-11T03:11:11.000Z","url":"https://arxiv.org/abs/2602.09725"}
2602.09578	{"submitted":{"date":"2026-02-10T09:27:03Z","dateType":"Submitted","dateInformation":"v1"},"created":"2026-02-11T03:07:35.000Z","registered":"2026-02-11T03:07:36.000Z","url":"https://arxiv.org/abs/2602.09578"}
2602.10090	{"submitted":{"date":"2026-02-10T18:55:41Z","dateType":"Submitted","dateInformation":"v1"},"created":"2026-02-11T03:19:53.000Z","registered":"2026-02-11T03:19:54.000Z","url":"https://arxiv.org/abs/2602.10090"}
2602.09591	{"submitted":{"date":"2026-02-10T09:45:42Z","dateType":"Submitted","dateInformation":"v1"},"created":"2026-02-11T03:07:54.000Z","registered":"2026-02-11T03:07:54.000Z","url":"https://arxiv.org/abs/2602.09591"}
2602.09598	{"submitted":{"date":"2026-02-10T09:50:24Z","dateType":"Submitted","dateInformation":"v1"},"created":"2026-02-11T03:08:04.000Z","registered":"2026-02-11T03:08:05.000Z","url":"https://arxiv.org/abs/2602.09598"}
2602.09345	{"submitted":{"date":"2026-02-10T02:37:42Z","dateType":"Submitted","dateInformation":"v1"},"created":"2026-02-11T03:02:03.000Z","registered":"2026-02-11T03:02:04.000Z","url":"https://arxiv.org/abs/2602.09345"}
2602.09501	{"submitted":{"date":"2026-02-10T07:56:46Z","dateType":"Submitted","dateInformation":"v1"},"created":"2026-02-11T03:05:44.000Z","registered":"2026-02-11T03:05:45.000Z","url":"https://arxiv.org/abs/2602.09501"}
2602.09268	{"submitted":{"date":"2026-02-09T23:06:58Z","dateType":"Submitted","dateInformation":"v1"},"created":"2026-02-11T03:00:11.000Z","registered":"2026-02-11T03:00:11.000Z","url":"https://arxiv.org/abs/2602.09268"}
2602.09138	{"submitted":{"date":"2026-02-09T19:36:16Z","dateType":"Submitted","dateInformation":"v1"},"created":"2026-02-11T02:56:58.000Z","registered":"2026-02-11T02:56:59.000Z","url":"https://arxiv.org/abs/2602.09138"}
2602.09305	{"submitted":{"date":"2026-02-10T00:45:24Z","dateType":"Submitted","dateInformation":"v1"},"created":"2026-02-11T03:01:06.000Z","registered":"2026-02-11T03:01:07.000Z","url":"https://arxiv.org/abs/2602.09305"}
2602.09937	{"submitted":{"date":"2026-02-10T16:14:05Z","dateType":"Submitted","dateInformation":"v1"},"created":"2026-02-11T03:16:19.000Z","registered":"2026-02-11T03:16:19.000Z","url":"https://arxiv.org/abs/2602.09937"}
2602.09063	{"submitted":{"date":"2026-02-09T03:20:31Z","dateType":"Submitted","dateInformation":"v1"},"created":"2026-02-11T02:55:05.000Z","registered":"2026-02-11T02:55:05.000Z","url":"https://arxiv.org/abs/2602.09063"}
2602.09109	{"submitted":{"date":"2026-02-09T19:01:13Z","dateType":"Submitted","dateInformation":"v1"},"created":"2026-02-11T02:56:14.000Z","registered":"2026-02-11T02:56:15.000Z","url":"https://arxiv.org/abs/2602.09109"}
2602.09430	{"submitted":{"date":"2026-02-10T05:50:19Z","dateType":"Submitted","dateInformation":"v1"},"created":"2026-02-11T03:04:03.000Z","registered":"2026-02-11T03:04:04.000Z","url":"https://arxiv.org/abs/2602.09430"}
2602.09341	{"submitted":{"date":"2026-02-10T02:24:53Z","dateType":"Submitted","dateInformation":"v1"},"created":"2026-02-11T03:01:57.000Z","registered":"2026-02-11T03:01:58.000Z","url":"https://arxiv.org/abs/2602.09341"}
2602.09051	{"submitted":{"date":"2026-02-06T21:08:33Z","dateType":"Submitted","dateInformation":"v1"},"created":"2026-02-11T02:54:46.000Z","registered":"2026-02-11T02:54:47.000Z","url":"https://arxiv.org/abs/2602.09051"}
2602.09038	{"submitted":{"date":"2026-01-30T07:03:18Z","dateType":"Submitted","dateInformation":"v1"},"created":"2026-02-11T02:54:26.000Z","registered":"2026-02-11T02:54:27.000Z","url":"https://arxiv.org/abs/2602.09038"}
2602.09369	{"submitted":{"date":"2026-02-10T03:20:06Z","dateType":"Submitted","dateInformation":"v1"},"created":"2026-02-11T03:02:38.000Z","registered":"2026-02-11T03:02:38.000Z","url":"https://arxiv.org/abs/2602.09369"}
2602.09316	{"submitted":{"date":"2026-02-10T01:24:28Z","dateType":"Submitted","dateInformation":"v1"},"created":"2026-02-11T03:01:22.000Z","registered":"2026-02-11T03:01:23.000Z","url":"https://arxiv.org/abs/2602.09316"}
2602.09080	{"submitted":{"date":"2026-02-09T17:58:23Z","dateType":"Submitted","dateInformation":"v1"},"created":"2026-02-11T02:55:30.000Z","registered":"2026-02-11T02:55:31.000Z","url":"https://arxiv.org/abs/2602.09080"}
2602.09214	{"submitted":{"date":"2026-02-09T21:37:09Z","dateType":"Submitted","dateInformation":"v1"},"created":"2026-02-11T02:58:48.000Z","registered":"2026-02-11T02:58:49.000Z","url":"https://arxiv.org/abs/2602.09214"}
2602.09173	{"submitted":{"date":"2026-02-09T20:27:52Z","dateType":"Submitted","dateInformation":"v1"},"created":"2026-02-11T02:57:48.000Z","registered":"2026-02-11T02:57:48.000Z","url":"https://arxiv.org/abs/2602.09173"}
2602.09323	{"submitted":{"date":"2026-02-10T01:31:30Z","dateType":"Submitted","dateInformation":"v1"},"created":"2026-02-11T03:01:32.000Z","registered":"2026-02-11T03:01:33.000Z","url":"https://arxiv.org/abs/2602.09323"}
2602.09372	{"submitted":{"date":"2026-02-10T03:21:42Z","dateType":"Submitted","dateInformation":"v1"},"created":"2026-02-11T03:02:42.000Z","registered":"2026-02-11T03:02:43.000Z","url":"https://arxiv.org/abs/2602.09372"}
2602.09375	{"submitted":{"date":"2026-02-10T03:35:52Z","dateType":"Submitted","dateInformation":"v1"},"created":"2026-02-11T03:02:46.000Z","registered":"2026-02-11T03:02:47.000Z","url":"https://arxiv.org/abs/2602.09375"}
2602.09434	{"submitted":{"date":"2026-02-10T05:57:35Z","dateType":"Submitted","dateInformation":"v1"},"created":"2026-02-11T03:04:09.000Z","registered":"2026-02-11T03:04:10.000Z","url":"https://arxiv.org/abs/2602.09434"}
2602.09483	{"submitted":{"date":"2026-02-10T07:26:56Z","dateType":"Submitted","dateInformation":"v1"},"created":"2026-02-11T03:05:19.000Z","registered":"2026-02-11T03:05:19.000Z","url":"https://arxiv.org/abs/2602.09483"}
2602.09472	{"submitted":{"date":"2026-02-10T07:11:36Z","dateType":"Submitted","dateInformation":"v1"},"created":"2026-02-11T03:05:02.000Z","registered":"2026-02-11T03:05:03.000Z","url":"https://arxiv.org/abs/2602.09472"}
2602.09383	{"submitted":{"date":"2026-02-10T03:51:03Z","dateType":"Submitted","dateInformation":"v1"},"created":"2026-02-11T03:02:57.000Z","registered":"2026-02-11T03:02:58.000Z","url":"https://arxiv.org/abs/2602.09383"}
2602.09433	{"submitted":{"date":"2026-02-10T05:57:30Z","dateType":"Submitted","dateInformation":"v1"},"created":"2026-02-11T03:04:07.000Z","registered":"2026-02-11T03:04:08.000Z","url":"https://arxiv.org/abs/2602.09433"}
2602.09517	{"submitted":{"date":"2026-02-10T08:20:26Z","dateType":"Submitted","dateInformation":"v1"},"created":"2026-02-11T03:06:08.000Z","registered":"2026-02-11T03:06:08.000Z","url":"https://arxiv.org/abs/2602.09517"}
2602.09719	{"submitted":{"date":"2026-02-10T12:22:14Z","dateType":"Submitted","dateInformation":"v1"},"created":"2026-02-11T03:11:00.000Z","registered":"2026-02-11T03:11:01.000Z","url":"https://arxiv.org/abs/2602.09719"}
2602.09528	{"submitted":{"date":"2026-02-10T08:36:40Z","dateType":"Submitted","dateInformation":"v1"},"created":"2026-02-11T03:06:23.000Z","registered":"2026-02-11T03:06:24.000Z","url":"https://arxiv.org/abs/2602.09528"}
2602.09555	{"submitted":{"date":"2026-02-10T09:05:07Z","dateType":"Submitted","dateInformation":"v1"},"created":"2026-02-11T03:07:02.000Z","registered":"2026-02-11T03:07:03.000Z","url":"https://arxiv.org/abs/2602.09555"}
2602.09574	{"submitted":{"date":"2026-02-10T09:23:26Z","dateType":"Submitted","dateInformation":"v1"},"created":"2026-02-11T03:07:29.000Z","registered":"2026-02-11T03:07:30.000Z","url":"https://arxiv.org/abs/2602.09574"}
2602.09639	{"submitted":{"date":"2026-02-10T10:38:16Z","dateType":"Submitted","dateInformation":"v1"},"created":"2026-02-11T03:09:04.000Z","registered":"2026-02-11T03:09:04.000Z","url":"https://arxiv.org/abs/2602.09639"}
2602.09651	{"submitted":{"date":"2026-02-10T10:56:46Z","dateType":"Submitted","dateInformation":"v1"},"created":"2026-02-11T03:09:20.000Z","registered":"2026-02-11T03:09:21.000Z","url":"https://arxiv.org/abs/2602.09651"}
2602.09657	{"submitted":{"date":"2026-02-10T11:08:07Z","dateType":"Submitted","dateInformation":"v1"},"created":"2026-02-11T03:09:31.000Z","registered":"2026-02-11T03:09:31.000Z","url":"https://arxiv.org/abs/2602.09657"}
2602.09629	{"submitted":{"date":"2026-02-10T10:17:25Z","dateType":"Submitted","dateInformation":"v1"},"created":"2026-02-11T03:08:49.000Z","registered":"2026-02-11T03:08:50.000Z","url":"https://arxiv.org/abs/2602.09629"}
2602.09789	{"submitted":{"date":"2026-02-10T13:49:08Z","dateType":"Submitted","dateInformation":"v1"},"created":"2026-02-11T03:12:43.000Z","registered":"2026-02-11T03:12:44.000Z","url":"https://arxiv.org/abs/2602.09789"}
2602.09825	{"submitted":{"date":"2026-02-10T14:33:24Z","dateType":"Submitted","dateInformation":"v1"},"created":"2026-02-11T03:13:38.000Z","registered":"2026-02-11T03:13:38.000Z","url":"https://arxiv.org/abs/2602.09825"}
2602.09924	{"submitted":{"date":"2026-02-10T15:57:00Z","dateType":"Submitted","dateInformation":"v1"},"created":"2026-02-11T03:16:00.000Z","registered":"2026-02-11T03:16:01.000Z","url":"https://arxiv.org/abs/2602.09924"}
2602.09849	{"submitted":{"date":"2026-02-10T14:54:01Z","dateType":"Submitted","dateInformation":"v1"},"created":"2026-02-11T03:14:12.000Z","registered":"2026-02-11T03:14:13.000Z","url":"https://arxiv.org/abs/2602.09849"}
2602.09856	{"submitted":{"date":"2026-02-10T14:56:19Z","dateType":"Submitted","dateInformation":"v1"},"created":"2026-02-11T03:14:23.000Z","registered":"2026-02-11T03:14:23.000Z","url":"https://arxiv.org/abs/2602.09856"}
2602.09883	{"submitted":{"date":"2026-02-10T15:23:18Z","dateType":"Submitted","dateInformation":"v1"},"created":"2026-02-11T03:15:02.000Z","registered":"2026-02-11T03:15:03.000Z","url":"https://arxiv.org/abs/2602.09883"}
2602.09902	{"submitted":{"date":"2026-02-10T15:39:31Z","dateType":"Submitted","dateInformation":"v1"},"created":"2026-02-11T03:15:29.000Z","registered":"2026-02-11T03:15:29.000Z","url":"https://arxiv.org/abs/2602.09902"}
2602.09878	{"submitted":{"date":"2026-02-10T15:19:17Z","dateType":"Submitted","dateInformation":"v1"},"created":"2026-02-11T03:14:55.000Z","registered":"2026-02-11T03:14:55.000Z","url":"https://arxiv.org/abs/2602.09878"}
2602.09944	{"submitted":{"date":"2026-02-10T16:29:09Z","dateType":"Submitted","dateInformation":"v1"},"created":"2026-02-11T03:16:29.000Z","registered":"2026-02-11T03:16:29.000Z","url":"https://arxiv.org/abs/2602.09944"}
2602.10097	{"submitted":{"date":"2026-02-10T18:57:53Z","dateType":"Submitted","dateInformation":"v1"},"created":"2026-02-11T03:20:04.000Z","registered":"2026-02-11T03:20:04.000Z","url":"https://arxiv.org/abs/2602.10097"}
2602.09934	{"submitted":{"date":"2026-02-10T16:08:19Z","dateType":"Submitted","dateInformation":"v1"},"created":"2026-02-11T03:16:15.000Z","registered":"2026-02-11T03:16:15.000Z","url":"https://arxiv.org/abs/2602.09934"}
2602.10044	{"submitted":{"date":"2026-02-10T18:11:00Z","dateType":"Submitted","dateInformation":"v1"},"created":"2026-02-11T03:18:49.000Z","registered":"2026-02-11T03:18:49.000Z","url":"https://arxiv.org/abs/2602.10044"}
2602.10019	{"submitted":{"date":"2026-02-10T17:40:39Z","dateType":"Submitted","dateInformation":"v1"},"created":"2026-02-11T03:18:14.000Z","registered":"2026-02-11T03:18:14.000Z","url":"https://arxiv.org/abs/2602.10019"}
2602.10004	{"submitted":{"date":"2026-02-10T17:27:26Z","dateType":"Submitted","dateInformation":"v1"},"created":"2026-02-11T03:17:53.000Z","registered":"2026-02-11T03:17:54.000Z","url":"https://arxiv.org/abs/2602.10004"}
2602.10021	{"submitted":{"date":"2026-02-10T17:42:31Z","dateType":"Submitted","dateInformation":"v1"},"created":"2026-02-11T03:18:17.000Z","registered":"2026-02-11T03:18:17.000Z","url":"https://arxiv.org/abs/2602.10021"}
2602.09947	{"submitted":{"date":"2026-02-10T16:33:40Z","dateType":"Submitted","dateInformation":"v1"},"created":"2026-02-11T03:16:33.000Z","registered":"2026-02-11T03:16:34.000Z","url":"https://arxiv.org/abs/2602.09947"}
2602.10098	{"submitted":{"date":"2026-02-10T18:58:01Z","dateType":"Submitted","dateInformation":"v1"},"created":"2026-02-11T03:20:05.000Z","registered":"2026-02-11T03:20:06.000Z","url":"https://arxiv.org/abs/2602.10098"}
2602.10099	{"submitted":{"date":"2026-02-10T18:58:04Z","dateType":"Submitted","dateInformation":"v1"},"created":"2026-02-11T03:20:06.000Z","registered":"2026-02-11T03:20:07.000Z","url":"https://arxiv.org/abs/2602.10099"}
2602.10104	{"submitted":{"date":"2026-02-10T18:58:41Z","dateType":"Submitted","dateInformation":"v1"},"created":"2026-02-11T03:20:14.000Z","registered":"2026-02-11T03:20:15.000Z","url":"https://arxiv.org/abs/2602.10104"}
2602.10109	{"submitted":{"date":"2026-02-10T18:59:17Z","dateType":"Submitted","dateInformation":"v1"},"created":"2026-02-11T03:20:21.000Z","registered":"2026-02-11T03:20:22.000Z","url":"https://arxiv.org/abs/2602.10109"}
2602.10116	{"submitted":{"date":"2026-02-10T18:59:55Z","dateType":"Submitted","dateInformation":"v1"},"created":"2026-02-11T03:20:31.000Z","registered":"2026-02-11T03:20:32.000Z","url":"https://arxiv.org/abs/2602.10116"}
```

## 当前官方事件页轻查（2026-10-04）

实际请求 `https://arxiv.org/abs/2602.<ID>v1` 的 citation_title、Comments 与 Submission history，已核23个实际采用/已准备家族：09578/09725/09345/09591/09598/09501/09297/09268/09138/09341/09937/09430/10090/09173/09214/09316/09369/09375/09383/09434/09483/09517/09528。题名/ID及v1提交时间与上方DOI家族对应，Sci-VLA题名保留v1，未继承后发AtomBridge；无已出现的撤回/勘误/先行独立正文公开说明。没有用未标记证明全站无信号。

版本历史中09591v2提交2026-02-11T12:19:33Z、AWMv2提交2026-02-11T18:20:25Z，依据官方排程最早正文公开不早于本窗终点；09316v2为2026-02-11T21:20:04Z更晚。09369v2提交2026-02-12T01:42:39Z、KVFetcher v2提交2026-02-12T03:30:35Z自身已窗外，其他列出的后续版本皆更晚；只有版本号、无影响本窗采用的纠错说明，不比较全版本。当前09173仅一个v1，compiled差异只为固定采用PDF所必需。剩余拟入选轻查仍普通待办。

### 剩余22拟采用家族原始事件页轻查（2026-10-04T11:31+08:00）

实际 GET 精确 `abs/2602.<ID>v1` 的 citation_title/Submission history 与现成 withdrawn/retracted/erratum/corrigendum/correction 信号，22项全200：09555/09574/09639/09651/09719/09789/09825/09849/09856/09878/09883/09902/09924/09934/10004/10021/10044/10097/10098/10099/10104/10109。v1 title/ID/submitted 与前述 DOI 家族相符，信号匹配为空不作为全站无纠错的证明。45 working 原始事件页身份轻查至此完成，不改变 DOI 登记只作最迟上界的角色，也不授尚未独立复核的日期 Gate。

新增 history 原值：09555v2 `2026-02-11T03:38:52Z`、BagelVLA09849v2 `2026-02-11T03:54:17Z`；它们在v1登记之后且依下一官方公告排程最早公开不早于本窗终点。其他后续history为09574v2 `2026-06-04T09:49:18Z`、09639v2 `2026-06-09T16:50:11Z`、09651v2 `2026-06-01T16:35:54Z`、09789v2 `2026-02-26T07:55:28Z`、09878v2 `2026-05-26T17:06:15Z`、09924v2 `2026-03-16T20:10:33Z`、10098v2 `2026-02-14T03:00:50Z`、10099v2 `2026-07-03T15:19:24Z`、10104v2 `2026-05-26T06:14:19Z`，其余当前仅v1。仅版本号无影响本窗采用的纠错说明，不比较全版本或采用后来正文。

### UniT 日期保留（来源有限发现，不计working45）

Meta官方页面 `https://ai.meta.com/research/publications/unit-unified-multimodal-chain-of-thought-test-time-scaling/` 日期原值 `February 11, 2026`，未给时区/时刻；完整题摘与arXiv2602.12279v1身份匹配，但arXiv v1 submitted `Thu, 12 Feb 2026 18:59:49 UTC` 晚于本窗，仅此不能推翻Meta先行正文的可能性，也不能将其改归当前日。Meta直连PDF当前web click internal error。保留潜在短训练轨迹→长序列推理与跨生成/理解迁移的准入线索；需要Meta Feb11正文首次公开时刻或覆盖整个可能范围的官方包络，取得后仅重开此家族。date-only相交未确认落窗，不采用为正面证据或Books；不为此查全部CVPR/Meta历年库。

## 有界新增13家族必要日期原字段

2026-10-04实际请求13个精确DataCite DOI均HTTP200；下列原字段完整保留，Updated不称实际公开时刻。v1 submitted均落同Mon14–Tue14 EST排程批次，registered只作最迟上界，与上文相同包络方法；完整v1身份/history在V3_BOUND_TITLE_FULL_AB.md。09170的v1 Updated Feb18不反证早先公开：registered Feb11已是存在上界，但须留其原字段不更改；下方现成event-page轻检已完成，独立日期Gate待核。

```text
{"id":"09448","status":200,"dates":[{"date":"2026-02-10T06:33:10Z","dateType":"Submitted","dateInformation":"v1"},{"date":"2026-02-11T01:29:54Z","dateType":"Updated","dateInformation":"v1"},{"date":"2026-02-24T15:35:33Z","dateType":"Submitted","dateInformation":"v2"},{"date":"2026-02-25T01:56:00Z","dateType":"Updated","dateInformation":"v2"},{"date":"2026-02-26T08:33:54Z","dateType":"Submitted","dateInformation":"v3"},{"date":"2026-02-27T01:32:37Z","dateType":"Updated","dateInformation":"v3"},{"date":"2026-03-16T12:57:55Z","dateType":"Submitted","dateInformation":"v4"},{"date":"2026-03-17T02:15:24Z","dateType":"Updated","dateInformation":"v4"},{"date":"2026-02","dateType":"Available","dateInformation":"v1"},{"date":"2026","dateType":"Issued"}],"created":"2026-02-11T03:04:29.000Z","registered":"2026-02-11T03:04:30.000Z","url":"https://arxiv.org/abs/2602.09448"}
{"id":"09616","status":200,"dates":[{"date":"2026-02-10T10:04:55Z","dateType":"Submitted","dateInformation":"v1"},{"date":"2026-02-11T01:41:33Z","dateType":"Updated","dateInformation":"v1"},{"date":"2026-07-15T08:11:18Z","dateType":"Submitted","dateInformation":"v2"},{"date":"2026-07-16T00:30:49Z","dateType":"Updated","dateInformation":"v2"},{"date":"2026-02","dateType":"Available","dateInformation":"v1"}],"created":"2026-02-11T03:08:30.000Z","registered":"2026-02-11T03:08:31.000Z","url":"https://arxiv.org/abs/2602.09616"}
{"id":"09229","status":200,"dates":[{"date":"2026-02-09T21:53:23Z","dateType":"Submitted","dateInformation":"v1"},{"date":"2026-02-11T01:10:05Z","dateType":"Updated","dateInformation":"v1"},{"date":"2026-03-05T12:45:26Z","dateType":"Submitted","dateInformation":"v2"},{"date":"2026-03-06T01:53:50Z","dateType":"Updated","dateInformation":"v2"},{"date":"2026-05-07T19:21:00Z","dateType":"Submitted","dateInformation":"v3"},{"date":"2026-05-11T00:09:23Z","dateType":"Updated","dateInformation":"v3"},{"date":"2026-02","dateType":"Available","dateInformation":"v1"},{"date":"2026","dateType":"Issued"}],"created":"2026-02-11T02:59:11.000Z","registered":"2026-02-11T02:59:11.000Z","url":"https://arxiv.org/abs/2602.09229"}
{"id":"09764","status":200,"dates":[{"date":"2026-02-10T13:24:06Z","dateType":"Submitted","dateInformation":"v1"},{"date":"2026-02-11T01:51:20Z","dateType":"Updated","dateInformation":"v1"},{"date":"2026-06-15T12:48:13Z","dateType":"Submitted","dateInformation":"v2"},{"date":"2026-06-16T01:44:19Z","dateType":"Updated","dateInformation":"v2"},{"date":"2026-02","dateType":"Available","dateInformation":"v1"},{"date":"2026","dateType":"Issued"}],"created":"2026-02-11T03:12:07.000Z","registered":"2026-02-11T03:12:08.000Z","url":"https://arxiv.org/abs/2602.09764"}
{"id":"09170","status":200,"dates":[{"date":"2026-02-09T20:22:33Z","dateType":"Submitted","dateInformation":"v1"},{"date":"2026-02-18T11:53:38Z","dateType":"Updated","dateInformation":"v1"},{"date":"2026-02","dateType":"Available","dateInformation":"v1"},{"date":"2026","dateType":"Issued"}],"created":"2026-02-11T02:57:43.000Z","registered":"2026-02-11T02:57:44.000Z","url":"https://arxiv.org/abs/2602.09170"}
{"id":"09276","status":200,"dates":[{"date":"2026-02-09T23:32:12Z","dateType":"Submitted","dateInformation":"v1"},{"date":"2026-02-11T01:13:16Z","dateType":"Updated","dateInformation":"v1"},{"date":"2026-05-28T19:23:27Z","dateType":"Submitted","dateInformation":"v2"},{"date":"2026-06-01T00:05:26Z","dateType":"Updated","dateInformation":"v2"},{"date":"2026-02","dateType":"Available","dateInformation":"v1"},{"date":"2026","dateType":"Issued"}],"created":"2026-02-11T03:00:22.000Z","registered":"2026-02-11T03:00:23.000Z","url":"https://arxiv.org/abs/2602.09276"}
{"id":"09331","status":200,"dates":[{"date":"2026-02-10T01:57:02Z","dateType":"Submitted","dateInformation":"v1"},{"date":"2026-02-11T01:17:37Z","dateType":"Updated","dateInformation":"v1"},{"date":"2026-02","dateType":"Available","dateInformation":"v1"},{"date":"2026","dateType":"Issued"}],"created":"2026-02-11T03:01:43.000Z","registered":"2026-02-11T03:01:44.000Z","url":"https://arxiv.org/abs/2602.09331"}
{"id":"09394","status":200,"dates":[{"date":"2026-02-10T04:02:29Z","dateType":"Submitted","dateInformation":"v1"},{"date":"2026-02-11T01:23:22Z","dateType":"Updated","dateInformation":"v1"},{"date":"2026-02-13T00:34:46Z","dateType":"Submitted","dateInformation":"v2"},{"date":"2026-02-16T01:12:16Z","dateType":"Updated","dateInformation":"v2"},{"date":"2026-02","dateType":"Available","dateInformation":"v1"},{"date":"2026","dateType":"Issued"}],"created":"2026-02-11T03:03:13.000Z","registered":"2026-02-11T03:03:13.000Z","url":"https://arxiv.org/abs/2602.09394"}
{"id":"09842","status":200,"dates":[{"date":"2026-02-10T14:46:14Z","dateType":"Submitted","dateInformation":"v1"},{"date":"2026-02-11T01:57:06Z","dateType":"Updated","dateInformation":"v1"},{"date":"2026-05-26T14:40:02Z","dateType":"Submitted","dateInformation":"v2"},{"date":"2026-05-27T01:05:40Z","dateType":"Updated","dateInformation":"v2"},{"date":"2026-02","dateType":"Available","dateInformation":"v1"},{"date":"2026","dateType":"Issued"}],"created":"2026-02-11T03:14:02.000Z","registered":"2026-02-11T03:14:03.000Z","url":"https://arxiv.org/abs/2602.09842"}
{"id":"09891","status":200,"dates":[{"date":"2026-02-10T15:30:12Z","dateType":"Submitted","dateInformation":"v1"},{"date":"2026-02-11T02:00:46Z","dateType":"Updated","dateInformation":"v1"},{"date":"2026-02","dateType":"Available","dateInformation":"v1"},{"date":"2026","dateType":"Issued"}],"created":"2026-02-11T03:15:14.000Z","registered":"2026-02-11T03:15:14.000Z","url":"https://arxiv.org/abs/2602.09891"}
{"id":"09983","status":200,"dates":[{"date":"2026-02-10T17:10:05Z","dateType":"Submitted","dateInformation":"v1"},{"date":"2026-02-11T02:07:15Z","dateType":"Updated","dateInformation":"v1"},{"date":"2026-02","dateType":"Available","dateInformation":"v1"},{"date":"2026","dateType":"Issued"}],"created":"2026-02-11T03:17:24.000Z","registered":"2026-02-11T03:17:25.000Z","url":"https://arxiv.org/abs/2602.09983"}
{"id":"10058","status":200,"dates":[{"date":"2026-02-10T18:25:04Z","dateType":"Submitted","dateInformation":"v1"},{"date":"2026-02-11T02:11:12Z","dateType":"Updated","dateInformation":"v1"},{"date":"2026-02-15T20:31:32Z","dateType":"Submitted","dateInformation":"v2"},{"date":"2026-02-17T02:06:20Z","dateType":"Updated","dateInformation":"v2"},{"date":"2026-02","dateType":"Available","dateInformation":"v1"},{"date":"2026","dateType":"Issued"}],"created":"2026-02-11T03:19:08.000Z","registered":"2026-02-11T03:19:09.000Z","url":"https://arxiv.org/abs/2602.10058"}
{"id":"09533","status":200,"dates":[{"date":"2026-02-10T08:45:30Z","dateType":"Submitted","dateInformation":"v1"},{"date":"2026-02-11T01:36:17Z","dateType":"Updated","dateInformation":"v1"},{"date":"2026-06-10T06:12:57Z","dateType":"Submitted","dateInformation":"v2"},{"date":"2026-06-11T00:30:18Z","dateType":"Updated","dateInformation":"v2"},{"date":"2026-02","dateType":"Available","dateInformation":"v1"},{"date":"2026","dateType":"Issued"}],"created":"2026-02-11T03:06:30.000Z","registered":"2026-02-11T03:06:31.000Z","url":"https://arxiv.org/abs/2602.09533"}
```

### 新13精确event-page身份与公开包络轻检

本轮 actual GET `https://arxiv.org/abs/2602.<ID>v1`，13项全HTTP200。citation_title及Submission history与上述DOI最终ID/v1提交时间对应；现成withdrawn/retracted/erratum/correction/replacement匹配均空，不以无标记证明全站无信号。后版history仅作窗口排程判断，不读后版正文或全版本diff；未见该家族更早独立正文公开说明。09229 abs citation_title为当前家族的 Beyond the Unit Hypersphere: Embedding Magnitude in Contrastive Learning，采用精确v1 HTML标题 On the Role of Embedding Magnitude in Contrastive Learning，不把后改标题当机制版本。

以下均推定含起不含终，原始Submitted/registered精度见上方UTC字段，+1second只用于覆盖登记所示秒的保守上界，不补造真实发布时间。下界统一北京时间2026-02-11T09:00:00+08:00（标准公开排程），全部上界也在该日，因而完整范围落窗；独立日期复核尚未授权。

| 精确v1 ID | Submission history v1 UTC | registered最迟上界+1秒，北京时间 | 后版最早公开排程及信号 |
| --- | --- | --- | --- |
| 09448 | 2026-02-10T06:33:10Z | 2026-02-11T11:04:31+08:00 | v2 Feb24，无现成纠错/撤回信号 |
| 09616 | 2026-02-10T10:04:55Z | 2026-02-11T11:08:32+08:00 | v2 Jul15，无现成信号 |
| 09229 | 2026-02-09T21:53:23Z | 2026-02-11T10:59:12+08:00 | v2 Mar5/v3 May7，标题差异不当新增 |
| 09764 | 2026-02-10T13:24:06Z | 2026-02-11T11:12:09+08:00 | v2 Jun15，无现成信号 |
| 09170 | 2026-02-09T20:22:33Z | 2026-02-11T10:57:45+08:00 | 仅v1；Updated Feb18不当真实首公开 |
| 09276 | 2026-02-09T23:32:12Z | 2026-02-11T11:00:24+08:00 | v2 May28，无现成信号 |
| 09331 | 2026-02-10T01:57:02Z | 2026-02-11T11:01:45+08:00 | 仅v1，无现成信号 |
| 09394 | 2026-02-10T04:02:29Z | 2026-02-11T11:03:14+08:00 | v2 Feb13，晚于本窗 |
| 09842 | 2026-02-10T14:46:14Z | 2026-02-11T11:14:04+08:00 | v2 May26，无现成信号 |
| 09891 | 2026-02-10T15:30:12Z | 2026-02-11T11:15:15+08:00 | 仅v1，无现成信号 |
| 09983 | 2026-02-10T17:10:05Z | 2026-02-11T11:17:26+08:00 | 仅v1，无现成信号 |
| 10058 | 2026-02-10T18:25:04Z | 2026-02-11T11:19:10+08:00 | v2 Feb15，晚于本窗 |
| 09533 | 2026-02-10T08:45:30Z | 2026-02-11T11:06:32+08:00 | v2 Jun10，无现成信号 |
