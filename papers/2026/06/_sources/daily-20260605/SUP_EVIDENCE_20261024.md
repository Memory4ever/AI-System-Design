# Jun04 补窗：首批四项必要证据与最小融合提案

作者 supp_20260605_author，2026-10-24 Asia/Shanghai。实际读回reader SUP_REVIEW R1–R5：04511/04594/04236/05152准入及联合Jun04日期通过，不第三准入；04101及04920官方撤回排除，不评分/候选/Books。保原Kimi字段/6分/有效§4。四篇官方exact-v1 HTML已下载为本目录`SUP_2606.<ID>v1_20261024.html`，不是当前新版摘要的替身。均未运行代码/复现。下列评分只给新命题，不借成熟通用原则加分。

Books公共三上下文和ROADMAP已实际重读；actual owner论点及邻章开头已定位。S1–S3经reader R6–R8、root三个明确窄位新授权后已实际保存，reader R11唯一非writer actualPOST已通过，新增3I生效且窄位释放。S4无授权/正文，按R9双证明接口争议隔离；本句只行政同步既成事实，不第三Source/POST。

## S1 SparDA 2606.04511v1

评分2+2+2=6，标准要求；因actual owner欠learned selector改变attention语义的分责而深入必要域。原件§3–6、C的configuration/efficiency、D的CTA与no-prefetch消融实际读。Forecast从前一层hidden产生下一层block分数，GQA每组一Forecast head，KL匹配原selector分布，参数增量小不等无需训练：32H100上MiniCPM4.1 64K约48h，NOSA32K约24h。persistent UVA kernel把PCIe读取与层执行重叠，CTA占用SM，更多CTA不一定更快。它是学得的近似选择，不是只有physical prefetch、随后exact selector纠错的无损接口。

作者评价是MiniCPM4.1-8B与NOSA-8B、HELMET/LongBench/RULER/有限数学；dense仍在若干质量列更好。主H10080GB/PCIe5x16、附A10080GB/PCIe4x16、host2TB；NOSI engine，各setting一次warmup后两次均值，重复训练不明。默认复用上一decode的top-k，层0 KV和压缩Key留GPU。128K下较Sparse-offload至多约1.69倍decode，5.28倍是比no-offload允许更大batch，不是等batch延迟。layer0使SparDA可比Sparse更早OOM；B4完整prefetch略慢于no-prefetch，B64后重叠才明显。精度未在本次必要段明确统一，记Not Disclosed；arrival/concurrency分布、p99/SLO未测，不能授在线服务保证。

Actual owner `INFER-KV-CACHE` Ch45现Offload/recall段→HybridGen，已有selector proxy非truth；后方“从反应式Recall到预测式Prefetch”及Janus另有exact选择/补读，未承载训练一个新的跨层selector本身改变模型选择。拟只在Offload/recall段后、Host tier算分段前插一段，不改其他机制：

> 选择器本身也可以训练成跨层接口：上一层hidden额外生成Forecast，预测下一层要读的KV blocks，让预取与本层计算重叠；GQA还可让每组共享一个选择head，减少selector开销。这改变的不仅是搬运时机，而是实际选块分布，不能继承“原selector最终补漏”的exactness。有限稀疏预训练模型上的SparDA以蒸馏selector、压缩Key驻留和persistent搬运kernel换取这一重叠；layer0仍需驻GPU，CTA又会争用SM，小batch可因预取开销退步。训练、误选质量、host容量与全部搬运必须计账；近似或净收益不合格时，保留原选择器、反应式读取或FullKV，不由大batch峰值吞吐批准等batch加速与SLO。<!-- source-family:SF-2026-ARXIV-2606-04511 -->

## S2 Ekka 2606.04594v1

评分2+2+2=6，因silent failure诊断的具体知识缺口深入必要域§2–5及A1。model tree/code definition工具建立one-many/many-one语义映射，不能靠同名模块；hooks取得activations/call sequence，生成postprocess对齐layout/shape并做validation。Eq1分子为target低精度对reference全精度的误差`||X_T(low)-Y_R(full)||`，分母为reference低/全精度差`||X_R(low)-Y_R(full)||+epsilon`；不是target-low与reference-low直接差。归一后找最早持续上升而非单尖峰。1.5为经验阈值，1.5/2/2.5有限九bug子集稳健，不是通用容差定理。reference必须语义可信且可运行；单框架特有组件可不映射并说明，不证明全图覆盖。此处按reader R7实际原式纠正。

17 bug来自vLLM/SGLang已能合理复现的模型stack：排除了Blackwell/ROCm、过大模型、setting外及特殊并发/旧版cases，有选择偏差。Sonnet4.5与baseline同backend，各输出top3可疑module，5trials；pass@k是定位指标非检出召回，九case消融不混全17case。成本表仅LLM tokens定价最坏无cache约30美元/次，不是GPU trace/存储/复现总费用。A1 BF16/FP8无bug误差比与bug误差分离只是该人口。硬件、完整precision/负载各case不统一，p99/SLO不适用；不授line级定位、任意runtime或生产正确性。

Actual owner `PLATFORM-PRODUCTION` Ch73现“小结”后Accelerator Silent Corruption只处理硬件整数/GEMM校验，不含软件语义差分；不能把所有silent错误都归硬件。拟在“Accelerator Silent Corruption”标题前插两段，保持现小结及Review notes边界：

