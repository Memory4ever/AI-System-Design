# 2026-04-10 单日来源补充

作者：supp_apr10_author；非作者reader：root。检查2026-10-14 BJT，只补2026-04-09北京时间自然日，冻结原70候选整行/评分/日期、旧窗口与连续原§4；完整baseline见同目录 `baseline-before-supplement-20261014.md`。不写共享索引/State，不stage/commit/push。

## 恢复与有限发现

当前AGENTS、RESEARCH_CONTRACT、REPORT_CONTRACTS V3、统一Prompt、来源使用说明/Daily/按需/arXiv主题、ROADMAP和State最新路由已独立完整读。原70有效身份/精确版本/命题按层复用，旧完成标签不授本轮Gate。旧587只是标题库存，不变逐AB/全文队列。跨日只定点同family去重及旧上界线索。

执行第一波搜索：`site:arxiv.org "Apr 8" "2026"`分别联合large language/inference GPU/agent memory/diffusion multimodal、MoE/RL/VLA/kernel、communication/distributed training/Transformer representation/attention KV/multimodal generation、agent planning/optimization dynamics/parallel GPU/accelerator quantization。每个有限query只看返回结果，日期不从搜索Submitted直接推断；相关完整题摘回官方精确v1。原日相同family不重评分，样例06628/06694/06515/06956/06970/07173与本日报07472/07609/07487/07645。

官方相关标题补检：起初 `/list/<category>/2604`是404，show=200也是无效参数，未用空响应证明零项。正确入口 `/list/<category>/2026-04?show=2000`用curl恢复CL/LG/AI/DC/CV/RO/AR/PL/OS/PF/IR/MA。只浏览已知Apr09批ID 06500–07362的相关标题（ID仅定位线索不代日期）。CL/LG/CV/AI均返回首2000项；DC388/RO976/AR227/PL138/OS37/PF69/IR512/MA348均页末。CL长脚本已续取完成；不称全分类召回。已知late具名07277/07279/07306/07328/07335/07340/07343/07345/07350与新命名MoRight07348从官方完整题摘判断，不遍历库存。

## 首批题摘准入与代表否侧

下面是完整官方v1题摘读后的中文概括与决定，不冒称证据完成。当前事件页无撤回/纠错提示；07277/07328/07343显示后修订，仍只采用v1，版本号本身不触发全史对比。

