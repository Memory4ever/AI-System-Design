# 已过 Source 三项的单段 owner PRE

root实际Source：00557/00688各6、00733纠错深入5。只当前日期，不扩原稿附件。已读当前公共Books上下文与三处现正文完整局部/相邻交接，以下各一段+本人静态注申请，未授锁不写。

## 00557 / MULTIMODAL-EMBODIED-VLA / Ch26

文件 `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md`，完整左锚：

> derived label 必须保存 provenance。VLM 自动生成的 state-transition description 是推断，不是传感器事实；固定 clip boundary 可能切断任务；跨 embodiment action mask 可能掩盖坐标和关节差异。

右锚现完整“真实环境的采集扩容还受‘下一次从哪里开始’约束…”两段reset采集/部署不改。现有派生trajectory条数≠独立示教只在retarget情境，缺同步camera×同τ/action-frame匹配的具体view预算资格。之间拟一段：

同一物理示教也可以被同步多相机转换成多份view-conditioned样本，但N条trajectory乘V个views仍不是N×V次独立动作经验。base/EEF坐标的动作可跨视角保持，camera坐标标签则需以extrinsic旋转变换位移增量与姿态增量；只改变图像、不改相应动作坐标会破坏监督合同。这个分支免新增物理轨迹，不免多相机标定、同步、更多训练样本与计算。[有限diffusion-policy对照](https://arxiv.org/html/2604.00557v1)中近邻视角改善部署front view，top/side或更远角度仍可反退，因此多样性不能替代deployment-view匹配，也不由单坐标结果证明本质更优。多camera聚合算子的未统一记法不作精确recipe；标定、view或质量失配时，保留目标视角的真实示教、base/EEF合同与原policy，分别验独立轨迹数、view曝光、训练费用和实际闭环，不把数据倍数当fresh physical evidence。<!-- source-family:SF-2026-ARXIV-2604-00557 -->

本人末注一条：`SF-2026-ARXIV-2604-00557` — Daily2026-04-03；[exact-v1](https://arxiv.org/html/2604.00557v1)III-B–D/IV-A–B/TablesI–IV，2+2+2=6，仅trajectory×views分母/camera动作标签与部署视角匹配；保top/side反侧、校准人工/训练全費，不采PoE歧义精确sampler/独立新示教或物理安全，未核实现/复现。

## 00688 / MULTIMODAL-GENERATIVE-PARADIGMS / Ch24

文件 `books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md`，Masked generation开篇。完整左锚：

> 每轮对多个 mask 产生预测，再按 confidence 或 schedule 提交一部分。保守 schedule 一次只接纳少量高置信 token，质量更稳但并行收益有限；激进 schedule 接纳更多 token，早期错误会成为后续条件。

完整右锚保持原文：

> 并行揭示的风险不只来自错误 token，也来自同轮独立 marginal 抽样省掉的条件依赖。一条可分析的分支先为位置取均匀随机顺序，每轮都在同一旧状态上估各位置的条件熵，沿该顺序累加，达到规定的 entropy-sum 停止条件后共同揭示；首次使总和越过阈值的位置也包括在本轮，而不是筛除所有高熵位置。这让提交量随当前不确定性变化，但生成分布与正确答案仍是两个对象。<!-- source-family:SF-2026-ARXIV-2603-22248 -->

只新增单段，保后续条件理论/position confidence/ELBO/selection完整论证。差额不是再说并行mask，而是acoustic codebook×time训练目标与推理揭示层次的分责。拟一段：

masked target也未必是一条单codebook序列：直接text-to-acoustic生成可以对多个codebook的每个time entry分别遮罩，在同一time汇总embedding却由各codebook的head预测，并对全部masked entries计loss。这改变了训练监督的覆盖，不证明codebooks统计独立，也不取消推理时不同codebook的揭示顺序或guidance。[有限语音对照](https://arxiv.org/html/2604.00688v1)以同300K更新比较8-codebook mask/loss与初始化，支持局部选择；AR权重改作双向backbone仍需适配，更多loss entries不是相同compute，32step也不是完整费用。600多训练语言不等全测，ASR代理低于真实录音的WER更不授听感超越。codec、entry mask、heads、初始化、揭示规则与评价人口需共同绑定，计全部训练/采样/codec费用；质量或预算失配时保留单层目标、较保守顺序或semantic-to-acoustic分层路径，不由更密监督签发全部语音质量与端到端加速。<!-- source-family:SF-2026-ARXIV-2604-00688 -->

本人末注一条：`SF-2026-ARXIV-2604-00688` — Daily2026-04-03；[exact-v1](https://arxiv.org/html/2604.00688v1)2.1.1–2.1.2/3/4.1/4.3/Tables5–8，2+2+2=6，仅full-codebook entry mask/loss与推理顺序/初始化适配分责；保AR→双向训练、ASR代理/语言覆盖与全費，不授独立codebooks/真实speech超越或固定steps零费，未核实现/复现。

## 00733 / TRAIN-LORA / Ch30

文件 `books/part-04-training-system/30-lora.md`，完整左锚：

> LoRA 借用低秩分解思想，但通常不是先训练完整 `Delta W`，再对它做 SVD 截断。`A`、`B` 从训练开始就作为参数被直接优化。

右锚现完整“低秩因子本身仍可能占较多可训练状态…”MPS分支及其完整反側不改。现ΔW/因子压缩不覆盖permanent W rank/capacity和shape-only可执行分母，拟单段：

低秩增量与永久低秩模型还应分开：LoRA保留完整W₀，只限制ΔW；若直接以`U diag(s) Vᵀ`替代W，rank上限就约束模型本身的容量。通过QR让因子回到Stiefel约束后继续优化，得到的是该参数化的精确梯度，不是dense W的完整梯度，也未免反向计算。[有限compact-training证据](https://arxiv.org/html/2604.00733v1)中的“70B-class”只是无softmax/mask的简化attention shape单step，不能当作完整70B语言模型已训成；实际1.7B只替MLP，PPL明显退步且学习率与dense不同，不能将损失全归因某一设置或证明容量足够。QR还占较大step费用，低参数/optimizer存储不等整训练便宜。可学习质量、rank或执行预算不合格时，保留完整基座加LoRA、更高rank或full fine-tuning，分别验shape feasibility、完整模型quality和所有状态/重traction成本，不由能运行一个矩阵批准训练成功。<!-- source-family:SF-2026-ARXIV-2604-00733 -->

本人末注一条：`SF-2026-ARXIV-2604-00733` — Daily2026-04-03；[exact-v1](https://arxiv.org/html/2604.00733v1)§3/Alg1/4.1–4.4/5，2+1+2=5，纠错深入仅permanent rank参数化/真实模型学习/shape单step分账；保简化attention、1.7B质量/LR未匹配、QR/全部费用，不授8GB完整70B训练或dense capacity，未核实现/复现。

三单段PRE/窄锁待root实际核，actual后分别发完整邻接/本人注POST，不授全日。

root实际三PRE和当前Ch26 752–771、Ch24 510–520、Ch30 67–82完整左右锚通过，授各单段+本人注窄锁。View按核准明确extrinsic旋转变换位移/姿态增量，不加position offset。作者实写并顺读View Ch26 752–775/正文762+注2422、OmniVoice Ch24 510–526/正文516+注2683、SCT Ch30 67–87/正文75+注987，限定diff通过。root随后逐篇actual完整邻接/本人末注 POST PASS，三锁释放；Source/consumer/有限评价与全部费用吻合，可正式计3项，不授DAY。旧申请态只履历。
