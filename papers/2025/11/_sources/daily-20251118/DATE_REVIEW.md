# Nov18 Date Review

作者Carver，原25项检查2026-10-04T20:13:46+08:00；Conformal定点增量同步2026-10-04T20:53:35+08:00。现26论文potential的本日DataCite原JSON全部200、原字段实际读完；v1 Submitted与本日exact-v1历史逐项一致，26项/差异0。不把Submitted、Updated、created偷换成public。

## 已核日期与权限

- [OpenAI原RSS](openai-rss.xml)1245items、missing pubDate0。本窗UTC `[2025-11-17T01:00:00Z,2025-11-18T01:00:00Z)`只有Gartner公告1事件，`Mon, 17 Nov 2025 10:00:00 GMT`完全落窗。厂商公告证其publication，不证Gartner评价为独立实验事实。核心拟关闭见[FIRST](FIRST_CALIBRATION_READY.md)。
- [Gemini3本日官方页](google-gemini3.html)JSON-LD `datePublished=2025-11-18T16:00:00+00:00`，BJT19日00:00，窗外；`dateModified=2026-03-19T17:52:32.737752+00:00`非本窗新事件。
- [DeepMind原日期恢复](web-deepmind-dates.json)、[补定位](web-date-recovery.json)：SIMA2 Nov13，TeachingAI Nov11，NorthernIreland teachers Nov10，nature Nov5。日期虽未逐一给时区，但与目标Nov17/18边界相距足够，非本窗首次公告；不将现行Research置顶当新发布，不展开旧report附件。
- [Antigravity原核心](web-date-recovery-last.json)只有`Nov 18, 2025`、没有timezone或clock。不能用Gemini3的16Z时间赋给它；若非作者能核原publication时刻/完全落窗上下界则解hold。当前为第27个potential（26论文+1公告），不正面采用。

## arXiv边界

[本日官方availability](arxiv-availability.html)实际读到moderation可能延迟、identifier在announcement时分配且不能backdate、Sun–Thu20ET/FriSat无公告。DST结束后EST：Sun Nov16 20ET换算BJTNov17 09正好18含起点；Mon Nov17 20ET=BJTNov18 09恰终点排除。**该schedule不能证明某论文真实公告精确时刻**。本日查询的submitted邻域只是发现，不能全批授首公开。

26原JSON中的v1 Submitted/Updated/Available、created与后续版本均保留。含新增Conformal的24项v1 Updated在Nov17 `01:02:54Z～02:01:55Z`、created在Nov17 `02:38:18Z～02:56:37Z`，字段名未注明首公开，不能仅靠二者建立完全落窗下界；这不是说它们必定窗外。若官方历史announcement/作者可核首公开时刻或已知未公开下界+首次可取正文上界完全在窗内，即可采用。

特殊两项：2511.13751 InsideVOLT Submitted Nov13但Updated Nov19 `01:00:54Z`、created Nov19 `02:44:51Z`，Available2025-11；跨截止可能延迟，不授Nov18公开。2601.08833 PD Submitted Nov14但Available2026-01、UpdatedJan15 `01:00:03Z`、createdJan15 `02:31:57Z`；结合identifier-month规则，November arxiv首公告排除成立，别处更早的材料家族首公开未知。不得为此恢复整January日报或迁移本文性能/能耗结论。

## 有限恢复与精确重开

本日[官方定点检索](web-date-recovery.json)11553/10899 announcement、FengHuang与[后两项](web-date-recovery-last.json)13751/10860未恢复原公告；[早期定点检索](web-target-recovery-b.json)两名称查询未有效恢复，保留实际失败范围，不当零命中证据。DataCite只有上列字段，本次不扩大全文/实验/owner队列。

26论文identity（全部v1）：2511.11553、11518、11505、11500、11315、11018、11007、10881、10899、10819、10811、11526、11520、11502、11313、11298、11011、10946、11332、11248、10909、10753、13751、10860、11472及2601.08833；对应`datacite-<ID>.json`和`abs-<ID>v1.html`。每项只请求其原announcement或作者/publisher可核首次公开时区及完全落窗界；收到后仅重开该identity的日期、贡献及必要Evidence，不复扫整窗/整月。

### Conformal最小日期恢复

root独立AB反馈撤销11472范围关闭后，作者仅定点读回[exact-v1原历史](abs-2511.11472v1.html)与新增[DataCite原JSON](datacite-2511.11472.json)：v1 Submitted `2025-11-14T16:42:42Z`、Updated `2025-11-17T01:56:07Z`、Available `2025-11`；created `2025-11-17T02:54:45.000Z`、registered `2025-11-17T02:54:46.000Z`。v2 Submitted `2025-11-17T03:21:34Z`、Updated `2025-11-18T02:20:59Z`不代v1；citation_date/online_date为Nov14日精度且与提交日期一致，也不构成首公开证明。无relatedIdentifiers可恢复原发布。

[具名原日期补检](web-conformal-date-recovery.json)实际只查arxiv公告ID和作者所属/主页域的精确题名，返回空，无可采用原announcement或完全落窗上下界；不把空搜索称零事件。现public hold，缺该ID原首公开公告/可核作者原发布或完全落窗首公开界；按该ID恢复，不读全文实验/理论/owner，不将医学结果采用为临床结论。

确定当窗候选0、未评分、正面Evidence采用0，Books No Change/写入0（非已有覆盖）；这些hold不支持来源无遗漏、实验正确或性能/安全保证。9完整题摘及6标题范围关闭不为无关日期扩请求。27项potential全部日期仍未获落窗证明；[root非作者日级复核](ROOT_INDEPENDENT_REVIEW.md)已实际核原日期、Conformal有限空补检及安全隔离边界，通过本窗终态保留。普通可执行待办0；收到该身份的必要原公告或完全落窗首公开界才定点重开，不扩全部实验/owner或月份。

作者最后同步2026-10-04T21:15:14+08:00，复用root截至2026-10-04T21:10:00+08:00实际日级结论；原日期值、失败及空检索不改写。普通0不表示firstpublic已核；本日终态保留不用于正面证据、不进入Books、不支持Coverage/无遗漏断言或性能/安全保证，仍按上述26论文ID及Antigravity原公告分别定点重开。
