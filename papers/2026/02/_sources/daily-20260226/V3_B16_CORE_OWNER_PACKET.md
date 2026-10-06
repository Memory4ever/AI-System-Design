# B16 — 八项必要原证与actual owner（七已有覆盖/一仅报告安全终态）

2026-10-06 feb26_close_oct06非原packet作者逐项定点读取本包所指原v1 paragraph方法/关键反侧及实际Ch72 1241–1255/600、Ch26 508/548–558、Ch23多层读出、Ch30模块/rank验收、Ch66 199/244/3671–3673。20999/21013/21015/21042/21044/21045/21054具体已有覆盖，21035否定读出局部recipe仅报告；sim-eval GT action、any-frame ASR、train-gate/infer-gate、minimal-support人口、38→26 exclusion、attentionknockout和s非归一化prob反侧保留。未运行artifact/复现，非日级验收。

## 2602.20999v1
https://arxiv.org/html/2602.20999v1

S3.SS1.p2.1 | Attacker’s Capabilities. The attacker aims to generate a video with unsafe content using the target model \mathcal{M} . We assume a black-box setting, where the attacker has no knowledge of, or access to, the parameters or internal gradients of \mathcal{M} . The attacker has full control over the input image-text pair and can submit crafted inputs to observe the generated video. Specifically, the attacker is given a safe reference image I_{safe} and an unsafe text prompt P_{mal} with malicious intent y_{mal} , and can modify the image and text prompt to construct adversarial variants.

S4.SS2.p2.1 | Impact of Visual Symbols. We evaluate a variant, VII w/o visual symbols, to isolate the contribution of explicit spatial grounding provided by the VIG module. In this setting, we remove all rendered visual symbols (i.e., bounding boxes and arrows) from the image. Crucially, to ensure a fair comparison, we also rewrite the typographic description P_{desc} into a purely semantic form P_{plain} by stripping away references to visual symbols (e.g., changing “piercing the skier inside the red box” to “piercing the skier”). The results indicate that removing these visual anchors significantly degrades attack performance. On PixVerse-V5, the ASR drops precipitously from 83.5% to 32.5%, rendering the attack nearly as ineffective as the text-only baseline. This confirms that the explicit grounding provided by visual symbols is essential for guiding the model’s generation. Furthermore, on Veo-3.1, removing visual cues causes the Refusal Rate (RR) to spike from 21.5% to 51.0%, suggesting that visual symbols also play a pivotal role in distracting safety mechanisms from recognizing potential risks.

A8.p2.1 | Post-Generation Defenses. VII is inherently ineffective against post-generation safety mechanisms (e.g. output-level safety classifiers), as it is designed to bypass pre-generation static safeguards and induce the explicit emergence of malicious intent during video generation. Consequently, successful attacks inevitably produce videos containing overt unsafe spatiotemporal content, which can be readily detected by standard post-generation classifiers. However, relying primarily on post-generation moderation entails non-negligible practical drawbacks [13, 22, 14, 62]. Video diffusion is computationally expensive, and detecting violations only after full sampling can lead to considerable computational overhead and increased latency in real-world deployments. Therefore, while post-generation filters remain an important last line of defense, proactively identifying and mitigating visual instruction threats prior to generation is highly desirable for building efficient and deployable I2V systems.

## 2602.21013v1
https://arxiv.org/html/2602.21013v1

S3.SS1.p2.1 | Next, we describe our proposed scratchpad in more detail. The scratchpad is updated by the VLA when necessary, i.e. when a sub-task is successfully completed by the VLA. Specifically, the VLA predicts a special update token that triggers the next description to be included in the scratchpad as seen in Alg. 1. In practice, the model is trained to recognize the completion of the current sub-task and produce a special token which triggers the description to be updated in the scratchpad. Thus, conditioning our proposed scratchpad lends the model a language defined memory. Since the descriptions can be a detailed description of the environment state, the scratchpad acts a flexible and extendable memory, allowing the model to perform memory dependent tasks. An example instantiation of a scratchpad augmented VLA can be seen in Fig. 1.

