# Jun12 补遗漏首批：必要证据、actual owner 与唯一稿

作者：`supp_jun12`；非作者准入校准：root 已实际读五项 exact-v1 题摘，同意 12117=6、11722=5、12299=7、12366=6，11260=N。本文件不签独立证据/PRE/POST/DAY，未写 Books。日期只用本日原字段与合同合法联合界，不把提交、登记或 created 改名为实际发布时间。当前 v2/v3 不倒填 v1。

## 12117 — Soft-Prompt Tuning for Fair and Efficient LLM Benchmark Evaluation

- 精确原件：[v1](https://arxiv.org/html/2606.12117v1)，§3.1–3.4、§4.1–4.2、Appendix A.9 已实际读。`v1=2026-06-10T14:12:19Z`；DataCite 同 DOI `registered=2026-06-11T02:13:12Z`，最早正常公告界 `2026-06-11T00:00:00Z`，两界全在 Jun11 BJT；需与同 DOI `arxiv.content/findable` 原字段联合，不证明全球首公开。
- 核心：冻结 θ，仅训练 L=10 prompt vectors；80步/640训练样本，以训练—测试分离控制适配预算。closed-ended knowledge proxy用选项log-likelihood，format用自由生成是否为合法选项；open-ended两项都由Qwen3-32B判。
- 对照/直接反侧：七个base/post-trained模型、七数据集、三seeds，lm-evaluation-harness zero/few-shot。格式与知识proxy曲线分别报告。开放题judge不能完全分离两者，A.9给出答案错误但格式正确却被判格式失败的实例；MATH500 ranking中few-shot略胜。其“GT”是soft-prompt过的post-trained同伴，不是独立真实知识/最佳下游性能。小参数或冻结backbone不证明没有学习/记忆；不采“post-training几乎不加知识”的普遍因果结论。
- 费用/配置：batch8、AdamW、1GPU但型号/precision/完整运行时未披露；训练、checkpoint选择、额外prompt tokens与双重评分付费。非在线吞吐/SLO研究，不推线上性能。未核实现、未复现。
- actual owner：`PLATFORM-EVALUATION-SYSTEM`，Ch66“Observed Capability 与 Elicitation Ceiling 必须分开”已有自然行为/监督后lower bound，但无小容量format-adapter与closed/open proxy分责；主张是新的受限评测分支，不把soft prompt实现复制到Prompt owner。
- 唯一拟稿（待 root PRE/窄授）：

格式遵循也可能挡住可观察能力，但为改善格式而做的适配仍是一次训练干预。可冻结模型权重，仅在训练划分上优化少量连续prompt vectors，再把自由生成的格式有效率、答案准确率与不需要自由格式的选项likelihood分别报告；适配预算、数据划分与prompt artifact须进入evaluation identity。它是一条有代价的elicitation分支，不是未经适配模型的原始分数，也不能由冻结权重断言没有获得任何任务信息。

[受限软提示对照](https://arxiv.org/html/2606.12117v1)中，格式指标改善而知识proxy近稳，支持先查format bottleneck；开放题judge却会把答案错误误判为格式错误，MATH500排名也非这条分支总胜。适配后的post-trained模型只是该研究的reference，不是真实知识或未来训练质量的oracle。prompt优化、额外token、选择与独立评分均付费；预算、判分或留出支持不齐时，保留原zero/few-shot、完整无效输出与独立内容评分，不从更高分推断纯知识增量。

## 11722 — ICA Lens: Interpreting Language Models Without Training Another Dictionary

- 精确原件：[v1](https://arxiv.org/html/2606.11722v1)，§3、§6、§9已实际读。`v1=2026-06-10T06:53:58Z`；同DOI `registered=2026-06-11T02:04:39Z`；最早界 `2026-06-11T00:00:00Z`，联合限定Jun11 BJT。当前v2题目、9B、43x等不用于v1。
- 核心：在normalized/centered residual activations上whiten再FastICA；读映射R与回写pseudoinverse D分责；strict max-LIM失败时p95接受但逐component保留稳定性标签，必要时减小component数重fit。row normalization放弃raw norm；compact最多d组件，不能承载SAE overcomplete词表。
- 对照/直接反侧：GPT-2 Small、Gemma2 2B、Qwen3.5 2B，1M Pile-10k activations，context1024；八sparse-probe数据集、相同feature budgets/splits，三模型各两层。signed ICA/PCA拆正负坐标；TPP仅两数据集/指定层，删除top-N后测target/non-target probe。小中N较好、大N时SAE可更强；这不是完整模型行为或天然独立因果feature。p95仍保不稳尾部，不授所有方向converged。
- 费用：cache百万activations、whitening/refit、独立probe/annotation均付费；未核代码、未复现，不采未比全费的统一加速数字。
- actual owner：`WORLDVIEW-REPRESENTATION`，Ch5“分布式表示与Superposition”/“从可读出到机制”已有SAE及readout—intervention证据阶梯，无compact nonGaussian rotation与p95尾部契约。
- 唯一拟稿（待 root PRE/窄授）：

解释表示不必一开始就训练overcomplete字典。另一分支先对白化后的activation寻找非高斯旋转，得到紧凑的signed coordinates；读取映射与把编辑送回activation的逆映射须分开保存，降维后后者只是pseudoinverse重建。对少量慢收敛方向，可保留整体探索结果但逐方向标记不稳尾部，不把分位数停止条件写成每一项都已稳定。

[有限ICA对照](https://arxiv.org/html/2606.11722v1)在相同probe数据、预算与划分下支持这条轻量探索路线，却只测指定层和proxy干预；较大删除预算时SAE可更好。去除activation norm改变了拟合对象，最多d个方向也不能取代overcomplete的细粒度表示；可解释标签、probe可读与真实行为机制仍分别验收。activation采集、白化/refit、标注和回写测试都付费；稳定性、重建或选择支持不足时，保留原activation、SAE/其他basis与独立行为检查，不由非高斯性批准安全编辑。

## 11722 current-v2：仅受影响采用层定点恢复

当前真实结果：root§27受影响必要/owner/唯一第二段PRE→作者仅替第二段和本人注→root唯一§30实际POST通过，采用层恢复关闭，I仍唯一原家族，不重复计数/评分，窄位释放。

2026-10-26 06:54～07:13 BJT实际current abs发现“substantially revised from v1 / comprehensive re-evaluation”说明，root授权作者为唯一首次必要准备者。精确当前原件为[v2](https://arxiv.org/html/2606.11722v2)，current history显示2026-10-19 17:23:26 UTC（按原字段=Oct20 BJT），仅作窗外重要revision线索，不重归Jun11、不另算家族或给本日重复评分。原Jun11 v1日期与root§4真实POST仍是历史检查事实；受影响采用层重新待核，不宣告旧全文失效。

实际只读对应原已采用的§3.3.2/3.3.3、B.1读取/回写与预处理、B.4/B.5有限稳定性、C.1明确feature orientation、E.1/3/4对应probe/TPP协议，不读全版diff、完整新interpretability/annotation或全模型扩表。需要C.1/E.3–4是因为v2定义的feature/干预与v1笔记保存的signed split不同，不能从主文“同预算”跳过这个身份变化。

- **不是只有扩9B模型**：B.1现在直接对raw residual减均值/whiten，保full d；不是v1 row-normalization后对象。read方向`UΛ^-1/2 w`与write方向`UΛ^1/2 w`为dual pair，保mean/U/Λ/W；原空间不要求各自orthogonal。v1降维pseudoinverse仍数学上可作分支，但不应暗示当前默认降维或丢norm。
- **稳定性不再等同旧p95停止recipe**：v2主实验固定50iter，以population nonGaussian统计约50轮平台作为工作点；B.4 GPT2L6五seed/同1M activations Hungarian绝对cosine匹配，50轮median约.82–.85、200轮.90–.91，仍有low-sim tail。B.5区分population饱和与单direction LIM/跨seedidentity继续稳定；不是证明每component收敛。旧“别把分位数停止当全稳定”的一般边界保持合理，但旧p95实现不能作为当前默认机制。
- **probe/TPP测量身份发生实质变化**：E.3仍相同k、4000/1000 split、8任务/每模型两层，v2probe用skewness-oriented signed score乘write-norm；C.1/E.4的TPP为selected-tail正half-wave feature，不是把ICA两sign拆成两个无条件可替代坐标。v2同样保原reconstructionerror并只删该正tail；预算k因此不等任意不同编码下相同干预强度。TPP仍仅target-v-nontarget probes，不升全模型行为因果。新版声称受测sparse区间TPP更高，不能倒填v1“大N SAE可更强”或拿新版结果签旧ranking。
- **纠错性质结论**：当前Comments明确全面重评；定点原文展示预处理、默认停止/稳定性度量与feature/干预定义改变，故是影响旧采用口径的revision，不是仅扩模型。已读部分未明确说“v1数据错误/撤回”，不可自行定性全v1错误，也不声称已排除所有实现纠错；新sign-sensitive correction直接针对既有早期ICA–SAE自动interpretability基线，本日报原书未采该新interpretability数字，不为此展开全C.4。无当前版本净性能量/新解释性真值进入Books。

**拟actual owner局部修正**：仅Ch5原11722两段的第二段与本人注；第一段read/write分责与不稳尾部契约仍成立，不删泛机制。原第二段将去norm、大预算排名写成无版本限定，需改成冻结preprocessing/feature/干预身份，保有限probe非行为因果、compact≠overcomplete与全费。不新开Books owner、不触及其他论文。

**唯一拟修正稿，待root必要/actualowner/PRE；尚未写Books：**

[有限ICA对照](https://arxiv.org/html/2606.11722v1)只支持指定层和proxy干预；比较时应冻结activation是否保留norm、component数、读取/回写及feature的signed-tail定义。[后续重评](https://arxiv.org/html/2606.11722v2)改变预处理和干预接口，population统计先饱和也不等逐方向或跨seed身份已稳定，不能把不同版本的预算与排名直接拼接。Compact directions不取代overcomplete的细粒度表示，可解释标签、probe可读与真实行为机制仍分别验收。activation采集、白化/refit、标注和回写测试都付费；稳定性、重建或选择支持不足时，保留原activation、SAE/其他basis与独立行为检查，不由非高斯性批准安全编辑。

## 12299 — Learning What to Say to Your VLA

- 精确原件：[v1](https://arxiv.org/html/2606.12299v1)，§4、§5、§6、Appendix7.2实际读；`v1=2026-06-10T16:34:49Z`；同DOI registered `2026-06-11T02:17:12Z`；最早界 `2026-06-11T00:00:00Z`，联合限定Jun11 BJT。
- 核心：narration提供local language-search proposal；交互rollout选择并RFT语言反馈policy；独立improvement head在初观察/原任务上预测相对原instruction的empirical Δ，再按有害校准子集score分位数决定是否steer，否则回原instruction。冻结VLA不等不训练、不交互。
- 对照/配置：π0.5-LIBERO/DROID，Franka腕部/第三视角，LFP Qwen3-VL-4B LoRA、Molmo2 narration、GPT5.4的16搜索扰动。模拟200 visual-semantic combinations、每项50rollouts，hardware每项30；table1模拟FPR38.92→9.31/refusal43.42→57.66，实机61.11→2.22/refusal9.72→24.72。开放loop71.3、逐phrase闭环70.4、trajectory闭环75.0均带SE，不能说任何闭环都胜。
- 直接反侧：保证要求cal/test exchangeable，Y由MC empirical improvement标记；任意OOD、真实损害与物理安全均不被保证。App7.2用q=s_(k), k=ceil((m+1)(1-alpha))且执行score>=q，未显式ties处理。具体反例：m=9、alpha=.1、所有harmful scores=0，则k=9、q=0，>=使所有有害例都steer，FPR1而非≤.1；不能将原式作为无条件有限样本保证采用。该反例不否认局部经验校准结果或风险接口。
- 费用：50视频/任务、narration/16搜索/rollout、LoRA/head/calibration与每步额外VLM推理全计费；precision bf16、train batch1，完整硬件/尾延迟/SLO未披露，controller授权不变。未核实现/未复现。
- actual owner：`MULTIMODAL-EMBODIED-VLA`，Ch26闭环主干目前把goal与controller分权，但没有“language steering是否切换”的有害类校准接口；evaluation章只保统计条件，不拥有动作接入。
- 唯一拟稿（待 root PRE/窄授）：

冻结的VLA可以先保留动作能力，只改它每步接收的语言，但改写并非总有益：同义指令可能被忽略，也可能触发更差动作。可先围绕行为narration搜索经真实rollout检验的语言序列，训练反馈policy；再另训improvement head，比较切换反馈与重复原指令的经验收益，仅在经校准的条件下切换，否则保留原instruction。语言提案、是否介入与低层执行由不同责任承担，不能由更顺的文本批准动作。

[受限语言干预研究](https://arxiv.org/html/2606.12299v1)支持有害类校准与拒绝介入的局部取舍，不提供任意OOD无害或物理安全：标签来自有限rollout，保证依赖cal/test可交换，原分位数公式在平分与非严格阈值下还需额外约定。Narration、搜索/交互、训练、校准与额外VLM闭环全付费；支持、校准或deadline失配时，保留原指令、可信controller、重观测或人工接管，不把冻结VLA或低FPR当安全证书。

## 12366 — APT

- 精确原件：[v1](https://arxiv.org/html/2606.12366v1)，§3、§4.1–4.2、E.6实际读；`v1=2026-06-10T17:34:25Z`，registered `2026-06-11T02:18:38Z`；最早界同为Jun11 00UTC，联合限定Jun11 BJT。
- 核心：continuous action expert先在半份pretrain数据上用冻结VLM/去语言输入学VA prior、仅激活N/2层；stage2 interleave新增N/2层、移除language mask并在全数据上联合优化，逐层sigmoid gate融合VLM features。prior并非stage2一直冻结，Bayesian factorization不证明模块实际分离/无shortcut。
- 对照/直接反侧：LIBERO-PRO、rigid pick-place，两stage与KI、FtVLM组合、π-style/GR00T-style与token insertion消融。Goal-Pos中APT低于π0.5；pick-place的joint variant并非所有UO/UC均最好，architecture/training-data等跨baseline混杂保留。实机每任务30示范，两pick-place共110/80 trials；E6仅10条UOUE轨迹，仍有push-after-grasp与跳过close-box，不能由平均成功认定language causality、termination或安全已解。
- 费用：两stage与动作层扩展、完整数据/任务适配、额外gate以及真实回归全计费；精确模型scale/hardware/precision/训练步数需仅在拟采对应性能数时再按A定点补，不以未读全文列外部受阻。未核代码/未复现。
- actual owner：`MULTIMODAL-EMBODIED-VLA`，Ch26“从只学Action到同时保存语义并对齐语言与动作”已有teacher/BC/semantic anchoring；“Action-facing Representation也是Gradient Authority Boundary”有mediator和freeze。具体VA warm-start再引language的分阶段分支仍缺。
- 唯一拟稿（待 root PRE/窄授）：

限制action梯度并非保留语言语义的唯一分支，还可先改变动作消费者的初始化。语言远少于逐帧视觉—动作变化时，随机初始化的continuous action expert可能先学视觉捷径；可先冻结VLM、不让动作层读取语言，用视觉—动作对训练VA prior，再引入语言条件与逐层gate，继续联合适配。第二阶段可以重开prior与VLM的训练权限，因而这不是永久隔离，也不由Bayesian分解证明真实模块已统计独立。

[有限两阶段对照](https://arxiv.org/html/2606.12366v1)支持把初始化、语言注入与stop-gradient分别验收，但有布局切片反退、跨baseline数据/结构混杂，实机仍会继续推或漏掉关盒步骤。两次训练、层扩展、数据/本体适配与闭环回归都计费；语言支持、空间鲁棒性或时限失配时，保留直接BC、knowledge insulation、语义回放/teacher与原策略，执行仍由真实观察和独立controller验收，不由instruction generalization批准物理安全。
