# Feb27自然日新增首批准入校准

只own02-28；原152候选、原窗口/评分/连续§4冻结。题摘相同可复用为发现材料，旧generic EX不作为新准入裁决；Submitted/registered/API published均不证首公开。旧报告日期推导是冻结历史论述，不是本轮新证明。

## P1 CourtGuard 2602.22557v1

完整精确v1题摘：[本轮原abs](SUP_ABS_COURTGUARD.txt)，Abstract段完整；无撤回/纠错标记；Submitted Feb26只是提交。原screening-ledger-author的EX为“虽与AI研究相关，但公开摘要只显示局部质量/任务方法增量，不足以进入长期AI System候选分母”，未指出为何政策替换试验不改变设计。

准入链：静态finetuned classifier遇新规则需要重训 → 作者把外部政策作为evidentiary debate依据，并声称换Wikipedia Vandalism政策可zero-shot适配 → 若匹配控制成立，会改变安全judging是否应把政策逻辑耦合到weights、以及policy替换后如何再验收的选择。有限局部结果也可能修正具体判断，不按其benchmark/90%或主题映射准入。暂定潜力；必要首公开日期尚缺，不评分、不进入确定候选、不读全文绕日期。

## X1 ESAA 2602.23193v1

完整题摘在[本轮API原件](SUP_ARXIV_QUERY.raw)，identity2602.23193v1；标题/题摘可能暗示可靠性新增，故只做一次决定准入的core：[精确v1](SUP_CORE_ESAA.txt)。旧“局部质量”理由本轮不复用；actual正文的event sourcing/intent→validated append log→projection、hash replay与两case成功是否建立新的成立条件/失败边界待校准，若只是成熟组合且无新增说明则EX，不为不影响处置日期发请求。

## X2 2602.23005 Managing Uncertainty

完整题摘在[本轮API原件](SUP_ARXIV_QUERY.raw)；其四机制representation/identification/evolution/adaptation和epistemological/ontological分层只在摘要以治理术语重述，未指出新的执行机制、传播模型/可验证条件，clinical case改善也没有改变具体系统选择的增量。因此EX；不把临床场景机械改成系统贡献，不追不必要公开日期。

## D1 / D2 / D3

- Nano Banana2：本轮DeepMind [100item RSS](SUP_DEEPMIND_RSS_100.xml) Feb26T16:01:50Z即Feb27；02-27已有同家族原release且原spec缺口，旧日期归属不动，only同事件去重，不授现modified spec为发布时原件。
- vSONAR 2603.01096：[Meta dated核心](SUP_META_VSONAR.txt)原公开目录Feb27但same family ICLR旧OpenReview稿线索已在02-27精确隔离；目录日不证明首次公开/重要修订事件，保留必要事件缺口。
- CUDA Agent2602.24286：Seed page60原PublishDate Feb27、UpdateTime Apr23；[原项目](SUP_CUDA_PROJECT.txt)News两项datedFeb27是workdir/数据集release事实，不直接证明论文正文first-public。日期粒度现在无需时分秒，若作者dated项目/Seed可支持原稿发布日期可恢复；只做一次有限日期校准，不据Registered/Submitted推导。

## 首批实际非作者校准

root已实际读CourtGuard完整v1AB、ESAA/ManagingUncertainty完整Atom摘要及ESAA一次§2.4/3、§6–8 core。CourtGuard原generic EX撤销，受限潜力通过；ESAA/ManagingUncertainty具体EX通过。CUDA Feb27两项datedworkdir/dataset只证artifact publication，不证原稿firstpublic；若无新增兼容/正确性/评价约束即release贡献前关闭，不另造低分candidate。Nano同事件有效去重；vSONAR旧身份/版本保留，不搬日期。

## 最终有限差额的19项潜力（均必要公开日期未证，不评分/不收确定候选/不Books）

完整题摘：[本轮官方Atom包](SUP_AB_PACKET_20261008.md)，精确v1题摘各SUP_ABS_<suffix>.txt，CourtGuard另SUP_ABS_COURTGUARD.txt。原件表仅用于发现；API updated/currentVersion不替代精确v1，全部技术主张暂不采用。以下链是决定值得日期核验的具体增量，不是已成立的结论。