S5.SS2.p3.1 | We also experiment with a recurrent VLA (R-VLA) with Mamba as backbone to compare against a model with inherent memory. While R-VLA usually performs better than T-VLA, we note that T-VLA+Scratchpad is able to match R-VLA performance on average even surpassing it on some tasks. This shows that language scratchpad is flexible enough to endow strong memory capabilities to stateless VLAs. We also note that recurrent VLAs despite having inherent memory capabilities also see an average improvement of 11% when trained with scratchpad. In Fig. 4, we show the average trajectory length of the tasks in ClevrSkills. As we can see, generally increasing task length leads to a higher performance improvement with scratchpad in R-VLAs with exception of Rotate-Restore which see no performance improvement as the task requires low-level fine-grained temporal memory which can not be aided by a scratchpad.

S5.SS3.p3.1 | We show performance of our T-VLA and T-VLA+Scratchpad on MemoryBench in Table I. Prior baselines evaluated on MemoryBench all take scene point clouds as input and are driven towards very precise manipulation whereas we just take front RGB and wrist RGB images as input. As we can see, scratchpad significantly improves performance over the stateless baseline. We also note that since we take RGB images as input as opposed to 3D point clouds, our model struggles to press the button and majority of the failure cases stem from this failure mode. Therefore, we also report a relaxed evaluation criteria (denoted by “sim-eval” in Table I) where if the VLA gets close to the button, we execute the ground-truth action to press that button instead of taking the action predicted by the VLA and continue the rest of the trajectory. Doing so leads to our model getting a 100% success rate on the Put-Block-Back task showing that our model is able to perform both temporal and spatial recall perfectly.

## 2602.21015v1
https://arxiv.org/html/2602.21015v1

S2.SS2.SSS0.Px2.p1.1 | To ensure experimental consistency, we unify the collected puzzles, spanning diverse structures and dynamics, into standardized interactive environments. We implement these environments using two complementary toolchains: Unity and a lightweight 3D Python engine. Unity is used for puzzles with complex interlocking mechanics (e.g., Kongming and Lu Ban locks), where precise control over kinematic constraints and contact interactions is required. In contrast, stacking-based spatial packing tasks, which involve simpler physical dynamics, are implemented in 3D Python for greater development efficiency. To provide a uniform interaction interface across tasks, we adopt a color-hinted control scheme: each object is assigned a distinct color, and the color–object mapping is exposed to the agent as additional metadata. The agent specifies objects by color when selecting and manipulating pieces. This design avoids introducing an additional action controller (as in VLA-style setups) that could confound the evaluation. Finally, we provide multi-view observations, allowing agents to inspect the scene from different viewpoints and reducing failures due to occlusion.

S3.SS5.p2.1 | Table 3 shows that one-shot performance is uniformly lower, which further highlights gains of interactions. This indicates that CHAIN cannot be reliably solved by pre-computed reasoning from a single view. For Puzzle, one-shot accuracy collapses to 0.0\% for all evaluated models, while interactive accuracy reaches 3.1\% , suggesting that even modest success requires iterative constraint discovery rather than a fully inferred disassembly plan from the initial observation. For Stacking, interaction is even more critical: GPT5.2 drops from 31.2\% (interactive) to 9.1\% (one-shot), Gemini-3-Pro shows the same drop ( 26.0\%\rightarrow 9.1\% ), and Claude-Sonnet-4.5 decreases from 18.2\% to 10.3\% . Aggregated over all tasks, the All Avg accuracy decreases sharply in one-shot. Overall, these consistent gaps support that CHAIN genuinely evaluates closed-loop physical-structure reasoning under evolving feasibility constraints, rather than one-shot recognition or static plan synthesis.

A1.SS1.p2.1 | (2) Current evaluation mainly reports Pass@1 due to high multi-step interaction cost. We primarily report Pass@1 (single-attempt success) as our main success metric. This choice is partly driven by the evaluation cost of closed-loop interaction: each episode involves a non-trivial number of rounds, and we cap the interaction budget at 30–60 steps per instance. We recognize that interactive tasks can exhibit run-to-run variability; however, our preliminary analysis in Section 3.6 suggests that multi-sample evaluation (e.g., Avg@4) and Pass@1 show consistent trends, indicating that the variance is not dominant in practice. Looking forward, once sufficient API budget is available, we will report more robust best-of- K results (e.g., Pass@4) following the standard multi-run protocol.

