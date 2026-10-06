# 本日第四批必要证据（root 实际必要原源及六项仅报告处置通过）

精确v1，六项均2+1+2=5；必要原文各在CORE_STANDARD_<id>v1.txt。不含代码核验或复現，不采用宣传普遍性。

root 已实际核方法、直接反侧与处置：选项/neutral 分母变化、critic预算不匹配、固定QK/iidV理论限制、teacher/index-storage与指标冲突、同题与token预算差异、attribution与utility反退均保留。六项仅报告判断通过，不声称精确配方已有书稿覆盖，无Books修改。

## 2601.21975 — Stated/Revealed Elicitation

§2–3.3及必要B/C协议：24模型、16values、AIRiskDilemmas3000，五prompt模板，temp0/top-p.01、GPT4o-mini分类；只将decisive binary comparisons构rank，neutral从分母去除。forced/forced→expanded-stated/forced通常相关提高，再expanded/expanded则多组趋零/负，且neutral>99%模型排除；因此变化不仅“价值更一致”，也更换了有效比较人口。capability相关n16/ρ.58只是模型间相关，不授能力因果。system steering只部分模型改善、Claude反退。B描述旧Litmus Elo，当前§2明确win-rate，不能把旧Elo流程强继承本次代码实现；未核artifact。硬件/precision/API exactrevision、排序不确定性/完整调用成本Not Disclosed。

拟仅报告：PLATFORM-EVALUATION-SYSTEM 的选项集合/弃权与有效分母是评价身份；本篇有局部protocol反转证据，但不证明latent真实value hierarchy或系统prompt可普遍修复。具体elicitation case留日报，不把主题相似当本算法已有覆盖，不强造书稿diff。

## 2601.21972 — CoLLM

§4–6/Alg1/Table1、C/G：CC读joint history及global progress；actor各自私有KV执行，critic只训练时存在，DC不等decentralized execution的必要条件。sequence-action logprob由teacher forcing相加；理论无偏依赖critic收敛，K叉树方差结论要求独立gradient/无earlytermination，不给任意共享prefix rollout通用方差保证。

H1 writing/密reward、H2 coding/稀reward、H4 games；K4或2。CC/DC/MonteCarlo的critic配置与train epochs不相同（writing20vs2、coding80vs8、games120vs16，LR/buffer也不同），sample效率曲线不是同FLOPs。C测试100/100 writing、16coding、每游戏2题，五runs bootstrap只覆盖该小population。writing metric是length/Jaccard/transitionword proxy，不是人工logical truth；单模型故意singleturn/较大size，不是等反馈基线。Table1CC不是各项最优，例如coding2.6s slower MAGRPO2.3s、HouseHP86.4低于singleAC100；model/token cost/latency不可合一。训练H100/H200/B200，推理RTX5090/Ryzen9950X；precision/batch/concurrency/SLO及critic训练E2E成本ND。主文局部short/dense与long/sparse差异可留，不能从跨task推纯horizon因果。

拟仅报告：AGENT-MULTI-AGENT 的execution topology与training critic是不同设计，当前材料支持小协作population的critic取舍，不建立新的部署控制权限或开放Agent普遍优势；未知joint-state/critic不稳时仍保留MC与独立真实outcome，不称具体CoLLM已有覆盖。

## 2601.21942 — Stochastic Transformer Clustering

§3–5明确模型：无FFN/position机制，K/Q固定、V层间iid centered bounded entries/方差固定，residual1/sqrt(L)，逐token unit-sphere RMS。Theorem1仅L→∞分布收敛，共同matrix Brownian与Ito radial drift保证sphere约束；并非训练过程convergence。Theorem2相变只N2及QᵀK=I，d−2与cosh(2β)决定antipodal概率；hybrid Proposition1又仅unnormalized USA、N2、scalar bounded noise，ε²与2exp(−β)严格两侧，不授等号/任意QK。

拟仅报告：MODEL-SELF-ATTENTION 的deterministic collapse解释应标明随机初始化/scale/RMS条件，原文给受限数学反例而非现代trainedTransformer设计处方；不采其公式阈值作为训练超参或通用antipodal collapse，必要假设与具体结论已核，证明附录不在采用范围。

