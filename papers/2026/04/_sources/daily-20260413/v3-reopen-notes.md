# 2026-04-13 V3重审记录

窗口：2026-04-12T09:00:00+08:00 ～ 2026-04-13T09:00:00+08:00。作者apr02；实际读取日期2026-09-26。旧报告完整存于v2.1-report-before-v3.md，不复用其DOI-created归属或泛化Evidence/Books结论。

## 来源与日期初步校准

机构目录真实读取停点复用Apr11 v3-reopen-notes.md中跨过本窗的未变化查询；仍需逐来源在本日报写清，不能说全源二次抓取。arXiv正常Sun04-12 20:00EDT槽为Mon04-13 08:00北京。旧504身份库存08549～09547的v1 Updated00:00:04～01:04:54Z，后段有跨09:00字段，日期例外须定点隔离；此字段不是首发本身。

Seed官方Papers目录Continuous Adversarial Flow Models，PublishDate Apr12T16Z落本窗，但目录事件不等于论文首次公开，需按真实arxiv/作者版本合并。旧15候选不自动retain，宽库存只做全标题查漏+有贡献可能性的定点完整题摘。

## 已形成证据的小批次（分母尚未冻结）

- `2604.08565v1`：官方HTML §3、§5–8，hard binary tree的同一线性响应负责routing与输出，stop-gradient branch；GELU位置改变路径梯度、利用率和剪枝。对读Ch21相邻Dense/Top-K与granularity论证，已在“树形条件计算”段作实际最小整合，root完成非作者原文/正文复核通过。26B scratch比较与利用预训练Attention的FT不可混为同预算；§8 theoretical/simulated边界阻止把Table5当生产加速。暂拟2+2+2=6，必要机制缺口深入完成，日级采用归属仍待批次冻结。
- `2604.08584v1`：官方HTML §3–4。Prefill把Query子空间centroid→key Top-L短表离线构造，Decode近邻centroid检索后合并并加recent window；完整KV仍线性存储，新增key维护短表，不是固定总内存。对读Ch45现有binary-key score estimator、query-dependent recall与prefetch；其write-once/read-many索引是明确机制差异，已向root请求Ch45锁。双EPYC7513/1TiB RAM/1或4A100、三7B/8B模型；Table3 step2 schedule 50.81 vs Full52.41反驳正文“全部差距≤0.6”，CPU-GPU预建索引8K/16K相对H2O0.88×/0.97×非全面更快；未披露线上并发/SLO，不外推生产。
- `2604.08585v1`：官方HTML §3–5。CPU少量key-norm anchors先给query上下文，取critical-middle-layer的K挑token，再按层prefetch/recompute；SGLang radix chunk identity与Triton绝对位置mask保证访问合同，不证明未重算KV语义exact。Ch45现有chunk位置/seam与层级prefetch承载背景但没有此selector→recompute流水线，等待root锁。单A10080GB、Llama3.1-8B/Qwen3-8B/Mistral7B、三个多跳QA数据集；40%recompute为受测质量结论，QCAll/QCLast为emulated比较，平均ROUGE/TTFT不构成端到端tail-SLO。

## 准入与版本污染纠正

root独立完整题摘首批校准支持08556/08557/08584/08585/08706/08720/08826的具体机制或设计边界进入证据审阅，未证明全部分母。08885不能仅因encoder或conformal标签关闭，需对照真正已有命题；08618只做必要机制消歧，不自动全文扩池。08557/08906/08988/09459的旧库存含后发标题/摘要，已重开官方exact-v1题摘；不得把后发DefenseInversion、EvolutionaryFlywheel或69篇至July31审计写成本日v1。

Google Vantage Apr13日精度文章完整核心原文读取：188名18–25岁NYU学生、LLM-avatar/rubric评价未来人类技能。它有受控实验而非无证据，但任务对象为人类教育技能；所用对话编排/评价未形成当前模型与Infra的新设计边界，前分母关闭，不因未标时区额外扩材料请求。

## 补充准入裁决

`2604.08885v1` 不按encoder身份拒绝。必要消歧读取§4算法/§5.4–5.7/§6：中间层kNN正负邻域距离比、CLS/flattened与PCA，reference仅正确训练点而calibration不得按正确性过滤；marginal与class-conditional拆开，BERT/RoBERTa GLUE/SuperGLUE中少数类严重undercoverage。其受控反证与release/calibration主线相关，暂拟1+2+2=5标准审阅，Books现Ch66“Continual Update同步Calibration State”、Judge区间的marginal限制及分布/切片合同已承载主要设计边界；不采用作者将标签不平衡直接等同exchangeability破坏的泛化解释，也不外推开放generation。最终Existing需独立逐命题裁决。

`2604.08618v1` 必要消歧读§2完整pipeline/§3.1–3.3：其VFS text-only skills/no arbitrary scripts，固定已验证tools；four-dimensional failure分析→分类聚合→映射skill section→minimal versioned编辑；1883tickets/3737任务，dev/heldout分离，Qwen3-Max+LLM consistency judge、三次离线评估。它不只是名字组合，但这一链路目前Ch81 declarative assets/runtime authority、nodeblueprint诊断、split-gated self-evolution已明确承载；作者domain-vsgeneric既换创建模型也换知识输入，不能因差值归因某单组件。没有组件级因果消融或新的commit/control合同，以已有章节相同机制而非“客服领域”关闭前分母，保留具体来源理由供独立抽检。

## 第二批证据与真实 Books 位置（尚未日级验收）

- `2604.08556v1`：§5–9。130M/FineWeb8B/bf16/H200及短结构任务，只支持在受测表示容量与预算下结构、内容检索的不同压力；小型attention消融不是130M主实验的同规模归因。DPI需要实际信息丢失，不能推出任何固定递推都无法记忆。Ch22正文95–111固定容量/recall、215–258 GDN输入依赖状态和hybrid边界已经承载该具体判断。拟1+2+2=5标准完成、已有覆盖，待非作者单篇采用复核。
- `2604.08557v1`：§3、§4.1–4.3、§6/Limitations，white-box修改denoising state；remask或prefix单独为0，组合才有效。原v1只有两模型，不能沿用旧库存后版三模型/Defense Inversion。Ch24 Editable tokens与commit boundary已实际插入“模型accepted vs外部篡改provenance”及isolated remask audit分支，保留两7B/8B模型、greedy线性schedule、单judge、非黑盒与未验证防线边界。拟2+2+2=6安全深入完成，写后非作者采用尚待root。
- `2604.08706v1`：§3–5.5及假设4.1–4.3，FIFO replay把N/R horizon、B/R reuse与W/T生成成本分开；样本与历史iterate依赖导致条件bias，importance correction不消除所有偏差。Qwen0.6B/7B OpenR1/MATH至少4seeds、matched LR，active GPU compute不是wall-clock；过高reuse与late overfitting是反例。Ch33 Replay小节已实际补这条条件分支，拟2+2+2=6机制缺口深入完成，写后root采用待核。
- `2604.08720v1`：§2、§4.4–4.5、§5.1–5.6/§6。116收集问题中77可重放，26被5个fuzzer找到，15graph问题全部漏检；四种graph需要跨调用oracle，非计算API及上下文变更另分。Ch49现staged differential未承载同编译artifact跨输入/context执行，已补alias/view/in-place/layout与多次oracle小节；LLM只生成mutation，不拥有correctness判定。拟2+2+2=6机制缺口深入完成，写后root待核，未将历史样本比例当生产故障率。
- `2604.08826v1`：§3–6，HiFloat4 tensor-role分工、32 metadata/64FP4、dW SR/RHT但NR forward不同，same-rotation在full precision等价不证明quantized等价；3架构50B tokens/25B ablation，loss gap不证明downstream quality。原文all-linear FP4与§5.1高精度保护、8/120与6.25%有内部口径问题，不采用全路径算力/功率断言。Ch28 mixed precision正文586–624、662–716已明确format×tensor role、SR非通用、RHT成本与高精度fallback。拟1+2+2=5标准完成、已有覆盖，待非作者单篇核。
- `2604.08584/08585v1`：Ch45已实际写入Query-side离线索引、context-aware selective recomputation两分支。root已独立重开必要v1方法/反例并对读正文，采用通过；此前“等待锁”仅为小批次旧状态，不再是普通Books待办。日级仍未冻结。

## 第三批贡献消歧（不以已有owner直接拒绝新证据）

