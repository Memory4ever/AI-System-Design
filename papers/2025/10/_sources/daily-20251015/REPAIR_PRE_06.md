# PRE06：诊断、物理偏好与模型控制

writer完整消费R11/12首次必要包，以下具体owner/完整两侧实际已读，不第二Methods。请仅审这四份正文/独立marker/本人note，未预写。

## I18 / 11512 / MULTIMODAL-WORLD-MODELS Ch25 / 2+1+2=5

文件 `books/part-03-multimodal-world-models/25-multimodal-world-models.md`，`semantic-body-binding: world-model-veracity-influence-sobriety-evaluation`原独立marker后、完整WorldReasonBench视频层面检查段前；不改原三结论分账。

拟正文全文：

物理评价还可先固定外观条件，构造valid/invalid成对视频，再比较生成模型在给定噪声时刻的去噪误差，而不只让另一个视觉裁判判断画面。[LikePhys的受限测量](https://arxiv.org/html/2510.11512v1#S3)把内部生成分布的偏好变成sensor，却不让ELBO surrogate的误差排序等于精确likelihood，更不证明模型会正确推进真实动力学。噪声耦合、tie规则和不同模型的预处理/guidance须一致记录；原文这些接口未全闭合时不拼完整统一排名recipe。合成场景、有限人评相关与受控外观也不排除全部视觉混杂，白盒noise接口又不等普通视频API可用。配对制备、所有噪声求值和独立人核均费；配对有效性、接口或真实控制支持不足时，保留分项人审、可信simulator/真实转移与Unknown，不由较低denoising loss批准物理定律、规划价值或安全动作。

<!-- source-family:SF-2025-ARXIV-2510-11512 -->

拟本人Review note：

- `SF-2025-ARXIV-2510-11512`：Popper，Daily2025-10-15补Oct14；整体消费Epicurus R11首次必要§3.2–3.3/4.1T1–3/§5/AppA/C/D2，2+1+2=5。只受控物理配对与denoising偏好sensor；不采ELBO排序精确等价/跨模型统一recipe，保noise/tie未闭、人评范围和全费。未第二Methods/代码/复现；PRE/SAVE/fullselfread/solePOST只本日canonical实际层。

## I19 / 11682 / MULTIMODAL-WORLD-MODELS Ch25 / 2+2+2=6

同文件，完整以`[Soft MPCritic 的有限仿真对照]`开头的段后、完整“刷新观测也不能只看模型报告的 uncertainty”段前。

拟正文全文：

价值头缩短规划后，还须固定它怎样跨想象步骤聚合：以候选序列上predicted Q的平均值作CEM排序，与累计reward加terminal value不是同一个优化目标。一个[受限接触规划分支](https://arxiv.org/html/2510.11682v1#S3)先训练低层本体控制，再由离线depth/proprioception latent模型提出高层增量动作，比较有限序列后仅执行首项、取得真实新观察再重规划。平均预测值可能平滑局部噪声，却不使learned Q无偏，相关时间误差也不能按独立方差相消；更长horizon已有反退，不能修成通用降方差保证。低层/数据/latent与价值训练、全部候选、执行与真实回归都计费；有限仿真和人工控制basevelocity的真机展示不认证完整自治或控制deadline。价值校准、动作支持或净质量失配时，保留较短搜索、原controller、显式代价/可信simulator与实测反馈，不让平均Q最好直接取得物理提交权。

<!-- source-family:SF-2025-ARXIV-2510-11682 -->

拟本人Review note：

- `SF-2025-ARXIV-2510-11682`：Popper，Daily2025-10-15补Oct14；完整消费Epicurus R12首次必要§III/Eq1–16/§IV，2+2+2=6。只mean-predicted-Q候选目标与真实首步反馈/低层控制分责；保方差打印不采、N6反退/人工basevelocity与全费，不授无偏Q/自治安全/SLO。未第二Methods/视频/实现/实机复现；PRE/SAVE/完整自读/solePOST只本日canonical实际层。

## I20 / 11715 / MULTIMODAL-WORLD-MODELS Ch25 / 2+1+2=5

同文件，独立`<!-- source-family:SF-2026-ARXIV-2605-24322 -->`后、原`### World Model 应选择对控制充分的 Modality`及完整引导前。

拟正文全文：

运动线索也可以从生成器的反事实响应中读出，而不先训练专用tracker：首帧加入彩色点，以编辑/未编辑条件的noise差加强标记传播，再用局部inpainting细化和颜色读取恢复位置。[Point Prompting的受限分支](https://arxiv.org/html/2510.11715v1#S3)读取的是以整段原视频为条件的生成结果，不是在线下一帧预测，也不赋予marker真实持久对象ID。颜色预处理、生成重排或refinement会移动内容，遮挡时沿用先前位置只是启发式，不是新观测；点变污渍、消失或附到背景都是直接失败。逐点完整去噪/细化、上采样及读取全计费，单视频数分钟不是实时tracking；不同分辨率结果不能拼为同协议优势。身份、轨迹或净预算不可靠时，保留原视频、专用tracker/人工点核和Unknown，不用生成标记的连续性批准物体永存、真实运动或控制真值。

<!-- source-family:SF-2025-ARXIV-2510-11715 -->

拟本人Review note：

- `SF-2025-ARXIV-2510-11715`：Popper，Daily2025-10-15补Oct14；整体消费Epicurus R12首次必要§3.2–3.3/4–5/T1–4/AppA/C，2+1+2=5。只全视频条件生成扰动的运动probe；保marker/遮挡/分辨率反侧与全部分钟级费用，不采在线观测/对象ID/实时性。未第二Methods/视频/代码/复现；PRE/SAVE/fullselfread/solePOST只本日canonical实际层。

## I21 / 11529 / PLATFORM-EVALUATION-SYSTEM Ch66 / 2+1+2=5

文件 `books/part-06-ai-infrastructure/66-evaluation-system.md`，独立`<!-- source-family:SF-2026-ARXIV-2601-05905 -->`之后、完整“同一个来源判断还应把证据层级与用户施压分成独立评价轴”段前。

拟正文全文：

幻觉诊断还可联合读取多份不同权限的信号：直接回答、CoT与反向推理分别产生候选，内部hidden状态与压缩推理表示经训练gate/cross-attention形成二分类sensor，而不是将一份自洽分数直接当真值。[一项受限检测分支](https://arxiv.org/html/2510.11529v1#S2)仍依赖judge/人工裁决的训练标签，多个judge同意或可读CoT不排除共同错误；hidden可视化也不证明唯一内部病因。原压缩token轴与融合维度未闭处不补成完整执行配方，AUROC不提供部署阈值下的误报/漏报或域移保证。所有候选生成、白盒读取、sensor训练及独立事实回归均费；标签、接口或阈值校准不足时，保留原回答/来源核验、外部factcheck和Unknown，不由融合多个相关信号批准事实正确与发布安全。

<!-- source-family:SF-2025-ARXIV-2510-11529 -->

拟本人Review note：

- `SF-2025-ARXIV-2510-11529`：Popper，Daily2025-10-15补Oct14；整体消费Epicurus R11与旧必要安全层，exact-v1 §2/3.1–3.3/T1，2+1+2=5。仅多路生成/hidden信号与标签/阈值权限分责；保Eq5接口未闭、split/seed校准缺口与全费，不采真实幻觉因果/部署检出保证。未第二Methods/实现/复现；PRE/SAVE/自读/solePOST只本日canonical真实层。
