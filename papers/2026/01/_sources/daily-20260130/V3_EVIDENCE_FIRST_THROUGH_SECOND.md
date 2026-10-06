# 01-30 必要原文审阅：第一/第二批
精确版本均为 arXiv v1，原始抽取见同目录 V3_CORE_<ID>.txt；没有复现、artifact 或生产验证。root实际核本15项证据笔记及决定性原源，必要命题/反侧通过，不第二次泛读附件。以下保留作者初次审阅时的潜在Books描述；最终WindowDiff/SuperInfer/FAQ/context整合POST、其余Only及日级判断在本日README，原有待比较措辞不是当前普通待办。

## [WindowDiff](https://arxiv.org/html/2601.20332v1)
评分修正为 2+2+2=6，不借成熟DLM cache原则加Durability。§3.1–3.2/图2–4在LLaDA/Dream、MBPP见活跃首16未解码位置与邻近buffer，远端低漂移；新解码位置短期仍不稳定，旧解码更稳定。§4外窗128、内窗16，仅phase边界滑窗：前phase decoded KV可缓存，本phase新decoded持续更新KV但不算logits；buffer复用KV，farfield剪枝，每32步refresh。§5/表1–2在FP32 NVIDIA A6000、GSM8K/MATH/HumanEval/MBPP同长度与cachebudget、无parallelFastdLLM/earlystop对照支持局部资源取舍。剪枝alone L16 Instruct HumanEval 27.4 vs55.5，L32回52.4，不支持普遍无损。§5.3过早refresh会冻结unstable刚decoded状态；过迟refresh又增加recompute/stalecontext。表3 headline99×比较静态最大1024 MBPP 217.8s vsadaptiveEOS2.2s，准确58.8→55.6，工作量不同，不能当同长度99×。
Books潜在差额：Ch45现有“DLM撤销prefix不可变”解释layer/block version及query-derived近似state，但未解释active/buffer/pruned三种角色与刚decoded稳定性phase。可窄补该状态生命周期，不外推其他模型。

## [SuperInfer](https://arxiv.org/html/2601.20309v1)
2+3+2=7深入必要部分。§3–5 RotaSched按waiting(now-arr-βF*TTFT_SLO)、rotary α*(now-lasttoken-βB*TBT_SLO)、running负runage排序，以HBM和transferbudget执行主动轮转；不是只在OOM才换出。DuplexKV在preempt前把fully-written块提前D2H同步，dirty部分才换出；双向copy不得同块race。block-first跨层连续+批量CUDA memcpy减少64KB碎片开销；C2C物理双向450GB/s但Grace DRAM半双工384限制方向并用。GH200 144GB HBM/480GB DRAM、400GBoffload、vLLM0.6.6.post1、LLaMA3-8B/Qwen2.5-32B/Mixtral8x7B、ShareGPT/LMSYSChat1M Poisson到达，SLO TTFT5s/TBT100ms，α3 βF.5 βB0 transferbudget2400。16GB双方8GB table1 naive1556ms→Duplex46.8ms，是transfermicrobenchmark，不是端到端SLO保证。消融低效swapengine加大transferbudget反而恶化TBT，调度与实际copy执行需协同；不推广所有PCIe机器、α3普遍最优或生产公平性。
Books潜在差额：Ch56现有完成operator后preempt、recovery/SLO与memory预算，但未承载“达到OOM前按双SLO虚拟滞后主动轮转，并受真实swapbudget约束”。唯一完整owner INFER-SCHEDULING；KV同步是该可执行机制必要依赖，不另章重复推导。

## [SATA](https://arxiv.org/html/2601.20267v1)
2+2+2=6标准。§III算法1二值mask位运算贪心排序O(n²)，把HEAD/TAIL/GLOB转入连续operandflow；K每head可变而Q固定count，故Q-stationary+interhead FIFO流水，GLOB退回常规。16×16 tilezero-skip。§IV controller SV+TSMC65nm综合/NeuroSim校准模拟、1GHz、32×32array；不是实芯片。TTST、kVT-DeiTTiny/Base、DRSformer，不是LLM端到端。包括TopK与scheduler代价；QK峰throughput1.76×/energy2.94×条件限定，Dk>=64或Sf<=24 scheduling<5%；Dk<32、Sf>28或tile太小会使ordering/zero-skip开销主导。仅报告局部数字与mask→物理dataflow条件，不授生产LLM收益。

