# Oct23 同日必要 Source：系统第 2 批

作者 oct23_live_arxiv。仅 2026-10-22 BJT 窗，29302/29646/29357/29489/29873/29523/28711/29464。启动已重读 AGENTS、当前研究/Report 合同、Prompt、每日来源用法与 arxiv 主题恢复、ROADMAP、本日 State 路由；不恢复别日或扩发现。复用 [ARXIV 逐项 AB/正式分/日期有效层](./ARXIV.md) 与 [官方公告分组](./arxiv-official-listing-groups.json)。全部 exact-v1、Oct22 New/Cross 而非 replacement，不以 Submitted 冒公开；root 唯一 Books/Report/State writer。本文只 Source/actualowner/条件 PRE，未独核或未实存均不预签。

## V1 — 2610.29302 QSelect；2+1+2=5；Ch49 小 gap

原证：[exact-v1 HTML](https://arxiv.org/html/2610.29302v1)、[原件](./source-system2-2610.29302.txt)。实读 §IV A–F、V 全设置、VI A–D、VII A–D、VIII；必要标准域，不读全表/全附录，不核代码/复现。日证 cs.RO New[27]/cs.LG Cross[193]。

旧约束→增量→选择：同位宽同格式但不同量化器的模块可以组成一个静态模型；局部 MSE/表示相似并不直接优化组成模型的最终分布。作者从匹配格式的 AWQ/GPTQ/AutoRound homogeneous bank 取候选，在当前部分已选模型上逐候选完整 forward，用 BF16 reference 的全词表 forward KL 作 module-wise 一遍坐标选择，KL 模式只接受严格下降。改变离线选择目标/候选拼装接口，不是增加运行时 ensemble 或重新训练量化器。

必要数值/支持边界：组128、W3/W4 A16，embedding/head/norm 不量化；局部 AWQ input scale/inverse 必须随模块封装，跨层变换/global rotation/activationquant 不在支持域。候选来自各自整模型校准，非任意独立权重可互换；FP16 host reference-logit cache/FP32 logsoftmax 与完整词表评分均付费。一遍顺序/初始 AutoRound/候选 bank 影响结果，校准 KL 单调不是 held-out/真实行为保证。TA 模式另用已知任务训练/dev 答案 NLL 与固定 1% shortlist/阈值，可累计 KL 容忍；不能把 TA 指标宣传为 label-free fidelity。CALM-reimpl 是同 bank 的独立 CKA scaffold，不冒官方 CALM 全方法。

对照与反侧：单 A800、3B/7B/8B、3 calibration-bank seeds，generic text/QA，未测空间任务/飞行。最终 KL 相对匹配表示代理的 held-out KL 更好，但 DS W4 PPL/任务可退；fidelity 去掉标签在 Llama3.2 W3 比 TA 少 1.57 Micro pp。细粒度不恒好，多 pass 很贵且收益小；候选生成费用不在选择时间。Packed export 只有 replicate17 TA，支持可执行与小漂移，不是 optimized low-bit kernel：实时 dequant，batch1/seq2048/noKV/含加载的 CUDA peak 仅降24.2–27.9%，不可把目录缩63–70%冒服务 memory/SLO。Bank 换即整个新 artifact/完整回归，非模块名字不变即无需重验。

actualowner：顺读 Ch49 校准粒度、VLA 接口/DINO-WM planner-budget、当前输入/原始输入重构、residual/RMSNorm、ProbeQuant 全局分配等具体邻段。已有局部/后续接口条件与 artifact 验收，没有“在匹配量化器 bank 上用当前拼装模型最终分布选择静态 module family”的替代离线接口。唯一 INFER-TENSORRT-LLM；只补此选择边界，不另讲空间应用。

条件逐字 PRE：
> 同一位宽与格式下，也可先保存不同量化器产生的候选，再逐模块在当前拼装模型上比较最终 next-token 分布，而不只比较局部重构或 hidden similarity。无标签模式只接受校准 KL 下降，静态导出被选 codes、scale/zero-point 及必要输入变换；格式或跨层变换不兼容时不能任意交换。校准单调与一遍贪心不保证未见行为、全局最优或所有任务更好，加入有标签答案目标又改变了选择合同。候选制备、驻留、全词表 reference cache、多次完整 forward、packing 和独立回归都付费；目录压缩也不等实际 kernel/SLO 收益。Bank、目标或净预算失配时，保留单一成熟量化器、较粗决策与更高精度，不由更低平均 KL 批准无损或安全。

精确插点：Ch49 DINO-WM 完整段后、当前输入/原始输入重构完整段前。完整上段：

量化后的 latent dynamics 若由 planner 反复展开，precision layout 的排序还要绑定搜索预算；同一组 paired 起点与目标下，encoder/dynamics 的位宽组合应与 rollout/优化迭代数共同验收，而不能先按固定总 bit 选出一个永久最佳 layout。[DINO-WM/Wall 的 weight-only 小实验](https://arxiv.org/html/2602.11882v1)中，mixed INT4 相对 uniform 的方向在严格 planner 预算下翻转，初轮差异的区间亦包含零；这只支持模块精度与 planner 预算的条件耦合，不认证 encoder 永远应更高精度。模型权重压缩、实际 low-bit kernel 与全 planning latency 是不同证据，额外搜索、dequant 与校准仍付费；任务、预算或轨迹分布改变时重新回归，并保留 uniform、局部高精度或原浮点模型，不从一个位宽或 bootstrap 读数授全 world-model 部署保证。<!-- source-family:SF-2026-ARXIV-2602-11882 -->

完整下段：

部分上游已经量化时，当前层实际输入 `X̃` 与原高精度输入 `X` 还定义了两种不同的重构参照：只追 `XW` 可以补偿上游偏差，追 `X̃W` 则保留当前输入下原权重的响应。一条 weight-only 校准分支将目标设为 `Y*(μ)=(1−μ)XW+μX̃W`，再用 weight-drift 正则约束偏离原权重的代价，显式选择补偿与响应保持的折中；这不是把 activation 一起量化，也不证明一种目标在所有层更好。逐列近似舍入还可保留包含 greedy 路径的多个候选，各自维护 residual buffer，再按同一目标评分，不能因称为联合目标就授全局最优。[有限 W3/W4、A16 对照](https://arxiv.org/html/2602.08376v1#S3)仍有任务退步，Qwen3-8B W3平均68.08低于AWQ的68.65；候选 buffer、scoring、校准样本和超参数搜索都增加制备费用，质量改善也不是实际 serving 加速。目标身份、候选轨迹或校准人口不可靠时，保留成熟PTQ、较简单单路径和敏感层高精度回退，再独立验收完整artifact与执行预算。<!-- source-family:SF-2026-ARXIV-2602-08376 -->

## V2 — 2610.29646 Paired Instruction Dependence；3+1+2=6；具体反证深入；Ch27 小 gap

原证：[exact-v1](https://arxiv.org/html/2610.29646v1)、[原件](./source-system2-2610.29646.txt)。实读 §3.1–3.5 全方法/estimand、§4 全设置/§5.1–5.5/§6，AppA 条件 MI 推导、B endpoint/predictor/λ/uncertainty、C prospective/precision 说明、D reliability 与 nested resampling 定义/主选择 CI、E correctness-resolved 反侧及 H 完整成本。未遍历 embodied 物理附件/全表，不核实现/复现。日证 cs.AI New[51]。

旧约束→新增反证→选择：同一观察/history 只换相反 goal 的 demonstrator switch rate 可测可重复的 instruction dependence，却把“两边都正确”和“两边都错”的 switch 压成同一无符号值；在二动作时 A=a+b、p=.5+(a−b)/2，实际 halt 使前式不精确、后式仍精确。它改变是否把此 audit 直接用于 corpus acquisition 排名的判断，不是泛称代理不等真值。

严格协议：136 独立 seeded tabular demonstrator corpora，56 dev/80 prospective-heldout、两 learner seeds；24 paired audit states/48 unpaired train trajectories/48 paired ID eval states三者 disjoint。M0 与 M1 复用同48 audit responses，M0已有 correctness/goal/actionentropy，M1仅加switch；λ由M0 whole-corpus CV确定再共用，避免多一次 tuning 冒信息增量。Primary beta-binomial proper logscore 为 equal-corpus，10K whole-corpus bootstrap；test audit256 resamples积分不含dev measurement error，另 nested sensitivity refit 才补后者。Prospective内部 content-addressed commit/预存 predictions，不冒 public preregistration。

直接反侧：heldout reliability .766、switch 与 downstream correctness Spearman .356，并不授增量决策价值。M1−M0 +.059nat CI[−.027,.133]未过预设下界>0；MAE .110→.096改善但 rank .589→.490、预定 K16/80 selected correctness .838→.811，差−.0266 CI[−.0990,+.0234]，不能写已证有害/零效应。Nested refit/reselection +.0019 CI[−.0605,.0430]是另一探索 estimand；bootstrap92.3%不是posterior概率。Cross-seed target rank .567、交叉选择 .874说明endpoint有可恢复排序，不把负面全归测量噪声；更成熟48子集 ordering仍差。Correctness-resolved a/b gains较大但posthoc，halt/有限样本/regularization几何未唯一隔离，不能授信息论优势或发现因果。

Scope/费用：一 simulator/一 demonstrator family/短corpus/maturity主变化，Qwen3.5为相关家族非独立模型族。需可重放/queryable demonstrator，固定单指令日志不能补算counterfactual。Fullaudit median4.18GPUmin，已取得正确性标注paired responses时重排求A零额外query才成立；target单fit+eval mean11.46min、Qwen3.5 proxyfit13.41min，proxy排序更强并不更便宜。Setup/download/render一时费未全计。Local bothgoal分支正确不等 navigation终局成功，physical48runs protocol不足估strictsuccess；不授realrobot安全/通用数据定理。

actualowner：读 Ch27 训练分布controller、gradient-target选择、loss-history预测/失败反馈、endpoint-relativeinfluence段，另 Ch66 calibration/ranking/发布 utility 与 proxy资格具体段。现有泛化/目标与数据有用性区分充分，但缺“同对照预算下 unsigned counterfactual response结构丢方向，MAE改善仍可能不改善预定topK选择”的具体 corpus-selection 分解。唯一 TRAIN-DATA，Ch66不重复写同一机制；新增不以未显著当无价值定理。

条件逐字 PRE：
> 成对干预的可重复性，也不能直接授予语料选择价值：固定观察只交换相反目标，无符号 switch rate 会把两目标都正确与都错误的响应合并；有 halt 等第三动作时，二动作下的简化分解还会失效。应在同一查询预算和已有正确性/组成基线上，分别验概率预测、排序与预先声明的 top-K 选择，而不以相关性或较小 MAE 代替 acquisition 收益。一项受限前瞻 corpus 对照中，加入该信号的 proper-score 与选择差额区间均跨零，目标跨 seed 仍有可恢复排序；这不证明零效应，也不支持压缩后的 audit 必然充分。可重放 demonstrator、配对采集、拟合与目标训练都计费；信号、排名或净费用未通过时，保留 correctness-aware 基线、直接小规模目标训练和独立留出验收，不把“会随指令变化”当“值得购买的训练数据”。

精确插点：Ch27 loss-prioritization 完整段后/失败反馈检索完整段前。完整上段：

逐样本反馈也不必靠对每个新候选额外 forward 取得。一条受限采样分支将词频、长度、词汇多样性与稀有词比例等廉价特征，与已经训练过的 per-sample loss 配对，周期性拟合线性 predictor，再按预测 loss 调整采样概率。[受限 loss-prioritization 实验](https://arxiv.org/html/2602.17066v1)减少的是候选 scoring forward，不是特征提取、逐样本 loss、history 存储和重拟合的全部成本；改分布也不自动保持原目标的无偏性。Loader/控制面须保存 predictor、特征版本、history、拟合 cadence、实际采样概率与恢复 cursor，held-out evaluator 仍独立。作者短程130M实验的 loss 改善不是同目标质量下墙钟加速，训练 loss 比较还受到采样人口变化影响；predictor 的相关性不随训练单调改善，history 长度原方法与配置有冲突，因此不采确定通用配方。预测失准、费用抵消收益或 held-out 退步时，保留静态 mixture/均匀采样，而不是由“高 loss”直接推断有用、记忆或过拟合。<!-- source-family:SF-2026-ARXIV-2602-17066 -->

完整下段：

失败反馈还可回流为语料检索信号，而不直接重写RL reward：先从已训练policy的rollout找出与低终局正确率相关的n-grams，再精确检索其周围文本，用有限corpus继续预训练后重跑同一RL。[受限CPT对照](https://arxiv.org/html/2610.25836v1#S3)用内容中性query走同管线/同文本预算作控制；它比较的是选择信号，不说明某句反思本身导致失败，也不证明检索文本补齐了唯一缺失skill。CPT同时改变RL起点与KL reference，目标状态更常出现而成功率只小变时，整体收益也不能全归该局部修复。更晚插入或扩大语料仍可退步，小pass@k差额不授真实能力边界已扩张。先验RL挖掘、索引、检索、CPT、全部重跑与旧能力回归都计费，不能只按新增tokens结算；marker失配、retention或净预算不合时，保留原mixture/通用CPT控制及可信任务监督，不由‘模型自己的失败’批准label-free或无成本自修。<!-- source-family:SF-2026-ARXIV-2610-25836 -->

## V3 — 2610.29357 MCCL；2+2+2=6；建议具体 No Change

原证：[exact-v1](https://arxiv.org/html/2610.29357v1)、沿有效 [§4 原件](./arxiv-source-2610.29357-section4.txt)/[§4b 原件](./arxiv-source-2610.29357-section4b.txt)。本批全页缓存 [此件](./source-system2-2610.29357.txt)含工具截断警告，不当完整原件；采用命题由前述两份未截断必要摘取核。复用已读核心 taxonomy/两loop/五stage有效层，现定点完成§4.1–4.3协议、实际实验与理论图区分及actualowner。日证 cs.CL New[44]/cs.AI Cross[145]。

旧约束→增量→选择：不以存了/召回多少memory替未来行为收益，联合测 retained capacity×reading 与stateful-reset随更新轨迹；真实增量是有限配对storage/read交互和token/latency非同方向的证据，不是命名MCCL/taxonomy就有新系统机制。保持6分，不因具体NC撤贡献。

必要标准证据：Qwen3-30BA3B用于construction/answer/localjudge；LoCoMo10dialogues1540Q、4×4storage/readgrid，512→2048读取在1/8history的F1增.89pp/fullhistory3.82pp，差2.93[2.06,4.02]为对话clusterbootstrap。LongMemEval选100例非全量；LoCoMo词面F1与另处local semanticaccuracy不能混同比。IdeaBench50fixedqueries×3随机训练顺序，Mem0 defaultonline会在eval50query时写库，t0偏移非真正空白冻结基线；8192/32768上限均未binding，不能把后期负gain归缺容量。每16/64dialogueconsolidation减occupancy仍不救最终负gain，不推出所有consolidation有害。9conversation/180Q同banks对照中summary读取43.52tokens而全读729.78，但query latency .367s高于.154s，F1差−.72pp CI[−1.14,−.27]；latency含retrieval/summary/answer不含offlineconstruction。

理论隔离：§4.3加性resourcepowerlaw明确hypothesize；Figs7/9/10/11用preset函数/参数的理论示意而非拟合实测scalinglaw。Fig12/13汇集其他publishedstudies不冒本文同budget实验；不由跨paper参数量/写入次数推统一指数。有限新实验证据不足批准genuinecontinuallearning/longrunproduction。全部write/maintenance/read/answer、反复probe与judge均计费，少inputtoken不是总费/latency更小。

actualowner具体NC：Ch77开篇rawstate与表示支持、writerpayload/readerprobe双预算完整段；“评估Memory”Neuromem因果stream/分阶段construction-maintenance-retrieval-answer完整段及修订break-even；MemoryArena rawhistory共存、on/off暴露/measurementfloor、干预矩阵、matchedcontent-vs-visiblelength以及acquisition/retention/forgetting/transfer完整局部均实读。现有正文已明确独立storage/readout/阶段费用、原history基线、写入/读取干预与跨更新能力验证，且禁止压缩率签质量/后期单平均签持续学习；本稿具体capacity/readgrid与小banksummary是这些选择边界的新证据，不纠正现判断，新增taxonomy或一组局部数值不足形成长期gap。唯一 AGENT-MEMORY；建议本窗报告保留具体证据、Books No Change，不把owner充分当贡献排除。

## V4 — 2610.29489 Long-vector FlashAttention；2+1+2=5；Ch49 小 gap

原证：[exact-v1](https://arxiv.org/html/2610.29489v1)、[原件](./source-system2-2610.29489.txt)。实读§II必要定义、III stock/packing及宽度profile、IV软件exp与spill/fusion条件、V转置recurrence/Alg3、VI完整hardware/measurement/region定义、VII A–D实际控制与VIII条件反侧。未核实现、逐位数值验证或任务质量；不读全references。日证 cs.AR New[4]/cs.DC Cross[17]/cs.PF Cross[3]。

旧约束→增量→选择：GPU/短SIMD自然行布局让PV沿d64执行、512FP32长vector仅填1/8，并把rowmax/sum作水平归约；把score和runningoutput的query轴改连续，让queryblock控制所有region的VL，以vector perquery状态沿keys作elementwise max/sum。数学normalization域不变，不把沿query向量化说成跨query归一，也不把少水平归约说成不遍历key。另degree6exp系数移scalarfile用splitmul/add多一指令避免vectorcoeff驻留spill；保持同polynomial不等浮点逐bit相同。

直接控制/反侧：Q packing替K packing每arm都计；V不物化转置，最终output转回融合division但增加该region9–13%（region<.5%总kernel）。Reorientation不总更快，Bq128比fused慢；Bq512/vlmax才胜，适合prefill/training，不适合query1decode。Fused与reorient各从scalarcoeff分叉，不把倍率连乘。EPAC RVV.7.1、2KBregister、32architectural/40physical、FP32-only、单核单head/N1024/d64；chip1GHz的DDR带宽6–7B/cycle、FPGA50MHz32B/cycle，芯片1.84–2.08x与FPGA2.71x不混；29.7%peak不是服务GPU利用率。RAVE仅instructionstream无cache/pipeline模型，cycles另实际counter；stock为作者PyTorchCPU结构RVVport，各arm vectorized非scalarbaseline，分别调8tiles。d128时PV增益降低，没有GPU/短SIMD实测、全LLM端到端/尾延迟证据；未披露跨seed/repeats/完整数值error统计，保独立artifact与数值验收。

actualowner：完整读Ch49 FlashAttention开篇/FA2–3硬件适配与后续mask隔离、scan、tile/wafer/XDNA/CIM执行分支。已有IO与不同硬件collective/stationarity，但未解释长vector下“query轴contiguous将水平softmax归约变为perqueryvectorstate”的同算子轴选择；不能只以通用硬件适配覆盖具体机制。唯一 INFER-TENSORRT-LLM，一小段，不在Ch14重推数学。

条件逐字 PRE：
> 长向量机器还会让 contiguous axis 成为计划选择：若 head dimension 远短于物理 vector，沿它执行 PV 会留下空 lane；可把 score 与 running output 的 query 轴改为连续，让足够长的 query block 决定各阶段 vector length，并用每个 lane 保存一个 query 的 max/sum，沿 keys 作逐元素累积。归一域仍是每 query 的 keys，消失的是水平归约，不是 key 计算；packing、输出布局还原与浮点数值验收仍付费。长 query block 的受限实硅对照支持这条 prefill 分支，较短 block 反而可慢，单 query decode 仍宜原轴或别的分组。寄存器压力还可能使多一条 scalar-coefficient 指令比 fused vector coefficient 更快，但需单测 spill 与真实 cycles；宽度、shape 或净收益不合时保原布局、已验 polynomial 与成熟 kernel，不将单头倍率外推完整服务。

精确插点：Ch49 FA2/FA3硬件适配完整段后、mask构建隔离完整段前。完整上段：

FlashAttention-2 进一步优化并行划分和 work partitioning；FlashAttention-3 则面向 Hopper 等新硬件利用异步数据搬运、WGMMA/TMA 和低精度能力。它们说明：kernel 优化不是只改数学公式，而是在适配硬件的 memory hierarchy 和执行单元。

完整下段：

优化attention的mask构建时，还须隔离每次调用的构建环境：临时替换共享模块的builder或offset helper，即使在finally恢复，交错退出也可能把另一调用的device/长度闭包留下，影响同时运行的原生消费者。[一个公开修订](https://github.com/ByteDance-Seed/VeOmni/commit/c84d10db668169f076c71b922b007b47e1a2f91c)改为本地组合padding/offset predicate，并显式传递shape、device与block size；编译缓存复用不再借共享函数替换，但仍须验原padding与可见token语义。其交错测试隔离了compiler启动，不能认证任意并发编译或全部硬件；局部构建、编译及回归均付费，特定CPU lowering失效还需eager回退。串行独占构建在简单环境仍可成立，无法证明隔离或语义一致时，保原已验实现、显式序列化/进程隔离，不由一份编译成功日志批准共享运行环境。<!-- source-family:SF-2026-VEOMNI-1328-C84 -->

## V6 — 2610.29523 pplx-embed-v2-late；1+2+2=5；建议具体 No Change

原证：[exact-v1](https://arxiv.org/html/2610.29523v1)、[原件](./source-system2-2610.29523.txt)。实读§1–2全部teacher/student目标、3.1internalbenchmark口径、3.3cross-model、3.4agentic/§4，不遍历各domain应用表；未核HFartifact/代码/复现/图像像素。日证 cs.IR New[15]/cs.CL Cross[126]/cs.LG Cross[205]。

旧约束→增量→选择：MaxSim的query/doc两侧可由不同大小encoder承担；把两student各token归一向量对齐同18Bteacher坐标，允许.6Bquery对9Bdocumentindex，而不是要求两侧同模型。具体delta是同teacher表示蒸馏的跨大小多向量部署实例，不是任意encoder可互换。训练loss是对应token的Euclidean norm（非平方），query/doc positions分别平均再相加；teacher冻结。Fullattention去causalmask但GDN仍causal，不能称全网络双向。9B最后8textlayer全训+其他LoRA，.6B全训且原.8B每block删2/3GDN；18B由27B删末20层，三者制备不同非仅参数名比较。

证据/限制：pair186M rows/981slices/28sources，raw88.3/8.3/3.4%与采样56.5/30.9/12.6%不同；teachercontrastivepair再hardnegative、studentreusepair非contrastive同流程。Golden-ratio sampling的sourcecontiguousCDF是局部构造，不采用通用trainingquality保证。128dim只定坐标宽，multi-vector数量/index/MaxSim仍费用；.6B240Mtextactive不等全部594M常驻。72publictasks自组6domainbenchmark完整list未披露，论文明确cannotindependentlyreproduced；domain等权不是72task等权。§3.3小query/大doc比小/小domainavg+1.6pp，未超大/大81.3且存在domain切片baseline更好；约等queryencodingcost不是全生命周期时延/fee相等。Agenticbenchmark+judge/搜索次数不识别所有end-to-end因果；无hardware/precision/完整wallclock/SLO/训练seed证据，不由共同teacher推出严格兼容任意任务。

actualowner具体NC：实际读Ch76 lateinteraction阶段与prompt/长度契约、teacher对query/positive/hardnegativeembeddingmatching两完整段、teacher/student/projection/indexrevision共同绑定；另embeddingupgrade旧indexcompatibility、adapter/reprojection/回填/rollback与冻结passage/query侧适配完整段。已有“监督对象是teacher表示而非pairscore”和“query改动与持久docindex的配对兼容要独验”的具体选择接口，且早段已有query/doc非对称部署、offlineindex费用；本稿共同teacher的局部实现不修正这两条，不需为9B/.6B重写同一机制或新增命名分支。保5分报告和跨模型实证，唯一 AGENT-RAG，建议 Books No Change；不是因报告缺hardware就撤贡献。

## V5 — 2610.29873 HAWK；2+2+2=6；Ch55 小 gap

原证：[exact-v1](https://arxiv.org/html/2610.29873v1)、[原件](./source-system2-2610.29873.txt)。实读§4.1–4.5/Alg1全部handoff、§5.1–5.4全部协议/直接对照与效率分母；不核驱动代码、故障注入或无关Appendix。日证 cs.AR New[6]/cs.DC Cross[19]。

旧约束→增量→选择：有GPU→NPU RDMA还不等可消费tensor到达。目标NPU按DRAMchannel有独立pointer-size/layout，单contiguousregisteredbuffer可造成channel分配失衡/OOM或到站跨channel重排。作者扩NPUpeer-memoryclient与tensor-awareallocation，每channel一连续RDMAregion，GPU先把目标channel片段排成大连续块，再在transfer中对应落位，接收端tensor可直接消费或仅有限intra-channel搬动。增量在physicalallocation+transfer/layout联合，不是笼统GPU/NPU分工或RDMA较快。

必要边界：仍有GPUtransform、copy-to-registeredbuffer、metadata exchange、batchrequests、waitcompletion/reconstruct/notifyrelease，不能称零copy/零host控制。Channel数限制request分片数量，按小tile直接映射几百byte请求方案会慢；把预处理放Prefill是该负载带宽余裕条件，不授任意GPU总有余量。Alg1只简化忽略firsttoken整数，requestID不是完整epoch/fencing/retry授权；tensor重建后buffer释放与未来consumerlifetime/faultrecovery无实证，不据伪码批准生产ownership安全。ReverseNPU→GPU、其他NPU/activationcut为讨论，不冒已测。

真实对照：一个prefill/decode实例各TP4、Llama3.1-70B唯一模型，prefill4×A100PCIe40G，decode4×A10080G对4×Tenstorrentp150a；200GbpsHDR/ConnectX6、vLLM.10、TTdriveruser.68/kernel2.5、Mooncake.3.6。官方stack模型/设备数耦合限制外推。Hoststage两同异构、GPUdirect、GNHAWK四路；singlecontiguousNPURDMA原型servingOOM故未量化，不补虚构finiteperfbaseline。Synthetic10–1280MB端到端transfer从request到KVpool含转换，短tensor残余开销；在线Poisson ShareGPT/LongBench两负载，SLO TTFT2s/15s、TPOT200ms、90%attainment；summarizationNPUdecode稍慢/排队backpressure仍在，peak吞吐低7.88%不是全负载不变损耗。

费用口径：1.26/1.15x power efficiency分母是双方aggregate ASICcore/SRAMpower，NPU接口只报core，GPU由DCGMboard乘NVBit/powersimulator估ASIC比例；不是整板、内存/网络/CPU全系统energy实测。1.72/1.61x是throughput/设备市场capex参考，非TCO/实时价保证；H100decode对照power优势仅1.03x，不能宣称NPUs普遍省26%。注册、多buffer、变换/驻留、驱动/栈适配、完整传输/queue与回归都计费；代码未来release承诺非已开源验证，无质量等价/跨平台fault测试。

actualowner：读Ch55KV语义producer/consumer与ownership、transfercost完整局部，以及codec/selectedtransfer/topologyepoch/跨层completion分支。已有layout“兼容”条件却没有独立DRAMchannelallocation下“相同elementorder仍非tensor对象、单region可channelOOM”的handoff实现选择；这不是仅加产品案例。唯一 INFER-PD-DISAGGREGATION，不在Ch49/70重复成本论述。

条件逐字 PRE：
> 异构接收端还可能让“同一元素顺序”和“同一可消费 tensor”分离：若目标按 DRAM channel 显式分配 tensor，普通单连续 RDMA buffer 会留下跨 channel 重排，甚至某些 channel 先耗尽而总容量仍有空闲。可以按目标 channel 分配注册区，在发送侧先把各区片段聚成较大的连续块，再以对应 RDMA 请求完成落位；这用发送侧变换、额外 buffer/metadata 与注册管理换少一次到站重排，不是零 copy 或只接通 RDMA 即可。Prefill 的带宽余量、目标 layout 与 channel 映射须实测，completion 后的 tensor lifetime、取消/重试与回收仍另有责任。有限 GPU–NPU 对照支持这一交接分支，不把芯片功耗估计或设备价格比当整机能耗/TCO保证；布局、生命周期或净收益不合时，保留显式 staging/转换和同构已验路径。

精确插点：Ch55 ownership完整段后/Transfer Cost 下界标题前。完整上段：

Handoff 还必须转移所有权，而不只是复制 bytes。系统要明确哪个 worker 对 cache 生命周期负责，失败重试是否会重复生成或泄漏 cache，以及 Decode 在 cache 未完整到达时能否开始执行。

下接标题：## Transfer Cost 下界

标题后首完整定义：

设需要传输的 KV bytes 为 `M_transfer`，有效链路带宽为 `BW_effective`，固定协议与排队开销为 `t_fixed`，理想化下界为：

## V7 — 2610.28711 Qwen-Audio-3.1-ASR；2+2+2=6；Ch23 小 gap；旧版具体重叠已有限核

原证：[exact-v1](https://arxiv.org/html/2610.28711v1)、[本窗原件](./source-system2-2610.28711.txt)；已知直接前身仅定点 [3.0 exact-v1](https://arxiv.org/html/2609.07549v1)/[旧版有限身份原件](./source-system2-qwen-old2609.07549v1.txt)。不加载旧Daily或通查版本。实读现§2.2/§3.4.2全部serialization/fieldloss/grid、§4variant接口、§5.7 display/final完整协议、§5.8全四数据表与解释；必要旧§4.2–4.3与其speaker/grid字段定位。现§3.5.2/3.6仅为最终评估多阶段recipe归因限制，不采用OPD为新机制。未核APIartifact/复现/图像像素。日证 cs.CL Cross[94] from cs.SD。

具体去重：3.0已明说hybrid streaming/full-context最终刷新，并有context/hotword/nativepolishing，所以3.1 display-final不是首次新机制；3.0cooldown也已有speakerdiarization训练任务词，不能把出现该名当本窗新概念。有限核未见3.0公开现§3.4.2的ID-number专属10×CE与12.5Hz/80ms framegrid联合输出接口，采用本窗这一具体增量及其评价边界，不整族判重复。

旧约束→增量→选择：联合ASR输出的文字、speakerlabel与timestamp权重/分辨率不同，flat CE可把稀少但重要的identity字段压低。当前newline [SPK|start-end]text按start排序但interval可重叠、speaker ID只recordinglocal非实名认证；只把ID numbertoken CE×10、其他字段×1，且把1ms标签量化到audioencoder/adapter实际12.5Hz的80msgrid。改变联合输出监督分配/可表达时间粒度，不是所有低loss字段都加权、提高时间戳精度或分离外置diarizer。

直接证据/反侧：ID number仅2.90%token/1.97%unweightedloss；timestamp33.44%token/49.51%loss、format14.48%token/.23%loss却不加权。Figure6caption为digitizedplots，共用纵轴但刻意省绝对loss和iter，正文仅支持same-mixture的fasterconvergence/DER-cpWER定性改善，不能补精确加速倍数/收敛步数。最终Table7四集合约4minchunks标准化，部分competitor直接抄technicalreport标*，两Qwenvariants不是任意逐项同优；finaljointpipeline多阶段数据/模型/OPD等不同，不能把全部收益唯一归IDweight或grid。没有整场跨chunk speakeridentity、absolutetimestamp误差/时间grid更准或物理权限保证。

Display/final只用作边界：Table6声学content结束→display，不是首包wallclock/最终刷新latency；Qwen selfhostH100、对方API、10streams、网络相当是假设。Streamingindustrytermmean63.93%与final92.82%是不同输出人口，不能把100msfirstchar与finalquality拼成单一实时SLA。SD/AU仅相应nonstreaming variants，Streaming/Message不支持，不以Next产品名冒全variant共同能力。Human/model标注、模拟meetings/TTS、jointfield训练/多阶段RL/teacher、长录音chunking和独立输出回归全付费。

actualowner：实读Ch23语音encoder/grid/duration接口、multi-speaker配对与DM-ASR来源分责完整局部。已有外置speaker/time作为可错prior与跨chunk映射，不含jointoutput时字段稀疏监督及时间标签过细于encodergrid的选择；选唯一 MULTIMODAL-REPRESENTATION，字段权重作为该语音接口所需训练条件，不在Ch29重写通用weightedCE。Ch42流式/final原边界不新增旧机制。

条件逐字 PRE：
> 若说话者、时间与词内容改由同一自回归目标联合产生，字段数多不代表监督足够：稀少的 speaker-ID number token 可以另加权，而已容易学会的 formatting 不必因为 loss 小就同样放大；时间标签也可量化到 encoder/adapter 实际帧网格，而不是保留远细于该输出网格的时间标签。这样的序列按起始时刻排列仍可保留重叠区间，speaker label 只在当前 recording 内一致，不授实名或权限。受限同-mixture对照支持字段分配与网格选择，省略绝对步数的曲线不授精确训练加速；约四分钟 chunk 的结果也不保证整场跨 chunk identity。标注、量化、联合训练及长程独立核验均付费；时间/身份或迁移失败时保原声、可靠外置 diarization/alignment 与人工核验，不把更低 DER/cpWER 当所有语音接口或实时流式均已支持。

精确插点：Ch23 DM-ASR完整段后/Cause-aware错误恢复完整段前。完整上段：

说话者、时间和词内容也可以分别生产，再作为同一转录接口的条件：先从前端取得speaker区间，把chunk内标签重映射并保存跨chunk对应，以离散时间/controltokens交给语言消费者；第一turn读取声学，后续文本turn复用已编码状态。标签与时间是可错的输入prior，不因模型能续写就变成真实speaker身份；哪一组件提供finalspeaker/time与文字须逐配置记账。[DM-ASR的受限对照](https://arxiv.org/html/2604.22467v1)中，外置speaker加模型时间的主表与不同finaloutput配置不能拼成一个fullyLLM系统，部分语言/数据切片也退步。Diarization、wordalignment监督、声学编码、LoRA/projector与状态驻留都付费，短chunk结果不授任意长stream全局identity或实时性；前端cue、chunk映射、重叠语音或下游质量失配时，保留原声、可靠外置speaker/time与专用转录/人工核验，不用较小decoder参数替完整系统费用或声学真值。<!-- source-family:SF-2026-ARXIV-2604-22467 -->

完整下段：

语音恢复还应区分‘有一个不确定的token’与‘整段内容没有形成token’：只看解码entropy，可能遗漏deletion，也不能说明错误来自声学受损还是已有输入下的语言识别失配。一条分支保留冻结ASR的内部表示，分别用token/frame级小detector提出错误位置和distortion原因，再将被flag部分交给相应澄清/恢复流程，而不让一个总confidence同时拥有定位、归因与修复权。[Cause-aware ASR v1 §3–5及A.8](https://arxiv.org/html/2605.25404v1)的clean pseudo-oracle与合成noise标签只是受限监督，不是真实认知因果；detector优先级也不等最优诊断。原声/hidden-state前向、标注、detector与多轮询问/TTS/LLM均计费，漏检、误归因或只允许修flag位置会限制恢复；English/冻结Parakeet、模拟用户/同模型judge与单run改善不认证真实人类或production效果。原因、位置或用户负担未核时，保留原声、专用转录、明确不确定性与人工澄清，不由较低WER替任务正确性或真实输入签字。<!-- source-family:SF-2026-ARXIV-2605-25404 -->

## V8 — 2610.29464 DIFF；2+1+2=5；Ch76 小 gap

原证：[exact-v1](https://arxiv.org/html/2610.29464v1)、[原件](./source-system2-2610.29464.txt)。实读§2.2–2.3/§3.1–3.4全部方向/置信/球面更新、§4设置、§5主对照/ablation/K反侧、AppA.1正交分解、B小系统解、D设置与E.3/E.4直接反侧/费用。未核实现/复现、全E逐query结果或图像像素。日证 cs.IR New[12]。

旧约束→增量→选择：固定encoder/docindex，反馈vector只说明某个局部修正方向，不应把其未表达的正交方向一并拉回零。先投到原unitquery切空间，按单位方向u/幅度l形成 (uᵀδ−l)²，配λ>0的原queryprior，联合解δ而不是对完整反馈点作平均；pointwise平方目标可精确拆此directionalloss+orthogonalpenalty，是有限几何identity，不是反馈语义正确性定理。

可支持数值范围：τ≥0/λ>0使SPD唯一解，δ在u span/tangent；以W=sqrtτ的K×K系统代D×D，O(K²D+K³)仍有费。主HTMLplain W字段不一致但LaTeX与AppB均sqrtτ，不照抄wrongdiag。最后角度min(||δ||,gθup)再sphereexpmap、δ0保q；confidence/MAD或residual0的degenerate处理未披露，不补可运行recipe。RelativeMADsigmoid affinity和方向coherence只是几何heuristic，不是绝对relevance/独立校准/贝叶斯truth；一致而错的feedback仍会误导。AppA.2 supported directions专指τ>0，主theorem不得删条件外推semanticcomplementarity或无关反馈必不影响。

直接控制/反侧：14BEIRsubsets、BGE/E5/Qwen3Embedding.6同encoder编码所有对象，PRFtopK或Qwen3.8-27B生成HyDE/Q2D/CoT，K1/3/5/10/20主K5；5runs、FP16batch256/FAISSGPU/单A800。全部法gridsearch而dev/test调参隔离未完整披露，局部最优不冒纯zero-tuning；报告nDCG/Recall不是answer支持。Table2的point-targetcontrol实际δ=Στlu，不是Eq4同λ完整ridge minimizer，ablation不能唯一归因所有改动为directional替换；保机制identity，不采“单干预严格证实唯一原因”。PRF与HyDE偏好angle不同、大K不应普遍增加；E.4仅10queries局部execution，AnchorQE3.67x不等包含LLMgeneration/encoding/index/全RAGfee或SLO。

actualowner：实际读Ch76queryvariant/reformulate、query-only向量正负目标两完整段、风格向量平移/latentresponse训练与RIME接口。已有“只改query/不重索引”，却没有“每feedback仅约束自己方向、避免把其他修正当误差”的局部目标差异；不能以已有向量优化覆盖新目标。唯一 AGENT-RAG，保固定索引和原文事实权威，小一段不新增数学小节。

条件逐字 PRE：
> 多份反馈也未必都指定完整的目标 query：在归一向量的局部切空间，可把每项只写成沿其支持方向的投影约束，再与原 query 的正则先验联合求修正；拟合整个目标点还会惩罚它未表达的正交方向，因而可能压低其他反馈提出的互补变化。正则化小系统与有界球面更新控制的是几何位移，不认证反馈相关或正确；相对 affinity 和方向一致性也可能一致地错，退化方向/归一统计须显式处理。受限多 retriever 对照支持这条固定 encoder/index 分支，但反馈来源与角度预算会改变取舍，局部消融并未唯一隔离全部改动。反馈生成/检索、编码、求解、调参与原文支持核验都付费；方向、数值或实际质量失配时，保留原 query、简单平均/多路融合和独立取证，不由 posterior 名称或较少额外 retrieval 批准答案真值与净服务收益。

精确插点：Ch76 query-only完整费用/反侧段后、风格示例向量平移完整段前。完整上段：

这种 query-only 分支省去模型重训与重新索引，却增加分解调用、子查询编码、梯度步骤和选择预算。[有限否定检索对照](https://arxiv.org/html/2603.09185v1#S4)中它优于直接扩写的 AVG/RRF 变体，过多步骤仍会退化，否定 pairwise 得分也远非可靠排除；参数优化的毫秒计时不含分解、编码与完整检索/回答成本。应把原 query、子查询、权重和有限步预算绑定为同一次查询身份，分别验收相关性、排除条件与真实总费用。分解不可信、目标越界或排序退步时，保留原 query、已核多路融合与可验证字段过滤，不把较远的负向 embedding 当作证据反驳、访问授权或答案真值。<!-- source-family:SF-2026-ARXIV-2603-09185 -->

完整下段：

当检索对象是供生成器参考的风格示例，而不是回答问题的事实证据，语义最近邻也未必提供合适条件。已有合格的源/目标语风格标注与参考人口时，可以分别估计目标语原生文本和翻译文本的表示中心，用其条件差异调整当前检索向量，再从目标语示例库提出少量近邻，交给翻译器作参考；这是示例选择提案，不是更新翻译器，也不让邻居内容成为待译文本的事实来源。原文、目标风格、标注/读出方式、encoder与bank版本须共同保留，未披露的逐请求风格判断或向量基点不能由公式补成已实现的无监督接口。[受限跨语对照](https://arxiv.org/html/2507.00216v1)中，风格相关提高仍可伴保义/质量退步，Pearson相关为一也不保证逐句风格值或方差相同；不能把几何平移称为消除文化差异。标注、参考翻译、风格读出与示例编码、额外输入和独立保义校核均计费，五个近邻不等五个独立证据；条件人口不匹配、语义漂移或净费用不成立时，保留原文本、普通翻译/显式风格提示与人工审校，不由较高相关或局部偏好分批准新内容。<!-- source-family:SF-2025-ARXIV-2507-00216 -->
