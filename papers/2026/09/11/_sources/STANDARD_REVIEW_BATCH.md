# Standard Source Review Batch — 2026-09-11

**审阅范围：** arXiv:2609.10657、2609.10658、2609.10723、2609.10863、2609.10976、2609.10993、2609.11127  
**审阅时间：** 2026-09-11（Asia/Shanghai）  
**审阅状态：** 7 / 7 标准审阅完成  
**写入边界：** 本文件只记录证据审阅；不修改 Candidate Denominator、Daily README 或 Books。

## 日期、版本与访问核验

七项材料均以 `arxiv.org/html/<id>v1` 的 exact-v1 正文为审阅对象，正文无需以摘要或后续 revision 代替。对应 primary category 的 arXiv `new` 列表均显示 `Showing new listings for Friday, 11 September 2026`，且七个 ID 均位于该批次：2609.10657 与 2609.11127 位于 `cs.AI`，2609.10658、2609.10863 与 2609.10976 位于 `cs.LG`，2609.10723 位于 `cs.CV`，2609.10993 位于 `cs.CL`。因此本报告使用的 first-public time 是 Friday batch 的 `2026-09-11T08:00:00+08:00`，而不是 abs 页所列作者提交时间。

访问时逐一检查 exact-v1 HTML 与 abs 页，七项均未出现 `withdrawn`、`withdrawal`、`retracted` 或 `retraction` 标记。该结论只表示 2026-09-11 本次访问时未见撤回/撤稿状态；未来若 arXiv 状态改变，应按最新状态重新打开对应材料家族。

## 1. [Quantifying the Memorization-to-Generalization Transition](https://arxiv.org/html/2609.10657v1)

**身份与评分：** arXiv:2609.10657v1；`2 + 1 + 2 = 5`；标准审阅完成。

- **问题：** 既有 grokking 工作解释了过参数化网络为何可能在先记忆后突然泛化，却缺少“在给定 data fraction、width、learning rate 与 weight decay 下何时跨越边界”的定量条件。
- **机制：** 作者在两个模运算任务上扫描 384 个两隐藏层 ReLU MLP 配置，将达到 95% 测试准确率的首个 step 定义为 `T_grok`，对 297 个成功 grok 的 run 拟合 `T_grok ∝ H^-0.27 D^-2.04 η^-0.50 λ^-0.64`。论文进一步把 weight decay 视为压缩高范数记忆解的动力，并以 memorization 到 generalization 之间的 weight-norm trajectory 描述经验 phase transition。
- **关键对照与评价：** 实验覆盖 addition mod 113、division mod 97，三种 width、四种 data fraction、四种 learning rate、四种 weight decay；356 个 run 完成、59 个在 150K steps 内未 grok。作者报告 base log-linear fit `R²=0.732`，加入交互项后 `R²=0.821`，并用 threshold sensitivity、right-censored Weibull model 和少量 seed-variance 检查稳健性。每个主配置只有一个 seed，20 个 norm-tracking 配置中仅 14 个具有非平凡 grokking gap。
- **收益：** 论文把“更多参数通常更强”的笼统叙事拆成 step、FLOPs 与 regime probability 三个不同问题；在该受控网格内，data coverage 与 regularization 对 generalization onset 的影响显著强于 width，为训练异常诊断提供了可证伪的条件关系。
- **代价与 failure mode：** 强 weight decay 或更高 learning rate 并非无条件收益；28 个高 learning-rate、低 weight-decay 配置发散，width 虽减少 steps 却提高每 step FLOPs。把 `T_grok` 当作连续量还会受到 150K censoring、阈值定义和初始化噪声影响。
- **适用边界：** 两个模运算任务、全批训练、小型 MLP、AdamW 与有限离散超参数网格；没有 Transformer、自然语言、预训练数据混合、分布式训练或 production SLO。论文自己把 phase boundary 和 norm threshold 标为 conjecture。
- **证据位置：** §2 给出任务、网格、单 seed 与 censoring；§3、Eq. (1)–(2)、Table 1 与 interaction model 给出拟合；§4–§5 给出 phase boundary 与 norm trajectory；§7 和 Appendix A–D 给出限制、阈值/seed 检查与可证伪预测。
- **证明 / 未证明：** 证明了在该实验网格中存在稳定的条件相关关系，并支持 norm compression 与 onset time 同步；未证明这些指数、`λ≈1` 边界或 norm ratio 是架构无关定律，也未证明 weight decay 单独因果地产生 LLM 的一般化跃迁。