## [T-Mimi](https://arxiv.org/html/2601.20094v1)
2+2+2=6标准。§3固定window transformer取代CNN deconv，新增4层至12+两linear waveformupsample，frozenencoder GAN/mel训练。§4同5M小时in-house语料基线，100客观/200pair×10raters，CMOS+2.32% CI[-.70,5.34]不能证明更优。TorchAO8bitperchannelweight/dynamicactivation QAT；表2 all4bit PESQ2.32、all8bit2.74，保留最终两transformer及两linear FP32到2.99（不是只两总operator）；最终QAT3.16 vsFP3.21。S22 80mschunk4.4ms/68.7MB vsCNN window5 42.1ms/window2 18ms/81MB，只codecdecoder不是整条TTS TTFT。Books若采纳应是接近waveform输出的重构误差放大导致混精度边界，不能泛化所有decoder最终两层不可量化。

## [VERGE](https://arxiv.org/html/2601.20055v1)
root第三校准授窄2+1+2=5候选（最终Books待证据核），不采“formal truth”。§3.3互相equivalent候选K3/roundtrip只证formula一致，translator可能一致错误。§3.4 SAT/MCS deletedclause反馈局部repair，MCS失败转soft/selfconfidence；strict strengthening只验证formula entailment。§4.2表2strict ARLSAT去MCS91.7→83.0；ZebraSoftOnly91→70.2；UnsatCoreOnly平均-10.9，是删除子句的纠错信息局部收益而非所有组件创新。router54stress94%不授通用安全。§4.4测试20B~30%validsyntax、120B/Sonnet>90；总结70Bthreshold未实测70B，不授阈值。§6 n>20 periteration15–30s vsCoT<2，greedy O(n SAT)不是SAT多项式保证。§7作者明确consistency≠事实/伦理truth与verifiedhallucination。倾向仅报告当前局部repair，已有solver/replan原则不自动Books新gap。

## [PoT](https://arxiv.org/html/2601.20379v1)
2+2+2=6标准，因预算/估算信号多读Appendix A/B/D受影响部分。§4每实例MCTS探索+可执行tests reward→transientLoRA GRPO，episode末丢弃adapter避免跨请求状态传播。code withoutLoRA37.14 vsfull49.71局部消融支持更新有用，未授所有任务性能。Appendix D backward281ms/forward192.66ms=1.46额外，节点/token近似预算不是equal端到端训练算力；静态各baseline实际call上限不同。Appendix A/B Table6明说measured OR conservatively estimated improvement并引用officialreportbaseline，故跨域、商业胜出、普遍节省算力不作为实测采用。Table7单迭代473.66ms需模型/序列配置绑定。当前仅报告机制和局部code边界。

## [FAEA](https://arxiv.org/html/2601.20334v1)
2+2+2=6标准，实际安全/对照影响读§II–IV。ClaudeOpus4.5/AgentSDK unmodified、absoluteend-effectorcontrol/get_obs privilegedstate，不是rawRGB；“demonstrationfree”不等zero-shot singletry，LIBERO试验10trial70.6%，取消presetlimit84.9%；ManiSkill14tasks×5seed60/70，MetaWorld48/50（两cheat/bruteforce记failed）。对照VLARGB来自原论文，作者明确非相同observation；LIBERO task0自动成功脚本还作后续例子。coaching迁移ManiSkill85.7→81.4、API成本150→220。§IV singleframework/model、仅simulation，highfrequency/contactdifficulty未来，不能说已替代VLA或真机安全。仅报告planningdominant可执行tool场景与资源边界。

