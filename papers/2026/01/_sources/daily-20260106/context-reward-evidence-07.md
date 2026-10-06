# Jan06 已知末批context/reward命题

只处理先前已知00348/00376/00452/00664及明确局部配方排除，不新增库存。精确v1缓存实际heading与checked可复查；缓存不等所有附件已读或日级通过。

## InlineCoder 2601.00376v1

actual完整HTML AB（abs原摘要缺实验尾）及§3.1–3.4/4.1–4.4/5.2/6.2。draft→caller参数替换、return转result、downstream AST+LLM名字union/substring检索，真实新的context表示分支，拟2+1+2=5。§3.4 PPL由§4.4 Qwen2.5Coder1.5B辅助model而非生成器估计，quantile40/40/20阈值不是正确性校准；repository dependency oracle来自dataset。Python/三个backbone/A40等、EM/ES/BLEU/IDF1，明确无Pass@k，不能把重写context的semantic equivalence或下游测试正确当已证实。naive identifier substitution/return normalization不自动保capture/earlyreturn/effect语义；此表示只是prompt派生view，原source仍保真值。actualCh75 72–97/310–317/444–463已有dependency sufficiency/原文派生view/no-confidence-authority，尚需root定点具体Existing或窄gap判断。

## RU 2601.00348v1

actual完整AB、III-A/III-C及IV-B1/IV-A models/data/IV-B2。FR/FT/FF由NLI拒答、BM25Wikidata及外部judge生成，fact/token由Yi-Lightning映射，再按类别改变logit公式；增量仅局部score recipe，拟1+1+2=4，仅报告不进一步采用，不能把external classification带来的AUC当intrinsic calibrated uncertainty。77fake/加50real、四model、5sampling/beam5/T1/100tokens，Table3/4部分ChatGLM/Llama退步与分类误差保留；未采普遍0.1–0.2增益、truth保证或无外部成本。无实际部署安全constraint变化/纠错信号，不因可靠性口号全附件深入。

## TGE 2601.00452v1

actual§4.1–4.4、5.1数据/baseline与kernel/horizon消融、A2实现。offline轨迹diffusionencoder、单位球embedding、expert topm距离重尾kernel为LfO reward，拟2+1+2=5的替代。D4RL MuJoCo/Adroit、mu包含200或30expert trajectories且额外DE仅1trajectory，三seed，IQL/ReBRAC依赖明显、cloned door/hammer失败；不证明全部disjoint支持或无state-aliasing。硬件/precision未披露，不采普遍效率/成功保证。

中心recipe冲突：§4.2 Eq2 mean f(d/σ)，f(d)=exp(-d)，Alg1 line7 f(-d/σ)反号；A2实现又logsumexp(log-kernel)而非mean kernel。奖励的非线性变换不自动保持RL最优策略，不能自行替作者修正并把主表归因统一公式。精确code/config或勘误须给actualreward、state-only与state-actionencoder输入映射、run对应表；中心reward/performance暂缓，不因此把一般trajectory表示事实判无效或降分。root待必要核。

## Avatar Forcing 2601.00664v1

actual完整AB、§4.1 InteractiveMotionGeneration/TrainingInference、4.2、5.1/5.2/Metrics/HumanStudy/5.5两必要ablation、B2架构/D5定点mask对照和limits。motionlatent一步一frame，dualuseraudio/motion与avataraudio编码→block DFoT rollingKV；synthetic loser来自另trained avatar onlyaudio（不把成熟DPO当新增）。拟2+2+2=6。H100/10NFE/25FPS；latency预提audio，只motion生成，22human×8video有限偏好，不授E2E500ms/所有expressiveness或lip/visual质量全优。

strict causal/onlineavailability中心未决：Eq5 floor(j/B)≤floor(i/B)+l把lookahead写block，文l称frames；setup又B=5blocks即10frames/block，与mask B blocksize身份不同。future noisy states、condition window与真实可得user inputs必须分别明确，不能仅causal名称授零future lookahead。有限block生成机制可报告；exactmask/index/online条件可用时再重开strictcausal或延迟保证。视频maskablation为视觉定性，不伪称已观看。root待必要source/owner核。

## 已知局部recipe4与贡献负侧

00509 SAFE-C：完整AB仅既有RAG repair、compiler/CodeQL/KLEE multi-tool feedback组合；1+1+2=4拟关闭，未采漏洞减少headline或semantic/security完备，无实际checker contract新变化或设计反证。

00270 RectifyingAE：完整AB新增classifier re-attack越decision boundary的局部rectification，不是基础模型组件或真实physical部署安全contract；1+1+2=4拟关闭，不采自主驾驶安全/任意attack保证；安全应用举例不自动全附件深审。

以下完整AB具体贡献前关闭，原v1题摘位于exact-v1-screening-*.jsonl，不列正式候选或评分：00202 TKG为LLM teacher→轻量temporalKG task distillation，未披露基础模型/系统新机制；00245 intra/intertoken neuromorphic综述只是已有SSM/sparseassociative框架归纳，无新反证/评价；00254五CWE数据上RAG/SFT/dual-agent比较，只task指标与既有expertcontext组合；00368 32³ artifact修复的mask+3DU-Net occupancy/color损失，无foundation生成机制增量；00388 GPS层级标签+Haversine reward定位配方，不以RL/VLM标签准入；00411 Wiki/Wikidata弱标注+LLM过滤LuxNER corpus，不是judge普遍有效性/失效新证据；00444三轻量encoder/三个classificationtask排序，未给改变系统设计的新效率条件，no-single-best是既有取舍不计原创；00446 forecastingTSFM→anomaly PEFT任务比较，未披露新的adaptation机制或可复用失效边界；00553 96K真假图像/五generator数据资源，不发现crossgenerator盲区、污染/机制反证，数据规模非准入理由。关闭不代表无学术价值，未把全部156metadata升为候选或强制逐项队列；root分层抽检尚待。

root非作者已实际复核本文件具名中心决定性原段，受影响保证隔离终态通过；此记录不授全篇无错误/代码复现失败/性能普遍性，也不替代其余家族或日级Gate。

## 最终处置同步（2026-10-02，日级Gate待root）

当前最终处置：Inline5具体已有覆盖Ch75；RU/SAFE-C/Rectify4局部recipe关闭仅报告；TGE5和Avatar6的中心reward/单位与online条件保证隔离终态。root必要原段/owner或完整AB关闭校准通过。九项普通贡献前关闭的原完整AB与具体理由保留，最终root按来源/主题/理由分层抽检汇总，不把它们变成必须全文读附件的队列。

root最终分层抽检已实际读00202/00245/00444/00553的完整v1题摘，四项具体关闭理由通过；不称九项或156metadata全量独立审阅。00129另在photonic-admission-reopen.md定点重开，不借这些样本替代该家族判断。
