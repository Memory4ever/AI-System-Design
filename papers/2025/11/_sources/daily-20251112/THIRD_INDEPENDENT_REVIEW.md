# 2025-11-12 第三批必要反侧独立复核

复核者Codex / Ohm；作者Noether，author != reviewer。实际工具clock 2026-10-04T21:02:19+08:00。fresh治理与窗口见[FIRST](FIRST_INDEPENDENT_REVIEW.md)，只加载本日原件；SECOND16完整题摘不重复。日期held材料只完整题摘与决定采用权限的安全/理论/纠错核心，不展开全部methods、实验或owner。

**结论：必要反侧内容总体成立，但整批须同步两处窄限定后通过；不授DAY。** Noether可立即同步§1的具体句子，其余有效反侧不重读。以下全部为实际原源读取范围，不将作者“已读”当非作者审阅。

最新变化回核（2026-10-04T21:27:51+08:00实际工具clock）：**THIRD通过，GPT必要Evidence与最终OnlyReport通过；不单独授DAY。** 实际读取作者21:07:47补段、THIRD表中More Agents/VMDT两行及当前README§4/5/6受影响句子。ASR缺clean正确mask/不自动有[0,1]界且未核实现不判代码必错、435/85.5%/.830仅T2V均已落实；AAPP门控方向与表文冲突隔离保留。未重读已过SECOND16或全部反侧附件。原首段是修正到达前的历史结论。

2026-10-04T21:31:15+08:00实际检查：THIRD/普通两份独立notes21本地引用、围栏/尾空白错误0；当前作者进行中V3 exit0，限定diff-check exit0。只确认实际内容范围与接口，不替Carver来源结论或DAY。

实际读作者[EVIDENCE_OWNER_NOTES](EVIDENCE_OWNER_NOTES.md)及当前README一个GPT家族候选和§4：同家族RSS日期、2025 card逐基线反侧沿用FIRST有效证据，Ch42/56预算权责及Ch66对象/分布/切片和相邻交接沿用本notes§3实际独立对读，采用命题未变化。作者两方向最终仅报告、共享Books差额0成立；不是Existing，不因未公开gate关闭准入，也不把局部安全负证据换成普遍安全。无实际Books写入/POST对象。本lane普通内容剩余题摘阅读0，分层结论另见[普通独立复核](ORDINARY_INDEPENDENT_REVIEW.md)；来源/query/有限停止/六部分由Carver接，整日需合并实际范围后裁决。

## 1. 两处作者窄同步

1. [THIRD](THIRD_CRITICAL_CALIBRATION.md) More Agents行及README§4/5：亲读[exact-v1](negative-math-multiagent-v1.html)§3.3。正文ASR称仅统计clean答对后被噪声翻错的子集，但所印分子为全部noisy错误、没有clean正确mask，分母为clean正确数；该公式不自动有[0,1]界。请保留公式/文字冲突，不能直接采用ASR为条件翻错概率，也不能只靠“按任务分层”消解。未核代码，不断言实际实现必错；日期隔离且不正面采用，不要求全代码/实验。潜在稳健性评价盲区不因此关闭。
2. 同包VMDT行：435样本、85.5% human–LLM agreement、interrater .830限定于T2V，不能连在V2T后形成跨模态统一验证。实际[C.1.3原文](negative-vmdt-v1.html)T2V段对应这些值；V2T另为324样本、87.7%、interrater .846。可只补T2V限定，不必引入新数字。保留短视频10frames、BR/HGR分账、V2T用细视频描述辅助judge的限制。

