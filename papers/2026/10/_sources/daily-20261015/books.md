# Daily 2026-10-15 — arXiv Books 比较

仅处理 `2026-10-14` 北京时间自然日；候选身份/日期与必要原证以 [arxiv.md](arxiv.md) 为准。此文件由 `oct15_books` 维护，不代替 source 或日级验收；历史 cursor 保持暂停。已读当前 AGENTS、ROADMAP、项目/学习/写作上下文、研究/Report合同、Prompt与每日来源组；已检查 owner 对应论点及局部交接。运行前及并发修改保护，不 stage/commit/push。

## 第一批：具体差额、原逐字提案与实施

### A3 Factuality — `PLATFORM-EVALUATION-SYSTEM`

现有 Ch66「Claim-level Confidence 不能直接升级为 Answer-level Reliability」实际区分 factual precision/all-claims/conclusion（现2616–2631），并有拒答/条件分母，尚未承载 supported-but-irrelevant filler、pool-dependent recall normalizer 对同一回答改分的联合边界。拟在「FActScore 类指标主要估计…」段后、下一小标题前加一段，不改已有概率推导：

> Claim 还要分别判断“被证据支持”和“回答了当前问题”。真实但无关的 filler 可能同时提高 factuality reward 与 supported-claim 分数；只保 precision 又会奖励几乎不说话。因而应冻结抽取/去重、零 claim 与拒答分母、相关性判定及 recall normalizer，联报相关 supported claims、回答量和覆盖；若 normalizer 来自本次模型池，新增一个模型就可能改变旧回答的分数。检索未找到支持也不等于事实为假。[受限复现与测量审计](https://arxiv.org/html/2610.18415v1#S6)支持这些接口差额，不证明所有事实性训练无效：训练预算/数据并未全匹配，相关性过滤本身也会误删，300-claim 人审中其拒绝判断仅55%正确。多轮抽取、检索、人工校准及固定参考的维护均付费；标签或支持不足时保留 Unknown、原始 claims 与人工核验，不把过滤后降分当成精确真值。<!-- source-family:SF-2026-ARXIV-2610-18415 -->

本人直接重开 exact-v1 §5.2–6/T2–3与人审，保留 FactGRPO biography F1+.017 的显著正反侧，不采用摘要“均无显著改善”整体断言；未核 artifact/未复现。

### A4 Injection probe — `PLATFORM-EVALUATION-SYSTEM`

现 Ch66「Guardrail 的 Review Unit 必须与 Clean Twin 一起验收」已有 clean twin 与 FPR/catch 分账；「表征审计必须先消除模板混淆」已有模板/长度混杂，但尚无同一时刻 clean twin 与 harmless look-alike 分别排除 position/format shortcut、以及 normal-traffic threshold 可能反转检测器比较的直接边界。拟在 clean-twin 两段之后、`Action Control` 标题之前加一段：

> Hidden-state 注入 probe 还应同时保留同一任务/时刻的 clean twin，以及沿用攻击格式但换成无害内容的 look-alike；随机干净负例可能仍让位置、长度或格式充当标签捷径。分别测这些负例、去格式攻击和新应用迁移，并把 test-label operating curve 与只用目标应用正常流量校准的部署阈值分开。[AgentDojo 六模型对照](https://arxiv.org/html/2610.18408v1#S5)中，matched negatives 减少误报，却不保证迁移检测总更强：按新应用正常流量设阈值后，标准 probe 的成功攻击检出中位数87%，反高于新方法74%。标签只表示接触注入，不表示已经服从；复核全检出和攻击流量比例又是成本推演假设。构造配对数据、白盒读取、阈值校准和二级审核付费，单 benchmark 与非自适应攻击不能签发实际防护保证；分布变化时重新校准，保留原检测器、独立审核与执行权限门禁。<!-- source-family:SF-2026-ARXIV-2610-18408 -->

本人直接重开 exact-v1 §3–5/T1–2、normal-traffic threshold反侧；只采用评价机制，不采用更安全/真实节省工时保证。未核 artifact/未复现。

### A11 SAGGS — `TRAIN-CHECKPOINT`

现 Ch35「为什么只保存 Weights 不够」已区分 weights-only/resume；但尚无**同函数权重仍有不同 optimizer 轨迹**。与 root 新增 construction-dtype 段不冲突。拟紧随“三个对象可能共享 tensors，但完成标准不同。”、下节状态清单之前加两段：

> 即使当前预测与 loss 相同，两份权重也未必是可互换的训练起点。正标量互逆缩放 Q/K、V/O 或满足齐次条件的 MLP 矩阵对，可以保持当前函数，却改变梯度与相对更新尺度；GELU 的 up/down 不满足这项精确对称，SwiGLU 也只覆盖 value–output 对而非 gate。对精确对称坐标 `θ′=sθ`，对应历史中的 Adam moments 应为 `m′=m/s`、`v′=v/s²`；但仅转换 moments 仍不足以让下一步等变，还需同时满足 `η′=sη`、`ε′=ε/s` 与 `decay′=decay/s`，并保持 counters 与随机性相同。函数等价因而不能代替 resume-state 等价。<!-- source-family:SF-2026-ARXIV-2610-18085 -->
>
> 一种受限恢复方式是在第一次 resumed update 前，把精确对称轨道上的矩阵对及 moments 一起规范到同一 balanced state；它不是任意权重重标定，也不等同只周期性调整权重。变换与校验增加状态迁移成本，错误的 pair、Norm 或 optimizer 耦合会破坏前提。[受控 checkpoint 实验](https://arxiv.org/html/2610.18085v1#S5)主要恢复人为引入的尺度失衡，不能推出正常大模型默认获益；soft damping 仍依赖起始位置，也不是 exact canonical restart。不能证明对称与完整状态变换时，保持原参数化，保留原 checkpoint 并按新优化轨迹验收，不以恢复时 loss 接近签发连续性。

本人直接重开 exact-v1 Theorem2/5/Corollary4/C.4–5；shared-LR block-local impossibility 另需 homogeneous degree≠−1 或 near-zero bounded，不扩成所有优化器不可能。后续正文不采用这项普遍性标题。未核 artifact/未复现。

实施：root PRE通过并授Ch35唯一窄锁后，两段已写现43–45行，增加未失衡control无可靠改善；本人实际顺读16–70完整局部，限定diff-check通过，lease已释放。独立actual POST待 `oct15_review`，不预签。

### A12 DoubtLess — 已有覆盖（无写入提案）

`MODEL-SAMPLING`，Ch20「Semantic Steering 可以从单向 Vector 扩展为受限 Subspace」现311–315已实际承载：同已提交 prefix 的双 prompt logits 差、强度旋钮、词表/前缀身份、两次前向成本、强度质量反侧及普通单模型回退。小辅助模型代替同 checkpoint 是受测成本实现选择；现有跨模型 controller 段又明确词表坐标和 producer identity。无需因缺 DoubtLess 名称新增摘要。原证的EOS/think-end保护、α/size质量损失、单B200/14题局部walltime保在报告，不把少token当普遍latency或非劣保证。

## 第二批：A5–A8 原逐字提案与实施

### A5 FastEEP — `INFER-DYNAMO`

现Ch52「Wide-EP 的部分 Rank 恢复…」完整覆盖membership/expert/routing epoch，但现路径要求重建collective/buffer/graph；尚未说明预初始化最大域内保虚拟地址、释放物理页、远端reachability撤销的复用边界。拟在其末尾、`与第55章的边界`前加两段：

> 可计划的 EP 收缩不一定要销毁全部执行身份。若先建立最大 worker 集合的通信 parent domain，后续可派生 active subgroup，并同时切换点对点可达 mask；worker 保留进程、executor 与 CUDA Graph，虚拟地址不变而物理页可释放。专家先在存活组中补齐、请求迁出或按规则重建 KV，再在 safe point 一起提交 request routing、expert mapping 与 active membership。清空本地请求队列不是 quiescence：远端仍可能向该 worker 的 experts 或通信 buffer 发起访问，必须先撤销 reachability 并 drain 在途操作，才允许 unmap/reuse；扩容则须先恢复页面与内容，再重新发布可达性。<!-- source-family:SF-2026-ARXIV-2610-18451 -->
>
> [FastEEP 的受限实现](https://arxiv.org/html/2610.18451v1#S4)用保留结构换更快切换，但仍支付 host 备份、专家复制、KV迁移/重算与预初始化最大拓扑的成本；专家slots也限制最小active组。16张H20-3e、EP2–16的有限对照不证明任意拓扑与SLO，closed-loop示例的8→4→8切换仍有4.2/7.3秒零输出期，不能叫无中断。超出parent域、无法保地址/正确内容或停顿超预算时，保留整组重建、固定EP与显式请求终止/重试，而不是让结构复用替状态有效性签字。

本人定点直读exact-v1 §3.2/4.1–4.3及reachability；source作者主评价/限制已收口。未核代码/未部署/未复现。

### A6 CSNB — `PLATFORM-PRODUCTION`

现Ch73「Accelerator Silent Corruption…」覆盖checksum/sketch局部检测/修复与回退，但未说明dense与router检测灵敏度不同且token-sequence变化不等semantic错误。拟紧随其两段、最终Review notes前加一段：

> 保护预算还应按算子分配，不能把 dense GEMM 的检出率移植到 MoE gate。以 row/column norm 构成的 Cauchy–Schwarz 全局上界，能省去 checksum roundoff-margin 的求值，却因界较松漏掉局部扰动；router 的微小 logit 变化又可能改选 experts。[受控 bit-flip 对照](https://arxiv.org/html/2610.18557v1#S3)中，bf16/L40S上的dense层检出接近checksum，而所测Mixtral gate仅保留约55%的检出能力；这不证明所有router都同样脆弱。该实验以生成token序列改变标记SDC，不是语义错误率，fusion中的FlashAttention matmul也未保护。KV还会复用未检错误，因此须沿token传播与任务结果验收，校验kernel和阈值求值开销分别计账。覆盖不足或高风险gate应保留checksum/重算与设备隔离，不由局部无误报签发完整输出正确或真实硬件故障率。

本人直读exact-v1 §3–4/结论，未核artifact/未复现。

### A7 RankLens — `TRAIN-DISTRIBUTED-TRAINING`

现Ch36「小规模仿真只能验证Control Path」已有真实rank+虚拟通信/校准误差，尚未区分timing substitution与recorded value restoration对numerical replay的必要证据。拟其第二段之后、packet仿真分支之前加一段：

> 单rank分析还要把“通信何时完成”与“完成后读到什么值”分开。结构/计时回放可用recorded或estimated duration模拟异步Work的submit→complete→wait，让本rank真实计算继续；若要复现远端扰动在本rank的数值症状，则必须另有与该execution对应的post-communication payload和本地输入/state，在消费者读取前恢复。估算时间不能补造缺失peer的数值执行，value replay也不重建远端根因。[RankLens的受限实验](https://arxiv.org/html/2610.18009v1#S3)支持这种边界：wait重排预测快23.60%，实跑仅14.75%，说明contention仍可遗漏；它不是任意规模job的等价或性能证书。真trace/payload先要由真实运行取得，采集、存储和事件匹配均付费；执行路径或payload不匹配时只保结构诊断，回到真实多rank replay验数值与性能。

本人直读exact-v1 §III-C/D与wait反侧，未核artifact/未复现。

### A8 QBA — `INFER-SCHEDULING`

现Ch56目标/fairness与预测slack已有一般取舍，但无不可被后续short admission挤掉的promotion debt及quota语义。拟「Iteration Scheduling」标题下、原正文前加一段：

> 预测短请求优先能改善均值，却可能长期挤压长请求；无限加大aging又会反过来拖慢短请求。一条受限折中把“等够久取得资格”和“已经欠一次晋升”分开：每完成 `k` 个短prefill admission赚取一个debt（chunk continuation不计），debt在最老eligible长请求实际admit前保持pending，不能被更多短请求冲掉；但decode、continuation与KV安全仍可延后它。因此quota限制晋升频率，不承诺任意流量下的有界墙钟等待。[QBA的trace-driven模拟](https://arxiv.org/html/2610.17795v1#S3)支持均值—尾部折中而非线上SLO保证：FCFS在部分高负载tail更强，长度误判还可能让均值改善同时两类tail恶化。计数/debt、历史分位数及分类误差需共同记录与校准，不能以M/G/n近似认证真实engine稳定；预测失准或tail优先时保留FCFS、保守fair queue与独立过载控制。

本人直读exact-v1 §III-A6与IV-B/tail反侧；未运行live engine，未复现。

实施：A5–A8四处root逐字PRE后获窄锁，已按拟文保存，A8依root要求改至旧Iteration Scheduling两段后、Age vs TTFT/TBT前。本人实际顺读Ch52 348–378、Ch73 276–295、Ch36 1666–1686、Ch56 391–407完整局部，限定diff-check通过，四lease已释放。独立actual POST待 `oct15_review`。

## 第三批：A9/A13–A15 原逐字提案与实施、A10 NC

### A9 AXIS — `MULTIMODAL-EMBODIED-VLA`

现Ch26数据演进保provenance、派生action/sim-to-real，未说明quality label的粒度与接入方式不是可独立排序的超参。拟在「derived label必须保存provenance」现778段后、便携gripper分支前加一段：

> 同一批自然次优示教的“质量”也不是单一筛选阈值。先区分chunk的局部进展幅度与episode中持续进展的比例，再决定质量用于loss权重、过滤训练人口还是作为policy输入；靠近物体但尚未接触的准备动作，不能只因对象状态未变就判为无用。粒度、处理方式、base VLA与后续FT/推理tag应联合比较，并匹配保留time steps和训练updates。[三VLA受控对照](https://arxiv.org/html/2610.18869v1#S5)中，episode conditioning与chunk filtering只是平均偏好，存在模型/奖励及seed反转；FT给全部示教同一高tag不提供质量排序，不能据此证明真实质量因果。真机plain BC simulation pretrain已达31.7%，质量conditioning仅32.5%且有退步任务，不能把全部sim-to-real收益归给质量机制。状态标签、筛选/重复曝光、阶段适配与真机验收费，代理低估必要准备/恢复或迁移失效时保留直接BC、目标本体示教和真实闭环验证，不采用统一最佳recipe。<!-- source-family:SF-2026-ARXIV-2610-18869 -->

本人直读exact-v1 §4/5.1–5.4/6的关键控制与反侧。未核artifact/未复现。

### A10 WorldOracle — 已有覆盖

`MULTIMODAL-WORLD-MODELS`。现Ch25「Evaluation/从平均预测误差到分层Rollout Admission」917–941已task-grounded event/predicate、物理约束/uncertainty、真实outcome与成本；「Action-conditioned World Model要先通过Integrity Gate」1333–1345已same initial observation+feasible expert/off-expert action→visual gate→reference end-effector对齐、invalid/action mismatch分账与严格真实安全边界；1005「视觉逼真与三维一致性…」另分感知/几何。WorldOracle用paired执行、失败/成功人口及多failure维度进一步验证这些合同，不改变现有解释，无须为四个metric名另写摘要。其multiview arm-reference不等3D几何、motion-following不蕴涵physical interaction、metric权重及judge边界保在source/report，不授闭环controller或通用因果机制归因。root已同意具体NC；未核artifact/未复现。

### A13 Depth Memory — `MODEL-TRANSFORMER-LAYER`

现Ch17「Residual Stream…Depth-wise Routing」449–483拥有显式history/block/slots与rank-one carry，未有保留普通residual、另用RLS压缩跨depth关联的三stream分支。拟在原bounded-depth-state取舍段（「模型较浅、吞吐优先…」）后、MSAR多路retrieval分支前加两段：

> 不逐层保存历史，还可以保留标准additive residual `x`，另为每个token维护固定宽度的关联矩阵 `M`与inverse-covariance `P`：当前层读取 `x+Mq`，子层增量既更新residual，又以预测残差乘gain的rank-one项写入 `M`。正forgetting/importance与ridge条件下，Sherman–Morrison递推给出加权depth regression的RLS解；这利用层本已顺序执行的约束，不意味着同样的不可并行求解适合token-sequence Prefill，也不是跨token持久KV。普通residual与压缩关联记忆承担不同职责，不能把后者当作前者的无损替代。<!-- source-family:SF-2026-ARXIV-2610-18809 -->
>
> 固定的是随depth推进的state宽度，不是总activation成本。分组各有 `P`，`Dk=8`时单memory matrix已为每token `8D`、另加residual与covariance；unwinding/windowing以重算、紧凑中间量和延迟融合减少保存/流量。[受限消融](https://arxiv.org/html/2610.18809v1#S4)中去掉residual的两种变体都劣于PreLN，而RLS替换为delta/outer仅有局部小差额；400M/1.5B质量及B200 kernel结果不证明普遍优越，1.5B也未跑FullAttnRes。额外状态、递推数值与专用kernel不合预算时，保留标准residual、粗block summary或显式depth retrieval，不能由较低PPL签发全规模吞吐保证。

本人直读exact-v1 §3.2/Eq6–8、4.1–4.2/T2–3，未核artifact/未复现。

### A14 Refresh — `TRAIN-PRETRAINING`

现Ch28约612行两侧预条件段只要求记录basis更新期/EMA，未明确同count/terminal age仍因placement×LR反转、frequency并非完整schedule。拟紧随该「两侧几何增加状态和刷新责任…」段之后、正交后幅度控制分支前加一段：

> “每隔多少步刷新”还不完全指定预条件器的使用历史。即使refresh次数和终点cache age相同，中间时刻不同也会改变累计staleness、当时参数/动量与后续缓存内容；因此应保存完整step集合，并在同一LR、数据、horizon与seed下比较placement，再跨LR检查排序。[Mousse的受控短训练](https://arxiv.org/html/2610.18695v1#S4)在FineWeb观察到低LR偏晚、高LR偏早，但它刻意处于undertraining区间，其他corpus、高密度refresh和更长horizon并未一致保留反转；uniform同预算仍常更好。谱宽度staleness proxy漏掉这次反转，不证明所有curvature sensor无效，更不证明非均匀schedule最优。eigendecomposition、完整schedule搜索、重复seed与恢复均付费，局部反转不能外推compute-optimal长期pretrain；没有匹配证据时保留已验证uniform cadence与原recipe，不用frequency或单proxy替代真实held-out比较。<!-- source-family:SF-2026-ARXIV-2610-18695 -->

本人直读exact-v1 §3.1/4.3及budget59/horizon与cumulative-age反侧；不是纯placement单因果控制，不授最佳step。未核artifact/未复现。

### A15 UniW(A)M — `MULTIMODAL-EMBODIED-VLA`（由原拟Ch25改Ch26，root确认）

Ch26「World-action model」425–482完整拥有显式/joint/direct接口和因果信息路径，尚未有同backbone多typed接口的eligible-expert范围与chunk级interface路由。Ch25不重复。拟在三接口表后、「显式rollout保留…」现437段前加两段：

> 这些接口也可以共用一个backbone，但共享参数不等于取消条件边界。可用attention mask分别声明：外供clean actions只预测future video、video/action互见、先video后action、action→video单向，或future两路互不读取；token group再仅在对应预测角色允许的experts内学习混合权重，shared expert保留共同路径。这把“能看见谁”和“可调用哪些计算”分成两份合同，角色命名与bidirectional joint mask都不能证明精确因果factorization或真实动力学已解耦。<!-- source-family:SF-2026-ARXIV-2610-18697 -->
>
> 部署还可在每个chunk选择interface，而不是固定全episode模式；但router的监督与费用须独立验收。[UniW(A)M的受限实现](https://arxiv.org/html/2610.18697v1#S3)冻结backbone，在每task2000个target chunk上用各接口相对真实action的MAE训练路由，近最优时偏好快接口；这不是zero-shot或直接最大化task success。OOD仍保持task goal、只改外观/物体条件，dense与MoE同steps也非同FLOPs；router head约2ms而含feature约63ms还不含观测/语言编码，step-normalized chunk latency不等完整chunk walltime或控制Hz。共训、目标场景标注、四接口离线求值和在线特征均付费；支持不足、路由误判或deadline不成立时保留固定已验接口/direct policy、短chunk与独立controller，不由共享expert或一次局部成功率签发安全。

本人直读exact-v1 §3.1–3.3/CATR与PAIR、A4/B1 target构造与费用，未核artifact/未复现。

## 当前实际处置（2026-10-15，本 source 15家族）

最终13项整合、2项具体已有覆盖；不是15篇都必须新增正文。A1–A4由root实施，A5–A9/A11/A13–A15由本人实施；每项证据与独立POST以[arxiv.md](arxiv.md)和[review.md](review.md)为准，不用此表预签日报完成。

| 项 | 最终处置 / 唯一owner | 当前实际位置 |
| --- | --- | --- |
| A1 Tev | 整合，`TRAIN-GRPO` | Ch33 `Phase-specific Credit`之后，现901；root写入，明确只有保终局势的具体配方改变目标 |
| A2 SparPR | 整合，`INFER-KV-CACHE` | Ch45 `Eviction 与 Offload`成本段后，现343；root写入，hidden checkpoint projection与整段copy比较 |
| A3 Factuality | 整合，`PLATFORM-EVALUATION-SYSTEM` | Ch66 atomic verification unit之后，现2613；root写入，supported/relevant及固定分母 |
| A4 Injection probe | 整合，`PLATFORM-EVALUATION-SYSTEM` | Ch66 `Guardrail…Clean Twin`末，现4584；root写入，matched negatives与正常流量阈值反侧 |
| A5 FastEEP | 整合，`INFER-DYNAMO` | Ch52 `Wide-EP…联合Runtime Contract`末、与55边界前，现365/367 |
| A6 CSNB | 整合，`PLATFORM-PRODUCTION` | Ch73 `Accelerator Silent Corruption`第三段，现286 |
| A7 RankLens | 整合，`TRAIN-DISTRIBUTED-TRAINING` | Ch36 `小规模仿真…`后、packet模拟分支前，现1674；最终外链为真实`#S3` |
| A8 QBA | 整合，`INFER-SCHEDULING` | Ch56 `Iteration Scheduling`旧两段后、Age vs TTFT/TBT之前，现397；最终外链为真实`#S3` |
| A9 AXIS | 整合，`MULTIMODAL-EMBODIED-VLA` | Ch26 `数据演进`provenance后、便携gripper前，现786 |
| A10 WorldOracle | 已有覆盖，`MULTIMODAL-WORLD-MODELS` | Ch25 `分层Rollout Admission`、`Integrity Gate`及视觉/几何分责；无写入 |
| A11 SAGGS | 整合，`TRAIN-CHECKPOINT` | Ch35 weights/resume/deployment三对象之后、状态清单前，现43/45；最终缩放改明确定义`c>0`，避免与章首step `s`冲突 |
| A12 DoubtLess | 已有覆盖，`MODEL-SAMPLING` | Ch20 Semantic Steering双prompt logit差、模型坐标与费用/质量段，现311–315；无写入 |
| A13 Depth Memory | 整合，`MODEL-TRANSFORMER-LAYER` | Ch17 bounded depth-state取舍后、MSAR读取分支前，现476/478 |
| A14 Refresh | 整合，`TRAIN-PRETRAINING` | Ch28两侧几何/刷新责任之后、正交后幅度控制之前，现614 |
| A15 UniW(A)M | 整合，`MULTIMODAL-EMBODIED-VLA` | Ch26 World-action model三接口表后，现437/439；最终owner已由原拟Ch25改Ch26，不重复写Ch25 |

最后四项均经root逐字PRE与指定窄锁后实际保存。A9最终按root修为“模型与seed反转”“真机验证均有成本”；本人实际顺读Ch26 425–449/770–791、Ch17 449–491、Ch28 606–620，限定diff-check通过。三lease全部释放，没有本人待写Books或后日工作。A1/A11独核修窄及A7/A8链接修正已实际回读确认，前批POST与两NC见review R6/R6.1；最后四项由非writer `oct15_review` 实际顺读完整局部与diff后在R7通过，本人已实际读回该结果。15项Books处置链闭合，不代签日报DAY/FINAL。

此处无实现核验、实验复现、线上部署或日级Complete声明；没有修改ROADMAP、索引、Learning State，没有stage/commit/push。既有和并发改动保留。
