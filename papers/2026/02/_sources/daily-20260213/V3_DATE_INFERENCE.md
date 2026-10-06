# 本日 arXiv 首公开范围推定（非 submitted）

官方入口：https://info.arxiv.org/help/availability.html 。相关标题有限查漏后恢复159份v1题摘；159不是候选分母，也未扩大567个宽标题库存为逐项队列。更正：当前恢复月列表没有daily batch标签，不能声称已实际核到2026-02-12公开列表批次。

官方 availability 原文说明 identifier 仅在 announcement 分配，不能提前取得；周三20:00 US Eastern announcement 在2026-02为 EST，对应北京时间周四2026-02-12 09:00。假期表没有本批公告日。Submitted 和 v1 Updated 是不同字段，不能当 first-public。

DataCite官方逐项HTTP200原值见 V3_DATE_ALL_NUMERIC_RAW.json：125项当时numeric临时判断，其 created 从2026-02-12T02:47:20.000Z至2026-02-12T03:11:06.000Z。created只是已经存在的上界，不是各项公开时刻，也不证明没有家族早公开。不能给125项统一授announcement下界；每项须另有相关batch证据，或用晚于上一公告的v1 submitted、官方排程与created上界联合推定。早提交项仍待必要核，Updated v1不直接等first-public。

## 10531 / 10545 逐项包络

逐项字段还支持另一条排程下界：V3_DATE_ALL_NUMERIC_RAW.json中119项v1 Submitted实际位于2026-02-10T19:00:02Z～2026-02-11T18:58:54Z，即Tue14:00～Wed14:00 EST提交段；官方表对应最早Wed20:00 EST（02-12T01:00Z）。这119项created实际范围是02-12T02:48:44Z～03:11:06Z（不是125项的02:47全局最小值），故延迟也不可能落入再下一正常批。逐项字段、119计数与官方排程包络已由root实际独立核验，可对119项与当前准入状态交集采用范围[02-12T09:00+08,02-12T11:12+08)；不把119当候选数，不覆盖早公开家族或更早submitted6项。KVP10238原Submitted=02-10T19:34:15Z，属该deadline后分支。6项10134/139/146/153/161/179的submitted早于本段，不从Updated v1直接反推公开，保留有限batch缺口。

10531：abs v1 history为Wed, 11 Feb 2026 05:01:46 UTC（V3_V1_AB_CLI_FORMATTED.md物理64行）；DataCite submitted同值、v1 Updated=2026-02-12T01:25:59Z、created=2026-02-12T02:56:27.000Z。10545：abs v1 history为Wed, 11 Feb 2026 05:37:22 UTC；DataCite submitted同值、v1 Updated=2026-02-12T01:26:57Z、created=2026-02-12T02:56:46.000Z。原字段保留上述JSON；当前abs未见withdrawn标记。

两篇submitted均晚于上一正常公告2026-02-11T01:00Z，不可能在上一批已有同v1；官方identifier/DOI不得在announcement前提供。下一正常公告为2026-02-12T01:00Z，created已于同日02:56Z出现且早于再下一批2026-02-13T01:00Z，故唯一正常公告批为02/12。分别采用保守范围`[2026-02-12T09:00:00+08:00,2026-02-12T10:57:00+08:00)`，终点向上取整；submitted/Updated不被当作public，01:25/26 Updated也不补造精确公开时刻。当前event页与必要core未见更早家族公开线索。两项逐项推定已由root实际验收，不能泛化到125项或授日级完成。

此范围不解决先公开家族。10144/10551/10583/10604/10743/10816/10884/10975/11105，以及已有明确MLSys/ASP-DAC线索的10729/11016，仍须各自必要首公开核查或精确隔离；其他准入改判也须补其对应metadata，不把125当最终候选分母。root的119排程范围通过只授各有效交集的arXiv事件落窗，不由作者授日级通过。

## 已实际读取的必要 schedule 段落

+L169:
L170: Work submitted to arXiv undergoes a series of quality assurance checks as part of cite83†moderation . This helps authors by ensuring their work will be discoverable and archivable and helps readers find relevant research that is in a consistent, readable format.
L171: Quality assurance checks can take between one to four days to resolve, sometimes longer. Authors will be notified by email if any issues are found in the submission. Authors will also receive an email when the submission is posted publicly.
L172: Submissions to arXiv are typically posted publicly Sunday through Thursday, with no announcements Friday or Saturday. You can check the cite88†current arXiv time†arxiv.org , which also shows the next deadline. Submissions are made public as part of the cite27†scheduled announcement process . This includes new submissions as well as cite35†replacements , cite44†withdrawal notices , cite30†cross listings and cite32†journal reference .
L173: ## A note about arXiv-id assignments
L174:
L175: The final cite49†arXiv identifier is assigned as part of the automated process when the work is announced. It is not possible to generate or to be provided with the arXiv identifier or DOI in advance. Submitting authors will receive an email when the work is announced and it will appear on their account dashboard.
L176: Note: The arXiv identifier cannot be back-dated, so identifiers will be assigned in the month of first announcement. It may be the case that a submission appears in a different identifier month than its original submission date due to various factors.
L177: ## Announcement Schedule
L178: Submissions received between
L179: (all times Eastern US)  | Will be announced
L180: (all times Eastern US)  | Mailed to subscribers
L181: --- | --- | ---
L182: Monday 14:00 – Tuesday 14:00  | Tuesday 20:00  | Tuesday night / Wednesday morning
L183: Tuesday 14:00 – Wednesday 14:00  | Wednesday 20:00  | Wednesday night / Thursday morning
L184: Wednesday 14:00 – Thursday 14:00  | Thursday 20:00  | Thursday night / Friday morning
L185: Thursday 14:00 – Friday 14:00  | Sunday 20:00  | Sunday night / Monday morning
L186: Friday 14:00 – Monday 14:00  | Monday 20:00  | Monday night / Tuesday morning
L187: ## On Deferred Mailings
L188:
L189: Occasionally, arXiv defers a mailing, either for locally celebrated holidays such as Thanksgiving or for ad hoc reasons. Information about deferred mailings may be found on the cite89†arXiv status†status.arxiv.org page, or on the cite16†arXiv blog†blog.arxiv.org .
L190: ### 2026 Holidays
L191:
L192:   * Thursday 2026-01-01
L193:   * Monday 2026-01-19
L194:   * Friday 2026-06-19
L195:   * Friday 2026-07-03
L196:   * Monday 2026-09-07
L197:   * Thursday 2026-11-26
L198:   * Friday 2026-12-25
L199:   * Tuesday 2026-12-29
L200:   * Thursday 2026-12-31