## 2602.21035v1
https://arxiv.org/html/2602.21035v1

Sx4.SSx3.p10.1 | To ensure stable optimization, the mask is fixed to \mathcal{M}=1 during training, allowing gradients to propagate consistently. It is only activated at inference time to selectively suppress negated alignments.

Sx5.SSx1.p2.1 | Trained on the CC-Neg dataset (Singh et al. 2025) (188K images, 376K captions), CLIPGlasses achieves 96.56% accuracy on the in-domain CC-Neg-val set. While slightly below CoN-CLIP’s 99.70%, this reflects a deliberate design choice to prioritize generalization over overfitting. The benefit becomes evident on the cross-domain Neg-COCO-MCQ benchmark (Alhamoud et al. 2025), where CLIPGlasses surpasses CoN-CLIP by 8.81 percentage points (34.51% vs. 25.70%).

Sx5.SSx3.p6.1 | Effect of Dynamic Repulsion Weight. We observe substantial performance degradation upon removing this module (32.82% accuracy decrease) underscores its critical importance. This ablation result motivates a deeper investigation into the underlying mechanisms driving its contribution. We hypothesize that the module’s primary function is to dynamically calibrate repulsion strength according to the linguistic intensity of negation. To test this hypothesis, we evaluate the predicted \lambda values across a controlled spectrum of negation intensities. Using Qwen2.5-72B (Yang et al. 2024), we generate four recaptioned variants for 500 randomly sampled CC-Neg examples, each corresponding to four distinct levels of negation strength: strong (“no”), moderate (“not any”), weak (“appears to be absent”), and weakest (“may not be”).

## 2602.21042v1
https://arxiv.org/html/2602.21042v1

S4.SS2.p1.3 | where \mathcal{L}^{t}_{\sup} is the supervised loss, M is the number of updated matrices, and \lambda controls sparsity. This design encourages the model to retain only the most critical update directions while pruning redundant ones, ensuring compact adaptation without extra inference cost.The complete training procedure is outlined in Algorithm 1. Through this mechanism, OmniOCR is able to efficiently adapt to the structural diversity across Tibetan, Ancient Yi, Shui, and Dongba scripts, while simultaneously mitigating catastrophic forgetting when learning sequentially across different minority languages. Moreover, by pruning redundant update directions and retaining only the most critical ones, the framework achieves compact adaptation without introducing additional inference overhead, making it both effective in low-resource scenarios and practical for real-world applications.

S5.SS1.p2.1 | The base model is initialized from the pre-trained RolmOCR[5]. We replace selected linear layers (self-attention projections and MLP layers) with the proposed Dynamic LoRA modules, which support dynamic rank adaptation. The initial LoRA rank is set to r=8 , LoRA scaling factor \alpha=16 . During training, the effective rank is adjusted via soft-shrinkage on rank weights, encouraging sparsity while retaining task-relevant capacity. To prevent overfitting, learned low-rank updates are merged back into the frozen backbone at checkpoint saving.

S6.p1.1 | Although OmniOCR demonstrates strong performance across diverse ethnic minority language datasets, several limitations remain. First, our experiments are conducted on four curated datasets (Tibetan numerals, Ancient Yi, Shui script, and Dongba script), which, while representative, do not cover the full diversity of minority writing systems. Many scripts feature richer structural variations, such as decorative glyphs, mixed phonetic–logographic properties, or highly context-dependent ligatures, which may expose additional challenges beyond our current evaluation. Second, while Dynamic LoRA significantly reduces the parameter footprint and improves adaptation efficiency, the training process still requires noticeable GPU resources and non-trivial memory usage. This may restrict deployment in resource-constrained environments or community-level digitization projects, where lightweight solutions are critical. Third, our study emphasizes recognition accuracy under benchmark settings, yet practical OCR systems must also contend with real-world issues such as document degradation, background noise, and complex layouts combining text, images, and annotations—factors that are only partially addressed in our current framework.

