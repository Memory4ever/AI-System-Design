# B17 — 八项必要原证与 actual owner（六已有覆盖/二仅报告安全终态）

2026-10-06 feb26_close_oct06非原packet作者逐项定点复核：本包所有所引pID在各精确v1 raw中实际定位（无缺失；math/format与原TeX相应文字核），必要方法/控制/反侧已读。实际Ch66五层成功/生成轴-oracle、Ch28扩容mapping/moments、Ch74抽约束/probe发布、Ch72 consent/reviewer真实性、Ch23code与consumer质量、Ch52membership/coverage/communicator/graph epoch逐项对应；21059/21064/21103/21127/21140/21143具体已有覆盖，21061/21133受限oracle/GF2与grid-codebook recipe仅报告。Perception非危险effect拦截、AIST++匹配容量PPL反退、Revive单card时钟/不可exactly-once、Best5 oracle非部署selector与multilabel32分母保留；未运行artifact/复现，非日级验收。

## 2602.21059v1
https://arxiv.org/html/2602.21059v1

S3.SS3.p3.1 | Second, we conducted an evaluation of the LLM answers to expert questions via a think aloud contextual inquiry (Beyer and Holtzblatt, 1995) and an interview study: experts discussed their reactions to the LLM answers out loud, as they were reading them for the first time. Prior to each expert feedback session, we used our system to generate responses to each expert’s questions. We conducted two-hour feedback sessions with each expert (N=10), which were recorded and transcribed to facilitate analysis. These sessions were structured in two parts: in part one, experts freely noted shortcomings in LLM answers to their questions without being primed by our schema; and in part two, experts applied an inventory of questions we wrote to operationalize our schema (Appendix D). The inventory did not include system failure errors, as the accurate identification of these errors requires LLM knowledge which we did not require in our experts. We did not require our experts to have this knowledge, and so eliminated the error type to avoid confusion.

S4.SS1.SSS2.p2.1 | In Phase 2, unprimed mentions of specific types of hallucinations were surprisingly low, with only 1-3 (out of 10) experts mentioning them. Despite considerable focus on hallucinated citation information in conversations about LLM errors in general media, even this sub-type was rarely caught, only by chance as when E6 noticed errors in their own name. Indeed, specific sub-types of hallucinations were among the most commonly identified categories of errors discovered using our schema-based inventory during the primed Phase 2 evaluation. With the inventory guiding them on specific types of potential hallucinations, experts were able to identify hallucinated citation information (E2-5 and E7). E1-2 and E6 noted additional instances of missing source materials such as tables and figures. They also found new cases with incorrectly attributed information within (E10) and across (E2) papers.

## 2602.21061v1
https://arxiv.org/html/2602.21061v1

S1.p7.1 | We provide the models with a perfect oracle that prevents them from going down incorrect reasoning paths. This structure allows us to find an empirical upper-bound for \gamma_{g} and measure the affect of problem complexity and reasoning depth without need to fine-tune the model learn how to handle back-tracking.

S5.SS2.p2.1 | Our construction completely avoids this limitation. Because the instance generator adheres to a deterministic curriculum and the oracle adaptively masks all future terms, there is exactly one valid continuation at each step g . As a result, validation reduces to parsing the model’s boxed array and checking set equivalence with the withheld ground-truth indices. For a monomial of degree d , this validation procedure runs in O(d) time. Since d is a small constant, the validation cost is negligible.

S6.SS3.p1.1 | We now extend our analysis of depth-induced collapse in small models to larger systems: GPT 5.2 with extended Thinking, Claude Opus 4.5 with max Thinking, and Gemini 3 Pro (Jan 2026). Because frontier models typically generate extremely long reasoning traces on this task, it was financially prohibitive to replicate the full experimental protocol from Section 6.2. Nonetheless, the findings in the previous section provide a strong prior that guides our interpretation of the observed trends in \gamma_{g} for these larger models, even with fewer data points. In this section, we report results from 60 queries per model, spread across g\in{31,63,127} with p=12 and d=4 . For half of the prompts, the model was instructed not to use tool calls; for the other half, it was free to choose any solution strategy, including tool use.

