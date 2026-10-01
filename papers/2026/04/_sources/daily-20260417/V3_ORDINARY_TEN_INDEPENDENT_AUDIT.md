# 2026-04-17 V3：普通十项有限独立复核

## 范围与结论

仅复核 14531、14820、14853、14922、15075、15109、14267、14568、14806、14528。复用已完整阅读且本任务未变更的 AGENTS、研究合同、报告合同与统一 Prompt；逐项重新打开官方 exact-v1 HTML 的必要方法和关键反证，直接比较 ROADMAP 的实际 Books 命题。本轮不扩大 536 raw / 88 candidate，不重做已通过的其他单篇复核，不遍历全部附件或版本史，不修改作者 README、Books 或全局 checkpoint。

下表 PASS 是单篇证据与窄处置的裁决；需修正的事实由作者同步后才能把对应正文作为终态使用。本文件不证明整日日期、Coverage、分母或 Daily Gate 已通过，也没有复现实验。十项均维持作者 `Design Delta 2 + System Reach 1 + Durability 2 = 5`；没有因主题命中而加分或自动写 Books。

| Family 后缀 | 单篇裁决 | 采用处置 | 实际 owner / 比较位置 |
| --- | --- | --- | --- |
| 14531 | 修正 coverage-floor 口径后 PASS | Weekly Only — Context（本日仅报告） | INFER-SCHEDULING / PLATFORM-EVALUATION-SYSTEM |
| 14820 | PASS；保留已披露的受限 wall-clock 结果 | Weekly Only — Context | TRAIN-GRPO / AGENT-REFLECTION |
| 14853 | PASS | Weekly Only — Context | INFER-SCHEDULING |
| 14922 | PASS；修正扰动证据规模表述 | No Change — Existing Coverage | TRAIN-LORA |
| 15075 | PASS | Weekly Only — Context | INFER-SCHEDULING |
| 15109 | PASS | No Change — Existing Coverage | PLATFORM-EVALUATION-SYSTEM |
| 14267 | PASS | No Change — Existing Coverage | TRAIN-GRPO |
| 14568 | PASS | Weekly Only — Context | TRAIN-GRPO / MULTIMODAL-REPRESENTATION |
| 14806 | 修正 baseline 身份后 PASS | Weekly Only — Context | MULTIMODAL-REPRESENTATION / TRAIN-GRPO |
| 14528 | 修正 benchmark 名称后 PASS | No Change — Existing Coverage | AGENT-REFLECTION |

## 逐项 source → owner 审阅

### 14531 — TRACER

