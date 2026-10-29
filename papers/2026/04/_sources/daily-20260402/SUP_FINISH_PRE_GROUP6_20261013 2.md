# 六个既存后批Source的具体owner窄PRE

复用B9原resume_tail与STOP §9.39–41/44/46/48有效必要Source、§9.55正常paper-v1日门；不扩发现或附件。作者实际Ch26 16–35、Ch66 305–343、Ch82 46–89/171–193、Ch23 66–91、Ch4 40–66、Ch24 CFM232–262完整局部。每項一段+本人末注，root具体窄锁前不写Books，不采全recipe/性能/安全保证。

## SparseDriveV2 29163 — MULTIMODAL-EMBODIED-VLA / Ch26

在VLA输出contract/真实控制风险完整段后、SF2605-20811跨本体goal marker之前。

~~~~markdown
有限动作词库还可先把无时间path与按时间采样的velocity分别筛选，再组合成trajectory供scene-conditioned消费者重评分；固定空间步长与固定时间步长是两个坐标，不是全action space已获密集覆盖。[SparseDriveV2的受限对照](https://arxiv.org/html/2603.29163v1)支持这种coarse-to-joint接口，但marginal Top-K丢掉的path/velocity不能由后续reconditioning恢复，benchmark teacher的评分也不等真实环境效用。词库/teacher制备、全部coarse筛选、组合、重评分和仿真回归均付费；NAVSIM新版/修正评分不能混成同protocol涨分，comfort、overtaking等切片仍有反退，有限CARLA成功不授物理安全。覆盖、组合召回或实际feedback失配时保留原planner、较宽词库/动态proposal与独立controller，不从固定词库效率批准动作正确与真实闭环。
<!-- source-family:SF-2026-ARXIV-2603-29163 -->
~~~~

~~~~markdown
- `SF-2026-ARXIV-2603-29163` — Daily2026-04-02补04-01；[exact-v1](https://arxiv.org/html/2603.29163v1)S3.1–3.5/Eq1–30/S4T2–6/S5，2+1+2=5，仅Δs path×Δt velocity/coarse→joint recondition及丢失召回分责。保1024×256/128:64→20:20与v2 20:10、NAVSIM1192/136/8L20/10epoch、v2 EPDMS86.7/90.1异protocol、CARLA220/44/comfort与overtaking反退；全词库/teacher/训练/仿真费，未核代码/实机/复现。
~~~~

## FED-Bench 29697 — PLATFORM-EVALUATION-SYSTEM / Ch66

在内部幅度/方向/非目标保留SF2610-09493完整段后、跨模型crosscoder段前，是独立输出编辑测量消费者。

~~~~markdown
输出编辑的变化大小还可以相对指定reference归一，而不只奖励identity/background保持：用source到实际输出的感知距离除以source到reference的距离，检查是否接近预期编辑幅度，再与指令/保真分项并列。这个ratio比较的是同一metric下的幅度，不是表达方向或语义正确，同幅错误编辑也可通过。[FED-Bench的受限测量](https://arxiv.org/html/2603.29697v1)以经筛选的generated reference同时制备目标与instruction，因而须保共享偏差、crop/mask和reference身份；近零分母未闭合，no-edit软罚仍非硬拒绝。Reference生成/筛选、人审、距离/掩码与judge校准均付费，有限human agreement不认证每样本正确或无偏真值。参考、分母或消费者失配时保留绝对变化、原输出/指令与独立编辑验收，不把归一幅度升为通用质量Gate。
<!-- source-family:SF-2026-ARXIV-2603-29697 -->
~~~~

~~~~markdown
- `SF-2026-ARXIV-2603-29697` — Daily2026-04-02补04-01；[exact-v1](https://arxiv.org/html/2603.29697v1)S3/4/Eq1–8/S5T3/S6，2+1+2=5，仅reference-normalized edit magnitude与方向/保真分验。保747sources/2760paired/三人2AFC、σ=.5/noedit e^-2≈.135、近零分母未闭、generatedGT与instruction共享偏差、agreement.7386/.7700非真值/CI；全制备/调用费，未核代码/复现。
~~~~

## WybeCoder 29088 — AGENT-MULTI-AGENT / Ch82

在MiroFlow完整输入输出/协调费用两段后、「因此架构选择应先测」前，具体proof子目标协作分支。

~~~~markdown
可机器检查的子目标允许另一种协作交接：失败的proof obligation先返回冲突，使implementation修订，再重新提取目标，尝试借named invariant迁移已证子目标；只有全部义务成立后才重构整体证明。Name相同提供复用线索，不保证新目标语义身份，完整类型检查/重构不可省。[WybeCoder的受限方法](https://arxiv.org/pdf/2603.29088v1)支持此接口，却有sequential模型优于multi的切片，solve统计还含disprove，formal正确也可能未满足imperative任务要求或原spec的用户意图。全部模型搜索、VC/SMT/Lean、迁移/重构、judge和人工spec费都计入，calls×agents不等总token或墙钟。目标身份、spec或重构失败时保留原证明、顺序求解/较小workflow及独立任务验收，不由多agent数量、重用name或子目标成功批准任意repo与生产正确性。
<!-- source-family:SF-2026-ARXIV-2603-29088 -->
~~~~

~~~~markdown
- `SF-2026-ARXIV-2603-29088` — Daily2026-04-02补04-01；[official PDF-v1](https://arxiv.org/pdf/2603.29088v1)pp3–7/S3.1/4.1–4.2/Alg1/S5T1–3，2+2+2=6，仅CHANGE修method→new obligation/name复用→全重构分责。保solve含disprove/顺序Opus74.1/62.1、imperativejudge75.1→51.9/model-dependent与人工Heapsort，截图失败不冒视觉核验；全部搜索/proof/spec费，未核66页全附件/代码/复现。
~~~~

## Fisheye3R 28896 — MULTIMODAL-REPRESENTATION / Ch23

在VFM stitching完整接口/回退段后、「若消费者需要可命名」CBM前，镜头适配与label身份不混概念瓶颈。

~~~~markdown
镜头投影改变时，冻结几何encoder仍需声明输入与label坐标：把perspective图像映成合成fisheye，再把dense预测逆映回原采样位置，分别用原teacher预测、真实perspective标签或真实fisheye标签监督；三个人口不共享真值资格。层内calibration tokens可由camera类型选择，但classifier/mask也成为接口状态。[Fisheye3R的受限对照](https://arxiv.org/html/2603.28896v1)不由冻结权重保证旧输入exact兼容：post-softmax mask未移除token对分母的影响，mixed-global层又可间接读取已被适配的普通token。Projection、teacher/GT制备、token/classifier训练、额外forward及旧新消费者回归全付费，监督更多仍有depth/pose反退，合成投影不恢复未观测FoV。类型、坐标或混合输入失配时保留原encoder、独立标定/分支与真实标签，不由mask、t-SNE或局部小overhead批准无损sensor迁移。
<!-- source-family:SF-2026-ARXIV-2603-28896 -->
~~~~

~~~~markdown
- `SF-2026-ARXIV-2603-28896` — Daily2026-04-02补04-01；[exact-v1](https://arxiv.org/html/2603.28896v1)S3/Eq1–16/S4T1/F5–7/S5/S8及必要T3，2+1+2=5，仅T/T^-1、teacher/GT三人口与camera类型token接口。保Eq16分母/mixedglobal间接路径、pi3ADT SL+.087>SSL.075与MapAnythingSSL.766>SL.730、六perspective/三fisheye数据集/4GPU约20h及约6%runtime4%memory局部身份未全闭；全费，未核代码/复现。
~~~~

## Noise Pretraining 29034 — WORLDVIEW-WHY-MODELS-LEARN / Ch4

在local NTK预训练/holdout早停完整段后、Loss标题前；是同初始化不同消费者反侧，不声称所有模型通则。

~~~~markdown
初始化的收益还须按目标消费者分验，快速拟合坐标信号不等更好的inverse prior。[受限INR对照](https://arxiv.org/html/2603.29034v1)在同一sine/Strainer结构中以noise预训练共享层，新任务重置head并继续更新全部相关参数：它可提高信号拟合，却比原初始化或structured pretraining更差地去噪。这是优化适应与恢复bias方向相反的局部证据，不由NTK/landscape图识别唯一因果。十signal预训练、全部fine-tune/诊断及停点选择都付费；报告的early-stop PSNR与迭代点需要干净reference评价，不是部署未知干净答案的停点，video切片也非全胜。目标、noise或早停支持失配时保留原初始化/structured prior与独立holdout，分开拟合和真实恢复质量，不从低重建loss或少步数批准更好泛化、免费初始化或LLM迁移。
<!-- source-family:SF-2026-ARXIV-2603-29034 -->
~~~~

~~~~markdown
- `SF-2026-ARXIV-2603-29034` — Daily2026-04-02补04-01；[exact-v1](https://arxiv.org/html/2603.29034v1)S3T1–3/F2–10/S4/5/7.1必要，2+1+2=5，仅noise-init fitting与inverse denoising消费者反向取舍。保六sine层/ω30/w256/十signal5000、encoder+newhead均更新、拟合Uniform85.7/79.9但denoise23对SIREN28.3/Spectrum27.6、video不全胜/cleanPSNR停点非deployment；全制备/训练费，不采临床结论，未核代码/复现。
~~~~

## WorldFlow3D 29089 — MULTIMODAL-GENERATIVE-PARADIGMS / Ch24

在Gaussian paircost完整新段后、少样本fine-tune前。是CFM source与新attribute维度交接，不是world dynamics；保旧solver段。

~~~~markdown
下一层flow的source也可来自已生成的coarse数据，而不总是重从同维Gaussian开始：将前层raw volume上采样，按需加入noise，新增属性channel另填独立Gaussian，再学习到更细数据分布的transport。前层自产误差、attribute维度与真实训练source人口需要分开核，latent-free不等没有中间状态。[WorldFlow3D的受限方法](https://arxiv.org/html/2603.29089v1)还在host保留全volume，逐chunk计算并按overlap合并velocity后更新，不是常数费用的无限场景或普通mesh后拼接。CFM配对不证OT最优，原Euler方向口径未闭不照完整recipe，平均velocity不保无seam/严格geometry；分项质量和训练费仍有反退。Raw数据、各层训练、host内存/transfer、chunk合并及积分全计价，source支持、布局或费用失配时保留原noise-source/latent分支、较小volume与独立几何验收，不由连贯场景图像批准action-conditioned真实transition。
<!-- source-family:SF-2026-ARXIV-2603-29089 -->
~~~~

~~~~markdown
- `SF-2026-ARXIV-2603-29089` — Daily2026-04-02补04-01；[exact-v1](https://arxiv.org/html/2603.29089v1)S3.1–3.6/Eq1–7/S4T2–5/S5，2+2+2=6，仅actual coarse-source/newattribute Gaussian/hostchunk velocity合并接口。保time方向/denominator口径未闭、training到自产prior人口、Waymo96m²/3DFront2m²与1000chunks×5000代理、JSD.490>.480/fullFD103.20>89.47/费144>72；全volume/transfer/训练/采样费，未核代码/复现。
~~~~