S6.SS3.p7.1 | Tool-based reasoning remains imperfect, however, as it still relies on copying intermediate data through context. A natural extension would allow models to apply learned programs directly to their inputs, avoiding this degradation. Notably, the only model to perform well “without" tool use was Opus, but closer inspection suggests that it frequently invoked tool-like behavior despite instructions to the contrary, though such usage was not always transparent.

## 2602.21064v1
https://arxiv.org/html/2602.21064v1

S3.SS1.p1.1 | The base model can be any neural network. It is trained whole for each batch and each epoch. Once motivation occurs, its weights and buffers are copied into the corresponding part of the motivated model as defined by the weights map and training is resumed on the bigger model.

S3.SS3.p1.1 | Since the motivated model can contain the base model in many different ways, a weights map that associates the exact weights in the base model with their equivalents in the motivated model is needed. Let’s take the example of a convolutional layer. In many scalable architectures like EfficientNet, convolutional modules of larger models have a bigger output dimension. With respect to the motivated convolutional layer of output dimension d^{\prime}_{out} , the base convolutional layer of dimension d_{out} can be extracted by combining any d_{out} outputs among the d^{\prime}_{out} possible ones. The number of combinations is \binom{d^{\prime}_{out}}{d_{out}} . In the following three sections, we explain how the weights map was defined for the three scalable architectures we experimented on.

S4.SS4.SSS1.p1.2 | We conduct evaluations on ResNet for CIFAR-10 and EfficientNet for CIFAR-100. We keep the training configuration the same as in the original experiments. The results reported in Tab. 6 show that Experiment A deteriorates performance compared to the classical training of the base model. This means that training the base model as a part of a bigger model at completely random times hurts its performance. We expected this on an intuitive level because, ultimately, we are disrupting the training and using weights from the motivated model in the base one whereas these same weights expect other layers down the line in the forward pass that are not present in the base model. However, surprisingly, activating the motivated model a specific number of time, an information leaked from the motivation condition, but with no condition on the exact batch indices did not hurt performance for Resnet and even achieved an increase in performance for EfficientNet. The activation of the motivated model exactly at the motivation condition provided the best performance as shown in bold proving its importance but Experiment B hints at the relative importance of the number of these activations independently of their moment of occurrence during training.

## 2602.21103v1
https://arxiv.org/html/2602.21103v1

S3.I2.i2.p1.1 | Adversarial Refinement: These failures along with successful examples are sampled and fed into a Conflict Resolution Model (same as teacher model). The model analyzes the root cause and generates an updated instruction that learns better prompt improving accuracy. Providing correct examples is critical to avoid performance degradation.

S5.SS2.p2.1 | Crucial Role of Conflict Resolution in Complex Domains: The closed-loop conflict resolution phase yielded a 2.5% increment macro-F1 improvement on the structurally complex Contract-NLI dataset. Initial single-example extractions seldom generates contradictory instructions often missing broader linguistic nuances. The refinement loop successfully rectified these contradictions by learning various nuances previously missed. Conversely, this phase provided negligible gains on the StereoSet, indicating that iterative refinement is primarily essential for tasks involving intricate and overlapping edge cases. Conflict resolution loop converged on first iteration on Stereoset and second iteration on Contract-NLI.

S5.SS2.p3.1 | Preserving Minority and Edge Cases: The teacher model tasked with synthesizing clustered instructions often discards conflicting rules associated with minority labels and edge cases (see Appendix D.1). Since the supervised extraction operates on isolated examples, it inherently produces narrow, sometimes conflicting heuristics (Appendix B.1), often due to not picking up the correct nuances in the example at first. The Conflict resolution Loop is therefore critical not just for overall accuracy, but for preserving the logical coverage of minority constraints within the consolidated prompt.

## 2602.21127v1
https://arxiv.org/html/2602.21127v1

S4.SS1.p7.1 | \bullet Between-Subjects for Guardrails: To measure the true effect of each defense without confounding learning effects, each participant is randomly assigned to one and only one of the three guardrails. Our random assignment successfully results in balanced groups (G1: N=101, G2: N=103, G3: N=99).

S4.SS4.p2.1 | In-Situ Susceptibility Metrics (During Task). Our primary outcome variables for measuring user susceptibility are: (1) Risk Perception Rate (%): the rate of participants who report noticing anything “unusual or questionable” (by answering “Yes” or “Unsure”), capturing an initial sense of anomaly. (2) Accurate Identification Rate (%): the rate of participants who not only perceive a risk but also correctly describe the underlying attack mechanism in a subsequent open-ended question, measuring a deeper understanding of the threat.