## 2602.21044v1
https://arxiv.org/html/2602.21044v1

S4.SS1.SSS0.Px3.p1.1 | To generate multiple reasoning paths, we first build a reasoning chain to a sampled depth, then pick an intermediate conclusion on the chain and expand it upward again using the same bottom-up procedure. Repeating this step produces a Logic DAG in which the goal is supported by multiple distinct premise sets. To ensure the ground-truth solution set is exhaustive, we assign a fresh atomic identifier to each newly introduced premise unless it is explicitly shared through an existing node, thereby avoiding unintended premise sharing and implicit extra paths.

S5.SS2.p3.1 | Divergent Thinking evaluates creativity and flexibility in discovering multiple distinct paths. This is measured by: (i) Diversity (Solution Recall), defined as R_{\text{sol}}=|\mathcal{S}_{Model}\cap\mathcal{S}_{GT}|/|\mathcal{S}_{GT}| , which quantifies the coverage of the solution space; (ii) Versatility (Family Recall), which reflects the agility to switch between distinct reasoning strategies; and (iii) Originality, which highlights the ability to identify rare paths by calculating the inverse frequency of a solution’s discovery across all models.

S6.SS2.SSS0.Px2.p1.1 | Despite near-saturated Success Rates for top models, divergent metrics remain markedly lower, revealing a gap between finding one valid reasoning path and enumerating many. This indicates that current models tend to concentrate on a limited subset of high-probability paths rather than systematically exploring diverse alternatives.

## 2602.21045v1
https://arxiv.org/html/2602.21045v1

S5.SS4.p2.1 | We report results from 26 participants after excluding data from 12 who did complete the study but their data was not valid. These 12 participants were excluded for the following reasons: (1) they took less than 10 mins to complete each task, without any interaction with the components of our systems; (2) they added gibberish text in their responses; and (3) their qualitative responses indicated that system latency had prevented them from engaging with the information (caused by load balancing issues in the backend). This exclusion process was conducted based only on feedback and task duration, without referencing our primary outcome measures, to avoid biasing the results.

S6.SS1.p1.1 | A paired t-test showed a statistically significant effect of the interface on subjective trust on the LLM. Participants reported significantly lower trust in LLMs when using PaperTrail compared to the baseline ( t(25)=2.61,p=0.015) ), with a medium effect size (Cohen’s d=0.44 ). This supports our hypothesis that claim-evidence annotations encourage more caution towards LLM use in scholarly settings. However, despite the reduction in trust, we found no significant difference in behavioral reliance between the two conditions ( W=146,p=0.313 ); nor in self-reported confidence ( t(25)=0.64,p=.525 ).

S8.p2.1 | Metrics and Measurement. First, our operationalization of reliance through edit distance may not fully capture the nuanced ways participants engaged with LLM assistance. The measure conflates various behaviors (from wholesale acceptance to strategic delegation), and creates a potential confound. Participants might maintain high textual similarity not from overtrust in the LLM, but from trust that PaperTrail would alert them to problems requiring intervention. Future work should develop more sophisticated behavioral measures that distinguish between passive acceptance and informed delegation. Relatedly, when reporting subjective trust using the TXAI scale, participants may not even have distinguished between the interface and the LLM. Component-specific trust measures will be important for future verification. Finally, we did not evaluate the quality of participants’ edited texts. While our focus was to capture behavioral differences, a quality assessment would help identify whether unsupported claims were removed, omitted information was added, and if the overall argumentation improved. Future work should include blind expert evaluation of output quality to complement behavioral measures.

## 2602.21054v1
https://arxiv.org/html/2602.21054v1

