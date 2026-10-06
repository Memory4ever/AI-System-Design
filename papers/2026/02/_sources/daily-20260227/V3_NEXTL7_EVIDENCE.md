# NEXT L7：最后已校准 named-tail 的表示/索引必要证据

作者必要审阅提案；不是 root Evidence/PRE，不更新 safe 分子。所有材料 exact-v1，已有同 ID 日期和完整题摘校准复用。原文坐标是 `V3_BLOCKS_2602.<ID>.md` 的 `[block]`，不是物理行。拟 I3/E4；贡献分数不由 Books 决定反推。

## [21402 FlowFixer](https://arxiv.org/html/2602.21402v1) — 2+1+2=5，拟 Existing

完整图像 embedding 相似度可能漏掉 subject 局部细节 → 原文以 keypoint correspondence 增量与 A/B 细节偏好作有限反证 → 必须用目标粒度而不是全局相似度验收。必要原文34–69/75–89/90–100：generated/reference VAE token 流、text-free LoRA192；训练 clean→SDXL 单次去噪并改变下采样/裁剪/参考颜色。Matcher 同时用于 crop 与 AKI，不能消除共享 proxy 偏差；85明确 copy-paste/对象放大会增加 AKI 而损全局一致性。91–94：FidelityBench300、每对5人，64.9%/64.4%局部偏好；Claude3.7 A/B 与 B/A 平均是同人口佐证，不是通用 ground-truth metric。50K step/B4/18450 Unsplash，训练预算非全面 matched，硬件/precision/全 runtime ND，crop/matching/LoRA/Poisson paste 均计费。采用局部/global 与 scorer/human 分账，不采用“AKI 认证所有细节”或全生成优越。

实际 owner：Ch66 78–116 的 EvalSpec 已明确 target behavior、eligible population、metrics/scorers、uncertainty；110 的 proxy 不能取得目标权威，112 的 reference encoder/尺度与人工锚点分责承载这一必要判断。局部 keypoint 配方不构成新长期 owner 差额，拟 Existing，无写书。

## [21499 Easy3E](https://arxiv.org/html/2602.21499v1) — 2+2+2=6，拟 Existing

单图编辑容易混同 shape 与 appearance → sparse active-voxel support/每 voxel latent 先编辑结构，再以法线条件生成多视角 appearance → 几何约束和外观 prior 的验收必须分开。必要25–39/48–85/90–107/112–116：occupancy 经 3D VAE；silhouette 为投影 proxy，采样结构再用 source forward-noised state repaint 未编辑域；soft mask 不认证严格局部保持。Frozen ControlNet/ERA3D + trained Ctrl-Adapter 的法线条件多视图是模型 prior，不是独立实测视角。60–70 的 correction 不作为可复用 exact solver/流形投影保证；采用接口责任只需机制和实际迭代事实。83：25 steps、2/4 velocity averages、源/目标 CFG 不同；runtime75s=结构30+纹理30+backprojection15，不能把 feed-forward 标签读成一次求值。100 assets、46人/10随机组，CLIP/DINO/LPIPS/FID 非几何真值；joint-guidance 的定性开关不拆开各机制因果。完整 hardware/precision/CI ND。

实际 Ch24 169–177 明确对象位置/外观接口分别校准与局部 mask 回退；248–254 明确初始 point identity/current movement、独立 reference appearance、派生深度非物理真值及多阶段费用。原文 sparse voxel 是有限实现实例，拟保 shape/appearance 分责 Existing，不增论文小节。

## [21514 Disk-resident ANN design space](https://arxiv.org/html/2602.21514v1) — 2+2+2=6，拟 Integrate Ch76

图节点近邻 locality 通常被当作 SSD I/O 优化 → page shuffling 与 page-level 消费规则有互补且并非都更快 → layout 与 expansion 必须联合评估，overlap 不能在饱和 SSD 下凭名取得收益。决定原文33–42/65–86/90–100/110–124/138–150：PS 令 graph-neighbors 共页；PSe 对已读整页算距离而不是只消费所需节点。PS 单独 SIFT 约9%减 I/O，PSe 增距离工作、IOPS 下降（SIFT690 vs791、SPACEV470 vs768）；组合在~98%recall提高有限 QPS。Pipeline speculative frontier 在48 workers 下加读而恶化；Pipe+DW 可高于原 base，却低于 DW-only，不能称所有 overlap 都坏。GIST 高维 DW 的 L10 recall66→50是直接反侧。Eq1 的 uniform expected-page approximation 不当 worst-case guarantee，OR=0也不外推。

Xeonw7-3455/128GB/4T NVMe、DIRECT_IO/libaio48workers/5runs，100M与GIST1M；PipeANN io_uring 禁用，同库测试不涵盖所有引擎；PS离线峰 RAM109.66GB，QPS/recall/建索引成本不同轴。实际 Ch76 212–235 已讲 graph/vector split、PQ/early stop 与 SSD latency，但缺同页读取的 layout×consumer expansion 互补及饱和下 prefetch 反侧。拟在 SSD 段一个窄段+ownnote，费用与低并发/原节点消费回退近文，等 PRE/lease。

## [21627 Tokenizing Semantic Segmentation with RLE](https://arxiv.org/html/2602.21627v1) — 2+1+2=5，拟 Integrate Ch23

