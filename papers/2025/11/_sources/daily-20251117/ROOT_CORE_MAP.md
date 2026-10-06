# Nov17 Root Requested Core Map

Carver按root独立复核分工定点取回；2026-10-04，receipt实际UTC12:17:32～12:18:14。所列安全/反证清单实际11项（此前口头误计13，纠正），全部exact-v1 HTML HTTP200，原URL/bytes/error在各自`.receipt.json`。只解析真实章节/表图caption作定位，没有重做root抽检，也不授全文Evidence/日期/Books通过。84题摘没有转84全文队列。

| 身份 / 原文文件 | 建议必要受影响位置（实际原标题/锚点已核） |
| --- | --- |
| [2511.12712 AFM](core-2511.12712v1.html) | §3.2～3.8 relevance/fidelity/budget/fallback；§4.5～4.8与Table1：single reference run、planned ablation；§5.4 Failure Modes。 |
| [2511.12497 SGuard](core-2511.12497v1.html) | §3.1 content labeling、§3.2 priority switching/Algorithm1–2；§4 benchmarks/baselines/metrics、Tables2–7 FNR/FPR/ASR与ablation Fig4；`Sx1` Limitation。 |
| [2511.12487 ToxSearch](core-2511.12487v1.html) | §2.1～2.3 population/selection/operators；§3 RQ1/Table4、RQ2/Figs2–3 transfer/refusals；§4 Ethical Considerations。 |
| [2511.12381 White Bear](core-2511.12381v1.html) | §2.2 experimental setup；§3 Figs1–2 rebound/load、Figs3–4层/head分析；§4 conclusion限制。 |
| [2511.12149 AttackVLA](core-2511.12149v1.html) | §3.2/3.3 AttackVLA/BackdoorVLA；§4.1/4.3/4.4 setup/模拟/真实环境；§4.5 Table2–3触发/poison rate，§4.6 Table4 defenses；action tokenizer适用差异在Table1 caption。 |
| [2511.10899 TIM](core-2511.10899v1.html) | §2；§3.2评价suite与§4 Table2；§5.1/5.2/5.3/5.4/5.6反侧与替代解释；§6.3 Table3 mitigation质量取舍、§9 limitations。 |
| [2511.10909 MMA-Sim](core-2511.10909v1.html) | §III-C/D/E/F summation/precision/rounding/special值；§IV TablesIII–IV及九算法；§V bitwise correctness validation；§VI-A/B/C未披露precision/range/rounding反侧。 |
| [2511.11601 Mind the Gap](core-2511.11601v1.html) | §III-A～E dataset/graph/variant/execution/output比较；§IV-A/B/C execution/output/compile与Figs3–5、TableI；§IV-D Threats to Validity。 |
| [2511.11733 Decentralized Speculation](core-2511.11733v1.html) | §2.2分布式假设；§2.3 adaptive verification/token identification/Algorithm1；§2.4 complexity；§3.1设置与§3.2 Tables1–2质量/参数/ablation，不能仅latency宣传授distribution-preserving。 |
| [2511.11313 DocSLM](core-2511.11313v1.html) | §3.1/3.2 compression/streaming abstention；§4.3 implementation；§5.2 Tables3/5/6模块、长度、OCR消融；Fig2实际memory设定；§6 limitations。 |
| [2511.11520 Video Policy Evaluation](core-2511.11520v1.html) | §III-A/B/C VLM judgment/action conditioning/rolloutaugmentation；§IV-A TableI/II synthetic评价；§IV-B pretrained/rollout消融、§IV-C realworld相关；§IV-D Fig8 hallucination/multiview不一致等失败。 |

章节锚点例：TIM `S3.SS2`、`S5.SS1`～`S5.SS6`；MMA `S3.SS3`～`S3.SS6`、`S5`、`S6`；其余对应HTML `S<section>.SS<subsection>`。无PDF/代码附件扩展；root可直接读必要原文，当前25/66日期hold仍不因此解开。

## 后续root三项请求（实际UTC12:28～12:35）

- [SureTrap2511.12414v1](core-2511.12414v1.html)：完整200/187128bytes/exit0。必要§III threat model/Algorithm1，§IV-A setup、IV-B/C/D open/closed/benign-only，Fig4的closed-weight sure-rate与harmful continuation分离，§V defenses、§VII limitations。只核定位，root尚待实际读，不以AB平均效果授安全因果。
- 2511.11612v1：首查HTTP200但exit28、142945/278039bytes；[30秒单retry](core-2511.11612v1-retry.html)仍exit28、198457/278039bytes，原receipt保留。native部分只到§3.4.1/Table1，不支持§4结论；改走一次原HTML web恢复：[原方法](web-core-2511.11612v1.json)、[必要§4/Table2/§5](web-core-2511.11612v1-results.json)，原工具显示369lines。请root核§3.1～3.4 single scenario/约束与参考、§4.1 Table2/§4.3说明、§5 future；特别§4.1/结论的三optimal模型名单与§4.3不同，不照搬所有计数/最优保证。不是native完整取回。
- [LLM4SCREENLIT2511.12635v1首查部分](core-2511.12635v1.html)：HTTP200但exit28、223873/261847bytes；[30秒单retry部分](core-2511.12635v1-retry.html)exit28、213426/261847bytes。原首查实际已有§2.1～2.5 correctness/lost evidence/biased metrics/dropping unclassified、§3.1～3.5 review/variation/confidence/limitations与§4.1～4.3建议标题、Table1–2/Figs1–4；不称完整HTML/全文。root可以先核这些必要段，若依赖缺失尾部只定点恢复；失败不支持缺段内容或完整正文验收，停止重复whole retrieval。

[OPFormer必要消歧](OPFORMER_CORE_DISAMBIGUATION.md)为另一个完整200core，root实际§3.1+B支持范围关闭。至此15个具名core材料路径（13完整native、2部分native，其中11612必要段web补回），不是15完整native/全84实验队列；当前OP关闭后65potential，原66日期核对作为历史保留。
