# Jan31 Batch5 — necessary exact-v1 evidence

2026-10-04 更新：root 已实际读取本批五项必要方法、匹配对照/直接反侧，五项仅报告处置独立复核通过。下段“尚待”为提交时过程状态，不是当前状态。

作者已完成以下五项的必要方法、匹配对照/直接反侧与 Books 判断；root 独立必要证据复核尚待。各项2+1+2=5，评分只取本项新增接口或条件，不取成熟原则/宣传规模。精确首次公开上下界沿用本日 DATES.md 的 submitted batch + schedule 下界/DataCite 上界；不是提交即公开。本批无撤回标记，后续版本号不作为历史 v1 的实验事实。原源均为 exact-v1 HTML，CORE_STANDARD 文件保留实际必要选择，不遍历附件，不运行 artifact/复现实验。

## 2601.22153 — DynamicVLA

- 原题：DynamicVLA: A Vision-Language-Action Model for Dynamic Object Manipulation；[v1](https://arxiv.org/html/2601.22153v1)，[实际原文](CORE_STANDARD_22153v1.txt) III-A–D、V-A/V-E、附录 C implementation、VI。
- 新增采用对象是两种执行选择的分工：continuous inference 在上一推理完成后立即再预测，不等旧 chunk 耗尽；latency-aware streaming 以预测时观测 t 与完成 t+m 对齐，丢弃已过期前 m 步，较新的 prediction 覆盖尚未执行的 overlap。旧动作已执行不能回滚。推导假设 horizon n>m；固定 m 示例不证明真实可变延迟/抖动下安全。
- TableII 在同360M架构下四种执行分支：都关 SR30.27/PL2.77/time9.86；只LAAS36.11/1.77/9.51；只CI39.72/2.61/8.84；都开47.06/2.50/8.53。合用的路径长度劣于只LAAS，不作全指标胜出。135M/1.7B/conv消融同时改变模型容量与时延，不能提出通用最优0.4B。
- DOM模拟Franka、真实Franka/PiPER，真实每实验20次，secondary arm固定发射轨迹但实际速度有噪声；success包括drop/timeout，time含失败终止，真实只报success而非完整延迟。越过workspace阈值abort算失败，不是控制安全证明。
- 训练32A100、perGPU batch40、约2周、AdamW 1e-4。作者inference RTX A6000约88Hz/1.8GB；precision/batch/concurrency/p95/SLO与88Hz的E2E闭环范围 Not Disclosed，不当deadline保证。限短中程rigid objects，不扩长任务/流体。
- III-B的插值方差和速度方向记号不一致（Normal variance写1−τ，线性插值会给平方；Aτ的导数与所写u符号相反），本次不采用数值flow公式，只保留上述可读执行接口。
- **仅报告提议**：MULTIMODAL-EMBODIED-VLA/Ch26 action chunk与L750–788 streaming、freshness、过期取消/执行前缀既有论证足以承载时间责任；本项是具体丢弃/覆盖策略与有限动态任务对照，不把该精确算法声称为已有正文覆盖，也不凭其参数配方强造长期差额。不同循环和horizon的具体收益留本日；无需Books diff。

## 2601.22094 — RefAny3D

- 原题：RefAny3D: 3D Asset-Referenced Diffusion Models for Image Generation；[v1](https://arxiv.org/html/2601.22094v1)，[实际原文](CORE_STANDARD_22094v1.txt) §3、§4.1–4.3/A1–2必要配置。
- joint RGB/pointmap generation由同spatial位置编码耦合，clean reference t=0 conditioning；reference LoRA与point-domain LoRA不同责任。Point tokens阻断text直连，RGB却可读text与point，其asymmetric attention不证明语义/几何完全disentangled，RGB-mediated路径尚在；pointmap是几何代理不是环境真值。
- 数据以rendered assets与200k subjects构造，GroundDINO、Hunyuan3D、FoundationPose、DepthPro等估计/筛选，maskIoU与LPIPS阈值不升级为真实pose正确。Flux1-dev，30k steps、8H800约8天、512×512、LoRA16、8等距reference views、text/reference随机drop .1。
- single-view预训练reference baselines与本方法8views的信息量不同；TI/DB per-asset调优另有训练成本，不称严格同资源。GPT5对3×3拼图0–10的结构判断、CLIP/DINO/对应keypoint数量都是代理，不构成3D物理一致保证；实际测试N、人评N、precision、inferencebatch/latency/concurrency/SLO Not Disclosed于必要段。不同PE/LoRA/textmask的反侧主要为qualitative，可支持接口可疑点，不唯一归因最终gains。
- §3 referenceLoRA all conditioning tokens 与A2 all tokens的作用范围文字存在差异，保留未决，不发布精确实现覆盖范围。
- **仅报告提议**：MULTIMODAL-REPRESENTATION/Ch23是模态、空间/版本接口owner，本项specific dual-domain recipe与渲染/估计条件并未证明通用semantic/geometry独立；不是书稿已有精确算法。局部条件生成对照留报告，无明确需采用的长期知识修正，不强制改书。

## 2601.22068 — SVE

- 原题：Making Foundation Models Probabilistic via Singular Value Ensembles；[v1](https://arxiv.org/html/2601.22068v1)，[实际原文](CORE_STANDARD_22068v1.txt) §4–5/Table1–5、C.3。
- 每线性权重分解，固定共享U/V，仅成员Σ重标与独立classifier heads；所有attention/FFN层单独处理，每forward重构dense W。可训练参数小不等于ensemble激活、dense计算或实际运行驻留小。所谓knowledge directions为作者假设，没有独立因果知识验证。
- 非负trainclamp与multiplicativeGaussian initialization分开：σ<1不能数学保证Gaussian样本正值/谱序保持，不采用原保证。随机初始化SVE较差，pretrained结构是成立条件；DINOv1/v2比较还改变训练，不把规模升级因果归给SVE。
- 视觉M4、SST2 M8、ARC M16；ARC引用基线成员3/5/10且部分published数字，非同budget。C.3称三random seeds mean±std，但学习率Single/Deep1e-4 vsLoRA1e-3等不同，不能取统一schedule宣称严格公平。
- 反侧：CIFAR100 SVE85.6/ECE2.1 vsLoRA88.2/.6，OOD AUROC81.6 vs82.8/FPR66.8 vs64.3；SST2 SVE92 vsDeep93.2，ECE2.8 vs4.7。精度和校准不是单调统赢。
- Table5 RTX4090/BERT/batch1/seq128，8members SVE175.2GFLOPs/21.9ms与LoRA同量级，single3.1ms。1%参数/理论memory overhead≠线上免费；作者承认当前parallel runtime未完全兑现memory saving，optimized sequential为future方向。SVD init3.5s是单次作者测量，precision、concurrency/tailSLO/E2E Not Disclosed。
- **仅报告提议**：TRAIN-LORA/Ch30拥有受限子空间适配；共享固定谱基底的ensemble是本项局部uncertainty/calibration方案，不建立knowledge-factorization长期真值，不保证资源pareto。现有低维更新/验收责任不需要被这一局部配方替代，报告留其实际反退与dense成本，不称具体SVE正文已有覆盖。

## 2601.22125 — Creative Image Generation

- 原题：Creative Image Generation with Diffusion Model；[v1](https://arxiv.org/html/2601.22125v1)，[实际原文](CORE_STANDARD_22125v1.txt) §5–7.5/S4.1；原决定core已保留。
- 5000 prior imageembeddings→768到50维PCA→Gaussian density，仅是作者的baseline embedding分布近似，不是图像真实概率/人类创意真值。Minimize logdensity在subject token/LoRA空间搜tail，CLIP anchor与每25steps MLLM yes/no检查分责；失败停止trial，negativecluster是用户选的undesirable区域，不是自动可靠审美判据。
- §7.5.1直接优化imageembedding很快失质；subjecttoken/adjtoken/LoRA的不同失败和色彩捷径表明低密度不等于有效主体变化。§7.5.4去anchor漂出domain；仅anchor时小fruit motifs仍可高匹配而主体变成人，checker可在图中定点截停，只有qualitative局部例，不是checker's完备可靠性或自动无adversarial。
- Kandinsky2.1，单A100、batch1、≤1000steps、AdamW1e-4、LoRA10；priorbatch500/5steps。每25steps Janus1.3B或LLaVANext还需decoder/checker调用。“50steps<2min”与ConceptLab300steps不是matched total wallbudget/独立seed统计，checker成本/precision/seedvariance/E2ESLO Not Disclosed。八subject paired三images/方法，人评>600users/>6000ratings但独立人口/抽样/重复相关性/盲法不明确；70.8/75%只作者偏好协议。alien无pullback五seeds曲线不证明Wundt理论或最优密度区间。
- **仅报告提议**：MULTIMODAL-GENERATIVE-PARADIGMS/Ch24拥有conditioning/guidance/quality验收，本项新增的是具体低密度目标与anchor欺骗反例；支持局部semantic-check必要性，不建立通用创新objective或checker保证，不把局部三模块组合长期普适化。无需强造Books diff，不称原具体配方已有覆盖。

## 2601.22057 — discriminator-driven decomposition/recombination

- 原题：Unsupervised Decomposition and Recombination with Discriminator-Driven Diffusion Models；[v1](https://arxiv.org/html/2601.22057v1)，[实际原文](CORE_STANDARD_22057v1.txt) §4/§5.1–5.2、B.2/C.1/Limitations。
- discriminator分辨internally single-source vsrecombined outputs，encoder/generator通过adversarialloss改representation；不是所有fakevsreal GAN，仅让重组更像自身单源。Fixeddecoder、randomlinear混合的synthetic实验隔离feedback，三seeds Mahalanobis²7.637→4.101近real3.99，同时MCC/MIG有改善；它支持recombination closure更好，明确不需要恢复真实generative factors，因此closure≠semantic/causal identifiability。
- image对照reimplement DecompDiffusion在同codebase，10k recombined samples计算FID against original distribution，FID是perceptual proxy不证明novel combinations正确。Falcor3D Table3 λ.005 MCC.707，λ.02 MCC.640低于Decomp.657而MIG.141更高；不同分解指标与λ不单调。带星模型三独立trainingruns，未带星published引用不当同protocol。
- 单V10032GB、batch16、20ksteps（Falcor40k）；C.1同时称Falcor128×128和allimages64×64，保留分辨率配置冲突，不授等训练FLOPs/精确执行recipe。训练disc用一次denoisedprediction、同source-noisyinput，可微proxy≠全采样真实generation；discriminator未conditiontime，噪声与mixedlatent不自洽是作者明确limitation，不称composition因果证明。precision/推理wallbudget/batch/concurrency/SLO Not Disclosed。
- 已读robot直接反侧：groundtruthaction warmup后才比较10pairedepisodes，warmup前常抓取失败，coverage不是tasksuccess/物理安全；本次贡献归表示重组而不扩VLA application链，不借35.8/73.8%增分。
- **仅报告提议**：MULTIMODAL-REPRESENTATION/Ch23拥有factorized接口；有局部closure与identifiability区别的实验贡献，但单源noise/one-stepproxy与λ反退使本次不采用通用semanticfactor接口，更不将机器人coverage授给WorldModel/执行安全。保留对成熟disc组合的具体受控边界，无需为算法名称强造Books改动。