更短 token 序列常被当作唯一表示预算 → RLE 的 start/length/class 字段合并或分解把预算转移到 vocabulary 与错误作用域 → 输出 schema 要联合验收 L、V 与实体 identity。必要26–35/42–64/85–108：flat start S² 词表分成两个坐标各 S，代价每 run 2→3 tokens；length 独立词表约束类型，超长 run 仍要拆。LAC 合 class×length 缩 L 却增 V；跨 N 帧 TAC class pattern 为 (C+1)^N−1，LTAC 又乘 S，不能称视频压缩免费。Class-wise/IW 使单个 class tag 错误污染整组 runs；IW 使用既给 instance 注释，不自动认证跨帧同一实例。L512/V3K或MTV32K、80/160 masks→640patch；RTX3090 上 L>4K 小 batch 仍 crash，不能由平均 RLE 倍数授全分辨率收益。视频/首帧输出对照非一致获益；作者 validation 选 checkpoint，与 Swin latest-only 不授全面公平优势。

实际 Ch23 135–149 shared token space 已讲 codec L/V/fidelity与 governance，204 的 image-conditioned mask codec 已讲 code/image/decoder identity；尚未具体承载显式 structured-mask 序列字段组合的 V 指数与 class-tag 错误作用域。拟 shared token space 附近一个窄段，只 representation contract，不收 ARIS/IPSC 领域性能或无预算的大规模分割保证。

## [21684 PF-DAG](https://arxiv.org/html/2602.21684v1) — 2+1+2=5，拟 Existing

粗离散码与连续动作并非互斥 → VQ prototype 的 mode classifier 给连续 MeanFlow residual 条件，最终输出不是量化 action → 对 mode 错路由、细动作与 NFE 分责。必要26–50/55–80/119–127：K64 VQ 先冻结、再 classifier+residual，one-NFE 是后者求值，前置 codebook/classifier/训练不免费。Table3 .72、去细化.01、去 mode.56；K8 .61/K1024 .58、kmeans .70，不证明 VQ 必需或越大越好。Ground-truth mode 的 total-variance 分解不赋予 deterministic mhat(o) 严格降 MSE，有限三 seed经验仍有效。18 simtasks 每200epochs挑 top5 checkpoints，不是独立 final-test model；真实4tasks所报比例无完整 N/CI。OOD/tactile dropout/high dynamics是直接限制。

实际 Ch26 187–189 已明确粗离散 planner→continuous细动作串接、粗粒度/码本/horizon/坐标、teacher-forced到预测 token 的 exposure、错误/陈旧条件与原单头回退；200还明确 mode gate 改连通前提而不授安全。拟 Existing，不为 one-NFE recipe 添段。

## [21723 LessMimic](https://arxiv.org/html/2602.21723v1) — 2+2+2=6，拟 Existing

物体 geometry 训练表示与运行感知易混同 → privileged distance-field/normal/tangent history teacher 经 DAgger 迁移到 depth student，背部接触不可见任务从视觉评估排除 → 转移成立域必须按运行可观测性而非 teacher 分数验收。必要32–43/49–65/75–91/102–117：DF距离本身仍随尺度变，不采所有 scale-invariant 证明；mocap physicalized参考、AMP/AIP仍为训练先验，reference-free部署不是无 reference学习。True-DF teacher长序列优于 vision表支持 privileged vspartial差距；real vision仅PickUp8/10+7/10，mocap10/10+8/10不能挪用，SitStand背部接触不可见故不测vision。Pretrain/DAgger queries、几何latent/目标机型适配均付费；硬件precision总训练budget ND。仅保该有限迁移界，不授无prior humanoid通用控制。

实际 Ch26 91–109 已明示 training-only privileged 3D teacher≠runtime observation，mask/teacher错误和geometry缺失时显式3D estimator留在runtime；同章159的MOCAP oracle不挪作learned pose。这里原文具体DF codec未建立超出上述观测/teacher消费责任的独立长期机制，拟 Existing，保不可见contact的具体负侧于报告。

## [21864 DynamicGTR](https://arxiv.org/html/2602.21864v1) — 2+1+2=5，拟 Integrate Ch23

同一个 graph IR 合法且完整不等对特定 query/consumer 最经济 → q-only router 从8个确定性图形/文字 representation选择模型相对效用 → semantic graph、render/serialize与消费预算是三层身份。必要20–35/42–61/65–91/112–121/152–155：5 Graphviz layouts/edge-set/list/matrix；“可重构完整拓扑”是原文针对给定规范的说明，不认证任意图像 label/权重。DeBERTa q-only router用7K小Erdos graphs、7algorithms、k10 probe 的 correctness与response length标签训练；score=log(1+100correct)−αlog(responseTOK)，不是指数 penalty。Argmax ties 用 multi-label BCE，不同 consumer API 需自己的 utility calibration。

三次temp.7测试、A100 router2.96h，8×7K×10调用/渲染/labeling在前置预算内；重设α复用缓存不免 router再训练。Graph大小3–30到OODn-hop子图，不等整巨图外推；答案verifier为这些有限图算法的trusted ground truth，不是通用知识真值。Table5 response更短非全任务：Conn router38.8 vsVneato7.7 tokens；GPT训练router跨Gemini相对native tokens+14.8，故不授 universal token saving。API精确版本/precision/完整input-image-render成本ND。

实际 Ch23 605–608 已分 IR可执行/重构/constraint/solve与renderer identity，未有 q→representation 的选择责任及 response-only utility 把 render/input成本漏掉的机制。拟其后一个窄段：保 canonical graph不变、consumer-relative标签、全面预算/固定format回退；等 PRE/lease，不为新router名字增小节。