- `2604.08601v1`：必要消歧读§5–9，intent/policy/scoped-TTL STS/event log与authority/trust/recency组成一条治理管线。§5把execution-event、conflict safety和fairness作为前提/不变量，再称端到端定理，未给外部effect与日志的原子性证明；§8两个模拟场景和10k人工proposal，没有LLM在环/受控failure或相对治理基线的机制增量。Ch78 effect-time/版本前置与未知outcome、Ch84 primitive authority实际正文已承载这些分权原则。拟按成熟组合的场景实现关闭前分母，保留作者可行性主张，不称其所有治理无价值；待独立准入校准。
- `2604.08595v1`：§3与§4.3/4.4/4.6、§5.3，五级verdict+generalized power mean/None penalty是可重聚合的标量分支。Table9 powermean相对算术ρ仅+.004/+.008，USR二值反而+.030；单GPT4.1-mini、temperature需calibration、最大8claim decomposition均限制比较。未提供claim probability、总体置信或release gate保证。拟按已有加权评价原则的局部operating point关闭前分母，不把correlation提高当真实正确性证明；待独立校准。
- `2604.08608v1`：完整题摘及Formal Model、Measurement Pipeline、Table5–7、Limitations已核。单次常规凭据请求由prompted orchestrator生成越权plan，42subtasks对旧LG7b/Koala过关；新LG3 posthoc可flag8/87，Table7 pure-SIF为0/14，LLM单步也见routing风险。故真实窄反证是局部goal alignment与composition policy不同，不支持“任何单步防线都不可能”。CIV同时参与10/14成功定义和防线评价，10/10存在同estimand循环；8benign还排除2个plan-generation失败，不称生产0FPR。拟2+2+2=6、安全深入完成，Ch72跨会话intent-neighborhood不完全覆盖单请求scope×destination，已发root具体最小差异等待owner判断。
- `2604.09107v1`：§3、§4.3–4.6、§5.1–5.4已按必要位置读（完整大块中间截断的评价末段仍需定点补读）。ROS引用已有GPU副本，unpublish撤引用并drain、retain保最后copy CPU offload；model-parallel group同一事务view、partial prefix复制与cross-DC seed。最后non-spot副本失败可返回unavailable，server fail重建soft references而非持久checkpoint。Ch36现885版本tensor/UniRL及946 delta/lease不含该reference-only存储分支，已请求写锁。拟3+3+2=8深入，采用前补齐必要评价末段、日期和写后独立复核。

## 第四批必要证据与实际写回

- `2604.09406v1` OASIS：§3/Alg1/3.2 online Oja basis、forward exact / backward activation projection，full weights更新并非LoRA；新旧basis重叠运输moment，而二阶逐坐标近似不保存full covariance。Tables1–3、§4.3/5低rank质量与basis步长、drift取舍明确；Llama3.2-1B rank32 GSM8K23.78<Adam27.09，130M C4loss3.28>3.21，不采用全质量等价。Ch39低bitstate后实际加入‘低秩状态还需要保存坐标身份’，root必要原文与实际正文独立PASS。2+2+2=6，gap深入完成；未复现实验。
- `2604.09083v1` EdgeFlow：§4.1channel greedy局部误差proxy、§4.2bit-interleaved weightlets→SIMD unpack INT8、§4.3CPU/NPU topology/chunk优先及steal阈值，改变端侧coldstartcriticalpath而非只有压缩率。§5.1–5.5全部Xiaomi15Pro/Snapdragon8Elite16GB/512GB，Llama/Mistral/Phi/Qwen，平均4–7bit vsINT8，默认5bit有质量代价，CPUdecode512/512不随TTFT普遍加速；QNN逆向格式新增兼容风险。Ch49图优化主干后实际吸收，root必要原文/正文独立PASS。2+2+2=6，gap深入完成。
- `2604.08995v1` MatrixGame3.0：§3.1–3.5 joint recent history/retrieved memory/currentnoisy latent，分开error-buffer corruption；600steps clean单段→2400steps multi-segment student ownrollout、memorypool更新后相机查询，最后段DMD。§5.1–5.2以viewrevisit定性展示为主，不证明每个组件质量因果、physically executable状态或硬件普适FPS。Ch25‘取回memory不证明使用’前实际吸收训练/部署上下文一致性分支，root必要原文/正文独立PASS。2+2+2=6，gap深入完成。
- `2604.09048v1` WattCounts：§3.2/5.1–5.3分别finite1000SQuAD workload和5minPoisson server，前者不含测量窗前后idle，后者含；50模型≤30B/10NVIDIAGPU/372configs、5runs、NVML10Hz仅board，单4090RAPL子集不证明host全覆盖。maxctx1024/maxgen256/temp0，无accuracy评价，不能当cost_per_good；hardware/modelranking变化是真受测反证。Ch70‘Utilization应由实际负载推出’/‘只量GPU漏整机’/usefulgoal分母已具体承载，拟1+2+2=5标准完成/Existing，待root非作者采用。

root单篇非作者采用已PASS08556/08826/08885/08865，分别对读Ch22固定容量/内容选择，Ch28tensorrole/format/保护回退，Ch66marginal/classwise校准，Ch32promptbaseline广播；不是新写入。08556官方history显示Mar17submitted、AprilID，仅证明投稿早于公告月，并非日期反证；最终owner仍用batch+slot+earlymetadata联合推定，不将提交改称公开时间。

## 后续具体贡献裁决与必要补读

- `2604.08630v1` Realisation-Level Privacy Filtering：完整题摘研究自适应数据库隐私release的逐实现privacyfilter与stopping规则；未把该定理接到当前模型训练、serving或Agent必要交互机制，只能作泛安全类比。按当前项目范围前分母关闭，不说隐私理论无价值。
- `2604.08756v1` Artifacts as Memory：完整题摘及intro提出agent/environment之外artifact信息通道，以classicalQlearning/RNN maze task说明；未研究foundation-model上下文、记忆检索或当前artifact authority新边界。当前主线范围前分母关闭，不声称全文定理已审完。
- `2604.09124v1` MATCHA：完整题摘/必要workload消歧为ONNXconvolution+constraintprogramming、SoCL3/L2与两个accelerator、MLPerfTiny；不是当前大模型算子/并行runtime的新design判断。具体范围关闭而非因为compiler标签拒绝。
- `2604.09459v1`：已重开officialv1完整题摘，47methods/41core+6adjacent taxonomy、证据分类与decisiontree；没有新controlled反证/解决具体creditassignment分歧，前分母关闭。旧库存v2的69methods/July31不可回填。
- `2604.08749v1`：已读§3artifactidentity/§5.1–5.3static-vs-resampled/§5.6/§6/§8必要证据；随机冻结scaffold是与预训练LoRA不同的条件训练分支，但WikiText103同架构samplebudget全scale差于fulltraining，H20032batch/128tokens Table9吞吐不快。5分→Ch30真正缺口深入拟稿，不采用96–100%跨任务摘要泛化、nominalrank=intrinsicdimension或ASIC速度猜测。
- `2604.08926v1`：§3.1–3.3动态分Hard/Mid/Easy，Hard随机multi-teacher target SFT、MidGRPO+onpolicy pairGAL、Easyskip；‘严格降variance’依赖两梯度噪声independent与teacherbias假设，不证明共用rollouts的variance必降。§4.1–4.5两个Qwen/16A800/bf16/G8/max8192，Table3分项control但AMC dynamicgrading可退步；§7onlinecost。6分→Ch33真实路由分支gap深入拟稿。
- `2604.08964v1`：§3.3Eq4–7currentdistribution作anchor、历史加权KL与decay阈值、futureblock提前unlock，不是单步confidence；§4threshold大可过早/小延迟、history2差6合适只对受测LLaDA/MMaDA。6分gap深入，Ch24拟窄增量；必要setup/理论假设补读后闭合。
- `2604.09073v1`：§3memoryerrorfree/bitflip模型、§4fixedinitialnoiseLPIPS、§5ABFTchecksummask大误差用earlieractivation近似覆盖、10stepoffload/layoutrepack，不能称exactrollback或pairedcancel不可能。§6hardware14nmsynthesis/SCALE-Sim、INT8/INT32与四diffusionconfig，energy/speed两DVFS点不合并承诺。6分gap深入，Ch49拟最窄近似恢复分支。

## 第五批审阅终态与写回（等待日级独立 Gate）

此前小批次中的“拟稿/待root”不再表示普通未执行工作：08749/08926/08964/09073四处已实际写入Ch30/33/24/49并由root独立对读必要v1方法、反例及正文通过；08723已实际写入Ch34 preference signal分解并通过root采用。09019已写Ch76，作者发现将§6.5 P-weighted消融混作主配置，现已重开§5.1–6.6/Alg1，改成二元Q/Union后冻结α=.25，Table2主配置MuSiQue+5.3pp/Hotpot+1.1pp不显著；P-weighted才为+2.6pp不显著/−.2pp。修正后root已独立核§5.3/Alg1/Table2/§6.5及实际正文通过，取代先前错误连续路由描述的采用结论；不称版本漂移。

