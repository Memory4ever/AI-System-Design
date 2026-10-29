# Jun05主题导航四项定点题摘与首次准入待校准

作者jun06_continue，2026-10-25。本轮不增宽NAV：只从既存[87标题模型主题导航](SUP_MODEL_DISCOVERY_20261025.md)中定点打开安全后训练、MoE量化、推理调度和steering supply-chain四个直接相关标题，未将其余83标题转必审队列，亦未声称整个主题stop完成。

已实际读下列exact-v1完整题摘/三项abs history；05958 abs的web CacheMiss后用exact-v1官方HTML恢复完整题摘/身份（HTML头v1/04Jun），其精确提交记录由官方DOI元数据提供。四项均未见撤回/纠错标记。未评分、未做必要/Books，不因已能映owner而直接入书。

## 日期原字段与组合推断

实际GET四精确DOI API，全部client=`arxiv.content`、state=`findable`、version=`1`、唯一Submitted条目标v1；三项与abs逐秒一致。原始字段如下，Updated不是公开日依据，Available月/Issued年均不作为独立日证。

| 身份与原件 | Submitted UTC v1 | registered UTC |
| --- | --- | --- |
| [05817 abs](https://arxiv.org/abs/2606.05817v1) / [DOI](https://api.datacite.org/dois/10.48550/arxiv.2606.05817) | 2026-06-04T07:58:55Z | 2026-06-05T02:09:30.000Z |
| [05688 abs](https://arxiv.org/abs/2606.05688v1) / [DOI](https://api.datacite.org/dois/10.48550/arxiv.2606.05688) | 2026-06-04T04:13:05Z | 2026-06-05T02:06:29.000Z |
| [05933 abs](https://arxiv.org/abs/2606.05933v1) / [DOI](https://api.datacite.org/dois/10.48550/arxiv.2606.05933) | 2026-06-04T09:36:40Z | 2026-06-05T02:12:01.000Z |
| [05958 HTML](https://arxiv.org/html/2606.05958v1) / [DOI](https://api.datacite.org/dois/10.48550/arxiv.2606.05958) | 2026-06-04T09:56:48Z | 2026-06-05T02:12:34.000Z |

按本日已核官方EDT公告/发号规则，四项最早可能公告均Jun05UTC00:00；至精确DOI注册上界整个区间均在Jun05BJT。它们支持本窗arXiv公告日，不把registered命名实际发布时间，不证明全球首公开或当前正文历史逐字不变。共同方法复用，不第三恢复日程。未发现更早稿具名线索，必要前仍应定点查同family真实覆盖，不扩别日报材料池。

## 具体贡献拟准入（待唯一reader）

| 身份 | 原约束→实际题摘增量→需要核验的设计选择 |
| --- | --- |
| **Consistency Training Along the Transformer Stack 05817** | 只在输出/已有residual一致性对照防护不足→MLP post-activation和per-head attention distribution两种内部一致性target，题摘报告跨persona/frustration/prefill/conditional threats及共享/不同机制→需核验内部target的训练与安全泛化边界；不由“unifying”宣传或更多任务直接认定统一定律 |
| **VSRAQ 05688** | MoE低比特误差能跨越top-k router边界，单纯reconstruction不保计算路径→value score对齐加expert ordering/top-k结构对齐的PTQ目标→需核验是否在同量化/校准预算下改变route稳定与质量，不把“无inference overhead”当总费用零或只因分数提高收录 |
| **SlidingServe 05933** | greedy当轮chunking不能同时看到下一轮SLO风险→batch latency predictor、current/next滑窗chunk、priority和DP batch选择→需核验预测误差/两轮展望与fairness/SLO条件；不采“strictQoS”或headline吞吐/违约率作已证保证 |
| **Steering Vectors are an Adversarial Attack Surface 05958** | 用户重算向量/检查来源/benign属性校验仍可能接受恶意对比数据→同一属性direction混入拒答抑制方向，合法bundle等价性证书只证明向量由给定文本算出、不证明文本安全→需核验steering artifact的provenance与行为授权必须分开；两model/eightcombo ASR/防御数字待必要，不给攻击或防御普适保证 |

四项潜在机制/边界已具体，实验可信度待必要，不因摘要没完备消融排除；拟准入而不先高分倒推。材料准备好立即交reader首校准/Jun05日证，后续按保留原分或首次正式评分及实际缺层逐项推进。没有本批方法稿、Book写入或预I，不把本文件作为全主题或全日验收。
