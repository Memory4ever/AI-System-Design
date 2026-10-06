# Jan14 必要证据批次3（具名独立处置已通过）

仅处理已校准07475/07396/07820，原分6/5/5不变。各自公开字段见DATE_FIELDS_1/0，条件区间按no-advance-ID与周一20ET计划、注册上界联合，不把Submitted或registered等同first-public日志。未复现实验/核完整实现。

## [ARCQuant exact-v1](https://arxiv.org/html/2601.07475v1)

2+2+2=6。CORE_12_INDEX L146–170实际机制：离线校准排列与S，激活主量化后只对outlier求residual再同格式量化；权重复制对应outlier列而非另作weight-residual。配对扩展reduction维K+S，以一次同NVFP4 GEMM累加两个贡献。CORE_14 L398–406 AppendixD物理实现将16-channel主/残差块交错，offline权重严格匹配；逻辑concat不等未经适配可直接进入任意kernel。在线reorder/RMSNorm/两次量化与scale/packing有成本，weight RTN误差没有因此被完整补偿。

CORE_13 §4.1/Table1–3及CORE_14/15效率/限制：Llama3.1-8B、Qwen2.5 7B/32B/Coder/Math有限任务，W4A8/FlatQuant等不全同numericalformat；NVFP4各方法表也不是everymetric superiority。PyTorch2.9/CUDA12.8，RTX5090/PRO6000，128×2048 WikiText2 seed0校准，prefill batch4–32/len512–2048测量而非decode/concurrentServingSLO；ARC比uncompensatedNVFP4自身增加延迟与内存。训练预算不适用PTQ，校准/转换总预算未完整披露。vLLM部署未来工作；静态S/排序依赖分布，不授极端OOD无损。

§3.4 Eq3/4只分析激活scalar rounding/scalealignment（不授全GEMM输出/权重量化/task guarantee），正文MXFP8 E4M3与Table7 FP8名/位宽展示须保身份谨慎，不据此采用MXFP8严格等价headline。采用机制不依赖这个理论强说法。

actualowner `INFER-TENSORRT-LLM`：[Ch49](../../../../../books/part-05-inference-system/49-tensorrt-llm.md)1304–1328：现SVDQuant/Nunchaku高精度low-rank分支与fused路径，尚未给“把补偿存成同精度新增reduction通道”的替代。拟其precision/graph/kernel共同执行说明后最多1–2段，表明残差量化+weightduplication+matchedinterleave、K+S与校准/activation成本、能力/quality与硬件支持分账；旧高精度路径/dense/recalibration回退共存。待独立source→owner与锁，未写。

## [SVD-Cache exact-v1](https://arxiv.org/html/2601.07396v1)

2+1+2=5。CORE_13 L99–142：reference prompt一次SVD，固定右basis；Eq8/9在非零保留singular values时相消成F V_k V_k^T，故是固定参考子空间投影，不是对每个输入重新求最佳truncatedSVD。Principal projection用EMA估计未来，orthogonal residual直接复用；EMA是近似平滑预测，低能量不保证对输出无害。适用与reference支持和temporal evolution绑定。

CORE_14/Table1–3、CORE_15 L219–245：FLUX1dev50step和HunyuanVideo50step，DrawBench ImageReward/CLIP、VBench与accelerated-baseline PSNR/SSIM/LPIPS是不同质量对象。更大interval有退步；子空间两策略ablation是作者有限FLUX观察，τ≈.85不是通用阈值，wholefeatureEMA/reuse差不证明任意模型残差可安全冻结。Table3 perceptual reference为各accelerated baseline，不是FP原模型，“超过baseline PSNR”措辞不能采用。硬件、精度、batch/concurrency/完整SVD预处理+峰值状态费用未披露，FLOPs倍数与墙钟分开，不采headline速度；未核code。

actualowner `MULTIMODAL-GENERATIVE-PARADIGMS`：[Ch24](../../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)Cache误差状态/增量模块1090–1103已有whole/module/cachefreshness但未分同feature内部投影子空间与residual两种估计。拟该段后1自然段，固定basis身份/近似投影与两分支forecast-vs-hold/校准成本/quality以及fullcompute刷新或wholefeature方案回退。需确认长期具体gap后深入已读必要ablation，原5不改变。未写且不争用root待裁d3位置。

## [Reference Games exact-v1](https://arxiv.org/html/2601.07820v1)

2+1+2=5。CORE_13 L73–115 §3.2/Table1、CORE_14 L116–131限制、CORE_15 L245–282 E/F：5次baselinemajority比例为离散sample-consistency sensor，clarification条件只sample1且prompt改动，不能把前后差归为同预算内部uncertainty policy。Qwen full dataset/GPT500subset与human60turn共同grounding机会不同；lowconfidence/asking/answeraccuracy可不一致，不能把问了就当真实信息需求或humanbenefit。

F只对Qwen72B请求切片，由一个作者专家标taskrelevant并答；不相关请求也改写description提供更多信息，因此补充回复不是同信息固定action反事实。Relaxed accuracy把任何clarification算成功，不等实质goal完成；canonical三个选项MSP只对该选项人口，非通用校准。

拟标准仅报告：此color-grid有限行为反证与clarification内容质量有用，但不能授普遍内部原因/可靠问句controller或新budgetmatched选择机制。Ch66 actual1012–1028 confidence对象/新证据、2076–2092含糊条件应澄清而entropy不自证、riskcoverage独立动作政策已承载一般权限边界；这里不称exactbenchmark/5vote/F标签算法已覆盖，不为制造重复正文扩展。待非作者裁决。

最新处置（覆盖上述准备语态）：root 实际必要原源→具体owner通过ARCQuant6/SVD-Cache5两窄gap与Reference Games5标准OnlyReport。作者actual写ARCQuant Ch49:1316/1318+2619注、SVD Ch24:1100+1782注，jan01_v3仅实际顺读新段、邻接及末注POST通过；没有重审source/复现，source层真实复用root，日级Gate未授。ARC同格式补偿与packing承接高精度分支再交静态低秩；SVD固定reference投影/两估计策略承接模块增量cache再交motion-refresh，均保cost/quality/fallback。