## 2. [GEOSTEER](https://arxiv.org/html/2609.10658v1)

**身份与评分：** arXiv:2609.10658v1；`2 + 1 + 2 = 5`；标准审阅完成。

- **问题：** 固定向量或单步 activation steering 会同时改变 activation direction 与 norm；即便使用 norm-preserving rotation，固定轨迹仍难以适应输入相关、非线性的 activation distribution。
- **机制：** GeoSteer 先将选定层/位置的 activation 归一化到单位球面，用 contrastive activation 训练 nonlinear Polynomial Count Sketch probe；推理时将 probe loss 的梯度投影到球面 tangent space，执行多步 geodesic update，再恢复原 activation norm。控制权从单个预定义方向转为“由当前 activation 与冻结 probe 共同决定的局部方向”。
- **关键对照与评价：** 在 Falcon-7B、Mistral-7B-v0.3、LLaMA-3.1-8B、Qwen2.5-7B 上，以 UltraFeedback、TruthfulQA、RealToxicityPrompts 测 helpfulness、truthfulness 与 detoxification；与 RepE、ITI、CAA、MiMiC、Linear-AcT、ODESteer 及三种 norm-preserving baseline 使用相同单层 intervention protocol，主表平均五次运行。ablation 比较 step count、总 steering strength 及 linear/RFF/PCS objective。吞吐实验在 4×A100 40GB 上对三种 backbone 报告约 0.9% 平均 overhead，但未披露输入/输出长度、batch、concurrency、precision 与 SLO，不能把该数字外推为部署开销。
- **收益：** 在论文的三项 primary metric 与四个 7B–8B backbone 上均优于所列 baseline；多步局部方向允许沿曲线路径调整，同时通过构造保持 activation norm。PCS 对照支持 nonlinear objective 比 linear objective 更适合该 steering contract。
- **代价与 failure mode：** 需要有标签的 desired/undesired activation、额外 probe 与生成期间的逐 token 梯度/多步更新；总强度过大仍会损害生成质量。保持 norm 不保证语义局部性、安全性或不产生跨属性副作用，错误 objective 还可直接把系统导向有害行为。
- **适用边界：** 只比较兼容 single-layer inference-time steering 的方法；没有多层 controller、SAE feature integration、长上下文稳定性、闭源模型或 adversarial/safety evaluation。benchmark evaluator 与 prompt 选择仍属于实验合同的一部分。
- **证据位置：** §3、Eq. (8)–(21) 与 Algorithm 1 定义 state owner 和 geodesic control flow；§4 Table 1 给出跨模型结果，Figure 2、Table 2–3 给出 ablation 与吞吐；§6 明确 SAE integration、安全与 misuse 限制。
- **证明 / 未证明：** 证明了在选定模型、层位与 benchmark 上，adaptive spherical trajectory 可改善这些评价指标并严格保持 activation norm；未证明 activation 位于语义正确的全局 manifold、norm preservation 足以保持模型能力，也未证明该 controller 在部署分布上安全可靠。

## 3. [AcFlow](https://arxiv.org/html/2609.10723v1)

**身份与评分：** arXiv:2609.10723v1；`2 + 1 + 2 = 5`；标准审阅完成。