S5.SS3.SSS0.Px1.p2.1 | The results in Table 3 show that masking the ground-truth evidence region ( \text{IS}_{\text{GT}} ) yields higher AUROC than the blank-image baseline ( \text{IS}_{\text{blank}} ), indicating that fine-grained and semantically relevant visual content is crucial for VAUQ score computation. In contrast, random masking ( \text{IS}_{\text{rand}} ) leads to degraded performance relative to the blank baseline, suggesting that indiscriminate perturbations disrupt the model’s ability to extract meaningful visual cues. These findings highlight the importance of carefully selecting which visual regions to mask when estimating image-information utilization. Our method ( \text{IS}_{\text{core}} ) achieves performance comparable to the GT (Oracle) setting, demonstrating that our approximated masking region effectively captures the core visual evidence.

Sx2.p1.1 | VAUQ aims to support more reliable use of vision–language models by providing a lightweight, training-free self-evaluation signal. Such a signal may be useful for identifying potentially unreliable outputs and for supporting selective prediction or human review in practical deployments. At the same time, VAUQ is not a comprehensive safety mechanism and should not be treated as a definitive measure of correctness. We view it as a complementary tool that is best used alongside existing safeguards and human oversight, particularly in sensitive or high-stakes settings.

A1.p1.1 | We implement our method using greedy decoding with a maximum generation length of 128 tokens. For implementation efficiency, rather than modifying the raw image inputs corresponding to \mathbf{v}_{\text{masked}} , we mask the attention weights associated with visual tokens in \mathbf{v}_{\mathrm{top}} when computing \mathrm{IS}_{\text{core}} , following the attention knockout strategy geva-etal-2023-dissecting; kaduri2025s. The weighting parameter \alpha and the proportion of masked image patches K used to compute the VAUQ score are selected based on a held-out validation set, as described in Appendix E. The layer index range (l_{s},l_{e}) is chosen heuristically based on empirical observations, as illustrated in Figure 3. For all experiments, we report results averaged over three random seeds. All experiments are conducted using Python 3.11.11 and PyTorch 2.6.0 paszke2019pytorch on a single NVIDIA A100 GPU with 80GB of memory.

### 21035 原display公式TeX

L908: \mathcal{R}_{\mathrm{neg}}=\lambda\cdot\max\left(\exp(\theta_{T})\cdot\frac{q^{\top}k_{\mathrm{neg}}}{\|q\|_{2}\|k_{\mathrm{neg}}\|_{2}},\ 0\right)

L997: S=S_{\mathrm{base}}-\mathcal{M}\cdot\mathcal{R}_{\mathrm{neg}}

### 21042 原display公式TeX

L395: \Delta W^{t,m}=\sum_{i=1}^{r}w_{i}^{t,m}B_{i}^{t,m}A_{i}^{t,m}

L448: \mathcal{L}^{t}_{\min}:=\mathcal{L}^{t}_{\sup}+\lambda\sum_{m=1}^{M}\|w^{t,m}\|_{1}

### 21054 原display公式TeX

L711: \mathrm{IS_{\text{blank}}}=H(\mathbf{y}\mid\varnothing,\mathbf{t})-H(\mathbf{y}\mid\mathbf{v},\mathbf{t}),

L910: \displaystyle=H(\mathbf{y}\mid\mathbf{v}_{\text{masked}},\mathbf{t})-H(\mathbf{y}\mid\mathbf{v},\mathbf{t}),

L957: \displaystyle(\mathbf{x},\mathbf{y})=H(\mathbf{y}\mid\mathbf{v},\mathbf{t})-\alpha\cdot\mathrm{IS}_{\text{core}}

## actual owner — books/part-06-ai-infrastructure/72-security.md

L1241–1252:
安全边界应位于工具执行器：

```text
model proposes action
→ typed schema validation
→ policy and authorization
→ parameter/content validation
→ optional human approval
→ least-privileged execution
→ result filtering and audit
```


L600–600:
安全数据闭环还可由当前 policy 生成 adversarial candidates，再由独立 guard / outcome policy 筛选后进入训练。它能把静态红队集扩展到当前模型暴露的 failure frontier，却同时制造 self-confirmation 风险：generator 与 guard 若共享模型家族、prompt 或表示盲点，可能一致地把危险样本标成安全；只保留通过 guard 的样本还会隐藏 false negative。因而 generated sample、generator checkpoint、guard version、policy taxonomy、人工复核切片和最终 deployment gate 必须分开保存。该机制适合作为受控 data augmentation，不能取代 output-time enforcement 或独立 red-team evaluation。

