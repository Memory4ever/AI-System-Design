# PCR23049 / CPU22774 — Source与实际已有覆盖

作者supp_mar26_fresh；两家族完整v1题摘、official availability+findable日级25BJT已reader独校。原7分保持，深入本次采用命题及直接反侧；没有把Books覆盖当准入排除。

## PCR23049v1

实际读exact-v1 §2.2、§4.1–4.4、§6.1–6.4、§8。只有完整相同前缀的KV可精确复用；chunk即使相同也依赖祖先，leaf eviction维护树依赖，queue前视影响replacement/SSD→DRAM预取；CPU→GPU三stream逐层加载/计算/offload，前提是每层搬运能被计算覆盖。小KV、低/过高到达率、少prefetchleadtime、window失配可少收益或回退；Only-Down在Qwen7B优于Up-Down直接说明pipeline同步不免费。

评价为vLLM共同backbone、Wikipedia/SQuAD/MiniLM、2documents/平均6.8K输入/16输出、Poisson0.5–1req/s，重复率40%/35%并有不同有放回oversampling；A6000或4090单/双GPU、DRAM/4TBSSD/PCIe4，precision未披露。§3 SSD约3GB/s读/0.5GB/s写，与§6『3GB/s读写』有口径差；§6.2 Fig15/16尾值叙述及数量级不能认证通用tail/SLO/生产能力。收益只绑配置，不借最大2.47x概括所有engine与总成本。

实际Books已有覆盖：Ch45『从反应式Recall到预测式Prefetch』L961–975中的waiting-request prefix→tree future-use→tier预取→layer overlap→identity验证/ordinaryload，及紧邻边界明确CPU/GPU容量污染、queue过期/I/O竞争、弱reuse/SSD动态回LRU。采用命题的独特联动实际位于正文，不是Review notes；SF-2026-ARXIV-2603-23049绑定已在正文。前文反应式host-tier与后文TempoKV timedcommit保留不同owner阶段。本次不新增Books：不为覆盖已有联动重复写段落，必要原文新鲜复核仍须通过。

## CPU22774v1

实际读exact-v1 §III、IV/V必要core及VI受限讨论。vLLM V1多进程即使process separation/CUDAgraphs也共享cores：tokenizer争用延后launch，collective等迟到worker、shared-memory一writer多reader轮询争用会延后调度元数据；加核可缓解CPU瓶颈但不是所有慢系统保证，poll协议对慢reader的结构依赖也非单加核彻底消解。正文1.36–5.40x绑定Llama3.1-8B/Qwen2.5-14B、4/8GPU H100/H200/Blackwell、(#GPU+1)对最高8cores/GPU、attacker1.8K–114K、victim2.8K、8/16RPS、5连续victim/十runstd、200s timeout；不是v3的agentic实验或1.47–7.11x，training外推仍futurework。数值不写新Book，不采云价格为当前费用。

实际Books已有覆盖：Ch56『GPU调度之前，Host Control Plane也要有容量合同』L800–812具体拥有host-core affinity/launch queue/tokenization/shared-memory/progress预算→CPU隔离/准入→GPU提交→idle溯源；近文保额外CPU成本、consolidation/NUMA/fabric转瓶颈及host薄/GPU满时旧GPU-first成立。SF-2026-ARXIV-2603-22774已绑定正文，后文multi-tenant阶段诊断及DPU/device控制权分支并存，没有把加CPU写成唯一升级。因此本次No Change；不借旧标题/完成标签当证据。

两项正文存在但本日旧actualPOST收据不包含它们，不能伪称旧审计通过。请本轮非writer实际核必要源、上述owner/前后交接，判定具体已有覆盖；不申请共享Books写锁。未复现、未核全部实现，尚不授日级完成。