- `2604.08974v1`，1+2+2=5标准完成：§3–6，BART/FlanT5/Llama3.1-8B/Gemma2-2B×translation/SQuAD/GSM8K×12metrics，144config/3seeds。SFT后48/144下降中仅2项显著、96/144上升中8项显著（Holm/ANOVA），不是普遍恶化；817TruthfulQA/Claude3.5Sonnet judge、23/48AUROC下降另列。作者testset minmax缩放不等概率校准，采用验证集属于平台规则。Ch66 calibration跟随model/task/metric version与独立quality sensor的真实正文承载，拟已有覆盖，未复现实验。
- `2604.08976v1`，1+2+2=5标准完成：§3–6 Tables3–7，Llama3-8B-Instruct、3000TriviaQA/4domains，Q5_K_M vsf16、7900GRE/Vulkan/llama.cpp。AUROC2与meta-d′/d′排序不同只在四域；LoRA因Q5merge不可用使用f16训练/评价，不当量化后直接恢复。seed42、10kbootstrap与宽CI不证明等价，低d′使M-ratio不稳定。Ch66 artifact/metric identity和切片校准已承载此受限边界，拟已有覆盖；不宣布某指标对量化普遍不变。
- `2604.09174v1`，1+2+2=5标准完成：§3–6，Hotpot3000/medical1500、24039/11007facets，goldsupport仅Hotpot，BGEbase/300chunk/50overlap/K5、RoBERTaMNLI entail−contradict不是校准概率。StrictEvidence/SoftRAG/LLMonly和resynthesis使用同facet而每case单run；strict失败与soft约30%退化不等内部先验因果定位。Ch76 301–337relevance/sufficiency/faithfulness及counterfactual evidence段已具体承载，拟已有覆盖。
- `2604.08588v1`，1+2+2=5标准完成：§2–6成本阈值基于外部tree的条件成功信号，8models/250samples（thinking50）及人类记录决定任务；不是让模型获得真值自知。Table1Qwen成本措辞增益小而GPT5mini有增益，不能照录cost无效；Qwen9B SFT模板外部p，heldoutMovieLens特定boundary全对，NoSignal幻造p不能作开放能力保证。Ch66外部校准与Ch56风险×成本policy已有具体正文，canonical Ch66拟已有覆盖。
- `2604.09443v1`，1+2+2=5标准完成：§4–6，853=427code+426IF、46agent contexts、10models/40k/temp0，多层增加同时改变冲突数量，无法只归因层数。ordinal/scalar表示与保序数值扰动也改变服从说明prompt labels不等authority。Ch72 InstructionHierarchy authenticated provenance/policyengine段已承载，拟已有覆盖；不把有限bootstrap当全模型保障。
- `2604.09285v1`，1+2+2=5标准完成：§3–4，SOP graph state→path→action与chat三judge分开，path是setoverlap非完整顺序合法性，judge labels输入rule仍非deterministic truth。27models/6scenarios、turn1/5/10/15/final，不称所有turn覆盖；不同Qwenjudges严格度构成反证。Ch66 process/outcome与judgecompetence/bias具体正文已承载，拟已有覆盖。
- `2604.09048v1`：root已经独立核§3.2/5.3并对读Ch70 121–145，finite1000query与5minPoissonλ口径、NVMLboard边界与idle改变排序；已有覆盖通过，不采用TDP代实际能耗。
- `2604.09175v1`，2+1+2=5标准完成/仅报告：§3Theorems3.2/3.4/3.7、§5–6，boundedhardTopK/Cβ/compactC1manifold/iid squaredloss下worstcase路由组合容量项；不是任意LM loss或learnedrouter优化的通用scaling recipe。TinyStories/WikiText/OpenWeb少预算拟合、估计intrinsicdimension和β与moderateM/k实验非单调，保留理论对象/假设差异，不据此修改Ch21工程路由结论。
- `2604.08988v1`，2+1+2=5标准完成/仅报告：§4–5顺序episode的memory/token成本证据有贡献，但§4.3.2总120与§4.3.3总90任务矛盾；实际12atomicgroups、两ClaudeOpus4.6harness，缺memoryreset/order/repeat干预，低token不能归因自动进化。OC后阶段token不单调；Ch77 acquisition/retention/forgetting/transfer主线不被替换，不把后版Flywheel题名回填v1。
- `2604.08905v1`，2+1+2=5标准完成/仅报告：§4.1–4.3、§5setup/相关/组件消融，adjacentembedding方向ACF与netdisplacement/pathlength PE加入outcome reward；两代理不是token真值因果信用，若干MW p=.1363/.2158不显著。正文3σ与15.87%尾概率口径矛盾不采用；受测Qwen/Math/Game24与GPT4omini标签的几何operating point不能成通用faithfulness选择。
- `2604.09000v1`，2+1+2=5标准完成/仅报告：§4–5，isolatedtext sphericalclustering/diversity与entity-connected degree/redundancy分别压缩，temporalretrieval含recency权重/segment预算；不是同一节点均匀topK。Table2固定M3Agent其余组件、30%压缩robot30.7>30.3/web47.0<47.9，70%+TMR不可归因compression单独。2A10080G/3次均值、GPT4o judge与固定memorygraphs，更多retrievalcalls可抵消压缩收益；仅保留受限压缩/读路径实验，不承诺开放长期memory保持或整体服务SLO。
- `2604.08644v1`，2+1+2=5标准完成/仅报告：§2–5公开1.2Bvisionencoder+32BLLM，visionGQA即无KV也选择减attention复杂度，resolution/tokenbudget、2D/1DRoPE、MTP与contextparallel构成明确受限架构分支，不因缺消融直接拒绝。§3vision温度1.0/文档.6、top-p.95/presence1.5、32k/128k输出且MTP关闭；对照混合官方报告与内测，不能将排行榜归因visionGQA/MTP或称生产吞吐。只记录版本/作者配置事实，Ch23/49稳定机制不因此改变，hardware/precision/batch/concurrency/SLO未在此采用证据披露。
- `2604.08906v1`，2+2+2=6标准完成/仅报告：exact-v1题名Dissecting Bug Triggers and Failure Modes，§3/8/9/11：截至2025-08-11取820→501→409fixedbugs；只有273有repro/config可分析，modelBackend×ID、ConsecutiveExec和ExportComponent提供具体interaction failure。35选择sourcebugs中16transfer，11reports仅1fixed/6communityack/4designboundary；47%是bugfix附test inclusion非测试覆盖率/生产失败率。Ch81 847–859确定性transition与agent scenario分测及verifiedstate版本绑定已承载大方向；不把historical样本当全框架通用oracle，保留受限触发模板证据。
- `2604.09155v1`，2+2+2=6安全深入/争议暂缓：§3.4Eq3–5控制joint risk，未给conditional executed-risk相同界；AppD Eq10 HR=Σeh/T所有proposal、Eq11mHR=Σeh/Σe执行条件率、Eq12GAR=executioncoverage非task-goal成功。coverage<1时joint≤α不足以推出“自主执行最多1% harmful”，需除coverage。root必要原文独立核同意隔离此采用保证，不否定jointCRC本身。恢复需作者补条件分母证明/明确收窄宣称；不写Books安全保证。

## 第六批否定侧恢复：五个具体机制缺口

原账本将08564/08690/08801/08844/08880泛化为benchmark/local或不改变evaluator而关闭，实际必要v1内容不支持该理由。五项early-v1Updated分别00:00:28/00:04:29/00:12:09/00:15:23/00:18:50Z，与官方slot/连续批次联合支持本窗推断，不将字段单独当首发。题摘与必要机制/反例已读，实际书稿分别Ch24/33/74/66/29窄改动，均待root非作者写后复核；35有效家族不重审，工作池暂40而非冻结分母。

### [Attention-Based Sampler for Diffusion Language Models — 2604.08564v1](https://arxiv.org/html/2604.08564v1)

§3.1–3.2/Alg1–2、§4与Table1/§5.1–5.5：单层Softmax、块内固定attention及平均代表性假设下，column-sum降序优化的是近似目标，不是任意多层全序列likelihood。动态阈值来自低置信组最大影响，sub-block提取绕开融合kernel不materialize attention的问题；理论FLOPs÷A100峰值不是实测开销。Fast-dLLMv2-1.5B/7B与LLaDA1.5-8B、单A6000、GSM8K/MATH/HumanEval/MBPP；1.5B Parallel MATH31.02<Confidence32.24，7B Parallel MATH51.88<Entropy51.92，不能称每项最优。采用证据中precision、输入输出长度、batch、并发/SLO未披露。Ch24 masked generation原confidence schedule与00375探索熵分支后已实际补影响排序/成本条件，root已完成必要原文与实际正文/相邻链路的独立采用复核；未复现实验。

### [Skip-Connected Policy Optimization for Implicit Advantage — 2604.08690v1](https://arxiv.org/html/2604.08690v1)

§3.1–3.2/Eq1–6、Table2/§4.1–4.3、AppendixC/D：上游早停段与原题重排[s,q]后，G个下游结果均值作prefix reward；单上游使用KL衰减历史SPO baseline，下游GRPO不能反向借作其空间baseline。vLLM同batch暂停，median mean-NLL选段、KV指针重定向并重算重排prefix；不保证无discard工作。Qwen2.5-Math7B/Llama3.2-3B、dapo-math-17k、500steps、128prompt/G8、bf16、1024/3072长度；训练GPU型号/生产SLO未披露。Table2组件移除均低于原方法，但GPT5-nano只分析correct轨迹且instruction continuation不是真rawprefix或learner因果信用。Ch33 token-credit原段后已实际补此分支，root已完成必要原文与实际正文/相邻链路的独立采用复核。

### [p1: Better Prompt Optimization with Fewer Prompts — 2604.08801v1](https://arxiv.org/html/2604.08801v1)

§3.2–3.3/Eq4–5、§4–5、§7：二元reward/iid response的总variance拆为response sampling与真实prompt差异，selector扣噪声而不用不稳SNR；每轮KNM成本及子集穷举不能遗漏。Qwen3-4B prompt generator、4B/1.7B frozen response、4H100三日预算、K×M约固定，数学Ktop1过拟合、IFBench全量仍更好；跨Qwen家族迁移未证明开放任务普适。precision/生产并发SLO未披露。Ch74生命周期中实际插入‘自动Prompt优化还要区分设计信号与采样噪声’，不把teacher训练或Prompt增加authority混写，root已完成必要原文与实际正文/相邻链路的独立采用复核。

### [Spectral Geometry of LoRA Adapters Encodes Training Objective and Predicts Harmful Compliance — 2604.08844v1](https://arxiv.org/html/2604.08844v1)