AAPP门控新增限定已见[SECOND§3](SECOND_INDEPENDENT_REVIEW.md#3-关键安全增补与剩余工作)：Fig2 harmful更近触发与`KL_harm-KL_safe >= tau_margin`分支不能未经阈值符号/实现解释等同。作者同步THIRD/README为“门控正确性未授采用”即可；不要求日期held全文代码审计。

## 2. 实际必要核心与权限

| 身份 | 亲读位置、裁决与停止 |
| --- | --- |
| AAPP 2511.07482v1 | Methods至Conclusion，Fig2、risk branch、Table1/紧邻解释及toxicity限制；PP/AAPP表文冲突、FLOPs估算非实测TPS、拒答proxy非全面安全均通过。保护alignment channel的潜力保留，门控定量正确性按上述隔离。 |
| Plugins 2511.05797v1 | §VII-C、VIII-C与Responsible Disclosure：Oct2024披露、P1服务端历史/加固prompt、P2警示与tool-instruction残留，各供应商/攻击分开。不得把所有hardening说成完全无效，也不外推全部当前模型。原raw部分468481/552628bytes，未核完整附件。 |
| Spectral 2511.05804v1 | Theorem1的class-conditional MLR/两regime条件与§7完整限制；118controlled context-statement、三模型、初步CN/FR，自然RAG/长上下文多轮/对抗仍未来。Bayes条件不变生产kill switch或已实现恢复/audit。 |
| Edits 2511.05852 | v1完整题摘另已读；v2原withdraw与current history实际核。行政author/order/status/未published错误不是实验造假；不采用撤回v2、不回用v1正面232配置，不使所有未来版本永久无效。v2 submitted Nov12 09:17:35Z在窗口终点之后，不作撤回公开时间。 |
| DBDI 2511.06852v1 | threat model、方向/层选择及Eq8–10、Tables2–5/关键消融与runtime段。白盒weights/hidden-state实时干预；Table2括号是simplified template，97.88不当official95.96，HarmBench92/95与其他表91/91.8按配置/冲突保留，TwinBreak不是统一重跑。15–25秒每层offline不能当E2E免费，未干预weights不变不证明干预一般能力无损。Eq6印成v_raw与harm mask，而harm提取文字定义u_raw；本批不采用该式为实现正确性，不为此全读代码。21:27:51定点重读原Eq4–6纠正本reviewer先前“refusal raw/mask”误写：mask确为harm，冲突只在raw向量符号，不扩大作者错误。 |
| QUEST-LOFT 2511.06125v1 | revised-gold完整人工流程、数据/模型与Justified QA、Table3列头及Pro RAG相关行、§7。100test/10dev、328entity、128K/top40、Gecko/Gemini分层；合并各方法答案后人工curation不是盲独立truth，移除DEBATABLE改变评价人口。Pro F1 .67/.81/.83与CoT .76/.74保留，不说每组件增益/所有RAG胜LC。raw部分242143/650219bytes，未读全附件。 |
| Contradictory RAG 2511.06668v1 | §3.2–3.5、§4/Table2与English/文档级限制；1476药物/8856query的检索探针，固定K5，most-similar与most/least-contradictory选择准则不同，不能纯因果归因矛盾。NLI sentence peak不是临床真值，ROUGE/同encoder similarity不是安全；5模型R1差异不合成18.2%普遍率。只保留LLM证据链的相关性/一致性轴，不引入医学机制。 |
| VMDT 2511.05682v1 | T2V/V2T题摘、数据/BR-HGR定义、C.1.3两评价流程/人工agreement；GPT4o-2024-08-06 judge、10frame采样、V2T详细描述辅助、能力不足可降低HGR。验证人口按§1分开；部分599400/1675175bytes，不声称全风险附件或真实生产安全。 |
| More Agents 2511.07112v1 | §3.2–3.3、既有模型/任务反侧及§7限制：same-model25采样，n1/2/5/10组数25/12/5/2，15/20/25仅一组；不是通用debate/verifier。English math/字符噪声、regex、相关错误/无adaptive攻击都保留。ASR按§1待作者窄同步；部分347301/672133bytes，不授全附录。 |
| Fraud 2511.06448v1 | §4.1双指标定义、§4.3 collusion/benign模型与规模反侧、§7/ethics。110模拟agent、100benign/10malicious；R1 collusion与maliciousV3下benign容量实验不混；Rconv按私聊、Rpop按benign人口，1000/100规模仍LLM模拟非真人转账率。当前局部不采模型总数矛盾或监控precision1为安全保证。 |
| Licensing Oracle 2511.06073v1 | 本日完整AB已读；只复用同exact-v1的[PDF题头身份](../daily-20251111/nov11-critical-identity.txt)及[§6.2–6.3原段](../daily-20251111/nov11-source-final-details.txt)，亲读所需段落。complete/formal KG、imprecise谓词、缺时态/歧义、多跳未实现、coverage–precision取舍均通过。不把论文必要充分宣传当所有外部truth/复合答案定理，不加载11池或其Coverage。 |

10个新增身份完整exact-v1题摘及AAPP此前题摘实际已核；理论只核决定命题权限的假设，不重证全部定理。未运行代码/模型、未复现实验，日期held不授Evidence/Books/确定当窗家族。其余普通潜力题摘与分层关闭正在继续，不能以本包为134AB全量通过。

## 3. GPT-5.1单项与作者下一步

[FIRST](FIRST_INDEPENDENT_REVIEW.md)同家族RSS/发布core/2025五页card已实际通过，含所有必要表列/风险反侧；本次不再读late/current卡来替换2025版本。正式README仍20:46:50旧停点，说RSS待核、候选空表、没有实际独立通过；这些应同步为本家族已确认落窗/必要Evidence与既有notes，不再隔离有效RSS。

本轮实际读取当前治理Books上下文、ROADMAP和Ch42请求身份/变长工作量/TTFT-E2E段、Ch56目标/SLO admission、Ch66对象身份/分布/切片不确定性及Ch43/67必要交接。判断为**支持仅报告、拟共享Books差额0**：未披露新gate/训练算法，2x快/慢只代表性ChatGPT任务行为，不提供新runtime SLO机制；安全表为新版本/基线的局部反侧，不改变Ch66的对象、分布、切片和不确定性验收选择。不是算法名已覆盖，也不是因此关闭准入；不要把5.1版本号不在Books当长期缺口。作者可核这些具体位置、确认最终处置并同步§1/3/4/5/6；若选择不同长期命题，先给root具体差额与owner，不直接改共享Books。

目前可执行：作者上述窄同步和GPT最终处置；本lane继续其余潜力AB/分层关闭、14源原query/native/stop与六部分DAY。来源/日期外部隔离不会变永久普通待办，也不把完整AB变全部实验队列。准备好单项即时审，未等待18或全月。只写本日独立notes，不改README/Books/state/index，不stage/commit/push。