| ID / 原稿 | 原约束或判断 → 原文实际增量 → 若成立改变的选择 | 一次含糊准入core/反侧 |
| --- | --- | --- |
| 2602.22557 CourtGuard | 新安全政策需重训classifier → 外部policy替换下evidentiary debate并测OOD规则 → 重新比较weight-coupled与document-conditioned judging及换policy后的验收 | 首批root已校准；不授robust/regulatory或90%普遍泛化 |
| 2602.22345 Spectral Study | 只在输出后检测失效、压缩忽略activation几何 → streaming谱描述/轻量recurrent检测与outlier投影self-distill → 检测时点与dense压缩子空间选择 | 仅精确v1题摘；thesis不是自动EX |
| 2602.22594 CMDM | 整序列双向diffusion无法流式、AR累计错误 → causal VAE/forcing及从partially-denoised前帧预测的uncertainty schedule → 联合核codec因果与streaming采样接口 | 作者[项目](SUP_CMDM_PROJECT.txt)无公开日期，不能用CVPR2026反推 |
| 2602.22859 DPE | 固定混合训练不定位能力盲区 → category/step诊断、失败pattern可执行提示与Acc分段quota → 比较静态mix与诊断驱动的下一轮生成预算 | 一次core§3.2：200诊断样本、12类、Acc分段weights→quota及error summary；是真实数据选择接口，暂不授因果诊断或全年持续收益 |
| 2602.23295 ManifoldGD | prototype-centroid引导忽略类内变化 → hierarchicalIPC/局部tangent投影每步mode-alignment → generative prior数据蒸馏的geometry路径选择 | 精确v1题摘；不把“first”或FID数字当准入 |
| 2603.00165 ConFoThinking | attend正确区域仍可能坐标错、layer attention碎裂且query敏感 → 中间层聚合attention训练与concise semantic cue提取 → 分开where-to-look representation与coordinate generation验收 | 精确v1题摘；不授所有attention就是groundtruth |
| 2603.00171 AdaFocus | 不分任务统一crop、question/spatial intent漂移 → token confidence门控+semantic target→attention crop → 比较初次global pass与crop总体资源/质量取舍 | 一次core§3/表3–4：不是仅when/where术语组合，V*-Bench少crop却1h04m→1h18m反侧可改变gate成本验收；root实核发现阈值叙述的超过阈值crop与最终decision相反，门控含混未解，不采用4×或信心即正确 |
| 2603.00175 Infinite SA | 单步softmax高分辨率二次内存 → 多hopNeumann解释及fixed-dh辅助state线性principal-eigenvector近似 → 选择近似对象/多hop消费与尺度代价 | 精确v1题摘；不把32万tokens宣传当通用hardware结论 |
| 2603.15634 NextMem | text记忆重context、parametric记忆forgetting → AR autoencoder的reconstruction alignment/progressive latent substitution+量化 → 回读接口需比较重构与storage而非只text/weights | 精确v1题摘；实际公开日期仍未知 |
| 2603.08741 AetherFloat | 窄格式依赖AMAX/block scaling → base4/explicit mantissa/one-complement与AF8 QAT-first取消AMAX代价 → 数值格式/硬件逻辑/微调成本联合选择 | 精确v1题摘；不授所宣称面积/功耗/梯度保证 |
| 2602.23400 U-CAN | forget-sensitive与utility共享neurons，硬prune破坏保留 → 激活contrast选风险、retain范数utility校准、LoRA软衰减 → 不仅二元prune，需验forget/retain联合条件 | 精确v1题摘；不授不可恢复删除/隐私保证 |
| 2603.00166 AI Obedience | 复杂自然图像高分被当简单指令可靠 → 精确v1 VIOLIN的pure-color六variant、pixel-level deterministic oracle → 生成评价需另验低熵硬约束 | 精确v1题摘；当前Atom v2的mask/shape不当v1，generative prior因果/“intellectual abstraction”未采用 |
| 2602.23407 SRCode | security reward instance-level定位粗 → 安全repair pairs及token-level reward → 局部安全pattern的信用分配与全quality/security联合验收 | 精确v1题摘；不授selfreflection输出真值或无漏洞 |
| 2603.00172 MM-MEPA | 只关注被改图像内容的multimodal RAG → 不改visual只改metadata仍操纵retrieval/generation → provenance/metadata必须进poisoning威胁模型 | 精确v1题摘；这是安全信号，日期隔离而非EX，不采用91%/防御无效普遍断言 |
| 2603.00173 Summer22B | video架构被当主要收益来源、μP跨约束transfer未知 → 50Mclips训练局部观察架构差异小/geometry约束下μPtransfer → 比较dataengineering与架构预算、核缩放假设 | 精确v1题摘；不是因工业规模或title收录，不授普遍μP条件 |
| 2602.23235 GUIPruner | history等分辨率且unstructured prune破坏坐标grid → 时间衰减resize+结构stratified spatial保全 → 压缩需区分视觉token省算与坐标grounding人口 | 精确v1题摘；不授94%保真或端到端3.3× |
| 2602.23057 Affine Attention | sum-to1仅间接控制magnitude → input-dependent scale+bias改softmax权重 → 重新比较normalization与attention强度路径 | 精确v1题摘；不把consistent stability当普遍保证 |
| 2602.22351 DSKD | 原encoder SKD的sense替换不适decoder全词表生成 → teacher最后态选next-token/同义/反义sense原型并给student态hinge MSE，训练期用而inference不lookup → 区分预测位语义监督与输出分布KD | 原EX撤销；一次方法core SUP_DSKD_ONCE.txt 669–718/894–1085，明确有增量，不因摘要缺细节关闭；未审实验/证明 |
| 2602.22678 ViCLIP-OT | pair-level对比忽略batch跨模态relational结构 → 四similarity矩阵平均graph soft-target与unbalancedOT plan KL耦合 → 需比较分布匹配与pair监督/图先验可靠性 | 原EX撤销；一次方法core SUP_VICLIP_ONCE.txt 840–1155/1235–1320，有具体损失耦合，不按Vietnamese新场景准入；未审实验/OT梯度实现 |

