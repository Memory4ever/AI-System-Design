# Power-Aware / SlideFormer：必要证据与实际owner比较

## 16164 Power-Aware：2+2+2=6，标准原证＋具体已有覆盖拟稿

实际[精确v1 HTML](https://arxiv.org/html/2603.16164v1)§3–8/Tables1–4、§5/Fig1文字、§6直接反侧已读；因HTML Table2合并列，另[同v1 PDF](https://arxiv.org/pdf/2603.16164v1)实际完整p6图像核Table2/实验设置。没有遍参考外部附件/核代码或复现。LLaMA3-8B LitGPT续训约30Mtoken/SGLang推理，CV三模型合成输入预载GPU；四GPU/单node、每GPU报告，MI300X八卡node只用四卡。NVIDIA P0/AMD auto，200–700W/100步、AMD另750W，AMD<400W实际不服从cap。GPU-only100ms callbacks，只active batches；11epochs弃首，LLM warmup/JIT排除、推理预热；§5曲线再假设每node额外常数100W，**不是实测整机**。

原Table2实际为H10094GB/H200141GB/MI300X192GB、HBM2e/HBM3/HBM3和2.4/4.8/5.3TBps；NVIDIA共同700W/4卡/900GBps/P0，AMD750W/8卡node/896GBps/auto。只保作者配置，不用其名称推导器件规格已独立认证。NVIDIA/AMD的CV环境PyTorch2.8.0vs2.9.1/CUDA12.9vsROCm7.1.1，LLM只CUDA12.4+/ROCm6.3+，精确LitGPT/SGLang版本、每workload最终batch、sequence/input/output/concurrency/SLO、LM实用precision/quality、重复CI NotDisclosed。§6承认AMD启动可15min且数值格式未单独控制，不采软件/硬件单变量因果或低cap平台排行。

受测H100峰300/400W按任务不同，H200多数400W而pretrain500W；功率cap最优与吞吐最优不同，只支持固定stack/负载局部curve。更多GPU利用/吞吐不等任务质量、收敛费、完整服务能耗或全设备通用setpoint；HBM归因是作者推测非控制实验。拟采用命题仅“操作点需绑定实际workload/hardware/执行边界重校，功率和有效完成成本分账”。

已载Books适用合同/完整ROADMAP/PROJECT_CONTEXT/学习理念/WRITING_GUIDE/LS当前路由。实际Ch70 130–214/253–290完整局部与Ch69/71交接，另Ch63 242–260权力分责：Ch70 141–144明确GPU/host边界、验证费与局部测量不能授整机；185–194真实frequency/activity/state/admission反馈、尾延迟/quality合同与default回退；267 hardware operating point/利用率/wall-clock联合quality测量合同。Ch63仅预算分配/telemetry执行权，不另建PowerAware调度算法。sole `PLATFORM-COST`：现文已具体承载此可采长期论点，不声称包含精确cap峰数/作者设备排行。拟已有覆盖NC，不因已覆盖缩候选或降分，不强造正文/静态注；待非作者必要Source＋具体NC独核。

## 16428 SlideFormer：2+2+3=7，必要深入＋唯一Ch39一段拟稿

Power-Aware 的非作者复核：root 实际读 16164 exact-v1 §3.1–3.3、Table4、§5–8，核对 device-only measurement、额外 100W 假设、不同功率峰/软件和精度混杂；actual Ch70 130–201/250–279及Ch69/71开头交接实际顺读。原 Ch70 同时承载设备/整机范围、实际workload/hardware operating point重校、全壁钟成本和质量/SLO分账，NC不声称覆盖作者各设备精确峰值或单变量因果。6分标准原证和具体 `PLATFORM-COST` 已有覆盖通过，无Books新写、无需静态注或POST，不预授DAY。原作者PDF核Table2可复用；root未冒称自己视觉核该PDF或复现。

实际[精确v1](https://arxiv.org/html/2603.16428v1)§2.3/§3.1–3.3/Table1/§4.1–4.6/§5必要方法和直接成本读完，无需所有fig数值附件或复现。层GPU backward完成后gradient D2H、CPU Layer-Adam，同时GPU继续前层并预取；forward隐藏需compute≥H2D，backward需compute≥D2H+update。GPU cache unit预分配复用、CPU FP32 master全层、gradient/FP32→BF16/FP16转换是**层共享**buffer，不是模型梯度全消失；activation sliding checkpoint要offload/prefetch/recompute。NVMe仅activation/optimizerstate，参数留host以免破坏关键prefetch；GDS不删除传输/更新的依赖。LCE/FA/其他kernel和调度共同改变性能，不能全部归因layer unit。

Table1 Qwen2.5-14B RTX4090B16 η.66、B32η1.55，对低batch不是零offload费；更多NVMe换CPU省60–80%而吞吐降30–50%，smallmodel activation双程搬运更贵。基线latest具体版本ND、LoHan MSEvs真实CE/支持model和kernel差异不完全可归因，不采用“current optimal”或全硬件零开销。Setup：4090/7900XT＋Ryzen9950X/256GBDDR5，A10080GB＋dual6338N/1024GBDDR4；synthetic fixedseq1024/PyTorch2.7/CUDA12.5，GPU/gradBF16FP16、host masterFP32。AMD对应runtime版本、实际NVMe规格/完整计时warmup重复CI、训练data/steps/loss/heldoutquality、checkpoint恢复及整步SLO ND。123B一般max声明与256GB-PC实测只90B必须并存；不声称123B只需256GB/无参数host费。吞吐实验不是能力保持或训练正确性认证。

Actual sole `TRAIN-ZERO`，[Ch39](../../../../../books/part-04-training-system/39-zero.md)实际246–316完整offload→UVM/MemFerry→FullHostCache→CPU-authoritative LayerStream及Ch38/40开头交接。现文已承载layer ready/gradientoffload/bufferfree依赖和CPU版本/overlap，不复写同机制；具体差额仅**层共享buffer的容量代价与不同state的NVMe层级选择**。拟插在原“这条流式路径还需要把…buffer生命周期”段之后、原“因此overlap只在计算…”之前，原段和MegaTrain分支保留。

逐字PRE（一段，未写未授锁）：

> 层流式执行还可以让 GPU cache unit 预分配复用，并让 CPU 的梯度接收与 FP32→低精度转换 buffer 按层共享：省去的是多层同时保留的中间副本，不是 FP32 master parameters、optimizer state 或当前层的存储。共享槽位仍须等搬运与 CPU 消费完成才可复用；当 host 容量也不足时，activation 和 optimizer state 可以进入 NVMe，而将下一层关键参数预取留在 host—GPU 路径，避免更慢存储落到每层计算的关键依赖上。该选择会新增 pinned memory、CPU 更新、activation 重算和 I/O 费用；只有当前计算能覆盖这些延迟才隐藏成本，较小 batch 或带宽不足时仍会等待。有限合成负载中更多 NVMe 容量伴随吞吐退步，不能以最大可训练模型或 GPU 利用率批准质量与恢复语义；应共同验收整步时间、状态版本和训练结果，必要时回到普通 offload、HBM 驻留或多 GPU ZeRO。<!-- source-family:SF-2026-ARXIV-2603-16428 -->

静态来源注拟稿：

> - `SF-2026-ARXIV-2603-16428` — [SlideFormer exact-v1](https://arxiv.org/html/2603.16428v1) §2.3/3.1–3.3/Table1/4.1–4.6；层共享梯度/转换buffer与NVMe state分责，低batch隐藏失败、NVMe容量—吞吐退步及synthetic/基线loss与kernel混杂保留。host FP32 master与层版本不消失，GPU缓存复用须等搬运/消费；有限PC/服务器配置不授全硬件零offload费、训练质量/恢复正确性或生产SLO。未核代码或复现实验。

Source/PRE与窄锁均待root/非作者，不先写书或计整合。

### root 独立 Source/PRE（SlideFormer，2026-10-11）

root 实际打开精确 v1 HTML §3.1–3.3/Table1/§4.1–4.6，核对共享 buffer、CPU master 与 NVMe 分责；实际顺读 Ch39 offload 至 CPU-authoritative stream 完整局部，以及 ROADMAP 解析的 Ch38/40 开篇。原文仅移走 activation/optimizer state，不移参数至 NVMe；Table1 的小 batch 隐藏失败及 §4.4 的容量—吞吐代价支持该受限分支，吞吐与可容纳规模不授训练质量/恢复证明。现有段落已经解释事件/槽位生命周期；逐字 PRE 的新差额是按层共享梯度/类型转换中间副本及 state-specific tiering，不重复建立第二 owner。Source 与上述一段 PRE/静态末注通过；仅授 resume_mar18 Ch39 窄写，实际非写入者 POST 通过前不计整合。未核代码、复现实验或采用 headline 性能。

### root 实际非writer POST（SlideFormer）

写入后实际顺读 Ch39 279–323 完整 FullHost→LayerStream→原 overlap/回退，以及 398–428 含本人静态末注。新增 303 与批准 PRE 一致，旧参数/梯度版本及搬运依赖未删除；新增费用、有限合成对照、不同 state 层级和普通 offload/ZeRO 共存边界近文可定位。正文与本人来源注回对必要原证通过，释放 Ch39 窄锁；允许计一项实际整合，不预支整日报验收。未要求第二轮身份尾注更新。