[exact-v1](https://arxiv.org/html/2604.14531v1) §3.1–3.3、§4.1–4.2：teacher trace 提供分类标签；BGE embedding 上训练传统 surrogate，acceptor 用 top-1/top-2/margin/entropy 预测 teacher agreement，再在 held-out calibration 选择阈值。独立 shadow split 不参与训练和阈值拟合；未达到 gate 时继续依赖 teacher。新贡献是把 trace、surrogate/acceptor refit、shadow promotion 与 fallback 组成受限 continual-routing 配方，不是模型“知道事实”。

必须修正：§3.3 的 **5% 是 surrogate coverage floor**，用于拒绝近零覆盖的 pipeline；它不是 shadow split 大小或 5% 在线抽检比例。MNLI 的 negative control 用 ground-truth label 作为 stand-in teacher，并非所有任务都由 Sonnet 4.6 生成标签。五个 daily batch 是缓存 trace 的模拟；CLINC150 calibration TA=.952、test TA=.930，低于 .95 目标，不能称部署质量保证。价格投影也不含完整 embedding/refit 成本。

[Ch56](../../../../../books/part-05-inference-system/56-inference-scheduling.md)“从经验 confidence threshold 到有条件的 Risk Contract”实际拥有 commit/defer、tier selection 与成本；[Ch66](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)拥有 evaluator/label/calibration identity。它们承载主要风险分权，却没有因此实现这套 teacher-trace→classical-surrogate 配方；不虚写全机制 Existing。**Only PASS**：保留该受限增量及 gate 失校准反证，不新增同义主干。缺 trace、teacher 本身有偏、标签变化或校准漂移时，直接 teacher/人工标签仍是成立分支。

### 14820 — SWE-TRACE

[exact-v1](https://arxiv.org/html/2604.14820v1) §3.2、§4.1–4.4、§5.1–5.2、§6.3 Tables 3–5：synthetic-bug metadata/repair scope 只给生成期 oracle；贪心选步和删除动作后重验不证明全局最短路径。PRM 学习 completed-trajectory rubric ranking，推理时再评分 candidate-extended partial prefix；这次角色转换是启发式，不是已获得可靠的 step-value 或逐动作因果标签。新贡献是合成轨迹、rubric PRM 与 action-level guide 的受限组合。

同起点 4B/30B ablation 支持作者环境中的贡献；privileged repair scope、rubric judge、测试遗漏及 prefix transfer 仍是 failure surface。**Table 5 确有 wall-clock min/issue**：30B parallel rollout 63.8、HG-TTS 36.5；不能说完全没有 latency 证据。这个结果不证明完整 guide/训练/环境成本已等预算，也不是生产并发/SLO；active parameters 或 token 数不能代替全部 compute。

[Ch33](../../../../../books/part-04-training-system/33-grpo.md)“Phase-specific Credit / Milestone”要求 boundary、mask、reward 与 verifier 分权；[Ch80](../../../../../books/part-07-agent/80-reflection.md)把 critique 作为 bounded proposal 而非 oracle。现有主干不因新 recipe 自动缺 owner。**Only PASS**：留报告中的真实方法、受限效率和监督迁移风险，不把具体框架摘要堆进 Books；短轨迹、可靠 execution verifier 或高 guide 成本时，execution-only/完整轨迹比较仍合理。

### 14853 — Solve-then-Learn

[exact-v1](https://arxiv.org/html/2604.14853v1) §3–4、§5.1–5.2：离线 question×budget utility 表上确定 dual price 和 oracle budget label，随后蒸馏成 cheap classifier；deployment 一次分类后调用所选 budget，不在线更新 price。新贡献是离线求解再摊销预算决策，不是由 classifier 获得真实效用 authority。

Theorem 3 允许 imitation error 把 **平均**预算上限扩大为 `B + epsilon × cost-range`，不能当逐请求 hard cap；有限离散 deterministic allocation 的 staircase 与附录随机策略条件不得混写成无条件 primal 最优。200 MATH、200 GSM8K、48 responses/question、五档 self-consistency、80/20 与三 seeds 只支持受限实验；entropy feature 的单次 LLM 调用和离线采样也要付费。

[Ch56](../../../../../books/part-05-inference-system/56-inference-scheduling.md)平均成本/dual feedback 段与“Answer 前 Routing 只能预测反事实效用”实际区分 router proposal、真实计费和 hard admission。主要分权已存在，新离线配方与理论并未迫使改变主线。**Only PASS**；utility 漂移、冷启动或高风险时冻结/保守固定 budget，不能借用 oracle 标签宣称模型自知。

### 14922 — LongAct

[exact-v1](https://arxiv.org/html/2604.14922v1) §3.3 Eq8–11、§4.1/4.3/4.5–4.7：current-batch Q/K 每 head 的高幅度 feature 选择对应 row-gradient mask；不是 LoRA，Wv/Wo/MLP 不据此全部冻结，整模型 backward/activation/optimizer cost 不能按 30% 推算。8×H800、Qwen3-4B/8B 长上下文 RL 只支持指定配置；8B RULER-64K QA 相对 DAPO 40.40→34.90，不能写各切片单调改善。

必要补充：正文 Figure 6 是一个展示 case，但 **Table 8 的指定 clamp-to-global-mean 干预统计了 503 例**；作者 notes 的“少数 real-world case”不能代表全部扰动证据。此结果仍不证明跨分布稳定因果 saliency，干预本身可能损坏表示。

[Ch30](../../../../../books/part-04-training-system/30-lora.md)当前 batch→per-head statistic→transient row mask→discard 的实际正文（本轮读到约273–287行）已经包含 base update、momentum/variance、mask churn、saliency drift 与相同 H800 边界。**Existing PASS**，不是仅因章节讲 parameter-efficient training。需要小 artifact/稳定恢复时固定 LoRA/row mask，容量优先时 full update，仍分别成立。

### 15075 — Atropos

[exact-v1](https://arxiv.org/html/2604.15075v1) §3.1–3.3、§4.2–4.4、§5.1–5.3：多轨迹 SFG 经 GCN 预测失败；parallel mode 在 active trajectory 继续时保留 prefix，而 sequential mode 只更换尚未生成的完整 trajectories，**后者没有 context migration**。这是新的受限 risk predictor / termination-hotswap recipe，不是所有 provider 都可无损切换。

“Context stateless”不证明 KV、tool effect 或 provider protocol 兼容。5-fold 的每折 holdout 再分 validation/test，合并 test 只占全数据50%；3090仅覆盖本地 GCN/Llama，其他模型是 API。费用是 tokens×公布价格，不含在线 GCN 与调用延迟；Table 2 AutoFL/Llama3 多个指标低于 voting confidence。RepairAgent 的 plausible-patch 标签也不是通用语义正确性 oracle。

[Ch56](../../../../../books/part-05-inference-system/56-inference-scheduling.md)“Model Switch Point 是生成中的版本边界”精确区分 scheduler switch、runtime committed-prefix/KV、compatible context 和不兼容重算。主线已有覆盖，但不声称包含新的 GCN recipe。**Only PASS**，保留受限失败预测贡献，不采纳普适无损 hotswap；状态不兼容、预测不稳或切换成本高时单模型请求仍更可靠。

### 15109 — IUQ

[exact-v1](https://arxiv.org/html/2604.15109v1) §3.1–3.5、§5.2–5.4 Tables 2–4：atomic claim 改写为至多三问，新 session 仍条件化原 prompt `x`，不带原 long response；同一模型生成、interrogate、判断 contradiction，再用前序衰减 kernel 汇聚。贡献是结构化 context intervention/矛盾分数，不是 fresh session 产生独立 truth authority，也不消除同模型系统偏差。

235 FActScore / 250 LongFact 的 Table 3 是 GPT-4o 生成的累计61,161短答，不是每请求成本或所有模型相同调用量；Table 2 GPT-4o/FActScore 没有全面胜过 baseline。AUROC 是区分能力，非校准正确率。拒答样本排除会改变 coverage；ground-truth/reference 的取得与同源 uncertainty estimator 必须分账。

[Ch66](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)“Atomic Claim 置信度怎样合成整体结论”和“对抗性相关错误：低熵与高共识也可以稳定地错”实际要求 claim dependency graph、独立 evidence、calibration/readout 分权，同源 samples 只支持 distribution description。**Existing PASS**，采用这个实际边界而非照搬 IUQ kernel。无独立材料时检索/可执行 verifier/abstain 仍是最终分支。

### 14267 — CW-GRPO

[exact-v1](https://arxiv.org/html/2604.14267v1) §3.3–3.5、§4.1–4.3、§5 Tables 2–3：judge 的 retrieval utility×reasoning validity 二值 product 经 softmax 分配成功轨迹 round advantage；失败轨迹 uniform，final-answer advantage 保持原值。平均 round advantage 守恒不等原 parameter gradient、不偏因果 credit 或稳定性保证；97 rounds 的95%人类 agreement也不是因果 oracle。

Qwen3-1.7B/8B、verl/SGLang、2018Wiki/E5/top3、200 steps、32×4 sampled trajectories、9192 context/10 rounds、Avg@4 和经72B筛出的 hard cases限定评价。1.7B Hotpot 27→24、有限 alpha 的总体反例保留；没有完整 judge/硬件/精度等预算比较，prompt 禁止 parametric knowledge 也不证明模型实际没有使用 weights。

[Ch33](../../../../../books/part-04-training-system/33-grpo.md)“Verifier 拥有方向，Privileged Teacher 最多调节幅度”及 phase/segment credit 正文实际已有权重改变参数轨迹、negative outcome reset、boundary/mask 与 causal attribution 限制（本轮约510–577行）。**Existing PASS** 采用这套 authority/credit 边界，不声称 exact conjunctive recipe 已全部写入。Judge 不可靠或预算昂贵时 ordinary outcome-GRPO 仍是成立分支。

### 14568 — Adaptive Visual Reasoning（AVR）

[exact-v1](https://arxiv.org/html/2604.14568v1) §4.1–4.3 Eq2–7、§5.1–5.2、§6.2–6.3：这是 **visual** 而非 audio。三格式 full perception→reasoning→answer / perception-only / direct 在 SFT 后由 correctness-dependent format bonus、decaying group diversity 和 length factor训练选择；直接答案只是省略显式 perception trace，不证明视觉编码器没有工作。新 contribution 是受限格式竞争与 collapse mitigation，不是校准自知。

Qwen3-VL2/4/8B、11k SFT/44k RL、七 benchmark、非MCQ GPT-4o-mini judge 的结果不证明生产成本；2B MathVision30.1→29.8、MMMU-Pro27.5→26.9及 L 阈值敏感性必须保留。长度缩短不直接等于 latency/SLO，格式探索也会增加训练/评价成本。

[Ch33](../../../../../books/part-04-training-system/33-grpo.md)“Reasoning Cost 也是版本化的 Reward Prior”实际承载 cost/prior/verifier/hard-cap 分权；[Ch23](../../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)区分观测、可检查 trace 与隐状态预算。没有必要复制这一局部奖励 recipe，亦不能说无机制贡献。**Only PASS**；复杂视觉/高风险仍保留完整证据，简单任务可用直接路径。

### 14806 — HyPeR

[exact-v1](https://arxiv.org/html/2604.14806v1) §4.3–4.6、§5.1–5.5 Tables 1–2：lowest-group token probability 决定 PAUSE/abort，最多3×64 latent tokens；ASR Levenshtein、background cue gate、reasoning-answer consistency 是 reward sensors，不是音频真值。新 contribution 是特定音频 hybrid gating+reward recipe；概率门槛、关键词 cold-start prior 和隐藏状态分析不证明系统自知或 latent 因果贡献。

必须修正：Table 2 Music **62.27<65.90 是 HyPeR 对外部 Qwen2.5-Omni-7B**，65.90不是其训练 base。训练 base Qwen2-Audio-7B-Instruct 的对应 Music53.59，SFT44.61，HyPeR62.27；所以可以说 SFT 有退步、HyPeR 未超过该外部 baseline，但不能说 HyPeR 在这个 Music 子项低于自身 base。更多 reflection turns 退步仍是有效反证。Table 1 与正文 WER/CER不一致不照录；claim“排除幻觉”不成立。

[Ch23](../../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)约416–425行实际区分 latent transitions、训练 scaffold、不可直接观察的表示与可检查的工具轨迹；[Ch33](../../../../../books/part-04-training-system/33-grpo.md)成本 prior 保留附加 forward 与 hard boundary。**Only PASS** 保留真实新配方与边界，不称完全 Existing；简单音频仍可直接前向，关键 speaker/ASR claim 需原音频/外部验证而非同源一致性。

### 14528 — Failure Dynamics / GUARD

[exact-v1](https://arxiv.org/html/2604.14528v1) §3、§4.1–4.3、§5/Table1：事后 failure onset 用 Gemini3Pro+人工标签定位，runtime 仅在 delimiter 后检测 entropy 相对历史 quantile；greedy / Wait / reconsider 三短分支选低平均 entropy，late phase 另用剩余预算与 hesitation marker 控制终止。新 contribution 是 selective entropy-triggered intervention 实例，不证明所有错误都早期可观测或低熵分支更真实。

必须修正：7B **87.5→90.6，Reflexion92.6 是 MATH500，不是 GSM8K**。Table1采用1.5B/7B/QwQ32B八任务；一些子项其他方法更好，主序列 token 不是全部分支费用或 wall-clock。共享 prefix KV 可以降低部分执行重复，不等其内存/latency开销无条件很小。

[Ch80](../../../../../books/part-07-agent/80-reflection.md)约196–214行实际已有 cheap entropy sensor→calibrated threshold→selective diagnosis→bounded repair，以及 logits/额外分支、稳定不等truth、probe/token不等latency。**Existing PASS** 采用此控制/证据边界，不声称全部GUARD recipe已实现。高风险/校准失败时独立 verifier，必要探索时继续有预算的检索，短简单任务直接回答，仍共同成立。

## 交付边界

十项必要官方正文已核，四项 Existing 均有实际正文而非仅主题映射，六项 Only 均保留具体贡献与不吸收理由。作者需同步 TRACER 的5%口径、HyPeR对照模型、GUARD benchmark，及 LongAct扰动规模；SWE-TRACE 的 wall-clock披露应作为受限证据保留。此批没有发现必须新增 Books 的窄 gap。最终日期归属、分母冻结及整日验收仍由各自 owner 完成。
