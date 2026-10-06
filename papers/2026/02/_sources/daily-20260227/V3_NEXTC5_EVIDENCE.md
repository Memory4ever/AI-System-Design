# 后续5项最小必要证据＋实际owner（root终态通过）

2026-10-06写后隔离复核：原21760仍残留Ch24正面调度正文和Experimental末注，与本包中心Disputed不符。本轮撤除仅属于21760的这一段及末注，前后其他家族保持不变；下述原方法、作者表格与明确重开条件全部保留，不用外围两分支并行原则重新吸收中心争议。

精确v1完整题摘已独立准入校准。原坐标为`V3_BLOCKS_2602.<ID>.md`中的block，不是文件行。只采用下面有限命题，无代码/复现/生产验收，不由下载或本文计完成。各项取得root必要证据与具体Books裁决后才终态。

root已实际核必要原文/具体owner：21760中心Disputed；21778 Existing Ch25 251–264；21779 Existing Ch66 456–460/419–436；21780 Existing Ch45 188–196/353–361/651–665。21788单窄段融入TRAIN-DISTRIBUTED-TRAINING Ch36 body585；root actual正文585/完整邻接576–600与自身末注2098 POST通过，ownnote同步、lease释放。五项安全终态，不能授整日完成。

## 21760 Accelerating Diffusion via Hybrid Data-Pipeline Parallelism Based on Conditional Guidance Scheduling — 2+2+2=6

