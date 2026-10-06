# 2026-01-30 最后十项必要证据

精确v1作者实际必要审阅；root已实际核十项必要命题/反侧。peer7分实际Ch66对照后OnlyReport通过；20047中心Cor22/函数类缺口Disputed终态NoBooks，其余Only。以下保留首审潜在owner描述，不是当前普通待办；实际日级/最终处置在本日README。未执行代码或重现实验。

## [HE-SNR / 2601.20255](https://arxiv.org/html/2601.20255v1)

2+1+2=5。§3–5物理130–235：私有MoE-S linearRoPE与约十倍MoE-L YaRN，32K→128K各checkpoint；取SWE-benchVerified500成功轨迹（与SFT同合成分布）、只保Action，用regex/AST剔除标签/注释/格式。HE-SNR为targetprob/top10-renormalized entropy平均，仅target在top10且entropy超过(log3+log4)/2。PPL在MoE-L context extension200step恶化而SFT后Pass1改善，局部反侧说明top1 confidence与post-SFT任务表现不能混同。三次evaluation不等三次training。每checkpoint >10k SWE轨迹SFT3epochs；未披露准确参数/全部硬件、train预算与CI，500同目标benchmark成功轨迹指标选择并无独立heldout proxy验证。

lnk是均匀k分类最大熵成熟事实，entropy峰不证明潜在候选只有k项或‘self-awareness’，Hypothesis4.3不当定理；SFT后HE-SNR降低不能单独证明实际reasoning下降。仅报告：具体私有checkpoint选择中的指标反例有价值，但过滤与threshold依赖该成功轨迹分布，未授通用intelligence/压缩或可迁移早停准则。

## [Peer prediction / 2601.20299](https://arxiv.org/html/2601.20299v1)

2+2+3=7，安全/设计反侧深入。§3 131–216、C.1 795–819/C.2 819–846、D892–912/958–986：source提供答案后expert预测另一target的logprob增益，participant通过source角色支付；DPO取高/低score配对。honest等如实private signal，不必客观正确。Theorem1用共同prior及诚实reported probabilities的BNE，不证明任意实际LLM达到唯一truthful equilibrium；信息保留的可逆重标亦可能同信息。Theorem2新增不同prior条件需participants/experts iid来自同population、boundedPMI/跨prior概率比、large m/n，且只对Alg2先平均prob后log成立。主Alg1的for all t文字含self，证明/Alg2 excludes self，必要边界保留；主实验算法/理论接口不能无条件等同。未泛审其全部证明或实现。

§4 217–260：37,079问/85domains、50-50split，four Llama3.1-8B clones含prompt-induced liar，one Smol135M expert；先50k deceptive LoRA，再120k high-low pair LoRADPO恢复accuracy。rule labels仅用于评价。评价强弱用8/70/405B同family，大模型大小作为quality proxy非事实真值；抵抗deception用honesty-label logistic CE/R²，不是攻击成功率。D1 forcedtarget字符串logprob+3example ICL，SGLang32A10080、temp1/max512；author训练/CI/全请求费用未明。D3 fewshot judge用了GPT4o注释与不同输入协议，不能混为统一label-freefairness。限制明确不涵盖collusion；实验m1/four clones不验证large-iid理论假设，也不保证无共同错信。

暂拟仅报告/待owner：局部score接口与具体理论条件值得核；不把弱judge小参数优势或incentive theorem授客观truth保证。须实际比较Ch66弱judge/correlation正文后最终处置。

## [Hyperbolic hierarchical learning / 2601.20047](https://arxiv.org/html/2601.20047v1)

2+1+3=6，必要理论反侧定点。§2/3/5物理137–245/288–331，B.3 604–632：regular-growth树、branching固定、depthR增大，Euclidean k固定/半径B受限、predictor Lip≤poly(R)。几何pigeonhole只迫使存在远树叶近Euclidean pair；相应cut要拟合需指数Lip。hyperbolic curvature随logΔ/(λε)容纳树，canonical按depthuniform、parentprefix已知条件leafsampling/BSCρ噪声有限pathclass，depthwise estimator upper O(mR log(mR/δ)/((1−2ρ)²ε²))、oracle lower Ω(mR logm/βρ)。不是所有LLMembedding/classification皆双曲优越；upper/lower还含confidence/accuracy因子不同。