- **问题：** frozen text-to-image DiT 的 prompt interface 难以连续控制 style strength，也难以可靠删除 prompt 中已有概念；既有 activation/parameter edits 多依赖固定方向或 per-concept fitting。
- **机制：** AcFlow 在 frozen DiT 的单个 single-stream block 上只接管 image-token residual state，用 concept text、denoising noise level 与 flow time 条件化一个 backbone-matched velocity field。每个 denoising step 重新从当前 activation 启动 Euler integration，integration horizon `T` 是连续 control knob。训练时以同一噪声下的 target-prompt denoising velocity 作为 teacher，对 source-prompt + controller 输出做 velocity distillation；同一 field 在一个 task family 内跨 concept 共享参数。
- **关键对照与评价：** 主实验是 FLUX.1-dev、512×512、28 denoising steps、guidance 3.5、block 16、训练 `T=1/N=3`。MegaStyle 采用 family-disjoint split，以 released style encoder cosine 与 CLIP content similarity 衡量 style-content frontier；还提供超过 1,000 个 concept 的 suppression qualitative cases、block/step ablation，以及 Z-Image portability 和 NSFW suppression appendix。参数适配 baseline 需要 per-style fitting，而 AcFlow 是 shared controller，因此固定 operating point 与能力接口并不完全同构；概念删除主要是定性证据。
- **收益：** 在所列 high-style-alignment 区间形成更好的 style-content trade-off，并能在 held-out style family 上响应新的自然语言 concept description；`T` 把离散开关扩展为连续 operating-point 控制。
- **代价与 failure mode：** 需要额外训练一个 FlowBlock，并在每个 denoising step 执行多次 field evaluation；step 数增加并不单调改善效果。更强 horizon 会继续降低 content alignment，概念 suppression 可能伴随 object position、pose、scene layout 与 composition 漂移。
- **适用边界：** 证据主要来自 FLUX.1-dev 的 style task；硬件、precision、端到端 latency、并发和 production SLO 未披露。held-out 是训练 family 外的 concept，不等同于开放世界组合泛化；未提供对删除完整性与 collateral damage 的充分量化。
- **证据位置：** §3、Eq. (1)–(11) 定义 image-token state、velocity field 和 distillation data flow；§4 Table 2、Figure 3–6 给出 trade-off 与 held-out/qualitative 结果；§5 Table 3 给出 block/Euler ablation；§6 解释 token/noise-level adaptivity；§7 明确 composition limitation；Appendix A–C、F–G 给出 portability、训练预算和完整结果。
- **证明 / 未证明：** 证明了 shared conditional field 在给定 backbone 与数据划分上可以提供连续、activation-dependent 控制；未证明概念被因果删除、非目标语义得到保持，或该机制比所有 per-concept/parameter adaptation 在相同资源与接口合同下更优。

## 4. [Flow Duality and Source Geometry for Categorical Generation](https://arxiv.org/html/2609.10863v1)

**身份与评分：** arXiv:2609.10863v1；`2 + 1 + 3 = 6`；标准审阅完成。