> 服务仍返回答案时，质量回归也可能来自软件语义而非设备bit错误。若有可信reference，可先按实现语义映射组件，再将两侧中间激活的布局、shape与执行顺序对齐；同名module不保证做同一运算，无法映射的节点应显式保留。定位可寻找归一误差首次持续上升的位置，把下游传播与一次尖峰分开；reference的低/高精度差提供数值噪声参照，却不能把一个经验阈值当作所有模型的正确性界。
>
> Ekka的受限模型stack对照支持这条诊断分支，不保证完整软件/硬件检出率：可复现bug选择、可信reference、hook粒度和对齐样例都会限制覆盖，top3组件的pass@k也不是实际修复成功率。Trace采集、双侧执行/精度参照、磁盘和LLM工具调用均付费；无reference、映射失配或特殊并发无法重现时，保留最小复现、版本bisect、人工核查及发布回滚，不由正常response或低误差比批准生产正确。<!-- source-family:SF-2026-ARXIV-2606-04594 -->

## S3 AXON 2606.04236v1

评分2+1+2=5，知识缺口触发必要深入§4–7、B、E/J/K。gate同时看pace/context deficit，attention×confidence和uncertainty构成facility-location coverage，greedy鼓励不同uncertain位置获得支持；固定k1与adaptive CVR不同，不照录为一个统一recipe。Algorithm1出现d_cov而定义为d_ctx的记号差，本次不用其逐行可执行处方。attention/置信度是代理，附G的界为额外架构/扰动条件，不是因果influence证书。Greedy cardinality近似界不保证真实token正确。

冻结Dream7B/LLaDA1.5/LLaDA8B，同base decoder、权重、data split、budget/stop，四math/code任务；8A10080GB集群、DAWN codebase。TPS包含commit selection，不把NFE替墙钟；较强gate/大候选集/更多anchor增加开销且低置信tail可污染后续。论文有限配置不证明所有质量列获益，precision/逐setting批次/独立重复未在本必要域充分披露，Not Disclosed；不授因果依赖、分布保持或AR替代。

Actual owner `MULTIMODAL-GENERATIVE-PARADIGMS` Ch24 Masked generation现“保守schedule…激进schedule…”段后→位置卷积段前拟一段：

> 先揭示哪些位置还可以服务于下一轮，而不只判断当轮哪些token足够安全：当剩余mask缺上下文时，选择高置信且能覆盖不同不确定位置的少量anchor，再继续原解码规则。AXON的受限分支用attention、confidence与pace/context gate近似这一支持度；它们不是因果依赖或正确性证明，错误anchor仍会成为后续条件。冻结backbone不取消attention读取、打分与选择开销。更多anchor虽可减少NFE，却增加选择开销并可引入低置信噪声；应在同decoder/预算下分别验质量与包含选择费的墙钟。代理失配或净收益不合时，保留base commit规则、小块与更保守schedule，不由training-free或少步宣告分布保持。<!-- source-family:SF-2026-ARXIV-2606-04236 -->

## S4 DistIL 2606.05152v1 — 必要机制已读，定理条件差异待独核

评分2+2+3=7，§3–5/B2/B3及§6coding/math、C对应预算实际必要读。Eq4在student实际访问prefix上拟合local teacher分布，teacher stop-gradient；Eq5不冻结student-induced状态分布，另有未来各prefix CE经score-function回传的项。只blackbox采teacher token可无偏估目标，不等单个最终label足够；实际top100最好，top1/full较差，blackbox可行性不冒实践全已验证。

**反侧：Prop4打印假设为logπT−logπθ在score span，B3却直接使用πT−πθ=πθ scoreᵀu，推得一阶mixture与reward改善。两者不能无说明互换。** reader R9已独立确认，不自行修原理论。暂不采用其单调保证、具体收敛recipe或“所有N改善”。另有第二接口争议：B1去掉`i<=t`的trajectory-score乘loss项，需要loss在对应prefix可测；但Algorithm1/§6.2的feedback可由整次rollout后的执行日志生成。Stop-gradient不使feedback独立于后续action，故不能无条件把Eq5称Eq4对任意rich-feedback的精确无偏完整梯度。只保留local teacher-CE与future-CE score-function作为作者实践surrogate的有效描述；这两个保证域均为具名中心争议，未批准S4正文。单局部保证还要求固定state人口、可微policy/合适Fisher及足够小NPG步；Theorem1另用有限ratio/KL concentrability、variance/recoverability与NPG-DistIL，不是神经SGD每步保证。

有限coding用Qwen3-8B、LCBv6公开tests反馈/私有tests评价；math738 hard训练和独立AIME等，GRPO在all-zero人口不能学习与rich solution feedback的对比，不能混信息预算。Local-CE和topK消融只在特定域，不认证普遍机制唯一因果。Teacher反馈、采样、全部训练/评价要计费；不是已复现。actual owner `TRAIN-RLHF` Ch31 Sequence reward与token updates错位一节，已有horizon/credit但未承载forward-CE的future-prefix项；待reader定理差异核后再提最小literal，目前不请求写入。

## 当前交接

S1–S3的必要Source/actual-owner/PRE经reader R6–R8通过，S2式和S3句已真实修正。root新授三个精确窄位后，三处四段及各true-H2 Review notes本人注已实际保存；新增全文、完整直接两侧及本人注均实际自读，scoped diff-check通过。reader R11已真实唯一actualPOST通过，新增3I生效且窄位释放，R12保存态核通过；本人注仅行政同步。S4 R9两个证明接口争议保留，7分不降，未获正文授权；其余有限来源/题摘仍ordinary，未签DAY/FINAL。