§3.1–3.6、§5.2–5.8/§7：Llama3.2-3B r8、q/v_proj、38adapter含4legacy，70/30小split。DPO训练sensor在steering上AUC0而非普适指纹；steering使生成collapse，Guard判unsafe而GPT4o对300条判0harmful，不能把artifact当真实攻击成功。ρ.72只来自24非steered且主要healthy/drift分群，PCA14/18文字冲突不采用定量全域分离。hardware/完整precision长度并发SLO未披露。Ch66 subject identity后、harness小节前已补跨method holdout与行为测量分支，安全反证及真实gap深入，root已完成必要原文与实际正文/相邻链路的独立采用复核。

### [Revisiting the Capacity Gap in Chain-of-Thought Distillation from a Practical Perspective — 2604.08880v1](https://arxiv.org/html/2604.08880v1)

§3.1–3.3、§4.1–4.3、AppendixA/B/C：Qwen2.5各尺寸与QwQ32B、MATH/15预选BBH、4A10080GB、单run。同题共同正确交集合法隔离rationale；单teacher全部正确集考察部署效用，却一起改变数量/难度/质量，不证明capacitygap不存在。原mix有效batch20而standard2造成10倍update差，对齐后原优势不稳定；BBH3:2split与>30pp ICLgap预选限定外推，1.3比例不成普适阈值。Ch29多teacher debate前已补基线与两种estimand；precision/线上并发SLO未披露，root已完成必要原文与实际正文/相邻链路的独立采用复核。

## 有限定点准入队列（30项，不是新增候选或全文队列）

root确认仅复查旧共同泛化关闭理由实际影响的以下身份；完整题摘为准，含糊时补最小方法/反证消歧，不因方法新名自动retain，不等待其他lane。`2604.`统一前缀：08920、09024、09029、09035、09054、09057、09059、09075、09088、09089、09101、09104、09121、09150、09159、09167、09168、09173、09181、09189、09222、09227、09244、09330、09332、09338、09364、09425、09429、09455。本节随后记录逐项终态；此时未完成准入，不能把30计入候选分母。

### 队列首批明确前分母关闭（完整 exact-v1 题摘；必要消歧不等同全文审阅）

