# 2026-05-15 增量来源补查

作者：`/root/may15_supp_author`；独立复核：`/root/may15_supp_reader`。本次仅补北京时间 2026-05-14 完整自然日；原小时窗口、95 原候选整行、日期、评分及有效原证不迁不覆。不扩 Live、Weekly、2025 或邻日研究。

## A1 — 真实起点与入口

已本日完整加载 AGENTS、RESEARCH_CONTRACT、REPORT_CONTRACTS V3、统一 Prompt、Sources 使用/每日/主题/恢复、ROADMAP 与 Learning State 当前路由。原报告本地检查时为完成态，但这只描述此前工作，不代替补查验收。运行前完整 README 已保存为 [基线](SUP_BASELINE_20261019.md)（203513 字符）；旧有效层身份、精确版本与采用命题不变时复用，不重研原池。

2026-10-19 04:20～04:25 BJT：官方 arXiv 两个日期列表 `https://arxiv.org/list/cs.AI/2026-05-14?show=2000`、`cs.CL` 对应入口均返回 Cache miss；这是两个入口受阻，尚不等价于历史来源不可恢复。DataCite registered 日期切片及标题主题查询成功，170 项只作有界发现线索，未逐项进入题摘或全文队列。精确查询、日期原字段和实际停止点保存在 [标题切片](SUP_DISCOVERY_TITLES_20261019.json)，`meta.total=170,totalPages=1,page=1`；无 next。

主题：language/foundation model、Transformer/attention、token、Agent、diffusion/world model、VLA/vision-language、RL、GPU/inference、pre/post-training、multimodal、quantization/long-context/MoE。标题检索不等于语义准入；检索可能遗漏未使用这些词的新机制，后续仍需主题补检。宽元数据响应一次触发工具400k字符截断，未保存/采用为完整原件；已改为只取发现必要字段，未将截断当完整证据。

精确身份定点去重：170 条线索中52个ID已在 05-14 的既有有效报告出现；仅核本批具名 ID，不借其候选池反推本日。原归属与既有审阅不迁移、不重复评分；该列表不证明全球首公开或本日覆盖。新线索只有贡献明确后才恢复完整题摘及日期/current 证据。

## A2 — 当前待办

首批完整题摘与代表性排除准入校准；其后精确 Source、日期/current、Books 必要对读；每日机构来源与主题补检；六节归并、限定校验、独立 DAY/保存完成态/FINAL。当前全部仍普通待办，无新增候选或来源完成声明。

### 入口增量

补LLM/VLA/reasoning、kernel/compiler/communication/scheduling、retrieval/RAG/memory/embedding/tokenizer、optimization/alignment/distillation/sparsity/MoE/serving等同义主题：[第二标题切片](SUP_DISCOVERY_EXTRA_TITLES_20261019.json) `total186/page1/totalPages1`，与首切片合并318身份线索；具名ID在05-14既有报告精确去重94，不迁移其既有日期/评分，不借候选池反推本日。主题误命中的pure math/医疗/5G/一般网络与AIforScience不进入题摘全文队列；这些318不是当日确定论文或待逐项关闭队列。第一批完整精确v1题摘实际取得8项（下列A6），其余12次curl在10秒时返回running会话、随后具体12957单次重试30秒timeout；未取回不能写已读/零命中，将按必要域继续替代入口恢复。批量响应仅有身份/error边界见[题摘批1](SUP_ABSTRACT_BATCH1_20261019.json)，error空值代表未收回会话而非官方无摘要。

## A3 — 首批准入提案（待独核）

下列均实际读取精确 v1 官方完整题摘，保存 `SUP_ABS_<id>v1_20261019.html`；DataCite 当前元数据另保 `SUP_DC_<id>_20261019.json`，不拿后版摘要替代 v1。Gaze 的 v1 标题与当前元数据不同，本文以 v1 为准。四项 v1 Submitted 都在 2026-05-13 18:00Z 截止前（12597是2026-05-12 18:00:02Z、即纽约cutoff后2秒）；按公告日程最早界均为 May14 00:00Z/08:00BJT，DataCite 精确DOI/arxiv.content/findable registered最晚界分别 02:24:05/02:31:47/02:41:24/02:12:27Z，整区间同May14 BJT；原字段未改称实际发布时间。后版存在本身不说明重要修订，后续轻量current检查只处理已见具体纠错/撤回信号。

