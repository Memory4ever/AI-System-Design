# Apr21 有界非作者审计：16774～16850 的指定 14 项

审阅者：apr02（非本日报作者、未写本批 Books）；实际访问：2026-09-27。

## 范围与结论

实际读取三份作者批次记录，并独立打开下列官方 exact-v1 的必要方法、关键评价及反证位置；对拟新增命题读取当前章节真实正文与相邻交接。没有重扫 270 条题摘、机构目录、全部附件或版本史，也没有复现实验、证明 first-public 日期或执行日级 Gate。本文不修改作者 README、作者 notes 或 Books。

14 项处置支持：2 项知识缺口深入提案、9 项仅报告、2 项窄争议、1 项前分母关闭。两项提案只是 source→owner 独立通过，尚无本审阅者批准的实际写入或写后验收。评分采用作者已有三维算术；本批核准贡献与审阅深度，不机械增加分数。

## 2604.16774v1 StageMem — 5 分标准，仅报告：通过

[官方 HTML v1](https://arxiv.org/html/2604.16774v1) §4.1–4.5、§5.6–5.8 的当前标题与方法确为 StageMem，不沿用旧库存题名或把已恢复材料继续隔离。不同 retention depth 的 admission、settlement 与 promotion 分工可定位；confidence validity 和保存强度不能混成一个数字。

实际对读 Ch77 retention admission 与 confidence/staleness 段：已有长期状态治理主干；本篇具体 tier recipe 不因此全部属于 Existing Coverage。符号合成环境、近似基线及改编外部数据的结果不足以采用一般端到端产品优越性，仅报告有据。

## 2604.16787v1 InformalNLI — 5 分标准，仅报告：通过

[官方 HTML v1](https://arxiv.org/html/2604.16787v1) §3.3–3.4、§4 表格与 §5.5 支持将不可恢复的 UNK 信息损失与仍在词表中的噪声权重区分。逆预处理与训练增强是不同干预；emoji 多对一恢复不能解释成完整语义还原。

实际 Ch11 byte fallback 段已说明 UNK 与 byte 展开代价，但不承载此完整 NLI 配方，故不宣称算法已有覆盖。SNLI/MNLI、ELECTRA WordPiece 与 RoBERTa byte BPE、额外增强训练及不同 warmup 的合同限制必须保留；零样本 GPT 比较不是同成本机制归因。

## 2604.16788v1 LongBench — 5 分标准，仅报告：通过

[官方 HTML v1](https://arxiv.org/html/2604.16788v1) §4.2–4.5、§5.1 实际区分长动作链与需要历史消歧的观测条件；不是仅因 robotic benchmark 而保留。六种 policy 比较不是对记忆开关的严格因果干预。

ARX-R5、双 RGB、20Hz 与 16-step open-loop 属测量身份；任务平均 atomic progress 与成功率、1000 demonstrations 也不能互换。Ch66 protocol/outcome 分账足以承载采用边界，本具体任务集仅报告，不提出一般记忆能力结论。

## 2604.16790v1 BiasLoop — 5 分标准，仅报告：通过

[官方 HTML v1](https://arxiv.org/html/2604.16790v1) §3.2.2–3.3、提示配置表与 §6 支持同一代码在位置/呈现变化下产生 judge 漂移。部分 cue（例如 rubric 或 CoT）同时改变任务接口，不能统一叫作语义无关扰动。

5352 个有限代码样本、三种 judge 与两次独立会话不证明长期重复稳定性；执行测试标签不是任意程序的真值 oracle。现 Ch66 judge 身份与 protocol 分账已提供长期主干，本篇受限 sensitivity 结果仅报告。

## 2604.16801v1 Coupled Flows — 5 分纠错深入，窄争议：通过

[官方 HTML v1](https://arxiv.org/html/2604.16801v1) Appendix B.4 Theorem 11、B28–B34 已实际核。定理确实要求对 top-m eigenspace 的非零投影，不能误写成没有初始化条件；但非零投影不推出 rank-m。

反例取 m=2、Σ=diag(3,2,1)，W 的两行均为 (1,1,0)。两个领先方向均非零、谱 gap 成立，而原 ODE `dot W = γ(WΣ − Tr(WΣWᵀ)W)` 保持两行相等及 rank≤1，不能获得声称的二维 row space。只隔离该充分条件至全维收敛的桥；不否定其他 Lyapunov/局部流结论或一般满秩随机初始化的经验结果。不据此保证写 Books。

## 2604.16809v1 BN delayed loss spikes — 5 分标准，仅报告：通过

[官方 PDF v1](https://arxiv.org/pdf/2604.16809v1) §3、Theorem 2、Appendix B Lemma 7（PDF 页 19–21）实际核：白化线性平方损失下的方向、可训练 scale 与 norm 动力学给出 `η αρ / ||w||²` 的 effective learning rate，延迟条件与 no-rising-edge 条件不同，并不是无条件完整相图。

线性/受限 logistic 结果与小型 full-batch 实验不能直接迁移为 RMSNorm 或生产 causal LM 的调参保证。Ch17 normalization 与优化耦合主干存在；此受限机制研究仅报告，不把所有 deep-network spike 因果归给这条链。

## 2604.16812v1 Introspection Adapters — 6 分知识缺口深入，Ch66 提案：通过

[官方 HTML v1](https://arxiv.org/html/2604.16812v1) §2.1–2.2、§3.4、§4.1–4.2、§6 已核。跨同一 base 的冻结 behavior-delta 联合训练共享报告 adapter，与对单一 backbone 校准 claim probe 是具体不同的训练身份。

实际 Ch66 “从 Raw Score 到 Claim Sensor”及 organism 诊断主线未明确这一共享报告接口；可窄补 base、behavior delta、report adapter、偏好标签与跨变体 holdout 的绑定。报告只提出行为审计线索，不是内部自知或发布权限。高假阳性、类别幻觉、跨家族不稳定、预先构造 organism 成本必须在正文近处保留；sandbagging 的 33% 与 15.8% FPR 不构成精确识别隐藏行为。仅 source→owner PASS，未写入。

## 2604.16824v1 SafeDream — 6 分保护行为深入，仅报告：通过

[官方 HTML v1](https://arxiv.org/html/2604.16824v1) §3.1–3.4、§4.1–4.2 已实际读。冻结 Qwen2.5-7B 第 19 层、5 个方向与 64 维增强组成 69 维状态；risk-logit CUSUM、灰区双类想象池与未来 latent 状态预测各有职责。

M=8、H=3 的双池为 48 个预测步，还需 hidden-state 前向，不能以小模块参数数代表全部成本。discriminator logit 不自动满足经典已知 likelihood-ratio CUSUM 条件，想象也不等真实未来用户律。实际 Ch72 cumulative effect 与版本化 sensor/保护动作分权已承载长期判断；该单 backbone 原型、共享 grader 与不完全 matched baseline 仅报告，不采用通用提前安全保证。

## 2604.16826v1 Pico — 6 分知识缺口深入，Ch30 提案：通过

[官方 HTML v1](https://arxiv.org/html/2604.16826v1) §4.1–4.2 与 §5.1/5.3 表格实际读。拼接任务 B 的 SVD、归一化奇异能量 shrinkage、再恢复有效 delta 的范数，是输出因子侧的预合并校准，不只是普通 delta 相加。

实际 Ch30 “多个 Adapter 能否直接相加”、ACT-Mat 与因子 gauge 身份的相邻正文缺该窄分支，可在 ACT-Mat 后补充。B 的能量只在固定参数化下作 proxy：B→BR、A→R⁻¹A 可保留 delta 却改变 B 谱，不能自动称 gauge-invariant 或真实共享任务数。finance 退步、范数恢复消融的非全面优势、SVD 构建与最终行为验证成本均保留。仅 source→owner PASS，未写入。

## 2604.16830v1 CaOPD — 6 分纠错深入，窄争议：通过

[官方 HTML v1](https://arxiv.org/html/2604.16830v1) §2.1–3.2、Appendix A.1 Eq8–10 与 B.1 实际核。对同一 joint 的条件期望塔律本身有效；争议在于 §2 不同 generation policies 下的 teacher 成功率与 deployment student 成功率之间缺识别桥。

固定 x，Z 等概率，teacher 条件成功率 .4/.8 的最小 MSE 投影为 .6，而无 Z 的部署 student 可以为 .2。同参数而不同 prefix 不强制该边缘相同。只隔离普遍部署校准/保持保证，不否定经验有效性。K 次 rollout 均值估 prompt-marginal 成功率，不直接是已经生成的单条答案概率；loss mask 也不冻结共享参数。恢复需明确共同生成律、边缘桥或收窄保证，不写该保证入 Books。

## 2604.16834v1 HE Batch Pipeline — 5 分标准，仅报告：通过，补硬件精度

[官方 HTML v1](https://arxiv.org/html/2604.16834v1) §VI Eq24–29 与 key residency、§VII A 实际核：downsampling 释放 CKKS slots，经 mask/rotation accumulator 合并中间 ciphertext；block group 的 key 驻留与更换是具体布局/内存机制。

官方明确 Xeon Gold 5418Y、32 cores/32 hardware threads、256GB、Rocky Linux 8.10、OpenFHE 1.4.0 和 HE 参数，不能把 hardware 全记未披露。仍缺逐请求尾延迟/并发/SLO 证明，per-image 摊销不能替代该合同。实际 Ch72 privacy/encoding/cost 分账可承载边界；受限 HE-friendly ResNet 配方仅报告，不能迁移成 Transformer 加速或 encrypted training 保证。

## 2604.16838v1 enclawed — 前分母关闭：通过

[官方 HTML v1](https://arxiv.org/html/2604.16838v1) 当前标题/preamble 与 §9.2–9.4 实际读到 204 tests/22 files、Set freeze 可变及 Promise-queue 日志问题。旧库存的 356 tests/proof-carrying 主张不能回填，恢复后的 v1 不应继续按日期或材料污染隔离。

BLP lattice、deny-egress、manifest/DLP/hash log/rollback 是有明确 trust 假设的成熟 host 硬化组合；这些具体实现修复未建立超出既有 host authority 的 AI-specific 新控制保证。single-user high-trust 假设不是敌意多租户证明。具体贡献门槛关闭，不评分、不列 selected、无 Books 决策。

## 2604.16845v1 DART — 6 分保护/评价深入，仅报告：通过

[官方 HTML v1](https://arxiv.org/html/2604.16845v1) 必要 App A.2（stage protocol）已实际核。分类 correctness 与生成 rationale 的 harm 可反向变化，paired audit/repair 是有效受限信号；不能把 gold-conditioned distillation 当梯度隔离。

原文明确 test prompts 上查 drift、用相应 gold/safe rationale repair，并在同 test 集报告 Table2，是 deliberate transductive post-hoc repair。它可能修复已知案例，却不是独立 held-out 泛化证明；不背诵原 rationale 不能消除 prompt/label 参与。Ch66 training/selection/outcome 分账支撑采用边界，本 pipeline 仅报告，不能把全部算法称 Existing 或将双 pass 成本省略。

## 2604.16850v1 I2RLC — 5 分标准，仅报告：通过

[官方 HTML v1](https://arxiv.org/html/2604.16850v1) §III.C–D Eq3/算法、§IV.C–D 实际读。逐速 reference warm-start、真实 tracking-error 更新与低层 compliance 之后生成 ACT demonstrations，区分轨迹 proposal 与物理执行职责，有可定位贡献。

实际 Ch26 observation→proposal→controller→actuator 闭环已承载采用边界，不因此称整套算法已有覆盖。有限确定性试验与同 update-budget 比较不提供一般安全保证；两种方案插孔均 100%，擦除仍有残留且并非每指标更好。保护停止的失败运行与报告口径不能被平均效率吞掉，不采用通用十倍速度/VLA 迁移结论。

## 交接

本批无待核普通审计项；IA/Pico 下一步仍需共享章节许可、实际最小正文、非作者写后复核。窄争议只隔离命名命题，保留实验与有效机制。日期组合证据、来源覆盖、候选冻结及日级完成由作者与独立日级 reviewer 处理，本文件不替代这些 Gate。