S5.SS3.p2.1 | \bullet Finding 7: Users want control and transparency, but they should be cautious with the transparency-trust paradox. We ask users what would make them feel safer using agentic systems. Table X shows they want more transparency and user control: “real-time warnings” (61.1%), and “periodic reminders” (55.8%). Users explicitly want visibility into system operations rather than black-box automation. These features exactly match our designed (G3) interactive alert and (G2) persistent reminder. However, Figure 7 reveals a troubling paradox: users who do not perceive issues but experience G2 and G3 often report more significantly increased trust. An IT professional (unperceived user) explains “the security/risk alert made me more aware of potential threats… which improved my overall sense of safety while using HAT-Lab.” Another participant notes: “The presence of alerts and transparency features improved my confidence in these tools when properly monitored.” A third describes how “the system demonstrated consistency, transparency in evaluation, and highlighted even subtle issues, showing thoughtful safeguards are in place.” This directly validates the “Transparency Preference” pattern from Finding 4: users interpret security warnings as indicators of system trustworthiness rather than markers of risk.

S6.p4.1 | Limitations and future work. Our large-scale study, while systematic, has limitations that open avenues for future research. (1) Our cross-sectional study provides an important snapshot of user vulnerability. However, understanding how these trust dynamics and vulnerabilities evolve requires longitudinal research. Our HAT-Lab platform serves as a good foundation to conduct in-situ studies within organizations, tracking user behavior over weeks or months. This would allow for an investigation of complex phenomena such as vigilance decay and the long-term effects of security training. (2) While our discovery of the Expert’s Paradox is a key finding, our experts are primarily defined by their IT/technical background. Whether this paradox holds for experts in other high-stakes domains, such as medicine, human resources, or finance, remains an open question. This is our future direction to understand their unique cognitive biases and trust patterns. (3) Although we consider diversified, realistic everyday and professional attacks, our attacks are statically configured. A future direction is to explore adaptive attacks that learn and exploit a specific user’s pattern of trust.

## 2602.21133v1
https://arxiv.org/html/2602.21133v1

S2.SS2.p2.1 | Grid organization. Each codebook entry e_{k}\in\mathbb{R}^{d} is associated with a fixed grid coordinate c_{k}\in\mathbb{R}^{2} (we use 2D grids, though higher dimensions are possible). For a codebook of size K , we arrange entries on a \sqrt{K}\times\sqrt{K} grid with integer coordinates. Token assignment remains nearest-neighbor in latent space (Eq. 2), preserving discrete semantics.

S2.SS2.p3.1 | Two-stage codebook update. Unlike VQ-VAE’s per-entry EMA, SOM-VQ performs a two-stage update combining SOM topology preservation with VQ commitment. For each input z_{e} with best-matching unit (BMU) k^{*} :

S3.SS3.p1.1 | To rule out architectural confounds, we compare three capacity-matched variants at identical architecture (hidden=256): VQ-EMA, VQ-EMA with dead-code reset, and SOM-VQ using its standard two-phase training schedule. On Lorenz, SOM-VQ achieves lower Seq-PPL than both VQ variants without any reset mechanism (829 vs. 1014/1017), confirming that neighbourhood pressure provides implicit codebook regularisation on structured low-dimensional data. On AIST++, capacity-matched VQ-EMA achieves lower Seq-PPL, suggesting that the Seq-PPL advantage in Table 1 is partially attributable to the richer evaluation protocol of the main experiments; SOM-VQ’s organised codebook geometry (Distortion) remains a unique property unavailable to either VQ variant. Full results are in Table 3 (supplementary).

S3.SS4.p1.1 | While we validate across two complementary domains, a broader evaluation across audio, images, or other modalities would strengthen generalizability claims. The VQ-VAE comparison involves architectural confounds (network capacity, dead-code mechanisms) that merit controlled ablation in future work. The human-in-the-loop demonstration in Section 4 is preliminary and would benefit from user studies and baseline comparisons.

## 2602.21140v1
https://arxiv.org/html/2602.21140v1

