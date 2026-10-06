# Jan09 public interval basis

Actually read official [availability](https://info.arxiv.org/help/availability.html) §§ID assignments/Announcement Schedule (web L170–186): moderation may delay; IDs/DOIs cannot be supplied in advance and are assigned on announcement, no backdating. Tue14ET–Wed14ET earliest scheduled announcement Wed20ET. Also actually read [2025 holiday announcement](https://blog.arxiv.org/2025/11/21/temporary-changes-to-announcement-schedule-due-to-end-of-year-holidays-2025/) L29/L32: Dec30/Jan1 changes do not extend to Jan7/8.

First five exact-v1 submissions all after Jan6T19Z and before Jan7T19Z, so earliest arXiv scheduled announcement Jan7T20ET = Jan8T01Z = Jan8T09BJT. Actual DataCite original fields in DATES_1.json show the real DOI already created on Jan8T02:36–02:39Z. Combined with no advance ID and actual creation, arXiv public interval is inferred as [Jan8T01Z, created+1second); created is an upper bound with second-resolution, not exact public time, and registered can differ by a second. The whole inferred interval lies in Jan09 window; v1 Updated is retained but not treated as independent public proof.

| v1 | inferred arXiv public BJT lower inclusive | exclusive upper |
| --- | --- | --- |
| 2601.03368 | 2026-01-08T09:00:00+08:00 | 2026-01-08T10:36:41+08:00 |
| 2601.03385 | 2026-01-08T09:00:00+08:00 | 2026-01-08T10:37:05+08:00 |
| 2601.03417 | 2026-01-08T09:00:00+08:00 | 2026-01-08T10:37:51+08:00 |
| 2601.03425 | 2026-01-08T09:00:00+08:00 | 2026-01-08T10:38:02+08:00 |
| 2601.03468 | 2026-01-08T09:00:00+08:00 | 2026-01-08T10:39:03+08:00 |

This establishes the arXiv event interval, not absence of earlier author/project publication. Any concrete earlier-public clue must be checked separately before claiming paper first-public. No later ordinary version is automatically an important Jan09 revision. No old-ID revisions zero assertion from submittedDate query.
## 第二批与MiMo身份

原字段 DATES_2.json 实际HTTP200。共同官方公告/无advanceID政策对Jan7 deadline内四项给arXiv公开区间：04071 [Jan8T01Z,Jan8T02:53:30Z)、03511 [Jan8T01Z,Jan8T02:40:03Z)、03782 [Jan8T01Z,Jan8T02:46:35Z)、03542 [Jan8T01Z,Jan8T02:40:54Z)。区间完全落Jan09窗，但较早作者公开仍需已有具体线索定点核；DataCite不是精确first-public。

MiMo2601.02780v1 Submitted Jan6T07:31:47Z与created Jan7T02:41:19Z，说明本窗前已公开上界；目录Jan8日期不改首次归属。v2 Submitted Jan8T05:52:17Z仅发现字段，下一可公告是Jan9T01Z（本窗不含），actual Updated Jan9T01:22:33Z；不能把该Submitted当本窗重要修订。当前两精确abs页无具体纠错/安全signal，不扩旧版本对照。官方纸目录日期仍保原值，非论文首次公开证据。
# 第三小批原公开区间（准入校准另行）

实际DataCite original created/registered与v1Submitted/Updated保DATES_3.json，exact-v1完整题摘身份保ABSTRACTS_3_RAW.txt。沿同一已核官方ID只在announcement分配/noadvanceID与Jan7截止后普通公告规则，v1均Jan6T19Z～Jan7T19Z buffer：最早公开下界Jan8T01Z；已注册真实ID上界按字段精度registered+1s，而不是registered精确公开。03388 [01Z,02:37:10Z)、03401 [01Z,02:37:28Z)、03444 [01Z,02:38:29Z)、03525 [01Z,02:40:28Z)、03577 [01Z,02:41:45Z)，完全本窗；较早作者正文有具体线索时需另定点核，日期不授贡献/Evidence。03525 DataCite现标题为v3，原v1标题VeRPO保原abs；后v2/v3非本窗事件不机械扩审。
# 后续第二小批日期原值（准入尚未授予）

DATES_4.json 保留真实 DataCite 200 返回的原字段，执行时间2026-10-02T14:49:43Z；不是registered直接等于first-public。四份exact-v1 Submitted均在Jan06T19Z～Jan07T19Z公告缓冲内，依既有官方ID仅公告分配政策，下界Jan08T01Z、上界registered下一秒：03648 `[01:00:00Z,02:43:24Z)`；03666 `[01:00:00Z,02:43:50Z)`；03493 `[01:00:00Z,02:39:38Z)`；03895 `[01:00:00Z,02:49:20Z)`。这些条件区间全部在本窗，但不排除具体更早作者公开线索，后者若出现再定点核；日期支持不授准入/Evidence。ABC DataCite现标题已改变，只取dateInformation=v1日期，本文沿用exact-v1原标题，不以当前v2正文替代本窗版本。
