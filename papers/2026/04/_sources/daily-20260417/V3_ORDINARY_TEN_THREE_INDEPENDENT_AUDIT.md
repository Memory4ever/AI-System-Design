# Apr17 V3：第三组十项有限独立语义复核

## 范围与裁决边界

仅复核 15167、14847、14164、14191、14227、14262、14339、14379、14433、14442。复用作者的必要证据定位，独立打开 exact-v1 方法和关键反证，并比较 ROADMAP 中实际 owner 正文；未扩展 536 raw / 88 candidates、附件全集或版本历史。评分维持作者表：七项 `2+2+2=6`、三项 `2+1+2=5`，未发现算术或定义错误。

本文件的 PASS 表示限定单篇 source→owner 判断可用，不表示 Books 已写入、整日日期/覆盖 Gate 或报告 Complete。first-public 日期归属仍由整日日期审计决定；页面 submission/header 不能代替 availability。

| ID | 独立裁决 | Score | 实际 owner |
| --- | --- | --- | --- |
| 15167 | PASS — Narrow Gap Proposal | 6 | Ch49 `INFER-TENSORRT-LLM` |
| 14847 | PASS — Narrow Gap Proposal，参数矛盾不得作为默认配置 | 6 | Ch56 `INFER-SCHEDULING` |
| 14164 | PASS — Narrow Gap Proposal | 6 | Ch29 `TRAIN-SFT` |
| 14191 | PASS — Narrow Gap Proposal，修正参数冻结范围 | 6 | Ch22 `MODEL-LONG-CONTEXT` |
| 14227 | PASS — No Change / Existing Coverage | 5 | Ch76 `AGENT-RAG` |
| 14262 | PASS — No Change / Existing Coverage | 5 | Ch66 `PLATFORM-EVALUATION-SYSTEM` |
| 14339 | PASS — Narrow Gap Proposal | 6 | Ch22 `MODEL-LONG-CONTEXT` |
| 14379 | PASS — Narrow Gap Proposal | 6 | Ch24 `MULTIMODAL-GENERATIVE-PARADIGMS` |
| 14433 | PASS — Narrow Gap Proposal，修正硬件记录 | 6 | Ch66 `PLATFORM-EVALUATION-SYSTEM` |
| 14442 | PASS — Report Only | 5 | Ch22 为连接，不假称整个结构已有覆盖 |

## 1. 15167：Checkpoint 轨迹与量化 Probe 要独立验收

