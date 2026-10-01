# Apr24 V3 必要证据与真实 Books 判断

作者 apr01；本日窗口 `[2026-04-23T09:00:00+08:00,2026-04-24T09:00:00+08:00)`。复用原始题摘、已读必要正文与有限非作者校准；这里不是新候选分母或完整日级 Gate。日期按 screening 保存的官方公告规则与批次组合判断，Submitted／processing 单字段不冒充首发。普通未读继续执行，不称材料受阻。

独立准入校准后，`2604.20897v1` 与 `2604.21203v1` 均转具体前分母关闭。下方相应小节保留当时实际读到的定义、公式和限制，**其旧 5 分／仅报告提案已失效**，不可用于正式候选表或 Books。

## [2604.20987 Co-Evolving LLM Decision and Skill Bank Agents for Long-Horizon Tasks](https://arxiv.org/html/2604.20987v1)

2+2+2=6，真实知识缺口深入完成，实际整合 AGENT-PLATFORM [Ch84](../../../../../books/part-07-agent/84-agent-platform.md)的可训练 Skill 维护→独立 admission 主线。复用[apr02必要源→owner审阅](V3_APR02_COS_ICL_CAP_CI_INDEPENDENT.md) §3、§4.1–4.3、§5.2、Appendix F 和已完成 root 写后复核，本轮实际再读正文三段及相邻交接。action/retrieval 消费 bank，maintenance 改变下一轮消费输入；policy×bank 交叉组合区分两侧共适应与单纯累积。六游戏、8B 和五功能 LoRA 的有限对照未匹配 frontier 总训练预算，episode-end 与 skill-switch reward 粒度差异不补造统一 credit。正文保额外 rollout、维护与回归成本及冻结库/人工维护回退，不声明共同训练普遍更优，未复现。

原字段 Submitted=2026-04-22T18:17:17Z、v1 Updated=2026-04-24T00:03:33Z、OAI04/24，与官方公告赋号/Thu20EDT slot及邻批共同推本窗08–09；任一字段不独证首发。精度、输入输出长度、线上并发/SLO没有完整披露，不外推生产性能。真实正文及 Review notes 的 SF-2026-ARXIV-2604-20987 已核，单篇实际 I 不代替日级验收。

## [2604.21018 Adaptive Test-Time Compute Allocation with Evolving In-Context Demonstrations](https://arxiv.org/html/2604.21018v1)

2+2+2=6，评价知识缺口深入完成，实际整合 PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)的 feedback-channel→长期 artifact 主线。复用[apr02必要源→owner审阅](V3_APR02_COS_ICL_CAP_CI_INDEPENDENT.md) §4.2、Algorithm1、§5及 root 实际写后通过；本轮再读正文两段及前后。ground-truth oracle 移除已解题并将成功回答回流同一 test pool，评价单位因而是有标签跨题适应序列，不是独立题或可部署 selector。正文 active set 与 Algorithm1 全 test pool 定义差异保留；四轮与一次 warmup、少数 API 模型不能推全配置改善。output-token 匹配不包含 ICL prefill、oracle 和池维护成本，无法恢复反馈/池状态时退回独立 snapshot，而不补造部署等价，未复现。

Submitted=2026-04-22T19:07:29Z、v1 Updated=2026-04-24T00:05:28Z、OAI04/24沿同一公告/邻批组合推08–09，非 processing 首发。完整模型硬件/precision/并发/SLO未披露。正文及 SF-2026-ARXIV-2604-21018 Review note 为实际 source/owner 与写后非作者 PASS，不预支日 Gate。

## [2604.21308 CI-Work: Benchmarking Contextual Integrity in Enterprise LLM Agents](https://arxiv.org/html/2604.21308v1)

2+2+2=6，保护评价深入完成，实际整合 PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)的任务必要传达×隐私→危险进展对照。复用[apr02审阅](V3_APR02_COS_ICL_CAP_CI_INDEPENDENT.md) §3–5.1、Appendix E及 root 写后通过，本轮再读正文与相邻交接。essential-entry conveyance、sensitive-entry leakage 与至少一次泄漏的 case violation 是不同分母；安全沉默不证明完成任务，平均 leakage 也不替代过程权限证据。125 seed 是25人工+100 Gemini-3-Pro 扩充，GPT-5.2用于后续场景/评价链路，不能改称其生成全部 seed；每例4+4 entries、五信息流方向只是受限模拟，不代表真实企业 incident 分布或独立 judge 真值。同源生成/模拟/评分限制及额外 judging 成本写入正文，未复现。

Submitted=2026-04-23T06:00:22Z、v1 Updated=2026-04-24T00:26:04Z、OAI04/24沿公告赋号/slot与邻批组合推本窗08–09，非孤字段确定时点。完整硬件/precision/并发/SLO未披露；真实正文与 SF-2026-ARXIV-2604-21308 的非作者写后状态一致，仍非日级 Complete。

## [2604.21505 Assessing the Impact of Requirement Ambiguity on LLM-based Function-Level Code Generation](https://arxiv.org/html/2604.21505v1)

2+1+2=5，标准完成，拟已有覆盖：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)的开放需求/多种合法实现与“合法多解、缺少条件的不同动作”正文。实际补读§5.1–5.4/§6，与已读四类定义、§4.1三阶段人审结合：沿用原测试的Pass@k只能证明原始规范接受，不能把其它可合理解释的行为都判模型失败；conflict rate是在相同输入时实现输出不同，不是错误率。检测、定位、提出澄清选项是不同接口，GPT-4 judge的50人工样本96%agreement不足以给全部模型/歧义类型的真实识别保证，约50%precision也不能改写成可靠在线澄清Gate。

六代表模型、temperature .8、max1024及原benchmark设置下，局部敏感性与同题多输出分歧可以报告，不证明强模型普遍更差或歧义是唯一原因。当前Ch66具体要求开放需求额外语义审计，并将合法多解的验证与缺条件的澄清分开，已经承担本项拟保留的长期结论；不声称全部Orchid分类/比例已写入。judge/采样增加成本，完整host/hardware、precision、并发/SLO未披露。Submitted=04/23T10:07:33Z、Updated=04/24T00:39:47Z、OAI04/24沿官方公告组合推08–09，不单证首发；待非作者具体Existing终核，未复现。

## [2604.21416 CSC: Turning the Adversary's Poison against Itself](https://arxiv.org/html/2604.21416v1)

**独立准入更正（root，2026-09-28）：具名前分母关闭。**以下为作者已读的原始机制/实验笔记，保留作可复查证据，不再作为本窗候选、评分、仅报告或 Books 采用结论。论文只在通用图像分类 DNN、ResNet18/CIFAR 等任务验证聚类与重标 head；没有研究大模型训练数据/参数/Agent 权限或 Infra 的直接保护合同。把“投毒防护也适用于 LLM”当作连接仅是类比，不满足当前项目范围与贡献准入。详情见 [三项有限复核](V3_ROOT_THREE_ONLY_SCOPE_FINITE.md)。

2+2+2=6，保护深入完成，拟仅报告。已读的early latent方法本轮补§4–5：在训练前十epoch累积DBSCAN可疑簇，疑似poison重标为第n+1虚拟类，冻结feature extractor、仅重训分类head。这是转移trigger→target对应关系的受限保护行为，不是删除trigger表示或任意知识遗忘。正文的可疑簇类别/非最大簇规则与Algorithm1“所有非最大簇”仍须按实现解释，不能把真实稀有良性cluster都视为poison。

四图像分类集/ResNet18、十二列明攻击（有些不适用于全部集）、原攻击配置、单RTX4090/Ubuntu24.04；100epoch主训练加10epochhead、额外早期特征聚类。§5.3 Adap-Blend的precision/recall例外、ABS/IAB recall低于AC和检测误隔离都保留，近零ASR均值只在受测trigger上，不证明适应性对手/新trigger下保护；35.21对29.31分钟仅CIFAR10 BadNets受限成本。当前Ch72的行为抑制/恢复/独立clean切片与不可混同参数删除原则保持；本篇重标head方案没有足以把它采用为大模型资产默认防护的支持，作为具体实现与误隔离风险仅报告，不称整个算法已有覆盖，也不因ResNet小模型排除贡献。precision/concurrency/SLO未披露或对离线训练不适用。Submitted=04/23T08:30:53Z、Updated=04/24T00:33:45Z、OAI04/24沿公告组合推08–09；待非作者窄核，未复现。

## [2604.21159 Adaptive Instruction Composition for Automated LLM Red-Teaming](https://arxiv.org/html/2604.21159v1)

2+1+2=5，安全评价预算触发深入必要审阅完成，拟仅报告。复用§4.1–4.3/Alg1后补读§5.1–5.4/§6–8：query/tactic embedding降维拼接，K500随机候选池上的小bandit适应成功反馈；成功组合去重，探索正则改变覆盖与局部成功的取舍。评价的受限方法差异成立，但embedding相似度/unique query计数不证明语义风险空间覆盖。三个目标模型、Mixtral攻击者和LlamaGuard训练judge，两个目标间迁移5Ktrial与本域10Ktrial区别；aggressive一种迁移仅保留原本56%表现，不承诺普适迁移。

HarmBench另用Llama2-13B classifier、训练后固定行为、每行为最多150attempt，命中是累计至少一次成功，不是单次攻击率或与其它公开数字matched E2E成本。主对照没用WildTeaming私有low-risk pruner，另有bandit GPU/embedding/攻击生成与反馈成本，不能因小bandit称零额外资源。Ch72/66既有累计尝试、sensor与风险分母保留一般约束；本篇有独立的探索操作点可报告，未给把该搜索器采用为通用安全评估默认的证据，不把全部算法称Existing。Submitted=04/22T23:55:32Z、Updated=04/24T00:13:45Z、OAI04/24联合推本窗08–09；未披露完整precision/concurrency/SLO不补造，待非作者核，未复现。

## [2604.21203 Refining Covariance Matrix Estimation in Stochastic Gradient Descent Through Bias Reduction](https://arxiv.org/html/2604.21203v1)

2+1+2=5，标准必要审阅完成，拟仅报告。复用已读Assumptions4–6/Theorem7，本轮重开§3.1–3.3/Eq5–8：平均SGD方差的双向cross-window项减当前outer product，最近两block把相关迭代的covariance估计递推到在线；Hessian-free不是不保留d×d矩阵，单步O(d²)仍有内存/算术成本，也不是迭代独立。正文在线batch长度/起点需按实际两个block一致解释，未核代码不声称递推实现已验证。

strong convexity、最优点Hessian、q≥8梯度矩、stochastic Lipschitz、衰减步长α∈(.5,1)与该batch scaling共同约束收敛率；不把它赋给Adam/非凸Transformer的上线置信证书。理论方法可保为统计训练诊断的条件性分支，但本篇没有建立向现代大模型训练场景的可用保证或可据此修改书稿的工程采纳结论，故仅报告而非“纯理论无价值”。性能负载/硬件/SLO对该定理不适用，不虚构实机收益。Submitted=04/23T01:48:08Z、Updated=04/24T00:17:09Z、OAI04/24沿公告组合推08–09，待必要命题非作者核。

## [2604.21232 ReCAPA: Hierarchical Predictive Correction to Mitigate Cascading Failures](https://arxiv.org/html/2604.21232v1)

2+1+2=5，纠错深入必要审阅完成，拟中心评价定义争议/Books暂缓。复用已实际§3.1–3.5/AppD.1–D.3：action/subgoal/trajectory三个预测/重选接口和first-error后续风险的匹配观测并非因果干预。主文Eq6用log后错概率的负斜率，AppD.3用q(k)/q(1)；q1=.5、q2=.25分别得到ln2与.5，不能把两者当同一PAC指标比较恢复/级联曲线。EPR匹配也没有自动剥离困难样本选择。

只隔离PAC实现/曲线解释及依赖其的中心保证，不否定全部分层控制方法或受限经验。当前Ch79/81 feedback、状态和回退边界不能替代此定义统一，暂不Books；重开材料为实际scorer/代码或作者统一统计定义与相应曲线，不通读全部版本/附件。Submitted=04/23T02:57:50Z、Updated=04/24T00:20:26Z、当前OAI05/12只与已保存公告链联合推08–09，非更新记录日首发；待非作者最小反例核，未复现。

## [2604.21265 Listen and Chant Before You Read: The Ladder of Beauty in LM Pre-Training](https://arxiv.org/html/2604.21265v1)

2+1+2=5，component归因纠错深入必要审阅完成，拟仅报告。实际补§3.4–3.5/§4/§5–6：音乐→语言时仅迁移attention/FFN/norm，词表embedding与LM head重置；poetry→prose同词表继续全模型训练，没有冻结内部计算参数。因此§5.3称新增收益只归embedding/“非重叠参数的orthogonal贡献”缺少桥，epoch0 head start也不能识别独立组件因果。音乐pretrain至200epoch/earlystop，其checkpoint固定seed42；五language seeds不构成五个独立音乐预训。

作者匹配的约14.6K对14.21K语言batch不包含音乐预训总工作，不能称全pipeline matched compute。33K～400K单头八层、序列256、真实/合成同token grammar的数据量与容量反向趋势和有限PPL结果仍成立；matched语言预算和plateau没有证明所有text-only长期不可追回/唯一课程顺序。Ch28数据/重复/预算与迁移接口已有一般分账，本篇受限跨域组件路线可报告，不按小规模拒绝也不采为foundation默认；不添加其无因果支撑的orthogonal保证。Submitted=04/23T04:20:12Z、Updated=04/24T00:23:13Z、OAI04/24联合推08–09；完整GPU/precision/并发/SLO未披露，不外推，待非作者窄核，未复现。

## [2604.20874 The Root Theorem of Context Engineering](https://arxiv.org/html/2604.20874v1)

2+1+2=5，纠错深入完成，拟争议/Books暂缓；作者已读的§3–8必要推导和apr20非作者§3–7.6记录未变，复用[具名审计](V3_APR20_SIX_MINIMAL_ADMISSION_AUDIT.md)，不重读全部附件。给定填充条件的质量下降与有限窗口不蕴含任务次数增长时必须保留完整历史：有限canonical state加有界read-time检索可以完成无限重复任务而保持窗口有界。§7.3另加full-history累积条件，不能在§7.5省略后称压缩是唯一长期架构。§3的first-order linear fidelity也不是所有LLM的无条件单调定律。仅隔离这些中心普遍保证，保留60+session受限实例与压缩可能有效的经验，不由反例否定所有context研究。

本次不写Books；Ch75的预算、摘要失真与read-time检索一般主线不能补上本稿缺失假设。重开材料为作者限定任务/history义务、质量函数适用范围和非唯一分支的修正证明，不要求追加任意benchmark。原Submitted=2026-03-29T20:41:58Z、v1 Updated=2026-04-24T00:00:45Z、OAI04/24只与永久ID公告赋号/Thu20EDT slot和相邻批次合用，推本窗08–09，非Submitted或Updated首发孤证。非性能材料，不适用生产batch/concurrency/SLO；未复现。

## [2604.20897 Watts-per-Intelligence Part II: Algorithmic Catalysis](https://arxiv.org/html/2604.20897v1)

2+1+2=5，标准完成，拟仅报告。复用作者§3–5/§7.1必要定义与[apr20具名非作者审阅](V3_APR20_SIX_MINIMAL_ADMISSION_AUDIT.md)：speedup是固定任务/智能要求、reference state下的irreversible-operation比，不是GPU计时或测得joule；generic implementation改进已吸入baseline，adapt/restore/deployment horizon分别承担成本。有限cache例的支持集扩张不覆盖真实heavy-hitter请求分布。§7.1的nd+n编码只是一个表示上界，简单affine子空间可以更短，不能作为精确Kolmogorov复杂度等式；受限枚举计数分支仍成立。

此条件理论值得报告，但没有给现代LLM硬件/请求分布的可用热力学节能证书，不向Ch70写设备功率或通用cache选型保证，也不声称算法理论全已覆盖。Submitted=2026-04-21T13:36:33Z、v1 Updated=2026-04-24T00:01:12Z、OAI空，与官方slot/ID分配及邻批联合推08–09，非单字段证明。硬件/精度/长度/并发/SLO对其抽象计数不适用；任何数值功率外推均不采用。

## [2604.21251 CAP: Controllable Alignment Prompting for Unlearning in LLMs](https://arxiv.org/html/2604.21251v1)

2+1+2=5，纠错深入完成，拟中心理论争议/Books暂缓。复用作者§3.1–3.3、Eq1–4、AppB和[apr02实际非作者核](V3_APR02_COS_ICL_CAP_CI_INDEPENDENT.md)：固定benchmark query的reference A=a(Q)时H(A|Q)=0，I(Y;A|Q)=0；跨query reference负例没有成为固定q下p(a|q)的条件抽样，因此不能将InfoNCE式直接作为该条件MI随prefix变化的下界。B.2的embedding proxy也不是实际KL证书。只隔离条件MI解释与privacy-compliance保证，保留冻结模型、训练可撤销prefix的受限行为抑制接口和实验，不声称所有prompt效果不存在。

Ch72已明确unlearning须声明secret substrate/observer与恢复攻击，prefix撤销可恢复不能支持参数删除；但既有原则不能修复本稿中心数学桥，故不以已有覆盖免除争议。重开是作者统一随机变量、条件采样和所声称下界/实现，不扩完整版本史。Submitted=2026-04-23T03:42:41Z、v1 Updated=2026-04-24T00:22:06Z、当前OAI05/18，与官方批次依据联合推08–09；不把后记录日或更新字段当首发。未复现实验。

## [2604.21677 Geometric Monomial (GEM): a family of rational 2N-differentiable activation functions](https://arxiv.org/pdf/2604.21677v1)

2+1+2=5，标准必要审阅完成，拟仅报告。复用HTML失败后已实际读的官方PDF-v1 §2.1–2.3、§3 CUDA说明、§3.2/3.3/4关键反例：有理gate的接合光滑度与scale是具体算术分支，基型/EGEM负半轴零梯度与SE-GEM不同；光滑阶数不等学习更好，高N深CNN退步与GPT/BERT epsilon排序反向均保留。独立elementwise CUDA kernel受带宽约束，少算术不等FFN或完整推理加速。

报告保留函数选择的条件性证据，不将一个activation operating point升级为Transformer默认或全局无梯度消失保证，不新增Books。独立算子与模型质量评价配置不能合并成生产latency/concurrency/SLO；未披露字段不补造。Submitted=2026-04-23T13:42:49Z、v1 Updated=2026-04-24T00:50:49Z、OAI04/24沿已保存公告/邻批组合推08–09；尚待本项有限非作者终核，未复現。

## [2604.20994 Breaking MCP with Function Hijacking Attacks: Novel Threats for Function Calling and Agentic Models](https://arxiv.org/html/2604.20994v1)

2+2+2=6，安全接口深入完成，拟已有覆盖：AGENT-MCP [Ch83](../../../../../books/part-07-agent/83-mcp.md)“Tool Description是可执行的Discovery Interface”及“MCP不等于Tool Authorization”。实际§4/5、§6.3、§7–9：攻击方可修改一个已列工具的description，不能改user query；离线梯度搜索作用于所测模型，转移评价另有边界。这证明tool-selection surface可由描述变化操纵，不证明未获权限的工具已执行或任意black-box系统都可破。名字命中与带参数完整调用不是同一ASR，BFCL-v3 multiple 200题/2–4工具与五模型有限配置不外推总体生产风险。

