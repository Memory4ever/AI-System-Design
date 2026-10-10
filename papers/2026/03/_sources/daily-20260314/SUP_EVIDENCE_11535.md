# 11535 Expert Threshold：必要 Source / actual Ch21 NC

mar14_supplement；精确[2603.11535v1](https://arxiv.org/html/2603.11535v1)，本地`SUP_NECESSARY_11535.raw`，请求实际200/493393B/14:19:55UTC见`SUP_ROUTING_DECODE_MANIFEST_RESULT.json`。完整题摘/唯一v1/history、DOI/题名与当前说明已核，无具名早稿/纠错/撤回信号；abs第一作者Hanchi Sun而HTML为Ryan Sun，原差异保留，不声称全部署名字面等同。题名、ID、DOI与正文机制一致可限定同稿，不追全版本史。owning/findable DOI/official URL/arxiv.content、registered Mar13 01:57:47UTC与Thu04:45:48UTC v1，结合已有效官方availability下界夹证Mar13BJT日级公开，不以注册/提交单独作首次正文日。

原fixed top-k compute或per-batch EC严格负载约束→per-expert过去batch kth-score EMA、当前token独立比较→在variable fanout/期望balance与因果Decode之间取舍。**2+2+2=6标准完成**：实际人口cutoff替代相对batch选择，改变训练/推理接口及资源波动，非借EMA或负载均衡成熟原则得分；不以Books NC减分。

## 实际必要原证

实际§2–3/Eq1–6/Alg1全行、§4.1–4.3.6/Tables1–2必要比较与主要反侧、§5.2–5.4继承关系、§6；B.2/C.1必要表/C.1.2/C.2/D评价、E.1/E.3/E.4、F.1直接capacity条件。不读所有fanout图/逐层diagnostic、理论附录完整证明或代码，因为采用命题是有限机制与实际边界，不是EMA估计population量化或充分统计保证。

Eq6 `r_ti>c_i`二元选择，输出用sigmoid原score而非softmax renormalization。Alg1先用旧cutoff选择，再只在training以当前batch kth-largest更新EMA；inference不更新。目标`E[z]=1/E`是population期望，不等每batch/每worker精确平衡；EMA of kth statistic只是估计，数据漂移/冷启动或cutoff revision不同不能授固定error界。warmup为4K EC/TopK-selection steps，不称训练全程无future batch依赖；冷启动no-warmup触发starvation。共享expert始终存在，零routed专家不等总FFN为零；varyingfanout更不自动是可靠难度估计，Figure5 ET loss-bin非单调。

F.1训练每expert `(1−C)N/E`至`(1+C)N/E`、C=.5，超额drop/不足pad；推理不施该约束，因此本文摘要“no train-inference mismatch”不作为无条件保证。作者warmup后低触发只能支持所测人口。Table8 shared improves CE但ET-no-warmup CORE16.867低于no-shared18.515，不能说所有质量都受益；§4.3大batch EC与ET接近，小batch EC退步，不授任何batch都等价。TC也固定fanout并非无用约束，严格latency/memory下仍合理。

Nanochat从头train d12 575M/195M active、d20 2.4B/561M active，16 routed+1shared、FineWeb-Edu10B/11.2B、seq2048/.5Mbatch，d20half minibatch/GA2；Muon+AdamW、单node8×B200180GB。TC ScatterMoE而EC/ET自写PyTorch/自写EP All-to-All/padding，不能把CE token-sample效率直接升为matched kernel wallclock/通信throughput。Table2 CE2.687→2.620及CORE22.31→25.14是作者有限设定，1.6×fewer tokens不是1.6×trainingtime/productionservice。precision、在线concurrency/deadline与完整费用/独立重复CI本轮未核为披露，不补造；可选代码未审、不声称复现。

## Actual owner 与具体 NC

实际顺读Ch21完整435–507相关论证与Ch20/22入口；ROADMAP `MODEL-MOE`。Ch21 **467–490「从 Batch-relative Balance 到 Population Routing State」**已逐字承载fixed-k predictable compute→EC batch-relative→per-expert historical population quantile/EMA→causal variable fanout，以及strict batchbalance改瞬时波动、cutoff/warmup/capacity/drop/分布作为checkpoint-adjacent state、coldstart/domainshift/revision失配、零路由/负载burst/OOM、训练drop/推理uncapped的gap、fixed-k/offlineEC共存与guard/rollback工程交接。不是仅相同主题；这些正文已经支持本稿可采用的具体设计选择。

最后stateversioning/guard/rollback是现有书稿工程推论，不认证原稿已实现这些controller。无需把4K、C或CE数字堆入长期段落，也不借NC补造新difference。**已有覆盖、Books新写0**；mar13_admission_review实际必要Source与上述完整局部/相邻入口核验通过，见本日SUP_INDEPENDENT_REVIEW_20261009.md。无需Books写入锁/POST，不授整日DAY。