| 身份 | 裁决与具体依据 |
| --- | --- |
| [2604.08920v1](https://arxiv.org/html/2604.08920v1) | 前分母关闭：该三小时 tutorial 将 relevance/utility、LLM-agnostic/specific 和 context-dependent 检索组织为综述；题摘未提供改变检索收益归因或评估有效性的新证据。不是因为 RAG 已有 owner 而排除，也不把综述框架名当新执行机制。 |
| [2604.09054v1](https://arxiv.org/html/2604.09054v1) | 前分母关闭：exact-v1 为 AccompGen 而非库存后发 HAFM；50Hz HuBERT→75Hz EnCodec、semantic/coarse/fine 三段 AR、CFG/QK-normalization 是面向伴奏的已知层级 codec/生成组合。本项主要增量是伴奏任务的工作点，题摘没有改变跨速率接口有效性或生成范式选择的独立证据；不沿缓存后发 FAD1.71。 |
| [2604.09059v1](https://arxiv.org/html/2604.09059v1) | 前分母关闭：完整题摘及§3.2表明 trajectory→imagined next-frame→reflect/revise trajectory，加 nuScenes-GR-20K 与 pretrain/SFT/RL；这是已知 action-conditioned imagination/reflection 的驾驶组合。未据此建立生成图像独立于预测轨迹的安全 witness 或新的闭环有效性条件，故不把该组合的规划指标提升当系统分支；驾驶/VLA本身并非范围外。 |
| [2604.09121v1](https://arxiv.org/html/2604.09121v1) | 前分母关闭：semantic-coherence judge 与人类互动修订用于 ASR，题摘没有独立的 judge-validity、回合反馈归因或控制权变化证据；不是仅因语音应用排除，而是 WER之外语义指标+human loop 的既有组合尚无具体长期增量。 |
| [2604.09167v1](https://arxiv.org/html/2604.09167v1) | 前分母关闭：MAG3D 在3D资产生成中分 planning/grounding/coding roles，再执行验证；题摘没有新增跨角色状态提交、验证独立性或协调失效边界，仅已知角色分工/执行反馈的应用组合。 |
| [2604.09088v1](https://arxiv.org/html/2604.09088v1) | 前分母关闭：必要§3.1–3.3显示 frozen backbone→side feature KD、side logits→backbone新 linear head KD，推理丢弃side network。并非把学习改动写回冻结 backbone；不同深度的 masked feature/logit蒸馏组合改善受测任务工作点，但未改变训练期辅助支路、部署期head及原base的职责或提出不同于既有train-only KD的适用边界。encoder/小模型不是排除依据。 |

以上六项保留原身份和具体拒绝证据，不评分、不进入候选分母；日期未独立核定不能冒充当窗事件核验。

| 身份 | 第二批前分母关闭的具体依据 |
| --- | --- |
| [2604.09024v1](https://arxiv.org/html/2604.09024v1) | 完整题摘及§3–4：白盒视觉扰动在shadow questions上训练通用拒绝，把已知visual prompt injection用于保护图片。威胁方仍可下载图像且不受授权协议控制；题摘中的六模型/四数据集及三种清洗代价验证这个保护工作点，没有新的隐私认证、攻击跨输入边界或改变既有防御原则的归因。不是把隐私研究排除范围外，也不将拒绝文本等于私有信息不可取得。 |
| [2604.09029v1](https://arxiv.org/html/2604.09029v1) | 完整题摘、§3及§4.1–4.2：251合成金融allocation案例，用Knapsack可行集合定义utility上下界，DSR为全部约束的交集、CSR为均值。指标说明有效性和效用要分开，但这是既有joint constraint与outcome评估的具体基准；未提供新的failure owner、独立约束机制或改变系统选择的干预证据。不是因为金融任务一律无贡献，也不凭“oracle”一词自动入选。 |
| [2604.09104v1](https://arxiv.org/html/2604.09104v1) | 完整题摘及§3.1/3.5–3.7：收集X上共享链接/截图、可信度分类及去重，提供真实事件线索和新hypothesis；52人工评分样本检查rubric一致性，不是完整执行trace的真实性保证或全体部署failure prevalence。本文新增主要是OSINT事件数据/研究议程，没有改变模型机制、发布合同或安全控制的受控证据，故本项目前分母关闭；不把作者数据集判伪，也不采用4.9×为真实事故率。 |
| [2604.09150v1](https://arxiv.org/html/2604.09150v1) | 完整题摘及§3.1–3.5：local entropy→检索/CAD，超过2000token→self-summary，answer KL→stop，再用long/short accuracy×compression作DPO。组合了既有entropy proxy、contrastive decoding、摘要与偏好优化，尚未建立entropy等于证据可靠性或stop状态的不同有效性边界；本项目不因组合带来受测效率工作点新增路线。保留摘要PPO与实际§3避开PPO的版本措辞差异，不把其训练叙述照录。 |
| [2604.09189v1](https://arxiv.org/html/2604.09189v1) | 完整题摘及§3：提取自述规则再对行为作一致性比较，Conditional条件UNPREDICTABLE及Opaque行另有排除，benign compliance对Absolute标签也可算违反。本项重验“自述policy不等行为/权限”的成熟原则，既未取得latent policy也未形成可执行权限或新的监控有效性约束；不把47,496观测量作长期贡献，不否定这个诊断的研究价值。 |

这11项已各有具体关闭理由，剩余19项题摘显示可定位的新机制或controlled边界，进入必要证据判断；目前只是准入工作队列，尚未全部独立校准或完成Source Review，不将67工作总数标为冻结分母。19项为：09035（advantage-guided短horizon world sampling）、09057（AV共享运动状态）、09075（MaxSMT instruction subset/蒸馏与parser边界）、09089（跨层安全signal与secure-and-correct目标）、09101（prompt artifact后门检出边界）、09159（flow policy entropy/truncated graph）、09168（共享loop中间深度监督）、09173（vector/index分离的压缩/I/O/update）、09181（conditional源与Gaussian fallback）、09222（audio band utility/attack非单调）、09227（LR/HR commutator）、09244（三阶段modality/time salience）、09330（同步video/action flow）、09332（固定base的speech interface数据效率对照）、09338（step/backtrack协议反收益）、09364（full-sequence causal patch）、09425（visual stability与multi-token access不同）、09429（camera/video联合接口）、09455（expert-anchor分支及shared-prefix梯度）。不沿库存后发标题/摘要回填，09159 HTML/PDF页头日期不同已定点查原PDF，拟以exact-v1 PDF为准。

## 待办

## 有限19项必要证据审阅（作者工作结果，未冻结；不是仅摘要标签）

以下均先重开exact-v1题摘，随后围绕真实机制/关键反证读所列必要位置。19项的v1 Updated为本批00:29:30～00:59:35Z，配合官方公告slot、连续ID/OAI边界作08:00～09:00有界推断；不是把Updated改名首次公开。root尚需准入/采用独立判断。未写Books的只是普通可执行待办，不冒充外部受阻。

### [Advantage-Guided Diffusion for Model-Based Reinforcement Learning — 2604.09035v1](https://arxiv.org/html/2604.09035v1)

必要§V–VII：短horizon trajectory diffusion只用窗口reward时会遗漏窗口外价值；SAG用有界sigmoid advantage weight，EAG用指数倾斜，采样将guided dynamics与policy action交替，再以synthetic buffer训练actor/critic。理想真实advantage、均值零和单调权重条件下的改善不等学习后的每次policy单调，state-dependent normalizer也不能省略。四MuJoCo任务、1.5M真实env steps、MLP diffusion和PolyGRAD/OnlineDiffuser对照；Hopper低于PolyGRAD，SAG/EAG对value误差敏感度不同。硬件/precision/生产SLO本次采用证据Not Disclosed。拟2+1+2=5标准完成，仅报告：明确advantage-window理论分支，但学得value的误差与生成轨迹分布没有独立真实部署验证；不据此把Ch25模型想象当作长期return保证。

### [Tora3 — 2604.09057v1](https://arxiv.org/html/2604.09057v1)

必要Method（Motion-conditioned Noise Prior、motion-conditioned audio、Hybrid Flow Matching）、evaluation/ablation/Limitations：首帧latent按2D轨迹搬运，8维position/velocity/acceleration状态同时供video与audio；trajectory region使用搬运endpoint、其余区域Gaussian，soft mask与等区域权重避免面积稀释，小负初始audio gate减少扰动。Ovi720×720/5s、32A100、bf16、batch32/30ksteps，50代表视频评价；video-only运动指标与audio-only同步各有优势，联合并非每项胜出。track-derived metric/音频motion相关不证明质量材料接触或物理因果；无3D动力学/空间音源。拟2+2+2=6，真实shared-kinematics+endpoint gap须深入与Ch24对读后决定，不自动因有AV名称采用。

### [Neuro-Symbolic Hierarchical Alignment — 2604.09075v1](https://arxiv.org/html/2604.09075v1)

必要§3 pipeline/MaxSMT、training与实验strong-language/多轮：parser将instruction按来源atomize，NLI估计pair conflict，再由MaxSMT提最大一致子集供生成，并把符号偏好蒸馏进policy。parser/NLI不是认证authority，也可能漏上下文/传递冲突；Qwen3-4B在strong user language下神经符号推理仍失败，不能把solver可满足性当开放语言安全保证。拟1+2+2=5标准完成，拟已有覆盖Ch72 Policy-as-Data与deterministic authorization：当前正文已分开policy artifact、model sensor、enforcement owner，且版本/fallback明确。新受限solver反证保留，非因已有安全主题排除；作者具体MaxSMT运行方案不升级为可执行ACL。

### [DeepGuard — 2604.09089v1](https://arxiv.org/html/2604.09089v1)

必要method/implementation、§4 setup、§5 ablation：多个层的attention aggregation训练token safety analyzer，LoRA同时secure CE/margin/KL；decode bias为empirical secure-vulnerable vocab prior，经一次prompt forward的分数调节，之后不随每个token重新安全判定。QwenCoder3/7B、DeepSeekCoder1.3/6.7B、SeedCoder8B，joint secure-pass与conditional security不同；删Lsec后仍执行untrained analyzer steering会伤功能，不能只归因表示；无KL安全上升但功能下降。拟2+2+2=6安全深入工作完成，需具体Ch72内部sensor/生成偏置现段比较；尚未采用固定bias为calibrated probability或late-risk实时守卫，硬件/precision/服务SLO不补造。

### [CLIP-Inspector — 2604.09101v1](https://arxiv.org/html/2604.09101v1)

必要§3 threat/method、§4 setup、§5.3 adaptive/limitations：frozen CLIP也可由learnable prompt/meta-network带后门；white-box按候选class在1000无标签OOD图做trigger inversion，ASR/loss相对跨class outlier判断。ViT-B16/CoCoOp、最多50candidate classes且须含target、10datasets/4attacks；47/50受测模型检出但fine-grained三例失败，pool100明显弱，adaptive窄basin测试并不证明任意attacker。修复额外需labeled clean data，k2阈值不是risk校准。拟2+1+2=5安全深入完成，拟已有覆盖Ch72 Supply-chain的可组合Prompt artifact+Backdoor trigger-neighborhood：当前已要求prompt/adapters独立identity、组合/邻域安全测试；不采用作者‘none existing methods could detect’或clean-free部署保证。

### [Truncated Rectified Flow Policy — 2604.09159v1](https://arxiv.org/pdf/2604.09159v1)

exact-v1 PDF页头Apr13，HTML页头Aug24编译不作为当时正文，官方abs submittedApr10只作provenance。必要method/entropy derivation、training/inference：deterministic prefix加Gaussian stochastic tail，只在tail做RL梯度，prefix另由off-policy endpoint MSE自蒸馏。其augmented joint density surrogate省略deterministic prefix的volume correction；沿某条路径velocity对time恒定不推出对state空间divergence为零。不得采用真实terminal entropy或exact convergence保证。评价可省stochastic tail并由N候选Q选择，one-step不等完整决策只有一次计算。拟2+1+2=5标准审阅结果保留此近似设计，中心entropy采用保证争议须隔离；不新写Books精确entropy或全局最优承诺。

### [Efficient Looped Transformers — 2604.09168v1](https://arxiv.org/html/2604.09168v1)

必要§3 ILSD、§4.1–4.2/Figure8、limitations：Nunique layers共享执行Lloops，full Lmax teacher与随机中间Lint student是同一图严格prefix，target stop-grad而teacher/student都更新同θ；groundtruth权重λ由1降0。不是固定点求解，也不是没有额外head/loss的免费adaptive depth。ImageNet256与UCF16×128×128，MaskGIT/MAGVIT codebook1024、270epochs；DiT SD1.4VAE、batch512/500k、默认512DDPM/CFG3。N1×L32仍差(FID10.30)，远超Lmax退步，fixed参数量不是fixed compute。拟2+2+2=6 gap深入完成，Ch24 equilibrium后缺显式prefix-supervised循环分支，已提交root精确写位置；硬件/precision/生产SLO未披露则ND。

### [Decoupling Vector Data and Index Storage for Space Efficiency — 2604.09173v1](https://arxiv.org/html/2604.09173v1)

exact-v1不是库存后发COMPASS标题。必要§3.1–3.4/§4.1–4.2/§5.1–5.2.2：把邻接index与vectors物理分开，前者sort/Elias-Fano、后者XOR/base-byte+Huffman；遍历优先adjacency I/O，全精度vector由PQ候选heap稳定性批量prefetch/rerank，early-stop是近似搜索非exact。batch graph merge/repair与append vector、asyncGC/ID-location切换分开；metadata/cache/buffer不是零成本。双32core Xeon8336C/512GB/PM9A3NVMe、64threads、109M proprietary/100M–1.4B public、recall@10与QPS/P99配对；8bit datasets XORdelta不改善，高层headline不能通用，Ls50与billion低recall可比PipeANN慢，最高11.9%。拟2+2+2=6 gap深入完成，Ch76 filtered ANN→indexupdate之间缺layout分层，已提交root窄命题，未外推在线freshness/SLO。

### [MixFlow — 2604.09181v1](https://arxiv.org/html/2604.09181v1)

必要§3–4/Alg1–2、§5–6：κ-conditioned Gaussian μ/Σ source与standard Gaussian随机mix共同训练velocity，κ=x1可仅训练可见，部署missingκ直接标准Gaussian，不携带source predictor。不要把文本线性随机变量插值与Alg1 covariance interpolation作同一公式；Alg1 KL(qκ)与Eq5 KL(qκ,w)形式也不同，采用部署分支不宣称exact objective统一。CIFAR10/FFHQ/AFHQ64，κnoise/class/image消融，低β减少曲率但过低时高NFE退步，FFHQ4NFE也非全部更好；采样步数/FID不等wallclock/SLO。拟2+2+2=6 gap深入完成，Ch24 source identity之后拟补missing-condition fallback训练条件，已提交root，hardware/precision ND。

### [GRM — 2604.09222v1](https://arxiv.org/html/2604.09222v1)

必要§3.1–3.3/§4.1/§4.3–4.4：attack/ASR utility两种band梯度选择稀疏Mel区域，固定universal扰动配semantic regularization；防御含义是威胁预算不能仅以更多bands排序，full-band更伤utility却攻击反降。四7B/10B ALLM共享Whisper-large-v3，AdvBench520音频80/20、Libri500、AIR800、4090/bf16/100epochs/T3000，LlamaGuard3与DeepSeekV3两个judge；同48band随机与full-band控制支持局部分支，不证明人耳无感或真实安全风险校准。拟2+1+2=5安全深入完成；拟已有覆盖Ch72 Sensor Robustness不能删除Task-critical Semantics与matched benign/attack双分支：已有正文规定robustness/utility联合验收，保留新的非单调反证而非新增攻击操作教程。

### [Low-Resolution Preview for Flow-based Generation — 2604.09227v1](https://arxiv.org/html/2604.09227v1)

必要§3/§4与analysis、AppendixB：早期HR状态选binary block downsampler D，检查D与velocity的commutator，再用stored HR velocity的局部近似校正LR，减少重新做HR步骤。跨分辨率一致要求不是架构自带保证；α/步长/缓存velocity漂移增加费用，LRpreview不是SR后完整HR等价。Flux1-dev/SD3.5L、A100、PixArt30K随机5000prompt(2–1885chars)、同GPU latency与quality/similarity验收；5step cosine>.95只来自受测500轨迹/指定D，不能推任意solver时间。拟2+2+2=6 gap深入已读，需Ch24现分辨率/近似状态分支比较后裁决。

### [Tri-Stage Modality-aware Visual Pruning — 2604.09244v1](https://arxiv.org/html/2604.09244v1)

必要§3 algorithm/§4 analysis及§5基线：2D/3Dfeature norm比例gate，首step不剪，以窗口runningmean/EMA指导后续topK；object/robot由attention clustering定位，background仍随机留10%，两选择集合空交集fallback。改变的是跨modality/time/history的token selection，而norm/attention不是因果salience。naive固定剪枝有SR大幅损失，tested selected ratio不等安全动作保证；LLM节省也不等controller全周期节省。拟2+1+2=5标准审阅进行中，尚须必要实验设置/反例后对读Ch23固定budget/modality可靠性门槛，不能将组合新名直接拟整合。

### [Video-Action Generation — 2604.09330v1](https://arxiv.org/html/2604.09330v1)

必要§3/§4.1–4.5/Limitations：video/action同步flowtime但cleanvideo latent detach后只video→action，pool成global channel重复到actionsequence，不是双向因果闭环或逐token几何对齐。CosmosPredict2Video2World2B、480P10Hz93frames432×768/35NFE、8H20/40k/batch1每GPU；AgiBot1794/200、LIBERO400/50。Table2所谓SR是各action维error<.2，不等真实任务success；LIBERO replay另Table3，机器人π0.5 syntheticpretrain+FT20trials11/20vs7/20而训练预算不同。生成视频未受action影响是作者limitations。拟2+2+2=6必要深审结果已收窄，需Ch25/26现joint-world-action与imagined-vs-real主干逐命题比，不采用摘要'rigorousaligned'/普遍安全。

### [Projector-based versus Phoneme-based Speech–Language Interfaces — 2604.09332v1](https://arxiv.org/html/2604.09332v1)

必要§4.4–4.5/§5.1–5.3：连续projector两stage与离散phoneme/多样phoneme候选S-SKM(K8)比较；Tatar20h双方同一冻结Whistle-large且不target-language fine-tune，English encoder FT不同不能称全程matching。BPEphoneme113→125tokens反而更长，收益可能是显式wordboundary而非少token；词表1000可退步，phonemerecognition error仍进入LLM。Qwen3-1.7/8B，Libri960h；代表E5 8A800 projector5.135+4.107h与phoneme5.83h只是披露训练recipe/steps并非通用latency。拟2+1+2=5标准完成，需Ch23 continuous/discrete接口现正文具体裁决；不据Tatar一语言宣布所有low-resource均最佳。

### [Mind the Gap Between Spatial Reasoning and Acting! — 2604.09338v1](https://arxiv.org/pdf/2604.09338v1)

HTML不可得已用官方PDFv1§3/§4.1–4.2定点恢复，不把普通读取阻碍留pending。八模型500同测试puzzles；合法move接口消掉部分formatting，weak模型改善而strong模型stepwise下降，backtrack使completion提升但不等solve。completion不能作success，作者training-incentive/contamination因果解释未有对应干预。one-shot与逐回合增加context/调用也改变执行协议，非同计算实验。拟2+1+2=5标准必要部分已读，拟Ch79/66已有覆盖须核actualbody；不得采用16%为所有空间问题或protocol-free模型能力。

### [Arbitration Between Visual Evidence and Language Priors — 2604.09364v1](https://arxiv.org/html/2604.09364v1)

必要full-sequence patching/steering、analysis/Limitations：linearprobe可读视觉不等最终答案采用，fullsequence而lasttokenpatch几乎不改结论；9models×100反事实input的受限干预与三7–8B SAE residual delta steering，保留other residual但不证明独立语义truth。MAC首稳定logit crossover只是定位heuristic，所有位置patch不能把distributed表示简化成最后token。293heldoutcolors/200train、seed42、steering有退步，naturalimages未验；早probe AUC/跨model相关非唯一因果。拟2+2+2=6真实诊断gap需Ch23写入/读取/latecounterfactual实际主干比较；尚未采用fullsequence必然最佳。

### [Visual Representational Stabilization versus Functional Necessity — 2604.09425v1](https://arxiv.org/html/2604.09425v1)

必要§3–7：depth state几何稳定并不等后层可删除；crosslayer state替换不等删image tokens，截断必须同步mask/positions/KV。single-answer也有退步只是multi-token更敏感，caption/ChartQA不同metric与teacher-outputdistill恢复不能作人类准确率；CoT不能补消失visual access。六VLModel有限任务，A.4 LoRA/decodingvariation为恢复代价而非推理免费。拟2+1+2=5标准完成，Ch23现geometry/interface/grounding论点需具体比；硬件precision/服务SLO未用于采用即ND，不写“删视觉完全不影响短答案”。

### [Rays as Pixels — 2604.09429v1](https://arxiv.org/html/2604.09429v1)

必要§3.2–3.5/§4 architecture/cycle/ablation：origin+direction编码three-channel raxel，canonicalreferenceframe、同videoVAE，但coarsegrid和位置信息要对齐；self/cross分离处理video/camera 双向状态。decodedray用Procrustes恢复pose，median focal ratio假设principalpoint居中。chain-rule两factorizations不是该network学得joint的证明；Plücker六channel须MLP而raxels复用VAE，消融同时改变codec，不单纯证明representation数学更强。Wan2.1T2V14B+raybranch6B=20B，RealEstate10K/DL3DV metric-scale、480×832/12FPS测试；cycle有GTpose误差但generatedself-consistency不是外部真实3D。拟2+2+2=6必要gap证据已读，待Ch23/24/25选唯一representation owner；内参假设/新增参数训练成本需正文。

### [Expert-Guided Exploration for Tool-Integrated Reasoning — 2604.09455v1](https://arxiv.org/html/2604.09455v1)

必要§3/§5.1–5.3/Table3及组件ablation：selfrollouts完整保留，expert在highentropyanchor分叉，expert池仅maxreward超过self时加入；expert负branch停止共同prefix梯度，suffix仍有off-policyratio和mixtureprefixratio。不是学得真实knowledgeboundary，expert错误/分支selection bias与额外budget均可能变动。Qwen2.5 3/7B、Llama3.1-8B，两tool/web数学十任务；3runs组件对照同expertprefix/budget，但treeadv去除AMC23更好，baselineheadline不每任务优胜。拟2+2+2=6 gap必要审阅进行中，先补exactsetup/§5.3组件表后对读Ch33已有tree/sharedprefix/teacherbranch，不照录全部名称或knowledgeawareness。

14来源最终范围、批次日期推断及具体例外、剩余题摘贡献消歧/必要证据与Books决定、独立Gate。当前不宣称正式分母或整日报完成。

### 三项实际书稿与非作者复核终态

09168、09173、09181已分别实际写入Ch24 equilibrium后、Ch76 filtered ANN→indexupdate间、Ch24 source identity后。root重新打开必要exact-v1方法、反例并顺读实际正文/相邻论证，三项非作者写后复核通过；此前本节‘拟提交/待root’是早期过程状态，以此最终结果替换。采用范围仍受原实验/理论约束，未复现实验。Formal工作集现51、25实际Integrate；有限30队列另16必要处置未完，不称67冻结。

## 有限新增当前官方说明检查

对19个新增工作身份的官方abs页面轻量读取可见撤回/纠错说明，没有发现‘This paper has been withdrawn’/‘withdrawn by’公告；未把页面无标记当作完整版本史证明。8个可见Comments分别为09057 ACM MM accepted、09089 ACL main、09101 CVPR Findings/17pages、09168 ECCV、09222 MM、09425 TRUE-V workshop oral、09429 ICML/9pages+supplement、09455 ACL/22pages10figures；这些后续发表信息不改变本次exact-v1事件归属，也不启动全版本diff。其余可读官方页无相应可见notice。正式审阅仍按已绑定exact-v1方法/反证，不用后发摘要或accepted标签升级证据。

## 有限新增的必要补读与具体 owner 对照

- 09089：补读exact-v1 Table3/Table4。一次prompt score固定bias不能响应生成后才出现的风险；300token interval re-score越频繁成本越高，k64作者延迟+38.7%只绑定该配置，不能当服务SLO。HumanEval中guided bias损伤部分模型的正常功能，adapted weights可保留而关闭bias。Ch72 Learned Security Sensor正文已分一次入口检查、生成中持续风险窗口、固定频率检查与独立action enforcement，并要求副作用校准；拟安全深入完成/已有覆盖这条cadence与side-effect命题，不把固定bias当calibrated truth。必要原文已足，待非作者裁决。
- 09244：补读§5.3/Table3/§5.4与setup：A100PCIE40GB+Xeon6348、frozen MLA、四RLBench任务、多种剪枝率；unpruned48.8与50%pruned47.5不能说完全无损。组件表S1+S3 SR62.2低于baseline70，S2+S3 71.5；时间EMA reuse没有semantic task-critical保护会传播错误。Ch23固定预算/分阶段剪枝/时间区间合并已承载有损选择责任，但尚无这条时间reuse顺序的受控反证，拟标准5分完成；真实gap是否需极窄整合由非作者定点判断，不因三阶段组合名自动新写。Table3 stage标签与前文术语须以具体操作解释，不将全部加速混为end-to-end控制SLO。
- 09455：补读§5.1/AppC。所有实验8A100；SFT LlamaFactory+ZeRO3/FlashAttention2、bf16、batch128/3epochs/4096；RL warm-up n8+m8、k3、50steps，Post-RL n16/m0、250steps，batch128/minibatch16、response8192/observation512/max4tools。组件对照固定专家prefix/budget，Table4叙述降幅与具体行不完全一致，不采用口述20.6/14.7；tree-adv去除在AMC23 43.5>43.3，非全面收益。必要原文已足，gap深入拟Ch33 shared-prefix stop-gradient与self/expert预算分流；不继续无关附件。
- 09338：补读官方PDF AppendixA设置，4A10080、未量化baseline/Gym、500同测试puzzles与1000总集合。full current grid仍提供，stepwise较弱模型改善但强模型退步；legal-action接口/多回合context改变协议，不能把它纯归因隐藏记忆。Ch79现Tree of Thoughts与graph budget段已规定搜索深度/成本不单调、Ch66 protocol与真实outcome分开；拟标准5分已有覆盖该协议依赖命题，或仅报告有限特定反证，待非作者具体采用裁决。

## 第七批否定侧定点裁决（8项，非全库扩池）

### [Drift and selection in LLM text ecosystems — 2604.08554v1](https://arxiv.org/html/2604.08554v1)

§4.5 Theorem2、§5.2–5.5：有限字母表、variable-order n-gram与soft normative publication下，描述性固定点是n-shallow，外部规范要求超出n阶可产生非零project–lift KL/L1稳态。matched exact recursion仅5符号、n3/r5、同seed、80/20贡献、α1，区分‘收敛’与‘保留长程结构’；不是实际训练LLM。Ch27递归synthetic语料段已拆supplier/parameter/corpus与human-anchor约束，但本项对真实tokenizer、learned conditional与过滤器没有可验证的对应或通用阈值。保留这个理论对象的新边界，不据toy equilibrium配置修改生产recipe；hardware/precision/length/batch/concurrency/SLO为理论不适用，未运行script。

审阅：标准完成，评分2+1+2=5；仅报告：受限recursive n-gram理论不据此采用真实LLM语料稳定过滤规则。early-v1 Updated与本批slot/连续身份相容，仅支持有据区间推断，非该字段单独证明首发。

### [Multi-User Large Language Model Agents — 2604.08567v1](https://arxiv.org/html/2604.08567v1)

§4.1–4.2、§5.1–5.3：共享上下文同时观察多用户消息，Ci默认私有、persona/global constraint串在单user-role；Says/Colon/XML并非认证authority。题目把instruction selection F1与execution Acc、privacy与authorized utility、partial-disclosure协调分开。温度/top-p均1，受测模型在selection高时执行仍低，隐私高时效用可低，conflict/aligned条件和轮数另有对照；不外推真实ACL。Ch72‘Agent Privacy必须对整条Trajectory记账’与‘隐私检测是Policy-bound Sensor’已要求独立收件人/任务效用评测和sensor≠access-control，Instruction Hierarchy区分prompt标签与真实authority，实际承载这个判断。保留新多用户反证，而不是因已有主题拒绝；hardware、精度、输出长度/batch/并发/服务SLO未披露，不采用数字保证。

审阅：标准完成，评分1+2+2=5；已有覆盖 `PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)。early-v1 Updated与本批slot/连续身份相容，仅支持有据区间推断，非该字段单独证明首发。

### [Distributionally Robust Token Optimization in RLHF — 2604.08577v1](https://arxiv.org/html/2604.08577v1)

exact-v1 §3.1–3.2/Alg2–3/§4/AppendixA.1：RTO用DPO-derived token reward，DRO重加权minibatch的完整trajectory，不是每span新增reward。作者与apr03重新核HTML MathML和PDF-v1 Eq8均为Ψη+ρ/η，与Alg2及ν=1/η一致；旧纯文本提取丢失fraction导致ρη误读，撤销原公式争议，不等待不存在的勘误。χ² mean/std上界仅满足非负权重条件时tight，不直接成为任意deployment OOD保证。Llama3-8B/OpenMath10k/五数学bench只支持披露目标分支；保留这个受限轨迹鲁棒目标于报告，不把minibatch半径升级为Ch32开放分布不变性。hardware/precision/完整长度/batch/concurrency/SLO未披露不补造，未运行代码或复现实验；apr03必要原文独立裁决为5分标准、仅报告。

审阅：标准完成，评分2+1+2=5；仅报告：受限minibatch trajectory-DRO不等任意OOD保证，原KL公式争议已按官方原式撤销。early-v1 Updated与本批slot/连续身份相容，仅支持有据区间推断，非该字段单独证明首发。

### [On the Spectral Geometry of Cross-Modal Representations: A Functional Map Diagnostic for Multimodal Alignment — 2604.08579v1](https://arxiv.org/html/2604.08579v1)

§4.1、§4.4–4.6、§5：DINOv2-B14 768维/MiniLM-L6 384维，Flickr30k1000图各5caption均值，graph kNN15、basis50–100、单seed。谱距离相近但functional-map basis不对齐，低监督composition弱，受测retrieval低于Procrustes/relative；image-level caption-equivalence使i2tR1=R5，与标准CLIP协议不可直接拼榜。graph采样本身可能影响几何诊断，不能推出所有encoder缺共享语义。Ch23‘统一架构不等于双向可用的统一语义空间’及随后的几何噪声反证，已明确相关几何≠可操纵/可用语义，实际承载本项采用命题；保留受控新负结果，但不据此替换跨模态alignment机制。hardware/precision/batch/concurrency/SLO未披露。

审阅：标准完成，评分1+2+2=5；已有覆盖 `MULTIMODAL-REPRESENTATION` [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)。early-v1 Updated与本批slot/连续身份相容，仅支持有据区间推断，非该字段单独证明首发。

### [Adjoint Matching through the Lens of the Stochastic Maximum Principle in Optimal Control — 2604.08580v1](https://arxiv.org/html/2604.08580v1)

§3/Table1、§5 Theorem4/Remark5、§6：general drift/control-dependent diffusion的Hamiltonian BAM涉及一阶/二阶adjoint；仅σ(t)的专门条件可lean AM避免二阶quantity。Lemma9 verification/regularity承接critical point与optimal control，不等有限神经参数训练全局收敛；SMP BSDE的q未知，lean-adjoint给Hamiltonian方向的无偏估计，在此连续控制对象下解释MSA。trust-region稳定保证属于future work。exact-v1没有实际生成器数值性能对比，不能沿缓存后发‘已数值证明必要性’；理论不适用硬件/precision/length/batch/concurrency/SLO。本项解释的是指定连续控制对象下的噪声/adjoint依赖，尚无训练生成器的数值迁移证据；保留这个理论增量于报告，不把它改写为Ch24已验证的采样器或训练保证。root必要来源独立裁决为标准完成、仅报告。

审阅：标准完成，评分2+1+2=5；仅报告：σ条件下理论未验证训练生成器迁移或部署收益；root必要原文独立核通过。early-v1 Updated与本批slot/连续身份相容，仅支持有据区间推断，非该字段单独证明首发。

### [Unified Multimodal Uncertain Inference — 2604.08701v1](https://arxiv.org/html/2604.08701v1)

§2–3.3、§4 Tables3–4：WikiVideo10主题的人类scalar premise/hypothesis判断分别标audio/video/AV；teacher5次推理均值不是独立真值，CLUE-D 100confidence bins、σ.05 Gaussian target、KL训练，输出期望替代直接生成标量。token-vs-distribution/pos:neg比例改变MSE，audio切片token分支可更好；1:1选ratio不能普适且改变training prior。modality-specific batch减少padding/gradient imbalance，不由总结果证明其全部因果作用。受测3B模型与human/MSE目标不证明世界事实概率或deployment risk校准；precision/hardware/完整长度/batch/concurrency/SLO本次必要位置未披露。分布化输出是拟合人类scalar target的可检验接口分支，但MSE不能证明事实正确性或风险校准；不据此改变Ch66的事实/部署calibration contract。root必要来源独立裁决为标准完成、仅报告。

审阅：标准完成，评分2+1+2=5；仅报告：人类scalar target拟合不形成事实正确性或risk calibration保证；root必要原文独立核通过。early-v1 Updated与本批slot/连续身份相容，仅支持有据区间推断，非该字段单独证明首发。

### [Every Response Counts: Quantifying Uncertainty of LLM-based Multi-Agent Systems through Tensor Decomposition — 2604.08708v1](https://arxiv.org/html/2604.08708v1)

§4.1–4.3、§5.1–5.7：10条独立run×不同agent/不同轨迹长度的embedding建ragged集合，PARAFAC2低秩重构残差量化整段结构变化而非只final-answer agreement。Qwen3-embedding-.6B/dim256，GPT4o/Qwen2.5-7B/Llama3.1-8B、Camel/AutoGen/AnyMac、MATH/MoreHopQA/MMLU/HumanEval，temperature.9、单A10080GB或API；GPT5给final correctness标签，AUROC/AUARC为ranking，不是频率校准。工具结果也字符串化，低残差可以共享同源错误；tensor轴不能仅凭名称取得topology/communication因果解释。新增多run成本、rank/embedding选择和judge版本影响测量，未给独立真实risk保证；Ch66已有trajectory evidence、correlated-error与calibrated sensor主干，本次只保留受限新proxy，不将它当稳定production Gate替换。precision/完整长度/batch/服务并发SLO未披露。

审阅：标准完成，评分2+1+2=5；仅报告：ragged重构代理尚不作为校准risk或通信因果归因。early-v1 Updated与本批slot/连续身份相容，仅支持有据区间推断，非该字段单独证明首发。

### [Revisiting Anisotropy in Language Transformers: The Geometry of Learning Dynamics — 2604.08764v1](https://arxiv.org/html/2604.08764v1)

§2–3、Table1、§5：10encoder/decoder模型210M–1.7B，同合并C4/Wiki/FineWeb/arxiv/Frenchwiki语料，以早30%activation拟一次固定PCA QT，再测早/晚gradient matrix在其与matched-rank normal方向的能量；20random normal null令p最小1/21。QT只是activation-derived tangent proxy，不是真实概念/流形；去QT改善IsoScore*与early gradient集中支持局部几何解释，却不证明isotropy改进必然提升语义或泛化。晚期一些切片退步、encoder更弱、proxy未跟随late变换均保留。论文明确没有新optimizer/architecture或干预训练结果，故保留形成机制与测量反证，不把相关性写成新训练recipe。hardware/precision/length/batch/concurrency/SLO未用于本次采用数字，未披露不补造。

必要理论反查§2.4 Eq9/10/11：tangent与normal两个梯度上界不能直接相除得到比率上界，尚缺tangent非退化下界。局部抛物线x=(u,u²)、对称小u、W=0平方损失y=−1时g=1，tangent期望E[u]=0而normal E[u²]>0；这是本次独立反例，不是作者实验。故不采用Prop2.3的普遍ratio或自强化因果保证；固定PCA proxy/匹配秩的有限测量不随之作废。局部实验仅报告，理论保证单独隔离于§5；重开须补适用的梯度下界或修正定理。apr03必要原文及具体反证独立核通过。

审阅：标准完成，评分2+1+2=5；仅报告：保留固定PCA局部测量，不采用缺少下界的梯度ratio保证或普遍泛化结论。early-v1 Updated与本批slot/连续身份相容，仅支持有据区间推断，非该字段单独证明首发。

仅这8项按具体方法/反证重开；08701/08580已由root核为5分标准Only，其余6项由apr03必要原文/实际owner独立核完成。08577 KL参数化争议已撤销：官方HTML/PDF-v1均ρ/η，原纯文本丢fraction误读不是论文冲突；仅报告受限trajectory DRO。08764有限PCA测量保留、缺tangent lowerbound的ratio保证隔离。504不是全文队列，未变化有效证据复用。

## 有限队列最终单篇状态（替换此前拟处置，不预称日级通过）

有限30项已完成作者题摘与必要证据处理：11项具体前分母关闭，19项保留。其中09168/09173/09181已由root完成必要源及实际Books写后PASS，另外16项如下；原先“拟/待root”只保留作为过程记录，以本节及正式日报最终处置为准。当前正式67=33整合/19已有覆盖/14仅报告/1CORA暂缓，37深入/29标准/1争议。原12个旧Existing/Only和日级Gate仍待root独立判断，不报整日报完成。

| 精确版本 | 三维评分 | 审阅 | 实际Books处置 | 独立范围 |
| --- | --- | --- | --- | --- |
| 2604.09035v1 | 2+1+2=5 | 标准完成 | 仅报告 | apr03必要源/owner独立通过 |
| 2604.09057v1 | 2+2+2=6 | 深入完成 | 整合 MULTIMODAL-GENERATIVE-PARADIGMS | apr03必要源/owner与实际写后独立通过 |
| 2604.09075v1 | 1+2+2=5 | 标准完成 | 已有覆盖 PLATFORM-SECURITY | apr03必要源/owner独立通过 |
| 2604.09089v1 | 2+2+2=6 | 深入完成 | 已有覆盖 PLATFORM-SECURITY | apr03必要源/owner独立通过 |
| 2604.09101v1 | 2+1+2=5 | 深入完成 | 已有覆盖 PLATFORM-SECURITY | apr03必要源/owner独立通过 |
| 2604.09159v1 | 2+1+2=5 | 标准完成 | 仅报告 | apr03必要源/owner独立通过 |
| 2604.09222v1 | 2+1+2=5 | 深入完成 | 已有覆盖 PLATFORM-SECURITY | apr03必要源/owner独立通过 |
| 2604.09227v1 | 2+2+2=6 | 深入完成 | 整合 MULTIMODAL-GENERATIVE-PARADIGMS | apr03必要源/owner与实际写后独立通过 |
| 2604.09244v1 | 2+1+2=5 | 深入完成 | 整合 MULTIMODAL-REPRESENTATION | apr03必要源/owner与实际写后独立通过 |
| 2604.09330v1 | 2+2+2=6 | 深入完成 | 已有覆盖 MULTIMODAL-WORLD-MODELS | apr03必要源/owner独立通过 |
| 2604.09332v1 | 2+1+2=5 | 深入完成 | 整合 MULTIMODAL-REPRESENTATION | apr03必要源/owner与实际写后独立通过 |
| 2604.09338v1 | 2+1+2=5 | 标准完成 | 已有覆盖 AGENT-PLANNING | apr03必要源/owner独立通过 |
| 2604.09364v1 | 2+2+2=6 | 深入完成 | 整合 MULTIMODAL-REPRESENTATION | apr03必要源/owner与实际写后独立通过 |
| 2604.09425v1 | 2+1+2=5 | 深入完成 | 整合 MULTIMODAL-REPRESENTATION | apr03必要源/owner与实际写后独立通过 |
| 2604.09429v1 | 2+2+2=6 | 深入完成 | 整合 MULTIMODAL-REPRESENTATION | apr03必要源/owner与实际写后独立通过 |
| 2604.09455v1 | 2+2+2=6 | 深入完成 | 整合 TRAIN-GRPO | apr03必要源/owner与实际写后独立通过 |

8项新实际增量位置：Ch23 encoder/projector后09332、时间区间合并后09244/09425、camera state接口09429、视觉仲裁probe后09364；Ch24跨尺度preview09227和guidance/prior后的AV状态09057；Ch33 expert/self shared-prefix信用09455。apr03必要源/实际正文/相邻衔接写后PASS，09425协议术语及09244 EMA先于候选且不调固定threshold已修正。没有复现实验或生产保证。

08577作者真实重取官方HTML MathML alttext Eq8 Psi_eta+rho/eta，与apr03官方PDF-v1一致；纯文本丢分式是读取错误，撤销旧D，5标准Only。08764作者重开§2.4 Eq9/10/11，两个upper bounds缺tangent lowerbound，局部抛物线反例及仅报告测量/隔离普遍比率均按独立结果同步；不否定固定PCA实验。09159受限设计Only、terminal entropy保证隔离，无需外部材料请求以完成普通审阅。独立详情见[V3_INDEPENDENT_INCREMENT_AUDIT](./V3_INDEPENDENT_INCREMENT_AUDIT.md)。

## 恢复 checkpoint：作者侧已收束，最终非作者 Gate 未确认

apr03 已再次实际核对有限任务的最终差异，22项来源/owner与8处真实Books增量写后均通过，审计文件尾有具名交接。当前仍为67=33整合/19已有覆盖/14仅报告/1CORA暂缓，37深入/29标准/1争议；正式报告保持进行中。再次运行本日 scoped validator 与 scoped diff check 通过，但不替代语义验收。

主任务此刻出现 transport/remote-compaction 网络中断，尚未收到原12项Existing/Only及日级Gate最终结论。恢复后只需完成这12项必要独立裁决及来源/日期/清单否定侧日级复核，再同步§1/§5/§6与完成状态；不重新扫描504、不重复已有效通过的33实际增量或有限22项。若复核发现具体矛盾，仅重开对应family。作者不因主任务离线自行把报告标Complete。

等待期间按主任务此前授权，Apr14 09791/09917/09890三项有限非作者校准已完成，独立结果存于[Apr14三项校准](../daily-20260414/V3_INDEPENDENT_THREE_CALIBRATION.md)；没有修改Apr14作者报告、其他日期、全局checkpoint或新增共享Books。

## root 恢复后的精确终态交接：SEA 原版受阻

root 已恢复，apr03已实际核原12项的11个必要源/owner及有界日级集合/日期。2604.08988v1当前官方HTML返回后版Flywheel而非原SEA-Eval，不用于exact-v1证据。作者先前实际PDF笔记仍保留，但未持久保存可供本次独立核对的完整PDF；apr03两官方入口下载缺EOF，作者45秒+一次240秒有界续传得6,102,037/10,828,779字节后仍截断，pdftotext无法解析。root已明确同意停止无限下载，按合同将这一篇受阻/暂缓，不支持正面结论或Books，不消除其身份/评分工作草稿。

当前正式67=33整合/19已有覆盖/13仅报告/1SEA原版受阻暂缓/1CORA争议暂缓，37深入/28标准/1受阻/1争议。恢复条件是可明确绑定SEA-Eval v1的完整官方PDF或作者稿必要§4–5；材料到达只重开此项及依赖判断，不做整个版本史或全日重扫。此前14Only/29标准的过程记录由此终态替换；未变化的33真实Books和其他有效复核继续有效。作者同步正式表/同URL§4/§5及计数，最终日级Gate仍交apr03，不自审Complete。