中心‘Euclidean exponential sample complexity’链有缺口：B.3 Cor22要求representation含δ-separated sizeM packing，Lemma5只给close pair上界，不能由近碰撞本身推出大packing；fatshattering全Lipschitz类lower又不能直接套固定path有限targetclass。保留作者几何witness与受约束协议，但不授同类minimax普遍指数分离；硬件/latency/bench不适用。暂缓中心样本复杂度命题、无Book，root待定点复核该缺口；不因疑问删准入或降分。

## [Multitask adaptation limits / 2601.20774](https://arxiv.org/html/2601.20774v1)

2+1+3=6。§2/3 61–117与§5 157–207：有限VC二元分类、所有task共享最佳classifier、Bernsteinβ/transfer exponents；adaptive只见source数据、不知哪源fair/noisy、没有targetdata。新构造fair与noisy都非常噪，去掉旧n<2/β−1限制，却仍要求N≥n^(nβ/(1−β))超级指数及分布随n/N设定。Theorem5.2的‘arbitrary n’不是固定现实task集合随每源数据增加仍无改善；oracle knows source order才达fasterminimax。pooling可近最佳adaptive、与知道结构oracle不同；作者明确poly(n)tasks是否可恢复adaptivity未决。必要定义/主证明sketch已读，不声称完整附录证明审计。仅报告：明确‘共享最佳解’不等自动可识别transfer-source质量；局部构造对实际Foundation multitask比例无可采用阈值，不把题名当more-data普遍失效。

## [SA-PEF / 2601.20738](https://arxiv.org/html/2601.20738v1)

2+2+2=6。§3/4 123–270、§5 270–322、B1112–1161：本地先w−αe，再localSGD，压缩(1−α)e+g并保新residual；server另η，g本身已经含innerη0，两stepsize不可混同。contractive compressorδ、Lsmooth/unbiased boundedvariance/heterogeneityβ²ν²、s=η0LT≤1/8、ρmax<1/Θ≤.5等方有stationarity bound；constantstepsize保variance/heterogeneity floor，非精确消除compression。正文‘milder compression largerδ’与Definitionδ=d/k方向相反，不采用这句。α近.84–1理论小s下强收缩不授任意α通用稳定。

Flower模拟K100、partial p .1/.5/1、Dirichlet γ .1/.5/1、ResNet9/18/34 CIFAR10/100/TinyImageNet、T5/200rounds/b64/momentum.9、Top1/5/10%5seeds mean/std；主gain在highcompression/lowparticipation，极端lowparticipationfixedhyperparams差会缩小。B按validation等bits grid调lr/serverη/T，comm统计index+FP32value UPLINK ONLY，dense downlink同compressed baseline省略；不是端到端networkwalltime/straggler服务收益。A100/A5000/H200，precision除uplink未明。gradient mismatch在evalmode同minibatch两pointprobe，不证明真实所有更新无错配。仅报告：具体residual owner与preview比例在模拟FL成立，仍需stationarity/participation条件，未外推LLM分布式训练。

## [Structural Anchor Pruning / 2601.20107](https://arxiv.org/html/2601.20107v1)

2+2+2=6，反侧深入。§3 100–140、§4/5 470–560、F3037–3088：只visual↔visual attention columnsum、headmean/max与固定40–60%depth平均选patch；OSR为pruned/full MaxSim比分，不等语义等价；比值denominator为0/负时解释须额外条件，不授所有query通用0–1fidelity。ColPali/ColQwen2/Jinav4、ViDoRev1/v2，AdaptiveEOS quantile对齐keepbudget、random/cluster baselines；10/20%keep局部约90/95%原NDCG。LightColPali25×compression仍更好、differentfullmodelupperbounds，不说无训练总胜。

OSR与NDCG Pearson .635，是中等proxy，不证明ranknoise已完美解耦或训练objective因果破坏结构；middlelayer plateau实测与MaxSim解释hypothesis分开。H200141GB Jinav4 206.05ms/page fullforward vsSAP .05/.06ms MASKGEN ONLY，不含attentionmaterialization访问代价/全索引retrieval/storage/CI，extract‘zeroFLOPs’不等zeroHBM成本。仅报告：query-agnostic middlelayer selector在这些late-interaction协议修正‘任何训练免费高压缩必失败’判断；没有industrial corpus/动态documentbudget，不普遍否定querydependence。

## [Implicit planning metrics / 2601.20164](https://arxiv.org/html/2601.20164v1)

2+2+2=6。§3/4 145–227、总结268–279：10rhymepfamilies/20pairs，Claude3.5 105lines每family train85/test20、test每prompt50samples；noun20pairs vowel/consonant train13/test5+7neutral。Gemma2/3/Qwen3/Llama1–32B base/instruct23models，单token residual mean-difference steering m1.5，layer/position取最大effect。原公式把两项都标C1相减为0，与prose C1/C2冲突，采用prose实验思想但不授公式/代码正确；max选择未说明独立heldoutselection，可能偏高。原train数据足够小、20nounpairs不能普遍taskplanning理论。

