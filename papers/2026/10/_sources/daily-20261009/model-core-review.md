# 四模型必要证据与 owner 提案

作者 supplement_20260311；仅 Daily 2026-10-09 / BJT 2026-10-08。冻结 arxiv-screening.md 的 25 个完整题摘及 2 个标题排除项，不扩大查询。review_mar11_continue 已独立全部新增 13 个题摘准入；本文件只负责 10395/10381/09346/09877，题摘通过不等必要 Source 或 Books 通过。公开日复用已核官方 Oct8 分组；不把 Submitted 当公开日。不写 Report/State；Books 仅在 root 逐项授窄锁后写。

## 2610.10395 — 固定构造的算法执行与状态交接

[exact-v1](https://arxiv.org/html/2610.10395v1)，[当前官方身份页](https://arxiv.org/abs/2610.10395v1) 实际轻核，无当前撤回标记；日期 2026-10-08 复用 LG 官方组 #338。原有可学习层更新不说明执行某个已知数值算法 → 指定无 softmax/Norm 的 linear-attention 与 bilinear/ReLU block，将当前 graph 和 multiplier 一起编码、更新并交给下一个 block → 重新考虑算法执行的算子与完整状态验收，而非把 graph 正确率当 executor 正确率。评分 2+1+2=5；重要构造/状态边界、单模型组件、稳定可复用。标准必要证据完成；Ch17 具体状态交接 gap 触发受影响内容深入，不改分。

实际读 HTML §3–9（122–299），其中 Alg1/2、§4 重复平方与 scratch/persistent 分账、§5 undamped multiplier、§6 fixed-stage 条件与 §8 对照；F.1（808–816）只补中心状态持续复用的实现纠错说明。未遍历全部证明/附录、图 pixels 或 GitHub，不授形式证明机器验证、代码运行、全实验复现。

机制：数值 prompt 每变量一行，保留 covariance/mask 与当前 W，控制行保留 α 及外部 ρ/γ/b。固定 unnormalized linear attention 计算矩阵积，bilinear 项与 ReLU 计算逐元素乘法和软阈值；重复平方得到固定指数 N 的约束及其梯度。执行 block 写回 W/α，并清理 scratch；外部仍决定 penalty schedule、line search/停止。这不是普通 causal softmax LM 的现成机制。实数精确构造与有限精度实现分开；只为特定 primitive class/affine 编解码给 logarithmic depth，不能套所有 solver 或生产 LLM。

直接反侧：同 W 不同 α 在非零约束梯度且阈值外可产生不同下一状态，不能仅保 W。接近无环时 α 误差可不衰减，状态误差不等 graph 误差；fixed-stage 收缩/不变区域/舍入界不认证外部 controller 或全局因果恢复。270 个原轨迹球均未通过曲率测试，额外优化后 46/90 中心才通过，不能把额外费用和早期步数藏进更新界。训练的普通 width64 attention 模型没有同构造一样的深度及 bilinear 子层，其有限失败不能证所有训练不可学。

关键评价绑定：literal attention/FF 单步 254 个有限 reference case 与另 1 overflow；单步每次重新编码，不证明 persistence。F.1 indexed specification 的 50 输入/150 三块 full-stream 比较才测继续交接，且只是 sampled float64；旧 wrapper scratch 未清会污染后块，当前文档明示清理，不追旧版历史。7 拓扑的 220 数据集用 Gaussian noise 和固定 topology weighting，arithmetic replay 与 solver 同错，不是真实 observational benchmark 或独立 graph 真值。训练是 p5、四 tied repeats、5 个尝试 seed、2460/12epoch 或 24600/30epoch，p10 转移仍失败；failed-run/finite-only summary 不能冒充所有运行都通过。硬件、batch/concurrency、实际 kernel/runtime SLO 为 Not Disclosed；此处不作 Serving 性能命题。编码、状态/宽 scratch、两次约束计算、外部调度、有限精度校验和 solver/graph 两道评价均付费。

唯一 owner 拟 `MODEL-TRANSFORMER-LAYER`：[Ch17](../../../../../books/part-02-model/17-transformer-layer.md)。actual 366–408 完整 Norm→层堆叠算法解释→Layer冗余邻接，另 588–668 recurrence/状态预算实际比较；Ch16/18 开篇交接已读。现 383–387 已有“存在性构造不等生产 hidden 机制”，但没有指定数值 executor 的 persistent/scratch 交接与单步重编码≠full-stream 复用验收；不第二 owner Ch22 或科学应用节点。

### 最小逐字 PRE（有效独核通过，已写并实际 POST 通过）

建议在 Ch17 现 387 算法解释完整段后、Layer冗余标题前一段：

若目标是执行一个给定数值更新，而不只是为可学习层提供优化类比，算子与状态可以直接按算法构造：把当前矩阵和乘子放在 persistent registers，用无 softmax 的 linear attention 做矩阵积、bilinear/ReLU 子层做乘法和阈值，再清理 scratch 后交给下一块。外部控制器仍拥有更新步长、penalty schedule 与停止，丢掉乘子可能使同一矩阵对应的下一步不再唯一。[受限固定权重构造](https://arxiv.org/html/2610.10395v1)因此要求分测同状态/控制下的单步对齐、完整 residual stream 的反复交接，以及 solver 自身的任务结果；每步重新编码和 arithmetic replay 不代替 scratch-reset 验收。有限 float64 检查不授任意 kernel 精确，fixed-stage 的收缩和误差界也不认证外部 controller、因果恢复或普通训练必能学会该执行器。编码、宽状态、完整更新与精度/回归检查都付费；状态或数值条件失配时保留显式数值 solver、完整状态和 reference transition 测试，不把流畅输出或最终 graph 命中批准为算法正确。<!-- source-family:SF-2026-ARXIV-2610-10395 -->

实际整合：review_mar11_continue非作者必要Source/actual owner与逐字PRE通过后，root授Ch17该单段及本人注窄锁。作者写new389/own863并顺读；root非writer实际366–410完整Norm→算法→新段→Layer冗余及863注回对有效Source/PRE，POST通过并释放锁。仅此家族整合成立，不授DAY。

## 2610.10381 — 跨 loop residual 与延迟入库

[exact-v1](https://arxiv.org/html/2610.10381v1)，当前[身份页](https://arxiv.org/abs/2610.10381v1)轻核无撤回信号；日期2026-10-08复用LG Oct8 #342。共享权重仍产生不同 loop KV → 用末 loop 的量化重建 anchor 加各 loop 的旋转低精度 residual，当前 token 则保 BF16 等 anchor 可用才入库 → 重选跨 loop 近似表示与因果可用时间，而不是直接共用同一 KV。评分2+2+2=6，KV表示/loop执行与cache-write边界、稳定可复用；标准完成，actual owner 的延迟写入缺口深入受影响接口，不改分。

实际 §2–5.3（122–264），关键 Tables1–5，A.1–2（350–365）、A.3 EqA1/A2及其元数据说明（371–378），G.1量化reference目标（473–479）。另5.4（265–289）只辨别activation immediate消费为何必须Previous-loop，不采用其扩展结果；没有全AppendixG/H、pixels、代码或复现。rotations/LS的特定优化超参不作已核完整训练recipe。

机制：每token/head的LS系数是X与量化重建anchor的内积除其平方norm，不是全局固定相似性；rotation针对residual，anchor和residual共享对应旋转。Last-loop避免链式重构但当前token最后loop之前没有anchor：prefill各loop BF16 causal计算后再量化存储；decode从压缩past读anchor+本loop residual，当前BF16 KV暂存，按softmax统计合并past/current，完成末loop后存packed codes和metadata。不是先读尚未产生的未来loop，也非用一个KV取代所有loop。LS零norm guard未在已读定义披露，不补可执行全域协议。

评价：Ouro1.4B四loop、Huginn3.5B每四loop一anchor（32loop分八组），weights BF16；INT2组16/32、INT4组32。Table2的effective bits属于direct/OptR-H，residual另有约0.1bit LS，不能说严格等byte。最小group32 mixed full方法平均52.37 vs BF16 52.94，Huginn MATH14.6<16.4，Ouro GSM77.03<79.23等局部反退；无statistical noninferiority。Table3 Last-loop uniformINT2 LS69.2→67.8反退；Table5组16 ascending+rotation74.6<uniformINT2+rotation75.2，非所有配置皆优/anchor位宽普遍最优。校准/旋转增加的训练与数据预算不由相同KV预算抵消。

Single GPU RTX5090或RTXPRO6000 96GB；A2 greedy单回答，GSM/MATH/HumanEval/MBPP分别1319/500/164/378，prompt/shot/输出限model-specific，code仅original tests basepass1。decode throughput只Ouro/5090、2k–16k、batch1→128按power2试、生成128token，warmup1后三次运行均值且不含prefill；fixedbatch和peak换batch不能混。vLLM exact revision、arrival/concurrency与tailSLO未披露，不能拿kernel/cache交通推完整服务。理论storage不含整个lifecycle的临时BF16驻留、metadata/layout、校准/rotation、pack/gather、重构和实际allocator费用。

唯一拟owner `INFER-KV-CACHE`：[Ch45](../../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)。actual1406–1426已有信息时间/跨迭代drift预算，1550–1574完整evidence→anchor/residual→logit补偿→eviction；Ch44/46开篇交接已核。既有anchor/residual是历史token分层、未承载同token跨loop anchor尚未产生的暂存→最后loop结束才写cache接口，值得单段差额；不第二ownerCh17/49。

### 最小逐字 PRE（非作者 Source/PRE 和实际 POST 已通过）

建议Ch45现1562历史anchor/residual完整段之后、1564logit补偿之前：

共享权重的循环层仍产生各轮不同 KV，近似表示还可以沿 loop 轴分解：保存每组最后一轮的量化重建 anchor，以按 token/head 的缩放与旋转 residual 重建其他轮，避免链式读取全部前轮。这里的关键不是相似度本身，而是 anchor 何时可用；当前 token 尚未完成最后一轮时，各轮 KV 继续以原精度计算并暂存，结束后才量化、形成 residual 并入库，past/current 的 attention 另按 softmax 统计合并。[ResidualQuant 的受限对照](https://arxiv.org/html/2610.10381v1)支持这一缓存分工，不把跨轮相似当 KV 相同，也不将小重构误差认证为全部任务无损。Anchor 精度、loop分组、缩放、rotation与packed metadata共同绑定；质量仍有局部反退，理论存储倍率和排除 Prefill 的 decode throughput不代全请求收益。校准、原精度暂存、packing、重构与全部实际驻留均计费；anchor、数值或质量条件失配时保留各轮 FullKV、独立量化或更高精度，不提前读取未产生状态，也不从权重共享推缓存共享正确。<!-- source-family:SF-2026-ARXIV-2610-10381 -->

实际整合：review_mar11_continue非作者necessary Source/actual Ch45 owner/PRE通过，root授该单段与本人注。作者写new1564/own2140并完整邻接顺读；root非writer实际1550–1577 anchor→新段→logit补偿→eviction及本人2140注回对有效Source/PRE，actualPOST通过，窄锁释放。仅此家族有效，不授DAY。

## 2610.09346 — 低位 policy 的实际访问前缀恢复

[OnlineQAT exact-v1](https://arxiv.org/html/2610.09346v1)，[当前身份页](https://arxiv.org/abs/2610.09346v1)轻核无撤回或新版本信号；公开日2026-10-08复用独立官方组准入记录，不以Submitted Oct7代替。原有固定completion恢复未覆盖量化学生自生前缀 → 可采样的block-wise QAT初始化后，用量化policy生成prefix、冻结同架构FP teacher在这些prefix上给sampled reverse-KL correction → 重新选择低位行为恢复的访问人口与监督，而非只比较固定语料重构。评分2+2+2=6；标准必要Source完成，Books拟有限已有覆盖，评分/准入不受NoChange影响。

实际HTML §3–5（61–124）完整方法Eq1–4、setup、Table1和Scope；§1–2（45–60）只核问题/借用机制边界，无附录库存，未读references链接/code/复现。Stage1在各块分别传递FP/quant input streams，更新master/scales/zero-points/RMSNorm（STE）；Stage2 teacher和zero-points冻结、student与scales的训练身份不能因此等同部署INT2/3 kernel。按学生采样token构造detached logstudent−logteacher，再乘student logprob，是局部sampled correction；这里不授整条trajectory occupancy/长度的完整unbiased梯度保证，也不补实现。

关键配置：Qwen3-1.7B thinking，W3A16/W2A16，group128非对称，activation/embedding/head仍float。Stage1 4096×2048，OpenThoughts80%/FineWeb20%，每块两epoch/batch2；各同位宽恢复起点相同。Stage2 Online采32757 OpenThoughts prompts、temperature.6、总长≤8192/EOS、loss仅response；8GPU有效batch64但型号/HW、运行revision、evaluator细节/推理采样限制、多seed与完整wallclock为Not Disclosed。W3 Online40steps vs ReasoningQAT512；W2 30warmup+120 vs1536；目标同时改prefix、RKL vs top20 FKL及去supervised term，不从少steps或平均数认同预算/独立因果/更高效率。

Table1独立反侧：W3平均57.28高于54.38，但IFEval59.5<60.3；W2平均32.52 vs32.08且MATH36<37.8、IFEval32.49<33.8、LCB4.83<5.3；均仍低于原BF16平均67.17。One model、无多seed/离线RKL control；Scope121作者明确上述混杂，不能将当前访问人口的局部收益当全部能力保持、真实teacher真值或生产发布。初始化/QAT、master训练状态、学生rollout、teacher前向与独立长生成/任务和实际kernel验收全计费。

唯一owner `INFER-TENSORRT-LLM`：[Ch49](../../../../../books/part-05-inference-system/49-tensorrt-llm.md)，有限 No Change—已有覆盖通过。Actual1041–1061完整execution→float/lowbitprobe→低位on-policy恢复→postquantization标题：1055明确先可采样lowbit、量化forward产生rollout、冻结FP teacher在同studentprefix指导、master更新≠BF16 rollout与teacher非真值；1057实际已有起点/预算非同费用、teacher/verifier混杂、局部反退、初始化/rollout/teacher/回归全费与QAD/PTQ/高精度退路。Ch29 actual697–720通用访问人口/teacher snapshot/成本与350–365同prefix RKL监督交接；Ch48/50开篇已读。拟采用的长期责任链已具体承载，不因本篇无verifier或使用sampled RKL新建第二owner；具体40/150步、两阶段量化参数与Eq3/4配方只保Report，不声称现书逐字已有此recipe。review_mar11_continue已非作者实际必要Source及owner校准通过，root接受该有限NC；未写Books、不需新POST，不授DAY。

## 其余普通可执行停点

前三模型停点：10395/10381实际整合POST通过，09346有限已有覆盖通过；有效结果复用，不重审。

## 2610.09877 — 局部扰动表与全模型误差必须分责

[官方PDF](https://arxiv.org/pdf/2610.09877)实际header为2610.09877v1，[精确身份页](https://arxiv.org/abs/2610.09877v1)只有v1且无撤回；精确HTML不可用、v1 PDF入口超时后官方current PDF恢复，身份不变。公开日2026-10-08复用官方LG Oct8#401独核。组合精度搜索昂贵/受坏校准扰动→区分前层传播与本层量化扰动，将FP参考输入下每个block/bit的局部扰动整理为mean+dispersion表、按增分/节省weight bits贪心降精度→重选局部校准与跨预算分配，不授solver-free全局最优。评分2+1+2=5；标准必要Source完成，具体可复用校准表/下游验收接口差额深入，评分不随Books决定改变。

实际PDF §3–7（117–614）包括Eq1–17/Alg1、T1–3/方法/主要评价；intro0–117只核问题。B1/B2/B3/B4（1485–1593）必要配置、CI、相同candidate反侧和时间；B7（1864–1894）diffusion人口/度量权限。未读全A证明、全部B曲线/pixels/code；必要方法页5/6截图入口内部失败，公式只按可读文本核，不声称完整图像或可执行实现验证。

Eq1先把线性层误差拆成W乘前层Δ和(W−W′)乘量化前态；理论fixed allocation的Cantelli/global及layerwise界依赖真正分布矩、条件协方差、有界输入和指定失效预算，不把有限校准估计授成证书。实际local Pg,b以FP输入而非当前量化S′计算，忽略传播只在作者所说沿greedy路径误差足够小时近似；sample mean+std/sqrt(δscore)中的δscore是dispersion权重，不是数据选择后的confidence。每candidate仍有局部矩阵求值，单FP pass不等免费；固定table可随memory预算复用，需绑定输入人口、backend、block和bit候选。Alg1从最高候选bit出发，以非负score增量/所省weight bits降一block，tie deterministic；不是联合quantile最优或所有kernel可实现的HBM预算。

DRUNet32.64M/64conv/36blocks，CelebA256²、输入Gaussianσ=.1；三calibration seeds各256、固定100test图片，activations FP32。RTN对照per-channel symmetric，CLADO只{3,4,8}、主方案3–8；AIMET另TFEnhanced{4,6,8}，不混为统一pipeline。T1 clean ours34.401<CLADO34.409，CI[-.015,-.001]；共同candidate T7 B3.5 32.9967<34.1012、B5 34.5139<34.5776，不能声称无质量代价。T2 B6 realized5.984 vs5.716并非同预算实际字节。只有calibration输入受p.5共RGBmask/p.9独立mask，test不变；T8共同candidate仍有对应stress增益，但不授自然OOD或所有坏校准鲁棒。CI先对每图平均三校准差再按100图估计，B1明确不覆盖新calibration集合。

B4选择时间含score/allocation、warmup后三runmedian，排除load/data preparation/quantization application/PSNR；A100PCIe40GB一张、CLADO两张，不能从28–2570倍认服务吞吐。24.32秒是记录阶段时间加总、三seedmedian，不沿用摘要“estimated”作实测全生命周期。Diffusion B7 CompVisCelebA-HQ256²，5120 timestep-latent校准、48blocks/123tensors、W3–8平均3.9932/A32；DDIM200/η0、50000输出、torch-fidelity.3.0。与Q-Diffusion分别重构故非score-only；历史noise全量同一性未能核、只1000FP32直接check，PSNR to FP32不等真实样本质量/FID。FID20.853仍高于FP32 20.807。完整校准/candidate选择、重构、artifact/layout、实际backend及独立任务质量全部计费；嵌入式mixedbit实现§7仍futurework，不授真实部署/seed通用保证。

唯一owner `INFER-TENSORRT-LLM` Ch49。Actual931–985完整校准链（ProbeQuant孤立/传播/完整质量三分测与greedy不授最优已承载）、1335–1341 Waterfilling完整局部；Ch48/50开篇实际只交接。窄差额是可复用block×bit局部扰动table与按memory预算降精度的接口，非再复述sensitivity主题。root接手非作者必要Source/actual owner/PRE并通过（不是reviewer再次重复）；root授单段与本人注窄锁后，作者已写new1341/own2328，实际1328–1352完整邻接顺读及限定diffcheck通过。root非writer实际1328–1353完整SchurReplay→Waterfilling→新1341→conditional及本人2328注回对必要原证/PRE，actualPOST通过，窄锁释放；本项实际整合完成，不授DAY、artifact核验或复现。四模型最终为10395/10381/09877三项实际整合、09346一项有限已有覆盖，普通Source/Books待办0。

逐字PRE：精度分配也可以先固定一张可复用的局部扰动表，而不反复求整个组合的联合损失：在全精度参考输入上，对每个 block 和候选 bit 计算权重量化扰动，按校准均值与离散程度形成 score；从高精度配置出发，以增分相对节省 weight bits 的代价逐步降精度，memory 预算变化时复用同一表。这里隔离了本层扰动，并没有重放前层量化后的真实输入或完整误差传播；dispersion 权重不是所选配置的置信度，贪心也不签联合最优。[Layerwise Error Attribution 的受限对照](https://arxiv.org/pdf/2610.09877v1)支持比较这一离线接口，但低预算 clean quality 仍退步，指定 calibration mask 的稳定性不证明任意分布漂移下的鲁棒。参考人口、block、quantizer、候选位宽、权重计数与预算须一起保存，实际 artifact 还要加入 metadata/layout 并单独验 held-out 质量与目标 kernel。全部候选扰动、统计与分配、重构、物理格式和独立 runtime 都计费，局部 selection 时间不能代全链成本；误差传播、质量或 backend 失配时，保留代表性校准、联合/下游敏感度、uniform 或局部高精度路径，不由 solver-free 名称批准发布。<!-- source-family:SF-2026-ARXIV-2610-09877 -->
