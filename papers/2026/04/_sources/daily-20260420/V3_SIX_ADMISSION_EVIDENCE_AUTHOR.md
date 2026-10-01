# 六项已准入材料的作者 Evidence → owner 有界提案

作者：apr20_resume。apr01 的 `V3_APR01_ORIGINAL_EIGHT_ADMISSION_AUDIT.md` 仅通过六项贡献入口，本文件把本日 `v3-reopen-notes.md` 已实读的必要方法、受控反证和当前实际 owner 比较转成待非作者裁决的具体结果；**不是独立 Evidence PASS、Books Gate 或整日 Gate**。官方首次公开仍由本日窄批链核定，不以以下 arXiv 提交字段单独证明。各项只读决定处置的 v1 段，不扩全附件。

## 15351 Aletheia — 拟5标准Only

[exact-v1](https://arxiv.org/html/2604.15351v1) §3–6：五批gradient probe/八层chunk选top50%，跨模型主对照同rank16；Qwen3B单模型asymmetric-rank search是另一支线。14成功模型的200-step/3seed、200问MMLU子集、Pythia fp16 NaN与matched-step/compute-matched区别保留；缺同数量random/depth选层基线，不能将收益唯一归因gradient排序。实际Ch30:133–140已有GRASS按gradient RMS周期抽原参数层并支付probing/offload成本；但它**不是**LoRA层子集的具体rank选择，故不签“整算法Existing”。本受限选择配方只有局部训练成本/质量案例，不足以修改LoRA低秩更新的长期机制，拟标准Only；layer selection校准仍须按实际任务验收，不把参数减少当activation免费。

## 15414 TeLAPA — 拟5标准Only

[exact-v1](https://arxiv.org/html/2604.15414v1) §3–5/Table1/Figs1–7：PPO policy archive保留source-competent邻域，以短transfer probe选种，重置optimizer；trajectory embedder通过anchor/replay/distillation及周期全库reembedding维持坐标。五MiniGrid任务/反复访问、20runs/95%CI下full SR .706/TTT3.35M 对ScratchReuse .525/5.49、Static .507/5.59，支持有限再学习分支；ScratchReuse有部分BWT反向，full coverage .50不等全部学会。probe/library/reembedding另付成本，source-best≠transfer-best的35.5%是任务内观察，不能证明普遍因果。实际Ch32拥有PPO update/old policy身份，Ch35拥有恢复checkpoint；本材料的policy archive与latent坐标维护不是旧PPO本身，却只在小环境给局部能力复访结果，没有构成须增长期书稿状态契约的可迁移保证。拟标准Only，不因无LLM硬关闭。

## 15451 Weak-to-Strong KD — 拟5标准Only

[exact-v1](https://arxiv.org/html/2604.15451v1) §3–7/Table1/3：已存在且适度弱的frozen teacher经warmup/hold/decay早期指导，学生连续两次validation超过它后永久停KD。RetinaNet同架构不同checkpoint AP50约12.8过弱/19.5适中/26.2过强，generation也有两端无收益；moderate Res18→Res50的4.75×只为first@target steps，极弱例可.51×。完整首次训练须计teacher构建及active forward，wall-clock成本表未在本轮必要阅读内，不能说净加速。实际Ch29:263–280已有teacher/student capacity gap、阶段/lineage与独立质量验收，但没有“两次超越即停”的通用KD定律；此特定视觉任务早期停止operating point可报告，未修正长期蒸馏所有权，拟Only。

## 15614 E-BoN — 拟5标准Only

[exact-v1](https://arxiv.org/html/2604.15614v1) §2–5/Eq16–19/Table2：固定N候选，entmax α与非负empowerment均值β缩放探索强度；额外transition/marginal模型、SAC off-policy是成立条件，近似entmax算法不叫精确采样。J全零时倒数分母及formal divergence符号不可默补；50seed CartPole/PointMass、8seed locomotion里Walker/Quadruped非最优。Ch20:246–333已将候选coverage、selection与额外采样/评价预算分账；本文的α/β操作分支仍有局部增量，非BoN原理全已有，但没有LLM负载或真实端到端固定成本证明，拟标准Only，不写普遍解码配方。

## 16076 PGCM — 拟5标准Only

[exact-v1](https://arxiv.org/html/2604.16076v1) §3.1–3.4/4.1–4.3/6–7：part segmentation→离散可显示prototype→concept decoder→concept-only task，支持受限编辑/删除；segmenter先看全image，不能称区域外像素从未影响概念。ColorMNIST+/CelebA/CLEVRHans、3seed，CelebA低于CBM、coupled干预更弱；prototype容量和人工认知成本需计，没有独立human alignment study。Ch23:1–96已有representation的modality/coordinate/artifact identity与视觉接口，但不等于本概念原型算法已覆盖；原型语义与任务因果的受限实证未改变表示主干，拟Only而非因非LLM关闭。

## 16090 AW-PSP — 拟5标准Only

[exact-v1](https://arxiv.org/html/2604.16090v1) §2–4.2.5/Eq13–15/Tables1–5：设备availability与本地数据相关时，快/常在线参与方被过采、类别支持偏置；EWMA/Markov/DHT风险估计影响同步选择，但Eq15的`(1−risk)`乘积未披露所有ρ合法概率的clamp/归一条件。10实际worker分波跑100–3000逻辑client、ResNet34/18章节配置不混；accuracy只算covered labels，缺失类不能写0或全类85%；Table5 noise提高时自身33.75→29.78的相对下降大于PSP，不采全指标更robust。Ch36:1340–56已有迟到/到场采样偏置与staleness owner，未覆盖availability×data-support co-correlation的本配方细节；有限CIFAR/Mininet/availability proxy未证明大模型同步或无偏质量，拟标准Only，不以FL/小ResNet硬拒。

六项均为作者提案；非作者应针对各自必要原文、反例和实际 owner 裁决，不把apr01准入PASS升级为Evidence PASS。任何Only变I须重新获得具体命题差集、最小正文、独立source→owner及写后核。