## actual owner — books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md

L548–550:
这类 memory 仍是 model-owned、episode-scoped derived state：identity 必须绑定 policy revision、embodiment、episode、
reset boundary、observation frontier 与 compression rule。它不能覆盖 sensor observation，也不能继承 Agent Memory 的
跨 session ACL、provenance 与删除语义。curator 错误会固化 stale belief，长期 latent 还会增加训练 credit horizon、

L555–555:
“换一段记忆后动作变了”只能证明 policy 对历史敏感，不能证明它选中了该历史真正要求的动作。若要把 memory 宣称为控制证据，应构造当前观测、非记忆状态和随机种子相同、但真实历史不同且应采取不同行动的成对场景；交叉喂入两段历史后，同时测动作变化、对应世界中的正确性、物理结果和重复试验稳定性。此审计把 memory sensitivity 与 warranted choice 分开，尤其能暴露“记得过去却据此做错决定”。代价是成对环境和正确动作标签难造，离线可重放不保证真实闭环可重放；物理平台的操作误差仍须独立计量。Counterfactual Memory Audit 的证据只覆盖所述 Mem-0 场景和有限双臂实机，不证明通用机器人记忆有效或安全；无法构造配对时，应保留较弱的行为敏感性表述，并以实际任务结果另行验收。<!-- source-family:SF-2026-ARXIV-2609-27247 -->

## actual owner — books/part-03-multimodal-world-models/23-multimodal-representation.md

L101–103:
读出所需的信息也未必集中在固定的最后层接口。冻结视觉 encoder 后，可以从多个层分别取 CLS 与平均 patch summary，将这些层级表示作为 keys/values，由一个可训练 query 的 cross-attention 学习任务条件下的融合，再交给分类读出。这分开了两个选择：访问哪些层，以及在每层保留 summary 还是逐 patch 的空间细节；它不是重训 backbone，也不由 attention 热图证明原模型已经因果使用了某层。Layer、token 类型、normalization、维度补齐、preprocessing 与 readout revision 共同定义表示接口，不能由末层某个 probe 失配宣布所有最后层表示不足。

