# 2025-09-11 精确版本定点证据

作者 Bacon，2026-10-06。按 [研究合同](../../../../../docs/RESEARCH_CONTRACT.md) §3–6。以下七项通过 root 的贡献潜力校准，但首次公开落窗仍缺证；这是保留的必要反侧阅读，不是七项正式候选或完整 Evidence Gate。没有运行作者代码、复现或生产验证。HTML 文本与 PDF 页文本为原文转换，不把已下载附件称为全部已读。

## 2509.08309v1 / Hetis

[精确 HTML](https://arxiv.org/html/2509.08309v1)，原件 `html-2509.08309v1.raw`，已定点读 §3.1–3.2、4.1–4.2、7.1–7.4。Primary worker 做 dense 与 prefill，decode attention/head/KV 可交给 attention worker；head 切分减少 sequence 切分的 query 复制，代价是搬运与动态配置。TP/PP/DP 子集搜索有近似筛选及 Δ=0.05 阈值，不是全局最优证明。

默认作者实机为 4 A100 80GB、4 RTX3090、4 P100，100Gbps LAN、机内 PCIe；Llama-13B/70B、OPT-30B，ShareGPT/HumanEval/LongBench。Splitwise 是作者重实现，不能自动授生产 engine 等价。P95 TTFT/TPOT 与未饱和请求率分开，不能把吞吐比当 SLO 保证。原文有 13% 额外 head-cache storage-operation 开销，不能照录 Hauler 的零开销宣传。160 GPU 是配置模拟，非实机；profiling ±20% 对实验 latency 的影响最多 6.9% 仍属受测设置。

若日期恢复，拟采用命题应是模块级算力/容量分工的条件与成本，不是所有异构集群普遍加速。完整在线迁移/状态一致性拟采用时还需定点 §5–6；当前不把未读内容记完成。潜在 owner `INFER-PD-DISAGGREGATION` [Ch55](../../../../../books/part-05-inference-system/55-pd-disaggregation.md)：已实际读开头“workload-specific break-even”、KV transfer/排队代价，与 Ch54 GPU capacity、Ch56 SLO 调度邻接。没有提交 Books 写入建议，因为日期尚未成立且该命题实现证据未完全关闭。

## 2509.08342v1 / MoEpic

[精确 HTML](https://arxiv.org/html/2509.08342v1)，`html-2509.08342v1.raw`。定点 §3.1–3.4、4.1–4.5：expert 纵向 top/bottom 分段，top 驻留扩大 cache 覆盖，bottom 预取与已驻留计算重叠；预测错仍加载真实 router 所需 expert，不以预测结果替代路由。首层借前 token 激活，初始层预测更差。Cache priority 同时计频率与间隔；配置器依赖实测命中/预测概率，连续松弛与 fixed-point/divide-and-conquer，不能称全局最优 guarantee。

作者 AMAX/Xeon8358P/512GB RAM、A6000 48GB、PCIe4x16；Qwen1.5-MoE FP16，Mixtral attention 4bit/MoE 2bit HQQ，MMLU。默认相同 expert VRAM budget，5 次均值；未读到误差条、请求 concurrency/SLO/长度分布或每项 GPU 数的明确绑定，写 `Not Disclosed` 而不补造。w/o SP 用随机预取、w/o LCP 用随机 cache、w/o CCA 同时 uniform allocation + split 0.5，复合消融不能把全部收益单归 expert split。Fig8 prose 把目标 TPOT 写成 TTFT，不采用该术语错配作结论。

可保留“缓存单位可以小于整 expert，错误预测仍需 exact fallback”的受限机制；尚未核公开实现或数值逐元素等价，不能授无损生产运行。潜在 owner `INFER-GPU-MEMORY` [Ch54](../../../../../books/part-05-inference-system/54-gpu-memory.md) 已读 HBM 的 weight/KV/workspace/communication/reserve 共同约束，与 Ch53 topology / Ch55 handoff 相邻；日期恢复后才比较精确 owner 差额。

## 2509.08184v1 / Selective Induction Heads

[精确 PDF](https://arxiv.org/pdf/2509.08184v1)，完整原件 `2509.08184v1.pdf`；HTML 定点 §4/5.1，PDF pp10–13 §5.2–7 补足反侧。对象是已知固定 transition matrix、有限 alphabet、不可约非周期 interleaved Markov chains 与未知 lag，不是现实因果发现。三层 disentangled 构造依次提取归一转移概率、按 lag 聚合，再 softmax/copy；不是 Bayesian model averaging 的 posterior，因为累加 normalized probability 而非 log-likelihood。

**§5.3 Claim1 的一般情形完整证明明确留待 future work。** 作者只对 two-lag/no-normalization、independent-lag 特例给附录证明；本次未核附录 A 全证明，不称一般 K 下已证明 MLE 收敛。§6 小 alphabet、长度128、fresh batch256、Adam LR0.001、三层构造/训练对照；单头训练模型可胜提出的构造，不能说多头机制唯一必要或普适最优。

潜在 owner `MODEL-MULTI-HEAD-ATTENTION` [Ch15](../../../../../books/part-02-model/15-multi-head-attention.md)，实际正文“可分化的表达路径不等于必然独立能力”及“attention pattern 只提供行为线索”已读。邻接 [Ch14](../../../../../books/part-02-model/14-self-attention.md)/[Ch16](../../../../../books/part-02-model/16-feed-forward-mlp.md)。若恢复日期，可自然接在 head 分化论证后，以合成 Markov 构造说明结构选择与概率学习的分工，同时保留一般 Claim 未证及单头反侧；这是条件路由，不授权写入。

## 2509.08358v1 / Toxic Synthetic Text

[精确 HTML](https://arxiv.org/html/2509.08358v1)，`html-2509.08358v1.raw`，§1–5 核心与风险。activation patch 的 Llama3/Qwen3/Cogito 生成毒性文本，再训练 BART-large detoxifier。Human ParaDetox J=0.481；同源 synthetic ParaDetox 0.428–0.459；SST2 source 0.322–0.362。Unique insults 与频率支持多样性缺口，但不是控制多样性的因果干预；SST2 语义分布变化也是替代解释。

标题为 Human Evaluation 的段落实际用 GPT-4.1 judge，不应报告成人工被试。训练总预算、重复 seed/CI 在所读材料中 `Not Disclosed`。可保留该 detoxification 方向的局部反证，不外推所有 synthetic data 必失败。潜在 owner `TRAIN-DATA` [Ch27](../../../../../books/part-04-training-system/27-data.md) 的 Synthetic data 段已实际说明 generator/judge 共源 blind spot 与真实支持集、联合 seed 多样性条件；相邻 Ch26 embodied input / Ch28 pretraining。日期恢复后，建议将本反例自然嵌入支持集检验段，明确 lexical coverage 与 downstream utility 分账，不用一条相关性宣布通用因果。

## 2509.08755v1 / AgentGym-RL

[精确 PDF](https://arxiv.org/pdf/2509.08755v1)，HTML 404。首次 PDF 传输不全保留为 `2509.08755v1.pdf`；另件实际续传至 11,939,091 bytes、39页可解析的 `2509.08755v1-complete.pdf`。定点 pp8–13、17–18、31–33；Fig7 p12 已实际渲染查看 `agentgym-figure7.png`，不是仅提取标题。只采用 WebArena/Deep Search 的 horizon 机制，不采用 SciWorld 数值或全五场景平均。

§3.3 以 monotone interaction horizon schedule 从 exploitation 转向 exploration；Fig7 的 10-turn 对照早升后坍塌，5-turn 稳定但较低，渐增曲线局部更好。曲线没有重复 seed/CI，不能把 caption 的 variance/credit/overfitting 原因当因果辨识，也不能据图保证普遍训练稳定。WebArena Table1 中同 7B baseline 22%、ScalingInter 26%，不是 +10 percentage points；低于 o3/o4-mini。Appendix B.1 372训练/50测试，从原812中排除会修改站点状态的 Content & Config，15-turn、GRPO LR5e-7、KL1e-3、每题4轨迹、temperature1。B.2 搜索7集合400例、最大4turn、LR1e-6/KL1e-3/8轨迹；与 Fig7 的训练 horizon 应区分。A100/Ascend910B 披露，不同实验精确卡数/精度/墙钟预算 `Not Disclosed`。

§5.3 WebArena 仍有冗余点击/滚动，状态可达不等于高效有效完成。可保留 horizon 是课程变量的局部证据，不把 benchmark 的所有优势归课程，训练/测试环境、预算与复现仍须绑定。潜在 `TRAIN-GRPO` Ch33；当前未做完整该巨章的差额核，不能声称已有覆盖或授权新增。

## 2509.08721v1 / SAPO

[精确 HTML](https://arxiv.org/html/2509.08721v1)，`html-2509.08721v1.raw`；§3.1–3.2/Algo1、4.1–4.2、5–7。各节点独立 policy，分享 decoded question/answer/verifier 信息，再本地 retokenize。核心按自己的 policy likelihood 使用外部轨迹；没有从本次所读核心得到 behavior policy importance correction 保证。不能从允许异构 policy 推“无需 off-policy 约束”。

受控实验8个Qwen2.5-0.5B节点/每节点一GPU、GRPO KL=0、clip0.2/0.28、LR0.001、2000 rounds、8训练task/round。4local/4external 的 1093 vs561.79 是 cumulative reward，非任务 accuracy +94%。外部零 advantage 过滤及 pool/subsampling 有预算差；2local/6external 更振荡。异构数千节点 demo 的 Qwen3-0.6B 无改善，且 demo 外部采样与受控实验不同；论文按 agent min/max 给的区间不是独立重复统计 CI。

可保留独立 policy 的经验共享与过滤/支持条件，不能授任意 async 收敛、安全抗污染或 scale 成本保证。潜在训练 objective owner `TRAIN-GRPO`，运行通信才归 `TRAIN-DISTRIBUTED-TRAINING`；不把 inference-time Multi-Agent 当同机制。日期/必要证据恢复前不提交自然整合段落。

## 2509.08826v1 / RewardDance

[精确 HTML](https://arxiv.org/html/2509.08826v1)，`html-2509.08826v1.raw`；§3.1–3.3、4.1–4.2/Tables2–3、4.4/Tables7–9、5–6。比较 image/reference/prompt/task instruction，以 yes-token probability 得 reward；InternVL1–26B、SEED-VL1.5 CoT teacher、先 decision 再 explanation。ReFL 的 Best-of-N reference 由 reward model 自选；test-time path pruning 与训练 reward 的成本不同。

Image240 prompts、Video SeedVideoBench300及 GSB=(G-B)/(G+S+B) 不直接合并成 accuracy。ID2500 与 OOD4000/ImageReward/HPS 的 RM 评价分开；ID accuracy 非单调，OOD 相关性不是机制因果。Table7 的参数化、Table8 reference 质量/预算、Table9 CoT 均改变条件。**1000-step reward variance 不是 CI，也不是没有 hacking 的证据。** 未读到独立自适应 hacking 检验或因果 mode-collapse 指标，不采用“解决 hacking”主张；局部独立偏好结果仍有价值。训练硬件/总steps/精度/annotator数/CI 在所读设置 `Not Disclosed`。

潜在 owner `TRAIN-RLHF` [Ch31](../../../../../books/part-04-training-system/31-rlhf.md) 实际开头已有“relative preference→reward proxy→reward hacking/rollout cost”的链；Ch30 LoRA / Ch32 PPO 邻接。日期恢复后应接 reward 参数化选择而非安全保证段，以比较式生成 reward 的输入条件/reference 成本限定替代回归 RM 的分支；没有正式写入建议或 Books Gate。

## 2509.08646v1 / Secure Plan-then-Execute 安全反侧

[精确 HTML](https://arxiv.org/html/2509.08646v1)，`html-2509.08646v1.raw`；§2.1–2.2、3、7.1、Appendix A.1 实际代码。威胁是 tool output 间接注入；不可变 trusted plan 的 control-flow 声明借 ACE，而非本文新证明。§2.2 已承认 data corruption/mail 恶意内容。

A.1 的 executor 由 Pydantic step 的 tool_name 选一个 tool，再 `create_react_agent`，把 raw past_steps 送入 context；限制工具集合不证明参数绑定、调用次数或完整操作顺序。§7.1 replanner 又可消费 past_steps 生成新 plan，若无独立可信 revalidation，immutability 条件失效。本次未获得形式化控制流证明或 adversarial evaluation，不授 guide 宣称的注入保证。保留为**日期受阻 + 安全中心主张争议**，不是普通教程排除；root 仍须独核受影响内容。

## 2509.08151v1 的版本修复

已取并定点读 `html-2509.08151v1.raw` 的 intro、II–III、IV/V。9 Pixel8/Dell server/GPT4o-mini/WiFi；3层 semantic tree 保留 device-task 历史并让 central teacher 减少重复询问。不是参数蒸馏，也未给新的 LLM 执行 ownership 或可靠性条件。与 TMFSC/无 memory 对照说明设备 collaborator 选择的应用收益；不把 memory 部件名称本身当主线设计贡献。v1 核并未发现足以重开普通排除的新机制，关闭理由仍是本次实际新增不足，而不是小样本或“领域”标签；日期未核，按合同不另追不影响处置的日期。

## 日期保留的统一重开位置

七项及安全项 abs 的 submission history、API `published` 原值在本目录原件；月列表无日级公告。已检查官方历史 day-list 路径、advanced 页面、arXiv availability 说明；有效日级公开记录未恢复。作者 AgentGym 页没有首发时刻，DSM release 空数组不能支持其他材料日期。需要官方 announcement/archive 或作者正文首次公开记录，支持完全落在 2025-09-10T09:00+08:00～09-11T09:00+08:00 的时刻/区间，并排除更早已公开家族；不必秒级但不能只用相交日期。先重开对应日期身份，再按拟采用命题补足上述精确 §，不把整个146/月份库存转为全文队列。