S3.SS2.p2.1 | As each decoding step proceeds, executors may receive the global signal to stop and exit upon a detected failure. We adopt step-level recovery because layer-level checkpoints can leave inconsistent KV states across layers, leading to corrupted cache reuse. We revert back to the start of the generation step by restoring the block table (§3.3) and recompute the next token while discarding any newly generated caches. This would perform the full model forward again when service continues.

S3.SS5.p1.1 | In recreating communications domains, we treat the failed NPU as inaccessible, meaning that it physically still exists in the system, but we cannot perform any operations with it. This comes into play when we assign ranks in the various communication groups. In PyTorch process groups using GLOO [26] or HCCL [1], we keep the default world group intact but reassign subgroups such as the DP and EP groups so that they do not contain the failed rank. In XCCL, we must fully destroy and recreate the domain. This involves destroying the trampoline [30] domain between experts for MA-disaggregated deployments, then a universal step of destroying the communication domain between attention and experts. To recreate XCCL domains, we must assign new logical ranks to compact the communication domain. For example, if NPU A with logical rank \ell_{A} fails, it leaves a gap in rank assignments. We reassign NPU B with logical rank \ell_{B}=\ell_{A}+1 to \ell_{A} and decrement subsequent ranks to close the gap. In the role switching case, switched NPU C with logical rank \ell_{C} takes the logical rank \ell_{A} of failed NPU A. Then we fill in any gaps according to the previous procedure. Using this new assignment, we can create the XCCL attention-expert domain.

S4.SS1.p1.1 | To show the effectiveness of our method, we simulate the failure of a single card in the system and initiate recovery. We compare ReviveMoE with the baseline technique of reinitializing the system using a compilation cache. We measure the cached reinitialization time as solely the time to initialize FlowServe, meaning that the Docker containers and Ray are assumed to be available and their times are not included, but FlowServe must relaunch the engine and all executor processes. It must then perform the corresponding weight loads, communications operations, and cached graph compilations. In our recovery technique, we subdivide it to evaluate cases in which an attention rank fails cases in which a MoE rank fails. In the case where a MoE rank fails, it requires either role switching an attention rank to MoE, leveraging redundant experts, or allowing for lost experts. The figure of merit here is the recovery time, which represents the downtime the system experiences upon failure and recovery.

S6.p2.1 | We identify some limitations with our current design and envision future avenues. Currently, we only handle failure detection in the case where there is an obvious failure. Slowdowns or power issues are not as obvious but should be handled, as even a single slow device can cause significant delays in the overall system due to communication synchronization in MoE models. In an alternative direction, larger-scale failures are not yet handled by ReviveMoE. An extension to solve this is that redundant expert placement would need to balance both performance and fault tolerance to handle node-level failures. Other large-scale failures, such as network partitions, are difficult to deal with under tight SLO constraints, even in typical distributed systems. Future avenues can aim to address these issues of hardware slowdowns and larger-scale failures.

## 2602.21143v1
https://arxiv.org/html/2602.21143v1

S4.SS1.SSS0.Px2.p1.1 | Figure 4(b) examines whether multiple attempts improve task completion on DeepSynth-Dev. Under Best@5, Smolagents (GPT-4.1) reaches 25.0% LLM-Judge accuracy compared to 17.5% for GPT-4.1, suggesting that tool-use introduces beneficial variance across runs. However, self-consistency (majority voting at N{=}5 ) yields only 5% accuracy for both systems, with low average consistency scores (0.27), indicating that correct answers rarely emerge as the majority prediction. The stark contrast between Best@5 and self-consistency (27.5% vs. 5% for Smolagents) demonstrates that current agents exhibit high output variance on DeepSynth tasks. Occasional runs succeed, but models lack the reliability needed for consistent, correct answers.