## 2601.21896 — PaFu-KV

§3.2–4.3/A：双向real-score teacher把past/diagonal/future分块max再均值作为salience label；线上last-layer QKV→S-MLP只能预测future relevance，attention label不是实际因果贡献真值。t0才用head，完成chunk后topk联合历史/current打分evict。training checkpointing不允许in-place改KV，维护index-cache与KV同步rollout，A中实际storage扩32760/51480而每chunk attention固定4680，不能称训练容量也仅4680或无需额外state。

Wan2.1 1.3B由14B DMD，自rollout+long tuning+frame sink，500warmup+2500eviction共同训练，16H200/两天；generator与SEH1e-5、critic2e-6。VBench5s/VBenchLong30s、832×480/16fps，吞吐单H100，A tensor B1；precision/实际concurrency/重复seed/eval不确定性/E2E SLO ND。Table1semantic71.36低于SelfForcing81.28/LongLive76.47，不是全质量提升。Table2 drift .29不如Rolling .01，定义absolute difference却表箭头↑，不继承方向。Table3减到3120/1560明显坏、Max/Avg与largerhead反退只局部，没same-trained-generator FIFO matched最终对照，不将所有最终收益单归future-head。

拟仅报告：INFER-KV-CACHE 当前identity-compatible缓存/approx selection已要求state绑定；本篇未来teacher→causal score及index-checkpoint具体配方具有增量，但未证明prediction可认证future效用或新通用缓存正确性。保留实际teacher可见性/训练storage/指标反侧，不声称正文已有该算法。若root认定checkpoint index接口存在具体长期差额再窄PRE，不凭score head名称改书。

## 2601.21894 — Not All Code Is Equal

§3–6/D：CodeNet同problem-language不同accepted solutions，CC或LLOC within-problem选min/low/mid/high/max；Instruct不同problem跨difficulty，并不是同题。每split8087样本、NL ShareGPT8087、2epochs相同LoRA配置，但高复杂code更长，sample/epoch匹配不是token/FLOP/unique内容预算匹配，不能把曲线纯归结构。A100/bf16，LoRA16/alpha16/max32768/batch4×accum4，greedy/temp0/max16384、stepwise boxed/math-verify。六个instruct3–14B、六reasoning suites只是carrier，不转AIforScience应用。重复训练/不确定性ND，五split的Spearman与事后最高点不证明普遍最优CC≈10。

关键反侧：非单调、Llama部分负相关、Mistral U型否定“所有模型middle最佳”，不同model/metric/dataset不能合成单规律；20/24最高restricted优于ctrl也未控事后选择与token长度。拟仅报告 TRAIN-DATA 中局部code-training selection的反例：精确population支持code exposure/complexity不自动增益，不能用本篇small-LoRA curve替代大规模预训练mix、通用难度代理或因果处方。

## 2601.21864 — KnowBias

§2.2–2.4/3.1/3.5及Table3/D.3/D.7.4：bias-knowledge yes/no target的integrated-gradient attribution→阈值/跨question频率聚合FFN neurons→inference activation multiply；原权重不改不等输出utility不变，selected-neuron名字不是其内部knowledge因果真值。45questions三demographic/三type，mixed-vs-single同question预算、union-vsintersection与等数量random反侧；不能只用其论文“knowledge enhancement”声明辨识机制。

Llama3.2 3B/3.1 8B/Qwen3 4B，BBQ ambiguous/disamb、CrowS/SS各不同目标不平均成统一安全truth。Table3 KnowBias Qwen OBQA .7779→.7401、Llama8B COPA .7132→.6780，所有保留不伤不成立。λ过大无益/退化，D.7.4称2最佳但D.3 Qwen设3.5，保留局部配置不同，不授权统一最优。D.3 A10080/AMD CPU/temp.8/max30 story配置，白盒gradient探针成本与生成吞吐/完整batch/precision/独立runs ND，不能称几乎无成本。

拟仅报告：PLATFORM-SECURITY 的activation sensor与独立utility/safety验收不授少量yes/no neurons普遍bias知识认证；这是具体enhance-vs-suppress counter与recipe，不能推任意人口公平、安全effect或跨模型不变，不因可映射owner强制整合。