[exact-v1](https://arxiv.org/html/2604.15167v1) §3、§4、§5.1–5.2、Appendix A/B：154 个 Pythia-160M checkpoint 共享固定 Pile validation 32 个 `4×512` batch。INT4 是未经校准的 group128 非对称 weight-only 探针；INT8 使用 per-output-channel 对称方案，不能把差异完全归于 bitwidth。训练 fork 三种 recipe 各三 seed；OLI cool phase 的低位宽 gap 改善伴随浮点 PPL 代价，不能据此推荐通用学习率配方，也不能从相关曲线认定 flatness 或 kurtosis 是唯一原因。

实际比较 [Ch49](../../../../../books/part-05-inference-system/49-tensorrt-llm.md)“Post-quantization Recovery 必须同时通过质量与执行 Gate”及“一个 Anchor Artifact 支撑多格式，不等于一次验收覆盖所有格式”：已有逐格式 artifact/recovery 验收，但尚未明确训练轨迹上 float convergence 与固定 probe compatibility 的独立性。

最窄增量：保留浮点训练基线，同时绑定 checkpoint revision、probe 的 group/scale/zero-point、是否校准及评估样本，分别检查低位宽行为；浮点 loss 趋稳不是低位宽发布证书。探针适合隔离直接 grid compatibility，却不否定 GPTQ/AWQ/QAT 的修复分支，也不证明真实 kernel 加速。生产发布仍回到实际质量与执行 Gate，不把这里的受限探针升级为新全局审计流程。

## 2. 14847：事件触发交接与持续强模型轮询不同

[exact-v1](https://arxiv.org/html/2604.14847v1) §3.2、§4.1、§4.5–4.6：LRM 先 priming，SRM 当前 step 的低 perplexity 比例触发 LRM 重生成；连续 hesitation 触发后续有限步接管，再交还 SRM。trigger 只是经校准的 proposal，不是真值验证。作者用 8×RTX4090、SGLang 0.4.9、TP4/prefix cache、温度 0.6/top-p 0.95、默认 8192 tokens、每题 16 次；主动不评 latency，SMT token 占比不能替代端到端成本。ARC 的 .948 低于 LRM .957，不能采用全面无损说法。

§3.2 Eq3 定义 PPL=1/p≥1，但 §4.1 写 τ=.85，§4.5/Appendix D 又用 PPL<1.05。该局部配置矛盾必须保留；不得发布作者阈值为可执行默认，亦不据此否定全部实验。

实际 [Ch56](../../../../../books/part-05-inference-system/56-inference-scheduling.md) VOI/expensive-estimator 段已经决定是否打开 endpoint estimator，尚未明确 partial reasoning 中按事件改变 generator ownership。最窄补充是把当前 step/provisional prefix、触发校准版本、重生成/接管范围与返回点纳入交接，成本包含双模型状态、切换与误触发；若代理不可靠或共享前缀成本高，固定模型或持续 verifier 仍合理。不要照录不一致阈值。

## 3. 14164：监督 Artifact 可以记录局部生成责任

[exact-v1](https://arxiv.org/html/2604.14164v1) §2.1–2.2、§3.1–3.3、§4：在同一 committed prefix 上，student 生成 style span、teacher 生成 capability span；boundary predictor 检出跨界后 rollback，再交接，最终答案由 student 生成。teacher annotation 是标签来源，不证明 style/capability 是客观可分因果成分；跨 tokenizer 最后词裁切不保证分布等价。主实验 GPT-OSS120B→Qwen3-8B、32 H200、40K 上限；Qwen3-8B 的 GPQA 60.16→59.34 明确反驳全任务改善。

实际 [Ch29](../../../../../books/part-04-training-system/29-sft.md)“Distillation 不是 Teacher 越强越好”已讨论 capacity、representation、数据选择与行为回归，也有多 teacher supervision，但尚未描述样本构造阶段逐 span producer 与 rollback boundary 的接口。

最窄增量：既有全 teacher demonstration 在分布相容时仍简单；分布冲突时可按局部职责协作构造 SFT 样本，并版本化 producer、边界判断、撤销规则与最终答案来源。新增标注器偏差、跨词表截断及多模型生成开销；token 归属比例不等总生成成本，teacher/student 错误仍需独立验收。不是把新框架名称加入蒸馏清单。

## 4. 14191：函数匹配的中间表示可作为迁移桥

[exact-v1](https://arxiv.org/html/2604.14191v1) §3.1–3.2、§4/Table1–2/Implementation remarks：先拟合 normalized linear feature map，再把 phi(K)/phi(Q)、V、恒等状态转移及 normalization state 映射到 SSM；conv/gate 初始保持原中间算子，然后学习新动力学。这是匹配中间 linear operator，不是原 softmax 精确等价，也不是保留原 attention 的 hybrid。

必须纠正作者 notes 的“放开全部参数”：§3.2/§4 明确 input-output embedding layers 保持冻结，其余模型 finetune。Pythia1B、10B OWT tokens、8A100/BF16；扩展 scan state 2048 引起 serialization，作者约 12d9h、训练时间 >8×。Lambada 32.31<42.07、BoolQ 55.20<60.82；少 distillation tokens 不证明更低 wall-clock 或全面保持能力。

实际 [Ch22](../../../../../books/part-02-model/22-long-context.md)“从 Dense Checkpoint 迁移到 Hybrid State Model”已有按层 probe、保留难转层、distillation 与长上下文校准；未覆盖完整替换路径中的“先构造可映射中间算子，再初始化新状态动力学，最后受控解锁”。拟在该段补此并存分支，清楚区分匹配误差、能力回归和 kernel 成本；不稳定时保留 dense/hybrid，不把非 attention 路线宣称为免费迁移。

## 5. 14227：Temporal Admission 的 Existing Coverage 有实际正文

[exact-v1](https://arxiv.org/html/2604.14227v1) §3.1–3.3、§4、§5：Wikidata fact interval 与 Wikipedia revisions 构造相关却过期的 hard negatives，query-time relevance 不能由语义相似度或 publication recency单独推出。19 reranker 的离线反证有价值；Obsolete Ratio 的分母是排在正例之前的负例，200 样本人审 98.5% 一致不能代表全量真值。优化时效 instruction 在非时效子集有退步，不能称普遍支配。

实际 [Ch76](../../../../../books/part-07-agent/76-rag.md)“Temporal Retrieval 要在 Admission 前验证事实有效期”已经明确 query fact date/source validity/corpus revision 联合 admission，以及 metadata 缺失时 Unknown/权威历史回退。本文采用命题确已承载，而非仅有 RAG 主题。保留 benchmark 和 reranker 排序反证于日报，不再添另一时效机制段；ranking 不拥有证据 authority，亦无线上 SLO 结论。

## 6. 14262：配对能力轴与混杂边界已有覆盖

[exact-v1](https://arxiv.org/html/2604.14262v1) §3.2–3.5、§4.3、§6、§7.4/§8：390 相同 target 的 web grounding steps，交叉 4 种视觉 variant 与 direct/relational instruction，经重新渲染 bbox 和人工过滤；三款 Qwen2.5VL7B lineage 的 post-training 差异包含数据/阶段混杂。rank8 LoRA 6.5K/25K 退步是该 recipe 的反证，不是所有 PEFT 或 SFT 失败。

§7.4“不给空间表示 gradient”的字面说法不能接受：action CE 可经链式法则传播至可训练表示；没有直接空间监督与没有 gradient 是不同命题。实验自己也承认无法隔离所有根因，functional affordance 未单独测试。

实际 [Ch66](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) EvalSpec 已要求交叉任务轴、冻结 oracle/scorer/budget、避免换题型曲线与混杂因果外推，paired intervention 也在现有评价主线。这里采用的有限诊断合同已有覆盖；保留新 GUI 受限反例于日报，不因新 benchmark 再复制一般评价段。

## 7. 14339：保持可见内容、扰动位置索引的一致性适配

[exact-v1](https://arxiv.org/html/2604.14339v1) §2.2–2.4、§3.1/3.6–3.7/Table10：同 token 内容和 causal mask，仅 suffix RoPE index 跳跃；standard view 的 stop-gradient distribution 为 teacher，perturbed view 做 suffix reverse-KL，同时保留 CLM。这不是真实文档重排。Llama8B64K/16A100、Qwen4B256K/32A100、1000steps；额外 forward 约1.6× step 时间，CLM 多1.6×steps是 wall-clock 对照，不能称同训练 token。NoPE 29.5、chunk permutation 46.2 都低于 baseline47.9，任意位置扰动不成立。

实际 [Ch22](../../../../../books/part-02-model/22-long-context.md) Position Encoding、Effective utilization、“路线一”已有缩放/继续训练及位置切片评价，尚无保持可见性而显式训练跨 index 一致性的分支。拟紧接路线一补该路径：额外 teacher forward 与一致性偏差换位置稳健性，仍保留语义顺序、任务位置敏感性和短 context 回归；teacher 错误也可能被固化，必要时回退普通 CLM/已验证 scaling。不是提升最大窗口的直接 runtime 优化。

## 8. 14379：融合逆条件分布的闭式保证只针对局部 Surrogate

[exact-v1](https://arxiv.org/html/2604.14379v1) §4.1 Eq3、§4.2 Theorem1/Eq6–7、§5：共同 reference policy/同 KL 温度、各 base 为局部 step surrogate 的最优解、Gaussian reverse distributions、非负归一化权重时，其 weighted product 可用 precision 加权均值/方差闭合。不是参数平均、随机选模型，也不是原 terminal-reward RL 的全局最优证书；经验 DPOK base 没有证明满足所有最优假设。

实际 [Ch24](../../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) Conditional Guidance、采样路径 policy 与 source geometry 已有，不含这个局部目标下 posterior-fusion 条件。最窄补充是区分融合概率接口与融合权重，并保留 reference/variance/optimality 兼容条件。多个 base 每步都执行；无新训练不等无推理开销。受限 SD1.5、DrawBench color、新组合 prompts/32seeds、ImageReward/VILA；w=.8 的一项 reward .65<CoDe .66，不能照录全面支配或凭不完整执行配置比较生产秒数。

## 9. 14433：Ablation Baseline 改变被检验的因果命题

[exact-v1](https://arxiv.org/html/2604.14433v1) §3、§4.1–4.4、§8 必要 controls、§12 Compute：全层 register zeroing 混合内容替换与 off-distribution cascade；layer mean、匹配边缘 Gaussian、跨图真实 activation shuffle 保留任务质量，却改变内部表示。DINOv2/v2+registers/v3、ViT-S/B、224²、四任务、5K 图校准及 paired tests 只支持此受限 content-dependence 反证；shuffle 不保留全部联合因果结构，DINOv3 recipe 差异不能全部归 Gram loss。

纠正硬件 ND：§12 明确单 RTX4090 24GB，全实验 GPU 时间约12–15小时；precision/线上 concurrency/SLO 仍未完整给出。无需把这些总时长推广为逐请求性能。

实际 [Ch66](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)“Interpretability Graph 只有 Diagnostic Authority”保留 raw/paired patching/version，却没明确 zero/reference choice 改变干预对象。拟补：先问内容必要还是轨道存在必要，再比较 zero、matched replacement/resampling，分别记录质量、表示变化与分布偏移；多 controls 增加校准成本且可能错保结构，不能据可替换就删除 register。这个因果反证不是复制 Ch23 的替换架构讨论。

## 10. 14442：有贡献的受控结构反证仍可 Report Only

[exact-v1](https://arxiv.org/html/2604.14442v1) §2.2/§3、§5.8–5.10：Fast/Slow 共享 block、不同更新频率与 K-window TBPTT，在约1.2B/OWT1024 的受限训练比较中比 flat shared iteration 更稳。统一超参 MultiSeed 时 T-L4 胜 HRM，分别调参的等预算搜索又改排名；不能由 loss 差证明更强函数类别或排除所有优化因素。

每轮产生自己的 K/V，cache 为 O(Mnd)，equal-param 的 M12/L4 反而约3倍KV；共享参数不等共享每轮历史。实际 [Ch22](../../../../../books/part-02-model/22-long-context.md)“Local 与 Global Attention”后的循环 full-attention/KV 与 local/global解耦段已承载此系统反证。但两速模块/TBPTT recipe 不能被虚称整个机制 Existing；受限规模、数据、seed/grid 与非生产 kernel 暂不足推动通用架构判断。故保留具体方法和调参反证于日报，Report Only，不宣称无机制贡献，也不为新架构名添加孤立段。

## 结果与后续

本批七个窄 gap 提案、两个实际 Existing、一个 Report Only。必要的两处事实修正已通知作者；其他候选不在本批范围。作者后续落 Books 时必须检查上述窄命题真实存在、相邻衔接与来源绑定，才能把提案变为实际 Integration。本审阅不修改共享文件、不变更日期 owner、不替代整日独立验收。