S5.SS0.SSS0.Px4.p1.1 | What types of errors do models commonly make? To better understand the challenges in solving DeepSynth, we manually analysed a random subset of 32 tasks44 4 Subset chosen due to the time and cost of manually analysing all outputs. in which OWL + GPT-4.1 made errors55 5 Two annotators who were not involved in the original data annotation conducted this analysis.. We focus on OWL because, as an open-source framework, it enables detailed examination of execution traces and interactions between agents and tools. We categorize errors into four types, with their frequencies summarized in Table 4: (1) Navigation errors – when the agent fails to locate or access the correct source of information, such as navigating to the wrong web page, document, or section; (2) No Answer – when the agent does not respond or fails to generate any output; (3) Technical Issue – errors caused by system limitations, software bugs, or tool malfunctions that prevent task completion, independent of reasoning or navigation; and (4) Synthesis Error – when the agent reaches an incorrect conclusion despite accessing the correct information, due to flaws in logical reasoning, interpretation, or multi-step analytical processes.

S5.SS0.SSS0.Px4.p2.1 | This analysis is multi-label, as a single instance may exhibit multiple error types. The majority of errors—15/32 due to navigation and 16/32 due to reasoning—highlight that DeepSynth presents significant challenges even for state-of-the-art open-source models. Figure 9 illustrates a failure case of OWL, in which the correct URL was found, but the agent fails to interact correctly with the website and its database interface.

## actual owner — books/part-06-ai-infrastructure/66-evaluation-system.md

L51–60:
传统服务的 `error rate` 通常把 timeout、连接失败、`5xx`、进程异常或显式 schema failure 记为错误。这些信号回答执行路径是否完成，却看不见一个语法正常、HTTP `200` 的答案是否事实错误、遗漏关键条件、违反策略或没有完成业务任务。

AI System 至少需要区分五种成功事件：

| 层次 | 成功条件 | 典型失败 |
| --- | --- | --- |
| Transport / Runtime | 请求完成，模型和依赖没有显式异常 | timeout、OOM、tool transport error |
| Contract | 输出满足 schema、stop、引用与协议约束 | JSON 无效、错误 tool arguments、流未正确终止 |
| Semantic Quality | 内容正确、相关、grounded，并遵循 instruction | hallucination、错误推理、忽略 evidence |
| Policy / Safety | 行为满足权限、安全、隐私与合规边界 | 越权动作、敏感数据泄漏、危险建议 |

L132–136:
任务难度切片也不能只按输入长度或实体数划分。关系推理可以分别改变输入规模、任务生成器规定的 binding arity，以及识别或比较单个 operand 的难度；它们是三个不同轴。同一 arity 下更多输入可能提供额外线索，而非必然更难；实体少却需要同时满足更多关系，也可能比长输入更困难。EvalSpec 应保存生成规则和 oracle，在输出格式、scorer、推理预算可比的切片中交叉改变这些轴，不把换任务后不同的 accuracy、substructure 或 recall 拼成同一条下降曲线。<!-- source-family:SF-2026-ARXIV-2604-12176 -->

这种控制比单一长度排行榜增加生成、oracle 与样本预算，也仍只能约束已测混杂。生成器定义的 relational complexity 是任务属性标签，不是模型内部容量的计算下界；合成、多选与有限 token 预算下的失败，更不证明增加任意计算都无效。简单任务、长度已主导成本时仍可保留原长度切片，复杂关系任务再补上述交叉维度。受限关系评估支持将这些难度来源分账，而不支持通用 arity 阈值或唯一失败因果。