| 身份/精确题摘 | 拟准入的具体变化 | 暂定评分/owner |
| --- | --- | --- |
| [2605.13080v1 Learning to See What You Need: Gaze Attention for Multimodal Large Language Models](https://arxiv.org/abs/2605.13080v1) | 提前压缩/丢弃视觉KV可能丢失未来query需要细节 → 每解码步按query重选空间region且加learned global context tokens → 重考虑一次性不可逆eviction与按步可逆稀疏读取的设计取舍；不把90%少参与attention误称90%存储节省。 | 2+2+3=7；MULTIMODAL-REPRESENTATION/INFER-KV-CACHE待actual owner对读 |
| [2605.13403v1 RotVLA](https://arxiv.org/abs/2605.13403v1) | 离散latent action可退化为帧重建且缺动作组合结构 → SO(n)连续旋转表示、triplet temporal约束和latent/robot joint denoising → 重考虑跨embodiment预训练latent action如何保连续/组合而不把latent planner视真实动作权限。 | 2+2+3=7；MULTIMODAL-EMBODIED-VLA |
| [2605.13810v1 Provable Quantization with Randomized Hadamard Transform](https://arxiv.org/abs/2605.13810v1) | dense随机旋转理论好但O(d²)，单HD的离散结构使现有保证弱 → HD后加随机scalar dither可证明unbiased与uniform高rate MSE渐近 → 重考虑便宜结构旋转的量化证据，不能直接外推LLM质量或低bit全部范围。 | 2+1+3=6；INFER-TENSORRT-LLM；理论假设必须核 |
| [2605.12597v1 The critical slowing down in diffusion models](https://arxiv.org/abs/2605.12597v1) | score模型即使架构包含精确解也可能有随相关长度增长的参数学习慢模 → Gaussian O(n)可解玩具中双层+local score将训练尺度从quadratic改log → 若论证成立，修正表达容量足以判断训练可行性的解释。其直接研究diffusion训练/架构理论而非仅用AI提高物理任务指标，暂拟按主线理论准入，严格保Gaussian/极限边界。 | 2+1+3=6；MULTIMODAL-GENERATIVE-PARADIGMS/TRAIN-PRETRAINING待对读 |

代表性排除：[2605.13507v1 Efficient Implementation of an Adaptive Transformer Accelerator for Massive MIMO Outdoor Localization](https://arxiv.org/abs/2605.13507v1)。已读完整精确题摘；贡献针对5G beam-delay propagation sparsity与特定定位模型FPGA realization，row skipping、mixed stationary dataflow和filtered router收益依赖该信号结构。未建立大模型计算/基础模型训练推理的直接机制关系，不因其使用Transformer/加速器就准入；不追不影响排除的公开日期。另[2605.13312](https://arxiv.org/abs/2605.13312)题名明确脑网络分析应用、[2605.13618](https://arxiv.org/abs/2605.13618)材料信息学Agent属暂停AI for Science，仅作范围排除；未读题摘，不冒贡献裁决。

## A4 — 13810 必要 Source 与逐字 PRE 提案

四项首批准入及代表排除已 reader R2 通过。13810 维持2+1+3=6；已实际读 v1 §1.1/Th1.1–1.2、§2 Alg1/Th2.2、§3 central/tail证明结构、A.3 Eq5/LemmaA.8–9/Alg5与§4 residual成本，reader R3 对同必要采用域支持；不要求其余完整附录。2026-10-19 04:39BJT 轻量实际GET current `https://arxiv.org/abs/2605.13810`：仅v1提交历史、无Comments纠错/撤回；不遍历全站/虚构无标记证明。理论不是GPU实验，hardware/precision/batch/concurrency/SLO/evaluator不适用；无代码、无复现声明。

唯一owner `INFER-TENSORRT-LLM`，现Ch49 Rotation Scope段实际完整前后对读：06014讨论固定scalar两次/固定block三次变换的统计保证，新项改dither/codebook可单HD，是替代条件分支，不否定原定理。拟在 `<!-- semantic-body-binding:SF-2026-ARXIV-2605-06014 -->` 后、`共享 scale 还使误差不只属于 outlier 本身` 前插入下列唯一自然段与本人Review note；未获root窄写前不写Books。Ch48 speculation目标分布与Ch50执行runtime的相邻交接已读，不把vector期望界外推为原分布精确。

拟正文（逐字）：

变换次数也可以通过改变 scalar quantizer 的假设来交换，而不只是继续叠加 rotation：一次随机符号 Hadamard 后，在高斯密度三次方根所定义的分位坐标中移动量化网格，再用满足“桶内平均还原原值”的重构函数，能同时控制离散变换下的期望误差与偏差。普通 midpoint 重构的 dither 版本仍略有偏差，不能把随机 offset 本身当无偏证明。[受限理论](https://arxiv.org/html/2605.13810v1#S2)的无偏版本还改变网格端点与重构规则；其 MSE 常数匹配 dense 随机旋转，是单位向量、位宽趋大且对维度统一的渐近结论，不认证常用低 bit 的模型质量。范数保存、维度 padding、随机状态、码本构建与变换都付费，内积误差界还需额外 residual 量化与 bits；这些成本和定理条件应一并进入 Numeric Plan。低位宽、目标 attention 质量或实际执行收益未验时，保留原 quantizer、多次变换或较高精度，不由单次变换的理论复杂度签发 Serving 加速。<!-- source-family:SF-2026-ARXIV-2605-13810 -->

拟本人 Review note（逐字）：

- `SF-2026-ARXIV-2605-13810` — Daily2026-05-15补May14；[exact-v1](https://arxiv.org/html/2605.13810v1) §1.1/2/3/A.3/4必要域，2+1+3=6；仅采单HD与dither/codebook共同改变的条件分支，保Alg1偏差与Alg5无偏区别、高rate/单位向量期望界、residual额外bits及全费；不授常用低bit模型质量、代码复现或Serving加速。

13810 实际状态：root已协调单段+本人注窄位；作者严格按A4保存并self-read，reader R6实际非writer POST通过，本精确位生效释放。新增实际整合1，不授整日完成。

## A5 — Gaze / RotVLA 必要 Source 与逐字 PRE

Gaze 13080：实际必要采用域§3.1–3.5、§4.1/4.4 T3、AppA，reader R5支持。保留full visual KV、每head每query TopK、context tokens、progressive K而非把事前eviction改名；79.8%GPU缓存依赖CPU/SSD保存全KV，FlashAttention下2.6×dense walltime直接反侧。其T3 route/context0.19/0.15 GFLOPs另计，未补造生产batch/concurrency/SLO、量化精度或独立重复；13image/6video基准同架构/训练token匹配对照与外架构published results不混。2026-10-19 04:41BJT实际GET current仅见v1/v2历史、无Comments纠错/撤回，后版title不回填本日v1；不宣称完整版本语义比较。唯一owner Ch23固定预算视觉token节，现DSTP2604.12358已有anchor/reserve临时并集，但没有learned per-head spatial descriptors+global context+progressive训练分支；Ch45已有logical可寻址/physical驻留/按query读取与offload，不重复推导。Ch22/24相邻交接已读。

13080拟位：Ch23 `<!-- source-family:SF-2026-ARXIV-2604-12358 -->` 同段（以“同一回答中的视觉需求也可能随生成步骤改变”开头）之后、`同一个 selector 还可能在三个阶段看到不同信息`之前。拟唯一自然段（逐字）：

逐步重选也可以直接成为训练中的视觉读取接口，而不只在 decode 中触发临时回读：将保留的视觉 keys 按空间与时间网格分区，以均值 descriptor 供每个 head 的当前 query 选择少量 regions，未选区域仍可被后续 query 读取；另给每帧加入始终可读的 context tokens，补偿局部读取的全局信息损失。训练从 dense 逐渐收紧 TopK，避免尚未学会 query–descriptor 对齐时过早关闭通道；固定网格、均值摘要和小预算仍可能漏掉细对象或跨区关系。[Gaze Attention 的有限对照](https://arxiv.org/html/2605.13080v1#S3)支持这条训练/可见集合分支，不把选择当 grounding 真值；route、额外 context、完整编码与训练都计费。少参与 attention 的 KV 不等于少保存同样数量的状态，GPU 驻留减少还依赖 CPU/SSD offload；作者启用 FlashAttention 的墙钟时间反而是 dense 的2.6倍，不能用 FLOPs 或参与条数签发加速。表示预算与全局信息退化时，保留静态 selector、更大保留下限或 dense；[第45章](../part-05-inference-system/45-why-kv-cache-speeds-up.md)接手缓存驻留和读取成本。<!-- source-family:SF-2026-ARXIV-2605-13080 -->

拟本人注（逐字）：

- `SF-2026-ARXIV-2605-13080` — Daily2026-05-15补May14；[exact-v1](https://arxiv.org/html/2605.13080v1)§3/4.1/4.4 T3/AppA必要域，2+2+3=7。仅采per-query regions+global context/progressive训练；保fullKV/CPU-SSD offload、routing/context全费、fixed-grid漏失与FlashAttention下2.6×dense反侧，不授通用压缩率、净加速或grounding，未核artifact/复现。

RotVLA13403：实际读§3.1 Eqs4–12/§3.2/3.3、§4.1–4.5 T2–4、AppA，reader必要Source支持。gauge anchor来自identical-pair batch mean投影，不直接假定I；composition为z12 zI^-1 z01。T2 reconstruction-vs-repeat仅proxy、不证明无future leakage或唯一因果；T4 SOalone97.0 vsCont96.7 marginal、full98.2含额外triplet因素；LARY* human58.13<64.19、H20 latency79ms>61ms反侧保留。8H200/50h是作者pretraining范围，不代表全pipeline预算。§3.2 literal VLM pair-frame条件不能当线上未来可读，本次不采用完整部署recipe；joint mask只采训练接口分工。2026-10-19约04:40BJT实际GET current仅v1/v2历史无Comments纠错/撤回，不为无标记遍历所有版本。唯一ownerCh26，已读03340加性局部先验两段及完整邻接，拟作为非加性group composition替代分支，非覆盖旧加性/ordinary reconstruction；Ch25/27交接已读。

13403拟位：Ch26以“这是短时局部 motion 的训练先验”开头的03340第二段后、`无动作标签视频还可以分别预训练 forward 与 inverse 两种责任`前。拟唯一自然段（逐字）：

当局部加性不再合适，也可以先为 latent 指定非加性的组合结构：保留 soft codebook 的连续混合，将编码矩阵经 SVD 投影到 SO(n)，再用相同帧对估计并投影出 identity anchor；两段 transition 以第二段矩阵、anchor 的逆与第一段矩阵相乘，由起始帧重建两步后的观测。三元监督与单步重建共同约束组合，而不让“旋转”自动等于真实机器人坐标或无坍缩证明。[RotVLA 的有限消融](https://arxiv.org/html/2605.13403v1#S3)中，SO(n)单独仅有小幅差额，完整收益还混合 triplet 与预训练；重复使用 latent 的重建诊断也不直接证明已消除 future leakage。下游 joint denoising 可令 robot-action tokens 读取 latent，latent 不反读 robot tokens，这是条件接口，不把训练中的未来帧变成线上观测。SVD、码本、三帧重建、预训练和联合求解都付费，作者H20单步延迟还慢于所比基线；组合假设、真实动作质量或预算失配时，保留原加性短时先验、普通重建/原生动作监督与独立controller，不从组合代数签发跨本体执行或实时安全。<!-- source-family:SF-2026-ARXIV-2605-13403 -->

拟本人注（逐字）：

- `SF-2026-ARXIV-2605-13403` — Daily2026-05-15补May14；[exact-v1](https://arxiv.org/html/2605.13403v1)§3.1–3.3/4.1–4.5 T2–4/AppA必要域，2+2+3=7。仅采SoftVQ/SVD-SO(n)/zI-anchor非加性triplet与joint-mask分责，保proxy非无泄漏证明、SOalone边际差额、LARY*反退/H20 79>61ms及全费；不采pair-frame完整部署recipe、真实几何或执行保证，未核artifact/复现。

## A6 — 第二批完整题摘准入提案（必要Source未完成）

完整精确v1题摘及各提交历史在SUP_ABSTRACT_BATCH1_20261019.json，初始完整元数据日期字段在两个发现切片，个别current notices/comparison仍需定点核；不按后版metadata题摘。此批待准入复核及exact DOI/date权限补齐后计确定候选。

| 身份 | 旧约束→实际增量→改变的选择 | 拟分 |
| --- | --- | --- |
| 13536 HLS-Seek | HLS代码RL若每候选都真实综合很贵→comparative proxy判Pareto并MCdropout低置信切真实综合、在线更新proxy→重考虑便宜reward与真实综合闭环的gate，不能让proxy自证QoR。 | 2+2+2=6 |
| 13435 Q-Flow | flow-policy价值优化需backprop through solver而不稳→沿deterministic flow将terminal value传播到中间latent，以intermediate gradients免unroll→重考虑表达力/优化稳定取舍。 | 2+1+3=6 |
| 13527 MMSkills | text/code skill难以表达何种视觉state适用、直接截图易overanchor→state cards+multiview keyframes临时branch读后与live对齐、结构化guidance给main→改变可复用procedure证据与主context污染边界。 | 2+2+2=6 |
| 13175 Heavy tails | heavy-tail噪声似与heavy-tail目标匹配→两代表HT/LT diffusion模型sampling-error估计难度反证→重考虑尾部覆盖与score估计误差共同选择noise。 | 2+1+3=6 |
| 13517 ArcVQ-VAE | 有限codebook覆盖与利用率受限→time-dependent ball norm+angular-margin prior→重考虑范数/方向的codebook约束，不由更均匀分布自证下游生成。 | 2+1+2=5 |
| 13322 KamonBench | caption正确可能不恢复组合因子→已知grammar因子的programcode、受控pair-recombination/counterfactual sensitivity/probe→分开语义描述与compositional factor recovery评价。 | 2+1+2=5 |
| 13161 A3B2 | fewshot固定同训图文两支假定同重要→OOD image adaptation可损害，uncertainty-aware dampening异构adapter→重考虑支路适配资格而非一律更训image。 | 2+1+2=5 |
| 13833 QLAM | SSM加性/线性state限制全局交互→input-conditioned quantum circuit演进+query measurement→潜在不同memory representation替代分支；需核量子模拟、测量重复/制备成本，不由quantum名称授基本突破。 | 2+1+2=5 |

13080/13403实际状态：严格按root已授A5窄位保存，reader R8两个实际非writer POST通过，各精确位生效释放；新增实际整合现3，不授整日完成。

## A7 — 12597 必要理论与逐字 PRE

12597保持2+1+3=6，实际读II设定/III.2–3/IV.1–5/V.1–2/VI，reader同必要域支持。Gaussian O(n→∞)、translation invariant linear score与score matching population gradient flow；一层conv表达exact score不等好condition，GD稳定步长受协方差谱影响、critical L²；二层线性factorization的相同函数族可改善到log尺度，但一般初始mismatch需c²d0²=O(1)，不采用原文进一步“standard init自动满足”推论（尺寸幂口径局部不稳）。Full kernel每score O(N²)可能吃掉steps收益，local截断误差与noise time另核；d2采用R~logL并非通用常数局部。数值V实际3线性层4channels、每noise t独立模型、L16–128/4096data/20epochs，不说二层已端到端加速；硬件未披露、没有LLM/实际生成大模型迁移或生产SLO。2026-10-19约04:52BJT实际GET current仅v1–v3历史无Comments纠错/撤回，后版本不代精确v1。

唯一ownerCh24“反向核与训练状态分别约束哪些误差”，实际13470两段完整上下文承载kernel表达存在/terminal mismatch，但没有同函数族参数化造成score学习慢模；Ch28已有一般表达/优化可达性，不复制通用结论。拟在13470第二段后、`迭代误差还改变训练状态的支持范围`之前唯一自然段与本人注。逐字正文：

表达得出目标 score，也不保证当前参数化容易把它学出来。一个可解的 Gaussian O(n→∞) 分支中，一层线性卷积已经能表达精确 score，临界附近的协方差谱仍限制梯度下降的稳定步长，使有效学习时间随系统尺度二次增长；把同一线性函数写成两层乘积，可在声明的小幅 Fourier-mode 初始化与层间失配条件下改变学习动力，将这条尺度依赖改善为对数。[受限理论](https://arxiv.org/html/2605.12597v1#S4)并未增加函数表达族，说明 kernel 存在、优化轨迹与采样质量要分开验收；不能假定标准初始化自动满足条件，也不能把双层结论外推到任意深度。全范围卷积每次 score 的额外计算仍可能抵消少训练步数的收益；[后到修订的直接反侧](https://arxiv.org/html/2605.12597v3)还显示，局部截断的总 score 相对误差可控时，低频 modes 仍可能失真、临界分布行为仍会失败，故局部误差不是分布保真证书。两层求值、逐噪声时刻训练、截断诊断与完整反向积分都计费；非Gaussian、初始化或真实生成质量不满足条件时，保留原参数化、显式预条件/优化器与已验收 sampler，不把玩具模型的学习尺度推成大模型墙钟加速。<!-- source-family:SF-2026-ARXIV-2605-12597 -->

逐字本人note：

- `SF-2026-ARXIV-2605-12597` — Daily2026-05-15补May14；[exact-v1](https://arxiv.org/html/2605.12597v1)II/III.2–3/IV/V/VI，2+1+3=6；后到v3仅§IV.2–3/IV.5/AppC纠错域由reader实际核，保small Fourier-mode init、双层非任意深度及local总误差不保低频/临界分布；不计后日revision为May14新事件，不采v3 Fourier新结果或LLM墙钟加速，未核artifact/复现。

A7修正状态：reader实际current发现摘要local→Fourier实质变化，已定点承担v3§IV.2–3/IV.5/AppC对读；不双份恢复。v3明确small init条件、>2层balancedcase可重现power慢模、local总score误差不保low-k/critical，故本次该受影响域深入。上方旧v1 local讨论只保历史证据，不作为当前正面结论；逐字稿已收窄并纳入已见反侧，待修后PRE。容量恢复后已按本日重读适用AGENTS/Research/Report/Prompt/Sources和当前路由，原有效3项POST不重做。

## A8 — 有界题摘第三批（准入提案/代表排除）

[批3](SUP_ABSTRACT_BATCH3_20261019.json)的前15完整题摘已实际读取（包括空抽取后改为任意id前缀的class匹配）；后15长请求有running，实际poll结果保[有限恢复](SUP_ABSTRACT_BATCH3_RECOVERY_20261019.json)。其中13328/13321/13173收到完整abstract闭合后正文timeout，完整题摘可用、不能声称全文完成；其余12无数据需后续替代入口，不将批列表变必须逐项全文的队列。不再在请求尚running时开启后批以免实际并发扩大；技术失败不作贡献排除。本批确定准入仍待reader校准/权限日期/current。

| 身份 | 实际题摘可支持的准入变化 | 拟分 |
| --- | --- | --- |
|12957 GTA|appearance先行易几何不一致→专门geometry视频diffusion先出新view结构再条件appearance，训练latent shuffle处理跨view一致→重考虑3D生成的几何/外观责任与级联误差。|2+2+2=6|
|13178 LiteLVLM|CLIP高相似排序常被当相关→referent像素反而低similarity，反排名+恢复context→重考虑理解selector对pixelgrounding的迁移。|2+1+3=6|
|12960 DiM3|跨语言多模态重训昂贵、两residual功能不等→逐参数方向/幅度感知合并且保vision/projector→重考虑异质update冲突与无训练能力融合边界。|2+2+2=6|
|13815 OmniLiDAR|不同sensor/domain独立generator→共享range-image、azimuth/elevation方向建模与domain feature scaling→重考虑跨传感条件统一生成的表示/调制条件。|2+1+2=5|
|13740 Pinductor|仅obs/action学POMDP交互昂贵且部分方法读取隐藏state→LLM提候选POMDP、belief-based likelihood迭代→重考虑prior/观测证据/隐state资格的worldmodel学习。|2+2+2=6|
|13651 NAACA|长音频背景淹没rare event、反复ALM调用→oscillatory working state能量变化门控后级ALM→重考虑salience-filter/state与语义推理调用分责。|2+1+2=5|
|13641 RDPO|mixed reward幅度与维度相关扭曲scalar advantage→prompt-level quantile magnitude normalization再active-subspace Mahalanobis whitening→重考虑reward聚合前尺度/相关性处理。|2+2+2=6|
|13586 HetScene|同质joint layout难处理dense/support依赖→primary结构先生成、secondary以support anchors+local modulation条件生成→重考虑global layout/local support两阶段factorization。|2+1+2=5|
|13554 CPPO|CRL常offpolicy/replay且连续动作→contrastive Q直接导onpolicy PPO advantage、无需手工reward/replay→重考虑selfsupervised目标进入PPO的策略/critic接口。|2+1+3=6|
|13436 BPE dropout|只finetune随机分词可能造成pretrain分布不匹配→跨pretrain/finetune/data-budget负面对照与形态边界诊断→重考虑随机segmentation的阶段一致性。|2+1+2=5|
|13399 Diffusion Encoder|用diffusion encoder时decoder压力方向相反、reparam训练难联训→EM启发交替训练传递latent监督→重考虑复杂posterior与decoder同步。|2+1+3=6|
|13375 GRIP-VLM|连续relaxation近似discrete prune受aggressive预算限制→SFTwarmup+groupRL discrete selection与budget-aware scorer→重考虑固定预算/训练分支。|2+1+2=5|

代表排除（完整题摘已读）：13711 MILM仅围绕EHR classification/mortality预测的XML三元序列与sampling-pattern两阶段适配，未建立基础模型/系统主线机制或非医疗评价边界，按暂停/领域预测关闭，不再追日期；13667 SceneGraphVLM将TOON序列化、SFT后常规coverage/unsupported relation reward及前图条件组合用于SGG，题摘没有新增训练/执行机制或足以修正原判断的证据，具体格式与任务速度数字本身不准入；13173 OxyEcomBench扩大电商角色/任务/中英图文与难度层，题摘只报告领域知识差距，未提出主线评价盲区的可归因证据，按领域benchmark关闭。13328 StereoNav/13321 HCSG导航与13496 MARLIN尚需一次定点core辨别可迁移机制/仅模块组合，未判拒绝或候选；不因摘要没实验细节而排除。其余12未取题摘保线索，不冒已判。

## A9 — 最新恢复/来源与单项必要域

2026-10-19 05:25BJT：reader R14第三批12准入/3代表排除通过，日期/current/必要Source仍待；R12实际八份DC permissions/date组合与官方v1history通过，A6八项可作为确定本日候选，必要Source仍未完成。12597修后正文/本人注获root唯一窄位、作者保存self-read，reader R15真实POST通过，新增实际整合4；不授DAY。

机构实际入口：Qwen canonical `https://qwen.ai/api/v2/article/retrieval?type=qwen_ai&language=en-US`响应4503654bytes、40篇，metadata投影保存SUP_SOURCE_qwen_20261019.json；本日实读date/title/path全集后，May14无条目，邻接Apr30/May19；仅当前集合，不能证明历史没有删除/隐去。Hunyuan research技术API POST publicList pageNum1/pageSize1000/renderType0/lang=en，实际total9，元数据保存SUP_SOURCE_hunyuan；日期displayPublishTime/publishedAt/createdAt各保原字段，不把catalog当不可变历史，中文补段仍待。Seed论文API count20/page_token0实际18items（pinned有影响）、next20/has_more/total246，最早非pinned仍May26，未到May14，不能说覆盖；原投影错误按content字段名过滤导致丢title字段，只能用外链/日期续页，待下一页保ArticleContent标题。原始metadata角色均有限，现不签机构源完成。

OpenAI本日真实搜索发现并读官方Safety Summaries核心，实际RSS pubDate Thu14May2026 00:00GMT（BJT08:00），精确URL于05-14既有有效报告已深入：本次同事件去重，不重复评分/Books；不扩读邻日其他材料。MobileCodex/Sea访谈为产品/采用消息，搜索仅发现不自动收入；Anthropic leadership场景17:06Z是May15BJT，明确窗外不迁入本日。

Q-Flow13435作者必要层：v1§3/4 Eqs7–10/Alg1/4.3、§5 Table1/2及G限制。Inner flow确定、无runningreward、discount1，value=outerQ(s,terminalmap)。Intermediate x采dataset straight path，只省采状态的完整初始rollout；target仍从x forward求terminal再给outer targetQ，免BPTT不等免solver。Policy用CFM target加inner-value gradient，经sg回归velocity，outerQ与innerV两网分训；targetcritic减波动不解policy-flow movingtarget。OGBench std8seeds/advanced12，Table1 antsoccer56<60 IFQL、humanoidlarge8<11、cube-single95<96；平均54.4vs43.8只受测任务，nonlinearcritic/路径支持与movingtarget限制保留。C实现MLP4×512、Euler10/ensemble2等已定点读，不补造GPU/生产SLO或机器人部署，未核代码/复现。待reader有限Source与actualowner/逐字PRE。

13810因具体Books-gap已实际读A.3/理论关键反侧达到深入采用域，报告仅将标准最低投入规范为“深入完成”，不改6分、不重读有效Source/POST。V3当前有95条旧公开range与补窗date比较限制（原始范围跨May15但用户要求冻结），不改旧日期来取全绿；初次运行另发现补充heading带“补充”/短题名导致4条严格标题映射失败，已机械改精确同题同URL，原证块不动。后续限定原95冻结与新行检查分开，不冒称全V3通过。

13536 reader一次必要Source已实际完成v1§3.3/3.4/4.1–4.4 T2–4及v2相同gate/性能修订域：编译/testbench先gate，再pairwise mean胜率；仅1正确候选reward1。MCdropoutvariance高才触发真实Vitis并onlinebuffer更新；v1保证OOD/hacking措辞v2弱化为mitigate，不能采全检出/无hack。v1摘要81.5实际Forge，T2的HLS84.7已存在，v2修摘要；16→19kernel表变化不混用。T4同73h比较12500vs1460steps，含42hfallback，不授同steps/同质量8.5×净加速；fgnn更快伴FF/LUT变大、seidel/portfolio与GPT Pareto3:3反侧。作者复用这一次实际必要Source，不另取全正文。

Q-Flow反侧列修正：reader实际对Table1 header核得antsoccer56<60的60是FQL，IFQL是33；作者A9此前误写IFQL，现透明纠正，不改变准入/评分。reader已实际必要Source与Ch26完整GR-RL后邻接支持，当前仅ICML2026/v2历史无具体纠错信号，不重读整v2。

## A10 — HLS-Seek / Q-Flow 逐字 PRE

13536唯一owner TRAIN-GRPO Ch33 Verifiable Reward，实际完整读该节从verifier specification到heldout/adversarial原则及caption双向reward交接；Ch32/34相邻交接已读。拟在“Policy 会优化 verifier 可见的目标，因此必须保留 held-out tests、adversarial cases 和独立人工检查。”之后、caption段之前，唯一自然段＋本人注：

真实评价昂贵时，可以让 proxy 只学习候选间的相对质量，而不预测一个可被当真值的绝对分数：先通过编译与功能测试，再把同组候选的 pairwise 胜率均值交给策略更新；重复 dropout 前向的分歧较大时，才调用真实综合工具并把结果加入 proxy 更新缓冲。[HLS-Seek 的受限代码训练](https://arxiv.org/html/2605.13536v1)支持这种“便宜排序—有条件真实反馈”的分支，但低分歧不保证没有 OOD 或 reward hacking，后到修订也将原保证措辞收窄为缓解。Proxy 数据、重复前向、功能检查、真实工具回退与在线更新都计费；作者同墙钟比较包含不同训练步数及大量真实综合时间，不能把步数比当同质量净加速，局部延迟改善也可能伴资源增加。排序失校准、漏检或部署目标失配时，增加独立真实评价并保留较慢的真实 reward 路径，不让 proxy 给自身或生成代码签发正确性与 QoR 保证。<!-- source-family:SF-2026-ARXIV-2605-13536 -->

- `SF-2026-ARXIV-2605-13536` — Daily2026-05-15补May14；2+2+2=6，v1§3.3/3.4/4.1–4.4与v2同gate/结果修订域由reader一次实际读、作者复用。仅采relative proxy/variance触发真反馈；保低variance漏检、testbench支持/资源反退和73h不同steps/42h回退费用，不混Forge81.5/HLS84.7或v1/v2 kernel数，不授无hack、净8.5×或Serving硬件结论，未核artifact/复现。

13435唯一owner MULTIMODAL-EMBODIED-VLA Ch26，实际GR-RL两段995附近只训初始noise头与noise-spacecritic、不覆盖完整flow中间状态velocity更新。拟GR-RL第二段末family marker之后、domain-conditioned simreal2604.13645:start之前，唯一自然段＋本人注：

如果要更新 flow 的整条 velocity，而不只选择初始 noise，还可以为中间状态另学一份 value：固定环境 state 与当前确定性 flow，内层没有 running reward、discount 为1时，中间 value 可定义为沿该 flow 到终点后的 outer action-Q。训练从数据动作与噪声的直线路径取中间点，仍须向前求终点来构造 target，再以该 value 的局部梯度修正 flow-matching target，通过 stop-gradient 回归 velocity；免穿过 solver 反传，不等于免掉 solver。[Q-Flow 的有限离线/在线对照](https://arxiv.org/html/2605.13435v1#S4)支持这个更新接口，学得的内外 value 仍有估计与支持误差，policy 改变还使目标不断移动；target critic 只缓和波动，不提供稳定或单调改进证明。额外 value 网络、终点求值、flow steps 与全部训练均付费，复杂 action-chunk 任务仍有反退，模拟回报不授 VLA 迁移或物理安全。数据支持、价值梯度或总预算失配时，保留仅训初始 noise、原多步 policy、直接 BC 与独立 controller，而不让中间 value 替动作执行验收。<!-- source-family:SF-2026-ARXIV-2605-13435 -->

- `SF-2026-ARXIV-2605-13435` — Daily2026-05-15补May14；[exact-v1](https://arxiv.org/html/2605.13435v1)§3/4 Eqs7–10/Alg1/§5.2–5.5 T1–2/G必要，2+1+3=6。只采deterministic/zero-inner-reward/γ1下inner value与velocity更新，保免BPTT非免solver、两网movingtarget/动作维度反退与全费；OGBench std8/adv12seeds不混，不授稳定定理/通用VLA迁移或执行安全，未核代码/复现。

A10实际保存：root授两唯一窄位后，作者严格逐字保存、自读完整新增与直接两侧/本人注；限定两Books diff-check通过。reader实际POST尚待，不预计整合完成。

## A11 — MMSkills Source / 逐字 PRE 与 HeavyTails 反侧更正

13527作者实际v1§2.1–2.4/Eqs11–12、§3.1–3.5/T3/Fig3/5与AppC，reader同必要域/§5及current有限检查支持；当前v1–v3无具体纠错信号，不遍历后版。单独state cards/多视图、临时branch的对照支持可重用程序性视觉咨询；direct full注入有overanchor/context污染，branch并非自动安全隔离。Stage1按live/recent/textstate先选view可选零，Stage2结构化G是可错建议，由main决定当前动作，不把历史图坐标当当前grounding。主路径步数不含branch/view/额外calls；GUI20step预算/缺失未跑配置/生成错误与coverage不授净费或普遍迁移。唯一owner AGENT-CONTEXT Ch75，实读现04304 manager/worker两段与直接上下邻、Ch77 procedural检索两段及Ch84 skill contract/registry边界；检索/资产身份不重复写，只补当前视觉procedure的消费接口。拟04304第二段后→长视频段前一个自然段与本人注，未授不写。

逐字正文：

程序性视觉参考还可以先在临时 branch 中解释，而不把全部截图直接追加给主 Agent：将 skill 拆成带文字状态卡的多个视图，先根据 live observation、近期历史与状态卡选择必要参考图，再在局部窗口对齐当前状态，输出是否适用、子目标、建议计划、禁做事项与验证提示。主路径消费这份结构化 guidance，再决定本次动作；参考图不是当前界面的坐标真值，branch 也只是上下文分工，不自动构成权限或安全隔离。[MMSkills 的有限对照](https://arxiv.org/html/2605.13527v1)支持把“参考表达—当前对齐—主路径决策”分开，直接注入完整参考可能过度锚定，咨询本身也会误解状态、遗漏 coverage 或生成错误步骤。多视图、咨询调用、图像编码、技能构建与完整轨迹都计费，主路径少几步不等端到端更省；覆盖不足、grounding 或预算失配时，回读当前画面、保留纯文本 skill/直接 VLM 与独立结果核验，不让历史成功示例或流畅计划取得本次执行权。<!-- source-family:SF-2026-ARXIV-2605-13527 -->

逐字本人注：

- `SF-2026-ARXIV-2605-13527` — Daily2026-05-15补May14；[exact-v1](https://arxiv.org/html/2605.13527v1)§2/3/5/AppC必要域，2+2+2=6。仅采state-card/multiview选择与临时branch→结构化G的当前咨询接口；保错误grounding/覆盖/生成、main自主选择、GUI20step及缺跑配置/全费，不授分支安全隔离、历史图坐标、通用迁移或净费保证，未核artifact/复现。

13175作者已实际v1§2.1–2.3 Assumptions2.1–4/Th2.1–2、§3 Tables1–4/§4必要域。此前发reader的口头摘要误称Wildfires DLPM最佳TCE95/99，实际T4读回为DLPMα1.7最佳MMD-RBF0.083，GFLinear最佳TCE95/99、DDPM最佳TCE90，已即时纠正；不改分或隐藏反侧。DLPM所给bound训练/估计误差乘T且T依赖比DDPM更差，是各自假设/schedule下上界，不是任意heavy-tail必差或下界。v1 §2.1残留merge标记，reader正在恢复对应prose/currentv2有限域；其余附件不扩。

## A12 — HeavyTails 逐字 PRE

Reader已实际v1必要假设/定理/§3设定/T4/§4，v2§2.1 clean smoothing与Th2.1对应域；v1 merge标记只是排版残留，相关prose可恢复，不虚构材料受阻。拟唯一ownerCh24反向核/训练误差节，已保存12597段之后、迭代support段之前唯一自然段与本人注。旧13470存在性→12597同函数族学习动力→本项噪声尾部与估计误差不同责任→support转移，相邻完整局部实际读过；不重写Ch28一般统计。拟逐字正文：

目标有重尾，也不意味着把前向噪声换成重尾就更容易生成：噪声分布既改变终端初始化与反向过程，也改变需要估计的训练对象及其误差传播。一个[受限理论与实验分支](https://arxiv.org/html/2605.13175v1)分别在 polynomial-tail、光滑性与噪声 schedule 条件下分析轻尾和重尾模型；重尾方案在其终端 SNR 指数衰减假设下可更快压低初始化项，但训练近似/估计误差界含扩散 horizon T 因子，这里的 T 不直接等同部署 solver 步数。这是不同设定下的上界分解，不是所有重尾方法必差的统计下界。合成与表格数据对照中，整体分布距离和不同尾部阈值也会偏好不同 sampler，不能把更好的 bulk 指标改写成所有极端值更准。重尾目标的覆盖、score/反向对象学习、采样步数、schedule 调参与完整积分应共同计费；训练假设、尾部诊断或预算不满足时，保留轻尾基线、原 sampler 与独立 tail evaluation，而不凭“噪声匹配目标尾部”直接认证采样质量。<!-- source-family:SF-2026-ARXIV-2605-13175 -->

逐字本人注：

- `SF-2026-ARXIV-2605-13175` — Daily2026-05-15补May14；[exact-v1](https://arxiv.org/html/2605.13175v1)§2 Assumptions2.1–4/Th2.1–2.2、§3/T1–4/§4必要，2+1+3=6；reader另有限恢复v2§2.1排版及对应定理。仅采初始化/训练估计误差的噪声tail条件分解，保不同schedule/正则假设、非一般HT下界、Wildfires MMD与TCE分歧及全费，不授全tail胜出或大模型质量，未核代码/复现。

## A13 — 已生效8项 / QLAM 中心争议与新增来源实查

A10两项R20、13527 R23、13175 R29均由reader真实非writer完整新段/完整两侧/本人注POST通过，作者已严格已授窄位保存并self-read，新增实际Books整合累计8，全部这八窄位释放；不授DAY。批3十二exactDC原字段见SUP_DC_BATCH3_20261019.json，官方current histories见SUP_CURRENT_BATCH3_20261019.json；旧误指AB包含history已透明改正，readerR27实际十二逐项组合通过。当前新增确定24家族，必要Source/Books仍普通。

QLAM13833保持准入5分；作者与readerR26已实际v1 IV-B–D/Eqs7–16、V全实验/TableI/实现、VI与current仅v1。中心资格争议安全隔离：Eq13的αt,s右侧只有同一ψt与O(qt)，未给s如何改变读出，逐历史token权重/值接口未闭；n/电路深度/p/measurement m与实际参数/费用均未披露，PyTorch/PennyLane模拟、784/3072像素末状态分类及10fold小幅均值改善，不证明可寻址long memory或量子硬件/端到端效率。Unitary范数保持也不是信息可读或参数梯度稳定证明。本文不撤准入、不改分、不写Books，不据此授线性时间/指数存储优势；重开需可核电路/读出定义、测量及制备/模拟全费与匹配强基线评价，未核代码/复现。

有界官方列表恢复成功：`/list/cs.CL/2026-05?show=2000`（3300026bytes，月列表2000pairs）、cs.CV月列表2000pairs、cs.DC459pairs；只浏览围绕精确registered May14线索的ID12500–13850 band，分别71/125/19标题，保存SUP_LIST_TITLE_BAND_20261019.json。该band/月列表不是公开日期证书，也不是逐项题摘/全文队列；只按主线机制语义补查，具名未变有效事件作ID去重。API一次目标submitted切片+六主题响应542/首500，尚未完成尾42和必要标题投影；不把返回200或关键词命中签为覆盖。

Hunyuan实际header accept-language:zh恢复11条（原错误body language/lang仍en9不冒中文覆盖），元数据与全部原日期字段保存SUP_SOURCE_hunyuan_zh_header_20261019.json；本次按title/date实读11条，无May14目录条目，邻接Apr30 context/May21 Hy-MT2。一次未投影完整响应触发工具截断，未作为完整raw；已只保必要metadata，不取窗外content。en9/zh11只是当前集合，不保证历史无删除。

机构实际入口增量：DeepSeek主页→news研究索引10条，日期邻接Feb25/Jun24，news Apr24/Sep10，展开全部按钮未证全历史；Moonshot当前平台Blog26条只到2025、GitHub当前research/infra目录不含不可变历史窗；Zhipu研究首屏14条跨May20/Apr29，ERNIE Blog第一页10条从May9往2025、下一页在2025，无May14目录项；MiMo Paper8条跨Mar13/Jun29，Blog15条未标日期；MiniMax英文目录12条跨Mar18/May26、中文重定向minimax.cn仅壳、AgentTechBlog3条均Sep–Oct。上列具体有限当前目录已实际打开，未签历史全覆盖。域限定May14搜索实际只带来Meta WhatsApp商业采用与Instagram父母通知区域扩展、Anthropic融资/采用及May13 SMB tour等，均无本窗新增主线研究机制；搜索不能证明零遗漏，必要历史缺口继续限定。Google/Meta完整目标历史slice与Seed Blog仍待有限恢复，不以旧报告标签代新补窗。

## A14 — ArcVQ / Kamon 逐字 PRE

13517 v1§4 Eqs4–13/§5 T1–6/B/C/D.2–5/F必要域已作者实际读取，readerR30有限独核/actual Ch23通过。更正此前口头“current仅v1”：current实际v2 May27/ICML2026，无具体纠错信号，不全版本重读；B硬件single H10080GB已reader实核，不是2H100。唯一Ch23 stage3 codebook governance段后→VideoFlexTok12887前，拟唯一自然段与本人注，未授不写。

逐字正文：

有限码本的预算还可以通过训练中的几何约束使用，而不立即扩大 codebook：早期限制码向量范数，再随训练放宽球形上界；量化以归一化后的余弦相似选择 codes，额外 angular-margin 目标让每个 code 邻近的少量 latent 更贴近、其余更分离。该目标停止对 codebook 的直接梯度，只更新 encoder，原 VQ 目标再间接移动码本；这不是直接把全部 codes 推成均匀分布，也没有证明均匀最优。[ArcVQ 的有限对照](https://arxiv.org/html/2605.13517v1)支持这条训练接口，但 usage 较高不保证重建更好，部分同类配置仍反退；更多 tokens 与不同下游 prior 的结果也不能只归于码本约束。Top-k、范数与 loss schedules、额外比较/训练、下游 prior 和完整采样均付费，几何可视化不认证语义或 STE 梯度保证。重建、实际消费者质量或预算失配时，保留原 VQ、较弱固定约束与独立重建/生成验收，不由码本利用率自签通用表示或零成本。<!-- source-family:SF-2026-ARXIV-2605-13517 -->

- `SF-2026-ARXIV-2605-13517` — Daily2026-05-15补May14；[exact-v1](https://arxiv.org/html/2605.13517v1)§4/5/B/C/D.2–5/F必要，2+1+2=5/具体差额深入；readerR30实际Source/actual Ch23通过。只采norm-bound/cosine/encoder-only ArcLoss，保CIFAR与ImageNet16²相对CVQ反退、usage非质量、token预算/下游prior全费和semantic/STE未证，不授均匀最优或零费；current v2非本日新事件，未核实现/复现。

13322一次必要Source由readerR28实读，作者复用具体限定域，不重取正文；仅KDL code可直接拆factor指标，JP/EN不拆，heldout熟悉C/M的新配对非新词，separation非正确，probe可读非decoder使用，只有(C,M)实测重训，collapse修复改多因素。Actual Ch66 27340 rule-generation后→12665 witness前及完整直接邻接已双方读，Ch23只owns表示机制不重复。拟唯一自然段与本人注：

对可控生成的视觉组合，还可以把描述得像、因素取对与表示中可读分开：先由已知 grammar 生成图像及其 container、modifier、motif，再让模型输出可解析程序码，逐因素检查；留出熟悉因素的新配对，测重组而不是新词识别。配对改变一个因素时，输出发生变化仅说明响应分离，不保证变化正确；冻结表示上的 probe 能取回因素，也不表示生成路径实际使用了它。[KamonBench 的有限对照](https://arxiv.org/html/2605.13322v1)显示响应分离可同为满分而配对正确率不同，因而这些量不能互代。自然语言描述没有相同的直接 factor scorer，已发布其他 split 也不等都已重训验证；同时改正则、context 与checkpoint 选择的修复不唯一归因某个 mask。Grammar/scorer、合成与留出、probe/重训和完整调用均计费；生成规则不代表真实人口、因素无法可靠解析或预算不合算时，保留原任务准确率与人工原图核验，不把这组合成诊断签成通用 VLM 理解或内部解耦证明。<!-- source-family:SF-2026-ARXIV-2605-13322 -->

- `SF-2026-ARXIV-2605-13322` — Daily2026-05-15补May14；[exact-v1](https://arxiv.org/html/2605.13322v1)grammar/KDL、heldout(C,M)、paired sensitivity/probe及关键反侧由readerR28一次实际读、作者有限复用；2+1+2=5/具体评价差额深入。保程序码vs自然语言scorer权限、separation非正确/probe非使用、熟悉因素新配对、非全split已测和多因素修复；不授通用理解/解耦/零泄漏，未核实现/复现。

## A15 — RDPO / A3B2 逐字 PRE

13641 RDPO一次必要Source由readerR31实际读取（作者未重复恢复正文），actual Ch33/Ch31对读明确唯一Ch33 reward统计接口：现21743仅分桶尺度，尚无多reward分布形状与相关性白化。拟21743完整段后→08545效率资格段前单自然段＋本人注；作者实际完整两侧已读。逐字正文：

多 reward 混合还可以先处理分布形状，再处理维度相关，而不把不同量纲的 raw 分数直接相加：在每个 prompt 的候选差额上，用全局 IQR 尺度压缩并映到 CDF normal scores，再只在共同出现的 reward 子空间估计 EMA 协方差、白化后聚合并归一。[RDPO 的受限训练](https://arxiv.org/html/2605.13641v1)支持把尺度与相关性作为不同统计责任，却不使 decorrelation 等同独立、真值或原偏好方向不变；白化后的等权也重新定义了聚合方向。Ties、全相同分数、IQR为零、CDF端点和奇异协方差的数值保护仍须独立声明，不能照抄为闭合的通用 recipe。额外评分、分布估计、协方差状态、白化与完整 rollout/训练均付费，两步组合的部分任务反而低于单步处理或基线，不授普遍多目标改进。人口、数值或任务质量失配时，保留已校准单reward、固定尺度/权重与普通 GRPO，不让较高去相关统计量替最终质量验收。<!-- source-family:SF-2026-ARXIV-2605-13641 -->

- `SF-2026-ARXIV-2605-13641` — Daily2026-05-15补May14；[exact-v1](https://arxiv.org/html/2605.13641v1)reward gap/IQR/log-CDF、co-occurrence白化与T3/T4必要域由readerR31一次实际Source、作者有限复用，2+2+2=6/实际差额深入。保ties/IQR0/CDF端点/奇异矩阵保护未闭、decorrelation非独立、等权改变偏好与Creative/GPQA/FullStack反退和全费；不采完整数值recipe、Shannon信息解释或lowcost，未核实现/复现。

13161 A3B2作者实际v1§3.2 Eqs9–16/§4 T1–4/C/E与AppB直接反侧，readerR33同域及v2 AppB有限对应仍有相同错误步骤。更正初始“current仅v1?”未决为实际v2 May15 18:29:50Z/CommentsIJCAI2026，无具体纠错标记，不算May14新revision。UAAD是训练soft penalty而非线上gate，正文norm/B平方norm不混；非负正则梯度不推出总梯度范数下降，不采用其稳定理论。Actual Ch23 08942冻结双线性评分两段后→23353前补层内适配差额，唯一段＋本人注，作者已读完整邻接。逐字正文：

适配也可以进入 image/text encoder 的层内，而不只改最后的双线性评分；两支却未必应得到同样强的更新。在每层加入共享 down-projection、多个 up-projection 的残差 adapters 后，可以用预测不确定性加权 image adapter 输出范数的训练惩罚，并另约束专家负载；text 支路继续适配。这是对图像修正的软约束，不是线上检测 OOD 后硬关闭 adapter，更不会恢复完整原 CLIP。[A3B2 的有限少样本对照](https://arxiv.org/html/2605.13161v1)支持分别验两支更新的选择，但 confidence 不是域外真值，非负正则项也不推出总梯度范数必降。跨数据集平均差额很小、部分任务退步，额外 adapters/router与训练/推理还慢于某些对照；分支不对称不签发普遍 OOD 支配或免费适配。标签、置信代理、原任务质量或总预算失配时，保留冻结 encoder、text-only适配或原双线性评分，并独立验新旧域，不让软惩罚替消费者兼容性与真实质量签字。<!-- source-family:SF-2026-ARXIV-2605-13161 -->

- `SF-2026-ARXIV-2605-13161` — Daily2026-05-15补May14；[exact-v1](https://arxiv.org/html/2605.13161v1)§3.2/4/C/E与B必要反侧，readerR33另有限v2 B对应，2+1+2=5/具体差额深入。仅采训练image-output软惩罚/双支adapter责任，保非线上gate、confidence非OOD、B梯度推论不成立、T2边际差/Food101反退与A800费用；不授理论稳定/普遍支配或完整CLIP回退，未核实现/复现。

## A16 — 新增39资格 / BPE 逐字 PRE / 来源尾

ReaderR35/R36/R39已对原timeout恢复12完整题摘及3 once-core准入独核通过（DESBench额外核LLM/framework/合法action/fallback决定域，不因industrial标签排）。十五原字段在SUP_DC_RECOVERY15_20261019.json，十二完整v1题摘/history在SUP_ABSTRACT_RECOVERY12_20261019.json，另三official currenthistory在SUP_CURRENT_CORE3_20261019.json；readerR43逐项组合日期通过。最早v1 May12 19:57Z已过NY18Zcutoff，统一May14 00Z lower至registered上界02:34Z都同May14BJT；GAGPO六月Updated不改名首公开。当前确定新增39，必要Source/Books未全完成，不预计DAY。ArcVQ/Kamon R37/R38 actualPOST及A3B2 R44已生效，新增实际整合11；RDPO已授权保存、self-read/diff-check通过，待实际POST。

13436必要Source由readerR42一次实际读（作者有限复用），唯一Ch11现固定artifact句与04706编码/输出mask间具体gap，作者实际完整相邻离线构词两段/固定身份句/后mask段已读；Ch28 activationdropout不拥有segmentation identity。拟唯一自然段＋本人注，未授不写。逐字正文：

固定词表与 merge identity，并不要求训练中每次都走同一条切分路径：BPE dropout 可以在既有 merge graph 内随机跳过合并，让同一原文出现多个合法 subword 序列，而不重建词表或重分配整数 ID。应把这种随机性作为训练阶段的输入分布选择，分别验预训练与下游微调是否采用它；[受限低资源对照](https://arxiv.org/html/2605.13436v1)中，两阶段都用的组合通常更强，仅微调时加入反而可能弱于确定切分。部署仍可保确定编码，不能把训练时的多种分段当热换 tokenizer 的授权。固定 token 预算与长度截断下，切分改变也改变原文曝光；较高形态边界 F1、外部形态词表替换与下游质量是不同证据，不能唯一归因“更符合 morphology”。随机编码、预训练、微调重复与回归均付费，部分语言/任务仍反退；阶段、原文覆盖或消费者质量失配时，保留确定 BPE、较弱训练随机性及原 checkpoint，不由某个 dropout 比率批准通用大模型 recipe。<!-- source-family:SF-2026-ARXIV-2605-13436 -->

- `SF-2026-ARXIV-2605-13436` — Daily2026-05-15补May14；[exact-v1](https://arxiv.org/html/2605.13436v1)pretrain/finetune阶段对照、T2及morphology必要域由readerR42一次实际Source、作者有限复用；2+1+2=5/Ch11具体差额深入。保10seeds仅FT、maxlen128/token非matched raw exposure、5/10%选择非最优定理、Morph F1采样/外部词表分母及部分任务反退；不授形态唯一因果/通用LM recipe或部署换ID，未核实现/复现。

Seed Blog实际从官网所载main.d734eb08.js定点读出enum Publication=1/Blog=2与同get_article_list_v2 caller（不是猜type0）。实际type2 count20/page0响应21948bytes、12条/total116/next20/hasmore，metadata保SUP_SOURCE_seed_blog0_20261019.json；非pinned已跨Oct13→Apr22→Apr8/Apr1，May14无可见目录项后停止，不遍历116全历史。Pinned与当前目录筛选影响回忆，display PublishDate、ArticleID/UpdateTime各保角色，不证明不可变历史无遗漏。

## A17 — 有效层恢复 / Support-NW PRE / Diffusion Encoder 必要域

压缩恢复后重读AGENTS/适用合同、来源Daily/arxiv/恢复、Prompt、ROADMAP和最新相关路由；只接本日。R45 RDPO实际POST通过，累计12整合；BPE R47逐字PRE/root授位后作者按A16严格保存Ch11，自读完整新段/完整两侧/本人注、限定diff-check通过，实际POST仍待。原95不动，普通来源/Source与日级仍待。

13386 readerR46一次实际Source及actual Ch24对读有限复用，不另取同域。作者实际完整读现CFM路径/条件均值、08344进度、PAFM候选target段与Euler原段，差额是部署给定reference support形成经验field，而非重复训练target平均。拟唯一Ch24 PAFM完整段后→Euler原段前一个自然段＋本人注；逐字正文：

条件 support 也可以在部署时直接决定 velocity，而不只作为训练 target 的候选：在 Gaussian base、声明的 OT 条件路径与有限均匀经验支集下，将当前点按时间去缩放，以路径噪声确定 bandwidth，得到 Nadaraya–Watson 局部均值，再经仿射 post-map 才成为速度场；普通 learned Attention 的输出本身不自动等于它。[Support-conditioned flow 的受限分析](https://arxiv.org/html/2605.13386v1)只在 t>0 的这些条件下成立，终点仍是经验支集的 Gaussian KDE，不是任意真实目标分布。Kernel 集中、度量失配与 support 稀缺是不同压力，有效邻居少不必失败，较健康的邻居统计也可能生成失配；跨任务学习结构可以修正某些切片，却在留出任务反而远弱于直接 plug-in。Support 编码/驻留、距离读取、额外 head、跨任务训练与完整积分均计费，普通图像 adapter 中的权重相关也不证明 velocity 或质量等价。支集、几何或预算不满足时，保留直接 plug-in、原条件 FM 与独立生成验收，不让 Attention 形式、有效邻居数或 learned 标签签发分布保真。<!-- source-family:SF-2026-ARXIV-2605-13386 -->

- `SF-2026-ARXIV-2605-13386` — Daily2026-05-15补May14；[exact-v1](https://arxiv.org/html/2605.13386v1)§2–3/Props1–2/Th3、§4/T1、§5/7与D必要域由readerR46一次实际Source、作者有限复用；2+1+3=6/部署support经验field具体差额深入。保Gaussian/OT/finite uniform/t>0、NW后仿射、KDE非q、n_eff非质量及LOFO GMM反退，IP-adapter权重相关不授Th3/velocity等价；全部训练约350GPUh非单模型，未核实现/复现。

13399 The Diffusion Encoder作者实际读[exact-v1](https://arxiv.org/html/2605.13399v1)§3–6/Alg1/Eqs20/32、A.2与E.7必要配置；current仅v1/Comments篇幅，无具体纠错信号。后验最优q*正比Gaussian prior乘decoder likelihood的1/γ次方；encoder样本短Langevin改进后作为conditional denoising encoder与decoder重建的共同目标，避免完整逆扩散BPTT。Exact EM单调性须精确posterior/充分Mstep，实际10步/(-1,1)clip与decoder缓慢变化不认证精确后验或单调；simulation-free仅forward噪声训练采样，不是免encoder ODE、Langevin梯度或重建。Neural entropy是KL上界非实际rate/MI；同convdecoder的Gaussian VAE在实际RD曲线更好，表达族更广不保证已学更好。A.2明确串行Langevin每步付decoder梯度，JAX随n变化recompile可抵消少步收益；critical damping仅未来想法不作实现。E.7 nstep10/4latents-per-image/batch256或128/50epochs、1H200约15/45/325min分别绑定数据与维度，不当matched预算或通用加速。必要有限证据不扩全部附件，未核代码/复现。

Actual owner对读：Ch24开头RAE-AR两完整段与后2610.22060/17492说明表示被生成路径预测的压力，不拥有encoder近似posterior训练；Ch23连续表示完整起段、PQ两段、07104两阶段目标及rate-distortion起段已读，后者联合rate/重构/consumer容量但没有灵活posterior训练与有限EM/近似rate反侧。建议唯一MULTIMODAL-REPRESENTATION，连续表示起段后/PQ存储分支前一段，解释从Gaussian编码到conditional diffusion posterior的训练责任，不复制Ch24 sampler。待reader必要Source/actual owner有限独核后再PRE，不先写。

## A18 — Diffusion Encoder / DP-Muon 逐字 PRE 与 LiteLVLM 必要域

R48 BPE实际POST生效，累计13整合；13386 root授位后作者按A17逐字保存单段/本人注、完整自读新增和PAFM/Euler两侧、限定diff-check通过，actualPOST待。恢复十五日期/准入确定已并入当前表共新增39，旧95不动；未把Source/PRE通过先算整合。

13399 readerR51必要Source/actualowner通过。拟Ch23连续表示起段后→PQ前唯一自然段与本人注，逐字正文：

连续 latent 的 encoder 也可以输出比 Gaussian 更灵活的条件分布，但更宽的分布族先带来训练耦合，而不保证更好的 rate–distortion。一个替代分支让条件 diffusion encoder 采出 latent，再用 decoder 梯度与 prior drift 做短 Langevin 改进；同一批改进样本分别监督 encoder 去噪和 decoder 重建，避免穿过整条逆扩散路径反传。目标为 prior 乘 likelihood 的1/γ次方，γ=1才是通常 posterior；[Diffusion Encoder 的有限对照](https://arxiv.org/html/2605.13399v1)使用有限步、梯度 clipping 与变化中的 decoder，不能继承精确 E/M 步的单调性，也不能由保梯度符号证明采样平稳分布不变。图中同 decoder 的 Gaussian VAE 前沿更好，encoder 的 neural-entropy 上界又不是精确 rate，因而既不授灵活族胜出，也不从这个横轴证明精确码率支配。条件读图、encoder ODE、每步 decoder 梯度、重建与编译全计费，simulation-free 只指 forward-noise 训练取样；后验近似、重构或预算不合算时，保留 Gaussian VAE、普通连续 feature 与原 decoder，不让更宽表达族或稳定 loss 替实际表示质量验收。<!-- source-family:SF-2026-ARXIV-2605-13399 -->

- `SF-2026-ARXIV-2605-13399` — Daily2026-05-15补May14；[exact-v1](https://arxiv.org/html/2605.13399v1)§3–6/Alg1/Eqs20/32、A.2/E.7，2+1+3=6/灵活posterior训练具体差额深入，readerR51有限独核通过。保γ=1通常posterior、10步clip非平稳/EM单调保证、neuralentropy非exactrate、所画VAE反胜与Heun/Langevin/JIT费用；不授SOTA/通用RD支配或免采样，未核代码/复现。

12994 readerR50一次必要v1与后到v2受影响域，作者有限复用，不再取全文。作者实际读Ch28 FlashDP完整段、03425 filter完整段与独立binding、后01129两阶段裁剪完整段和22610前向clip段；新差额为非线性矩阵map的输出均值而非temporal filter二阶矩。拟唯一TRAIN-PRETRAINING Ch28 03425 binding后→01129前一段＋本人注；逐字正文：

私有梯度进入非线性矩阵 optimizer 后，还要区分输入噪声的零均值与更新输出的均值：momentum 经有限 Newton–Schulz map 近似正交化，可能产生有偏的输出扰动。一条[受限 DP-Muon 分支](https://arxiv.org/html/2605.12994v1)在冻结 clipped-gradient 路径与光滑性条件下，用额外对称 Gaussian probes 估计平滑差额，再校正领先偏差项；这不恢复无噪声梯度，也不是实际 adaptive history 上的无偏定理。[后到修订](https://arxiv.org/html/2605.12994v2)改用 global clipping、fresh-noise 条件分析与平滑 map，提示旧累积噪声方差不能直接冒充当前条件方差，但这些新结果不倒填首发。原 v1 同 lot 的多矩阵发布须联合会计，shuffled fixed-size 采样与 subsampling 近似也仍需独验；post-processing 只保已经有效的私有 release，不替原裁剪/采样/会计补证。J=1校正共三次矩阵 map，probe 方差、逐样本计算、参数分支及完整训练/调参都计费，较小输出偏差不保证更好 loss，所测任务仍有反退。光滑条件、隐私会计或效用不通过时，保留已验证 DP-SGD/DP-Adam与原显式路径，不由正交化或 bias correction 自签隐私与收敛。<!-- source-family:SF-2026-ARXIV-2605-12994 -->

- `SF-2026-ARXIV-2605-12994` — Daily2026-05-15补May14；[exact-v1](https://arxiv.org/html/2605.12994v1)§2–5/Alg1/Th2.1/D与v2必要受影响域由readerR50一次实际Source、作者有限复用，2+2+2=6/非线性output mean具体差额深入。保冻结路径/光滑性、v2只纠过推不计本日新理论、same-lot联合会计/采样近似、J1三次NS、生成指标反侧与全部费用，不授adaptive无偏/端到端privacy或普遍utility，未核实现/复现。

13178作者实际exact-v1 §3.1–5.6/T1–6、D.2/E.1–2必要反侧/current（v2Jun1/ICML，无具体纠错信号）。RefCOCO-val 576patch低EOS相似ref-region关联，gradient chain是省略QK依赖的近似、EOS→SOS attention0.68观察不识别唯一因果；不采“contrastive必然导致/低相似普遍grounding”。Selector低相似前景＋按CLS attention×Vnorm补context，多指代取候选intersection、单指代50%预算；保多个query额外textencoding/交集与单query固定比例。完整SAM encoder/pixel decoder仍读取dense image，不是所有视觉计算删除。T4 context-only63.3低于random65、低sim66.1到组合68.9，支持该两支责任；T1保192tokens68.2 vsdense75.5（90.3%非无损）。A10040GB T6 CUDA340.89→265.83ms但prefill166.25→74.88ms不同指标，activation .81→.35GB不是整模型显存；E.2实际CUDA16022→15904MB只有约118MB少量，4bit额外量化才大减，不归pruning。E.1后FT能回升不混training-free，D.2 SigLIP2无CLS/EOS时改proxy均值，不沿用CLIP token身份因果。更多seed/uncertainty/precision与服务SLO未披露，未核实现/复现。

Actual owner作者实读Ch23 22394全局vs局部masking段与25803传感器段、固定预算03072 projectedfeature/PMI完整段及上下02689/21701；已有“相似不等真值/评分接口”但无text/global投影反排名＋前景context分责/完整dense pixelconsumer这一具体反侧。建议唯一Ch23 03072完整段后→21701多轮复用前，作为当前query selector替代分支；待reader必要Source/actualowner独核再PRE。

## A19 — 16整合有效 / 三项逐字 PRE / 有界来源尾

R52 Support-NW、R57 DiffEncoder、R59 DPMuon均实际POST生效释放，新增16实际Books整合；QLAM1中心隔离、余22普通Source/Books，未DAY。容量故障不使有效证据失效；重读AGENTS/当前合同后仅同日续跑。13178 R55必要Source/actualowner已通过，额外明确E2偏context/SQA表128tokens而prose192、D2正文97.6/91.7%与T10 Avg82.3→75.7/63.4冲突，均不采用错比例。拟Ch23 03072完整段后→21701前唯一自然段＋本人注；逐字正文：

固定 query 下，图文相似度的排序方向也要由当前 consumer 验证，而不能默认越高越值得保留：全局图文投影对齐，不代表局部指代区域必与句末表示最相似。一条[受限 pixel-grounding 分支](https://arxiv.org/html/2605.13178v1)反而先保低相似 patch，再按 CLS attention 与 value norm 补回背景 context；前景读取和边界判别由两份预算承担。低相似与目标重叠只是该表示和人口中的关联，近似梯度链与 attention sink 不识别唯一因果，也不授权所有 encoder 普遍反排名；换无 CLS/EOS 的 encoder 又须另定义 sensor。进入语言路径的 tokens 少了，独立 dense SAM/pixel consumer 仍读完整图像，较好的剪枝结果也仍弱于完整输入。多 query 编码、排序/交集、context 恢复与完整视觉、语言和像素输出均计费，activation 的缩减不是模型全部 CUDA 显存同比缩减；问题或任务改变时重选并独立验 grounding，质量或净预算不合格时提高保留量、恢复原排名或 dense，而不由更低 FLOPs 批准细节无损。<!-- source-family:SF-2026-ARXIV-2605-13178 -->

- `SF-2026-ARXIV-2605-13178` — Daily2026-05-15补May14；[exact-v1](https://arxiv.org/html/2605.13178v1)§3–5/T1–6、D.2/E.1–2必要，2+1+3=6/低相似反侧具体差额深入，readerR55独核通过。保关联非因果、context-only弱于random、SAM dense/质量损失及全部费用；E2 token数/D2比例冲突不采，activation与CUDA显存分账，current v2只ICML无具体纠错信号，未核实现/复现。

13217 readerR53一次必要Source/actualowner复用；作者实际完整读Ch33无critic成本节/完整tradeoff式、后policy-implied两段，拟该式后→Policy-implied标题前唯一段＋本人注；逐字正文：

多步任务中，也可以把同 task 已采轨迹按声明的文本 state 聚组，用组内 discounted return 均值作非参数 value，再构造相邻 state 的 TD residual 与 GAE，而不为整条轨迹广播一个 episode offset。[GAGPO 的受限对照](https://arxiv.org/html/2605.13217v1)支持这种 return 复用，但相同文本不证明隐藏状态或策略可见 history 相同，均值又含本次样本自身，不是独立的精确 baseline。若整段所有 state 都是 singleton，均值就等于各自 Monte Carlo return，按其递推每个 TD residual 为零，不能照录成自动退回 MC 信号；只有当前一步 singleton 则未必如此。归一人口是同 task 的全部 steps，action 内 token ratio 的几何均值也不等整串概率的 importance ratio，不授无偏信用或硬 trust region。State key、组统计、全部 rollout/回报、递推与调参均计费，局部任务仍会反退；状态 alias、复访支持或预算不合格时，保留终局 group baseline、明确 state 监督或已校准 critic，不由省一份 value network 认证免费、稳定或真实因果贡献。<!-- source-family:SF-2026-ARXIV-2605-13217 -->

- `SF-2026-ARXIV-2605-13217` — Daily2026-05-15补May14；[exact-v1](https://arxiv.org/html/2605.13217v1)§2.2/3/4/6与A–C由readerR53一次实际Source、作者有限复用，2+2+2=6/非参数state baseline差额深入。保exacttext非Markov、含自身/全singleton整段零信号、task-step归一/几何ratio非jointIS、1.5B Heat反退与3seeds/160updates及非全matched前作，未核实现/复现。

12857 readerR58一次必要Source/actualowner复用；作者实际完整读Ch82共同错文档句、后Vend监督段与03053 verifier粒度段，拟该句后→Vend前唯一段＋本人注；逐字正文：

异构实现可以提供比互相复述更具体的诊断，但一致仍不是正确：同一规格分别生成 Verilog 与 Python reference，双方不看对方代码，通过有限随机 stimuli 比较 cycle 输出，把首个分歧转成结构反馈；下一轮只有 agreement 提高才接纳，否则回到上次版本。[ChipMATE 的受限运行](https://arxiv.org/html/2605.12857v1)使 rollback 的控制对象清楚，却只保这组测试的一致性，不保规格、时钟/位宽或未测输入正确，两个实现仍可能共享错解。部署无 golden 也不等训练无正确性来源：数据生成读取 golden Verilog，训练中的 local/correct-fix reward 还依赖额外正确性信号，pair reward 如何归约到各策略未闭合时不照抄完整联合训练 recipe。内部多候选、多 turn 与回退必须计入 system pass 的成本，不能把系统 pass1 当单次单 agent 前向；更多候选/轮数并非单调改善。数据/API、双方训练、仿真与全部修订都付费；共同错、测试支持或预算不合格时，回到可信 reference、形式验证与人工规格核验，不由 code-blind 或100% agreement 认证硬件安全及正确性。<!-- source-family:SF-2026-ARXIV-2605-12857 -->

- `SF-2026-ARXIV-2605-12857` — Daily2026-05-15补May14；[exact-v1](https://arxiv.org/html/2605.12857v1)§2.1–2.4/3.1–3.6/T1–2必要由readerR58一次实际Source、作者有限复用，2+2+2=6/异构互测rollback差额深入。保stimuli agreement非正确、部署无gold非训练无gold、XGRPO归约未闭、内部best3×3turn/重复估pass与API/训练全费及frontier反退，未核实现/复现。

API主题submitted切片已读完两页0/500共542个当前标题投影，保SUP_API_TITLE_PROJECTION_20261019.json；submitted不当publicdate，含后移ID与current版本，不按返回集合全题摘。只在本窗邻近ID band与主线语义上补标题盲区；13360/12978/13737/13485/13768/13095精确ID在05-14旧有效报告，同事件具名去重，不借其候选池。另16项可能机制定点取v1 AB，11成功5timeout，原件SUP_ABSTRACT_TAIL16_20261019.json，未读域不授完整恢复。12836 history有v2withdrawn须核当前撤回，不能入本日确定候选；13848 GraphBit仅DAG显式编排/typed函数/三memory tiers和数字，完整题摘未有新的执行语义或足以改主线的有归因边界，具体组合不足贡献，关闭且不追日期（其historyMar8也不搬May14）。其余待首批完整题摘校准/必要date，未增确定39或fullSource队列。

OpenAI release-notes May14核心已实际读：mobile连接host显示live approvals/screenshots/terminal/diffs/tests；access tokens准trusted noninteractive local scripts/schedulers/privateCI以workspaceidentity运行。此项不再简单按“产品”标签关闭，必要准入核心是非交互认证/连接状态是否有具体兼容性和权限变化，后续只核官方说明/日期资格，不扩全产品史。

12960 DiM3作者实际exact-v1 §3.1–3.3 Eqs1–17/§4/§5.1–5.4 T2–6、§6与AppB/C及T15/16必要反侧；current实际v2May20，官方abs无具体纠错/撤回标记、摘要关键机制未变，不据版本号全版对照。共同language base N、multilingual M、MM language V，visualencoder/projector保原；矩阵以column为单位分解norm与方向偏移，各source内部matrix-column rank归一、跨source softmax后两branch等权平均，再对base-relative residual凸组合；1D仅绝对偏移另分责。不写成逐scalar方向或整个非线性modelfunction凸混，也不把rank salience当真实语言/视觉语义重要性。DoRA式径向+角向残差分解是恒等式，不证明任务兼容或tSNE真实semantic因果；固定vision模块仍可因语言读出变化损grounding。

三sharedbackbone设置，57language总集合非每任务57，lm-eval/lmms-eval同设置，baseline经validation gridsearch，验证人口/搜索费不能免费；hardware/precision/重复seed与完整wallclock未充分披露。T2XNLI42.93<Emma43.64，T15CVQAZh47.80<原48.57/Pt53.52<57.39，T16SEED40.45<anchor40.97且MMStar低DARE，T6部分layer SEED42.03>full40.45，故不采“所有任务/保全能力”与“全部scope更差”。未新增endtoendjointtraining也仍付sourcepretraining/坐标核对、rank/softmax/模型读写、gridsearch与回归费；tSNE/silhouette只所测表示相关。架构/tokenizer不兼容时该共同参考残差未成立，C明确未解决；保independentexpert/原MM/真实多语配对训练，未核artifact/复现。

Actual作者完整读Ch23 21584 SSAM两段与后22823projector分片段，前14016projector/LoRA分责两段；旧SSAM根据激活二阶矩投共同子空间，新DiM3是language residual column径角rank与视觉接口保留，特定异质MM/多语源差额。Ch30 merge与dynamicadapter标题是资产策略而非本处模态接口，建议唯一Ch23 SSAM完整第二段后→22823前单段，待reader必要Source/actualowner独核再PRE。

## A20 — 尾部16完整题摘校准与日期限定

SUP_ABSTRACT_TAIL16中5次timeout已通过精确官方abs URL逐一真实恢复题摘/history（12951/12501/12622/12521/13307），仅本次web回读，不冒原JSON含恢复内容。其余11完整题摘作者已实际读，不按数量配额准入。12836 current明确整篇withdrawn，Comments称原欲replacement2602.16169、后续更新在那里：本ID不入选、不评分/Books，仅保撤回依据，不扩读另ID。GraphBit13848沿A19具体贡献排除。12501v1 May12 17:59:58Z早截止2秒、12521v1 Apr3 17:02:20Z，均须精确DC/公告合证；无法整区间定May14时资格隔离，不以ID月份/dateband搬日，不展开fullSource。12586仅已有crossday具体线索，同样隔离首公开资格、不评分，不需要正文。

下列十项完整v1题摘新增潜力明确，拟准入/评分待reader校准与date，尚不增39确定表、不预授Source：

|ID|具体潜力：旧约束→原文增量→需要重新考虑|拟评分|
|---|---|---|
|12928 Byte gap|移除subword与AR结构先验的成本常被混合→compute-matched AR/MDM×byte/token scaling及controlled permutation反证→分开context连续性与byte计算预算。|2+1+3=6|
|13681 FLM bridges|onehot FLM denoiser均值落simplex非合法endpoint→factorized posterior抽onehot再OU bridge、条件multi-information分解→分开token marginal保留与crossposition损失。|2+1+3=6|
|12951 CCVFM|hierarchical innerflow从各向同性噪声拟合多峰velocity→Sinkhorn coreset的GMM surrogate条件law加小correctionflow→分开source压缩/闭式proposal与residual学习。|2+1+3=6|
|13214 latentbackdoor|密码后门不易迁现代网络→latent方向利用/参数分布检验猜想与ResNet/ViT防御反侧→不由clean accuracy或既有defense签无backdoor；不先授密码不可检证明。|2+2+2=6|
|13487 PiFM|单时间FM不保证多控制参数组合path-independent→条件path/结构约束与simulationfree多参回归→检验分布插值的可积条件。|2+1+3=6|
|13565 QwenImageVAE2|高压缩重构/高维latent可扩散性相互牵制→GSC/增channel、语义alignment与非对称无attentioncodec、文本render评价→重考虑瓶颈位置/编码预算与重构非生成。|2+2+2=6|
|12954 AdaFocus|onepass稀疏不可回读or预载全帧→query relevance/diversity与uncertainty触发磁盘高分辨lookback→分开preview覆盖/临时恢复/驻留I/O费。|2+2+2=6|
|12964 AsymFlow|高维velocity拟合同时承担高维noise→低rank噪声/full数据非对称参数化并解析重组velocity→重考虑预测对象与latent→pixel迁移。|2+1+3=6|
|13307 PRISM-X|simuser常替真人评价个性化→530人52国within-subject/真人与sim层级vs个人判断反差→不能从aggregate排序授权个体偏好、个体FT收益或长期关系行为。|2+2+3=7|
|12622 StreamingIntent|VLA语义reasoning与多峰轨迹条件割裂→跨clip intent承诺/四步reasoning intent token→两步FM CFG条件→重考虑意图条件/时间一致，非AR必平均或安全保证。|2+2+2=6|

13675 UniversalObjectRepresentations完整题摘是162模型非负similarity因素的跨模型复现、semantic可解释性及生物一致性；可能具体修正representation convergence解释，也可能只是相关性归纳，需一次core判其操作性证据/对照，不因bio词直接排。13803 EvoGround proposer生成query-moment、solver反馈双方自RL的完整题摘仍有是否只是常规selfplay组合的准入含糊，一次core核具体奖励/数据接口得到判断即停；不自动准入也不因局部任务拒。

## A21 — 19实际整合 / DiM3 与 Pinductor 逐字 PRE / CPPO 采用域

R62三项实际POST均生效释放，累计19实际Books；当前README表/§1/§4已同步19完成、QLAM1中心隔离、39内19普通，既取尾16另作有限准入/日期，不新扩发现。一次README六行同步因hunk次序逆文件位置失败，实际未写入；按源位置排序后成功读回、限定diff-check通过，无旧95变化，不改公共脚本。

12960 readerR63必要Source/actualowner通过，T5 ZScore/DirW的SEED也高full，不声称full每项最佳。拟Ch23 SSAM21584完整第二段后→22823前一个自然段＋本人注；逐字正文：

语言骨干的合并还可把多语适配与多模态适配当作不同来源，而不假定二者是可互换的参数增量：相对同一 base，在每个矩阵 column 上分别比较 norm 与方向偏移，先在每个 source/矩阵内对各列的两种偏移分别排名校准，再跨 source 形成权重，把两份 residual 加回共同参考点；bias 与 normalization 等一维参数另按幅度处理。[DiM3 的受限对照](https://arxiv.org/html/2605.12960v1)支持这条无新增 joint training 的分支，但几何 salience 不是真实语言/视觉重要性，径角分解恒等式与表示可视化也不证明任务兼容或因果。原 vision encoder/projector 保留，语言 consumer 却已改变，因此不能承诺原 grounding 函数不变；部分语言和一般多模态指标仍反退，联合规则也不是每个指标最好。Source checkpoints 的训练、共同 tokenizer/层坐标核对、rank/合并、validation 搜索与新旧任务回归均计费。共同基座不成立、能力回退或预算不合算时，保留原多模态 anchor、独立语言模型/adapter 或真实配对适配，不由免后训或参数几何自签全部能力保持。<!-- source-family:SF-2026-ARXIV-2605-12960 -->

- `SF-2026-ARXIV-2605-12960` — Daily2026-05-15补May14；[exact-v1](https://arxiv.org/html/2605.12960v1)§3–6/Eqs1–17/T2–6/B/C/T15–16必要，2+2+2=6/异质language-MM residual差额深入，readerR63有限独核。保column与1D分责、rank salience非语义、固定vision非保函数、SEED/各语反退及搜索/预训练全费；current v2无具体纠错信号，不全版对照，未核实现/复现。

13740 readerR61一次必要Source与actualCh25有限复用，作者实际完整读05138可执行hypothesis两段与上下演进/Hierarchy交接。拟第二段后→Hierarchy标题前一个自然段＋本人注；逐字正文：

隐藏 state 不可直接观测时，程序候选也可以接受软观测检验，而不只做确定 transition replay：先由语言 prior 提出 initial、transition、observation 与 reward components，按真实 action 推进粒子，再用候选 observation 与实测的 distance kernel 更新 belief，并以该候选 filter 后 belief 下的 expected log-kernel 排名。[Pinductor 的有限 MiniGrid 对照](https://arxiv.org/html/2605.13740v1)支持这种候选修订接口，score 却不是 marginal likelihood、ELBO 或校准的真实 posterior；reward/termination 只经局部诊断进入修订，不由观测分数认证其正确。无 hidden-state label 也不等无结构先验：空间/API、任务描述与人工选的成败轨迹已经限定候选，低 entropy、委员会分歧或较高 score 都不证明唯一辨识。程序/API、粒子重播、rejuvenation、planner 与真实交互全部计费，少交互的配置仍可能墙钟更慢，真实模型加近似 planner 也不是最优 policy oracle。先验、观测支持或预算不合适时，保留显式模型/可信 simulator、短 horizon 实测重规划与更宽不确定性，不让自诱导 belief 或想象状态取得真实环境的提交权。<!-- source-family:SF-2026-ARXIV-2605-13740 -->

- `SF-2026-ARXIV-2605-13740` — Daily2026-05-15补May14；[exact-v1](https://arxiv.org/html/2605.13740v1)§3–6/Alg1/Eqs5–10/A/C/D/F/G/H必要由readerR61一次实际Source、作者有限复用，2+2+2=6/latent下softkernel检验差额深入。保score非marginal likelihood、结构prior/10条人工轨迹、reward/termination局部权限、K可暂超及同LLM对照调用/planner差异；CPU/API总费与实际墙钟反侧，不授唯一辨识/最优控制/安全，未核实现/复现。

13554 CPPO作者已实际exact-v1 §2/§3.1–3.3 Eqs1–9/Alg1、§4.1–4.2/T2、§6/Limit及D默认/会计。InfoNCE同trajectory未来obs为positive、其他trajectory为negative；用negativeL2 encoder相似作Q proxy，再减当前policy actions均值：discrete全枚举、continuous MonteCarlo，送PPO clip不用GAE/手工reward/replay/targetnet。InfoNCE打分/负L2不是天然已校准occupancy概率，不继承论文“thus equivalent”精确Q；PPO clip非硬trustregion。方法prose先encoder后adv，Alg1先算adv再epoch训encoder，未闭完整更新身份时不照完整recipe。Goal仍人定singlefixed g*，不是免目标设计，IPPO全参数共享/localobs/id，中央critic只是未来建议非已实现。

默认18tasks/10trials/80Menvsteps，80evaluation×2048episodes，IQM minmax/95%stratifiedbootstrap；T2 JaxGCRL .806<CSAC .916，连续任务相对densePPO亦落后；“MCvariance导致”作者Limit明确无实质证据，不作因果。Goal-vsreward七变体仅两环境，不能泛化所有spec易设计/普遍无reward。TPE tune在缺配置或弱基线重调、完整搜索与encoder/rollout全计费；D单seed单task约10min–2h各绑定80Msteps，硬件/precision/净效率未充分核，不能报通用省费。当前官方仅v1，无具体纠错信号。尚需必要B goal定义/直接配置与actualCh32 vsCh26对读后交reader，不预Source完成。

CPPO必要B/D差额补足：B实际不是每环境七个reward＋七goal，Connector4+4、SMAX3+3合七。SMAX目标依可见敌人health、未见视满血；Connector目标含人工distance/progress，全connected等，NavixDoorKey goal混key-door/player-goal Manhattan进度，故免reward不等免shaping先验。D实际H100/每job8CPU已核（前“硬件未核”只是读到一半停点现消解），128rollout×512env×1250updates约80M，batch256，4×512swish/LN、repr64；matching training-scale不等匹配TPE搜索费，precision未充分披露。Alg1对negative-set是否含positive与adv冻结身份不完整不拼闭合recipe。

Actual作者完整读Ch32替代critic producers两段07579/10701与00347visual turncritic、GAE原定义和SAE直接交接；Ch26 goal/action proposal与generativeplanner两段 owns controller消费，不拥有PPO advantage生产。现Ch32只return/learnedV/rollout-based Q，缺same-batch hindsight contrastive score→action-centred advantage接口，拟唯一TRAIN-PPO，在“若 value estimate 很差，advantage 噪声会直接污染 policy update。”之前/HiPER完整段之后单段（需reader实际owner比较）。只采proxy producer与goal责任/连续反侧，不继承精确occupancy/单调保证，未核代码/复现。作者必要Source已足，待reader有限独核。

## A22 — 21实际POST / NAACA逐字PRE / GTA必要域

ReaderR66 DiM3/Pinductor实际POST生效释放，累计21整合；无未执行Books写锁。原95与确定新增39保留，QLAM1中心隔离，39内17普通，既取尾16有限闭合仍待，不新扩发现。当前README仍19统计，待本节下一轮同步，不当已最终归并。尾日期原字段实际保SUP_DC_TAIL15_20261019.json：12501 lowerMay13 00Z–registeredMay13 02:51:02Z整区间May13BJT，明确窗外而非材料失败；12521 Apr3提交→May14 registered、12586 May12截止前→May14 registered跨日，未确认资格/不评分/不读fullSource。其余A20十拟入＋两once-core最早May14 00Z到02:41:13Z全同May14，权限/唯一v1与官方history已作者逐项对，待reader有限日期合证。

13651 NAACA readerR65一次必要Source/currentartifact限定和actualowner有限复用；作者实际完整读Ch23 TimeOmni→ZeroSyl完整段→SSL训练identity两段，gap是全流轻声学前端后的event admission，不重复codec unit/记忆事实。拟ZeroSyl完整段后→SSL训练身份前单自然段＋本人注；逐字正文：

声学前端也可以先决定哪些片段值得交给昂贵的 audio-language consumer，而不直接把每个窗口都变成语言描述：完整流仍经过轻量分类 encoder，其概率变化驱动带阻尼的 recurrent field，再用自适应阈值、persistence 与 cooldown 提出候选事件，只有选中窗口进入后级。[NAACA 的有限对照](https://arxiv.org/html/2605.13651v1)支持这种有状态门控分支，不把 field 当神经机制真值或已验证的语义记忆；持续、重复或类别外声音可能不触发，未调用必须保留“未审/未知”，不能自动赋正常。重复 horn 的前两次漏选说明省掉冗余与丢掉重要再现是同一接口的两面，后级描述也可能失去边界上下文。转发音频比例不等净端到端时间，所有窗口的 encoder、field更新、缓冲、描述后分类与真实回归仍计费；当前 artifact 的较长上下文又不能倒填首发短窗口评价。输出帧分数与未触发窗口协议未闭时，不照搬连续检测 recipe；重要声音漏选、上下文或预算不可靠时，保留周期抽样、完整流读取与专用声学检测，不由少调用或局部 AP 签发持续监测安全。<!-- source-family:SF-2026-ARXIV-2605-13651 -->

- `SF-2026-ARXIV-2605-13651` — Daily2026-05-15补May14；[exact-v1](https://arxiv.org/html/2605.13651v1)§2–4/Limit/B/C/H及I重复horn直接反侧、官方当前XD入口有限检查由readerR65一次实际Source、作者有限复用，2+1+2=5/声学event admission具体差额深入。保全流PANN费用/未知非正常、C1/H未闭连续AP协议、四秒v1与current15秒上下文分离、time-sent非净40%与重复漏选；不授神经最优或安全/实时，未核实现/复现。

12957 GTA作者实际exact-v1 §4.1–4.3/Eqs3–7/Alg1、§5.1–5.6/T1–5必要方法/评价/反侧。单图DepthAnythingV2深度→已知K/targetcamera warp partialRGB→CogVideoX5B geometry diffusion补多视depth→独立appearance diffusion消费depth/partialRGB。Prose说concat+projection，Eq6写rgb+geo再Π，未闭shape不拼完整recipe。共同VAE读RGB/depth不证明深度无损或metric真值。Shuffle训练时以p=.5同置换noisy/GT views（空间样本不是物理时钟），保监督对应但未证明全部网络permutation equivariance或temporalbias唯一因果；不把该静态视图重排扩成动态video乱序。

Testtime近输入的Q=5先当可靠，再warp/mask已可render区域、逐步添生成视图；只是camera-distance启发式非独立验证，self-generated不新增真实observations，mask不证逐像素锁定。T4 scaling PSNR17.47→17.35反退，不采stable/monotonic或不损数字；T1 RealEstate translation .026高FlexWorld .024，不采所有指标最优。SAGvsGTA T2未配平两模型capacity/训练总费，shuffle T3支持所测增量但不隔离全部prior因果。VGGT pose/VideoDepthAnything训练标签亦为模型估计，QAlign/pose-estimator派生误差非真实几何/人评完整证明。

DL3DV约10Kscene×10traj=100K，eval55scene disjoint；RealEstate随机100筛79可用，非全部100。49frames720×480，8A800两模型各40ksteps，单A800约20GBpeak；precision/独立seeds/完整walltime/SLO未披露，不能以10K/100K训练样本数免去CogVideo/深度prior全费。两model采样、VAE、深度估计/warp、重复testtime、后处理及全部训练需计。Currentv2Sep9/IJCV，无具体纠错信号，不全版本重读。作者未核artifact/图像素/复现；已有geometry→appearance段不够时只补static-view顺序与恢复/自生成条件的具体gap，不把image-to3D的world名称迁Ch25真实transition。

GTA actual作者完整对读Ch24 14302时间codec/viewaxis两段与上下22554/ReTime、06667完整camera-motion交接两段/binding；MotionForcing10408两段已拥有depth先生成→RGB消费，单凭stage标签应NoChange，但缺view序列训练shuffle削弱视频temporalprior及有限自生成近视图回读分责。建议唯一Ch24在14302完整第二段后→06667:start前一段，承接codec identity再讲模型vieworder，避免复制10408两阶段机制；若独核已有覆盖则按具体论点NC，不为差额强写。待reader必要Source/owner有限独核，不先拟宽稿。

## A23 — 尾部准入闭合 / CPPO逐字PRE

恢复已重读AGENTS/当前Research、Report、Prompt与Sources适用分组、ROADMAP及Books背景/理念/指南；21 actualPOST有效，不重取。ReaderR69实际尾十完整题摘与两once-core、十二精确日期组合通过，确定新增51，非数量目标；12501 wholeMay13窗外，12521/12586跨日资格隔离，12836整篇撤回不入选不评分，13848具体贡献排除保持。必要Source尚未完成，不授DAY。NAACA A22逐字PRE已通过，向root申请唯一窄位，未授不写。

CPPO13554 readerR67必要Source/actualowner通过；作者恢复实际完整读GAE→SAE→信息时间→HiPER及后Value model原段，采用reader更精确位置：HiPER完整段后、`Value model 也需要训练：`前，绝不拆开Lvalue公式与原噪声结论。逐字正文：

Advantage 也可以从同批轨迹的目标可达性代理产生，而不先回归手工 reward 的 return：用当前轨迹的未来 observation 做 hindsight positive、其他轨迹做 negative，训练 state-action 与 goal encoder，再把所选 action 的负距离分数减去当前 policy 下 action 分数的均值，送入普通 PPO clipping。[CPPO 的有限对照](https://arxiv.org/html/2605.13554v1)支持这条 contrastive producer 分支，但它仍训练 Q-like proxy，不是 critic-free；负距离也不自动成为校准的 occupancy probability。离散 action 可全枚举均值，连续 action 要 Monte Carlo，所测连续任务反而落后；不能把差额唯一归因采样方差，更不由 clipping 得到硬 trust-region 或单调改进。Goal 与 hindsight 规则仍含人工设计，免 reward 不等免目标与 shaping 先验；更新顺序和 negative-set 身份未闭时不拼完整执行 recipe。Encoder、动作采样、rollout、调参及重复评估均计费，匹配环境步数不等全生命周期预算相同；目标不稳、代理失准或连续均值代价不合时，保留已验 reward、learned value 与 GAE，不让目标可达性分数替真实 outcome 和稳定 policy update 签字。<!-- source-family:SF-2026-ARXIV-2605-13554 -->

- `SF-2026-ARXIV-2605-13554` — Daily2026-05-15补May14；[exact-v1](https://arxiv.org/html/2605.13554v1)§2–4/Alg1/Eqs1–9/T2/B/D及Limit必要域，readerR67独核、2+1+3=6/contrastive advantage producer具体差额深入。保same-batch hindsight/goal先验、负L2非校准occupancy、连续MC反侧、更新次序/negative-set未闭与H100/搜索重复全费；不授critic-free、硬trust-region/单调改善或普遍省费，未核实现/复现。

GTA12957 readerR70必要Source/actualowner通过，作者拟Ch24 14302完整第二段后→06667:start前唯一自然段＋本人注；逐字正文：

静态多视图还要区分“用视频模型串起 camera views”与真实时间演化。若一条序列只表示同一场景的不同视点，可以在训练时对 noisy views 与监督目标施加同一随机排列，让模型少依赖原有相邻顺序；[GTA 的有限分支](https://arxiv.org/html/2605.12957v1)只在训练中如此处理，推理不 shuffle，不由它得到全网络 permutation equivariance，更不批准动态视频乱序。Depth→RGB 的分工仍是前述生成路线；这里额外改变的是 view-order 训练与测试时条件更新：先挑距输入较近的少数 camera views，再把自生成视图 warp 成后续条件。距离近只是可靠性启发式，生成图不变成独立观测，mask conditioning 也不保证最终像素锁定；重复扩展仍有 PSNR 反退，所测完整路线的部分几何指标也非最优。深度/pose 标签和评价亦含模型估计，不能以内部几何一致替真实场景保真。两套模型训练/采样、深度估计、warp、VAE 与重复回读全部计费；view-order、重投影或质量失配时，保留已验证 camera path、真实参考和较短扩展，不让自产条件累积成世界状态的事实权限。<!-- source-family:SF-2026-ARXIV-2605-12957 -->

- `SF-2026-ARXIV-2605-12957` — Daily2026-05-15补May14；[exact-v1](https://arxiv.org/html/2605.12957v1)§4/Eqs3–7/Alg1、§5/T1–5必要，2+2+2=6/静态view-order与自生成回读具体差额深入，readerR70独核。保sameπ训练限定、近Q5非验证、自生成非观测/mask非锁像素、T4/T1反退与两模型全费；不复制10408阶段分离、不授动态时序等变/metric真值，current v2仅IJCV无具体纠错信号，未核实现/复现。

SMA12872作者必要exact-v1§3.1–3.4/Eqs1–3、§4/T2–5、A1/A3/A5已读足，current官方仅v1/无具体纠错信号。多augmentation/多caption按entity成set，GLU对齐层消费冻结DINOv2/GTE1.5，FLVMI以min-max、FLQMI以max聚合跨set cosine，不是ShannonMI自动等价。Eq1正例SMI减负例称loss而prose需maximize，§3.3 singleton/logsumexp负集分母未明确包含positive，不能当标准CLIP完全等价或照拼完整loss。A1由跨和到D+2系数的代数不成立为一般identity，SMI增大亦可伴norm/组内形状变化，不能采“最大SMI等价最小centroid gap”的理论。此信号加深仅对应域，不因理论有错抹掉set objective经验分支。

80K MSCOCO多caption与冻结预训练prior，不是从80K样本从零预训练；FLQ16K/FLV1K对SAIL32K，50epoch多正/单正至200且validation早停，训练预算/negative人口不匹配。T2 FGVC1.83<CSA3.51、Flowers8.28<SAIL8.75，T3多正FLV I2T50.50>48.40但T2I37.70<39.16，与prose“单正例外”指向相反，按表保反侧；T5平均L2非分布divergence/解耦或通用质量。RTX A6000 48GB，crosssimilarity矩阵内存瓶颈、重复编码与epoch/搜索全费，precision/seeds/总wallND，不授ordersless全费或普遍支配。未核代码/复现。

Actual Ch23已有2507.06979完整段＋独立marker、前05462与后ST-STORM两完整段已对读：已讲positive kernel池及log聚合/negative人口，但未具体讲entity内多caption以facility-location coverage选相似对象的替代聚合。建议只在06979独立marker之后→ST-STORM前一段，保SMI非Shannon、gap非质量/无理论等价、set/negative身份与内存/反退；actual共同坐标与适配空间各段已有冻结encoder责任不重复。待reader Source/actualowner有限独核，不先写。

## A24 — Enhanced-EWC / learned perturbation必要域

12789作者已实际exact-v1§3.1–3.3/Eqs1–3、§4–6/T1；current官方仅v1，Comments8pages/应用说明无纠错。三支Fisher惩罚与旧相似关系约束有准入潜力，但Eq3对current配对i与old配对j作全部i,j差，未闭对应关系/old输入可用性，不认证关系不漂移；λ的“adaptive”更新规则、Fisher如何取样/拟合及CLIP实际规模未给。四任务10K/8K/12K/15K pairs只给aggregate，caption/image matching的“accuracy”粒度/逐任务忘记矩阵/seed、precision、hardware与wall全未披露；Fig3原caption明确Simulated Fisher，不能当真实训练Fisher。正文EWC .78与T1 .74不一致，78%摘要与.31→.08约74%不一，300%减overhead不可成立为通常定义。以上是中心方法/评价资格具体未闭，不由小数据或单seed自动拒绝，也不倒改5分准入。拟本次中心争议隔离：不采78%/74%/15%或普遍保留，不进Books；重开需要对应身份已闭的保留loss、Fisher/λ规则及逐任务可复查评价/预算。Actual Ch30已拥有full-weight Fisher保护/低秩冻结非唯一因果，不以其泛主题当本篇证据通过；待reader有限必要独核后定终态。

13284作者实际exact-v1§2/Alg1–2、§3条件/Th1–2、§4/T1/A1、B1–2与C2直接score期望域、D1–2配置。每token重采低维latent，由context LSTM+MLP生成整个prefix embedding扰动；训练用观测token score减独立latent先生成的synthetic token score，预测仍重采扰动，不是只训练NEFTune或离散token替换。匹配真实模型假设下两score期望同分布可消；这不是有限估计量无偏、非边际MLE梯度，也不保证真实语言可识别。有限目标的synthetic-sampling是否stopgradient须实现闭合，不能把期望依赖γ与sample固定求导混同完整recipe。Γ*仅stationary set、compact/smooth/凸set和投影curvature条件不授一般Transformer全局或OOD正确；C1投影等距推步未给足normal-space条件，不采用精确统计速率为部署保证。

Synthetic500×长10、10rep/±2SE只模拟perturbedbigram；真实WikiText2训练/OPT、Qwen3、GPTNeo；具体型号不补猜。LoRA仅本方法（rank8/alpha16/.05）对baseline full-param，learningrate亦差，不唯一归因连续扰动。K5、r64、batch16/maxlen64，eval20prefix+80continuation×5sampling，5次是生成重复非独立训练seed；PPL与Mauve不一，ID Mauve差、GPTNeoCodeParrot PPL28高NEFTune26，QwenDB反退等近表保。Hardware/precision、全search和wall未披露；每步全prefix重扰动不直接复用旧KV，额外model samples/forward必须计费。current官方仅v1/35pages无具体纠错，不扩附件/实现。拟仅可保learned prefix perturbation＋observed-vs-model score接口，是否整合待实际owner/reader；不授外推普适/净省费。

SMA12872 readerR75必要Source/actualowner通过。拟唯一Ch23 06979独立source-family marker后→ST-STORM前一自然段＋本人注；逐字正文：

同一实体的多份图文还可以先构成两侧集合，再以 facility-location 关系评价跨集合的覆盖，而不只平均所有 pair 的分数：max 聚合偏向最强对应，min-max 聚合再约束两侧可代表性。这是相似度聚合的替代分支，须保留 entity、增强/描述、正负集合与 encoder 身份；[SMA 的有限对照](https://arxiv.org/html/2605.12872v1)只支持冻结预训练 encoder 后的低数据对齐，不把组合型 SMI 自动当成 Shannon mutual information，也不由较小平均距离证明模态完全对齐。原目标符号与负集合分母尚未闭合，所写 centroid-gap 等价推导也不足成立，因此这里不发布完整 loss recipe 或 CLIP 等价定理。部分分类与 text-to-image 检索仍反退，batch/early-stop 与预训练支持又不同；多描述、编码、跨相似度矩阵、对齐训练和回归全计费，少配对样本不等少全部训练。集合质量、negative 人口或净收益不合算时，保留普通 pairwise/多视图目标、真实配对与原共同空间，不由 coverage score 或距离替下游质量签字。<!-- source-family:SF-2026-ARXIV-2605-12872 -->

- `SF-2026-ARXIV-2605-12872` — Daily2026-05-15补May14；[exact-v1](https://arxiv.org/html/2605.12872v1)§3–4/Eqs1–3/T2–5/A1/A3/A5必要，2+1+2=5/跨set facility-location聚合具体差额深入，readerR75独核。保SMI非自动ShannonMI、A1代数/目标符号/负分母未闭不采定理或完整recipe，T3 T2I反退与batch/预训练/矩阵全费；current仅v1，未核实现/复现。

13284 actual作者完整读Ch28 08984 latent target段→27925两段→08287扰动一致性完整段→后feedback target梯度定义，现已有固定corrupt/clean agreement与semantic gate，尚无每次token重新学习latent prefix分布并用data-vs-model score估计的替代训练接口。拟唯一Ch28 08287完整段后→feedback分支前单段，不迁Ch30只因其用LoRA；未核的真实模型可识别/有限估计量无偏不纳正文。12789争议与本篇必要Source可交reader有限独核，不为推定理论去读全C附件。

OmniLiDAR13815 readerR73一次必要Source/actualowner有限复用，作者完整读Ch24 DDPM抽样公式/简化loss段、后25289与02751两完整段。差额是empirical跨域训练人口与两种condition责任，非新CFG空条件或Mamba内核理论。拟DDPM“一次训练更新只需抽数据…”完整段后→25289前单自然段/本人注；逐字正文：

数据抽样还定义了联合生成器实际学习的域人口：直接拼接多个域的训练集，并不等每个 batch 含全域或训练权重平衡。条件也可分两层，短文本 descriptor 提供共享语义提示，显式 domain identity 再选择限幅的 gain/bias 调制；[OmniLiDAR 的有限 range-image 分支](https://arxiv.org/html/2605.13815v1)在固定域集合上使用这种分工，不把 descriptor 当任意 open-vocabulary 域控制。共享方向结构只是处理扫描几何的 prior，不保证物理有效；八个已构造域也不是传感器、平台与天气的完整笛卡尔覆盖，合成天气和 teacher 伪标不能当真实独立观测。完整模型在部分域/指标弱于局部模块或专用对照，并且参数与生成时间更高；共享训练不自动省成本。域数据、模拟/teacher、descriptor 编码、调制、全部训练与采样均计费，须分别验生成质量及实际下游；人口偏移、未知域或净收益不合格时，保留单域模型、已验证条件与真实数据回归，不由一个联合 checkpoint 或平均指标签发跨域无损。<!-- source-family:SF-2026-ARXIV-2605-13815 -->

- `SF-2026-ARXIV-2605-13815` — Daily2026-05-15补May14；[exact-v1](https://arxiv.org/html/2605.13815v1)必要方法/域构造/生成及GDA评价由readerR73一次实际Source、作者有限复用，2+1+2=5/训练人口与condition职责具体差额深入。保concat非平衡、descriptor固定域/domainid限幅、8域非Cartesian/模拟与teacher费用、DroneMMD/CDFM反侧及97.73M/3.52s对31.71M/1.87s更贵；不授物理/开词域或净省费，未核实现/复现。

12703 MMCL作者实际exact-v1§3.1–3.4、§4.1–4.2/T2–3、§5/T4、A1–3/A7/B1–3必要域。102tasks/14subclasses区分localrule/procedure/induction；judge只读rubric+文本输出可减少judge视觉误读，但不能独立回原图审oracle真值，91%agreement非正确率。主榜strictallrubric与rubricavg分别报，不能以76.6%对26.5%推唯一failure类型；human-agent任务过滤偏好上下文必要人口，nocontent成功则至多3次修/删，不认证预训练无污染。24个可textualize合成任务oracle 37.5→62.5→75不是全102或长manual，cleantext还经额外curation，不唯一隔离perception；manual pointer strict仍0、crop12.5却rubric低于pointer，局部定位与保上下文不同。B分类prompt看messages/response/rubric/judge但不看图，故4类为间接归因非因果真值，manual只subsetreview未给全量正确性。AgentScaffold Claude19.6→18.6而GPT26.5→31.4，额外计算/检索/recheck非matchedcalls，不授工具普遍胜。API每model整榜约2–3h/至多8worker、默认或推荐解码，token预算/独立重复seed/成本未全给；不并成训练/推理因果。Current仅v1无具体纠错，artifact非必要不取；保5分，拟评价流水线局部受控ablation，actualowner待。

13375 GRIP作者实际exact-v1§3–5.5/Eqs2–9/T1–3及AppC/D/E延迟必要域。FrozenLLM仅ATS取local/retainedmean residual/current-targetbudget经FiLM、learned/heuristic凸mix；stage1feature/KL/ratio蒸馏＋curriculum，stage2独立Bernoulli masks G16 grouprelative PPOclip/task-budgetsurcharge。Sigmoid openended targetloss仍非真quality、convexmix不是hard安全fallback。二值correctness在离散mask跳变不推出continuous relaxation梯度发散/全部梯度法失败，组相对相关credit不等isolates唯一因果token；Bernoulli与soft budget罚也不保每次exactK，上线hardmask/zero-groupstd未闭不拼完整recipe。LLaVA665K/10epochs/Adam1e-5，7B/13B、decoder3/7/16vsencoderbeforeprojector不同位置费用；192decoder100.22avg不等无损(MME1773.87<1862.17/TextVQA57.79<58.21)，64decoder90.71低VisionZip93.32/Vispruner93.98，13B110SQA72.73<74.07/55AI2D56.54<56.74反退。GQATTFT表s原64.60/192decoder47.50慢VisionZip44.70，batch/length/hardware/precision未披露不授15%同全费或服务SLO，训练G16完整backbone/teacher额外费不能漏；空间entropy/connectedcomponent非语义quality。Current仅v1无具体纠错，准入5保留，拟budget条件化离散视觉mask训练机制，actualowner待。

MMCL actual作者完整对读Ch66 00799三view段→00913跨depiction段/marker→“视频评估先确认模态与时间信息是否必要”及09851两完整段；现有00913已分add/replace description不同input，不覆盖teaching/test两角色交叉及pagepointer-vs-crop，Ch75 contextassembly不拥有benchmark验收。建议唯一Ch66 00913独立marker后→视频标题前一段，明示24可转换子集、额外textcuration/间接错误标签、pagepointer不修strict与crop丢context、费用，不授感知因果或通用无泄漏。待reader必要Source/actualowner有限独核。

GRIP actual作者完整读Ch23 CLASP12767段→23717音频profile→DSTP12358段→Gaze13080段→17087三阶段selector两段→02689 teacherattention段：Gaze拥有可读取region，17087拥有goldmask离线/线上信息责任，但未讲蒸馏后在固定consumer上以groupmask采样训练budget-aware ATS。拟17087第二完整段后→02689前单段，保soft罚非hardbudget/credit非因果、decoder/encoder层位及quality与TTFT反侧/全费，不再讲GRPO通式（Ch33已有）。待reader有限必要Source/owner。

MARLIN13496 readerR79一次必要评价/actualowner有限复用，作者实际完整读Ch56“目标函数不止吞吐”的全部goodput/目标/冲突段与后SLO admission公式/余量及校正段。拟“这些目标会冲突…”完整段后→SLO-aware Admission标题前唯一自然段＋本人注。逐字正文：

多目标权重还可以变成跨 epoch 的协商状态，而不每次只求一个固定加权分数：各单目标 actor 先提出计划，critic 对混合计划给出效用 proposal，再经有限 refinement 与投影；带边界的资本状态决定各方后续影响，超过阈值的反对才把计划拉回己方提案。[MARLIN 的受限仿真](https://arxiv.org/html/2605.13496v1)支持比较这种慢时间尺度控制分支，不使资本成为公平性或真实效用，更不证明 Nash、个体理性或任意混合计划可行。Reward 方向、归一化、离散映射与 veto 后约束未闭时，不照搬完整执行 recipe；最终请求仍由实际 admission 与 runtime 资格决定。其 trace 只提供到达 pattern，能源/碳水和所谓 TTFT 来自模拟/profile；将总执行时间除输出 token 数不能替代 prefill、排队及逐请求尾延迟。不同单目标配置的收益不能拼成一次同时达标，Balanced 在延迟/碳项还可弱于对照；候选、critic、模拟、预测和迁移/装载全费也未由较高 Pareto proxy 抹去。模型、freshness、真实 SLO 或总预算不通过时，保留固定可解释权重、保守余量与原 admission，不让协商同意替用户 deadline 或物理资源验收。<!-- source-family:SF-2026-ARXIV-2605-13496 -->

- `SF-2026-ARXIV-2605-13496` — Daily2026-05-15补May14；[exact-v1](https://arxiv.org/html/2605.13496v1)§3–6/Eqs1–11/必要Alg描述与直接反侧，2+2+2=6/慢时间多目标proposal与capital控制具体差额深入，readerR79一次必要评价/actualowner独核。保仿真/TTFT surrogate非逐requestSLA、reward/投影/veto资格未闭、Balanced反退/PHV人口与全费；不授公平/IR/Nash/生产节能，current仅v1，未核实现/复现。

## A25 — HetScene / Motion-INR 必要Source

13586作者实际exact-v1§3.2–3.4/Eqs4–6、§4/T1–3/配置及current，官方仅v1；正文自带August24日期不替history的v1身份/登记组合，不据此迁本日。Primary64/secondary37分类，先noise主对象，后固定无噪主anchors与noisysecondary concat selfattention，仅后支反传；几何embedding小初值learned scalar避免数值盖过类别是优化prior非语义或物理保证。LSG类+实例索引区分同类对象、边transformer/meanpool成globaltoken；Eq6第三项重复dst而文意需relation，未闭不发完整可执行recipe。NL<20/NS<100过滤、fixedslot/emptyclass，与“无固定上限”宣传不同；11508train/1496validation、BERT文字/ResNet18roommask、baseline重训同split但容量/两stage费用未配平。2D正交bbox投影FID/KID和topdown检索render的CLIP不验证物理contact/碰撞或行动sim安全；MP3D XZ FID79.10高于Diffu63.94、KID2.28高于.40，InfXYKID.45>.39、YZ .30>.28；T3 TB对sideview反退、HP非全metrics单调，不能把总差全归层级或scalar。两服务器2RTX4090/4A800配置、batch64/原文30000epochs/1000diffsteps，precision/seeds/wallND，不把epochs改steps或当全费匹配。只采heterogeneous noising/supportanchor接口，不作physical/simready保证，artifact/附加材料不为非采用性能结论扩取。

12778作者实际exact-v1§III/IV-A–C/Eqs1–10/Alg1、V/T1–2、VI-A–C/T3–5、VIII/T7、IX/T8/Limit；current官方仅v1/无具体纠错。FrozenNeMF INR-VAE：local1024+global256=1280latent，decode(z,t)时间查询；Diffusion4crossattention blocks读位置编码后keyframes，训练latent＋geometry/10%dropCFG。Inference posterior cleanlatent经decoder keyframe几何loss与slerp/gaussiansmoothedmask混合运动→encoder回读latent差额双约束，只最后300/1000steps作IMG，不等真实流形投影/后验采样/硬keyframe。Alg1 i=0/符号以及是否detach回读target未闭不照完整kernel；连续decoder不保所有derivative物理/接触。HumanML3D MotionX/SMPL转换固定128frames30fps，文本metrics仅参考无textcondition，seeds/precision/训练配置未充分披露；T1 R.K1 Rprecision .536<Cond.630/foot.066>.049，denseK20FID.348>NeMF.282，crossAIST keyerr.125>NeMF.030/foot.059>.024，constraint强度大质量/多样性反退。RTX4090/CUDA12.4/B32/5key/10runs timing，IMG30036.73s比noIMG6.96，IMG100097.61慢Cond44.72/DNO88.66；1000DDIMvsbaseline不同solver/优化预算非同质量全费。预训练INR、diffusion、每stepdecode/reencode/gradient及search均付，不能只单DiTFLOPs签linear全费或净加速。保5分窄采queryable-motion codec＋cleanlatent双约束采样接口，actualowner待独核。

两篇actualowner作者对读：Ch24 22742线性metric projection完整段与后00426刚体装配完整段/下一05163 articulatedasset完整段及后04662接触共同生成段，Ch23 codec/消费者分责及Ch26 controller只在必要交接核，不用静态layout名迁Ch25。Motion-INR22742后→00426前可补非线性decoder观测loss＋reencode有限双约束，区别硬线性projection与posterior保真；HetScene可在05163 articulatedasset完整段后→04662接触共同生成段前补无噪primary-anchor/secondary-onlynoise与语义尺度校准，不重讲普通stage串联。作者实际读全这些直接邻接，待reader独核具体差额/位置，尚未PRE。

R81 EnhancedEWC12789中心争议隔离通过，不计正面Evidence/Books，保原5分。R83 learned perturb13284必要Source/actual Ch28通过5；这里“不授有限估计量无偏”专指求出的参数估计量，不否定匹配真模型处有限MC估计函数的期望为零。拟08287完整段后→feedback分支前单段＋本人注，逐字正文：

扰动分布本身也可以学习，并同时进入训练与生成，而不是只把固定随机替换当正则：由低维随机变量与当前 context 生成 prefix embedding 的连续扰动，每次预测重新抽样。[Learned perturbation 的受限分支](https://arxiv.org/html/2605.13284v1)以观测 token 的 score 减去模型自产 token 的 score 来构造估计函数；在声明的匹配真模型条件下，有限 Monte Carlo 版本的期望可为零，但这不使求出的参数估计量无偏，也不等于任意参数处的 marginal-likelihood 梯度。自产样本随参数变化和固定样本求导的执行身份仍须闭合，不把条件渐近结果搬成通用 SGD、OOD 或全局最优保证。真实任务对照同时改变 LoRA/full tuning 与 learning rate，且 PPL 改善不伴随所有分布相似指标改善，不能唯一归因连续扰动。每 token 重扰整个 prefix、额外模型采样与多路训练均计费，旧 KV 的精确复用也不再默认成立；扰动支持、原任务质量或总预算不合算时，保留无扰动 NTP、固定增强与原缓存路径，不由一个零均值估计函数批准外推质量或净加速。<!-- source-family:SF-2026-ARXIV-2605-13284 -->

- `SF-2026-ARXIV-2605-13284` — Daily2026-05-15补May14；[exact-v1](https://arxiv.org/html/2605.13284v1)§2–4/Alg1–2/T1、B1–2/C2期望差/D1–2必要，2+1+2=5/learned prefix分布与估计函数具体差额深入，readerR83独核。保匹配真模型处有限MC函数均值零≠参数估计无偏/边际MLE梯度，stopgradient/全局rate不授，LoRA-vs-full混杂/PPL-vsMauve与全prefix/样本全费；current仅v1，未核实现/复现。

## A26 — MANGO / DESBench必要Source

12943作者实际exact-v1§4.1–4.5/Eqs5–11/Alg1–3、§5/T1–2、A3/B1–3/C必要，current仅v1/无具体纠错。历史最短正确workflow→同LLM且相似operation聚类，连续相邻不能同node；sourceplanner/重规划在既有graph邻接内挑nextnode，4sim状态不保一般Markov充分，role/prompt改变会改router输入身份。Reward混历史assignment process label和finalgt，textgrad global/local是模型反馈非数学微分/因果credit；selfjudge可靠性亦用GPT4omini对中间groundtruth比，非独立无标签真值。K-hop skip训练填历史GT中间步骤，部署改为到达node承担被跳subtasks，两权限不可混，不能推线上也可GT填空或跳过必需证据。推断只冻结优化prompt不等无planner/executor预算。MATH阈.7/384nodes、policyhidden128/100episodes每题、textgrad5epochs/B30、α.5/γ.95；K1主58.44→K2 54.32→K3 53.09→K5 52.26，token/time省损质量，T2 MaASAPI.709低MANGO.935，时间更短不等所有cost更少。Baseline搜索/训练人口非matched，hardware/precision/独立seed/完整workflow制备费ND，表construction62s不全lifecycle。保5分仅可采router-edge与prompt-node双状态及skip训练/线上分责；actualCh82 MASPO06623完整段前后/ResourceAlgebra、Ch81 SquRL15564完整段已作者读，前者仅固定拓扑prompt刷新、后者仅workflow选择，拟唯一Ch82 MASPO段后→ResourceAlgebra标题前具体联合gap；待reader必要独核，不写完整可执行recipe或最优path。

13172作者已在R39一次core有效层上补exact-v1§3.1–3.4/Eqs1–5/metrics、§4/T3与§5、A1–2/B1/D、current。共同DESsubstrate只控制物理状态/任务资源，不控制protocol改变的activation/可见信息/accept-only vsreject/localreroute/legalaction，因此不把差额唯一归graph形状或LLM推理。localcontrollerpayload含guidance/workingmemory，隐藏queue/状态不直读；state维护LangGraph/AgentScope不同但同payload，不等完整contexthistory配平。动作来源LLM/fallbackcontract单独计，fallback不是模型决策；各model/framework10seeds×3scenario30episode，A5C12/3profile平均遮异质，不推所有工业任务架构排序。Holonic lowmakespan/tardiness是早停/少completed(如GPTLangGraph仅2.8jobs、trunc .93)，不是总体优质/约束有效证明；相反层级效率改善仍更violations，energy/makespan皆simulation非现实deployment。i7-12700K/32GB本地runtime不含API全部服务费用、decoding/latency/precision不披露不授cheap，通信条数/LLM决策数非token数。AppD仅thinorchestrator不证明replication，current仅v1/无具体纠错，不扩E全部12大表。5分保留，拟评价时把权限/合法action与完成债务、rulefallback分账，actualowner待。

## A27 — MMCL / GRIP逐字PRE

12703 readerR86必要Source/actualowner有效，唯一Ch66 00913独立marker后→视频标题前单自然段与本人注。逐字正文：

任务要从局部视觉材料学习规则时，还应将 teaching evidence 与待解决的 test state 分开干预：先保留原图，只补 test state 的文字 oracle，再补 teaching evidence，最后才比较纯文字；指向正确页面与裁掉其他页面也是两种不同输入政策。[MMCL 的有限诊断](https://arxiv.org/html/2605.12703v1)只在以合成任务为主的可转换子集做这些对照，文字还经过额外整理，不由收益唯一归因感知，也不外推全部多模态任务能被无损 textualize。Manual pointer 可以提高 rubric 满足却仍不通过整题，crop 也可能损失必要上下文，因此应同时保留严格完成率、分项质量和原任务人口。只看 rubric/文本的 judge 与错误分类器不能独立回原图认证 oracle；跨 judge 一致和四类标签仍不是错误因果真值。材料制备、oracle 人审、额外 API/agent recheck 与重复评估都计费，scaffold 在不同模型上可反退；子集、文字支持或净预算不合适时，保留原图全上下文与独立核验，不以更干净输入的高分签发通用视觉理解或部署改进。<!-- source-family:SF-2026-ARXIV-2605-12703 -->

- `SF-2026-ARXIV-2605-12703` — Daily2026-05-15补May14；[exact-v1](https://arxiv.org/html/2605.12703v1)§3–5/T2–4/A1–3/A7/B1–3必要，2+1+2=5/teaching-test与定位诊断具体差额深入，readerR86独核。保24可转换子集/额外curation非全102、pointer/crop两口径、无图judge与标签非因果/真值、API-agent反退和全部费用；current仅v1，未核artifact/复现。

13375 readerR87必要Source/actualowner有效，唯一Ch23 17087完整第二段后→02689前单自然段与本人注。逐字正文：

Selector 的训练也可以把预算作为输入，而不是每个保留率重新拟合：用当前与目标压缩比例调制 local features，再与 retained-token 汇总的残差及已有 heuristic 分数组合；先蒸馏 dense consumer 的 feature/logits，再在冻结 consumer 上抽多组离散 Bernoulli masks，以任务反馈和超预算惩罚更新 scorer。[GRIP 的有限分支](https://arxiv.org/html/2605.13375v1)支持比较这种训练责任，soft penalty 却不保证每次 exact-K，learned/heuristic 凸混合也不是硬安全回退。组相对反馈只提供相关 credit，不识别唯一因果 token；离散 correctness 的跳变更不证明所有连续 surrogate 的梯度必发散或只有 RL 能解。部分低预算/大模型切片弱于其他 selector，target-loss reward 不等真实答案质量，较低空间聚集也不认证语义充分。Teacher、每组完整 consumer 评价、额外 scorer 与全部训练/推理均计费，剪枝层位和 GQA 的有限 TTFT 表不能替匹配质量的总请求 SLO；预算、标签或真实 consumer 质量失配时，增加保留量、回原静态 selector 或 dense，不由较高平均分批准无损或净省费。<!-- source-family:SF-2026-ARXIV-2605-13375 -->

- `SF-2026-ARXIV-2605-13375` — Daily2026-05-15补May14；[exact-v1](https://arxiv.org/html/2605.13375v1)§3–5.5/Eqs2–9/T1–3/C/D/E必要，2+1+2=5/budget-conditioned离散mask训练具体差额深入，readerR87独核。保softbudget/凸mix权限、credit非因果/非RL必要定理、64decoder/13B反退与GQA秒级TTFT配置不足/全费；current仅v1，未核实现/复现。

R88 learnedperturb13284 actualPOST生效，累计28I；尚未把PRE或已读Source算整合。R89 HetScene必要Source/current/actualowner已通过，按前A25有限域拟Ch24 05163完整段后→04662接触共同生成前一自然段＋本人注。逐字正文：

对象集合的生成也可以让不同语义角色承受不同噪声，而不在同一条链上同时求全局布局与局部细物：先生成主对象，再把它们作为无噪 anchor 与带噪次对象拼在同一 attention 序列，只学习后者的去噪；几何 embedding 另用小初值的可学习尺度，避免早期数值压过类别。[HetScene 的有限布局对照](https://arxiv.org/html/2605.13586v1)支持这份分责，不使预测的 support 成为真实接触或物理安全，也不使紧凑图条件保证每条关系。训练仍使用固定 slots、空类别与对象数过滤，不是无上限生成；原图编码的重复端点记号未闭时，不发布完整 graph recipe。投影 bbox 的 FID/KID 与检索渲染的 CLIP 只验各自代理，部分 MP3D/侧视与中间配置反退，不能从总均值唯一归因层级或尺度校准。标签/资产库、两阶段训练、图/文字编码、全采样与下游几何检查均计费；anchor、对象人口或质量预算失配时，保留单阶段、较稀布局与真实几何/接触验收，不由生成场景可导出就批准 simulator 或动作使用。<!-- source-family:SF-2026-ARXIV-2605-13586 -->

- `SF-2026-ARXIV-2605-13586` — Daily2026-05-15补May14；[exact-v1](https://arxiv.org/html/2605.13586v1)§3.2–3.4/Eqs4–6、§4/T1–3/配置必要，2+1+2=5/异质noising与anchor具体差额深入，readerR89独核。保fixedslot/<20/<100、Eq6重复端点不采recipe、proxy非physical/MP3D与side反退，原文epochs/两stage及全部费用；current仅v1，未核artifact/复现。

Google/Meta历史slice尾部按root授权只一次robots声明入口：deepmind.google/robots.txt与research.google/robots.txt实际均tool inaccessible；ai.meta.com/robots.txt实际44line声明唯一sitemap/ai_meta_com_sitemap.xml.gz，跟进一次只有3line不可读publication，不能据lastmod或目录存在证明May14无发布。加上已实际官网/域内日期搜索停止范围，仅将未恢复历史slice精确隔离，不再猜endpoint/遍历全年。

## A28 — 机构既有release资格 / 具体尾Source

OpenAI既有A19/A20线索已实际补读[官方Business release notes](https://help.openai.com/en/articles/11391654-chatgpt-business-release-notes)明确May14 2026完整section：remote mobile连接host Mac的livecontext/approval/diff/test；另trusted noninteractive local scripts/scheduler/privateCI可用ChatGPT workspace identity的access tokens。不是仅产品名：原来交互登录/人工确认路径→新增非交互workspace凭证入口→需重看runner信任/身份与审批职责，拟本日具名release准入，2+2+1=5，公开日期只采用官方May14日，不造时刻。不同于RSS同SafetySummaries已有效去重；不继承任何同日之外release字段。

日期事件采用层仅此section，拟仅报告版本/兼容事实；必要安全变化深入有限跟明确链接[当前access-token文档](https://learn.chatgpt.com/docs/enterprise/access-tokens)实际读Howworks/risks/permission/transport及revoke域：凭证代表creator/workspace而非PlatformAPIkey；tokencreation、localpermission与runtimeprofile不同，suspend非revoke，client→appserver transport credential另设。这些current字段含后到Work/WorkspaceAgent scopes，不反填May14全套权限/endpoint；不把只需trusted runner写成可安全执行任意fork。没有历史pinned实现或可比安全/性能实验，不能给May14新理论/普遍安全或无人批准保证，也不把currentdocs变本日新增第二事件。拟OnlyReport：日期固定的认证/远程观察能力变化，长期身份、leastprivilege/secret与audit分责不凭此source创造新机制。待reader一次准入/date/必要层与处置校准；未通过前不增确定表。

DESBenchactual作者完整读Ch66 harness/environment/scorer身份开头两段及后scorefirst适配段、Ch82典型topology/supervisor两个完整CORAL段。现有Ch66已讲adapter/retry改变被测对象，尚无authority改变legal-action空间与truncation-censored完成债务的组合验收；拟唯一Ch66 harness身份第二完整段后→scorefirst参数适配前单段，而非Ch82架构排序。只采受控protocol实验的比较资格，保samephysical非puretopologycausal、fallback来源和少完成导致低delay；待reader实际owner核，不授框架部署/工业优化。

MotionINR12778 readerR90必要Source/current/actual22742→00426通过。拟唯一Ch24 22742完整段后→00426前单自然段＋本人注；逐字正文：

观测经过非线性 motion decoder 时，也可以保留软约束而不强求一次线性投影：在冻结的时间可查询 INR-VAE latent 中生成整段运动，对预测的 clean latent 同时施加关键帧几何误差，以及由插值关键帧与当前运动混合、重新编码所得参考 latent 的差额，再继续反向采样。[Motion-INR 的有限分支](https://arxiv.org/html/2605.12778v1)只在采样后段使用这种双约束，回读参考仍来自模型和插值，不是新增测量、真实 manifold projection 或精确 posterior；soft loss 也不保证关键帧误差为零。可查询连续时间不自动保证接触、所有导数或物理可执行，较强 guidance 又会损害质量与多样性，脚滑、密关键帧及跨数据集切片仍有反退。预训练 codec、diffusion、每步解码/重编码/梯度、采样与调参全部计费，更多修正步可比原对照更慢；关键帧支持、几何质量或总预算不足时，保留原显式条件、较弱 guidance、插值或已验线性约束，动作提交仍由 controller 与真实反馈验收，不让较低 FID 替约束或部署安全签字。<!-- source-family:SF-2026-ARXIV-2605-12778 -->

- `SF-2026-ARXIV-2605-12778` — Daily2026-05-15补May14；[exact-v1](https://arxiv.org/html/2605.12778v1)§III–VI/Eqs1–10/Alg1/T1–5、VIII–X/T7–8必要，2+1+2=5/cleanlatent双软约束具体差额深入，readerR90独核。保非硬keyframe/真实manifold或posterior、脚滑/密key与AIST反侧、RTX4090/CUDA12.4/B32及IMG全费/非matchedsolver；current仅v1，未核实现/复现。

## A29 — 已授窄写闭合 / MANGO与DESBench逐字PRE / STOP必要域

R96已实际POST GRIP13375与HetScene13586，累计30I生效释放；MMCL12703与MotionINR12778已按root授R92稿精确保存单段与本人注，作者完整新增/直接两侧/注读回及限定Ch66/24 diff-check通过，待reader实际POST不预计整合。两次patch因不完整/公式转义锚点验证拒绝均无落盘，改用既读非公式完整邻段锚后一次成功，批准正文未变。R94纠正A26：DESBench B1明确deterministic decoding+short output budget；未披露是具体budget和完整服务latency/precision，不再称decoding策略ND。R95 OpenAI既有May14 release准入/date/必要域与仅报告通过，为新增第52家族；current scopes不反填历史，非新扩发现。

12943 readerR93必要Source/actualowner有效，Ch82 MASPO06623完整段后→ResourceAlgebra标题前一段＋本人注拟逐字稿：

图上的选择策略与节点 prompt 还可以共同学习，而不只在固定图内刷新旧候选：从有正确性记录的历史 workflow 构建操作节点与可用边，先按当前节点和任务相似状态选择后继，再用终局及局部文字反馈修正角色 prompt。[MANGO 的有限分支](https://arxiv.org/html/2605.12943v1)让路由状态与节点语义互相改变，四个相似度却不保证 Markov 充分，文字反馈也不是数学梯度或唯一因果 credit。尤其 K-hop skip 的训练数据可填历史 ground-truth 中间步骤，线上则须由到达节点承担被跳过的子任务，不能把离线填空权限带入部署或默许必需证据已经完成。更多跳步可同时降费用与降质量，更短时间也未必更低 API 成本；历史正确轨迹制备、聚类、策略训练、prompt 搜索、规划/重规划与执行均计费。支持、角色版本、跳步完成资格或净预算失配时，保留原固定图、原 prompts 与独立终局验证，资源准入仍由下一节另验，不由 learned path 授予最优或安全运行。<!-- source-family:SF-2026-ARXIV-2605-12943 -->

- `SF-2026-ARXIV-2605-12943` — Daily2026-05-15补May14；[exact-v1](https://arxiv.org/html/2605.12943v1)§4.1–4.5/Eqs5–11/Algs1–3、§5/T1–2/5、A2–3/B1–3/C必要，2+1+2=5/router-edge与prompt-node双状态及skip权限差额深入，readerR93独核。保GT训练/线上执行分责、相似状态非充分/文字反馈非因果、K质量下降与API.935>.709及workflow全费；SelfRefine轮数口径不拼，current仅v1，未核实现/复现。

13172 readerR94必要Source/actualowner有效，Ch66 harness身份第二完整段后→scorefirst前一段＋本人注拟逐字稿：

比较协调协议时，还应把 authority 与合法动作空间加入评估身份，而不只固定物理环境：同一任务到达和资源状态下，激活时机、可见信息、accept-only、reject、局部重路由或竞价权限不同，就已改变被测策略的可行集合。[DESBench 的受限对照](https://arxiv.org/html/2605.13172v1)据此能比较完整协议，却不能把结果唯一归因拓扑形状、框架或 LLM 推理。模型动作与规则 fallback 必须分账，确定性 decoding 也不消除它们的责任差别；同时报告完成量、失败/截断和未完成债务，不能让早停或少完成造成的低 delay 冒充全任务更优。部分层级配置的效率与违规还可背向变化，平均数会遮蔽模型/场景切片。共同 simulation、控制器状态、重复 episodes、本地及 API 服务和通信 token 全费须绑定；权限、完成分母或预算无法配平时，保留分层结果与不可比说明，不由同一 simulator 的低 makespan 签发通用架构优胜或现实工业安全。<!-- source-family:SF-2026-ARXIV-2605-13172 -->

- `SF-2026-ARXIV-2605-13172` — Daily2026-05-15补May14；[exact-v1](https://arxiv.org/html/2605.13172v1)§3.1–3.4/Eqs1–5/metrics、§4/T3/§5/A1–2/B1/D必要，2+1+2=5/authority与完成债务比较资格差额深入，readerR39一次core/R94必要Source与actualowner独核。保samephysical≠puretopology、LLM/fallback分账、低完成/截断伪低delay与违规反侧；deterministic短输出但具体budget/完整服务费用不足，current仅v1，未核实现/复现。

13165 STOP作者实际读exact-v1§2.1–2.3/§3–5/T1/Limit、A1–3与C/E相关评价口径；v2具体信号仅定点读§2同域/A3/A4的ECN prompt与新增annotation结果。v1以同student best4成功轨迹、规则节点分割、Gemini功能/正确结论标注，按GT保最早正确回答结论的前缀作LoRA SFT；tree用于分析，不是剪枝必要在线搜索。ECN是训练oracle非未知答案线上停止规则；同student初始分布不等训练全过程严格on-policy。v1单A10080G/BF16/r8/seed1/8192、SD6epochs对TG2epochs；预算图另TG6不拼，1000PRM问题筛后约900，推断cap AIME16384/其他8192。Llama AIME .400低Base .433、低SDfull .600；MATH Qwen .868低.878，输出token非含annotation/BoK/训练的净墙钟。Bootstrap问级不是独立train seeds，v1T1与AppE部分acc/token不一致（如LlamaGSM/Math互换与QwenRP），不拼置信区间或独立显著性。current v2明确Sep20 camera-ready；A4把correct-answer匹配改成完整逻辑充分解措辞但仍含GT，新增第二annotator而非取消oracle；只限定May14原主张，不把后到实验或新模型当本日新事件。拟窄采离线标注/训练目标与线上stopping分责，actualowner待对读，不授推理无损/净加速或完整recipe。

## A30 — PRISM-X逐字PRE / 两导航必要Source

MANGO/DESBench已按root R99授位精确保存，作者完整新增/直接两侧/注与限定diff-check通过；readerR101真实POST逐项通过，累计34I生效释放。13214 readerR100安全必要域/v3差额中心资格争议隔离，6分不改、不进Books；不是未读普通。STOP actual作者已完整读Ch29 P-ALIGN10064两完整段、前23041/后ScheduledCheckpoint10114两完整段，旧student选择teacher前缀再补全与本项GT最早正确self-prefix目标有具体差额；拟P-ALIGN第二段后→SCD前，已交reader有限Source/owner独核。

13307 PRISM-X readerR97一次深入Source/current/actualCh66通过，作者完整复用并读08118两完整段、前12894两段及后2507.06310/02460两段。拟唯一08118第二完整段后→2507.06310前单段＋本人注。逐字正文：

模拟器还要分别通过群体排序与同一人的偏好检验，不能由 aggregate 相似反推逐人可替代。先让模拟 judge 读取真人已产生的相同对话再排序，另让 persona 真正参与交互、产生自己的对话再排序；后者同时改变 assistant 的输出人口，不是对同一证据换一个 scorer。[PRISM-X 的受限真人对照](https://arxiv.org/html/2605.13307v1)中，四个模型 worth 的高相关与较低逐人一致可以共存，个性化路线的小差额也会随 rank/cardinal 读出及多重检验改变判断。真人同次 rating 与 rank 的一致只是跨提问方式参照，不是重测真值或绝对 ceiling；重复模型 traits 评分的 ICC 同样不能认证人类构念。应保存同人配对、实际输入权限、生成失败和有效人口，不用删错后的模拟分数抹去失败成本；短期偏好及条件相关也不签长期福利或因果伤害。用户样本/隐私、profile 制备、适配、完整交互、重复 grader 和人审均付费，输入 token 较少不是全费节省；逐人或互动分布未校准时，模拟只作预筛选，保留真实交互、持出用户与任务分项验收。<!-- source-family:SF-2026-ARXIV-2605-13307 -->

- `SF-2026-ARXIV-2605-13307` — Daily2026-05-15补May14；[exact-v1](https://arxiv.org/html/2605.13307v1)§2–4/式1–4/§6、SI5.1/6.1/7.1–7.3/9.1必要由readerR97一次深入，2+2+3=7。保530返访/52国但非全球随机、四worth点非逐人、Judgement与Dynamic人口/权限差额、rank/cardinal与FDR、同trial参照非retest、ICC非validity/非对称lag不授因果和全部费用；current仅v1，未核实现/复现。

13328 StereoNav作者在R36 oncecore有效层上补exact-v1§4.1–4.4/Eqs1–4、§5.1–5.4/T1–2、B1/Alg1/B3/T3、C1–2/T4及D必要；current官方仅v1/无具体纠错。Target-location prior是额外已给世界坐标＋当前pose/intrinsics，视内红点/视外边界cue，不是从语言凭空恢复终点。融合InternViT/DINOv2/FoundationStereo costvolume，action四步与disparity辅助联合训；pose/目标/encoder身份及三分支全费用都在，3B非sameRGB information。T1无外数RxR SR58低Efficient67/SPL43.5低54.3；外数后SPL52仍低54.3。T2同一semantic branch加render34.4→52.3表明目标信息/表示改变；其余geometry/深度不逐项唯一因果。C1fuzzy半径3m实际2m时SR72.8→50.6/SPL56.4→33，目标噪声并非无害。BF16/B512/两stage各1epoch/176+688GPUh、448²/8history/4actions，GPU具体型号/独立trainseed/完整服务wallND。实机G1/ZEDMini＋laptop/Ethernet/cloud，GPT parser提指令/target的来源与额外权限不能淡化；4场景×5instruction×3重复、1.5m停距不保碰撞或真实deadline，Alg1空投影条件疑误不照kernel。拟只采目标prior显式输入与stereo/action-depth consumer分责；actualCh26 17437地图/pose配对两完整段与后18374/前17351两段已读，可在17437第二段后/18374前补目标prior而非整地图输入分支；Ch23可复用encoder不是此owner。

13321 HCSG作者在R36 oncecore有效层上补exact-v1 III/IV-A–D/Eqs1–13、V-A–C/T1–7必要，current官方仅v1/无具体纠错。Waypoint暂停时detect，检测到人收6帧/预测后3帧；2Dposeconfidence与bbox中心depth回投trajectory喂LSTM，forecast hidden与当前crop经Qwen3VL生成文字→CLIP，再按node聚合人特征入graph。语义branch实际单当前crop而非完整video，forecast不是意图真值；meanpool及漏检/错人/时钟不可由GASA补证。Social collision/proximity trainingloss不是在线shield/无碰撞保证，softloss到离散action的梯度接口不照recipe。HA-VLNCE seen/unseen，2A6000/static100KstepsB64与finetune15K B8；precision/独立seeds/完整detector+VLM+等待/latencyND。T1 unseenCR.36仍非零，TCR5.02反弱BEVBert4.71；T2两分支seenSR.28低pose-only.29。T3语义增益SR.23→.24幅度有限；无独立人类intent/socialnorm标注，不能把gain说唯一intent理解或物理安全。拟Ch26 17351静态图摘要两完整段后/17437前补当前crop语义与未来占用特征的动态node更新，不迁Ch25世界预测理论；作者完整邻接已读，待reader有限Source/owner独核。

## A31 — MCB / PiFM必要Source与actual owner

13681作者实际[exact-v1](https://arxiv.org/html/2605.13681v1)§3.2–4.2/Eqs4–21、§5–6、A/Alg5与B1–3必要定理/证明，current官方仅v1无具体纠错。One-hot数据使posterior mean各block可解释成token marginal，先逐位置抽onehot clean endpoint，再按当前noisy state与该endpoint的解析OU pinned bridge抽下一state，而非直接fresh重加噪或平均到simplex内。Exact marginal下endpoint KL差为conditional multi-information，bridge的KL仅由data-processing得不增上界，不消除跨位置依赖；同mean但增加endpoint variance有限恒等可保。Th4 path-space比较须same终端law、绝对连续/Novikov和exactmarginals；到离散终端的适用及有限近似网络不能由标签自动满足，不拟采用无条件全路径支配。Temperature/topP修改posterior、theorem不无缝继承。Frozen LM1B/OWT FLM，1024samples/GPT2Large GenPPL和unigramentropy是proxy非精确likelihood/语义或任务质量；ODE低步低PPL同时collapse，more NFE、tau/p改变前沿，非普遍支配。GH200每config约1h、OWT1024tokens到1024NFE；训练/词表维state、categorical与bridge抽样/搜索/全部solver费用保留，precision/servingbatch/独立trainseed/生产wallND，不由sameNFE签same成本。新增离散branch也妨碍smooth deterministic distillation。ActualCh24连续文本02028两完整段及后05031/11748两段、11125球面分支已完整读；旧02028 freshforward resampling不是真reverse，MCB是currentstate＋onehot endpoint的OUbridge，可在02028第二段后/05031前补采样接口，不重复Ch20通用temp/topP。6分窄Source待reader。

13487作者实际[exact-v1](https://arxiv.org/html/2605.13487v1)§3.1–3.4/Defs/Lemma3.1/Prop3.2/Th3.3/Cor3.4/Th3.5/Eqs2–9/Alg1、§4.1–4.2/§5、A3 admissible定义与B2.1–B2.3必要，current官方仅v1无具体纠错；AIscience单细胞应用不采用、不扩其附录。两连续parameter的field共享同一probability path并各满足continuity则distributional path independence，弱于逐sample交换；pointwise还需partial-time差与Lie bracket兼容及足够正则/存在唯一条件。Affine conditional means＋固定positiveσ是平滑路径，population边际匹配不使有限network恰好可积，零额外regularizer只对该构造的精确目标适用；一般curly例不正则也失败，不能称共享backbone就自动commute。Barycenter仅admissible OTmap family/σ→0/非负simplex权重条件，不把square外插或负权claim升标准WB，更非一般多参数保证。Toydisc10seeds/512batch/3000epochs与CelebA64²两个attribute、sharedUNet双head/EMA；imageMFM是重适配baseline和OTstyle配对，图像定性/不适合的FID不验证属性正确或保身份，缺独立人评/完整预算控制，不采大模型quality/成本优胜。Lie/JVP/OT配对/额外head、训练和所有path积分全费，hardware/precision/image独立seed/fullwallND；不由B1推断快签端到端速度。ActualCh24 CFM定义/原Euler完整段、前00825+13386与后Cartan03588/04013完整段已读；可在Euler完整段后/Cartan前补多parameter共享density与sample-vsdistribution职责，不重讲单time solver。6分窄理论Source待reader，未核实现/复现或图像像素。

## A32 — STOP逐字PRE / 当前停点

13165 readerR102必要Source/actualCh29已通过。拟P-ALIGN10064第二完整段后→ScheduledCheckpoint10114前单段＋本人注，逐字正文：

另一种边界选择不请求 teacher 前缀，而从 student 初始化自身产生的成功轨迹里保留最早正确回答结论的前缀，再以它做监督。[STOP 的受限离线构造](https://arxiv.org/html/2605.13165v1)先按规则切节点，借 ground truth 与标注模型判哪些节点真正回答了问题；树结构主要用于事后分析，不是部署时可读取的正确性 oracle。这里的最早只相对既定切分与标注，不保证逻辑充分或未知答案时可无损停止，初始化 self-trace 也不使后续 SFT 全程严格 on-policy。标注错误可进入 target，后到修订改变正确结论的标注措辞仍保留 gold，不能倒填成首发已有的线上能力。作者不同监督源的 epoch 预算不一，部分难题/模型与未剪轨迹或原模型相比退步，正文与附录的局部数值也不拼成独立显著性。Best-of-K 生成、gold/节点标注、训练与完整推理均付费；标注支持、任务质量或净预算失配时，保留完整 verified trace、原 student 或经校准的显式 verifier，不由较短输出批准可部署 stopping 或普遍加速。<!-- source-family:SF-2026-ARXIV-2605-13165 -->

- `SF-2026-ARXIV-2605-13165` — Daily2026-05-15补May14；[exact-v1](https://arxiv.org/html/2605.13165v1)§2–5/T1/Limit/A1–4/C1–3/E必要、[v2受影响标注域](https://arxiv.org/html/2605.13165v2)，2+1+2=5/离线最早正确self-prefix与线上权限具体差额深入，readerR102独核。保GT/标注依赖、SD6/TG2与单seed/BF16/A100、AIME反退、T1/AppE冲突及全BoK/标注/训练费用；v2后到不作May14新事件，未核实现/复现。

PRISM-X已按root R103授权保存A30精确段/本人注，作者完整新段/直接两侧与注读回、限定Ch66 diff-check通过，待reader实际POST，不预计35I。README当前已将全部14每日源归并为本轮实际入口/停止/缺口，原机构记录只按原小时窗历史引用；将继续同步34I/3争议/1仅报告与14普通，而非沿旧完成标签签DAY。所有既有candidate行/日期评分/原连续§4仍冻结，不stage/commit/push。

## A33 — StereoNav/HCSG逐字PRE / Byte与VAE必要域

PRISM-X R104实际POST生效累计35I。STOP按root R107授A32稿/本人注保存，作者完整新增/两侧与注读回及限定diff-check通过，待实际POST。R105/R106两导航必要Source/actualowner有效；HCSG V-D/T8的Leo office五场景各10/合41of50实机由reader一次必要域复用，不另恢复，不授开放动态人群/通用安全。

13328拟唯一Ch26 17437第二完整段后→18374前单段＋本人注，逐字正文：

先验还可以只给终点而不提供整张地图：把外部 target-location prior 经当前 pose、相机标定投影到左右视图，视内画点、视外给边界方向，再将双目语义、结构与视差表示交给 action consumer，并以深度预测作辅助训练。[StereoNav 的有限分支](https://arxiv.org/html/2605.13328v1)改变了输入信息与表示，不是模型只靠原指令恢复目标；粗目标和预测 depth 也不是真实可达或碰撞许可。目标噪声会损伤停止与路径效率，部分 RxR 指标仍弱于对照，不能把模型较小或局部鲁棒性归成同信息预算的全面优胜。目标来源、pose/标定、左右视图时钟和 parser/encoder 版本须共同保存，先验渲染、双目三分支、两阶段训练、历史驻留、云端通信和 controller 全部计费；先验错误、出视域线索不足、几何或 deadline 不合时，重观测/重定位、恢复可靠目标与原导航路径或停机，不由屏幕中的红点批准真实到达。<!-- source-family:SF-2026-ARXIV-2605-13328 -->

- `SF-2026-ARXIV-2605-13328` — Daily2026-05-15补May14；[exact-v1](https://arxiv.org/html/2605.13328v1)§4–5/Eqs1–4/T1–2/B1/Alg1/B3/C1–2/T4/D必要，2+1+2=5/targetprior输入与stereo/action-depth consumer差额深入，readerR105独核。保额外目标/pose权限、Alg1不照kernel、RxR与fuzzy反侧、BF16/B512/176+688GPUh及G1/ZED云全费；current仅v1，未核实现/复现。

13321拟唯一Ch26 17351第二完整段后→17437前单段＋本人注，逐字正文：

图中涉及动态的人时，还可以把当前语义和短时运动预测分别写入 waypoint node，而不只压缩静态对象清单：检测到人后收集短观察序列，用 pose/trajectory 预测的中间表示提供未来占用线索，另将当前 crop 的模型描述编码成语义，再与静态 node 特征融合供指令条件选择。[HCSG 的有限分支](https://arxiv.org/html/2605.13321v1)只支持这种动作条件接口，单帧文字不是完整视频理解或真实意图，预测也不成为新增观测；漏检、错人关联、均值聚合和观察暂停仍可删失关键证据。碰撞与接近的训练惩罚不是在线 shield，所测 collision 仍非零、部分总碰撞指标还弱于对照，有限实机成功不批准任意人群安全。检测/追踪、额外观察等待、VLM/文字编码、预测与全部训练/执行均计费，节点时间或质量失配时恢复当前观测、较短 waypoint 与已验避障/controller，必要时停止接管，不由较高导航成功率替独立安全边界签字。<!-- source-family:SF-2026-ARXIV-2605-13321 -->

- `SF-2026-ARXIV-2605-13321` — Daily2026-05-15补May14；[exact-v1](https://arxiv.org/html/2605.13321v1)III/IV-A–D/Eqs1–13/V-A–D/T1–8必要，2+1+2=5/动态node的当前crop与forecast分责差额深入，readerR106独核，V-D实机必要域一次复用。保6帧/预测3帧非真实intent、softloss非shield、TCR反侧/有限office实机与2A6000/等待/VLM全费；current仅v1，未核实现/复现。

12928 Byte作者实际[exact-v1](https://arxiv.org/html/2605.12928v1)§4–7/T1、A–B算费、D同长度/E压缩proxy/Fspan/G词表反侧必要；current仅v1无具体纠错。SlimPajama/UTF8-256对Llama2 BPE32K，8192bytes对1792tokens声明raw exposure近似匹配，与G平均3.74byte统计不同，不升级逐batch等信息；B1152/48M–1.23B nonembedding sweep、6e18–2e21估算FLOPs，compute-match会改变capacity/raw exposure，capacity-match又不等compute。MDM ELBO训练、sequential chain-rule评分不等其任意并行sampler精确likelihood。外推AR1.3e22/MDM4.2e26远超最大实测2e21，不作已见交点/计算下界；FLOPs模型不替硬件wall/精度/seeds未披露。AR entropy AUC.829对BPE boundary仅probe统计，static AR token与position一起置换不是MDM随机mask的同因果干预；压缩器proxy亦非语义或唯一失败机制。关键反侧F朴素BPE-span byte mask更差，不由contiguity诊断直接开修复recipe，BoolQ部分byte胜BPE/难任务近随机，不能普遍byte不行。actualCh11信息量/Scaling三完整段及前后、dynamicByte章节原段已读；拟唯一信息量第二段后→跨tokenizer蒸馏前，补representation×objective交互/两matching合同，而非重写Ch24MDM生成。6分必要Source/owner待独核，未核实现/复现。

13565 QwenVAE作者实际[exact-v1](https://arxiv.org/html/2605.13565v1)§2.1–2.3/T1、§3/§4.1–4.3/Eqs1–4、§5.2–5.3/Eq5与§6.1/T2–3/6.1.3必要，current仅v1无具体纠错。f16/f32减spatialtokens＋expandC，GSC space-to-channel residual、attentionfree/lightencoder heavydecoder；C增加仍付projection/I-O/memory，不是全费不变。DINOv2-L中层单target，cosine/空间relation双margin先严后松；移KL/GAN在大data/budget成立的经验选择，不证明regularizer普遍有害或精确VAE prior。Billion-scale/模糊过滤、OCR密集real文档及多背景5–20px中英合成共同改变，不逐归GSC或semantic schedule因果。OmniDoc约3K/9类/256² crop与OCR字符筛选、同PP-OCRv5原图输出作reference；NED其实1-normalized edit agreement且高更好，共同OCR偏差不必自动抵消，不认原字符真值。T2 f16c128重建优而gFID10.29弱VAVAE6.03/VTP5.25，f32c192 gFID18.33弱同家f32c12815.05；T3 f16c128FID.79弱Flux2 .73，不授全指标支配。SiT80epochs/ImageNet256，无CFG但f8XL/2 vsf16/32XL/1不同token/patch预算；训练硬件/precision/independentseeds/完整wall及KL/GAN独立消融不足，不授净速/全费省。actualCh23 GAE10365两完整段＋前TREN/后11320两完整段和连续PAE07915段已读；拟GAE第二段后→11320前单段，补直接中层teacher的margin日程/细节容量与diffusability分验，不重复通用rate三角。6分必要Source/owner待独核，未核artifact/复现/图像像素。

## A34 — 三个已核生成机制逐字PRE / 导航POST停点

HCSG/StereoNav已按原授权顺序保存，作者完整新段/直接两侧/本人注读回与限定diff-check通过，readerR112实际POST逐项通过，累计38I，Ch26两窄位已释放。压缩恢复重读AGENTS/适用当前合同、Prompt、Sources使用/每日/arxiv/恢复、ROADMAP/最新路由与Books背景/理念/指南，仅复用本日有效层。未重复Source，未新扩发现。以下三项actual完整邻接已作者重新读回，R109/113/114必要Source与具体owner复用；各单段＋本人注逐字拟稿，未授写。

12951 CCVFM拟Ch24 19740第二完整段后→09639前：

Gaussian mixture 还可以不直接提供数据 score，而在 velocity space 提供可解析的 source：先从数据 coreset 拟合低秩 mixture，再构造条件 velocity law，最后学习它与目标 velocity 之间的修正。[CCVFM 的首发分支](https://arxiv.org/html/2605.12951v1)在给定条件后独立抽 source 与 target；起点处的平移恒等只解释 surrogate 差距，不让有限网络或离散积分无误差，也不保证 source 总比 Gaussian 更近。后到[修订](https://arxiv.org/html/2605.12951v2)改成按训练数据行选 component，已改变 coupling，不能倒填为首发已有的 within-mode 配对；其边际匹配证明也不授任意时间的完整执行保证。量化率与少步界另有假设，matched source-only retrain 尚未完成，部分修正与媒体指标仍反退。Coreset/Sinkhorn、SVD、mixture 驻留、codec、修正训练和全部积分/搜索均计费，解析抽样的 NFE 记账不等真实 neural call 或墙钟；近似、coupling 或净质量不合时，保留原 noise source、解析 reference 或原 FM，不由可解析 source 签发少步无损或全费优势。<!-- source-family:SF-2026-ARXIV-2605-12951 -->

- `SF-2026-ARXIV-2605-12951` — Daily2026-05-15补May14；[exact-v1](https://arxiv.org/html/2605.12951v1)§3–5/Eqs2–10/Th1–3、A3/C/D1–5/E7必要，2+1+3=6，readerR109一次必要Source与v2受影响域独核。保v1条件独立/v2行anchor改变coupling、t0身份非任意t、量化/少步条件与D5归因缺口；CIFAR/T7反侧、GH200/B128等原配置和全费；未核实现/复现。

13681 MCB拟Ch24 02028第二完整段后→05031前：

若 clean 表示是 one-hot，posterior mean 的每个 block 还可读成 categorical marginal：先逐位置抽取离散 endpoint，再按当前 noisy state 与该 endpoint 抽解析 OU pinned bridge，而不是重新从前向噪声分布独立起步。[MCB 的受限接口](https://arxiv.org/html/2605.13681v1)保留当前状态，并在精确 marginals 下保留均值、增加 endpoint 协方差；逐位置抽样仍丢失跨位置依赖，factorization 的 KL 是 conditional multi-information，bridge 只有 data-processing 上界，不是完整 joint 已恢复。近似网络、temperature/top-p 与离散终点也不自动满足路径比较的全部假设。有限文本 GenPPL 与 unigram entropy 要联合看，较低前者可伴多样性塌缩；词表维状态、categorical/bridge 抽样、训练和全部 solver/搜索均付费，同 NFE 不等同墙钟，新增随机分支还增加确定性蒸馏压力。边际、质量—多样性或净预算未校准时，保留原连续求解器、离散 diffusion 或 AR，不由解析 bridge 名称批准精确生成或普遍少步优势。<!-- source-family:SF-2026-ARXIV-2605-13681 -->

- `SF-2026-ARXIV-2605-13681` — Daily2026-05-15补May14；[exact-v1](https://arxiv.org/html/2605.13681v1)§3.2–4.2/Eqs4–21、§5–6/B1–2/C必要由readerR113有限独核；作者另读A/Alg5/B3，2+1+3=6。只采用currentstate＋onehot endpoint pinnedOU与MI/data-processing界，不采无条件path支配；保frozen LM1B/OWT、GH200约1h/config、1024samples/GenPPL+entropy proxy和全费。current仅v1，未核实现/复现。

13487 PiFM拟Ch24原Euler完整段后→Cartan03588前：

当控制量不止一个连续参数时，还须区分“沿不同参数顺序得到同一分布”与“每个样本都到同一点”：两个 field 若分别满足同一唯一 probability-density path 的 continuity，支持前者；后者还要时间偏导与 Lie bracket 的兼容及足够正则、存在唯一条件。[PiFM 的有限构造](https://arxiv.org/html/2605.13487v1)以 affine conditional mean 与正噪声尺度构造共享平滑路径，精确 population 目标的相容性不让有限网络或共享 backbone 自动可积。Wasserstein barycenter 联系另限 admissible OT family、噪声趋零和非负 simplex 权重，不延伸为任意外插或多参数保证。小型分布与双属性图像对照也不认证语义编辑、身份保持或大模型净收益；OT 配对、额外 head、Lie/JVP、训练及全部 path 积分均计费。相容性、属性或预算失配时，保留原单参数场、显式顺序与独立终态检验，不让分布路径独立替逐样本交换或有限步误差签字。<!-- source-family:SF-2026-ARXIV-2605-13487 -->

- `SF-2026-ARXIV-2605-13487` — Daily2026-05-15补May14；[exact-v1](https://arxiv.org/html/2605.13487v1)§3.1–3.4/Defs/Lemma3.1/Prop3.2/Th3.3–3.5/Eqs2–9/Alg1、§4.1–4.2/A3/B2.1–3必要，2+1+3=6，readerR114独核。保unique shared density≠逐sample/有限net可积、WB条件与Curly反侧；10seed toy及CelebA64²非人评/全matched预算，AIscience应用不采用。current仅v1，未核实现/复现。

## A35 — Byte/QwenVAE逐字PRE / AdaFocus与AsymFlow必要域

12951/PiFM/MCB已获root A34三个精确窄位并顺序保存，作者完整新段/直接两侧/本人注读回、限定Ch24 diff-check通过，待reader实际POST，未提前计整合。R115/R116 Byte与QwenVAE必要Source/actualowner通过，作者实际完整再读Ch11信息量前01386两段、信息量两段及蒸馏后接；Ch23 TREN/GAE两段与11320两段，逐字拟稿如下。

12928拟唯一Ch11信息量第二完整段后→跨tokenizer蒸馏前：

稳定分母之外，还应把 representation 与训练 objective 联合比较：同样的 bytes 换成细粒度单元，AR 与随机 mask 的学习条件并不相同；相同估算 compute 会改变容量和 raw exposure，相同容量/数据又未必同 compute。[受限 byte/BPE 对照](https://arxiv.org/html/2605.12928v1)在这些不同 matching 合同下显示交互，不能把近似长度配平当成逐 batch 同信息，或把超过实测预算很远的拟合交点当成已见平价。AR entropy 对 BPE boundary 的 probe 关联不是唯一因果，朴素按 BPE span 联合 mask 的 byte 变体还退步，诊断因此不自动交付修复 recipe；部分任务的 byte 反胜也否定普遍不可行。ELBO、顺序评分与并行 sampler 的质量须分开，tokenizer、搜索、训练和完整采样均计费，估算 FLOPs 不替真实墙钟。Objective、人口或预算不匹配时，保留原 BPE、原 byte 接口及分项结果，不由较短序列、单一 loss 或外推曲线签发通用编码优胜。<!-- source-family:SF-2026-ARXIV-2605-12928 -->

- `SF-2026-ARXIV-2605-12928` — Daily2026-05-15补May14；[exact-v1](https://arxiv.org/html/2605.12928v1)§4–7/T1/A–B/D–G必要，2+1+3=6，readerR115独核。保raw exposure近似/两matching合同、MDM ELBO非任意sampler精确likelihood、外推非实测、span反退/BoolQ反侧及全费；原FLOPs处方未闭不照算，hardware/precision/seeds/fullwall未足披露。current仅v1，未核实现/复现。

13565拟唯一Ch23 GAE10365第二完整段后→11320前：

另一条 codec 分支不先压缩 teacher，而直接以冻结视觉模型的中层 feature 监督 latent，用 cosine 与空间关系的 margin 先严格对齐、随后放松，让重构细节获得容量；同时减少 spatial tokens、增加 channels，以 space-to-channel residual 和较重 decoder 承接细节。[Qwen-Image VAE 2.0 的有限对照](https://arxiv.org/html/2605.13565v1)支持这份接口选择，不使更高 channel 免费，也不证明去 KL/GAN 普遍更好或形成正确 Gaussian prior。大规模数据、密文字文档与合成细字同时变化，不能把收益唯一归架构或日程；OCR 评价以原图同一识别器输出作 reference，只是识别一致，不是字符真值。重构更好仍可伴下游生成指标更差，较宽 latent 也不总更易生成；teacher/数据制备、codec、OCR、generator 适配与全部采样均计费，不同 patch/token 预算不能拼成净加速。细节、diffusability 或总费用失配时，保留紧凑 teacher、原 VAE/regularizer 与已验 operating point，分别验像素、语义及生成，而不由单一重构分数批准全消费者兼容。<!-- source-family:SF-2026-ARXIV-2605-13565 -->

- `SF-2026-ARXIV-2605-13565` — Daily2026-05-15补May14；[exact-v1](https://arxiv.org/html/2605.13565v1)§2/T1、§3–4/Eqs1–4、§5.2–5.3/Eq5/§6.1/T2–3必要，2+2+2=6，readerR116独核。保direct中层teacher/margin日程与GAE区别、OCR agreement非GT、gFID/宽C反退与f8/f16/32预算差、全部codec/data/generator费；current仅v1，未核实现/复现/图像像素。

12954 AdaFocus作者实际[exact-v1](https://arxiv.org/html/2605.12954v1)§3.1–3.3/Eqs1–6、§4训练、§5.1–5.6/T1–13与§6必要。Current metadata题名加Efficient但仅v1，无具体纠错。1fps CLIP全流候选→query relevance/temporal diversity greedy选preview；低相关时feature KMeans，不保证temporal全覆盖。乘积greedy不等Eq1加性objective的精确optimizer；confidence是长度归一logprob，而§4默认positive .97口径未闭，不照完整gate recipe。模型输出timestamp经regex或preview attention fallback提议±1.5s磁盘seek/解码，再追加regenerate最多3次；proposal不是正确证据定位。Zero-cache仅不预存dense帧RAM/VRAM，仍有CLIP全流features/preview/KV/磁盘。T8随机回看已有部分收益，不能独归定位；T1LongVideo57.85低base60.9、原权重T6VideoMMMU51.4低52.1，RL对Charadesbaseline反退。T13是一分钟Qwen2.5VL7B/单A100估算，single3.2s→avg6.5/worst14，非latency加速；33×只是视觉token footprint，未消CLIP/disk/重复forward。ckpt3000另8A100×8h、BF16/ZeRO2，adapter训练和混合数据费；完整服务batch/并发/seed/SLO未足披露。ActualCh23 activeobservation01345两完整段、前20392和后16455，另21079两段已完整读；旧静态crop/自回归crop路径未含磁盘重取时间窗与preview/archive分责，可在01345第二段后→16455前一段，强调可回读的时间证据而非新claim gate。Ch75无该具体读取机制，不重复generic context。

12964 AsymFlow作者实际[exact-v1](https://arxiv.org/html/2605.12964v1)§3–5/Eqs1–7、§6.1–6.2/T1–4/Limit、A1–4/B1–2与C1–2/Th1必要。P=AAᵀ正交projector只压noise，target=Pε−x0仍全D；P内velocity/P外−clean，恢复P外仍除σ，不消低噪敏感性。Latent线性lift的连续ODE同投影noise/init/time/scale耦合，不等非线性VAE decode逐像素或语义相同；scale还须校input/output/time。T1无clampFID2.28弱.04时1.76，PCA胜random、rank继续增又退；T2 1.57含REPA/CFG搜索且protocol可差.08。T3 fullLPIPS FID19.1弱latent15、CLIP .278弱VR .280，LPIPS改善pFID又损FID，不授全指标支配。ImageNet600epoch~1750H100h/BF16/50Heun；9B 3M图/B256/15k~1100H100h/32UniPCAPG，T3另10k非15k；同tokens不证整条服务墙钟，全PCA/Procrustes/teacher/LPIPS/调参费保留。Current v2具体把§5.2 Eq7与A3/Eq18/A4 Eq19的+λ/负最优系数改−λ/正系数，因随后clip[0,1]并非纯重命名；只作后到纠错，不倒填v1。即使符号修正，teacher读paired xtL而非xt、patchwise adaptiveλ也不自动保条件零均值，不采完整无偏降方差recipe。ActualCh24 22158两完整段/前ASBM后10099两段与总交接已读；旧image-like平均velocity输出未含同一target按subspace混合，拟22158第二段后→10099前一段，只采rank-asymmetric接口/线性lift限定，不重复Ch23codec。两篇6分必要层待reader有限独核，不核实现/复现/图像像素。

## A36 — ActionEmergence逐字PRE / 最后两项必要域

R119三项实际POST使累计41I；Byte/QwenVAE已按rootR121授位精确保存，作者完整新增/直接两侧/本人注与限定两文件diff-check通过，待实际POST。12622直接复用readerR120一次必要Source/安全边界，作者完整读Ch26前00500、11219两完整段、后23121两完整段及24584交接；拟唯一11219第二段后→23121前单段＋本人注，逐字稿：

高层语义也可以先成为闭集 commitment，再进入连续动作场，而不是只在训练后比较两层类别：自回归输出 intent，经解析映成 action bias，并保留有版本的 previous-intent 表与 FIFO memory，使后续 clip 消费历史承诺。[ActionEmergence 的有限分支](https://arxiv.org/html/2605.12622v1)支持这份条件接口，不使模型文字等于真实意图，解析失败的默认类别也不取得安全权限。离线标注使用未来 video/kinematics，与部署可见历史不同，不能把特权 target 当线上信息；共享权重和 causal 顺序亦不证明语言对动作的忠实因果控制。少量 intent 改写与短场景结果不覆盖全部驾驶行为，局部 RFS/TR 与 CFG 蒸馏仍有反退；两次变一次的 action forward 只减少局部 head/条件计算，不是视觉、AR、memory 与整条采样费用减半。标注/teacher、训练、历史维护和真实闭环全计费，commitment、时序、意图支持或 controller 期限失配时，保留原示教与条件动作路径、重观测或接管，不由 intent 格式、内部一致或位移指标批准真实道路安全。<!-- source-family:SF-2026-ARXIV-2605-12622 -->

- `SF-2026-ARXIV-2605-12622` — Daily2026-05-15补May14；[exact-v1](https://arxiv.org/html/2605.12622v1)§2.1–2.3/Eqs1–2、§3.1–3.5/T1–3/§5、B3/C必要由readerR120一次独核，2+2+2=6。保20closedset/parse非安全、future监督/prev-intent/FIFO身份、438val有限RFS与TR/蒸馏反退、8GPU BF16与全部费用；current v2无具体纠错说明不全比，不计May14第二事件，未核实现/复现或驾驶安全。

13675 UniversalObjectRep作者实际[exact-v1](https://arxiv.org/html/2605.13675v1)§3.1–3.4/Eqs1–4、§4.1–4.3/式5/相关Fig2–3及§5–6必要，current官方仅v1无具体纠错，不采用或扩神经科学预测应用。162固定视觉模型/22248 THINGS图/1854类各12，penultimate features→每模型RBF关系矩阵→非负低秩分解，模型内调bandwidth/stability/reconstruction与五factorinit；五init不是五独立模型训练seed。固定r50后Hungarian一一匹配维度，row permutation null破坏图像对应而保column结构，避免dense正向量的偶然cosine；不是模型权重/功能对齐。ObjectNet人口与leavefamily/bootstrap只支持所测ranking稳健，不证普遍ontology或下游improvement。Universality与重构重要性近零相关(.01 pooled/.08 within)，specific同可有几何贡献；高可解释不等重要/因果。Taskonomy任务cluster效应F12.7/p<.001、contrastive contrast g1.76但校正p.065、architecture CI含.29，不能把不显著写成无inductivebias影响。Nonnegative additive/倒数第二层/偏向人用模型及图像人口限制，superposition与其他层未捕获；全特征提取、N²关系、bandwidth/rank/init搜索/匹配与标注计费，hardware具体/precision/fullwall未足披露。正文Appendix引用有缺失，不自补null公式或完整复现处方；窄采用方法分责/几何重要性反证已足，不为全附件无限恢复。ActualCh5 12703 susceptibility两段、29654 taskmetric完整段、00474 iERF完整段与24302跨模型分数迁移完整段及后自省两段已读。拟唯一00474后→24302前补跨模型relationalfactor发现与functionalimportance分验，不重复Ch23模态codec、Ch66通用harness；5分必要Source/owner待独核。

13803 EvoGround作者实际[exact-v1](https://arxiv.org/html/2605.13803v1)§3.1–3.3/Eqs1–10、§4.1–4.2/T1–3、§5/T4–7/Limit、A2–4/Eqs15–17/T8–10必要；current官方仅v1无具体纠错。同backbone两角色交替冻结：proposer出4个query/time；SigLIP2 .4B按时长8–32帧，以exp(-γstd) intra×跨moment softmax inter约束，再用solver与自产时间的tIoU反馈/δ0→.3→.5限制资格；solver在独立pair上GRPO，proposer用GDPO不是所有角色同归一。低variance本身可均匀不相符，inter只相对同组，不证绝对semantic truth；提高δ依赖当前solver可解而非真实难度，伪timestamp不是独立GT。相同rawcorpus不配平CoT/采样/训练/监督，A4不能唯一归causalframework。T1Charades mIoU53.1弱TimeR1 58.1；TVG R1@.7 15.3<16及ET69<69.4；7.5K扩数据TVG R1@.3/.7反退，captionSODAc4.1弱6.4；不是allmetric支配。三轮/每轮~9Kpair/4A100下24h原措辞范围不扩总费用，Qwen2.5VL7B/2fps/2.8Mpixels/B1gradacc4/G2/Adam1e-6/max512/200；precision/独立trainseed/完整服务wallND，bootstrap1000testresamples非多训练seed。teacher/全部视频编码、SigLIP/双role rollout/反馈/两套更新/评价全计费，超长视频明确成本增。ActualCh33 selfplay完整角色段、ScaleLogic、ToolR0完整段与V-Zero两段/20209两段已读；既有外部/verifier或多数投票分支没有跨moment对比与一致性×可解率资格，拟唯一21320完整段后→10094第一段前单段，长期机制owner为TRAIN-GRPO不在Ch82照搬twoagents，也不重写Ch23video表示。6分必要Source/owner待独核，未核实现/复现/图像像素。

## A37 — AdaFocus / AsymFlow逐字PRE

Byte/QwenVAE R122真实POST通过累计43I；五普通身份均仍保原评分。README表/§1正在按实际层同步，先前一处多hunk未按源位置排序导致验证原子拒绝、无落盘，已按实际index排序后成功，不影响任何有效原行。以下R123/R124必要Source/current/actualowner有效复用，逐字拟稿：

12954拟唯一Ch23 01345第二完整段后→16455前：

视频的补充观察还可以回到压缩前的时间档案，而不把全部 dense frames 常驻内存：先用全流低频 features 选 query-conditioned preview，由初答提出时间窗，再从磁盘 seek/decode 局部片段，追加证据并重新生成。[AdaFocus 的有限分支](https://arxiv.org/html/2605.12954v1)区分 preview 与可回读 archive，模型 timestamp 或 attention 只提名读取位置，不认证定位正确或证据充分。Zero-cache 不等零状态，低频全流 features、preview/KV 与磁盘仍在；原 logprob 与阈值口径未闭，不照录完整 confidence gate。随机回看也贡献收益，部分原权重/任务反退，不能把全部提升归定位或训练无关。档案制备、全流编码、额外 seek/decode、混合训练与重复 forward 均计费，作者一分钟视频的估计平均/最坏延迟反而高于单轮，视觉 token footprint 不是全链 memory 或 latency。时间映射、回看位置或净预算失配时，保留固定帧预算、静态读取或扩大原片段，不让自己提出的时间窗取代独立答案验收。<!-- source-family:SF-2026-ARXIV-2605-12954 -->

- `SF-2026-ARXIV-2605-12954` — Daily2026-05-15补May14；[exact-v1](https://arxiv.org/html/2605.12954v1)§3.1–3.3/Eqs1–6/§4/§5.1–5.6/T1–13/§6必要，2+2+2=6，readerR123独核。保preview/archive回读接口、乘积greedy与logprob阈值不照recipe、T1/T6及随机回看反侧；单A100估计3.2→6.5/14s与8A100×8h训练/全部费用。current仅v1/metadata改名不回填，未核实现/复现。

12964拟唯一Ch24 22158第二完整段后→10099前：

预测接口还可以在同一 target 内按子空间分责：保留完整 data 项，只把 noise 投影到正交低秩子空间，使该空间内预测 velocity、正交补内预测负 clean，再组合回完整 velocity。[AsymFlow 的有限构造](https://arxiv.org/html/2605.12964v1)由 rank 连接两种端点参数化，不是把原数据或 token 数都降维；补空间恢复仍除 noise scale，低噪放大与 clamp 依赖未消失。配对 noise、时间和尺度下的线性 latent lift 可耦合连续 ODE，却不等非线性 decoder 的逐像素或语义保真。首发的控制变量符号在[后到修订](https://arxiv.org/html/2605.12964v2)中改变，clip 后不是纯重命名；近似 teacher 的输入条件及 adaptive 权重亦不授无偏减差，不把这条训练处方当成保证。部分 rank、无 clamp 与 FID/感知指标互有反退，REPA、guidance 和 perceptual correction 的收益分账；PCA/Procrustes、尺度校准、codec/teacher、训练和全部采样/搜索均付费。子空间、转换或净质量失配时，保留原 image-like/velocity head、latent 路线与多步 solver，不由解析恢复或同 token 数批准免费生成和全面优胜。<!-- source-family:SF-2026-ARXIV-2605-12964 -->

- `SF-2026-ARXIV-2605-12964` — Daily2026-05-15补May14；[exact-v1](https://arxiv.org/html/2605.12964v1)§3–5/Eqs1–7、§6/T1–4/Limit、A1–4/B1–2/C1及C2必要耦合声明/构造由readerR124独核，作者另读C2证明；[v2受影响符号域](https://arxiv.org/html/2605.12964v2)§5.2/Eq7/A3/Eq18/A4/Eq19，2+1+3=6。保全Ddata/低ranknoise/补空间1σ、线性lift范围与非无偏VR、clamp/LPIPS反侧、H100训练和全费；修订不算本日新事件，未核实现/复现/像素。

## A38 — 最后两项采用草稿 / 报告真实归并

README已实际归并43I/3中心争议/1仅报告/5普通，补写MANGO/DES/PRISM/STOP/两导航/CCVFM/PiFM/MCB/Byte/QwenVAE与13214必要判断；按完整baseline核95原行全存、原窗口全存、原§4连续块全存，当前147行。尚未DAY/FINAL，新增52不变，以下是等待必要独核的最小采用草稿，不授书稿写入。

13675拟唯一Ch5 iERF00474完整段后→24302前：

跨模型发现共享解释时，也可以比较同一组输入的关系，而不直接对齐不同维数的 activation：每个模型先形成图像间 RBF 相似矩阵，再分解为非负维度，以一一匹配比较各维度在相同图像上的 loading，并用破坏图像对应的 row-permutation null 校准偶然相似。[受限视觉模型对照](https://arxiv.org/html/2605.13675v1)中，这种复现度与人工可解释性相关，却几乎不预测该维度对关系重构的重要性；模型特有部分也可承担重要几何，不能因不共享就删除。核尺度、rank、输入人口与层都属于测量身份，倒数第二层的非负加性分解不捕获全部层或 superposition，也不证明这些维度驱动真实输出。某些设计对照未显著不等没有影响，特定任务族仍有差额；特征提取、二次规模关系矩阵、分解/匹配/参数搜索与标注均计费。共享分数、重要性或行为发生冲突时，保留原表示与模型特有维度，回到任务 consumer、受控干预和独立行为评价，不把通用标签当作跨模型可移植的真实因果字典。<!-- source-family:SF-2026-ARXIV-2605-13675 -->

- `SF-2026-ARXIV-2605-13675` — Daily2026-05-15补May14；[exact-v1](https://arxiv.org/html/2605.13675v1)§3.1–3.4/Eqs1–4、§4.1–4.3/Figs2–3、§5–6必要，2+1+2=5。仅共同图像关系/维度匹配null与重要性分验；保162模型/22248THINGS/r50/五factorinit非训练seed、Taskonomy与显著性/几何反侧和全部费用，缺Appendix不补完整null执行处方。Current仅v1，神经应用不采用，未核实现/复现。

13803拟唯一Ch33 ToolR0 21320完整段后→V-Zero10094首段前：

视频自训练还可以把语义一致与当前可解率分开反馈：proposer 生成 query–moment pairs，用冻结图文 encoder 比较一个 moment 内的相似度波动与跨 moment 的相对匹配，再由 solver 对自产时间的 tIoU 调整可训练资格；两角色交替冻结，proposer 与 solver 的奖励归一也分别声明。[EvoGround 的有限分支](https://arxiv.org/html/2605.13803v1)使课程同时受到外部预训练表示和当前 solver 约束，但低波动可以一直不匹配，相对匹配又不认证绝对语义，伪 timestamp 不是独立 ground truth。提高资格阈值会筛掉当前不可解的人口，不能把内循环分数当全覆盖或真实难度；同一 raw corpus 也未配平监督、rollout 与训练预算。更多数据和部分定位/描述指标仍有反退，test-set bootstrap 不替多训练 seed。视频/encoder 制备、双角色生成、SigLIP、反馈、更新及全部评价均计费，超长视频尤其昂贵；代理失准、课程收窄或全费不合算时，保留固定题库、独立人工标注/验题与原 solver，不由无需新增人工时间标签推成无外部先验或无限自提升。<!-- source-family:SF-2026-ARXIV-2605-13803 -->

- `SF-2026-ARXIV-2605-13803` — Daily2026-05-15补May14；[exact-v1](https://arxiv.org/html/2605.13803v1)§3.1–3.3/Eqs1–10、§4–5/T1–7/Limit/A2–4/Eqs15–17/T8–10必要，2+2+2=6。仅intra×inter与tIoU资格/交替冻结差额，保pseudo时间/同corpus非matched因果、Charades/TVG/ET/扩数/SODAc反侧、4A100/2fps/B1G2与全部费用；testbootstrap非trainseed。Current仅v1，未核实现/复现/图像像素。

## A39 — 全部单篇终态 / 六节归并待DAY

R130 ActionEmergence与R131最后四项实际非writer完整新增/两侧/本人注POST均通过，新增52＝48实际Books整合（15唯一章）＋3中心资格争议＋1仅报告，单篇Source/Books普通0。全部精确窄位释放，不把Source/PRE当写后。README六节已实际同步147候选；§1旧完成段显式限旧小时窗，§5自包含三中心争议不采边界/替代材料/精确重开条件、12521/12586跨日资格、12501 wholeMay13窗外及机构历史slice隔离；§6新旧复核分责分开，未签DAY/FINAL。

作者复算95原整行各存在、原窗口不变、147517字符连续原§4不变；52新行与原评分/日期保持。V3按当前工具通过，310本地引用/39唯一文件及全部hash零缺。真实原SUP_BASELINE不改，另以apply_patch生成工具文档要求的canonical baseline-before-supplement-20261019.md（只去末尾空行）并显式引用，不靠改旧日期换绿。两处A21 hash与新增StableNode链接外位置已修；四必查历史slice由检索受限改受阻，不冒no-hit。Reader六节通读具名6处表贡献句（DiM3/DiffEnc/Pinductor/GTA/PRISM/GAGPO）按其已核必要层最小澄清、两个补充表内空行删除，不动原95。全SUP本人note对原表评分分量比对只发现13565误誊2+1+3，已机械纠为冻结的2+2+2=6（A35与Ch23本人纯注），正文/总分/日期不变，交reader短读而非重Source。

限定working diff-check通过；限定cached检查发现既有SUP_SOURCES第630行尾空行警告，扩大到冻结旧基线另见SUP_BASELINE第925行相同警告。Index非本作者更改，不stage修它，最终透明保这两个cached例外，不称全量零警告。当前42个日期回归测试41过，唯一test_renamed_event_cannot_inherit_old_date单独复现同败；只读定位为旧test要求改题名即错误、现工具文档/实现按精确URL冻结允许题名纠正的预期失配。公共脚本/原日期不在本日修复范围，未改；V3本报告通过不冒全suite绿。无实现/GPU/生产实验复现、无stage/commit/push。待reader实际DAY→作者保存完成态→reader实际FINAL。

## A40 — R133 DAY后完成态已实际保存，待真实FINAL

ReaderR133已实际完整六节DAY通过，R134定点核回工具例外仍通过。作者按授权于2026-10-19T10:22:27+08:00实际保存README完成态：147＝原95＋补52；补52＝48实际整合/15唯一章＋3中心争议隔离＋1仅报告，单篇/来源可执行普通0，全部精确Books位释放。不扩Live/Weekly/2025/下一日，root负责总路由，本作者不写LS/索引，不stage/commit/push。

完成字段/§1/§5/§6已仅行政同步本次通过与普通0，旧95/窗口/连续原§4不动；§6准确记5个具名贡献排除样本与未检查范围、48实际POST及R133六节实际范围。最新工具例外是扩大cached仅冻结SUP_BASELINE:925既有尾空行；旧630输出按历史留A39，不冒当前仍有两警告。42日期测试41过/改名预期冲突由readerR134独立只读核回，不改公共脚本/index。保存后本报告V3再通过、限定working diff-check通过；下一仅reader对保存完成态实际FINAL，未由本作者自签。
