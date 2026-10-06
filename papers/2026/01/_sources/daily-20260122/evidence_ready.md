# 已准备单项证据

## RAPIDServe — 2601.11822v1

采用精确v1 [原文](https://arxiv.org/html/2601.11822v1)，§3 Design、§4 Implementation、§5 Evaluation实际读；逐段材料[机制](./rapid_core.txt)、[评价](./rapid_eval.txt)。增量不是抽象P/D拆分，而是同GPU不同Python进程共享weights/KV IPC，decode独占allocator先把prompt确定需要的blockIDs交prefill，再收到完成消息，不复制KV；AMD CU mask约束两阶段计算资源，让phase并行不需重复权重或跨设备迁移。HIP graph mask在launch后不可变，按profile选满足ITL最低decode CU，heavy load分剩余CU给prefill，低负载允许P/D都用100%增强利用；异步one-step-ahead会产生无用额外decode token。mask不隔离HBM/cache/interconnect；GEMM decode受prefill竞争大，作者未消除此干扰。

评价为单机8×MI300X、ROCm6.4、基于vLLMv1 0.10.2rc3，对照vLLM0.10.2的chunked-prefill512/2048与4P4D disagg (TP4 each)。Dense图/文字在Llama3 vs3.1 70B命名存在不一致，MoE为Mixtral8×7B；precision Not Disclosed。LMSYS平均prompt2K、arxiv8K、Loogle20K，前两种截断10K、按prompt长度分层；精确output长度、batch、完整QPS扫点Not Disclosed。吞吐到饱和，不混为SLO goodput：TTFT限每1000prompttoken≤1秒；ITL dense100ms/MoE50ms。RAPID比chunked512吞吐max4.1×/avg1.7×，比disagg max2.9×/avg1.5×；Mixtral无disagg可比实现。dual-SLO goodput32×峰值来自接近零baseline条件，不能作固有加速；在非微小baseline条件平均4.9×。disagg p95ITL平均约比RAPID低2×但吞吐低，故非各目标严格优越。

支持：同设备co-location可用共享状态与受约束CU并行改善局部吞吐/SLO取舍，且资源partition范围必须明确。未证明：通用GPU portability、共享带宽性能隔离、production能力、每种SLO最优。没有运行/复现代码。

评分建议2+2+2=6，标准审阅已准备；仅报告：MI300X CUmask具体实现和该配置资源取舍不自动改长期“P/D phases may differ but colocated phases share resource”原则，也不能只因owner未收此recipe造Books diff。待root必要证据复核，不自授终态。

## AGGC — 2601.11864v1

采用精确v1 [原文](https://arxiv.org/html/2601.11864v1) §3Method、§4.3Ablation、§4.4RLVR、Limitations实际读。按functional type跨层聚合（query/value等）梯度，以group norm EMA `S_j=βS_prev+(1−β)||g_j||`生成上下界；低于下界也放大至边界，上界抑制，保方向；coefficient linear schedule使早期宽、后期紧。不同于一个全局clipmax，具体增量是跨层function-group与time-varying双侧band。

§4.3 timebound控制：Mistral7B GSM71.39→72.93/MATH21.02→21.42；Gemma7B GSM76.34→78.54/MATH29.56→29.84。β表MATH20.76/21.22/21.30/21.22/21.42，不是严格单调，不能照录“consistently”外推。§4.4Table5 GRPO vsAGGC：Qwen2.5-3B GSM87.9同分/MATH66.9→67.2；1.5B GSM77.6→79.8/MATH58.6→59.1；Llama3.2-3B GSM81.4→82.3/MATH49.0→50.2。局部training curve早期高KL后期低KL不证明普遍variance规律。Hyperparameters经验调节，>70B/新架构/更长context未验证；准确repeat/seed、训练hardware及precision未在已采用必要段披露，不宣称统计普保。

支持：此family提供与全局clip不同的group-wise双侧动态约束，局部SFT/RLVR对照可考察；不是所有参数clip都应改此band。评分2+1+2=5、标准证据已准备。仅报告：特定group/EMA/alpha recipe尚不足改变跨模型稳定优化原则，未确认长期缺口，Books No Change有实际理由而非因小模型关闭。待root必要证据复核。

## TOON — 2601.12014v1（root已准入窄反例，必要原源复核待同步）

精确v1[原文](https://arxiv.org/html/2601.12014v1) §3～4与§4.7读取。50paired生成，sameNLquery、等semantic约束，8模型GPT-oss20/120B、Gemma3 4/12/27B、Mistral7B、Llama3.3 70B、Qwen3 4B，RTXA6000、256GB/i9。模型都无TOON native support，TOON prompt给规范，未控制native-training intervention；capacity相关不证明training因果。

JSON对TOON平均tokens296.15→217.94，但decode duration9.724→10.007sec、render .990→.630、GCS .840→.513；XML472.528→239.205token、13.84→10.878sec；YAML275.518→233.5token、9.363→10.909sec。GCS=.2render+.8syntax，不是全部semantic correctness。std跨模型不能当50instance独立repeat置信区间。排除firsttoken前promptprocessing，未测retry/repair；因此单次outputtoken减少不能证明端到端效率。CE方法称token-derived，setup称CodeCarbon估计测量，二者解释未充分一致；不采用节能数字/统一green ranking为系统结论。precision/quantization、batch/concurrency及SLO Not Disclosed。

仅建议采用局部反例“compact syntax不等于schema成功或decode低延迟”，而非native support强因果或可持续生产。2+2+2=6；局部数据仅报告，不新增format名称为长期owner缺口。
