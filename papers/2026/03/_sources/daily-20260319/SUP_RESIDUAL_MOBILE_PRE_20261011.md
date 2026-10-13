# 03-19：Residual / Mobile 必要原证与实际 owner

作者 resume_mar18；仅 BJT03-18自然日，两篇首批准入/日期已root正式校准，Source/Books以下是作者判断，未获独立通过；未核代码或复现实验。

## 2603.16039 Residual Stream Duality — 1+1+2=4，具体关闭/已有覆盖拟核

[精确v1](https://arxiv.org/html/2603.16039v1)必要§2.1–2.6/Eq/Alg1、§3结论。评分只给实际新增的双轴局部算子重索引/placement解释，而不是借用成熟state/caching原则；不是因NC减分，也不默认EX。固定token后沿depth排序的显式QKV causalwindow与ShortSWA属同一算子family，这是定义下的有限等价；ELC-BERT/DenseFormer静态权重不是literallyQKV实例，整网factorization/gate/injection与硬件成本更不等价。作者O(Twd)局部项仍叠加global O(T²d)，depth window O(TKLd)/full O(TL²d)及历史state保存/转发/重算，额外PP statepath必须计费。DDL改变carry/write而非保存全部depthhistory。原稿没有实验/benchmark，因而 sequence-side优先只是有已成熟kernel/cache/chunk支持时的设计建议，不是全硬件最优、质量优势或实测加速。Hardware/precision、workload、batch/并发/I/O/SLO与evaluator=Not Applicable（纯结构说明，无性能实测）；实现未核。

实际 owner MODEL-TRANSFORMER-LAYER，Ch17 435–466完整“Residual从单一累加→Depth-wise Routing”：历史选择的activation/跨stage传输/inference I/O、blocksummary/boundedslots、checkpoint/runtime职责、浅模型/吞吐/带宽限制回退，已承载拟保留的depth-state/placement取舍；461–465另有DDL的input-conditionedcarry/write、非整层Jacobian保证、无实测收益及基线回退。Ch16/18开头交接已读。ShortSWA局部索引恒等只是报告中的解释性坐标，不为名称缺失强造书稿diff；已有正文不被说成已含该精确公式或已认证sequence普遍更快。拟低分已关闭＋具体已有覆盖（无书稿变更），需要非作者必要core与actualNC裁决，不能只凭topic类比认证。

## 2603.15954 MobileLLM-Flash — 2+2+2=6，具体 execution-search 缺口深入

[HTML v1](https://arxiv.org/html/2603.15954v1)必要§3.1–3.5/§4.1–4.2/Tables1–7、Limitations及AppB；出现HTML封面Aug24,2026的具体字段异常，定点取[PDF v1](https://arxiv.org/pdf/2603.15954v1) P0标题/作者/date实际March18,2026及arXiv v1March16、P4–P6对应搜索/训练方法、P13 AppB已回对，未把HTML日字段当首次公开。公开归属仍用已核arXiv日级夹证；不是later v2当本窗新版本。

新增不是BO名称或参数更小，而是硬件cheap-latency/expensive-quality评估预算分离，继承剪枝权重并短CPT作为候选排序proxy，实机先拟合latencysurrogate，再投放quality评估搜索Pareto；§3.3实际20candidate Kendall .74比较相同architecture从零训练与继承权重CPT的loss排序，不是2.6B→500B早晚排序。§3.2/图4另外以10k→120k步曲线提出早晚排序稳定的经验声明，不能由.74替其代签。100architecture/ExecuTorch/S25@2k中参数/FLOP与latency Kendall仅约.4–.55；不能把FLOPs省当latency测量。深宽/attention full,SWA,skip候选，600M calibration、8candidate/iter/200trial、2.6B短CPT，选中后500B distillteacher恢复与报告800B IFT费用（不替原文改错），训练hyperparameter未联合搜索。

必要反侧：AppB是在ExecuTorch1.1.0、1024prefillchunk、window至少1024/2k输入时ringbuffer完整矩阵计算的局部实现成本，才使SWA反输skip/普通attention；CPT window256不是相同runtimewindow，两者分账。相同skip count/latency而>3consecutive skip TQA8.8 vs33.2、NQ2.5 vs10，最终“禁止≥3连续efficient”是authorheuristic，与表>3不当成数学阈值。单S25/Snapdragon8Elite CPU/12GB、XNNPACK/4threads/W4 group32/A8dynamic/quantKV，1k/2k/4k、warmup后3runmean；batch/concurrency、output length、warmup量/SLO=Not Disclosed。多任务lm-eval0shot/5shot/25shot；quality结果与性能模型不同精度路线，不能默认量化同等质量。350M对LFM350M全部prefill反退(.91/2.78/5.33s vs .84/2.18/4.52)，650M4k8.48>8.24s，1.4B2k9.08>8.41s、1kdecode60.52<61.14；350MARC等、1.4BMBPP35.6<Llama39.6/MMLU47.89<49.3，up to1.8/1.6只局部。词表202k含有压缩单位差，token/sec不可当相同raw text服务；Nemotron因unsupportedJetBlock未测不能称所有对手均更慢。不授跨设备CPU/NPU、生产或能耗保证。

actual INFER-TENSORRT-LLM Ch49 500–527有GEMMepilogue→MoP等参数深宽混合/短恢复质量proxy→projectioncluster→稀疏layout；2044–2068有target measurement/cost drift和feasibility/ranking，但**没有cheap目标先拟合/expensive质量后投入、runtimeSWAchunk反成本及连续skip pattern关键反侧**。Ch48/50开头交接已读。本owner只execution约束的modelartifactsearch，不另写训练recipe/Tokenizer/模型层证明。拟在MoP反侧513后/cluster515前插一段＋静态本人注；下面是逐字PRE，需Source/actualowner/PRE独核与root窄锁，不先写。

### Mobile 一段逐字 PRE

当参数或 FLOPs 无法稳定排序目标设备的延迟，而每个候选的质量恢复又很昂贵时，搜索预算也应分层：从同一 checkpoint 剪枝并继承权重，先密集测量较便宜的目标 runtime 延迟并拟合代价模型，再把短训练的质量评估投向可能改善 Pareto 前沿的候选；短恢复只近似预测最终质量，选中后仍须支付完整恢复与任务验收。这样可以联合选择深宽与 attention pattern，却不能把较少算术量当成较少时间：[受限移动 CPU 证据](https://arxiv.org/pdf/2603.15954v1)中，chunk 与 ring-buffer 的实现限制使 sliding-window attention 在所测配置下反而更慢，连续跳过过多 attention 也损害检索质量。窗口、chunk、精度、backend 和质量 proxy 共同属于搜索合同，换设备或部署路径就应重新校准；该单手机实验也有更小模型或特定长度反退，不授普遍加速。搜索、短训练、最终恢复与兼容成本不能摊销，或没有可靠的目标测量时，固定深宽剪枝、成熟 attention 与未压缩模型仍是合理回退。<!-- source-family:SF-2026-ARXIV-2603-15954 -->

### Mobile 静态末注

- `SF-2026-ARXIV-2603-15954` — Daily `2026-03-19`补`03-18`自然日；[MobileLLM-Flash exact-v1 PDF](https://arxiv.org/pdf/2603.15954v1)与HTML必要§3–4/Limitations/AppB，2+2+2=6，具体execution-search缺口深入。只采用cheap latency/expensive quality分层、短恢复proxy与runtime pattern成本；S25/XNNPACK/W4A8/4threads/1k–4k，SWA chunk/window及连续skip反侧、局部速度/质量反退保留。不授跨设备或生产收益，未核代码或复现。
