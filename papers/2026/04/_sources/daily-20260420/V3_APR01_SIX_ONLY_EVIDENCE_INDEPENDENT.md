# 六项已准入材料的有限非作者 Evidence→owner 复核

复核者 apr01；仅核已准入单篇的必要 exact-v1 方法、评价反证与现有书稿命题。作者提案见 `V3_SIX_ADMISSION_EVIDENCE_AUTHOR.md`。本记录不核 04/20 日期、14 来源或整日 Gate；未审条目不得因列入“六项”而视为通过。

## 2604.15351v1 Aletheia — 5 分标准，仅报告：PASS

- 原始证据：[官方 exact-v1](https://arxiv.org/html/2604.15351v1) §3.2–3.5、§4.5–4.6、§5.5、§6。主实验用五批 full-parameter gradient probe、逐八层处理，选梯度范数最高的约半数层，只给这些层加固定 `rank=16` LoRA；Qwen3B 的非对称 rank/recipe search 属另一个单模型支线，不能把它写成跨架构主实验同时证明的机制。200 fixed steps 与延长到 250 steps 的 equal-wall-clock 对照须分开；后者三个模型 eval loss 均较标准 LoRA 高，有限下游任务“相近”不能代替 loss 或未完成测项。无等层数 random/depth 选择基线，不能把全部时延/质量差归因为 gradient 排序。Pythia fp16 NaN 同时发生于两方案，非 Aletheia 独有失败。跳层省的是 adapter 算子及状态，冻结 base 的 token forward/backward 执行并不免费消失。
- 真实 owner：`TRAIN-LORA` [Ch30](../../../../../books/part-04-training-system/30-lora.md) 的“低秩更新与轮流更新原参数层”已说明 gradient RMS probe、选择层、探测与 offload 代价，但那是原参数层动态轮换，不是本文训练前一次性选择 LoRA 层；故不得写 `Existing — 整算法已覆盖`。然而本文没有隔离 gradient 排序相对等层数简单选择的独立收益，且 equal-wall-clock 质量并非全正。它提供受限的 adapter 计算/质量 operating point，尚不足改变 Ch30 已有“选择代理、训练成本和 held-out 质量共同验收”的长期判断。维持 `Report Only`，不新增 Books；不能以“已有 GRASS”作为前分母关闭理由。

## 2604.15414v1 TeLAPA — 5 分标准，仅报告：PASS

- 原始证据：[官方 exact-v1](https://arxiv.org/html/2604.15414v1) §3–4、Table 1、Fig. 1–7。方法保留多个 source-competent policies 而非唯一 source-best，短目标 transfer probe 选种，重新初始化 optimizer；trajectory embedder 使用 anchors/replay/distillation 与周期重嵌入维持 archive 坐标可比。`35.5%` 是作者有限 source→target 对中 source-best 非 transfer-best 的观测，不是全部持续学习任务的因果比例。五个 MiniGrid 任务、20 runs、受限任务反复访问下，full method 的平均 success/TTT 优于 Scratch-Reuse/Static，但 Scratch-Reuse 的 BWT/nBWT 更优，full coverage 也仅约 `0.50`；不能写成无遗忘或全任务掌握。Archive/短 probe/全库重嵌入都另付训练与维护成本。
- 真实 owner：`TRAIN-PPO` [Ch32](../../../../../books/part-04-training-system/32-ppo.md) 只拥有 rollout/old policy/update；`TRAIN-CHECKPOINT` [Ch35](../../../../../books/part-04-training-system/35-checkpoint.md) 负责可恢复训练状态和 RL pipeline 多对象一致性，两者均未声称存在此特定 archive 搜索算法。Source-best 不必 transfer-best 是可报告的受限反例，但现有证据未将 MiniGrid policy-neighborhood 机制与大模型后训练的长期 checkpoint/admission 选择建立可检验桥，也未隔离 archive 维护各部分对收益的贡献。维持 `Report Only`，不误写 `Existing — 具体算法已覆盖`，更不因“小模型”直接前分母关闭。

## 2604.15451v1 Weak-to-Strong KD — 5 分标准，仅报告：PASS

- [官方 exact-v1](https://arxiv.org/html/2604.15451v1) §3 stop rule、§4.3/§5 Table 3、§6：冻结的弱 teacher 只在早期 warmup–hold–decay 供监督，student 连续两次 validation 越过 teacher 时永久停 KD。它改变 time-to-threshold，而非证明首次完整训练 wall-clock 下降；现成 teacher、active teacher forward、选择/验证都要计账。RetinaNet 同一 teacher 架构的 checkpoint 强弱消融使“适度弱”不只等于换架构，但极弱分类 .51×、极弱生成 .80×和过强近持平反证通用加速，`≤15%` 不是普遍有效带。作者的 first@target 是 epoch/step；不能以 `4.75×` 写生产吞吐。
- 对读 `TRAIN-SFT` [Ch29](../../../../../books/part-04-training-system/29-sft.md) 容量差、分阶段 teacher/lineage 和质量验收：当前并未包含该两次超越规则，因此不是“完整方法 Existing”。这篇在视觉分类/检测/CIFAR 生成给一个可用但受限的阶段停止 operating point，未建立可跨本书后训练主线直接迁移的阈值或净成本保证。维持 `Report Only`，保留冻结 teacher 已存在这一必要条件，不为局部数字改写长期 KD 章节。

## 2604.15614v1 E-BoN — 5 分标准，仅报告：PASS

- [官方 exact-v1](https://arxiv.org/html/2604.15614v1) §3.1–3.2/Eqs.16–19、§4/Table 2：在固定 `N` 候选上，目标 `J≥0` 的样本均值倒数给状态内尺度，Tsallis/entmax `α` 决定尾部/零支持；`α` 不等于简单温度，近似 `λ` 求解不等于精确 entmax。需要额外 empowerment 的 transition/marginal 模型，策略改变后使用 SAC off-policy。若本组 `J` 全零，作者 Algorithm 2 的 `β=1/mean(J)` 无定义；仅能列为需 fallback 的形式边界，不从此否定其它实验。受测 CartPole/PointMass 与三 locomotion 并非都最优，固定 `N` 只锁候选生成次数，额外模型/打分/近似归一与 wall-clock 不一定固定。
- `MODEL-SAMPLING` [Ch20](../../../../../books/part-02-model/20-sampling.md) 已将并行候选 coverage、selection、judge/聚合预算及错误相关性分账；本文提供独立的受限选择分布形状配方，并非 Ch20 已有同一算法，但未测 LLM reasoning 的生成/selector 闭环或端到端预算。其论证对象主要是 off-policy 控制行动，不能靠 Best-of-N 名词把小环境结果升为本书默认解码规则。维持 `Report Only`，不采“恒定计算成本”宣传。

## 2604.16076v1 PGCM — 5 分标准，仅报告：PASS

- [官方 exact-v1](https://arxiv.org/html/2604.16076v1) §3.3–3.4/§4.2–4.3、Table 4：segmentation part→视觉 prototype→concept decoder→concept-only task 的确增加可显示/可编辑的中间状态，不能说一般 CBM 已完整包含此操作。其“mask 外像素未用于预测”至多适用于给定分割后下游 part feature 路径；part 的分割模型先见原图，不能升级为整条系统的无外部像素因果保证。ColorMNIST+/CelebA/CLEVR-Hans、三 seeds 是局部示例；CelebA PGCM concept/task `78.5/83.0` 低于 CBM `81.3/84.0`，依赖概念联动干预在 CelebA 又有反向。未有独立人类对齐研究，prototype 数量增加会提高容量也提高检查负担。
- `MULTIMODAL-REPRESENTATION` [Ch23](../../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) 已分 tensor/semantic compatibility、encoder/projector 接口及任务输出验收，但没有宣称包含这套具体 prototype 算法。现材料只支持有限视觉概念可编辑性的实现点；没有证明 prototype 语义即人类概念真值，也未改变书稿表示/证据权力的长期责任链。维持 `Report Only`，不能因小视觉模型硬排，也不按作者“verifiable”名词写正式保证。

## 2604.16090v1 AW-PSP — 作者 Only 尚需 root 定点 Books 裁决

- [官方 exact-v1](https://arxiv.org/html/2604.16090v1) §3.2–3.3 Eqs.13–15、§4.2–4.2.5/Tables 1–5：availability 与数据支持相关，使频繁在线设备/其类别被过采；方法又用共同失败历史与 DHT 近邻惩罚调整采样概率。`ρ` 是否始终令 `(1−ρ)` 为合法概率、如何归一/截断，主文未交代完整保证；一台服务器上十个实际 worker 分波模拟 100–3000 逻辑 clients，不能写作千设备真实同步或 LLM 收敛。accuracy 只对 covered labels，unseen classes 另计；§4.2.3 Gini 公式数的是 client participation，而后文字又解作 class representation，两者不等。Table 5 增噪时本法 `33.75→29.78`（−11.8%）相对降幅比 PSP `27.85→26.84`（−3.6%）更大，不能称各维更 robust。
- `TRAIN-DISTRIBUTED-TRAINING` [Ch36](../../../../../books/part-04-training-system/36-distributed-training.md) 1140–1150 已有单 worker 到达频率造成 objective sampling bias、按边际频率校正与 stale direction 分离；并未明确 **相关共同不可用 × 非 IID 类别支持** 可能让单 worker 权重校正仍无法保证每轮类别 coverage。这是潜在窄长期失效边界，不能仅用“Ch36 已有到场偏置”签 `Existing`，也不能因小 FL 硬拒。作者的具体 EWMA/Markov/DHT 配方和受限模拟尚不足支持通用算法 adoption；建议 root 对此一个命题作 Books 判断：若现有 Ch36 的 intended-global-weighting/coverage 已实质承载，则 `Report Only`；若没有，可只吸收“边际到场率校正≠联合类覆盖保证”的条件性反例，仍不采本文概率公式/质量数字。**本项非作者 Evidence 与边界复核完成，但不签作者的最终 `Only`，待 root 窄裁决。**

本记录只核六份具名材料的必要段和实际 owner，不替代 04/20 首公开、全部来源、其他候选或日级语义 Gate；所有实验均未独立复现。`16090` 的 Books 决策问题不应被记成外部材料阻断，也不扩查其所有附录/参考文献。
