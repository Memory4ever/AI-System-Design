# Jan31 Batch6 — necessary exact-v1 evidence

九项必要方法、对照与直接反侧已由root实际独立复核通过；FBS中心人口争议终态隔离通过，EWSJF按root要求把formal starvation/stability中心保障争议明确隔离（整项暂缓，不以经验结果替换准入）。以下历史提议保留实际过程，正式日报采用最终处置。发现范围不变；原题摘与具体准入改判仍在SCREENING。日期沿本日DATES的逐项submitted batch+公告schedule下界/DataCite上界；精确v1不是后版。除ZipMoE为2+2+2=6外，本批均2+1+2=5，评分只取新增机制/成立条件，不取成熟原则或宣传速度。未运行artifact/复现实验。所有Only为具体条件留报告，不冒称精确算法已有正文覆盖。

## 2601.21824 — DASH

- [exact-v1](https://arxiv.org/html/2601.21824v1)，[必要原文](CORE_STANDARD_21824v1.txt) §3–4/关键图表。
- 将deterministic attention backward的compute/reduce形成DAG：c/r constant、dependency边零成本、KV tiles与SM数匹配、每KV梯度按固定Q顺序reduce。Descending Q缩causal尾部bubble；shift/symmetric shift只在上述ideal DAG成立，Lemma1的isomorphic chains/monotone depth条件不是任意GPU全局optimal证明。
- H800/CUDA12.6/Triton3.4/FA3，BF16随机输入、总16384tokens、hidden2048、head64/128、长度512–16384。关键反侧：full mask16384的shift比baseline更慢，L2 remote sync代价；causal head128简单descending胜symmetric shift，后者额外约10register导致spill。理论critical path不含实际register/cache成本，实测不是无条件最优。
- transformer block fwd+bwd（不是完整训练E2E）：LLM batch1 length8/16/32k与其他full attention batch16 length4k；约2–10%/4%绑定这些条件。作者内部thousands-GPU叙述没有公开匹配控制，不采用大规模生产保证。Table1十次同一backward零deviation是局部算子determinism，不能扩成所有RNG/collective/checkpoint的全训练可复现；precision外、并发、完整模型/step/尾部SLO Not Disclosed于必要段。
- **仅报告提议**：TRAIN-PRETRAINING/Ch28拥有梯度数值与训练执行；本项局部reduce-DAG配方及register/L2反侧支持保守schedule选择，不支持普遍optimal或完整训练determinism。没有需采用的全系统长期修正，不为schedule名称改书。

## 2601.21623 — LAMP

- [exact-v1](https://arxiv.org/html/2601.21623v1)，[原方法信号](LAMP_SIGNAL_v1.txt)、[必要机制/实验](CORE_STANDARD_21623v1.txt) §2.3/3.3/4。Major revision已按CURRENT_SIGNALS定点核：v2是weighted componentwise目标变化，不据此否认限定v1 unweighted命题；不引后版历史结论。
- f(g(x))中用局部Jacobian/sensitivity选少量g分量高精重算，freeze computed low-precision reference。small perturbation/Jacobian稳定是条件，快速变化需Hessian，实际f/J也只是floating结果。matvec可重算分量；softmax同一输出需整体重算，composition选择不是任意DNN尾部免费重算。
- v1 unweighted softmax Ku=I−1z^T与weighted RMS分开；top-probability recompute说明局部策略，但不采用未读足/记号争议的完整greedy定理。Proposition3.6正文unweighted而末bound写Kw，记号冲突保留，不输出正式最优证明。
- GPT2XL/OpenWebText 200序列×1024，用FP32 reference KL/argmax flip，不是任务正确率。PSμ为FP32中手动round1–23mantissa/8exponent、不模拟overflow，scalar accumulation FP32/ties-even，不是native BF16/GPU kernel。作者3.4%/15%/34.3%重算对应约10/100/1000×KL改善只作数值演示，不转为runtime速度；硬件高效实现明确out of scope，hardware/batch/concurrency/端到端SLO Not Disclosed。
- **仅报告提议**：INFER-TENSORRT-LLM/Ch49拥有校准、表示与execution实现界，SCREENING早期Ch54仅是capacity联想，此处纠正owner但不改变贡献/评分。具体局部数值重算启发留报告，未核runtime收益和通用误差保证，不声称现章已有LAMP公式或强造长期实现缺口。

## 2601.21351 — A/F provisioning ratio

- [exact-v1](https://arxiv.org/html/2601.21351v1)，[实际原文](CORE_STANDARD_21351v1.txt) §3–5.4；v1原题Theoretically Optimal Attention/FFN Ratios in Disaggregated LLM Serving，不用后版题目冒充。
- rA–1F、每A full microbatchB且立即补槽、同步token cycle=max(A,C,F)。A latency随context线性、F随rB线性且compute-bound、communication随B线性且不依r，未建共享link contention。D几何随机长度、termination概率固定p、prefill均值有限、fresh slot立即补入，才有steady expected KV load与horizon-average approximation。
- closed form在A balance/C balance/FFN intercept候选中选r，优化average throughput per instance而非单请求latency/SLO。deepseekV3/Ascend910C trace校准系数，验证是discrete-event simulator不是在线系统；两inflight microbatch下A/F>2C才能隐藏communication。
- B256、μD500、μP100、N10000、r grid1/2/4/8/16/24/32，对比理论9.3与grid附近。只计前80% completion排除tail/drain，不是full-run交付吞吐；r32 simulation比expected model约低15%，slowest A的max load≠mean是直接反侧。精度/trace采样人口/独立repeat/并发/线上SLO Not Disclosed；不推任意长度分布、admission、KV容量或拥塞拓扑。
- **仅报告提议**：INFER-PD-DISAGGREGATION/Ch55已有attention/FFN的state/compute分工，本项具体解析比率只能在局部概率/通信模型下用，不是可采用的通用provisioning常数；不将本公式声称为已有覆盖，无Books diff。

## 2601.21473 — ScaleSim

- [exact-v1](https://arxiv.org/html/2601.21473v1)，[实际原文](CORE_STANDARD_21473v1.txt) §3–4/limitations。
- frontend提供relative invocation distance而非未来真实time：independent action remaining、交互min(action,physical distance/velocity)、predefined graph BFS hops。阈值prefetch仅替换inactive更远state；prefix eviction可以不备份CPU、之后full recompute，不叫restore同状态。估计可能由应用/LLM提示，不能授future oracle truth。
- SGLang0.5.2、Qwen2.5-7B单H10080/PCIeGen5 64GB/s，32B最多8H100/NVLinkTP。每agent逻辑adapter/prefix独立但实际adapter参数内容共用一套，测试memory churn不证明异质trained adapter能力。三类synthetic activation（AgentSociety变体空间交互/BFS）；20%active/25%resident、125上下及25–1000agents，非任意外界事件。
- SGLang radix无host与HiCache host-LRU均reactive，load时间减少但prefill/decode基本不变，decode占比限制gain。precision、input/outputlength、batch/concurrency trace、seed CI、p95/SLO Not Disclosed；不能把up1.74×推广所有sparse workloads。
- **仅报告提议**：INFER-GPU-MEMORY/Ch54实际L327–337 capacity vsplacement以及已知timeline的working-set handoff可承载约束，本项是具体simulation hint和memory policy，非未知未来负载普遍predictability，不冒称精确算法已有覆盖。无明确长期差额需写入。

## 2601.21686 — StiefAttention

- [exact-v1](https://arxiv.org/html/2601.21686v1)，[必要原文](CORE_STANDARD_21686v1.txt) §3/4/diagnostic与limits。
- 不优化孤立matrix SVD error，而以decoder-layer output error学正交projection：mean/variance→MLP→QR，每layer K basis共享/V head-specific。离线fullbasis后truncate50–90%候选，用uncompressed calibration inputs逐layer error surface和位置加权Pareto分rank；不界定误差经全模型累计，early/late权重2/1.75是配方不是定理。
- Llama3-8B、2RTXA5000 24GB、512WikiText2×2048、≤50epochs earlystop5、AdamW5e-3、K batch1/V4、FP16。EigenAttention在同校准data/protocol及KV footprint重跑，但额外learned calibration与SVD训练预算不同。Table1 full Wiki=7.79/C4=18.05/MMLU=.62，ratio.85为9.96/24.58/.60、.61 C4=40.06/MMLU=.40：仍损失质量；mild>.9的Wiki局部Eigen更优，不全指标Pareto胜出。
- §4.4诊断原文称(rK,rV)=(512,512)是half original per-head dimension，映射与实际head/rank含义未充分披露；不据此采5.2%/3.3%的因果解释。无需为此证明所有附录。wallclock inference/throughput/concurrency/SLO Not Disclosed，folding projection不等于net-cost免费。
- **仅报告提议**：INFER-KV-CACHE/Ch45持有质量门/恢复条件；具体layer-output calibration/rank权重与局部对照并未证明端到端quality-cost通用界，不将其精确basis/rank配方写成已有覆盖，也不强造正文差额。

## 2601.21758 — EWSJF

- [exact-v1](https://arxiv.org/html/2601.21758v1)，[决定性方法/证明](CORE_QUERY_21758v1.txt) §4.4/A2、[必要实验和limits](CORE_STANDARD_21758v1.txt) §6–7。
- Φ=q_i/(b+1)×(base+urg×wait/Cprefill+fair log(b+1))。Theorem声称positive fair即可starvationfree，但实际proof借positive constant urgency与queuefactor；learned mean-length weights与online adaptation没有强制保持正下界。wait priority增长亦不足证明无界arrival/竞争者下finite wait。此具体条件缺口才准入，不凭KMeans/bubble/metaopt组合。
- 4A10080、Llama2-13BChat、vLLM0.11TP，anonymized chat+long-context数据名字ND，input32–4096、80/20短长、Poisson10–40rps。precision/outputlength/maxbatch/concurrency/SLO/repeatuncertainty Not Disclosed。
- Table7 200k rate10 EWSJF req/s5.15<FCFS5.38，虽然tokens430.53>409.46，反驳文字全req/tokens双改善。Table8总tokens320783 vs401416，Table9 117625 vs134288，tok/s不是同工作量完成速度。long40queues61.88>30queues60.92与“peaking30”不一致；Table10 tail95p仅High/Lower，不作定量SLO。
- 正文formal guarantee与Limits直接说noformalguarantees/misconfiguredbias的争议保留。Bayesian5–8 trials×10–15min是学习成本，bursty/adversarial交通可能来不及适应。采用对象仅“正urgency/权重/arrival条件需核”，不采用无条件公平证明、headline速度或production部署。
- **争议/暂缓**：准入命题是fairness guarantee的实际成立条件，故整项按中心保障争议隔离，不以局部经验增益替换准入命题。Theorem A.1的wfair>0前提、proof所借wurg与qf正constant、adaptive权重及arrival约束均未接成可核保障，§7又明确否认formal guarantee；formal starvation/stability均未采用，不签已验证公平、不进入Books。INFER-SCHEDULING/Ch56仍是恢复owner；需作者统一定理/limits、显式权重不变量、arrival/competition条件与相应受控保障证据才重开。现有受限Table7–10只作双方争议证据保留，不授调度SLO。

## 2601.21503 — MAR

- [exact-v1](https://arxiv.org/html/2601.21503v1)，[实际原文](CORE_STANDARD_21503v1.txt) §2–3/Table1–3。
- ternary neuron {-1,0,1}的threshold=exp(a)>0、external input只在t0，之后residual membrane随时间更新，置于Mamba2/FFN输入输出projection前。此learned temporal interface是准入增量，SSM/sparseFFN/distillation组合或生物类比不是新保证。
- teacher Llamba1.4B、约7B GenQA/OpenHermes2.5/Infinity tokens一epoch。Table2 binary46.28→ATMN55.20→reverseKL55.46→pre-norm57.20；post56.75/both56.08更差。Table1ours57.20<teacher61.88，所有测试任务更低，不称dense质量恢复。prose57.93/5.45pt与Table57.20、Spike52.48（4.72pt）冲突，保留不照录headline。
- Energy是weight/activation/firing×假定MAC4.6pJ/Mul3.7/AC.9等逐操作估算，不是真实硬件energy/latency/E2E。traininghardware/precision/batch/seeds/具体timeT/τ配置 Not Disclosed于必要正文；teacher预算与temporal多步计算不能消失。
- **仅报告提议**：MODEL-TRANSFORMER-LAYER/Ch17拥有替代block的信息/执行接口；这里保留具体ternary时间更新和局部counter，不采生产低能耗/质量无损，单篇受限配方不改变通用block选择，不强造Books gap。

## 2601.21198 — ZipMoE

- [exact-v1](https://arxiv.org/html/2601.21198v1)，[决定核心](CORE_QUERY_21198v1.txt) §3.1–3.3、[必要方法/实测](CORE_STANDARD_21198v1.txt) §3.4–5。
- BF16 exponent(E)/sign-mantissa(SM)分开：E压缩与CPU解压、SM紧凑驻留/读入和GPU恢复形成不同ready时刻，DAG从I/O-bound改为CPU/I/O/GPU各自critical path权衡。采用这一具体component interface，不等同lossless+cache成熟组合。
- rank-frequency marginal stationarity→Bernoulli/conditional exact-k subset的DP cache partition，router correlation/drift不由模型保证。不采用未核appendix近似界或unconditionalplanning保证。实际原型融合E read/decompression OS page-cache，所以理想DAG组件成本非实测完美独立。
- HFTransformers、lz4/zstd、约2.6kPython+8kC++CUDA、contiguous pools/host-pinnedUMA zero-copy；Orin64/32GB Jetpack6.2.1/Ubuntu22.04/Samsung970EVO3.5GB/s，DeepSeekV2Lite/Qwen1.5MoE/SwitchLarge128 ShareGPT random matchedprompt BF16 unchanged。ZipDRAM20/10GB vsDeepSpeed18/10不是全等预算，pagecache参与收益，不纯algorithm归因。
- bs1/4/16，output cap不总等实际长度、mean及10–90bands不是CI。encoderdecoder skew收益更小，FIFO/Marking/LRU及wholeplanning消融不足独立分解所有CPU/I/O组件。sampleN/seed、CPUthreadK、其他operator精度、concurrency/SLO、offlinecompressionE2E摊销 Not Disclosed。
- **仅报告提议**：INFER-GPU-MEMORY/Ch54实际tiering/placement与kernel/runtime residency责任已读，但不冒称E/SM精确机制已有覆盖。component分解是受限BF16/Orin/cache配方，必要证据未建立跨format/router/topology通用收益，作为局部设计选择及反侧留报告，不凭名称或必然lowerfootprint强制书稿差额。

## 2601.21708 — FBS

- [exact-v1](https://arxiv.org/html/2601.21708v1)，[决定核心](CORE_QUERY_21708v1.txt) §2.2–2.4、[必要标准证据](CORE_STANDARD_21708v1.txt) §3/B1/E1–2，[中心split双方](FBS_SPLIT_CONFLICT.txt) B2/B7/E3及cais/mmlu官方card。
- causal本token状态→多个future horizon分布→连续preview，chunk boundary在线cache→skip gate是清楚潜在接口，仍保留5分准入。E1skip不计算本层QKV/FFN、prefix cache不变，但skipped current token KV位置/padding/mask状态未充分说明，不能授标准KV精确语义。E2 Bernoulli ST训练forward与部署deterministic threshold分布不同，不照录“no mismatch”。Stage1主文说不实际skip，而E3 surrogate-only SG operatingpoint依赖路径也需清楚绑定。
- 实验单A100、greedy prompt512/gen128、batch1主表与B4不同batchharness；relativeFLOPs是invocation计数，不等actualwallcost。B7≤1%近似parameter matched与主文strict/exact措辞不一致，4.00B rounded不是真实精确counts。E3noRL551ms/.72/MMLU56.3 vsadditionalRL532/.70/56.6；追加PPO预算不能当iso-training纯模块因果。threshold τ.9→.65时MMLU56.7→55.7是质量取舍，不是无损加速。
- **中心人口争议**：§3.1.2及B2称随机取5000 MMLU dev并去exactduplicates，官方cais/mmlu all/dev却285。官方card已实际打开verified上传commit c30699e；只引用必要count，不扩dataset审计。需要具体训练split/样本ID、是否变换/重采样、实际unique prompt数及held-outoverlap规则才能解释。不能将此假定为排版错，更不能靠bootstrap或“zeroexactoverlap”消解；未声称CMMLU的数量。
- **争议/暂缓提议**：不采用中心quality-speed/PPO人口与精确训练部署等价保证，不进入Books。机制只作为未经证实恢复线索，不借其提出全局新长期约束。重开条件为作者可核split/unique population与matched质量/预算，以及skip current-token KV状态和ST→hard选择说明；不因争议EX/降分/删反证。当前必要双方可读，是中心争议而非访问阻碍。
