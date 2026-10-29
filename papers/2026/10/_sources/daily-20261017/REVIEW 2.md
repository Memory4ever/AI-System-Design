# Daily 2026-10-17 — 独立复核

复核者：`live1017_reader`（非报告、Books 作者）。仅窗口北京时间 2026-10-16；历史补查暂停，不恢复。执行时间：2026-10-17 09:15 +08:00。本人仅维护本文件复核层，不改 README、Books、Learning State 或索引，不 stage/commit/push。

## R1 — 首批准入校准（六项具名样本）

已完整读本轮 `AGENTS.md`、研究合同、Report 合同、Research Prompt、来源使用说明/每日组/arXiv 主题、ROADMAP；核本日独立窗口。使用 using-agent-skills 选择复核流程；当前 checkout 为事实依据，旧历史 checkpoint 不构成本日验收。

实际日期依据：[CL recent 首50](https://arxiv.org/list/cs.CL/recent?show=50&skip=0)与[LG recent 首50](https://arxiv.org/list/cs.LG/recent?show=50&skip=0)，均显示 Fri, 16 Oct 2026；CL 当日177条、LG306条，未将后续宽列表变成逐项审阅队列。仅定位以下六身份：CL #3/#19；LG #2/#4/#10/#13。未核其余条目，不称全量验证。`/new` 返回 Oct14 缓存，LG `/new` 错误，均不用作本窗证据。六项当前官方 abs 页均只有 v1，未见官方撤回/纠错/安全标签；Oct15 submitted 记录只用于精确版本身份，不当作公开日。

| 身份/官方原件 | 实际读法与具体准入判断 |
| --- | --- |
| [2610.22353v1 Routing Exploration](https://arxiv.org/abs/2610.22353v1) | 完整题摘。共享路径使路由改动难以影响表示，同时细粒度专家扩大组合空间；提出 mirror-selection 与原概率 aggregation 分责，可能修正“更多组合自然兑现容量”的判断，准入。不是凭 MoE 主题关联。 |
| [2610.22256v1 BitSparse](https://arxiv.org/abs/2610.22256v1) | 完整题摘。重算/有损缓存之外，利用 ReLU 精确零值压缩保存状态，并以 device buffer 避免变长分配的 host 同步，形成具体 memory/runtime 分支，准入。 |
| [2610.22273v1 Librarian Agents](https://arxiv.org/abs/2610.22273v1) | 完整题摘。外部语料在 query 前构造成跨查询复用文件系统，以下游效用训练 builder；改变查询前后计算分工，准入，不把 MDP 命名本身当新机制。 |
| [2610.22314v1 MindEval2](https://arxiv.org/abs/2610.22314v1) | 完整题摘后定点读 HTML §2–4.3/Limitations。不能称“只扩题集”：模拟用户过度合作造成评价盲区，先工具提交 move 再 verbalize，并对真人/原 simulator 校验保真，足以准入核验评价边界。rubric、临床排名与一般记忆组件本身不足以单独准入；领域名不排除 LLM 评价贡献。建议 2+1+2=5；具体采用与 Books 决定尚待。 |
| [2610.22336v1 Dynamic Treatment Regimes](https://arxiv.org/abs/2610.22336v1) | 完整题摘，确有 robust contextual MDP（patient 为 hidden context），不虚写“无机制”。增量与验证是生物标记误差、疾病转移与癌症治疗模拟策略；未建立模型能力形成或 foundation/LLM 系统选择的直接贡献，按项目范围排除，不评分。 |
| [2610.22110v1 Nawatl NMT](https://arxiv.org/abs/2610.22110v1) | 完整题摘，承认 variant fragmentation、syntax plaintext prefix 复用 embedding 的具体设计，不按传统 NLP 标签排除。但证据围绕单变体 mT5/LoRA specialization、领域语法 analyzer、backtranslation 与现成 int8 部署的组合，未建立改变主线设计的可迁移机制/边界，具体贡献排除，不评分。 |

校准结论：前三与 MindEval2 可继续证据审阅；后两项排除有效。没有以局部实验、未披露详情或 Books 已覆盖倒推排除。校准不是 Source、Books POST 或 DAY 通过。

## R2 — 三项必要 Source 与具体 owner 比较

以下仅通过明确限定的必要原证；未核代码、复现实验、GPU 运行或生产能力。建议评分供报告作者独立确认，不因工作量调整。

### 2610.22353v1 — 受限 Source 通过；owner 差额明确

[精确 HTML](https://arxiv.org/html/2610.22353v1)：§2–4、Eq3–6、Def3.1、Props3.2–3.3、B.1/B.3/B.5–7。建议 2+1+3=6；因实际 owner 差额读到直接反侧。

采用界：混合正/负 logits 的概率只选支持集，aggregation 仍用原概率；低原概率专家仍执行，仅功能贡献被压低，不能称减少真实激活、通信或 FLOPs。rho anneal、modified balancing 是配方的一部分。H100/DCLM/seq2048，100M–2.4B；无共享组的 GPU/EP/global-batch 不同，不能把全部质量差唯一归因共享专家；理论 variance 上界用归一化 Z，实验 Z=1，不将定理搬作实验保证。B.6 有持平/反退，保原 Top-K 路线；dtype/质量重复不确定性未充分披露。

具体 owner：`MODEL-MOE` Ch21。已读“扩大容量…/Shared-first”与“选择支持集与输出贡献权重分别控制”完整局部；已有正文承载共享瓶颈、有效支持度与分责，但没有 shared dominance→探索可辨识度→反向概率选择、原概率聚合的训练期分支。可在既有支持集/贡献权重讨论附近小幅整合，不重复容量总览；不是新结构节点。本人不写 Books，逐字 PRE/POST 由 root 另核。

### 2610.22256v1 — 受限 Source 通过；owner 差额明确

[精确 HTML](https://arxiv.org/html/2610.22256v1)：§2–4/6、C.2、D.1/D.3/D.4、E.6–7，存储精确式与主要反侧实读。建议 2+2+2=6；具体缓存语义差额深入。

采用界：mask/compact positives/tile prefix 保存 ReLU 支持及值；ReLU² 存未平方值；无损限所选 storage dtype，FP8 不因此相对 BF16 无损，dense forward 不变。TensorBuffer 必须按 step reset 并容量足够，不授 overflow guard/分布式正确。31/30% 是无 optimizer、无持久全梯度且不更新参数的 F/B slope，不是完整8B训练总显存。完整3350步 NanoGPT 同 microbatch32 实为7.668 vs7.428秒（约3.2%慢）；不能采用普遍≤1% overhead。checkpoint 在低稀疏度/LLM测量中仍可更省；sign packing 多一层费用。RTX3090/5090、seed0、五次计时；端到端 SLO 不适用。

具体 owner：`TRAIN-PRETRAINING` Ch28 “Activation checkpointing 移动了什么瓶颈”已读完整邻接：保存/重算、状态类别与在线 rematerialization 已有，精确结构零的缓存编码分支未有。Ch36 “Activation Compression 必须服从 Operator 语义”实际承载有损线性误差合同，不宜在此重复推导本地无损缓存；Ch28 可加入条件分支并保既有 checkpoint 的适用性。无新分布式机制，不以 GPU kernel 名称把 owner 移到 Ch49。

### 2610.22273v1 — 受限 Source 通过；owner 差额明确

[精确 HTML](https://arxiv.org/html/2610.22273v1)：§2/4、A.1–A.8 必要方法、对照、结构干预、费用与配置。建议 2+2+2=6；因具体持久派生 state 差额深入。

采用界：query-hidden builder 创建/合并/删除 synthetic（不可删 raw），固定 answerer 消费文件/原源；主跑每8 turn probe加terminal，三费用系数实际全0，不能称已优化成本目标或精确 dense-reward 等价。680/50任务，4B builder、固定35B-A3B executor及compactor均有费用。扩展443题的0.64/0.24不得混成原50题0.77；A.5 flatten质量相近、导航更贵，shuffle伤质量；raw token仍高，归一后成本不是总token更少。静态corpus，更新/规模未解决，引用fallback仅个案。

具体 owner：已读 Ch75 当前call-visible定义、Ch77 state边界/Construction-vs-Retrieval/constructor credit与marginal reward局部。持久跨query的派生 filesystem 属 `AGENT-MEMORY` Ch77，不是当前 Context assembly；已有 credit/lineage 原则不等于已有“query前一次构造、query后复用”的完整机制。可在 construction policy 邻接小幅整合；不重复marginal-reward推导，不把QA reward当事实authority。实际拟文与写后尚未核。

## R3 — MindEval2 必要标准 Source 与已有覆盖

[2610.22314v1](https://arxiv.org/html/2610.22314v1) 已定点实读 §2–4.3、§5必要设置/限制、Appendix G 的 memory ablation。5分（2+1+2），标准审阅完成；不为临床排行榜扩读47页全部附件。

准入命题收窄为：不合作行为覆盖、simulator fidelity 与最终回答质量应分别验收；tool commit_move→verbalize 是本研究采用的受限 steering 实现，不因整体拟真改进就取得唯一机制归因。原文只称 preliminary direct-prompt 对照，没有足以单独认证工具拆步因果收益的主消融。§4.3 的真人参考、相同100 profiles 的 baseline、盲专家真实度标注与分布统计支持局部评价边界；专家一致性/样本和1app英语first-session限制保留。评分严重度权重是约定，不是校准的harm比例；3-model judge排名一致不认证全面judge正确。共享memory的效用不等真实度，memory消融不补纵向真人验证。

实际读 `PLATFORM-EVALUATION-SYSTEM` Ch66 “User Simulator 必须包含不合作与行为差异”完整正文与前后交接（当前1676–1688）：已有合作用户会高估稳健性、persona coverage、真实交互回退，以及realism/文字多样性/task outcome分别测量、human–proxy outcome gap和信息预算分账。它实际承载本项可采用的一般判断，不是仅标题相似；新增临床taxonomy、模型排名与具体prompt/tool组合仍为本报告局部证据。故本次可判**已有覆盖**，不新增 Books。未把原本有贡献的候选事后改成范围排除，不改变5分或宣称临床效能。root 可独读实际 owner 后确认这一具体NC；本人未写正文。

## R4 — 同日追加六项具名必要复核

仅按 root 指定六身份定点处理，不扩发现。六项完整官方题摘已读，均准入；其中 22263 是 regularized IS 后 covariance estimand/两种中心化的具体边界，22316 是可学习 when/how 干预分责，不以“理论note”或“Agent组合”关闭。LG recent FriOct16 首50中的 #6/#11/#19/#31/#32/#34 已定位，abs 当前均 v1，未见撤回/纠错；submitted 不替代公开日。R2/R3 未变层复用。

### R4.1 — LCT 2610.22179v1：受限 Source 通过

[精确 HTML](https://arxiv.org/html/2610.22179v1) §3–6、A训练测量/A.3–4、B.1–3必要存储和失败边界。建议 2+2+2=6，因实际训练表示差额深入。固定 bounded exponent codes/escape 与不变 sign–fraction byte 保 BF16 bits；sampled center 不是全分布在线拟合，codebook/center/stream预算/overflow tail 共同构成表示。GEMM仍还原dense；融合pointwise减少重复memory traffic，不证明全训练更快。allow_raw 只看fixed payload/padding，不防overflow后膨胀；arena需容量、连续空间/碎片与live-state生命周期，进程内只计arena一次。量级变化的entropy界有rounding/range条件，不认证任意分布。RTX3090、BF16/Muon、batch1 Qwen峰值及五optimizer-step测量（warmup后，不含保存/validation）；3.5倍只是所测500–3500序列网格的可行点比，不是精确最大context。NanoGPT全3400步质量不变是局部记录，memory/time是短测，保7–9%运行代价。

Owner：已实读 Ch28 activation checkpointing完整邻接及mixed-precision状态局部；`TRAIN-PRETRAINING`。既有低精度/重算与R2 BitSparse的结构零都不承载“非稀疏BF16指数的反复encode-decode”机制。与BitSparse在同一memory分支合并组织最小新增，不重复到Ch36或量化执行Ch49。

建议最小拟文（待 root 逐字 PRE，非 Books 已写）：

> 不依赖精确零值时，也可以保存 BF16 的原始 sign–fraction byte，只对集中分布的 exponent 做有界前缀编码；稀有值走 escape，超出固定 stream 预算的尾部保存原字节，使分布失配首先改变容量和编解码代价，而非主动量化误差。训练与静态权重推理不同：权重和 optimizer state 需逐步重编码，saved activation 又跨 forward/backward 存活，因此必须把 encode、decode、融合pointwise与overflow/live-buffer一起计费。Dense GEMM仍要可消费操作数，采样center只适应量级，不能消除任意分布漂移、padding或碎片。原源在少量模型上以约7–9%单步代价换局部memory headroom；低冗余、短tensor或容量无法验证时，dense保存、重算和已验低精度仍更简单。

### R4.2 — Fidelity/Consumability 2610.22016v1：受限 Source 通过

[精确 HTML](https://arxiv.org/html/2610.22016v1) §2–6、A–F必要probe、anchors、干预及配置；建议 2+2+2=6，因Ch82兼容性差额深入。实际支持同Qwen2.5-1.5B split-context/SQuAD、8token greedy、n200的cosine排序与真实消费排序可相反，且替换/附加是不同readout实验；floor/native reference是实测锚，不是数学界。拟合reader目标的桥在负结论外；source-only全局不可能/普遍softmax障碍不采用。部分trained sweep在正文措辞和“未拟合桥”范围间有张力，故只采用可直接核验的同模型扰动、放置与行为对照，不把此分类提升为否定所有training bridge的定理。F中不同adapter的negative-control也不同，不采用单调优劣。

### R4.3 — Carrier/Fusion 2610.22026v1：受限 Source 通过

[精确 HTML](https://arxiv.org/html/2610.22026v1) §2–4/A.1–6必要方法、控制、兼容及反侧；建议 2+2+2=6，因同owner接口差额深入。与22016同作者/大量同probe结果，不算独立复现。KV augmentation主阳性q/k/v rank16而非只训q；activation replacement得oracle fact span和swept layer，非部署查找。carrier两侧anchors/n/conditional分母不同，不用0.742等作直接胜负或严格等价。深层错配control上升，采用浅层clean band；同权重多passage pool不等多模型，近checkpoint heldout有局部lift，稍远及跨family均失败，三点不定义通用兼容半径。改attention有作者parity/rebuild检查，不等本人核实现。

两文共同Owner：`AGENT-MULTI-AGENT` Ch82。已读“通信可以压缩成latent…”329–399/“Latent Communication只能压缩Payload…”431–451及959–964完整局部；已有身份/变换/错配审计，但没有carrier×fusion耦合与oracle对齐分责。建议合一小段共同论证、分别source-family标识，不复制两段同结论或新增节点。

建议最小拟文（待 root 逐字 PRE）：

> 几何接近还不能证明state可被当前reader消费：同一probe里，更高cosine的扰动cache可能比稍远的原生cache更差，因而兼容性必须以实际receiver行为及no-op/错源对照验收，而不只优化重建误差。还要把carrier与注入点一起选择：保留receiver自身KV并附加同坐标来源，与覆盖其KV不是同一接口；在正确fact位置和layer已由oracle给定时，直接替换残差activation又可能比附加更有效。后者是对齐正确后的consumability测量，不是线上定位机制。两项同源小模型研究不证明任意模型可互换或所有训练bridge失败；附加state、adapter、训练/校准、attention与恢复均付费，错源control、模型revision或坐标不能闭合时仍回到typed/text message和receiver自己的state。

### R4.4 — Selection Is Not Learning 2610.22029v1：受限 Source 通过

[精确 HTML](https://arxiv.org/html/2610.22029v1) §3–6、B.1–4、C.1–2采用条件、F/G必要对照与预算。建议 2+2+3=7。准入增量是task admission≠realized update value、选recipient/吸经验/确认final三种责任，而不是“更多自训练轮”。保archive可独立于权重接受；recipient teacher固定、repair有reference/keep无reference，同前缀forward-KL，不是直接继承donor参数。fresh confirmation只测已冻结final proposal，拒后不重试recipient；经验零阈值不享正margin/sub-Gaussian定理风险界。NLL audit不当accuracy、acquire与forget分账；低budget Full反侧及verification共错保留。2×RTXPRO6000/96GB、三seed/十轮，accounting units非GPUh/FLOPs；construction等全部费用不被“同轮”消掉。

Owner：`TRAIN-GRPO` Ch33 “Verifiable Reward 不等于每个样本都可学习”2464–2472完整邻接已读：当前正文只到sample admission/gradient方向，不拥有冻结实际successor的独立接受与经验/参数继承拆分。Ch77持久experience/独立gate一般原则不能替代训练state的选择责任。本次可在Ch33该节末单段最小补全，不将archive搬成Memory新架构。

建议最小拟文（待 root 逐字 PRE）：

> 当训练按轮从自造任务产生候选模型时，还要在sample admission之后验收已经发生的参数更新：同样可验证、看似可学的任务并不保证successor相对root获益。先冻结候选并选recipient，若再吸收当前/归档experience，则必须冻结吸收后的final proposal，再用与筛选和训练分离的新probe成对决定继承或保留root；不能复用把winner选出来的噪声作为接受证据。合格experience可继续保留而不继承donor参数，repair与preservation则按当前recipient的失败/成功重新分组。这增加分支、teacher、verification、确认和完整state恢复费用；原研究的零阈值仍会错收坏更新，正margin界另依赖条件无偏与sub-Gaussian等假设。预算或probe资格不足时保留固定数据/单路径训练与独立阶段验收，不把task通过自签为模型进步。

### R4.5 — Policy Gradient Baselines 2610.22263v1：受限理论 Source 通过

[精确 HTML](https://arxiv.org/html/2610.22263v1) §2必要IS对象、§3.1–3.5的估计器/证明与§4总结，建议 2+1+3=6；因当前estimator知识缺口深入。独立同prompt完整rollouts、G>1、所需矩/终止条件已核；regularized ratio的covariance是另选estimand，不能称无偏恢复true PG。Sequence真目标与token的old-occupancy surrogate不同；sample/known population mean不能混用，组std/PPO signed min-clip/自适应baseline不在给定恒等式里。Token conditional mean按prefix变化，group reward mean不能消掉其累积项；f=id才消该额外差额。理论无实测，不能承诺真实LLM训练收益；有限词表求均值可行不等免费，也不能由样本估计自动继承known-mean无偏。

Owner：`TRAIN-GRPO` Ch33。实际567及其前后、2768–2775已读：有LOO/self-inclusion与off-policy平移身份一般说明，但未给regularized sequence vs token centering的不同消项条件，可在group-relative gradient节567后小幅整合。

建议最小拟文（待 root 逐字 PRE）：

> Ratio一旦截断、mask或裁剪，importance-weighted score的期望通常不再为零，所以给reward加常数可能改变更新。将reward与weighted score的covariance定义为目标可以恢复平移不变性，但这不等于无偏恢复原policy gradient。对同prompt独立完整回答的sequence-level estimator，reward减group mean后，任何共同score常量都会相消，G/(G−1)只处理self-inclusion尺度；token-level的weighted-score均值却随prefix改变，累积后在不同rollout间不同，不能由同一group mean消去。后一分支需在所声明surrogate下按prefix居中；词表求和、rollout与均值估计都有成本，未知population mean、相关采样、group-std或PPO符号相关clip都须另验，支持不足时保留fresh、未正则IS理论对象与现有稳定recipe，不把代数相消当普遍收敛。

### R4.6 — Steering Agents 2610.22316v1：受限 Source 通过

[精确 HTML](https://arxiv.org/html/2610.22316v1) §3–4、A.1–4、B.1–3必要机制/成本/反侧，建议 2+2+2=6，因intervention credit差额深入。fast是yes/no logits加soft Bernoulli threshold，不是校准drift真值；rank target为绝对outcome change，有害干预也可高rank。slow相对G actions+unsteered pooled mean，正A不保证高于unsteered outcome；共享backbone不等独立无干扰优化。8B steering/7B frozen executor，35k/300steps；crossmodel/任务迁移是有限search范围。MAS zero-shot干预越多越坏；RL F1增而agent turns9.2→10.4/11.9，不授总费用下降。fast仍付同prefill，B.2在12并发/GPU的call latency不能当端到端SLO；dtype/hardware/多seed不充分披露。

Owner：`AGENT-REFLECTION` Ch80。实际“Learned Adaptation Policy”130–152、“Trajectory Drift Sensor…”157–164与“Critic Accuracy不等于Intervention Value”384–395完整局部已读：一般when/how和paired intervention gate有覆盖，但没有用conditional continuation同时训练priority/干预内容的实际credit边界。可在384–395既有论证中添一小段，不在Ch81/82重复Agent流程。

建议最小拟文（待 root 逐字 PRE）：

> 可学习的监督者还可以把“哪里有介入影响”与“哪条介入有正收益”分开训练：先从同一冻结execution state采样多个建议，并分别续跑有/无介入的分支，用结果差训练便宜priority gate，再让慢路径学习具体note/retry。若priority用绝对差，破坏成功的介入同样会被排高；若慢路径只相对含baseline的候选均值归一，正advantage也不认证它优于无介入。因此gate只拥有有限触发权，结果verifier、预算和workflow owner仍决定是否接受；soft threshold改变平均介入频率而非逐任务硬quota。原search实验中未训练监督会引入重复拒绝，RL也可能以更多agent turns换质量；共同prefill、全部续跑训练、慢推理和回退费用须保留，校准或预算不足时仍用no-intervention、规则guard和独立最终验收。

## R5 — 四家族实际 Books POST（非 writer，局部增量）

仅读实际保存的新正文、完整相邻论证及本人 Review notes，不重审 R2/R4.1 已有效原件。Ch28 `1188–1207` checkpoint 段及 `1684` 起本人 note 已读回：BitSparse/LCT 分别在保存/重算之间承载精确零编码与 BF16 无损编码；两段保留 dtype、buffer/overflow、dense operand、性能与回退条件，未覆盖 checkpoint/DTR 原机制，两个正文 marker 各唯一，**两项 POST 通过**。Ch77 `405–442` 及 `1846` 起本人 note 已读回：Librarian 位于事实记忆成本与 JitMem 之间，query 前构造、raw authority、主实验费用系数为零、flatten 对照及静态语料边界保留，与 query-conditioned 接口明确分责；正文 marker 唯一，**POST 通过**。

Ch21 `521–543` 及 `972` 起本人 note 已读回：MirrorMoE 正文的真实执行/effective support、共享路径对照、理论/实验归一化区别及稳定基线均保留，marker 唯一；但“增加采样”误导为随机采样（原机制确定性 Top-K），且新段插入后下一节“前一分支”不再紧邻固定系数机制。已通知 writer 改为路由概率计算与明确“前述固定贡献系数分支”；**本项 POST 待这两处保存后定点复读**，不倒退有效 Source。

## R6 — 关闭项分层负侧抽检（非全附件重扫）

独立完整读 [Name Bias 22053 当前唯一 v1 题摘](https://arxiv.org/abs/2610.22053)、[TagInsert 21862 当前唯一 v1 题摘](https://arxiv.org/abs/2610.21862)、[SITAR 21440v1 题摘](https://arxiv.org/abs/2610.21440v1)，实际官方页未见纠错/撤回提示。日期未另从 submitted 推断；这些贡献前关闭项不借此取得入选日期资格。Name Bias 新结果是给定名字配对/固定句式下的偏好分布，非 judge 排序污染；SITAR 是 ASR 严重度递归聚合与离线 LLM 监督的便宜回归器，题摘未给新的大模型评价失效接口。二者与 ROOT.md 具体关闭理由一致，不因领域名关闭。

TagInsert 初看具有去因果 mask、推迟困难预测的机制，故不能以小模型/标签任务或缺乏普适性直接关闭。只定点补读 [21862v1](https://arxiv.org/html/2610.21862v1) §2.1–3.3 与 §5.1–5.2 必要区别：文中明确承接已有 insertion/easy-first；新增是已知固定标签位置的 `<U>` 占位、随机 gold 插入轨迹、最高置信度填槽这一 tagging 适配。训练约按平均序长倍增，单 pass 自定义 mask 尝试未收敛；结果只修正有限 POS/CCG 数据/标签条件的比较，不把摘要概括成通用稀有类收益。关闭仍成立，但理由应改为旧插入机制的任务适配/局部验证未形成新的主线判断，而非仅要求基础模型普适证据。已向 root 同步；未发现要求重开全部关闭项的共同错误理由。

## R7 — MoE 修后与另五家族实际 Books POST 通过

非 writer 实际重读 Ch21 `521–550`：已保存“确定性地选择 Top-K”“路由概率计算”与“前述固定贡献系数分支”，R5 两处问题消除；前后分支责任清楚，**22353 POST 通过**。R2 原件与已通过部分复用，不扩审。

实际完整读 Ch33 group-relative 局部 `520–605`、sample-admission 局部 `2458–2492` 与 `2798` 起本人 note：**22263、22029 POST 通过**。前者将 regularized covariance 与原 PG 目标分开，sequence 共同均值与 prefix-dependent token 均值分开，未把 group std/PPO/样本均值套入恒等式；后者明确最终 proposal 冻结后以新 probe 接受、经验/参数分责和零阈值/假设风险。旧 LOO/self-inclusion 与可验证/可学习论证仍保留，未宣称普遍收敛或单调提升。

实际完整读 Ch80 `365–415`（critic/intervention 全节、新段至小结与本人 note）：**22316 POST 通过**。absolute priority 与有益介入、pooled advantage 与无介入增益、soft threshold 与硬 quota 均未混同；全费用与 turns 反侧保留，仍由 verifier/workflow 接受，不覆盖原 paired pilot 路径。

实际完整读 Ch82 `426–476` latent payload/identity 全局部至 reward-shaping 交接及 `1137` 起本人 note：**22016、22026 POST 通过**。共同单段载明 geometry/consumability、carrier/fusion、oracle 定位限制、q/k/v 与同源非独立复现；不同分母/anchors 不直比、不将负例升级所有桥失败。显式消息与 receiver state 回退保留，未改现有通信 identity/transform owner。

上述六家族正文 source-family marker 各仅一处，本人 notes 均位于现有 Review notes；引用精确 v1，原机制和章节交接未静默替换。四目标文件 `git diff --check` 通过。Notes 中“写后另核”只是 writer 待同步的临时状态，不构成另一项技术缺口；本记录给出既成 POST，未授 DAY/FINAL、运行或复现。

## R8 — root 指定 CV 首页 26 项完整题摘筛选（非 Source / 非 DAY）

范围仅 root 本轮具名 26 项，不补后页、不加日期。实际逐项打开以下官方当前 abs，完整读题名、摘要与当前 version/history；均显示唯一 v1，实际页未见撤回/纠错提示。这里不把 submitted Oct15 改写成公告日期；公开日落窗仍由 root 的 Fri16 CV recent 原证独核。本层仅给贡献准入及建议评分，不采用宣传数字，不声称方法/评价/owner/Books 已审。本人是本层初筛者，后续由 root 做相应独立校准；不把本人重复读回当独立 Source。

首批消息曾把多个新模块组合粗给 6 分，经 root 提醒已按实际新增命题重校：不是有命名模块即长期贡献，也不因摘要实验细节少而排除已经明确的机制。P3-WAM 从初步保留改为下面具体关闭；其他分数以本表为准。多数是局部模型机制 `2+1+2=5`，跨训练/推理或 evaluator/reward 接口才计 Reach 2；没有因联想多个章节授 Reach 3。

### 明确具有待核验具体增量的 20 项

| 官方题名/身份 | 原约束 → 题摘实际增量 → 可能改变的选择（非已证结论） | 建议 Delta+Reach+Durability |
| --- | --- | --- |
| [22371 Gen4P: Video Generators are 4D Perceivers](https://arxiv.org/abs/2610.22371) | 视频生成先验通常经迭代去噪消费 → clean latent 单次 encoder、轻量 cross-attention 按需预测 4D 属性，连续时间 query，冻结 depth LoRA → 是否可用同一生成预训练底座提供前馈几何查询而非再跑生成循环。不是因 tracking/depth 新榜单准入。 | 2+1+2=5 |
| [22370 Which Tokens to Merge? Diffusion Dynamics for Efficient Image Generation](https://arxiv.org/abs/2610.22370) | 按 prompt relevance 保护前景会漏掉未提及结构 → Tweedie clean estimate 的跨步变化与局部高频共同决定 anchor/merge → 合并资格应按未解决动力学和结构，而不只文本对齐。 | 2+1+2=5 |
| [22369 SoftCache: Adaptive Step Size Caching for Diffusion Transformers](https://arxiv.org/abs/2610.22369) | staleness threshold 只作 refresh/reuse 开关且步长固定 → headroom 决定 cached step 跨多节点或逐渐缩小，允许离开固定 grid → cache policy 与 numerical sampler 步长需联合选择。速度数字未核。 | 2+2+2=6 |
| [22360 Grounding Generative Verification in 3D Content](https://arxiv.org/abs/2610.22360) | 多视角表观变化不能直接当需求违反，decision accuracy 不能认证拒绝解释 → controlled specification/candidate edits、value/target-binding 分类与 linked counterfactual 反馈 → verifier 要验反例响应及解释定位，不只外观/榜单。Oracle selection 与人工 refinement 不等自动系统能力。 | 1+2+2=5 |
| [22356 DK-VLM: Geometry as Position for Spatial Reasoning in Vision-Language Models](https://arxiv.org/abs/2610.22356) | 重建 feature 融合会破坏有限空间监督下的语义对齐 → 原生 semantic kernel 保留，另用点位移/相对相机变换的 geometry kernel 与 learned gate；逐步 reference-frame composition 监督 → geometry 可作为位置调 attention 而非必须进 feature 内容。 | 2+1+2=5 |
| [22347 Speculative Forcing for Efficient Autoregressive Video Generation](https://arxiv.org/abs/2610.22347) | 每 token 都付满 denoising steps → 中间 clean estimate 作 draft，逐 token verifier 决定冻结，已冻结 token 不再去噪但 KV 仍可供未结束 token → token 完成与上下文可见性可分责。题摘未证明分布精确。 | 2+2+2=6 |
| [22343 GeoState: Learning View-Decoupled Geometry States for 3D World Modeling](https://arxiv.org/abs/2610.22343) | GFM state 的视角变化混入场景动力学 → 多视角 feature 聚成 scene state、camera-ray query 解码，camera motion 单独预测且 rollout 沿用同一尺度 → world state 与 observation/camera 可分开建模。非仅驾驶数据集提升。 | 2+1+2=5 |
| [22328 ACEdit: Stable Multi-Turn Image Editing via Asymmetric Conditioning](https://arxiv.org/abs/2610.22328) | 自轨迹训练暴露 drift，却使原 ground truth 不再对齐 → student 连续消费自己输出，teacher 仍锚原图并读复合编辑指令 → on-policy 蒸馏两侧不必共享同一污染输入，需重新选择监督锚。 | 2+2+2=6 |
| [22321 AVC-Reward: Event-Centric Audio-Video Consistency Evaluation](https://arxiv.org/abs/2610.22321) | 沿用简单单向任务的 whole-clip score 不能分清多事件/多层音频/非对称关系 → 分离事件后独立分析、跨模态核关系，汇 narrative/temporal/attribute 三层 → 是否须以 event/relation 为测量单位而非单个整体相似度。准入仅针对这个盲点；新 benchmark、human alignment 数字和 RL gain 本身不授长期贡献，待 root 独核是否有具体反证。 | 1+2+2=5 |
| [22311 Velox: Spatial Memory Makes World Models Efficient](https://arxiv.org/abs/2610.22311) | 历史 KV 增长带来 chunk attention 开销，几何不确定区不能硬删 → frustum slab overlap 仅在 covered 区调 model-derived route，未覆盖区保留原 route；固定块对应 tiled attention、geometry 与 denoise 同 GPU 异步 → 几何资格、模型信号与 kernel 粒度共同约束稀疏执行。 | 2+2+2=6 |
| [22282 Routing Policy Optimization for Online Diffusion Reinforcement Learning](https://arxiv.org/abs/2610.22282) | score-function RL 常改 sampler 为随机轨迹 → stochastic attention route 作为探索 action，围 dense velocity 的 likelihood 训练，pair 只换 routes，测试恢复 dense/原 sampler → 训练探索接口不必等于测试采样器随机性。估计器正确性/成本待核。 | 2+2+2=6 |
| [22276 MJev-Spatial: System One Spatial Intelligence via Native Attention Matching](https://arxiv.org/abs/2610.22276) | 紧凑选择/数值/点输出仍为 AR 文本与 parsing 付费 → 用原生 q/k 为候选打分类分，值区间/图像区域 coarse-to-fine，全 stage teacher forcing 单 pass → 输出接口和训练阶段可按有限决策空间构造而非默认生成 token。 | 2+2+2=6 |
| [22267 Beyond Pairwise Repulsion: Collective Diversity via Determinant Maximization in Diffusion Sampling](https://arxiv.org/abs/2610.22267) | pairwise distance 不必认证整个 batch 有效维度 → 初始 noise 优化 one-step Tweedie prediction 的 RBF Gram logdet，加 fidelity anchor → diversity 目标应测集合体积而非只逐对排斥。新目标而非 synthetic-data 指标本身准入。 | 2+1+2=5 |
| [22264 SCOPE: Semantic Bounded Credit Optimization for Prompt Engineering in Text-to-image Generation](https://arxiv.org/abs/2610.22264) | image outcome 对每 subword 同粒度消费，可能切断对象/数量/关系整体 → rewriter 同产 prompt+semantic partition，span 内 pooling logprob shifts，共同 coefficient、completion 仍单 advantage → 不加 render/span reward 也能改变 update weighting 粒度，须区分结构先验与新 truth。 | 2+1+2=5 |
| [22217 Skill-Decoupled On-Policy Expert Distillation for Unified Vision-Language Models](https://arxiv.org/abs/2610.22217) | 混合能力 RL 有冲突，直接专用 reward 又会混入 hacking 偏差 → 独立专家提显式 skill，仅 teacher supervision 可见，student 的 on-policy 输入不见 skill → 专家技能外显与学生输入/推理依赖可分离，不能把带提示专家分数直接当统一学生能力。 | 2+1+2=5 |
| [22200 OpenGCUA: Toward a Fully Open Stack for Generalist Computer Use](https://arxiv.org/abs/2610.22200) | GUI-only batching 与固定 harness 状态决策限制中间反馈 → agent 可在 visual/programmatic 接口中决定观察/动作，code 中间结果控制后续，选定 harness 观察/任务状态决策迁至 model → 需重选模型/harness 分责及可审计状态界面。开源与榜单分不单独准入。 | 2+2+2=6 |
| [22075 Retrofitting Recurrent Vision-Language Models from Pretrained Backbones](https://arxiv.org/abs/2610.22075) | depth recurrence 能减存参但破坏已有 VLM 对齐 → 先剪/循环已有 VLM，加 recurrence adapter，language recovery→projector alignment→visual instruction recovery，并比较 recurrent LM 后转 VLM → retrofit 的顺序/恢复对象是具体设计选择，不能从存参下降推延迟下降。 | 1+2+2=5 |
| [22070 Memory as Weights: Internalizing Long-Term History for Streaming Videos](https://arxiv.org/abs/2610.22070) | 检索/压缩历史仍占 current context → recurrent HyperNetwork 逐步写固定大小 LoRA，历史权重/current observation 输入分离 → streaming memory 可改存储接口，但遗忘、更新/归属与费用须核，不能因固定大小授无损。 | 2+2+2=6 |
| [22060 FeaTok: Feature-Loss Tokenization for Image Generation](https://arxiv.org/abs/2610.22060) | pixel reconstruction fidelity 未必给 generator 易建模 token → 以重建冻结预训练 feature 替代 pixel loss，在多种 feature backbone 消融 → tokenizer 质量目标须回到下游生成可建模性/质量算力，而非以 pixel fidelity 自签最优。 | 2+2+2=6 |
| [21937 Flow-CLIP: Image-Conditioned Residual Scoring for CompositionalImage-Text Matching](https://arxiv.org/abs/2610.21937) | 句级 similarity 可满足同对象/属性却错绑定，也可借语言先验排 caption → 图像条件 token-patch evidence change 修全局分，同一 caption 正负对跨 matched/mismatched 图比较 margin → 绑定分的证据/监督要因图像而变，不能只校 global similarity。 | 2+1+2=5 |

### 贡献前具体关闭的 6 项（不评分）

| 官方题名/身份 | 承认的实际增量及关闭依据 |
| --- | --- |
| [22363 Perceive, Predict, and Plan: a Unified World Action Model for Egocentric Dexterous Manipulation](https://arxiv.org/abs/2610.22363) | 将手/相机 3D、动作条件视频和 goal planning 放入共享 base 的 mixture-of-transformers，模态适配/双向 attention/随机模态可见性合训，single-mode 与专用 baseline 对照。题摘目前显示既有多任务生成/masked-modality 思路的 manipulation 组合与能力提升，没有给超出组合的执行机制、模块收益新成立条件或原判断反证；不能因三个功能或世界模型标签自动准入。初步保留在此改判，非因 Source 工作量。 |
| [22341 3DCodeVerse: Exploring 3D Worlds as Code](https://arxiv.org/abs/2610.22341) | 可执行 3D code/资产/环境/验证记录的数据，加多 agent DAG、执行/空间测量/视觉反馈迭代和 component study。完整题摘没有指出区别于现有 executable-artifact/harness 的新控制或验证边界；新语料和领域 win rate 本身不足，非因 3D 领域名排除。 |
| [22240 MMSearch-OPD: Easy Made Hard, Hard Made Learnable for Long-Horizon Multimodal Search Agents](https://arxiv.org/abs/2610.22240) | 参数化加深已有 image-question 推理链，联合 answer RL/behavior penalties 与 reward-gap 调制 OPD、指数退火。承认有具体权重 recipe；现题摘仍是已有 curriculum/on-policy teacher feedback 的任务组合，只报告分阶段指标增益，未给会重选既有主线机制的独立新条件/反证。 |
| [22232 WaveLLM: Wavelet-Domain LLM Entropy Modeling for Lossless Image Compression](https://arxiv.org/abs/2610.22232) | wavelet subband 将流分得更同质，value embedding/coefficient head/任务 prompt 接 Llama LoRA，含同 wavelet 的 PixelCNN 对照。新增集中在 codec 的既有变换与 LLM 适配组合及码率，没有说明新的基础模型形成/运行机制或可迁移边界；不是因为“压缩”或小模型排除。 |
| [22182 LAMP: Layerwise Adaptive Mixing of Predictors for Training-Free Few-Shot Vision-Language Adaptation](https://arxiv.org/abs/2610.22182) | 多层 global/regional kernel predictors 在 class-score 空间混合、验证标签选择、cached exact residual update，免去异维 feature projection。承认利用中层特征与明确验证成本的局部实现；当前新增仍为既有 kernel/预测集成的 few-shot 分类配方与局部准确率，没有形成新基础模型知识边界，不把 training-free 当零监督。 |
| [21918 BridgeAfford: Bridging Query-Target Gap for Generalizable 3D Affordance Grounding](https://arxiv.org/abs/2610.21918) | 跨物体几何相似交互区域对齐，加 2D affordance attention 引导 query，改 unseen-object 泛化。题摘只支持 affordance grounding 中既有 alignment/外部证据汇聚的组合及两个数据集提升，未提出超出此适配的模型系统新机制或判断反证；不是仅因机器人标签关闭。 |

以上关闭理由与新候选均待 root 独立准入校准；后来若有具体反例只重开受影响项。没有任何项因已经有 Books owner、Source 费时或网络受阻而关闭。R8 不授权全体展开全文，也不预签候选日期、Source、Books 或本日完成。

## R9 — CV 指定七项必要 Source 与 actual owner（持续分批，不写 Books）

本层仅 root 指定 22371/22370/22369/22360/22356/22347/22343；本人为 Source 初审者，root 需独立核对应采用命题。R8 题摘与当前唯一 v1/无可见纠错层复用；未核实现、逐图像素或复现，后续 PRE 只是建议，不等实际整合。

### R9.1 Gen4P 22371v1：标准 Source 通过，Ch23 最小 PRE

[精确 HTML](https://arxiv.org/html/2610.22371v1) §3.1–3.4、4.1–4.5/T1–4。5=2+1+2；因 Ch23 生成先验到感知接口的具体差额读必要消融。Wan2.1-1.3B clean latent、末 scheduler time/空 text、final block features；VAE/DiT 冻结但 4D LoRA rank512 有 0.70B 可训练参数，decoder 0.18B，不能把“LoRA/单 pass”写成零适配或微小总成本。连续时间是 clip 内归一位置的两个端点 embedding 插值，不是物理时钟或任意时长可靠性；49-frame 训练，有限测试至105。Depth-LoRA 只是不增加可训练参数，仍有历史深度训练/驻留；主结果不是所有 depth/pose 切片胜出，Sintel depth 的双LoRA局部反退也在。200K/11数据、8H200/75Ksteps/b32；dtype、多seed、完整延迟 Not Disclosed，未用 headline 证明实时或模型先验唯一因果。

Actual owner：`MULTIMODAL-REPRESENTATION` Ch23。实际完整读 1730–1757 perceiver 与下一节交接、1128–1203 时间/空间身份局部；现正文承载可复用 VLM→LLM perceiver 与时钟/query身份，但未承载生成 DiT clean-feature→多头几何 query 的不同 consumer。不是 Ch25 transition：原文重建输入视频，未取得 action-conditioned future/world truth。

建议在“可复用 Multimodal Perceiver”两段之后最小补一段（待 root PRE）：

> 生成预训练的主干也可以改作感知 encoder，而不在部署时继续执行生成循环：把 clean video latent 送入冻结主干与受训 adapter，一次提取 scene tokens，再由独立 query decoder 读取指定位置和 clip 内时间，回归几何与运动。这改变 prior 的消费接口，不把重建器变成可推进的世界模型。连续时间 embedding 只编码相对 clip 位置，深度 prior 也仍是派生知识；adapter/decoder 训练、特征驻留和每次查询都付费。有限长度、动态遮挡或几何回归失准时保留专用 GFM、真实几何监督与原帧回读，不由单 pass 签发实时性或物理真值。

### R9.2 DaTMe 22370v1：标准 Source 通过，Ch24 最小 PRE

[精确 HTML](https://arxiv.org/html/2610.22370v1) §3–4/T1–6、Appendix A/B与C必要超参/反侧及D。5=2+1+2。Temporal/spatial低分交集先作 source，高分交集是 protected set，但不足预算会从其余位置 grid-sample补 source，故不是所有被合并token均有“安全证书”。局部空间 nearest destination 合并，第一步无前一估计不启用。Clean-estimate变化只对完整轨迹终点的 pseudo-GT，与真实语义/最终无误差不同；Eq6/18依赖给定 deterministic update，flow式依 Euler，不授所有solver。PixArt10KCOCO、20steps/CFG4.5，FLUX35steps/guidance3.5；RTXPRO6000Blackwell，dtype/seed重复/完整timing边界未披露。PixArt同压缩率比CFG慢且TFLOPs更高；FLUX部分FID/LPIPS反侧，细grid可比dense更慢，激进压缩损结构，不采全指标最优或普遍加速。

Actual owner：`MULTIMODAL-GENERATIVE-PARADIGMS` Ch24。实际1455–1478完整两条成本轴与 conditional-refinement局部已读：已有 expert budget/可变patch布局及训练型接口，未承载无需重训的 merge资格必须同时考虑未收敛变化与未提及空间边界。这是生成近似策略，不另在 kernel owner 重复。

建议在 refinement 位置段之后、既有 latent-render 分支之前最小补段（待 root PRE）：

> Token 合并也不应只保护 prompt 相关前景：背景边界可能不参与文本对齐，却仍决定结构。一个训练免除的分支同时读取相邻 clean estimate 的变化与局部高频残差，先保护两者都高的位置，从较稳定、同质区域提出合并，再用局部空间匹配完成预算。该信号只是近似资格；补足压缩预算还会消费未同时满足低分条件的位置，不能称全体安全合并。估计、排序、grid 与 merge 都付费，同压缩率也未必比旧策略更快；复杂结构或质量预算失配时减少合并，保留固定 patch、原 token 与完整计算，不用文本相似度保持认证整幅结构无损。

### R9.3 SoftCache 22369v1：标准 Source 通过，Ch24 最小 PRE

[精确 HTML](https://arxiv.org/html/2610.22369v1) §3–5.4、A.1–4/AlgA.1.1与必要成本定义。6=2+2+2。沿 SeaCache 非负 staleness 累计的 headroom 设有界跳步，刷新仍取普通步；两个 fresh residual 按实际时间差线性外推并重排尾 grid，首 anchor 不外推、开头/大probe变化禁止跳。Headroom与reuse error仅 uncached FLUX经验相关，不是严格误差控制；beta按速度段变，非完全无设置。50Euler/bf16/b1/seed0；FLUX200/Hunyuan946/Wan100分层，H100NVL vs A5000不能跨backbone比延迟；Wan已将原UniPC改Euler。Matched近似速度band不是同一次exact运行；fidelity对同seed未缓存图，非真实quality全面正确，VBench分差小，消融PSNR有反胜。计时仅denoising-loop，FLOPs却含VAE，额外旧residual占内存；不照录3.5–6.9×为端到端SLO。

Actual owner：同 Ch24，完整1752–1794 cache-error/velocity段已读。已有轨迹校准、threshold refresh、predictive feature与anchor-reuse代数跳步；当前缺口是复用判定与 sampler step/tail-grid 的联合状态，而非再次讲“动态刷新”。

建议在 cache-error 首段之后最小补段（待 root PRE）：

> 刷新信号还可以决定复用状态推进多远，而非只决定本步是否重算：将阈值下的剩余 headroom 转为有界步长，在较可信区跳过部分预定节点，并按新的落点重排尾 grid；跨节点的 residual 估计须使用真实时间间隔，而非旧 step 编号。这同时改变 cache 与 sampler，是近似轨迹，不是严格局部误差求解器。历史 anchor、额外 residual、probe 和重排都计费，经验相关及同 seed 保真不认证语义或端到端服务收益；条件突变、步长或质量失配时缩短跳步、增加刷新，回到原 grid 与完整求值。

### R9.4 3D Verification 22360v1：标准 Source 通过，Ch66 No Change

[精确 HTML](https://arxiv.org/html/2610.22360v1) §3–5.5、C.1–3/D.3–4及H必要反侧。5=1+2+2。固定candidate换spec与固定claim换candidate构造linked pair/triplet；answer-only与correct-negative explanation联合计分不同，True不验解释。Qwen122B-FP8 reference-semantic Judge不见图且本身也是受测模型，300条human审计有双向错；故36.5%只是参考语义不符，不等全部客观无效解释。source-group排重与cluster intervals保留，少量motion-direction不稳，不能外推全3D智能。40input×16candidate oracle选择及8input人工递归不等自动verifier收益，更不认证fidelity/无缺陷。硬件/运行成本/多seed在所用评价未闭，不授部署性能。

Actual owner：`PLATFORM-EVALUATION-SYSTEM` Ch66。实际完整读1006–1015多view/depiction、2247–2282 verdict/semantic及3032–3060 target-change/invariance/解释效用局部。当前已要求几何与语义分验、same-verdict paired语义反例、分别测目标改变/保持与解释/原答案能力。拟保留的长期命题均已有正文实际承载；新增3D题集、局部模型排名和人工选择上限留本日报，**No Change**，不是以同主题或 Source 费时关闭。

### R9.5 DK-VLM 22356v1：标准 Source 通过，Ch23 最小 PRE

[精确 HTML](https://arxiv.org/html/2610.22356v1) §3–4.5、A.5–8/A.10/A.12。5=2+1+2；actual gap而深入必要注入策略对照。Native semantic Q/K/V与mRoPE/causal mask保留；额外geometry-valid视觉token用full attention，text/invalid不进几何支路，不等全模型解除因果。Point/camera GTA分别作用子空间，融合projection独立于native，gate初值0.5而非零扰动。10%同数据/优化的A12显示直接替原position可能乱码，不能外推一切几何注入失败；main含RC/geometryloss，不把联合成绩归单kernel。238/338M trainable不含frozenGFM，32H200约11/10日；general MVBench、部分空间bucket及换frontend均有反退。RC四步是有限同构造测试，不等任意组合。dtype、多seed、完整推理延迟 Not Disclosed，不授低开销。

Actual owner：Ch23 `MULTIMODAL-REPRESENTATION`。完整1128–1203与1404–1493所需空间/几何交接已读（大段输出曾截断的1436–1471已补），1415–1417现有query-view投影2D位置，但没有保原语义路径、另设scene-point/camera kernel的替代接口。建议在这两段之后、混合rig段之前最小补段（待root PRE）：

> 几何也不必替换原生位置规则或直接叠入语义 feature：可保留原 attention 路径，另用估计 scene points 与相对 camera pose 构造几何 kernel，再按层 gate 融合。几何支路只在资格完整的已观察视觉 tokens 间交换，文本与缺几何位置继续走原路径；这不取消整段序列的因果合同，也不使估计位置成为真值。该分责增加投影、几何 attention、前端与训练费用；受限同数据对照中直接替换原 position 会退化，并不证明此双支路普遍最优或无遗忘。标定、坐标或质量不稳时保留原 attention、显式几何工具与原视图回读，分别验空间答案和一般能力。

### R9.6 Speculative Forcing 22347v1：标准 Source 通过，Ch24 最小 PRE

[精确 HTML](https://arxiv.org/html/2610.22347v1) §3–4.3、A/B.1–2及D.1。6=2+2+2。Token接受后输出冻结、其accept-step KV保留供active；chunk完成另做clean forward统一刷新history。因此混龄KV不等exact historical state，mean denoising steps排除了clean pass；FPS仅DiT forward、不含VAE，不能报完整生成实时SLO。Full-step reference是训练/校准oracle；learned gap/smoothing阈值并非在线真gap、分布精确或硬误差界。Frozen1.3B LongLive/Lingbot、1K训练、H100，5s/30s及200navigation场景；head4.11M/b4，dtype/训练完整时长未披露。阈值更松损质量，TF局部consistency下降；RPE逐segment独立Sim3，Drift是quality分数标准差，均非物理truth。匹配meansteps granularity对照支持窄差额，不采全控制安全。

Actual owner：Ch24完整1663–1752 commitment/cache局部已读。已有“未来稳定轨迹训练commit”与early-convergence≠confidence，但未承载连续视频中冻结输出/供其他token消费的KV/最终clean-refresh三状态。建议仅在“Commitment Policy可以从未来稳定轨迹学习”首段后添段（待root PRE）：

> 连续视频的提前结束还要分开输出与上下文：接受某个中间 clean estimate 后，可冻结其最终 token 并停止该 token 的后续去噪，却保留接受时各层 KV 供仍活跃位置读取；chunk 拼完再全体 clean forward，刷新给后续 chunk 的历史。此时 chunk 内 KV 来自不同去噪阶段，不是原 full-step 分布的精确缓存。相似/稳定 proxy 或受训 gap head 只提出接受，仍有阈值漂移与误锁风险；head、平滑、索引、缓存及最后 clean pass 都付费。Mean denoising depth 不含 clean pass，DiT FPS 也不含 codec；质量失配时收紧门槛，保留固定完整步数与统一历史刷新。

### R9.7 GeoState 22343v1：标准 Source 通过，Ch25 最小 PRE

[精确 HTML](https://arxiv.org/html/2610.22343v1) §3–4.5、A.3–4必要scale/训练。5=2+1+2。FrozenGFM→512×512scene state、camera-ray decoder另读视角；四state残差AR，不提供action-conditioned干预。Observed12images joint编码，训练future-prefix target不可改称部署未来已知；每窗observed FRONT LiDAR至少128有效匹配提供scale，并非纯RGB恢复米制。未来LiDAR只score，无target逐帧scale对齐。Sameworldmodel/data/训练的compression控制和camera-matchedCopyLast支持分责，quotedFR3D/原分辨率与targetalignment不同不宣公平架构因果。Contextencoder/pretrain+staticWaymo适配与dynamicworldmodel训练分账；rollout持续latent matching反而差，采用decoded-depth监督。有效overlap重投影一致不等全场景几何。训练200K+50K、world20K+35K/b36；硬件/dtype/多seed/完整延迟NotDisclosed，不授加速。

Actual owner：`MULTIMODAL-WORLD-MODELS` Ch25。完整216–246 ego分解、275–350 latent dynamics及672–707projective4D局部已读。已有解析ego/residual与VGGT early-feature预测，但没有view-decoupled scene query和one-step-state/rollout-geometry监督分责的具体边界。建议在303行VGGT-World段之后最小补段（待root PRE）：

> 不依赖解析 ego 传播器时，也可先把多视图特征聚成场景状态，仅在解码时注入 camera rays，让预测器推进 scene、另一接口提供未来 camera。要用 camera-matched Copy-Last 检查收益是否只是重查询旧几何，并区分可重建与可预测：受限对照里两种状态重建接近，未来预测却不同；one-step 用 latent matching 初始化有用，rollout 继续强配GFM target反而可能受其上下文变化污染，故可改以解码几何监督。固定尺度仍依赖观测期校准，重投影一致也只覆盖有效重叠，不证明 action 后果、完整世界或物理真值。前端、tokenizer/decoder、camera预测与训练均付费；尺度、视角支持或horizon失配时保留原观测、独立几何/短horizon预测和显式simulator。

R9 七项 Source 初审与六项最小拟文/一项NC已备齐；原件未变化时不重跑。其采用仍待root独立Source/PRE，未写Books、未授这些新增项POST或DAY。

## R10 — root 新保存 13 家族实际 Books POST 通过（非 writer）

本层复用 root 已独立核过的 Source，仅定点读 ORG_A/B 对应既有效 notes 的采用边界，再实际完整读新增正文、上下论证和本人 Review notes；没有重新打开原件，也不将此层冒充独立 Source。实际读取如下：

- Ch29 `35–72`、`436–473`、`1048–1080`与`1390–1400`：21633 ContextLift、21496 OPRD、22293 SST **POST 通过**。语境搬运不改 aligned target/保坏能力与coherent分母，teacher提醒寿命不等lossmask/TopK近似与刷新，双侧最终delta/anchor重定及rank非energy均保留；原安全配对、privileged teacher与旧gradient/mask机制未替换。
- Ch33 `279–311`、`759–797`、`2798–2813`：21671 PACE、22234 OS-Helix **POST 通过**。PACE明确正null项非full−null/去语言捷径，符号/均值不保完整gradient；Helix只说未clip标量中每action系数合计，未升级参数范数或joint IS，保Office/Workflow反退、GUI buffer/disk commit差异、旧GSPO回退。
- Ch66 `355–413`与`5070–5085`：22046 HiddenStateProbe、21561 DialFork **POST 通过**。报警/续跑值/定位分标签，读位置与rollout预算限制不被负probe掩盖；fork construction label与人审误差、独立turn max-match不授顺序感知、hindsight与online-prefix信息面分开。原internal sensor、TRACE三实验及下一邻接保持。
- Ch77 `107–145`、`161–196`、`1116–1143`、`1210–1260`与`1853–1872`：21739 RIKA、22196 Hy-Memory、21571 ToolGraphNegative、21900 TEM **POST 通过**。RIKA允许admitted退pending且canonical重建，模型计数/相关传播不认证真值；Hy-Memory gold归属非反事实、one-vote非等loss mass、完整bank续接/缺消融保留；工具图与额外探索/非等算力分账；完整版本组先于TopK，摄入序号不冒充valid time。原typed-state、poison、counterfactual credit、curated/procedural与双时态机制仍共存。
- Ch76 `672–713`与`1460–1473`：21731 RetrievedNotRead **POST 通过**。菜单可达/open/实际使用/claim支持分层，局部同页/重申干预不授open因果或全域恢复，摘要充分时不强制全文；上下可用工作集与sufficiency论证不被替换。
- Ch75 `568–612`与`703–716`：Kimi `SF-2026-MOONSHOT-KIMI-CODE-20261016` 事件A **POST 通过**。精确commit是18c6d642，rendered baseline/watch-reload/clear-compaction和尾删身份保留；record-before-notify/无工具仍推进基线说明不是消费ACK、exactly-once或遵从保证。事件B未写正文，不冒称guard/整工具安全；Typed Instruction→Partial Observation两侧交接清楚。

上述13家族正文 marker 各唯一、精确来源与原note路由一致；六目标文件 `git diff --check` 通过。本人 notes 的“写后待独核”可由 writer 同步为本层既成结果，不需再审正文；若改采用命题/实质正文，只重开对应增量。未写 Books、未stage/commit/push，未授本日DAY或运行/复现。

## R11 — 最后 AI 指定十项必要 Source / actual owner（分批）

仅 root 官方 AI Fri16 首12/286切片中指定十项，不重新发现，不采用submitted作公布日期。本层本人作 Source 初审；root须独立核采用命题。精确v1方法/评价足够即停，不核实现/复现，NC不是关闭候选。

### R11.1 FDE-Gym 22350：标准 Source 通过，Ch66 最小 PRE

[精确v1](https://arxiv.org/html/2610.22350v1) §3–5/7；5=1+2+2。95任务来自20场景，L0–L2只20原任务、其中3个L2复用相同L3；不是95独立世界或四层全量配对。评分把donothing设0、reference约1，扣专家设定而非实测的stakeholder成本；literal≤.2有正确完整请求例外，不能普遍奖励怀疑用户。Shortcut测试是有限反侧非防gaming证明。主模型L0→L1损失较大不证明全部问题定义不重要；事实全取仍未交付好是条件相关。3次运行、200turn/150min/$8cap；human baseline尚在收集，process isolation非统一container，API route费用非listprice。不得将模拟KPI/部署as-is等同生产业务因果。

Actual owner `PLATFORM-EVALUATION-SYSTEM` Ch66，完整3427–3441交互式Spec与3084–3113效用评分局部已读。已有需求访问/实现分离和成本效用，但未承载业务负uplift、询问成本与literal/reference/shortcut四anchor共同校验的具体差额。建议在交互式Spec三段后最小补：

> 需求问答还应与交付效用分账：把可执行交付物置于同一冻结环境，分别测取得哪些事实、相对“不做任何事”的业务增量、事故和联系人力成本；通过测试或拿到全部约束不保证业务改善。评分器先用不行动、可信参照、字面照做与有限捷径校验；若请求本来正确完整，字面方案必须允许成功，不能诱导无条件反抗用户。专家设定的询问价格只是成本模型，同场景变体也不是独立业务；未有真实人类/线上基线时保留分项与不确定性，不把负分或模拟部署推成实际商业回报。旧明确Issue与固定测试仍适合局部回归。

### R11.2 MLExpert / WIRL 22344：标准 Source 通过，Ch33 最小 PRE

[精确v1](https://arxiv.org/html/2610.22344v1) §3–5、C.1–3/D.1；6=2+2+2。Experiment-result之间新生成动作组成window，继承history仅条件；每窗共享原始结果/趋势reward，非组标准化advantage。异步每token保存rollout logprob，preupdate/rollout ratio限区间且detach，只乘PG，区外不删KL/entropy或归一分母；不是整轨迹IS，不恢复原history人口。无可信执行feedback/infrastructure error排除而非model失败奖。MLEbenchLite22任务12h/3000steps、单H200/20CPU/220GB，同SFT和baseline必要对照/去trend与去correction支持窄差额；3次评价SEM不是训练seed。Wait share87.6→39.3不是等总训练墙钟；SFT筛优/截尾与树工具也改变起点。AIME冻结scaffold测试不能授普遍自我改进。

Actual owner `TRAIN-GRPO` Ch33，实际完整2597–2625 Async RL至后继ratio/view校正局部已读。已有版本身份与sampler人口边界，未承载长实验把完整episode换为feedback-closed window的loss单位。建议在Async RL首两段后最小补：

> 昂贵实验不必等整条episode结束才更新：可把相邻可信实验结果之间的主模型新动作冻结成window，以开始时history为条件，只给本窗新token分配该次结果与局部趋势的共享权重。它优化局部window目标，不自动等价完整任务回报；继承上下文、subagent及无feedback失败须分别标注。异步window还要逐token记录实际rollout概率，校正或拒绝失配PG项，并明确KL、entropy与归一分母是否仍保留；局部ratio不是整轨迹无偏保证。窗口化减少等待却增加切分、版本和可信feedback状态，净成本与最终实验质量需独立验收；反馈慢、噪声或状态失配时保留完整trajectory、同步barrier与原outcome credit。

### R11.3 Indic Evaluation Awareness 22333：标准 Source 通过，Ch66 No Change

[精确v1](https://arxiv.org/html/2610.22333v1) §3–5/Limitations及必要标注协议；5=1+2+2。同一原prompt的五cue、4模型、英语+5Indic，harmful199/benign200，greedy单样本、部分reasoning关闭。显式cue使拒绝变化不是内部awareness或scheming证明，implicit eval_logs与普通logging还改变合规指令；refusal不等完整安全。原题相关GEE/配对McNemar与多重校正保留，blind主judge+secondjudge及每语320native审计不消除Telugu弱一致、译文和单annotator可见judge标签偏差。行为、解释和隐变量不能混同。

Actual owner Ch66，完整292–324 paired monitoring、2685–2705 Language×Model×Estimator与3804–3822 awareness/release局部已读。当前已承载同题环境cue配对、行为不反推内部动机、语言/模型/judge分层及probe无发布权；本文多语量化补充留报告，拟保留的长期命题无实际正文差额，**No Change — Existing Coverage**。

### R11.4 KnowGPO 22331：标准 Source 通过（带原文索引冲突），Ch33 最小 PRE

[精确v1](https://arxiv.org/html/2610.22331v1) §3–4、A/B/C必要层；6=2+2+2。两阶段条件构造第二阶段用gold+成功reference trajectory，不是在线无真值知识发现。LLM逐步判已满足fact并OR累计，false positive会永久保留；same bitset不保证同history/Markov等价，OR也不证明上下文不会遗忘。**Eq5写s_t，Algorithm1行13明确s_(t−1)，正文称prior state；只按算法窄采用并披露冲突，不授权公式/实现已一致。** §3称new observation而C说完整history，不能认证只读增量。三个bench/四split、同Qwen3-8B/SFT/data/tools，3次evaluation非多训练seed；消融omega=0行仍异于GRPO，不采“无step reward的grouping独立正则”因果解释。Verifier200人工pair、94.7% agreement非真值；356s verification可重叠不等免费GPU/API，group size增大非同分布证书；hyperparameter/硬件完整成本未闭合。

Actual owner `TRAIN-GRPO` Ch33，完整1788–1815层级group/采样stategraph及其后交接已读。已有canonical state graph+success distance，没有query-specific条件bitset代替surface state、以新fact数而非未来return分局部credit。建议在层级分组两段后最小补：

> 搜索状态还可以按“已经取得哪些任务条件”提出比较组，而不按页面文本相似度合并：离线用参考答案与成功轨迹构造有限原子条件，verifier把每步证据累计成bitset，按动作前的已满足集合归组，将本步新满足条件数的组内信用与终局信用混合。这里条件、判定器与累计规则都是group identity；相同集合不保证历史或剩余动作分布等价，单调OR还会固化误判，不能称真实知识或无偏贡献。条件构造、成功reference与逐步核验均付费，异步重叠不是零成本。原文公式与算法的时点索引未统一，不搬整套精确处方；状态不可离散、gold或可靠verifier缺失时保留完整history、原outcome组或critic。

### R11.5 LangDiT 22330：标准 Source 通过，Ch24 最小 PRE

[精确v1](https://arxiv.org/html/2610.22330v1) §3–4及必要A/B/E说明；5=2+1+2。保持LangFlow表征/CE/solver，区分RMS/QK尺度控制、较宽noise modulation、shortcut显式codebook factor detach与有界forward gate、训练SC entropy gate。Detach不阻断noisy-state的codebook梯度，也不自动证明梯度冲突；QK界含learned gain，非固定temperature。训练25%bootstrap无梯度、entropy仅aux输入启发式，部署保unweighted posterior mean且无额外bootstrap，不是更准clean estimator。OWT1024/327→334M，bf16/seed42，cumulative ladder单训练seed、conditioning增加7.36M；对照不能独立归因六项/证明机制。GenPPL与unigram entropy同报，非完整语义多样性；Plaid只迁四项、checkpoint进度不匹配，660K/520K不是完成1M。无throughput/latency优势。

Actual owner `MULTIMODAL-GENERATIVE-PARADIGMS` Ch24，实际完整连续文本510–528附近LangFlow/DoubleCat交接已读；已有posterior mean/SC/schedule，不含forward shortcut与gradient path、训练feedback与推断estimator三分责。建议紧接LangFlow两段后：

> 在continuous text denoiser中，同一shortcut还应分开前向证据与反向更新：可以只detach其显式codebook因子，另用有界noise gate调前向权重，而让codebook仍经noisy input学习；这不是冻结全部embedding，也不由代数移除一条梯度就证明冲突被消除。训练bootstrap的posterior mean还可按token entropy衰减为辅助SC输入，但采样继续用未加权mean推进solver，不能把辅助置信gate搬成更准确的clean estimator。额外bootstrap、宽conditioning和训练均付费，单seed累加消融不识别各模块独因果；质量、多样性或兼容性不足时保留原shortcut/SC、固定schedule与离散或AR路径。

### R11.6 Private RAG RP 22297：标准 Source 通过，Ch76 最小 PRE

[精确v1](https://arxiv.org/html/2610.22297v1) §3–4.6/Limitations；5=1+2+2。离线采一份固定secret Gaussian R，query及index同投影、k维检索；不是每query重抽，也不删除standard RAG取回的原文。KNN-LM mixing与standard concat分开。**本文明确经验防extraction，不授DP**，JL相似保持不是privacy theorem；matrix/embedding不可见、黑盒text-only，whitebox/inversion/sidechannel均排除。重复同query最多10次且假设系统block，adaptive最多200queries；有限低leak不等无界privacy。ECHR多个模型、Enron/C4/HotpotQA有非零泄漏及QA/F1反退；raw生日被生成错误、比较答案仍对不等事实效用全保。A100单配置四舍五入per-token同.08，pergeneration9.42>8.35；query matvec、index重建/存储和攻击评价均付费，不能“无runtime overhead”。100K documents不证明生产scale，dtype/seeds/tail无披露。

Actual owner `AGENT-RAG` Ch76，实际完整1148–1188 lifecycle与上下poison/exposure论证已读。现覆盖投毒/索引/删除分权，没有retrieval geometry扰动的extraction分支及它与DP/原文授权的边界；不在Ch72重复一般privacy定义。建议在lifecycle标题下旧poison分支之前补：

> 限定黑盒extraction威胁时，也可以固定一份不公开的随机投影，同时变换query与index，让相近候选的检索排序发生扰动；KNN token替代与standard RAG原文拼接是不同消费路径。它不等于访问控制、匿名化或DP，保持相似度也不证明隐私；取回原文仍可能泄漏，投影矩阵、embedding或侧信道可见时不能继承text-only实验。有限重复/自适应query预算下应分别测泄漏、事实正确性与检索效用，不能把错误的敏感细节当全效用保持。投影、重建及在线matvec均计费，威胁、查询量或质量失配时保留授权/敏感内容门、可靠正式机制与人工治理，不由低攻击成功率授无限查询安全。

### R11.7 EliteReplay 22290：标准 Source 通过，Ch33 最小 PRE

[精确v1](https://arxiv.org/html/2610.22290v1) §2–5、B.1/B.3–6、C.1–3；6=2+2+2。Frozen base的MAP-Elites探索按LLM approach+结构cell留最短已验解，固定archive与原prompt作长度均值NLL，按question/cell平衡混入GRPO；不是旧reward离策略重放，部署无archive查询。Search标签与评价AST策略分开仍只是结构proxy，执行正确限给定DB，不保所有DB语义等价。U@k不同于pass@k，retention只base至少两种已采正确策略人口；保持约60%不是全部支持。4B/5K BIRD、archive1K且仅780有可验解，72K生成尝试/1500replay、每步128replay+128×8online/100steps，4A100。IID archive同生成次数/例数与same replay控制支持composition差额，但不等全部token/labeler/验证compute；训练seed/dtype/完整墙钟未披露。更大mu降低pass1，AmbiQT仍不及base，不采无损保真或通用新能力。

Actual owner Ch33，完整265–280策略稀有度与1699–1718 replay各分支已读。当前有当前group稀有度重权、动态成功buffer正则，但没有按verified行为cell固定base支持再监督rehearsal。建议在旧动态replay段后最小补：

> 若目标是保存base的多种已验证解法，archive可在训练前由冻结base按行为cell定向探索，只保可执行正确的代表；训练中按题与cell平衡取样，作为长度归一的监督NLL与on-policy目标并行。此时旧解提供rehearsal，不携带一份旧reward advantage，也不需要把它冒称无偏off-policy更新。Search标签、实际cell、verification及独立strategy evaluator须分账；相近pass@k仍可能只剩少数结构，retention也只针对已观测base支持。定向生成、判分和额外反向均付费，较强replay可牺牲pass1；archive质量、覆盖或净收益不足时保留普通GRPO、较小/均匀replay与独立新任务验收。

### R11.8 EnvTraverse / Scaffolding 22289：标准 Source 通过，Ch66 No Change

[精确v1](https://arxiv.org/html/2610.22289v1) §3–4/6–9与必要执行协议；5=1+2+2。两prompt同code/controller/tools，“report to me”实际交给自动controller，未有人答复或任务建议；same conversation/workspace继续，stuck两次noaction退出可被recovery再启，最多10恢复，非十次普通continuation。JSON request–response不意味着环境静止，terminal与success分开；Controlled_RESET只把既知GAME_OVER规则交脚本，非新规则，且prompt禁止非硬权限，完整专用scaffold是bundle。25ARC/106Maze/89Terminal、每块3保留重复非matchedseeds，替换整块技术失败不重用其子题，单独冻结tier/并发/version。游戏均值进步伴更多cost-token，Terminal方向mixed、教程也可伤；无等compute因果、非劣证明或普适scaffold优越。CPU/remoteAPI条件不是model训练硬件/精度披露。

Actual owner `PLATFORM-EVALUATION-SYSTEM` Ch66，完整385–413 identity/harness三实验、4574–4597 compliance/early-stop局部已读。当前明确prompt/tool/retry/timeout影响行为、harness/environment/scorer分权、固定任务配对和控制流干预及全部continuation预算；本文受控RESET与small prompt反例补充已承载的判断，没有必要再写一段“相同模型不等相同系统”。**No Change — Existing Coverage**，具体结果/跨环境反退留报告，不以有owner或小模型/领域名关闭准入。

### R11.9 LEASH 22280：标准 Source 通过，Ch82 最小 PRE

[精确v1](https://arxiv.org/html/2610.22280v1) §3–5、A.2–4/B.1必要层；6=2+2+2。Query/last-action hidden双bank，success/fail共协方差LDA拟合仍要有标签/核验、SVD/额外调用；training-free仅无gradient。Runtime threshold按**每任务max score**分位非逐step，task-grouped10fold OOF→全bank refit改变scale，实际43–64%不等目标50%，非错误率硬界。99reference与262eval disjoint；不分task的.997AUROC是泄漏反侧。升级后weak继续消费实际strong历史、每3步shadow候选从不执行/不向strong显示；过阈只移去pending action并提高reasoning再决，不回滚已执行GUI。6checkpoints/两次action改变后停。Runtime label继承Manager subgoal非单action正确，弱失败排名非强补救收益；§5最优性只initial Gaussian/同协方差和gain单调条件，不覆盖runtime/Shadow。Always-on无Manager，Shadow与干预bundle，31triggered条件子集非全人口随机因果。固定reference价全workflow token估算不等本地硬件费/延迟，未披露完整runtime/dtype/多独立重复；不采生产省钱或安全。

Actual owner `AGENT-MULTI-AGENT` Ch82，实际完整920–948 delegation与976–989 fleet oversight/后续交接已读。已有触发/收回与校准，但没有handoff不终止弱observer、双时钟及task-max频次校准分责。建议在delegation首两段后最小补：

> 升级也不必停止原弱Agent：先按初始状态与运行期信号决定何时移交，移交后让弱模型只读实际强模型历史，在固定checkpoint提出未执行的候选，以其表示触发强模型重审。Observer不拥有动作提交权；干预只替换尚未执行的pending action，不能冒称撤销旧副作用。若一次越阈即可升级，频次校准应消费每任务的最大运行分数，而非逐step分位；按task分fold防轨迹泄漏，重拟合与shift仍会改变实际升级率。这不是失败概率或硬预算，weak异常也不证明strong可修。Bank标注、manager、shadow与反思均付费；分布/标签或总成本失配时保留随机对照、单Agent、可信执行验证及硬权限门。

### R11.10 Disagreement Routing 22245：标准 Source 通过（带indicator符号冲突），Ch82 最小 PRE

[精确v1](https://arxiv.org/html/2610.22245v1) §3–6、A.5–6及B.1条件；6=2+2+2。Population目标是strong正确率减可选weak最大正确率，非weak失败率；用strong分布近似gold后得到cross disagreement减strong self-disagreement。Exact只在所述independence/iid与s=q条件，不代表强模型真值；实践两probe用weak hidden、离线10×双方生成，非免费/无需训练。**§6.1 A写1{transitions相等}，而§5明确A=1表示分歧，correctness probe又1−A；不复制该符号处方或认证实现已统一。** 动作同call+args/SQL同数据库结果/hidden tests一致仅局部等价，不等正确或未来价值。BFCL correction收益不显著、强者难也难修；实际最高score按预算排序消去threshold误差，不是在线硬频次校准。Agent data iterative routed population、train-task records训练，test-task records也收集但不得据此说训练用test；五runs非多训练seed。单步gain理论不授长期trajectory最优，N=8/first-action selection固定，不授实际最优selection。Feature层/超参待acceptance公开，硬件/dtype/完整成本未披露，无延迟SLO。

Actual owner Ch82，实际完整840–872 step routing与920–932 delegation/976–989 oversight已读。已有confidence/current state与预算，但没有“是否可补救”而非只“weak可能错”的模型间分歧修正。建议在Device–Cloud逐步路由首段后最小补：

> 选择升级还要估计strong相对当前候选的增益，而不只找weak最不确定的位置。没有逐action正确标签时，可离线学习weak–strong分歧，再减strong自身分歧，部署时只读weak候选与表示提出升级优先级；后项用于避免把双方都摇摆的位置当必可补救。它以strong分布近似真值，不保证分歧即错误、同意即正确或单步收益等于全程收益；等价判据及有限采样也有噪声。两个probe、双方离线生成和路由后state重采集均付费，理论oracle与按分数配额排序不能替在线阈值/总成本验收。原文indicator符号不一致不照搬精确处方；teacher不可靠、人口漂移或收益不成立时保留随机/置信基线、外部verifier与不升级路径。

R11 十项已备齐：8最小PRE、2 actual NC。逐项当前官方abs显示唯一v1，未见撤回/替换/纠错提示；历史显示Oct15 submission仅作版本身份，公开日期沿root已实读官方Fri16列表，不从submission推导。LangDiT范围校正：本层实际完整读§3–4及正文对A/B/E边界说明，未声称完整打开A/B/E；EliteReplay B.1只取archive统计，B.3–6/C.1–3必要层实读。未写Books/报告、未核实现/复现，尚待root独立采用复核，不能自授这十项Books POST或DAY。

## R12 — 授权六 family 已实写自读；非本人 writer 的 Ch66 三 family POST 通过

root实际完整消费R11 Source/actual owner/PRE后，明确授本人六个窄段与本人注写入，覆盖此前“只写REVIEW”的限制但不扩其他位置。本人重读Books三文档，协调后只在三文件各既定论证位增一自然段/家族：Ch33 replay成本分支22290、hierarchy group22331、Async RL22344；Ch76 lifecycle开头22297；Ch82 step-routing22245与delegation22280。每段精确v1与唯一正文marker均已读回，旧机制/源注保留；章末本人Review notes在原notes内，不再接机制正文。实际完整新段与直接上下两侧、本人注已自读，PG-only保留mask/denominator、索引/indicator冲突、gold/reference与OR、非DP/有限query、task-max与initial理论限制、strong≈gold及完整费用均在正文。**本人是这六family Books writer，不能自授实际POST；待root非writer核验。** 三文件限定diff-check无诊断，未stage/commit/push。

root另决定FDE-Gym本窗**仅报告**：business anchors/专家成本模型是benchmark-specific结果，拟长期一般判断已有InteractWeb隐条件及production success交集承载；不是宣称现文已有同一算分公式。R11.1最小PRE仅保留为审稿历史，不执行写入，也不将最终处置写成硬NC。Indic和EnvTraverse两NC继续有效，LangDiT由ORG_A唯一写入，本人未碰Ch24。

本人非writer实际完整读回root新Ch66：22158 PremiseSQL、22187 Rating Scale、22321 AVC三新段及各完整直接两侧与三项章末note；复用ORG_B S19/S15、ORG_A AVC有效Source边界，不重复打开原件，也不冒称本层Source独立审阅。**三个实际POST均通过**：真实输入flaw与断言交叉/normal false rejection、is_valid/GEN/条件EX分母；归一不保逐item刻度且无same-scale noise因果；声画关系资格先于同步/缺分解消融/离屏与静默保留。正文不迁taxonomy、任意scale/指标或bench排名为通用真值，旧refusal、scalar/prompt与joint sensor论证未替换。三个正文marker各唯一、精确原链接与本人note一致；Ch66限定diff-check无诊断。root可将其note“写后待独核”同步为本层已发生结果；改采用命题时只重开对应差额。

## R13 — 六项非writer POST 已由root通过；指定45项 README 已保存/交回

root已实际新正文/完整直接两侧与三组本人注核过R12本人writer六family并通过POST；此为root既成独立层，本人不自签。root后续统一行政同步notes，本人不再改这些Books。R12本人非writer Ch66三项通过仍有效。

root另授本人唯一README §3/§4写入ownership，指定新增A晚5/B晚10/CV20/AI10共45家族，且禁止改原36、DC8、状态/结论计数/复核区。本人按实际读过REVIEW R9/R11与ORG_A/B具名必要Source记录、root最终NC/Only/Disputed归并，已保存45表行与45精确v1证据节：37整合、6具体NC、FDE-Gym1仅报告、RBCD1中心争议暂缓。每行Oct16与实际三维评分；每证据节有关键位置、机制/反侧、实际owner和长笔记链接，不把简略版当实现复现。22249实际定点完整读Ch66 task demand window及质量匹配局部，NC只指frequency≠appropriateness/quality-matched控制，不声称已有特定句式实验。RBCD复用B及root实际假设/Eq14/Eq20独核，不授其rate或写书。

保存后实际读回并逐项核45身份各一表行/同标题同URL证据头/完整采用正文；合81行。保护检查：原36行逐字各一次、原36证据连续前缀、§1–2与§5–6逐字保持；新增45的20条唯一章节/长记录目标均存在。README/REVIEW限定diff-check无诊断。V3当前42错误均为原检查时间非ISO、原36标题/abs-vs-html URL不一致、5条旧“写入中”无效决定；**新增45错误0，未越权修原层，不称整报校验通过。** root需在合DC8/最终计数时同步旧层和§6。

本层使本人成为README共同作者，**不再具有本日报DAY/FINAL独立复核资格**；root指定A承担最终DAY，必须按实际角色记录，不能沿用旧§6“reader非报告作者”。README ownership现交回root，本人只保本日REVIEW追加权；不扩发现、日期或其他任务，不stage/commit/push。

## 当前未完成层

本人具名Source、授权六项Books及指定45项报告写入已交付，既成独立层按R1–13复用。剩余DC8归并、全报计数/旧层格式与来源覆盖收口、A的非作者DAY及保存完成态验收由root协调；本人已成为报告共同作者，不代签DAY/FINAL，不预支本日验收，不再扩发现。