未来rhyme/answer改变、前导article a/an及移除原context后lastwordregeneration变化支持早state干预影响后续约束，不仅最后token替换；仍可有通用conditioning/feature传播替代解释，不证明独立完整plan object/chain reasoning。newline效果只少数family/size，lastword更普遍；某些弱base steering劣于baseline。hardware/temp/precision/CI Not Disclosed，task circuits不能移植所有领域。仅报告：该干预+中间输出受约束结果修正单步nexttoken只能局部统计的误解，但不把metric关联升为通用planning保证。

## [One-word rank attack / 2601.20283](https://arxiv.org/html/2601.20283v1)

2+2+2=6，安全深入。§3/4 99–178、270–281：query-aware doc可修改，300d lexicalcenter one-word插首/词替换，whitebox top20gradientpositions实际score择优；不是不知query/blackbox皆91%。MSMARCO8.8M、TREC2019 43queries/2020 54、BM25top100后BERT/MonoT5base rerank，top10排除，PRADA改为同whitebox而非原blackboxprotocol。SR仅排名有一点提高，RB/SB分开，USEcos~.98非句义不变或人类coherence证明；‘one word’可为tokenizer多tokens。

midrank40–80 ISR高为局部Goldilocks条件；top10未测且提升未证明进入实际RAGtopk/下游答案影响。Score饱和解释只是hypothesis无controlledcausal。报告up91%单词改动/heuristic30–60%皆绑定此corpus模型，硬件/精度/latency/query费用/CI未明。仅报告：rank interval与攻击访问budget应靠近威胁评价，不授现代全检索器或微改语义保留保证。

## [TABED / 2601.20357](https://arxiv.org/html/2601.20357v1)

2+2+2=6。§4/5 327–415、B1113–1124、G1565–1624：共享同drafter参数，把multimodal/textonly输入作为batch并混prob；用target已验证hist hard/softlabels在pastwindow挑ensembleweight，缓存历史q/p；没有新增training但多输入forward/cache/historysearch成本仍真实。主窗口ALL，未授在线history新条件最优理论；model68/160M LLaVAtraineddraft、targetLLaVA1.5/NeXT7/13B，single/multiimage与followup、5imageOOD，gamma5/greedy/output128。单drafter跨turn不稳定，dynamic对static/random局部消融支持权重选择。

所谓1.74× WALLTIME是2.29blockeff/(5*.063+1)代入估算，不是完整服务E2E实测；G测A10080GB/fp16/S≤3K/draftB≤4/targetB1/gamma≤10时latency差<5%。oneimage576image+24text FLOPs .09→.17、target66.08，只能说明此小draft负担，并非普遍throughput无成本/长上下文SLO保证。caption variant/其他模型未来扩展不采用。仅报告：已验证历史作为预算内chooser信号的局部可行性，必须小draft/shortcontext/低batch条件；不借通用SD correctness成熟原则抬分或授任意ensemble无额外成本。

## [ES forgetting / 2601.20861](https://arxiv.org/html/2601.20861v1)

2+2+2=6，设计反侧深入。§3/限制72–138，A379–420：Qwen2.5-1.5B/Llama3.2-1B，4mathreasoningtask/200trainexamples、population30与GRPO30rollouts/batch200/minibatch32/500epoch plateau提前停。peakvalidationselected、sameupdatecount并不是matched total compute：ESno-backprop vsGRPOgrad/KL.001，fp16替bf16与chattemplate也调了ES。Table1除LlamaGSM8K多劣于GRPO，LlamaCountdown15.2vs37.6甚至不支持统一‘within3–4points’。

forgetting仅QwenCountdown训练/HellaSwag一个prior-task随checkpoint，约10pointdecline与新task饱和后仍恶化；不是完整多任务continuallearning泛证。相同updates下ESnorm约三数量级更大、tau1e-6阈值sparsity更低是关联，不是因果隔离（没有equalnorm/equalsparsity/无KLmatched control）；norm绝对threshold不能排除学习率/precision差。GRPO正文关联safeupdate也不证明所有GRPO不会forget。RTXA6000/FSDP GRPO、ES硬件数量/CI未明，ES高variance population30限制明确。仅报告：低memory gradientfree设计需独立priorretention指标，局部失败反侧不支持ES不可修复或norm单因果定律。
