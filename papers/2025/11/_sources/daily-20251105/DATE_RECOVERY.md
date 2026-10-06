# 2025-11-05 具名首公开有限恢复

作者Carver；本日BJT `[2025-11-04T09:00:00+08:00,2025-11-05T09:00:00+08:00)`，UTC `[11/04 01:00,11/05 01:00)`。不授论文日期准入或非作者通过。

## 原字段与边界

13个具名ID分别实际获取DataCite，均HTTP200，原JSON与receipt在本目录。Submitted是提交，Updated未被证实是首公开，Available=2025-11仅月精度，Issued=2025仅年精度；DOI created/registered是登记事件，不能据此补首公开精确时刻或保证此前正文公开。arXiv普通公告schedule不能补造本次历史时刻，09:00终点属于下一Daily。

| exact-v1 ID | Submitted UTC | Updated v1 UTC | created / registered UTC | 当前必要缺口 |
| --- | --- | --- | --- | --- |
| 2511.01824 Simia | 11/03 18:29:57 | 11/04 02:54:10 | 11/04 04:32:12 / 04:32:13 | 原正文首次公开下界未证 |
| 2511.01805 Context | 11/03 18:05:57 | 11/04 02:52:49 | 11/04 04:31:46 / 04:31:46 | 同上；v2 Submitted11/04 17:41:28、Updated11/05 01:59:19，不证明重要修订或在窗公开 |
| 2511.01758 RLAC | 11/03 17:15:05 | 11/04 02:50:16 | 11/04 04:30:38 / 04:30:39 | 原项目无历史公开时刻 |
| 2511.01386 RAGSmith | 11/03 09:36:27 | 11/04 02:25:34 | 11/04 04:21:39 / 04:21:40 | 作者库Published/Last updated仅November2025 |
| 2511.01059 Efficient Test-Time RAG | 11/02 19:32:39 | 11/04 02:04:52 | 11/04 04:13:40 / 04:13:41 | 作者原事件未恢复；辅助转载错述不采用 |
| 2511.01554 DDCL | 11/03 13:16:57 | 11/04 02:36:57 | 11/04 04:25:42 / 04:25:43 | 范围歧义与首公开分别待核 |
| 2511.02770 AMER | 11/04 17:57:20 | 11/05 02:00:10 | 11/05 03:00:27 / 03:00:28 | 跨终点；具体OpenReview匿名同题稿可能更早 |
| 2511.02776 XR-1 | 11/04 17:59:12 | 11/05 02:00:22 | 11/05 03:00:36 / 03:00:37 | 跨终点；项目现为ICML2026页，v2/v3在2026不替代v1 |
| 2511.02919 ARC | 11/04 19:02:29 | 11/06 01:01:52 | 11/06 02:44:06 / 02:44:07 | 更晚跨截止；不能由字段判完全窗内/窗外 |
| 2511.00796 AReaL-Hex | 11/02 04:17:30 | 11/04 01:48:32 | 11/04 04:07:17 / 04:07:17 | 完整题摘已读，无历史announcement下界 |
| 2511.00807 FREESH | 11/02 05:17:02 | 11/04 01:49:27 | 11/04 04:07:34 / 04:07:35 | 作者库无历史事件；v2提交11/05 18:15:57在截止后，未据版本号扩审 |
| 2511.01866 EdgeReasoning | 10/21 04:18:25 | 11/05 01:00:13 | 11/05 02:38:52 / 02:38:53 | Oct submitted不是October public；Updated距截止13秒且登记更晚 |
| 2511.01872 Learned Cost Model | 10/21 22:45:45 | 11/05 01:00:23 | 11/05 02:39:01 / 02:39:02 | 同样跨截止；旧PDF线索与DAC2022 style不是可核历史发表证明 |

## 实际有限恢复与停止范围

完整题摘及轻量版本标记：先10篇（SECOND_CALIBRATION_READY），再系统月标题仅定点4篇，见[原返回](RAW_SYSTEM_TITLE_EXACT_AB.json)。未读全部CL1527/DC338题摘；CL/DC skip0/show25仅相关标题查漏，不继承其他日关闭。CL第2项原目录明确withdrawn，仅保留标记，不入选/评分；月列表不证明撤回在本窗。

官方advanced search实际说明announcement只年月；无效日路径HTTP400、旧格式2511月URL404均不证明历史公告不存在。有效CL`2025-11?skip=0&show=25`web实际25标题可读；有效DC同格式本日native200且25标题逐项可见，web失败由此有限替代。停next25，不扩月表为全类题摘/全文队列。

作者恢复：Microsoft Simia库无release历史事件；JiayiGeng/LM-belief-change无原时刻；RLAC项目只有论文/代码身份；yAquila/RAGSmith仅月精度；XR-1现页ICML2026。查询及返回见[作者恢复](RAW_AUTHOR_DATE_RECOVERY.json)、[有限末次](RAW_AUTHOR_DATE_FINITE_END.json)。当前代码/commit日期不当历史公开时刻，未遍历代码、全部commit或附件。

AMER精确同题ICLR稿`nGIydjpyLD`触发按需OpenReview；forum实际browser-verification页，api2 notes native403、web不可达，原response/receipt保留在openreview-amer.json。作者timchen0618/amer可核身份但无历史时刻，不读全部156commits。ARC精确标题/项目查询只恢复arXiv与辅助索引。最后系统查询及作者页见[发现](RAW_SYSTEM_DATE_DISCOVERY.json)、[有限末次](RAW_SYSTEM_DATE_FINITE_END.json)：FREESH当前库、Edge作者organization的UpdatedOct21只作线索；Learned Cost作者papers路径不可达。

## 日期层本次终态保留，贡献层未关闭

13项有限当前原入口到上述停点，首公开仍不支持完全落窗；具名日期层隔离，不用于正面Evidence、Books、确定候选计数或无遗漏断言，不是13篇机制已关闭，不扩成全文队列。精确重开：对应ID/v1正文的真实官方announcement，或作者正式公开事件与可证明完全落窗的首次公开上下界。AMER可用OpenReview同题note的可核公开字段及版本正文关系，不能只用cdate/submission或名称；跨截止AMER/XR/ARC/Edge/Cost优先核更早公开与实际归属，不能把Updated当public反向宣布窗外。

普通待办仍有首批2公告准入校准/必要证据/Books判断、13项机制/范围校准和六部分非作者验收；日期层隔离不授整日报完成。
