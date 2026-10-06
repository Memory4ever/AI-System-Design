# ProPer / CAFEDistill / FlowAct 必要证据提案

三项精确v1已核日期与准入，只必要方法/keyeval/directcounter。缓存为2601.IDv1-method/eval/protocol/equiv/standard-necessary.txt，均author actual读，不授复现。待root终裁，不自动Booksgap。

## 09926 ProPer — 拟5标准 + 直接sign反侧核 Only

[原文](https://arxiv.org/html/2601.09926v1)§4.1–4.4 Eq7/§5.1–5.2/7/A3/A5.1。主动不等越多补充越好→userexplicit/systemcovered/implicit gap分开，DGA候选+预算rerank+RGA保留baselineintent→GPT5 rubric同时惩overreach/underreach改变仅helpfulpairwin验收。选择机制是局部配方而非心理真值或安全authorization。Eq7 unmetexplicit cosine项是负号，正文声称鼓励alignment；不自行翻符号，明确不采用该式确保alignment/calibrated policy。只有independentscore rubric事实及局部模型report可采用，若root认为central必须依该式可Disputed。

Llama3.1/Qwen3 8B vs同backbone与CoT，MedDG/CodeContest/PWAB，judge GPT5每response独立0–5但同prompt同时给A/B，非盲真人或医疗validity。LoRA alltransformer rank8、7epoch/LR1e-4/batch8/bf16/max3248；GPU Not Disclosed。12conversation/domain multi-turn小质性。λ regime效应不证明缺知识causal/已校准uncertainty；作者承认judge风格/无用户长期state/无humantrust验证。保留exactEq7冲突位置与重开条件（作者selection实作/符号统一）但rubric局部实例Only无新Books/精确Existing。

## 10015 CAFEDistill — 拟5标准 + equivalence受影响核 Only或争议

[原文](https://arxiv.org/html/2601.10015v1)§4.1–4.4 Eq4–12/5.1/5.4.1–4/B2 Eq20–25/D1.1。多client×exit共用backbone冲突→last-exitteacher、浅层优先扩student然后depth内similaritygreedy、clientteacherQP及depthsharedweights→局部训练协调替代，不是earlyexit自身原创。所谓gradientproxy实际parametercos；μ/λ固定heuristic/R(t)=min2t/T不授因果梯度冲突已测或最优。

**中心equivalence限制**：Eq4为teacher预测分布KLweighted目标；Eq9平均classifier参数，B2 Eq22–25当输出φ(x)^T h线性后把它当KL概率。线性logit可平均，softmax probability一般不等参数平均输出，不能授exactKL equivalence/privacypreservation；不自行补activation。若只采用client-depth协调与实际localeval可Only，并显式暂停该保证；root决定是否中心Disputed。

CIFAR10Conv3/CIFAR100&TinyResNet18/AGNews4blockTransformer、Dir.1/.3、A10040G+Xeon6230R。precision/seed完整参数本包未采用数字。matchedextendedEENbaselines，crossclientKD+studentselectionablation局部，exitthreshold.6对应2.01accuracydrop/37.15%MACreduction，MAC不是E2E latency/通信或privacy保证；highμ拉无关teacher/lowμ退localKD反侧。成本需QP/teacher参数aggregate与共享backbone，每client personalizedheads；无Booksgap/精确Existing。

## 10103 FlowAct-R1 — 拟6标准Only

[原文](https://arxiv.org/html/2601.10103v1)短文§2.1–2.6/3。满上下文DiT长流约束→reference+longqueue≤3+shortrecent+3chunk×3latent fixedbuffer，fakecausal memory不能看denoising、训练generatedGT memory、shortmemory周期noise/repair→受限streamingcommit与累计error策略值得比较，不等真实永久identity/worldstate。

SeedanceMMDiT/VAE/Whisper16k25features、ARadapt/audio-motion/distillation CFGembed+3segments+DMD(teacher/fake初始化前阶段)/3NFE无CFG；FP8部分attentionlinear、framehybridparallel、kernelfusion、DiT/VAEasync联合而非单factor speedattribution。A100480p25fps/TTFF~1.5s作者报告，GPU数/network/长度/concurrency/latencyp分布和质量matched运行SLO Not Disclosed；3NFE≠总链路成本，periodicmemoryrepair/MLLM actionprior额外未量化。20人GSB研究fullaudio对LiveAvatar vs其他分别30s/5min截断，无单memoryrepair/MLLM因素受控消融；不能普遍indefinitequality/noerror或因果行为自然性。具体配方系统实例Only、未实际运行、无新Books/精确Existing。

