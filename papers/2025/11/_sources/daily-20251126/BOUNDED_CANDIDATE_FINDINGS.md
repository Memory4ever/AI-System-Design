# Nov26 有界题摘、日期与关键反侧追加

作者 Aristotle。本日窗口UTC[Nov25 01Z,Nov26 01Z)，续FIRST_CALIBRATION；未从其他日反推。Productivity单项原源及具体Existing/0写入已root通过，20潜力/必要反侧有限核验见POTENTIAL_INDEPENDENT_REVIEW，Carver日级见DAY_REVIEW。下列不是确定落窗候选或全证据通过。完整v1题摘均实际读，不用摘要缺实验细节关闭，不以名字未见造Books缺口。

## 收窄主题的完整题摘判断

原始*-abstract.html/.json及raw-narrow-exact14保留完整标题、摘要、history与当前撤回轻量检查。各当前页未见撤回不是遍历全部历史保证。

| 精确材料 | 提交原值(UTC，非公开) | 原约束→潜在增量→拟改变的选择 |
| --- | --- | --- |
| [SWAN: Sparse Winnowed Attention for Reduced Inference Memory via Decompression-Free KV-Cache Compression](https://arxiv.org/abs/2511.18936v1) | Nov24 09:41:24 | KV压缩重构开销→offline正交旋转/剪枝后直接attention，小dense buffer且runtime可调→需比较压缩率与重构/执行成本；50～60%只作者测定条件，不证明无损或全长上下文有效 |
| [Deterministic Continuous Replacement: Fast and Stable Module Replacement in Pretrained Transformers](https://arxiv.org/abs/2511.18670v1) | Nov24 00:55:14 | 冷替换冻结backbone扰动→确定annealed teacher/student output blend去除随机gate方差→异构operator替换可比较优化路径；single seed局部不因此关闭，不能泛称全模型稳定 |
| [CDLM: Consistency Diffusion Language Models For Faster Sampling](https://arxiv.org/abs/2511.19269v1) | Nov24 16:21:25 | 多轮refinement且常规KV不适用→consistency multi-token finalize+block causal finetune支持KV→须区分目标/attention改变与纯推理优化；v2Feb2026不借，倍率未授通用结论 |
| [Learning Plug-and-play Memory for Guiding Video Diffusion Models](https://arxiv.org/abs/2511.19229v1) | Nov24 15:42:23 | 冻结DiT缺可显式注入的参考知识→150M encoder、embedding低/高通filter与memory tokens，10K videos→物理/appearance可分指导是否只是局部现象待证，不因memory旧概念关闭；v2Nov27窗后不借 |
| [M3-Bench: Multi-Modal, Multi-Hop, Multi-Threaded Tool-Using MLLM Agent Benchmark](https://arxiv.org/abs/2511.17729v1) | Nov21 19:27:02 | 最终答案掩盖多工具graph/argument失配→signature embedding、similarity buckets/Hungarian一对一对应与分离metrics→评价一致性需要验证对齐授权，不因benchmark名即收/关；v2Nov30窗后不借 |
| [Orchestrating Dual-Boundaries: An Arithmetic Intensity Inspired Acceleration Framework for Diffusion Language Models](https://arxiv.org/abs/2511.21759v1) | Nov24 13:36:54 | 固定answer length与KV周期refresh使prefill/decoding双成本→adaptive length+diffusion jump-share→需要同质量/长度/refresh条件，不把46～162x当普遍能力；高ID/晚DOI收录不能直接判首公开晚 |
| [Fast Escape, Slow Convergence: Learning Dynamics of Phase Retrieval under Power-Law Data](https://arxiv.org/abs/2511.18661v1) | Nov24 00:21:17 | isotropic两维动态不足→anisotropic Gaussian power-law spectrum的三阶段/尾谱误差→canonical nonlinear学习理论可直接影响scaling解释，不能扩成LLM通用定律，也不因小模型关闭 |

代表性关闭：[Episodic Memory in Agentic Frameworks: Suggesting Next Tasks](https://arxiv.org/abs/2511.17775v1)，submittedNov21 20:47:41Z。完整题摘只是科学workflow human-AI co-creation，通过历史sequence匹配推荐下一任务，没有新增通用执行/可靠性成立条件；本项目AI for Science暂缓。不是因为episodic memory成熟而关闭。当前原页无相关撤回标记，日期不影响此处置，不另造date请求。

## cs.DC 有界标题定点四篇

raw-system-title-exact21含四个exact-v1完整题摘/原query，不是整月全文队列；这些已读方向需要独立校准：

- [Opt4GPTQ](https://arxiv.org/abs/2511.19438v1)：原submitted **Oct29 12:57:53Z**，不是按2511号改日期。SMB单thread write/VML loads/native ISA half FMA面向GPTQ/vLLM跨平台kernel选择有潜在具体delta；不能从最高84%扩全模型。DOI跨Nov26终点，只日期保留；v2Feb2026不借。
- [Low-Rank GEMM](https://arxiv.org/abs/2511.18674v1)：submittedNov24 01:13:52Z。按SVD能量选择rank/FP8表示可能改变质量预算的GEMM选择，不是保持exact计算的免费加速；原核心必要反侧见下。
- [ADF-LoRA](https://arxiv.org/abs/2511.18291v1)：submittedNov23 05:09:32Z。decentralized FL phase mismatch下交替只更新一个LoRA factor而每轮mix两者，以约束cross terms；潜在新增成立条件是因子更新/聚合耦合，不是FL应用映射就收。smoothness/通信条件尚未验证。
- [AVERY](https://arxiv.org/abs/2511.18151v1)：submittedNov22 18:42:04Z。VLM edge-cloud不是只沿depth split，functional dual stream将高频低分辨context与低频高保真insight分离，network/operator intent选择压缩；可能改变dynamic network下状态/带宽取舍，不能从LISA7B局部结果推全端侧。v2/3Feb/Mar2026不借。

## 首批关键条件和负证据的实际有限审阅

raw-needed-mechanisms22、raw-affected-controls23、raw-limited-methods24保存原v1位置/请求，以下只主张实际读到的内容，不授完整proof或全部methods/benchmark：

**Bias mitigation 2511.18635v1**：§3～6、L49～283实际核心。StereoSet intersentence2123项，gender/race/profession/religion计数242/827/976/78，不等人口。四techniques十models七families，hooks层/强度及editor同StereoSet train/dev8:1；held-out评估拆分权限不完全明确。SS下降不必向50趋近；LMS/coherence下降可能产生表面有利SS，ICAT结合两者。off-axis局部退化是可审负证据，但不能作严格No Free Lunch theorem、必然损害或因果disentangle；160runs/640evaluations不是独立模型重复。religion少样本及English文化benchmark限制保留，20.6/31.5不扩普遍保证。当前2026 journal收录与late Updated不改变本窗归属。

**Context/parameter equivalence 2511.17864v1**：§3 Eq2～4、Theorem1/2、Definition/theorem5必要段；fixed x/context、rank1 normalization denominator非零、output h_mlp各元素非零，patch依赖token/context；multilayer逐层记录目标再重算。不是单个patch对所有input的函数等价，更不是SGD/PPO学习等价。低精度division不稳定是原文条件，未通读附录proof或验证所有MoE路由。

**GAM 2511.18423v1**：§2 memo保留full-page原session，§2.2.2 planner vector/BM25/ID search+binary reflection；Table3模块/tool消融及Table4表明full-page F1变化伴token105.9→2379.82，不能授免费预算收益。long-baseline max-over-chunk scoring权限不等同相同test-time budget；RL公式不自动证明实际训练已使用RL。当前2026-03-29 issue#13问Figure2复现，无作者结论，不是撤回/本窗新事件；只保留实现复现限制，未复现实验。

**Low-Rank GEMM 2511.18674v1**：§3/4/5必要核心，99% energy rank、FP8储存/FP16 GPU计算，RTX4090 5warmup/5measure。误差1～2%与baseline<.01%不是相同质量，7.8x不能当exact替换；effective dense TFLOPS不能无条件解释成实际执行相同FLOPs。分解/预计算amortization未充分核，gradient误差/通用准确不据宣传成立，未有已核model-quality protocol。不借通用低rank原则评分，只保留质量/成本对照权限问题。

## HunyuanOCR 模型事件与普通PR分开

[HunyuanOCR Technical Report](https://arxiv.org/abs/2511.19575v1)，submittedNov24 17:59:59Z；官方vision发布字段Nov25但timezone未知，原v1.0 README当前newsNov25而不是历史冻结；repo createdNov18不等first-public，DOI createdNov26 02:50Z/Updated01:05Z跨终点也不能关掉原Nov25模型事件。v2Dec11不借。HF必要日期两次有限原生失败后停止，详SOURCE_CHECK。

实际v1 §3 nativeViT约0.4B+LLM0.5B/learned pooling MLP adapter/native aspect≤2028²/XD-RoPE；§5.2 reward按spotting IoU+normalizededit、parsing edit、VQA binary judge、translation softjudge、schema/length invalid0及过滤zero variance passrate；§C.1 RL batch512/N8/temp.85、**KL coefficient0**，不能从主β公式声称真实KL正则。parsing92.5→94.1 pre/postRL是局部结果，不隔离全部数据/阶段改变。

原README实际Nov28 vLLM inference bugs/systemprompt纠正，Transformers inference降级、评估TensorRT numbers可能不同。受影响执行backend/评价条件已深入必要片段(raw-dates-and-ocr13、raw-availability-ocr16、raw-ocr-rl-list18、raw-ocr-appendix19)，不把Nov28纠正算本窗新发布或采用pipeline error0/industry first/生产可靠性。潜在delta必须落到reward/data/执行backend条件，不因ViT/GRPO具名即收。准入/日期仍待root校准。

PR6 createdNov25 13:58:23Z、merged14:13:07Z，实际两文件patch只有pip --pre/uv安装文档。独立关闭普通文档变更，无新模型机制，不以PR代模型first-public；日期清楚不强造release family。

## 有限日期尝试与停点

FIRST_CAL八项+本追加七项+OCR+cs.DC四项，共20具名潜在方向各一次DataCite精确DOI全部200，date-ID.json原created/Updated/Available保留。多项Nov25凌晨字段只是元数据登记/更新线索，不构成正文首次公开上界，也没有可信首公开下界完全落窗；不授schedule精确09。Bias当前Updated2026保留不当v1updated。ODB Dec1收录、OCR/Opt4GPTQ Nov26跨终点既不能确认本日也不能从晚元数据断言排除。作者官方/项目历史query、两OpenReview403、GAM/VLM截止commits、OCR releases/README/PR/HF尝试都已有限，缺口不反复空路径。

定点重开只要对应v1官方公开公告/原版本public record，或作者真实带时区事件的首公开上下界完全在窗内；若没有则隔离为未采用潜在贡献，不记零贡献/全证据完成，不进Books。不要求root逐字全部附件；先核Productivity与代表性负侧、上述关键反证/日期权限，再判断剩余本日普通停点。Books目前0写入，只有Productivity做实际owner对读，其他不因名称缺位提差额。
