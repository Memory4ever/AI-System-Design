# 03-12 首公开定点恢复（不重算原候选）

执行2026-10-09。arxiv公开日夹证由SUP_ARXIV_AVAILABILITY.html及SUP_EXACT_FIRST.json支持，review_mar12实际读通过；Submitted/Updated、DOI注册均不单独算公开日。这里只处理具体先稿线索，不扩OpenReview会议池。

## 2603.09488 — Diagonal Distillation

current-v2 comment ICLR2026触发先稿核。官方作者项目页https://spherelab.ai/diagdistill/标题、作者与arxiv同家族，无日期。官方OpenReview作者实名版https://openreview.net/pdf/08bdee8b1fcf7062a2b019026c7b0456bb3fa1c0.pdf、匿名under-review版https://openreview.net/pdf/b16531e951fba05f6c77c62cf3cc12697284526e.pdf与https://openreview.net/pdf/a6c9c465e84422ee07fb2cf2bca59c71a660419c.pdf，标题、Diagonal Forcing与2.61s/31FPS等机制同家族；未将搜索引擎“last year/10months”作官方公开日。直接官方api2 notes exact title及api notes exact title均返回403 ChallengeRequiredError；作者主页https://brandon-liu-jx.github.io/有限链接恢复未得具体forum id。必要pdate/公开版本边界尚缺，精准先稿身份/日期保留；未评分、不作本日确认首次公开候选。恢复只需对应公开note的pdate/公开读者权限与exact paper，不以全文绕日期或通用ICLR日程充该稿公开日。

## 2603.09079 — GST-VLA

官方作者https://s-elim.github.io/publications/明确为ICMLw2026、The6thMuslims inMLWorkshop/MusIML，而非ICLR；具体OpenReview id J57nR3hyAd。直接forum https://openreview.net/forum?id=J57nR3hyAd跳Challenge，api2 /notes?id同403，未绕Challenge。官方PDF https://openreview.net/pdf?id=J57nR3hyAd可读完整题摘，作者/128GST/256primitive与原稿同家族，但无已取到的note pdate。因此先稿公开日/版本边界精准保留，不把accepted本身推出窗前；arxiv当日公开夹证仍有效。

必要纠错信号：官方OpenReview摘要明确只提供preliminary stage1training/validation loss与offlineMSE，simulation evaluation/real-world deployment/ablations仍ongoing；arxiv-v1却写96.4%LIBERO/80.2%SimplerEnv和ablation完成，current arxiv comment已有preliminary/finaldata maychange。此处不采用这些最终指标，不声称实验完成，必要后续审阅围绕机制与直接冲突；若date无法恢复则不因此投入全稿。需要作者定稿与实际完成数据时才可重开性能采用链。

## 2603.09452 — CyberThreat-Eval

root独核§1/AppE.1的具体评价排序反例后撤销原领域EX。作者有界检索exact title＋TMLR，官方OpenReview PDF首页内容恢复为完整标题、Xiangsen Chen等作者、相同CTI triage/deep-search/TI-drafting摘要、forum tiFtZHwr7O，页眉原值“Published in Transactions on Machine Learning Research (11/2025)”。原入口 https://openreview.net/pdf?id=tiFtZHwr7O 与 https://openreview.net/pdf/c78b73a670ab5b05bb234fca4343aca137f89fa2.pdf 。此处不使用搜索引擎published/crawl age、arxiv accepted comment作公开日期。随后实际直接PDF/hash/forum均跳OpenReview Challenge；本轮获得的是官方PDF内容恢复线索，而非已取公开note pdate或直接PDF文件。因此先公开身份/发表状态待独立定点确认，不计本日候选，不扩会议池或用全文绕日期。若出版方可访问原件确认11/2025发表身份即可判定先于本窗，无需追该月精确时刻；否则提供该note公开pdate/visibility与匹配exact paper。评价反例潜力不因此被再排除。

## 2603.09200 — The Reasoning Trap / RAISE

ICLR2026 Logical Reasoning workshop的具体先稿触发，有界exact title搜索恢复官方PDF https://openreview.net/pdf?id=c4pkfkUaY3 首页完整标题、Subramanyam Sahoo/Aman Chadha/Vinija Jain/Divya Chaudhary与相同RAISE abstract。网页直接forum/PDF实际跳Challenge，api2 notes?id入口不可访问；因此公开note pdate/visibility与版本边界缺，不将accepted或搜索published age推出更早日期。作者上传ResearchGate Mar11 day-only只是同稿发现线索，未核时区/是否此前公开，不能覆盖必要原始note日期。当前隔离为精准先公开保留，不评分或本日采用；恢复该note公开日期/权限及对应paper即可定点去重，不再读无关全文。root已有效实际精确v1§6完整boxed/AppC.2–C.4/F的中心Disputed裁决保留，日期受阻不抹去证据也不升级为当窗candidate。