- [07277 Android Coach](https://arxiv.org/abs/2604.07277v1)：昂贵模拟器状态只执行一个action难以充分利用；作者在已观察状态抽多个action但不执行，以在线Q和PRM给长期值，再用leave-one-out组基线更新。题摘给两Android benchmark成功率和相同成功率效率比较。增量是实际transition与未执行候选值的监督分责，改变交互/critic预算选择，不把critic预测叫额外环境探索。2+2+2=6，root完整AB实际准入通过；必要证据见下文。
- [07345 Whole-Facility Power Profiles](https://arxiv.org/abs/2604.07345v1)：GenAI功率数据缺粒度/公开可复算口径；H100训练、LoRA微调与vLLM推理以0.1秒记录，再用bottom-up事件模型合成设施负载。增量是工作负载测量到设施推断的边界及公开测量案例，不是生产超配证明。2+2+2=6，root完整AB实际准入通过；拟Ch70具体已有覆盖。
- [07279 Mem3R](https://arxiv.org/abs/2604.07279v1)：固定latent state的漂移/遗忘压力；camera tracking用TTT更新轻量MLP fast weights，geometry mapping保显式固定token，两者解耦且可叠per-token更新。题摘有限500–1000frame/多任务支持参数与内存工作点。2+2+2=6，跨pose与geometry状态消费增量；待root准入。
- [07306 AlignPrune](https://arxiv.org/abs/2604.07306v1)：noisy-label高loss被错误当hard sample保留；用loss trajectory的Dynamic Alignment Score替瞬时loss排序，作为dynamic pruning插件，五benchmark/noise/prune ratio实验。2+1+2=5，增量仅数据选择统计，非所有训练系统；待核reference/排序含义。
- [07328 Sketch Learning](https://arxiv.org/abs/2604.07328v1)：想知道排除一组训练数据后输出而不逐次重训；stability假设下随机complex方向高阶导数对学习arithmetic circuit作local sketch，前算/推断/storage均poly(1/epsilon)额外成本，microgpt只初步支持稳定性。2+2+2=6，训练预算与删除后output-query接口改变，不授部署删除；待必要理论。
- [07335 TAMEn](https://arxiv.org/abs/2604.07335v1)：手持示范受形态、追踪及不可回放限制且缺真实contact recovery；跨gripper wearable、mocap/VR双采集模式、在线feasibility/tactile可视恢复，加tactile预训练→bimanual示范→human recovery闭环。2+2+2=6，数据/可执行回放与真实反馈接口增量，不以success数字准入。
- [07340 TC-AE](https://arxiv.org/abs/2604.07340v1)：高compression加latent channel可能坍塌；固定latent budget改ViT patch/token数量，拆两stage token-to-latent压缩，再joint SSL强化语义结构。2+1+2=5，仅codec表示瓶颈机制，需核固定预算对照与reconstruction/generation区分。
- [07343 Personalized RewardBench](https://arxiv.org/abs/2604.07343v1)：一般高质量偏好不能测user-specific RM；严格个人rubric chosen/rejected且两者general quality都高，人评确认personal区分，再检BoN/PPO下游相关性。2+2+2=6，reward/evaluation消费盲区，相关性不当然给普遍proxy保证。
- [07348 MoRight](https://arxiv.org/abs/2604.07348v1)：camera/object motion被同tracking信号混合且kinematic位移不处理反应；canonical静态view指定object motion，经temporal cross-view attention转目标camera，active/passive分条件，正向预测后果/逆向给潜在动作。2+2+2=6，view条件与interaction预测接口增量，causal wording待受控证据。
- [07350 Fast Spatial Memory](https://arxiv.org/abs/2604.07350v1)：LaCT全塑性fastweight跨chunk过拟合/遗忘使其常单大chunk；Fisher加权elastic prior围绕EMAanchor约束更新，3D/4D预训练后小chunk适应与camera-interpolation shortcut评价。2+1+2=5，仅fastweight稳定/可塑分支，不授无限序列保证。

代表否侧：ATOM07190完整AB是下载、模型派生、inference marketshare的生态快照，不改变本项目模型/Infra机制，关闭。PRIME07645同v1/同命题及原本日必要方法关闭复用。TRAPTI06955/PPFT06831原相邻日notes:163–164只有题摘组合关闭；root校准发现该共同理由不足，故仅重开二core如下，不用‘未证明privacy’当无贡献。

ConvApparel：[04-09官方Blog](https://research.google/blog/convapparel-measuring-and-bridging-the-realism-gap-in-user-simulators/)核心与[ACL March2026](https://aclanthology.org/2026.eacl-long.244/)完整AB同Good/Bad双agent、population stats/HLS/counterfactual三柱。Blog没有新的方法/数据/纠错，作为再介绍事件关闭，首发不搬到Apr09。root实际两页确认通过，不展开March历史。

## 必要Source与Books比较

### 07277

[exact HTMLv1](https://arxiv.org/html/2604.07277v1) §3.2–3.4/Eq2–4、§4.1–4.3/Table2/Fig4–7、AppD已读：执行rollout提供Q训练target（PRM+outcome），同state新action只预测Q；LOO在iid action/固定critic条件下抵消baseline均值，不修learned-Q误差或PPO clipping偏差。AppD.2只证constant-shift invariance，不能自动推出gradient variance下降：两动作等概率、Q=±1、score=±0.5时无baseline梯度恒0.5、方差0，而k=2的LOO梯度0/1各半、方差0.25。该反例不否定有限GUI经验或候选复用机制。UI-TARS1.5-7B，两benchmark、同RL时间预算三次run；硬件/precision/maxlen按A1待精确读回，不采用通用1.4x。

实际Ch32「Baseline Granularity」只写prompt-only V与group outcome rollout，随后flat GAE，不承载同昂贵已观察state上重采未执行action、Q-score与独立LOO baseline的这一接口。已读Ch31开头与Ch33主线相邻交接，拟在Ch32 baseline分支后两段最窄正文；Source/PRE与窄ownership待root。

### 07345

[exact HTMLv1](https://arxiv.org/html/2604.07345v1) §2.2/2.3、§3.1/3.2/3.5、§4/§5：NVML/RAPL读数不是外部全设施电表；0.1s采样不保证相同sensor刷新/瞬态带宽。微调随2/4/8/16node改变global batch，是weak scaling；online Llama3-70B/vLLM的finite1000prompt、rate/length/dataset与三seed，仅部分rate另持续3min采power；设施日内arrival/平均utilization和模型instance界是用户输入，超量请求被计unsupported而非实测SLO。10MW/1MW均模拟，不把其空闲余量当真实安全超配。前文研究/方法/关键负侧已够此命题，不扩代码/完整引用。

Ch70实际「Installed Power不是可部署AI Capacity」的power/拓扑约束→request活动与实测配置功率合成server/rack/site trace→相关性/设施附加功率/离线what-if与measurement分责完整承载（现280–300行）；67只拥有sensor/attribution交接。拟具体已有覆盖，无Books改动，root待核。

### TRAPTI / PPFT局部重开

[TRAPTI exact-v1](https://arxiv.org/html/2604.06955v1) III-A/B Eq1–5与IV-A/B定点：执行schedule固定，needed/obsolete/live tensor trace→容量无writeback→bank sweep；active-bank式假定contiguous packing+headroom alpha，gating由idle interval/leakage/wake成本break-even。CACTI/TransInferSim45nm、8bit、M2048是模拟；GPT2XL与DSdistill不仅MHA/GQA不同，还layer/hidden/FFN不同，2.72x不能隔离归因GQA。拟2+1+2=5准入受限bank/timeline复用与physical mapping边界，不把纯工作点升成新执行硬件。

[PPFT exact-v1](https://arxiv.org/html/2604.06831v1) §3.1–3.4/4.1–4.3定点：stage1更新client encoder/projector/server LoRA以learn continuous prefix；stage2冻client、server消费noised k-pooled embeddings与target labels，再部署同interface。不是仅一般隐私噪声模板；改变训练与推理的表示兼容/参数owner，拟2+2+2=6准入。无raw prompt≠无语义或output泄漏，uniform dchi budget对不同表示/有无重训也不自动同效；不因未有全安全证明排贡献。root待core裁决，不扩全部隐私证明。

### 07277 逐字拟正文（Ch32 Baseline Granularity后）

#### 同一昂贵状态的候选复用，不等于多条真实 Transition

当在线状态来自延迟高、不能可靠 fork 的 GUI 环境时，每次实际动作都让环境进入下一状态，直接收集同状态的多条后续轨迹很贵。一条条件分支先用真实执行轨迹训练 action-value critic，再在已观察状态上由当前策略独立抽取多个候选动作，只用 critic 估值而不执行；每个候选的优势减去其余候选 Q 值的均值。它以更多 action 采样和 Q forward 换取较少环境交互，也省去单独的 state-value baseline，却没有获得这些候选的真实 transition 或扩大已观察 state 的覆盖。过程奖励与真实终局结果形成 critic target，二者的身份和误差仍须分开，不能把未执行动作的预测值当作环境真值。<!-- source-family:SF-2026-ARXIV-2604-07277 -->

对固定 critic、同状态独立采样的普通 score-function 更新，leave-one-out baseline 不改变该 Q 代理的期望梯度；这不修正 critic 与真实 Q 的差异，也不消除 PPO clipping 的偏差。常数平移不变仅说明优势使用相对值，不足以证明完整梯度方差总会降低。[受限 GUI 对照](https://arxiv.org/html/2604.07277v1#S3)支持候选复用接口，收益仍受 critic 预训练、过程监督与部署外状态漂移限制；新增模型训练、采样、估值和 verifier 都计费，同在线 RL 时间预算不证明全部预处理费用已匹配。critic 失准、过程标签不可核或总预算不合算时，保留真实执行的 PPO；环境多 rollout 便宜时，也可保留不训练 critic 的 group baseline，而非让预测候选自签优化收益。<!-- source-family:SF-2026-ARXIV-2604-07277 -->

拟末注：`[Android Coach v1](https://arxiv.org/html/2604.07277v1) §3.2–3.4/Eq2–4、§4.1–4.3、A1/A2与D；仅采用已观察state候选重采/Q代理及独立LOO baseline边界，不采通用真实梯度无偏/方差下降或端到端1.4x，8A10080GB/BF16/受限GUI作者评价，未核代码或复现；必要证据深入及实际正文写后独立复核状态按完成后记录。`

### 2026-10-14 独核进展

root实际全部10具名complete官方v1 AB准入通过；07277/07345先通过，后8项直接HTTP/官方HTML全文读取，不依标题猜测。TRAPTI/PPFT局部core恢复理由通过进入必要证据，不称已验证。ConvApparel两页实际去重通过。07277 A1/A2实际读回：8A10080GB、BF16、parallel emulators=batchsize（不写固定8）；Table2三runs/同online RL时间预算，PRM与Q预训练/额外verifier成本不因此全匹配。root其D2与最后评价核验、以上逐字PRE/写锁仍待。

## 普通路由

拟入选9点资格及TRAPTI/PPFT准入、必要Source/Books比较仍进行；普通未读不标external。原70旧外部保留不扩全史；本轮新的正式六部分/实际写后与日Gate未授。来源、日期具体证据和实际独核结果在此一个记录继续追加，不建立平行JSON账本。

## 第二批必要证据与逐字 PRE

07277必要Source/PRE与实际Ch32写后独核已通过，作者回读84–90及source末注、释放owner，计1实际整合；07345必要Source及Ch70具体NC已通过。Seeduplex官方core独核支持关闭：native语义节奏/streaming披露，没有新的可核实现或评价接口；未披露spec/quant/A-B条件的相对数字不构成长证据。

### PPFT06831 → MODEL-EMBEDDING Ch12，连续输入两段后

[官方exact-v1 PDF](https://arxiv.org/pdf/2604.06831v1)物理p3–4/§3.1–3.4与HTML已实际对读，身份header Apr08/v1和原库存完整AB一致。DataCite单Updated Sep09不足以宣身份失效；采用复合公告批界支持Apr09首公开日，不改旧已有日期。Stage1 encoder/projector/server LoRA联合更新，stage2 client冻、server消费扰动embedding和明文label y再训练。必要评价§4.1–4.3只限ModernBERT/Llama与QA/局部inversion attacker，未展开全部隐私证明。Ch12原134–138的expert单anchor、冻结expert/base projector适配没有这一full-prompt k-pool→server前缀及阶段消费差额；Ch11/13接口相邻已读。

逐字拟文：

连续输入还可以承载经 client encoder 编码的整段 prompt，而不只是一份 expert 的单 token 摘要：把 token hidden states 按连续 k 个位置求均值，降低传输序列长度，再由 server projector 对齐到 decoder 的 embedding 空间，作为多 token prefix。此时文本 token ids 与检索用 sentence embedding 都不是 server 的直接输入；encoder、pooling 粒度和 projector 共同定义一份需要训练的接口。一个受限分支先联合适配 encoder、projector 与 server LoRA，再冻结 client encoder，只让 server 在扰动后的表示分布上适配 projector/LoRA；冻结 client 不等于 server 可直接消费任意版本的表示。<!-- source-family:SF-2026-ARXIV-2604-06831 -->

Pool 会丢失局部顺序和细节，扰动又改变 server 的输入分布，因此带宽减少与任务效用必须联合验收。[PPFT 的必要接口与有限对照](https://arxiv.org/html/2604.06831v1#S3)只支持所测 encoder/decoder 和 QA 人口下的适配分支，未传原始 prompt 不等于没有语义、输出或 label 泄漏；训练 server 仍接收 target label，局部 inversion attacker 的重构分数也不是完整隐私保证。Client 编码、两阶段训练、pool/projector 与完整 decoder 都付费，降序列长度不是端到端等比例加速。表示版本、精确数字/单位、噪声分布或效用不合格时，保留已验收的原文本/连续输入接口与更小压缩，并由安全 owner 独立决定跨信任边界的暴露资格。

拟末注：`[PPFT exact-v1](https://arxiv.org/pdf/2604.06831v1) p3–4/§3.1–3.4及§4.1–4.3；深入，只采用pooled continuous prefix及两阶段参数/消费兼容边界，不采全隐私保证、全费加速；必要证据与实际正文独核状态按实际完成记录，未核代码或复现。`

### AlignPrune07306 → TRAIN-DATA Ch27，per-sample loss-prioritization段后

[exact-v1](https://arxiv.org/html/2604.07306v1) §3.2/3.3 Eq4–7/Alg1、§4.2–4.4/Tables4–5、B2.5/7/9已读。窗口loss轨迹与均值reference Pearson比较不是梯度对齐；purity/distribution/cadence决定reference。B2.9关于排序独立的泛无偏说法不采用：有非零inclusion probability/正确校正才可讨论原目标无偏。CIFAR/ImageNet小视觉模型/3次有限实验，高prune可伤clean而益noise；root纠正Table5 pseudo-clean可比且部分更高，反退是随机noisy reference/purity扰动，不把pseudo与noisy混合。Ch27现173–179只讲方向validation与廉价loss预测，未承载轨迹参照选留；Ch26/28交接已读。

逐字拟文：

“高 loss”还可能来自错误标签而非值得保留的困难样本。一条受限 pruning 分支保存逐样本一段 loss history，与可信 reference population 的平均轨迹比较相关性，再按这种 Dynamic Alignment Score 选择 active set；它区分随训练共同变化与持续偏离的样本，不是在测真实梯度方向或因果贡献。[AlignPrune 的有限噪声对照](https://arxiv.org/html/2604.07306v1#S3)支持这一选择信号；估计的 pseudo-clean reference 可能有效，但不能把任意 noisy population 当可信 reference，reference 的纯度、领域、窗口与刷新 cadence 会改变排序，强 pruning 也可伤害 clean 数据。History、reference scoring、排名和恢复 active set 都计费；改变选择人口不自动保持原训练目标无偏，需另声明非零抽样概率与校正。Reference 漂移、独立 test 退步或净成本不合算时，保留静态 mixture、均匀采样与现有 loss 基线，不让轨迹相关性签发样本有用性。<!-- source-family:SF-2026-ARXIV-2604-07306 -->

### Sketch Learning07328 → TRAIN-DATA Ch27，attribution specification两段后、projected inverse前

[exact-v1](https://arxiv.org/html/2604.07328v1) §1.1/2.2/3.3 Def2、§4/5.1 Scheme/Th2及必要proof、§5.2已读。A为固定初始化/batch/randomness的训练arithmetic circuit，未来未知φ在预计算后才给出；复杂方向高阶forward AD Taylor +随机projection/MOM，稳定性要求φ∘A Frobenius高阶导数，不是通常连续性。Formal RAM exact-real/局部多项式，非无条件现实LLM finiteprecision；microgpt GELU/改Adamε、1000batch1names只proof-of-concept。现Ch27 influence/目标spec与JL曲率sketch未拥有整训练circuit的未来measurement query接口。

逐字拟文：

当未来要问的 measurement 尚未确定，逐目标保存 influence 排名仍不够。另一条理论分支把固定初始化、batch 次序和随机性的训练过程视为数据权重的 arithmetic circuit，预先沿随机 complex 方向计算高阶导数并保存 sketch；之后才给出 measurement 与一组 downweight/delete 权重，用局部 Taylor 近似预测这一声明训练过程下的输出。这里查询的是“若按指定过程重训，measurement 会怎样”，不是对已部署权重执行删除，也不自动提供真实样本因果归责。<!-- source-family:SF-2026-ARXIV-2604-07328 -->

[Sketch Learning 的条件保证](https://arxiv.org/html/2604.07328v1#S5)需要 measurement 与训练组合的高阶稳定性，precompute、query 与 storage 都支付随误差要求增长的额外预算；exact-real arithmetic circuit 的结论不能直接当作有限精度大模型工程保证。修改激活与 optimizer 的 microgpt 小实验仅展示可行线索，没有验证任意 LLM、强删除扰动或部署 unlearning。应共同保存训练随机性、权重干预、measurement、近似阶数与误差范围；稳定性不可核、扰动越界或查询会触发删改时，保留小规模匹配重训、原 influence 诊断与独立行为验收，而不是让预测的删除后分数替代实际删除或隐私闭合。

### TC-AE07340 → MULTIMODAL-REPRESENTATION Ch23，UniCom两段后、串行HYDRA前

[exact-v1](https://arxiv.org/html/2604.07340v1) §3.1–3.5/4.1–4.2、Tables1–3已读：固定latent f32,c128，patch32/16/8改变encoder读取tokens；内部compress¼sequence与末端bottleneck分段，iBOT EMA teacher/CLS masked patch辅助。A2/A1 linear probe比值不采MI或语义保存率。Table2 jointSSL使部分PSNR/SSIM/LPIPS退步而gFID好；ImageNet256有限AE50+16decode/DiT80ablation800full，多阶段非零费。实际Ch23 325–329已经拆spatial/channel与共享consumer，但未拆固定output latent下pixel-to-token读取和token-to-latent内部压缩。

逐字拟文：

输出 latent 的空间与 channel 预算固定时，encoder 的读取预算仍可变化：更小 image patch 让模型先看到更多 tokens，再在中间层压短序列、在末端形成同样形状的 latent。这把 pixel-to-token 读取与 token-to-latent 压缩拆成两个阶段，避免把增大 latent channel 当作唯一扩容办法；但较细读取仍增加 encoder 工作，内部压缩也会丢信息。联合 masked/CLS 自监督目标可约束表示结构，不证明 latent 无损或只含语义。<!-- source-family:SF-2026-ARXIV-2604-07340 -->

[TC-AE 的有限同预算对照](https://arxiv.org/html/2604.07340v1#S4)支持这份瓶颈位置取舍，却有生成指标改善而重建指标退步；linear probe 比值不是 mutual information 或语义保留率。AE、teacher、decoder 与后续生成 prior 的阶段费用须合计，固定输出 latent 与较少生成训练迭代都不等端到端更便宜。细节、重建或总预算不合格时，保留较粗 patch、原 codec/无辅助目标操作点或理解/生成双表示，分别验重建、理解与生成，不让固定 latent budget 给三个消费者互签保证。

### Fast Spatial Memory07350 → MODEL-LONG-CONTEXT Ch22，KV-binding等价边界段后、CRAM前

[exact-v1](https://arxiv.org/html/2604.07350v1) §2.3 Eq4–6、§3.1 Eq7、§4.1–4.2/Fig5/Table1与§5.1已读。LaCT更新后consolidation θnext=θ′−λF(θ′−anchor)，F为更新幅度/平方/SI update×drift的EMA代理，default SI；不采是真Fisher，streaming EMA anchor与慢learning模块区分。λF无clip可overshoot，不能授稳定硬界。12layer、8H100、128²、32+32views/32ksteps/136frameclips有限posedrender；全部基线有reported/reproduced/resolution差异，不授严格全优。Ch22 TTT写入目标与多更新时标没有importance-weighted anchor consolidation；Ch21/23交接已读。只拥有generic状态保留，不重复Ch25scene query。

逐字拟文：

单个 chunk 的重建更新可能迅速覆盖较早关联，因此写入目标之外还可增加一次 consolidation：先按当前数据更新 fast weights，再按逐参数 importance 把它们拉回较慢的 anchor；streaming EMA anchor 随历史缓慢移动，而 importance 可由更新幅度或更新与漂移的乘积作代理。这不是把多个 memory 模块设成不同学习频率，也不应把这些代理直接叫真实 Fisher。它用额外 anchor/importance 状态与修正计算换取保留—可塑性的可调接口，anchor 仍是参数参考，不是可追溯事实记录。<!-- source-family:SF-2026-ARXIV-2604-07350 -->

[Fast Spatial Memory 的有限重建对照](https://arxiv.org/html/2604.07350v1#S3)支持小 chunk 下研究这一分支，未证明无限序列、不遗忘或 action-conditioned dynamics。过强修正可能压制新信息，未受硬界约束的步长也可能越过 anchor；稀疏视图和 importance 失准仍会退化。训练、每 chunk 梯度、两份状态与后续读取都计费，更多可用 frames 不是所有场景端到端更省。需共同绑定 chunk 人口、更新/修正次序、anchor cadence 与 reset；历史变化、质量或预算失败时，保留原 TTT、较大 chunk、显式历史/几何 bank 与重观测，不让记忆正则取得事实或删除语义。

### TRAPTI06955 → INFER-GPU-MEMORY Ch54，片上生命周期两段后

必要§III-A/B Eq1–5、§IV-A/B已读如上；实际Ch54 132–138是eDRAM bit-sensitive刷新保护，不覆盖SRAM live set→contiguous bank packing/gating，Ch53/55相邻已读。

逐字拟文：

若片上 SRAM 允许分 bank 休眠，同一 lifetime trace 还可用于选择装多少容量、何时关掉空闲 bank：先按固定执行 schedule 的 needed/obsolete tensors 求 live occupancy，再在无 writeback 的容量约束下扫描 bank 数，以足够的 active banks 容纳当前 live set；只有空闲时间超过 leakage 节省与唤醒能耗/延迟的 break-even 才值得 gating。这一分支与 eDRAM 的 bit-sensitive refresh 不同，减少 active banks 要求真实地址能按假定连续打包；逻辑占用降低本身不证明物理 bank 已可关闭。<!-- source-family:SF-2026-ARXIV-2604-06955 -->

[TRAPTI 的必要模型与有限仿真](https://arxiv.org/html/2604.06955v1)依赖固定 schedule、headroom 和 CACTI/TransInferSim 参数；两个 Transformer 的层数、维度与 FFN 同时不同，不能把能耗比唯一归因 MHA/GQA。Trace、mapping/搬移、bank 控制与唤醒全部计费，碎片、动态 shape、schedule 改写或时限失配会使离线 bank 数与 gating 失效。模型没有证明制造硬件或生产 deadline；这些条件不可核或净节省不足时，保留保守 SRAM 容量、固定 active banks 与原 allocator/执行 schedule，而不是由理想 live set 批准物理掉电。

上述新增Books拟末注统一只留各自exact-v1、上列必要section、采用边界、实际审阅状态与未核代码/复现，不写过程锁历史。待root必要Source/actual owner逐字PRE与窄ownership后才写。

### Mem3R07279 → MULTIMODAL-WORLD-MODELS Ch25，ZipMap两段后、实体关系查询前

[exact-v1](https://arxiv.org/html/2604.07279v1) §3.1–3.4/Eq3–10、§4.1–4.5/Table3–4已读。Camera prior由fastweight MLP读取，decoder posterior pose作为TTT alignment target；显式geometry tokens另融合当前candidate与旧state。Eq10外部G_t乘两部分，不照写canonical convex更新全recipe。26dataset/CUT3R stage 4–64views，32H100预训练/10h；evalA10040GB质量、BlackwellMaxQ512×384效率，不混同。有限50–1000frames/Sim3 ATE不能证metric truth；Table4有quality反退与TTT3R addon不能单归因。现ZipMap731/733只camera-ray查询同隐式scene function，未承载camera隐式与geometry显式的不同写入分责；Ch24/26邻接已实际读。

逐字拟文：

固定容量场景状态还可按消费者拆分，而不让 pose 与 geometry 争用完全相同的更新接口：camera tracking 从 fast-weight MLP 读取 prior，经当前 decoder 得到 posterior pose，再在线更新二者的对齐；geometry mapping 则保留显式 tokens，把当前候选与历史状态门控融合。它用可更新参数承载相机关联、用显式状态承载几何，增加不同状态的同步与更新责任；posterior 是模型估计而非新 sensor 真值，geometry gate 也不证明历史一定保留。<!-- source-family:SF-2026-ARXIV-2604-07279 -->

[Mem3R 的有限重建对照](https://arxiv.org/html/2604.07279v1#S3)支持这一双记忆分工，却只在有限视图与长度检验漂移/重建，部分质量切片仍不占优；经 Sim(3) 对齐的轨迹误差不能认证原始 metric 坐标。Encoder 预训练、两个状态、TTT 梯度与逐帧融合都计费，效率与质量使用的硬件操作点也须分开。Pose prior 失准、geometry gate 遗忘、长序列或净成本回归时，保留原统一状态、显式 view/geometry bank 与重新锚定；这些 observation-derived 状态不获得 action-conditioned dynamics、真实 transition 或控制安全资格。

### MoRight07348 → MULTIMODAL-GENERATIVE-PARADIGMS Ch24，canonical角色训练两段后、GeneratedReality前

[exact-v1](https://arxiv.org/html/2604.07348v1) §3.1–3.4/Eq1–5、§4.1–4.4/Table3已读。同DiT两stream temporal concat joint selfattention，不误写独立crossattention架构；canonical静态camera含object轨迹、targetcamera不含object轨迹。Active/passive轨迹训练dropout但无角色标签，条件补全不授真实causal intervention。ViPE/AllTracker/Qwen3/SAM2派生标签；76kstatic/43ksyntheticpaired/3.4ksyntheticinteraction、constantintrinsics支持域。Wan2.1-14B、64GPU/15kiters/globalbatch16；480p35steps单A100约15min/video非robotrealtime。Table3去canonical camera/object下降，但PC/SA近似不变；11human330response只是视觉评价。现Ch24 391–397已经相机/角色分阶段数据，未承载canonical与target两共同去噪streams及轨迹条件互补；Ch23/25实际邻接已读。

逐字拟文：

相机与物体运动混在同一投影轨迹时，还可增加一条 canonical 生成流：在静态相机坐标中给 object trajectory，让另一条目标视角流只接收 camera 条件；两组 noisy latents 沿时间拼接后在同一 DiT 内共同 self-attend、联合去噪。Canonical 流分离控制输入，不是已知真实 scene state，也不是单独输出后几何 warp 成最终视频；两流仍可能共同生成错误运动。对主动/被动对象轨迹作条件 dropout，可以学习给定一方补另一方的正向或逆向条件分布，却不等于实施了物理干预或识别真实动力学因果。<!-- source-family:SF-2026-ARXIV-2604-07348 -->

[MoRight 的必要接口与有限消融](https://arxiv.org/html/2604.07348v1#S3)支持 canonical 条件化带来局部 camera/object 控制差额，物理观感 proxy 与人类偏好没有闭合真实接触、反事实因果或可执行 action。Depth、camera、tracking 与对象角色仍是派生标签，固定 intrinsics 和合成人口限定支持域；标注、配对生成、双流训练和完整去噪都计费，单 A100 约15分钟的视频工作点不是实时控制。坐标/角色条件失配、生成质量或预算回归时，保留独立/联合控制、干净 trajectory scaffold 与普通 I2V，物理状态及动作提交仍由第25/26章另行验收。

### TAMEn07335 → MULTIMODAL-EMBODIED-VLA Ch26，derived-label provenance后、多相机派生前

[exact-v1](https://arxiv.org/html/2604.07335v1) III-C/D、IV-B/C及TablesII–IV已读。Gripper pose在线映射target robot后检查IK/softlimit/overspeed/comms，不只是空间可达；mocap/VR可换采集模式，AR触觉在policy真实失败时采humanrecovery。两任务/有限用户与轨迹回放，不把未明确的10条扩大为每用户各10条，不授所有示教100%可执行。四下游task每20trial，+10%真实失败recovery与+50%nominal/+10%offline模拟failure不同人口、预算，不能归因AR或触觉唯一收益。实际Ch26 766–785 portability/derivedlabel线及后续reset讨论未拥有采集时targetfeasibility与onlinecontact recovery数据接口；Ch25/27邻接已读。

逐字拟文：

便携 gripper 示教要供指定机器人回放，采集时就应把“跟踪到了轨迹”与“目标本体可消费”分开：将当前 gripper pose 映射到目标机器人，检查 IK、soft joint limit、速度与通信状态，不只验 workspace 内的几何可达。Mocap 与便携 VR 跟踪可在准确性、遮挡与部署费用间选择，触觉/AR feedback 也可帮助人类在 policy 的真实接触失败处补采 recovery。Feasibility 标记仅覆盖该机器人及检查项，仍需原观察、跟踪/映射 revision 与 controller 回放证据；收下示教不等于物理安全提交。<!-- source-family:SF-2026-ARXIV-2604-07335 -->

[TAMEn 的有限采集与真机对照](https://arxiv.org/html/2604.07335v1)支持把真实失败 recovery 与普通成功示教分层使用，而不是只离线模拟 near-failure。两任务的有限回放与四任务小样本成功率不授通用可执行性；不同 recovery/nominal 人口和追加数据预算，也不隔离触觉、AR 或采样选择的唯一收益。跟踪/标定、目标 IK 检查、触觉硬件、分阶段训练和人类干预都计费，遮挡、接触变化或标记失准时丢弃不可靠轨迹、重新标定/采集，保留目标本体 teleoperation、直接 BC 与独立 controller/停机接管，不让便携示教覆盖替代真实闭环验收。

### Personalized RewardBench07343 → TRAIN-RLHF Ch31，具体已有覆盖

[exact-v1](https://arxiv.org/html/2604.07343v1) §3/4.3/5、Table1/3已读。LaMPQA三个域、Contriever top10history、Gemini3Flash chosen/rejected按相反rubric；Table1 chosen4.9而rejected4.3–4.7，general质量未matched，不采纯personal因果。直接baseline不喂profile；profile直注反退，planner估rubric缓解输入偏差。下游Qwen2.5-0.5B/BoN N16/PPO、Qwen2.5-32B rubric judge；Spearman .2571/.3714不能授普适下游预测或真实个体偏好。Ch31实际216–225“谁偏好什么”已明确profile contract、held-out paraphrase/personal slices、同contract downstream、synthetic/真实人口/安全边界及窄域/保守回退，完整覆盖采用的评价消费命题；不新增同义Books段，不采其数字作普遍排名保证。标准审阅，拟具体NC待root实际核。

## 补充公开日与覆盖收尾

12新增均在Apr08提交、Available=Apr2026；official abs exact-v1与DataCite `10.48550/arxiv.<ID>`、arXiv公告PID赋号规则、旧已核连续Apr09公告批界共同支持Apr09BJT日值。Submitted、Updated、DOI创建均不是公开动作，秒数不单独当宣布时刻。root实际读10具名raw receipt的Apr09 created；06831/06955作者本轮直接官方DataCite读created分别Apr09T01:58:45Z/02:01:42Z。PPFT UpdatedSep09仅metadata更新，精确v1 PDF Apr08header和必要机制/原AB一致，不能据此整family外部隔离。所有12在相邻04-09/04-08正式表无既选同family，不搬日期。其余Apr09公告批已被相邻日原冻结合法选择者只去重。

| exact-v1 | Submitted Apr08 UTC | Updated(v1) UTC | 本次采用公开日 |
| --- | --- | --- | --- |
| 2604.06831v1 | 08:49:17 | Sep09 02:20:29 | 2026-04-09（合证，非Updated） |
| 2604.06955v1 | 11:15:52 | Apr09 00:44:01 | 2026-04-09 |
| 2604.07277v1 | 16:40:26 | Apr09 01:00:47 | 2026-04-09 |
| 2604.07279v1 | 16:41:22 | Apr09 01:00:50 | 2026-04-09 |
| 2604.07306v1 | 17:14:50 | Apr09 01:02:31 | 2026-04-09 |
| 2604.07328v1 | 17:46:06 | Apr09 01:03:45 | 2026-04-09 |
| 2604.07335v1 | 17:49:35 | Apr09 01:03:52 | 2026-04-09 |
| 2604.07340v1 | 17:53:52 | Apr09 01:04:02 | 2026-04-09 |
| 2604.07343v1 | 17:55:00 | Apr09 01:04:08 | 2026-04-09 |
| 2604.07345v1 | 17:56:41 | Apr09 01:04:10 | 2026-04-09 |
| 2604.07348v1 | 17:59:22 | Apr09 01:04:18 | 2026-04-09 |
| 2604.07350v1 | 17:59:48 | Apr09 01:04:24 | 2026-04-09 |

14 Daily到期来源的补Apr09实际入口/范围、有效层复用、停点与精确缺口已自包含融入README §2，无重复source rows。有限主题query与官方相关title补检没有转全月/fulltext队列；on-demand没有新触发，未扫Weekly组。Current新事件官方页无撤回/纠错提示，显示后版本者仅当前提示轻量核，不遍历史。Seeduplex及ConvApparel实际必要core关闭与ATOM题摘生态快照关闭；旧泛‘成熟组合/没privacy证’的TRAPTI/PPFT局部恢复，其他有限AB未用理论/小模型/行业否决。

已有普通Books进度：07277、06831、06955实际正文/两侧及自身source note非作者POST通过，作者回读并释放，3I。07345具体NC通过。余8候选Source/PRE/NC独核待，尚不授DAY；源目录精确缺口不是普通未读。

## 用户暂停 checkpoint（2026-10-14，系统更新前）

用户明确要求暂停，停止研究、发现、进一步Books写入与后日分配。当前冻结原70候选整行/评分/日期、旧窗口与连续原§4，唯一完整baseline保存；没有stage/commit/push。

- 已实际POST的本轮3I：07277→Ch32（84–90）、06831→Ch12（140/142）、06955→Ch54（140/142）；三项纯source注已同步实际写后通过，作者回读，ownership已释放。07345→Ch70具体已有覆盖的必要Source/独核已通过，不改书。
- 第二批4项已按root窄授保存，作者实际正文/旧两侧/自身注回读、scoped diff-check通过，当前等待root实际POST：07306→Ch27新180（Table5 pseudo-clean纠正后），07328→Ch27新912/914，07340→Ch23新333/335，07350→Ch22新722/724；四项source注仍写actual写后待完成。未POST不计整合；root将仅核已经发生的写入，不开展新研究。当前所有窄Books ownership均释放，不继续修改。
- 其余3项07279→Ch25、07348→Ch24、07335→Ch26的必要Source作者已读、完整具体差额及逐字PRE在上文，尚未取得root Source/PRE独核/ownership，没有写Books。07343→Ch31具体NC方案也只是作者实际比较，普通独核未完成，不能称external或已闭合。
- 12新增的完整官方AB准入及公开日合证已准备，上文保留精确identity/日值与PPFT metadata边界；README §2已融入14每日来源的实际有限范围/停止点及明确目录限制，尚无本轮Coverage/DAY整体独核。原70有效层只按未变身份/命题复用，旧DAY不授补查完成。
- 正式README仍为进行中，仅增补窗口/冻结字段、当前说明与来源表；尚未把12新候选行和12证据段并入§3/4，也未改原旧完成段为最终补查数量。最终82候选或Books分布尚不能宣布。原baseline完整，后续需在剩余独核/实际POST之后融入原六部分，再校验冻结整行、原§4连续、Markdown/引用/scoped cached/unstaged diff并获非作者DAY与实际写后最终复核。

恢复只读本日窗口/此checkpoint及当前合同；不得因暂停标签继承尚未完成Gate。未核处只定点该Source/实际owner，不重读原70/全附件，不扩下一日期。

暂停收尾的 root 实际写后检查：07306 Ch27 174–185、07328 Ch27 905–921、07340 Ch23 329–340、07350 Ch22 714–729的新正文与完整旧邻接，以及四项本人来源注均已真实读回，与已核必要原证和修窄后的PRE一致，POST通过。此前“四项待root POST”由本段取代；不重读这些有效层。四注的旧“实际写后待完成”文字尚未同步，恢复仅先同步这四处真实状态并回读，再接剩余三项Source/PRE、PRBench具体NC及六部分汇总。已有3项全链落实和4项实际POST层通过，不预授最终候选分布或日级DAY。所有ownership已释放，任务暂停。

## 本轮恢复与有限写后（2026-10-14，系统更新后）

用户明确恢复后，resume_apr10_report 独立重读当前AGENTS/适用合同、ROADMAP、本日窗口与本停点；原70日期/评分/窗口及连续§4冻结，不扩发现或附件。四注07306/07328/07340/07350已获root纯状态窄授权，同步实际POST通过并真实回读，正文未变；相应纯注ownership释放。

root本轮独立实读Mem3R必要§3.1–3.4/Eq3–10、§4.1–4.5/T3–4与Ch25完整ZipMap/实体关系邻接，MoRight必要§3.1–3.4/§4.1/T3/4.7与Ch24 canonical/GeneratedReality邻接，TAMEn III-C–E/IV-B–C/T2–4与Ch26 derivedlabel/多相机邻接；三项Source/PRE通过、各两段正文＋纯source注窄授权。作者已按上文逐字PRE写入Ch25/24/26，真实顺读完整局部及本人末注、限定diff-check通过；实际POST待root，不预授DAY。TAMEn回放人口窄纠正如上，不扩大为每用户10条。

root本轮实读PRBench §3/T1/4.3/5/T3与Ch31“谁偏好什么”完整正文及两侧，具体已有覆盖通过；保general quality差异、synthetic rubric/judge proxy、小policy和低Spearman边界，不写书。12新增正式候选/证据及六部分汇总继续，只有最终独核完成才授日级。

root已actual读Ch25 728–747、Ch24 391–403、Ch26 778–791完整新两正文与旧两侧、三条自身来源注，三项nonwriter POST通过。三注已同步真实状态、作者actual回读，Ch25/24/26窄ownership释放；此前“待root POST”由本段取代。12新增＝10实际整合（9唯一owner，Ch27两family）＋2具体已有覆盖，全部单项必要Source/采用边界/实际POST或NC有效；不是日级验收。

正式README已合82候选行/82证据项，§1/3/5/6明确原70历史有效层与本轮普通全日待核差别，§2自包含14实际每日来源，ConvApparel已具体关闭，七晚family/Nexus只属原小时窗保留层，不扩补Apr09。本轮作者校验：V3通过；原70整行逐字、旧窗口和连续31880字符原§4保持；82unique family、70本地引用均存在；限定cached/unstaged diff-check通过。没有改公共脚本、stage/commit/push。当前仅待root本轮有限Coverage/全六部分DAY和完成字段真实回读，不以机器通过代语义验收。

### root 本轮独立日级复核：通过（2026-10-14）

root非补充报告作者已实际复核六部分：§1漏斗/44整合、19具体已有覆盖、15仅报告及4争议边界；§2十四每日源的实际入口、有限查询/分类相关标题停止、可复用目录层与精确外部缺段；§3全部12新增行与原70逐字冻结；§4全部12新增证据及未变连续原§4的有效审阅层复用；§5普通余项/原小时窗日期隔离/争议重开；§6实际独核与机器检查分责。首批准入和十项必要Source/正文邻接/本人注实际POST已具名通过，两具体已有覆盖已读真实Ch70/31；不无差别重读原70或无关附件。本轮另实际读ATOM07190完整官方v1摘要，生态采用快照不新增模型/Infra机制的关闭成立；ConvApparel/Seeduplex的已核core关闭、TRAPTI/PPFT误排局部纠正及原分层否侧有效层复用，未独抽其余宽库存，不授全学科召回。

独立读取baseline/current确认70→82、旧70完整行/日期/评分和原窗口保持、连续原§4仍原样存在、12新增均Apr09日值、本地链接无缺失；当前V3及限定cached/unstaged diff检查通过。必要目录、原小时窗资格与中心争议已安全隔离，不授其正面Coverage/Evidence、性能/隐私保证或无遗漏。没有普通可执行研究/Books/报告待办；本轮DAY通过，可只同步完成字段和本结论，再进行一次实际完成态回读。未核代码或复现，不stage、commit、push。

作者完成态同步：README状态已切完成，§1/5/6同步本轮实际DAY通过/普通0/有限审阅范围；未改候选、原正文或新的研究命题。完成态V3、82unique/82证据、70本地引用零缺失、原70完整行/旧窗口/连续31880字符原§4与所有本轮文件限定cached/unstaged diff-check再次通过。各窄Books锁已释放；当前仅供root实际FINAL回读后接纳计数，不分新日期，不写共享State，不stage/commit/push。

root实际FINAL：已真实读完成header、§1安全终态、§5普通0/原小时窗隔离和§6本轮独核范围，current V3/限定diff exit0，通过并接纳2026-04-10日级。作者本日README/唯一SUP及全部窄Books ownership已释放、退出；不继续研究/改书/分配后日，共享State与fresh下一日由root处理。必要目录/资格/中心争议仍安全隔离，不授正面Coverage/Evidence或无遗漏；未stage、commit、push。