多层 summary 可减少读出端需要消费的空间 tokens，却增加中间特征提取/缓存、监督训练、容量与调参成本；平均 pooling 还可能丢掉定位线索。[受限 ViT 多任务对照](https://arxiv.org/html/2601.09322v1)中，细空间任务有末层 patch attention 更强的 slice，部分任务也更适合简单线性融合；主实验单 run 与局部 seed 检查不能授任意配置稳定性，单 query 融合也不采用文中二次复杂度宣传作为实测加速。任务只需末层语义、缓存成本过高或融合过拟合时，保留原 last-layer readout；需要空间细节时保留 patch-level 接口，并以相同训练/搜索预算重新验收。<!-- source-family:SF-2026-ARXIV-2601-09322 -->

## actual owner — books/part-04-training-system/30-lora.md

L215–217:
只适配 Q/V 与覆盖全部 Attention/MLP 会得到不同容量和 artifact shape。最优 rank 与位置依赖任务、数据、基座和预算，不能从 LoRA 名称推出。

Rank 也不等于任务“本质维度”的直接测量。训练成功只说明该配置足以形成某个有用 update，不证明所有任务更新都严格低秩。

L295–295:
为每个预算单独训练 LoRA 最清楚，却会产生多个不可共享的 adapter revision。若部署需要动态 rank，可让同一 adapter 的 ordered factors 形成 nested sub-ranks，并把训练目标和 artifact identity 绑定到可用 rank set；验收同时报告关键 rank 的单点质量与 rank–accuracy curve/AURAC，不能让平均曲线掩盖低 rank collapse。该路径减少多 checkpoint 成本，却依赖方向 ordering、任务分布和 kernel 支持；固定预算或某一关键 rank 不合格时，回退普通固定-rank LoRA。 [受限证据：arXiv:2605.07850v1]

## actual owner — books/part-06-ai-infrastructure/66-evaluation-system.md

L74–74:
某些任务无法为每个请求即时获得 ground truth，因此不能简单把语义错误重新编码成另一个实时 `error_rate`。平台通常组合离线标注集、规则与 deterministic checks、抽样 human review、judge、用户反馈和延迟到达的业务 outcome，并为不同证据保留 provenance 与不确定性。高风险 policy failure 还应作为 hard gate，而不是被大量正常请求在平均值中抵消。

L199–199:
能力测试也应区分“看见当前 state”与“知道环境怎样转移”。在相同环境和交互预算下，一组明确提供 transition rules、另一组要求通过行动与反馈推断这些规则，可以把规则给予后的推理表现与规则发现过程分开测量；可见 surface state 不等于 dynamics 已知。两组差距仍可能来自历史截断、信息披露或 prompt 的变化，不单独识别架构性的 induction ceiling。作者受限环境的 solvable 筛选、固定任务/trajectory、有限 human 对照及其一致性都限制外推，交互和配对运行也增加成本。规则本来是业务已知协议时，明确提供规则仍是合理基线；规则未知时保留 history/belief、可验证观察和探索预算，不能用一次低分宣称模型普遍没有归纳能力。<!-- source-family:SF-2026-ARXIV-2602-05843 -->

L244–244:
attention sensor 还可保留 aggregate mass 或 entropy 丢掉的位置变化：对当前生成 token 的 context attention 与 preceding-generation attention 分别按 token 顺序构成向量，以高通算子的输出幅值汇集各层、各 head，再训练线性 detector 判断 response 是否受到 context 支持。这是 token-position frequency，不是 wall-clock 频率，也不是高频即幻觉的因果定律。[原版本的算子与 high/low-pass 对照](https://arxiv.org/html/2602.18145v1#S3)支持这一受限特征分支，但部分任务仍弱于 mass-based baseline，QA 训练向 summarization/data-to-text 迁移也会失准；operator、cutoff、padding、标签、模型与阈值校准都属于 sensor identity。实验冻结 LLM 并 teacher-force 已有 response，不证明免费在线预警；提取多层 attention、训练及 validation 阈值都有模型访问与计算成本。context 支持也不等于独立事实正确或发布安全，访问不足、迁移漂移或告警不可校准时，保留简单 mass/entropy sensor 与独立证据核验，不让这一信号取得 effect authority。<!-- source-family:SF-2026-ARXIV-2602-18145 -->

L3671–3673:
长上下文回答可能最终正确，却引用了无关或错误 evidence path；也可能轨迹合理但终局合成失败。评测应分别保存 claim、自然 evidence trail、检索/工具事件与最终 verdict，让 scorer 只拥有对应层的判断权。这样提高诊断性，却增加标注和 trace 成本；低风险短答案仍可用 final-only baseline，关键结论则不能从答案正确反推证据链正确。

开放文本轨迹还可以先把公开参考 rationale 拆成 atomic units，再比较候选理由覆盖了哪些参考单元；但这先定义了一份新的测量人口，而不是发现模型内部真正使用的推理。拆分规则、人工筛选、参考集合、匹配器及其 reuse/阈值约束、输出与理由预算都应进入 scorer identity，不能让更长的理由或同一候选片段反复匹配制造无条件 coverage。[必要方法与反侧](https://arxiv.org/html/2602.04649v1)支持这一参考对齐分支；公开文本的一致性、与另一个 judge 的相关性不等人类事实真值或内部 faithfulness，匹配公式与提示实现尚未一致的子命题也不能用来认证奖励机制。工程上应定点人工核对拆分与匹配、同时保留 final verdict 和不匹配样本，这是测量验收推导而非作者已实现完整 guard。标注、匹配调用及更长 trace 均有成本；参考不可信、划分或匹配不稳定时，回退 final-only、可执行 oracle 或人工 evidence 审计，不让参考覆盖率替过程正确性自证。<!-- source-family:SF-2026-ARXIV-2602-04649 -->
