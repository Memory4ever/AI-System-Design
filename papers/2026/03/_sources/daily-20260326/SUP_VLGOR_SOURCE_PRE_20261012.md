# VLGOR necessarySource / sole Ch25 两PRE

2026-10-12，[2603.22892v1](https://arxiv.org/html/2603.22892v1)，原2+1+3=6/date25保持。actual§3–5/Eq1–3/T1–2/A1–2/T3–4与B1–2决定人口/接口；不读全部图值/所有对照C2，无code/复现。因具体world→policy数据资格差额深入必要内容，不为凑等级读附件。

## 可采用命题与反侧

Fine-tune BAGEL共享MMSA LoRA＋text/visualheads，从初视觉s0、instruction/初action预测未来visualstate与action。原文说extract前hsteps作sample但Eq1实际给初态/初action输入，不能自授全部futurehprefix在线可见。固定background模板，再改target或behavior造目标，预测rollouts与真实数据按固定ratio给offline BC/CQL。生成器同时拟dynamics与imitationpolicy，既非独立actioncontrolled环境响应、也非truecounterfactual识别；目标变更同时改初action条件，不能归因只语言改变。B2 MetaWorld只有单对象，target实际换目标区域、behavior改路径，不称换实体。JointMMSA共享信息，两heads不证明模态独立。

环境reward用于real与imaginedtrajectory，但从预测RGB/action恢复足够simulatorstate或reward接口未披露，不补replay/可靠oracle实现。S3 BC/CQL discreteaction formulas vs B1 MetaWorldR4continuous、CLEVRR40onehot不同schema，原公式CQL只有conservativeterm、Bellman与continuous扩展未给，BAGEL visualrectifiedflow vs正文直接state/action MSE不授同recipe。只采goal-edit imagined数据源/联合future-image与action生成→consumerpolicy分责，不授整套grounded物理或可执行BC/CQL配方。

单H80080GBPCIe、BAGEL20epochB16、offline50epochB128/Adam3e-4→1e-6cosine、三seed/最后5checkpoint平均（errorbar halfstd不是CI/五独立seed）；100K原rolloutgoal、SFT10K/ChatGPT1440CLEVR+200Meta goals，baseline6.4Kreal而VLGOR另5.4K/6.4K/1.68Kimagined，但S4.2称totaldata恒定，采样/replay次数/固定ratio具体值未披露，不认为唯一matchedbudget或视觉增量归因。T1两行都10000但不同metrics未闭身份，不自改15K；initial128²与A2VAE256²/ViT224²是不同input/preprocess而非一统一分辨率。Difftimesteps70/temp.3/maxthink1024明确；precision/模型具体checkpoint/LoRArank/生成长/B/concurrency/完整time/SLO ND。

PSNR/SSIM/主object normalizedMED只state代理，不测所有碰撞/contact/物理规律；KALM文本state经MuJoCo渲染对比，不等所有生成图同renderer或真dynamics对照。T2按target/behavior移除减收益是局部接口反侧；与成熟KALM在rephrase接近，hard仍19.3/17.8有限，S5只简单simulation，真实controlfuture。所有实采、BAGEL适配/LLM造goal、imagined生成/完整70steps/VAE/奖励映射、混合policy/value学习与评价都计费；sameepochs不证明同sample/算力/费用，表提高不认证所有unseen目标/无loss。

## actual owner gap与窄锚

actual Ch25完整361–410 imaginedrollout（chunk/realstart→risk→realfailed模型vs筛过successBC→Dreamerlatentfeedback→DreamPlan离线pairs→localgradient→optimisticbias/variance）与214–244 Goal传递/稀疏keyframe完整、Ch24/26开篇有效。现12063按真实成功失败更新并筛imaginedsuccess没有说明固定初视觉/改targetbehavior让generator联合出futureimage+action作为离线目标数据源；DreamPlan冻结的是偏好pairs，Dreamerlatent模型是独立动作候选反馈。此差额sole MULTIMODAL-WORLD-MODELS Ch25，不复制CQL数学/训练优化器。

拟12063完整末段（末“不继续用想象标签放大自证循环。”+marker）之后、当前Dreamer24587“当逐候选解码视频再判分过贵时…”段之前，原两PRE+本人纯静态注；原Goal/真实数据/反馈路线保持。Ch25别日窄锁由root协调，作者仅准备不并发写；未独核/锁/实际写/POST。

## 两逐字PRE

离线目标覆盖还可以通过编辑生成请求来扩展，而不只从当前 policy 的真实失败中继续采集。一个受限分支固定初始视觉和背景模板，改变目标对象或行为条件，再由适配的视觉语言生成器联合提出未来观察与动作，把这些 imagined rollouts 与真实轨迹分账交给离线 policy。某些单对象任务的“改目标”实际改变的是终点区域，不是换对象；生成器同时学习状态变化与行为模仿，也不因此成为可独立响应任意动作的环境模型。<!-- source-family:SF-2026-ARXIV-2603-22892 -->

这改变的是训练数据源和任务条件的支持，不是赋予想象 transition 真值。目标改写、初动作和生成器版本须共同保存，真实与生成数据的比例、样本预算和奖励取得方式也须明确；从预测图像恢复奖励所需状态的实现未披露，不能补造可靠 simulator 接口。受限仿真中的图像/位置代理和较高任务成功率不证明接触、全部反事实或实机安全，部分预算和动作配方口径也未闭合。实采、生成器适配、全部目标/轨迹生成、奖励映射与 policy 学习共同付费；生成支持、数据资格或奖励失配时，保留真实轨迹、短想象与独立环境验收，不让语言目标和 imagined 高分替代真实反馈。

## 自身静态证据注PRE

- `SF-2026-ARXIV-2603-22892` — [VLGOR exact-v1](https://arxiv.org/html/2603.22892v1)必要§3–5/Eq1–3/T1–2/A/B；仅固定初视觉/改targetbehavior的联合future-image/action生成与离线消费接口。保goal/action条件身份、奖励state映射未披露、data预算/schema/目标函数口径不闭、局部simulation与全制备训练生成费；不授truecounterfactual、完整recipe、实机安全或SLO，未核code/全部图值/复现。
