# 首批其余六项必要证据与 owner 差额（待独核）

均 exact-v1，日级夹证已通过准入口径，尚未授本文件 Source/Books/DAY；原件 C1/D/E/F/G/H/I/J/K/L/M/N 均保留。方法与直接评价/反侧足够后停止，不遍历无关附件，不核artifact或复现实验。

## 15031 Attention Residuals — 2+2+3=7，深入

HTML conversion 缺正文，采用 exact-PDF §2–5.3；C1/D/J/L/M 保存。learned pseudo-query 是 input-independent 参数，key 来自历史 output 且 RMSNorm，因此权重仍 content-dependent；Full 存历史使 O(Ld)状态/传输增长，Block 保留N摘要并在块内普通累加。两阶段 online-softmax parallel聚合/块内 sequential更新、缓存跨物理PP的虚拟stage重复传输都是成本处理，不授任意旧checkpoint改接。

五规模194–528M activeMoE的8K context、同baseline hyperparameters/预算 loss对照，Full/Block优于pre-norm；1.25×是拟合compute-equivalent而非GPU throughput。48Btotal/3Bactive KimiLinear，54layers、9block+embedding=10sources，1.4Ttokens/WSD/Muon/batch8M、4K→32K，以同recipe对比。16-head同预算ablation显示SWA只有1.764 vsFull1.737，Block1.746；input-dependent query更好1.731却加d²projection/串行访问，multihead1.752反差、去RMSNorm退步。hardware、precision、serving batch/concurrency/SLO在拟采用证据中 Not Disclosed；128Kexample 15GB历史buffer经sequence sharding变约1.9GB不是所有环境成本，文中需chunkprefill配合。

Books 已有覆盖提案：MODEL-TRANSFORMER-LAYER [Ch17 431–455](../../../../books/part-02-model/17-transformer-layer.md) 实际含single accumulated→depth-history selection→blocksummary、有界slots、checkpoint/runtime历史状态/通信成本及旧residual适用域；这不是只同主题。拟采用命题已由正文承载，分数不因NoChange降低，不另写作者headline或未复现实验。作者 latency<2%/PP<4% 未绑定完整硬件/precision/batch/SLO，不授普遍低开销。

## 15202 LMetric — 2+2+2=6；具体调度差额深入

