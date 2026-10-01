# 2026-09-29 Daily：Tail A 作者证据与有限采用提案

窗口：2026-09-28T09:00:00+08:00 ～ 2026-09-29T09:00:00+08:00。作者：sep29_tail_a；这是作者提案，不是独立 PRE、实际 Books 写入、POST 或日级验收。

仅处理 SPIMOE、PolyCIM、ToolWait、PRISM、MTP Performance 五个已获准入校准的家族。N1–19 的有效结果不重跑；不扩分类列表、代码或可选附件。依据本日 [唯一停点](screening-checkpoint.md) 复用四项未变化的必要正文证据，并补读精确 v1 与 PRISM 的必要理论/评价反侧。当前 abs 的五项身份、v1 历史和题名已重新核对，未见撤回、勘误或纠错标记；没有因审阅投入、Books 已覆盖或访问状态改分、删候选。只写本文件；共享 Books、正式 README、LEARNING_STATE 由 root 处理。

## 日期与作者结论概览

本日停点的 fresh 官方 Tuesday 29 September New 身份与 [arXiv 正常公告日程](https://info.arxiv.org/help/availability.html#announcement-schedule)、精确 v1 历史联合支持五项首次公开为 **2026-09-29T08:00:00+08:00**。下面 Submitted 原值只验证版本身份，不用于代替公开时刻；没有把 HTML 页首的 28 Sep 当成北京时间公开日期。AR/PF 的 New 与 CY/AI 恢复出的 primary New 依据均在唯一停点，未因 Cross 重计。

| 家族、准确原始题名与精确版本 | Submitted 原值（UTC） | 评分与实际投入 | 最终作者建议 |
| --- | --- | --- | --- |
| [SPIMOE: Exploiting Hybrid Sparsity for Reasoning MoE Inference on Heterogeneous PIM Architectures](https://arxiv.org/abs/2609.34612v1) | Mon, 28 Sep 2026 08:40:10 UTC | 2+1+3=6；标准及拟采用耦合命题必要核 | 仅报告，不把整套 recipe 变成强制 Books 差额 |
| [PolyCIM: Improving Data Reuse in Digital CIM Accelerators with Polyhedral-Based Compilation](https://arxiv.org/abs/2609.34351v1) | Mon, 28 Sep 2026 05:24:06 UTC | 2+1+2=5；标准后实际 owner 缺口定点深入 | 窄整合提案：`INFER-TENSORRT-LLM` |
| [Tool Waiting and Re-arrival in Compile-Time-Static LLM Serving: Cost Mechanisms and Configuration Selection](https://arxiv.org/abs/2609.34663v1) | Mon, 28 Sep 2026 09:02:13 UTC | 2+1+3=6；设计反证必要深入 | 窄整合提案：`INFER-CONTINUOUS-BATCHING` |
| [Beyond Energy: When Sustainability Dimensions Reshape LLM Serving Decisions](https://arxiv.org/abs/2609.35569v1) | Mon, 28 Sep 2026 16:31:50 UTC | 2+1+3=6；理论条件与生命周期反例必要深入 | 窄整合提案：`PLATFORM-COST` |
| [Beneath the Tokens: A Performance Engineering Study of Multi-Token Prediction in GPU-Accelerated LLM Inference](https://arxiv.org/abs/2609.35188v1) | Mon, 28 Sep 2026 13:49:34 UTC | 1+1+3=5；标准及性能归因反侧必要核 | 仅报告；现有机制覆盖不等于整套实验已存在 |

## 1. SPIMOE — 仅报告

采用 [精确 v1 HTML](https://arxiv.org/html/2609.34612v1) §3.2–3.4、§4.1–4.4；复用唯一停点已读的稀疏、硬件和反侧，定点重读 §3.4.2/§4.1 确认 prediction 与执行权限。论文不是仅换介质：phase/depth 阈值、思考关键 expert boost、拥塞 channel 上的额外 expert pruning 会改变模型路径；block selection 只减读取，结构边界 eviction 才释放实际 KV。SRAM attention 与 HBM QKV/FFN 分工后，sub-batch 需要在真实 gate 结果尚不可见时预测 MoE 成本，以前一步 mask、EMA affinity 和频率 prior 作 hint，再使两个阶段的时间相近。式6仍显式支付 startup/drain；hint 不能当作已经发生的 routing。

评价边界：Qwen3-30B-A3B、Phi-mini-MoE；Switch 只用于 FFN/PIMoE 对照，dense Qwen3-1.7B 只用于稀疏 attention。32 SRAM cores/4 HBM-PIM、FP16 GEMV、12nm 综合及 CIMFlow/DRAMsim3/Noxim 模拟不是实芯部署。A100-80GB 为作者标准 inference 对照；长序列无 sparse 配置反而变慢，uniform pruning 有质量反退，batch 增大又改善 GPU GEMM。仅以一般数学推理的有限质量检查界定近似，不引入科学领域效力；线上 concurrency/SLO 与普遍质量保证不采用，未复现。

实际 owner 对读：Ch21 [Execution Phase / 有边界计算预算](../../../../../books/part-02-model/21-moe.md) 已解释 phase 输入、错误边界、variable capacity 与质量/瞬时负载分账；Ch49 [联合编译及异构 IO](../../../../../books/part-05-inference-system/49-tensorrt-llm.md) 的“从逐 Kernel Launch 到 Persistent Executor”、动态 expert placement、tile collective 与 CIM 驻留分支，已经要求稀疏、精度、状态与 schedule 共同验收；Ch54 [物理视图及 sparse selection](../../../../../books/part-05-inference-system/54-gpu-memory.md) 区分 selection、实际 page residency、访问位置与容量预算。不是声称这些正文已完整解释本文算法。本文新增的是一套模型/介质校准 recipe 与其联合模拟证据；有限消融支持这些模块在该方案的组合价值，但不足把 phase-depth 门、boundary eviction 或 predictor 混合系数提炼成新的跨模型设计规则。可长期采用的“稀疏率不等物理容量/完整加速、预测不拥有语义、两阶段须共同结算”已有具体正文承载。本次保留这份联合验证与失败配置于报告，**仅报告**，不以模块组合、模拟倍率或新介质强造整套 Books I；评分和候选身份保持不变。

## 2. PolyCIM — Ch49 窄整合提案

采用 [精确 v1 HTML](https://arxiv.org/html/2609.34351v1) §3.2–3.5、§4.1–4.3；复用唯一停点未变化的必要方法/反侧。Access matrix 的 null 方向描述同 operand 的复用，斜向 hyperplane 在原迭代坐标里不一定沿轴；先 pre-tiling 限制 affine 变换后的 bounding-box 膨胀，再暴露/重新对齐复用、virtual coalescing、有限 macro post-tiling，最后处理 operand layout 和搬运/缓冲。改变的是可映射的复用坐标，不是用更多 macro 或换 operator 名；依赖合法性与数学结果、浮点 accumulation 次序要分开验收。

评价边界：8 macros、两种 SRAM array shape、CIMFlow 周期模拟，im2col 对照与 C1 单算子消融；group/3D convolution 较少获益，完整网络为三个 CNN，不是 LLM serving 吞吐。Macro utilization 优先及 sum-log traffic 求解不证明总 walltime 最优；离线搜索、layout 变换、缓冲和累加重排成本不免费，亦不授 bitwise 浮点等价。没有采用 headline 倍率、线上 SLO 或跨模型质量保证，未运行 artifact。

实际差额与唯一 owner：`INFER-TENSORRT-LLM`，[Ch49](../../../../../books/part-05-inference-system/49-tensorrt-llm.md) 当前“融合决策与数据搬运可以分层表达”已有 scalar→VR-tile→MA-tile 与 repair/live-range 分责；“FlashAttention 在这里的位置”已有 CIM 写/转置与驻留成本。两者未解释 **non-axis reuse → affine realignment → 有限 CIM macro/layout** 的候选形成机制。前后 Ch48 提供算法/acceptance，Ch50 提供 engine state，不接管这一编译论点。提案在 Nautilus source-family `SF-2026-ARXIV-2604-14825` 后、“从逐 Kernel Launch 到 Persistent Executor”前插入下面两段；仅机制缺口，不复制 CNN 数字。

### 拟写入的两段 literal（尚未写入 Books）

按循环轴选择 tile，在矩阵乘法等复用已沿轴对齐的算子中最简单；数字 CIM 的阵列形状固定后，卷积等算子的同一 operand 复用却可能落在斜向 hyperplane 上，原坐标会掩盖可共享访问。编译器可以从 access matrix 的零变化方向识别复用，先用 pre-tiling 限制坐标变换的边界膨胀，再以合法 affine 变换把这些方向重新对齐；随后才合并虚拟复用空间、按有限 macro 数 post-tile，并确定实际 operand layout、搬运与缓冲。复用被表达出来与阵列能高效执行是两步，不应只按 operator 名或逻辑 tile 大小判断映射。

这条分支增加变换搜索、索引/layout 转换、缓冲与边界处理；提高 macro utilization 或降低一个 traffic 代理，不等于完整执行时间最短。[PolyCIM v1 §3–4](https://arxiv.org/html/2609.34351v1) 的有限数字 CIM 模拟与 CNN/单算子对照支持这种复用暴露，group/3D 算子收益较小，离线准备也不能从账本消失。合法迭代域与依赖保持还不自动保证浮点 accumulation 逐 bit 相同，完整任务质量和服务 SLO 需另验。原复用已对齐、搜索难摊销或目标阵列/数值检查不支持时，保留常规 tiling、im2col 或已验证 kernel，而不是为追求阵列填充继续重排。

## 3. ToolWait — Ch46 窄整合提案

采用 [精确 v1 HTML](https://arxiv.org/html/2609.34663v1) §II、§III-A–C 与相关已读测量限制；复用唯一停点必要干预，定点重读 §II 绑定配置，不补读全部 2077 配置搜索。固定 bucket 的单步成本主要为固定项；tool re-arrival 会改变 active membership 和步骤数，因此较少 padding 仍可能产生更多 decode cost。Prefix 管理的 128-token 粒度与 8192-token eager KV slot 不同；dummy 从同一 block pool 分配，能改变 FIFO eviction，slot 数字复现不证明原 generation 幸存。作者发现 hit counter 假阳性，实际 reuse 用 cached-token 数与 request log 而非仅 hit label 确认。

评价绑定：Rebellions RBLN-CA25 的单 instance/4 devices（其余设备不用）、Qwen3-4B/BF16、8192 max length、vLLM0.22.0+cpu/vllm-rbln0.11.1/optimum-rbln0.11.1/rebel-compiler0.11.1.post1/KMD3.2.2、eager cache、baseline buckets1/2/4/8 与8 slots。每 session 两请求、一次 tool wait，prompt800–1600、生成32–256，greedy；N=3–16，确认范围6/8与探索10不得混合推广。三个 seeds 配同 input plan，但 re-arrival 时刻由前次执行反馈产生，不是相同外生 arrival trace；生成 token 数匹配不证明字节/前缀 ID 全一致。扩 slot 干预连同 batch limit 改，不授 slot 单因素收益；response chunk 间隔不当逐 token ITL。Device-time 重建与 client in-flight proxy 的经验容差不是统计/硬件占用证书，88-token 外推低估保留；生产 SLO、一般最优搜索与真实 Agent 成功不采用，未复现。

实际差额与唯一 owner：`INFER-CONTINUOUS-BATCHING`，[Ch46](../../../../../books/part-05-inference-system/46-continuous-batching.md) “Trade-off”已拥有 waiting、KV pressure 与 prefill/decode 干扰，“Batch 饱和后，请求数不再是容量尺度”已拥有 bandwidth plateau。但正文尚未解释 **编译 bucket 固定步费 × endogenous re-arrival 导致 padding 和步骤反向变化，以及 dummy 与 cache 共池造成生存反馈**。Ch45/47 的 cache identity、物理 block 核心原则继续保留，不在此另推导；Ch49 的静态图只是 backend 条件。提案插于“Trade-off”末、“工程实践中的判断”前。

### 拟写入的两段 literal（尚未写入 Books）

请求在工具等待后重新到达，不能只把它当作释放了一个 batch slot：前次完成时刻与工具时长共同决定再次到达，服务配置改变后 arrival 序列也会改变。编译时固定 bucket 的 backend 又按可用容量向上取整，单步成本可能主要是固定项；等待把原本同步的请求打散后，即使总 padding 更少，也可能执行更多 decode steps 而更慢。配置应共同结算实际 membership、选中 bucket、步数、未缓存 prefill 与生成节奏，不把 padding ratio 单独授予效率结论；同 input plan 也不等于同一组外生 arrival 时刻。

若 padding dummy 与真实请求共用 KV block pool，补齐形状本身还会改变 cache 生存和重新 prefill 的压力；同一 slot ID 再出现不证明原内容仍在，应核 generation、实际 cached tokens 和请求轨迹，而不是只信 hit counter。[ToolWait v1 §II–III](https://arxiv.org/html/2609.34663v1) 的有限静态 backend 干预支持这些反例，不证明一般动态引擎都如此；slot 与 batch limit 联动、chunk 到达间隔和重建 device time 也不能分别冒充单因素因果、逐 token ITL 或硬件占用证书。增加 slots/buckets 会付出编译、驻留和调参成本，扩大池后 prefill 仍可能支配；条件不匹配或收益不足时保留原 bucket、保守接纳与已验证 cache policy，重新校准完整执行而非只追更低 padding。

## 4. PRISM — Ch70 窄整合提案

采用 [精确 v1 HTML](https://arxiv.org/html/2609.35569v1) §2/式2–6、§3 输入定义、§4、§6–7、§9，以及必要 A.3.3–A.3.7、A.5.1、A.6.1/A.6.2/A.6.4。§2 的排名命题是条件代数：同 workload/functional unit、固定 region/time、对各配置相同且正的 intensity 时，operational impact 等于 IT energy 乘固定正系数，故配置排序相同。变部署时各维 intensity 排序可异；加入配置相关 embodied 项后，只有较高能耗配置的 embodied 优势超过其 operational 劣势才发生 pairwise reversal。Embodied 总占比大不充分，pairwise reversal 也不保证改变整个可行集合的最优项。§6/必要 A.5.1 有数值 crossover 与 lifetime 敏感性，不把经验稀少率作普遍定理。

评价与反侧：ShareGPT/RepoBench/LongBench/SWE-bench Verified，Llama3/GPT-OSS/Qwen3/Gemma4；4L40/4A100SXM/8H100SXM、vLLM0.23、Harbor0.21。NVML board 能量实测，CPU/DRAM/storage 用 utilization 模型；非 Agent 按 latency/quality 可行 operating point，Agent 并发10并计远端 sandbox、以成功任务作分母；各任务 native score 与 chat pairwise judge 不混成同质量数字。地域46个为建模 proxy，不是这些地区真正测得同设备、容量或站点外部性；同配置各地域同 IT profile/可用性是关键假设。路由为2024两个 stream 对齐相对小时、H100 profile、24h/12 regions、20 capacity seeds、合成 lognormal 容量，非真实在线容量/网络 SLO。底层 energy/环境原数据未随文分发；运输/end-of-life 排除，六年 amortization、WUE/水应力/生态端点系数不确定。Precision/input-output 分布/batch/rate 随模型和 workload 不同，不以其任何汇总性能倍率作采用依据；未复现。已存在 fleet 的 embodied 是 sunk cost，论文 operational 路由目标不能转作新购硬件/生命周期规划的同一优化权限。

实际差额与唯一 owner：`PLATFORM-COST`，[Ch70](../../../../../books/part-06-ai-infrastructure/70-cost.md) “Unit Economics 与总需求反弹”已要求同 functional unit、lifecycle 数据和不确定性；“水耗…Dispatch”与“Energy Geography…”已有硬约束后的地域优化。但未解释 **为什么相同地点/时段的 operational 各维可以共享配置排序，何时 embodied 差额才能改变排序**；不能只因现有文字写“指标不互代”判完整 E，也无需重写已有功能单位/授权边界。相邻 Ch69 保测量证据，Ch71 保租户/资源约束；Ch56 保真正 routing authority。提案在 `SF-2026-ARXIV-2605-27480` 现有两段 lifecycle 核算后、“量化、batching、cache reuse…”前，仅插条件与反例，不写 PRISM 路由 headline。

### 拟写入的两段 literal（尚未写入 Books）

环境维度不能互相代理，并不意味着每次选择计算配置都需要不同排名。若 workload、质量/延迟可行集合及 functional unit 固定，同一地点和时段下的 operational impact 都写成 IT energy 乘各自相同的正 intensity，能耗更低的配置在这些维度中也更低；这是比例模型的条件结论。改变地点或时段后，各 intensity 的次序可以不同，能耗最优地域不再自然是碳、水或生态影响最优地域。应把计算配置排序和部署排序分开，不将固定部署的经验一致性扩大成跨地域代理权限。

加入配置相关的 embodied impact 后，设配置 i 的 IT energy 低于 j；只有 i 相对 j 的 embodied 劣势大于 `intensity × (energy_j − energy_i)`，对应维度才会偏好更高能耗的 j。关键是差额方向与 crossover，而不是 embodied 总占比大；pairwise 翻转也未必改变全候选最优项。[PRISM v1 §2/§6/A.5.1](https://arxiv.org/html/2609.35569v1)支持这条条件边界，结论仍依赖相同地域执行 profile、硬件寿命/利用率分摊与环境系数。新增核算与优化不确定性不能变成真实站点合规或生产收益；既有 fleet 的制造负担已发生，运行路由与采购决策还须分账。条件失配、迁移/网络代价未知或数据不足时保留原部署与范围估算，由调度 owner 在硬约束内另行验收。

## 5. MTP Performance — 仅报告

采用 [精确 v1 HTML](https://arxiv.org/html/2609.35188v1) §3.1–3.5、§4.3–4.4 及已读必要 profile 反侧；复用唯一停点方法与测量边界，不扩全部 kernel 附件。Matched AR/MTP 的主要 GEMM 每次调用没有变快，selected recurring-group cadence 还更长；但每 completion token 的重复调用和 graph replay 更少，完整生成仍更快。是 useful token progress 的摊销，不能从单 kernel 时长、kernel duration 求和或观察到的短辅助图次序直接推 GPU walltime/操作语义。

评价限定：同 Gemma4-E4B W4A16 target checkpoint、另 assistant drafter、speculative depth2、单 NVIDIA A10G、单 request；9 prompts×20 repeats×2 modes=360 clean benchmark，text/reasoning/tool calling 三类。AR 全部先完成再 MTP，时间顺序不能称随机交错；profiles 使用同输入但与 clean benchmark 分开，profiler 有扰动。只验证该 engine path 的局部性能归因，未提供批量/并发、跨设备或生产 SLO 普遍收益；命名 MTP 不证明 target 原生多 token 头，未复现。

实际 owner：`INFER-SPECULATIVE-DECODING`，[Ch48](../../../../../books/part-05-inference-system/48-speculative-decoding.md) “草稿模型和目标模型”末已明确一次 target forward 产更多有效 tokens，“Memory-limited Speculation”及 Drafter 分支已保额外 state/verify/acceptance 成本；`INFER-TENSORRT-LLM`，[Ch49](../../../../../books/part-05-inference-system/49-tensorrt-llm.md) graph capture/replay 与 backend 分账说明固定 launch/graph 成本不等单算子速度。Ch44 也把 iteration cadence 与 memory/batch 分开。论文提供一份可检验的局部 profile，未推翻摊销解释，也未提出新 execution/acceptance 机制。建议 **仅报告**：不是把整套实验标成“已有覆盖”，也不为“GEMM 不快但整体更快”的既有摊销机制新增一段论文摘要。保留测量范围与 kernel/graph/walltime 不互换的反侧，评分5不变。

## 作者完成范围与交接

五项作者必要证据与 actual-owner 处置已完成：3 个窄 I literal、2 个仅报告；没有本批新增的外部终态保留项。三份 Books 提案均未实际写入，不计 I/POST；root 仍需非作者 source→owner/literal PRE 后自行整合与检查。两项仅报告同样需独立终判，不能由作者自授接受。没有冻结全日分母、认证全日来源、改变 N1–19 或宣称整日报完成；未 stage、commit、push。