- **问题：** continuous flow matching 与 discrete flow matching 通常被当作两套独立构造，continuous source law 也常被视为中性初始化；论文追问 one-hot categorical target 经 argmax 投影后究竟诱导什么 discrete path。
- **机制：** 在 product、coordinate-permutation-invariant、无 tie mass 的 continuous source，以及 `X1` 在给定 `X0=argmax(Z0)` 后与 `Z0` 条件独立的 lifted coupling 下，continuous convex interpolant 经 position-wise argmax 形成 discrete convex-interpolant conditional path。continuous source 的 pairwise-gap distribution 决定 effective coefficient `k_t`：Gaussian source 随 vocabulary 增大而延迟，bounded uniform 由 support width 控制，centered negative-exponential 的表达式不显式依赖 vocabulary size。
- **关键对照与评价：** 核心证据是 Lemma 3.1–3.3、Theorem 3.4 及 Appendix A/B 的证明与 source-coefficient 推导。经验部分只有一个 10K-step OpenWebText single-run pilot，比较 Gaussian、centered negative-exponential 与一个 shifted uniform operating point，并以 generative perplexity 和 unigram-entropy surrogate 组合 plug-in KL；另有 vocabulary-two 的 toy learned-flow trajectory。
- **收益：** 将 source distribution 从实现细节提升为路径设计变量，解释了相同 continuous schedule 为何可能在不同 vocabulary/source geometry 下对应不同 token transition timing；也提供 continuous 与 discrete categorical flow 之间可检查的接口条件。
- **代价与 failure mode：** duality 依赖 argmax-compatible lifted coupling、位置乘积分解、对称 source、无 ties/threshold atoms 与 coefficient matching；任一条件破坏都不能直接沿用定理。bounded source 还可能在 continuous endpoint 之前令 discrete coefficient 已达 1，使含 `(1-k_t)^-1` 的 velocity 需要重新限定区间。
- **适用边界：** 定理覆盖条件路径而非任意 learned marginal transport；不包含 optimal transport、consistency、mask-source 的一般证明，也不解决实际大模型的训练稳定性或 sample quality。pilot 是短训练、单 run，硬件及大部分系统条件未披露，plug-in KL 使用 unigram entropy 代替 joint sequence entropy。
- **证据位置：** §1 给出问题与假设；§3.1 Theorem 3.4 / Eq. (23)–(29) 给出 duality；§3.2 Eq. (31)–(35)、Figure 1–2 给出三类 source coefficient；§3.3 Table 1 给出受限 pilot；§3.4–3.5 区分 learned marginal trajectory 与 conditional theorem，并说明 reverse lift/mask 边界；Appendix A/B 给出证明。
- **证明 / 未证明：** 在列明假设下数学证明了 argmax pushforward 的离散条件路径形式及 source-dependent coefficient；没有证明某种 source 在训练后的大语言模型上普遍更好，10K-step 单点结果也不足以建立生成质量排序。

## 5. [Phases in a Class of Associative Memories via Hidden Neurons](https://arxiv.org/html/2609.10976v1)

**身份与评分：** arXiv:2609.10976v1；`2 + 1 + 3 = 6`；标准审阅完成。

- **问题：** polynomial-load dense associative memory 与 exponential-load softmax attention 长期由不同数学工具描述，因而难以在同一架构内判断 storage scale、retrieval stability 与 crosstalk statistics 分别由谁决定。
- **机制：** 论文使用 Krotov–Hopfield bipartite `class H`，把 hidden neurons 作为 retrieval order parameter。visible Lagrangian 通过 visible entropy 决定给定 crosstalk 下的 retrieval stability；hidden Lagrangian 决定 storage scale 与 disorder statistics。polynomial hidden nonlinearity 对应 polynomial load 与 central-limit crosstalk；softmax hidden layer 对应 exponential load，并通过 copy representation 映射到 random-energy-model counting，产生 paramagnetic、condensed 与 frozen phases。
- **关键对照与评价：** Models A/C 在 replica-symmetric ansatz 下得到 phase diagram 与 zero-temperature capacity；两者共享 crosstalk moment，但 visible entropy 导致 Ising 与 spherical retrieval 行为不同。Model B 以大偏差/极值统计分析 exponential load，温度通过离散 attention reassignment 破坏 retrieval。证据是统计力学推导、closed-form capacity 与数值 phase boundaries，不是 LLM benchmark 或真实 attention trace。
- **收益：** 把 Hopfield、higher-order associative memory 与 softmax attention 组织为同一架构的两个设计轴，明确“稳定性 owner”与“容量/噪声 owner”不同；这比把 attention 的内容寻址能力简单等同为高容量 memory 更精确。
- **代价与 failure mode：** 高阶 polynomial interaction 虽改变理论 load scale，但 crosstalk 高阶矩的 factorial growth 会压缩实际 retrieval region；exponential load 下典型 Gaussian pattern 只保持 metastable，且升温以量化 reassignment 而非平滑 overlap 下降的方式破坏 retrieval。
- **适用边界：** Models A/C 使用 replica symmetry；未检查 AT stability，spin-glass 与低温边界可能受 RSB 修正。`k>2` 与 Model B 采用 hidden-neuron adiabatic limit；finite two-temperature dynamics 未覆盖。Model B 的 hidden-sector fluctuation correction 在 exponential load 下并不小，能否吸收进 reference measure 仍未解决。
- **证据位置：** §I–II 定义统一架构与 hidden order parameter；§III 给出 Models A/C 的 RS capacity、crosstalk 与 phase diagrams；§IV 给出 softmax Model B 的 copy/REM 分析；§V 汇总两条设计轴并明确 RS、adiabatic 与 hidden-sector-correction 限制；Appendix B/C 给出推导细节。
- **证明 / 未证明：** 证明了指定 statistical-mechanics model 在所列 ansatz/limit 下的 phase 结构；未证明生产 Transformer 的 learned attention 服从相同 equilibrium、Gaussian-pattern 或温度假设，也未给出可直接用于 LLM serving/training 的容量公式。