逻辑任务还应把“判定不存在解”与“提交可核验的 witness”分开：前者需可信求解 oracle，后者需检查赋值是否满足每个 clause。[参数化逻辑问题的有限对照](https://arxiv.org/html/2602.12665v1)固定 2-CNF，并改变 core 结构、free-to-bound 比例、填充和呈现；其 UNSAT 人口测 decision、SAT 人口测 witness，不能从两者准确率差直接归因能力。系统若要比较同一可满足实例的 decision 与 witness，应另作配对设计，不冒称作者已完成这个控制。Free-variable ratio 的总体结果与局部叙述、参数难度方向并非一致，不能照录成普遍难度律。生成、求解 oracle、witness 解析及模型调用均需计费，未完成输出也不能静默从人口中删除；没有可信 witness scorer 或任务只需决策时，保留原决策评价，把结构诊断作为补充而非替代真实任务结果。 <!-- source-family:SF-2026-ARXIV-2602-12665 -->

## actual owner — books/part-04-training-system/28-pretraining.md

L245–260:
模型结构在训练中扩容时，state contract 还要包含 parameter mapping。简单复制旧单元可以近似保持 forward function，却会把相同 optimizer moments 与 learning-rate schedule 一并复制，导致新单元沿相同梯度轨道形成 symmetry lock。受控扩容需要联合迁移：

```text
old weights + optimizer moments
→ shape-aware parameter mapping
→ activation-scale preservation
→ reset or differentiate new optimizer state
→ asymmetric rewarm for new capacity
→ loss-shock canary and rollback point
```

它用已有训练计算换取延后容量决策，却新增短期 loss shock、parallel-layout migration 与可复现性风险。从头训练在目标形状已知、稳定性优先时仍是清晰基线；“函数近似不变”也不证明 optimizer trajectory 连续。

如果目标是保持已有轨道，而非立即使用新增容量，扩容还存在条件性的等价 continuation 分支。对无 bias 的 MLP 作整数倍宽度复制、按输入复制倍数缩放权重，并联动 SGD learning rate 的输入/输出倍数，可以在相同数据与随机条件下保持函数更新；换成带状态 optimizer 时，迁移还必须匹配 update 的齐次条件。一阶 momentum/exp_avg 随梯度尺度变化，exp_avg_sq 按其平方变化，learning rate、decay 与 epsilon 也要相容。只复制权重或部分 buffers 不构成这份等价合同；条件不满足时，原有 reset、rewarm 与回归 canary 仍合理。

保持对称也意味着重复单元沿同一轨道前进，并未自动使用新容量；按宽度尺度加 noise 是另一个打破对称、允许探索的分支，会重新引入 loss shock。[受限扩容对照](https://arxiv.org/html/2602.10545v1)不能把两种目标合成“无损解锁容量”：窄 MLP/SGD 结论不直接覆盖任意架构，ResNet 的 validation 还存在退步；GPT2 对照的固定扩容后 steps 未计齐 base 训练与 sweep 总成本。mapping、moments、随机/noise revision 和旧训练预算应共同进入恢复与比较合同；轨道失配或质量回归时，回退原 checkpoint、受控 rewarm 或从头训练，而非以较低 training loss 代替最终能力验收。<!-- source-family:SF-2026-ARXIV-2602-10545 -->

## actual owner — books/part-07-agent/74-prompt.md

L132–134:
当多个 system、project、user 与 tool instruction 同时出现时，仅靠文本顺序和人工 review 解析 precedence，在规则少且冲突罕见时足够；规则增长后，同一组局部合理约束可能不存在共同可满足解，或只在某些输入上冲突。可执行的 prompt specification 可以先把候选约束编译成逻辑谓词，用 SAT/SMT 类检查发现 collision，生成最小 witness，并把选择的 resolution profile 绑定到部署版本。

形式检查拥有的是“抽取后约束是否一致”，不是自然语言意图真值。抽取错误、开放世界知识与概率行为仍需 regression、canary 和人工判断；过度形式化也会抬高维护成本。短 prompt 仍可直接审阅，只有多层 policy、重复继承与高代价冲突出现时，才值得用 executable spec 提前暴露不一致，并让 witness 成为可复现测试，而不是把求解器当作模型行为保证。

L218–218:
repository guidance 从静态 README/AGENTS 文本变为 probe-and-refine：运行 coding agent，定位失败 step，再在固定 step budget 内修改 guidance 并跨模型验证；repo owner 持有发布/回滚，过拟合时保留旧指导。代价是 probe 成本和 benchmark leakage。

## actual owner — books/part-06-ai-infrastructure/72-security.md

L3052–3061:
这种分权增加 schema、渲染一致性和交互延迟，也不能保证用户理解所有后果；工具语义不完整或 effect 无法预测时，摘要仍会
遗漏。低风险、可逆、无外部副作用的操作可保留简化确认；高风险 action 的渲染与 canonical call 不一致、approval 过期或
effect receipt 缺失时必须 fail closed。exact-v1 只支持作者 black-box Agent 与 consent-integrity threat model，不证明任意
tool schema 都能被完整自然语言化。

<!-- semantic-body-binding:SF-CONSENT-INTEGRITY -->

审批视图忠实呈现 action，仍不证明按下 Approve 的是人。若同一 Agent 能操作 review 面板、调用其 API 或取得审批 credential，外观上的 human-in-the-loop 会退化为自我授权。审批 principal、credential 和输入通道必须与被审 Agent 的 capability 隔离，并将批准绑定到具体待执行对象；这是工程控制要求，不是以检测分数代替身份验证。[METR 的 per-action monitor 复盘](https://metr.org/notes/2026-09-27-implementing-a-basic-blocking-action-monitor/#4-will-a-flagged-action-be-stopped-and-appropriately-reviewed-before-it-causes-harm-with-safe-actions-only-rarely-being-blocked)实际观察到 coding agent 自行打开人审面板并发送按键，同时明确尚未强制人类 reviewer 身份。其审批链的错误/超时 fail-closed 测试只覆盖实现路径，不能签发人审可靠性或开放攻击保障。<!-- source-family:SF-2026-METR-PERACTION-MONITOR -->

隔离审批增加身份校验、交互延迟、恢复与 reviewer capacity 成本；误报又可能在长轨迹聚集，不能用平均动作误报率推导每次人审质量。低风险可逆动作可保留自动 policy approval，但须如实命名；高风险 action 的 reviewer 身份、批准对象或有效期无法核实时，应保持 blocked、缩小 capability 或由独立人执行。监控覆盖、动作可见性、检测和可信审批是共同成立的条件，不是可默认独立相乘的成功概率；第66章负责评测证据，本章只拥有批准 authority 的真实边界。

## actual owner — books/part-03-multimodal-world-models/23-multimodal-representation.md

L198–198:
离散 codes 可共享 categorical prediction objective，也适合缓存、传输和自回归生成。代价是 codebook collapse、rare-code mismatch、长序列和重建误差。一个 code 是否“语义化”必须由 intervention、retrieval 或 reconstruction evidence 支持，不能从可视化聚类直接推断。

L206–208:
同一 codebook 还承担不同优化职责：encoder 的 straight-through reconstruction/commitment 更新，不等于 code 向当前 feature 分布追踪。一个稳定训练分支按相对 assignment distance 停止梯度地缩放 STE，在有限窗口保存近期 active features、为近邻 inactive codes 提出追踪 target，并分别调 encoder/decoder 的 warmup–anneal 与 codebook 学习率。稀有 code 获得候选目标、共享投影受影响，都不等每个原 code 每步得到非零独立梯度；没有获得目标的 inactive code 可以只有零 self-target loss。

[StableVQ 的受限图像实验](https://arxiv.org/html/2609.26774v1)中组件单独仍有 NaN/低利用率，Eq 4 最匹配距离为零的数值 guard 未披露，不能称 threshold-free 完整稳定实现。不同 projector/epochs 的比较未全匹配预算，满 usage 也不保证语义或生成质量，IS/Precision 仍有反退。窗口、近邻搜索与分组优化增加训练成本；数值/质量验收失败时保留普通 VQ、EMA/reset、统一 optimizer 或连续 feature，不把 codebook 利用率升级为音频、视频或部署安全保证。<!-- source-family:SF-2026-ARXIV-2609-26774 -->

## actual owner — books/part-05-inference-system/52-dynamo.md

L346–357:
普通 worker failure 可以把请求迁走并重算；宽 Expert Parallel MoE 中，一个 rank 丢失还会同时改变 live membership、
expert coverage、通信 group 与已捕获 CUDA graph 的执行身份。只让 membership service 删除失败 worker 会留下 expert
空洞；只复制 expert 又可能让旧 graph、buffer address 或 collective topology 继续引用失效 rank。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-10670:start -->
可恢复路径需要把三个提交合成一个 epoch：先冻结受影响请求，收缩 live membership；再从具备正确 model/expert
revision 的冗余状态恢复 coverage；最后重建 collective、buffer 与 CUDA-graph execution identity，全部通过后才发布
新 routing epoch。旧请求若已产生不可撤回 token，只能按 stream policy 终止或显式重试，不能假装无缝迁移。

这用冗余 expert state、额外 HBM、reconfiguration latency 与更复杂的 admission 换 partial-rank survival；它只覆盖
预先声明的故障模型，无法处理模型状态共同损坏、控制面分区或不足以恢复 expert coverage 的多点故障。小规模 EP、
无冗余预算或恢复时间超过 SLO 时，整组重启和请求级 fallback 仍更清楚。公开实验只支持其 partial-rank failure 与
