# Oct07 reader2 独立必要证据与 Books 判断

复核者：`/root/oct18_missing`（不是本日报告作者）；范围仅 Oct06 北京时间自然日内 root 条件准入的 04119、04808、04089、04473、04938。只写本文件，不改 Report、Books、索引。2026-10-20 13:57+08 开始分项保存；不是日级 DAY/FINAL，也不预授尚未读到的 PRE/POST。

## R2-1 — 2610.04119：Source/date 与具体 owner 差额通过

材料：[Copying Before Suppression: What Drives a Below-Chance Dip During Language Model Training?](https://arxiv.org/html/2610.04119v1)，实际读取本目录 `core-04119v1.raw.html` §1–6、Discussion/Limitations、Appendix D.1–D.5 与 H.1–H.6。支持与关键替代解释足够，未遍历其余无关附录/代码，也未复现实验。

**日期独核。** 2026-10-20T05:51:11Z 实际 GET [官方版本页](https://arxiv.org/abs/2610.04119)，身份与 exact-v1 一致；版本历史唯一 v1=`Fri, 2 Oct 2026 22:50:59 UTC`，当前页未见撤回/纠错提示。提交不当作公开。实际读本地 `datacite-04119.raw.json`：精确 DOI `10.48550/arxiv.2610.04119`，client=`arxiv.content`，state=`findable`，registered=`2026-10-06T04:26:20.000Z`。复用未变的官方历史公告/发号规则：v1 在周五 14:00 EDT 后，最早普通公告为周一 Oct05 20:00 EDT，即 Oct06 08:00 BJT；登记结合公告发号规则给最晚界 Oct06 12:26:20 BJT，整个可能区间均在 Oct06。此为联合约束，不把 registered 改称实际发布时间，不声称全球所有发布渠道已查尽。

**准入与评分。** 旧判断若只从成熟 checkpoint 的电路倒推早期，就可能把功能尚未形成误写为同一电路的弱版本；本稿以跨 checkpoint 的有害复制、后形成抑制以及成熟参数回植的部分救援，给出可证伪的局部非单调能力形成解释。评分 **2+1+2=5**：重要机制/边界；所采用命题仍局限模型训练轨迹与内部诊断，不因能联系多个章节就给跨系统 reach；约束可复用。标准审阅最低要求已满足；因确认 Ch5 长期缺口，额外深入相关因果控制，不为增加工作量抬分。

**采用证据与反证。**

- 主实验是 Pythia 160M/410M/1B 的结构化 IOI，另有独立训练160M与9个 PolyPythia seed 支持行为低谷；forced-choice=IO 与重复名 S 的二选一，不是全词表准确率。总体 Pile loss 下降并不消除任务低谷，但这本身不是新机制。
- §3 对第二次名字出现位置的 residual patch 在低谷改善、成熟时破坏；随机匹配范数扰动也可呈反转，所以它定位因果作用，**不单独识别 duplication-specific feature**。
- §4/D.1–5：筛选、验证排序、控制均值构造与最终评价分离；冻结头集合，均值控制组与评价组 names/templates 不相交。选头输出替换在四个低谷均改善 IO−S，template→item nested interval 均为正；更严格三名字 margin 的 interval 在独立160M和1B跨零，不能称所有对照均稳健。仅替换第一名字位置的 value、固定第二次名字与其余模型后，贡献跟随 donor 身份；四组 margin 的 nested interval 均为正，支持有害贡献确实承载名字复制，而非只与重复名 logit 相关。
- §5/H：成熟时固定选择的抑制头参数 Q/K/V/O 与专属bias回植早期模型，其他参数不动且激活由早期模型自身重算；三个规模分别关闭 **35.3%/67.9%/40.5%** 的低谷到成熟 LD 差额，属部分充分性，不是完整恢复。8个随机成熟头参数控制明显较弱，但不是等参数或head-for-head匹配；单头 output-norm-matched graft 是不同因果问题，不能合并成同一对照。把早期头输出放大2–16倍仍未过 chance，反驳“同一成熟操作只是幅度小”的简单解释。
- 成熟抑制头移除后 forced-choice 仍高于 chance；410M再加入 correct-name writers 才进一步重建，不能把一个头称为完整成熟电路。为何训练先学复制、后学抑制仍未由改变数据/优化路径的干预证明；更大模型、其他任务只有有限扩展，不能声称普适训练定律。

**实际 owner 比较。** `WORLDVIEW-REPRESENTATION` / [Ch5](../../../../../books/part-01-worldview/05-what-neural-networks-learn.md) 的“从可读出到机制：证据应逐级变强”（约312–370行）已有 correlation→decodability→intervention→跨环境证据阶梯，以及 sufficiency 不等 necessity、局部解释限制；“工程上怎样验证模型学到了什么”（约493–538行）已有总体指标/切片/干预及基底比较；“行为方向可能早于 Post-training 形成”（约646行）已有行为方向可在预训练出现。相邻 Ch4“训练成功为何不等于系统成功”已有 loss≠任务成功，Ch6 开篇承担架构 content-dependent routing。上述均没有承载 **同一组件作用可随 checkpoint 反转、低谷中有害复制与稍后抑制竞争、用成熟参数自身重算的部分充分性来区分缺功能与弱幅度** 这一具体链。建议最小整合 Ch5 的证据阶梯内（不是章末继续追加），保留原 probe/干预原则；不能只新增“loss不能代表能力”这条已有常识，也不在 Ch4/Ch6复制机制。

Source/date/owner 差额结论：通过，允许作者提出上述窄命题 literal PRE；**尚无逐字稿，PRE/实际 Books POST 未通过**。

## R2-2 — 2610.04808 Alkaid：Source/date 与 Ch49 差额通过

实际读 `core-04808v1.raw.html` 摘要、§I–V（核心 III-A/B/C/D、IV 及 Tables III–VI），精确来源为 [v1 HTML](https://arxiv.org/html/2610.04808v1)。论文尾部仅References/HTML错误反馈，没有必要附录待审；不核代码或复现实芯结果。

**日期。** 同批实际 GET [官方版本页](https://arxiv.org/abs/2610.04808)，唯一 v1=`Sat, 3 Oct 2026 23:24:05 UTC`，当前无具名撤回/纠错信号；实际本地 `datacite-04808.raw.json` 为精确DOI、`arxiv.content`/`findable`、registered=`2026-10-06T04:42:52.000Z`。依 R2-1 同一官方规则，最早界 Oct06 08:00 BJT，最晚界 Oct06 12:42:52 BJT，整个区间落本日。不是把提交日或登记日单独当公开。

**准入/评分：2+2+2=6。** 旧 ML→FPGA layer-template 对支持模型方便，但新增算子与前后处理不易承接；算术中心 SSA IR 保存任意固定点 bitwidth、算术依赖与显式量化，统一 lowering、位宽优化与 synthesis-free 估价，再由真实 place-and-route 验收。增量是**静态超低时延数据流里的 numeric IR/估价共同设计与其具体失效域**，不是 Python接口或又一个模型部署工具。Reach 跨编译表示、数值语义和物理实现，仍不授 LLM serving 或通用加速器结论。标准完成，并为长期 Ch49 缺口深入相关实现/反证。

**机制与评价。** III-A 的13类低层操作保留 fixed-point/heterogeneous bitwidth；bit-extension/concat 在算术语义内，避免过早分解成位操作。Tracing 阶段用 affine arithmetic（不适用时退 interval）追踪中间增长、局部优化；构图后再迭代 CSE/dead-op/canonicalization。用户须显式量化权重/操作：没有隐式量化，未限制的中间位宽可能不可综合。White-box cost 为硬件pin/结构分析加微基准拟合，不是无校准第一性精确公式；模型主要估 LUT 和组合延迟，不覆盖完整FF/DSP/placement。

IV 基准除另说明均为 Vivado2025.1、UltraScale+ VU13P `xcvu13p-flga2577-2-e`、out-of-context post-routing，输入输出registered，latency=cycles/Fmax。JSC HLF MLP 与 PLF GNN/Transformer（至多16/32 particles）比较固定训练模型的 **bit-exact RTL/HLS**，同accuracy不是另训模型增益；若引用20–30% LUT下降，仅限与 da4ml/hls4ml+da4ml 比较的这些神经网设计。部分Transformer latency几乎不变，不能笼统称40%加速。2410设计的估价与 post-routing 对照一般 LUT误差<10%、latency<20%，不是逐项误差上界；clock target、拥塞、工具版本及跨SLR可超出模型。JEDInet为保持原hls4ml accumulator overflow关闭完整da4ml优化，原hls4ml未routed，**不得比较实际 latency**；虽II1对2也不等同端到端SLO。TreeLUT对比重新拟合且时延计数调整，不是bit-exact同模型；非ML的Altera/Quartus演示仅证明有限后端接入，不授全平台同收益。

**采用边界/成本。** 当前是编译时图/shape/type已知的stateless全流水静态kernel，PE reuse、throughput–area折衷和更大模型仍未来工作；算术IR不负责高层调度/编排。RTL生成通常小于一分钟、估价小于一秒不意味着完整综合免费（作者神经网逻辑综合至约50分钟）。无LLM token lengths/batch/concurrency/SLO，因为并非动态LLM服务评价，不能自行补这些字段或把科学分类效果写为研究贡献。

**owner差额。** `INFER-TENSORRT-LLM` / [Ch49](../../../../../books/part-05-inference-system/49-tensorrt-llm.md)：实际读119行起 lowering/数值commit、709行起硬件代理、1921行起layout/cost-model独核和2168行起专用加速器workload contract；已有“可编译≠正确/快”“cost model须实测”“专用性依赖workload”，也有受限HLS协议变换。新增不是重复这些原则，而是 **固定点算术IR保留依赖以收紧中间位宽，并让同一低层结构供白盒资源/延迟估价；bit-exact溢出语义和post-routing失配形成两道不同边界**。建议在 lowering 论证内增加静态FPGA替代分支，邻接已有HLS段；不要开孤立Alkaid节或把它当GPU runtime继任。相邻Ch48负责分布保持speculation、Ch50负责动态request/KV协同，不承接这份numeric IR机制。

Source/date/owner 差额：通过；**等待逐字 PRE，未授 PRE/POST**。

## R2-3 — 2610.04089 Pareto-Dominant Clarification：限定命题 Source/date 通过

实际读 [exact-v1](https://arxiv.org/html/2610.04089v1) 本地 `core-04089v1.raw.html` §1–6、Limitations、Appendix A全部必要实现/预算/选择细节、B/C直接反证；未遍历无关episode附件，不核代码。官方abs同批实际GET唯一v1=`Fri, 2 Oct 2026 21:54:46 UTC`；精确DOI本地DataCite为`arxiv.content`/`findable`、registered=`2026-10-06T04:25:36.000Z`。按R2-1历史规则，下上界 Oct06 08:00–12:25:36 BJT，全落本日；当前页未见撤回/具名纠错。

**准入与分数。** 已有ask/assume gate不能仅按“多问更稳”选择：受限对照显示同一未训练编码模型的澄清工作点可被同时更少问题、更高测试成绩的策略支配；预算约束的有效/失效区域及部分独立run，使长期增量是**可学习的期望问题预算分配及不能升级为运行时保证的边界**，不是新PPO/CMDP算法，也不是把成熟RL换任务就准入。**2+1+2=5**：重要局部policy边界、单个交互决策负载、可复用约束。标准完成，为明确Ch81缺口深入Appendix A/C。

**实际机制。** Qwen2.5-Coder-7B-Instruct LoRA，三value/GAE streams分别为terminal测试奖励、原子问题数、turn数；按batch超预算调非负Lagrange multiplier。问题按simulator数出的atomic requests计，而非把一个含多问的turn当一问；用户模拟器同时握完整oracle，不能当无偏真实用户。`[ASK]`/`[ANSWER]`用两token prefix近似评分，PPO ratio**排除prefix**，routing仅通过共享LoRA continuation梯度间接改变；不称决策token已被显式直接优化。d2=4的turn multiplier全部为0，Tmax=6硬cap才是运行时截断，不宣称双预算均有效。

**评价/成本。** HumanEvalComm全为人为退化coding任务；按base problem分split以免不同退化泄漏，303训练/52验证/417测试，greedy、相同prefix routing/turn cap与frozen baseline。论文叫pass@1的量实为**每题通过hidden assertions的比例均值**，不是通常一次生成全部通过率。七budget、十policy，仅d=.5/.75/1有双seed，80iterations×32episodes，约11h/2×A100-40GB每policy，另有simulator API；无production throughput、batch/SLO评价，不能报成真实人工摩擦节省。

**支持与关键反证。** d=.75两run score=.748/.761 vs baseline.690，平均问题=.719/.782 vs.856，两次均显示更高score/更少问题；这是局部Pareto证据。d=.5两run .683/.719，“与baseline无显著差异”**不等证明无退化或非劣效**。d=.75之一均值.782已高于目标.75，作者未拒绝超预算假设不证明预算满足；d=.25验证可行、test=.417违约，d=1另一run1.072也违约。Frontier取满足预算的run、违约run另报，应保留选择条件而不把拟合log curve作为普遍定律。大budget multiplier趋0的近无约束PPO仍提升成绩，故不能把全部质量增益归Lagrange约束。相同1Q子群提升不能拆分question targeting与code quality，而且pooling两run复用相同base测试项，不是490独立问题；论文自己承认未做冻结coding头等干净归因。模拟器确定性、有限seed、小训练集和自然歧义迁移均限制结论。

**具体已有差额。** `AGENT-WORKFLOW` / [Ch81](../../../../../books/part-07-agent/81-workflow.md) 263行起已有clarification gate/detector与用户budget/call混杂；约279行已有missing-info type、timing、rollback、remaining budget；852行起已有approval独立与human handback。相邻Ch80约309行已有belief→answer/clarify/abstain，Ch82开篇限制多agent必要性。这些正文**尚未承载按atomic request训练期望预算、用质量–问题数联合工作点检验，以及训练均值控制不保证test/每episode合规**。建议Ch81既有澄清段内插最小机制+反证，保留detector/timing与硬权限路径，不能把期待成本控制写成授权或安全硬门禁。不为本稿另改Ch32 PPO owner，不复制成熟算法推导。

限定Source/date/owner差额通过，允许窄literal PRE；**PRE/POST待实际阅读，不能预签**。

## R2-4 — 2610.04473 InferOpt：窄机制/边界 Source/date 通过

实际读 [exact-v1 HTML](https://arxiv.org/html/2610.04473v1) `core-04473v1.raw.html` §1–4、Tables1/2、Figure2说明及AppendixA（正文短，支持与关键反证已足够），不追代码或未披露实验。官方abs同批实际GET唯一v1=`Sat, 3 Oct 2026 12:19:09 UTC`；本地精确DOI DataCite=`arxiv.content`/`findable`、registered=`2026-10-06T04:34:44.000Z`。按同一规则下上界 Oct06 08:00–12:34:44 BJT，本日资格通过；未见具名撤回/纠错。

**准入与评分 2+2+2=6。** 不把TPE+proxy+Pareto的模块组合宣称新优化算法。具体可保留的是：同一平均预算下，不同层分配可同时改变有损质量和真实执行效率；因此在搜索接口里分开**便宜确定的架构资源代理、冻结人口上的质量排序和最终真实运行复验**，而不能只调selector或把一个uniform点当预算最优。两个异构配置空间支持这条选择边界，不证明统一框架普适优于全部机制。Reach横跨KV/路由配置与执行，非单个性能数字。标准完成，因具体Ch49缺口深入所需反证。

**接口与未披露。** §2把variable domain、ResourceCost与evaluation hook分离；在KV28维mean retention上，over-budget先拒而不做昂贵前向，冻结proxy再更新Pareto及收紧budget。**MoE26维top-k试验没有总expert硬约束**，不可把KV前置预算拒绝的实施范围推广到MoE。成本只是均值retained block/expert，不是显存、latency或energy；confidence sampling与adaptive budget更新没有足够公式/实现细节，故不写成可复现recipe，不声称验证其具体优化实现。0.02 MoE quality tolerance只作标签，不是质量硬可行性门禁。

**可比证据。** Qwen2.5-7B-Instruct、bf16、LongBench21任务，210固定proxy/1050 held-out；保护prefix128/recent512，同mean middle retention .321，allocation与selector分开对照。相同selector下layer-wise对uniform高3.21/6.13 **绝对质量点**；所谓7.3/14.0是相对Full-KV43.83分的比率，不是再多7.3/14绝对点。所有压缩仍较FullKV下降5.79–10.78点，不能写无损。DeepSeek-V2-Lite-Chat的384proxy/768heldout对照中，∑k=89的三个分配具有同routed pairs，却有不同TPOT；near-uniform/entropy控制在winner已知后才构造，只能作post-hoc分配验证。取“离uncompressed分数更近”而非分数更高为目标，也不能推出更正确。

**反证/费用。** MoE proxy→heldout Kendall τ=.59，80%proxy-front保留，说明代理只支持粗排；KV proxy loss约.053点的最佳搜索点不能与另一个heldout .321工作点拼为无退化保证。Random/NSGA-II/MOTPE的24trial比较没有adaptive-tightening，未见完整component ablation、独立seed及等总搜索墙钟账，不授全部收益唯一归给某组件。原文只披露单GPU/Python3.11/PyTorch2.5.1/bf16，**GPU型号/batch/concurrency/SLO未披露**。KV系统矩阵4K/8K/16K、生成128token、一次warmup/十次测量；主表16K TPOT/缓存是局部路径，不是整个serving吞吐或端到端TTFT，FullKV称generation-only，不能补称包含prefill/pruning/search开销。MoE8K系统数据也不证明生产SLO。搜索、proxy构造、full再评分及压缩/布局管理均需另外计费。

**具体owner差额。** 实际读 `INFER-TENSORRT-LLM` / [Ch49](../../../../../books/part-05-inference-system/49-tensorrt-llm.md) 的typed-system-IR搜索（525行起）、tactic资产（921行起）和cost-model独核（1921行起）。已有proposal/合法性/真实measurement分权、profile身份及模型最优≠真实最优，但尚无**有损层级配置里确定成本前筛/冻结质量proxy/heldout排序衰减，与相同均值预算不保证相同质量或执行成本**这一具体接口链。Ch45实际读446行起eviction/604行起depth变化，已有许多压缩策略与质量–容量–时延三轴；不在其下重复generic搜索。建议Ch49调优资产邻接最小加入上述机制及τ=.59/同预算反证，明确它不是semantics-preserving IR变换的证明；Ch48和Ch50的交接仍分别由exact speculation及动态engine负责。

Source/date/具体差额通过；仅支持上述有限采用，**等待literal PRE/实际POST**。

## R2-5 — 2610.04938 D-DOIT：通用离散采样机制 Source/date 通过

实际读 [exact-v1 HTML](https://arxiv.org/html/2610.04938v1) 本地 `core-04938v1.raw.html` 完整题摘、§1–3、§4.4–4.6/Discussion，以及Appendix B证明、D估值偏差、G费用与L.5–7直接相关控制。§4科学效果表仅用于辨识实验范围，不采用DNA/蛋白应用成效，也不以这些成效入选；没有扩展生物/科学研究路线。未核artifact/复现实验，不遍历其他领域附件。

**身份/日期。** 同批实际 GET [当前官方版本页](https://arxiv.org/abs/2610.04938)，v1=`Sun, 4 Oct 2026 04:34:02 UTC`，v2=`Thu, 15 Oct 2026 01:36:58 UTC`。本次明确采用v1，不用v2摘要替v1结论，也不从版本号变化推重要修订。随后实际读本地 `datacite-04938.raw.json`，DOI=`10.48550/arxiv.2610.04938`、client=`arxiv.content`、state=`findable`、registered=`2026-10-06T04:46:04.000Z`。同一历史规则下上界 Oct06 08:00–12:46:04 BJT，全落Oct06；不是声称registered为精确首发时刻，无具名更早正文/撤回信号触发额外追查。

**准入与评分 2+2+2=6。** 连续score/drift correction不能原样搬到categorical不可逆reveal：冻结reverse kernel须在转移概率上乘下游终点权重的条件期望比；真正实现又用head completion代替未来rollout。长期差额是**精确目标/局部核与可执行近似的分界，以及单步干净补全不等多步条件终态**；不是Doob定理名称或科学reward数字。Reach跨base sampler、clean-head预测与black-box reward接口。标准完成，因Ch24已确认具体知识差额，深入证明/近似反证。

**核验的理论。** §2/Theorem2.1与AppendixB在固定有限序列/词表、β>0、正且有限normalizer、冻结reverse-chain支持与Markov路径下，令φ(x)=exp(R(x)/β)，h(x,t)=E_P[φ(X0)|Xt=x]。由tower property，P^h(y|x)=P(y|x)h(y)/h(x)归一化；deterministic all-mask初态使h(mask)=Z，路径比telescopes为φ(X0)/Z，因此终态为pθφ/Z。若初始状态不是确定mask，不能直接保留原初始律就继承此结论。它不是任意learned-head估值/有限候选实现的精确性保证；reward也不拥有事实/安全真值。

**执行近似与反证。** §3从当前state共享一次proposal forward，抽M个candidate；各candidate再跑head，在未揭示位置独立抽clean tokens、固定revealed token，用black-box reward weight重采样下一state；一guided step为1+M模型序列级NFE与M reward evaluations。多completion只降低head-expectation抽样方差；AppendixD说明未来head会随新增context/time改变，所以其factorized completion一般不等rollout条件律。即使M或completion数趋∞也不能消除这个系统偏差。实测matched-state pooled h-summary相近不证明逐state条件律相等，KS在此是CDF距离不是显著性检验。

Proposal temperature τ≠1改变proposal，原目标需要P/Q importance ratio且support覆盖；作者执行配置省略此ratio。Completion temperature γ改变估值对象，非单纯降噪；ω sharpening对随机h的幂与对期望的幂不可互换，不能统称只是原target换个温度。Late best-of-K共享prefix、只付suffix分支成本，但不能撤销已reveal token，terminal argmax也改变输出律。高ω控制呈接近best-of-M的weight concentration，ESS低不是终态多样性或distribution accuracy的证书。以上是采用必须相邻写出的界，不能写“training-free精确采样”。

**适用/费用。** 通用机制无需reward梯度/主干重训，却每步新增head及oracle计算；NFE按sequence-level forward，物理batch调用/总墙钟另算，terminal ranking未缓存时还至多K次reward。AppendixG明确多completion若复用同head概率可不增模型NFE但增加oracle次数，不能以模型budget匹配声称总费用匹配。具体实验限小词表生物序列与A100条件，尚未证明大词表文本、多模态或服务SLO；只吸收理论接口、估值偏差和可逆性/预算边界，不采应用效果或任何领域设计建议。

**owner具体差额。** `MULTIMODAL-GENERATIVE-PARADIGMS` / [Ch24](../../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)：实际读约686行起h估计/连续Doob/DOIT、782行masked-reveal、1776行离散Feynman–Kac与2185行rate-policy/reward接口。已有连续`∇log h`、one-step terminal surrogate、离散particle path reweight和“终点奖励不认证事实”，故不能只写无梯度reward/多采样付费。真正差额为**categorical candidate核的乘性h比→head direct-completion与rollout条件值的偏差→proposal温度/terminal selection各自破坏原目标精确性**，以及共享prefix的不可撤销suffix分支。建议在现有连续DOIT段之后增加受限离散替代分支，不复制通用RL或领域应用；相邻Ch23拥有representation/codec，Ch25拥有action-conditioned environment state，不接管这一sampler概率接口。

Source/date/具体差额通过，允许仅通用采样机制literal PRE；**尚未PRE/POST**。

## R2-6 — 首两项 literal PRE（2026-10-20 14:11+08）

实际逐字读作者 `READER2_PRE.md` 的04119/04808单段及本文件已读owner前后。04808在Ch49 Relational-Hoare HLS段后的一段通过。04119原“区分尚未具备相同操作与仅幅度小”要求收窄；作者已保存为“支持计算本身发生变化、而不只是原操作幅度变小的解释”，本reader实际读回该句及整段，**修订态literal PRE通过**。两段保原机制、成本、反证与fallback，允许root协调的窄写；来源链接应在正文或本人注明确指向exact-v1。此处只授逐字PRE，**实际正文/本人注尚未读，不授POST**；本人不写Books。

## R2-7 — Alkaid 实际 Books POST 通过

2026-10-20 14:13+08 实际读 Ch49约135–151行完整局部：RVV交接、原Relational-Hoare HLS两段、新唯一Alkaid段（144行）、原模型IP/shell段及后续数值回归交接；并实际读约3242行本人注含exact-v1链接。新增与已批literal一致，numeric语义/估价/最终实物分责、静态范围与失败回退保留，未静默覆盖既有HLS协议或shell机制；本人注仍如实待非作者POST，没有伪称复现。本条现授 **04808单段+本人注实际POST通过，窄锁可释放**。作者可仅同步本人注真实POST层；后续措辞若改再按影响核查，不授日报完成。

## R2-8 — 04119 实际 Books POST 通过

2026-10-20 14:15+08 实际读 Ch5约315–337行完整局部：原证据阶梯与“完整机制”段、新唯一331行段、后续“内部读数的预测用途应与因果解释分别验收”及其控制；实际读约851行本人注的exact-v1、5分及限制。新段与收窄后PRE一致，checkpoint功能反转、复制身份干预、后抑制/参数自身重算部分充分性均有支撑，仍明写三名字/随机头控制不完全与训练路径成因未证。既有阶梯/相关性vs因果边界未被替换，后文交接自然。**04119正文+本人注实际POST通过，窄锁可释放**；作者仅同步本人注事实层，不预授整日DAY/FINAL。

## R2-9 — root 同日追加三项的日期有限独核

root明确追加只读06394 HarnessHOI、04537 PhaseGate、05748 MOLT的必要Source/date/owner与后续PRE/POST；不重复其05559，不扩其他材料/日期。首五项尚待三份literal时，独立推进可执行日期核验；不预签尚未读到的Source。

2026-10-20T06:15:40Z 实际GET三个官方abs，各精确身份/唯一v1、无具名撤回/纠错：06394=`Mon, 5 Oct 2026 14:16:28 UTC`，04537=`Sat, 3 Oct 2026 14:07:04 UTC`，05748=`Mon, 5 Oct 2026 03:53:21 UTC`。实际读本地对应DataCite原件，均精确`10.48550/arxiv.2610.<ID>`/`arxiv.content`/`findable`，registered依次为`2026-10-06T05:24:32.000Z`、`2026-10-06T04:36:15.000Z`、`2026-10-06T05:06:53.000Z`。三v1均位于周五Oct2 14:00EDT后、周一Oct5 14:00EDT前，按复用规则最早公告均为Oct06 08:00BJT；最晚分别13:24:32/12:36:15/13:06:53BJT，同日区间成立。提交、registered均不改名实际公开时刻，不追假想所有first-public渠道。一次早先并行请求未保留可读输出，没有据其签判断；上述为随后实际取得并读到的官方history。

## R2-10 — 06394 HarnessHOI：必要 Source/Ch23 差额通过，但修正对照归因

实际读 [exact-v1](https://arxiv.org/html/2610.06394v1) 本地 `core-06394v1.raw.html` 完整题摘、§3.1–3.4/4.1/4.3/T3–4、D.4–D.5、E.2/E.4/E.5、Conclusion；仅必要机制/核心反侧，不遍历领域附件，不核代码或复现。日期见R2-9。

**准入/评分2+2+2=6。** 多源视觉候选先保persistent instance identity、原图坐标及source view，再按对象identity/category/visible extent统一选框供关系consumer读取；消除的是表示/消费接口中早期关系提议对几何选择的循环偏置风险，不是发明一般detect→verify流程或凭HOI榜单准入。Reach从多视图perception、共享instance状态跨到action/role消费者。标准完成，具体差额所需深入D/E控制。

§3的每identity可保多个(box,category,source-view)，有一个候选时不再裁决；多候选按同一frozen MLLM的answer-logit normalized support选择。所有涉及它的关系用同一最终box/category；unknown保未决，与missing physical target不同。归一化answer logit不是独立校准正确概率，物理/角色支持的乘积也不是由统计独立性证明的真联合概率。保持一致的错误框仍可影响所有下游。

**关键更正。** 实际D.4明确 relation-conditioned 与 relation-agnostic 条件都“select one shared grounding per instance”。因此固定boxes/views时T4的+0.41 HICO mAP、+0.47/+0.54 VCOCO AP只支持**去掉earliest relation association提示、改用identity/category/visible extent criterion**，不单独证明shared geometry优于每role独立框（未做这种对照）。T3 first-candidate与完整模型差额0.25/0.27/0.22也不能自签显著或把全pipeline收益归几何。已通知作者/root收窄，未用错误因果进入PRE。

**实验边界/成本。** 同frozen Qwen3.5-9B、最多2local observations，prompt/policy在训练集选，HICO9658/VCOCO4946全test、IoU.5；各外部模型/role定义不统一，不采排行榜倍率。E.4 GT-assisted ranking固定boxes/labels得到上界，仅说明当前候选覆盖/排序空间，不证明一般pipeline或独立视觉真值。E.5全harness三generation seeds给SD，不等T4每组件显著性或严格因果置信区间。E.2实披露BF16/A6000、4GPU、每GPU一副本/4active images/最多32concurrent requests；约119.81/311.27 scoring requests每图，amortized GPU-worker time含input/model/collection但排加载/evaluator，**不是请求latency或SLO**。Crop、坐标关联、候选评分、cached context及全最终回归均付费，training-free不是无需训练集policy选择或通用零成本。

**具体owner。** `MULTIMODAL-REPRESENTATION` / [Ch23](../../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) 实际1260–1282局部有caption/原图分权、可render scene IR、same-model验证不独立、节点inventory/分组edge；1381段有坐标/provenance。尚无**同一persistent实例保存多源几何候选、关系盲criterion选择一份几何供所有关系读取**的接口，现有可parse图不等此candidate identity/adjudication状态。建议sceneIR/实体consumer局部最小一段，不能复制一般“合法IR非真值”；相邻Ch24采样与Ch25环境状态边界不变。只采用关系盲选择的局部对照与一致性结构，不授“消除语义循环/独立verifier/真实世界状态”。

Source/date/具体差额通过，等待限定literal PRE；**未PRE/POST**。

## R2-13 — 第二批逐字 PRE：04089 通过，另两项窄改待读回

实际逐字读 `READER2_PRE.md` 新增04089/04473/04938三段及本人注，并读回Ch81 Ask-or-Assume两段/后续workflow bypass、Ch49 tactic资产完整小节/低batch交接、Ch24连续DOIT及前后h/引导段。04089的atomic预算/测试违约/metric与非劣效边界准确，**唯一段+本人注literal PRE通过**，可按作者锚点窄写，不授尚未读到的POST。

04473主要链可支持，但实际冻结proxy是小样本评估人口，未核其训练预测器，因此要求把“代理拟合”换为“代理构造”，保存后读回再授PRE。04938原稿“有限步长的无转移近似”没有本篇已核依据，不授PRE；应改为明确head direct completion≠rollout、候选/温度/缺失P/Q/幂权与terminal argmax各自偏差，并补deterministic all-mask初态、正有限normalizer。实际为这个问题读回exact-v1 §2.1–3开头（blocks20–57），有限离散网格本身仍可满足精确Doob核，不能把其有限步数单独说成必然近似。已逐项通知作者，不回滚Source有效层。

## R2-14 — 04473 修订 PRE / 04089 实际 POST

实际读回04473修订全文和本人注，“代理构造”准确，**04473 literal PRE通过**，按原Ch49 tactic资产末单段锚点窄写。04938主要修订已正确移除无依据步长句并补clean-head/初态/normalizer；还要求首句明确“正的终态权重”（有限正normalizer本身不排除负权重），待保存后只读回受影响句，不重做Source。

随后实际读Ch81 261–282完整局部和1626行本人注：原Ask-or-Assume机制/反侧，新269行唯一澄清预算段，后续workflow speculation与timing均连贯且保留。新增与已批逐字稿一致，metric口径、期望预算非硬权限/合规、未检出非劣效及费用回退齐全，本人注有exact-v1、5分与未复现限定，未伪称日报验收。**04089实际正文+本人注POST通过，窄锁可释放**；仅行政同步真实通过层，其他改写另按影响核验。

## R2-15 — 04938 修订态 literal PRE 通过

实际读回作者READER2_PRE的完整04938段和本人注，首句已恢复“正的终态权重的条件期望h”，all-mask/正有限normalizer、冻结clean-head直接补全与rollout差别、P/Q/温度/terminal选择和不采科学应用均准确。**04938现修订态唯一段+本人注literal PRE通过**，允许Ch24原连续DOIT段后、下一引导分权段前窄写；尚未看实际正文，不授POST。

## R2-16 — 04473 实际 Books POST 通过

实际读Ch49 921–941完整局部：tactic资产三段及marker、新933行InferOpt段、后续低batch collective标题/开篇；实际读3258行本人注和邻近注。新增与已批修订稿一致，保MoE无总expert约束/FullKV反侧、held-out与真实执行分权、配置ND/局部TPOT、代理构造全费与回退。旧tactic环境/一致性论证和下节collective协议未被替换；本人注exact-v1及6分准确、不授复现/日报验收。**04473正文+本人注实际POST通过，窄锁可释放**。

## R2-17 — 04938 实际 Books POST 通过；首五项已全层落实

实际读Ch24 686–700完整局部：support与density区别、训练h/梯度分账、连续DOIT、692行新增离散分支、后续VLM-guidance与低rank目标交接；实际读3474行本人注。新增与最终PRE一致，保正权重/all-mask/正有限Z、head不等rollout及实践近似、通用机制而非科学成效与全费回退；连续/离散接口不混，原连续DOIT限制未被删改。本人注exact-v1、6分和未核实现/复现限制真实。**04938正文+本人注实际POST通过，窄锁可释放**。至此首五项04119/04808/04089/04473/04938均有实际Source/date/owner、逐字PRE、真实正文及本人注POST，不能据此预授整日DAY；新增三项仍只Source完成，literal/POST待做。

## R2-18 — 追加三项 literal：06394通过；另两窄改待读回

实际读READER2_PRE新增06394/04537/05748各完整单段与本人注；读回Ch23 sceneIR/04721两段/page交接、Ch56 Host合同首两段及后续诊断、Ch54 128–146生命周期/VMM及eDRAM交接。**06394 literal PRE通过**，允许04721两段之后/page之前唯一段：D4两边共享的关键修正明确、criterion增量/非独立MLLM/worker-seconds边界完整。未授其尚未读到的POST。

04537要求只补“按离线校准的prefill/decode caps”及“获准检索调用”，避免把LLM请求与HNSW16query call混作控制单位；余内容足够，待修订读回。05748原“保护相邻层/快照”过于省略新增正确性接口，要求明确completion前一层→dispatch frontier、snapshot暂停CPU派发并延后callbacks而GPU继续已派发工作；“均值SLO”改为inference-alone均值三倍阈值，“单run cap波动”改手设容忍带而非测得置信。支持已有Source，不另扩论文/附件；这两份尚不授PRE/POST。

## R2-19 — 04537 修订 PRE / 06394 实际 POST

实际读回04537完整修订段和本人注，已明确离线校准caps、获准检索调用与active work，**04537 literal PRE通过**，允许指定Host合同后唯一段。05748核心与SLO/cap已修正，现只要求“70BTP4未展示调优收益”明确比较对象为step-level handover（同64.5tokens/s），不泛化为相对SIRIUS也无增益（原对照为3.3倍）；本人注同步这一限定，待读回后PRE。

实际读Ch23 1270–1286完整局部：caption反侧、sceneIR两段、04721因子化两段、新06394段、page/consumer-router交接，以及2947行本人注。新增现行行号1281（并发移动不影响唯一身份），与已批PRE一致，原图/坐标权限、两边shared/D4criterion差别、同MLLM非独立、组件统计及worker-seconds限制保留，邻接未越权改写既有分组/页面机制。本人注exact-v1和6分准确、不授复现或整日验收。**06394正文+本人注实际POST通过，窄锁可释放**。

## R2-20 — 04537 实际 POST / 05748 最终 PRE

实际读Ch56 823–851完整Host合同含代码/增核837行/后续request lifecycle诊断、2107行本人注。新增与通过修订态一致，CPU launch starvation与UMA contention没有合成同因，离线校准admission与active/drain区分清晰，非E2E/检索尾未验及全费回退保留，原容量合同与后续OS证据链未被替换。本人注exact-v1、6分准确，无复现或日报验收外推。**04537正文+本人注实际POST通过，窄锁可释放**。

同时实际读回READER2_PRE的05748完整最终段和本人注，comparison现明确70BTP4对step-level handover没有tuning吞吐增益，不再误伤相对SIRIUS对照；completion→dispatch/快照/TPunion/reback、SLO与单run限制完整。**05748最终literal PRE通过**，允许原Ch54生命周期/VMM后唯一段；实际Books尚未读，不授POST。

## R2-21 — 05748 实际 Books POST；原分配八项全层完成

实际读Ch54 133–148完整VMM/alias/新139行MOLT/eDRAM交接及1014行本人注。新段与最终PRE一致，保护窗/CPU暂停而GPU续跑/TPunion/reback边界、inference-alone均值阈值与正确step-level比较对象均实际落实；原workspace与片上保护成本论证未被改写，断言未扩大为普遍checkpoint正确性、训练质量或SLO保证。本人注exact-v1、6分和未复现限定有效。**05748正文+本人注实际POST通过，窄锁可释放**。至此本reader原五+追加三共八项均实际Source/date/具体owner、逐字PRE与正文/本人注POST通过，局部层完成不授整日DAY。

root随后具名追加仅05977/06801/04277/05683四份最小稿的owner/PRE/POST；已实际读 `ROOT_REVIEW.md` R10，复用root非作者实际Source/date/6分结论，不第三次重查abs/全篇。作者仍为唯一Books writer；四项逐字稿/写后尚待实际读取，不预签。

## R2-22 — root R10 四项实际 owner/literal PRE 通过

实际完整读作者 `R10_LAST_PRE.md` 中05977/06801/04277/05683四份正文及本人注；不读写其中06069，也不替root重审其余稿。Source/date/各6分及反侧复用root R10已完成的独立原证，不声称本人第三遍重读论文。

- **05977 StagQ / `INFER-TENSORRT-LLM` Ch49**：实际读量化粒度b+m/g段、前一affine-grid说明与后续MX-axis段。已有metadata成本和group轴，但不含多精度共用base+dyadic bitplane前缀/共享metadata、全精度必读pre-grid原值及post-grid残差side records、加载repack与运行精度分离。最小稿限定padding/guard/3bit退步及synthetic-weight microkernel，足够区别现有generic低比特不是加速。**正文+本人注literal PRE通过**，精确只在粒度首段b+m/g后、MX段前唯一段；“逐层bitplanes”按精度细化层而非网络层理解，不能新增按网络层动态切换主张。
- **06801 MC-Sparse / `MULTIMODAL-GENERATIVE-PARADIGMS` Ch24**：实际读72–83局部：尺度历史、自回归SparVAR的query/KV坐标迁移与残差、下一个head–source-scale驻留段及稀疏执行交接。已有pattern/残差复用一般边界；新增明确**去噪anchor真实dense概率→tile均衡query grouping/individualKV→同时缓存group/index/residual，当前QKV仍重算**，不是再写通用cache≠exact。最小稿保anchor/QK/warmup/padding/prefetch/质量退步与3D估算上界限制。**正文+本人注literal PRE通过**；精确锚为SparVAR唯一段及`2602-04361` marker后、下一“跨尺度还要把…”前，不误把后者另篇驻留机制合并算作SparVAR两段。
- **04277 SyclKittens / Ch49**：实际读317–332 Device-initiated三段/marker及PhysicalCore开篇；原文拥有候选directive与runner分权，尚不含tile/subgroup/matrix-engine布局和同context peer release/acquire的具体范围合同。最小稿不借可移植语法授同步或数值真值，vendor GQA fallback/大消息oneCCL/进程卡数混杂均保留。**正文+本人注literal PRE通过**，2603-02376 marker后/PhysicalCore标题前唯一段。相邻Ch48 exact speculation与Ch50 engine状态交接实际读，不迁其owner。
- **05683 RESOLVE / Ch49**：实际读197–225完整persistent开篇、graph/replay/dynamic分支、typed milestones/mid-state oracle、marker及后续persistent executor。旧段已有有限oracle非全证明；新增**冲突trace选扰动位而非HB证据→有限CTA/scope determinism→有限input GPU/顺序提取桥→real代数规格证明的各层权限**，不让弱测试/实数证明补签并发浮点全输入。稿保100/14/11选择范围、mutant漏检、全部费用与Unknown，**正文+本人注literal PRE通过**；2609-12379 marker后、以“Persistent executor在进程启动时…”起首段前唯一段（仍在既有标题内），不另加heading/章末机制。

以上四项允许作者作为唯一writer按精确位置窄写，无需root额外lease；**实际正文/本人注尚未读，不授POST或整日DAY**。

## R2-23 — root R10 四项实际 Books POST 通过

收到作者保存消息后，实际分别读完整新增、两侧局部和本人注，未以其自读替代独立核验：

- **05977**：Ch49现1076行，实际读1067–1083的PoT/粒度b+m/g、新StagQ段及后续MX/scale段，并读3274行本人注。与PRE逐字一致；base/bitplanes共享metadata/side record全精度必读、load repack非在线切换及padding/microkernel范围完整，未替换旧axis与校准论证。**实际POST通过**。
- **06801**：Ch24现78行，实际读72–84的尺度历史/连续残差、SparVAR、新MC-Sparse段及下一个head–scale驻留/ToProVAR交接，并读3478行本人注。精确插在SparVAR marker后，不覆盖另篇；当前QKV重算、anchor额外费用、旧残差非exact及质量/估算上界限制齐全，正文与PRE一致。**实际POST通过**。
- **04277**：Ch49现329行，实际读315–338的既有host/P2P交接、Device-initiated三段/marker、新SyclKittens段及PhysicalCore开篇，并读3276行本人注。布局/参与范围/同context release-acquire不自动跨进程，原candidate/runner权限与下一虚拟执行资源机制保留，反侧与全费吻合。**实际POST通过**。
- **05683**：Ch49现221行，实际读211–232的graph元数据寿命/动态分支/typed milestone、新RESOLVE、persistent executor及后续event依赖，并读3278行本人注。与PRE一致，有限扰动/桥接/实数规格层级没有互相补签，14/11选择人口与mutant漏检、Unknown/全部费用保留，原executor控制权未改。**实际POST通过**。

四本人注均有exact-v1、6分、root R10必要Source/date和未核实现/复现限定，未伪称日报验收。**四窄锁可释放**。本reader当前授权12项：前8项本人实际Source/date/owner、PRE/POST；后4项Source/date复用root非作者R10，本人实际owner/PRE/POST，均已完成对应局部层。未改Books/日报/索引，不授整日DAY；最终六部分与保存态由root验收。

## R2-24 — Oct07 tail 固定六项：刷新合同与实际日期独核

root再分配仅04510/04540/04585/04607/04659/04767的必要Source/owner/PRE/POST。实际重读AGENTS、当前Research/Report合同、Prompt、ROADMAP、来源说明及每日14行，并读本日TAIL_CALIBRATION；原12项不重做，不扩发现/应用附件。作者仍唯一Books writer，本reader仅改本文件。

2026-10-20T07:00:08–10Z实际GET六当前官方abs、完整题摘及history，无具名撤回/纠错标记。唯一v1 UTC依次：04510=`Oct3 13:18:15`，04540=`Oct3 14:15:06`，04585=`Oct3 15:18:32`，04607=`Oct3 15:49:04`，04659=`Oct3 17:15:26`，04767=`Oct3 21:07:46`。04607另有Oct9 02:34:53Z v2，明确本日只审v1、不用现行v2摘要支撑首版细节。实际读作者保存六精确DOI DataCite原件，皆`arxiv.content`/`findable`，registered Oct6 UTC依次04:35:35、04:36:19、04:37:25、04:37:55、04:39:12、04:41:52。复用本日已核历史公告/发号规则，最早公告Oct6 08:00BJT，最晚分别12:35:35/12:36:19/12:37:25/12:37:55/12:39:12/12:41:52BJT，整个区间在Oct6自然日。不是称提交或登记为实际公告时刻，不追假想全球首公开。最初一次本地解析因bs4缺失在发请求前失败，随后实际用stdlib取得上述结果，不计失败为外部缺口。

## R2-25 — 04510 ManifoldCache：仅一般理论 Source/Ch24 差额通过，强摘要须收窄

实际读[exact-v1](https://arxiv.org/html/2610.04510v1) `core-04510v1.raw.html` 完整题摘、§3/A1–A6中一般方法、假设、MMSE与Jacobian证明和直接限制（本地blocks17–54、251–318）。只扫§4的硬件/参数口径，不采用其8项科学应用质量、不展开应用附录。当前abs摘要的“普遍sharp safe boundary”式表述比exact-v1正文更强；采用正文及证明，不从当前页面反推首日逐字内容。

一般机制不依赖某个科学任务，因此贡献准入可保留，**2+2+2=6**：已有缓存只看变化量/proxy→VP条件模型中把frozen terminal estimator误差、mode selection与层feature drift三个对象分开、给可计算但有条件的界→不能由同一schedule/depth给全部block签安全复用。跨score/估值/网络block，长期边界可复用。理论支持与反侧足够停止，不借应用效果抬分。

**实际成立范围。** 正交分解需要C2/full-rank constraint map、正reach的管邻域；不因此证明所有噪声state都在该管域。Theorem1其实是等权双Gaussian mixture、VP噪声、exact Tweedie条件均值、特定within-mode covariance/归一化总covariance eigenvalue≥1。MMSE≤线性MMSE本身对任意有限covariance prior成立，但半总variance简界与mode-flip显式式子有另加条件。冻结估值的MSE不是实际block cache rollout误差，nearest-mode错误不是实际constraints violation判据。flip随SNR连续变化、safe侧仍可正概率错；αbar=.5只是对所有σu∈(0,1]统一lower bound的边界，不是该处误差跳变或任意模型safe/unsafe相变。Theorem1不用g的几何，也不证明八个真实模型满足双Gaussian假设。

Theorem2对directional Jacobian upper bounds做unit-gain归一化，并**假设**深度β排序、ODE小步remainder和window temporal regularity；只有κ(normal/tangent power ratio)<κ*时，深层的**上界/认证stride**更优。实际drift严格更小还要transversality/lower-gain和gap条件，不能仅由两个上界大小推出实际排序。该κ条件不由噪声schedule推导，runtime也不测κ、不算g/投影或检查约束；Eq6按t/block索引选stride是启发式实施，不继承逐样本certificate。两定理用exact score，learned score另加误差；flow须重新定义SNR、随机sampler新噪声尚未覆盖。保留这些边界即可采用一般理论接口，不采“data-free普遍安全加速”。

**具体已有差额。** 实际读 `MULTIMODAL-GENERATIVE-PARADIGMS` / [Ch24](../../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) 1972起trajectory cache/CacheScope方向gain、prompt/timestep与低秩正交feature段；旧文已有proxy≠global Jacobian/最终误差、缓存状态与schedule绑定，但无**terminal MMSE/nearest-mode/feature-drift三种证据对象，SNR简界与κ/深度排序各自假设、认证上界不等实测drift**。建议该cache误差段内最小理论分支，保现有经验proxy/完整刷新。Ch23拥有表示，Ch25拥有环境状态，本稿不以物理/科学约束名义跨owner。Source/date/具体差额通过，允许有限literal；未PRE/POST，未核代码/复现。

## R2-26 — 04540 DreamFormer：Source/date/Ch25 具体差额通过

实际读[exact-v1](https://arxiv.org/html/2610.04540v1)完整题摘、§IV方法、§V/TablesI–IV/消融与费用、§VI配置及Conclusion限制（本地blocks32–133）。不把已有Dream Imitation/STORM单token本身称新发明；新可保留的是**全分辨率多视角经扩容量categorical state压成一个time-position，连同维度/目标稳定性、growing imagination context与部署real-context分账**的实际取舍，**2+2+2=6**。Reach跨观察编码、可预测state、policy imagination/部署接口；支持局部设计而非Transformer WM普遍优越。

两个train-from-scratch ResNet18+spatial softmax分别读200×200/84×84视角，融合成64×32 categorical posterior（flatten2048/64active，**不是词表单一整数token**），再和action过MLP占一个Transformer位置。相比32×32，entropy regularizer、KL前250K cosine ramp和trajectory-consistent pixel shift共同稳定；改变latent capacity也改变objective，消融不能归因纯“多一倍容量”。WM不预测task reward，冻结后actor-critic在H32 imagination中按既有expert-latent alignment reward训练，full expert plan recognizer只训练可见，部署用current state/goal proposer，不能泄漏未来示教。训练KV随context+imagined history增长，部署不在线想象、只保存最近真实C16 context；单position不等状态无损或无限memory。

CALVIN1000五任务链/三seed；无视觉预训练但language encoder已预训。LUMOS由外部published report、仅D→D有值2.34 vs2.52（SD.05/.11），差异同时含recurrence→Transformer/resolution/state维度等，不单独归tokenizer。ABCD→D与HULC3.11 vs3.06在SD内；ABC→D1.30 vs.67不能当真实语义grounding证明。TableIII组件同5/2 shift下reference2.44、shallow2.32、32×32+原objective2.02、imagination内改BC1.70；不同于最终10/4 shift2.52，不拼接归因。外部预训methods训练in-domain仅1%与本稿full play也不等预算，不用榜单抬贡献。

TableIV只在**假定width/depth匹配**时数query-key interactions和cached token，不实测wallclock；H²全history vs固定C的H线性有取舍，不说长H任意都更便宜。原型WM60M/4×QuadroRTX6000、B16/seq64；actor47M/B512/H32/C16/单GPU每seed，precision/总训练时间/服务concurrency与SLO未披露。56-step open-loop用GT actions的定性例子不是policy闭环准确性，gripper blur从posterior已有、small object末端漂移，真实机器人未测。编码、latent训练/重建、全部imagination与critic/actor更新/部署均费，不由不下采样推保留全部空间细节。

实际读 `MULTIMODAL-WORLD-MODELS` / [Ch25](../../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) 300起latent/control sufficient与457–479 imagined rollout/chunk/real-refresh；已有latent便宜≠足够、缩horizon/时间单位，但尚无**one time-position≠单symbol/无损，多视角latent维度与稳定目标成套、growing训练history vs部署window，以及query-key代理非wallclock**的具体成本链。建议imagined rollout局部一段，不复制Ch23一般codec或Ch24生成概率。Source/date/具体差额通过；允许有限literal，未PRE/POST。

## R2-27 — 04585 TI-JEPA/Velocity Blind Spot：Source/date/Ch25 差额通过

实际读[exact-v1](https://arxiv.org/html/2610.04585v1)题摘、§4–9方法/全部主要反侧、AppendixA所需命题/假设及C配置/D4不同seed比较范围（blocks19–79、106–129）。**2+2+2=6**：不是单帧看不到速度的常识，而是把该不可辨识性放到single-frame预测target/goal cost，并用named finite-difference motion target与不同memory读口分开测试，修正“next embedding已是动力state”的具体接口判断。无负面结果排除或夸大架构优越性，支持+关键反侧已够停止。

理论仅在instantaneous renderer `o=g(q)`（无motion blur/velocity overlay）与单帧确定E下成立；若velocity不是q的a.s.函数，则z不能可辨识它，conditional independence不排除数据集q-v相关可作统计预测。输入history/recurrent belief可携带速度，不在单帧encoder命题排除范围；**predictor有三帧历史不使其single-frame target本身成为速度码**，也不证明该history predictor不能分开未来路径。memoryless相同q/相反v两branch输出相同是构造保证，不能拿k1对有三帧前端的TI作为等观察预算SOTA证据。

TI同一pose encoder逐帧读k3，连续pose差经bias-free MLP成motion code；相同重复帧给零motion是构造保证，不证明真实物理速度正确（pose encoder不可辨或采样太稀仍失败）。predictor只消费current(q,v,a)，联合预测pose/motion，SIGReg只约束pose、motion另soft variance floor；把motion并入同一isotropy目标会collapse。部署虽无额外predictor history，形成motion仍须短窗encoder/差分，不写零历史或免费。RateIdent分episode探针、same-q/opposite-v zeroaction kill与stop-at-goal cost；前者原frame split出现邻帧泄漏已修。官方checkpoint速度linear probe null也不能升级为全部nonlinear/所有任务不可用。

主正planning限三个受控synthetic environments，k1对照显著p值是配对任务/seed统计，不是大量独立training seeds。k3与GRU aggregator保持更强反侧：InertiaBall/Pendulum recurrent可胜TI；CartPole只某些指标较好，官方ViT Pendulum rolloutMSE .576劣k3 .391。D4第二seed只重训recurrent、TI固定，不认证TI更seed-robust。真实dm_control Reacher照片仍是模拟renderer、非真实机器人；motion对true velocity probe chance、sign accuracy .525、branch-separation2.166超过GT不是更准确，rolloutMSE .230仍劣k3 .041；PushT planning为null。故不能照录38倍branch separation为38倍物理准确性。

成本配置：smallCNN latent8 vsTI4+4、B256/8ksteps；official-scale fromscratchViT-Tiny/14+6层AdaLN约16.5M/224²、5ksteps，GPU只披露单46GB预算而型号/precision及总费ND。Reacher600episodes/40200decimatedframes；训练、window编码、joint预测、探针/kill/CEM真实反馈费用另计，不授服务或物理安全。必要骨干/优化变更在官方scale曾collapse，不能以理论推出任意recipe稳定。

实际读Ch25 `MULTIMODAL-WORLD-MODELS` 346–386 next-embedding表示合同、LeWAM信息mask、停止梯度/Crafter、冻结latent时间监督，以及300开篇。旧文已有latent相似≠state完整/缺运动的经验失败，但缺**rendering/target可辨识性→predictor history与被读出的target权限不同→命名pose/finite-difference motion目标/各自regularization→same-configuration反事实与probe/规划不同资格**。建议next-embedding合同限制后最小段，保recurrent belief/多帧替代，不另占Ch23/26。Source/date/具体差额通过；未PRE/POST，未复现。

## R2-28 — 04607 ForeAct3D exact-v1：Source/date/Ch26 差额通过

实际读[exact-v1](https://arxiv.org/html/2610.04607v1)题摘、§3–5/Table1–5、A3配置/A7限制以及直接相关geometry有效性说明；本日版本只v1，现行abs/v2无权填首版结论。**2+2+2=6**：单纯feature辅助预测没说明未来对应哪段拟执行动作→policy产生action chunk条件化future几何queries，并以current/future静态/刚体/kinematic软损失回写共享action表示→训练目标与部署控制的具体接口，不把一般加geometry loss或榜单当新贡献。

六queries对depth/seg/pose×current/future，只有future读policy-generated action chunk；agent/wrist两视角depth/seg，pose仅wrist，action horizon endpoint预测而非中间帧轨迹。3class seg仅background/robot/object，**不预测instance ID/跨时correspondence**。closure用GT标定把预测agent-view depth反投影，GT masks/instance IDs选同pixel、两端有效点；≥32pts实例做Kabsch residual，gripper近物体时降权.1，wrist pose另对FK+handeye监督，不由预测pose自行认证geometry。samepixel+同instance不等material-point tracking，大运动/遮挡/可形变/关节物/动背景失效；它是soft training regularizer，不是hard physics或真实碰撞/contact closure。

训练后future branch不用于选/refine动作，故不授runtime safety checker/在线world planner；预测提供sharedrepresentation监督。future输入由当前policy产生但label来自示教episode，原文未建立所有反事实拟议动作的结果对应或统一闭环因果，不能外推counterfactual validity。去action消融固定queries/closure/训练协议支持局部conditioning作用，但累计组件顺序不是完整factorial/所有收益唯一原因。LIBERO98.3 vsbase96.6、CALVIN3.73 vs2.94等为论文受限协议，geometry外部对手horizon8/5/3不等；pred-mask仍GTinstanceIDs，CALVIN recall92.8→65.9揭示mask错误，LIBERO用predmask更低error可因丢难pixel，不能称更真。实机3任务50示教/每配置15trials，总3/45→17/45小人口、累计加模块，不授安全/泛化或seed显著性。

16×A10040GB/B128/30ksteps/5kwarmup，closure2k ramp.1。precision/backbone精确asset/部署latency与control deadline必要段未披露，不以“without robot pretraining”称无预训练。dense labels、depth/seg/instance标注、FK标定、queries/decoders与全部训练回归均费，部署删除预测分支不等训练零成本。

具体owner：实际读 `MULTIMODAL-EMBODIED-VLA` / [Ch26](../../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) 394–414 action-facing gradient authority、GuidedVLA头分工/posebottleneck、426–430未来监督；Ch25开篇区分transition/planning及Ch27数据交接。已有geometry mediator与训练未来目标，但缺**同policy chunk只接future query、current/future GT校准下soft closure与runtime未来预测可删的分权**。建议action-facing representation局部最小一段，soft约束/GTinstance/短时对应与不在线决策紧邻，不再改Ch25一般action-conditioned世界模型。Source/date/具体差额通过；未PRE/POST，未核实现/复现。

## R2-29 — 04510 实际修订 literal PRE 通过

实际读 `TAIL_READER2_PRE.md` 04510完整正文/本人注，并读回Ch24 CacheScope段及前后cross-request/prompt-aware边界。原稿成本句容易混成paper运行时必须算geometry，要求收窄后已实际读回为核验假设的geometry/score诊断、stride选参/cache/刷新/回归另计，未谎称原runtime测g或κ。三证据对象、twoGaussian/exactTweedie、κ-depth与实际drift不同资格、无科学效果均保留，插在CacheScope后/promptaware前自然。**修订态唯一段+本人注literal PRE通过**，允许作者窄写，不预签实际POST。

## R2-30 — 04659 PermVLA：Source/date/Ch26 差额通过

实际读[exact-v1](https://arxiv.org/html/2610.04659v1)题摘、§3–5方法/主控制/诊断与限制、A9两stream具体mask/A10配置（blocks24–97、144–159）。**2+2+2=6**：不把XLNet/orderless chainrule新应用本身计贡献；新增是**同actionchunk的subset-conditional训练辅助与固定LTR部署分开、同数据/decoder-compute对照及lowNLL/跨order一致性不等闭环质量**的实际设计边界，因Ch26缺该目标/执行分权深入必要mask/反侧。

K固定前K个physical slots按chronological reveal，其余采permutation；K0全随机也只训练，physical-time embedding不变。content读reveal≤自身，query只strict prefix，Gaussian head读query，避免self/target泄漏；共用encodercontext/decoder参数。L=.75LTR+.25CAP，reference M1/K1/H16/execute8；不是把动作实际倒序执行，也不是所有order对应同一个learned density已获链式恒等保证。有限模型可在各order拟合不同joint，理论identity与经验sharedparameter regularization分开；不授新的物理causality。

LIBERO每suite30k seed0/500matched episodes，Qwen3VL4B-LoRA+67M8层Gaussiandecoder，同init/data/schedule/deployment；LTR2pass匹配decoder工作/dropout而不等总墙钟已被独立测量。reference71.7 vs62.6/62.2只此配置；H8均值77.5不是只改CAP的等值对比。M4/K0/K8/λ.5各suite有取舍，不能称prefix越长越好或CAP最佳固定参数。LIBEROPlus10030instances每项一次，20/28或25/28suite×扰动组合胜而非全部；CALVIN100k同seed0，1.364 vs1.090/.694，externalOpenVLA3.27协议不同不拿作输赢。多数主控制单trainingseed，nestedSuccess@k不算独立五次实验或新置信。

诊断是同chunk两sampled revealorder joint logdensity差平方/H²，下降多数量级不证明世界/动作正确：各slot完全独立可平凡agreement，M4更好Long未再降sensor，K8在Π1评更高sensor仍改善Long。Continuation/recovery归因需额外perturb-and-recover，尚未做；diffusion扩展只有可行例，缺matchedcontrols，不把Gaussian结论迁给全部flow/diffusion。

oneA80080GB每suite进程，BF16/SDPA，LoRA32，B16/30k，CALVINLoRA64/B64/100k；所有M训练decoder passes、context/监督和控制费用计入，部署parameter与LTR结构不变不是免费训练或实测实时SLO。仿真/无实机，robot pretraining互动未验。实际读Ch26 `MULTIMODAL-EMBODIED-VLA` 666–704动作表示/chunk、Chronos物理time、GoalVLA监督stage与target-padding。已有chunk staleness/时钟/监督身份，缺**revealorder只改变训练条件集合、mask泄漏资格/physicalindex保持/LTR执行与compute-match反侧**。建议actionchunk局部最小段，不改Ch24一般生成factorization。Source/date/具体差额通过；未PRE/POST。

## R2-31 — 04767 Flow skill-level WM：Source/date/Ch25 差额通过

实际读[exact-v1](https://arxiv.org/html/2610.04767v1)完整题摘、§III–V方法/主对照/全部关键诊断及Conclusion（blocks20–96；无须追扩展附件）。**2+2+2=6**：不是泛options/latent action新名称；新增可留的是**冻结flow policy的输入作为可执行WM action、完整skill endpoint作为transition，并把抽象表征、proposal可执行性、效果ranking与search horizon分别干预**的具体条件，避免仅以label/预测误差解释规划。跨控制chunk、抽象state与搜索，支持必要反侧后停止。

每skill完整256×10setpoints在settled scenes间开环执行，再真观察/replan；全部方法都需预分段skill、quasi-static端点。四policy分别训练但共架构/120k脚本示教（7500start×16valid branches）；动作是pure seed压缩(VQ256+4d)、learnedFSQ625code+effectdecoder、objectcentric1512code或handlabel+2dresidual。code两支execution重新抽seed，因此世界模型吸收executionnoise，不是code就精确决定结果。objectcentric另需stable object IDs、one-moved-object/fixedgrid；手写label另有完整preconditions/effects。无symbolic label不等无动作示教/无分段/无物体特权。

世界模型分别从各policy rollout训练51k(label)/64k(seed)/128k(eachcode) transitions，**同recipe不等同数据量**。主结果用GT poses，感知通路三固定相机确保无全遮挡、预训pose regressor冻结；不能声称原始视觉端到端条件对等。beam32与CEM(label64×5/seed128×10)不等总搜索预算，budget物理时间配平的control-rate baseline也不等wallclock。每k1–14有100pairedtask，k+5执行turns/horizon≤15；Wilson/McNemar在task人口上，不授多trainingseed鲁棒性。

proposal side移除label preconditions**连带effects传播**，其他action/model/search保留；label优势大幅缩小，支持候选知识bundle的作用，不是只precondition一项纯因果。学得filter/codeprior仍有误差，AUC.73/.78不是硬执行许可。valid random labels不用WM全失败说明validity≠有用计划；executed-effect ranking label98 vscode约60不等未来物理精确。pureseed fresh57%valid→compressed30%、decodability33 vsobsalone8%、rare skill掉，说明压缩损执行支持，不能“所有seed等价/无损”。>6skill普遍下降，optimal plan低预测cost只是模型能够在oracle proposal上分辨，不证明全部model正确；beam32→256没改善指向distance-to-goal剪掉必要stagingmoves，特定k14tower swap仍87%不能推广所有长链。

只MuJoCo桌面/六blocks/四skill类型，truepose与perceivedpose差额分账；硬件/precision/完整训练总费与planning墙钟deadline均ND，不报实际在线效率/安全。脚本示教、flow/seedVAE/code/filter/WM/感知、每candidate rollout/beam/CEM和开环执行/重观察全费。缩抽象步数不认证每步error或所有contact控制简化。

实际读Ch25 `MULTIMODAL-WORLD-MODELS` 195–210 abstraction×timescale、300latent、457–479 imagination/chunk闭环；已有多时间尺度、chunk末状态及短rollout，但缺**WM action精确绑定flow生成器seed/code/label、executability/decodability分别检验、同planner下proposal知识/效果评分/距离剪枝瓶颈分责**。建议imaginedrollout/chunk局部有限一段，不重复Ch26通用skill/control方法，也不授symbolic state真值或标签决定优越。Source/date/具体差额通过；未PRE/POST。

## R2-32 — 04510 实际 POST / 04540 PRE / 两份窄修

实际读Ch24 1980–1991 CacheScope/新1984行04510/promptaware完整相邻，以及3481行本人注。最终PRE一致、受限通用理论、runtime未测geometry/κ和cost验证责任准确，不挪用科学结果，原经验sensor与条件分支未改。**04510正文+本人注实际POST通过，窄锁可释放**。

实际读TAIL_READER2_PRE新增04540/04585/04607三完整段与本人注，相关owner局部R2-26/27/28已实际读，未改论证可复用。**04540唯一段+本人注literal PRE通过**，imaginedrollout开篇反馈段后/“有限离线数据下”前窄写；position≠单symbol/无损、training growingKV vsruntime C16、proxy非wallclock及latent/目标联合消融均清楚，未POST。

04585要求去掉未核实“较快inference”信号，保branch-separation/seed反侧，q精确称configuration；修后待读回，不预签。04607原稿把预测类别错成static/rigid/articulated，**不授PRE**：须改background/robot/object，并与staticity/rigidity/end-effector-kinematics三softclosure分清。closure本体是GT相机标定/语义instance监督下的两端**预测depth**，不是直接拿current/future GT几何闭合；92.8→65.9须绑定pred-mask Recall@2cm指标。已通知作者定点修正，Source与准入仍有效，不重读全部论文。

## R2-33 — 04585/04607 修订 literal PRE 通过

实际读回TAIL_READER2_PRE两项完整修订正文与本人注。04585已用configuration q、删除未核快inference，仅有限branch/seed反侧，保TI前端三帧与RSSM/多帧替代；**04585 literal PRE通过**，指定Ch25 next-step/same-step段及2603-02765 marker后、waypoint时间监督前唯一段。04607三seg类别已更正background/robot/object，另列staticity/rigidity/末端kinematics，GT标定/语义instance监督下比较predicteddepth、Recall@2cm及不online选动作限定准确；**04607 literal PRE通过**，指定Ch26 GuidedVLA完整段后/接触信号分支前唯一段。本人注均exact-v1/6分，04607不借v2，未复现表述真实；均尚未实际POST。

## R2-34 — 04540 实际 Books POST 通过

实际读Ch25 457–476 imaginedrollout原开篇/误差代码/feedback段、新467行DreamFormer、后续有限离线规划与SoftMPCritic等直接交接，并实际读2107行本人注。与PRE一致，position/state维度、训练history/部署context分开，query-key proxy非真实总费、latent目标联合消融与blur反侧紧邻，原latent/真实反馈路径未覆盖；本人注exact-v1/6分/未核代码复现准确。**04540正文+本人注实际POST通过，窄锁可释放**。余四item仍须各自写后，不预授DAY。

## R2-35 — 04585/04607 实际 Books POST 通过

实际读Ch25 372–389的LeWAM/梯度目标、next-vs-same-step/marker、新04585段（现383行）、waypoint时间目标与后续VideoWorld交接，并读2110行本人注。新增和最终PRE一致，单帧target/历史predictor分权、TI三帧真实费用/GRU反侧、simulated Reacher与seed限定保留，原“未来预测可能促进history”条件命题未被静默否定；本人注exact-v1/6分准确。**04585正文+本人注POST通过**。

实际读Ch26 398–414 action-facing mediator/GuidedVLA、新04607段（406行）、接触CRAFT与posebottleneck交接，并读2857行本人注。最终修订态三seg类别、3softclosure、GT标定/instance下预测depth、pred-mask Recall下降与部署不选/refine动作均实际落实；原旁路/接触/pose机制没有替换，本人注仍仅v1而非Oct9v2且未复现。**04607正文+本人注POST通过**。两窄锁可释放，不预授整日DAY；tail最后04659/04767仍等literal/写后。

## R2-36 — tail 最后两项 literal 实读，必要窄修

实际读TAIL_READER2_PRE的04659/04767完整正文和本人注，读回Ch26 682–696 actionchunk开篇/FFDC/Chronos与Ch25 477–491 VLA-MBPO两段/RaWMPC/失败人口交接。原Source与owner有效层不重做；两位置可承载最小差额，但原稿各有须修事实，**尚不授PRE**。

04659将content/query ≤/<写为“按physical index”有误：CAP依据sampled reveal rank建mask，physical-time embedding只保留动作身份；若按原physicalindex定mask会错成LTR。要求精准改为physicalidentity/timeembedding与revealrank权限分开。04767消融从proposal移除的是preconditions/effects bundle而**action label保持**，不能写成整个label都删除；oracle最优计划低预测cost与实际beam剪必要stagingmove是两份证据，不混为一个“oracle-beam”对照，validity57→30须标百分率。已通知作者保存修订后定点读回，不复读全篇或扩发现。

## R2-37 — tail 最后两项修订 literal PRE 通过

实际读回TAIL_READER2_PRE中04659/04767两完整修订段及本人注。CAP明确physicaltimeembedding保存身份、sampled revealrank决定content≤/query<，scope不扩大到实际倒序控制；FlowSkill明确actionlabel保持而proposal规则bundle移除，oracleplan与beam剪staging分述，validity57%→30%单位正确。两段其余位置/机制/对照/费用/回退及exact-v1来源未变，已有owner上下文复用。**04659/04767修订态各唯一段+本人注literal PRE通过**，允许作者按原Ch26 actionchunk开篇后、Ch25 VLA-MBPO两段后/RaWMPC前窄写；尚未读真实写后，不授POST。

## R2-38 — tail 最后两项实际 POST；本reader本日授权层全部收齐

实际读Ch26 684–704 actionchunk开篇/代码/open-loop段、新694行CAP、FFDC/Chronos与阶段target-padding交接，并读2866行本人注。新段与修订PRE一致，physicaltime/revealrank正确分开，mask≤/<没有写回LTR；部署不重排、orderagreement非控制真值、单seed与全费fallback保留。原runtime stale suffix/时钟机制未改变。**04659正文+本人注实际POST通过**。

实际读Ch25 479–492原时变dynamics交接、VLA-MBPO两段、新485行FlowSkill、RaWMPC风险覆盖与失败人口段，并读2113行本人注。与最终PRE一致，label保持/proposal规则bundle变化明确，oracle低cost与beam中间移位分开，GTpose/settled端点/物理时间与wallclock不同、预算不配平及57%→30%反侧落实；原chunk训练与风险population机制没有替换。**04767正文+本人注实际POST通过**。两注exact-v1/6分/未核实现复现如实，**两窄锁可释放**。

本次tail六项最终真实POST归并：04510 R2-32；04540 R2-34；04585/04607 R2-35；04659/04767 R2-38。六项均必要Source/date/具体owner、逐字PRE及实际正文/本人注POST完成（仅04510一般理论、不采科学应用；04607仅v1）。合此前12项，本reader本日18个授权item局部层已齐，不授整日DAY/FINAL；作者合并六部分、root非作者验收。本reader只改本文件，不改Books/日报/索引、不做Git写；当前停止本日，不接新日期、不额外Source复读。

## R2-12 — 05748 MOLT：必要 Source/date/Ch54 差额通过

实际读[exact-v1 HTML](https://arxiv.org/html/2610.05748v1)本地 `core-05748v1.raw.html` 完整题摘及§2–5全必要机制、Tables1–2/Figures5–14文字与§6–7边界；短文已经足够支持与关键反证，不追实现附件、不声称artifact复现。日期联合独核见R2-9。

**准入/评分2+2+2=6。** 不是一般checkpointing/共置节省内存，而是autoscale副本内部秒级KV增长时，把训练step内的saved activation变成可撤回物理backing单元，同时约束CPU/GPU异步与TP一致性，使撤回不必丢弃整个正在运行的step。固定预算重算和request边界租借不能直接解决这个边界；Reach跨inference KV allocator、tuning重算与TP执行。标准完成，因Ch54具体差额深入§4.3–4.4及§5反侧。

**机制。** 预profile activation大小，保留固定VA slot；shared physical pool供KV与backed slots，SST保存backing、重算成本、enqueued状态。forward/backward派发前读真实backing，unbacked的activation改走pinned临时路径，前向末次消费后释放，反向重新计算。已经产生但被撤回的activation也按当前状态重算；页只在step边界re-back，不能把两个方向说成任意时刻对称变化。Frozen weights、LoRA参数/梯度/optimizer、intermediate和不可重算layer input不受该撤回协议支配，不能称全部训练内存随时释放。

CPU dispatch并不证明GPU完成。保护窗从completion frontier前一layer到dispatch frontier，保留跨layer消费；首次dispatch时标记，下一layer完成callback才清旧标记。handover snapshot暂停CPU派发并延迟callbacks，GPU继续消费已派发工作；只能撤回窗外slot，之后恢复callbacks/dispatch。TP取rank-local窗的并集并在每rank选相同slots，否则不同重算路径会破坏collective顺序。小dispatch cap增可撤回集合却会饿GPU，须离线profile，不授任意异步kernel或rank故障正确性。

**可比性与费用。** 原型vLLM0.11/PyTorch2.8，Mistral24B的H100 TP1/2、Llama70B的H100 TP4/B200 TP1，rank8 LoRA；ShareGPT serving/Alpaca tuning，sequence分别768/2048/1024/512。precision、完整serving I/O长度分布和concurrency未披露。SLO是同deployment inference-alone的mean TTFT/TPOT各3倍，不是通用固定毫秒customer SLO。Table2 continuous与step-level共享实现/页面池，区别为boundary移动时机，支持fine-grain受限作用；continuous99.7–100%达标、比discard-based1.9–3.3倍tuning work，但compute-only在24B两配置更快且SLO失败，不能忽略取舍。70B TP4的continuous与step-level同64.5tokens/s，只有SLO改善；对SIRIUS的TPOT p95还可能更差（136.8 vs105.1ms），不报所有指标都优。

§5.5每cap只有一run，图中±5%是手设容忍带而非CI；cap4让step慢13.1–24.6%，默认profile不是零代价。handover p99≤1.6ms及大小/TP overhead绑定受测page pool/trace，不是最坏时间保证；IPC、snapshot、VMM page map/unmap、zero-fill、callback及recompute全付费。未展示最终adapter质量/数值等价独立实验，不由“保留step”签发训练语义普遍等价。没有在线压力/失效恢复或实生产trace结果；支持机制接口而不授生产透明共置。

**具体owner差额。** 实际读 `INFER-GPU-MEMORY` / [Ch54](../../../../../books/part-05-inference-system/54-gpu-memory.md) 固定/动态/瞬时生命周期及VMM/alias段、PeerGPU/EMA约321–333行的可撤销借用与安全request边界，以及439行起multi-cache committed map。现有已有VA≠physical、tensor lifetime、共享页与撤回权，但**尚无训练step内activation backing动态撤回→当前backing驱动save/recompute→异步completion前一layer保护/快照→TP窗并集一致撤回**。可在既有生命周期/VMM局部最小一段建立这一分支，不重复peer容量层或写成任意多租户allocator。Ch53开篇拥有replica/serving拓扑，Ch55开篇拥有跨池PD；两者不接管activation lease。Source/date/具体差额通过；等逐字PRE和实际POST，不预签。

## R2-11 — 04537 PhaseGate：必要 Source/date/Ch56 差额通过

实际读[exact-v1 HTML](https://arxiv.org/html/2610.04537v1)本地 `core-04537v1.raw.html` 完整题摘、§2–5、Tables1–4及A.1–A.5的指标/校准/反侧/trace定义；B只读对应控制目标边界，不追artifact或其他附件。日期实际联合核验见R2-9。

**准入/评分2+2+2=6。** 不把prefill/ decode已有资源差异当新贡献。新增可保留的是UMA上独立CPU检索会经共享内存干扰GPU生成，且同样的高/低cap、占比/切换率在phase-blind时不能保留phase-aligned的尾延迟工作点；因此phase可以驱动CPU检索准入，但门限、active work和drain必须分开。Reach跨CPU检索、统一内存、GPU生成及执行事件。标准完成，为具体owner缺口补读必要A控制。

**机制与条件。** 原型通过MLX phase事件选择离线校准的prefill/decode cap，FAISS HNSW每call单线程16queries，cap计call、QPS计vector query。已admit的call非抢占，lower cap不撤销它；active>1的decode时长约1.06%，远大于high-admission-state的0.003%，两者不能混称。drain定义为count降至≤1并保持到decode末，七held-out trace的p95中位26.6ms、跨trace最大31.5ms；这是短HNSW chunk的观察值，不是任意后台job的界。没有增加affinity/QoS权限，也不把逻辑GB/s解释为精确memory-service归因。

**比较。** M4 Mini/16GB UMA、4-bit Qwen2.5-1.5B、2048 synthetic input IDs/128 fixed-token model evaluations、100k×384 HNSW M32/efSearch128/top10；没有自然文本sampling/feedback，prefill省vocab head。B=1.25是测试过10–45%预算中两family均有非零feasible点的最小预算，不是通用SLO。每候选3×100requests校准，按每run两p95均达标选fixed1/4→1；冻结后7 paired randomized×250requests，约0.78→1.6kQPS且两者7/7通过。TimeGate用同cap与校准所得high/low时间结构、不读runtime phase，约1.5kQPS但TPOT+60%、0/7通过；支持本工作负载phase alignment，不是任意周期策略不可能达标。4→0反而比4→1差、原因未解，不能先验假定降低cap总改善。

**反证/成本。** M4 p95 TPOT是request内p95再request间p95；M2/M2Pro是request内mean再跨request p95，不能合并成统一尾延迟证据。M2Pro缺TimeGate及pageout-free matched pairs，只支持ordering。长输出512步增益收窄；burst duty试验不是随机到达/真实agent依赖。原始retrieval独立于LLM response，没有测retrieval waiting tail/E2E RAG或长不可抢占job。transition p95增加约5.2ms、少量system pageouts仍混杂；一台每device/单小模型不授生产普适性。校准/事件hook/排队/排空成本均保留，背景负载、模型/长度或chunk尾变化须重校准，不能把mean余量当保证。

**具体owner差额。** 实际读 `INFER-SCHEDULING` / [Ch56](../../../../../books/part-05-inference-system/56-inference-scheduling.md) 823–855的Host Control Plane容量合同、诊断与device-owned控制交接，以及503–509 SoC异构dispatch/带宽/不可抢占边界。既有已覆盖CPU launch starvation、core隔离、共享DDR与dispatch，但未有**独立CPU检索按GPU phase准入、phase-blind同cap反侧，以及requested cap≠active work的drain trace双账**。可在Host容量合同下最小一段补此替代分支，避免把CPU争core与UMA争memory混为同因。Ch55开篇拥有PD跨池拆分，Ch57开篇拥有平台契约，不迁移其owner。Source/date/具体差额通过；等待逐字PRE/实际POST，不预签。