## 6. [Distribution-aware Language Neuron Identification](https://arxiv.org/html/2609.10993v1)

**身份与评分：** arXiv:2609.10993v1；`2 + 1 + 2 = 5`；标准审阅完成。

- **问题：** 以 activation 是否大于零计算每种语言的 activation probability，再用 entropy 找“language-specific neuron”，会丢掉负值区域、分布形状及语言之间的关系；相同 positive rate 可能掩盖明显不同的 activation distribution。
- **机制：** DLN 对每个 GLU neuron 估计逐语言 activation density，计算所有语言对的 overlap-coefficient matrix，再以最小化最大跨簇 overlap 的二分聚类选出较小 language set。低 overlap 的 neuron 被分为 single-language neuron 或 multi-language neuron。evaluation 通过 mean-patching 干预选定 neuron，把“统计分离”连接到 target-language NLL、任务准确率与生成语言切换。
- **关键对照与评价：** 主实验覆盖 Llama-3.1-8B、SmolLM3-3B-Base、七种语言，以及 WIKI/FLORES 两个 held-out corpus；按 neuron count 匹配 LAPE/LSN baseline，报告 on-target/off-target `ΔNLL`、Belebele、MGSM 和生成语言识别。displacement-matched random control 只产生约 1% 的 SLN effect；site 对照比较 GLU gate activation 与 gate-up product，appendix 另扩到 Llama-3.1-70B 与 Aya-23-8B。
- **收益：** 识别出 positive-rate 方法看不见的 negative-region neuron，并把中文等信号从错误的 single-language 缺失解释改写为 multi-language cluster；干预的 on-target damage 集中而 off-target damage 较小，说明 ranking 不只是大位移或 neuron count 的副产物。
- **代价与 failure mode：** 需要保存大规模逐语言 activation distribution 并估计密度/overlap，threshold 以模型内 percentile 设定，跨模型绝对值不可直接比较。mean-patching 在 gate-up product 处因跨语言 mean spread 更小而整体变弱；cluster 选择也可能把连续、多簇结构压成较小一侧的二分集合。
- **适用边界：** 主证据只有七种语言，且限于带 SiLU-GLU FFN 的 autoregressive Transformer；未验证普通 MLP 或不同 activation architecture。对 neuron 的干预证明 functional sensitivity，不等同于该 neuron 单独、单义地“存储一种语言”，也不证明识别结果可提高跨语言任务能力。
- **证据位置：** §3 与 Figure 2 定义 overlap matrix、clustering 和 selection；§4 Figure 3–5、Table 1–2 给出 SLN/MLN、held-out corpus 与 downstream intervention；§5 Table 3–5 给出 set-difference、displacement 与 GLU-site controls；`Limitations` 明确语言、架构与 z-site 边界；Appendix D–G 给出扩展模型和逐语言结果。
- **证明 / 未证明：** 支持 full-distribution criterion 在指定模型/语言/干预下更准确地定位具有选择性 causal effect 的 neuron；未证明这些 unit 是稳定的语言知识 owner、跨训练版本可复用，或对实际 multilingual serving/training contract 产生普遍收益。

## 7. [KuaiRP Series Role-playing Models Technical Report](https://arxiv.org/html/2609.11127v1)

**身份与评分：** arXiv:2609.11127v1；`2 + 2 + 2 = 6`；标准审阅完成。

