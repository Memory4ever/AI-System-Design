# Live 2026-10-09：新增四项必要证据

作者 supplement_20260312；只处理本日BJT2026-10-08的09876/09679/09493/10533，不扩发现或复用其他日候选。四完整精确v1题摘贡献已由非作者review_mar11_continue独校准PASS；公开日复用author11实际官方Oct8目标组，经root允许有效复用，不以Submitted替代。必要Source、owner/PRE、实际Books POST和DAY分开记录。

## 2610.09876 — Think Before You Paint: Recursive Latent Reasoning for Diffusion Models

[exact-v1 HTML](https://arxiv.org/html/2610.09876v1)。本人实际完整题摘/current v1 history无withdraw/先稿信号；date为官方AI Oct8目标组。评分2+1+2=5，标准必要Source完成；具体生成状态gap深入受影响范围，不改分。actual §3完整方法/Eq1，§4.1 Tables1–3/必要正反文字、§4.2/4.3完整、§5与Appendix C/H/K/L/N必要文字和Tables5/6/13/20/21/22；图只caption与正文，未核像素、代码或复现。初次大输出中段截断后从官方HTML按section定点补全，不将截断当全读。

原有约束→小recursive Thinker在单denoise内更新(y,z)，只把y空间tokens解码给ControlNet，frozen Painter读取该信号→把探索潜状态和当前noisy sample分开。z本身不解码为解；基础版每denoise reset，efficient版才跨步保留/早期多递归/后段复用最后输出，不合并为唯一recipe。先训Painter，再冻结并训Thinker/condition encoder；两段仍均用重构loss。无symbolic训练target/solver/verifier不等无结构条件，也不等输出无需规则验收。

关键评价/反侧：MNIST Sudoku、AMAZE maze/Queens、CLEVR空间关系；Maze fine-tuned Bagel在pass/coverage可高于PaTh，PaTh的exact指标人口不同；CLEVR T3属性53.8低于普通DM54.6/56.3，Recall也略退，不称不伤视觉质量。注入错误从已知valid解重加噪开始，晚段两模型均难修；Sudoku70%处DM反超，不授任意时刻修复。K probe训练label是同一轨迹最终图像的MNIST classifier读数，不是外部真解，latent probe波动不能认证内部正确搜索/普遍因果。

决定性适用边界：L T21 conditioning与目标空间错配时Puzzle0/Cell11.1%，增加token81→144不修；同变换条件也只部分恢复3.4/44.3，不是完全等变。L T22关系tokens无空间anchor时51.2空间/7.8属性，centroid定位条件才明显改善；不能声称从无锚符号自动推出物体位置。N早递归/跨步保留只有限配置；不用图像精确曲线批准全域最优预算。H两阶段85h vs joint113h是该Sudoku配置，不授统一训练节约或生产时延。Painter/Thinker训练、ControlNet、递归、状态驻留/复用、空间条件和最终检查均计费，参数量非完整成本。

Actual owner唯一MULTIMODAL-GENERATIVE-PARADIGMS，Ch24已实际828–875完整workflow→provisional/committed→持久条件副本→runtime交接，145–162普通diffusion状态与固定条件接口，Ch23/25开篇。旧正文区分条件副本/noisy state/外部commit，但未承载不解码探索状态经readout引导frozen sampler及其空间anchor失败条件。拟在持久条件副本完整段后、UI外部commit段前一段；不改旧定义，也不将论文所谓sample commit冒充对用户承诺。

### 逐字最小PRE（已独核/已写，actual POST通过）

尚未解码的探索状态还可以与 noisy sample 分开：在每个 denoising step 内，让递归网络反复更新潜状态和读出候选，只将读出的空间信号经 adapter 交给冻结生成器；中间潜状态不必是一幅可展示图像，也不要求每次更新都单调变好。这不同于持续覆盖输入的 clean-token 副本，也不将 sampler 内一次状态更新当作外部 commit。[受限像素约束对照](https://arxiv.org/html/2610.09876v1)支持这条分工，但无符号目标训练不等无空间先验：条件与输出位置失配时，增加潜 token 仍不能恢复规则满足；晚段错误难修，部分视觉质量指标也会退步。递归、adapter、两阶段训练与状态驻留均付费，跨步保留或早段集中计算须另验，probe 读出的最终样本倾向不认证真实解。空间对应、质量或预算失败时，保留普通生成/显式约束与独立输出检查，不以内部探索批准发布。<!-- source-family:SF-2026-ARXIV-2610-09876 -->

supplement_20260311非作者必要Source/actual owner/逐字PRE实际PASS，记录additional-independent-review.md；root授Ch24窄锁。作者实际写一段及自身末注，写后完整邻接顺读；root非writer实际846–875完整邻接、新858与本人2321注POST通过，锁释放。仅此项实际整合，不授DAY。

## 2610.09679 — CERO: Where and When to Allocate Rollouts for RL Post-Training

[exact-v1 HTML](https://arxiv.org/html/2610.09679v1)。本人actual完整AB/current v1无withdraw或先稿信号；公开日复用官方LG Oct8#420。评分2+2+2=6，标准必要Source完成，具体horizon调度缺口深入受影响接口。实际§2–7完整必要文字、Eq1–12/Algorithm1/Tables1–2、B.2/B.4完整；初次长输出中段截断后定点恢复§2–4文字及原公式。未读全部D/E/F证明、G全实现或图像像素/代码，不把未读证明升为正确保证。

固定每轮预算只决定本轮组从哪里来；CERO保存跨轮prompt Beta状态/支持斜率、shared price与剩余budget，按正margin排序产生virtual allocation，再以剩余budget裁执行。双变量反馈用virtual而非实际budget-clipped allocation；实验每选prompt仍固定8responses，不是动态组内G，zero-allocation round不更新policy。qhat=ab/[(a+b)(a+b+1)]是条件iid Bernoulli下预期组reward variance，不是参数更新后的学习收益；rho遗忘可跟踪但不认证非stationary校准。指数concave曝光utility是所选surrogate，Fenchel affine表示服务调度，不把surrogate定理搬成全局policy最优。

关键人口：三backbone、同DAPO Math17K 50%子集、500rounds/256kresponses；avg@16是16次binary reward均值非pass@16；五数学benchmark macro有限人口。Random-matched保groups/pacing而randomize prompt分配支持promptaware assignment，不等纯budget pacing因果。T2 DSR1 1.5B三seed区分fixed/preset/greedy；不是三backbone全部多seed。T1 7B MINERVA27.55低于GRPO28.06/Knapsack28.72，Olympiad38.45低于Knapsack38.64；4B AIME17.29也低于Knapsack17.50，不授所有任务更优。

B.2仅selected32k组：预测均值.154/观察variance .119有上偏，bin/时序相关不认证绝对calibration、未选人口或downstream gain；withinrun CI未调整重复prompt/时序依赖。§5 same-path rate对照固定现实q序列，替代allocation改变policy/q路径的反事实收益不由该保证推出；本轮不采用数值regret bound或所有证明正确。B.4完整E2E包括init/validation/checkpoint，token归一core含generation/reward/logprob/optimizer/allocation；固定response不等固定tokens或updates。CERO/Random在各backbone只488/486/487更新，普通GRPO500；成本每方法/模型只有一run，4B Knapsack35.85GPUh比CERO36.31低。Beta/dual状态、selection统计、完整rollout/judge/更新/存盘均计費，不写免费调度/生产速度保证。

Actual唯一owner TRAIN-GRPO，Ch33 actual432–491选择/动态G/停轨迹与499–548跨任务prior→prompt replay→errorbranch完整局部，Ch32/34开篇。现prompt replay有近期信号/current rollout与均匀fallback，但未承载固定group下跨horizon剩余预算与virtual/actual反馈分责。拟2603.21177完整marker后/errorbranch前一段，不改原GRPO式或覆盖静态quota。

### 逐字最小PRE（已独核/已写，actual POST通过）

即使每道入选题的 group size 固定，训练预算仍可在轮次之间调节，而不只在本轮挑题。一个有限 horizon 分支保存 prompt 的近期二值 outcome 统计、累计暴露、支持斜率和共享预算价格：以所选凹暴露效用产生本轮虚拟配额，再按剩余总预算裁剪执行；双变量反馈消费虚拟配额，不把被全局预算截掉的量误当题目没有价值。它只控制 admission、重访和支出节奏，当前 policy 仍重新生成完整组，verifier 与 optimizer 保持原责。[受限调度对照](https://arxiv.org/html/2610.09679v1)支持这种跨轮控制，但 reward variance 只是可区分度 proxy，不是学习增益；固定 rate 或 same-path 的 surrogate 界不授权不同采样产生的 policy 路径同样最优。部分任务仍退步，预测有上偏，统计/调度/rollout与更新均付费，固定 response 预算也不等同 token、更新次数或完整训练成本。覆盖、proxy或费用失配时保留均匀/静态支出与既有 prompt replay，按真实质量和全链费用验收，不由有效组比例给最终能力签字。<!-- source-family:SF-2026-ARXIV-2610-09679 -->

supplement_20260311非作者actual必要110–346/B2 423–443/B4 451–461及Ch33完整owner/逐字PRE通过，独核见additional-independent-review.md。root授本段与自身注窄锁，作者实际写后完整邻接顺读；root非writer实际528–552完整邻接、新543和本人3124注actualPOST通过，锁释放。仅此项实际整合，不授DAY。

## 2610.09493 — The Attribution Blind Spot: Layerwise Trajectory Diagnostics for Source Reliance in Retrieval-Augmented Language Models

[exact-v1 HTML](https://arxiv.org/html/2610.09493v1)，公开日复用已独核官方AI Oct8组，完整v1 AB已非作者准入PASS。当前abs轻核仅v1/27pages4figures，无withdraw/先公开comment信号，不将Submitted作公开日。评分2+1+2=5，标准必要Source完成，内部测量与受限干预具体gap深入。本人实际§2完整方法/Eq1–11、§3/4完整关键人口和评价、§6/A.1限制、D.2完整候选梯度对照及Tables15–18；图仅caption/正文，不核像素、代码或复现。长输出截断不作完整附录已读，必要D.2另由官方HTML定点补全；不依赖其他附录证明。

同一最后共享prompt位置的paired hidden-state差，区分context exposure、冲突source choice与反向控制。PC1在outer-training中心化拟合，但原始差的signed投影与L2幅度负责不同端点：幅度在NQSwap更好预测二元choice，方向用于控制。训练内冻结符号/层块/幅度/剂量，再向held-out同prompt加向量；不从held-out答案或梯度拟方向，也不把无上下文候选A强制定义当普遍事实真值。

关键人口/反侧：OLMo verified exposure为1000 items/100 source groups，Pythia为3994 verified targets；线性LTS AUC近chance和OLMo有限检验力不证无membership/非线性信号。NQSwap120探索items、113全条件/112二元终点，ConflictQA两模型777/617有效二元，outcome-adjacent margin非独立source证书。早层控制失败；source-margin变化不等greedy翻转，独立conditional cohort与全集分母不混。训练冻结平均candidate-gradient对照保持同items/prompt/token/layer/operator/dose/per-layer norm，能改偏好但congruent与no-context保留点估计约91.6/90%，低于所设95%点门；LTS有限点估计97.8/96.5也不是全能力保证。D.2只排除这条平均梯度解释，不排除所有非线性/item特定方向或识别唯一natural mediator。

长段OLMo200例/197有效是限量局部source-use评价，NLI判分非事实真值；cross-model要500无标签anchors/SVD对齐和target-native幅度，不是零成本/任意架构。提取多层paired activations、训练方向、干预重复前向、保留/直接生成评价、judge及跨模型对齐均计费，不授生产provenance certificate或普遍安全能力。controlled incompatible answers只使choice可观察，原来两个来源答案一致时不能反推自然依赖。

Actual唯一owner PLATFORM-EVALUATION-SYSTEM，Ch66本人实际266–297完整adapter/内部sensor→Gemma2重建/输出/解释→跨模型差异→Evaluation Identity邻接，另1098–1130 RAG评估单位；Ch65/67开篇已读。既有internal差异/steering分测但未承载变化幅度诊断与signed source-control的具体职责、等范数答案梯度反侧。拟Gemma2两完整段后/跨模型差异段前一段，不新增RAG第二owner。

### 逐字最小PRE（已独核/已写，actual POST通过）

内部状态变化的大小与可干预方向也须分开验收：在相同 prompt 位置配对有无上下文或冲突条件，变化幅度可以预测输出选哪一来源，但这不让最大幅度方向自动成为有效控制器；可在训练样本拟合带符号方向，冻结层、剂量与操作，再以等层范数的随机方向及平均答案梯度作对照，分别测来源选择、离散答案变化和非目标保留。[受限来源冲突实验](https://arxiv.org/html/2610.09493v1)中，平均答案梯度也能移动偏好，却更破坏非目标行为；早层干预失败、跨模型须额外对齐，点估计保留率不认证全能力。该对照只区分所测方向，不识别唯一因果回路；两来源答案原本一致时也不能由匹配文本反推自然依赖。激活采集、方向拟合、重复前向、对齐与独立行为评价均付费；没有可校准冲突人口或保留失败时回到直接出处/行为验证，不由内部 signal 给来源真值或发布授权签字。<!-- source-family:SF-2026-ARXIV-2610-09493 -->

supplement_20260311非作者实际§2–4 69–212、§6/A1、D2 403–453/T15–18与Ch66完整owner/逐字PRE PASS，独核记录additional-independent-review.md。root授Gemma2第二完整段后/crossmodel前单段与本人注，作者已实际写后完整邻接与本注顺读；root非writer实际274–294完整邻接、新283与本人5860注actualPOST通过，锁释放。仅本项实际整合，不授DAY。

## 2610.10533 — EngramEdit: Decoupled Knowledge Updates in LLMs through Conditional Memory

[exact-v1 HTML](https://arxiv.org/html/2610.10533v1)，current exact-v1题摘/history已实读无withdraw/先公开信号；公开日复用已核官方CL Oct8组。评分2+1+2=5，标准必要Source完成，具体MODEL-EMBEDDING更新接口gap深入。本人actual §2/3完整Eq3–10、§4.1–4.4/Tables1–2/§6、B.2/B.4完整必要文字、A.3.1/3.2原聚合与gate说明、A.4 sequential/cost文字；未核A.5全部证明、完整Algorithm表体或图像像素/代码。长输出截断未作完整附录已读，必要方法及原公式另web小段补全；成本公式未采用精确阶数。

机制：同edit生成多种表达，冻结模型学习共用memory perturbation作每表达目标；在最后subject token枚举suffix n-grams，batch级expression×distinct-ngram mapping记录共享，求AU≈B的reuse-regularized least squares，每共享ngram只解一更新。Sum聚合下positive diagonal使normal matrix唯一可解，不等任意门控聚合都线性；A.3.2门控需nonlinear优化或固定query的局部Jacobian，若上游query受改则重算依赖。频率/长度是reuse proxy，不认证任意未见输入保留。

关键实现身份：实验LongCat-Flash-Lite68.5B，其中31.4B ngram容量、2 RTX PRO6000；三种长度2/3/4×4 hashed subtables，projection后与token平均。B.4.3实际保持pretrained hashed tables和token/projection固定，另以精确token序列索引edited-ngram cumulative update，激活时加到embedding output；不是直接更新pretrained hashrow。这样避免hash collision耦合新增edit，但同一真实ngram多表达reuse仍共享，附加存储随distinct edited-ngram增长。四生成表达/五prefixcontexts、至多25步target反传、batch100/2000→5000编辑、Wikipedia频率估计及FP32直接solve均有费用；不由‘decoder冻结’称零成本或零全局影响。

评价分责：T1原prompt efficacy高不等heldout expression generalization；CounterFact Specificity85.2低于pre86.8，不能写无影响。ZsRE reference-next-token postaccuracy会把新纠正混进保留；本轮不采用C1.3精确transition数字。MQuAKE standard与CoT最长输出32/128不同、一个case任一问法正确的endpoint不等所有问法/同compute质量；不采图像‘3×’性能。六general任务各100例mean weightedF1非benchmark标准全人口，MRPC退步保留。T2去joint/regularization/表达有条件消融，不能认证任意层或架构皆有同效；related-disable支持有限memory参与，不给edit真实性签字。实验counterfactual目标也不是verified现实事实。

Actual唯一owner MODEL-EMBEDDING，Ch12 actual272–310完整token row→hashed ngram容量→collision/MPHF/EngramNine→data-aware routing，及开篇和Ch11/13入口。旧body承载地址碰撞/容量/注入，但未区分表达触发覆盖、真实ngram共享更新与精确序列overlay，亦未承载matching目标与不相关保留的分验。拟EngramNine完整段后/扩大词法容量段前一段，不改原MPHF与hash路径。

### 逐字最小PRE（已独核/已写，actual POST通过）

已有词法容量还可成为受限编辑接口，但改一个问法命中的行不等改好了同一事实：不同表达触发不同 n-gram，同一个 n-gram 又可能被多表达复用。可以先冻结 decoder，为多表达求共同的 memory-representation 目标，再把表达到真实 n-gram 的共享关系写成联合匹配问题，以长度/频率的复用惩罚分配更新。[受限编辑对照](https://arxiv.org/html/2610.10533v1)采用精确 token 序列索引的累计更新 overlay，激活时加到读出，原 hashed tables 保持固定；这避免新增编辑被地址碰撞耦合，不消除相同 n-gram 的语义复用或全网络输出影响。线性解属于所用加性聚合，门控或上游依赖变化须重建优化关系；原问法命中、跨表达迁移、未改知识保留和任务质量分别验收，部分指标仍退步，post-edit 准确率也可能用新纠正掩盖旧正确丢失。表达制备、反传求目标、共享系统求解、频率统计与随编辑增长的 overlay 均计费，decoder 冻结不等免费或正确事实已获认证；覆盖、保留或成本不合格时保留普通查表与已有知识更新路径，不由编辑成功给任意关联问法签字。<!-- source-family:SF-2026-ARXIV-2610-10533 -->

review_mar11_continue非作者必要Source/actual Ch12 owner/逐字PRE PASS，独立记录live-20261009-evaluation.md。root授Ch12 EngramNine完整后/扩大词法容量前本段与本人注窄锁，作者已写且完整邻接/自身注实际顺读；root非writer实际288–315完整邻接、新298与本人403注actualPOST通过，锁释放。仅本项实际整合，不授DAY。