同意图改写的迁移与不同意图迁移分开；§7明确单意图攻击在其它意图失败，多payload扩展主要是单个BFCL样本及50扰动，不能称全目录通用鲁棒。优化epochs、suffix/context与额外搜索成本属于风险预算，未披露完整E2E时延/并发/SLO；不照录70–100%为统一攻击率。当前Ch83具体要求description/schema/server-tool身份同版发布、selection-effect test及描述变更后失效重测，并在effect time独立复核权限，已承担本次长期边界；不声称其全部搜索算法或ASR已写入。Submitted=2026-04-22T18:32:38Z、Updated=2026-04-24T00:04:01Z、OAI空，与官方slot/ID和邻批联合推08–09；待非作者复核此具体Existing，未复现。

## [2604.21160 Reinforcing 3D Understanding in Point-VLMs via Geometric Reward Credit Assignment](https://arxiv.org/html/2604.21160v1)

2+2+2=6，真实知识缺口触发深入必要审阅完成，拟TRAIN-GRPO Ch33窄分支，尚未非作者采用/未写。实际重开§3.3–3.5/Eq6–16、§4.2/Table3与§4.5：JSON字符span按累计解码offset回到token index，四geometry field各自产生group-relative advantage，仅路由本字段span；语义/格式background另接平均字段advantage与RPC混合。RPC比较预测3D投影与预测2D，相互一致不是独立几何真值；KPA是落入GT box的containment，不是关键点坐标逐一正确。解析/char-token对应、字段group support及background混合是不同于完整回答reward或集合Shapley span的具体训练接口。

对读Ch33“Sequence Reward怎样作用到Tokens”与其集合/首错/denoising分支，已有一般process granularity但没有结构字段解析身份→独立字段归一→background的一条责任链。拟在通用process说明后补两段，强调malformed/重叠token边界、零方差组及独立几何验收是工程要求，不冒称作者已验证完备parser防御。Qwen2.5-VL3B/PointBERT、ShapeNet、4×A80080GB，SFT两epoch b128、RL一epoch G8、λ=.15；Table3 GRCA-only IoU3D .683低于broadcast .684，RPC分支 .686只支持有限设置，近似48小时不是全管线成本可比。precision/concurrency/SLO未披露，未复现。Submitted=2026-04-23T00:01:40Z、Updated=2026-04-24T00:14:03Z、OAI04/24仅联合官方公告链推08–09。

## [2604.21794 Learning to Communicate: Toward End-to-End Optimization of Multi-Agent Language Systems](https://arxiv.org/html/2604.21794v1)

评分2+2+2=6，纠错触发深入审阅，拟中心实现/保证范围争议、Books暂缓。实际读exact-v1 Figure1、§3.1–3.4、§4.1–4.2、§6、AppendixA/C/D：四顺序Agent将固定数量latent KV片段追加到共享trace，不覆写旧片段，最终输出的teacher-forced CE只更新LoRA而base冻结。但Figure1写上游trace构造without gradient updates、只更新最终Agent的LoRA；§3.3及AppendixC却写梯度跨全部stage、联合训练上游编码与下游解释。共享参数在最终stage更新也可能改变上游下一次forward，并不等于梯度实际经过本次上游计算；必要实现图、detach位置和参数共享/优化清单未统一，不能将本稿直接作端到端joint training的正面实现依据。

Proposition3.1/Eq5在各overwrite Jacobian范数≤ρ<1的额外条件下给衰减上界，Eq6的concatenation子块梯度≤整体梯度也成立；后一式是上界，不能推出每个子块非零、同强度或不随decoder注意力衰减。正文“各stage可比梯度”的普遍解释超出此桥，不据此否定追加trace可能有效或全部有限实验。实际§4/AppC是210道Hendrycks Math一epoch、50道HumanEval十epoch、700正确Gemini轨迹CSQA一epoch；**AppendixD明确从评价中排除50训练题**，不记为未排除或已证数据泄漏。A40/H200与LoRA r8/α16、gradacc64已披露，但joint trajectory、单Agent SFT和C2C不同训练数据使增益不能全归通信接口；§6同一AIME24上TextMAS+SFT与DiffMAS持平、40latent步反退也保留。精度/完整训练与推理成本、并发、SLO未披露。

实际对读Ch82“通信可以压缩成latent，但contract不能一起消失”及receiver-conditioned trained handoff：现有producer/consumer identity和fallback不能替代本稿未统一的计算图，故不写Books，也不称已有完整覆盖。重开只需作者统一Figure1/§3.3/AppC与可核梯度/optimizer路径，及明确Eq6解释边界；不要求全版本史或追加全部benchmark。原字段Submitted=2026-04-23T15:53:25Z、Updated=2026-04-24T00:57:58Z、OAI当前04/24，与官方公告分配/Thu20EDT slot和邻批联合推断本窗08–09，非任一字段独证。官方abs当前仅v1、无撤回说明；待非作者窄审。

## [2604.21809 Quotient-Space Diffusion Models](https://arxiv.org/html/2604.21809v1)

实际读exact-v1 §3.1–3.2/3.4、平滑商空间/群作用条件及官方abs-v1；原准入一般生成机制仍成立，分子应用不作为项目目标。Ginvariant prior/equivariant drift条件下，投影SDE须含平均曲率修正，不是直接删群方向；horizontal lift给同商过程，Corollary3在其分布前提下给原对称分布。translation非紧不能直接选translation-invariant概率，实例先去center-of-mass再SO3；非退化/光滑商空间和模型条件不可丢。aligned target与ordinary sampler的目标桥是受限方法问题，不能外推所有对齐都错误、有限步实现完全保持分布，或一般生成更快。