[v1](https://arxiv.org/html/2602.21760v1)实际43–74、89–103、124、149–152。拟增量CFG两branch差异较小时引入pipeline阶段，以relative noise MAE近期slope提议τ1、固定k决定τ2，分时减少通信换质量。直接原文[71]：“During the parallelism phase, … converge to an identical value … τ2 is empirically fixed … k after τ1”；[73] larger k faster/lowerquality，不采同时更快无损。

中心执行规范有真实冲突，不是外围proof：文字[57]用descending t的warm-up[T,τ1]/parallel(τ1,τ2)/end[τ2,0]，但Eq3[72] τ2=τ1+k>τ1；Algorithm1[124] loop t=T…1，先if t≥τ1 warm-up，再else-if t>τ2 parallel，后者不能被满足。τcap被称整条curve global minimum却又声称online决定，未交代离线population/calibration怎样成为已知input；warmup[60]又称diff低，前[50/57]称首尾高。不照字面规范实现或授自动可行／optimal switch。只核此决定中心，不遍历附录证明。

有限表格不自动认伪：Table1[74] SDXL single16.49s→2GPU7.12，SD3 19.36→9.33，source149 3090 24GB/PCIeGen3/DDIM50/1024²/COCOval5000；precision、batch/concurrency、统计不全。Table2[101] fullCFGpartition9.24s、FID-to-original3.623 vs hybrid7.12/FID4.100，真实速度质量交换；Table4[151] k5→30，7.12→5.94s，FID4.100→9.191。FID-to-reference/groundtruth不同分母，不称singleimage物理或指令真值。

拟中心Disputed终态：当前矛盾决定唯一新schedule接口，有限作者table仍可报告但不替中心规范认证、不Books。Ch24实际228–232已有guidance两forward/不同branch身份与质量/总成本，不能仅取成熟两支并行制造gap。定点重开只需与descending/elapsed step一致的三段执行规范、实际branch exchange与τcap校准人口，以及对应可比实验；不要求全部附件或全修订diff。

## 21778 From Statics to Dynamics: Physics-Aware Image Editing with Latent Transition Priors — 2+2+2=6

[v1](https://arxiv.org/html/2602.21778v1)实际20–29、45–58、60–65、77–85、138–143。端点编辑对不约束过程，训练对source+text+reasoning后的64shared queries，用syntheticvideo中间6帧DINO/VAE压缩feature相对source的delta监督；queries/projections只由transition loss更新，diffusion/featureextractor按diffusion loss更新。推理从source/text实例化latent，不读真实future。t混合结构/纹理两表示，**flow采样时间不是物理时间**，featuredelta也不自成真实dynamics。

决定原文[28]：“boundary conditions … leaving the transition dynamics … underspecified”；[143]：“residual difference between … intermediate frame and … source image”；[58]明确两个gradient目标分责。Eq2的physicalintegral是任务解释，不是实现了有physical-law authority的simulator。

Table3[77] baseline61.26、same-dataset SFT61.79、reasoning62.31、visual62.41、combined64.86；visual-only Mechanics52.38低于baseline55.04。Table4[78] DINO-only GST70.16高于combined67.67，hardswitch LST62.08高于combined60.52；不采full所有维度最优或DINO只结构/VAE只纹理的因果定律。4A100/1epoch/LoRAr128/LR5e−5/B1每GPU/约12h；训练数据38k synthetic videos与LLM规则筛选先验，precision、完整sourcegeneration/judge费用与重复不全。PICABench GPT5现实感和KRIS知识题不是physical sensor真值。额外reasoning、video/双encoder/queries/监督与diffusion LoRA计总费。

拟具体Existing MULTIMODAL-WORLD-MODELS Ch25实际251–261：same-step与next-step目标分账；稀疏waypoint可端点好而中途冻结/跳变，沿decoder加中间帧监督使时间结构进入objective，额外解码/监督与外观过拟合成本，受限task非physics保证，inverse action recovery有假设。该有限image-edit验证在同一“端点≠过程、latent监督≠物理truth”论点内；不同latent/双stream recipe不必新段。若root判断query差额独立长期，须只保owner实际短差额，不建论文小节。

## 21779 Beyond Static Artifacts: A Forensic Benchmark for Video Deepfake Reasoning in Vision Language Models — 2+1+2=5

[v1](https://arxiv.org/html/2602.21779v1)实际39–58、62–72、75–86。最小core确认有finite负面入口，非仅三层新榜：静态QA SFT对空间时间grounding Level2可退，full带temporalQA与独立人注interval评价改变支持域。但static-only训练数据更少/类型不同，不隔离“更多temporalreasoning”唯一原因。

原[55]以time/artifact/region中二项问剩余维度；[58]人注验证start-end，1.5/3/5min按Level1/2/3，33kQA，必要身份与费用可核。Table3[71] Qwen2.5VL Level2 baseline23.8→static21.9→full41.4，LLaVA29→28.8→45.8；Table4 F2F差、highcompression下降保留。原[85]由blur损−8.2声称证实temporal而非static，这不成立：blur同时影响static高频cue，无frame-order shuffle／sameframes重排控制，不采unique temporal因果；open-ended49.1接近MCQ也不完全排除选择／语言捷径。TableR1[86]mixed54.4 vsstaged35.6／L3-only37.8，人口/目标budget不等；不同levels不能简单直接测“能力阶梯”。

Qwen2.5VL7B/LLaVANext7B、frozenVE/fullLMconnector、4H200/oneepoch/GBS16/LR1e−5/warmup500；precision、重复、LLMQA/judge/human总费不全。跨数据有限fake类型不是可靠开放域鉴伪或人类truth。

拟具体Existing PLATFORM-EVALUATION-SYSTEM Ch66实际456–458选项顺序/CoT/trajectory与原输出共同冻结，419–436真实过程证据和finalscore分开；Ch23 actual107的稳定/依赖/accuracy分账与random干预不唯一内部因果。采用仅finite“静态标签SFT对temporal题不能替时间证据验收；blur/MCQ成绩非唯一真实temporalcausal”验证，不新增主线理论。若root认为真正temporal支持域不被该正文承载，可窄PRE补评价而非领域深伪造部署章节；不把invalid blur强宣传当新纠错知识单独入选。

## 21780 XStreamVGGT: Extremely Memory-Efficient Streaming Vision Geometry Grounded Transformer with KV Cache Compression — 2+2+2=6

[v1](https://arxiv.org/html/2602.21780v1)实际30–64、66–68、71–81。关键cache机制不是全genericCV：FlashAttention不暴露fullattentionmap，用current frame grouped queries/headmean对historicalkeysummary作topk **proxy ranking**；每层temporalglobalattention之后剪中间frames，首/current完整保留，K/V同步相同indices，之后K-channel/V-token INT4（KIVI g64）并dequant attention。Pooling score不等真实attentionweights/几何关键性，且在当前attention**之后**剪，为后续frames的成本而非省当前完整求值。

原[32]：“optimized … kernels … do not provide … attention scores”；[39]：“Tokens from the first and current frames are always preserved”；[47] sameindices给K/V，长度预算约束须first/current能放下，不授任意resolution/frame budget。

Table7[74] video-depth三数据：prune+quant KITTI absrel .206 vsdense .198／δ63.9vs69，Bonn .073/94.3 vsprune-only .067/94.9；原[78]“quantization no additional degradation”不由表支持。3D7Scenes Table3 meanacc .142vs.132、NC .734vs.749，cameraScanNet Table4 .171vs.160 ATE，都非无损。518maxedge/gpool16/Lmax2k/INT4group64，A10080GB/50–1000frames；claimed4.42xcapacity/5.48xFPS未给统一单workload、输入帧与endtoendpercentile，不作通用数值。cache已限长仍有weights/currentactivations/output等预算，totalpeak不是永恒常量。selector/requant/scales/dequant/GPUgather都付费。

拟具体Existing INFER-KV-CACHE Ch45实际188–196physicalgather/proxyselector≠attention、保存row/head/布局身份与成本；353–375selector近似／budget和fullcache回退；651–665token×feature联合质量/物理layout/精读分责。该streaminggeometry有限实例支持同一kernel-compatible选择/联合精度预算，不新增cache原则；KIVI既有granularity不以新name加量化段。保retirement及irreversible错剪要回完整历史重算，不将后续FullKVfallback假定被删KV仍在。

## 21788 DHP: Efficient Scaling of MLLM Training with Dynamic Hybrid Parallelism — 2+2+2=6

[v1](https://arxiv.org/html/2602.21788v1)实际23–61、64–85。固定TP/PP，按tokenlength/mask/内存profile把longsequence与shortsequence BFD组成atomicgroups，再2DDP给每组整数RingCPdegree；Ring不受headdivisor的power2限制。dynamicCP/DP groups从pool复用，CPU排下一globalbatch与NPU当前batch overlap；不是全mesh/wt迁移任意动态。原[27]：“exclude … TP & PP … overhead … unacceptable”；[28] CPdegree任意positiveinteger；Table4[84]case有6/3degree实际示例。

[47]明确原NP-hard problem用两阶段**approximation**，DP只能给固定atomicgroups和costestimator的最佳allocation，不授全packing全局optimal／硬physicalmemory guarantee。Alg1backtrack startsK′+1/N+1 vs正文DP[K′][N]接口有offbyone，不照抄伪代码实现；不因此否认finite非power2group经验。内存模型group/rank state记法不清，实际perrankpeak要另核，不用Eq7签精确OOMadmission。

64Ascend910B64GB/8nodes/HCCS+100GbpsIB/InternVL与QwenVL2/4/8B/3datasets，GBS512，同步baseline调best；warmup5、next10steps平均是短runtime测试不是训练convergence／quality／longrunfault证明，precision与完整profilefee不全。Table1[76]GBS128 schedule468ms/compute2.04s、512 schedule921ms/7.32s，solver21–86ms不能冒整个schedulecost；Table2[77]16/32/64NPU schedule294/549/921ms，depend于lookahead足够，groupcachegrow不免费。EstimatorTable3[81]平均4.12–7.93%不等worstcasebound，case1/2有限1.17/1.14x，不能普遍8倍scale。

TRAIN-DISTRIBUTED-TRAINING Ch36实际575–606已有SP/CP区别、不同状态联合单轴、memory buffer与stages/topology、metadata/fallback；没有明确**heterogeneous sequences的dynamic integerCPdegree与固定TP/PP分界、group pooling/nextbatch lookahead费**。拟“ContextParallel buffer容量”前一窄段：groupplan只改变CP/DP，modelreplica/batch/序列mask/profile及communicationgroup identity绑定，packing+fixedgroupsDP非全局optimal，profile/921ms scheduleoverlap条件/oom保护及staticCP/SP回退近文。请求PRE／实际Existing。
