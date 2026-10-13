# SpecForge18567：必要 Source / actual sole owner / 具体已有覆盖

作者resume_mar18；本03-21补BJT03/20，首批root仅准入通过，Source/NC独核待授。精确v1身份与日级夹证见SUP_FIRST_ADMISSION、SUP_FIRST_ARXIV_DATE_FIELDS；不据后续版本倒填公开事件，不授production标签。未改Books/LS/索引，未计safe或DAY。

## 必要原证

[exact-v1](https://arxiv.org/html/2603.18567v1)：§2.4 TTT条件与prefix/prediction接口、§3、§4.1–4.2/Algorithms1–3、§5.1–5.4/Table1；§6.1/Tables2–3及§7.1–7.3直接收益反侧。已读必要机制、关键评价与直接代价即停，不遍历发布库或完整recipes/code，不把“production-oriented”当生产认证，未核实现/复现。

原增量：冻结target生成训练hidden states属于prefill推理，小draft仍保存backward/optimizer；二者不必同ZeRO布局。实际target用SGLang runner/TP（可支持EP/PP）、draft只shard optimizer+gradients（ZeRO2）。正文允许co-locate/disaggregate，但实验明确仅co-locate，不授独立远端服务/跨卡传输瓶颈已验证。TTT在训练中消费原prefix和先前预测的K/V，BlockMask/streaming attention减少attention logits物化；loss backward将不再使用的logits buffer换作gradient，须保留正确buffer生命周期，不据伪代码认证精确实现。

评价是8×H200、seq4096、各方法按内存容量选择batch。Table1 8B EAGLE batch16/1.04s→Spec batch64/2.07s，吞吐2.01倍但单step更慢；70B batch8/2.21s→16/3.18s，1.39倍且step更慢。235B同batch8 ZeRO3 11.2s→TP8/1.62s、9.99倍；并行plan、engine/kernel与graph共同变化，不能把总增益全归纯解耦，baseline“最佳ZeRO2/3”亦有OOM反侧。单H200、TTT7最后一步kernel的62.1%时间/93.5%峰存减少不是完整训练/Serving倍率。precision/全网络拓扑、故障、收敛等在采用范围Not Disclosed。

SpecBundle另用1.4M PerfectBlend、target温度.8重生成、2epochs/LR1e-4，再以SGLang H200运行；8B并发8、大模型16，五个spec configs择最高吞吐，不授普遍4.48倍/SLO。Llama8B/70B MTBench吞吐450.0<454.7、1253.0<1272.7旧draft（作者称MTBench performance下降，这里表值是throughput，不误写质量分）。Data regeneration有FinanceQA acceptance例外且生成训练成本需摊销；TTT更长增加训练时/内存、最优长度任务相关。MoE draft有限设置不胜dense，不能从所测topk1/容量推普遍不适合。

## 评分与实际已有覆盖判断

2+2+2=6，评分对象是target前向与draft更新的非对称并行接口及局部证据，不给FSDP/streamsoftmax既有原则新高分。实际fresh Book上下文已读，Ch36 878–945完整communication/topology→Teacher/Student→globalbatch，1500–1568 phase pools/迁移及1670–1687 split training，邻Ch35/37开篇；Ch48 368–405 drafter artifact与447–496 offline→decoupled hidden capture→online update/commit交接已顺读。

**sole owner `TRAIN-DISTRIBUTED-TRAINING`，具体NC拟成立。** Ch36现931–937“Teacher与Student不应共享一份并行Plan”正文明确承载：teacher推理、student反向与optimizer footprint不同→分别规划inference/training分片→版本化teacher output、buffer ownership/消费顺序handoff→topologysearch/buffer/一致性/完整吞吐显存收敛验收→证据不足回对称布局。不是只凭主题/论文名相似。SpecForge在draft训练场景补局部实证，但所采用稳定接口不缺；不为SpecForge名字或SGLang具体backend增章。Ch48已有targethidden capture与独立draft trainer、candidate revision/target验证分责，不将实际训练吞吐冒称上线correctness。

TTT BlockMask与in-place logits是该接口的实现/资源优化，原式不新增所需长期acceptance/commit条件；只在报告保留实际代价和评价，未把有限loss/kernel recipe升为一般运行保证。不创建第二owner、不强造正文/注diff；若非准备者认为prefix/prediction训练布局仍构成具体知识缺口，应定点该接口改判，不删除已有反侧或缩候选。

## 复核请求

请非准备者独核必要Source与上述实际Ch36具体NC。通过前不计安全处置，NC不虚构POST，不给Books附动态验收收据；单篇不等全部来源结束。

2026-10-11 root非准备者必要Source/actual具体NC正式PASS：实际exact-v1 §4.1/4.2/Algorithms2–3、§5.1–5.4/Table1、§6.1评价配置/MT吞吐反退及§7.1–7.2成本，actual Ch36 Teacher/Student931–937与两侧完整承载所采用接口。保独立并行/单共置、baseline batch/backend共同变化、TTT重算、再生成摊销和有限调优择优全部反侧。具体已有覆盖成立，不强造正文/源注diff，不虚构POST或生产保证；单项安全NC，不预支整日DAY。
