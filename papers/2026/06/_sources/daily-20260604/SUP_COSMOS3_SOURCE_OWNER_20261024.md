# Cosmos 3 02800 必要Source / actualowner / 最小两段PRE

作者supp_20260604_author；R45 exact-v1完整题摘/准入/Jun03联合日证/notice与A44 S2方法复用，不第三。正式拟2+2+2=6：有向AR/DM条件图、连续多模态clean/noisy角色任务及动作consumer跨生成/状态接口，稳定机制，不按omni标签、参数量、机构或榜单评分。为具体长期gap深入受影响部分，仍待首次正式评分独核。

## 精确原件及实际读界

HTMLfirst [exact-v1](https://arxiv.org/html/2606.02800v1)。沿用[完整S2方法切片](2606.02800v1.S2.methods.txt)，本轮只定点恢复[S4.2](2606.02800v1.S4.SS2.txt)、[E.4](2606.02800v1.A5.SS4.txt)、[E.5](2606.02800v1.A5.SS5.txt)及[S5.2](2606.02800v1.S5.SS2.txt)必要预算段，fetch实际exit0。大HTML2.95M不作全报告逐项队列；section匹配同时取得A3 synthetic dataset原件但未审、也不是必读。首次直接打印对象输出超过外层预算，随后从完整保存toolresult分段读所需证据，不以截断签足。

实际读S2完整；S4.2开头与4.2.1/4.2.2、4.2.5 RobotPolicy完整；E.4/T31/E.5完整；S5.2仅开头训练stack/早段loader（尚非完整loader/CP证明/所有infra）。未读4.2.3/4.2.4全文、A3、全结果/全部benchmark、图像像素或代码/复现。拟采用命题不依赖未读部分，支持及直接关键反侧足即止。

## 必要机制与边界

S2.1理解侧ViT与生成侧WanVAE分开；ViT jointtrain、generationVAE frozen，音频VAE frozen，不把共享hiddenwidth等同共享codec信息。action为ego/effector相对SE3 pose pseudo-action与直接graspstate；domain独立input/output projection，新sharedlatent不证明机器人低层动作互换、PID/actuation被辨识或动力学因果变量已证。S2.2 AR在前、DM在后，DM按cleancondition→noisytarget、vision→audio→action排；mode可只AR language/visionunderstanding，或DM视觉/音频/动作flow。动作FD以cleanaction预测noisyvision，ID反向，policy二者共同noisy；不是所有方向有等量证据，也不是输出同一语义真值。

S2.3两路独立LN、attentionprojections、FFN，AR Q只causal读AR K/V；DM Q双向读AR+DM K/V，AR从不依DM更新。共同的是attention操作/可交互图，不是所有参数一套或AR读取未来DM。因参数/输入/position等固定才有对应前向隔离，训练冻结集合另验，不能由mask证明原模型全能力保持。S2.4物理TPS缩放依codec压缩与采样率，gap15000经验处理伪影不是通用常数，不在本PRE另扩position主线。S2.5 Edge/Nano/Super不同规模，Edge当时laterrelease；不授当前artifact核验。

S4.2 rectifiedflow：xσ=σε+(1−σ)x0，目标ε−x0，cleanconditioning不计loss；各模态noisetime采样，modalityweightedvelocityMSE，actionloss×10用于normalizedvector量级，不等模态/任务效用校准。pretrain仅generation参数更新，reasoner冻结；此是明确阶段事实，不推广所有mid/poststage。74Ktokenpacking与resolution/framebudget不等全compute等量。Nano pretrain31.05T/1024GB200、Super17.86T/2048GB200；midtrain2.4T/1.9T同对应GPU规模，训练tokens/卡数不自行换算GPUhours或全生命周期能耗。Midstage action25%与transfer等数据配比/分辨率/noiseshift同时变化，不能把总提升唯一归mask/双塔。

S4.2.5 DROID pilot新增freshactionencoder/decodingMLP/embedding，5×LR multiplier；以proprio+3viewcanvas预测32个absolutejointpositions和auxRGB，15Hz。部署4diffusionsteps/CFGscale3、跳videolatentdecode、两RTXPro6000与Frankycontroller消费32actions。不是原相对pose伪动作直接无适配下发；部分生成video可不decode，不证明不需视频训练或完整deadline/实机安全。未采用§6.2.5排名或全闭环成功率，无需为这些未采主张扩所有bench。

E.4/T31是Edge/PushT：singlemodeFD/ID/policy各2Kstep，joint6K使每mode optimizationsteps相同；joint每step计算与tokens/完整pretrain预算并未由此认证相同。FD PSNR27.13→26.22反退，ID MSE1.11e−3→3.09e−4与policycoverage74.1→77.3改善。policy50initial×10rollouts不等独立训练seed；coverage是Tblock目标重叠代理非任意机器人任务成功，未给CI不得由小差额签显著/普遍正迁移。

E.5 Nano-Policy-DROID只DROIDtrain→RoboLab heldout；同一预测actionchunk在simulator执行后比predvideo，left/wrist PSNR23.19/17.33仅图像一致性、视角/遮挡人口，不把模型自洽当真值，也不与不同DROID FD条件作严格同条件优越。未证真实机器人安全、所有counterfactual正确、长期rollout或模型自己修复动力学。

S5.2已读开头HSDP+CP/onflycodec/异步checkpoint的一般配置。此处loop把Generator称EDM loss而S4.2明确rectifiedflow，保留文字口径差别，不照此认证完整实现recipe；本PRE不依它。完整training/inferenceprecision、eachrunbatch/concurrency、seedCI、端到端SLO/完整数据制备/teacher预算未在所读必要证据充分给出，不外推未知全报告未披。codec、map/pose/paired数据、双塔常驻/各阶段训练、modalitysampling、controller/simulator与独立质量回归全计费，不核实现或复现。

## actualowner与精确差额

唯一MULTIMODAL-GENERATIVE-PARADIGMS Ch24。actual先核Ch23 opening/sharedselfattention通用role/noisetime和Training/Serving职责、Ch25已有Cosmos简述/短note；后在Ch24发现现有2504-20996已真实承载AR/flow双塔，完整读1792–1830相关条件桥、H3 discrete/continuous和双塔及后20316组，故不另建Ch23平行owner。Ch23本身只应保表示身份/融合元数据，Ch25旧Cosmos段只保sharedinterface/owner安全概述，不迁全文。相邻Ch23/25职责有效复用，Ch22首试错路径后按ROADMAP正确Part02已读，不沿失败声称已读。

现有双塔分支强调共同交错上下文、可选cross-query混合，尚未承载**AR自含且只DM读AR的单向条件图、DM内clean/noisy角色切换FD/ID/joint与动作consumer具体适配**。这不是泛双塔再介绍或原gap已有覆盖，也不靠joint分数排序宣布优越。只在原2504-20996完整段marker后/20316完整组之前新增下列两段+本人trueH2注；无新授/未写，不预I/DAY。

完整上侧：

从已有语言模型接入视觉生成时，另一条分支是保留每层冻结的text block、另训vision block，让两者读取共同的交错上下文，再按当前token的模态选择对应输出。[受限双塔设计](https://arxiv.org/html/2504.20996v1)让文本继续消费AR目标、视觉消费连续flow目标，不要求全部序列成为同一个离散AR分布；不算另一类query的默认路径与额外计算跨塔query、融合两侧输出的可选路径，应分别验收。冻结语言参数不等图文条件下hidden不变，可选融合也不能无条件继承纯文本行为；共同attention的复杂度相同，更不抹掉新增参数、驻留和训练费用。Codec、模态路由、冻结集合、目标/数据配比与融合开关须共同版本化，分别回归语言、理解、生成和全预算；有限MMLU、caption代理或FID不能相互代证全部能力，特征对齐在较大模型上也可能反退。双塔、配对数据或质量/费用条件不合适时，保留原语言路径、独立视觉模型与显式条件桥，不由参数未更新或统一checkpoint签发全能力无损和净省费。
<!-- source-family:SF-2025-ARXIV-2504-20996 -->

拟增两段：

双塔还可以把条件化方向固定得更窄，而不让两侧都读取同一交错上下文：AR prefix 的 query 只 causal 地读 AR，DM query 则双向读取 AR 与 DM；两路各有 normalization、Q/K/V projection 和 FFN，只在共同 Attention 计算中按这张图交接。这样后续去噪状态不会反向成为 AR 的输入条件，但不证明语义无干扰、参数更新无损或整个系统共享一份计算预算。这条[单向条件化分支](https://arxiv.org/html/2606.02800v1#S2.SS3)还区分理解侧 ViT 与生成侧 VAE，不能因同属视觉 token 就交换其缓存、位置或 checkpoint 身份。

在 DM 内改变哪些 token 是 clean condition、哪些是 noisy target，可以用同一接口分别学习给定动作预测视频、给定视频推断动作，以及联合提出视频和动作；训练只对目标计算 velocity loss，模态噪声与 loss scale 仍需各自声明。这不是三种任务已互证真实因果或低层控制相容：相对 pose 的伪动作、grasp 状态和 domain projection 仍有各自单位与 consumer，机器人后训练还会重建动作接口，不能直接把共享 latent 交给任意 controller。作者在 PushT 上以每 mode 2K 步与联合 6K 步比较，动作指标改善而前向视频 PSNR 下降；RoboLab 把同一预测动作 chunk 真正送入 simulator 后再比视频，只支持有限视觉一致性，不签真实安全。双塔常驻、codec、配对数据/多阶段训练、各模态采样与动作消费/回归全计费；方向、接口、质量或总预算不合格时，保留单任务训练、显式条件桥和独立生成器/控制器，不由统一 checkpoint 批准全能力占优。<!-- source-family:SF-2026-ARXIV-2606-02800 -->

完整下侧（原20316完整组；不插marker内）：

<!-- semantic-body-binding:SF-2026-ARXIV-2605-20316:start -->
从头联合训练不是获得双向生成的唯一入口。已有 text-to-image checkpoint 在 image prior 值得保留、数据与算力受限时，
可以冻结 text encoder，只用 LoRA 与新增 text heads 把 `image time` 和 `text time` 分开；text→image、image→text、
joint generation 与 partial-text completion 由此成为同一二维时间状态空间里的不同轨迹，而不是把两种状态压成一个
timestep。Checkpoint identity 也随之扩展为 base revision、LoRA、text head、双时间 schedule 与 token insertion
规则。

薄适配降低训练成本，却把两条时间轴、跨模态接口和 schedule compatibility 变成新的故障面；小数据也不足以补齐
外部知识与复杂 VQA。分辨率、数据或 text task 越出验证域时，应回退单向生成器配独立 caption/VQA 模型，或进行
完整 multimodal pretraining。现有 evidence 只支持 exact-v1 的 matched-LoRA、有限 SD3/FLUX 与 joint/VQA 设置，
不证明这种迁移合同可替代大规模统一训练。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-20316:end -->

本人trueH2注拟：

- `SF-2026-ARXIV-2606-02800`：Daily2026-06-04补Jun03；exact-v1 S2、S4.2开头/4.2.1–2/4.2.5、E.4/T31与E.5，S5.2仅预算相关开头，2+2+2=6具体AR→DM条件图/clean-noisy任务接口差额深入。保独立参数与单向可见性非物理因果、pseudo-action/domain与DROID新动作接口、PushT每mode步数匹配非全compute匹配且FD反退、simulator PSNR非安全及全部费；未读全报告/附录/基础设施、图像或实现/复现。待首次Source/正式评分/actualowner/PRE及新授，不预I/DAY。

