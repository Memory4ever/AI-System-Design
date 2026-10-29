# 00959：决策统计分解不能冒充模态真值或因果电路

仅06-03补Jun02；当前AGENTS/研究与Report合同、Sources使用/Daily/arXiv/恢复、Prompt、ROADMAP及本日停点已重读。R62完整v1题摘/联合Jun02日证复用，不第三日期层。[exact-v1](https://arxiv.org/html/2606.00959v1)本次实际读§2–5全部核心机制/主要评价、C完整限制、D配置及H.1–2/H.4–6直接对照与反侧；没有读全部引用、其他无关附件/像素/代码或复现。[当前abs](https://arxiv.org/abs/2606.00959)有Aug08 v2，所见无withdrawn/removed/erratum提示；只采用v1，不倒填后版/把版本号当重要修订。访问2026-10-25 BJT。

## 必要机制、证据及边界

§2的Y是候选选项上的模型预测，不是正确标签。给定经验输入人口与模型soft概率，BROJA/PID把联合信息分为两路unique、redundancy、synergy；tri-modal则以文字T为条件，估I(Y;V,A|T)，不是把三路无条件独立，也不是T拥有事实裁定权。BATCH是借用的Sinkhorn coupling估计后端，原文贡献是模型决策分布的诊断/条件化应用，不借成熟PID本身给分。每模态token mean pooling/共享空间、候选softmax与raw option mass<.3时uniform gating共同限定估计；Gauss moment-matched embedding masking只是近似unimodal条件，不等原生缺模态模型。统计依赖不是内部head/circuit因果或真实grounding，C明确承认这些限制。高synergy不证明答案正确、未被估计输入没信息或都应加强fusion。

§3–4对20个VL模型/6benchmark，greedy温度0；同模型移除图像测accuracy差，表1按20模型的Spearman只是关联，模型家族/benchmark人口有相关性，不授独立训练实验因果。MUSIC-AVQA三分层上VITA1.5/Qwen2.5Omni3B/7B共3模型；video/audio跨样本shuffle保边际却破对应，支持此扰动下视觉依赖较强，不是唯一内部“visual hegemony”因果。4.3层间profile可定位诊断，不能从信息上升直接宣称该层发生唯一离散融合；换指令的例子改变需回答的语义，不是单纯保义paraphrase，不能排除任务需求变化。原文也只称model–benchmark profile，不是数据集/架构固有属性。

§5把BATCH local additive scores先clip非负再归一，故个样本SR/SC是代理分数，不再是全局非负PID分解的严格逐样本真值。50随机batch contexts均值、预测熵减少的fusion potential、先选择language-shortcut再选gap且二者不重叠，形成3/.5/1权重；不是直接把低synergy都upweight。H.1 matched counts Kg389/Ks746，MMBench training3000，不用eval样本做profiling/selection/train是作者披露的partition条件，未独立验证数据。H.2同LoRA rank16/alpha32/dropout.05/2e-5、cosine5%warmup/effectivebatch16、末20%层、3seed；Random每seed3权重分配共9runs。有限matched-weight/random、difficulty和ablation对照支持此选择信号有额外作用，不证明是唯一fusion机制或普遍最佳训练recipe。

T3/H.4 Qwen2.5VL7B PID对Uniform在MMStar64.3 vs62.0，但MMMU53.5 vs54.0、PMC52.7 vs53.0反退；H.5 Gemma3-12B的MMStar54.3低于Uniform56.2、甚至Base54.8，MMMU54.1远低于Uniform59.3。不能照录“limited effect +.3”来掩主要退步（+.2 MMBench也不等所有任务+.3）。H.6加权5x令PID更高却MMStar低于3x，MMMU更低；高测得synergy非单调质量目标。Seed-stratified bootstrap是作者协议，不额外授样本或训练独立性。具体GPU、precision、输入image/audio长度、完整训练steps/总费用和serving并发/SLO在本必要域未披露，Not Disclosed；不是速度benchmark，不能从轻LoRA或training-free analysis称零训练/零成本。编码/三条件推理、估计器训练/50contexts、选择、LoRA与新旧任务回归都付费。

## 评分、actual owner与最小稿

正式拟2+2+2=6：两路unique/redundant/synergistic与文字条件化的决策诊断，跨模态表示→当前消费者/训练选择边界，可复用但仍MCQ/估计约束；不借PID数学成熟性、20模型数量或所有生命周期给分。现`MULTIMODAL-REPRESENTATION` Ch23“任务贡献与当前可靠性不能共用一个Gate”实际完整任务/当前质量两sensor、reliability整段与直接TC-LIA上下文已读；“Modality domination”完整既有head/probe/冲突取源组也已读。现文有可读不等消费/真值、静态与sample reliability分责，但没有这份条件决策分解与训练重权后依赖/任务收益不一致的具体分支，不因topic近判NC。Ch22长上下文及Ch24生成开头/交接实际读，唯一Ch23，不另写Ch27/66同机制。

拟在完整“可靠性估计器拥有的是 policy hint…”段之后、直接完整“对图文问答，sensor还可以先检查…”TC-LIA段之前插入以下两段（若独核找到具体充分承载则NC，不造diff）：

> 要把任务贡献测得更细，还可在固定模型与样本人口上，把候选答案分布与两路输入之间的统计信息分成独有、冗余和协同部分；音视频任务则先以文字指令为条件，再分解两路感官输入的增量。这回答的是“当前决策怎样依赖输入”，不是“哪一路内容为真”。[受限PID诊断](https://arxiv.org/html/2606.00959v1#S2)用模态token汇聚、选项概率和噪声mask近似缺模态条件，因而必须绑定输入表示、题型、候选集、mask与估计器；层间曲线和跨样本shuffle可补功能验证，却不能仅凭较高协同量定位因果电路或批准答案正确。相同总信息量或总准确率也可能对应不同的模态依赖，不能用它们替代这份分解。
>
> 这类诊断也可只在训练侧改变样本权重：先用有限预测分布估计局部shortcut与fusion-gap代理，再对不重叠样本分别降权、升权，而不是部署时直接改变事实信任。[匹配权重数量的有限LoRA对照](https://arxiv.org/html/2606.00959v1#S5)支持部分推理/grounding收益，但知识题可退步，Gemma的主要切片也劣于普通微调；更高测得协同量不保证更好任务质量。多条件推理、估计器训练、选样、适配与全部回归都有成本；估计不稳、原任务或净预算退步时，保留uniform训练、简单模态消融与独立可靠性/事实核验，不把统计profile变成通用融合配方。<!-- source-family:SF-2026-ARXIV-2606-00959 -->

当前首次必要/正式拟分/actual owner与两段PRE待独核，未写Books/Report、不预I/DAY。支持与直接反侧已足，即停止附件扩读。
