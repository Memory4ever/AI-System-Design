# 18项补充完整题摘后有限判断/原始日期

本轮实际DataCiteAPI与current官方abs逐项读取；以下projection保留原submitted/registered/Updated，不是exact public，findable/client arxiv.content所有18均实际。注册晚于03/19T01Z不能推出nextday公开；Updated无官方公开语义。官方合法cs.DC月列表250两host都412255B，无分日heading，停止。当前current header/comments除17044明确withdraw外未见重要纠错说明；17917字符串correction是正文affine机制不是erratum；普通current v2不扩全版diff。

| identity/primary | v1 Submitted UTC | Registered UTC | Updated v1 UTC | 贡献/状态 |
| --- | --- | --- | --- | --- |
| [17063 Transformers are Bayesian Networks](https://arxiv.org/abs/2603.17063v1) | 2026-03-17T18:50:13Z | 2026-03-19T02:23:21.000Z | 2026-03-19T00:08:55Z | sigmoid架构anyweights→weighted loopyBP/acyclic declaredKB exact posterior；必须核假设，不外推allTransformer或hallucination不可scaling |
| [17170 PAuth - Precise Task-Scoped Authorization For Agents](https://arxiv.org/abs/2603.17170v1) | 2026-03-17T22:05:03Z | 2026-03-19T02:25:52.000Z | 2026-03-19T00:23:55Z | operatorOAuth宽权→NLslice象征calls+operand concrete值provenance envelope服务端检查→task operation权限而非提示约束 |
| [17884 DebugLM: Learning Traceable Training Data Provenance for LLMs](https://arxiv.org/abs/2603.17884v1) | 2026-03-18T16:06:21Z | 2026-03-19T02:42:52.000Z | 2026-03-19T01:24:30Z | 训练data行为难归因→provenance tag联合学习+source targeted testtime refusal→dataasset修复选择；不把selftag当因果证据 |
| [17917 Only relative ranks matter in weight-clustered large language models](https://arxiv.org/abs/2603.17917v1) | 2026-03-18T16:55:13Z | 2026-03-19T02:43:38.000Z | 2026-03-19T01:27:14Z | weights数值都重要→rank-preserving/scrambled control与multilayer scale drift→压缩rank≠全局scale保证 |
| [17946 CARE: Covariance-Aware and Rank-Enhanced Decomposition for Enabling Multi-Head Latent Attention](https://arxiv.org/abs/2603.17946v1) | 2026-03-18T17:18:35Z | 2026-03-19T02:44:19.000Z | 2026-03-19T01:29:22Z | SVDweight误差+uniformrank→activationcovariance factorization和fixedKV rankallocation→GQA→MLA conversion预算选择 |
| [17104 When the Specification Emerges: Benchmarking Faithfulness Loss in Long-Horizon Coding Agents](https://arxiv.org/abs/2603.17104v1) | 2026-03-17T19:53:35Z | 2026-03-19T02:24:17.000Z | 2026-03-19T00:13:05Z | 完整upfront spec评测→emergent约60轮design commitments→exposure audit及single-shot control揭示faithfulness loss；需控制相同暴露/预算 |
| [17174 Detecting Data Poisoning in Code Generation LLMs via Black-Box, Vulnerability-Oriented Scanning](https://arxiv.org/abs/2603.17174v1) | 2026-03-17T22:08:45Z | 2026-03-19T02:25:57.000Z | 2026-03-19T00:24:21Z | token一致性不捕获代码语义→多cleanprompt divergence+AST normalization recurringstructure漏洞扫描→blackbox poisoning detection边界 |
| [17484 Learning When to Attend: Conditional Memory Access for Long-Context LLMs](https://arxiv.org/abs/2603.17484v1) | 2026-03-18T08:48:18Z | 2026-03-19T02:33:22.000Z | 2026-03-19T00:57:11Z | 全局attention每token代价→tokenwise conditional globalaccess+Triton可执行稀疏→contexttraining/KV取舍 |
| [17771 Attention Sinks Induce Gradient Sinks](https://arxiv.org/abs/2603.17771v1) | 2026-03-18T14:31:21Z | 2026-03-19T02:40:11.000Z | 2026-03-19T01:17:34Z | forward sinks/activation共现→causalmask训练gradient concentration，valuebackprop intervention保sinks去massiveactivation→mediator反证 |
| [17044 Do Understanding and Generation Fight? A Diagnostic Study of DPO for Unified Multimodal Models](https://arxiv.org/abs/2603.17044v1) | 2026-03-17T18:26:29Z | 2026-03-19T02:22:55.000Z | 2026-03-19T00:07:12Z | 已撤回，不准入、不评分、不Books；保v1原文及当前withdraw理由 |
| [17677 Adaptive Guidance for Retrieval-Augmented Masked Diffusion Models](https://arxiv.org/abs/2603.17677v1) | 2026-03-18T12:54:50Z | 2026-03-19T02:37:58.000Z | 2026-03-19T01:11:39Z | 固定RAGguidance在diffusion噪声冲突→retrievedshiftSNR控制每denoisingguidance→contextprior权重选择 |
| [17902 Differential Privacy in Generative AI Agents: Analysis and Optimal Tradeoffs](https://arxiv.org/abs/2603.17902v1) | 2026-03-18T16:35:12Z | 2026-03-19T02:43:17.000Z | 2026-03-19T01:25:55Z | 只promptprivacy→enterprise邻接dataset token/messageDP温度长度bounds+utility优化→生成配置隐私预算；假设尚未核 |
| [17775 CoVerRL: Breaking the Consensus Trap in Label-Free Reasoning via Generator-Verifier Co-Evolution](https://arxiv.org/abs/2603.17775v1) | 2026-03-18T14:38:55Z | 2026-03-19T02:40:17.000Z | 2026-03-19T01:17:53Z | majorityselfconsistency伪label→diversitycollapse错误自强化，generator/verifieralternate过滤→label-free reward可靠性边界 |
| [17828 TINA: Text-Free Inversion Attack for Unlearned Text-to-Image Diffusion Models](https://arxiv.org/abs/2603.17828v1) | 2026-03-18T15:25:03Z | 2026-03-19T02:41:32.000Z | 2026-03-19T01:21:07Z | textalignment erasure=concept删→nulltext DDIMinversion+误差优化视觉probe→visualpath残存安全反证 |
| [17117 MosaicMem: Hybrid Spatial Memory for Controllable Video World Models](https://arxiv.org/abs/2603.17117v1) | 2026-03-17T20:19:44Z | 2026-03-19T02:24:35.000Z | 2026-03-19T00:15:11Z | explicit3D静态/implicitpose失准→3Dlocalized patch compose+nativeconditioning→保persistent与可动scene分工 |
| [17476 UniSAFE: A Comprehensive Benchmark for Safety Evaluation of Unified Multimodal Models](https://arxiv.org/abs/2603.17476v1) | 2026-03-18T08:30:31Z | 2026-03-19T02:33:11.000Z | 2026-03-19T00:56:24Z | 跨task安全评测fragmented→sharedtarget7I/O configs→imageout/multiimage/multiturn安全比较可控；不授safe排行 |
| [17639 VeriGrey: Greybox Agent Validation](https://arxiv.org/abs/2603.17639v1) | 2026-03-18T12:00:54Z | 2026-03-19T02:37:05.000Z | 2026-03-19T01:09:07Z | 黑盒输出只看成功→toolsequence feedback驱动mutational injection必要任务依赖→罕见危险tool coverage；不是生产安全保证 |
| [17541 Temporal Gains, Spatial Costs: Revisiting Video Fine-Tuning in Multimodal Large Language Models](https://arxiv.org/abs/2603.17541v1) | 2026-03-18T09:46:44Z | 2026-03-19T02:34:44.000Z | 2026-03-19T01:00:46Z | VideoSFT可自动兼顾image→framesbudget跨配置收益与static退步→hybridframe受限缓解设计取舍 |

17044当前官方[abs](https://arxiv.org/abs/2603.17044)实际withdraw banner；v2 history Fri22May2026T19:13:04UTC，Comments原文：Experiments are inconclusive: The claim that architectures such as Chameleon or Emu would exhibit stronger gradient conflict is not supported by experiments or analysis, and all experiments are conducted on Janus-Pro without evaluation on other unified multimodal architectures。DataCiteWithdrawn(dateInformation v2)同原因。当前paper撤回不采用其v1贡献，不记访问受阻。

首10 current comments修正：17019=28pages6fig；17111=15p6fig11tables；17172=CAOWorkshopICLR2026；17280=Workinprogress；17435=ASPLOS26accepted；17456=18p14fig；17803/17970/17123无Comments字段；17419=agent security等Keywords。history仅17019/17280/17456普通v2，无具体withdraw/correction标记，不完整versiondiff。

## 首10潜在项具体准入范围

| primary identity | v1Submitted UTC | Registered UTC | 具体潜在增量 |
| --- | --- | --- | --- |
| [17123 Security Assessment and Mitigation Strategies for Large Language Models: A Comprehensive Defensive Framework](https://arxiv.org/abs/2603.17123v1) | 2026-03-17T20:32:06Z | 2026-03-19T02:24:43.000Z | capability不替安全评价：同temp/token但版本/测试期混杂，保留potential不采安全排行 |
| [17019 Transformers Can Learn Rules They've Never Seen: Proof of Computation Beyond Interpolation](https://arxiv.org/abs/2603.17019v1) | 2026-03-17T18:02:28Z | 2026-03-19T02:22:20.000Z | heldout XOR近邻反标签/circuit及symbolic intermediates，挑战强interpolation-only架构假设（非普遍LLM能力） |
| [17456 Multi-stage Flow Scheduling for LLM Serving](https://arxiv.org/abs/2603.17456v1) | 2026-03-18T07:53:28Z | 2026-03-19T02:32:42.000Z | 未知preciseslack多阶段竞争→LLFapprox/deferpromote/RMLQ，改变TTFT网络调度策略 |
| [17280 The 1/W Law: An Analytical Study of Context-Length Routing Topology and GPU Generation Gains for LLM Inference Energy Efficiency](https://arxiv.org/abs/2603.17280v1) | 2026-03-18T02:15:40Z | 2026-03-19T02:28:25.000Z | contextKV并发×roofline/logisticpower→context分桶routing能耗界；WIP分析非hardware实测 |
| [17419 Caging the Agents: A Zero Trust Security Architecture for Autonomous AI in Healthcare](https://arxiv.org/abs/2603.17419v1) | 2026-03-18T06:54:47Z | 2026-03-19T02:31:46.000Z | frameworkmetadata→LLM解释与infra执行权限分离/audit高权target边界，target≠全部已部署 |
| [17970 Beyond Muon: MUD (MomentUm Decorrelation) for Faster Transformer Training](https://arxiv.org/abs/2603.17970v1) | 2026-03-18T17:37:31Z | 2026-03-19T02:44:56.000Z | polar大GEMM代价→triangularwhitening/fixedpoint/localquadratic条件，优化step非只loss数字 |
| [17111 Hidden Clones: Exposing and Fixing Family Bias in Vision-Language Model Ensembles](https://arxiv.org/abs/2603.17111v1) | 2026-03-17T20:08:01Z | 2026-03-19T02:24:26.000Z | model family错误相关破坏independentvote，family-aware投票及candidate breadth重排改变ensemble判断 |
| [17172 Noise-Response Calibration: A Causal Intervention Protocol for LLM-Judges](https://arxiv.org/abs/2603.17172v1) | 2026-03-17T22:08:06Z | 2026-03-19T02:25:54.000Z | inputnoise干预/slope检验暴露text与tabular judge响应差异，非noise稳健性的普遍证明 |
| [17803 Swarm: Co-Activation Aware KVCache Offloading Across Multiple SSDs](https://arxiv.org/abs/2603.17803v1) | 2026-03-18T14:59:16Z | 2026-03-19T02:40:56.000Z | stableKVcoactivation→offlinecluster/selectivereplication+runtimeSSDloadbalance，placement并行边界 |
| [17435 ZipServ: Fast and Memory-Efficient LLM Inference with Hardware-Aware Lossless Compression](https://arxiv.org/abs/2603.17435v1) | 2026-03-18T07:21:21Z | 2026-03-19T02:32:11.000Z | variableentropybitstream/SIMT失配→fixedformat/registerdecompress/fusedGEMM消中间流量 |

首次及额外17都只是potential，未证公开落窗/方法实验成立，不评分不Books。共同有界日期停止/重开如正式§5与SOURCE。