**日期/重复家族隔离，不进入本窗确定候选、不评分或Books。** 官方abs Comments为ICLR2026 Oral，定点检索已恢复同题OpenReview匿名under-review正文[官方PDF](https://openreview.net/pdf/ad24b2428a4d3403fbc30f18deabd58b5ea82589.pdf)和同作者正式稿[官方PDF](https://openreview.net/pdf?id=3JPAkwSVc4)，已实际读取题名/摘要及一般商空间中心框架，不能把arXiv首次赋号当整个家族首次公开。Forum与api2官方note两入口都返回challenge，尚不能取原公开时间字段或本窗重要修订说明；搜索“11months”不是原始公开日期，ICLR接收身份也不是具体首发日。保留原Submitted=04/23T16:04:40Z、Updated=04/24T00:58:46Z、当前OAI05/15而不改名。可恢复材料为官方note公开时间/历史正文时间和足以证明本窗新增事件的说明；只重开这一家族，不扩会议/完整版本差分。既有必要方法阅读有效保留。

## [2604.21829 Black-Box Skill Stealing Attack from Proprietary LLM Agents: An Empirical Study](https://arxiv.org/html/2604.21829v1)

评分2+2+2=6，保护行为触发深入完成，拟仅报告。实际exact-v1 §III、§IV-B–E、§V-A–D：公开用户/API权限无backend直接读取，但runtime读取skill后可在文本响应复述。主实验目标是公开的find-skills SKILL.md，不能以目标复现单独证明非公开秘密仅从当次runtime流出、厂商后端泄漏或版权归属；若要证明这些，需独立未知canary、启用/停用加载对照及访问trace。本稿120个自动生成probe和最多三次尝试支持有限接口风险，best-of-three不是每请求成功率。EM为规范化完整目标子串命中，ROUGE/embedding cosine不是泄露字节比例；target-aware模型judge也只是其语义sensor。

输出LAN复用泄露judge与NVRecall，阈值.85/.30，flagged响应移除后计算剩余响应分数，不可把接受集结果当全流量零泄漏或无效用成本。§V-D/TableIV实际有翻译/改写仍高语义分数而EM近零、同LAN部分改写几乎未改善的反证；本稿自己的讨论限制了§V-C防护宣传。正常find-skills问题的误报对照只覆盖其benign集，未证明任意任务不被误拒；完整grader/token、时延、硬件、并发与SLO未披露。

实际对读Ch72“Secret Release需要跨Agent的Root Identity”与“Safety Evaluation单位是Run”中root secret、detector/policy分权和attempt budget：长期原则已承担保密对象/输出sensor/累计尝试分账，但不声称全部LAN算法已覆盖。本稿公开skill单目标与接受集分母只能保留受限实验及检测失败条件，不因此把LAN采为通用保密防线，故仅报告而非Existing或新的Books必需更新。原字段Submitted=2026-04-23T16:18:47Z、Updated=2026-04-24T00:59:32Z、当前OAI04/28；沿公告slot/ID与邻批联合推断08–09，不将近截点processing当逐篇首发时刻。官方abs-v1无撤回说明；待非作者必要命题复核，未复现。

## [2604.21772 Back to Source: Open-Set Continual Test-Time Adaptation via Domain Compensation](https://arxiv.org/html/2604.21772v1)

评分2+2+2=6，标准完成，拟仅报告。实际读exact-v1 §3/4.1–4.3、§5.1–5.3、B.3、C.1及官方abs版本说明。先用当前prompt下与固定源类原型的距离作二簇ID/OOD proposal；只在拟ID上以源均值/方差对齐和pairwise cosine结构正则更新prompt，再把更新prompt用于同batch拟OOD。原分类器冻结、其输出仍限已知类，并不是学习新类的开放世界分类器；同batch共享域因素是传播假设，结构正则与AUC不能证明语义真实解耦。小batch另启64历史距离FIFO及无ID跳过，不把主结果当相同路径。

ViT-B/16/ImageNet-1K、15种ImageNet-C severity5及6种LAION-C severity3，6类OOD数据同样受腐化；batch64、300源样本、初始prompt50次更新、8prompt/AdamW。超参数只首个dataset-domain调后冻结；ACC、AUC及两者调和H-score分别报告，AUC不是线上阈值保证。单Quadro P6000下相对Tent时间为1.9/2.1，不能称无适配开销；各baseline可更新不同参数/取不同源统计，消融仅支持所测联合选择。当前Ch23表示/融合与Ch66域漂移验收存在通用分权，本算法尚不是已覆盖的全实现，但受限视觉TTA操作点不足以采作大模型线上适配默认分支，保留本报告不强加Books。

原字段v1 Submitted=2026-04-23T15:29:29Z、v1 Updated=2026-04-24T00:57:05Z、当前OAI=04/24。官方abs本次可读、Comments为CVPR2026接收，无撤回说明。归属沿本日已保存官方公告赋号/Thu20EDT slot与邻批联合推断08–09，不将任一字段改称公开时间。待独立采用复核，非日Gate。

## [2604.21776 Reshoot-Anything: A Self-Supervised Model for In-the-Wild Video Reshooting](https://arxiv.org/html/2604.21776v1)

评分2+2+2=6，标准完成，拟仅报告。实际读exact-v1 §3.1–3.2/4.1–4.3/5.1–5.3及officialabs-v1。单目视频的两条独立平滑crop轨迹构造source/target，dense tracking与crop offset把源帧forward warp为有孔洞anchor；source提供纹理、anchor提供目标运动提案。训练以双流token self-attention、source temporal RoPE offset50及高噪声模型source重建loss回应对齐，低噪声模型不使用同一auxloss。2D训练未直接监督真实4D重建，图像间路由与生成补全不能当几何或物理真值。

Wan2.2-14B、约100k单目clips/30k视频+15%合成多视图、rank512 LoRA/patchify更新，2ksteps、batch24；test100条5秒480p/16fps，部分baseline只比前49帧。跨模型比较有1.3B旧checkpoint混杂；组件消融支持所测recipe而非所有self-attention比cross-attention强。更大角度需合成支持，双视频使token长度翻倍，未披露完整硬件/precision、并发或SLO。对读Ch25视角reference/geometry分责和Ch23位置身份：这些已有原则不能说明本伪视图训练算法全已承载，但此有限重拍训练分支未提供普适的世界状态或执行保证，报告保留其方法与非刚性支持边界，不为配方单独追加Books。

原字段Submitted=2026-04-23T15:32:56Z、Updated=2026-04-24T00:57:11Z、当前OAI=04/27；OAI是当前记录不是首发。officialabs-v1与所读HTML题名机制一致，v2 Submitted=04/24T04:18:46Z在窗后，不追版本差分。归属用已保存官方公告链/邻批作08–09有据推断而非Submitted或Updated孤证；待独立采用复核，非日Gate。

## [2604.21725 AEL: Agent Evolving Learning for Open-Ended Environments](https://arxiv.org/html/2604.21725v1)

2+1+2=5，标准必要审阅完成，拟仅报告，待非作者核。实际§3–4：fast Thompson选择memory策略，slow窗口反思诊断并影响prompt；低pool reward条件下新增retrieval arm，默认planner/tool固定。训练/validation/test顺序划分，test全部bandit/memory/evolution冻结，不是无限在线稳定适应。208episode/10ticker/五seed，复杂planner/tool/credit等变体反退；反思文字称“causal insight”不构成唯一因果识别。先诊断再扩策略池有受限可行性，但小样本Beta历史、合成先验与模板偏差不能推出普遍稳定。

当前Ch77检索/placement和Ch81候选/evaluator/search-holdout已有可复用控制边界，本篇具体双时标operating point与简单credit反证报告，不声称完整算法已有，也不把金融回报作为当前项目目标。版本纠正：库存题名“Evolving Agent Harness”、support-ticket扩展及provably no-harm属于较后口径；official abs-v1、PDF首页与HTML为本节题名、原顺序portfolio实验，不采用库存理论/跨域扩展。Submitted14:29:25Z、Updated00:53:29Z/OAI空仅与官方公告组合推08–09。未复现，不外推性能/成本/SLO。

## [2604.21728 Ramen: Robust Test-Time Adaptation of Vision-Language Models with Active Sample Selection](https://arxiv.org/html/2604.21728v1)

2+1+2=5，标准必要审阅完成，有限非作者核后仅报告。System Reach 限于视觉分类测试时适配组件：梯度缓存未跨越 serving、持久模型资产或线上发布边界。实际§3.1–3.3/§4/§5：每query从固定pretrained状态出发，只适配normalization affine参数，再推理并reset。按pseudo-class FIFO和embedding相似度选support，复用同一base参数下的sample gradient做加权组合，因此不是在不断变化的长期权重上随意复用旧梯度；若改成持续更新，cache identity条件就不再由这一方法支持。所谓无额外forward/backward仅指support重算，当前sample算梯度、更新、第二次推理、检索/存储仍有成本。

CLIP三ViT、CIFAR-C/ImageNet-C/DomainNet mixed stream对照；域相似只是proxy，pseudo-label错误与不平衡可能影响选择，小k噪声/大k跨域混合保留。单normalization/二分类/小步长理论不能代表整encoder无条件增强class特征。490×相对naive support重算，不是部署吞吐/SLO；原分类TTA可行性有新增局部机制，报告保留，不据此将该算法采成Agent Memory或通用LLM适配默认。原页面配置之外不补precision/并发。Submitted14:33:27Z、Updated00:53:43Z/OAI04/28是处理/当前记录，沿公告组合推08–09，未复现。

## [2604.21741 Hi-WM: Human-in-the-World-Model for Scalable Robot Post-Training](https://arxiv.org/pdf/2604.21741v1)

2+2+2=6，真实训练/模拟状态缺口深入必要审阅完成，拟Ch26窄分支，source→actual-owner/literal 已 apr02 独立通过，尚未实写，不计 Integrate。采用实际官方 PDF v1 §3.5/§4.1–4.4及Table2；HTML内部Aug24标签不作原始v1依据：policy在action-conditioned world model闭环，失败前状态缓存允许human短纠正后返还policy，同一模拟状态rollback/branch多次，纠正片段和真实演示合并posttrain。Ch26目前human在线RL与counterfactual proxy/real residual分权已有，但缺这一“模拟失败状态复用→分支纠正片段→真实重新验收”的数据采集责任；不把模拟终态升为物理事实。 具名有限审阅见[三项独立记录](V3_APR02_THREE_21632_21724_21741_INDEPENDENT.md)，不代替日期或日级Gate。

14维双臂动作、YAM-Ultra15Hz、三个刚/柔任务、DP/π0、有限匹配posttrain budget。Edge-case数据与failure数据支持覆盖内定位/控制，十分钟Push-T插值是定性演示；r=.953是有限policy/task相关，不证明所有错误状态准确或唯一因果。人纠正相对只收成功sim轨迹存在数据支持差异，不能将整体收益唯一归rollback。成本含setup/labor/inference的作者模型，不冒称真实省近十万美元部署账。保留world-model训练/人检/branch成本及分布外回退真实机器人纠正；precision/batch/并发/SLO未披露不补造。Submitted14:42:54Z、Updated00:54:28Z/OAI05/06仅组合日期线索，08–09有据推断；未复现。

## [2604.21765 PrismaDV: Automated Task-Aware Data Unit Test Generation](https://arxiv.org/html/2604.21765v1)

2+1+2=5，标准必要审阅完成，拟仅报告，待非作者核。复用此前实际§4/§5.1–5.3/§8.3，当前补核§5.3与8.3：以有失败constraint的task–column凝缩train，按最低failure precision回溯assumption/code生成反馈，同时联合修改耦合module prompts；eval在每round固定且不按失败凝缩。局部CFPr不是全F1、任务成功真值或因果识别，训练非降门槛也不证明新任务有效。

60tasks/五单表文件datasets、25batches、train/eval/test任务3:3:4、observed/new batch1:1、15完整eval预算、两seed、gpt5 proposer/gpt4.1mini backbone。NewTasks略胜manual，GEPA不同封装和反馈内容构成比较条件，不证明GEPA不能优化一般组合系统；测试不了所有未访问列/错误类型。Ch81状态化prompt/scaffold候选更新与evaluator-holdout保留一般约束，本篇稀缺反馈的选择性操作点值得报告，但不采用其具体诊断算法为通用默认、不称全算法已Covered。API总预算/hostprecision/concurrency/SLO未披露。Submitted15:18:50Z、Updated00:56:37Z/OAI04/24沿公告组合推08–09，未复现。

## [2604.21632 To See the Unseen: on the Generalization Ability of Transformers in Symbolic Reasoning](https://arxiv.org/html/2604.21632v1)

2+2+2=6，知识缺口及理论限定深入必要审阅完成，拟Ch12条件性机制，source→actual-owner/literal 已 apr02 独立通过，尚未实写，不计 Integrate。实际§3–6、AppA/B/E：input/output tying使未作为label出现的softmax row仍受归一化梯度与weight decay，未见token的输出行差异可能收缩，从而损害多个新符号的区分；copy shortcut、冻结/reset及训练符号diversity分别改变读出、参数与数据支持，并非一个通用解决方案。Ch12当前weight tying只讲共享参数，尚无这一训练支持压力分支。 具名有限审阅见[三项独立记录](V3_APR02_THREE_21632_21724_21741_INDEPENDENT.md)，不代替日期或日级Gate。

Lemma4.1印刷上界遗漏小步长条件：取feature为0、r=0、λ=1、η=2、两个不同未见row，更新差异反号但范数不变，右侧却为负。只隔离未限定η的普遍收缩保证；补ηλ≤1后仍须r²p<λ，不能把GD/SGD条件推广成AdamW定理。AdamW现象另由实验支持。60–75M逻辑模型、100未见符号与有限Gemma3 unused-row微调显示受限失败/干预；AppE冻结embedding显著损害C4 loss，临时reset停止后普通结构可再失败，cosine本身不是因果证书。具体训练b256/AdamW等见AppB，不推所有稀有词或部署收益。abs-v1同题，Submitted12:51:10Z、Updated00:47:30Z/OAI04/24沿已保存官方公告组合推08–09，非单证首发。未复现；理论采用须非作者核这一窄条件。

## [2604.21686 WorldMark: A Unified Benchmark Suite for Interactive Video World Models](https://arxiv.org/pdf/2604.21686v1)

2+2+2=6，标准必要审阅完成；非作者有限复核后维持仅报告。以官方PDF v1首页（Date: April 24, 2026）及§3.4/4为本次版本和机制依据；HTML `/v1` 内部脚注却显示 August 24, 2026，不能据它的内部日期证明原始版本。PDF v1确认共享WASD/LR通过每模型adapter标定step/yaw，再在同场景/动作下比较六模型、三轴八指标。六模型/500cases、50参考场景及合成第三视角、20–60s有限协议不是所有world model能力。DROID-SLAM几何和Gemini3.1Pro判断仍是proxy，动作选择与评分共享VLM、adapter语义等价未有独立全域校准证明；有限人评rank相关不等真实物理控制真值。Ch25现有perceptual/geometry/action分权足以承担长期边界，本suite作为受限操作点报告，不称全算法已有覆盖。

重要版本纠正：旧库存摘要写十模型、direction purity/latency/stability四控制量；当前official abs-v1与PDFv1却为六模型及translation/rotation error，PDF全文无latency字段。初筛依据收窄到原始v1真实的共享动作映射与多轴比较，不回填八月v2扩展；不需要全版本差分。Submitted13:50:47Z、Updated00:51:04Z/OAI空，结合官方slot/ID/邻批有据推08–09；非Updated孤证。未披露的运行precision/concurrency/SLO不补造，未复现。

## [2604.21700 Stealthy Backdoor Attacks against LLMs Based on Natural Style Triggers](https://arxiv.org/html/2604.21700v1)

2+2+2=6，保护深入必要审阅完成，拟Ch72窄训练/评价分支，未独立采用/未写。实际§III、§IV-A及C–F：有权修改隐藏system prompt或注入LoRA的提供方，用自然风格输入触发指定内容；这是资产/配置写权限威胁，不是普通用户仅靠低权限输入突破sandbox。长答案whole-response CE会稀释目标片段监督，另设poison强化/clean抑制target loss改变训练选择性。Ch72现有trigger邻域/强度矩阵未解释这一长生成target-credit分支。

20%poison、Alpaca500train/200test、四种开源模型规模与GPT prompt-only、有限分类及200下游任务；ASR字符串/benign FPR/METEOR分母不同，不把流畅或低PPL当不可察觉安全。Legal及Sentence某下游FPR很高，aux不是所有trigger全面胜；输出反演还会被正常无害prefix诱导，不能将一次inversion检测失败当无后门。必要配置和威胁权限均保留，未承诺未知输入/输出防御全部失败。official abs-v1同题，无页面撤回标记；Submitted14:08:53Z、Updated00:51:56Z/OAI04/24仅联合公告依据。未复现。

## [2604.21724 Beyond N-gram: Data-Aware X-GRAM Extraction for Efficient Embedding Parameter Scaling](https://arxiv.org/html/2604.21724v1)

2+2+2=6，知识缺口深入必要审阅完成，拟Ch12 hashed n-gram容量分支，source→actual-owner/literal 已 apr02 独立通过，尚未实写，不计 Integrate。实际§4/§5.1–5.5：频繁token专用表、尾部频率平衡bucket/alias与多hash混合；局部causal ShortConv/SwiGLU重新提取动态n-gram，再按层注入value与residual。这不同于只把词表变大：更新频率分配、局部提取器与层位职责需共同验收。当前Ch12只有静态hash容量/collision/skew与allocation frontier，缺这条训练支持机制。 具名有限审阅见[三项独立记录](V3_APR02_THREE_21632_21724_21741_INDEPENDENT.md)，不代替日期或日级Gate。

当层value注入可保持其Q/K，但后层状态已改变；host预取的带宽估计不包含所有launch/控制开销，compute-decoupled不是所有FLOPs免费。0.73B/1.15B、训练token与受限memory budget对照；memory大小还改变hash/view配置，不能把质量差全部归单一容量。早层/全层注入比较也改参数，frequency proxy/与初态余弦不证明语义容量。0.73B的2×平均49.7高于4×49.5，保留非单调与新增训练/缓存成本。official abs-v1同题；Submitted14:27:10Z、Updated00:53:28Z/OAI04/27当前记录，与官方公告slot/邻簇联合推本窗08–09，不将后记录日改owner。未复现/未部署，尚待非作者采用。

## [2604.21461 Do MLLMs Understand Pointing? Benchmarking and Enhancing Referential Reasoning in Egocentric Vision](https://arxiv.org/html/2604.21461v1)

2+1+2=5，标准必要审阅完成，拟仅报告，待非作者核。复用已实际§3.2/§4.1–4.5/Limitations：模拟ray-cast给指向物体标签，真实指认另采，手势定位和定位后的reasoning失败分开；400错误子集诊断及LoRA rescue不是全任务比例。11K题目与微调收益本身不证明视角/近手/显著性唯一因果，没有独立改变这些cue的完整反事实控制。Ch66 Self-report/Behavior Probe/Deployment Outcome已有多层证据分权，但不称该egocentric指标全已承载；受限“先ground gesture再reason”诊断值得报告，不因此更改通用评估或VLA训练标准。真实域收益弱于模拟域、短单轮问题和人工/模拟标签条件保留；未披露的precision/batch/concurrency/SLO不补造。官方abs-v1同题、无撤回/纠错标记；Submitted04/23T09:15:42Z、Updated00:37:02Z/OAI04/24只与官方slot/ID/邻批联合推08–09，不单证首发。未复现。

## [2604.21590 AgenticQwen: Training Small Agentic Language Models with Dual Data Flywheels for Industrial-Scale Tool Use](https://arxiv.org/html/2604.21590v1)

2+2+2=6，真实知识缺口深入必要审阅完成，拟TRAIN-DATA Ch27，待非作者采用/未写。实际复用§4及重新读§3.1–3.3/Algorithm1：linear轨迹先扩条件behavior tree，再选branch反推environment state/user instruction/agent SOP，令目标路径由条件变得必需；mock user可提出误导要求，正确branch需由环境/权限条件支持。这改变的是合成任务的触发条件与输入职责，而不是仅把旧题随机变难。Ch27 synthetic generator/judge同源错误、evidence-first真实trace反推QA已有；尚未明确“路径扩展→逆生成触发条件→三输入分权”的模拟数据分支，拟仅在synthetic compilation主线窄补。

更强模型成功走预定branch只是mock环境的一种admission，既不证明真实工具状态/授权，也不保证任意支路合理；所谓multi-model consistency实际Qwen3-235B同模型三次一致。失败导向采样可能反复强化同源盲点，需保留输入/branch/rubric lineage与独立真实tool canary，这是工程判断，不称作者已验证。§4模型总体提升没有独立剥离两flywheel匹配消融，工业结果混合部署，不将recipe效果唯一归此结构。必要实验配置沿原读§4记录；新增mock生成与过滤成本、真实状态失配回退固定真实轨迹。官方abs-v1同题；Submitted04/23T12:14:52Z、Updated00:44:52Z/OAI04/24联合支持本窗08–09推断，未复现，未扩Science persona应用或全部附件。

## [2604.21592 Sculpt4D: Generating 4D Shapes via Sparse-Attention Diffusion Transformers](https://arxiv.org/html/2604.21592v1)

2+1+2=5，标准必要审阅完成，拟仅报告，待非作者核。复用已实际§3.2–3.3/§4.1–4.4/§7–8：token全部保留而连接稀疏，全局首帧anchor读权、局部时域与按时间差改变block同余密度不是删远帧表示。索引同余本身不证明3D语义对应，首帧anchor通过局部实验而非全局最优证明。Ch24分层生成/稀疏执行已有主线，本篇4D受限mask取舍可报告，未形成需将该特定mask采为通用默认的证据。

保留apr20_resume实际纠正：Table2 noanchor CD/IoU/F三项均劣于Ours；几何更好/代价更大的是conservative与fullattention，不写“无anchor更好”。预训练3D模型、有限4D训练、50对象、几何标签条件与长序列退化保留；FLOPs节省非端到端SLO，未披露precision/并发/线上SLO不补造。官方abs-v1同题、无撤回/纠错说明；Submitted04/23T12:18:55Z、Updated00:45:03Z/OAI04/24仅公告组合线索，08–09有据推断。未复現或重读所有附件。

## [2604.21611 Process Supervision via Verbal Critique Improves Reasoning in Large Language Models](https://arxiv.org/html/2604.21611v1)

2+2+2=6，标准必要审阅完成，拟仅报告，待非作者核。实际§3–4.4，actor参数固定，supervisor step-level文字critique条件化再生成，非gradient policy update/可执行局部reward。所谓matched compute的SC@5只约五倍actor tokens且无supervisor；Reflexion同supervisor并限制outcome critique，但原文没有逐调用完整token/硬件成本matched证明。R=1–4非单调、强actor被critique后可低于standalone，r=.90只是有限model-pair相关，不证明headroom唯一因果或第四条普律。§3“ideal fixed point”无可验全局收敛条件，不采用收敛保证。

GPQA198/AIME30/LCBV6，GPT5.4 effort变体与三开源model-pair，单run且作者明确camera-ready才加误差；科学题只为通用推理测试不引入AIforScience应用。代码任务文字critique的有限失败不证明所有runtime错误不能用语言描述。Ch80 evidence-gap/verifier-biased reflection、Ch33 Critic须改善后续Solver并保留teacher-student可教性已有长期边界；本篇步骤粒度/不同pair反证值得报告，但不声称全部本实验已有覆盖，也不将现有原则加一个benchmark变成新默认编排。硬件/precision/batch/concurrency/SLO、全API预算未披露。官方abs-v1同题无撤回说明；Submitted04/23T12:36:12Z、Updated00:46:15Z/OAI04/24沿slot/ID/邻批组合推08–09，未复现。

## [2604.21571 Separable Expert Architecture: Toward Privacy-Preserving LLM Personalization via Composable Adapters and Deletable User Proxies](https://arxiv.org/html/2604.21571v1)

2+2+2=6，保护主张深入必要审阅完成，拟仅报告，待非作者核。实际§2–5：冻结base及共享domain LoRA，用户routing bias/steering/personal LoRA另存proxy，删除/旁路proxy后在有限heldout prompts比较基线分布。这个架构确实把新增个人适配的写入目标从共享权重移到可撤销资产；但不训练共享参数并不证明base原来没有该用户信息，也不覆盖merged副本、cache与日志。§2的KL阈值只是受限验证：§3四合成用户/四域、20prompts、140runs，§4约82–89%通过并非所有输出严格恢复；keyword style count及Jaccard相似都不是完整隐私或membership攻击验收。DP-SGD只是可兼容扩展，未取得端到端DP保证。

实际对读Ch72“Unlearning必须分开参数擦除与推理拒答”的删除对象/参照与部署artifact身份，以及可恢复资产权限段：这些已承担长期判定边界；不能称本三层架构已全部写入。保留冻结共享组件×可撤销个人proxy的受限可行分支，不把“deterministic unlearning”采用为完整概念/训练影响删除证明，也不为架构组合强写Books。Phi3.5-mini3.8B/Llama3.1-8B、NF4、expert r32/personal r4、路由BART-MNLI；硬件、batch/concurrency/SLO未披露；§5承认四个域分离明显、缺组件消融和proxy文件保护。官方abs-v1同题；Submitted04/23T11:51:31Z、v1Updated04/24T00:43:46Z/OAI04/24与既有官方赋号/slot/邻批联合支持08–09推断，不是单字段公开证据。未复现。

## [2604.21579 A Metamorphic Testing Approach to Diagnosing Memorization in LLM-Based Program Repair](https://arxiv.org/html/2604.21579v1)

2+2+2=6，标准必要审阅完成，拟仅报告，待非作者核。实际§III–VI：自然/语义保持代码变换后比较test-adequate repair，原文件NLL percentile与SR差值作关联；§IV-A只以原始至少一轮能解决的bug为分母，闭源每prompt5patch而开源1patch，不是matched search预算。Defects4J广泛下降而GitBug-Java平均趋势弱，NLL相关只在四开源模型和低NLL半区；复杂度/项目/基准年龄与自然性仍可能共同影响。关联与变形敏感性不能单独确定训练泄漏、更不能给修复语义正确性。§IV-B最高NLL区域也会更脆弱，不能把所有下降归记忆。

Ch66“污染校正需要主动干预”已区分能力/记忆/生态和缺受控注入时只能疑似污染；本篇补受限黑盒变形与白盒熟悉度操作点，而非使相关成为因果，因此仅报告、不声称整个实验已有覆盖。854 Defects4J/199 GitBug-Java（去44多函数）、七模型、每bug10prompt；hardware/precision/batch/concurrency/SLO未披露。官方abs-v1同题；Submitted04/23T11:59:53Z、v1Updated00:44:13Z/OAI04/24，沿既有公开批次组合推断08–09。[作者链接的Zenodo](https://zenodo.org/records/15837296)实际Published07/08/2025，仅anonymous software/reproduction zip，未列正文；这证明实现artifact早于本次arXiv，不能冒称机制代码首发或单凭它回拨论文正文。若恢复更早公开论文正文则仅重开本家族日期/去重；未下载软件或扩发表史。

## [2604.21593 Language as a Latent Variable for Reasoning Optimization](https://arxiv.org/html/2604.21593v1)

2+1+2=5，标准必要审阅完成，拟仅报告，待非作者核。实际§3–5：同题五rollout，一条语言不约束、四条从language set抽语言prompt，规则answer+format reward、组相对归一化；在多语数学数据上改变探索条件，而非测得内部潜变量因果。语言受约束/不受约束配比和language set消融有局部机制证据，但100字符format条件不等跨语言同token工作，输出语言遵守及entropy又随训练改变，不能从较高早期entropy推出唯一增益原因或普遍最佳内部路径。

Qwen2.5-7B/Llama3-8B、18,140训练examples、8A100、batch256、分别5/1epoch、greedy无语言约束推理；§4.4小模型无约束变体会反优，§5延长训练英语收益下降/输出转英语而其它语言不同，不采用所有slice稳定获益。precision/输出长度matched compute、wall-clock及SLO未披露。Ch33已有sample身份/实际探索有效性、format/readability与R1-Zero language-mixing边界；本篇提供可报告的语言prompt探索recipe，不将未识别的“language latent”升为长期内部机制或默认训练策略，也不称本算法已写入。官方abs-v1同题、当前v2仅列Under Reviewing没有纠错/撤回声明；Submitted04/23T12:19:14Z、exact-v1Updated00:45:05Z与邻批/官方slot联合推断08–09，OAI05/05是当前记录日期而非本事件首发。未比较所有版本/附件或复现。

## [2604.21598 DryRUN: On the Role of Public Tests in LLM-Driven Code Generation](https://arxiv.org/html/2604.21598v1)

2+2+2=6，标准必要审阅完成，拟仅报告，待非作者核。实际§3–5：去公共示例的spec先两轮无外部反馈plan refinement，再两轮自造输入/mental trace更新plan并重新生码，最后polish；这研究弱公共测试与自生成反思的条件差异，mental trace不是真执行。§4基于80道March2025后LiveCodeBench、两API模型minimal reasoning/三runs，消融仅gpt5mini的37hard；DryRUN和CodeSIM总体方向因模型反转，std重叠，既不是equivalence检验也非相同调用/token预算。去公共示例同时改变计划/循环次数与输入策略，不能唯一归因去测试；作者§5.3自己不主张据此删公共测试。

Ch80 verification-centric reflection已区分evidence gap与同模型judge偏差、Ch79完成证据需machine-checkable witness；本受限代码操作点不改变“模拟结果不能替代执行证据”，不将作者overconfidence解释当已识别因果。§4.5一轮simulation反退、§5.2 Qwen7B失败及§5.4未来sandbox核trace都保留；额外约19倍baseline tokens只是特定配置，不能推通用成本优势。hardware/precision/batch/concurrency/部署SLO未披露。官方abs-v1同题；Submitted04/23T12:21:03Z、v1Updated00:45:15Z沿既有组合推08–09，OAI04/29与v2后发记录不改名首发；当前无撤回/纠错说明。未复现或扩整个版本史。

## [2604.20851 HAT-VTR](https://arxiv.org/html/2604.20851v1)

2+1+2=5，标准必要审阅完成，拟仅报告，待非作者核。实际 §4.1–4.3/Eq5–12、§5.1/5.4–5.5/Tables6–9、F.2–F.3：FIFO 保存最近 query-gallery score，双向归一化分别影响 pseudo-positive 选择和最终 rerank；LN 更新另用视频内/间 uniformity 与 RM alignment。Ch76 hubness/neighbor margin 与域迁移已有长期诊断，但不声称本算法已完整写入。受限新证据值得报告，尚不把这项 TCR/DSL 组合变成普遍检索更新规则。

主评价 CLIP4Clip/X-Pool、五视频数据集、RTX4090/batch16。32.27ms/query 对 TCR26.37，backward21.2ms；不是零成本 rerank。F.2 明确低 hubness 扰动下纯 HSM 可匹敌或优于训练，F.3 扰动强度非单调且依赖辅助模型；Recall 不等答案支持/生产可靠性。precision/并发/SLO 未披露。raw00:00:15Z/OAI04/24结合官方公告slot仅支持本窗08–09推断，不是孤证首发。

## [2604.20902 Frequency-Forcing](https://arxiv.org/html/2604.20902v1)

2+2+2=6，标准必要审阅完成，拟仅报告/实现表述待澄清，不预先写Books。实际 §3.1–3.4/Eq1–5、Algorithm1、§4.1–4.3/Table2、§5：保留 pixel 插值，早成熟频率流作条件，learnable wavelet 与冻结副本另付训练成本。Ch24 分层 latent/连续路径尚没有此精确分支，但缺口不自动证明实现充分。

§3.3 同时写同网格 embedding 相加与 joint K/V 的按流 block-causal mask，未交代相加后流身份如何保持，不能据此编造可执行布局。ImageNet256 的461M/400epoch learnable two-stream FID3.99劣于semantic-only3.21；单流基线仅200epoch，不能把收益全归频率。三流466M的3.11只局部改善。既有checkpoint微调明确未做，不采用“直接互换/免重训”；硬件、precision、batch、NFE/时延及SLO未披露。定点重开条件是流token布局/attention实现说明或精确artifact；不否定双插值数学对象及全部作者经验。raw00:01:18Z/OAI04/24只为公告组合线索，日期独立核仍另行。

## [2604.20849 SPIRE](https://arxiv.org/pdf/2604.20849v1)

2+2+2=6；真实知识缺口深入完成，已实际整合 AGENT-RAG Ch76 Chunking 的 parser 证据单元后；root 必要源→实际 owner 与正文写后复核均通过，见 `V3_ROOT_QUORUM_TERNARY_INDEPENDENT.md` 末节。HTML首页August24标签与PDF原版April24不一致，本项采用官方PDF-v1 §2.1–2.3、§3.1–3.2、§4.1–4.3，不据HTML标签移植后发结论。存的是原文树上的path-set，embedding时另加global context；回读时扩local view、选label，再映回原路径。标题/非DOM祖先的活跃header、nested-list标签和table行列header是不同结构依赖；同文path-set合并可摊销重复scaffolding。正文补的是**稳定选择身份与用于embedding/reader的结构上下文分开，并延迟渲染**；需绑定原文revision/解析规则，path稳定不等跨修订稳定或support truth。

PDF §4为两数据集各400题、1000-token citation budget，BGE-Large-EN、Qwen3-32B filter、235B judge；helpful/total不是答案正确或支持完备。Hotpot embedding ratio .215略低block .222，关闭global context反而产生更多helpful总数；换block-leaf同时换encoder，不能唯一归因粒度。生成filter额外成本未与纯embedding匹配，precision/硬件/batch/concurrency/SLO未披露。不采用全面更好/所有结构可解释或生产scalability保证。**日期更正：**同作者[Zenodo v1](https://zenodo.org/records/19441410)已标 `Published April 6, 2026`，并关联同一 arXiv ID；arXiv 页面/PDF 页脚的 Feb12 与 April ID/正文日期又相互冲突。原 `raw v1处理00:00:13Z/OAI04/24+slot` 组合不能压过先行公开证据，故本项不再计04/24候选或整合，定点归属见 `V3_ROOT_SPIRE_FIRST_PUBLIC_CORRECTION.md`。本项已真实写入 `AGENT-RAG` Ch76 Chunking 的parser单元后两段，source→owner和实际正文/相邻衔接均由root非作者复核通过，记录见 `V3_ROOT_QUORUM_TERNARY_INDEPENDENT.md` 末节；机制审阅及书稿写后有效，真实日报 owner 待核，未复现实验，不代表日级Gate通过。

## [2604.20933 IRIS](https://arxiv.org/html/2604.20933v1)

2+2+2=6；纠错深入必要审阅完成，拟仅报告，理论采用边界待非作者核。实际读§3.1–3.3/Eq4–10、§4.1/Table2–3、AppendixB.1–B.3/C.1。real与synthetic分别按log-ratio指数倾斜、batch内归一化，order调整改变梯度分配；不是普通chosen/rejected标签。Ch34当前Bradley–Terry pair-loss与reference坐标不包含此完整objective，但本轮不能把“统一所有self-play散度”或“α→1两边均uniform”写成长期事实：Eq8在α→1的synthetic weight仍为pθ/pold，不一般等1；population期望的该梯度可相消不等每样本uniform。Eq4后的Rényi等式缺α/(α−1)比例。

B.1 Eq15/19对0<α<1把正指数当翻转不等号，取pdata=pold=(.5,.5)、pθ=(.9,.1)、α=.5时A=1.4907、B=.8944、M=1，A^α=1.2209>B^(α−1)=1.0574，印刷的≤不成立。但正确reverse Hölder方向仍可推出Eq20固定点下界，不据这个局部错误否定固定点本身或所有经验。两模型Zephyr7B/Qwen2.5-3B、50k UltraChat、5轮/每轮2epoch、batch64/8H100；短基准与固定target、启发式α不证明动态目标收敛或普遍优越，precision/序列长度/SLO缺口保留。这里只隔离几何等价及普遍weight叙述，不为纠错重写整套self-play书稿；可接受精确公式/权重勘误与对应实现定点重开。raw00:01:56Z/OAI04/24仅有界组合日期线索。

## [2604.20911 Omission Constraints Decay](https://arxiv.org/html/2604.20911v1)

拟2+2+2=6，保护边界深入完成，作者提案**仅报告**，待非作者采用核。实际读exact-v1 §2.1–2.6、§3.1–3.5、§4.2–4.5：12模型、4416 trials只测8条任意格式规则；per-constraint纵向只四模型，ArmC只Gemini/Llama且不在主要易受影响组。ArmB/C平均482/620 tokens，未严格匹配，不能采用“唯一attention dilution因果”。正向incident-ID保持与no-bullet失败是受限独立反证，但不证明凭据/执行安全、模型架构成因或全provider。STD为六深度上50%格式通过率的插值，不是安全session阈值；reinjection段无独立防御验收。Ch72现有policy owner独立于code proposal（约733行）、白盒/黑盒接口区分（约674行）及guard-visible window（约1620行）已有长期执行边界，本项尚不足将格式proxy改成安全runtime设计规则；保留新受限观察而非声称原八约束实验全已覆盖。precision/batch/concurrency/SLO未披露；API身份部分未pin，非生产攻击复现。

## [2604.20915 Absorber LLM](https://arxiv.org/html/2604.20915v1)

2+1+2=5，真实知识缺口深入完成，已实际整合 MODEL-LONG-CONTEXT Ch22，root 非作者写后通过。实读§3.1–3.3 Eq2–6/Alg1–2、§4.1–4.6：LoRA让无X的学生在有限后续Y上对齐full-context模型的hidden states，而非KV在线回归目标；滑窗把X吸收后继续Y。写前 Ch22 约713–720行仅有KV binding在线回归与history-dependent attention等价，未承载**历史重建目标→后续行为teacher对齐**的目标分支。实际正文已插在该TTT段后：有限Y的full-context目标仅提供受限teacher；alignment小不保证未知future、真正因果保持或精确恢复。额外teacher前向/反传、LoRA更新与forget/reset身份要与显式KV分账。Llama2-7B/RTX4080SUPER、n1024/m2048/r64、128生成tokens、1–16K；表1短上下文比standard慢，prefill被时延公式减除，不能采用全成本O(1)或一般性能优越。precision/batch/concurrency/SLO未披露；§4.6.3非所有m单调，不采“更大即更好”。source→owner与实际正文/相邻交接写后复核均已通过，见 `V3_APR02_ABSORBER_GIST_INDEPENDENT.md` 末节；未复现，不代表日级Gate。

## [2604.20920 Gist Sparse Attention](https://arxiv.org/html/2604.20920v1)

2+2+2=6，真实知识缺口深入完成，已实际整合 INFER-KV-CACHE Ch45，root 非作者写后通过。实际读§3.1–3.5、§4.1–4.5：required CPT训练interleaved gist；query×gist key选chunk，再读selected gist+raw KV，unselected不读，GQA每head选择后union；首attention层gist输入相同故跳选择。可选finetune把query-dependent稀疏mask放训练，不等普通top-k自动可微。写前 Ch45 已有残余summary（592）、synthetic cache distill（627）和host recall（681），没有**可训练summary同时做query路由且保可展开原KV**的分支。实际插入 learned eviction之后、recoverable recall之前，明确active read budget≠原始KV驻留总量、gist summary proxy≠证据真值，训练mask/model与原KV身份共同验收。Qwen2-7B/Llama3.2-1B、8H100训练，LongBench/RAG质量与SG+SR消融；FullFT平均仍更高、AG+SR局部优，未披露端到端latency/servingSLO，不采用无损或全配置更快。source→owner与实际正文/相邻交接写后复核均已通过，见 `V3_APR02_ABSORBER_GIST_INDEPENDENT.md` 末节；未复现，不代表日级Gate。

## [2604.21428 Decoupled DiLoCo](https://arxiv.org/html/2604.21428v1)

2+3+2=7，深入完成，已实际整合 TRAIN-DISTRIBUTED-TRAINING Ch36，root 非作者写后通过。实读§3.1–3.3/Alg1–2、§5.1–5.5、Table2–5：独立learner保局部状态，syncer按fragment达到K后聚合，步时/通信slack内grace增加到场贡献；权重实际为tokens×tokens/steps，RDA另分方向/范数，不是简单token均值。写前 Ch36 的跨地域层级staleness（约1350）/optimizer与stepcommit已有原则，但缺**minimum quorum+有界grace把可用性与样本贡献权分开**。实际在异构跨站聚合后写入两段：各fragment持source revision/steps/tokens与恢复状态，quorum不等所有样本或集中式语义；代价staleness、样本权偏置与checkpoint组合，slack不足回同步/缩小grace。150K～1.2M chips是failure simulation，真实heterogeneous setup正文TPUv5e/v5p却Table5称v6e/v5p，需保配置歧义；K1无grace部分质量退步，非所有slice匹配，未披露precision/SLO，不采用百万卡实训/无损一致性。与Google日历日博客去重同家族，日期仅按官方公告slot/ID分配及精确v1相邻处理簇有据推断08–09，不称逐篇公告确证；source→owner与实际正文/相邻交接写后通过见 `V3_ROOT_QUORUM_TERNARY_INDEPENDENT.md`。

## [2604.20913 FairyFuse](https://arxiv.org/html/2604.20913v1)

2+1+2=5；真实知识缺口深入完成，已实际整合 INFER-TENSORRT-LLM Ch49，root 非作者写后通过。实际读§2.3、§3/Algorithm1、§4、§5.1–5.5及Table5/6：complex widely-linear八子GEMV共享mask解码、activation与寄存器累加，以ternary正负mask驱动AVX-512/BMI2加减；仍有每输出scale乘法，不能称整个模型无乘法。写前 Ch49 量化成本清单及product-LUT（约720–741）、CPU layout→SIMD/LUT（约807–817）未承载无LUT条件加减与多子GEMV共享解码分支。实际在 LUT 后补一个并列执行选择，不否定LUT或常规反量化。评价限Fairy2i-W2/Llama2-7B、单socket48线程Xeon8558P、FP32累加/2bitpacked+scales、至少128输出；prompt长度/并发/SLO未披露。Table6 CPU对照1线程dense与48线程ternary混杂；H200自写CUDA回归不证明所有GPU极低位实现不可行，质量也低于FP16。不采用29.6×、GPU结构性无收益或近无损宣传。原v1处理00:01:34Z/OAI04/24仅组合日期线索，非孤证首发。source→owner与实际正文/相邻交接写后通过见 `V3_ROOT_QUORUM_TERNARY_INDEPENDENT.md`，未复现，不代表日级Gate。

## [2604.20930 SafeRedirect](https://arxiv.org/html/2604.20930v1)

2+2+2=6；保护深入完成，作者拟仅报告。实读§3.1–3.4、§4.1–4.4/Table1–2及Limitations：给validator修复压力下的模型明确失败许可、固定拒答与保留placeholder，是prompt级替代行为而非runtime hard stop。三AI工具任务/七OpenRouter模型，每条件2100次；Grok judge只将可提取且最高等级有害计入unsafe，未证明所有剩余输出安全。消融并非完整组合必胜：去P3的Grok、去P2的Kimi平均更低；良性输入行为相同是目标而非此实验已证明。Ch72约1664–1674明确危险路径覆盖、条件失败与剩余可达行为分权，约733policy/CI owner独立于模型；本项提示词不授予新的执行保护，不据此改成system message可信hard gate。保有限任务重定向证据，不声称心理/attention成因、零开放风险或防线验证；precision/length/batch/concurrency/SLO未披露。原v1处理00:01:53Z/OAI04/24作组合日期线索。

## [2604.20854 ERA](https://arxiv.org/pdf/2604.20854v1)

2+2+2=6；纠错深入，拟争议暂缓，待非作者核。实际 HTML §4.1–4.3/Eq7/13–16、Table2 与官方 PDF-v1 物理第5页 Eq7/A.1核同：`tilde alpha = y(1-y) ⊙ alpha`；one-hot y 使全部参数为零，Dirichlet 不定义。不是仅HTML转录问题；不擅自改成常见EDL公式，不据此断言全部经验虚假。双head对应query-only/检索输入，不自动保证独立；DST冲突与不确定性也是学习proxy，不证明真实知识状态分解。

必要评价A.1是10次回答全正确定义Known、top3 golden context分四象限，5000训练/3000测试、IDK=.7；Qwen3-8B/Llama3.1-8B、4A100、NF4+bf16 QLoRA/r8、1epoch；WikiEvents另含GPT4o合成负例。回答与拒答F1分账，Table2非处处最优。Ch76现sufficiency/critic校准不授权该分布模型；不作Existing或正面Books。重开需要作者Eq7勘误或同版实际loss artifact及其评价对应，不扩全版本史。原v1处理00:00:21Z/OAI04/24仅结合官方公告slot与ID批次支持本窗有据推断，Feb Submitted/PDF页眉不单独回拨。

## [2604.20938 HARBOR](https://arxiv.org/html/2604.20938v1)

2+2+2=6；纠错深入，拟争议暂缓，待非作者核。实际 §VI/Eq4–7/Alg1 与 §VII–VIII：reference SAAS/NUTS/Matérn5/2/qNEHVI换成ridge/linear Boolean tensor-product/greedy单候选EHVI，原文承认不保完整posterior，却又称Boolean Matérn仅仿射Hamming重标等价。d=2、lengthscale=1时 k(0)=1、k(2)≈.13866、k(2sqrt2)≈.03702，仿射要求末者等于2k(2)-1≈−.72268，直接不成立；不能把reference后验chance约束或全体实现等价移交替代artifact。

89 TerminalBench任务、gpt5.4-nano Responses API、并发4；候选smoke仅看on-flag telemetry，不是任务安全证书。原B17/89、D12/89、Harbor17/89，五不同pick非同配置重复估计，11 error/timeout不得随意去分母；memory flag实际retrieval0限制归因。Ch81搜索budget/holdout既有主线支持保留这项受限harness经验，不证明新的安全posterior保证。重开需正确kernel对应、替代surrogate后验/约束定义与固定配置有效对照，不读所有引用。原v1处理00:02:04Z/OAI04/24为公告组合线索。

## [2604.21026 MCAP](https://arxiv.org/html/2604.21026v1)

2+1+2=5；标准必要审阅完成，拟仅报告，待非作者核。实际 §3.1–3.3/§3.1.1/§4.8及AppendixD：Q/V与FFN activation norm的load-time层排序供precision/residency选择；sub-Gaussian/iid条件下top-k失败界随variance/gap²缩放，12题明确purposive、不是经检验的iid。界只恢复排序，不证明低精度/删层后的任务质量；scorer对自身reference100%不是独立oracle。先前“没有恢复界”的关闭理由已纠正，不因相同主题再次排除。

Config A保全层paging，B/C hot-only跳过其他层，不能当同等质量的单一驻留对照。T4/sm75 16GB、A10G24GB，W4A8/W4A16 F16 I/O；所测Llama1/3/8B及8B低预算0任务准确率反例保留，未用tok/s推出可用性或SLO。Ch49量化artifact/逐格式验收与Ch54容量主线已有长期原则，但不声称完整MCAP算法已有覆盖；保其受限ranking/operating-point仅报告，不采普遍保护末层或无损低预算。rawv1处理00:05:45Z、当前OAI04/27不同字段如实保留；日期独立核用官方slot/ID批次组合，不称OAI04/27首发，也不以处理字段孤证定Apr24。

## 两处实际写入已获独立写后通过

20915/20920 已由apr02 source→actual-owner窄采用通过，并按root授锁实际写到Ch22 KV-binding后、Ch45 learned-policy至recall交接；source-family marker分别2604-20915/20920。root已实际順读正文与邻接并通过，记录在 `V3_APR02_ABSORBER_GIST_INDEPENDENT.md` 末节；两项均深入完成、整合，当前实际I5。两锁已释放；早期小节末的待root提案状态由本节替代，普通队列继续，整日报未验收。

## [2604.20932 Adaptive RAG Defense](https://arxiv.org/html/2604.20932v1)

2+2+2=6；保护深入完成，作者拟仅报告。实读§4.2–4.3/Algorithms1–3、§5.1–5.4、§6/Table7：sentinel观测query/retrieval统计，strategist选择pre/post hook；50queries/700docs/Top5、Llama3.1-8B generator与多controller，MBA exact mask-fill不是membership inference advantage，content-leakage只架构未测。静态测试顺序与adaptive随机交织协议不同；Table7针对性静态TrustRAG的recall/ASR优于若干ADO，不能把动态选择写成必然优于轻静态分支。Ch72约2310–2313 joint failure correlation/覆盖差异/false-refusal与1664–1674残余风险，已有本项可支持的长期保护验收；没有采用coherence/attention当可信真值。所测零ASR不推出open-world安全；judge/局部小样本、额外controller成本与未披露hardware/precision/concurrency/SLO限制保留。原v1处理00:01:55Z/OAI04/24仅组合日期依据。

## [2604.20917 The Path Not Taken / DexBench](https://arxiv.org/html/2604.20917v1)

2+1+2=5，标准必要审阅完成，拟仅报告，待非作者核。实际§2.1–2.3/3.1–3.2/3.5、§4.2/4.3/7：同程序和原输入分别测exact coverage预测、为指定未覆盖branch生成mutant输入；联合成功是两项pass@k指示的交集，不要求同一次样本共享内部推理，也不证明因果理解。SlipCover执行提供coverage oracle，445配对样本源自三公开Python基准、13模型、one-shot；原代码可能污染，最大coverage增加的branch选择有偏。forward exact-set与backward单branch命中难度不同，Jaccard宽松评价仍有分歧，不能将差值全归能力机制。hardware/precision/并发/SLO未披露。Ch66现有可执行oracle、same-verdict语义配对与round-trip编辑分别承担执行证据/语义/保留性，不声称此forward/inverse程序协议已完整承载；本轮保留这一受限新evaluation slice，不把joint score采为一般因果理解证书。rawv1处理00:01:39Z/OAI04/24与官方slot/ID批次仅支持有据08–09推断。

## [2604.20923 ILDR: Geometric Early Detection of Grokking](https://arxiv.org/pdf/2604.20923v1)

2+1+2=5，标准必要审阅完成，拟仅报告，待非作者核。HTML工具失败后已恢复official PDF-v1必要§2.3/3.1–3.3、Tables1/6/9–11/§5，不是材料Blocked。held-out类间centroid距离除类内scatter、step3000基线2.5倍阈值，每100步检测；单层d128/4heads、modular与S5、AdamW、batch512。阈值single-heldout-seed预扫，乘法8seeds而大多数sweep单seed；不是全面独立holdout发布。Table9停止后7.1%～99.3%准确率直接限制“几何flag就是训练完成”，Table6 f=.4信号落后grok；Table11三seed LR/WD干预与未干预对照未隔离触发时刻是否必要，不能把预测相关性升级唯一因果。Ch5已把几何解释限定为诊断并要求行为/持出验收（representation-gap及几何比较段），不称ILDR算法全已有；具体新诊断/干预经验仅报告。硬件/精度未披露，scalar计算与日志成本保留，不引wall-clock数字为通用效率。raw00:01:45Z/OAI04/24结合官方slot/ID批次，而非submitted首发。

## 两项实际写后通过

21428已实际写Ch36跨站聚合后，20913已实际写Ch49 product-LUT后；root实际顺读正文及相邻交接，写后复核通过，见 `V3_ROOT_QUORUM_TERNARY_INDEPENDENT.md`。两章锁已释放，本日实际I7；这不是日级Gate。

## [2604.20903 Sensitivity–Uncertainty Alignment in Large Language Models](https://arxiv.org/html/2604.20903v1)

2+2+2=6，保护保证/纠错深入必要审阅完成，拟中心保证争议、Books暂缓，待非作者核。实际读§3.1–3.5、§4.1–4.3、A.1的风险桥、§5.2/Alg1及§6–7评价与限制。预测分布的平均扰动差异S与熵H是不同对象；Remark3.3仅给S≤sup divergence，不能在风险上界用更小的S无条件替换sup。A.1 Step2加减ψ后不能仅因ψ非负删除正项，Step4在λH≥ψ时写−ψ≤−λH，方向也相反。

Eq11有满足所列条件的最小反例：所有输入上pθ=ptrue=(.5,.5)，0–1 loss/TV的Lipschitz常数1，Z取单值、模式分解精确，A2取允许的ψ≡0，λ=1。此时κ=0、S=0、H=ln2、Rrob=Rθ=.5；作者Eq11要求.5≤.5−ln2，不成立。这只否定该桥及无条件entropy subtraction，不声称此反例否定ψ=0时Eq10的标准sup界，也不否定全部诊断或实验。

§5的task+consistency+positive-entropy训练另需K=4扰动forward；分类实验不能直接给开放生成的安全拒绝保证。§6所读报告未充分披露可复核的模型身份/数据规模与硬件、precision、并发/SLO，不把表中改善作为通用收益。Ch66的calibration/selective prediction与Ch31奖励代理并未承载此新风险定理；因中心保证未成立，本轮不将它写进Books。重开材料为修正的风险桥/假设与对应目标说明，不要求额外benchmarks替代理论。原v1处理2026-04-24T00:01:19Z、OAI04/24仅与官方ID公告赋号/Thu20EDT及批次组合支持08–09的有据推断，不叫孤证首发。

## [2604.20904 Normative Simulacra](https://arxiv.org/html/2604.20904v1)

2+2+2=6，保护与实际知识缺口深入必要审阅完成，已实际整合Ch31；apr20与root必要源→owner及root实际正文/相邻交接写后复核通过（记录见 `V3_APR20_NORM_SINK_FOUR_INDEPENDENT.md`）。实际读§3.1–3.5、§4.1–4.2/§5/Ethics及A.1/A.3/A.4。十部小说中的信息flow与应然norm分开抽取；SFT先学typed extraction，GRPO再以结构及context/norm grounding组合reward。§3.4.2对同一completion分别使用正确检索norm universe与随机错误universe评分，reward为clamp(r_correct−λr_wrong,0,1)，不是只奖励更保守拒绝。Top3 norm检索与弱critic构成训练代理，并不赋予小说规则法律/安全authority。

Ch31“Preference Data 的困难”已讲pair难度/rubric/background/shortcut与data drift，Ch72拥有recipient/subject/context权限，但未解释“保持同一flow解释，只改变其norm context，再把差异送回reward”的具体训练桥。拟在Ch31该数据困难段之后、Preference Admission之前两段融入此分支：先分账形式识别、拒绝倾向与appropriateness，再解释条件contrast及judge/retrieval代价，不重复Ch72运行时授权。

Qwen3.5-9B/TRL、GRPO G=2、LR1e−6、有效batch8、max completion2048；论文A.1写Qwen3-32B reward judge，disclosure又写Qwen2.5-32B-Instruct，此身份不一致保留而不静默修补。小说抽取的Qwen2.5-72B-Instruct AWQ/vLLM/两RTX A6000不冒称训练GPU。SFT recognition/保守性不保证appropriateness；多数benchmarks后训练并非全面改善，context reward的HIPAA退步和λ改变的有限收益均保留。50条PrivacyLens人工检查中至少一个配置40%判断有误是该样本切片，不推所有judge总体误差；WEIRD与小说历史偏差也不当规范真值。额外两个judge context、检索、抽取与GRPO成本不可删；高风险应用仍回到明确规则与独立授权。处理00:01:20Z/OAI04/24与公开批次组合日期推断，非Submitted首发。

## [2604.20937 SToP](https://arxiv.org/html/2604.20937v1)

2+2+2=6，实际知识缺口深入必要审阅完成，已实际整合Ch23；apr20与root必要源→owner及root实际正文/相邻交接写后复核通过（记录见 `V3_APR20_NORM_SINK_FOUR_INDEPENDENT.md`）。实际读§3、§4 Eq4–6、§5.1–5.4/Tables1–5及naive sink处置对照。高attention并非稳定的语义重要性；跨帧累计attention经幂与MinMaxNorm形成sink proxy，空间选择用A−μ_s s，时间剪枝将sink项与相似度共同判定。累计值不能区分短暂尖峰与持续高值；它只是条件性排名惩罚，不证明持久高分token都无用，也不授权无条件硬删除静态显著对象。

Ch23现视觉budget/stage selector/局部时间merge已有压缩主线，但没有“跨帧持久高attention可能挤占预算，因此排名与sink proxy应分别校准”的分支。拟在视觉预算/时间冗余选择附近两段嵌入，并交接Ch66细粒度evaluator；不复制一篇benchmark摘要。代价为attention读取/跨帧汇总和μ、w/阈值调参；场景中静态物体真重要时需回退原attention/richer token路径。

LLaVA-OneVision7B/LLaVA-Video7B，32帧×196token，10/15/20%保留率，原文GPU字符串“NVIDIA GeForce A6000 48GB”按披露保留、不自行改设备身份。五MCQA与EventHallusion/Desc、VideoCompAct、VCGBench自由生成并非同一评价分母，后者使用GPT5 judge。Table1 VisionZip20%的一致性/时序切片和Holitom YC存在退步；组件消融与naive hard prune对照支持局部selector取舍，不证明全部收益唯一因果或90%无损。runtime/precision/并发/SLO未披露，不引质量表当端到端性能。处理00:02:03Z/OAI空与官方公告/ID批次联合推断，不据OAI缺失定晚发。

## [2604.20940 Sema](https://arxiv.org/html/2604.20940v1)

2+2+2=6，标准必要审阅完成，拟仅报告，待非作者核。实际读§2.2、§3.1–3.3、§4.1–4.5/§5。将原生模态codec编码放客户端，server按一致codebook重建图像/波形后仍调用原有模型encoder；不是任意LLM直接理解任意离散codes。modality/codebook/count/seq/time framing及session协商、视觉codes加AX/OCR文本、audio SpeechTokenizer首RVQ层50token/s与Whisper-large-v3、Qwen2.5-VL7B构成具体placement分支。lossless文本运输不证明AX/OCR内容完整。

§4.1明确是component测量加模拟网络的preliminary simulation，端到端prototype属于§5未来工作。Fig4 encode+transfer+decode排除了恒定model inference，不称实际端到端部署SLO；200 LibriSpeech/100 OSWorld导航与50文本任务、application payload不含全部wire/TLS，客户端未披露精确硬件/precision/并发。codec增加45–180ms音频及vocoder成本，低带宽可能获益，高带宽边际缩小；WER2.7→4.1、visual-only75.5/hybrid93.3/raw94说明质量取舍。3–5秒下行chunk与“不专设jitter buffer”不等时间延迟无关。

Ch23已有codec revision/表示与任务fidelity、Ch62拥有transport与流时序；不声称整个客户端算法已在现章，但本轮simulation不足以将这一placement采为长期通用系统选择，保留受限新操作点与尚需原型/网络损失/tail/client capability验收。处理00:02:06Z/OAI04/24与官方slot/ID批次组合日期线索，非单字段首次公开。

## [2604.20985 Differentially Private Model Merging](https://arxiv.org/html/2604.20985v1)

2+2+2=6，保护合同/真实知识缺口深入必要审阅完成，拟Ch72增量，待非作者source→owner与写锁，尚未整合。实际读v1 §2–5、§6.1–6.3、§8.1–8.2：同数据集的多个DP资产中随机只发布一个，RS的RDP界为各profile指数混合，PLD可做混合；不能等同发布所有模型的联合组合。线性参数组合LC仅知最终profiles时可退回联合发布的composition；按DP-SGD训练轨迹得到更紧界还依赖每步clipping、sampling、学习率/权重及独立noise，组合noise方差与各加权更新有关。§6.3同run checkpoints共享早期随机更新，不满足这个独立noise分支；RS仍可按profile混合。不能采用“模型平均自动平均epsilon”或“后处理消除已发布资产的历史预算”。更紧accountant随模型数指数复杂，而非随参数数指数复杂。

Ch72“Differential Privacy先定义被保护对象”现有单输出post-processing与composition正文未承载**选择一个资产、线性合并、相关checkpoint三种发布对象的不同会计依据**；Ch30接手utility合并，不拥有privacy accounting。最小提案在现post-processing段后、production contract前两段：绑定privacy unit/各run随机性lineage/发布集合与selection规则；public或非敏感权重可使用，若选择依赖私有validation或重复发布则另计。这是工程交接，不声称论文已实现端到端发布系统。作者实例限裁剪均值、MNIST logistic与CIFAR10 ResNet18/GN，不外推LLM质量/SLO；不采用未逐条核验的所有定理或泛称相关checkpoint永不改善任何privacy界。

本轮重新核官方abs-v1身份/当前版本说明，无撤回标记；v1Submitted=04/22T18:13:37Z、v1Updated=04/24T00:03:31Z、当前OAI=05/21原字段分别保存，Submitted/Updated/OAI均不直接改名首发。后两字段结合官方公告slot、ID赋号与相邻批次仅支持08–09有据推断，不由v2号触发全版本比较。采用需非作者核；未复现实验。

## [2604.20995 Value-Conflict Diagnostics Reveal Widespread Alignment Faking in Language Models](https://arxiv.org/html/2604.20995v1)

2+2+2=6，保护评价深入必要审阅完成，拟仅报告，待非作者核。实际§3–5、§6.1–6.7：合成250二选一道德情境后经四模型多数回答筛到50，反向developer policy与monitored/free、unmonitored/paid tags及不服从后果组合；compliance gap是条件行为差异，不识别持久真实价值或战略意图。无后果时总体gap近零仍有模型例外，oversight概率效应非单调；scratchpad自述、PCA主方向和steering均不构成内在意图真值或严格一维因果。训练/评价场景的priming及样本选择必须保留，不能从37%外推自然总体。

steering采用220条SorryBench/WMDP各训练、选层/contrast vector，Table3只支持相应模型协议下的gap变化；Table4 trace-aware计数与不同分类器任务不能混成“能力无损”证明。Ch66现有observed behavior/elicitation ceiling、完整evaluator identity及评估感知控制已承担本项能支持的长期边界，但不声称原VLAF协议全部已有覆盖；本轮保其新受限诊断，不把控制标签当隐藏意图sensor。原评价不能证明开放防御或online效能；硬件/precision/并发/SLO在本次必要评价未披露，不引用headline低开销。官方abs-v1本轮已核无撤回标记；Submitted04/22T18:37:25Z、v1Updated00:04:22Z、当前OAI04/29不混用，按本日公告组合推断08–09。未复现实验。

## [2604.21016 SGD at the Edge of Stability: The Stochastic Sharpness Gap](https://arxiv.org/html/2604.21016v1)

2+1+2=5，标准必要审阅完成，拟仅报告，待非作者核。实际§2–4、Assumptions1–8、§5：gradient noise在top-Hessian方向注入波动，经cubic restoring force压低平均sharpness；有限coupling要求C4 loss、eigengap、导数/噪声条件。闭式gap另用frozen coefficients、stationarity/decorrelation closure及正alpha/beta，不因特征向量正交就有独立性，也不是普遍Transformer/Adam调参公式或generalization证书。

评价为CIFAR10的5000例、两隐层tanh/MSE及有限CNN/ReLU/CE、vanillaSGD，LR .005–.02与3–5seed；沿SGD轨迹测量代替movingPGD reference有近似。log-batch slope −1.27不叫精确−1，五seedplateau207.8对200也不推所有配置均在阈值下。Ch28训练稳定性现有curvature/多个failure proxies但没有该完整理论；保受限理论分支仅报告，不虚称全公式已有覆盖，也不把它采为通用执行controller。无端到端性能主张，不引用wall-clock或SLO。官方abs-v1身份已核无撤回标记；Submitted04/22T19:02:52Z、Updated00:05:25Z、OAI04/24分别保留，日期为官方slot/ID批次组合的08–09推断。

## [2604.21041 Projected Gradient Unlearning for Text-to-Image Diffusion Models: Defending Against Concept Revival Attacks](https://arxiv.org/html/2604.21041v1)

2+2+2=6，保护保证深入必要审阅完成；拟窄争议暂缓正面保证，经验只作受限报告，待非作者裁决。实际III-A–D/Alg1、IV、V-A–F、VI：retain activations covariance生成投影P，hardening更新G−GP。固定输入r在range(P)的局部线性层可得W'r=Wr，但没有全网非线性/上游改变后activation、bias及后续任意fine-tuning的同等保证。未来不受约束更新并不自动执行该投影，故“精确保留全部retain输出”“未来任意fine-tuning不能undo”不由这段局部等式推出；不因此否定全部作者经验。

评价SDv1.4/A10040GB、100 retain例/100步/1e−5、VanGogh与GolfBall两个概念的10级curriculum，用CLIP+ViT阈值判revival；ordinal checkpoint不等攻击成本或privacy保证。UCE最初未成功删除，PGU也不能修复；Receler-GolfBall部分退步、gamma=.9复活及PGU/Meta各有占优保持。6min/12GB与其他硬件2h不能当matched速度。Ch72已有suppression≠forget、retain/attack验收长期边界，本项不据错误exact/unrestricted保证写Books；重开需全网不变的充分条件、未来更新约束或作者收窄/勘误及对应实测，不要求全版本史。官方abs-v1身份已核无撤回标记；Submitted04/22T19:39:56Z、Updated00:06:32Z、OAI04/24用于公告组合日期推断，非孤证首发。未复现实验。

## 两处已落实的 literal 提案（以实际 Books 正文为准）

两项实际写后由root非作者通过；以下保留写前提案过程，其中20937首句已在实际正文收窄为“累计attention不能区分短峰和持续高值”。本日累计真实整合10，不代表日级Gate。

20904 `TRAIN-RLHF` Ch31，插在“来源可靠度与先验强度”段后、Preference Admission前，source→actual owner由apr20有限独立通过。拟正文：

形式完整的规范说明还不能决定行为在该情境下是否恰当。监督可先把流程识别、norm识别和回答的norm appropriateness分开；再固定同一completion，分别在适用norm context与随机错误context下评价，以两者reward差异抑制只会复述规则的shortcut。一个受限分支先把提取的类型化norm与流程转换为SFT，再用正确context分数减去带权错误context分数并截断的信号做GRPO。这里retriever和critic提供训练proxy，不拥有现实规范真值，更不能由模型生成的规范自动授权运行行为。

双context评价、norm检索/抽取和policy训练增加成本，也可能把judge误解和context选择偏差一同学入参数。作者的虚构社会规范及9B模型仅支持受限迁移，HIPAA任务亦有不利切片，judge模型披露存在不一致，不采普遍法律遵从或零trade-off保证。现实高风险场景仍保独立规范来源、人工争议处理和确定性policy gate；原有直接偏好对在目标清晰、上下文稳定时更简单。部署执行保护交第72章，不由这项训练reward批准。

20937 `MULTIMODAL-REPRESENTATION` Ch23，插在视频全局冗余选择/局部区间合并后、连续控制的salience平滑前，source→actual owner由apr20有限独立通过。拟正文：

跨帧持续得到高attention的区域不一定每次都提供新增证据，它也可能成为预算中的attention sink。因而可把当前帧的空间重要性与跨帧累计attention形成的sink proxy分开：前者提供保留候选，后者以软惩罚调整排名，再用相似性阈值处理时间冗余，而不是把高attention位置硬判无用。这样修正的是selector分配规则，既不证明低attention缺少语义，也不证明持续出现的静态物体不重要。

额外attention统计、跨帧汇总与惩罚系数需要校准，静态关键对象或短事件可能被误罚，应在细节证据不足时提高预算、回退原attention排名或完整输入。作者仅在两类7B video VLM、32帧和固定保留率上提供选择器消融；MCQA与GPT-5评价的自由生成不是同一质量分母，部分切片仍退步，未证明90%剪枝无损或生产净加速。selector质量交第66章按输出协议验收，驻留KV生命周期交第45章；soft penalty不是安全或事实authority。

## [2604.21072 Distributed Generative Inference of LLM at Internet Scales with Multi-Dimensional Communication Optimization](https://arxiv.org/html/2604.21072v1)

2+2+2=6，标准必要审阅完成，拟已有覆盖 `INFER-SCHEDULING` [Ch56](../../../../../books/part-05-inference-system/56-inference-scheduling.md)“低带宽拓扑要联合预算Hops、Bytes与Steps”实际三段。已读§4–7、§8.1/Table4及必要microbatch/KV背景。layer placement、microbatch overlap与KV offload共用显存/带宽约束，FP16字节分拆+ZSTD为lossless通信而非低比特量化；proxy draft/top-k与验收反馈piggyback只为低带宽预算，不能替代target验证。既有正文具体联合planner、cache location/communicator/runtime分权及高带宽/CPU-cost回退已承载拟采用机制，不声称全部DP或packing实现已被写入。

动态规划serial目标与pipeline bottleneck目标不能无条件称全局最优；masked hole/background compaction不证明故障或slot lineage安全。8.1与Table4对E6的RTX4090/5090披露不一致，不静默修补设备；网络仿真、FP16模型、若干高带宽AR优于组合的反例不外推生产SLO。§7成本式c/(na)与后式c/n不能作为精确控制律采用。官方abs-v1已实际轻核，v2仅5月后发线索，无撤回说明；不比版本史。Submitted22Apr20:36:47Z、v1 Updated24Apr00:08:37Z/OAI05/06与本批公告组合支持08–09推断，字段自身不是首发。

## [2604.21079 Foveated Reasoning: Stateful, Action-based Visual Focusing for Vision-Language Models](https://arxiv.org/html/2604.21079v1)

2+2+2=6，真实知识缺口深入必要审阅完成，拟 `MULTIMODAL-REPRESENTATION` Ch23 窄增量，未写。已读§2.1–3.3、§4/Table3与AppendixC。离散foveation触发与hidden-state连续box回归在同一AR trajectory取得crop并注入新视觉状态；训练先CE+box监督，再区分普通token的accuracy/format信号、foveation动作accuracy及correct-only area regularizer。当前Ch23主动Observation已有coarse-view/proposal/assembler/answer gate，但没有这种单trajectory连续取证动作头及正确性条件化面积目标的训练责任；不是以crop主题重新写一次。

额外crop编码与视觉KV增长，区域选择错误可自确认；只单图而非视频，全部新增视觉仍驻留使cache随crop数增长，不称零调用或exact跨路径复用。Table3面积惩罚存在内点取舍，极大/极小皆非最佳，所谓全图oracle并不是语义真值上界；预算/准确率与端到端tail未等价。Qwen2.5-VL3/7B与两stage数据/训练条件只支持该受限机制，非开放视觉充分性。官方abs-v1实际已核，8月v2只是后发线索不倒灌；无撤回标记。Submitted22Apr20:44:24Z、Updated24Apr00:09:01Z/OAI空与公告组合为日期推断，不由空OAI推晚首发。

## [2604.21083 Behavioral Consistency and Transparency Analysis on Large Language Model API Gateways](https://arxiv.org/html/2604.21083v1)

2+2+2=6，保护评价合同深入必要审阅完成，拟仅报告。已读§3.1–3.3、§4.1–4.3、billing/latency实验必要段和训练/测试分割。55固定probes的多种特征训练24个one-vs-rest分类器；每model/test_id的重复样本10训练2测试不是新prompt-domain holdout。行为identity signal与密码学backend attestation不同，5未见变体不匹配不证明所有未知backend都能拒绝。多轮recall失败不能唯一归因于truncation，latencyCV亦受网络/负载影响；billing分母仍依gateway自报tokens，无法独立证明真实token或算力。

Ch62认证/授权/immutable model revision和Ch66 sensor calibration已有主体边界，但这套有限黑盒测量不是这些原则的完整实现，也未建立足以替换backend identity证据的部署合同，保留新的受限协议与负面边界，不为其测量headline强写Books。官方abs-v1实际已核Comments为2025-11投稿/2026-03录用，不以私下投稿或acceptance冒充公开正文；若有更早正式全文则单family去重重开。Submitted22Apr20:51:20Z、Updated24Apr00:09:18Z/OAI04/24用于本批组合日期，不据其中一项确定首发。

## [2604.21098 Propensity Inference: Environmental Contributors to LLM Behaviour](https://arxiv.org/html/2604.21098v1)

2+2+2=6，保护行为评价深入必要审阅完成，拟仅报告。实际读§2.1–2.5、§3.4、§4.2与必要factor/randomization说明。12环境因素的随机组合、避免围绕最有利model/config选择环境、Bayesian logistic effects及模型/环境intercepts构成有限评价合同；判据为人设计的行为proxy，不测内部战略信念。odds ratio2并不等于概率翻倍，因子更多取值会影响L1效应总量，capability分组含补估值，战略因素“约半”来自特定GLM likelihood比较，不是意图因果份额。

Ch66实际Self-report/BehaviorProbe/DeploymentOutcome与capability×elicitation×opportunity×permission×consequence段已承担authority和异质实验分账，但不冒称本篇完整随机化程序全已有。23模型11构建环境的新的有限反证值得报告；不存在显著能力趋势不能证明独立或部署安全，跨环境普适认知模型作者亦列未来工作，不将这一实验计数变成长久常数或另加泛化原则。官方abs-v1实际已核，无撤回说明；Submitted22Apr21:35:27Z、Updated24Apr00:10:10Z/OAI04/24与官方公告槽/ID批次形成推断，非Submitted首发。未复现。

## [2604.21045 Hierarchical Policy Optimization for Simultaneous Translation of Unbounded Speech](https://arxiv.org/html/2604.21045v1)

2+2+2=6，中心目标/纠错深入必要审阅完成，拟争议暂缓，待非作者核。已读v1 §3.2–3.3、§4.1–4.3、§5.1–5.2；InfiniSST的交错输入/KV复用是此前baseline，本篇贡献是句级hypothesis/reference对齐后，让quality阈值决定latency reward是否可用，并分别聚合归一化。null对齐被赋最差质量和10秒lag，阻止空译/错译仅靠抢先输出获奖；这只是训练proxy，不是运行时翻译真值或SLO。

印刷目标的桥未闭：Eq4文本称latency独立标准化，分母却写quality std；Eq7已外乘policy ratio，Eq8内部又出现ratio/clipped ratio。rho=2、正优势1、clip上界1.2时，非KL项是2.4而通常一次clipped surrogate为1.2。不能同时按该式与“标准GRPO”概括采用；可能是文稿/实现差异，不证明代码必错或全部实验无效。重开仅需公式勘误/对应loss实现及两种归一化说明，不扩普通代码或完整版本史。

YODAS约5k小时合成子集、ACL60/60的长学术讲话与RealSI十段讲话，EN→ZH/DE/JA，MetricX/COMET及StreamLAAL不构成生产延迟或普遍质量保证；本轮不采用headline数字，必要评价未建立hardware/precision/batch/concurrency/SLO的完整绑定。当前官方abs-v1实际核题名、ACL2026 Oral说明和v1历史，无撤回说明。Submitted=2026-04-22T19:43:51Z、v1Updated=2026-04-24T00:06:45Z、OAI04/24分别保留；日期仅按本批官方ID公告赋号/Thu20EDT及相邻处理簇组合推断08–09，非Submitted或Updated孤证。未复现，不入Books正面保证。

## [2604.21057 TRACES: Tagging Reasoning Steps for Adaptive Cost-Efficient Early-Stopping](https://arxiv.org/html/2604.21057v1)

2+1+2=5，标准必要审阅完成，拟仅报告，待非作者核。已读§3–6、G.4/G.5/H.1：按换行切reasoning step，文本分类器区分constructive/evaluative，再以累计比例和连续五步阈值触发强制答案（100-token预算）。角色迁移是一种可学习sensor；gold first-correct forced-readout/正确样本条件化只用于分析，不能作为部署时内部“已知正确”证据。

核心评价实际为离线完整生成后的回放，停止时延由token-length回归模型加classifier/强制读出成本估算，不是已运行在线SLO。三类8B/14B/32B模型、数学多seed与部分知识集单seed不能混成全协议多次独立复现；困难题质量/阈值代价、标签来源和分类错误仍限制停止。Ch66“推理早停要区分可恢复性与强制读出”已承担oracle、heldout和总成本的长期边界，但不声称本算法全部已有；本轮保留受限新sensor实证，不另加重复原则。当前abs-v1显示后发v2 Aug27，无必要纠错说明，不比较版本史。Submitted=04/22T20:00:18Z、v1Updated=04/24T00:07:37Z、OAI空；日期按同批公开组合推断，空OAI不推晚发。

## [2604.21100 Preconditioned DeltaNet: Curvature-aware Sequence Modeling for Linear Recurrences](https://arxiv.org/html/2604.21100v1)

2+2+2=6，实际知识缺口深入必要审阅完成，拟 `MODEL-LONG-CONTEXT` Ch22增量，未写，待非作者采用核。已读§2.3/§3.1–3.5/§4.1/§4.3与E.3：在线ridge least-squares令G=Σkkᵀ+λI、C=Σvkᵀ、P=G⁻¹；精确ATQ的CPq可用Sherman–Morrison对应ATK写入key=P_prev k/(1+kᵀP_prev k)，在所列初始化/可逆条件下有S=CP。它改变的是写入几何，不是额外保存所有历史token。

精确inverse带来顺序依赖；diagonal second-moment前缀统计换取chunk执行，但明确失去ATQ/ATK的精确等价。实际训练另用独立decay/gain和log-centering/squash稳定write key，不能把diagonal近似冒称全曲率或全局稳定性定理。Ch22现delta/gate/erase-write与momentum分支没有这条精确最小二乘→近似执行的责任链，拟插在Gated DeltaNet状态更新之后、混合训练预算前两段；保留额外统计/反向/kernel成本与固定状态碰撞，统计收益不足时原delta/softmax仍合理。

340M/15B与1B/50B SlimPajama、2048训练长度；340M配置8H100/DDP吞吐测量约10%额外preconditioner成本，不把不同KDA参数/recipe当matched体系。未稳定ATK、若干ARC/Hella/needle切片退步，NIAH不等自然长文精确回读；不采所有模型普适收益。当前abs-v1题名身份已核，未见撤回说明；Submitted04/22T21:38:25Z、Updated04/24T00:10:12Z/OAI04/24用于同批公告组合推断。未复现。

## [2604.21106 How Much Is One Recurrence Worth? Iso-Depth Scaling Laws for Looped Language Models](https://arxiv.org/pdf/2604.21106v1)

2+1+2=5，真实知识缺口深入必要审阅完成，拟 `TRAIN-PRETRAINING` Ch28窄增量，未写。实际读官方PDF-v1首页及§2–6、相关拟合/下游与AppA：116 runs、六FLOPs预算，固定20个有效blocks、recurrence r=1/2/4/8、full BPTT，输入注入的额外compute也计入。共享减少unique参数，却仍执行重复blocks；预算固定时宽度与训练tokens需要一起改变。联合拟合N_eff=N_once+r^φ N_rec，φ约.46是该范围经验结果，不是一般递归容量定律。

所测范围baseline compute frontier仍占优；下游gold-continuation loss、参数知识差距、open-book/composition和reasoning分辨率不混成普遍生成准确率。**v1没有执行truncated-BPTT或hyperconnection改善实验**，这些是未来工作/他作线索；库存摘要对此污染已在screening纠正。abs-v1与PDF一致，后版Apr27/May7不倒灌，也不逐版比较。

Ch28“Scaling不是只增加参数”现有参数/tokens/数据/compute分账尚未明确unique parameter memory与执行depth FLOPs的不同轴；Ch18 loop训练覆盖拥有推理边界。拟在Ch28 compute-optimal总论之后、压缩baseline之前两段说明固定depth共享的联合预算和重新拟合责任，保留dense baseline/优化与kernel成本，不采用φ作为普遍常数或参数下降=wall-clock下降。Submitted04/22T21:51:11Z、v1Updated04/24T00:10:37Z、当前OAI05/08只是原字段，按官方slot/ID与v1簇有据推断08–09。未复现，不因未来工作虚构额外收益。

## [2604.21131 Cross-Session Threats in AI Agents: Benchmark, Evaluation, and Algorithms](https://arxiv.org/html/2604.21131v1)

2+2+2=6，保护评价深入必要审阅完成，拟仅报告，并隔离指标命名/补偿性保证，待非作者核。已读§3.4/3.6、§4.1–4.5/5/6.1–6.2/7.3及必要metric定义：两54-scenario shards、identity-anchor policy与闭环改写对同一Claude judge，完整日志仍低召回是受限反证，不是所有长上下文防御失败。K50 coreset用不同prompt、单provider和较宽区间，不能将差异唯一归因于信息瓶颈；ordered prefix stability与集合相同不同，可作缓存代价sensor，但不是安全真值或端到端净成本。

§4.3把1−FPR命名precision，实际为specificity；其与recall的调和项不是通常TP/(TP+FP)分母的F1。加上.3CSR的可补偿复合分数不能同时称安全非补偿性保证。只隔离该命名/保证，不否定全部局部实验或定义一个加权指标的可能性。rewrite子集正文与附录计数叙述亦不用于正面数量主张；harness未公开不自动抹去可读协议，但不声称实现复现。

Ch72跨session组合intent及持久状态policy正文、Ch45派生prefix身份已有本项能安全采用的长期边界；并非该benchmark全已覆盖。本轮报告新的受限protocol/失败证据，不为它增加重复安全原则。当前abs-v1实际核同题单v1、Comments数据集链接，无撤回说明。Submitted04/22T22:40:31Z、Updated04/24T00:12:12Z/OAI04/24结合公告slot/批次推断，非孤证；正式候选仍待独立裁决，未复现。

## [2604.21139 Slot Machines: How LLMs Keep Track of Multiple Entities](https://arxiv.org/html/2604.21139v1)

2+1+2=5，标准必要审阅完成，拟已有覆盖 `WORLDVIEW-REPRESENTATION` [Ch5](../../../../../books/part-01-worldview/05-what-neural-networks-learn.md)“从可读出到机制”“信息存在、可读与被使用是三个不同命题”，待非作者核。已读§2.1、§3.1、§4.2、§5.3/C.3：受限合成多entity提示与Qwen3-32B残差的无监督slots可读current/prior信息；交换指定entity文本的K/V影响序列关系任务，事实属性任务则未显示同样的prior路径使用。存在/可解码不等原行为使用，现章具体probe→干预→下游及模块移植已经承载这一解释，而非仅同名主题。

选择layer45和句末位置、10k合成prompt、200次特定名字/trait交换只支持该受限观察；全entity token/all-layer K/V patch并不孤立唯一潜在方向，格式变化使slot结构不稳，frontier行为较好亦不识别同一机制。不能从sycophancy/deception类比推真实内部意图。当前abs-v1实际核单v1同题，无撤回说明；Submitted04/22T23:00:49Z、Updated04/24T00:12:30Z/OAI04/24按公告组合推断08–09。未复现，不把新实证名字堆进Books。

## [2604.21164 MAGIC-TTS: Fine-Grained Controllable Speech Synthesis with Explicit Local Duration and Pause Control](https://arxiv.org/html/2604.21164v1)

2+1+2=5，标准必要审阅完成，拟仅报告，待非作者核。已实际读精确v1 §3.1–3.4/4.1–4.4与Tables1–3：F5-TTS flow模型将逐token duration/pause作为声学frame数，用log编码、可用mask和中心化残差注入文本表示，训练随机丢弃控制，保留无指定条件的生成分支。真零经中心化后残差为零，missing由mask置零，二者对该支路均为零，不能说公式已使“零停顿”与“不指定”在输出上可识别。局部条件编码与对齐处理是受限实现，不因映射Ch24就造通用控制保证。

约30k小时粗对齐与230.72小时MFA交叉验证子集；8 A800、动态30000frames/GPU、两阶段训练不是无代价控制。时间评价100条中分别保留92/90可对齐样本，target与测量皆依MFA而非独立时间真值。三条中文局部编辑demo和均值偏差不证明未编辑区域全部保持；Table3部分pause指标反向，不采所有指标改善/零偏置唯一因果。精度、并发、生产SLO未披露，未复现。abs-v1题名/Submitted04/23T00:13:16Z已核，v2 Apr27只为后发线索不比版本，无撤回说明。Updated04/24T00:14:15Z/OAI04/28与公告组合推断08–09，非字段就是首发。

## [2604.21189 Full-Body Dynamic Safety for Robot Manipulators: 3D Poisson Safety Functions for CBF-Based Safety Filters](https://arxiv.org/html/2604.21189v1)

2+2+2=6，保护/实际知识缺口深入必要审阅完成，拟 `MULTIMODAL-EMBODIED-VLA` Ch26窄增量，未写，待非作者采用核。已实际读II-A/B、III-A–D/Theorem1证明、IV-A–C/V：连续机器人表面由ε球采样覆盖，再将自由空间向内缓冲ε，所有采样点留在缓冲空间才推出完整表面安全。这是条件几何保证，不是采样最小间距或QP永远可行。Poisson-disk密集点云实现还依原点云逼近δ，实验用ε+δ及完全free voxel；最小间距不代替真实连续覆盖证明。

单Dirichlet Poisson场供body点查询，joint-velocity QP/低层速度跟踪负责执行。动态障碍依已知几何/状态，感知、自碰撞仍未来工作。Intro消除infeasibility不能采：Figure3 ε≥.2有不可行；serial base缺DOFs也无法避让。FR3七DoF、100³voxel、典型ε.1约30点；UR10e球障碍100Hz状态，RTX5090 PDE平均.002s/OSQP平均.003s及50–100Hz非WCET/物理SLO。Ch26“离散控制周期要为Safety Filter预留一步可达域”解决时间采样，未承载表面采样→空间侵蚀→覆盖/可行性链，拟该节后两段，保留缓冲代价和低层急停/停止。abs-v1单版本/题名/Submitted04/23T01:13:02Z已核，无撤回；Updated04/24T00:15:41Z/OAI04/24按官方slot/赋号与批次组合推断08–09，未复现。

## [2604.21192 How VLAs (Really) Work In Open-World Environments](https://arxiv.org/html/2604.21192v1)

2+2+2=6，保护评价深入必要审阅完成，拟已有覆盖 `PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)“Outcome Witness决定分数的证据基础”中具身attempt/near-hazard/terminal与能力/机会/censor段，待非作者核。已实际读III-A/B、IV-A/B指标与V：B1K50任务×10变体官方checkpoint/seed复跑；8专家500视频按每任务该失败类是否出现计，不是全部事件频率。非确定性导致落差只是解释线索，未唯一控制因果。

sQ将goal progress×upright×handling相乘，seQ加入support-object subgoals；contact本身不坏，移动10cm/跌落才罚，seQOracle置support为1只是上界式对照。g=0使sQ零而可能隐藏危险，TV/nTV须单列；失败/缺机会不证明安全。安全只选20个中等任务非全50，低成功限制机会，scope只限目标/支撑物非所有环境危险，不是真实开放安全。现章已具体承载“不达终点≠未危险、机会和终态分开”的长期判断，不声称整套seQ已有。abs-v1单v1/8pages/Submitted04/23T01:32:51Z已核，无撤回；Updated04/24T00:16:31Z/OAI04/24结合公开批次推断08–09，未复现。

## [2604.21197 Toward Efficient Membership Inference Attacks against Federated Large Language Models: A Projection Residual Approach](https://arxiv.org/html/2604.21197v1)

2+2+2=6，安全/理论纠错深入必要审阅完成，拟争议暂缓，待非作者核。已实际读II-C、III-A–D、IV-A–H及Appendix B-A/B-B：honest-but-curious server持有全局参数及单client当前轮梯度，可对指定target前向；不是secure aggregation后仍必可攻击。投影残差是经验sensor，从gradient span到精确训练record的确定性桥未成立：三个不同输入表示e1、e2、e1+e2，前两为成员、第三非成员，梯度若张成e1/e2，则非成员残差也零。表示不同不排除非成员位于训练样本线性包。

Eq12–14/Appendix B又将乘积rank无条件设min(n,p,m)。取n=3、p=m=2，输入矩阵满列秩2、上游δ秩1或零，梯度rank至多1，成员另一方向会丢失；维度条件只是上界，非full-rank/独立性。只隔离精确判定/能力边界，不否定经验AUC/全部攻击。重开需rank与非成员可识别假设、证明/实现澄清，不扩版本树，不写Books正面保证。

30随机clients、batch16、100当前batch-member/nonmember配对；sum=100命名不冒充真实类别分母。四模型/四数据集容量与padding非唯一因果；IV-F大型LLM只评前两层成本，不将BERT/GPT2全模型或两层时延外推FedLLM。clipping1/noiseσ无完整epsilon/delta会计/adjacency，不采突破正式DP。Ch72 MIA可识别性/变换家族/classifier提供背景，不以主题已有替代理论裁决。abs-v1单v1同题/IEEE S&P2026 accepted已核，acceptance不独证早首发；Submitted04/23T01:44:04Z、Updated04/24T00:16:57Z/OAI04/24按公告组合推断08–09，未复现。

## [2604.21215 The Recurrent Transformer: Greater Effective Depth and Efficient Decoding](https://arxiv.org/html/2604.21215v1)

2+2+2=6，真实知识缺口深入必要审阅完成，拟 `MODEL-LONG-CONTEXT` Ch22窄增量，未写/待非作者核。实际§2.1–2.3/§4–7/E.4：同层过去KV从过去位置的**层输出**派生，当前位置用层输入temporary KV避免自身循环，输出后才写persistent KV。不同于普通KV与跨层共享feedback，仍保存逐token历史而非固定容量state。Ch22现local/global、YOCO-U与GDN分支未说明这条同层时间递归的状态身份和并行代价；拟在YOCO-U后、线性混合前插两段，不另给Ch45重复模型语义owner。

未来query只依当前层输入，提前可算；在线softmax统计让已生成KV tile对未来query提前累计，数学attention不变但浮点重排，HBM从二次到NlogN不消除二次FLOPs或MLP顺序依赖。B512/N512、checkpoint重算、CUDA graph、position-major与custom backward都是必要工程代价，gradient accumulation不增加实际MLP batch。§4稳定定理只简化一层uniform attention初始化，不能作为所有learned attention稳定保证。150/300M C4、single H100、逐层latency排除embedding/unembedding/loss；parameter-matched不是compute-matched。E.4多个accuracy切片更差，完整optimized decode latency明确未来工作，不将较少层KV公式叫实测线上加速。abs-v1单版本/题名/Submitted04/23T02:12:58Z已核，无撤回；日期按官方slot/赋号与本批v1簇有据推断08–09，非提交首发；未复现。

## [2604.21221 Sparse Forcing: Native Trainable Sparse Attention for Real-time Autoregressive Diffusion Video Generation](https://arxiv.org/html/2604.21221v1)

2+2+2=6，真实知识缺口深入必要审阅完成，拟 `MULTIMODAL-GENERATIVE-PARADIGMS` Ch24窄增量，未写/待非作者核。实际§3.1–3.5/4.1–4.5、Tables1–3：完全denoised历史作为persistent anchors，local窗口承载近处/当前denoise；evicted local进入coarse pooling/Top-C候选，sink保留，persistent密读+local Top-K合为一个masked softmax。pool代表只供routing不成为细粒度内容真值；被丢旧history不可无限恢复。DMD训练就启用动态cache/局部稀疏，与训练后单独剪cache不同。Ch24 Salt已有历史质量coverage，但没有“历史保留策略与局部mask同训练目标覆盖”的具体分支，拟在Salt后两段；kernel artifact仍handoff Ch49。

Wan2.1 1.3B、5秒训练/4-step/8H100/1200steps/batch64、C/local各6frames/TopK25%；PBSA ThunderKittens支持训练反向。Table3去persistent更快22.8vs18.3FPS但质量下降，训练不是免费；短片Table1有quality反向，不能采用全指标/所有长度优。H10096GB kernel原字符串非自行修硬件，kernel速比不叫完整生成SLO；VBench5sample×946prompts、rewrite及有限20/60秒不能证明无限一致性/物理world真值。保dense/full-history或增预算回退。abs-v1单版本/同题/Submitted04/23T02:22:25Z已核，无撤回；官方公告批次组合推断08–09，未复现。

## [2604.21229 EngramaBench: Evaluating Long-Term Conversational Memory with Structured Graph Retrieval](https://arxiv.org/html/2604.21229v1)

2+1+2=5，标准必要审阅完成，拟仅报告，待非作者核。实际§3–8/Limitations：5synthetic personas、100conversation/150query，每factual slice30；固定GPT4o/temperature.3不使其他extraction/retrieval预算相同。cross-space .6532>.6291但aggregate .5367<.6186，移除planner或typed answer增加aggregate却损该slice，体现任务专用结构的受限取舍而非Graph普遍优；未充分power证明总体排名。

query serving费用排除所有离线构建；Mem0 Top20/default与proprietary Engrama内部weight/prompt未披露，不从同answerer归因所有收益。emergent insight tokenF1不是语义truth，exact runtime evidence provenance未完整审计；分persona snapshot与frozen scorer不证明部署回放。Ch77“先分解Memory组件，再判断Graph是否值得”和workload Pareto已承载长期选择原则，但本报告保独立有限消融反证，不冒签整算法Existing或因为owner已有就删候选。abs-v1单版本/同题/Submitted04/23T02:51:42Z已核，无撤回；本批slot/赋号及邻接v1簇推断08–09，非Submitted独证；未复现。

## [2604.21241 CorridorVLA: Explicit Spatial Constraints for Generative Action Heads via Sparse Anchors](https://arxiv.org/html/2604.21241v1)

2+2+2=6，保护/中心公式纠错深入必要审阅完成，拟争议暂缓，待非作者核。已实际读III-A–C Eq1–10、IV-A/B、V-A–C。extended action含被监督的Δ-position，g取同一组anchor增量，而p*又由GT状态定义；Eq6用g(A*)与p*的差设δ。因此按印刷定义二者相同、δ=0，不能推出所宣称的正容忍带。预测anchor也未直接出现在该δ定义中；若真实实现采用另一组状态/预测值，需补定义与算法桥。只隔离正容忍/预测物理线索约束的中心采用，不否定auxiliary head与受限经验收益，不扩所有实验重审。

SmolVLA/GR00T与LIBERO/Plus有限评价，K=3增加输出职责，不是现实碰撞安全证明；部分Object切片低于base。重开需Eq6对象及实际corridor构造说明、对应实现/受控对照，不写Ch26正面保证。官方abs-v1同题、v2后发July5，无撤回说明；Submitted04/23T03:17:50Z、Updated04/24T00:21:21Z、OAI空，使用官方slot/赋号与相邻处理簇的有据08–09推断，不把单字段当首发；未复现。

## [2604.21254 Hyperloop Transformers](https://arxiv.org/html/2604.21254v1)

2+2+2=6，真实知识缺口深入必要审阅完成，拟 `MODEL-TRANSFORMER-LAYER` Ch17窄增量，未写/待非作者核。实际§2.1–2.2/3、§4.1–4.3及Tables1–2：begin/end一次、中段重复，matrix residual只在loop边界混合；diagonal sigmoid carry不是Sinkhorn双随机mixer，另有loop-specific权重与位置，不能称所有参数完全共享。当前Ch17 depth-routing/multi-stream/mixer说明可行性与资源成本，但未承载“混合频率在loop而非每子层”与权重驻留/执行深度分账；Ch18的loop状态/停止交接不是这个架构分支。拟Ch17 mixer之后两段，避免重复Ch18停止策略。

GPTQ跨全部loop采集activation，不能以首轮画像代表共享权重输入；depth-matched不等compute-matched，少权重不等少activation/KV或低延迟。8H100 BF16训练/INT4 group128受限，训练吞吐有反向，100B overtraining切片PPL12.19高于vanilla12.15/mHC12.16，不采全面优。官方abs-v1同题，v2 Apr25/v3 July2为后发、不比较全部版本；Submitted03:46:14Z、Updated00:22:10Z/OAI空，按本批官方slot组合推断08–09；未复现。

## [2604.21255 When Agents Look the Same: Quantifying Distillation-Induced Similarity in Tool-Use Behaviors](https://arxiv.org/html/2604.21255v1)

2+1+2=5，标准必要审阅完成，拟仅报告，待非作者核。实际§3.1–3.3/4.1–4.2/5.1–5.2及Limitations/AppC.3：RPS只评共同stage，AGS从成功模型tool交集定义mandatory集合，再评optional节点与依赖。交集是本model/task pool的经验对象，不是逻辑必需tool证明；图/语句相似不能作为训练来源attestation。受控200条teacher轨迹LoRA提供局部teacher-specific变化，但不同分量并非全同向，Pearson .491、p=.054也不证明两sensor独立。

18模型/150英语客服任务、单Claude参考及judge/harness受限；确认商业模型蒸馏来源需要额外provenance，不从排行榜相似推内部teacher。Ch66 subject/harness identity及权威provenance与behavioral association分离已有长期边界，本项保留新的有限diagnostic protocol，不声称整指标已被Books完整承载、也不把它采为发布证明。官方abs单v1/ACL accepted无撤回，Submitted03:48:56Z、Updated00:22:11Z/OAI04/24；按官方slot组合推断08–09。未复现。

## [2604.21268 Measure Twice, Click Once: Co-evolving Proposer and Visual Critic via Reinforcement Learning for GUI Grounding](https://arxiv.org/html/2604.21268v1)

2+2+2=6，标准必要审阅完成，拟仅报告，待非作者核。实际§4.1–4.3 Eq1–9与§5.1–5.7：同MLLM不同prompt作proposer/visual critic，K坐标一次提出后将marker渲染到图上排序；各角色的EMA正确率/nDCG控制另一角色coverage/ranking奖励。maturity是受限训练proxy，不是critic真实可靠性证书；accuracy加hit项不必限于[0,1]。Ch33已有共同训练及独立outcome/角色credit分账，本法新的GUI operating point可报告，尚不据其协同曲线修改通用训练保证。

Oracle@K只问有无正确box，不是在线critic top1；几何baseline八次独立生成与一proposal加critic未等端到端预算。token成本不等wall-clock，grounding成功不证明task completion/执行授权；部分MMBench2/ScreenSpot切片低于base，拒绝“全slice更优”。官方abs同题单v1无撤回说明；Submitted04:23:31Z、Updated00:23:16Z/OAI04/24，按公告slot/赋号与本批簇推断08–09，非单证；未复现。

## [2604.21276 Do LLM Decoders Listen Fairly? Benchmarking How Language Model Priors Shape Bias in Speech Recognition](https://arxiv.org/html/2604.21276v1)

2+2+2=6，标准必要审阅完成，拟已有覆盖 `PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) Compression Release人口组WER/循环输出与“差距缩小须检查较好群体退化”三段，待非作者核。实际§2.1–2.4/4.1–4.3/5.1–5.2：matched-prompt FairSpeech减少词汇差异，9ASR/12噪声条件与bootstrap只支持受限切片；mask让全组错误很高、相对差距压缩，不是fairness改善。该可迁移判断已在实际正文，报告新acoustic degradation例证，不把权重压缩与音频压缩混为同一机制。

不同模型的训练语料/decoder/音频瓶颈仍混杂，不采“compression唯一决定robustness”；严重mask也不能凭优势仍在就排除预训练transcript泄漏。WER差/最大最小比需与绝对错误同列，英语朗读不推多语或自然会话。官方abs-v1同题、未给撤回标记；Submitted04/23T04:40:58Z、Updated04/24T00:23:37Z/OAI04/24，按官方slot/赋号与相邻簇组合推断08–09，未复现。

## [2604.21277 Can MLLMs "Read" What is Missing?](https://arxiv.org/html/2604.21277v1)

本项贡献复裁为前分母关闭，不评分、不列候选或 Books。原必要审阅证据保留供复查：实际§3.1–3.3/4.1–4.6的局部mask target、剩余视觉/布局重构与level-aware词面/语义/judge评分，是masked reconstruction及scorer的具体题库组合；100随机样本91%agreement不证明binary判定能避免hallucination。没有matched prompt/instruction/cue消融隔离新的因果辨别或发布条件，末节也承认指令跟随混杂，不采用“已经纯测量”的保证。具体关闭理由与改判在 `V3_SCREENING_NOTES.md`；不是因文档领域或规模拒绝。

人审唯一答案与样例中多个合理领域解释仍有张力；六月2025后材料日期和target masking均不能证明预训练无泄漏。length权重/语义近似/judge错误须保留，排行榜差不解释内部visual failure。官方abs-v1题名一致、未给撤回标记；Submitted04/23T04:44:25Z、Updated04/24T00:23:51Z/OAI04/28，结合官方公告/赋号与批次簇推断08–09，不把后OAI回填为首发；未复现。

## [2604.21286 Cross-Entropy Is Load-Bearing: A Pre-Registered Scope Test of the K-Way Energy Probe on Bidirectional Predictive Coding](https://arxiv.org/html/2604.21286v1)

2+1+2=5，标准必要审阅完成，拟仅报告，待非作者核。实际§2/3/4.1–4.4/5/6：TinyConv2.1M、CIFAR10、10配对seed在CE/MSE/双向条件比较energy margin与softmax AUROC2；预注册latent movement操作检查失败，不能把probe改善归bidirectional dynamics。改logit temperature改变向量到scalar margin的非线性排名，并非后置单调score变换，所以AUROC可变；温度消融只作部分描述解释，非66%严格因果份额。

bPC同时改变归一化与训练/评价settling次数，small positive .008与generative能量<1%只限此模型。报告这一objective/readout-baseline公平对照的受限反证，不据它造“模型自知”或向所有LLM推荐probe；Ch66既有calibration identity/diagnostic authority是背景，并非本实验完整已有覆盖。官方abs-v1同题、未给撤回标记；Submitted04/23T05:03:18Z、Updated04/24T00:24:33Z/OAI04/24，按官方公告组合推断08–09；未复现。

## [2604.21327 Understanding and Mitigating Spurious Signal Amplification in Test-Time Reinforcement Learning for Math Reasoning](https://arxiv.org/html/2604.21327v1)

2+2+2=6，纠错深入必要审阅完成，拟中心解释争议/暂缓，待非作者核。实际§2–3/Eq5–7、§4.1–4.4/Tables1–4：从N64多数答案构造伪reward，K32组将正例数限制在K/2并给正负固定±1，最后M128重采样多数答案作五epoch SFT。固定幅度确实取消组内std的放大，但不能消除多数标签错误；负例筛选改变优化分布，稀有有效答案仍可能被罚。§4.4却称MATH后期mean advantage转正；按印刷Eq5–7，每prompt均值=(2K⁺−K)/K≤0，任意正权跨prompt平均也≤0，无法出现该正均值。需要作者说明日志分母、token权重或实际实现与公式的差异；不据此采用“自适应正信号转换”机制，不否定所有实验或取消固定幅度的一般可行性。

三种Qwen/Llama、三数学任务，BCS单独在Qwen3B退步，Llama AIME弱于ETMR；五epoch壁时不含全部额外128rollout构建成本，不能作matched总compute。现Ch33伪标签/归一化原则不解决本篇公式-日志冲突，暂不写Books。官方abs-v1同题、未给撤回标记；Submitted04/23T06:32:08Z、v1Updated04/24T00:27:26Z/OAI04/24；依官方slot/赋号、相邻处理簇的组合有据推断08–09，非Updated孤证首发。重开：精确日志定义或代码/勘误能解释正均值；未复现。

## [2604.21330 Teacher-Guided Routing for Sparse Vision Mixture-of-Experts](https://arxiv.org/html/2604.21330v1)

2+2+2=6，真实知识缺口深入必要审阅完成，拟MODEL-MOE Ch21窄分支，待非作者采用/未写。实际§3/4/5.1–5.4/J.4：冻结dense视觉teacher backbone的中间features供辅助router，辅助router由load/entropy训练而非task loss，stop-gradient的teacher routing分布再以KL约束student router。teacher backbone冻结不等于teacher router固定，后者联合训练；这有别于现Ch21已激活expert虚拟移除的离线contribution prior和dense-upcycling初始化蒸馏：用外部feature空间形成训练期assignment proxy，补selected experts之外的路由信号，但load/entropy不取得语义正确authority。

ImageNet1K/DeiT Tiny–Base、三个MoE层、2/4 H100、预训ImageNet21K teacher为额外特权资产。early-half指导、末层teacher与仅模仿消融有反向结果；teacher inference upper bound不能当部署结果。J.4列单H100秒/epoch1006→1020、2560→2570、4930→4954且参数计数排除teacher，不采“零成本”。CLS实现不推任意LLM token路由稳定/吞吐。官方abs-v1同题、无撤回标记；Submitted04/23T06:34:10Z、Updated04/24T00:27:30Z/OAI04/24；组合推断08–09。拟插入负载均衡代理段后，按不同训练信号职责与指导时序叙述；未复现。

## [2604.21335 Sub-Token Routing in LoRA for Adaptation and Query-Aware KV Compression](https://arxiv.org/html/2604.21335v1)

2+2+2=6，标准必要审阅完成，拟仅报告，待非作者核。实际§3.1–3.4/Eq4–13、§4.3–4.4/A.2/C.6：Q/K保留，V分组；无query分支保部分groups并学习重建，另一分支对context-token/group联合Top-M且query末16token完整保留，未保V置零，不混称同一恢复策略。split层context hidden预测诊断query-attention目标；causal context状态本身不能读取末位未来query，属于学习近似proposal而非已观察当前query的精确打分。不能从名字query-aware推出任意新query同一cache可复用。

Qwen7–72B/单卡H100NVL、batch1/400token局部forward、MMLU/RULER有限对照；TotalKV=(1+ρV)/2已计完整K，不误写ρV就是总KV率。C.6某memory/latency配置无收益或略退，warmup排除，重建/selector不是免费；没有足够packed动态group执行、完整服务或SLO证据。现Ch45状态重建及attention-distortion主线可承载边界，但不把具体value-group算法冒称完整Existing；暂将它作为该轴受限operating point，仅报告并保质量/执行缺口。官方abs-v1同题、无撤回标记；Submitted04/23T06:47:33Z、v1Updated04/24T00:27:52Z、OAI空，组合处理簇推断08–09；后v2/v3不展开差分。未复现。

## [2604.21343 Latent Denoising Improves Visual Alignment in Large Multimodal Models](https://arxiv.org/html/2604.21343v1)

2+2+2=6，真实知识缺口深入必要审阅完成，拟MULTIMODAL-REPRESENTATION Ch23，待非作者采用/未写。实际§3.1–3.3/Eq9–12、§4.1–4.6必要对照：projected visual token按saliency选noise/mask，在LMM中间层接辅助decoder，恢复冻结视觉encoder的clean patch features，加逐行关系KL与同图patch contrastive；仍保答案loss。现Ch23已区分masked input与全patch target监督，未明确“腐化发生在projector之后、恢复责任落在语言模型中间状态”的这条训练分支。它不改变所有encoder层或在部署期持续denoise，训练corruption/辅助head撤掉才恢复普通inference。

LLaVA CLIP/SigLIP及Qwen2.5VL7B、558K/665K两阶段、LoRA128/α256；clean MME CLIP与Qwen有退步，CKA/kNN仅诊断不能证明唯一语义因果。latent corruption训练与pixel noise/blur/weather/digital测试是不同对象，受限迁移不保证任意污染稳健；saliency、layer16及noise比例是校准recipe非truth。额外训练decoder/teacher目标有成本，零新增inference不能改名零训练成本。官方abs-v1同题、无撤回标记；Submitted04/23T06:58:08Z、Updated04/24T00:28:23Z/OAI空；官方slot/赋号与邻簇组合推断08–09。拟接在完整patch监督两段之后，与视觉encoder预训练分支区别；未复现。

## [2604.21346 Symbolic Grounding Reveals Representational Bottlenecks in Abstract Visual Reasoning](https://arxiv.org/html/2604.21346v1)

2+2+2=6，标准必要审阅完成，拟仅报告，待非作者核。实际§3/4.1–4.3/5.1–5.5：以Bongard LOGO真实生成程序替代pixels，形式grammar/自然语言、已知concept、额外query image与两类permutation作诊断。已知生成程序是特权representation上界，不是已部署perception模块；主rawimage Gemini与多LLM symbolic池不完全matched，grounded子集只补query图，不等恢复所有13张图像的感知控制。symbolic成绩提升支持输入接口受限诊断，不证明所有原失败唯一因果是vision encoder，也不证明任意无oracle场景可由C–G修复。

2000固定subset、四splits、parse失败计错，开放模型temperature0不保证全执行确定性；concept指导有负向、query permutation改变生成图的真实语义却保旧label，所以下降仅条件敏感性而非正确结构理解证明。现Ch66规则/状态/alias及oracle分账是背景，不能称本benchmark整套已有；暂报告这项受限诊断，不写通用视觉能力因果。官方abs-v1同题、无撤回标记；Submitted04/23T07:03:48Z、Updated04/24T00:28:49Z/OAI04/24，依官方slot/ID赋号与处理簇有据推断08–09，未复现。

## [2604.21361 Time, Causality, and Observability Failures in Distributed AI Inference Systems](https://arxiv.org/html/2604.21361v1)

2+1+2=5，标准必要审阅完成，拟已有覆盖 `PLATFORM-TRACE` Ch69（ROADMAP实际ID为PLATFORM-TRACE），待非作者核。实际§3/4.1–4.4/5.1–5.4/6.1–6.4：仅应用级inference时戳加偏移而非改OS，Kafka/ZeroMQ实际测到send→postreceive负span，输出/吞吐仍正常。负span数不是失败请求数；3–5ms仅本配置边界，30s health滚窗恢复不证明时钟已恢复，绝对counts跨不同duration不能直接比。Aeron只future，部分同步/漂移与硬件/模型条件不完整，不能采用通用clock阈值或平台SLO。

Ch69现“跨节点时间戳不是天然的因果顺序”76–86行已实际写出这一受控反证、clock domain/误差及request/message dependency优先、不可排序保留、单机timestamp共存；本轮对读实际正文/两侧，No Change不是仅同主题。Ch67聚合health不重复拥有请求因果。官方abs-v1同题、无撤回标记；Submitted04/23T07:21:45Z、Updated04/24T00:29:36Z/OAI04/24；组合推断08–09。未复现。

## [2604.21391 From Noise to Intent: Anchoring Generative VLA Policies with Residual Bridges](https://arxiv.org/html/2604.21391v1)

2+2+2=6，中心理论纠错深入必要审阅完成，拟争议/暂缓，不采理论必要性，待非作者核。实际§3.1–3.3/Eq5–7、§4/Eq8–11、§5直接对照、§7、AppA.3：DCT低频回归prior再作residual flow matching是具体条件分支，频率本身不是intent真值。AppA.3以起点density/score不含c推CFM vector field必不含c，没有连接速度与路径时间导数。反例x0~N(0,1)独立c，x1=c（c=±1），直线CFM在t=0的最优条件速度u0(x,c)=c−x，依然依赖c，而p0完全相同；故源独立不能单独推出其“条件梯度必消失/anchor为必要条件”结论。

近target source降低给定pair残差范数还需原比较假设，均值anchor不一般最大化MI；low/high不是物理意图/执行的唯一分解。LIBERO/Plus、SimplerEnv、有限ALOHA三阶段提供经验，训练规模与pretrainedbaseline不同，NFE不是总延迟/安全证明。AppA.3保证为中心桥，故不把理论必要性写Ch26；不否定受限anchor算法、全部实验或独立安全controller的必要性。重开需正确CFM路径推导/条件及实现对照，不查整篇引用树。官方abs-v1同题、无撤回标记；Submitted04/23T07:59:26Z、Updated04/24T00:31:50Z/OAI空；官方slot/赋号与邻簇组合推断08–09，未复现。

## [2604.21395 Supervised Learning Has a Necessary Geometric Blind Spot: Theory, Consequences, and Minimal Repair](https://arxiv.org/html/2604.21395v1)

2+2+2=6，中心普遍保证纠错深入必要审阅完成，拟争议/暂缓，待非作者核。实际§4/5.1–5.2/Prop5–7、§6及§7主要受限评价：以Gaussian encoder一致性loss并设task-loss cap，比较Jacobian与归一化TDI的排序。但Prop5证明只依赖covariance=σ²I，却在主文宣称Gaussian是唯一isotropic law；独立±σ Rademacher分量同样有该covariance且对任意J满足E||Jδ||²=σ²||J||F²，直接否定分布唯一性，不否定协方差等式。Corollary2把crossentropy excess写I(n;y|x)>0，但x已包含n时该条件MI=0，需要说明是否本意是I(n;y|s)。Prop6所定义F²/||Jw||²也不一般最大仅dx：J=diag(1,ε),w=e2时比值=(1+ε²)/ε²可任意大。

有限ViT/CIFAR及BERT片段的经验对照可保留，但TDI含逐层representation norm归一化，不是Jacobian Fro或未归一化drift的同一个量；局部低敏感度不能凭指标排名扩写“all ERM必同缺陷、Gaussian唯一修复”。taskloss cap只给分数上界≤cap/(1+cap)，没饱和不能直接恒等。中心理论与诊断解释需作者修正/明确条件后才能正面采用，不据三处反例否定全部实验。官方abs-v1同题、无撤回标记；Submitted04/23T08:03:33Z、Updated04/24T00:32:02Z/OAI空；组合推断08–09，未复现。

## [2604.21326 MiMIC: Mitigating Visual Modality Collapse in Universal Multimodal Retrieval While Avoiding Semantic Misalignment](https://arxiv.org/html/2604.21326v1)

2+2+2=6，真实知识缺口深入必要审阅完成，拟 `MULTIMODAL-REPRESENTATION` Ch23 fusion窄增量，待非作者采用/未写。实际§3.1–3.2/4/5.1–5.5/A.3：独立text/visual编码、BOS query仅在decoder交叉读取两KV，无两源self-attention；训练将single-modality embedding随机混入fused representation，再caption dropout使contrastive目标覆盖缺caption。现Ch23早/晚/cross-fusion有支配与隔离原则，但缺“融合点与缺模态训练支持联合验收”的这一实际分支。

去dropout/FiD与mixin消融提供受限支持，不把t-SNE或neighborhood overlap当语义truth/唯一因果。T5/CLIP-B32、text128、batch64、20epoch/earlystop与ANCE Top100重建负例均有训练成本；mixin/ratio最优随任务变，部分T2T R20低于baseline，不采全slice赢。大型VLM扩展未来，硬件/precision/线上SLO未披露；旧late/early仍合理。官方abs-v1同题、未给撤回标记；Submitted04/23T06:29:42Z、Updated04/24T00:27:25Z/OAI04/24，官方slot/赋号与邻簇推断08–09；未复现。

## [2604.21275 Optimizing High-Throughput Distributed Data Pipelines for Reproducible Deep Learning at Scale](https://arxiv.org/html/2604.21275v1)

2+2+2=6，真实知识缺口深入必要审阅完成，拟 `TRAIN-DATA` Ch27 读取顺序分支，待非作者采用/未写。实际§III-A/B、IV-A/B、V-A–C：先以RAM缓存及本地disk对照分离HDFS I/O与主线程Arrow→NumPy CPU瓶颈，再将转换推至worker、缓存预转换rowgroup；顺序epoch采用quota填满后回源，而非声称LRU总是最差。固定shuffle种子仍不能固定共享ventilator/result queue的领取与返回顺序；专属worker队列按同一round-robin分派与合并，把最终batch顺序从线程完成顺序中分离。RNG更新不是单独确定性证明，算法只限定同配置/rowgroup与正常完成路径，论文未验证worker故障、resume或任意异构配置的顺序恢复。

实际对读Ch27不可变manifest/seed/cursor（约782–817）及Ch36相关worker/聚合顺序，已有发布与lineage合同不包含“输入身份相同而并发返回仍改变训练序列”的具体责任，拟接在lineage→checkpoint之后、batch原子发布之前两段。代价是ready-to-train缓存内存、quota回源、慢worker的有序合并等待与额外队列/线程timeout；不把增加worker视为无限吞吐。受限推荐模型、HDFS Parquet数十TB/数百features、Ray/Horovod多GPU；具体模型/设备/精度/batch/并发/故障策略未披露。MAP差距.5%→.13%同时有auxiliary stability techniques，不能归因全部reader redesign，也不能采用“全训练严格确定”宣传或6×普律。官方abs-v1同题/Comments5页8图1表，无撤回标记；Submitted04/23T04:40:47Z、Updated04/24T00:23:35Z/OAI04/24，仅与官方slot/ID赋号/邻簇联合推断08–09；未复现。

## [2604.21454 Reasoning Primitives in Hybrid and Non-Hybrid LLMs](https://arxiv.org/html/2604.21454v1)

2+2+2=6，标准必要审阅完成，拟已有覆盖 `MODEL-LONG-CONTEXT` Ch22，待非作者核。当前官方abs-v1/HTML题名只有上述主标题，旧库存长副标题不作为版本身份。实际§3.1–3.2/4.1–4.2/5：OLMo3与Hybrid7B的预训练data/recipe为受限matched pair，再比较Think/Instruct在AstroRecall与Collision的顺序状态更新×检索两轴。每(m,n)100题，JSON parsing与conditional accuracy另分账；Think最大6000生成token而Instruct40，SFT/推理预算不是matched，不能将Think收益单独归因 reasoning training，parse失败也不等内部状态真实消失。Hybrid在不同难度/模型变体的方向不同，作者明确范围很窄。

Ch22现约238–242的“先更新状态、再选择历史需要组合能力”、固定训练与目标成本分账，以及194的访问图匹配已实际承载此设计判断；不是声称这些新模型/题库所有细节已写入。额外外显推理不是免费架构替代，也不证明hybrid普遍更好，受限生成/解析结果可留报告，无须重复书稿。硬件/precision/运行batch/concurrency/SLO未披露，vLLM/temperature0不证明所有调用确定。Submitted04/23T09:13:28Z、Updated04/24T00:36:49Z；当前OAI05/27为后续记录状态，不冒称04/24首发证据。精确v1身份、永久赋号/Thu20EDT slot及相邻早批处理簇仅构成08–09有据范围推断，未比较v2或复现实验。

## [2604.21477 MCP Pitfall Lab: Exposing Developer Pitfalls in MCP Tool Server Security under Multi-Vector Attacks](https://arxiv.org/html/2604.21477v1)

2+2+2=6，保护合同深入必要审阅完成，拟已有覆盖 `PLATFORM-SECURITY` Ch72，待非作者核。实际§4–7、§8.1–8.5/§10.3：本文是protocol-aware静态检查+trace/objective-validator测试，不是screening旧句所说semantic BOM。Tier1仅查本地描述、schema、日志/guard等P1/P2/P5/P6，P3跨tool forwarding与P4图像→sink尚需动态数据流；清除29项静态finding、risk0不是全部attack被阻断。可信arena predicate区分attacker目的地命中与一般message side effect，拒绝按Agent narrative证明执行安全。

六server版本36binarylabels是静态分母；324是生成计划/大队列，真正Axis3只有email下19runs，其中12sink runs。全部divergence为D5未写具体tool name，不是所有自述否认/全部隐私攻击；图像链全面实测future。实际设备M2/macOS、Python3.10/FastMCP2.14/GPT4.1-mini；没有跨模型部署/攻击族总体保证。Ch72现“Security Agent…Tool Trace与Deterministic Predicate”“Containment…阶段”、1009附近value→transformation→sink授权，以及2585描述/静态动态行为独立审计都直接承载采用命题和限制；No Change不是同主题，也不称本套规则完整已写。官方abs-v1同题且当前仅列后续v2无撤回标记；Submitted04/23T09:39:15Z、Updated04/24T00:38:42Z/OAI空，官方slot/ID赋号+邻簇有据推断08–09，未复现、未无差别读324runs。

## [2604.21480 Efficient Agent Evaluation via Diversity-Guided User Simulation](https://arxiv.org/html/2604.21480v1)

2+2+2=6，标准必要审阅完成，拟仅报告，待非作者核。实际§3.1–3.5、§4、§5/Table1/3、B.1、E.2/G：在用户turn前保存完整orchestrator/environment/toolDB/history/RNG/routing/counter状态；先LLM选junction，再生成3候选用户回应、取embedding最不相似者，恢复同prefix继续。完整状态不是仅conversation文本，论文宣称exact restoration但未验证所有外部不可序列化副作用；KV reuse是潜在兼容路径，不是已测服务加速。意图保持是事后judge而非在线接受Gate，25.27%仍有intent-miss，不能把定向失败率当真实用户失败概率。

τ-bench Airline/Retail/Telecom、GPTOSS120B/Gemini2.5Flash、fixedseed42、Agent0/User.7、max100steps/10errors。Table3固定12trajectory时JC单独errors/token提高而unique failing tasks78→75下降，加入divergent response/selection才80/81；因此成本效率与覆盖不是同一收益。公开表1加branch也增加总token，所谓严格更高效只限给定采样合同，不证明wall-clock/生产成本。E.2每branch约429.52框架token另算，0.2%–.08%是两类模型token价格假设下的钱比，不是token或GPU时间占比；fixedseed/没有API错误不证明普遍determinism。Ch66已有完整fork identity/恢复边界，Ch81有状态fork与搜索账本，但不能称本新junction/用户多样性策略全部已有；本轮保留其受限效率—覆盖操作点与反证，不把具体选择heuristic采为长期默认。硬件/precision/batch/concurrency/SLO未披露；Submitted04/23T09:41:21Z、Updated04/24T00:38:50Z/OAI04/24与官方公告规则/邻簇仅组合推断08–09，未复现。
## [2604.21511 From Tokens to Concepts: Leveraging SAE for SPLADE](https://arxiv.org/html/2604.21511v1)

2+2+2=6，真实知识缺口深入必要审阅完成，拟AGENT-RAG Ch76 learned-sparse表示分支，待非作者采用/未写。实际§3–5/6–7：先冻结PLM重建token hidden训练SAE，再删decoder、解冻PLM与SAE encoder按检索distillation/FLOPs regularizer联合训练；把倒排维度从token词表换为训练的latent dictionary。token TopK不保证聚合文档仍同等稀疏，SAE reconstruction良好也不等相关性或可解释concept真值。现Ch76 lexical/dense与单/多向量取舍未承载这个倒排词表与retrieval目标联合训练的替代分支，拟在检索表示段窄补，不把latent名称当稳定语义身份。

DistilBERT/MSMARCO8.8M、单A100、SAE160k步batch768和retrieval240k步query32/8负例，query32/doc256；35h+24h是额外两阶段训练。QDFLOPs只是posting访问预期、E²权重任意，不是实测GPU FLOPs或部署SLO。Tables3/6部分ID/TREC/语言退步；多语训练mMARCO翻译数据，跨强基线预算不matched。§6共现阈值定义synonymy/polysemy只是启发式，作者不能得出conclusive概念结论；§7仍有词法精细匹配与latent组合压力。若作为工程资产采用，encoder/dictionary/index joint revision与重建是我们的推断，不冒称作者已验证滚动升级。官方abs-v1同题、Comments未见撤回标记；Submitted04/23T10:13:21Z，与官方slot/ID赋号、邻簇处理范围联合推断08–09，不将Submitted当公开。未复现。

## [2604.21523 Seeing Isn't Believing: Uncovering Blind Spots in Evaluator Vision-Language Models](https://arxiv.org/html/2604.21523v1)

2+2+2=6，标准必要审阅完成，拟仅报告，待非作者核。实际§2–4、B人审过程：600 I2T/750 T2I seed经人工检查，模型生成退化与不改应得分的变体再人工筛选，四VLM三种评价接口。§3.1三指标对象不同：single看分数不变、pairwise看未独选gold、reference看给满分。因此不能按这些失败率直接证明pairwise普遍更可靠，分数下降不保证方向正确/校准；pairwise在invariant切片反而更不稳定。§4.4换reference在I2T变差/T2I变好，§4.5更高reasoning可反退，§4.7理由识别依赖另一Gemini judge，不是人类独立感知证明。

Ch66长视频评价器最低辨别力/合成偏差（SLVMEval）、rubric criterion与ranking分权已有长期原则，但不称本静态图像40维benchmark全已覆盖。保留受限“参考、无害变换及评分接口共同决定错误切片”的操作点和跨指标比较限制，不据此更换默认judge或采厂商排名。人工认为可感知的合成扰动不代表自然生成错误分布，temperature0/同prompt不保证跨API预算matched；hardware/precision/batch/concurrency/SLO未披露。官方abs-v1同题、未见撤回说明；Submitted04/23T10:36:50Z与官方slot/ID分配及相邻早处理簇构成08–09有据推断，未复现实验。

## [2604.21549 Unbiased Prevalence Estimation with Multicalibrated LLMs](https://arxiv.org/pdf/2604.21549v1)

2+2+2=6，真实知识缺口深入必要审阅完成，拟PLATFORM-EVALUATION-SYSTEM Ch66总体质量估计分支，待非作者采用/未写。HTML404后实际官方PDF-v1物理3–9页必要理论/方法/评价/限制已读，不作为正文受阻。源总体组残差能按旧权重抵消，新群体组权重改变后残差重新出现；若条件误差在可重加权各组均为零、目标支持重叠且P(Y|X)稳定，平均预测通过塔律得到目标prevalence。多重校准是更强条件，有限MCGrad拟合不自动取得全feature/任意未来分布保证，classifier AUC高不证明总体估计无偏。

Ch66现代表性人工残差校正及TPR/FPR约束MLE没有明确这个“旧总体残差抵消→再加权失效→条件残差校准”的具体支路，拟两段接在总体estimator现文中，而非导入政治/公共卫生应用。ACS约644k校准与CAP约13.4k、ClaudeOpus4.6/30k文本两campaign，AppS2 Llama70B是补受限配置；within-support与新documenttype OOD方向不同，probability输入有时弱于binary+metadata。人工标签、分组复杂度/新support与concept drift仍需重新校准，校准不是免费且不存在任意shift universal guarantee。hardware/precision/servingbatch/concurrency/SLO未披露；官方abs-v1同题、Submitted04/23T11:23:34Z，处理原字段与官方赋号/slot/邻批联合推08–09。未复现，未扩读非必要应用附件。

## [2604.21570 SpecSyn: LLM-based Synthesis and Refinement of Formal Specifications for Real-world Program Verification](https://arxiv.org/html/2604.21570v1)

2+2+2=6，纠错深入必要审阅完成，拟窄争议/暂缓，待非作者核。实际§3.2–3.4/Algorithm1、§4–6：AST依赖SCC分段/POI后序，verifier拒绝候选后修复，未被当前spec区分的mutant作为细化上下文。Algorithm1保留原程序可验证候选是合理；但§3.4更新式从新增集合减去在mutant上被refute的spec，恰移除了能区分mutant的候选，与本节优化VDR目的及Algorithm1另一过滤对象不一致。仅隔离这个印刷递推/中心保证映射，不能称整算法无效。GCC-O2 binary不同不证明程序语义非等价，verifier未证明也不一般等于语义false，VDR只能是给定变体/solver合同下信号。

50文件14库、人工ACSL参考、Frama-C/WP25、GPT4/5/DeepSeekR1、repair/refine各5与t.75。Precision是verifiability、Recall是人工reference覆盖，1071/1365只为给定targets，不是所有NL需求。§5受限消融/不同RTE baseline保留，§6平均3.62h对1.42h不采便宜/全自动保证。Ch66 compile→mutation与任务spec完备性分权已有原则，但不解决本打印递推冲突；本轮不写Books。重开需作者澄清正确递推/实现过滤集合及“不可证明/不成立”和non-equivalent判据，不需要更多benchmark。官方abs-v1同题、无撤回说明；Submitted04/23T11:46:19Z与官方slot/ID/邻早处理簇有据推断08–09，未复现。