[v1](https://arxiv.org/html/2603.15202v1) §3–6，F/H/K/N。score=P-token×BS，P-token含当前待路由未命中prompt与queued prefill，BS含queued/running请求；两个量分别近似cache-sensitive prefill与decode负担，不是精确TTFT，更非统一PD两池/异构模型默认。高hit类份额x与持其prefix副本集合M若 x/(1−x)>|M|/|Mbar|，小P-token可能持续吸向已过载副本；1min窗口中首警报后，超过2×|M|个连续该类请求仍在hot副本得到更小multiplicative score才过滤（§5.2 L235–236），不是第二次BS超过其他2倍；两阶段仍是启发式，非稳定性/无阈值保证。

同一Rust指标框架重实现/调参对照vLLM/Dynamo/llm-d/Bailian政策，16H20(each96GB)、16instances、CPU160Xeon/1TB，vLLMv1 co-located，Qwen2-7B/Qwen3-30B，含hashedinput/outputlen/arrival的4trace，arrival缩至离线capacity半载，EOS后仍按trace解码数。chatBot/API/coderagent局部收益不是直接部署四产品的公平ranking；ToolAgent meanTTFT比llm-d差10%而TPOT好30%，simpleproxy有反侧。precision、具体vLLMversion、固定input/outputlength、productionSLO Not Disclosed；batch由trace动态不填固定值，量化/跨cluster不由本稿证明。

Books差额：INFER-SCHEDULING Ch56 465–493已区分route/placement/autoscale与latency model，1439–1441已讲prefix构造/传输/驻留，但未有乘积组合及cache热点失稳条件。拟最多两段插「全局Routing需要延迟模型」前，解释在同质co-located条件下为何simple乘积proxy可少调权重、以及上述热点检测/回退与费用。尚未PRE/写锁，不以genericcacheaware内容冒新增。

## 15340 DOS — 2+1+2=5；sampler具体差额深入

[v1](https://arxiv.org/html/2603.15340v1) §4–6/Alg1、A.2/A.3、B.1–B.3，F/H/K/L/M/N。每个masked row对observed columns的attention求和，head平均选高分先unmask，是本轮对已观测context依赖代理，不是attention列和的对其余位置影响；attention不是因果依赖或joint分布精确重建证明。可与EB累计熵约束的并行集合组合，不更改content predictor。

LLaDAInstruct8B/Dreamv0Instruct7B，HumanEval/MBPP256输出、GSM8K/MATH500512；singleblock/块32与top1/parallel协议分别验收。作者§6 headline allwins不成立：singleblock LLaDA MBPP38.4比best38.8低、Dream GSM8K DOS80.21 vsEntropy83.93，B表parallel也有反退。DOS+EB能降NFE vs相同EB uncertainty路径，但Fast-dLLM常更低NFE；A.2明确未用blockwise KVcache并优先比较解码策略；同v1的Table9 L478–497另报告有限TPS/Time，不能说没有wall-clock测量。该表DOS+EB有更高TPS却更差Time/NFE的HumanEval对照，也不授普遍加速。A.3主表按任务最优attention layer，B.3固定firstlayer另作控制，不能混成全部默认无调参。A.1 L335实际披露单NVIDIA L40 48GB、batch1、temperature0、seed42；precision/concurrency/SLO在拟采用证据中Not Disclosed，attention提取/排序额外访存不由sameforward删账。

Books差额：MULTIMODAL-GENERATIVE-PARADIGMS Ch24 465–519已有confidence/position/search及列和影响代理，691–706已有MI图选择；仍欠“masked-query到observed-context的row-mass”这条不同代理及接口。只拟一短段与现列和段并置，近文保留代理/矩阵物化成本、quality反侧/保守回退，不重抄joint概念。Ch23/25交接需读齐后再送PRE；尚未写锁/写书。

## 15401 SWE-Skills-Bench — 3+2+2=7，设计反证深入

[v1](https://arxiv.org/html/2603.15401v1) §3–5，E/L。49公开curated可unit-test skills、565新repo任务，固定commit与Docker/runtime，LLM生成要求/pytest后可执行不等gold需求oracle或独立完整testcoverage。WITH/WITHOUT局部多skills零observed收益，少数正向与三负向；baseline89.8%/many100存在ceiling，零observed不等统计等效。ClaudeCode+Haiku4.5单配置、Ubuntu24.04 CPU环境，不授跨model/scaffold、多skill retrieval因果；one-skill-per-task已preplace。token平均+10.5%是这套protocol，task-specificlimits、precision、temperature/seeds/repeats/productionSLO Not Disclosed，技能放置位置两节描述不一致不自行统一。

Linkerd near-match旧version/protocol模板会anchor并诱发不存在field与概念混入；这是受测trace解释，不是已排除所有confound的普遍因果。CPU taskcontainer不等模型推理硬件；CE定义在省token同时提高pass时可变负，故不采用作者正负标签背书净效用。采用结论仅skill相关性≠当前净效用、要固定WITH/WITHOUT并维护version。Books已有覆盖提案：AGENT-PLATFORM Ch84 1119–1123明确同task/model/decode/env/evaluator配对净效用与Load/Abstain、无益退回；846–855明确drift/依赖revision/退役。既有1123也含多skill条件边际收益，本稿尚未评价故不替其认证；不为diff再添benchmark摘要。

## 15530 DUET — 2+2+2=6；PD硬件分工差额深入

[v1](https://arxiv.org/html/2603.15530v1) §3–4.4，G/J。Prefill的matrix/SSM选择state-stationary systolic本地state与scalar重排，Decode选vector reduction/local register与高HBM；不把SSM逐token recurrence当普通attention全KV读。SystemVerilog+TSMC28 synthesis、RAMCACTI、RTL核过的cycle/events/NoI/Ramulator以及inhouse B200模型，是设计/仿真证据非fabricated DUET或实测B200。

FP16 prefill16chiplets×192arrays(each64×32)、192GBGDDR7/3TBs、4.4PFLOPs；decode8chiplets×96vectors、288GBHBM/12TBs、2.2PFLOPs；B200192GB/8TBs、2.3PFLOPs，两DUET700MHz vsB2001.8GHz资源不等，4×TTFT不唯一归因数据流。NemotronH56B/Zamba7B/Llama8B、4doc/chat/longwriterworkloads、batch1–128；长docbaseline>64存不下。§4.4明确不模拟multi-requestscheduler，只假设PDthroughput匹配与两池满载；真实concurrency/arrival/SLO Not Disclosed。SSM/KVhandoff与功耗封装另计，不授生产PD最优。

Books差额提案：INFER-PD-DISAGGREGATION Ch55 14–22、60–82已覆盖阶段差异/匹配/goodput，却未有阶段专用compute dataflow。拟一段紧接两种阶段节奏，解释prefill systolic/SSM state与decode vector/HBM分工不是“拆到同样GPU”同义，resource/scheduler建模与旧co-located回退近文；不讲Ch22模型SSM机制，不新增硬件细节章。尚未PRE/写锁。

## 15589 LEXI — 2+2+2=6；bit-exact transport差额深入

[v1](https://arxiv.org/html/2603.15589v1) §3–5.4，F/I/J/N。BF16仍1sign+8exp+7mantissa，Huffman只编码exp、sign/mantissa原样；weights离线、activation/KV/SSMcache在线，perlayercodebook/header、flitpack与ingressdecode才保证恢复数值。首512activation建立最多32entrybook；未见exp以24bitescape+8rawexp恢复，极端分布可扩传输，不因实验没exception授总是缩小/无额外cost。10lane8cache与四stage8/16/24/32prefixdecode在设计点摊startup/decoder瓶颈，不等所有形状singlecycle。

Jambatiny319M（另表称mini，原标签冲突保留）、Zamba1.2B/Qwen1.8B，WikiText1k/C4 2k输入+512输出，BF16，Simba6×6chiplet NoI100Gbps，modifiedcycleaccurateHeteroGarnet trace模拟。RTL GF22nm/1GHz synthesis再scaled16nm算.09%area不是physical芯片measurement；RTX3090用于entropyprofiling不等最终latencyhardware。communication68–95%主导的模拟有endtoend30–35%改善，非通用GPU解压/servingSLO。batch/concurrency/SLO/模型质量复现Not Disclosed；只bit-exactcodec语义，不授完整runtime实现verified。

Books差额提案：INFER-GPU-MEMORY Ch54 703–709已有bit-exactweights/GEMMtile ANS；Ch55 102–119已有PD exponentdensecode/escape/transfer identity，但没有在线activation/SSMcache perlayer wirecodebook+prefixfreedecode恢复和32entryescape的本路径。唯一owner拟Ch54「减少Bytes」分支，最多两段只解释运行中tensor lossless wire编码≠arithmetic精度变更、metadata/entropy/shortpayload成本及rawfallback，不复制PD transfer协议或长附件。尚未PRE/锁。