## [FAQ](https://arxiv.org/html/2601.20251v1)
2+2+3=7深入§3/Thm3.1、AppendixA.1–A.3/B与§4–6。finitebank固定binarycorrectness不是未来真实用户总体；historicalBayes factors用于采样效率而非可信度。PAI estimate预测均值+inversepropensity residual，prob/pred仅依赖past，withreplacement。hybridvariance/activelearning配合τ/Nuniformfloor避免extremeweights。unbiased逐实例，但95%CI是nb→∞且variancepositive-stabilization、Lindeberg、conditionalvariancecontrol下渐近，不是任意有限预算保证。AppendixB去重抽样但沿原q权重破坏martingale，Figure6大预算miscoverage。两suite MMLUPro/BBH+GPQA+IFEval+MATH+MuSR，按releasedate2.2Khistorical/2.2Ktest，100seed，预算2.5–25%，historymissingMCAR。4–5×ESS是同CI宽估计查询数（1500 vsuniform7515），不表示5×walltime/全新OODbank保证。可能Ch66差额“自适应选题不可用naive去重+旧propensity构造覆盖CI”，先owner实际比较后决定。

## [d-PLENA](https://arxiv.org/html/2601.20706v1)
2+2+2=6标准。§III–IV separatedVector/FP/IntSRAM、reduction/exp/reciprocal/ArgMaxTopK/maskwrite、in-place覆盖logits，分片约4k趋饱和。§IV GPU LLaDA8BInstruct/MoE dInfer/vLLM采样占比最高71%依配置；TableII T1 B16 L32 V126k、VLEN512–2048 R1，2.53×只sampling，model()excluded。HBM2e/Ramulator、CocotbRTL+7nmOpenROADDC1GHzsimulation/synthesis不是芯片实测。Algorithm2温度Gumbelnoise略去未来补，不能声称所有sampling功能equivalent。仅报告减少GEMM之外samplingtail的具体映射，不授endtoend2.53或通用NPU架构已验证。

## [LinguaMap](https://arxiv.org/html/2601.20009v1)
2+1+2=5标准。§3四种prompt保语义控codeswitch/Englishdistractor/bilingualans，langdetectlanguageconsistency与taskaccuracy分开；Qwen3-32B code-switchMMLU准确60.5% vsmono51.77%，LC8.35% vs45.17%，不是中文等全部language普遍规律。§4logitlens/meanpoolcos只观察层结构，不证因果英文思考；BLOOM7.1B/Qwen3-8/32B。§5仅最后k层SFT+maskQRAtokens，business五科2500examples80/20，Claude3.5Sonnetverify/生成CoT，非business52科MGSM/XQuAD验，随机selective/fullSFT对照。最佳层数§5.1与AppendixE文字有2vs3层差，故不采用唯一通用k；只采用languageadherence可以不同于准确度、有限late-layer修复。无硬件性能/SLO主张，Not Applicable。

## [SAMA](https://arxiv.org/html/2601.20125v1)
2+2+2=6，安全信号深入受影响§2.1/§3–4/D.1/D.4–7。greybox可提交custommasked文本并读tokenlogits，还需referencebase；fine-tuningmembership不是不加条件的公开API泄露。mask5→50% T16，每步target/reference一对forward、离线N128子集m10 signvote+inverse-stepweights。LLaDA8BBase/Dreamv0Base7B，MIMIR6×1000member/1000nonmember+3NLP×10000，AdamW bf16 3×A100 batch48 lr5e-5，4epochearlystop，fine-tuning而非未知pretrainingmembership。Table1 avgAUC.81 vsRatio.62/TPR1%FPR.16 vs.04仅controlled设定，baseline查询T16；D.1同时写4MC平均，预算精确实现未artifact核。§3.3称centeredzero noise推出sign>.0概率.5并不由均值零成立（需median/symmetry）；因此不采用分布无关universalproof。D.6 tokenizer/architecture差异使reference校准变差；D.5 SOFT/DP等为该攻击下降不是已证全部privacy安全。D.7 Ratio1h32m00/Sama1h32m16只是指定benchmark，不授productionefficiency。必要机制/实测风险已读，Books仍需owner现状差额，不因安全高分自动写。