## 其他8篇贡献前关闭：完整题摘均见官方Atom包

| ID | 具体EX理由（不是按局部/低分/已覆盖关闭） |
| --- | --- |
| 2602.23193 ESAA | 一次§3/6–8原证：schema验证/append log/投影/hash replay直接组合Event Sourcing/CQRS；两个case仅local运行/一致性，无Agent新增执行协议、特有成功/失败条件或改变设计的控制证据。§3.2 trace-first与§4.2 effects→append顺序不一致、完整effect可infer与future conflict detection也不支持新保证；不授事务原子性。root EX校准通过 |
| 2602.23005 Managing Uncertainty | 四生命周期/认识论与本体不确定性只在摘要重述层级治理，无新增传播/执行机制或其成立条件；clinical可行性不改当前模型/系统选择。root EX校准通过 |
| 2603.00159 FlowPortrait | MLLM多维judge+temporal/perceptual regularizer+GRPO组合用于portrait；摘要没给新增reward construction、judge盲区/成立条件或控制结果，方法组合与better talkinghead不足准入 |
| 2602.22492 Shallow BNN→GP | 新covariance/identifiability/Nystrom服务浅层Bayesian模型的tabular回归建模，没有提出改变当前foundation-model学习/训练/执行主线的具体关系；非所有理论EX |
| 2602.22624 Image Editing Planning | CoTplanning→区域网络→hint diffusion是理解/区域/生成模块链，摘要没有新增接口条件或原chain失效边界，复杂case质量提升本身不足以改变长期选择 |
| 2602.22743 Taesar | 将contrastive decoding的crossdomain context输出给既有sequence推荐器，无新的decoding机制/干扰条件；domain再生成改善推荐benchmark不足建立foundation-model训练/系统的设计差额 |
| 2602.22747 Uncertainty comparison | 共用同一有限predictive collection控制模型混杂的对照原则已具体，题摘却不报告哪种representational差异改变何选择/适用界；只说feasible/informative，不能把known like-for-like原则作为本文新结论 |
| 2602.22958 Frequency Tokenization | BPE词表ID按频率重排/varint后给zlib/lzma/zstd是无损文本压缩路径；未改model token语义/学习/attention或训练/serving存储约束。一般数据压缩收益不自动建立AI系统相关性 |

CUDA artifact release另贡献前关闭：原项目Feb27工作目录与数据集公开，只证素材publication，本轮未发现其相对原稿的新机制/兼容/正确性/评价约束；不评分/不新增candidate。其论文first-public原保留仍在。

后续root实际独核DSKD §4、ViCLIP §4.2–4.3公式9–20以及DPE step-scoring和AdaFocus gate/localization必要片段，19潜力/8EX准入校准同意。AdaFocus阈值内在混淆保留，不以准入核心证明confidence可靠性；所有19项仍在必要日期处隔离，无新候选证据/Books采用。完整六部分DAY已经root实际通过，依据与末检见supplement §3及README §6，不从准入通过继承完成。