- **问题：** full-parameter domain SFT 能注入角色/world knowledge，却使 tool calling、reasoning 与 instruction-following 等 general agent capability 遗忘；温和的 LoRA 或 on-policy reverse-KL signal 又可能因为 student 很少采到 domain token 而学不到知识。
- **机制：** pipeline 先以模板、用户行为模拟和 reverse-profile filtering 构建 SFT 数据，再用 format/length/diversity 三个 binary reward 的最小值做 GRPO。恢复阶段让“原始 base model”作为 student、SFT+RL domain model 作为 teacher：Stage 1 在完整数据上用较温和的 OPD-PG 迁移 style/format，Stage 2 只在 world-setting subset 上用 top-k forward-KL GKD 注入知识。CDD 用当前 token 之前的累计、detached top-k divergence 指数衰减后续 token loss，并设 floor，避免严重 prefix drift 后的 teacher distribution 与噪声梯度仍获得相同权重。
- **关键对照与评价：** 基于 Qwen3 8B/4B 比较 Base、SFT、RL、OPD1、OPD2 w/o CDD、OPD2 w/ CDD；Table 5 用 BFCL v4 测 general agent/tool calling，Table 6–7 用 TRACEbench 测通用/领域 role play，Table 8 测安全拒答与 domain knowledge，领域角色结果报告五次运行。RPF 与 CDD 有消融，但 benchmark、数据生产及部分 teacher 使用自有或商业模型，不能视为完全独立评价。
- **收益：** 阶段结果支持“domain adaptation 与能力恢复是两个不同 control objective”：SFT/RL 改善领域与输出约束后，OPD1 将 BFCL 拉回接近 base，OPD2 再恢复部分 world knowledge；CDD 相比无 CDD 主要改善 domain-character consistency 的均值/波动与知识注入，而不是所有指标统一上升。
- **代价与 failure mode：** 需要同时维护 base student、domain teacher、student on-policy rollout、teacher top-k logprob 和两套数据分布；top-k GKD 不是完整 KL。CDD 会在 divergence 累积后衰减所有后续 token，若 divergence 代表有效 alternative path 而非 prefix failure，可能压低有价值监督；weight floor 又保留了一部分已漂移 signal。hard-min reward 容易形成稀疏奖励，并把 evaluator loophole 当作优化目标。
- **适用边界：** 结论来自角色扮演、特定 world-setting、Qwen3 4B/8B 与自建 evaluator。作者在 Qwen3.5-9B 上未复现同等提升，说明收益依赖 base capability 与 teacher/data freshness。单 24GB GPU、低 latency 与极低部署成本只作为目标/结论陈述，正文未给出完整 model size、quantization、hardware、length、batch、concurrency、latency 或 SLO 合同，不可据此作 serving 结论。
- **证据位置：** §3 及 Table 1 定义 SFT data/recipe；§4、Eq. (1)–(8)、Table 2 定义 hard-conjunction reward；§5、Eq. (9)–(17)、Table 3–4 定义 OPD、prefix drift 与 CDD control flow；§6 Table 5–8 给出逐阶段/消融结果；§7 定义自建 evaluation contract；§8 给出 Qwen3.5 failure 与 subjective-quality 缺口。
- **证明 / 未证明：** 论文支持这套两阶段 distillation 在其 4B/8B role-play pipeline 中恢复部分通用能力并保留领域能力；未证明 CDD 优于所有 prefix-drift 方法、适用于开放域或更强 base model，也未证明 benchmark 排名、低成本部署或安全拒答能外推到独立生产分布。

## 批次结论

- 七项均完成与 5–6 分等级相称的标准 Source Review；没有把摘要、标题或作者结论直接当作机制事实。
- 七项均属于 2026-09-11 Friday batch，且本次访问未见撤回/撤稿标记。
- 所有性能与规模数字均绑定到论文实际披露的模型、任务或硬件条件；未披露的 precision、length、batch、concurrency、latency/SLO 等没有补推。
- 本文件没有替代 Daily 的 Books Decision；它只提供逐篇的机制、评价合同与证明边界，供 reconciliation owner 更新日报时使用。