## [Order-Token Search](https://arxiv.org/html/2601.20339v1)
2+2+2=6标准，§4/§5/AppendixA.3–A.7。beam在block边界分叉order和token，prune score仅本次newlyrevealed块且以fullprediction futurecontext条件，不累计allrevealedprefix或maskfuture。LLaDA8BInstruct/1.5在GSM8K/MATH500/Countdown/HumanEval，对照lowconfidence、random/AR+MV、ARbeam、orderonly/tokenonly；scorer单独消融保持search相同。AppendixA.4 NFE S*K*L+B*K²*L，K4/S=L2/B=L32≈MV5 FLOPs，不是调度walltime普遍相同；主要beam3/5/8且temperature.2–1search预算应保留。A.5同temp.4Countdown K1 22.7 vsK5 34.4亦扩大预算，不单独证免费收益。A.7 Sudoku模型likelihood与全局合法性不相关时全部方法低于/近randomcellaccuracy25%，结构search不能补模型缺失约束knowledge。仅报告固定maskmodel的局部选择与搜索成本，不能采tokenlikelihood等于correctness。

## [Context-dependent feature drift](https://arxiv.org/html/2601.20834v1)
2+2+3=7，新增context-dependentfeature/steering portability而非借linear原则。§2Gemma3-27B-IT为主，岭/线性logisticregression factualyes/no方向，§3 Figure2反向prompt避免词形/behaviourconstruct混杂后，再用oppositeday+empty训练robust方向；heldoutconsciousness/chakras conversations，topicrelevantmargin反转generic大致稳定；offpolicyreplay/onpolicy都有，显式fictionstory弱。AppendixB.8另在answer前一token拟合direction并steer，chakras会相反效果consciousness相对一致，所以不可用某个长context成功授全context有效。注意该beforeanswer方向不同于主实验afteranswer方向，不能当同一probe证明因果；§4少量conversation/concepts、机制未知、非普遍belief改变或完整安全监测。拟Ch5差额需实际核existingcontextportability，未改书。

## [TaF-VLA](https://arxiv.org/html/2601.20321v1)
2+2+2=6标准§IV–VI/表I–III。同步tactile+6axiswrench+12×12pressuremap，N5滑窗force双codebookVQVAE reconstruction防collapse，tactileViT+causalTFsummary，InfoNCE对齐forcecode；部署不需FTsensor。7realworldforcecriticaltasks ACT/DP/π0.5及tactilebaselines，nohistory/小codebook/连续latent/forceexplicit对照；history消融支持瞬时纹理不能分辨staticgrip与incipientslip。SeenCustomA75 vs66.7、GelSight65 vs58.3；UnseenCustomB60.3 vs30、GelSight53.3vs23.3。仅相似visuotactilesensortypes不能推capacitive等普遍transfer；VI微米airgap/contact前控制错误未解，actionchunk慢于forcespike会失败，感测通道不等于fastsafecontroller。Chocolategentle任务vision可比，不授全部VLA必须touch。仅报告特定contact/historylatent取舍，Books候选差额需Ch23/26已覆盖论点核。

## [ProfInfer](https://arxiv.org/html/2601.20755v1)
2+1+2=5标准§3–5。libbpf/BCC uprobes解析llama.cpp/GGML operator/tensor/graph并关联CPU PMC/thread/expertID，QoS<5tok/s动态关闭部分probes，在token/graph与operator粒度间交易可见性；ringbuffer更轻但丢事件不报告，perfbuffer可知missingevents。OrangepiRK3588/OpenHarmony5.1 Ubuntu22.04/RubikPiQCS6490Ubuntu24.04，CortexA76 2/4cores，完整BCCdecode速度-2.8–4%、libbpf最低-1.7%（部分feature不支持），tok/graphonly-.1%。先验ONNX8%只是preliminary不同系统不能公平profiler优势。MoEQwen1.5A2.7B4bit8.9GB>RAM+mmap时expertdistance/pagefault定位diskIO，不能泛化所有MoE bottleneck。论文支持runtime动态probe取舍，未声称first-eBPF/全GPU完整可观测。仅报告局部工具与配置，现有observability lossbudget是否已承载长期链待比。
